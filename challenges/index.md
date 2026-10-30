---
title: Build Your Own Open-Source AI Project
nav_order: 5
description: "Choose your own problem, develop an original solution, and build a focused open-source AI MVP."
---

# Build Your Own Open-Source AI Project
{: .no_toc }

**Identify a real problem. Imagine a better solution. Build it with open-source AI. Explore what Gemma 4 makes possible. Publish your work for others to use and improve.**
{: .fs-6 .fw-300 }

There are **no fixed project prompts, mandatory tracks or required application domains**. Choose your own problem, target users, domain, product concept and technical implementation. You can combine techniques or invent a different approach entirely.

1. TOC
{: toc }

## Prize categories are awards, not project prompts
{: #the-official-mlh-challenge }

The live MLH event lists two categories:

| Official category | What your project needs to demonstrate |
|---|---|
| **[Best Open-Source AI Project](https://www.mlh.com/events/hacktoberfest-hack-day-nairobi-x-itech-club/challenges/01a0d987-0c41-12ea-13ac-5b85755dc2f3)** — DigitalOcean-supported | An original project with open-source/open-weight AI central to a useful working solution; public GitHub source and a suitable open-source code licence. Using an AI coding assistant alone is not enough. Agent skills must follow the Agent Skills Open Standard; a model harness must be original or a meaningful extension. Those conditions apply only if you build that type of project. |
| **[Best Use of Gemma 4](https://www.mlh.com/events/hacktoberfest-hack-day-nairobi-x-itech-club/challenges/01a03b87-be22-9180-5e2d-b3beeb66666d)** — Gemma / Google DeepMind | Meaningful, working **Gemma 4** integration. Explain its role and show the actual model call in code and the demo. The [MLH partner winner guidance](https://hacktoberfest-handbook.mlh.com/hack-days-partner-modules/partner-challenge-google-gemma) requires Gemma use through the **Gemini API**; do not assume local-only inference or an older Gemma model qualifies. Ask organisers to resolve any exception against event onboarding. |

**One project can qualify for both categories. Submit once and select every category it qualifies for.** Permission to enter both does not establish permission to win both; organisers must confirm that policy. Do not submit duplicate forms for the same project.

**DigitalOcean is a supported resource, not a mandatory technology choice.** You may build locally or use suitable hosting elsewhere. Provider choice alone does not establish open-source AI eligibility. Check [optional deployment and pricing resources]({{ site.baseurl }}/resources/#optional-digitalocean-resources) before incurring costs; no universal free-credit entitlement is promised.

### Best Open-Source AI Project — DigitalOcean-supported
{: #best-open-source-ai-project }

The [official MLH requirements](https://hacktoberfest-handbook.mlh.com/fest-planning-guide/open-source-prize-categories) concern the project's actual contribution, not its application domain:

- Build an **original project** where open-source or open-weight AI is an **important functional part** of how it works. An unused model setting or an AI coding assistant used only during development is insufficient.
- Publish the project in a **public GitHub repository** with an appropriate open-source licence for the application code.
- If you submit an **agent skill**, follow the [Agent Skills open standard](https://agentskills.io/specification).
- If you submit a **model harness**, show an original implementation or meaningful changes to an existing open-source harness. Link upstream, describe your changes and preserve attribution; merely renaming a project is insufficient.

Skills and harnesses are eligible forms, **not the only possible forms**. Another useful AI application or tool is equally welcome.

Make the evidence easy to inspect: include a README explaining what you built, how to run or try it, the exact model/version, its role, key dependencies and your original contribution. **Link the model's actual licence or terms**, separately from your code licence. Demonstrate the AI contribution in a working user flow, and describe test results and limitations honestly.

**Open-weight and open-source are not interchangeable labels.** Available weights do not automatically mean every part of a model is open source or that there are no use restrictions. Check the actual model terms; an open-source code licence does not relicense its models, datasets or hosted services.

DigitalOcean can optionally support hosting, APIs, model workflows, AI infrastructure or other services. **You do not have to use it**, and neither using it nor paying for infrastructure earns extra points.

### Best Use of Gemma 4 — Gemma / Google DeepMind
{: #best-use-of-gemma-4 }

**Gemma 4 must do meaningful work in the actual product**, not merely appear in a README, dependency list or unused configuration. Show the exact model identifier, inference code/path and its contribution to the working demo.

The [live MLH description](https://www.mlh.com/events/hacktoberfest-hack-day-nairobi-x-itech-club/challenges/01a03b87-be22-9180-5e2d-b3beeb66666d) suggests text/image experiences where useful, focused tools for learning, creativity, productivity or communities, and rapid prototyping through the Gemini API. These are possibilities, **not mandatory domains or a requirement to build a multimodal project**. A well-designed text-only tool may be the right solution.

| Approach | What to verify |
|---|---|
| **Hosted Gemini API** | The [current official hosted guide](https://ai.google.dev/gemma/docs/core/gemma_on_gemini_api), rechecked **30 October 2026**, lists `gemma-4-31b-it` and `gemma-4-26b-a4b-it`. Check current model availability, account access, quotas and [API terms](https://ai.google.dev/gemini-api/terms) before publishing or running examples. A Gemini-branded model is not Gemma 4. |
| **Local inference** | Official routes include [Ollama](https://ai.google.dev/gemma/docs/integrations/ollama), [llama.cpp](https://ai.google.dev/gemma/docs/integrations/llamacpp), [Transformers](https://ai.google.dev/gemma/docs/core/huggingface_inference) and [LM Studio](https://ai.google.dev/gemma/docs/integrations/lmstudio). Check support for the exact checkpoint, quantisation and input type, and test actual memory and latency. Technical availability does not establish prize eligibility. |

The [MLH partner winner guidance](https://hacktoberfest-handbook.mlh.com/hack-days-partner-modules/partner-challenge-google-gemma) instructs organisers to confirm Gemma through the **Gemini API**. Follow that published route for this award unless MLH confirms different event-specific instructions. Do not promise local-only eligibility; ask organisers to resolve it against onboarding before selecting a winner.

Model variants differ. Consult the [current model card](https://ai.google.dev/gemma/docs/core/model_card_4), [model sizing/capabilities](https://ai.google.dev/gemma/docs/core), [image guide](https://ai.google.dev/gemma/docs/capabilities/vision/image) and [audio guide](https://ai.google.dev/gemma/docs/capabilities/audio). Native audio is listed for E2B, E4B and 12B, not every size; model capability also does not guarantee endpoint/runtime support. Larger models, extra modalities and expensive hardware are not inherently better for your use case.

Hosted-service terms are separate from the model licence. The current Gemini API terms include age/audience and permitted-use restrictions; unpaid services must not receive sensitive, confidential or personal information. Review the [starter kit's API terms check]({{ site.baseurl }}/starter-kit/#hosted-api-terms-check) before choosing that route.

### How the awards are judged

Appointed **human judges** review each entered category separately using [proposed category-specific 100-point rubrics]({{ site.baseurl }}/judging/#category-specific-evaluation-lenses). These category weights and the separate local overall rubric are **local judging guidance for organiser review, not an official MLH numerical rubric**. There is no AI judge, automated project scoring, automated score aggregation service, ranking service, leaderboard or automated winner selection.

The retained **iTech Club local Top Three awards** are separate from the two MLH categories; their continuation, eligibility and prize inventory need organiser confirmation. Entering both official categories requires neither duplicate projects nor duplicate repositories. Whether one team may receive both prizes remains an explicit organiser/MLH confirmation item.

## Develop an idea quickly

Use the following process with your team and a mentor. Write brief answers in the [problem statement worksheet]({{ site.baseurl }}/templates/problem-statement/); it is a planning aid, not a separate idea-approval requirement.

### Step 1 — Identify a real problem

- Who experiences the problem?
- What are they trying to achieve?
- What makes the current process difficult, slow, expensive, inaccessible, confusing or unreliable?
- How do they currently solve it?
- Can you talk to or observe a potential user during the event, with their consent?

Start with an observed need rather than a model feature looking for a use.

### Step 2 — Define the user and use case

Describe **one primary user and one specific use case**. Name the task, context and expected outcome.

“An AI platform for education” is too broad. “A first-year student checks their attempted solution against a worked example and receives one explanatory hint” is narrow enough to test. You may choose any domain; this example is not a prescribed project.

### Step 3 — Decide whether AI is appropriate

- What task specifically benefits from AI?
- Why is an open model useful here?
- Could a normal rule, form, database query or conventional application solve the problem more reliably and cheaply?
- What will the model do, and what must remain under human control?

Do not add a chatbot or LLM just to appear AI-powered. Use conventional software for deterministic tasks. If the idea does not need AI, narrow or reconsider the idea before entering an AI prize category. Define human review for uncertain or consequential outputs.

### Step 4 — Choose the model and architecture

For **Best Open-Source AI Project**, choose Gemma 4 or another suitable open-source/open-weight model. For **Best Use of Gemma 4**, use Gemma 4 meaningfully and follow its category requirements above.

| Decision | Trade-offs to check before committing |
|---|---|
| Local inference | Can work without internet after setup and keep inference on-device, but weights take time to download and require enough RAM/VRAM, disk and runtime support. Test latency on your actual hardware. Local execution alone does not prove complete privacy or partner-prize eligibility. |
| Hosted API | Reduces local compute needs but depends on connectivity, account access, quotas, service terms and possible charges. Check what data leaves the device and whether you have permission to send it. |
| Model capability | Verify the exact model and runtime support your inputs, output format, context size and language. Text, image, audio and tool support vary by model and endpoint. |
| Architecture | Choose the simplest flow that serves the user. Retrieval, agents, fine-tuning, mobile apps and web interfaces are options, not requirements. Limit tool permissions and validate model outputs. |
| Cost and feasibility | Measure response time, memory and API usage early. A larger model or paid deployment does not earn extra points. Keep a safe failure path for unavailable inference. |

The [starter kit]({{ site.baseurl }}/starter-kit/) explains hosted Gemma through the Gemini API versus local inference. **Gemini API is the hosting service; a proprietary Gemini model is not Gemma 4.**

### Step 5 — Scope the MVP

Choose:

- **One core user journey.**
- **One important AI capability.**
- **One working application flow**, from input through validation/model use to a useful output.
- **A small test dataset or realistic test scenarios**, using public, permitted or synthetic data.
- **One demonstrable outcome achievable in the organiser-confirmed hack period.**

Aim for a focused, demonstrable minimum viable product, not an unfinished commercial platform. Cut extra personas, dashboards, integrations and deployment work before cutting the core flow or testing.

### Step 6 — Build, test and document

Test and record:

1. Normal inputs with an expected useful result.
2. Edge cases such as empty, malformed, long or unsupported inputs.
3. **At least one failure or uncertainty scenario**, such as unavailable inference, insufficient source evidence or an ambiguous request.

Compare actual results with expected behaviour and explain failures honestly. **A model response appearing on screen does not by itself establish that the project works well.** Show whether the result helps the user, how errors surface and when a human should intervene. Do not label an unrun test as passed.

### Step 7 — Publish and submit

- Publish your work in a **public GitHub repository** with a suitable [OSI-approved code licence](https://opensource.org/licenses).
- Write a useful README: problem, primary user, original contribution, selected prize categories, architecture, exact model/version/runtime, model and dependency licences, data permissions, setup commands, tests and known limitations.
- Disclose AI coding tools separately from models used by the running application.
- Keep secrets and personal/sensitive data out of the repository. Provide placeholder configuration and reproducible setup instructions.
- Prepare a working demo and explain what is implemented versus planned. Use the [README template]({{ site.baseurl }}/templates/project-readme-template/), [submission checklist]({{ site.baseurl }}/templates/submission-checklist/) and [demo guide]({{ site.baseurl }}/templates/demo-script/).
- Register and check in. One team member submits on behalf of the team through the event's [OrganizerHQ Challenges page](https://www.mlh.com/events/hacktoberfest-hack-day-nairobi-x-itech-club/challenges). Choose **Add Submission**, provide the repository and project details, and select every eligible category.

## Time and feasibility

**Public listing checked: 30 October 2026.** The [official event listing](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club) gives **Friday 30 October, 7:00 PM → Saturday 31 October, 6:00 AM EAT**. Both live category pages display **31 October, 6:00 AM EAT** as the submission close.

{: .important }
> **Event duration is not a confirmed build window.** Earlier local instructions used a 5:00 AM deadline and an eight-hour building session. Those timings conflict with the live submission close and must not be used as current instructions. The Lead Organiser must confirm and announce the coding start/stop, submission window, demo schedule and any approved change to OrganizerHQ. Consult the [schedule status]({{ site.baseurl }}/rules/#the-hacking-timeline) before planning; do not assume that all eleven event hours are available for coding.

Once the remaining build time is confirmed, work backwards from it. Reserve time for tests, README/setup verification, publishing, submitting and demo rehearsal. Get a thin end-to-end flow running early, then improve reliability. If time is short, reduce features rather than promising a complete platform. Agree a fallback demonstration and disclose what it cannot prove.

## Need a starting point?

Explore [Project Inspiration]({{ site.baseurl }}/inspiration/) for optional examples across different domains. **Choose none, adapt one, combine ideas or bring a completely different problem.** These examples are not MLH-approved challenge tracks.
