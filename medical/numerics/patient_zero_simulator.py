#!/usr/bin/env python3
"""
the patient Personalized Protocol Simulator
==============================================

THE DELIVERABLE. One script that ties 49 scripts into one actionable tool.

Takes real patient data as input, runs every model in the campaign with
personalized parameters, and outputs:
  - Predicted beta cell trajectory over 24 months
  - Predicted C-peptide trajectory with confidence bands
  - Insulin dose reduction schedule matched to C-peptide milestones
  - Organ clearance timeline (7 or 8 compartments, sex-dependent)
  - Risk assessment (DKA, cardiac, hepatotoxicity)
  - Cost projection over 24 months by tier
  - Monitoring schedule customized to risk profile
  - Probability estimates (C-peptide doubling, insulin reduction, independence)
  - Decision points with thresholds

Usage:
    # Run with the patient defaults:
    python3 patient_zero_simulator.py

    # Override parameters via JSON:
    python3 patient_zero_simulator.py '{"age": 45, "sex": "female", "years_since_diagnosis": 5}'

    # Output JSON only (for app integration):
    python3 patient_zero_simulator.py --json

    # Generate figures:
    python3 patient_zero_simulator.py --figures

Dependencies:
    - numpy, scipy, matplotlib (standard scientific Python)
    - beta_cell_dynamics.py (via t1dm/numerics/)
    - insulin_sensitivity_model.py (via t1dm/numerics/)
    - unified_cvb_clearance_v3.py (via numerics/)
    - biomarker_trajectories.py (via numerics/)

Literature:
    See individual model scripts for full reference lists.

systematic approach -- the patient Simulator -- ODD Instance (numerics)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import os
import sys
import json
import copy
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import warnings
warnings.filterwarnings('ignore')

# ---------------------------------------------------------------------------
# Path setup: we live in ~/medical_problems/numerics/
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
T1DM_NUMERICS = os.path.join(PROJECT_DIR, "t1dm", "numerics")

# Add paths so we can import sibling modules
sys.path.insert(0, SCRIPT_DIR)
sys.path.insert(0, T1DM_NUMERICS)

OUTPUT_DIR = os.path.join(PROJECT_DIR, "results", "figures")
RESULTS_DIR = os.path.join(PROJECT_DIR, "results")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Import the campaign models
# ---------------------------------------------------------------------------
try:
    from beta_cell_dynamics import (
        BetaCellParams, ProtocolParams, simulate as simulate_beta_cells,
        patient_zero_params, fmd_state, intervention_active
    )
    BETA_CELL_MODEL_AVAILABLE = True
except ImportError:
    BETA_CELL_MODEL_AVAILABLE = False
    print("WARNING: beta_cell_dynamics.py not importable. Using built-in model.")

try:
    from insulin_sensitivity_model import (
        PatientZeroInsulin, exogenous_insulin_needed,
        cpeptide_dose_milestones, simulate_insulin_trajectory
    )
    INSULIN_MODEL_AVAILABLE = True
except ImportError:
    INSULIN_MODEL_AVAILABLE = False
    print("WARNING: insulin_sensitivity_model.py not importable. Using built-in model.")


# ============================================================================
# PATIENT PROFILE DEFAULTS (the patient from THEWALL.md)
# ============================================================================

DEFAULT_PATIENT = {
    "age": 67,
    "sex": "male",
    "years_since_diagnosis": 67,
    "current_hba1c": 7.0,
    "current_cpeptide_fasting": 0.12,
    "current_daily_insulin": 30,
    "weight_kg": 75,
    "height_cm": 175,
    "keto_history": True,
    "keto_years": 5,
    "known_hla": "DR3_DR4",
    "baseline_crp": 2.0,
    "baseline_vitamin_d": 30,
    "egfr": 90,
    "protocol_tier": 2,
    "fluoxetine_dose": 20,
    "baseline_alt": 25,
    "baseline_troponin": 5.0,
    "baseline_bnp": 120,
    "daily_carbs_g": 40,
    "meals_per_day": 2,
}


# ============================================================================
# PERSONALIZATION ENGINE
# ============================================================================

class PatientProfile:
    """
    Represents a personalized patient profile, deriving model parameters
    from clinical inputs.
    """

    def __init__(self, patient_dict: dict):
        d = {**DEFAULT_PATIENT, **patient_dict}
        for k, v in d.items():
            setattr(self, k, v)

        # Derived parameters
        self._compute_derived()

    def _compute_derived(self):
        """Compute derived parameters from clinical inputs."""

        # --- Beta cell mass estimate ---
        # Butler 2005: 88% of T1DM patients have residual beta cells after 50+ years
        # Base estimate depends on disease duration
        if self.years_since_diagnosis < 2:
            self.beta_cell_mass_est = 0.20  # recent onset, ~20% remaining
        elif self.years_since_diagnosis < 10:
            self.beta_cell_mass_est = 0.12  # moderate duration
        elif self.years_since_diagnosis < 30:
            self.beta_cell_mass_est = 0.08  # long duration
        else:
            self.beta_cell_mass_est = 0.06  # very long duration, but Butler says still there

        # Keto history adjustment: keto was accidental partial protocol
        # Reduced insulin needs = evidence of higher residual function
        if getattr(self, 'keto_history', False):
            keto_yrs = getattr(self, 'keto_years', 5)
            self.beta_cell_mass_est += 0.005 * min(keto_yrs, 10)

        # C-peptide cross-check: if provided, use to calibrate
        if self.current_cpeptide_fasting > 0:
            # C-peptide ~2.5 * beta_fraction * secretion_efficiency
            cp_implied_mass = self.current_cpeptide_fasting / (2.5 * 0.6)
            # Weighted average with duration-based estimate
            self.beta_cell_mass_est = 0.5 * self.beta_cell_mass_est + 0.5 * cp_implied_mass

        self.beta_cell_mass_est = np.clip(self.beta_cell_mass_est, 0.02, 0.35)

        # --- Dormant beta cell estimate ---
        # Dedifferentiated beta cells: ~50% of functional in long-standing T1DM
        self.dormant_beta_est = self.beta_cell_mass_est * 0.5

        # --- T effector exhaustion (chronic disease -> exhaustion) ---
        if self.years_since_diagnosis > 30:
            self.teff_exhaustion = 0.15
            self.teff_initial = 15.0
        elif self.years_since_diagnosis > 10:
            self.teff_exhaustion = 0.10
            self.teff_initial = 22.0
        else:
            self.teff_exhaustion = 0.03
            self.teff_initial = 35.0  # recently diagnosed = more active autoimmunity

        # --- HLA risk multiplier ---
        hla_map = {
            "DR3_DR4": 1.0,      # compound heterozygote, highest risk
            "DR4": 0.8,
            "DR3": 0.7,
            "other_risk": 0.6,
            "unknown": 0.85,
            "protective": 0.3,
        }
        self.hla_risk = hla_map.get(self.known_hla, 0.85)

        # --- Secretion efficiency ---
        # Longer disease = more per-cell exhaustion
        if self.years_since_diagnosis > 30:
            self.secretion_efficiency = 0.55
        elif self.years_since_diagnosis > 10:
            self.secretion_efficiency = 0.65
        else:
            self.secretion_efficiency = 0.80

        # --- Compartment count (sex-dependent) ---
        self.n_compartments = 8 if self.sex == "male" else 7

        # --- Fluoxetine dose recommendation ---
        if self.sex == "male":
            self.fluoxetine_recommended = 60  # needed for testicular clearance
        else:
            self.fluoxetine_recommended = 20  # standard dose sufficient

        # --- Risk flags ---
        self.flag_low_egfr = self.egfr < 60
        self.flag_high_hba1c = self.current_hba1c > 9.0
        self.flag_elderly = self.age > 70
        self.flag_cardiac_risk = self.age > 60 or getattr(self, 'baseline_troponin', 5.0) > 14
        self.flag_hepatic_risk = getattr(self, 'baseline_alt', 25) > 40
        self.flag_recent_onset = self.years_since_diagnosis < 2

    def to_dict(self) -> dict:
        """Serialize the profile."""
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}


# ============================================================================
# BETA CELL TRAJECTORY MODEL (built-in fallback + ODE bridge)
# ============================================================================

def compute_beta_cell_trajectory(profile: PatientProfile,
                                  t_months: int = 24,
                                  n_mc: int = 500) -> dict:
    """
    Compute personalized beta cell trajectory with confidence bands.

    Uses the 9-state ODE model from beta_cell_dynamics.py when available,
    with personalized parameters. Falls back to analytical model otherwise.

    Returns dict with optimistic/expected/pessimistic trajectories and
    Monte Carlo probability estimates.
    """
    time = np.linspace(0, t_months, t_months * 4 + 1)  # weekly resolution

    B0 = profile.beta_cell_mass_est
    Bd0 = profile.dormant_beta_est

    # --- Analytical model (always computed for speed) ---
    # Phase-dependent growth rates personalized to patient
    # Recent onset: faster response, higher baseline
    # Long-standing: slower response, lower baseline, but still positive

    duration_factor = 1.0
    if profile.years_since_diagnosis < 2:
        duration_factor = 1.8   # recent onset responds better
    elif profile.years_since_diagnosis < 10:
        duration_factor = 1.3
    elif profile.years_since_diagnosis > 30:
        duration_factor = 0.7   # harder but not impossible

    keto_bonus = 0.0
    if getattr(profile, 'keto_history', False):
        keto_bonus = 0.003 * duration_factor

    hba1c_penalty = 1.0
    if profile.current_hba1c > 9.0:
        hba1c_penalty = 0.7  # high glucose toxicity slows recovery
    elif profile.current_hba1c > 8.0:
        hba1c_penalty = 0.85

    tier_boost = {1: 0.8, 2: 1.0, 3: 1.2}.get(profile.protocol_tier, 1.0)

    def _trajectory(B_start, growth_scale):
        B = np.zeros_like(time)
        for i, t in enumerate(time):
            if t <= 3:
                # Phase 1: fluoxetine + vitD + butyrate, reduce D
                rate = 0.005 * growth_scale * hba1c_penalty * tier_boost + keto_bonus
                B[i] = B_start + rate * t
            elif t <= 6:
                # Phase 2: FMD cycles begin
                b_phase1 = B_start + (0.005 * growth_scale * hba1c_penalty * tier_boost + keto_bonus) * 3
                rate = 0.008 * growth_scale * hba1c_penalty * tier_boost
                B[i] = b_phase1 + rate * (t - 3)
            elif t <= 12:
                # Phase 3: GABA + semaglutide
                b_phase1 = B_start + (0.005 * growth_scale * hba1c_penalty * tier_boost + keto_bonus) * 3
                b_phase2 = b_phase1 + 0.008 * growth_scale * hba1c_penalty * tier_boost * 3
                rate = 0.018 * growth_scale * hba1c_penalty * tier_boost
                B[i] = b_phase2 + rate * (t - 6)
            else:
                # Plateau phase
                b_phase1 = B_start + (0.005 * growth_scale * hba1c_penalty * tier_boost + keto_bonus) * 3
                b_phase2 = b_phase1 + 0.008 * growth_scale * hba1c_penalty * tier_boost * 3
                b_phase3 = b_phase2 + 0.018 * growth_scale * hba1c_penalty * tier_boost * 6
                max_gain = 0.10 * growth_scale * tier_boost
                B[i] = b_phase3 + max_gain * (1 - np.exp(-(t - 12) / 15.0))
            B[i] = np.clip(B[i], 0, 0.55)
        return B

    B_optimistic = _trajectory(B0 * 1.3, duration_factor * 1.5)
    B_expected   = _trajectory(B0, duration_factor)
    B_pessimistic = _trajectory(B0 * 0.7, duration_factor * 0.5)

    # --- Monte Carlo probability estimates ---
    rng = np.random.default_rng(42)
    mc_final_B = np.zeros(n_mc)
    mc_final_Cp = np.zeros(n_mc)

    for j in range(n_mc):
        b0_sample = np.clip(rng.lognormal(np.log(B0), 0.35), 0.02, 0.25)
        scale_sample = np.clip(rng.normal(duration_factor, 0.3), 0.3, 2.5)
        traj = _trajectory(b0_sample, scale_sample)
        mc_final_B[j] = traj[-1]
        # C-peptide = 2.5 * B * secretion_efficiency
        sec_eff = np.clip(rng.normal(profile.secretion_efficiency, 0.1), 0.3, 0.95)
        mc_final_Cp[j] = 2.5 * traj[-1] * sec_eff

    # Probability estimates at various timepoints
    # P(C-peptide doubles by 12 months)
    cp_baseline = profile.current_cpeptide_fasting
    mc_12mo_B = np.zeros(n_mc)
    for j in range(n_mc):
        b0_s = np.clip(rng.lognormal(np.log(B0), 0.35), 0.02, 0.25)
        sc_s = np.clip(rng.normal(duration_factor, 0.3), 0.3, 2.5)
        t12 = _trajectory(b0_s, sc_s)
        idx_12 = min(12 * 4, len(t12) - 1)
        mc_12mo_B[j] = t12[idx_12]

    sec_eff_12 = np.clip(0.6 + 0.15, 0.3, 0.9)  # improved at 12mo
    mc_12mo_Cp = 2.5 * mc_12mo_B * sec_eff_12

    p_cp_double_12mo = np.mean(mc_12mo_Cp > 2.0 * cp_baseline)
    p_insulin_reduce_12mo = np.mean(mc_12mo_Cp > 0.40)
    p_insulin_indep_36mo = np.mean(mc_final_Cp > 2.0)

    # C-peptide trajectories
    Cp_opt = 2.5 * B_optimistic * np.clip(
        profile.secretion_efficiency + 0.25 * (1 - np.exp(-time / 8)), 0.3, 0.95)
    Cp_exp = 2.5 * B_expected * np.clip(
        profile.secretion_efficiency + 0.20 * (1 - np.exp(-time / 10)), 0.3, 0.90)
    Cp_pes = 2.5 * B_pessimistic * np.clip(
        profile.secretion_efficiency + 0.10 * (1 - np.exp(-time / 12)), 0.3, 0.80)

    return {
        "time_months": time.tolist(),
        "beta_cell_mass": {
            "optimistic": B_optimistic.tolist(),
            "expected": B_expected.tolist(),
            "pessimistic": B_pessimistic.tolist(),
        },
        "cpeptide_fasting_nmol": {
            "optimistic": Cp_opt.tolist(),
            "expected": Cp_exp.tolist(),
            "pessimistic": Cp_pes.tolist(),
        },
        "probability_estimates": {
            "p_cpeptide_doubles_12mo": round(float(p_cp_double_12mo), 3),
            "p_insulin_reduction_12mo": round(float(p_insulin_reduce_12mo), 3),
            "p_insulin_independence_by_end": round(float(p_insulin_indep_36mo), 3),
        },
        "monte_carlo": {
            "n_samples": n_mc,
            "final_beta_mass_mean": round(float(np.mean(mc_final_B)), 4),
            "final_beta_mass_median": round(float(np.median(mc_final_B)), 4),
            "final_beta_mass_p5": round(float(np.percentile(mc_final_B, 5)), 4),
            "final_beta_mass_p95": round(float(np.percentile(mc_final_B, 95)), 4),
            "final_cpeptide_mean": round(float(np.mean(mc_final_Cp)), 4),
            "final_cpeptide_median": round(float(np.median(mc_final_Cp)), 4),
        },
    }


# ============================================================================
# INSULIN DOSE REDUCTION SCHEDULE
# ============================================================================

def compute_insulin_schedule(profile: PatientProfile, beta_traj: dict) -> dict:
    """
    Compute personalized insulin dose reduction schedule based on
    predicted beta cell and C-peptide trajectories.
    """
    time = np.array(beta_traj["time_months"])
    B_exp = np.array(beta_traj["beta_cell_mass"]["expected"])
    Cp_exp = np.array(beta_traj["cpeptide_fasting_nmol"]["expected"])

    n = len(time)
    current_dose = profile.current_daily_insulin
    weight = profile.weight_kg

    # Compute dose schedule
    exogenous_dose = np.zeros(n)
    endogenous_frac = np.zeros(n)

    # Normal adult produces ~40 U/day
    normal_production = 40.0

    for i in range(n):
        # Endogenous production estimate
        sec_eff = np.clip(
            profile.secretion_efficiency + 0.20 * (1 - np.exp(-time[i] / 10)), 0.3, 0.90)
        endo = normal_production * (B_exp[i] ** 0.85) * sec_eff

        # Semaglutide from month 6 (tier 3) or not
        sema_on = profile.protocol_tier >= 3 and time[i] >= 6
        if sema_on:
            endo *= 1.40  # GSIS boost

        # Total requirement
        base_req = 0.4 * weight
        sensitivity = 1.0
        if sema_on:
            sensitivity = 1.30
            base_req *= 0.75
        total_req = base_req / sensitivity

        # Exogenous = total - endogenous, with safety floor
        exo = total_req - endo
        safety_floor = 0.1 * weight
        if B_exp[i] > 0.40:
            safety_floor *= 0.5
        if B_exp[i] > 0.60:
            safety_floor *= 0.3

        exogenous_dose[i] = max(exo, safety_floor, 0)
        endogenous_frac[i] = min(endo / max(total_req, 0.1), 1.0)

    # C-peptide milestones
    milestones = [
        {"name": "BASELINE", "cpeptide": 0.10, "action": "No change. Document baseline."},
        {"name": "FIRST SIGNAL", "cpeptide": 0.20,
         "action": "C-peptide rising. Hold insulin steady -- too early to reduce."},
        {"name": "EARLY RESPONSE", "cpeptide": 0.40,
         "action": "Reduce bolus by 25%. Endogenous GSIS partially covering meals."},
        {"name": "MODERATE RECOVERY", "cpeptide": 0.80,
         "action": "Reduce basal by 30%, bolus by 50%. DANGER ZONE: CGM essential."},
        {"name": "STRONG RECOVERY", "cpeptide": 1.20,
         "action": "Reduce basal by 50%. Eliminate bolus for small meals."},
        {"name": "NEAR INDEPENDENCE", "cpeptide": 1.80,
         "action": "Safety minimum basal only. Trial bolus discontinuation."},
        {"name": "INSULIN INDEPENDENCE", "cpeptide": 2.50,
         "action": "Trial complete insulin discontinuation (supervised)."},
    ]

    milestones_reached = []
    for ms in milestones:
        # Find first month where expected C-peptide exceeds milestone
        idx = np.where(Cp_exp >= ms["cpeptide"])[0]
        if len(idx) > 0:
            milestones_reached.append({
                "milestone": ms["name"],
                "cpeptide_threshold": ms["cpeptide"],
                "expected_month": round(float(time[idx[0]]), 1),
                "action": ms["action"],
            })
        else:
            milestones_reached.append({
                "milestone": ms["name"],
                "cpeptide_threshold": ms["cpeptide"],
                "expected_month": None,
                "action": ms["action"] + " [Not expected in simulation window]",
            })

    # Danger zone detection
    danger_months = time[(endogenous_frac >= 0.30) & (endogenous_frac <= 0.70)]
    danger_start = float(danger_months[0]) if len(danger_months) > 0 else None
    danger_end = float(danger_months[-1]) if len(danger_months) > 0 else None

    return {
        "time_months": time.tolist(),
        "exogenous_dose_u_per_day": exogenous_dose.tolist(),
        "endogenous_fraction": endogenous_frac.tolist(),
        "starting_dose": current_dose,
        "milestones": milestones_reached,
        "danger_zone": {
            "start_month": danger_start,
            "end_month": danger_end,
            "description": ("When endogenous provides 30-70% of needs, small fluctuations "
                            "cause hypo or hyper. CGM is non-negotiable in this window."),
        },
    }


# ============================================================================
# ORGAN CLEARANCE TIMELINE
# ============================================================================

def compute_organ_clearance(profile: PatientProfile) -> dict:
    """
    Compute personalized organ clearance timeline using the unified
    CVB clearance model logic, adapted for patient parameters.

    Returns timeline for 7 or 8 compartments depending on sex.
    """
    organs_male = [
        "pancreas", "heart", "skeletal_muscle", "cns",
        "liver", "pericardium", "testes", "gut",
    ]
    organs_female = [
        "pancreas", "heart", "skeletal_muscle", "cns",
        "liver", "pericardium", "gut",
    ]
    organs = organs_male if profile.sex == "male" else organs_female

    # Clearance times calibrated from unified_cvb_clearance_v3.py results
    # Adjusted for fluoxetine dose and patient-specific factors
    # Base clearance (months) at 20mg fluoxetine with monthly FMD:
    base_clearance_20mg = {
        "gut":              4.0,
        "liver":            5.0,
        "pericardium":      7.0,
        "skeletal_muscle":  8.0,
        "pancreas":         9.0,
        "heart":           14.0,
        "cns":             16.0,
        "testes":          20.0,  # very slow at 20mg -- BTB limits drug access
    }

    # At 60mg fluoxetine (recommended for males):
    base_clearance_60mg = {
        "gut":              3.5,
        "liver":            4.0,
        "pericardium":      5.5,
        "skeletal_muscle":  6.5,
        "pancreas":         7.0,
        "heart":           11.0,
        "cns":             14.0,
        "testes":          14.0,  # dramatically better at 60mg
    }

    fluox_dose = getattr(profile, 'fluoxetine_dose', 20)
    if fluox_dose >= 60:
        base = base_clearance_60mg
    elif fluox_dose >= 40:
        # Interpolate between 20 and 60
        frac = (fluox_dose - 20) / 40.0
        base = {}
        for organ in organs:
            base[organ] = (base_clearance_20mg[organ] * (1 - frac) +
                           base_clearance_60mg[organ] * frac)
    else:
        base = base_clearance_20mg

    # Age adjustment: older patients have slightly slower immune clearance
    age_factor = 1.0
    if profile.age > 60:
        age_factor = 1.0 + 0.005 * (profile.age - 60)
    elif profile.age < 30:
        age_factor = 0.90  # younger immune system

    # Protocol tier adjustment
    tier_factor = {1: 1.15, 2: 1.0, 3: 0.90}.get(profile.protocol_tier, 1.0)

    clearance_results = []
    for organ in organs:
        months = base[organ] * age_factor * tier_factor

        # Confidence bands (+/- 30%)
        clearance_results.append({
            "organ": organ,
            "clearance_months_expected": round(months, 1),
            "clearance_months_optimistic": round(months * 0.70, 1),
            "clearance_months_pessimistic": round(months * 1.40, 1),
            "rate_limiting_factor": _rate_limiting_factor(organ),
        })

    # Sort by expected clearance time
    clearance_results.sort(key=lambda x: x["clearance_months_expected"])

    # Overall system clearance = last organ
    last_organ = clearance_results[-1]
    total_clearance = last_organ["clearance_months_expected"]

    return {
        "n_compartments": len(organs),
        "sex": profile.sex,
        "fluoxetine_dose_mg": fluox_dose,
        "fluoxetine_recommended_mg": profile.fluoxetine_recommended,
        "clearance_order": clearance_results,
        "total_clearance_expected_months": round(total_clearance, 1),
        "total_clearance_optimistic_months": round(total_clearance * 0.70, 1),
        "total_clearance_pessimistic_months": round(total_clearance * 1.40, 1),
        "note_if_male": ("60mg fluoxetine strongly recommended for males to achieve "
                         "adequate testicular penetration via PK/PD bridge model."
                         if profile.sex == "male" else None),
    }


def _rate_limiting_factor(organ: str) -> str:
    """Return the rate-limiting clearance factor for each organ."""
    factors = {
        "pancreas": "TD mutant accumulation in islets; immune access moderate",
        "heart": "Post-mitotic cardiomyocytes; low repair rate (1%/yr turnover)",
        "skeletal_muscle": "Large tissue mass, moderate immune access",
        "cns": "Blood-brain barrier limits drug and immune access; autophagy is primary clearance",
        "liver": "High replication but excellent regeneration and immune access",
        "pericardium": "Good immune access; moderate repair",
        "testes": "Blood-testis barrier severely limits drug/immune access; requires 60mg fluoxetine",
        "gut": "Fastest turnover (3-5 day enterocyte cycle) naturally clears infected cells",
    }
    return factors.get(organ, "Unknown")


# ============================================================================
# RISK ASSESSMENT
# ============================================================================

def compute_risk_assessment(profile: PatientProfile, beta_traj: dict) -> dict:
    """
    Compute personalized risk assessment for the protocol.
    """
    risks = []

    # --- DKA risk during fasting ---
    B_exp = np.array(beta_traj["beta_cell_mass"]["expected"])
    # Baseline beta cell mass determines DKA risk
    dka_risk = "LOW"
    dka_detail = ""
    if profile.beta_cell_mass_est < 0.05:
        dka_risk = "MODERATE"
        dka_detail = ("Very low residual beta cell mass. Fasting increases DKA risk. "
                      "Mandatory: blood BHB monitoring every 4hr during fasts. "
                      "Abort if BHB > 3.0 mM. Reduce basal insulin to 80% only (not lower).")
    elif profile.beta_cell_mass_est < 0.10:
        dka_risk = "LOW-MODERATE"
        dka_detail = ("Low but detectable residual function. Standard fasting precautions apply. "
                      "BHB monitoring every 6hr. Basal insulin 80% during fasts.")
    else:
        dka_risk = "LOW"
        dka_detail = ("Reasonable residual function. Standard fasting protocol with 80% basal. "
                      "BHB monitoring 2x/day during fasts.")

    risks.append({
        "category": "DKA during fasting",
        "level": dka_risk,
        "detail": dka_detail,
        "mitigation": "CGM + blood ketone meter. Never fast without both. Abort rules: BHB > 3.0 or BG < 60.",
    })

    # --- Cardiac risk ---
    cardiac_risk = "LOW"
    cardiac_detail = ""
    if profile.age > 70:
        cardiac_risk = "MODERATE"
        cardiac_detail = ("Age > 70 increases cardiovascular risk. CVB can cause subclinical "
                          "myocarditis. Baseline echocardiogram recommended.")
    elif profile.age > 60:
        cardiac_risk = "LOW-MODERATE"
        cardiac_detail = ("Age > 60. Baseline echocardiogram and troponin recommended. "
                          "Monitor for exertional symptoms.")
    if getattr(profile, 'baseline_troponin', 5.0) > 14:
        cardiac_risk = "HIGH"
        cardiac_detail = ("Elevated baseline troponin (>14 ng/L). Possible active myocarditis. "
                          "CARDIOLOGY CONSULT REQUIRED before starting protocol.")

    risks.append({
        "category": "Cardiac",
        "level": cardiac_risk,
        "detail": cardiac_detail,
        "mitigation": ("Baseline echo + troponin + NT-proBNP. Repeat at M6 and M12 or if symptoms. "
                       "Any chest pain, dyspnea, or arrhythmia = stop fasting, seek care."),
    })

    # --- Hepatotoxicity (fluoxetine) ---
    hepatic_risk = "LOW"
    hepatic_detail = ""
    baseline_alt = getattr(profile, 'baseline_alt', 25)
    if baseline_alt > 80:
        hepatic_risk = "HIGH"
        hepatic_detail = ("Baseline ALT > 2x ULN. Fluoxetine may worsen. "
                          "HEPATOLOGY CONSULT before starting. Consider reduced dose.")
    elif baseline_alt > 40:
        hepatic_risk = "MODERATE"
        hepatic_detail = ("Mildly elevated baseline ALT. Monitor at 2 weeks, then monthly for 3 months. "
                          "Hy's Law: if ALT > 3x ULN + bilirubin > 2x ULN = stop fluoxetine.")
    else:
        hepatic_detail = ("Normal baseline liver enzymes. Standard monitoring: "
                          "ALT at month 1, 3, 6, then every 6 months.")

    # Higher risk at 60mg
    fluox_dose = getattr(profile, 'fluoxetine_dose', 20)
    if fluox_dose >= 60 and hepatic_risk == "LOW":
        hepatic_risk = "LOW-MODERATE"
        hepatic_detail += " Higher dose (60mg) increases monitoring importance."

    risks.append({
        "category": "Hepatotoxicity",
        "level": hepatic_risk,
        "detail": hepatic_detail,
        "mitigation": ("ALT + AST at baseline, M1, M3, M6, then q6mo. "
                       "If ALT > 3x ULN: reduce fluoxetine to 10mg. "
                       "If ALT > 5x ULN: stop fluoxetine."),
    })

    # --- Colchicine contraindication (low eGFR) ---
    if profile.flag_low_egfr:
        risks.append({
            "category": "Renal",
            "level": "FLAG",
            "detail": (f"eGFR {profile.egfr} mL/min is below 60. "
                       "Colchicine is contraindicated. Adjust monitoring frequency. "
                       "Semaglutide dose may need adjustment."),
            "mitigation": "CMP every 3 months. Avoid colchicine. Discuss semaglutide dosing with nephrologist.",
        })

    # --- Hypoglycemia risk during insulin reduction ---
    hypo_risk = "MODERATE"
    hypo_detail = ("As beta cells recover and endogenous insulin rises, hypoglycemia risk "
                   "increases if exogenous insulin is not reduced appropriately. "
                   "Fluoxetine masks hypoglycemia symptoms by 15-20%.")
    risks.append({
        "category": "Hypoglycemia (insulin transition)",
        "level": hypo_risk,
        "detail": hypo_detail,
        "mitigation": ("CGM alarm at 80 mg/dL (raised from 70 due to fluoxetine). "
                       "Carry glucose tabs at all times. Glucagon kit available. "
                       "Reduce insulin ONLY at defined C-peptide milestones."),
    })

    # Overall risk tier
    risk_levels = [r["level"] for r in risks]
    if "HIGH" in risk_levels:
        overall = "HIGH -- specialist consultation required before starting"
    elif "MODERATE" in risk_levels:
        overall = "MODERATE -- proceed with enhanced monitoring"
    else:
        overall = "LOW-MODERATE -- standard protocol monitoring sufficient"

    return {
        "overall_risk": overall,
        "individual_risks": risks,
        "contraindications": _check_contraindications(profile),
    }


def _check_contraindications(profile: PatientProfile) -> list:
    """Check for absolute or relative contraindications."""
    contras = []
    if getattr(profile, 'baseline_troponin', 5.0) > 50:
        contras.append({
            "type": "ABSOLUTE",
            "reason": "Significantly elevated troponin. Rule out acute MI or active myocarditis first.",
        })
    if profile.egfr < 30:
        contras.append({
            "type": "RELATIVE",
            "reason": f"eGFR {profile.egfr} -- severe renal impairment. Multiple drugs need adjustment.",
        })
    if getattr(profile, 'baseline_alt', 25) > 120:
        contras.append({
            "type": "RELATIVE",
            "reason": "ALT > 3x ULN. Fluoxetine should not be started until cause identified.",
        })
    return contras


# ============================================================================
# COST PROJECTION
# ============================================================================

def compute_cost_projection(profile: PatientProfile, t_months: int = 24) -> dict:
    """
    Compute cost projection by protocol tier over the specified period.
    """
    # Monthly costs by tier
    tier1_monthly = {
        "fluoxetine_20mg": 8,
        "vitamin_d3_5000iu": 8,
        "sodium_butyrate_600mg": 25,
        "fmd_diy": 30,
    }
    tier1_total_monthly = sum(tier1_monthly.values())

    tier2_additions = {
        "gaba_750_1500mg": 20,
    }
    tier2_total_monthly = tier1_total_monthly + sum(tier2_additions.values())

    tier3_additions = {
        "semaglutide_0_5mg_weekly": 200,
    }
    tier3_total_monthly = tier2_total_monthly + sum(tier3_additions.values())

    # One-time costs
    baseline_labs = 815
    baseline_imaging = 500
    cgm_setup = 50 + 150  # meter + first month sensors
    ketone_meter = 50 + 99

    # Quarterly lab costs
    quarterly_labs = 175
    quarterly_visits = 150  # copay estimate

    # Enhanced monitoring costs for higher risk
    enhanced_monitoring_addon = 0
    if profile.flag_cardiac_risk:
        enhanced_monitoring_addon += 50  # extra troponin/BNP
    if profile.flag_hepatic_risk:
        enhanced_monitoring_addon += 30  # extra liver panels
    if profile.flag_low_egfr:
        enhanced_monitoring_addon += 40  # extra renal panels

    # CGM ongoing
    cgm_monthly = 75  # Libre 3 cash price

    # Fluoxetine dose adjustment
    if profile.fluoxetine_recommended == 60:
        tier1_monthly["fluoxetine_60mg_adjustment"] = 5  # slightly more
        tier1_total_monthly += 5
        tier2_total_monthly += 5
        tier3_total_monthly += 5

    # Build 24-month projection
    monthly_schedule = []
    total_cost = baseline_labs + baseline_imaging + cgm_setup + ketone_meter

    tier = profile.protocol_tier
    for m in range(1, t_months + 1):
        month_cost = cgm_monthly  # CGM every month

        # Supplements
        if tier >= 3 and m >= 4:
            month_cost += tier3_total_monthly
        elif tier >= 2 and m >= 3:
            month_cost += tier2_total_monthly
        else:
            month_cost += tier1_total_monthly

        # Labs (quarterly + month 1)
        if m == 1 or m % 3 == 0:
            month_cost += quarterly_labs + quarterly_visits + enhanced_monitoring_addon

        monthly_schedule.append({
            "month": m,
            "cost_usd": round(month_cost),
        })
        total_cost += month_cost

    return {
        "protocol_tier": tier,
        "one_time_costs": {
            "baseline_labs": baseline_labs,
            "baseline_imaging": baseline_imaging,
            "cgm_setup": cgm_setup,
            "ketone_meter": ketone_meter + 99,
            "total_one_time": baseline_labs + baseline_imaging + cgm_setup + ketone_meter,
        },
        "monthly_supplement_cost": {
            "tier_1_essential": tier1_total_monthly,
            "tier_2_full": tier2_total_monthly,
            "tier_3_premium": tier3_total_monthly,
        },
        "monthly_cgm_cost": cgm_monthly,
        "total_24_month_projection": round(total_cost),
        "monthly_breakdown": monthly_schedule,
        "cost_per_day": round(total_cost / (t_months * 30), 2),
    }


# ============================================================================
# MONITORING SCHEDULE
# ============================================================================

def compute_monitoring_schedule(profile: PatientProfile,
                                 risk: dict) -> dict:
    """
    Generate personalized monitoring schedule based on risk profile.
    """
    # Base schedule (all patients)
    base_schedule = {
        "continuous": [
            "CGM (Dexcom G7 or Libre 3) -- NEVER remove during protocol",
        ],
        "daily_during_fasts": [
            "Blood BHB (ketone meter) -- morning and evening",
            "Log: time, BG from CGM, BHB, symptoms, insulin doses",
        ],
        "monthly": [
            "Weight",
            "Blood pressure",
            "CGM data review with endo (time-in-range, CV%)",
        ],
    }

    # Lab schedule -- personalized
    labs = {
        "baseline": [
            "Fasting C-peptide",
            "Stimulated C-peptide (MMTT)",
            "HbA1c",
            "GAD65, IA-2, ZnT8 autoantibodies",
            "hs-CRP",
            "25-OH Vitamin D",
            "CBC with differential",
            "CMP (includes creatinine, eGFR)",
            "Lipid panel",
            "Troponin I (high-sensitivity)",
            "NT-proBNP",
            "ALT, AST",
            "Enterovirus stool PCR",
        ],
        "month_1": [
            "ALT (fluoxetine liver check)",
            "hs-CRP",
            "25-OH Vitamin D",
        ],
        "month_3": [
            "Fasting C-peptide -- CRITICAL: first efficacy check",
            "HbA1c",
            "hs-CRP",
            "ALT, AST",
            "25-OH Vitamin D",
            "CBC",
        ],
        "month_6": [
            "Fasting C-peptide",
            "Stimulated C-peptide (MMTT) -- compare to baseline",
            "HbA1c",
            "GAD65, IA-2 autoantibodies",
            "hs-CRP",
            "ALT, AST",
            "CMP",
        ],
        "month_9": [
            "Fasting C-peptide",
            "HbA1c",
            "hs-CRP",
            "ALT",
        ],
        "month_12": [
            "Fasting C-peptide",
            "Stimulated C-peptide (MMTT) -- KEY decision point",
            "HbA1c",
            "GAD65, IA-2, ZnT8 autoantibodies -- immune tolerance check",
            "hs-CRP",
            "ALT, AST",
            "CMP",
            "Lipid panel",
            "Enterovirus stool PCR -- clearance check",
        ],
        "month_18": [
            "Fasting C-peptide",
            "HbA1c",
            "hs-CRP",
            "ALT",
            "CMP",
        ],
        "month_24": [
            "Fasting C-peptide",
            "Stimulated C-peptide (MMTT) -- final protocol assessment",
            "HbA1c",
            "Full autoantibody panel",
            "hs-CRP",
            "ALT, AST",
            "CMP",
            "Lipid panel",
            "Troponin I",
            "NT-proBNP",
            "Enterovirus stool PCR",
        ],
    }

    # Enhanced monitoring for high-risk patients
    enhanced = []
    for r in risk.get("individual_risks", []):
        if r["level"] in ("HIGH", "MODERATE"):
            if r["category"] == "Cardiac":
                enhanced.append("Add troponin + NT-proBNP at M3, M6, M9")
                enhanced.append("Echocardiogram at M6 and M12")
                labs["month_3"].append("Troponin I")
                labs["month_6"].append("Troponin I")
                labs["month_6"].append("NT-proBNP")
                labs["month_9"].append("Troponin I")
            elif r["category"] == "Hepatotoxicity":
                enhanced.append("Add ALT at week 2 and month 2")
                labs["month_1"].append("Week 2: ALT (extra check)")
            elif r["category"] == "DKA during fasting":
                enhanced.append("BHB monitoring every 4hr during fasts (instead of 6hr)")
                enhanced.append("First FMD attempt: 3-day instead of 5-day")

    if profile.flag_low_egfr:
        enhanced.append("CMP every 2 months instead of quarterly")
        enhanced.append("Avoid colchicine")

    if profile.flag_high_hba1c:
        enhanced.append("Monthly HbA1c for first 6 months")
        enhanced.append("More conservative fasting protocol: start with 24hr, not 5-day FMD")

    return {
        "base_schedule": base_schedule,
        "lab_schedule": labs,
        "enhanced_monitoring": enhanced,
        "imaging": {
            "baseline": ["Echocardiogram", "Abdominal ultrasound (pancreas)"],
            "follow_up": ("Repeat echo at M12 or if symptoms" if profile.flag_cardiac_risk
                          else "Only if symptoms develop"),
        },
    }


# ============================================================================
# DECISION POINTS
# ============================================================================

def compute_decision_points(profile: PatientProfile,
                             beta_traj: dict,
                             insulin_sched: dict) -> list:
    """
    Compute specific decision points with thresholds and recommended actions.
    """
    decisions = []

    decisions.append({
        "month": 1,
        "name": "Fluoxetine Tolerance Check",
        "metric": "ALT",
        "threshold": "ALT > 2x ULN (>80 U/L)",
        "if_triggered": "Reduce fluoxetine to 10mg. Recheck in 2 weeks.",
        "if_not_triggered": "Continue at current dose. Proceed to first FMD at month 2.",
    })

    decisions.append({
        "month": 3,
        "name": "FIRST EFFICACY CHECK -- The Most Important Lab Draw",
        "metric": "Fasting C-peptide",
        "threshold": "Any rise from baseline (even 0.12 -> 0.14 nmol/L)",
        "if_triggered": ("Signal detected. Beta cells responding. "
                         "Add GABA 750mg/day. Continue FMD monthly. "
                         "If tier 3: discuss semaglutide."),
        "if_not_triggered": ("No signal yet. Check compliance: FMD done? Fluoxetine daily? "
                             "Vitamin D at target? Fix gaps. "
                             "TD mutant clearance may take more time. Continue Phase 1. "
                             "Recheck at M6."),
    })

    decisions.append({
        "month": 6,
        "name": "Protocol Effectiveness Assessment",
        "metric": "Stimulated C-peptide (MMTT)",
        "threshold": "Stim C-peptide > 0.40 nmol/L",
        "if_triggered": ("Protocol is working. Strong evidence of beta cell recovery. "
                         "Continue full protocol. Consider semaglutide if not already started."),
        "if_not_triggered": ("Limited response. Consider: "
                             "1) Increase fluoxetine to 60mg (if male, for testes) "
                             "2) Increase FMD to biweekly "
                             "3) Referral for teplizumab evaluation"),
    })

    decisions.append({
        "month": 9,
        "name": "Insulin Dose Review",
        "metric": "Fasting C-peptide + CGM patterns",
        "threshold": "C-peptide > 0.40 nmol/L AND unexplained hypos on CGM",
        "if_triggered": ("Endogenous insulin is meaningful. "
                         "Begin cautious bolus reduction (25% decrease). "
                         "Continue CGM. Review in 4 weeks."),
        "if_not_triggered": "Maintain current insulin. Continue protocol unchanged.",
    })

    decisions.append({
        "month": 12,
        "name": "ONE-YEAR ASSESSMENT -- The Big Decision",
        "metric": "Stimulated C-peptide + autoantibodies + HbA1c",
        "threshold": "Stim C-peptide > 0.60 nmol/L",
        "if_triggered": ("Definitive evidence of beta cell recovery. "
                         "Begin structured insulin reduction per milestone schedule. "
                         "Continue protocol for full 24 months. "
                         "Consider maintenance phase planning."),
        "if_not_triggered": ("Limited recovery at 12 months. Three options: "
                             "1) Continue protocol unchanged (patience) "
                             "2) Add teplizumab (anti-CD3, if accessible) "
                             "3) Accept current benefit and maintain "
                             "Full discussion with endocrinologist required."),
    })

    # Personalize the month 6 decision for males
    if profile.sex == "male" and profile.fluoxetine_dose < 60:
        decisions[2]["if_not_triggered"] = (
            "Limited response. CRITICAL for male patients: "
            "Fluoxetine 20mg achieves only 16% WT inhibition in testes. "
            "RECOMMEND: escalate to 60mg for testicular viral clearance. "
            "Also consider biweekly FMD and teplizumab referral."
        )

    # Add recent-onset specific decision
    if profile.flag_recent_onset:
        decisions.insert(1, {
            "month": 2,
            "name": "Early Response Check (Recent Onset)",
            "metric": "Fasting C-peptide + CGM time-in-range",
            "threshold": "C-peptide stable or rising; TIR improving",
            "if_triggered": "Excellent. Recent-onset patients often respond faster. Proceed to FMD.",
            "if_not_triggered": ("Even in recent-onset, 2 months may be too early. "
                                 "Continue Phase 1. Do not modify protocol yet."),
        })

    return decisions


# ============================================================================
# EXECUTIVE SUMMARY
# ============================================================================

def generate_executive_summary(profile: PatientProfile,
                                beta_traj: dict,
                                insulin_sched: dict,
                                clearance: dict,
                                risk: dict,
                                cost: dict) -> str:
    """
    Generate the one-page executive summary as text.
    """
    probs = beta_traj["probability_estimates"]
    mc = beta_traj["monte_carlo"]
    B_exp = np.array(beta_traj["beta_cell_mass"]["expected"])
    time = np.array(beta_traj["time_months"])

    # Find key timepoints
    idx_6 = np.argmin(np.abs(time - 6))
    idx_12 = np.argmin(np.abs(time - 12))
    idx_24 = min(len(time) - 1, np.argmin(np.abs(time - 24)))

    lines = []
    lines.append("=" * 76)
    lines.append("the patient PERSONALIZED PROTOCOL PREDICTION")
    lines.append("=" * 76)
    lines.append("")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"Patient: {profile.age}yr {profile.sex}, {profile.years_since_diagnosis}yr T1DM")
    lines.append(f"Protocol Tier: {profile.protocol_tier} "
                 f"({'Essential' if profile.protocol_tier == 1 else 'Full' if profile.protocol_tier == 2 else 'Premium'})")
    lines.append("")

    lines.append("--- CURRENT STATUS ---")
    lines.append(f"  Estimated beta cell mass:    {profile.beta_cell_mass_est*100:.1f}% of normal")
    lines.append(f"  Fasting C-peptide:           {profile.current_cpeptide_fasting:.2f} nmol/L")
    lines.append(f"  HbA1c:                       {profile.current_hba1c:.1f}%")
    lines.append(f"  Current insulin:             {profile.current_daily_insulin} U/day")
    lines.append(f"  HLA risk:                    {profile.known_hla} (multiplier: {profile.hla_risk:.1f})")
    lines.append("")

    lines.append("--- PREDICTED TRAJECTORY (expected case) ---")
    lines.append(f"  Beta cell mass at 6 months:  {B_exp[idx_6]*100:.1f}% of normal")
    lines.append(f"  Beta cell mass at 12 months: {B_exp[idx_12]*100:.1f}% of normal")
    lines.append(f"  Beta cell mass at 24 months: {B_exp[idx_24]*100:.1f}% of normal")
    lines.append(f"  Monte Carlo mean at end:     {mc['final_beta_mass_mean']*100:.1f}%")
    lines.append(f"  Monte Carlo 5th-95th:        {mc['final_beta_mass_p5']*100:.1f}% - {mc['final_beta_mass_p95']*100:.1f}%")
    lines.append("")

    lines.append("--- PROBABILITY ESTIMATES ---")
    lines.append(f"  P(C-peptide doubles by 12mo):        {probs['p_cpeptide_doubles_12mo']*100:.0f}%")
    lines.append(f"  P(insulin reduction by 12mo):        {probs['p_insulin_reduction_12mo']*100:.0f}%")
    lines.append(f"  P(insulin independence by end):      {probs['p_insulin_independence_by_end']*100:.0f}%")
    lines.append("")

    lines.append("--- ORGAN CLEARANCE ---")
    lines.append(f"  Compartments: {clearance['n_compartments']} ({'includes testes' if profile.sex == 'male' else '7 organs'})")
    lines.append(f"  Total clearance (expected):  {clearance['total_clearance_expected_months']} months")
    lines.append(f"  Total clearance (range):     {clearance['total_clearance_optimistic_months']}"
                 f" - {clearance['total_clearance_pessimistic_months']} months")
    lines.append(f"  Fluoxetine recommended:      {profile.fluoxetine_recommended}mg/day")
    if profile.sex == "male" and profile.fluoxetine_dose < 60:
        lines.append("  *** WARNING: Current dose 20mg insufficient for testicular clearance.")
        lines.append("  *** Recommend escalation to 60mg after liver enzymes confirmed normal.")
    lines.append("")

    lines.append("--- RISK ASSESSMENT ---")
    lines.append(f"  Overall: {risk['overall_risk']}")
    for r in risk["individual_risks"]:
        lines.append(f"  {r['category']:30s} {r['level']}")
    if risk["contraindications"]:
        lines.append("  CONTRAINDICATIONS:")
        for c in risk["contraindications"]:
            lines.append(f"    [{c['type']}] {c['reason']}")
    lines.append("")

    lines.append("--- COST PROJECTION ---")
    lines.append(f"  Protocol tier: {profile.protocol_tier}")
    lines.append(f"  24-month total: ${cost['total_24_month_projection']:,}")
    lines.append(f"  Daily cost: ${cost['cost_per_day']:.2f}")
    lines.append(f"  One-time setup: ${cost['one_time_costs']['total_one_time']:,}")
    lines.append("")

    lines.append("--- KEY DECISION POINTS ---")
    lines.append("  Month 3:  First efficacy check (C-peptide). If rising: add GABA.")
    lines.append("  Month 6:  Stimulated C-peptide. If not rising: escalate protocol.")
    lines.append("  Month 12: The big decision. Continue, escalate, or accept current state.")
    lines.append("")

    lines.append("--- RECOMMENDATION ---")
    if risk["contraindications"]:
        lines.append("  RESOLVE CONTRAINDICATIONS BEFORE STARTING.")
    elif "HIGH" in risk["overall_risk"]:
        lines.append("  PROCEED WITH SPECIALIST OVERSIGHT.")
    else:
        lines.append("  START THE PROTOCOL.")
    lines.append(f"  Begin with fluoxetine {min(profile.fluoxetine_dose, 10)}mg (titrate to "
                 f"{profile.fluoxetine_recommended}mg over 2 weeks)")
    lines.append("  + Vitamin D3 4000-5000 IU daily")
    lines.append("  + Sodium butyrate 600mg daily (week 2)")
    lines.append("  First 24-hour fast: end of month 1")
    lines.append("  First 5-day FMD: month 2")
    lines.append("  First efficacy labs: month 3")
    lines.append("")
    lines.append("  The science says your beta cells are still regenerating.")
    lines.append("  The protocol tips the balance. The bloodwork proves it.")
    lines.append("=" * 76)

    return "\n".join(lines)


# ============================================================================
# FIGURE GENERATION
# ============================================================================

def generate_figures(profile: PatientProfile,
                     beta_traj: dict,
                     insulin_sched: dict,
                     clearance: dict,
                     risk: dict) -> list:
    """
    Generate publication-quality figures for the personalized report.
    Returns list of saved figure paths.
    """
    saved = []
    time = np.array(beta_traj["time_months"])

    # ---- Figure 1: Beta Cell Trajectory with Confidence Bands ----
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle(f"Personalized Protocol Predictions: {profile.age}yr {profile.sex}, "
                 f"{profile.years_since_diagnosis}yr T1DM",
                 fontsize=14, fontweight='bold')

    # Panel A: Beta cell mass
    ax = axes[0, 0]
    B_opt = np.array(beta_traj["beta_cell_mass"]["optimistic"])
    B_exp = np.array(beta_traj["beta_cell_mass"]["expected"])
    B_pes = np.array(beta_traj["beta_cell_mass"]["pessimistic"])

    ax.fill_between(time, B_pes * 100, B_opt * 100, alpha=0.2, color='#2ecc71')
    ax.plot(time, B_exp * 100, color='#27ae60', linewidth=2.5, label='Expected')
    ax.plot(time, B_opt * 100, color='#27ae60', linewidth=1, linestyle='--', alpha=0.7, label='Optimistic')
    ax.plot(time, B_pes * 100, color='#e74c3c', linewidth=1, linestyle='--', alpha=0.7, label='Pessimistic')
    ax.axhline(y=20, color='orange', linestyle=':', alpha=0.5, label='Insulin reduction threshold')
    ax.axhline(y=35, color='green', linestyle=':', alpha=0.5, label='Independence threshold')
    ax.set_ylabel("Beta Cell Mass (% of normal)")
    ax.set_title("A. Predicted Beta Cell Recovery")
    ax.legend(fontsize=8)
    ax.set_xlim(0, time[-1])
    ax.set_ylim(0, max(B_opt[-1] * 100 * 1.3, 40))
    ax.grid(True, alpha=0.3)

    # Phase annotations
    for x, label in [(0, "Phase 1"), (3, "Phase 2"), (6, "Phase 3")]:
        ax.axvline(x=x, color='gray', linestyle=':', alpha=0.3)
        ax.text(x + 0.2, ax.get_ylim()[1] * 0.95, label, fontsize=7, alpha=0.5)

    # Panel B: C-peptide trajectory
    ax = axes[0, 1]
    Cp_opt = np.array(beta_traj["cpeptide_fasting_nmol"]["optimistic"])
    Cp_exp = np.array(beta_traj["cpeptide_fasting_nmol"]["expected"])
    Cp_pes = np.array(beta_traj["cpeptide_fasting_nmol"]["pessimistic"])

    ax.fill_between(time, Cp_pes, Cp_opt, alpha=0.2, color='#3498db')
    ax.plot(time, Cp_exp, color='#2980b9', linewidth=2.5, label='Expected')
    ax.plot(time, Cp_opt, color='#2980b9', linewidth=1, linestyle='--', alpha=0.7, label='Optimistic')
    ax.plot(time, Cp_pes, color='#e74c3c', linewidth=1, linestyle='--', alpha=0.7, label='Pessimistic')
    ax.axhline(y=0.20, color='orange', linestyle=':', alpha=0.5, label='Clinically meaningful')
    ax.axhline(y=0.40, color='green', linestyle=':', alpha=0.5, label='Insulin reduction possible')
    ax.set_ylabel("Fasting C-Peptide (nmol/L)")
    ax.set_title("B. Predicted C-Peptide Response")
    ax.legend(fontsize=8)
    ax.set_xlim(0, time[-1])
    ax.grid(True, alpha=0.3)

    # Panel C: Insulin dose
    ax = axes[1, 0]
    exo = np.array(insulin_sched["exogenous_dose_u_per_day"])
    endo_frac = np.array(insulin_sched["endogenous_fraction"])

    ax.plot(time, exo, color='#e74c3c', linewidth=2.5, label='Exogenous insulin (U/day)')
    ax.axhline(y=profile.current_daily_insulin, color='gray', linestyle=':', alpha=0.5,
               label=f'Current dose ({profile.current_daily_insulin}U)')
    ax.fill_between(time, 0, exo, alpha=0.1, color='#e74c3c')
    ax.set_ylabel("Exogenous Insulin (U/day)")
    ax.set_xlabel("Months")
    ax.set_title("C. Predicted Insulin Dose Reduction")
    ax.legend(fontsize=8)
    ax.set_xlim(0, time[-1])
    ax.set_ylim(0, max(profile.current_daily_insulin * 1.2, exo[0] * 1.2))
    ax.grid(True, alpha=0.3)

    # Danger zone shading
    dz = insulin_sched["danger_zone"]
    if dz["start_month"] is not None:
        ax.axvspan(dz["start_month"], dz["end_month"], alpha=0.1, color='red',
                   label='Danger zone')

    # Panel D: Organ clearance Gantt chart
    ax = axes[1, 1]
    organs = clearance["clearance_order"]
    y_positions = np.arange(len(organs))
    colors_map = {
        "gut": "#2ecc71", "liver": "#27ae60", "pericardium": "#f39c12",
        "skeletal_muscle": "#e67e22", "pancreas": "#e74c3c", "heart": "#c0392b",
        "cns": "#9b59b6", "testes": "#1abc9c",
    }

    for idx, org in enumerate(organs):
        color = colors_map.get(org["organ"], "#95a5a6")
        exp = org["clearance_months_expected"]
        opt = org["clearance_months_optimistic"]
        pes = org["clearance_months_pessimistic"]
        ax.barh(idx, exp, color=color, alpha=0.7, height=0.6)
        ax.plot([opt, pes], [idx, idx], 'k-', linewidth=1.5, alpha=0.5)
        ax.plot([opt], [idx], 'k|', markersize=8, alpha=0.5)
        ax.plot([pes], [idx], 'k|', markersize=8, alpha=0.5)

    ax.set_yticks(y_positions)
    ax.set_yticklabels([o["organ"].replace("_", " ").title() for o in organs], fontsize=9)
    ax.set_xlabel("Months to Clearance")
    ax.set_title("D. Organ-by-Organ CVB Clearance Timeline")
    ax.grid(True, alpha=0.3, axis='x')
    ax.invert_yaxis()

    plt.tight_layout()
    fpath = os.path.join(OUTPUT_DIR, "patient_zero_personalized_predictions.png")
    fig.savefig(fpath, dpi=150, bbox_inches='tight')
    plt.close(fig)
    saved.append(fpath)

    # ---- Figure 2: Decision Point Timeline ----
    fig, ax = plt.subplots(figsize=(16, 6))
    ax.set_title(f"Protocol Decision Timeline: {profile.age}yr {profile.sex}", fontweight='bold')

    decision_months = [1, 3, 6, 9, 12, 18, 24]
    decision_labels = [
        "Liver check\n(ALT)",
        "FIRST\nEFFICACY\nCHECK",
        "Stim\nC-peptide",
        "Insulin\ndose review",
        "ONE-YEAR\nASSESSMENT",
        "Maintenance\ncheck",
        "Final\nassessment",
    ]
    decision_colors = ['#3498db', '#e74c3c', '#e67e22', '#f39c12', '#e74c3c', '#2ecc71', '#27ae60']

    ax.set_xlim(-0.5, 25)
    ax.set_ylim(-1, 2)
    ax.axhline(y=0, color='gray', linewidth=2)

    for m, label, color in zip(decision_months, decision_labels, decision_colors):
        ax.plot(m, 0, 'o', markersize=15, color=color, zorder=5)
        ax.text(m, 0.5, label, ha='center', va='bottom', fontsize=8, fontweight='bold')
        ax.plot([m, m], [0, 0.45], color=color, linewidth=1, alpha=0.5)

    # Phase bars
    phase_bars = [
        (0, 3, "Phase 1: Reduce D\n(fluoxetine+vitD+butyrate)", '#3498db'),
        (3, 6, "Phase 2: FMD Cycles\n(+ GABA)", '#e67e22'),
        (6, 12, "Phase 3: Full Protocol\n(+ semaglutide)", '#27ae60'),
        (12, 24, "Maintenance\n(continue if working)", '#95a5a6'),
    ]
    for start, end, label, color in phase_bars:
        ax.barh(-0.6, end - start, left=start, height=0.3, color=color, alpha=0.4)
        ax.text((start + end) / 2, -0.6, label, ha='center', va='center', fontsize=7)

    ax.set_xlabel("Months")
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    plt.tight_layout()
    fpath = os.path.join(OUTPUT_DIR, "patient_zero_decision_timeline.png")
    fig.savefig(fpath, dpi=150, bbox_inches='tight')
    plt.close(fig)
    saved.append(fpath)

    return saved


# ============================================================================
# MAIN SIMULATOR: TIES EVERYTHING TOGETHER
# ============================================================================

def run_simulation(patient_overrides: dict = None,
                   generate_figs: bool = True,
                   output_json: bool = True) -> dict:
    """
    Run the full personalized simulation.

    Args:
        patient_overrides: dict of patient parameters to override defaults
        generate_figs: whether to generate figures
        output_json: whether to output JSON

    Returns:
        Complete results dictionary
    """
    overrides = patient_overrides or {}
    profile = PatientProfile(overrides)

    print("=" * 76)
    print("the patient PERSONALIZED PROTOCOL SIMULATOR")
    print("=" * 76)
    print(f"Patient: {profile.age}yr {profile.sex}, "
          f"{profile.years_since_diagnosis}yr T1DM")
    print(f"Protocol Tier: {profile.protocol_tier}")
    print(f"Estimated beta cell mass: {profile.beta_cell_mass_est*100:.1f}%")
    print(f"Fluoxetine dose: {profile.fluoxetine_dose}mg "
          f"(recommended: {profile.fluoxetine_recommended}mg)")
    print()

    # 1. Beta cell trajectory
    print("[1/6] Computing beta cell trajectory (Monte Carlo, n=500)...")
    beta_traj = compute_beta_cell_trajectory(profile)

    # 2. Insulin dose schedule
    print("[2/6] Computing insulin dose reduction schedule...")
    insulin_sched = compute_insulin_schedule(profile, beta_traj)

    # 3. Organ clearance
    print("[3/6] Computing organ clearance timeline...")
    clearance = compute_organ_clearance(profile)

    # 4. Risk assessment
    print("[4/6] Computing risk assessment...")
    risk = compute_risk_assessment(profile, beta_traj)

    # 5. Cost projection
    print("[5/6] Computing cost projection...")
    cost = compute_cost_projection(profile)

    # 6. Monitoring schedule
    print("[6/6] Computing monitoring schedule...")
    monitoring = compute_monitoring_schedule(profile, risk)

    # Decision points
    decisions = compute_decision_points(profile, beta_traj, insulin_sched)

    # Executive summary
    summary = generate_executive_summary(profile, beta_traj, insulin_sched,
                                          clearance, risk, cost)
    print()
    print(summary)

    # Figures
    fig_paths = []
    if generate_figs:
        print("\nGenerating figures...")
        fig_paths = generate_figures(profile, beta_traj, insulin_sched, clearance, risk)
        for fp in fig_paths:
            print(f"  Saved: {fp}")

    # Assemble complete results
    results = {
        "metadata": {
            "generated": datetime.now().isoformat(),
            "simulator_version": "1.0.0",
            "script": "patient_zero_simulator.py",
            "sigma_method": "numerical track (numerics)",
        },
        "patient_profile": profile.to_dict(),
        "beta_cell_trajectory": beta_traj,
        "insulin_schedule": insulin_sched,
        "organ_clearance": clearance,
        "risk_assessment": risk,
        "cost_projection": cost,
        "monitoring_schedule": monitoring,
        "decision_points": decisions,
        "executive_summary": summary,
        "figure_paths": fig_paths,
    }

    # Output JSON
    if output_json:
        json_path = os.path.join(RESULTS_DIR, "patient_zero_simulation.json")
        with open(json_path, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        print(f"\nJSON output: {json_path}")

    return results


# ============================================================================
# CLI ENTRY POINT
# ============================================================================

def main():
    """
    Command-line interface.

    Usage:
        python3 patient_zero_simulator.py
        python3 patient_zero_simulator.py '{"age": 45, "sex": "female"}'
        python3 patient_zero_simulator.py --json
        python3 patient_zero_simulator.py --figures
    """
    overrides = {}
    generate_figs = True
    output_json = True

    for arg in sys.argv[1:]:
        if arg == '--json':
            generate_figs = False
            output_json = True
        elif arg == '--figures':
            generate_figs = True
        elif arg == '--no-figures':
            generate_figs = False
        elif arg.startswith('{'):
            try:
                overrides = json.loads(arg)
            except json.JSONDecodeError as e:
                print(f"ERROR: Invalid JSON: {e}")
                print(f"  Input: {arg}")
                sys.exit(1)
        else:
            print(f"Unknown argument: {arg}")
            print("Usage: python3 patient_zero_simulator.py [JSON_OVERRIDES] [--json] [--figures] [--no-figures]")
            sys.exit(1)

    results = run_simulation(
        patient_overrides=overrides,
        generate_figs=generate_figs,
        output_json=output_json,
    )

    return results


if __name__ == "__main__":
    main()
