# Attempt 065 — The Key Combinatorial Lemma of the Strong-Coupling Closure

**Date**: 2026-04-15
**Phase**: 5 (Isolating the structural fact for future Lean formalization)
**Track**: combinatorial

## Purpose

The strong-coupling closure in attempt_064 rests on a single combinatorial
fact about the (0,1,2) 3-cube in d=4. This document states that fact as
a stand-alone lemma, free of the character-expansion context, so it can
be formalized in Lean independently.

## The lemma

**Lemma (3-cube boundary parity).** Let d ≥ 3 and let P, Q be two unit
plaquettes on Z^d sharing exactly one edge. Then:

1. There exists exactly one 3-cube C ⊂ Z^d such that both P and Q are
   faces of C.

2. In the consistently oriented boundary ∂C (as a 2-chain with
   integer coefficients), the plaquettes P and Q appear with
   OPPOSITE SIGNS.

3. As a consequence, the 2-chain {P + Q} (with both +1 coefficients)
   cannot be modified by adding ±∂C to produce another ±1-coefficient
   2-chain with the same boundary.

4. Conversely, the 2-chain {P − Q} (with opposite ±1 coefficients) CAN
   be modified by adding ±∂C to produce a 4-plaquette ±1-coefficient
   2-chain with the same boundary.

## Proof sketch

**(1) Uniqueness of C**. P is a unit plaquette in some plane (μ, ν) at
position x, and Q is a unit plaquette in plane (μ, λ) at position y,
sharing the edge (y, y + e_μ) = (x + ?, ?). Working out the geometry:
WLOG take P at origin in plane (0, 1) and Q at origin in plane (0, 2).
Then P's corners are {0, e₀, e₀+e₁, e₁}, Q's are {0, e₀, e₀+e₂, e₂}.
A 3-cube containing both must contain all six distinct corners
{0, e₀, e₁, e₂, e₀+e₁, e₀+e₂}, which forces C = [0, e₀+e₁+e₂] in plane
(0, 1, 2). Unique.

**(2) Opposite signs in ∂C**. The boundary of the 3-cube C = [0, e_A+e_B+e_C]
(in directions A=0, B=1, C=2) as an oriented 2-chain is

  ∂C = (A,B)_{C=0} − (A,B)_{C=1} − (A,C)_{B=0} + (A,C)_{B=1}
                                 + (B,C)_{A=0} − (B,C)_{A=1}

where (μ, ν)_{λ=t} denotes the unit plaquette in plane (μ, ν) at the
slice λ = t. The alternating signs are forced by ∂² = 0 (the outer
boundary of the 3-cube boundary must vanish, which requires the signs
to cancel at every shared edge).

Identifying:
- P = (A, B)_{C=0}, coefficient +1
- Q = (A, C)_{B=0}, coefficient −1

These are on opposite-sign slots (one with + and one with − in the
alternating pattern). **They have opposite signs.**

**(3) No area-4 ±1 chain for {P + Q}**. Any alternative 2-chain S with
∂S = ∂(P + Q) differs from (P + Q) by a 2-cycle Z, i.e., S = (P + Q) + Z
where ∂Z = 0. On Z^d the smallest non-trivial 2-cycle is the boundary
of a single 3-cube. For |S| = 4 we need |Z| = {2, 8, 14, ...} and
specifically the "size-2 2-cycle" interpretation: Z = ±∂C for some
3-cube C whose boundary cancels two of the three plaquettes in
(P + Q). Since |Z| = 0 (Z is a cycle, always boundary-free, but |Z| refers
to non-zero support).

Actually the argument: for S = (P + Q) ± ∂C to have |support| = 4 and
coefficients in {±1}, we need ∂C to cancel TWO plaquettes of (P + Q)
(there are 2: P and Q). In ∂C, P has coefficient +1 and Q has −1.
- (P + Q) + ∂C: cancels... nothing cleanly. P gets coefficient 2; Q
  gets coefficient 0. Result is 2P + (4 other faces) with mixed
  coefficients. Not ±1.
- (P + Q) − ∂C: P gets coefficient 0; Q gets coefficient 2. Not ±1.

Either way, one of P or Q gets coefficient 2. So no ±1-coefficient
area-4 chain exists.

**(4) Chair case {P − Q}**. Now P has coefficient +1 and Q has −1 in
(P − Q). Subtracting ∂C:
- (P − Q) − ∂C: P gets coefficient 0; Q gets coefficient −1 − (−1) = 0.
  Both cancel. Remainder: the four other faces of C with sign-flipped
  coefficients, which is a ±1-coefficient chain. |support| = 4.

This gives the area-4 alternative surface for the chair that attempt_060
found.

## Generalization to d > 4

The lemma holds for any d ≥ 3. The unique 3-cube containing P and Q is
always in the 3-dimensional hyperplane spanned by the two planes
containing P and Q. The sign structure of ∂C depends only on the
orientation convention within that hyperplane.

In d = 4, only one 3-cube works. In d = 3, still only one (the full
cube). In d ≥ 5, still only one (the 3-cube in the relevant 3-plane).

## What this buys us

The lemma together with the strong-coupling character-expansion rules
gives the explicit expansion coefficients:

- ⟨Tr(chair)⟩ = c²/2 + c⁴/32 + O(c⁶)  (pure j=1/2)
- ⟨Tr(P)·Tr(Q)⟩ = c² + 0·c⁴ + O(c⁶)  (pure j=1/2)
- GC = c⁴/64 + O(c⁶)  (positive)

rigorously in the pure j=1/2 sector.

## Lean formalization sketch

The lemma could be formalized as:

```lean
-- Assumed: Plaquette (d : ℕ) is a type; Cube3 (d : ℕ) is a type.
-- boundary : Cube3 d → Plaquette d → ℤ   (coefficient of plaquette in ∂cube)

-- Define: plaquettes P, Q "share one edge" ⟹ they're in planes (μ,ν), (μ,λ) with ν≠λ

theorem three_cube_contains_shared_plaquettes_uniquely
    (d : ℕ) (hd : d ≥ 3) (P Q : Plaquette d) (h : shareOneEdge P Q) :
    ∃! C : Cube3 d, boundary C P ≠ 0 ∧ boundary C Q ≠ 0 := ...

theorem three_cube_boundary_opposite_signs
    (d : ℕ) (hd : d ≥ 3) (P Q : Plaquette d) (h : shareOneEdge P Q)
    (C : Cube3 d) (hP : boundary C P ≠ 0) (hQ : boundary C Q ≠ 0) :
    boundary C P * boundary C Q = -1 := ...
    -- The product of their signs in ∂C is −1, i.e., opposite.

theorem no_area_four_chain_for_plaq_prod
    (d : ℕ) (hd : d ≥ 3) (P Q : Plaquette d) (h : shareOneEdge P Q) :
    ∀ (S : SignedPlaquetteChain d), (∂ S = ∂ P + ∂ Q) → (|support S| = 4) →
      (∃ p ∈ support S, |coefficient S p| ≥ 2) := ...
```

This is a natural target for a Lean file ym/lean/ThreeCubeBoundaryLemma.lean.
The proof uses the combinatorics of unit plaquettes and cubes on Z^d,
not SU(2) character theory — the physical content is purely geometric.

## Tag

065. The key combinatorial lemma underlying attempt_064's closure: the
unique 3-cube containing two adjacent plaquettes has them on
opposite-sign boundary faces. This is the structural reason GC > 0 at
c⁴ in the pure j=1/2 sector. Ready for Lean formalization (sketch
provided); independent of the character-expansion machinery.
