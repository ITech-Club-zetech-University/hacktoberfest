# Hacktoberfest Hack Day Nairobi x iTech Club

Documentation for an open-ended, problem-driven [Hacktoberfest Hack Day Nairobi x iTech Club](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club) — **Friday 30 October 2026, 7:00 PM – Saturday 31 October 2026, 6:00 AM EAT**, at **Zetech University, Ruiru Campus**. Hosted by iTech Club in partnership with Major League Hacking (MLH). Follow the [rules](./rules.md) and event briefing for coding and demo sessions.

📖 **Live Site:** `https://itech-club-zetech-university.github.io/hacktoberfest/` (hosted via GitHub Pages)

---

## Event & Award Structure

- **Open-ended projects:** Identify a real problem, choose your users and architecture, and build a focused original software or AI MVP. No fixed prompts or primary tracks.
- **Three event categories:** [Best Open-Source AI Project](https://www.mlh.com/events/hacktoberfest-hack-day-nairobi-x-itech-club/challenges/01a0d987-0c41-12ea-13ac-5b85755dc2f3) (DigitalOcean), [Best Use of Gemma 4](https://www.mlh.com/events/hacktoberfest-hack-day-nairobi-x-itech-club/challenges/01a03b87-be22-9180-5e2d-b3beeb66666d) (Google DeepMind / Gemma), and [Best Project Deployed on PrimeCloud](./challenges/index.md#best-project-deployed-on-primecloud) (PrimeCloud). The first two have verified public MLH listings; configure/verify PrimeCloud in authenticated HQ before accepting entries. These are awards, not project prompts.
- **Choice:** Gemma 4 is required only for its category; PrimeCloud deployment only for its category, which does not require AI. Other suitable open models are welcome for Best Open-Source AI Project. DigitalOcean is optional.
- **PrimeCloud prize:** **PrimeCloud Production Plan – 3 Months**. The winning developer will receive three months of PrimeCloud Production, with access to the standard Production plan features and allowances.
- **Human judging:** Review each eligible category pool separately using proposed organiser rubrics, not official sponsor/MLH-published weights. Each category is out of 100; never combine three scores. The retained local overall rubric is separate. Approval and award-policy decisions are tracked in [repository-only organiser documentation](./_internal/organiser/publication-decisions.md).
- **Submissions:** Submit once through OrganizerHQ and select every qualifying category. The live pages display **31 October, 6:00 AM EAT**; reconcile earlier local timings before publishing the coding/demo schedule. Team-size policy also requires confirmation.

---

## What's in this repository

| Path | Purpose |
|---|---|
| `index.md` | Home page and overview of the hack day |
| `rules.md` | Official MLH rules, local award policies, teams, timeline, and submission guidelines |
| `starter-kit.md` | Optional-stack guide: hosted/local Gemma 4, architecture, DigitalOcean, PrimeCloud deployment preparation, safe release and time-boxed workflow |
| `examples/gemma/` | Runnable Python/JavaScript hosted text/image examples, local Ollama client and scoped dependency manifests |
| `resources.md` | Official Gemma, DigitalOcean, PrimeCloud, Agent Skills, GitHub and MLH resources |
| `challenges/` | Current open-ended participant project brief |
| `_internal/archives/challenges/` | Five full historical briefs, preserved but excluded from publication |
| `inspiration.md` | Optional problem-led examples, not mandatory tracks |
| `templates/problem-statement.md` | Project proposal / idea canvas with a plain Markdown download |
| `templates/downloads/` | Copy-ready Markdown canvas and README, without Jekyll front matter or Liquid tags |
| `submission.md` | Participant submission workflow, multiple-category entry and saved-entry checking |
| `judging.md` | Category rubrics, scoring scale, independent reviews and human selection |
| `code-of-conduct.md` | MLH Code of Conduct and local reporting procedures |
| `faq.md` | Frequently asked questions |
| `organizer-runbook.md` | Repository-only event runbook, excluded from the published Jekyll site |
| `organizer-checklist.md` | Chronological quick-reference checklist for event leads and mentors |
| `templates/project-readme-template.md` | Copy-and-fill `README.md` template for participant repositories |
| `templates/demo-script.md` | Seven-part working demo flow using organiser-confirmed presentation/Q&A allowances |
| `templates/submission-checklist.md` | Publishing, testing and category-specific submission checks |
| `_internal/organiser/` | Uncompleted category/local judge templates and non-sensitive publication decision records; excluded from Jekyll |
| `references/source-register.md` | Organiser source register, verification status, and review log |
| `scripts/check_submission.py` | Automated preliminary eligibility checker for baseline repo hygiene |
| `scripts/data/osi-approved-licenses.json` | Canonical OSI-approved SPDX license database |
| `tests/test_check_submission.py` | Comprehensive offline unit test suite (43 tests) |
| `_config.yml` | Jekyll / Just the Docs theme configuration |

---

## For Organisers

Operational documentation and administrative tools for running the hackathon:

The runbook, organiser checklist, source register, QA report and `_internal/` are excluded from the Jekyll build. Their sources remain in this public repository: exclusion does not make them confidential. Never add secrets or private operational data.

- **[Organiser Runbook](./organizer-runbook.md):** Complete master timeline, staff roles, offline contingency procedures, score tabulation, and official MLH winner marking steps.
- **[Organiser Quick-Reference Checklist](./organizer-checklist.md):** Chronological checklist from T-minus 24 hours through doors opening (6:30 PM) to post-event reporting.
- **[Source-of-Truth Register](./references/source-register.md):** Verified reference log for event policies, API endpoints, model tags, and license terms.
- **[Publication decisions](./_internal/organiser/publication-decisions.md):** Outstanding approvals and confirmed public facts.
- **[Category score sheet](./_internal/organiser/category-score-sheet.md):** Independent sheets matching the proposed category rubrics.
- **[PrimeCloud score sheet](./_internal/organiser/primecloud-score-sheet.md):** Separate five-criterion proposed rubric and genuine deployment evidence.
- **[Local score CSV](./_internal/organiser/judge-score-sheet.csv):** Retained local-only numerical template with fictional examples.
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
   - Before uploading, the workflow runs `python3 scripts/qa_publication.py _site`
     against the exact generated output. It rejects internal/archived pages,
     unintended download navigation/search entries, changed raw downloads,
     duplicate headings/IDs and broken local links.
   - Do not enable a simultaneous legacy branch build: its optional-front-matter
     processing can turn raw Markdown downloads into extra navigation pages.
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

### Checking starter examples offline

Install only the dependencies for the language being checked; do not install both stacks merely to attend the event:

```bash
# In an isolated Python environment:
python -m pip install -r examples/gemma/requirements.txt
PYTHONPATH=tests python -m unittest test_starter_examples test_site_qa -v

# If checking the JavaScript example:
npm ci --prefix examples/gemma
node --test tests/starter_examples.test.mjs
```

These tests use fake credentials and mock transports, not paid API calls or model downloads. Python hosted checks explicitly skip if the optional SDK dependencies are absent; run with the declared dependencies to verify that path. The local example uses only the standard library. See the [starter kit](./starter-kit.md) for live smoke-test instructions and the verification boundary.

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

Inconclusive results (such as network timeouts or GitHub API 403/429 rate limits) must **never** be treated as noncompliance; organisers inspect repositories manually in a browser. See the [runbook](./organizer-runbook.md) for operational details.

---

## License

The contents of this documentation repository are licensed under the MIT License — see [`LICENSE`](./LICENSE). Participant hackathon projects are independent works licensed under their authors' chosen open-source licenses.
