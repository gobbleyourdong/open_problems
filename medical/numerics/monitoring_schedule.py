#!/usr/bin/env python3
"""
Monitoring Schedule Generator — Optimal Lab Testing Schedule for Protocol
==========================================================================

Generates the complete monitoring schedule for the patient's T1DM protocol:
  - Which tests at each visit (baseline, month 1, 3, 6, 9, 12, 18, 24)
  - Cost per test (approximate US pricing, cash-pay)
  - Total monitoring cost over 24 months
  - Priority tiers: Tier 1 (must have), Tier 2 (important), Tier 3 (nice to have)
  - Minimum monitoring set for budget-constrained patients

Outputs:
  1. Clean printable table (stdout + text file)
  2. JSON for app integration
  3. Cost summary by tier and by visit
  4. Printable PDF-ready lab order for each visit

Visit schedule rationale:
  - Month 0: Full baseline before starting protocol
  - Month 1: Fluoxetine safety check (ALT), vitamin D compliance
  - Month 3: First efficacy signal (hs-CRP, C-peptide, HbA1c)
  - Month 6: Key decision point (escalate if no C-peptide rise)
  - Month 9: Interim check
  - Month 12: Primary endpoint evaluation
  - Month 18: Durability check
  - Month 24: Final protocol assessment

Literature references:
  [1] ADA Standards of Care 2024 — monitoring guidelines for T1DM
  [2] FDA guidance on drug hepatotoxicity monitoring
  [3] Palmer 2004 Diabetes 53:250 — C-peptide thresholds
  [4] Herold 2019 NEJM 381:603 — teplizumab trial monitoring schedule

systematic approach — Clinical Monitoring Bridge — ODD Instance (numerics)
"""

import json
import os
from datetime import datetime

# =============================================================================
# OUTPUT
# =============================================================================

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
RESULTS_DIR = os.path.join(PROJECT_DIR, "results")
os.makedirs(RESULTS_DIR, exist_ok=True)

# =============================================================================
# TEST DEFINITIONS
# =============================================================================

# Visit schedule (months from protocol start)
VISITS = [0, 1, 3, 6, 9, 12, 18, 24]

# Each test: (name, code, tier, cost_usd, category, specimen, fasting_required,
#             schedule: which visits, notes)

TESTS = [
    # ==================== TIER 1: MUST HAVE ====================
    {
        "name": "Fasting C-Peptide",
        "code": "004051",
        "tier": 1,
        "cost_usd": 45,
        "category": "Beta Cell Function",
        "specimen": "Serum (fasting 12hr)",
        "fasting": True,
        "schedule": [0, 3, 6, 9, 12, 18, 24],
        "notes": "PRIMARY ENDPOINT. Gold standard for residual beta cell function. "
                 "Draw fasting AM. Previous level 0.9 ng/mL at Dx (12/2019).",
        "lab": "LabCorp/Quest",
    },
    {
        "name": "Stimulated C-Peptide (MMTT)",
        "code": "MMTT",
        "tier": 1,
        "cost_usd": 150,
        "category": "Beta Cell Function",
        "specimen": "Serum (timed draws at 0, 30, 60, 90, 120 min after Boost)",
        "fasting": True,
        "schedule": [0, 6, 12, 24],
        "notes": "THE gold standard. Mixed Meal Tolerance Test using Boost drink. "
                 "More sensitive than fasting C-peptide. Requires clinic visit with "
                 "timed blood draws. Peak C-peptide at 60-90 min is the key value.",
        "lab": "Endocrine clinic",
    },
    {
        "name": "HbA1c",
        "code": "001453",
        "tier": 1,
        "cost_usd": 20,
        "category": "Glycemic Control",
        "specimen": "Whole blood (EDTA)",
        "fasting": False,
        "schedule": [0, 3, 6, 9, 12, 18, 24],
        "notes": "Reflects 3-month average glucose. Lags real-time changes. "
                 "Target: <7.0% ADA, <6.5% on protocol.",
        "lab": "LabCorp/Quest",
    },
    {
        "name": "hs-CRP",
        "code": "120766",
        "tier": 1,
        "cost_usd": 25,
        "category": "Inflammation",
        "specimen": "Serum",
        "fasting": False,
        "schedule": [0, 1, 3, 6, 12, 24],
        "notes": "Fastest inflammation marker to respond. Expect decline within 1-3 months "
                 "if protocol reducing systemic inflammation. >10 mg/L = investigate infection.",
        "lab": "LabCorp/Quest",
    },
    {
        "name": "25-OH Vitamin D",
        "code": "081950",
        "tier": 1,
        "cost_usd": 40,
        "category": "Compliance/Immune",
        "specimen": "Serum",
        "fasting": False,
        "schedule": [0, 1, 3, 6, 12, 24],
        "notes": "Compliance marker + immune modulator. Target 50-70 ng/mL. "
                 "If >100 ng/mL, reduce dose (hypercalcemia risk).",
        "lab": "LabCorp/Quest",
    },
    {
        "name": "ALT",
        "code": "001545",
        "tier": 1,
        "cost_usd": 15,
        "category": "Hepatic Safety",
        "specimen": "Serum",
        "fasting": False,
        "schedule": [0, 1, 3, 6, 12, 18, 24],
        "notes": "Fluoxetine hepatotoxicity screen. Normal <40 U/L. "
                 "If >80 (2x ULN), recheck in 2 weeks. If >120 (3x ULN), reduce/stop fluoxetine. "
                 "Hy's Law: ALT >3x ULN + bilirubin >2x ULN = STOP immediately.",
        "lab": "LabCorp/Quest",
    },
    {
        "name": "AST",
        "code": "001123",
        "tier": 1,
        "cost_usd": 15,
        "category": "Hepatic Safety",
        "specimen": "Serum",
        "fasting": False,
        "schedule": [0, 1, 3, 6, 12, 18, 24],
        "notes": "Paired with ALT. AST/ALT ratio helps differentiate drug effect from other causes.",
        "lab": "LabCorp/Quest",
    },
    {
        "name": "Troponin I (high-sensitivity)",
        "code": "164921",
        "tier": 1,
        "cost_usd": 30,
        "category": "Cardiac Safety",
        "specimen": "Serum",
        "fasting": False,
        "schedule": [0, 6, 12, 24],
        "notes": "SAFETY MARKER. Any value >14 ng/L = active myocardial injury. "
                 "Immediate cardiology consult required. Screens for occult CVB myocarditis.",
        "lab": "LabCorp/Quest",
    },

    # ==================== TIER 2: IMPORTANT ====================
    {
        "name": "GAD65 Autoantibodies",
        "code": "164350",
        "tier": 2,
        "cost_usd": 85,
        "category": "Autoimmune Status",
        "specimen": "Serum",
        "fasting": False,
        "schedule": [0, 6, 12, 24],
        "notes": "Autoimmune marker. Slow to change. >20% decline over 6-12 months "
                 "suggests immune tolerance improving. Most persistent autoantibody in T1DM.",
        "lab": "LabCorp/Quest",
    },
    {
        "name": "IA-2 Autoantibodies",
        "code": "164355",
        "tier": 2,
        "cost_usd": 85,
        "category": "Autoimmune Status",
        "specimen": "Serum",
        "fasting": False,
        "schedule": [0, 12, 24],
        "notes": "Autoimmune marker. Combined with GAD65 for full staging. "
                 "Often declines faster than GAD65.",
        "lab": "LabCorp/Quest",
    },
    {
        "name": "Fasting Insulin",
        "code": "004333",
        "tier": 2,
        "cost_usd": 30,
        "category": "Beta Cell Function",
        "specimen": "Serum (fasting 12hr)",
        "fasting": True,
        "schedule": [0, 6, 12, 24],
        "notes": "Enables HOMA-B (beta cell function) and HOMA-IR (insulin resistance) calculation. "
                 "Important context for C-peptide interpretation. Note: exogenous insulin "
                 "must be accounted for (draw before morning dose).",
        "lab": "LabCorp/Quest",
    },
    {
        "name": "NT-proBNP",
        "code": "250913",
        "tier": 2,
        "cost_usd": 40,
        "category": "Cardiac Safety",
        "specimen": "Serum",
        "fasting": False,
        "schedule": [0, 12, 24],
        "notes": "Heart failure marker. Normal for age >65: <300 pg/mL. "
                 ">300 = cardiology referral. >900 = urgent evaluation.",
        "lab": "LabCorp/Quest",
    },
    {
        "name": "Treg Count (CD4+CD25+FoxP3+)",
        "code": "Flow cytometry panel",
        "tier": 2,
        "cost_usd": 200,
        "category": "Immune Function",
        "specimen": "Whole blood (heparinized, FRESH — must process within 6hr)",
        "fasting": False,
        "schedule": [0, 6, 12],
        "notes": "Most informative immune marker for butyrate/vitamin D response. "
                 "Requires specialized flow cytometry lab. Normal: 5-10% of CD4+. "
                 "Must process fresh — cannot ship frozen.",
        "lab": "Academic immunology lab",
    },
    {
        "name": "Lipid Panel (full fractionation)",
        "code": "303756",
        "tier": 2,
        "cost_usd": 35,
        "category": "Metabolic",
        "specimen": "Serum (fasting 12hr)",
        "fasting": True,
        "schedule": [0, 12, 24],
        "notes": "Total, LDL, HDL, VLDL, TG. Patient reports high total with low LDL/VLDL. "
                 "Track changes with protocol (FMD/keto may affect lipid profile).",
        "lab": "LabCorp/Quest",
    },
    {
        "name": "TSH",
        "code": "004259",
        "tier": 2,
        "cost_usd": 25,
        "category": "Thyroid (co-autoimmune)",
        "specimen": "Serum",
        "fasting": False,
        "schedule": [0, 12, 24],
        "notes": "ADA-recommended annual screen. Autoimmune thyroid co-occurs in 17-30% of T1DM. "
                 "If abnormal, add Free T4 and TPO antibodies.",
        "lab": "LabCorp/Quest",
    },
    {
        "name": "Glucose CV (from CGM data)",
        "code": "N/A (calculated)",
        "tier": 2,
        "cost_usd": 0,
        "category": "Glycemic Control",
        "specimen": "N/A (download from CGM software)",
        "fasting": False,
        "schedule": [0, 1, 3, 6, 9, 12, 18, 24],
        "notes": "Coefficient of variation from CGM. Target <36%. Free if already wearing CGM. "
                 "Calculate from 14-day report. Download at each visit.",
        "lab": "Patient's CGM (Dexcom/Libre)",
    },

    # ==================== TIER 3: NICE TO HAVE ====================
    {
        "name": "ZnT8 Autoantibodies",
        "code": "164382",
        "tier": 3,
        "cost_usd": 85,
        "category": "Autoimmune Status",
        "specimen": "Serum",
        "fasting": False,
        "schedule": [0, 12, 24],
        "notes": "Completes autoantibody panel. Often declines with disease duration regardless. "
                 "Lower priority than GAD65/IA-2.",
        "lab": "LabCorp/Quest",
    },
    {
        "name": "Insulin Autoantibodies (IAA)",
        "code": "086215",
        "tier": 3,
        "cost_usd": 60,
        "category": "Autoimmune Status",
        "specimen": "Serum",
        "fasting": False,
        "schedule": [0, 24],
        "notes": "May be confounded by exogenous insulin use. Baseline and endpoint only.",
        "lab": "LabCorp/Quest",
    },
    {
        "name": "Enterovirus PCR (stool RT-PCR)",
        "code": "Research",
        "tier": 3,
        "cost_usd": 150,
        "category": "Viral Status",
        "specimen": "Stool sample",
        "fasting": False,
        "schedule": [0, 6, 12, 24],
        "notes": "Detects active CVB shedding. Research-grade test — not available at standard labs. "
                 "Academic virology lab or send-out to DiViD-affiliated center.",
        "lab": "Research virology lab",
    },
    {
        "name": "Serum IFN-alpha",
        "code": "Quest 36718",
        "tier": 3,
        "cost_usd": 75,
        "category": "Viral Status",
        "specimen": "Serum",
        "fasting": False,
        "schedule": [0, 12],
        "notes": "Chronic elevation indicates persistent viral immune activation. "
                 "Marker of ongoing TLR3/RIG-I/MDA5 stimulation.",
        "lab": "Quest/specialty",
    },
    {
        "name": "Anti-CVB Neutralizing Antibodies",
        "code": "Research",
        "tier": 3,
        "cost_usd": 200,
        "category": "Viral Status",
        "specimen": "Serum",
        "fasting": False,
        "schedule": [0, 12],
        "notes": "Neutralizing vs total antibodies ratio. Low neutralizing titers may indicate "
                 "non-protective immune response. Research lab only.",
        "lab": "Research virology lab",
    },
    {
        "name": "NK Cell Cytotoxicity",
        "code": "Flow/51Cr release",
        "tier": 3,
        "cost_usd": 250,
        "category": "ME/CFS (if applicable)",
        "specimen": "Whole blood (fresh, same-day processing)",
        "fasting": False,
        "schedule": [0, 12],
        "notes": "Only if ME/CFS symptoms present. Normal: 15-40% lysis at 50:1 E:T ratio. "
                 "Requires specialized immunology lab.",
        "lab": "Specialized immunology lab",
    },
    {
        "name": "Lactate:Pyruvate Ratio",
        "code": "Specialty",
        "tier": 3,
        "cost_usd": 80,
        "category": "ME/CFS (if applicable)",
        "specimen": "Serum (exercise-free for 24hr)",
        "fasting": False,
        "schedule": [0, 12],
        "notes": "Mitochondrial function marker. Only if fatigue/PEM symptoms present. "
                 "Normal: 10-20.",
        "lab": "Specialty metabolic lab",
    },
    {
        "name": "Proinsulin:C-Peptide Ratio",
        "code": "Specialty",
        "tier": 3,
        "cost_usd": 100,
        "category": "Beta Cell Stress",
        "specimen": "Serum (fasting 12hr)",
        "fasting": True,
        "schedule": [0, 12],
        "notes": "Elevated ratio = beta cell ER stress. Stressed beta cells produce neoantigens "
                 "that amplify autoimmune attack. Decline indicates reduced beta cell stress.",
        "lab": "Specialty endocrine lab",
    },
    {
        "name": "Zonulin",
        "code": "Specialty",
        "tier": 3,
        "cost_usd": 90,
        "category": "Gut Permeability",
        "specimen": "Serum",
        "fasting": False,
        "schedule": [0, 12],
        "notes": "Intestinal permeability marker. Elevated in T1DM. "
                 "Guides gut barrier repair interventions (glutamine, zinc carnosine, butyrate).",
        "lab": "Vibrant Wellness / Genova",
    },
    {
        "name": "Echocardiogram",
        "code": "93306",
        "tier": 3,
        "cost_usd": 300,
        "category": "Cardiac Safety",
        "specimen": "Imaging (transthoracic)",
        "fasting": False,
        "schedule": [0, 12],
        "notes": "Baseline ejection fraction (EF). Normal >55%. "
                 "Screens for occult CVB cardiomyopathy. Repeat annually or if troponin rises.",
        "lab": "Cardiology/imaging center",
    },
    {
        "name": "Microbiome 16S Sequencing",
        "code": "N/A (consumer)",
        "tier": 3,
        "cost_usd": 150,
        "category": "Gut Microbiome",
        "specimen": "Stool sample (kit)",
        "fasting": False,
        "schedule": [0, 12],
        "notes": "Profiles gut bacteria. Key targets: butyrate producers (Faecalibacterium, Roseburia) "
                 "and D-lactate producers. Consumer kits: Viome, Ombre, or clinical GI-MAP.",
        "lab": "Viome / Ombre / GI-MAP",
    },
    {
        "name": "D-Lactate (serum)",
        "code": "Specialty",
        "tier": 3,
        "cost_usd": 75,
        "category": "Gut Metabolic",
        "specimen": "Serum",
        "fasting": True,
        "schedule": [0, 12],
        "notes": "D-lactate from gut bacteria may drive inappropriate gluconeogenesis. "
                 "Elevated levels may partly explain glucose excursions beyond dietary carbs.",
        "lab": "Genova / Doctor's Data",
    },
]


# =============================================================================
# SCHEDULE MATRIX
# =============================================================================

def build_schedule_matrix():
    """Build the complete schedule matrix: tests x visits."""
    matrix = {}
    for test in TESTS:
        row = {}
        for visit in VISITS:
            row[visit] = visit in test["schedule"]
        matrix[test["name"]] = row
    return matrix


def compute_visit_costs(tier_filter=None):
    """Compute cost at each visit, optionally filtered by tier."""
    costs = {v: 0 for v in VISITS}
    for test in TESTS:
        if tier_filter is not None and test["tier"] != tier_filter:
            continue
        for visit in test["schedule"]:
            costs[visit] += test["cost_usd"]
    return costs


def compute_total_cost(tier_filter=None):
    """Total cost over 24 months."""
    costs = compute_visit_costs(tier_filter)
    return sum(costs.values())


# =============================================================================
# PRINTABLE TABLE
# =============================================================================

def print_schedule_table(tier_max=3, file=None):
    """Print a clean, clinician-readable schedule table."""
    import sys
    out = file or sys.stdout

    def w(text=""):
        print(text, file=out)

    w("=" * 130)
    w("MONITORING SCHEDULE — the patient T1DM Protocol")
    w("24-month monitoring plan with cost estimates")
    w("=" * 130)
    w()

    for tier in range(1, tier_max + 1):
        tier_tests = [t for t in TESTS if t["tier"] == tier]
        if not tier_tests:
            continue

        tier_labels = {1: "MUST HAVE", 2: "IMPORTANT", 3: "NICE TO HAVE"}
        w(f"{'─' * 130}")
        w(f"TIER {tier}: {tier_labels[tier]}")
        w(f"{'─' * 130}")

        # Header
        header = f"{'Test':<35} {'$':>5} {'Cat':<18}"
        for v in VISITS:
            header += f" {'M'+str(v):>4}"
        header += f" {'Total':>7}"
        w(header)
        w("-" * 130)

        tier_total = 0
        for test in tier_tests:
            row = f"{test['name']:<35} {test['cost_usd']:>5}"
            row += f" {test['category'][:17]:<18}"
            test_total = 0
            for v in VISITS:
                if v in test["schedule"]:
                    row += f" {'  X ':>4}"
                    test_total += test["cost_usd"]
                else:
                    row += f" {'  . ':>4}"
            row += f" ${test_total:>5}"
            tier_total += test_total
            w(row)

        w(f"{'':>60}{'TIER ' + str(tier) + ' SUBTOTAL':>56} ${tier_total:>5}")
        w()

    # Grand total
    w("=" * 130)
    w("COST SUMMARY")
    w("=" * 130)
    for tier in range(1, 4):
        total = compute_total_cost(tier)
        w(f"  Tier {tier} total (24 months): ${total:,}")
    grand = compute_total_cost()
    w(f"  {'GRAND TOTAL (24 months)':>30}: ${grand:,}")
    w()

    # Per-visit breakdown
    w("COST PER VISIT")
    w("-" * 80)
    w(f"  {'Visit':<10} {'Tier 1':>10} {'Tier 2':>10} {'Tier 3':>10} {'Total':>10}")
    w(f"  {'-'*50}")
    for v in VISITS:
        c1 = sum(t["cost_usd"] for t in TESTS if t["tier"] == 1 and v in t["schedule"])
        c2 = sum(t["cost_usd"] for t in TESTS if t["tier"] == 2 and v in t["schedule"])
        c3 = sum(t["cost_usd"] for t in TESTS if t["tier"] == 3 and v in t["schedule"])
        w(f"  Month {v:<4} ${c1:>8,} ${c2:>8,} ${c3:>8,} ${c1+c2+c3:>8,}")
    w()

    # Minimum monitoring set
    w("=" * 130)
    w("MINIMUM MONITORING SET (budget-constrained)")
    w("If you can only afford some tests, prioritize in this order:")
    w("=" * 130)
    w()
    w("  ABSOLUTE MINIMUM ($425 over 24 months):")
    w("    1. Fasting C-Peptide — M0, M6, M12     (3 x $45  = $135) — THE primary endpoint")
    w("    2. HbA1c — M0, M6, M12                  (3 x $20  = $ 60) — glycemic control")
    w("    3. ALT — M0, M1, M3, M6, M12            (5 x $15  = $ 75) — fluoxetine safety")
    w("    4. Vitamin D — M0, M3                    (2 x $40  = $ 80) — compliance check")
    w("    5. hs-CRP — M0, M3                       (2 x $25  = $ 50) — inflammation baseline")
    w("    6. CGM glucose CV — every visit           (free)            — from existing CGM")
    w("    7. Daily insulin dose log — continuous     (free)            — THE functional metric")
    w()
    w("  ADD IF POSSIBLE ($200 more):")
    w("    8. GAD65 antibodies — M0, M12            (2 x $85  = $170) — autoimmune tracking")
    w("    9. Troponin I — M0                        (1 x $30  = $ 30) — cardiac safety baseline")
    w()
    w("  THE FREE METRICS (track these regardless):")
    w("    - Daily insulin dose (THE most important functional metric)")
    w("    - CGM time-in-range and glucose CV")
    w("    - Subjective energy, sleep quality, mood (1-10 daily log)")
    w("    - Weight (weekly)")
    w()
    w("  THE CHEAPEST SIGNAL:")
    w("    If insulin dose is trending DOWN while HbA1c is stable or improving,")
    w("    the protocol is working. This costs $0 to measure.")
    w()

    # Fasting requirements
    w("=" * 130)
    w("SPECIMEN COLLECTION NOTES")
    w("=" * 130)
    w()
    w("  FASTING REQUIRED (12-hour overnight fast, water permitted):")
    fasting_tests = [t["name"] for t in TESTS if t["fasting"]]
    for t in fasting_tests:
        w(f"    - {t}")
    w()
    w("  NON-FASTING:")
    nonfasting = [t["name"] for t in TESTS if not t["fasting"]]
    for t in nonfasting:
        w(f"    - {t}")
    w()
    w("  SPECIAL HANDLING:")
    w("    - Treg flow cytometry: FRESH blood, process within 6 hours. Cannot freeze/ship.")
    w("    - NK cytotoxicity: FRESH blood, same-day processing.")
    w("    - Stimulated C-peptide (MMTT): Clinic visit, timed draws over 2 hours.")
    w("    - Enterovirus PCR: Stool sample, ship frozen to research lab.")
    w("    - Microbiome 16S: Stool kit, follow kit instructions (ship within 24hr).")
    w()

    return grand


# =============================================================================
# JSON EXPORT
# =============================================================================

def export_schedule_json():
    """Export the complete monitoring schedule as JSON."""
    schedule = {
        "generated": datetime.now().isoformat(),
        "visit_months": VISITS,
        "tests": [],
        "cost_summary": {
            "tier_1_total_24mo": compute_total_cost(1),
            "tier_2_total_24mo": compute_total_cost(2),
            "tier_3_total_24mo": compute_total_cost(3),
            "grand_total_24mo": compute_total_cost(),
        },
        "per_visit_costs": {},
        "minimum_monitoring_set": {
            "total_cost_24mo": 425,
            "tests": [
                {"name": "Fasting C-Peptide", "visits": [0, 6, 12], "cost": 135},
                {"name": "HbA1c", "visits": [0, 6, 12], "cost": 60},
                {"name": "ALT", "visits": [0, 1, 3, 6, 12], "cost": 75},
                {"name": "25-OH Vitamin D", "visits": [0, 3], "cost": 80},
                {"name": "hs-CRP", "visits": [0, 3], "cost": 50},
                {"name": "Glucose CV (CGM)", "visits": "every visit", "cost": 0},
                {"name": "Daily insulin dose log", "visits": "continuous", "cost": 0},
            ],
            "add_if_possible": [
                {"name": "GAD65 Autoantibodies", "visits": [0, 12], "cost": 170},
                {"name": "Troponin I", "visits": [0], "cost": 30},
            ],
        },
        "safety_abort_criteria": [
            {
                "marker": "Troponin I",
                "threshold": ">14 ng/L",
                "action": "STOP protocol. Immediate cardiology consult.",
            },
            {
                "marker": "ALT",
                "threshold": ">120 U/L (3x ULN)",
                "action": "Reduce fluoxetine to 10mg. If ALT + bilirubin elevated (Hy's Law), STOP.",
            },
            {
                "marker": "NT-proBNP",
                "threshold": ">900 pg/mL",
                "action": "Urgent cardiac evaluation. Likely symptomatic heart failure.",
            },
            {
                "marker": "hs-CRP",
                "threshold": ">10 mg/L sustained",
                "action": "Investigate infection source. Not protocol-related.",
            },
        ],
    }

    # Build per-test entries
    for test in TESTS:
        entry = {
            "name": test["name"],
            "code": test["code"],
            "tier": test["tier"],
            "cost_usd": test["cost_usd"],
            "category": test["category"],
            "specimen": test["specimen"],
            "fasting_required": test["fasting"],
            "schedule_months": test["schedule"],
            "lab": test["lab"],
            "notes": test["notes"],
            "total_cost_24mo": test["cost_usd"] * len(test["schedule"]),
        }
        schedule["tests"].append(entry)

    # Per-visit cost breakdown
    for v in VISITS:
        visit_tests = [t for t in TESTS if v in t["schedule"]]
        schedule["per_visit_costs"][f"month_{v}"] = {
            "tests": [t["name"] for t in visit_tests],
            "tier_1_cost": sum(t["cost_usd"] for t in visit_tests if t["tier"] == 1),
            "tier_2_cost": sum(t["cost_usd"] for t in visit_tests if t["tier"] == 2),
            "tier_3_cost": sum(t["cost_usd"] for t in visit_tests if t["tier"] == 3),
            "total_cost": sum(t["cost_usd"] for t in visit_tests),
            "fasting_required": any(t["fasting"] for t in visit_tests),
            "special_labs_needed": [t["lab"] for t in visit_tests
                                     if t["lab"] not in ("LabCorp/Quest", "N/A (calculated)",
                                                          "Patient's CGM (Dexcom/Libre)")],
        }

    filepath = os.path.join(RESULTS_DIR, "monitoring_schedule.json")
    with open(filepath, 'w') as f:
        json.dump(schedule, f, indent=2)
    print(f"  Saved: {filepath}")
    return filepath


# =============================================================================
# VISIT-SPECIFIC LAB ORDERS
# =============================================================================

def print_visit_lab_order(month, tier_max=3, file=None):
    """Print a lab order for a specific visit, ready to hand to a physician."""
    import sys
    out = file or sys.stdout

    def w(text=""):
        print(text, file=out)

    visit_tests = [t for t in TESTS if month in t["schedule"] and t["tier"] <= tier_max]
    fasting_needed = any(t["fasting"] for t in visit_tests)

    w(f"{'=' * 80}")
    w(f"LAB ORDER — Month {month} Visit")
    w(f"the patient Protocol — T1DM Monitoring")
    w(f"{'=' * 80}")
    w()
    w(f"  Patient: Adult male, 67yr, T1DM Dx 12/2019")
    w(f"  Protocol: Antiviral + immune retraining + regeneration")
    w(f"  Fasting required: {'YES (12-hour overnight)' if fasting_needed else 'No'}")
    w()

    for tier in range(1, tier_max + 1):
        tier_tests = [t for t in visit_tests if t["tier"] == tier]
        if not tier_tests:
            continue

        tier_labels = {1: "MUST HAVE", 2: "IMPORTANT", 3: "IF ACCESSIBLE"}
        w(f"  --- Tier {tier}: {tier_labels[tier]} ---")
        for t in tier_tests:
            fasting_note = " [FASTING]" if t["fasting"] else ""
            w(f"  [ ] {t['name']:<35} Code: {t['code']:<15} ${t['cost_usd']:>5}{fasting_note}")
            w(f"       {t['notes'][:90]}")
        w()

    total = sum(t["cost_usd"] for t in visit_tests)
    w(f"  Estimated cost this visit: ${total}")
    tier1_cost = sum(t["cost_usd"] for t in visit_tests if t["tier"] == 1)
    w(f"  Tier 1 only: ${tier1_cost}")
    w()


# =============================================================================
# MAIN
# =============================================================================

def main():
    print()
    print("=" * 70)
    print("MONITORING SCHEDULE GENERATOR")
    print("the patient Protocol — T1DM + Cross-Disease Safety")
    print("=" * 70)
    print()

    # Print full schedule table
    grand = print_schedule_table(tier_max=3)
    print()

    # Print individual visit lab orders
    print("=" * 80)
    print("VISIT-SPECIFIC LAB ORDERS (bring to your doctor)")
    print("=" * 80)
    for month in VISITS:
        print_visit_lab_order(month, tier_max=2)

    # Export JSON
    print("\nEXPORTING JSON...")
    json_path = export_schedule_json()

    # Save text version
    text_path = os.path.join(RESULTS_DIR, "monitoring_schedule.txt")
    with open(text_path, 'w') as f:
        print_schedule_table(tier_max=3, file=f)
        f.write("\n\n")
        for month in VISITS:
            print_visit_lab_order(month, tier_max=2, file=f)
    print(f"  Saved: {text_path}")

    # Summary
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"  Total tests defined: {len(TESTS)}")
    print(f"  Tier 1 (must have): {sum(1 for t in TESTS if t['tier'] == 1)}")
    print(f"  Tier 2 (important): {sum(1 for t in TESTS if t['tier'] == 2)}")
    print(f"  Tier 3 (nice to have): {sum(1 for t in TESTS if t['tier'] == 3)}")
    print()
    print(f"  24-month cost (Tier 1 only): ${compute_total_cost(1):,}")
    print(f"  24-month cost (Tier 1+2):    ${compute_total_cost(1) + compute_total_cost(2):,}")
    print(f"  24-month cost (all tiers):   ${compute_total_cost():,}")
    print()
    print(f"  Minimum monitoring set: ~$425 over 24 months")
    print(f"  Most expensive single visit: Month 0 (baseline — all tests)")
    print()
    print(f"  Cheapest signal that the protocol is working:")
    print(f"    Insulin dose trending DOWN + HbA1c stable/improving = $0")
    print()
    print("Done.")


if __name__ == "__main__":
    main()
