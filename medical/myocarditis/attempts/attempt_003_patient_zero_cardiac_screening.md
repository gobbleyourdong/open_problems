# Attempt 003: the patient Cardiac Screening — Detection and Early Intervention Protocol

## The Rationale

the patient has confirmed T1DM → confirmed CVB exposure → elevated risk for subclinical myocarditis. The T1DM protocol will treat the virus systemically, but we need to KNOW the cardiac status before starting because:

1. **Itraconazole is contraindicated in heart failure** (FDA black box)
2. **Baseline cardiac status determines monitoring intensity**
3. **Subclinical myocarditis caught early has excellent prognosis with antiviral treatment**
4. **Missed subclinical myocarditis can progress silently to DCM**

## The Screening Protocol for the patient

### Step 1: Non-Invasive Markers (Day 1 — blood draw)
```
hs-Troponin I:
  <14 ng/L → no active cardiomyocyte damage → REASSURING
  14-52 ng/L → low-grade damage → CONCERNING (subclinical myocarditis?)
  >52 ng/L → active damage → URGENT cardiac workup

NT-proBNP:
  <125 pg/mL → no wall stress → REASSURING
  125-450 pg/mL → mild stress → CONCERNING
  >450 pg/mL → significant stress → URGENT

ECG:
  Normal → REASSURING
  ST changes, T wave inversions, low voltage, arrhythmia → CONCERNING
  New bundle branch block, AV block → URGENT
```

### Step 2: Echocardiogram (If ANY Step 1 marker abnormal, or as baseline)
```
LVEF:
  >55% → normal systolic function → REASSURING
  45-55% → mildly reduced → MONITORING (early DCM?)
  35-45% → moderately reduced → TREATMENT (start GDMT)
  <35% → severely reduced → URGENT (advanced HF)

Chamber dimensions:
  Normal → good
  LV dilation → DCM pattern → start GDMT

Diastolic function:
  Normal → good
  Impaired relaxation → early dysfunction → monitor

Wall motion:
  Normal → good
  Regional abnormalities → possible focal myocarditis/fibrosis
```

### Step 3: Cardiac MRI (The Gold Standard — if echo abnormal OR as proactive baseline)
```
Cardiac MRI reveals what echo and biomarkers cannot:

T2 mapping (edema):
  Normal T2 → no active inflammation → no active myocarditis
  Elevated T2 (regional or global) → ACTIVE inflammation → active myocarditis
  
T1 mapping (diffuse fibrosis):
  Normal T1 → no diffuse fibrosis → EARLY (good prognosis)
  Elevated native T1 → diffuse fibrosis → ESTABLISHED disease
  
Late Gadolinium Enhancement (LGE):
  No LGE → no focal fibrosis → EXCELLENT
  Mid-wall LGE → viral/inflammatory pattern → CVB myocarditis signature
  Subendocardial LGE → ischemic pattern → different etiology
  
Extracellular Volume (ECV):
  Normal → no diffuse fibrosis → REASSURING
  Elevated → diffuse fibrosis or inflammation → CONCERNING

LVEF on MRI (more accurate than echo):
  Confirms or refines echo LVEF measurement
```

## Decision Matrix

```
SCENARIO A: All normal (most likely)
  hs-TnI <14, BNP <125, ECG normal
  ├── No subclinical myocarditis detected
  ├── Safe to use itraconazole in protocol
  ├── Cardiac MRI optional but recommended as baseline
  ├── Start full T1DM protocol as designed
  └── Repeat cardiac markers at 3, 6, 12 months

SCENARIO B: Borderline (troponin 14-52 or BNP mildly elevated)
  ├── Echo + cardiac MRI mandatory
  ├── If MRI shows T2 elevation: ACTIVE subclinical myocarditis
  │   ├── DO NOT use itraconazole (cardiotoxic)
  │   ├── Fluoxetine as sole antiviral (safe in cardiac patients)
  │   ├── Add colchicine 0.5mg (anti-inflammatory, may be cardioprotective)
  │   ├── Add empagliflozin 10mg (HF prevention + autophagy)
  │   └── Repeat MRI at 3 months (expect T2 normalization with antiviral)
  ├── If MRI shows LGE but normal T2: OLD fibrosis, no active inflammation
  │   ├── Scar is stable — not actively worsening
  │   ├── Antiviral protocol may prevent further fibrosis
  │   └── Standard monitoring

SCENARIO C: Abnormal (LVEF reduced, significant LGE)
  ├── Established CVB cardiomyopathy alongside T1DM
  ├── Start GDMT immediately:
  │   ├── Sacubitril/valsartan (ARNI)
  │   ├── Carvedilol (beta-blocker)
  │   ├── Spironolactone (MRA)
  │   └── Empagliflozin (SGLT2i — triple purpose)
  ├── Fluoxetine as sole antiviral (NO itraconazole)
  ├── FMD only if LVEF >35% and clinically stable
  ├── More frequent monitoring (monthly echo, troponin)
  └── Referral to cardiologist for co-management
```

## The Probability Estimate

Based on general population data for CVB-seropositive adults:
- ~60-70% of adults are CVB seropositive
- Of seropositive: ~5-10% have evidence of subclinical cardiac involvement on MRI
- the patient is CONFIRMED CVB-seropositive (T1DM = CVB evidence)
- Risk of subclinical myocarditis: estimated 5-15% (higher than general population)

**Most likely outcome: Scenario A (all normal).** But checking is essential because Scenario B is treatable and Scenario C requires protocol modification.

## The T2 Mapping Insight

If cardiac MRI shows elevated T2 in myocardium:
- This is ACTIVE inflammation (edema) → active myocarditis → CVB is currently damaging the heart
- Starting fluoxetine + anti-inflammatory stack should normalize T2 within 3-6 months
- **T2 normalization on follow-up MRI = direct evidence that the protocol is working at the cardiac level**
- This becomes a measurable cardiac endpoint ALONGSIDE the T1DM C-peptide endpoint

## Cost
- hs-Troponin + BNP + ECG: ~$150
- Echo: ~$400
- Cardiac MRI: ~$1,000-2,000
- Total cardiac screening: $150-2,550 depending on how far down the decision tree

## Status: SCREENING PROTOCOL — actionable immediately, determines protocol modifications for the patient
