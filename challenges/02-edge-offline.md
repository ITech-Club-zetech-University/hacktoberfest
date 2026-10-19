---
title: "2. Gemma Off the Grid"
parent: Challenges
nav_order: 2
description: "Build something useful that runs Gemma fully on-device, no internet required."
---

# Challenge 2: Gemma Off the Grid
{: .no_toc }

**MLH category:** Open-weight small language model (SLM) · **Team size:** 3–4
{: .fs-5 .fw-300 }

1. TOC
{: toc }

---

## The pitch

Nairobi has great connectivity most of the time — but "most of the time" isn't "always," and plenty of real use cases (rural clinics, field research, classrooms with capped data, a packed venue's overloaded Wi-Fi) need AI that works **without a live connection**. Gemma 4's small variants (E2B/E4B, ≤10B parameters) are built exactly for this.

## What to build

A working application where **Gemma runs entirely on-device** — no API call to a cloud model at inference time — solving a problem that genuinely benefits from being offline-capable.

Ideas to riff on:

- A study/revision assistant that works with zero data bundle
- A basic symptom-triage or first-aid information tool for use where connectivity is unreliable
- An offline translator or language-learning tool for one of Kenya's local languages
- A field-data assistant (forms, note-taking, summarization) for research or fieldwork with no signal
- Adapt the idea Gemma's own team has highlighted: using a small on-device model to detect things in the field with no network required

## Requirements

- [ ] Uses a Gemma 4 **SLM** (E2B or E4B, ≤10B parameters — per MLH's definition)
- [ ] Demonstrably runs **with Wi-Fi/data off** — judges may ask you to prove it live
- [ ] Public GitHub repo, OSI-approved license, README (see [Rules]({{ site.baseurl }}/rules/#submitting-your-project))
- [ ] README states exact model/quantization used and approximate memory footprint

## Suggested Gemma tooling

- [Ollama](https://ai.google.dev/gemma/docs/integrations/ollama) or [LM Studio](https://ai.google.dev/gemma/docs/integrations/lmstudio) for quick local inference
- [LiteRT-LM](https://ai.google.dev/edge/litert-lm/overview) or [llama.cpp](https://ai.google.dev/gemma/docs/integrations/llamacpp) for lighter-weight / mobile deployment
- [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) if you want to target Android specifically
- QAT (quantization-aware training) checkpoints — see [Resources]({{ site.baseurl }}/resources/) — for the best quality-per-megabyte tradeoff
- See the [Gemma 4 memory requirements table]({{ site.baseurl }}/starter-kit/#which-gemma-4-size-should-you-use) before picking a size

## What a strong entry looks like

- It actually works offline in the demo, not "it would work offline in theory"
- Honest about trade-offs: what did you give up by going small/local, and how did you work around it (e.g. clever prompting, a small fine-tune, caching)?
- Solves a problem where offline is the point, not an afterthought

## Judging emphasis for this track

On top of the [base rubric]({{ site.baseurl }}/judging/#the-score-sheet), judges will specifically check: does the live demo actually run without a network connection, and is the model size/quantization choice justified given the device it's running on?
