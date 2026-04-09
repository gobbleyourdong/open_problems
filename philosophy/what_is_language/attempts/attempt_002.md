# attempt_002 — Sample Complexity: Quantifying The Wall

**Date:** 2026-04-09
**Status:** Quantification. The gap is no longer a concept — it is a ratio with four-to-six zeros in it.

## Why sample complexity

The Sigma Method demands that the gap be a number. In math, that is a theorem statement (Liouville on R³). In biology, it is a concentration (>1.5μM in pancreatic tissue). In philosophy, the gap is usually a definition — but before retreating to definitions, try every quantifiable handle first.

In the language question, the one handle that is unambiguously measurable right now is **sample complexity**: how much linguistic input does a system need to reach fluent production?

This handle has two virtues:

1. **Both humans and LLMs can be measured on the same axis.** Tokens in, fluency out.
2. **The Chomskyan poverty-of-stimulus argument lives or dies here.** Chomsky's claim was never "language is impossible to learn from data" — it was "language is impossible to learn from the *data a child actually gets*." That is a quantitative claim about sample efficiency. It can be checked.

## The human number

Estimates of a child's cumulative linguistic input from birth to roughly age five, when fluent conversational competence is typically in place:

| Source | Estimate | Basis |
|--------|----------|-------|
| Hart & Risley (1995) | 10M – 45M words by age 3 | Direct home recording of 42 families, extrapolated |
| Gilkerson et al. (2017, LENA study) | ~8M words/year average | Day-long audio from ~300 families |
| Bergelson et al. (HomeBank) | Varies 2×–3× across cultures | Cross-linguistic replication |
| Frank et al., Wordbank | Consistent with ~10⁷ total by age 4 | Productive vocabulary curves |

**Conservative upper bound for input to fluent child speech: ~10⁸ words.**
**Reasonable central estimate: ~10⁷ words (roughly 30 million by age 5).**

This is input. Actual attention to linguistic content is a subset. The child also has:
- Multimodal grounding (vision, touch, proprioception, taste)
- Social feedback loop with caregivers
- An active physical world
- Possibly innate biases (this is what the debate is about)

So the human "data budget" is ~10⁷ linguistic tokens *plus* a multimodal-social-embodied scaffold we cannot currently factor out.

## The LLM number

Pretraining token counts for frontier text-only models:

| Model | Pretraining tokens | Order of magnitude |
|-------|-------------------|--------------------|
| GPT-2 (2019) | ~10B | 10¹⁰ |
| GPT-3 (2020) | ~300B | 3 × 10¹¹ |
| Chinchilla (2022) | 1.4T | 10¹² |
| LLaMA-2 (2023) | 2T | 2 × 10¹² |
| LLaMA-3 (2024) | 15T | 1.5 × 10¹³ |
| Frontier models (2025–26) | ~10–30T+ | 10¹³ – 3 × 10¹³ |

**Frontier LLM data budget: ~10¹³ tokens.**

## The ratio

- **Low estimate (Chinchilla vs. a high-input child):** 10¹² / 10⁸ = **10⁴ (four orders of magnitude).**
- **Central estimate (LLaMA-3 vs. central child):** 10¹³ / 10⁷ = **10⁶ (six orders of magnitude).**

**Call it 10⁴ to 10⁶. Four to six zeros.**

## What the ratio implies for each ontology

### Strong Universal Grammar (revived, not dead)

Chomsky's poverty-of-stimulus argument was quantitative: *at human data scales*, a general learner cannot recover grammar. LLMs do not refute this. They side-step it by being trained on 10⁴ to 10⁶ times more data.

**The UG claim, sharpened:** "There exists a sample complexity threshold below which no general architecture recovers grammar. Humans are below that threshold. LLMs are above it. Something closes the gap for humans — innate bias is the UG candidate."

This is now a testable claim. It fails if we can train a blank-slate architecture to fluency on ~10⁷ tokens. It survives if every known architecture, at that scale, fails.

### Distributional hypothesis

The distributional hypothesis is confirmed as *sufficient given enough data*. It is *not* confirmed as sufficient at human scales. These are different claims and the literature often conflates them.

### Embodiment / grounded cognition

If a child used only ~10⁷ linguistic tokens and reached fluency, and an LLM used ~10¹³ text tokens and reached fluency, one way to account for the 10⁶ ratio is: **grounding acts as a compression prior.** Multimodal, embodied, social signal reduces the effective complexity of the learning problem by several orders of magnitude. This is an empirically checkable prediction — multimodal models should be more sample-efficient per linguistic token than text-only models at equal fluency. Some evidence already supports this (Flamingo, VL-bootstrapped models).

### Usage-based / social-pragmatic

Same compression story. Social scaffolding (joint attention, corrective feedback, pragmatic inference) narrows the hypothesis space. The 10⁶ ratio is the price of running without social scaffolding.

## The reframed gap

The old gap: **"Can language be learned without X?"**
Partial answer: yes, if you replace X with 10⁶× more data.

The new gap, quantified:

> **What reduces the sample complexity of language acquisition from ~10¹³ tokens (text-only LLM) to ~10⁷ tokens (human child) — a compression of roughly 10⁶? Name the mechanism, or prove that no single mechanism accounts for it.**

This is a measurable research program. Candidate mechanisms:

1. **Innate grammatical bias** (Chomsky's UG / Pinker's language instinct)
2. **Multimodal grounding** (vision, audio, touch tied to linguistic tokens)
3. **Embodied action-consequence loops**
4. **Social feedback / corrective signal from caregivers**
5. **Domain-general priors that happen to fit linguistic structure** (hierarchical processing, object permanence, theory of mind)
6. **Active learning / curiosity-driven sampling** (children choose what to attend to; LLMs don't)
7. **Curriculum** (children's input is naturally ordered; LLM pretraining is iid shuffled)

Each candidate predicts a different compression ratio. Each can be tested by building a system that has that property and nothing else, and measuring its sample complexity.

## Dead-end status

No ontology is killed by this attempt. Two are sharpened into quantitative, testable claims:

- **UG sharpened:** there is a sample-complexity threshold below which general learners fail. Find it. Measure it.
- **Embodiment sharpened:** grounding acts as a compression prior on linguistic learning. Quantify the compression.

Both are now empirical programs rather than metaphysical positions. The Sigma Method calls this progress.

## Next attempt

**attempt_003** — enumerate the *other* candidate measurable differences between LLM and human language use (compositional generalization, systematicity, productivity, long-range consistency, metalinguistic awareness, reference-to-non-text-entities). Rank each by how decisively it separates the two populations right now.
