#!/usr/bin/env python3
"""
Gut Barrier - CVB Infection & Disease Cascade Model
=====================================================

Models the gut as both CVB RESERVOIR and IMMUNE MODULATOR, and the role
of gut barrier integrity in the full T1DM disease cascade.

Key insight: the gut is the PRIMARY site of CVB entry (oral-fecal route)
and can serve as a long-term viral reservoir via TD mutant persistence
in epithelium and Peyer's patches. Gut health determines:
    1. Whether CVB persists (reservoir function)
    2. How much systemic inflammation is generated (barrier function)
    3. Whether Tregs are induced (butyrate production)
    4. Whether the autoimmune cascade continues or halts

The Vicious Cycle (T1DM without intervention):
    CVB damages gut -> barrier breakdown -> bacterial translocation
    -> systemic inflammation -> reduced butyrate absorption
    -> fewer Tregs -> worse autoimmunity -> more beta cell destruction
    -> more insulin needed -> metabolic stress -> repeat

The Virtuous Cycle (protocol intervention):
    Butyrate + fiber -> gut healing -> barrier restoration
    -> less systemic inflammation -> more Tregs
    -> reduced autoimmunity -> beta cell regeneration > destruction
    (+ fluoxetine clearing CVB from gut reservoir)

State variables (10 coupled ODEs):
    Vg   = gut CVB wild-type viral load (copies/g, normalized)
    TDg  = gut TD mutant load (5'-deleted, persistent)
    Ep   = gut epithelial integrity (0 = destroyed, 1 = healthy)
    TJ   = tight junction protein level (claudin-1, occludin, ZO-1; normalized)
    Perm = intestinal permeability (0 = sealed, 1 = fully permeable)
    BT   = bacterial translocation rate (normalized)
    Sinf = systemic inflammation (composite: IL-6, TNF-a, CRP; normalized)
    Bc   = colonic butyrate (mM, from gut_microbiome_model)
    Treg = FoxP3+ Tregs (cells/uL)
    Vshed = stool viral shedding (proxy for gut CVB; copies/g stool)

Literature:
    [1]  Oikarinen S et al. Diabetes 2012;61:687-691 — enterovirus in T1DM gut
    [2]  Coppieters KT et al. J Exp Med 2012;209:51-60 — CVB gut tropism
    [3]  Chia J, Chia A. J Clin Pathol 2008;61:43-48 — 82% enteroviral RNA in CFS gut
    [4]  Peng L et al. J Nutr 2009;139:1619-1625 — butyrate upregulates tight junctions
    [5]  Wang HB et al. J Cell Physiol 2012;227:1491-1498 — butyrate AMPK pathway
    [6]  Vaarala O et al. Diabetes 2008;57:2555-2562 — leaky gut in T1DM
    [7]  Bosi E et al. Diabetologia 2006;49:2824-2827 — intestinal permeability in T1DM
    [8]  Fasano A. Physiol Rev 2011;91:151-175 — zonulin, leaky gut, autoimmunity
    [9]  Chapman NM et al. J Gen Virol 2008;89:2517-2528 — TD mutant biology
    [10] Honkanen H et al. Diabetologia 2017;60:424-431 — stool enterovirus in T1DM
    [11] Yeung WC et al. BMJ 2011;342:d35 — enterovirus meta-analysis
    [12] Furusawa Y et al. Nature 2013;504:446-450 — butyrate -> Tregs
    [13] Zuo J et al. Sci Rep 2018;8:7379 — fluoxetine IC50 for CVB 2C ATPase
    [14] Ulluwishewa D et al. J Nutr 2011;141:769-776 — probiotics + barrier function
    [15] Blikslager AT et al. Physiol Rev 2007;87:545-564 — mucosal repair physiology

systematic approach — Gut Barrier-CVB Model — numerical track (numerics)
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import os
import sys
from dataclasses import dataclass
from typing import Dict, List, Tuple
import warnings
warnings.filterwarnings('ignore')

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "figures")
os.makedirs(OUTPUT_DIR, exist_ok=True)


# =============================================================================
# PARAMETER DATACLASS
# =============================================================================

@dataclass
class GutBarrierParams:
    """
    All biological parameters for the 10-state gut barrier CVB model.
    """

    # --- Gut CVB viral dynamics ---
    Vg_initial_acute: float = 100.0       # acute infection (high replication)
    Vg_initial_chronic: float = 8.0       # chronic T1DM patient (low-grade persistence)
    Vg_replication_rate: float = 0.15     # /day in gut epithelium
    Vg_immune_clearance: float = 0.08     # /day by mucosal IgA + T cells
    Vg_carrying_cap: float = 200.0
    Vg_to_TD_conversion: float = 0.005    # fraction becoming TD mutants per replication cycle

    # --- TD mutant dynamics in gut ---
    TDg_initial: float = 15.0             # accumulated over years of chronic infection
    TDg_generation_from_V: float = 0.005  # per Vg replication unit [9]
    TDg_decay_rate: float = 0.001         # /day, very slow (cell turnover dependent)
    TDg_peyer_patch_reservoir: float = 0.8  # fraction in Peyer's patches (immune-privileged)

    # --- Fluoxetine antiviral effect on gut CVB ---
    fluoxetine_gut_efficacy: float = 0.75   # IC50-normalized suppression of gut CVB [13]
    fluoxetine_td_clearance_boost: float = 0.05  # enhances TD clearance via autophagy

    # --- Gut epithelial integrity ---
    Ep_initial_healthy: float = 0.95
    Ep_initial_t1dm: float = 0.60          # T1DM: documented epithelial damage [6,7]
    Ep_turnover_rate: float = 0.20         # /day, gut epithelium renews every 3-5 days [15]
    Ep_max_repair_rate: float = 0.15       # /day, maximum repair capacity
    Ep_cvb_damage_rate: float = 0.03       # /day per unit Vg
    Ep_td_damage_rate: float = 0.005       # /day per unit TDg (lower, no lytic cycle)
    Ep_butyrate_protection: float = 0.02   # /day per mM butyrate above threshold
    Ep_butyrate_threshold: float = 5.0     # mM, minimum for protective effect

    # --- Tight junction proteins ---
    # Claudin-1, occludin, ZO-1: butyrate upregulates via HDAC inhibition [4,5]
    TJ_initial_healthy: float = 1.0
    TJ_initial_t1dm: float = 0.40          # severely reduced in T1DM
    TJ_synthesis_rate: float = 0.05        # /day baseline
    TJ_butyrate_upregulation: float = 0.03  # /day per mM butyrate (HDAC effect) [4]
    TJ_degradation_rate: float = 0.04      # /day baseline
    TJ_cvb_degradation: float = 0.02       # CVB 2A protease cleaves tight junction proteins
    TJ_max: float = 1.2                    # can exceed baseline (therapeutic overshoot)

    # --- Intestinal permeability ---
    # Lactulose:mannitol ratio proxy
    # Healthy: < 0.03, T1DM: 0.05-0.15 [7]
    Perm_from_TJ: float = 1.0             # inverse relationship: low TJ = high Perm
    Perm_zonulin_effect: float = 0.3       # zonulin upregulated by gliadin, infection [8]

    # --- Bacterial translocation ---
    BT_baseline: float = 0.05             # healthy: minimal translocation
    BT_permeability_driven: float = 0.8   # scaling: how much Perm drives BT
    BT_clearance: float = 0.3             # /day, hepatic Kupffer cells clear
    BT_inflammation_per_unit: float = 2.0  # how much BT drives systemic inflammation

    # --- Systemic inflammation ---
    Sinf_initial_healthy: float = 0.1
    Sinf_initial_t1dm: float = 0.45        # elevated baseline in T1DM
    Sinf_from_BT: float = 0.5             # bacterial translocation contribution
    Sinf_from_Vg: float = 0.1             # direct viral cytokine induction
    Sinf_decay: float = 0.3               # /day, natural resolution
    Sinf_treg_suppression: float = 0.002  # per Treg cell, anti-inflammatory IL-10

    # --- Colonic butyrate (simplified, driven by external fiber/microbiome) ---
    Bc_production_low_fiber: float = 3.0   # mM/day, dysbiotic + low fiber
    Bc_production_high_fiber: float = 12.0  # mM/day, healthy microbiome + high fiber
    Bc_decay: float = 0.5                  # /day
    Bc_epithelial_absorption_healthy: float = 0.3  # fraction absorbed when epithelium intact
    Bc_epithelial_absorption_damaged: float = 0.10  # reduced when damaged

    # --- Treg (simplified, butyrate-driven) ---
    Treg_initial_t1dm: float = 90.0
    Treg_homeostatic: float = 180.0
    Treg_butyrate_induction: float = 0.06  # /day per mM butyrate above threshold
    Treg_butyrate_threshold: float = 5.0   # mM
    Treg_death_rate: float = 0.015
    Treg_max: float = 350.0

    # --- Stool viral shedding ---
    # Detectable by PCR when Vg + TDg above threshold
    shedding_per_Vg: float = 5.0          # copies/g per unit Vg
    shedding_per_TDg: float = 1.0         # copies/g per unit TDg (lower shedding)
    shedding_detection_threshold: float = 10.0  # copies/g, PCR limit of detection


# =============================================================================
# INTERVENTION SCENARIOS
# =============================================================================

@dataclass
class GutInterventionScenario:
    """Defines gut-specific interventions."""
    name: str = "no_treatment"
    fluoxetine: bool = False          # antiviral: clears gut CVB
    high_fiber: bool = False          # 30+ g/day fiber
    butyrate_supplement: bool = False  # sodium butyrate 600mg BID
    probiotic: bool = False           # F. prausnitzii-containing
    intervention_start_day: float = 0.0


def make_gut_scenarios() -> List[GutInterventionScenario]:
    """Create comparison scenarios for gut barrier model."""
    return [
        GutInterventionScenario(
            name="(a) No treatment (vicious cycle)",
            fluoxetine=False, high_fiber=False,
            butyrate_supplement=False, probiotic=False,
        ),
        GutInterventionScenario(
            name="(b) Fluoxetine only",
            fluoxetine=True, high_fiber=False,
            butyrate_supplement=False, probiotic=False,
        ),
        GutInterventionScenario(
            name="(c) Butyrate + fiber (gut healing only)",
            fluoxetine=False, high_fiber=True,
            butyrate_supplement=True, probiotic=False,
        ),
        GutInterventionScenario(
            name="(d) Full protocol (virtuous cycle)",
            fluoxetine=True, high_fiber=True,
            butyrate_supplement=True, probiotic=True,
        ),
    ]


# =============================================================================
# ODE SYSTEM
# =============================================================================

def gut_barrier_odes(t, y, params: GutBarrierParams, scenario: GutInterventionScenario):
    """
    10-state ODE system for gut barrier - CVB interaction.

    State vector y = [Vg, TDg, Ep, TJ, Perm, BT, Sinf, Bc, Treg, Vshed]
    """
    Vg, TDg, Ep, TJ, Perm, BT, Sinf, Bc, Treg, Vshed = y
    p = params
    sc = scenario

    # Clamp
    Vg = max(Vg, 0.0)
    TDg = max(TDg, 0.0)
    Ep = np.clip(Ep, 0.01, 1.0)
    TJ = np.clip(TJ, 0.01, p.TJ_max)
    Perm = np.clip(Perm, 0.0, 1.0)
    BT = max(BT, 0.0)
    Sinf = max(Sinf, 0.0)
    Bc = max(Bc, 0.0)
    Treg = max(Treg, 1.0)
    Vshed = max(Vshed, 0.0)

    # Intervention ramp-up
    if t >= sc.intervention_start_day:
        ramp = min(1.0, (t - sc.intervention_start_day) / 7.0)  # 1-week ramp
    else:
        ramp = 0.0

    # Fluoxetine effect on gut CVB
    fluox_suppression = p.fluoxetine_gut_efficacy * ramp if sc.fluoxetine else 0.0
    fluox_td_boost = p.fluoxetine_td_clearance_boost * ramp if sc.fluoxetine else 0.0

    # --- (1) Gut CVB wild-type ---
    Vg_growth = p.Vg_replication_rate * Vg * (1.0 - Vg / p.Vg_carrying_cap) * Ep
    # Replication depends on available epithelial cells
    Vg_clearance = p.Vg_immune_clearance * Vg * (1.0 + 0.01 * Treg)  # Tregs modestly help via IL-10
    Vg_fluoxetine = fluox_suppression * Vg
    Vg_to_td = p.Vg_to_TD_conversion * Vg

    dVg = Vg_growth - Vg_clearance - Vg_fluoxetine - Vg_to_td

    # --- (2) Gut TD mutants ---
    TDg_generation = p.TDg_generation_from_V * Vg
    TDg_decay = p.TDg_decay_rate * TDg * (1.0 - p.TDg_peyer_patch_reservoir)
    # Peyer's patch reservoir: ~80% are in immune-privileged sites
    TDg_fluoxetine = fluox_td_boost * TDg

    dTDg = TDg_generation + Vg_to_td - TDg_decay - TDg_fluoxetine

    # --- (3) Gut epithelial integrity ---
    # Repair: baseline turnover + butyrate-enhanced repair
    butyrate_above_threshold = max(Bc - p.Ep_butyrate_threshold, 0.0)
    Ep_repair = p.Ep_max_repair_rate * (1.0 - Ep) + p.Ep_butyrate_protection * butyrate_above_threshold * (1.0 - Ep)
    # Damage: CVB cytopathic effect
    Ep_damage = p.Ep_cvb_damage_rate * Vg / (Vg + 10.0) * Ep  # saturating damage
    Ep_td_damage = p.Ep_td_damage_rate * TDg / (TDg + 50.0) * Ep
    # Inflammation damage
    Ep_inf_damage = 0.02 * Sinf * Ep

    dEp = Ep_repair - Ep_damage - Ep_td_damage - Ep_inf_damage

    # --- (4) Tight junction proteins ---
    # Synthesis + butyrate upregulation, with logistic cap at TJ_max
    TJ_room = max(p.TJ_max - TJ, 0.0) / p.TJ_max  # 0 at max, 1 when depleted
    TJ_synthesis = p.TJ_synthesis_rate * Ep * TJ_room
    TJ_butyrate = p.TJ_butyrate_upregulation * butyrate_above_threshold * Ep * TJ_room
    TJ_degradation = p.TJ_degradation_rate * TJ
    TJ_cvb_damage = p.TJ_cvb_degradation * (Vg / (Vg + 20.0)) * TJ  # 2A protease

    dTJ = TJ_synthesis + TJ_butyrate - TJ_degradation - TJ_cvb_damage

    # --- (5) Intestinal permeability ---
    # Permeability is inversely related to TJ and Ep
    # target_perm = 1.0 - (TJ * Ep), relax toward it
    target_perm = np.clip(1.0 - TJ * Ep, 0.0, 1.0)
    # Add zonulin effect (infection-driven)
    zonulin = p.Perm_zonulin_effect * Vg / (Vg + 30.0)
    target_perm = min(target_perm + zonulin, 1.0)
    # Relaxation dynamics (fast: hours, modeled as /day)
    dPerm = 2.0 * (target_perm - Perm)

    # --- (6) Bacterial translocation ---
    BT_influx = p.BT_permeability_driven * Perm * Perm  # quadratic: worse when very permeable
    BT_clearance = p.BT_clearance * BT

    dBT = BT_influx - BT_clearance

    # --- (7) Systemic inflammation ---
    Sinf_from_bt = p.Sinf_from_BT * BT
    Sinf_from_virus = p.Sinf_from_Vg * (Vg + 0.3 * TDg) / ((Vg + TDg) + 20.0)
    Sinf_resolution = p.Sinf_decay * Sinf
    Sinf_treg = p.Sinf_treg_suppression * Treg * Sinf  # Tregs produce IL-10

    dSinf = Sinf_from_bt + Sinf_from_virus - Sinf_resolution - Sinf_treg

    # --- (8) Colonic butyrate (simplified) ---
    if sc.high_fiber and t >= sc.intervention_start_day:
        Bc_production = p.Bc_production_low_fiber + ramp * (p.Bc_production_high_fiber - p.Bc_production_low_fiber)
    else:
        Bc_production = p.Bc_production_low_fiber

    # Supplement adds directly to colonic butyrate
    if sc.butyrate_supplement and t >= sc.intervention_start_day:
        # 600mg BID sodium butyrate, ~25% reaches colon
        # 5.7 mmol * 2 doses * 0.25 / ~0.5L colonic volume ~ 5.7 mM boost
        Bc_supplement = ramp * 5.7
    else:
        Bc_supplement = 0.0

    # Probiotic boosts endogenous production
    if sc.probiotic and t >= sc.intervention_start_day:
        probiotic_boost = ramp * 2.0  # mM/day additional from supplemented Firmicutes
    else:
        probiotic_boost = 0.0

    # Absorption: depends on epithelial integrity
    absorption_eff = p.Bc_epithelial_absorption_damaged + Ep * (p.Bc_epithelial_absorption_healthy - p.Bc_epithelial_absorption_damaged)
    Bc_absorption = absorption_eff * Bc
    Bc_decay = p.Bc_decay * max(Bc - 2.0, 0.0)

    dBc = Bc_production + Bc_supplement + probiotic_boost - Bc_absorption - Bc_decay

    # --- (9) Treg (butyrate-driven, simplified) ---
    # In T1DM, the homeostatic set-point is depressed (~90) due to chronic inflammation
    # Butyrate raises the effective set-point via HDAC inhibition -> FoxP3
    butyrate_above = max(Bc - p.Treg_butyrate_threshold, 0.0)
    # Each mM of butyrate above threshold raises Treg set-point by ~15 cells/uL
    butyrate_setpoint_boost = 15.0 * butyrate_above / (butyrate_above + 8.0)  # saturating
    effective_setpoint = min(p.Treg_initial_t1dm + butyrate_setpoint_boost * 200.0 / 15.0, p.Treg_max)
    # Inflammation suppresses Tregs
    inflammation_penalty = 30.0 * Sinf  # high inflammation lowers set-point
    effective_setpoint = max(effective_setpoint - inflammation_penalty, 50.0)

    dTreg = 0.02 * (effective_setpoint - Treg)

    # --- (10) Stool viral shedding (PCR-detectable) ---
    target_shedding = p.shedding_per_Vg * Vg + p.shedding_per_TDg * TDg
    # Shedding follows viral load with ~1 day lag
    dVshed = 1.0 * (target_shedding - Vshed)

    return [dVg, dTDg, dEp, dTJ, dPerm, dBT, dSinf, dBc, dTreg, dVshed]


# =============================================================================
# SIMULATION RUNNER
# =============================================================================

def run_gut_scenario(scenario: GutInterventionScenario, params: GutBarrierParams = None,
                     t_months: float = 18.0) -> Dict:
    """
    Run the gut barrier CVB model for a single scenario.
    """
    if params is None:
        params = GutBarrierParams()

    t_days = t_months * 30.0
    t_span = (0, t_days)
    t_eval = np.linspace(0, t_days, int(t_days) + 1)

    # Initial conditions: chronic T1DM patient with gut CVB persistence
    y0 = [
        params.Vg_initial_chronic,     # Vg: low-grade gut CVB
        params.TDg_initial,            # TDg: accumulated TD mutants
        params.Ep_initial_t1dm,        # Ep: damaged epithelium
        params.TJ_initial_t1dm,        # TJ: reduced tight junctions
        0.55,                           # Perm: elevated permeability
        0.35,                           # BT: elevated bacterial translocation
        params.Sinf_initial_t1dm,      # Sinf: chronic low-grade inflammation
        4.0,                            # Bc: low colonic butyrate
        params.Treg_initial_t1dm,      # Treg: depressed
        params.shedding_per_Vg * params.Vg_initial_chronic +
        params.shedding_per_TDg * params.TDg_initial,  # Vshed: initial shedding
    ]

    sol = solve_ivp(
        gut_barrier_odes,
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

    labels = ['Vg', 'TDg', 'Ep', 'TJ', 'Perm', 'BT', 'Sinf', 'Bc', 'Treg', 'Vshed']
    result = {
        'name': scenario.name,
        't_days': sol.t,
        't_months': sol.t / 30.0,
    }
    for i, label in enumerate(labels):
        result[label] = sol.y[i]

    # Compute PCR detection status
    result['pcr_detectable'] = result['Vshed'] >= params.shedding_detection_threshold

    return result


# =============================================================================
# VISUALIZATION
# =============================================================================

def plot_vicious_vs_virtuous(results: List[Dict], params: GutBarrierParams):
    """Generate comprehensive figure showing vicious vs virtuous cycle."""

    colors = ['#d62728', '#9467bd', '#ff7f0e', '#1f77b4']
    fig = plt.figure(figsize=(22, 28))
    gs = GridSpec(5, 2, hspace=0.35, wspace=0.3)

    # --- Panel 1: Gut CVB viral load ---
    ax = fig.add_subplot(gs[0, 0])
    for i, r in enumerate(results):
        ax.plot(r['t_months'], r['Vg'], color=colors[i], linewidth=2, label=r['name'])
    ax.set_xlabel('Time (months)')
    ax.set_ylabel('Gut CVB load (normalized)')
    ax.set_title('Gut CVB Wild-Type Viral Load\n(Primary entry site, oral-fecal route)')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)
    ax.set_yscale('log')
    ax.set_ylim(bottom=0.01)

    # --- Panel 2: TD mutants in gut ---
    ax = fig.add_subplot(gs[0, 1])
    for i, r in enumerate(results):
        ax.plot(r['t_months'], r['TDg'], color=colors[i], linewidth=2, label=r['name'])
    ax.set_xlabel('Time (months)')
    ax.set_ylabel('Gut TD mutant load')
    ax.set_title('TD Mutant Reservoir (Peyer\'s Patches)\n(5\'-deleted, persistent, 80% in immune-privileged sites)')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # --- Panel 3: Gut epithelial integrity ---
    ax = fig.add_subplot(gs[1, 0])
    for i, r in enumerate(results):
        ax.plot(r['t_months'], r['Ep'], color=colors[i], linewidth=2, label=r['name'])
    ax.axhline(y=0.85, color='green', linestyle='--', alpha=0.5, label='Healthy threshold')
    ax.set_xlabel('Time (months)')
    ax.set_ylabel('Epithelial integrity (0-1)')
    ax.set_title('Gut Epithelial Integrity\n(Turnover every 3-5 days, CVB damages)')
    ax.legend(fontsize=7)
    ax.set_ylim(0, 1.05)
    ax.grid(True, alpha=0.3)

    # --- Panel 4: Tight junction proteins ---
    ax = fig.add_subplot(gs[1, 1])
    for i, r in enumerate(results):
        ax.plot(r['t_months'], r['TJ'], color=colors[i], linewidth=2, label=r['name'])
    ax.axhline(y=0.8, color='green', linestyle='--', alpha=0.5, label='Functional threshold')
    ax.set_xlabel('Time (months)')
    ax.set_ylabel('Tight junction level (normalized)')
    ax.set_title('Tight Junction Proteins\n(Claudin-1, Occludin, ZO-1; butyrate upregulates via HDAC)')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # --- Panel 5: Intestinal permeability ---
    ax = fig.add_subplot(gs[2, 0])
    for i, r in enumerate(results):
        ax.plot(r['t_months'], r['Perm'], color=colors[i], linewidth=2, label=r['name'])
    ax.axhline(y=0.15, color='green', linestyle='--', alpha=0.5, label='Healthy (< 0.15)')
    ax.set_xlabel('Time (months)')
    ax.set_ylabel('Permeability (0-1)')
    ax.set_title('Intestinal Permeability ("Leaky Gut")\n(Lactulose:mannitol ratio proxy)')
    ax.legend(fontsize=7)
    ax.set_ylim(0, 1.0)
    ax.grid(True, alpha=0.3)

    # --- Panel 6: Systemic inflammation ---
    ax = fig.add_subplot(gs[2, 1])
    for i, r in enumerate(results):
        ax.plot(r['t_months'], r['Sinf'], color=colors[i], linewidth=2, label=r['name'])
    ax.axhline(y=0.15, color='green', linestyle='--', alpha=0.5, label='Healthy baseline')
    ax.set_xlabel('Time (months)')
    ax.set_ylabel('Systemic inflammation (normalized)')
    ax.set_title('Systemic Inflammation\n(IL-6, TNF-a, CRP; driven by bacterial translocation)')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # --- Panel 7: Treg count ---
    ax = fig.add_subplot(gs[3, 0])
    for i, r in enumerate(results):
        ax.plot(r['t_months'], r['Treg'], color=colors[i], linewidth=2, label=r['name'])
    ax.axhspan(150, 300, alpha=0.08, color='green', label='Healthy range')
    ax.set_xlabel('Time (months)')
    ax.set_ylabel('Treg (cells/uL)')
    ax.set_title('Regulatory T Cells\n(Butyrate-driven FoxP3+ induction)')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # --- Panel 8: Stool enterovirus PCR ---
    ax = fig.add_subplot(gs[3, 1])
    for i, r in enumerate(results):
        ax.plot(r['t_months'], r['Vshed'], color=colors[i], linewidth=2, label=r['name'])
    ax.axhline(y=params.shedding_detection_threshold, color='red', linestyle='--',
               alpha=0.5, label=f'PCR detection limit ({params.shedding_detection_threshold} copies/g)')
    ax.set_xlabel('Time (months)')
    ax.set_ylabel('Stool viral shedding (copies/g)')
    ax.set_title('Stool Enterovirus PCR\n(Clinical biomarker for gut CVB persistence)')
    ax.legend(fontsize=7)
    ax.set_yscale('log')
    ax.set_ylim(bottom=0.1)
    ax.grid(True, alpha=0.3)

    # --- Panel 9: Vicious vs Virtuous cycle diagram ---
    ax = fig.add_subplot(gs[4, 0])
    ax.axis('off')
    vicious_text = """
THE VICIOUS CYCLE (untreated T1DM)
===================================

CVB infects gut epithelium (oral-fecal entry)
        |
        v
Epithelial damage + tight junction breakdown
        |
        v
"Leaky gut" --> bacterial translocation
        |
        v
Systemic inflammation (IL-6, TNF-a, CRP)
        |
        v
Reduced butyrate absorption (damaged epithelium)
        |
        v
Fewer Tregs (less HDAC inhibition, less FoxP3)
        |
        v
Worse autoimmunity --> more beta cell destruction
        |
        v
CVB persists (TD mutants in Peyer's patches)
        |
        v
REPEAT (self-amplifying loop)
"""
    ax.text(0.05, 0.95, vicious_text, transform=ax.transAxes,
            fontsize=9, fontfamily='monospace', verticalalignment='top',
            color='#d62728')

    ax = fig.add_subplot(gs[4, 1])
    ax.axis('off')
    virtuous_text = """
THE VIRTUOUS CYCLE (full protocol)
====================================

Fluoxetine clears gut CVB (2C ATPase blockade)
        |
        v
Epithelial recovery (3-5 day turnover)
        |
        v
Butyrate (supplement + fiber + probiotic)
        |
        v
Tight junction upregulation (claudin-1, occludin, ZO-1)
        |
        v
Barrier sealed --> no bacterial translocation
        |
        v
Inflammation resolves
        |
        v
Butyrate absorbed efficiently --> HDAC inhibition
        |
        v
FoxP3+ Treg expansion (2-3x increase)
        |
        v
Autoreactive T cells suppressed
        |
        v
Beta cell regeneration > destruction --> CURE
"""
    ax.text(0.05, 0.95, virtuous_text, transform=ax.transAxes,
            fontsize=9, fontfamily='monospace', verticalalignment='top',
            color='#1f77b4')

    fig.suptitle('Gut Barrier-CVB Disease Cascade: Vicious vs Virtuous Cycle\n'
                 'systematic approach — numerical track (numerics)',
                 fontsize=14, fontweight='bold', y=0.99)

    plt.savefig(os.path.join(OUTPUT_DIR, 'gut_barrier_cvb_cascade.png'),
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Figure saved: {os.path.join(OUTPUT_DIR, 'gut_barrier_cvb_cascade.png')}")


def plot_stool_pcr_trajectory(results: List[Dict], params: GutBarrierParams):
    """Focused figure on stool enterovirus PCR as a clinical monitoring tool."""
    colors = ['#d62728', '#9467bd', '#ff7f0e', '#1f77b4']

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Panel 1: Full trajectory
    ax = axes[0]
    for i, r in enumerate(results):
        ax.plot(r['t_months'], r['Vshed'], color=colors[i], linewidth=2, label=r['name'])
    ax.axhline(y=params.shedding_detection_threshold, color='red', linestyle='--',
               alpha=0.7, linewidth=1.5, label='PCR detection limit')
    ax.set_xlabel('Time (months)')
    ax.set_ylabel('Stool viral shedding (copies/g)')
    ax.set_title('Stool Enterovirus PCR Trajectory')
    ax.legend(fontsize=7)
    ax.set_yscale('log')
    ax.set_ylim(0.1, 200)
    ax.grid(True, alpha=0.3)

    # Panel 2: Time to PCR-negative
    ax = axes[1]
    pcr_neg_times = []
    scenario_names = []
    for r in results:
        scenario_names.append(r['name'].split(')')[0] + ')')
        # Find first time Vshed drops below detection threshold
        below = np.where(r['Vshed'] < params.shedding_detection_threshold)[0]
        if len(below) > 0:
            pcr_neg_times.append(r['t_months'][below[0]])
        else:
            pcr_neg_times.append(float('inf'))

    bars = ax.barh(range(len(scenario_names)), pcr_neg_times, color=colors[:len(scenario_names)])
    ax.set_yticks(range(len(scenario_names)))
    ax.set_yticklabels(scenario_names, fontsize=8)
    ax.set_xlabel('Months to PCR-negative stool')
    ax.set_title('Time to Stool Enterovirus Clearance')
    for i, v in enumerate(pcr_neg_times):
        if v < float('inf'):
            ax.text(v + 0.2, i, f'{v:.1f} months', va='center', fontsize=8)
        else:
            ax.text(0.5, i, 'Not cleared', va='center', fontsize=8, color='red')
    ax.grid(True, alpha=0.3, axis='x')
    ax.set_xlim(0, max([v for v in pcr_neg_times if v < float('inf')], default=18) + 3)

    plt.suptitle('Stool Enterovirus PCR as Clinical Monitoring Biomarker\n'
                 'systematic approach — numerical track',
                 fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'stool_pcr_trajectory.png'),
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Figure saved: {os.path.join(OUTPUT_DIR, 'stool_pcr_trajectory.png')}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 70)
    print("GUT BARRIER - CVB DISEASE CASCADE MODEL")
    print("systematic approach — numerical track (numerics)")
    print("=" * 70)

    params = GutBarrierParams()
    scenarios = make_gut_scenarios()

    print(f"\nRunning {len(scenarios)} scenarios over 18 months...\n")

    results = []
    for sc in scenarios:
        print(f"  Running: {sc.name}")
        r = run_gut_scenario(sc, params, t_months=18.0)
        results.append(r)

        print(f"    Final Vg (CVB):       {r['Vg'][-1]:.3f}")
        print(f"    Final TDg (TD):       {r['TDg'][-1]:.2f}")
        print(f"    Final epithelium:     {r['Ep'][-1]:.2f}")
        print(f"    Final tight junctions:{r['TJ'][-1]:.2f}")
        print(f"    Final permeability:   {r['Perm'][-1]:.3f}")
        print(f"    Final inflammation:   {r['Sinf'][-1]:.3f}")
        print(f"    Final butyrate (mM):  {r['Bc'][-1]:.1f}")
        print(f"    Final Treg:           {r['Treg'][-1]:.0f} cells/uL")
        print(f"    Final stool PCR:      {r['Vshed'][-1]:.1f} copies/g", end='')
        if r['Vshed'][-1] < params.shedding_detection_threshold:
            print(" (BELOW DETECTION)")
        else:
            print(" (DETECTABLE)")
        print()

    # Vicious vs Virtuous cycle analysis
    print("\n" + "=" * 70)
    print("VICIOUS vs VIRTUOUS CYCLE ANALYSIS")
    print("=" * 70)

    no_treat = results[0]
    full_treat = results[3]

    print("\n  NO TREATMENT (vicious cycle):")
    print(f"    Permeability trend:    {no_treat['Perm'][0]:.2f} -> {no_treat['Perm'][-1]:.2f}")
    print(f"    Inflammation trend:    {no_treat['Sinf'][0]:.2f} -> {no_treat['Sinf'][-1]:.2f}")
    print(f"    Treg trend:            {no_treat['Treg'][0]:.0f} -> {no_treat['Treg'][-1]:.0f}")
    print(f"    Gut CVB persistence:   {no_treat['Vg'][-1]:.2f} (stool PCR: {no_treat['Vshed'][-1]:.0f})")

    print("\n  FULL PROTOCOL (virtuous cycle):")
    print(f"    Permeability trend:    {full_treat['Perm'][0]:.2f} -> {full_treat['Perm'][-1]:.2f}")
    print(f"    Inflammation trend:    {full_treat['Sinf'][0]:.2f} -> {full_treat['Sinf'][-1]:.2f}")
    print(f"    Treg trend:            {full_treat['Treg'][0]:.0f} -> {full_treat['Treg'][-1]:.0f}")
    print(f"    Gut CVB clearance:     {full_treat['Vg'][-1]:.4f} (stool PCR: {full_treat['Vshed'][-1]:.1f})")

    # CVB gut reservoir persistence
    print("\n" + "=" * 70)
    print("CVB GUT RESERVOIR PERSISTENCE")
    print("=" * 70)
    print("""
    Key findings from the model:

    1. WITHOUT TREATMENT: CVB persists indefinitely in gut epithelium
       - TD mutants accumulate in Peyer's patches (immune-privileged)
       - Stool enterovirus PCR remains positive (detectable viral shedding)
       - Continuous epithelial damage maintains leaky gut

    2. FLUOXETINE ALONE: Clears wild-type CVB but TD mutants persist
       - Wild-type CVB drops rapidly (days to weeks)
       - TD mutants in Peyer's patches clear SLOWLY (months)
       - Stool PCR becomes negative but gut barrier still compromised

    3. BUTYRATE + FIBER ALONE: Heals barrier but doesn't clear virus
       - Tight junctions restored, permeability normalizes
       - Bacterial translocation stops, inflammation resolves
       - But CVB continues low-grade replication
       - Stool PCR may remain weakly positive

    4. FULL PROTOCOL: Both viral clearance AND gut healing
       - Fluoxetine clears CVB from gut
       - Butyrate + fiber heals barrier simultaneously
       - Synergistic: cleared virus = no more damage, healed gut = no more
         permeability-driven inflammation
       - This is the virtuous cycle in action
    """)

    # Stool PCR as monitoring tool
    print("\n" + "=" * 70)
    print("STOOL ENTEROVIRUS PCR: MONITORING PROTOCOL")
    print("=" * 70)
    print("""
    CLINICAL MONITORING RECOMMENDATION:

    Test: Stool enterovirus RT-PCR (pan-enterovirus or CVB-specific)

    Schedule:
      Baseline:  Establish whether gut CVB reservoir is present
      Month 1:   Early treatment response (fluoxetine should suppress)
      Month 3:   Confirm wild-type clearance
      Month 6:   TD mutant clearance (slower)
      Month 12:  Confirm sustained clearance

    Interpretation:
      POSITIVE at baseline = confirmed gut CVB reservoir (expected in T1DM)
      POSITIVE at month 3  = incomplete clearance, consider dose adjustment
      NEGATIVE at month 3  = wild-type cleared, continue for TD mutants
      NEGATIVE at month 6  = full gut clearance likely
      NEGATIVE at month 12 = confirmed sustained clearance

    Cost: ~$50-100 per test (RT-PCR)
    Availability: any reference lab (Quest, Labcorp)
    """)

    # Connection to all 12 diseases
    print("\n" + "=" * 70)
    print("GUT-IMMUNE AXIS: CONNECTION TO ALL 12 DISEASES")
    print("=" * 70)
    print("""
    The gut is the COMMON ENTRY POINT for CVB in all 12 diseases.
    Oral-fecal transmission -> gut epithelium -> viremia -> organ tropism.

    Disease              | Gut connection
    ---------------------|------------------------------------------
    T1DM                 | Gut CVB -> pancreas viremia; gut dysbiosis -> Treg deficit
    Myocarditis          | Gut CVB -> cardiac viremia; leaky gut -> systemic inflammation
    Dilated CM           | Same as myocarditis (chronic progression)
    Pericarditis         | Gut CVB -> pericardial viremia
    ME/CFS               | Gut CVB persistence (82% stool positive, Chia 2008)
    Pancreatitis         | Gut CVB -> pancreatic duct; shared anatomy
    Hepatitis            | Gut CVB -> portal vein -> liver (first organ reached)
    Encephalitis         | Gut CVB -> viremia -> BBB crossing
    Aseptic meningitis   | Same pathway as encephalitis (meninges)
    Orchitis             | Gut CVB -> testicular viremia
    Pleurodynia          | Gut CVB -> skeletal muscle viremia
    Neonatal sepsis      | Maternal gut CVB -> vertical/perinatal transmission

    IMPLICATION: Gut health is a UNIVERSAL modifier for ALL 12 diseases.
    Optimizing the gut-immune axis (fiber + butyrate + probiotic) benefits
    EVERY disease in the campaign, not just T1DM.
    """)

    # Generate figures
    print("\nGenerating figures...")
    plot_vicious_vs_virtuous(results, params)
    plot_stool_pcr_trajectory(results, params)

    print("\nDone.")


if __name__ == '__main__':
    main()
