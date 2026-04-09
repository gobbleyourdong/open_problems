# NS Even 001 — Computing dW_NS/dt: Where the Transfer Breaks

**Date**: 2026-04-07
**Instance**: Even (cross-problem transfer from Poincaré)

## The Computation

W_NS = ∫ [τ(|ω|² + |∇f|²) + f - 3] · u dx,  u = (4πτ)^{-3/2} e^{-f}

## Why Ricci Flow Has dW/dt ≥ 0

Perelman showed Ricci flow is a GRADIENT FLOW of the F-entropy:

  ∂g/∂t = -2Ric = -∇F(g)

Therefore: dF/dt = -||∇F||² ≤ 0 (F decreases = W increases).
The variation is a perfect square BECAUSE the flow is gradient descent.

## Why NS Is Different

NS is NOT a gradient flow. It's HAMILTONIAN + DISSIPATION:

  ∂u/∂t = νΔu - (u·∇)u - ∇p
         = (dissipation) + (advection) + (pressure)

The Euler part (ν = 0) CONSERVES energy (Hamiltonian).
The viscous part (ν > 0) DISSIPATES energy.
The combination is NOT gradient descent for any known functional.

## The Explicit Variation

d/dt |ω|² = 2ω · ∂ω/∂t = 2ω · [νΔω + (ω·∇)u - (u·∇)ω]
           = 2ν ω·Δω + 2ωᵢωⱼSᵢⱼ - 2(u·∇)(|ω|²/2)
           = 2ν(Δ|ω|²/2 - |∇ω|²) + 2ωᵢωⱼSᵢⱼ - (u·∇)|ω|²

Integrating with the weight u = (4πτ)^{-3/2} e^{-f}:

∫ [d/dt |ω|²] u dx involves:
  (A) -2ν ∫ |∇ω|² u dx  ← GOOD (negative = diffusion, helps W increase)
  (B) +2 ∫ ωᵢSᵢⱼωⱼ u dx  ← BAD (vortex stretching, NO SIGN)
  (C) advection terms (integrate by parts against ∇f, manageable)

## The Critical Comparison

**Ricci flow**: dW/dt = 2τ ∫ |Ric + Hess(f) - g/2τ|² u dV

The Ric term (curvature) is analogous to the |∇ω|² term (enstrophy gradient).
The Hess(f) term comes from the conjugate equation.
The g/2τ term is the scaling correction.

ALL terms combine into ONE perfect square. No leftover.

**NS**: dW_NS/dt would contain:
  2τ ∫ |ν∇²ω + Hess(f)·ω - ω/2τ|² u dx  ← diffusion + conjugate + scaling
  + 2τ ∫ ωᵢSᵢⱼωⱼ u dx  ← THE LEFTOVER (stretching)

The stretching term DOES NOT fit into the square. It's an EXTRA term
with no definite sign. This is where the transfer breaks.

## Why the Stretching Resists

In Ricci flow: the "reaction" term Rm² (curvature squared) fits into the
square because the Bianchi identity constrains Rm to be algebraically
compatible with Ric. The algebraic structure of curvature makes everything fit.

In NS: the stretching ωᵢSᵢⱼωⱼ involves the STRAIN S = (∇u + ∇u^T)/2, which
is related to ω by a NONLOCAL operator (Biot-Savart law: u = K * ω where K
is a singular integral kernel). There's no algebraic identity that forces
ωSω to fit into a square with the diffusion terms.

**The nonlocality of Biot-Savart kills the perfect-square structure.**

## What Survives

Even though dW_NS/dt ≠ (perfect square), we get:

dW_NS/dt ≥ (perfect square) - 2τ |∫ ωᵢSᵢⱼωⱼ u dx|

If the stretching term is BOUNDED by the square term:

  |∫ ωSω · u dx| ≤ C ∫ |∇ω|² u dx  (?)

then dW_NS/dt ≥ (1-Cτ) × (perfect square) ≥ 0 for τ small enough.

**This would give LOCAL-IN-TIME regularity** (W is monotone for τ < 1/C).
Not global regularity, but better than nothing.

## The Refined Gap

The NS transfer from Poincaré identifies the EXACT obstruction:

**THE GAP = the Biot-Savart nonlocality.**

In Ricci flow: Ric is a LOCAL function of the metric → perfect square.
In NS: S is a NONLOCAL function of ω → square + leftover.

**A proof of NS regularity must either:**
(a) Tame the Biot-Savart nonlocality (make ωSω fit into a square), OR
(b) Bound the nonlocal term by the local term (ωSω ≤ C|∇ω|²), OR
(c) Find a DIFFERENT functional where the stretching DOES fit

Option (c) is the Multiple Mountains insight: maybe the right W is not
∫τ(|ω|² + |∇f|²)... but something ELSE that naturally absorbs the
Biot-Savart structure. The search over functionals continues.

## The Honest Verdict

The Poincaré → NS transfer SUCCEEDS in:
- Identifying the right framework (monotone entropy)
- Pinpointing the exact obstruction (Biot-Savart nonlocality)
- Giving a candidate functional (W_NS)
- Producing a partial result (local-in-time W monotonicity)

The transfer FAILS in:
- Giving global regularity (stretching term not absorbed)
- Producing a perfect-square variation (nonlocality prevents it)

**The gap for NS, refined by the transfer**: Biot-Savart nonlocality.
This is MORE SPECIFIC than "Liouville conjecture." It tells you EXACTLY
what mathematical structure needs to be controlled.
