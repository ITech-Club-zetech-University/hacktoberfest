---
title: "2. Gemma Off the Grid"
nav_exclude: true
search_exclude: true
published: false
description: "Build an edge application that runs Gemma entirely on-device, with zero network connectivity required at runtime."
---

# Challenge 2: Gemma Off the Grid
{: .no_toc }

{: .important }
> **Historical brief — not current rules.** The event is now open-ended. This archived brief's track choice, team size, time estimate, model conditions and acceptance checklist are not participant requirements. Local-only inference does not automatically qualify for the Gemma 4 prize. Read the [current project brief]({{ site.baseurl }}/challenges/) or [optional inspiration]({{ site.baseurl }}/inspiration/) instead.

**Track focus:** On-device edge inference & offline-first design · **Target window:** ~8 hours · **Team size:** 3–4
{: .fs-5 .fw-300 }

1. TOC
{: toc }

---

## 1. Pitch & target user

In many regions across Kenya and sub-Saharan Africa, dependable high-speed internet is neither guaranteed nor affordable. From rural clinics and field research stations to campus computer labs during power outages or packed venue Wi-Fi networks, real people need intelligent tools that work completely disconnected from the cloud. In this track, your team builds a working, practical application where **Gemma runs 100% locally on-device**.

- **Target user:** Field healthcare workers, agricultural extension officers, rural students with limited data bundles, or anyone operating in environments where cloud APIs are unavailable, costly, or unreliable.
- **The golden rule:** A cloud API call to any remote server does **not** satisfy offline inference. The model weights must sit on your local hard drive and execute on local compute. Record an unmet offline check under the rubric; deliberately misrepresenting cloud inference as local is handled under the published integrity rules.

## 2. Problem to solve

Cloud-dependent AI fails the moment connectivity drops. Your team will address a problem where offline capability is the core requirement, not an afterthought:
- **Emergency first aid & symptom triage:** Immediate guidance for first responders or community health volunteers in remote areas without cellular reception.
- **Offline campus study companion:** Instant question answering, concept revision, and quiz generation for students studying on low-cost laptops without Wi-Fi.
- **Field research & agricultural assistant:** Structured data collection, crop disease symptom identification, or soil treatment lookup in remote farms.
- **Local language translation helper:** Offline translation and phrasebook assistance between English, Swahili, or local languages for field workers.

## 3. Minimum viable project (MVP)

A successful MVP for this track requires:
1. A small open-weight Gemma model (such as a 2B or edge variant) downloaded and configured to run locally via an offline runtime (e.g. [Ollama](https://ollama.com), [llama.cpp](https://github.com/ggerganov/llama.cpp), or [LiteRT-LM](https://ai.google.dev/edge/litert-lm/overview)).
2. A lightweight user interface (command-line CLI, terminal TUI, or local web UI served on `localhost`).
3. An end-to-end workflow solving a specific problem that completes input, local model inference, and output display with **all network connections disabled**.

## 4. Required Gemma contribution

Gemma is the local cognitive engine powering the application:
- **What Gemma does:** Gemma generates answers, structures field notes, or categorizes symptoms directly on your laptop's CPU or consumer GPU.
- **How judges inspect it:** Disable external network connections (Wi-Fi, Ethernet, Bluetooth tethering and cellular hotspots) live; keep loopback available for a local UI or Ollama. Launch the app and submit a prompt. Show cached weights, the local runtime and CPU/GPU activity. Process monitors alone do not prove zero external traffic; use adapter state and, where available, network monitoring as supporting evidence.

## 5. Minimum implementation acceptance criteria

These four observable checks define a working baseline. Missing checks inform the published rubric, not automatic local disqualification or fixed deductions; see [incomplete prototypes and cross-track fairness]({{ site.baseurl }}/judging/#fair-cross-track-evaluation).

1. **Complete offline operation:** 100% of runtime inference, prompt processing, and UI display functions normally with Wi-Fi, Ethernet, and cellular hotspot adapters disabled. (External web scraping and remote API calls are strictly disallowed during inference).
2. **Documented cold-start instructions:** The repository `README.md` provides exact, copy-pasteable commands explaining how to launch the local model runtime and the application from a clean boot.
3. **Responsive baseline performance:** Handles a realistic, standard user input and returns a coherent, helpful response within a reasonable latency window on standard student laptop hardware (under 30 seconds on modern consumer CPUs).
4. **Graceful edge-case handling:** Safely handles at least one boundary condition—such as an empty input, an input that exceeds the context window, or a prompt outside the model's domain—without crashing or hanging indefinitely.

## 6. Suggested 2-minute demo scenario

When presenting your offline project to judges, follow this demo script:

- **0:00 – 0:30 (The Disconnect & Proof):** State the problem and target user. Open your operating system's network settings and **toggle Wi-Fi completely OFF** in front of the judges.
- **0:30 – 1:15 (Standard Flow):** Launch your application locally. Submit a realistic input (e.g., "Patient reports sudden high fever and joint pain in a remote area without hospital access; what are the initial triage steps?"). Show Gemma generating the response locally in real time.
- **1:15 – 1:45 (Edge Case):** Submit an edge case (e.g., an empty string, gibberish input, or an excessively long prompt). Show that the app handles it cleanly with a helpful error message instead of crashing.
- **1:45 – 2:00 (Architecture & Footprint):** Open terminal / task manager briefly to show the active local process (e.g. `ollama` or `llama.cpp`), stating the exact quantized model format and memory footprint (RAM/VRAM).

## 7. Required repository & README evidence

Your public GitHub repository must include:
- [ ] A `README.md` with:
  - Clear user problem statement, target audience, and explicit declaration of this track as your team's primary iTech Club challenge track.
  - Exact local Gemma model variant used (e.g. `gemma-2-2b-it` or quantized GGUF tag) and parameter count.
  - Model runtime used (Ollama, llama.cpp, LiteRT-LM, etc.) and acknowledgment of the [Gemma Terms of Use](https://ai.google.dev/gemma/terms).
  - Approximate disk space and RAM required to run the model.
  - Step-by-step cold-start instructions to pull weights and start the application locally.
  - Disclosure of any AI pair-programming tools used during development.
- [ ] Working source code (CLI script or local web server).
- [ ] An OSI-approved open-source `LICENSE` file.

{: .important }
> **Pre-download warning:** Download your model weights and Python dependencies **at home before the hackathon starts**. Do not rely on venue Wi-Fi on the night of the event to download gigabytes of model checkpoints.

## 8. Stretch goals (optional)

These optional enhancements will distinguish advanced entries but are **not** required to pass:
- **Local persistence:** Store conversation logs or collected field reports in a local SQLite database or JSON file on disk.
- **Quantization tuning:** Benchmark and compare inference speed between 4-bit quantized (Q4_K_M) and 8-bit quantized weights on CPU.
- **Lightweight local UI:** Build a responsive terminal TUI (using `rich` or `textual`) or a clean local web interface (using Streamlit, Gradio, or vanilla HTML/JS).
- **Audio/Voice output:** Add local offline text-to-speech (TTS) or voice input for accessibility in field settings.

## 9. Starter resources

- [Ollama Gemma Integration Guide](https://ai.google.dev/gemma/docs/integrations/ollama) — Running small Gemma models locally with one command
- [llama.cpp Integration Guide](https://ai.google.dev/gemma/docs/integrations/llamacpp) — High-performance C/C++ CPU/GPU local inference
- [LM Studio Integration](https://ai.google.dev/gemma/docs/integrations/lmstudio) — Local desktop GUI runner for quick prompt testing
- [LiteRT-LM Overview](https://ai.google.dev/edge/litert-lm/overview) — Google's lightweight edge runtime for mobile and embedded devices
- [Gemma 4 Model Overview](https://ai.google.dev/gemma/docs/core) — Specifications and memory requirements for lightweight models

## 10. Privacy, safety & licensing

- **Open-source software license:** Your application code must be published under an OSI-approved open-source license (such as MIT, Apache-2.0, or GPL-3.0).
- **Model terms:** Gemma weights are released under open-weight terms—specifically the [Gemma Terms of Use](https://ai.google.dev/gemma/terms)—rather than traditional software licenses. Comply with these terms when redistributing checkpoints or quantized weights.
- **Inherent privacy advantage:** Running 100% locally means user prompts never leave the device. Highlight this privacy benefit if handling sensitive health or personal field data.
- **Safety disclaimers:** If your app addresses medical, health, or legal triage, include a clear user-facing disclaimer stating that the model provides informational assistance and does not replace certified professional care.

## 11. Challenge-specific evaluation notes

These notes guide judges when assessing projects in this track against the general 100-point rubric in [`judging.md`]({{ site.baseurl }}/judging/). They do not constitute bonus points or separate scoring categories:

- **What the team must demonstrate (under Technical Execution):** The live demo MUST be conducted with all network interfaces (Wi-Fi, Ethernet, and mobile hotspot) completely disabled in front of judges. The user workflow must run end-to-end on local compute, ingesting an input and streaming/displaying model output with zero connectivity.
- **What evidence judges should inspect (under Technical Execution & Open-Source Quality):** Inspect disabled external adapters, cached weights, local runtime activity and measured RAM use. Local loopback sockets are permitted. README instructions must state hardware, quantization, test input, output length and measured end-to-end latency so the under-30-second baseline can be checked on the demonstrated device, not assumed from CPU specifications.
- **What constitutes a working implementation:** A software build that launches and executes Gemma inference on local hardware without remote dependencies. A hosted fallback fails the offline check; use that evidence with the general Technical Execution anchors, without an extra fixed penalty.
- **How Gemma must contribute to the solution (under Meaningful Gemma Integration):** A local quantized Gemma model (e.g. Gemma 4 E2B, Gemma 2 2B) must actively generate the diagnostic, analytical, or generative response. Hardcoded lookup tables, regex scripts, or static canned outputs fail this requirement.
- **Relevant limitations and safety considerations (under Responsible AI & Safety):** Teams must highlight the inherent privacy advantages of local on-device processing for sensitive data. If the app addresses health, legal, or crisis triage, an explicit user disclaimer must state that the model provides informational assistance, not professional care. Teams should openly state quantitative hardware limits (e.g., token generation speeds on CPU).
