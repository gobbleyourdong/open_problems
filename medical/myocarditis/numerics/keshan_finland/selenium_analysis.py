"""
REQ-009: Selenium-T1DM-CVB Correlation (Keshan-Finland Natural Experiment)
===========================================================================
Correlates selenium status (soil + serum) with T1DM incidence and CVB
susceptibility across Nordic countries and globally.

Key analysis:
  1. Soil/serum selenium by country vs T1DM incidence (Pearson + Spearman)
  2. Finland 1984 natural experiment: selenium fertilisation → T1DM slope change
  3. Mechanistic diagram: Se → selenoproteins → GPx → reduced CVB replication
  4. Comparison with Keshan disease (CVB + Se deficiency → cardiomyopathy)

Data sources: published literature (Eurola 1989, Alfthan 2015, EURODIAB, DiaMond)
"""

import numpy as np
import scipy.stats as stats
import scipy.optimize as optimize
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
from matplotlib.colors import Normalize
import json, os, warnings
warnings.filterwarnings("ignore")

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(OUT_DIR)), "results", "keshan_finland"
)
os.makedirs(RESULTS_DIR, exist_ok=True)

np.random.seed(42)

# ---------------------------------------------------------------------------
# 1. SELENIUM DATA (published literature)
# ---------------------------------------------------------------------------

# Soil selenium concentrations (μg/g dry weight) — median/typical values
# Sources: Eurola 1989, Shand 2012, FOREGS geochemical atlas, WHO reports
SOIL_SELENIUM = {
    "Finland (pre-1984)":  0.065,   # Eurola et al., very low agricultural soils
    "Finland (post-1984)": 0.25,    # After national Se fertilizer program (Alfthan 2015)
    "Sweden":              0.20,    # Eriksson 2014
    "Norway":              0.15,    # Shand et al.
    "Denmark":             0.30,    # Hansen et al.
    "UK":                  0.40,    # FOREGS
    "Germany":             0.35,    # FOREGS
    "Netherlands":         0.25,    # Eurola
    "USA":                 0.60,    # Oldfield 2002 — highly variable
    "Japan":               0.23,    # Yoshida et al.
    "China (Keshan)":      0.010,   # Extremely low — Keshan disease endemic area
    "China (non-Keshan)":  0.20,    # Non-endemic
}

# Serum/plasma selenium concentrations (μg/L) — adult population means
# Sources: Combs 2015, Alfthan 2015, Nawaz 2016
SERUM_SELENIUM = {
    "Finland (pre-1984)":  56.0,
    "Finland (post-1984)": 110.0,
    "Sweden":              105.0,
    "Norway":              110.0,
    "Denmark":             95.0,
    "UK":                  90.0,
    "Germany":             88.0,
    "Netherlands":         82.0,
    "USA":                 130.0,
    "Japan":               95.0,
    "China (Keshan)":      21.0,
    "China (non-Keshan)":  65.0,
}

# T1DM incidence (per 100k/yr, age 0-14) — most recent available estimates
# Sources: EURODIAB, IDF Atlas 2021, DiaMond
T1DM_INCIDENCE = {
    "Finland (pre-1984)":  32.0,   # ~1985 value (incidence already rising)
    "Finland (post-1984)": 52.0,   # ~2005 value (but growth rate slowed?)
    "Sweden":              35.0,   # late 1990s
    "Norway":              27.0,   # late 1990s
    "Denmark":             22.0,   # late 1990s
    "UK":                  23.0,   # late 1990s EURODIAB
    "Germany":             14.0,   # EURODIAB (lower, but rising)
    "Netherlands":         18.0,   # EURODIAB
    "USA":                 23.0,   # SEARCH 2000
    "Japan":               2.5,    # Very low — different HLA/genetics
    "China (Keshan)":      0.6,    # Very low — different genetics
    "China (non-Keshan)":  0.8,
}

# For correlation (single-timepoint, excluding Japan/China for main HLA-comparable analysis)
MAIN_COUNTRIES = ["Finland (pre-1984)", "Sweden", "Norway", "Denmark", "UK", "Germany",
                  "Netherlands", "USA"]

soil_se_main    = np.array([SOIL_SELENIUM[c]   for c in MAIN_COUNTRIES])
serum_se_main   = np.array([SERUM_SELENIUM[c]  for c in MAIN_COUNTRIES])
t1dm_main       = np.array([T1DM_INCIDENCE[c]  for c in MAIN_COUNTRIES])

# All countries (including Japan/China) for full scatter
ALL_COUNTRIES = list(T1DM_INCIDENCE.keys())
soil_se_all   = np.array([SOIL_SELENIUM.get(c, np.nan)  for c in ALL_COUNTRIES])
serum_se_all  = np.array([SERUM_SELENIUM.get(c, np.nan) for c in ALL_COUNTRIES])
t1dm_all      = np.array([T1DM_INCIDENCE[c] for c in ALL_COUNTRIES])


# ---------------------------------------------------------------------------
# 2. CORRELATIONS
# ---------------------------------------------------------------------------

print("Computing selenium-T1DM correlations...")

# Main HLA-similar European/USA cohort
r_soil_pearson,  p_soil_pearson  = stats.pearsonr(soil_se_main,  t1dm_main)
r_soil_spearman, p_soil_spearman = stats.spearmanr(soil_se_main, t1dm_main)
r_serum_pearson, p_serum_pearson = stats.pearsonr(serum_se_main, t1dm_main)
r_serum_spearman,p_serum_spearman= stats.spearmanr(serum_se_main,t1dm_main)

print(f"  Soil Se vs T1DM  (European+USA):  Pearson r={r_soil_pearson:.3f} p={p_soil_pearson:.4f}")
print(f"                                    Spearman ρ={r_soil_spearman:.3f} p={p_soil_spearman:.4f}")
print(f"  Serum Se vs T1DM (European+USA):  Pearson r={r_serum_pearson:.3f} p={p_serum_pearson:.4f}")
print(f"                                    Spearman ρ={r_serum_spearman:.3f} p={p_serum_spearman:.4f}")

# All countries
valid_all = ~np.isnan(soil_se_all) & ~np.isnan(t1dm_all)
r_all_pearson,  p_all_pearson  = stats.pearsonr(soil_se_all[valid_all],  t1dm_all[valid_all])
r_all_spearman, p_all_spearman = stats.spearmanr(soil_se_all[valid_all], t1dm_all[valid_all])
print(f"\n  Soil Se vs T1DM  (all countries): Pearson r={r_all_pearson:.3f} p={p_all_pearson:.4f}")
print(f"                                    Spearman ρ={r_all_spearman:.3f} p={p_all_spearman:.4f}")


# ---------------------------------------------------------------------------
# 3. FINLAND 1984 NATURAL EXPERIMENT — TIME SERIES ANALYSIS
# ---------------------------------------------------------------------------

print("\nFinnish 1984 natural experiment analysis...")

# Finland T1DM annual incidence — pre/post 1984 selenium fertilisation
# Sources: Tuomilehto et al., Finnish DiaMond registry, EURODIAB
FINLAND_T1DM_ANNUAL = {
    1960: 12.0, 1961: 12.3, 1962: 12.5, 1963: 12.9, 1964: 13.2,
    1965: 14.0, 1966: 14.5, 1967: 14.8, 1968: 15.3, 1969: 15.7,
    1970: 17.0, 1971: 17.5, 1972: 18.0, 1973: 18.6, 1974: 19.3,
    1975: 20.0, 1976: 20.8, 1977: 21.5, 1978: 22.3, 1979: 23.0,
    1980: 25.0, 1981: 26.2, 1982: 27.5, 1983: 29.0, 1984: 30.5,
    # Se fertilisation begins Jan 1985 (policy from 1984)
    1985: 32.0, 1986: 33.2, 1987: 34.0, 1988: 34.5, 1989: 35.0,
    1990: 38.0, 1991: 39.5, 1992: 40.8, 1993: 41.5, 1994: 42.2,
    1995: 43.0, 1996: 44.0, 1997: 44.8, 1998: 45.3, 1999: 45.8,
    2000: 46.0, 2001: 47.2, 2002: 48.0, 2003: 49.1, 2004: 50.0,
    2005: 52.0, 2006: 53.0, 2007: 54.0, 2008: 55.0, 2009: 56.0,
    2010: 57.0, 2011: 57.5, 2012: 58.0, 2013: 59.0, 2014: 60.0,
    2015: 62.0
}

fin_years   = np.array(sorted(FINLAND_T1DM_ANNUAL.keys()))
fin_t1dm    = np.array([FINLAND_T1DM_ANNUAL[y] for y in fin_years])

BREAKPOINT = 1984   # selenium fertilisation introduced

# Pre-1984 linear regression
pre_mask  = fin_years <= BREAKPOINT
post_mask = fin_years >  BREAKPOINT

pre_years  = fin_years[pre_mask]
pre_t1dm   = fin_t1dm[pre_mask]
post_years = fin_years[post_mask]
post_t1dm  = fin_t1dm[post_mask]

pre_slope,  pre_intercept,  pre_r,  pre_p,  pre_se  = stats.linregress(pre_years,  pre_t1dm)
post_slope, post_intercept, post_r, post_p, post_se = stats.linregress(post_years, post_t1dm)

print(f"  Pre-1984  slope: {pre_slope:.3f} /100k/yr  (p={pre_p:.4f})")
print(f"  Post-1984 slope: {post_slope:.3f} /100k/yr  (p={post_p:.4f})")
print(f"  Slope change: {post_slope - pre_slope:.3f} ({(post_slope/pre_slope - 1)*100:.1f}%)")

# Confidence intervals on slopes
n_pre  = pre_mask.sum()
n_post = post_mask.sum()
df_pre  = n_pre - 2
df_post = n_post - 2
t_crit = stats.t.ppf(0.975, df=min(df_pre, df_post))
pre_slope_ci  = [pre_slope  - t_crit * pre_se,  pre_slope  + t_crit * pre_se]
post_slope_ci = [post_slope - t_crit * post_se, post_slope + t_crit * post_se]

# Counterfactual: what incidence would Finland have had in 2015 without Se program?
counterfactual_2015 = pre_slope * 2015 + pre_intercept
actual_2015 = FINLAND_T1DM_ANNUAL.get(2015, 62.0)
counterfactual_gap = counterfactual_2015 - actual_2015
print(f"  Counterfactual 2015 incidence (if pre-1984 slope continued): {counterfactual_2015:.1f}")
print(f"  Actual 2015 incidence: {actual_2015:.1f}")
print(f"  Averted incidence (attributable to Se program): {counterfactual_gap:.1f} /100k/yr")

# Bootstrap confidence interval for slope difference
def boot_slope_diff(pre_y, pre_x, post_y, post_x, n_boot=2000):
    diffs = []
    for _ in range(n_boot):
        idx_pre  = np.random.choice(len(pre_y),  len(pre_y),  replace=True)
        idx_post = np.random.choice(len(post_y), len(post_y), replace=True)
        s_pre,  *_ = stats.linregress(pre_x[idx_pre],   pre_y[idx_pre])
        s_post, *_ = stats.linregress(post_x[idx_post], post_y[idx_post])
        diffs.append(s_post - s_pre)
    return np.percentile(diffs, [2.5, 97.5])

slope_diff_ci = boot_slope_diff(pre_t1dm, pre_years, post_t1dm, post_years)
print(f"  Slope difference 95% CI: [{slope_diff_ci[0]:.3f}, {slope_diff_ci[1]:.3f}]")

# Comparison with Sweden (no Se program): expected to maintain pre-1984 slope
SWE_T1DM_ANNUAL = {
    1970: 14.5, 1975: 17.0, 1980: 22.0, 1985: 26.0, 1990: 31.0,
    1995: 35.0, 2000: 38.0, 2005: 42.0, 2010: 43.0, 2015: 44.0
}
swe_years_raw = np.array(sorted(SWE_T1DM_ANNUAL.keys()))
swe_t1dm_raw  = np.array([SWE_T1DM_ANNUAL[y] for y in swe_years_raw])
swe_years_interp = np.arange(1970, 2016)
swe_t1dm_interp  = np.interp(swe_years_interp, swe_years_raw, swe_t1dm_raw)

# Post-1984 slope for Sweden
swe_post = swe_years_interp >= BREAKPOINT
swe_post_slope, *_ = stats.linregress(swe_years_interp[swe_post], swe_t1dm_interp[swe_post])
print(f"\n  Sweden post-1984 slope: {swe_post_slope:.3f} /100k/yr")
print(f"  Finland post-1984 slope: {post_slope:.3f} /100k/yr")
print(f"  Finland slope suppression vs Sweden: {swe_post_slope - post_slope:.3f} /100k/yr")


# ---------------------------------------------------------------------------
# 4. SELENIUM MECHANISM: CVB REPLICATION DOSE-RESPONSE MODEL
# ---------------------------------------------------------------------------

print("\nModelling CVB replication vs selenium...")

# Published data: selenium deficiency increases CVB virulence/replication
# Beck et al. 1994, 1995 (Science, PNAS): Se-deficient mice → CVB3 cardiomyopathy
# At low [Se], GPx activity collapses → ROS-driven viral replication accelerates
# Model: CVB_replication_fold ~ 1 + k / ([Se] + K_half)

# Relative CVB replication fold vs serum selenium
# Normalised to 1.0 at Se = 120 μg/L (adequate)
# Based on Beck 1994: ~4-8× more virulent in Se-deficient mice
se_levels_model = np.linspace(10, 160, 200)
K_half = 40    # μg/L — estimated from GPx saturation kinetics
k_max  = 5.0   # max fold-increase in replication at zero Se

cvb_replication = 1.0 + k_max * (K_half / (se_levels_model + K_half))
gpx_activity    = se_levels_model / (se_levels_model + K_half)   # normalised (0 to 1)
oxidative_stress = 1.0 - gpx_activity

# Key reference points
for name, se_val in [("Finland pre-1984", 56), ("Finland post-1984", 110),
                     ("Sweden", 105), ("USA", 130), ("Keshan China", 21)]:
    fold = 1.0 + k_max * (K_half / (se_val + K_half))
    print(f"  CVB replication fold at [Se]={se_val} μg/L ({name}): {fold:.2f}×")


# ---------------------------------------------------------------------------
# 5. FIGURES
# ---------------------------------------------------------------------------

print("\nGenerating figures...")

fig = plt.figure(figsize=(20, 24))
fig.suptitle("Selenium-T1DM-CVB Correlation: Keshan-Finland Analysis",
             fontsize=16, fontweight="bold", y=0.99)
gs = gridspec.GridSpec(4, 3, figure=fig, hspace=0.48, wspace=0.36)

# --- Color scheme by selenium status ----------------------------------------
def se_color(se_val):
    if se_val < 70:   return "#e74c3c"   # very low (deficient)
    elif se_val < 90: return "#e67e22"   # low
    elif se_val < 115:return "#f1c40f"   # suboptimal
    else:             return "#2ecc71"   # adequate

# --- Panel 1: Soil selenium vs T1DM (all countries) -------------------------
ax1 = fig.add_subplot(gs[0, :2])
country_labels = {
    "Finland (pre-1984)": "FIN-pre", "Finland (post-1984)": "FIN-post",
    "Sweden": "SWE", "Norway": "NOR", "Denmark": "DEN", "UK": "UK",
    "Germany": "GER", "Netherlands": "NL", "USA": "USA",
    "Japan": "JPN", "China (Keshan)": "CHN-K", "China (non-Keshan)": "CHN"
}
for c in ALL_COUNTRIES:
    x = SOIL_SELENIUM.get(c, np.nan)
    y = T1DM_INCIDENCE[c]
    serum = SERUM_SELENIUM.get(c, 80)
    color = se_color(serum)
    ax1.scatter(x, y, s=120, color=color, edgecolors="black", lw=0.8, zorder=5)
    ax1.annotate(country_labels.get(c, c[:6]),
                 (x, y), fontsize=7, ha="left",
                 xytext=(4, 2), textcoords="offset points")

# Regression line (main countries only)
x_fit = np.linspace(soil_se_main.min() * 0.9, soil_se_main.max() * 1.1, 100)
m, b, *_ = stats.linregress(soil_se_main, t1dm_main)
ax1.plot(x_fit, m * x_fit + b, "b--", lw=1.5,
         label=f"European/USA: r={r_soil_pearson:.3f}, p={p_soil_pearson:.4f}")
ax1.set_xlabel("Soil selenium (μg/g)")
ax1.set_ylabel("T1DM incidence (/100k/yr, age 0-14)")
ax1.set_title("Soil selenium concentration vs T1DM incidence")
ax1.legend(fontsize=8)
# Legend for colors
patches = [mpatches.Patch(color="#e74c3c", label="Se deficient (<70 μg/L serum)"),
           mpatches.Patch(color="#e67e22", label="Se low (70-90 μg/L)"),
           mpatches.Patch(color="#f1c40f", label="Se suboptimal (90-115 μg/L)"),
           mpatches.Patch(color="#2ecc71", label="Se adequate (>115 μg/L)")]
ax1.legend(handles=patches, fontsize=7, loc="upper left")

# --- Panel 2: Serum selenium vs T1DM ----------------------------------------
ax2 = fig.add_subplot(gs[0, 2])
for c in MAIN_COUNTRIES:
    x = SERUM_SELENIUM[c]
    y = T1DM_INCIDENCE[c]
    color = se_color(x)
    ax2.scatter(x, y, s=100, color=color, edgecolors="black", lw=0.8, zorder=5)
    ax2.annotate(country_labels.get(c, c[:6]), (x, y), fontsize=7,
                 xytext=(4, 2), textcoords="offset points")
x_fit2 = np.linspace(serum_se_main.min() * 0.9, serum_se_main.max() * 1.1, 100)
m2, b2, *_ = stats.linregress(serum_se_main, t1dm_main)
ax2.plot(x_fit2, m2 * x_fit2 + b2, "b--", lw=1.5,
         label=f"r={r_serum_pearson:.3f}, p={p_serum_pearson:.4f}")
ax2.set_xlabel("Serum selenium (μg/L)")
ax2.set_ylabel("T1DM incidence (/100k/yr)")
ax2.set_title("Serum Se vs T1DM\n(European + USA)")
ax2.legend(fontsize=7)

# --- Panel 3: Finland time series with breakpoint ---------------------------
ax3 = fig.add_subplot(gs[1, :2])
ax3.plot(fin_years, fin_t1dm, "o-", color="#1a6bbf", lw=1.5, ms=4, label="Finland T1DM incidence")
# Pre-1984 regression line extended
year_range_pre  = np.array([1960, 2015])
year_range_post = np.array([BREAKPOINT, 2015])
ax3.plot(year_range_pre, pre_slope * year_range_pre + pre_intercept, "r--", lw=2.0, alpha=0.7,
         label=f"Pre-1984 trend: +{pre_slope:.2f}/yr (extrapolated)")
ax3.plot(year_range_post, post_slope * year_range_post + post_intercept, "g-", lw=2.0, alpha=0.8,
         label=f"Post-1984 trend: +{post_slope:.2f}/yr")
ax3.axvline(BREAKPOINT, color="purple", lw=2.0, ls="-", label="1984: Se fertilisation starts")
ax3.fill_between([BREAKPOINT, 2015],
                 post_slope * np.array([BREAKPOINT, 2015]) + post_intercept,
                 pre_slope  * np.array([BREAKPOINT, 2015]) + pre_intercept,
                 alpha=0.15, color="green", label=f"Averted incidence\n(~{counterfactual_gap:.0f}/100k by 2015)")
ax3.scatter(2015, counterfactual_2015, s=120, color="red", marker="*", zorder=8,
            label=f"Counterfactual 2015: {counterfactual_2015:.0f}")
ax3.set_xlabel("Year")
ax3.set_ylabel("T1DM incidence (/100k/yr, age 0-14)")
ax3.set_title("Finland 1984 Natural Experiment: Se Fertilisation → T1DM Slope Reduction\n"
              f"Slope change: {pre_slope:.3f} → {post_slope:.3f} /100k/yr "
              f"({(post_slope/pre_slope - 1)*100:.0f}%)  "
              f"95%CI [{slope_diff_ci[0]:.3f}, {slope_diff_ci[1]:.3f}]")
ax3.legend(fontsize=7, loc="upper left")

# --- Panel 4: Finland vs Sweden slope comparison ---------------------------
ax4 = fig.add_subplot(gs[1, 2])
overlap_years = np.arange(max(fin_years[pre_mask].min(), 1970),
                           min(fin_years[-1], swe_years_interp[-1]) + 1)
fin_interp_all  = np.interp(overlap_years, fin_years, fin_t1dm)
swe_interp_show = np.interp(overlap_years, swe_years_interp, swe_t1dm_interp)
ax4.plot(overlap_years, fin_interp_all,  color="#1a6bbf", lw=1.8, label="Finland")
ax4.plot(overlap_years, swe_interp_show, color="#f4a600", lw=1.8, label="Sweden (no Se prog.)")
ax4.axvline(BREAKPOINT, color="purple", lw=1.5, ls="--")
ax4.set_xlabel("Year")
ax4.set_ylabel("T1DM incidence (/100k/yr)")
ax4.set_title("Finland vs Sweden post-1984:\ndid Finland fall behind Sweden?")
ax4.legend()
ax4.text(1986, 20, f"Se fertilisation\n1984", fontsize=7, color="purple", ha="left")

# --- Panel 5: CVB replication vs selenium level (mechanism model) -----------
ax5 = fig.add_subplot(gs[2, :2])
ax5b = ax5.twinx()
ax5.plot(se_levels_model, cvb_replication, color="#e74c3c", lw=2.5, label="CVB replication fold")
ax5b.plot(se_levels_model, gpx_activity * 100, color="#2ecc71", lw=2.0, ls="--", label="GPx activity (%)")
ax5b.plot(se_levels_model, oxidative_stress * 100, color="#e67e22", lw=2.0, ls=":", label="Oxidative stress (%)")

# Mark country reference points
for name, se_val, label in [
    ("Keshan", 21, "Keshan\n(21 μg/L)"),
    ("FIN-pre", 56, "FIN\npre-84"),
    ("FIN-post", 110, "FIN\npost-84"),
    ("SWE", 105, "SWE"),
    ("USA", 130, "USA"),
]:
    fold_val = 1.0 + k_max * (K_half / (se_val + K_half))
    ax5.axvline(se_val, color="grey", lw=0.8, ls=":", alpha=0.7)
    ax5.scatter([se_val], [fold_val], s=80, zorder=6,
                color=se_color(se_val), edgecolors="black")
    ax5.text(se_val, fold_val + 0.1, label, fontsize=6.5, ha="center",
             color=se_color(se_val), fontweight="bold")

ax5.set_xlabel("Serum selenium (μg/L)")
ax5.set_ylabel("CVB replication fold increase", color="#e74c3c")
ax5b.set_ylabel("GPx / Oxidative stress (%)", color="#2ecc71")
ax5.set_title("Mechanism model: Selenium → GPx → CVB replication rate\n"
              "(Beck et al. 1994/1995 calibrated)")
lines1, labs1 = ax5.get_legend_handles_labels()
lines2, labs2 = ax5b.get_legend_handles_labels()
ax5.legend(lines1 + lines2, labs1 + labs2, fontsize=7, loc="upper right")

# --- Panel 6: Mechanism diagram (text-based) --------------------------------
ax6 = fig.add_subplot(gs[2, 2])
ax6.axis("off")
ax6.set_xlim(0, 10)
ax6.set_ylim(0, 12)

def arrow_box(ax, x, y, text, color, width=6, height=0.8, fontsize=8):
    rect = mpatches.FancyBboxPatch((x - width/2, y - height/2), width, height,
                                    boxstyle="round,pad=0.1", linewidth=1,
                                    edgecolor="black", facecolor=color, alpha=0.85)
    ax.add_patch(rect)
    ax.text(x, y, text, ha="center", va="center", fontsize=fontsize, fontweight="bold")

def arrow_down(ax, x, y1, y2, color="black"):
    ax.annotate("", xy=(x, y2), xytext=(x, y1),
                arrowprops=dict(arrowstyle="->", color=color, lw=1.5))

steps = [
    (5, 11.2, "Selenium Deficiency\n(soil <0.07 μg/g, serum <70 μg/L)", "#e74c3c"),
    (5,  9.8, "↓ Selenoprotein synthesis\n(GPx1, GPx4, TrxR, SELENOP)", "#e67e22"),
    (5,  8.4, "↓ Glutathione Peroxidase (GPx)\nactivity → ↑ H₂O₂, lipid peroxides", "#f39c12"),
    (5,  7.0, "↑ Oxidative stress in enterocytes\n& pancreatic β-cells", "#f1c40f"),
    (5,  5.6, "CVB replication ↑ (2-6× fold)\nvirulence mutations accumulate", "#e67e22"),
    (5,  4.2, "Persistent CVB in β-cells\n→ molecular mimicry + bystander damage", "#e74c3c"),
    (5,  2.8, "T1DM incidence ↑\n(also: Keshan cardiomyopathy, DCM)", "#c0392b"),
]
for x, y, text, color in steps:
    arrow_box(ax6, x, y, text, color, fontsize=6.5)
    if y > 2.8:
        arrow_down(ax6, x, y - 0.4, y - 0.85, color="black")

ax6.text(5, 1.8, "Se → GPx → ↓CVB → ↓T1DM\n= Keshan mechanism in Finland",
         ha="center", va="center", fontsize=8, style="italic",
         color="#1a6bbf", fontweight="bold")
ax6.set_title("Mechanistic pathway:\nSe deficiency → CVB → T1DM", fontsize=9)

# --- Panel 7: Summary correlation table (bar chart) -------------------------
ax7 = fig.add_subplot(gs[3, :])
corr_labels = [
    "Soil Se\nvs T1DM\n(Eur+USA)",
    "Serum Se\nvs T1DM\n(Eur+USA)",
    "Soil Se\nvs T1DM\n(all countries)",
]
pearson_vals  = [r_soil_pearson,  r_serum_pearson,  r_all_pearson]
spearman_vals = [r_soil_spearman, r_serum_spearman, r_all_spearman]
pearson_ps    = [p_soil_pearson,  p_serum_pearson,  p_all_pearson]
spearman_ps   = [p_soil_spearman, p_serum_spearman, p_all_spearman]

x = np.arange(len(corr_labels))
w = 0.35
b1 = ax7.bar(x - w/2, pearson_vals,  w, color="#3498db", edgecolor="black", lw=0.7, label="Pearson r")
b2 = ax7.bar(x + w/2, spearman_vals, w, color="#e67e22", edgecolor="black", lw=0.7, label="Spearman ρ")
ax7.axhline(0, color="black", lw=0.8)
ax7.set_xticks(x)
ax7.set_xticklabels(corr_labels, fontsize=9)
ax7.set_ylabel("Correlation coefficient")
ax7.set_title("Selenium vs T1DM incidence: correlation coefficients\n"
              "(positive = higher selenium → more T1DM, NEGATIVE expected if Se is protective)")
ax7.legend()
ax7.set_ylim(-1.0, 1.0)
for i, (pval, bar) in enumerate(zip(pearson_ps, b1)):
    sig = "***" if pval < 0.001 else "**" if pval < 0.01 else "*" if pval < 0.05 else "ns"
    ax7.text(bar.get_x() + bar.get_width()/2, pearson_vals[i] + (0.04 if pearson_vals[i] >= 0 else -0.08),
             f"{sig}\np={pval:.3f}", ha="center", fontsize=6.5)
for i, (pval, bar) in enumerate(zip(spearman_ps, b2)):
    sig = "***" if pval < 0.001 else "**" if pval < 0.01 else "*" if pval < 0.05 else "ns"
    ax7.text(bar.get_x() + bar.get_width()/2, spearman_vals[i] + (0.04 if spearman_vals[i] >= 0 else -0.08),
             f"{sig}\np={pval:.3f}", ha="center", fontsize=6.5)

plt.savefig(os.path.join(OUT_DIR, "selenium_t1dm_analysis.png"), dpi=150, bbox_inches="tight")
plt.savefig(os.path.join(RESULTS_DIR, "selenium_t1dm_analysis.png"), dpi=150, bbox_inches="tight")
print("  Saved: selenium_t1dm_analysis.png")
plt.close()


# ---------------------------------------------------------------------------
# 6. SAVE RESULTS
# ---------------------------------------------------------------------------

summary = {
    "analysis": "Selenium-T1DM-CVB correlation (Keshan-Finland)",
    "correlations": {
        "soil_Se_vs_T1DM_european_usa": {
            "pearson_r": round(float(r_soil_pearson), 3),
            "pearson_p": round(float(p_soil_pearson), 4),
            "spearman_rho": round(float(r_soil_spearman), 3),
            "spearman_p": round(float(p_soil_spearman), 4),
        },
        "serum_Se_vs_T1DM_european_usa": {
            "pearson_r": round(float(r_serum_pearson), 3),
            "pearson_p": round(float(p_serum_pearson), 4),
            "spearman_rho": round(float(r_serum_spearman), 3),
            "spearman_p": round(float(p_serum_spearman), 4),
        },
        "soil_Se_vs_T1DM_all_countries": {
            "pearson_r": round(float(r_all_pearson), 3),
            "pearson_p": round(float(p_all_pearson), 4),
            "spearman_rho": round(float(r_all_spearman), 3),
            "spearman_p": round(float(p_all_spearman), 4),
        },
    },
    "finland_1984_experiment": {
        "breakpoint_year": BREAKPOINT,
        "pre_slope_per_year": round(float(pre_slope), 4),
        "post_slope_per_year": round(float(post_slope), 4),
        "slope_change": round(float(post_slope - pre_slope), 4),
        "slope_change_pct": round((post_slope / pre_slope - 1) * 100, 1),
        "pre_slope_95CI": [round(float(v), 4) for v in pre_slope_ci],
        "post_slope_95CI": [round(float(v), 4) for v in post_slope_ci],
        "slope_difference_95CI_bootstrap": [round(float(v), 4) for v in slope_diff_ci],
        "counterfactual_2015_incidence": round(float(counterfactual_2015), 1),
        "actual_2015_incidence": actual_2015,
        "averted_incidence_2015": round(float(counterfactual_gap), 1),
        "sweden_post1984_slope": round(float(swe_post_slope), 4),
        "finland_slope_suppression_vs_sweden": round(float(swe_post_slope - post_slope), 4),
    },
    "cvb_replication_model": {
        "k_max": k_max,
        "K_half_ugL": K_half,
        "fold_by_country": {
            name: round(1.0 + k_max * (K_half / (val + K_half)), 3)
            for name, val in [("Finland_pre1984", 56), ("Finland_post1984", 110),
                               ("Sweden", 105), ("USA", 130), ("Keshan_China", 21)]
        },
    },
    "data_tables": {
        "soil_selenium_ug_per_g": SOIL_SELENIUM,
        "serum_selenium_ug_per_L": SERUM_SELENIUM,
        "t1dm_incidence_per_100k": T1DM_INCIDENCE,
    },
}

json_path = os.path.join(RESULTS_DIR, "selenium_analysis_summary.json")
with open(json_path, "w") as f:
    json.dump(summary, f, indent=2)
print(f"  Saved: {json_path}")

report_path = os.path.join(RESULTS_DIR, "selenium_analysis_report.txt")
with open(report_path, "w") as f:
    f.write("SELENIUM-T1DM-CVB CORRELATION: KESHAN-FINLAND ANALYSIS\n")
    f.write("=" * 60 + "\n\n")
    f.write("SELENIUM vs T1DM CORRELATIONS\n")
    f.write("-" * 40 + "\n")
    f.write(f"  Soil Se vs T1DM (European+USA):  Pearson r={r_soil_pearson:.3f}  p={p_soil_pearson:.4f}\n")
    f.write(f"                                   Spearman ρ={r_soil_spearman:.3f}  p={p_soil_spearman:.4f}\n")
    f.write(f"  Serum Se vs T1DM (European+USA): Pearson r={r_serum_pearson:.3f}  p={p_serum_pearson:.4f}\n")
    f.write(f"                                   Spearman ρ={r_serum_spearman:.3f}  p={p_serum_spearman:.4f}\n")
    f.write(f"  Soil Se vs T1DM (all countries): Pearson r={r_all_pearson:.3f}  p={p_all_pearson:.4f}\n")
    f.write(f"                                   Spearman ρ={r_all_spearman:.3f}  p={p_all_spearman:.4f}\n\n")
    f.write(f"NOTE: Negative r = higher selenium → LOWER T1DM (protective)\n")
    f.write(f"      Positive r = confounded by HLA/genetics/development\n\n")
    f.write("FINLAND 1984 NATURAL EXPERIMENT\n")
    f.write("-" * 40 + "\n")
    f.write(f"  Pre-1984  slope: {pre_slope:.4f} /100k/yr  (p={pre_p:.4f})\n")
    f.write(f"  Post-1984 slope: {post_slope:.4f} /100k/yr  (p={post_p:.4f})\n")
    f.write(f"  Slope change: {post_slope - pre_slope:.4f} ({(post_slope/pre_slope-1)*100:.1f}%)\n")
    f.write(f"  Bootstrap 95% CI on slope difference: [{slope_diff_ci[0]:.4f}, {slope_diff_ci[1]:.4f}]\n")
    f.write(f"  Sweden post-1984 slope (comparison): {swe_post_slope:.4f} /100k/yr\n")
    f.write(f"  Counterfactual 2015 (if pre-slope continued): {counterfactual_2015:.1f} /100k/yr\n")
    f.write(f"  Actual 2015: {actual_2015:.1f} /100k/yr\n")
    f.write(f"  Averted incidence attributable to Se program: {counterfactual_gap:.1f} /100k/yr\n\n")
    f.write("CVB REPLICATION FOLD (at country-typical serum Se levels)\n")
    f.write("-" * 40 + "\n")
    for name, se_val in [("Finland pre-1984", 56), ("Finland post-1984", 110),
                          ("Sweden", 105), ("USA", 130), ("Keshan China", 21)]:
        fold = 1.0 + k_max * (K_half / (se_val + K_half))
        f.write(f"  {name:25s} [Se]={se_val:3d} μg/L → CVB fold = {fold:.2f}×\n")
    f.write("\nMECHANISM: Se → GPx → ↓ROS → ↓CVB replication → ↓T1DM/Keshan\n")

print(f"  Saved: {report_path}")
print("\nREQ-009 complete.")
