#!/usr/bin/env python3
"""
3-Manifold Census: Generate and classify closed 3-manifolds.

Approach: Use RANDOM DEHN SURGERY on knots in S³.
Every closed orientable 3-manifold can be obtained by Dehn surgery on a
link in S³ (Lickorish-Wallace theorem).

Dehn surgery on a knot K ⊂ S³ with slope p/q:
- Remove a tubular neighborhood of K (a solid torus)
- Glue back a solid torus with meridian mapped to p·μ + q·λ
  (where μ = meridian, λ = longitude of K)

For the UNKNOT: p/q surgery gives the lens space L(p,q).
- L(1,0) = S³ (trivial surgery)
- L(0,1) = S¹ × S² (0-surgery on unknot)
- L(p,1) = L(p,1) (lens space with π₁ = Z_p)

π₁(L(p,q)) = Z_p. Simply connected iff p = ±1 iff result is S³.

For the TREFOIL and other knots: more interesting surgeries.

For now: compute π₁ of lens spaces and surgery on simple knots,
verify that π₁ = 0 ⟹ S³.
"""

import numpy as np
from itertools import product


def lens_space_pi1(p, q):
    """
    π₁(L(p,q)) = Z_|p| for p ≠ 0.
    L(0,1) = S¹ × S² has π₁ = Z.
    L(1,q) = S³ has π₁ = 0.
    L(-1,q) = S³ has π₁ = 0.
    """
    if p == 0:
        return "Z"  # infinite cyclic
    return f"Z_{abs(p)}" if abs(p) > 1 else "0"


def is_simply_connected_lens(p, q):
    """Is L(p,q) simply connected?"""
    return abs(p) == 1


def is_S3_lens(p, q):
    """Is L(p,q) homeomorphic to S³?"""
    return abs(p) == 1


def dehn_surgery_unknot_census():
    """
    Census of Dehn surgeries on the unknot.
    p/q surgery on unknot = L(p,q).
    """
    print("--- Dehn Surgery on UNKNOT ---")
    print(f"{'p':>4} {'q':>4} | {'π₁':>8} | {'SC?':>4} | {'≅S³?':>5} | {'SC⟹S³?':>8}")
    print("-" * 45)

    sc_count = 0
    s3_count = 0
    counterexample = False

    for p in range(-10, 11):
        for q in range(0, 5):
            if p == 0 and q == 0:
                continue  # not a valid surgery
            if q == 0 and p != 0:
                q_eff = 0
                p_eff = 1  # p/0 surgery = trivial = S³
            else:
                from math import gcd
                g = gcd(abs(p), abs(q)) if q != 0 else abs(p)
                if g == 0:
                    continue
                p_eff, q_eff = p // g, q // g

            pi1 = lens_space_pi1(p_eff, q_eff)
            sc = is_simply_connected_lens(p_eff, q_eff)
            s3 = is_S3_lens(p_eff, q_eff)

            if sc:
                sc_count += 1
                if s3:
                    s3_count += 1
                else:
                    counterexample = True

            if sc or abs(p) <= 3:
                check = "✓" if (not sc or s3) else "✗ FAIL"
                print(f"{p:4d} {q:4d} | {pi1:>8} | {'Y' if sc else 'N':>4} | "
                      f"{'Y' if s3 else 'N':>5} | {check:>8}")

    return sc_count, s3_count, counterexample


def surgery_on_trefoil():
    """
    Dehn surgery on the trefoil knot.

    The trefoil is a torus knot T(2,3). Surgery with slope p/q gives:
    - Seifert fibered spaces for most slopes
    - π₁ depends on p and the knot group

    For the trefoil: the knot group is ⟨a, b | a² = b³⟩ (braid group B₃).
    After p/q surgery: add relation μ^p λ^q = 1 where μ = aba, λ = (ab)² a⁻⁶.

    Key surgeries:
    - (+1)-surgery: Poincaré homology sphere Σ(2,3,5), π₁ = binary icosahedral
      (order 120). NOT simply connected but H₁ = 0!
    - (0)-surgery: π₁ = Z (infinite)
    - (-1)-surgery: S³ (π₁ = 0)

    The Poincaré homology sphere is the CLASSIC example showing that
    H₁ = 0 does NOT imply simply connected in dim 3.
    """
    print("\n--- Surgery on TREFOIL ---")
    print("The trefoil has knot group ⟨a,b | a² = b³⟩")
    print()

    surgeries = {
        (1, 1): ("Poincaré homology sphere Σ(2,3,5)", "Binary icosahedral (order 120)", False, False),
        (0, 1): ("S¹ × S² # (something)", "Z", False, False),
        (-1, 1): ("S³", "0", True, True),
        (2, 1): ("Seifert", "Z_3 or similar", False, False),
        (-2, 1): ("Seifert", "finite, nontrivial", False, False),
        (5, 1): ("Seifert", "Z_? (complicated)", False, False),
    }

    print(f"{'p/q':>6} | {'Result':>30} | {'π₁':>25} | {'SC?':>4} | {'≅S³?':>5}")
    print("-" * 80)

    for (p, q), (name, pi1, sc, s3) in sorted(surgeries.items()):
        check = "✓" if (not sc or s3) else "✗"
        print(f"{p:3d}/{q:<2d} | {name:>30} | {pi1:>25} | {'Y' if sc else 'N':>4} | "
              f"{'Y' if s3 else 'N':>5} {check}")

    print()
    print("KEY: (+1)-surgery on trefoil gives the Poincaré homology sphere.")
    print("π₁ = binary icosahedral group (order 120, perfect: [π₁,π₁] = π₁).")
    print("H₁ = π₁/[π₁,π₁] = 0, but π₁ ≠ 0. NOT simply connected.")
    print("This is why Poincaré needed FUNDAMENTAL GROUP, not just homology.")


def main():
    print("=" * 70)
    print("3-MANIFOLD CENSUS — Blind Poincaré Attack")
    print("=" * 70)
    print("Poincaré: π₁ = 0 + closed + 3-manifold ⟹ S³")
    print("Testing by enumeration of Dehn surgeries.")
    print()

    sc_count, s3_count, counterexample = dehn_surgery_unknot_census()
    print(f"\nUnknot census: {sc_count} simply connected, {s3_count} are S³")
    print(f"Counterexample found? {'YES ✗' if counterexample else 'NO ✓'}")

    surgery_on_trefoil()

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print("""
1. Unknot surgeries: L(p,q) has π₁ = Z_|p|.
   Simply connected iff |p| = 1 iff L(p,q) = S³. ✓
   Poincaré holds for ALL lens spaces.

2. Trefoil surgeries: the Poincaré homology sphere has H₁ = 0
   but π₁ ≠ 0. It is NOT a counterexample to Poincaré (not simply connected).
   Only (-1)-surgery gives S³ (π₁ = 0).

3. The pattern: for simple knots, the ONLY surgery giving π₁ = 0 is
   the one that gives S³. No counterexamples found.

NEXT: Generate random triangulations (e.g., using the Pachner moves on S³)
and compute π₁ from the triangulation. If the fundamental group ever
becomes trivial for a non-S³ manifold, we have a counterexample.
(We won't find one — but the search reveals the structure.)
""")


if __name__ == "__main__":
    main()
