---
source: COUNTEREXAMPLE — α = |ω|/2 for a single Fourier mode at θ = π/4
type: KILLS all kinematic bounds — the proof MUST be dynamic
date: 2026-03-29
---

## The Counterexample

ω = (0, cos(x+z), 0) on T³.

This is:
- Smooth (single Fourier mode, C^∞) ✓
- Divergence-free (k·ω̂ = (1,0,1)·(0,1,0) = 0) ✓
- Has max |ω| = 1 at x+z = 0 ✓

The velocity (from Biot-Savart):
  u = (-sin(x+z)/2, 0, sin(x+z)/2)

The strain at x+z=0:
  S = diag(-1/2, 0, 1/2)

The stretching rate: α = ê·S·ê with ê = (0,1,0) (the ω direction).
Wait — ω = (0,1,0)cos(x+z). So ê = (0,1,0). And α = S₂₂ = 0.

Hmm, that gives α = 0, not 1/2. Let me recheck.

ω = (0, cos(x+z), 0). At (0,0,0): ω = (0,1,0). ê = (0,1,0).

S = diag(-1/2, 0, 1/2). ê·S·ê = S₂₂ = 0. α = 0.

I made an error. The stretching α = 0 for this mode! The per-mode
bound says |α̂| ≤ |ω̂|/2 = 1/2, and the actual α̂ = 0 (below the bound).

Let me find a mode where α actually reaches |ω|/2.

## Corrected Analysis

For mode k = (1,0,1) with ω̂ = (0,1,0):
  ω is along ŷ. ê = ŷ.
  S_yy = 0 (computed above). α = 0.

The per-mode bound: α̂(k) = (k·ê)((k×ω̂)·ê)/|k|².
k·ê = (1,0,1)·(0,1,0) = 0. So α̂ = 0!

When k ⊥ ê: α̂ = 0. The mode contributes NOTHING to α.

For α̂ ≠ 0: need k·ê ≠ 0 AND (k×ω̂)·ê ≠ 0.

k = (1,1,0), ω̂ ⊥ k: e.g., ω̂ = (-1,1,0)/√2. ê = (0,0,1).
k·ê = 0. α̂ = 0. Still zero.

For α̂ = |ω̂|/2: need k at θ = π/4 to ê AND ω̂ in the right direction.

k = (0,1,1), ê = (0,0,1). k·ê = 1, |k| = √2, θ: cos θ = 1/√2, θ = π/4. ✓
ω̂ ⊥ k: ω̂ = (1,0,0) (perpendicular to k).
k×ω̂ = (0,1,1)×(1,0,0) = (0,1,-1)... wait: (0,1,1)×(1,0,0) = (1×0-0×1, 1×1-0×0, 0×0-1×1)
Hmm, let me be careful: a×b = (a₂b₃-a₃b₂, a₃b₁-a₁b₃, a₁b₂-a₂b₁).
(0,1,1)×(1,0,0) = (1×0-1×0, 1×1-0×0, 0×0-1×1) = (0, 1, -1).

(k×ω̂)·ê = (0,1,-1)·(0,0,1) = -1.

α̂ = (k·ê)(k×ω̂·ê)/|k|² = 1×(-1)/2 = -1/2.

And |ω̂| = 1. So |α̂|/|ω̂| = 1/2. SATURATED. ✓

Now: ω(x) = Re(ω̂ e^{ik·x}) = (cos(y+z), 0, 0).
|ω| = |cos(y+z)|. Max = 1 at y+z = 0.

ê = ω/|ω| = (1,0,0) at the max. NOT (0,0,1) as I assumed!

At the max: ê = (1,0,0). α = ê·S·ê = S₁₁.

u = BS(ω): û = ik×ω̂/|k|² = i(0,1,1)×(1,0,0)/2 = i(0,1,-1)/2.
u = Re(û e^{i(y+z)}) = (0, -sin(y+z)/2, sin(y+z)/2).

At y+z=0: A = ∇u.
A₂₂ = ∂u₂/∂y = -cos(0)/2 = -1/2.
A₂₃ = ∂u₂/∂z = -cos(0)/2 = -1/2.
A₃₂ = ∂u₃/∂y = cos(0)/2 = 1/2.
A₃₃ = ∂u₃/∂z = cos(0)/2 = 1/2.
All other A_ij = 0.

S₁₁ = 0. So α = S₁₁ = 0!

The actual α at the max is 0, not 1/2. The per-mode bound α̂ = -1/2
is achieved in FOURIER space, but at the PHYSICAL max of |ω|, the ê
direction changes, and α = 0.

## THE KEY INSIGHT

The per-mode bound |α̂(k)| ≤ |ω̂(k)|/2 is about the Fourier coefficient.
The PHYSICAL α at the max depends on the ALIGNMENT of ω with the strain.
For a single mode: ω is always perpendicular to the strain eigenvector
that has the mode's contribution. So α = 0 at the max for single modes!

This is because a single Fourier mode is a BELTRAMI eigenmode:
curl(ω) = ±|k|ω (for div-free single mode). So α = 0 at its max.

## THE COUNTEREXAMPLE FAILS

A single Fourier mode at θ = π/4:
- Per-mode: |α̂| = |ω̂|/2 (saturated)
- Physical: α = 0 at the max (Beltrami!)

The per-mode bound being saturated does NOT mean α = |ω|/2 physically.
The physical α at the max is ZERO for any single mode (Beltrami).

For α/|ω| to be large: need MULTIPLE modes interacting.
This is Instance C's Beltrami mixing insight (file 304).

## 263. The counterexample FAILS. Single modes are Beltrami with α = 0.
## α/|ω| < 1/2 MIGHT be provable after all (from multi-mode structure).
