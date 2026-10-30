---
title: Starter Kit
nav_order: 3
description: "A practical, optional-stack launchpad for Gemma 4 and original open-source AI projects."
---

# Gemma 4 & Open-Source AI Starter Kit
{: .no_toc }

Start with your [problem, primary user and focused MVP]({{ site.baseurl }}/challenges/). **Install only what your chosen project needs.** You do not need every language, framework, database or inference runtime on this page.

1. TOC
{: toc }

## 1. Prerequisites and developer setup

- [ ] A laptop, power supply and reliable internet where available. Plan large downloads ahead; local inference still needs initial downloads.
- [ ] Git and a GitHub account for publishing the project.
- [ ] VS Code or another familiar code editor.
- [ ] **One familiar language/runtime.** Install Python only for a Python stack, Node.js only for a JavaScript/TypeScript stack, or your chosen alternative.
- [ ] A browser and terminal.
- [ ] A way to run and test the core flow locally before deployment.
- [ ] Backend environment-variable handling for secrets, a placeholder `.env.example`, and `.env` excluded from Git.

Run only checks relevant to your stack:

```bash
git --version
python3 --version
node --version
```

The Python hosted example below uses **Python 3.11+**; the JavaScript example uses **Node.js 22+**. These are example requirements, not event-wide requirements. The Python Ollama example uses the standard library only.

## 2. Choose an AI execution path

| Path | Good starting point when... | Trade-offs |
|---|---|---|
| **A: Hosted Gemma 4** | You want a quick model connection without local model compute | Internet, provider/account eligibility, API access, quota, latency, data handling and possible cost |
| **B: Local Gemma 4 with Ollama** | You need local experimentation or operation without internet after setup | Large initial downloads, runtime support, RAM/VRAM, disk, quantisation trade-offs and measured performance |
| **Another suitable open model/runtime** | It fits your problem better | Verify its licence, capabilities, documentation and reproducibility |

**Gemma is not Gemini.** The **Gemini API** is a hosting service that can serve explicitly selected **Gemma 4** models; a Gemini-branded model is not Gemma 4. Coding with Gemini CLI alone does not establish product integration.

Another suitable open-source/open-weight model is welcome for **Best Open-Source AI Project**. For **Best Use of Gemma 4**, demonstrate meaningful Gemma 4 use and follow [MLH's published category/API conditions]({{ site.baseurl }}/challenges/#best-use-of-gemma-4). Local technical support does not automatically establish partner-prize eligibility.

## Path A — Hosted Gemma 4 API
{: #option-a--hosted-gemma-via-the-gemini-api }

<a id="option-a"></a>

Start with the [MLH Gemma resources](https://mlh.link/gemma), [MLH quickstart](https://mlh.link/gemma-quickstart), [MLH beginner guide](https://mlh.link/gemma-beginnerguide) and [official hosted Gemma guide](https://ai.google.dev/gemma/docs/core/gemma_on_gemini_api).

**Guide rechecked 30 October 2026:** supported hosted IDs are **`gemma-4-31b-it`** and **`gemma-4-26b-a4b-it`**. Examples use the latter. Re-check the live guide and your account's availability before running or publishing code; do not substitute a Gemini model silently.

### Hosted API terms check

Review the current [Gemini API terms](https://ai.google.dev/gemini-api/terms), [available regions](https://ai.google.dev/gemini-api/docs/available-regions), [rate limits](https://ai.google.dev/gemini-api/docs/rate-limits) and [pricing](https://ai.google.dev/gemini-api/docs/pricing):

- API users must be **18+**, and the terms restrict clients directed towards or likely to be accessed by under-18s. This is a service restriction, **not an event attendance rule**.
- Do not send sensitive, confidential or personal information to unpaid services. Review retention/data use, permitted uses, region and account conditions.
- The terms prohibit clinical practice and medical advice. A disclaimer or model licence does not override hosted-service restrictions.
- Quotas and model access can vary. **No fixed quota, free usage or credit amount is promised.** Requests require network connectivity and may incur costs.

If the hosted route is unsuitable, explore a permitted local/open-model path for the broad category and ask organisers about prize eligibility rather than bypassing service terms.

### Configure an API key safely

1. Open [Google AI Studio API keys](https://aistudio.google.com/apikey), sign in with an eligible account, and create/configure a key through the provider's instructions. Review [key security guidance](https://ai.google.dev/gemini-api/docs/api-key).
2. Keep the key **on your backend or in a server-side/terminal environment variable**. Never put it in a browser bundle, mobile application package, public notebook output, screenshot or Git commit. Frontend-prefixed public variables are not secret storage.
3. Use the files in the repository's [example folder](https://github.com/ITech-Club-zetech-University/hacktoberfest/tree/main/examples/gemma), or download the scripts/manifests linked below into your own project. From that folder, copy `.env.example` to `.env` and edit the private file in your editor:

   ```bash
   cp .env.example .env
   ```

`.env.example` contains **placeholders only**:

```dotenv
GEMINI_API_KEY=replace_with_your_api_key
```

Merge these ignore rules into your project's `.gitignore` rather than overwriting existing rules:

```gitignore
.env
.env.*
!.env.example
.venv/
node_modules/
__pycache__/
*.pyc
```

Verify before committing:

```bash
git check-ignore .env
```

It should identify `.env` as ignored. If it does not, fix your ignore rules first. If a key has already been published, revoke/rotate it immediately in AI Studio; deleting the latest file alone does not remove a leaked key from history.

### Python: text and optional image input

Use the **official `google-genai` SDK**, imported as `from google import genai`, not the legacy `google-generativeai` package. The [example requirements]({{ site.baseurl }}/examples/gemma/requirements.txt) pin the checked SDK version and environment loader.

From `examples/gemma`, create an isolated environment and install only this Python path's dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python hosted.py
```

On Windows, use `py -m venv .venv`, then `.venv\Scripts\activate` in Command Prompt or `.venv\Scripts\Activate.ps1` in PowerShell instead of the POSIX activation command.

Download [hosted.py]({{ site.baseurl }}/examples/gemma/hosted.py):

```python
{% include_relative examples/gemma/hosted.py %}
```

For an image, put a **permitted JPEG/PNG** at `sample.png` and run:

```bash
python hosted.py --image sample.png --prompt "Describe this image and say what is uncertain."
```

Use `--model gemma-4-31b-it` only if that documented model is available to your account. The inline-image SDK pattern follows the [official image-input guide](https://ai.google.dev/gemini-api/docs/image-understanding); Gemma image support is also documented in the hosted Gemma guide. This example's **5 MiB limit is an application safeguard**, not a claim about the provider's maximum.

### JavaScript / TypeScript: backend text and image input

Use the official **`@google/genai` SDK**. The SDK includes TypeScript types; use your existing TypeScript build setup if needed, not a compulsory new framework.

With the [package manifest]({{ site.baseurl }}/examples/gemma/package.json) and [lockfile]({{ site.baseurl }}/examples/gemma/package-lock.json), run from `examples/gemma`:

```bash
npm ci
node --env-file=.env hosted.mjs
```

Download [hosted.mjs]({{ site.baseurl }}/examples/gemma/hosted.mjs). This is **Node.js backend code, not browser code**:

```javascript
{% include_relative examples/gemma/hosted.mjs %}
```

To send your own permitted image:

```bash
node --env-file=.env hosted.mjs sample.png
```

Both examples print non-empty returned text and exit non-zero on validation/API failure. **Text returned does not prove correctness**: inspect it against the task's expected outcome. Do not retry an empty/blocked response blindly.

### Hosted troubleshooting

| Symptom | Next step |
|---|---|
| Missing/placeholder key | Edit private `.env` or configure the backend environment; do not paste the key into source |
| Authentication/access error | Check the key, project, region, account permissions and current model access |
| 404 / model unavailable | Re-check the two exact documented IDs and account availability; do not silently substitute Gemini |
| 429 / quota | Inspect account limits, billing and provider retry guidance; use bounded backoff where appropriate, not an infinite retry loop or fixed quota assumption |
| Timeout/network error | Check connectivity, provider status and application timeout; surface the failure to the user |
| Empty/blocked output or invalid media | Inspect response safety/finish information, supported input types and request size; offer a safe failure state |

## Path B — Local Gemma 4 with Ollama
{: #option-b--local-offline-gemma-with-ollama }

<a id="option-b"></a>

1. Install Ollama from its [official download site](https://ollama.com/download) using the instructions for your OS.
2. Verify installation:

   ```bash
   ollama --version
   ```

3. Start the Ollama application/service. If the local server is not running, run **`ollama serve` in a separate terminal**. Do not launch a second server if the application already owns port 11434.
4. Choose a variant from the [official Google/Ollama guide](https://ai.google.dev/gemma/docs/integrations/ollama) and [current model tags](https://ollama.com/library/gemma4/tags). For the smaller documented E2B route:

   ```bash
   ollama pull gemma4:e2b
   ollama list
   ollama run gemma4:e2b "Explain open-source software in one sentence."
   ```

   The guide also lists `gemma4:e4b`, `gemma4:26b` and `gemma4:31b`. Do not accidentally select a `-cloud` tag when claiming local inference.

### Downloads and hardware

The first download can be large. The current [E2B tag page](https://ollama.com/library/gemma4:e2b) displays approximately **7.5 GB**, and the [E4B page](https://ollama.com/library/gemma4:e4b) approximately **9.5 GB** (checked 30 October 2026). Tags can change: inspect the selected tag and quantisation before downloading.

**Download size is not a RAM requirement or performance guarantee.** Allow disk for weights and caches, and memory for the OS, model, context, optional media and runtime. RAM, GPU/VRAM, quantisation, context length and latency vary. Compare the [current Gemma model card](https://ai.google.dev/gemma/docs/core/model_card_4) and [official sizing guide](https://ai.google.dev/gemma/docs/core), then measure on the actual device. A smaller/quantised variant may reduce resource use but change quality.

### Call the local HTTP API

The documented [Ollama generation endpoint](https://docs.ollama.com/api/generate) is `http://localhost:11434/api/generate`. Set **`"stream": false`** for one JSON response instead of a stream.

Optional terminal test, if `curl` is installed:

```bash
curl --fail-with-body http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{"model":"gemma4:e2b","prompt":"Explain open-source software in one sentence.","stream":false}'
```

Download [ollama.py]({{ site.baseurl }}/examples/gemma/ollama.py), a small application using only Python's standard library. Run `python3 ollama.py`; **no Google SDK or API key is needed**:

```python
{% include_relative examples/gemma/ollama.py %}
```

JavaScript and other language stacks can call the same documented HTTP endpoint from their backend without installing Python. Keep this unauthenticated development endpoint on loopback; do not expose it directly to the internet.

- **Cannot connect / timeout:** start the application or `ollama serve`, check the port and allow for slow cold starts; reduce model/context demands if necessary.
- **Model missing / 404:** run `ollama pull gemma4:e2b` and verify `ollama list`.
- **Empty, incomplete or malformed output:** treat it as a failure, inspect logs and display an explicit error—not “smoke test passed”.
- **Memory failure:** choose an appropriate smaller/quantised model or another permitted execution path. No universal laptop guarantee is made.

After setup, disconnect external connectivity and rerun the core flow if you claim offline operation. Local inference does not by itself prove complete application privacy or eligibility for the Gemma API prize.

## Other supported runtimes
{: #option-c--open-weight-checkpoints-for-custom-harnesses }

<a id="option-c"></a>

These are **optional**, not additional prerequisites:

| Runtime | When to investigate |
|---|---|
| [llama.cpp](https://ai.google.dev/gemma/docs/integrations/llamacpp) | Local GGUF/quantised experimentation and CPU/GPU inference |
| [Hugging Face Transformers](https://ai.google.dev/gemma/docs/core/huggingface_inference) | Python model integration and checkpoint-level control; check hardware and exact library/model support |
| [LM Studio](https://ai.google.dev/gemma/docs/integrations/lmstudio) | Desktop local exploration and a local serving interface |
| [MLX](https://gemma.ai/deployment/mlx/) | Apple-silicon/unified-memory experimentation; community-converted checkpoint names and coverage vary |
| [vLLM](https://gemma.ai/deployment/vllm/) | Advanced high-throughput/concurrent serving with suitable compute; unnecessary for most single-user prototypes |

Google's older MLX page now points to the [new official Gemma documentation hub](https://gemma.ai/). Follow current runtime guidance rather than guessing package versions or checkpoint names. Consult model-specific text/image/audio capability pages; **not every variant or endpoint supports every modality**.

## 3. Choose an application architecture

Pick the least complex tools that serve the proposed problem:

| Layer | Optional choices and decision rule |
|---|---|
| Frontend | HTML/CSS/JavaScript, React, Next.js, Vue, Svelte or a relevant mobile framework. A CLI is also valid; no polished frontend is compulsory. |
| Backend/API | Python with FastAPI/Flask, Node.js/Express, or framework API routes. Prefer a stack you can test and explain. |
| Model integration | Official hosted SDK **on the backend**, or the local inference HTTP API. Validate inputs and outputs. |
| Persistence | No database if none is needed; SQLite for a small prototype, PostgreSQL/managed storage when justified. |
| Retrieval/RAG | Parse, chunk, embed and retrieve only when answers need grounding over a content collection. Show sources and missing-evidence behaviour. AI does not automatically require a vector database. |
| Agents/tools | Only if the model needs to select well-defined tools. Validate arguments, allowlist permissions, bound steps/time/spending and require human confirmation for consequential actions. |
| Testing | Unit tests for ordinary code, a small repeatable AI evaluation set, edge/failure cases and one demo-ready end-to-end flow. |

```text
Browser / mobile client
          |
          v
Backend: input validation + API secrets in environment
          |
          +--> Hosted Gemma 4 API OR local model runtime
          |
          +--> Optional database / retrieval / permitted tools
                     (validate model-selected actions;
                      human approval before consequential actions)
```

The model's output returns to the backend for validation and any approved supporting operations before the client sees it. **API secrets never travel to frontend code.** If the application does not need storage, retrieval or tools, omit those branches.

## 4. Optional DigitalOcean path

**DigitalOcean is optional. Using a DigitalOcean product is not required to win Best Open-Source AI Project.** A working local application or another suitable provider is acceptable. Provider branding is not proof that the selected AI model meets category requirements.

DigitalOcean's MLH material refers to **Gradient AI / Agentic Cloud**. Current product documentation separates the relevant services:

| Resource | Use only when justified |
|---|---|
| [MLH DigitalOcean partner resources](https://www.mlh.com/partners/digitalocean), [Inference](https://docs.digitalocean.com/products/inference/) and [Managed Agents](https://docs.digitalocean.com/products/managed-agents/) | Explore supported managed AI/model workflows and governed agent infrastructure; check current availability, model choice and service maturity |
| [Knowledge Bases](https://docs.digitalocean.com/products/knowledge-bases/) | Managed indexing/retrieval when your project genuinely needs RAG over permitted content |
| [App Platform](https://docs.digitalocean.com/products/app-platform/) | Deploy a web app/API from a Git repository or container image; configure secrets server-side |
| [Droplets](https://docs.digitalocean.com/products/droplets/) / [GPU Droplets](https://docs.digitalocean.com/products/gpu-droplets/) | Only when runtime/compute control warrants VM/GPU administration, setup time and cost |
| [General DigitalOcean documentation](https://docs.digitalocean.com/) | Select storage, databases or networking only as needed |

Open the **current DigitalOcean promo offer in [My Hacktoberfest](https://hacktoberfest.com/my/)** and check the official event/MLH instructions. Check account eligibility, offer availability, expiry, usage limits, billing verification and covered products **before creating resources**. Do not assume a fixed credit amount, free use or a past-year promotion applies to your account.

**Billable cloud resources can continue to incur costs after promotional credits expire or are exhausted.** Review [current inference pricing](https://docs.digitalocean.com/products/inference/details/pricing/) and each chosen product's pricing. Serverless inference has its own prepaid-balance rules; do not assume other services stop automatically. Monitor usage, understand whether alerts are hard spending limits, and remove unneeded resources and retained storage after testing.

## 5. Open-source release checklist

- [ ] Create a **public GitHub repository** for the actual project.
- [ ] Choose an appropriate [OSI-approved application-code licence](https://opensource.org/licenses) and include a real `LICENSE` file. GitHub's licence picker is safer than copying a licence template with unfilled names/placeholders.
- [ ] Name the exact AI model/version/runtime and link its licence/terms. **Open-weight does not automatically mean open-source.** [Gemma 4 is Apache 2.0 licensed](https://ai.google.dev/gemma/docs/core/model_card_4); other models/generations may differ.
- [ ] Record important dependencies, versions, licences, upstream work and original team changes.
- [ ] Document installation, configuration, run commands, tests and expected behaviour; verify a cold start.
- [ ] Include screenshots or a demo URL where possible, without secrets or private information.
- [ ] Never commit API keys, secrets, private user data or unlicensed datasets, including in history.
- [ ] Record data sources, permissions, acknowledgements and known limitations.

Use the [README template]({{ site.baseurl }}/templates/project-readme-template/), [submission checklist]({{ site.baseurl }}/templates/submission-checklist/) and [demo guide]({{ site.baseurl }}/templates/demo-script/). One project/repository may enter both official categories when it qualifies.

## 6. Responsible AI and data

- Use public, synthetic or appropriately consented data with permission for the intended use and redistribution.
- Minimise personal information; do not upload sensitive/confidential data to any model/API without appropriate authorisation and review. Service terms may prohibit it regardless of consent.
- Generated output can be wrong. Check it against evidence; expose uncertainty and missing information instead of presenting unsupported output as fact.
- Design explicit failure states for invalid input, unavailable inference, rate limits, malformed output and unsupported tasks.
- Add human review before high-impact or consequential actions. Do not build unsupported medical diagnosis, legal determination, credit-decision or other high-impact decision systems without suitable professional oversight and safeguards; hosted-service prohibitions still apply.
- Test use-case-relevant prompt injection, malformed inputs and misuse. Treat retrieved documents and model output as untrusted data, not permission to change system rules or execute arbitrary tools.
- Document safety boundaries, model/data limitations and what remains under human control.

Consult Google's [Responsible Generative AI Toolkit](https://ai.google.dev/responsible/docs) and the [Gemma model cards](https://ai.google.dev/gemma/docs/core/model_card_4). The toolkit's current stated focus is English text-to-text; do not assume it certifies every language, modality or application.

## 7. Time-boxed build workflow

The event is **30 October 2026, 7:00 PM → 31 October, 6:00 AM EAT**, with a **6:00 AM submission close** on both category pages. Follow the [event briefing]({{ site.baseurl }}/rules/#the-hacking-timeline) for coding start/stop and demo slots; not all event hours are coding time.

Work backwards from the time available:

1. **Problem and scope:** one primary user, task, AI role and observable success check; complete the [worksheet]({{ site.baseurl }}/templates/problem-statement/).
2. **Minimal model test:** choose one execution path and prove a non-empty response with safe test input; check latency, account/hardware and failure behaviour.
3. **Core application flow:** connect input, validation, model and useful output before adding secondary features.
4. **Only necessary integration:** add persistence, retrieval, tools or deployment only if the core user journey needs them.
5. **Testing and refinement:** run the small evaluation set, edge cases, at least one failure/uncertainty case and relevant misuse tests.
6. **Release and demo preparation:** stop adding features early enough to verify setup, README, licences, configuration, public repo, official submission and rehearsal. Deployment is optional; do not trade a working demonstration for last-minute infrastructure.

## Before relying on an example

The example manifests pin **`google-genai 2.34.0`** and **`@google/genai 2.32.0`**. Use the committed dependencies and current provider documentation for your chosen route.

Run the connection test with your own eligible account or downloaded model, then evaluate the application outcome. Mock tests do not establish live model availability, image accuracy or hardware performance. Measure latency and memory on your actual device, inspect outputs and practise the failure path before your demo.
