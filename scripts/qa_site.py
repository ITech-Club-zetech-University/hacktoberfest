#!/usr/bin/env python3
"""
Lightweight Site QA and Internal Link Validator for Hacktoberfest Hack Day Nairobi.

Validates:
1. Markdown front matter and navigation parent/child hierarchies.
2. Internal links (including {{ site.baseurl }} and relative links).
3. Anchor targets against generated and explicit kramdown heading IDs.
4. Heading level progression (flags skipped levels, e.g. H1 -> H3).

Zero external dependencies: uses Python standard library only.
Exit code:
  0: All QA checks passed.
  1: Issues or broken links detected.
"""

import sys
import os
import re
import glob
from pathlib import Path


def kramdown_slug(text: str) -> str:
    """Simulate kramdown heading ID generation."""
    # Remove explicit IAL if present
    text = re.sub(r"\{:\s*#[a-zA-Z0-9_-]+\s*\}", "", text)
    text = re.sub(r"\{:.*?\}", "", text)
    # Remove markdown links
    text = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", text)
    # Remove markdown emphasis/code
    text = re.sub(r"[`*_~]", "", text)
    # Non-alphanumeric to hyphen
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return slug


def parse_front_matter(content: str):
    """Extract YAML front matter if present."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        return {}, content
    fm_raw = match.group(1)
    body = content[match.end():]
    fm = {}
    for line in fm_raw.splitlines():
        line = line.strip()
        if ":" in line and not line.startswith("#"):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip("\"'")
    return fm, body


def audit_repository(repo_root: str):
    root_path = Path(repo_root).resolve()
    errors = []
    warnings = []

    # Excluded directories and files
    exclude_dirs = {"scripts", "tests", "vendor", ".bundle", "_site", ".git", ".github"}
    exclude_files = {"README.md", "LICENSE"}

    all_md_files = []
    for p in root_path.rglob("*.md"):
        rel_parts = p.relative_to(root_path).parts
        if any(part in exclude_dirs for part in rel_parts):
            continue
        all_md_files.append(p)

    all_md_files.sort()

    pages = {}
    title_to_page = {}
    url_to_page = {}

    # Pass 1: Parse pages, headings, and URLs
    for p in all_md_files:
        rel_str = str(p.relative_to(root_path))
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()

        fm, body = parse_front_matter(content)
        title = fm.get("title")

        # Derive expected URL
        permalink = fm.get("permalink")
        if not permalink:
            # Jekyll default with permalink: pretty
            stem = p.stem
            if stem == "index":
                parent_dir = p.parent.relative_to(root_path)
                if str(parent_dir) == ".":
                    permalink = "/"
                else:
                    permalink = f"/{parent_dir}/"
            else:
                rel_without_ext = p.relative_to(root_path).with_suffix("")
                permalink = f"/{rel_without_ext}/"

        if not permalink.endswith("/") and not permalink.endswith(".html"):
            permalink += "/"

        # Collect headings and anchors
        headings = []
        anchors = set()
        in_code = False
        last_level = 0

        for line_num, line in enumerate(body.splitlines(), 1):
            stripped = line.strip()
            if stripped.startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue

            # Check explicit block IAL right after heading
            ial_match = re.match(r"^\{:\s*([#a-zA-Z0-9_\s-]+)\s*\}", stripped)
            if ial_match:
                for token in ial_match.group(1).split():
                    if token.startswith("#"):
                        anchors.add(token[1:])

            h_match = re.match(r"^(#{1,6})\s+(.*)$", line)
            if h_match:
                level = len(h_match.group(1))
                htext = h_match.group(2).strip()

                # Check inline explicit ID: {: #my-id }
                inline_id = re.search(r"\{:\s*#([a-zA-Z0-9_-]+)\s*\}", htext)
                if inline_id:
                    anchor = inline_id.group(1)
                    anchors.add(anchor)
                else:
                    anchor = kramdown_slug(htext)
                    if anchor:
                        anchors.add(anchor)

                # Check heading hierarchy
                if last_level == 0:
                    if level != 1:
                        warnings.append(f"{rel_str}:{line_num} - Initial heading is H{level} ('{htext}'), expected H1.")
                else:
                    if level > last_level + 1:
                        errors.append(f"{rel_str}:{line_num} - Skipped heading level from H{last_level} to H{level} ('{htext}').")
                last_level = level
                headings.append((level, htext, anchor))

        pages[rel_str] = {
            "path": p,
            "fm": fm,
            "title": title,
            "permalink": permalink,
            "anchors": anchors,
            "content": content
        }

        if title:
            title_to_page[title] = rel_str

        # Register URL mappings
        url_to_page[permalink] = rel_str
        clean_url = permalink.rstrip("/")
        if clean_url:
            url_to_page[clean_url] = rel_str
            url_to_page[clean_url + ".html"] = rel_str

    # Pass 2: Validate Front Matter Hierarchy
    for rel_str, page in pages.items():
        fm = page["fm"]
        if not fm and rel_str not in exclude_files:
            errors.append(f"{rel_str} - Missing Jekyll front matter.")
            continue

        parent = fm.get("parent")
        if parent:
            if parent not in title_to_page:
                errors.append(f"{rel_str} - Parent page '{parent}' not found in any page title.")
            else:
                parent_rel = title_to_page[parent]
                parent_fm = pages[parent_rel]["fm"]
                if not parent_fm.get("has_children") and parent_fm.get("has_children") != "true":
                    errors.append(f"{rel_str} - Parent page '{parent}' ({parent_rel}) does not declare 'has_children: true'.")

    # Pass 3: Validate Links and Anchors
    link_count = 0
    anchor_count = 0

    for rel_str, page in pages.items():
        content = page["content"]
        # Extract markdown links [text](target)
        links = re.findall(r"\[([^\]]*)\]\(([^)]+)\)", content)
        for text, target in links:
            # Skip external or protocol links
            if target.startswith(("http://", "https://", "mailto:", "tel:", "javascript:")):
                continue

            link_count += 1
            url_part = target
            anchor_part = None
            if "#" in target:
                url_part, anchor_part = target.split("#", 1)

            # Resolve target URL
            target_page_rel = None

            if not url_part or url_part == ".":
                # Self-page anchor
                target_page_rel = rel_str
            else:
                # Strip Jekyll liquid variable
                clean_target = url_part.replace("{{ site.baseurl }}", "").replace("{{site.baseurl}}", "")
                
                # Check direct path relative to repo or file
                if clean_target.startswith("/"):
                    resolved_url = clean_target
                    if resolved_url in url_to_page:
                        target_page_rel = url_to_page[resolved_url]
                    elif (resolved_url + "/") in url_to_page:
                        target_page_rel = url_to_page[resolved_url + "/"]
                elif clean_target.startswith("./") or not clean_target.startswith("/"):
                    # Relative link from current file
                    curr_dir = Path(rel_str).parent
                    candidate = (curr_dir / clean_target).as_posix()
                    # Normalize
                    candidate_clean = os.path.normpath(candidate)
                    if candidate_clean in pages:
                        target_page_rel = candidate_clean
                    elif (candidate_clean + ".md") in pages:
                        target_page_rel = candidate_clean + ".md"
                    elif "/" + candidate_clean + "/" in url_to_page:
                        target_page_rel = url_to_page["/" + candidate_clean + "/"]

            if not target_page_rel:
                # Check if it resolves to an existing file on the filesystem (e.g. LICENSE, workflow, script)
                curr_dir = Path(rel_str).parent
                clean_target = url_part.replace("{{ site.baseurl }}", "").replace("{{site.baseurl}}", "")
                if clean_target.startswith("/"):
                    direct_file = root_path / clean_target.lstrip("/")
                else:
                    direct_file = (root_path / curr_dir / clean_target).resolve()

                if direct_file.is_file():
                    # Valid existing file on filesystem
                    continue

                # Check if file exists at repo root (e.g. templates referencing repo-root LICENSE)
                root_direct_file = root_path / clean_target.lstrip("./")
                if root_direct_file.is_file():
                    continue

                errors.append(f"{rel_str} - Broken internal link '{target}' (text: '{text}'). Target file or page could not be resolved.")
                continue

            # If anchor is present, verify it exists in target page
            if anchor_part:
                anchor_count += 1
                target_anchors = pages[target_page_rel]["anchors"]
                if anchor_part not in target_anchors:
                    errors.append(
                        f"{rel_str} - Broken anchor '#{anchor_part}' in link '{target}' pointing to '{target_page_rel}'. "
                        f"Target page has {len(target_anchors)} valid anchors."
                    )

    # Print summary
    print("=" * 60)
    print(" Jekyll Site QA & Link Audit Report")
    print("=" * 60)
    print(f"  Pages checked         : {len(pages)}")
    print(f"  Internal links checked: {link_count}")
    print(f"  Anchor targets verified: {anchor_count}")
    print(f"  Errors detected       : {len(errors)}")
    print(f"  Warnings detected     : {len(warnings)}")
    print("=" * 60)

    if warnings:
        print("\n[!] WARNINGS:")
        for w in warnings:
            print(f"  - {w}")

    if errors:
        print("\n[x] ERRORS:")
        for e in errors:
            print(f"  - {e}")
        print("\nRESULT: FAILED (issues detected)\n")
        return 1

    print("\nRESULT: PASSED (all internal links, anchors, and front matter are valid)\n")
    return 0


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    exit_code = audit_repository(base_dir)
    sys.exit(exit_code)
