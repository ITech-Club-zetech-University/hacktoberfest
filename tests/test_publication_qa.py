"""Regression checks for the exact generated participant-only Pages artifact."""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts import qa_publication


class TestPublicationQA(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.site = self.root / "site"
        self.source = self.root / "source"
        for relative in qa_publication.PARTICIPANT_PAGES:
            target = self.site / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(
                '<html><head><link rel="stylesheet" href="/hacktoberfest/assets/site.css">'
                '</head><body><nav aria-label="Main"><a href="/hacktoberfest/">Home</a></nav>'
                '<main id="main-content"><h1 id="title">Participant guide</h1>'
                '<a href="#main-content">Content</a></main></body></html>',
                encoding="utf-8",
            )
        assets = self.site / "assets"
        assets.mkdir(exist_ok=True)
        (assets / "site.css").write_text("body { color: white; }", encoding="utf-8")
        (assets / "js").mkdir()
        (assets / "js/search-data.json").write_text("{}", encoding="utf-8")
        for relative in qa_publication.DOWNLOADS:
            for base in (self.source, self.site):
                target = base / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text("# Copy-ready source\n", encoding="utf-8")

    def audit(self, baseurl="/hacktoberfest"):
        return qa_publication.audit_publication(self.site, self.source, baseurl)

    def test_participant_artifact_passes(self):
        self.assertEqual(self.audit(), [])

    def test_internal_archived_and_extra_download_pages_are_rejected(self):
        for relative in (
            "_internal/organiser/judge-score-sheet.csv", "organizer-runbook/index.html",
            "organizer-checklist/index.html", "references/source-register/index.html",
            "challenges/02-edge-offline/index.html", "templates/judge-score-sheet.csv",
            "templates/downloads/index.html", "templates/downloads/project-proposal/index.html",
        ):
            with self.subTest(path=relative):
                path = self.site / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("Old content", encoding="utf-8")
                self.assertTrue(any("unintended output" in error for error in self.audit()))
                path.unlink()

    def test_missing_participant_page_and_changed_download_are_rejected(self):
        (self.site / "rules/index.html").unlink()
        (self.site / "templates/downloads/README.md").write_text("<html>not Markdown</html>", encoding="utf-8")
        errors = self.audit()
        self.assertIn("Missing participant page: rules/index.html", errors)
        self.assertIn("Participant download changed during generation: templates/downloads/README.md", errors)

    def test_raw_downloads_must_not_appear_in_navigation_or_search(self):
        path = self.site / "index.html"
        path.write_text(
            path.read_text().replace(
                ">Home</a>", '>Home</a><a href="/hacktoberfest/templates/downloads/README.md">[Project Name]</a>',
            ),
            encoding="utf-8",
        )
        (self.site / "assets/js/search-data.json").write_text(
            '{"url":"/hacktoberfest/templates/downloads/project-proposal/"}', encoding="utf-8",
        )
        errors = self.audit()
        self.assertTrue(any("leaked into navigation" in error for error in errors))
        self.assertTrue(any("unintended page in search index" in error for error in errors))

    def test_broken_links_anchors_and_duplicate_headings_are_rejected(self):
        path = self.site / "index.html"
        path.write_text(
            path.read_text().replace(
                "</main>",
                '<h1 id="title">Duplicate</h1><a href="/hacktoberfest/absent/">Missing</a>'
                '<a href="/hacktoberfest/rules/#absent">Anchor</a></main>',
            ),
            encoding="utf-8",
        )
        errors = self.audit()
        for message in ("Missing target", "Missing anchor", "Duplicate ID", "Expected one H1"):
            self.assertTrue(any(message in error for error in errors), message)

    def test_editorial_content_and_unstyled_pages_are_rejected(self):
        path = self.site / "index.html"
        path.write_text(
            "<html><body><h1>Verification status before publication</h1></body></html>",
            encoding="utf-8",
        )
        errors = self.audit()
        self.assertTrue(any("Internal editorial text" in error for error in errors))
        self.assertTrue(any("Missing theme stylesheet" in error for error in errors))

    def test_unexpected_page_and_placeholder_heading_are_rejected(self):
        extra = self.site / "editorial/index.html"
        extra.parent.mkdir()
        extra.write_text("<h1>Internal notes</h1>", encoding="utf-8")
        portal = self.site / "templates/project-readme-template/index.html"
        portal.write_text(portal.read_text().replace("Participant guide", "[Project Name]"), encoding="utf-8")
        errors = self.audit()
        self.assertIn("Unexpected HTML page: editorial/index.html", errors)
        self.assertTrue(any("Template placeholder used as page heading" in error for error in errors))

    def test_empty_baseurl_is_supported(self):
        for path in self.site.rglob("*.html"):
            path.write_text(path.read_text().replace("/hacktoberfest/", "/"), encoding="utf-8")
        self.assertEqual(self.audit(baseurl=""), [])


if __name__ == "__main__":
    unittest.main()
