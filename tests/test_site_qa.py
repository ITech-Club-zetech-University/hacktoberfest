"""Unit tests verifying Jekyll site link integrity and front matter QA."""

import unittest
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


if __name__ == "__main__":
    unittest.main()
