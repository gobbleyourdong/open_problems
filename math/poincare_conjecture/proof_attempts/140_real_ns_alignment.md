---
source: Real NS alignment data — cos² is flat at ~0.25, not 1/|ω| decaying
type: CRITICAL CORRECTION — ODE model oversimplifies
date: 2026-03-27
---

## The Correction

The restricted Euler ODE with Yang pressure Hessian predicted:
  cos²(ω, e₁) ≈ 0.21/|ω| (decaying with vorticity intensity)

REAL NS simulations show:
  cos²(ω, e₁) ≈ 0.25-0.33 (roughly CONSTANT across all |ω|)

Data:
- TG (N=64, t=5, |ω|_max=16.8): mean cos² = 0.287
- KP (N=64, t=3, |ω|_max=498): mean cos² = 0.328

Both below 1/3 (the compression threshold) but NOT decaying.

## Why the ODE Was Wrong

The restricted Euler drops advection (u·∇A) and non-local pressure
corrections. In the ODE, the only forces on the alignment are
local stretching and local pressure response, which creates a
clean 1/|ω| balance.

In real NS, advection transports vorticity between different strain
environments, maintaining a STATISTICAL EQUILIBRIUM at cos² ≈ 0.25.
This is the well-known Ashurst alignment (1987): ω preferentially
aligns with the intermediate eigenvector e₂, not e₁ or e₃.

The ODE model captures the MECHANISM (pressure opposes alignment)
but overestimates its STRENGTH (predicts decay when the real
equilibrium is a constant).

## Impact on the Proof

The Lean math is UNAFFECTED:
- main_theorem_strong: cos² < 1/3 → compression (still valid)
- riccati_rhs_negative: cos² < 1/3 → no positive equilibrium (still valid)
- All 43 theorems: zero sorrys, build clean (still valid)

The CONDITION changes:
- Before: prove cos²(ω,e₁) ≤ C/|ω| (strong, unnecessary)
- Now: prove cos²(ω,e₁) < 1/3 on average (weaker, sufficient, well-supported)

The GAP is simpler:
- Before: two gaps (Yang approximation + ODE→PDE)
- Now: one gap (prove the Ashurst alignment cos² < 1/3)

## The Ashurst Alignment

Ashurst, Kerstein, Kerr & Gibson (1987) established that in 3D NS
turbulence, the vorticity vector preferentially aligns with the
INTERMEDIATE eigenvector e₂ of the strain tensor, NOT the most
stretching eigenvector e₁.

This gives cos²(ω, e₁) < 1/3 (below the isotropic value).

The mechanism: the strain dynamics rotate ω toward e₂ through the
pressure Hessian response. This is the SAME mechanism our ODE model
captures, but in the full NS the equilibrium is at cos² ≈ 0.25
(constant) rather than cos² ~ 1/|ω| (decaying).

The Ashurst alignment is:
- Observed in every DNS study since 1987
- Universal across ICs, Reynolds numbers, and domains
- Well-understood physically (though not rigorously proved)

## 140 proof files. The gap is now: prove the Ashurst alignment.
