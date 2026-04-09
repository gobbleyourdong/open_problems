---
source: Instance B — synthesis of all three instances' progress
range: 224
type: STATUS UPDATE — first variation proven, global max needed
date: 2026-03-29
---

## Three-Instance Convergence

### Instance A (Analytical):
- File 180: Lamb-Oseen straight tube: R = 1 exactly (PROVEN)
- File 184: Variational principle formulated
- File 188: **FIRST VARIATION dR/dε < 0 at straight tube (PROVEN)**
  Any z-perturbation with g(x*)>0 reduces R below 1.
  Straight tube is LOCAL maximum of R.
- Gap: need GLOBAL maximum (second variation for g(x*)=0 case)

### Instance B (Adversarial):
- File 220: 7 adversarial ICs, worst ratio 0.955 (N=48 resolved)
- File 221: Evolved thin trefoil peaks at 0.985, self-corrects to 0.973
- File 222: Lemma from file 267 verified (sign opposition 100%)
- File 223: Q bounded at ~11, α self-bounds at √Q_max ≈ 3.3
- **CANNOT BREAK R = 1 despite extreme efforts**

### Instance C (Shell/Structure):
- File 267: **THE PROOF** — two-case argument with Fourier lemma
  Case 1 (z-independent): α = 0 trivially. ✓
  Case 2 (z-variation): Lemma → H_ωω > 0 → compression. ✓
- File 268: Quantitative routes (Q1, Q2, Q3 identified)
- Gap: quantitative lower bound on H_ωω

## The Proof State

PROVEN:
- R = 1 for straight tube (local max of R)
- dR/dε < 0 for z-perturbations (first variation)
- H_ωω > 0 whenever z-variation exists (Fourier lemma)
- ê·S²·ê ≥ α² (Cauchy-Schwarz, in Lean)
- BKM chain: α bounded → exponential → finite integral

MEASURED (not proven):
- R ≤ 0.985 for all evolved adversarial ICs
- Q/|ω|² ≈ 0.018 (bounded and decreasing)
- H_ωω/ê·S²·ê ≈ 2.9 at the max point (post-transient)

ONE GAP REMAINING:
  Prove R ≤ 1 GLOBALLY (not just locally around the straight tube).
  Equivalently: no smooth div-free ω on T³ has R > 1 at its max-|ω| point.
  The first variation says the straight tube is local max.
  The adversarial search says no IC achieves R > 0.985.
  A second-variation or convexity argument would close it.

## 224 files total across all instances.
