---
title: Starter Kit
nav_order: 3
description: "Step-by-step setup: get Gemma running before the hack day starts."
---

# Starter Kit
{: .no_toc }

Get this done **before** you arrive—venue Wi-Fi on an overnight hack day with 50+ laptops downloading multi-gigabyte dependencies is not where you want to be running your first setup command.
{: .fs-6 .fw-300 }

1. TOC
{: toc }

---

## Quick path decision matrix

Find the setup path that matches your laptop hardware and chosen challenge track:

| If your team goal is... | Recommended Path | Setup Section | Declared iTech Club Track |
|---|---|---|---|
| **Fastest path (minimal setup, student laptop)** | Hosted Gemini API (`gemma-4-26b-a4b-it`) | [Option A](#option-a--hosted-gemma-via-the-gemini-api) | [Track 1]({{ site.baseurl }}/challenges/01-agent-skill/), [Track 3]({{ site.baseurl }}/challenges/03-multimodal-assistant/), [Track 4]({{ site.baseurl }}/challenges/04-dev-harness/), or [Track 5]({{ site.baseurl }}/challenges/05-rag-knowledge-companion/) |
| **Must work offline (no Wi-Fi/signal dependency)** | Local quantized model via Ollama (`gemma4:e2b` or `gemma2:2b`) | [Option B](#option-b--local-offline-gemma-with-ollama) | **[Track 2: Gemma Off the Grid]({{ site.baseurl }}/challenges/02-edge-offline/)** |
| **Need image or audio input** | Hosted Gemini API or local multimodal model | [Option A](#option-a--hosted-gemma-via-the-gemini-api) | **[Track 3: Multimodal Campus Companion]({{ site.baseurl }}/challenges/03-multimodal-assistant/)** |
| **Need retrieval / RAG over documents** | Hosted Gemma 4 + EmbeddingGemma 2 | [Option A & RAG](#retrieval--embeddings-with-embeddinggemma) | **[Track 5: Campus Knowledge Companion (RAG)]({{ site.baseurl }}/challenges/05-rag-knowledge-companion/)** |
| **Need custom model / tool harness control** | Function calling via Gemini API or local FunctionGemma / Ollama | [Option A](#option-a--hosted-gemma-via-the-gemini-api) or [Option C](#option-c--open-weight-checkpoints-for-custom-harnesses) | **[Track 4: Gemma-Powered Dev Harness]({{ site.baseurl }}/challenges/04-dev-harness/)** |

---

## 1. Core concepts & distinctions

Before installing packages, understand the architecture:

- **Hosted API vs. Local Inference:**
  - **Hosted API (Option A):** Model compute runs on Google's cloud servers via the Gemini API. You only send HTTP requests with an API key. This is the fastest, lowest-resource path for standard student laptops.
  - **Local Inference (Option B & C):** Model weights sit on your laptop's hard drive and execute on local CPU/GPU compute. **Mandatory for Track 2 (Offline Edge)**, but optional for all other tracks.
- **Model-Hosting Runtimes:** Tools like [Ollama](https://ollama.com) or [llama.cpp](https://github.com/ggerganov/llama.cpp) manage local weights, quantize memory, and expose local endpoints.
- **Embeddings vs. Generative Models:**
  - **Embedding models** (e.g. `EmbeddingGemma 2`) convert text, code, or images into vector numbers for search. They do *not* generate conversational text.
  - **Generative models** (e.g. `Gemma 4`, `Gemma 2`) read retrieved context and generate the final answer.
- **Gemma vs. Gemini:** This hackathon requires building with the **Gemma family** (Google's open-weight model family). Do not substitute a proprietary Gemini-branded model (such as Gemini 1.5 Pro) for Gemma.

---

## 2. Prerequisites & version checks

Check that your machine has the baseline development tools installed:

```bash
# Check Git version
git --version          # Recommended: 2.30+

# Check Python version (primary SDK language)
python3 --version      # Required: Python 3.10, 3.11, or 3.12

# Check Node.js version (if building a JavaScript/TypeScript frontend)
node -v                # Recommended: Node 18+ or 20 LTS
```

If you plan to run models locally (Option B), verify free disk space:
- Minimum **5–10 GB free disk space** for lightweight quantized models (e.g. `gemma4:e2b` or `gemma2:2b`).
- Check available disk space in terminal: `df -h .` (Linux/macOS) or File Explorer (Windows).

---

## 3. Progressive setup: Option A — Hosted Gemma via Gemini API

The hosted path is recommended for all tracks except Track 2. Google provides free-tier compute for Gemma models, requiring zero local GPU hardware.

### Step 1: Obtain your API key
1. Sign in to [Google AI Studio](https://aistudio.google.com/apikey) with your Google account.
2. Click **Create API Key**.
3. Copy the key.

### Step 2: Set up a clean project and virtual environment
Open your terminal and initialize your project folder:

```bash
mkdir my-gemma-app && cd my-gemma-app
python3 -m venv .venv

# Activate the virtual environment:
# On Linux/macOS:
source .venv/bin/activate
# On Windows (cmd):
# .venv\Scripts\activate
# On Windows (PowerShell):
# .venv\Scripts\Activate.ps1
```

### Step 3: Install the official Google GenAI SDK
Install the current, official Google GenAI SDK and `python-dotenv`:

```bash
pip install --upgrade google-genai python-dotenv
```

{: .note }
> **Package Note:** Use `google-genai` (imported as `from google import genai`). Do not use the legacy `google-generativeai` package, which has been superseded.

### Step 4: Configure secrets safely
Never commit API keys to version control. Follow this strict hygiene:

1. Create a `.gitignore` file before making any commits:
   ```bash
   cat << 'EOF' > .gitignore
   .venv/
   .env
   .env.local
   __pycache__/
   *.pyc
   node_modules/
   EOF
   ```
2. Create a safe `.env.example` template for your repository:
   ```bash
   cat << 'EOF' > .env.example
   # Copy this file to .env and fill in your real key
   GEMINI_API_KEY=your_gemini_api_key_here
   EOF
   ```
3. Create your local `.env` file containing your actual secret:
   ```bash
   echo "GEMINI_API_KEY=AIzaSyYourActualKeyHere" > .env
   ```
4. Verify `.env` is ignored by Git:
   ```bash
   git status --ignored
   # Ensure .env appears under "Ignored files", not "Untracked files"
   ```

{: .important }
> **Accidental Key Exposure:** If you ever commit an API key to GitHub, treat it as compromised immediately. Delete or rotate it at [Google AI Studio API Keys](https://aistudio.google.com/apikey).

---

## 4. Smoke test: Proving the API call works

Create a minimal script `smoke_test.py` to verify end-to-end connectivity:

```python
import os
import sys
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key or api_key == "your_gemini_api_key_here":
    print("ERROR: GEMINI_API_KEY is not set. Add your key to .env", file=sys.stderr)
    sys.exit(1)

# Initialize the GenAI client
client = genai.Client(api_key=api_key)

try:
    # Use the official hosted Gemma 4 model
    response = client.models.generate_content(
        model="gemma-4-26b-a4b-it",
        contents="Say hello to Zetech University students in exactly one sentence.",
    )
    print("=== SMOKE TEST PASSED ===")
    print("Model output:")
    print(response.text)
except Exception as e:
    print(f"ERROR: API call failed: {e}", file=sys.stderr)
    sys.exit(1)
```

Run the smoke test:

```bash
python3 smoke_test.py
```

### Expected output shape
If successful, the script exits with code `0` and prints non-empty text similar to:
```text
=== SMOKE TEST PASSED ===
Model output:
Hello students of Zetech University, welcome to the hackathon and happy building!
```

---

## 5. Option B — Local offline Gemma with Ollama

Required for **[Track 2: Gemma Off the Grid]({{ site.baseurl }}/challenges/02-edge-offline/)**, and an excellent local backup for all teams if venue connectivity drops.

### Step 1: Install Ollama
Download and install [Ollama](https://ollama.com/download) for your operating system (Linux, macOS, Windows).

### Step 2: Pre-download model weights at home
Download your chosen model **before coming to the venue**. Choose a size that matches your laptop's memory:

```bash
# Recommended for standard student laptops (approx. 1.5–2.5 GB download):
ollama pull gemma4:e2b

# Alternative lightweight option (approx. 1.6 GB download):
ollama pull gemma2:2b

# For laptops with 16 GB RAM and dedicated GPU (approx. 3.5 GB download):
ollama pull gemma4:e4b
```

### Step 3: Test local inference in terminal
Verify that inference executes locally:

```bash
ollama run gemma4:e2b "Name three key considerations for offline application design."
```

### Step 4: Python smoke test for local Ollama
You can query Ollama from Python without any extra external packages using standard `urllib`:

```python
import json
import urllib.request

url = "http://localhost:11434/api/generate"
payload = {
    "model": "gemma4:e2b",
    "prompt": "Respond with 'Local Gemma is working' and nothing else.",
    "stream": False
}

req = urllib.request.Request(
    url,
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        print("=== LOCAL SMOKE TEST PASSED ===")
        print("Model response:", result.get("response"))
except Exception as e:
    print(f"ERROR: Could not connect to local Ollama daemon: {e}")
```

{: .tip }
> **Offline Validation Test:** Turn off your Wi-Fi and rerun the script above. It should execute with zero network access.

---

## 6. JavaScript / TypeScript minimal example

If your team is building a Node.js backend or web application, install the official package:

```bash
npm install @google/genai dotenv
```

Create `test_gemma.mjs`:

```javascript
import { GoogleGenAI } from "@google/genai";
import dotenv from "dotenv";

dotenv.config();

const apiKey = process.env.GEMINI_API_KEY;
if (!apiKey) {
  console.error("ERROR: GEMINI_API_KEY is not set in .env");
  process.exit(1);
}

const ai = new GoogleGenAI({ apiKey });

try {
  const response = await ai.models.generateContent({
    model: "gemma-4-26b-a4b-it",
    contents: "Respond in 10 words: What is open-source software?",
  });
  console.log("=== JS SMOKE TEST PASSED ===");
  console.log(response.text);
} catch (error) {
  console.error("API error:", error);
  process.exit(1);
}
```

Run with: `node test_gemma.mjs`

---

## 7. Model hardware requirements & sizing guide

Memory requirements vary significantly depending on **quantization format**, **runtime overhead**, and **workload context length**. Below is Google's official baseline memory reference:

### Gemma 4 approximate memory requirements (Official Reference)

| Model Size | Parameters | Unquantized BF16 | 8-bit (SFP8) | 4-bit (Q4_0) | Mobile (LiteRT-LM) | Recommended Target Hardware |
|---|---|---|---|---|---|---|
| **E2B** | ~2B effective | 11.4 GB | 5.7 GB | **2.9 GB** | 1.1 GB (0.84 GB text) | Standard student laptop (4–8 GB RAM), CPU or mobile |
| **E4B** | ~4B effective | 17.9 GB | 8.9 GB | **4.5 GB** | 2.5 GB (2.2 GB text) | Consumer laptop (8–16 GB RAM), CPU or integrated GPU |
| **12B Unified** | 12B multimodal | 26.7 GB | 13.4 GB | **6.7 GB** | — | Workstation laptop (16 GB RAM) or consumer GPU (8 GB VRAM) |
| **26B A4B (MoE)**| 26B (4B active) | 57.7 GB | 28.8 GB | **14.4 GB** | — | High-end workstation (24 GB VRAM / 32 GB Unified RAM) or **Gemini API** |
| **31B** | 31B dense | 69.9 GB | 34.9 GB | **17.5 GB** | — | Workstation GPU (24 GB VRAM) or **Gemini API** |

{: .note }
> **Key Takeaway for Students:** You do **not** need expensive GPU workstations. If your laptop has 4–8 GB RAM, use the **free hosted Gemini API** (`gemma-4-26b-a4b-it`) or run **`gemma4:e2b` / `gemma2:2b` locally in 4-bit quantization** on your CPU.

---

## 8. Option C — Open-weight checkpoints for custom harnesses

Needed only if you are downloading raw weights for fine-tuning, Hugging Face Transformers, or custom llama.cpp harnesses:

- **Hugging Face Hub:** [huggingface.co/collections/google/gemma-4](https://huggingface.co/collections/google/gemma-4)
- **Kaggle Models:** [kaggle.com/models?query=gemma-4&publisher=google](https://www.kaggle.com/models?query=gemma-4&publisher=google)
- **Lightweight GGUF weights:** Look for community or official GGUF weights tagged with `Q4_K_M` or `Q4_0` to run locally via `llama.cpp` or LM Studio.

---

## 9. Common troubleshooting

| Error / Symptom | Likely Cause | Fix |
|---|---|---|
| `ValueError: GEMINI_API_KEY is not set` | Script did not find API key in environment or `.env` | Ensure `.env` exists in working directory and contains `GEMINI_API_KEY=...`, and verify `load_dotenv()` was called. |
| `HTTP 403 Forbidden` / `API_KEY_INVALID` | API key was copied with extra spaces or revoked | Re-generate key at [Google AI Studio](https://aistudio.google.com/apikey) and re-paste into `.env`. |
| `HTTP 429 RESOURCE_EXHAUSTED` | Exceeded free-tier per-minute rate limits | Add a short sleep delay (`time.sleep(2)`) between requests or retry with exponential backoff. |
| `HTTP 404 NOT_FOUND` (Model ID) | Misspelled model string | Verify exact model string: use `gemma-4-26b-a4b-it` or `gemma-4-31b-it`. |
| `CUDA out of memory` / Process killed (OOM) | Local model exceeded available system RAM or VRAM | Switch to a smaller quantized model (e.g. `gemma4:e2b` instead of 12B/31B) or use the hosted API. |
| Ollama download stalled / partial weights | Interrupted network connection during `ollama pull` | Re-run `ollama pull <model-tag>`; Ollama automatically resumes from the last completed layer. |

---

## 10. Repository scaffolding checklist

Scaffold your repo cleanly during the first 30 minutes of the event:

```bash
mkdir my-team-project && cd my-team-project
git init

# Download an OSI-approved license (e.g. MIT)
curl -sL https://raw.githubusercontent.com/github/choosealicense.com/gh-pages/_licenses/mit.txt -o LICENSE

# Create essential files
touch README.md .env.example
echo "GEMINI_API_KEY=your_key_here" > .env.example

# Set up .gitignore BEFORE committing
cat << 'EOF' > .gitignore
.venv/
.env
.env.local
__pycache__/
*.pyc
EOF

git add -A
git commit -m "Initial commit: scaffold project with license and gitignore"
```

Now head to the [Challenges]({{ site.baseurl }}/challenges/) page and start building!
