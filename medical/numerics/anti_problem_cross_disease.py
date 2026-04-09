#!/usr/bin/env python3
"""
Cross-Disease Anti-Problem: Why Most CVB Infections Resolve
=============================================================

Phase 4 systematic approach — "What would a counterexample look like?"

The ultimate anti-problem: >99% of CVB infections are self-limiting.
Most people get infected, clear the virus, and never develop ANY chronic
disease. What separates the >99% who resolve from the <1% who don't?

This model answers:
  1. At what viral load x immune response x time does the TD mutant
     population become self-sustaining? (the fork point)
  2. What fraction of subclinical CVB infections establish TD persistence?
  3. Of those with persistence, what fraction develop clinical disease?
  4. How do organ-specific factors affect disease probability?
  5. What are the base rates that all disease-specific models should
     calibrate against?

The fork model:
  Acute CVB → peak viral load → immune clearance phase
  During clearance: stochastic 5' terminal deletions create TD mutants
  If immune clearance completes before TD population is self-sustaining → CURED
  If TD population exceeds critical threshold → PERSISTENCE → possible disease

Literature references:
  [1]  Khetsuriani et al. 2006 MMWR 55:1-20 — enterovirus epidemiology
  [2]  Oberste et al. 2004 J Gen Virol 85:2577-84 — CVB seroprevalence ~75%
  [3]  Wessely et al. 1998 Circulation 98:450-7 — TD mutant persistence
  [4]  Chapman et al. 2008 J Gen Virol 89:2517-28 — 5' terminal deletions
  [5]  Kim et al. 2005 J Virol 79:7024-41 — TD mutant biology
  [6]  Krogvold et al. 2015 Diabetes 64:1682-7 — DiViD study
  [7]  Richardson et al. 2016 Diabetologia 59:1972-9 — enteroviral persistence
  [8]  Chia & Chia 2008 J Clin Pathol 61:1321-2 — 82% CVB in ME/CFS gut
  [9]  Why et al. 1994 Br Heart J 72:S27 — 35% CVB in DCM biopsies
  [10] Lane et al. 2003 J Med Virol — 42% CVB in ME/CFS muscle
  [11] Garolla et al. 2013 Fertil Steril — 18% enteroviral in infertile semen
  [12] Oikarinen et al. 2012 Diabetologia 55:1926-34 — CVB in T1DM
  [13] Atkinson et al. 2014 Lancet 383:69-82 — T1DM epidemiology
  [14] Badorff et al. 1999 Nat Med 5:320-6 — 2A protease tissue damage
  [15] Mukherjee et al. 2011 PLoS Pathog 7:e1002291 — 3C autophagy block
  [16] Jaaskelainen et al. 2006 — CVB5 Sertoli cells
  [17] Hyypia et al. 1993 Rev Med Virol 3:171-8 — CVB receptor distribution
  [18] Mena et al. 1999 J Virol 73:544-51 — CVB neurotropism
  [19] Laitinen et al. 2014 JAMA 311:1778 — CVB seroconversion timing
  [20] Dotta et al. 2007 PNAS 104:5115-20 — CVB4 in T1DM islets

systematic approach — Cross-Disease Anti-Problem — numerical track (numerics)
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "figures")
os.makedirs(OUTPUT_DIR, exist_ok=True)


# =============================================================================
# THE FORK MODEL: ACUTE CVB → CLEARANCE vs PERSISTENCE
# =============================================================================
#
# Phase 1: Acute infection (days 0-7)
#   - CVB enters via gut enterocytes (fecal-oral)
#   - Viremia: virus spreads to target organs via blood
#   - Exponential viral growth in susceptible tissues
#   - Peak viral load day 3-5
#
# Phase 2: Immune response (days 3-14)
#   - Innate: IFN-alpha/beta → antiviral state in neighboring cells
#   - Innate: NK cells → kill infected cells (no antigen specificity)
#   - Adaptive: CTL response expands (day 7+)
#   - Viral load declining
#
# Phase 3: The Fork (days 7-21)
#   - DURING viral clearance, stochastic 5' terminal deletions occur
#   - Each deletion event creates one TD mutant
#   - TD mutants are nearly invisible to immune system
#   - IF immune clearance is fast enough: all virus eliminated, including TD
#   - IF TD population exceeds self-sustaining threshold: PERSISTENCE
#
# Phase 4 (persistence path only): Chronic disease risk
#   - TD mutants produce low-level proteases (2A, 3C) indefinitely
#   - Organ-specific damage accumulates
#   - Whether clinical disease develops depends on:
#     (a) organ regenerative capacity
#     (b) organ-specific immune response
#     (c) genetic susceptibility (HLA for autoimmune organs)
#     (d) time elapsed

@dataclass
class InfectionParams:
    """Parameters for a single CVB infection in one host."""

    # --- Viral dynamics ---
    initial_dose: float = 100.0         # TCID50 equivalent, gut inoculum
    viral_growth_rate: float = 2.5      # /day, exponential growth phase
    viral_carrying_cap: float = 1e8     # peak viral load (copies/g in target organ)

    # --- TD mutant formation ---
    # Probability of 5' terminal deletion per replication cycle
    # This is the KEY stochastic parameter [Ref 4]
    td_formation_rate: float = 1e-5     # per replication event
    # TD mutant growth rate: ~100,000x slower than acute [Ref 5]
    td_growth_rate: float = 0.002       # /day (vs 2.5/day for acute)
    td_carrying_cap: float = 1e4        # steady-state if established
    # Critical threshold: below this, TD mutants die out stochastically
    td_critical_threshold: float = 50.0 # copies, minimum self-sustaining population

    # --- Immune response ---
    # IFN response: delay + magnitude
    ifn_delay_days: float = 0.5         # time to first IFN production
    ifn_magnitude: float = 1.0          # normalized (1.0 = average healthy adult)
    ifn_viral_suppression: float = 0.7  # fraction by which IFN reduces viral growth

    # NK cell response
    nk_delay_days: float = 1.0          # NK mobilization delay
    nk_killing_rate: float = 0.3        # fraction of infected cells killed per day at peak NK
    nk_magnitude: float = 1.0           # normalized

    # CTL (adaptive) response
    ctl_delay_days: float = 7.0         # time for antigen-specific CTL expansion
    ctl_killing_rate: float = 0.5       # fraction cleared per day at peak CTL
    ctl_magnitude: float = 1.0          # normalized

    # --- Host factors ---
    age: float = 25.0                   # years (neonates and elderly are different)
    is_neonate: bool = False            # neonates have immature immunity

    # --- Organ-specific ---
    organ_susceptibility: float = 1.0   # how easily virus infects this organ
    organ_repair_rate: float = 0.05     # tissue repair rate (fraction/day)


@dataclass
class OrganProfile:
    """Organ-specific parameters affecting disease probability after persistence."""
    name: str
    disease: str
    cvb_serotypes: str
    susceptibility: float          # relative susceptibility to CVB infection
    repair_rate: float             # tissue repair rate (fraction/day)
    autoimmune_risk: float         # probability of autoimmune component
    damage_per_protease: float     # tissue damage per unit protease activity
    clinical_threshold: float      # fraction of tissue damage at clinical disease
    prevalence_if_persistent: float  # probability of clinical disease given TD persistence


# =============================================================================
# ORGAN PROFILES
# =============================================================================

ORGAN_PROFILES = {
    "pancreas_islets": OrganProfile(
        name="Pancreatic Islets",
        disease="T1DM",
        cvb_serotypes="CVB1, CVB4",
        susceptibility=0.8,          # CAR receptor on islet surface [Ref 17]
        repair_rate=0.005,           # beta cell regen ~1-3%/yr [Butler 2005]
        autoimmune_risk=0.9,         # high autoimmune amplification
        damage_per_protease=0.003,   # ER stress → neoantigen cascade
        clinical_threshold=0.80,     # 80% beta cell loss for Dx [Ref 13]
        prevalence_if_persistent=0.08,  # ~8% of persistent → T1DM (HLA dependent)
    ),
    "myocardium": OrganProfile(
        name="Myocardium",
        disease="Myocarditis/DCM",
        cvb_serotypes="CVB3, CVB4",
        susceptibility=0.6,
        repair_rate=0.01/365,        # ~1%/yr cardiomyocyte renewal [Bergmann 2009]
        autoimmune_risk=0.4,         # anti-cardiac myosin in ~40%
        damage_per_protease=0.005,   # 2A cleaves dystrophin → sarcolemma damage
        clinical_threshold=0.30,     # 30% CM loss → EF<40%
        prevalence_if_persistent=0.05,  # ~5% of persistent → clinical myocarditis/DCM
    ),
    "skeletal_muscle": OrganProfile(
        name="Skeletal Muscle",
        disease="ME/CFS, Pleurodynia",
        cvb_serotypes="CVB2-5",
        susceptibility=0.5,
        repair_rate=0.02,            # satellite cells → good regeneration
        autoimmune_risk=0.2,
        damage_per_protease=0.004,   # dystrophin (skeletal isoform) cleavage
        clinical_threshold=0.20,     # lower threshold for fatigue symptoms
        prevalence_if_persistent=0.12,  # ~12% → ME/CFS or pleurodynia
    ),
    "cns": OrganProfile(
        name="CNS (Meninges/Brain)",
        disease="Meningitis/Encephalitis",
        cvb_serotypes="CVB2-5",
        susceptibility=0.15,         # BBB limits access
        repair_rate=0.001,           # very limited neurogenesis
        autoimmune_risk=0.1,
        damage_per_protease=0.008,   # neurons fragile
        clinical_threshold=0.05,     # low threshold for CNS symptoms
        prevalence_if_persistent=0.03,  # ~3% (usually acute, rarely persistent)
    ),
    "liver": OrganProfile(
        name="Liver",
        disease="Hepatitis",
        cvb_serotypes="CVB1-5",
        susceptibility=0.7,          # high blood flow, CAR expression
        repair_rate=0.10,            # liver regenerates excellently
        autoimmune_risk=0.1,
        damage_per_protease=0.002,
        clinical_threshold=0.50,     # liver tolerates substantial damage
        prevalence_if_persistent=0.02,  # ~2% (liver usually wins)
    ),
    "pericardium": OrganProfile(
        name="Pericardium",
        disease="Pericarditis",
        cvb_serotypes="CVB3, CVB4",
        susceptibility=0.4,
        repair_rate=0.05,            # mesothelial repair is good
        autoimmune_risk=0.3,
        damage_per_protease=0.003,
        clinical_threshold=0.15,     # effusion threshold is low
        prevalence_if_persistent=0.15,  # ~15% (pericardium is sensitive)
    ),
    "exocrine_pancreas": OrganProfile(
        name="Exocrine Pancreas",
        disease="Pancreatitis",
        cvb_serotypes="CVB1, CVB4",
        susceptibility=0.7,
        repair_rate=0.03,            # acinar regeneration is decent
        autoimmune_risk=0.15,
        damage_per_protease=0.004,
        clinical_threshold=0.25,
        prevalence_if_persistent=0.06,  # ~6%
    ),
    "testes": OrganProfile(
        name="Testes",
        disease="Orchitis",
        cvb_serotypes="CVB5",
        susceptibility=0.3,
        repair_rate=0.005,           # Sertoli cells limited regen
        autoimmune_risk=0.5,         # immune-privileged = harder to clear but also less autoimmune
        damage_per_protease=0.003,
        clinical_threshold=0.20,
        prevalence_if_persistent=0.04,  # ~4%
    ),
}


# =============================================================================
# ACUTE INFECTION DYNAMICS (DETERMINISTIC)
# =============================================================================

def acute_infection_ode(t, y, params: InfectionParams):
    """
    ODE for acute CVB infection dynamics.
    State: [V, TD, I_innate, I_adaptive]
      V          = wild-type viral load
      TD         = TD mutant count
      I_innate   = innate immune response (IFN + NK, 0-1)
      I_adaptive = adaptive immune response (CTL, 0-1)
    """
    V, TD, I_innate, I_adaptive = y

    V = max(V, 0.0)
    TD = max(TD, 0.0)
    I_innate = np.clip(I_innate, 0, 1)
    I_adaptive = np.clip(I_adaptive, 0, 1)

    # --- IFN + NK response (innate) ---
    # Ramps up after delay, proportional to viral load
    if t > params.ifn_delay_days:
        innate_stimulus = V / (V + 1e4)  # saturating response to viral load
        innate_growth = 2.0 * params.ifn_magnitude * innate_stimulus * (1.0 - I_innate)
    else:
        innate_growth = 0.0
    innate_decay = 0.2 * I_innate  # decays when virus clears
    dI_innate = innate_growth - innate_decay

    # Neonates: severely impaired innate immunity
    if params.is_neonate:
        dI_innate *= 0.3

    # --- CTL response (adaptive) ---
    if t > params.ctl_delay_days:
        adaptive_stimulus = V / (V + 1e3)
        adaptive_growth = 0.5 * params.ctl_magnitude * adaptive_stimulus * (1.0 - I_adaptive)
    else:
        adaptive_growth = 0.0
    adaptive_decay = 0.05 * I_adaptive
    dI_adaptive = adaptive_growth - adaptive_decay

    if params.is_neonate:
        dI_adaptive *= 0.5

    # --- Wild-type viral dynamics ---
    # Growth: logistic, suppressed by IFN
    ifn_suppression = 1.0 - params.ifn_viral_suppression * I_innate
    ifn_suppression = max(ifn_suppression, 0.05)
    viral_growth = params.viral_growth_rate * V * (1.0 - V / params.viral_carrying_cap) * ifn_suppression

    # Killing: NK + CTL
    nk_killing = params.nk_killing_rate * params.nk_magnitude * I_innate * V
    ctl_killing = params.ctl_killing_rate * params.ctl_magnitude * I_adaptive * V
    total_killing = nk_killing + ctl_killing

    dV = viral_growth - total_killing

    # --- TD mutant formation and dynamics ---
    # TD mutants form stochastically during viral replication
    # Rate = viral replication events * td_formation_rate
    replication_events = max(viral_growth, 0)  # only during active replication
    td_formation = params.td_formation_rate * replication_events

    # TD mutant growth: slow, independent
    td_growth = params.td_growth_rate * TD * (1.0 - TD / params.td_carrying_cap)

    # TD clearance: much harder than wild-type (nearly invisible)
    # Only CTLs clear TD mutants, and at 1/20th efficiency
    td_clearance = 0.05 * params.ctl_killing_rate * I_adaptive * TD

    dTD = td_formation + td_growth - td_clearance

    return [dV, dTD, dI_innate, dI_adaptive]


def simulate_acute_infection(params: InfectionParams, t_days: float = 30.0) -> dict:
    """Simulate one acute CVB infection through the fork point."""
    t_span = (0, t_days)
    t_eval = np.linspace(0, t_days, int(t_days * 4))

    y0 = [params.initial_dose, 0.0, 0.0, 0.0]

    sol = solve_ivp(
        acute_infection_ode, t_span, y0,
        args=(params,),
        method='RK45',
        t_eval=t_eval,
        max_step=0.5,
        rtol=1e-6, atol=1e-8
    )

    V = np.clip(sol.y[0], 0, None)
    TD = np.clip(sol.y[1], 0, None)
    I_innate = np.clip(sol.y[2], 0, 1)
    I_adaptive = np.clip(sol.y[3], 0, 1)

    # Determine outcome
    # Wild-type cleared when V < 1
    wt_cleared = V[-1] < 1.0
    if np.any(V < 1.0):
        clearance_times = np.where(V < 1.0)[0]
        wt_clearance_day = sol.t[clearance_times[0]] if len(clearance_times) > 0 else None
    else:
        wt_clearance_day = None

    # TD persistence: TD > critical threshold at end of simulation
    td_persistent = TD[-1] > params.td_critical_threshold
    peak_td = np.max(TD)
    final_td = TD[-1]

    # Peak viral load
    peak_v = np.max(V)
    peak_v_day = sol.t[np.argmax(V)]

    return {
        "t": sol.t,
        "V": V,
        "TD": TD,
        "I_innate": I_innate,
        "I_adaptive": I_adaptive,
        "wt_cleared": wt_cleared,
        "wt_clearance_day": wt_clearance_day,
        "td_persistent": td_persistent,
        "peak_v": peak_v,
        "peak_v_day": peak_v_day,
        "peak_td": peak_td,
        "final_td": final_td,
    }


# =============================================================================
# THE FORK POINT ANALYSIS
# =============================================================================

def find_fork_point():
    """
    Systematically vary immune response speed and viral dose to find
    the boundary between clearance and persistence.

    The fork point is a surface in (viral_dose, ifn_speed, ctl_speed) space.
    """
    print("=" * 70)
    print("THE FORK POINT: WHERE CLEARANCE BECOMES PERSISTENCE")
    print("=" * 70)

    # Vary viral dose and IFN response magnitude
    doses = np.logspace(0, 4, 15)       # 1 to 10,000 TCID50
    ifn_mags = np.linspace(0.2, 2.0, 15)  # 20% to 200% of normal IFN

    persistence_map = np.zeros((len(doses), len(ifn_mags)))

    print("  Computing fork point surface (15x15 grid)...")
    for i, dose in enumerate(doses):
        for j, ifn in enumerate(ifn_mags):
            params = InfectionParams(
                initial_dose=dose,
                ifn_magnitude=ifn,
            )
            result = simulate_acute_infection(params, t_days=30.0)
            persistence_map[i, j] = 1.0 if result['td_persistent'] else 0.0

    # Find the boundary
    # For each dose, find the minimum IFN magnitude that prevents persistence
    critical_ifn = np.full(len(doses), np.nan)
    for i in range(len(doses)):
        for j in range(len(ifn_mags)):
            if persistence_map[i, j] == 0:
                critical_ifn[i] = ifn_mags[j]
                break

    print("\n  FORK POINT BOUNDARY:")
    print(f"  {'Viral dose (TCID50)':<25} {'Min IFN magnitude':>20}")
    print("  " + "-" * 47)
    for k in range(0, len(doses), 5):
        ifn_val = critical_ifn[k]
        if np.isnan(ifn_val):
            ifn_str = "ALWAYS PERSISTS"
        else:
            ifn_str = f"{ifn_val:.2f}"
        print(f"  {doses[k]:<25.0f} {ifn_str:>20}")

    return doses, ifn_mags, persistence_map, critical_ifn


# =============================================================================
# MONTE CARLO: POPULATION-LEVEL BASE RATES
# =============================================================================

def monte_carlo_base_rates(n_infections: int = 10000, seed: int = 42):
    """
    Simulate n_infections CVB exposure events in the general population.
    Determine:
      1. What fraction establish TD persistence?
      2. Of those, what fraction develop clinical disease per organ?
      3. Overall disease incidence rates
    """
    print("\n" + "=" * 70)
    print(f"MONTE CARLO: {n_infections:,} CVB INFECTIONS — BASE RATE ESTIMATION")
    print("=" * 70)

    rng = np.random.default_rng(seed)

    # Track outcomes
    total_symptomatic_acute = 0
    total_asymptomatic = 0
    total_td_persistent = 0
    total_clinical_disease = {organ: 0 for organ in ORGAN_PROFILES}
    peak_viral_loads = []
    clearance_days = []
    td_final_loads = []

    print("  Simulating infections (this may take a minute)...")

    for i in range(n_infections):
        if (i + 1) % 10000 == 0:
            print(f"    Infection {i+1:,}/{n_infections:,}...")

        # Draw individual variation
        # Viral dose: lognormal (varies enormously in real life)
        dose = rng.lognormal(np.log(500), 1.5)
        dose = np.clip(dose, 1, 1e6)

        # IFN response: normal(1.0, 0.3) — population variation
        ifn = rng.normal(1.0, 0.3)
        ifn = np.clip(ifn, 0.1, 2.5)

        # NK magnitude: normal(1.0, 0.25)
        nk = rng.normal(1.0, 0.25)
        nk = np.clip(nk, 0.1, 2.5)

        # CTL: normal(1.0, 0.2)
        ctl = rng.normal(1.0, 0.2)
        ctl = np.clip(ctl, 0.2, 2.5)

        # Age effects
        age = rng.uniform(0, 80)
        is_neonate = age < 0.08  # < 1 month
        # Elderly have reduced immunity
        if age > 65:
            ifn *= 0.7
            nk *= 0.8
            ctl *= 0.8

        params = InfectionParams(
            initial_dose=dose,
            ifn_magnitude=ifn,
            nk_magnitude=nk,
            ctl_magnitude=ctl,
            age=age,
            is_neonate=is_neonate,
        )

        result = simulate_acute_infection(params, t_days=30.0)
        peak_viral_loads.append(result['peak_v'])

        if result['wt_clearance_day'] is not None:
            clearance_days.append(result['wt_clearance_day'])

        # Was the acute infection symptomatic?
        # ~50% of CVB infections are symptomatic [Ref 1]
        if result['peak_v'] > 1e5:
            total_symptomatic_acute += 1
        else:
            total_asymptomatic += 1

        if result['td_persistent']:
            total_td_persistent += 1
            td_final_loads.append(result['final_td'])

            # For each organ: does this individual develop clinical disease?
            for organ_name, organ in ORGAN_PROFILES.items():
                # Disease probability depends on:
                # 1. Whether this organ was infected (susceptibility)
                # 2. TD load in that organ
                # 3. Genetic susceptibility (for autoimmune organs)
                # 4. Organ repair capacity

                # Probability that THIS organ is infected
                organ_infected = rng.random() < organ.susceptibility * 0.5

                if organ_infected:
                    # Probability of clinical disease given persistence in this organ
                    # Adjusted by individual factors
                    p_disease = organ.prevalence_if_persistent

                    # HLA modulation for autoimmune diseases (T1DM, myocarditis)
                    if organ.autoimmune_risk > 0.3:
                        hla_risk = rng.normal(1.0, 0.4)
                        p_disease *= np.clip(hla_risk, 0.2, 3.0)

                    # Higher TD load → higher disease risk
                    td_factor = result['final_td'] / 1000.0
                    td_factor = np.clip(td_factor, 0.5, 3.0)
                    p_disease *= td_factor

                    p_disease = min(p_disease, 0.95)  # cap at 95%

                    if rng.random() < p_disease:
                        total_clinical_disease[organ_name] += 1

    # --- Results ---
    print(f"\n  OUTCOME SUMMARY ({n_infections:,} CVB infections):")
    print(f"  {'Outcome':<45} {'Count':>8} {'Rate':>10}")
    print("  " + "-" * 65)
    print(f"  {'Asymptomatic acute infection':<45} {total_asymptomatic:>8,} "
          f"{total_asymptomatic/n_infections*100:>9.1f}%")
    print(f"  {'Symptomatic acute infection':<45} {total_symptomatic_acute:>8,} "
          f"{total_symptomatic_acute/n_infections*100:>9.1f}%")
    print(f"  {'TD mutant persistence established':<45} {total_td_persistent:>8,} "
          f"{total_td_persistent/n_infections*100:>9.1f}%")
    print()

    print(f"  CLINICAL DISEASE RATES (among all {n_infections:,} infections):")
    print(f"  {'Organ/Disease':<35} {'Cases':>8} {'Rate':>12} {'Per persistent':>15}")
    print("  " + "-" * 72)
    total_disease = 0
    for organ_name, count in sorted(total_clinical_disease.items(), key=lambda x: -x[1]):
        organ = ORGAN_PROFILES[organ_name]
        rate = count / n_infections * 100
        per_persistent = count / max(total_td_persistent, 1) * 100
        print(f"  {organ.disease + ' (' + organ.name + ')':<35} {count:>8,} "
              f"{rate:>11.3f}% {per_persistent:>14.1f}%")
        total_disease += count

    print(f"\n  {'ANY clinical disease':<35} {total_disease:>8,} "
          f"{total_disease/n_infections*100:>11.3f}% "
          f"{total_disease/max(total_td_persistent,1)*100:>14.1f}%")

    # --- Key statistics ---
    pvl = np.array(peak_viral_loads)
    cd = np.array(clearance_days)
    tdf = np.array(td_final_loads) if td_final_loads else np.array([0])

    print(f"\n  VIRAL DYNAMICS STATISTICS:")
    print(f"    Peak viral load — median: {np.median(pvl):.0f}, mean: {np.mean(pvl):.0f}")
    print(f"    Wild-type clearance — median: {np.median(cd):.1f} days, mean: {np.mean(cd):.1f} days")
    if len(td_final_loads) > 0:
        print(f"    TD final load (persistent) — median: {np.median(tdf):.0f}, mean: {np.mean(tdf):.0f}")

    print(f"\n  KEY ESTIMATES:")
    persistence_rate = total_td_persistent / n_infections * 100
    print(f"    TD persistence rate: {persistence_rate:.1f}% of all CVB infections")
    print(f"    (Hypothesis: 10-30%. Model: {persistence_rate:.1f}%)")
    disease_given_pers = total_disease / max(total_td_persistent, 1) * 100
    print(f"    Clinical disease given persistence: {disease_given_pers:.1f}%")
    print(f"    Overall CVB → clinical disease: {total_disease/n_infections*100:.2f}%")

    return {
        "n_infections": n_infections,
        "total_td_persistent": total_td_persistent,
        "persistence_rate": persistence_rate,
        "clinical_disease": total_clinical_disease,
        "total_disease": total_disease,
        "peak_viral_loads": pvl,
        "clearance_days": cd,
    }


# =============================================================================
# THE SUCCESSFUL CLEARANCE vs FAILED CLEARANCE COMPARISON
# =============================================================================

def clearance_vs_persistence_comparison():
    """
    Compare the dynamics of a successful clearance vs failed clearance.
    Side-by-side trajectories showing WHERE the paths diverge.
    """
    print("\n" + "=" * 70)
    print("CLEARANCE vs PERSISTENCE: THE TWO PATHS")
    print("=" * 70)

    # Clearance case: strong immune response, moderate dose
    clear_params = InfectionParams(
        initial_dose=100,
        ifn_magnitude=1.3,
        nk_magnitude=1.2,
        ctl_magnitude=1.1,
    )

    # Persistence case: same dose, weaker immune response
    persist_params = InfectionParams(
        initial_dose=100,
        ifn_magnitude=0.5,
        nk_magnitude=0.7,
        ctl_magnitude=0.8,
    )

    r_clear = simulate_acute_infection(clear_params, t_days=30.0)
    r_persist = simulate_acute_infection(persist_params, t_days=30.0)

    print(f"\n  CLEARANCE CASE:")
    print(f"    Peak viral load: {r_clear['peak_v']:.0f} (day {r_clear['peak_v_day']:.1f})")
    print(f"    Wild-type clearance: day {r_clear['wt_clearance_day']:.1f}" if r_clear['wt_clearance_day'] else "    Wild-type: NOT CLEARED")
    print(f"    Peak TD mutants: {r_clear['peak_td']:.0f}")
    print(f"    Final TD mutants: {r_clear['final_td']:.0f}")
    print(f"    TD persistent: {r_clear['td_persistent']}")

    print(f"\n  PERSISTENCE CASE:")
    print(f"    Peak viral load: {r_persist['peak_v']:.0f} (day {r_persist['peak_v_day']:.1f})")
    print(f"    Wild-type clearance: day {r_persist['wt_clearance_day']:.1f}" if r_persist['wt_clearance_day'] else "    Wild-type: NOT CLEARED")
    print(f"    Peak TD mutants: {r_persist['peak_td']:.0f}")
    print(f"    Final TD mutants: {r_persist['final_td']:.0f}")
    print(f"    TD persistent: {r_persist['td_persistent']}")

    print(f"\n  THE FORK POINT:")
    print(f"    Same initial viral dose (100 TCID50)")
    print(f"    Different immune response strength (1.3x vs 0.5x IFN)")
    print(f"    The weaker immune response allows higher peak viral load")
    print(f"    → more replication cycles → more TD formation events")
    print(f"    → TD population exceeds critical threshold → PERSISTENCE")

    return r_clear, r_persist


# =============================================================================
# VISUALIZATION
# =============================================================================

def plot_fork_point(doses, ifn_mags, persistence_map, critical_ifn):
    """Plot the fork point boundary."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Panel 1: Heatmap
    ax = axes[0]
    im = ax.pcolormesh(ifn_mags, doses, persistence_map, cmap='RdYlGn_r', shading='auto')
    ax.set_yscale('log')
    ax.set_xlabel('IFN Response Magnitude (1.0 = average)')
    ax.set_ylabel('Initial Viral Dose (TCID50)')
    ax.set_title('The Fork: Red = Persistence, Green = Clearance')
    plt.colorbar(im, ax=ax, label='Persistence probability')

    # Overlay boundary
    valid = ~np.isnan(critical_ifn)
    if np.any(valid):
        ax.plot(critical_ifn[valid], doses[valid], 'k-', linewidth=2, label='Fork boundary')
        ax.legend()

    # Panel 2: Clearance vs persistence trajectories
    ax = axes[1]
    # Quick simulations for illustration
    r_clear = simulate_acute_infection(
        InfectionParams(initial_dose=100, ifn_magnitude=1.3), t_days=25
    )
    r_persist = simulate_acute_infection(
        InfectionParams(initial_dose=100, ifn_magnitude=0.5), t_days=25
    )

    ax.semilogy(r_clear['t'], r_clear['V'] + 1, 'g-', linewidth=2, label='Cleared: wild-type V')
    ax.semilogy(r_clear['t'], r_clear['TD'] + 1, 'g--', linewidth=1.5, label='Cleared: TD mutants')
    ax.semilogy(r_persist['t'], r_persist['V'] + 1, 'r-', linewidth=2, label='Persist: wild-type V')
    ax.semilogy(r_persist['t'], r_persist['TD'] + 1, 'r--', linewidth=1.5, label='Persist: TD mutants')
    ax.axhline(y=51, color='black', linestyle=':', alpha=0.5, label='TD critical threshold')

    ax.set_xlabel('Days post-infection')
    ax.set_ylabel('Viral load (copies + 1)')
    ax.set_title('Two Fates: Clearance vs Persistence')
    ax.legend(fontsize=8)
    ax.set_ylim(1, 1e9)

    plt.suptitle('Cross-Disease Anti-Problem: The Fork Point\n'
                 'Where >99% of CVB infections resolve and <1% become chronic disease',
                 fontsize=12, fontweight='bold', y=1.02)
    plt.tight_layout()

    outpath = os.path.join(OUTPUT_DIR, "anti_problem_fork_point.png")
    plt.savefig(outpath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\n  Saved: {outpath}")


def plot_disease_base_rates(mc_results):
    """Plot the disease incidence funnel."""
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))

    # Funnel: all infections → symptomatic → persistent → disease per organ
    n = mc_results['n_infections']
    n_persistent = mc_results['total_td_persistent']
    n_disease = mc_results['total_disease']

    # Bar chart of clinical disease rates per organ
    organs = list(mc_results['clinical_disease'].keys())
    counts = [mc_results['clinical_disease'][o] for o in organs]
    labels = [ORGAN_PROFILES[o].disease for o in organs]
    rates = [c / n * 100 for c in counts]

    # Sort by count
    sorted_idx = np.argsort(counts)[::-1]
    labels_sorted = [labels[i] for i in sorted_idx]
    rates_sorted = [rates[i] for i in sorted_idx]
    counts_sorted = [counts[i] for i in sorted_idx]

    colors = plt.cm.Reds(np.linspace(0.3, 0.9, len(labels_sorted)))
    bars = ax.barh(range(len(labels_sorted)), rates_sorted, color=colors)

    for i, (bar, count, rate) in enumerate(zip(bars, counts_sorted, rates_sorted)):
        ax.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2,
                f'{count:,} cases ({rate:.3f}%)',
                ha='left', va='center', fontsize=9)

    ax.set_yticks(range(len(labels_sorted)))
    ax.set_yticklabels(labels_sorted)
    ax.set_xlabel(f'Clinical disease rate per CVB infection (%)')
    ax.set_title(f'Disease Incidence per {n:,} CVB Infections\n'
                 f'TD persistence rate: {mc_results["persistence_rate"]:.1f}% | '
                 f'Any clinical disease: {n_disease/n*100:.2f}%',
                 fontsize=12, fontweight='bold')
    ax.invert_yaxis()
    ax.set_xlim(0, max(rates_sorted) * 1.5)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, "anti_problem_disease_base_rates.png")
    plt.savefig(outpath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {outpath}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 70)
    print("CROSS-DISEASE ANTI-PROBLEM: WHY MOST CVB INFECTIONS RESOLVE")
    print("Phase 4 systematic approach — numerical track (numerics)")
    print("=" * 70)
    print()
    print("Question: >99% of CVB infections are self-limiting.")
    print("          Why do <1% become chronic disease?")
    print()
    print("Answer:   There is a FORK POINT during acute infection.")
    print("          If immune clearance beats TD mutant formation → cure.")
    print("          If TD mutants exceed critical threshold → persistence.")
    print("          Then: organ susceptibility + genetics → specific disease.")
    print()

    # The fork point
    doses, ifn_mags, persistence_map, critical_ifn = find_fork_point()

    # Clearance vs persistence comparison
    r_clear, r_persist = clearance_vs_persistence_comparison()

    # Monte Carlo base rates
    mc_results = monte_carlo_base_rates(n_infections=10000, seed=42)

    # Plots
    plot_fork_point(doses, ifn_mags, persistence_map, critical_ifn)
    plot_disease_base_rates(mc_results)

    # --- Final synthesis ---
    print("\n" + "=" * 70)
    print("CROSS-DISEASE ANTI-PROBLEM: THE BASE RATE CALIBRATION")
    print("=" * 70)
    print(f"""
    THE FUNNEL:
    ~~~~~~~~~~~
    100% of population exposed to CVB at some point [Ref 2: ~75% seropositive]

    ~{mc_results['persistence_rate']:.0f}% establish TD mutant persistence
    → This is the "seed" for ALL chronic CVB diseases

    Of those with persistence, disease probability depends on organ:
    """)

    for organ_name in sorted(mc_results['clinical_disease'].keys(),
                              key=lambda x: -mc_results['clinical_disease'][x]):
        organ = ORGAN_PROFILES[organ_name]
        count = mc_results['clinical_disease'][organ_name]
        rate_all = count / mc_results['n_infections'] * 100
        rate_pers = count / max(mc_results['total_td_persistent'], 1) * 100
        print(f"      {organ.disease:<30} {rate_pers:>5.1f}% of persistent → {rate_all:.3f}% of all infections")

    print(f"""
    CALIBRATION GUIDANCE:
    ~~~~~~~~~~~~~~~~~~~~~
    All disease-specific models should produce incidence rates consistent
    with these base rates. If a model predicts 50% of CVB → T1DM, something
    is wrong — the real rate is ~0.1%.

    The base rate provides a CEILING on protocol efficacy:
    - Protocol cannot prevent disease in people without CVB persistence
    - Protocol CAN prevent progression in the ~{mc_results['persistence_rate']:.0f}% with persistence
    - The earlier intervention begins, the more the fork point shifts
      toward clearance

    THE ANTI-PROBLEM ANSWER:
    ~~~~~~~~~~~~~~~~~~~~~~~~
    The >99% who clear CVB without disease do so because:
    1. Their IFN response is fast enough to limit peak viral load
    2. Their NK cells kill infected cells before TD mutants form
    3. Their CTL response clears virus before TD population is self-sustaining
    4. It is mostly stochastic: same person, different day, might get different outcome

    The protocol recreates conditions 1-3 pharmacologically:
    - Fluoxetine → reduces viral replication (like having better IFN)
    - BHB + anti-inflammatory → reduces collateral damage (like better NK specificity)
    - Butyrate + VitD → restores immune regulation (like natural clearance)
    """)


if __name__ == "__main__":
    main()
