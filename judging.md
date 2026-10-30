---
title: Judging
nav_order: 6
description: "Human-led hackathon judging system: standardised 100-point rubric, 0–5 rating scale, 9-step workflow, score consolidation, and winner selection."
---

# Judging
{: .no_toc }

1. TOC
{: toc }

---

## Human-led hackathon judging system

Hacktoberfest Hack Day Nairobi × iTech Club operates on a **strictly human-led judging model**.

{: .important }
> **Competition Management Decision:**  
> We will **NOT** use an automated leaderboard, automated project evaluation, or an AI-based ranking system.  
> There is:
> - **No automated project evaluation** of code quality, architecture, or model accuracy.
> - **No AI-based project scoring** or automated ranking algorithms.
> - **No automated leaderboard** displayed or operating during the hackathon.
> - **No script that assigns project scores** or generates competitive standings.
> - **No automated winner-selection algorithm**.
>
> All projects are evaluated by appointed human judges using a published common rubric and standardised judge score sheets. Event organisers consolidate the completed score sheets and determine the final rankings.

### Why human judging is essential

1. **Working substance over gaming:** Per official Major League Hacking (MLH) rules, **Hacktoberfest does not use pull-request counts, commit volume, or lines of code as the basis for judging or prizes.** Automated metrics reward artificial activity rather than practical utility.
2. **Multi-disciplinary tracks:** The 5 preset challenge tracks span agent skill standards, offline edge quantization, multimodal perception, developer harnesses, and retrieval-augmented generation. A single automated formula that evaluates all five fairly cannot exist.
3. **Live demonstration verification:** A two-minute live demonstration and code walk-through answers crucial questions no script can evaluate: Does the software actually run? Does Gemma actively power the reasoning? Can the team explain what they built and where its limitations lie?

---

## The judging panel

Judging is conducted by an appointed panel of approximately **3–5 judges**, composed of university faculty, industry mentors, and experienced alumni.

### Capacity and assignment goal

- Wherever event judging capacity allows, each competing team should receive **at least three independent evaluations** from distinct panel members.
- The organisers establish judge assignments prior to the demonstration period to distribute the evaluation load equitably across all participating teams.

### Core judge responsibilities & ethical standards

- **Evaluate against the published rubric:** Judges assess every project strictly against the published 100-point rubric and scoring anchors.
- **Independent scoring:** Judges score independently on their own score sheets during and immediately following the demonstration, without discussing marks or attempting to influence fellow judges before score sheets are submitted.
- **Evidence-based evaluation:** Judges must record brief qualitative comments, observed strengths, areas requiring improvement, and concrete supporting evidence for their ratings.
- **Implementation over presentation:** Judges evaluate the actual running software, codebase, and technical execution rather than slide decks or rehearsed marketing pitches.
- **Mandatory conflict recusal:** Any judge who directly mentored a team, contributed code, or has an academic/personal conflict of interest must declare the conflict and recuse themselves. The team's score is computed from the remaining non-conflicted judges (minimum 2 valid evaluations required).
- **Avoid favouritism:** All teams are granted equal presentation time and evaluated with impartial professional standards regardless of track choice or background.
- **Strict confidentiality:** Individual score sheets, raw numerical marks, internal notes, and provisional tallies are **strictly confidential internal records**. They are never published on the website or disclosed to participants. Only final validated winners and high-level constructive feedback are announced.

---

## Standardised 100-point judging rubric
{: #the-100-point-score-sheet #the-100-point-operational-rubric }

Every project is evaluated out of **100 total weighted points** across six core criteria:

| Evaluation criterion | Weight | Core question for judges |
|---|:---:|---|
| **Problem relevance and practical impact** | **15** | Does the project address a real, clearly articulated campus, community, or developer need with demonstrable practical impact? |
| **Meaningful Gemma/open-weight AI integration** | **20** | Is Gemma an essential, functioning component of the architecture rather than a superficial prompt wrapper or disconnected afterthought? |
| **Technical execution and working demonstration** | **25** | Does the software run live in front of judges? Is substantial, working technical engineering demonstrated within the hackathon window? |
| **Originality and creativity** | **15** | Does the project demonstrate fresh thinking, novel problem-solving, or clever adaptation compared to standard boilerplate tutorials? |
| **Responsible AI, privacy and safety** | **10** | Are privacy, data protection, safety guardrails, bounded actions, honest limitations, and model term compliance thoughtfully implemented? |
| **Open-source quality and reproducibility** | **15** | Is the repository public with a valid OSI license, reproducible cold-start documentation, model attribution, and transparent AI tool disclosures? |
| **TOTAL** | **100** | |

There are **no hidden points, surprise bonuses, or unannounced criteria**.

---

## The 0–5 rating scale and weighted score conversion

Judges evaluate each criterion using a consistent, standardized integer rating scale from **0 to 5**:

| Rating | Tier | General Meaning |
|:---:|---|---|
| **0** | **Not demonstrated** | Completely missing, unaddressed, non-functional, or absent from the project and demonstration. |
| **1** | **Very poor** | Minimal effort; severely broken or superficial; negligible understanding of the domain or requirement. |
| **2** | **Below expectations** | Incomplete implementation; major bugs or unhandled edge cases; weak connection to the problem or model. |
| **3** | **Meets expectations** | Solid, working baseline; achieves the core requirement cleanly; standard solution with minor rough edges. |
| **4** | **Very good** | High-quality implementation; robust execution; clear understanding of tradeoffs, edge cases, and architecture. |
| **5** | **Excellent** | Standout achievement; flawless live execution; deep technical insight, exceptional polish, and user empathy. |

### Score conversion formula

Judges convert their rating (0–5) into weighted points using this formula:

$$\text{Weighted Score} = \left(\frac{\text{Judge Rating}}{5}\right) \times \text{Criterion Weight}$$

### Weighted point conversion table

| Criterion | Weight | Rating 0 | Rating 1 | Rating 2 | Rating 3 | Rating 4 | Rating 5 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Problem relevance and practical impact | **15** | 0.0 | 3.0 | 6.0 | 9.0 | 12.0 | 15.0 |
| Meaningful Gemma integration | **20** | 0.0 | 4.0 | 8.0 | 12.0 | 16.0 | 20.0 |
| Technical execution and working demo | **25** | 0.0 | 5.0 | 10.0 | 15.0 | 20.0 | 25.0 |
| Originality and creativity | **15** | 0.0 | 3.0 | 6.0 | 9.0 | 12.0 | 15.0 |
| Responsible AI, privacy and safety | **10** | 0.0 | 2.0 | 4.0 | 6.0 | 8.0 | 10.0 |
| Open-source quality and reproducibility | **15** | 0.0 | 3.0 | 6.0 | 9.0 | 12.0 | 15.0 |
| **Total Possible** | **100** | **0.0** | **20.0** | **40.0** | **60.0** | **80.0** | **100.0** |

- **Judge Total Score:** The sum of all six weighted criterion scores produces that judge's total score out of 100 for the project.
- **Team Final Score:** The arithmetic average of all completed independent judge totals for that team.

---

## Detailed scoring anchors

To maintain fairness and objective scoring across all panel members, judges apply these explicit criteria anchors:

### 1. Problem relevance and practical impact (Weight: 15 points)
- **Rating 0 (0 pts):** No identifiable problem; target audience unstated; solution has no apparent user or relevance.
- **Rating 1 (3 pts):** Vague, generic concept with minimal connection to campus life, developer workflows, or real-world needs.
- **Rating 2 (6 pts):** Relevant problem identified, but scope is poorly defined, assumptions are unverified, or value proposition is weak.
- **Rating 3 (9 pts):** Clear, well-scoped problem solving a real bottleneck for Zetech students, local developers, or the broader community.
- **Rating 4 (12 pts):** High-impact problem supported by strong user empathy, clear workflow understanding, and demonstrable practical benefit.
- **Rating 5 (15 pts):** Exceptional relevance; addresses an urgent, compelling need with immediate usability, high community value, and clear scalability.

### 2. Meaningful Gemma/open-weight AI integration (Weight: 20 points)
- **Rating 0 (0 pts):** Gemma is not integrated, non-functional, or replaced by an unrelated proprietary API; non-working mock.
- **Rating 1 (4 pts):** Superficial wrapper or trivial prompt; Gemma could be deleted without altering the product's core utility.
- **Rating 2 (8 pts):** Gemma is invoked, but prompts are unoptimized, model parameters are unexamined, or reasoning is shallow.
- **Rating 3 (12 pts):** Substantive, functional integration; Gemma powers the essential analytical, generative, or perceptual pipeline.
- **Rating 4 (16 pts):** Highly effective integration; prompt engineering, runtime selection, and model sizing reflect thoughtful engineering.
- **Rating 5 (20 pts):** Indispensable, masterful integration; model capabilities, fallbacks, parameter handling, and latency tradeoffs are deeply understood and defended.

### 3. Technical execution and working demonstration (Weight: 25 points)
- **Rating 0 (0 pts):** Application does not run; demo relies exclusively on pre-rendered video or static slides; crashes on launch.
- **Rating 1 (5 pts):** Fragile prototype that crashes during basic interaction; heavily scripted happy-path demo with no error handling.
- **Rating 2 (10 pts):** Core workflow runs, but suffers from significant bugs, unhandled errors, or very little engineering completed during the event.
- **Rating 3 (15 pts):** Solid live demo; core user workflow executes reliably in front of judges; handles basic inputs and standard edge cases.
- **Rating 4 (20 pts):** High technical stability; fast, smooth live execution; substantial coding achieved overnight; clean architecture.
- **Rating 5 (25 pts):** Flawless live demo; robust error recovery; clean, elegant engineering; verified compliance with declared track acceptance checks under live inspection.

### 4. Originality and creativity (Weight: 15 points)
- **Rating 0 (0 pts):** Direct duplicate of an existing boilerplate tutorial or public repo with zero original thought or modification.
- **Rating 1 (3 pts):** Minor cosmetic restyling of existing sample code; predictable concept with negligible team insight.
- **Rating 2 (6 pts):** Standard, familiar idea implemented with some localized adaptation or minor functional customization.
- **Rating 3 (9 pts):** Fresh perspective on a genuine problem; creative technical approach or unique user interaction design.
- **Rating 4 (12 pts):** Inventive, memorable concept combining technical capability with distinctive creative insight.
- **Rating 5 (15 pts):** Breakthrough innovation; highly original concept that surprises and delights the panel; exceptional problem-solving ingenuity.

### 5. Responsible AI, privacy and safety (Weight: 10 points)
- **Rating 0 (0 pts):** Blatant disregard for privacy or safety (e.g., exposing private student data, executing arbitrary unvalidated shell commands, hardcoded API secrets).
- **Rating 1 (2 pts):** Minimal safety awareness; no input boundaries; ignores privacy implications or model hallucinations.
- **Rating 2 (4 pts):** Basic awareness noted, but missing critical guardrails, disclaimers, or data sanitization procedures.
- **Rating 3 (6 pts):** Sound safety baseline; no hardcoded secrets; clear user disclaimers; graceful failure states; bounded tool execution.
- **Rating 4 (8 pts):** Proactive safety design; input validation, hallucination mitigation, synthetic test data, and user confirmation on actions.
- **Rating 5 (10 pts):** Exemplary responsible AI engineering; comprehensive privacy protection (e.g., 100% offline edge privacy or robust safety filters), ethical data handling, and transparent disclosure of model limitations.

### 6. Open-source quality and reproducibility (Weight: 15 points)
- **Rating 0 (0 pts):** Missing or invalid license; private repository after deadline; broken or empty documentation.
- **Rating 1 (3 pts):** License file exists, but README is empty or missing installation instructions; no attribution.
- **Rating 2 (6 pts):** Standard README with partial setup steps, but difficult cold-start, missing dependencies, or vague team role attribution.
- **Rating 3 (9 pts):** Clean public repository with valid OSI license, reproducible cold-start setup instructions, and transparent AI coding tool disclosures.
- **Rating 4 (12 pts):** High-quality open-source repository; effortless installation instructions; clear architecture diagrams; clean commit history.
- **Rating 5 (15 pts):** Exemplary open-source standard; pristine repository hygiene; comprehensive documentation; modular structure; full citations of model terms and upstream dependencies.

---

## Challenge-specific evaluation within the unified rubric

iTech Club provides **5 preset challenge tracks** to give teams structured starting points:

1. **[Build a Gemma Agent Skill]({{ site.baseurl }}/challenges/01-agent-skill/)**
2. **[Gemma Off the Grid]({{ site.baseurl }}/challenges/02-edge-offline/)**
3. **[Multimodal Campus Companion]({{ site.baseurl }}/challenges/03-multimodal-assistant/)**
4. **[Gemma-Powered Dev Harness]({{ site.baseurl }}/challenges/04-dev-harness/)**
5. **[Campus Knowledge Companion (RAG)]({{ site.baseurl }}/challenges/05-rag-knowledge-companion/)**

### Fair cross-track evaluation

- **One primary track per team:** Each team declares exactly one primary track in their `README.md`.
- **Acceptance criteria inform the rubric:** Challenge-specific acceptance tests guide judges when scoring the universal rubric (specifically *Technical Execution*, *Meaningful Gemma Integration*, and *Responsible AI*).
- **No bonus points:** Challenge-specific requirements are **not** separate bonus categories and cannot push criterion scores above their maximum weights.
- **Equal podium access:** All eligible teams across all five tracks are evaluated in a single unified pool against the same 100-point rubric.

---

## Selecting the top three projects

The local competition recognizes the top three overall teams:

- **First Place – Overall Winner**
- **Second Place – Overall Runner-up**
- **Third Place – Overall Third Place**

### Score tabulation process

1. The organisers collect all completed judge score sheets following demonstrations.
2. For each team, judges' individual total scores (0–100) are averaged arithmetically:
   $$\text{Final Score} = \frac{1}{N} \sum_{i=1}^{N} \text{Judge Total}_i \quad (N \ge 3 \text{ preferred, } N \ge 2 \text{ minimum})$$
3. Teams are ranked from highest to lowest according to their consolidated average score.
4. **No automated ranking software is used:** Organisers perform calculations transparently in a private workbook.

### Deterministic tie-breaking protocol

If two or more teams tie in their overall consolidated average score, ties are resolved using this pre-established hierarchy:

1. **Higher Meaningful Gemma Integration Score:** The team with the higher average score in *Meaningful Gemma/open-weight AI integration* (out of 20) takes precedence.
2. **Higher Technical Execution Score:** If still tied, the team with the higher average score in *Technical execution and working demonstration* (out of 25) takes precedence.
3. **Deliberation by the Judging Panel:** If still tied, the judging panel convenes for a structured conference led by the Lead Organizer. The panel reviews live demo notes, commit history freshness, and codebase depth to reach a consensus decision. The final decision and rationale are formally documented in the organiser records.

---

## Official MLH challenge distinction

To maintain complete clarity between local and global recognition:

1. **Official MLH Challenge (Best Open-Source AI Project):**
   - [Best Open-Source AI Project](https://hacktoberfest-handbook.mlh.com/fest-planning-guide/open-source-prize-categories) is the official MLH Hack Day competition on OrganizerHQ with **one winning team**.
   - The winner is selected by the organizing panel according to [MLH Hack Day guidelines](https://hacktoberfest-handbook.mlh.com/project-submissions-and-judging-for-hacktoberfest-hack-day) and marked directly in OrganizerHQ.
   - While the local First Place winner is typically a strong contender, the MLH winner must strictly satisfy all MLH-specific eligibility requirements (e.g., student status, individual MLH registration, OSI licensing).
2. **Local iTech Club Top Three Overall:**
   - The five local tracks represent iTech Club's curated project tracks—they are **not** five separate MLH prize categories.
   - The local podium honors the top three submissions across all five tracks based on the 100-point rubric.
3. **Partner Prize Policy:**
   - An additional partner prize (such as a Google Gemma partner category) is awarded **only if explicitly confirmed and configured** in OrganizerHQ for event 14735. Organisers will confirm on-site whether a partner prize is active; it is never assumed in advance.

---

## The standardised judge score sheet

Judges use a standardised scoring sheet to evaluate each project. An import-ready template is provided in [`templates/judge-score-sheet.csv`](https://github.com/ITech-Club-zetech-University/hacktoberfest/blob/main/templates/judge-score-sheet.csv).

### Required fields on each score sheet

- **Team Name & Declared Track:** Identified before the demo begins.
- **Repository URL:** Inspected during the evaluation.
- **Judge Identification & Date:** Name or assigned judge ID, and evaluation date.
- **Criteria Ratings (0–5):** Integer rating for each of the 6 criteria.
- **Weighted Criteria Scores:** Calculated via `(Rating / 5) * Weight`.
- **Total Score (0–100):** Sum of the six weighted scores.
- **Qualitative Feedback:**
  - *Strengths observed:* What impressed the judge about the code, demo, or problem-solving.
  - *Areas requiring improvement:* Specific suggestions for technical or documentation growth.
  - *Evidence / demonstration notes:* Notes on whether Gemma was running live and acceptance checks passed.
  - *Judge final recommendation:* Overall qualitative recommendation or remarks.
- **Conflict of Interest Declaration (Yes/No):** Formal confirmation of no conflict.

### Instructions for judges completing score sheets

1. Enter your assigned Judge ID, Team Name, and Track before the demo starts.
2. Watch the live 2-minute demonstration and participate in the 1-minute Q&A.
3. Assign an integer rating from 0 to 5 for each criterion based on the scoring anchors.
4. Record brief, concrete evidence in the notes column (e.g., *"Offline demo verified with Wi-Fi disabled; Ollama local inference ran in 4s"*).
5. Verify that your weighted scores sum correctly out of 100.
6. Submit completed sheets directly to the Lead Organiser immediately after the demo session.

---

## Complete 9-step judging procedure

The complete judging workflow is conducted in nine sequential steps:

```
[1. Verify Eligibility] ──> [2. Receive Materials] ──> [3. Team Demos]
                                                            │
[6. Consolidate Scores] <── [5. Score Sheets] <── [4. Inspect Repo & App]
         │
         ▼
[7. Review & Tie-Breakers] ──> [8. Announce Results] ──> [9. Mark MLH Winner]
```

### Step 1: Organisers verify team registration and submission eligibility
- **Time Window (Proposed):** 4:30 AM – 5:00 AM EAT.
- Organisers verify that submissions are registered on [MLH OrganizerHQ](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club) and run the administrative pre-screening check ([`scripts/check_submission.py`](#preliminary-eligibility-gate-vs-scoring)) to catch baseline issues (e.g., un-flipped private repositories or missing license files) before the 5:00 AM deadline.

### Step 2: Judges receive project list and judging materials
- **Time Window (Proposed):** 4:50 AM – 5:00 AM EAT.
- Organisers distribute the final project demo queue, track declarations, repository links, scoring anchors, and judge score sheets to confirmed panel members.
- Judges declare any conflicts of interest; organisers reassign judging duties as needed so every team has at least 3 independent evaluations where capacity allows.

### Step 3: Each team presents its working application
- **Time Window (Proposed):** 5:00 AM – 5:45 AM EAT *(Confirmed timings announced on-site by lead organiser)*.
- **Presentation Time:** Strictly **2 minutes for demonstration** + **1 minute for judge Q&A** (total 3 minutes per team).
- **Time Management:** Timekeepers enforce strict cutoffs. Slide decks and pre-recorded videos are prohibited; teams must demonstrate running software live on screen.

### Step 4: Judges inspect the repository and demonstration
- Judges actively observe the live workflow, verify that inputs yield dynamic model outputs, and inspect repository structure, code contributions, and AI tool disclosures.

### Step 5: Judges independently complete their score sheets
- Immediately following each team's demo and Q&A, judges assign ratings (0–5), calculate weighted scores, record brief supporting evidence, and finalize individual score sheets without discussing marks with peers.

### Step 6: Organisers consolidate the scores
- Organisers collect completed score sheets, audit them for completeness, discard any incomplete sheets, and compute the arithmetic average score for each team in an access-controlled workbook.

### Step 7: Judging panel reviews provisional top three and resolves ties
- Organisers present the provisional top three ranked teams to the panel.
- If score ties exist among podium contenders, the panel applies the published tie-breaking protocol (Gemma Integration score &rarr; Technical Execution score &rarr; documented panel deliberation).
- The panel conducts a final integrity check to confirm that winning projects were built during the event and adhere to open-source guidelines.

### Step 8: Organisers announce final results
- **Time Window (Proposed):** 5:55 AM – 6:00 AM EAT.
- Organisers announce the local Top Three Overall winners (First Place, Second Place, Third Place) live to the venue and present awards/certificates.

### Step 9: Official MLH winner is recorded in OrganizerHQ
- Following MLH requirements, organisers log in to OrganizerHQ with the **Announce Winners** toggle set to **PRIVATE**.
- Organisers locate the selected project under **Best Open-Source AI Project**, click **Mark Winner &rarr; Winner**, verify the gold badge, and switch **Announce Winners** to **PUBLIC** to publish the official gallery.

---

## Preliminary eligibility pre-screening vs. scoring
{: #preliminary-eligibility-gate-vs-scoring }

Before live demonstrations begin, organisers run [`scripts/check_submission.py`](https://github.com/ITech-Club-zetech-University/hacktoberfest/blob/main/scripts/check_submission.py) against submitted GitHub repository URLs:

```bash
# Check one or more repositories
python3 scripts/check_submission.py https://github.com/team-one/project https://github.com/team-two/project

# Check specifically for Challenge 1 (enforces SKILL.md presence)
python3 scripts/check_submission.py --track 1 https://github.com/team-one/agent-skill

# Run the automated offline test suite
python3 -m unittest discover -s tests -v
```

### Administrative scope of the checker
1. **URL Validation:** Verifies genuine `github.com` repository URLs with valid `owner/repo` path syntax.
2. **Public Visibility:** Confirms repository is accessible publicly without authentication.
3. **OSI License Presence:** Validates reported license metadata against canonical OSI-approved SPDX license identifiers stored in [`scripts/data/osi-approved-licenses.json`](https://github.com/ITech-Club-zetech-University/hacktoberfest/blob/main/scripts/data/osi-approved-licenses.json).
4. **Root README.md:** Confirms a root documentation entry point exists.
5. **Gemma Mention:** Scans README for "Gemma" as a **weak informational signal** to prompt teams to cite model terms.
6. **Track 1 SKILL.md:** When `--track 1` is specified, checks that `SKILL.md` is present.

### Strict operational boundaries

{: .warning }
> **The Checker is NOT an Evaluation Tool:**  
> - It does **NOT** award points, calculate scores, or rank projects.  
> - It does **NOT** evaluate code quality, system utility, or architecture.  
> - It does **NOT** verify whether Gemma was invoked or if inferences succeeded.  
> - It does **NOT** clone or execute participant code.  
> - Inconclusive outcomes (such as GitHub API rate limits or network timeouts) must **NEVER** penalize a team; organisers perform an immediate visual check in a browser.

| Status Category | Meaning | Organizer Action Required |
|---|---|---|
| **`ELIGIBLE (PASS)`** | Passes preliminary administrative hygiene checks. | Proceed directly to live demo. |
| **`NEEDS MANUAL REVIEW`** | Inconclusive metadata (e.g., root LICENSE present with unasserted SPDX ID, or 404 response on repo that may still be private). | Inspect in browser; assist team in resolving administrative issue before 5:00 AM. |
| **`CLEARLY INELIGIBLE`** | Definitive baseline failure (invalid URL, confirmed non-existent repo, or no code). | Confirm failure with Lead Organizer before disqualification. |
| **`CHECK UNAVAILABLE`** | Check was interrupted by rate limits or network timeout. | **Do NOT penalize the team.** Perform immediate manual visual check in browser. |

---

## Standard demo checklist for judges

Judges use this 6-point checklist during each 2-minute demonstration (participants should follow the [Live Demo Script Template]({{ site.baseurl }}/templates/demo-script/)):

- [ ] **Live software demonstration:** Project runs live on screen (not slides or pre-rendered video).
- [ ] **Meaningful Gemma integration verified:** Team demonstrates or shows logs of Gemma processing inputs and generating outputs.
- [ ] **Track acceptance test demonstrated:**
  - *Track 1:* Skill structure matches open standard and executes in an agent or test harness.
  - *Track 2:* Live demo executes with Wi-Fi/network completely disabled on local compute.
  - *Track 3:* Live input of a non-text image or audio file generates grounded response.
  - *Track 4:* Model autonomously initiates a bounded tool call with safety confirmation.
  - *Track 5:* Dynamic retrieval returns citations; system admits when information is absent.
- [ ] **Responsible AI & safety:** Boundaries, disclaimers, or data sanitization are visible and understood.
- [ ] **Code understanding & tool transparency:** Team members explain their implementation and disclose any AI coding assistants used.
- [ ] **Graceful boundary handling:** Application handles an edge case, invalid input, or missing data cleanly.

---

## Organiser source register

For the complete verification log, testing constraints, and licensing matrix, see the dedicated [Organiser Source Register](https://github.com/ITech-Club-zetech-University/hacktoberfest/blob/main/references/source-register.md).
