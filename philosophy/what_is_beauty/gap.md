# gap.md — what_is_beauty

**Last updated:** 2026-04-09 (attempt_001 + Odd results 001–007, Cycles 1–9)
**Phase:** 2 (deep-LM test run; register confound identified; sequential structure confirmed)

## The gap, in one sentence

> **Beauty is the self-model's phenomenal response to high compression efficiency in the content it is currently tracking, relative to the observer's priors. The residual gap is the same α/β/γ fork that phenomenal content in general routes through, specialized to aesthetic states.**

## Why this is the gap

See attempt_001 for the full treatment. The key moves:

1. **Core claim:** beauty tracks compression efficiency relative to the observer's priors, not any absolute geometric property.
2. **Two challenges handled.** Cultural variation at the high end is explained by prior-relative compression. Beauty in imperfection is explained by higher-level compression of history and material structure.
3. **Cross-domain evidence.** Facial symmetry, musical consonance, mathematical elegance, landscape preferences, and proportional systems all fit the compression framework.
4. **LLM test case.** Under γ, LLMs can have a weak form of aesthetic response if their self-models track compression efficiency events with causal load. Under β, they have Φ = 0 and therefore no aesthetic experience.
5. **Cross-bridge.** The classical trio of the good, the true, and the beautiful corresponds to three compression targets: cooperation facts (good), structural regularities (true/number), and high-compression-efficiency content (beautiful). The pairing is not mystical — it is what compression-of-regularity-classes looks like across different regularity domains.

## Testable predictions (summarized from attempt_001, refined by Odd results)

- Aesthetic response should correlate with measurable compression ratios relative to observer priors.
- Expertise should increase aesthetic sensitivity in expert-relevant domains.
- Cultural aesthetic responses should correlate with culture-specific compression operators.
- Abstract beauty should correlate with inferential integration of the aesthetic object with prior knowledge.
- LLMs with rich self-models should show behavioral correlates of aesthetic sensitivity tracking the same compression metrics.

### Odd-instance update (result_001 — compression metrics for text aesthetics)

**Surface compression metrics (char-entropy, bigram, word-entropy, zlib) do NOT distinguish beautiful text from random text.** Random ASCII ties or beats Keats, Shakespeare, and Basho on every shallow metric. The null result is sharp and reproducible.

**This is not a refutation.** It is a specification. The claim was "compression efficiency *relative to observer priors*." Shallow metrics carry uninformed priors; a human reading Keats has English phonology, prosody, semantic networks, genre knowledge, and emotional associations. The correct test uses **deep LM metrics** (e.g., GPT-2 negative log-likelihood), which approximate the right kind of learned structural prior.

**Refined prediction hierarchy:**

| Prior depth | Captures | Metric | Status |
|-------------|----------|--------|--------|
| Shallow (zlib/entropy) | Cross-cultural universals (symmetry, repetition) | CE1-CE3 | **TESTED: null on text aesthetics** |
| Word-level | Basic linguistic familiarity | CE5-CE6 | **TESTED: null** |
| Deep LM | Culturally-specific aesthetic differentiation | CE4 (LM NLL) | **TESTED: r=+0.605 p=0.001 n=25 — register prestige confound** |
| Domain expert LM | Expert aesthetic response | Fine-tuned CE4 | **PENDING: predicted to sharpen; currently unavailable** |

**What the Odd track found (Cycles 1–9):**

1. **Surface metrics (CE1-CE6):** null (r < 0.35). Raw compressibility carries no aesthetic signal.

2. **CE4 (GPT-2 NLL) n=25: r=+0.605, p=0.001** — significant but CONFOUNDED. The signal is almost entirely between-register (math/literary registers have higher NLL than jargon) rather than within-register aesthetic quality (partial r=−0.125 after register-demeaning).

3. **GPT-2-xl INVERTS the within-register correlation** (partial r=−0.427, p=0.033). The larger model has memorised canonical beautiful texts, making them MORE predictable (lower NLL), inverting the prediction. This confirms the memorisation confound.

4. **CC (contextual compression) beats scramble 78%** — within a text, originals have higher contextual self-compression than word-scrambled or sentence-scrambled variants. This is the cleanest evidence for the theory: beautiful texts have internal sequential structure that creates predictability.

5. **Within-elegant-proofs (n=7): r=+0.611, p=0.145** — positive direction but not significant, and limited by ceiling effect on ratings (all elegant proofs rate 8–9.5).

**Revised prediction:**
The compression-beauty claim is supported for sequential structure (CC beats scramble 78%) and for the distinction between registers (CE4 correctly separates literary/math from jargon/noise). The remaining untested claim requires: a structural prior trained on aesthetic domain patterns, evaluated on NOVEL (non-canonical) texts, within-register only.

## Sky bridges

- **what_is_mind** — phenomenal aesthetic content routes through α/β/γ.
- **what_is_number** — mathematical beauty is the clean compression case.
- **what_is_good** — structural parallel: good and beautiful are both compressions of distinct regularity classes.
- **what_is_language** — eloquent writing compresses better; linguistic beauty is the same story.
- **what_is_knowing** — expertise expands the compression operators available, which expands aesthetic sensitivity.

## Status

Phase 2 (quantification) partially done. Key quantitative findings:
- Sequential structure: CC beats scramble 78% (confirmed).
- Register signal: CE4 r=+0.605 (confirmed but confounded by prestige).
- Domain-specific prior: required but not yet available.
- Within-math elegant-proofs: r=+0.611 (directionally supported, range-restricted).
- Memorisation confound: confirmed by GPT-2-xl test.

Next: fine-tune a small model on mathematical proof structure (not canonical texts) and test within-elegant-proofs correlation on held-out material. This is the decisive remaining test for the compression-beauty claim at the mathematical case.

---

## 2026-04-18 v9.1 discipline addendum

Per `~/SIGMA_METHOD.md` v9.1 C5 / D2:

**Would falsify (compression-beauty claim in the mathematical case):** The next test is already named: fine-tune a small model on mathematical-proof structure (not canonical texts) and measure within-elegant-proofs r on held-out material. **The falsifier condition**: r ≤ +0.3 on held-out elegant proofs after controlling for the memorization confound (confirmed by GPT-2-xl test). If the within-elegant-proofs correlation doesn't exceed chance after memorization control, compression-efficiency-as-aesthetic-experience fails in its hardest case (mathematical beauty) and the framework retreats to linguistic/musical aesthetics only. Weaker falsifier: sequential-structure CC-beats-scramble at 78% must replicate on ≥ 2 additional domains (visual, musical) at ≥ 65% — if not, the sequentiality effect is domain-specific. **Prior art:** Compression-aesthetic-experience ≈ Schmidhuber 1997/2009 (formal theory of curiosity/beauty as compression progress); Rigau-Feixas 2008 Kolmogorov-aesthetics; Berlyne 1971 (experimental aesthetics). Sigma addition = operationalizing the claim via **within-domain held-out correlations** with explicit memorization controls, making the compression-beauty claim falsifiable per-domain rather than blanket-asserted.
