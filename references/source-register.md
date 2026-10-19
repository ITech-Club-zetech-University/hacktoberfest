# Organiser Source Register & Technical Verification Log

This document serves as the internal source-of-truth register for event organisers and documentation maintainers. It records the primary documentation sources, their verified status, dates checked, and review notes for fast-evolving model checkpoints and SDK releases.

{: .note }
> **Maintainer Note:** This file is intended for organisers and site maintainers. Keep this updated whenever model families, API endpoints, SDK versions, or MLH event rules change.

---

## 1. Primary Sources & Verification Status

| Resource Title | Primary URL | Publisher / Authority | What Claim / Guidance It Supports | Date Checked | Verification Status | Next Review Note |
|---|---|---|---|---|---|---|
| **MLH Event Listing (14735)** | [events.mlh.com/.../14735](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club) | Major League Hacking | Event date, venue, overnight schedule, student-only eligibility | 19 Oct 2026 | **Verified** | Check for last-minute venue or timing notices |
| **MLH Gemma Partner Hub** | [mlh.link/gemma](https://mlh.link/gemma) | MLH / Google DeepMind | Redirects to `www.mlh.com/partners/gemma`; general partner overview | 19 Oct 2026 | **Verified** (Redirect) | Periodic review of partner perks |
| **MLH Gemma Quickstart** | [mlh.link/gemma-quickstart](https://mlh.link/gemma-quickstart) | MLH / Google | Redirects to `ai.google.dev/gemma/docs/core/gemma_on_gemini_api` | 19 Oct 2026 | **Verified** (Redirect) | Check for changes in supported API model IDs |
| **MLH Gemma Docs** | [mlh.link/gemma-docs](https://mlh.link/gemma-docs) | MLH / Google | Redirects to `ai.google.dev/gemma/docs/get_started` | 19 Oct 2026 | **Verified** (Redirect) | Review when Google updates getting started flow |
| **MLH Gemma Beginner Guide** | [mlh.link/gemma-beginnerguide](https://mlh.link/gemma-beginnerguide) | MLH / Google | Redirects to `github.com/google-gemma/cookbook` | 19 Oct 2026 | **Verified** (Redirect) | Confirm repo branch and structure stability |
| **Gemma Models Overview** | [ai.google.dev/gemma/docs](https://ai.google.dev/gemma/docs) | Google AI for Developers | Architecture, model family categorization, context windows | 19 Oct 2026 | **Verified** | Check monthly for new model family announcements |
| **Gemma Release Notes** | [ai.google.dev/gemma/docs/releases](https://ai.google.dev/gemma/docs/releases) | Google AI for Developers | Release chronology, parameter sizes, and release dates | 19 Oct 2026 | **Verified** | Check before hackathon kickoff for new patch releases |
| **Run Gemma on Gemini API** | [ai.google.dev/.../gemma_on_gemini_api](https://ai.google.dev/gemma/docs/core/gemma_on_gemini_api) | Google AI for Developers | Hosted models (`gemma-4-31b-it`, `gemma-4-26b-a4b-it`), SDK syntax (`google-genai`), thinking modes, function calling | 19 Oct 2026 | **Verified** | Confirm model strings remain active in v1beta API |
| **Gemma 4 Core Docs & Sizing** | [ai.google.dev/gemma/docs/core](https://ai.google.dev/gemma/docs/core) | Google AI for Developers | Table 1 memory requirements, quantization formats (BF16, SFP8, Q4_0, Mobile), multimodal specs | 19 Oct 2026 | **Verified** | Re-verify memory benchmarks when runtimes update |
| **EmbeddingGemma 2 Documentation** | [ai.google.dev/gemma/docs/embeddinggemma](https://ai.google.dev/gemma/docs/embeddinggemma) | Google AI for Developers | 740M multimodal embeddings, Apache 2.0 license, 8K context, MRL dimensions (128–768) | 19 Oct 2026 | **Verified** | Test sentence-transformers compatibility scripts |
| **FunctionGemma Model Card** | [ai.google.dev/gemma/docs/functiongemma](https://ai.google.dev/gemma/docs/functiongemma) | Google AI for Developers | 270M specialized function calling base model, Kaggle/HF links | 19 Oct 2026 | **Verified** | Review adapter format requirements |
| **Gemma 3n Overview** | [ai.google.dev/gemma/docs/3n](https://ai.google.dev/gemma/docs/3n) | Google AI for Developers | Mobile-optimized E2B and E4B architecture | 19 Oct 2026 | **Verified** | Corrected slug from older `gemma-3n` to `3n` |
| **ShieldGemma Documentation** | [ai.google.dev/gemma/docs/shieldgemma](https://ai.google.dev/gemma/docs/shieldgemma) | Google AI for Developers | Safety evaluation models and policy definitions | 19 Oct 2026 | **Verified** | Monitor for ShieldGemma policy updates |
| **Ollama Model Library** | [ollama.com/library](https://ollama.com/library) | Ollama | Official model tags (`gemma4:e2b`, `gemma4:e4b`, `gemma2:2b`, `embeddinggemma`) and pull commands | 19 Oct 2026 | **Verified** | Verify tags against local Ollama daemon before event |
| **Google GenAI Python SDK** | [github.com/googleapis/python-genai](https://github.com/googleapis/python-genai) | Google Cloud | Current `google-genai` SDK package, replacing legacy `google-generativeai` | 19 Oct 2026 | **Verified** | Monitor pip release cadence |
| **Agent Skills Specification** | [agentskills.io/specification](https://agentskills.io/specification) | Agent Skills Community | `SKILL.md` YAML frontmatter requirements, directory structure | 19 Oct 2026 | **Verified** | Track version updates to the specification |
| **MLH Hack Day Handbook: Submissions** | [hacktoberfest-handbook.mlh.com/...](https://hacktoberfest-handbook.mlh.com/project-submissions-and-judging-for-hacktoberfest-hack-day) | Major League Hacking | OrganizerHQ submission steps, private/public winner marking workflow | 19 Oct 2026 | **Verified** | Ensure compliance during submission window |
| **MLH Prize Categories** | [hacktoberfest-handbook.mlh.com/...](https://hacktoberfest-handbook.mlh.com/fest-planning-guide/open-source-prize-categories) | Major League Hacking | Best Open-Source AI Project challenge requirements | 19 Oct 2026 | **Verified** | Re-verify single-winner criteria |

---

## 2. Model Licensing & Terms Matrix

| Model Family / Variant | Underlying License / Terms | OSI-Approved? | Commercial Use Permitted? | Attribution / Usage Obligations |
|---|---|---|---|---|
| **Participant Application Code** | Author's choice (e.g. MIT, Apache-2.0, GPL-3.0) | **Yes** | Yes (per license) | Required by MLH baseline rules (`LICENSE` at root) |
| **Gemma 4 (E2B, E4B, 12B, 26B, 31B)** | [Gemma Terms of Use](https://ai.google.dev/gemma/terms) | No (Open-Weight) | Yes (Responsible use) | Must acknowledge terms; comply with Prohibited Use Policy |
| **Gemma 3 / Gemma 3n** | [Gemma Terms of Use](https://ai.google.dev/gemma/terms) | No (Open-Weight) | Yes (Responsible use) | Standard Gemma commercial terms |
| **Gemma 2 (2B, 9B, 27B)** | [Gemma Terms of Use](https://ai.google.dev/gemma/terms) | No (Open-Weight) | Yes (Responsible use) | Standard Gemma commercial terms |
| **EmbeddingGemma 2 (740M)** | [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) | **Yes** | Yes | Permissive open-source license |
| **EmbeddingGemma 1 (308M)** | [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) | **Yes** | Yes | Permissive open-source license |
| **FunctionGemma (270M)** | [Gemma Terms of Use](https://ai.google.dev/gemma/terms) | No (Open-Weight) | Yes (Responsible use) | Standard Gemma commercial terms |
| **PaliGemma / PaliGemma 2** | [Gemma Terms of Use](https://ai.google.dev/gemma/terms) | No (Open-Weight) | Yes (Responsible use) | Standard Gemma commercial terms |

---

## 3. Untested External Operations & Assumptions

The following operations were validated by authoritative documentation inspection and syntax verification, but intentionally excluded from live automated CI/QA to avoid paid account consumption, API rate exhaustion, or gigabyte-scale network downloads during repository maintenance:
1. **Live Paid API Inference:** Live calls to `client.models.generate_content()` against the Gemini API were not executed during testing; syntax was verified against the official `google-genai` SDK reference.
2. **Multi-Gigabyte Weight Downloads:** Commands such as `ollama pull gemma4:31b` or downloading unquantized 70 GB checkpoints were not executed on the local runner; official Ollama tags and file sizes were verified against the public Ollama registry.
3. **Private OrganizerHQ Dashboard:** Direct inspection of event `14735` behind organizer login was left as an internal action item for the lead organizer.
