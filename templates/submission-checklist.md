---
title: Submission Checklist
nav_exclude: true
permalink: /templates/submission-checklist/
description: "Project-neutral publishing, testing and category submission checks."
---

# Hack Day Submission Checklist

Copy this into your team notes. The public category close is **31 October 2026, 6:00 AM EAT**; check [schedule status]({{ site.baseurl }}/rules/#the-hacking-timeline) for a verified organiser announcement. No primary track is required.

## Project and evidence

- [ ] Describe one primary user, one problem/use case and the expected outcome.
- [ ] Explain the important open-source/open-weight AI role and why a conventional approach alone is insufficient.
- [ ] Identify the exact model/version, runtime and working inference code.
- [ ] Distinguish original event work from upstream, starter and pre-existing components.
- [ ] Test normal inputs, edge cases and **at least one failure or uncertainty scenario**; record actual results.
- [ ] Prepare one working user journey and explain limitations, safety boundaries and human control.

## Public repository

- [ ] Public GitHub repository with a suitable OSI-approved application-code licence.
- [ ] Useful [README]({{ site.baseurl }}/templates/project-readme-template/): problem, user, selected categories, architecture, model/dependency/data disclosures and permissions.
- [ ] Tested installation/run commands and placeholder environment configuration.
- [ ] Team contributions and proportionate AI coding-tool disclosure.
- [ ] No credentials, private records or unpermitted data in files or Git history.
- [ ] Exact model licence linked: Gemma 4 uses Apache 2.0; check other generations/models separately.

## Category-specific evidence

Complete only the conditions relevant to the category/project you are entering. These are not new tracks or bonus-point categories.

- [ ] **Best Open-Source AI Project:** original public licensed project with an important functional open-source/open-weight AI contribution.
- [ ] **If an agent skill:** demonstrate Agent Skills Open Standard conformance.
- [ ] **If a model harness:** document original implementation or meaningful upstream extension.
- [ ] **If entering Best Use of Gemma 4:** demonstrate meaningful Gemma 4 use with exact model ID, code and live evidence. Follow the [Gemma API requirement and official category links]({{ site.baseurl }}/challenges/#the-official-mlh-challenge); do not assume local-only or older Gemma use qualifies.
- [ ] DigitalOcean use is optional; no mandatory provider, domain or archived acceptance checklist.

## Official submission

- [ ] Register and check in.
- [ ] One team member submits on behalf of the team through the event's [OrganizerHQ Challenges page](https://www.mlh.com/events/hacktoberfest-hack-day-nairobi-x-itech-club/challenges).
- [ ] Provide project name, public repository URL, description, technologies and optional demo URL.
- [ ] Submit **once** and select **every category the project qualifies for**.
- [ ] Verify the saved submission before the confirmed close; keep the repository public.

## Human demo and administrative review

- [ ] Rehearse the [two-minute demo and one-minute Q&A]({{ site.baseurl }}/templates/demo-script/).
- [ ] Show the real model workflow, one boundary/failure and the relevant code.
- [ ] Ask staff to resolve administrative flags promptly. A legacy checker missing-Gemma warning does not exclude other open models from the broad category.
- [ ] Treat checker PASS as preliminary hygiene only, not a score or guaranteed category eligibility. Network/rate-limit failures must never penalise a team.
