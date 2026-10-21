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
- **Venue:** Zetech University Technology Park, Mang'u Campus, Off Thika Road, Nairobi 00200, Kenya
- **Audience Eligibility:** Exclusive to registered Zetech University students and iTech Club members
- **Official MLH Challenge Category:** [Best Open-Source AI Project](https://hacktoberfest-handbook.mlh.com/fest-planning-guide/open-source-prize-categories) (1 winning team marked in OrganizerHQ)
- **Local Awards:** iTech Club Top Three Overall (1st, 2nd, and 3rd Place) evaluated via the published [100-Point Rubric]({{ site.baseurl }}/judging/#the-100-point-score-sheet)
- **Team Size Policy:** 3–4 members required for local award eligibility; solo hackers and pairs are welcome to attend, build, and submit to the general MLH competition

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
| **Submission & Eligibility Checker** | Runs automated baseline checker script (`check_submission.py`) between 4:30–5:00 AM, assists teams with manual reviews | Judge Desk |
| **Judge Panel Coordinator** | Distributes score sheets, briefs judges on rubric anchors, times 2-minute live demos and 1-minute Q&A | Judging Area |
| **Score Tabulator** | Consolidates judge sheets, computes averages, applies deterministic tie-breakers, verifies Top 3 | Private Tabulation Room |
| **OrganizerHQ Winner Lead** | Executes private/public winner marking in OrganizerHQ following official MLH workflow | Private Tabulation Room |

---

## 3. Pre-Event Readiness: Judging Materials & Offline Fallbacks

### A. Testing the Automated Checker
Prior to the submission window, verify the eligibility checker on the organizer workstation:
```bash
# 1. Run the test suite (must show 43 passing tests)
python3 -m unittest discover -s tests -v

# 2. Verify CLI options and help text
python3 scripts/check_submission.py --help
```

### B. Preparing Scoring Sheets
- Create a private, access-controlled spreadsheet (Google Sheets or Excel) in the organizer drive.
- Import [`templates/judge-score-sheet.csv`](https://github.com/ITech-Club-zetech-University/hacktoberfest/blob/main/templates/judge-score-sheet.csv).
- Pre-populate sheets for confirmed judges with columns for Team Name, Primary Track, Judge Name, the 5 rubric criteria, Total, Conflict of Interest, and Notes.
- **Never store completed score sheets or personal judge notes in the public git repository.**

### C. Bandwidth & Offline Fallback Contingencies
- **Pre-downloading Advice:** Remind participants in pre-event emails to download Ollama and small quantized model weights (e.g. `gemma4:e2b` or `gemma2:2b`) at home before arriving.
- **Emergency USB Cache:** Have 2–3 USB flash drives ready at the help desk containing:
  - Python wheels for common packages (`google-genai`, `fastapi`, `uvicorn`, `sentence-transformers`)
  - Standalone Ollama installers (Linux/macOS/Windows)
  - Common model GGUF files for offline edge testing
- **Bandwidth Congestion Fallback:** If venue Wi-Fi becomes congested overnight, encourage teams to switch to [Track 2: Gemma Off the Grid]({{ site.baseurl }}/challenges/02-edge-offline/) or use mobile hotspots for API token calls.

---

## 4. Master Event Schedule & Run of Show

{: .important }
> **Schedule Stability:** The published event window is **7:00 PM to 6:00 AM EAT**. Do not alter start, submission cutoff, demo, or closing times without formal approval from the Lead Organizer and announcement to all tables.

| Time (EAT) | Stage | Organizer Actions |
|---|---|---|
| **6:30 – 7:00 PM** | Setup & Venue Prep | Power on AV, test projector, verify registration desk, power strips, and Wi-Fi |
| **7:00 – 7:30 PM** | Check-in & Team Matching | Check in attendees on OrganizerHQ; match solo/pair hackers into 3–4 person teams |
| **7:30 – 8:00 PM** | Opening & Briefing | Welcome remarks, review 5 preset tracks, explain 100-pt rubric, code of conduct |
| **8:00 – 8:30 PM** | Gemma Setup Clinic | Technical walkthrough: Gemini API keys, safe `.env`, local Ollama setup |
| **8:30 PM – 4:30 AM** | **Building Window** (~8h) | Roving technical mentorship; hourly time checks; distribute water/snacks |
| **4:00 AM** | 30-Minute Warning | Announce submission deadline: *"1 hour until submission deadline at 5:00 AM"* |
| **4:30 – 5:00 AM** | Submission & Preliminary Review | Teams submit on OrganizerHQ & push to GitHub; checker runs preliminary hygiene check |
| **5:00 AM** | **Submission Cutoff** | Submissions locked; eligibility issues addressed; judge briefing conducted |
| **5:00 – 5:45 AM** | **Live Project Demos** | Time-boxed 2-minute live demos + 1-minute judge Q&A across the panel |
| **5:45 – 5:55 AM** | Score Consolidation & Winner Marking | Tabulate scores; apply tie-breakers; mark winners in OrganizerHQ |
| **5:55 – 6:00 AM** | Closing & Awards | Announce local Top Three Overall and official MLH winner; closing remarks |

---

## 5. Submission Review & Judge Briefing (4:30–5:00 AM)

### Preliminary Hygiene Check Procedure
At 4:30 AM, as teams submit their GitHub URLs, the Eligibility Checker Lead runs:
```bash
python3 scripts/check_submission.py <repo-url-1> <repo-url-2> ...
```
- **`ELIGIBLE (PASS)`**: Team is cleared for demo schedule.
- **`NEEDS MANUAL REVIEW`**: Organizer immediately visits the team's table to resolve administrative issues (e.g. flipping a private repository to public, adding the missing `LICENSE` file) before 5:00 AM.
- **`CLEARLY INELIGIBLE`**: Severe failure (no code, non-existent repo). Escalate to Lead Organizer.
- **`CHECK UNAVAILABLE`**: In case of GitHub API rate limit (403/429) or network timeout, **do not penalize the team**. Open the repository in a browser to visually verify baseline hygiene.

### Judge Briefing Checklist (4:50 AM)
Before demos begin, brief all judges on these core principles:
1. **Reward Working Substance Over Polish:** A functional terminal prototype or local CLI that executes real Gemma inference scores higher than a glossy web UI with hardcoded responses.
2. **Independent Scoring:** Judges enter marks on their individual sheets without discussing scores during the demo.
3. **Mandatory Conflict Recusal:** Judges must recuse themselves from scoring any team they directly mentored or contributed code to.
4. **Time Limits:** Enforce strict time limits: exactly 2 minutes for demo, 1 minute for Q&A.

---

## 6. Score Tabulation, Tie-Breaking & Separation of Notes

### Aggregation Formula
$$\text{Judge Total} = \sum (\text{5 Category Scores}) \quad [0 \dots 100]$$
$$\text{Team Final Score} = \frac{1}{N} \sum_{i=1}^{N} \text{Judge Total}_i \quad (N \ge 2)$$

- **Missing Sheets:** If a judge cannot complete a sheet, discard the incomplete sheet. The score is the average of completed sheets, provided at least 2 valid sheets remain.
- **Deterministic Tie-Breakers:** If team totals are tied, apply tie-breakers in this pre-published order:
  1. Highest aggregated score in **Use of Gemma / open-weight AI** (out of 25)
  2. Highest aggregated score in **Technical execution & working demo** (out of 25)
  3. Highest aggregated score in **Problem & impact** (out of 20)
  4. Highest aggregated score in **Open-source quality** (out of 15)
  5. Panel consensus conference led by Lead Organizer

### Confidentiality of Judge Notes
- Individual judge score sheets, raw numerical points, internal deliberation notes, and provisional ranks are **strictly confidential internal records**.
- Only final validated rankings (Top 3 Overall) and high-level constructive feedback are announced. Personal judge comments must never be posted publicly or shared with participants.

---

## 7. Winner Marking Workflow in MLH OrganizerHQ

Follow this exact step-by-step procedure to mark the official MLH winner:

1. Log in to [MLH OrganizerHQ](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club).
2. Ensure the **Announce Winners** toggle is set to **PRIVATE**.
3. Navigate to **Manage Submissions**.
4. Filter submissions by **Best Open-Source AI Project**.
5. Select the winning project, click **Mark Winner → Winner**, and verify that the gold **WINNER** badge appears next to the project name.
6. If an official partner challenge (e.g. Best Use of Gemma) was active and verified in OrganizerHQ, filter by that challenge and mark its winner.
7. Switch the **Announce Winners** toggle from **PRIVATE** to **PUBLIC** to publish the project gallery.
8. Announce the local Top Three Overall and official MLH winner live to the room.

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
| **1. Partner Challenge in OrganizerHQ** | Confirm whether an additional partner challenge (e.g. Best Use of Gemma) is enabled in OrganizerHQ for event `14735`, or if Best Open-Source AI Project is the sole challenge. | Lead Organizer | Pending HQ Check |
| **2. Physical Awards for Local Top 3** | Confirm trophies, medals, certificates, or swag packs designated for the local 1st, 2nd, and 3rd Place Overall teams. | iTech Club Exec | Pending |
| **3. Track Recording Mechanism** | Confirm whether primary track is recorded via README declaration only, or via check-in sheet at doors. | Registration Lead | Verified (README + Submission) |
| **4. Final Judge Roster** | Confirm roster of 3–5 faculty, mentor, and alumni judges and assign Judge IDs. | Judge Coordinator | Pending Roster |

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
