---
title: Judging
nav_order: 6
description: "How projects are scored: operational rubric, scoring anchors, tie-breakers, 5 AM judge workflow, and winner marking."
---

# Judging
{: .no_toc }

1. TOC
{: toc }

---

## Leaderboard vs. judge sheet: the decision

When planning this event, we evaluated two distinct evaluation models: a **fully automated leaderboard** (ranking repositories by commit counts, lines of code, or static test metrics), and a **judge sheet** (a published qualitative rubric evaluated by a human panel during live demonstrations). Here is why we chose a human panel with an automated preliminary hygiene gate.

### Automated leaderboard

**Pros:** Instantaneous feedback, operates continuously overnight without recruiting a human judge panel.

**Cons, specific to this event:**
- MLH's official [winner-selection guidance](https://hacktoberfest-handbook.mlh.com/project-submissions-and-judging-for-hacktoberfest-hack-day) for the mandatory Best Open-Source AI Project challenge is explicitly qualitative: judges assess whether a project *solves a clear problem*, *demonstrates original technical work*, and *explains itself clearly*. None of these can be determined by an automated script.
- The official MLH handbook states explicitly: **"Hacktoberfest does not use pull-request counts as the basis for these prizes."** Automated metrics that measure volume (commits, lines of code, PR counts) reward gaming rather than genuine utility.
- Our 5 challenge tracks represent distinct technical disciplines (agent skill standards, offline edge quantization, multimodal perception, agentic dev harnesses, and retrieval-augmented generation). A single automated formula that evaluates all five fairly does not exist.
- "Does it actually work in a live demo" and "can the team explain what they built" settle credibility in two minutes, which no static analysis script can replicate.

### Our approach: human judge sheet with a preliminary hygiene gate

{: .important }
> **Primary evaluation mechanism:** A published **100-point rubric** scored independently by a human judge panel during live, time-boxed 2-minute demonstrations.  
> **Preliminary hygiene gate:** Before live demos, an **automated eligibility checker** runs against submitted GitHub repositories to verify basic open-source hygiene (public repo, OSI license, `README.md`, Gemma mention). This automates administrative checks without pretending software can evaluate human creativity or usefulness.

---

## The 100-point operational rubric
{: #the-100-point-score-sheet #the-100-point-operational-rubric }

Every project is evaluated out of 100 points against this universal base rubric:

| Criterion | Points | Summary of Evaluation |
|---|---|---|
| **Problem & impact** | 20 | Does the project solve a real, clearly articulated campus, community, or developer need? |
| **Use of Gemma / open-weight AI** | 25 | Is Gemma an essential, functional part of the solution rather than a superficial afterthought? |
| **Technical execution & working demo** | 25 | Does the application work live in front of judges? Is substantial technical logic achieved during the event window? |
| **Originality & creativity** | 15 | Does the project offer a thoughtful, creative approach to the problem? |
| **Open-source quality** | 15 | Is the repository public with a valid OSI license, thorough cold-start docs, model attribution, and transparent AI tool disclosures? |
| **Total** | **100** | |

A ready-to-use template is in [`templates/judge-score-sheet.csv`](https://github.com/ITech-Club-zetech-University/hacktoberfest/blob/main/templates/judge-score-sheet.csv) for importing directly into Google Sheets or Excel.

---

## Detailed scoring anchors

To ensure consistent, objective evaluation that **rewards working substance over visual polish**, judges apply these explicit scoring anchors:

### 1. Problem & impact (0–20 points)
- **0 points (Missing / Not Demonstrated):** No clear problem identified; target user is unstated or completely undefined.
- **1–5 points (Low / Largely Incomplete):** Vague, generic problem statement; minimal connection to campus life, community needs, or real developer workflows.
- **6–11 points (Middle / Partially Working):** Genuine problem identified, but target audience is broad, assumptions are untested, or practical impact is weakly substantiated.
- **12–17 points (High / Strong Evidence):** Clear, practical, and well-scoped problem solving a real campus, community, or developer bottleneck with compelling impact.
- **18–20 points (Full / Exceptional):** Deeply relevant problem with outstanding clarity; immediate practical value to Zetech students, developers, or the broader community with demonstrable user empathy.

### 2. Use of Gemma / open-weight AI (0–25 points)
- **0 points (Missing / Not Demonstrated):** Gemma is not integrated, or replaced with an unrelated proprietary model; non-functional mock.
- **1–6 points (Low / Largely Incomplete):** Superficial wrapper or static prompt; Gemma could be removed entirely without affecting the core functionality of the product.
- **7–14 points (Middle / Partially Working):** Gemma is connected and invoked, but prompts are unoptimized, model parameters are unexamined, or reasoning is superficial.
- **15–21 points (High / Strong Evidence):** Substantive, functional integration; Gemma actively powers the core analytical, perceptual, or generative reasoning required by the application.
- **22–25 points (Full / Exceptional):** Outstanding, indispensable integration; model choice, prompt/tool architecture, parameter handling, and fallback behavior are deeply understood and defended by the team.

### 3. Technical execution & working demo (0–25 points)
- **0 points (Missing / Not Demonstrated):** Application does not run; demo relies solely on static slides or pre-rendered video; crashes on launch.
- **1–6 points (Low / Largely Incomplete):** Fragile build that crashes frequently; heavily scripted happy-path demo with no error handling or recovery.
- **7–14 points (Middle / Partially Working):** Core workflow works live, but suffers from noticeable bugs, unhandled edge cases, or minimal code written during the event.
- **15–21 points (High / Strong Evidence):** Solid, stable live demonstration; handles basic edge cases cleanly; substantial, demonstrable engineering completed during the 8-hour window.
- **22–25 points (Full / Exceptional):** Flawless live execution; robust error handling; passes all declared primary track acceptance tests cleanly under live inspection.

### 4. Originality & creativity (0–15 points)
- **0 points (Missing / Not Demonstrated):** Direct copy of a starter tutorial or existing public repository with zero original thinking.
- **1–4 points (Low / Largely Incomplete):** Minor cosmetic re-skin of boilerplate code; predictable idea with minimal personal insight.
- **5–9 points (Middle / Partially Working):** Standard, well-known concept executed with some novel local adaptation or practical twist.
- **10–13 points (High / Strong Evidence):** Fresh, thoughtful perspective on a real problem; clever technical adaptation or unique user workflow.
- **14–15 points (Full / Exceptional):** Highly inventive solution combining technical insight with unique creativity; creates a memorable, standout experience.

### 5. Open-source quality & transparency (0–15 points)
- **0 points (Missing / Not Demonstrated):** Missing license file, broken repository, or private repository after the submission deadline.
- **1–4 points (Low / Largely Incomplete):** License present but `README.md` is empty or lacks setup steps; no attribution of model terms or AI tools.
- **5–9 points (Middle / Partially Working):** Standard README with basic setup steps, but incomplete cold-start instructions, missing role breakdown, or vague disclosures.
- **10–13 points (High / Strong Evidence):** Clear OSI-approved `LICENSE`, reproducible cold-start instructions, declared primary track, accurate model terms citation, and transparent AI tool disclosures.
- **14–15 points (Full / Exceptional):** Pristine repository hygiene; effortless cold-start installation; clear architecture diagrams; comprehensive attribution; clean git history reflecting active hackathon collaboration.

---

## Score calculation & aggregation

1. **Judge Total:** Each judge rates all 5 categories for a team. The sum of the 5 criteria produces that judge's score out of 100.
2. **Team Final Score:** The final score for a team is the **arithmetic mean (average)** of the completed judge totals across all panel members who evaluated that team.
3. **Minimum Judge Panel:** Every team must be evaluated by **at least 2, and preferably 3, judges**.
4. **Handling Missing or Incomplete Score Sheets:**
   - If a judge fails to score all 5 categories or must step away mid-session, their incomplete sheet is discarded.
   - The team's score is computed as the mean of the remaining valid, completed score sheets, provided at least 2 completed sheets remain.
   - If an unexpected judge absence leaves a team with fewer than 2 completed sheets, an alternate neutral judge immediately reviews the team's live recorded demo and repository before final tabulation.

---

## Deterministic tie-breakers

To prevent arbitrary decisions or subjective re-voting at 5:00 AM, ties in overall aggregated scores are broken using this pre-agreed deterministic hierarchy:

1. **Tie-Breaker 1:** Highest aggregated score in **Use of Gemma / open-weight AI** (out of 25).
2. **Tie-Breaker 2:** Highest aggregated score in **Technical execution & working demo** (out of 25).
3. **Tie-Breaker 3:** Highest aggregated score in **Problem & impact** (out of 20).
4. **Tie-Breaker 4:** Highest aggregated score in **Open-source quality** (out of 15).
5. **Tie-Breaker 5:** Structured consensus conference led by the Lead Organizer, reviewing code commit history and demo integrity.

---

## One primary track per team

Each team must declare **one primary preset track** (Track 1, 2, 3, 4, or 5) in their repository `README.md` and submission description.

- **No Double-Dipping:** Teams cannot submit the same project to multiple local tracks. This ensures fair, peer-level comparison among projects tackling the same domain.
- **Acceptance Checks Inform the Rubric:** The challenge-specific acceptance tests on each track page provide objective benchmarks for scoring the **Technical execution & working demo** (0–25) and **Use of Gemma** (0–25) categories. They are **not** hidden bonus points and cannot push category scores above their published maximums.

---

## Award structure: Local Top 3 vs. Official MLH Award

To avoid confusion among judges and participants, understand how local recognition relates to the official MLH challenge:

1. **Local iTech Club Recognition (Top Three Overall):**
   - All eligible submissions across all 5 preset tracks are ranked together on a single leaderboard using the universal 100-point rubric.
   - The top three ranked teams are awarded **1st Place, 2nd Place, and 3rd Place Overall**.
   - Preset tracks provide structured focus areas and peer comparison; individual track excellence may be acknowledged with honorable mentions at the organizer's discretion, but the primary competitive podium is the Top Three Overall.
2. **Official MLH Challenge (Best Open-Source AI Project):**
   - [Best Open-Source AI Project](https://hacktoberfest-handbook.mlh.com/fest-planning-guide/open-source-prize-categories) is the official MLH Hack Day competition on OrganizerHQ with **one winning team**.
   - The winning project is selected by the organizing panel according to [MLH Hack Day guidelines](https://hacktoberfest-handbook.mlh.com/project-submissions-and-judging-for-hacktoberfest-hack-day) and marked directly in OrganizerHQ.
   - While the locally highest-scoring project is a very strong candidate, the MLH winner must be evaluated and marked in OrganizerHQ following official MLH requirements. The local #1 is not automatically guaranteed to be the MLH winner if MLH-specific eligibility requirements differ or if separate criteria apply.
3. **Partner Prize Policy:**
   - If an official partner challenge (such as a Google Gemma partner prize) has not been verified in OrganizerHQ for event 14735, it is **not** awarded or named as a confirmed category in participant-facing materials.

---

## Governance, ethics & appeals

- **Conflicts of Interest:** No judge may evaluate a project if they contributed code, provided intense non-neutral mentoring, or have an immediate personal/academic conflict with team members. Conflicted judges must recuse themselves; the team's score will be the average of the remaining non-conflicted judges (minimum 2).
- **Independent Scoring:** Judges enter ratings independently during the demonstration without discussing scores or attempting to influence other judges before individual sheets are submitted.
- **Strict Submission Deadline:** The submission deadline is **5:00 AM EAT**. Submissions after 5:00 AM are marked late. A grace period (up to 10 minutes) is granted only for verified platform outages (e.g. GitHub or OrganizerHQ downtime). Late projects may demo for mentor feedback but are ineligible for awards.
- **Confidentiality of Scoring:** Individual judge score sheets, raw numerical marks, internal notes, and provisional rankings are **strictly confidential**. They are never published on the public website or disclosed to participants. Only final validated winners and high-level constructive comments are shared publicly.
- **Final Authority:** The Lead Event Organizer (Faculty/iTech Club advisor), in consultation with the MLH representative, holds final authority for resolving any rule interpretation, edge case, or dispute.

---

## Preliminary eligibility gate vs. scoring

Before live demos begin, organizers run [`scripts/check_submission.py`](https://github.com/ITech-Club-zetech-University/hacktoberfest/blob/main/scripts/check_submission.py) against submitted GitHub repository URLs:

```bash
# Check one or more repositories
python3 scripts/check_submission.py https://github.com/team-one/project https://github.com/team-two/project

# Check specifically for Challenge 1 (enforces SKILL.md presence)
python3 scripts/check_submission.py --track 1 https://github.com/team-one/agent-skill

# Run the automated offline test suite
python3 -m unittest discover -s tests -v
```

### What the checker checks
1. **Genuine GitHub URL parsing:** Strictly accepts `github.com` and `www.github.com` URLs with valid two-segment `owner/repo` paths; rejects lookalike domains (`notgithub.com`, `github.com.evil.com`) and malformed links.
2. **Public repository visibility:** Verifies that the repository is accessible without authentication and is not configured as private.
3. **Open-source software license:** Validates reported license metadata against canonical OSI-approved SPDX license identifiers stored in [`scripts/data/osi-approved-licenses.json`](https://github.com/ITech-Club-zetech-University/hacktoberfest/blob/main/scripts/data/osi-approved-licenses.json) (sourced from the [SPDX License List v3.26](https://spdx.org/licenses/) and [Open Source Initiative](https://opensource.org/licenses/), last reviewed 20 October 2026).
4. **Root `README.md` presence:** Verifies that a documentation entry point exists at repository root.
5. **README mentions Gemma (weak signal):** Checks for word-boundary mentions of "Gemma" in the README. This is explicitly labeled as a **weak signal only**; it flags repositories that might have omitted model attribution, but does not substitute for judge verification of substantive model use.
6. **Track 1 `SKILL.md` presence:** When invoked with `--track 1`, verifies that `SKILL.md` exists at repository root. For all other tracks, `SKILL.md` presence or absence is purely informational and has no effect on baseline eligibility.

### What the checker does NOT check
- **Not an AI judge or leaderboard:** It does not score code quality, system utility, architectural elegance, or assign numerical points.
- **Not proof of model integration:** It cannot verify whether Gemma was actually invoked, if inferences succeeded, or if responses were generated by Gemma.
- **Not a plagiarism or security scanner:** It does not compare code against external repositories or check for vulnerabilities.
- **Not a legal opinion:** Verifying an SPDX identifier confirms repository metadata hygiene, not that the full text of a custom license is legally sound.
- **Never executes code:** The script performs read-only GitHub API requests. It never clones participant repositories, runs local shell commands, or exposes `GITHUB_TOKEN`.

### Operational status categories & exit codes

The script categorizes each submission into one of four operational states and exits with a standard process exit code:

| Status Category | Meaning | Organizer Action Required |
|---|---|---|
| **`ELIGIBLE (PASS)`** | Passes all preliminary hygiene checks (public, OSI license, README, Gemma mention, SKILL.md if Track 1). | Proceed directly to live demo. |
| **`NEEDS MANUAL REVIEW`** | Inconclusive or non-standard metadata (e.g. valid non-OSI SPDX ID, root `LICENSE` file present with unasserted SPDX ID, README lacks "Gemma", or 404 response on repo that may still be set to private). | Inspect repository in browser; allow team until 5:00 AM to resolve administrative issues. |
| **`CLEARLY INELIGIBLE`** | Definitive baseline failure (invalid GitHub URL, confirmed private repo, or completely missing README/LICENSE). | Confirm failure with Lead Organizer before disqualification. |
| **`CHECK UNAVAILABLE`** | Automated check was interrupted by a GitHub API rate limit (HTTP 403/429) or network timeout. | **Do NOT penalize the team.** Perform immediate visual manual inspection in browser. |

**Process exit codes:**
- `0`: All checked repositories are `ELIGIBLE (PASS)`.
- `1`: At least one repository is `CLEARLY INELIGIBLE`.
- `2`: At least one repository is `NEEDS MANUAL REVIEW` or `CHECK UNAVAILABLE` (and none are `CLEARLY INELIGIBLE`).
- `3`: Command-line syntax or invocation error (e.g. no URLs provided).

{: .warning }
> **Critical Rule on Inconclusive Results:**  
> Automated API rate limits (HTTP 403/429), connection timeouts, or unasserted license texts must **NEVER** be interpreted as evidence of team noncompliance or project failure. In any inconclusive state, organizers must perform an immediate visual check of the repository in a web browser.

---

## Standard demo checklist for judges

Judges use this 5-point checklist during each 2-minute demonstration (participants should follow the [Live Demo Script Template]({{ site.baseurl }}/templates/demo-script/)):

- [ ] **Live software demonstration:** Project runs live in front of the panel (not a pre-recorded video or slide deck).
- [ ] **Active Gemma integration verified:** Team demonstrates or shows logs of Gemma processing inputs and generating responses.
- [ ] **Track acceptance test demonstrated:**
  - *Track 1:* Skill structure matches open standard and executes in an agent or test harness.
  - *Track 2:* Live demo executes with Wi-Fi/network completely disabled on local compute.
  - *Track 3:* Live input of a non-text image or audio file generates grounded response.
  - *Track 4:* Model autonomously initiates a bounded tool call with safety confirmation.
  - *Track 5:* Dynamic retrieval returns citations; system admits when information is absent.
- [ ] **Code understanding & tool transparency:** Team members clearly explain their architecture, prompts, and disclose any AI coding tools used.
- [ ] **Graceful boundary handling:** Application handles an edge case, invalid input, or missing data cleanly.

---

## Compact 5:00 AM judge decision flow

When judging begins at 5:00 AM EAT, follow this streamlined 6-step workflow:

1. **Confirm Eligibility Gate:** Verify that all teams scheduled for demos have status `ELIGIBLE (PASS)` or cleared manual review.
2. **Time-Box Demos & Score Independently:** Conduct each demo (2 minutes demo + 1 minute Q&A). Judges score silently and independently on individual sheets across all 5 criteria (sum out of 100). Recuse if conflicted.
3. **Audit Score Sheets:** Tabulator collects sheets, verifies at least 2 completed sheets per team, and discards any incomplete sheets.
4. **Compute Averages & Apply Tie-Breakers:** Calculate the arithmetic mean of judge totals for each team. Apply deterministic tie-breakers (Gemma → Tech Execution → Impact → Open Source) if totals are tied.
5. **Review Top Three Overall:** Validate that the top three overall teams meet all hackathon rules (fresh build, valid license, functioning demo).
6. **Mark Winners in MLH OrganizerHQ:**  
   In compliance with [official MLH requirements](https://hacktoberfest-handbook.mlh.com/project-submissions-and-judging-for-hacktoberfest-hack-day#mark-every-winner):
   - Keep the **Announce Winners** toggle set to **PRIVATE** during evaluation.
   - Go to **Manage Submissions** in OrganizerHQ.
   - Filter by **Best Open-Source AI Project**, select the winning project, click **Mark Winner → Winner**, and verify the gold **WINNER** badge.
   - If an official partner challenge was verified and active, mark its corresponding winner.
   - Switch **Announce Winners** to **PUBLIC** to publish the official gallery.
   - Announce the local Top Three Overall and the official MLH winner live in the venue.

{: .note }
> `[ORGANISER CONFIRMATION REQUIRED]`  
> **Pre-Event Organizer Action Items for Event 14735:**  
> Prior to the hacking window opening, the lead organizer must log in to OrganizerHQ and complete these checks:  
> 1. Open **OrganizerHQ → Challenges** and confirm whether **Best Open-Source AI Project** is the sole challenge, or whether an additional partner challenge (such as a Google Gemma partner prize) is enabled for event 14735.  
> 2. Confirm the roster of 3–5 confirmed judges and assign judge numbers before 5:00 AM.  
> 3. Confirm physical prizes/trophies/swag designated for the local Top Three Overall.

---

## Organiser-maintained source register

For the complete verification log, testing constraints, and licensing matrix, see the dedicated [Organiser Source Register](https://github.com/ITech-Club-zetech-University/hacktoberfest/blob/main/references/source-register.md).
