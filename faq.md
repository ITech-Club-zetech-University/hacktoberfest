---
title: FAQ
nav_order: 8
description: "Quick answers to common questions about rules, teams, tracks, and submission."
---

# FAQ
{: .no_toc }

1. TOC
{: toc }

---

#### Do I need to be an expert in AI/ML to take part?

No. All 5 challenges are designed to be approachable with the [Starter Kit]({{ site.baseurl }}/starter-kit/) and guidance from mentors. Calling Gemma through the Gemini API is a straightforward API call—you do not need to understand deep model internals or write complex neural nets to build a helpful campus tool.

#### Can I come without a team?

Yes. Under official MLH guidelines, solo hackers and pairs are completely welcome at the event. You can attend workshops, hack on ideas, and submit to the broader MLH challenge.

However, to be eligible for the **5 preset iTech Club challenge track awards**, you need to be part of a **3–4 person team**. If you arrive solo or as a pair, join the **team formation session from 7:00–7:30 PM** right after check-in. Organizers will help match you with peers interested in the same challenge track. See [Rules → Team size & formation]({{ site.baseurl }}/rules/#team-size--formation).

#### Can my team enter more than one challenge track?

For local judging, **no—each team must declare exactly one primary iTech Club track** in their repository `README.md` and submission description.

**Why one primary track:** Selecting one primary track ensures fair, direct comparison among entries tackling the same problem domain and prevents teams from gaining an unfair scoring advantage by double-entering multiple tracks. You are welcome to incorporate techniques from other tracks (for example, adding an offline fallback to a RAG assistant), but judges will evaluate your project against the criteria and demo scenario of your declared primary track.

On [MLH OrganizerHQ](https://events.mlh.com/events/14735-hacktoberfest-hack-day-nairobi-x-itech-club), submit your project to **Best Open-Source AI Project** (and any verified partner challenge if announced by organizers).

#### What is the difference between open-source code and open-weight AI?

- **Your application source code** must be released under an [OSI-approved open-source license](https://opensource.org/licenses) (such as MIT, Apache-2.0, or GPL-3.0) via a `LICENSE` file at your repository root.
- **The AI model weights** (such as Gemma) are governed by responsible open-weight terms—specifically the [Gemma Terms of Use](https://ai.google.dev/gemma/terms)—rather than traditional OSI software licenses. In your `README.md`, simply specify which Gemma model you used and cite its terms of use.

#### Does my repo need to be public during the hack, or just at submission?

Your repository must be **public by the submission deadline (5:00 AM EAT)** and must **remain public after the event** to stay eligible for prizes, per standard MLH rules. You can develop in a private repository overnight if your team prefers, but make sure it is public with a `LICENSE` file before submitting.

#### What if our project isn't completely finished?

Submit anyway and demo what you have. "Technical execution & working demo" is 25 points on the [score sheet]({{ site.baseurl }}/judging/#the-100-point-score-sheet), but the remaining 75 points evaluate your problem framing, use of Gemma, originality, open-source documentation, and learning. A functioning prototype with clear documentation and an honest explanation of limitations can score very competitively.

#### Can we use a model other than Gemma?

The 5 iTech Club preset tracks are specifically designed for the **Gemma family** (any size or variant, including Gemma 2, Gemma 3n, PaliGemma, or EmbeddingGemma). For the broader MLH "Best Open-Source AI Project" challenge, other open-weight models are permissible, but to be eligible for iTech Club track recognition, Gemma must be an important functional component.

#### What counts as an "important part" of the project for Gemma?

Ask yourself: *If we removed Gemma from our project, would the core product still work?* If the answer is yes, Gemma is likely just an afterthought. Judges look for projects where Gemma provides the core reasoning, perceptual understanding, tool-calling intelligence, or synthesis.

#### Is there internet at the venue, and should I rely on it?

Venue Wi-Fi is provided, but with dozens of students downloading dependencies simultaneously, network congestion can occur. We strongly recommend downloading model weights (if running locally) and Python/Node libraries **at home before arriving**. If you want an experience that is completely immune to network slowdowns, choose [Track 2: Gemma Off the Grid]({{ site.baseurl }}/challenges/02-edge-offline/).

#### Who do I ask if I'm stuck on a rule or a submission question?

Approach any organizer wearing an iTech Club badge or MLH lanyard at the venue, or check the [Resources]({{ site.baseurl }}/resources/) page for guidance.
