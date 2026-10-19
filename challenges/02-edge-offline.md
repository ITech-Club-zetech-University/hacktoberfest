---
title: "2. Gemma Off the Grid"
parent: Challenges
nav_order: 2
description: "Build an edge application that runs Gemma entirely on-device, with zero network connectivity required at runtime."
---

# Challenge 2: Gemma Off the Grid
{: .no_toc }

**Track focus:** On-device edge inference & offline-first design · **Target window:** ~8 hours · **Team size:** 3–4
{: .fs-5 .fw-300 }

1. TOC
{: toc }

---

## 1. Pitch & target user

In many regions across Kenya and sub-Saharan Africa, dependable high-speed internet is neither guaranteed nor affordable. From rural clinics and field research stations to campus computer labs during power outages or packed venue Wi-Fi networks, real people need intelligent tools that work completely disconnected from the cloud. In this track, your team builds a working, practical application where **Gemma runs 100% locally on-device**.

- **Target user:** Field healthcare workers, agricultural extension officers, rural students with limited data bundles, or anyone operating in environments where cloud APIs are unavailable, costly, or unreliable.
- **The golden rule:** A cloud API call to Google AI Studio, OpenAI, or any remote server is **strictly disqualified** from being presented as offline inference. The model weights must sit on your local hard drive and execute on local compute.

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
- **How judges inspect it:** Judges will ask you to **turn off your laptop's Wi-Fi and Bluetooth live**. You will launch the app, enter a prompt, and observe the model generating tokens. Judges will verify via local process monitoring (such as `top`, Activity Monitor, or Ollama CLI status) that inference is happening locally on your hardware with zero outgoing network packets.

## 5. Mandatory acceptance criteria

Every valid entry in this track must pass these four observable tests:

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
- [Gemma 2 Model Overview](https://ai.google.dev/gemma/docs/core) — Specifications and memory requirements for lightweight models

## 10. Privacy, safety & licensing

- **Open-source software license:** Your application code must be published under an OSI-approved open-source license (such as MIT, Apache-2.0, or GPL-3.0).
- **Model terms:** Gemma weights are released under open-weight terms—specifically the [Gemma Terms of Use](https://ai.google.dev/gemma/terms)—rather than traditional software licenses. Comply with these terms when redistributing checkpoints or quantized weights.
- **Inherent privacy advantage:** Running 100% locally means user prompts never leave the device. Highlight this privacy benefit if handling sensitive health or personal field data.
- **Safety disclaimers:** If your app addresses medical, health, or legal triage, include a clear user-facing disclaimer stating that the model provides informational assistance and does not replace certified professional care.

## 11. Challenge-specific evaluation notes

These notes supplement the 100-point rubric in [`judging.md`]({{ site.baseurl }}/judging/):
- **Live offline verification (under Technical Execution):** The live demo MUST be conducted with network adapters turned off. Any attempt to query remote hosted endpoints will result in disqualification from this specific track.
- **Hardware realism (under Problem & Impact):** Judges evaluate whether the project runs on realistic, accessible hardware (standard laptop CPU/RAM). Teams running smaller quantized models efficiently on student laptops will score just as high as teams with high-end GPUs.
