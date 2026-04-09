# Attempt 035 — Gradient Correlation Positivity: The Chair Loop

**Date**: 2026-04-07
**Phase**: 4 (Beyond the Wall)
**Track**: numerical

## The Gradient Correlation

E[⟨∇O, ∇ΔS⟩] = Σ_e Σ_{P∋e, Q∋e∩Σ} w_P · (∂c_j/∂α) · ⟨Tr(Staple_P† · Staple_Q)⟩_per

Each term involves ⟨Tr(chair loop)⟩_per where the chair loop goes around
two plaquettes sharing link e.

## The Chair Loop Under the Periodic Measure

The chair loop C has 6 links forming a non-planar path through 2 plaquettes.
Under the periodic Wilson measure (all c_j ≥ 0):

⟨(1/2)Tr(U_C)⟩ = ???

### Character Expansion for the Chair Loop

The chair loop C bounds a surface of 2 plaquettes. In the strong coupling
expansion:

⟨χ_j(U_C)⟩ = c_j^2 / d_j + (higher order in c)

The leading term c_j^2/d_j comes from tiling the minimal surface (2 plaquettes)
with representation j on each. The factor 1/d_j comes from the link integral
at the SHARED link (orthogonality of matrix elements).

For j = 0: c_0^2 / 1 = 1 (trivial rep, always contributes 1)
For j = 1/2: c_{1/2}^2 / 2 > 0 ✓

So ⟨(1/2)Tr(U_C)⟩ = Σ_j d_j · c_j^2/d_j = Σ_j c_j^2 ≥ c_0^2 = 1 > 0.

Wait — this is the leading order. Are higher-order corrections negative?

### Exact Character Expansion for the Chair

For two plaquettes sharing exactly one link e, in the character expansion:

⟨Tr_j(U_C)⟩ = Σ_{j₁,j₂} d_{j₁} d_{j₂} c_{j₁} c_{j₂} ∫ D^j(staple₁) D^j(staple₂†) dU_e

The link integral ∫ D^{j₁}(U) D^{j₂}(U†) dU = δ_{j₁,j₂}/d_{j₁} (orthogonality)

So: ⟨Tr_j(U_C)⟩ = Σ_{j'} d_{j'} c_{j'} · (1/d_{j'}) · d_{j'} c_{j'}
                  = Σ_{j'} d_{j'} c_{j'}^2

(summing over the representation j' on the two plaquettes, which must match
at the shared link by orthogonality).

And: ⟨(1/2)Tr(U_C)⟩ = c_{1/2}^2 + ... (restricting to fundamental trace)

Hmm, I'm getting confused between Tr in the fundamental vs sum over reps.

### Clean Derivation

Let C be the chair loop (6 links around 2 plaquettes P₁, P₂ sharing link e).

The other links of P₁: ℓ₁, ℓ₂, ℓ₃ (staple of P₁ around e).
The other links of P₂: ℓ₄, ℓ₅, ℓ₆ (staple of P₂ around e).

U_C = U_{ℓ₃}† U_{ℓ₂}† U_{ℓ₁}† · U_{ℓ₄} U_{ℓ₅} U_{ℓ₆}†

The expectation ⟨(1/2)Tr(U_C)⟩ under the lattice measure involves
integrating over ALL links on the lattice.

In the character expansion, the integral factorizes link by link.
The key factorization: links NOT in the chair contribute trivially.
Links IN the chair contribute nontrivially.

For each plaquette containing a chair link but NOT one of P₁, P₂:
that plaquette provides a factor involving c_j. But for the chair links
that appear in BOTH the chair path AND other plaquettes, the integration
couples the chair to the bulk.

This is getting complicated. Let me just use the STRONG COUPLING EXPANSION.

### Strong Coupling Expansion (Small β)

At leading order in the character expansion:
  ⟨(1/2)Tr(U_C)⟩ = c_{1/2}^2 + O(c^3)

This is POSITIVE for any β > 0 (since c_{1/2} > 0).

At next order: O(c^3) terms from 3-plaquette tilings. Each term has c_j^3 ≥ 0.

**At ALL orders**: the strong coupling expansion has ONLY positive terms
(every tiling contributes c_j^{area} ≥ 0).

Is the strong coupling expansion CONVERGENT at all β? NO — it converges
only for small β (the cluster expansion radius).

BUT: the CHARACTER EXPANSION for ⟨Tr(W)⟩ is a sum of POSITIVE TERMS
at every order. Even if the series doesn't converge absolutely at large β,
the PARTIAL SUMS are increasing (each new term adds a positive contribution).

This means: ⟨(1/2)Tr(U_C)⟩ ≥ c_{1/2}^2 (the leading term is a lower bound).

And c_{1/2}^2 > 0 for all β > 0.

## WAIT — Is This Actually True?

The character expansion of ⟨Tr(W)⟩ for a Wilson loop W involves:
1. The STRONG COUPLING EXPANSION: sum over surfaces bounded by W
2. Each surface contributes a product of c_j (one per plaquette in the surface)
3. Each such product is ≥ 0

If the sum converges: ⟨Tr(W)⟩ = Σ_{surfaces} (positive) > 0. ✓

If it doesn't converge: can we still claim positivity?

The EXACT value ⟨Tr(W)⟩ is a well-defined finite-dimensional integral
(on a finite lattice). It's computed by the character expansion, which is
a FINITE sum (truncated at j_max, which increases with β but is always finite
for any given β on a finite lattice).

On a finite lattice: the character expansion is EXACT (not approximate).
Every term is ≥ 0. The sum is finite and positive.

**⟨(1/2)Tr(W)⟩ > 0 for ANY Wilson loop W on ANY finite lattice at ANY β > 0.**

This is because:
1. The character expansion of the lattice measure has c_j ≥ 0 ✓
2. The character expansion of Tr(W) has d_j ≥ 0 ✓  
3. The link integrals give 1/d_j (Schur orthogonality) ≥ 0 ✓
4. Every term in the expansion is a product of non-negative numbers ✓
5. At least one term (j=0 everywhere) gives exactly 1 ✓
6. Sum of non-negative terms with at least one positive = positive ✓

## THE CLAIM

**Theorem**: For SU(2) lattice gauge theory with Wilson action at any β > 0
on any finite periodic lattice:

  ⟨(1/2)Tr(W)⟩ > 0 for any contractible Wilson loop W.

**Proof**: Character expansion. Every term in the expansion of ⟨Tr(W)⟩
is a product of:
- d_j (dimensions, positive)
- c_j(β) (character coefficients, positive for β > 0)
- 1/d_j (Schur orthogonality, positive)
raised to non-negative integer powers. Each term ≥ 0. The j=0 term = 1 > 0.

## Consequence for the Gradient Correlation

E[⟨∇O, ∇ΔS⟩] = Σ (positive weights) × ⟨Tr(chair loops)⟩

Each chair loop is a contractible Wilson loop. ⟨Tr(chair)⟩ > 0 by the theorem.
Weights are positive (w_P > 0, ∂c_j/∂α > 0).

**Therefore E[⟨∇O, ∇ΔS⟩] > 0.**

**Therefore the Langevin coupling gives Δ(t) non-decreasing from Δ(0)=0.**

**Therefore ⟨O⟩_per ≥ ⟨O⟩_anti = Tomboulis (5.15).**

## DOES THIS BREAK THE WALL?

The theory track said the 6j-symbol signs kill the argument. But the
character expansion for ⟨Tr(W)⟩ doesn't involve 6j symbols — it involves
SCHUR ORTHOGONALITY (which gives 1/d_j > 0). The 6j symbols arise for
DISCONNECTED Wilson loop expectations ⟨Tr(W₁) Tr(W₂)⟩, not for single
connected loops ⟨Tr(W)⟩.

**The gradient correlation involves SINGLE CONNECTED Wilson loops.**
**The 6j wall applies to DISCONNECTED loop products.**
**These are DIFFERENT quantities. The wall doesn't apply here.**

## 035. POTENTIAL BREAKTHROUGH: Wilson loop positivity for connected loops.
## Character expansion: every term ≥ 0, j=0 gives 1.
## Gradient correlation = sum of positive × ⟨Tr(connected loop)⟩ > 0.
## This does NOT hit the 6j wall (which is for disconnected products).
## If correct: Langevin coupling → (5.15) → confinement → mass gap.
## NEEDS RIGOROUS VERIFICATION BY theory track.
