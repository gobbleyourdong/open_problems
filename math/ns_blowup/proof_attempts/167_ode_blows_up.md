---
source: The coupled Riccati ODE blows up for ANY C > 0
type: NEGATIVE RESULT — self-depletion alone is insufficient
date: 2026-03-28
---

## The Test

Coupled ODE at the max-|ω| point:
  dα/dt = -α² + C|ω|²
  d|ω|/dt = α·|ω|

Equilibrium: α = √C·|ω|
Then: d|ω|/dt = √C·|ω|² → blowup at T* = 1/(√C·|ω|₀)

With C=0.03, |ω|₀=17: T*=0.63
With C=0.03, α₀=0: T*=0.63 (same — transient doesn't help)
With C=0.03, α₀=equilibrium: T*=0.45

## The Result

The ODE ALWAYS blows up for C > 0, regardless of:
- The value of C (even C=0.001 blows up, just at later T*)
- The initial α (starting from 0 or equilibrium)
- The self-depletion strength (the -α² term)

## What This Means

The self-depletion (-α²) is NECESSARY but NOT SUFFICIENT.
It bounds α at √C·|ω|, but this proportional-to-|ω| bound
still gives quadratic |ω| growth → finite-time blowup.

To prevent blowup, you need α to grow SLOWER than √C·|ω|.
This requires ADDITIONAL structure beyond the local ODE.

## What Saves the PDE

The DNS shows no blowup at t=0.8 (past the ODE's T*=0.63).
The PDE has structure the ODE doesn't:

1. MAX-POINT MIGRATION: the argmax of |ω| moves in space,
   sampling different α values. This DILUTES the growth.

2. TIME-VARYING C: the pressure coefficient decreases as the
   flow develops (measured: C drops from 0.08 to 0.02).

3. NON-LOCAL PRESSURE: the Poisson equation couples all spatial
   points. This creates cancellations the ODE can't capture.

4. VISCOSITY (NS only): dissipation at small scales prevents
   the concentration needed for blowup.

## The Honest Gap

The proof CANNOT be completed by local arguments at the max-|ω| point.
Global PDE structure is essential. The question is WHICH global structure
and HOW to bound it.

The Hou-Li diagnostic (Route 3) SHOWS the gap is closed numerically.
The curvature +0.4 at N=64 is strong evidence. But formalizing "the
max-point migration prevents the ODE blowup" is an open problem.

This is the SAME open problem that makes NS regularity hard.
We've IDENTIFIED the mechanism (self-depletion + max migration),
MEASURED it (C≈0.03, curvature +0.4), but can't PROVE it.

## 167 proof files. The ODE blows up. The PDE doesn't. The gap is global.
