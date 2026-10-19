---
title: "1. Build a Gemma Agent Skill"
parent: Challenges
nav_order: 1
description: "Package a reusable capability for AI coding agents, powered by Gemma."
---

# Challenge 1: Build a Gemma Agent Skill
{: .no_toc }

**MLH category:** Agent skill · **Team size:** 3–4
{: .fs-5 .fw-300 }

1. TOC
{: toc }

---

## The pitch

AI coding agents (Claude Code, Gemini CLI, OpenCode, and dozens of others) can be extended with **Agent Skills** — portable folders of instructions and scripts that teach an agent a new, reusable capability. Build one that's genuinely useful to the Zetech / iTech Club community, and use Gemma to do real work inside it.

## What to build

An **Agent Skill** — a `SKILL.md` file (plus any scripts, templates, or reference material it needs) that follows the [Agent Skills open standard](https://agentskills.io/specification) — where **Gemma does a meaningful piece of the work**, not just a thin wrapper around a prompt.

Some starting ideas (don't feel limited to these):

- A skill that reviews a student's code submission against a rubric and drafts feedback using Gemma
- A skill that turns lecture notes or slides into a study guide or quiz using Gemma's multimodal input
- A skill that onboards a new contributor to an iTech Club repo — reads the codebase, explains conventions, and drafts a "good first issue" list
- A skill that drafts accessible alt-text and captions for images in course material, using Gemma's vision capability

## Requirements

- [ ] A `SKILL.md` with `name` and `description` frontmatter at minimum, following the [Agent Skills specification](https://agentskills.io/specification)
- [ ] Gemma (any variant/size) performs a real, identifiable part of the skill's work — not just "could technically call an LLM"
- [ ] The skill actually runs: demo it inside at least one real agent (Claude Code, Gemini CLI, OpenCode, etc. — see the [client showcase](https://agentskills.io/) for options available at the venue)
- [ ] Public GitHub repo, OSI-approved open-source license, clear README (see [Rules]({{ site.baseurl }}/rules/#submitting-your-project))
- [ ] README states which agent(s) you tested the skill in and how to install it

## Suggested Gemma tooling

- Start from the [Agent Skills quickstart](https://agentskills.io/skill-creation/quickstart) for the skill folder structure
- Call Gemma via the [Gemini API quickstart](https://mlh.link/gemma-quickstart) from inside your skill's scripts
- For a skill that needs to run fully offline, use a small Gemma 4 variant (E2B/E4B) via [Ollama](https://ai.google.dev/gemma/docs/integrations/ollama)
- Browse the [Gemma Cookbook `apps/` folder](https://github.com/google-gemma/cookbook/tree/main/apps) for end-to-end patterns to adapt

## What a strong entry looks like

- The skill solves a problem a real iTech Club member actually has — not a toy example
- It's genuinely reusable: a teammate (or judge) can install it fresh and get the same result
- Gemma's contribution is visible and explained plainly — what would break if you removed it?
- The `SKILL.md` is clean enough that another developer could extend it without asking you questions

## Judging emphasis for this track

On top of the [base rubric]({{ site.baseurl }}/judging/#the-score-sheet), judges will specifically check: does the `SKILL.md` actually comply with the Agent Skills standard, and did you demonstrate it running inside a real agent (not just described what it would do)?
