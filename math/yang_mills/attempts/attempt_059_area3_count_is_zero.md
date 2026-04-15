# Attempt 059 — The Area-3 Surface Count Bounded by the Chair Is Zero

**Date**: 2026-04-15
**Phase**: 5 (Audit of attempt_050's O(c³) claim)
**Track**: numerical + combinatorial

## Empirical finding

`numerics/area3_chair_enumeration.py` enumerates all 3-plaquette signed
2-chains with support on plaquettes in a radius-2 box around the chair
(34-plaquette pool, 5,984 unordered 3-subsets × 8 sign patterns = 47,872
chains tested) and counts those with signed boundary equal to ±(chair
boundary).

**Result: 0 chains with boundary = ±chair.**

## Topological reason the count is zero

The chair is a 2-chain with ∂ = (chair Wilson loop). Any other 2-chain
C with ∂C = chair Wilson loop satisfies

  C − chair = Z,     ∂Z = 0

i.e. Z is a closed 2-chain (2-cycle) on Z⁴. The smallest nontrivial
2-cycle on a hypercubic lattice is the boundary of a single 3-cube,
which is a sum of 6 plaquettes (with alternating signs summing to 0 at
each edge). So any alternative surface differs from the chair by 0, 6,
12, ... plaquettes. Alternative |C| ∈ {2, 8, 14, 20, ...}.

**There is no 3-plaquette 2-chain with ∂ = chair.**

(The general statement: the Euler characteristic of a lattice 2-chain
bounded by a fixed 1-chain has a fixed parity modulo 2 on the hypercubic
lattice, and this parity picks out even area increments.)

## Consequence for attempt_050

attempt_050 argues:

  ⟨Tr(chair)⟩ = c² + 5c³ + O(c⁴)  (informally)

with the 5c³ coming from "~10 area-3 tilings, each contributing c³/2".
This is incorrect as stated: **there are no area-3 surfaces bounded by
the chair** in the pure-geometric counting sense. The correct statement
at strong coupling is:

  ⟨Tr(chair)⟩ = c² + 0·c³ + O(c⁴)

The O(c⁴) term comes from area-4 surfaces (and higher) bounded by the
chair. The smallest alternatives to the chair have area 2+6 = 8 from
adding a 3-cube boundary. But surfaces with some plaquette counted
twice can give lower areas — a "two-sheet" construction with overlapping
plaquettes contributes at area 4 (= 2 + 2 via doubled plaquettes).

## What this does to the GC > 0 proof

attempt_050's strong-coupling argument was:
  GC = (1/2)⟨Tr(chair)⟩ - (1/4)⟨Tr(P)⟩⟨Tr(Q)⟩
     = (c²/2) + 5c³/2 + O(c⁴) − c² − (separate corrections)
     = 0 + 5c³/2 + O(c⁴)  [at leading order beyond c²]

This now collapses to:
  GC = 0 + 0 · c³ + O(c⁴)  [at leading order beyond c²]

The sign of GC at strong coupling is determined by the c⁴ term — and
attempt_050 does not analyze c⁴. The "PROVEN at strong coupling" claim
in pattern_061 and attempt_053 is an overstatement.

The numerical evidence (GC > 0 observed at β ∈ [2.0, 8.0] across 1500+
MC measurements) still stands. What is shown to be incorrect is the
**analytical derivation** of the sign via area-3 surface counting.

## Where the informal argument went astray

attempt_050 wrote:

> "At area A_min + 1 = 3: add one plaquette to the minimal 2-plaquette
>  surface. The added plaquette shares at least one link with the
>  existing surface."

This conflates "surface containing the chair as a subsurface" with
"surface bounded by the chair." Adding a plaquette to the chair gives a
different boundary (the added plaquette's free edges become part of
the new boundary). It does NOT give a 3-plaquette surface bounded by
the chair's original 6 edges.

## The same argument applies to the plaquette Wilson loop

A single plaquette P has 4-edge boundary ∂P. Any alternative 2-chain C
with ∂C = ∂P satisfies |C| − 1 ∈ 2Z for the same parity reason — the
smallest non-trivial 2-cycle (3-cube boundary, 6 plaquettes) has even
intersection with any fixed plaquette. So alternative surfaces bounded
by P have |C| ∈ {1, 7, 13, ...}.

**Consequence for the plaquette expectation in pure j=1/2 character
expansion**:

  ⟨Tr(P)⟩ = c + 0·c² + 0·c³ + 0·c⁴ + 0·c⁵ + 0·c⁶ + O(c⁷)

(The O(c⁷) term comes from P plus a 3-cube cover, a 7-plaquette surface.)

attempt_050 implicitly assumed ⟨Tr(P)⟩ = c + O(c³), with the c³ from
"independent corrections". Under pure-rep counting this is wrong. The
plaquette product at strong coupling is

  ⟨Tr(P)⟩⟨Tr(Q)⟩ = c² + c·O(c⁷) + O(c¹⁴) = c² + O(c⁸)

and likewise ⟨Tr(chair)⟩ = c² + O(c⁸). Both sides of GC agree to O(c⁸).
The "leading correction" that attempt_050 tried to compute doesn't exist
in the pure-j=1/2 sector.

**Where the real O(c³) or O(c⁴) corrections come from**: higher-
representation contributions. A plaquette upgraded from j=1/2 to j=1
costs c_1/c_{1/2} ≈ c at strong coupling (since c_1 ∝ β²/32 and
c_{1/2} ∝ β/4, ratio ≈ β/8 ≈ c/2). So a 2-plaquette surface with one
plaquette upgraded to j=1 contributes c · c² = c³ (area cost) · c_1
(rep cost) — a mixed-rep correction at O(c³) or thereabouts, depending
on Schur factors at the shared edge.

This is the correct scaffold for the strong-coupling analysis, and it
requires enumerating **representation-weighted** surfaces, not
geometric area-counted surfaces. attempt_050's pure-area argument is
the wrong object.

## Recommendation

- Retract the "5c³ at area 3" claim in attempt_050.
- Analyze the actual leading nonzero correction to ⟨Tr(chair)⟩ −
  c²⟨Tr(P)⟩⟨Tr(Q)⟩/⟨Tr(P)²⟩ at O(c⁴). This requires enumerating
  area-4 surfaces bounded by the chair with the lattice parity
  constraint.
- Update THEWALL.md Option D section to reflect that the "strong
  coupling PROVEN" status is downgraded.

## Tag

059. Direct enumeration (34-plaquette pool, 47,872 signed 3-chains)
shows zero area-3 2-chains bounded by the chair. Lattice parity
argument confirms: alternative surfaces differ from chair by 6, 12, ...
plaquettes. attempt_050's "5c³" claim was based on conflating
"subsurface" with "alternative-bounding-surface" and does not apply.
The strong-coupling GC > 0 analytical derivation needs revision at c⁴
or higher.
