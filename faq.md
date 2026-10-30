---
title: FAQ
nav_order: 8
description: "Quick answers to common questions about rules, teams, tracks, scoring, and submission."
---

# FAQ
{: .no_toc }

1. TOC
{: toc }

---

## Do I need to be an expert in AI/ML to take part?

No. All 5 challenges are designed to be approachable with the [Starter Kit]({{ site.baseurl }}/starter-kit/) and guidance from mentors. Calling Gemma through the Gemini API is a straightforward API call—you do not need to understand deep model internals or write complex neural nets to build a helpful campus tool.

## Can I come without a team?

Yes. Under official MLH guidelines, solo hackers and pairs are completely welcome at the event. You can attend workshops, hack on ideas, and submit to the broader MLH challenge on OrganizerHQ.

However, to be eligible for the **local iTech Club awards and Top Three Overall podium**, you need to be part of a **3–4 person team**. If you arrive solo or as a pair, join the **team formation session from 7:00–7:30 PM** right after check-in. Organizers will help match you with peers interested in the same challenge track. See [Rules → Team size & formation]({{ site.baseurl }}/rules/#team-size-formation).

## Can my team enter more than one challenge track?

For local judging, **no—each team must declare exactly one primary iTech Club track** in their repository `README.md` and submission description.

**Why one primary track:** Selecting one primary track ensures fair, direct comparison among entries tackling the same problem domain and prevents teams from gaining an unfair scoring advantage by double-entering multiple tracks. You are welcome to incorporate techniques from other tracks (for example, adding an offline fallback to a RAG assistant), but judges will evaluate your project against the criteria and demo scenario of your declared primary track. Track-specific acceptance tests inform the rubric (specifically Technical Execution and Use of Gemma); they are **not** hidden bonus points.

On [MLH OrganizerHQ](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club), submit your project to **Best Open-Source AI Project** (and any verified partner challenge if announced by organizers).

## How are winners selected and ranked?

The hackathon operates under a **strictly human-led judging system**. There is no automated project evaluation, no AI-based project scoring, and no automated leaderboard. All projects are evaluated by an appointed panel of human judges using a published common rubric and standardised judge score sheets.

- **Local iTech Club Recognition:** All eligible local submissions across all 5 preset tracks are evaluated by appointed human judges during live 2-minute demos using the published [100-Point Rubric]({{ site.baseurl }}/judging/#the-100-point-score-sheet). Judges evaluate projects independently across 6 criteria (Problem Relevance 15, Meaningful Gemma Integration 20, Technical Execution 25, Originality 15, Responsible AI & Safety 10, Open-Source Quality 15) using a 0–5 rating scale converted to weighted points. Individual scores are averaged across judges (minimum 2 valid scores per team; 3 preferred where capacity allows). The top three highest-scoring teams are awarded:
  - **First Place – Overall Winner**
  - **Second Place – Overall Runner-up**
  - **Third Place – Overall Third Place**
- **Official MLH Challenge:** The official [Best Open-Source AI Project](https://hacktoberfest-handbook.mlh.com/fest-planning-guide/open-source-prize-categories) challenge has **one winning team** marked directly in OrganizerHQ according to official MLH requirements. While the local First Place project is a prime candidate, the MLH winner must be evaluated and marked in OrganizerHQ following official MLH requirements.
- **Partner Prizes:** If an official Google Gemma partner prize is active and verified in OrganizerHQ for event 14735, it will be awarded separately as confirmed on-site by organizers.

## What happens if there is a tie in scores?

If two or more teams tie in their overall consolidated average score, ties are resolved in this strict pre-published order:
1. Higher score in **Meaningful Gemma/open-weight AI integration** (out of 20).
2. Higher score in **Technical execution and working demonstration** (out of 25).
3. **Deliberation by the judging panel**, with the decision and rationale formally documented in organiser records.

## How should our team disclose AI coding assistants?

Keep disclosure proportionate: add a short **AI Tools Used** section to your `README.md` listing any tools used (e.g. GitHub Copilot, Gemini CLI, Claude Code, Cursor) and a brief 1–2 sentence explanation of your team's own contribution. Every team member must understand and be able to explain the submitted code during the live demo.

## Are judge score sheets and notes published publicly?

No. Individual judge sheets, raw numerical scores, and provisional rankings are **strictly confidential internal records**. They are never published on the public website or shared with participants. Only final validated winners and high-level constructive feedback are announced.

## What is the difference between open-source code and open-weight AI?

- **Your application source code** must be released under an [OSI-approved open-source license](https://opensource.org/licenses) (such as MIT, Apache-2.0, or GPL-3.0) via a `LICENSE` file at your repository root.
- **The AI model weights** (such as Gemma) are governed by responsible open-weight terms—specifically the [Gemma Terms of Use](https://ai.google.dev/gemma/terms)—rather than traditional OSI software licenses. In your `README.md`, simply specify which Gemma model you used and cite its terms of use.

## Does my repo need to be public during the hack, or just at submission?

Your repository must be **public by the submission deadline (5:00 AM EAT)** and must **remain public after the event** to stay eligible for prizes, per standard MLH rules. You can develop in a private repository overnight if your team prefers, but make sure it is public with an OSI `LICENSE` file before submitting.

## What if our project isn't completely finished?

Submit anyway and demo what you have. "Technical execution & working demo" is 25 points on the [score sheet]({{ site.baseurl }}/judging/#the-100-point-score-sheet), but the remaining 75 points evaluate your problem framing, use of Gemma, originality, open-source documentation, and learning. A functioning prototype with clear documentation and an honest explanation of limitations can score very competitively.

## Can we use a model other than Gemma?

The 5 iTech Club preset tracks are specifically designed for the **Gemma family** (any size or variant, including Gemma 4, Gemma 2, PaliGemma, or EmbeddingGemma). For the broader MLH "Best Open-Source AI Project" challenge, other open-weight models are permissible, but to be eligible for iTech Club track recognition, Gemma must be an important functional component.

## What counts as an "important part" of the project for Gemma?

Ask yourself: *If we removed Gemma from our project, would the core product still work?* If the answer is yes, Gemma is likely just an afterthought. Judges look for projects where Gemma provides the core reasoning, perceptual understanding, tool-calling intelligence, or synthesis.

## Is there internet at the venue, and should I rely on it?

Venue Wi-Fi is provided, but with dozens of students downloading dependencies simultaneously, network congestion can occur. We strongly recommend downloading model weights (if running locally) and Python/Node libraries **at home before arriving**. If you want an experience that is completely immune to network slowdowns, choose [Track 2: Gemma Off the Grid]({{ site.baseurl }}/challenges/02-edge-offline/).

## Are there starter templates for our project README and live demo?

Yes! We provide copy-ready templates to save your team time:
- **[Project README Template]({{ site.baseurl }}/templates/project-readme-template/)** — copy-and-fill template covering problem, architecture, model specifications, `.env.example`, and disclosures.
- **[Live Demo Script Template]({{ site.baseurl }}/templates/demo-script/)** — a 2–3 minute presentation structure with track-specific live demo prompts.
- **[Submission Checklist]({{ site.baseurl }}/templates/submission-checklist/)** — pre-submission verification checklist to copy into your repository before 5:00 AM.

## Where can organizers and mentors find the event runbook?

Organizers and mentors can refer to the **[Organiser Runbook]({{ site.baseurl }}/organizer-runbook/)** and the **[Organiser Quick-Reference Checklist]({{ site.baseurl }}/organizer-checklist/)** for timelines, staff roles, offline contingency kits, score tabulation, and official MLH winner marking workflows.

## Who do I ask if I'm stuck on a rule or a submission question?

Approach any organizer wearing an iTech Club badge or MLH lanyard at the venue, or check the [Resources]({{ site.baseurl }}/resources/) page for guidance.
