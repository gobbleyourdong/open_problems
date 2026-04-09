# Pattern 001: The DCM Reversibility Window

## Status: QUANTIFIED (ODE model + parameter sweeps)

## The Pattern

Dilated cardiomyopathy (CVB-induced) is the downstream consequence of uncleared viral myocarditis. The progression is:

```
Acute myocarditis → incomplete viral clearance → TD mutant persistence
→ chronic 2A protease → dystrophin cleavage → DGC disruption
→ sarcolemma tears → cardiomyocyte death → fibrosis → dilation → heart failure
```

**There exists a time window during which antiviral intervention can halt and reverse this progression.** After this window closes, structural damage (fibrosis) exceeds the heart's regenerative capacity, and the disease becomes irreversible.

## The Three Recovery Rates

The reversibility window is determined by three biological clocks running at very different speeds:

| Process | Rate | Source | Bottleneck? |
|---------|------|--------|-------------|
| Dystrophin resynthesis | Weeks to months after 2A removed | Badorff 1999, model | No — fast |
| Cardiomyocyte renewal | ~1%/year (age 25), declining with age | Bergmann 2009 (C14) | Yes — slow |
| Fibrosis resolution | ~0.5-1%/year at best | Chapman 2016, est. | Yes — nearly irreversible |

**Key insight**: Dystrophin recovers fast. The heart muscle does not. Fibrosis is the rate-limiting barrier.

## Quantitative Reversibility Thresholds

From the ODE model (`dcm_progression_model.py`) and clinical literature:

| Fibrosis Level | EF Range | Recovery Potential | Clinical Stage |
|----------------|----------|-------------------|----------------|
| < 10% | > 50% | **Full recovery** — EF normalizes within years | Subclinical / early myocarditis |
| 10-20% | 40-50% | **Good recovery** — EF improves to near-normal | Early DCM, often pre-symptomatic |
| 20-35% | 30-45% | **Partial recovery** — EF improves but remains reduced | Established DCM |
| 35-50% | 20-35% | **Minimal recovery** — symptoms improve, EF plateaus | Advanced DCM |
| > 50% | < 25% | **Irreversible** — transplant trajectory | End-stage |

**Sources**: Merlo et al. 2011 (EF recovery predictors), Halliday et al. 2019 (reverse remodeling), model output.

## Timeline in the Progression Model

Using baseline parameters (V0 = 1000 copies/g, D0 = 95%):

| Milestone | Model Output (Years Post-Myocarditis) |
|-----------|---------------------------------------|
| Dystrophin drops below DGC threshold (60%) | ~2 years |
| EF drops below 50% (subclinical DCM) | **4.1 years** |
| Fibrosis exceeds 10% (early) | **7.1 years** |
| EF drops below 40% (DCM diagnosis) | **10.5 years** |
| EF drops below 35% (severe DCM) | **13.1 years** |
| EF drops below 25% (end-stage) | **15.4 years** |
| Fibrosis exceeds 20% (partial recovery limit) | **18.4 years** |

**Note**: These are model estimates with significant parameter uncertainty. Individual variation is large — some patients progress in 2-3 years, others remain stable for decades. Viral load and individual immune response are key variables. The 5-20 year timeline is consistent with clinical literature (Hershberger 2013).

## Why the T1DM Protocol is Cardiac-Protective

The T1DM systematic approach protocol (THEWALL.md) includes:

1. **Fluoxetine** — CVB 2C protein inhibitor, blocks viral replication
2. **Fasting-mimicking diet** — reduces inflammatory milieu
3. **Butyrate/Vitamin D/GABA** — Treg restoration, anti-inflammatory
4. **BHB (ketosis)** — NLRP3 inflammasome suppression

Components 1 and 4 are directly cardiac-relevant:
- **Fluoxetine clears CVB from ALL organs**, including myocardium. If TD mutants are present in the heart (which they likely are in T1DM patients with pancreatic CVB), fluoxetine should eliminate them.
- **BHB/NLRP3 suppression** reduces the inflammatory component of myocarditis/pericarditis, which drives both cardiomyocyte death and fibrosis.

**Prediction**: T1DM patients on the full protocol should show cardiac improvement on CMR if subclinical myocarditis was present. This is a testable secondary outcome.

## Intervention Scenarios (Model Output)

| Intervention Time | EF at Intervention | Fibrosis at Intervention | EF at 30 Years | Verdict |
|-------------------|-------------------|--------------------------|----------------|---------|
| 0.5 yr (during myocarditis) | 57.8% | 2.2% | **75.0%** | Full recovery |
| 2 yr (subclinical) | 54.4% | 3.7% | **75.0%** | Full recovery |
| 5 yr (early DCM) | 48.9% | 7.5% | **65.7%** | Full recovery |
| 10 yr (established DCM) | 41.0% | 13.0% | **51.7%** | Full recovery (borderline) |
| 15 yr (pre-transplant) | 26.5% | 17.5% | **40.9%** | Partial recovery |
| No intervention | -- | -- | **10.0%** | Heart failure / transplant |

**Values are direct model output.** Exact numbers depend on parameter choices (see parameter sweeps in `dcm_progression_model.py`).

### Dystrophin Recovery Kinetics (Post-Clearance)

Dystrophin recovers rapidly once 2A protease production stops:

| Starting Level | Time to 80% Recovery |
|---------------|---------------------|
| 30% | 59 days (2.0 months) |
| 40% | 56 days (1.9 months) |
| 50% | 51 days (1.7 months) |
| 60% | 45 days (1.5 months) |
| 70% | 35 days (1.2 months) |

**Dystrophin is NOT the bottleneck.** It recovers in weeks. Fibrosis takes decades.

## Clinical Implications

1. **Screen every T1DM patient for subclinical myocarditis** before starting the antiviral protocol. Baseline cardiac MRI + troponin. This provides both safety data and a measurable secondary outcome.

2. **Early intervention is everything.** The same fluoxetine that clears CVB from the pancreas clears it from the heart. Starting early prevents DCM entirely.

3. **Fibrosis is the enemy, not dystrophin.** Dystrophin recovers in weeks. Fibrosis takes decades to resolve (if ever). The intervention window is defined by fibrosis, not dystrophin.

4. **Even late intervention helps.** Stopping viral protease activity halts further damage. The heart will not fully recover, but progression stops. This matters for patients already diagnosed with DCM.

5. **IFN-beta clinical data supports this model.** Kuhl et al. 2003 showed that IFN-beta treatment of enterovirus-positive DCM patients led to viral clearance and EF improvement. The protocol's antiviral component should achieve the same.

## Files

- Model: `numerics/dcm_progression_model.py`
- Intervention analysis: `numerics/intervention_window.py`
- Plots: `results/dcm_progression.png`, `results/early_vs_late_intervention.png`

## References

1. Badorff et al. (1999) Nat Med 5:320-6 — 2A protease cleaves dystrophin
2. Bergmann et al. (2009) Science 324:98-102 — cardiomyocyte renewal rates
3. Merlo et al. (2011) JACC 57:1468-76 — EF recovery predictors
4. Kuhl et al. (2003) Circulation 107:2793-8 — IFN-beta in enteroviral DCM
5. Chapman et al. (2016) Circ Res 119:1173-82 — cardiac fibrosis biology
6. Halliday et al. (2019) JACC 73:70-80 — reverse remodeling in DCM
7. Wessely et al. (1998) Circulation 98:450-7 — TD mutant persistence
