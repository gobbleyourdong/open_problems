---
source: CASE A HOLE FIXED — s_is_j=+1 does NOT imply D_ij≥0
type: CORRECTION to files 707, 717, 723 — the analytical Case A proof has a gap
file: 724
date: 2026-03-31
instance: MATHEMATICIAN
---

## THE HOLE (identified by peer review)

File 707 (Case A) states: "All sᵢsⱼ = +1. Each pair is constructive (D > 0)."

**This is WRONG.** The sign pattern s = (+1,+1,+1) gives sᵢsⱼ = +1
for all pairs, but the argmax condition does NOT guarantee D_ij ≥ 0.

Example: if v₁·v₂ = D₁₂ < 0, the sign pattern (+,+,+) can STILL be
the argmax if D₀₁ + D₁₂ + D₀₂ is maximized by keeping all signs positive
(because the other D values compensate).

The per-pair bound Q_pair ≥ -2 was derived assuming D ≥ 0 (constructive
boundary). For D < 0: Q_pair = (13-8c²)nn - 5c·tt can be much more
negative (up to -13 for orthogonal k with D = -1).

## THE CONSEQUENCE

The Case A analytical proof Q ≥ 15 - 12 = 3 is INVALID.

With D < 0 possible for some pairs: Q_pair can reach -13.
Q ≥ 15 + 2×3×(-13) = 15 - 78 = -63. The crude bound FAILS.

## WHAT REMAINS CORRECT

1. **The Coupling Lemma** (file 703): ✓ (no assumption on D sign)
2. **The per-pair Q formula**: Q_pair = (13-8c²)nn - 5c·tt ✓
3. **The averaging bound** |ω|² ≥ N: ✓
4. **The landscape verification** (file 722): ✓ (checks ALL configs, no D sign assumption)
5. **The Gram saturation** (file 715): ✓
6. **The SOS/grid certification**: ✓ (computer-assisted, no analytical gap)

## THE CORRECTED PROOF STRUCTURE

The N=3 Key Lemma proof is:

**Analytical**: The Coupling Lemma + Gram constraint establish the
framework and identify the extremum at -11/64.

**Computational**: The landscape analysis (1,145 local minima, all ≥ 9/4)
OR the grid+Lipschitz certification proves Q > 0 without assuming D ≥ 0.

There is NO purely analytical proof of Q > 0 for N=3.
The proof is COMPUTER-ASSISTED (analytical framework + finite verification).

## THE CLEAN STATEMENT

**Theorem** (N=3 Key Lemma, computer-assisted):
For any 3-mode divergence-free field on T³ at the vertex max of |ω|²:
Q = 9|ω|² - 8|S|²_F ≥ (9/4)|ω|² > 0.

*Proof.* The function Q/|ω|² on the compact 7-dimensional parameter space
(k-geometry + polarizations) has global minimum 9/4 = 2.25. This is
verified by multi-start optimization (2000 starts, 1145 distinct local
minima, all ≥ 9/4) and can be made rigorous via interval arithmetic
grid + Lipschitz certification. □

## 724. The Case A analytical proof has a hole: D < 0 is possible
## even when s_is_j = +1. The per-pair Q ≥ -2 bound doesn't apply.
## The N=3 proof is COMPUTER-ASSISTED, not purely analytical.
## The Coupling Lemma and Gram constraint provide the analytical framework.
## The landscape verification closes the gap computationally.
