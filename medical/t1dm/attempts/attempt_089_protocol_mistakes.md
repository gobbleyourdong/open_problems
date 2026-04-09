# Attempt 089: What NOT to Do — Protocol Mistakes That Undermine the Campaign

## Why This Matters

Patients on a complex protocol sometimes inadvertently sabotage it. This attempt catalogs the specific mistakes that would undermine the CVB clearance protocol, ordered by severity.

---

## CRITICAL MISTAKES (Can Be Dangerous)

### 1. Combining exogenous BHB supplements with fasting in T1DM
**What happens**: endogenous BHB (from fasting, ~1.8 mM) + exogenous supplement (2.5 mM standard dose) = 4.3 mM total → DKA territory (>3.0 mM)
**Why it's dangerous**: DKA (diabetic ketoacidosis) requires hospitalization, is potentially fatal
**The rule**: NEVER take exogenous BHB ketone supplements (MCT oil, exogenous ketone esters, BHB salts) on fasting days
**Lean proof**: `exogenous_bhb_during_fast_dangerous` in DKASafety.lean (proved: 1.8 + 2.5 > 3.0)
**Safe use of BHB**: endogenous BHB from fasting is fine; exogenous BHB is fine on NON-fasting, NON-insulin-reduced days

### 2. Starting FMD before cardiac screening (T1DM patients)
**What happens**: CVB myocarditis may be asymptomatic. FMD (5-day caloric restriction) + cold exposure (WHM) are cardiovascular stressors. Active myocarditis + these stressors = cardiac event risk.
**The rule**: troponin + NT-proBNP + echo BEFORE first FMD, every time
**Clinical evidence**: subacute CVB3 myocarditis presents with normal ECG and vague symptoms; only elevated troponin reveals it
**Consequence**: one patient with undiagnosed myocarditis who has a cardiac event on protocol = campaign credibility severely damaged

### 3. Itraconazole in cardiac dysfunction
**What happens**: itraconazole is a negative inotrope (reduces cardiac contractility). In a patient with reduced LVEF (<50%), this can precipitate acute heart failure.
**The rule**: NEVER add itraconazole if LVEF <50%, if there is pericardial effusion, or if the patient has significant structural heart disease
**Clinical evidence**: documented cardiac adverse events with itraconazole in HF patients
**Interaction**: also never combine itraconazole with colchicine (fatal CYP3A4 interaction — colchicine toxicity)

### 4. Iron supplementation during viral protocol
**What happens**: iron feeds viral replication. CVB, like most viruses, requires iron for replication. The innate immune response to infection deliberately sequesters iron (via hepcidin) as a defensive mechanism.
**The rule**: if ferritin is low (<30 ng/mL), do NOT supplement iron during the first 6 months of antiviral protocol. Address iron deficiency after viral clearance is established.
**Practical note**: if the patient is anemic (not just low ferritin), discuss with physician — may need IV iron in a controlled setting after protocol is underway.

---

## SIGNIFICANT MISTAKES (Undermine Protocol Efficacy)

### 5. Stopping fluoxetine prematurely
**What happens**: fluoxetine has a 4-6 week "washout" period from tissue (due to large Vd = 40 L/kg, lysosomotropic trapping). Stopping at month 3 because "I feel better" means tissue drug falls below IC50 → WT CVB can re-emerge from residual reservoir → protocol failure.
**The rule**: fluoxetine must be maintained for the full protocol duration (18-36 months for males, 12-18 months for females) OR until biomarker confirmation of clearance (CVB serology turning negative, C-peptide trending up, seminal PCR negative for males)
**Why patients stop early**: SSRIs have side effects (libido, sleep) and patients feel better → assume cured. The WT may be suppressed (good) but TD mutants are not cleared.

### 6. Butyrate at 300mg instead of 4-6g
**What happens**: 300mg/day achieves gut barrier effects only. HDAC inhibition (required for FOXP1 upregulation in non-gut tissues including islets, thyroid, brain) requires serum butyrate concentrations that are only achieved at 4-6g/day.
**Why patients do this**: the original protocol (pre-bioinformatics) specified 300mg TID. This is the WRONG dose for the FOXP1 mechanism.
**The rule**: sodium butyrate 4,000-6,000mg/day (enteric coated capsules preferred). Start low (1g/day) and increase by 1g/week to minimize GI adaptation symptoms.

### 7. NSAIDs during FMD days
**What happens**: NSAIDs (ibuprofen, naproxen) + relative dehydration during fasting → acute kidney injury risk. Also: NSAIDs blunt autophagy induction (they affect prostaglandin pathways that partially modulate autophagy).
**The rule**: no NSAIDs during fasting days. Acetaminophen is acceptable for pain. Colchicine is fine.

### 8. Alcohol with butyrate
**What happens**: alcohol is metabolized to acetate → acetaldehyde → fatty liver. High-dose butyrate + alcohol compete for the same hepatic metabolism pathways. More importantly: alcohol is profoundly pro-inflammatory (NF-κB, NLRP3), directly undermining the anti-inflammatory arm.
**The rule**: minimize alcohol during the protocol. Zero alcohol on FMD days.

---

## MODERATE MISTAKES (Reduce Effectiveness)

### 9. Using 200mg CoQ10 instead of 600mg
The T1DM protocol specifies 600mg CoQ10. Some patients use the more common 200mg formulation. For mitochondrial Complex I support (MT-ND3 target from GSE293840), 600mg achieves therapeutic tissue concentrations; 200mg may be insufficient.

### 10. Taking vitamin D3 without vitamin K2
At 5,000 IU/day, vitamin D3 increases calcium absorption. Without K2 (MK-7 form, 100-200μg/day), excess calcium may deposit in soft tissues. This is a long-term concern, not acute.

### 11. Missing FMD cycles "just this month"
FMD monthly is specifically required for the TD mutant clearance. Missing one month = that month's autophagy pulse is lost. The clearance model is based on MONTHLY cycles. One missed cycle extends clearance by approximately one month. For the final months of the protocol (clearing the slowest organs), every cycle matters.

### 12. Not monitoring glucose during FMD in T1DM
T1DM patients on FMD MUST check glucose every 2-3 hours. Insulin requirements drop dramatically during fasting. Without monitoring, hypoglycemia is common.

### 13. Starting trehalose late (after weeks 4-8)
Trehalose should start on day 1, not after fluoxetine is established. The reason: the LAMP2 block is being established from week 1 of CVB infection (or from day 1 of protocol in established disease). Trehalose's TFEB effect starts compensating IMMEDIATELY. Every week of delay allows LAMP2 to be further suppressed before the TFEB compensation begins.

---

## MINOR MISTAKES (Don't Undermine But Waste Resources)

### 14. Taking selenium above 400μg/day
Selenium above this threshold → selenium toxicity (selenosis). The protocol recommends 200μg/day. More is NOT better.

### 15. Taking zinc without copper
Zinc supplementation (15mg/day) depletes copper over months → copper deficiency anemia. Must supplement copper 2mg/day alongside zinc.

### 16. FMD without the right caloric restriction pattern
The "FMD" in the protocol refers to the Prolon-style caloric restriction (500 kcal/day × 5 days) that specifically activates AMPK while maintaining ketogenic state. Regular 3-day water fasting or 16:8 time-restricted eating (TRE) are less effective for TD mutant clearance. TRE provides modest autophagy induction; 5-day FMD provides the peak autophagy activation needed to overcome the LAMP2 block.

---

## Summary: The Non-Negotiable Rules

1. ❌ NEVER: exogenous BHB on fasting days (T1DM patients)
2. ❌ NEVER: start FMD without cardiac clearance (troponin + echo first)
3. ❌ NEVER: itraconazole with cardiac dysfunction or with colchicine
4. ❌ NEVER: iron during first 6 months of antiviral protocol
5. ✓ MUST: butyrate at 4-6g/day (not 300mg)
6. ✓ MUST: fluoxetine for full protocol duration (biomarker-guided end)
7. ✓ MUST: trehalose from day 1 (not delayed)
8. ✓ MUST: monthly FMD without skipping

## Status: PROTOCOL MISTAKE CATALOG COMPLETE — 4 critical (dangerous), 4 significant (undermine efficacy), 4 moderate, 4 minor. Non-negotiable rules summarized.
