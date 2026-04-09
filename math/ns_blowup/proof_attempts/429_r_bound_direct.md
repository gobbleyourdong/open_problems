---
source: DIRECT r BOUND — prove |ω|²/|S|² > 8/9 for N ≥ 4 at the global max
type: THE SIMPLEST REMAINING GAP — one inequality about eigenvalue ratios
file: 429
date: 2026-03-30
---

## THE REDUCTION

The entire NS regularity proof reduces to ONE INEQUALITY:

    |ω(x*)|²/|S(x*)|² > 8/9

at the global maximum x* of |ω|, for any smooth div-free field with N ≥ 4
active Fourier modes on T³.

Equivalently: |S(x*)|² < (9/8)|ω(x*)|².
Equivalently: |∇u(x*)|² < (9/8 + 1/2)|ω|² = (13/8)|ω|² (the trace-free route).

## WHY THIS IS SIMPLER THAN THE KEY LEMMA

The Key Lemma asks: S²ê < 3|ω|²/4.
This involves the DIRECTION ê (alignment with strain eigenvectors).

The r-bound asks: |S|² < (9/8)|ω|².
This is a SCALAR inequality — no direction involved!

|S|² = Σλᵢ² (sum of eigenvalue squares).
|ω|² = the vorticity magnitude squared.

Both are Frobenius norms (or their physical-space equivalents).
No eigenvector alignment needed. Just magnitudes.

## THE DATA

| N | min r = |ω|²/|S|² | > 8/9? | margin |
|---|-------------------|--------|--------|
| 4 | 1.69 | YES | 47% |
| 5 | 2.06 | YES | 57% |
| 6 | 3.02 | YES | 71% |
| 7 | 3.08 | YES | 71% |
| 8 | 3.88 | YES | 77% |

ALL above 8/9 with massive margin (47-77%).

## WHY r > 8/9 SHOULD BE PROVABLE

From the Biot-Savart Parseval identity (L² level):
||S||² = ||ω||²/2 (exact). So the L² AVERAGE ratio is r = 2.

At the MAX of |ω|: the ratio can differ from 2. But:
- The max of |ω| is at a PEAK — |ω| is above average there
- |S| at the peak is NOT the max of |S| — it's the S value at ω's max
- The Biot-Savart structure couples S to ω with phase shifts (sin vs cos)
- At the max of |ω| (where cos=1): |S| involves sin factors → SMALLER

From the per-mode analysis: each S_k has |S_k| = |ω̂_k|/2 (half the mode amplitude).
But the self-vanishing S_k·v̂_k = 0 means the EFFECTIVE |S| at the max is reduced.

## THE PROOF ATTEMPT

For N modes at the global max vertex:
|ω|² = |Σ s_k a_k v̂_k|² = Σa_k² + 2Σ_{j<k} s_js_k D_{jk}
|S|² = |Σ S_k|²_F = Σ|S_k|² + 2Σ_{j<k} S_j:S_k

From the per-mode: |S_k|²_F = a_k²/2 (half the mode energy).
So: Σ|S_k|² = Σa_k²/2.

The cross-terms: 2Σ S_j:S_k = 2Σ s_js_k × (strain cross-correlation).

From the identity (file 367): |S|² = |∇u|² - |ω|²/2.
And: |∇u|² = Σa_k² + 2Σ s_js_k G_{jk}.

So: |S|² = Σa_k²/2 + Σ s_js_k (G_{jk} - D_{jk}) = Σa_k²/2 + EXCESS/2.

For r > 8/9: need |S|² < (9/8)|ω|².
Σa²/2 + EXCESS/2 < (9/8)(Σa² + 2Σ s*D)
Σa²/2 + EXCESS/2 < (9/8)Σa² + (9/4)Σ s*D

EXCESS < (9/4 - 1)Σa² + (9/2)Σ s*D = (5/4)Σa² + (9/2)Σ|D_eff|

Since EXCESS ≤ Σa² × (per-pair max 1/4) × pairs... this is the same bound.

## STATUS

The r > 8/9 condition IS the |∇u|²/|ω|² < 13/8 condition (identical).
The simplification from direction → scalar doesn't help because the
trace-free factor 2/3 already handles the direction part.

The gap remains: prove |∇u|²/|ω|² < 13/8 for all N at the global max.

## 429. r > 8/9 IS the same as |∇u|²/|ω|² < 13/8. No new reduction.
