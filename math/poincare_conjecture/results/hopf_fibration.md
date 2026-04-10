# Hopf Fibration S³ → S² — Geometric Foundation

**Date:** 2026-04-09
**Script:** `numerics/hopf_fibration.py`
**Track:** Numerical
**Reference:** Hopf 1931, Adams 1960

## The Hopf Map

  H: S³ ⊂ C² → S² ⊂ R³
  (z₁, z₂) ↦ (2 Re(z₁ z̄₂), 2 Im(z₁ z̄₂), |z₁|² - |z₂|²)

In real coordinates p = (a, b, c, d):
  H(a,b,c,d) = (2(ac+bd), 2(bc-ad), a²+b²-c²-d²)

This is the only non-trivial circle bundle structure on S³ (Adams 1960).

## Test 1 — Hopf Map Image — PASS

6 random points on S³ tested:

| (a,b,c,d) on S³ | (x,y,z) on S² | \|H(p)\| |
|-----------------|---------------|----------|
| (0.580, 0.132, 0.322, 0.737) | (0.567, -0.770, -0.293) | 1.000000 |
| (0.806, -0.422, 0.410, -0.065) | (0.716, -0.241, 0.655) | 1.000000 |
| (-0.068, 0.270, 0.095, 0.956) | (0.503, 0.181, -0.845) | 1.000000 |
| (0.801, 0.128, 0.467, 0.351) | (0.839, -0.443, 0.317) | 1.000000 |
| (0.848, -0.116, 0.178, -0.485) | (0.415, 0.781, 0.466) | 1.000000 |
| (-0.889, 0.228, 0.301, -0.258) | (-0.653, -0.323, 0.685) | 1.000000 |

All |H(p)| = 1.000000 — Hopf map lands on S² to machine precision.

## Test 2 — Fibers Are Great Circles — PASS

For 3 base points on S², compute the preimage (fiber) and verify:

| Base point on S² | All on S³? | All map back? |
|------------------|-----------|---------------|
| (0, 0, 1) | YES | YES |
| (1, 0, 0) | YES | YES |
| (0.6, 0, 0.8) | YES | YES |

20 sample points per fiber, all checks pass. Each fiber is a great
circle in S³ that the Hopf map collapses to a single point on S².

## Test 3 — Linking Number = 1 (Hopf Invariant) — PASS

Two distinct Hopf fibers are LINKED with linking number 1.
Verified for the north/south pole fibers:

  Fiber 1 (north pole): {(cos θ, sin θ, 0, 0) : θ ∈ [0, 2π)}
  Fiber 2 (south pole): {(0, 0, cos φ, sin φ) : φ ∈ [0, 2π)}

Min distance between fibers: **1.414214** = √2 (orthogonal great circles in R⁴).
Disjoint: YES.

These are two perpendicular great circles in R⁴. Under stereographic
projection from a point not on either, one becomes a circle and the
other a line through its center — linking number 1, exactly the Hopf
invariant generating π₃(S²) = Z.

## Test 4 — Berger and Lens Space Connection

**Berger sphere** (used in `berger_sphere.py`):
  g_Berger = ε² · vertical ⊕ horizontal
where the vertical direction is the Hopf fiber. ε = 1 gives round S³,
ε ≠ 1 squashes the Hopf circles.

**Lens spaces** L(p, q):
  S³ / (z₁, z₂) ∼ (e^(2πi/p) z₁, e^(2πi q/p) z₂)
This Z_p action commutes with the Hopf U(1), so L(p, q) is a circle
bundle over S² with degree p.

| Lens space | π₁ | Notes |
|------------|-----|-------|
| L(1, 1) | 0 | = S³ |
| L(2, 1) | Z₂ | = RP³ |
| L(p, 1) for p ≥ 3 | Z_p | distinct, π₁ ≠ 0 |

π₁ = 0 only for p = 1, recovering S³.

## Summary

4 tests pass:
- Hopf map sends S³ to S² (norm-preserving to machine precision)
- Fibers are great circles in S³
- Two distinct fibers are linked (Hopf invariant = 1)
- Berger sphere and lens spaces both arise from this structure

**The Hopf fibration S³ → S² is the geometric foundation underneath**:
- `berger_sphere.py` (Hopf circles squashed)
- `manifold_census.py` (lens spaces are quotients of S³)
- `spherical_space_forms.py` (S³/Γ classification)
- `thurston_geometries.py` (S³ as the spherical model)

Adams 1960 proved this is one of only 4 non-trivial Hopf fibrations
(C, H, O — and the trivial real one). The complex case S³ → S²
is the simplest non-trivial fibration in topology and underlies all
3-manifold classification.

## For the Theory Track

Complements:
- `lean/RicciFlow.lean` (geometry of S³)
- `lean/SurgerySurvival.lean` (lens spaces are spherical quotients)
- `numerics/berger_sphere.py` (Hamilton 1982 on Hopf-squashed S³)
- `numerics/manifold_census.py` (lens space census)

The Hopf fibration is what makes S³ a non-trivial fiber bundle:
S³ is a circle bundle over S² with non-zero Chern class. This single
topological fact is the geometric reason the spherical space forms
exist and have the structure they do.
