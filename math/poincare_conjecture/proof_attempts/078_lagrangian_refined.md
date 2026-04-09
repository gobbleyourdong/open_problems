---
source: Refined Lagrangian argument without tube model
type: SCALING ARGUMENT — ρ ≤ C^{1/5} |ω₀|^{4/5}
status: Heuristic scaling, not rigorous. The 1/σ₃ estimate needs proof.
date: 2026-03-26 cycle 24
---

## Refined Argument

### Chain of rigorous identities:
1. ω(Φ(t,a),t) = (∇Φ)·ω₀(a) (Cauchy formula, exact)
2. det(∇Φ) = 1 (incompressibility, exact)
3. Sheet-like strain during stretching: σ₁ ≈ σ₂, σ₃ = 1/σ₁² (Betchov)
4. ρ = |ω| = σ₁ × |ω₀| (from Cauchy + alignment)

### The scaling estimate (HEURISTIC):
5. |∇ξ| ~ 1/σ₃ = σ₁² (direction changes on the thin-direction scale)
6. ∫ρ|∇ξ|² ~ ρ × σ₁⁴ = ρ⁵/|ω₀|⁴ (from steps 4,5)
7. Constantin: ∫ρ|∇ξ|² ≤ C → ρ⁵ ≤ C|ω₀|⁴ → ρ ≤ (C|ω₀|⁴)^{1/5}

### The bound:
```
||ω(t)||_∞ ≤ (C(ν,E₀) × ||ω₀||_∞⁴)^{1/5}
```

Bounded by initial data → REGULARITY.

## Why This Isn't (Yet) a Proof

Step 5 (|∇ξ| ~ 1/σ₃) is a SCALING ESTIMATE for organized vortex
structures (tubes/sheets). In reality:

- |∇ξ| at a point depends on the SPATIAL structure of ξ, not
  just the Lagrangian stretching at that point
- The estimate assumes the direction ξ changes primarily across
  the thin direction (σ₃ scale), not along the tube
- The spatial integral ∫ρ|∇ξ|² involves ALL points, not just
  the material element at x*

## The Gap (One Step)

Need to prove: at the max point x*, the direction gradient |∇ξ|
is bounded below by C/σ₃ (the reciprocal of the thin-direction
Lagrangian stretch factor).

Physical argument: ξ changes from ê at x* to some different
direction at distance σ₃ (the compressed scale). The direction
change is O(1) over distance σ₃, giving |∇ξ| ~ 1/σ₃.

Rigorous version: need to show the vorticity direction MUST CHANGE
by O(1) over the compressed scale. This requires the vorticity
outside the "sheet" (at distance σ₃ from x*) to have a different
direction than ê.

From single-mode orthogonality: ê is perpendicular to the strain
eigenvectors of each contributing mode. In the thin direction
(σ₃ scale), the modes with wavenumber ~ 1/σ₃ contribute strain
perpendicular to their own vorticity. If ê is the dominant direction
at x*, the modes at scale 1/σ₃ must have vorticity in a DIFFERENT
direction (otherwise they'd be the same mode and contribute zero
self-stretching).

This is the connection between single-mode orthogonality and the
Lagrangian structure: the scale separation between the dominant
mode (at x*) and the interacting modes (at scale σ₃) forces
direction variation on the σ₃ scale.

## Status

The BEST heuristic argument we've found. The bound ρ ≤ C^{1/5}|ω₀|^{4/5}
would prove regularity with room to spare. The gap is ONE scaling
estimate (|∇ξ| ~ 1/σ₃) that connects Lagrangian deformation to
direction variation.

This estimate is TRUE for organized structures (tubes, sheets, filaments)
and is consistent with our curvature data. Making it rigorous
requires showing the vorticity direction MUST change across the
compressed Lagrangian scale — which is exactly what single-mode
orthogonality forces (different modes → different directions).

78 proof attempt files. The space converges.
