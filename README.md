# Hacktoberfest Hack Day Nairobi x iTech Club

Documentation for an open-ended, problem-driven [Hacktoberfest Hack Day Nairobi x iTech Club](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club) — **Friday 30 October 2026, 7:00 PM – Saturday 31 October 2026, 6:00 AM EAT**. Hosted by iTech Club, Zetech University, in partnership with Major League Hacking (MLH). Venue, exact build period and demo schedule require organiser reconciliation; see [rules](./rules.md).

📖 **Live Site:** `https://itech-club-zetech-university.github.io/hacktoberfest/` (hosted via GitHub Pages)

---

## Event & Award Structure

- **Open-ended projects:** Identify a real problem, choose your users and architecture, and build a focused original open-source AI MVP. No fixed prompts or primary tracks.
- **Two live MLH categories:** [Best Open-Source AI Project](https://www.mlh.com/events/hacktoberfest-hack-day-nairobi-x-itech-club/challenges/01a0d987-0c41-12ea-13ac-5b85755dc2f3) (DigitalOcean-supported) and [Best Use of Gemma 4](https://www.mlh.com/events/hacktoberfest-hack-day-nairobi-x-itech-club/challenges/01a03b87-be22-9180-5e2d-b3beeb66666d) (Gemma / Google DeepMind). These are awards, not project prompts.
- **Choice:** Other suitable open models are welcome in the broad category. DigitalOcean is optional. Follow Gemma 4/API requirements only when entering that category.
- **Human judging:** Preserve the six-criterion, 100-point process; no automated project scoring, ranking or leaderboard. Confirm separate local awards and multiple-category winner policy.
- **Submissions:** Submit once through OrganizerHQ and select every qualifying category. The live pages display **31 October, 6:00 AM EAT**; reconcile earlier local timings before publishing the coding/demo schedule. Team-size policy also requires confirmation.

---

## What's in this repository

| Path | Purpose |
|---|---|
| `index.md` | Home page and overview of the hack day |
| `rules.md` | Official MLH rules, local award policies, teams, timeline, and submission guidelines |
| `starter-kit.md` | Step-by-step Gemma setup guide (Gemini API and local Ollama) |
| `resources.md` | Curated documentation links for Gemma, Agent Skills, and MLH |
| `challenges/` | Open-ended project brief and five preserved, nav/search-excluded historical briefs |
| `inspiration.md` | Optional problem-led examples, not mandatory tracks |
| `templates/problem-statement.md` | Quick idea-development worksheet |
| `judging.md` | The human-led 100-point rubric, 0–5 rating scales, scoring anchors, tie-breakers, 9-step judging workflow, and MLH winner recording |
| `code-of-conduct.md` | MLH Code of Conduct and local reporting procedures |
| `faq.md` | Frequently asked questions |
| `organizer-runbook.md` | Public event runbook, operational checklists, staff roles, and MLH winner marking workflow |
| `organizer-checklist.md` | Chronological quick-reference checklist for event leads and mentors |
| `templates/project-readme-template.md` | Copy-and-fill `README.md` template for participant repositories |
| `templates/demo-script.md` | Project-neutral 2-minute live demo and 1-minute Q&A |
| `templates/submission-checklist.md` | Publishing, testing and category-specific submission checks |
| `templates/judge-score-sheet.csv` | Ready-to-import scoring sheet for judges (keep completed scores in private drive) |
| `references/source-register.md` | Organiser source register, verification status, and review log |
| `scripts/check_submission.py` | Automated preliminary eligibility checker for baseline repo hygiene |
| `scripts/data/osi-approved-licenses.json` | Canonical OSI-approved SPDX license database |
| `tests/test_check_submission.py` | Comprehensive offline unit test suite (43 tests) |
| `_config.yml` | Jekyll / Just the Docs theme configuration |

---

## For Organisers

Operational documentation and administrative tools for running the hackathon:

- **[Organiser Runbook](./organizer-runbook.md):** Complete master timeline, staff roles, offline contingency procedures, score tabulation, and official MLH winner marking steps.
- **[Organiser Quick-Reference Checklist](./organizer-checklist.md):** Chronological checklist from T-minus 24 hours through doors opening (6:30 PM) to post-event reporting.
- **[Source-of-Truth Register](./references/source-register.md):** Verified reference log for event policies, API endpoints, model tags, and license terms.
- **Privacy & Access Control:** Completed judge scoring sheets, internal deliberation notes, and incident records must be maintained exclusively in an internal, access-controlled organizer drive. Never commit completed scores or private attendee data to git.

---

## For Organisers: publishing with GitHub Pages

This documentation site is built with Jekyll and the [Just the Docs](https://github.com/just-the-docs/just-the-docs) theme, deployed automatically via **GitHub Actions**:

1. **Verify Git State First:** Before pushing, inspect your local repository state to avoid overwriting existing history:
   ```bash
   git status
   git remote -v
   git branch
   ```
   Ensure you are on the `main` branch connected to `https://github.com/ITech-Club-zetech-University/hacktoberfest.git`. Never force-push (`git push --force`) or reinitialize an existing repository.
2. **Push to GitHub:**
   ```bash
   git push origin main
   ```
3. **Configure GitHub Pages Source:**
   - In your repository on GitHub, navigate to **Settings → Pages**.
   - Under **Build and deployment → Source**, select **GitHub Actions** (do *not* select "Deploy from a branch").
   - Once selected, pushes to `main` automatically run the [`.github/workflows/deploy.yml`](./.github/workflows/deploy.yml) workflow, run the test suite and QA link checks, compile the site, and publish the artifact.
4. **Site Address:**
   The site publishes at `https://itech-club-zetech-university.github.io/hacktoberfest/`.

### Previewing locally (optional)

To preview the documentation site locally on your workstation, you need Ruby 3.x with development headers (`ruby-dev` and `build-essential` on Debian/Ubuntu):

```bash
# 1. Install dependencies specified in Gemfile
bundle install

# 2. Start the local Jekyll preview server
bundle exec jekyll serve

# 3. Open in your browser:
# http://localhost:4000/hacktoberfest/
```

*Note on local environment headers:* If your local system lacks Ruby development headers (e.g., `mkmf` missing `ruby.h` when compiling native extensions like `http_parser`), you can run the test build using the containerized command or rely on the GitHub Actions pipeline:
```bash
docker run --rm -v "$(pwd)":/app -w /app ruby:3.2-alpine sh -c "apk add --no-cache build-base && bundle install && bundle exec jekyll build"
```

### Running the preliminary eligibility checker

The repository includes a lightweight, automated preliminary hygiene gate for submissions:

```bash
# Check one or more repositories
python3 scripts/check_submission.py https://github.com/team-one/repo https://github.com/team-two/repo

# Run the complete automated test suite (offline, mocked)
python3 -m unittest discover -s tests -v
```

**What it checks:** Genuine GitHub repository URL parsing (`github.com` and `www.github.com` only), public repository visibility, root `README.md`, open-source software license validated against canonical OSI-approved SPDX identifiers from `scripts/data/osi-approved-licenses.json` (sourced from [SPDX License List v3.26](https://spdx.org/licenses/) and [OSI](https://opensource.org/licenses/), last reviewed 20 October 2026), Gemma mentions in the README (labeled as a weak signal only), and `SKILL.md` presence when `--track 1` is specified.

**What it does NOT check:** It does not score code quality, evaluate model performance, verify whether Gemma generated outputs, or serve as an automated leaderboard. It never clones or executes participant code.

**Legacy compatibility:** `--track 1` is an old skill-file probe, not a current competition track. The checker can send non-Gemma projects to manual review; absence of Gemma must not exclude an otherwise qualifying open-model project. Review category eligibility manually and do not demand a misleading README keyword.

**Exit codes:**
- `0`: All checked repositories are `ELIGIBLE (PASS)`.
- `1`: At least one repository is `CLEARLY INELIGIBLE`.
- `2`: At least one repository is `NEEDS MANUAL REVIEW` or `CHECK UNAVAILABLE`.
- `3`: Usage or syntax error.

Inconclusive results (such as network timeouts or GitHub API 403/429 rate limits) must **never** be treated as noncompliance; organizers inspect repositories manually in a browser. See [`judging.md`](./judging.md#preliminary-eligibility-gate-vs-scoring) for complete operational details.

---

## License

The contents of this documentation repository are licensed under the MIT License — see [`LICENSE`](./LICENSE). Participant hackathon projects are independent works licensed under their authors' chosen open-source licenses.
