---
source: Instance C — Attempt to close the quantitative gap
type: PROOF ANALYSIS — how close are we?
file: 268
date: 2026-03-29
---

## The Equation

Dα/Dt = ê·S²·ê - 2α² - H_ωω

Need Dα/Dt < 0 when α > 0.

## The Data (trefoil max point, t=0.25)

ê·S²·ê = 6.7
2α² = 1.3  (α = 0.8)
H_ωω = 19.5
Dα/Dt = 6.7 - 1.3 - 19.5 = -14.1  ← STRONGLY NEGATIVE ✓

## The Proven Bounds

H_ωω > 0 (Fourier lemma, file 267). RIGOROUS.
ê·S²·ê ≥ α² (Cauchy-Schwarz). RIGOROUS.
ê·S²·ê ≤ |S|² (maximum eigenvalue). RIGOROUS.
|S|² ≤ |ω|²/4 (attractor). NUMERICAL (not proven).

## The Gap

Need: 2α² + H_ωω > ê·S²·ê.

With just H_ωω > 0 and ê·S²·ê ≤ |S|² ≤ |ω|²/4:
2α² + 0 > |ω|²/4 → α > |ω|/(2√2) ≈ 0.354|ω|.
But measured: α ≈ 0.03|ω| (far below 0.354|ω|).

The bound is LOOSE by factor 10×. The reason:
- ê·S²·ê ≈ 6.7 << |S|² ≈ 156 (alignment suppresses by 23×)
- H_ωω ≈ 19.5 >> 0 (the Fourier lemma gives > 0 but not the magnitude)

## Three Routes to Close Quantitatively

### Route Q1: Prove ê·S²·ê ~ α² (alignment variance small)

If ω approaches an eigenvector of S: ê·S²·ê → α².
From file 173: eigenvector tilting pushes ω toward e₃ at rate 15:1.
Over time: Var = ê·S²·ê - α² → 0.

If Var ≤ Cα²: ê·S²·ê ≤ (1+C)α².
Dα/Dt ≤ (1+C)α² - 2α² - H_ωω = (C-1)α² - H_ωω.
For C < 1: Dα/Dt < 0 without needing H_ωω! (Pure self-depletion.)

From data: Var/α² ≈ 10. So C ≈ 10. Too large for C < 1.
But H_ωω makes up the difference: Dα/Dt = (10-1)α² - 19.5 = 5.1 - 19.5 = -14.4 < 0.

### Route Q2: Prove H_ωω ≥ c × ê·S²·ê (pressure proportional to strain)

If H_ωω ≥ c × ê·S²·ê with c > 0: Dα/Dt ≤ (1-c)ê·S²·ê - 2α².
For c ≥ 1: Dα/Dt ≤ -2α² < 0. QED.

From data: H_ωω/ê·S²·ê ≈ 19.5/6.7 = 2.9. So c ≈ 2.9 >> 1.

Can we prove c ≥ 1? This says the pressure Hessian is at least as
large as the strain self-interaction projected onto ω. Dimensionally:
both scale as |ω|² (roughly), so c being O(1) is plausible.

### Route Q3: The combined bound (most promising)

Don't separate the terms. Instead, note:
Dα/Dt = ê·S²·ê - 2α² - H_ωω = (ê·S²·ê - H_ωω) - 2α²

If ê·S²·ê - H_ωω ≤ 0: Dα/Dt ≤ -2α² < 0. QED.

From data: ê·S²·ê - H_ωω = 6.7 - 19.5 = -12.8 < 0. ✓

So: if H_ωω ≥ ê·S²·ê at the max: PROOF COMPLETE.

Can we prove H_ωω ≥ ê·S²·ê? This is a comparison between:
- The pressure Hessian along ω (non-local, from Poisson solve)
- The strain quadratic form along ω (local)

From the data (trefoil max, multiple times):
| t | ê·S²·ê | H_ωω | H_ωω ≥ S²ê? |
|---|--------|------|------------|
| 0.07 | 12.96 | 7.78 | NO ✗ |
| 0.09 | 12.17 | 7.45 | NO ✗ |
| 0.13 | 8.95 | 19.11 | YES ✓ |
| 0.15 | 8.60 | 18.41 | YES ✓ |
| 0.19 | 7.24 | 10.80 | YES ✓ |
| 0.25 | 6.68 | 19.46 | YES ✓ |

H_ωω ≥ ê·S²·ê holds 67% of the time at the max point.
The early violations (t < 0.1) are during the transient.
After t = 0.12: H_ωω ≥ ê·S²·ê consistently.

But "consistently after a transient" is NOT a proof.

## BOTTOM LINE

The quantitative closure is NUMERICALLY CONFIRMED but not proven.
Three routes exist (Q1, Q2, Q3), each requiring an estimate that
is true with large margin in the data but not yet proven analytically.

The BEST route is probably Q3: prove H_ωω ≥ ê·S²·ê at the max.
This follows if the pressure Hessian dominates the strain self-interaction.
The physical reason: the pressure is a GLOBAL quantity (Poisson solve),
while ê·S²·ê is local. The global quantity includes contributions from
the entire vorticity field, which (for the specific NS source) is larger.

## 268. Three quantitative routes identified. Each needs one estimate.
