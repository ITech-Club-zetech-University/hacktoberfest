---
title: Resources
nav_order: 4
description: "Official MLH, Gemma, DigitalOcean, PrimeCloud and open-source development resources."
---

# Resources
{: .no_toc }

Use these official resources for your chosen problem and architecture. There are no mandatory technical tracks; check the current model/runtime documentation before relying on a capability.
{: .fs-6 .fw-300 }

1. TOC
{: toc }

---

## Official MLH event resources (start here)

Choose your own project; the three [event prize categories]({{ site.baseurl }}/challenges/#the-official-mlh-challenge) are awards, not project prompts. The [idea framework]({{ site.baseurl }}/challenges/) and [optional inspiration]({{ site.baseurl }}/inspiration/) help you get started.

| Category | Start with |
|---|---|
| Best Open-Source AI Project | MLH open-source guidance, model/licensing resources and optional DigitalOcean resources below |
| Best Use of Gemma 4 | MLH Gemma links and current hosted Gemma documentation below |
| Best Project Deployed on PrimeCloud | [PrimeCloud resources](#primecloud-resources) and the [deployment preparation guide]({{ site.baseurl }}/starter-kit/#deploying-your-project-with-primecloud); AI is optional |

These four verified links were provided directly by MLH for this Hacktoberfest Hack Day:

| Resource | Verified Target | Use this when... |
|---|---|---|
| **[Gemma Resources Hub](https://mlh.link/gemma)** | [mlh.com/partners/gemma](https://www.mlh.com/partners/gemma) | You need an overview of MLH's partnership with Google DeepMind and general event benefits. |
| **[Gemma Quickstart](https://mlh.link/gemma-quickstart)** | [ai.google.dev/.../gemma_on_gemini_api](https://ai.google.dev/gemma/docs/core/gemma_on_gemini_api) | You want the fastest path to make your first hosted API call without downloading weights. |
| **[Gemma API & Setup Docs](https://mlh.link/gemma-docs)** | [ai.google.dev/gemma/docs/get_started](https://ai.google.dev/gemma/docs/get_started) | You want setup instructions and official landing docs across SDKs and environments. |
| **[Gemma Beginner Guide](https://mlh.link/gemma-beginnerguide)** | [github.com/google-gemma/cookbook](https://github.com/google-gemma/cookbook) | You want copy-and-adapt starter notebooks and worked applications from the official cookbook. |

---

## Core model documentation & specifications

- **[Official Gemma Quickstart](https://gemma.ai/get-started/)** — Choose a model and execution route using the current Gemma documentation hub.
- **[Gemma Models Overview](https://ai.google.dev/gemma/docs)** — *Use this when* reviewing model generations, architectural families, and general context windows.
- **[Gemma 4 Core Documentation](https://ai.google.dev/gemma/docs/core)** — *Use this when* checking parameter sizes, official memory sizing tables, and quantization formats (BF16, SFP8, Q4_0, Mobile).
- **[Gemma 4 Model Card](https://ai.google.dev/gemma/docs/core/model_card_4)** — *Use this when* reviewing technical benchmarks, training dataset distributions, and safety evaluations.
- **[Gemma 4 Technical Report](https://goo.gle/Gemma4Report)** — *Use this when* researching architecture details like Multi-Token Prediction and encoder-free unified vision.
- **[Gemma Release Notes](https://ai.google.dev/gemma/docs/releases)** — *Use this when* checking the chronological release history and exact official model identifiers.

---

## Capabilities & prompt engineering

- **[Thinking Modes Guide](https://ai.google.dev/gemma/docs/capabilities/thinking)** — *Use this when* configuring multi-step reasoning for logically demanding tasks or complex code analysis.
- **[Function Calling with Gemma](https://ai.google.dev/gemma/docs/capabilities/text/function-calling-gemma4)** — *Use this when* your project needs bounded, structured tool calls.
- **[Prompt Formatting Guide](https://ai.google.dev/gemma/docs/core/prompt-formatting-gemma4)** — *Use this when* structuring turn-based chat templates (user, model, system) for raw open weights.
- **[Image Understanding Guide](https://ai.google.dev/gemma/docs/capabilities/vision/image)** — Check model and endpoint support before sending images.
- **[Audio Processing Guide](https://ai.google.dev/gemma/docs/capabilities/audio)** — Check the exact model/runtime; family-level audio support does not establish hosted API support.

---

## Model downloads & open weights

- **[Gemma 4 on Hugging Face](https://huggingface.co/collections/google/gemma-4)** — *Use this when* downloading Transformers checkpoints, community GGUF files, or PyTorch weights.
- **[Gemma 4 on Kaggle Models](https://www.kaggle.com/models?query=gemma-4&publisher=google)** — *Use this when* downloading weights directly or running free cloud GPU notebooks on Kaggle.
- **[Gemmaverse Community Hub](https://deepmind.google/models/gemma/gemmaverse/)** — *Use this when* seeking inspiration from community-built tools, fine-tunes, and experimental apps.

---

## Local runtimes & edge inference

- **[Current Gemma with Ollama Guide](https://gemma.ai/deployment/ollama/)** and [Ollama documentation](https://docs.ollama.com/) — Current tags, downloads and local API setup; technical support does not prove partner-prize eligibility.
- **[Hugging Face Transformers](https://huggingface.co/docs/transformers/index)** — Optional model integration; verify support for the exact checkpoint and hardware.
- **[llama.cpp Integration Guide](https://ai.google.dev/gemma/docs/integrations/llamacpp)** — *Use this when* optimizing high-performance CPU/GPU local execution with GGUF checkpoints.
- **[LM Studio Integration](https://ai.google.dev/gemma/docs/integrations/lmstudio)** — *Use this when* you prefer a visual desktop GUI runner to test prompts locally without writing code.
- **[MLX on the current Gemma hub](https://gemma.ai/deployment/mlx/)** — Optional Apple-silicon/unified-memory inference; community checkpoint conversions vary.
- **[vLLM on the current Gemma hub](https://gemma.ai/deployment/vllm/)** — Advanced concurrent/high-throughput serving, not required for a small local prototype.
- **[LiteRT-LM Overview](https://developers.google.com/edge/litert-lm/overview)** — *Use this when* deploying ultra-compact quantized models to mobile devices or embedded hardware.

---

## Specialized model variants

- **[EmbeddingGemma Documentation](https://ai.google.dev/gemma/docs/embeddinggemma)** — Check the exact embedding model's supported inputs, licence and runtime when building retrieval.
- **[FunctionGemma Model Card](https://ai.google.dev/gemma/docs/functiongemma)** — Optional specialised function calling; an older model is not a substitute for Gemma 4 prize evidence.
- **[ShieldGemma 2 Documentation](https://ai.google.dev/gemma/docs/shieldgemma)** — *Use this when* evaluating prompt safety and filtering abusive or harmful model outputs.
- **[PaliGemma 2 Overview](https://ai.google.dev/gemma/docs/paligemma)** — *Use this when* needing fine-grained visual question answering and spatial image captioning.
- **[Gemma 3n Architecture](https://ai.google.dev/gemma/docs/gemma-3n)** — *Use this when* exploring mobile-first, edge-optimized models from Google's earlier release wave.

---

## Agent standards & developer harnesses

- **[Agent Skills Open Standard](https://agentskills.io/)** — *Use this when* understanding the principles and ecosystem behind portable agent skills.
- **[Agent Skills Specification](https://agentskills.io/specification)** — Required conformance if your entry is an agent skill, not a requirement to build a skill.
- **[Agent Skills Quickstart](https://agentskills.io/skill-creation/quickstart)** — *Use this when* creating, testing, and packaging your first reusable agent skill.
- **[OpenCode Architecture](https://github.com/anomalyco/opencode)** — An optional reference for bounded harness designs; attribute upstream work and document your original contribution.
- **[llama.cpp](https://github.com/ggml-org/llama.cpp)** and [vLLM documentation](https://docs.vllm.ai/) — Optional runtime references; neither is a required participant dependency.

---

## Official MLH policies & licensing references

- **[MLH Open-Source AI Guide](https://www.mlh.com/opensource-ai)** — Original project expectations, public licensed source, model disclosures and skill/harness conditions.
- **[MLH Open Source Prize Categories](https://hacktoberfest-handbook.mlh.com/fest-planning-guide/open-source-prize-categories)** — *Use this when* reviewing the exact evaluation criteria for the official Best Open-Source AI Project challenge.
- **[MLH Submissions & Winner Selection](https://hacktoberfest-handbook.mlh.com/project-submissions-and-judging-for-hacktoberfest-hack-day)** — *Use this when* checking official submission rules and OrganizerHQ winner marking.
- **[MLH Standard Hackathon Rules](https://github.com/MLH/mlh-policies/blob/main/standard-hackathon-rules.md)** — *Use this when* verifying event integrity, timing guidelines, and team conduct.
- **[MLH Code of Conduct](https://github.com/MLH/mlh-policies/blob/main/code-of-conduct.md)** — *Use this when* reviewing community standards and safety reporting procedures.
- **[Open Source Initiative (OSI) Approved Licenses](https://opensource.org/licenses)** — *Use this when* choosing an open-source license (such as MIT, Apache-2.0, or GPL-3.0) for your team's application code.
- **[GitHub: Licensing a Repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)** — Add a code licence; publishing code without one does not automatically grant open-source reuse rights.
- **[Responsible Generative AI Toolkit](https://ai.google.dev/responsible/docs)** — Practical responsible-AI guidance alongside the chosen model's card and service terms.
- **[Gemma 4 Model Card and Apache 2.0 Licence](https://ai.google.dev/gemma/docs/core/model_card_4)** — Verify Gemma 4 licensing separately from your code and hosted-service terms.
- **[Earlier Gemma Terms](https://ai.google.dev/gemma/terms)** — Check applicability for older model generations; do not apply these terms indiscriminately to Gemma 4.

## Optional DigitalOcean resources

DigitalOcean supports **Best Open-Source AI Project** but is **not mandatory**. Use any suitable deployment approach, including a working local application. No provider use alone establishes open-source AI eligibility or earns bonus points.

- [MLH DigitalOcean partner hub](https://www.mlh.com/partners/digitalocean) — General partner resources, not additional category rules.
- [DigitalOcean Inference](https://docs.digitalocean.com/products/inference/) — The former Gradient AI Platform documentation URL redirects here. Optional hosted model services; verify whether the selected model meets your category requirements.
- [App Platform](https://docs.digitalocean.com/products/app-platform/) — Optional application deployment.
- [Knowledge Bases](https://docs.digitalocean.com/products/knowledge-bases/) — Managed retrieval only if the problem needs grounded answers over permitted content.
- [Managed Agents](https://docs.digitalocean.com/products/managed-agents/) and [GPU Droplets](https://docs.digitalocean.com/products/gpu-droplets/) — Optional advanced workflows/compute; check availability, maturity and cost.
- [My Hacktoberfest](https://hacktoberfest.com/my/) — Sign in yourself to inspect the current DigitalOcean promo offer, eligibility, expiry, limits and billing terms. No credit amount is assumed.
- [Inference pricing](https://docs.digitalocean.com/products/inference/details/pricing/) — Check usage charges, credit/balance requirements and account access before spending. Event credits are not assumed.
- [General DigitalOcean documentation](https://docs.digitalocean.com/) — Storage, databases and networking only where your project needs them.

## PrimeCloud resources
{: #primecloud-resources }

**PrimeCloud — Build. Launch. Grow.** These resources support **Best Project Deployed on PrimeCloud**. Deployment on PrimeCloud is required only for that category; Gemma 4 is not required.

| Official resource | Use this for |
|---|---|
| [PrimeCloud website](https://primecloud.cloud) | Platform overview and current official navigation |
| [Documentation](https://primecloud.cloud/docs) | Starting points for deployment, services, security and plans |
| [Deployment quickstart](https://primecloud.cloud/docs/quickstart) | Account/workspace preparation, application/services, deployment and live verification; its CLI block is labelled illustrative |
| [Account signup](https://primecloud.cloud/signup) | Create your own account; follow the current account and workspace instructions |
| [Plans and pricing](https://primecloud.cloud/pricing) | Current Production plan details, limits and billing terms before provisioning |
| [Support](https://primecloud.cloud/support) | Deployment, account, billing and recovery help; confirm exact runtime/version support and configuration for your stack |

The documentation describes deployment from Git, containers or source code, and the quickstart mentions the Customer Console or CLI. These high-level descriptions are **not a verified runtime/version compatibility matrix or executable CLI recipe**. Confirm the exact supported technologies and workflow with sponsor support. The [starter guide]({{ site.baseurl }}/starter-kit/#deploying-your-project-with-primecloud) separates general preparation from those platform-specific steps.

**PrimeCloud Production Plan – 3 Months**  
The winning developer will receive three months of PrimeCloud Production, with access to the standard Production plan features and allowances.

This winner's prize is not a promise of free services to every entrant. Use the current plan page for product information; do not infer extra credits, resource allowances or redemption conditions. See the [category requirements]({{ site.baseurl }}/challenges/#best-project-deployed-on-primecloud).
