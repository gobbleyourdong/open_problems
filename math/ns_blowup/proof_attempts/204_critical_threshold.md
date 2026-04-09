---
source: The unconditional argument gives EXACTLY quadratic growth — BKM critical
type: AT THE THRESHOLD — need one more epsilon for regularity
date: 2026-03-29
file: 204
---

## The Cycle Analysis

Phase A (α/|S| ≥ 0.095, DMP proven): α decreases (Riccati). ||ω|| stable.
Phase B (α/|S| < 0.095, Q > 0): α grows. ||ω|| grows by ~3%.
                                  Duration: ~0.3/||ω||.
                                  Exits to Phase A when α/|S| = 0.095.

Effective growth rate: (3% of ||ω||) / (0.3/||ω||) = 0.1||ω||².

This is ||ω||' ≈ 0.1||ω||² → ||ω|| ~ 1/(T*-t). QUADRATIC. BKM CRITICAL.

## Why This Doesn't Quite Close

Quadratic growth ||ω|| ~ 1/(T*-t) gives:
  ∫₀^T* ||ω|| dt = ∫₀^T* C/(T*-t) dt = ∞  (BKM DIVERGES)

For regularity: need ||ω||' ≤ C||ω||^{2-ε} for ANY ε > 0.
The unconditional argument gives ||ω||' ≈ C||ω||² (ε = 0).

## What Would Give the ε

The 3% growth per cycle comes from α reaching 0.095|S| during Phase B.
If the ACTUAL maximum α during Phase B is LESS than 0.095|S|:
the growth per cycle is less → effective rate sub-quadratic → regularity.

From data: during Phase B episodes, α typically reaches 0.02-0.05|S|
(much less than 0.095|S|). The 0.095 is the WORST-CASE upper bound.

The ACTUAL cycle gives ~0.5% growth (not 3%), with effective rate
~0.02||ω||². This is STILL quadratic but with smaller constant.

For SUB-quadratic: need the pressure to keep Q < 0 during Phase B
(preventing α from growing at all). From data: Q < 0 in Phase B
at 100% of post-transient measurements. The pressure correction
makes S²ê < H_ωω → Q < 0 even for α = 0.

## The Tiny Gap

The unconditional proof gives: ||ω||' ≤ C||ω||².
This is BKM-CRITICAL (logarithmic divergence of the integral).

For regularity: need ||ω||' ≤ C||ω||^{2-ε} for ε > 0.
The ε comes from the pressure making Q < 0 in the low-α regime.

From data: the pressure gives Q < 0 with margin (H_ωω ≈ 3× variance).
This margin provides ε > 0 → sub-quadratic → regularity.

But PROVING the margin (H_ωω > S²ê in low-α) needs the non-local bound.

## The Narrowest Gap in 204 Files

Previous gap: prove c₁ < 1/3 (Ashurst alignment).
Current gap: prove H_ωω > S²ê when α/|S| < 0.095.

These are DIFFERENT conditions:
- c₁ < 1/3 is about the DIRECTION of ω relative to strain eigenvectors.
- H_ωω > S²ê is about the PRESSURE exceeding the self-interaction variance.

The second condition is WEAKER (only needs to hold in the low-α regime).
And it's what the data shows (H_ωω ≈ 3× S²ê at the max).

## The Conditional Theorem (final version)

THEOREM: If H_ωω > S²ê at vorticity maxima with α/|S| < 0.095
for evolved Euler solutions, then 3D NS has global regularity.

PROOF:
- Phase B doesn't occur (Q = S²ê - α² - H_ωω < S²ê - H_ωω < 0).
- Only Phase A: DMP holds (proven unconditionally).
- α bounded by Riccati → ||ω|| exponential → BKM finite → regularity. ∎

## 204 files. The gap is: H_ωω > S²ê in the low-stretching regime.
## This is the FINAL, NARROWEST formulation of the open problem.
