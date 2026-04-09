#!/usr/bin/env python3
"""
physics_ncd.py — NCD analysis across 6 physics problems

Tests whether compression distance creates visible K-clustering among the six
physics open problems. Expected clusters based on conceptual structure:
  - K-manipulation cluster: information + computation (both about K-manipulation)
  - K-dynamics cluster: time + change (both about K-evolution)
  - K-ontology cluster: reality + nothing (both about K-grounding)

NCD(x,y) = [C(xy) - min(C(x), C(y))] / max(C(x), C(y))
where C = gzip compressed size.

NCD ≈ 0: near-identical K-structure
NCD ≈ 1: mostly independent K-structure
NCD > 1: gzip artifact (header overhead); means fully independent

Saves results to: results/physics_ncd_data.json
Writes findings to: results/physics_ncd_findings.md
"""

import gzip
import json
import itertools
from pathlib import Path

# ---------------------------------------------------------------------------
# Problem descriptions (150-200 words each, focused on core K-claims)
# Each description states what the track found, using K/S vocabulary
# ---------------------------------------------------------------------------

DESCRIPTIONS = {
    "what_is_information": """
Information is doing two distinct jobs that have been conflated. S-information (Shannon
entropy) measures channel capacity: how many distinguishable states a source can produce.
K-information (Kolmogorov complexity) measures compressibility: how much structure a
string contains, or equivalently, the length of its shortest generating program. These
are orthogonal. Random noise has maximum S-information and minimum K-information.
A structured English text has high S-information and moderate K-information. Sorting
a string changes K by 94 percent while leaving S unchanged. The S/K bifurcation has
a second level: K_laws (K of dynamical laws, approximately invariant under physical
reformulation) vs K_state (K of specific configurations, highly description-relative).
Maxwell equations vary only 17.7 percent across four formulations; a permuted English
text varies 88-fold. The fundamental information content of reality is K_laws, which
equals roughly 21,834 bits for all known physics. K_state and S_state are derived from
K_laws plus contingent quantum history. The hierarchy is: K_laws ≤ K_state ≤ S_state.
Every classical ontology of information (Shannon, Kolmogorov, Landauer, Wheeler) is a
theory of one level of this hierarchy; none is a complete general theory.
""".strip(),

    "what_is_computation": """
Computation is K-information manipulation in finitely specifiable form. A computation
takes inputs with some K-content and S-content and produces outputs, implementing a
K-level function while consuming thermodynamic resources at the S level. The Church-Turing
thesis restated is: every effectively calculable function has a finite K-specification as
a Turing program. Physical Church-Turing adds that every physically realizable K-function
has such a specification. The P vs NP problem restates as: compression-finding is
categorically harder than compression-verifying. A NP witness is the K-specification of
the solution; finding that K-specification requires exponential search through K-opaque
landscapes. Measured SAT landscapes at clause ratio 4.3 show flat gzip-K during search,
meaning no compression gradient and no exploitable K-structure. Easy instances show
decreasing gzip-K under unit propagation, revealing exploitable K-structure. Quantum
search halves the exponent but structured classical search beats quantum on K-structured
problems. The find-versus-verify ratio reaches 4698-fold at n=18 variables, growing
super-polynomially. K-complexity and circuit complexity converge: minimum program length,
circuit depth, and information content are the same quantity viewed from different angles.
""".strip(),

    "what_is_time": """
Time is the dimension along which compression makes predictions. The block-universe vs
phenomenal-flow contradiction dissolves under the compression view: block universe
describes the physical substrate; felt flow describes the self-model traversing it.
The thermodynamic arrow of time is an S-arrow: Shannon entropy H increases monotonically
from boundary conditions. K does not have a corresponding arrow in the same way. Both
the initial macrostate (all particles in left half) and the final macrostate (uniform
in box) are K-simple — each is a short description — while the microstate K remains
roughly constant throughout. The arrow is not about K decreasing but about the growing
divergence between macro-description K (bounded and short) and micro-description K
(growing incompressible as the gas spreads). Emergent time programs (entanglement-first,
information-first) locate time as the dimension along which entanglement entropy grows.
Phenomenological time (Husserl: retention, now, protention) is the self-model's report
of updating over successive compressed states. Feedforward systems have no phenomenal
time; recurrent systems have time proportional to self-model tracking of consecutive
compressed states. The residual gap is why this specific arrow direction and whether
primitivist accounts of felt time survive the compression reframing.
""".strip(),

    "what_is_change": """
Change is the structured dynamics of compressible states: successive states related by
rules shorter to specify than the states themselves. Three elements are jointly necessary
for change: states, transitions, and structured transitions (transitions compressible by
the same laws). Zeno's arrow paradox confuses relational properties with momentary ones;
the dichotomy paradox misses that an infinite process can have finite K-content. The S/K
bifurcation resolves Zeno ontologically: a motion from A to B with infinitely many
intermediate positions has K(trajectory) = K(law + endpoints), which is finite. The
causal-glue question — what connects successive states into change — is answered by saying
the connection IS the compressibility of the relation. Laws are short programs generating
long state sequences; the shortness of the program is the causal structure. DNA mutation
involves K-change of 2 bits and Landauer cost of 5.93e-21 joules; actual biological cost
is 36 times the floor. Neuron firing involves K-change of 1 bit; actual cost is 700
million times the Landauer floor, reflecting the overhead of thermodynamic irreversibility
beyond the minimal K-update cost. Change is fundamentally a K-information update; entropy
increase is thermodynamic background noise distinct from the K-events that constitute change.
""".strip(),

    "what_is_reality": """
Reality is its converged compression: the regularity stack that competent compressors
must converge on given sufficient observations. The seven classical ontologies (physicalism,
mathematical universe, informationalism, process philosophy, idealism, neutral monism,
relational) are not competitors but different vocabularies for the same converged K-stack.
The simulation hypothesis reduces to a question about how many layers of compression are
stacked; the difference between real and simulated reality dissolves if no layer can see
its outer layer. The Standard Model Lagrangian plus General Relativity encodes all known
physics in approximately 21,834 bits. The observable universe history occupies approximately
10^124 bits under the holographic bound. K_laws divided by S_holo is approximately 10^-119:
the universe is a 10^119-to-1 compression of its possible state space. This ratio is the
quantitative backbone of K-informationalism as an ontological thesis. S-ontologies (it-from-bit
in the Shannon sense) and K-ontologies (it-from-compression) make different predictions
about Planck-scale discretization. The Parmenidean impossibility of genuine nothingness
holds under the compression view: zero K-content is not a specifiable state, because
specifying it introduces K-content. Reality as converged compression is what the claim
that the universe has a specific information content means when made precise.
""".strip(),

    "what_is_nothing": """
Nothing has been four distinct concepts that the literature conflates: empty room (no
objects of a given type), physical vacuum (no particles but quantum fields present),
quantum vacuum (ground state of quantum field theory, with energy and fluctuations),
and metaphysical non-being (genuine absence of everything including laws and possibility).
Only the fourth is the real tier-0 question. The quantum vacuum is K-poor in laws but
S-rich in modes: the Standard Model Lagrangian is approximately 2000 characters, while
Planck-scale modes per cubic meter number 10^104. K divided by S is 10^-101 for the
vacuum, the most extreme S/K split in physics. The cosmological constant problem is an
S/K problem: quantum field theory sums all S-modes to predict vacuum energy density
roughly 10^120 times too large. If vacuum energy is a K-quantity (determined by K_laws)
rather than an S-sum, the discrepancy may reflect using an S-calculation where a
K-calculation is needed. Metaphysical nothingness is conceptually unstable: a state
of zero K-content cannot be specified without introducing K-content to make the
distinction between nothing and not-nothing. Genuine nothingness may be impossible
for the same reason that specifying an empty set requires the concept of set. The
Parmenidean argument — something must exist because genuine non-being is incoherent —
receives compression-theoretic support: K-zero is not a stable reachable state.
""".strip(),
}

# ---------------------------------------------------------------------------
# NCD computation
# ---------------------------------------------------------------------------

def gzip_compress(data: bytes) -> int:
    """Return compressed byte count using gzip."""
    return len(gzip.compress(data, compresslevel=9))


def ncd(x: bytes, y: bytes) -> float:
    """Normalized Compression Distance."""
    cx = gzip_compress(x)
    cy = gzip_compress(y)
    cxy = gzip_compress(x + y)
    return (cxy - min(cx, cy)) / max(cx, cy)


def encode(text: str) -> bytes:
    return text.encode("utf-8")


# ---------------------------------------------------------------------------
# Main analysis
# ---------------------------------------------------------------------------

def main():
    problems = list(DESCRIPTIONS.keys())
    encoded = {p: encode(DESCRIPTIONS[p]) for p in problems}
    sizes = {p: gzip_compress(encoded[p]) for p in problems}

    # Compute all pairwise NCD values
    pairs = list(itertools.combinations(problems, 2))
    ncd_values = {}
    for a, b in pairs:
        val = ncd(encoded[a], encoded[b])
        ncd_values[(a, b)] = val
        print(f"NCD({a.replace('what_is_','')}, {b.replace('what_is_','')}) = {val:.4f}")

    # Rank pairs by NCD (ascending = most similar)
    ranked = sorted(ncd_values.items(), key=lambda kv: kv[1])

    print("\n--- Ranked by similarity (lowest NCD = most shared K-structure) ---")
    for (a, b), v in ranked:
        a_short = a.replace("what_is_", "")
        b_short = b.replace("what_is_", "")
        print(f"  {a_short:15s} <-> {b_short:15s}  NCD = {v:.4f}")

    # Check predicted clusters
    clusters = {
        "K-manipulation (info+comp)": ("what_is_information", "what_is_computation"),
        "K-dynamics (time+change)": ("what_is_time", "what_is_change"),
        "K-ontology (reality+nothing)": ("what_is_reality", "what_is_nothing"),
    }

    print("\n--- Predicted cluster pairs ---")
    cluster_ncds = {}
    for label, (a, b) in clusters.items():
        key = (a, b) if (a, b) in ncd_values else (b, a)
        v = ncd_values[key]
        cluster_ncds[label] = v
        rank = [k for k, _ in ranked].index(key) + 1
        print(f"  {label}: NCD = {v:.4f}  (rank {rank}/{len(pairs)})")

    # Cluster analysis: within-cluster vs between-cluster
    cluster_members = {
        "K-manipulation": ["what_is_information", "what_is_computation"],
        "K-dynamics": ["what_is_time", "what_is_change"],
        "K-ontology": ["what_is_reality", "what_is_nothing"],
    }

    within_ncds = []
    between_ncds = []
    for (a, b), v in ncd_values.items():
        same_cluster = False
        for members in cluster_members.values():
            if a in members and b in members:
                same_cluster = True
                break
        if same_cluster:
            within_ncds.append(v)
        else:
            between_ncds.append(v)

    avg_within = sum(within_ncds) / len(within_ncds)
    avg_between = sum(between_ncds) / len(between_ncds)
    separation = avg_between - avg_within

    print(f"\n--- Cluster separation ---")
    print(f"  Within-cluster NCD mean:  {avg_within:.4f}")
    print(f"  Between-cluster NCD mean: {avg_between:.4f}")
    print(f"  Separation:               {separation:.4f}")
    print(f"  Clustering visible: {'YES' if separation > 0 else 'NO'}")

    # Save JSON results
    result = {
        "descriptions": DESCRIPTIONS,
        "compressed_sizes_bytes": sizes,
        "ncd_pairs": {
            f"{a}|{b}": round(v, 6)
            for (a, b), v in ncd_values.items()
        },
        "ranked_pairs": [
            {
                "a": a,
                "b": b,
                "ncd": round(v, 6),
                "rank": i + 1,
            }
            for i, ((a, b), v) in enumerate(ranked)
        ],
        "predicted_clusters": {
            label: {
                "pair": list(pair),
                "ncd": round(ncd_values.get(pair, ncd_values.get((pair[1], pair[0]), None)), 6),
            }
            for label, pair in clusters.items()
        },
        "cluster_analysis": {
            "within_cluster_ncds": [round(v, 6) for v in within_ncds],
            "between_cluster_ncds": [round(v, 6) for v in between_ncds],
            "avg_within": round(avg_within, 6),
            "avg_between": round(avg_between, 6),
            "separation": round(separation, 6),
            "clustering_visible": separation > 0,
        },
    }

    out_dir = Path(__file__).parent.parent / "results"
    out_dir.mkdir(exist_ok=True)
    json_path = out_dir / "physics_ncd_data.json"
    with open(json_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nSaved: {json_path}")

    return result


if __name__ == "__main__":
    main()
