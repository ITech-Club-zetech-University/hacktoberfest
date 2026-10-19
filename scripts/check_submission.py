#!/usr/bin/env python3
"""
check_submission.py — Automated preliminary eligibility checker for
Hacktoberfest Hack Day Nairobi x iTech Club submissions.

PURPOSE & BOUNDARY:
This is a lightweight, preliminary administrative hygiene checker. It is NOT
an AI project judge, NOT an automated leaderboard, NOT a performance scoring
tool, NOT a plagiarism detector, and NOT a legal opinion on licensing. It does
NOT prove that Gemma generated any output or that code is legally compliant.
Its sole purpose is to flag baseline repository hygiene oversights before live
demos, giving organizers and student teams time to address administrative
issues.

CHECKED CRITERIA:
1. Genuine GitHub repository URL parsing (github.com and www.github.com only).
2. Repository public visibility (via GitHub API).
3. Open-source software LICENSE (validated against official OSI-approved SPDX IDs).
4. Root README.md presence.
5. README mentions Gemma (explicitly labelled as a WEAK SIGNAL only).
6. SKILL.md presence (mandatory for Challenge 1 / Track 1; informational for others).

STATUS CATEGORIES:
- ELIGIBLE (PASS): Passes all preliminary hygiene checks.
- NEEDS MANUAL REVIEW: Ambiguity or unverified metadata requiring human review
  (e.g., non-OSI SPDX ID, unasserted license file, missing Gemma mention in README,
  or 404 response that might be an un-flipped private repo).
- CLEARLY INELIGIBLE: Definitive failure of baseline requirements
  (e.g., invalid GitHub URL, confirmed private repo, or missing README/license).
- CHECK UNAVAILABLE: GitHub API rate limit (403/429) or network timeout.
  CRITICAL: Automated check unavailability must NEVER be treated as noncompliance.
  Organizers must inspect the repository manually in a browser.

EXIT CODES:
- 0: All checked repositories are ELIGIBLE (PASS).
- 1: At least one repository is CLEARLY INELIGIBLE.
- 2: At least one repository is NEEDS MANUAL REVIEW or CHECK UNAVAILABLE (none ineligible).
- 3: Command-line syntax or invocation error.

USAGE:
    python3 scripts/check_submission.py <repo-url> [<repo-url> ...]
    python3 scripts/check_submission.py --track 1 <repo-url>
    python3 scripts/check_submission.py --help

OPTIONAL ENVIRONMENT:
    export GITHUB_TOKEN="ghp_xxx"  # Raises GitHub API limit from 60 to 5000 req/hr
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

API_ROOT = "https://api.github.com"
DEFAULT_TIMEOUT = 15

# Exit code definitions
EXIT_OK = 0
EXIT_INELIGIBLE = 1
EXIT_REVIEW_NEEDED = 2
EXIT_USAGE_ERROR = 3

# Fallback set of standard OSI-approved SPDX license identifiers
# (used if scripts/data/osi-approved-licenses.json cannot be read)
FALLBACK_OSI_SPDX_IDS = {
    "0bsd", "afl-3.0", "agpl-3.0", "agpl-3.0-only", "agpl-3.0-or-later",
    "apache-2.0", "artistic-2.0", "bsd-2-clause", "bsd-3-clause",
    "bsd-3-clause-clear", "bsl-1.0", "cddl-1.0", "epl-2.0", "eupl-1.2",
    "gpl-2.0", "gpl-2.0-only", "gpl-2.0-or-later", "gpl-3.0",
    "gpl-3.0-only", "gpl-3.0-or-later", "isc", "lgpl-2.1", "lgpl-2.1-only",
    "lgpl-2.1-or-later", "lgpl-3.0", "lgpl-3.0-only", "lgpl-3.0-or-later",
    "mit", "mit-0", "mpl-2.0", "ms-pl", "ms-rl", "mulanpsl-2.0",
    "ncsa", "ofl-1.1", "osl-3.0", "postgresql", "python-2.0",
    "unlicense", "upl-1.0", "zlib",
}


def load_osi_approved_licenses(json_path: str | Path | None = None) -> set[str]:
    """Load the canonical set of OSI-approved SPDX identifiers.

    Returns a set of lowercase SPDX identifiers. Falls back to FALLBACK_OSI_SPDX_IDS
    if the data file is missing or unparseable.
    """
    if json_path is None:
        json_path = Path(__file__).resolve().parent / "data" / "osi-approved-licenses.json"
    else:
        json_path = Path(json_path)

    if json_path.is_file():
        try:
            with open(json_path, "r", encoding="utf-8") as fp:
                data = json.load(fp)
            ids = data.get("approved_spdx_ids", [])
            if isinstance(ids, list) and ids:
                return {str(item).strip().lower() for item in ids if str(item).strip()}
        except Exception:
            pass
    return set(FALLBACK_OSI_SPDX_IDS)


# Pre-load OSI identifiers
OSI_APPROVED_SPDX_IDS = load_osi_approved_licenses()


def parse_repo_slug(url: str) -> str | None:
    """Parse and strictly validate a GitHub repository URL into 'owner/repo'.

    Guarantees:
    - Hostname must be strictly 'github.com' or 'www.github.com' (rejects lookalike hosts).
    - Strips '.git' suffix and harmless trailing slashes.
    - Requires exactly two path segments: valid owner and valid repository name.
    - Returns None for invalid or unsupported URLs.
    """
    if not url or not isinstance(url, str):
        return None
    raw = url.strip()
    if not raw:
        return None

    # Handle URLs supplied without scheme
    if not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", raw):
        raw = "https://" + raw

    try:
        parsed = urllib.parse.urlparse(raw)
    except Exception:
        return None

    hostname = (parsed.hostname or "").lower()
    if hostname not in ("github.com", "www.github.com"):
        return None

    path = parsed.path.strip("/")
    parts = [p for p in path.split("/") if p]
    if len(parts) != 2:
        return None

    owner, repo = parts[0], parts[1]
    repo = re.sub(r"\.git$", "", repo)

    # Validate GitHub owner: 1-39 chars, alphanumeric and single hyphens, not starting/ending with hyphen
    if not re.match(r"^[a-zA-Z0-9](?:[a-zA-Z0-9]|-(?=[a-zA-Z0-9])){0,38}$", owner):
        return None

    # Validate GitHub repository name: 1-100 chars, alphanumeric, hyphens, underscores, dots
    if not re.match(r"^[a-zA-Z0-9_.-]{1,100}$", repo) or repo in (".", ".."):
        return None

    return f"{owner}/{repo}"


def _api_get(path: str, timeout: int = DEFAULT_TIMEOUT) -> tuple[int, dict | None]:
    """Perform a read-only GET request against the GitHub REST API.

    Returns (status_code, json_dict_or_none).
    Security note: GITHUB_TOKEN is read only from environment and is never logged.
    """
    url = f"{API_ROOT}{path}"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "itech-club-hacktoberfest-checker")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")

    token = os.environ.get("GITHUB_TOKEN")
    if token:
        # Pass token strictly in header; never expose in error strings
        req.add_header("Authorization", f"Bearer {token.strip()}")

    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status = resp.status
            content = resp.read().decode("utf-8")
            try:
                data = json.loads(content)
                return status, data if isinstance(data, dict) else None
            except Exception:
                return status, None
    except urllib.error.HTTPError as e:
        # Capture status code without logging sensitive header info
        return e.code, None
    except (urllib.error.URLError, TimeoutError):
        # Network unreachable, DNS failure, or timeout
        return 0, None


def _file_exists(repo_slug: str, filename: str, timeout: int = DEFAULT_TIMEOUT) -> tuple[bool, str | None]:
    """Check if a file exists at repo root and retrieve its decoded text if present."""
    status, data = _api_get(f"/repos/{repo_slug}/contents/{filename}", timeout=timeout)
    if status == 200 and isinstance(data, dict) and "content" in data:
        try:
            raw_b64 = data.get("content", "")
            text = base64.b64decode(raw_b64).decode("utf-8", errors="ignore")
            return True, text
        except Exception:
            return True, None
    return False, None


@dataclass
class RepoReport:
    raw_url: str
    repo_slug: str | None = None
    track: str | None = None

    # Public visibility
    is_public: bool | None = None

    # License details
    # Statuses: "APPROVED", "NON_OSI_SPDX", "UNREPORTED_FILE_PRESENT", "MISSING", "CHECK_UNAVAILABLE"
    license_status: str = "UNKNOWN"
    license_id: str | None = None

    # Baseline files
    has_readme: bool | None = None
    readme_mentions_gemma: bool | None = None
    has_skill_md: bool | None = None

    # Network / API state
    is_rate_limited: bool = False
    is_network_error: bool = False
    http_status: int = 200

    # Diagnostic messages
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    notices: list[str] = field(default_factory=list)

    @property
    def is_track_1(self) -> bool:
        """Check if this report specifically targets Challenge 1 (Agent Skill)."""
        if not self.track:
            return False
        norm = str(self.track).strip().lower()
        return norm in ("1", "track-1", "track 1", "agent-skill", "agent_skill")

    @property
    def status_category(self) -> str:
        """Categorize preliminary check outcome into one of four operational states."""
        if self.is_rate_limited or self.is_network_error:
            return "CHECK UNAVAILABLE"

        if not self.repo_slug:
            return "CLEARLY INELIGIBLE"

        # Explicitly private repository
        if self.is_public is False and self.http_status == 200:
            return "CLEARLY INELIGIBLE"

        # 404 response: repository might be private (not yet toggled) or URL misspelled
        if self.http_status == 404:
            return "NEEDS MANUAL REVIEW"

        # Completely missing README
        if self.has_readme is False:
            return "CLEARLY INELIGIBLE"

        # Completely missing LICENSE (neither endpoint nor root file)
        if self.license_status == "MISSING":
            return "CLEARLY INELIGIBLE"

        # Ambiguous license: valid non-OSI SPDX or unasserted file
        if self.license_status in ("NON_OSI_SPDX", "UNREPORTED_FILE_PRESENT", "CHECK_UNAVAILABLE"):
            return "NEEDS MANUAL REVIEW"

        # README present but does not mention Gemma (weak signal requiring manual check)
        if self.has_readme is True and self.readme_mentions_gemma is False:
            return "NEEDS MANUAL REVIEW"

        # Track 1 specific check: SKILL.md is required for Challenge 1
        if self.is_track_1 and self.has_skill_md is False:
            return "NEEDS MANUAL REVIEW"

        # All baseline requirements verified
        if (
            self.is_public is True
            and self.license_status == "APPROVED"
            and self.has_readme is True
            and self.readme_mentions_gemma is True
            and (not self.is_track_1 or self.has_skill_md is True)
            and not self.errors
        ):
            return "ELIGIBLE (PASS)"

        return "NEEDS MANUAL REVIEW"


def check_repo(url: str, track: str | None = None, timeout: int = DEFAULT_TIMEOUT) -> RepoReport:
    """Run non-destructive preliminary eligibility checks against a single repository URL."""
    slug = parse_repo_slug(url)
    if not slug:
        report = RepoReport(raw_url=url, repo_slug=None, track=track)
        report.errors.append("Invalid GitHub repository URL. Must be a valid 'github.com/owner/repo' URL.")
        return report

    report = RepoReport(raw_url=url, repo_slug=slug, track=track)

    # 1. Check repository visibility
    status, data = _api_get(f"/repos/{slug}", timeout=timeout)
    report.http_status = status

    if status in (403, 429):
        report.is_rate_limited = True
        report.errors.append("GitHub API rate limit reached (HTTP 403/429).")
        return report

    if status == 0:
        report.is_network_error = True
        report.errors.append("Network timeout or connection error reaching GitHub API.")
        return report

    if status == 404:
        report.is_public = False
        report.warnings.append("Repository returned HTTP 404. It may be private or the repository name is misspelled.")
        return report

    if status != 200 or not isinstance(data, dict):
        report.errors.append(f"Unexpected GitHub API response (HTTP {status}).")
        return report

    report.is_public = not data.get("private", True)
    if report.is_public is False:
        report.errors.append("Repository is configured as PRIVATE on GitHub.")

    # 2. Check License
    lic_status, lic_data = _api_get(f"/repos/{slug}/license", timeout=timeout)
    if lic_status in (403, 429):
        report.is_rate_limited = True
        report.license_status = "CHECK_UNAVAILABLE"
        report.errors.append("GitHub API rate limit reached while checking license.")
        return report

    if lic_status == 0:
        report.is_network_error = True
        report.license_status = "CHECK_UNAVAILABLE"
        report.errors.append("Network timeout while checking license.")
        return report

    spdx_id = ""
    if lic_status == 200 and isinstance(lic_data, dict):
        lic_obj = lic_data.get("license")
        if isinstance(lic_obj, dict):
            spdx_id = (lic_obj.get("spdx_id") or "").strip()
        elif "spdx_id" in lic_data:
            spdx_id = (lic_data.get("spdx_id") or "").strip()

    norm_spdx = spdx_id.lower()
    if norm_spdx and norm_spdx in OSI_APPROVED_SPDX_IDS:
        report.license_status = "APPROVED"
        report.license_id = spdx_id
    elif norm_spdx and norm_spdx not in ("noassertion", "none"):
        # Fixes original defect: Non-empty SPDX ID that is NOT OSI-approved
        report.license_status = "NON_OSI_SPDX"
        report.license_id = spdx_id
        report.warnings.append(
            f"Repository reports SPDX ID '{spdx_id}', which is not in the canonical OSI-approved list. Organizers must verify."
        )
    else:
        # Fallback check for root LICENSE file
        has_lic_file, _ = _file_exists(slug, "LICENSE", timeout=timeout)
        if not has_lic_file:
            has_lic_file, _ = _file_exists(slug, "LICENSE.md", timeout=timeout)
        if not has_lic_file:
            has_lic_file, _ = _file_exists(slug, "LICENSE.txt", timeout=timeout)

        if has_lic_file:
            report.license_status = "UNREPORTED_FILE_PRESENT"
            report.license_id = spdx_id if spdx_id else "Unasserted/Custom"
            report.warnings.append(
                "A LICENSE file exists at repository root, but GitHub could not detect an approved SPDX identifier. Manual inspection required."
            )
        else:
            report.license_status = "MISSING"
            report.errors.append("No open-source LICENSE file detected at repository root or via GitHub license API.")

    # 3. Check README.md
    has_readme, readme_text = _file_exists(slug, "README.md", timeout=timeout)
    if not has_readme:
        has_readme, readme_text = _file_exists(slug, "readme.md", timeout=timeout)

    report.has_readme = has_readme
    if has_readme:
        if readme_text:
            # Word-boundary check for 'gemma' (case-insensitive)
            report.readme_mentions_gemma = bool(re.search(r"\bgemma\b", readme_text, re.IGNORECASE))
        else:
            report.readme_mentions_gemma = False

        if not report.readme_mentions_gemma:
            report.warnings.append(
                "README.md does not explicitly mention 'Gemma'. (Weak signal: human judges will verify substantive model use)."
            )
    else:
        report.errors.append("README.md missing from repository root.")

    # 4. Check SKILL.md (Track 1)
    has_skill, _ = _file_exists(slug, "SKILL.md", timeout=timeout)
    report.has_skill_md = has_skill
    if report.is_track_1 and not has_skill:
        report.warnings.append(
            "Track 1 declared: SKILL.md was not found at repository root. Check if skill is placed in a subfolder."
        )

    return report


def _mark(val: bool | None) -> str:
    if val is None:
        return "?"
    return "PASS" if val else "FAIL"


def print_report(report: RepoReport) -> None:
    """Print readable, formatted preliminary eligibility report to stdout."""
    cat = report.status_category
    header_title = report.repo_slug if report.repo_slug else report.raw_url
    print(f"\n{'=' * 60}")
    print(f"Repository : {header_title}")
    if report.track:
        print(f"Track      : {report.track}")
    print(f"Status     : [{cat}]")
    print(f"{'=' * 60}")

    if report.is_rate_limited or report.is_network_error:
        for err in report.errors:
            print(f"  [!] {err}")
        print("\n  CRITICAL NOTICE FOR ORGANIZERS:")
        print("  Automated check was unavailable due to network timeout or GitHub API rate limit.")
        print("  Do NOT penalize the team. Organizers must inspect the repository manually in a browser.")
        return

    # Errors
    for err in report.errors:
        print(f"  [x] ERROR: {err}")

    # Warnings
    for warn in report.warnings:
        print(f"  [!] WARNING: {warn}")

    # Visibility
    print(f"  [{_mark(report.is_public)}] Public repository visibility")

    # License
    if report.license_status == "APPROVED":
        print(f"  [PASS] OSI-approved license ({report.license_id})")
    elif report.license_status == "NON_OSI_SPDX":
        print(f"  [REVIEW] License reported ({report.license_id}) — not in default OSI list")
    elif report.license_status == "UNREPORTED_FILE_PRESENT":
        print(f"  [REVIEW] License file present at root, but SPDX unasserted ({report.license_id})")
    else:
        print(f"  [FAIL] License missing ({report.license_status})")

    # README
    print(f"  [{_mark(report.has_readme)}] README.md present at root")

    # Gemma mention (weak signal)
    mention_mark = _mark(report.readme_mentions_gemma)
    print(
        f"  [{mention_mark}] README mentions Gemma "
        f"[WEAK SIGNAL ONLY — does not prove model integration; judges verify depth of use]"
    )

    # Track 1: SKILL.md
    if report.is_track_1:
        skill_mark = _mark(report.has_skill_md)
        print(f"  [{skill_mark}] SKILL.md present [MANDATORY for Track 1: Agent Skill]")
    else:
        skill_note = "present" if report.has_skill_md else "not found"
        track_note = f"Track {report.track}" if report.track else "general tracks"
        print(f"  [i] SKILL.md: {skill_note} (informational — not required for {track_note})")

    # Outcome guidance
    print("\nAction / Guidance:")
    if cat == "ELIGIBLE (PASS)":
        print("  --> Baseline hygiene confirmed. Proceed to live demo.")
    elif cat == "NEEDS MANUAL REVIEW":
        print("  --> Flagged for manual review. Allow team to resolve before demos start.")
    elif cat == "CLEARLY INELIGIBLE":
        print("  --> Ineligible under baseline rules. Review with Lead Organizer before disqualification.")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Lightweight automated preliminary eligibility checker for Hacktoberfest Hack Day Nairobi.",
        epilog=(
            "Exit codes:\n"
            "  0: All checked repositories are ELIGIBLE (PASS)\n"
            "  1: At least one repository is CLEARLY INELIGIBLE\n"
            "  2: At least one repository is NEEDS MANUAL REVIEW or CHECK UNAVAILABLE\n"
            "  3: Command-line invocation or syntax error"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "urls",
        nargs="*",
        help="One or more GitHub repository URLs to check (e.g. https://github.com/team/project)",
    )
    parser.add_argument(
        "--track",
        dest="track",
        default=None,
        help="Optional primary challenge track (e.g. '1' for Agent Skill, '2' for Edge Offline, etc.)",
    )
    parser.add_argument(
        "--timeout",
        dest="timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help=f"HTTP request timeout in seconds (default: {DEFAULT_TIMEOUT})",
    )

    args = parser.parse_args(argv)

    if not args.urls:
        parser.print_help()
        return EXIT_USAGE_ERROR

    reports = [check_repo(url, track=args.track, timeout=args.timeout) for url in args.urls]
    for rep in reports:
        print_report(rep)

    # Compute summary counts
    pass_count = sum(1 for r in reports if r.status_category == "ELIGIBLE (PASS)")
    review_count = sum(1 for r in reports if r.status_category in ("NEEDS MANUAL REVIEW", "CHECK UNAVAILABLE"))
    ineligible_count = sum(1 for r in reports if r.status_category == "CLEARLY INELIGIBLE")

    print(f"\n{'=' * 60}")
    print(
        f"Summary: {len(reports)} checked | "
        f"{pass_count} eligible | "
        f"{review_count} need manual review | "
        f"{ineligible_count} clearly ineligible"
    )
    print(f"{'=' * 60}\n")

    if ineligible_count > 0:
        return EXIT_INELIGIBLE
    if review_count > 0:
        return EXIT_REVIEW_NEEDED
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
