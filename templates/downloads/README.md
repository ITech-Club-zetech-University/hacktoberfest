# [Project Name]

[One-sentence description of the working project and its benefit.]

Replace bracketed prompts with facts, remove inapplicable sections, and do not
describe unbuilt features or unrun tests as completed.

## Problem and intended users

- **Problem:** [One specific task and its current difficulty.]
- **Primary user:** [Who needs the outcome and in what context?]
- **Current alternative:** [How the user solves it today.]
- **Why it matters:** [Evidence or clearly labelled assumptions.]
- **Solution:** For [specific user] who needs [specific outcome], we are building
  [solution], helping the user to [measurable or observable benefit].
  [If using AI, explain its specific role.]

## Features and screenshots

- **Working features:** [What a user can actually do now.]
- **Screenshots:** [Add screenshots and captions using permitted, non-sensitive data.]
- **Original event contribution:** [What the team built during the confirmed hack period.]
- **Pre-existing/upstream work:** [Sources, licences, reuse and meaningful changes.]
- **Unfinished work:** [Clearly labelled roadmap, not a feature claim.]

## Architecture and data flow

[Describe or draw the actual components and where inputs, model requests,
outputs and stored data travel. Identify anything sent to an external provider.
Document retrieval, databases and tools only if used.]

- **AI role and importance (if used):** [The specific model task and why a rule or ordinary query is insufficient.]
- **Open-model choice (if used):** [Why this open-source/open-weight model fits the problem.]
- **Human control:** [Decisions/actions the model cannot take without review.]
- **Trade-offs:** [Capability, latency, cost, connectivity, hardware and data sensitivity.]

## Models, dependencies and terms

| Component | Exact name, variant and version | Provider/runtime and role | Licence/terms and source URL |
|---|---|---|---|
| Primary model, if used | [Actual model ID and variant] | [Hosted/local, provider/runtime and task] | [Model licence URL and hosted terms if applicable] |
| Other model, if used | [Actual ID/version] | [Embedding/safety/etc.] | [Licence/terms URL] |
| Libraries/services | [Names and pinned versions] | [Purpose] | [Dependency licences and service terms] |

- **Technology stack:** [Languages, frameworks, runtimes and relevant hardware.]
- **Dependency manifests:** [Locations of manifests/lockfiles and important dependencies.]

Application code, model weights, datasets and hosted-service terms are distinct.
Available weights alone do not establish that a model is open source.

## Gemma 4 implementation (if applicable)

- **Exact Gemma 4 model and variant:** [Actual identifier, not a Gemini model name.]
- **Inference route:** [Provider/API or local runtime and configuration.]
- **Code location:** [Where the real model call and response handling occur.]
- **Meaningful role:** [What Gemma 4 does in the working user journey and why it fits.]
- **Capabilities used:** [Only modalities supported by the actual variant and needed by the project.]
- **Terms:** [Model licence URL and any hosted API terms.]

## Intended prize categories

- **Categories:** [Best Open-Source AI Project, Best Use of Gemma 4 and/or Best Project Deployed on PrimeCloud, only where eligible.]
- **Open-source AI contribution:** [Important functional AI role and original contribution, if entering that category.]
- **Gemma evidence:** [Actual Gemma 4 integration and published category conditions, if entering that category.]
- **PrimeCloud evidence:** [Working public deployment URL, actual platform use, architecture and deployment instructions, if entering that category.]
- **Conditional requirements:** [Agent Skills standard conformance if a skill; original implementation or meaningful changes if a harness.]

Entering categories in this README does not complete official submission.
One project may enter multiple categories when eligible; entry does not
guarantee permission to receive multiple prizes. DigitalOcean is optional.
Gemma 4 is required only for its category. PrimeCloud deployment is required
only for its category, which does not require AI. If a category is missing
from the submission form, contact staff before the deadline.

## PrimeCloud deployment (if entering)

- **Public deployment URL:** [Working public URL, not a dashboard link.]
- **PrimeCloud usage:** [How the platform genuinely deploys/runs this application.]
- **Technologies and frameworks:** [Actual stack, versions and services used.]
- **Deployment architecture:** [Components, connections, storage and public request path.]
- **Deployment configuration:** [Actual non-secret build/start/runtime configuration.]
- **Environment variables:** [Names and purposes only; safe placeholders, never credentials.]
- **Setup and deployment steps:** [Steps actually used, including prerequisites and verification.]
- **Live demonstration:** [Safe user journey or sample API request and expected result.]
- **Operational limits:** [Known issues, errors, persistence and realistic scaling constraints.]
- **Team contributions:** [Who implemented the application and deployment.]

A deployment-dashboard screenshot alone is not evidence of working software.
Keep configuration secrets private; do not claim unrun deployment steps as verified.

## Setup and configuration

Replace these prompts with commands tested for this project's actual stack.
Do not require every language, database or inference runtime.

1. [Prerequisites: exact runtime versions, hardware/disk and account access.]
2. [Clone command and working directory.]
3. [Dependency installation command using committed manifests/lockfiles.]
4. [Copy the placeholder-only .env.example to a private .env if needed.]
5. [Explain how configuration is loaded and how to download/start a local model if used.]

### Environment variables

Replace these placeholder names with only the variables your application uses.
List names and safe placeholder values, never real credentials.

| Variable name | Purpose | Required? | Placeholder value |
|---|---|---|---|
| [ENV_VAR_NAME] | [Purpose, including backend-only secret handling if relevant] | [Yes/No] | [Non-secret placeholder] |

Commit only placeholder configuration. Ignore private `.env` files and keep
API secrets on the backend, never in frontend bundles. Document actual
provider/runtime setup rather than requiring providers the project does not use.

## Run and test

- **Start:** [Tested command and expected URL or CLI invocation.]
- **Try it:** [One realistic input and expected behaviour.]
- **Tests:** [Test command, evaluation data location and how to repeat AI checks.]
- **Stop:** [How to stop the application and any local services.]

| Scenario | Input / command | Expected behaviour | Actual result and limitations |
|---|---|---|---|
| Normal | [Realistic case] | [Observable useful outcome] | [Observed result, not assumed PASS] |
| Edge case | [Empty/malformed/unsupported input] | [Validation or safe boundary] | [Observed result] |
| Failure / uncertainty | [Unavailable model, ambiguous request or missing evidence] | [Explicit error/uncertainty and human next step] | [Observed result] |

## Demo

- **Demo URL:** [Public URL, or Not available.]
- **Video URL:** [Optional recording URL, or Not available.]
- **Demo steps:** [Problem/user, live journey, any actual model call, normal case, limitation and code; show the public deployment if entering PrimeCloud.]

Label recordings, fallbacks and edited examples honestly. Follow the
organiser-confirmed presentation format and time limit.

## Data sources and licences

| Dataset/source | Origin and access URL | Permission/licence | Use, storage and redistribution limits |
|---|---|---|---|
| [Public, synthetic or consented data] | [Source and date] | [Actual permission/licence] | [Relevant restrictions] |

## Known limitations, safety and privacy

[Describe supported inputs, accuracy limits, unfinished work, model/network
failures, input validation, uncertainty, data minimisation and retention.
Explain what leaves the device, human approval and tool permissions where used.
Do not publish private data or claim that prompts eliminate hallucinations.]

[For high-impact use cases, explain oversight and safeguards. Do not claim
unsupported medical diagnosis, treatment or other professional determinations.]

## Team contributions

| Contributor | GitHub username | Original work and responsibilities |
|---|---|---|
| [Name] | [Username] | [Contribution] |

- **AI coding tools used:** [Tools or None; describe their role and the team's own decisions.]

## Run, contribute and improve

[Explain how another developer can reproduce the core flow, run tests,
report a problem or contribute. Link to contribution instructions if present.]

## Project source-code licence

[Chosen OSI-approved licence and location of the LICENSE file.]
Retain required upstream notices. The code licence does not replace model,
dataset or hosted-service terms.

## Acknowledgements

[Credit upstream projects, models, datasets, documentation, mentors and other
contributors as appropriate, with source URLs and required attribution.]
