#!/usr/bin/env python3
"""
Discrete Ricci Flow on a triangulated S³.

Blind implementation: no reading Perelman, just the PDE ∂g/∂t = -2 Ric.

For a triangulated manifold (Regge calculus):
- Metric data: edge lengths {l_e}
- Curvature: deficit angles at edges (2D) or hinges (3D)
- Ricci flow: evolve edge lengths to reduce curvature variation

Simplest test: start with a PERTURBED S³ (the boundary of a regular
4-simplex = 5-cell, with perturbed edge lengths) and flow toward
the round metric (all edges equal).

The 5-cell has:
- 5 vertices
- 10 edges
- 10 triangular faces
- 5 tetrahedral cells

Its boundary is topologically S³.
"""

import numpy as np
from itertools import combinations


def five_cell_vertices():
    """Vertices of a regular 5-cell (4-simplex) in R⁴."""
    # Regular simplex in R⁴: vertices at distance √2 from each other
    # Standard: v_i = e_i (unit vectors) projected to the hyperplane Σx_i = 1
    # Simple construction: vertices of the 5-cell centered at origin
    v = np.array([
        [1, 1, 1, -1/np.sqrt(5)],
        [1, -1, -1, -1/np.sqrt(5)],
        [-1, 1, -1, -1/np.sqrt(5)],
        [-1, -1, 1, -1/np.sqrt(5)],
        [0, 0, 0, 4/np.sqrt(5)],
    ], dtype=float)
    # Normalize so all pairwise distances are equal
    # The regular 5-cell has edge length = √(8/5) ≈ 1.265
    return v


def edge_lengths(vertices):
    """Compute all pairwise edge lengths."""
    n = len(vertices)
    edges = {}
    for i in range(n):
        for j in range(i+1, n):
            edges[(i,j)] = np.linalg.norm(vertices[i] - vertices[j])
    return edges


def perturb_edges(edges, scale=0.1):
    """Randomly perturb edge lengths."""
    perturbed = {}
    for e, l in edges.items():
        perturbed[e] = l * (1 + scale * np.random.randn())
    # Ensure positive
    for e in perturbed:
        perturbed[e] = max(perturbed[e], 0.1)
    return perturbed


def tetrahedra_of_5cell():
    """The 5 tetrahedral cells of the 5-cell boundary."""
    verts = list(range(5))
    # Each tetrahedron = 4 of the 5 vertices (complement of one vertex)
    return [tuple(v for v in verts if v != i) for i in range(5)]


def dihedral_angle(l_ab, l_ac, l_ad, l_bc, l_bd, l_cd):
    """
    Dihedral angle at edge (a,b) in tetrahedron (a,b,c,d).
    Uses the Cayley-Menger determinant approach.
    """
    # Volume of tetrahedron from edge lengths
    # The dihedral angle θ at edge ab satisfies:
    # cos(θ) = (A_abc · n_abc + A_abd · n_abd) stuff...
    # Simpler: use the formula via face areas and volumes.

    # Face areas: triangle (a,b,c) and (a,b,d)
    def triangle_area(p, q, r):
        s = (p + q + r) / 2
        arg = s * (s-p) * (s-q) * (s-r)
        return np.sqrt(max(arg, 0))

    A1 = triangle_area(l_ab, l_ac, l_bc)  # face abc
    A2 = triangle_area(l_ab, l_ad, l_bd)  # face abd

    if A1 < 1e-10 or A2 < 1e-10:
        return np.pi  # degenerate

    # Cayley-Menger for dihedral angle at edge ab:
    # cos θ = (l_ac² + l_bd² - l_ad² - l_bc² - l_ab² + l_cd²) * l_ab / (something)
    # Actually this is getting complicated. Use a simpler formula.

    # For a tetrahedron with vertices in R³, the dihedral angle can be computed.
    # But we only have edge lengths, not coordinates.
    # Use the Gram matrix approach.

    # cos(dihedral at ab) = (cos α_c - cos α_a cos α_b) / (sin α_a sin α_b)
    # where α_a, α_b, α_c are angles in the face opposite vertex d... too complex.

    # Just use a numerical approach: embed the tetrahedron in R³ from edge lengths.
    # Place a at origin, b along x-axis.
    a = np.array([0, 0, 0])
    b = np.array([l_ab, 0, 0])

    # c in the xy-plane
    cos_bac = (l_ab**2 + l_ac**2 - l_bc**2) / (2 * l_ab * l_ac + 1e-15)
    cos_bac = np.clip(cos_bac, -1, 1)
    sin_bac = np.sqrt(max(0, 1 - cos_bac**2))
    c = np.array([l_ac * cos_bac, l_ac * sin_bac, 0])

    # d above the xy-plane
    # |d - a| = l_ad, |d - b| = l_bd, |d - c| = l_cd
    dx = (l_ad**2 - l_bd**2 + l_ab**2) / (2 * l_ab + 1e-15)
    dy_num = l_ad**2 - dx**2
    if c[1] > 1e-10:
        dy = (l_ad**2 - l_cd**2 + np.dot(c, c) - 2*c[0]*dx) / (2*c[1] + 1e-15)
    else:
        dy = 0
    dz_sq = l_ad**2 - dx**2 - dy**2
    dz = np.sqrt(max(dz_sq, 0))
    d = np.array([dx, dy, dz])

    # Dihedral angle at edge ab: angle between faces abc and abd
    # Normal to abc: n1 = (b-a) × (c-a)
    # Normal to abd: n2 = (b-a) × (d-a)
    ab = b - a
    n1 = np.cross(ab, c - a)
    n2 = np.cross(ab, d - a)

    n1_norm = np.linalg.norm(n1)
    n2_norm = np.linalg.norm(n2)
    if n1_norm < 1e-15 or n2_norm < 1e-15:
        return np.pi

    cos_theta = np.dot(n1, n2) / (n1_norm * n2_norm)
    cos_theta = np.clip(cos_theta, -1, 1)
    return np.arccos(cos_theta)


def edge_curvature(edges, tets):
    """
    Discrete scalar curvature at each edge (Regge curvature).
    κ_e = 2π - Σ_{tets containing e} θ_e(tet)
    where θ_e(tet) is the dihedral angle at edge e in tetrahedron tet.
    """
    curvatures = {e: 2 * np.pi for e in edges}

    for tet in tets:
        # Get all 6 edges of the tetrahedron
        tet_edges = list(combinations(tet, 2))
        tet_lengths = {}
        for i, j in tet_edges:
            key = (min(i,j), max(i,j))
            tet_lengths[(i,j)] = edges.get(key, edges.get((j,i), 1.0))

        a, b, c, d = tet
        for e1, e2 in tet_edges:
            key = (min(e1,e2), max(e1,e2))
            # Compute dihedral angle at this edge
            # Need the 6 edge lengths of the tetrahedron
            l = lambda i, j: tet_lengths.get((i,j), tet_lengths.get((j,i), 1.0))
            theta = dihedral_angle(l(e1,e2), l(e1,c if c not in (e1,e2) else d),
                                   l(e1, d if d not in (e1,e2) else c),
                                   l(e2, c if c not in (e1,e2) else d),
                                   l(e2, d if d not in (e1,e2) else c),
                                   l(c if c not in (e1,e2) else d,
                                     d if d not in (e1,e2) else c))
            curvatures[key] -= theta

    return curvatures


def ricci_flow_step(edges, curvatures, dt=0.01):
    """One step of discrete Ricci flow: dl/dt = -κ_e * l_e."""
    new_edges = {}
    for e, l in edges.items():
        kappa = curvatures.get(e, 0)
        new_edges[e] = l - dt * kappa * l
        new_edges[e] = max(new_edges[e], 0.01)  # prevent collapse
    return new_edges


def main():
    print("=" * 70)
    print("DISCRETE RICCI FLOW ON S³ (5-cell boundary)")
    print("=" * 70)

    # Build the 5-cell
    verts = five_cell_vertices()
    edges = edge_lengths(verts)
    tets = tetrahedra_of_5cell()

    print(f"5-cell: {len(verts)} vertices, {len(edges)} edges, {len(tets)} tetrahedra")
    print(f"Edge lengths (regular): {[f'{l:.4f}' for l in edges.values()][:3]}...")

    # Perturb
    np.random.seed(42)
    edges = perturb_edges(edges, scale=0.15)
    print(f"After perturbation: min={min(edges.values()):.4f}, max={max(edges.values()):.4f}")

    # Run Ricci flow
    print(f"\n--- Discrete Ricci Flow ---")
    print(f"{'Step':>6} | {'min(l)':>8} | {'max(l)':>8} | {'max(l)/min(l)':>14} | {'max|κ|':>8}")
    print("-" * 52)

    for step in range(201):
        curvatures = edge_curvature(edges, tets)
        max_kappa = max(abs(k) for k in curvatures.values())
        min_l = min(edges.values())
        max_l = max(edges.values())
        ratio = max_l / min_l

        if step % 20 == 0:
            print(f"{step:6d} | {min_l:8.4f} | {max_l:8.4f} | {ratio:14.6f} | {max_kappa:8.4f}")

        edges = ricci_flow_step(edges, curvatures, dt=0.005)

    print(f"\n--- Result ---")
    print(f"max(l)/min(l) = {max_l/min_l:.6f} (should → 1 for round sphere)")
    print(f"max|κ| = {max_kappa:.6f} (should → 0 for constant curvature)")
    print()
    if ratio < 1.1:
        print("Flow CONVERGED to approximately round metric. ✓")
        print("The perturbed S³ flows back to the round S³.")
    else:
        print(f"Flow did not fully converge (ratio = {ratio:.4f}).")
        print("May need more steps or smaller dt.")


if __name__ == "__main__":
    main()
