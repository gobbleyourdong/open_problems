# the patient — Multi-Disease CVB Screening Protocol

## Rationale

the patient has confirmed T1DM → confirmed CVB exposure → ALL 12 CVB diseases are possible.
The T1DM protocol treats the whole virus, not just the pancreas. But we need to know WHAT ELSE is affected before starting, for three reasons:
1. **Safety**: itraconazole contraindicated in heart failure, hepatotoxic with liver disease
2. **Monitoring**: need baselines to detect improvement
3. **Completeness**: clearing CVB from pancreas but missing cardiac/CNS/testicular reservoir = reseeding

## The Screening Panel

### Tier 1: Blood Draw (Standard Lab, ~$300-500 total)

| Test | Screens for | Normal | Flag if |
|------|------------|--------|---------|
| **Troponin-I (hs)** | Active myocardial damage | <14 ng/L | Any elevation |
| **NT-proBNP** | Cardiac wall stress / heart failure | <125 pg/mL (age-adjusted) | Elevated |
| **ALT, AST** | Hepatocellular damage | <40 U/L | >1.5x ULN |
| **GGT, ALP** | Cholestatic liver disease | Age/sex normal ranges | Elevated |
| **Bilirubin (total + direct)** | Liver function | <1.2 mg/dL total | Elevated direct |
| **Testosterone (total + free)** | Leydig cell function (orchitis) | Age-adjusted | Below normal |
| **FSH** | Sertoli cell function | 1.5-12.4 mIU/mL | Elevated |
| **Inhibin B** | Direct Sertoli cell marker | 80-400 pg/mL | Low |
| **CRP (hs)** | Systemic inflammation | <1.0 mg/L | >3.0 mg/L |
| **ESR** | Chronic inflammation | <15 mm/hr | Elevated |
| **25-OH Vitamin D** | Baseline for protocol | 30-100 ng/mL | <30 (deficiency) |
| **Selenium (serum)** | NK cell function support | 70-150 μg/L | <70 |
| **Zinc (serum)** | NK cell maturation | 60-120 μg/dL | <60 |
| **Ferritin** | Iron stores / inflammation | 30-300 ng/mL | <30 or >300 |
| **CBC with differential** | Immune cell counts | Normal ranges | Lymphopenia, NK count |
| **HbA1c** | Glycemic control (T1DM baseline) | <7% target | Baseline |
| **C-peptide (fasting + stimulated)** | Beta cell function (the KEY measurement) | >0.6 ng/mL = residual function | Any positive = hope |
| **GADA (GAD65 antibody)** | LADA screen — T1DM vs T2DM distinction | Negative | Positive = LADA confirmed → switch from sulfonylurea, CVB protocol indicated |
| **TSH + free T4** | Thyroid function | TSH 0.4-4.0 mIU/L | Abnormal TSH |
| **Anti-TPO antibody** | Hashimoto's co-screen (25-30% of T1DM) | <35 IU/mL | Positive → thyroid CVB co-involvement likely |
| **Anti-transglutaminase-2 (anti-TG2)** | Celiac disease co-screen (5-10% of T1DM) | <7 U/mL | Positive → celiac (Disease 17 candidate), GADA + anti-TG2 = full polyglandular screen |

### Tier 2: CVB-Specific (Research/Specialty Lab, ~$200-400)

| Test | What it shows | Where to order |
|------|-------------|---------------|
| **CVB1-5 neutralizing antibodies** | Serotype-specific immune history | Research virology lab |
| **Enteroviral VP1 antigen (serum)** | Active/recent CVB | Research lab |
| **Stool enteroviral RT-PCR** | Gut viral shedding | Clinical virology |
| **IFN-α level** | Ongoing antiviral response (elevated if virus persisting) | Immunology lab |

### Tier 3: Imaging (~$500-2000)

| Test | Screens for | When to order |
|------|------------|---------------|
| **Cardiac MRI with LGE** | Subclinical myocarditis/fibrosis | If troponin or BNP abnormal, or as baseline |
| **Echocardiogram** | LVEF, chamber dimensions, valve function | If any cardiac marker abnormal |
| **Testicular ultrasound** | Inflammation, atrophy | If testosterone low or FSH elevated |

### Tier 4: Functional / Immune (Specialty, ~$300-600)

| Test | What it shows | When to order |
|------|-------------|---------------|
| **NK cell cytotoxicity assay** | Functional immune capacity | Baseline for protocol monitoring |
| **Treg frequency (flow cytometry)** | CD4+CD25+FOXP3+ as % of CD4 | Baseline for immune status |
| **Cytokine panel (IL-1β, IL-6, TNF-α, IL-10)** | Inflammatory balance | Baseline |

## Decision Tree

```
RESULTS → ACTION

Troponin/BNP elevated → Cardiac MRI → 
  ├── LGE positive → active myocarditis/fibrosis → ESCALATE cardiac protocol
  │   ├── Start GDMT if LVEF reduced
  │   ├── Avoid itraconazole (cardiotoxic)
  │   └── Prioritize cardiac monitoring during CVB clearance
  └── LGE negative → functional cardiac concern → echo follow-up

ALT/AST elevated →
  ├── Exclude NAFLD, alcohol, medications
  ├── Check CVB serology → if positive: subclinical CVB hepatitis
  ├── Reduce itraconazole dose or avoid
  └── Use fluoxetine as primary antiviral (hepatically metabolized but better safety profile)

Testosterone low / FSH elevated →
  ├── Testicular ultrasound
  ├── If abnormal: CVB orchitis suspected → testicular reservoir
  ├── Ensure fluoxetine (crosses BTB) is primary antiviral
  └── Monitor testosterone during protocol (should improve with viral clearance)

CRP > 3.0 →
  ├── Chronic inflammation confirmed
  ├── Aggressive anti-inflammatory stack justified
  └── Good baseline for monitoring response

Vitamin D < 30 →
  ├── Start 5000 IU immediately (loading dose 50,000 IU × 1 if <20)
  └── Recheck at 3 months

Se/Zn low →
  ├── NK cell function likely impaired
  ├── Start supplementation immediately
  └── Critical for immune protocol success

C-peptide:
  ├── Stimulated > 0.6 ng/mL → significant residual function → BEST PROGNOSIS
  ├── Stimulated 0.2-0.6 → reduced but present → GOOD PROGNOSIS  
  ├── Stimulated < 0.2 → minimal residual → harder but not impossible
  └── Undetectable → beta cells very low → depends on regeneration capacity
```

## Priority Order

1. **C-peptide** (fasting + stimulated) — determines whether the protocol can work for T1DM
2. **GADA** — identifies LADA (better prognosis if positive); change medication class immediately
3. **Anti-TPO + TSH** — thyroid co-screen (25-30% T1DM); anti-TPO decline validates protocol
4. **Cardiac panel** (troponin, BNP, +/- MRI) — safety before starting drugs
3. **Liver panel** (ALT, AST, GGT) — drug dosing safety
4. **CVB serology** — confirm viral hypothesis
5. **Immune panel** (NK, Tregs, cytokines) — optimize protocol targeting
6. **Hormonal** (testosterone, FSH) — identify reservoirs
7. **Micronutrients** (D, Se, Zn) — fill gaps before starting protocol

## Cost Summary

| Tier | Cost | Priority |
|------|------|----------|
| Tier 1 (blood) | $300-500 | ESSENTIAL — order immediately |
| Tier 2 (CVB-specific) | $200-400 | HIGH — confirms viral hypothesis |
| Tier 3 (imaging) | $500-2000 | CONDITIONAL — based on Tier 1 results |
| Tier 4 (functional immune) | $300-600 | IDEAL — establishes treatment baselines |
| **Total (comprehensive)** | **$1,300-3,500** | |

## Timeline

```
Week 1:  Tier 1 blood draw (can be done at any Quest/LabCorp)
Week 2:  Results back → decision tree → order Tier 2 + conditional Tier 3
Week 3:  Tier 2 results → CVB hypothesis confirmed/denied
Week 4:  START PROTOCOL (with appropriate modifications based on screening)
         Continue Tier 3/4 if ordered
```

**The screening IS the wall.** (THEWALL.md, final line: "The bloodwork appointment is the wall.")
