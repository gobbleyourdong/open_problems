# Attempt 004 — The Character Expansion Route

**Date**: 2026-04-07
**Phase**: 1→2 (Arsenal → Formalization)
**Track**: theory (Theory)

## Observation

The lattice partition function can be EXACTLY expanded using representation
theory of the gauge group. This is the **character expansion** (also called
strong coupling expansion or high-temperature expansion).

For SU(N), the Peter-Weyl theorem says L²(SU(N)) decomposes into matrix
elements of irreducible representations:

  L²(G) = ⊕_R dim(R) · V_R ⊗ V_R*

The Boltzmann weight for a single plaquette is:

  exp(β/N · Re Tr(U_P)) = Σ_R d_R · a_R(β) · χ_R(U_P)

where:
- R ranges over irreps of SU(N)
- d_R = dim(R)
- χ_R = character (trace in representation R)
- a_R(β) = modified Bessel function ratios (known explicitly for SU(2))

For SU(2): a_j(β) = I_{2j+1}(β) / I_1(β), where I_n is the modified Bessel
function and j = 0, 1/2, 1, 3/2, ... labels irreps.

## Why This Matters

### The partition function becomes EXACT
Z = ∫ ∏_ℓ dU_ℓ · ∏_P [Σ_R d_R a_R(β) χ_R(U_P)]

The link integrals can be done using orthogonality of matrix elements:
∫_G D^R_{ij}(U) D^{R'}_{kl}(U†) dU = (1/d_R) δ_{RR'} δ_{ik} δ_{jl}

This is a COMBINATORIAL sum over assignments of irreps to plaquettes,
weighted by a_R(β) factors, with combinatorial constraints from link sharing.

### The transfer matrix is EXACTLY diagonalizable (in principle)
In the character expansion basis, the transfer matrix is a matrix of
known Bessel function ratios. The eigenvalues can be computed.

### The mass gap is VISIBLE
Δ(β) = -ln(a_{1/2}(β) / a_0(β)) + corrections from spatial plaquettes

For SU(2) at strong coupling (small β):
  a_{1/2}(β) / a_0(β) ≈ β/4 + O(β³)
  Δ ≈ -ln(β/4) → ∞ as β → 0 ✓

For SU(2) at weak coupling (large β):
  a_{1/2}(β) / a_0(β) ≈ 1 - 3/(2β) + O(1/β²)
  Δ ≈ 3/(2β) → 0 as β → ∞

Wait — Δ → 0 as β → ∞? That looks like the mass gap DISAPPEARS!

## The Subtlety: Lattice Units vs Physical Units

Δ above is in LATTICE UNITS (dimensionless). The PHYSICAL mass gap is:
  m = Δ/a

As β → ∞ (continuum limit), a → 0 with the relationship:
  a = (1/Λ_QCD) exp(-1/(2b₀g²)) = (1/Λ_QCD) exp(-β/(4b₀N))

For SU(2): b₀ = 22/(48π²), so:
  a ~ exp(-β · 48π²/(88)) = exp(-β · π²/2 · 12/22)

The physical mass gap is:
  m = Δ(β) / a(β) = [3/(2β)] / [Λ⁻¹ exp(-cβ)]
    = (3Λ/(2β)) exp(cβ)
    → ∞ as β → ∞

That's WRONG — the physical mass gap should be FINITE (m ~ Λ_QCD).

## The Real Scaling

The naive character expansion breaks down at weak coupling because:
1. The expansion is in powers of a_R(β), which all → 1 as β → ∞
2. The mass gap comes from CANCELLATIONS between many terms
3. The dominant contribution shifts from single-plaquette to extended objects

The correct weak-coupling behavior requires RESUMMING the character expansion.
This resummation is essentially the RG (Balaban's program).

## What This Means for the Proof

The character expansion gives us:
✅ EXACT results at strong coupling (converges absolutely)
✅ A basis for the transfer matrix (representation theory)
✅ A framework where the mass gap is a COMBINATORIAL question

But it does NOT give us:
❌ Weak coupling behavior (expansion diverges / loses accuracy)
❌ The continuum limit directly
❌ The non-perturbative mass gap

## The Route This Suggests

**Hybrid approach**: Use the character expansion at strong coupling (where it converges)
and Balaban's RG at weak coupling (where perturbation theory is valid). The mass gap
must be proved to be CONTINUOUS in β — it exists at strong coupling (proven) and the
question is whether it survives to weak coupling.

This is a MONOTONICITY or CONTINUITY argument:
"Can the mass gap vanish at some intermediate β?"

If we could prove Δ(β) > 0 for ALL β > 0, we'd have the lattice mass gap.
Then the continuum limit question is separate.

## Key Observation

On a FINITE lattice, the transfer matrix is a positive-definite operator
on a compact space. By Perron-Frobenius theory (for positive matrices /
positive kernels), the leading eigenvalue is simple and strictly larger
than all others. So:

**Theorem (finite lattice mass gap)**: For any finite periodic lattice Λ,
any compact simple gauge group G, and any β > 0, the transfer matrix T(β)
has a unique largest eigenvalue λ₀ > λ₁ ≥ λ₂ ≥ ...

Proof: T has a strictly positive continuous kernel (the Boltzmann weight
exp(-S) > 0 everywhere on G^{links}). By the Krein-Rutman theorem
(infinite-dimensional Perron-Frobenius), the leading eigenvalue is simple.

**This is PROVABLE in Lean.** It's a real theorem, not a conjecture.

## Result
The character expansion gives exact strong-coupling mass gap. The finite-lattice
mass gap is a theorem (Perron-Frobenius/Krein-Rutman). The open problem reduces
to: does the gap survive the infinite-volume and continuum limits?

## Next Steps
1. Formalize the finite-lattice mass gap theorem in Lean
2. Implement the character expansion numerically (numerical track)
3. Study Δ(β) as a function of β for small lattices
