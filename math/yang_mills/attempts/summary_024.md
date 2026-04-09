# Summary After 24 theory track Attempts

**Date**: 2026-04-07
**Phase**: 3 (Proof Attempts — mid-phase)
**Instance**: Even (Theory)
**Repo**: github.com/gobbleyourdong/math_problems, branch even/session_1

## The Proof Architecture

```
YANG-MILLS MASS GAP
    ↑ (spectral theory / Chatterjee 2021)
CONFINEMENT FOR ALL β (area law)
    ↑ (Tomboulis 2007 framework)
INEQUALITY (5.15): ⟨O⟩_per ≥ ⟨O⟩_anti
    ↑ (center decomposition, CenterDecomposition.lean — PROVED)
⟨O⟩_odd_sector ≥ ⟨O⟩_even_sector
    ↑ (????)
THE GAP: uniformity of MK decimation in thermodynamic limit
```

## Route Status After 24 Attempts

### DEAD (formalized as theorems):
| # | Route | Kill reason | Attempt |
|---|-------|-------------|---------|
| 1 | Lee-Yang / Fisher zeros | No gauge theory analog (50 years) | 007-008 |
| 2 | Spin foam positivity | 6j-symbols mixed signs | 008 |
| 3 | Balaban completion | Large field entropy exp vs linear | 005 |
| 4 | FKG for SU(2) | Not a distributive lattice | 020 |
| 5 | Convexity interpolation | Convex ≠ analytic (counterexample) | 010 |

### ALIVE:
| # | Route | Status | Rating |
|---|-------|--------|--------|
| 1 | Tomboulis + uniformity | Gap = MK decimation uniform in volume | ★★★★★ |
| 2 | Topological (Faddeev-Niemi/trefoil) | Exploring (agent running) | ★★★? |
| 3 | SZZ/Nissim extension | Strong coupling only, no path to weak | ★★ |
| 4 | Tomboulis-Yaffe BC insensitivity | Not yet explored in depth | ★★★ |

## Lean Formalization

| File | Proofs | Sorry | Key Result |
|------|--------|-------|------------|
| Identities.lean | 1 | 1 | trace_cyclic |
| FiniteLatticeGap.lean | 2 | 0 | boltzmann_weight_pos, finite lattice gap |
| NoPhaseTransition.lean | 1 | 1 | pos_of_continuous_never_zero |
| Convexity.lean | 0 | 1 | pressure_convex (sorry) |
| MKDecimation.lean | 1 | 1 | sandwich_to_zero, interpolation (sorry) |
| VortexCost.lean | 1 | 0 | expectation_comparison_from_covariance |
| SpectralPositivity.lean | 4 | 0 | spectral_positivity (Lehmann representation) |
| CenterDecomposition.lean | 2 | 0 | center_decomposition_identity, sign theorem |
| **TOTAL** | **12** | **4** | |

## Key Theorems Proved

1. **Spectral positivity**: G(P,Q) ≥ 0 for plaquette correlators under RP measure
2. **Center decomposition**: Sign(⟨O⟩_per - ⟨O⟩_anti) = Sign(⟨O⟩₋ - ⟨O⟩₊)
3. **Sandwich convergence**: MK coefficients → 0 (strong coupling)
4. **Expectation comparison**: Negative covariance → larger expectation
5. **Finite lattice gap**: Transfer matrix has gap (Krein-Rutman argument)

## The Refined Gap Statement

After 24 attempts, 7 research agents, and 5 killed routes:

**THE GAP**: Tomboulis's MK decimation flows the exact lattice coefficients
to the strong coupling regime (proved by sandwich theorem). At strong coupling,
inequality (5.15) holds (proved by cluster expansion). The question is whether
"in the strong coupling regime" means "close enough to zero for the cluster
expansion to converge uniformly in the lattice size."

Quantitatively: after n decimation steps, the exact coefficients satisfy
0 ≤ c̃_j(n) ≤ c_j^U(n). If c_j^U(n) < ε₀ (the cluster expansion radius),
then the cluster expansion converges and (5.15) holds. The question is
whether n₀ (the number of steps to reach ε₀) is INDEPENDENT of the
lattice size |Λ|.

This is a QUANTITATIVE ANALYSIS question, not a conceptual one.

## What the numerical track Should Do

Priority-ordered requests:
1. **MK decimation + vortex cost** (request_020): Test Z > Z⁺ under decimation
2. **Plaquette correlation sign**: Cov(Tr(U_P), Tr(U_Q)) ≥ 0 for all β
3. **Center sector comparison**: ⟨O⟩₋ vs ⟨O⟩₊ for SU(2) on small lattices
4. **Trefoil energy**: If the topological route opens, compute knot energies

## What's Running

- Agent: Faddeev-Niemi topological mass gap analysis (background)

## Session Statistics

| Metric | Count |
|--------|-------|
| Even attempts | 13 (002-024, even only) |
| Summaries | 2 (010, 024) |
| Lean proofs | 12 |
| Lean sorry | 4 |
| Dead ends | 5 |
| Research agents | 7 (all completed or running) |
| Papers in manifest | 40+ |
| Routes explored | 9 |
| Routes alive | 4 |
