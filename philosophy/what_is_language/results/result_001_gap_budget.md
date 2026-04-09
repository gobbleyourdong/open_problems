# result_001 — Sample-Complexity Gap Budget

**Date:** 2026-04-09
**Track:** Numerical (Odd)
**Tool:** `numerics/sample_complexity_gap.py`

## What we ran

Quantitative analysis of the 10^6 sample-complexity gap between human and LLM
language acquisition. Computed:
1. Raw gap from central estimates
2. Stacked compression from all known mechanisms
3. Residual gap after stacking
4. Budget analysis (holding-one-out)
5. Sensitivity sweep over human/LLM token estimates

## Key numbers

**Raw gap (central estimate):** ~10^5.5 (333,000×)
- Human tokens to fluency: 3×10^7 (central)
- LLM tokens to fluency: 10^13 (frontier 2025-26)

Note: the Even track stated "10^6" — this computation gives 10^5.5 for central
estimates and 10^6 only if using LLaMA-3 (1.5×10^13) and low human estimate
(10^7). The gap is in the right ballpark but is closer to 10^5.5 than 10^6
for current frontier models.

## Central finding: the gap is over-explained

Stacking all known mechanisms multiplicatively:

| Mechanism | Factor | Cumulative |
|-----------|--------|------------|
| Multimodal grounding | ×10 | 1×10^1 |
| Curriculum learning | ×5 | 5×10^1 |
| Instruction tuning + RLHF | ×30 | 1.5×10^3 |
| Active learning | ×5 | 7.5×10^3 |
| UG / inductive bias | ×100 | 7.5×10^5 |
| Prior world knowledge | ×20 | 1.5×10^7 |

Total stacked compression: **10^7.2** — closes **10^7.2** of a **10^5.5** gap.

**The known mechanisms over-explain the gap by roughly 50×.**

## What this means

The over-explanation forces a choice between three interpretations:

### A. The mechanism estimates are inflated

Most factors are rough literature orders-of-magnitude, not controlled
measurements. Multimodal grounding "×10" comes from VL task-level studies,
not pure language learning. Curriculum learning "×5" is averaged over many
settings. If each estimate is inflated by 2-3×, the total compression collapses
from 10^7 to 10^5–10^6, which closes the gap without residual.

**Implication:** The gap is fully explained by imprecisely estimated known
mechanisms. No mysterious residue. The research program becomes: measure each
mechanism's actual compression factor for CORE language acquisition, not tasks.

### B. The mechanisms don't stack multiplicatively

The mechanisms are not independent. A model with multimodal grounding AND
curriculum learning benefits less from both together than from each alone
(because both reduce the same variance, not orthogonal variance). If mechanisms
have 50% overlap, effective stacked compression drops from 10^7 to ~10^3.5,
leaving a residual of 10^2 — which still requires the UG/world-knowledge
mechanisms to close.

**Implication:** Mechanism independence is the key empirical question. The
residual gap exists iff the mechanisms overlap substantially.

### C. The gap is larger than estimated

The "fluency" benchmark for LLMs is ill-defined. If "fluency" means something
more demanding than current benchmarks (e.g., consistent multi-turn reasoning,
reliable metalinguistic awareness), frontier LLMs are not yet fluent, and the
effective LLM token count for TRUE fluency might be 10^14 or higher —
pushing the raw gap back toward 10^6–10^7.

**Implication:** The gap measurement is the primary empirical uncertainty.
The Even track (attempt_003) identified this: the behavioral separator is
"HOST properties," not language per se. The fluency definition is load-bearing.

## Budget analysis result

Under the holding-one-out analysis, when all other mechanisms contribute their
literature estimates, the UG prior only needs to contribute ×2.2 to close the
gap — not the ×1000+ that would make it a decisive, unfalsifiable appeal to
innate structure.

This is significant: **UG at ×2 is a reasonable, falsifiable claim.** It
predicts that an LLM with ×2 better compositional inductive bias (compared to
a plain transformer) would close the remaining gap. This is testable with
controlled architecture ablations.

## Connection to the three-mountain structure

attempt_003 found that the remaining behavioral separators between humans and
LLMs are about HOST properties (grounding, memory, agency), not about language
itself. This budget analysis is consistent: the mechanisms that contribute the
most compression (grounding ×10, active learning ×5, world knowledge ×20) are
ALL host properties. Language-internal mechanisms (curriculum, UG) contribute
×5 and ×100 respectively — and even these may be partially present in LLMs
through instruction tuning.

**The gap budget formalises the three-mountain connection:** the sample-
complexity gap is NOT primarily a language problem. It is a HOST problem. The
language gap closes once the host is instantiated. This is the same conclusion
attempt_003 reached from the behavioral separator analysis, arrived at
quantitatively from a different direction.

## Next steps (numerical track)

1. **Refine human token estimate**: the current range spans 10× (10^7 to 10^8).
   Narrowing this to a factor of 2 would substantially clarify the analysis.
   Target: find the best current estimate for tokens-to-fluency from developmental
   psycholinguistics literature (Snow 1994, Hart & Risley 1995 updates).

2. **Independence analysis**: empirically test mechanism overlap by analyzing
   studies that combine mechanisms (e.g., grounded language learners with
   curriculum vs. without). This requires a literature survey, not computation.

3. **Fluency benchmark selection**: identify the single benchmark that is most
   "decisive" in the sense of attempt_003's decisiveness scale. The token-to-
   fluency estimate is only well-defined once the benchmark is fixed.

4. **LM scaling law extrapolation**: use the Chinchilla scaling coefficients
   to extrapolate what token count achieves the same performance as a human
   at age 5 on a specific benchmark. This gives a more principled LLM token
   estimate than "frontier models are fluent."

## Status

First quantitative pass complete. Central finding: the gap is 10^5.5, known
mechanisms collectively over-explain it, and the residual depends critically on
mechanism independence and fluency definition. The over-explanation is itself
informative: no single mechanism is required; the explanation is distributed.
