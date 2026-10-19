---
title: Challenges
nav_order: 5
has_children: true
description: "5 preset Gemma challenge tracks — pick one primary track instead of inventing an idea from scratch."
---

# Challenges
{: .no_toc }

Pick a track below instead of staring at a blank whiteboard. Each track is designed for an **approximately eight-hour build window** by a 3–4 person student team, with clear baselines and no expensive infrastructure required.
{: .fs-6 .fw-300 }

1. TOC
{: toc }

---

## The official MLH challenge

When your team submits its project on [MLH OrganizerHQ](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club), you are submitting to the **official MLH Hack Day competition**:

- **[Best Open-Source AI Project](https://hacktoberfest-handbook.mlh.com/fest-planning-guide/open-source-prize-categories)** *(Official MLH Hack Day Challenge)*  
  - **What it requires:** Build an original project where open-source software or open-weight AI is an important functional component. Your repository must be public under an OSI-approved open-source license.  
  - **Prize:** Exactly **one winning team** receives official Hacktoberfest Winner DEV Badges on their DEV accounts, plus MLH+DEV swag bags (subject to availability).

{: .note }
> **Understanding the Award Structure:**
> - **One Official MLH Challenge:** "Best Open-Source AI Project" is the confirmed, official Hack Day challenge on OrganizerHQ, with one winning team selected across the event.
> - **Local iTech Club Recognition (Top Three Overall):** All eligible submissions across all 5 preset tracks are evaluated together on a common leaderboard using our published [100-Point Rubric]({{ site.baseurl }}/judging/#the-100-point-score-sheet), naming the **Top Three Overall (1st, 2nd, and 3rd Place)**.
> - **iTech Club Preset Tracks:** The 5 tracks below are iTech Club's curated, structured ways for teams to approach that broader challenge. They represent technical specializations—they are **not** five separate MLH prize categories by default. Challenge-specific acceptance tests inform rubric scoring (specifically Technical Execution and Use of Gemma); they are **not** hidden bonus points.
> - **Partner Prize Availability:** An additional partner challenge (such as a Google Gemma partner prize) is an optional module in OrganizerHQ. It is available only if confirmed in the event's actual OrganizerHQ configuration. Organizers will confirm on-site whether a separate partner challenge is active; event sponsorship alone does not guarantee a separate prize category.

{: .important }
> **Submission Procedure for All Teams:**
> 1. Submit your project on [MLH OrganizerHQ](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club) to **Best Open-Source AI Project** (and any verified partner challenge if confirmed on-site) by 5:00 AM EAT.
> 2. In your repository `README.md` and project description, declare **one primary iTech Club challenge track** (Track 1–5). Local judging evaluates your project against the criteria of your declared primary track.

---

## Overview of the 5 preset tracks

To help you get straight to building, iTech Club has created **5 preset challenge tracks** tailored to Gemma's real strengths. None of these tracks require paid APIs, high-end GPUs, private datasets, or complex cloud infrastructure.

### Quick comparison table for teams

| # | Track Name | Expected Complexity | Technical focus within the MLH challenge | Key Technique | Inference Mode | Likely Laptop Requirements |
|---|---|---|---|---|---|---|
| **1** | **[Build a Gemma Agent Skill]({{ site.baseurl }}/challenges/01-agent-skill/)** | Beginner to Intermediate | Packaging reusable agent capabilities | Agent Skills open standard (`SKILL.md`), CLI driver | Flexible (Gemini API or local Ollama) | Standard student laptop (4–8 GB RAM), internet for API or ~3 GB disk for local |
| **2** | **[Gemma Off the Grid]({{ site.baseurl }}/challenges/02-edge-offline/)** | Intermediate | On-device edge inference & offline execution | Local quantization, edge runtimes, offline-first design | **100% Local Offline** (Ollama, llama.cpp, LiteRT-LM) | Consumer laptop (8–16 GB RAM, ~4–8 GB free disk space for quantized weights); Wi-Fi OFF during demo |
| **3** | **[Multimodal Campus Companion]({{ site.baseurl }}/challenges/03-multimodal-assistant/)** | Beginner to Intermediate | Multimodal vision or audio reasoning | Multimodal model integration, media upload validation | Flexible (Gemini API recommended; local if model supports) | Standard student laptop (4–8 GB RAM); phone/camera for test photos |
| **4** | **[Gemma-Powered Dev Harness]({{ site.baseurl }}/challenges/04-dev-harness/)** | Intermediate to Advanced | Agentic control loops & safety boundaries | Structured function calling, bounded tool execution loops | Flexible (Gemini API or local quantized model) | Standard student laptop (8 GB RAM), Python/Node environment |
| **5** | **[Campus Knowledge Companion (RAG)]({{ site.baseurl }}/challenges/05-rag-knowledge-companion/)** | Intermediate | Retrieval-augmented generation & citations | Document chunking, vector embeddings, similarity search | Flexible (EmbeddingGemma + Gemma API or local) | Standard student laptop (8 GB RAM), ~2 GB disk for local embedding model |

---

## How to choose your primary track

Teams must declare **one primary track** for local judging to ensure fair, peer-level comparison:

- **If your team has standard laptops with modest hardware:** Choose **Track 1 (Agent Skill)**, **Track 3 (Multimodal Companion)**, or **Track 5 (RAG)** using the free [Gemini API](https://mlh.link/gemma-quickstart) where Google provides hosted compute.
- **If your team wants to build without relying on Wi-Fi:** Choose **Track 2 (Gemma Off the Grid)**. Download your small model weights (such as a 2B or edge quantized variant via Ollama) **at home before the event**, and you will not have to worry about venue bandwidth all night.
- **If your team loves developer tools and software engineering:** Choose **Track 1 (Agent Skill)** or **Track 4 (Dev Harness)** to build tools that help other developers write, review, and test code.
- **If your team wants to solve a physical campus problem:** Choose **Track 3 (Multimodal Companion)** or **Track 5 (Campus Knowledge RAG)** using real campus notice boards, course notes, or club documents.

---

## Official MLH reference links

- [MLH Open Source Prize Categories](https://hacktoberfest-handbook.mlh.com/fest-planning-guide/open-source-prize-categories) — Official description of the Best Open-Source AI Project challenge
- [MLH Hack Day Submissions & Winner Selection](https://hacktoberfest-handbook.mlh.com/project-submissions-and-judging-for-hacktoberfest-hack-day) — Official rules for project submission and winner marking
- [MLH Hacktoberfest Planning Guide](https://hacktoberfest-handbook.mlh.com/fest-planning-guide/) — General event format and guidelines
- [Event Registration Page](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club) — Official registration on MLH
