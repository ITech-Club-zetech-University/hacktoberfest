---
title: Resources
nav_order: 4
description: "Curated, official Gemma and MLH resources, organized by what you're trying to do."
---

# Resources
{: .no_toc }

1. TOC
{: toc }

---

## Official event resources (start here)

These four links were provided directly by MLH for this event:

| Resource | What it's for |
|---|---|
| [Gemma Resources hub](https://mlh.link/gemma) | General landing page — model family overview |
| [Gemma Quickstart](https://mlh.link/gemma-quickstart) | *Run Gemma with the Gemini API* — the fastest way to make your first call |
| [Gemma API Docs](https://mlh.link/gemma-docs) | *Get started with Gemma models* — setup and reference |
| [Gemma Beginner Guide](https://mlh.link/gemma-beginnerguide) | The [Gemma Cookbook](https://github.com/google-gemma/cookbook) — tutorials, apps, and worked examples |

## Model documentation

- [Gemma 4 model overview](https://ai.google.dev/gemma/docs/core) — sizes, capabilities, memory requirements
- [Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4) — technical specifications
- [Gemma 4 Technical Report](https://goo.gle/Gemma4Report)
- [Prompt formatting for Gemma 4](https://ai.google.dev/gemma/docs/core/prompt-formatting-gemma4)
- [Function calling with Gemma 4](https://ai.google.dev/gemma/docs/capabilities/text/function-calling-gemma4) — needed for agentic/tool-use projects
- [Thinking modes](https://ai.google.dev/gemma/docs/capabilities/thinking) — configurable reasoning
- [Image understanding](https://ai.google.dev/gemma/docs/capabilities/vision/image) · [Video understanding](https://ai.google.dev/gemma/docs/capabilities/vision/video) · [Audio](https://ai.google.dev/gemma/docs/capabilities/audio)

## Download the models

- [Gemma 4 on Hugging Face](https://huggingface.co/collections/google/gemma-4)
- [Gemma 4 on Kaggle](https://www.kaggle.com/models?query=gemma-4&publisher=google)
- [Gemmaverse](https://deepmind.google/models/gemma/gemmaverse/) — community fine-tunes and variants for inspiration

## Running Gemma

| Where | Guide |
|---|---|
| Cloud (Gemini API) | [Gemma on the Gemini API](https://ai.google.dev/gemma/docs/core/gemma_on_gemini_api) |
| Local, chat UI | [Ollama](https://ai.google.dev/gemma/docs/integrations/ollama) · [LM Studio](https://ai.google.dev/gemma/docs/integrations/lmstudio) |
| Edge / on-device | [LiteRT-LM](https://ai.google.dev/edge/litert-lm/overview) · [llama.cpp](https://ai.google.dev/gemma/docs/integrations/llamacpp) · [MLX (Apple Silicon)](https://ai.google.dev/gemma/docs/integrations/mlx) |
| Android | [Google AI Edge Gallery app](https://github.com/google-ai-edge/gallery) |
| Google Cloud | [Vertex AI / GKE](https://ai.google.dev/gemma/docs/integrations/google-cloud) |

## Building and fine-tuning

- [Tuning overview](https://ai.google.dev/gemma/docs/tune)
- [Fine-tune with Hugging Face Transformers + QLoRA](https://ai.google.dev/gemma/docs/core/huggingface_text_finetune_qlora)
- [Fine-tune in Colab (LoRA)](https://colab.sandbox.google.com/github/google/generative-ai-docs/blob/main/site/en/gemma/docs/lora_tuning.ipynb)
- [Keras inference guide](https://ai.google.dev/gemma/docs/core/keras_inference)

## Gemma variants worth knowing about

Useful beyond the core chat model, depending on your challenge track:

- [EmbeddingGemma](https://ai.google.dev/gemma/docs/embeddinggemma) — text embeddings for semantic search / RAG
- [ShieldGemma 2](https://ai.google.dev/gemma/docs/shieldgemma) — safety classification for inputs/outputs
- [FunctionGemma](https://ai.google.dev/gemma/docs/functiongemma) — small model fine-tuned specifically for function calling
- [PaliGemma](https://ai.google.dev/gemma/docs/paligemma) — vision-language model for deeper image analysis
- [Gemma 3n](https://ai.google.dev/gemma/docs/gemma-3n) — the previous generation's efficient on-device model, still widely supported

## The Gemma Cookbook

The [google-gemma/cookbook](https://github.com/google-gemma/cookbook) repository is the single best source of copy-and-adapt starting points:

- **`tutorials/`** — tested, runnable notebooks for core Gemma capabilities
- **`apps/`** — full-stack, end-to-end demo applications (closest thing to a project template)
- **`docs/`** — core documentation and capability guides
- **`experiments/`** — research-focused notebooks (e.g. domain-specific variants like MedGemma)

## Agent Skills & model harnesses (for Challenges 1 & 4)

- [Agent Skills open standard](https://agentskills.io/) — the spec your Agent Skill submission must comply with
- [Agent Skills specification](https://agentskills.io/specification)
- [Agent Skills quickstart](https://agentskills.io/skill-creation/quickstart)
- Open-source harnesses you can fork or draw from: [OpenCode](https://opencode.ai/) · [Pi](https://github.com/badlogic/pi-mono) · [Hermes Agent](https://hermes-agent.nousresearch.com/) · [OpenClaw](https://openclaw.ai/)

## MLH policies & licensing reference

- [MLH Standard Hackathon Rules](https://github.com/MLH/mlh-policies/blob/main/standard-hackathon-rules.md)
- [MLH Code of Conduct](https://static.mlh.io/docs/mlh-code-of-conduct.pdf)
- [MLH Hacktoberfest Handbook: Best Open-Source AI Project](https://hacktoberfest-handbook.mlh.com/fest-planning-guide/open-source-prize-categories)
- [MLH Hacktoberfest Handbook: Project Submissions & Winner Selection](https://hacktoberfest-handbook.mlh.com/project-submissions-and-judging-for-hacktoberfest-hack-day)
- [Open Source Initiative — approved licenses](https://opensource.org/licenses) (MIT, Apache-2.0, GPL-3.0, and more)

## Can't reach something?

Ask a mentor to pull it up on their hotspot, or check the [Gemma developer forum](https://discuss.ai.google.dev/c/gemma/10) / [Discord](https://ai.google.dev/gemma/docs/discord) — but see [Starter Kit]({{ site.baseurl }}/starter-kit/) for why you really want model weights downloaded *before* the night starts.
