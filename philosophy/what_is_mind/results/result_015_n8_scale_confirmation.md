# result_015 — n=8 Scale Confirmation: γ Crossing Cell Holds at All Scales

**Date:** 2026-04-09
**Track:** Numerical (Odd)
**Tool:** inline Cycle 21

## Crossing cell (T2 vs R1) across three scales

| n | T2 Phi | R1 Phi | Ratio | t | p | d |
|---|--------|--------|-------|---|---|---|
| 4 | 0.119 | 0.031 | 3.87 | 6.91 | 0.0023 | 3.45 |
| 6 | 0.133 | 0.026 | 5.09 | 7.94 | 0.0014 | 3.97 |
| **8** | **0.124** | **0.026** | **4.82** | **7.34** | **0.0018** | **3.67** |

**γ prediction (T2 > R1) confirmed at n=4, n=6, and n=8.**

All three sizes: p < 0.003, Cohen's d > 3.4.

## What this means

The crossing cell result — T2 (feedforward + rich self-model) has substantially
higher Phi than R1 (recurrent + minimal self-model) — is robust to system size
across the testable range (n=4 to n=8).

The ratio (T2/R1) is stable: 3.87, 5.09, 4.82 — clustering around 4–5× across
three octaves of system size. This is not a small-n artefact; it is a consistent
architectural feature.

**β's crossing-cell prediction (R1 > T2) is rejected at all three scales
(p<0.003 at n=4, n=6, n=8). γ's prediction is confirmed at all three.**

## Updated scaling table for cert_001

| n | Test | T2 Phi | R1 Phi | Ratio | p |
|---|------|--------|--------|-------|---|
| 4 | Crossing cell | 0.112 (20s) / 0.119 (5s) | 0.028 / 0.031 | ~4× | <0.001 |
| 6 | Crossing cell | 0.133 | 0.026 | 5× | 0.001 |
| 8 | Crossing cell | 0.124 | 0.026 | 5× | 0.002 |

The result is scale-stable within the testable range. Whether it holds at n>10
(where Phi becomes uncomputable) is unknown.
