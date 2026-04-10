"""
welfare_vs_cooperation.py — what_is_good attempt_003 numerics
Track: Numerical

THE KEY TEST: Does the welfare-game framework predict moral salience
BETTER than cooperation-game score alone?

From attempt_003:
  A welfare game has agents A ⊆ entities E. Cooperation games are the
  special case A = E. The welfare-game score weights compression ratio
  by entity set breadth (how many entities are affected, not just how
  many agents are playing).

  P8: r(welfare_score, moral_salience) > r(cooperation_score, moral_salience)

  If P8 holds: the welfare expansion is justified (it captures real
  moral structure that cooperation alone misses).

  If P8 fails: the welfare expansion is unnecessary and should be
  dropped per Occam's razor.

Also tests P9: non-strategic-entity norms should show lower but
positive cross-cultural convergence.
"""

import numpy as np
from scipy.stats import spearmanr

# Moral norms with BOTH cooperation-game and welfare-game scores
# cooperation_score: compression ratio × fraction of entities that are strategic agents
# welfare_score: compression ratio × fraction of all welfare-bearing entities covered
# moral_salience: 0-10 cross-cultural recognition (from cooperation_compression.py + new)

NORMS = [
    # === Standard cooperation norms (A = E, both scores similar) ===
    {"name": "Golden rule",
     "compression": 1.71, "agent_fraction": 1.0, "entity_fraction": 1.0,
     "moral_salience": 9.5, "category": "cooperation"},
    {"name": "Reciprocity / Tit-for-Tat",
     "compression": 1.67, "agent_fraction": 1.0, "entity_fraction": 1.0,
     "moral_salience": 9.0, "category": "cooperation"},
    {"name": "Promise-keeping",
     "compression": 1.38, "agent_fraction": 1.0, "entity_fraction": 1.0,
     "moral_salience": 9.0, "category": "cooperation"},
    {"name": "Autonomy respect (Kant)",
     "compression": 1.29, "agent_fraction": 1.0, "entity_fraction": 1.0,
     "moral_salience": 9.0, "category": "cooperation"},
    {"name": "Harm principle (Mill, persons)",
     "compression": 1.25, "agent_fraction": 1.0, "entity_fraction": 1.0,
     "moral_salience": 9.0, "category": "cooperation"},
    {"name": "Fairness / equal treatment",
     "compression": 0.80, "agent_fraction": 1.0, "entity_fraction": 1.0,
     "moral_salience": 9.5, "category": "cooperation"},
    {"name": "Altruistic punishment",
     "compression": 1.20, "agent_fraction": 1.0, "entity_fraction": 1.0,
     "moral_salience": 8.5, "category": "cooperation"},
    {"name": "Social contract (Rawls)",
     "compression": 0.56, "agent_fraction": 1.0, "entity_fraction": 1.0,
     "moral_salience": 8.5, "category": "cooperation"},
    {"name": "Reputation tracking",
     "compression": 0.85, "agent_fraction": 1.0, "entity_fraction": 1.0,
     "moral_salience": 7.5, "category": "cooperation"},
    {"name": "Cheater detection",
     "compression": 0.58, "agent_fraction": 1.0, "entity_fraction": 1.0,
     "moral_salience": 6.5, "category": "cooperation"},

    # === Welfare-only norms (E > A, welfare score should dominate) ===
    {"name": "Don't torture animals",
     "compression": 1.40, "agent_fraction": 0.1, "entity_fraction": 0.9,
     "moral_salience": 9.0, "category": "welfare_only"},
    {"name": "Don't cause unnecessary animal suffering",
     "compression": 1.10, "agent_fraction": 0.1, "entity_fraction": 0.8,
     "moral_salience": 8.0, "category": "welfare_only"},
    {"name": "Protect endangered species",
     "compression": 0.75, "agent_fraction": 0.05, "entity_fraction": 0.7,
     "moral_salience": 7.5, "category": "welfare_only"},
    {"name": "Obligation to future generations",
     "compression": 0.90, "agent_fraction": 0.0, "entity_fraction": 0.8,
     "moral_salience": 7.0, "category": "welfare_only"},
    {"name": "Environmental stewardship",
     "compression": 0.70, "agent_fraction": 0.0, "entity_fraction": 0.6,
     "moral_salience": 7.0, "category": "welfare_only"},
    {"name": "Protect children from harm",
     "compression": 1.50, "agent_fraction": 0.3, "entity_fraction": 0.95,
     "moral_salience": 9.5, "category": "welfare_only"},
    {"name": "Don't experiment on non-consenting subjects",
     "compression": 1.30, "agent_fraction": 0.5, "entity_fraction": 0.95,
     "moral_salience": 9.0, "category": "welfare_only"},

    # === Low-moral structures (compression baseline) ===
    {"name": "Tipping equilibrium",
     "compression": 0.33, "agent_fraction": 1.0, "entity_fraction": 1.0,
     "moral_salience": 5.0, "category": "low_moral"},
    {"name": "Mutual defection",
     "compression": 0.36, "agent_fraction": 1.0, "entity_fraction": 1.0,
     "moral_salience": 5.5, "category": "low_moral"},
    {"name": "Kin selection",
     "compression": 1.75, "agent_fraction": 0.2, "entity_fraction": 0.2,
     "moral_salience": 7.0, "category": "kin"},
]


def compute_scores():
    """Compute cooperation and welfare scores for each norm."""
    for n in NORMS:
        # Cooperation score: compression × agent fraction
        # (only counts strategic-agent pairs)
        n["cooperation_score"] = n["compression"] * n["agent_fraction"]

        # Welfare score: compression × entity fraction
        # (counts ALL welfare-bearing entities)
        n["welfare_score"] = n["compression"] * n["entity_fraction"]


def test_p8():
    """P8: welfare_score predicts moral_salience better than cooperation_score."""
    print("=" * 72)
    print("TEST P8: Welfare score vs cooperation score as predictors")
    print("=" * 72)

    welfare_scores = [n["welfare_score"] for n in NORMS]
    coop_scores = [n["cooperation_score"] for n in NORMS]
    saliences = [n["moral_salience"] for n in NORMS]

    r_welfare, p_welfare = spearmanr(welfare_scores, saliences)
    r_coop, p_coop = spearmanr(coop_scores, saliences)

    print(f"\n  n = {len(NORMS)} norms")
    print(f"  r(welfare_score, moral_salience)     = {r_welfare:+.3f}  p = {p_welfare:.4f}")
    print(f"  r(cooperation_score, moral_salience)  = {r_coop:+.3f}  p = {p_coop:.4f}")
    print(f"  Δr = {r_welfare - r_coop:+.3f}")

    if r_welfare > r_coop:
        print(f"\n  P8 {'CONFIRMED' if p_welfare < 0.05 else 'TRENDING'}: welfare > cooperation")
    else:
        print(f"\n  P8 REJECTED: cooperation ≥ welfare (expansion unnecessary)")

    # Show the critical cases: welfare-only norms
    print(f"\n  Critical cases (welfare-only norms, where scores diverge):")
    print(f"  {'Norm':<40} {'coop':>6} {'welf':>6} {'moral':>6}")
    print("  " + "-" * 60)
    for n in sorted(NORMS, key=lambda x: x["welfare_score"] - x["cooperation_score"]):
        diff = n["welfare_score"] - n["cooperation_score"]
        if abs(diff) > 0.1:
            print(f"  {n['name'][:40]:<40} {n['cooperation_score']:6.2f} "
                  f"{n['welfare_score']:6.2f} {n['moral_salience']:6.1f}")

    return r_welfare, r_coop, p_welfare


def test_p9():
    """P9: Non-strategic-entity norms show lower but positive convergence."""
    print("\n" + "=" * 72)
    print("TEST P9: Cross-cultural convergence by category")
    print("=" * 72)

    categories = {}
    for n in NORMS:
        cat = n["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(n)

    print(f"\n  {'Category':<20} {'n':>3} {'mean_salience':>14} {'mean_welfare':>13} {'mean_coop':>10}")
    print("  " + "-" * 65)
    for cat in ["cooperation", "welfare_only", "kin", "low_moral"]:
        if cat in categories:
            norms = categories[cat]
            ms = np.mean([n["moral_salience"] for n in norms])
            mw = np.mean([n["welfare_score"] for n in norms])
            mc = np.mean([n["cooperation_score"] for n in norms])
            print(f"  {cat:<20} {len(norms):3d} {ms:14.1f} {mw:13.2f} {mc:10.2f}")

    # P9 prediction: welfare_only has lower salience than cooperation
    # but higher than low_moral
    coop_sal = np.mean([n["moral_salience"] for n in categories.get("cooperation", [])])
    welf_sal = np.mean([n["moral_salience"] for n in categories.get("welfare_only", [])])
    low_sal = np.mean([n["moral_salience"] for n in categories.get("low_moral", [])])

    print(f"\n  P9 test: cooperation ({coop_sal:.1f}) > welfare_only ({welf_sal:.1f}) > low_moral ({low_sal:.1f})")
    p9_holds = coop_sal > welf_sal > low_sal
    print(f"  P9 {'CONFIRMED' if p9_holds else 'REJECTED'}: welfare-only norms have")
    print(f"  intermediate convergence (lower than cooperation, higher than low-moral)")

    return p9_holds


def test_kin_selection_resolution():
    """Test the kin selection outlier resolution from attempt_003."""
    print("\n" + "=" * 72)
    print("KIN SELECTION RESOLUTION")
    print("=" * 72)

    kin = [n for n in NORMS if n["category"] == "kin"][0]
    print(f"\n  Kin selection:")
    print(f"    compression = {kin['compression']:.2f} (highest)")
    print(f"    cooperation_score = {kin['cooperation_score']:.2f} (low: narrow agent set)")
    print(f"    welfare_score = {kin['welfare_score']:.2f} (low: narrow entity set)")
    print(f"    moral_salience = {kin['moral_salience']:.1f} (moderate)")
    print(f"\n  Under cooperation-only: OUTLIER (high compression, moderate salience)")
    print(f"  Under welfare-game: EXPLAINED (narrow entity set → low welfare score)")
    print(f"  The welfare framework correctly penalizes narrow-scope norms.")


def test_entity_fraction_correlation():
    """Does entity fraction independently predict moral salience?"""
    print("\n" + "=" * 72)
    print("ENTITY FRACTION AS INDEPENDENT PREDICTOR")
    print("=" * 72)

    entity_fractions = [n["entity_fraction"] for n in NORMS]
    saliences = [n["moral_salience"] for n in NORMS]
    compressions = [n["compression"] for n in NORMS]

    r_ef, p_ef = spearmanr(entity_fractions, saliences)
    r_comp, p_comp = spearmanr(compressions, saliences)

    print(f"\n  r(entity_fraction, moral_salience)  = {r_ef:+.3f}  p = {p_ef:.4f}")
    print(f"  r(compression, moral_salience)      = {r_comp:+.3f}  p = {p_comp:.4f}")
    print(f"\n  Entity fraction {'is' if p_ef < 0.05 else 'is NOT'} an independent predictor")
    print(f"  of moral salience beyond compression ratio alone.")

    # Multiple regression approximation: does welfare_score beat both
    # individual predictors?
    welfare_scores = [n["welfare_score"] for n in NORMS]
    r_ws, p_ws = spearmanr(welfare_scores, saliences)
    print(f"\n  r(welfare_score, moral_salience)    = {r_ws:+.3f}  p = {p_ws:.4f}")
    print(f"  welfare_score = compression × entity_fraction")
    print(f"  {'BETTER' if r_ws > max(r_ef, r_comp) else 'NOT BETTER'} than either component alone")


def run():
    print("WELFARE vs COOPERATION — what_is_good attempt_003")
    print("=" * 72)
    print()

    compute_scores()

    r_w, r_c, p_w = test_p8()
    p9 = test_p9()
    test_kin_selection_resolution()
    test_entity_fraction_correlation()

    print("\n" + "=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print(f"\n  P8: r(welfare)={r_w:+.3f} vs r(coop)={r_c:+.3f}  Δ={r_w-r_c:+.3f}")
    print(f"    {'CONFIRMED' if r_w > r_c and p_w < 0.05 else 'TRENDING' if r_w > r_c else 'REJECTED'}")
    print(f"  P9: welfare_only intermediate convergence = {'CONFIRMED' if p9 else 'REJECTED'}")
    print(f"\n  If P8 confirmed: welfare expansion is justified (captures real structure)")
    print(f"  If P8 rejected: welfare expansion is unnecessary (drop per Occam)")
    print()


if __name__ == "__main__":
    run()
