---
title: "Quick-Reference Checklist"
parent: Organiser Runbook
nav_order: 1
permalink: /organizer-checklist/
description: "Chronological operational checklist for event hosts, leads, and mentors running Hack Day."
---

# Hack Day Organiser Quick-Reference Checklist

A chronological operational checklist for event hosts, leads, and mentors running the **Hacktoberfest Hack Day Nairobi × iTech Club**.

---

## 1. Pre-Event Setup & Verification (T-Minus 24 Hours)

- [ ] **Verify Event Listing:** Confirm venue, timing (**Friday 30 Oct 2026, 7:00 PM – Saturday 31 Oct 2026, 6:00 AM EAT**), and registration at [events.mlh.com/events/14735](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club).
- [ ] **OrganizerHQ Configuration Check:** Both **Best Open-Source AI Project** and **Best Use of Gemma 4** are publicly listed. Verify them in authenticated HQ, including actual requirements and multiple-category winner policy.
- [ ] **Test Automated Checker:** Run `python3 -m unittest discover -s tests -v` on the organiser workstation; all tests must pass.
- [ ] **Prepare Private Judge Sheets:** Import the [judge score sheet CSV]({{ site.baseurl }}/templates/judge-score-sheet.csv), delete fictional examples and duplicate the blank row. It has no formulas; verify manual arithmetic using the conversion table. Wrap and expand criterion evidence cells and keep judges' scores independent.
- [ ] **Reconcile Schedule:** Public categories close at **6:00 AM EAT on 31 October**, also the event end. Confirm coding start/stop, submission opening and feasible demos/awards with the lead and in HQ; announce one schedule. Do not enforce the previous 5:00 AM cutoff or assume eight coding hours.
- [ ] **Emergency Offline USB Drives:** Pre-load 2–3 USB drives with Ollama installers, quantized GGUF weights (`gemma4:e2b`, `gemma2:2b`), and common Python wheels.
- [ ] **Confirm Judge Panel:** Confirm 3–5 faculty, mentor, or alumni judges and distribute rubric scoring anchors.

---

## 2. Before Opening Doors (6:30 PM EAT)

- [ ] **Power & AV:** Inspect power outlets and extension cords across all tables; test projector and microphone.
- [ ] **Wi-Fi Credentials:** Write venue Wi-Fi SSID and password clearly on whiteboards/screens.
- [ ] **Welcome Desk:** Stage check-in desk with attendee roster and OrganizerHQ dashboard open.
- [ ] **Water & Refreshments:** Ensure drinking water and late-night snacks are staged.
- [ ] **Code of Conduct:** Confirm on-site safety contact and verify incident escalation procedure.

---

## 3. Check-In & Kickoff (7:00 PM – 8:30 PM EAT)

- [ ] **7:00 PM:** Open venue doors; check in registered students on OrganizerHQ.
- [ ] **Team Formation:** Match collaborators by interests and skills; confirm numerical limits and any separate local award restrictions.
- [ ] **Opening Remarks:** Explain own-problem projects, the idea worksheet, optional inspiration, both prize categories, meaningful open AI, the 100-point human rubric and code of conduct. No primary track.
- [ ] **8:00 PM (Gemma Clinic):** Walk through Gemini API key creation, safe `.env` management, and local Ollama setup using the [Starter Kit]({{ site.baseurl }}/starter-kit/).

---

## 4. Overnight Hacking (Confirmed Build Period)

- [ ] **Mentorship Rounds:** Ensure technical mentors circulate every 60–90 minutes to unblock model setup and prompt architecture.
- [ ] **Hourly Announcements:** Maintain energy; announce remaining hours at 12:00 AM, 2:00 AM, and 4:00 AM.
- [ ] **Network Monitoring:** Assist with suitable local runtime or connectivity options; disclose fallbacks and do not promise local-only Gemma prize eligibility.

---

## 5. Submission & Preliminary Review (Confirmed Window)

- [ ] **Deadline Warnings:** Announce only timings verified against the saved live window.
- [ ] **Submission Reminder:** One team member submits once and selects every qualifying category:
  - **Best Open-Source AI Project** and/or **Best Use of Gemma 4**, as eligible.
  - Repository must be public with an OSI-approved `LICENSE` file.
  - README describes the problem, user, models, licences, setup, original contribution and test evidence; no track declaration.
- [ ] **Before cutoff:** Run administrative repository checker:
  ```bash
  python3 scripts/check_submission.py <repo-urls...>
  ```
- [ ] **Manual Review:** Resolve actual hygiene issues; a legacy missing-Gemma warning does not exclude other open models from the broad category.
- [ ] **Cutoff:** Verify the saved submissions and enforce only the reconciled, announced window.

---

## 6. Live Project Demos (Confirmed Session)

- [ ] **Judge Briefing:** Review 100-point rubric anchors (6 criteria, 0–5 scale, weighted conversion), time limits (2 min demo + 1 min Q&A), and mandatory conflict recusal rule.
- [ ] **Timekeeping:** Enforce strict 2-minute demonstration limit per team (no slide decks; live code only).
- [ ] **Independent Scoring:** Judges silently enter ratings (0–5) across the 6 criteria on individual score sheets without discussing marks.

---

## 7. Score Tabulation & Winner Marking (After Evaluation)

- [ ] **Audit Sheets:** Follow the [tabulation procedure]({{ site.baseurl }}/judging/#score-tabulation-process): ask original judges to correct missing fields or arithmetic; exclude conflicted, duplicate or uncorrected incomplete sheets with a reason. Arrange another independent evaluation if fewer than two valid sheets remain (three preferred).
- [ ] **Compute Averages:** Average valid judge totals privately; use the same sheets for criterion averages and tie-breakers. Compare full precision and round only displayed means to two decimals. No automated ranking software.
- [ ] **Apply Tie-Breakers (if needed):**
  1. Higher average Meaningful open-source/open-weight AI integration score (out of 20)
  2. Higher average Technical execution and working demonstration score (out of 25)
  3. Deliberation by the judging panel, with decision and rationale documented
- [ ] **Mark Official MLH Winner in OrganizerHQ:**
  1. Set **Announce Winners** toggle to **PRIVATE**.
  2. Filter by **Best Open-Source AI Project**, select winner, click **Mark Winner → Winner**, verify gold badge and **Winner saved**.
  3. Verify and mark **Best Use of Gemma 4** separately, following the confirmed multiple-category winner policy.
  4. Preview the public view, switch to **PUBLIC**, and verify the published gallery before announcing in the room.
- [ ] **Local Awards:** Confirm whether separate Top Three recognition/prizes remain before recording or announcing them.
- [ ] **Closing Ceremony:** Announce winners live; present awards and certificates.

---

## 8. Post-Event Tasks (Next 24–48 Hours)

- [ ] **High-Resolution Event Photos:** Group photo, hacking tables, demo presentations.
- [ ] **Confirm Public Gallery:** Ensure OrganizerHQ project gallery is public.
- [ ] **Submit MLH Event Report:** Complete the official post-event organizer form.
- [ ] **Itemized Receipts:** Process receipts for food/swag if claiming reimbursement.
- [ ] **Attendee Survey:** Send feedback form to participants.
