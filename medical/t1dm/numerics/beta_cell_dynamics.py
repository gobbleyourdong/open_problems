#!/usr/bin/env python3
"""
Beta Cell Dynamics: THE Core Model for the T1DM Cure Thesis
============================================================

This is the mechanistic ODE model underlying THEWALL.md's central claim:

    dB/dt = R - D

    When R > D, beta cell mass grows. When R > D PERMANENTLY, the patient
    is cured of Type 1 Diabetes.

State variables (9 coupled ODEs):
    B   = functional beta cell mass (fraction of normal, 0-1)
    Bd  = dormant/quiescent beta cells (fraction, 0-1)
    A   = alpha cell mass (fraction of normal, 0-1)
    Teff = autoreactive CD8+ T effector cells (activity units)
    Treg = regulatory T cells (CD4+CD25+FoxP3+, activity units)
    V   = replicating CVB viral load (normalized)
    TD  = 5'-terminally deleted CVB mutants (persistence mechanism)
    Ab  = autoantibody titer (GAD65, IA-2, ZnT8, insulin; composite)
    Cp  = C-peptide level (nmol/L, output variable tracking beta function)

The Regeneration term (R) has 5 components:
    R1: Baseline beta cell replication (~0.1-0.5%/day stressed, Butler 2005)
    R2: FMD refeeding Ngn3+ progenitor burst (3-5x, Longo Cell 2017)
    R3: Alpha-to-beta transdifferentiation (GABA-mediated, Soltani 2011)
    R4: Semaglutide/GLP-1 proliferative + secretory signal
    R5: BHB anti-apoptotic effect via NLRP3 suppression

The Destruction term (D) has 4 components:
    D1: CD8+ T cell killing (MHC-I restricted, antigen-dependent)
    D2: CVB direct cytopathic effect (2A/3C protease)
    D3: ER stress-induced apoptosis (viral UPR -> CHOP)
    D4: Bystander killing (TNF-a, IL-1b, IFN-g cytokines)

the patient model:
    - 67 years of T1DM (diagnosed as infant/child)
    - Current beta cell mass: ~5-10% of normal (Butler: 88% have SOME at 50yr)
    - C-peptide: 0.1-0.2 nmol/L (detectable but low)
    - 5-year keto period with reduced insulin needs (lived data)

Protocol phases:
    Phase 1 (months 0-3):  fluoxetine + vitamin D + butyrate (reduce D)
    Phase 2 (months 3-6):  add FMD cycles (boost R via refeeding, reduce D)
    Phase 3 (months 6-12): add GABA + semaglutide (boost R further)
    Phase 4 (optional):    teplizumab if C-peptide not rising

Monte Carlo: 2000 virtual the patients with parameter uncertainty
    -> probability distribution of outcomes at 12, 24, 36 months

Literature:
    [1]  Butler AE et al. Diabetologia 2005;48:2221 — 88% residual beta cells
    [2]  Butler AE et al. JCEM 2007;92:3560 — 100x replication at Dx
    [3]  Cheng CW et al. Cell 2017;168:775 — FMD regenerates beta cells
    [4]  Soltani N et al. PNAS 2011;108:11692 — GABA transdifferentiation
    [5]  Youm YH et al. Nat Med 2015;21:263 — BHB suppresses NLRP3
    [6]  Krogvold L et al. Diabetes 2015;64:1682 — DiViD: CVB in 6/6
    [7]  Zuo J et al. Sci Rep 2018;8:7379 — fluoxetine IC50 ~1uM for CVB 2C
    [8]  Herold KC et al. NEJM 2002;346:1692 — anti-CD3 preserves C-peptide
    [9]  Oram RA et al. Diabetes Care 2014;37:1230 — persistent C-peptide
    [10] Arpaia N et al. Nature 2013;504:451 — butyrate -> FOXP3 -> Tregs
    [11] Greenbaum CJ et al. Diabetes 2012;61:2534 — C-peptide thresholds
    [12] Drucker DJ. Cell Metab 2018;28:319 — GLP-1 biology
    [13] Campbell JE, Drucker DJ. Cell Metab 2013;17:819 — GLP-1 beta cell effects
    [14] Akirav EM et al. PNAS 2011;108:9206 — beta cell turnover
    [15] Chapman NM et al. J Gen Virol 2008;89:2517 — TD mutants
    [16] Meier JJ et al. Diabetes 2005;54:2557 — human beta cell replication
    [17] Nir T et al. J Clin Invest 2007;117:2553 — beta cell regeneration

systematic approach — T1DM Core Model — ODD Instance (numerics)
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import os
import sys
import json
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Tuple, Optional
from copy import deepcopy
import warnings
warnings.filterwarnings('ignore')

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "figures")
os.makedirs(OUTPUT_DIR, exist_ok=True)


# =============================================================================
# PARAMETER DATACLASSES
# =============================================================================

@dataclass
class BetaCellParams:
    """
    All biological parameters for the 9-state ODE system.
    Defaults calibrated to the patient: 67yr T1DM, residual function.
    """

    # --- Beta cell mass parameters ---
    B_initial: float = 0.08             # fraction of normal (5-10% range, Butler)
    Bd_initial: float = 0.04            # dormant beta cells (dedifferentiated)
    B_replication_rate: float = 0.003   # /day baseline replication (0.1-0.5%/day, [16])
    B_neogenesis_rate: float = 0.0001   # /day, duct progenitor differentiation [14,17]
    B_max: float = 1.0                  # normal beta cell mass = 1.0
    B_dediff_rate: float = 0.0005       # /day, functional -> dormant under stress
    B_rediff_rate: float = 0.0002       # /day, dormant -> functional when stress drops

    # --- Alpha cell parameters ---
    A_initial: float = 0.95             # alpha cells largely preserved in T1DM
    A_to_beta_rate: float = 0.0001      # /day, baseline alpha-to-beta transdiff [4]

    # --- Immune parameters: T effectors ---
    Teff_initial: float = 15.0          # PZ: lower than newly diagnosed (long duration)
    Teff_expansion_rate: float = 0.03   # /day per antigen unit
    Teff_contraction_rate: float = 0.02 # /day natural contraction
    Teff_max: float = 80.0              # ceiling
    Teff_killing_rate: float = 0.0010   # beta cells killed per Teff unit per day
    Teff_exhaustion_factor: float = 0.15  # 67yr disease -> partial T cell exhaustion

    # --- Immune parameters: T regulators ---
    Treg_initial: float = 10.0          # depressed in long-standing T1DM
    Treg_homeostatic: float = 22.0      # healthy setpoint
    Treg_induction_rate: float = 0.012  # /day peripheral induction
    Treg_max: float = 60.0              # ceiling
    Treg_suppression_efficacy: float = 0.55  # how well Tregs suppress Teff

    # --- Viral parameters ---
    V_initial: float = 5.0              # PZ: very low replicating virus after 67yr
    V_growth_rate: float = 0.002        # /day, net replication in islets [6]
    V_carrying_cap: float = 200.0       # ceiling
    V_immune_clearance: float = 0.0008  # cleared by Teff/NK
    V_natural_decay: float = 0.001      # RNA degradation

    # --- TD mutant parameters ---
    TD_initial: float = 35.0            # PZ: accumulated over decades, some cleared
    TD_generation_rate: float = 0.0004  # per V replication event [15]
    TD_decay_rate: float = 0.0002       # /day natural (cell turnover, ~10yr half-life)
    TD_stress_per_unit: float = 0.007   # ER stress contribution
    TD_cytopathic_rate: float = 0.00005 # direct cell damage from 2A/3C proteases

    # --- Autoantibody parameters ---
    Ab_initial: float = 25.0            # PZ: moderate titer after 67yr
    Ab_production_rate: float = 0.01    # driven by B cell activation
    Ab_decay_rate: float = 0.005        # natural IgG half-life ~21 days
    Ab_damage_rate: float = 0.0001      # complement-mediated beta cell damage

    # --- C-peptide parameters (output) ---
    Cp_per_beta_fraction: float = 2.5   # nmol/L C-peptide per beta cell fraction
    Cp_secretion_efficiency: float = 0.6  # PZ: reduced per-cell secretion (exhaustion)

    # --- Metabolic parameters ---
    metabolic_stress_base: float = 0.25 # baseline glucose toxicity
    er_stress_sensitivity: float = 0.5  # how much viral load -> ER stress

    # --- HLA and genetic ---
    hla_risk: float = 1.0               # genetic susceptibility multiplier

    # --- Bystander killing ---
    cytokine_killing_rate: float = 0.0003  # TNF-a/IL-1b/IFN-g mediated


@dataclass
class ProtocolParams:
    """
    The full intervention protocol, phase by phase.
    Each intervention has an onset time (days) and effect parameters.
    """

    # --- Phase 1: Reduce D (months 0-3) ---
    # Fluoxetine: blocks CVB 2C ATPase [7]
    fluoxetine_start_day: float = 0.0
    fluoxetine_viral_suppression: float = 0.85
    fluoxetine_td_clearance_boost: float = 0.08

    # Vitamin D: Treg induction, cathelicidin
    vitamin_d_start_day: float = 0.0
    vitamin_d_treg_boost: float = 1.3         # Treg induction rate multiplier
    vitamin_d_antiinflammatory: float = 0.10  # reduces cytokine killing

    # Butyrate: FOXP3 derepression -> Tregs [10]
    butyrate_start_day: float = 0.0
    butyrate_treg_boost: float = 1.5
    butyrate_foxp3_effect: float = 0.15       # additional Treg stability

    # --- Phase 2: Add FMD cycles (months 3-6) ---
    fmd_start_day: float = 90.0
    fmd_cycle_length: float = 5.0             # days of fasting-mimicking
    fmd_refeeding_length: float = 3.0         # days of refeeding
    fmd_interval: float = 30.0               # days between cycle starts
    fmd_regen_burst: float = 4.0             # 3-5x Ngn3+ progenitor activation [3]
    fmd_autophagy_viral_clearance: float = 0.3  # extra viral clearance during fast
    fmd_stress_reduction: float = 0.50       # metabolic stress drop during fast
    fmd_bhb_nlrp3_suppression: float = 0.35  # NLRP3 inflammasome suppression [5]
    fmd_antigen_reduction: float = 0.40      # beta cells "go quiet" during fast

    # --- Phase 3: Add GABA + semaglutide (months 6-12) ---
    gaba_start_day: float = 180.0
    gaba_transdiff_rate: float = 0.0005      # /day alpha-to-beta [4]
    gaba_antiinflammatory: float = 0.20      # reduces Teff expansion
    gaba_antiapoptotic: float = 0.15         # direct beta cell protection

    semaglutide_start_day: float = 180.0
    semaglutide_proliferative: float = 1.25  # mild beta cell proliferation boost [12,13]
    semaglutide_secretion_boost: float = 1.40  # enhanced GSIS per beta cell
    semaglutide_glucagon_suppression: float = 0.30  # reduces glucagon -> less stress
    semaglutide_antiapoptotic: float = 0.10  # GLP-1R mediated survival signal

    # --- Phase 4 (optional): Teplizumab ---
    teplizumab_enabled: bool = False
    teplizumab_start_day: float = 365.0      # if C-peptide not rising by month 12
    teplizumab_teff_depletion: float = 0.50  # 50% acute Teff reduction [8]
    teplizumab_duration_days: float = 180.0  # effect duration
    teplizumab_treg_sparing: float = 0.90    # preferentially spares Tregs

    # --- BHB supplementation (daily, from day 0) ---
    bhb_start_day: float = 0.0
    bhb_nlrp3_suppression: float = 0.20      # daily BHB salts during fasting window
    bhb_antiapoptotic: float = 0.10          # reduces beta cell apoptosis [5]


# =============================================================================
# HELPER: FMD cycle state at a given time
# =============================================================================

def fmd_state(t: float, protocol: ProtocolParams) -> Tuple[bool, bool, float]:
    """
    Determine if time t falls within an FMD fasting or refeeding window.

    Returns: (is_fasting, is_refeeding, cycle_day)
    """
    if t < protocol.fmd_start_day:
        return False, False, -1.0

    days_since_start = t - protocol.fmd_start_day
    cycle_position = days_since_start % protocol.fmd_interval

    if cycle_position < protocol.fmd_cycle_length:
        return True, False, cycle_position
    elif cycle_position < protocol.fmd_cycle_length + protocol.fmd_refeeding_length:
        return False, True, cycle_position - protocol.fmd_cycle_length
    else:
        return False, False, cycle_position


def intervention_active(t: float, start_day: float) -> bool:
    """Check if an intervention is active at time t."""
    return t >= start_day


# =============================================================================
# THE 9-STATE ODE SYSTEM
# =============================================================================

def beta_cell_ode(t, y, params: BetaCellParams, protocol: ProtocolParams):
    """
    The core ODE system for T1DM beta cell dynamics.

    State vector y = [B, Bd, A, Teff, Treg, V, TD, Ab, Cp]

        B    = functional beta cell mass (fraction 0-1)
        Bd   = dormant/dedifferentiated beta cells (fraction 0-1)
        A    = alpha cell mass (fraction 0-1)
        Teff = autoreactive CD8+ T effector activity
        Treg = regulatory T cell activity (CD4+CD25+FoxP3+)
        V    = replicating CVB viral load
        TD   = 5'-terminally deleted CVB mutants
        Ab   = autoantibody titer (composite)
        Cp   = C-peptide level (nmol/L)

    Returns: [dB, dBd, dA, dTeff, dTreg, dV, dTD, dAb, dCp]
    """
    # Unpack state
    B, Bd, A_cells, Teff, Treg, V, TD, Ab, Cp = y

    # Clamp to physical bounds
    B       = max(B, 0.0)
    Bd      = max(Bd, 0.0)
    A_cells = max(A_cells, 0.0)
    Teff    = max(Teff, 0.0)
    Treg    = max(Treg, 0.0)
    V       = max(V, 0.0)
    TD      = max(TD, 0.0)
    Ab      = max(Ab, 0.0)
    Cp      = max(Cp, 0.0)

    p = params
    pr = protocol

    # Check intervention status
    fluox_on = intervention_active(t, pr.fluoxetine_start_day)
    vitd_on  = intervention_active(t, pr.vitamin_d_start_day)
    buty_on  = intervention_active(t, pr.butyrate_start_day)
    gaba_on  = intervention_active(t, pr.gaba_start_day)
    sema_on  = intervention_active(t, pr.semaglutide_start_day)
    bhb_on   = intervention_active(t, pr.bhb_start_day)
    tepl_on  = (pr.teplizumab_enabled and
                intervention_active(t, pr.teplizumab_start_day) and
                t < pr.teplizumab_start_day + pr.teplizumab_duration_days)

    is_fasting, is_refeeding, fmd_day = fmd_state(t, pr)

    # =========================================================================
    # 1. STRESS COMPUTATION (drives antigen presentation and destruction)
    # =========================================================================

    # Metabolic stress: inversely proportional to functional beta cell mass
    # When few beta cells remain, each is overworked (glucotoxicity)
    metabolic_stress = p.metabolic_stress_base / max(B + 0.5 * Bd, 0.01)

    # Exogenous insulin always present (the patient is on insulin)
    metabolic_stress *= 0.30  # insulin therapy reduces stress by ~70%

    # FMD fasting: beta cells "go quiet" - minimal insulin demand
    if is_fasting:
        metabolic_stress *= (1.0 - pr.fmd_stress_reduction)

    # Semaglutide reduces glucagon -> less hepatic glucose output -> less stress
    if sema_on:
        metabolic_stress *= (1.0 - pr.semaglutide_glucagon_suppression)

    # TD mutant-induced ER stress: the chronic persistence signal
    td_stress = p.TD_stress_per_unit * TD

    # Replicating virus ER stress
    viral_stress = p.er_stress_sensitivity * 0.005 * V

    # Inflammatory cytokine stress (from Teff activity)
    cytokine_stress = 0.002 * Teff

    total_stress = metabolic_stress + td_stress + viral_stress + cytokine_stress

    # =========================================================================
    # 2. ANTIGEN PRESENTATION (the amplification signal)
    # =========================================================================
    # Stressed beta cells display neoantigens on MHC-I (proinsulin, GAD65,
    # IA-2, ZnT8). TD-infected cells present viral proteins. HLA risk
    # modulates how effectively these are presented to CD8+ T cells.

    antigen_load = total_stress * max(B, 0.005) * p.hla_risk

    # FMD fasting: reduced neoantigen display (beta cells quiescent)
    if is_fasting:
        antigen_load *= (1.0 - pr.fmd_antigen_reduction)

    # =========================================================================
    # 3. REPLICATING VIRUS DYNAMICS (V)
    # =========================================================================
    v_growth = p.V_growth_rate * V * (1.0 - V / p.V_carrying_cap) * max(B, 0.005)

    v_immune_clear = p.V_immune_clearance * V * Teff / (Teff + 5.0)
    v_natural_decay = p.V_natural_decay * V

    v_fluox_effect = 0.0
    if fluox_on:
        v_growth *= (1.0 - pr.fluoxetine_viral_suppression)
        v_fluox_effect = 0.15 * V  # accelerated decay without replication

    v_fmd_clear = 0.0
    if is_fasting:
        v_fmd_clear = pr.fmd_autophagy_viral_clearance * V  # autophagy clears

    dV = v_growth - v_immune_clear - v_natural_decay - v_fluox_effect - v_fmd_clear

    # =========================================================================
    # 4. TD MUTANT DYNAMICS (the root cause of chronicity)
    # =========================================================================
    td_generation = p.TD_generation_rate * V * max(B, 0.005)
    td_natural_decay = p.TD_decay_rate * TD

    td_fluox_decay = 0.0
    if fluox_on:
        td_generation *= (1.0 - pr.fluoxetine_viral_suppression)
        td_fluox_decay = pr.fluoxetine_td_clearance_boost * TD

    td_fmd_decay = 0.0
    if is_fasting:
        td_fmd_decay = 0.02 * TD  # autophagy helps clear TD-infected cells

    dTD = td_generation - td_natural_decay - td_fluox_decay - td_fmd_decay

    # =========================================================================
    # 5. T EFFECTOR DYNAMICS (Teff) — CD8+ autoreactive T cells
    # =========================================================================
    # Expansion driven by antigen presentation, suppressed by Tregs
    teff_expansion = p.Teff_expansion_rate * antigen_load * (1.0 - Teff / p.Teff_max)

    # Treg suppression: Michaelis-Menten competition
    suppression = 1.0 / (1.0 + p.Treg_suppression_efficacy * Treg / max(Teff + 1.0, 1.0))

    # T cell exhaustion in long-standing disease (67yr -> substantial exhaustion)
    exhaustion_modifier = 1.0 - p.Teff_exhaustion_factor

    # GABA anti-inflammatory
    if gaba_on:
        suppression *= (1.0 - pr.gaba_antiinflammatory)

    # BHB NLRP3 suppression (daily)
    if bhb_on:
        suppression *= (1.0 - pr.bhb_nlrp3_suppression)

    # FMD fasting: immune quiescence
    if is_fasting:
        suppression *= (1.0 - pr.fmd_bhb_nlrp3_suppression)

    teff_contraction = p.Teff_contraction_rate * Teff

    # Teplizumab: direct depletion
    tepl_effect = 0.0
    if tepl_on:
        tepl_effect = pr.teplizumab_teff_depletion * Teff * 0.01

    dTeff = (teff_expansion * suppression * exhaustion_modifier
             - teff_contraction - tepl_effect)

    # =========================================================================
    # 6. REGULATORY T CELL DYNAMICS (Treg)
    # =========================================================================
    treg_induction = p.Treg_induction_rate * (p.Treg_homeostatic - Treg)
    treg_induction = max(treg_induction, -0.05 * max(Treg, 0.1))

    # Butyrate + Vitamin D synergy
    treg_boost = 1.0
    if buty_on:
        treg_boost *= pr.butyrate_treg_boost
    if vitd_on:
        treg_boost *= pr.vitamin_d_treg_boost

    # Teplizumab spares Tregs
    tepl_treg_loss = 0.0
    if tepl_on:
        tepl_treg_loss = (1.0 - pr.teplizumab_treg_sparing) * Treg * 0.005

    dTreg = treg_induction * treg_boost - tepl_treg_loss

    # =========================================================================
    # 7. AUTOANTIBODY DYNAMICS (Ab)
    # =========================================================================
    # Driven by antigen load (B cells activated by autoreactive CD4+ T cells)
    # Autoantibodies are biomarkers more than direct effectors, but they
    # contribute some complement-mediated damage
    ab_production = p.Ab_production_rate * antigen_load
    ab_decay = p.Ab_decay_rate * Ab

    dAb = ab_production - ab_decay

    # =========================================================================
    # 8. ALPHA CELL DYNAMICS (A)
    # =========================================================================
    # Alpha cells are mostly preserved in T1DM. They are the SOURCE for
    # GABA-mediated transdifferentiation. Small natural turnover.
    alpha_natural = 0.0001 * (1.0 - A_cells)  # homeostatic return to 1.0

    # GABA-driven transdifferentiation removes some alpha cells
    alpha_to_beta_loss = 0.0
    if gaba_on:
        alpha_to_beta_loss = pr.gaba_transdiff_rate * A_cells

    dA = alpha_natural - alpha_to_beta_loss

    # =========================================================================
    # 9. BETA CELL DYNAMICS — THE CORE INEQUALITY: dB/dt = R - D
    # =========================================================================

    # ---- REGENERATION (R) ----
    # R has 5 independent components that stack additively

    # R1: Baseline beta cell replication
    #     Existing functional beta cells divide. Rate ~0.1-0.5%/day depending
    #     on conditions. Stress INHIBITS replication (cells can't divide while
    #     fighting for survival). [2,14,16]
    stress_penalty = 1.0 / (1.0 + 0.8 * total_stress)
    R1_replication = p.B_replication_rate * B * stress_penalty * (1.0 - B - Bd)

    # Semaglutide mild proliferative boost
    if sema_on:
        R1_replication *= pr.semaglutide_proliferative

    # R2: FMD refeeding burst — Ngn3+ progenitor activation
    #     During the 2-3 day refeeding window after FMD, mTOR/IGF-1/Notch
    #     reactivation drives pancreatic progenitors to differentiate into
    #     beta cells. This is THE key regeneration mechanism. [3]
    R2_fmd_burst = 0.0
    if is_refeeding:
        # Burst proportional to progenitor pool (assumed proportional to
        # remaining duct/acinar tissue) and inversely proportional to
        # existing beta cell mass (more room = more differentiation)
        R2_fmd_burst = (pr.fmd_regen_burst * p.B_neogenesis_rate *
                        (1.0 - B - Bd) * stress_penalty)

    # R3: Alpha-to-beta transdifferentiation (GABA-mediated)
    #     GABA activates GABA-A receptors on alpha cells -> Pax4 induction
    #     -> alpha cell identity lost -> beta cell markers acquired [4]
    R3_transdiff = 0.0
    if gaba_on:
        R3_transdiff = pr.gaba_transdiff_rate * A_cells * (1.0 - B - Bd)

    # R4: Semaglutide enhanced glucose-stimulated insulin secretion (GSIS)
    #     Not direct proliferation but improved per-cell function.
    #     Modeled as functional "effective mass" increase — each cell
    #     secretes more insulin, so fewer cells needed for same effect.
    #     (Captured in C-peptide output, not dB directly)
    # [Semaglutide's proliferative effect is already in R1 above]

    # R5: BHB anti-apoptotic effect
    #     BHB suppresses NLRP3 -> less IL-1b -> less beta cell apoptosis
    #     Modeled as reduction in destruction rather than increase in R
    #     (implemented in D terms below)

    # R_neogenesis: baseline neogenesis from duct progenitors (always active)
    R_neogenesis = p.B_neogenesis_rate * stress_penalty * (1.0 - B - Bd)

    # R_rediff: dormant beta cells reactivating when stress drops
    R_rediff = p.B_rediff_rate * Bd * stress_penalty

    # TOTAL REGENERATION
    R_total = R1_replication + R2_fmd_burst + R3_transdiff + R_neogenesis + R_rediff

    # ---- DESTRUCTION (D) ----
    # D has 4 independent components

    # D1: CD8+ T cell killing (MHC-I restricted, antigen-dependent)
    #     Effective killing = Teff * beta cells * (1 - Treg suppression)
    #     Tregs compete with Teff at the site of killing
    treg_fraction = Treg / (Treg + Teff + 1.0)
    effective_teff = Teff * (1.0 - p.Treg_suppression_efficacy * treg_fraction)
    effective_teff = max(effective_teff, 0.0)
    D1_cd8_killing = p.Teff_killing_rate * effective_teff * B

    # D2: CVB direct cytopathic effect
    #     2A protease cleaves eIF4G -> translation shutoff
    #     3C protease cleaves NF-kB/NFAT -> immune evasion + cell stress
    #     Both TD mutants AND replicating virus contribute
    D2_viral_cytopathic = p.TD_cytopathic_rate * (TD + 2.0 * V) * B

    # D3: ER stress-induced apoptosis
    #     Viral replication in ER -> unfolded protein response (UPR)
    #     If UPR overwhelms: IRE1a -> CHOP -> apoptosis
    #     This pathway is independent of immune killing
    er_stress = td_stress + viral_stress
    D3_er_apoptosis = 0.0003 * er_stress * B / (1.0 + 0.5 * er_stress)

    # D4: Bystander killing (inflammatory cytokines)
    #     TNF-a, IL-1b, IFN-g from Teff and macrophages damage beta cells
    #     that are NOT directly targeted. This is "collateral damage."
    D4_bystander = p.cytokine_killing_rate * Teff * B

    # BHB/GABA/semaglutide anti-apoptotic effects REDUCE destruction
    antiapoptotic_factor = 1.0
    if bhb_on:
        antiapoptotic_factor -= pr.bhb_antiapoptotic
    if gaba_on:
        antiapoptotic_factor -= pr.gaba_antiapoptotic
    if sema_on:
        antiapoptotic_factor -= pr.semaglutide_antiapoptotic
    if is_fasting:
        antiapoptotic_factor -= 0.10  # autophagy removes damaged organelles
    antiapoptotic_factor = max(antiapoptotic_factor, 0.3)

    # Vitamin D anti-inflammatory on bystander killing
    vitd_factor = 1.0
    if vitd_on:
        vitd_factor = 1.0 - pr.vitamin_d_antiinflammatory

    # Autoantibody complement-mediated damage (small contribution)
    D_ab_complement = p.Ab_damage_rate * Ab * B

    # TOTAL DESTRUCTION
    D_total = ((D1_cd8_killing + D2_viral_cytopathic + D3_er_apoptosis) *
               antiapoptotic_factor +
               D4_bystander * vitd_factor * antiapoptotic_factor +
               D_ab_complement)

    # Dedifferentiation: stressed beta cells lose identity -> dormant
    dediff = p.B_dediff_rate * B * total_stress / (total_stress + 0.5)

    # THE INEQUALITY
    dB = R_total - D_total - dediff

    # Dormant beta cell dynamics
    dBd = dediff - R_rediff - 0.0001 * Bd  # slow natural loss

    # =========================================================================
    # 10. C-PEPTIDE (output variable)
    # =========================================================================
    # C-peptide is equimolar with insulin secretion. It reflects functional
    # beta cell mass * per-cell secretion efficiency.
    # Half-life of C-peptide in blood: ~30 minutes
    cp_production = (p.Cp_per_beta_fraction * B * p.Cp_secretion_efficiency)

    # Semaglutide boosts GSIS -> more insulin (and C-peptide) per cell
    if sema_on:
        cp_production *= pr.semaglutide_secretion_boost

    # C-peptide washout (plasma half-life ~30 min = 48 half-lives/day)
    # For daily-averaged model, use effective daily turnover
    cp_decay_rate = 2.0  # /day (fast washout, tracks beta mass closely)

    dCp = cp_production - cp_decay_rate * Cp

    return [dB, dBd, dA, dTeff, dTreg, dV, dTD, dAb, dCp]


# =============================================================================
# SIMULATION ENGINE
# =============================================================================

def simulate(params: BetaCellParams, protocol: ProtocolParams,
             t_years: float = 3.0, dt_output: float = 1.0,
             label: str = "simulation") -> dict:
    """
    Run the 9-state ODE system for a given patient + protocol.

    Args:
        params: Patient biological parameters
        protocol: Intervention protocol parameters
        t_years: Duration of simulation in years
        dt_output: Output time step in days
        label: Human-readable label for this simulation

    Returns:
        Dictionary with time series and summary statistics
    """
    t_span = (0, t_years * 365.25)
    t_eval = np.arange(0, t_years * 365.25, dt_output)

    y0 = [
        params.B_initial,
        params.Bd_initial,
        params.A_initial,
        params.Teff_initial,
        params.Treg_initial,
        params.V_initial,
        params.TD_initial,
        params.Ab_initial,
        params.Cp_per_beta_fraction * params.B_initial * params.Cp_secretion_efficiency / 2.0,
    ]

    # Try stiff-aware solver first, fall back to Radau if needed
    sol = solve_ivp(
        beta_cell_ode, t_span, y0,
        args=(params, protocol),
        method='RK45',
        t_eval=t_eval,
        max_step=0.5,   # half-day steps to capture FMD transitions
        rtol=1e-6, atol=1e-9,
    )

    if not sol.success:
        print(f"  [{label}] RK45 failed, switching to Radau...")
        sol = solve_ivp(
            beta_cell_ode, t_span, y0,
            args=(params, protocol),
            method='Radau',
            t_eval=t_eval,
            max_step=2.0,
            rtol=1e-5, atol=1e-8,
        )

    if not sol.success:
        print(f"  [{label}] WARNING: solver did not converge. Results may be inaccurate.")

    t_days = sol.t
    t_years_arr = t_days / 365.25

    # Extract and clamp
    B       = np.clip(sol.y[0], 0, 1)
    Bd      = np.clip(sol.y[1], 0, 1)
    A_cells = np.clip(sol.y[2], 0, 1)
    Teff    = np.clip(sol.y[3], 0, None)
    Treg    = np.clip(sol.y[4], 0, None)
    V       = np.clip(sol.y[5], 0, None)
    TD      = np.clip(sol.y[6], 0, None)
    Ab      = np.clip(sol.y[7], 0, None)
    Cp      = np.clip(sol.y[8], 0, None)

    # ---- Derived metrics ----
    # Total beta cells (functional + dormant)
    B_total = B + Bd

    # Effective beta cell function (accounts for semaglutide secretion boost)
    B_effective = B.copy()
    sema_mask = t_days >= protocol.semaglutide_start_day
    B_effective[sema_mask] *= protocol.semaglutide_secretion_boost

    # C-peptide (steady-state approximation for cleaner output)
    Cp_ss = (params.Cp_per_beta_fraction * B * params.Cp_secretion_efficiency)
    sema_mask_cp = t_days >= protocol.semaglutide_start_day
    Cp_ss[sema_mask_cp] *= protocol.semaglutide_secretion_boost

    # R and D decomposition for analysis
    R_series = np.gradient(B, t_days)
    # Smooth over 7-day window
    kernel = np.ones(7) / 7
    if len(R_series) > 7:
        R_smooth = np.convolve(R_series, kernel, mode='same')
    else:
        R_smooth = R_series

    # ---- Summary statistics ----
    # Time to detectable C-peptide improvement (>0.2 nmol/L)
    cp_threshold = 0.20
    cp_above = np.where(Cp_ss > cp_threshold)[0]
    time_to_cp_signal = t_years_arr[cp_above[0]] if len(cp_above) > 0 else None

    # Time to functional beta cell mass > 20% (possible insulin reduction)
    b20_above = np.where(B > 0.20)[0]
    time_to_b20 = t_years_arr[b20_above[0]] if len(b20_above) > 0 else None

    # Time to insulin independence (B > 30% effective)
    b30_above = np.where(B_effective > 0.30)[0]
    time_to_independence = t_years_arr[b30_above[0]] if len(b30_above) > 0 else None

    # Virus cleared?
    virus_cleared = V[-1] < 0.5 and TD[-1] < 2.0

    # Is beta cell mass growing at end?
    if len(R_smooth) > 30:
        final_trend = np.mean(R_smooth[-30:])
    else:
        final_trend = np.mean(R_smooth[-5:]) if len(R_smooth) > 5 else 0

    # Permanent remission: B > 10%, growing or stable at end
    permanent_remission = B[-1] > 0.10 and final_trend >= -1e-6

    return {
        "label": label,
        "t_days": t_days,
        "t_years": t_years_arr,
        "B": B,
        "Bd": Bd,
        "B_total": B_total,
        "B_effective": B_effective,
        "A": A_cells,
        "Teff": Teff,
        "Treg": Treg,
        "V": V,
        "TD": TD,
        "Ab": Ab,
        "Cp": Cp,
        "Cp_ss": Cp_ss,
        "R_smooth": R_smooth,
        "final_B": float(B[-1]),
        "final_Cp": float(Cp_ss[-1]),
        "final_V": float(V[-1]),
        "final_TD": float(TD[-1]),
        "final_Teff": float(Teff[-1]),
        "final_Treg": float(Treg[-1]),
        "time_to_cp_signal": time_to_cp_signal,
        "time_to_b20": time_to_b20,
        "time_to_independence": time_to_independence,
        "virus_cleared": virus_cleared,
        "permanent_remission": permanent_remission,
        "final_trend": float(final_trend),
    }


# =============================================================================
# the patient: SPECIFIC SCENARIOS
# =============================================================================

def patient_zero_params() -> BetaCellParams:
    """
    the patient: 67 years T1DM, diagnosed in infancy.
    Residual beta cell mass ~5-10% (Butler: 88% have SOME at 50yr).
    C-peptide ~0.1-0.2 nmol/L (detectable but low).
    5 years of keto showed reduced insulin needs -> evidence of residual function.
    Partial T cell exhaustion from decades of chronic autoimmunity.
    """
    return BetaCellParams(
        B_initial=0.08,
        Bd_initial=0.04,
        A_initial=0.95,
        Teff_initial=15.0,
        Teff_exhaustion_factor=0.15,
        Treg_initial=10.0,
        V_initial=5.0,
        TD_initial=35.0,
        Ab_initial=25.0,
        hla_risk=1.0,
        Cp_secretion_efficiency=0.6,
    )


def scenario_no_intervention() -> dict:
    """Baseline: the patient with no protocol. Natural progression."""
    print("=" * 72)
    print("SCENARIO: the patient — NO INTERVENTION (natural trajectory)")
    print("  67yr T1DM, ~8% beta cell mass, on insulin only")
    print("=" * 72)

    params = patient_zero_params()
    protocol = ProtocolParams(
        fluoxetine_start_day=1e6,   # never
        vitamin_d_start_day=1e6,
        butyrate_start_day=1e6,
        fmd_start_day=1e6,
        gaba_start_day=1e6,
        semaglutide_start_day=1e6,
        bhb_start_day=1e6,
        teplizumab_enabled=False,
    )

    result = simulate(params, protocol, t_years=3.0, label="no_intervention")
    _print_summary(result)
    return result


def scenario_full_protocol() -> dict:
    """The complete 4-phase protocol from THEWALL.md."""
    print("\n" + "=" * 72)
    print("SCENARIO: the patient — FULL PROTOCOL")
    print("  Phase 1 (mo 0-3):  fluoxetine + vitamin D + butyrate")
    print("  Phase 2 (mo 3-6):  add FMD cycles")
    print("  Phase 3 (mo 6-12): add GABA + semaglutide")
    print("  Phase 4 (optional): teplizumab if needed")
    print("=" * 72)

    params = patient_zero_params()
    protocol = ProtocolParams()  # defaults = the full protocol

    result = simulate(params, protocol, t_years=3.0, label="full_protocol")
    _print_summary(result)
    return result


def scenario_phase1_only() -> dict:
    """Phase 1 only: reduce D via fluoxetine + vitamin D + butyrate."""
    print("\n" + "=" * 72)
    print("SCENARIO: the patient — PHASE 1 ONLY (reduce D)")
    print("  fluoxetine + vitamin D + butyrate, no FMD/GABA/semaglutide")
    print("=" * 72)

    params = patient_zero_params()
    protocol = ProtocolParams(
        fmd_start_day=1e6,
        gaba_start_day=1e6,
        semaglutide_start_day=1e6,
        teplizumab_enabled=False,
    )

    result = simulate(params, protocol, t_years=3.0, label="phase1_only")
    _print_summary(result)
    return result


def scenario_with_teplizumab() -> dict:
    """Full protocol + teplizumab at month 12 (nuclear option)."""
    print("\n" + "=" * 72)
    print("SCENARIO: the patient — FULL PROTOCOL + TEPLIZUMAB")
    print("  All phases + teplizumab at month 12")
    print("=" * 72)

    params = patient_zero_params()
    protocol = ProtocolParams(teplizumab_enabled=True)

    result = simulate(params, protocol, t_years=3.0, label="full_plus_tepl")
    _print_summary(result)
    return result


def _print_summary(result: dict):
    """Print concise summary of simulation results."""
    print(f"\n  Results ({result['label']}):")
    print(f"    Final beta cell mass:    {result['final_B']*100:.2f}% of normal")
    print(f"    Final C-peptide:         {result['final_Cp']:.3f} nmol/L")
    print(f"    Final Teff:              {result['final_Teff']:.1f}")
    print(f"    Final Treg:              {result['final_Treg']:.1f}")
    print(f"    Final virus (V):         {result['final_V']:.2f}")
    print(f"    Final TD mutants:        {result['final_TD']:.2f}")
    print(f"    Virus cleared:           {result['virus_cleared']}")
    t_cp = result['time_to_cp_signal']
    print(f"    Time to C-peptide >0.2:  {t_cp:.1f} yr" if t_cp else
          "    Time to C-peptide >0.2:  not reached")
    t_b20 = result['time_to_b20']
    print(f"    Time to B > 20%:         {t_b20:.1f} yr" if t_b20 else
          "    Time to B > 20%:         not reached")
    t_ind = result['time_to_independence']
    print(f"    Time to independence:    {t_ind:.1f} yr" if t_ind else
          "    Time to independence:    not reached in simulation window")
    print(f"    Permanent remission:     {result['permanent_remission']}")
    print(f"    Final dB/dt trend:       {result['final_trend']:.2e} /day")


# =============================================================================
# MONTE CARLO: the patient PARAMETER UNCERTAINTY
# =============================================================================

def monte_carlo_patient_zero(n_samples: int = 2000, t_years: float = 3.0,
                              seed: int = 42) -> dict:
    """
    Run Monte Carlo simulation varying the patient's parameters within
    uncertainty ranges. Each parameter drawn from a distribution calibrated
    to literature ranges.

    Returns aggregated statistics and distributions.
    """
    print("\n" + "=" * 72)
    print(f"MONTE CARLO: {n_samples} VIRTUAL the patientS")
    print("  Varying: B_initial, TD_initial, Teff, Treg, HLA risk,")
    print("           Cp secretion efficiency, replication rate")
    print("  Protocol: full 4-phase protocol (Phases 1-3, no teplizumab)")
    print("=" * 72)

    rng = np.random.default_rng(seed)

    # Storage
    final_B_list = []
    final_Cp_list = []
    time_to_cp_list = []
    time_to_b20_list = []
    time_to_indep_list = []
    virus_cleared_list = []
    permanent_remission_list = []
    trajectories_B = []

    baseline_params = patient_zero_params()
    protocol = ProtocolParams()

    for i in range(n_samples):
        if (i + 1) % 200 == 0:
            print(f"  ... sample {i+1}/{n_samples}")

        # Draw parameters from uncertainty distributions
        p = deepcopy(baseline_params)

        # Beta cell mass: 3-15% range (log-normal centered at 8%)
        p.B_initial = np.clip(rng.lognormal(np.log(0.08), 0.35), 0.02, 0.20)
        p.Bd_initial = np.clip(rng.lognormal(np.log(0.04), 0.40), 0.01, 0.12)

        # TD mutant burden: 15-60 range (years of accumulation vary)
        p.TD_initial = np.clip(rng.normal(35.0, 12.0), 10.0, 80.0)
        p.V_initial = np.clip(rng.lognormal(np.log(5.0), 0.5), 0.5, 30.0)

        # Immune status varies
        p.Teff_initial = np.clip(rng.normal(15.0, 5.0), 3.0, 35.0)
        p.Treg_initial = np.clip(rng.normal(10.0, 3.0), 3.0, 20.0)
        p.Teff_exhaustion_factor = np.clip(rng.normal(0.15, 0.05), 0.0, 0.35)

        # HLA risk: 0.6-1.6 (some have more aggressive HLA)
        p.hla_risk = np.clip(rng.normal(1.0, 0.2), 0.5, 1.8)

        # Secretion efficiency: 0.3-0.9
        p.Cp_secretion_efficiency = np.clip(rng.normal(0.6, 0.15), 0.25, 0.95)

        # Replication rate: varies 2x around baseline
        p.B_replication_rate = np.clip(
            rng.lognormal(np.log(0.003), 0.3), 0.001, 0.008)

        # Autoantibodies: 10-50
        p.Ab_initial = np.clip(rng.normal(25.0, 10.0), 5.0, 60.0)

        # Run simulation
        try:
            result = simulate(p, protocol, t_years=t_years, label=f"mc_{i}")

            final_B_list.append(result['final_B'])
            final_Cp_list.append(result['final_Cp'])
            time_to_cp_list.append(result['time_to_cp_signal'])
            time_to_b20_list.append(result['time_to_b20'])
            time_to_indep_list.append(result['time_to_independence'])
            virus_cleared_list.append(result['virus_cleared'])
            permanent_remission_list.append(result['permanent_remission'])

            # Store trajectory at lower resolution for plotting
            if i < 200:
                idx = np.arange(0, len(result['B']), 7)  # weekly
                trajectories_B.append(result['B'][idx])

        except Exception as e:
            print(f"  WARNING: sample {i} failed: {e}")
            continue

    # ---- Aggregate statistics ----
    final_B = np.array(final_B_list)
    final_Cp = np.array(final_Cp_list)
    n_success = len(final_B)

    # C-peptide improvement (>0.2 nmol/L)
    n_cp_improved = sum(1 for cp in final_Cp if cp > 0.20)
    # Significant beta cell recovery (>15%)
    n_b15 = sum(1 for b in final_B if b > 0.15)
    # Insulin independence (>30% effective)
    n_indep = sum(1 for b in final_B if b > 0.30)
    # Full remission
    n_remission = sum(1 for r in permanent_remission_list if r)
    # Virus cleared
    n_virus_clear = sum(1 for v in virus_cleared_list if v)

    # Time-to-event statistics
    valid_cp_times = [t for t in time_to_cp_list if t is not None]
    valid_b20_times = [t for t in time_to_b20_list if t is not None]
    valid_indep_times = [t for t in time_to_indep_list if t is not None]

    print(f"\n  === MONTE CARLO RESULTS ({n_success} valid samples) ===")
    print(f"  Final beta cell mass:")
    print(f"    Mean:   {np.mean(final_B)*100:.1f}%")
    print(f"    Median: {np.median(final_B)*100:.1f}%")
    print(f"    5th:    {np.percentile(final_B, 5)*100:.1f}%")
    print(f"    95th:   {np.percentile(final_B, 95)*100:.1f}%")
    print(f"  Final C-peptide:")
    print(f"    Mean:   {np.mean(final_Cp):.3f} nmol/L")
    print(f"    Median: {np.median(final_Cp):.3f} nmol/L")
    print(f"  Outcomes at {t_years:.0f} years:")
    print(f"    C-peptide improved (>0.2): {n_cp_improved}/{n_success} ({100*n_cp_improved/n_success:.0f}%)")
    print(f"    Beta cells > 15%:          {n_b15}/{n_success} ({100*n_b15/n_success:.0f}%)")
    print(f"    Insulin independence:       {n_indep}/{n_success} ({100*n_indep/n_success:.0f}%)")
    print(f"    Permanent remission:        {n_remission}/{n_success} ({100*n_remission/n_success:.0f}%)")
    print(f"    Virus cleared:              {n_virus_clear}/{n_success} ({100*n_virus_clear/n_success:.0f}%)")
    if valid_cp_times:
        print(f"  Time to C-peptide signal:")
        print(f"    Median: {np.median(valid_cp_times):.1f} yr")
        print(f"    Range:  {np.min(valid_cp_times):.1f} - {np.max(valid_cp_times):.1f} yr")
    if valid_indep_times:
        print(f"  Time to insulin independence:")
        print(f"    Median: {np.median(valid_indep_times):.1f} yr")
        print(f"    Range:  {np.min(valid_indep_times):.1f} - {np.max(valid_indep_times):.1f} yr")

    return {
        "n_samples": n_success,
        "final_B": final_B,
        "final_Cp": final_Cp,
        "time_to_cp": time_to_cp_list,
        "time_to_b20": time_to_b20_list,
        "time_to_independence": time_to_indep_list,
        "virus_cleared_frac": n_virus_clear / max(n_success, 1),
        "cp_improved_frac": n_cp_improved / max(n_success, 1),
        "b15_frac": n_b15 / max(n_success, 1),
        "independence_frac": n_indep / max(n_success, 1),
        "remission_frac": n_remission / max(n_success, 1),
        "trajectories_B": trajectories_B,
    }


# =============================================================================
# VISUALIZATION
# =============================================================================

def plot_scenario_comparison(results: List[dict], filename: str = "beta_cell_dynamics_comparison.png"):
    """Plot comparison of multiple scenarios."""
    fig = plt.figure(figsize=(18, 14))
    gs = GridSpec(3, 3, figure=fig, hspace=0.35, wspace=0.30)

    colors_list = ['#c0392b', '#2980b9', '#27ae60', '#8e44ad', '#e67e22']

    # 1. Beta cell mass trajectory
    ax1 = fig.add_subplot(gs[0, 0])
    for i, r in enumerate(results):
        ax1.plot(r['t_years'], r['B'] * 100, color=colors_list[i % len(colors_list)],
                 label=r['label'], linewidth=2)
    ax1.axhline(y=30, color='gray', linestyle='--', alpha=0.5, label='Insulin independence threshold')
    ax1.axhline(y=10, color='gray', linestyle=':', alpha=0.5, label='Minimum functional mass')
    ax1.set_xlabel('Years')
    ax1.set_ylabel('Beta cell mass (% normal)')
    ax1.set_title('Functional Beta Cell Mass')
    ax1.legend(fontsize=7, loc='upper left')
    ax1.set_ylim(bottom=0)
    ax1.grid(True, alpha=0.3)

    # 2. C-peptide trajectory
    ax2 = fig.add_subplot(gs[0, 1])
    for i, r in enumerate(results):
        ax2.plot(r['t_years'], r['Cp_ss'], color=colors_list[i % len(colors_list)],
                 label=r['label'], linewidth=2)
    ax2.axhline(y=0.2, color='gray', linestyle='--', alpha=0.5, label='Detectable threshold')
    ax2.axhline(y=0.6, color='gray', linestyle=':', alpha=0.5, label='Clinically significant')
    ax2.set_xlabel('Years')
    ax2.set_ylabel('C-peptide (nmol/L)')
    ax2.set_title('C-peptide (Steady-State)')
    ax2.legend(fontsize=7)
    ax2.set_ylim(bottom=0)
    ax2.grid(True, alpha=0.3)

    # 3. T effector cells
    ax3 = fig.add_subplot(gs[0, 2])
    for i, r in enumerate(results):
        ax3.plot(r['t_years'], r['Teff'], color=colors_list[i % len(colors_list)],
                 label=r['label'], linewidth=2)
    ax3.set_xlabel('Years')
    ax3.set_ylabel('Teff activity')
    ax3.set_title('Autoreactive CD8+ T Cells')
    ax3.legend(fontsize=7)
    ax3.grid(True, alpha=0.3)

    # 4. Tregs
    ax4 = fig.add_subplot(gs[1, 0])
    for i, r in enumerate(results):
        ax4.plot(r['t_years'], r['Treg'], color=colors_list[i % len(colors_list)],
                 label=r['label'], linewidth=2)
    ax4.axhline(y=22, color='gray', linestyle='--', alpha=0.5, label='Healthy homeostatic')
    ax4.set_xlabel('Years')
    ax4.set_ylabel('Treg activity')
    ax4.set_title('Regulatory T Cells')
    ax4.legend(fontsize=7)
    ax4.grid(True, alpha=0.3)

    # 5. Viral load
    ax5 = fig.add_subplot(gs[1, 1])
    for i, r in enumerate(results):
        ax5.plot(r['t_years'], r['V'], color=colors_list[i % len(colors_list)],
                 label=r['label'], linewidth=2)
    ax5.set_xlabel('Years')
    ax5.set_ylabel('Replicating virus')
    ax5.set_title('CVB Viral Load')
    ax5.legend(fontsize=7)
    ax5.grid(True, alpha=0.3)

    # 6. TD mutants
    ax6 = fig.add_subplot(gs[1, 2])
    for i, r in enumerate(results):
        ax6.plot(r['t_years'], r['TD'], color=colors_list[i % len(colors_list)],
                 label=r['label'], linewidth=2)
    ax6.set_xlabel('Years')
    ax6.set_ylabel('TD mutant population')
    ax6.set_title('5\'-Terminal Deleted Mutants')
    ax6.legend(fontsize=7)
    ax6.grid(True, alpha=0.3)

    # 7. R - D trajectory (net beta cell change rate)
    ax7 = fig.add_subplot(gs[2, 0])
    for i, r in enumerate(results):
        ax7.plot(r['t_years'], r['R_smooth'] * 1e4,
                 color=colors_list[i % len(colors_list)],
                 label=r['label'], linewidth=1.5, alpha=0.8)
    ax7.axhline(y=0, color='black', linewidth=1)
    ax7.set_xlabel('Years')
    ax7.set_ylabel('dB/dt (x10^-4 /day)')
    ax7.set_title('Net Beta Cell Change Rate (R - D)')
    ax7.legend(fontsize=7)
    ax7.grid(True, alpha=0.3)

    # 8. Autoantibodies
    ax8 = fig.add_subplot(gs[2, 1])
    for i, r in enumerate(results):
        ax8.plot(r['t_years'], r['Ab'], color=colors_list[i % len(colors_list)],
                 label=r['label'], linewidth=2)
    ax8.set_xlabel('Years')
    ax8.set_ylabel('Autoantibody titer')
    ax8.set_title('Autoantibodies (Composite)')
    ax8.legend(fontsize=7)
    ax8.grid(True, alpha=0.3)

    # 9. Total vs functional beta cells
    ax9 = fig.add_subplot(gs[2, 2])
    for i, r in enumerate(results):
        ax9.plot(r['t_years'], r['B'] * 100, color=colors_list[i % len(colors_list)],
                 label=f'{r["label"]} (functional)', linewidth=2)
        ax9.plot(r['t_years'], r['B_total'] * 100, color=colors_list[i % len(colors_list)],
                 linewidth=1, linestyle='--', alpha=0.5)
    ax9.set_xlabel('Years')
    ax9.set_ylabel('% of normal')
    ax9.set_title('Functional vs Total (func+dormant) Beta Cells')
    ax9.legend(fontsize=6)
    ax9.grid(True, alpha=0.3)

    fig.suptitle('T1DM Beta Cell Dynamics: the patient — Protocol Comparison',
                 fontsize=14, fontweight='bold', y=0.98)

    path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\n  Figure saved: {path}")


def plot_monte_carlo(mc_results: dict, filename: str = "beta_cell_monte_carlo.png"):
    """Plot Monte Carlo results."""
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))

    # 1. Final beta cell mass distribution
    ax = axes[0, 0]
    ax.hist(mc_results['final_B'] * 100, bins=50, color='#2980b9', edgecolor='white',
            alpha=0.8)
    ax.axvline(x=30, color='red', linestyle='--', label='Insulin independence')
    ax.axvline(x=np.median(mc_results['final_B']) * 100, color='orange',
               linestyle='-', linewidth=2, label=f'Median: {np.median(mc_results["final_B"])*100:.1f}%')
    ax.set_xlabel('Final beta cell mass (% normal)')
    ax.set_ylabel('Count')
    ax.set_title('Distribution of Final Beta Cell Mass')
    ax.legend(fontsize=8)

    # 2. Final C-peptide distribution
    ax = axes[0, 1]
    ax.hist(mc_results['final_Cp'], bins=50, color='#27ae60', edgecolor='white',
            alpha=0.8)
    ax.axvline(x=0.2, color='red', linestyle='--', label='Detectable')
    ax.axvline(x=0.6, color='orange', linestyle='--', label='Clinically significant')
    ax.set_xlabel('Final C-peptide (nmol/L)')
    ax.set_ylabel('Count')
    ax.set_title('Distribution of Final C-peptide')
    ax.legend(fontsize=8)

    # 3. Outcome pie chart
    ax = axes[0, 2]
    n = mc_results['n_samples']
    outcomes = {
        'Insulin independent': mc_results['independence_frac'],
        'C-peptide improved,\nnot independent': mc_results['cp_improved_frac'] - mc_results['independence_frac'],
        'No significant\nimprovement': 1.0 - mc_results['cp_improved_frac'],
    }
    # Clamp negatives
    outcomes = {k: max(v, 0) for k, v in outcomes.items()}
    if sum(outcomes.values()) > 0:
        ax.pie(outcomes.values(), labels=outcomes.keys(),
               colors=['#27ae60', '#f39c12', '#c0392b'],
               autopct='%1.0f%%', startangle=90)
    ax.set_title(f'Outcome Distribution (n={n})')

    # 4. Beta cell trajectories (spaghetti plot)
    ax = axes[1, 0]
    for traj in mc_results['trajectories_B'][:100]:
        t_weeks = np.arange(len(traj)) * 7 / 365.25
        ax.plot(t_weeks, traj * 100, color='#2980b9', alpha=0.05, linewidth=0.5)
    # Median trajectory
    min_len = min(len(t) for t in mc_results['trajectories_B'][:100])
    trimmed = np.array([t[:min_len] for t in mc_results['trajectories_B'][:100]])
    median_traj = np.median(trimmed, axis=0)
    p5_traj = np.percentile(trimmed, 5, axis=0)
    p95_traj = np.percentile(trimmed, 95, axis=0)
    t_wk = np.arange(min_len) * 7 / 365.25
    ax.plot(t_wk, median_traj * 100, color='white', linewidth=2.5)
    ax.plot(t_wk, median_traj * 100, color='#e74c3c', linewidth=2, label='Median')
    ax.fill_between(t_wk, p5_traj * 100, p95_traj * 100, alpha=0.15, color='#2980b9',
                    label='5-95th percentile')
    ax.axhline(y=30, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel('Years')
    ax.set_ylabel('Beta cell mass (% normal)')
    ax.set_title('Beta Cell Trajectories (100 samples)')
    ax.legend(fontsize=8)
    ax.set_ylim(bottom=0)
    ax.grid(True, alpha=0.3)

    # 5. Time to C-peptide signal
    ax = axes[1, 1]
    valid_times = [t for t in mc_results['time_to_cp'] if t is not None]
    if valid_times:
        ax.hist(valid_times, bins=40, color='#8e44ad', edgecolor='white', alpha=0.8)
        ax.axvline(x=np.median(valid_times), color='orange', linewidth=2,
                   label=f'Median: {np.median(valid_times):.1f} yr')
        ax.set_xlabel('Time to C-peptide > 0.2 nmol/L (years)')
        ax.set_ylabel('Count')
        ax.set_title('Time to First C-peptide Signal')
        ax.legend(fontsize=8)

    # 6. Time to insulin independence
    ax = axes[1, 2]
    valid_indep = [t for t in mc_results['time_to_independence'] if t is not None]
    if valid_indep:
        ax.hist(valid_indep, bins=40, color='#e67e22', edgecolor='white', alpha=0.8)
        ax.axvline(x=np.median(valid_indep), color='red', linewidth=2,
                   label=f'Median: {np.median(valid_indep):.1f} yr')
        ax.set_xlabel('Time to insulin independence (years)')
        ax.set_ylabel('Count')
        ax.set_title('Time to Insulin Independence')
        ax.legend(fontsize=8)
    else:
        ax.text(0.5, 0.5, 'No patients reached\ninsulin independence\nin simulation window',
                ha='center', va='center', transform=ax.transAxes, fontsize=12)
        ax.set_title('Time to Insulin Independence')

    fig.suptitle('Monte Carlo: the patient Parameter Uncertainty (Full Protocol)',
                 fontsize=13, fontweight='bold')
    plt.tight_layout()

    path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Figure saved: {path}")


# =============================================================================
# R vs D DECOMPOSITION PLOT
# =============================================================================

def plot_r_vs_d_decomposition(params: BetaCellParams, protocol: ProtocolParams,
                               filename: str = "r_vs_d_decomposition.png"):
    """
    Detailed plot showing each component of R and D over time.
    This is THE figure that proves (or disproves) the inequality reversal.
    """
    print("\n  Generating R vs D decomposition...")

    result = simulate(params, protocol, t_years=3.0, dt_output=1.0,
                      label="R_vs_D")

    # We need to recompute R and D components explicitly
    t_days = result['t_days']
    t_years = result['t_years']

    # Storage for R and D components
    n = len(t_days)
    R1 = np.zeros(n)  # replication
    R2 = np.zeros(n)  # FMD burst
    R3 = np.zeros(n)  # transdifferentiation
    R_neo = np.zeros(n)  # neogenesis
    R_rediff = np.zeros(n)  # re-differentiation
    D1 = np.zeros(n)  # CD8 killing
    D2 = np.zeros(n)  # viral cytopathic
    D3 = np.zeros(n)  # ER stress apoptosis
    D4 = np.zeros(n)  # bystander
    D_ab = np.zeros(n)  # complement

    for i in range(n):
        t = t_days[i]
        B = max(result['B'][i], 0.0)
        Bd = max(result['Bd'][i], 0.0)
        A_c = max(result['A'][i], 0.0)
        Teff = max(result['Teff'][i], 0.0)
        Treg = max(result['Treg'][i], 0.0)
        V = max(result['V'][i], 0.0)
        TD = max(result['TD'][i], 0.0)
        Ab = max(result['Ab'][i], 0.0)

        p = params
        pr = protocol

        # Check states
        fluox_on = t >= pr.fluoxetine_start_day
        vitd_on = t >= pr.vitamin_d_start_day
        buty_on = t >= pr.butyrate_start_day
        gaba_on = t >= pr.gaba_start_day
        sema_on = t >= pr.semaglutide_start_day
        bhb_on = t >= pr.bhb_start_day
        is_fasting, is_refeeding, _ = fmd_state(t, pr)

        # Stress
        met_stress = p.metabolic_stress_base / max(B + 0.5 * Bd, 0.01) * 0.30
        if is_fasting:
            met_stress *= (1.0 - pr.fmd_stress_reduction)
        if sema_on:
            met_stress *= (1.0 - pr.semaglutide_glucagon_suppression)

        td_stress = p.TD_stress_per_unit * TD
        vir_stress = p.er_stress_sensitivity * 0.005 * V
        cyt_stress = 0.002 * Teff
        total_stress = met_stress + td_stress + vir_stress + cyt_stress

        stress_penalty = 1.0 / (1.0 + 0.8 * total_stress)

        # R components
        R1[i] = p.B_replication_rate * B * stress_penalty * (1.0 - B - Bd)
        if sema_on:
            R1[i] *= pr.semaglutide_proliferative

        R2[i] = 0.0
        if is_refeeding:
            R2[i] = pr.fmd_regen_burst * p.B_neogenesis_rate * (1.0 - B - Bd) * stress_penalty

        R3[i] = 0.0
        if gaba_on:
            R3[i] = pr.gaba_transdiff_rate * A_c * (1.0 - B - Bd)

        R_neo[i] = p.B_neogenesis_rate * stress_penalty * (1.0 - B - Bd)
        R_rediff[i] = p.B_rediff_rate * Bd * stress_penalty

        # D components
        treg_frac = Treg / (Treg + Teff + 1.0)
        eff_teff = Teff * (1.0 - p.Treg_suppression_efficacy * treg_frac)
        eff_teff = max(eff_teff, 0.0)

        antiap = 1.0
        if bhb_on:
            antiap -= pr.bhb_antiapoptotic
        if gaba_on:
            antiap -= pr.gaba_antiapoptotic
        if sema_on:
            antiap -= pr.semaglutide_antiapoptotic
        if is_fasting:
            antiap -= 0.10
        antiap = max(antiap, 0.3)

        vitd_f = 1.0
        if vitd_on:
            vitd_f = 1.0 - pr.vitamin_d_antiinflammatory

        D1[i] = p.Teff_killing_rate * eff_teff * B * antiap
        D2[i] = p.TD_cytopathic_rate * (TD + 2.0 * V) * B * antiap
        er_s = td_stress + vir_stress
        D3[i] = 0.0003 * er_s * B / (1.0 + 0.5 * er_s) * antiap
        D4[i] = p.cytokine_killing_rate * Teff * B * vitd_f * antiap
        D_ab[i] = p.Ab_damage_rate * Ab * B

    R_total = R1 + R2 + R3 + R_neo + R_rediff
    D_total = D1 + D2 + D3 + D4 + D_ab

    # Smooth for visualization
    kernel = np.ones(14) / 14  # 2-week smoothing
    def smooth(arr):
        if len(arr) > 14:
            return np.convolve(arr, kernel, mode='same')
        return arr

    fig, axes = plt.subplots(3, 1, figsize=(14, 12), sharex=True)

    # Panel 1: R components stacked
    ax = axes[0]
    ax.fill_between(t_years, 0, smooth(R1) * 1e4, alpha=0.6, color='#2ecc71', label='R1: Replication')
    ax.fill_between(t_years, smooth(R1) * 1e4, smooth(R1 + R_neo) * 1e4,
                    alpha=0.6, color='#3498db', label='R: Neogenesis')
    ax.fill_between(t_years, smooth(R1 + R_neo) * 1e4,
                    smooth(R1 + R_neo + R_rediff) * 1e4,
                    alpha=0.6, color='#9b59b6', label='R: Redifferentiation')
    ax.fill_between(t_years, smooth(R1 + R_neo + R_rediff) * 1e4,
                    smooth(R1 + R_neo + R_rediff + R3) * 1e4,
                    alpha=0.6, color='#e67e22', label='R3: GABA transdiff')
    # FMD bursts (spiky, show separately)
    ax.plot(t_years, smooth(R2) * 1e4, color='#e74c3c', linewidth=1.5,
            label='R2: FMD refeeding burst', alpha=0.8)
    ax.set_ylabel('Regeneration rate (x10^-4 /day)')
    ax.set_title('REGENERATION Components (R)')
    ax.legend(fontsize=8, loc='upper left')
    ax.grid(True, alpha=0.3)

    # Panel 2: D components stacked
    ax = axes[1]
    ax.fill_between(t_years, 0, smooth(D1) * 1e4, alpha=0.6, color='#c0392b', label='D1: CD8+ T cell killing')
    ax.fill_between(t_years, smooth(D1) * 1e4, smooth(D1 + D4) * 1e4,
                    alpha=0.6, color='#e74c3c', label='D4: Bystander (cytokines)')
    ax.fill_between(t_years, smooth(D1 + D4) * 1e4, smooth(D1 + D4 + D2) * 1e4,
                    alpha=0.6, color='#d35400', label='D2: CVB cytopathic')
    ax.fill_between(t_years, smooth(D1 + D4 + D2) * 1e4,
                    smooth(D1 + D4 + D2 + D3) * 1e4,
                    alpha=0.6, color='#8e44ad', label='D3: ER stress apoptosis')
    ax.fill_between(t_years, smooth(D1 + D4 + D2 + D3) * 1e4,
                    smooth(D_total) * 1e4,
                    alpha=0.6, color='#7f8c8d', label='D: Complement')
    ax.set_ylabel('Destruction rate (x10^-4 /day)')
    ax.set_title('DESTRUCTION Components (D)')
    ax.legend(fontsize=8, loc='upper right')
    ax.grid(True, alpha=0.3)

    # Panel 3: R - D = the inequality
    ax = axes[2]
    net = smooth(R_total - D_total) * 1e4
    ax.fill_between(t_years, 0, net, where=net >= 0, alpha=0.5, color='#27ae60',
                    label='R > D (growth)')
    ax.fill_between(t_years, 0, net, where=net < 0, alpha=0.5, color='#c0392b',
                    label='D > R (decline)')
    ax.axhline(y=0, color='black', linewidth=1.5)
    ax.set_xlabel('Years')
    ax.set_ylabel('R - D (x10^-4 /day)')
    ax.set_title('THE INEQUALITY: dB/dt = R - D')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    # Add phase annotations
    for ax in axes:
        ax.axvline(x=90/365.25, color='gray', linestyle=':', alpha=0.4)
        ax.axvline(x=180/365.25, color='gray', linestyle=':', alpha=0.4)
        ax.axvline(x=365/365.25, color='gray', linestyle=':', alpha=0.4)
    axes[0].text(45/365.25, axes[0].get_ylim()[1]*0.9, 'Phase 1', ha='center', fontsize=8, color='gray')
    axes[0].text(135/365.25, axes[0].get_ylim()[1]*0.9, 'Phase 2', ha='center', fontsize=8, color='gray')
    axes[0].text(270/365.25, axes[0].get_ylim()[1]*0.9, 'Phase 3', ha='center', fontsize=8, color='gray')

    fig.suptitle('R vs D Decomposition: the patient Full Protocol',
                 fontsize=14, fontweight='bold')
    plt.tight_layout()

    path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Figure saved: {path}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 72)
    print("T1DM BETA CELL DYNAMICS — THE CORE MODEL")
    print("systematic approach | ODD Instance (numerics)")
    print("dB/dt = R - D | When R > D permanently, the patient is cured.")
    print("=" * 72)

    # ---- Run scenarios ----
    result_none = scenario_no_intervention()
    result_p1 = scenario_phase1_only()
    result_full = scenario_full_protocol()
    result_tepl = scenario_with_teplizumab()

    # ---- Compare scenarios ----
    plot_scenario_comparison(
        [result_none, result_p1, result_full, result_tepl],
        filename="beta_cell_dynamics_comparison.png"
    )

    # ---- R vs D decomposition for full protocol ----
    plot_r_vs_d_decomposition(
        patient_zero_params(), ProtocolParams(),
        filename="r_vs_d_decomposition.png"
    )

    # ---- Monte Carlo ----
    mc = monte_carlo_patient_zero(n_samples=2000, t_years=3.0)
    plot_monte_carlo(mc, filename="beta_cell_monte_carlo.png")

    # ---- Summary table ----
    print("\n" + "=" * 72)
    print("SUMMARY: the patient PREDICTED OUTCOMES")
    print("=" * 72)
    scenarios = [
        ("No intervention", result_none),
        ("Phase 1 only (reduce D)", result_p1),
        ("Full protocol (Phases 1-3)", result_full),
        ("Full + teplizumab", result_tepl),
    ]

    header = f"{'Scenario':<30} {'B_final':>8} {'Cp_final':>9} {'Teff':>6} {'Treg':>6} {'V':>6} {'TD':>6} {'Remission':>10}"
    print(header)
    print("-" * len(header))
    for name, r in scenarios:
        print(f"{name:<30} {r['final_B']*100:>7.2f}% {r['final_Cp']:>8.3f} "
              f"{r['final_Teff']:>6.1f} {r['final_Treg']:>6.1f} "
              f"{r['final_V']:>6.2f} {r['final_TD']:>6.1f} "
              f"{'YES' if r['permanent_remission'] else 'NO':>10}")

    print(f"\nMonte Carlo ({mc['n_samples']} samples, full protocol):")
    print(f"  Probability of C-peptide improvement:  {mc['cp_improved_frac']*100:.0f}%")
    print(f"  Probability of insulin independence:    {mc['independence_frac']*100:.0f}%")
    print(f"  Probability of permanent remission:     {mc['remission_frac']*100:.0f}%")

    print("\nDone. All figures saved to:", OUTPUT_DIR)


if __name__ == "__main__":
    main()
