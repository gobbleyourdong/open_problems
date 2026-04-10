# Hopf Fibration Certificate

## Date: 2026-04-09
## Script: numerics/hopf_fibration.py

## CERTIFICATE

The Hopf fibration H: S³ → S² verified explicitly:

| Test | Verification | Result |
|------|--------------|--------|
| 1 | \|H(p)\| = 1 for 6 random p ∈ S³ | 1.000000 (exact) |
| 2 | Fibers project back via H for 3 base points | YES |
| 3 | North/south fibers disjoint, distance √2 | 1.414214 |
| 4 | Linking number = 1 (Hopf invariant) | qualitative argument |

## Key Numbers

  Hopf map: (a,b,c,d) ↦ (2(ac+bd), 2(bc-ad), a²+b²-c²-d²)
  Min distance between orthogonal fibers: √2 = 1.414214
  Hopf invariant (linking number): 1
  Berger family: g_ε with vertical/horizontal split, ε = 1 = round S³
  Lens space π₁: Z_p, simply connected only for p = 1

## Connections

The Hopf fibration is the geometric foundation underneath:
  - berger_sphere.py (Hamilton 1982 verification)
  - manifold_census.py (lens space census)
  - spherical_space_forms.py (S³/Γ classification)

Single topological fact: S³ is a non-trivial circle bundle over S²
with first Chern class generating H²(S²; Z) = Z. This is what gives
the spherical space forms their structure.

## Reproducibility

Dependencies: numpy. Runtime: < 1 second.
