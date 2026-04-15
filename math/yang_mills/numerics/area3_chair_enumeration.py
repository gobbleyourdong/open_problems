"""
area3_chair_enumeration.py — count area-3 surfaces bounded by the
chair loop, for attempt_050 / attempt_058 (YM mass-gap program).

Setup: the chair is two plaquettes sharing one edge at 90°. Concretely,
on Z^4:
  P = plaquette in (0,1)-plane at origin, corners {0, e0, e0+e1, e1}
  Q = plaquette in (0,2)-plane at origin, corners {0, e0, e0+e2, e2}
Shared edge: 0 ↔ e0.

Chair as a signed 2-chain: we pick orientations so the shared 0↔e0 edge
cancels between P and Q. The chair's boundary (6 edges) is then the
oriented 1-chain
  ∂Chair = ∂P + ∂Q,
where ∂P uses orientation that sends 0→e0, and ∂Q uses orientation that
sends e0→0 (opposite), so [0↔e0] terms cancel.

Area-3 surfaces bounded by Chair = signed 2-chains with support on
exactly 3 plaquettes whose signed boundary equals ∂Chair.

We enumerate all plaquettes within a small bounding box around the chair
(box radius = 2 in each direction around {0, e0, e1, e2}), generate all
3-subsets, and test the boundary-equality condition for each subset with
all 2^3 sign patterns. The count is reported.

For comparison: we also compute the area-3 surfaces bounded by the
single-plaquette Wilson loop of P (the boundary of P alone), which is
what appears in the product ⟨Tr P⟩⟨Tr Q⟩ expansion at the c³ level in P.
"""
import itertools
from collections import defaultdict


# ---------- edge and plaquette representation ----------

def canon_edge(a, b):
    """Unoriented edge key as a frozenset of endpoints (tuples)."""
    return frozenset([tuple(a), tuple(b)])


def oriented_edge(a, b):
    """Oriented edge as a tuple (from, to)."""
    return (tuple(a), tuple(b))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def unit(i, d=4):
    return tuple(1 if j == i else 0 for j in range(d))


def plaquette_boundary(pos, mu, nu, d=4):
    """Oriented boundary of a unit plaquette at corner `pos` in plane (mu,nu).
    Goes pos -> pos+e_mu -> pos+e_mu+e_nu -> pos+e_nu -> pos.
    Returns a list of oriented edges (as 4 tuples each of 2 points).
    """
    e_mu = unit(mu, d)
    e_nu = unit(nu, d)
    v0 = tuple(pos)
    v1 = add(v0, e_mu)
    v2 = add(v1, e_nu)
    v3 = add(v0, e_nu)
    return [(v0, v1), (v1, v2), (v2, v3), (v3, v0)]


def signed_boundary(oriented_edges_list, sign):
    """Scale a boundary list by ±1: returns list of (oe, sign) pairs."""
    return [(oe, sign) for oe in oriented_edges_list]


def combine(signed_chains):
    """Merge list of [(oe, s), ...] into canonical form.
    Orient every edge so the "from" vertex is lexicographically smaller,
    flipping the sign if needed. Sum signs per canonical edge. Drop zeros.
    Returns a dict: canonical_oriented_edge -> net sign.
    """
    acc = defaultdict(int)
    for oe, s in signed_chains:
        a, b = oe
        if a < b:
            acc[(a, b)] += s
        else:
            acc[(b, a)] -= s
    return {k: v for k, v in acc.items() if v != 0}


def plaquettes_in_box(radius, d=4):
    """All plaquettes (pos, mu, nu) with all four corners in [-radius, radius]^d."""
    out = []
    for pos in itertools.product(range(-radius, radius + 1), repeat=d):
        for mu in range(d):
            for nu in range(mu + 1, d):
                e_mu = unit(mu, d)
                e_nu = unit(nu, d)
                corners = [pos, add(pos, e_mu),
                           add(add(pos, e_mu), e_nu), add(pos, e_nu)]
                if all(all(-radius <= c <= radius for c in corner) for corner in corners):
                    out.append((pos, mu, nu))
    return out


def plaquette_edges(pos, mu, nu, d=4):
    """Set of canonical (unoriented) edges of the plaquette."""
    bdy = plaquette_boundary(pos, mu, nu, d)
    return frozenset(canon_edge(a, b) for a, b in bdy)


def near_chair_plaquettes(chair_edges_canon, radius=1, d=4):
    """Plaquettes that share at least one edge with the chair."""
    pool = plaquettes_in_box(radius, d)
    out = []
    for p in pool:
        pe = plaquette_edges(*p, d=d)
        if pe & chair_edges_canon:
            out.append(p)
    return out


# ---------- chair construction ----------

def chair_chain(d=4):
    """The chair 2-chain. Returns list of (plaquette_id, sign) and
    the canonical boundary as a dict."""
    origin = tuple(0 for _ in range(d))
    # P in (0,1), Q in (0,2). Orient P with +1, Q with -1 so shared edge cancels.
    P_bdy = plaquette_boundary(origin, 0, 1, d)
    Q_bdy = plaquette_boundary(origin, 0, 2, d)
    chain = signed_boundary(P_bdy, +1) + signed_boundary(Q_bdy, -1)
    boundary = combine(chain)
    return [('P', +1), ('Q', -1)], boundary


# ---------- enumeration ----------

def enumerate_area_k(chair_bdy, k=3, radius=1, d=4):
    """Count k-plaquette signed 2-chains with boundary = ±chair_bdy."""
    chair_edges_canon = frozenset(canon_edge(a, b) for (a, b) in chair_bdy.keys())
    e0 = unit(0, d)
    zero = tuple(0 for _ in range(d))
    chair_edges_canon = chair_edges_canon | {canon_edge(zero, e0)}
    plaquettes = near_chair_plaquettes(chair_edges_canon, radius=radius, d=d)
    pre_bdy = {p: plaquette_boundary(*p, d=d) for p in plaquettes}
    chair_bdy_neg = {e: -s for e, s in chair_bdy.items()}
    count = 0
    examples = []
    for sub in itertools.combinations(plaquettes, k):
        for signs in itertools.product([+1, -1], repeat=k):
            signed = []
            for p, s in zip(sub, signs):
                signed.extend(signed_boundary(pre_bdy[p], s))
            bdy = combine(signed)
            if bdy == chair_bdy or bdy == chair_bdy_neg:
                count += 1
                if len(examples) < 3:
                    examples.append((sub, signs))
    return count, examples, len(plaquettes)


def enumerate_area3(chair_bdy, radius=1, d=4):
    """Count 3-plaquette signed 2-chains (with ±1 signs each) whose boundary
    equals chair_bdy. Restricts pool to plaquettes that share at least one
    edge with the chair's 7 edges (including the internal 0↔e0 edge)."""
    chair_edges_canon = frozenset(canon_edge(a, b) for (a, b) in chair_bdy.keys())
    # Also include the internal shared edge (0↔e0)
    e0 = unit(0, d)
    zero = tuple(0 for _ in range(d))
    chair_edges_canon = chair_edges_canon | {canon_edge(zero, e0)}

    plaquettes = near_chair_plaquettes(chair_edges_canon, radius=radius, d=d)
    # Precompute each plaquette's signed boundary (with sign +1) as
    # list of (oe, +1) pairs
    pre_bdy = {p: plaquette_boundary(*p, d=d) for p in plaquettes}

    count = 0
    examples = []

    for sub in itertools.combinations(plaquettes, 3):
        for signs in itertools.product([+1, -1], repeat=3):
            signed = []
            for p, s in zip(sub, signs):
                signed.extend(signed_boundary(pre_bdy[p], s))
            bdy = combine(signed)
            if bdy == chair_bdy:
                count += 1
                if len(examples) < 6:
                    examples.append((sub, signs))

    return count, examples, len(plaquettes)


# ---------- main ----------

def main():
    print("Area-3 surface enumeration for the chair loop (SU-N lattice, d=4)")
    print("=" * 70)
    chair_chain_list, chair_bdy = chair_chain(d=4)
    print(f"Chair boundary has {len(chair_bdy)} oriented edges.")
    print(f"Chair boundary edges (canonical):")
    for e, s in sorted(chair_bdy.items()):
        print(f"  {e[0]} -> {e[1]}  (sign {s})")
    print()
    print("Enumerating area-3 chains with plaquettes SHARING an edge with chair...")
    # Also test against ±chair boundary (since sign of chain can flip)
    chair_bdy_neg = {k: -v for k, v in chair_bdy.items()}
    count_pos, examples_pos, pool_size = enumerate_area3(chair_bdy, radius=2, d=4)
    count_neg, examples_neg, _ = enumerate_area3(chair_bdy_neg, radius=2, d=4)
    count = count_pos + count_neg
    examples = examples_pos + examples_neg
    print(f"  Area-3 chains with bdy = +chair: {count_pos}")
    print(f"  Area-3 chains with bdy = -chair: {count_neg}")
    total_subs = (pool_size * (pool_size - 1) * (pool_size - 2)) // 6
    print(f"  Near-chair plaquette pool size: {pool_size}")
    print(f"  Total 3-subsets tested: {total_subs}")
    print()
    print(f"Area-3 chains with boundary = chair boundary: {count}")
    print()
    print("First few examples:")
    for i, (sub, signs) in enumerate(examples):
        print(f"  [{i + 1}]")
        for (pos, mu, nu), s in zip(sub, signs):
            print(f"      plaq pos={pos} plane=({mu},{nu}) sign={s:+d}")


if __name__ == "__main__":
    main()
