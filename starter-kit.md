---
title: Starter Kit
nav_order: 3
description: "Step-by-step setup: get Gemma running before the hack day starts."
---

# Starter Kit
{: .no_toc }

Get this done **before** you arrive — venue Wi-Fi on an overnight hack day with 50+ laptops downloading multi-gigabyte model weights is not where you want to be doing your first `pip install`.
{: .fs-6 .fw-300 }

1. TOC
{: toc }

---

## 1. Prerequisites checklist

Bring a laptop with the following installed. Tick these off before 30 Oct:

- [ ] **Git** and a **GitHub account** ([github.com](https://github.com/join))
- [ ] **Python 3.10+** (`python3 --version`) — most Gemma tooling is Python-first
- [ ] **Node.js 18+**, if your track needs a web frontend
- [ ] A code editor (VS Code, or your preferred one)
- [ ] You've **registered and checked the event page** on [MLH OrganizerHQ](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club)
- [ ] You've read the [Rules]({{ site.baseurl }}/rules/) and picked a [Challenge]({{ site.baseurl }}/challenges/) (or shortlisted 2)
- [ ] At least **10 GB free disk space** if you plan to run Gemma locally (small variants are a few GB; see sizing table below)

## 2. Pick how you'll run Gemma

There are three realistic paths. Most teams should set up **both** Option A and Option B — use the API when you have signal, fall back to local when you don't.

### Option A — Gemma via the Gemini API (fastest to start, needs internet)

1. Go to [Google AI Studio](https://aistudio.google.com) and sign in with a Google account.
2. Create an **API key**.
3. Follow the official [Run Gemma with the Gemini API quickstart](https://mlh.link/gemma-quickstart) to make your first call.
4. Store your key as an environment variable — **never commit it to your repo**:
   ```bash
   export GEMINI_API_KEY="your-key-here"
   ```
5. Add a `.env` file to your project for local secrets, and add `.env` to `.gitignore` immediately — before your first commit.

### Option B — Gemma 4 running locally with Ollama (works offline, good backup)

Best for the **[Gemma Off the Grid]({{ site.baseurl }}/challenges/02-edge-offline/)** challenge, and as a safety net if venue Wi-Fi gets congested.

1. Install [Ollama](https://ollama.com/download).
2. Pull a small Gemma 4 variant (E2B is the lightest — download this at home, not at the venue):
   ```bash
   ollama pull gemma4:e2b
   # or, for a bit more capability:
   ollama pull gemma4:e4b
   ```
3. Test it:
   ```bash
   ollama run gemma4:e2b "Give me 3 ideas for an offline campus assistant."
   ```
4. Call it from Python with the `ollama` package, or hit its local OpenAI-compatible endpoint at `http://localhost:11434`.

Prefer a GUI? [LM Studio](https://ai.google.dev/gemma/docs/integrations/lmstudio) works the same way and is friendlier for quick prompt testing.

### Option C — Hugging Face / Kaggle weights (for fine-tuning or custom harnesses)

Needed for the **[Gemma-Powered Dev Harness]({{ site.baseurl }}/challenges/04-dev-harness/)** and **[Build an Agent Skill]({{ site.baseurl }}/challenges/01-agent-skill/)** tracks if you want to run Gemma yourself rather than through the Gemini API.

1. Create accounts on [Hugging Face](https://huggingface.co/) and/or [Kaggle](https://www.kaggle.com/).
2. Browse available checkpoints: [Gemma 4 on Hugging Face](https://huggingface.co/collections/google/gemma-4) · [Gemma 4 on Kaggle](https://www.kaggle.com/models?query=gemma-4&publisher=google).
3. For quantized, laptop-friendly weights, look for the `-qat-q4_0-gguf` checkpoints — they run on CPU/consumer GPU via `llama.cpp` or LM Studio.
4. Full setup and inference examples: [ai.google.dev/gemma/docs/get_started](https://ai.google.dev/gemma/docs/get_started).

### Which Gemma 4 size should you use?

{: .note }
> Gemma 4 ships as 5 sizes. "SLM" and "LLM" below follow MLH's own definition for this challenge: **10B parameters or fewer = small (SLM)**, **more than 10B = large (LLM)**.

| Size | Class | Good for | Runs on |
|---|---|---|---|
| E2B | SLM | Ultra-light, on-device, fast iteration | Laptop CPU, phone |
| E4B | SLM | A step up in quality, still edge-friendly | Laptop CPU/GPU, phone |
| 12B | LLM | Multimodal "Unified" model (text, image, audio in one) | Single consumer GPU |
| 26B A4B | LLM | Mixture-of-experts, fast high-throughput reasoning | Single 24–48 GB GPU |
| 31B | LLM | Dense, highest quality, best for fine-tuning | Single 80 GB GPU (H100-class) or API |

If you don't have a beefy GPU, use **E2B/E4B locally** or the **larger sizes through the Gemini API**, where Google hosts the compute for you.

## 3. Scaffold your repository

Do this in the first 15 minutes of hacking, not the last 15 minutes before submission:

```bash
mkdir my-team-project && cd my-team-project
git init
# Pick a license — see Rules → Submission for the list of OSI-approved choices
curl -sL https://raw.githubusercontent.com/github/choosealicense.com/gh-pages/_licenses/mit.txt -o LICENSE
touch README.md .gitignore
echo ".env" >> .gitignore
echo "__pycache__/" >> .gitignore
git add -A && git commit -m "Initial commit"
gh repo create <your-team-name>-<challenge-slug> --public --source=. --push
```

Your `README.md` should answer, from the top: what the project does, which Gemma model/variant you used, which challenge you're entering, how to run it, and who built it. See the [submission checklist]({{ site.baseurl }}/judging/#automated-eligibility-check) — judges and the automated checker both look for this.

## 4. Go build

Head to the [Challenges]({{ site.baseurl }}/challenges/) page, pick your track, and check that track's specific requirements and starter links. Each challenge page links straight to the relevant Gemma Cookbook notebook or guide to fork from.

## Where to get help

- **At the venue**: flag a mentor — that's what they're there for.
- **Official docs**: start at the [Resources]({{ site.baseurl }}/resources/) page.
- **Community**: the [Gemma Discord](https://ai.google.dev/gemma/docs/discord) and the [Gemma developer forum](https://discuss.ai.google.dev/c/gemma/10).
- **Stuck on rules or submissions**: ask an organizer, or see the [FAQ]({{ site.baseurl }}/faq/).
