"""Unit tests verifying Jekyll site link integrity and front matter QA."""

import unittest
import csv
import re
import os
import sys
import tempfile
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
        worksheet = (repo_root / "templates" / "downloads" / "project-proposal.md").read_text(encoding="utf-8")
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

    def test_participant_downloads_are_copy_ready_and_embedded(self):
        pairs = (
            ("problem-statement.md", "project-proposal.md"),
            ("project-readme-template.md", "README.md"),
        )
        for page_name, download_name in pairs:
            with self.subTest(template=download_name):
                page = (repo_root / "templates" / page_name).read_text(encoding="utf-8")
                download = (repo_root / "templates" / "downloads" / download_name).read_text(encoding="utf-8")
                self.assertIn(f"include_relative downloads/{download_name}", page)
                self.assertIn(f"/templates/downloads/{download_name}", page)
                self.assertFalse(download.startswith("---"))
                self.assertNotIn("{{", download)
                self.assertNotIn("{%", download)
        canvas = (repo_root / "templates" / "downloads" / "project-proposal.md").read_text(encoding="utf-8")
        for text in (
            "Team name:", "Exact model name and variant:", "Inference method, provider and runtime:",
            "Data sources and permission/licence status:", "Safety and privacy considerations",
            "How we will test normal inputs", "- [ ] Best Open-Source AI Project",
            "- [ ] Best Use of Gemma 4", "does not replace",
        ):
            self.assertIn(text, canvas)
        readme = (repo_root / "templates" / "downloads" / "README.md").read_text(encoding="utf-8")
        for heading in (
            "Features and screenshots", "Architecture and data flow", "Models, dependencies and terms",
            "Gemma 4 implementation (if applicable)", "Environment variables", "Run and test",
            "Demo", "Data sources and licences", "Known limitations, safety and privacy",
            "Team contributions", "Project source-code licence", "Acknowledgements",
        ):
            self.assertIn(f"## {heading}", readme)

    def test_submission_and_demo_guidance_preserve_verification_boundary(self):
        guide = (repo_root / "submission.md").read_text(encoding="utf-8")
        fm, _ = qa_site.parse_front_matter(guide)
        self.assertEqual(fm["permalink"], "/submission/")
        self.assertIn("nav_order", fm)
        for text in (
            "https://www.mlh.com/events/hacktoberfest-hack-day-nairobi-x-itech-club/challenges",
            "One submission can enter every category it qualifies for",
            "Authenticated host configuration is not verified",
            "no separate licence-attestation field",
            "demo URL if available",
        ):
            self.assertIn(text, guide)
        demo = (repo_root / "templates" / "demo-script.md").read_text(encoding="utf-8")
        self.assertEqual(len(re.findall(r"^[1-7]\. \*\*", demo, flags=re.MULTILINE)), 7)
        for text in ("Working journey", "Actual AI role", "Normal test and limitation",
                     "Built versus unfinished", "Reproduce and contribute"):
            self.assertIn(text, demo)
        for filename in (
            "templates/demo-script.md", "templates/submission-checklist.md",
            "judging.md", "organizer-runbook.md", "organizer-checklist.md",
        ):
            content = (repo_root / filename).read_text(encoding="utf-8")
            self.assertNotRegex(
                content,
                r"(?i)(?:two|one|three|[123])[- ]minute|120 seconds|60 seconds",
                filename,
            )

    def test_plain_markdown_downloads_are_not_treated_as_jekyll_pages(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "index.md").write_text("---\ntitle: Home\n---\n# Home\n", encoding="utf-8")
            downloads = root / "templates" / "downloads"
            downloads.mkdir(parents=True)
            (downloads / "proposal.md").write_text("# A plain planning aid\n", encoding="utf-8")
            self.assertEqual(qa_site.audit_repository(directory), 0)

    def test_score_sheet_remains_project_neutral_and_arithmetically_valid(self):
        with (repo_root / "templates" / "judge-score-sheet.csv").open(newline="", encoding="utf-8") as source:
            rows = list(csv.reader(source))
        self.assertEqual(len(rows[0]), 37)
        self.assertEqual(rows[0][1], "Entered Prize Categories")
        self.assertNotIn("Gemma Integration", ",".join(rows[0]))
        self.assertEqual(rows[-1], [""] * 37)
        self.assertEqual(len(rows[1:-1]), 3)
        for row in rows[1:]:
            self.assertEqual(len(row), 37)
            if not any(row):
                continue
            if row[36] == "Not Assessed":
                self.assertEqual(row[5:18], [""] * 13)
                self.assertEqual(row[23:29], [""] * 6)
                continue
            self.assertEqual(row[36], "Scored")
            self.assertTrue(all(row[23:29]))
            total = 0
            for rating_index, weight in zip((5, 7, 9, 11, 13, 15), (15, 20, 25, 15, 10, 15)):
                rating = int(row[rating_index])
                self.assertIn(rating, range(6))
                weighted = rating / 5 * weight
                self.assertEqual(float(row[rating_index + 1]), weighted)
                total += weighted
            self.assertEqual(float(row[17]), total)

    def test_score_sheet_category_assignments_do_not_force_entry(self):
        with (repo_root / "templates" / "judge-score-sheet.csv").open(newline="", encoding="utf-8") as source:
            examples = [row for row in csv.DictReader(source) if row["Team Name"]]
        self.assertEqual(len(examples), 3)
        for row in examples:
            entered = {name.strip() for name in row["Entered Prize Categories"].split(";")}
            considered = {name.strip() for name in row["Categories Considered By This Judge"].split(";")}
            self.assertTrue(considered <= entered)
            for category in ("Best Open-Source AI Project", "Best Use of Gemma 4"):
                with self.subTest(team=row["Team Name"], category=category):
                    status = row[f"{category} Eligibility"]
                    self.assertIn(status, ("Eligible", "Pending", "Ineligible", "Not Entered"))
                    if category not in entered:
                        self.assertEqual(status, "Not Entered")
                        self.assertEqual(row[f"{category} Eligibility Evidence"], "")
                    if category in considered:
                        self.assertEqual(status, "Eligible")
                        self.assertTrue(row[f"{category} Eligibility Evidence"])
                        self.assertTrue(row[f"{category} Category Notes"])
                    else:
                        self.assertEqual(row[f"{category} Category Notes"], "")
        self.assertEqual(examples[1]["Best Use of Gemma 4 Eligibility"], "Not Entered")
        self.assertEqual(examples[2]["Best Open-Source AI Project Eligibility"], "Not Entered")
        self.assertEqual(examples[2]["Local Overall Assessment (Scored/Not Assessed)"], "Not Assessed")

    def test_category_rubrics_are_distinct_from_official_requirements_and_local_scores(self):
        guide = (repo_root / "judging.md").read_text(encoding="utf-8")
        for text in (
            "## A. How judging works",
            "## B. Prize categories and judging criteria",
            "## C. Scoring scale",
            "## D. Final selection",
            "not official MLH-published scoring weights",
            "Gemma 4 is not required, and DigitalOcean is optional",
            "same team may receive both prizes still requires organiser/MLH confirmation",
            "A local overall score does not determine either MLH category winner",
            "iTech Club local awards",
            "Weighted score = (Judge rating / 5) × Criterion weight",
            "sum of valid judge category totals / number of valid judges",
        ):
            self.assertIn(text, guide)
        for removed in ("Why human judging is essential", "Competition Management Decision", "automated leaderboard"):
            self.assertNotIn(removed, guide)
        rubrics = (
            ("Best Open-Source AI Project", (
                ("Problem relevance and practical impact", 15),
                ("Meaningful use of open-source/open-weight AI", 20),
                ("Technical execution and working demonstration", 20),
                ("Originality and innovation", 15),
                ("Open-source quality, licensing and documentation", 20),
                ("Responsible AI, privacy and safety", 10),
            )),
            ("Best Use of Gemma 4", (
                ("Meaningful integration of Gemma 4", 25),
                ("Effective use of Gemma 4 capabilities", 20),
                ("Technical execution and working demonstration", 20),
                ("Problem relevance and usefulness", 15),
                ("Originality and innovation", 10),
                ("Responsible AI, privacy and safety", 10),
            )),
        )
        for number, (category, expected) in enumerate(rubrics, 1):
            with self.subTest(category=category):
                section = guide.split(f"### Category {number}: {category}", 1)[1].split("</section>", 1)[0]
                rows = re.findall(r"^\| ([^|]+) \| (\d+) \| ([^|]+) \|$", section, re.MULTILINE)
                self.assertEqual([(name, int(weight)) for name, weight, _ in rows], list(expected))
                self.assertTrue(all(description.strip() for _, _, description in rows))
                weights = [int(weight) for _, weight, _ in rows]
                self.assertEqual(sum(weights), 100)
                self.assertIn("| **TOTAL** | **100** |", section)
                for rating in range(6):
                    self.assertEqual(sum(rating / 5 * weight for weight in weights), rating * 20)
        scale = guide.split("## C. Scoring scale", 1)[1].split("### Weighted points", 1)[0]
        self.assertEqual(
            re.findall(r"^\| ([0-5]) \| ([^|]+) \|$", scale, re.MULTILINE),
            list(zip("012345", (
                "Not demonstrated", "Very poor", "Below expectations",
                "Meets expectations", "Very good", "Excellent",
            ))),
        )
        brief = (repo_root / "challenges" / "index.md").read_text(encoding="utf-8")
        for text in (
            "gemma-4-31b-it",
            "gemma-4-26b-a4b-it",
            "https://ai.google.dev/gemini-api/terms",
            "https://ai.google.dev/gemma/docs/core/model_card_4",
            "not mandatory domains or a requirement to build a multimodal project",
            "merely renaming a project is insufficient",
            "Open-weight and open-source are not interchangeable labels",
        ):
            self.assertIn(text, brief)

    def test_starter_launchpad_uses_real_example_files_and_safe_configuration(self):
        starter = (repo_root / "starter-kit.md").read_text(encoding="utf-8")
        fm, _ = qa_site.parse_front_matter(starter)
        self.assertEqual(fm["nav_order"], "3")
        for name in ("hosted.py", "hosted.mjs", "ollama.py", ".env.example", ".gitignore"):
            self.assertTrue((repo_root / "examples" / "gemma" / name).is_file())
            if not name.startswith("."):
                self.assertIn(f"include_relative examples/gemma/{name}", starter)
        for language, name in (("dotenv", ".env.example"), ("gitignore", ".gitignore")):
            with self.subTest(snippet=name):
                snippet = (repo_root / "examples" / "gemma" / name).read_text().strip()
                self.assertIn(f"```{language}\n{snippet}\n```", starter)
                self.assertNotIn(f"include_relative examples/gemma/{name}", starter)
        self.assertEqual(
            (repo_root / "examples" / "gemma" / ".env.example").read_text().strip(),
            "GEMINI_API_KEY=replace_with_your_api_key",
        )
        ignore = (repo_root / "examples" / "gemma" / ".gitignore").read_text().splitlines()
        self.assertIn(".env", ignore)
        self.assertIn("!.env.example", ignore)
        for section in (
            "## 1. Prerequisites", "## 2. Choose an AI execution path",
            "## 3. Choose an application architecture", "## 4. Optional DigitalOcean",
            "## 5. Open-source release", "## 6. Responsible AI", "## 7. Time-boxed",
        ):
            self.assertIn(section, starter)
        self.assertIn("https://hacktoberfest.com/my/", starter)
        self.assertIn("not a RAM requirement or performance guarantee", starter)
        self.assertIn("offline", starter)
        config = (repo_root / "_config.yml").read_text()
        self.assertIn("examples/gemma/node_modules/", config)
        self.assertIn("examples/gemma/.venv/", config)

    def test_site_qa_ignores_local_example_dependencies(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "index.md").write_text("---\ntitle: Home\n---\n# Home\n")
            for name in ("node_modules", ".venv", "__pycache__"):
                dependency = root / "examples" / "gemma" / name
                dependency.mkdir(parents=True)
                (dependency / "README.md").write_text("### Not a published page\n[bad](missing.md)")
            self.assertEqual(qa_site.audit_repository(directory), 0)


if __name__ == "__main__":
    unittest.main()
