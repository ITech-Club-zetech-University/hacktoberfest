---
title: FAQ
nav_order: 8
description: "Answers about original ideas, models, teams, prize categories, human judging and submission."
---

# FAQ

## Do I have to select one of the former five challenges?

**No.** Choose your own problem, users, domain, product concept and implementation. The former briefs are historical archives, not active tracks. [Project Inspiration]({{ site.baseurl }}/inspiration/) is entirely optional.

## How do we turn an idea into a feasible project?

Use the [seven-step framework]({{ site.baseurl }}/challenges/#develop-an-idea-quickly) and [problem statement worksheet]({{ site.baseurl }}/templates/problem-statement/). Define one primary user, one use case, one important AI role and one working journey. Reserve time for tests, documentation and rehearsal within the confirmed build period.

## Do I need to be an AI expert?

No. Start small and ask mentors for help. The [starter kit]({{ site.baseurl }}/starter-kit/) covers Gemma setup; you may choose another suitable open model for the broad category.

## Can I come without a team?

Yes. Solo hackers and teams are welcome to build, and staff can help match collaborators. Confirm numerical limits and any separate local award restrictions with organisers; the previous 3–4-member local policy is not a universal MLH requirement. See [team formation]({{ site.baseurl }}/rules/#team-size-formation).

## Can one project enter both categories?

**Yes, if it meets both sets of requirements.** Submit once through the event's [OrganizerHQ Challenges page](https://www.mlh.com/events/hacktoberfest-hack-day-nairobi-x-itech-club/challenges), selecting every qualifying category. The two are **Best Open-Source AI Project** and **Best Use of Gemma 4**. They are awards, not technical tracks. Whether one project may **win** both needs organiser confirmation.

## Must we use Gemma 4 or DigitalOcean?

For **Best Open-Source AI Project**, use Gemma 4 or another suitable open-source/open-weight model as an important functional component. **Best Use of Gemma 4** requires meaningful Gemma 4 use and its published conditions. **DigitalOcean is optional**, not mandatory hosting or a scoring advantage. See [both official category links and evidence requirements]({{ site.baseurl }}/challenges/#the-official-mlh-challenge).

## What makes a strong Best Open-Source AI Project entry?

Show an original, useful AI contribution in working software, public GitHub source with an appropriate code licence, and a README explaining what was built, how to run it, the exact model and model-licence link, dependencies and limitations. Agent skills must follow the open standard; harnesses need original implementation or meaningful changes, not just a rename. Other AI applications and tools are welcome too.

## Must a Gemma 4 entry be multimodal or use a prescribed domain?

No. The official text/image, focused-tool and rapid-prototyping examples are suggestions. A useful text-only tool can be appropriate. Gemma 4 must do actual product work, not merely appear in an unused configuration or README.

The [hosted guide](https://ai.google.dev/gemma/docs/core/gemma_on_gemini_api) currently lists `gemma-4-31b-it` and `gemma-4-26b-a4b-it`; check availability and service terms before use. Local routes include Ollama, llama.cpp, Transformers and LM Studio. Check the [model card and capability/runtime links]({{ site.baseurl }}/challenges/#best-use-of-gemma-4): modality, memory and performance vary, and local technical support does not establish prize eligibility.

## Does local Gemma inference qualify for the Gemma 4 prize?

Do not assume so. Local inference is a valid technical option for suitable projects, but MLH's Gemma partner winner guidance calls for Gemma through the **Gemini API**. Confirm any exception with organisers against onboarding. Older Gemma versions or using Gemini CLI only to write code do not prove Gemma 4 integration.

## Is Gemini API the same as a Gemini model?

No. The API can host **Gemma** models selected explicitly by model ID. A proprietary Gemini model is not Gemma 4. Document the exact model and runtime, not just the provider name.

## What are the timing and submission deadline?

The public event runs **30 October, 7:00 PM → 31 October, 6:00 AM EAT**. Both category pages display a **31 October, 6:00 AM EAT** submission close. The build window and demo schedule still need organiser reconciliation with earlier local timings. Do not assume an eight-hour build or the former 5:00 AM cutoff. See [schedule status]({{ site.baseurl }}/rules/#the-hacking-timeline).

## How are projects judged?

Appointed humans review each eligible entered category separately using [proposed category-specific lenses]({{ site.baseurl }}/judging/#category-specific-evaluation-lenses), subject to organiser approval. These are local guidance, **not an official MLH numerical rubric**. A local overall score does not automatically win either category.

The existing 100-point rubric and tie-breakers belong to **iTech Club local overall assessment**, separate from the two MLH awards. Local Top Three continuation and prizes need confirmation, not silent removal or new promises. There is no AI judge, automated scoring, score aggregation service, leaderboard or automated winner selection.

## What if we do not qualify for one category?

Judges record **Eligible**, **Pending**, **Ineligible** or **Not Entered** separately for each award. Resolve pending evidence with organisers. A project can remain eligible for another category; unentered/ineligible categories are not zero scores. The [judge sheet]({{ site.baseurl }}/templates/judge-score-sheet.csv) records actual considered categories and separate evidence/notes. No duplicate project or repository is needed for dual entry.

## What if our project is unfinished?

Submit an honest prototype and demonstrate what works. Missing or failed checks inform the relevant rubric criteria, not automatic fixed deductions or hidden gates. Official category winners must still meet category requirements. Cut scope to a useful MVP instead of presenting roadmap features as completed.

## What should we test?

Normal inputs, edge cases and **at least one failure or uncertainty scenario**. Compare outputs with expected results, document actual outcomes and show human control where needed. A response on screen is not proof of correctness.

## What licence and disclosures do we need?

Use a suitable OSI-approved application-code licence and document exact models, their licences, dependencies and data permissions. [Gemma 4 uses Apache 2.0](https://ai.google.dev/gemma/docs/core/model_card_4); older models can have different terms. Disclose AI coding tools separately and explain your team's original contribution. Never publish credentials or private data.

Open-weight and open-source are not interchangeable: available weights do not automatically mean every model component is open source or unrestricted. Hosted API terms are separate too; see the [age/audience, data and permitted-use check]({{ site.baseurl }}/starter-kit/#hosted-api-terms-check).

## Are judge notes public?

No. Completed sheets, individual marks, conflicts and provisional results remain in access-controlled organiser storage. Only validated winners and appropriate constructive feedback are announced.

## What if connectivity or an API fails?

Test your chosen runtime early. Local models need downloaded weights and sufficient hardware; hosted APIs need connectivity, account access and quota. Prepare a safe failure path, not a hidden model substitution. A network failure in the administrative checker must not penalise a team.

## Which templates can we copy?

- [Project Proposal / Idea Canvas]({{ site.baseurl }}/templates/problem-statement/) — includes a plain Markdown download.
- [Project README Template]({{ site.baseurl }}/templates/project-readme-template/)
- [Submission Checklist]({{ site.baseurl }}/templates/submission-checklist/)
- [Demo Preparation Guide]({{ site.baseurl }}/templates/demo-script/) — use the organiser-confirmed time limit.

Follow the [OrganizerHQ submission guide]({{ site.baseurl }}/submission/) after preparing them. The templates do not replace the official form; authenticated host fields and timings still need organiser verification.
