# Hack Day Submission Checklist

Copy this checklist into your team repository's `README.md` or a tracking GitHub Issue, and check off every box before the **5:00 AM EAT** submission deadline.

---

## 1. Repository & Baseline Eligibility

- [ ] **Public Repository**: Repository is set to public on GitHub before 5:00 AM EAT.
- [ ] **Open-Source Software License**: An OSI-approved license (`LICENSE` file at repo root, e.g., MIT, Apache-2.0, or GPL-3.0) for your application source code.
- [ ] **Open-Weight Model Terms**: The `README.md` documents which Gemma model/variant was used and acknowledges the [Gemma Terms of Use](https://ai.google.dev/gemma/terms).
- [ ] **Clear README.md** (Use our copy-and-fill [Project README Template](./project-readme-template.md)):
  - [ ] 2–3 sentence overview of what the project does and who it serves.
  - [ ] Declared **single primary iTech Club challenge track** (Track 1, 2, 3, 4, or 5).
  - [ ] Specific Gemma model/variant used and how it runs (e.g., Gemma 4 26B A4B via Gemini API, or Gemma 4 E2B / Gemma 2 2B via Ollama).
  - [ ] Step-by-step cold-start installation and run instructions that judges can test.
  - [ ] Team members and role contributions (teams of 3–4 for local award eligibility).
  - [ ] **AI Coding Tools Disclosure**: Proportionate short list under `AI Tools Used` (e.g. GitHub Copilot, Gemini CLI) with a 1–2 sentence explanation of your team's original contribution.
- [ ] **No Committed Secrets**: No API keys (`GEMINI_API_KEY`), credentials, or tokens committed anywhere in git history (`git log -p | grep -i key`).
- [ ] **Automated Hygiene Check**: Ran `python3 scripts/check_submission.py <repo-url>` with outcome `ELIGIBLE (PASS)`. (If flagged as `NEEDS MANUAL REVIEW`, resolve with organizers before 5:00 AM).

---

## 2. Challenge-Specific Acceptance Criteria

Complete the section matching your declared **primary** iTech Club challenge track. These checks provide direct evidence for judges evaluating **Technical execution & working demo** (0–25) and **Use of Gemma** (0–25) on the [100-Point Rubric]({{ site.baseurl }}/judging/#the-100-point-score-sheet) (they are not hidden bonus points):

### Track 1: Build a Gemma Agent Skill
- [ ] `SKILL.md` present inside a dedicated skill folder (or repo root) adhering to the [Agent Skills Open Standard](https://agentskills.io/specification).
- [ ] YAML frontmatter contains valid `name` and `description` fields.
- [ ] Detailed instructions define a concrete, reusable workflow with explicit trigger conditions and output formats.
- [ ] At least one realistic example invocation is provided (e.g., in `examples/` or within the skill specification).
- [ ] Live demo shows Gemma actively executing the skill workflow, verified via a compatible agent or a documented standalone test harness.

### Track 2: Gemma Off the Grid
- [ ] Target quantized model weights pre-downloaded locally prior to demo setup.
- [ ] Cold-start run instructions in `README.md` verified without internet access.
- [ ] Core user workflow demonstrated live with Wi-Fi and cellular connections completely disabled.
- [ ] Model inference runs 100% locally on CPU or consumer GPU (no fallback to cloud or external APIs).
- [ ] Handled at least one edge case (e.g., malformed input, context boundary, or graceful fallback) completely offline.

### Track 3: Multimodal Campus Companion
- [ ] Employs a genuine multimodal Gemma variant that ingests non-text inputs (images/audio) directly.
- [ ] Supported file types and maximum input file size limits clearly documented in `README.md`.
- [ ] Live demo accepts a real non-text file and produces an accurate, context-grounded response.
- [ ] Invalid/corrupted/unsupported media input is caught gracefully with a clear, user-facing explanation of limitations (no unhandled stack traces).

### Track 4: Gemma-Powered Dev Harness
- [ ] Implements a real, bounded tool with strict argument schema validation (not just plain chat completion).
- [ ] Closed tool-call execution loop: Gemma chooses tool, runtime executes action, and result is synthesized back to the user.
- [ ] Explicit user confirmation prompt or safety boundary required before executing any state-modifying or destructive action.
- [ ] If forking/extending upstream software: upstream repository linked, OSI license verified, original team contribution documented, and a clean git diff provided.

### Track 5: Campus Knowledge Companion (RAG)
- [ ] Small, inspectable public or synthetic corpus committed under `corpus/` (no private student records or unconsented university data).
- [ ] Real retrieval pipeline implemented (document chunking + vector search); whole-corpus prompt stuffing disallowed.
- [ ] `README.md` explicitly documents both the retrieval embedding model and the generative Gemma model.
- [ ] Live demo proves grounded answer with explicit chunk citations for a question present in the corpus.
- [ ] Live demo proves graceful refusal / admission of ignorance when asked a question absent from the corpus.

---

## 3. MLH OrganizerHQ Submission

- [ ] Project submitted via **Add Submission** on [OrganizerHQ](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club) before 5:00 AM EAT.
- [ ] Selected **Best Open-Source AI Project** (the official MLH Hack Day challenge).
- [ ] If an official partner challenge (such as Best Use of Gemma) was confirmed and announced on-site by organizers, selected it as instructed.
- [ ] Explicitly declared your team's **single primary iTech Club Track** (Track 1–5) in the project description and README.
- [ ] Public GitHub repository link entered into the submission form.
- [ ] Optional demo link (video, hosted preview, or slides) added to the submission form.

---

## 4. 2-Minute Demo Preparation (See [Live Demo Script Template](./demo-script.md))

- [ ] **30 seconds — Problem & User**: Clearly state the problem, target campus user, and declared primary track.
- [ ] **60 seconds — Core Gemma Workflow**: Show the live input, model execution, and output on screen.
- [ ] **30 seconds — Edge Case & Verification**: Demonstrate edge-case handling or offline state, and highlight where the judge can verify the code in the repository.
- [ ] **Code Readiness & Transparency**: All team members are prepared to explain their implementation, prompt/tool architecture, and AI tool usage during judging Q&A.
