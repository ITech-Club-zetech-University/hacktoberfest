---
title: Judging
nav_order: 6
description: "How projects are scored: the leaderboard-vs-judges decision, the rubric, demo checklist, and winner marking."
---

# Judging
{: .no_toc }

1. TOC
{: toc }

---

## Leaderboard vs. judge sheet: the decision

When planning this event, we weighed two models for evaluating submissions: a **fully automated leaderboard** that ranks repositories by commit counts or automated test metrics, or a **judge sheet**—a published qualitative rubric scored by a human panel during live demos. Here is why we chose a human panel with an automated eligibility gate.

### Automated leaderboard

**Pros:** Feels fast, scales without recruiting judges, can run continuously during the hackathon.

**Cons, specific to this event:**
- MLH's official [winner-selection guidance](https://hacktoberfest-handbook.mlh.com/project-submissions-and-judging-for-hacktoberfest-hack-day) for the mandatory Best Open-Source AI Project challenge is explicitly qualitative: judges assess whether a project *solves a clear problem*, *demonstrates original technical work*, and *explains itself clearly*. None of these can be determined by an automated script.
- The official MLH handbook states explicitly: **"Hacktoberfest does not use pull-request counts as the basis for these prizes."** Automated metrics that measure volume (commits, lines of code, PR counts) reward gaming rather than genuine utility.
- Our 5 challenge tracks represent distinct technical disciplines (agent skill standards, offline edge quantization, multimodal perception, agentic dev harnesses, and retrieval-augmented generation). A single automated formula that evaluates all five fairly does not exist.
- "Does it actually work in a live demo" and "can the team explain what they built" settle credibility in two minutes, which no static analysis script can replicate.

### Our approach: judge sheet, with a lightweight automated gate

{: .important }
> **Primary mechanism: A published 100-point rubric, evaluated by a human judge panel during live demos.** In front of it, an **automated eligibility checker** runs against submitted GitHub repositories before demos to verify baseline hygiene (public repository, OSI license, `README.md`, Gemma mention). This automates basic structure checks without pretending software can evaluate human creativity or usefulness.

---

## The 100-point score sheet

Every project is evaluated out of 100 points against this universal base rubric:

| Criterion | Points | What judges are looking for |
|---|---|---|
| **Problem & impact** | 20 | Is the problem real and clearly stated? Does this solve a genuine campus, community, or developer need? |
| **Use of Gemma / open-weight AI** | 25 | Is Gemma an *important, functional part* of how the project works—not bolted on as an afterthought? Could the project function without Gemma? (Weighted highest because this is the core challenge requirement). |
| **Technical execution & working demo** | 25 | Does the application work live in front of judges? How much substantial technical logic was achieved during the event window? Are errors handled gracefully? |
| **Originality & creativity** | 15 | Does the project offer a thoughtful, creative approach to the problem? (A well-executed fresh take on an established idea scores high; novelty is valued but execution is prioritized). |
| **Open-source quality** | 15 | Is the repository public with a clear OSI-approved `LICENSE`? Is the `README.md` thorough, documenting model names, run instructions, architecture, and team member contributions? |
| **Total** | **100** | |

A ready-to-use template is in [`templates/judge-score-sheet.csv`](https://github.com/ITech-Club-zetech-University/hacktoberfest/blob/main/templates/judge-score-sheet.csv) for importing into Google Sheets or Excel.

### How challenge-specific notes supplement the rubric

Each of the 5 challenge pages contains **Challenge-Specific Evaluation Notes**. These do **not** add extra points or silently alter the 100-point maximum; instead, they give judges objective guidance when scoring the universal criteria:
- **Track 1 (Agent Skill):** Open-source quality directly checks conformance to the [Agent Skills standard](https://agentskills.io/specification) (`name` matching parent folder, descriptive frontmatter).
- **Track 2 (Offline Edge):** Technical execution requires verifying live that inference runs with **Wi-Fi and mobile data toggled off**.
- **Track 3 (Multimodal):** Use of Gemma requires verifying that visual or audio input is processed natively by Gemma, not converted via third-party OCR before touching text-only prompts.
- **Track 4 (Dev Harness):** Technical execution verifies that a genuine tool-calling loop executed with argument validation and explicit safety prompts for destructive actions.
- **Track 5 (RAG):** Technical execution verifies dynamic chunk retrieval and source citations, rejecting whole-corpus prompt stuffing.

---

## Standard demo checklist for judges

Judges will use this concise checklist across all 2-minute project demonstrations:

- [ ] **Live software demonstration:** Project is demonstrated running live in front of the panel (not a pre-rendered video or slide deck).
- [ ] **Active Gemma integration verified:** Team demonstrates or shows logs of Gemma processing inputs and generating responses.
- [ ] **Track acceptance test demonstrated:**
  - *Track 1:* Skill structure matches standard and executes in an agent or test harness.
  - *Track 2:* Live demo executes with Wi-Fi/network disabled on local compute.
  - *Track 3:* Live input of a non-text image or audio file generates grounded response.
  - *Track 4:* Model autonomously initiates a bounded tool call with safety confirmation.
  - *Track 5:* Dynamic retrieval returns citations; system admits when information is absent.
- [ ] **Code understanding:** Team members can clearly explain their architecture, prompts, and code when asked.
- [ ] **Graceful boundary handling:** Application handles an edge case, invalid input, or missing data cleanly.

---

## Automated eligibility check

Before demos begin, organizers run [`scripts/check_submission.py`](https://github.com/ITech-Club-zetech-University/hacktoberfest/blob/main/scripts/check_submission.py) against submitted repository URLs:

```bash
python3 scripts/check_submission.py https://github.com/team-one/project https://github.com/team-two/project
```

It checks basic repository readiness:
1. Repository is public.
2. A valid OSI-approved open-source `LICENSE` is present at the repo root.
3. A `README.md` exists and documents the project and Gemma usage.
4. For Track 1 entries: A valid `SKILL.md` is present.

This is an **eligibility gate, not a ranking tool**. A repository that fails a check is flagged so organizers can help the team fix administrative issues (such as a missing license file) before judges review the submission.

---

## The judging & winner marking process

1. **Judging panel:** 3–5 judges comprising faculty, mentors, sponsor representatives, and senior iTech Club leaders. Judges recuse themselves from scoring any project they directly mentored.
2. **Time-boxed demos:** Each team receives approximately 2 minutes to demo live, followed by 1 minute of judge Q&A.
3. **Independent scoring:** Judges enter scores on their individual score sheets. Scores are averaged across judges for each team.
4. **Track recognition & overall rankings:**
   - Teams are evaluated against the specific acceptance criteria of their declared **primary preset track**.
   - The top-scoring project in each primary track receives iTech Club local track honors.
   - The overall highest-scoring project across the entire event is recommended for the official MLH award.
   - Ties are broken by the **Use of Gemma** score first, followed by judge panel consensus.
5. **Marking winners in MLH OrganizerHQ:**  
   In compliance with [official MLH Hack Day requirements](https://hacktoberfest-handbook.mlh.com/project-submissions-and-judging-for-hacktoberfest-hack-day#mark-every-winner), organizers complete the following before announcing results:
   - Keep the **Announce Winners** toggle set to **PRIVATE** while evaluating submissions.
   - Open **Manage Submissions** in OrganizerHQ.
   - Filter by **Best Open-Source AI Project**, select the winning project, click **Mark Winner → Winner**, and verify the gold **WINNER** badge.
   - If an official partner challenge (e.g. Best Use of Gemma) was active and verified in OrganizerHQ, filter by that challenge and mark the corresponding winner.
   - Once all winners are marked and verified, switch **Announce Winners** to **PUBLIC** to publish the official event project gallery.
6. **Announcing:** Winners are announced live in the venue matching the published OrganizerHQ gallery.

{: .note }
> `[ORGANISER CONFIRMATION REQUIRED]`  
> **Pre-Event Organizer Action Items for Event 14735:**  
> Prior to the hacking window opening, the lead organizer must log in to OrganizerHQ and complete these checks:  
> 1. Open **OrganizerHQ → Challenges** and confirm whether **Best Open-Source AI Project** is the sole challenge, or whether an additional partner challenge (such as a Google Gemma partner prize) is enabled for event 14735.  
> 2. Confirm the exact track-recording mechanism (e.g. participant declaration in `README.md` and submission description) so judges have a unified list of teams per preset track before demos start.

---

## Organiser-maintained source-of-truth register

This table documents the primary source references governing the event rules, submission processes, and technical tracks.

| Source Document | Primary URL | Scope / Authority | Last Reviewed |
|---|---|---|---|
| **MLH Event Registration** | [events.mlh.com/events/14735](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club) | Official event listing, venue, date, audience restrictions | October 2026 |
| **MLH Hack Day Handbook** | [hacktoberfest-handbook.mlh.com/fest-planning-guide/](https://hacktoberfest-handbook.mlh.com/fest-planning-guide/) | Core Hack Day structure, team recommendations | October 2026 |
| **MLH Open Source Prize Categories** | [hacktoberfest-handbook.mlh.com/.../open-source-prize-categories](https://hacktoberfest-handbook.mlh.com/fest-planning-guide/open-source-prize-categories) | Official "Best Open-Source AI Project" requirements | October 2026 |
| **MLH Submissions & Judging** | [hacktoberfest-handbook.mlh.com/.../submissions-and-judging](https://hacktoberfest-handbook.mlh.com/project-submissions-and-judging-for-hacktoberfest-hack-day) | OrganizerHQ submission rules, private/public winner marking | October 2026 |
| **MLH Standard Rules & Conduct** | [mlh.io/code-of-conduct](https://static.mlh.io/docs/mlh-code-of-conduct.pdf) | Safety, harassment policy, baseline hackathon rules | October 2026 |
| **Agent Skills Open Standard** | [agentskills.io/specification](https://agentskills.io/specification) | Track 1 skill structure, frontmatter format, discovery | October 2026 |
| **Google Gemma Documentation** | [ai.google.dev/gemma](https://ai.google.dev/gemma) | Model specifications, terms of use, local runtime guides | October 2026 |
