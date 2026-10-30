---
title: Resources
nav_order: 4
description: "Curated, verified official Gemma and MLH resources, organized by capability."
---

# Resources
{: .no_toc }

Use these official resources for your chosen problem and architecture. There are no mandatory technical tracks; check the current model/runtime documentation before relying on a capability.
{: .fs-6 .fw-300 }

1. TOC
{: toc }

---

## Official MLH event resources (start here)

Choose your own project; the two [live prize categories]({{ site.baseurl }}/challenges/#the-official-mlh-challenge) are awards, not project prompts. The [idea framework]({{ site.baseurl }}/challenges/) and [optional inspiration]({{ site.baseurl }}/inspiration/) help you get started.

These four verified links were provided directly by MLH for this Hacktoberfest Hack Day:

| Resource | Verified Target | Use this when... |
|---|---|---|
| **[Gemma Resources Hub](https://mlh.link/gemma)** | [mlh.com/partners/gemma](https://www.mlh.com/partners/gemma) | You need an overview of MLH's partnership with Google DeepMind and general event benefits. |
| **[Gemma Quickstart](https://mlh.link/gemma-quickstart)** | [ai.google.dev/.../gemma_on_gemini_api](https://ai.google.dev/gemma/docs/core/gemma_on_gemini_api) | You want the fastest path to make your first hosted API call without downloading weights. |
| **[Gemma API & Setup Docs](https://mlh.link/gemma-docs)** | [ai.google.dev/gemma/docs/get_started](https://ai.google.dev/gemma/docs/get_started) | You want setup instructions and official landing docs across SDKs and environments. |
| **[Gemma Beginner Guide](https://mlh.link/gemma-beginnerguide)** | [github.com/google-gemma/cookbook](https://github.com/google-gemma/cookbook) | You want copy-and-adapt starter notebooks and worked applications from the official cookbook. |

---

## Core model documentation & specifications

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

- **[Ollama Integration Guide](https://ai.google.dev/gemma/docs/integrations/ollama)** — Optional local inference; technical support does not prove partner-prize eligibility.
- **[llama.cpp Integration Guide](https://ai.google.dev/gemma/docs/integrations/llamacpp)** — *Use this when* optimizing high-performance CPU/GPU local execution with GGUF checkpoints.
- **[LM Studio Integration](https://ai.google.dev/gemma/docs/integrations/lmstudio)** — *Use this when* you prefer a visual desktop GUI runner to test prompts locally without writing code.
- **[LiteRT-LM Overview](https://ai.google.dev/edge/litert-lm/overview)** — *Use this when* deploying ultra-compact quantized models to mobile devices or embedded hardware.

---

## Specialized model variants

- **[EmbeddingGemma Documentation](https://ai.google.dev/gemma/docs/embeddinggemma)** — Check the exact embedding model's supported inputs, licence and runtime when building retrieval.
- **[FunctionGemma Model Card](https://ai.google.dev/gemma/docs/functiongemma)** — Optional specialised function calling; an older model is not a substitute for Gemma 4 prize evidence.
- **[ShieldGemma 2 Documentation](https://ai.google.dev/gemma/docs/shieldgemma)** — *Use this when* evaluating prompt safety and filtering abusive or harmful model outputs.
- **[PaliGemma 2 Overview](https://ai.google.dev/gemma/docs/paligemma)** — *Use this when* needing fine-grained visual question answering and spatial image captioning.
- **[Gemma 3n Architecture](https://ai.google.dev/gemma/docs/3n)** — *Use this when* exploring mobile-first, edge-optimized models from Google's earlier release wave.

---

## Agent standards & developer harnesses

- **[Agent Skills Open Standard](https://agentskills.io/)** — *Use this when* understanding the principles and ecosystem behind portable agent skills.
- **[Agent Skills Specification](https://agentskills.io/specification)** — Required conformance if your entry is an agent skill, not a requirement to build a skill.
- **[Agent Skills Quickstart](https://agentskills.io/skill-creation/quickstart)** — *Use this when* creating, testing, and packaging your first reusable agent skill.
- **[OpenCode Architecture](https://github.com/sst/opencode)** — An optional reference for bounded harness designs; attribute upstream work and document your original contribution.

---

## Official MLH policies & licensing references

- **[MLH Open Source Prize Categories](https://hacktoberfest-handbook.mlh.com/fest-planning-guide/open-source-prize-categories)** — *Use this when* reviewing the exact evaluation criteria for the official Best Open-Source AI Project challenge.
- **[MLH Submissions & Winner Selection](https://hacktoberfest-handbook.mlh.com/project-submissions-and-judging-for-hacktoberfest-hack-day)** — *Use this when* checking official submission rules and OrganizerHQ winner marking.
- **[MLH Standard Hackathon Rules](https://github.com/MLH/mlh-policies/blob/main/standard-hackathon-rules.md)** — *Use this when* verifying event integrity, timing guidelines, and team conduct.
- **[MLH Code of Conduct](https://static.mlh.io/docs/mlh-code-of-conduct.pdf)** — *Use this when* reviewing community standards and safety reporting procedures.
- **[Open Source Initiative (OSI) Approved Licenses](https://opensource.org/licenses)** — *Use this when* choosing an open-source license (such as MIT, Apache-2.0, or GPL-3.0) for your team's application code.
- **[Gemma 4 Model Card and Apache 2.0 Licence](https://ai.google.dev/gemma/docs/core/model_card_4)** — Verify Gemma 4 licensing separately from your code and hosted-service terms.
- **[Earlier Gemma Terms](https://ai.google.dev/gemma/terms)** — Check applicability for older model generations; do not apply these terms indiscriminately to Gemma 4.

## Optional DigitalOcean resources

DigitalOcean supports **Best Open-Source AI Project** but is **not mandatory**. Use any suitable deployment approach, including a working local application. No provider use alone establishes open-source AI eligibility or earns bonus points.

- [MLH DigitalOcean partner hub](https://www.mlh.com/partners/digitalocean) — General partner resources, not additional category rules.
- [DigitalOcean Inference](https://docs.digitalocean.com/products/inference/) — Optional hosted model services; verify whether the selected model meets your category requirements.
- [App Platform](https://docs.digitalocean.com/products/app-platform/) — Optional application deployment.
- [Inference pricing](https://docs.digitalocean.com/products/inference/details/pricing/) — Check usage charges, credit/balance requirements and account access before spending. Event credits are not assumed.

---

## Organiser maintenance documentation

For event staff and documentation maintainers:
- **[`references/source-register.md`](https://github.com/ITech-Club-zetech-University/hacktoberfest/blob/main/references/source-register.md)** — The internal source-of-truth register tracking URLs, dates checked, verification status, and review schedules.
