#!/usr/bin/env python3
"""
check_submission.py — lightweight, automated PRELIMINARY ELIGIBILITY gate for
Hacktoberfest Hack Day Nairobi x iTech Club submissions.

This is a preliminary administrative gate, NOT an automated quality score or
ranking tool. It does NOT judge project quality, utility, architecture, or how
well Gemma is used — that is solely the role of the human judge panel and the
rubric in judging.md. All this script does is verify baseline repository hygiene
so organizers and teams can resolve administrative oversights before live demos.

Outcomes are strictly categorized into four operational states:
1. ELIGIBLE (PASS) — Meets preliminary repository hygiene requirements.
2. NEEDS MANUAL REVIEW — Administrative issue or nuance requiring human check.
3. CLEARLY INELIGIBLE — Critical failure after deadline (e.g. invalid repo, 404).
4. CHECK UNAVAILABLE — Network timeout or GitHub API rate limit.
   IMPORTANT: API rate limits and network errors must NEVER be interpreted as
   evidence of team noncompliance or project failure!

Usage:
    python3 scripts/check_submission.py <github-repo-url> [<github-repo-url> ...]

Optional:
    export GITHUB_TOKEN="ghp_xxx"  # Raises GitHub API limit from 60 to 5000 req/hr
"""

from __future__ import annotations

import base64
import json
import os
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from urllib.parse import urlparse

API_ROOT = "https://api.github.com"
OSI_LICENSE_IDS = {
    "mit", "apache-2.0", "gpl-3.0", "gpl-2.0", "lgpl-3.0", "bsd-3-clause",
    "bsd-2-clause", "mpl-2.0", "agpl-3.0", "unlicense", "isc",
}


@dataclass
class RepoReport:
    repo_slug: str
    is_public: bool | None = None
    has_license: bool | None = None
    license_id: str | None = None
    has_readme: bool | None = None
    readme_mentions_gemma: bool | None = None
    has_skill_md: bool | None = None
    is_rate_limited: bool = False
    is_network_error: bool = False
    errors: list[str] = field(default_factory=list)

    @property
    def status_category(self) -> str:
        """Categorize the preliminary check outcome into one of four states."""
        if self.is_rate_limited or self.is_network_error:
            return "CHECK UNAVAILABLE"
        if not self.repo_slug or "Not a recognizable" in " ".join(self.errors):
            return "CLEARLY INELIGIBLE"
        if self.is_public is False and any("404" in e for e in self.errors):
            return "NEEDS MANUAL REVIEW"  # Could be private; team needs to flip public
        if (
            self.is_public
            and self.has_license
            and self.has_readme
            and self.readme_mentions_gemma
            and not self.errors
        ):
            return "ELIGIBLE (PASS)"
        return "NEEDS MANUAL REVIEW"


def _api_get(path: str) -> tuple[int, dict | None]:
    """GET a GitHub API path. Returns (status_code, json_or_none)."""
    req = urllib.request.Request(f"{API_ROOT}{path}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "itech-club-hacktoberfest-checker")
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        if e.code in (403, 429):
            return e.code, None
        return e.code, None
    except (urllib.error.URLError, TimeoutError):
        return 0, None


def _parse_repo_slug(url: str) -> str | None:
    """Turn a GitHub repo URL into 'owner/repo', or None if it doesn't look like one."""
    parsed = urlparse(url.strip())
    if "github.com" not in parsed.netloc:
        return None
    parts = [p for p in parsed.path.split("/") if p]
    if len(parts) < 2:
        return None
    owner, repo = parts[0], parts[1]
    repo = re.sub(r"\.git$", "", repo)
    return f"{owner}/{repo}"


def _file_exists(repo_slug: str, filename: str) -> tuple[bool, str | None]:
    """Check whether a file exists at the repo root. Returns (exists, decoded_text_or_none)."""
    status, data = _api_get(f"/repos/{repo_slug}/contents/{filename}")
    if status == 200 and data and "content" in data:
        try:
            text = base64.b64decode(data["content"]).decode("utf-8", errors="ignore")
        except Exception:
            text = None
        return True, text
    return False, None


def check_repo(url: str) -> RepoReport:
    slug = _parse_repo_slug(url)
    if not slug:
        report = RepoReport(repo_slug=url)
        report.errors.append("Not a recognizable GitHub repository URL.")
        return report

    report = RepoReport(repo_slug=slug)

    status, data = _api_get(f"/repos/{slug}")
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
        report.errors.append("Repository not found (HTTP 404). Check URL or verify if repository is private.")
        return report
    if status != 200 or data is None:
        report.errors.append(f"Could not reach repository (HTTP {status}).")
        return report

    report.is_public = not data.get("private", True)

    # Check license
    status, license_data = _api_get(f"/repos/{slug}/license")
    if status == 200 and license_data:
        spdx = (license_data.get("license") or {}).get("spdx_id", "") or ""
        report.license_id = spdx
        report.has_license = spdx.lower() in OSI_LICENSE_IDS or bool(spdx)
    else:
        # Fallback check for root LICENSE file
        has_lic, _ = _file_exists(slug, "LICENSE")
        if not has_lic:
            has_lic, _ = _file_exists(slug, "LICENSE.md")
        report.has_license = has_lic

    # Check README.md
    has_readme, readme_text = _file_exists(slug, "README.md")
    report.has_readme = has_readme
    if has_readme and readme_text:
        report.readme_mentions_gemma = "gemma" in readme_text.lower()
    else:
        report.readme_mentions_gemma = False

    # Check SKILL.md (Track 1)
    has_skill, _ = _file_exists(slug, "SKILL.md")
    report.has_skill_md = has_skill

    return report


def _mark(value: bool | None) -> str:
    if value is None:
        return "?"
    return "PASS" if value else "FAIL"


def print_report(report: RepoReport) -> None:
    category = report.status_category
    print(f"\n=== {report.repo_slug} ===")
    print(f"  Preliminary Status : [{category}]")

    if report.is_rate_limited or report.is_network_error:
        for err in report.errors:
            print(f"  NOTICE: {err}")
        print("  --> ACTION REQUIRED: Do NOT penalize team. Perform immediate visual manual review in browser.")
        return

    if report.errors:
        for err in report.errors:
            print(f"  ISSUE: {err}")

    print(f"  [{_mark(report.is_public)}] Public repository")
    lic_str = f" ({report.license_id})" if report.license_id else ""
    print(f"  [{_mark(report.has_license)}] Open-source LICENSE file present{lic_str}")
    print(f"  [{_mark(report.has_readme)}] README.md present")
    print(f"  [{_mark(report.readme_mentions_gemma)}] README mentions Gemma (substantive depth verified by judges)")
    skill_note = "present" if report.has_skill_md else "not found"
    print(f"  [i] SKILL.md: {skill_note} (only required for Track 1: Agent Skill)")

    if category == "ELIGIBLE (PASS)":
        print("  --> Outcome: Baseline eligibility confirmed. Proceed to live demo.")
    elif category == "NEEDS MANUAL REVIEW":
        print("  --> Outcome: Flagged for manual review. Allow team to resolve before demos start.")
    elif category == "CLEARLY INELIGIBLE":
        print("  --> Outcome: Disqualifying issue detected. Confirm with Lead Organizer.")


def main() -> int:
    urls = sys.argv[1:]
    if not urls:
        print(__doc__)
        return 1

    reports = [check_repo(url) for url in urls]
    for report in reports:
        print_report(report)

    needs_review = [r for r in reports if r.status_category in ("NEEDS MANUAL REVIEW", "CHECK UNAVAILABLE")]
    ineligible = [r for r in reports if r.status_category == "CLEARLY INELIGIBLE"]
    print(f"\nSummary: {len(reports)} repo(s) checked | {len(reports) - len(needs_review) - len(ineligible)} eligible | {len(needs_review)} need manual review | {len(ineligible)} clearly ineligible.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
