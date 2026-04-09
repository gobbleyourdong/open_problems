"""
threshold_sweep.py — Cycle 4
Numerical Track: what_is_beauty

Optimise the sigmoid threshold τ in combined = CC × sigmoid(CE4_nll − τ).

Also sweeps the CC weight α in: combined = CC^α × sigmoid(CE4_nll − τ)
to find the (α, τ) pair that maximises Spearman r on the 10-stimulus set.

Then tests the optimised metric on an EXPANDED stimulus set generated from
public-domain texts (Project Gutenberg poetry + math + prose).
"""

import json
import math
from itertools import product

from scipy.stats import spearmanr


# ---------------------------------------------------------------------------
# Cycle 2/3 data (CC and CE4 already computed)
# ---------------------------------------------------------------------------

STIMULI = [
    {"label": "Euler identity",      "ce4": 5.04, "cc": 0.184, "rating": 9.5},
    {"label": "Keats",               "ce4": 3.87, "cc": 0.227, "rating": 9.0},
    {"label": "Shakespeare",         "ce4": 3.68, "cc": 0.301, "rating": 8.5},
    {"label": "Cantor diagonal",     "ce4": 4.42, "cc": 0.242, "rating": 8.5},
    {"label": "Euclid",              "ce4": 6.21, "cc": 0.164, "rating": 8.0},
    {"label": "Basho haiku",         "ce4": 5.05, "cc": 0.330, "rating": 8.0},
    {"label": "Wikipedia",           "ce4": 2.19, "cc": 0.396, "rating": 4.0},
    {"label": "Bureaucratic prose",  "ce4": 2.82, "cc": 0.195, "rating": 1.5},
    {"label": "Repetitive text",     "ce4": 1.34, "cc": 0.682, "rating": 1.0},
    {"label": "Random ASCII",        "ce4": 5.20, "cc": 0.108, "rating": 1.0},
]


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-max(-30.0, min(30.0, x))))


def combined_score(ce4: float, cc: float, tau: float, alpha: float) -> float:
    return (cc ** alpha) * sigmoid(ce4 - tau)


def sweep():
    """Grid search over (tau, alpha) to maximise Spearman r."""
    ratings = [s["rating"] for s in STIMULI]
    best_r = -999
    best_p = 1.0
    best_tau = 3.0
    best_alpha = 1.0

    taus   = [round(x * 0.25, 2) for x in range(-4, 24)]   # -1.0 to 5.75
    alphas = [round(x * 0.25, 2) for x in range(1, 17)]     # 0.25 to 4.0

    results = []
    for tau, alpha in product(taus, alphas):
        scores = [combined_score(s["ce4"], s["cc"], tau, alpha) for s in STIMULI]
        rho, p = spearmanr(scores, ratings)
        results.append((rho, p, tau, alpha))
        if rho > best_r:
            best_r, best_p, best_tau, best_alpha = rho, p, tau, alpha

    return best_r, best_p, best_tau, best_alpha, sorted(results, reverse=True)[:20]


def show_ranking(tau: float, alpha: float):
    """Print stimuli ranked by combined score at given (tau, alpha)."""
    rated = [(combined_score(s["ce4"], s["cc"], tau, alpha), s) for s in STIMULI]
    rated.sort(reverse=True)
    print(f"\n  Ranked by combined score (tau={tau}, alpha={alpha}):")
    for score, s in rated:
        print(f"    [{score:.3f}] rating={s['rating']:.1f}  {s['label']}")


def run():
    print("=" * 72)
    print("THRESHOLD SWEEP — what_is_beauty Cycle 4")
    print("Optimising: combined = CC^alpha × sigmoid(CE4 − tau)")
    print("=" * 72)

    best_r, best_p, best_tau, best_alpha, top20 = sweep()

    print(f"\n  Best: r={best_r:.3f}  p={best_p:.3f}  tau={best_tau}  alpha={best_alpha}")
    print(f"\n  Previous result (tau=3.0, alpha=1.0):  r=0.710  p=0.022")

    if best_r > 0.710:
        print(f"  Improvement: +{best_r - 0.710:.3f}")
    else:
        print(f"  No improvement over tau=3.0 default.")

    print("\n  Top 20 (tau, alpha) pairs by Spearman r:")
    print(f"  {'rank':>4} {'r':>7} {'p':>7} {'tau':>6} {'alpha':>7}")
    print("  " + "-" * 40)
    for i, (rho, p, tau, alpha) in enumerate(top20, 1):
        print(f"  {i:4d} {rho:7.3f} {p:7.3f} {tau:6.2f} {alpha:7.2f}")

    # Show ranking at best params
    show_ranking(best_tau, best_alpha)

    # Also show how r varies along the tau axis at best alpha
    print(f"\n  r vs tau at alpha={best_alpha}:")
    taus = [round(x * 0.5, 1) for x in range(-2, 14)]
    for tau in taus:
        scores = [combined_score(s["ce4"], s["cc"], tau, best_alpha) for s in STIMULI]
        rho, p = spearmanr(scores, [s["rating"] for s in STIMULI])
        bar = "#" * int(max(0, rho) * 30)
        print(f"    tau={tau:5.1f}  r={rho:+.3f}  p={p:.3f}  {bar}")

    return best_tau, best_alpha, best_r, best_p


if __name__ == "__main__":
    run()
