# Attempt 003 — The Structure of the Gap

**Date**: 2026-04-07
**Phase**: 1 (Paper Arsenal)
**Instance**: Even (Theory)

## What Makes YM₄ Unique

Every solved constructive QFT problem (φ⁴₂, φ⁴₃, 2D YM, 3D YM partial) has
a dimensional coupling constant. This means:

- Finitely many UV divergences → finitely many RG steps
- The coupling provides a natural mass scale
- The mass gap is "obvious" from dimensional analysis

YM₄ has a DIMENSIONLESS coupling. This means:

- Infinitely many UV divergences → infinitely many RG steps (each log-suppressed)
- No classical mass scale (conformal at classical level)
- The mass gap is DYNAMICALLY GENERATED through dimensional transmutation
- Λ_QCD = μ exp(-1/(2b₀g²(μ))) — an exponentially small scale

## The Three Miracles Needed

### Miracle 1: UV Stability (Partially Achieved)
Balaban proved: at each RG step, the effective action is controlled in the small-field
region. The renormalized coupling runs according to asymptotic freedom.

**What remains**: Large field control + composition over all scales.

### Miracle 2: Thermodynamic Limit (Not Started)
The infinite-volume limit must exist. This requires:
- Cluster expansion: correlations decay fast enough that distant regions decouple
- Pressure exists: free energy per unit volume has a limit
- Translation invariance of the limiting state

For superrenormalizable theories (3D), this follows from standard cluster expansion
(Glimm-Jaffe-Spencer). For 4D, the marginal coupling makes everything harder.

### Miracle 3: Mass Gap / Exponential Clustering (The Prize)
The connected 2-point function must decay exponentially:
⟨O(x)O(0)⟩_c ≤ C exp(-Δ|x|), Δ > 0

**This is the mass gap.** It's equivalent to:
- Spectral gap of the Hamiltonian
- Exponential decay of transfer matrix correlations
- Analyticity of the free energy in the fugacity

## The NS Parallel

In NS: the gap was "prove C > -|ω|²/4 at the vorticity maximum."
All routes led to this one inequality. 547 attempts. The gap = Liouville conjecture.

In YM: the gap (preliminary assessment) is:
**"Prove exponential clustering for the continuum limit of 4D lattice Yang-Mills."**

This decomposes into:
1. The continuum limit EXISTS (Balaban program + large field + composition)
2. The limit has EXPONENTIAL CLUSTERING (mass gap)

These may be two separate gaps, or they may be one (if the construction method
automatically gives clustering).

## What I Think the Real Gap Is

The NS gap turned out to be a single inequality at a specific point (the max of |ω|).
What's the YM analog?

**Candidate**: The "spectral gap of the block-averaged transfer matrix survives
the continuum limit."

More precisely: on the lattice at spacing a, the mass gap is Δ(a). We need:
lim_{a→0} Δ(a) = Δ > 0

The lattice mass gap Δ(a) exists for any a > 0 (finite lattice, positive transfer
matrix). The question is whether it persists in the limit.

**Why it might not**: If the theory is trivial (like φ⁴₄), Δ(a) → ∞ (free theory,
no particles). But YM is asymptotically free, so it should be non-trivial, and
Δ(a) should converge to a finite nonzero value.

**The key bound needed**: Something like
  Δ(a) ≥ c · Λ_QCD = c · (1/a) exp(-1/(2b₀g²(a)))
This is nonperturbative — the RHS is exponentially small in 1/g², invisible to
perturbation theory. This is the non-perturbative IR bound.

## What the numerical track Should Test

1. Compute Δ(a) for SU(2) on small lattices as β = 2N/g² varies
2. Plot Δ(a) × a vs β — does it approach a constant? (= mass gap in physical units)
3. Look for any β where Δ(a) gets suspiciously small
4. The scaling should be Δ(a) ~ (1/a) exp(-1/(2b₀g²(1/a))) in the weak coupling region

## Result
Gap structure identified (preliminary). The anti-problem is:
"What would Δ(a) → 0 look like? What lattice configurations drive the gap to zero?"

If we can prove such configurations have measure zero in the continuum limit,
we have the mass gap.
