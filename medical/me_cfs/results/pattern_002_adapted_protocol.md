# Pattern 002: ME/CFS-Adapted Treatment Protocol

## Status: IDENTIFIED — Numerics complete, not yet certified

## Why ME/CFS Needs Protocol Modifications

ME/CFS is not simply "CVB in another organ." It presents three challenges absent from single-organ CVB diseases like T1DM or myocarditis:

### 1. Multi-Reservoir Persistence
Unlike T1DM (pancreas only) or myocarditis (heart only), ME/CFS involves persistent CVB across 2-3 tissue compartments simultaneously: skeletal muscle (42% of ME/CFS patients positive), gut (82%), and CNS (30% estimated from neuroinflammation PET data). Clearing virus from one site allows reseeding from another. The CNS is a sanctuary site — the blood-brain barrier limits immune access to ~20% of systemic levels.

### 2. Bioenergetic Crisis
ME/CFS has a primary energy deficit that no other CVB disease has at the same scale. Mitochondrial Complex I activity is reduced 30-50% (Tomas 2017, Missailidis 2020). ATP production drops to 15-28 kg/day vs the normal 40 kg/day. This energy deficit:
- Prevents NK cell degranulation (ATP-dependent process)
- Prevents autophagy induction (mTOR/AMPK requires energy)
- Creates the hallmark symptom: post-exertional malaise (PEM)

### 3. Neuroinflammation
PET imaging shows widespread microglial activation in ME/CFS brains. This drives brain fog, cognitive dysfunction, and unrefreshing sleep. The T1DM protocol has no specific neuroinflammation component — the pancreas is not a neuroinflamed organ.

---

## The ME/CFS-Adapted Protocol

### Base Layer (from T1DM protocol — targets the virus)

| Component | Dose | Mechanism | ME/CFS Role |
|-----------|------|-----------|-------------|
| **Fluoxetine** | 20 mg/day | CVB 2C ATPase inhibitor | Antiviral across ALL reservoirs; crosses BBB (critical for CNS) |
| **Modified FMD** | 800 kcal/day x 3 days/month | Autophagy induction | Clears infected cells; MODIFIED (lower intensity than T1DM to avoid PEM) |
| **Butyrate** | 2 g/day | FOXP3 -> Treg expansion | Gut barrier repair + immune regulation |
| **Vitamin D** | 4000 IU/day | Innate immunity + Treg support | Deficiency correction (common in ME/CFS) |

Cost: ~$43/month

### ME/CFS-Specific Additions (address energy + neuroinflammation)

| Component | Dose | Mechanism | ME/CFS Role |
|-----------|------|-----------|-------------|
| **CoQ10** | 200-400 mg/day | Electron carrier: bypasses Complex I -> Complex III | Directly addresses the primary mito defect; RCT evidence (Castro-Marrero 2015) |
| **Low-Dose Naltrexone (LDN)** | 1.5-4.5 mg/day (titrate) | OGF pathway -> microglial M1-to-M2 shift | Neuroinflammation modulation; ME/CFS/fibromyalgia evidence (Brewer 2018) |
| **NMN (or NR)** | 500 mg/day | NAD+ precursor -> restores OXPHOS cofactor | Corrects NAD+ depletion from IDO2 metabolic trap (Germain 2022) |

Cost: ~$158/month (including base layer)

### Aggressive Mitochondrial Support (for severe patients)

| Component | Dose | Mechanism | ME/CFS Role |
|-----------|------|-----------|-------------|
| **PQQ** | 20 mg/day | PGC-1alpha activation -> mitochondrial biogenesis | New mitochondria replace damaged ones (weeks to months) |
| **D-Ribose** | 5g x 3/day | Direct ATP synthesis substrate | Immediate energy substrate; 61% improvement (Teitelbaum 2006) |
| **CoQ10 high-dose** | 400 mg/day (up from 200) | Higher electron carrier saturation | Dose-response in severe patients |

Cost: ~$233/month (all layers combined)

---

## Expected Recovery Timeline by Severity

Based on the coupled ODE model (6-variable: viral load, mitochondrial function, neuroinflammation, immune competence, energy envelope, T cell exhaustion):

### Mild ME/CFS (Bell Scale 50/100, housebound part-time)

| Milestone | Base T1DM | ME/CFS-adapted | Aggressive Mito |
|-----------|-----------|----------------|-----------------|
| +10% energy | ~6 months | ~5 months | ~4.4 months |
| Functional (70%) | ~10 months | ~7 months | ~6 months |
| Near-normal (85%) | >36 months | ~20 months | ~12 months |

### Moderate ME/CFS (Bell Scale 30/100, housebound)

| Milestone | Base T1DM | ME/CFS-adapted | Aggressive Mito |
|-----------|-----------|----------------|-----------------|
| +10% energy | ~4 months | ~3.6 months | ~3.3 months |
| Ambulatory (50%) | ~6 months | ~5 months | ~4.4 months |
| Functional (70%) | ~26 months | ~12 months | ~9 months |
| Near-normal (85%) | >36 months | >36 months | ~21 months |

### Severe ME/CFS (Bell Scale 15/100, mostly bedbound)

| Milestone | Base T1DM | ME/CFS-adapted | Aggressive Mito |
|-----------|-----------|----------------|-----------------|
| +10% energy | ~3.3 months | ~3.1 months | ~3.0 months |
| Ambulatory (50%) | ~11 months | ~8 months | ~7 months |
| Functional (70%) | >36 months | ~16 months | ~12 months |
| Near-normal (85%) | >36 months | >36 months | ~32 months |

**Key finding**: The base T1DM protocol alone never reaches functional threshold (70%) for moderate/severe patients within 3 years. The ME/CFS adaptations cut time-to-functional by 40-50%.

---

## ATP Recovery: Mitochondrial Support Makes the Difference

Starting from 40% mitochondrial function (moderate-severe baseline):

| Scenario | Time to 70% mito function |
|----------|---------------------------|
| No mito support (viral clearance only) | ~10 months |
| CoQ10 200mg only | ~7 months |
| CoQ10 + NMN | ~5 months |
| Full stack (CoQ10 + NMN + PQQ + D-ribose) | ~4 months |

The full mito stack reaches functional threshold **2.5x faster** than viral clearance alone. This is because CoQ10 directly bypasses the Complex I defect (immediate effect) while PQQ stimulates new mitochondrial biogenesis (sustained effect).

---

## LDN Neuroinflammation Model

Low-dose naltrexone acts via the Opioid Growth Factor (OGF) pathway:

1. Transient opioid receptor blockade (4-6 hours at bedtime)
2. Compensatory upregulation of endogenous opioids (endorphin rebound)
3. OGF (met-enkephalin) binds OGF receptor on microglia
4. Microglia shift from M1 (pro-inflammatory) to M2 (reparative)
5. Reduced TNF-alpha, IL-1beta, IL-6 in CNS

Model results at 12 months:
- No LDN: neuroinflammation reduced 30% (natural resolution)
- LDN 1.5mg: neuroinflammation reduced ~100%
- LDN 3.0mg: neuroinflammation reduced ~100%
- LDN 4.5mg: neuroinflammation reduced ~100%

**Note**: The model shows LDN is highly effective even at the low 1.5mg starting dose. Clinical recommendation: start at 1.5mg, titrate to 4.5mg over 2-4 weeks. The titration is for tolerability, not efficacy.

---

## Monitoring Adaptations for ME/CFS

ME/CFS requires different biomarkers than T1DM:

### Primary Biomarkers (Monthly)

| Biomarker | What It Tracks | Target |
|-----------|----------------|--------|
| Bell Disability Scale | Functional capacity (patient-reported) | Increasing score |
| VP1 antibody titer | CVB viral load (surrogate) | Declining |
| NK cell cytotoxicity (51Cr release) | Immune reconstitution | Increasing toward normal range |
| hsCRP | Systemic inflammation | <1.0 mg/L |

### Secondary Biomarkers (Quarterly)

| Biomarker | What It Tracks | Target |
|-----------|----------------|--------|
| Tryptophan / kynurenine ratio | IDO2 metabolic trap status | Normalizing |
| CoQ10 levels (plasma) | Supplement adequacy | >2.0 ug/mL |
| NAD+ levels (if available) | NMN supplement effect | Increasing |
| 2-day CPET | Objective exercise tolerance | Increasing VO2max, no day-2 drop |

### ME/CFS-Specific Assessments

| Assessment | Frequency | Purpose |
|------------|-----------|---------|
| Activity diary (steps/day) | Daily | Track PEM threshold expansion |
| Sleep quality (Pittsburgh Sleep Quality Index) | Monthly | Neuroinflammation response |
| Cognitive function (MoCA or similar) | Quarterly | Brain fog resolution |
| Orthostatic vitals (10-min stand test) | Monthly | Autonomic recovery |

### What NOT to Use from T1DM Monitoring
- HbA1c, C-peptide, insulin antibodies: not relevant (no pancreatic disease)
- Semaglutide monitoring: not applicable
- Teplizumab immune panels: not applicable

---

## PEM Management Strategy During Treatment

PEM (post-exertional malaise) is the most dangerous pitfall during ME/CFS treatment. Patients who feel improvement often overexert, crash, and lose weeks of progress.

### Phase 1: Strict Pacing (Months 0-3)
- **Rule**: Stay within 70% of current energy envelope. NEVER push to 100%.
- Activity tracking: steps/day, heart rate monitoring
- If PEM occurs: immediate rest, do NOT "push through"
- The FMD cycle itself is an exertion — use the modified 800 kcal version, not the full 500 kcal T1DM version
- PEM threshold at start: ~25% of normal (severe) to ~50% (mild)

### Phase 2: Gradual Expansion (Months 3-9)
- As mito support takes effect, the energy envelope grows
- Increase activity by no more than 10% per month
- Monitor for delayed PEM (can appear 24-72h after exertion)
- PEM threshold expanding: ~40-60% depending on severity and protocol

### Phase 3: Reconditioning (Months 9-18)
- If energy envelope exceeds 60%, begin gentle reconditioning
- Start with recumbent exercise (removes orthostatic challenge)
- 5-10 minutes, increasing by 2 minutes/week IF no PEM
- PEM threshold: ~60-80%

### Phase 4: Normalization (Months 18+)
- Progressive return to normal activity
- Exercise tolerance approaching normal
- PEM threshold: >80% (PEM becomes rare)

---

## Cost Comparison

| Protocol | Monthly | Annual | Cost per QALY gained (estimated) |
|----------|---------|--------|----------------------------------|
| Base T1DM only | $43 | $516 | Higher (slower recovery) |
| ME/CFS-adapted | $158 | $1,896 | Lower (faster to functional) |
| Aggressive mito | $233 | $2,796 | Lowest for severe patients |
| Current standard of care | $50-200 | $600-2,400 | Infinite (no recovery) |

**Context**: A moderate ME/CFS patient loses ~$30,000-60,000/year in lost income (inability to work). Even the aggressive protocol at $2,796/year is a 10-20x return if it restores work capacity.

All supplements are OTC except:
- Fluoxetine: generic prescription, $10/month
- LDN: compounding pharmacy prescription, ~$35/month

---

## Key Differences from Base T1DM Protocol

| Aspect | T1DM Protocol | ME/CFS-Adapted Protocol |
|--------|---------------|------------------------|
| **Primary target** | Beta cell preservation | Multi-site viral clearance + energy restoration |
| **FMD intensity** | 500 kcal x 5 days | 800 kcal x 3 days (reduced for PEM safety) |
| **Mito support** | Not needed | Essential: CoQ10 + NMN (+ PQQ, D-ribose for severe) |
| **Neuroinflammation** | Not addressed | LDN for microglial modulation |
| **GABA** | Included (alpha-to-beta conversion) | Optional (anxiolytic benefit, not primary) |
| **Semaglutide** | Included (beta cell preservation) | Excluded (weight loss worsens energy deficit) |
| **Teplizumab** | Included (anti-CD3 for autoimmunity) | Excluded (ME/CFS is not primarily autoimmune T cell-mediated) |
| **Monitoring focus** | HbA1c, C-peptide, GAD65 | Bell Scale, NK cytotoxicity, CPET, tryptophan |
| **Duration** | 6-12 months | 12-24+ months (multi-site clearance is slower) |
| **PEM risk** | None | Critical — must pace throughout treatment |
| **Cost** | ~$43-500/mo (varies by Rx) | ~$158-233/mo |

---

## Clinical Caveat

These are MODEL ESTIMATES based on:
- ODE system with 6 coupled variables
- Parameter values from published literature (see energy_metabolism_model.py and cvb_persistence_multisite.py references)
- Assumed CVB-positive ME/CFS subset (~30-42% of all ME/CFS patients)

**The protocol is NOT applicable to non-CVB ME/CFS patients.** Screening for CVB (VP1 antibody, enteroviral RNA PCR in stomach/muscle biopsy if available) is essential before starting the antiviral component.

For CVB-negative ME/CFS patients, the mitochondrial support + LDN components may still provide symptomatic benefit, but the antiviral component (fluoxetine) would have no target.

---

## Files

- Numerics: `numerics/treatment_protocol.py` (3-protocol comparison, LDN model, ATP recovery, severity sweep)
- Numerics: `numerics/energy_metabolism_model.py` (ATP deficit, IDO2 trap, NK function, PEM model)
- Numerics: `numerics/cvb_persistence_multisite.py` (multi-reservoir ODE, intervention modeling)
- Pattern 001: `results/pattern_001_energy_immune_coupling.md` (the energy-immune loop)
- This pattern: `results/pattern_002_adapted_protocol.md`

*Generated by ODD instance (numerics), systematic approach, 2026-04-08*
*Based on: treatment_protocol.py coupled ODE model (6 variables), 3 protocol scenarios, 3 severity levels*
