# gap.md — what_is_language

**Last updated:** 2026-04-09 (attempt_002)
**Phase:** 1 (moving toward 2)

## The gap, in one sentence

> **Human children reach fluent language on ~10⁷ linguistic tokens. Frontier text-only LLMs need ~10¹³. What accounts for the ~10⁶× compression that humans enjoy — and can any single mechanism close the ratio?**

## Why this is the gap

The Sigma Method requires the gap to be a number, not a concept. In the language question, the cleanest number on the table right now is the **sample-complexity ratio** between human and LLM language acquisition: **four to six orders of magnitude**.

Every ontology of language (Universal Grammar, embodiment, usage-based, distributional) can be re-stated as a claim about what closes that ratio. That is progress: the metaphysical positions become empirical predictions.

## The ratio, precisely

| System | Tokens to fluent conversational competence | Order of magnitude |
|--------|-------------------------------------------|-------------------|
| Human child (central estimate, by age 5) | ~3 × 10⁷ words | 10⁷ |
| Human child (upper bound, heavy input) | ~10⁸ words | 10⁸ |
| LLM (Chinchilla, 2022) | 1.4 × 10¹² tokens | 10¹² |
| LLM (LLaMA-3, 2024) | 1.5 × 10¹³ tokens | 10¹³ |
| LLM (frontier, 2025–26) | ~10¹³–10¹⁴ tokens | 10¹³ – 10¹⁴ |

**Ratio (central):** 10⁶.
**Ratio (conservative lower bound):** 10⁴.

Tokens and words are not identical units; a factor of 1.3–1.5× in either direction does not dent an order-of-magnitude argument.

## What closing the gap would look like

- **UG confirmed:** a human-scale corpus (~10⁷ tokens) plus an innate bias inspired by linguistic universals reaches fluency; the same corpus without the bias does not.
- **Embodiment confirmed:** adding multimodal grounding (vision, audio, action-consequence) to a ~10⁷-token text corpus reaches fluency; text alone at the same scale does not.
- **Usage-based confirmed:** adding an active interlocutor / corrective-feedback loop to a ~10⁷-token interaction reaches fluency; passive exposure to the same tokens does not.
- **Distributional (full-strength) confirmed:** a plain transformer on a curated, clean ~10⁷-token corpus reaches fluency with the right data composition. Sample complexity is a matter of data quality, not kind of signal.

Each of these is a concrete experimental target. Each has some evidence already. None is fully settled.

## What "fluent" means in this document

Provisional operational definition (refinable): able to pass a held-out conversational benchmark (e.g. MMLU-language subset, BLiMP, a discourse-coherence test) at adult-human level, plus grammatical acceptability judgments matching native-speaker norms. The point is not this specific definition — it is that the definition must be fixed before the sample-complexity claim is meaningful. attempt_003 or later will select a concrete benchmark.

## Known compression mechanisms (partial credit)

No single mechanism is proven to close the full 10⁶. Each has evidence for partial compression:

| Mechanism | Approximate compression seen in literature | Source |
|-----------|-------------------------------------------|--------|
| Multimodal grounding | ~10× | VL bootstrap studies, Flamingo-era results |
| Curriculum learning | 2–10× | Bengio 2009 line, child-directed-speech studies |
| Instruction tuning + feedback | 10–100× at task level, less at pretraining | RLHF literature |
| Active / curiosity-driven selection | 2–10× in synthetic benchmarks | Active learning lit |
| Architectural inductive bias | unclear, often <10× | Tree-RNN vs. transformer ablations |

Adding these multiplicatively, you get maybe 10³–10⁴×. That leaves 10²–10³× unaccounted for. **The residue is the real gap.**

## The anti-problem

What would it mean for the gap to NOT exist?

- If humans actually need the same 10¹³ tokens and we are mismeasuring child input: then LLMs and humans are on the same learning curve and there is no puzzle. This would require roughly a 10⁵× underestimate of child input, which is implausible under any measurement methodology.
- If LLMs are not actually fluent in the way humans are and we are mismeasuring LLM output: then the apparent no-gap is an illusion of superficial competence. This is the steelman of Chomsky's "they're not doing language" response. It is not falsifiable by current benchmarks.

The anti-problem therefore points at **measurement**: the gap is real if and only if our measurements of (a) child input and (b) LLM fluency are both roughly correct. Strengthening those two measurements is the first concrete research move.

## Sky bridges to adjacent generative questions

- **what_is_mind** — the compression gap may be a proxy for the hard problem. Humans may be cheap learners because they are minds, and minds do something with data that transformers don't. If true, the language gap inherits the hardness of the consciousness gap.
- **what_is_meaning** — if grounding closes part of the gap, reference and meaning become compression priors. Meaning is not a mystery on top of syntax; it is structure that makes syntax cheaper to learn.
- **what_is_knowing** — children learn from very few examples because they already know a lot (object permanence, agency, causality). Prior knowledge compresses new learning. Epistemology meets statistics.
- **what_is_number** — if learning is cheap when structure is pre-known, mathematics looks like the maximally compressible domain: infinite correct sentences recoverable from a tiny seed. The number question may be the compression question in its purest form.
- **what_is_self** — active learners are cheaper than passive ones. Agency is a compression prior. Self-as-learner may be a computational necessity rather than a luxury.

These are hypotheses, not claims. The bridges get built as the other problems develop.

## Current status

Phase 1 (foundation) done by attempt_001.
Phase 2 (quantification) begun by attempt_002. Sample-complexity ratio is the first handle.

Next: attempt_003 will enumerate other candidate measurable separations (compositional generalization, systematicity, long-range consistency, metalinguistic awareness, reference) and rank each by decisiveness.
