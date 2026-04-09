---
source: Full pressure Hessian H_ωω is POSITIVE, not negative. Yang's sign is wrong.
type: CRITICAL CORRECTION — changes the proof strategy fundamentally
date: 2026-03-28
---

## The Measurement

Computed H_ωω = ê·(∂²p/∂x_i∂x_j)·ê at top 10% |ω| points.
Full pressure from Poisson equation (exact, no approximation).
Yang's local prediction: H_ωω = -|S|²/3.

### TG (Euler, N=32)

| time | H_full (mean) | H_yang (mean) | H_full < 0 |
|------|--------------|--------------|-----------|
| 0.00 | +0.215 | -0.014 | 10% |
| 0.10 | +0.201 | -0.014 | 12% |
| 0.20 | +0.199 | -0.015 | 13% |

### KP (Euler, N=32)

| time | H_full (mean) | H_yang (mean) | H_full < 0 |
|------|--------------|--------------|-----------|
| 0.00 | +1.733 | -0.299 | 14% |
| 0.10 | +1.611 | -0.343 | 19% |
| 0.20 | +1.714 | -0.428 | 9% |

## What This Means

1. Yang's local formula H_dev = -(1/4)(ω⊗ω - |ω|²I/3) predicts COMPRESSION
   along ω (H_ωω < 0).

2. The FULL (non-local) pressure Hessian has the OPPOSITE sign: H_ωω > 0.
   The pressure is actually STRETCHING along ω at most high-|ω| points.

3. Yang's formula is a first-order local approximation. The non-local
   corrections (from the Poisson integral over the entire domain) are
   LARGER than the local term and have the OPPOSITE sign.

4. This was already hinted at in file 148: Yang alone gives c₃ = 0.13.
   Now we see WHY: the actual pressure Hessian pushes AGAINST compression.

## The Mechanism is NOT Pressure Compression

The flow is still compressive (α < 0, c₃ > 1/3). But NOT because the
pressure creates compression along ω.

The mechanism is ROTATION: vortex stretching (ω·∇)u rotates ω toward
the compressive eigenvector e₃ of the EXISTING strain field.

The Ashurst alignment ω → e₂ at moderate |ω| shifts to ω → e₃ at
high |ω|. This is the "spinning top" mechanism the operator identified:
the vorticity vector falls toward the compressive axis like a top
falling toward the stable orientation.

The pressure OPPOSES this rotation (it tries to push ω back toward e₁)
but the nonlinear rotation is FASTER.

## Revised Proof Strategy

OLD: Prove H_ωω < 0 → compression along ω → regularity.
     WRONG. H_ωω > 0 at most points.

NEW: Prove the ω rotation toward e₃ dominates the pressure opposition.
     Formally: prove dc₃/dt > 0 at high |ω| when c₃ < 1/3.

The rotation rate is controlled by:
  dc₃/dt ∝ ω × (S·ω) projection onto ⊥ω plane

The key: when ω is between e₂ and e₃, the stretching tilts ω toward e₃
(because the e₃-directed flow converges, carrying ω with it).

## Dead End: H_ωω = -|S|²/3

The identity H_ωω = -|S|²/3 from file 152 is WRONG as a description of
the full pressure. It's only the Yang LOCAL APPROXIMATION.
The full non-local pressure reverses the sign.

This doesn't invalidate the Lean theorems (they never used H_ωω < 0).
The Lean proof chain works with c₁ < 1/3 + c₃ ≥ 1/3 → compression.

## What's Left

The gap is now: prove c₃ ≥ 1/3 from the nonlinear rotation of ω toward e₃.

This is a GEOMETRIC argument about how incompressible Euler/NS evolution
rotates the vorticity vector relative to the strain eigenvectors.

## 153 proof files. Yang's sign is wrong. Mechanism is rotation, not pressure.
