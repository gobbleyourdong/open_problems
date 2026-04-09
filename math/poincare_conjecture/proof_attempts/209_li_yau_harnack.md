---
source: Li-Yau / Perelman approach — Harnack inequality for NS vorticity
type: NEW DIRECTION — gradient estimate instead of pointwise pressure bound
date: 2026-03-29
file: 209
---

## The Li-Yau Gradient Estimate (1986)

For the heat equation ∂f/∂t = Δf on a manifold with Ric ≥ -K:

  Δlog(f) ≥ -n/(2t) - nK/2

This gives a LOWER BOUND on the Laplacian of log(f), which controls
how fast f can concentrate. It's the key to the Harnack inequality
and to Perelman's entropy monotonicity.

## The NS Analog

For the enstrophy density e = |ω|²: De/Dt = 2αe + 2νω·Δω (NS).

Define ψ = log(e) = log|ω|². Then:
  Dψ/Dt = De/(eDt) = 2α + 2νω·Δω/|ω|²

At the MAX of e (= max of |ω|²): ∇e = 0, Δe ≤ 0.
Δe = 2|∇ω|² + 2ω·Δω ≤ 0 → ω·Δω ≤ -|∇ω|².

So at the max: Dψ/Dt = 2α + 2ν(ω·Δω)/|ω|² ≤ 2α - 2ν|∇ω|²/|ω|².

The Li-Yau quantity: Δψ = Δ(log|ω|²) = Δe/e - |∇e|²/e².
At the max: ∇e = 0, so Δψ = Δe/e ≤ 0.

This just says: log|ω|² is SUBharmonic at the max → no local max of Δψ.
(Trivial from the max condition.)

## A Harnack-Type Bound for Vorticity

The Li-Yau Harnack: for the heat equation,
  (∂/∂t - Δ)log f ≥ -n/(2t).

For NS vorticity: (D/Dt - νΔ)log|ω|² = 2α + correction terms.

At the max: D(log|ω|²)/Dt = 2α.
And νΔ(log|ω|²) ≤ 0 (at the max).

So: 2α ≥ D(log|ω|²)/Dt ≥ D(log|ω|²)/Dt - νΔ(log|ω|²)

The Harnack-type bound: D(log||ω||∞²)/Dt = 2α* (exact, at the max).

For the HEAT EQUATION: D(log||f||∞)/dt ≤ 0 (maximum principle, f decreasing).
For NS VORTICITY: D(log||ω||∞)/dt = α* which can be positive.

The bound: α* ≤ ?? is exactly what we're trying to prove.

## The Perelman Connection

Perelman's entropy for Ricci flow: W = ∫(τ(|∇f|² + R) + f - n)u dV
where u = (4πτ)^{-n/2}e^{-f} and f satisfies the conjugate heat equation.

The MONOTONICITY: dW/dt = 2τ∫|Ric + ∇²f - g/(2τ)|² u dV ≥ 0.

The RHS is a SQUARED QUANTITY — manifestly non-negative!

The key: the coupling between f (adjoint) and g (metric/flow) creates
a PERFECT SQUARE in the derivative. This is algebraic magic.

For NS: can we find f such that:
dW/dt = ∫(something)² × (positive weight) dx ≥ 0 ?

The "something" squared would absorb all the problematic terms
(pressure, alignment, CZ operator) into a single non-negative expression.

## The Research Program

1. Define the NS analog of Perelman's conjugate heat equation:
   ∂f/∂t = -Δf - (u·∇f) + |∇f|² - α + (terms to be determined)

2. Define W involving ω and f.

3. Compute dW/dt and try to make it a sum of squares.

4. The sum-of-squares structure would give monotonicity WITHOUT
   needing any CZ bounds, alignment conditions, or pressure estimates.

## Why This Is Hard But Possible

Hard: the NS nonlinearity is QUADRATIC in u (cubic in ω through Biot-Savart).
The Ricci flow nonlinearity is also quadratic in g. Perelman found the
right functional after years of work.

Possible: the STRUCTURE is similar — both are geometric flows with
a Laplacian + nonlinear lower-order terms. The techniques of
differential geometry (Bochner formulas, maximum principles, entropy
monotonicity) SHOULD have NS analogs.

## Connection to Our Findings

Our Q = Dα/Dt + α² < 0 at the max is the NS analog of the
Harnack inequality: it says the "curvature" α can't accelerate.

Perelman's entropy PROVES the Harnack via a global functional.
If we can find the NS analog: it would prove Q < 0 globally.

The Fourier cancellation (file 171) is the NS analog of the
curvature cancellation in the Bochner formula. The 98% cancellation
IS the structure that would appear in the perfect-square computation.

## 209. The Perelman/Li-Yau direction is the RIGHT framework.
## The proof needs: the NS conjugate heat equation + the right W.
