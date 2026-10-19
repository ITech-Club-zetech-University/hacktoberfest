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
> 2. **iTech Club Local Award Rules:** Additional criteria (such as team size and primary track declaration) governing eligibility for local iTech Club track prizes and recognition.
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
To compete for the **5 preset iTech Club challenge track awards**, teams must consist of **3–4 members**.

**Why 3–4 members:** An overnight hackathon is intense. Building an open-weight AI application requires splitting substantial work across an ~8-hour build window:
- Model integration & prompt engineering
- Application logic & user interface (CLI, web, or mobile)
- Testing, documentation, open-source licensing, and demo preparation

Teams of 1–2 frequently run out of hours to complete all facets; teams of 5+ often leave members with too little hands-on code.

### Solo Hackers and Pairs
- Solo hackers and pairs are completely welcome at the event, can attend all workshops, and may submit their projects to the broad MLH competition on OrganizerHQ.
- To enter one of the 5 preset iTech Club tracks and qualify for local track awards, solo hackers and pairs are strongly encouraged to team up during the **team formation session (7:00–7:30 PM)** right after check-in. Organizers will facilitate matching based on technical interests.
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

### Using AI Coding Assistants
You are welcome to use AI pair-programming assistants (such as Gemini CLI, GitHub Copilot, Claude Code, or Cursor) to help write, debug, and scaffold code during the night:
- **Be transparent:** List any AI coding assistants used in your `README.md`.
- **Code understanding:** Every team member must understand and be able to explain the submitted code to judges.

### Open-Source Software vs. Open-Weight AI
It is essential to distinguish your application's software license from the AI model's terms:
- **Your Application Code (OSI License Required):** Your team's source code must be published under an [OSI-approved open-source license](https://opensource.org/licenses) (such as MIT or Apache-2.0).
- **The Model Weights (Open-Weight Terms):** Open-weight models (like Google's Gemma) are released with open weights under model-specific licenses (such as the [Gemma Terms of Use](https://ai.google.dev/gemma/terms)). These are responsible open-weight terms rather than traditional OSI-approved software licenses. Your `README.md` must state the model name and acknowledge its terms of use.
- **AI Tool Usage Alone Does Not Qualify:** Using Copilot to write code for a standard web app does not satisfy the open-source AI requirement. Gemma (or a compatible open-weight model) must be a functional component of what the product *does*.

---

## The hacking timeline

| Time (EAT) | Stage | Details |
|---|---|---|
| 7:00 – 7:30 PM | Check-in & Team Formation | Venue doors open, registration confirmation, matching solo hackers into 3–4 person teams |
| 7:30 – 8:00 PM | Opening & Challenge Briefing | Welcome remarks, track briefing, rules, and rubric review |
| 8:00 – 8:30 PM | Gemma Setup Workshop | Hands-on setup clinic (API keys, Ollama, local scaffolding) |
| 8:30 PM – 4:30 AM | **Building Window** (~8 hours) | Active development; technical mentors circulate across tables |
| 4:30 – 5:00 AM | Submission Window | Final commits, pushes to GitHub, and submission via MLH OrganizerHQ |
| 5:00 – 5:45 AM | Live Project Demos | Time-boxed 2-minute demos + 1-minute Q&A in front of the judge panel |
| 5:45 – 6:00 AM | Judging Wrap-Up & Closing | Winner marking on OrganizerHQ, announcement, and wrap-up |

Organizers will announce any minor timing adjustments directly to the room.

---

## Submitting your project

To be considered for awards, every team must complete **both** submission steps before the 5:00 AM EAT deadline:

### Step 1: Open-source your GitHub repository
1. Ensure your repository is **public** on GitHub.
2. Include an OSI-approved `LICENSE` file at the root of the repository (e.g. MIT, Apache-2.0, or GPL-3.0).
3. Provide a thorough `README.md` containing:
   - What the project does and who it serves (2–3 sentences).
   - Your team's **single declared primary iTech Club track** (Track 1, 2, 3, 4, or 5).
   - The exact Gemma model/variant used, its runtime environment, and a reference to its license/terms.
   - Step-by-step cold-start instructions for running the project.
   - Team members and roles.
   - Disclosure of any AI coding assistants used.
4. Run the automated eligibility checker (`python3 scripts/check_submission.py <repo-url>`) to catch administrative oversights.

### Step 2: Submit through MLH OrganizerHQ
[MLH OrganizerHQ](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club) is the official platform for Hacktoberfest Hack Day submissions:
1. Log in to OrganizerHQ with the account used for event registration.
2. Go to **Challenges** on the event page and select **Add Submission**.
3. Fill in your project name, repository URL, tech stack, and short description.
4. **Challenge selection in OrganizerHQ:**
   - Select **Best Open-Source AI Project** (the official MLH Hack Day challenge).
   - *Note on Partner Prizes:* If a specific partner challenge (such as a Google Gemma partner prize) is active on the OrganizerHQ dashboard for this event, select it as directed by event staff.
5. In your project description and repository `README.md`, explicitly declare your **one primary iTech Club challenge track**.

{: .important }
> **Why one primary track for local judging?**  
> Teams must declare exactly **one primary preset track** for local evaluation. This ensures fair, apples-to-apples comparison among projects tackling the same technical problem. Teams are free to incorporate ideas from other tracks (e.g. adding offline fallback to a RAG project), but judges will evaluate the submission against the rubric notes and acceptance tests of the declared primary track.

---

## How winners are chosen

1. **Official MLH Challenge:**
   - The official [Best Open-Source AI Project](https://hacktoberfest-handbook.mlh.com/fest-planning-guide/open-source-prize-categories) challenge has **one winning team**.
   - The winner is selected by the organizing panel according to [MLH Hack Day guidelines](https://hacktoberfest-handbook.mlh.com/project-submissions-and-judging-for-hacktoberfest-hack-day) and marked directly in OrganizerHQ.
2. **iTech Club Local Track Awards:**
   - Evaluated by a human judge panel using the published [100-Point Rubric]({{ site.baseurl }}/judging/#the-100-point-score-sheet) during live, 2-minute demos.
   - Top-scoring projects within each primary track receive local track honors.
3. **No Pull-Request Counting:**
   - Per official MLH rules: **Hacktoberfest Hack Day does not use pull-request counts for judging or prizes.** Scoring is based entirely on project merit, technical execution, working demonstration, and open-source quality.

---

## Disqualification & Ownership

- **Disqualification:** Organizers reserve the right to disqualify any entry for Code of Conduct violations, plagiarism, pre-building code before the event, or misrepresenting model functionality.
- **Ownership:** Teams retain full intellectual property ownership of their code. Open-sourcing under a permissive license allows the community to learn from your work without transferring ownership to iTech Club, MLH, or sponsors.
