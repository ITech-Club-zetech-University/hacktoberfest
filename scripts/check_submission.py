#!/usr/bin/env python3
"""
check_submission.py — lightweight, automated ELIGIBILITY check for Hacktoberfest
Hack Day Nairobi x iTech Club submissions.

This is NOT a scoring or ranking tool. It does not judge project quality, how
well Gemma is used, or how good a demo is — that's what the human judge panel
and the rubric in judging.md are for. All this script does is flag the basic,
objectively-checkable requirements from rules.md, so judges don't spend their
limited time discovering a missing license or README during judging.

Usage:
    python3 scripts/check_submission.py <github-repo-url> [<github-repo-url> ...]

Example:
    python3 scripts/check_submission.py \
        https://github.com/some-team/gemma-offline-notes \
        https://github.com/some-team/gemma-agent-skill

Optional: set a GITHUB_TOKEN environment variable to raise the GitHub API rate
limit from 60 requests/hour (unauthenticated) to 5000/hour. Not required for a
typical night's worth of submissions.
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
    errors: list[str] = field(default_factory=list)

    @property
    def passed_baseline(self) -> bool:
        """The core, required checks — everything except SKILL.md, which is
        only required for Challenge 1 (Agent Skill) submissions."""
        return bool(
            self.is_public
            and self.has_license
            and self.has_readme
            and self.readme_mentions_gemma
            and not self.errors
        )


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
        if e.code == 404:
            return 404, None
        if e.code in (403, 429):
            return e.code, None
        return e.code, None
    except (urllib.error.URLError, TimeoutError):
        return 0, None


def _parse_repo_slug(url: str) -> str | None:
    """Turn a GitHub repo URL into 'owner/repo', or None if it doesn't look
    like one."""
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
    """Check whether a file exists at the repo root. Returns
    (exists, decoded_text_or_none)."""
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
    if status == 404:
        report.errors.append("Repository not found (404) — check the URL, or it may be private.")
        return report
    if status in (403, 429):
        report.errors.append(
            "GitHub API rate-limited this request. Set a GITHUB_TOKEN env var and re-run."
        )
        return report
    if status != 200 or data is None:
        report.errors.append(f"Could not reach the repository (HTTP {status}).")
        return report

    report.is_public = not data.get("private", True)

    status, license_data = _api_get(f"/repos/{slug}/license")
    if status == 200 and license_data:
        spdx = (license_data.get("license") or {}).get("spdx_id", "") or ""
        report.license_id = spdx
        report.has_license = spdx.lower() in OSI_LICENSE_IDS or bool(spdx)
    else:
        report.has_license = False

    has_readme, readme_text = _file_exists(slug, "README.md")
    report.has_readme = has_readme
    if has_readme and readme_text:
        report.readme_mentions_gemma = "gemma" in readme_text.lower()
    else:
        report.readme_mentions_gemma = False

    has_skill, _ = _file_exists(slug, "SKILL.md")
    report.has_skill_md = has_skill

    return report


def _mark(value: bool | None) -> str:
    if value is None:
        return "?"
    return "PASS" if value else "FAIL"


def print_report(report: RepoReport) -> None:
    print(f"\n=== {report.repo_slug} ===")
    if report.errors:
        for err in report.errors:
            print(f"  ERROR: {err}")
        return
    print(f"  [{_mark(report.is_public)}] Public repository")
    license_note = f" ({report.license_id})" if report.license_id else ""
    print(f"  [{_mark(report.has_license)}] Open-source license present{license_note}")
    print(f"  [{_mark(report.has_readme)}] README.md present")
    print(f"  [{_mark(report.readme_mentions_gemma)}] README mentions Gemma (manual check still needed — judges confirm depth of use)")
    skill_note = "present" if report.has_skill_md else "not found"
    print(f"  [i] SKILL.md: {skill_note} (only required for Challenge 1 — Agent Skill)")
    print(f"  --> Baseline eligibility: {'PASS' if report.passed_baseline else 'NEEDS FOLLOW-UP'}")


def main() -> int:
    urls = sys.argv[1:]
    if not urls:
        print(__doc__)
        return 1

    reports = [check_repo(url) for url in urls]
    for report in reports:
        print_report(report)

    needs_followup = [r for r in reports if not r.passed_baseline]
    print(f"\n{len(reports)} repo(s) checked, {len(needs_followup)} need follow-up before judging.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
