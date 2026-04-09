# Attempt 004 — Routes Ranked by systematic approach Fit

**Date**: 2026-04-07
**Phase**: 1 (Paper Arsenal)
**Instance**: Even (Theory)

## Ranking Criteria

The systematic approach favors:
1. Routes with COMPUTATIONAL certification targets (numerical track work)
2. Routes where DEAD ENDS can be formalized as theorems
3. Routes where the GAP can be precisely identified
4. Routes that build on EXISTING rigorous results

## Route Rankings

### 1. Connes' Program (Weil Positivity) ★★★★★

**Why #1**: This is the ONLY route with a complete roadmap where partial
results exist (archimedean case proved 2023) and the remaining gap is
precisely identified (finite prime positivity).

**The gap**: Prove positivity of the Weil distribution on test functions
supported on [0,1], restricted to contributions from finite primes.
This is a concrete analytical/algebraic condition.

**systematic approach fit**:
- Lean: formalize the archimedean result (Connes 2023)
- Numerics: compute the Weil distribution numerically, check positivity
- Certificates: verify positivity for increasingly large truncations
- Gap: precisely identified (finite prime contribution)

**Risk**: May require decades of F₁ geometry development.

### 2. de Bruijn-Newman Constant (Λ = 0) ★★★★

**Why #2**: RH ⟺ Λ = 0. Currently 0 ≤ Λ ≤ 0.22. The gap is QUANTITATIVE
— push the upper bound from 0.22 to 0.

**systematic approach fit**:
- Numerics: compute Λ upper bounds with interval arithmetic
- Certificates: each improvement Λ ≤ c is a certificate
- The gap narrows with computation: Polymath 15 got 0.22, can we get 0.1? 0.01?
- Lean: formalize the heat equation analysis

**Risk**: The bound Λ ≤ 0.22 used massive computation. Getting to Λ = 0
might require infinite computation (the bound might not converge to 0
with current methods).

### 3. Li's Criterion (λ_n ≥ 0) ★★★

**Why #3**: Direct computational target. λ_n computable for each n.

**systematic approach fit**:
- Numerics: compute λ_n for n up to 10^6 or beyond
- Certificates: each verified λ_n ≥ 0 is a certificate
- Look for STRUCTURE in the λ_n sequence
- Lean: formalize the Li equivalence theorem

**Risk**: Proving λ_n ≥ 0 for ALL n is as hard as RH. The per-n certificates
don't accumulate into a proof (unlike the NS SOS certificates which covered
a continuous parameter space).

### 4. Hilbert-Pólya (Operator Search) ★★★

**Why #4**: If the operator is found, the proof is immediate. The search
is parallelizable and can be guided by numerics.

**systematic approach fit**:
- Numerics: test candidate operators against known zeros
- Certificates: eigenvalue matching to high precision
- Lean: formalize self-adjointness criteria
- The search space is large but structured (Berry-Keating gives the target)

**Risk**: The operator might not exist in any "nice" form. 170 years of
searching with nothing to show.

### 5. Guth-Maynard Extensions ★★

**Why low**: Improves density near σ = 1, cannot reach σ = 1/2.
The exponential sum barrier is structural.

### 6. Analytic Zero-Free Region ★

**Why lowest**: Stuck for 65 years. The 2/3 exponent appears fundamental.

## Decision

**Primary route**: Connes' program (Weil positivity).
- theory track: study arXiv:2310.18663, formalize the framework
- numerical track: compute the Weil distribution numerically

**Secondary route**: de Bruijn-Newman Λ = 0.
- theory track: study Polymath 15, identify what limits the bound
- numerical track: attempt to push Λ upper bound below 0.22

**Computational**: Li's criterion λ_n.
- numerical track: compute λ_n for large n, look for patterns

## What the NS Campaign Teaches Us

In NS: the gap was a SINGLE INEQUALITY at a point. 547 attempts mapped it.
The certificates (1.33M SOS) gave quantitative confidence.

In RH: the gap is more diffuse. No single inequality captures it. But:
- The de Bruijn-Newman constant Λ is the CLOSEST to an NS-style gap
  (a single number that must be 0, currently bounded by 0.22)
- The Weil positivity is the DEEPEST structural formulation
- Li's criterion gives a SEQUENCE of certificates

The systematic approach should pursue ALL three in parallel: Connes (theory),
Λ (quantitative), Li (certificates).

## Result
Routes ranked. Primary = Connes (Weil positivity). Secondary = Λ = 0.
Computational = Li criterion. Three-pronged attack.
