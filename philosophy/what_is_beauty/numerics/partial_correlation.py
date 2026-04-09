"""
partial_correlation.py — Cycle 5
Numerical Track: what_is_beauty

Two analyses:
  A. Partial correlation: what is r(CE4, rating | register), controlling for register?
     If CE4 is purely a register-prestige effect, this partial r should be near 0.
     If CE4 carries a genuine within-register aesthetic signal, partial r > 0.

  B. Within-register regression:
     For each register separately, compute r(CE4, rating).
     If CE4 works within registers, these should be positive.
     If CE4 is purely a between-register effect, these should be near 0.

  Result will answer: is the CE4-aesthetics correlation a genuine aesthetic signal
  or entirely driven by register assignment?
"""

import math
from scipy.stats import spearmanr, pearsonr
import numpy as np

DATA = [
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

REGISTERS = ["math", "literary", "expository", "jargon", "noise"]
REG_TO_INT = {r: i for i, r in enumerate(REGISTERS)}


def partial_corr_controlling_register(data=DATA):
    """
    Partial correlation r(CE4, rating | register) using residuals from
    within-register mean (demeaning by register).
    """
    regs = [d[3] for d in data]
    ce4s = [d[1] for d in data]
    rats = [d[2] for d in data]

    # Compute register means for CE4 and rating
    reg_ce4_mean = {}
    reg_rat_mean = {}
    for reg in REGISTERS:
        sub = [(ce4, rat) for _, ce4, rat, r in data if r == reg]
        if sub:
            reg_ce4_mean[reg] = sum(x[0] for x in sub) / len(sub)
            reg_rat_mean[reg] = sum(x[1] for x in sub) / len(sub)

    # Residuals = actual - register mean
    ce4_resid = [ce4 - reg_ce4_mean[reg] for _, ce4, _, reg in data]
    rat_resid = [rat - reg_rat_mean[reg] for _, _, rat, reg in data]

    rho, p = spearmanr(ce4_resid, rat_resid)
    rho_p, p_p = pearsonr(ce4_resid, rat_resid)
    return rho, p, rho_p, p_p, ce4_resid, rat_resid


def within_register_corr(data=DATA):
    """r(CE4, rating) computed within each register separately."""
    results = {}
    for reg in REGISTERS:
        sub = [(ce4, rat) for _, ce4, rat, r in data if r == reg]
        if len(sub) < 3:
            results[reg] = {"n": len(sub), "r": None, "p": None}
            continue
        ce4s = [x[0] for x in sub]
        rats = [x[1] for x in sub]
        rho, p = spearmanr(ce4s, rats)
        results[reg] = {"n": len(sub), "r": round(rho, 3), "p": round(p, 3)}
    return results


def between_register_analysis(data=DATA):
    """Show register-level means: is the CE4-rating correlation between registers?"""
    regs = REGISTERS
    reg_ce4_mean = {}
    reg_rat_mean = {}
    for reg in regs:
        sub = [(ce4, rat) for _, ce4, rat, r in data if r == reg]
        if sub:
            reg_ce4_mean[reg] = sum(x[0] for x in sub) / len(sub)
            reg_rat_mean[reg] = sum(x[1] for x in sub) / len(sub)

    reg_ce4s = [reg_ce4_mean[r] for r in regs if r in reg_ce4_mean]
    reg_rats = [reg_rat_mean[r] for r in regs if r in reg_rat_mean]
    rho, p = spearmanr(reg_ce4s, reg_rats)
    return reg_ce4_mean, reg_rat_mean, rho, p


def run():
    print("=" * 72)
    print("PARTIAL CORRELATION ANALYSIS — what_is_beauty Cycle 5")
    print("Is CE4→rating correlation within or between registers?")
    print("=" * 72)

    # Between-register signal
    reg_ce4, reg_rat, rho_bet, p_bet = between_register_analysis()
    print("\nA. Between-register signal:")
    print(f"  Register means:  {'Register':<14} CE4_mean  Rating_mean")
    for reg in REGISTERS:
        if reg in reg_ce4:
            print(f"    {reg:<14} {reg_ce4[reg]:.3f}     {reg_rat[reg]:.1f}")
    print(f"  r(register_CE4_mean, register_rating_mean) = {rho_bet:+.3f}  p={p_bet:.3f}")

    # Within-register signal
    print("\nB. Within-register correlations r(CE4, rating | same register):")
    within = within_register_corr()
    for reg, res in within.items():
        r_str = f"{res['r']:+.3f}" if res["r"] is not None else "  N/A"
        p_str = f"{res['p']:.3f}" if res["p"] is not None else "  N/A"
        print(f"  {reg:<14}  n={res['n']}  r={r_str}  p={p_str}")

    # Partial correlation
    rho, p, rho_p, p_p, ce4_r, rat_r = partial_corr_controlling_register()
    print(f"\nC. Partial correlation r(CE4, rating | register demeaned):")
    print(f"  Spearman  r={rho:+.3f}  p={p:.3f}")
    print(f"  Pearson   r={rho_p:+.3f}  p={p_p:.3f}")

    # Show residuals for key stimuli
    print("\n  Largest residual pairs (CE4 resid, rating resid):")
    items = sorted(
        zip(ce4_r, rat_r, [d[0] for d in DATA], [d[2] for d in DATA]),
        key=lambda x: abs(x[0]) + abs(x[1]), reverse=True
    )[:8]
    for cr, rr, label, rating in items:
        print(f"    {label[:35]:<35}  CE4_resid={cr:+.3f}  rat_resid={rr:+.2f}")

    print()
    print("D. Interpretation:")
    print(f"  Full r(CE4, rating)          = +0.606 (n=25)")
    print(f"  Between-register r           = {rho_bet:+.3f}")
    print(f"  Within-register partial r    = {rho:+.3f}")
    if abs(rho) < 0.2:
        print("  → CE4-rating correlation is PRIMARILY a between-register effect.")
        print("    CE4 measures register prestige, not within-register aesthetic quality.")
        print("    The true compression-beauty signal requires a domain-specific prior.")
    else:
        print("  → CE4 carries a genuine within-register aesthetic signal (partial r > 0.2).")


if __name__ == "__main__":
    run()
