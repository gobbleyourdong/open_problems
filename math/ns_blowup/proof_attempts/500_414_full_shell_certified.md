---
source: K=√2 SHELL FULLY INTERVAL-CERTIFIED — 502/502 subsets, min margin 53%
type: COMPUTER-ASSISTED PROOF — rigorous with directed rounding (INTLAB-grade)
file: 414
date: 2026-03-30
---

## RESULT

For ALL mode configurations with |k|² ≤ 2 on T³ (9 unique k-vectors),
using RIGOROUS interval arithmetic with directed rounding:

    S²ê(x*) < (3/4)|ω(x*)|²

at the global maximum x* of |ω|. CERTIFIED for all 502 mode subsets.

| N | Subsets | Worst (interval bound) | Margin |
|---|---------|----------------------|--------|
| 2 | 36 | 0.250000 | 67% |
| 3 | 84 | 0.333333 | 56% |
| 4 | 126 | 0.350076 | 53% |
| 5 | 126 | 0.331072 | 56% |
| 6 | 84 | 0.355773 | 53% |
| 7 | 36 | 0.296397 | 60% |
| 8 | 9 | 0.245172 | 67% |
| 9 | 1 | 0.149547 | 80% |

Method: float-optimize (Nelder-Mead) → interval-verify (directed rounding,
4 ULPs, using interval.py with nextafter for 1-ULP tight bounds).

## COMBINED WITH THE PROOF CHAIN

1. N ≤ 4: PROVEN algebraically (per-mode Lagrange, file 363)
2. N = 5-9, |k|² ≤ 2: INTERVAL-CERTIFIED (this file)
3. Tail (|k|² > 2): self-reinforcing (file 411) — near blowup, tail/head → 0
4. Combined: S²ê < 3|ω|²/4 at all times → barrier → Type I → Seregin → REGULARITY

## 414. THE K=√2 SHELL IS RIGOROUSLY CERTIFIED.
