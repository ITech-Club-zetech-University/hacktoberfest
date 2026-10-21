# [Project Name]

> [One-sentence summary: What does your application do, who is it for, and what real campus or developer problem does it solve?]

---

## 1. Primary Challenge Track

- **Declared Primary Track:** [Select exactly ONE: Track 1: Build a Gemma Agent Skill | Track 2: Gemma Off the Grid | Track 3: Multimodal Campus Companion | Track 4: Gemma-Powered Dev Harness | Track 5: Campus Knowledge Companion (RAG)]
- **Why this track was chosen:** [1–2 sentences explaining why this challenge track fits your team's solution]

---

## 2. Problem Statement & Intended Users

- **Target Audience:** [e.g. Zetech University CS students, campus lab technicians, iTech Club open-source maintainers, commuter students]
- **The Problem:** [Describe the specific, real-world friction or bottleneck your project addresses]
- **Why Existing Tools Fall Short:** [Why generic chat bots or standard manual processes are insufficient]

---

## 3. What We Built During the Hackathon

- **Summary of Implementation:** [Describe the application logic, user interface (CLI, web, or mobile), and workflow built during the ~8-hour build window]
- **Key Features:**
  - Feature 1: [Description]
  - Feature 2: [Description]
  - Feature 3: [Description]
- **What Was Built Fresh:** [All code written between Friday 7:00 PM and Saturday 5:00 AM EAT]
- **What Was Pre-existing / Upstream:** [Any boilerplate, starter libraries, or open-source repositories forked]

---

## 4. How Gemma is Used & Why It Is Central

- **Why Gemma is Indispensable:** [Would the product function if Gemma were removed? Explain why Gemma's reasoning, perceptual capability, or structured outputs are essential to the core value proposition.]
- **Model Role in Architecture:** [e.g. Cognitive reasoning engine, multimodal image analyzer, structured tool-call dispatcher, or retrieval synthesizer]
- **Prompting / Tool Design:** [Describe system prompts, temperature settings, function schemas, or context formatting used]

---

## 5. Model Specifications & Inference Path

- **Exact Model & Version:** [e.g. `gemma-4-26b-a4b-it`, `gemma-4-31b-it`, `gemma4:e2b`, `gemma4:e4b`, `gemma2:2b`, `EmbeddingGemma 2 (740M)`]
- **Inference Path:** [Select one: Hosted via Google Gemini API | Local on-device via Ollama | Local via llama.cpp | Local via LiteRT-LM]
- **Hardware Footprint (if run locally):** [e.g. 4-bit quantized Q4_0, ~2.9 GB RAM utilized, tested on student laptop with 8 GB RAM / CPU-only]

---

## 6. Other Models, Services & Dependencies

- **Secondary Models (if applicable):** [e.g. `EmbeddingGemma 2` for retrieval embeddings, `ShieldGemma 2` for safety filtering]
- **Runtime & Language Stack:** [e.g. Python 3.11, Node.js 20, FastAPI, React/Vite]
- **Key Dependencies:**
  - `google-genai` (v1.0+) or `@google/genai`
  - [List other key packages from requirements.txt or package.json]

---

## 7. Setup & Cold-Start Instructions

Follow these step-by-step commands to clone, configure, and launch the project from scratch.

### Prerequisites
- Python 3.10+ (or Node.js 18+)
- [Ollama installed if running locally](https://ollama.com)
- Git

### Installation
```bash
# 1. Clone the repository
git clone https://github.com/[your-org-or-username]/[your-repo-name].git
cd [your-repo-name]

# 2. Set up virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Environment Configuration
Never commit your real API key to version control. Copy the example environment file:
```bash
cp .env.example .env
```

Edit `.env` with your editor:
```env
# Required for hosted Gemini API inference
GEMINI_API_KEY=your_gemini_api_key_here

# Required for local Ollama inference (if applicable)
OLLAMA_HOST=http://localhost:11434
```

### Running the Application
```bash
# Example run command (CLI or web server)
python3 main.py
# Or: npm run dev
```

---

## 8. Safe `.env.example` Template

*(Include this exact format in a `.env.example` file in your repository root with placeholder values only)*:

```env
# Google Gemini API key for Gemma inference (get from Google AI Studio / MLH Quickstart)
GEMINI_API_KEY=your_api_key_here

# Optional: Host address for local Ollama daemon
OLLAMA_HOST=http://localhost:11434

# Application port
PORT=8000
```

---

## 9. Live Demo Instructions & Known Limitations

### Step-by-Step Demo Flow (2 Minutes)
1. **The Setup (0:00–0:30):** [Show launching the app and explain the target user problem]
2. **Core Gemma Workflow (0:30–1:30):** [Input realistic test data; observe Gemma generating response]
3. **Challenge Acceptance Test (1:30–2:00):** [Demonstrate the specific requirement matching your declared primary track: Wi-Fi toggled off for Track 2, SKILL.md invocation for Track 1, image upload for Track 3, bounded tool confirmation for Track 4, or dynamic chunk citation for Track 5]

### Known Limitations & Incomplete Features
- **Limitation 1:** [e.g. Local inference token rate is ~8 tokens/sec on CPU]
- **Limitation 2:** [e.g. UI is currently CLI-based; responsive web interface remains a future roadmap item]
- **Limitation 3:** [e.g. Corpus currently contains 12 documents; larger corpus ingestion needs batch indexing]

---

## 10. Acceptance Criteria & Test Evidence

| Acceptance Test (from Challenge Page) | Verification Command or Action | Result |
|---|---|---|
| Test 1: [e.g. SKILL.md frontmatter matches directory] | `head -n 10 my-skill/SKILL.md` | PASS |
| Test 2: [e.g. Live offline inference with Wi-Fi disabled] | Wi-Fi toggled off, `python3 main.py` | PASS |
| Test 3: [e.g. Bounded tool schema validation] | `python3 -m unittest tests/` | PASS |
| Test 4: [e.g. Out-of-corpus query refusal] | Input: "Who won the 1990 world cup?" | PASS (Graceful refusal) |

---

## 11. Data Sources & Permission Evidence

- **Corpus / Dataset Origin:** [e.g. Synthetic course syllabus generated by our team, public Zetech University club constitution, open-source documentation]
- **Privacy Assurance:** **No private student records, grades, admission numbers, personal phone numbers, or confidential faculty emails are included in this repository.**
- **Permission Evidence:** [e.g. Public domain data, creative commons documentation, or synthetic mock data created during the hackathon]

---

## 12. Safety, Boundary & Privacy Considerations

- **Safety Guardrails:** [Describe how input validation, system prompts, or ShieldGemma prevent hallucinations or misuse]
- **Tool Bounding (if Track 4 / Agents):** [Explicit confirmation prompt required before any file write or command execution; no arbitrary shell execution]
- **Data Privacy:** [Inference prompts do not retain user PII; local edge inference keeps all data on-device]

---

## 13. Team Member Contributions

This project was built by a team of [3–4] members during the Hacktoberfest Hack Day Nairobi window:

| Team Member Name | GitHub Username | Role & Contributions |
|---|---|---|
| [Member 1] | `@[username]` | Model integration, prompt architecture, and Gemini API / Ollama setup |
| [Member 2] | `@[username]` | Application logic, backend API endpoints, and data processing |
| [Member 3] | `@[username]` | Frontend user interface, demo workflow, and testing |
| [Member 4] | `@[username]` | Open-source licensing, README documentation, and edge-case handling |

*Note: All team members understand the entire codebase and are prepared to explain architecture and prompts during the live demo.*

---

## 14. AI-Assisted Coding Tools Disclosure

In compliance with hackathon rules, we disclose the AI pair-programming tools used during development:

- **AI Tools Used:** [e.g. GitHub Copilot, Gemini CLI, Claude Code, Cursor, None]
- **How Tools Were Used:** [e.g. Autocompleting boilerplate dataclass definitions, generating initial regex patterns, drafting test assertions]
- **Our Original Contribution:** [e.g. Our team designed the system architecture, authored the domain-specific prompts, integrated the Gemma model loop, and implemented the tool boundary logic from scratch. Every line of code was reviewed, tested, and is understood by the team.]

---

## 15. Upstream Attribution (If Forked or Built on Existing Code)

*(If your team built from scratch, delete this section or state: "Built 100% from scratch during the hackathon window.")*

- **Upstream Repository:** [Link to original upstream repository]
- **Upstream Author & License:** [Original author name, upstream OSI license e.g. MIT]
- **Substantial Delta Built During Hackathon:** [Describe the concrete new logic, adapters, tools, or UI added by your team overnight]
- **Clean Git Diff:** [Provide a link to the commit history or diff showing your team's contributions]

---

## 16. Licensing & Model Terms

- **Application Source Code License:** This project is open-source software licensed under the **[MIT License / Apache 2.0 License]** — see the [`LICENSE`](./LICENSE) file at repository root.
- **AI Model Terms of Use:** The underlying AI model weights are governed separately:
  - Generative Gemma models (Gemma 4, Gemma 2, FunctionGemma) are governed by the [Gemma Terms of Use](https://ai.google.dev/gemma/terms).
  - Embedding models (EmbeddingGemma 2) are governed by the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).
