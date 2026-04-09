# Clinical Investigator's Brief — One Virus, Twelve Diseases

> For the physician encountering this project for the first time. Read this document only. Everything else is supporting detail.

## The Thesis (3 sentences)

Coxsackievirus B (serotypes 1-5) establishes persistent infection via 5'-terminally deleted mutants in multiple organs. This single persistence mechanism drives at least 12 distinct clinical diseases, from type 1 diabetes to dilated cardiomyopathy to ME/CFS. A protocol combining a repurposed antiviral (fluoxetine), autophagy induction (fasting-mimicking diet), and multi-target anti-inflammatory support should clear the virus and halt disease progression across all affected organs.

## The Evidence (what's proven, what's not)

| Claim | Grade | Key citation |
|-------|-------|-------------|
| CVB persists in human T1DM islets | B+ | Krogvold 2015 (DiViD): VP1 in 6/6 newly diagnosed |
| CVB persists in human DCM hearts | B+ | Bowles 2003: enteroviral RNA in ~35% of DCM explants |
| CVB persists in ME/CFS muscle | B | Gow 1991: 42% of ME/CFS biopsies positive |
| Fluoxetine inhibits CVB in vitro | B | Zuo 2012, Benkahla 2018: IC50 1-10 μM |
| Fluoxetine protects mice from CVB myocarditis | B | Benkahla 2018 |
| BHB suppresses NLRP3 inflammasome | A- | Youm 2015 (Nature Medicine) |
| Fasting induces autophagy in humans | A | Multiple studies (LC3, p62 markers) |
| Colchicine reduces pericarditis recurrence | A | COPE, CORP, CORP-2 RCTs |
| IFN-β clears enterovirus from DCM + improves LVEF | B | Kühl 2003 (Circulation): n=22, LVEF 44→53% |
| CVB vaccine (VLP-ΔVP4) prevents ADE | C | Preclinical (Soppela) |
| Combined protocol clears CVB in humans | **Not tested** | This is the gap |

## The Protocol

### Antiviral arm
- **Fluoxetine 20mg daily** — CVB 2C ATPase inhibitor. Generic, $4/month.
- **Fasting-mimicking diet (FMD)** — 5-day cycle monthly. Induces autophagy to clear intracellular TD mutants.
- **Itraconazole 200mg daily** — OSBP/PI4KB inhibitor. ⚠️ Contraindicated in heart failure, hepatotoxicity risk. Optional, conditional on organ status.

### Anti-inflammatory arm
- **BHB** via ketogenic periods or exogenous ketones — NLRP3 suppression
- **Colchicine 0.5mg daily** — NLRP3 microtubule block. ⚠️ Do NOT combine with itraconazole at full dose (fatal CYP3A4 interaction documented).
- **Omega-3 3g EPA/DHA daily** — resolvin production
- **Vitamin D 5000 IU daily** — Treg induction

### Immune modulation arm
- **Butyrate 300mg TID** — gut barrier + FOXP3 → Tregs
- **Cold exposure** (2-3 min cold shower) — norepinephrine → IL-10 + NK cell mobilization
- **Sleep optimization** — NK cell activity peaks during slow-wave sleep

### Monitoring
- C-peptide (fasting + stimulated) — beta cell function (T1DM)
- hs-Troponin I, NT-proBNP — cardiac safety
- ALT/AST — hepatic safety
- CRP — inflammation tracking
- NK cell cytotoxicity — immune function (if available)

### Cost: ~$155/month (all generics and supplements)

## The Safety Concerns

| Concern | Severity | Mitigation |
|---------|----------|------------|
| **Itraconazole + colchicine** | CRITICAL — fatal interaction | Never combine at full dose. See DRUG_SAFETY_MATRIX.md |
| **Itraconazole in heart failure** | CRITICAL — negative inotrope | Contraindicated if LVEF <50%. Use fluoxetine alone. |
| **Fluoxetine + NSAIDs** | Moderate — bleeding risk | Add PPI during NSAID course. Limit NSAID to 2 weeks. |
| **Fasting in T1DM** | Moderate — hypoglycemia | Glucose monitoring, insulin adjustment, medical supervision |
| **BHB in T1DM** | Low-moderate — DKA risk | Monitor ketones, distinguish nutritional ketosis (1-3 mM) from DKA (>10 mM) |

## The Fastest Proof

**Option 1: the patient (n=1, 3-6 months)**
- Start protocol → measure stimulated C-peptide at baseline and 3-month intervals
- C-peptide improvement = direct evidence of beta cell recovery
- Fast, cheap, but n=1 limits generalizability

**Option 2: Pericarditis RCT (n=195, 18 months)**
- Colchicine ± fluoxetine for first-episode pericarditis
- Primary endpoint: recurrence at 18 months (binary)
- Clean, rigorous, publishable, but takes longer
- Most convincing to the medical community

**Option 3: ME/CFS Pilot (n=30, 16 weeks)**
- PEM-safe adapted protocol
- Endpoints: SF-36, NK cell cytotoxicity, 2-day CPET
- Largest unmet need, fastest recruitment, most subjective endpoints

## The Honest Assessment

The protocol is **mechanistically sound, clinically unproven.** Individual components have B-C grade evidence. The combination has never been tested. The weakest link is fluoxetine dose adequacy in target tissues (achievable plasma concentration is at or near the in vitro IC50). The strongest link is NLRP3 suppression by BHB (Grade A-).

The campaign will be validated or refuted by three data points:
1. the patient's stimulated C-peptide (tests the T1DM model)
2. Pericarditis recurrence rate with fluoxetine added (tests CVB persistence → disease)
3. Pharmacokinetic modeling of fluoxetine tissue concentrations (tests dose adequacy)

All three are achievable within 12-18 months.

## Where to Start Reading

| If you're interested in... | Read... |
|--------------------------|---------|
| The complete unifying thesis | MEDICAL_PROBLEMS.md |
| The T1DM cure hypothesis | t1dm/THEWALL.md |
| Drug safety | DRUG_SAFETY_MATRIX.md |
| Trial designs | CONVERGENCE.md |
| Honest uncertainty | EVIDENCE_GRADES.md, FAILURE_MODES.md |
| The vaccine endgame | CVB_VACCINE_STRATEGY.md |
| the patient next steps | PATIENT_ZERO_SCREENING.md |
