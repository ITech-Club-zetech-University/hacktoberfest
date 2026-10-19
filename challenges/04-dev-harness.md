---
title: "4. Gemma-Powered Dev Harness"
parent: Challenges
nav_order: 4
description: "Build or meaningfully extend an open-source agent harness with structured tool-calling and safety boundaries, powered by Gemma."
---

# Challenge 4: Gemma-Powered Dev Harness
{: .no_toc }

**Track focus:** Agentic control loops, tool calling & safety boundaries · **Target window:** ~8 hours · **Team size:** 3–4
{: .fs-5 .fw-300 }

1. TOC
{: toc }

---

## 1. Pitch & target user

Language models become truly useful to engineers when they stop merely talking and start taking action. A **model harness** is the scaffolding software around an AI model: it translates model reasoning into concrete tool invocations, validates arguments, manages execution context, and feeds results back to the model in a closed loop. In this track, your team builds a lightweight developer harness from scratch or meaningfully extends an existing open-source harness using Gemma's structured function-calling capabilities.

- **Target user:** Software developers, student teams, and open-source project maintainers who want automated agents to inspect repositories, run tests, triage pull requests, or lint code safely.
- **What this is NOT:** An ordinary chatbot that writes code snippets in markdown is **not** a harness. A harness must execute real, bounded operations and react dynamically to their output.

## 2. Problem to solve

Developers spend hours on manual, repetitive maintenance tasks:
- Inspecting a Git pull request diff, automatically running a linter or test suite, and summarizing the results.
- Auditing a local repository for deprecated dependencies or security vulnerabilities via bounded command calls.
- Triaging open GitHub issues against recent commits to identify which pull request likely caused a regression.
- Running a test harness that executes unit tests, observes failures, and proposes targeted diffs for human review.

The challenge is building a harness that gives the model agency to use tools while maintaining strict safety boundaries so the agent cannot inadvertently damage code or execute unsafe commands.

## 3. Minimum viable project (MVP)

A successful MVP for this track requires:
1. **A defined tool interface:** At least one real, bounded tool (such as reading a git diff, running a local linter, inspecting file trees, or running a mock test runner).
2. **An active action loop:** A control loop where Gemma decides *which* tool to call and with *what arguments*, the harness runs the tool, and the tool's output is fed back to Gemma to formulate the final answer.
3. **Strict safety guardrails:** Built-in safeguards that prevent arbitrary shell execution or require explicit user confirmation before any state-modifying action (such as writing to a file or pushing a commit).
4. If extending an existing open-source harness (such as OpenCode, Pi, or Hermes Agent), a distinct, original contribution (such as an offline Gemma provider adapter, a new linting tool, or an interactive safety approval mechanism).

## 4. Required Gemma contribution

Gemma serves as the autonomous decision-maker within the harness:
- **What Gemma does:** Gemma inspects user instructions and available tool schemas, decides whether a tool call is needed, emits structured tool parameters (via function calling or JSON schemas), and interprets the tool's return values.
- **How judges inspect it:** Judges will watch the terminal or web execution logs to verify that the tool call was generated dynamically by Gemma, that the harness intercepted and validated the arguments, executed the tool, and fed the output back to Gemma for the final resolution.

## 5. Mandatory acceptance criteria

Every valid entry in this track must pass these four observable tests:

1. **Closed tool/action loop:** Demonstrably executes a complete loop: User Prompt → Model Decides Tool Call → Harness Validates & Executes Tool → Tool Result Fed Back → Model Generates Final Output.
2. **At least one real, bounded tool:** Implements a genuine tool with typed argument validation (e.g. `read_diff(path)`, `run_linter(file)`, or `search_files(pattern)`). Purely simulated mock tools that do not touch actual data do not pass.
3. **Safety confirmation boundary:** The harness strictly disallows arbitrary shell execution (`eval`, raw bash injection). If any action could modify disk state, the harness requires an explicit user confirmation prompt or operates in a strict read-only/dry-run mode.
4. **Transparent provenance (for forks):** If extending an existing open-source project, the repository clearly links to the upstream repository, verifies license compatibility, and provides a clear description of the original contribution. (Renamed repositories or configuration-only edits will be disqualified).

## 6. Suggested 2-minute demo scenario

When presenting your dev harness to judges, follow this demo flow:

- **0:00 – 0:30 (Problem & Tool Definition):** Explain what developer task your harness automates. Briefly show the registered tool definition and safety rules in your code.
- **0:30 – 1:15 (The Autonomous Tool Call):** Trigger the harness on a sample repository with a known issue (e.g. a Python script with syntax or formatting errors). Show Gemma deciding to run the linter or diff tool, display the harness executing the command, and show Gemma summarizing the findings.
- **1:15 – 1:45 (Safety Prompt in Action):** Command the agent to perform an action that would write or modify a file. Show that the harness halts and displays an explicit user confirmation prompt (`[y/N]`) before any destructive action is taken.
- **1:45 – 2:00 (Architecture & Schema):** Walk judges through the code that handles Gemma's function-calling response and passes tool results back into the model context.

## 7. Required repository & README evidence

Your public GitHub repository must include:
- [ ] A `README.md` containing:
  - Clear explanation of the harness architecture, developer problem solved, and explicit declaration of this track as your team's primary iTech Club challenge track.
  - Which Gemma model was used (e.g. `gemma-4-31b-it` via Gemini API or a local quantized variant with function calling) and acknowledgment of the [Gemma Terms of Use](https://ai.google.dev/gemma/terms).
  - List of registered tools with their input schemas and purpose.
  - Safety and security boundary explanation (how arbitrary execution is prevented).
  - If forked/extended: upstream repository URL, license verification, and detailed explanation of what your team wrote during the hack day.
  - Disclosure of any AI pair-programming tools used during development.
- [ ] Sample test repository or files (e.g., in a `demo_repo/` folder) so judges can test the harness safely.
- [ ] Working source code with argument validation.
- [ ] An OSI-approved open-source `LICENSE` file.

## 8. Stretch goals (optional)

These optional enhancements will distinguish advanced entries but are **not** required to pass:
- **Multi-tool chaining:** Allow Gemma to call two or more tools sequentially (e.g., search files → read matches → summarize diff) to resolve a complex prompt.
- **Interactive terminal TUI:** Provide a clean terminal interface (e.g. using `textual` or `rich`) displaying model thought streaming and tool execution progress.
- **Automated rollback:** Automatically revert changes if a test runner returns a non-zero exit code following a suggested patch.
- **Local offline harness:** Power the entire harness with a locally hosted quantized Gemma model via Ollama.

## 9. Starter resources

- [Gemma Function Calling Guide](https://ai.google.dev/gemma/docs/capabilities/text/function-calling-gemma4) — Official documentation for Gemma tool use
- [FunctionGemma Model Card](https://ai.google.dev/gemma/docs/functiongemma) — Compact model specialized for function calling
- [OpenCode Architecture](https://github.com/sst/opencode) — Minimalist reference implementation of an agent tool harness
- [Gemma Quickstart via Gemini API](https://mlh.link/gemma-quickstart) — Quick API invocation for function calling
- [Gemma Cookbook `tutorials/`](https://github.com/google-gemma/cookbook/tree/main/tutorials) — Notebooks illustrating function calling patterns

## 10. Privacy, safety & licensing

- **Open-source software license & Upstream license compatibility:** Your application source code must use an OSI-approved license (e.g., MIT, Apache-2.0). When building on existing open-source harnesses, maintain all original copyright notices and adhere to their upstream licenses. The Gemma model itself is governed separately by the [Gemma Terms of Use](https://ai.google.dev/gemma/terms).
- **Never execute arbitrary shell:** Do not expose `os.system()` or `subprocess.run(..., shell=True)` with unvalidated model strings. Keep tool functions strictly bounded to predefined operations.
- **No production credentials:** Use test repositories and mock data; never point an experimental hackathon agent at production codebases or private repositories.
- **API security:** Read all API keys from environment variables; never hardcode credentials into your repository.

## 11. Challenge-specific evaluation notes

These notes supplement the 100-point rubric in [`judging.md`]({{ site.baseurl }}/judging/):
- **Tool-calling integrity (under Technical Execution):** Judges will verify that a real tool executed and that Gemma dynamically chose the tool and arguments. Static responses or simulated text outputs will score poorly.
- **Safety implementation (under Technical Execution):** Judges will test that the harness cannot be coerced into running dangerous arbitrary commands or writing files without confirmation.
- **Substantial delta (for forks, under Originality):** If an existing harness was forked, judges will review git commits to verify that your team contributed substantive original logic during the event.
