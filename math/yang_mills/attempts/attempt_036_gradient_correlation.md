# Attempt 036 — The Gradient Correlation: Explicit Computation

**Date**: 2026-04-07
**Phase**: 4 (Beyond the Wall)
**Track**: theory (Theory)

## The Question (from attempt_034)

Does E_per[⟨∇O, ∇ΔS⟩] ≥ 0 on SU(2)^|E|?

Where:
- O = Σ_P w_P Tr(U_P), w_P > 0 (coupling response)
- ΔS = 2 Σ_{Q∈Σ} Σ_{j half-int} d_j c_j χ_j(U_Q) (surface vortex cost)
- ∇ means gradient with respect to link variables U_e ∈ SU(2)
- E_per means expectation under the periodic Wilson measure

## Integration by Parts

On a compact Riemannian manifold (SU(2)^|E| with product metric), the
Langevin generator L satisfies:

  E_μ[f · Lg] = -E_μ[⟨∇f, ∇g⟩]

where Lf = Δf + ⟨∇S, ∇f⟩ (the drift-Laplacian operator).

So: E_per[⟨∇O, ∇ΔS⟩] = -E_per[O · L(ΔS)]
                        = -E_per[O · (ΔΔS + ⟨∇S_per, ∇ΔS⟩)]

## What is L(ΔS)?

ΔS = 2 Σ_{Q∈Σ} Σ_{j half-int} d_j c_j χ_j(U_Q)

L(ΔS) = Δ(ΔS) + ⟨∇S_per, ∇(ΔS)⟩

### Term 1: Δ(ΔS) — the Laplacian on SU(2)

The Laplacian of χ_j(U_P) with respect to the link variables in P.
For SU(2): the Casimir eigenvalue is j(j+1) for spin j.

Δ_e χ_j(U_P) = -j(j+1) · χ_j(U_P)  (if e ∈ P, Laplacian on one link)

Wait — this needs care. U_P = U_{e₁}U_{e₂}U_{e₃}†U_{e₄}†.
The Laplacian with respect to e₁:

Δ_{e₁} Tr(U_{e₁} · staple) = Δ_{SU(2)} [U ↦ Tr(U · staple)]

For f(U) = Tr(U · M) on SU(2): Δf = -C₂ · f where C₂ = 3/4 for
the fundamental (j=1/2) representation. More generally for spin j:
Δ χ_j(U · M) involves the Casimir j(j+1).

So: Δ_{e₁} χ_j(U_P) = -j(j+1) · χ_j(U_P) (for each link in P)

Since P has 4 links: Δ χ_j(U_P) = -4·j(j+1)·χ_j(U_P)
(the Laplacian from all 4 links, assuming independence — but links
are shared between plaquettes, so this overcounts.)

Actually, the Laplacian is with respect to ALL links simultaneously:
Δ = Σ_e Δ_e. For a plaquette P involving links {e₁,...,e₄}:

Δ χ_j(U_P) = Σ_{e∈P} Δ_e χ_j(U_P) = Σ_{e∈P} (-j(j+1)) χ_j(U_P) = -4j(j+1) χ_j(U_P)

But this is only correct if χ_j(U_P) depends on each link e ∈ P through
a SINGLE matrix element. For the plaquette trace Tr(U_{e₁}U_{e₂}U_{e₃}†U_{e₄}†),
the Laplacian with respect to e₁ is:

Δ_{e₁} Tr(U_{e₁} · staple_{e₁}) = Σ_{a} ∂²/∂θ_a² Tr(e^{iθ_a T_a} U_{e₁} · staple)

At U_{e₁} = identity: this gives -C₂(j) · Tr(staple) where j is the
representation. But at general U_{e₁}, it's more complex.

This computation is getting involved. Let me simplify.

## A Simpler Route: The Dirichlet Form

Instead of computing L(ΔS) explicitly, use the fact that:

E[⟨∇O, ∇ΔS⟩] = Σ_e E[⟨∇_e O, ∇_e ΔS⟩]

Each term involves the gradient of O and ΔS with respect to a single link e.

For link e: ∇_e O = Σ_{P∋e} w_P · ∇_e Tr(U_P) = Σ_{P∋e} w_P · staple_P(e)
            ∇_e ΔS = 2 Σ_{Q∈Σ, Q∋e} Σ_{j h.i.} d_j c_j · ∇_e χ_j(U_Q)

The inner product: ⟨∇_e O, ∇_e ΔS⟩ = Σ_{P∋e, Q∈Σ∩e} w_P · 2d_j c_j · ⟨staple_P(e), ∇_e χ_j(U_Q)⟩

**For links NOT touching Σ**: ∇_e ΔS = 0 (ΔS only involves Σ-plaquettes).
So these links contribute 0.

**For links ON Σ** (touching at least one Σ-plaquette):

⟨staple_P(e), ∇_e χ_j(U_Q)⟩ = Tr(staple_P(e)† · ∇_e χ_j(U_Q))

This is a product of staples — essentially a LARGER Wilson loop.

## The Key Insight: Locality

Only links touching Σ contribute to E[⟨∇O, ∇ΔS⟩]. The number of such
links is O(|Σ| · coordination) — proportional to the surface area, not
the volume.

**At strong coupling**: each term is O(c_j) and POSITIVE at leading order
(the staple products are positive in the cluster expansion).

**At weak coupling**: the staples ≈ I, so the inner products ≈ d_j > 0.
The leading term is:

E[⟨∇O, ∇ΔS⟩] ≈ Σ_{e∈Σ} Σ_{P∋e} w_P · 2c_{1/2} · ⟨I, I⟩ = Σ_{e∈Σ} (stuff) · 2c_{1/2} · 2

This is POSITIVE.

**At intermediate coupling**: the expectation is a sum of Wilson-loop-like
quantities. These are ALWAYS positive for the periodic measure (they're
traces of products of unitary matrices, and the Wilson measure gives
positive expectation to traces of contractible loops).

## Wait — Is This Actually True?

⟨Tr(W)⟩_per > 0 for any CONTRACTIBLE Wilson loop W? Not necessarily.
For large loops at strong coupling, ⟨Tr(W)⟩ ~ exp(-σ·Area) which is
positive but exponentially small.

The staple products here are NOT contractible loops in general. They
involve links from plaquettes P (not on Σ) and Q (on Σ). The combined
path may cross Σ and be non-contractible.

For CONTRACTIBLE loops: ⟨Tr(W)⟩ ≥ 0 by... hmm, is this even true?
⟨Tr(U_P)⟩ = ⟨χ_{1/2}(U_P)⟩ > 0 at all β > 0 (by the positivity of the
leading character expansion coefficient). But for larger loops, the
expectation involves products of c_j from each plaquette in the
minimal surface, and at strong coupling these decay exponentially.

The SIGN is positive (all c_j > 0, all contributions from the character
expansion are products of positive terms). So yes: ⟨Tr(W)⟩_per > 0
for contractible loops W, at any β > 0.

## The Argument (Condensed)

1. E[⟨∇O, ∇ΔS⟩] = Σ_{e∈Σ-links} (terms involving staple-staple products)

2. Each term is a Wilson-loop-like expectation under the periodic measure

3. Under the periodic measure (all c_j > 0): these expectations are POSITIVE
   (character expansion: each contribution is a product of positive c_j values)

4. Sum of positive terms = positive

5. Therefore E[⟨∇O, ∇ΔS⟩] > 0

6. Therefore d/dt E[O^{per} - O^{anti}] > 0 from any shared starting point

7. Therefore Δ(∞) = ⟨O⟩_per - ⟨O⟩_anti > 0

8. Therefore (5.15) holds

## Critical Check: Step 3

"Wilson-loop-like expectations are positive under the periodic measure."

This uses the same spectral positivity argument from attempt_022: the
connected correlator of any gauge-invariant observable with itself is
≥ 0 (Lehmann representation). But here we need the FULL expectation
(not just the connected part) to be positive.

⟨Tr(W)⟩_per = ⟨Ω|Tr(W)|Ω⟩ (vacuum expectation of Wilson loop operator)

Is this always positive? For the TRIVIAL representation (j=0): yes, the
vacuum expectation of the identity loop is 1. For the FUNDAMENTAL (j=1/2):

⟨Tr(W)⟩ = Σ_n ⟨Ω|Tr(W)|n⟩ = ⟨Ω|Tr(W)|Ω⟩ + Σ_{n≥1} ⟨Ω|Tr(W)|n⟩

This includes excited-state contributions. The vacuum matrix element
⟨Ω|Tr(W)|Ω⟩ is positive (vacuum is the ground state, maximally ordered).
But excited-state contributions could have either sign.

**In the character expansion**: ⟨Tr(W)⟩ = c_{1/2}^{Area(W)} × (positive combinatorial)
for a planar loop W. Since c_{1/2} > 0, this is positive. ✓

For non-planar loops: the character expansion is more complex but still
involves products of c_j ≥ 0. The combinatorial factors (from link integrals)
are sums of products of Clebsch-Gordan coefficients, which CAN be negative.

**So Step 3 is NOT obviously true for non-planar loops.**

## Revised Assessment

The gradient correlation E[⟨∇O, ∇ΔS⟩] involves Wilson-loop-like expectations
that are NOT guaranteed positive for non-planar configurations.

The same 6j-symbol sign issue that killed the FKG approach (attempt_020)
reappears here. The Langevin coupling reduces to the SAME algebraic
question: are certain products of SU(2) recoupling coefficients positive?

## Result

The Langevin coupling approach (attempt_034) reduces to the SAME wall,
viewed from a different angle. The gradient correlation E[⟨∇O, ∇ΔS⟩] ≥ 0
requires positivity of Wilson-loop-like expectations involving non-planar paths.
This positivity fails in general (6j-symbols have mixed signs).

The wall is the wall, regardless of approach:
- MK decimation: local control vs global property (attempt_032)
- Cluster expansion: convergence regime limited (attempt_028, Step 7)
- FKG: not a distributive lattice (attempt_020)
- Langevin coupling: 6j-symbol signs (this attempt)

**All roads lead to the same obstacle: the non-abelian recoupling coefficients
of SU(2) have mixed signs, preventing any global positivity argument.**

This IS the wall. It's not a technical issue — it's a structural feature
of non-abelian gauge theory.
