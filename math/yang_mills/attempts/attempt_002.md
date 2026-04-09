# Attempt 002 — Viable Proof Paths Ranked

**Date**: 2026-04-07
**Phase**: 1 (Paper Arsenal)
**Instance**: Even (Theory)

## Four Paths (from paper survey)

### Path A: Complete Balaban's Program (Constructive RG)
**Steps**: UV stability (large field) → continuum limit → infinite volume → OS axioms → mass gap
**Status**: Most advanced. 3D complete, 4D small-field done.
**Gap**: Large field bounds in 4D never published. Composition over ∞ RG steps unverified.
**People alive who understand it**: ~5-10 (Balaban retired, Sénéor deceased 2021)
**Sigma Method fit**: HIGH. Systematic, each step formalizable.
**Risk**: 2000+ pages of estimates. Could take decades.

### Path B: Stochastic Quantization (Hairer School)
**Steps**: Critical regularity structures → global existence of 4D gauge Langevin → invariant measure → OS axioms → mass gap
**Status**: 2D done, 3D local. 4D is critical (marginal) — current tech handles subcritical only.
**Gap**: Need breakthrough in critical singular SPDEs. Active research (Hairer, Chevyrev, Chandra, Shen).
**Sigma Method fit**: MEDIUM. More modern, but the 4D barrier is the same.
**Risk**: The critical case may be fundamentally harder, not just technically harder.

### Path C: Probabilistic Lattice (Chatterjee School)
**Steps**: Strong-coupling area law → extend to weak coupling → continuum limit → OS
**Status**: Strong coupling done. Weak coupling completely open.
**Gap**: The interpolation from strong to weak coupling. No known technique.
**Sigma Method fit**: HIGH for Odd instance (computational). The theory side needs Path A.
**Risk**: Strong-to-weak coupling interpolation may not exist smoothly.

### Path D: New Framework
**Ideas**: Operator algebras, topological QFT, categorical methods, information theory
**Status**: Beautiful frameworks, zero concrete results for YM₄.
**Gap**: Everything.
**Sigma Method fit**: LOW. Can't systematize what doesn't exist.
**Risk**: Could waste years on aesthetics.

## Decision

**Primary**: Path A (Balaban). This is the only path with a partially complete program.
The Even instance will formalize Balaban's framework and identify exactly where it breaks.

**Secondary**: Path C (lattice numerics). The Odd instance builds the SOS certificate
analog — rigorous bounds on lattice quantities.

**Monitor**: Path B (stochastic). If Hairer's group cracks critical regularity structures,
pivot immediately.

## The Honest Assessment

Nobody is close to solving this. The gap between what's known and what's needed is vast:
- **UV**: Controlled (asymptotic freedom + Balaban small field)
- **IR**: Completely open (mass gap is an IR phenomenon)
- **The actual hard part**: Proving that the lattice theory, in the continuum limit,
  has exponentially decaying correlations. This requires controlling the theory at ALL
  scales simultaneously — UV, intermediate, and IR.

The closest analog from NS: this is like needing to control the full nonlinear dynamics,
not just local estimates. The "one gap" here is: **exponential clustering in the
continuum limit of 4D lattice YM**.

## Result
Path ranking established. Even instance proceeds with Balaban formalization.
