# the patient — Week-by-Week Implementation Timeline

> This document integrates PATIENT_ZERO_SCREENING, DRUG_SAFETY_MATRIX, and the T1DM protocol into a concrete implementation plan. Every week has specific actions and decision gates.

## Pre-Protocol: Screening Phase

### WEEK 0: Blood Draw
**Location**: Any Quest/LabCorp or primary care office

**Order:**
```
ESSENTIAL (non-negotiable):
  □ C-peptide, fasting
  □ C-peptide, stimulated (mixed-meal tolerance test OR glucagon stim)
  □ HbA1c
  □ Comprehensive metabolic panel (includes ALT, AST, glucose, electrolytes)
  □ hs-Troponin I
  □ NT-proBNP
  □ CBC with differential
  □ hs-CRP
  □ 25-OH Vitamin D
  □ Testosterone, total + free (if male)
  □ FSH (if male)

HIGH PRIORITY (if available):
  □ CVB1-5 neutralizing antibodies (research/specialty lab)
  □ Serum enteroviral RT-PCR (research lab)
  □ Stool enteroviral RT-PCR (clinical virology)
  □ Selenium (serum)
  □ Zinc (serum)
  □ Ferritin

IDEAL (if accessible and affordable):
  □ NK cell cytotoxicity assay
  □ Treg frequency (flow cytometry: CD4+CD25+FOXP3+)
  □ Cytokine panel (IL-1β, IL-6, TNF-α, IL-10, IFN-α)
  □ ECG
```

**Cost**: $300-800 depending on what's ordered and insurance coverage

### WEEK 1: Results Review + Decision Tree

**C-peptide result determines the entire T1DM strategy:**
```
Stimulated C-peptide ≥ 0.6 ng/mL:
  → SIGNIFICANT residual beta cell function
  → The R > D model is testable
  → Full protocol JUSTIFIED — realistic chance of insulin independence
  → This is the BEST CASE scenario

Stimulated C-peptide 0.2-0.6 ng/mL:
  → Reduced but present function
  → Protocol may slow destruction and allow partial recovery
  → Insulin reduction (not independence) is realistic goal
  → Still worth pursuing

Stimulated C-peptide < 0.2 ng/mL:
  → Minimal residual function
  → Protocol may prevent further loss and stabilize
  → Insulin independence UNLIKELY without regeneration strategy
  → Anti-inflammatory + antiviral still valuable (protects other organs)
  → Consider adding semaglutide for regeneration support

Stimulated C-peptide undetectable:
  → See FAILURE_MODES.md, Mode 1
  → Anti-inflammatory stack still protects heart, CNS, other organs
  → Pivot T1DM strategy to stem cell + immune protection
```

**Cardiac results:**
```
hs-Troponin <14 ng/L AND BNP <125 pg/mL:
  → Cardiac status: CLEAR
  → Itraconazole safe to use (if desired)
  → No cardiac MRI urgently needed (but baseline recommended)

Either marker elevated:
  → Order: echocardiogram + cardiac MRI with LGE and T2 mapping
  → See myocarditis/attempts/attempt_003 for full decision tree
  → Itraconazole CONTRAINDICATED until cardiac status clarified
```

**Liver results:**
```
ALT and AST within normal limits:
  → Liver status: CLEAR
  → Full protocol safe

ALT or AST 1-3x ULN:
  → Investigate: exclude NAFLD, medications, alcohol
  → Start fluoxetine at 10mg (half dose), recheck LFTs at 2 weeks
  → Itraconazole: use with caution, check LFTs weekly × 4 weeks

ALT or AST >3x ULN:
  → Do NOT start hepatotoxic drugs until investigated
  → May be subclinical CVB hepatitis — check enteroviral RNA
  → Fluoxetine still possible at reduced dose with monitoring
  → Itraconazole: AVOID
```

**Micronutrient results:**
```
Vitamin D < 30 ng/mL:
  → Loading dose: 50,000 IU × 1 (if <20) then 5,000 IU daily
  → Recheck at 3 months, target 40-60 ng/mL

Selenium < 70 μg/L:
  → Start 200 μg/day immediately (Keshan disease connection — see attempt 004)
  → Low selenium may be ENHANCING CVB virulence in this patient

Zinc < 60 μg/dL:
  → Start 15 mg/day + copper 2 mg/day (prevent zinc-induced copper deficiency)

Ferritin < 30 ng/mL:
  → Iron deficiency — but DO NOT supplement iron during active viral protocol
  → Iron feeds viral replication (hepcidin response is a defense)
  → Address after viral clearance phase (month 6+)

Ferritin > 300 ng/mL:
  → Chronic inflammation marker — will likely normalize with protocol
```

## Protocol Phase 1: Foundation (Weeks 2-4)

**Start the safe, non-controversial components first. Build the anti-inflammatory and immune base before adding antivirals.**

### Week 2: Start supplements
```
□ Vitamin D 5,000 IU daily (or loading dose if deficient)
□ Omega-3 (EPA/DHA) 3g daily (with food)
□ Butyrate 300mg TID (enteric coated, with meals)
□ Magnesium glycinate 400mg (bedtime)
□ Selenium 200μg daily (if deficient or not tested)
□ Zinc 15mg + Copper 2mg daily
□ CoQ10 600mg daily (with fat-containing meal) — Complex I cofactor; mt-ND3 target
□ NAD+ precursor: NMN 500mg or NR 500mg daily (morning) — mitochondrial repair
□ Trehalose 2g daily (in water, with any meal) — TFEB activator → lysosomal biogenesis; $15/month, food-grade
   NOTE: trehalose is a disaccharide; use pure crystalline form (not a sweetener blend)
□ Vitamin K2 (MK-7 form) 100-200μg daily — REQUIRED with VitD 5000 IU to prevent
   soft-tissue calcium deposition; VDR activation increases calcium absorption
□ GABA 500mg daily (with food) — alpha→beta transdifferentiation (R₃ term);
   synergistic with FMD refeeding window; take in evenings (mild calming effect)
□ Increase Butyrate to 4,000mg/day by end of week 2 (start at 1g, add 1g every 3 days)
   [CRITICAL DOSE CHANGE from initial 300mg — 4-6g needed for FOXP1/HDAC mechanism]

DO NOT START YET:
  × Fluoxetine (wait for baseline stabilization)
  × Fasting/FMD (wait for antiviral support)
  × Cold exposure (wait for foundation)
  × Itraconazole (conditional on cardiac/hepatic status)
```

### Week 3: Add lifestyle interventions
```
□ Sleep optimization: target 7-9 hours, consistent schedule
   (NK cell activity peaks during sleep — this is not optional)
□ Time-restricted eating: 16:8 pattern (eating window 12-8pm)
   (Mild autophagy induction, glucose monitoring required)
□ Glucose monitoring: track fasting glucose, post-meal glucose during TRE
   (Adjust insulin as needed — TRE will reduce insulin requirements)
```

### Week 4: Pre-antiviral assessment
```
□ How did TRE affect glucose? Insulin needs changed?
□ Any supplement side effects? GI issues with butyrate?
□ Sleep improved? Energy level baseline noted?
□ If cardiac MRI was ordered: results reviewed?
□ DECISION GATE: ready to add antiviral?
```

## Protocol Phase 2: Antiviral (Weeks 5-8)

### Week 5: Start fluoxetine
```
□ Fluoxetine 10mg daily × 7 days (titration)
   - Monitor: mood, sleep, GI (common SSRI startup effects)
   - T1DM specific: fluoxetine can affect glucose — monitor closely
   
□ Continue all supplements
□ Continue TRE (16:8)
```

### Week 6: Titrate fluoxetine
```
□ Fluoxetine 20mg daily (target dose)
   - Takes 4-5 weeks to reach steady state (long half-life)
   - Antiviral effect begins ramping up
   
□ Check LFTs if any liver concern from Week 1
```

### Week 7-8: Stabilize on fluoxetine
```
□ Continue fluoxetine 20mg
□ Monitor glucose patterns (fluoxetine may slightly lower glucose)
□ Optional: add itraconazole 200mg if cardiac/hepatic CLEAR
   - If adding: ⚠️ REDUCE colchicine to 0.25mg or STOP colchicine
□ Plan first FMD cycle for Week 9
```

## Protocol Phase 3: Autophagy Activation (Weeks 9-12)

### Week 9: First FMD cycle
```
⚠️ MEDICAL SUPERVISION REQUIRED for T1DM patient during fasting

5-DAY FASTING-MIMICKING DIET:
  Day 1: ~1,100 kcal (34% carb, 56% fat, 10% protein)
  Days 2-5: ~725 kcal (47% carb, 44% fat, 9% protein)
  
INSULIN MANAGEMENT DURING FMD:
  □ Reduce bolus insulin by 50-75% (less food = less insulin)
  □ Reduce basal insulin by 20-30%
  □ Monitor glucose every 2-3 hours during waking
  □ Keep glucose rescue available (juice, glucose tabs)
  □ Target: glucose 80-180 mg/dL (wider range during fasting)
  □ If glucose <70: break fast immediately, treat hypoglycemia
  
POST-FMD REFEEDING (Days 6-7):
  □ Gradual reintroduction of normal calories
  □ This is the REGENERATION WINDOW (Longo 2017)
  □ Beta cell progenitors activated during refeeding
  □ Resume normal insulin dosing gradually
```

### Week 10: Recovery + assessment
```
□ How did FMD go? Glucose control?
□ Any hypoglycemic episodes?
□ Energy level? (expect temporary fatigue during FMD, recovery after)
□ Adjust plan for next FMD cycle (month 2)
```

### Week 11: Add cold exposure
```
□ Start cold face immersion (30 seconds, basin of cold water)
   - Triggers mammalian dive reflex → vagal tone → anti-inflammatory
   - Safe, minimal stress
   
□ Progress to: cold shower, last 30 seconds
   - Norepinephrine release → NK mobilization → IL-10 production
   - Increase by 15 seconds/week up to 2 minutes
```

### Week 12: Add Wim Hof breathing
```
□ 3 rounds of WHM breathing, morning
   - 30 deep breaths → exhale → hold → inhale hold
   - Intermittent hypoxia → epinephrine spike → β-arrestin-2 → IκBα stabilization → attenuated NF-κB (Kox 2014 *PNAS* PMID 24799686)
   - See T1DM attempt 061, 062, 063 for molecular mechanism
   
□ Sequence: WHM breathing → cold shower → supplements → breakfast (end of 16hr fast)
   - This 30-minute morning routine hits: autophagy, NLRP3, NF-κB, NK cells, Tregs
```

## Protocol Phase 4: Measurement (Week 13 / Month 3)

### Week 13: First follow-up labs
```
□ C-peptide, fasting + stimulated (THE KEY MEASUREMENT)
   Compare to baseline:
   - Improved → protocol working, continue
   - Stable → may need more time (antiviral steady state was reached at ~Week 10)
   - Declined → reassess (see FAILURE_MODES.md)

□ HbA1c (reflects prior 3 months — may be too early for change)
□ hs-CRP (expect reduction if anti-inflammatory stack working)
□ LFTs (safety monitoring)
□ Insulin requirements log (trend more informative than single measure)

□ Second FMD cycle (Week 13-14)
```

## Protocol Phase 5: Continuation (Months 4-12)

```
MONTHLY:
  □ FMD cycle (5 days)
  □ Insulin requirement tracking
  □ Glucose averages (CGM data if available)

QUARTERLY (Months 3, 6, 9, 12):
  □ C-peptide (fasting + stimulated)
  □ HbA1c
  □ hs-CRP
  □ LFTs
  □ CVB serology (if available — tracking antibody response)
  □ Cardiac markers (troponin, BNP) at month 6 and 12

AT MONTH 6:
  □ Full reassessment
  □ If C-peptide improving: continue protocol, consider reducing insulin
  □ If C-peptide stable: add semaglutide for regeneration boost?
  □ If C-peptide declining: add teplizumab (if accessible)?
  □ Cardiac MRI if baseline was abnormal

AT MONTH 12:
  □ Comprehensive reassessment
  □ Decision: continue, modify, or declare failure
  □ Publish findings regardless of outcome (both positive and negative results matter)
```

## The Decision Points Summary

```
Week 1:  C-peptide result → determines ambition level
Week 1:  Cardiac/hepatic results → determines drug selection
Week 4:  Foundation tolerance → proceed to antiviral?
Week 8:  Fluoxetine tolerance → proceed to FMD?
Week 13: First C-peptide follow-up → protocol working?
Month 6: Midpoint reassessment → continue/modify/escalate?
Month 12: Final assessment → success/partial/failure?
```

## Cost Summary (12-Month Protocol)

| Component | Monthly | Annual |
|-----------|---------|--------|
| Supplements (D, omega-3, butyrate, Mg, Se, Zn, CoQ10) | $120 | $1,440 |
| Fluoxetine 20mg | $4 | $48 |
| FMD food costs (5 days × 12 months) | $50 | $600 |
| Labs (quarterly C-peptide + panels) | ~$100 | $1,200 |
| Baseline screening | — | $500 |
| Cardiac MRI (if needed) | — | $1,500 |
| **Total (without MRI)** | | **$3,788** |
| **Total (with MRI)** | | **$5,288** |

**Under $5,300 for a 12-month cure attempt.** Compare: annual cost of T1DM management (insulin, CGM, supplies, complications): $10,000-20,000+.
