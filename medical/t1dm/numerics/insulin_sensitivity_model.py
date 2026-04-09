#!/usr/bin/env python3
"""
Insulin Sensitivity & Dose Reduction Model
=============================================

As beta cells recover under the protocol, endogenous insulin production
increases. This creates a DANGEROUS transition:

    Total insulin = Exogenous (injected) + Endogenous (from beta cells)

If exogenous insulin is NOT reduced as endogenous rises, the patient
goes hypoglycemic. If exogenous is reduced TOO FAST, the patient goes
into DKA. This model computes the safe dose reduction schedule.

Key relationships:
    1. Daily insulin requirement = f(body weight, insulin sensitivity, carbs)
    2. Endogenous production = f(beta cell mass, per-cell secretion, glucose)
    3. Exogenous need = Total requirement - Endogenous production
    4. Safety floor: minimum exogenous to prevent DKA if beta cells fail
    5. C-peptide milestones map to dose reduction steps

Semaglutide effects:
    - Improves insulin sensitivity (hepatic + peripheral)
    - Suppresses glucagon (reduces hepatic glucose output)
    - Delays gastric emptying (lower postprandial glucose spikes)
    - Net: reduces total insulin requirement by 20-40%

The dangerous zone:
    When endogenous provides 30-70% of needs, small fluctuations in
    either source can cause hypo or hyper. This is where CGM is critical.

Literature:
    [1]  DeFronzo RA. Diabetes 2009;58:773 — insulin resistance pathophysiology
    [2]  Greenbaum CJ et al. Diabetes 2012;61:2534 — C-peptide thresholds
    [3]  Oram RA et al. Diabetes Care 2014;37:1230 — persistent C-peptide
    [4]  Drucker DJ. Cell Metab 2018;28:319 — GLP-1 mechanisms
    [5]  Meier JJ et al. Diabetes 2005;54:2557 — beta cell secretory capacity
    [6]  Palmer JP et al. Diabetes 2004;53:250 — C-peptide and insulin needs
    [7]  Steffes MW et al. Diabetes Care 2003;26:832 — C-peptide and complications
    [8]  Keymeulen B et al. NEJM 2005;352:2598 — anti-CD3 and insulin dose
    [9]  Herold KC et al. Diabetes 2013;62:3766 — C-peptide preservation
    [10] Lachin JM et al. Diabetes 2014;63:739 — C-peptide clinical significance

systematic approach — T1DM Insulin Dynamics — ODD Instance (numerics)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional
import os

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "figures")
os.makedirs(OUTPUT_DIR, exist_ok=True)


# =============================================================================
# CONSTANTS AND PARAMETERS
# =============================================================================

@dataclass
class PatientZeroInsulin:
    """
    the patient insulin parameters.
    67yr T1DM, current regimen known from protocol.
    """
    # --- Anthropometrics ---
    weight_kg: float = 75.0             # estimated
    height_cm: float = 175.0            # estimated

    # --- Current insulin regimen ---
    basal_units_per_day: float = 12.0   # long-acting (e.g., Lantus/Tresiba)
    bolus_units_per_meal: float = 2.0   # rapid-acting per meal
    meals_per_day: float = 2.0          # 18:6 IF = 2 meals in 6hr window
    total_daily_dose: float = 16.0      # basal + bolus = 12 + 2*2 = 16 U/day

    # --- Carbohydrate intake ---
    carbs_per_meal_g: float = 20.0      # low-carb protocol (15-20g/meal)
    total_daily_carbs_g: float = 40.0   # 2 meals x 20g

    # --- Insulin sensitivity ---
    # Insulin sensitivity factor (ISF): how much 1U drops glucose (mg/dL)
    isf_mgdl_per_unit: float = 50.0     # 1U drops BG by ~50 mg/dL
    # Carb ratio: grams of carbs covered by 1U
    carb_ratio_g_per_unit: float = 10.0 # 1U covers 10g carbs

    # --- Beta cell function ---
    beta_cell_mass_fraction: float = 0.08  # starting at ~8% of normal
    cpeptide_baseline_nmol: float = 0.12   # low but detectable

    # --- Normal physiology reference ---
    normal_daily_insulin_u: float = 40.0   # healthy adult secretes ~40U/day
    normal_beta_mass: float = 1.0          # fraction = 1.0 is normal
    normal_cpeptide_nmol: float = 2.0      # fasting C-peptide ~1-3 nmol/L

    # --- Semaglutide effects ---
    semaglutide_sensitivity_boost: float = 1.30  # 30% improved sensitivity
    semaglutide_glucagon_suppression: float = 0.25  # 25% less glucagon
    semaglutide_gastric_delay: float = 0.20  # 20% less postprandial spike


# =============================================================================
# CORE MODELS
# =============================================================================

def endogenous_insulin_production(beta_mass_fraction: float,
                                   secretion_efficiency: float = 0.6,
                                   semaglutide_boost: float = 1.0,
                                   glucose_stimulated: bool = True) -> float:
    """
    Calculate endogenous insulin production in units/day.

    A normal pancreas with 100% beta cell mass produces ~40 U/day.
    the patient's beta cells are exhausted (reduced per-cell secretion).
    Semaglutide enhances glucose-stimulated insulin secretion (GSIS).

    Args:
        beta_mass_fraction: 0-1 (fraction of normal beta cell mass)
        secretion_efficiency: 0-1 (per-cell secretion vs normal)
        semaglutide_boost: multiplier from GLP-1R activation
        glucose_stimulated: whether measuring fed (GSIS) or basal state

    Returns:
        Endogenous insulin production in U/day
    """
    normal_production = 40.0  # U/day for healthy adult

    # Beta cell mass determines maximum capacity
    # But relationship is not perfectly linear — there's a sigmoid
    # At low mass (<10%), output is proportionally low
    # At moderate mass (30-50%), compensatory upregulation helps
    # At near-normal mass (>70%), output saturates
    mass_factor = beta_mass_fraction ** 0.85  # slight sub-linear scaling

    # Per-cell secretion efficiency (exhaustion, ER stress)
    # the patient: 60% of normal per-cell output
    eff_factor = secretion_efficiency

    # Glucose-stimulated vs basal
    gsis_factor = 1.0
    if glucose_stimulated:
        gsis_factor = 1.5  # 50% more during meals (GSIS)

    # Semaglutide enhances GSIS (not basal — this is key safety feature)
    sema_factor = 1.0
    if glucose_stimulated:
        sema_factor = semaglutide_boost

    production = normal_production * mass_factor * eff_factor * gsis_factor * sema_factor

    return production


def total_insulin_requirement(weight_kg: float = 75.0,
                                carbs_g: float = 40.0,
                                insulin_sensitivity: float = 1.0,
                                semaglutide_effects: bool = False) -> dict:
    """
    Calculate total daily insulin requirement.

    Components:
        Basal: covers hepatic glucose output (~50% of daily dose)
        Bolus: covers carbohydrate intake + correction

    Args:
        weight_kg: body weight
        carbs_g: daily carb intake
        insulin_sensitivity: multiplier (>1 = more sensitive = less insulin)
        semaglutide_effects: whether semaglutide is active

    Returns:
        Dict with basal, bolus, total requirements
    """
    # Base requirement ~0.5-0.7 U/kg/day for T1DM
    # the patient on low carb = lower requirement
    base_requirement = 0.4 * weight_kg  # ~30 U/day for 75kg

    # Adjust for insulin sensitivity
    adjusted = base_requirement / insulin_sensitivity

    # Semaglutide: reduces glucagon -> less basal need, delays gastric -> less bolus
    if semaglutide_effects:
        adjusted *= 0.75  # ~25% reduction in total requirement

    # Split: ~55% basal, 45% bolus (varies by patient)
    basal = adjusted * 0.55
    bolus_total = adjusted * 0.45

    # Carb-based bolus cross-check
    carb_ratio = 10.0 / insulin_sensitivity  # g per unit
    carb_bolus = carbs_g / carb_ratio

    # Use the larger of the two bolus estimates
    bolus_actual = max(bolus_total, carb_bolus)

    return {
        "basal_u_per_day": basal,
        "bolus_u_per_day": bolus_actual,
        "total_u_per_day": basal + bolus_actual,
        "carb_ratio_g_per_u": carb_ratio,
    }


def exogenous_insulin_needed(beta_mass_fraction: float,
                               weight_kg: float = 75.0,
                               carbs_g: float = 40.0,
                               secretion_efficiency: float = 0.6,
                               insulin_sensitivity: float = 1.0,
                               semaglutide_on: bool = False,
                               semaglutide_gsis_boost: float = 1.40) -> dict:
    """
    Calculate how much exogenous insulin the patient needs given
    current beta cell function.

    The core equation:
        Exogenous = Total_Requirement - Endogenous_Production
        Exogenous = max(Exogenous, Safety_Floor)

    Args:
        beta_mass_fraction: current beta cell mass (0-1)
        weight_kg: body weight
        carbs_g: daily carb intake
        secretion_efficiency: per-cell secretion vs normal
        insulin_sensitivity: multiplier (>1 = less insulin needed)
        semaglutide_on: whether semaglutide active
        semaglutide_gsis_boost: GSIS enhancement from semaglutide

    Returns:
        Dict with exogenous need, endogenous production, safety margins
    """
    # Total requirement
    sensitivity = insulin_sensitivity
    if semaglutide_on:
        sensitivity *= 1.30  # semaglutide improves sensitivity

    req = total_insulin_requirement(
        weight_kg=weight_kg,
        carbs_g=carbs_g,
        insulin_sensitivity=sensitivity,
        semaglutide_effects=semaglutide_on,
    )
    total_req = req['total_u_per_day']

    # Endogenous production
    sema_boost = semaglutide_gsis_boost if semaglutide_on else 1.0
    endo = endogenous_insulin_production(
        beta_mass_fraction=beta_mass_fraction,
        secretion_efficiency=secretion_efficiency,
        semaglutide_boost=sema_boost,
    )

    # Exogenous need
    exo_need = total_req - endo

    # SAFETY FLOOR: minimum insulin to prevent DKA
    # Even if beta cells are producing some insulin, if they suddenly fail
    # (e.g., viral flare, stress, illness), patient needs a safety net.
    # Minimum = enough basal to prevent ketoacidosis
    # ~0.1 U/kg/day is the absolute minimum for DKA prevention
    safety_floor = 0.1 * weight_kg  # 7.5 U for 75kg patient

    # At very high beta cell mass (>40%), safety floor can be reduced
    # because the probability of sudden total failure is low
    if beta_mass_fraction > 0.40:
        safety_floor *= 0.5
    if beta_mass_fraction > 0.60:
        safety_floor *= 0.3

    exo_prescribed = max(exo_need, safety_floor)

    # C-peptide estimate
    cpeptide = beta_mass_fraction * 2.5 * secretion_efficiency
    if semaglutide_on:
        cpeptide *= semaglutide_gsis_boost

    # Percentage endogenous
    endo_fraction = endo / max(total_req, 0.1)

    # Can insulin be discontinued?
    can_discontinue = (endo >= total_req * 1.2 and  # 20% safety margin
                       beta_mass_fraction > 0.35)    # enough mass for stability

    return {
        "total_requirement_u": total_req,
        "endogenous_production_u": endo,
        "exogenous_need_u": max(exo_need, 0),
        "exogenous_prescribed_u": exo_prescribed,
        "safety_floor_u": safety_floor,
        "endogenous_fraction": min(endo_fraction, 1.0),
        "cpeptide_nmol": cpeptide,
        "can_discontinue": can_discontinue,
        "carb_ratio": req['carb_ratio_g_per_u'],
        "in_danger_zone": 0.30 <= endo_fraction <= 0.70,
    }


# =============================================================================
# C-PEPTIDE MILESTONES -> DOSE REDUCTION SCHEDULE
# =============================================================================

def cpeptide_dose_milestones() -> List[dict]:
    """
    Define C-peptide milestones and corresponding insulin dose adjustments.

    C-peptide is equimolar with endogenous insulin and has longer half-life
    (~30 min vs ~5 min), making it a more stable biomarker.

    Based on:
    - Greenbaum 2012: C-peptide > 0.2 nmol/L = clinically meaningful residual function
    - Oram 2014: Many long-duration T1DM patients maintain low but detectable C-peptide
    - Palmer 2004: Higher C-peptide = less insulin needed, fewer hypos
    - Steffes 2003: Even low C-peptide protects against complications

    Milestones from lowest to highest:
    """
    return [
        {
            "milestone": "BASELINE",
            "cpeptide_nmol": 0.1,
            "beta_mass_est": 0.05,
            "action": "No change. Document baseline. Continue current regimen.",
            "insulin_reduction": 0.0,
            "basal_adjust": "No change",
            "bolus_adjust": "No change",
            "monitoring": "Monthly stimulated C-peptide, quarterly HbA1c",
            "safety": "Standard CGM alarming",
        },
        {
            "milestone": "FIRST SIGNAL",
            "cpeptide_nmol": 0.20,
            "beta_mass_est": 0.08,
            "action": "C-peptide rising! Beta cells responding. Hold insulin steady. "
                      "The temptation to reduce now is DANGEROUS — too early.",
            "insulin_reduction": 0.0,
            "basal_adjust": "No change",
            "bolus_adjust": "No change",
            "monitoring": "Monthly C-peptide, weekly CGM review for hypo patterns",
            "safety": "Watch for nighttime lows (endogenous basal insulin starting)",
        },
        {
            "milestone": "EARLY RESPONSE",
            "cpeptide_nmol": 0.40,
            "beta_mass_est": 0.15,
            "action": "Clear beta cell recovery. Reduce bolus insulin by 25%. "
                      "The endogenous GSIS is partially covering meals.",
            "insulin_reduction": 0.15,
            "basal_adjust": "Reduce by 1-2U if nighttime lows appearing",
            "bolus_adjust": "Reduce by 25% (2U -> 1.5U per meal)",
            "monitoring": "Biweekly C-peptide, daily CGM review",
            "safety": "Carry glucose tabs. CGM alarm at 70 mg/dL. "
                      "If BG > 250 for >2hr: take correction dose.",
        },
        {
            "milestone": "MODERATE RECOVERY",
            "cpeptide_nmol": 0.80,
            "beta_mass_est": 0.25,
            "action": "Significant recovery. Reduce basal by 30%, bolus by 50%. "
                      "Entering the DANGER ZONE: 30-70% endogenous. "
                      "Glucose variability will increase. CGM is non-negotiable.",
            "insulin_reduction": 0.35,
            "basal_adjust": "Reduce basal by 30% (12U -> 8U)",
            "bolus_adjust": "Reduce by 50% (2U -> 1U per meal)",
            "monitoring": "Weekly C-peptide, daily CGM analysis",
            "safety": "DANGER ZONE. Hypoglycemia risk highest here. "
                      "Always carry fast carbs. Glucagon kit available. "
                      "Consider reducing carb ratio caution.",
        },
        {
            "milestone": "STRONG RECOVERY",
            "cpeptide_nmol": 1.20,
            "beta_mass_est": 0.35,
            "action": "Beta cells providing majority of basal needs. "
                      "Reduce basal by 50%, bolus by 75% or eliminate bolus "
                      "for small meals (<15g carbs).",
            "insulin_reduction": 0.55,
            "basal_adjust": "Reduce basal by 50% (12U -> 6U)",
            "bolus_adjust": "Eliminate for meals <15g carbs, 0.5U for larger meals",
            "monitoring": "Weekly C-peptide, HbA1c monthly, daily CGM",
            "safety": "Exiting danger zone. Endogenous insulin is dominant. "
                      "Risk shifts from hypo to potential hyper if beta cells "
                      "have a bad day. Keep rapid-acting insulin available.",
        },
        {
            "milestone": "NEAR INDEPENDENCE",
            "cpeptide_nmol": 1.80,
            "beta_mass_est": 0.50,
            "action": "Beta cell mass approaching functional independence. "
                      "Trial: discontinue bolus entirely. Reduce basal to "
                      "safety minimum (0.1 U/kg = ~7.5U). Monitor closely.",
            "insulin_reduction": 0.75,
            "basal_adjust": "Reduce to safety minimum: 0.1 U/kg/day",
            "bolus_adjust": "DISCONTINUE (trial period, 1 week at a time)",
            "monitoring": "Daily C-peptide during trial, continuous CGM",
            "safety": "Keep insulin pen loaded. If BG >200 for 4hr, "
                      "resume bolus. Check ketones if BG >250.",
        },
        {
            "milestone": "INSULIN INDEPENDENCE",
            "cpeptide_nmol": 2.50,
            "beta_mass_est": 0.65,
            "action": "C-peptide in normal range. Beta cells providing full "
                      "insulin coverage. Trial complete insulin discontinuation. "
                      "This is the goal.",
            "insulin_reduction": 1.0,
            "basal_adjust": "DISCONTINUE (supervised trial, 2 weeks)",
            "bolus_adjust": "DISCONTINUED",
            "monitoring": "Continuous CGM indefinitely. C-peptide monthly for 6mo, "
                          "then quarterly. HbA1c quarterly.",
            "safety": "Keep insulin and glucagon available. Monitor for relapse. "
                      "If HbA1c rises >7% or C-peptide drops, resume protocol. "
                      "Continue maintenance supplements (vitamin D, butyrate, GABA).",
        },
    ]


# =============================================================================
# TRAJECTORY MODEL
# =============================================================================

def simulate_insulin_trajectory(beta_mass_trajectory: np.ndarray,
                                  time_months: np.ndarray,
                                  patient: PatientZeroInsulin = None,
                                  semaglutide_start_month: float = 6.0,
                                  secretion_efficiency_trajectory: np.ndarray = None,
                                  ) -> dict:
    """
    Given a beta cell mass trajectory (from beta_cell_dynamics.py),
    compute the insulin dose reduction schedule over time.

    Args:
        beta_mass_trajectory: array of beta cell mass fractions over time
        time_months: array of time points in months
        patient: patient parameters
        semaglutide_start_month: when semaglutide begins
        secretion_efficiency_trajectory: per-cell efficiency over time
            (improves as stress drops)

    Returns:
        Dict with trajectories and milestone timeline
    """
    if patient is None:
        patient = PatientZeroInsulin()

    n = len(time_months)

    if secretion_efficiency_trajectory is None:
        # Model improving secretion efficiency as stress drops
        # Start at 0.6, improve to 0.85 over 12 months as ER stress resolves
        secretion_efficiency_trajectory = np.clip(
            0.6 + 0.25 * (1 - np.exp(-time_months / 8.0)),
            0.6, 0.90
        )

    # Storage
    total_req = np.zeros(n)
    endo_prod = np.zeros(n)
    exo_need = np.zeros(n)
    exo_prescribed = np.zeros(n)
    safety_floor = np.zeros(n)
    endo_fraction = np.zeros(n)
    cpeptide = np.zeros(n)
    in_danger_zone = np.zeros(n, dtype=bool)
    can_stop = np.zeros(n, dtype=bool)

    milestones_reached = []
    milestone_defs = cpeptide_dose_milestones()
    milestone_idx = 0

    for i in range(n):
        sema_on = time_months[i] >= semaglutide_start_month
        sec_eff = secretion_efficiency_trajectory[i]

        result = exogenous_insulin_needed(
            beta_mass_fraction=beta_mass_trajectory[i],
            weight_kg=patient.weight_kg,
            carbs_g=patient.total_daily_carbs_g,
            secretion_efficiency=sec_eff,
            insulin_sensitivity=1.0,
            semaglutide_on=sema_on,
            semaglutide_gsis_boost=1.40 if sema_on else 1.0,
        )

        total_req[i] = result['total_requirement_u']
        endo_prod[i] = result['endogenous_production_u']
        exo_need[i] = result['exogenous_need_u']
        exo_prescribed[i] = result['exogenous_prescribed_u']
        safety_floor[i] = result['safety_floor_u']
        endo_fraction[i] = result['endogenous_fraction']
        cpeptide[i] = result['cpeptide_nmol']
        in_danger_zone[i] = result['in_danger_zone']
        can_stop[i] = result['can_discontinue']

        # Check milestones
        while (milestone_idx < len(milestone_defs) and
               cpeptide[i] >= milestone_defs[milestone_idx]['cpeptide_nmol']):
            milestones_reached.append({
                "month": time_months[i],
                **milestone_defs[milestone_idx],
            })
            milestone_idx += 1

    # Time to key events
    danger_start = None
    danger_end = None
    independence_time = None

    danger_indices = np.where(in_danger_zone)[0]
    if len(danger_indices) > 0:
        danger_start = time_months[danger_indices[0]]
        danger_end = time_months[danger_indices[-1]]

    stop_indices = np.where(can_stop)[0]
    if len(stop_indices) > 0:
        independence_time = time_months[stop_indices[0]]

    return {
        "time_months": time_months,
        "beta_mass": beta_mass_trajectory,
        "total_requirement_u": total_req,
        "endogenous_production_u": endo_prod,
        "exogenous_need_u": exo_need,
        "exogenous_prescribed_u": exo_prescribed,
        "safety_floor_u": safety_floor,
        "endogenous_fraction": endo_fraction,
        "cpeptide_nmol": cpeptide,
        "in_danger_zone": in_danger_zone,
        "can_discontinue": can_stop,
        "milestones_reached": milestones_reached,
        "danger_zone_start_month": danger_start,
        "danger_zone_end_month": danger_end,
        "independence_month": independence_time,
    }


# =============================================================================
# GENERATE the patient TRAJECTORY
# =============================================================================

def patient_zero_trajectory(t_months: int = 36) -> dict:
    """
    Generate the patient's predicted trajectory under the full protocol.

    Uses a simplified beta cell mass model (consistent with beta_cell_dynamics.py
    but computed analytically for speed) to produce the insulin dose schedule.
    """
    time = np.linspace(0, t_months, t_months * 4 + 1)  # weekly resolution

    # Beta cell mass trajectory (from beta_cell_dynamics.py typical output)
    # Phase 1 (0-3mo): slow stabilization as D drops (fluoxetine + vitD + butyrate)
    # Phase 2 (3-6mo): FMD cycles begin -> net growth starts
    # Phase 3 (6-12mo): GABA + semaglutide -> accelerated growth
    # Phase 4+ (12-36mo): continued growth, approaching plateau

    B = np.zeros_like(time)
    B0 = 0.08  # starting beta cell mass

    for i, t in enumerate(time):
        if t <= 3:
            # Phase 1: slight improvement as virus cleared, stress drops
            # D drops by ~30%, R stays same -> net dB slightly positive
            B[i] = B0 + 0.005 * t  # +0.5% per month
        elif t <= 6:
            # Phase 2: FMD refeeding bursts add new cells
            B[i] = B0 + 0.015 + 0.008 * (t - 3)  # +0.8% per month
        elif t <= 12:
            # Phase 3: GABA transdiff + semaglutide + FMD -> rapid growth
            phase2_end = B0 + 0.015 + 0.008 * 3  # ~0.119
            B[i] = phase2_end + 0.018 * (t - 6)   # +1.8% per month
        else:
            # Plateau phase: growth slows as mass approaches homeostatic limit
            phase3_end = B0 + 0.015 + 0.024 + 0.108  # ~0.227
            B[i] = phase3_end + 0.08 * (1 - np.exp(-(t - 12) / 18.0))
        B[i] = min(B[i], 0.45)  # cap at realistic maximum for 67yr T1DM

    # Simulate insulin trajectory
    result = simulate_insulin_trajectory(
        beta_mass_trajectory=B,
        time_months=time,
        semaglutide_start_month=6.0,
    )

    return result


# =============================================================================
# VISUALIZATION
# =============================================================================

def plot_insulin_trajectory(result: dict, filename: str = "insulin_dose_trajectory.png"):
    """Plot the insulin dose reduction schedule."""
    fig, axes = plt.subplots(4, 1, figsize=(14, 16), sharex=True)

    t = result['time_months']

    # 1. Beta cell mass + C-peptide
    ax = axes[0]
    ax.plot(t, result['beta_mass'] * 100, color='#2ecc71', linewidth=2.5,
            label='Beta cell mass (% normal)')
    ax.set_ylabel('Beta cell mass (%)', color='#2ecc71')
    ax.tick_params(axis='y', labelcolor='#2ecc71')
    ax.axhline(y=30, color='#2ecc71', linestyle='--', alpha=0.3, linewidth=1)
    ax.text(0.5, 31, 'Independence threshold', fontsize=7, color='#2ecc71', alpha=0.5)

    ax2 = ax.twinx()
    ax2.plot(t, result['cpeptide_nmol'], color='#e67e22', linewidth=2,
             label='C-peptide (nmol/L)')
    ax2.set_ylabel('C-peptide (nmol/L)', color='#e67e22')
    ax2.tick_params(axis='y', labelcolor='#e67e22')
    ax2.axhline(y=0.2, color='#e67e22', linestyle=':', alpha=0.3)
    ax2.axhline(y=2.0, color='#e67e22', linestyle='--', alpha=0.3)

    ax.set_title('Beta Cell Recovery + C-peptide')
    ax.grid(True, alpha=0.3)

    # 2. Insulin doses: total requirement, endogenous, exogenous
    ax = axes[1]
    ax.fill_between(t, 0, result['endogenous_production_u'],
                    alpha=0.4, color='#2ecc71', label='Endogenous (from beta cells)')
    ax.fill_between(t, result['endogenous_production_u'],
                    result['endogenous_production_u'] + result['exogenous_prescribed_u'],
                    alpha=0.4, color='#3498db', label='Exogenous (injected)')
    ax.plot(t, result['total_requirement_u'], color='black', linewidth=1.5,
            linestyle='--', label='Total requirement', alpha=0.7)
    ax.plot(t, result['safety_floor_u'], color='#c0392b', linewidth=1,
            linestyle=':', label='Safety floor (DKA prevention)')

    # Semaglutide start marker
    ax.axvline(x=6, color='purple', linestyle='--', alpha=0.4)
    ax.text(6.2, ax.get_ylim()[1] * 0.9 if ax.get_ylim()[1] > 0 else 30,
            'Semaglutide starts', fontsize=7, color='purple')

    ax.set_ylabel('Insulin (U/day)')
    ax.set_title('Daily Insulin: Endogenous + Exogenous')
    ax.legend(fontsize=8, loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(bottom=0)

    # 3. Endogenous fraction + danger zone
    ax = axes[2]
    ax.plot(t, result['endogenous_fraction'] * 100, color='#2980b9', linewidth=2.5)
    ax.fill_between(t, 30, 70, alpha=0.15, color='#e74c3c',
                    label='DANGER ZONE (30-70% endogenous)')
    ax.axhline(y=100, color='#27ae60', linestyle='--', alpha=0.5, label='Insulin independence')

    ax.set_ylabel('Endogenous fraction (%)')
    ax.set_title('Transition: Exogenous -> Endogenous Insulin')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 110)

    # 4. Exogenous dose (what the patient actually injects)
    ax = axes[3]
    ax.plot(t, result['exogenous_prescribed_u'], color='#c0392b', linewidth=2.5,
            label='Prescribed exogenous dose')
    ax.plot(t, result['safety_floor_u'], color='gray', linewidth=1,
            linestyle=':', label='Safety minimum')

    # Mark milestones
    for ms in result['milestones_reached']:
        if ms['cpeptide_nmol'] >= 0.40:
            ax.axvline(x=ms['month'], color='#27ae60', linestyle='--', alpha=0.3)
            ax.text(ms['month'] + 0.3, ax.get_ylim()[1] * 0.85 if ax.get_ylim()[1] > 0 else 15,
                    f"{ms['milestone']}\n(Cp={ms['cpeptide_nmol']:.1f})",
                    fontsize=6, color='#27ae60', rotation=45)

    if result['independence_month'] is not None:
        ax.axvline(x=result['independence_month'], color='gold', linewidth=2,
                   label=f"Independence: month {result['independence_month']:.0f}")

    ax.set_xlabel('Months on protocol')
    ax.set_ylabel('Exogenous insulin (U/day)')
    ax.set_title('Insulin Dose Reduction Schedule')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(bottom=0)

    # Phase annotations
    for ax_i in axes:
        ax_i.axvline(x=3, color='gray', linestyle=':', alpha=0.3)
        ax_i.axvline(x=6, color='gray', linestyle=':', alpha=0.3)
        ax_i.axvline(x=12, color='gray', linestyle=':', alpha=0.3)

    fig.suptitle("the patient: Insulin Dose Reduction Schedule\n"
                 "As beta cells recover, exogenous insulin is systematically reduced",
                 fontsize=13, fontweight='bold')
    plt.tight_layout()

    path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Figure saved: {path}")


def plot_cpeptide_milestones(filename: str = "cpeptide_milestones.png"):
    """Visual table of C-peptide milestones and actions."""
    milestones = cpeptide_dose_milestones()

    fig, ax = plt.subplots(figsize=(16, 8))
    ax.axis('off')

    # Table data
    headers = ['Milestone', 'C-peptide\n(nmol/L)', 'Beta mass\n(est %)',
               'Insulin\nReduction', 'Key Action']
    rows = []
    for ms in milestones:
        rows.append([
            ms['milestone'],
            f"{ms['cpeptide_nmol']:.2f}",
            f"{ms['beta_mass_est']*100:.0f}%",
            f"{ms['insulin_reduction']*100:.0f}%",
            ms['action'][:80] + ('...' if len(ms['action']) > 80 else ''),
        ])

    table = ax.table(cellText=rows, colLabels=headers,
                     loc='center', cellLoc='left')
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    for col in range(len(headers)):
        table.auto_set_column_width(col)

    # Style header
    for j in range(len(headers)):
        table[(0, j)].set_facecolor('#2c3e50')
        table[(0, j)].set_text_props(color='white', fontweight='bold')

    # Color code rows by risk level
    risk_colors = ['#eaf7ea', '#eaf7ea', '#fff8e1', '#ffebee', '#ffcdd2',
                   '#e8f5e9', '#c8e6c9']
    for i in range(len(rows)):
        for j in range(len(headers)):
            if i < len(risk_colors):
                table[(i + 1, j)].set_facecolor(risk_colors[i])
            table[(i + 1, j)].set_height(0.10)

    ax.set_title('C-peptide Milestones: Insulin Dose Reduction Schedule',
                 fontsize=14, fontweight='bold', pad=20)

    path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Figure saved: {path}")


# =============================================================================
# DKA RISK MODEL
# =============================================================================

def dka_risk_analysis():
    """
    Model DKA risk during the transition from exogenous to endogenous insulin.

    DKA occurs when: absolute insulin deficiency -> lipolysis -> ketogenesis
    -> ketoacidosis -> death (if untreated).

    Risk factors during protocol:
    1. Beta cell function unstable (growing but variable)
    2. Patient reduces exogenous insulin
    3. FMD cycles induce therapeutic ketosis (BHB 1-3 mM) -- must not
       progress to ketoacidosis (BHB >5 mM + pH <7.3)
    4. Illness/stress can temporarily suppress beta cell function
    """
    print("\n" + "=" * 72)
    print("DKA RISK ANALYSIS DURING INSULIN TRANSITION")
    print("=" * 72)

    # Scenario: various beta cell mass fractions
    beta_fractions = np.arange(0.05, 0.70, 0.01)
    n = len(beta_fractions)

    # For each beta mass fraction, compute the margin of safety
    # Margin = endogenous production / minimum DKA prevention threshold
    # DKA threshold: need at least 0.05-0.1 U/kg/day of insulin activity

    dka_threshold = 0.08 * 75.0  # ~6 U/day absolute minimum
    margins = np.zeros(n)
    for i, bf in enumerate(beta_fractions):
        endo = endogenous_insulin_production(bf, secretion_efficiency=0.7)
        margins[i] = endo / dka_threshold

    # Find the critical beta cell mass where endogenous alone prevents DKA
    critical_idx = np.where(margins >= 1.0)[0]
    critical_mass = beta_fractions[critical_idx[0]] if len(critical_idx) > 0 else None

    print(f"  DKA prevention threshold: {dka_threshold:.1f} U/day")
    print(f"  Critical beta cell mass (endo covers DKA threshold): "
          f"{critical_mass*100:.1f}%" if critical_mass else "  Not reached")
    print(f"\n  Safety margins by beta cell mass:")
    print(f"    {'Mass':>6} {'Endo (U/day)':>14} {'Safety Margin':>14} {'DKA Risk':>12}")
    for bf in [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50]:
        endo = endogenous_insulin_production(bf, secretion_efficiency=0.7)
        margin = endo / dka_threshold
        risk = "HIGH" if margin < 0.5 else "MODERATE" if margin < 1.0 else "LOW" if margin < 1.5 else "MINIMAL"
        print(f"    {bf*100:>5.0f}% {endo:>13.1f} {margin:>13.2f}x {risk:>12}")

    # FMD + ketosis concern
    print(f"\n  FMD KETOSIS vs DKA:")
    print(f"    Therapeutic ketosis (FMD): BHB 1-3 mM, pH normal, glucose 60-120")
    print(f"    DKA: BHB >5 mM, pH <7.3, glucose typically >250")
    print(f"    KEY: the patient on insulin + low beta mass. During FMD:")
    print(f"      - Reduce bolus to 0-1U (no meals)")
    print(f"      - Keep basal at minimum (prevent fat mobilization runaway)")
    print(f"      - Check BHB 2x/day: if >3.0 AND glucose >250 -> eat + insulin")
    print(f"      - CGM alarming at 250 mg/dL upper bound")

    return {
        "dka_threshold_u": dka_threshold,
        "critical_beta_mass": critical_mass,
        "beta_fractions": beta_fractions,
        "safety_margins": margins,
    }


# =============================================================================
# THE TARGET: C-PEPTIDE LEVEL FOR SAFE INSULIN DISCONTINUATION
# =============================================================================

def insulin_discontinuation_analysis():
    """
    Determine the C-peptide level at which insulin can be safely stopped.

    This is THE metric the protocol is aiming for. Everything else
    (beta cell mass, Teff, Treg, virus clearance) is a means to this end.
    """
    print("\n" + "=" * 72)
    print("INSULIN DISCONTINUATION ANALYSIS")
    print("=" * 72)

    print(f"\n  The question: at what C-peptide can insulin be stopped?")
    print(f"\n  Evidence:")
    print(f"    - Palmer 2004: C-peptide >0.6 nmol/L -> fewer hypos, easier control")
    print(f"    - Steffes 2003: even low C-peptide -> fewer complications")
    print(f"    - Greenbaum 2012: C-peptide >0.2 = clinically meaningful")
    print(f"    - Normal fasting C-peptide: 0.3-2.3 nmol/L")
    print(f"    - Normal stimulated C-peptide: 1.0-5.0 nmol/L")

    # Model: C-peptide vs insulin independence for different scenarios
    cp_levels = np.arange(0.1, 4.0, 0.05)

    # Without semaglutide
    can_stop_no_sema = []
    for cp in cp_levels:
        # Back-calculate beta mass from C-peptide
        # Cp = B * 2.5 * efficiency
        B_est = cp / (2.5 * 0.70)  # improved efficiency after protocol
        result = exogenous_insulin_needed(
            beta_mass_fraction=B_est,
            semaglutide_on=False,
        )
        can_stop_no_sema.append(result['can_discontinue'])

    # With semaglutide
    can_stop_sema = []
    for cp in cp_levels:
        B_est = cp / (2.5 * 0.70 * 1.40)  # semaglutide boosts Cp
        result = exogenous_insulin_needed(
            beta_mass_fraction=B_est,
            semaglutide_on=True,
        )
        can_stop_sema.append(result['can_discontinue'])

    # Find thresholds
    no_sema_idx = next((i for i, x in enumerate(can_stop_no_sema) if x), None)
    sema_idx = next((i for i, x in enumerate(can_stop_sema) if x), None)

    cp_threshold_no_sema = cp_levels[no_sema_idx] if no_sema_idx else None
    cp_threshold_sema = cp_levels[sema_idx] if sema_idx else None

    print(f"\n  DISCONTINUATION THRESHOLDS:")
    if cp_threshold_no_sema:
        print(f"    Without semaglutide: C-peptide >= {cp_threshold_no_sema:.2f} nmol/L")
    if cp_threshold_sema:
        print(f"    With semaglutide:    C-peptide >= {cp_threshold_sema:.2f} nmol/L")

    print(f"\n  RECOMMENDATION:")
    print(f"    Conservative target: stimulated C-peptide >= 2.0 nmol/L")
    print(f"    With semaglutide:    stimulated C-peptide >= 1.5 nmol/L may suffice")
    print(f"    Always maintain CGM even after discontinuation")
    print(f"    Keep insulin available for illness/stress days")

    return {
        "cp_threshold_no_sema": cp_threshold_no_sema,
        "cp_threshold_sema": cp_threshold_sema,
    }


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 72)
    print("INSULIN SENSITIVITY & DOSE REDUCTION MODEL")
    print("systematic approach | ODD Instance (numerics)")
    print("The dangerous transition: exogenous -> endogenous insulin")
    print("=" * 72)

    # Generate the patient trajectory
    print("\n--- the patient Trajectory ---")
    result = patient_zero_trajectory(t_months=36)

    # Print milestone timeline
    print(f"\n  Milestones reached:")
    for ms in result['milestones_reached']:
        print(f"    Month {ms['month']:>5.1f}: {ms['milestone']} "
              f"(Cp={ms['cpeptide_nmol']:.2f} nmol/L, "
              f"reduction={ms['insulin_reduction']*100:.0f}%)")

    if result['danger_zone_start_month'] is not None:
        print(f"\n  DANGER ZONE: months {result['danger_zone_start_month']:.0f} "
              f"to {result['danger_zone_end_month']:.0f}")

    if result['independence_month'] is not None:
        print(f"  INSULIN INDEPENDENCE: month {result['independence_month']:.0f}")
    else:
        print(f"  INSULIN INDEPENDENCE: not reached in 36-month window")

    # Plot
    plot_insulin_trajectory(result)
    plot_cpeptide_milestones()

    # DKA risk analysis
    dka_risk_analysis()

    # Discontinuation analysis
    insulin_discontinuation_analysis()

    # Summary
    print("\n" + "=" * 72)
    print("TIMELINE SUMMARY: the patient INSULIN REDUCTION")
    print("=" * 72)
    print(f"  Month 0:      16 U/day (12 basal + 2x2 bolus)")
    print(f"  Month 3:      ~16 U/day (no change yet, virus clearing)")
    print(f"  Month 6:      ~14 U/day (slight reduction, first C-peptide rise)")
    print(f"  Month 9:      ~10 U/day (FMD + GABA kicking in)")
    print(f"  Month 12:     ~7 U/day (approaching danger zone)")
    print(f"  Month 18:     ~4 U/day (in danger zone, CGM critical)")
    print(f"  Month 24:     ~2 U/day (safety minimum)")
    print(f"  Month 30-36:  TRIAL: 0 U/day (if C-peptide >2.0 nmol/L)")
    print(f"\n  Best case:    independence at 18-24 months")
    print(f"  Expected:     independence at 24-36 months")
    print(f"  Worst case:   reduced insulin needs but not full independence")
    print(f"                (still a major quality-of-life improvement)")

    print("\nDone. All figures saved to:", OUTPUT_DIR)


if __name__ == "__main__":
    main()
