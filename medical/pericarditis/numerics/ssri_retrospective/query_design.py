"""
REQ-007: SSRI-Pericarditis Retrospective Database Query Design
==============================================================
Designs a retrospective claims database analysis for SSRI (fluoxetine)
use in recurrent pericarditis. Includes:
  - ICD-10 / drug code specification
  - Power calculation for 30% recurrence reduction
  - Effect-size model
  - 10,000-patient-per-arm simulation
  - PubMed search for existing SSRI+pericarditis/myocarditis studies
"""

import numpy as np
import scipy.stats as stats
import scipy.optimize as optimize
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from statsmodels.stats.power import TTestIndPower, NormalIndPower
from Bio import Entrez
import json, os, warnings
warnings.filterwarnings("ignore")

Entrez.email = "noreply@example.com"

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(OUT_DIR)), "results", "ssri_retrospective"
)
os.makedirs(RESULTS_DIR, exist_ok=True)

np.random.seed(42)

# ---------------------------------------------------------------------------
# 1. DATABASE QUERY DESIGN
# ---------------------------------------------------------------------------

QUERY_DESIGN = {
    "study_type": "Retrospective cohort study (claims database)",
    "target_databases": ["Optum Clinformatics", "IBM MarketScan", "CPRD (UK)", "Danish NPR"],
    "observation_window": "2010-2023 (ICD-10 era)",
    "follow_up": "18 months from index pericarditis encounter",

    "inclusion_criteria": {
        "index_event": {
            "description": "First pericarditis diagnosis in claims",
            "icd10_codes": {
                "I30.0": "Acute nonspecific idiopathic pericarditis",
                "I30.1": "Infective pericarditis",
                "I30.8": "Other forms of acute pericarditis",
                "I30.9": "Acute pericarditis, unspecified",
                "I31.0": "Chronic adhesive pericarditis",
            },
            "require": ">=1 inpatient OR >=2 outpatient claims within 30 days",
        },
        "age": "18-75 years at index",
        "enrollment": ">=12 months continuous enrollment pre-index",
        "washout": "No prior pericarditis diagnosis in 12-month pre-index window",
    },

    "exposure_definition": {
        "primary": {
            "drug": "Fluoxetine",
            "atc_code": "N06AB03",
            "ndc_codes": ["00777-3105-02", "00093-0814-01"],  # examples
            "timing": "Prescription dispensed within 30 days of index pericarditis",
            "minimum_supply": ">=30 days supply (adherence proxy)",
        },
        "secondary": {
            "drug": "Any SSRI",
            "atc_codes": {
                "N06AB03": "fluoxetine",
                "N06AB04": "citalopram",
                "N06AB05": "paroxetine",
                "N06AB06": "sertraline",
                "N06AB08": "fluvoxamine",
                "N06AB10": "escitalopram",
            },
        },
    },

    "outcome_definition": {
        "primary": "Recurrent pericarditis: >=1 new I30.x encounter >=28 days and <=18 months after index",
        "secondary": [
            "Hospitalization for pericarditis within 18 months",
            "Constrictive pericarditis (I31.1) within 36 months",
            "Pericardial effusion (I31.3) within 18 months",
        ],
    },

    "confounders_to_adjust": {
        "demographics": ["age_at_index", "sex", "calendar_year"],
        "pericarditis_tx": {
            "colchicine": {"atc": "J01XC01", "window": "index ±30 days"},
            "nsaids":     {"atc": ["M01AB", "M01AE", "M01AC"], "window": "index ±30 days"},
            "steroids":   {"atc": "H02AB", "window": "index ±30 days"},
        },
        "cardiac_comorbidities": {
            "heart_failure":     "I50.x",
            "afib":              "I48.x",
            "myocarditis":       "I40.x, I41.x",
            "connective_tissue": "M32.x (SLE), M35.1 (Sjogren), M05.x (RA)",
            "recent_MI":         "I21.x within 6 months",
            "prior_cardiac_surgery": "Z95.x, Z98.61",
        },
        "infection_markers": {
            "recent_viral_illness": "B34.x, J06.x within 30 days pre-index",
            "HIV": "B20.x",
        },
        "depression_psych": {
            "major_depression": "F32.x, F33.x (indication for SSRI — must control)",
        },
        "healthcare_utilization": ["charlson_comorbidity_index", "n_prior_hospitalizations"],
    },

    "statistical_methods": {
        "primary": "Cox proportional hazards (time to recurrence)",
        "adjustment": "Inverse probability of treatment weighting (IPTW) using propensity score",
        "propensity_model": "Logistic regression on all confounders listed above",
        "sensitivity_analyses": [
            "Active comparator design: fluoxetine vs antidepressant from different class (bupropion)",
            "High-dimensional propensity score (hdPS)",
            "Restrict to viral/idiopathic pericarditis (I30.0, I30.9) only",
            "Restrict to colchicine-treated patients (test incremental benefit)",
            "ITT vs per-protocol (require SSRI for >=90 days)",
        ],
        "subgroup_analyses": [
            "Age <40 vs >=40",
            "CVB-era (summer-onset, 18-40yo) vs non-CVB era",
            "Colchicine users vs non-users",
        ],
    },
}

# ---------------------------------------------------------------------------
# 2. EFFECT SIZE MODEL
# ---------------------------------------------------------------------------

print("Computing effect size model...")

# Published recurrence rates
p_no_colchicine  = 0.30   # Imazio et al. COPE trial — 30% recurrence
p_with_colchicine = 0.15  # Imazio et al. COPE trial — 15% with colchicine

# Fluoxetine (antiviral) effect model
# CVB causes ~20% of pericarditis (literature)
# If fluoxetine clears CVB in 6mo, expected absolute reduction in CVB-caused cases
p_cvb_etiology = 0.20
p_fluoxetine_clearance = 0.70  # ~70% of persistent CVB cleared by 6mo (Komarow et al.)

# Expected absolute reduction in recurrence from fluoxetine (among all-pericarditis patients):
#   = p_cvb_etiology × p_fluoxetine_clearance × p_recurrence_if_cvb_persists
# Assume CVB-persistent patients recur at 2× background rate
p_recurrence_if_cvb = p_no_colchicine * 2.0
expected_abs_reduction_fluox = p_cvb_etiology * p_fluoxetine_clearance * p_recurrence_if_cvb

# Scenarios
scenarios = {
    "base_no_treatment":   p_no_colchicine,
    "with_colchicine":     p_with_colchicine,
    "with_colchicine_plus_fluoxetine_low":  p_with_colchicine - 0.05,
    "with_colchicine_plus_fluoxetine_mid":  p_with_colchicine - expected_abs_reduction_fluox,
    "with_colchicine_plus_fluoxetine_high": p_with_colchicine - 0.15,
}
for k, v in scenarios.items():
    scenarios[k] = max(v, 0.01)  # floor at 1%

print(f"  Expected absolute reduction from fluoxetine: {expected_abs_reduction_fluox:.3f} ({expected_abs_reduction_fluox*100:.1f}%)")
print("  Scenario recurrence probabilities:")
for k, v in scenarios.items():
    print(f"    {k}: {v:.3f} ({v*100:.1f}%)")


# ---------------------------------------------------------------------------
# 3. POWER CALCULATION
# ---------------------------------------------------------------------------

print("\nPower calculations...")

def power_for_two_proportions(p1, p2, alpha=0.05, power_target=0.80):
    """Sample size per arm for two-proportion z-test."""
    z_alpha = stats.norm.ppf(1 - alpha / 2)
    z_beta  = stats.norm.ppf(power_target)
    p_bar   = (p1 + p2) / 2
    n = ((z_alpha * np.sqrt(2 * p_bar * (1 - p_bar)) +
          z_beta  * np.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) /
         (p1 - p2)) ** 2
    return int(np.ceil(n))

def achieved_power(p1, p2, n, alpha=0.05):
    """Achieved power for given n per arm."""
    z_alpha = stats.norm.ppf(1 - alpha / 2)
    p_bar   = (p1 + p2) / 2
    se      = np.sqrt(p1 * (1 - p1) / n + p2 * (1 - p2) / n)
    if se == 0:
        return np.nan
    z       = abs(p1 - p2) / se
    return float(stats.norm.cdf(z - z_alpha))

p_control = p_with_colchicine  # control arm already on colchicine

power_table = []
for reduction_pct in [5, 10, 15, 20, 25, 30]:
    p_treatment = p_control * (1 - reduction_pct / 100)
    n_per_arm_80 = power_for_two_proportions(p_control, p_treatment, power_target=0.80)
    n_per_arm_90 = power_for_two_proportions(p_control, p_treatment, power_target=0.90)
    power_at_10k  = achieved_power(p_control, p_treatment, 10000)
    rr = p_treatment / p_control
    nnt = 1 / abs(p_control - p_treatment)
    power_table.append({
        "reduction_%":  reduction_pct,
        "p_control":    round(p_control, 3),
        "p_treatment":  round(p_treatment, 3),
        "RR":           round(rr, 3),
        "NNT":          round(nnt, 1),
        "n_80pct_power": n_per_arm_80,
        "n_90pct_power": n_per_arm_90,
        "power_at_10k_per_arm": round(power_at_10k, 3),
    })
    print(f"  {reduction_pct}% reduction: NNT={nnt:.1f}  n/arm(80%)={n_per_arm_80:,}  power@10k={power_at_10k:.3f}")


# ---------------------------------------------------------------------------
# 4. SIMULATION — 10,000 PATIENTS PER ARM
# ---------------------------------------------------------------------------

print("\nRunning 10,000-patient simulation...")

N_SIM = 10_000
N_BOOT = 2_000

# Arm assignments
control_arm   = np.random.binomial(1, p_with_colchicine, N_SIM)  # colchicine alone
treatment_arm = np.random.binomial(1, p_with_colchicine - expected_abs_reduction_fluox, N_SIM)

obs_ctrl  = control_arm.mean()
obs_treat = treatment_arm.mean()
obs_rr    = obs_treat / obs_ctrl
obs_rd    = obs_ctrl - obs_treat   # absolute risk difference
obs_nnt   = 1 / obs_rd if obs_rd > 0 else np.inf

# Bootstrap CI for RR and RD
boot_rr = []
boot_rd = []
for _ in range(N_BOOT):
    bc = np.random.choice(control_arm, N_SIM, replace=True).mean()
    bt = np.random.choice(treatment_arm, N_SIM, replace=True).mean()
    boot_rr.append(bt / bc if bc > 0 else np.nan)
    boot_rd.append(bc - bt)

boot_rr = np.array(boot_rr)
boot_rd = np.array(boot_rd)
rr_ci = np.nanpercentile(boot_rr, [2.5, 97.5])
rd_ci = np.nanpercentile(boot_rd, [2.5, 97.5])

# Chi-squared test
from scipy.stats import chi2_contingency
ct = np.array([[treatment_arm.sum(), N_SIM - treatment_arm.sum()],
               [control_arm.sum(),   N_SIM - control_arm.sum()]])
chi2, p_chi2, _, _ = chi2_contingency(ct)

# Z-test for proportions
z_stat = (obs_ctrl - obs_treat) / np.sqrt(
    obs_ctrl * (1 - obs_ctrl) / N_SIM + obs_treat * (1 - obs_treat) / N_SIM)
p_ztest = 2 * (1 - stats.norm.cdf(abs(z_stat)))

sim_power = achieved_power(p_with_colchicine, p_with_colchicine - expected_abs_reduction_fluox, N_SIM)

print(f"  Simulated control recurrence rate:   {obs_ctrl:.4f}")
print(f"  Simulated treatment recurrence rate: {obs_treat:.4f}")
print(f"  Relative risk (RR): {obs_rr:.3f} (95% CI {rr_ci[0]:.3f}-{rr_ci[1]:.3f})")
print(f"  Absolute risk difference: {obs_rd:.4f} (95% CI {rd_ci[0]:.4f}-{rd_ci[1]:.4f})")
print(f"  NNT: {obs_nnt:.1f}")
print(f"  Chi-squared p: {p_chi2:.4g}  Z-test p: {p_ztest:.4g}")
print(f"  Analytical power at N=10k per arm: {sim_power:.3f}")

# Minimum detectable effect at N=10k
def mde(n, alpha=0.05, power=0.80, p_ctrl=p_with_colchicine):
    """Minimum detectable absolute risk difference."""
    z_alpha = stats.norm.ppf(1 - alpha / 2)
    z_beta  = stats.norm.ppf(power)
    # Approximate using pooled SE
    se = np.sqrt(2 * p_ctrl * (1 - p_ctrl) / n)
    return (z_alpha + z_beta) * se

mde_10k = mde(10000)
mde_1k  = mde(1000)
print(f"  MDE at N=10k: {mde_10k:.4f} ({mde_10k*100:.2f}% absolute difference)")
print(f"  MDE at N=1k:  {mde_1k:.4f} ({mde_1k*100:.2f}% absolute difference)")


# ---------------------------------------------------------------------------
# 5. PUBMED SEARCH — existing SSRI + pericarditis/myocarditis studies
# ---------------------------------------------------------------------------

print("\nSearching PubMed: SSRIs in pericarditis/myocarditis...")

pubmed_results = []
try:
    query = '"fluoxetine" AND ("pericarditis" OR "myocarditis")'
    handle = Entrez.esearch(db="pubmed", term=query, retmax=30, usehistory="y")
    record = Entrez.read(handle)
    handle.close()

    pmids = record["IdList"]
    count = record["Count"]
    print(f"  Total records in PubMed: {count}, fetching top {len(pmids)}")

    if pmids:
        handle = Entrez.efetch(db="pubmed", id=",".join(pmids),
                               rettype="medline", retmode="text")
        raw = handle.read()
        handle.close()

        current = {}
        for line in raw.split("\n"):
            if line.startswith("PMID-"):
                if current:
                    pubmed_results.append(current)
                current = {"pmid": line.split("-", 1)[1].strip()}
            elif line.startswith("TI  -"):
                current["title"] = line.split("-", 1)[1].strip()
            elif line.startswith("DP  -"):
                current["date"] = line.split("-", 1)[1].strip()
            elif line.startswith("AB  -"):
                current["abstract"] = line.split("-", 1)[1].strip()[:300]
            elif line.startswith("AU  -"):
                current.setdefault("authors", []).append(line.split("-", 1)[1].strip())
        if current:
            pubmed_results.append(current)

        print(f"  Parsed {len(pubmed_results)} records")
        for r in pubmed_results[:10]:
            print(f"  [{r.get('date','')}] {r.get('title','N/A')[:80]}")

except Exception as e:
    print(f"  PubMed error: {e}")
    pubmed_results = [{"note": str(e)}]

# Also search for CVB antiviral drug trials in pericarditis
pubmed_cvb = []
try:
    query2 = '("Coxsackievirus" OR "enterovirus" OR "CVB") AND ("pericarditis" OR "myocarditis") AND ("antiviral" OR "treatment")'
    handle = Entrez.esearch(db="pubmed", term=query2, retmax=20)
    record2 = Entrez.read(handle)
    handle.close()
    print(f"\n  CVB antiviral+pericarditis: {record2['Count']} records total, {len(record2['IdList'])} fetched")
    pubmed_cvb = record2["IdList"]
except Exception as e:
    print(f"  CVB search error: {e}")


# ---------------------------------------------------------------------------
# 6. FIGURES
# ---------------------------------------------------------------------------

print("\nGenerating figures...")

fig = plt.figure(figsize=(18, 20))
fig.suptitle("SSRI-Pericarditis Retrospective Study: Design & Power Analysis",
             fontsize=15, fontweight="bold", y=0.98)
gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.45, wspace=0.35)

# --- Panel 1: Power curves --------------------------------------------------
ax1 = fig.add_subplot(gs[0, :2])
ns = np.logspace(2, 4.5, 200).astype(int)
for reduction_pct, color in [(10, "#e74c3c"), (15, "#e67e22"), (20, "#2ecc71"), (30, "#2980b9")]:
    p_t = p_with_colchicine * (1 - reduction_pct / 100)
    powers = [achieved_power(p_with_colchicine, p_t, n) for n in ns]
    ax1.semilogx(ns, powers, color=color, lw=2.0,
                 label=f"{reduction_pct}% reduction (p={p_t:.3f})")
ax1.axhline(0.80, color="black", ls="--", lw=1.0, label="80% power")
ax1.axhline(0.90, color="black", ls=":",  lw=1.0, label="90% power")
ax1.axvline(10000, color="grey", ls="--", lw=1.0, alpha=0.7, label="N=10k/arm")
ax1.set_xlabel("Sample size per arm")
ax1.set_ylabel("Statistical power")
ax1.set_title("Power curves: detecting recurrence reduction with fluoxetine\n"
              f"(Control = colchicine alone, p={p_with_colchicine:.0%})")
ax1.legend(fontsize=8)
ax1.set_ylim(0, 1.05)

# --- Panel 2: Effect size scenarios ----------------------------------------
ax2 = fig.add_subplot(gs[0, 2])
scenario_names = ["No tx", "+Colchicine", "+Colch\n+Fluox\n(low)", "+Colch\n+Fluox\n(mid)", "+Colch\n+Fluox\n(high)"]
scenario_values = list(scenarios.values())
bar_colors = ["#e74c3c", "#e67e22", "#f1c40f", "#2ecc71", "#1abc9c"]
ax2.bar(range(len(scenario_names)), [v * 100 for v in scenario_values],
        color=bar_colors, edgecolor="black", lw=0.8)
ax2.set_xticks(range(len(scenario_names)))
ax2.set_xticklabels(scenario_names, fontsize=7)
ax2.set_ylabel("18-month recurrence rate (%)")
ax2.set_title("Expected recurrence rates\nby treatment scenario")
for i, v in enumerate(scenario_values):
    ax2.text(i, v * 100 + 0.3, f"{v*100:.1f}%", ha="center", fontsize=7)

# --- Panel 3: Power table heatmap ------------------------------------------
ax3 = fig.add_subplot(gs[1, :2])
reductions = [5, 10, 15, 20, 25, 30]
ns_grid = [500, 1000, 2000, 5000, 10000, 20000]
power_grid = np.zeros((len(reductions), len(ns_grid)))
for i, red in enumerate(reductions):
    p_t = p_with_colchicine * (1 - red / 100)
    for j, n in enumerate(ns_grid):
        power_grid[i, j] = achieved_power(p_with_colchicine, p_t, n)

im3 = ax3.imshow(power_grid, aspect="auto", cmap="RdYlGn", vmin=0, vmax=1)
ax3.set_xticks(range(len(ns_grid)))
ax3.set_xticklabels([f"{n:,}" for n in ns_grid])
ax3.set_yticks(range(len(reductions)))
ax3.set_yticklabels([f"{r}%" for r in reductions])
ax3.set_xlabel("Sample size per arm")
ax3.set_ylabel("Relative risk reduction")
ax3.set_title("Power heat map: reduction vs sample size")
plt.colorbar(im3, ax=ax3, label="Power")
for i in range(len(reductions)):
    for j in range(len(ns_grid)):
        ax3.text(j, i, f"{power_grid[i,j]:.2f}", ha="center", va="center", fontsize=7,
                 color="black" if 0.3 < power_grid[i,j] < 0.8 else "white")

# --- Panel 4: Simulation results -------------------------------------------
ax4 = fig.add_subplot(gs[1, 2])
sim_categories = ["Control\n(colchicine)", "Treatment\n(+fluoxetine)"]
sim_values = [obs_ctrl * 100, obs_treat * 100]
sim_errors = [
    (obs_ctrl  - stats.binom.ppf(0.025, N_SIM, obs_ctrl)  / N_SIM) * 100,
    (obs_treat - stats.binom.ppf(0.025, N_SIM, obs_treat) / N_SIM) * 100,
]
bars4 = ax4.bar(sim_categories, sim_values, color=["#e74c3c", "#2ecc71"],
                edgecolor="black", lw=0.8, width=0.5)
ax4.errorbar([0, 1], sim_values, yerr=sim_errors, fmt="none", color="black", lw=1.5, capsize=5)
ax4.set_ylabel("18-month recurrence rate (%)")
ax4.set_title(f"Simulated trial (N={N_SIM:,}/arm)\n"
              f"RR={obs_rr:.3f}  p={p_ztest:.4g}  Power={sim_power:.2%}")
for bar, val in zip(bars4, sim_values):
    ax4.text(bar.get_x() + bar.get_width() / 2, val + 0.2,
             f"{val:.2f}%", ha="center", fontsize=9, fontweight="bold")

# --- Panel 5: NNT by effect size -------------------------------------------
ax5 = fig.add_subplot(gs[2, :2])
rd_range = np.linspace(0.02, 0.20, 200)
nnt_range = 1 / rd_range
ax5.plot(rd_range * 100, nnt_range, color="#2980b9", lw=2.5)
ax5.axvline(expected_abs_reduction_fluox * 100, color="red", ls="--", lw=1.5,
            label=f"Expected ARD = {expected_abs_reduction_fluox*100:.1f}%")
ax5.axhline(obs_nnt, color="green", ls="--", lw=1.5,
            label=f"Simulated NNT = {obs_nnt:.1f}")
ax5.fill_betweenx(nnt_range, 5, 15, alpha=0.1, color="green", label="Expected ARD range (5-15%)")
ax5.set_xlabel("Absolute risk difference (%)")
ax5.set_ylabel("Number Needed to Treat (NNT)")
ax5.set_title("NNT vs absolute recurrence reduction")
ax5.set_ylim(0, 80)
ax5.set_xlim(0, 20)
ax5.legend(fontsize=8)

# --- Panel 6: Confounder DAG (simplified text diagram) ----------------------
ax6 = fig.add_subplot(gs[2, 2])
ax6.axis("off")
dag_text = (
    "STUDY DESIGN SUMMARY\n"
    "─────────────────────────────\n"
    "Exposure:  Fluoxetine (N06AB03)\n"
    "           within 30d of I30.x\n\n"
    "Outcome:   Recurrent I30.x\n"
    "           within 18 months\n\n"
    "Confounders (IPTW-adjusted):\n"
    "  Age, sex, calendar year\n"
    "  Colchicine (J01XC01)\n"
    "  NSAIDs (M01AB, M01AE)\n"
    "  Steroids (H02AB)\n"
    "  Depression (F32/F33)\n"
    "  Cardiac comorbidities\n"
    "  Viral illness (B34.x)\n\n"
    f"Expected ARD: {expected_abs_reduction_fluox*100:.1f}%\n"
    f"NNT: {round(1/expected_abs_reduction_fluox, 0):.0f}\n"
    f"N/arm for 80% power: {power_for_two_proportions(p_with_colchicine, p_with_colchicine - expected_abs_reduction_fluox):,}\n"
    f"Power @ N=10k/arm: {sim_power:.1%}"
)
ax6.text(0.05, 0.95, dag_text, transform=ax6.transAxes,
         fontsize=8, verticalalignment="top", fontfamily="monospace",
         bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.8))

plt.savefig(os.path.join(OUT_DIR, "ssri_pericarditis_power_analysis.png"), dpi=150, bbox_inches="tight")
plt.savefig(os.path.join(RESULTS_DIR, "ssri_pericarditis_power_analysis.png"), dpi=150, bbox_inches="tight")
print("  Saved: ssri_pericarditis_power_analysis.png")
plt.close()


# ---------------------------------------------------------------------------
# 7. SQL QUERY TEMPLATE
# ---------------------------------------------------------------------------

sql_query = """
-- SSRI-Pericarditis Retrospective Cohort Study
-- Target: Optum Clinformatics Extended Data / IBM MarketScan
-- Analyst: [Name], [Institution]

-- Step 1: Index pericarditis encounters
WITH index_pericarditis AS (
    SELECT DISTINCT
        patid,
        MIN(clm_from_dt) AS index_date
    FROM medical_claims
    WHERE
        dx1 IN ('I30.0','I30.1','I30.8','I30.9','I31.0')
        AND clm_from_dt BETWEEN '2010-01-01' AND '2022-06-30'
    GROUP BY patid
),

-- Step 2: Exclude prior pericarditis (washout)
prior_pericarditis AS (
    SELECT DISTINCT mc.patid
    FROM medical_claims mc
    INNER JOIN index_pericarditis ip ON mc.patid = ip.patid
    WHERE
        mc.dx1 IN ('I30.0','I30.1','I30.8','I30.9','I31.0')
        AND mc.clm_from_dt BETWEEN DATEADD(day, -365, ip.index_date)
                                AND DATEADD(day, -1,   ip.index_date)
),

-- Step 3: Continuous enrollment check
enrolled AS (
    SELECT patid
    FROM enrollment
    GROUP BY patid
    HAVING MIN(enroll_start) <= DATEADD(day, -365, (SELECT MIN(index_date) FROM index_pericarditis ip2 WHERE ip2.patid = enrollment.patid))
       AND MAX(enroll_end)   >= DATEADD(month, 18, (SELECT MIN(index_date) FROM index_pericarditis ip3 WHERE ip3.patid = enrollment.patid))
),

-- Step 4: Cohort
cohort AS (
    SELECT ip.patid, ip.index_date
    FROM index_pericarditis ip
    INNER JOIN enrolled e ON ip.patid = e.patid
    WHERE ip.patid NOT IN (SELECT patid FROM prior_pericarditis)
      AND DATEDIFF(year, dob, ip.index_date) BETWEEN 18 AND 75
),

-- Step 5: Fluoxetine exposure (within 30 days of index)
fluoxetine_exposure AS (
    SELECT DISTINCT c.patid, 1 AS fluoxetine_exposed
    FROM cohort c
    INNER JOIN pharmacy_claims rx ON c.patid = rx.patid
    WHERE
        rx.ndc IN (/* fluoxetine NDC codes */ '00777310502','00093081401')
        AND rx.fill_dt BETWEEN c.index_date AND DATEADD(day, 30, c.index_date)
        AND rx.days_supply >= 30
),

-- Step 6: Confounders (colchicine, NSAIDs, steroids)
confounders AS (
    SELECT
        c.patid,
        MAX(CASE WHEN rx.ndc IN (/* colchicine */ '00603133321') THEN 1 ELSE 0 END) AS colchicine,
        MAX(CASE WHEN rx.ndc IN (/* NSAIDs */    '00591243305','00054491925') THEN 1 ELSE 0 END) AS nsaid,
        MAX(CASE WHEN rx.ndc IN (/* steroids */  '54569136200')  THEN 1 ELSE 0 END) AS steroid,
        MAX(CASE WHEN mc.dx1 LIKE 'F3%' THEN 1 ELSE 0 END) AS depression
    FROM cohort c
    LEFT JOIN pharmacy_claims rx ON c.patid = rx.patid
        AND rx.fill_dt BETWEEN DATEADD(day,-30,c.index_date) AND DATEADD(day,30,c.index_date)
    LEFT JOIN medical_claims mc ON c.patid = mc.patid
        AND mc.clm_from_dt BETWEEN DATEADD(day,-365,c.index_date) AND c.index_date
    GROUP BY c.patid
),

-- Step 7: Outcome (recurrent pericarditis within 18 months)
outcome AS (
    SELECT DISTINCT c.patid, 1 AS recurrence
    FROM cohort c
    INNER JOIN medical_claims mc ON c.patid = mc.patid
    WHERE
        mc.dx1 IN ('I30.0','I30.1','I30.8','I30.9')
        AND mc.clm_from_dt BETWEEN DATEADD(day, 28,  c.index_date)
                               AND DATEADD(month, 18, c.index_date)
)

-- Final analytic dataset
SELECT
    c.patid,
    c.index_date,
    COALESCE(fe.fluoxetine_exposed, 0) AS fluoxetine,
    COALESCE(o.recurrence, 0)          AS recurrence_18mo,
    conf.colchicine,
    conf.nsaid,
    conf.steroid,
    conf.depression
FROM cohort c
LEFT JOIN fluoxetine_exposure fe ON c.patid = fe.patid
LEFT JOIN confounders conf       ON c.patid = conf.patid
LEFT JOIN outcome o              ON c.patid = o.patid
ORDER BY c.patid;
"""

sql_path = os.path.join(OUT_DIR, "claims_query_template.sql")
with open(sql_path, "w") as f:
    f.write(sql_query)
print(f"  Saved: {sql_path}")


# ---------------------------------------------------------------------------
# 8. SAVE RESULTS
# ---------------------------------------------------------------------------

summary = {
    "study": "SSRI-Pericarditis Retrospective",
    "effect_size_model": {
        "p_control_colchicine_alone": p_with_colchicine,
        "p_cvb_etiology": p_cvb_etiology,
        "p_fluoxetine_cvb_clearance": p_fluoxetine_clearance,
        "expected_absolute_risk_difference": round(expected_abs_reduction_fluox, 4),
        "expected_nnt": round(1 / expected_abs_reduction_fluox, 1),
    },
    "power_table": power_table,
    "simulation": {
        "n_per_arm": N_SIM,
        "control_recurrence": round(float(obs_ctrl), 4),
        "treatment_recurrence": round(float(obs_treat), 4),
        "RR": round(float(obs_rr), 3),
        "RR_95CI": [round(float(rr_ci[0]), 3), round(float(rr_ci[1]), 3)],
        "ARD": round(float(obs_rd), 4),
        "ARD_95CI": [round(float(rd_ci[0]), 4), round(float(rd_ci[1]), 4)],
        "NNT": round(float(obs_nnt), 1),
        "chi2_p": round(float(p_chi2), 4),
        "ztest_p": round(float(p_ztest), 4),
        "power": round(float(sim_power), 3),
        "MDE_at_10k": round(float(mde_10k), 4),
    },
    "pubmed_results_count": len(pubmed_results),
    "pubmed_results": pubmed_results[:8],
    "icd10_codes": QUERY_DESIGN["inclusion_criteria"]["index_event"]["icd10_codes"],
}

json_path = os.path.join(RESULTS_DIR, "ssri_retrospective_summary.json")
with open(json_path, "w") as f:
    json.dump(summary, f, indent=2, default=str)
print(f"  Saved: {json_path}")

# Text report
report_path = os.path.join(RESULTS_DIR, "ssri_retrospective_report.txt")
with open(report_path, "w") as f:
    f.write("SSRI-PERICARDITIS RETROSPECTIVE: QUERY DESIGN & POWER ANALYSIS\n")
    f.write("=" * 65 + "\n\n")
    f.write("EFFECT SIZE MODEL\n")
    f.write(f"  Control arm (colchicine alone):       {p_with_colchicine:.0%} recurrence\n")
    f.write(f"  CVB etiology fraction:                {p_cvb_etiology:.0%}\n")
    f.write(f"  Fluoxetine CVB clearance rate:        {p_fluoxetine_clearance:.0%}\n")
    f.write(f"  Expected absolute risk difference:    {expected_abs_reduction_fluox*100:.1f}%\n")
    f.write(f"  Expected NNT:                         {1/expected_abs_reduction_fluox:.0f}\n\n")
    f.write("POWER TABLE (control p=15%, varying fluoxetine effect)\n")
    f.write(f"  {'Reduction':>10} {'p_treat':>8} {'RR':>6} {'NNT':>6} {'n/arm(80%)':>12} {'n/arm(90%)':>12} {'Power@10k':>10}\n")
    for row in power_table:
        f.write(f"  {row['reduction_%']:>9}% {row['p_treatment']:>8.3f} {row['RR']:>6.3f} "
                f"{row['NNT']:>6.1f} {row['n_80pct_power']:>12,} {row['n_90pct_power']:>12,} "
                f"{row['power_at_10k_per_arm']:>10.3f}\n")
    f.write(f"\nSIMULATION (N={N_SIM:,}/arm)\n")
    f.write(f"  Control recurrence:   {obs_ctrl:.4f}\n")
    f.write(f"  Treatment recurrence: {obs_treat:.4f}\n")
    f.write(f"  RR = {obs_rr:.3f} (95% CI {rr_ci[0]:.3f}-{rr_ci[1]:.3f})\n")
    f.write(f"  ARD = {obs_rd:.4f} (95% CI {rd_ci[0]:.4f}-{rd_ci[1]:.4f})\n")
    f.write(f"  NNT = {obs_nnt:.1f}\n")
    f.write(f"  p = {p_ztest:.4g}\n")
    f.write(f"  Power = {sim_power:.1%}\n")
    f.write(f"  MDE at N=10k/arm = {mde_10k*100:.2f}%\n\n")
    f.write("PUBMED RESULTS: fluoxetine AND (pericarditis OR myocarditis)\n")
    f.write(f"  Total records: {len(pubmed_results)}\n")
    for r in pubmed_results[:6]:
        f.write(f"  [{r.get('date','')}] {r.get('title','N/A')[:78]}\n")

print(f"  Saved: {report_path}")
print("\nREQ-007 complete.")
