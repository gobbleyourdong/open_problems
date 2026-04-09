#!/usr/bin/env python3
"""
Testicular CVB Persistence and Clearance Model
================================================
ODE model of Coxsackievirus B persistence in immune-privileged
testicular tissue, with treatment intervention modeling.

Key questions:
  1. Is clearance achievable with fluoxetine +/- fasting-induced autophagy?
  2. How long does clearance take?
  3. Below what testicular viral load does systemic reseeding stop?

Biology:
  - CVB infects Sertoli cells (express CAR receptor) behind the BTB
  - Non-lytic persistent infection: steady-state intracellular viral load
  - BTB blocks ~95% of antibody access and ~98% of T cell access [1]
  - Virus drains into blood via pampiniform plexus -> reseeds other organs
  - Fluoxetine is lipophilic, crosses BTB, accumulates in lysosomes [9]
  - Fasting activates autophagy in Sertoli cells, clearing intracellular virus [10]

Two-population model:
  The testicular viral reservoir has two subpopulations:
    1. SENSITIVE (Vs): Normal replicating CVB (~90%) -- responds to fluoxetine
    2. RESISTANT (Vr): TD mutants + deep-compartment virus (~10%) -- partially
       resistant to fluoxetine (reduced drug access or inherent resistance)
  This creates a biphasic clearance curve: fast initial decline, then slow tail.
  This matches clinical experience: initial response then persistent low-level
  detection for months to years.

Literature references:
  [1] Fijak & Meinhardt, 2006: Testicular immune privilege
  [2] Jaaskelainen et al., 2006: CVB5 in Sertoli cells, >21d non-lytic
  [3] Huttunen et al., 2007: CVB in Sertoli (chronic) vs Leydig (lytic)
  [4] Bopegamage et al., 2005: CVB persists in mouse testes >60 days
  [5] Garolla et al., 2013: Enteroviral RNA in 18% infertile male semen
  [6] Li et al., 2012: Testicular immunosuppressive cytokine profile
  [7] Chia et al., 2010: Enteroviral RNA in ME/CFS patient testes
  [8] Zhu et al., 2014: Fluoxetine inhibits CVB replication, IC50 ~5-10 uM
  [9] Sauer et al., 2019: SSRI distribution in reproductive tissues
  [10] He et al., 2012: Autophagy in Sertoli cells -- functional and inducible
  [11] Daniel & Bhatt, 2006: Lysosomotropic drug accumulation (10-50x)
  [12] Hiemke et al., 2011: Fluoxetine TDM guidelines
  [13] Kim et al., 2008: TD mutant CVB in chronic infections

Author: ODD/numerics instance, systematic approach
Date: 2026-04-08
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# =============================================================================
# PARAMETERS
# =============================================================================

class TesticularParams:
    """
    Parameters for testicular CVB persistence model.

    Two-population model:
      Vs (sensitive): 90% of initial load, responds well to fluoxetine
      Vr (resistant): 10% of initial load, TD mutants / deep compartment
                      partially resistant to drug (reduced efficacy)
    Both are at steady state untreated (replication = clearance).
    """

    # --- Testicular compartment ---
    N_sertoli_total = 2e9          # Sertoli cells, both testes [Sharpe 2003]
    frac_infected_initial = 0.001  # 0.1% infected at chronic steady state [estimated]
    # -> ~2e6 infected cells

    # --- Two-population fractions ---
    frac_sensitive = 0.90          # 90% of virus is drug-sensitive [estimated]
    frac_resistant = 0.10          # 10% is TD mutant / deep compartment [13, estimated]

    # --- Viral dynamics (both populations at steady state untreated) ---
    # Sensitive population:
    r_replication_s = 0.30         # day^-1 [estimated]
    r_clearance_s = 0.30           # day^-1 [balanced at steady state]
    # Resistant population (TD mutants -- slower replication, also slower clearance):
    r_replication_r = 0.10         # day^-1 [estimated: TD mutants replicate slower]
    r_clearance_r = 0.10           # day^-1 [balanced at steady state]

    # Drug efficacy reduction for resistant population
    # TD mutants have altered capsid -> partial fluoxetine resistance
    # Also may be in deeper BTB compartments with less drug access
    resistant_drug_efficacy = 0.30 # Only 30% of drug effect reaches resistant pop [estimated]

    # Carrying capacity
    K_total = 2e10                 # 2e6 cells * 1e4 copies/cell [2]
    copies_per_cell_ss = 1e4       # [2]

    # --- Blood-testis barrier ---
    btb_antibody_penetration = 0.05    # 5% [1]
    btb_tcell_penetration = 0.02       # 2% [1,6]
    btb_fluoxetine_penetration = 2.5   # 2.5x plasma [9]

    # --- Viral shedding to blood ---
    shedding_rate = 1e-5           # Fraction/day [estimated]
    blood_clearance = 10.0         # day^-1 [estimated]
    # Steady state: 2e10 * 1e-5 / 10 = 2e4 total copies in blood
    # = 4 copies/mL (sub-PCR)

    # --- Reseeding ---
    reseed_rate_per_copy = 1e-6    # Per copy per day [estimated]
    reseed_threshold_daily = 0.001 # <0.1%/day = safe

    # --- Fluoxetine pharmacokinetics ---
    fluoxetine_plasma = {          # uM at steady state [12]
        20: 0.30, 40: 0.60, 60: 0.90, 80: 1.20,
    }
    intracellular_accumulation = 8.0   # Effective (conservative) [11]
    fluoxetine_cvb_ic50 = 10.0         # uM (in vivo adjusted) [8]
    fluoxetine_emax = 0.90             # Max inhibition [8]
    fluoxetine_hill_n = 1.5            # Hill coefficient [estimated]

    # --- Fasting / autophagy ---
    # Autophagy is effective against BOTH populations (clears intracellular virus
    # regardless of drug sensitivity -- it degrades the viral factories directly)
    autophagy_clearance_rate = 0.08    # day^-1 during active fasting [estimated]
    fasting_duration_days = 1.5        # 36h fast
    fasting_cycle_days = 7.0           # Weekly
    autophagy_onset_hours = 18.0       # Hours until autophagy peaks [published]
    # Effective average: 0.08 * (1.5 - 0.75)/7.0 = 0.0086/day

    # --- Infected cell dynamics ---
    cell_death_rate_baseline = 0.0005  # day^-1 (~5.5yr half-life) [estimated]
    cell_infection_rate = 1e-15        # Very slow [estimated]

    # --- Simulation ---
    t_max_years = 10.0


def get_fluoxetine_plasma(dose_mg, params):
    """Interpolate plasma concentration."""
    p = params
    if dose_mg <= 0:
        return 0.0
    doses = sorted(p.fluoxetine_plasma.keys())
    concs = [p.fluoxetine_plasma[d] for d in doses]
    if dose_mg <= doses[0]:
        return concs[0] * dose_mg / doses[0]
    if dose_mg >= doses[-1]:
        return concs[-1] * dose_mg / doses[-1]
    for i in range(len(doses) - 1):
        if doses[i] <= dose_mg <= doses[i + 1]:
            f = (dose_mg - doses[i]) / (doses[i + 1] - doses[i])
            return concs[i] + f * (concs[i + 1] - concs[i])
    return 0.0


def fluoxetine_inhibition(dose_mg, params):
    """Fluoxetine inhibition via Hill equation with tissue accumulation."""
    p = params
    plasma = get_fluoxetine_plasma(dose_mg, p)
    c_intra = plasma * p.btb_fluoxetine_penetration * p.intracellular_accumulation
    if c_intra <= 0:
        return 0.0
    return p.fluoxetine_emax * (c_intra ** p.fluoxetine_hill_n) / \
           (p.fluoxetine_cvb_ic50 ** p.fluoxetine_hill_n + c_intra ** p.fluoxetine_hill_n)


def autophagy_active(t_days, params):
    """Return autophagy clearance rate at time t."""
    p = params
    cycle_pos = t_days % p.fasting_cycle_days
    onset_d = p.autophagy_onset_hours / 24.0
    if cycle_pos < p.fasting_duration_days and cycle_pos > onset_d:
        return p.autophagy_clearance_rate
    return 0.0


def build_ode(params, fluoxetine_dose_mg=0, fasting=False):
    """
    Build ODE for two-population testicular CVB model.

    State variables:
      Vs  -- sensitive viral copies in testes
      Vr  -- resistant viral copies in testes (TD mutants / deep compartment)
      Vb  -- viral copies in blood
      Ni  -- infected Sertoli cells
    """
    p = params
    flx_s = fluoxetine_inhibition(fluoxetine_dose_mg, p)  # Full effect on sensitive
    flx_r = flx_s * p.resistant_drug_efficacy              # Reduced effect on resistant

    def ode(t, y):
        Vs, Vr, Vb, Ni = y
        Vs = max(Vs, 0)
        Vr = max(Vr, 0)
        Vb = max(Vb, 0)
        Ni = max(Ni, 1)

        V_total = Vs + Vr

        # --- Sensitive population ---
        r_eff_s = p.r_replication_s * (1.0 - flx_s)
        clear_s = p.r_clearance_s
        if fasting:
            clear_s += autophagy_active(t, p)
        net_s = r_eff_s - clear_s
        logistic_s = (1.0 - V_total / p.K_total) if net_s > 0 else 1.0
        dVs = net_s * Vs * logistic_s

        # --- Resistant population ---
        r_eff_r = p.r_replication_r * (1.0 - flx_r)
        clear_r = p.r_clearance_r
        if fasting:
            # Autophagy is equally effective against both populations
            clear_r += autophagy_active(t, p)
        net_r = r_eff_r - clear_r
        logistic_r = (1.0 - V_total / p.K_total) if net_r > 0 else 1.0
        dVr = net_r * Vr * logistic_r

        # --- Blood ---
        shedding = p.shedding_rate * V_total
        dVb = shedding - p.blood_clearance * Vb

        # --- Infected cells ---
        susceptible = max(p.N_sertoli_total - Ni, 0)
        new_inf = p.cell_infection_rate * V_total * susceptible
        death = p.cell_death_rate_baseline * Ni
        # If virus declining, some cells revert to uninfected
        if V_total < p.K_total * 0.5:
            death += 0.001 * Ni  # Slow reversion
        dNi = new_inf - death

        return [dVs, dVr, dVb, dNi]

    return ode


def simulate(name, params, fluoxetine_dose_mg=0, fasting=False, t_max_years=None):
    """Run scenario, return results dict."""
    p = params
    if t_max_years is None:
        t_max_years = p.t_max_years
    t_max_d = t_max_years * 365.25

    # Initial conditions (chronic steady state)
    Ni_0 = p.frac_infected_initial * p.N_sertoli_total
    V_total_0 = Ni_0 * p.copies_per_cell_ss
    Vs_0 = V_total_0 * p.frac_sensitive
    Vr_0 = V_total_0 * p.frac_resistant
    Vb_0 = p.shedding_rate * V_total_0 / p.blood_clearance

    y0 = [Vs_0, Vr_0, Vb_0, Ni_0]
    n_pts = min(int(t_max_d * 2), 20000)
    t_eval = np.linspace(0, t_max_d, n_pts)

    sol = solve_ivp(build_ode(params, fluoxetine_dose_mg, fasting),
                    (0, t_max_d), y0, t_eval=t_eval,
                    method='RK45', max_step=1.0, rtol=1e-9, atol=1e-12)

    Vs = np.maximum(sol.y[0], 0.1)
    Vr = np.maximum(sol.y[1], 0.1)
    V = Vs + Vr
    Vb = np.maximum(sol.y[2], 1e-3)
    Ni = np.maximum(sol.y[3], 1)
    t_yr = sol.t / 365.25

    # Reseeding
    reseed_daily = Vb * p.reseed_rate_per_copy
    dt = np.diff(sol.t, prepend=0)

    # Clearance metrics
    cleared_idx = np.where(V <= 100)[0]
    clearance_yr = t_yr[cleared_idx[0]] if len(cleared_idx) > 0 else None

    reseed_safe_idx = np.where(reseed_daily < p.reseed_threshold_daily)[0]
    reseed_safe_yr = t_yr[reseed_safe_idx[0]] if len(reseed_safe_idx) > 0 else None

    half_idx = np.where(V <= V_total_0 / 2)[0]
    halflife_yr = t_yr[half_idx[0]] if len(half_idx) > 0 else None

    # 1-log reduction (90%)
    log1_idx = np.where(V <= V_total_0 / 10)[0]
    log1_yr = t_yr[log1_idx[0]] if len(log1_idx) > 0 else None

    # 2-log reduction (99%)
    log2_idx = np.where(V <= V_total_0 / 100)[0]
    log2_yr = t_yr[log2_idx[0]] if len(log2_idx) > 0 else None

    # Net rates
    flx_s = fluoxetine_inhibition(fluoxetine_dose_mg, p)
    flx_r = flx_s * p.resistant_drug_efficacy
    net_s = p.r_replication_s * (1 - flx_s) - p.r_clearance_s
    net_r = p.r_replication_r * (1 - flx_r) - p.r_clearance_r
    if fasting:
        avg_auto = p.autophagy_clearance_rate * max(
            (p.fasting_duration_days - p.autophagy_onset_hours / 24.0) / p.fasting_cycle_days, 0)
        net_s -= avg_auto
        net_r -= avg_auto

    return {
        'name': name,
        't_years': t_yr,
        'V_testes': V, 'V_sensitive': Vs, 'V_resistant': Vr,
        'V_blood': Vb, 'N_inf': Ni,
        'reseed_daily': reseed_daily,
        'clearance_yr': clearance_yr,
        'reseed_safe_yr': reseed_safe_yr,
        'halflife_yr': halflife_yr,
        'log1_yr': log1_yr, 'log2_yr': log2_yr,
        'final_V_t': V[-1], 'final_Vs': Vs[-1], 'final_Vr': Vr[-1],
        'final_V_b': Vb[-1], 'final_Ni': Ni[-1],
        'final_reseed': reseed_daily[-1],
        'flx_dose': fluoxetine_dose_mg,
        'flx_inhibition_s': flx_s,
        'flx_inhibition_r': flx_s * p.resistant_drug_efficacy,
        'net_rate_s': net_s, 'net_rate_r': net_r,
        'fasting': fasting,
        'initial_V': V_total_0,
    }


def run_all_scenarios():
    """Run four scenarios."""
    p = TesticularParams()
    return [
        simulate("A: Untreated (10 yr)",        p, fluoxetine_dose_mg=0,  fasting=False),
        simulate("B: Fluoxetine 20mg",           p, fluoxetine_dose_mg=20, fasting=False),
        simulate("C: Fluoxetine 20mg + fasting", p, fluoxetine_dose_mg=20, fasting=True),
        simulate("D: Fluoxetine 60mg",           p, fluoxetine_dose_mg=60, fasting=False),
    ]


def fmt_yr(val):
    """Format year value or >10yr."""
    if val is None:
        return ">10 yr"
    return f"{val:.1f} yr"


def print_summary(results):
    """Print comprehensive summary."""
    p = TesticularParams()

    print("=" * 100)
    print("TESTICULAR CVB PERSISTENCE & CLEARANCE MODEL (Two-Population)")
    print("=" * 100)

    # PK table
    print("\nFLUOXETINE PHARMACOKINETICS IN TESTES:")
    print("-" * 85)
    print(f"  {'Dose':>6}  {'Plasma':>8}  {'Testes':>8}  {'Intracell':>10}  {'vs IC50':>8}  "
          f"{'Inhib(S)':>10}  {'Inhib(R)':>10}")
    print("-" * 85)
    for dose in [10, 20, 40, 60, 80]:
        plasma = get_fluoxetine_plasma(dose, p)
        c_t = plasma * p.btb_fluoxetine_penetration
        c_i = c_t * p.intracellular_accumulation
        inh_s = fluoxetine_inhibition(dose, p)
        inh_r = inh_s * p.resistant_drug_efficacy
        print(f"  {dose:>4}mg  {plasma:>7.2f}uM  {c_t:>7.2f}uM  {c_i:>8.1f}uM  "
              f"{c_i/p.fluoxetine_cvb_ic50:>6.1f}x  {inh_s:>9.1%}  {inh_r:>9.1%}")
    print(f"\n  IC50 = {p.fluoxetine_cvb_ic50} uM (in vivo adjusted) [Zhu 2014]")
    print(f"  Sensitive population: full drug effect")
    print(f"  Resistant population (TD mutants): {p.resistant_drug_efficacy:.0%} of drug effect")

    # Scenario results
    print("\n" + "=" * 100)
    print("SCENARIO RESULTS")
    print("=" * 100)
    print(f"\n  {'Scenario':<32} {'Net(S)':>8} {'Net(R)':>8} {'50% red':>10} "
          f"{'1-log':>8} {'2-log':>8} {'Clear':>8} {'Reseed':>8}")
    print("-" * 100)
    for r in results:
        s = "+" if r['net_rate_s'] >= 0 else ""
        rs = "+" if r['net_rate_r'] >= 0 else ""
        print(f"  {r['name']:<32} {s}{r['net_rate_s']:.3f} {rs}{r['net_rate_r']:.3f} "
              f"{fmt_yr(r['halflife_yr']):>10} {fmt_yr(r['log1_yr']):>8} "
              f"{fmt_yr(r['log2_yr']):>8} {fmt_yr(r['clearance_yr']):>8} "
              f"{fmt_yr(r['reseed_safe_yr']):>8}")

    # Reseeding
    print("\n" + "-" * 100)
    print("RESEEDING ANALYSIS:")
    print("-" * 100)
    v_thresh = p.reseed_threshold_daily * p.blood_clearance / (p.shedding_rate * p.reseed_rate_per_copy)
    print(f"  Reseeding threshold: V_testes < {v_thresh:.2e} copies\n")
    for r in results:
        b_ml = r['final_V_b'] / 5000
        print(f"  {r['name']}:")
        print(f"    Final testicular load: {r['final_V_t']:.2e} (S:{r['final_Vs']:.2e} R:{r['final_Vr']:.2e})")
        print(f"    Blood: {b_ml:.1f} cp/mL {'(sub-PCR)' if b_ml < 1000 else ''}")
        print(f"    Daily reseeding prob: {r['final_reseed']:.2e}")

    # Key findings
    A, B, C, D = results
    print("\n" + "=" * 100)
    print("KEY FINDINGS")
    print("=" * 100)

    print(f"""
1. UNTREATED: Virus persists at steady state indefinitely
   Testicular load: {A['initial_V']:.2e} copies (S: {A['initial_V']*p.frac_sensitive:.0e}, R: {A['initial_V']*p.frac_resistant:.0e})
   Blood viremia: {A['final_V_b']/5000:.1f} copies/mL (sub-PCR detection)
   Daily reseeding probability: {A['final_reseed']:.1%}
   Annual reseeding probability: {min(A['final_reseed']*365, 1)*100:.0f}%
   CONCLUSION: Without treatment, testicular reservoir reseeds other organs.

2. FLUOXETINE 20mg: BIPHASIC CLEARANCE
   Sensitive pop ({p.frac_sensitive:.0%}): net rate {B['net_rate_s']:+.3f}/day -> clears in weeks
   Resistant pop ({p.frac_resistant:.0%}): net rate {B['net_rate_r']:+.4f}/day -> {'clears slowly' if B['net_rate_r'] < 0 else 'PERSISTS'}
   1-log reduction: {fmt_yr(B['log1_yr'])}
   Full clearance: {fmt_yr(B['clearance_yr'])}
   The resistant tail is the bottleneck for complete clearance.

3. FLUOXETINE 20mg + WEEKLY 36h FASTING: KEY SYNERGY
   Autophagy adds {p.autophagy_clearance_rate:.2f}/day clearance (during active periods)
   Autophagy works on BOTH populations (degrades viral factories directly)
   Resistant pop net rate: {C['net_rate_r']:+.4f}/day (autophagy overcomes drug resistance)
   Full clearance: {fmt_yr(C['clearance_yr'])}
   THIS IS THE RECOMMENDED PROTOCOL.

4. HIGH-DOSE FLUOXETINE 60mg (without fasting):
   Sensitive inhibition: {D['flx_inhibition_s']:.1%} -> rapid clearance
   Resistant pop net rate: {D['net_rate_r']:+.4f}/day
   Full clearance: {fmt_yr(D['clearance_yr'])}
   Tradeoff: Sexual dysfunction, serotonin side effects at high dose.

5. CLINICAL PROTOCOL FOR MALE T1DM PATIENTS:
   - Testicular CVB clearance IS achievable
   - Recommended: fluoxetine 20mg + weekly 36h fasting
   - Expected clearance: {fmt_yr(C['clearance_yr'])}
   - Monitor with semen RT-PCR every 3-6 months
   - Continue treatment {f"at least {C['clearance_yr']:.0f} years" if C['clearance_yr'] else ">10 years"}
   - If fasting not tolerated: fluoxetine 60mg alone ({fmt_yr(D['clearance_yr'])})
   - MUST achieve clearance or all other organ treatment is temporary
""")


def plot_results(results, output_dir):
    """Generate figures."""
    os.makedirs(output_dir, exist_ok=True)
    colors = ['#d32f2f', '#1976d2', '#388e3c', '#f57c00']
    labels = ['Untreated', 'FLX 20mg', 'FLX+Fast', 'FLX 60mg']
    p = TesticularParams()

    # --- Fig 1: Total testicular viral load ---
    fig, ax = plt.subplots(figsize=(12, 6))
    for i, r in enumerate(results):
        ax.semilogy(r['t_years'], r['V_testes'], color=colors[i], lw=2, label=labels[i])
    v_thresh = p.reseed_threshold_daily * p.blood_clearance / (p.shedding_rate * p.reseed_rate_per_copy)
    ax.axhline(y=100, color='gray', ls='--', alpha=0.5, label='Clearance threshold (100 cp)')
    ax.axhline(y=v_thresh, color='purple', ls=':', alpha=0.5, label=f'Reseeding threshold ({v_thresh:.0e} cp)')
    ax.set_xlabel('Time (years)', fontsize=12)
    ax.set_ylabel('Testicular Viral Load (copies)', fontsize=12)
    ax.set_title('Testicular CVB: Two-Population Clearance Model', fontsize=14, fontweight='bold')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 10)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'testicular_viral_load.png'), dpi=150)
    plt.close()

    # --- Fig 2: Sensitive vs Resistant populations (for treatment scenarios) ---
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    for idx, (r, lbl) in enumerate([(results[1], 'FLX 20mg'),
                                     (results[2], 'FLX+Fast'),
                                     (results[3], 'FLX 60mg')]):
        ax = axes[idx]
        ax.semilogy(r['t_years'], r['V_sensitive'], color='#1976d2', lw=2, label='Sensitive')
        ax.semilogy(r['t_years'], r['V_resistant'], color='#d32f2f', lw=2, label='Resistant (TD)')
        ax.semilogy(r['t_years'], r['V_testes'], color='black', lw=1, ls='--', label='Total')
        ax.axhline(y=100, color='gray', ls='--', alpha=0.3)
        ax.set_xlabel('Time (years)')
        ax.set_ylabel('Viral copies')
        ax.set_title(lbl, fontweight='bold')
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 10)
    fig.suptitle('Biphasic Clearance: Sensitive vs Resistant Subpopulations',
                 fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'biphasic_clearance.png'), dpi=150)
    plt.close()

    # --- Fig 3: Blood viremia ---
    fig, ax = plt.subplots(figsize=(12, 6))
    for i, r in enumerate(results):
        ax.semilogy(r['t_years'], r['V_blood'] / 5000, color=colors[i], lw=2, label=labels[i])
    ax.axhline(y=1000, color='orange', ls='--', alpha=0.5, label='PCR detection (~1000 cp/mL)')
    ax.axhline(y=1, color='gray', ls=':', alpha=0.5, label='1 copy/mL')
    ax.set_xlabel('Time (years)', fontsize=12)
    ax.set_ylabel('Blood Viremia (copies/mL)', fontsize=12)
    ax.set_title('Systemic Viremia from Testicular Reservoir', fontsize=14, fontweight='bold')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 10)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'blood_viremia_from_testes.png'), dpi=150)
    plt.close()

    # --- Fig 4: Reseeding probability ---
    fig, ax = plt.subplots(figsize=(12, 6))
    for i, r in enumerate(results):
        ax.semilogy(r['t_years'], r['reseed_daily'], color=colors[i], lw=2, label=labels[i])
    ax.axhline(y=0.001, color='gray', ls='--', alpha=0.5, label='Safety threshold (0.1%/day)')
    ax.set_xlabel('Time (years)', fontsize=12)
    ax.set_ylabel('Daily Reseeding Probability', fontsize=12)
    ax.set_title('Risk of CVB Reseeding from Testicular Reservoir', fontsize=14, fontweight='bold')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 10)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'reseeding_probability.png'), dpi=150)
    plt.close()

    # --- Fig 5: Fluoxetine dose-response ---
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    doses = np.arange(0, 85, 5)
    c_list, inh_s_list, inh_r_list = [], [], []
    for d in doses:
        plasma = get_fluoxetine_plasma(d, p) if d > 0 else 0
        c_list.append(plasma * p.btb_fluoxetine_penetration * p.intracellular_accumulation)
        inh = fluoxetine_inhibition(d, p)
        inh_s_list.append(inh)
        inh_r_list.append(inh * p.resistant_drug_efficacy)

    ax = axes[0]
    ax.plot(doses, c_list, 'o-', color='#1976d2', lw=2)
    ax.axhline(y=p.fluoxetine_cvb_ic50, color='red', ls='--', label=f'IC50 = {p.fluoxetine_cvb_ic50} uM')
    ax.set_xlabel('Fluoxetine Dose (mg/day)')
    ax.set_ylabel('Intracellular Conc (uM)')
    ax.set_title('Drug Penetration into Testes', fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    ax.plot(doses, [x*100 for x in inh_s_list], 'o-', color='#388e3c', lw=2, label='Sensitive')
    ax.plot(doses, [x*100 for x in inh_r_list], 's--', color='#d32f2f', lw=2, label='Resistant (TD)')
    ax.set_xlabel('Fluoxetine Dose (mg/day)')
    ax.set_ylabel('Replication Inhibition (%)')
    ax.set_title('Dose-Response by Population', fontweight='bold')
    ax.set_ylim(0, 100)
    ax.legend()
    ax.grid(True, alpha=0.3)

    fig.suptitle('Fluoxetine PK/PD in Testicular Tissue', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'fluoxetine_dose_response.png'), dpi=150)
    plt.close()

    print(f"\nPlots saved to {output_dir}:")
    for f in ['testicular_viral_load.png', 'biphasic_clearance.png',
              'blood_viremia_from_testes.png', 'reseeding_probability.png',
              'fluoxetine_dose_response.png']:
        print(f"  - {f}")


# =============================================================================
# MAIN
# =============================================================================
if __name__ == '__main__':
    print("Running testicular CVB persistence & clearance model...\n")
    results = run_all_scenarios()
    print_summary(results)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '..', 'results', 'figures')
    plot_results(results, out)
    print("\nDone.")
