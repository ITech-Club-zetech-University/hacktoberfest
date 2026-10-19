# Hacktoberfest Hack Day Nairobi x iTech Club

Documentation site, rules, starter kit, and preset Gemma challenge tracks for the [Hacktoberfest Hack Day Nairobi x iTech Club](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club) — **Friday 30 October 2026, 7:00 PM – Saturday 31 October 2026, 6:00 AM EAT**, at Zetech University Technology Park, Mang'u Campus. Hosted by iTech Club in partnership with Major League Hacking (MLH), sponsored by Gemma.

📖 **Live Site:** `https://itech-club-zetech-university.github.io/hacktoberfest/` (hosted via GitHub Pages)

---

## Event & Award Structure

- **Official MLH Challenge:** [Best Open-Source AI Project](https://hacktoberfest-handbook.mlh.com/fest-planning-guide/open-source-prize-categories) is the official competition on [MLH OrganizerHQ](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club), with **one winning team** across the event.
- **iTech Club Preset Tracks:** 5 guided technical tracks designed for an ~8-hour build on consumer laptops using Gemma. Teams declare **one primary track** for local evaluation and track honors.
- **Team Size:** Teams of **3–4 members** for local track award eligibility; solo hackers and pairs are welcome to attend, build, and submit to the general MLH competition.
- **Submissions:** All projects are submitted to "Best Open-Source AI Project" on OrganizerHQ, with the primary preset track declared in the project `README.md`.

---

## What's in this repository

| Path | Purpose |
|---|---|
| `index.md` | Home page and overview of the hack day |
| `rules.md` | Official MLH rules, local award policies, teams, timeline, and submission guidelines |
| `starter-kit.md` | Step-by-step Gemma setup guide (Gemini API and local Ollama) |
| `resources.md` | Curated documentation links for Gemma, Agent Skills, and MLH |
| `challenges/` | The 5 preset challenge briefs and comparison index |
| `judging.md` | The 100-point rubric, judge demo checklist, winner marking, and source register |
| `code-of-conduct.md` | MLH Code of Conduct and local reporting procedures |
| `faq.md` | Frequently asked questions |
| `templates/judge-score-sheet.csv` | Ready-to-import scoring sheet for judges |
| `templates/submission-checklist.md` | Participant checklist to copy into project repositories |
| `scripts/check_submission.py` | Automated eligibility checker for basic repo hygiene |
| `_config.yml` | Jekyll / Just the Docs theme configuration |

---

## For organizers: publishing with GitHub Pages

This site uses the [Just the Docs](https://github.com/just-the-docs/just-the-docs) Jekyll theme via `remote_theme`, which GitHub Pages builds automatically without local Ruby setup:

1. Push this repository to `github.com/ITech-Club-zetech-University/hacktoberfest`.
2. On GitHub, navigate to **Settings → Pages**.
3. Under **Build and deployment → Source**, choose **Deploy from a branch**.
4. Set Branch to **`main`** and folder to **`/ (root)`**, then click **Save**.
5. The site will publish at `https://itech-club-zetech-university.github.io/hacktoberfest/`.

### Previewing locally (optional)

```bash
gem install bundler jekyll
bundle init
echo 'gem "jekyll"' >> Gemfile
echo 'gem "just-the-docs"' >> Gemfile
bundle install
bundle exec jekyll serve
# Open http://localhost:4000/hacktoberfest/
```

### Running the eligibility checker

```bash
python3 scripts/check_submission.py https://github.com/some-team/their-repo
```

See `judging.md` for details on the automated checks versus human qualitative judging.

---

## License

The contents of this documentation repository are licensed under the MIT License — see [`LICENSE`](./LICENSE). Participant hackathon projects are independent works licensed under their authors' chosen open-source licenses.
