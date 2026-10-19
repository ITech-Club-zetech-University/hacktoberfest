---
title: "5. Campus Knowledge Companion (RAG)"
parent: Challenges
nav_order: 5
description: "Build a retrieval-augmented generation (RAG) assistant that answers questions strictly grounded in a real, inspectable campus corpus with visible citations."
---

# Challenge 5: Campus Knowledge Companion (RAG)
{: .no_toc }

**Track focus:** Retrieval-augmented generation, grounding & citation · **Target window:** ~8 hours · **Team size:** 3–4
{: .fs-5 .fw-300 }

1. TOC
{: toc }

---

## 1. Pitch & target user

Standard language models are trained on general internet data—they have never read Zetech University's course syllabus, the iTech Club constitution, or yesterday's official campus club announcements. If asked about these, generic models either hallucinate plausible fiction or admit complete ignorance. **Retrieval-Augmented Generation (RAG)** solves this by retrieving relevant text excerpts from an inspectable document collection and feeding those excerpts to Gemma to produce an accurate, grounded answer with citations.

- **Target user:** Students looking up degree prerequisites and exam policies, new iTech Club members exploring club archives, or staff members navigating university procedures.
- **The golden rule:** **Prompt stuffing is strictly not RAG.** Stuffing an entire multi-page document into a single static prompt window fails the retrieval requirement. Your project must implement a real indexing and retrieval mechanism that dynamically fetches only the top relevant chunks for each query.

## 2. Problem to solve

Students routinely struggle to find definitive answers across scattered campus documents:
- Looking up specific graduation credit requirements or prerequisite rules across departmental syllabus PDFs.
- Navigating the iTech Club constitution, election rules, or project contribution guidelines.
- Searching university academic calendar deadlines, fee payment milestones, and library policies.
- Answering questions over open Kenyan civic datasets or public tech community archives.

The goal is to create a trustworthy assistant that provides accurate answers backed by verified source citations, while clearly stating when a question cannot be answered from the provided corpus.

## 3. Minimum viable project (MVP)

A successful MVP for this track requires:
1. **A small, inspectable corpus:** A collection of 5–30 public or synthetic documents (markdown files, text documents, or public PDFs) stored directly in your repository.
2. **Document chunking & indexing:** A script that breaks documents into manageable text chunks and indexes them (using vector embeddings such as [EmbeddingGemma](https://ai.google.dev/gemma/docs/embeddinggemma) or sentence-transformers, or a local vector store like Chroma, FAISS, or an in-memory cosine similarity matrix).
3. **Dynamic retrieval:** A query engine that searches the index for a user prompt and retrieves the top-k most relevant chunks.
4. **Grounded synthesis with Gemma:** A generation step where Gemma receives the retrieved context and user query, formats an answer based *only* on that context, and appends explicit source citations.
5. **Honest unanswerable handling:** The system explicitly states when information is missing from the corpus rather than fabricating an answer.

## 4. Required Gemma contribution

In a RAG system, two distinct AI roles must be clearly identified:
- **The embedding model:** Converts corpus chunks and user queries into dense mathematical vector representations (e.g. `EmbeddingGemma` or a sentence-transformers embedding model).
- **The generative Gemma model:** Reads the retrieved text chunks, analyzes the user question, synthesizes a clear answer, and produces citations directly referencing the source documents (via Gemini API or local Gemma inference).
- **How judges inspect it:** Judges will inspect the retrieved context in your logs before Gemma generates its response. They will verify that the answer quotes or references details present in those specific chunks and will ask an unanswerable question to ensure Gemma admits the limit of its retrieved knowledge.

## 5. Mandatory acceptance criteria

Every valid entry in this track must pass these five observable tests:

1. **Genuine retrieval pipeline:** Implements active chunking, indexing, and dynamic top-k chunk retrieval. Whole-document prompt stuffing or static context windows will not pass.
2. **Answerable question with visible citations:** When asked a question present in the corpus, the assistant answers accurately and displays visible citations (document name, section, or chunk number) for every factual claim.
3. **Source verification:** The facts cited in the answer can be directly verified by judges opening the corresponding raw file in the repository's `corpus/` folder.
4. **Graceful handling of absent information:** When asked a question completely absent from the corpus (e.g. "What is the fee policy at Oxford University?"), the assistant clearly states that the information is not available in the corpus, with zero hallucination.
5. **Resistance to distractor/irrelevant text:** When presented with queries where some retrieved chunks are irrelevant, the system correctly discards the irrelevant information and answers using only the pertinent facts.

## 6. Suggested 2-minute demo scenario

When presenting your RAG companion to judges, follow this structured demo script:

- **0:00 – 0:30 (Corpus & Architecture):** Show judges your `corpus/` directory in the repository (e.g. 10 campus club policies). Explain your chunking strategy and identify the embedding model and generative Gemma model used.
- **0:30 – 1:10 (Test 1 — Answerable Query with Citation):** Ask a specific question answerable from your corpus (e.g., "What is the quorum required for an iTech Club constitutional amendment?"). Show the retrieved chunks, followed by Gemma's generated answer with clear citations (e.g., `[Source: itech_constitution.md#section-4]`).
- **1:10 – 1:40 (Test 2 — Absent / Unanswerable Query):** Ask a question that is intentionally **not** in the corpus (e.g., "What are the rules for campus parking permits?"). Show that the system detects zero relevant matches and politely responds that the corpus does not contain this information.
- **1:40 – 2:00 (Behind the Scenes):** Open your terminal or developer console to show the raw retrieved similarity scores and chunks, proving that dynamic search took place.

## 7. Required repository & README evidence

Your public GitHub repository must include:
- [ ] A `README.md` containing:
  - User problem, campus scenario, target audience, and explicit declaration of this track as your team's primary iTech Club challenge track.
  - Description of the corpus and proof that it contains only public or permissible data.
  - Exact embedding model used (e.g. `EmbeddingGemma` or sentence-transformers).
  - Exact generative Gemma model used (e.g. `gemma-4-31b-it` via Gemini API or local Ollama) and acknowledgment of the [Gemma Terms of Use](https://ai.google.dev/gemma/terms).
  - Chunking strategy (chunk size, overlap) and vector store choice (Chroma, FAISS, in-memory array, etc.).
  - Step-by-step instructions to index the corpus and run the query interface.
  - Disclosure of any AI coding tools used during development.
- [ ] A `corpus/` directory containing the text/markdown files used for indexing.
- [ ] Working indexing and retrieval scripts.
- [ ] An OSI-approved open-source `LICENSE` file.

## 8. Stretch goals (optional)

These optional enhancements will distinguish advanced entries but are **not** required to pass:
- **Hybrid search:** Combine semantic vector retrieval with exact keyword search (BM25) for high-accuracy acronym and name matching.
- **Interactive source viewer:** Enable users to click on a citation in the UI to view the exact highlighted paragraph in the original document.
- **Re-ranking step:** Implement a lightweight re-ranker to order retrieved chunks before passing them to Gemma.
- **ShieldGemma integration:** Add a safety classification layer using [ShieldGemma 2](https://ai.google.dev/gemma/docs/shieldgemma) to filter toxic queries or harmful outputs.

## 9. Starter resources

- [EmbeddingGemma Overview](https://ai.google.dev/gemma/docs/embeddinggemma) — Google's official text embedding model for retrieval
- [EmbeddingGemma Sentence-Transformers Guide](https://ai.google.dev/gemma/docs/embeddinggemma/inference-embeddinggemma-with-sentence-transformers) — Quick vectorization in Python
- [Gemma Quickstart via Gemini API](https://mlh.link/gemma-quickstart) — Generative Gemma setup
- [Gemma Cookbook `tutorials/`](https://github.com/google-gemma/cookbook/tree/main/tutorials) — Runnable RAG notebooks
- [ShieldGemma Documentation](https://ai.google.dev/gemma/docs/shieldgemma) — Safety filtering for AI applications

## 10. Privacy, safety & licensing

- **Open-source software license:** Your application source code must be published under an OSI-approved license (e.g., MIT, Apache-2.0). Underlying model weights (EmbeddingGemma, generative Gemma) are governed separately by the [Gemma Terms of Use](https://ai.google.dev/gemma/terms).
- **Public and synthetic data only:** **Never use private student records, grades, admission numbers, disciplinary logs, or confidential university faculty communications** in your corpus.
- **Permissible documents:** Use public club constitutions, open-source documentation, synthetic syllabus outlines created by your team, or public government data.
- **Preventing hallucinations:** Grounding is a safety feature. Ensure your system prompt explicitly instructs Gemma not to invent facts outside the retrieved context.

## 11. Challenge-specific evaluation notes

These notes supplement the 100-point rubric in [`judging.md`]({{ site.baseurl }}/judging/):
- **Verification of dynamic retrieval (under Technical Execution):** Judges will inspect code to verify that the query runs against an index and retrieves top chunks dynamically. Hardcoded prompts or static context will fail this test.
- **Citation accuracy (under Open-Source Quality):** Judges will spot-check citations against the raw files in your `corpus/` folder to ensure citations are genuine and accurate.
- **Handling unknown queries (under Problem & Impact):** The system must gracefully admit when it does not know something rather than hallucinating answers.
