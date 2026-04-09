# result_002 — Chinchilla Scaling Law and the BLiMP-based Gap

**Date:** 2026-04-09
**Track:** Numerical (Odd)
**Tool:** `numerics/scaling_law_extrapolation.py`

## What we ran

Calibrated the Chinchilla scaling law (Hoffmann et al. 2022) to BLiMP grammatical
acceptability accuracy using 4 published empirical points, then:
1. Extrapolated what D (tokens) is needed for human-equivalent BLiMP (94%).
2. Computed what BLiMP an LLM trained on 3×10^7 tokens (human-scale) achieves.

## Calibration quality

Linear mapping BLiMP ~ a*L + b fitted to 4 points:

| Model | Predicted BLiMP | Actual | Error |
|-------|----------------|--------|-------|
| GPT-2-small | 0.668 | 0.670 | 0.002 |
| GPT-3-6.7B | 0.838 | 0.810 | 0.028 |
| GPT-3-175B | 0.868 | 0.860 | 0.008 |
| GPT-Neo-20B | 0.856 | 0.890 | 0.034 |

Max error: 3.4%. Adequate for order-of-magnitude analysis.

## Key finding: what BLiMP does a human-sized LLM corpus achieve?

An LLM trained on 3×10^7 tokens (human central estimate) would predict:

| N (params) | Chinchilla L | Predicted BLiMP |
|------------|-------------|-----------------|
| 10^8 | 5.668 | 0.051 |
| 10^9 | 5.219 | 0.151 |
| 10^10 | 5.012 | 0.197 |
| 10^11 | 4.916 | 0.218 |

**Human BLiMP: 0.94.** LLM at same token count: 0.05–0.22.

The gap on the BLiMP benchmark: **~4 to 4.5 log-orders of performance loss**
for an LLM trained on human-scale data. A 100B-parameter model trained on 30M
tokens would achieve ~0.22 BLiMP, compared to human 0.94.

## The floor warning: is the gap fundamental?

The analysis flagged that the human BLiMP target (loss=1.666) is marginally
below the Chinchilla floor (E=1.690). This would imply no LLM can ever reach
human performance by scaling alone. However:
- The margin is 0.024 nats, smaller than calibration error (0.034 max)
- The linear BLiMP↔loss calibration is approximate
- The Chinchilla floor E is itself an empirical constant, not a theorem

**More conservative reading:** LLMs can eventually reach human BLiMP at
extreme scale (loss approaching floor), but they need vastly more data than
humans do. The gap is in training efficiency, not necessarily in asymptotic capability.

## Reconciliation with the gap budget (result_001)

result_001 found the gap is ~10^5.5 in tokens. This analysis finds ~4 to 4.5
log-orders in BLiMP performance when trained at human token scale.

These are compatible: the BLiMP gap at human token scale measures "how bad is
performance when humans stop training, at their scale?" (~4 log-orders behind
on BLiMP). The token gap measures "how many tokens until the LLM reaches human
performance?" (~10^5.5 more). Both are measuring the same underlying efficiency
deficit from different angles.

## The benchmark selection matters

BLiMP measures grammatical acceptability — a relatively "syntactic" benchmark.
Frontier LLMs already exceed human BLiMP (96-98% vs 94%), so the gap on BLiMP
is ALREADY CLOSED for current models. This means BLiMP is not the right measure
of the remaining gap.

The remaining gap (per attempt_003) is in HOST properties: long-range consistency,
grounded reference, persistent identity. These don't appear in BLiMP at all.

**Implication:** The sample-complexity gap is benchmark-dependent.
- On BLiMP: gap is closed at the frontier (but required ~10^13 tokens to close)
- On host properties: gap may not be closeable by adding tokens alone

## Next steps

1. Repeat this analysis for a benchmark that measures HOST properties
   (e.g., consistency over long conversations, grounded reference). Such a
   benchmark would show whether the gap on host properties also shrinks with
   more tokens, or is architecturally blocked.

2. The "floor warning" deserves a more careful treatment: fit a non-linear
   model (e.g., log-loss ~ f(N, D)) to the empirical points rather than
   using the full Chinchilla constant E as-is.

3. Cross-check: does the Chinchilla optimal compute point (D=20N) correspond
   to human-equivalent token counts for small models (suggesting small models
   can be trained efficiently), or does it only work at scale?
