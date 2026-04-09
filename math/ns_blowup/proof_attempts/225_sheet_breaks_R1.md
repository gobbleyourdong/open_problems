---
source: Instance B — R = 2 for a flat sheet. R ≤ 1 is NOT universal.
range: 225
type: CRITICAL — the bound requires NS structure, not just Laplacian
date: 2026-03-29
---

## The Counterexample

f = exp(-z²/2σ²) (uniform in x,y), ê = (0,0,1).

H = diag(0, 0, f). H_dev,zz = 2f/3. R = |2f/3|/(f/3) = 2.

R = 2. The bound R ≤ 1 FAILS for this function.

## The Dimensional Structure

| Source type | Variation | R at max |
|------------|-----------|----------|
| 3D blob | x,y,z | R = 0 (isotropic) |
| Straight tube | x,y only | R = 1 (tube bound) |
| Flat sheet | z only | R = 2 (sheet bound) |

R depends on the DIMENSIONALITY of the source concentration:
- d=3 (isotropic): R = 0
- d=2 (tube, no z-variation): R = 1
- d=1 (sheet, no x,y-variation): R = 2
- d=0 (point): R = 0 (isotropic by symmetry)

## What This Means for the Proof

R ≤ 1 is NOT a universal property of the Laplacian on T³.
It requires the source to have at least 2D spatial variation
(not purely 1D like a sheet).

The NS source Δp = |ω|²/2 - |S|² has TUBE structure:
- Concentrated along vortex lines (1D curves)
- Cross-section in 2D (perpendicular to the tube)
- This gives d=2 variation → R ≤ 1

A sheet-like source would need the vorticity to be concentrated
in a 2D surface. But incompressible vorticity satisfies ∇·ω = 0,
which means ω must be TANGENT to any surface of concentration.
This forces the source to have tube-like (not sheet-like) structure.

## The Missing Argument

PROVE: for div-free ω on T³, the source Δp = |ω|²/2 - |S|² has
enough cross-sectional (⊥ê) variation at the max that R ≤ 1.

This requires: ω is div-free → source has tube structure → R ≤ 1.

The div-free constraint is the KEY NS structure (Tao's barrier):
- Div-free ω cannot be purely 1D (a sheet of ω would violate ∇·ω = 0
  unless ω is tangent to the sheet → the source has ⊥ variation)
- The Biot-Savart law creates the 2D cross-sectional structure

## Implication

Instance A's proof (file 267, 188) needs modification:
the bound R ≤ 1 requires the div-free constraint on ω,
not just positivity of f. The Fourier lemma (file 267) is
correct but applies to the NS source specifically, not to
arbitrary non-negative functions.

The proof structure is SOUND but it needs the additional
ingredient: ∇·ω = 0 implies tube-like source structure.

## 225 — The sheet breaks R ≤ 1. Proof needs div-free constraint.
