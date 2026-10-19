---
title: Judging
nav_order: 6
description: "How projects are scored: the leaderboard-vs-judges decision, the rubric, and the process."
---

# Judging
{: .no_toc }

1. TOC
{: toc }

---

## Leaderboard vs. judge sheet: the decision

When planning this event, we weighed two models for finding the top 3 projects: a **fully automated leaderboard** that scores and ranks submissions by some measurable signal, or a **judge sheet** — a published rubric scored by a human panel. Here's the trade-off as we see it, and what we landed on.

### Automated leaderboard

**Pros:** feels objective and fast, scales without recruiting judges, can run live during the night for a bit of gamified energy.

**Cons, specific to this event:**
- MLH's own [winner-selection guidance](https://hacktoberfest-handbook.mlh.com/project-submissions-and-judging-for-hacktoberfest-hack-day) for the mandatory Best Open-Source AI Project challenge is explicitly qualitative — judges are asked to assess whether a project *solves a clear problem*, *shows originality and thoughtful technical work*, and *explains itself clearly*. None of that is something you can compute from a repo.
- The handbook says outright: **"Hacktoberfest does not use pull-request counts as the basis for these prizes."** The one thing that *is* easy to automate (commit/PR counts, lines of code, test coverage) is explicitly not what MLH wants weighted.
- Winners still have to be marked by a human in MLH OrganizerHQ regardless — so a fully automated leaderboard wouldn't actually replace a judging step, just add one in parallel.
- Our 5 challenge tracks are deliberately varied (an Agent Skill, an offline app, a multimodal tool, a dev harness, a RAG assistant) — a single automated metric that's fair across all five is a hard research problem on its own, let alone something to build correctly with 11 days of lead time.
- "Does it work" and "is the demo convincing" are exactly the things a live demo settles in 30 seconds and a script struggles to verify at all.

### Judge sheet (human panel + published rubric)

**Pros:** matches how MLH itself evaluates the mandatory challenge, lets judges watch a live demo (which is the actual point of a hack day), handles the 5 different challenge types fairly since humans can weigh "did this team pull off something hard in their specific track" rather than forcing every track through one formula, realistic to set up well with the time we have.

**Cons:** needs 3–5 people willing to judge, carries some subjectivity (mitigated below), slower than reading a leaderboard off a screen.

### Our approach: judge sheet, with a lightweight automated gate in front of it

{: .important }
> **Primary mechanism: a published rubric, scored by a human judge panel.** In front of it, an **automated eligibility checker** (not a performance leaderboard) runs against every submitted repo to confirm the baseline requirements — public, licensed, documented, uses Gemma — before judges spend time on it. This gets you real automation where it's actually reliable (checking a repo's structure) without pretending a script can judge creativity or usefulness.

This also keeps us aligned with MLH's required process: OrganizerHQ is the mandatory submission and winner-marking platform for the Best Open-Source AI Project challenge, and it's explicitly a human-reviewed step, not an automated one.

## The score sheet

Every project is scored out of 100 against this base rubric. Each challenge page also lists 1–2 **challenge-specific checks** judges weigh alongside these.

| Criterion | Points | What judges are looking for |
|---|---|---|
| **Problem & impact** | 20 | Is the problem real and clearly stated? Would someone actually use this? |
| **Use of Gemma / open-weight AI** | 25 | Is Gemma an *important part* of how the project works — not bolted on? Weighted highest because this is the actual prize requirement. |
| **Technical execution & working demo** | 25 | Does it work, live, in front of judges? How much was actually built in one night? |
| **Originality & creativity** | 15 | A thoughtful take on a known idea counts — it doesn't need to be unprecedented. |
| **Open-source quality** | 15 | License, README clarity, is the model/approach easy to verify from the repo? |
| **Total** | **100** | |

A ready-to-use version of this table is in [`templates/judge-score-sheet.csv`](https://github.com/ITech-Club-zetech-University/hacktoberfest/blob/main/templates/judge-score-sheet.csv) — import it into Google Sheets or Excel for the night.

## Automated eligibility check

Before demos, organizers run [`scripts/check_submission.py`](https://github.com/ITech-Club-zetech-University/hacktoberfest/blob/main/scripts/check_submission.py) against every submitted repo URL. It checks, per repo:

- Repository is public
- A `LICENSE` file is present and matches a recognizable OSI license (MIT, Apache-2.0, GPL-3.0, etc.)
- A `README.md` exists and mentions Gemma (a weak signal judges then confirm properly)
- For Challenge 1 submissions specifically: a `SKILL.md` file exists in the repo

```bash
python3 scripts/check_submission.py https://github.com/team/repo-one https://github.com/team/repo-two
```

This **is not a scoring or ranking tool** — it only flags repos that are missing something basic, so judges spend their limited time on substance instead of paperwork. A repo that fails a check isn't automatically disqualified; an organizer follows up with the team before judging starts.

## The judging process

1. **Panel:** 3–5 judges — a mix of mentors, sponsor reps, and senior iTech Club members. No judge scores their own team.
2. **Demos:** each team gets a short, fixed window (see the [timeline]({{ site.baseurl }}/rules/#the-hacking-timeline)) — live demo, no slide decks required.
3. **Scoring:** each judge scores every team independently on the sheet above, then scores are averaged per team per criterion.
4. **Per challenge:** teams are ranked within their own challenge track first — you're competing against other entries in your track, not across all 5 tracks at once.
5. **Top 3 overall:** after each track has a winner, the organizing team selects the **top 3 projects across the whole event** by taking the highest average total scores, for the overall iTech Club prizes.
6. **Ties:** broken by the "use of Gemma" score first (the highest-weighted, most on-theme criterion), then by judge discussion.
7. **MLH's Best Open-Source AI Project:** selected separately by organizers using [MLH's own guidance](https://hacktoberfest-handbook.mlh.com/project-submissions-and-judging-for-hacktoberfest-hack-day) and marked as **Winner** in OrganizerHQ — see [Rules → How winners are chosen]({{ site.baseurl }}/rules/#how-winners-are-chosen). It doesn't have to be the same project as the overall #1 on the iTech Club side, though it often will be.
8. **Announcing:** results are kept private in OrganizerHQ until every winner is confirmed, then announced together in the room.
