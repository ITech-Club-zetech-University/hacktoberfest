---
title: Organiser Runbook
nav_order: 9
has_children: true
permalink: /organizer-runbook/
description: "Operational event runbook, organizer checklists, roles, timeline, and winner marking workflow."
---

# Organiser Runbook
{: .no_toc }

This document provides operational guidance for event organizers, mentors, and the judging committee for the **Hacktoberfest Hack Day Nairobi × iTech Club**.

{: .note }
> **Public Operational Guidance:**  
> This runbook is published in the open repository to ensure community transparency in governance, timeline management, and scoring procedures. In compliance with event privacy standards, it contains **no private attendee data, personal phone numbers, secret API tokens, or unpublished judge marks**. Completed scoring records and incident logs are maintained exclusively in an internal, access-controlled organizer drive.

1. TOC
{: toc }

---

## 1. Verified Event Parameters

Organizers must verify all event details against the live [MLH Event Registration Page](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club):

- **Event Name:** Hacktoberfest Hack Day Nairobi × iTech Club (Event ID: `14735`)
- **Host Institution:** iTech Club, Zetech University
- **Date & Timing:** **Friday, 30 October 2026, 7:00 PM EAT → Saturday, 31 October 2026, 6:00 AM EAT**
- **Venue / audience:** Reconcile the listing's Ruiru Campus and attendance metadata with earlier local Mang'u/member-only instructions; publish one confirmed answer.
- **Official MLH Categories:** **Best Open-Source AI Project** and **Best Use of Gemma 4**, with [live links and requirements]({{ site.baseurl }}/challenges/#the-official-mlh-challenge).
- **Project Format:** Open-ended; no mandatory tracks. Brief problem discovery, user definition, appropriate AI and a focused MVP.
- **Local Awards / Team Size:** Confirm whether separate Top Three recognition and the former 3–4-member local restriction remain; do not present either as universal MLH policy.
- **Timing:** Public categories close at **6:00 AM EAT on 31 October**. Coding start/stop, submission opening and demos need reconciliation before announcement.

---

## 2. Staff Roles & Division of Duties

To ensure smooth overnight operations, assign staff members to these distinct roles before doors open:

| Role | Key Responsibilities | Primary Location |
|---|---|---|
| **Lead Event Organizer** | Overall event authority, final rule interpretations, MLH liaison, venue escalation | Main Stage / Roaming |
| **Registration & Check-In Lead** | Verifies student IDs, checks in attendees in OrganizerHQ, matches solo hackers during team formation (7:00–7:30 PM) | Welcome Desk |
| **Technical Mentorship Lead** | Conducts 8:00 PM Gemma Setup Workshop, coordinates roving technical mentors across tables | Hacking Tables |
| **Safety & Conduct Officer** | First point of contact for MLH Code of Conduct concerns, manages attendee wellbeing and venue safety | Quiet Space / Desk |
| **Timekeeper & Operations Lead** | Enforces published schedule, manages announcements, coordinates power strips and venue Wi-Fi | AV Desk |
| **Submission & Eligibility Checker** | Reviews repository hygiene and actual category evidence before the confirmed deadline; never excludes a broad-category project merely for lacking Gemma | Judge Desk |
| **Judge Panel Coordinator** | Distributes score sheets, briefs judges on rubric anchors, times 2-minute live demos and 1-minute Q&A | Judging Area |
| **Score Tabulator** | Consolidates judge sheets, computes averages, applies deterministic tie-breakers, verifies Top 3 | Private Tabulation Room |
| **OrganizerHQ Winner Lead** | Executes private/public winner marking in OrganizerHQ following official MLH workflow | Private Tabulation Room |

---

## 3. Pre-Event Readiness: Judging Materials & Offline Fallbacks

### A. Testing the Automated Checker
Prior to the submission window, verify the eligibility checker on the organizer workstation:
```bash
# 1. Run the full test suite (all tests must pass)
python3 -m unittest discover -s tests -v

# 2. Verify CLI options and help text
python3 scripts/check_submission.py --help
```

### B. Preparing Scoring Sheets
- Create a private, access-controlled spreadsheet (Google Sheets or Excel) in the organizer drive.
- Import the [judge score sheet CSV]({{ site.baseurl }}/templates/judge-score-sheet.csv). Delete the **three fictional examples** and copy the blank row for each team/judge pair. The CSV has **37 columns and no formulas**, including category eligibility/evidence/notes and actual categories considered.
- Set up **Eligible / Pending / Ineligible / Not Entered** status choices per category and **Scored / Not Assessed** for local overall assessment. No category defaults to eligible. Do not force unentered projects into a pool or assign them zero.
- Retain all evidence fields, wrap text and expand row heights. Keep judges' copies independent until submission. The category-only example has intentional blank numerical/criterion cells: do not confuse **Not Assessed** with an incomplete **Scored** block.
- For confirmed local assessment only, manually enter weighted values from the conversion table and audit all totals. Category qualitative notes do not add points.
- **Never store completed score sheets or personal judge notes in the public git repository.**

### C. Bandwidth & Offline Fallback Contingencies
- **Pre-downloading Advice:** Remind participants in pre-event emails to download Ollama and small quantized model weights (e.g. `gemma4:e2b` or `gemma2:2b`) at home before arriving.
- **Emergency USB Cache:** Have 2–3 USB flash drives ready at the help desk containing:
  - Python wheels for common packages (`google-genai`, `fastapi`, `uvicorn`, `sentence-transformers`)
  - Standalone Ollama installers (Linux/macOS/Windows)
  - Common model GGUF files for offline edge testing
- **Bandwidth Congestion Fallback:** Help teams test suitable local inference or connectivity alternatives without changing their problem. Disclose runtime changes; local-only fallback does not automatically meet the Gemma API prize requirement.

---

## 4. Master Event Schedule & Run of Show

{: .important }
> **Schedule reconciliation required:** The public event is **7:00 PM to 6:00 AM EAT** and public categories close at **6:00 AM**. The former eight-hour build and 5:00 AM cutoff are not confirmed current instructions. Verify OrganizerHQ, confirm actual coding allowances and announce a feasible submission/demo/judging schedule to all tables before enforcing it.

| Time (EAT) | Stage | Organizer Actions |
|---|---|---|
| **7:00 PM** | Public event start | Check in registered attendees and confirm collaborator/team policy |
| **Confirm with lead** | Briefing and setup | Explain own-problem format, both categories, common rubric, safety and optional provider choices |
| **Confirm start/stop** | Building | Mentors help narrow one user journey; reserve time for tests, documentation and publishing |
| **Before verified close** | Submission review | One submission, every eligible category; public licensed repo; review flags manually |
| **6:00 AM, 31 October** | Public category close / event end | Resolve this overlap with demos and awards in OrganizerHQ and announce the approved plan |
| **Confirmed feasible session** | Demos, judging and awards | Equal two-minute demos plus one-minute Q&A; validate scores and save category winners before announcement |

---

## 5. Submission Review & Judge Briefing

### Preliminary Hygiene Check Procedure
Before the confirmed deadline, as teams submit their GitHub URLs, the Eligibility Checker Lead runs:
```bash
python3 scripts/check_submission.py <repo-url-1> <repo-url-2> ...
```
- **`ELIGIBLE (PASS)`**: Team is cleared for demo schedule.
- **`NEEDS MANUAL REVIEW`**: Review before the confirmed deadline. Missing Gemma is not a failure for the broad category; inspect the actual open model and evidence rather than requiring a keyword.
- **`CLEARLY INELIGIBLE`**: Reported baseline failure (e.g. invalid URL, confirmed private visibility, or missing root README/license). Confirm manually with the Lead Organizer; the checker does not inspect working code.
- **`CHECK UNAVAILABLE`**: In case of GitHub API rate limit (403/429) or network timeout, **do not penalize the team**. Open the repository in a browser to visually verify baseline hygiene.

### Judge Briefing Checklist (4:50 AM)
Before demos begin, brief all judges on these core principles:
1. **Reward Working Substance Over Polish:** A functional terminal prototype using a suitable open model provides stronger evidence than a glossy UI with hardcoded responses. Verify Gemma 4/API evidence separately where entered.
2. **Independent Scoring:** Judges enter marks on their individual sheets without discussing scores during the demo.
3. **Mandatory Conflict Recusal:** Judges must recuse themselves from scoring any team they directly mentored or contributed code to.
4. **Time Limits:** Enforce strict time limits: exactly 2 minutes for demo, 1 minute for Q&A.

### Distinct category review — organiser approval required

Approve and announce the [proposed category lenses]({{ site.baseurl }}/judging/#category-specific-evaluation-lenses) before judging. They are local guidance, **not an official MLH numerical rubric**.

- **Best Open-Source AI Project:** verify originality, important functional open AI, public GitHub code, code licence and applicable skill/harness conditions. Review usefulness, technical demo, meaningful contribution, README/setup, exact model/model-licence/dependency disclosure, reproducibility and responsible data/limitations. DigitalOcean is optional; skills/harnesses are not the only eligible forms.
- **Best Use of Gemma 4:** verify actual Gemma 4 model ID and inference path, meaningful product use and the published API requirement. Review variant/route fit, useful capabilities, demo, reliability/tests, privacy, safety and documentation. No mandatory multimodal feature or domain; no credit for a README keyword alone.
- Record each category status and its evidence. **Pending** requires lead clarification; **Not Entered** and **Ineligible** stay out of that pool. Do not automatically remove an entry from the other pool.
- Assign category reviews only where eligible; obtain independent non-conflicted notes before discussion. Use one project/demo/repository for dual entry. Confirm whether one team may receive both prizes before decisions.
- Re-check [hosted model availability and API terms]({{ site.baseurl }}/starter-kit/#hosted-api-terms-check). Local runtime capability does not override published partner requirements.
- **iTech Club local Top Three awards** retain their own rubric and rules; confirm continuation and inventory rather than silently deleting or inventing prizes. Never award an official category solely from the local total.

---

## 6. Score Tabulation, Tie-Breaking & Separation of Notes

### Local overall aggregation formula

Use this section only for a confirmed **iTech Club local overall assessment**. It is not the decision rule for either official MLH category. Exclude **Not Assessed** numerical blocks rather than treating blanks as zero.
**Judge total = sum of the six (integer rating / 5 × criterion weight) values**, out of 100.

**Team final score = sum of valid judge totals / number of valid independent judges**, with 3 preferred and 2 required. Use the same valid sheets for criterion averages and tie-breakers. Preserve full precision for comparisons; round displayed averages only, to two decimal places.

- **Judging Capacity:** Each team should receive **at least three independent evaluations** from distinct panel members wherever judging capacity allows (minimum 2 valid sheets required).
- **Human-only Decisions:** Organisers manually enter/check arithmetic in a private workbook. No AI judge, automated score aggregation service, ranking software, leaderboard or automated winner selection. Compare each official category's eligible pool separately using independent notes and a documented human rationale.
- **Sheet Validation:** Follow the [published tabulation procedure]({{ site.baseurl }}/judging/#score-tabulation-process). Return missing fields or arithmetic errors to the original judge without revealing other scores. Never substitute zero for a blank. Exclude conflicted, duplicate or uncorrected incomplete sheets with a recorded reason. If fewer than two valid independent sheets remain, arrange another non-conflicted evaluation before finalising results.
- **Deterministic Tie-Breakers:** If team totals are tied, apply tie-breakers in this strict pre-published order:
  1. Higher average score in **Meaningful open-source/open-weight AI integration** (out of 20)
  2. Higher average score in **Technical execution and working demonstration** (out of 25)
  3. **Deliberation by the judging panel**, with the decision and rationale formally documented in organiser records
- **Podium Designations (only if local awards are confirmed):**
  - **First Place – Overall Winner**
  - **Second Place – Overall Runner-up**
  - **Third Place – Overall Third Place**

### Confidentiality of Judge Notes
- Individual judge score sheets, raw numerical points, internal deliberation notes, and provisional ranks are **strictly confidential internal records**.
- Only validated official winners, any confirmed local awards and appropriate high-level feedback are announced. Personal judge comments must never be posted publicly or shared with participants.

---

## 7. Winner Marking Workflow in MLH OrganizerHQ

Confirm the live controls in event `14735` and follow this procedure **before announcing results in the room**. Do not create a duplicate MLH challenge or an unassigned partner category; contact MLH if an expected category is missing.

1. Log in to [MLH OrganizerHQ](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club).
2. Ensure the **Announce Winners** toggle is set to **PRIVATE**.
3. Navigate to **Manage Submissions**.
4. Confirm and record the dual-prize policy, then review the eligible **Best Open-Source AI Project** pool against official requirements and approved local lenses. Filter that category in HQ.
5. Select the winning project, click **Mark Winner → Winner**, and verify the gold **WINNER** badge and **Winner saved** confirmation.
6. Separately review the eligible **Best Use of Gemma 4** pool and save its human decision/rationale. Mark its winner after checking the actual model/API evidence and confirmed dual-prize policy. Pending eligibility must be resolved first. Contact MLH if an expected category is missing; do not create a replacement.
7. Use **Preview public view**, check all projects, then switch **Announce Winners** from **PRIVATE** to **PUBLIC**. Verify **WINNERS ANNOUNCED**, **Submissions are public** and the public gallery. This publishes non-winning submissions too, but never upload confidential judge sheets.
8. Announce both saved official category winners and only any separately confirmed local awards.

---

## 8. Official Post-Event Requirements

Complete these required tasks within 24–48 hours of event closing:

1. **Event Photography:** Capture high-resolution photos of:
   - Group photo of all hackers and organizers
   - Winner presentation on stage
   - Action shots of hacking tables and live demos
2. **Public Project Gallery:** Confirm that the OrganizerHQ project gallery is set to public and viewable by all attendees.
3. **MLH Post-Event Reporting:** Complete the official MLH Hack Day wrap-up / event report form with verified attendance numbers.
4. **Receipts & Reimbursement Documentation:** If food, swag, or venue expenses qualify for MLH or club reimbursements, compile all itemized receipts, proof of payment, and attendee counts per the official MLH handbook guidelines.
5. **Attendee Feedback:** Send the post-event survey to participants to gather feedback for future iTech Club events.

---

## 9. Decision Log: Pre-Event Action Items

{: .note }
> `[ORGANISER CONFIRMATION REQUIRED]`  
> The following items must be confirmed by the Lead Organizer prior to opening doors:

| Item | Decision Needed | Assigned To | Status |
|---|---|---|---|
| **1. Categories in OrganizerHQ** | Both categories are publicly listed. Verify Best Open-Source AI Project and Best Use of Gemma 4 in authenticated HQ; confirm eligibility, API evidence and multiple-category winner policy. | Lead Organizer | Pending HQ Check |
| **2. Physical Awards for Local Top 3** | Confirm trophies, medals, certificates, or swag packs designated for the local 1st, 2nd, and 3rd Place Overall teams. | iTech Club Exec | Pending |
| **3. Open-Ended Format & Teams** | No track declaration. Record actual project and entered categories; confirm team-size/local-award policy and announce it. | Registration Lead | Pending Policy Confirmation |
| **4. Final Judge Roster** | Confirm roster of 3–5 faculty, mentor, and alumni judges and assign Judge IDs. | Judge Coordinator | Pending Roster |
| **5. Schedule & Winner Controls** | Reconcile public 6:00 AM close with demos/event end; confirm build start/stop, submission opening, timezone, winner saving and publication. Announce one approved schedule. | OrganizerHQ Winner Lead | Pending HQ Check |
| **6. Demo Capacity & Calibration** | Rehearse the rubric and sample sheets; confirm non-conflicted assignments. A single 45-minute demo session fits at most 15 three-minute slots before transitions or scoring time; publish any fair parallel-session plan or approved timing change to everyone. | Judge Coordinator | Pending |
| **7. MLH Prizes & Onboarding** | Confirm DEV account collection, any swag availability and assigned partner conditions against MLH onboarding; confirm local awards separately. | Lead Organizer | Pending HQ / Onboarding Check |

---

## 10. "Before Opening Doors" Final Checklist (6:30 PM EAT)

- [ ] Venue power strips tested and operational across all tables.
- [ ] Venue Wi-Fi SSID and credentials clearly displayed on whiteboards/screens.
- [ ] Projector and audio system tested for opening slides and live demos.
- [ ] Emergency USB drives preloaded with Ollama, common Python wheels, and GGUF models.
- [ ] Check-in desk prepared with attendee roster and OrganizerHQ dashboard open.
- [ ] Code of Conduct reporting contact designated and visible to attendees.
- [ ] Private judge scoring spreadsheet created and shared only with confirmed judges.
- [ ] Automated eligibility checker verified (`python3 -m unittest discover -s tests -v` passing).
- [ ] Water and snacks staged for overnight hackers.
- [ ] Doors unlocked and welcome signage posted at venue entrance.
