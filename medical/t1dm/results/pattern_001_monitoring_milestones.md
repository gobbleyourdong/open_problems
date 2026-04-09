# Pattern 001: Clinical Monitoring Milestones
## What to measure, when, and what the results mean

systematic approach -- ODD Instance (numerics) -- Clinical Bridge
Date: 2026-04-08

---

## Why This Document Exists

The computational models (CVB clearance, protocol optimization, propagation matrix) predict that the T1DM protocol should work. But predictions are not proof. This document defines how to MEASURE whether the protocol is working, in a real patient, with real blood tests, on a real timeline.

The audience is the patient and his physician. Every claim here maps to a specific lab test that can be ordered tomorrow.

---

## The Biomarkers and Why Each Matters

### PRIMARY ENDPOINT: C-Peptide

**What it is:** C-peptide is a byproduct of insulin production. For every molecule of insulin your pancreas makes, it makes one molecule of C-peptide. Measuring C-peptide tells you how much insulin YOUR beta cells are producing (vs. the insulin you inject).

**Why it matters:** This is THE metric. Everything else is supporting evidence. If C-peptide rises on the protocol, beta cells are regenerating. If it does not, the protocol is not working at the primary target.

**Two versions:**
- *Fasting C-peptide*: Simple blood draw after 12-hour fast. Less sensitive but convenient.
- *Stimulated C-peptide (MMTT)*: Drink a mixed meal (Boost), draw blood at 0, 30, 60, 90, 120 minutes. More sensitive. Shows how well beta cells respond to a glucose load. This is what clinical trials use.

**the patient context:** Diagnosed 12/2019 with C-peptide 0.9 ng/mL (~0.30 nmol/L). Achieved 5-year insulin independence on keto, suggesting significant residual beta cell mass. Current estimate: fasting C-peptide 0.15-0.25 nmol/L (needs measurement to confirm).

**Clinical thresholds (nmol/L):**
| Level | Meaning |
|-------|---------|
| <0.07 | No measurable beta cell function |
| 0.07-0.20 | Minimal residual function |
| >0.20 | Clinically meaningful (Palmer 2004) — associated with better glycemic control, fewer hypos |
| >0.40 | Moderate function — meaningful insulin reduction possible |
| >0.60 | Significant function — insulin independence may be achievable with low-carb diet |
| >1.00 | Near-normal — essentially in remission |

### HbA1c

**What it is:** Percentage of hemoglobin with glucose attached. Reflects average blood glucose over ~3 months.

**Why it matters:** Integrates all the glucose management — endogenous + exogenous insulin, diet, exercise, fasting. If HbA1c improves while insulin dose decreases, that means the body is doing more of the work.

**Target:** <6.5% on protocol (current estimate: 6.5-7.0%).

### Glucose Variability (CGM)

**What it is:** Coefficient of variation (CV) calculated from continuous glucose monitor data. Measures how much glucose bounces around.

**Why it matters:** Beta cells provide BASAL insulin — the constant trickle that keeps glucose steady between meals. If beta cells are regenerating, the first thing you should see is smoother glucose traces (lower CV), even before total insulin dose drops.

**Target:** CV <36% (current estimate: ~42%).

**Cost:** Free if already wearing a CGM. This is the earliest, cheapest signal.

### Autoantibodies (GAD65, IA-2, ZnT8)

**What they are:** Antibodies your immune system makes against your own pancreatic proteins. Their presence confirms autoimmune T1DM. Their levels reflect ongoing immune attack intensity.

**Why they matter:** If the protocol is restoring immune tolerance (via Tregs, butyrate, vitamin D), autoantibody titers should decline over 6-24 months. This is SLOW — do not expect rapid changes.

**GAD65** is the most persistent and most informative. IA-2 and ZnT8 are supporting evidence.

### hs-CRP (high-sensitivity C-reactive protein)

**What it is:** A protein the liver makes in response to inflammation anywhere in the body.

**Why it matters:** The protocol targets multiple inflammatory pathways (NLRP3 via BHB, NF-kB via butyrate, chronic viral stimulation via fluoxetine). If inflammation is decreasing, hs-CRP should decline. This is the FASTEST marker to respond — expect changes within 1-3 months.

**Normal:** <1.0 mg/L. T1DM patients often 1-3 mg/L. **If >10:** investigate acute infection (not protocol-related).

### Regulatory T Cells (Tregs)

**What they are:** CD4+CD25+FoxP3+ T cells — the immune system's brakes. They suppress autoimmune attack.

**Why they matter:** T1DM patients have reduced Treg function. Butyrate and vitamin D both promote Treg differentiation. Rising Treg percentage confirms the immune retraining arm of the protocol is working.

**Normal:** 5-10% of CD4+ cells. T1DM: often 3-5%.

**Limitation:** Requires flow cytometry at a specialized lab. Expensive ($200). Fresh blood only — cannot ship.

### 25-OH Vitamin D

**What it is:** The circulating form of vitamin D. Reflects supplementation and sun exposure.

**Why it matters:** Vitamin D is both a compliance marker (is the patient taking supplements?) and a functional immune modulator. Target 50-70 ng/mL for immune optimization.

**Safety:** >100 ng/mL risks hypercalcemia. If levels are high, check serum calcium.

### Enterovirus PCR (stool)

**What it is:** RT-PCR for enteroviral RNA in stool samples.

**Why it matters:** The DiViD study found enteroviral protein in 6/6 T1DM islets. Stool PCR is a non-invasive proxy for persistent CVB infection. If fluoxetine + autophagy is clearing the virus, stool PCR should become negative.

**Limitation:** Research-grade test. Not available at LabCorp/Quest. Requires academic virology lab.

### Cardiac Safety: Troponin I and NT-proBNP

**Why monitor:** Coxsackievirus B also targets the heart. Persistent CVB can cause myocarditis or cardiomyopathy. The protocol mobilizes viral clearance, which could theoretically cause transient cardiac inflammation. Monitoring troponin provides an early warning.

- **Troponin I >14 ng/L:** Active myocardial injury. STOP protocol. Cardiology consult IMMEDIATELY.
- **NT-proBNP >300 pg/mL (age >65):** Suggests heart failure. Cardiology referral.

### Hepatic Safety: ALT/AST

**Why monitor:** Fluoxetine, though generally safe, has rare hepatotoxic potential (<1%). ALT is the screening test.

- **ALT >80 U/L (2x ULN):** Recheck in 2 weeks.
- **ALT >120 U/L (3x ULN):** Reduce fluoxetine to 10mg or discontinue.
- **ALT >3x ULN + bilirubin >2x ULN (Hy's Law):** STOP fluoxetine. This combination predicts severe drug-induced liver injury.

---

## The Monitoring Schedule

### Full Schedule (all tiers)

| Test | M0 | M1 | M3 | M6 | M9 | M12 | M18 | M24 | Cost/test |
|------|:--:|:--:|:--:|:--:|:--:|:---:|:---:|:---:|----------:|
| **Tier 1: Must Have** | | | | | | | | | |
| Fasting C-Peptide | X | | X | X | X | X | X | X | $45 |
| Stimulated C-Peptide (MMTT) | X | | | X | | X | | X | $150 |
| HbA1c | X | | X | X | X | X | X | X | $20 |
| hs-CRP | X | X | X | X | | X | | X | $25 |
| 25-OH Vitamin D | X | X | X | X | | X | | X | $40 |
| ALT | X | X | X | X | | X | X | X | $15 |
| AST | X | X | X | X | | X | X | X | $15 |
| Troponin I (hs) | X | | | X | | X | | X | $30 |
| **Tier 2: Important** | | | | | | | | | |
| GAD65 Antibodies | X | | | X | | X | | X | $85 |
| IA-2 Antibodies | X | | | | | X | | X | $85 |
| Fasting Insulin | X | | | X | | X | | X | $30 |
| NT-proBNP | X | | | | | X | | X | $40 |
| Tregs (flow cytometry) | X | | | X | | X | | | $200 |
| Lipid Panel | X | | | | | X | | X | $35 |
| TSH | X | | | | | X | | X | $25 |
| CGM Glucose CV | X | X | X | X | X | X | X | X | $0 |
| **Tier 3: Nice to Have** | | | | | | | | | |
| ZnT8 Antibodies | X | | | | | X | | X | $85 |
| IAA | X | | | | | | | X | $60 |
| Enterovirus PCR (stool) | X | | | X | | X | | X | $150 |
| Serum IFN-alpha | X | | | | | X | | | $75 |
| Anti-CVB Neutralizing Ab | X | | | | | X | | | $200 |
| NK Cytotoxicity | X | | | | | X | | | $250 |
| Lactate:Pyruvate | X | | | | | X | | | $80 |
| Proinsulin:C-Peptide | X | | | | | X | | | $100 |
| Zonulin | X | | | | | X | | | $90 |
| Echocardiogram | X | | | | | X | | | $300 |
| Microbiome 16S | X | | | | | X | | | $150 |
| D-Lactate | X | | | | | X | | | $75 |

### Cost Summary (24 months)

| Tier | 24-Month Total |
|------|----------------|
| Tier 1 only | ~$2,500 |
| Tier 1 + 2 | ~$4,500 |
| All tiers | ~$8,500 |
| Minimum set | ~$425 |

---

## Decision Tree by Time Point

### MONTH 0: Baseline

**Goal:** Establish all baseline values before starting any protocol interventions.

**Actions:**
- Order all Tier 1 tests, as many Tier 2 as feasible
- Start protocol AFTER results are back
- If fasting C-peptide >0.30 nmol/L: excellent starting position, high probability of response
- If fasting C-peptide 0.10-0.30 nmol/L: expected range for the patient, proceed with standard protocol
- If fasting C-peptide <0.10 nmol/L: minimal residual function, add semaglutide from day 1

### MONTH 1: Safety Check

**Goal:** Confirm fluoxetine is safe, vitamin D is absorbing.

**Key tests:** ALT, AST, vitamin D, hs-CRP, CGM data.

**Decision tree:**
- ALT normal (<40 U/L): Continue protocol as-is
- ALT elevated (40-80 U/L): Recheck in 2 weeks
- ALT >80 U/L: Reduce fluoxetine to 10mg, recheck in 2 weeks
- ALT >120 U/L: Stop fluoxetine, evaluate
- Vitamin D <30 ng/mL: Increase dose or investigate absorption
- Vitamin D >80 ng/mL: Check calcium, consider dose reduction
- hs-CRP declining from baseline: Anti-inflammatory arm responding (earliest positive signal)

### MONTH 3: First Efficacy Signal

**Goal:** First look at whether the protocol is affecting disease markers.

**Key tests:** Fasting C-peptide, HbA1c, hs-CRP, vitamin D, ALT, CGM CV.

**Early success indicators:**
1. hs-CRP declined >30% from baseline (inflammation reducing)
2. CGM glucose CV declined (smoother traces, even if total insulin unchanged)
3. C-peptide stable or rising (not declining further)
4. Vitamin D 50-70 ng/mL (compliance confirmed)
5. ALT normal (fluoxetine safe)
6. Subjective: better energy, better sleep, more stable glucose

**Decision tree:**
- All 6 indicators positive: Protocol on track. Continue, recheck at month 6.
- 3-5 indicators positive: Promising. Continue.
- C-peptide declining: ADD semaglutide if not already on it. Consider increasing FMD frequency.
- hs-CRP unchanged or rising: Anti-inflammatory arm underperforming. Check butyrate dose, vitamin D level.

### MONTH 6: Key Decision Point

**Goal:** Determine whether C-peptide is rising (the primary signal).

**Key tests:** Fasting C-peptide, stimulated C-peptide (MMTT), HbA1c, GAD65, troponin, all safety markers.

**Decision tree:**

```
C-peptide at Month 6
        |
   ┌────┴────┐
  Rising    Flat or Declining
   |              |
   |         ┌────┴────┐
   |      Flat (no     Declining
   |      change)     (worse)
   |         |           |
Continue   Escalate:    MAJOR
protocol   - Add        ESCALATION:
           semaglutide  - Teplizumab
           - Increase     referral
           FMD to       - Add
           biweekly       semaglutide
           - Recheck    - Consider
           month 9        if protocol
                          is wrong
```

**If C-peptide rising + GAD65 declining:** Strong evidence of both beta cell regeneration AND immune tolerance improvement. This is the best possible scenario at 6 months. Continue and document thoroughly.

**If C-peptide rising + GAD65 unchanged:** Beta cells regenerating but immune attack unchanged. The regeneration is outpacing destruction. This may not be durable — immune modulation needs strengthening (increase butyrate, consider teplizumab as insurance).

**Cardiac safety check:** Troponin at month 6. If any elevation, STOP and evaluate. If normal, continue.

### MONTH 9: Interim Check

**Goal:** Track trajectory before primary endpoint at month 12.

**Key tests:** Fasting C-peptide, HbA1c, CGM CV.

**If trajectory positive:** Continue to month 12 without changes.
**If trajectory flat after month 6 escalation:** Teplizumab referral becomes urgent.

### MONTH 12: Primary Endpoint

**Goal:** Determine whether the protocol has achieved its primary objective.

**Key tests:** ALL Tier 1, all Tier 2, as many Tier 3 as feasible. This is the comprehensive reassessment.

**Definitive success criteria (must meet ALL of these):**
1. Stimulated C-peptide >0.60 nmol/L (clinically meaningful beta cell function)
2. HbA1c <6.5% on same or less insulin than baseline
3. Daily insulin dose reduced by at least 30% from baseline
4. No safety signals triggered during 12 months
5. GAD65 declined from baseline (any decline)

**Strong success (the dream scenario):**
- Stimulated C-peptide >1.0 nmol/L
- Insulin dose reduced >50%
- GAD65 declined >50%
- hs-CRP <1.0 mg/L
- Glucose CV <30%

**Partial success (protocol is helping but not curative alone):**
- Stimulated C-peptide 0.20-0.60 nmol/L
- Insulin dose reduced 10-30%
- Some biomarker improvement but not all
- Action: Continue protocol, consider adding teplizumab

**Protocol not working at primary target:**
- C-peptide unchanged or declined from baseline
- No insulin dose reduction
- Action: Full reassessment. Consider: (a) the model is wrong for this patient, (b) the protocol is not reaching the target, (c) the damage is too far progressed

### MONTH 18: Durability

**Goal:** Confirm gains are sustained and not transient.

**Key tests:** Fasting C-peptide, HbA1c, ALT, insulin dose log.

**If month 12 was successful:**
- Continue protocol
- If C-peptide still rising: begin cautious insulin taper under endocrinology supervision
- If C-peptide plateaued: this may be the maximum response. Maintain.

### MONTH 24: Final Assessment

**Goal:** Definitive 2-year outcome. Full comprehensive panel.

**Key tests:** Everything from month 0 (full repeat for comparison).

**Outcome categories:**
1. **Remission:** C-peptide >0.60 nmol/L, insulin-free or near-free, HbA1c <6.0%. Publish.
2. **Significant improvement:** C-peptide 0.30-0.60 nmol/L, insulin reduced >50%. Continue protocol.
3. **Moderate improvement:** C-peptide 0.20-0.30 nmol/L, insulin reduced 20-50%. Continue, consider escalation.
4. **Minimal/no response:** C-peptide <0.20 nmol/L. Document, analyze, share data for others.

---

## Safety Abort Criteria

### STOP the protocol IMMEDIATELY if:

1. **Troponin I >14 ng/L** at any visit
   - Indicates active myocardial injury
   - Action: Stop all protocol interventions. Emergency cardiology evaluation.
   - Resume only after cardiac clearance with modified protocol (no fasting, monitor closely)

2. **ALT >3x ULN (>120 U/L) AND bilirubin >2x ULN** (Hy's Law)
   - Indicates serious drug-induced liver injury
   - Action: Stop fluoxetine permanently. Do NOT rechallenge.
   - Can continue non-fluoxetine components of protocol

3. **NT-proBNP >900 pg/mL**
   - Indicates likely symptomatic heart failure
   - Action: Urgent cardiac evaluation. Stop fasting components.

4. **Blood ketones >3.0 mmol/L with blood glucose >250 mg/dL**
   - Indicates diabetic ketoacidosis (DKA)
   - Action: Eat carbs, take insulin, go to ER. This is an emergency.
   - FMD cycling must be done with CGM and ketone monitoring

5. **New cardiac symptoms** (chest pain, dyspnea, palpitations, syncope)
   - Action: Stop protocol, urgent cardiac workup

6. **Severe hypoglycemia** (<54 mg/dL with impaired consciousness)
   - Action: Standard hypo treatment. Reduce insulin dose. Reassess fasting protocol.

### REDUCE but don't stop if:

- ALT 80-120 U/L (2-3x ULN): Reduce fluoxetine to 10mg. Recheck in 2 weeks.
- hs-CRP >10 mg/L: Investigate infection source (likely not protocol-related). Can continue protocol while investigating.
- NT-proBNP 300-900 pg/mL: Cardiology referral. Can continue protocol cautiously pending evaluation.

---

## The Minimum Monitoring Set

### For patients who cannot afford comprehensive testing:

**ABSOLUTE MINIMUM ($425 over 24 months):**

| # | Test | When | Cost | Why |
|---|------|------|------|-----|
| 1 | Fasting C-Peptide | M0, M6, M12 | $135 | The primary endpoint |
| 2 | HbA1c | M0, M6, M12 | $60 | Glycemic control |
| 3 | ALT | M0, M1, M3, M6, M12 | $75 | Fluoxetine safety |
| 4 | 25-OH Vitamin D | M0, M3 | $80 | Compliance |
| 5 | hs-CRP | M0, M3 | $50 | Inflammation baseline |
| 6 | CGM glucose CV | Every visit | $0 | From existing CGM |
| 7 | Insulin dose log | Daily | $0 | THE functional metric |

**THE FREE METRICS (everyone should track these):**

1. **Daily insulin dose** — THE most important functional metric. Costs nothing. If this is trending down while glucose control is maintained, the protocol is working regardless of what the lab tests show.

2. **CGM data** — Time-in-range, glucose CV, hypo frequency. Already being collected if wearing a CGM.

3. **Subjective log** — Energy (1-10), sleep quality (1-10), mood, digestive symptoms. Daily, 30 seconds.

4. **Weight** — Weekly. FMD causes temporary weight loss; long-term trend matters.

**THE CHEAPEST SIGNAL THAT THE PROTOCOL IS WORKING:**
> If insulin dose is trending DOWN while HbA1c is stable or improving, beta cells are picking up more of the load. This costs $0 to measure.

---

## Early Success Indicators (What to Look for at Month 3)

If you see ANY of these at month 3, the protocol is affecting the disease:

1. **hs-CRP dropped >30%** — inflammation resolving (earliest lab signal)
2. **CGM glucose CV decreased** — smoother traces = beta cells providing basal insulin
3. **Insulin dose reduced even slightly** — functional evidence of beta cell recovery
4. **Energy/mood improved** — subjective but meaningful; correlates with reduced inflammation
5. **Vitamin D in target range** — confirms compliance and absorption
6. **ALT normal** — fluoxetine is safe in this patient

None of these alone proves the protocol works. But 3+ out of 6 at month 3 is a very encouraging signal. The definitive proof comes from C-peptide at month 6-12.

---

## What Definitive Success Looks Like at Month 12

The protocol is PROVEN to work if, at month 12:

1. Stimulated C-peptide >0.60 nmol/L (up from baseline of ~0.50)
2. Fasting C-peptide >0.25 nmol/L (up from baseline of ~0.20)
3. Daily insulin reduced from 6u/day (2u x 3 meals) to <4u/day
4. HbA1c <6.5% on reduced insulin
5. No safety signals in 12 months
6. GAD65 declined from baseline

If all 6 criteria are met, this is publishable evidence that the protocol reverses T1DM progression. It does not prove the mechanism (that requires the computational models + additional testing), but it proves the clinical effect.

---

## Generating the Figures and Data

The companion scripts generate everything needed for clinical use:

```bash
# Generate biomarker trajectory plots and JSON data
python3 /home/jb/medical_problems/numerics/biomarker_trajectories.py

# Generate monitoring schedule (printable table + JSON)
python3 /home/jb/medical_problems/numerics/monitoring_schedule.py
```

Output locations:
- Trajectory plots: `/home/jb/medical_problems/results/figures/`
- Biomarker data (JSON): `/home/jb/medical_problems/results/biomarker_trajectories.json`
- Schedule data (JSON): `/home/jb/medical_problems/results/monitoring_schedule.json`
- Printable schedule: `/home/jb/medical_problems/results/monitoring_schedule.txt`

---

*Generated by numerical track (numerics), systematic approach, 2026-04-08*
*Based on: THEWALL.md unified model, patient_zero_protocol.py, patient_zero_lab_order.py*
*Literature: Palmer 2004, Lachin 2011, Herold 2019, Butler 2005, Cheng 2017, ADA Standards 2024*
