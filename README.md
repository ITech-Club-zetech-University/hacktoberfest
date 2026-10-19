# Hacktoberfest Hack Day Nairobi x iTech Club

Event docs, rules, starter kit, and preset Gemma challenges for the [Hacktoberfest Hack Day Nairobi x iTech Club](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club) — **Friday 30 October 2026, 7:00 PM – Saturday 31 October 2026, 6:00 AM EAT**, at Zetech University Technology Park, hosted by iTech Club in partnership with MLH, sponsored by Gemma.

📖 **Read the full site:** `https://itech-club-zetech-university.github.io/hacktoberfest/` (live once GitHub Pages is enabled — see below)

## What's in this repo

| Path | Purpose |
|---|---|
| `index.md` | Home page |
| `rules.md` | General rules & regulations (eligibility, teams, timeline, submission, code of conduct) |
| `starter-kit.md` | Step-by-step Gemma setup guide |
| `resources.md` | Curated Gemma + MLH resource links |
| `challenges/` | The 5 preset challenge tracks |
| `judging.md` | The leaderboard-vs-judges decision, the rubric, and the judging process |
| `code-of-conduct.md` | MLH Code of Conduct adoption + how to report a concern on-site |
| `faq.md` | Quick answers |
| `templates/judge-score-sheet.csv` | Importable judge scoring sheet |
| `templates/submission-checklist.md` | Checklist teams can paste into their own README |
| `scripts/check_submission.py` | Automated **eligibility** checker (not a scoring/ranking tool — see `judging.md`) |
| `_config.yml` | Jekyll / [Just the Docs](https://just-the-docs.com/) site configuration |

## For organizers: publishing this with GitHub Pages

This site uses the [Just the Docs](https://github.com/just-the-docs/just-the-docs) Jekyll theme via `remote_theme`, which GitHub Pages builds automatically — **no local Ruby install or Gemfile needed.**

1. Push this repo to `github.com/ITech-Club-zetech-University/hacktoberfest` (see commands below).
2. On GitHub: **Settings → Pages**.
3. Under **Build and deployment → Source**, choose **Deploy from a branch**.
4. Branch: **`main`**, folder: **`/ (root)`** → **Save**.
5. Wait 1–2 minutes, then the site is live at `https://itech-club-zetech-university.github.io/hacktoberfest/`.

If your org has GitHub Pages restricted, an org owner needs to allow Pages for this repository first (**Organization settings → Pages**).

### Pushing this repo for the first time

From inside this folder:

```bash
git init
git add -A
git commit -m "Set up Hacktoberfest Hack Day Nairobi x iTech Club site"
git branch -M main
git remote add origin https://github.com/ITech-Club-zetech-University/hacktoberfest.git
git push -u origin main
```

### Previewing locally (optional)

```bash
gem install bundler jekyll
bundle init
echo 'gem "jekyll"' >> Gemfile
echo 'gem "just-the-docs"' >> Gemfile
bundle install
bundle exec jekyll serve
# open http://localhost:4000/hacktoberfest/
```

### Running the eligibility checker

```bash
python3 scripts/check_submission.py https://github.com/some-team/their-repo
```

See `judging.md` for what this script does and doesn't do.

## Updating content

Every page is plain Markdown with [Just the Docs front matter](https://just-the-docs.com/docs/navigation-structure/) (`title`, `nav_order`, `parent`, etc.) at the top. Edit the `.md` file, commit, and push — GitHub Pages rebuilds automatically within a minute or two.

## License

The contents of this repository (docs, templates, scripts) are MIT-licensed — see `LICENSE`. Hackathon participants' own projects are separate works under their own chosen open-source license.
