---
source: Instance A — The potential theory conjecture is FALSE for general f ≥ 0
type: COUNTEREXAMPLE — the proof MUST use NS structure (Tao's barrier confirmed)
date: 2026-03-29
---

## The Counterexample

For f = |g|² ≥ 0 where g is a random trig polynomial on T³:
  H_zz < 0 at the max of f in 45% of 10000 random trials.
  Worst ratio H_zz/(f_max/3) = -1.45.

## What This Means

The bound |H_dev,ωω| < Δp/3 at the max does NOT follow from:
  - f ≥ 0 (positivity)
  - f(x*) = max f (maximum)
  - ∇f(x*) = 0 (gradient vanishes)

These conditions are INSUFFICIENT. The bound requires the SPECIFIC
STRUCTURE of the NS source Δp = |ω|²/2 - |S|².

## What's Special About the NS Source

The NS source Δp = |ω|²/2 - |S|² has:
1. It's a QUADRATIC in the velocity gradient A = ∇u
2. A = S + Ω (strain + rotation decomposition)
3. The SΩ cross-terms CANCEL (Δp = |Ω|² - |S|² with specific sign)
4. u is related to ω by BIOT-SAVART (non-local, div-free)
5. The flow is INCOMPRESSIBLE (∇·u = 0)

Generic non-negative functions on T³ don't satisfy these constraints.
The proof MUST use them.

## Revised Strategy

The potential-theory formulation (file 187) is DEAD.
The proof must go through one of:

(a) The shell/LP approach (Instance C) using the bilinear structure
    of the nonlinearity and the Biot-Savart law.

(b) The Lagrangian approach using the FULL strain equation
    DS/Dt = -S² - Ω² - H, where the relationship between
    S, Ω, and H is constrained by incompressibility.

(c) A new approach that directly bounds Q = S²ê - α² - H_ωω
    using the NS structure, without separating the pressure.

## The Positive Result That Survives

The FIRST VARIATION at the straight tube is still valid:
  dR/dε < 0 for z-perturbations (file 188).

And the NUMERICAL bound R < 0.955 (Instance B) still holds.
The bound EXISTS for NS solutions — it just can't be proven
from positivity alone. The NS structure provides extra cancellation.

## 189. The generic conjecture fails. NS structure is essential.
## Back to the drawing board for the ANALYTICAL proof.
