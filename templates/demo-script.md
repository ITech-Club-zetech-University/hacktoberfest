---
title: Demo Preparation Guide
nav_exclude: true
permalink: /templates/demo-script/
description: "A project-neutral working demonstration, test evidence and judge Q&A preparation."
---

# Demo Preparation Guide

Rehearse one real user journey for human judges. Use the **final presentation format, demo duration and Q&A allowance announced by organisers**, not a time limit inferred from this guide. The [session schedule still requires confirmation]({{ site.baseurl }}/rules/#the-hacking-timeline).

Show what actually runs. Slides, recordings and mock outputs do not establish working functionality; label any fallback, edited example or unfinished feature honestly. A recording or demo URL can help explain your project but does not replace the required working demonstration.

## Seven-part demo flow

1. **Problem and user:** Name one specific user, the task they struggle with and the outcome you want to improve.
2. **Working journey:** Start with a realistic input and show the core application flow through to its useful result. Prefer a focused working MVP over a tour of unfinished features.
3. **Actual AI role:** Point out exactly where the model is called and what it contributes. Show the relevant code or request path; distinguish dynamic inference from cached or mocked output.
4. **Model and technical decisions:** Identify the exact model/variant, provider/runtime, architecture and important trade-offs. Explain why the approach fits the problem. A Gemini model is not Gemma 4.
5. **Normal test and limitation:** Show one normal case and one edge case or limitation. Explain expected versus observed results, uncertainty, safe failure and any human next step. Keep recorded failure/uncertainty tests available too.
6. **Built versus unfinished:** Explain the team's original work during the confirmed hack period, what was reused, and what remains incomplete. Do not present roadmap features as built.
7. **Reproduce and contribute:** Open the public repository, code licence and README. Show how another developer can configure, run, test and contribute to the project.

Keep the core flow short enough for the organiser-confirmed slot, leaving the announced time for questions. Cut optional features from the presentation before cutting the evidence needed to understand the project.

## Adapt evidence to your actual project

No technical pattern below is mandatory:

- If claiming offline operation, show local inference with external connectivity disabled; explain what it proves and any remaining dependencies.
- If using media, demonstrate a supported real input and handle an unreadable or unsupported one.
- If retrieving information, show source evidence and behaviour when the answer is absent.
- If executing tools, show bounded permissions, validated arguments and approval or blocking of consequential actions.
- If publishing an agent skill, show standard conformance and an actual invocation.
- If entering **Best Use of Gemma 4**, show the exact Gemma 4 model ID and Gemini API call as required by the [category guidance]({{ site.baseurl }}/challenges/#the-official-mlh-challenge).

These are evidence suggestions, not archived acceptance gates, fixed deductions or extra points. Other architectures and domains are welcome.

## Rehearsal and Q&A

- Test the demo on the actual device and chosen inference path; check connectivity, downloaded models, account access and permitted sample data.
- Prepare an honest failure path for unavailable inference; never silently substitute a different model or a canned answer.
- Be ready to explain model choice, original versus reused work, test outcomes, privacy, costs, limitations and what happens when inference fails.
- Keep secrets and personal data out of terminals, screenshots, logs and recordings.
- Use one project, repository and demo for all categories it qualifies for. Human judges keep [distinct category notes]({{ site.baseurl }}/judging/#category-specific-evaluation-lenses); the local 100-point assessment is separate from the MLH awards.

A model response appearing on screen does not establish correctness. Explain the observable benefit and what your test evidence does and does not prove. Finish with the [pre-submission checklist]({{ site.baseurl }}/templates/submission-checklist/).
