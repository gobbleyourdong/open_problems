# Dumbbell PDE Simulation — DEAD END (Naive Warped Product)

**Date:** 2026-04-09
**Script:** `numerics/dumbbell_pde.py`
**Track:** Numerical
**Status:** **DEAD END — instructive failure**

## What Was Attempted

A 1D PDE solver for Ricci flow on a warped product 3-manifold:
  g = dx² + φ(x,t)² g_S²

Equation:
  ∂φ/∂t = φ'' - (φ'² - 1)/φ

Initial data: dumbbell profile (two Gaussian bulbs + thin neck at φ_min = 0.3).

## What Happened

**Test 1 (n=401, dt=0.0005, fine grid):**
- Step 99 (t=0.0495): neck min crashed to 1e-6 (numerical floor)
- The PDE became unstable when the neck got small, because the term
  (φ'² - 1)/φ blows up as φ → 0 with φ'² < 1
- Predicted singularity time from neck²/4 was 0.0225
- Actual "crash" at t=0.0495 — slightly past prediction, dominated by
  numerical instability rather than true geometric pinch

**Test 2 (n=201, dt=0.001, coarser grid):**
- The neck **FILLED IN** rather than pinched
- φ_min went from 0.300 → 2.06 over t ∈ [0, 2.0]
- Volume grew from 124 → 687 (5.5×)
- No pinch at any time tested

## Why This Is Instructive (Not a Bug)

The 1D warped-product model is **not faithful** to the 3D Ricci flow
on a dumbbell manifold for two reasons:

### 1. The +1/φ term is regularizing, not destabilizing

At a local minimum of φ (the neck), φ' = 0 and φ'' > 0. The PDE gives:
  ∂φ/∂t = φ'' - (0 - 1)/φ = φ'' + 1/φ > 0

So the neck WANTS TO GROW under this PDE, not shrink. This is opposite
to what happens in true 3D Ricci flow on a dumbbell, where the neck
shrinks because of the SECOND fundamental form contributions that are
absent in the 1D warped-product reduction.

### 2. Arclength is not preserved

In the warped product g = dx² + φ² g_S², we assumed x is arclength.
But under Ricci flow, the metric on the dx² direction also changes —
the parameterization needs to evolve. Using a fixed x-coordinate
loses the contribution from this evolution.

The CORRECT 1D model (Angenent-Knopf 2004) tracks both ψ(x,t)² and
the line element s(x,t)² simultaneously, and uses a self-similar
ansatz φ(x,t) = √(2(T-t)) · F(x/√(T-t)) for the neck region near
singularity.

## Lesson for the Numerical Track

The neck pinch in dumbbell Ricci flow is **inherently 3D** and
requires either:
- (a) Full 3D simulation on a triangulated manifold (the discrete
  Ricci flow that diverges on the 5-cell, see `discrete_ricci_flow.py`)
- (b) Self-similar Angenent-Knopf ansatz with TWO unknowns (φ, s),
  not one (just φ)
- (c) Symmetry-reduced ODE for the neck profile near singularity

The naive 1D warped-product PDE FAILS to reproduce the neck pinch.
This is why Perelman's proof works at the level of full 3-manifolds
(canonical neighborhood theorem), not at the level of effective 1D
reductions.

## Status

**DEAD END.** Recording per v6 "Maps include noise" principle:
this failure tells future explorers that the 1D warped-product model
is not the right tool for neck pinch verification.

Productive alternatives (next attempts):
- `angenent_knopf_shrinker.py` — analytical self-similar solution
- `3d_pinch_invariants.py` — compute curvature invariants on a
  parameterized dumbbell (no PDE evolution, just verify R blows up)
- `surgery_topology.py` — track topology change after surgery,
  not the metric evolution
