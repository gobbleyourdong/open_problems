# Attempt 060 — Correction to attempt_059: Area-4 Surfaces DO Exist

**Date**: 2026-04-15
**Phase**: 5 (Self-correction to attempt_059)
**Track**: numerical + combinatorial

## What attempt_059 got wrong

attempt_059 claimed "alternative surfaces bounded by the chair have
|C| ∈ {2, 8, 14, ...}" via a parity argument. That argument was flawed
because it did not account for the fact that both chair plaquettes P and
Q are themselves faces of the same 3-cube (the (0,1,2) unit 3-cube at
origin). When this 3-cube's boundary is added to the chair, BOTH P and Q
cancel simultaneously, leaving only the 4 other faces of the 3-cube.

## Direct verification

`area3_chair_enumeration.py` extended to area-4:

```
k=2: 2 chains bounded by ±chair (the chair itself, both orientations)
k=3: 0 chains bounded by ±chair
k=4: 2 chains bounded by ±chair  ← ATTEMPT_059 MISSED THESE
```

The two area-4 chains are the (0,1,2) 3-cube's 4 non-chair faces:
- plaquette (0,0,0,0) in plane (1,2)       [3-cube "front" face]
- plaquette (1,0,0,0) in plane (1,2)       [3-cube "back" face]
- plaquette (0,0,1,0) in plane (0,1)       [P shifted by e_2]
- plaquette (0,1,0,0) in plane (0,2)       [Q shifted by e_1]

with specific ±1 signs. The two sign patterns correspond to flipping the
3-cube's orientation. At radius=1 only the (0,1,2) 3-cube is captured;
at larger radius, analogous configurations involving (0,1,3) 3-cubes
give additional area-4 surfaces (the chair's P in (0,1) and Q in (0,2)
plane do NOT share a 3-cube with the (2,3) 3-cube so that case doesn't
contribute area-4).

## Corrected strong-coupling expansion

In the pure j=1/2 sector:

  ⟨Tr(chair)⟩ = c² + A₄ · c⁴ + A₆ · c⁶ + O(c⁸)

where A₄ is a nonzero coefficient from the area-4 surfaces (one per
shared 3-cube containing both P and Q; in d=4 there is 1 such 3-cube,
namely the (0,1,2) 3-cube — so 2 signed chains counted as ±1, but in the
character expansion they contribute the SAME sign because they differ
only by global orientation flip). The coefficient involves:

- 4 plaquettes × c^4 = c⁴ weight
- SU(2) Schur factors at each internal edge (6 internal edges in the
  4-plaquette 3-cube face set)
- Sign from the 3-cube orientation

Computing A₄ requires tracking the exact Schur/link factors. This is
within reach of direct character-expansion enumeration but was not done
in attempt_050 or attempt_059.

## Corrected statement about ⟨Tr(P)⟩

Similarly, ⟨Tr(P)⟩ in the pure j=1/2 sector has a nonzero c⁵ term from
the 5 non-P faces of any 3-cube containing P (each with P oriented so
the 3-cube boundary cancels P). For P in plane (0,1) at origin in d=4,
there are 4 such 3-cubes: (0,1,2) and (0,1,3), each at position 0 or at
one-unit-back in the extra direction. So:

  ⟨Tr(P)⟩ = c + B₅ · c⁵ + O(c⁷)

not c + O(c⁷) as attempt_059 claimed.

## The actual O(c³) coefficient of GC

In the pure j=1/2 sector:

  ⟨Tr(chair)⟩ − ⟨Tr(P)⟩⟨Tr(Q)⟩
    = [c² + A₄·c⁴ + ...] − [c + B₅·c⁵ + ...][c + B₅·c⁵ + ...]
    = c² + A₄·c⁴ − c² − 2·B₅·c⁶ + O(c⁸)
    = A₄·c⁴ − 2·B₅·c⁶ + O(c⁸)

So GC differs from zero at O(c⁴), with sign depending on A₄. **This is a
fourth-order effect, not third-order.** attempt_050's "leading 5c³
correction" claim was wrong by at least one order of magnitude in c.

The sign of A₄ is the new question. If A₄ > 0: GC > 0 at strong coupling
via pure j=1/2. If A₄ < 0: the pure j=1/2 sector gives GC < 0 at leading
nontrivial order, and higher-rep corrections would need to override.

## What remains

- Compute A₄ explicitly using SU(2) Schur factors. This is a 6-edge
  integration problem on the (0,1,2) 3-cube — tractable by hand.
- Repeat area-4 enumeration at larger radius to catch contributions from
  3-cubes in other direction triples.
- Re-run the area-3 enumeration with mixed-representation support to
  check if the "true" O(c³) correction exists there. That's a separate
  and harder enumeration.

## Correction to THEWALL.md

The annotation added in attempt_059 overstated the correction. The
correct statement is:
- attempt_050's specific "5c³ from area-3 surfaces" is incorrect (there
  are 0 area-3 signed 2-chains with the chair's boundary).
- The leading nontrivial correction to GC from pure j=1/2 surfaces
  appears at O(c⁴), from the (0,1,2) 3-cube's 4 non-chair faces.
- The sign at O(c⁴) has NOT been computed.

## Tag

060. Self-correction: area-4 surfaces bounded by the chair DO exist
(4 non-chair faces of the (0,1,2) 3-cube whose two "bottom" faces are
exactly P and Q). So ⟨Tr(chair)⟩ has a c⁴ term, not c⁸ as attempt_059
claimed. The correct leading nontrivial order for GC in pure j=1/2 is
c⁴, with unknown sign. attempt_050's c³ claim remains wrong. The
parity argument in attempt_059 required the SAME-3-cube alignment
exclusion that the chair geometry happens to satisfy.
