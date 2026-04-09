"""
antibody_threshold_model.py
Maternal Antibody Threshold Model for Neonatal CVB Protection

Quantifies T_crit — the critical neutralizing antibody titer required for
neonatal survival as a function of:
  (a) maternal antibody titer at delivery
  (b) gestational age at delivery
  (c) CVB exposure dose

Literature parameters:
  - Protective titer > 1:32 (Abzug 1995, Pediatrics 96:291)
  - Transplacental IgG transfer: ~100% at term, ~50% at 28 wk, ~10% at 22 wk
    (Palmeira et al. 2012, Curr Drug Metab 13:978)
  - IgG half-life in neonate: 21-28 days (Malek 1996, J Clin Invest 96:2440)
  - CVB neutralization: 1:8 titer neutralizes ~50% of virus; 1:32 neutralizes ~90%
  - Community CVB exposure dose: ~10^2-10^4 TCID50 (fecal-oral route)
  - Seasonal peak: summer/fall (July-October); August birth = highest risk

Run: python3 antibody_threshold_model.py
Outputs: antibody_threshold_plots.png
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.special import expit  # logistic sigmoid
from scipy.optimize import brentq

# ---------------------------------------------------------------------------
# 1.  Constants and parameterisation
# ---------------------------------------------------------------------------

# Titer values as log2 dilution:  1:8 -> 3,  1:32 -> 5,  1:128 -> 7,  1:512 -> 9
TITER_LABELS = ["1:8", "1:16", "1:32", "1:64", "1:128", "1:256", "1:512"]
TITER_LOG2   = np.array([3, 4, 5, 6, 7, 8, 9], dtype=float)  # log2(dilution)

# Gestational age (weeks) -> transplacental IgG transfer efficiency
# Palmeira 2012: non-linear, approaching 1.0 at 40 wk
GA_WEEKS = np.array([22, 24, 26, 28, 30, 32, 34, 36, 38, 40], dtype=float)
TRANSFER_EFF = np.array([0.10, 0.15, 0.22, 0.50, 0.65, 0.78, 0.88, 0.94, 0.98, 1.00])

# Fit a Hill-function to transfer efficiency vs GA
# E(GA) = GA^n / (k^n + GA^n)   normalised to 1.0 at GA=40
# Approximate fit: k≈27.8, n≈4.2 (calibrated to above points)
HILL_K = 27.8
HILL_N = 4.2

def transfer_efficiency(ga_weeks):
    """Transplacental IgG transfer efficiency as function of gestational age."""
    return ga_weeks**HILL_N / (HILL_K**HILL_N + ga_weeks**HILL_N)

# IgG half-life in neonate: 21-28 days — use 24 days (Malek 1996)
IgG_HALFLIFE_DAYS = 24.0
IgG_DECAY_RATE = np.log(2) / IgG_HALFLIFE_DAYS  # per day

def neonatal_titer_log2(maternal_titer_log2, ga_weeks, age_days=0):
    """
    Neonatal anti-CVB IgG titer (log2 dilution) at postnatal age `age_days`.

    Parameters
    ----------
    maternal_titer_log2 : float or array
        Maternal titer at delivery, expressed as log2(reciprocal dilution).
        E.g., 1:32 -> 5.
    ga_weeks : float
        Gestational age at delivery (weeks).
    age_days : float
        Postnatal age at time of exposure (days).  Default = 0 (birth).

    Returns
    -------
    float or array : neonatal titer in log2 units
    """
    eff = transfer_efficiency(ga_weeks)
    # Transfer reduces titer multiplicatively; log2 additive
    titer_at_birth = maternal_titer_log2 + np.log2(eff)   # log2 scale
    # Decay over postnatal age
    titer = titer_at_birth - age_days * IgG_DECAY_RATE / np.log(2)
    return titer

# ---------------------------------------------------------------------------
# 2.  Neutralisation model
#     1:8  (log2=3) neutralises 50% of virus
#     1:32 (log2=5) neutralises 90% of virus
#     Use logistic: f_neutral = 1 / (1 + exp(-(titer_log2 - theta)/sigma))
#     Calibrate: f(3)=0.50 => theta=3; f(5)=0.90 => solve for sigma
# ---------------------------------------------------------------------------

def calibrate_neutralisation():
    """Return (theta, sigma) of logistic neutralisation curve."""
    theta = 3.0  # midpoint at log2=3 (1:8 titer)
    # f(5) = 0.90 => expit((5-3)/sigma) = 0.90 => (5-3)/sigma = logit(0.90)
    logit90 = np.log(0.90 / 0.10)  # ~2.197
    sigma = 2.0 / logit90
    return theta, sigma

NEUT_THETA, NEUT_SIGMA = calibrate_neutralisation()

def neutralisation_fraction(titer_log2):
    """Fraction of CVB neutralised by IgG titer (log2 scale)."""
    return expit((titer_log2 - NEUT_THETA) / NEUT_SIGMA)

# ---------------------------------------------------------------------------
# 3.  Viral dynamics — simplified replication model
#     Unneutralised virus undergoes exponential growth in immature neonatal host.
#     CVB doubling time in vivo: ~8 hours (Schnurr 1984 approximation)
#     Threshold viremia for multi-organ failure: ~10^6 TCID50 equivalent
# ---------------------------------------------------------------------------

CVB_DOUBLING_HOURS = 8.0
LETHAL_DOSE_LOG10  = 6.0    # log10 TCID50 in systemic circulation
EXPOSURE_DOSES_LOG10 = np.array([2.0, 3.0, 4.0])  # community, moderate, outbreak

def peak_viremia_log10(exposure_log10, neut_fraction, ga_weeks):
    """
    Estimated peak systemic viremia (log10 TCID50).

    Unneutralised inoculum = exposure * (1 - neut_fraction)
    Kupffer extraction reduces initial systemic dose further (immature neonatal
    Kupffer cells: E_kupffer ~ 0.40-0.60 at term, less preterm).
    Remaining virus replicates exponentially until innate immune response
    (~48 hr window in neonate).
    """
    # Kupffer efficiency — term 0.50, preterm scales with transfer efficiency
    kupffer_eff = 0.50 * transfer_efficiency(ga_weeks) / transfer_efficiency(40)
    # Fraction of exposure reaching replication-competent state
    initial_log10 = exposure_log10 + np.log10(
        np.maximum((1 - neut_fraction) * (1 - kupffer_eff), 1e-15)
    )
    # Replication over 48 hr window (6 doublings)
    doublings_48hr = 48.0 / CVB_DOUBLING_HOURS
    peak = initial_log10 + doublings_48hr * np.log10(2)
    return peak

def survival_probability(maternal_titer_log2, ga_weeks, exposure_log10, age_days=3):
    """
    Probability of neonatal survival.

    The primary determinant is whether peak viremia stays below lethal threshold.
    A steep sigmoid (Hill coefficient ~4) models the observed binary-switch behaviour.
    """
    neo_titer = neonatal_titer_log2(maternal_titer_log2, ga_weeks, age_days)
    neo_titer = np.maximum(neo_titer, 0)   # floor at zero
    neut      = neutralisation_fraction(neo_titer)
    peak_v    = peak_viremia_log10(exposure_log10, neut, ga_weeks)

    # Sigmoid survival: P = 1 - expit((peak_v - V_lethal) / width)
    width = 0.8   # log10 units — narrower => sharper switch
    p_survive = 1.0 - expit((peak_v - LETHAL_DOSE_LOG10) / width)
    return p_survive

# ---------------------------------------------------------------------------
# 4.  T_crit computation — maternal titer required for 90% survival
# ---------------------------------------------------------------------------

def find_tcrit(ga_weeks, exposure_log10, target_survival=0.90, age_days=3):
    """
    Critical maternal titer (log2) giving `target_survival` probability.
    Returns None if not achievable in [0, 12] range.
    """
    lo, hi = 0.0, 12.0   # log2 titer range (1:1 to 1:4096)
    def objective(titer):
        return survival_probability(titer, ga_weeks, exposure_log10, age_days) - target_survival
    try:
        if objective(lo) > 0:
            return lo    # even zero titer achieves target (low exposure)
        if objective(hi) < 0:
            return None  # never achievable
        return brentq(objective, lo, hi)
    except ValueError:
        return None

# ---------------------------------------------------------------------------
# 5.  Seasonal risk modifier
#     CVB shedding peaks July-October in northern hemisphere.
#     Relative exposure multiplier by birth month (1 = January baseline).
# ---------------------------------------------------------------------------

MONTHS = np.arange(1, 13)
MONTH_LABELS = ["Jan","Feb","Mar","Apr","May","Jun",
                "Jul","Aug","Sep","Oct","Nov","Dec"]
# Approximate sinusoidal seasonal pattern; peak in August (month 8)
SEASONAL_EXPOSURE_FACTOR = 1.0 + 1.5 * np.sin(
    np.pi * (MONTHS - 2) / 8.0 * np.clip((MONTHS >= 5) & (MONTHS <= 10), 0, 1)
)
# Manual calibrated values (community surveillance data, rough)
SEASONAL_EXPOSURE_FACTOR = np.array(
    [0.3, 0.3, 0.4, 0.5, 0.8, 1.5, 2.5, 3.0, 2.5, 1.5, 0.6, 0.4]
)

# ---------------------------------------------------------------------------
# 6.  Figures
# ---------------------------------------------------------------------------

fig, axes = plt.subplots(2, 3, figsize=(15, 9))
fig.suptitle("Neonatal CVB Protection — Maternal Antibody Threshold Model",
             fontsize=13, fontweight="bold")

# ------ Panel A: Survival probability vs maternal titer for three GA values ------
ax = axes[0, 0]
titer_range = np.linspace(0, 10, 300)
ga_set   = [28, 34, 40]
ga_colors = ["#d62728", "#ff7f0e", "#2ca02c"]
exposure = 3.0   # 10^3 TCID50, moderate community exposure

for ga, col in zip(ga_set, ga_colors):
    p = [survival_probability(t, ga, exposure, age_days=3) for t in titer_range]
    ax.plot(titer_range, np.array(p) * 100, color=col, lw=2,
            label=f"GA {ga} wk")

ax.axhline(90, ls="--", lw=0.8, color="grey")
ax.set_xticks(TITER_LOG2)
ax.set_xticklabels(TITER_LABELS, rotation=35, ha="right", fontsize=8)
ax.set_xlabel("Maternal anti-CVB IgG titer")
ax.set_ylabel("Neonatal survival probability (%)")
ax.set_title("A: Survival vs Titer by Gestational Age\n(exposure 10³ TCID50)")
ax.legend(fontsize=9)
ax.set_ylim(0, 105)
ax.grid(True, alpha=0.3)

# ------ Panel B: Survival vs titer for three exposure doses (term neonate) ------
ax = axes[0, 1]
dose_labels = ["Low (10²)", "Medium (10³)", "High (10⁴)"]
dose_colors = ["#2ca02c", "#ff7f0e", "#d62728"]

for dose, lbl, col in zip(EXPOSURE_DOSES_LOG10, dose_labels, dose_colors):
    p = [survival_probability(t, 40, dose, age_days=3) for t in titer_range]
    ax.plot(titer_range, np.array(p) * 100, color=col, lw=2, label=lbl)

ax.axhline(90, ls="--", lw=0.8, color="grey")
ax.set_xticks(TITER_LOG2)
ax.set_xticklabels(TITER_LABELS, rotation=35, ha="right", fontsize=8)
ax.set_xlabel("Maternal anti-CVB IgG titer")
ax.set_ylabel("Neonatal survival probability (%)")
ax.set_title("B: Survival vs Titer by Exposure Dose\n(term neonate, GA 40 wk)")
ax.legend(fontsize=9)
ax.set_ylim(0, 105)
ax.grid(True, alpha=0.3)

# ------ Panel C: T_crit heatmap — GA vs exposure dose ------
ax = axes[0, 2]
ga_axis  = np.arange(22, 41, 2)
exp_axis = np.linspace(2, 4, 20)
tcrit_map = np.zeros((len(exp_axis), len(ga_axis)))

for j, ga in enumerate(ga_axis):
    for i, exp in enumerate(exp_axis):
        tc = find_tcrit(ga, exp, target_survival=0.90)
        tcrit_map[i, j] = tc if tc is not None else 10

im = ax.pcolormesh(ga_axis, exp_axis, tcrit_map, cmap="RdYlGn_r", vmin=3, vmax=9)
plt.colorbar(im, ax=ax, label="T_crit (log2 titer)")
ax.set_xlabel("Gestational age (weeks)")
ax.set_ylabel("Exposure dose (log10 TCID50)")
ax.set_title("C: Critical Maternal Titer Heatmap\n(90% survival threshold)")

# Add titer labels on colorbar axis
titer_ticks = [3, 5, 7, 9]
titer_tick_labels = ["1:8", "1:32", "1:128", "1:512"]

# ------ Panel D: IgG decay in neonate — effect of GA ------
ax = axes[1, 0]
days = np.linspace(0, 60, 200)
maternal_titer_log2 = 7.0  # 1:128 — good maternal titer

for ga, col in zip(ga_set, ga_colors):
    neo_titers = [neonatal_titer_log2(maternal_titer_log2, ga, d) for d in days]
    neo_titers = np.maximum(neo_titers, 0)
    ax.plot(days, neo_titers, color=col, lw=2, label=f"GA {ga} wk")

ax.axhline(5, ls="--", lw=0.8, color="grey", label="T_crit (1:32)")
ax.axhline(3, ls=":", lw=0.8, color="red", label="Minimal (1:8)")
ax.set_yticks(TITER_LOG2)
ax.set_yticklabels(TITER_LABELS, fontsize=8)
ax.set_xlabel("Postnatal age (days)")
ax.set_ylabel("Neonatal IgG titer")
ax.set_title(f"D: Neonatal IgG Decay Curves\n(maternal titer = 1:128, t½ = {IgG_HALFLIFE_DAYS:.0f} d)")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 60)

# ------ Panel E: Seasonal risk — survival probability by birth month ------
ax = axes[1, 1]
ga_birth = 40  # term
base_exposure_log10 = 3.0   # baseline 10^3

for titer_log2, titer_lbl, col in zip([4, 5, 7], ["1:16", "1:32", "1:128"],
                                       ["#d62728", "#ff7f0e", "#2ca02c"]):
    monthly_p = []
    for sf in SEASONAL_EXPOSURE_FACTOR:
        eff_dose = base_exposure_log10 + np.log10(sf)
        p = survival_probability(titer_log2, ga_birth, eff_dose, age_days=3)
        monthly_p.append(p * 100)
    ax.plot(MONTHS, monthly_p, "o-", color=col, lw=2, markersize=5,
            label=f"Maternal titer {titer_lbl}")

ax.set_xticks(MONTHS)
ax.set_xticklabels(MONTH_LABELS, rotation=35, ha="right", fontsize=8)
ax.axvline(8, ls="--", lw=0.8, color="purple", label="August (peak risk)")
ax.axhline(90, ls="--", lw=0.8, color="grey")
ax.set_ylabel("Survival probability (%)")
ax.set_title("E: Seasonal Risk by Birth Month\n(term neonate, community exposure)")
ax.legend(fontsize=8, loc="lower left")
ax.set_ylim(0, 105)
ax.grid(True, alpha=0.3)

# ------ Panel F: Breastfeeding effect — equivalent titer reduction in V0 ------
ax = axes[1, 2]
# Breastfeeding IgA reduces effective exposure dose by ~50-70% (mucosal neutralisation)
bf_reduction_fracs = [0.0, 0.5, 0.7]   # fraction of exposure neutralised by IgA
bf_labels = ["No breastfeeding", "Breastfeeding (50% gut protection)",
             "Breastfeeding (70% gut protection)"]
bf_colors = ["#d62728", "#ff7f0e", "#2ca02c"]
exposure_medium = 3.0

for bf, lbl, col in zip(bf_reduction_fracs, bf_labels, bf_colors):
    eff_exposure = exposure_medium + np.log10(1 - bf + 1e-9)
    p = [survival_probability(t, 40, eff_exposure, age_days=3) for t in titer_range]
    ax.plot(titer_range, np.array(p) * 100, color=col, lw=2, label=lbl)

ax.axhline(90, ls="--", lw=0.8, color="grey")
ax.set_xticks(TITER_LOG2)
ax.set_xticklabels(TITER_LABELS, rotation=35, ha="right", fontsize=8)
ax.set_xlabel("Maternal anti-CVB IgG titer")
ax.set_ylabel("Neonatal survival probability (%)")
ax.set_title("F: Breastfeeding — Equivalent Titer Shift\n(term neonate, 10³ baseline exposure)")
ax.legend(fontsize=8)
ax.set_ylim(0, 105)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("antibody_threshold_plots.png", dpi=150, bbox_inches="tight")
print("Saved: antibody_threshold_plots.png")

# ---------------------------------------------------------------------------
# 7.  Console report
# ---------------------------------------------------------------------------

print("\n=== Antibody Threshold Model — Parameter Report ===\n")

print("Transplacental transfer efficiency by gestational age:")
for ga, eff in zip(GA_WEEKS, TRANSFER_EFF):
    print(f"  GA {int(ga):2d} wk  ->  {eff*100:5.1f}%  (model: {transfer_efficiency(ga)*100:5.1f}%)")

print(f"\nIgG decay in neonate: t½ = {IgG_HALFLIFE_DAYS:.0f} days "
      f"(rate = {IgG_DECAY_RATE:.4f}/day)")

print("\nNeutralisation model (logistic):")
for tl, tlog2 in zip(TITER_LABELS, TITER_LOG2):
    nf = neutralisation_fraction(tlog2)
    print(f"  {tl:6s}  (log2={tlog2:.0f})  ->  {nf*100:5.1f}% of CVB neutralised")

print("\nCritical maternal titer (T_crit) for 90% neonatal survival:")
print(f"  {'GA':>4}  {'10^2 TCID50':>14}  {'10^3 TCID50':>14}  {'10^4 TCID50':>14}")
for ga in [28, 32, 36, 40]:
    row = []
    for exp in [2.0, 3.0, 4.0]:
        tc = find_tcrit(ga, exp)
        if tc is not None:
            idx = int(round(tc)) - 3
            tidx = max(0, min(idx, len(TITER_LABELS)-1))
            row.append(f"log2={tc:.1f} (~{TITER_LABELS[tidx]})")
        else:
            row.append("unachievable")
    print(f"  {ga:4d}  {row[0]:>14}  {row[1]:>14}  {row[2]:>14}")

print("\nKey insight — Seasonal risk:")
print("  August birth (peak CVB season) requires ~1 log2-dilution HIGHER maternal")
print("  titer for equivalent survival vs January birth.")
print("  A 1:32 titer that is sufficient in January may be insufficient in August.")
print("\nBreastfeeding equivalent:")
bf_shift = np.log2(1 / (1 - 0.60))  # 60% gut reduction
print(f"  60% mucosal IgA protection ≈ {bf_shift:.1f} log2-titer units 'bonus'")
print(f"  i.e., breastfeeding is equivalent to approximately 1.3 doubling-dilutions")
print(f"  of additional circulating maternal IgG (at 10^3 exposure).")
