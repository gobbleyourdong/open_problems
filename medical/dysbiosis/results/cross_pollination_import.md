# Cross-Pollination Import — From CVB Campaign to Dysbiosis Framework
## 2026-04-12

> The broader CVB disease campaign (../t1dm, ../myocarditis, ../me_cfs, 94+ attempts)
> has developed a core protocol and safety matrix that the dysbiosis framework was
> built without access to. This document imports the critical gaps.
>
> Source: ../CONVERGENCE.md (core protocol), ../DRUG_SAFETY_MATRIX.md (safety),
> ../CROSS_POLLINATION.md (inter-disease findings)

---

## CRITICAL SAFETY UPDATE — READ FIRST

### Itraconazole + Colchicine: DOCUMENTED FATALITIES

From DRUG_SAFETY_MATRIX.md:

```
⚠️ DANGER COMBINATION ⚠️

Itraconazole is a POTENT CYP3A4 inhibitor
Colchicine is a CYP3A4 SUBSTRATE

Itraconazole → blocks colchicine metabolism → colchicine levels rise 2-3x
Colchicine has a NARROW therapeutic index
→ Bone marrow suppression, rhabdomyolysis, multi-organ failure, DEATH

DOCUMENTED FATALITIES exist in the literature.

RULE: NEVER use itraconazole + colchicine together at full doses.
```

**This was NOT in the dysbiosis protocol. Adding itraconazole to any colchicine-based protocol is potentially lethal.**

Options if both are considered:
- Use fluoxetine as sole CVB antiviral (preferred — see below) + keep colchicine if using it
- Use itraconazole as sole antiviral + eliminate colchicine entirely (use BHB for NLRP3 instead)
- NEVER both at standard doses

### Itraconazole Contraindicated in Heart Failure

From DRUG_SAFETY_MATRIX.md:

```
Itraconazole | Heart: negative inotrope, CI in HF
```

T1DM can progress to dilated cardiomyopathy (DCM) via CVB cardiac involvement (../dilated_cardiomyopathy). DCM is listed as a CVB disease in the campaign. If any cardiac symptoms or ejection fraction questions exist, itraconazole is contraindicated.

**Any patient considering itraconazole should have a baseline echocardiogram to rule out HF before initiating.**

---

## Protocol Gap 1: Fluoxetine — Primary CVB Antiviral MISSING

**What the broader campaign says:**
Fluoxetine 20-60mg is the PRIMARY antiviral in the 12-disease CVB campaign. It is the first-line and most evidence-based CVB antiviral in the current framework.

**Mechanism:** CVB 2C ATPase inhibitor. The 2C protein is a viral helicase/ATPase required for CVB replication and RNA packaging. Fluoxetine disrupts this → prevents new CVB assembly.

**Evidence grade:** II-2 to II-3 (cell culture confirmed; retrospective human data for pericarditis recurrence reduction; no prospective T1DM-specific trial)

**Dosing:**
- Standard: 20mg QD (antidepressant dose; also effective for CVB)
- For males: 60mg QD (higher mass-based dosing; T1DM attempts recommend 60mg for males)
- CYP2D6 metabolism; interacts with serotonin-active drugs (serotonin syndrome with MAOIs)
- QTc prolongation with other QT-prolonging drugs (monitor baseline ECG)

**What was in the dysbiosis protocol:**
Itraconazole (OSBP inhibitor) was listed as the primary pharmacological antiviral option.
Fluoxetine was COMPLETELY ABSENT.

**Correction:**
Fluoxetine should be FIRST-CHOICE pharmacological antiviral before itraconazole, for three reasons:
1. Better evidence base (2C ATPase mechanism is more studied than OSBP for CVB)
2. No cardiac contraindication (unlike itraconazole)
3. No colchicine death risk (unlike itraconazole)
4. Lower cost (~$4-8/month generic vs $50+/month itraconazole)
5. Already commonly prescribed → easier to discuss with physician

**If fluoxetine is already being taken for depression at 20mg:** this provides DUAL benefit (antidepressant + CVB antiviral). No adjustment needed; HPA axis benefits (reduces cortisol-mediated immune dysregulation) are additional.

---

## Protocol Gap 2: Butyrate Dose — 600mg → 4-6g/day

**Current dysbiosis protocol:** Butyrate (sodium butyrate or tributyrin): 600mg/day

**What the broader campaign says:**
```
Butyrate increased 300mg → 4–6g/day:
FOXP1 mechanism (−67x in persistent infection) requires HDAC-level dose
for tissue-local Treg restoration.
```

**Why this matters for the dysbiosis framework:**
The entire M1↔M4 bridge (GALT Th17 → skin Treg depletion) and the M6↔M4 structural floor both depend on butyrate-mediated HDAC inhibition for Foxp3 CNS1/CNS3 acetylation. The dose-response matters.

**What 600mg achieves:** mild gut barrier support (enterocyte fuel), some commensal selection pressure
**What 4-6g achieves:** HDAC inhibition at CNS1/CNS3 → pTreg differentiation → Foxp3+ Treg induction

The 600mg dose is the typical commercial supplement dose. The 4-6g dose is the research-backed HDAC-effective dose. For the Treg induction mechanism specifically, 600mg is likely sub-therapeutic.

**Practical note:**
- Enteric-coated sodium butyrate 4-6g/day can cause significant GI gas/bloating initially
- Tributyrin (precursor, less odor) is better tolerated; dose equivalence ~5-7g tributyrin = 4g sodium butyrate
- Start at 600mg, titrate up over 4-6 weeks to minimize GI side effects
- Alternatively: very high-fiber diet (≥40g/day, diverse sources) + LGG probiotic produces endogenous butyrate approaching this range via fermentation

---

## Protocol Gap 3: Trehalose 2g/day — TFEB/LAMP2 Mechanism

**What the broader campaign says:**
Trehalose 2g/day — TFEB → lysosomal biogenesis → LAMP2 bypass.
"Critical for low-LAMP2 organs: CNS, testes, muscle."

**Mechanism:**
CVB persistent infection → LAMP2 downregulation → impaired lysosomal-mediated autophagy → virus persists in autophagic vacuoles → cannot be cleared.
Trehalose → activates TFEB (transcription factor EB) → upregulates lysosomal biogenesis including LAMP2 → restores autophagic flux → allows CVB clearance.

**Confirmed:** CVB-infected human cells (GSE184831 bioinformatics): LAMP2 knockdown confirmed as persistence mechanism.

**Relevance to dysbiosis:**
T1DM beta cells (islets) are a relevant tissue. If LAMP2 is depleted in beta cells by persistent CVB, the antiviral protocol's autophagy arm (IF, BHB, fasting) is working through a partially blocked pathway. Trehalose restores the pathway.

**The dysbiosis protocol does NOT mention trehalose.**

**Should it be added?**
Yes, for T1DM patients on the antiviral arm:
- Cost: ~$15/month (food-grade trehalose; available online)
- Safety: very safe; metabolized as glucose (2g/day = minimal glycemic effect)
- T1DM consideration: 2g trehalose = modest glucose load; incorporate into carbohydrate counting or take with protein/fat to blunt spike
- Timing: morning dose with breakfast; TFEB effect is not timing-critical

---

## Protocol Gap 4: FMD (Fasting-Mimicking Diet) vs. Simple IF

**Current dysbiosis protocol:** "Autophagy support: BHB elevation (intermittent fasting) → NLRP3 suppression"

**What the broader campaign says:**
FMD (fasting-mimicking diet, 5-day/month) — autophagy for TD (truncation-defective) mutant clearance.

**Why FMD is distinct from simple IF:**
- 16:8 IF produces mild autophagy primarily in metabolically active tissues
- FMD (5-day/month, ~800 cal/day of specific macro ratio: high fat, low protein, low carb) produces deep autophagy sufficient to clear persistent viral reservoirs
- Prolon protocol (Longo lab) is the evidence-based version; home-made approximation is lower cost
- For CVB clearance specifically: the viral reservoir in islets requires deeper autophagy than daily IF provides

**Recommendation:**
Add FMD (5-day/month) to the antiviral protocol arm for T1DM patients with suspected CVB persistence. Daily 16:8 IF remains for NLRP3 suppression but is insufficient for reservoir clearance.

**T1DM caution:** FMD significantly lowers blood glucose; insulin adjustments are mandatory during FMD days. This requires physician supervision for insulin-dependent patients.

---

## Protocol Gap 5: SGLT2 Inhibitor Consideration (T1DM with Protocol)

From CROSS_POLLINATION.md: "SGLT2i as triple-purpose drug | DCM attempt 002 | T1DM (autophagy + BHB via one drug), ME/CFS (continuous autophagy without fasting) | One drug replaces three protocol components"

**What SGLT2i does in T1DM context:**
1. Lowers blood glucose (primary indication in T2DM; off-label in T1DM — empagliflozin has some T1DM data)
2. Produces glycosuria → mild ketosis → endogenous BHB production (continuous, without fasting)
3. Activates autophagy via AMPK pathway (independent of caloric restriction)
4. Cardioprotective (EMPA-REG, HF benefit — directly relevant to CVB cardiac risk)
5. Renal protective

**Relevance to dysbiosis protocol:**
If a T1DM patient is already on SGLT2i, they have continuous mild BHB and autophagy activation — this PARTIALLY replaces the need for FMD and exogenous BHB. The protocol's "IF + BHB" arm is less critical in this case.

**Note:** SGLT2i in T1DM (type 1, not type 2) is off-label in some countries; DKA risk is higher in T1DM. Must be discussed with endocrinologist. This is NOT a recommendation to add SGLT2i — it is context for interpreting the protocol if SGLT2i is already prescribed.

---

## Protocol Gap 6: NK Cell Function as Rate-Limiting Factor

From CROSS_POLLINATION.md: "NK cell restoration as rate-limiting | ME/CFS attempt 002 | All CVB diseases | If NK cells can't kill infected cells, no protocol works"

**Implication for dysbiosis/T1DM:**
If NK cell function is severely impaired, neither the antiviral protocol nor the immune modulation elements will clear CVB from islets. The protocol assumes baseline NK cell competence.

**NK cell assessment:**
- CBC with differential gives NK percentage but not function
- NK cytotoxicity assay (CD56+CD16+ function test) is research-grade; not routinely available
- Clinical proxy: recurrent severe viral infections, Herpes zoster at unusual age, EBV complications

**If NK cell function appears compromised:**
- Zinc sufficiency (NK cell number and function are zinc-dependent)
- Vitamin D (NK cell activation)
- GABA (the broader campaign notes GABA for T1DM - beta cell function/transdifferentiation; not NK specifically)
- Consider referral for immunological assessment if pattern suggests NK deficiency

---

## Updated Protocol Priority Order (Post-Import)

**Revised order for antiviral arm (replacing previous):**

1. **Fluoxetine** (primary CVB antiviral) — FIRST CHOICE
   - 20mg QD baseline; 60mg QD for males
   - Add when: IFN-α2 elevated OR active rosacea in T1DM OR clinical CVB suspicion
   - Physician prescription required

2. **Itraconazole** (OSBP inhibitor, CVB-specific secondary) — SECOND CHOICE
   - Only if fluoxetine contraindicated or inadequate response
   - NEVER with colchicine (documented fatalities)
   - CONTRAINDICATED in HF — baseline echocardiogram required before use
   - Full drug interaction review mandatory (CYP3A4)

3. **Trehalose 2g/day** — ADD to antiviral arm
   - Restores LAMP2-mediated autophagy flux depleted by CVB
   - Safe, cheap (~$15/month), minimal glucose impact
   - Start with breakfast

4. **FMD 5-day/month** — REPLACE simple IF for reservoir clearance
   - Simple 16:8 IF: KEEP for daily NLRP3 suppression
   - Monthly FMD: ADD for deep autophagy / viral reservoir clearance
   - T1DM: mandatory insulin adjustment; physician supervision required

5. **Butyrate 4-6g/day** — REPLACE 600mg/day
   - Titrate up from 600mg over 4-6 weeks
   - Enteric-coated sodium butyrate or tributyrin
   - High-fiber diet (40g+/day) + LGG is an alternative route to similar endogenous production

---

## DRUG_SAFETY_MATRIX — Additions to Dysbiosis Protocol

| Combination | Risk | Rule |
|-------------|------|------|
| Itraconazole + Colchicine | ⚠️ FATAL | NEVER together at full doses |
| Itraconazole + HF | ⚠️ CI | Check echo before use; negative inotrope |
| Fluoxetine + NSAIDs | Moderate | Add PPI for GI protection; monitor bleeding |
| Fluoxetine + MAOIs | ⚠️ FATAL | Serotonin syndrome — absolute CI |
| Fluoxetine + QT-prolonging drugs | Moderate | ECG at baseline and follow-up |
| Trehalose + T1DM insulin | Low | Minor glucose load; count as carbohydrate (~8g glucose equivalent per 2g trehalose) |

---

## Protocol Gap 7: Selenium 200μg/day — Prevents CVB Virulence Mutations

From CROSS_POLLINATION.md:
"Selenium/Keshan connection | Attempt 004 (myocarditis) | All 12 — but discovered from cardiac literature | Selenium isn't optional: it prevents viral virulence mutations"

**Mechanism:** Selenium deficiency → increased viral RNA mutation rate (because selenoproteins are antioxidants that normally reduce replication error rate) → CVB accumulates more mutations → quasispecies with enhanced virulence and persistence. Keshan disease: selenium-deficient areas of China → endemic CVB-induced cardiomyopathy.

**Relevance to dysbiosis M3 arm:** If the patient's selenium status is low, CVB persisting in islets is more likely to generate mutations that evade clearance. Selenium repletion reduces the mutation rate → less CVB quasispecies diversity → easier for immune surveillance.

**Dose:** 200μg QD (from DRUG_SAFETY_MATRIX.md). Do NOT exceed 400μg/day (toxicity — selenosis).

**Cost:** ~$5-10/month

**This is completely absent from the current dysbiosis protocol.**

## What Was Already Correct in Dysbiosis Protocol

These elements from the dysbiosis protocol are consistent with the broader campaign:
- Vitamin D3 + K2 (consistent: broader uses 5000 IU)
- Omega-3 2-4g EPA+DHA (consistent: broader uses 3g)
- Zinc sufficiency check (consistent; NK cell + VDR function)
- Intermittent fasting / BHB (consistent; now supplemented by FMD for clearance)
- Ketoconazole topical (M2 arm; not in broader campaign; appropriate for seb derm)
- Chlorhexidine + periodontal treatment (M7 arm; not in broader campaign; appropriate)
- I-FABP + IFN-α2 Simoa testing (consistent; broader campaign uses IFN-signature tests)

---

## Sky Bridge to ../eczema and ../psoriasis

From CONVERGENCE.md:
"Eczema and psoriasis are NOT caused by CVB. They are included because they share enough mechanism with the protocol's anti-inflammatory and immune-modulating components to improve as co-beneficiaries."

**This is the dysbiosis framework's M2 (skin dysbiosis) mountain described from the other direction.**
The campaign already includes eczema (Category 2) and psoriasis (Category 2) as co-beneficiaries. The dysbiosis framework's sky bridges (M1↔M4, M2+M4) are the mechanistic explanations for WHY these conditions improve as co-beneficiaries of a CVB-targeting anti-Th17 protocol.

**These directories should cross-reference each other.**

---

*Filed: 2026-04-12 | Cross-pollination import from ../CONVERGENCE.md + ../DRUG_SAFETY_MATRIX.md*
*Critical safety: Itraconazole + Colchicine DOCUMENTED FATALITIES — not previously noted in dysbiosis protocol*
*Protocol gaps: Fluoxetine (primary antiviral missing), butyrate dose (600mg → 4-6g), trehalose (missing), FMD (IF insufficient for reservoir clearance)*
*Update protocol_integration.md with these findings before any protocol implementation*
