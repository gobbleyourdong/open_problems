#!/usr/bin/env python3
"""
Biomarker Trajectory Model — Clinical Monitoring for T1DM Protocol
====================================================================

Models expected biomarker trajectories during the the patient protocol,
providing the bridge between computational CVB clearance models and
real-world clinical measurement.

For each biomarker, models:
  - Baseline estimate (the patient: 67yr male, T1DM Dx 12/2019)
  - Expected trajectory on protocol over 24 months
  - Confidence bands (optimistic / expected / pessimistic)
  - Decision points (when to escalate, modify, or abort)
  - Safety thresholds

Biomarker categories:
  1. T1DM PRIMARY: C-peptide, HbA1c, glucose variability, autoantibodies
  2. IMMUNE: Tregs, hs-CRP, vitamin D, enterovirus PCR
  3. CARDIAC SAFETY: Troponin I, NT-proBNP, echocardiogram EF
  4. HEPATIC SAFETY: ALT/AST (fluoxetine monitoring)
  5. ME/CFS (if applicable): NK cytotoxicity, lactate:pyruvate

Literature references:
  [1]  Butler 2005 Diabetologia 48:2221 — beta cell persistence in T1DM
  [2]  Herold 2019 NEJM 381:603 — teplizumab delays T1DM onset
  [3]  Cheng 2017 Cell 168:775 — FMD beta cell regeneration
  [4]  DiViD study — enteroviral VP1 in 6/6 T1DM islets
  [5]  Youm 2015 Nat Med 21:263 — BHB/NLRP3 suppression
  [6]  Arpaia 2013 Nature 504:451 — butyrate -> FOXP3 -> Tregs
  [7]  Palmer 2004 Diabetes 53:250 — C-peptide thresholds clinical significance
  [8]  Lachin 2011 Diabetes 60:2379 — stimulated C-peptide preservation
  [9]  Ridker 2017 NEJM 377:1119 — hs-CRP and inflammation
  [10] FDA guidance — ALT thresholds for drug hepatotoxicity (Hy's Law)

systematic approach — Clinical Monitoring Bridge — numerical track (numerics)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import os
import json
from datetime import datetime

# =============================================================================
# OUTPUT DIRECTORY
# =============================================================================

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(PROJECT_DIR, "results", "figures")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# =============================================================================
# TIME AXIS: 24 months, weekly resolution
# =============================================================================

MONTHS = np.linspace(0, 24, 24 * 4 + 1)  # weekly for 24 months
MONTH_LABELS = [0, 1, 3, 6, 9, 12, 18, 24]  # clinical visit schedule

# =============================================================================
# the patient BASELINE ESTIMATES
# =============================================================================

PATIENT_ZERO = {
    "age": 67,
    "sex": "male",
    "dx_date": "2019-12",
    "disease_duration_years": 6.3,
    "dx_c_peptide_ng_ml": 0.9,      # at diagnosis
    "insulin_free_years": 5,          # 2020-2024 on keto
    "current_insulin": "2u Humalog/meal",
    "current_diet": "18:6 IF, 15-20g carbs/meal",
    "notes": "5yr insulin-free remission suggests significant residual beta cell mass",
}


# =============================================================================
# BIOMARKER DEFINITIONS
# =============================================================================

class Biomarker:
    """A single biomarker with trajectory model and clinical thresholds."""

    def __init__(self, name, unit, category, tier,
                 baseline_mean, baseline_range,
                 trajectory_fn,
                 normal_range=None,
                 success_threshold=None,
                 safety_threshold=None,
                 decision_points=None,
                 cost_usd=None,
                 direction="lower_is_better",
                 notes=""):
        self.name = name
        self.unit = unit
        self.category = category
        self.tier = tier  # 1=must have, 2=important, 3=nice to have
        self.baseline_mean = baseline_mean
        self.baseline_range = baseline_range
        self.trajectory_fn = trajectory_fn  # fn(months) -> (optimistic, expected, pessimistic)
        self.normal_range = normal_range
        self.success_threshold = success_threshold
        self.safety_threshold = safety_threshold
        self.decision_points = decision_points or {}
        self.cost_usd = cost_usd
        self.direction = direction  # "lower_is_better" or "higher_is_better"
        self.notes = notes

    def compute_trajectories(self, months=None):
        """Compute optimistic, expected, and pessimistic trajectories."""
        if months is None:
            months = MONTHS
        return self.trajectory_fn(months)

    def to_dict(self):
        """Serialize for JSON output."""
        opt, exp, pes = self.compute_trajectories(np.array(MONTH_LABELS, dtype=float))
        return {
            "name": self.name,
            "unit": self.unit,
            "category": self.category,
            "tier": self.tier,
            "baseline_mean": self.baseline_mean,
            "baseline_range": list(self.baseline_range),
            "normal_range": list(self.normal_range) if self.normal_range else None,
            "success_threshold": self.success_threshold,
            "safety_threshold": self.safety_threshold,
            "direction": self.direction,
            "cost_usd": self.cost_usd,
            "decision_points": self.decision_points,
            "trajectory_at_visits": {
                "months": MONTH_LABELS,
                "optimistic": [round(float(v), 4) for v in opt],
                "expected": [round(float(v), 4) for v in exp],
                "pessimistic": [round(float(v), 4) for v in pes],
            },
            "notes": self.notes,
        }


# =============================================================================
# TRAJECTORY FUNCTIONS
# =============================================================================
# Each returns (optimistic, expected, pessimistic) arrays.
# Based on published kinetics where available, extrapolated where not.

def cpeptide_trajectory(months):
    """
    C-peptide (fasting, nmol/L).

    the patient baseline: Dx C-peptide was 0.9 ng/mL = ~0.30 nmol/L (Dec 2019).
    After 6.3 years of T1DM, expect decline. BUT 5yr insulin-free on keto
    suggests preserved mass. Estimate current fasting C-peptide ~0.15-0.25 nmol/L.

    On protocol:
    - Optimistic: beta cell regeneration via FMD + GABA + viral clearance,
      C-peptide rises to 0.4-0.6 nmol/L by 18 months (insulin reduction possible)
    - Expected: slow rise, C-peptide reaches 0.2-0.3 nmol/L by 12 months
      (clinically meaningful but not insulin-independent)
    - Pessimistic: no significant change, remains 0.1-0.15 nmol/L
      (protocol not working, consider escalation)

    References: Palmer 2004, Lachin 2011 — 0.2 nmol/L = clinically meaningful
    """
    baseline = 0.20  # nmol/L, best estimate for the patient

    # Optimistic: sigmoid rise, reaching ~0.55 by 18 months
    opt = baseline + 0.40 * (1 / (1 + np.exp(-0.35 * (months - 9))))

    # Expected: slower sigmoid, reaching ~0.30 by 12 months
    exp = baseline + 0.15 * (1 / (1 + np.exp(-0.30 * (months - 10))))

    # Pessimistic: flat or very slight decline
    pes = baseline - 0.02 * (1 - np.exp(-months / 12))

    return opt, exp, pes


def cpeptide_stimulated_trajectory(months):
    """
    Stimulated C-peptide (mixed meal tolerance test, nmol/L).
    Typically 2-3x fasting value. More sensitive to beta cell function changes.

    This is THE gold standard measurement.
    """
    f_opt, f_exp, f_pes = cpeptide_trajectory(months)
    # Stimulated is ~2.5x fasting in partial function
    return f_opt * 2.5, f_exp * 2.5, f_pes * 2.0


def hba1c_trajectory(months):
    """
    HbA1c (%).

    the patient likely has good control (2u/meal + keto + IF).
    Baseline estimate: 6.5-7.0%.
    On protocol: should improve as endogenous insulin returns.

    HbA1c reflects 3-month average glucose; changes lag biomarker reality.
    """
    baseline = 6.8

    # Optimistic: drops to ~5.8% by 18 months (near-normal)
    opt = baseline - 1.0 * (1 / (1 + np.exp(-0.30 * (months - 10))))

    # Expected: drops to ~6.3% by 12 months
    exp = baseline - 0.5 * (1 / (1 + np.exp(-0.25 * (months - 10))))

    # Pessimistic: no change or slight worsening
    pes = baseline + 0.2 * (1 - np.exp(-months / 18))

    return opt, exp, pes


def glucose_cv_trajectory(months):
    """
    Glucose coefficient of variation (CV, %).
    Measures glycemic variability from CGM data.

    CV <36% is considered stable. T1DM typically 36-50%.
    As beta cells provide basal insulin, variability should decrease.
    """
    baseline = 42.0  # % CV, typical for well-controlled T1DM on low-dose insulin

    # Optimistic: beta cells smooth out glucose, CV drops to ~28%
    opt = baseline - 14.0 * (1 / (1 + np.exp(-0.25 * (months - 8))))

    # Expected: moderate improvement, CV to ~34%
    exp = baseline - 8.0 * (1 / (1 + np.exp(-0.20 * (months - 10))))

    # Pessimistic: no improvement
    pes = baseline + 2.0 * np.sin(months * 0.5) * np.exp(-months / 24)

    return opt, exp, pes


def gad65_trajectory(months):
    """
    GAD65 autoantibodies (IU/mL).

    Baseline: unknown, likely elevated (T1DM-associated).
    Long-standing T1DM: GAD65 often persists even when other autoantibodies fade.
    Typical: 20-200 IU/mL in active T1DM, <5 IU/mL is negative.

    On protocol: if immune tolerance improving, should decline over 12-24 months.
    This is a SLOW marker. Do not expect rapid changes.
    """
    baseline = 80.0  # IU/mL, moderate elevation

    # Optimistic: declines by 60% over 24 months
    opt = baseline * (0.4 + 0.6 * np.exp(-months / 12))

    # Expected: declines by 30% over 24 months
    exp = baseline * (0.7 + 0.3 * np.exp(-months / 18))

    # Pessimistic: no change
    pes = baseline * (1.0 + 0.05 * np.sin(months * 0.3))

    return opt, exp, pes


def ia2_trajectory(months):
    """IA-2 autoantibodies (IU/mL). Similar kinetics to GAD65 but often lower."""
    baseline = 30.0
    opt = baseline * (0.3 + 0.7 * np.exp(-months / 10))
    exp = baseline * (0.6 + 0.4 * np.exp(-months / 15))
    pes = baseline * (1.0 + 0.03 * np.sin(months * 0.4))
    return opt, exp, pes


def znt8_trajectory(months):
    """ZnT8 autoantibodies (IU/mL). Often declines with disease duration."""
    baseline = 15.0  # may already be low after 6 years
    opt = baseline * (0.2 + 0.8 * np.exp(-months / 8))
    exp = baseline * (0.5 + 0.5 * np.exp(-months / 14))
    pes = baseline * (1.0 + 0.02 * np.sin(months * 0.3))
    return opt, exp, pes


def hscrp_trajectory(months):
    """
    hs-CRP (mg/L).

    Systemic inflammation marker. Normal <1.0, moderate 1-3, high >3.
    T1DM patients often 1-3 mg/L from chronic immune activation.

    Protocol targets multiple inflammatory pathways:
    - BHB -> NLRP3 suppression -> less IL-1b
    - Butyrate -> Tregs -> less inflammatory signaling
    - Fluoxetine -> viral clearance -> less chronic immune stimulation
    """
    baseline = 2.5  # mg/L

    # Optimistic: drops to <0.5 (resolving inflammation)
    opt = 0.4 + (baseline - 0.4) * np.exp(-months / 5)

    # Expected: drops to ~1.2 by 12 months
    exp = 1.0 + (baseline - 1.0) * np.exp(-months / 8)

    # Pessimistic: minimal change
    pes = baseline - 0.3 * (1 - np.exp(-months / 12))

    return opt, exp, pes


def treg_trajectory(months):
    """
    Regulatory T cells (CD4+CD25+FoxP3+), % of CD4+ cells.

    Normal: 5-10% of CD4+. T1DM patients often have reduced Treg
    function (not always reduced numbers).

    Butyrate and vitamin D both promote Treg differentiation.
    Expect measurable increase by 3-6 months.
    """
    baseline = 4.5  # % of CD4+, low end

    # Optimistic: rises to ~8% (normal range) by 6 months
    opt = baseline + 4.0 * (1 / (1 + np.exp(-0.5 * (months - 4))))

    # Expected: rises to ~6.5% by 9 months
    exp = baseline + 2.0 * (1 / (1 + np.exp(-0.4 * (months - 6))))

    # Pessimistic: minimal change
    pes = baseline + 0.5 * (1 - np.exp(-months / 12))

    return opt, exp, pes


def vitamin_d_trajectory(months):
    """
    25-OH Vitamin D (ng/mL).

    Baseline: if not supplementing, likely 20-35 ng/mL.
    Protocol target: 50-70 ng/mL (immune modulation range).
    With 5000 IU/day, should reach target by 2-3 months.

    This is a COMPLIANCE marker as much as a biological one.
    """
    baseline = 28.0  # ng/mL

    # Optimistic: reaches 65 ng/mL by month 2 and holds
    opt = 65.0 - (65.0 - baseline) * np.exp(-months / 1.5)

    # Expected: reaches 55 ng/mL by month 3
    exp = 55.0 - (55.0 - baseline) * np.exp(-months / 2.0)

    # Pessimistic: poor compliance, reaches only 40
    pes = 40.0 - (40.0 - baseline) * np.exp(-months / 3.0)

    return opt, exp, pes


def enterovirus_pcr_trajectory(months):
    """
    Enterovirus PCR in stool (log10 copies/g or binary positive/negative).

    Modeled as probability of positive result (0-1 scale).
    Persistent enteroviral shedding is common in T1DM.
    Fluoxetine + autophagy should reduce shedding over months.

    This is a proxy for systemic CVB clearance.
    """
    baseline = 0.70  # 70% probability of positive at any test

    # Optimistic: negative by month 6
    opt = baseline * np.exp(-months / 3)
    opt = np.clip(opt, 0, 1)

    # Expected: negative by month 12
    exp = baseline * np.exp(-months / 6)
    exp = np.clip(exp, 0, 1)

    # Pessimistic: slow decline, still 30% positive at 24 months
    pes = baseline * (0.4 + 0.6 * np.exp(-months / 12))
    pes = np.clip(pes, 0, 1)

    return opt, exp, pes


def troponin_trajectory(months):
    """
    Troponin I (ng/L, high-sensitivity assay).

    Normal: <14 ng/L (99th percentile).
    Baseline should be normal unless active myocarditis.
    This is a SAFETY marker, not a treatment target.
    Any rise >14 requires cardiology consult.

    Fasting and supplements are not expected to cause troponin rise.
    Monitoring for occult myocarditis (CVB can affect the heart).
    """
    baseline = 5.0  # ng/L, normal

    # All scenarios: should remain stable/normal
    opt = baseline * np.ones_like(months)
    exp = baseline * np.ones_like(months)
    # Pessimistic: slight rise indicating subclinical myocarditis
    pes = baseline + 3.0 * (1 / (1 + np.exp(-0.3 * (months - 6))))

    return opt, exp, pes


def bnp_trajectory(months):
    """
    NT-proBNP (pg/mL).

    Normal for age 67: <300 pg/mL.
    Heart failure threshold: >300 pg/mL.
    Monitoring for cardiac safety during protocol.
    """
    baseline = 120.0  # pg/mL, normal for age

    # Optimistic: slight decrease with anti-inflammatory effects
    opt = baseline - 20 * (1 - np.exp(-months / 6))

    # Expected: stable
    exp = baseline * np.ones_like(months)

    # Pessimistic: mild rise (cardiac concern)
    pes = baseline + 40 * (1 / (1 + np.exp(-0.2 * (months - 12))))

    return opt, exp, pes


def alt_trajectory(months):
    """
    ALT (U/L).

    Normal: <40 U/L.
    Fluoxetine hepatotoxicity is rare (<1%) but serious.
    Hy's Law: ALT >3x ULN (>120 U/L) + bilirubin >2x ULN = abort.
    Protocol: monitor at 1, 3, 6 months, then every 6 months.
    """
    baseline = 25.0  # U/L, normal

    # All scenarios: should remain normal
    opt = baseline * np.ones_like(months)
    exp = baseline + 3 * np.sin(months * 0.5)  # mild fluctuation
    # Pessimistic: fluoxetine-induced rise
    pes = baseline + 15 * (1 / (1 + np.exp(-0.5 * (months - 2))))

    return opt, exp, pes


def nk_cytotoxicity_trajectory(months):
    """
    NK cell cytotoxicity (% lysis at 50:1 E:T ratio).
    Normal: 15-40%. ME/CFS patients often <10%.
    If applicable to the patient (fatigue symptoms).
    """
    baseline = 18.0  # % lysis, low-normal

    opt = baseline + 15 * (1 / (1 + np.exp(-0.3 * (months - 6))))
    exp = baseline + 8 * (1 / (1 + np.exp(-0.25 * (months - 9))))
    pes = baseline + 2 * (1 - np.exp(-months / 18))

    return opt, exp, pes


def lactate_pyruvate_trajectory(months):
    """
    Lactate:pyruvate ratio (dimensionless).
    Normal: 10-20. Elevated in mitochondrial dysfunction.
    ME/CFS marker. If applicable.
    """
    baseline = 22.0  # mildly elevated

    opt = 14.0 + (baseline - 14.0) * np.exp(-months / 6)
    exp = 17.0 + (baseline - 17.0) * np.exp(-months / 10)
    pes = baseline - 1.0 * (1 - np.exp(-months / 18))

    return opt, exp, pes


# =============================================================================
# BIOMARKER REGISTRY
# =============================================================================

BIOMARKERS = [
    # === T1DM PRIMARY ===
    Biomarker(
        name="Fasting C-Peptide",
        unit="nmol/L",
        category="T1DM Primary",
        tier=1,
        baseline_mean=0.20,
        baseline_range=(0.10, 0.30),
        trajectory_fn=cpeptide_trajectory,
        normal_range=(0.37, 1.47),
        success_threshold=0.20,  # clinically meaningful (Palmer 2004)
        safety_threshold=None,
        decision_points={
            "month_3": "If <0.12 nmol/L (declining), check adherence. Consider adding semaglutide.",
            "month_6": "If <0.15 nmol/L (no rise), consider adding teplizumab referral.",
            "month_12": "If <0.20 nmol/L, protocol has not achieved primary endpoint. Full reassessment.",
            "month_12_success": "If >0.30 nmol/L, beta cell regeneration confirmed. Begin cautious insulin reduction.",
            "month_18": "If >0.60 nmol/L, insulin reduction likely possible. Endocrinology team manages taper.",
        },
        cost_usd=45,
        direction="higher_is_better",
        notes="THE primary endpoint. 0.2 nmol/L = clinically meaningful. >0.6 = insulin reduction possible.",
    ),

    Biomarker(
        name="Stimulated C-Peptide (MMTT)",
        unit="nmol/L",
        category="T1DM Primary",
        tier=1,
        baseline_mean=0.50,
        baseline_range=(0.20, 0.75),
        trajectory_fn=cpeptide_stimulated_trajectory,
        normal_range=(0.93, 3.67),
        success_threshold=0.60,
        safety_threshold=None,
        decision_points={
            "month_6": "If <0.40 nmol/L, consider escalation (teplizumab).",
            "month_12": "If >0.60 nmol/L, definitive evidence of beta cell function improvement.",
        },
        cost_usd=150,  # includes MMTT setup
        direction="higher_is_better",
        notes="Gold standard. Requires clinic visit with timed blood draws after mixed meal.",
    ),

    Biomarker(
        name="HbA1c",
        unit="%",
        category="T1DM Primary",
        tier=1,
        baseline_mean=6.8,
        baseline_range=(6.2, 7.5),
        trajectory_fn=hba1c_trajectory,
        normal_range=(4.0, 5.6),
        success_threshold=6.0,
        safety_threshold=None,
        decision_points={
            "month_3": "First on-protocol value. If <6.5%, early signal of improved control.",
            "month_6": "If rising (>7.5%), protocol is not improving control. Reassess.",
            "month_12": "Target: <6.5%. If achieved with less insulin, protocol is working.",
        },
        cost_usd=20,
        direction="lower_is_better",
        notes="Reflects 3-month average glucose. Lags behind real-time changes by ~6 weeks.",
    ),

    Biomarker(
        name="Glucose CV (from CGM)",
        unit="%",
        category="T1DM Primary",
        tier=2,
        baseline_mean=42.0,
        baseline_range=(35.0, 50.0),
        trajectory_fn=glucose_cv_trajectory,
        normal_range=(None, 36.0),  # <36% is target
        success_threshold=36.0,
        safety_threshold=None,
        decision_points={
            "month_3": "If CV <36%, beta cells providing meaningful basal insulin.",
        },
        cost_usd=0,  # from CGM, already worn
        direction="lower_is_better",
        notes="Calculated from CGM data (coefficient of variation). Free if already wearing CGM.",
    ),

    # === AUTOANTIBODIES ===
    Biomarker(
        name="GAD65 Autoantibodies",
        unit="IU/mL",
        category="Autoimmune",
        tier=2,
        baseline_mean=80.0,
        baseline_range=(20.0, 200.0),
        trajectory_fn=gad65_trajectory,
        normal_range=(None, 5.0),
        success_threshold=None,  # any decline is meaningful
        safety_threshold=None,
        decision_points={
            "month_6": "Baseline comparison. GAD65 is slow to change. >20% decline is encouraging.",
            "month_12": "If declined >30%, immune tolerance is improving.",
            "month_24": "If normalized (<5 IU/mL), remarkable result. Immune tolerance likely achieved.",
        },
        cost_usd=85,
        direction="lower_is_better",
        notes="Slow marker. Do NOT expect rapid changes. 6-12 month intervals are appropriate.",
    ),

    Biomarker(
        name="IA-2 Autoantibodies",
        unit="IU/mL",
        category="Autoimmune",
        tier=2,
        baseline_mean=30.0,
        baseline_range=(5.0, 80.0),
        trajectory_fn=ia2_trajectory,
        normal_range=(None, 7.5),
        success_threshold=None,
        safety_threshold=None,
        decision_points={},
        cost_usd=85,
        direction="lower_is_better",
        notes="Combined with GAD65 and ZnT8 for full autoimmune status.",
    ),

    Biomarker(
        name="ZnT8 Autoantibodies",
        unit="IU/mL",
        category="Autoimmune",
        tier=3,
        baseline_mean=15.0,
        baseline_range=(0.0, 40.0),
        trajectory_fn=znt8_trajectory,
        normal_range=(None, 15.0),
        success_threshold=None,
        safety_threshold=None,
        decision_points={},
        cost_usd=85,
        direction="lower_is_better",
        notes="Often declines with disease duration regardless of intervention.",
    ),

    # === IMMUNE MARKERS ===
    Biomarker(
        name="hs-CRP",
        unit="mg/L",
        category="Inflammation",
        tier=1,
        baseline_mean=2.5,
        baseline_range=(1.0, 5.0),
        trajectory_fn=hscrp_trajectory,
        normal_range=(None, 1.0),
        success_threshold=1.0,
        safety_threshold=10.0,  # >10 suggests acute infection, not protocol-related
        decision_points={
            "month_1": "If >10 mg/L, suggests acute infection. Not protocol-related. Investigate.",
            "month_3": "Expect >30% decline from baseline if protocol reducing inflammation.",
            "month_6": "Target: <1.5 mg/L. If still >3.0, anti-inflammatory arm underperforming.",
        },
        cost_usd=25,
        direction="lower_is_better",
        notes="Fastest-responding inflammation marker. Should see changes within 1-3 months.",
    ),

    Biomarker(
        name="Treg Count (CD4+CD25+FoxP3+)",
        unit="% of CD4+",
        category="Immune",
        tier=2,
        baseline_mean=4.5,
        baseline_range=(3.0, 6.0),
        trajectory_fn=treg_trajectory,
        normal_range=(5.0, 10.0),
        success_threshold=6.0,
        safety_threshold=None,
        decision_points={
            "month_3": "First check. If >5.5%, butyrate + vitamin D working.",
            "month_6": "Target: >6.0%. If <4.5% (no change), increase butyrate dose to 600mg BID.",
        },
        cost_usd=200,  # flow cytometry panel
        direction="higher_is_better",
        notes="Requires flow cytometry (specialized lab). Most informative immune marker for this protocol.",
    ),

    Biomarker(
        name="25-OH Vitamin D",
        unit="ng/mL",
        category="Compliance",
        tier=1,
        baseline_mean=28.0,
        baseline_range=(15.0, 40.0),
        trajectory_fn=vitamin_d_trajectory,
        normal_range=(30.0, 100.0),
        success_threshold=50.0,  # immunomodulatory target
        safety_threshold=100.0,  # toxicity threshold
        decision_points={
            "month_1": "Should be rising. If <30 ng/mL, increase dose or check absorption.",
            "month_3": "Target: 50-70 ng/mL. If <40, compliance issue or malabsorption.",
            "month_6": "If >100 ng/mL, reduce dose (toxicity risk: hypercalcemia).",
        },
        cost_usd=40,
        direction="higher_is_better",
        notes="Compliance marker. Should respond within 4-8 weeks. Check calcium if >80 ng/mL.",
    ),

    Biomarker(
        name="Enterovirus PCR (stool)",
        unit="probability positive",
        category="Viral",
        tier=3,
        baseline_mean=0.70,
        baseline_range=(0.50, 0.90),
        trajectory_fn=enterovirus_pcr_trajectory,
        normal_range=(None, 0.0),  # negative is normal
        success_threshold=0.10,  # <10% probability = likely cleared
        safety_threshold=None,
        decision_points={
            "month_6": "If still positive, viral clearance is slow. Consider increasing FMD frequency.",
            "month_12": "If still positive, fluoxetine may not be reaching pancreatic reservoir. Consider dose increase.",
        },
        cost_usd=150,  # research lab, not standard
        direction="lower_is_better",
        notes="Research-grade test. Not available at standard labs. Academic virology lab needed.",
    ),

    # === CARDIAC SAFETY ===
    Biomarker(
        name="Troponin I (hs)",
        unit="ng/L",
        category="Cardiac Safety",
        tier=1,
        baseline_mean=5.0,
        baseline_range=(2.0, 10.0),
        trajectory_fn=troponin_trajectory,
        normal_range=(None, 14.0),
        success_threshold=None,  # not a treatment target
        safety_threshold=14.0,  # 99th percentile
        decision_points={
            "any_visit": "If >14 ng/L, STOP protocol and get cardiology consult immediately.",
            "any_visit_2": "If rising trend (even within normal), get echocardiogram.",
        },
        cost_usd=30,
        direction="lower_is_better",
        notes="SAFETY MARKER. Any elevation above 14 ng/L = active myocardial injury. Immediate workup.",
    ),

    Biomarker(
        name="NT-proBNP",
        unit="pg/mL",
        category="Cardiac Safety",
        tier=2,
        baseline_mean=120.0,
        baseline_range=(50.0, 250.0),
        trajectory_fn=bnp_trajectory,
        normal_range=(None, 300.0),  # age-adjusted for >65
        success_threshold=None,
        safety_threshold=300.0,
        decision_points={
            "any_visit": "If >300 pg/mL, suggests heart failure. Cardiology referral.",
            "any_visit_2": "If >900 pg/mL, likely symptomatic HF. Urgent evaluation.",
        },
        cost_usd=40,
        direction="lower_is_better",
        notes="Age-adjusted threshold: <300 pg/mL normal for age >65. Screen for occult CVB cardiomyopathy.",
    ),

    # === HEPATIC SAFETY ===
    Biomarker(
        name="ALT",
        unit="U/L",
        category="Hepatic Safety",
        tier=1,
        baseline_mean=25.0,
        baseline_range=(15.0, 35.0),
        trajectory_fn=alt_trajectory,
        normal_range=(None, 40.0),
        success_threshold=None,
        safety_threshold=120.0,  # 3x ULN — drug hepatotoxicity threshold
        decision_points={
            "month_1": "First fluoxetine safety check. If >80 U/L (2x ULN), recheck in 2 weeks.",
            "month_3": "If >120 U/L (3x ULN), REDUCE fluoxetine dose to 10mg or discontinue.",
            "any_visit": "If ALT >3x ULN + bilirubin >2x ULN (Hy's Law), STOP fluoxetine immediately.",
        },
        cost_usd=15,
        direction="lower_is_better",
        notes="Fluoxetine hepatotoxicity is rare (<1%) but must be monitored. Hy's Law is the abort criterion.",
    ),

    # === ME/CFS (IF APPLICABLE) ===
    Biomarker(
        name="NK Cell Cytotoxicity",
        unit="% lysis",
        category="ME/CFS",
        tier=3,
        baseline_mean=18.0,
        baseline_range=(8.0, 25.0),
        trajectory_fn=nk_cytotoxicity_trajectory,
        normal_range=(15.0, 40.0),
        success_threshold=25.0,
        safety_threshold=None,
        decision_points={},
        cost_usd=250,
        direction="higher_is_better",
        notes="Only if ME/CFS symptoms present. Requires specialized immunology lab.",
    ),

    Biomarker(
        name="Lactate:Pyruvate Ratio",
        unit="ratio",
        category="ME/CFS",
        tier=3,
        baseline_mean=22.0,
        baseline_range=(15.0, 30.0),
        trajectory_fn=lactate_pyruvate_trajectory,
        normal_range=(10.0, 20.0),
        success_threshold=20.0,
        safety_threshold=None,
        decision_points={},
        cost_usd=80,
        direction="lower_is_better",
        notes="Marker of mitochondrial function. Only if fatigue/PEM symptoms present.",
    ),
]

# Index by name for easy lookup
BIOMARKER_MAP = {b.name: b for b in BIOMARKERS}


# =============================================================================
# PLOTTING
# =============================================================================

def plot_single_biomarker(biomarker, ax=None, show_decisions=True):
    """Plot a single biomarker trajectory with confidence bands."""
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(10, 5))
        standalone = True
    else:
        standalone = False

    months = MONTHS
    opt, exp, pes = biomarker.compute_trajectories(months)

    # Confidence bands
    ax.fill_between(months, pes, opt, alpha=0.15, color='steelblue', label='Range (optimistic-pessimistic)')
    ax.plot(months, exp, 'b-', linewidth=2, label='Expected trajectory')
    ax.plot(months, opt, 'g--', linewidth=1, alpha=0.7, label='Optimistic')
    ax.plot(months, pes, 'r--', linewidth=1, alpha=0.7, label='Pessimistic')

    # Baseline
    ax.axhline(y=biomarker.baseline_mean, color='gray', linestyle=':', linewidth=1, alpha=0.5)
    ax.annotate('Baseline', xy=(0.5, biomarker.baseline_mean), fontsize=7, color='gray', alpha=0.7)

    # Success threshold
    if biomarker.success_threshold is not None:
        ax.axhline(y=biomarker.success_threshold, color='green', linestyle='--', linewidth=1.5, alpha=0.6)
        side = "above" if biomarker.direction == "higher_is_better" else "below"
        ax.annotate(f'Success: {side} {biomarker.success_threshold} {biomarker.unit}',
                    xy=(18, biomarker.success_threshold), fontsize=7, color='green',
                    va='bottom' if biomarker.direction == "higher_is_better" else 'top')

    # Safety threshold
    if biomarker.safety_threshold is not None:
        ax.axhline(y=biomarker.safety_threshold, color='red', linestyle='-', linewidth=2, alpha=0.6)
        ax.annotate(f'SAFETY LIMIT: {biomarker.safety_threshold} {biomarker.unit}',
                    xy=(18, biomarker.safety_threshold), fontsize=7, color='red', fontweight='bold',
                    va='bottom')

    # Normal range
    if biomarker.normal_range and biomarker.normal_range[0] is not None and biomarker.normal_range[1] is not None:
        ax.axhspan(biomarker.normal_range[0], biomarker.normal_range[1],
                    alpha=0.05, color='green', label='Normal range')

    # Decision point markers at clinical visit months
    if show_decisions and biomarker.decision_points:
        for key, text in biomarker.decision_points.items():
            if key.startswith("month_"):
                try:
                    m = int(key.split("_")[1])
                    _, exp_at_m, _ = biomarker.compute_trajectories(np.array([float(m)]))
                    ax.plot(m, exp_at_m[0], 'ko', markersize=8, zorder=5)
                    # Truncate text for readability
                    short_text = text[:60] + "..." if len(text) > 60 else text
                    ax.annotate(short_text, xy=(m, exp_at_m[0]),
                                xytext=(m + 1, exp_at_m[0]),
                                fontsize=5.5, color='black', alpha=0.8,
                                arrowprops=dict(arrowstyle='->', color='gray', lw=0.5),
                                bbox=dict(boxstyle='round,pad=0.2', facecolor='lightyellow',
                                          edgecolor='gray', alpha=0.8))
                except (ValueError, IndexError):
                    pass

    ax.set_xlabel('Months on Protocol', fontsize=10)
    ax.set_ylabel(f'{biomarker.name} ({biomarker.unit})', fontsize=10)
    ax.set_title(f'{biomarker.name} — Expected Trajectory on Protocol\n'
                 f'[Tier {biomarker.tier}: {biomarker.category}]',
                 fontsize=11, fontweight='bold')
    ax.set_xlim(0, 24)
    ax.set_xticks(MONTH_LABELS)
    ax.legend(fontsize=7, loc='best')
    ax.grid(True, alpha=0.3)

    if standalone:
        plt.tight_layout()
        return fig, ax
    return ax


def plot_all_biomarkers():
    """Generate individual plots for each biomarker and a summary dashboard."""

    # Individual plots
    for bm in BIOMARKERS:
        fig, ax = plot_single_biomarker(bm)
        fname = bm.name.lower().replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")
        filepath = os.path.join(OUTPUT_DIR, f"trajectory_{fname}.png")
        fig.savefig(filepath, dpi=150, bbox_inches='tight')
        plt.close(fig)
        print(f"  Saved: {filepath}")

    # Summary dashboard: Tier 1 biomarkers in a grid
    tier1 = [b for b in BIOMARKERS if b.tier == 1]
    n = len(tier1)
    cols = 2
    rows = (n + 1) // 2

    fig, axes = plt.subplots(rows, cols, figsize=(16, 4 * rows))
    axes = axes.flatten()

    for i, bm in enumerate(tier1):
        plot_single_biomarker(bm, ax=axes[i], show_decisions=False)

    # Hide unused subplots
    for i in range(n, len(axes)):
        axes[i].set_visible(False)

    fig.suptitle('Tier 1 Biomarker Dashboard — the patient Protocol\n'
                 'Expected trajectories over 24 months with optimistic/pessimistic bands',
                 fontsize=14, fontweight='bold', y=1.02)
    fig.tight_layout()
    dashboard_path = os.path.join(OUTPUT_DIR, "dashboard_tier1_biomarkers.png")
    fig.savefig(dashboard_path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"  Saved: {dashboard_path}")

    # Decision timeline plot
    plot_decision_timeline()

    return dashboard_path


def plot_decision_timeline():
    """
    Plot a visual timeline showing decision points across all biomarkers.
    This is the clinician's at-a-glance guide.
    """
    fig, ax = plt.subplots(1, 1, figsize=(16, 10))

    # Collect all decision points
    decisions = []
    for bm in BIOMARKERS:
        for key, text in bm.decision_points.items():
            if key.startswith("month_"):
                parts = key.split("_")
                try:
                    month = int(parts[1])
                    dtype = "success" if "success" in key.lower() else "decision"
                    decisions.append((month, bm.name, text, bm.tier, dtype))
                except ValueError:
                    pass
            elif key.startswith("any_visit"):
                decisions.append((None, bm.name, text, bm.tier, "safety"))

    # Sort by month
    timed = sorted([d for d in decisions if d[0] is not None], key=lambda x: x[0])
    safety = [d for d in decisions if d[0] is None]

    # Plot timed decisions
    y_pos = 0
    colors_map = {"decision": "#2196F3", "success": "#4CAF50", "safety": "#F44336"}
    tier_colors = {1: "#1a5276", 2: "#1a6e3e", 3: "#6c3483"}

    for month, name, text, tier, dtype in timed:
        color = colors_map.get(dtype, "#666666")
        ax.barh(y_pos, 0.3, left=month - 0.15, height=0.6, color=color, alpha=0.8)
        label = f"[T{tier}] {name}: {text}"
        if len(label) > 100:
            label = label[:97] + "..."
        ax.text(month + 0.5, y_pos, label, fontsize=6.5, va='center',
                fontfamily='sans-serif')
        y_pos -= 1

    # Safety alerts at top
    if safety:
        y_pos -= 0.5
        ax.text(0, y_pos, "SAFETY ALERTS (check at every visit):", fontsize=8,
                fontweight='bold', color='red')
        y_pos -= 0.8
        for _, name, text, tier, dtype in safety:
            label = f"  {name}: {text}"
            if len(label) > 110:
                label = label[:107] + "..."
            ax.text(0.5, y_pos, label, fontsize=6.5, color='red', va='center')
            y_pos -= 0.7

    ax.set_xlim(-0.5, 25)
    ax.set_ylim(y_pos - 1, 1)
    ax.set_xlabel('Month on Protocol', fontsize=11)
    ax.set_xticks(MONTH_LABELS)
    ax.set_yticks([])
    ax.set_title('Clinical Decision Timeline — All Biomarkers\n'
                 'Blue=decision point, Green=success criterion, Red=safety alert',
                 fontsize=12, fontweight='bold')
    ax.grid(True, axis='x', alpha=0.3)

    # Legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#2196F3', label='Decision Point'),
        Patch(facecolor='#4CAF50', label='Success Criterion'),
        Patch(facecolor='#F44336', label='Safety Alert'),
    ]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=8)

    filepath = os.path.join(OUTPUT_DIR, "decision_timeline.png")
    fig.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"  Saved: {filepath}")


# =============================================================================
# C-PEPTIDE DEEP DIVE
# =============================================================================

def cpeptide_scenario_analysis():
    """
    Detailed C-peptide analysis with multiple intervention scenarios.
    This is the single most important plot for the entire campaign.
    """
    months = MONTHS
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel A: Fasting C-peptide trajectories
    ax = axes[0, 0]
    opt, exp, pes = cpeptide_trajectory(months)
    ax.fill_between(months, pes, opt, alpha=0.12, color='steelblue')
    ax.plot(months, exp, 'b-', lw=2, label='Protocol (expected)')
    ax.plot(months, opt, 'g--', lw=1.5, label='Protocol (optimistic)')
    ax.plot(months, pes, 'r--', lw=1.5, label='No response')

    # Add teplizumab scenario: if added at month 6
    teplizumab_boost = np.zeros_like(months)
    mask = months >= 6
    teplizumab_boost[mask] = 0.10 * (1 / (1 + np.exp(-0.4 * (months[mask] - 9))))
    ax.plot(months, exp + teplizumab_boost, 'm-', lw=1.5, label='+ Teplizumab at month 6')

    ax.axhline(y=0.20, color='green', ls=':', lw=1.5, alpha=0.7)
    ax.text(20, 0.21, 'Clinically meaningful', fontsize=7, color='green')
    ax.axhline(y=0.60, color='darkgreen', ls=':', lw=1.5, alpha=0.7)
    ax.text(20, 0.61, 'Insulin reduction possible', fontsize=7, color='darkgreen')
    ax.set_title('A: Fasting C-Peptide Trajectories', fontweight='bold')
    ax.set_ylabel('C-Peptide (nmol/L)')
    ax.set_xlabel('Months')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel B: Stimulated C-peptide
    ax = axes[0, 1]
    s_opt, s_exp, s_pes = cpeptide_stimulated_trajectory(months)
    ax.fill_between(months, s_pes, s_opt, alpha=0.12, color='steelblue')
    ax.plot(months, s_exp, 'b-', lw=2, label='Expected')
    ax.plot(months, s_opt, 'g--', lw=1.5, label='Optimistic')
    ax.plot(months, s_pes, 'r--', lw=1.5, label='Pessimistic')
    ax.axhline(y=0.60, color='green', ls=':', lw=1.5, alpha=0.7)
    ax.text(18, 0.62, 'Clinically meaningful', fontsize=7, color='green')
    ax.set_title('B: Stimulated C-Peptide (MMTT)', fontweight='bold')
    ax.set_ylabel('Stimulated C-Peptide (nmol/L)')
    ax.set_xlabel('Months')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel C: Insulin dose projection
    ax = axes[1, 0]
    baseline_insulin = 6.0  # 2u x 3 meals
    # Insulin need decreases as C-peptide rises
    # Rough model: each 0.1 nmol/L C-peptide rise = ~1u/day less insulin needed
    insulin_opt = np.maximum(0, baseline_insulin - (opt - opt[0]) * 10)
    insulin_exp = np.maximum(0, baseline_insulin - (exp - exp[0]) * 10)
    insulin_pes = np.maximum(0, baseline_insulin - np.maximum(0, pes - pes[0]) * 10)

    ax.fill_between(months, insulin_opt, insulin_pes, alpha=0.12, color='orange')
    ax.plot(months, insulin_exp, 'b-', lw=2, label='Expected')
    ax.plot(months, insulin_opt, 'g--', lw=1.5, label='Optimistic')
    ax.plot(months, insulin_pes, 'r--', lw=1.5, label='Pessimistic')
    ax.axhline(y=0, color='green', ls=':', lw=2, alpha=0.7)
    ax.text(18, 0.3, 'Insulin independence', fontsize=7, color='green', fontweight='bold')
    ax.set_title('C: Daily Insulin Dose Projection', fontweight='bold')
    ax.set_ylabel('Total Daily Insulin (units)')
    ax.set_xlabel('Months')
    ax.set_ylim(-0.5, 7)
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel D: Decision flowchart as text
    ax = axes[1, 1]
    ax.axis('off')
    decision_text = (
        "C-PEPTIDE DECISION ALGORITHM\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "MONTH 0: Baseline fasting + stimulated C-peptide\n"
        "  If fasting >0.30 nmol/L → Excellent starting position\n"
        "  If fasting 0.10-0.30 → Expected range, proceed\n"
        "  If fasting <0.10 → Minimal residual function; add\n"
        "    semaglutide from day 1\n\n"
        "MONTH 3: First check\n"
        "  If rising → Protocol working, continue\n"
        "  If flat → Increase FMD frequency to biweekly\n"
        "  If declining → Add semaglutide, refer teplizumab\n\n"
        "MONTH 6: Key decision point\n"
        "  If >0.20 → Continue, monitor quarterly\n"
        "  If <0.15 → ESCALATE: teplizumab referral\n\n"
        "MONTH 12: Primary endpoint\n"
        "  If >0.30 → SUCCESS: begin insulin taper\n"
        "  If 0.20-0.30 → Partial success: continue protocol\n"
        "  If <0.20 → Protocol insufficient alone\n\n"
        "MONTH 18-24: Long-term\n"
        "  If >0.60 → Insulin reduction/independence likely\n"
        "  Track for durability of response"
    )
    ax.text(0.05, 0.95, decision_text, transform=ax.transAxes,
            fontsize=7.5, fontfamily='monospace', va='top',
            bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='gray', alpha=0.9))
    ax.set_title('D: Clinical Decision Algorithm', fontweight='bold')

    fig.suptitle('C-Peptide Deep Dive — The Primary Endpoint\n'
                 'the patient: 67yr male, T1DM Dx 2019, 5yr insulin-free remission on keto',
                 fontsize=13, fontweight='bold', y=1.02)
    fig.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, "cpeptide_deep_dive.png")
    fig.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"  Saved: {filepath}")

    return filepath


# =============================================================================
# EXPORT
# =============================================================================

def export_trajectories_json():
    """Export all biomarker trajectories as JSON for app integration."""
    data = {
        "generated": datetime.now().isoformat(),
        "patient": PATIENT_ZERO,
        "months_modeled": 24,
        "visit_schedule_months": MONTH_LABELS,
        "biomarkers": [bm.to_dict() for bm in BIOMARKERS],
        "summary": {
            "tier_1_count": sum(1 for b in BIOMARKERS if b.tier == 1),
            "tier_2_count": sum(1 for b in BIOMARKERS if b.tier == 2),
            "tier_3_count": sum(1 for b in BIOMARKERS if b.tier == 3),
            "total_tier1_cost_per_visit": sum(b.cost_usd for b in BIOMARKERS if b.tier == 1 and b.cost_usd),
            "primary_endpoint": "Fasting C-Peptide > 0.20 nmol/L at 12 months",
            "safety_abort_criteria": [
                "Troponin I > 14 ng/L at any visit",
                "ALT > 3x ULN (>120 U/L) AND bilirubin > 2x ULN (Hy's Law)",
                "NT-proBNP > 900 pg/mL (symptomatic heart failure)",
                "hs-CRP > 10 mg/L sustained (uncontrolled infection/inflammation)",
            ],
        },
    }

    filepath = os.path.join(PROJECT_DIR, "results", "biomarker_trajectories.json")
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"  Saved: {filepath}")
    return filepath


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 70)
    print("BIOMARKER TRAJECTORY MODEL — Clinical Monitoring Bridge")
    print("the patient Protocol — T1DM + Cross-Disease Safety Monitoring")
    print("=" * 70)
    print()

    # Summary table
    print("BIOMARKER REGISTRY")
    print("-" * 90)
    print(f"{'Name':<30} {'Category':<18} {'Tier':<6} {'Baseline':<12} {'Unit':<15} {'Cost':>6}")
    print("-" * 90)
    for bm in BIOMARKERS:
        cost_str = f"${bm.cost_usd}" if bm.cost_usd else "N/A"
        print(f"{bm.name:<30} {bm.category:<18} {bm.tier:<6} {bm.baseline_mean:<12.2f} {bm.unit:<15} {cost_str:>6}")

    print()
    total_t1 = sum(b.cost_usd for b in BIOMARKERS if b.tier == 1 and b.cost_usd)
    total_t2 = sum(b.cost_usd for b in BIOMARKERS if b.tier == 2 and b.cost_usd)
    total_t3 = sum(b.cost_usd for b in BIOMARKERS if b.tier == 3 and b.cost_usd)
    print(f"Cost per visit — Tier 1 (must-have): ${total_t1}")
    print(f"Cost per visit — Tier 2 (important): ${total_t2}")
    print(f"Cost per visit — Tier 3 (nice-to-have): ${total_t3}")
    print(f"Cost per visit — ALL: ${total_t1 + total_t2 + total_t3}")
    print()

    # Trajectory values at key timepoints
    print("EXPECTED TRAJECTORIES AT CLINICAL VISITS")
    print("-" * 110)
    print(f"{'Biomarker':<30} {'M0':>8} {'M1':>8} {'M3':>8} {'M6':>8} {'M9':>8} {'M12':>8} {'M18':>8} {'M24':>8}")
    print("-" * 110)
    for bm in BIOMARKERS:
        _, exp, _ = bm.compute_trajectories(np.array(MONTH_LABELS, dtype=float))
        vals = "".join(f"{v:8.2f}" for v in exp)
        print(f"{bm.name:<30}{vals}")
    print()

    # Generate plots
    print("GENERATING PLOTS...")
    plot_all_biomarkers()
    print()

    print("GENERATING C-PEPTIDE DEEP DIVE...")
    cpeptide_scenario_analysis()
    print()

    print("EXPORTING JSON...")
    export_trajectories_json()
    print()

    # Decision summary
    print("CRITICAL DECISION POINTS")
    print("=" * 70)
    for bm in BIOMARKERS:
        if bm.decision_points:
            print(f"\n  {bm.name} ({bm.unit}):")
            for key, text in sorted(bm.decision_points.items()):
                print(f"    {key}: {text}")

    print()
    print("SAFETY ABORT CRITERIA")
    print("=" * 70)
    print("  1. Troponin I > 14 ng/L at ANY visit → STOP, cardiology consult")
    print("  2. ALT > 3x ULN (>120 U/L) → REDUCE fluoxetine; if + bilirubin > 2x ULN → STOP")
    print("  3. NT-proBNP > 900 pg/mL → STOP, urgent cardiac evaluation")
    print("  4. hs-CRP > 10 mg/L sustained → investigate infection source")
    print("  5. Any new cardiac symptoms (chest pain, dyspnea, palpitations) → immediate workup")
    print()
    print("Done.")


if __name__ == "__main__":
    main()
