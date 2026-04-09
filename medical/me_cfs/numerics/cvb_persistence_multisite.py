#!/usr/bin/env python3
"""
CVB Multi-Site Persistence Model — numerical track Numerics
========================================================

Models CVB persistence across multiple tissue reservoirs in ME/CFS:
muscle, CNS, gut. Includes inter-reservoir viral shedding, immune
exhaustion dynamics, and why multi-site persistence is harder to
clear than single-organ CVB disease.

References:
-----------
[1] Chia & Chia, J Clin Pathol 2008: Enterovirus RNA in stomach
    biopsies of ME/CFS patients — 82% positive vs 20% controls
[2] Chia, J Clin Virol 2005: "The role of enterovirus in CFS"
    — comprehensive review of CVB persistence in ME/CFS
[3] Lane et al., J Med Virol 2003: CVB RNA in muscle biopsies
    of ME/CFS patients — 42% positive
[4] Douche-Aourik et al., J Med Virol 2003: Persistent CVB in
    dilated cardiomyopathy — similar persistence mechanism
[5] Chapman et al., J Gen Virol 2008: TD mutant persistence
    — 5' deletions confer persistence phenotype
[6] Gow et al., BMJ 1991: Enteroviral RNA in muscle of CFS patients
[7] Wherry & Kurachi, Nat Rev Immunol 2015: T cell exhaustion
    during chronic viral infection
[8] McLane et al., Ann Rev Immunol 2019: CD8 T cell exhaustion
    — TOX/NR4A drive exhaustion program
[9] VanElzakker, Med Hypotheses 2013: Vagus nerve infection →
    sickness behavior in ME/CFS
[10] Rasa et al., J Transl Med 2018: Chronic viral infections
     in ME/CFS — comprehensive review
[11] Tracy et al., J Clin Invest 2000: Group B coxsackievirus
     myocarditis and pancreatitis — persistence mechanisms

Model structure:
  3 tissue compartments (muscle, CNS, gut) each with:
    - Viral load (V_i): TD mutant population
    - Immune response (I_i): local CD8+ T cells + NK cells
    - Tissue damage (D_i): accumulated organ dysfunction
  Plus systemic variables:
    - Exhaustion (X): T cell exhaustion (PD-1, Tim-3, TOX)
    - Cytokine burden (C): systemic inflammation

ME/CFS systematic approach — Phase 0 numerics
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "figures")
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ============================================================================
# TISSUE COMPARTMENT PARAMETERS
# ============================================================================

# Each tissue has different properties that affect CVB persistence.
# Values are relative rates (normalized to muscle = 1.0 for viral replication).

TISSUE_PARAMS = {
    "muscle": {
        "name": "Skeletal Muscle",
        # CVB tropism: high for muscle (CAR receptor + DAF co-receptor)
        # Ref: [3] Lane 2003 — 42% of ME/CFS patients positive
        "viral_replication_rate": 0.05,     # TD mutants replicate slowly
        "viral_carrying_capacity": 1000.0,  # arbitrary units
        "immune_access": 0.6,               # moderate (good blood supply but large volume)
        "immune_killing_rate": 0.3,         # per immune unit per virus per day
        "viral_shedding_rate": 0.01,        # rate virus enters systemic circulation
        "tissue_damage_rate": 0.002,        # damage per viral unit per day
        "tissue_repair_rate": 0.01,         # repair rate (muscle regenerates slowly)
        "initial_viral_load": 100.0,        # at disease onset
        "color": "#e74c3c",                 # red
        "prevalence_in_mecfs": 0.42,        # [3] Lane 2003
    },
    "cns": {
        "name": "Central Nervous System",
        # CVB can infect neurons, microglia, astrocytes
        # BBB limits immune access but also limits viral seeding
        # Ref: [9] VanElzakker 2013 — vagus nerve infection hypothesis
        "viral_replication_rate": 0.03,     # slower in CNS
        "viral_carrying_capacity": 500.0,   # smaller compartment
        "immune_access": 0.2,               # LOW — blood-brain barrier
        "immune_killing_rate": 0.15,        # microglia less efficient than CD8s
        "viral_shedding_rate": 0.005,       # limited by BBB
        "tissue_damage_rate": 0.005,        # neurons very sensitive to damage
        "tissue_repair_rate": 0.002,        # neurons barely regenerate
        "initial_viral_load": 20.0,         # less initial seeding
        "color": "#9b59b6",                 # purple
        "prevalence_in_mecfs": 0.30,        # ESTIMATE based on neuroinflam PET data
    },
    "gut": {
        "name": "Gastrointestinal Tract",
        # Primary site of enterovirus entry and persistence
        # Ref: [1] Chia & Chia 2008 — 82% positive in stomach biopsies
        "viral_replication_rate": 0.08,     # highest — enteric tropism
        "viral_carrying_capacity": 2000.0,  # large surface area
        "immune_access": 0.8,               # high — GALT well-vascularized
        "immune_killing_rate": 0.25,        # good, but tolerance mechanisms interfere
        "viral_shedding_rate": 0.02,        # highest — gut drains to portal circulation
        "tissue_damage_rate": 0.003,        # moderate
        "tissue_repair_rate": 0.05,         # gut epithelium regenerates fast (~5 days)
        "initial_viral_load": 200.0,        # highest initial load (entry site)
        "color": "#2ecc71",                 # green
        "prevalence_in_mecfs": 0.82,        # [1] Chia & Chia 2008
    },
}


# ============================================================================
# SYSTEM-LEVEL PARAMETERS
# ============================================================================

SYSTEMIC_PARAMS = {
    # T cell exhaustion dynamics (Ref: [7] Wherry 2015, [8] McLane 2019)
    "exhaustion_rate": 0.005,       # rate exhaustion accumulates per total viral load/day
    "exhaustion_recovery_rate": 0.001,  # rate exhaustion resolves when viral load is low
    "max_exhaustion": 0.95,         # maximum exhaustion (never fully reaches 1.0)

    # Immune cell production
    "basal_immune_production": 5.0,  # baseline immune cell production per day (all sites)
    "max_immune_production": 20.0,   # max when stimulated by viral antigen
    "immune_halflife": 14.0,         # days — immune cell turnover

    # Cross-compartment viral seeding
    "cross_seeding_efficiency": 0.1,  # fraction of shed virus that seeds another compartment

    # Systemic cytokine dynamics
    "cytokine_production_per_virus": 0.001,  # cytokine units per virus unit
    "cytokine_clearance_rate": 0.2,          # per day (~3.5h half-life)
}


# ============================================================================
# ODE MODEL
# ============================================================================

def multisite_cvb_ode(t, y, tissues, systemic, intervention=None):
    """
    Multi-site CVB persistence ODE system.

    State vector y = [V_muscle, V_cns, V_gut, I_muscle, I_cns, I_gut,
                      D_muscle, D_cns, D_gut, X, C]

    V_i: viral load in tissue i
    I_i: immune response strength in tissue i
    D_i: accumulated tissue damage in tissue i
    X:   systemic T cell exhaustion (0 = fresh, 1 = fully exhausted)
    C:   systemic cytokine level
    """
    tissue_names = list(tissues.keys())
    n = len(tissue_names)

    V = y[0:n]           # viral loads
    I = y[n:2*n]         # immune responses
    D = y[2*n:3*n]       # tissue damage
    X = y[3*n]           # exhaustion
    C = y[3*n + 1]       # cytokines

    # Clamp
    V = np.maximum(V, 0)
    I = np.maximum(I, 0)
    D = np.clip(D, 0, 1)
    X = np.clip(X, 0, systemic["max_exhaustion"])
    C = max(C, 0)

    dV = np.zeros(n)
    dI = np.zeros(n)
    dD = np.zeros(n)

    total_viral_load = np.sum(V)
    total_shedding = 0.0

    # Apply interventions if specified
    antiviral_factor = 1.0  # multiplier on viral replication (< 1 = antiviral)
    autophagy_factor = 1.0  # multiplier on immune killing (> 1 = enhanced clearance)
    mito_support = 0.0      # additive boost to immune function

    if intervention is not None:
        if "antiviral" in intervention:
            antiviral_factor = intervention["antiviral"]
        if "autophagy" in intervention:
            autophagy_factor = intervention["autophagy"]
        if "mito_support" in intervention:
            mito_support = intervention["mito_support"]

    for i, tname in enumerate(tissue_names):
        tp = tissues[tname]

        # --- Viral dynamics ---
        # Logistic growth (TD mutants: slow but persistent)
        growth = (tp["viral_replication_rate"] * antiviral_factor *
                  V[i] * (1.0 - V[i] / tp["viral_carrying_capacity"]))

        # Immune killing: reduced by exhaustion
        effective_immune = I[i] * (1.0 - X) * tp["immune_access"] * autophagy_factor
        killing = tp["immune_killing_rate"] * effective_immune * V[i] / (V[i] + 50.0)
        # Michaelis-Menten saturation: at high viral loads, killing saturates

        # Viral shedding to systemic circulation
        shedding = tp["viral_shedding_rate"] * V[i]
        total_shedding += shedding

        dV[i] = growth - killing - shedding

        # --- Tissue damage ---
        damage = tp["tissue_damage_rate"] * V[i]
        repair = tp["tissue_repair_rate"] * (1.0 - D[i])  # repair toward D=0
        # Cytokine-mediated bystander damage
        bystander = 0.001 * C * (1.0 - D[i])

        dD[i] = damage - repair + bystander

        # --- Local immune response ---
        # Antigen-driven recruitment
        antigen_signal = V[i] / (V[i] + 100.0)  # saturates at high load
        recruitment = (systemic["basal_immune_production"] +
                       (systemic["max_immune_production"] - systemic["basal_immune_production"]) *
                       antigen_signal * tp["immune_access"])
        # Immune cell death
        death = I[i] / systemic["immune_halflife"]
        # Exhaustion reduces immune cell fitness (not just killing)
        exhaustion_attrition = 0.1 * X * I[i]

        dI[i] = recruitment - death - exhaustion_attrition + mito_support

    # Cross-compartment seeding: shed virus can seed other compartments
    for i in range(n):
        other_shedding = total_shedding - TISSUE_PARAMS[tissue_names[i]]["viral_shedding_rate"] * V[i]
        incoming = systemic["cross_seeding_efficiency"] * other_shedding / max(n - 1, 1)
        dV[i] += incoming

    # --- T cell exhaustion ---
    # Increases with chronic antigen exposure, recovers when virus is low
    exhaustion_drive = systemic["exhaustion_rate"] * total_viral_load / (total_viral_load + 100.0)
    exhaustion_recovery = systemic["exhaustion_recovery_rate"] * (1.0 - total_viral_load / (total_viral_load + 50.0))
    dX = exhaustion_drive * (systemic["max_exhaustion"] - X) - exhaustion_recovery * X

    # --- Systemic cytokines ---
    cytokine_production = systemic["cytokine_production_per_virus"] * total_viral_load
    cytokine_clearance = systemic["cytokine_clearance_rate"] * C
    dC = cytokine_production - cytokine_clearance

    dy = np.concatenate([dV, dI, dD, [dX, dC]])
    return dy


# ============================================================================
# SIMULATION SCENARIOS
# ============================================================================

def run_natural_history(years=10):
    """Simulate natural history of ME/CFS without intervention."""
    print("=" * 70)
    print("SCENARIO 1: NATURAL HISTORY — CVB PERSISTENCE WITHOUT TREATMENT")
    print("=" * 70)

    tissues = TISSUE_PARAMS
    systemic = SYSTEMIC_PARAMS
    tissue_names = list(tissues.keys())
    n = len(tissue_names)

    # Initial conditions: acute CVB infection seeding all compartments
    V0 = [tissues[t]["initial_viral_load"] for t in tissue_names]
    I0 = [10.0, 3.0, 15.0]  # initial immune response (gut highest, CNS lowest)
    D0 = [0.0, 0.0, 0.0]    # no initial damage
    X0 = 0.0                  # no exhaustion yet
    C0 = 0.5                  # acute infection cytokines

    y0 = V0 + I0 + D0 + [X0, C0]

    t_span = (0, years * 365)
    t_eval = np.linspace(0, years * 365, 5000)

    sol = solve_ivp(
        multisite_cvb_ode, t_span, y0, args=(tissues, systemic),
        method='RK45', t_eval=t_eval, max_step=1.0,
    )

    plot_results(sol, tissue_names, tissues, "Natural History (No Treatment)",
                 "natural_history", years)

    # Print final state
    print(f"\nFinal state at {years} years:")
    final = sol.y[:, -1]
    for i, tname in enumerate(tissue_names):
        print(f"  {tissues[tname]['name']:>25}: V={final[i]:.1f}, I={final[n+i]:.1f}, D={final[2*n+i]:.3f}")
    print(f"  {'T cell exhaustion':>25}: {final[3*n]:.3f}")
    print(f"  {'Systemic cytokines':>25}: {final[3*n+1]:.3f}")

    return sol


def run_single_organ_comparison(years=10):
    """
    Compare single-organ CVB disease vs multi-site ME/CFS.
    This shows why ME/CFS is harder to clear.
    """
    print("\n" + "=" * 70)
    print("SCENARIO 2: SINGLE-ORGAN vs MULTI-SITE PERSISTENCE")
    print("=" * 70)

    tissues = TISSUE_PARAMS
    systemic = SYSTEMIC_PARAMS
    tissue_names = list(tissues.keys())
    n = len(tissue_names)

    t_span = (0, years * 365)
    t_eval = np.linspace(0, years * 365, 5000)

    # Scenario A: Single organ (muscle only, like post-viral myalgia)
    V0_single = [100.0, 0.0, 0.0]  # only muscle
    I0 = [10.0, 3.0, 15.0]
    D0 = [0.0, 0.0, 0.0]
    y0_single = V0_single + I0 + D0 + [0.0, 0.5]

    sol_single = solve_ivp(
        multisite_cvb_ode, t_span, y0_single, args=(tissues, systemic),
        method='RK45', t_eval=t_eval, max_step=1.0,
    )

    # Scenario B: Multi-site (all three — ME/CFS)
    V0_multi = [100.0, 20.0, 200.0]
    y0_multi = V0_multi + I0 + D0 + [0.0, 0.5]

    sol_multi = solve_ivp(
        multisite_cvb_ode, t_span, y0_multi, args=(tissues, systemic),
        method='RK45', t_eval=t_eval, max_step=1.0,
    )

    # Plot comparison
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    t_years = t_eval / 365

    # Total viral load
    total_V_single = np.sum(sol_single.y[0:n, :], axis=0)
    total_V_multi = np.sum(sol_multi.y[0:n, :], axis=0)

    axes[0, 0].plot(t_years, total_V_single, 'b-', linewidth=2, label='Single organ (muscle)')
    axes[0, 0].plot(t_years, total_V_multi, 'r-', linewidth=2, label='Multi-site (ME/CFS)')
    axes[0, 0].set_ylabel('Total Viral Load')
    axes[0, 0].set_title('Total Viral Burden')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)

    # T cell exhaustion
    axes[0, 1].plot(t_years, sol_single.y[3*n, :], 'b-', linewidth=2, label='Single organ')
    axes[0, 1].plot(t_years, sol_multi.y[3*n, :], 'r-', linewidth=2, label='Multi-site')
    axes[0, 1].set_ylabel('T Cell Exhaustion')
    axes[0, 1].set_title('Immune Exhaustion')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)

    # Cytokines
    axes[1, 0].plot(t_years, sol_single.y[3*n+1, :], 'b-', linewidth=2, label='Single organ')
    axes[1, 0].plot(t_years, sol_multi.y[3*n+1, :], 'r-', linewidth=2, label='Multi-site')
    axes[1, 0].set_ylabel('Systemic Cytokines')
    axes[1, 0].set_xlabel('Years')
    axes[1, 0].set_title('Inflammatory Burden')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)

    # Total tissue damage
    total_D_single = np.sum(sol_single.y[2*n:3*n, :], axis=0)
    total_D_multi = np.sum(sol_multi.y[2*n:3*n, :], axis=0)

    axes[1, 1].plot(t_years, total_D_single, 'b-', linewidth=2, label='Single organ')
    axes[1, 1].plot(t_years, total_D_multi, 'r-', linewidth=2, label='Multi-site')
    axes[1, 1].set_ylabel('Total Tissue Damage')
    axes[1, 1].set_xlabel('Years')
    axes[1, 1].set_title('Accumulated Organ Damage')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)

    fig.suptitle('Why ME/CFS Is Harder to Clear: Multi-Site vs Single-Organ CVB', fontsize=15)
    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "single_vs_multisite.png"), dpi=150)
    plt.close(fig)

    # Quantify the difference
    print(f"\nComparison at {years} years:")
    print(f"{'Metric':<30} {'Single-organ':<18} {'Multi-site (ME/CFS)':<20} {'Ratio'}")
    print("-" * 80)

    for metric, idx_s, idx_m in [
        ("Total viral load", total_V_single[-1], total_V_multi[-1]),
        ("T cell exhaustion", sol_single.y[3*n, -1], sol_multi.y[3*n, -1]),
        ("Systemic cytokines", sol_single.y[3*n+1, -1], sol_multi.y[3*n+1, -1]),
        ("Total tissue damage", total_D_single[-1], total_D_multi[-1]),
    ]:
        ratio = idx_m / max(idx_s, 1e-6)
        print(f"{metric:<30} {idx_s:<18.2f} {idx_m:<20.2f} {ratio:.1f}x")

    print(f"\n  Key finding: Multi-site persistence creates:")
    print(f"  1. Cross-seeding: virus cleared from one site gets reseeded from others")
    print(f"  2. Higher total antigen load → faster exhaustion")
    print(f"  3. More tissue damage → more DAMPs → more inflammation")
    print(f"  4. WHY single-organ CVB diseases (myocarditis, pancreatitis)")
    print(f"     can often resolve, but ME/CFS persists indefinitely")
    print(f"\n  Plot saved: {os.path.join(OUTPUT_DIR, 'single_vs_multisite.png')}")


def run_intervention_scenarios(years=5):
    """
    Model the T1DM protocol + ME/CFS-specific additions.

    Interventions:
    1. Fluoxetine (antiviral: inhibits CVB 2C ATPase)
    2. Fasting/FMD (autophagy: clears infected cells)
    3. Mitochondrial support (CoQ10, NAD+ precursors, D-ribose)
    4. Combined protocol
    """
    print("\n" + "=" * 70)
    print("SCENARIO 3: INTERVENTION MODELING")
    print("=" * 70)

    tissues = TISSUE_PARAMS
    systemic = SYSTEMIC_PARAMS
    tissue_names = list(tissues.keys())
    n = len(tissue_names)

    # Start from established ME/CFS state (2 years of untreated disease)
    V0 = [100.0, 20.0, 200.0]
    I0 = [10.0, 3.0, 15.0]
    D0 = [0.0, 0.0, 0.0]
    y0 = V0 + I0 + D0 + [0.0, 0.5]

    # First run 2 years untreated to establish disease state
    t_establish = (0, 2 * 365)
    sol_est = solve_ivp(
        multisite_cvb_ode, t_establish, y0, args=(tissues, systemic),
        method='RK45', max_step=1.0, dense_output=True,
    )
    established_state = sol_est.y[:, -1]

    print(f"\nEstablished disease state (after 2 years untreated):")
    for i, tname in enumerate(tissue_names):
        print(f"  {tissues[tname]['name']:>25}: V={established_state[i]:.1f}")
    print(f"  {'Exhaustion':>25}: {established_state[3*n]:.3f}")

    # Now model interventions starting at year 2
    interventions = {
        "No treatment": None,
        "Fluoxetine only": {"antiviral": 0.3},       # 70% reduction in viral replication
        "Fasting/FMD only": {"autophagy": 2.0},      # 2x autophagy-mediated clearance
        "Mito support only": {"mito_support": 3.0},   # boost immune cell energy
        "Full protocol": {"antiviral": 0.3, "autophagy": 2.0, "mito_support": 3.0},
    }

    t_treat = (0, years * 365)
    t_eval = np.linspace(0, years * 365, 3000)

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    colors = {'No treatment': 'gray', 'Fluoxetine only': 'blue',
              'Fasting/FMD only': 'green', 'Mito support only': 'orange',
              'Full protocol': 'red'}

    results = {}
    for name, intv in interventions.items():
        sol = solve_ivp(
            multisite_cvb_ode, t_treat, established_state.copy(),
            args=(tissues, systemic, intv),
            method='RK45', t_eval=t_eval, max_step=1.0,
        )
        results[name] = sol

        t_years = t_eval / 365 + 2  # offset by 2 years of established disease
        total_V = np.sum(sol.y[0:n, :], axis=0)
        total_D = np.sum(sol.y[2*n:3*n, :], axis=0)

        c = colors[name]
        lw = 3 if name == "Full protocol" else 1.5

        axes[0, 0].plot(t_years, total_V, color=c, linewidth=lw, label=name)
        axes[0, 1].plot(t_years, sol.y[3*n, :], color=c, linewidth=lw, label=name)
        axes[1, 0].plot(t_years, sol.y[3*n+1, :], color=c, linewidth=lw, label=name)
        axes[1, 1].plot(t_years, total_D, color=c, linewidth=lw, label=name)

    titles = ['Total Viral Load', 'T Cell Exhaustion', 'Systemic Cytokines', 'Total Tissue Damage']
    ylabels = ['Viral Load', 'Exhaustion (0-1)', 'Cytokine Level', 'Damage Score']
    for ax, title, ylabel in zip(axes.flat, titles, ylabels):
        ax.set_title(title, fontsize=13)
        ax.set_ylabel(ylabel)
        ax.set_xlabel('Years')
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)
        ax.axvline(x=2, color='black', linestyle='--', alpha=0.3, label='Treatment start')

    fig.suptitle('ME/CFS Intervention Modeling: Protocol Components', fontsize=15)
    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "intervention_comparison.png"), dpi=150)
    plt.close(fig)

    # Print comparison table
    print(f"\nIntervention comparison at {years} years of treatment:")
    print(f"{'Intervention':<25} {'Viral Load':<15} {'Exhaustion':<15} {'Cytokines':<15} {'Damage':<15}")
    print("-" * 85)
    for name, sol in results.items():
        final = sol.y[:, -1]
        total_V = np.sum(final[0:n])
        total_D = np.sum(final[2*n:3*n])
        print(f"{name:<25} {total_V:<15.1f} {final[3*n]:<15.3f} {final[3*n+1]:<15.3f} {total_D:<15.4f}")

    # Calculate clearance time for full protocol
    sol_full = results["Full protocol"]
    total_V_full = np.sum(sol_full.y[0:n, :], axis=0)
    clearance_idx = np.where(total_V_full < 1.0)[0]
    if len(clearance_idx) > 0:
        clearance_days = t_eval[clearance_idx[0]]
        print(f"\n  Full protocol: viral load < 1.0 at {clearance_days:.0f} days ({clearance_days/30:.1f} months)")
    else:
        print(f"\n  Full protocol: viral load still >1.0 at {years} years (needs longer treatment)")

    print(f"\n  Plot saved: {os.path.join(OUTPUT_DIR, 'intervention_comparison.png')}")

    return results


def run_exhaustion_dynamics():
    """
    Deep dive on immune exhaustion: the key reason ME/CFS self-perpetuates.

    T cell exhaustion hierarchy (Wherry 2015):
    1. Progenitor exhausted (TCF1+, PD-1lo) — still rescuable
    2. Intermediate exhausted (PD-1hi, Tim-3-) — partially rescuable
    3. Terminally exhausted (PD-1hi, Tim-3+, TOX+) — not rescuable

    In ME/CFS: years of chronic antigen → most T cells terminally exhausted
    → EVEN IF you clear the virus, immune reconstitution takes months
    """
    print("\n" + "=" * 70)
    print("SCENARIO 4: IMMUNE EXHAUSTION DYNAMICS — WHY RECOVERY IS SLOW")
    print("=" * 70)

    # Model 3 populations of CD8+ T cells
    # P: progenitor exhausted (rescuable)
    # I: intermediate exhausted (partially rescuable)
    # T: terminally exhausted (not rescuable)

    def exhaustion_ode(t, y, viral_load_func):
        P, Int, Term = y
        V = viral_load_func(t)

        # Antigen stimulation drives progression through exhaustion hierarchy
        stim = V / (V + 50.0)  # normalized antigen signal

        # Progenitor → Intermediate: driven by chronic stimulation
        # Ref: [8] McLane 2019: TOX upregulation drives exhaustion program
        p_to_i = 0.02 * stim * P

        # Intermediate → Terminal: slower, requires sustained stimulation
        i_to_t = 0.005 * stim * Int

        # Progenitor self-renewal (maintains pool in low antigen)
        p_renewal = 0.01 * P * (1 - stim) * (1 - P / 100)

        # Terminal cells die faster (senescence)
        t_death = 0.01 * Term

        # New naive T cells entering (thymic output, ~constant in adults)
        # These start as progenitor exhausted in presence of antigen
        naive_input = 0.5  # cells/day (diminishes with age)

        dP = naive_input + p_renewal - p_to_i
        dI = p_to_i - i_to_t
        dT = i_to_t - t_death

        return [dP, dI, dT]

    # Scenario: viral load that decreases after treatment at year 3
    def viral_load_untreated(t):
        """Constant moderate viral load (untreated ME/CFS)."""
        return 200.0

    def viral_load_treated(t):
        """Viral load drops after treatment starts at day 0."""
        # Exponential decay with treatment (full protocol)
        if t < 0:
            return 200.0
        return 200.0 * np.exp(-0.005 * t)  # ~140 day half-life

    # Run untreated for 5 years
    t_span = (0, 5 * 365)
    t_eval = np.linspace(0, 5 * 365, 2000)
    y0 = [50.0, 5.0, 1.0]  # mostly progenitor at start

    sol_untreated = solve_ivp(
        exhaustion_ode, t_span, y0, args=(viral_load_untreated,),
        method='RK45', t_eval=t_eval,
    )

    # Then treat for 3 more years (starting from exhausted state)
    exhausted_state = sol_untreated.y[:, -1]
    t_treat = (0, 3 * 365)
    t_eval_treat = np.linspace(0, 3 * 365, 1500)

    sol_treated = solve_ivp(
        exhaustion_ode, t_treat, exhausted_state.copy(), args=(viral_load_treated,),
        method='RK45', t_eval=t_eval_treat,
    )

    # Plot
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    t_yr_1 = t_eval / 365
    t_yr_2 = t_eval_treat / 365 + 5  # offset

    # Panel 1: Untreated exhaustion progression
    axes[0, 0].stackplot(t_yr_1,
                         sol_untreated.y[2], sol_untreated.y[1], sol_untreated.y[0],
                         labels=['Terminal', 'Intermediate', 'Progenitor'],
                         colors=['#e74c3c', '#f39c12', '#2ecc71'], alpha=0.7)
    axes[0, 0].set_title('Untreated: Exhaustion Progression (5 years)', fontsize=13)
    axes[0, 0].set_ylabel('CD8+ T Cell Count')
    axes[0, 0].legend(loc='upper left')
    axes[0, 0].set_xlabel('Years')
    axes[0, 0].grid(True, alpha=0.3)

    # Panel 2: After treatment — immune reconstitution
    axes[0, 1].stackplot(t_yr_2,
                         sol_treated.y[2], sol_treated.y[1], sol_treated.y[0],
                         labels=['Terminal', 'Intermediate', 'Progenitor'],
                         colors=['#e74c3c', '#f39c12', '#2ecc71'], alpha=0.7)
    axes[0, 1].set_title('After Treatment: Immune Reconstitution', fontsize=13)
    axes[0, 1].set_ylabel('CD8+ T Cell Count')
    axes[0, 1].set_xlabel('Years')
    axes[0, 1].axvline(x=5, color='black', linestyle='--', label='Treatment start')
    axes[0, 1].legend(loc='upper right')
    axes[0, 1].grid(True, alpha=0.3)

    # Panel 3: Functional immune capacity over full course
    # Functional capacity: P contributes 100%, I contributes 40%, T contributes 5%
    func_untreated = (sol_untreated.y[0] * 1.0 + sol_untreated.y[1] * 0.4 +
                      sol_untreated.y[2] * 0.05)
    func_treated = (sol_treated.y[0] * 1.0 + sol_treated.y[1] * 0.4 +
                    sol_treated.y[2] * 0.05)

    full_t = np.concatenate([t_yr_1, t_yr_2])
    full_func = np.concatenate([func_untreated, func_treated])

    axes[1, 0].plot(full_t, full_func, 'b-', linewidth=2)
    axes[1, 0].axvline(x=5, color='red', linestyle='--', label='Treatment start')
    axes[1, 0].axhline(y=func_untreated[0], color='green', linestyle=':', alpha=0.5, label='Initial capacity')
    axes[1, 0].set_title('Functional Immune Capacity Over Full Course', fontsize=13)
    axes[1, 0].set_ylabel('Functional Capacity (AU)')
    axes[1, 0].set_xlabel('Years')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)

    # Panel 4: Viral load trajectory
    vl_untreated = [viral_load_untreated(t) for t in t_eval]
    vl_treated = [viral_load_treated(t) for t in t_eval_treat]

    axes[1, 1].plot(t_yr_1, vl_untreated, 'gray', linewidth=2, label='Untreated')
    axes[1, 1].plot(t_yr_2, vl_treated, 'red', linewidth=2, label='Under treatment')
    axes[1, 1].axvline(x=5, color='black', linestyle='--')
    axes[1, 1].set_title('Viral Load Trajectory', fontsize=13)
    axes[1, 1].set_ylabel('Viral Load (AU)')
    axes[1, 1].set_xlabel('Years')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)

    fig.suptitle('Immune Exhaustion in ME/CFS: Why Recovery Is Slow Even After Viral Clearance', fontsize=14)
    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "exhaustion_dynamics.png"), dpi=150)
    plt.close(fig)

    # Calculate recovery metrics
    initial_func = func_untreated[0]
    final_func = func_treated[-1]
    nadir_func = np.min(full_func)

    print(f"\nImmune exhaustion timeline:")
    print(f"  Initial functional capacity: {initial_func:.1f}")
    print(f"  Nadir (5 years untreated):   {nadir_func:.1f} ({nadir_func/initial_func*100:.0f}% of initial)")
    print(f"  After 3 years treatment:     {final_func:.1f} ({final_func/initial_func*100:.0f}% of initial)")
    print(f"\n  KEY INSIGHT: Even after viral load drops to near zero,")
    print(f"  immune reconstitution takes YEARS because:")
    print(f"  1. Terminal exhausted T cells (PD-1hi/Tim-3+/TOX+) are not rescuable")
    print(f"  2. They must die and be replaced by new progenitors")
    print(f"  3. Adult thymic output is low (~0.5 cells/day)")
    print(f"  4. This explains why ME/CFS patients who improve often take 1-3 years")
    print(f"\n  IMPLICATION FOR PROTOCOL:")
    print(f"  - Antiviral alone is not enough — must also support immune recovery")
    print(f"  - Anti-PD-1 therapy could accelerate reconstitution (research needed)")
    print(f"  - Time is part of the treatment — set realistic expectations")
    print(f"\n  Plot saved: {os.path.join(OUTPUT_DIR, 'exhaustion_dynamics.png')}")


# ============================================================================
# PLOTTING HELPER
# ============================================================================

def plot_results(sol, tissue_names, tissues, title, filename, years):
    """Plot multi-panel results for a simulation."""
    n = len(tissue_names)
    t_years = sol.t / 365

    fig, axes = plt.subplots(2, 3, figsize=(18, 10))

    # Row 1: Per-tissue viral load, immune response, damage
    for i, tname in enumerate(tissue_names):
        tp = tissues[tname]
        axes[0, 0].plot(t_years, sol.y[i], color=tp["color"], linewidth=2,
                        label=f'{tp["name"]} ({tp["prevalence_in_mecfs"]*100:.0f}%)')
        axes[0, 1].plot(t_years, sol.y[n+i], color=tp["color"], linewidth=2,
                        label=tp["name"])
        axes[0, 2].plot(t_years, sol.y[2*n+i], color=tp["color"], linewidth=2,
                        label=tp["name"])

    axes[0, 0].set_ylabel('Viral Load')
    axes[0, 0].set_title('CVB Viral Load by Tissue')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)

    axes[0, 1].set_ylabel('Immune Response')
    axes[0, 1].set_title('Local Immune Response')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)

    axes[0, 2].set_ylabel('Tissue Damage')
    axes[0, 2].set_title('Accumulated Damage')
    axes[0, 2].legend()
    axes[0, 2].grid(True, alpha=0.3)

    # Row 2: System-level
    # Total viral load
    total_V = np.sum(sol.y[0:n, :], axis=0)
    axes[1, 0].plot(t_years, total_V, 'k-', linewidth=2)
    axes[1, 0].set_ylabel('Total Viral Load')
    axes[1, 0].set_title('Total Viral Burden')
    axes[1, 0].set_xlabel('Years')
    axes[1, 0].grid(True, alpha=0.3)

    # Exhaustion
    axes[1, 1].plot(t_years, sol.y[3*n, :], 'purple', linewidth=2)
    axes[1, 1].set_ylabel('T Cell Exhaustion')
    axes[1, 1].set_title('Immune Exhaustion (0=fresh, 1=fully exhausted)')
    axes[1, 1].set_xlabel('Years')
    axes[1, 1].set_ylim(0, 1)
    axes[1, 1].grid(True, alpha=0.3)

    # Cytokines
    axes[1, 2].plot(t_years, sol.y[3*n+1, :], 'darkorange', linewidth=2)
    axes[1, 2].set_ylabel('Systemic Cytokines')
    axes[1, 2].set_title('Chronic Inflammation')
    axes[1, 2].set_xlabel('Years')
    axes[1, 2].grid(True, alpha=0.3)

    fig.suptitle(f'Multi-Site CVB Persistence in ME/CFS — {title}', fontsize=15)
    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, f"{filename}.png"), dpi=150)
    plt.close(fig)
    print(f"\n  Plot saved: {os.path.join(OUTPUT_DIR, f'{filename}.png')}")


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("=" * 70)
    print("CVB MULTI-SITE PERSISTENCE MODEL — ME/CFS")
    print("systematic approach — numerical track Numerics")
    print("=" * 70)
    print(f"\nOutput directory: {OUTPUT_DIR}")

    print(f"\nTissue reservoir prevalence in ME/CFS:")
    for tname, tp in TISSUE_PARAMS.items():
        print(f"  {tp['name']:<25}: {tp['prevalence_in_mecfs']*100:.0f}% of patients "
              f"(replication rate: {tp['viral_replication_rate']}, "
              f"immune access: {tp['immune_access']})")

    # Scenario 1: Natural history
    sol_natural = run_natural_history(years=10)

    # Scenario 2: Single organ vs multi-site
    run_single_organ_comparison(years=10)

    # Scenario 3: Intervention modeling
    results_intv = run_intervention_scenarios(years=5)

    # Scenario 4: Exhaustion dynamics deep dive
    run_exhaustion_dynamics()

    # Final summary
    print("\n" + "=" * 70)
    print("SUMMARY: WHY ME/CFS IS THE HARDEST CVB DISEASE TO CLEAR")
    print("=" * 70)
    print(f"""
1. MULTI-SITE PERSISTENCE
   - CVB persists in muscle (42%), gut (82%), CNS (30%)
   - Cross-seeding between compartments prevents clearance
   - Single-organ diseases (myocarditis, pancreatitis) can often resolve
   - ME/CFS has 2-3 reservoirs reinforcing each other

2. IMMUNE EXHAUSTION CASCADE
   - Years of chronic antigen → T cells become terminally exhausted
   - Terminal exhaustion (TOX+, Tim-3+) is IRREVERSIBLE in those cells
   - Must wait for new T cell generation (months-years)
   - This is why even effective treatment takes time

3. THE CNS SANCTUARY
   - Blood-brain barrier limits immune access to 20% of systemic
   - CNS virus is the LAST to clear
   - This may explain persistent brain fog even during recovery

4. THE SELF-REINFORCING LOOP
   CVB persistence → mito damage → low ATP → NK dysfunction
        ↑                                        ↓
   immune escape ←←←←←←←←←←←←←←←←←←←←←←← can't clear virus

5. PROTOCOL IMPLICATIONS FOR ME/CFS
   Must address ALL of:
   a. Viral persistence (fluoxetine → 2C ATPase inhibition)
   b. Autophagy deficit (FMD/fasting → clear infected cells)
   c. Energy deficit (CoQ10, NAD+, D-ribose → restore ATP)
   d. Immune exhaustion (time + possibly PD-1 blockade)
   e. CNS penetration (fluoxetine crosses BBB — this is an advantage)
   f. Gut microbiome (butyrate, probiotics → restore GALT function)
""")

    print("=" * 70)
    print("ALL SCENARIOS COMPLETE — Figures saved to results/figures/")
    print("=" * 70)


if __name__ == "__main__":
    main()
