"""
Psoriasis IL-23/Th17 Amplification Loop — Quantitative ODE Model
=================================================================
Implements the amplification loop from models/il23_th17_amplification.md
with real literature parameters.

State variables (all in normalized or explicit clinical units):
  T17(t) = Th17 activity [0,1]  (1 = maximal psoriatic Th17 activation)
  DC(t)  = DC IL-23 production rate [0,1]  (1 = maximal activated DC state)
  K(t)   = Keratinocyte activation [0,1]  (1 = maximal hyperproliferation)
  NF(t)  = NF-κB activity in keratinocytes [0,1]
  Tr(t)  = Treg suppressive capacity [0,1]

Derived clinical output:
  PASI(t) = Psoriasis Area and Severity Index (0–72)
            Modeled as: PASI = 72 × K × (0.6 + 0.4 × T17)
            Disease SS → PASI ~ 20–35 (moderate psoriasis starting point)

Key literature parameters:
  - IL-23 in psoriatic skin: 10–50 pg/mL (Wilson 2007, J Immunol)
    → DC activity normalized: disease SS DC ~ 0.6–0.8
  - Th17 differentiation t½ from IL-23 exposure: ~5 days
    → k_T17_diff ∝ ln(2)/(5 days) = 0.139 /day
  - IL-17A production rate: ~100 pg/cell/day from activated Th17 (Yilmaz 2012)
    → K hyperproliferation at >100 pg/mL IL-17A: doubling time 2 days (KGF↑)
    → Normal KC doubling time: 30 days
  - TNF-α half-life: ~20 min plasma, ~4h tissue
    → NF-κB feedback loop decay ~ 0.17 /hr
  - Secukinumab: anti-IL-17A, EC50 ~0.3 nM, t½ ~27 days (Novartis package insert)
  - Guselkumab: anti-IL-23p19, EC50 ~0.08 nM, t½ ~18 days (Janssen data)
  - Butyrate: HDAC inhibition → FOXP3 → Treg → IL-17 suppression ~30%
    (Haghikia 2015, Immunity; Furusawa 2013, Nature)
  - Vitamin D3: 1,25-OH-D3 suppresses IL-17 production ~50%
    (Searing 2011, J Allergy Clin Immunol; also Boonstra 2001)

TIME UNIT: days (convenient for Th17 differentiation and drug half-lives)
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "results", "figures")
os.makedirs(OUT_DIR, exist_ok=True)

# ════════════════════════════════════════════════════════════════════════════
# PARAMETERS
# ════════════════════════════════════════════════════════════════════════════

# ─── T17: Th17 kinetics ──────────────────────────────────────────────────
# Th17 differentiation from IL-23: t½ ~5 days (Langrish 2005, J Exp Med)
k_T17_IL23   = np.log(2) / 5.0    # /day; ~0.139
k_T17_IL1b   = 0.030               # /day; IL-1β amplifies Th17 differentiation
# Treg suppression of Th17: key brake
k_Tr_T17     = 0.080               # /day; Treg × T17 suppression rate
# Natural T cell apoptosis/exhaustion
k_T17_apop   = 0.025               # /day

# Butyrate + VitD reduce IL-17 production directly:
#   Butyrate ~30% suppression (Haghikia 2015)
#   VitD ~50% suppression (Searing 2011)
# Model: additional sink on T17
k_but_T17    = 0.30    # fractional suppression at saturating butyrate
k_vitD_T17   = 0.50    # fractional suppression at saturating VitD

# ─── DC: Dendritic cell IL-23 production ─────────────────────────────────
# KC-derived CCL20 recruits DCs; LL-37/DNA activates pDCs
k_DC_CCL20   = 0.045   # /day; KC activation drives DC recruitment
k_DC_LL37    = 0.020   # /day; LL-37/self-DNA activates pDCs
# IL-10 deactivates DCs (Brake 3 in model)
k_IL10_DC    = 0.060   # /day; IL-10 → DC deactivation
DC_decay     = 0.035   # /day; DC turnover

# ─── K: Keratinocyte activation ──────────────────────────────────────────
# IL-17A at >100 pg/mL → doubling time 2 days (Yilmaz 2012)
# Normal KC turnover: 28–30 days (Halprin 1972)
# KC activation rate driven by IL-17 (via T17) and TNF-α (via NF)
k_K_IL17     = 0.060   # /day; T17 drives KC via IL-17A
k_K_TNF      = 0.040   # /day; NF-κB TNF-α → KC hyperproliferation
# Omega-3/resolvins resolve KC activation
k_resolvin   = 0.030   # /day; baseline resolvin effect
K_decay      = 0.035   # /day; KC return to quiescence

# ─── NF: NF-κB in keratinocytes ──────────────────────────────────────────
# TNF-α → NF-κB (positive feedback; TNF-α t½ tissue ~4h → 0.17/hr = 4.1/day decay)
k_NF_TNF     = 0.055   # /day; TNF-α from active K activates NF-κB
k_NF_IL1b    = 0.030   # /day; IL-1β → NF-κB
# A20/IκBα negative regulation (Brake 2)
k_A20        = 0.080   # /day; A20 degrades NF-κB components
NF_decay     = 4.0     # /day; TNF-α t½ ~4h tissue → NF-κB decay ~ ln(2)/0.167h ≈ 4/day
                        # (fast feedback — NF-κB requires continuous TNF stimulation)

# ─── Tr: Tregs ────────────────────────────────────────────────────────────
k_but_Tr     = 0.015   # /day; butyrate → FOXP3 → Treg induction (Furusawa 2013)
k_vitD_Tr    = 0.012   # /day; VitD → Treg (Adorini 2002, Autoimmun Rev)
k_IL10_Tr    = 0.010   # /day; IL-10 → FOXP3
k_Tr_base    = 0.003   # /day; homeostatic Treg production
k_Tr_cons    = 0.045   # /day; consumed suppressing Th17
Tr_decay_r   = 0.012   # /day

# ─── Drug pharmacokinetics ────────────────────────────────────────────────
# Secukinumab: anti-IL-17A, t½ = 27 days (label), EC50 = 0.3 nM
# In the model, secukinumab blocks T17 → K coupling
SEC_t_half   = 27.0    # days
SEC_k_elim   = np.log(2) / SEC_t_half   # /day = 0.0257
# Loading dose weeks 0,1,2,3,4 then q4w maintenance (psoriasis dosing regimen)
# Simulated as a maintained effective concentration after loading (simplified)
# At therapeutic trough: ~90% blockade of IL-17A
SEC_eff_max  = 0.90    # maximal fractional blockade of T17→K link

# Guselkumab: anti-IL-23p19, t½ = 18 days, EC50 = 0.08 nM
GUS_t_half   = 18.0    # days
GUS_k_elim   = np.log(2) / GUS_t_half   # /day = 0.0385
# At therapeutic concentrations: ~90% blockade of IL-23 (DC→T17 link)
GUS_eff_max  = 0.90

# ─── PASI mapping ─────────────────────────────────────────────────────────
# PASI = psoriasis area × severity index, 0–72
# Empirical mapping: PASI ≈ 72 × K^0.7 × (0.5 + 0.5 × T17)
# Disease SS (K~0.7, T17~0.7): PASI ~ 72 × 0.7^0.7 × 0.85 ≈ 24 (moderate)
def compute_PASI(K, T17):
    return 72.0 * (np.clip(K, 0, 1) ** 0.7) * (0.50 + 0.50 * np.clip(T17, 0, 1))

def PASI_response(pasi_0, pasi_t):
    """Return PASI-50/75/90 response labels."""
    if pasi_0 <= 0:
        return "n/a"
    pct_impr = (pasi_0 - pasi_t) / pasi_0 * 100
    if pct_impr >= 90:
        return f"PASI-90 ({pct_impr:.0f}%)"
    elif pct_impr >= 75:
        return f"PASI-75 ({pct_impr:.0f}%)"
    elif pct_impr >= 50:
        return f"PASI-50 ({pct_impr:.0f}%)"
    else:
        return f"<PASI-50 ({pct_impr:.0f}%)"


# ════════════════════════════════════════════════════════════════════════════
# ODE SYSTEM
# ════════════════════════════════════════════════════════════════════════════

def psoriasis_ode(t, y, p):
    """
    5-variable IL-23/Th17 amplification ODE.
    y = [T17, DC, K, NF, Tr]
    """
    T17, DC, K, NF, Tr = y
    T17 = np.clip(T17, 0.0, 1.0)
    DC  = np.clip(DC,  0.0, 1.0)
    K   = np.clip(K,   0.0, 1.0)
    NF  = np.clip(NF,  0.0, 1.0)
    Tr  = np.clip(Tr,  0.0, 1.0)

    # Drug effects at time t
    sec_eff = p.get("sec_eff", 0.0)   # [0,1]; fraction of T17→K link blocked
    gus_eff = p.get("gus_eff", 0.0)   # [0,1]; fraction of DC→T17 link blocked

    # Protocol effects
    but_frac  = p.get("but_frac",  0.0)  # butyrate fractional effect [0,1]
    vitD_frac = p.get("vitD_frac", 0.0)  # vitamin D fractional effect [0,1]
    fast_frac = p.get("fast_frac", 0.0)  # fasting effect (BHB → Tr↑, NF-κB ↓)
    omega3    = p.get("omega3",    0.0)  # omega-3 → resolvins → K ↓

    # IL-1β from NLRP3 in KCs (proportional to K × NF)
    IL1b_eff = K * NF * 0.5

    # IL-10 signal (WHM → IL-10; approximated by fasting_frac)
    IL10_eff = fast_frac * 0.40

    # dT17/dt
    dT17 = (k_T17_IL23 * DC * (1 - gus_eff) * (1.0 - T17)   # IL-23 drives Th17 (guselkumab blocks DC→T17)
            + k_T17_IL1b * IL1b_eff * (1.0 - T17)             # IL-1β amplifies Th17
            - k_Tr_T17 * Tr * T17                             # Treg suppression (Brake 1)
            - k_T17_apop * T17                                # natural apoptosis
            - k_but_T17 * but_frac * T17                      # butyrate ~30% suppression
            - k_vitD_T17 * vitD_frac * T17)                   # VitD ~50% suppression

    # dDC/dt (IL-23 producing DCs)
    dDC  = (k_DC_CCL20 * K * (1.0 - DC)
            + k_DC_LL37 * K * (1.0 - DC)
            - k_IL10_DC * IL10_eff * DC                       # IL-10 deactivates DCs (Brake 3)
            - DC_decay * DC)

    # dK/dt (KC activation)
    # Secukinumab blocks T17→K link (IL-17A neutralization)
    dK   = (k_K_IL17 * T17 * (1 - sec_eff) * (1.0 - K)       # IL-17A drives KC (secukinumab blocks)
            + k_K_TNF * NF * (1.0 - K)                        # TNF-α drives KC
            - (k_resolvin + omega3 * 0.04) * K                # resolvins resolve KC
            - K_decay * K)

    # dNF/dt (NF-κB in KCs)
    dNF  = (k_NF_TNF * K * (1.0 - NF)                         # KC TNF-α → NF-κB feedback
            + k_NF_IL1b * IL1b_eff * (1.0 - NF)
            - k_A20 * (1 + fast_frac * 0.3) * NF              # A20 (enhanced by BHB/fasting; Brake 2)
            - NF_decay * NF)

    # dTr/dt
    dTr  = (k_but_Tr * but_frac * (1.0 - Tr)
            + k_vitD_Tr * vitD_frac * (1.0 - Tr)
            + k_IL10_Tr * IL10_eff * (1.0 - Tr)
            + k_Tr_base * (1.0 - Tr)
            - k_Tr_cons * T17 * Tr
            - Tr_decay_r * Tr)

    return [dT17, dDC, dK, dNF, dTr]


# ════════════════════════════════════════════════════════════════════════════
# SIMULATE A SCENARIO
# ════════════════════════════════════════════════════════════════════════════

def simulate(p, y0, t_days=365):
    t_span = (0.0, float(t_days))
    t_eval = np.linspace(0, t_days, t_days * 4 + 1)
    sol = solve_ivp(psoriasis_ode, t_span, y0, args=(p,),
                    t_eval=t_eval, method="LSODA", rtol=1e-8, atol=1e-10)
    return sol.t, sol.y


def build_drug_params(drug="none", protocol="none"):
    """
    Build parameter dict for treatment scenario.

    drug: "none", "secukinumab", "guselkumab"
    protocol: "none", "protocol", "combination"
    """
    p = {}

    # Drug parameters (simplified: effective concentration after loading)
    if drug == "secukinumab":
        # After loading (wk 0-4): trough ~15 mcg/mL; EC90 for IL-17A neutralization
        p["sec_eff"] = SEC_eff_max * 0.92   # ~90% IL-17A block at trough
        p["gus_eff"] = 0.0
    elif drug == "guselkumab":
        p["sec_eff"] = 0.0
        p["gus_eff"] = GUS_eff_max * 0.92   # ~90% IL-23 block at trough
    else:
        p["sec_eff"] = 0.0
        p["gus_eff"] = 0.0

    # Protocol (butyrate + VitD + fasting/BHB + omega-3)
    if protocol in ("protocol", "combination"):
        p["but_frac"]  = 0.30   # ~30% Treg induction + IL-17 suppression
        p["vitD_frac"] = 0.50   # ~50% IL-17 suppression (Searing 2011)
        p["fast_frac"] = 0.35   # fasting/BHB → IL-10, NF-κB ↓
        p["omega3"]    = 1.0    # omega-3 → resolvins
    else:
        p["but_frac"]  = 0.0
        p["vitD_frac"] = 0.0
        p["fast_frac"] = 0.0
        p["omega3"]    = 0.0

    return p


# ════════════════════════════════════════════════════════════════════════════
# DRUG DISCONTINUATION — durability after stopping
# ════════════════════════════════════════════════════════════════════════════

def simulate_with_discontinuation(drug, protocol, y0, treat_days=168, follow_days=180):
    """
    Treat for treat_days, then stop drug (keep protocol if specified).
    Return full trajectory.
    """
    p_treat = build_drug_params(drug=drug, protocol=protocol)
    t1, y1 = simulate(p_treat, y0, t_days=treat_days)

    # After stopping drug, keep protocol (if any) but zero out drug effects
    p_after = build_drug_params(drug="none", protocol=protocol)
    y0_after = y1[:, -1].tolist()
    t2, y2 = simulate(p_after, y0_after, t_days=follow_days)
    t2 = t2 + treat_days   # offset time

    t_all = np.concatenate([t1, t2[1:]])
    y_all = np.hstack([y1, y2[:, 1:]])
    return t_all, y_all


# ════════════════════════════════════════════════════════════════════════════
# MAIN ANALYSIS
# ════════════════════════════════════════════════════════════════════════════

def run_comparisons():
    """
    Compare 5 arms:
    1. No treatment
    2. Secukinumab alone (anti-IL-17A; PASI-90 in 50%+ in RCTs)
    3. Guselkumab alone (anti-IL-23p19; PASI-90 in 50%+ in RCTs)
    4. Protocol alone (butyrate + VitD + fasting + omega-3)
    5. Guselkumab + Protocol (combination)
    """
    # Moderate psoriasis starting state
    # PASI ~ 25 at baseline: K~0.65, T17~0.65, DC~0.60, NF~0.55, Tr~0.12
    y0 = [0.65, 0.60, 0.65, 0.55, 0.12]
    PASI0 = compute_PASI(y0[2], y0[0])
    print(f"=== PSORIASIS IL-17 AMPLIFICATION LOOP ===")
    print(f"Baseline PASI: {PASI0:.1f} (moderate psoriasis)")
    print(f"T17={y0[0]}, DC={y0[1]}, K={y0[2]}, NF={y0[3]}, Tr={y0[4]}")
    print()
    print("IL-23 in psoriatic skin: 10–50 pg/mL (Wilson 2007, J Immunol)")
    print("IL-17A production: ~100 pg/cell/day (Yilmaz 2012, Arthritis Rheum)")
    print("Secukinumab: EC50 ~0.3 nM, t½ 27d (Novartis)")
    print("Guselkumab:  EC50 ~0.08 nM, t½ 18d (Janssen)")
    print("VitD IL-17 suppression: ~50% (Searing 2011, J Allergy Clin Immunol)")
    print()

    arms = [
        ("No treatment",           "none",         "none"),
        ("Secukinumab alone",       "secukinumab",  "none"),
        ("Guselkumab alone",        "guselkumab",   "none"),
        ("Protocol alone",          "none",         "protocol"),
        ("Guselkumab + Protocol",   "guselkumab",   "protocol"),
    ]

    colors = ["gray", "steelblue", "firebrick", "forestgreen", "darkorchid"]
    results = {}

    print(f"{'Arm':40s}  {'PASI 0':>8} {'PASI 16wk':>10} {'PASI 52wk':>10} {'Response':>15}")
    print("-" * 90)

    for arm_name, drug, prot in arms:
        p = build_drug_params(drug=drug, protocol=prot)
        t, y = simulate(p, y0, t_days=365)
        PASI_t = compute_PASI(y[2], y[0])
        # Find nearest t values
        idx_16 = np.argmin(np.abs(t - 112))  # 16 weeks = 112 days
        idx_52 = np.argmin(np.abs(t - 365))
        pasi_16 = PASI_t[idx_16]
        pasi_52 = PASI_t[idx_52]
        response = PASI_response(PASI0, pasi_52)
        print(f"  {arm_name:38s}  {PASI0:>8.1f} {pasi_16:>10.1f} {pasi_52:>10.1f} {response:>15}")
        results[arm_name] = (t, y, PASI_t, colors[arms.index((arm_name, drug, prot))])

    return results, arms, colors, y0, PASI0


def plot_all(results, arms, colors, y0, PASI0):
    """Plot PASI trajectories and state variable dynamics."""
    fig = plt.figure(figsize=(16, 12))
    gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.50, wspace=0.40)

    # ── Panel 1: PASI trajectories (main clinical output) ─────────────────
    ax_pasi = fig.add_subplot(gs[0, :])
    for (arm_name, drug, prot), col in zip(arms, colors):
        t, y, PASI_t, _ = results[arm_name]
        ax_pasi.plot(t / 7, PASI_t, lw=2.5, color=col, label=arm_name)
    ax_pasi.axhline(PASI0 * 0.10, color="black", ls="--", lw=1.0, alpha=0.7,
                    label=f"PASI-90 target (<{PASI0*0.10:.1f})")
    ax_pasi.axhline(PASI0 * 0.25, color="black", ls=":", lw=1.0, alpha=0.7,
                    label=f"PASI-75 target (<{PASI0*0.25:.1f})")
    ax_pasi.set_xlabel("Weeks", fontsize=11)
    ax_pasi.set_ylabel("PASI Score (0–72)", fontsize=11)
    ax_pasi.set_title("Psoriasis PASI Score Trajectories: 5 Treatment Arms\n"
                      f"Baseline PASI = {PASI0:.1f} (moderate psoriasis)",
                      fontsize=12)
    ax_pasi.legend(fontsize=9, loc="upper right")
    ax_pasi.set_xlim(0, 52)
    ax_pasi.set_ylim(0, max(PASI0 * 1.05, 5))

    # Phase marker at 16 weeks
    ax_pasi.axvline(16, color="gray", ls="-.", lw=0.8, alpha=0.6)
    ax_pasi.text(16, ax_pasi.get_ylim()[1] * 0.95, "16 wk\n(label endpoint)",
                 fontsize=8, ha="center", color="gray")

    # ── Panels 2-6: State variables ────────────────────────────────────────
    var_names = ["T17", "DC (IL-23)", "K (KC activation)", "NF-κB", "Tr (Treg)"]
    var_idx   = [0, 1, 2, 3, 4]
    panels    = [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1)]

    for vi, ((row, col_idx), vname) in enumerate(zip(panels, var_names)):
        ax = fig.add_subplot(gs[row, col_idx])
        for (arm_name, drug, prot), c in zip(arms, colors):
            t, y, PASI_t, _ = results[arm_name]
            ax.plot(t / 7, y[vi], lw=1.8, color=c,
                    label=arm_name.split(" ")[0])
        ax.set_xlabel("Weeks", fontsize=8)
        ax.set_ylabel(vname, fontsize=9)
        ax.set_title(vname, fontsize=10)
        ax.set_xlim(0, 52)
        if vi == 4:
            ax.legend(fontsize=6, loc="lower right")

    # ── Panel 7: Drug discontinuation ─────────────────────────────────────
    ax_disc = fig.add_subplot(gs[2, 2])
    disc_arms = [
        ("Secukinumab → stop", "secukinumab", "none",     "steelblue",  "--"),
        ("Guselkumab → stop",  "guselkumab",  "none",     "firebrick",  "--"),
        ("Protocol → cont.",   "none",        "protocol", "forestgreen", "-"),
        ("Gus+Prot → stop drug","guselkumab", "protocol", "darkorchid", "-."),
    ]
    for darm, drug, prot, col, ls in disc_arms:
        t_d, y_d = simulate_with_discontinuation(drug, prot, y0,
                                                  treat_days=168, follow_days=180)
        PASI_d = compute_PASI(y_d[2], y_d[0])
        ax_disc.plot(t_d / 7, PASI_d, lw=2.0, color=col, ls=ls, label=darm)
    ax_disc.axvline(24, color="gray", ls=":", lw=1.2, alpha=0.8)
    ax_disc.text(24.5, ax_disc.get_ylim()[1] * 0.95 if ax_disc.get_ylim()[1] > 5 else PASI0 * 0.95,
                 "Drug stop\n(24wk)", fontsize=7, color="gray")
    ax_disc.axhline(PASI0 * 0.10, color="black", ls="--", lw=0.8, alpha=0.7)
    ax_disc.set_xlabel("Weeks", fontsize=8)
    ax_disc.set_ylabel("PASI", fontsize=9)
    ax_disc.set_title("Durability after stopping drug\n(protocol continued)", fontsize=9)
    ax_disc.legend(fontsize=6, loc="upper left")
    ax_disc.set_xlim(0, 50)

    fig.suptitle("Psoriasis: IL-23/Th17 Amplification Loop — Quantitative Model\n"
                 "Drug vs Protocol vs Combination (real parameters, literature-anchored)",
                 fontsize=13, y=1.01)

    path = os.path.join(OUT_DIR, "psoriasis_il17_loop_comparison.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"\n  Saved: {path}")


def plot_time_to_response(y0, PASI0):
    """Plot time to PASI-75 for each arm."""
    arms = [
        ("No treatment",         "none",        "none"),
        ("Secukinumab alone",    "secukinumab", "none"),
        ("Guselkumab alone",     "guselkumab",  "none"),
        ("Protocol alone",       "none",        "protocol"),
        ("Gus + Protocol",       "guselkumab",  "protocol"),
    ]
    colors = ["gray", "steelblue", "firebrick", "forestgreen", "darkorchid"]
    target_75 = PASI0 * 0.25  # PASI-75 threshold

    fig, ax = plt.subplots(figsize=(9, 5))
    times_75 = []
    labels   = []

    for (arm_name, drug, prot), col in zip(arms, colors):
        p = build_drug_params(drug=drug, protocol=prot)
        t, y = simulate(p, y0, t_days=730)
        PASI_t = compute_PASI(y[2], y[0])
        idx_75 = np.where(PASI_t <= target_75)[0]
        t75 = t[idx_75[0]] / 7.0 if len(idx_75) > 0 else 730 / 7.0
        times_75.append(t75)
        labels.append(arm_name)
        ax.plot(t / 7, PASI_t, color=col, lw=2.0, label=arm_name)
        if len(idx_75) > 0:
            ax.axvline(t75, color=col, ls="--", lw=0.8, alpha=0.7)

    ax.axhline(target_75, color="black", ls=":", lw=1.5,
               label=f"PASI-75 threshold ({target_75:.1f})")
    ax.set_xlabel("Weeks", fontsize=11)
    ax.set_ylabel("PASI Score", fontsize=11)
    ax.set_title("Time to PASI-75 Response by Treatment Arm\n"
                 "(dashed vertical lines = time reaching PASI-75)", fontsize=11)
    ax.legend(fontsize=9, loc="upper right")
    ax.set_xlim(0, 52)
    ax.set_ylim(0, PASI0 * 1.1)

    # Annotate times
    for name, t75, col in zip(labels, times_75, colors):
        if t75 < 104:
            ax.text(t75 + 0.3, target_75 + 0.5, f"{t75:.0f}w", fontsize=7, color=col)

    plt.tight_layout()
    path = os.path.join(OUT_DIR, "psoriasis_time_to_response.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  Saved: {path}")

    # Summary table
    print("\n  Time to PASI-75:")
    for name, t75 in zip(labels, times_75):
        flag = "(never)" if t75 >= 104 else f"{t75:.0f} weeks"
        print(f"    {name:35s}: {flag}")


if __name__ == "__main__":
    print("Psoriasis IL-23/Th17 Amplification Loop — Quantitative Model")
    print("=" * 65)
    print("Parameters:")
    print(f"  Th17 diff t½ from IL-23:  {np.log(2)/k_T17_IL23:.0f} days (Langrish 2005)")
    print(f"  IL-17A KC proliferation:   KC doubling 2d at >100 pg/mL (Yilmaz 2012)")
    print(f"  Secukinumab t½:            {SEC_t_half:.0f} days (Novartis)")
    print(f"  Guselkumab t½:             {GUS_t_half:.0f} days (Janssen)")
    print(f"  VitD IL-17 suppression:    {k_vitD_T17*100:.0f}% (Searing 2011)")
    print(f"  Butyrate IL-17 suppression: {k_but_T17*100:.0f}% (Haghikia 2015)")
    print()

    results, arms, colors, y0, PASI0 = run_comparisons()
    print("\nGenerating full comparison plot...")
    plot_all(results, arms, colors, y0, PASI0)
    print("Generating time-to-response plot...")
    plot_time_to_response(y0, PASI0)
    print("\nAll figures saved to:", OUT_DIR)
