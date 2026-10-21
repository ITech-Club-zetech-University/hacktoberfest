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
- [ ] **OrganizerHQ Configuration Check:** Log in to OrganizerHQ and confirm whether **Best Open-Source AI Project** is the sole challenge or if an additional partner challenge is active.
- [ ] **Test Automated Checker:** Run `python3 -m unittest discover -s tests -v` on organizer workstation (ensure 43 tests pass).
- [ ] **Prepare Private Judge Sheet:** Import [`templates/judge-score-sheet.csv`](https://github.com/ITech-Club-zetech-University/hacktoberfest/blob/main/templates/judge-score-sheet.csv) into an access-controlled Google Sheet / Excel workbook.
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
- [ ] **7:15 PM (Team Formation):** Match solo hackers and pairs into **3–4 person teams** for local award eligibility.
- [ ] **7:30 PM (Opening Remarks):** Welcome attendees, explain the 5 preset tracks, review the 100-point rubric, and emphasize code of conduct.
- [ ] **8:00 PM (Gemma Clinic):** Walk through Gemini API key creation, safe `.env` management, and local Ollama setup using the [Starter Kit]({{ site.baseurl }}/starter-kit/).

---

## 4. Overnight Hacking (8:30 PM – 4:30 AM EAT)

- [ ] **Mentorship Rounds:** Ensure technical mentors circulate every 60–90 minutes to unblock model setup and prompt architecture.
- [ ] **Hourly Announcements:** Maintain energy; announce remaining hours at 12:00 AM, 2:00 AM, and 4:00 AM.
- [ ] **Network Monitoring:** If venue Wi-Fi slows down, guide teams to [Track 2: Gemma Off the Grid]({{ site.baseurl }}/challenges/02-edge-offline/) or provide USB drive packages.

---

## 5. Submission & Preliminary Review (4:30 AM – 5:00 AM EAT)

- [ ] **4:00 AM:** 1-hour submission warning announced to the room.
- [ ] **4:30 AM:** Submission window opens. Remind teams:
  - Submit repository URL on OrganizerHQ under **Best Open-Source AI Project**.
  - Repository must be public with an OSI-approved `LICENSE` file.
  - Project `README.md` must declare their **single primary iTech Club track**.
- [ ] **4:45 AM:** Run automated eligibility checker:
  ```bash
  python3 scripts/check_submission.py <repo-urls...>
  ```
- [ ] **4:50 AM:** Address any flagged `NEEDS MANUAL REVIEW` submissions (e.g. asking team to toggle repo public).
- [ ] **5:00 AM:** **Strict Submission Cutoff.** Lock submission queue.

---

## 6. Live Project Demos (5:00 AM – 5:45 AM EAT)

- [ ] **Judge Briefing:** Review 100-point rubric anchors, time limits (2 min demo + 1 min Q&A), and conflict recusal rule.
- [ ] **Timekeeping:** Enforce strict 2-minute demonstration limit per team (no slide decks; live code only).
- [ ] **Independent Scoring:** Judges silently enter marks across the 5 categories on individual score sheets.

---

## 7. Score Tabulation & Winner Marking (5:45 AM – 6:00 AM EAT)

- [ ] **Audit Sheets:** Ensure at least 2 completed score sheets per team; discard any incomplete sheets.
- [ ] **Compute Averages:** Tabulate arithmetic mean of completed judge totals.
- [ ] **Apply Tie-Breakers (if needed):**
  1. Use of Gemma (0–25)
  2. Technical execution (0–25)
  3. Problem & impact (0–20)
  4. Open-source quality (0–15)
- [ ] **Mark Official MLH Winner in OrganizerHQ:**
  1. Set **Announce Winners** toggle to **PRIVATE**.
  2. Filter by **Best Open-Source AI Project**, select winner, click **Mark Winner → Winner**, verify gold badge.
  3. If partner prize confirmed, mark partner winner.
  4. Switch toggle to **PUBLIC**.
- [ ] **Record Local Top 3 Overall:** Note 1st, 2nd, and 3rd Place Overall for iTech Club awards.
- [ ] **Closing Ceremony:** Announce winners live; present awards and certificates.

---

## 8. Post-Event Tasks (Next 24–48 Hours)

- [ ] **High-Resolution Event Photos:** Group photo, hacking tables, demo presentations.
- [ ] **Confirm Public Gallery:** Ensure OrganizerHQ project gallery is public.
- [ ] **Submit MLH Event Report:** Complete the official post-event organizer form.
- [ ] **Itemized Receipts:** Process receipts for food/swag if claiming reimbursement.
- [ ] **Attendee Survey:** Send feedback form to participants.
