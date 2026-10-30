---
title: Submission Checklist
nav_exclude: true
permalink: /templates/submission-checklist/
description: "Project-neutral publishing, testing and category submission checks."
---

# Hack Day Submission Checklist

Copy this into your team notes. Follow the [event timing]({{ site.baseurl }}/rules/#the-hacking-timeline), live category close and [submission guide]({{ site.baseurl }}/submission/). Choose your own project; no primary track is required.

## Project and evidence

- [ ] Describe one primary user, one problem/use case and the expected outcome.
- [ ] If entering an AI category, explain the important AI role and why a conventional approach alone is insufficient.
- [ ] If using a model, identify its exact version, runtime and working inference code.
- [ ] Distinguish original event work from upstream, starter and pre-existing components.
- [ ] Test normal inputs, edge cases and **at least one failure or uncertainty scenario**; record actual results.
- [ ] Prepare one working user journey and explain limitations, safety boundaries and human control.

## Public repository

- [ ] Public GitHub repository with a suitable OSI-approved application-code licence.
- [ ] Useful [README]({{ site.baseurl }}/templates/project-readme-template/): problem, user, selected categories, architecture, model/dependency/data disclosures and permissions.
- [ ] Tested installation/run commands and placeholder environment configuration.
- [ ] A different developer can follow the setup and test instructions; record any unverified steps honestly.
- [ ] Team contributions and proportionate AI coding-tool disclosure.
- [ ] No credentials, private records or unpermitted data in files or Git history.
- [ ] If using a model, link its exact licence: Gemma 4 uses Apache 2.0; check other generations/models separately.

## Category-specific evidence

Complete only the conditions relevant to the category/project you are entering. These are not new tracks or bonus-point categories.

- [ ] **Best Open-Source AI Project:** original public licensed project with an important functional open-source/open-weight AI contribution.
- [ ] **If an agent skill:** demonstrate Agent Skills Open Standard conformance.
- [ ] **If a model harness:** document original implementation or meaningful upstream extension.
- [ ] **If entering Best Use of Gemma 4:** demonstrate meaningful Gemma 4 use with exact model ID, code and live evidence. Follow the [Gemma API requirement and official category links]({{ site.baseurl }}/challenges/#the-official-mlh-challenge); do not assume local-only or older Gemma use qualifies.
- [ ] **If entering Best Project Deployed on PrimeCloud:** original application with public licensed GitHub source, genuine PrimeCloud deployment and working public URL; show the deployed user journey, not only a dashboard screenshot.
- [ ] **PrimeCloud README evidence:** technologies, actual PrimeCloud usage, architecture/non-secret configuration, setup/deployment instructions, team members and contributions.
- [ ] Gemma 4 is required only for its category; PrimeCloud deployment only for its category, which needs no AI. DigitalOcean remains optional.

## Official submission

- [ ] Register and check in.
- [ ] Confirm team details and contributions; follow the actual form and organiser-confirmed team policy without publishing private registration information.
- [ ] One team member submits on behalf of the team through the event's [OrganizerHQ Challenges page](https://www.mlh.com/events/hacktoberfest-hack-day-nairobi-x-itech-club/challenges).
- [ ] Provide project name, public repository URL, description and technologies. A demo URL is optional except for the required working public PrimeCloud deployment URL when entering that category.
- [ ] Submit **once** and select **every category the project qualifies for**.
- [ ] Verify the saved submission before the confirmed close; keep the repository public.
- [ ] Open the saved repository/demo links and check the entered categories. A canvas or README alone is not official submission.

## Demo preparation

- [ ] Rehearse the [demo flow]({{ site.baseurl }}/templates/demo-script/) within the organiser-confirmed presentation and Q&A allowance.
- [ ] Show the working user journey, one boundary/failure and relevant code; include the actual model workflow if used and public deployment if entering PrimeCloud.
- [ ] Ask staff for help before the deadline if you cannot access or save your submission.
- [ ] If PrimeCloud or another intended category is absent from the actual form, contact staff before the deadline; a README checkbox is not official entry.
- [ ] Keep your repository and demo accessible, with evidence for each entered category.
