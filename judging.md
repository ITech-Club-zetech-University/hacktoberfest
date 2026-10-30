---
title: Judging
nav_order: 6
description: "Prize-category criteria, proposed scoring weights and how winners are selected."
---

# Judging
{: .no_toc }

Prepare to show **what works, where AI contributes and what your team built**.

1. TOC
{: toc }

<style>
.judging-card {
  border: 1px solid rgba(150, 150, 170, .4);
  border-top: 4px solid #7253ed;
  border-radius: .5rem;
  margin: 1.5rem 0;
  padding: clamp(.75rem, 3vw, 1.5rem);
  min-width: 0;
}
.judging-card h3 { margin-top: 0; }
.judging-card--gemma { border-top-color: #47b8bf; }
.judging-rubric { overflow-x: auto; }
.judging-rubric table { width: 100%; min-width: 30rem; }
.judging-rubric th:nth-child(2),
.judging-rubric td:nth-child(2) { text-align: center; white-space: nowrap; }
.judging-rubric:focus-visible { outline: 2px solid #7253ed; outline-offset: 3px; }
</style>

## A. How judging works

1. Teams demonstrate their completed projects to the judging panel.
2. Judges assess the implementation, working demonstration and repository.
3. Each judge independently completes a score sheet using the published criteria for the applicable category.
4. Organisers consolidate the completed scores.
5. Winners are selected within each eligible category under the approved award structure.

### Eligibility checks
{: #preliminary-eligibility-gate-vs-scoring }

Eligibility is checked separately from marks. Only categories a team enters and qualifies for are considered. Follow the [competition requirements]({{ site.baseurl }}/challenges/#the-official-mlh-challenge), [rules]({{ site.baseurl }}/rules/) and [submission guide]({{ site.baseurl }}/submission/).

## B. Prize categories and judging criteria
{: #category-specific-evaluation-lenses }

{: .important }
> **Proposed organiser scoring criteria:** These are **not official MLH-published scoring weights**. Final approval and confirmation against the event's OrganizerHQ category settings are pending; the approved criteria will be published before judging.

The two confirmed MLH categories are distinct. **One submission may enter both when it meets both sets of requirements**; no duplicate project or repository is needed.

<section class="judging-card" markdown="1">

### Category 1: Best Open-Source AI Project

**DigitalOcean-supported.** Build an original, functional and useful solution in which open-source/open-weight AI makes an important contribution. **Gemma 4 is not required, and DigitalOcean is optional.**

Your public GitHub repository must include an appropriate open-source code licence and a README explaining the project, setup, model and key dependencies. Identify the model and link its licence or terms: **open-weight and open-source are not interchangeable labels**. Demonstrate the AI contribution in the running product.

Agent skills must follow the [Agent Skills open standard](https://agentskills.io/). Model harnesses need original implementation or meaningful changes, not just a new name. These are examples of eligible project forms, not required architectures.

<div class="judging-rubric" role="region" aria-label="Best Open-Source AI Project scoring criteria" tabindex="0" markdown="1">

| Criterion | Weight | What judges assess |
|---|:---:|---|
| Problem relevance and practical impact | 15 | A clear user need and a useful, demonstrated outcome. |
| Meaningful use of open-source/open-weight AI | 20 | AI performs an important function in the product, rather than only helping write its code. |
| Technical execution and working demonstration | 20 | The core user journey works; the team can explain its implementation, tests and failure handling. |
| Originality and innovation | 15 | Original thinking, useful adaptation and a clear contribution beyond existing tools or tutorials. |
| Open-source quality, licensing and documentation | 20 | Public code, appropriate licensing, model/dependency disclosure, attribution and instructions another developer can follow. |
| Responsible AI, privacy and safety | 10 | Appropriate data permissions, privacy safeguards, tested limitations and human control where needed. |
| **TOTAL** | **100** | |

</div>

[Read the official category description](https://www.mlh.com/events/hacktoberfest-hack-day-nairobi-x-itech-club/challenges/01a0d987-0c41-12ea-13ac-5b85755dc2f3).

</section>

<section class="judging-card judging-card--gemma" markdown="1">

### Category 2: Best Use of Gemma 4

**Gemma / Google DeepMind.** Show how effectively Gemma 4 contributes to the actual product. An unused dependency, model configuration or README mention does not demonstrate integration.

Identify the exact Gemma 4 variant, inference route and model terms in your code and README. **A Gemini model is not Gemma 4.** Choose capabilities appropriate to your problem and supported by your variant; a strong text-only tool is welcome. Neither multimodal features nor a particular application domain are compulsory.

Follow the [published MLH Gemini API winner guidance](https://hacktoberfest-handbook.mlh.com/hack-days-partner-modules/partner-challenge-google-gemma). Local inference support alone does not establish prize eligibility; confirm any local-only entry with organisers. Consult the current [model card and capabilities](https://ai.google.dev/gemma/docs/core/model_card_4).

<div class="judging-rubric" role="region" aria-label="Best Use of Gemma 4 scoring criteria" tabindex="0" markdown="1">

| Criterion | Weight | What judges assess |
|---|:---:|---|
| Meaningful integration of Gemma 4 | 25 | Gemma 4 performs a genuine product function, with a verifiable model variant and appropriate inference route. |
| Effective use of Gemma 4 capabilities | 20 | The application uses supported capabilities well for its task; extra modalities earn no automatic bonus. |
| Technical execution and working demonstration | 20 | A working end-to-end journey, sound integration, repeatable tests and handling of errors or uncertainty. |
| Problem relevance and usefulness | 15 | A clearly identified user and an outcome that helps solve their problem. |
| Originality and innovation | 10 | A distinctive idea or meaningful adaptation, with the team's contribution clearly explained. |
| Responsible AI, privacy and safety | 10 | Proportionate safeguards, privacy, appropriate data use and honest disclosure of model limitations. |
| **TOTAL** | **100** | |

</div>

[Read the official category description](https://www.mlh.com/events/hacktoberfest-hack-day-nairobi-x-itech-club/challenges/01a03b87-be22-9180-5e2d-b3beeb66666d).

</section>

### Fair assessment across projects
{: #fair-cross-track-evaluation }

- The same category criteria apply across problems, domains and interfaces. There are no hidden points, provider bonuses or extra marks for model size, spending, pull-request counts or commit volume.
- Show a normal test, an edge case and a failure or uncertainty case. Judges assess working evidence, not presentation polish alone.
- Missing functionality affects the relevant criterion; an incomplete prototype is not automatically disqualified. Published eligibility and conduct rules still apply.
- Teams receive equal presentation time under the final organiser schedule. Judges with a mentoring, code-contribution or personal/academic conflict recuse themselves.

## C. Scoring scale

Each criterion receives an **integer rating from 0 to 5**.

| Rating | Meaning |
|:---:|---|
| 0 | Not demonstrated |
| 1 | Very poor |
| 2 | Below expectations |
| 3 | Meets expectations |
| 4 | Very good |
| 5 | Excellent |

### Weighted points
{: #the-100-point-score-sheet }

<a id="the-100-point-operational-rubric"></a>

**Weighted score = (Judge rating / 5) × Criterion weight.**

For example, a rating of **4** on a **20-point** criterion earns **16 points**. Add the six weighted scores for a **category total out of 100 points**. A project entered in both categories receives separate evaluations, not a combined 200-point score.

## D. Final selection

### Consolidating scores
{: #score-tabulation-process }

Organisers average the completed independent score sheets **separately for each category**. Each contender receives at least two non-conflicted reviews.

**Final category score = sum of valid judge category totals / number of valid judges.**

Each judge has equal weight. Only complete, valid sheets count; missing marks are not zero. Scores are compared before rounding, and individual score sheets remain private.

Within each eligible category, the highest consolidated score under the approved rubric leads selection, subject to the applicable published award requirements. A local overall score does not determine either MLH category winner.

### Tie-breaking
{: #deterministic-tie-breaking-protocol }

For an MLH category tie, the non-conflicted panel reviews the tied projects' evidence against that category's published criteria and reaches a consensus under the approved category rules. No extra criteria or unpublished bonuses are added.

For **local overall assessment only**, the existing order remains: higher average meaningful AI integration score, then higher average technical execution score, then panel consensus against the local rubric. This is not an official MLH category tie-breaker.

### Award structure

The two MLH category awards remain separate from the retained **iTech Club local awards**:

- **First Place - Overall Winner**
- **Second Place - Overall Runner-up**
- **Third Place - Overall Third Place**

Local awards, eligibility and prizes remain subject to organiser confirmation.

If local overall assessment is confirmed, its existing weights remain **problem relevance 15, AI integration 20, technical execution 25, originality 15, responsible AI 10 and open-source quality/reproducibility 15** (100 total), using the same rating scale and averaging method. The proposed category tables above do not replace that separate local rubric.

One project may enter both MLH categories, but **whether the same team may receive both prizes still requires organiser/MLH confirmation**.
