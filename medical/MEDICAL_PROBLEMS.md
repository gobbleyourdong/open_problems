# Medical Problems — systematic approach Campaign

> All caused by the same virus: **Coxsackievirus B (CVB)**

| # | Problem | Directory | Status | Phase | Connection |
|---|---------|-----------|--------|-------|------------|
| 1 | **Type 1 Diabetes** | `t1dm/` | 63 attempts, 5 targets | Phase 3 | Beta cell autoimmune destruction (CVB1/B4) |
| 2 | **Viral Myocarditis** | `myocarditis/` | Gap, model, anti-problem, 4 attempts | Phase 2 | Cardiomyocyte lysis + autoimmunity (CVB3) |
| 3 | **Dilated Cardiomyopathy** | `dilated_cardiomyopathy/` | Gap, model, anti-problem, 3 attempts | Phase 2 | 2A cleaves dystrophin → chronic heart failure |
| 4 | **ME/CFS** | `me_cfs/` | Gap, model, anti-problem, 3 attempts | Phase 2 | Persistent CVB in muscle/CNS → chronic fatigue |
| 5 | **Viral Pancreatitis** | `pancreatitis/` | Gap, anti-problem, 2 attempts | Phase 2 | Exocrine pancreas destruction (CVB1/B4) |
| 6 | **Pericarditis** | `pericarditis/` | Gap, model, anti-problem, 2 attempts | Phase 2 | NLRP3-driven, colchicine responsive |
| 7 | **Viral Hepatitis** | `hepatitis/` | Gap, model, anti-problem, 2 attempts | Phase 2 | Hepatocyte lysis, severe in neonates |
| 8 | **Pleurodynia (Bornholm)** | `pleurodynia/` | Gap, anti-problem, 2 attempts | Phase 2 | Intercostal muscle infection, sentinel symptom |
| 9 | **Aseptic Meningitis** | `aseptic_meningitis/` | Gap, model, anti-problem, 2 attempts | Phase 2 | CNS invasion, usually self-limiting |
| 10 | **Encephalitis** | `encephalitis/` | Gap, anti-problem, 2 attempts | Phase 2 | Brain parenchyma, rare but serious |
| 11 | **Orchitis** | `orchitis/` | Gap, anti-problem, 2 attempts | Phase 2 | Immune-privileged reservoir (CVB5) |
| 12 | **Neonatal Sepsis** | `neonatal_sepsis/` | Gap, model, anti-problem, 2 attempts | Phase 2 | Multi-organ, high mortality, earliest seeding |
| 13 | **Atopic Dermatitis / Eczema** | `eczema/` | Gap, model, anti-problem, 3 attempts, manifest | Phase 2 | NOT CVB — Th2/IgE; shared NLRP3, gut-skin axis, Treg deficit |
| 14 | **Psoriasis** | `psoriasis/` | Gap, model, anti-problem, 3 attempts, manifest | Phase 2 | NOT CVB — Th17/IL-23; shared NF-κB/TNF-α, NLRP3, Treg/Th17 balance |

## The Unifying Thesis

**One protocol. Fourteen diseases. Two categories.**

### Category 1: CVB-caused (diseases 1-12)
All 12 share:
- Same pathogen (CVB serotypes B1-B5)
- Same persistence mechanism (5' terminal deletion → TD mutants)
- Same proteases doing damage (2A cleaves dystrophin/host proteins, 3C cleaves SNAP29/host proteins)
- Same immune evasion (MHC-I downregulation, autophagy hijacking, exosomal escape)
- Same autoimmune trigger (molecular mimicry → tissue-specific autoantibodies)

### Category 2: Immune dysregulation co-beneficiaries (diseases 13-14)
Not CVB-caused, but share:
- NF-κB / TNF-α amplification loops
- NLRP3 inflammasome activation
- Treg insufficiency (Th2 in eczema, Th17 in psoriasis)
- Gut dysbiosis → immune dysregulation
- Bistable attractor dynamics

### The Shared Mechanism
**Tregs are the universal brake.** Every disease involves insufficient Treg suppression of a pathogenic T helper response. The protocol's Treg-restoring components (butyrate, vitamin D, BHB, WHM→IL-10) address all 14 diseases.

The T1DM protocol (attempt 001-063) is the most developed. Its anti-inflammatory and immune-modulating components are disease-agnostic. The antiviral arm (fluoxetine, autophagy) applies to CVB diseases only.

## Method

Same as `gobbleyourdong/math_problems` — see `SIGMA_METHOD.md`.

Adapted for biology:
- "Lean theorems" → mechanistic pathway models (formalized where possible)
- "SOS certificates" → clinical trial data, genomic datasets, reproducible analyses
- "Proof attempts" → treatment approaches (each with documented failure mode)
- "The gap" → the single mechanism that, if solved, unlocks the cure
- "Anti-problem" → study spontaneous remission cases, tolerized patients

## Priority

T1DM is the patient's disease → primary focus. But findings propagate to all 12.
Myocarditis/DCM is #2 priority (cardiac screening for the patient).
ME/CFS is #3 (largest affected population, most underserved).

## Cross-Disease Documents
- `CONVERGENCE.md` — Clinical trial roadmap, shared protocol core, disease hierarchy
- `PATIENT_ZERO_SCREENING.md` — Multi-disease CVB screening protocol ($1,300-3,500)
- `CVB_VACCINE_STRATEGY.md` — The endgame: one vaccine prevents all 12 diseases
- `DRUG_SAFETY_MATRIX.md` — Drug interactions, contraindications, organ-specific safety
- `CLINICAL_BRIEF.md` — Entry point for physicians: thesis, evidence, protocol, safety, in one document
- `FOR_YOUR_DOCTOR.md` — Practical communication guide for the patient's doctor visit
- `PATIENT_ZERO_TIMELINE.md` — Week-by-week implementation plan with decision gates
- `CROSS_POLLINATION.md` — How findings from each disease inform all the others
- `EVIDENCE_GRADES.md` — Adversarial scrutiny of every major claim (A-E grading)
- `FAILURE_MODES.md` — Pre-registered failure modes, probabilities, mitigations
- `ODD_INSTANCE_REQUESTS.md` — 8 computational tasks queued for the numerical track
- `CAMPAIGN_SUMMARY.md` — Full campaign status, key discoveries, what's next
- `models/cvb_persistence_universal.md` — The shared persistence mechanism across all 12 diseases
