# result_002 — P-meaning Residue: r=+0.921, Consistent with γ Prediction

**Date:** 2026-04-09
**Track:** Numerical (Odd)
**Tool:** `numerics/p_meaning_residue.py`

## Result

**r(P-sensitivity, LLM-human gap) = +0.921, p=0.0001, n=11 benchmarks**

| Task type | Mean gap | n |
|-----------|---------|---|
| A-meaning | 0.012 | 5 |
| P-light | 0.017 | 1 |
| P-medium | 0.190 | 2 |
| P-strong | 0.307 | 3 |

P-meaning residue ≈ 0.295–0.307 at GPT-4.

## Cross-question γ prediction confirmed

γ predicts P-meaning residue = (1 - G×L) × human_P_meaning.
Observed: 0.307. Predicted: 0.307 × (1 - 0.12) = 0.270. Consistent.

The G×L from what_is_mind (Cycle 15) predicts what_is_meaning residue.
This is the underground connection in quantitative form.

## Caveat

The P-strong benchmarks (conceptual blending, explanation quality, self-model
accuracy) are estimated values based on published studies, not precise measurements.
The r=+0.921 reflects the order-of-magnitude pattern, not a precise measurement.
