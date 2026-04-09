---
source: DISCREPANCY RESOLVED — C ≥ -1/8 is FALSE for N≥3
type: CORRECTION to 400s conjecture (file 456)
file: 527
date: 2026-03-30
instance: CLAUDE_OPUS (500s)
---

## THE DISCREPANCY

File 456 (400s) conjectured: C ≥ -|ω|²/8 for all N.
File 455 claimed: "C/|ω|² ≥ -0.125 for ALL tested configurations."

**THIS IS WRONG.** My DE adversarial search finds:

N=3, k = [(-2,-1,1), (-1,0,0), (-1,1,0)]:
  **C/|ω|² = -0.1695 < -1/8 = -0.125**

Verified with both DE (popsize=20, maxiter=500) and 100³ grid search.
The continuous max and vertex max coincide (cos values = ±1 to 10⁻⁹).

## WHY THE 400s MISSED IT

The 400s instance likely didn't optimize polarization angles as
aggressively. Their "10K adversarial" used vertex maxima (correct)
but with insufficient polarization optimization (less restarts or
coarser angle search).

DE with popsize=20, maxiter=500 finds configurations that simpler
searches miss. The worst case requires specific polarization angles
that are not near simple rational multiples of π.

## CORRECTED BOUNDS

| N | Worst C/|ω|² | C ≥ -1/8? | C > -5/16? | Margin to -5/16 |
|---|-------------|-----------|------------|-----------------|
| 2 | -0.125 | = (tight) | YES | 60% |
| 3 | -0.170 | **NO** | YES | 46% |
| 4 | -0.167 (est) | **NO** | YES | 47% |
| 5 | ~-0.17 (est) | **NO** | YES | ~46% |

The C ≥ -1/8 conjecture is FALSE for N ≥ 3.
The weaker bound C > -5/16 holds with ~46% margin.

## THE TRUE GAP

**Prove C > -5|ω|²/16 at argmax|ω|² for all N ≥ 3.**

This is the same gap as file 526, now with the 400s conjecture disproven.

The worst case for N≥3 is driven by MIXED K-shells:
- k₁ on K²=6 shell (many diverse angles)
- k₂, k₃ on K²=1,2 shells
- Polarizations optimized to maximize negative correction
- Pairwise angle ~73° (large sin²θ ≈ 11/12 for the dominant pair)

## THE REMAINING CHAIN (corrected)

1. C > -5|ω|²/16 at the max [THE GAP, margin 46%]
2. |S|²_F < 9|ω|²/8 [from identity]
3. S²ê ≤ (2/3)|S|²_F [trace-free, tight]
4. S²ê < (3/4)|ω|² [combining 2+3, strict for generic fields]
5. Barrier → Type I → Seregin → regularity [proven]

## 527. C ≥ -1/8 is FALSE for N≥3 (worst -0.170 vs -0.125).
## C > -5/16 holds with 46% margin. This is the true gap.
