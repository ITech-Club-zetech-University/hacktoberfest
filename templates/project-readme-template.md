---
title: Project README Template
nav_exclude: true
permalink: /templates/project-readme-template/
description: "Copy-and-fill README for an original, open-ended AI project."
---

# [Project Name]

Copy and adapt the sections below. Replace placeholders with actual facts; remove inapplicable examples. There is no required project track.

## Problem, user and solution

- **Problem:** [One specific task and its current difficulty.]
- **Primary user:** [Who needs the outcome and in what context?]
- **Current alternative:** [How the user solves it today.]
- **Why it matters:** [Evidence or clearly labelled assumptions.]
- **Solution:** For [specific user] who needs [specific outcome], we are building [solution]. The AI component will [specific role], helping the user to [measurable or observable benefit].

Use the full [problem statement worksheet]({{ site.baseurl }}/templates/problem-statement/) if helpful.

## Prize categories

- **Entered categories:** [Best Open-Source AI Project and/or Best Use of Gemma 4, only where eligible.]
- **Evidence of eligibility:** [Important functional open-source/open-weight AI contribution; if relevant, meaningful Gemma 4 use through the Gemini API, exact model ID and code location.]
- **Conditional project requirements:** [If an agent skill, standard conformance; if a harness, original implementation or meaningful upstream extension.]

Read the [official category links and requirements]({{ site.baseurl }}/challenges/#the-official-mlh-challenge). DigitalOcean is optional. Do not claim that local-only inference automatically meets the Gemma prize requirements.

## MVP and original contribution

- **Working user journey:** [One end-to-end flow implemented.]
- **Features completed:** [List working features, not roadmap items.]
- **Original event contribution:** [What the team built during the organiser-confirmed period.]
- **Pre-existing/upstream work:** [Links, licences and what was reused or changed.]
- **Remaining work:** [Clearly labelled limitations and future plans.]

## AI role and architecture

- **Why AI is appropriate:** [Why a rule, form or ordinary query is insufficient.]
- **Why an open model:** [The relevant benefit.]
- **Model task:** [Precise input, processing role and expected output.]
- **Human control:** [What the model cannot decide or execute unaided.]
- **Data flow:** [Where inputs go, what is stored, retrieval/tools if used.]
- **Trade-offs:** [Capability, latency, cost, connectivity, hardware and sensitivity.]

## Models, dependencies and licences

| Component | Exact name/version | Role and runtime/provider | Licence/terms and source |
|---|---|---|---|
| Primary model | [Actual model ID] | [Hosted/local and task] | [Actual model licence link] |
| Other model, if any | [Actual version] | [Embedding/safety/etc.] | [Licence] |
| Libraries/services | [Versions] | [Purpose] | [Licence/service terms] |
| Data | [Origin and date] | [Purpose] | [Permission and redistribution limits] |

Gemma 4 uses [Apache 2.0](https://ai.google.dev/gemma/docs/core/model_card_4); verify older generations and other models separately. Application code, model weights, datasets and hosted-service terms are distinct.

## Setup and running

Replace these placeholders with commands tested by your team:

1. [Prerequisites: runtime versions, hardware/disk and any account access.]
2. [Clone command and working directory.]
3. [Dependency installation command using the committed manifest/lockfile.]
4. [Configuration: placeholder-only `.env.example`, how variables are loaded, model download if applicable.]
5. [Launch command and expected URL or CLI invocation.]
6. [A realistic sample input and expected behaviour.]
7. [Test command and how to stop the application.]

Never commit a real key. For hosted Gemma, document `GEMINI_API_KEY` if used; for local inference, document the actual runtime/model and startup procedure. Do not require providers your project does not use.

## Test evidence and demonstration

| Scenario | Input / command | Expected behaviour | Actual result and limitations |
|---|---|---|---|
| Normal | [Realistic case] | [Observable useful outcome] | [Measured result; not assumed PASS] |
| Edge case | [Empty/malformed/unsupported input] | [Clear validation or safe boundary] | [Result] |
| Failure / uncertainty | [Unavailable model, ambiguous request or missing evidence] | [Explicit error/uncertainty and human next step] | [Result] |

- **Demo steps:** [Problem and user → live core flow → boundary/failure → repository.]
- **Code evidence:** [Where inference and validation occur.]
- **Known limitations:** [Accuracy, supported inputs, runtime, latency and unfinished work.]
- **Demo URL:** [Optional; does not replace the required working demonstration.]

## Safety and privacy

[Describe input/output validation, data permissions, retention, what leaves the device, human approval and tool boundaries where applicable. Do not equate offline inference with complete privacy or claim prompts eliminate hallucinations.]

For health-related information, use public/synthetic examples, authoritative sources and clear uncertainty. Do not claim unsupported diagnosis or treatment; refer clinical decisions to qualified professionals.

## Team contributions

| Contributor | GitHub username | Original work and responsibilities |
|---|---|---|
| [Name] | [Username] | [Contribution] |

Add a row for each actual contributor. Confirm team-size policy with organisers rather than treating this template as an eligibility rule.

## AI Tools Used

- **Coding assistants:** [Tools used, or None.]
- **How used:** [Short factual disclosure.]
- **Our contribution:** [Architecture, implementation, testing and decisions the team can explain.]

## Application licence

[Chosen OSI-approved licence and link to your project's licence file.] Attribute upstream components and retain required notices. The team retains ownership subject to these granted reuse rights.
