---
title: Rules & Regulations
nav_order: 2
description: "Open-ended project rules, schedule confirmation, integrity and official MLH submission guidance."
---

# Rules & Regulations
{: .no_toc }

1. TOC
{: toc }

## Spirit of the event

Choose your own problem, primary user, domain and technical approach. There are **no mandatory project tracks**. Follow the [open-ended project brief]({{ site.baseurl }}/challenges/), the [MLH Standard Hackathon Rules](https://github.com/MLH/mlh-policies/blob/main/standard-hackathon-rules.md) and [Code of Conduct]({{ site.baseurl }}/code-of-conduct/).

Help others, build something useful and explain honestly what works. Optional inspiration is not an eligibility checklist.

## Who can take part

Register through the [official MLH event listing](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club) and check in at the venue for prize eligibility. Organisers, judges, mentors and sponsor representatives must not judge their own competitive work.

The listing's audience tags and local membership wording need organiser reconciliation. Confirm attendance eligibility and the venue with staff; the live listing names Ruiru Campus while earlier local material names Mang'u Campus.

## Team size & formation
{: #team-size-formation }

Solo hackers and teams are welcome to build. Ask organisers for team matching based on interests, skills and availability, not a required track.

**Organiser confirmation required:** the previous local awards policy required 3–4 members. The final team-size limits and any separate local award restrictions must be confirmed and announced for the new format; do not treat that old local rule as a universal MLH requirement.

List every contributor and their role. Every member should understand the application and be able to explain their own contribution. Do not split one codebase into duplicate submissions to gain extra entries.

## What you can and cannot bring in

- Project-specific work must take place during the **organiser-confirmed build period**. Disclose pre-existing work, upstream code and starter components.
- You may bring ideas and use permitted libraries, public packages, model weights and boilerplate with attribution and compatible licences.
- Do not present an existing personal project or someone else's work as an original event build.
- Stop feature work at the confirmed cutoff. The MLH standard rules distinguish small demo-breaking bug fixes from new features; disclose any permitted post-cutoff fix to judges.
- Do not commit credentials, private records or data you lack permission to use.

## AI coding tools vs. models in the product

AI coding assistants may help you develop. Include an **AI Tools Used** disclosure and explain your team's original contribution. Be able to explain the generated code.

Using Copilot, Gemini CLI or another coding tool alone does not qualify an ordinary application for an AI prize. The running product needs the relevant functional AI contribution.

For **Best Open-Source AI Project**, Gemma 4 or another suitable open-source/open-weight model may be used. For **Best Use of Gemma 4**, demonstrate meaningful Gemma 4 use and follow the [category's API/evidence requirements]({{ site.baseurl }}/challenges/#the-official-mlh-challenge).

## Code, model and data licences

- Publish application source under a suitable [OSI-approved licence](https://opensource.org/licenses), with a root licence file.
- Identify each exact model/version, its licence, runtime and any hosted-service terms. [Gemma 4 is Apache 2.0 licensed](https://ai.google.dev/gemma/docs/core/model_card_4); older Gemma generations may have different terms. Do not apply one generation's licence to all models.
- Attribute dependencies, datasets and upstream work. Public availability alone does not grant permission to redistribute data or code.
- Keep personal/sensitive data out of demos and public repositories; prefer permitted public or synthetic test data.

## The hacking timeline

**Checked against the public MLH listing on 30 October 2026:**

| Item | Current status |
|---|---|
| Event | Friday 30 October, **7:00 PM** → Saturday 31 October, **6:00 AM EAT** |
| Public submission close | Both official category pages display **31 October, 6:00 AM EAT** |
| Coding start/stop and setup allowances | **Awaiting Lead Organiser confirmation** |
| Submission opening, demos and judging | **Awaiting confirmation and reconciliation with the public close** |

The event lasts eleven hours, but that is not eleven confirmed coding hours. Earlier local instructions used a 5:00 AM cutoff and an eight-hour building session. **Those timings are superseded pending reconciliation and must not be used as current instructions.**

Organisers must verify the live OrganizerHQ window, confirm the build period and announce the same schedule to everyone. Do not silently close submissions an hour before the published deadline or promise a demo timetable that cannot fit. Consult the live category pages and confirmed staff announcement if the schedule changes.

Scope one working user journey for the actual time remaining, reserving time for testing, documentation, submission and rehearsal. The [idea framework]({{ site.baseurl }}/challenges/#develop-an-idea-quickly) helps cut scope.

## Submitting your project

1. Publish a **public GitHub repository** with a suitable code licence and useful README. Include the problem, primary user, original contribution, selected prize categories, exact models, dependency/data disclosures, setup, tests and limitations.
2. Test normal inputs, edge cases and at least one failure or uncertainty scenario. Prepare a working demo.
3. Use the [README template]({{ site.baseurl }}/templates/project-readme-template/), [submission checklist]({{ site.baseurl }}/templates/submission-checklist/) and [demo guide]({{ site.baseurl }}/templates/demo-script/).
4. One team member opens the event's [OrganizerHQ Challenges page](https://www.mlh.com/events/hacktoberfest-hack-day-nairobi-x-itech-club/challenges), chooses **Add Submission**, and supplies the project name, repository link, description, technologies and optional demo URL.
5. **Submit once and select every category the project qualifies for:** [Best Open-Source AI Project](https://www.mlh.com/events/hacktoberfest-hack-day-nairobi-x-itech-club/challenges/01a0d987-0c41-12ea-13ac-5b85755dc2f3) and/or [Best Use of Gemma 4](https://www.mlh.com/events/hacktoberfest-hack-day-nairobi-x-itech-club/challenges/01a03b87-be22-9180-5e2d-b3beeb66666d). No primary-track declaration is required.

The public category close is **6:00 AM EAT on 31 October**, subject to a verified, clearly announced organiser change. Keep the repository public after submission.

Organisers may run administrative repository checks, but they do not score or rank projects. A checker PASS does not guarantee category eligibility. Missing-Gemma warnings from the legacy checker do not exclude non-Gemma projects from the broad category; staff must review the actual model evidence. Network/rate-limit failures must never penalise a team.

## How winners are chosen & award structure

Appointed **human judges** independently evaluate projects using the [six-criterion, 100-point rubric]({{ site.baseurl }}/judging/#the-100-point-score-sheet). There is no automated scoring, ranking or leaderboard; pull-request counts and commit volume do not determine merit.

The two live MLH categories are awards, not fixed project prompts. Category eligibility is checked separately from common rubric scores. Open-source AI integration is assessed without favouring a particular provider or imposing archived technical baselines. Missing implementation evidence informs rubric scores; incomplete prototypes are not automatically disqualified.

Organisers must confirm whether any separate local Top Three awards remain, their prizes and whether a project may win both official categories. Do not infer prize inventory from partner marketing.

Judge sheets and provisional scores remain private. Compare unrounded averages and use the [published tie-breaking procedure]({{ site.baseurl }}/judging/#deterministic-tie-breaking-protocol).

<a id="disqualification-ownership"></a>

## Governance, disqualification & ownership
{: #governance-disqualification-ownership }

- **Conflicts:** Judges recuse from projects they helped build, closely mentored or have a personal interest in. At least two valid independent evaluations are required; three are preferred where capacity allows.
- **Disqualification:** Published eligibility/conduct failures, plagiarism, prohibited pre-building and deliberately misrepresented functionality are handled by the Lead Organiser, not an automated checker.
- **Appeals:** Raise administrative flags promptly before the confirmed deadline. The Lead Organiser, consulting the MLH representative where necessary, resolves disputes and records the rationale.
- **Ownership:** Teams retain ownership of their work. Open-source licensing grants reuse rights without transferring ownership to the organisers or sponsors.
