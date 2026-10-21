---
title: "1. Build a Gemma Agent Skill"
parent: Challenges
nav_order: 1
description: "Package a reusable capability for AI coding agents according to the Agent Skills open standard, powered by Gemma.
"
---

# Challenge 1: Build a Gemma Agent Skill
{: .no_toc }

**Track focus:** Packaging reusable agent capabilities · **Target window:** ~8 hours · **Team size:** 3–4
{: .fs-5 .fw-300 }

1. TOC
{: toc }

---

## 1. Pitch & target user

AI coding agents (such as Claude Code, Gemini CLI, OpenCode, and cursor-based agents) are transforming software engineering, but out of the box they lack specialized knowledge of campus workflows, lab rubrics, and community standards. In this track, your team packages a **reusable Agent Skill**—a portable directory of instructions and scripts that teaches any compatible coding agent a brand-new, repeatable capability powered by Gemma.

- **Target user:** Computer science students, teaching assistants, student developers, and iTech Club open-source maintainers who want automated, high-quality assistance directly inside their daily coding agents.
- **What this is NOT:** This is **not** a generic README file, a one-off prompt copy-pasted into a web chat box, or a standalone chatbot. You are authoring a modular, standard-compliant package designed to be discovered and invoked by an AI agent.

## 2. Problem to solve

Student developers and club members routinely face repetitive, multi-step engineering tasks that generic models perform inconsistently:
- Reviewing student programming assignments against strict academic rubrics and generating constructive line-by-line feedback.
- Onboarding new contributors to iTech Club repositories by inspecting repository architecture, checking conventions, and identifying "good first issues".
- Analyzing Git pull request diffs to check for missing tests, security gotchas, or style deviations before mentor review.
- Auditing educational markdown notes and lab handouts to automatically generate accessible image descriptions and structured study quizzes.

Your goal is to build an Agent Skill that solves one of these real problems cleanly, consistently, and safely.

## 3. Minimum viable project (MVP)

A successful MVP for this track consists of:
1. A valid skill directory containing a compliant `SKILL.md` file that follows the [Agent Skills Open Standard](https://agentskills.io/specification).
2. An executable script or structured instruction set where **Gemma actively performs the core analytical or generative reasoning task**.
3. Concrete sample data (e.g. a sample student script, a test Git diff, or sample course notes) that demonstrates the skill working end-to-end.
4. A verified demonstration showing the skill being invoked by a compatible coding agent, or executed via a reproducible local test runner.

## 4. Required Gemma contribution

Writing a `SKILL.md` specification file alone does **not** prove Gemma is an essential part of the solution. Your project must clearly separate the agent harness/skill structure from the intelligence engine:

- **What Gemma does:** Gemma (invoked via the Gemini API or run locally via Ollama) must perform the substantive cognitive work—such as evaluating semantic code correctness, synthesizing diffs, or generating rubric-grounded feedback.
- **How judges inspect it:** Judges will inspect your skill's scripts or execution logs to see the prompt payload sent to Gemma and the response received. If Gemma were removed or replaced with static regex/templates, the core functionality must fail or become trivial. Every team member must be able to explain how Gemma is invoked and how its temperature, prompts, and outputs are handled.

## 5. Mandatory acceptance criteria

Every valid submission in this track must satisfy these four observable, testable criteria:

1. **Standard directory and frontmatter conformance:** The skill lives in a directory named to match the skill name (e.g. `code-rubric-reviewer/SKILL.md`). The `SKILL.md` file starts with valid YAML frontmatter containing:
   - `name`: 1–64 characters, lowercase alphanumeric and hyphens only, no consecutive hyphens, matching the parent folder name.
   - `description`: 1–1024 characters, non-empty, clearly explaining both *what* the skill does and *when* an agent should invoke it.
2. **Gemma-driven execution:** Gemma is directly invoked (either via the Gemini API or a local open-weight runtime) within the skill's workflow to perform the core task, demonstrable in logs or terminal output.
3. **Concrete, reproducible example invocation:** The repository includes a realistic test input file and step-by-step instructions showing the exact command or prompt used to trigger the skill.
4. **Agent compatibility & discovery evidence:** The skill is demonstrated running inside at least one real agent environment (e.g. Claude Code, Gemini CLI, OpenCode) **OR** includes a documented local test driver script (`test_skill.py` or `test_skill.sh`) that simulates agent skill discovery and execution for judges whose laptops lack that specific agent client.

## 6. Suggested 2-minute demo scenario

When presenting to judges, follow this concise demo flow:

- **0:00 – 0:30 (The Setup):** State the user problem. Show your repository directory layout (`my-skill/SKILL.md`, `scripts/`, `examples/`), highlighting the frontmatter in `SKILL.md`.
- **0:30 – 1:20 (Live Invocation):** Run the skill against a realistic sample input (e.g., submit a Python file with a known logic bug or style issue). Show the agent discovering the skill, dispatching the task to Gemma, and displaying the resulting output.
- **1:20 – 1:45 (Inspect the Output):** Highlight the specific output generated by Gemma (e.g. rubric grade, actionable fix recommendation, or diff analysis) and show where the Gemma call occurred.
- **1:45 – 2:00 (Edge Case & Extensibility):** Briefly demonstrate or describe how the skill handles invalid input (e.g. empty file or unsupported language) and explain how another student can install your skill with one command.

## 7. Required repository & README evidence

Your public GitHub repository must include:
- [ ] A root or dedicated skill directory conforming to the [Agent Skills specification](https://agentskills.io/specification).
- [ ] A `README.md` containing:
  - Clear explanation of the skill, the target user, declaring this as your team's primary iTech Club challenge track, and why Gemma was chosen.
  - Which Gemma model/variant was used, how it is called (Gemini API endpoint or local Ollama model ID), and acknowledgment of the [Gemma Terms of Use](https://ai.google.dev/gemma/terms).
  - Prerequisites and step-by-step installation instructions for the skill.
  - Which AI agents were tested (e.g. Claude Code, Gemini CLI, OpenCode).
  - Explicit disclosure of any AI coding tools (Copilot, Cursor, etc.) used by your team to scaffold or write code during the hack day.
- [ ] Sample input files in an `examples/` or `assets/` folder so judges can immediately test the skill without creating test data from scratch.
- [ ] An OSI-approved open-source `LICENSE` file at the repository root.

## 8. Stretch goals (optional)

These optional enhancements will help distinguish top entries but are **not** required to pass:
- **`skills-ref` validation:** Validate your skill using the official `skills-ref validate` CLI tool with zero schema warnings.
- **Progressive disclosure structure:** Implement a `references/` subfolder with specialized documentation (e.g. `rubric-spec.md` or `conventions.md`) that the agent reads only on demand.
- **Multi-agent verified:** Document verified compatibility across two or more distinct agent harnesses (e.g. Claude Code and Gemini CLI).
- **Interactive refinement:** Enable the skill to engage in multi-turn feedback, allowing the developer to ask follow-up questions about Gemma's suggestions.

## 9. Starter resources

- [Agent Skills Open Standard](https://agentskills.io/) — Official standard home
- [Agent Skills Specification](https://agentskills.io/specification) — Formal frontmatter & directory specification
- [Agent Skills Quickstart](https://agentskills.io/skill-creation/quickstart) — Step-by-step skill creation guide
- [Agent Skills Best Practices](https://agentskills.io/skill-creation/best-practices) — Writing effective skill instructions
- [Gemma Quickstart via Gemini API](https://mlh.link/gemma-quickstart) — Fast cloud setup for Gemma inference
- [Gemma Cookbook `apps/`](https://github.com/google-gemma/cookbook/tree/main/apps) — Worked examples of Gemma workflows

## 10. Privacy, safety & licensing

- **Open-source software license:** Your application code must use an OSI-approved license (e.g., MIT, Apache-2.0). The underlying model weights are governed separately by the [Gemma Terms of Use](https://ai.google.dev/gemma/terms).
- **No secrets in code:** Never commit API keys (`GEMINI_API_KEY`) or personal tokens in `SKILL.md` or scripts. Read keys from environment variables or `.env` files (make sure `.env` is in `.gitignore`).
- **Student privacy:** Use synthetic or anonymized code submissions for testing; never publish private student grades, admission numbers, or personal identifying information.
- **Safe script execution:** If your skill includes executable helper scripts under `scripts/`, restrict them to read-only or bounded operations. Do not run destructive shell commands without explicit user prompts.

## 11. Challenge-specific evaluation notes

These notes supplement the 100-point rubric in [`judging.md`]({{ site.baseurl }}/judging/):
- **Agent standard compliance (under Open-Source Quality):** Judges will inspect `SKILL.md` to verify that `name` matches the directory name, frontmatter is valid YAML, and the description provides actionable triggering guidance.
- **Demonstrated Gemma agency (under Use of Gemma):** Judges will verify that Gemma is actively invoked to produce the output. If a team presents a static prompt without working Gemma integration, points will be deducted under the Gemma criterion.
- **Code understanding:** Every team member must be able to explain the skill's instructions, prompt structure, and integration scripts during the live demo.
