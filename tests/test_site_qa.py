"""Unit tests verifying Jekyll site link integrity and front matter QA."""

import unittest
import csv
import re
import os
import sys
from pathlib import Path

# Ensure repository root and scripts directory are on sys.path
repo_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(repo_root))
sys.path.insert(0, str(repo_root / "scripts"))

try:
    from scripts import qa_site
except ImportError:
    import qa_site


class TestJekyllSiteQA(unittest.TestCase):
    def test_repository_site_qa_passes(self):
        """Verify all internal links, anchors, heading hierarchy, and front matter pass QA."""
        exit_code = qa_site.audit_repository(str(repo_root))
        self.assertEqual(exit_code, 0, "Site QA audit failed. Check broken links or front matter.")

    def test_kramdown_slug_generator(self):
        """Test kramdown slug generation helper."""
        self.assertEqual(qa_site.kramdown_slug("Quick Path Decision Matrix"), "quick-path-decision-matrix")
        self.assertEqual(qa_site.kramdown_slug("Team size & formation"), "team-size-formation")
        self.assertEqual(qa_site.kramdown_slug("Option A: Hosted Gemma [API]"), "option-a-hosted-gemma-api")

    def test_config_layout_defaults(self):
        """Verify _config.yml defines front-matter defaults for pages to use the default layout."""
        config_path = repo_root / "_config.yml"
        self.assertTrue(config_path.is_file(), "_config.yml must exist")
        content = config_path.read_text(encoding="utf-8")
        self.assertIn("defaults:", content)
        self.assertRegex(content, r"layout:\s*['\"]?default['\"]?")

    def test_homepage_preserves_home_layout(self):
        """Verify index.md explicitly preserves layout: home."""
        index_path = repo_root / "index.md"
        self.assertTrue(index_path.is_file(), "index.md must exist")
        content = index_path.read_text(encoding="utf-8")
        fm, _ = qa_site.parse_front_matter(content)
        self.assertEqual(fm.get("layout"), "home", "Homepage index.md must explicitly specify layout: home")

    def test_open_ended_brief_and_categories(self):
        content = (repo_root / "challenges" / "index.md").read_text(encoding="utf-8")
        fm, _ = qa_site.parse_front_matter(content)
        self.assertEqual(fm["title"], "Build Your Own Open-Source AI Project")
        self.assertNotIn("has_children", fm)
        self.assertEqual(len(re.findall(r"^### Step [1-7] ", content, flags=re.MULTILINE)), 7)
        for category_id in (
            "01a0d987-0c41-12ea-13ac-5b85755dc2f3",
            "01a03b87-be22-9180-5e2d-b3beeb66666d",
        ):
            self.assertIn(f"/challenges/{category_id}", content)
        self.assertIn("not a mandatory technology choice", content)
        self.assertIn("failure or uncertainty scenario", content)

    def test_former_briefs_are_archived_without_changing_urls(self):
        briefs = sorted((repo_root / "challenges").glob("0*.md"))
        self.assertEqual(len(briefs), 5)
        for brief in briefs:
            with self.subTest(brief=brief.name):
                content = brief.read_text(encoding="utf-8")
                fm, _ = qa_site.parse_front_matter(content)
                self.assertEqual(fm.get("nav_exclude"), "true")
                self.assertEqual(fm.get("search_exclude"), "true")
                self.assertNotIn("parent", fm)
                self.assertNotIn("permalink", fm)
                self.assertIn("Historical brief", content)
                self.assertIn("{{ site.baseurl }}/challenges/", content)

    def test_worksheet_and_optional_inspiration(self):
        worksheet = (repo_root / "templates" / "problem-statement.md").read_text(encoding="utf-8")
        for field in (
            "Project name:", "Problem:", "Primary user:", "Why the problem matters:",
            "Current alternative or workaround:", "Proposed solution:",
            "What the AI model will do:", "Why an open model is appropriate:",
            "Why Gemma 4 is being used (if applicable):", "Data and tools required:",
            "Main risks or limitations:", "MVP features for the hack period:",
            "How the team will demonstrate success:",
        ):
            self.assertIn(field, worksheet)
        inspiration = (repo_root / "inspiration.md").read_text(encoding="utf-8")
        self.assertIn("optional starting points", inspiration)
        self.assertIn("No unsupported diagnosis", inspiration)

    def test_score_sheet_remains_project_neutral_and_arithmetically_valid(self):
        with (repo_root / "templates" / "judge-score-sheet.csv").open(newline="", encoding="utf-8") as source:
            rows = list(csv.reader(source))
        self.assertEqual(len(rows[0]), 29)
        self.assertEqual(rows[0][1], "Entered Prize Categories")
        self.assertNotIn("Gemma Integration", ",".join(rows[0]))
        for row in rows[1:]:
            self.assertEqual(len(row), 29)
            if not any(row):
                continue
            total = 0
            for rating_index, weight in zip((5, 7, 9, 11, 13, 15), (15, 20, 25, 15, 10, 15)):
                rating = int(row[rating_index])
                self.assertIn(rating, range(6))
                weighted = rating / 5 * weight
                self.assertEqual(float(row[rating_index + 1]), weighted)
                total += weighted
            self.assertEqual(float(row[17]), total)


if __name__ == "__main__":
    unittest.main()
