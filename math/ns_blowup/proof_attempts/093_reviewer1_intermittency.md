---
source: Reviewer 1 gap-fill response
type: CRITICAL INSIGHT — need spatial intermittency bound
date: 2026-03-26
---

## Reviewer 1's Verdict on Our Three Approaches

### 1. ||Q||/||-ΔS|| < 1: FAILS
- ||S²||_{L²} ≤ C||S||_{L∞}||S||_{L²} ≤ C||-ΔS||_{L²}||S||_{L²}
- The ratio ||S²||/||-ΔS|| ~ ||S||_{L²} (enstrophy) which GROWS
- Pointwise Lean lemma → global L² norm requires intermittency

### 2. Advection term: FAILS
- ||(u·∇)S||_{L²} ≤ ||u||_{L∞}||∇S||_{L²}
- ||u||_{L∞} needs H^{3/2+} regularity — circular
- Transport preserves magnitude but stretches gradients

### 3. Galerkin eigenfunction distance: FAILS to be uniform in N
- Optimal ρ tracks dominant wavenumber → N-dependent
- Bernstein: ||-ΔS_N|| ≤ N²||S_N|| — explicit N divergence
- Uniform in N ↔ energy cascade halts ↔ regularity (circular)

## THE KEY INSIGHT: Spatial Intermittency

To bridge pointwise Lean lemmas to Miller's L² criterion:

**Need:** Vol({x : |S(x)| > λ/2}) ≤ C λ^{-γ} for large enough γ.

This is a LEVEL SET GEOMETRY bound — exactly Grujić's program!

If the high-strain region is sufficiently SPARSE (thin filaments/sheets):
||S²||_{L²}² = ∫|S|⁴ dx ≤ ||S||_{L∞}² × ∫_{|S|>λ/2} |S|² dx
             ≤ ||S||_{L∞}² × λ² × Vol(high-strain) ≤ C λ^{4-γ}

For γ > 2: ||S²||_{L²} grows SLOWER than ||S||_{L∞}² → the ratio
||S²||_{L²}/||-ΔS||_{L²} is sublinear in enstrophy.

## Connection to Our Data

- Event duration τ ~ ρ^{-3}: implies extreme SPATIAL LOCALIZATION
- The high-strain region shrinks as ρ grows
- Our convergence data: ratio=1.0 at N≥64 means the localization IS happening
- Grujić (2012): near blowup, super-level sets are thin filaments with
  cross-section ~ ρ^{-1/2}, volume ~ ρ^{-3/2} (γ = 3/2 from Chebyshev)

## The Gap (Refined)

Need γ > 2 for the intermittency to close Miller's criterion.
Chebyshev gives γ = 3/2 (from ||ω||_{L¹} bounded).
Better than Chebyshev requires USING the Biot-Savart structure.

This is Grujić's EXACT gap: proving the super-level sets are
SPARSER than Chebyshev predicts. His scaling gap paper (2018)
pushed the a priori from γ=1/3 to γ=2/5 using component-level
sparseness. Need γ > 2 but have γ ≤ 2/5.

The gap from γ=2/5 to γ=2 is LARGE. But our DATA shows γ >> 2
(the high-strain region collapses much faster than Chebyshev).

## For Reviewers 2 and 3

Question: Can we prove Vol({|S| > λ}) ≤ C λ^{-γ} with γ > 2
using the Biot-Savart structure + single-mode orthogonality?

The single-mode orthogonality restricts WHERE strain can be large:
strain requires CROSS-MODE interactions (self-stretching = 0).
Cross-mode interactions have PHASE structure that limits the
volume where they constructively interfere.

Is this a quantifiable sparseness bound?
