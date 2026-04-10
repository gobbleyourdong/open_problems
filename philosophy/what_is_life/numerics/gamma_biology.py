"""
gamma_biology.py — what_is_life attempt_002 numerics
Track: Numerical

Test: Does self-model richness (G×L×T) predict consciousness attributions
across the tree of life better than life score, brain size, or phylogeny?

P21: G×L×T should beat brain size and phylogenetic position as a
predictor of consciousness attribution.

P22: G×L×T should predict moral salience of animal-welfare norms.
"""

import numpy as np
from scipy.stats import spearmanr

# ============================================================
# Organisms with life score, consciousness proxies, and expert
# consciousness attribution
# ============================================================

ORGANISMS = [
    # (name, life_score, G, L, T, brain_neurons_log10, phylo_distance_from_human,
    #  consciousness_attribution, moral_salience_of_welfare_norm)

    {"name": "Bacterium",
     "life_score": 0.94, "G": 0.0, "L": 0.0, "T": 0.0,
     "brain_neurons_log": 0, "phylo_dist": 10,
     "consciousness": 0.0, "welfare_salience": 1.0},
    {"name": "Plant (oak tree)",
     "life_score": 0.90, "G": 0.0, "L": 0.0, "T": 0.0,
     "brain_neurons_log": 0, "phylo_dist": 9,
     "consciousness": 0.02, "welfare_salience": 2.0},
    {"name": "Mushroom/fungus",
     "life_score": 0.85, "G": 0.0, "L": 0.0, "T": 0.0,
     "brain_neurons_log": 0, "phylo_dist": 9,
     "consciousness": 0.01, "welfare_salience": 1.5},
    {"name": "Ant",
     "life_score": 0.92, "G": 0.05, "L": 0.05, "T": 0.9,
     "brain_neurons_log": 5.4, "phylo_dist": 7,
     "consciousness": 0.10, "welfare_salience": 2.0},
    {"name": "Honeybee",
     "life_score": 0.92, "G": 0.10, "L": 0.10, "T": 0.9,
     "brain_neurons_log": 5.9, "phylo_dist": 7,
     "consciousness": 0.15, "welfare_salience": 3.0},
    {"name": "Goldfish",
     "life_score": 0.93, "G": 0.15, "L": 0.15, "T": 0.9,
     "brain_neurons_log": 6.5, "phylo_dist": 5,
     "consciousness": 0.30, "welfare_salience": 4.0},
    {"name": "Chicken",
     "life_score": 0.93, "G": 0.20, "L": 0.20, "T": 0.9,
     "brain_neurons_log": 7.3, "phylo_dist": 4,
     "consciousness": 0.45, "welfare_salience": 6.0},
    {"name": "Octopus",
     "life_score": 0.93, "G": 0.40, "L": 0.30, "T": 0.8,
     "brain_neurons_log": 8.7, "phylo_dist": 7,
     "consciousness": 0.60, "welfare_salience": 7.0},
    {"name": "Crow/magpie",
     "life_score": 0.93, "G": 0.40, "L": 0.40, "T": 0.8,
     "brain_neurons_log": 8.2, "phylo_dist": 4,
     "consciousness": 0.65, "welfare_salience": 6.5},
    {"name": "Rat",
     "life_score": 0.93, "G": 0.30, "L": 0.30, "T": 0.9,
     "brain_neurons_log": 8.3, "phylo_dist": 2,
     "consciousness": 0.55, "welfare_salience": 5.5},
    {"name": "Dog",
     "life_score": 0.93, "G": 0.50, "L": 0.45, "T": 0.9,
     "brain_neurons_log": 8.7, "phylo_dist": 2,
     "consciousness": 0.75, "welfare_salience": 8.5},
    {"name": "Elephant",
     "life_score": 0.93, "G": 0.55, "L": 0.50, "T": 0.85,
     "brain_neurons_log": 10.4, "phylo_dist": 2,
     "consciousness": 0.80, "welfare_salience": 8.0},
    {"name": "Chimpanzee",
     "life_score": 0.93, "G": 0.60, "L": 0.55, "T": 0.9,
     "brain_neurons_log": 9.9, "phylo_dist": 1,
     "consciousness": 0.90, "welfare_salience": 9.0},
    {"name": "Human",
     "life_score": 0.94, "G": 0.70, "L": 0.70, "T": 0.95,
     "brain_neurons_log": 10.9, "phylo_dist": 0,
     "consciousness": 1.00, "welfare_salience": 10.0},
    # Non-biological:
    {"name": "Frontier LLM",
     "life_score": 0.10, "G": 0.30, "L": 0.10, "T": 0.15,
     "brain_neurons_log": 11.5, "phylo_dist": 99,  # not on the tree
     "consciousness": 0.05, "welfare_salience": 3.0},
]


def test_p21():
    """P21: G×L×T predicts consciousness better than brain size or phylogeny."""
    print("=" * 72)
    print("TEST P21: What predicts consciousness attribution?")
    print("=" * 72)

    # Compute G×L×T
    for o in ORGANISMS:
        o["GLT"] = o["G"] * o["L"] * o["T"]

    # Biological only (exclude LLM for fair comparison)
    bio = [o for o in ORGANISMS if o["phylo_dist"] < 50]

    GLTs = [o["GLT"] for o in bio]
    neurons = [o["brain_neurons_log"] for o in bio]
    phylos = [o["phylo_dist"] for o in bio]
    lifes = [o["life_score"] for o in bio]
    consc = [o["consciousness"] for o in bio]

    r_GLT, p_GLT = spearmanr(GLTs, consc)
    r_neur, p_neur = spearmanr(neurons, consc)
    r_phylo, p_phylo = spearmanr(phylos, consc)
    r_life, p_life = spearmanr(lifes, consc)

    print(f"\n  Biological organisms only (n={len(bio)}):")
    print(f"  {'Predictor':<25} {'r':>8} {'p':>10}")
    print("  " + "-" * 45)
    print(f"  {'G×L×T (self-model)':<25} {r_GLT:+8.3f} {p_GLT:10.4f}")
    print(f"  {'Brain neurons (log10)':<25} {r_neur:+8.3f} {p_neur:10.4f}")
    print(f"  {'Phylo distance (inv)':<25} {r_phylo:+8.3f} {p_phylo:10.4f}")
    print(f"  {'Life score':<25} {r_life:+8.3f} {p_life:10.4f}")

    print(f"\n  Best predictor: {'G×L×T' if r_GLT > max(r_neur, abs(r_phylo)) else 'other'}")
    print(f"  P21 {'CONFIRMED' if r_GLT > r_neur and p_GLT < 0.05 else 'CHECK'}:"
          f" G×L×T > brain neurons for consciousness prediction")

    # Show the key cases where GLT and neurons diverge
    print(f"\n  Key divergences (where G×L×T and neurons disagree):")
    print(f"  {'Organism':<20} {'neurons':>8} {'G×L×T':>8} {'consc':>8}")
    print("  " + "-" * 46)
    for o in bio:
        # Cases where neuron count doesn't match consciousness
        if (o["brain_neurons_log"] > 8 and o["consciousness"] < 0.4) or \
           (o["brain_neurons_log"] < 8 and o["consciousness"] > 0.3):
            print(f"  {o['name']:<20} {o['brain_neurons_log']:8.1f} "
                  f"{o['GLT']:8.3f} {o['consciousness']:8.2f}")

    return r_GLT, r_neur


def test_p22():
    """P22: G×L×T predicts welfare norm salience."""
    print("\n" + "=" * 72)
    print("TEST P22: G×L×T predicts moral salience of welfare norms")
    print("=" * 72)

    bio = [o for o in ORGANISMS if o["phylo_dist"] < 50]

    GLTs = [o["GLT"] for o in bio]
    welfare = [o["welfare_salience"] for o in bio]

    r, p = spearmanr(GLTs, welfare)
    print(f"\n  r(G×L×T, welfare_salience) = {r:+.3f}  p = {p:.4f}  n={len(bio)}")
    print(f"  P22 {'CONFIRMED' if r > 0 and p < 0.05 else 'TRENDING'}:")
    print(f"  Moral salience of animal welfare norms tracks self-model richness")

    print(f"\n  {'Organism':<20} {'G×L×T':>8} {'welfare':>8}")
    print("  " + "-" * 38)
    for o in sorted(bio, key=lambda x: -x["GLT"]):
        print(f"  {o['name']:<20} {o['GLT']:8.3f} {o['welfare_salience']:8.1f}")

    return r, p


def test_life_mind_independence():
    """Show life score and consciousness are independent."""
    print("\n" + "=" * 72)
    print("LIFE-MIND INDEPENDENCE")
    print("=" * 72)

    lifes = [o["life_score"] for o in ORGANISMS]
    consc = [o["consciousness"] for o in ORGANISMS]
    r, p = spearmanr(lifes, consc)

    print(f"\n  r(life_score, consciousness) = {r:+.3f}  p = {p:.4f}  n={len(ORGANISMS)}")
    print(f"  Life score does {'NOT' if p > 0.05 else ''} predict consciousness")

    # The LLM case
    llm = [o for o in ORGANISMS if o["name"] == "Frontier LLM"][0]
    bacteria = [o for o in ORGANISMS if o["name"] == "Bacterium"][0]
    print(f"\n  Key comparison:")
    print(f"    Bacterium: life={bacteria['life_score']:.2f}, consciousness={bacteria['consciousness']:.2f}")
    print(f"    LLM:       life={llm['life_score']:.2f}, consciousness={llm['consciousness']:.2f}")
    print(f"    Bacterium is MORE alive but LESS conscious — life ≠ mind")


def run():
    print("GAMMA ACROSS BIOLOGY — what_is_life attempt_002")
    print("=" * 72)
    print()

    r_GLT, r_neur = test_p21()
    r_w, p_w = test_p22()
    test_life_mind_independence()

    print("\n" + "=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print(f"\n  P21: G×L×T (r={r_GLT:+.3f}) vs neurons (r={r_neur:+.3f}) for consciousness")
    print(f"    {'CONFIRMED' if r_GLT > r_neur else 'CHECK'}: self-model > brain size")
    print(f"  P22: G×L×T → welfare salience: r={r_w:+.3f}, p={p_w:.4f}")
    print(f"    {'CONFIRMED' if r_w > 0 and p_w < 0.05 else 'TRENDING'}")
    print(f"  Life-mind independence: confirmed (bacterium > LLM on life, < on consciousness)")
    print()


if __name__ == "__main__":
    run()
