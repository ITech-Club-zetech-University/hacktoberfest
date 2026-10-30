---
title: Rules & Regulations
nav_order: 2
description: "Open-ended project rules, event timing, integrity and official MLH submission guidance."
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

The event takes place at **Zetech University, Ruiru Campus, Off Thika Road, Nairobi**. Follow the registration requirements on the official event listing. Contact the host through that listing if you need help with attendance or access.

## Team size & formation
{: #team-size-formation }

Solo hackers and teams are welcome to build. Ask organisers for team matching based on interests, skills and availability, not a required track.

Follow the team requirements provided at registration and the event briefing.

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

## Official event categories and participant evidence

Enter any of the **three categories** whose requirements your project meets. One project and repository may enter multiple categories; each is evaluated separately. Gemma 4 is required only for its own category, PrimeCloud deployment only for its own category, and DigitalOcean use is optional.

### Best Open-Source AI Project — DigitalOcean-supported

Build an original project with open-source/open-weight AI as an important functional component. Publish public GitHub source with an appropriate open-source code licence. Provide a README explaining what was built, how to run or try it, the exact model and its licence/terms link, key dependencies and original team contribution. Show the AI contribution in a working demo.

An agent skill must follow the [Agent Skills open standard](https://agentskills.io/specification). A harness must be original or contain meaningful changes to an existing open-source harness; renaming alone is insufficient. These are eligible forms, not the only permitted kinds of application or tool. **DigitalOcean is optional** for hosting, APIs, model workflows, infrastructure or supporting services, not an eligibility gate.

### Best Use of Gemma 4 — Gemma / Google DeepMind

Gemma 4 must meaningfully power the actual product, not just appear in dependencies, configuration or a README. Demonstrate its exact model ID and inference path. A Gemini model is not Gemma 4.

Text/image experiences, focused tools and rapid Gemini API prototyping are suggestions from the category description, not compulsory modalities or domains. A text-only tool can be appropriate. For this prize, follow MLH's published **Gemini API** guidance. Local inference remains a technical option for suitable projects, but does not by itself establish eligibility for this award.

Follow the [official category links, current model/API documentation and capability limits]({{ site.baseurl }}/challenges/#best-use-of-gemma-4). Variants differ in modality, hardware and performance. Check [service terms]({{ site.baseurl }}/starter-kit/#hosted-api-terms-check) as well as model licensing.

### Best Project Deployed on PrimeCloud — PrimeCloud

Build an original software application, publish its source in a public GitHub repository under an appropriate open-source licence, and deploy it using PrimeCloud. Provide a **working, publicly accessible deployment URL** and demonstrate the intended functionality. A dashboard screenshot alone is insufficient.

Explain how PrimeCloud was used, including deployment architecture/configuration. The README must include the technologies, setup and deployment instructions, team members and contributions. See the [complete requirements and confirmed prize]({{ site.baseurl }}/challenges/#best-project-deployed-on-primecloud).

**AI and Gemma 4 are not required.** An AI application can also enter the AI categories if independently eligible. Other categories do not require PrimeCloud deployment.

## Code, model and data licences

- **Open-weight is not automatically open-source:** downloadable weights may carry restrictions and do not establish that all model components are open source. Identify the actual model and link its licence/terms; the application licence does not relicense it.
- Publish application source under a suitable [OSI-approved licence](https://opensource.org/licenses), with a root licence file.
- Identify each exact model/version, its licence, runtime and any hosted-service terms. [Gemma 4 is Apache 2.0 licensed](https://ai.google.dev/gemma/docs/core/model_card_4); older Gemma generations may have different terms. Do not apply one generation's licence to all models.
- Attribute dependencies, datasets and upstream work. Public availability alone does not grant permission to redistribute data or code.
- Keep personal/sensitive data out of demos and public repositories; prefer permitted public or synthetic test data.

## The hacking timeline

| Item | Time |
|---|---|
| Event | Friday 30 October 2026, **7:00 PM** → Saturday 31 October, **6:00 AM EAT** |
| Published MLH category close | Saturday **31 October, 6:00 AM EAT**, on the Open-Source AI and Gemma 4 category pages |

Follow the event briefing for the coding period, workshops and your demo slot. Do not assume the entire event window is available for coding. Check the [official event listing](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club) and live category pages for updates; ask staff promptly if your submission window differs.

Scope one working user journey for the actual time remaining, reserving time for testing, documentation, submission and rehearsal. The [idea framework]({{ site.baseurl }}/challenges/#develop-an-idea-quickly) helps cut scope.

## Submitting your project

1. Publish a **public GitHub repository** with a suitable code licence and useful README. Include the problem, primary user, original contribution, selected prize categories, dependencies/data disclosures, setup, tests and limitations. Disclose exact models and their terms if used; include the live URL and deployment instructions if entering PrimeCloud.
2. Test normal inputs, edge cases and at least one failure or uncertainty scenario. Prepare a working demo.
3. Use the [README template]({{ site.baseurl }}/templates/project-readme-template/), [submission checklist]({{ site.baseurl }}/templates/submission-checklist/) and [demo guide]({{ site.baseurl }}/templates/demo-script/).
4. One team member follows the [submission guide]({{ site.baseurl }}/submission/) through the event's [Challenges area](https://www.mlh.com/events/hacktoberfest-hack-day-nairobi-x-itech-club/challenges). Sign in and check that the project is saved.
5. **Submit once and select every category the project qualifies for:** [Best Open-Source AI Project](https://www.mlh.com/events/hacktoberfest-hack-day-nairobi-x-itech-club/challenges/01a0d987-0c41-12ea-13ac-5b85755dc2f3), [Best Use of Gemma 4](https://www.mlh.com/events/hacktoberfest-hack-day-nairobi-x-itech-club/challenges/01a03b87-be22-9180-5e2d-b3beeb66666d) and/or [Best Project Deployed on PrimeCloud]({{ site.baseurl }}/challenges/#best-project-deployed-on-primecloud). No primary-track declaration is required. If a category is absent from the form, contact staff before the deadline.

The two published MLH category pages close at **6:00 AM EAT on 31 October**, subject to a verified, clearly announced organiser change. Follow the actual form and event briefing for the PrimeCloud submission window; ask staff before that close if its category or deadline is missing. Do not assume extra time. Keep the repository public after submission.

Provide evidence for each entered category in your repository and demo. An otherwise qualifying project using another suitable open model can enter Best Open-Source AI Project without using Gemma.

## How winners are chosen & award structure

Appointed **human judges** review the implementation, working demo and repository separately for each eligible category. See the [judging guide]({{ site.baseurl }}/judging/) for the proposed local 100-point category rubrics, rating scale and selection process. These are not official MLH-published scoring weights.

You are considered only for categories you enter and qualify for. An unmet condition in one category does not automatically exclude your project from another. Entering both does not require duplicate projects or repositories.

Any **iTech Club local overall awards** are separate from the three category awards. Follow the event's award announcement for local recognition and prize arrangements. Missing functionality affects the relevant criterion, not an unpublished fixed deduction.

Entering multiple categories does not guarantee multiple prizes; the applicable published award rules govern prize allocation.

Independent scores are consolidated separately for each category. Judge sheets and provisional scores remain private; final winners are announced after eligibility and results are validated.

<a id="disqualification-ownership"></a>

## Governance, disqualification & ownership
{: #governance-disqualification-ownership }

- **Conflicts:** Judges recuse from projects they helped build, closely mentored or have a personal interest in. At least two valid independent evaluations are required; three are preferred where capacity allows.
- **Disqualification:** Published eligibility/conduct failures, plagiarism, prohibited pre-building and deliberately misrepresented functionality may lead to disqualification.
- **Appeals:** Raise submission, eligibility or conduct concerns promptly with the Lead Organiser, who can involve the MLH representative where appropriate.
- **Ownership:** Teams retain ownership of their work. Open-source licensing grants reuse rights without transferring ownership to the organisers or sponsors.
