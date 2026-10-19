---
title: "3. Multimodal Campus Companion"
parent: Challenges
nav_order: 3
description: "Use Gemma's native text, image, audio, and video understanding to build a useful assistant."
---

# Challenge 3: Multimodal Campus Companion
{: .no_toc }

**MLH category:** Open-weight large/small language model · **Team size:** 3–4
{: .fs-5 .fw-300 }

1. TOC
{: toc }

---

## The pitch

Gemma 4 natively understands **text, image, audio, and video** — not as bolted-on add-ons, but as first-class input. This track is about building something a student or staff member would actually reach for, where "multimodal" isn't a buzzword but the actual feature.

## What to build

A working application where Gemma's multimodal understanding does something a text-only chatbot couldn't.

Ideas to riff on:

- Point your phone at a timetable, notice board, or handwritten notes and get a clean, structured summary
- Turn a recorded lecture or voice memo into a study guide with timestamps
- An accessibility tool: describe a diagram, slide, or lab setup out loud for a visually impaired student
- A "what is this error" tool: screenshot a stack trace or terminal output, get a plain-language explanation
- A short video walkthrough → a step-by-step written guide (great for lab procedures or club workshop recaps)

## Requirements

- [ ] Uses Gemma 4's native image, audio, or video input (not a separate OCR/ASR tool bolted in front of a text-only call — Gemma itself should be doing the understanding)
- [ ] Solves a specific, real problem — name it clearly in your README
- [ ] Public GitHub repo, OSI-approved license, README (see [Rules]({{ site.baseurl }}/rules/#submitting-your-project))
- [ ] README states which Gemma 4 size you used and which modality/modalities

## Suggested Gemma tooling

- [Image understanding guide](https://ai.google.dev/gemma/docs/capabilities/vision/image) and [Video understanding guide](https://ai.google.dev/gemma/docs/capabilities/vision/video)
- [Audio data guide](https://ai.google.dev/gemma/docs/capabilities/audio)
- Native audio/vision is featured on the **E2B, E4B, and 12B** sizes specifically — see the [sizing table]({{ site.baseurl }}/starter-kit/#which-gemma-4-size-should-you-use)
- [Gemma Cookbook `apps/` folder](https://github.com/google-gemma/cookbook/tree/main/apps) for full-stack multimodal demo patterns

## What a strong entry looks like

- You can show, live, a real photo/recording going in and a genuinely useful output coming out
- The UX respects the modality — e.g. voice input stays fast, image upload doesn't require a PhD to use
- Thought given to who actually needs this (accessibility, low-literacy users, or a specific campus workflow)

## Judging emphasis for this track

On top of the [base rubric]({{ site.baseurl }}/judging/#the-score-sheet), judges will specifically check: does the demo genuinely exercise non-text input live, and does the chosen modality meaningfully improve the experience versus a text-only version?
