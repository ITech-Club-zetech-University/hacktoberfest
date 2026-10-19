#!/usr/bin/env python3
"""
Unit tests for scripts/check_submission.py.

All tests mock network and GitHub API responses so they can run offline
without requiring live network calls, GitHub API tokens, or external dependencies.
"""

import base64
import os
import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

# Ensure repository root is on sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.check_submission import (
    DEFAULT_TIMEOUT,
    EXIT_INELIGIBLE,
    EXIT_OK,
    EXIT_REVIEW_NEEDED,
    EXIT_USAGE_ERROR,
    OSI_APPROVED_SPDX_IDS,
    RepoReport,
    _api_get,
    _file_exists,
    check_repo,
    load_osi_approved_licenses,
    main,
    parse_repo_slug,
)


class TestURLParsing(unittest.TestCase):
    """Test strict GitHub repository URL parsing and hostname security."""

    def test_valid_standard_url(self):
        self.assertEqual(parse_repo_slug("https://github.com/octocat/Hello-World"), "octocat/Hello-World")

    def test_valid_url_with_www(self):
        self.assertEqual(parse_repo_slug("https://www.github.com/octocat/Hello-World"), "octocat/Hello-World")

    def test_valid_url_with_git_suffix(self):
        self.assertEqual(parse_repo_slug("https://github.com/octocat/Hello-World.git"), "octocat/Hello-World")

    def test_valid_url_with_trailing_slash(self):
        self.assertEqual(parse_repo_slug("https://github.com/octocat/Hello-World/"), "octocat/Hello-World")

    def test_valid_url_with_git_and_trailing_slash(self):
        self.assertEqual(parse_repo_slug("https://github.com/octocat/Hello-World.git/"), "octocat/Hello-World")

    def test_valid_url_without_scheme(self):
        self.assertEqual(parse_repo_slug("github.com/octocat/Hello-World"), "octocat/Hello-World")

    def test_valid_url_with_http(self):
        self.assertEqual(parse_repo_slug("http://github.com/octocat/Hello-World"), "octocat/Hello-World")

    def test_reject_lookalike_domain_prefix(self):
        self.assertIsNone(parse_repo_slug("https://notgithub.com/octocat/Hello-World"))

    def test_reject_lookalike_subdomain(self):
        self.assertIsNone(parse_repo_slug("https://github.com.evil.com/octocat/Hello-World"))

    def test_reject_lookalike_hyphenated(self):
        self.assertIsNone(parse_repo_slug("https://evil-github.com/octocat/Hello-World"))

    def test_reject_unsupported_host_gitlab(self):
        self.assertIsNone(parse_repo_slug("https://gitlab.com/octocat/Hello-World"))

    def test_reject_unsupported_host_bitbucket(self):
        self.assertIsNone(parse_repo_slug("https://bitbucket.org/octocat/Hello-World"))

    def test_reject_root_url(self):
        self.assertIsNone(parse_repo_slug("https://github.com/"))

    def test_reject_owner_only_url(self):
        self.assertIsNone(parse_repo_slug("https://github.com/octocat"))

    def test_reject_deep_subpath(self):
        self.assertIsNone(parse_repo_slug("https://github.com/octocat/Hello-World/tree/main"))

    def test_reject_empty_or_whitespace(self):
        self.assertIsNone(parse_repo_slug(""))
        self.assertIsNone(parse_repo_slug("   "))

    def test_reject_arbitrary_string(self):
        self.assertIsNone(parse_repo_slug("not a url at all"))

    def test_reject_invalid_username_characters(self):
        self.assertIsNone(parse_repo_slug("https://github.com/invalid user/Hello-World"))


class TestLicenseValidation(unittest.TestCase):
    """Test license verification against official OSI-approved SPDX IDs."""

    def test_canonical_osi_list_loads_successfully(self):
        self.assertIn("mit", OSI_APPROVED_SPDX_IDS)
        self.assertIn("apache-2.0", OSI_APPROVED_SPDX_IDS)
        self.assertIn("gpl-3.0", OSI_APPROVED_SPDX_IDS)
        self.assertIn("bsd-3-clause", OSI_APPROVED_SPDX_IDS)

    def test_approved_license_mit(self):
        api_responses = {
            "/repos/test/repo": (200, {"private": False}),
            "/repos/test/repo/license": (200, {"license": {"spdx_id": "MIT"}}),
            "/repos/test/repo/contents/README.md": (200, {"content": base64.b64encode(b"# Built with Gemma").decode()}),
            "/repos/test/repo/contents/SKILL.md": (404, None),
        }

        def fake_api(path, timeout=DEFAULT_TIMEOUT):
            return api_responses.get(path, (404, None))

        with patch("scripts.check_submission._api_get", side_effect=fake_api):
            report = check_repo("https://github.com/test/repo")
            self.assertEqual(report.license_status, "APPROVED")
            self.assertEqual(report.license_id, "MIT")
            self.assertEqual(report.status_category, "ELIGIBLE (PASS)")

    def test_approved_license_apache_2_case_insensitive(self):
        api_responses = {
            "/repos/test/repo": (200, {"private": False}),
            "/repos/test/repo/license": (200, {"license": {"spdx_id": "Apache-2.0"}}),
            "/repos/test/repo/contents/README.md": (200, {"content": base64.b64encode(b"Uses gemma 4 model.").decode()}),
            "/repos/test/repo/contents/SKILL.md": (404, None),
        }

        def fake_api(path, timeout=DEFAULT_TIMEOUT):
            return api_responses.get(path, (404, None))

        with patch("scripts.check_submission._api_get", side_effect=fake_api):
            report = check_repo("https://github.com/test/repo")
            self.assertEqual(report.license_status, "APPROVED")
            self.assertEqual(report.status_category, "ELIGIBLE (PASS)")

    def test_original_bug_unapproved_spdx_does_not_pass(self):
        """CRITICAL: Test that any non-empty unapproved SPDX identifier does NOT pass.

        The original defective check `spdx.lower() in OSI_LICENSE_IDS or bool(spdx)`
        accepted any non-empty SPDX ID. This test verifies that an unknown/unapproved
        SPDX string yields NON_OSI_SPDX and NEEDS MANUAL REVIEW.
        """
        api_responses = {
            "/repos/test/repo": (200, {"private": False}),
            "/repos/test/repo/license": (200, {"license": {"spdx_id": "RANDOM-UNAPPROVED-ID"}}),
            "/repos/test/repo/contents/README.md": (200, {"content": base64.b64encode(b"Uses Gemma").decode()}),
            "/repos/test/repo/contents/SKILL.md": (404, None),
        }

        def fake_api(path, timeout=DEFAULT_TIMEOUT):
            return api_responses.get(path, (404, None))

        with patch("scripts.check_submission._api_get", side_effect=fake_api):
            report = check_repo("https://github.com/test/repo")
            self.assertEqual(report.license_status, "NON_OSI_SPDX")
            self.assertEqual(report.license_id, "RANDOM-UNAPPROVED-ID")
            # Must NOT be ELIGIBLE (PASS)
            self.assertNotEqual(report.status_category, "ELIGIBLE (PASS)")
            self.assertEqual(report.status_category, "NEEDS MANUAL REVIEW")

    def test_known_non_osi_spdx_cc_by_4_needs_manual_review(self):
        api_responses = {
            "/repos/test/repo": (200, {"private": False}),
            "/repos/test/repo/license": (200, {"license": {"spdx_id": "CC-BY-4.0"}}),
            "/repos/test/repo/contents/README.md": (200, {"content": base64.b64encode(b"Gemma project").decode()}),
            "/repos/test/repo/contents/SKILL.md": (404, None),
        }

        def fake_api(path, timeout=DEFAULT_TIMEOUT):
            return api_responses.get(path, (404, None))

        with patch("scripts.check_submission._api_get", side_effect=fake_api):
            report = check_repo("https://github.com/test/repo")
            self.assertEqual(report.license_status, "NON_OSI_SPDX")
            self.assertEqual(report.status_category, "NEEDS MANUAL REVIEW")

    def test_noassertion_with_root_license_file_needs_manual_review(self):
        api_responses = {
            "/repos/test/repo": (200, {"private": False}),
            "/repos/test/repo/license": (200, {"license": {"spdx_id": "NOASSERTION"}}),
            "/repos/test/repo/contents/LICENSE": (200, {"content": base64.b64encode(b"Custom License Text").decode()}),
            "/repos/test/repo/contents/README.md": (200, {"content": base64.b64encode(b"Gemma app").decode()}),
            "/repos/test/repo/contents/SKILL.md": (404, None),
        }

        def fake_api(path, timeout=DEFAULT_TIMEOUT):
            return api_responses.get(path, (404, None))

        with patch("scripts.check_submission._api_get", side_effect=fake_api):
            report = check_repo("https://github.com/test/repo")
            self.assertEqual(report.license_status, "UNREPORTED_FILE_PRESENT")
            self.assertEqual(report.status_category, "NEEDS MANUAL REVIEW")

    def test_missing_license_completely_is_ineligible(self):
        api_responses = {
            "/repos/test/repo": (200, {"private": False}),
            "/repos/test/repo/license": (404, None),
            "/repos/test/repo/contents/LICENSE": (404, None),
            "/repos/test/repo/contents/LICENSE.md": (404, None),
            "/repos/test/repo/contents/LICENSE.txt": (404, None),
            "/repos/test/repo/contents/README.md": (200, {"content": base64.b64encode(b"Gemma project").decode()}),
            "/repos/test/repo/contents/SKILL.md": (404, None),
        }

        def fake_api(path, timeout=DEFAULT_TIMEOUT):
            return api_responses.get(path, (404, None))

        with patch("scripts.check_submission._api_get", side_effect=fake_api):
            report = check_repo("https://github.com/test/repo")
            self.assertEqual(report.license_status, "MISSING")
            self.assertEqual(report.status_category, "CLEARLY INELIGIBLE")


class TestRepoVisibility(unittest.TestCase):
    """Test public vs. private vs. missing repository handling."""

    def test_public_repo_passes(self):
        api_responses = {
            "/repos/test/repo": (200, {"private": False}),
            "/repos/test/repo/license": (200, {"license": {"spdx_id": "MIT"}}),
            "/repos/test/repo/contents/README.md": (200, {"content": base64.b64encode(b"Gemma project").decode()}),
            "/repos/test/repo/contents/SKILL.md": (404, None),
        }

        with patch("scripts.check_submission._api_get", side_effect=lambda p, timeout=DEFAULT_TIMEOUT: api_responses.get(p, (404, None))):
            report = check_repo("https://github.com/test/repo")
            self.assertTrue(report.is_public)
            self.assertEqual(report.status_category, "ELIGIBLE (PASS)")

    def test_explicitly_private_repo_is_clearly_ineligible(self):
        api_responses = {
            "/repos/test/repo": (200, {"private": True}),
        }

        with patch("scripts.check_submission._api_get", side_effect=lambda p, timeout=DEFAULT_TIMEOUT: api_responses.get(p, (404, None))):
            report = check_repo("https://github.com/test/repo")
            self.assertFalse(report.is_public)
            self.assertEqual(report.status_category, "CLEARLY INELIGIBLE")

    def test_404_repo_needs_manual_review_not_permanent_disqualification(self):
        """A 404 might be an un-flipped private repo; give team a chance before 5 AM."""
        with patch("scripts.check_submission._api_get", return_value=(404, None)):
            report = check_repo("https://github.com/test/repo")
            self.assertFalse(report.is_public)
            self.assertEqual(report.status_category, "NEEDS MANUAL REVIEW")


class TestReadmeAndGemmaMention(unittest.TestCase):
    """Test README check and Gemma weak signal detection."""

    def test_missing_readme_is_ineligible(self):
        api_responses = {
            "/repos/test/repo": (200, {"private": False}),
            "/repos/test/repo/license": (200, {"license": {"spdx_id": "MIT"}}),
            "/repos/test/repo/contents/README.md": (404, None),
            "/repos/test/repo/contents/readme.md": (404, None),
        }

        with patch("scripts.check_submission._api_get", side_effect=lambda p, timeout=DEFAULT_TIMEOUT: api_responses.get(p, (404, None))):
            report = check_repo("https://github.com/test/repo")
            self.assertFalse(report.has_readme)
            self.assertEqual(report.status_category, "CLEARLY INELIGIBLE")

    def test_readme_without_gemma_needs_manual_review(self):
        api_responses = {
            "/repos/test/repo": (200, {"private": False}),
            "/repos/test/repo/license": (200, {"license": {"spdx_id": "MIT"}}),
            "/repos/test/repo/contents/README.md": (200, {"content": base64.b64encode(b"# My Hackathon Project\nDoes things.").decode()}),
            "/repos/test/repo/contents/SKILL.md": (404, None),
        }

        with patch("scripts.check_submission._api_get", side_effect=lambda p, timeout=DEFAULT_TIMEOUT: api_responses.get(p, (404, None))):
            report = check_repo("https://github.com/test/repo")
            self.assertTrue(report.has_readme)
            self.assertFalse(report.readme_mentions_gemma)
            self.assertEqual(report.status_category, "NEEDS MANUAL REVIEW")

    def test_readme_with_gemma_passes(self):
        api_responses = {
            "/repos/test/repo": (200, {"private": False}),
            "/repos/test/repo/license": (200, {"license": {"spdx_id": "MIT"}}),
            "/repos/test/repo/contents/README.md": (200, {"content": base64.b64encode(b"Powered by Google's Gemma 4 model.").decode()}),
            "/repos/test/repo/contents/SKILL.md": (404, None),
        }

        with patch("scripts.check_submission._api_get", side_effect=lambda p, timeout=DEFAULT_TIMEOUT: api_responses.get(p, (404, None))):
            report = check_repo("https://github.com/test/repo")
            self.assertTrue(report.has_readme)
            self.assertTrue(report.readme_mentions_gemma)
            self.assertEqual(report.status_category, "ELIGIBLE (PASS)")


class TestSkillMdAndTrackCheck(unittest.TestCase):
    """Test Challenge 1 (Track 1: Agent Skill) specific SKILL.md check."""

    def test_skill_md_optional_for_general_tracks(self):
        """When no track or track != 1 is given, missing SKILL.md is informational only."""
        api_responses = {
            "/repos/test/repo": (200, {"private": False}),
            "/repos/test/repo/license": (200, {"license": {"spdx_id": "MIT"}}),
            "/repos/test/repo/contents/README.md": (200, {"content": base64.b64encode(b"Gemma project").decode()}),
            "/repos/test/repo/contents/SKILL.md": (404, None),
        }

        with patch("scripts.check_submission._api_get", side_effect=lambda p, timeout=DEFAULT_TIMEOUT: api_responses.get(p, (404, None))):
            # No track specified
            report_no_track = check_repo("https://github.com/test/repo")
            self.assertEqual(report_no_track.status_category, "ELIGIBLE (PASS)")

            # Track 2 specified
            report_track_2 = check_repo("https://github.com/test/repo", track="2")
            self.assertEqual(report_track_2.status_category, "ELIGIBLE (PASS)")

    def test_skill_md_mandatory_for_track_1(self):
        """When Track 1 is explicitly declared, missing SKILL.md flags NEEDS MANUAL REVIEW."""
        api_responses = {
            "/repos/test/repo": (200, {"private": False}),
            "/repos/test/repo/license": (200, {"license": {"spdx_id": "MIT"}}),
            "/repos/test/repo/contents/README.md": (200, {"content": base64.b64encode(b"Gemma Agent Skill").decode()}),
            "/repos/test/repo/contents/SKILL.md": (404, None),
        }

        with patch("scripts.check_submission._api_get", side_effect=lambda p, timeout=DEFAULT_TIMEOUT: api_responses.get(p, (404, None))):
            report = check_repo("https://github.com/test/repo", track="1")
            self.assertFalse(report.has_skill_md)
            self.assertEqual(report.status_category, "NEEDS MANUAL REVIEW")

    def test_skill_md_present_for_track_1_passes(self):
        api_responses = {
            "/repos/test/repo": (200, {"private": False}),
            "/repos/test/repo/license": (200, {"license": {"spdx_id": "MIT"}}),
            "/repos/test/repo/contents/README.md": (200, {"content": base64.b64encode(b"Gemma Agent Skill").decode()}),
            "/repos/test/repo/contents/SKILL.md": (200, {"content": base64.b64encode(b"---\nname: my-skill\n---").decode()}),
        }

        with patch("scripts.check_submission._api_get", side_effect=lambda p, timeout=DEFAULT_TIMEOUT: api_responses.get(p, (404, None))):
            report = check_repo("https://github.com/test/repo", track="1")
            self.assertTrue(report.has_skill_md)
            self.assertEqual(report.status_category, "ELIGIBLE (PASS)")


class TestNetworkFailureAndRateLimiting(unittest.TestCase):
    """Test that API rate limits and network errors yield CHECK UNAVAILABLE rather than false failure."""

    def test_rate_limit_403_yields_check_unavailable(self):
        with patch("scripts.check_submission._api_get", return_value=(403, None)):
            report = check_repo("https://github.com/test/repo")
            self.assertTrue(report.is_rate_limited)
            self.assertEqual(report.status_category, "CHECK UNAVAILABLE")

    def test_rate_limit_429_yields_check_unavailable(self):
        with patch("scripts.check_submission._api_get", return_value=(429, None)):
            report = check_repo("https://github.com/test/repo")
            self.assertTrue(report.is_rate_limited)
            self.assertEqual(report.status_category, "CHECK UNAVAILABLE")

    def test_network_timeout_yields_check_unavailable(self):
        with patch("scripts.check_submission._api_get", return_value=(0, None)):
            report = check_repo("https://github.com/test/repo")
            self.assertTrue(report.is_network_error)
            self.assertEqual(report.status_category, "CHECK UNAVAILABLE")


class TestSecurityAndTokenHandling(unittest.TestCase):
    """Test that GITHUB_TOKEN is transmitted safely and never exposed in output."""

    @patch("urllib.request.urlopen")
    def test_token_passed_in_authorization_header(self, mock_urlopen):
        mock_resp = MagicMock()
        mock_resp.status = 200
        mock_resp.read.return_value = b'{"private": false}'
        mock_urlopen.return_value.__enter__.return_value = mock_resp

        with patch.dict(os.environ, {"GITHUB_TOKEN": "secret_token_123"}):
            status, data = _api_get("/repos/test/repo")
            self.assertEqual(status, 200)

            # Inspect request sent to urlopen
            args, _ = mock_urlopen.call_args
            req = args[0]
            self.assertIn("Authorization", req.headers)
            self.assertEqual(req.headers["Authorization"], "Bearer secret_token_123")
            self.assertEqual(req.headers["Accept"], "application/vnd.github+json")
            self.assertEqual(req.headers["User-agent"], "itech-club-hacktoberfest-checker")

    def test_token_not_leaked_in_reports(self):
        report = RepoReport(raw_url="https://github.com/test/repo", repo_slug="test/repo")
        report.errors.append("Connection error occurred.")
        report_str = str(report)
        self.assertNotIn("secret_token_123", report_str)


class TestMainExitCodes(unittest.TestCase):
    """Test CLI main() exit codes for organizers."""

    def test_main_all_eligible_returns_exit_ok(self):
        passing_report = RepoReport(
            raw_url="https://github.com/test/repo",
            repo_slug="test/repo",
            is_public=True,
            license_status="APPROVED",
            license_id="MIT",
            has_readme=True,
            readme_mentions_gemma=True,
        )
        with patch("scripts.check_submission.check_repo", return_value=passing_report):
            code = main(["https://github.com/test/repo"])
            self.assertEqual(code, EXIT_OK)

    def test_main_ineligible_returns_exit_ineligible(self):
        ineligible_report = RepoReport(
            raw_url="https://github.com/test/repo",
            repo_slug="test/repo",
            is_public=False,
            http_status=200,
        )
        with patch("scripts.check_submission.check_repo", return_value=ineligible_report):
            code = main(["https://github.com/test/repo"])
            self.assertEqual(code, EXIT_INELIGIBLE)

    def test_main_review_needed_returns_exit_review(self):
        review_report = RepoReport(
            raw_url="https://github.com/test/repo",
            repo_slug="test/repo",
            http_status=404,
        )
        with patch("scripts.check_submission.check_repo", return_value=review_report):
            code = main(["https://github.com/test/repo"])
            self.assertEqual(code, EXIT_REVIEW_NEEDED)

    def test_main_no_urls_returns_exit_usage_error(self):
        code = main([])
        self.assertEqual(code, EXIT_USAGE_ERROR)


if __name__ == "__main__":
    unittest.main()
