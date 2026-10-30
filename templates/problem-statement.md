---
title: Project Proposal / Idea Canvas
nav_exclude: true
permalink: /templates/problem-statement/
description: "A downloadable planning canvas for a user, problem, model, achievable MVP and intended awards."
---

# Project Proposal / Idea Canvas

[Download the Markdown canvas]({{ site.baseurl }}/templates/downloads/project-proposal.md), copy it into your team notes and answer briefly. Use the [seven-step idea framework]({{ site.baseurl }}/challenges/#develop-an-idea-quickly) to refine it. This is a planning aid, not an additional submission form or idea-approval gate.

Follow the [submission guide]({{ site.baseurl }}/submission/) and complete the fields required by the official form; this canvas does not replace it.

The downloadable canvas is shown below:

{% capture proposal %}{% include_relative downloads/project-proposal.md %}{% endcapture %}
{{ proposal | remove_first: "# Project Proposal / Idea Canvas" }}

## Quick feasibility check

- Can you explain one user journey without saying “a platform for everyone”?
- Would a simpler non-AI approach work better? AI categories need a meaningful model role; a PrimeCloud entry does not need AI.
- Can you access permitted test data and run your chosen stack? If using a model, can you run it on your actual hardware or API account?
- If entering PrimeCloud, can you deploy the application, show a working public URL and document its architecture and deployment steps?
- What will remain under human control?
- Can you demonstrate the core flow, one edge case and one failure/uncertainty case?
- Does the scope fit the [organiser-confirmed time available]({{ site.baseurl }}/rules/#the-hacking-timeline), with time left for testing, documentation, submission and rehearsal?

Cut features until the answers are credible. State an observable success check; do not invent user validation or claim tests you have not run.
