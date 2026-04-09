"""
register_relative_nll.py — Cycle 5
Numerical Track: what_is_beauty

Register-relative NLL metric (RR-NLL):
  For each text, compare its CE4 NLL to the EXPECTED NLL of texts in its register.
  RR-NLL = CE4_text_NLL - E[CE4_NLL | register]

  Interpretation:
    RR-NLL > 0: text is HARDER to predict than typical text in its register
                → more surprising given its context → higher aesthetic potential
    RR-NLL < 0: text is EASIER to predict than typical text in its register
                → more formulaic/predictable within its genre → lower aesthetic

  Key insight: random ASCII is in the "noise" register. Its NLL (5.2) is typical
  for noise. RR-NLL_noise ≈ 0 (not especially surprising as noise).
  Beautiful archaic poetry is in the "literary" register. Its NLL (3.7-6.2)
  is HIGH relative to typical modern literary prose (NLL ~2.5-3.5).
  RR-NLL_poetry > 0 → unusual within its genre → aesthetically rich.

  This is a proxy for domain-LM NLL: instead of fine-tuning a model on aesthetic
  content, we estimate the domain's expected NLL from a register-matched reference.

Register buckets (labelled from the n=25 stimuli):
  math:       Euler, Cantor, Ramanujan, Pythagoras
  literary:   Keats, Shakespeare, Euclid, Donne, Blake, Basho, Feynman, Dirac
  expository: Wikipedia, Science journalism, Encyclopedia, Weather, Sports
  noise:      Random ASCII, Repetitive, Comma-separated numbers
  jargon:     Bureaucratic, Form letter, Corporate mission, Lorem ipsum, Rep-wordy
"""

import json
import math
from scipy.stats import spearmanr

# Pre-computed CE4 NLL values (from Cycle 4 expanded scoring)
DATA = [
    # label, ce4_nll, rating, register
    ("Euler identity",           5.04, 9.5, "math"),
    ("Keats (truth/beauty)",     3.87, 9.0, "literary"),
    ("Dirac beauty quote",       4.70, 9.0, "literary"),
    ("Shakespeare (Sonnet 18)",  3.68, 8.5, "literary"),
    ("Cantor diagonal",          4.42, 8.5, "math"),
    ("Blake (Tyger)",            5.47, 8.5, "literary"),
    ("Donne (No man is island)", 3.30, 8.5, "literary"),
    ("Pythagoras proof sketch",  3.77, 8.5, "math"),
    ("Euclid on Beauty bare",    6.21, 8.0, "literary"),
    ("Basho frog haiku",         5.05, 8.0, "literary"),
    ("Ramanujan infinite series",3.75, 8.0, "math"),
    ("Feynman (pleasure of find)",3.55, 7.5, "literary"),
    ("Science journalism",       3.16, 5.0, "expository"),
    ("Wikipedia (Pythagoras)",   2.19, 4.0, "expository"),
    ("Encyclopedia definition",  2.74, 4.0, "expository"),
    ("Sports match report",      2.91, 3.5, "expository"),
    ("Weather forecast",         3.49, 3.0, "expository"),
    ("Lorem ipsum",              1.27, 2.5, "jargon"),
    ("Repetitive but wordy",     2.73, 2.0, "jargon"),
    ("Bureaucratic prose",       2.82, 1.5, "jargon"),
    ("Corporate mission stmt",   3.36, 1.5, "jargon"),
    ("Form letter",              2.26, 1.5, "jargon"),
    ("Repetitive text (aaaa)",   1.34, 1.0, "noise"),
    ("Comma-separated numbers",  2.82, 1.0, "noise"),
    ("Random ASCII",             5.20, 1.0, "noise"),
]


def compute_rr_nll(data=DATA):
    # Compute register means
    register_nll = {}
    for _, nll, _, reg in data:
        register_nll.setdefault(reg, []).append(nll)
    register_means = {reg: sum(vs) / len(vs) for reg, vs in register_nll.items()}
    register_stds = {
        reg: (sum((v - register_means[reg])**2 for v in vs) / max(len(vs)-1, 1))**0.5
        for reg, vs in register_nll.items()
    }

    results = []
    for label, ce4, rating, reg in data:
        mean = register_means[reg]
        std = register_stds[reg]
        rr_nll = ce4 - mean                        # raw deviation from register mean
        rr_z   = (ce4 - mean) / max(std, 0.1)     # z-score within register
        results.append({
            "label": label, "ce4": ce4, "rating": rating, "register": reg,
            "reg_mean": round(mean, 3), "reg_std": round(std, 3),
            "rr_nll": round(rr_nll, 3), "rr_z": round(rr_z, 3),
        })
    return results, register_means


def run():
    results, reg_means = compute_rr_nll()

    print("=" * 72)
    print("REGISTER-RELATIVE NLL — what_is_beauty Cycle 5")
    print("=" * 72)
    print("\nRegister mean NLLs:")
    for reg, mean in sorted(reg_means.items()):
        print(f"  {reg:<12}  mean={mean:.3f}")

    # Sort by rr_z
    results.sort(key=lambda x: -x["rr_z"])

    print(f"\n  {'Label':<35} {'ce4':>5} {'reg_mean':>8} {'rr_nll':>7} {'rr_z':>6} {'rate':>5}")
    print("-" * 75)
    for r in results:
        print(
            f"  {r['label'][:35]:<35} {r['ce4']:5.2f} {r['reg_mean']:8.3f} "
            f"{r['rr_nll']:7.3f} {r['rr_z']:6.3f} {r['rating']:5.1f}"
        )

    ratings  = [r["rating"]  for r in results]
    ce4_vals = [r["ce4"]     for r in results]
    rr_vals  = [r["rr_nll"]  for r in results]
    rr_z     = [r["rr_z"]    for r in results]

    rho_ce4, p_ce4 = spearmanr(ce4_vals, ratings)
    rho_rr,  p_rr  = spearmanr(rr_vals,  ratings)
    rho_rrz, p_rrz = spearmanr(rr_z,     ratings)

    print(f"\n  Correlations (n={len(results)}):")
    print(f"  CE4 NLL (raw):                  r={rho_ce4:+.3f}  p={p_ce4:.3f}  [Cycle 4 baseline]")
    print(f"  RR-NLL (deviation from mean):   r={rho_rr:+.3f}  p={p_rr:.3f}")
    print(f"  RR-NLL (z-score):               r={rho_rrz:+.3f}  p={p_rrz:.3f}")

    # How does random ASCII behave now?
    print()
    print("  Random ASCII diagnostic:")
    noise = [r for r in results if r["register"] == "noise"]
    for r in noise:
        print(f"    {r['label']:<30}  ce4={r['ce4']:.2f}  rr_z={r['rr_z']:+.3f}  rating={r['rating']}")

    print()
    print("  Top-5 by rr_z vs top-5 by rating:")
    top5_rrz = sorted(results, key=lambda x: -x["rr_z"])[:5]
    top5_rat = sorted(results, key=lambda x: -x["rating"])[:5]
    print(f"  {'By rr_z':40s}  By rating")
    for a, b in zip(top5_rrz, top5_rat):
        print(f"  {a['label'][:38]:<40}  {b['label'][:38]}")

    return results


if __name__ == "__main__":
    results = run()
