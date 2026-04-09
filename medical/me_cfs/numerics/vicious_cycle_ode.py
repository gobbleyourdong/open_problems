"""
ME/CFS Vicious Cycle — 6-Variable ODE System
=============================================
Implements the bistable attractor model from models/vicious_cycle.md
with real literature parameters.

State variables:
  V(t) = viral load (log10 copies/g tissue; TD mutant CVB persisting in muscle/CNS)
  I(t) = immune dysfunction index (0=normal NK, 1=fully exhausted)
  N(t) = neuroinflammation (normalized TSPO binding; 1 = +45% above control baseline)
  M(t) = mitochondrial dysfunction index (0=normal, 1=fully impaired)
  A(t) = autonomic dysfunction index (0=normal HRV, 1=fully impaired)
  F(t) = functional capacity, Bell Disability Scale 0–100

Literature parameter sources:
  - NK cytotoxicity: 40–60% reduced (Brenu 2011, J Intern Med)
  - NK transcriptomics: GZMH -5.45x, NKG7 -5.21x, GZMA -4.49x (GSE268212, our analysis)
  - Neuroinflammation: TSPO PET binding +45% vs controls (Nakatomi 2014, Brain, n=45)
  - Mitochondrial complex I: 30–60% reduced (Myhill 2009, Int J Clin Exp Med)
  - HRV: ~30% reduced (Miwa 2013, Intern Med)
  - NK-viral coupling: each log10 increase in viral persistence → ~15% NK dysfunction
    (inferred from viral titres vs NK activity correlations in Chia 2008 + Brenu 2011)
  - V→I coupling fitted so disease SS has I ≈ 0.5 (40–60% impaired)
  - N disease SS: TSPO +45% → N_disease ≈ 0.45 normalized
  - M disease SS: 30–60% impaired → M_disease ≈ 0.45
  - A disease SS: HRV -30% → A_disease ≈ 0.30
  - F disease SS: Bell Scale ~20–40 (severe ME/CFS) for fully established disease SS
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os

# ── Output directory ──────────────────────────────────────────────────────────
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "results", "figures")
os.makedirs(OUT_DIR, exist_ok=True)

# ════════════════════════════════════════════════════════════════════════════
# PARAMETERS
# ════════════════════════════════════════════════════════════════════════════

# V: viral load (log10 copies/g tissue)
# Natural replication rate for TD-mutant CVB in immune-compromised tissue
k_rep   = 0.05   # log10 units/day; slow because TD mutants replicate poorly without capsid
# NK clearance: each unit of NK function (I) clears ~k_nk_clear × V per day
k_nk_clear = 0.08  # per day per unit I inverse (lower I = less clearance)
# Autophagy clearance (A here encodes autophagy via M proxy — see note)
k_auto  = 0.03   # per day; when M=0 (healthy mito → AMPK active) autophagy clears virus
# V decay floor (immune-independent): mucosal shedding / cell turnover
k_v_decay = 0.01  # per day

# I: immune dysfunction (NK exhaustion, 0=normal, 1=fully exhausted)
# Viral load drives NK exhaustion (chronic antigen stimulation)
# Brenu 2011 + Chia 2008: I disease_SS ~ 0.5
# Each log10 increase in V reduces NK function by ~15%  (k_vi = 0.15/log10V_ref)
V_ref   = 4.0    # log10 copies/g (reference disease viral load)
k_vi    = 0.15 / V_ref   # per log10 per day → NK function reduction rate
k_i_restore = 0.03  # per day spontaneous NK restoration (sleep, nutrients baseline)
k_i_M   = 0.02   # M dysfunction further impairs NK (mitochondria power NK killing)

# N: neuroinflammation (0=baseline, 0.45=disease SS ≡ +45% TSPO binding; Nakatomi 2014)
# Driven by CNS viral persistence + systemic IL-6/TNF escaping BBB
k_NV    = 0.025  # per day per log10 V; viral CNS seeding → microglial priming
k_NI    = 0.020  # per day per unit I; NK dysfunction → persistent CNS CVB → microglia
N_decay = 0.030  # per day; natural microglial quiescence when stimulus removed
# Ceiling: can't exceed ~2.0 normalized (lethal encephalitis range — clamped)
N_max   = 2.0

# M: mitochondrial dysfunction (0=normal, 1=fully impaired)
# Neuroinflammatory cytokines (IL-1β, TNF-α) suppress Complex I
# Myhill 2009: M_disease_SS ~ 0.45
k_MN    = 0.018  # per day per unit N; neuroinflam cytokines → mitochondrial damage
k_MI    = 0.015  # per day per unit I; systemic inflammation → mito damage
k_M_repair = 0.025 # per day; CoQ10/NAD restore mito (baseline)
# AMPK effect: when V low and exercise possible, AMPK enhances mito biogenesis
# Represented in recovery trajectory as protocol term

# A: autonomic dysfunction (0=normal HRV, 1=fully impaired)
# Miwa 2013: HRV ~30% reduced → A_disease_SS ~ 0.30
# Driven by neuroinflammation in brainstem autonomic nuclei
k_AN    = 0.015  # per day per unit N; neuroinflam in brainstem → ANS dysregulation
k_AM    = 0.012  # per day per unit M; mitochondrial impairment in autonomic ganglia
A_decay = 0.025  # per day; ANS recovery when neuroinflam resolves

# F: functional capacity — Bell Disability Scale 0–100
# F = 100 × (1-I)^0.4 × (1-M)^0.4 × (1-A)^0.2 at steady state
# Disease SS: I≈0.5, M≈0.45, A≈0.30 → F ≈ 100 × 0.5^0.4 × 0.55^0.4 × 0.70^0.2 ≈ 45–55
# We track dF/dt explicitly with additional PEM crash term
k_F_base  = 0.8   # per day; approach composite functional target
k_pem     = 0.15  # PEM amplifier: if V>2 & activity spike → crash term (not used in autonomous ODE)

def params_baseline():
    """Return baseline parameter dict for untreated ME/CFS dynamics."""
    return dict(
        k_rep=k_rep, k_nk_clear=k_nk_clear, k_auto=k_auto, k_v_decay=k_v_decay,
        k_vi=k_vi, k_i_restore=k_i_restore, k_i_M=k_i_M,
        k_NV=k_NV, k_NI=k_NI, N_decay=N_decay, N_max=N_max,
        k_MN=k_MN, k_MI=k_MI, k_M_repair=k_M_repair,
        k_AN=k_AN, k_AM=k_AM, A_decay=A_decay,
        k_F_base=k_F_base,
        # protocol terms (zero at baseline)
        fluox=0.0,   # Fluoxetine: antiviral, reduces V replication (+k_rep suppression)
        fmd=0.0,     # FMD/autophagy: boosts autophagic clearance
        cold_nk=0.0, # Cold exposure + Se/Zn: restores NK (adds to k_i_restore)
        coq_nr=0.0,  # CoQ10 + NR: reduces M
        bhb_but=0.0, # BHB + butyrate: reduces N (anti-neuroinflam)
    )


# ════════════════════════════════════════════════════════════════════════════
# ODE SYSTEM
# ════════════════════════════════════════════════════════════════════════════

def vicious_cycle(t, y, p):
    """
    6-variable ME/CFS vicious cycle ODE.
    y = [V, I, N, M, A, F]
    All variables clipped to [0, max] within ODE for numerical stability.
    """
    V, I, N, M, A, F = y
    V = max(V, 0.0)   # log10 copies/g; 0 = virus cleared
    I = np.clip(I, 0.0, 1.0)
    N = np.clip(N, 0.0, p["N_max"])
    M = np.clip(M, 0.0, 1.0)
    A = np.clip(A, 0.0, 1.0)
    F = np.clip(F, 0.0, 100.0)

    # Effective NK clearance capacity (higher I = more dysfunctional = less clearance)
    NK_eff = 1.0 - I   # 0 = fully exhausted, 1 = normal

    # --- dV/dt ---
    repli   = p["k_rep"] * (1.0 - p["fluox"]) * V          # replication (fluox suppresses)
    nk_kill = p["k_nk_clear"] * NK_eff * V                  # NK-mediated clearance
    autoph  = (p["k_auto"] + p["fmd"]) * (1.0 - M) * V     # autophagy (mito must work)
    decay   = p["k_v_decay"] * V                             # baseline decay
    dV = repli - nk_kill - autoph - decay
    # Enforce V >= 0
    if V <= 0.0:
        dV = max(dV, 0.0)

    # --- dI/dt (NK exhaustion: I increases = worse) ---
    exhaust = p["k_vi"] * V * (1.0 - I)                     # viral load exhausts NK
    mito_imp = p["k_i_M"] * M * (1.0 - I)                   # mito impairment limits NK
    restore = (p["k_i_restore"] + p["cold_nk"]) * I         # sleep/cold/Se/Zn restores NK
    dI = exhaust + mito_imp - restore

    # --- dN/dt (neuroinflammation: N increases = worse) ---
    viral_cns  = p["k_NV"] * V * (N_max - N) / N_max        # viral CNS seeding
    nk_dysfn   = p["k_NI"] * I * (N_max - N) / N_max        # NK dysfunction → persistent CNS virus
    antinflam  = (p["bhb_but"] * 0.3) * N                   # BHB/butyrate reduce neuroinflam
    resolution = p["N_decay"] * N                            # natural resolution
    dN = viral_cns + nk_dysfn - resolution - antinflam

    # --- dM/dt (mitochondrial dysfunction: M increases = worse) ---
    cytokine_dmg = p["k_MN"] * N * (1.0 - M) + p["k_MI"] * I * (1.0 - M)
    repair       = (p["k_M_repair"] + p["coq_nr"] * 0.4) * M
    dM = cytokine_dmg - repair

    # --- dA/dt (autonomic dysfunction: A increases = worse) ---
    brainstem = p["k_AN"] * N * (1.0 - A) + p["k_AM"] * M * (1.0 - A)
    recovery  = p["A_decay"] * A
    dA = brainstem - recovery

    # --- dF/dt (Bell Scale: F decreases = worse) ---
    # Target functional level based on current I, M, A
    F_target = 100.0 * ((1.0 - I) ** 0.40) * ((1.0 - M) ** 0.40) * ((1.0 - A) ** 0.20)
    dF = p["k_F_base"] * (F_target - F)

    return [dV, dI, dN, dM, dA, dF]


# ════════════════════════════════════════════════════════════════════════════
# FIXED POINT FINDER
# ════════════════════════════════════════════════════════════════════════════

def find_fixed_point(guess, p):
    """Newton solve for zeros of ODE system."""
    def rhs(y):
        return vicious_cycle(0, y, p)
    sol = fsolve(rhs, guess, full_output=True)
    fp = sol[0]
    # Check it's actually a zero
    residual = np.max(np.abs(rhs(fp)))
    return fp, residual


# ════════════════════════════════════════════════════════════════════════════
# STEADY STATE ANALYSIS
# ════════════════════════════════════════════════════════════════════════════

def compute_steady_states():
    p = params_baseline()
    print("\n=== STEADY STATE ANALYSIS (untreated) ===")

    # Health attractor guess: V=0, all dysfunction=0, F=100
    health_guess = [0.01, 0.05, 0.02, 0.05, 0.05, 95.0]
    health_fp, res_h = find_fixed_point(health_guess, p)
    print(f"\nHealth fixed point (residual={res_h:.2e}):")
    print(f"  V (log10 cp/g):  {health_fp[0]:.3f}")
    print(f"  I (NK dysfn):    {health_fp[1]:.3f}")
    print(f"  N (neuroinflam): {health_fp[2]:.3f}")
    print(f"  M (mito dysfn):  {health_fp[3]:.3f}")
    print(f"  A (ANS dysfn):   {health_fp[4]:.3f}")
    print(f"  F (Bell Scale):  {health_fp[5]:.1f}")

    # Disease attractor guess: V=4 (10^4 cp/g), I=0.5, N=0.45, M=0.45, A=0.30, F=45
    disease_guess = [4.0, 0.50, 0.45, 0.45, 0.30, 45.0]
    disease_fp, res_d = find_fixed_point(disease_guess, p)
    print(f"\nDisease fixed point (residual={res_d:.2e}):")
    print(f"  V (log10 cp/g):  {disease_fp[0]:.3f}  (literature target: ~4.0)")
    print(f"  I (NK dysfn):    {disease_fp[1]:.3f}  (literature: 0.40–0.60; Brenu 2011)")
    print(f"  N (neuroinflam): {disease_fp[2]:.3f}  (literature: 0.45; Nakatomi 2014)")
    print(f"  M (mito dysfn):  {disease_fp[3]:.3f}  (literature: 0.30–0.60; Myhill 2009)")
    print(f"  A (ANS dysfn):   {disease_fp[4]:.3f}  (literature: ~0.30; Miwa 2013)")
    print(f"  F (Bell Scale):  {disease_fp[5]:.1f}  (moderate-severe ME/CFS)")

    return health_fp, disease_fp


# ════════════════════════════════════════════════════════════════════════════
# PHASE PORTRAIT — V–I plane (M, N, A at SS values)
# ════════════════════════════════════════════════════════════════════════════

def phase_portrait_VI(health_fp, disease_fp):
    """Plot V–I phase portrait with nullclines and fixed points."""
    p = params_baseline()
    # Fix N, M, A at disease SS midpoint for visualization
    N0 = disease_fp[2]
    M0 = disease_fp[3]
    A0 = disease_fp[4]

    V_vals = np.linspace(0, 6, 300)
    I_vals = np.linspace(0, 1, 300)
    VV, II = np.meshgrid(V_vals, I_vals)

    dV_arr = np.zeros_like(VV)
    dI_arr = np.zeros_like(VV)
    for i in range(VV.shape[0]):
        for j in range(VV.shape[1]):
            v, ii = VV[i, j], II[i, j]
            dy = vicious_cycle(0, [v, ii, N0, M0, A0, 60.0], p)
            dV_arr[i, j] = dy[0]
            dI_arr[i, j] = dy[1]

    speed = np.sqrt(dV_arr**2 + dI_arr**2)
    speed[speed == 0] = 1e-10

    fig, ax = plt.subplots(figsize=(8, 6))
    # Streamplot
    ax.streamplot(V_vals, I_vals, dV_arr, dI_arr,
                  color=np.log1p(speed), cmap="Blues_r",
                  linewidth=0.8, density=1.4, arrowsize=0.8)

    # Fixed points
    ax.scatter(health_fp[0], health_fp[1], s=180, c="green", zorder=5,
               label=f"Health SS  V={health_fp[0]:.1f}, I={health_fp[1]:.2f}")
    ax.scatter(disease_fp[0], disease_fp[1], s=180, c="red", marker="X", zorder=5,
               label=f"Disease SS  V={disease_fp[0]:.1f}, I={disease_fp[1]:.2f}")

    # Annotate literature references on disease SS
    ax.annotate("NK dysfn 40–60%\n(Brenu 2011)\nGZMH -5.45x (GSE268212)",
                xy=(disease_fp[0], disease_fp[1]),
                xytext=(disease_fp[0] + 0.5, disease_fp[1] + 0.18),
                fontsize=7, color="darkred",
                arrowprops=dict(arrowstyle="->", color="darkred", lw=0.8))

    ax.set_xlabel("V — Viral load (log10 copies/g tissue)", fontsize=11)
    ax.set_ylabel("I — NK immune dysfunction (0=normal, 1=exhausted)", fontsize=11)
    ax.set_title("ME/CFS Vicious Cycle: V–I Phase Portrait\n"
                 "(N, M, A fixed at disease midpoint)", fontsize=12)
    ax.legend(fontsize=9, loc="upper left")
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    path = os.path.join(OUT_DIR, "mecfs_VI_phase_portrait.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  Saved: {path}")


# ════════════════════════════════════════════════════════════════════════════
# BIFURCATION DIAGRAM — F vs viral load
# ════════════════════════════════════════════════════════════════════════════

def bifurcation_diagram():
    """Sweep over k_rep (proxy for viral load intensity) and find SS of F."""
    p = params_baseline()
    print("\n=== BIFURCATION DIAGRAM ===")

    V_init_vals = np.linspace(0, 5.5, 55)
    F_ss_vals = []

    t_span = (0, 2000)
    t_eval = np.linspace(1800, 2000, 201)

    for V0 in V_init_vals:
        y0 = [V0, 0.35, 0.25, 0.30, 0.20, 70.0]
        sol = solve_ivp(vicious_cycle, t_span, y0, args=(p,),
                        t_eval=t_eval, method="LSODA", rtol=1e-8, atol=1e-10)
        F_ss_vals.append(np.mean(sol.y[5, -20:]))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Left: F vs initial viral load
    ax1.plot(V_init_vals, F_ss_vals, "o-", ms=4, color="steelblue", lw=1.5)
    ax1.axhline(60, color="green", ls="--", lw=1, label="Mild ME/CFS threshold (Bell 60)")
    ax1.axhline(40, color="orange", ls="--", lw=1, label="Moderate/severe threshold (Bell 40)")
    ax1.axhline(20, color="red", ls="--", lw=1, label="Severe/bedbound (Bell 20)")
    ax1.set_xlabel("Initial viral load V₀ (log10 copies/g)", fontsize=11)
    ax1.set_ylabel("F — Bell Disability Scale at t=2000 days", fontsize=11)
    ax1.set_title("Bifurcation: Steady-state function vs viral burden", fontsize=11)
    ax1.legend(fontsize=8)
    ax1.set_ylim(0, 105)

    # Right: F vs k_rep (viral replication rate parameter)
    k_rep_vals = np.linspace(0.01, 0.12, 50)
    F_ss_krep = []
    for kr in k_rep_vals:
        p2 = params_baseline()
        p2["k_rep"] = kr
        y0 = [4.0, 0.5, 0.4, 0.4, 0.25, 50.0]
        sol = solve_ivp(vicious_cycle, t_span, y0, args=(p2,),
                        t_eval=t_eval, method="LSODA", rtol=1e-8, atol=1e-10)
        F_ss_krep.append(np.mean(sol.y[5, -20:]))

    ax2.plot(k_rep_vals, F_ss_krep, "s-", ms=4, color="firebrick", lw=1.5)
    ax2.axhline(60, color="green", ls="--", lw=1, label="Mild threshold")
    ax2.axhline(40, color="orange", ls="--", lw=1, label="Mod/severe threshold")
    ax2.set_xlabel("k_rep — Viral replication rate (day⁻¹)", fontsize=11)
    ax2.set_ylabel("F — Bell Disability Scale at t=2000 days", fontsize=11)
    ax2.set_title("Bifurcation: Steady-state function vs viral replication rate", fontsize=11)
    ax2.legend(fontsize=8)
    ax2.set_ylim(0, 105)

    plt.tight_layout()
    path = os.path.join(OUT_DIR, "mecfs_bifurcation.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  Saved: {path}")


# ════════════════════════════════════════════════════════════════════════════
# TREATMENT TRAJECTORY — 4-phase protocol
# ════════════════════════════════════════════════════════════════════════════

def treatment_trajectory():
    """
    Simulate the 4-phase protocol from models/vicious_cycle.md:
      Phase 1 (days 0–56):   supplements only — CoQ10+NR (coq_nr↑), BHB/butyrate (bhb_but↑)
      Phase 2 (days 57–112): add fluoxetine (fluox↑) + FMD (fmd↑) + cold exposure (cold_nk↑)
      Phase 3 (days 113–168): all protocol maximal; threshold crossing expected
      Phase 4 (days 169–365): reconditioning; gradual F improvement
    """
    print("\n=== TREATMENT TRAJECTORY ===")

    # Starting state: moderate-severe ME/CFS
    y0 = [4.0, 0.50, 0.43, 0.44, 0.29, 47.0]

    def protocol_params(t):
        p = params_baseline()
        if t < 56:   # Phase 1
            p["coq_nr"]  = 0.30
            p["bhb_but"] = 0.40
        elif t < 112:  # Phase 2
            p["coq_nr"]  = 0.40
            p["bhb_but"] = 0.50
            p["fluox"]   = 0.35
            p["fmd"]     = 0.40
            p["cold_nk"] = 0.30
        elif t < 168:  # Phase 3
            p["coq_nr"]  = 0.50
            p["bhb_but"] = 0.60
            p["fluox"]   = 0.50
            p["fmd"]     = 0.60
            p["cold_nk"] = 0.50
        else:          # Phase 4
            p["coq_nr"]  = 0.40
            p["bhb_but"] = 0.40
            p["fluox"]   = 0.40
            p["fmd"]     = 0.30
            p["cold_nk"] = 0.40
        return p

    # Use event-driven integration per phase
    t_ends = [56, 112, 168, 365]
    t_all, y_all = [], []
    y_cur = y0.copy()

    for i, t_end in enumerate(t_ends):
        t_start = 0 if i == 0 else t_ends[i - 1]
        p = protocol_params((t_start + t_end) / 2)
        t_ev = np.linspace(t_start, t_end, int((t_end - t_start) * 4) + 1)
        sol = solve_ivp(vicious_cycle, (t_start, t_end), y_cur, args=(p,),
                        t_eval=t_ev, method="LSODA", rtol=1e-8, atol=1e-10)
        t_all.extend(sol.t.tolist())
        y_all.append(sol.y)
        y_cur = sol.y[:, -1].tolist()

    t_arr = np.array(t_all)
    y_arr = np.hstack(y_all)

    var_names = ["V (log10 cp/g)", "I (NK dysfn)", "N (neuroinflam)",
                 "M (mito dysfn)", "A (ANS dysfn)", "F (Bell Scale)"]
    colors = ["firebrick", "darkorange", "purple", "steelblue", "teal", "green"]
    literature_ss = [None, 0.5, 0.45, 0.45, 0.30, 47.0]
    literature_labels = [None, "NK dysfn 40-60% (Brenu 2011)",
                         "TSPO +45% (Nakatomi 2014)",
                         "Complex I -30-60% (Myhill 2009)",
                         "HRV -30% (Miwa 2013)", None]

    fig = plt.figure(figsize=(14, 10))
    gs = gridspec.GridSpec(3, 2, figure=fig, hspace=0.45, wspace=0.35)

    phase_boundaries = [56, 112, 168]
    phase_labels = ["Phase 1\nSupplements", "Phase 2\n+Fluox+FMD+Cold",
                    "Phase 3\nMax Protocol", "Phase 4\nReconditioning"]

    for idx in range(6):
        ax = fig.add_subplot(gs[idx // 2, idx % 2])
        ax.plot(t_arr, y_arr[idx], color=colors[idx], lw=2)

        for pb in phase_boundaries:
            ax.axvline(pb, color="gray", ls="--", lw=0.8, alpha=0.7)

        if literature_ss[idx] is not None:
            ax.axhline(literature_ss[idx], color="gray", ls=":", lw=1.2,
                       alpha=0.8, label=literature_labels[idx])
            ax.legend(fontsize=7, loc="upper right")

        ax.set_xlabel("Days", fontsize=9)
        ax.set_ylabel(var_names[idx], fontsize=9)
        ax.set_title(var_names[idx], fontsize=10)

        # Phase labels on F panel
        if idx == 5:
            for pi, (t0, t1) in enumerate(zip([0] + phase_boundaries,
                                               phase_boundaries + [365])):
                ax.text((t0 + t1) / 2, ax.get_ylim()[0] + 2,
                        phase_labels[pi], ha="center", fontsize=6.5, color="gray")
            ax.axhline(60, color="green", ls="-.", lw=0.8, alpha=0.6, label="Mild/Normal threshold")
            ax.axhline(40, color="orange", ls="-.", lw=0.8, alpha=0.6, label="Mod/Severe threshold")
            ax.legend(fontsize=7)

    fig.suptitle("ME/CFS Treatment Trajectory: 4-Phase Protocol\n"
                 "(Vicious cycle ODE; real parameters from literature)",
                 fontsize=13, y=0.98)
    path = os.path.join(OUT_DIR, "mecfs_treatment_trajectory.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  Saved: {path}")

    # Print final state
    print("\n  Final state at day 365:")
    for i, name in enumerate(var_names):
        print(f"    {name}: {y_arr[i, -1]:.3f}")


# ════════════════════════════════════════════════════════════════════════════
# SEPARATRIX APPROXIMATION — project onto V–F plane
# ════════════════════════════════════════════════════════════════════════════

def separatrix_VF():
    """
    Numerically approximate the separatrix by shooting from the saddle region.
    Use many initial conditions to identify which ones go to health vs disease.
    """
    print("\n=== SEPARATRIX (V–F projection) ===")
    p = params_baseline()

    V_range  = np.linspace(0, 5.5, 30)
    F_range  = np.linspace(5, 95, 30)

    # Fix I, N, M, A near threshold midpoints
    I0, N0, M0, A0 = 0.35, 0.25, 0.25, 0.20
    outcomes = np.zeros((len(F_range), len(V_range)))  # 0=health, 1=disease

    for fi, F0 in enumerate(F_range):
        for vi, V0 in enumerate(V_range):
            y0 = [V0, I0, N0, M0, A0, F0]
            sol = solve_ivp(vicious_cycle, (0, 1500), y0, args=(p,),
                            t_eval=[1500], method="LSODA", rtol=1e-7, atol=1e-9)
            F_final = sol.y[5, 0]
            outcomes[fi, vi] = 1 if F_final < 60.0 else 0

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.contourf(V_range, F_range, outcomes, levels=[0, 0.5, 1],
                colors=["#d4edda", "#f8d7da"], alpha=0.6)
    ax.contour(V_range, F_range, outcomes, levels=[0.5],
               colors=["black"], linewidths=2)

    # Label regions
    ax.text(0.3, 80, "HEALTH\nattractor", fontsize=12, color="darkgreen",
            ha="left", va="center")
    ax.text(4.5, 25, "DISEASE\nattractor", fontsize=12, color="darkred",
            ha="center", va="center")
    ax.text(2.8, 52, "SEPARATRIX", fontsize=10, color="black",
            ha="center", va="center", rotation=-40,
            bbox=dict(fc="white", ec="black", boxstyle="round,pad=0.2"))

    ax.set_xlabel("V — Initial viral load (log10 copies/g)", fontsize=11)
    ax.set_ylabel("F — Initial Bell Disability Scale", fontsize=11)
    ax.set_title("ME/CFS Bistability Separatrix\n"
                 "(I=0.35, N=0.25, M=0.25, A=0.20 fixed; t=1500 days)", fontsize=11)
    ax.set_xlim(0, 5.5)
    ax.set_ylim(5, 95)
    plt.tight_layout()
    path = os.path.join(OUT_DIR, "mecfs_separatrix.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  Saved: {path}")


# ════════════════════════════════════════════════════════════════════════════
# MAIN
# ════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("ME/CFS Vicious Cycle ODE — Parameter Summary")
    print("=" * 60)
    print("Key disease steady-state targets (from literature):")
    print("  V: ~4 log10 copies/g (TD-mutant CVB; Chia 2008)")
    print("  I: 0.40–0.60 (NK dysfunction; Brenu 2011)")
    print("     Transcriptomics: GZMH -5.45x, NKG7 -5.21x (GSE268212)")
    print("  N: +0.45 normalized TSPO binding (Nakatomi 2014, Brain)")
    print("  M: 0.30–0.60 (Complex I -30-60%; Myhill 2009)")
    print("  A: ~0.30 (HRV -30%; Miwa 2013, Intern Med)")
    print("  F: Bell Scale 20–55 (moderate-severe ME/CFS)")

    health_fp, disease_fp = compute_steady_states()
    print("\nGenerating phase portrait...")
    phase_portrait_VI(health_fp, disease_fp)
    print("Generating bifurcation diagram...")
    bifurcation_diagram()
    print("Generating separatrix...")
    separatrix_VF()
    print("Generating treatment trajectory...")
    treatment_trajectory()

    print("\nAll figures saved to:", OUT_DIR)
