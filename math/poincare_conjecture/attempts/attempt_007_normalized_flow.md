# Attempt 007 — Normalized Ricci Flow: Still Diverges on 5-Cell

**Date**: 2026-04-07
**Phase**: 0 (Blind)
**Instance**: Odd

## Result

Normalized flow dl/dt = -(κ - r̄/3)·l still diverges on the 5-cell.
Ratio 1.33 → 18.4 in 300 steps. The normalization doesn't help.

## Why

The 5-cell has only 5 tetrahedra and 10 edges. The discrete curvature
(deficit angle) is poorly defined on such a coarse triangulation.
Small perturbations cause large curvature oscillations → instability.

## The Deeper Point

The SMOOTH Ricci flow works because:
1. The PDE has good short-time existence (parabolic, maximum principle)
2. Curvature estimates control the flow (Hamilton's work)
3. Singularities are classified (neck pinches, cusps)

The DISCRETE version fails because:
1. No maximum principle (discrete curvature can oscillate wildly)
2. No smooth curvature estimates
3. The triangulation topology is rigid (can't do surgery)

This is why Perelman needed SMOOTH analysis, not computation.
The Ricci flow approach is inherently ANALYTICAL, not computational.

## What the Odd Instance CAN Do

1. **Verify the flow on FINE triangulations** (1000+ tetrahedra)
   where discrete curvature is more reliable. Needs a mesh library.

2. **Test the 2D analog** (Ricci flow on surfaces). In 2D, discrete
   Ricci flow (circle packing) WORKS and proves the uniformization theorem.
   Implementing this would demonstrate the concept.

3. **Monitor topological invariants** during flow: if π₁ changes,
   the flow isn't preserving topology (sanity check).

## Prediction Update

The proof of Poincaré requires:
1. Smooth Ricci flow (PDE theory, not discretizable easily)
2. Entropy monotonicity (Perelman's W-functional? — I'm guessing blind)
3. Surgery at singularities (cut neck pinches, cap off)
4. Finite extinction for π₁ = 0 (the manifold shrinks to a point)

The odd instance can VERIFY these numerically on fine meshes but
can't substitute for the analytical proof.

## 007. Normalized Ricci flow still diverges on 5-cell (too coarse).
## Discrete curvature unreliable on 5 tetrahedra. The proof needs
## smooth PDE analysis — this is inherently analytical, not computational.
## Next: try 2D analog (circle packing) or finer 3D mesh.
