---
title: Demo Script Template
nav_exclude: true
permalink: /templates/demo-script/
description: "A project-neutral two-minute working demonstration and one-minute judge Q&A."
---

# 2-Minute Live Demo + 1-Minute Judge Q&A Template

Rehearse one real user journey for human judges. The session schedule requires [organiser confirmation]({{ site.baseurl }}/rules/#the-hacking-timeline); do not rely on the former 5:00–5:45 AM slot.

Slides or prerecorded video do not replace working software. Show what actually runs, identify your model and disclose any fallback, edited example or unfinished feature.

Use one project, repository and demo for every category it qualifies for. Human judges keep [distinct category notes]({{ site.baseurl }}/judging/#category-specific-evaluation-lenses); those proposed lenses are local guidance for organiser review, not an official MLH numerical rubric. The retained 100-point block applies only to separately confirmed **iTech Club local overall assessment**.

## Universal demo flow

| Timing | What to show | Evidence for category review / local rubric |
|---|---|---|
| **0:00–0:15** (15s) | One specific user, problem and desired outcome | Problem relevance |
| **0:15–0:30** (15s) | Exact model/runtime and why AI helps; entered prize categories | Meaningful open-source/open-weight AI integration |
| **0:30–1:15** (45s) | Realistic input through the working application to a useful output; your original contribution | Technical execution and originality |
| **1:15–1:45** (30s) | An edge case, failure or uncertainty; safety boundary and human next step | Responsible AI, privacy and safety |
| **1:45–2:00** (15s) | Public repo, licence, setup/tests, model/dependency disclosures and limitations | Open-source quality |
| **2:00–3:00** (60s) | Judge Q&A and relevant code | All six criteria |

The demonstration totals **120 seconds**, followed by **60 seconds** of Q&A. See the [proposed category lenses]({{ site.baseurl }}/judging/#category-specific-evaluation-lenses) and, where applicable, the [separate local rubric]({{ site.baseurl }}/judging/#the-100-point-score-sheet).

## Adapt evidence to your actual project

No technical pattern below is mandatory:

- If claiming offline operation, show local inference with external connectivity disabled; explain what it proves and any remaining dependencies.
- If using media, demonstrate a supported real input and handle an unreadable or unsupported one.
- If retrieving information, show source evidence and behaviour when the answer is absent.
- If executing tools, show bounded permissions, validated arguments and approval or blocking of consequential actions.
- If publishing an agent skill, show standard conformance and an actual invocation.
- If entering **Best Use of Gemma 4**, show the exact Gemma 4 model ID and Gemini API call as required by the [category guidance]({{ site.baseurl }}/challenges/#the-official-mlh-challenge).

These are evidence suggestions, not archived acceptance gates, fixed deductions or extra points. Other architectures and domains are welcome.

## Q&A preparation

Be ready to show the actual model call, explain original versus reused work, describe test results and limitations, and answer what happens when inference fails. A response appearing on screen does not establish correctness; explain the observable benefit to the user.
