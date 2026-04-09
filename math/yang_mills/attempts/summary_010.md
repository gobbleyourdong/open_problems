# Summary After 10 Attempts — Yang-Mills Even Instance

**Date**: 2026-04-07
**Phase**: 2 (Exploration, mid-phase)
**Instance**: Even (Theory)

## What We've Done

### Phase 1 (Paper Arsenal): COMPLETE
- 40+ papers catalogued in MANIFEST.md with equations
- Balaban RG fully digested (BALABAN_RG.md)
- Mathlib4 coverage mapped (8 critical gaps identified)
- Phase transition literature exhaustively surveyed

### Phase 2 (Exploration): IN PROGRESS — 10 attempts, 5 routes explored

## Route Status

| # | Route | Attempts | Status | Rating |
|---|-------|----------|--------|--------|
| 1 | Extend Chatterjee 't Hooft to finite N | 009 | **INVESTIGATING** | ★★★★★ |
| 2 | Fix Tomboulis RG decimation | 009 | **INVESTIGATING** | ★★★★ |
| 3 | Convexity interpolation | 010 | **KILLED** (insufficient) | ★★ |
| 4 | Tomboulis-Yaffe BC insensitivity | 009 | Not yet explored | ★★★ |
| 5 | Fisher zeros / Lee-Yang | 007-008 | **KILLED** (no gauge analog) | ✗ |
| 6 | Direct Balaban completion | 005 | **KILLED** (entropy obstruction) | ✗ |
| 7 | Character expansion | 004 | Informative but limited | — |
| 8 | Finite lattice gap (Krein-Rutman) | 004 | **PROVED** (warm-up only) | ✓ |

## Dead Ends Formalized

1. **Lee-Yang / Fisher zeros** (attempts 007-008): No gauge theory analog of
   Lee-Yang theorem exists. 6j-symbols have mixed signs. 50 years, no progress.
   DEAD.

2. **Convexity interpolation** (attempt 010): Convexity of pressure is proved
   but insufficient. Analyticity of p ⟺ clustering ⟺ mass gap. Circular.
   DEAD as standalone route.

3. **Balaban infinite composition** (attempt 005): Large field entropy
   exp(c'L^{4k}) beats suppression exp(-c·b₀·k·log L) at all large k.
   The fundamental obstruction. DEAD without new large field bounds.

## Theorems Proved

| Theorem | File | Status |
|---------|------|--------|
| trace_cyclic | Identities.lean | Proved |
| boltzmann_weight_pos | FiniteLatticeGap.lean | Proved |
| finite_lattice_mass_gap_exists | FiniteLatticeGap.lean | Proved (trivial) |
| pos_of_continuous_never_zero_pos_somewhere | NoPhaseTransition.lean | 1 sorry (IVT reverse) |
| pressure_convex | Convexity.lean | 1 sorry (calculus) |

## The Current Gap (Best Understanding)

**Gap A** (lattice mass gap for all β): The mass gap Δ(β) > 0 is known at
strong coupling (β small, Osterwalder-Seiler) and on finite lattices (all β,
Krein-Rutman). The question is: does Δ(β) > 0 persist for the infinite lattice
at ALL β > 0?

**Best lead**: Adhikari-Butez-Chatterjee (2025) proved this for U(N) in the
't Hooft limit. If their methods extend to finite N, Gap A is closed.

**Gap B** (continuum limit): Separate question — does the lattice mass gap
have a nonzero limit as the lattice spacing → 0? This requires UV control
(Balaban-type). Less urgent than Gap A.

## What's Running

- Agent analyzing arXiv:2510.22788 (Chatterjee 't Hooft mass gap)
- Agent analyzing arXiv:0707.2179 + arXiv:0711.4930 (Tomboulis + critique)

## Next Steps

1. Integrate Chatterjee and Tomboulis agent results
2. If Chatterjee methods look extendable → pursue Route 1
3. If Tomboulis gap is fixable → pursue Route 2
4. Explore Route 4 (Tomboulis-Yaffe BC insensitivity) if Routes 1-2 stall
5. Every 10 more attempts: write another summary

## Lean Status: 6 files, 5 proofs (2 sorry), ~500 LOC
## Attempts: 10 + 1 summary
## Agents launched: 5 (all completed or running)
