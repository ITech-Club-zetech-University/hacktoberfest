---
title: "5. Campus Knowledge Companion (RAG)"
parent: Challenges
nav_order: 5
description: "Build a retrieval-augmented Gemma assistant that answers questions grounded in a real source."
---

# Challenge 5: Campus Knowledge Companion (RAG)
{: .no_toc }

**MLH category:** Open-weight large/small language model + retrieval · **Team size:** 3–4
{: .fs-5 .fw-300 }

1. TOC
{: toc }

---

## The pitch

Gemma is a great generalist — but it doesn't know your course outline, your club's constitution, or yesterday's announcement. Retrieval-augmented generation (RAG) fixes that: search a real corpus first, then let Gemma answer **grounded in what it found**, with citations. This track pairs Gemma with [EmbeddingGemma](https://ai.google.dev/gemma/docs/embeddinggemma) for retrieval.

## What to build

A working question-answering tool over a real, specific corpus you choose — not a generic "chat with any PDF" demo, but grounded in something genuinely useful to the Zetech / iTech Club / Nairobi tech community.

Ideas to riff on:

- A Q&A assistant over a specific course's notes, past papers, and course outline
- An assistant over iTech Club's own documentation, constitution, and past event archives
- A tool that answers questions over Kenyan open government or civic data
- A "contribute to this repo" assistant that answers questions grounded in a real open-source project's docs and issues

## Requirements

- [ ] Retrieval is real: a genuine index (vector or otherwise) over a genuine corpus, not a prompt stuffed with the whole document
- [ ] Gemma's answers are **grounded** — the app shows which source(s) an answer came from
- [ ] Corpus is something a judge can inspect (even a sample), and you're allowed to use it (your own notes, public data, or content you have rights to)
- [ ] Public GitHub repo, OSI-approved license, README (see [Rules]({{ site.baseurl }}/rules/#submitting-your-project))
- [ ] README states what embedding model and what Gemma model you used, and roughly how big the corpus is

## Suggested Gemma tooling

- [EmbeddingGemma](https://ai.google.dev/gemma/docs/embeddinggemma) for turning your corpus into searchable vectors — see its [get-started guide](https://ai.google.dev/gemma/docs/embeddinggemma/inference-embeddinggemma-with-sentence-transformers)
- Gemma 4 for the generation step, via the [Gemini API](https://mlh.link/gemma-quickstart) or local inference
- [ShieldGemma 2](https://ai.google.dev/gemma/docs/shieldgemma) if you want to add a safety filter on top (bonus, not required)
- A simple vector store is fine for an overnight build — even an in-memory array with cosine similarity is legitimate RAG at this scale; don't burn hours standing up infrastructure you don't need

## What a strong entry looks like

- Ask it something that's *only* answerable from your corpus, and it gets it right **with a citation**
- Ask it something **not** in the corpus, and it says so rather than confidently making something up
- The corpus is real and specific enough that a judge can spot-check an answer

## Judging emphasis for this track

On top of the [base rubric]({{ site.baseurl }}/judging/#the-score-sheet), judges will specifically check: does retrieval actually run (not simulated), are answers grounded with visible citations, and does the tool admit when something isn't in its corpus?
