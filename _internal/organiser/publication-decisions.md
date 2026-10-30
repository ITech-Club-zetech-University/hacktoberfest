# Organiser publication decisions

Repository-only maintenance record, excluded from Jekyll. This public repository
is not confidential storage. Never add completed scores, attendee records,
incident details, credentials or private contact information.

## Confirmed public facts

- Official event listing: 30 October 2026, 7:00 PM to 31 October, 6:00 AM EAT,
  at Zetech University, Ruiru Campus, Off Thika Road, Nairobi.
- The two public MLH category pages display a 31 October, 6:00 AM EAT close.
- The three event categories are Best Open-Source AI Project, Best Use of Gemma 4,
  and Best Project Deployed on PrimeCloud. PrimeCloud is confirmed by the event
  organiser's update request, not by an inspected MLH/HQ category setting.
- One project may enter every category for which it qualifies.
- DigitalOcean is optional. Gemma 4 is required only for its own category.
  PrimeCloud deployment is required only for its category; AI is not required.
- Organiser-supplied PrimeCloud prize: **PrimeCloud Production Plan – 3 Months**.
  The winning developer will receive three months of PrimeCloud Production,
  with access to the standard Production plan features and allowances.

Sources: [event](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club),
[open-source AI category](https://www.mlh.com/events/hacktoberfest-hack-day-nairobi-x-itech-club/challenges/01a0d987-0c41-12ea-13ac-5b85755dc2f3),
[Gemma category](https://www.mlh.com/events/hacktoberfest-hack-day-nairobi-x-itech-club/challenges/01a03b87-be22-9180-5e2d-b3beeb66666d).
Public sources checked 30 October 2026; authenticated HQ was not inspected.

## Decisions requiring host/MLH approval

- Attendance restrictions and numerical team limits.
- Coding start/stop, workshops, submission opening and demo/Q&A slots.
- Any discrepancy between local communications and the official venue/window.
- Approval of all three proposed organiser category rubrics, averaging and tie rules
  against the applicable sponsor/MLH requirements.
  Do not treat removing editorial notes from public copy as approval.
- Continued iTech Club local Top Three recognition, eligibility and prize
  inventory. Retain the existing local rubric separately; do not silently cancel
  or newly promise awards.
- Whether a team may receive multiple category prizes. Entry permission does not answer
  the winner-allocation question.
- Authenticated OrganizerHQ fields, category settings, registration/check-in
  requirements and submission window/timezone.
- Any exception to published MLH Gemma Gemini API winner guidance.
- Local safety/reporting staffing and enforcement arrangements.
- Add/verify **Best Project Deployed on PrimeCloud** in authenticated OrganizerHQ,
  with the exact title, sponsor, requirements, required live URL, submission
  window/timezone and winner controls. Contact MLH for the authorised setup;
  changing this website does not create an HQ category. Do not invent its ID.
- Confirm PrimeCloud prize redemption/activation, account eligibility, start
  date, expiry and post-prize billing/cancellation with the sponsor. No monetary
  value, credits or extra infrastructure allowances have been promised.
- Obtain supported runtime/version guidance and exact repository connection,
  secrets, build/start/public routing, persistence and monitoring instructions.
  The public quickstart is high-level and its CLI example is labelled illustrative;
  no authenticated deployment or executable CLI workflow was verified.

Resolve these in the relevant official configuration and participant briefing.
Do not invent limits, exceptions, prize terms or grace periods.

## Judging materials

- [Category score sheet](./category-score-sheet.md): proposed category-specific
  numerical blocks for the two AI categories. Approve before use.
- [PrimeCloud score sheet](./primecloud-score-sheet.md): five criteria totalling
  100, independent evidence/comments and mandatory live deployment verification.
  Use separately; do not extend the local CSV into a combined three-category score.
- [Retained local CSV](./judge-score-sheet.csv): 37 columns, three fictional
  examples and one blank row. Its numerical weights apply only to local overall
  assessment, not either MLH category.
- Keep independent reviews and manual consolidation. No automated leaderboard,
  scoring/aggregation service or winner-selection process is introduced.
- Completed records belong in access-controlled organiser storage, not Git.

## PrimeCloud source scope

The organiser identified [primecloud.cloud](https://primecloud.cloud).
Its [documentation](https://primecloud.cloud/docs) and rendered
[quickstart](https://primecloud.cloud/docs/quickstart) describe account/workspace,
application/services, Console or CLI deployment and verification. The
[features](https://primecloud.cloud/features) page describes Git/container/source
deployment and resource monitoring, not a runtime/version compatibility matrix.
[Signup](https://primecloud.cloud/signup), [pricing](https://primecloud.cloud/pricing)
and [support](https://primecloud.cloud/support) are official linked destinations.
These sources do not independently confirm hackathon prize redemption terms.

## Publication boundary

- The five full historical briefs are preserved under
  [archives/challenges](../archives/challenges/) and are not published.
- `_internal/` is explicitly excluded, in addition to Jekyll's normal underscore
  directory handling.
- Raw participant Markdown downloads remain free of front matter and Liquid.
  They must not become extra navigation/search pages.
- Use the existing GitHub Actions workflow as the single publishing authority,
  with Pages configured to **GitHub Actions**, not branch-based legacy builds.
- Do not deploy the old root-owned `_site` directory. A fresh workflow build
  creates the publication artifact.
