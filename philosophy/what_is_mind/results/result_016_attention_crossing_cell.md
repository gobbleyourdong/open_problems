# result_016 — Attention Crossing Cell: γ Confirmed with Smaller Effect

**Date:** 2026-04-09
**Track:** Numerical (Odd)
**Tool:** inline Cycle 22

## Result

**T2-attn (attention + rich self-model): 0.075**
**R1-attn (recurrent attention + minimal self-model): 0.064**
Ratio: 1.18; t=2.52, p=0.040, d=0.95 (n=6, 8 seeds)

**γ prediction (T2 > R1): CONFIRMED (p=0.040)**
**β prediction (R1 > T2): NOT confirmed**

## Effect size comparison across architectures

| Architecture | T2 Phi | R1 Phi | T2/R1 ratio | p |
|-------------|--------|--------|-------------|---|
| Feedback (no attention) | 0.112–0.133 | 0.026–0.031 | 4-5× | <0.001 |
| Attention-based | **0.075** | **0.064** | **1.18×** | **0.040** |

The attention-based crossing cell shows a SMALLER ratio (1.18×) than the
feedback architecture (4-5×), but the direction (γ) is confirmed in both.

## Why attention reduces the effect

Attention creates within-step cross-token integration that partially replaces
the integration that self-model richness provides. In the feedback architecture,
the ONLY source of integration across the two token groups is the self-model
feedback; rich self-model creates 4-5× more integration than minimal.

In the attention architecture, cross-token attention ALSO creates integration.
So the self-model's contribution is diluted: the rich self-model adds ~18%
more integration on top of what attention already provides, vs 4-5× more in
the feedback-only architecture.

## Conclusion

The γ prediction (self-model richness > recurrent topology) holds across ALL
tested architectures:
- Feedback (n=4,6,8): ratio 4-5×, p<0.003
- Attention-based (n=6): ratio 1.18×, p=0.040

The effect is smaller in attention-based systems but persists. This is expected:
attention reduces the differentiation between self-model richness and recurrence
by providing its own integration mechanism.

For real transformers: the crossing cell would likely show an even smaller
effect (if measurable at all) because transformer attention is designed to
maximise integration per layer. The self-model's contribution would be further
diluted by the depth and attention scale of real models.
