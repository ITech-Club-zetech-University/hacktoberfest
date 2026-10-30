---
title: FAQ
nav_order: 8
description: "Answers about original ideas, models, teams, prize categories, human judging and submission."
---

# FAQ

## Do I have to select a predefined challenge?

**No.** Choose your own problem, users, domain, product concept and implementation. [Project Inspiration]({{ site.baseurl }}/inspiration/) is entirely optional.

## How do we turn an idea into a feasible project?

Use the [seven-step framework]({{ site.baseurl }}/challenges/#develop-an-idea-quickly) and [problem statement worksheet]({{ site.baseurl }}/templates/problem-statement/). Define one primary user, one use case, one important AI role and one working journey. Reserve time for tests, documentation and rehearsal within the confirmed build period.

## Do I need to be an AI expert?

No. Start small and ask mentors for help. The [starter kit]({{ site.baseurl }}/starter-kit/) covers Gemma setup; you may choose another suitable open model for the broad category.

## Can I come without a team?

Yes. Solo hackers and teams are welcome, and staff can help match collaborators. Follow the team requirements provided at registration and the event briefing. See [team formation]({{ site.baseurl }}/rules/#team-size-formation).

## Can one project enter both categories?

**Yes, if it meets both sets of requirements.** Submit once through the event's [Challenges area](https://www.mlh.com/events/hacktoberfest-hack-day-nairobi-x-itech-club/challenges), selecting every qualifying category. The two are **Best Open-Source AI Project** and **Best Use of Gemma 4**. They are awards, not technical tracks. Entering both does not guarantee multiple prizes.

## Must we use Gemma 4 or DigitalOcean?

For **Best Open-Source AI Project**, use Gemma 4 or another suitable open-source/open-weight model as an important functional component. **Best Use of Gemma 4** requires meaningful Gemma 4 use and its published conditions. **DigitalOcean is optional**, not mandatory hosting or a scoring advantage. See [both official category links and evidence requirements]({{ site.baseurl }}/challenges/#the-official-mlh-challenge).

## What makes a strong Best Open-Source AI Project entry?

Show an original, useful AI contribution in working software, public GitHub source with an appropriate code licence, and a README explaining what was built, how to run it, the exact model and model-licence link, dependencies and limitations. Agent skills must follow the open standard; harnesses need original implementation or meaningful changes, not just a rename. Other AI applications and tools are welcome too.

## Must a Gemma 4 entry be multimodal or use a prescribed domain?

No. The official text/image, focused-tool and rapid-prototyping examples are suggestions. A useful text-only tool can be appropriate. Gemma 4 must do actual product work, not merely appear in an unused configuration or README.

The [hosted guide](https://ai.google.dev/gemma/docs/core/gemma_on_gemini_api) currently lists `gemma-4-31b-it` and `gemma-4-26b-a4b-it`; check availability and service terms before use. Local routes include Ollama, llama.cpp, Transformers and LM Studio. Check the [model card and capability/runtime links]({{ site.baseurl }}/challenges/#best-use-of-gemma-4): modality, memory and performance vary, and local technical support does not establish prize eligibility.

## Does local Gemma inference qualify for the Gemma 4 prize?

Local inference is a valid technical option for suitable projects, but for this award follow MLH's published **Gemini API** guidance. Local inference alone, older Gemma versions or using Gemini CLI only to write code do not establish eligibility.

## Is Gemini API the same as a Gemini model?

No. The API can host **Gemma** models selected explicitly by model ID. A proprietary Gemini model is not Gemma 4. Document the exact model and runtime, not just the provider name.

## What are the timing and submission deadline?

The event runs **30 October 2026, 7:00 PM → 31 October, 6:00 AM EAT**, at **Zetech University, Ruiru Campus**. Both category pages display a **31 October, 6:00 AM EAT** submission close. Follow the event briefing for coding start/stop and demo slots; not all event hours are coding time. See [event timing]({{ site.baseurl }}/rules/#the-hacking-timeline).

## How are projects judged?

Appointed humans review your implementation, demo and repository. The [judging guide]({{ site.baseurl }}/judging/) explains the proposed local 100-point category rubrics, rating scale and selection process. These are **not official MLH-published scoring weights**. Each category is evaluated separately; a local overall score does not automatically win either category.

Any **iTech Club local awards** are separate from the MLH categories. Follow the event's award announcement for local recognition and prize arrangements.

## What if we do not qualify for one category?

Your project can still be considered for another category whose requirements it meets. You are not assigned a zero score for a category you did not enter. Use the same project and repository for all eligible categories, and ask staff if you need help understanding a requirement.

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

Test your chosen runtime early. Local models need downloaded weights and sufficient hardware; hosted APIs need connectivity, account access and quota. Prepare a safe failure path, not a hidden model substitution. Tell judges what failed and show your actual test evidence honestly.

## Which templates can we copy?

- [Project Proposal / Idea Canvas]({{ site.baseurl }}/templates/problem-statement/) — includes a plain Markdown download.
- [Project README Template]({{ site.baseurl }}/templates/project-readme-template/)
- [Submission Checklist]({{ site.baseurl }}/templates/submission-checklist/)
- [Demo Preparation Guide]({{ site.baseurl }}/templates/demo-script/) — use the organiser-confirmed time limit.

Follow the [OrganizerHQ submission guide]({{ site.baseurl }}/submission/) after preparing them. The templates do not replace the official form; authenticated host fields and timings still need organiser verification.
