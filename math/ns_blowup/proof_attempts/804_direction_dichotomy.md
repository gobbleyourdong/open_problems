---
source: DIRECTION DICHOTOMY — coherent vs incoherent vorticity near blowup
type: SPECULATIVE — untested but potentially powerful
file: 804
date: 2026-04-01
instance: MATHEMATICIAN (Opus)
---

## THE IDEA

Near a potential blowup, the vorticity direction ξ = ω/|ω| either:
(A) Varies slowly in space (coherent) → Constantin-Fefferman applies → regular
(B) Varies rapidly in space (incoherent) → stretching cancels → sub-Type I → regular

In either case: regularity. This is a DICHOTOMY argument.

## BRANCH A: COHERENT DIRECTION

Constantin-Fefferman 1993: if |∇ξ| ≤ C|ω|^{-1/2+ε} in the region
where |ω| > ||ω||∞/2, then the solution is regular.

For coherent vorticity (slowly varying direction): this condition is
satisfied. The vortex tubes have well-defined axis direction, and the
stretching is organized.

## BRANCH B: INCOHERENT DIRECTION

If ξ varies rapidly, the stretching integral ∫ω·Sω involves contributions
from different regions with different ω directions. The strain S at a point
is determined by the Biot-Savart integral over ALL ω, so rapidly varying ξ
creates cancellations in S that reduce the effective stretching.

Formally: ∫ω·Sω = ∫∫ K(x,y)·(ω(x)⊗ω(y)) dx dy (Biot-Savart kernel)

For incoherent ξ: the off-diagonal (x ≠ y) contributions oscillate due to
direction variation, producing cancellation. The diagonal (x ≈ y) contributions
are bounded by the Key Lemma.

## THE KEY LEMMA'S ROLE

The Key Lemma bounds the DIAGONAL contribution: at the vorticity max,
α < (√3/2)|ω|. This bounds the local (self-) stretching.

The off-diagonal contributions come from the non-local Biot-Savart interaction.
For incoherent ξ, these cancel. For coherent ξ, they add constructively, but
then Constantin-Fefferman applies.

## THE GAP

Neither branch is proven:
- Branch A: need to show SOME regularity criterion is satisfied for coherent ξ
  with the specific Key Lemma constant √3/2
- Branch B: need to QUANTIFY the cancellation from incoherent ξ and show
  it makes the stretching sub-Type-I

The dichotomy itself (every blowup candidate falls into A or B) needs proof.
The partition between "coherent" and "incoherent" must be made precise.

## CONNECTION TO DEPLETION OF NONLINEARITY

This dichotomy is essentially the depletion of nonlinearity conjecture
(Constantin 1994) repackaged. The conjecture says: near NS blowup, the
nonlinear stretching is depleted relative to the generic bound.

The Key Lemma PROVES depletion at the pointwise level: α < (√3/2)|ω|
instead of α ≤ |ω|. The gap is: does pointwise depletion at the max
imply GLOBAL depletion (integrated over space)?

## WHAT WOULD MAKE THIS WORK

1. A quantitative version of Constantin-Fefferman that uses the constant √3/2
2. A quantitative cancellation lemma for incoherent vorticity fields
3. A continuity argument showing the transition between A and B is smooth
   (no "critical" case that escapes both branches)

## 804. Dichotomy: coherent ξ → CF regularity, incoherent ξ → cancellation.
## Both branches need quantification. Related to depletion conjecture.
## The Key Lemma provides the pointwise bound; need to globalize.
