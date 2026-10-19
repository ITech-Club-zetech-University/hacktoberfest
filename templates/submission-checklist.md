# Submission checklist

Copy this into your team's README or a project issue, and tick through it before the submission deadline.

## Repository

- [ ] Repository is **public**
- [ ] `LICENSE` file at the repo root (MIT, Apache-2.0, GPL-3.0, or another [OSI-approved license](https://opensource.org/licenses))
- [ ] `README.md` states:
  - [ ] What the project does, in 2–3 sentences
  - [ ] Which Gemma model/variant is used, and how
  - [ ] Which challenge track(s) you're entering
  - [ ] How to run it (setup steps, not just "see the code")
  - [ ] Who built it (team members)
  - [ ] Which AI coding tools (if any) you used while building
- [ ] No secrets (API keys, tokens) committed anywhere in the history — check with `git log -p | grep -i key` if unsure
- [ ] Ran [`scripts/check_submission.py`](../scripts/check_submission.py) against your repo URL with no failing checks

## Challenge-specific

- [ ] (Challenge 1 only) `SKILL.md` present and follows the [Agent Skills spec](https://agentskills.io/specification)
- [ ] (Challenge 2 only) Confirmed the demo runs with Wi-Fi/data off
- [ ] (Challenge 4, if forking) README clearly links the upstream project and states exactly what you changed
- [ ] (Challenge 5 only) README states the embedding model used and roughly how large the corpus is

## MLH OrganizerHQ

- [ ] Project submitted via **Add Submission** on OrganizerHQ before the deadline
- [ ] Selected **Best Open-Source AI Project**
- [ ] Selected your specific iTech Club challenge track
- [ ] Demo link added (if you have one beyond the live demo)
