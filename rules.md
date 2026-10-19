---
title: Rules & Regulations
nav_order: 2
description: "General rules for the iTech Club x MLH Hacktoberfest Hack Day: eligibility, teams, timeline, submission, and conduct."
---

# Rules & Regulations
{: .no_toc }

1. TOC
{: toc }

---

## Spirit of the event

This is a learning-first, overnight hack day. You're here to ship something real with Gemma, learn from mentors and each other, and leave with an open-source project you're proud of. Competing for prizes is part of the fun, but it's not the point — helping a struggling team next to you is worth more than guarding your lead.

These rules extend the [MLH Standard Hackathon Rules](https://github.com/MLH/mlh-policies/blob/main/standard-hackathon-rules.md) and the [MLH Code of Conduct](https://static.mlh.io/docs/mlh-code-of-conduct.pdf), which every participant, mentor, judge, and organizer agrees to by attending. See [Code of Conduct]({{ site.baseurl }}/code-of-conduct/).

## Who can take part

- Open **exclusively to Zetech University students and iTech Club members**, per the [official MLH event listing](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club).
- You must **register on MLH OrganizerHQ** and **check in at the venue** the night of the event to be eligible for any prize.
- Organizers, volunteers, mentors, judges, and sponsor representatives may help teams but may not compete as hackers themselves — this follows the standard MLH rule.

## Team size

{: .important }
> **Teams competing in the 5 preset Challenges must have 3–4 members.**

Why 3–4: it's small enough to stay nimble over one overnight session, but large enough to realistically split the work a Gemma project needs — someone on the model/prompting side, someone on the app/UI, and someone on integration, testing, and the README/demo. Teams of 1–2 tend to run out of hours; teams of 5+ tend to have idle members on a single-night build.

- **Solo hackers and pairs are welcome at the event** — MLH's general listing welcomes solo hacking — but to enter one of the 5 Challenges below (and therefore the iTech Club prizes and leaderboard/judging), you need to find teammates and form a 3–4 person team.
- Team formation happens in the **first 30 minutes** after doors open (7:00–7:30 PM). Organizers will run a quick round of "what do you want to build / what can you do" to help solo hackers pair up.
- A team may **not** split into two teams to double-submit the same idea.
- Every team member must actively participate — this is checked informally by mentors during the night and explicitly during demos (every member should be able to speak to some part of the project).

## What you can and can't bring in

Following the [MLH Standard Hackathon Rules](https://github.com/MLH/mlh-policies/blob/main/standard-hackathon-rules.md):

- ✅ You can pitch up with an **idea** you already had.
- ✅ You can use open-source libraries, frameworks, boilerplate, and Gemma itself.
- ✅ You can work on an idea that's "already been done" — originality isn't required, execution is judged.
- ❌ You **cannot** bring in a codebase you (or your team) already built, including code you open-sourced just before the event specifically to reuse it here.
- ❌ You cannot re-use code or project material from a past project you personally worked on.
- **All project work must happen during the event window**: Friday 30 Oct, 7:00 PM EAT → Saturday 31 Oct, 6:00 AM EAT.

### Using AI coding tools

You're encouraged to use AI pair-programming tools (Claude Code, Gemini CLI, GitHub Copilot, Cursor, etc.) — in fact, several of the challenge tracks are *about* building with AI agents. Two rules:

1. **Be transparent.** List the AI tools you used in your README and be ready to explain, in your own words, what your team built versus what a tool scaffolded.
2. **The open-weight AI requirement is separate from "I used an AI coding assistant."** Using Copilot to write code doesn't satisfy the Best Open-Source AI Project requirement — Gemma (or another open-weight model) has to be an *important part of what the project does*, not just how you wrote it. See [Judging]({{ site.baseurl }}/judging/).

## The hacking timeline

| Time (EAT) | What's happening |
|---|---|
| 7:00 – 7:30 PM | Check-in, registration confirmation, welcome |
| 7:30 – 8:00 PM | Opening talk, challenge briefing, team formation |
| 8:00 – 8:30 PM | Gemma setup workshop (bring a laptop with the [starter kit]({{ site.baseurl }}/starter-kit/) prerequisites installed) |
| 8:30 PM – 4:30 AM | **Hacking** (8 hours) — mentors circulate throughout |
| 4:30 – 5:00 AM | Submissions close — final commit, push, and MLH OrganizerHQ submission |
| 5:00 – 5:45 AM | Demos (all teams, time-boxed) |
| 5:45 – 6:00 AM | Judging wrap-up and winners announced |

Organizers reserve the right to adjust this timeline on the night and will announce any change to every team at once.

## Submitting your project

Every team that wants to be considered for a prize — iTech Club challenge prizes **or** the MLH Best Open-Source AI Project prize — must do **both** of the following before the submission deadline:

### 1. Open-source your repository

- Your project's source code must be in a **public GitHub repository**.
- The repository must carry a **clear open-source license** — [MIT](https://opensource.org/license/mit), [Apache-2.0](https://opensource.org/license/apache-2.0), [GPL-3.0](https://opensource.org/license/gpl-3.0), or another license from the [OSI list](https://opensource.org/licenses). Put the license as a `LICENSE` file at the repo root.
- Your `README.md` must clearly state: what the project does, which Gemma model/variant you used and how, which challenge track you're entering, how to run it, and which team members built it.
- Run the [submission eligibility checker]({{ site.baseurl }}/judging/#automated-eligibility-check) against your own repo before the deadline — it catches the easy misses (missing license, missing README, etc.) before a judge ever sees it.

### 2. Submit through MLH OrganizerHQ

{: .note }
> OrganizerHQ is MLH's mandatory submission platform for Hacktoberfest Hack Day — it isn't optional and can't be replaced by a separate form, even though we also run our own challenge tracks and judge sheet on this site.

1. Sign in to OrganizerHQ with the account you registered with.
2. Open **Challenges** from the event page.
3. Select **Add Submission** and fill in your project link, name, description, technologies used, and a demo link if you have one.
4. Under **"Which challenge(s) are you submitting to?"**, select:
   - **Best Open-Source AI Project** (the mandatory MLH challenge — every team should select this), **and**
   - The specific **iTech Club challenge track** you built for (e.g. "Challenge 2: Gemma Off the Grid").
5. Submit before the deadline. One team member submits on behalf of the whole team.

You can enter **more than one** challenge with the same project if it genuinely fits — just select every challenge it's eligible for.

## How winners are chosen

Full detail, including the judge sheet, is on the [Judging]({{ site.baseurl }}/judging/) page. In short:

- The 5 iTech Club challenge tracks are judged by a **human judge panel using a published rubric**, informed by a lightweight automated check that confirms each repo meets the baseline eligibility rules above.
- The MLH **Best Open-Source AI Project** winner is selected and marked through MLH OrganizerHQ, following [MLH's official winner-selection guidance](https://hacktoberfest-handbook.mlh.com/project-submissions-and-judging-for-hacktoberfest-hack-day), by the organizing team.
- **Hacktoberfest does not use pull-request counts as the basis for any prize here** — this is a build night, not a PR-counting challenge.

## Disqualification

Organizers may disqualify a team at their discretion for breaking these rules, the MLH Code of Conduct, or for other unsporting behavior (e.g. plagiarizing another team's work, misrepresenting what was built during the event, or submitting a pre-built project).

## Ownership

Teams retain full ownership of what they build. Open-sourcing your repo under a permissive license means others can use and build on it — it does not transfer ownership to iTech Club, MLH, or Google.
