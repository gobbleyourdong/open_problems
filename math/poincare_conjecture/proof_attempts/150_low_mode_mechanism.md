---
source: Galerkin truncation scaling — c₃ ≥ 1/3 is a LOW-MODE phenomenon
type: BREAKTHROUGH DATA — the mechanism needs only ~4 shells, not the cascade
date: 2026-03-28
---

## The Experiment

Run full NS dynamics (TG and KP) at N=32, ν=10⁻³.
At each diagnostic step, Galerkin-truncate to k_retain = 2, 4, 6, 8, 10, 21 (full).
Recompute c₁, c₂, c₃ from the truncated fields.

## Key Result: k ≤ 4 is SUFFICIENT

| k_retain | c₃ at t=0.1 (TG) | c₃ at t=0.4 (TG) | c₃ ≥ 1/3? |
|----------|------------------|------------------|-----------|
| 2        | 0.288            | 0.289            | NO (stuck) |
| 4        | 0.428            | 0.650            | YES ✓     |
| 6        | 0.441            | 0.643            | YES ✓     |
| 8        | 0.428            | 0.639            | YES ✓     |
| 10       | 0.427            | 0.652            | YES ✓     |
| 21 (full)| 0.426            | 0.648            | YES ✓     |

c₃ at k≤4 is INDISTINGUISHABLE from the full resolution result.

## Why k=4 is the threshold

TG IC modes: ω has wavenumber components (±1, ±1, ±1), so |k| = √3 ≈ 1.73.

Triadic products: (1,1,1) + (1,1,-1) = (2,2,0), |k| = 2√2 ≈ 2.83
                   (1,1,1) + (1,1,1) = (2,2,2), |k| = 2√3 ≈ 3.46

At k≤2: the (2,2,2) and (0,2,2) products are LOST. Only partial interactions survive.
At k≤4: ALL first-generation triadic products are captured. Full interaction set.

The c₃ mechanism operates within the FIRST TRIADIC GENERATION of the IC modes.

## Experiment 2: Galerkin truncation DURING evolution

Even when we truncate at k_trunc=4 at EVERY timestep (forcing dynamics to stay
within 4 shells), the result is the same:

| k_trunc | c₃ at t=0.4 (TG) |
|---------|------------------|
| 4       | 0.640            |
| 8       | 0.644            |
| 16      | 0.630            |
| 21      | 0.644            |

The dynamics within 4 shells are SELF-SUFFICIENT. No cascade needed.

## KP confirmation

KP IC has modes at |k| up to ~4.4 (wavenumbers 1 and 3).
At k≤4: c₃ = 0.32 (borderline). At k≤6: c₃ = 0.37+. At k≤8: c₃ = 0.41.
KP needs k≤6 because its IC has higher wavenumber content.

Consistent: the mechanism needs ONE FULL TRIADIC GENERATION of the IC modes.

## Pressure Hessian

Yang degeneracy (⊥ω eigenvalue ratio) ≈ 1.5 — NOT degenerate.
The full pressure Hessian is NOT well-approximated by Yang's local formula.
But ê·H·ê (ω-projection) > 0 — pressure DOES oppose stretching.

## What This Means for the Proof

1. The mechanism is FINITE-DIMENSIONAL — ~268 modes for TG, ~804 real DOF
2. The TG octahedral symmetry reduces this dramatically
3. The c₃ ≥ 1/3 property could potentially be proven for the TRUNCATED Galerkin ODE
4. Then: Galerkin convergence theorems give the full PDE result

This changes the proof strategy from "analyze the infinite-dimensional PDE" to
"analyze a finite-dimensional ODE and lift the result."

## The Mechanism (physical interpretation)

The TG vortex sheets create strain. The strain eigenvectors are determined by
the velocity gradient. When the vortex sheets interact (first triadic generation),
the resulting strain field has e₃ (compressive) aligned with ω.

This is NOT the cascade. This is NOT multi-scale. This is the GEOMETRIC CONSEQUENCE
of incompressible triadic interactions at the fundamental wavenumber.

## Next Steps

1. Find the MINIMAL number of modes: which specific k-vectors are needed?
2. Write out the Galerkin ODE for TG with k≤4 (finite system)
3. Analyze the ODE: prove c₃ ≥ 1/3 for this specific system
4. Lift to full PDE via Galerkin convergence

## 150 proof files. The mechanism is LOW-MODE.
