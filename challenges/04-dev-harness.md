---
title: "4. Gemma-Powered Dev Harness"
parent: Challenges
nav_order: 4
description: "Build or meaningfully extend an open-source agent harness, powered by Gemma's agentic capabilities."
---

# Challenge 4: Gemma-Powered Dev Harness
{: .no_toc }

**MLH category:** Model harness · **Team size:** 3–4
{: .fs-5 .fw-300 }

1. TOC
{: toc }

---

## The pitch

A "model harness" is the software *around* a model — the part that manages prompts, tools, memory, and actions, turning raw model output into something that can actually get work done. Gemma 4 ships with built-in function calling and agentic capabilities specifically to power harnesses like this. Build one, or meaningfully extend an existing open-source one.

## What to build

Either:

- **An original harness**: a CLI, bot, or small app that wraps Gemma 4 with tool-use (function calling), memory, and multi-step planning to automate a real developer or campus workflow, **or**
- **A meaningful extension to an existing open-source harness** — e.g. adding a Gemma backend to [OpenCode](https://opencode.ai/), [Pi](https://github.com/badlogic/pi-mono), [Hermes Agent](https://hermes-agent.nousresearch.com/), or [OpenClaw](https://openclaw.ai/), or adding a genuinely new capability (not a cosmetic tweak) to one of them.

Ideas to riff on:

- A PR-review bot that reads a diff, runs tests via tool calls, and leaves structured review comments
- A terminal agent that triages open GitHub issues on an iTech Club repo and drafts first responses
- A study-session agent that plans a revision schedule, pulls in course material, and quizzes you — using tool calls to check your answers
- A Gemma backend/adapter for an existing open-source harness, so it can run entirely offline on a small Gemma variant

## Requirements

- [ ] If extending an existing harness: your changes must be **original or a meaningful improvement** — a config tweak or a renamed fork doesn't qualify. Explain the delta clearly in your README.
- [ ] If building from scratch: it must genuinely manage **tools/actions**, not just forward a prompt and print the response
- [ ] Uses Gemma 4's [function calling](https://ai.google.dev/gemma/docs/capabilities/text/function-calling-gemma4) or [thinking mode](https://ai.google.dev/gemma/docs/capabilities/thinking) capability as a core part of how it plans and acts
- [ ] Public GitHub repo, OSI-approved license, README (see [Rules]({{ site.baseurl }}/rules/#submitting-your-project))
- [ ] If forked: README links clearly to the upstream project and states exactly what you changed

## Suggested Gemma tooling

- [Function calling with Gemma 4](https://ai.google.dev/gemma/docs/capabilities/text/function-calling-gemma4) — the core mechanism you'll build around
- [FunctionGemma](https://ai.google.dev/gemma/docs/functiongemma) — a small model fine-tuned specifically for function calling, useful if you want a lightweight planner
- [Thinking modes](https://ai.google.dev/gemma/docs/capabilities/thinking) for multi-step reasoning before acting
- Study an existing harness's source before you fork it: [OpenCode](https://github.com/sst/opencode), [Pi](https://github.com/badlogic/pi-mono)

## What a strong entry looks like

- You can point at a specific moment in the demo where the agent **decided** to take an action, not just answered a question
- Tool calls are real (hit a real API, run a real script, touch a real file) — not simulated in the prompt
- If extending a harness, the diff is substantial enough that a maintainer of that project would recognize it as a real contribution

## Judging emphasis for this track

On top of the [base rubric]({{ site.baseurl }}/judging/#the-score-sheet), judges will specifically check: is there a genuine, demonstrable tool-use/action loop (not just chat), and — for forks — is the contribution original and substantial rather than cosmetic?
