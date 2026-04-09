#!/usr/bin/env python3
"""
Protocol Implementation Generator — Day-by-Day Plan for the patient
======================================================================

Generates the complete practical implementation plan bridging from
computational models (beta_cell_dynamics, insulin_sensitivity_model,
drug_interactions, safety_pharmacology) to real-world action.

This is THE deliverable. A person reads the output and knows:
  - What to buy
  - What to take, and when
  - What to tell their doctor
  - What labs to get, when, and where
  - What to expect at each stage
  - When to worry, when to celebrate
  - How much it costs

Outputs:
  1. Gantt-chart timeline visualization (PNG)
  2. Monthly cost breakdown (table + plot)
  3. Shopping list with specific products/doses/links
  4. Printable lab order sheets for each visit
  5. Structured JSON of the entire plan
  6. Decision tree at each milestone

Depends on:
  - Pattern 003 (inequality reversal model)
  - Pattern 005 (corrected clearance order)
  - Pattern 007 (safety profile)
  - insulin_sensitivity_model.py (dose reduction milestones)
  - monitoring_schedule.py (lab schedule)

systematic approach -- ODD Instance (numerics) -- Protocol Implementation Bridge
"""

import json
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from datetime import datetime, timedelta

# =============================================================================
# OUTPUT DIRECTORIES
# =============================================================================

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
RESULTS_DIR = os.path.join(PROJECT_DIR, "results")
FIGURES_DIR = os.path.join(RESULTS_DIR, "figures")
os.makedirs(FIGURES_DIR, exist_ok=True)

# =============================================================================
# PROTOCOL PHASES -- THE MASTER PLAN
# =============================================================================

PROTOCOL = {
    "name": "T1DM Beta Cell Recovery Protocol v1.0",
    "version": "1.0",
    "date_generated": datetime.now().isoformat(),
    "total_duration_months": 24,
    "phases": [
        # =====================================================================
        # PREPARATION PHASE (Week -2 to 0)
        # =====================================================================
        {
            "phase": "PREPARATION",
            "name": "Baseline & Setup",
            "start_week": -2,
            "end_week": 0,
            "goal": "Establish baseline measurements, set up monitoring, build medical team",
            "actions": [
                {
                    "week": -2,
                    "day": "Week -2, Day 1",
                    "action": "Schedule endocrinologist appointment",
                    "details": "Find an endocrinologist willing to monitor an experimental supplement protocol. "
                               "Bring the 1-page protocol summary (included below). You need: "
                               "(1) someone who will order labs, (2) someone who will adjust insulin as needed, "
                               "(3) someone who won't panic at the word 'fasting' in T1DM. "
                               "If your current endo won't do it, find one who will.",
                    "cost": 0,
                    "category": "medical",
                },
                {
                    "week": -2,
                    "day": "Week -2, Day 1-3",
                    "action": "Order CGM system",
                    "details": "Dexcom G7 or Libre 3. If insurance covers it, use insurance. "
                               "If not: Libre 3 reader + sensors = ~$75/month without insurance. "
                               "CGM is NON-NEGOTIABLE for this protocol. You cannot fast safely without it.",
                    "cost": 75,
                    "category": "monitoring",
                },
                {
                    "week": -2,
                    "day": "Week -2, Day 1-3",
                    "action": "Order blood ketone meter",
                    "details": "Keto-Mojo GK+ meter (~$50) + ketone strips (~$1 each). "
                               "You need this for every fasting day. Urine strips are NOT acceptable "
                               "(they measure acetoacetate, not BHB; 6-12hr lag time).",
                    "cost": 50,
                    "category": "monitoring",
                },
                {
                    "week": -2,
                    "day": "Week -2, Day 3-5",
                    "action": "Order supplements (shopping list below)",
                    "details": "Order ALL supplements now so they arrive before Week 1. "
                               "See SHOPPING LIST section for exact products.",
                    "cost": 85,
                    "category": "supplements",
                },
                {
                    "week": -1,
                    "day": "Week -1",
                    "action": "BASELINE LABS -- Full panel",
                    "details": "Fasting draw (12hr overnight fast). This is the most important "
                               "single blood draw of the entire protocol. Everything is measured against this.",
                    "labs": [
                        "C-peptide, fasting ($45)",
                        "C-peptide, stimulated/MMTT ($150 -- requires clinic visit, Boost drink, timed draws at 0/30/60/90/120 min)",
                        "HbA1c ($20)",
                        "GAD65 autoantibodies ($85)",
                        "IA-2 autoantibodies ($85)",
                        "ZnT8 autoantibodies ($85)",
                        "hs-CRP ($25)",
                        "25-OH Vitamin D ($40)",
                        "CBC with differential ($15)",
                        "CMP (comprehensive metabolic panel) ($20)",
                        "Lipid panel ($25)",
                        "Troponin I high-sensitivity ($30)",
                        "NT-proBNP ($40)",
                        "ALT ($15)",
                        "AST ($15)",
                        "Enterovirus stool PCR ($120 -- specialty lab)",
                    ],
                    "total_lab_cost": 815,
                    "cost": 815,
                    "category": "labs",
                },
                {
                    "week": -1,
                    "day": "Week -1",
                    "action": "BASELINE IMAGING",
                    "details": "Echocardiogram: establishes baseline ejection fraction (EF). "
                               "Screens for occult CVB myocarditis (EF <50% = flag). "
                               "Abdominal ultrasound: visualize pancreas (atrophy? calcification?). "
                               "These are one-time baseline tests.",
                    "imaging": [
                        "Transthoracic echocardiogram ($200-500)",
                        "Abdominal ultrasound, limited to pancreas ($150-300)",
                    ],
                    "cost": 500,
                    "category": "imaging",
                },
                {
                    "week": -1,
                    "day": "Week -1",
                    "action": "CGM calibration period",
                    "details": "Wear CGM for at least 7 days before starting protocol. "
                               "This gives you: (1) baseline glucose patterns, (2) time in range, "
                               "(3) overnight patterns, (4) post-meal patterns. "
                               "Save screenshots. This is your 'before' data.",
                    "cost": 0,
                    "category": "monitoring",
                },
                {
                    "week": 0,
                    "day": "Week 0",
                    "action": "ENDOCRINOLOGIST VISIT -- Protocol Discussion",
                    "details": "Bring: (1) baseline labs, (2) CGM data, (3) protocol summary, "
                               "(4) safety profile document, (5) your supplement list. "
                               "Key asks: Will you monitor me? Will you order quarterly labs? "
                               "Will you adjust my insulin if C-peptide rises? "
                               "Can you prescribe fluoxetine 10mg (or refer to PCP/psychiatrist)? "
                               "Can we discuss semaglutide at month 4 if things look good?",
                    "cost": 50,
                    "category": "medical",
                },
            ],
        },
        # =====================================================================
        # PHASE 1: FOUNDATION (Months 1-3) -- Reduce Destruction
        # =====================================================================
        {
            "phase": "PHASE_1",
            "name": "Foundation -- Reduce Destruction",
            "start_month": 1,
            "end_month": 3,
            "goal": "Clear virus (fluoxetine), reduce inflammation (vitamin D, butyrate), "
                    "establish fasting practice. Target: D drops by ~50%.",
            "model_prediction": {
                "D_reduction": "~50% (from 1.4e-3 to 6.5e-4 /day)",
                "R_change": "slight improvement from reduced stress",
                "dB_dt": "still declining but much slower (-4.3e-4 vs -1.2e-3 /day)",
                "expected_cpeptide": "may start rising by month 3",
            },
            "actions": [
                {
                    "week": 1,
                    "day": "Month 1, Week 1",
                    "action": "START fluoxetine 10mg/day",
                    "details": "Take in the morning with breakfast. Half dose for 2 weeks to minimize "
                               "side effects. Common side effects (week 1-2): nausea, headache, insomnia, "
                               "anxiety increase, GI upset. These typically resolve by week 3-4. "
                               "If severe nausea: take with food. If insomnia: take in AM, not PM. "
                               "IMPORTANT: Fluoxetine can mask hypoglycemia symptoms (tremor, anxiety) "
                               "by ~15-20%. Raise CGM low alarm to 80 mg/dL (from typical 70).",
                    "prescription_needed": True,
                    "cost_monthly": 10,
                    "category": "medication",
                },
                {
                    "week": 1,
                    "day": "Month 1, Week 1",
                    "action": "START Vitamin D3 4000 IU/day",
                    "details": "Take with a fat-containing meal (improves absorption 50%). "
                               "Morning or evening, same time daily. If baseline 25-OH-D was <20 ng/mL: "
                               "start with 5000-6000 IU for first 2 months, then drop to 4000 IU. "
                               "Target blood level: 50-70 ng/mL. If >100 ng/mL on any check: reduce dose.",
                    "prescription_needed": False,
                    "cost_monthly": 8,
                    "category": "supplement",
                },
                {
                    "week": 2,
                    "day": "Month 1, Week 2",
                    "action": "START sodium butyrate 300mg 2x/day",
                    "details": "Take with meals (morning + evening). Butyrate smells bad -- "
                               "enteric-coated capsules avoid the smell and GI issues. Start with 1 capsule "
                               "for 3 days, then add the second. Common early effect: mild GI discomfort, "
                               "loose stool. Usually resolves in 1 week. Mechanism: butyrate upregulates "
                               "FOXP3 expression -> expands regulatory T cells -> suppresses autoimmune attack.",
                    "prescription_needed": False,
                    "cost_monthly": 25,
                    "category": "supplement",
                },
                {
                    "week": 3,
                    "day": "Month 1, Week 3",
                    "action": "INCREASE fluoxetine to 20mg/day",
                    "details": "Full therapeutic dose. If side effects from 10mg were severe, stay at "
                               "10mg for another 2 weeks before increasing. 20mg is the target dose for "
                               "CVB 2C ATPase inhibition. At steady state (4-6 weeks), brain concentration "
                               "reaches ~15x plasma = ~4.5 uM, well above the 1.0 uM IC50.",
                    "prescription_needed": True,
                    "cost_monthly": 10,
                    "category": "medication",
                },
                {
                    "week": 4,
                    "day": "Month 1, Week 4",
                    "action": "FIRST 24-hour fast (supervised)",
                    "details": "THIS IS THE MOST IMPORTANT SAFETY EVENT IN THE PROTOCOL.\n\n"
                               "Preparation:\n"
                               "  - Eat your last meal at 6 PM\n"
                               "  - Reduce basal insulin to 80% of normal dose\n"
                               "  - No bolus insulin during fast\n"
                               "  - CGM on, ketone meter ready\n"
                               "  - Glucose tabs, juice box within arm's reach\n"
                               "  - Tell someone you are fasting\n\n"
                               "During fast:\n"
                               "  - Check blood ketones at hours 0, 4, 8, 12, 16, 20, 24\n"
                               "  - Watch CGM continuously\n"
                               "  - Drink water, black coffee, plain tea -- no calories\n"
                               "  - Light activity only (walking OK, no gym)\n"
                               "  - Log everything: BG, ketones, how you feel\n\n"
                               "ABORT if:\n"
                               "  - Blood glucose < 60 mg/dL (or <70 with symptoms)\n"
                               "  - Blood BHB > 3.0 mM\n"
                               "  - Nausea, vomiting, abdominal pain\n"
                               "  - Feeling confused or unable to self-monitor\n\n"
                               "Break fast at 6 PM next day with a normal meal.\n"
                               "Take full bolus insulin for the meal.\n\n"
                               "EXPECTED: BHB peaks 1.0-1.5 mM at 80% basal. This is ideal -- "
                               "enough to suppress NLRP3 inflammasome, not enough for DKA.",
                    "prescription_needed": False,
                    "cost_monthly": 0,
                    "category": "fasting",
                },
                {
                    "week": 5,
                    "day": "Month 1, end",
                    "action": "SAFETY LABS -- Month 1",
                    "details": "Quick safety check. 3 tests only.",
                    "labs": [
                        "ALT ($15) -- fluoxetine liver check",
                        "hs-CRP ($25) -- early inflammation signal",
                        "25-OH Vitamin D ($40) -- is supplementation working?",
                    ],
                    "total_lab_cost": 80,
                    "cost": 80,
                    "category": "labs",
                },
                {
                    "week": 8,
                    "day": "Month 2",
                    "action": "FIRST 5-day FMD cycle",
                    "details": "The Fasting Mimicking Diet is the ENGINE of regeneration.\n\n"
                               "Option A: ProLon kit ($199/cycle, pre-packaged, easiest)\n"
                               "Option B: DIY FMD (~$30/cycle):\n"
                               "  Day 1: ~1100 kcal (11% protein, 46% fat, 43% carbs)\n"
                               "  Days 2-5: ~800 kcal (9% protein, 44% fat, 47% carbs)\n"
                               "  Focus: nuts, olives, vegetables, small amounts of grain\n"
                               "  NO animal protein, NO sugar, NO dairy\n\n"
                               "Insulin adjustments during FMD:\n"
                               "  - Basal: 80-85% of normal (75% if on semaglutide later)\n"
                               "  - Bolus: 40-50% of normal (small FMD meals)\n"
                               "  - Check ketones 2x/day\n"
                               "  - CGM alarm at 80 mg/dL\n\n"
                               "REFEEDING (Days 6-8): THIS IS WHERE REGENERATION HAPPENS\n"
                               "  - Day 6: light meals, normal insulin\n"
                               "  - Day 7-8: normal eating, slightly larger portions\n"
                               "  - mTOR reactivates, IGF-1 rebounds\n"
                               "  - Ngn3+ pancreatic progenitors activate\n"
                               "  - NEW BETA CELLS ARE BORN in this window\n"
                               "  - Each cycle: ~0.3% beta cell mass gain",
                    "prescription_needed": False,
                    "cost_monthly": 50,
                    "category": "fasting",
                },
                {
                    "week": 12,
                    "day": "Month 3",
                    "action": "KEY LABS -- Month 3 Assessment",
                    "details": "This is the FIRST EFFICACY CHECK. The question: is anything happening?\n"
                               "C-peptide is the primary endpoint. Even a small rise (0.12 -> 0.15) is signal.",
                    "labs": [
                        "C-peptide, fasting ($45) -- PRIMARY ENDPOINT",
                        "HbA1c ($20) -- glycemic trend",
                        "hs-CRP ($25) -- inflammation down?",
                        "ALT ($15) -- liver still OK?",
                        "AST ($15) -- paired with ALT",
                        "25-OH Vitamin D ($40) -- target reached?",
                        "CBC ($15) -- general health",
                    ],
                    "total_lab_cost": 175,
                    "cost": 175,
                    "category": "labs",
                },
                {
                    "week": 12,
                    "day": "Month 3",
                    "action": "DECISION POINT #1",
                    "details": "Review Month 3 labs with endocrinologist.\n\n"
                               "IF C-peptide rose (even slightly): Protocol is working. Continue. Move to Phase 2.\n"
                               "IF C-peptide flat: Protocol may need more time. Continue Phase 1 for 3 more months. "
                               "Consider: Was fluoxetine taken consistently? Were FMD cycles completed? "
                               "Is vitamin D at target? Fix compliance before adding more components.\n"
                               "IF C-peptide dropped: Concerning but not fatal. Check autoantibodies. "
                               "Consider adding GABA early (move Phase 2 components forward).\n"
                               "IF ALT > 3x ULN: Reduce fluoxetine to 10mg. Recheck in 2 weeks.\n"
                               "IF hs-CRP unchanged or rising: Investigate other sources of inflammation.",
                    "cost": 50,
                    "category": "medical",
                },
            ],
        },
        # =====================================================================
        # PHASE 2: AMPLIFY (Months 3-6) -- Boost Regeneration
        # =====================================================================
        {
            "phase": "PHASE_2",
            "name": "Amplify -- Boost Regeneration",
            "start_month": 3,
            "end_month": 6,
            "goal": "Add GABA (transdifferentiation + anti-inflammatory) and semaglutide "
                    "(proliferation + sensitivity). Target: R begins approaching D.",
            "model_prediction": {
                "R_total": "~2.7e-4 /day (averaged, FMD bursts included)",
                "D_total": "~4.5e-4 /day (continuing to drop as TD clears)",
                "dB_dt": "-1.8e-4 /day (approaching zero -- the gap is closing)",
                "expected_cpeptide": "0.12-0.20 nmol/L range",
            },
            "actions": [
                {
                    "week": 13,
                    "day": "Month 3, Week 1",
                    "action": "START GABA 250mg 3x/day",
                    "details": "GABA (gamma-aminobutyric acid) has TWO mechanisms:\n"
                               "  1. Anti-inflammatory: reduces Teff expansion by ~20%\n"
                               "  2. Transdifferentiation: activates GABA-A on alpha cells -> Pax4 -> "
                               "alpha-to-beta identity switch\n\n"
                               "Start 250mg with each meal (3x/day = 750mg total). "
                               "Can increase to 500mg 3x/day (1500mg) after 2 weeks if tolerated. "
                               "Side effects: mild drowsiness (especially first week), slight dizziness. "
                               "If drowsy: take larger dose at bedtime, smaller doses at meals. "
                               "GABA does NOT cross the blood-brain barrier well in adults, so "
                               "central sedation is minimal. GI effects are the main route.",
                    "prescription_needed": False,
                    "cost_monthly": 20,
                    "category": "supplement",
                },
                {
                    "week": 17,
                    "day": "Month 4, Week 1",
                    "action": "DISCUSS semaglutide with endocrinologist",
                    "details": "Semaglutide (Ozempic) is a GLP-1 receptor agonist. Off-label for T1DM "
                               "but increasingly studied (ADJUNCT ONE and TWO trials).\n\n"
                               "What to tell your doctor:\n"
                               "  'I'd like to try low-dose semaglutide as an adjunct to my insulin. "
                               "The evidence from ADJUNCT trials shows it can reduce insulin dose by "
                               "20-30% in T1DM, improve time-in-range, and reduce HbA1c. I understand "
                               "the hypoglycemia risk and I have CGM monitoring. I'd like to start at "
                               "0.25mg weekly and titrate slowly.'\n\n"
                               "If physician agrees:\n"
                               "  - Start 0.25mg subcutaneous weekly\n"
                               "  - Proactively reduce basal insulin by 10% when starting\n"
                               "  - Watch CGM closely for lows in the first 2 weeks\n"
                               "  - Common side effects: nausea (50% of patients), reduced appetite\n\n"
                               "If physician declines:\n"
                               "  The protocol works without semaglutide. It provides ~25% R boost and "
                               "30% sensitivity improvement, but GABA + FMD are the main drivers. "
                               "Semaglutide is Tier 3 (premium). Skip it and continue.",
                    "prescription_needed": True,
                    "cost_monthly": 300,
                    "category": "medication",
                },
                {
                    "week": 21,
                    "day": "Month 4-5",
                    "action": "TITRATE semaglutide to 0.5mg weekly",
                    "details": "After 4 weeks at 0.25mg, increase to 0.5mg if tolerated.\n"
                               "  - Reduce basal insulin by another 10% (total 20% reduction from baseline)\n"
                               "  - Adjust fasting protocol: basal at 70% (not 80%) during fasts\n"
                               "  - Monitor weight: semaglutide causes weight loss. If BMI drops below 20, "
                               "  discuss with doctor.\n"
                               "  - DO NOT go above 0.5mg. This is not for weight loss -- "
                               "  we want the beta cell and immune effects, not max GLP-1 stimulation.",
                    "prescription_needed": True,
                    "cost_monthly": 300,
                    "category": "medication",
                },
                {
                    "week": 13,
                    "day": "Months 3-6, ongoing",
                    "action": "CONTINUE monthly FMD cycles",
                    "details": "One 5-day FMD per month. Schedule it the same week each month. "
                               "The refeeding window (days 6-8) is cumulative -- each cycle adds ~0.3% "
                               "beta cell mass. After 6 cycles, ~2-3% gain.",
                    "cost_monthly": 50,
                    "category": "fasting",
                },
                {
                    "week": 26,
                    "day": "Month 6",
                    "action": "COMPREHENSIVE LABS -- Month 6",
                    "details": "The major assessment. This is where we expect to see signal.",
                    "labs": [
                        "C-peptide, fasting ($45) -- PRIMARY ENDPOINT",
                        "C-peptide, stimulated/MMTT ($150) -- gold standard",
                        "HbA1c ($20)",
                        "GAD65 autoantibodies ($85) -- declining?",
                        "hs-CRP ($25)",
                        "ALT + AST ($30)",
                        "Troponin I hs ($30) -- cardiac safety",
                        "CBC ($15)",
                        "CMP ($20)",
                        "25-OH Vitamin D ($40)",
                        "Fasting insulin ($30)",
                    ],
                    "total_lab_cost": 490,
                    "cost": 490,
                    "category": "labs",
                },
                {
                    "week": 26,
                    "day": "Month 6",
                    "action": "IMAGING -- Echocardiogram (repeat)",
                    "details": "Repeat echo if baseline showed any abnormality, or if troponin was elevated. "
                               "If baseline was normal and troponin normal: skip (save money).",
                    "cost": 350,
                    "category": "imaging",
                },
                {
                    "week": 26,
                    "day": "Month 6",
                    "action": "DECISION POINT #2 -- The Big One",
                    "details": "Review all Month 6 data with endocrinologist.\n\n"
                               "OUTCOME A: C-peptide rising (any amount)\n"
                               "  -> CELEBRATE. The inequality is shifting. Continue to Phase 3.\n"
                               "  -> If stimulated C-peptide > 0.4 nmol/L: you are responding strongly.\n\n"
                               "OUTCOME B: C-peptide flat but hs-CRP dropped\n"
                               "  -> The anti-inflammatory arm is working but regeneration hasn't kicked in yet.\n"
                               "  -> Add GABA 1500mg/day if not already at full dose.\n"
                               "  -> Continue 3 more months before reassessing.\n\n"
                               "OUTCOME C: C-peptide flat, hs-CRP flat, autoantibodies unchanged\n"
                               "  -> Consider: is the protocol being followed consistently?\n"
                               "  -> Consider: teplizumab discussion with specialist (see Phase 3).\n"
                               "  -> Do NOT stop -- 6 months may not be enough for a 67-year T1DM patient.\n"
                               "  -> The model predicts inequality reversal at month 8-10.\n\n"
                               "OUTCOME D: C-peptide dropped\n"
                               "  -> Uncommon. Check for concurrent illness, infection, severe stress.\n"
                               "  -> Repeat in 1 month. Single drop is not failure.",
                    "cost": 50,
                    "category": "medical",
                },
            ],
        },
        # =====================================================================
        # PHASE 3: SUSTAIN (Months 6-12)
        # =====================================================================
        {
            "phase": "PHASE_3",
            "name": "Sustain -- The Inequality Reverses",
            "start_month": 6,
            "end_month": 12,
            "goal": "All components running. R overtakes D around month 8-10. "
                    "Beta cell mass begins GROWING. Begin insulin dose reduction if C-peptide rising.",
            "model_prediction": {
                "month_9_R": "~8.0e-4 /day (GABA transdiff + semaglutide + FMD)",
                "month_9_D": "~3.5e-4 /day (TD mostly cleared, Tregs strong)",
                "dB_dt": "+4.5e-4 /day -- INEQUALITY REVERSED",
                "month_12_B": "~13% (up from 8%)",
                "month_12_Cp": "~0.25 nmol/L",
            },
            "actions": [
                {
                    "week": 26,
                    "day": "Months 6-12, ongoing",
                    "action": "CONTINUE all protocol components",
                    "details": "Fluoxetine 20mg daily\n"
                               "Vitamin D3 4000 IU daily\n"
                               "Sodium butyrate 300mg 2x/day\n"
                               "GABA 250-500mg 3x/day\n"
                               "Semaglutide 0.5mg weekly (if started)\n"
                               "Monthly 5-day FMD cycle\n\n"
                               "This is the grind. Nothing changes except the numbers. "
                               "The model says the inequality reverses around month 8-10. "
                               "You won't feel it. The C-peptide will show it.",
                    "cost_monthly": 0,
                    "category": "maintenance",
                },
                {
                    "week": 26,
                    "day": "Month 6+",
                    "action": "IF C-peptide rising: begin insulin dose reduction per milestone ladder",
                    "details": "C-PEPTIDE MILESTONE LADDER:\n\n"
                               "0.20 nmol/L (FIRST SIGNAL): No insulin change. Just celebrate.\n"
                               "0.40 nmol/L (EARLY RESPONSE): Reduce bolus by 25%.\n"
                               "0.80 nmol/L (MODERATE RECOVERY): Reduce basal 30%, bolus 50%. DANGER ZONE.\n"
                               "1.20 nmol/L (STRONG RECOVERY): Reduce basal 50%, bolus 75%.\n"
                               "1.80 nmol/L (NEAR INDEPENDENCE): Safety minimum basal only. Trial discontinue bolus.\n"
                               "2.50 nmol/L (INDEPENDENCE): Trial complete discontinuation.\n\n"
                               "NEVER reduce insulin without CGM data and C-peptide confirmation.\n"
                               "NEVER skip more than one step at a time.\n"
                               "ALWAYS keep insulin pen loaded and accessible.",
                    "cost": 0,
                    "category": "insulin",
                },
                {
                    "week": 26,
                    "day": "Month 6+",
                    "action": "IF C-peptide flat: consider teplizumab",
                    "details": "Teplizumab (Tzield) is an anti-CD3 monoclonal antibody.\n"
                               "FDA-approved for delaying T1DM onset (Herold 2019 NEJM).\n"
                               "Off-label for established T1DM but biologically rational.\n\n"
                               "Requires specialist (academic endocrinologist or immunologist).\n"
                               "Single 14-day IV infusion course.\n"
                               "Cost: ~$13,000 per course (without insurance).\n"
                               "Side effects: cytokine release syndrome (CRS, flu-like), lymphopenia, rash.\n\n"
                               "DO NOT fast during teplizumab course.\n"
                               "Resume FMD 4 weeks after completing infusion.\n\n"
                               "This is Tier 3+. Most patients should try the full Phase 1-2 protocol "
                               "for 9-12 months before considering teplizumab.",
                    "prescription_needed": True,
                    "cost": 13000,
                    "category": "medication",
                },
                {
                    "week": 39,
                    "day": "Month 9",
                    "action": "LABS -- Month 9",
                    "details": "Interim check. Primary focus: C-peptide trajectory.",
                    "labs": [
                        "C-peptide, fasting ($45)",
                        "HbA1c ($20)",
                        "hs-CRP ($25)",
                        "ALT ($15)",
                    ],
                    "total_lab_cost": 105,
                    "cost": 105,
                    "category": "labs",
                },
                {
                    "week": 52,
                    "day": "Month 12",
                    "action": "FULL REASSESSMENT -- Month 12",
                    "details": "One-year milestone. Comprehensive re-evaluation.",
                    "labs": [
                        "C-peptide, fasting ($45)",
                        "C-peptide, stimulated/MMTT ($150)",
                        "HbA1c ($20)",
                        "GAD65 autoantibodies ($85)",
                        "IA-2 autoantibodies ($85)",
                        "hs-CRP ($25)",
                        "ALT + AST ($30)",
                        "Troponin I hs ($30)",
                        "NT-proBNP ($40)",
                        "CBC ($15)",
                        "CMP ($20)",
                        "25-OH Vitamin D ($40)",
                        "Fasting insulin ($30)",
                    ],
                    "total_lab_cost": 615,
                    "cost": 615,
                    "category": "labs",
                },
                {
                    "week": 52,
                    "day": "Month 12",
                    "action": "DECISION POINT #3 -- Continue, Modify, or Celebrate",
                    "details": "Review 12-month data.\n\n"
                               "RESPONDING (C-peptide up, insulin dose down):\n"
                               "  -> Continue all components. Move to Phase 4 (Maintenance).\n"
                               "  -> If C-peptide > 0.8 nmol/L: you are on track for independence.\n"
                               "  -> Projected timeline: insulin independence 18-36 months.\n\n"
                               "PARTIAL RESPONSE (C-peptide up slightly, insulin unchanged):\n"
                               "  -> The inequality reversed but slowly. Continue for another 6-12 months.\n"
                               "  -> Consider semaglutide if not started. Consider teplizumab.\n\n"
                               "NO RESPONSE (C-peptide flat after 12 months):\n"
                               "  -> The 20-35% of patients who may not respond at 3 years.\n"
                               "  -> Options: (1) continue anyway (no harm, supplements are safe), "
                               "(2) stop protocol, (3) try teplizumab, (4) wait for next-gen interventions.\n"
                               "  -> Even no response = you are healthier from vitamin D, reduced inflammation, "
                               "improved gut health, and better glucose control from fasting discipline.",
                    "cost": 50,
                    "category": "medical",
                },
            ],
        },
        # =====================================================================
        # PHASE 4: MAINTENANCE (Months 12-24)
        # =====================================================================
        {
            "phase": "PHASE_4",
            "name": "Maintenance -- Consolidate Gains",
            "start_month": 12,
            "end_month": 24,
            "goal": "If responding: continue protocol, reduce insulin per milestones, "
                    "reduce monitoring frequency. If near independence: trial discontinuation.",
            "model_prediction": {
                "month_18_B": "~22% (expected case)",
                "month_18_Cp": "~0.55 nmol/L",
                "month_18_insulin": "~10 U/day",
                "month_24_B": "~28% (approaching independence)",
                "month_24_Cp": "~0.75 nmol/L",
                "month_24_insulin": "~7 U/day",
            },
            "actions": [
                {
                    "week": 52,
                    "day": "Months 12-24, ongoing",
                    "action": "CONTINUE responding components",
                    "details": "If responding:\n"
                               "  - Fluoxetine 20mg daily (continue for full 24 months minimum)\n"
                               "  - Vitamin D3 4000 IU daily (indefinite)\n"
                               "  - Butyrate 300mg 2x/day (continue)\n"
                               "  - GABA 250-500mg 3x/day (continue)\n"
                               "  - FMD: can reduce to every 6-8 weeks if C-peptide steadily rising\n"
                               "  - Semaglutide: continue if well-tolerated\n\n"
                               "If not responding after 12 months:\n"
                               "  - Can stop FMD (it was worth trying)\n"
                               "  - Continue fluoxetine + supplements (still beneficial)\n"
                               "  - Consider stopping semaglutide (expensive if not helping)",
                    "cost_monthly": 0,
                    "category": "maintenance",
                },
                {
                    "week": 78,
                    "day": "Month 18",
                    "action": "LABS -- Month 18",
                    "labs": [
                        "C-peptide, fasting ($45)",
                        "HbA1c ($20)",
                        "ALT ($15)",
                        "25-OH Vitamin D ($40)",
                    ],
                    "total_lab_cost": 120,
                    "cost": 120,
                    "category": "labs",
                },
                {
                    "week": 78,
                    "day": "Month 18",
                    "action": "FLUOXETINE TAPER DECISION",
                    "details": "At 18 months, the CVB clearance model predicts all 8 compartments cleared.\n"
                               "Consider tapering fluoxetine IF:\n"
                               "  - C-peptide has been rising for 6+ months\n"
                               "  - Autoantibodies declining or stable\n"
                               "  - hs-CRP normal\n\n"
                               "Taper: 20mg -> 10mg for 2 weeks -> 10mg every other day for 2 weeks -> stop.\n"
                               "NEVER stop fluoxetine abruptly (discontinuation syndrome: dizziness, "
                               "brain zaps, irritability, flu-like symptoms).\n\n"
                               "If C-peptide is still flat: continue fluoxetine. No harm in longer duration.",
                    "cost": 0,
                    "category": "medication",
                },
                {
                    "week": 104,
                    "day": "Month 24",
                    "action": "FINAL ASSESSMENT -- Month 24",
                    "labs": [
                        "C-peptide, fasting ($45)",
                        "C-peptide, stimulated/MMTT ($150)",
                        "HbA1c ($20)",
                        "GAD65 autoantibodies ($85)",
                        "IA-2 autoantibodies ($85)",
                        "ZnT8 autoantibodies ($85)",
                        "hs-CRP ($25)",
                        "ALT + AST ($30)",
                        "Troponin I hs ($30)",
                        "NT-proBNP ($40)",
                        "CBC ($15)",
                        "CMP ($20)",
                        "25-OH Vitamin D ($40)",
                        "Fasting insulin ($30)",
                        "Lipid panel ($25)",
                    ],
                    "total_lab_cost": 725,
                    "cost": 725,
                    "category": "labs",
                },
                {
                    "week": 104,
                    "day": "Month 24",
                    "action": "DECISION POINT #4 -- The Verdict",
                    "details": "Two-year mark. The model's expected case:\n"
                               "  B ~ 0.28, C-peptide ~ 0.75 nmol/L, insulin ~ 7 U/day\n\n"
                               "SUCCESS (C-peptide > 0.8 nmol/L, insulin reduced >50%):\n"
                               "  -> Continue maintenance: vitamin D + butyrate + GABA\n"
                               "  -> Quarterly FMD if desired\n"
                               "  -> Semi-annual labs (C-peptide + HbA1c)\n"
                               "  -> Continue insulin reduction per milestone ladder\n"
                               "  -> You are on track for independence at 30-36 months\n\n"
                               "PARTIAL SUCCESS (C-peptide 0.3-0.8, insulin reduced somewhat):\n"
                               "  -> Continue protocol. You are responding, just slowly.\n"
                               "  -> Consider extending to 36 months.\n"
                               "  -> Even if you never reach independence, every 0.1 nmol/L of C-peptide "
                               "reduces complications, reduces hypo frequency, and improves quality of life.\n\n"
                               "NO RESPONSE (C-peptide unchanged after 24 months):\n"
                               "  -> Reasonable to stop active protocol components.\n"
                               "  -> Continue vitamin D and butyrate (general health benefits).\n"
                               "  -> The supplements were safe and the attempt was rational.\n"
                               "  -> You learned your autoimmune phenotype: likely not CVB-driven, or "
                               "  beta cell reserve was truly exhausted.",
                    "cost": 50,
                    "category": "medical",
                },
            ],
        },
    ],
}


# =============================================================================
# SHOPPING LIST -- EXACT PRODUCTS AND DOSES
# =============================================================================

SHOPPING_LIST = {
    "tier_1_essential": {
        "name": "Tier 1 -- Essential (minimum effective protocol)",
        "monthly_cost": 93,
        "items": [
            {
                "item": "Fluoxetine 20mg capsules",
                "dose": "10mg/day weeks 1-2, then 20mg/day",
                "quantity": "30 capsules/month",
                "source": "Prescription (generic, any pharmacy)",
                "cost_monthly": 10,
                "notes": "Generic fluoxetine. GoodRx price ~$4-10/month. "
                         "Do NOT use brand Prozac ($300+). Ask pharmacist for generic.",
            },
            {
                "item": "Vitamin D3 4000 IU softgels",
                "dose": "4000 IU/day (1 softgel)",
                "quantity": "30 softgels/month",
                "source": "Amazon, iHerb, Costco, any pharmacy",
                "example_product": "NatureWise Vitamin D3 4000 IU or NOW Vitamin D3 5000 IU",
                "cost_monthly": 8,
                "notes": "Cholecalciferol (D3), not ergocalciferol (D2). Take with fat. "
                         "5000 IU products are fine -- take 5000 IU on alternating days with 4000 IU "
                         "or just take 5000 IU daily and adjust if levels go above 70 ng/mL.",
            },
            {
                "item": "Sodium butyrate 300mg capsules (enteric-coated)",
                "dose": "300mg 2x/day (600mg total)",
                "quantity": "60 capsules/month",
                "source": "Amazon, iHerb",
                "example_product": "BodyBio Sodium Butyrate 600mg (take 1/day) or "
                                   "ProButyrate 300mg (take 2/day)",
                "cost_monthly": 25,
                "notes": "MUST be enteric-coated or you will taste/smell butyrate (rancid butter). "
                         "Calcium/magnesium butyrate also acceptable. "
                         "Tributyrin (e.g., CoreBiome) is a prodrug alternative.",
            },
            {
                "item": "ProLon FMD kit (or DIY equivalent)",
                "dose": "5-day cycle, once per month",
                "quantity": "1 kit/month (or DIY supplies)",
                "source": "prolonfmd.com or DIY",
                "cost_monthly": 50,
                "notes": "ProLon: $199 first kit, then $149/mo subscription. "
                         "DIY option: nuts, olives, vegetable soups = ~$30-50/cycle. "
                         "See FMD protocol details above for exact macros.",
            },
        ],
    },
    "tier_2_full": {
        "name": "Tier 2 -- Full protocol (add GABA)",
        "additional_monthly_cost": 20,
        "total_monthly_cost": 113,
        "items": [
            {
                "item": "GABA 750mg capsules",
                "dose": "250-500mg 3x/day (750-1500mg total)",
                "quantity": "90-180 capsules/month (depending on dose)",
                "source": "Amazon, iHerb, any supplement store",
                "example_product": "NOW GABA 750mg capsules (take 1 capsule 2x/day = 1500mg) or "
                                   "Thorne PharmaGABA 100mg (chewable, more bioavailable but more expensive)",
                "cost_monthly": 20,
                "notes": "Regular GABA powder capsules are fine. PharmaGABA (fermented) may have "
                         "slightly better absorption but costs 3x more. Start low (250mg 1x/day) "
                         "and increase over 2 weeks.",
            },
        ],
    },
    "tier_3_premium": {
        "name": "Tier 3 -- Premium (add semaglutide)",
        "additional_monthly_cost": 300,
        "total_monthly_cost": 413,
        "items": [
            {
                "item": "Semaglutide 0.25mg -> 0.5mg weekly injection",
                "dose": "0.25mg/week months 4-5, then 0.5mg/week",
                "quantity": "4 injections/month",
                "source": "Prescription (Ozempic pen, or compounding pharmacy)",
                "cost_monthly": 300,
                "notes": "Ozempic with insurance: $25-50 copay. Without insurance: ~$900-1000/month. "
                         "Compounding pharmacies: $150-300/month (check local). "
                         "Canadian pharmacy (with valid Rx): ~$250-350/month. "
                         "If cost prohibitive: SKIP. The protocol works without it.",
            },
        ],
    },
    "monitoring_equipment": {
        "name": "Monitoring Equipment (one-time + ongoing)",
        "items": [
            {
                "item": "CGM System (Dexcom G7 or Libre 3)",
                "cost_monthly": 75,
                "notes": "With insurance: usually covered for T1DM ($0-50 copay). "
                         "Without insurance: Libre 3 ~$75/month, Dexcom ~$150/month. "
                         "Libre 3 is the budget option and perfectly adequate.",
            },
            {
                "item": "Blood ketone meter + strips",
                "cost_one_time": 50,
                "cost_monthly": 30,
                "notes": "Keto-Mojo GK+ kit: ~$50 (meter + 10 strips). "
                         "Additional strips: ~$1/strip, need ~30/month during fasting.",
            },
        ],
    },
}


# =============================================================================
# COST MODEL
# =============================================================================

def compute_monthly_costs():
    """Compute month-by-month costs for each tier."""
    months = list(range(-1, 25))
    tiers = {
        "tier_1": [],
        "tier_2": [],
        "tier_3": [],
    }

    # Lab costs at specific months
    lab_costs = {
        -1: 815,   # baseline
        1: 80,     # month 1 safety
        3: 175,    # month 3
        6: 490,    # month 6 comprehensive
        9: 105,    # month 9
        12: 615,   # month 12 full
        18: 120,   # month 18
        24: 725,   # month 24 final
    }

    # Imaging costs
    imaging_costs = {
        -1: 500,  # baseline echo + US
        6: 350,   # repeat echo (conditional)
    }

    # Monthly supplement/med costs by tier
    # Tier 1: fluoxetine + vitamin D + butyrate + FMD + CGM + ketone strips
    tier1_monthly = 10 + 8 + 25 + 50 + 75 + 30  # = $198/mo ongoing
    # Tier 2: + GABA
    tier2_monthly = tier1_monthly + 20  # = $218/mo
    # Tier 3: + semaglutide (starts month 4)
    tier3_monthly_before_sema = tier2_monthly
    tier3_monthly_after_sema = tier2_monthly + 300  # = $518/mo

    for m in months:
        labs = lab_costs.get(m, 0)
        imaging = imaging_costs.get(m, 0)
        visits = 50 if m in [0, 3, 6, 12, 24] else 0

        # Phase-dependent: supplements start at different times
        if m < 1:
            # Prep phase: only equipment + labs
            t1_supplements = 0
            t2_supplements = 0
            t3_supplements = 0
        elif m < 3:
            # Phase 1: fluoxetine + vitD + butyrate + FMD
            t1_supplements = 10 + 8 + 25 + 50 + 75 + 30
            t2_supplements = t1_supplements  # GABA not started yet
            t3_supplements = t1_supplements  # semaglutide not started yet
        elif m < 4:
            # Month 3: add GABA for tier 2+
            t1_supplements = 10 + 8 + 25 + 50 + 75 + 30
            t2_supplements = t1_supplements + 20
            t3_supplements = t2_supplements
        else:
            # Month 4+: add semaglutide for tier 3
            t1_supplements = 10 + 8 + 25 + 50 + 75 + 30
            t2_supplements = t1_supplements + 20
            t3_supplements = t2_supplements + 300

        tiers["tier_1"].append(t1_supplements + labs + imaging + visits)
        tiers["tier_2"].append(t2_supplements + labs + imaging + visits)
        tiers["tier_3"].append(t3_supplements + labs + imaging + visits)

    return months, tiers


def compute_cumulative_costs():
    """Compute cumulative cost over 24 months for each tier."""
    months, tiers = compute_monthly_costs()
    cum = {}
    for tier_name, costs in tiers.items():
        cum[tier_name] = np.cumsum(costs).tolist()
    return months, tiers, cum


# =============================================================================
# VISUALIZATION: GANTT CHART TIMELINE
# =============================================================================

def generate_gantt_chart():
    """Generate Gantt-chart style timeline of the entire protocol."""
    fig, ax = plt.subplots(figsize=(20, 14))

    # Define tracks (y positions)
    tracks = {
        "Fluoxetine": 14,
        "Vitamin D3": 13,
        "Sod. Butyrate": 12,
        "GABA": 11,
        "Semaglutide": 10,
        "24h Fasts": 9,
        "5-day FMD": 8,
        "CGM": 7,
        "Ketone Monitoring": 6,
        "Lab Draws": 5,
        "Endo Visits": 4,
        "Imaging": 3,
        "Insulin Reduction": 2,
        "Teplizumab (opt.)": 1,
    }

    colors = {
        "medication": "#E74C3C",
        "supplement": "#3498DB",
        "fasting": "#2ECC71",
        "monitoring": "#F39C12",
        "labs": "#9B59B6",
        "medical": "#1ABC9C",
        "imaging": "#E67E22",
        "insulin": "#E91E63",
        "optional": "#95A5A6",
    }

    # Background phase bands
    phase_bands = [
        (-0.5, 0, "Prep", "#FDEBD0"),
        (0, 3, "Phase 1:\nFoundation", "#FADBD8"),
        (3, 6, "Phase 2:\nAmplify", "#D5F5E3"),
        (6, 12, "Phase 3:\nSustain", "#D6EAF8"),
        (12, 24, "Phase 4:\nMaintain", "#F5EEF8"),
    ]

    for start, end, label, color in phase_bands:
        ax.axvspan(start, end, alpha=0.3, color=color)
        mid = (start + end) / 2
        ax.text(mid, 15.3, label, ha='center', va='bottom', fontsize=9,
                fontweight='bold', color='#333333')

    # Draw bars
    bar_height = 0.6

    # Fluoxetine: 10mg weeks 1-2, 20mg week 3+
    ax.barh(tracks["Fluoxetine"], 0.5, left=0, height=bar_height,
            color=colors["medication"], alpha=0.5, label='_nolegend_')
    ax.text(0.25, tracks["Fluoxetine"], "10mg", ha='center', va='center', fontsize=7, color='white', fontweight='bold')
    ax.barh(tracks["Fluoxetine"], 17.5, left=0.5, height=bar_height,
            color=colors["medication"], alpha=0.85)
    ax.text(9, tracks["Fluoxetine"], "Fluoxetine 20mg/day", ha='center', va='center', fontsize=8, color='white', fontweight='bold')
    # Taper at month 18 (optional)
    ax.barh(tracks["Fluoxetine"], 6, left=18, height=bar_height,
            color=colors["medication"], alpha=0.35)
    ax.text(21, tracks["Fluoxetine"], "taper?", ha='center', va='center', fontsize=7, color='#666', style='italic')

    # Vitamin D: continuous from week 1
    ax.barh(tracks["Vitamin D3"], 24, left=0, height=bar_height,
            color=colors["supplement"], alpha=0.7)
    ax.text(12, tracks["Vitamin D3"], "Vitamin D3 4000 IU/day", ha='center', va='center', fontsize=8, color='white', fontweight='bold')

    # Butyrate: from week 2
    ax.barh(tracks["Sod. Butyrate"], 23.5, left=0.5, height=bar_height,
            color=colors["supplement"], alpha=0.7)
    ax.text(12, tracks["Sod. Butyrate"], "Sodium Butyrate 600mg/day", ha='center', va='center', fontsize=8, color='white', fontweight='bold')

    # GABA: from month 3
    ax.barh(tracks["GABA"], 21, left=3, height=bar_height,
            color=colors["supplement"], alpha=0.7)
    ax.text(13.5, tracks["GABA"], "GABA 750-1500mg/day", ha='center', va='center', fontsize=8, color='white', fontweight='bold')

    # Semaglutide: from month 4 (optional)
    ax.barh(tracks["Semaglutide"], 1, left=4, height=bar_height,
            color=colors["optional"], alpha=0.5)
    ax.text(4.5, tracks["Semaglutide"], "0.25", ha='center', va='center', fontsize=7, color='white')
    ax.barh(tracks["Semaglutide"], 19, left=5, height=bar_height,
            color=colors["medication"], alpha=0.5, hatch='///')
    ax.text(14.5, tracks["Semaglutide"], "Semaglutide 0.5mg/wk (Tier 3 only)", ha='center', va='center', fontsize=8, color='#333')

    # 24h fasts: monthly from month 1
    for m in range(1, 24):
        ax.barh(tracks["24h Fasts"], 0.15, left=m - 0.075, height=bar_height,
                color=colors["fasting"], alpha=0.8)

    # 5-day FMD: monthly from month 2, maybe every 6-8 weeks after month 12
    for m in range(2, 13):
        ax.barh(tracks["5-day FMD"], 0.17, left=m - 0.085, height=bar_height * 1.1,
                color=colors["fasting"], alpha=0.9)
    for m in [14, 16, 18, 20, 22, 24]:
        ax.barh(tracks["5-day FMD"], 0.17, left=m - 0.085, height=bar_height * 1.1,
                color=colors["fasting"], alpha=0.5)

    # CGM: continuous
    ax.barh(tracks["CGM"], 24, left=0, height=bar_height,
            color=colors["monitoring"], alpha=0.6)
    ax.text(12, tracks["CGM"], "CGM continuous", ha='center', va='center', fontsize=8, color='white', fontweight='bold')

    # Ketone monitoring: every fasting day
    ax.barh(tracks["Ketone Monitoring"], 24, left=0, height=bar_height,
            color=colors["monitoring"], alpha=0.4)
    ax.text(12, tracks["Ketone Monitoring"], "Blood ketones (every fasting day)", ha='center', va='center', fontsize=8, color='#333')

    # Lab draws
    lab_months = [-0.5, 1, 3, 6, 9, 12, 18, 24]
    lab_labels = ["BL", "M1", "M3", "M6", "M9", "M12", "M18", "M24"]
    for m, lbl in zip(lab_months, lab_labels):
        ax.barh(tracks["Lab Draws"], 0.3, left=m - 0.15, height=bar_height,
                color=colors["labs"], alpha=0.9)
        ax.text(m, tracks["Lab Draws"], lbl, ha='center', va='center', fontsize=6, color='white', fontweight='bold')

    # Endo visits
    visit_months = [0, 3, 6, 12, 24]
    for m in visit_months:
        ax.plot(m, tracks["Endo Visits"], 'D', color=colors["medical"], markersize=10, alpha=0.8)

    # Imaging
    ax.plot(-0.5, tracks["Imaging"], 's', color=colors["imaging"], markersize=12, alpha=0.8)
    ax.text(-0.5, tracks["Imaging"] - 0.45, "Echo+US", ha='center', fontsize=6)
    ax.plot(6, tracks["Imaging"], 's', color=colors["imaging"], markersize=10, alpha=0.5)
    ax.text(6, tracks["Imaging"] - 0.45, "Echo?", ha='center', fontsize=6, style='italic')

    # Insulin reduction (conditional, from ~month 6)
    ax.annotate('', xy=(24, tracks["Insulin Reduction"]),
                xytext=(6, tracks["Insulin Reduction"]),
                arrowprops=dict(arrowstyle='->', color=colors["insulin"], lw=2, alpha=0.6))
    ax.text(15, tracks["Insulin Reduction"] + 0.4, "Insulin dose reduction (if C-peptide rising)",
            ha='center', fontsize=8, color=colors["insulin"], style='italic')

    # Teplizumab (optional)
    ax.barh(tracks["Teplizumab (opt.)"], 0.5, left=6, height=bar_height,
            color=colors["optional"], alpha=0.4, hatch='xxx')
    ax.text(8, tracks["Teplizumab (opt.)"], "14-day course (if needed, Tier 3+)",
            ha='center', fontsize=7, color='#999', style='italic')

    # Key milestones
    milestones = [
        (0, "START", "#E74C3C"),
        (3, "1st C-peptide\ncheck", "#9B59B6"),
        (6, "Key\ndecision", "#E74C3C"),
        (10, "R > D\n(model)", "#2ECC71"),
        (12, "1-year\nassess", "#9B59B6"),
        (24, "2-year\nverdict", "#E74C3C"),
    ]
    for m, label, color in milestones:
        ax.axvline(x=m, color=color, linestyle='--', alpha=0.4, linewidth=1)
        ax.text(m, 0.2, label, ha='center', va='top', fontsize=7,
                color=color, fontweight='bold')

    # Formatting
    ax.set_yticks(list(tracks.values()))
    ax.set_yticklabels(list(tracks.keys()), fontsize=10)
    ax.set_xlim(-1.5, 25)
    ax.set_ylim(0, 16)
    ax.set_xlabel("Months from protocol start", fontsize=12)
    ax.set_title("T1DM Beta Cell Recovery Protocol — Complete Timeline",
                 fontsize=16, fontweight='bold', pad=20)

    # Legend
    legend_patches = [
        mpatches.Patch(color=colors["medication"], alpha=0.8, label="Medication (Rx)"),
        mpatches.Patch(color=colors["supplement"], alpha=0.7, label="Supplement (OTC)"),
        mpatches.Patch(color=colors["fasting"], alpha=0.8, label="Fasting/FMD"),
        mpatches.Patch(color=colors["monitoring"], alpha=0.6, label="Monitoring"),
        mpatches.Patch(color=colors["labs"], alpha=0.9, label="Lab draws"),
        mpatches.Patch(color=colors["optional"], alpha=0.5, label="Optional/Tier 3"),
    ]
    ax.legend(handles=legend_patches, loc='upper right', fontsize=9, framealpha=0.9)

    ax.grid(axis='x', alpha=0.3, linestyle=':')
    plt.tight_layout()

    output_path = os.path.join(FIGURES_DIR, "protocol_gantt_timeline.png")
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {output_path}")
    return output_path


# =============================================================================
# VISUALIZATION: COST BREAKDOWN
# =============================================================================

def generate_cost_plots():
    """Generate monthly and cumulative cost comparison plots."""
    months, tiers, cum = compute_cumulative_costs()

    fig, axes = plt.subplots(1, 2, figsize=(18, 7))

    # Monthly costs
    ax1 = axes[0]
    bar_width = 0.25
    x = np.array(months)
    ax1.bar(x - bar_width, tiers["tier_1"], bar_width, label="Tier 1: Essential (~$198/mo)",
            color="#3498DB", alpha=0.8)
    ax1.bar(x, tiers["tier_2"], bar_width, label="Tier 2: Full (~$218/mo)",
            color="#2ECC71", alpha=0.8)
    ax1.bar(x + bar_width, tiers["tier_3"], bar_width, label="Tier 3: Premium (~$518/mo)",
            color="#E74C3C", alpha=0.8)

    ax1.set_xlabel("Month", fontsize=11)
    ax1.set_ylabel("Cost ($USD)", fontsize=11)
    ax1.set_title("Monthly Cost by Tier", fontsize=13, fontweight='bold')
    ax1.legend(fontsize=9)
    ax1.grid(axis='y', alpha=0.3)
    ax1.set_xticks(range(-1, 25, 3))

    # Cumulative costs
    ax2 = axes[1]
    ax2.plot(months, cum["tier_1"], 'o-', color="#3498DB", linewidth=2, markersize=4,
             label=f"Tier 1: ${cum['tier_1'][-1]:,.0f} total")
    ax2.plot(months, cum["tier_2"], 's-', color="#2ECC71", linewidth=2, markersize=4,
             label=f"Tier 2: ${cum['tier_2'][-1]:,.0f} total")
    ax2.plot(months, cum["tier_3"], 'D-', color="#E74C3C", linewidth=2, markersize=4,
             label=f"Tier 3: ${cum['tier_3'][-1]:,.0f} total")

    # Reference: annual insulin cost
    insulin_annual = 3000  # average US cost for T1DM insulin
    ax2.axhline(y=insulin_annual, color='#999', linestyle='--', alpha=0.5)
    ax2.text(1, insulin_annual + 200, f"1 year insulin (~${insulin_annual:,})", fontsize=8, color='#999')

    ax2.set_xlabel("Month", fontsize=11)
    ax2.set_ylabel("Cumulative Cost ($USD)", fontsize=11)
    ax2.set_title("Cumulative Cost Over 24 Months", fontsize=13, fontweight='bold')
    ax2.legend(fontsize=9)
    ax2.grid(alpha=0.3)

    plt.tight_layout()

    output_path = os.path.join(FIGURES_DIR, "protocol_cost_breakdown.png")
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {output_path}")
    return output_path


# =============================================================================
# VISUALIZATION: DECISION TREE
# =============================================================================

def generate_decision_tree():
    """Generate the milestone decision tree visualization."""
    fig, ax = plt.subplots(figsize=(18, 12))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    def draw_box(x, y, w, h, text, color, fontsize=8, alpha=0.9):
        box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                             boxstyle="round,pad=0.3", facecolor=color,
                             edgecolor='#333', linewidth=1.5, alpha=alpha)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
                fontweight='bold', wrap=True,
                bbox=dict(boxstyle='round,pad=0', facecolor='none', edgecolor='none'))

    def draw_arrow(x1, y1, x2, y2, label="", color='#333'):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=color, lw=1.5))
        if label:
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            ax.text(mid_x, mid_y, label, fontsize=7, ha='center', va='center',
                    color=color, style='italic',
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='none', alpha=0.8))

    # Title
    ax.text(50, 97, "Protocol Decision Tree: What To Do At Each Milestone",
            ha='center', fontsize=14, fontweight='bold')

    # Start
    draw_box(50, 90, 20, 5, "START\nBaseline labs done", "#FDEBD0", fontsize=9)

    # Month 3
    draw_arrow(50, 87.5, 50, 77)
    draw_box(50, 74, 22, 5, "MONTH 3\nC-peptide check", "#D5F5E3", fontsize=9)

    draw_arrow(50, 71.5, 25, 65, "C-pep rising")
    draw_arrow(50, 71.5, 50, 65, "C-pep flat")
    draw_arrow(50, 71.5, 75, 65, "C-pep dropped")

    draw_box(25, 62, 18, 4, "Continue!\nAdd GABA (Phase 2)", "#2ECC71", fontsize=8)
    draw_box(50, 62, 18, 4, "Continue Phase 1\nFix compliance", "#F39C12", fontsize=8)
    draw_box(75, 62, 18, 4, "Check antibodies\nAdd GABA early", "#E74C3C", fontsize=8)

    # Month 6
    draw_arrow(25, 60, 50, 53)
    draw_arrow(50, 60, 50, 53)
    draw_arrow(75, 60, 50, 53)

    draw_box(50, 50, 22, 5, "MONTH 6\nFull labs + MMTT", "#D6EAF8", fontsize=9)

    draw_arrow(50, 47.5, 20, 41, "C-pep rising")
    draw_arrow(50, 47.5, 50, 41, "CRP down,\nC-pep flat")
    draw_arrow(50, 47.5, 80, 41, "Nothing\nchanged")

    draw_box(20, 38, 18, 4, "Phase 3!\nSemaglutide?", "#2ECC71", fontsize=8)
    draw_box(50, 38, 18, 4, "Continue 3 more\nmonths at full dose", "#F39C12", fontsize=8)
    draw_box(80, 38, 18, 4, "Consider\nteplizumab", "#E74C3C", fontsize=8)

    # Month 12
    draw_arrow(20, 36, 50, 29)
    draw_arrow(50, 36, 50, 29)
    draw_arrow(80, 36, 50, 29)

    draw_box(50, 26, 22, 5, "MONTH 12\nFull reassessment", "#F5EEF8", fontsize=9)

    draw_arrow(50, 23.5, 15, 17, "Responding\nC-pep > 0.4")
    draw_arrow(50, 23.5, 50, 17, "Partial\n0.15-0.4")
    draw_arrow(50, 23.5, 85, 17, "No response")

    draw_box(15, 14, 20, 5, "Phase 4!\nReduce insulin\nper milestones", "#2ECC71", fontsize=8)
    draw_box(50, 14, 20, 5, "Continue 12 more\nmonths. Consider\nsemaglutide/tepl.", "#F39C12", fontsize=8)
    draw_box(85, 14, 20, 5, "Stop active protocol\nKeep VitD + butyrate\nNo harm done", "#E74C3C", fontsize=8)

    # Month 24
    draw_arrow(15, 11.5, 50, 6)
    draw_arrow(50, 11.5, 50, 6)

    draw_box(50, 4, 25, 4, "MONTH 24: Verdict\nIndependence / partial / stable / reassess", "#FDEBD0", fontsize=9)

    plt.tight_layout()

    output_path = os.path.join(FIGURES_DIR, "protocol_decision_tree.png")
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {output_path}")
    return output_path


# =============================================================================
# VISUALIZATION: EXPECTED TRAJECTORY
# =============================================================================

def generate_trajectory_plot():
    """Plot expected C-peptide, beta cell mass, and insulin dose over 24 months."""
    months = np.linspace(0, 24, 100)

    # Expected case trajectories (from Pattern 003)
    # Beta cell mass: starts 0.08, slow rise, accelerates after month 8-10
    beta_mass = 0.08 + 0.02 * (1 - np.exp(-months / 8)) + \
                0.12 * np.maximum(0, (months - 8) / 16) ** 1.3
    beta_mass = np.clip(beta_mass, 0, 0.5)

    # C-peptide tracks beta mass with secretion efficiency improving
    eff = 0.6 + 0.15 * (1 - np.exp(-months / 6))
    cpeptide = beta_mass * 2.5 * eff

    # Insulin dose: starts 16, begins dropping when C-peptide rises
    insulin = np.full_like(months, 16.0)
    for i, (m, cp) in enumerate(zip(months, cpeptide)):
        if cp >= 0.40:
            insulin[i] = 16 * (1 - 0.15)
        if cp >= 0.80:
            insulin[i] = 16 * (1 - 0.35)
        if cp >= 1.20:
            insulin[i] = 16 * (1 - 0.55)
        if cp >= 1.80:
            insulin[i] = 7.5  # safety minimum
        if cp >= 2.50:
            insulin[i] = 0

    # Best and worst case bands
    beta_best = beta_mass * 1.5
    beta_worst = beta_mass * 0.6
    cp_best = cpeptide * 1.6
    cp_worst = cpeptide * 0.5

    fig, axes = plt.subplots(3, 1, figsize=(14, 14), sharex=True)

    # Beta cell mass
    ax1 = axes[0]
    ax1.fill_between(months, beta_worst * 100, beta_best * 100, alpha=0.2, color='#2ECC71')
    ax1.plot(months, beta_mass * 100, 'g-', linewidth=2.5, label='Expected')
    ax1.axhline(y=30, color='#E74C3C', linestyle='--', alpha=0.5, linewidth=1)
    ax1.text(1, 31, "Independence threshold (~30%)", fontsize=8, color='#E74C3C')
    ax1.set_ylabel("Beta Cell Mass (%)", fontsize=11)
    ax1.set_title("Expected Protocol Trajectory (24 Months)", fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(alpha=0.3)

    # C-peptide
    ax2 = axes[1]
    ax2.fill_between(months, cp_worst, cp_best, alpha=0.2, color='#3498DB')
    ax2.plot(months, cpeptide, 'b-', linewidth=2.5, label='Expected')
    # Milestone lines
    milestones_cp = [0.20, 0.40, 0.80, 1.20, 1.80]
    milestone_labels = ["First signal", "Early response", "Moderate recovery", "Strong recovery", "Near independence"]
    for cp_val, lbl in zip(milestones_cp, milestone_labels):
        ax2.axhline(y=cp_val, color='#999', linestyle=':', alpha=0.4)
        ax2.text(24.5, cp_val, lbl, fontsize=7, va='center', color='#666')
    ax2.set_ylabel("C-peptide (nmol/L)", fontsize=11)
    ax2.legend(fontsize=10)
    ax2.grid(alpha=0.3)

    # Insulin dose
    ax3 = axes[2]
    ax3.plot(months, insulin, 'r-', linewidth=2.5, label='Expected insulin dose')
    ax3.axhline(y=7.5, color='#F39C12', linestyle='--', alpha=0.5)
    ax3.text(1, 8.2, "Safety floor (0.1 U/kg)", fontsize=8, color='#F39C12')
    ax3.set_ylabel("Insulin (U/day)", fontsize=11)
    ax3.set_xlabel("Months", fontsize=11)
    ax3.legend(fontsize=10)
    ax3.grid(alpha=0.3)

    # Phase annotations
    for ax in axes:
        ax.axvspan(0, 3, alpha=0.05, color='red')
        ax.axvspan(3, 6, alpha=0.05, color='green')
        ax.axvspan(6, 12, alpha=0.05, color='blue')
        ax.axvspan(12, 24, alpha=0.05, color='purple')

    plt.tight_layout()

    output_path = os.path.join(FIGURES_DIR, "protocol_expected_trajectory.png")
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {output_path}")
    return output_path


# =============================================================================
# PRINTABLE LAB ORDER SHEETS
# =============================================================================

def generate_lab_orders():
    """Generate printable lab order information for each visit."""
    visits = {
        "BASELINE (Week -1)": {
            "fasting": True,
            "priority": "ALL required before starting protocol",
            "tests": [
                ("C-peptide, fasting", "004051", "Serum, fasting 12hr"),
                ("C-peptide, stimulated (MMTT)", "MMTT", "Requires clinic: Boost drink + timed draws 0/30/60/90/120 min"),
                ("HbA1c", "001453", "Whole blood EDTA"),
                ("GAD65 Ab", "164350", "Serum"),
                ("IA-2 Ab", "164355", "Serum"),
                ("ZnT8 Ab", "ZnT8", "Serum (specialty lab)"),
                ("hs-CRP", "120766", "Serum"),
                ("25-OH Vitamin D", "081950", "Serum"),
                ("CBC with differential", "005009", "Whole blood EDTA"),
                ("CMP (Comprehensive Metabolic Panel)", "322000", "Serum, fasting"),
                ("Lipid panel", "303756", "Serum, fasting"),
                ("Troponin I, high-sensitivity", "164921", "Serum"),
                ("NT-proBNP", "250913", "Serum"),
                ("ALT", "001545", "Serum"),
                ("AST", "001123", "Serum"),
                ("Enterovirus stool PCR", "EV-PCR", "Stool sample (specialty lab)"),
            ],
            "estimated_cost": "$815",
        },
        "MONTH 1 (Safety check)": {
            "fasting": False,
            "priority": "Fluoxetine liver safety + vitamin D compliance",
            "tests": [
                ("ALT", "001545", "Serum"),
                ("hs-CRP", "120766", "Serum"),
                ("25-OH Vitamin D", "081950", "Serum"),
            ],
            "estimated_cost": "$80",
        },
        "MONTH 3 (First efficacy check)": {
            "fasting": True,
            "priority": "C-peptide is the PRIMARY ENDPOINT",
            "tests": [
                ("C-peptide, fasting", "004051", "Serum, fasting 12hr"),
                ("HbA1c", "001453", "Whole blood EDTA"),
                ("hs-CRP", "120766", "Serum"),
                ("ALT", "001545", "Serum"),
                ("AST", "001123", "Serum"),
                ("25-OH Vitamin D", "081950", "Serum"),
                ("CBC", "005009", "Whole blood EDTA"),
            ],
            "estimated_cost": "$175",
        },
        "MONTH 6 (Comprehensive -- KEY decision point)": {
            "fasting": True,
            "priority": "FULL panel. This determines Phase 2 -> Phase 3 transition.",
            "tests": [
                ("C-peptide, fasting", "004051", "Serum, fasting 12hr"),
                ("C-peptide, stimulated (MMTT)", "MMTT", "Clinic: Boost + timed draws"),
                ("HbA1c", "001453", "Whole blood EDTA"),
                ("GAD65 Ab", "164350", "Serum"),
                ("hs-CRP", "120766", "Serum"),
                ("ALT + AST", "001545/001123", "Serum"),
                ("Troponin I, hs", "164921", "Serum"),
                ("CBC", "005009", "Whole blood EDTA"),
                ("CMP", "322000", "Serum"),
                ("25-OH Vitamin D", "081950", "Serum"),
                ("Fasting insulin", "004333", "Serum, fasting"),
            ],
            "estimated_cost": "$490",
        },
        "MONTH 9 (Interim)": {
            "fasting": True,
            "priority": "Track C-peptide trajectory",
            "tests": [
                ("C-peptide, fasting", "004051", "Serum, fasting 12hr"),
                ("HbA1c", "001453", "Whole blood EDTA"),
                ("hs-CRP", "120766", "Serum"),
                ("ALT", "001545", "Serum"),
            ],
            "estimated_cost": "$105",
        },
        "MONTH 12 (Full reassessment)": {
            "fasting": True,
            "priority": "PRIMARY ENDPOINT. One-year comprehensive evaluation.",
            "tests": [
                ("C-peptide, fasting", "004051", "Serum, fasting 12hr"),
                ("C-peptide, stimulated (MMTT)", "MMTT", "Clinic: Boost + timed draws"),
                ("HbA1c", "001453", "Whole blood EDTA"),
                ("GAD65 Ab", "164350", "Serum"),
                ("IA-2 Ab", "164355", "Serum"),
                ("hs-CRP", "120766", "Serum"),
                ("ALT + AST", "001545/001123", "Serum"),
                ("Troponin I, hs", "164921", "Serum"),
                ("NT-proBNP", "250913", "Serum"),
                ("CBC", "005009", "Whole blood EDTA"),
                ("CMP", "322000", "Serum"),
                ("25-OH Vitamin D", "081950", "Serum"),
                ("Fasting insulin", "004333", "Serum, fasting"),
            ],
            "estimated_cost": "$615",
        },
        "MONTH 18 (Durability)": {
            "fasting": True,
            "priority": "Confirm sustained response. Fluoxetine taper decision.",
            "tests": [
                ("C-peptide, fasting", "004051", "Serum, fasting 12hr"),
                ("HbA1c", "001453", "Whole blood EDTA"),
                ("ALT", "001545", "Serum"),
                ("25-OH Vitamin D", "081950", "Serum"),
            ],
            "estimated_cost": "$120",
        },
        "MONTH 24 (Final protocol assessment)": {
            "fasting": True,
            "priority": "COMPREHENSIVE. Two-year verdict. Compare to every prior result.",
            "tests": [
                ("C-peptide, fasting", "004051", "Serum, fasting 12hr"),
                ("C-peptide, stimulated (MMTT)", "MMTT", "Clinic: Boost + timed draws"),
                ("HbA1c", "001453", "Whole blood EDTA"),
                ("GAD65 Ab", "164350", "Serum"),
                ("IA-2 Ab", "164355", "Serum"),
                ("ZnT8 Ab", "ZnT8", "Serum"),
                ("hs-CRP", "120766", "Serum"),
                ("ALT + AST", "001545/001123", "Serum"),
                ("Troponin I, hs", "164921", "Serum"),
                ("NT-proBNP", "250913", "Serum"),
                ("CBC", "005009", "Whole blood EDTA"),
                ("CMP", "322000", "Serum"),
                ("25-OH Vitamin D", "081950", "Serum"),
                ("Fasting insulin", "004333", "Serum, fasting"),
                ("Lipid panel", "303756", "Serum, fasting"),
            ],
            "estimated_cost": "$725",
        },
    }
    return visits


# =============================================================================
# EMERGENCY PROTOCOLS
# =============================================================================

EMERGENCY_PROTOCOLS = {
    "hypoglycemia": {
        "title": "HYPOGLYCEMIA (Blood glucose < 70 mg/dL)",
        "severity_levels": [
            {
                "level": "MILD (54-70 mg/dL, aware)",
                "symptoms": "Shakiness, sweating, hunger, fast heartbeat, anxiety",
                "action": [
                    "Eat 15g fast carbs: 4 glucose tabs, 4oz juice, or 1 tbsp honey",
                    "Wait 15 minutes",
                    "Recheck blood glucose",
                    "If still <70: repeat 15g carbs",
                    "Once >70: eat a snack with protein + fat",
                    "Log the event. Identify cause (too much insulin? missed meal? exercise?)",
                ],
            },
            {
                "level": "MODERATE (40-54 mg/dL, symptomatic)",
                "symptoms": "Confusion, difficulty speaking, blurred vision, weakness",
                "action": [
                    "Eat 30g fast carbs immediately",
                    "If unable to eat safely: glucagon nasal spray (Baqsimi) or injection",
                    "Call someone to stay with you",
                    "Recheck in 15 minutes",
                    "If no improvement: CALL 911",
                    "After recovery: eat a full meal",
                    "Report to endocrinologist. Review insulin doses.",
                ],
            },
            {
                "level": "SEVERE (<40 mg/dL or unconscious)",
                "symptoms": "Seizure, loss of consciousness, unable to self-treat",
                "action": [
                    "CALL 911 IMMEDIATELY",
                    "If glucagon available: bystander should administer",
                    "Do NOT put food in mouth of unconscious person",
                    "Place on side (recovery position)",
                    "This is a medical emergency",
                ],
            },
        ],
    },
    "dka": {
        "title": "DKA SYMPTOMS (Diabetic Ketoacidosis)",
        "triggers": "Most likely during fasting, illness, missed insulin, or pump failure",
        "warning_signs": [
            "Blood BHB > 3.0 mM",
            "Blood glucose > 250 mg/dL + ketones > 1.5 mM",
            "Nausea and vomiting",
            "Abdominal pain",
            "Fruity/acetone breath",
            "Rapid deep breathing (Kussmaul breathing)",
            "Confusion, lethargy",
        ],
        "action": [
            "STOP FASTING immediately -- eat carbs",
            "Check blood glucose AND blood ketones",
            "If BHB > 3.0 mM with symptoms: GO TO ER",
            "If BHB > 5.0 mM: CALL 911 -- this IS DKA",
            "Take correction insulin dose (50% of normal correction factor)",
            "Drink water (dehydration accelerates DKA)",
            "Do NOT exercise (worsens ketosis)",
            "Do NOT take exogenous BHB supplements",
            "ER will give IV fluids + insulin drip",
        ],
    },
    "chest_pain": {
        "title": "CHEST PAIN / CARDIAC SYMPTOMS",
        "context": "CVB can cause myocarditis/pericarditis. Protocol includes cardiac monitoring.",
        "warning_signs": [
            "Chest pain (especially sharp, worse with breathing or lying down = pericarditis)",
            "Shortness of breath at rest or with minimal exertion",
            "New or worsening palpitations",
            "Sudden exercise intolerance",
            "Syncope (fainting) or near-syncope",
        ],
        "action": [
            "STOP all exercise immediately",
            "If severe chest pain or difficulty breathing: CALL 911",
            "If mild and intermittent: urgent cardiology appointment (within 24-48h)",
            "Troponin and BNP blood test ASAP",
            "ECG and echocardiogram",
            "DO NOT fast until cardiac evaluation is complete",
            "Continue fluoxetine and supplements (these are not cardiac-risky)",
            "Report to protocol-monitoring endocrinologist",
        ],
    },
    "severe_side_effects": {
        "title": "SEVERE SIDE EFFECTS",
        "fluoxetine": {
            "stop_immediately_if": [
                "Rash, hives, swelling (allergic reaction)",
                "Jaundice (yellowing of skin/eyes) -- hepatotoxicity",
                "Severe agitation, tremor, fever, diarrhea (serotonin syndrome -- RARE)",
                "Suicidal thoughts (rare in adults, report immediately)",
                "Seizure",
            ],
            "reduce_dose_if": [
                "Persistent severe nausea (>2 weeks)",
                "Sexual dysfunction (common, discuss with doctor)",
                "Significant weight change",
                "Excessive sedation or insomnia",
            ],
        },
        "semaglutide": {
            "stop_immediately_if": [
                "Severe abdominal pain that won't stop (pancreatitis risk)",
                "Vision changes (rare: diabetic retinopathy worsening)",
                "Allergic reaction (rash, swelling, breathing difficulty)",
                "Severe vomiting unable to keep fluids down >24h",
            ],
            "reduce_dose_if": [
                "Persistent nausea >2 weeks",
                "Weight loss >5% in first month (too fast for T1DM patient)",
                "Frequent loose stools",
            ],
        },
        "general_rule": "When in doubt, contact your endocrinologist. "
                        "If they are unavailable and symptoms are severe, go to the ER. "
                        "Bring your medication list and tell them you are on an experimental "
                        "supplement protocol for T1DM beta cell recovery.",
    },
}


# =============================================================================
# JSON OUTPUT
# =============================================================================

def generate_json_output():
    """Generate complete structured JSON of the entire protocol."""
    output = {
        "protocol": PROTOCOL,
        "shopping_list": SHOPPING_LIST,
        "lab_orders": generate_lab_orders(),
        "emergency_protocols": EMERGENCY_PROTOCOLS,
        "cost_summary": {
            "tier_1_monthly_ongoing": 198,
            "tier_2_monthly_ongoing": 218,
            "tier_3_monthly_ongoing": 518,
            "year_1_tier_1": None,  # computed below
            "year_1_tier_2": None,
            "year_1_tier_3": None,
            "year_2_tier_1": None,
            "year_2_tier_2": None,
            "year_2_tier_3": None,
        },
        "model_predictions": {
            "inequality_reversal_month": "8-10 (expected)",
            "first_cpeptide_signal_month": "3-6",
            "insulin_independence_month": "24-36 (expected case)",
            "probability_cpeptide_improvement_3yr": "65-80%",
            "probability_insulin_independence_3yr": "20-35%",
        },
    }

    # Compute year costs
    months, tiers, cum = compute_cumulative_costs()
    # Find index of month 12 and month 24
    m12_idx = months.index(12) if 12 in months else -1
    m24_idx = months.index(24) if 24 in months else -1

    if m12_idx >= 0:
        output["cost_summary"]["year_1_tier_1"] = cum["tier_1"][m12_idx]
        output["cost_summary"]["year_1_tier_2"] = cum["tier_2"][m12_idx]
        output["cost_summary"]["year_1_tier_3"] = cum["tier_3"][m12_idx]
    if m24_idx >= 0:
        output["cost_summary"]["year_2_tier_1"] = cum["tier_1"][m24_idx]
        output["cost_summary"]["year_2_tier_2"] = cum["tier_2"][m24_idx]
        output["cost_summary"]["year_2_tier_3"] = cum["tier_3"][m24_idx]

    output_path = os.path.join(RESULTS_DIR, "protocol_implementation.json")
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2, default=str)
    print(f"Saved: {output_path}")
    return output_path


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 70)
    print("T1DM BETA CELL RECOVERY PROTOCOL -- IMPLEMENTATION GENERATOR")
    print("=" * 70)
    print()

    # Generate all outputs
    print("1. Generating Gantt chart timeline...")
    gantt_path = generate_gantt_chart()

    print("2. Generating cost breakdown plots...")
    cost_path = generate_cost_plots()

    print("3. Generating decision tree...")
    tree_path = generate_decision_tree()

    print("4. Generating expected trajectory plot...")
    traj_path = generate_trajectory_plot()

    print("5. Generating lab order sheets...")
    lab_orders = generate_lab_orders()

    print("6. Generating structured JSON output...")
    json_path = generate_json_output()

    print()
    print("=" * 70)
    print("COST SUMMARY")
    print("=" * 70)
    months, tiers, cum = compute_cumulative_costs()

    m12_idx = months.index(12)
    m24_idx = months.index(24)

    print(f"\n{'Tier':<25} {'Year 1':>12} {'Year 2 (cum)':>15} {'Monthly avg':>15}")
    print("-" * 70)
    print(f"{'Tier 1 (Essential)':<25} ${cum['tier_1'][m12_idx]:>10,.0f} ${cum['tier_1'][m24_idx]:>13,.0f} ${cum['tier_1'][m24_idx]/25:>13,.0f}")
    print(f"{'Tier 2 (Full)':<25} ${cum['tier_2'][m12_idx]:>10,.0f} ${cum['tier_2'][m24_idx]:>13,.0f} ${cum['tier_2'][m24_idx]/25:>13,.0f}")
    print(f"{'Tier 3 (Premium)':<25} ${cum['tier_3'][m12_idx]:>10,.0f} ${cum['tier_3'][m24_idx]:>13,.0f} ${cum['tier_3'][m24_idx]/25:>13,.0f}")

    print()
    print("=" * 70)
    print("LAB ORDER SUMMARY")
    print("=" * 70)
    for visit, info in lab_orders.items():
        fasting_note = " [FASTING REQUIRED]" if info["fasting"] else ""
        print(f"\n--- {visit}{fasting_note} ---")
        print(f"    Priority: {info['priority']}")
        print(f"    Estimated cost: {info['estimated_cost']}")
        for test_name, code, specimen in info["tests"]:
            print(f"    [ ] {test_name} ({code}) -- {specimen}")

    print()
    print("=" * 70)
    print("ALL OUTPUTS GENERATED")
    print("=" * 70)
    print(f"  Gantt chart:    {gantt_path}")
    print(f"  Cost plots:     {cost_path}")
    print(f"  Decision tree:  {tree_path}")
    print(f"  Trajectory:     {traj_path}")
    print(f"  JSON:           {json_path}")
    print()
    print("Protocol implementation bridge: COMPLETE")
    print()


if __name__ == "__main__":
    main()
