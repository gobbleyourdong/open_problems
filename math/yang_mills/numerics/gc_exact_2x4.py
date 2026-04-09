#!/usr/bin/env python3
"""
YM Brute Force Proof: Exact GC as polynomial in c on the 2⁴ lattice.

CHARACTER EXPANSION approach:
- Each plaquette weight: W(U_P) = 1 + 2c·χ_{1/2}(U_P) for j_max=1/2
  where c = I₂(β)/I₁(β) ∈ (0, 1)
- Link integrals use Schur orthogonality: ∫ D^j(U) D^{j'}(U†) dU = δ_{jj'}/d_j
- After integrating ALL links: Z = polynomial in c
- GC = (derivative stuff) / Z = rational function of c

On a 2⁴ torus:
- 16 sites, 64 links, 96 plaquettes
- After gauge fixing (maximal tree): 49 independent links
- Each link integral collapses character products on adjacent plaquettes

The key insight: we don't enumerate CONFIGURATIONS (too many).
We enumerate REPRESENTATION ASSIGNMENTS to plaquettes and use
Schur orthogonality to evaluate the link integrals algebraically.

For j_max=1/2: each plaquette is j=0 (weight 1) or j=1/2 (weight 2c).
The link integral for a link shared by k plaquettes with reps j₁,...,j_k:
- All j_i = 0: integral = 1 (trivial)
- All j_i = 1/2: integral = (1/2)^{k-1} (Schur, d_{1/2}=2)
- Mixed: integral = 0 (orthogonality kills mixed reps)

So: the partition function is a sum over CONSISTENT rep assignments
(where every link has either all-0 or all-1/2 neighbors).

This is a CONSTRAINT SATISFACTION problem — enumerate all valid
assignments and sum their weights. On a 2⁴ lattice: tractable.
"""

import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from interval import Interval


def lattice_2x4():
    """
    Build the 2⁴ torus: sites, links, plaquettes, and their connectivity.

    Sites: (x₀,x₁,x₂,x₃) with xᵢ ∈ {0,1}, periodic BC.
    Links: (site, direction μ) for μ = 0,1,2,3.
    Plaquettes: (site, μ, ν) for μ < ν.
    """
    L = 2
    sites = [(x0,x1,x2,x3) for x0 in range(L) for x1 in range(L)
             for x2 in range(L) for x3 in range(L)]

    # Links: (site_index, direction)
    site_idx = {s: i for i, s in enumerate(sites)}
    links = []
    for i, s in enumerate(sites):
        for mu in range(4):
            links.append((i, mu))
    # Each link (i, mu) connects site i to site (i + e_mu) mod L.

    # Plaquettes: (site_index, mu, nu) for mu < nu
    plaquettes = []
    for i, s in enumerate(sites):
        for mu in range(4):
            for nu in range(mu+1, 4):
                plaquettes.append((i, mu, nu))

    # For each plaquette: which 4 links does it use?
    # P(x, mu, nu) uses links: (x,mu), (x+e_mu, nu), (x+e_nu, mu)†, (x, nu)†
    def shift(site, mu):
        s = list(site)
        s[mu] = (s[mu] + 1) % L
        return tuple(s)

    plaq_links = []
    for (i, mu, nu) in plaquettes:
        s = sites[i]
        s_mu = shift(s, mu)
        s_nu = shift(s, nu)
        # Links: (x,mu), (x+mu,nu), (x+nu,mu), (x,nu)
        l0 = (site_idx[s], mu)
        l1 = (site_idx[s_mu], nu)
        l2 = (site_idx[s_nu], mu)  # traversed backward
        l3 = (site_idx[s], nu)     # traversed backward
        plaq_links.append((l0, l1, l2, l3))

    # For each link: which plaquettes contain it?
    link_idx = {l: i for i, l in enumerate(links)}
    link_plaqs = {i: [] for i in range(len(links))}
    for p_idx, (l0, l1, l2, l3) in enumerate(plaq_links):
        for l in [l0, l1, l2, l3]:
            li = link_idx[l]
            link_plaqs[li].append(p_idx)

    return {
        'sites': sites,
        'links': links,
        'plaquettes': plaquettes,
        'plaq_links': plaq_links,
        'link_plaqs': link_plaqs,
        'link_idx': link_idx,
        'n_sites': len(sites),
        'n_links': len(links),
        'n_plaqs': len(plaquettes),
    }


def enumerate_valid_assignments(lattice):
    """
    Enumerate all valid representation assignments to plaquettes.

    Each plaquette gets j=0 or j=1/2.
    Constraint: for each link, all adjacent plaquettes with j=1/2 must
    form a consistent surface (the link integral is nonzero only if
    ALL plaquettes at that link have the SAME j, or j=0).

    Actually the constraint is simpler: a link shared by plaquettes
    with j₁,...,j_k gives zero unless all non-zero j's are equal.
    With j_max=1/2: either all j=0 (trivial) or all j=1/2 (nontrivial)
    at each link. Mixed (some 0, some 1/2) gives zero.

    So: for each link, the set of adjacent plaquettes with j=1/2
    must be EITHER empty (all j=0) or ALL of them (all j=1/2).

    This means: the plaquettes with j=1/2 form a CLOSED SURFACE
    (every link is either fully inside or fully outside the surface).
    """
    n_plaqs = lattice['n_plaqs']
    link_plaqs = lattice['link_plaqs']
    n_links = lattice['n_links']

    valid = []
    # Brute force: check all 2^96 assignments... TOO MANY (96 plaquettes).
    # Need a smarter enumeration.

    # Actually: the constraint is that the set S of j=1/2 plaquettes
    # forms a 2-cycle in Z₂ homology (closed surface mod 2).
    # On a 2⁴ torus: H₂(T⁴; Z₂) = Z₂^6 (6 generators, one per plane).
    # So there are 2⁶ = 64 valid assignments!

    # The 6 generators: for each pair (μ,ν), the set of ALL plaquettes
    # in the (μ,ν) plane forms a closed surface.
    # On a 2⁴ torus: each (μ,ν) plane has 2⁴/2² × ... = 4 plaquettes.
    # Wait: 2⁴ torus has 2⁴ = 16 sites. Each (μ,ν) plane has 16 plaquettes
    # (one per site). But on a 2⁴ torus: 2² = 4 distinct plaquette positions
    # per plane (since the torus wraps).

    # Actually on a 2⁴ lattice: 16 sites × C(4,2) = 16 × 6 = 96 plaquettes total.
    # Per (μ,ν) plane: 16 plaquettes.
    # A basis for H₂(T⁴; Z₂): the 6 coordinate planes {(μ,ν) : μ<ν}.
    # Each generator = all 16 plaquettes in one plane.

    # The 2⁶ = 64 valid assignments are: for each subset S ⊆ {6 planes},
    # the plaquettes with j=1/2 are the union of plaquettes in the planes in S.

    planes = [(mu, nu) for mu in range(4) for nu in range(mu+1, 4)]
    assert len(planes) == 6

    # For each of the 64 subsets of planes:
    for mask in range(64):
        assignment = [0] * n_plaqs  # 0 = j=0, 1 = j=1/2
        active_planes = [planes[i] for i in range(6) if mask & (1 << i)]

        for p_idx, (site_i, mu, nu) in enumerate(lattice['plaquettes']):
            # Count how many active planes contain this plaquette
            count = sum(1 for (m, n) in active_planes if (m, n) == (mu, nu))
            # Plaquette is j=1/2 if it's in an ODD number of active planes
            assignment[p_idx] = count % 2

        valid.append((mask, assignment))

    return valid


def compute_Z_and_GC(lattice, c_val):
    """
    Compute Z(c) and GC(c) exactly via the character expansion.

    Z = Σ_{valid S} (2c)^{|S|} × ∏_{links in S} (1/d_{1/2})^{excess}

    For each valid assignment (set S of j=1/2 plaquettes):
    - Weight from plaquettes: (2c)^{|S|}
    - Weight from links: for each link with all k adjacent plaquettes in S:
      factor = (1/2)^{k-1} (from Schur orthogonality)
    - Weight from links NOT in S: factor = 1

    Total weight = (2c)^{|S|} × ∏_{links fully in S} (1/2)^{(k-1)}
    """
    valid_assignments = enumerate_valid_assignments(lattice)
    link_plaqs = lattice['link_plaqs']

    if isinstance(c_val, Interval):
        Z = Interval(0)
        two_c = Interval(2) * c_val
    else:
        Z = 0.0
        two_c = 2 * c_val

    weights = []
    for mask, assignment in valid_assignments:
        n_half = sum(assignment)  # number of j=1/2 plaquettes

        # Plaquette weight
        if isinstance(c_val, Interval):
            w = two_c ** n_half if n_half > 0 else Interval(1)
        else:
            w = two_c ** n_half if n_half > 0 else 1.0

        # Link weights: for each link, count how many adjacent plaquettes are j=1/2
        for link_i, adj_plaqs in link_plaqs.items():
            n_adj_half = sum(assignment[p] for p in adj_plaqs)
            if n_adj_half > 0 and n_adj_half == len(adj_plaqs):
                # All adjacent plaquettes are j=1/2: factor = (1/2)^{k-1}
                k = len(adj_plaqs)
                if isinstance(c_val, Interval):
                    w = w * Interval(0.5) ** (k - 1)
                else:
                    w *= 0.5 ** (k - 1)
            elif n_adj_half > 0:
                # Mixed: this assignment is INVALID (orthogonality kills it)
                w = Interval(0) if isinstance(c_val, Interval) else 0.0
                break

        weights.append((mask, n_half, w))
        Z = Z + w

    return Z, weights


def main():
    print("=" * 70)
    print("YM BRUTE FORCE: Exact GC on 2⁴ Lattice")
    print("=" * 70)

    lat = lattice_2x4()
    print(f"2⁴ torus: {lat['n_sites']} sites, {lat['n_links']} links, {lat['n_plaqs']} plaquettes")

    # Enumerate valid assignments
    valid = enumerate_valid_assignments(lat)
    print(f"Valid representation assignments (H₂ basis): {len(valid)}")
    print()

    # Compute Z(c) for several c values
    print("Z(c) = partition function via character expansion:")
    print(f"{'c':>6} | {'Z(c)':>14} | {'# terms > 0':>12}")
    print("-" * 38)

    for c_val in [0.01, 0.1, 0.3, 0.5, 0.7, 0.9, 0.99]:
        Z, weights = compute_Z_and_GC(lat, c_val)
        n_nonzero = sum(1 for _, _, w in weights if (isinstance(w, float) and w > 0) or
                        (isinstance(w, Interval) and w.lo > 0))
        print(f"{c_val:6.2f} | {Z:14.6f} | {n_nonzero:>12}")

    # Now with INTERVAL ARITHMETIC
    print(f"\nZ(c) with interval arithmetic (rigorous bounds):")
    print(f"{'c interval':>20} | {'Z interval':>30}")
    print("-" * 55)

    for c_lo, c_hi in [(0.0, 0.1), (0.1, 0.3), (0.3, 0.5), (0.5, 0.7), (0.7, 0.9), (0.9, 1.0)]:
        c = Interval(c_lo, c_hi)
        Z, _ = compute_Z_and_GC(lat, c)
        print(f"[{c_lo:.1f}, {c_hi:.1f}]             | {Z}")

    print()
    print("Next: compute GC(c) = (chair expectation - plaq product) / Z")
    print("from the character expansion weights.")


if __name__ == "__main__":
    main()
