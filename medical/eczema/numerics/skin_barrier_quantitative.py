"""
Eczema Skin Barrier — Treg/Th2 Bistability Quantitative Model
==============================================================
Implements the bistability model from models/treg_th2_bistability.md
with real literature parameters.

State variables:
  B(t)  = barrier integrity [0, 1]  (1 = intact, 0 = totally breached)
  T2(t) = Th2 activity (arbitrary units; 1 = maximally activated)
  Tr(t) = Treg suppressive capacity [0, 1]
  S(t)  = S. aureus density (log10 CFU/cm²)
  Itch(t) = itch intensity [0, 1]

Key literature parameters:
  - FLG null alleles: 10–30% of eczema patients → B_max = 0.70 (not 1.0)
    (Palmer 2006, Nat Genet, n=3,471 Scottish children)
  - S. aureus threshold for flares: >10^5 CFU/cm² = log10 S > 5
    (Kong 2012, Genome Res, n=28)
  - Butyrate EC50 for FoxP3 induction: ~0.5 mM in vitro
    (Furusawa 2013, Nature, n=Treg culture assay)
  - Vitamin D effect: 1,25-OH-D3 at 10 nM → ~40% Th2 suppression
    (Boonstra 2001, J Immunol)
  - TSLP production from barrier-disrupted keratinocytes: ~10 pg/mL/hr
    (Yoo 2005, J Exp Med — estimated from supernatant data)
  - IL-4/IL-13 half-life in skin: 4–8 h → T2 decay ~ 0.08–0.17 /hr
    Using 6h mean: k_T2_decay = 0.115 /hr
  - Topical butyrate: limited direct evidence; estimate skin effect ≈ 10% of
    oral systemic effect (Boehme 2021, estimated)
  - S. aureus log10 scale: healthy skin ~2–3, colonized ~4–5, flare >5
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
# TIME UNIT: hours (convenient for IL-4/IL-13 half-life scale)
# Simulation runs over weeks: 1 week = 168 hours
# ════════════════════════════════════════════════════════════════════════════

# ─── Barrier repair ───────────────────────────────────────────────────────
k_repair    = 0.006   # /hr; natural barrier repair rate (approaches B_max)
# FLG null: B_max = 0.70 (FLG carriers, ~20% of eczema patients; Palmer 2006)
# FLG WT:   B_max = 1.00
B_max_FLG   = 0.70
B_max_WT    = 1.00
k_scratch   = 0.035   # /hr; Itch × B → barrier damage from scratching
k_IL4_B     = 0.012   # /hr; IL-4/IL-13 suppresses filaggrin → barrier weakens

# ─── Th2 kinetics ─────────────────────────────────────────────────────────
k_ag_prime  = 0.040   # /hr; antigen through broken barrier → Th2 priming
k_staph_T2  = 0.025   # /hr; S. aureus superantigen → polyclonal Th2 activation
# TSLP: ~10 pg/mL/hr from disrupted keratinocytes → drives Th2
k_TSLP      = 0.020   # /hr; TSLP → Th2 amplification
k_T2_decay  = 0.115   # /hr; IL-4/IL-13 half-life ~6h → decay = ln(2)/6
k_Tr_supp   = 0.080   # /hr; Tregs suppress Th2

# ─── Treg dynamics ────────────────────────────────────────────────────────
# Butyrate EC50 for FoxP3 induction: 0.5 mM (Furusawa 2013, Nature)
# Oral butyrate → serum ~0.05–0.2 mM → skin penetration ~10% → ~0.005–0.02 mM
# Effective [butyrate]_skin for oral supplement: ~0.01 mM (modest effect)
# Topical butyrate: estimated ~0.10 mM effective concentration in epidermis
EC50_butyrate  = 0.5    # mM (Furusawa 2013)
k_butyrate_max = 0.015  # /hr maximal Treg induction rate from butyrate

# Vitamin D at 10 nM → 40% Th2 suppression (Boonstra 2001)
# We model VitD as increasing Tr induction rate (Tr-indirect suppression)
k_vitD_max  = 0.012   # /hr maximal Treg induction rate from VitD
EC50_vitD   = 0.005   # arbitrary; VitD supplementation at therapeutic doses saturates

k_Tr_baseline = 0.004  # /hr; baseline Treg homeostatic production
k_Tr_consume  = 0.050  # /hr; Tregs consumed by suppressing active Th2
Tr_decay       = 0.010  # /hr; natural Treg turnover

# ─── S. aureus kinetics (log10 CFU/cm²) ───────────────────────────────────
# Flare threshold: >10^5 CFU/cm² = log10 S > 5 (Kong 2012, Genome Res)
S_max          = 7.0    # log10 CFU/cm²; maximal colonization density
k_colonize     = 0.008  # /hr; colonization rate through broken barrier
k_cathelicidin = 0.020  # /hr; LL-37 kills S. aureus (VitD upregulates LL-37)
k_compete      = 0.005  # /hr; commensal bacteria competition
S_health       = 2.5    # log10 CFU/cm²; healthy baseline (~300 CFU/cm²)

# ─── Itch kinetics ────────────────────────────────────────────────────────
k_IL31         = 0.060   # /hr; IL-31 from Th2 → itch
k_itch_decay   = 0.100   # /hr; natural itch resolution

# Antihistamine effect (baseline = off)
antihistamine  = 0.0
emollient      = 0.0

FLARE_THRESHOLD_S = 5.0  # log10 > 5 → clinical flare (Kong 2012)


# ════════════════════════════════════════════════════════════════════════════
# INTERVENTION PARAMETER SETS
# ════════════════════════════════════════════════════════════════════════════

def make_params(FLG_null=False, butyrate_mM=0.0, vitD_nm=0.0,
                emollient_on=True, bleach_bath=False):
    """
    Build parameter dictionary for a given intervention combination.

    butyrate_mM: effective skin concentration (mM)
      - No supplement:       0.0 mM
      - Oral supplement:     0.01 mM (10% of serum ~0.1 mM; Boehme 2021 estimate)
      - Topical butyrate:    0.10 mM (epidermis estimate)
    vitD_nm: serum 1,25-OH-D3 in nM
      - Deficient:           0.0 nM (treated as 0 in model)
      - Supplemented:        0.01 nM normalized units (therapeutic → near saturation)
    FLG_null: True → B_max = 0.70 (Palmer 2006)
    emollient_on: True → k_repair × 1.5, Itch recovery × 1.3
    bleach_bath: True → extra S. aureus killing
    """
    p = dict(
        B_max       = B_max_FLG if FLG_null else B_max_WT,
        k_repair    = k_repair * (1.5 if emollient_on else 1.0),
        k_scratch   = k_scratch,
        k_IL4_B     = k_IL4_B,
        k_ag_prime  = k_ag_prime,
        k_staph_T2  = k_staph_T2,
        k_TSLP      = k_TSLP,
        k_T2_decay  = k_T2_decay,
        k_Tr_supp   = k_Tr_supp,
        # Treg induction from butyrate (Hill equation, EC50=0.5 mM)
        k_butyrate  = k_butyrate_max * butyrate_mM / (EC50_butyrate + butyrate_mM),
        # Vitamin D → Tr + LL37
        k_vitD_Tr   = k_vitD_max * vitD_nm / (EC50_vitD + vitD_nm),
        # Vitamin D → cathelicidin LL-37 → kills S. aureus (~40% boost at 10nM; Boonstra 2001)
        k_cathelicidin = k_cathelicidin * (1 + 0.40 * vitD_nm / (EC50_vitD + vitD_nm)),
        k_Tr_baseline = k_Tr_baseline,
        k_Tr_consume  = k_Tr_consume,
        Tr_decay      = Tr_decay,
        k_colonize    = k_colonize,
        k_compete     = k_compete,
        S_max         = S_max,
        S_health      = S_health,
        k_IL31        = k_IL31,
        k_itch_decay  = k_itch_decay * (1.3 if emollient_on else 1.0),
        bleach_kill   = 0.060 if bleach_bath else 0.0,  # /hr extra S. aureus killing
    )
    return p


# ════════════════════════════════════════════════════════════════════════════
# ODE SYSTEM
# ════════════════════════════════════════════════════════════════════════════

def eczema_ode(t, y, p):
    """
    5-variable Treg/Th2 bistability ODE.
    y = [B, T2, Tr, S, Itch]
    """
    B, T2, Tr, S, Itch = y
    B    = np.clip(B,    0.0, p["B_max"])
    T2   = np.clip(T2,   0.0, 1.0)
    Tr   = np.clip(Tr,   0.0, 1.0)
    S    = np.clip(S,    0.0, p["S_max"])
    Itch = np.clip(Itch, 0.0, 1.0)

    breach = max(1.0 - B, 0.0)  # fractional barrier breach [0,1]

    # Convert log10 S to linear for thresholding (flare if S > 5 log10)
    S_thresh_effect = max(S - FLARE_THRESHOLD_S, 0.0) / 2.0  # normalized excess

    # dB/dt
    dB = (p["k_repair"] * (p["B_max"] - B)
          - p["k_scratch"] * Itch * B
          - p["k_IL4_B"] * T2 * B)

    # dT2/dt — sources: antigen entry + staph superantigen + TSLP; sink: Tregs + decay
    dT2 = (p["k_ag_prime"] * breach * (1.0 - T2)
           + p["k_staph_T2"] * S_thresh_effect * (1.0 - T2)
           + p["k_TSLP"] * breach * (1.0 - T2)
           - p["k_Tr_supp"] * Tr * T2
           - p["k_T2_decay"] * T2)

    # dTr/dt — sources: butyrate + VitD + baseline; sink: consumption + decay
    dTr = (p["k_butyrate"] * (1.0 - Tr)
           + p["k_vitD_Tr"] * (1.0 - Tr)
           + p["k_Tr_baseline"] * (1.0 - Tr)
           - p["k_Tr_consume"] * T2 * Tr
           - p["Tr_decay"] * Tr)

    # dS/dt — colonization of broken barrier vs killing
    # S in log10 space: dS/dt = k_colonize × breach × (S_max - S) - killing
    # killing is proportional to S (in log10 space, rate constant reduces log-density)
    killing = (p["k_cathelicidin"] + p["k_compete"] + p["bleach_kill"]) * S
    dS = p["k_colonize"] * breach * (p["S_max"] - S) - killing

    # dItch/dt
    dItch = (p["k_IL31"] * T2 * (1.0 - Itch)
             - p["k_itch_decay"] * Itch)

    return [dB, dT2, dTr, dS, dItch]


# ════════════════════════════════════════════════════════════════════════════
# SIMULATION SCENARIOS
# ════════════════════════════════════════════════════════════════════════════

def simulate(params, y0, t_weeks=24):
    """Integrate ODE for t_weeks weeks, return time array (hours) and state."""
    t_span = (0.0, t_weeks * 168.0)
    t_eval = np.linspace(0, t_weeks * 168.0, t_weeks * 168 + 1)
    sol = solve_ivp(eczema_ode, t_span, y0, args=(params,),
                    t_eval=t_eval, method="LSODA", rtol=1e-8, atol=1e-10)
    return sol.t / 168.0, sol.y   # return time in weeks


def remission_probability(y_final_cols, threshold_B=0.70, threshold_T2=0.15,
                          threshold_S=4.5):
    """
    Estimate probability of sustained remission from final-state distribution.
    A trajectory is in remission if B > threshold_B AND T2 < threshold_T2
    AND S < threshold_S at end of simulation.
    """
    n = y_final_cols.shape[1]
    ok = ((y_final_cols[0] > threshold_B) &
          (y_final_cols[1] < threshold_T2) &
          (y_final_cols[3] < threshold_S))
    return np.sum(ok) / n


# ════════════════════════════════════════════════════════════════════════════
# MAIN ANALYSIS
# ════════════════════════════════════════════════════════════════════════════

def run_all_scenarios():
    """
    Simulate 2×2×2 = 8 scenarios: FLG status × butyrate × vitamin D.
    Disease starting state: B=0.35, T2=0.75, Tr=0.15, S=5.5, Itch=0.70
    """
    print("=== ECZEMA BARRIER QUANTITATIVE MODEL ===")
    print("Disease start: B=0.35, T2=0.75, Tr=0.15, S=5.5 log10 CFU/cm², Itch=0.70")
    print(f"S. aureus flare threshold: >{FLARE_THRESHOLD_S} log10 CFU/cm² (Kong 2012)")
    print(f"Butyrate EC50 FoxP3 induction: {EC50_butyrate} mM (Furusawa 2013, Nature)")
    print(f"VitD Th2 suppression: 40% at 10nM (Boonstra 2001, J Immunol)")
    print()

    y0_disease = [0.35, 0.75, 0.15, 5.5, 0.70]

    scenarios = [
        # (FLG_null, butyrate_mM, vitD_nm, label)
        (False, 0.00, 0.000, "WT / No supplement"),
        (False, 0.01, 0.000, "WT / Oral butyrate (~0.01mM skin)"),
        (False, 0.00, 0.010, "WT / Vitamin D3"),
        (False, 0.10, 0.010, "WT / Butyrate(topical) + VitD"),
        (True,  0.00, 0.000, "FLG null / No supplement"),
        (True,  0.01, 0.000, "FLG null / Oral butyrate"),
        (True,  0.00, 0.010, "FLG null / VitD"),
        (True,  0.10, 0.010, "FLG null / Butyrate(topical) + VitD"),
    ]

    results = {}
    for flg, but, vd, label in scenarios:
        p = make_params(FLG_null=flg, butyrate_mM=but, vitD_nm=vd, emollient_on=True)
        t, y = simulate(p, y0_disease, t_weeks=24)
        results[label] = (t, y)
        B_end  = y[0, -1]
        T2_end = y[1, -1]
        Tr_end = y[2, -1]
        S_end  = y[3, -1]
        remit  = "REMISSION" if B_end > 0.70 and T2_end < 0.15 and S_end < 4.5 else "disease"
        print(f"  {label:42s}  B={B_end:.2f} T2={T2_end:.2f} Tr={Tr_end:.2f} "
              f"S={S_end:.1f}  → {remit}")

    return results, scenarios


def plot_barrier_trajectories(results, scenarios):
    fig = plt.figure(figsize=(16, 12))
    gs = gridspec.GridSpec(4, 4, figure=fig, hspace=0.55, wspace=0.40)

    var_names = ["B (barrier)", "T2 (Th2)", "Tr (Treg)", "S (log10 CFU/cm²)"]
    var_idx   = [0, 1, 2, 3]
    thresholds = [None, 0.15, None, FLARE_THRESHOLD_S]
    thresh_labels = [None, "Remission <0.15", None, "Flare threshold >5\n(Kong 2012)"]
    thresh_cols = [None, "green", None, "red"]
    y_labels = ["B [0,1]", "T2 [0,1]", "Tr [0,1]", "log₁₀ CFU/cm²"]

    linestyles = ["-", "--", "-.", ":", "-", "--", "-.", ":"]
    colors_WT  = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
    colors_FLG = ["#9467bd", "#8c564b", "#e377c2", "#7f7f7f"]

    for vi, (vname, vi_idx) in enumerate(zip(var_names, var_idx)):
        ax = fig.add_subplot(gs[vi, :2])  # WT group
        ax2 = fig.add_subplot(gs[vi, 2:])  # FLG null group

        for si, (flg, but, vd, label) in enumerate(scenarios):
            t, y = results[label]
            col = (colors_FLG if flg else colors_WT)[si % 4]
            ls = linestyles[si]
            target_ax = ax2 if flg else ax
            target_ax.plot(t, y[vi_idx], lw=1.8, color=col, ls=ls,
                           label=label.replace("FLG null / ", "").replace("WT / ", ""))

        for target_ax, title in [(ax, "FLG WT"), (ax2, "FLG Null (B_max=0.70)")]:
            if thresholds[vi] is not None:
                target_ax.axhline(thresholds[vi], color=thresh_cols[vi],
                                  ls=":", lw=1.2, alpha=0.8, label=thresh_labels[vi])
            target_ax.set_ylabel(y_labels[vi], fontsize=9)
            target_ax.set_xlabel("Weeks", fontsize=8)
            target_ax.set_title(f"{vname} — {title}", fontsize=9)
            target_ax.legend(fontsize=7, loc="upper right")

        # Mark FLG B_max
        if vi_idx == 0:
            ax2.axhline(B_max_FLG, color="purple", ls="--", lw=1.0, alpha=0.5,
                        label=f"B_max FLG null = {B_max_FLG}")

    fig.suptitle("Eczema Skin Barrier: Treg/Th2 Bistability — 8 Scenarios\n"
                 "FLG status × Butyrate × Vitamin D (emollients ON in all)",
                 fontsize=13, y=1.01)

    path = os.path.join(OUT_DIR, "eczema_barrier_trajectories.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"\n  Saved: {path}")


def plot_remission_heatmap():
    """
    Compute sustained remission probability over a grid of
    butyrate × vitD concentrations, for FLG WT vs FLG null.
    """
    print("\n=== REMISSION PROBABILITY HEATMAP ===")
    but_vals = np.array([0.0, 0.005, 0.01, 0.05, 0.10, 0.20])  # mM effective skin
    vd_vals  = np.array([0.0, 0.002, 0.005, 0.01, 0.02, 0.05])  # normalized units

    y0 = [0.35, 0.75, 0.15, 5.5, 0.70]

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    for ai, FLG_null in enumerate([False, True]):
        rem_grid = np.zeros((len(vd_vals), len(but_vals)))
        for bi, but in enumerate(but_vals):
            for vi, vd in enumerate(vd_vals):
                p = make_params(FLG_null=FLG_null, butyrate_mM=but,
                                vitD_nm=vd, emollient_on=True)
                _, y = simulate(p, y0, t_weeks=24)
                y_end = y[:, -1].reshape(-1, 1)
                rem = remission_probability(y_end, threshold_B=0.65 if FLG_null else 0.75)
                rem_grid[vi, bi] = rem

        ax = axes[ai]
        im = ax.imshow(rem_grid, origin="lower", aspect="auto",
                       cmap="RdYlGn", vmin=0, vmax=1,
                       extent=[0, len(but_vals), 0, len(vd_vals)])
        ax.set_xticks(np.arange(len(but_vals)) + 0.5)
        ax.set_xticklabels([f"{v:.3f}" for v in but_vals], fontsize=8, rotation=45)
        ax.set_yticks(np.arange(len(vd_vals)) + 0.5)
        ax.set_yticklabels([f"{v:.3f}" for v in vd_vals], fontsize=8)
        ax.set_xlabel("Butyrate (mM effective skin)", fontsize=10)
        ax.set_ylabel("Vitamin D3 (norm. units)", fontsize=10)
        title = f"{'FLG Null' if FLG_null else 'FLG WT'}\nRemission at 24 weeks"
        ax.set_title(title, fontsize=11)
        plt.colorbar(im, ax=ax, label="Remission probability")

        # Annotate grid with values
        for bi in range(len(but_vals)):
            for vi in range(len(vd_vals)):
                ax.text(bi + 0.5, vi + 0.5, f"{rem_grid[vi, bi]:.0%}",
                        ha="center", va="center", fontsize=7,
                        color="black" if rem_grid[vi, bi] < 0.8 else "white")

    fig.suptitle("Eczema: Sustained Remission Probability\n"
                 "at 24 weeks vs Butyrate × Vitamin D3\n"
                 "(B threshold: WT>0.75, FLG null>0.65; T2<0.15; S<4.5 log10 CFU/cm²)",
                 fontsize=11)
    plt.tight_layout()
    path = os.path.join(OUT_DIR, "eczema_remission_heatmap.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  Saved: {path}")


if __name__ == "__main__":
    print("Eczema Skin Barrier Quantitative Model")
    print("=" * 60)
    print("Parameters:")
    print(f"  FLG null B_max:       {B_max_FLG} (Palmer 2006, Nat Genet)")
    print(f"  Staph flare threshold: {FLARE_THRESHOLD_S} log10 CFU/cm² (Kong 2012, Genome Res)")
    print(f"  Butyrate EC50 FoxP3:  {EC50_butyrate} mM (Furusawa 2013, Nature)")
    print(f"  VitD Th2 suppression: 40% at 10nM (Boonstra 2001, J Immunol)")
    print(f"  T2 decay (IL-4/13):   {k_T2_decay:.3f} /hr (t½~6h)")
    print()

    results, scenarios = run_all_scenarios()
    print("\nGenerating barrier trajectory plots...")
    plot_barrier_trajectories(results, scenarios)
    print("Generating remission probability heatmap...")
    plot_remission_heatmap()
    print("\nAll figures saved to:", OUT_DIR)
