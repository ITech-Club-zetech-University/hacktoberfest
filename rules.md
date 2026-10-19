---
title: Rules & Regulations
nav_order: 2
description: "Rules for the iTech Club x MLH Hacktoberfest Hack Day: official MLH policies, local award rules, teams, timeline, and submission."
---

# Rules & Regulations
{: .no_toc }

1. TOC
{: toc }

---

## Spirit of the event

This is a learning-first, overnight hack day. You are here to ship something real with open-weight AI, learn from mentors and each other, and leave with an open-source project you are proud of. Competing for prizes is part of the fun, but it is not the main point—helping a struggling team next to you is worth more than guarding your lead.

These rules extend the [MLH Standard Hackathon Rules](https://github.com/MLH/mlh-policies/blob/main/standard-hackathon-rules.md) and the [MLH Code of Conduct](https://static.mlh.io/docs/mlh-code-of-conduct.pdf), which every participant, mentor, judge, and organizer agrees to by attending. See [Code of Conduct]({{ site.baseurl }}/code-of-conduct/).

{: .note }
> **Three types of guidelines on this page:**
> 1. **Official MLH Requirements:** Mandatory rules governing participation, open-source licensing, and submission via [MLH OrganizerHQ](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club).
> 2. **iTech Club Local Award Rules:** Additional criteria (such as team size, primary track declaration, and rubric scoring) governing eligibility for the local Top Three Overall awards.
> 3. **Practical Recommendations:** Best-practice suggestions (such as pre-downloading model weights) to help your team succeed.

---

## Who can take part

- **Official MLH Requirement:** Open **exclusively to Zetech University students and iTech Club members**, per the [official MLH event listing](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club).
- **Official MLH Requirement:** You must **register on MLH** and **check in at the venue** the night of the event to be eligible for any prize.
- **Official MLH Requirement:** Organizers, volunteers, mentors, judges, and sponsor representatives may help teams but may not compete as hackers themselves.

---

## Team size & formation

### Official MLH Policy
Under [MLH Hack Day guidelines](https://hacktoberfest-handbook.mlh.com/fest-planning-guide/), individuals and teams (typically up to 4 hackers) are welcome to register, attend, and build. No student is excluded from attending or learning as a solo hacker or pair.

### iTech Club Local Track Rule
To compete for the **local iTech Club awards and Top Three Overall podium**, teams must consist of **3–4 members**.

**Why 3–4 members:** An overnight hackathon is intense. Building an open-weight AI application requires splitting substantial work across an ~8-hour build window:
- Model integration & prompt/tool engineering
- Application logic & user interface (CLI, web, or mobile)
- Testing, documentation, open-source licensing, and live demo preparation

Teams of 1–2 frequently run out of hours to complete all facets; teams of 5+ often leave members with too little hands-on code.

### Solo Hackers and Pairs
- Solo hackers and pairs are completely welcome at the event, can attend all workshops, and may submit their projects to the broad MLH competition on OrganizerHQ.
- To qualify for local iTech Club awards, solo hackers and pairs are strongly encouraged to team up during the **team formation session (7:00–7:30 PM)** right after check-in. Organizers will facilitate matching based on technical interests.
- A team may not split into multiple sub-teams to submit the same codebase.
- Every team member must actively participate and be prepared to explain their contribution during the live demo.

---

## What you can and cannot bring in

Following the [MLH Standard Hackathon Rules](https://github.com/MLH/mlh-policies/blob/main/standard-hackathon-rules.md):

- ✅ **Fresh Builds:** All project code must be written during the event window: **Friday 30 October 2026, 7:00 PM EAT → Saturday 31 October 2026, 6:00 AM EAT**.
- ✅ **Ideas & Tools:** You may arrive with an idea in mind, and you may use open-source libraries, public packages, boilerplate templates, and public model weights.
- ✅ **Re-implementations:** You may build a fresh take on an established concept; execution, utility, and learning are judged rather than pure novelty.
- ❌ **No Pre-built Projects:** You **cannot** bring in a codebase you (or your team) built before the event, including personal repos open-sourced right before the hackathon specifically for reuse.
- ❌ **No Plagiarism:** You cannot claim another author's work or upstream code as your own original hackathon build.

---

## AI coding tools vs. Open-weight models

### Proportionate Disclosure of AI Coding Tools
You are welcome to use AI pair-programming assistants (such as Gemini CLI, GitHub Copilot, Claude Code, or Cursor) to help write, debug, and scaffold code during the night:
- **Proportionate disclosure:** Include a short list in your `README.md` under an **AI Tools Used** heading (e.g. `GitHub Copilot, Gemini CLI`) along with a brief 1–2 sentence explanation of your team's own architectural contribution.
- **Code understanding:** Every team member must understand and be able to explain the submitted code to judges. If a team cannot explain code generated by an AI assistant during the demo, points will be deducted under Technical Execution.

### Open-Source Software vs. Open-Weight AI
It is essential to distinguish your application's software license from the AI model's terms:
- **Your Application Code (OSI License Required):** Your team's source code must be published under an [OSI-approved open-source license](https://opensource.org/licenses) (such as MIT or Apache-2.0).
- **The Model Weights (Open-Weight Terms):** Open-weight models (like Google's Gemma) are released with open weights under model-specific terms (such as the [Gemma Terms of Use](https://ai.google.dev/gemma/terms)). These are responsible open-weight terms rather than traditional OSI-approved software licenses. Your `README.md` must state the model name and cite its terms of use.
- **AI Tool Usage Alone Does Not Qualify:** Using Copilot to write code for a standard web app does not satisfy the open-source AI requirement. Gemma (or a compatible open-weight model) must be a functional component of what the product *does*.

---

## The hacking timeline

| Time (EAT) | Stage | Details |
|---|---|---|
| 7:00 – 7:30 PM | Check-in & Team Formation | Venue doors open, registration confirmation, matching solo hackers into 3–4 person teams |
| 7:30 – 8:00 PM | Opening & Challenge Briefing | Welcome remarks, track briefing, rules, and rubric review |
| 8:00 – 8:30 PM | Gemma Setup Workshop | Hands-on setup clinic (API keys, Ollama, local scaffolding) |
| 8:30 PM – 4:30 AM | **Building Window** (~8 hours) | Active development; technical mentors circulate across tables |
| 4:30 – 5:00 AM | Submission & Preliminary Review | Final commits, pushes to GitHub, submission via MLH OrganizerHQ, automated hygiene gate |
| 5:00 – 5:45 AM | Live Project Demos | Time-boxed 2-minute demos + 1-minute Q&A in front of the judge panel |
| 5:45 – 6:00 AM | Judging Wrap-Up & Closing | Winner marking on OrganizerHQ, announcement of Top 3 Overall, and wrap-up |

Organizers will announce any minor timing adjustments directly to the room.

---

## Submitting your project

To be considered for awards, every team must complete **both** submission steps before the **5:00 AM EAT** deadline:

### Step 1: Open-source your GitHub repository
1. Ensure your repository is **public** on GitHub.
2. Include an OSI-approved `LICENSE` file at the root of the repository (e.g. MIT, Apache-2.0, or GPL-3.0).
3. Provide a thorough `README.md` containing:
   - What the project does and who it serves (2–3 sentences).
   - Your team's **single declared primary iTech Club track** (Track 1, 2, 3, 4, or 5).
   - The exact Gemma model/variant used, its runtime environment, and a reference to its license/terms.
   - Step-by-step cold-start instructions for running the project.
   - Team members and roles.
   - Proportionate disclosure of any AI coding assistants used.
4. Run the automated eligibility checker (`python3 scripts/check_submission.py <repo-url>`) to catch administrative oversights.
   - If flagged as `NEEDS MANUAL REVIEW` (e.g. non-standard license filename), use the 4:30–5:00 AM window to resolve it before demos start.
   - Note: Automated rate-limit or network errors do not penalize your team.

### Step 2: Submit through MLH OrganizerHQ
[MLH OrganizerHQ](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club) is the official platform for Hacktoberfest Hack Day submissions:
1. Log in to OrganizerHQ with the account used for event registration.
2. Go to **Challenges** on the event page and select **Add Submission**.
3. Fill in your project name, repository URL, tech stack, and short description.
4. **Challenge selection in OrganizerHQ:**
   - Select **Best Open-Source AI Project** (the official MLH Hack Day challenge).
   - *Note on Partner Prizes:* If a specific partner challenge (such as a Google Gemma partner prize) is verified and announced by event staff as active in OrganizerHQ, select it as instructed.
5. In your project description and repository `README.md`, explicitly declare your **one primary iTech Club challenge track**.

{: .important }
> **Why one primary track for local judging?**  
> Teams must declare exactly **one primary preset track** for local evaluation. This prevents duplicate submissions from inflating opportunities and ensures fair, peer-level comparison. Teams may incorporate ideas from other tracks (e.g. adding offline fallback to a RAG project), but judges evaluate the submission against the rubric notes and acceptance tests of the declared primary track.

---

## How winners are chosen & award structure

1. **Local iTech Club Recognition (Top Three Overall):**
   - Evaluated by a human judge panel using the published [100-Point Rubric]({{ site.baseurl }}/judging/#the-100-point-score-sheet) during live, 2-minute demos.
   - All eligible local submissions across all 5 preset tracks are ranked together on a single leaderboard using the common rubric.
   - The top three highest-scoring teams are awarded **1st Place, 2nd Place, and 3rd Place Overall**.
   - Preset track acceptance tests inform the rubric (specifically Technical Execution and Use of Gemma); they are **not** separate hidden bonus points.
2. **Official MLH Challenge (Best Open-Source AI Project):**
   - The official [Best Open-Source AI Project](https://hacktoberfest-handbook.mlh.com/fest-planning-guide/open-source-prize-categories) challenge has **one winning team**.
   - The winner is selected by the organizing panel according to [MLH Hack Day guidelines](https://hacktoberfest-handbook.mlh.com/project-submissions-and-judging-for-hacktoberfest-hack-day) and marked directly in OrganizerHQ.
   - While the locally highest-scoring project is a very strong candidate, the MLH winner must be evaluated and marked in OrganizerHQ following official MLH requirements. The local #1 is not automatically guaranteed to be the MLH winner if MLH-specific eligibility requirements differ or if separate criteria apply.
3. **Deterministic Tie-Breakers:**
   - Ties in overall scores are broken deterministically in this order:
     1. Use of Gemma / open-weight AI (out of 25)
     2. Technical execution & working demo (out of 25)
     3. Problem & impact (out of 20)
     4. Open-source quality (out of 15)
     5. Judge panel consensus conference
4. **No Pull-Request Counting:**
   - Per official MLH rules: **Hacktoberfest Hack Day does not use pull-request counts for judging or prizes.** Scoring is based entirely on project merit, technical execution, working demonstration, and open-source quality.
5. **Confidentiality:**
   - Individual judge sheets, raw marks, and provisional rankings are internal and confidential. Only final validated winners and high-level constructive comments are published.

---

## Governance, disqualification & ownership

- **Conflicts of Interest:** Judges recuse themselves from scoring any team they helped build, closely mentored, or have a direct interest in. Scores are computed from the remaining non-conflicted judges (minimum 2 valid scores per team).
- **Disqualification:** Organizers reserve the right to disqualify any entry for Code of Conduct violations, plagiarism, pre-building code before the event, or misrepresenting model functionality.
- **Appeals & Final Authority:** Teams flagged by the automated hygiene check have until 5:00 AM to resolve administrative issues. The Lead Event Organizer (Faculty/iTech Club advisor), in consultation with the MLH representative, holds final authority for resolving any rule interpretation, edge case, or dispute.
- **Ownership:** Teams retain full intellectual property ownership of their code. Open-sourcing under an OSI license allows the community to learn from your work without transferring ownership to iTech Club, MLH, or sponsors.
