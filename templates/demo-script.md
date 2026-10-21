# 2–3 Minute Live Demo Script Template

This guide provides a time-boxed, structured script for presenting your hackathon project to the judge panel during the live demo session (5:00–5:45 AM EAT).

{: .important }
> **No Slide Decks Required:** Judges want to see working software running live on screen, not pitch decks or pre-rendered marketing videos. Live execution, honest explanations of limitations, and deep code comprehension will score far higher than polished slides.

---

## Universal 2.5-Minute Demo Flow

| Timing | Phase | What to Say and Show |
|---|---|---|
| **0:00 – 0:30** (30s) | **Problem & Target User** | State the problem in one sentence, introduce your team, and declare your **single primary iTech Club challenge track**. |
| **0:30 – 0:50** (20s) | **Gemma's Exact Role** | State exactly what Gemma does, which model variant is running, and whether inference is hosted (Gemini API) or local (Ollama). |
| **0:50 – 1:35** (45s) | **Core Live Workflow** | Run a standard, normal end-to-end use case live. Show inputs, model processing, and the generated output on screen. |
| **1:35 – 2:05** (30s) | **Track Acceptance Test** | Demonstrate the specific observable acceptance test matching your declared track (see track scenarios below). |
| **2:05 – 2:25** (20s) | **Limitation & Safe Fallback** | Demonstrate an intentional edge case, failure state, or graceful fallback. Be completely honest about what doesn't work yet. |
| **2:25 – 2:45** (20s) | **What We Built vs. Incomplete** | Summarize the substantial code written overnight vs. roadmap items, and open the floor for judge Q&A (1 minute). |

---

## Track-Specific Demonstration Scenarios

Prepare your live demo to hit the exact acceptance checks for your declared primary track:

### Track 1: Build a Gemma Agent Skill
- **The Pitch:** *"We built an Agent Skill for CS students and club contributors that automates Python assignment feedback according to the Agent Skills open standard, powered by Gemma."*
- **Gemma's Role:** Gemma reasons over student code to evaluate logical bugs and style deviations against rubric instructions.
- **Core Workflow:**
  1. Open the project folder in terminal or code editor.
  2. Show `my-skill/SKILL.md` frontmatter (`name: code-rubric-reviewer`, clear description).
  3. Run the driver command or invoke from an agent: `python3 test_skill.py examples/student_submission.py`.
  4. Show Gemma outputting structured, constructive feedback.
- **Track Acceptance Check:** Show that the directory name matches the `SKILL.md` frontmatter name, and that execution fails gracefully if Gemma is unavailable.
- **Honest Limitation:** *"The skill currently only evaluates single-file Python scripts; multi-file repository parsing is a future milestone."*

### Track 2: Gemma Off the Grid
- **The Pitch:** *"We built an offline medical triage notes assistant for rural clinics with unreliable connectivity, running Gemma 100% locally on a student laptop."*
- **Gemma's Role:** Gemma 4 E2B (or Gemma 2 2B) running via Ollama locally parses patient symptom notes and extracts structured triage categories.
- **Core Workflow:**
  1. **In front of judges, toggle Wi-Fi and mobile data completely OFF.**
  2. Launch your CLI or web app pointing to `http://localhost:11434`.
  3. Submit a clinical symptom memo: *"Patient aged 24 presents with acute fever for 3 days and dry cough."*
  4. Observe Gemma generating triage notes locally in ~3 seconds.
- **Track Acceptance Check:** Open terminal process monitor (`top` or Activity Monitor) showing zero network I/O and local CPU/GPU RAM utilization.
- **Honest Limitation:** *"Because we are running 4-bit quantized weights on a CPU without a GPU, generation speed is ~8 tokens per second."*

### Track 3: Multimodal Campus Companion
- **The Pitch:** *"We built a campus notice-board reader that allows visually impaired or busy students to photograph physical campus signs and hear or read an instant explanation."*
- **Gemma's Role:** Gemma (via Gemini API multimodal endpoint) directly perceives the image tokens without third-party OCR, understanding layout and context.
- **Core Workflow:**
  1. Upload or drag-and-drop a sample photo of a messy whiteboard or handwritten campus notice from `examples/`.
  2. Prompt: *"What is the deadline for submitting the lab assignment, and where should it be handed in?"*
  3. Show Gemma providing a grounded, accurate answer directly from the photo.
- **Track Acceptance Check:** Upload a second, different test image (e.g. a campus map or lab circuit) to prove that responses dynamically reflect the input image, not hardcoded text.
- **Honest Limitation:** *"Images taken in extreme low light or with severe glare sometimes result in lower confidence responses."*

### Track 4: Gemma-Powered Dev Harness
- **The Pitch:** *"We built a bounded developer harness that enables Gemma to inspect Git repositories, run unit tests, and safely propose bug fixes."*
- **Gemma's Role:** Gemma dynamically selects tool calls with structured JSON arguments based on developer requests.
- **Core Workflow:**
  1. Prompt: *"Run the test suite and summarize failing test cases."*
  2. Show the harness executing the bounded test runner tool and feeding output back to Gemma.
  3. Prompt: *"Fix the bug in `calculator.py`."*
  4. **Highlight the Safety Boundary:** The harness prompts the user: *"Gemma wants to modify `calculator.py`. Do you approve this file write? [y/N]"*.
- **Track Acceptance Check:** Show code preventing arbitrary shell execution (`os.system` is rejected; tools are strictly whitelisted).
- **Honest Limitation:** *"The harness does not yet support multi-step autonomous loops; it requires human confirmation for each write action."*

### Track 5: Campus Knowledge Companion (RAG)
- **The Pitch:** *"We built a verifiable knowledge assistant for Zetech University students that answers club and academic questions strictly grounded in public club documents with clickable citations."*
- **Gemma's Role:** `EmbeddingGemma 2` retrieves semantic chunks; Gemma generates the final synthesis citing exact document sections.
- **Core Workflow:**
  1. Query: *"What is the procedure for joining the iTech Club executive committee?"*
  2. Show dynamic retrieval returning top 2 chunks from `corpus/constitution.md` with similarity scores.
  3. Show Gemma's response with explicit citations: `[Source: constitution.md#section-4]`.
- **Track Acceptance Check (Out-of-Corpus Refusal):** Query: *"Who won the 1994 FIFA World Cup?"*  
  Show the system responding honestly: *"I cannot find information about the 1994 World Cup in the provided campus documents"* (proves grounding and absence of hallucination).
- **Honest Limitation:** *"Our vector store is currently in-memory; scaling beyond 1,000 documents will require an external vector database like Chroma or Qdrant."*

---

## 1-Minute Judge Q&A Preparation

Judges will ask 1–2 technical questions. Be prepared to answer:
1. **"Can you show me the exact code where Gemma is called?"**  
   *(Have the file open in your editor and know the line numbers).*
2. **"What happens if the model output is malformed or invalid?"**  
   *(Explain your try/catch logic, schema validation, or fallback behavior).*
3. **"Which AI coding tools did you use, and what did your team write yourselves?"**  
   *(Answer candidly: point to the architecture, prompt engineering, and custom logic).*
4. **"Why did you choose this specific model size and runtime?"**  
   *(Explain your laptop hardware constraints, memory footprint, or response latency considerations).*
