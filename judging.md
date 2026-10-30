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
2. **Open-ended projects:** Teams choose their own users, problems, domains and architectures. Judges compare practical outcomes and evidence against the same rubric, not a prescribed technical track.
3. **Live demonstration verification:** A two-minute live demonstration and code walk-through answers crucial questions no script can evaluate: Does the software actually run? Does the chosen open-source/open-weight AI meaningfully power the product? Can the team explain what they built and where its limitations lie?

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
- **Avoid favouritism:** All teams are granted equal presentation time and evaluated with impartial professional standards regardless of domain, model/provider choice or background.
- **Strict confidentiality:** Individual score sheets, raw numerical marks, internal notes, and provisional tallies are **strictly confidential internal records**. They are never published on the website or disclosed to participants. Only final validated winners and high-level constructive feedback are announced.

---

<a id="the-100-point-operational-rubric"></a>

## Standardised 100-point judging rubric
{: #the-100-point-score-sheet }

Every project is evaluated out of **100 total weighted points** across six core criteria:

| Evaluation criterion | Weight | Core question for judges |
|---|:---:|---|
| **Problem relevance and practical impact** | **15** | Does the project address a real, clearly articulated campus, community, or developer need with demonstrable practical impact? |
| **Meaningful open-source/open-weight AI integration** | **20** | Is the chosen open-source/open-weight model an important, functioning component of the product rather than a disconnected afterthought? |
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

**Weighted score = (integer rating / 5) × criterion weight.**

### Weighted point conversion table

| Criterion | Weight | Rating 0 | Rating 1 | Rating 2 | Rating 3 | Rating 4 | Rating 5 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Problem relevance and practical impact | **15** | 0.0 | 3.0 | 6.0 | 9.0 | 12.0 | 15.0 |
| Meaningful open-source/open-weight AI integration | **20** | 0.0 | 4.0 | 8.0 | 12.0 | 16.0 | 20.0 |
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

### 2. Meaningful open-source/open-weight AI integration (Weight: 20 points)
- **Rating 0 (0 pts):** Relevant open-source/open-weight AI is absent or non-functional; only a non-working mock or unrelated proprietary model is shown.
- **Rating 1 (4 pts):** Superficial wrapper or trivial prompt; the model could be deleted without altering the product's core utility.
- **Rating 2 (8 pts):** The model is invoked, but its role is weakly justified, outputs are unvalidated or capability/runtime choices are unexamined.
- **Rating 3 (12 pts):** Substantive, functional integration; the chosen model powers an important analytical, generative, perceptual or predictive pipeline.
- **Rating 4 (16 pts):** Highly effective integration; prompt engineering, runtime selection, and model sizing reflect thoughtful engineering.
- **Rating 5 (20 pts):** Indispensable, masterful integration; model capabilities, fallbacks, parameter handling, and latency tradeoffs are deeply understood and defended.

### 3. Technical execution and working demonstration (Weight: 25 points)
- **Rating 0 (0 pts):** Application does not run; demo relies exclusively on pre-rendered video or static slides; crashes on launch.
- **Rating 1 (5 pts):** Fragile prototype that crashes during basic interaction; heavily scripted happy-path demo with no error handling.
- **Rating 2 (10 pts):** Core workflow runs, but suffers from significant bugs, unhandled errors, or very little engineering completed during the event.
- **Rating 3 (15 pts):** Solid live demo; core user workflow executes reliably in front of judges; handles basic inputs and standard edge cases.
- **Rating 4 (20 pts):** High technical stability; fast, smooth live execution; substantial coding achieved overnight; clean architecture.
- **Rating 5 (25 pts):** Flawless live demo; robust error recovery; clean, elegant engineering; convincing normal, edge-case and failure/uncertainty test evidence under live inspection.

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

## Project-specific evidence within the unified rubric

### Fair evaluation across different projects
{: #fair-cross-track-evaluation }

- **No primary track:** Teams choose their own problem, users, domain, model and architecture.
- **Common rubric:** Apply the same six weights and 0–5 anchors. Evidence must relate to the team's actual use case and claims, not an archived brief.
- **No bonus points:** Optional inspiration, provider choice, model size and additional features do not add criteria, score caps or fixed deductions.
- **Incomplete prototypes:** Record missing or failed functionality under the relevant criterion; it is not automatic disqualification. Published [eligibility and conduct rules]({{ site.baseurl }}/rules/#governance-disqualification-ownership) remain separate.
- **Comparable evidence:** CLI, web and mobile interfaces and suitable hosted/local approaches are acceptable. Judge usefulness, engineering and proportionate safety, not spending or presentation polish. Offline inference alone does not establish complete privacy.
- **Separate category eligibility:** Verify each selected category's published conditions separately. Other suitable open models are welcome in the broad category; meaningful Gemma 4 use and the published API conditions apply to the Gemma category. See the [official category links]({{ site.baseurl }}/challenges/#the-official-mlh-challenge).
- **Tests:** Look for normal, edge-case and at least one failure/uncertainty scenario with actual results. A model response alone is not proof of success.

---

## Selecting the top three projects

If organisers confirm separate local Top Three recognition, the designations are:

- **First Place – Overall Winner**
- **Second Place – Overall Runner-up**
- **Third Place – Overall Third Place**

### Score tabulation process

1. The organisers collect all completed judge score sheets following demonstrations.
2. For each team, average valid independent judge totals (0–100): **Final score = sum of valid judge totals / number of valid judges** (3 preferred, 2 minimum). Each judge has equal weight; use the same valid sheets for criterion averages and tie-breakers.
3. Teams are ranked from highest to lowest according to their consolidated average score.
4. **No automated ranking software is used:** Organisers perform calculations transparently in a private workbook.
5. Check every rating is an integer from 0 to 5, every weighted value matches the conversion table, and every total matches its six weighted values. Return incomplete or inconsistent sheets to the original judge for correction without discussing other judges' scores; never treat blanks as zero. Exclude conflicted, duplicate, or still-incomplete sheets and record why. If fewer than two valid independent sheets remain, arrange another non-conflicted evaluation before finalising results.
6. Preserve full precision for comparisons and tie-breakers; round only displayed averages to two decimal places. For example, totals of 80, 89 and 86 yield 85.00; with only 80 and 89 valid, the mean is 84.50. Display rounding must not create a tie.

### Deterministic tie-breaking protocol

If two or more teams tie in their overall consolidated average score, ties are resolved using this pre-established hierarchy:

1. **Higher Meaningful AI Integration Score:** The team with the higher average score in *Meaningful open-source/open-weight AI integration* (out of 20) takes precedence.
2. **Higher Technical Execution Score:** If still tied, the team with the higher average score in *Technical execution and working demonstration* (out of 25) takes precedence.
3. **Deliberation by the Judging Panel:** If still tied, non-conflicted judges review the recorded evidence against the same six published criteria and reach a consensus led by the Lead Organizer. Commit history may verify event-time work, but commit volume, pull-request counts, extra criteria and unpublished bonuses must not determine the result. Record the decision, participating judges and rubric-based rationale in the private organiser records.

---

## Official MLH challenge distinction

The live event has **Best Open-Source AI Project** (DigitalOcean-supported) and **Best Use of Gemma 4** (Gemma / Google DeepMind). They are award categories, not required project prompts. Follow the [live category requirements]({{ site.baseurl }}/challenges/#the-official-mlh-challenge) and [MLH winner workflow](https://hacktoberfest-handbook.mlh.com/project-submissions-and-judging-for-hacktoberfest-hack-day).

One project may enter every category it qualifies for. Review eligibility and record the human winner decision for each category separately; the common rubric is local judging guidance, not a claim that MLH mandates these weights. Confirm any multiple-category winner policy, separate local podium and prize inventory with organisers before announcing results.

---

## The standardised judge score sheet

Judges use a standardised scoring sheet to evaluate each project. [Download the judge score sheet CSV]({{ site.baseurl }}/templates/judge-score-sheet.csv) and import it into a private workbook.

The CSV is a **manual-entry template with no spreadsheet formulas**. It contains two clearly labelled fictional examples followed by a blank row to copy for each team/judge pair. Delete the examples from the operational workbook; never include them in averages. Use the conversion table above to fill weighted scores and verify totals. Enable text wrapping and expand row heights for evidence; each criterion has its own unrestricted text field. Keep all completed copies private.

### Required fields on each score sheet

- **Team Name & Entered Prize Categories:** Identified before the demo begins; no primary track.
- **Repository URL:** Inspected during the evaluation.
- **Judge Identification & Date:** Name or assigned judge ID, and evaluation date.
- **Criteria Ratings (0–5):** Integer rating for each of the 6 criteria.
- **Weighted Criteria Scores:** Calculated via `(Rating / 5) * Weight`.
- **Criterion evidence and comments:** A separate free-text field for each of the six criteria; record observations and missing or failed checks, not just the overall impression.
- **Total Score (0–100):** Sum of the six weighted scores.
- **Qualitative Feedback:**
  - *Strengths observed:* What impressed the judge about the code, demo, or problem-solving.
  - *Areas requiring improvement:* Specific suggestions for technical or documentation growth.
  - *Evidence / demonstration notes:* Actual model/runtime, working user flow and observed test outcomes; record category-specific eligibility evidence separately in private organiser records.
  - *Judge final recommendation:* Overall qualitative recommendation or remarks.
- **Conflict of Interest Declaration (Yes/No):** Enter **No** only when there is no conflict. Enter **Yes** and stop scoring if conflicted; notify the coordinator for reassignment. A conflicted sheet is excluded from all calculations.

### Instructions for judges completing score sheets

1. Enter your assigned Judge ID, Team Name, and entered prize categories before the demo starts.
2. Watch the live 2-minute demonstration and participate in the 1-minute Q&A.
3. Assign an integer rating from 0 to 5 for each criterion based on the scoring anchors.
4. Record brief, concrete evidence in each criterion's evidence/comments field (e.g., *"Offline demo verified with external adapters disabled; Ollama local inference ran in 4s"*). General notes and recommendations supplement evidence; they do not add points or override the rubric.
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
[7. Review & Tie-Breakers] ──> [8. Mark MLH Winner] ──> [9. Announce Results]
```

### Step 1: Organisers verify team registration and submission eligibility
- **Time window:** Organiser confirmation required; see [schedule status]({{ site.baseurl }}/rules/#the-hacking-timeline). Public category pages currently close at 6:00 AM EAT on 31 October.
- Organisers verify registration and selected categories on [MLH OrganizerHQ](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club), then review repository visibility, licence and actual category evidence. Administrative checks do not replace human eligibility review.

### Step 2: Judges receive project list and judging materials
- **Time window:** Confirm before demos, consistently with the saved submission close.
- Organisers distribute the final project demo queue, entered categories, repository links, scoring anchors, and judge score sheets to confirmed panel members.
- Judges declare any conflicts of interest; organisers reassign judging duties as needed so every team has at least 3 independent evaluations where capacity allows.

### Step 3: Each team presents its working application
- **Time window:** The Lead Organiser must announce a feasible demo session; the previous 5:00–5:45 AM slot is not confirmed.
- **Presentation Time:** Strictly **2 minutes for demonstration** + **1 minute for judge Q&A** (total 3 minutes per team).
- **Time Management:** Timekeepers enforce strict cutoffs. Slide decks and pre-recorded videos are prohibited; teams must demonstrate running software live on screen.

### Step 4: Judges inspect the repository and demonstration
- Judges actively observe the live workflow, verify that inputs yield dynamic model outputs, and inspect repository structure, code contributions, and AI tool disclosures.

### Step 5: Judges independently complete their score sheets
- Immediately following each team's demo and Q&A, judges assign ratings (0–5), calculate weighted scores, record brief supporting evidence, and finalize individual score sheets without discussing marks with peers.

### Step 6: Organisers consolidate the scores
- Organisers follow the score tabulation process above: correct arithmetic and missing fields with the original judge, exclude invalid sheets with a recorded reason, obtain at least two valid independent evaluations, and calculate full-precision averages in an access-controlled workbook.

### Step 7: Judging panel reviews provisional top three and resolves ties
- Organisers present the provisional top three ranked teams to the panel.
- If score ties exist among contenders, the panel applies the published tie-breaking protocol (open-source/open-weight AI Integration score &rarr; Technical Execution score &rarr; documented panel deliberation).
- The panel conducts a final integrity check to confirm that winning projects were built during the event and adhere to open-source guidelines.

### Step 8: Record and publish the official MLH winner before the room announcement
- **Time window:** After completed evaluation and score review, before announcing results.
- Following MLH requirements, organisers log in to OrganizerHQ with the **Announce Winners** toggle set to **PRIVATE**.
- Organisers locate the selected project under **Best Open-Source AI Project**, click **Mark Winner &rarr; Winner**, and verify the gold badge and **Winner saved** confirmation. Record **Best Use of Gemma 4** separately after checking its requirements and the confirmed multiple-category winner policy. Preview the public view, then switch **Announce Winners** to **PUBLIC** and verify the gallery before the room announcement. Confirm live controls and the saved window; contact MLH rather than creating duplicate categories.

### Step 9: Organisers announce final results
- **Time window:** Organiser-confirmed, after saved/publicly verified winner decisions.
- Announce the official category winners as recorded in OrganizerHQ and only any separately confirmed local awards.

---

## Preliminary eligibility pre-screening vs. scoring
{: #preliminary-eligibility-gate-vs-scoring }

Before live demonstrations begin, organisers run [`scripts/check_submission.py`](https://github.com/ITech-Club-zetech-University/hacktoberfest/blob/main/scripts/check_submission.py) against submitted GitHub repository URLs:

```bash
# Check one or more repositories
python3 scripts/check_submission.py https://github.com/team-one/project https://github.com/team-two/project

# Run the automated offline test suite
python3 -m unittest discover -s tests -v
```

### Administrative scope of the checker
1. **URL Validation:** Verifies genuine `github.com` repository URLs with valid `owner/repo` path syntax.
2. **Public Visibility:** Confirms repository is accessible publicly without authentication.
3. **OSI License Presence:** Validates reported license metadata against canonical OSI-approved SPDX license identifiers stored in [`scripts/data/osi-approved-licenses.json`](https://github.com/ITech-Club-zetech-University/hacktoberfest/blob/main/scripts/data/osi-approved-licenses.json).
4. **Root README.md:** Confirms a root documentation entry point exists.
5. **Gemma Mention:** Scans README for "Gemma" as a **weak informational signal** to prompt teams to cite model terms.
6. **Legacy skill option:** The retained `--track 1` CLI option only probes root `SKILL.md`; it does not represent a current competition track. Inspect skill conformance manually only for projects that are actually agent skills.

The legacy checker can flag a valid non-Gemma project for manual review. **Absence of Gemma is not an eligibility failure for Best Open-Source AI Project.** Review the actual open model and evidence; never require a team to add a misleading Gemma mention for a PASS.

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
| **`NEEDS MANUAL REVIEW`** | Inconclusive metadata (e.g., root LICENSE present with unasserted SPDX ID, or 404 response on repo that may still be private). | Inspect in browser; assist before the confirmed submission cutoff. |
| **`CLEARLY INELIGIBLE`** | Reported baseline failure such as an invalid URL, confirmed private visibility, or missing root README/license. The checker does not inspect whether working project code exists. | Confirm the actual failure manually with the Lead Organizer before disqualification. |
| **`CHECK UNAVAILABLE`** | Check was interrupted by rate limits or network timeout. | **Do NOT penalize the team.** Perform immediate manual visual check in browser. |

---

## Standard demo checklist for judges

Judges use this 6-point checklist during each 2-minute demonstration (participants should follow the [Live Demo Script Template]({{ site.baseurl }}/templates/demo-script/)):

- [ ] **Live software demonstration:** Project runs live on screen (not slides or pre-rendered video).
- [ ] **Meaningful AI integration verified:** Exact open model/runtime and real input/output evidence are shown. Check Gemma 4/API evidence only where that category is entered.
- [ ] **User outcome and tests demonstrated:** One primary user's flow, normal/edge inputs and at least one failure or uncertainty scenario are supported by actual results; no archived technical checklist is required.
- [ ] **Responsible AI & safety:** Boundaries, disclaimers, or data sanitization are visible and understood.
- [ ] **Code understanding & tool transparency:** Team members explain their implementation and disclose any AI coding assistants used.
- [ ] **Graceful boundary handling:** Application handles an edge case, invalid input, or missing data cleanly.

---

## Organiser source register

For the complete verification log, testing constraints, and licensing matrix, see the dedicated [Organiser Source Register](https://github.com/ITech-Club-zetech-University/hacktoberfest/blob/main/references/source-register.md).
