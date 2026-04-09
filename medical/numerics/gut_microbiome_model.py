#!/usr/bin/env python3
"""
Gut Microbiome-Butyrate-Treg Axis Model
=========================================

Models WHERE butyrate comes from and HOW to optimize it for the T1DM protocol.

The pipeline:
    Dietary fiber  -->  Fermented by Firmicutes  -->  Butyrate (colonic)
    Butyrate  -->  Feeds colonocytes (70% energy)  -->  Gut barrier integrity
    Butyrate  -->  Portal vein  -->  Systemic (first-pass depletes ~90%)
    Systemic butyrate  -->  HDAC inhibition  -->  FoxP3+ Treg induction

T1DM gut dysbiosis (well-documented):
    - Reduced Firmicutes:Bacteroidetes ratio
    - Lower butyrate-producing species (F. prausnitzii, Roseburia, Eubacterium)
    - Lower colonic butyrate -> lower systemic butyrate -> fewer Tregs
    - CVB infects gut epithelium -> barrier disruption -> "leaky gut"

State variables (7 coupled ODEs):
    Fp  = butyrate-producing Firmicutes fraction (F. prausnitzii, Roseburia,
          Eubacterium rectale, Clostridium clusters IV/XIVa) [0-1]
    Bd  = Bacteroidetes fraction (compete for niche) [0-1]
    Bc  = colonic butyrate concentration (mM)
    Bs  = systemic butyrate concentration (uM, portal -> hepatic first-pass)
    Bi  = gut barrier integrity (0 = destroyed, 1 = healthy)
    Treg = FoxP3+ regulatory T cells (cells/uL blood)
    Teff = autoreactive T effector cells (cells/uL blood)

Interventions:
    1. High-fiber diet (30g/day): feeds butyrate producers
    2. Fermented foods (kimchi, sauerkraut, kefir): diverse microbiome seeding
    3. Sodium butyrate supplement (600mg/day): direct systemic bypass
    4. Probiotic (F. prausnitzii-containing): recolonize depleted species

Four scenarios compared:
    (a) T1DM dysbiotic baseline: low fiber, no intervention
    (b) High fiber + fermented foods
    (c) High fiber + fermented foods + sodium butyrate 600mg/day
    (d) Full protocol: (c) + F. prausnitzii probiotic

Literature:
    [1]  Furusawa Y et al. Nature 2013;504:446-450 — butyrate -> colonic Tregs
    [2]  Arpaia N et al. Nature 2013;504:451-455 — butyrate -> FoxP3 via CNS1
    [3]  Smith PM et al. Science 2013;341:569-573 — SCFAs regulate colonic Tregs
    [4]  Marino E et al. Nat Immunol 2017;18:552-562 — butyrate protects NOD mice
    [5]  de Goffau MC et al. Diabetologia 2013;56:1783-1791 — T1DM gut dysbiosis
    [6]  Giongo A et al. ISME J 2011;5:82-91 — T1DM microbiome shifts
    [7]  Brown CT et al. PLoS ONE 2011;6:e25792 — Firmicutes depletion in T1DM
    [8]  Cummings JH et al. Gut 1987;28:1221-1227 — colonic SCFA concentrations
    [9]  Hamer HM et al. Aliment Pharmacol Ther 2008;27:104-119 — butyrate review
    [10] Sokol H et al. PNAS 2008;105:16731-16736 — F. prausnitzii anti-inflammatory
    [11] Riviere A et al. Front Microbiol 2016;7:979 — fiber -> butyrate pathways
    [12] David LA et al. Nature 2014;505:559-563 — diet reshapes gut in 24h
    [13] Donaldson GP et al. Nat Rev Microbiol 2016;14:20-32 — gut barrier biology
    [14] Peng L et al. J Nutr 2009;139:1619-1625 — butyrate upregulates tight junctions
    [15] Coppieters KT et al. J Exp Med 2012;209:51-60 — T1DM gut CVB reservoir

systematic approach — Gut Microbiome Model — ODD Instance (numerics)
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import os
import sys
from dataclasses import dataclass, field
from typing import Dict, Optional, Tuple, List
import warnings
warnings.filterwarnings('ignore')

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "figures")
os.makedirs(OUTPUT_DIR, exist_ok=True)


# =============================================================================
# PARAMETER DATACLASS
# =============================================================================

@dataclass
class GutMicrobiomeParams:
    """
    All biological parameters for the 7-state gut microbiome ODE system.

    Defaults calibrated to a T1DM patient with documented dysbiosis.
    """

    # --- Microbiome composition ---
    # Healthy: Firmicutes ~60-80%, Bacteroidetes ~20-30% (Human Microbiome Project)
    # T1DM dysbiotic: Firmicutes ~30-40%, Bacteroidetes ~40-50% [5,6,7]
    Fp_initial_healthy: float = 0.25          # butyrate-producer fraction (of total community)
    Fp_initial_dysbiotic: float = 0.08        # T1DM patient: severely depleted [5,6]
    Bd_initial_healthy: float = 0.30          # Bacteroidetes fraction
    Bd_initial_dysbiotic: float = 0.45        # T1DM: expanded Bacteroidetes [6]

    # Firmicutes growth parameters
    Fp_max_growth_rate: float = 0.12          # /day, maximum growth rate on fiber
    Fp_fiber_half_saturation: float = 12.0    # g/day fiber for half-max growth
    Fp_carrying_capacity: float = 0.35        # max fraction achievable
    Fp_death_rate: float = 0.03              # /day, basal turnover
    Fp_probiotic_seeding: float = 0.003       # /day, exogenous F. prausnitzii input

    # Bacteroidetes parameters
    Bd_growth_rate: float = 0.08              # /day, baseline (less fiber-dependent)
    Bd_carrying_capacity: float = 0.55        # max fraction
    Bd_death_rate: float = 0.03              # /day
    Bd_competition_from_Fp: float = 0.08      # competition coefficient (weak)

    # --- Butyrate production ---
    # Colonic butyrate: healthy = 10-20 mM, T1DM ~ 3-8 mM [8,9]
    butyrate_production_per_Fp: float = 80.0  # mM per unit Fp fraction per day
    butyrate_production_per_fiber: float = 0.4  # mM per g fiber (baseline, modulated by Fp)
    butyrate_colonocyte_uptake: float = 0.70  # fraction consumed by colonocytes (70%) [9]
    butyrate_colonic_decay: float = 0.8       # /day, first-order decay constant
    butyrate_colonic_healthy: float = 15.0    # mM, healthy reference

    # --- Systemic butyrate (portal -> hepatic first-pass) ---
    # Only ~5-10% of colonic butyrate reaches systemic circulation
    # Hepatic first-pass metabolism extracts ~90% [9]
    portal_absorption_rate: float = 0.10      # fraction of colonic butyrate absorbed to portal
    hepatic_extraction: float = 0.90          # fraction removed by liver
    systemic_butyrate_clearance: float = 8.0  # /day, renal + tissue uptake
    systemic_butyrate_healthy: float = 5.0    # uM, healthy reference [9]

    # Exogenous sodium butyrate supplement
    # 600mg sodium butyrate -> ~500mg butyric acid -> ~5.7 mmol
    # Bioavailability ~20-30% (enteric-coated reaches colon)
    supplement_dose_mmol: float = 5.7         # mmol per 600mg dose
    supplement_bioavailability: float = 0.25  # fraction reaching systemic circulation
    supplement_doses_per_day: float = 2.0     # BID dosing

    # --- Gut barrier integrity ---
    barrier_healthy: float = 1.0
    barrier_dysbiotic: float = 0.55           # T1DM: documented increased permeability
    barrier_repair_rate_butyrate: float = 0.005  # /day per mM colonic butyrate (above threshold)
    barrier_butyrate_threshold: float = 8.0   # mM, minimum for net barrier repair
    barrier_decay_rate: float = 0.005         # /day, baseline damage (slow)
    barrier_cvb_damage_rate: float = 0.008    # /day per unit gut CVB load (lower: chronic, not acute)

    # Tight junction proteins: claudin-1, occludin, ZO-1
    # Butyrate upregulates via HDAC inhibition of promoters [14]
    tight_junction_upregulation_rate: float = 0.03  # /day per mM butyrate above threshold

    # --- Treg induction ---
    # From cert_005: butyrate 2-3 fold increase in colonic Tregs [1,2,3]
    # NOD mice: 30% T1DM with SCFA diet vs 80% controls [4]
    Treg_initial_healthy: float = 180.0       # cells/uL (healthy adult ~150-300)
    Treg_initial_t1dm: float = 90.0           # cells/uL (T1DM: ~50% of normal)
    Treg_homeostatic_rate: float = 0.005      # /day, thymic output + peripheral expansion
    Treg_butyrate_induction: float = 0.08     # /day per uM systemic butyrate
    Treg_half_saturation_butyrate: float = 3.0  # uM systemic butyrate for half-max effect
    Treg_max: float = 350.0                   # cells/uL, ceiling
    Treg_death_rate: float = 0.015            # /day, natural turnover

    # --- T effector (autoreactive) ---
    Teff_initial_t1dm: float = 45.0           # cells/uL, elevated in T1DM
    Teff_initial_healthy: float = 15.0        # cells/uL
    Teff_antigen_driven_expansion: float = 0.02  # /day, driven by gut permeability
    Teff_contraction_rate: float = 0.01       # /day, natural contraction
    Teff_suppression_by_Treg: float = 0.0003  # /day per Treg cell
    Teff_max: float = 120.0                   # cells/uL

    # --- Autoimmune attack rate (output metric) ---
    # Beta cell destruction rate ~ Teff * (1 - Treg_suppression)
    autoimmune_attack_base: float = 0.001     # fraction beta cells/day per Teff
    treg_suppression_hill_n: float = 2.0      # Hill coefficient for Treg suppression
    treg_suppression_ec50: float = 150.0      # Treg cells/uL for 50% suppression

    # --- Dietary parameters ---
    fiber_western_diet: float = 12.0          # g/day, average American/Western
    fiber_high_diet: float = 35.0             # g/day, intentional high-fiber
    fiber_fermented_food_equivalent: float = 5.0  # g/day additional from fermented foods

    # --- Timeline parameters ---
    # Literature: dietary shift -> microbiome change in 24-72h [12]
    # Stable recolonization: 3-6 months
    # Treg expansion: 2-4 weeks after butyrate rise
    dietary_response_lag: float = 3.0         # days for microbiome to begin responding
    microbiome_stabilization_time: float = 120.0  # days for stable new composition


# =============================================================================
# INTERVENTION SCENARIOS
# =============================================================================

@dataclass
class InterventionScenario:
    """Defines what interventions are active and when they start."""
    name: str = "baseline"
    fiber_intake: float = 12.0        # g/day
    fermented_foods: bool = False      # adds fiber + diversity
    butyrate_supplement: bool = False   # sodium butyrate 600mg/day
    probiotic: bool = False            # F. prausnitzii-containing
    gut_cvb_load: float = 0.3         # normalized (0-1), T1DM patient with gut persistence

    # Timing
    intervention_start_day: float = 0.0  # when dietary changes begin


def make_scenarios() -> List[InterventionScenario]:
    """Create the four comparison scenarios."""
    return [
        InterventionScenario(
            name="(a) T1DM dysbiotic baseline",
            fiber_intake=12.0,
            fermented_foods=False,
            butyrate_supplement=False,
            probiotic=False,
            gut_cvb_load=0.3,
        ),
        InterventionScenario(
            name="(b) High fiber + fermented foods",
            fiber_intake=35.0,
            fermented_foods=True,
            butyrate_supplement=False,
            probiotic=False,
            gut_cvb_load=0.3,
        ),
        InterventionScenario(
            name="(c) High fiber + fermented + butyrate",
            fiber_intake=35.0,
            fermented_foods=True,
            butyrate_supplement=True,
            probiotic=False,
            gut_cvb_load=0.3,
        ),
        InterventionScenario(
            name="(d) Full protocol + probiotic",
            fiber_intake=35.0,
            fermented_foods=True,
            butyrate_supplement=True,
            probiotic=True,
            gut_cvb_load=0.3,
        ),
    ]


# =============================================================================
# ODE SYSTEM
# =============================================================================

def gut_microbiome_odes(t, y, params: GutMicrobiomeParams, scenario: InterventionScenario):
    """
    7-state ODE system for gut microbiome-butyrate-Treg axis.

    State vector y = [Fp, Bd, Bc, Bs, Bi, Treg, Teff]
        Fp   = butyrate-producing Firmicutes fraction [0, Fp_carrying_capacity]
        Bd   = Bacteroidetes fraction [0, Bd_carrying_capacity]
        Bc   = colonic butyrate concentration (mM) [0, ~25]
        Bs   = systemic butyrate concentration (uM) [0, ~20]
        Bi   = gut barrier integrity [0, 1]
        Treg = FoxP3+ Treg cells/uL [0, Treg_max]
        Teff = autoreactive T effector cells/uL [0, Teff_max]
    """
    Fp, Bd, Bc, Bs, Bi, Treg, Teff = y
    p = params
    sc = scenario

    # Clamp to physical bounds
    Fp = max(Fp, 0.001)
    Bd = max(Bd, 0.001)
    Bc = max(Bc, 0.0)
    Bs = max(Bs, 0.0)
    Bi = np.clip(Bi, 0.0, 1.0)
    Treg = max(Treg, 1.0)
    Teff = max(Teff, 1.0)

    # --- Determine effective fiber and interventions ---
    # After intervention start, dietary parameters shift
    if t >= sc.intervention_start_day:
        # Smooth ramp-up over dietary_response_lag days
        ramp = min(1.0, (t - sc.intervention_start_day) / max(p.dietary_response_lag, 1.0))
        fiber = p.fiber_western_diet + ramp * (sc.fiber_intake - p.fiber_western_diet)
        fermented_boost = ramp * p.fiber_fermented_food_equivalent if sc.fermented_foods else 0.0
        total_fiber = fiber + fermented_boost
        probiotic_active = sc.probiotic
        supplement_active = sc.butyrate_supplement
    else:
        total_fiber = p.fiber_western_diet
        probiotic_active = False
        supplement_active = False

    # --- (1) Firmicutes (butyrate producers) dynamics ---
    # Growth: Monod kinetics on fiber
    fiber_factor = total_fiber / (total_fiber + p.Fp_fiber_half_saturation)
    Fp_growth = p.Fp_max_growth_rate * fiber_factor
    # Logistic ceiling: carrying capacity depends on fiber availability
    # Low fiber -> low carrying capacity; high fiber -> full carrying capacity
    effective_carrying_cap = 0.05 + (p.Fp_carrying_capacity - 0.05) * fiber_factor
    Fp_logistic = 1.0 - Fp / effective_carrying_cap
    # Probiotic seeding
    Fp_seed = p.Fp_probiotic_seeding if probiotic_active else 0.0
    # Fermented foods provide some diversity seeding (smaller than probiotic)
    Fp_fermented_seed = 0.001 * ramp if (sc.fermented_foods and t >= sc.intervention_start_day) else 0.0

    dFp = Fp * (Fp_growth * Fp_logistic - p.Fp_death_rate) + Fp_seed + Fp_fermented_seed

    # --- (2) Bacteroidetes dynamics ---
    # Bacteroidetes are weakly fiber-dependent; they grow on many substrates
    # As Firmicutes expand, Bacteroidetes contract slightly (competitive exclusion)
    Bd_equilibrium = p.Bd_carrying_capacity - 0.4 * Fp  # Fp expansion compresses Bd niche
    Bd_equilibrium = max(Bd_equilibrium, 0.20)  # floor
    dBd = 0.03 * (Bd_equilibrium - Bd)  # slow relaxation toward equilibrium

    # --- (3) Colonic butyrate ---
    # Production: depends on Fp fraction AND fiber availability
    production = p.butyrate_production_per_Fp * Fp * (total_fiber / (total_fiber + p.Fp_fiber_half_saturation))
    # Total colonic loss: colonocyte uptake (70%) + portal absorption (10%) + stool (20%)
    # Model as single first-order clearance with rate constant
    colonic_clearance = p.butyrate_colonic_decay * Bc

    dBc = production - colonic_clearance

    # --- (4) Systemic butyrate ---
    # From colonic absorption: ~10% of colonic butyrate enters portal vein,
    # liver extracts ~90% (first-pass), so systemic = Bc * 0.10 * 0.10 = 1% of colonic
    # But units: Bc is mM in ~0.5L colon volume; systemic is uM in ~15L blood volume
    # Flux: Bc(mM) * 0.5L * 0.10(portal) * 0.10(survive liver) = mmol/day
    # -> uM: mmol / 15L * 1e3 = uM
    # Simplify: systemic input = absorption_constant * Bc
    gut_to_systemic = p.portal_absorption_rate * (1.0 - p.hepatic_extraction) * Bc * 1000.0 * 0.5 / 15.0
    # = 0.10 * 0.10 * Bc * 33.3 = 0.333 * Bc  uM/day per mM colonic

    # From supplement: direct systemic delivery
    supplement_systemic = 0.0
    if supplement_active:
        # 600mg sodium butyrate BID, systemic bioavailability ~10% (enteric-coated,
        # some absorbed pre-hepatically, some escapes first-pass)
        # 5.7 mmol * 2 doses * 0.10 / 15L * 1e3 = ~76 uM/day input
        # But clearance is fast (t1/2 ~6 min), so steady-state = input/clearance
        supplement_systemic = p.supplement_dose_mmol * p.supplement_doses_per_day * 0.10 * 1000.0 / 15.0

    systemic_clearance = p.systemic_butyrate_clearance * Bs

    dBs = gut_to_systemic + supplement_systemic - systemic_clearance

    # --- (5) Gut barrier integrity ---
    # Baseline epithelial repair: gut renews every 3-5 days, but barrier requires
    # butyrate for tight junction maintenance; without butyrate, barrier is suboptimal
    baseline_repair = 0.005 * (1.0 - Bi)  # very slow without butyrate
    # Butyrate-enhanced repair: upregulates claudin-1, occludin, ZO-1 [14]
    butyrate_repair = p.barrier_repair_rate_butyrate * max(Bc - p.barrier_butyrate_threshold, 0.0) * (1.0 - Bi)
    # CVB damages barrier (saturating: damage plateaus at high viral load)
    cvb_damage = p.barrier_cvb_damage_rate * sc.gut_cvb_load * Bi
    # Butyrate-deficiency stress: low butyrate = starved colonocytes = barrier degrades
    butyrate_deficiency = 0.005 * max(p.barrier_butyrate_threshold - Bc, 0.0) / p.barrier_butyrate_threshold * Bi

    dBi = baseline_repair + butyrate_repair - cvb_damage - butyrate_deficiency

    # --- (6) Treg dynamics ---
    # Homeostatic production (thymic + peripheral)
    Treg_homeostasis = p.Treg_homeostatic_rate * (p.Treg_initial_healthy - Treg)
    # Butyrate-induced: HDAC inhibition -> FoxP3 locus hyperacetylation [1,2,3]
    # Michaelis-Menten on systemic butyrate
    butyrate_induction = (p.Treg_butyrate_induction * Bs /
                          (Bs + p.Treg_half_saturation_butyrate)) * (p.Treg_max - Treg)
    # Death
    Treg_death = p.Treg_death_rate * Treg

    dTreg = Treg_homeostasis + butyrate_induction - Treg_death

    # --- (7) T effector (autoreactive) dynamics ---
    # Antigen-driven expansion: gut permeability drives systemic antigen exposure
    gut_permeability = 1.0 - Bi  # higher when barrier is damaged
    # Homeostatic term: Teff has a set-point driven by antigen exposure
    # More permeable gut = higher set-point; Tregs lower it
    Teff_setpoint = 15.0 + 40.0 * gut_permeability  # 15 at healthy barrier, 55 at fully permeable
    # Treg suppression lowers the effective set-point
    treg_suppression_factor = 1.0 / (1.0 + p.Teff_suppression_by_Treg * Treg)
    effective_setpoint = Teff_setpoint * treg_suppression_factor
    # Relaxation toward set-point
    dTeff = 0.02 * (effective_setpoint - Teff)

    return [dFp, dBd, dBc, dBs, dBi, dTreg, dTeff]


# =============================================================================
# DERIVED METRICS
# =============================================================================

def compute_autoimmune_attack_rate(Treg, Teff, params: GutMicrobiomeParams):
    """
    Compute relative autoimmune attack rate on beta cells.

    Attack = Teff_activity * (1 - Treg_suppression)
    Treg suppression follows Hill kinetics: S = Treg^n / (EC50^n + Treg^n)
    """
    p = params
    Treg_suppression = Treg**p.treg_suppression_hill_n / (
        p.treg_suppression_ec50**p.treg_suppression_hill_n + Treg**p.treg_suppression_hill_n
    )
    attack_rate = p.autoimmune_attack_base * Teff * (1.0 - Treg_suppression)
    return attack_rate, Treg_suppression


def compute_firmicutes_bacteroidetes_ratio(Fp, Bd):
    """F:B ratio, a standard clinical microbiome metric."""
    # Fp is butyrate-producers only (~40% of total Firmicutes)
    # Total Firmicutes ~ Fp / 0.4
    total_firmicutes = Fp / 0.4
    return total_firmicutes / max(Bd, 0.01)


# =============================================================================
# SIMULATION RUNNER
# =============================================================================

def run_scenario(scenario: InterventionScenario, params: GutMicrobiomeParams = None,
                 t_months: float = 12.0) -> Dict:
    """
    Run the gut microbiome model for a single scenario.

    Returns dict with time arrays and all state trajectories.
    """
    if params is None:
        params = GutMicrobiomeParams()

    t_days = t_months * 30.0
    t_span = (0, t_days)
    t_eval = np.linspace(0, t_days, int(t_days) + 1)

    # Initial conditions: T1DM dysbiotic patient
    y0 = [
        params.Fp_initial_dysbiotic,    # Fp: depleted butyrate producers
        params.Bd_initial_dysbiotic,     # Bd: expanded Bacteroidetes
        4.0,                              # Bc: low colonic butyrate (mM)
        1.5,                              # Bs: low systemic butyrate (uM)
        params.barrier_dysbiotic,        # Bi: compromised barrier
        params.Treg_initial_t1dm,        # Treg: depressed
        params.Teff_initial_t1dm,        # Teff: elevated
    ]

    sol = solve_ivp(
        gut_microbiome_odes,
        t_span,
        y0,
        args=(params, scenario),
        method='RK45',
        t_eval=t_eval,
        max_step=0.5,
        rtol=1e-8,
        atol=1e-10,
    )

    if not sol.success:
        print(f"WARNING: Integration failed for {scenario.name}: {sol.message}")

    # Compute derived metrics
    Fp_traj = sol.y[0]
    Bd_traj = sol.y[1]
    Bc_traj = sol.y[2]
    Bs_traj = sol.y[3]
    Bi_traj = sol.y[4]
    Treg_traj = sol.y[5]
    Teff_traj = sol.y[6]

    # Autoimmune attack rate over time
    attack_rates = []
    suppression_rates = []
    fb_ratios = []
    for i in range(len(sol.t)):
        attack, supp = compute_autoimmune_attack_rate(Treg_traj[i], Teff_traj[i], params)
        attack_rates.append(attack)
        suppression_rates.append(supp)
        fb_ratios.append(compute_firmicutes_bacteroidetes_ratio(Fp_traj[i], Bd_traj[i]))

    return {
        'name': scenario.name,
        't_days': sol.t,
        't_months': sol.t / 30.0,
        'Fp': Fp_traj,
        'Bd': Bd_traj,
        'Bc': Bc_traj,
        'Bs': Bs_traj,
        'Bi': Bi_traj,
        'Treg': Treg_traj,
        'Teff': Teff_traj,
        'attack_rate': np.array(attack_rates),
        'suppression': np.array(suppression_rates),
        'fb_ratio': np.array(fb_ratios),
    }


# =============================================================================
# MICROBIOME RESTORATION TIMELINE
# =============================================================================

def estimate_restoration_timeline(result: Dict) -> Dict:
    """
    Estimate key milestones in microbiome restoration.

    Literature benchmarks:
        - Microbiome composition shift: 24-72 hours [12]
        - Butyrate increase measurable: 1-2 weeks
        - Treg expansion detectable: 2-4 weeks
        - Stable recolonization: 3-6 months
        - Gut barrier normalization: 4-8 weeks with butyrate
    """
    t = result['t_days']

    milestones = {}

    # When does F:B ratio reach 1.0 (healthy threshold)?
    fb = result['fb_ratio']
    fb_crossings = np.where(fb >= 1.0)[0]
    milestones['fb_ratio_normal'] = t[fb_crossings[0]] if len(fb_crossings) > 0 else None

    # When does colonic butyrate reach 10 mM (lower bound of healthy)?
    bc = result['Bc']
    bc_crossings = np.where(bc >= 10.0)[0]
    milestones['colonic_butyrate_10mM'] = t[bc_crossings[0]] if len(bc_crossings) > 0 else None

    # When does systemic butyrate reach 3 uM (Treg-inducing threshold)?
    bs = result['Bs']
    bs_crossings = np.where(bs >= 3.0)[0]
    milestones['systemic_butyrate_3uM'] = t[bs_crossings[0]] if len(bs_crossings) > 0 else None

    # When does Treg count reach 150 (lower normal)?
    treg = result['Treg']
    treg_crossings = np.where(treg >= 150.0)[0]
    milestones['treg_normal'] = t[treg_crossings[0]] if len(treg_crossings) > 0 else None

    # When does gut barrier reach 0.8 (functional integrity)?
    bi = result['Bi']
    bi_crossings = np.where(bi >= 0.80)[0]
    milestones['barrier_functional'] = t[bi_crossings[0]] if len(bi_crossings) > 0 else None

    # When does autoimmune attack rate drop 50% from baseline?
    ar = result['attack_rate']
    if len(ar) > 0 and ar[0] > 0:
        ar_half = ar[0] * 0.5
        ar_crossings = np.where(ar <= ar_half)[0]
        milestones['attack_rate_halved'] = t[ar_crossings[0]] if len(ar_crossings) > 0 else None
    else:
        milestones['attack_rate_halved'] = None

    return milestones


# =============================================================================
# VISUALIZATION
# =============================================================================

def plot_all_scenarios(results: List[Dict], params: GutMicrobiomeParams):
    """Generate comprehensive 6-panel comparison figure."""

    colors = ['#d62728', '#ff7f0e', '#2ca02c', '#1f77b4']
    fig = plt.figure(figsize=(20, 24))
    gs = GridSpec(4, 2, hspace=0.35, wspace=0.3)

    # --- Panel 1: Butyrate-producing Firmicutes ---
    ax1 = fig.add_subplot(gs[0, 0])
    for i, r in enumerate(results):
        ax1.plot(r['t_months'], r['Fp'] * 100, color=colors[i], linewidth=2, label=r['name'])
    ax1.axhline(y=params.Fp_initial_healthy * 100, color='gray', linestyle='--', alpha=0.5, label='Healthy reference')
    ax1.set_xlabel('Time (months)')
    ax1.set_ylabel('Butyrate producers (% of community)')
    ax1.set_title('Butyrate-Producing Firmicutes\n(F. prausnitzii, Roseburia, Eubacterium)')
    ax1.legend(fontsize=7, loc='lower right')
    ax1.set_ylim(0, 40)
    ax1.grid(True, alpha=0.3)

    # --- Panel 2: Firmicutes:Bacteroidetes ratio ---
    ax2 = fig.add_subplot(gs[0, 1])
    for i, r in enumerate(results):
        ax2.plot(r['t_months'], r['fb_ratio'], color=colors[i], linewidth=2, label=r['name'])
    ax2.axhline(y=1.5, color='gray', linestyle='--', alpha=0.5, label='Healthy (F:B > 1.5)')
    ax2.axhline(y=1.0, color='gray', linestyle=':', alpha=0.3)
    ax2.set_xlabel('Time (months)')
    ax2.set_ylabel('F:B ratio')
    ax2.set_title('Firmicutes:Bacteroidetes Ratio\n(Clinical dysbiosis marker)')
    ax2.legend(fontsize=7, loc='lower right')
    ax2.grid(True, alpha=0.3)

    # --- Panel 3: Colonic butyrate ---
    ax3 = fig.add_subplot(gs[1, 0])
    for i, r in enumerate(results):
        ax3.plot(r['t_months'], r['Bc'], color=colors[i], linewidth=2, label=r['name'])
    ax3.axhspan(10, 20, alpha=0.1, color='green', label='Healthy range (10-20 mM)')
    ax3.set_xlabel('Time (months)')
    ax3.set_ylabel('Colonic butyrate (mM)')
    ax3.set_title('Colonic Butyrate Concentration\n(Drives colonocyte health + gut barrier)')
    ax3.legend(fontsize=7, loc='lower right')
    ax3.set_ylim(0, 25)
    ax3.grid(True, alpha=0.3)

    # --- Panel 4: Systemic butyrate ---
    ax4 = fig.add_subplot(gs[1, 1])
    for i, r in enumerate(results):
        ax4.plot(r['t_months'], r['Bs'], color=colors[i], linewidth=2, label=r['name'])
    ax4.axhspan(3, 8, alpha=0.1, color='green', label='Healthy range (3-8 uM)')
    ax4.axhline(y=0.5, color='red', linestyle=':', alpha=0.5, label='HDAC IC50 ~0.1-0.5 mM (100-500 uM)')
    ax4.set_xlabel('Time (months)')
    ax4.set_ylabel('Systemic butyrate (uM)')
    ax4.set_title('Systemic Butyrate\n(Portal vein -> hepatic first-pass -> HDAC inhibition)')
    ax4.legend(fontsize=7, loc='lower right')
    ax4.grid(True, alpha=0.3)

    # --- Panel 5: Treg count ---
    ax5 = fig.add_subplot(gs[2, 0])
    for i, r in enumerate(results):
        ax5.plot(r['t_months'], r['Treg'], color=colors[i], linewidth=2, label=r['name'])
    ax5.axhspan(150, 300, alpha=0.1, color='green', label='Healthy range (150-300 cells/uL)')
    ax5.set_xlabel('Time (months)')
    ax5.set_ylabel('FoxP3+ Treg (cells/uL)')
    ax5.set_title('Regulatory T Cells\n(Butyrate -> HDAC inhibition -> FoxP3 -> Treg differentiation)')
    ax5.legend(fontsize=7, loc='lower right')
    ax5.grid(True, alpha=0.3)

    # --- Panel 6: Gut barrier integrity ---
    ax6 = fig.add_subplot(gs[2, 1])
    for i, r in enumerate(results):
        ax6.plot(r['t_months'], r['Bi'], color=colors[i], linewidth=2, label=r['name'])
    ax6.axhline(y=0.85, color='gray', linestyle='--', alpha=0.5, label='Functional threshold')
    ax6.set_xlabel('Time (months)')
    ax6.set_ylabel('Barrier integrity (0-1)')
    ax6.set_title('Gut Barrier Integrity\n(Tight junctions: claudin-1, occludin, ZO-1)')
    ax6.legend(fontsize=7, loc='lower right')
    ax6.set_ylim(0, 1.05)
    ax6.grid(True, alpha=0.3)

    # --- Panel 7: Autoimmune attack rate ---
    ax7 = fig.add_subplot(gs[3, 0])
    for i, r in enumerate(results):
        # Normalize to baseline scenario at t=0
        baseline_attack = results[0]['attack_rate'][0] if results[0]['attack_rate'][0] > 0 else 1.0
        ax7.plot(r['t_months'], r['attack_rate'] / baseline_attack * 100,
                 color=colors[i], linewidth=2, label=r['name'])
    ax7.axhline(y=50, color='gray', linestyle=':', alpha=0.5, label='50% reduction threshold')
    ax7.set_xlabel('Time (months)')
    ax7.set_ylabel('Relative attack rate (%)')
    ax7.set_title('Autoimmune Attack Rate on Beta Cells\n(Teff activity * (1 - Treg suppression))')
    ax7.legend(fontsize=7, loc='upper right')
    ax7.grid(True, alpha=0.3)

    # --- Panel 8: Summary table ---
    ax8 = fig.add_subplot(gs[3, 1])
    ax8.axis('off')

    summary_text = "RESTORATION TIMELINE MILESTONES\n" + "=" * 45 + "\n\n"
    for i, r in enumerate(results):
        milestones = estimate_restoration_timeline(r)
        summary_text += f"{r['name']}\n"
        for key, val in milestones.items():
            if val is not None:
                summary_text += f"  {key}: day {val:.0f} ({val/30:.1f} months)\n"
            else:
                summary_text += f"  {key}: NOT REACHED in 12 months\n"
        # Final values
        summary_text += f"  Final Treg: {r['Treg'][-1]:.0f} cells/uL\n"
        summary_text += f"  Final colonic butyrate: {r['Bc'][-1]:.1f} mM\n"
        summary_text += f"  Final systemic butyrate: {r['Bs'][-1]:.2f} uM\n"
        summary_text += f"  Final barrier: {r['Bi'][-1]:.2f}\n"
        attack_pct = r['attack_rate'][-1] / max(results[0]['attack_rate'][0], 1e-10) * 100
        summary_text += f"  Final attack rate: {attack_pct:.1f}% of baseline\n\n"

    ax8.text(0.02, 0.98, summary_text, transform=ax8.transAxes,
             fontsize=8, fontfamily='monospace', verticalalignment='top')

    fig.suptitle('Gut Microbiome-Butyrate-Treg Axis: T1DM Protocol Optimization\n'
                 'systematic approach — ODD Instance (numerics)',
                 fontsize=14, fontweight='bold', y=0.98)

    plt.savefig(os.path.join(OUTPUT_DIR, 'gut_microbiome_butyrate_treg.png'),
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Figure saved: {os.path.join(OUTPUT_DIR, 'gut_microbiome_butyrate_treg.png')}")


def plot_microbiome_restoration_detail(results: List[Dict]):
    """Focused figure on microbiome restoration kinetics."""
    colors = ['#d62728', '#ff7f0e', '#2ca02c', '#1f77b4']

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: First 30 days — rapid dietary response
    ax = axes[0, 0]
    for i, r in enumerate(results):
        mask = r['t_days'] <= 30
        ax.plot(r['t_days'][mask], r['Fp'][mask] * 100, color=colors[i], linewidth=2, label=r['name'])
    ax.set_xlabel('Days')
    ax.set_ylabel('Butyrate producers (%)')
    ax.set_title('Early Response (first 30 days)\nDiet reshapes microbiome in 24-72h')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 2: Butyrate kinetics — how fast does butyrate rise?
    ax = axes[0, 1]
    for i, r in enumerate(results):
        mask = r['t_days'] <= 90
        ax.plot(r['t_days'][mask], r['Bs'][mask], color=colors[i], linewidth=2, label=r['name'])
    ax.set_xlabel('Days')
    ax.set_ylabel('Systemic butyrate (uM)')
    ax.set_title('Systemic Butyrate Rise (first 3 months)\nSupplement provides fastest boost')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 3: Treg expansion lag
    ax = axes[1, 0]
    for i, r in enumerate(results):
        mask = r['t_days'] <= 120
        ax.plot(r['t_days'][mask], r['Treg'][mask], color=colors[i], linewidth=2, label=r['name'])
    ax.axhline(y=150, color='gray', linestyle='--', alpha=0.5, label='Normal lower bound')
    ax.set_xlabel('Days')
    ax.set_ylabel('Treg (cells/uL)')
    ax.set_title('Treg Expansion (first 4 months)\nLag: 2-4 weeks after butyrate rise')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 4: Attack rate reduction
    ax = axes[1, 1]
    for i, r in enumerate(results):
        baseline = results[0]['attack_rate'][0] if results[0]['attack_rate'][0] > 0 else 1.0
        ax.plot(r['t_months'], r['attack_rate'] / baseline * 100,
                color=colors[i], linewidth=2, label=r['name'])
    ax.axhline(y=50, color='red', linestyle=':', alpha=0.5, label='50% reduction = R > D threshold')
    ax.set_xlabel('Months')
    ax.set_ylabel('Attack rate (% of baseline)')
    ax.set_title('Autoimmune Attack Rate Trajectory\nGoal: reduce enough that R > D')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    plt.suptitle('Microbiome Restoration Kinetics Detail\nsystematic approach — ODD Instance',
                 fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'microbiome_restoration_kinetics.png'),
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Figure saved: {os.path.join(OUTPUT_DIR, 'microbiome_restoration_kinetics.png')}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 70)
    print("GUT MICROBIOME-BUTYRATE-TREG AXIS MODEL")
    print("systematic approach — ODD Instance (numerics)")
    print("=" * 70)

    params = GutMicrobiomeParams()
    scenarios = make_scenarios()

    print(f"\nRunning {len(scenarios)} scenarios over 12 months...\n")

    results = []
    for sc in scenarios:
        print(f"  Running: {sc.name}")
        r = run_scenario(sc, params, t_months=12.0)
        results.append(r)

        # Print final state summary
        print(f"    Final Fp:       {r['Fp'][-1]*100:.1f}% (butyrate producers)")
        print(f"    Final F:B:      {r['fb_ratio'][-1]:.2f}")
        print(f"    Final Bc:       {r['Bc'][-1]:.1f} mM (colonic butyrate)")
        print(f"    Final Bs:       {r['Bs'][-1]:.2f} uM (systemic butyrate)")
        print(f"    Final barrier:  {r['Bi'][-1]:.2f}")
        print(f"    Final Treg:     {r['Treg'][-1]:.0f} cells/uL")
        print(f"    Final Teff:     {r['Teff'][-1]:.0f} cells/uL")
        print(f"    Final attack:   {r['attack_rate'][-1]:.5f}")
        print()

    # Restoration timelines
    print("\n" + "=" * 70)
    print("RESTORATION TIMELINES")
    print("=" * 70)
    for r in results:
        milestones = estimate_restoration_timeline(r)
        print(f"\n  {r['name']}:")
        for key, val in milestones.items():
            if val is not None:
                print(f"    {key}: day {val:.0f} ({val/30:.1f} months)")
            else:
                print(f"    {key}: NOT REACHED in 12 months")

    # Comparative analysis
    print("\n" + "=" * 70)
    print("COMPARATIVE ANALYSIS")
    print("=" * 70)
    baseline_attack = results[0]['attack_rate'][0]
    for r in results:
        final_attack = r['attack_rate'][-1]
        reduction = (1.0 - final_attack / baseline_attack) * 100 if baseline_attack > 0 else 0
        print(f"\n  {r['name']}:")
        print(f"    Attack rate reduction: {reduction:.1f}%")
        print(f"    Treg gain: +{r['Treg'][-1] - r['Treg'][0]:.0f} cells/uL")
        print(f"    Butyrate gain (colonic): +{r['Bc'][-1] - r['Bc'][0]:.1f} mM")
        print(f"    Butyrate gain (systemic): +{r['Bs'][-1] - r['Bs'][0]:.2f} uM")

    # Dietary recommendations summary
    print("\n" + "=" * 70)
    print("DIETARY RECOMMENDATIONS FOR T1DM PROTOCOL")
    print("=" * 70)
    print("""
    1. FIBER TARGETS:
       - Minimum: 25 g/day (2x Western average)
       - Optimal: 30-40 g/day
       - Sources: oats, legumes, Jerusalem artichoke, chicory root (inulin),
         resistant starch (cooled potatoes/rice), psyllium husk
       - CRITICAL: increase gradually (5g/week) to avoid GI distress

    2. FERMENTED FOODS:
       - Daily: 2-3 servings of fermented foods
       - Sources: sauerkraut, kimchi, kefir, yogurt (live cultures),
         miso, tempeh, kombucha
       - Provides microbial diversity + direct SCFA production

    3. SODIUM BUTYRATE SUPPLEMENT:
       - Dose: 600mg BID (1200mg/day total)
       - Form: enteric-coated sodium butyrate or tributyrin (better bioavailability)
       - Tributyrin alternative: 500-1000mg TID
       - Take with meals for better absorption
       - Provides IMMEDIATE systemic butyrate while microbiome recovers

    4. PROBIOTIC (F. PRAUSNITZII-CONTAINING):
       - Currently limited commercial availability
       - Next-generation probiotics in development (Exeliom Biosciences)
       - Alternative: Clostridium butyricum (Miyarisan, available in Japan)
       - Spore-based: Bacillus coagulans (indirect butyrate support)
       - Timeline: probiotic + prebiotic fiber = synbiotic approach

    5. TIMELINE:
       - Week 1-2: microbiome shift begins (measurable in stool)
       - Week 2-4: colonic butyrate rises, barrier repair starts
       - Month 1-2: systemic butyrate normalized, Treg expansion measurable
       - Month 3-6: stable microbiome recolonization, sustained Treg benefit
       - Month 6-12: full gut-immune axis restoration
    """)

    # Microbiome testing protocol
    print("\n" + "=" * 70)
    print("MICROBIOME TESTING PROTOCOL")
    print("=" * 70)
    print("""
    WHAT TO MEASURE:
      - 16S rRNA sequencing: Firmicutes:Bacteroidetes ratio
      - Specific taxa: F. prausnitzii, Roseburia, Eubacterium abundance
      - Fecal butyrate: gas chromatography (target > 10 mM)
      - Fecal calprotectin: gut inflammation marker (target < 50 ug/g)
      - Intestinal permeability: lactulose/mannitol ratio (target < 0.03)
      - Stool enterovirus PCR: CVB gut persistence marker
      - Serum butyrate: LC-MS/MS (target > 3 uM)

    WHEN TO MEASURE:
      - Baseline: before any intervention
      - 1 month: early response assessment
      - 3 months: microbiome composition shift
      - 6 months: stable recolonization check
      - 12 months: long-term maintenance
    """)

    # Generate figures
    print("\nGenerating figures...")
    plot_all_scenarios(results, params)
    plot_microbiome_restoration_detail(results)

    print("\nDone.")


if __name__ == '__main__':
    main()
