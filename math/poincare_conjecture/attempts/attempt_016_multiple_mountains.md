# Attempt 016 — Multiple Mountains for Hodge

**Date**: 2026-04-07
**Phase**: 2 (Multiple Mountains doctrine)
**Instance**: Even (Theory)

## Current: One Mountain (Algebraic Geometry)

Hodge lives on ONE mountain: algebraic geometry. Every approach
(Grothendieck, motives, Chow groups, Lefschetz) is algebraic.
The wall: "no exponential sequence for p ≥ 2."

## The Other Mountains

### M2: DIFFERENTIAL GEOMETRY (the curvature mountain)
- Key insight: Hodge classes are HARMONIC FORMS (Δω = 0).
  Algebraic cycles are CALIBRATED submanifolds (volume-minimizing).
  Hodge conjecture ⟺ every harmonic (p,p)-form is the current
  of a calibrated submanifold.
- Connection: Harvey-Lawson theory of calibrated geometries.
  The associative and coassociative calibrations produce
  algebraic cycles from differential geometry.

### M3: PHYSICS (the string theory mountain)
- Key insight: Hodge classes on Calabi-Yau manifolds correspond to
  MASSLESS STATES in the string theory compactification. Algebraic
  cycles correspond to D-BRANES. Hodge ⟺ every massless state
  wraps a brane.
- Mirror symmetry: Hodge classes on X ↔ curve counts on X̌.
  This COMPUTES Hodge classes from enumerative geometry.

### M4: CATEGORY THEORY (the derived mountain)
- Key insight: the derived category D^b(X) determines the Hodge
  structure (Orlov's representability). Chern characters of objects
  in D^b(X) give algebraic classes. Hodge ⟺ Chern characters SPAN
  the Hodge lattice.
- The Hochschild-Kostant-Rosenberg theorem connects HH*(X) to
  Hodge cohomology. Deformation quantization might fill the gap.

## The Cheapest Intervention

**M3 (physics/mirror symmetry)**: For Calabi-Yau manifolds, mirror symmetry
COMPUTES the Hodge classes as Gromov-Witten invariants (curve counts).
If every Hodge class has a mirror-dual curve count, and curve counts
are algebraic (they're integers!), then Hodge follows for CY manifolds.

This is the "cheapest" because:
1. Mirror symmetry is already PROVED for many CY families (Givental, Lian-Liu-Yau)
2. Gromov-Witten invariants are COMPUTABLE
3. The connection Hodge class ↔ GW invariant is EXPLICIT for CY3s
4. It avoids the "exponential sequence" wall entirely

## Result

Hodge goes from 1 mountain to 4. The cheapest intervention is mirror
symmetry for Calabi-Yau manifolds: compute Hodge classes as curve counts
on the mirror. This is a DIFFERENT mountain with DIFFERENT tools that
avoids the p ≥ 2 wall (no exponential sequence needed — use enumerative
geometry instead).
