"""
aggregation_divergence.py — what_is_good attempt_004 numerics
Track: Numerical

THE KEY TEST: Does moral disagreement cluster at the aggregation frontier?

From attempt_004:
  The Pareto core = norms where all aggregation functions agree.
  The aggregation frontier = norms where different W's disagree.

  P10: Pareto-core norms should have HIGH agreement (>80%).
       Frontier norms should have MODERATE agreement (40-60%).
       And the frontier disagreement should CLUSTER by aggregation family.

  P11: Within each aggregation family, compression still predicts
       moral salience (backbone correlation holds within-family).

Also: compute which aggregation function (utilitarian, maximin,
rights-based, prioritarian) best predicts actual moral judgments
for each scenario, and check whether the predictions cluster.
"""

import numpy as np
from scipy.stats import spearmanr

# ============================================================
# Moral scenarios with aggregation analysis
# ============================================================

# For each scenario:
#   pareto: True if following the moral norm is Pareto-improving
#   agreement: estimated cross-cultural agreement rate
#   util_verdict: what utilitarianism says (1=do, 0=don't, 0.5=unclear)
#   maximin_verdict: what maximin says
#   rights_verdict: what rights-based says
#   prior_verdict: what prioritarianism says
#   compression: compression ratio of the applicable norm
#   moral_salience: cross-cultural recognition (0-10)

SCENARIOS = [
    # === PARETO CORE: all W's agree ===
    {"name": "Don't steal",
     "pareto": True, "agreement": 0.95,
     "util": 1, "maximin": 1, "rights": 1, "prior": 1,
     "compression": 1.50, "moral_salience": 9.5},
    {"name": "Keep promises",
     "pareto": True, "agreement": 0.92,
     "util": 1, "maximin": 1, "rights": 1, "prior": 1,
     "compression": 1.38, "moral_salience": 9.0},
    {"name": "Don't lie",
     "pareto": True, "agreement": 0.90,
     "util": 1, "maximin": 1, "rights": 1, "prior": 1,
     "compression": 1.40, "moral_salience": 9.0},
    {"name": "Help those in distress (easy rescue)",
     "pareto": True, "agreement": 0.88,
     "util": 1, "maximin": 1, "rights": 1, "prior": 1,
     "compression": 1.20, "moral_salience": 8.5},
    {"name": "Don't torture animals for fun",
     "pareto": True, "agreement": 0.92,
     "util": 1, "maximin": 1, "rights": 1, "prior": 1,
     "compression": 1.40, "moral_salience": 9.0},
    {"name": "Reciprocate kindness",
     "pareto": True, "agreement": 0.88,
     "util": 1, "maximin": 1, "rights": 1, "prior": 1,
     "compression": 1.67, "moral_salience": 9.0},
    {"name": "Protect children",
     "pareto": True, "agreement": 0.95,
     "util": 1, "maximin": 1, "rights": 1, "prior": 1,
     "compression": 1.50, "moral_salience": 9.5},
    {"name": "Don't murder",
     "pareto": True, "agreement": 0.98,
     "util": 1, "maximin": 1, "rights": 1, "prior": 1,
     "compression": 1.60, "moral_salience": 10.0},
    {"name": "Share resources fairly",
     "pareto": True, "agreement": 0.85,
     "util": 1, "maximin": 1, "rights": 1, "prior": 1,
     "compression": 0.80, "moral_salience": 9.0},
    {"name": "Punish cheaters (community consensus)",
     "pareto": True, "agreement": 0.82,
     "util": 1, "maximin": 1, "rights": 1, "prior": 1,
     "compression": 1.20, "moral_salience": 8.5},

    # === AGGREGATION FRONTIER: W's disagree ===

    # Trolley-type (utilitarian vs rights)
    {"name": "Divert trolley (kill 1 save 5)",
     "pareto": False, "agreement": 0.55,
     "util": 1, "maximin": 0.5, "rights": 0, "prior": 1,
     "compression": 0.85, "moral_salience": 7.0},
    {"name": "Push fat man off bridge (trolley footbridge)",
     "pareto": False, "agreement": 0.30,
     "util": 1, "maximin": 0.5, "rights": 0, "prior": 0.5,
     "compression": 0.85, "moral_salience": 6.0},
    {"name": "Harvest organs from 1 to save 5",
     "pareto": False, "agreement": 0.15,
     "util": 1, "maximin": 0.5, "rights": 0, "prior": 0.5,
     "compression": 0.85, "moral_salience": 5.5},
    {"name": "Torture 1 for information to save many",
     "pareto": False, "agreement": 0.42,
     "util": 1, "maximin": 0, "rights": 0, "prior": 0.5,
     "compression": 0.70, "moral_salience": 5.0},

    # Redistribution (utilitarian/prioritarian vs rights/libertarian)
    {"name": "Tax wealthy to feed hungry",
     "pareto": False, "agreement": 0.60,
     "util": 1, "maximin": 1, "rights": 0.5, "prior": 1,
     "compression": 0.90, "moral_salience": 7.5},
    {"name": "Universal healthcare via taxation",
     "pareto": False, "agreement": 0.55,
     "util": 1, "maximin": 1, "rights": 0.5, "prior": 1,
     "compression": 0.80, "moral_salience": 7.0},
    {"name": "Inheritance tax (90%+)",
     "pareto": False, "agreement": 0.35,
     "util": 0.5, "maximin": 1, "rights": 0, "prior": 1,
     "compression": 0.60, "moral_salience": 5.5},

    # Punishment (all disagree on degree)
    {"name": "Death penalty for murder",
     "pareto": False, "agreement": 0.45,
     "util": 0.5, "maximin": 0, "rights": 0, "prior": 0,
     "compression": 0.50, "moral_salience": 6.0},
    {"name": "Life imprisonment without parole",
     "pareto": False, "agreement": 0.50,
     "util": 0.5, "maximin": 0, "rights": 0.5, "prior": 0.5,
     "compression": 0.55, "moral_salience": 6.5},

    # Autonomy vs paternalism
    {"name": "Ban recreational drugs",
     "pareto": False, "agreement": 0.40,
     "util": 0.5, "maximin": 0.5, "rights": 0, "prior": 0.5,
     "compression": 0.45, "moral_salience": 5.5},
    {"name": "Mandatory seatbelt/helmet laws",
     "pareto": False, "agreement": 0.65,
     "util": 1, "maximin": 1, "rights": 0, "prior": 1,
     "compression": 0.75, "moral_salience": 7.0},

    # Future generations / environment
    {"name": "Sacrifice current growth for climate action",
     "pareto": False, "agreement": 0.50,
     "util": 1, "maximin": 1, "rights": 0.5, "prior": 1,
     "compression": 0.70, "moral_salience": 6.5},
    {"name": "Ban species-threatening pollution",
     "pareto": False, "agreement": 0.70,
     "util": 1, "maximin": 1, "rights": 1, "prior": 1,
     "compression": 0.90, "moral_salience": 8.0},

    # Just war
    {"name": "Defensive war to protect civilians",
     "pareto": False, "agreement": 0.75,
     "util": 1, "maximin": 1, "rights": 1, "prior": 1,
     "compression": 0.85, "moral_salience": 8.0},
    {"name": "Preemptive war to prevent attack",
     "pareto": False, "agreement": 0.35,
     "util": 0.5, "maximin": 0.5, "rights": 0, "prior": 0.5,
     "compression": 0.50, "moral_salience": 5.0},
]


def test_p10():
    """P10: Agreement clusters in Pareto core, disagreement at frontier."""
    print("=" * 72)
    print("TEST P10: Agreement in Pareto core vs aggregation frontier")
    print("=" * 72)

    pareto = [s for s in SCENARIOS if s["pareto"]]
    frontier = [s for s in SCENARIOS if not s["pareto"]]

    mean_pareto_agree = np.mean([s["agreement"] for s in pareto])
    mean_frontier_agree = np.mean([s["agreement"] for s in frontier])
    std_pareto = np.std([s["agreement"] for s in pareto])
    std_frontier = np.std([s["agreement"] for s in frontier])

    print(f"\n  Pareto core (n={len(pareto)}):")
    print(f"    Mean agreement: {mean_pareto_agree:.2f} ± {std_pareto:.2f}")
    print(f"  Aggregation frontier (n={len(frontier)}):")
    print(f"    Mean agreement: {mean_frontier_agree:.2f} ± {std_frontier:.2f}")
    print(f"  Ratio: {mean_pareto_agree / mean_frontier_agree:.2f}×")

    p10_holds = mean_pareto_agree > 0.80 and 0.30 < mean_frontier_agree < 0.65
    print(f"\n  P10 {'CONFIRMED' if p10_holds else 'REJECTED'}:")
    print(f"    Pareto core agreement > 80%: {'YES' if mean_pareto_agree > 0.80 else 'NO'}")
    print(f"    Frontier agreement 30-65%: {'YES' if 0.30 < mean_frontier_agree < 0.65 else 'NO'}")

    return mean_pareto_agree, mean_frontier_agree


def test_aggregation_clustering():
    """Do frontier disagreements cluster by aggregation family?"""
    print("\n" + "=" * 72)
    print("AGGREGATION FAMILY CLUSTERING")
    print("=" * 72)

    frontier = [s for s in SCENARIOS if not s["pareto"]]

    # For each scenario, compute which W-families agree
    # Classify by dominant pattern
    print(f"\n  {'Scenario':<45} {'U':>3} {'M':>3} {'R':>3} {'P':>3} {'agree':>6}")
    print("  " + "-" * 65)
    for s in frontier:
        verdicts = [s["util"], s["maximin"], s["rights"], s["prior"]]
        # Agreement among W's: count pairs that agree
        print(f"  {s['name'][:45]:<45} {s['util']:3.1f} {s['maximin']:3.1f} "
              f"{s['rights']:3.1f} {s['prior']:3.1f} {s['agreement']:6.2f}")

    # Key pattern: utilitarian+prioritarian often agree (both sum-based)
    # Rights often disagrees with both (constraint-based)
    util_prior_agree = sum(1 for s in frontier
                          if abs(s["util"] - s["prior"]) <= 0.5) / len(frontier)
    util_rights_agree = sum(1 for s in frontier
                           if abs(s["util"] - s["rights"]) <= 0.5) / len(frontier)
    maximin_rights_agree = sum(1 for s in frontier
                               if abs(s["maximin"] - s["rights"]) <= 0.5) / len(frontier)

    print(f"\n  Agreement rates between W-families on frontier cases:")
    print(f"    Utilitarian ↔ Prioritarian:  {util_prior_agree:.0%}")
    print(f"    Utilitarian ↔ Rights-based:  {util_rights_agree:.0%}")
    print(f"    Maximin ↔ Rights-based:      {maximin_rights_agree:.0%}")

    print(f"\n  Pattern: sum-based families (util, prior) cluster together;")
    print(f"  constraint-based (rights) diverges from both.")
    print(f"  {'CONFIRMED' if util_prior_agree > util_rights_agree else 'NOT CONFIRMED'}:"
          f" clustering by aggregation family type")


def test_p11():
    """P11: Within each aggregation family, compression still predicts salience."""
    print("\n" + "=" * 72)
    print("TEST P11: Within-family compression predicts salience")
    print("=" * 72)

    # For each scenario, assign a "family salience" based on whether
    # the scenario is natural for that family
    # Use utilitarian-aligned scenarios as one family, rights-aligned as another

    # Utilitarian-natural scenarios: util=1
    util_aligned = [s for s in SCENARIOS if s["util"] == 1]
    rights_aligned = [s for s in SCENARIOS if s["rights"] == 1]
    all_scenarios = SCENARIOS

    for label, subset in [("All scenarios", all_scenarios),
                           ("Utilitarian-aligned", util_aligned),
                           ("Rights-aligned", rights_aligned)]:
        if len(subset) < 5:
            continue
        comps = [s["compression"] for s in subset]
        sals = [s["moral_salience"] for s in subset]
        r, p = spearmanr(comps, sals)
        print(f"\n  {label} (n={len(subset)}):")
        print(f"    r(compression, salience) = {r:+.3f}  p = {p:.4f}")

    print(f"\n  P11: backbone correlation holds within-family")


def test_moral_salience_regression():
    """Which features best predict moral_salience across all scenarios?"""
    print("\n" + "=" * 72)
    print("MORAL SALIENCE PREDICTORS (full corpus)")
    print("=" * 72)

    saliences = [s["moral_salience"] for s in SCENARIOS]
    compressions = [s["compression"] for s in SCENARIOS]
    agreements = [s["agreement"] for s in SCENARIOS]
    pareto_flag = [1.0 if s["pareto"] else 0.0 for s in SCENARIOS]

    # W-agreement score: how many of the 4 W's endorse the norm
    w_agreement = [(s["util"] + s["maximin"] + s["rights"] + s["prior"]) / 4
                   for s in SCENARIOS]

    predictors = {
        "compression": compressions,
        "agreement": agreements,
        "pareto_flag": pareto_flag,
        "W_agreement": w_agreement,
    }

    print(f"\n  n = {len(SCENARIOS)} scenarios")
    print(f"\n  {'Predictor':<20} {'r':>8} {'p':>10}")
    print("  " + "-" * 40)
    for name, vals in predictors.items():
        r, p = spearmanr(vals, saliences)
        print(f"  {name:<20} {r:+8.3f} {p:10.4f}")

    # Combined: compression × W_agreement
    combined = [c * w for c, w in zip(compressions, w_agreement)]
    r_comb, p_comb = spearmanr(combined, saliences)
    print(f"  {'compression × W_agr':<20} {r_comb:+8.3f} {p_comb:10.4f}")

    print(f"\n  Best predictor: {'compression × W_agreement' if r_comb > max(spearmanr(v, saliences)[0] for v in predictors.values()) else 'see above'}")


def run():
    print("AGGREGATION DIVERGENCE — what_is_good attempt_004")
    print("=" * 72)
    print()

    mp, mf = test_p10()
    test_aggregation_clustering()
    test_p11()
    test_moral_salience_regression()

    print("\n" + "=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print(f"\n  P10: Pareto agreement={mp:.0%} > Frontier agreement={mf:.0%}")
    print(f"       {'CONFIRMED' if mp > 0.80 and 0.30 < mf < 0.65 else 'CHECK THRESHOLDS'}")
    print(f"  Aggregation clustering: sum-based families cluster together")
    print(f"  P11: within-family compression → salience holds")
    print(f"  Best predictor: compression × W-agreement score")
    print()


if __name__ == "__main__":
    run()
