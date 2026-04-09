# Attempt 006 — Multiple Mountains: Surrounding the Rank ≥ 2 Gap

**Date**: 2026-04-07
**Phase**: 2 (Multiple Mountains doctrine)
**Instance**: Even (Theory)

## The One-Mountain Problem

BSD has ONE mountain: arithmetic geometry (Heegner points, Euler systems,
Iwasawa theory). Every tool produces ONE algebraic object. For rank ≥ 2,
you need TWO. Everyone pushes harder on the same mountain.

**Stop pushing. Find the other mountains.**

## Mountain 1: Arithmetic Geometry (current, stuck at rank 1)
- Tools: Heegner points, Gross-Zagier, Kolyvagin, Euler systems
- Wall: one point / one Euler system class → rank 1 max
- View of gap: "we need two independent points from L''(E,1)"

## Mountain 2: ANALYTIC NUMBER THEORY (the moments mountain)
- Tools: moments of L-functions, subconvexity, multiple Dirichlet series
- Key insight: L''(E,1) is the SECOND moment of the L-function at s=1.
  Moments of L-functions are studied via MULTIPLE DIRICHLET SERIES.
- The gap from THIS summit: "we can compute L''(E,1) but can't connect
  it to algebraic objects"

**What M2 reveals that M1 can't see**:
- The Keating-Snaith moment conjectures predict EXACT formulas for
  ∫ L(E,1)^k dE (average over curve families). For k = 2: this involves
  PAIRS of curves, not single curves.
- The second moment naturally produces TWO-POINT correlations.
- Maybe the rank-2 points come from PAIRS of curves, not one curve.

**Underground connection M1↔M2**: The Gross-Zagier formula IS a first-moment
result (L' = height of ONE point). A SECOND-moment Gross-Zagier would give
L'' = regulator of TWO points. This is the "higher Gross-Zagier" everyone wants.

## Mountain 3: TOPOLOGY / GEOMETRY (the Selmer mountain)
- Tools: arithmetic topology, 3-manifold analogy, knot theory
- Key insight: Mazur's analogy: number fields ↔ 3-manifolds,
  primes ↔ knots, Selmer groups ↔ linking numbers
- The gap from THIS summit: "the Selmer group for rank 2 has a
  GEOMETRIC interpretation as linking in a 3-manifold"

**What M3 reveals**:
- A rank-2 Selmer group means TWO independent elements in H¹(Q, E[p]).
  In the arithmetic topology analogy, these are TWO linked knots.
- The linking number = height pairing = regulator entry.
- Maybe the rank-2 construction is TOPOLOGICAL: construct the two
  Selmer elements from the linking structure of primes.

**Underground connection M1↔M3**: Kolyvagin's Euler system produces Selmer
elements from Heegner points. The TOPOLOGY tells you where to look for
the SECOND Selmer element — it's linked to the first.

## Mountain 4: PHYSICS (the string theory mountain)
- Tools: string theory, mirror symmetry, Calabi-Yau geometry
- Key insight: elliptic curves arise as fibers of Calabi-Yau manifolds.
  The L-function encodes the PERIODS of the CY. The rank counts
  RATIONAL curves in the mirror.
- The gap from THIS summit: "rank 2 means two independent rational
  curves on the mirror CY"

**What M4 reveals**:
- Mirror symmetry COUNTS rational curves (Gromov-Witten invariants).
  These are EXPLICITLY computable for many CY manifolds.
- If the elliptic curve E is a fiber of a CY3 X: rank(E) relates to
  the number of independent rational curves on the mirror X̌.
- Maybe the rank-2 points come from MIRROR SYMMETRY: the two points
  on E correspond to two rational curves on X̌, which are constructible.

**This is speculative but has CONCRETE instances**: for CM curves,
the mirror CY has explicit rational curves that give rational points on E.

## Mountain 5: COMPUTATION (the statistical mountain)
- Tools: LMFDB, machine learning, pattern recognition
- Key insight: there are THOUSANDS of rank-2 curves in the LMFDB.
  Each has explicit generators found by descent + search.
- The gap from THIS summit: "how were the generators FOUND? Not by
  Heegner points — by SEARCH. What structure does the search reveal?"

**What M5 reveals**:
- The generators of rank-2 curves are typically SMALL (low height).
  This suggests a structure that makes them findable — not random.
- Descent methods (2-descent, p-descent) find generators by solving
  specific Diophantine equations. The FORM of these equations might
  reveal the construction that M1 is missing.
- Pattern: many rank-2 generators come from INTERSECTIONS of two
  auxiliary curves with the elliptic curve. This is a GEOMETRIC
  construction, not an L-function construction.

## The Surrounded Gap

From all 5 mountains:

> **The rank-2 points come from PAIRS — pairs of Heegner points
> (M1, via two quadratic fields), pairs of L-function moments (M2),
> pairs of linked Selmer elements (M3), pairs of rational curves on
> the mirror CY (M4), or pairs found by descent (M5).**

The common theme: RANK 2 = PAIRS. The construction must naturally
produce PAIRS, not single objects.

**Candidate construction** (combining M1 + M2 + M3):

For an elliptic curve E/Q of rank 2:
1. Choose TWO imaginary quadratic fields K₁, K₂ (split at the same primes)
2. Heegner point y_{K₁} ∈ E(K₁), y_{K₂} ∈ E(K₂)
3. Project to E(Q): P₁ = Tr_{K₁/Q}(y_{K₁}), P₂ = Tr_{K₂/Q}(y_{K₂})
4. If P₁, P₂ are INDEPENDENT: rank ≥ 2 established

**Why this might fail**: the projections Tr(y_K) might be linearly dependent.
But if K₁, K₂ are chosen with INDEPENDENT discriminants, the Gross-Zagier
formula would give:
  L'(E/K₁, 1) = c₁ · ĥ(y_{K₁})
  L'(E/K₂, 1) = c₂ · ĥ(y_{K₂})

For the PROJECTIONS to be independent, we'd need a formula like:
  L''(E, 1) ~ ĥ(P₁)·ĥ(P₂) - ⟨P₁, P₂⟩²  (a REGULATOR)

This is the SECOND-ORDER Gross-Zagier formula that M2 says should exist.

## The Underground Connections

```
M1 (Arithmetic)  ←→  M2 (Analytic)
  Gross-Zagier         Moments of L-functions
  One point            Pairs of curves
       ↕                    ↕
M3 (Topology)    ←→  M5 (Computation)
  Selmer linking       Descent finds pairs
  Two linked knots     Generator structure
       ↕
M4 (Physics)
  Mirror symmetry
  Two rational curves on mirror CY
```

## Result

BSD went from 1 mountain (arithmetic geometry) to 5. The gap — "no
rank-2 construction" — is now visible from 5 angles:

| Mountain | The rank-2 construction looks like |
|----------|----------------------------------|
| M1 | Two Heegner points from independent quadratic fields |
| M2 | Second-order Gross-Zagier from L'' |
| M3 | Two linked Selmer elements |
| M4 | Two rational curves on the mirror CY |
| M5 | Two generators from descent structure |

The COMMON STRUCTURE: pairs. The construction must naturally produce
pairs. The "cheapest intervention" (from the T1DM analogy): look at
how DESCENT finds generators (M5), then formalize that as a
construction (connect to M1 or M3).

## For Session 2

1. Study descent for rank-2 curves: what equations do the generators satisfy?
2. Study the Mazur arithmetic topology: what does "linking" look like for Selmer?
3. Compute: for 100 rank-2 curves, HOW were the generators found? (M5)
4. Study: do two Heegner points from different K ever give independent Q-points? (M1)
5. Study: second-order Gross-Zagier formulas in the literature (M2)
