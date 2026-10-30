#!/usr/bin/env python3
"""Validate the exact generated participant handbook before uploading Pages."""

import argparse
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import posixpath
import re
from urllib.parse import unquote, urlsplit


PARTICIPANT_PAGES = (
    "index.html", "rules/index.html", "starter-kit/index.html",
    "resources/index.html", "challenges/index.html", "inspiration/index.html",
    "submission/index.html", "judging/index.html", "code-of-conduct/index.html",
    "faq/index.html", "templates/problem-statement/index.html",
    "templates/project-readme-template/index.html", "templates/demo-script/index.html",
    "templates/submission-checklist/index.html",
)
DOWNLOADS = (
    "templates/downloads/README.md", "templates/downloads/project-proposal.md",
    "examples/gemma/hosted.py", "examples/gemma/hosted.mjs", "examples/gemma/ollama.py",
    "examples/gemma/requirements.txt", "examples/gemma/package.json",
    "examples/gemma/package-lock.json",
)
FORBIDDEN_PATHS = (
    "_internal/", "organizer-runbook/", "organizer-checklist/",
    "references/source-register/", "QA-REPORT/", "QA-REPORT.md",
    "templates/judge-score-sheet.csv", "scripts/", "tests/",
    "templates/downloads/index.html", "templates/downloads/project-proposal/",
    "_config.yml", "Gemfile", "Gemfile.lock", "README.md", ".git/", ".github/",
)
EDITORIAL_TEXT = re.compile(
    r"organiser confirmation required|awaiting lead organiser confirmation|"
    r"verification status before publication|authenticated host configuration is not verified|"
    r"staff should reconcile|pending confirmation before judging",
    re.IGNORECASE,
)


def forbidden_path(path):
    return (
        any(path == item.rstrip("/") or path.startswith(item) for item in FORBIDDEN_PATHS)
        or bool(re.match(r"challenges/0[1-5]-", path))
        or "node_modules" in Path(path).parts
        or "__pycache__" in Path(path).parts
        or ".venv" in Path(path).parts
    )


class PublicationPage(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.references = []
        self.navigation = []
        self.stylesheets = []
        self.heading_count = 0
        self.heading_text = []
        self.in_heading = False
        self.text = []
        self.nav_depth = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "nav":
            self.nav_depth += 1
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "h1":
            self.heading_count += 1
            self.in_heading = True
        for attribute in ("href", "src"):
            if attrs.get(attribute):
                self.references.append(attrs[attribute])
        if tag == "a" and self.nav_depth and attrs.get("href"):
            self.navigation.append(attrs["href"])
        if tag == "link" and attrs.get("rel") == "stylesheet":
            self.stylesheets.append(attrs.get("href"))

    def handle_endtag(self, tag):
        if tag == "nav":
            self.nav_depth -= 1
        if tag == "h1":
            self.in_heading = False

    def handle_data(self, data):
        self.text.append(data)
        if self.in_heading:
            self.heading_text.append(data)


def audit_publication(site_root: Path, source_root: Path, baseurl="/hacktoberfest"):
    site_root = site_root.resolve()
    baseurl = baseurl.rstrip("/")
    errors = []
    pages = {}
    if not site_root.is_dir():
        return [f"Missing generated site: {site_root}"]

    for path in site_root.rglob("*"):
        relative = path.relative_to(site_root).as_posix()
        if forbidden_path(relative):
            errors.append(f"Repository-only or unintended output: {relative}")
        if path.is_file() and path.suffix == ".html":
            if relative not in PARTICIPANT_PAGES:
                errors.append(f"Unexpected HTML page: {relative}")
            page = PublicationPage()
            page.feed(path.read_text(encoding="utf-8"))
            pages[relative] = page

    for required in PARTICIPANT_PAGES:
        if required not in pages:
            errors.append(f"Missing participant page: {required}")
    for relative in DOWNLOADS:
        output = site_root / relative
        source = source_root / relative
        if not output.is_file():
            errors.append(f"Missing participant download: {relative}")
        elif not source.is_file() or output.read_bytes() != source.read_bytes():
            errors.append(f"Participant download changed during generation: {relative}")

    for relative, page in pages.items():
        if not page.stylesheets:
            errors.append(f"Missing theme stylesheet: {relative}")
        if page.heading_count != 1:
            errors.append(f"Expected one H1 in {relative}, found {page.heading_count}")
        if "[Project Name]" in "".join(page.heading_text):
            errors.append(f"Template placeholder used as page heading: {relative}")
        if EDITORIAL_TEXT.search(" ".join(page.text)):
            errors.append(f"Internal editorial text in participant page: {relative}")
        for identity, count in Counter(page.ids).items():
            if count > 1:
                errors.append(f"Duplicate ID in {relative}: {identity}")
        for href in page.navigation:
            if "/templates/downloads/" in href:
                errors.append(f"Raw download leaked into navigation: {relative}: {href}")

        page_url = "/" + relative
        if page_url.endswith("index.html"):
            page_url = page_url.removesuffix("index.html")
        for reference in page.references:
            url = urlsplit(reference)
            if url.scheme or url.netloc:
                continue
            path = unquote(url.path)
            if baseurl and (path == baseurl or path.startswith(baseurl + "/")):
                path = path[len(baseurl):] or "/"
            elif baseurl and path.startswith("/"):
                errors.append(f"Link outside baseurl in {relative}: {reference}")
                continue
            target_url = (
                posixpath.normpath(posixpath.join(posixpath.dirname(page_url), path))
                if path else page_url
            )
            target = site_root / target_url.lstrip("/")
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                errors.append(f"Missing target in {relative}: {reference}")
                continue
            target_relative = target.relative_to(site_root).as_posix()
            target_page = pages.get(target_relative)
            if url.fragment and target_page and unquote(url.fragment) not in target_page.ids:
                errors.append(f"Missing anchor in {relative}: {reference}")

    search_path = site_root / "assets/js/search-data.json"
    if not search_path.is_file():
        errors.append("Missing participant search index")
    else:
        search = search_path.read_text(encoding="utf-8").replace("\\/", "/")
        for marker in (
            "/organizer-runbook", "/organizer-checklist", "/references/source-register",
            "/_internal/", "/templates/downloads/", "/challenges/01-", "/challenges/02-",
            "/challenges/03-", "/challenges/04-", "/challenges/05-",
        ):
            if marker in search:
                errors.append(f"Repository-only/unintended page in search index: {marker}")
    return sorted(set(errors))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path)
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--baseurl", default="/hacktoberfest")
    args = parser.parse_args()
    errors = audit_publication(args.site, args.source, args.baseurl)
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"Publication audit failed: {len(errors)} issue(s).")
        return 1
    print("Publication audit passed: participant pages, raw downloads, links, navigation and search.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
