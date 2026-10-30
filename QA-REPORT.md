---
title: Final Human Judging QA Report
nav_exclude: true
search_exclude: true
permalink: /qa-report/
description: "Final review findings, validation evidence and organiser publication checks."
---

# Final Human Judging System QA Report

**Historical report:** This reviews the previous fixed-track format, not the current open-ended brief. Its track and schedule statements are superseded by the [current project brief](./challenges/index.md).

**Review date:** 30 October 2026  
**Baseline:** `0062ed8` (human-led judging implementation)  
**Disposition:** Documentation corrections completed; final local build validation in progress. Organiser confirmations below remain required. No commit, push or deployment was requested or performed.

## 1. Summary of changes

- Preserved the six-criterion, 100-point, human-led judging model.
- Clarified valid-sheet auditing, conflict recusal, missing-sheet recovery, equal judge weighting, full-precision comparisons and display rounding.
- Removed ambiguous track-specific score caps, automatic deductions and disqualification wording. The organiser explicitly chose to score incomplete prototypes under the rubric; published eligibility and conduct rules remain separate.
- Added six dedicated evidence/comments fields and a reusable blank row to the CSV. Labelled both sample rows as fictional and documented manual calculations, private copies and spreadsheet wrapping.
- Corrected the universal demo script from 2 minutes 45 seconds plus Q&A to exactly 2 minutes plus 1 minute Q&A.
- Aligned image/audio entries, read-only harnesses, alternative RAG embedding models and offline loopback/network evidence.
- Corrected MLH winner-recording order, official eligibility wording, conditional swag wording and the homepage's incorrect automatic-eligibility claim.
- Made organiser confirmation requirements explicit; removed an invalid website-relative license link from the participant README template.
- Repaired rubric, governance and team-formation anchor targets that the source-only validator accepted but the existing generated HTML did not contain. Retained the older rubric/governance aliases.

## 2. Files modified

| File | Purpose |
|---|---|
| `README.md` | Correct demo-template duration in repository inventory. |
| `index.md` | Remove the claim that local track participation automatically establishes official MLH eligibility. |
| `judging.md` | Clarify scoring, fairness, sheet completion, arithmetic, tie-breaking and announcement order; provide a direct CSV download. |
| `challenges/index.md` | Correct official AI requirements, skill/harness conditions and conditional physical-prize language. |
| `challenges/01-agent-skill.md` | Align baseline checks and score anchors; complete skill-name constraints. |
| `challenges/02-edge-offline.md` | Distinguish unmet checks from misrepresentation; clarify external adapters, loopback and measurable latency evidence. |
| `challenges/03-multimodal-assistant.md` | Make audio-only evidence and demonstrations equally acceptable. |
| `challenges/04-dev-harness.md` | Remove mock-tool contradiction and align read-only safety demonstrations and meaningful upstream contribution. |
| `challenges/05-rag-knowledge-companion.md` | Preserve the allowed choice of embedding model while requiring generative Gemma and real retrieval. |
| `rules.md` | Clarify submission cutoff versus closing time, incomplete prototypes and average-score tie-breakers; repair governance/team anchor targets. |
| `faq.md` | Align unfinished-project guidance and tie-breakers with the actual rubric. |
| `starter-kit.md` | Limit the Gemma-only requirement to local tracks, not the broader official MLH challenge. |
| `organizer-runbook.md` | Align private sheet preparation, validation, winner marking and outstanding HQ/capacity decisions. |
| `organizer-checklist.md` | Align operational checks with the judging guide and live MLH workflow. |
| `references/source-register.md` | Record current public-source verification and distinguish it from untested authenticated HQ settings and historical model claims. |
| `templates/demo-script.md` | Correct timing, matching skill-folder example and read-only safety option. |
| `templates/judge-score-sheet.csv` | Add criterion evidence fields, labelled fictional examples and a blank row. |
| `templates/submission-checklist.md` | Permit manual administrative review and remove any invented partner-category name or implication that a video replaces a live demo. |
| `templates/project-readme-template.md` | Align track evidence and remove the broken site-relative license link. |
| `QA-REPORT.md` | This final report; excluded from navigation, but available for organiser review. |

No application code, dependency manifests, theme settings or deployment workflow were intentionally changed.

## 3. Judging rubric and scoring validation

| Criterion | Weight |
|---|---:|
| Problem relevance and practical impact | 15 |
| Meaningful Gemma/open-weight AI integration | 20 |
| Technical execution and working demonstration | 25 |
| Originality and creativity | 15 |
| Responsible AI, privacy and safety | 10 |
| Open-source quality and reproducibility | 15 |
| **Total** | **100** |

**Passed:**

- All six criteria have a core question and detailed anchors for each integer rating from 0 through 5.
- Weighted points are `(rating / 5) * weight`; all 36 values in the published conversion table were checked against this formula.
- All 36 detailed anchors exist and their criterion weights match the conversion table.
- Enumerating all 46,656 possible six-criterion integer-rating combinations confirms totals remain within 0 through 100. All-zero and all-five ratings yield 0 and 100.
- Independent judge totals are averaged with equal weight. At least two valid, non-conflicted, distinct judges are required; three are preferred. Missing ratings are not zero, and another evaluation is required when fewer than two valid sheets remain.
- Worked aggregation examples: `(80 + 89 + 86) / 3 = 85.00`; `(80 + 89) / 2 = 84.50`.
- Ties use unrounded total means, then average Gemma points, then average Technical Execution points, then documented non-conflicted panel deliberation against the same rubric.
- No extra track points, hidden score caps, fixed deductions, presentation-only bonuses, commit-count or pull-request-count scoring rules remain in the reviewed documentation.

The local rubric is not presented as an official universal MLH scoring rubric. Official challenge eligibility is checked separately.

## 4. Judge score sheet validation

The [downloadable CSV]({{ site.baseurl }}/templates/judge-score-sheet.csv) has **29 columns**:

- Team, primary track, repository URL, judge ID and evaluation date.
- Six integer ratings and six corresponding weighted scores.
- Total out of 100.
- Strengths, improvement areas, general demonstration notes and qualitative recommendation.
- Explicit conflict-of-interest declaration.
- Six separate criterion-specific evidence/comments fields.

CSV parsing confirmed consistent column counts, two labelled fictional examples and a completely blank entry row. Both example totals were recalculated: **80** and **89**. Each example contains evidence for all six criteria.

**There are no formula cells.** This is a manual-entry CSV, not a preconfigured spreadsheet application. Judges use the conversion table; organisers verify arithmetic. Import instructions require deleting examples, copying the blank row, wrapping text and expanding row heights. Text fields have no template-imposed length limit. A native Excel/Google Sheets editing session was not exercised; organisers should rehearse the import and access controls before judging.

## 5. Challenge alignment findings

| Track | Minimum working implementation and demonstration | Alignment outcome |
|---|---|---|
| Agent Skill | Standard-compliant skill folder/frontmatter; Gemma performs the substantive task; agent or local driver runs a realistic example. | Clear baseline and evidence; vague additional score cap removed; no leading/trailing/consecutive hyphens in skill names. |
| Offline Edge | Cached local weights, actual local inference with external adapters disabled, reproducible launch, documented response latency and an edge case. | Loopback is permitted; process monitors alone no longer claim to prove zero external traffic. The under-30-second baseline remains an observable implementation check, not an automatic award gate. |
| Multimodal | Image or supported audio goes directly to Gemma; grounded response; supported formats/size limits and invalid-input handling. | Audio-only teams can demonstrate equivalent media evidence; no image-only requirement is imposed on them. |
| Dev Harness | Gemma selects a validated bounded tool, executes it against real fixture data and synthesises the returned result. | Mock-only actions do not satisfy the baseline. Confirmation before writes or enforced read-only/dry-run behaviour are equally valid safety designs. |
| RAG | Inspectable corpus, chunking/indexing, dynamic retrieval, generative Gemma, visible citations and absent-information handling. | EmbeddingGemma is not mandatory; the embedding model must be documented. Static prompt stuffing is not retrieval. |

All five descriptions contain minimum requirements, an explicit Gemma role, observable checks, a two-minute demonstration scenario, repository evidence and rubric-linked evaluation notes. They share the same scoring pool and weights. Optional stretch goals, hardware cost, model size and interface type are not separate points.

The homepage, challenge index and all five briefs, rules, FAQ, starter kit, judging guide, submission templates and organiser instructions were searched and reviewed. References to automated leaderboards/rankings are prohibitions, not instructions to run one. The submission checker remains administrative: it does not score projects, judge model performance, execute submissions or select winners.

## 6. MLH compliance and organiser confirmation

Public sources rechecked:

- [Official Best Open-Source AI Project requirements](https://hacktoberfest-handbook.mlh.com/fest-planning-guide/open-source-prize-categories).
- [Official submissions and winner-selection workflow](https://hacktoberfest-handbook.mlh.com/project-submissions-and-judging-for-hacktoberfest-hack-day).
- [MLH standard rules](https://github.com/MLH/mlh-policies/blob/main/standard-hackathon-rules.md).
- [Agent Skills specification](https://agentskills.io/specification).

Confirmed public guidance: one Best Open-Source AI Project winning team; important open-source/open-weight AI contribution; public licensed GitHub source; compliant agent skills; original or meaningfully extended harnesses; a DEV Badge for each winning member. Physical MLH+DEV swag is conditional on availability and onboarding instructions. The five local tracks and local Top Three Overall are not five official MLH prize categories.

**Authenticated organiser confirmation remains necessary:**

1. Confirm Best Open-Source AI Project appears for event `14735`. Contact MLH if absent; do not create a duplicate.
2. Verify whether MLH assigned any partner category. Use only its actual name, technology requirements, eligibility and prize instructions. Sponsorship is not proof of a prize category.
3. Save and verify the 31 October 2026 submission window, 4:30-5:00 AM EAT, including timezone and access to Add Submission/Manage Submissions.
4. Verify winner permissions and controls: PRIVATE while checking, Mark Winner > Winner, gold badge and Winner saved, preview public view, then PUBLIC and public-gallery verification **before the room announcement**.
5. Confirm DEV account collection, any swag availability and event-specific onboarding/eligibility instructions; local physical awards must be confirmed separately.

No authenticated HQ settings were changed or certified by this review. Earlier source-register claims about model IDs, modality support, SDK execution and model licensing were not re-certified; run a current Gemma smoke test and verify the actual checkpoint's terms before use.

## 7. Website build and deployment status

- Source QA initially passed and was rerun after corrections: no source-link, front-matter or heading-hierarchy errors.
- Existing full offline suite: **47 tests passed** before corrections; final verification is recorded below when complete.
- Initial `bundle exec jekyll build` could not run because the unversioned Bundler executable was absent. The available executable is `bundle3.2`; its first build attempt found missing Jekyll gems. Restoration of existing locked dependencies was attempted in session-local storage, without adding dependencies.
- Fresh Jekyll build, generated HTML/anchor checks, CSS/navigation checks and browser validation: **pending completion**.
- All 20 baseline tracked Markdown documents are preserved, including all pages present before the human-judging commit. No existing tracked page was deleted.
- The latest observed deployment workflow succeeded for baseline `0062ed8`: [GitHub Actions run](https://github.com/ITech-Club-zetech-University/hacktoberfest/actions/runs/41096900001). The published homepage responded **HTTP 200**.
- **The QA working-tree changes have not been committed, pushed or deployed.** A successful existing deployment is not validation of these unpublished changes.

## 8. Outstanding issues before publication

- Complete the fresh-build and rendered-site checks recorded above.
- Complete the authenticated OrganizerHQ/onboarding confirmations in section 6.
- Confirm final non-conflicted judge assignments, rehearse score-sheet entry and arithmetic, and ensure the private workbook does not expose one judge's scores to another before submission.
- Confirm demo capacity: 45 minutes permits at most 15 three-minute slots even before transitions/scoring time. Arrange calibrated parallel panels or publish an approved timing adjustment if required.
- Confirm local award inventory and on-site safety/reporting contacts.
- Smoke-test the actual Gemma inference path, modality support and runtime terms. This review does not certify external APIs, participant projects or hardware performance.

All source changes remain in the existing repository's working tree for organiser review. No new repository or ZIP archive was created.
