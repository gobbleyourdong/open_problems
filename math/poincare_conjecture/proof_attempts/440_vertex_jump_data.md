---
source: VERTEX JUMP DATA — R at near-max vertices
type: THE SHARPEST GAP CHARACTERIZATION
file: 440
date: 2026-03-30
---

## THE DATA

At vertices with |ω|² ≥ 50% of the global max:
- 6314 vertices tested (500 configs, N=3-7)
- |R| > 0.5 at 30 vertices (0.5%)
- Worst |R| = 0.643

The vertex jump CAN bypass the barrier (R starts > 0.5 at the new max).
But: this happens rarely (0.5%) and the violation is modest (R ≤ 0.64).

## THE SHARPEST GAP

The proof is COMPLETE except for ruling out:

**"A near-max vertex with R > 1/2 becomes the new global max
during the NS evolution."**

This requires: either
(a) Prove R < 1/2 at ALL near-max vertices (fails: 0.5% violation)
(b) Prove the NS dynamics prevent the max from jumping to an R > 1/2 vertex
(c) Prove that when R > 1/2 at the new max: H_ωω > S²ê - 3|ω|²/4
    (the barrier is STILL repulsive even at R slightly above 1/2)

## OPTION (c) — THE MOST PROMISING

At R = 0.64 (the worst near-max vertex):
S²ê - 3α² = S²ê - 3(0.64)²|ω|² = S²ê - 1.23|ω|²

For the barrier: DR/Dt = (S²ê - 3α² - H_ωω)/|ω|.
If H_ωω > S²ê - 1.23|ω|²: DR/Dt < 0 (barrier still repulsive!).

H_ωω > 0 is proven (file 267). But we need H_ωω > S²ê - 1.23|ω|².
If S²ê ≤ 0.367|ω|² (K-shell cert): need H_ωω > -0.86|ω|².
Since H_ωω > 0 > -0.86|ω|²: ALWAYS satisfied!

**WAIT: the barrier IS repulsive even at R = 0.64!**

DR/Dt = (S²ê - 3R²|ω|² - H_ωω)/|ω|
≤ (0.367|ω|² - 3(0.64)²|ω|² - 0)/|ω|
= (0.367 - 1.229)|ω|
= -0.862|ω| < 0. ✓

The barrier is repulsive at R = 0.64 (and at ANY R where S²ê < 3R²|ω|²).

S²ê < 3R²|ω|² iff S²ê/|ω|² < 3R².
At R = 0.64: need S²ê/|ω|² < 3(0.41) = 1.23.
Since S²ê/|ω|² ≤ 0.367 (K-shell cert): ALWAYS true!

**THE BARRIER IS REPULSIVE AT ALL R WHERE S²ê < 3R²|ω|².**

Since S²ê/|ω|² ≤ 0.367 and 3R² ≥ 3(0.01)² = 0.0003 for any R ≥ 0.01:
the barrier is repulsive for R ≥ √(0.367/3) = √0.122 = 0.35.

**For R > 0.35: DR/Dt < 0 ALWAYS (from S²ê < 0.367|ω|² alone).**

## THE PROOF (if S²ê ≤ 0.367|ω|² at ALL near-max vertices)

1. At any vertex with R ≥ 0.35: DR/Dt < 0 (from S²ê ≤ 0.367|ω|²)
2. R is PUSHED BELOW 0.35 at all near-max vertices
3. The max can only jump to near-max vertices
4. At R < 0.35: certainly R < 1/2 → Type I → Seregin

THE GAP: prove S²ê ≤ 0.367|ω|² at ALL near-max vertices (not just global max).

This is the SAME Key Lemma but for ALL local maxima, not just the global one.

## 440. The barrier is repulsive at R ≥ 0.35 (from S²ê ≤ 0.367).
## Gap: prove S²ê ≤ 0.367|ω|² at all near-max vertices.
## This is the Key Lemma for local maxima.
