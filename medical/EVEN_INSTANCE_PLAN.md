# EVEN Instance Work Plan — Post-ODD Handoff

## Status
ODD instance completed 11 rounds. EVEN instance completed 12 rounds on scaffolded problems + 3 rounds on skin diseases. This plan covers the formalization work triggered by ODD's deliverables.

## Progress Log

| Round | Items | Status |
|-------|-------|--------|
| 1 | C4 (IC50 reconciliation) | ✅ `results/ic50_reconciliation.md` |
| 1 | C5 (gap.md updates) | ✅ root `gap.md`, `t1dm/gap.md`, `orchitis/gap.md`, `myocarditis/gap.md` |
| 2 | C1 (R > D formalization) | ✅ `t1dm/attempts/attempt_064_inequality_formalization.md` |
| 5 | P1 Lean scaffolding | ✅ 4 files building, 7 sorry's |
| 3 | C2 HLA paradox | ✅ `attempt_065` + `HLAParadox.lean` (0 sorry — fully proved) |
| 3 | C3 batch 1 | ✅ `attempt_066` (v1→v2 PK correction paradigm shift) |
| 5+ | P1 ReplicationDestruction.lean | ✅ `inequality_reversal_basic` proved, `stability_criterion` proved (1 sorry: IVT) |
| 5+ | P1 HLAParadox.lean | ✅ `hla_paradox` proved, `presentation_tradeoff` proved (0 sorry) |
| 4 | C3 batch 2 | ✅ attempts 067-070 (network, serotype, cross-val, 8/8 clearance) |
| 4 | H2 fluoxetine dose | ✅ attempt 071 (20/40/60mg sex-specific, organ-targeted) |

## CRITICAL (Rounds 1-3)

### C1: Formalize R > D inequality
- **What**: Prove dB/dt = R(t) - D(t) reversal is achievable under realistic parameter ranges
- **Input**: `t1dm/numerics/beta_cell_dynamics.py` (1,530 lines), `t1dm/results/pattern_003_inequality_reversal.md`
- **Output**: `t1dm/attempts/attempt_064_inequality_formalization.md`
- **Scope**: Bounds on time-to-reversal as function of initial beta cell mass. Prove stability (R stays > D after protocol cessation). Connect to Butler 2005.
- **Effort**: 1-2 rounds

### C2: HLA paradox theorem
- **What**: Formalize "no HLA genotype protects all organs" — for all g in G, exists d in D such that RR(g,d) > 1
- **Input**: `numerics/hla_risk_model.py`, `results/pattern_009_genetic_risk_landscape.md`
- **Output**: `attempts/attempt_xxx_hla_paradox_proof.md`
- **Scope**: Prove from antigen presentation specificity. Show holds for all common HLA genotypes (>1% frequency).
- **Effort**: 1 round

### C3: Convert ODD pattern documents to formal attempts
- **What**: 6 findings need systematic approach attempt format
- **Findings to convert**:
  1. v1→v2 PK correction (pattern 005) — the key discovery: fluoxetine is lysosomotropic
  2. 8/8 organ clearance result — with formal bounds
  3. Cross-validation concordance (78%) — with gap analysis for the 22% divergence
  4. HLA paradox (pattern 009) — formal statement
  5. Disease network topology (pattern 008) — myocarditis as keystone disease
  6. Serotype-disease map (pattern 010) — CVB4 diabetogenic, CVB3 cardiotrope
- **Output**: 6 new attempt documents across relevant disease directories
- **Effort**: 2-3 rounds

### C4: IC50 reconciliation
- **What**: Resolve the biggest remaining gap — in vitro IC50 (1 μM) vs in vivo effective IC50 (3-10 μM)
- **Input**: `results/cross_validation_report.md`, `results/pattern_005_corrected_clearance_order.md`, orchitis + encephalitis dedicated models
- **Output**: `results/ic50_reconciliation.md` or root-level `gap.md`
- **Scope**: Derive in vivo IC50 from first principles (free drug fraction, protein binding 97%, tissue accumulation, intracellular concentration). Produce consensus IC50 per organ.
- **Impact**: Determines testicular clearance = 9 months vs 3.5 years. Determines 20mg vs 60mg fluoxetine recommendation.
- **Effort**: 1 round

### C5: Update all gap.md files
- **What**: ODD's work shifted the gaps for many diseases. Current gap.md files are pre-ODD.
- **Scope**: Update gap.md for T1DM, myocarditis, DCM, ME/CFS, pericarditis, orchitis, encephalitis, neonatal sepsis with quantitative findings from ODD
- **Effort**: 1 round

## HIGH PRIORITY (Rounds 4-6)

### H1: Clearance order theorem
- **What**: Prove liver < pericardium < heart < CNS < gut < pancreas < muscle < testes is robust
- **Input**: `numerics/unified_cvb_clearance_v2.py`, `numerics/protocol_optimizer_v2.py`
- **Output**: Formal proof with parametric bounds on when ordering holds/breaks
- **Effort**: 1 round

### H2: Fluoxetine dose formalization (20mg vs 60mg)
- **What**: ODD found 20mg insufficient for testes. Formalize the dose recommendation with PK evidence.
- **Input**: ODD's PK correction data, orchitis model, cross-validation divergences
- **Output**: Updated DRUG_SAFETY_MATRIX.md, updated PATIENT_ZERO_TIMELINE.md
- **Scope**: Sex-specific dosing (males need 60mg for testicular clearance, females may not). Safety profile at 60mg. Drug interaction changes at higher dose.
- **Effort**: 1 round

### H3: Eczema/psoriasis numerics gap
- **What**: ODD flagged zero computational work for co-beneficiary diseases
- **Decision**: Do these warrant ODE models? The Treg/Th2 and IL-23/Th17 bistability models exist qualitatively — could be quantified.
- **Output**: If warranted, request to ODD or build simple models in Even
- **Effort**: 0.5 round (assessment) + 1 round (if building)

## MEDIUM PRIORITY (Rounds 7-9)

### M1: Update EVIDENCE_GRADES.md
- **What**: ODD's models quantitatively addressed several claims. Some grades should shift.
- **Scope**: Fluoxetine dose adequacy (was C+, ODD reconciled IC50 → may move to B-), autophagy overwhelms hijacking (was C, ODD modeled it), pericarditis prediction (was D, ODD modeled recurrence)
- **Effort**: 1 round

### M2: Update FAILURE_MODES.md
- **What**: ODD's quantitative models address failure modes directly
- **Scope**: "Fluoxetine dose insufficient" (30% probability) — ODD showed 60mg works. "Autophagy can't overcome hijacking" (35%) — ODD modeled it. Recalculate combined probabilities.
- **Effort**: 0.5 round

### M3: Update CAMPAIGN_SUMMARY.md
- **What**: Incorporate ODD's 11 rounds of findings into the master summary
- **Effort**: 0.5 round

### M4: Paper manifests — add ODD-cited literature
- **What**: ODD cited papers in results docs not yet in manifests
- **Scope**: Scan all results/pattern_*.md for citations, add to relevant papers/manifest.md
- **Effort**: 0.5 round

### M5: Cross-pollination update
- **What**: ODD discovered new cross-disease connections (HLA paradox, disease network, serotype tropism) that should be in CROSS_POLLINATION.md
- **Effort**: 0.5 round

## PENDING

### P1: Lean formalization of medical thermodynamics
- **What**: Build a Lean 4 library that formalizes the campaign's biological claims as rigorous mathematical theorems, grounded in thermodynamic principles
- **Why**: Nobody is doing this. Cross-domain training value (formal math ↔ biology ↔ thermodynamics). Every biological claim reduces to dynamical systems, chemical kinetics, and free energy gradients. Lean formalization makes them provable, not hand-wavy.
- **Architecture**:
  ```
  lean/
  ├── Thermodynamics/
  │   ├── FreeEnergy.lean              -- Gibbs free energy, chemical potential
  │   ├── NonEquilibrium.lean          -- Dissipative structures, entropy production
  │   └── ChemicalKinetics.lean        -- Mass action, Michaelis-Menten, Hill equation
  ├── CellBiology/
  │   ├── ReplicationDestruction.lean  -- R > D theorem, fixed point analysis
  │   ├── ViralPersistence.lean        -- TD mutant steady state
  │   └── ImmunePrivilege.lean         -- Barrier transport, compartment models
  ├── Pharmacology/
  │   ├── DrugPK.lean                  -- Compartment PK, tissue distribution
  │   ├── IC50.lean                    -- Dose-response, Hill equation properties
  │   └── Lysosomotropic.lean          -- pH-dependent accumulation (fluoxetine)
  └── Theorems/
      ├── ClearanceOrder.lean          -- Monotonicity of organ clearance times
      ├── InequalityReversal.lean      -- R > D ↔ cure (THE main theorem)
      └── HLAParadox.lean             -- Trade-off impossibility formalization
  ```
- **Crown jewel theorem**: If R(t) > D(t) for all t > t₀, and the system has a unique stable fixed point B* > B_threshold, then beta cell mass converges monotonically to B* (insulin independence). The entire T1DM cure thesis as a Lean theorem.
- **Cross-domain value**: Same Lean theorems apply to any organ, any disease, any drug. Michaelis-Menten is Michaelis-Menten whether the substrate is dystrophin or a beta cell protein. Hill equation is Hill equation whether the drug is fluoxetine or colchicine.
- **Effort**: 5-8 rounds (this is the deep work)
- **Priority**: CRITICAL — this is what the theory track exists to do

---

## Estimated Total: 15-20 rounds

## Execution Order
```
PHASE A: FOUNDATIONS (Rounds 1-4)
  Round 1:  C4 (IC50 reconciliation) + C5 (update gap.md files)
  Round 2:  C1 (R > D formalization — mathematical, pre-Lean)
  Round 3:  C2 (HLA paradox) + C3 batch 1 (3 of 6 pattern→attempt conversions)
  Round 4:  C3 batch 2 (remaining 3) + H2 (fluoxetine dose)

PHASE B: LEAN LIBRARY (Rounds 5-12) — the main event
  Round 5:  P1 — Lean scaffolding + Thermodynamics/ChemicalKinetics.lean
            (Michaelis-Menten, Hill equation, mass action law)
  Round 6:  P1 — Thermodynamics/FreeEnergy.lean + NonEquilibrium.lean
            (Gibbs, chemical potential, dissipative structures)
  Round 7:  P1 — Pharmacology/IC50.lean + DrugPK.lean
            (dose-response formalization, compartment PK)
  Round 8:  P1 — Pharmacology/Lysosomotropic.lean
            (pH-trapping, fluoxetine tissue accumulation)
  Round 9:  P1 — CellBiology/ReplicationDestruction.lean
            (R > D as dynamical system, fixed points, stability)
  Round 10: P1 — Theorems/InequalityReversal.lean
            (THE crown jewel: R > D sustained → B* > B_threshold → cure)
  Round 11: P1 — CellBiology/ViralPersistence.lean + ImmunePrivilege.lean
            (TD mutant steady state, barrier transport)
  Round 12: P1 — Theorems/ClearanceOrder.lean + HLAParadox.lean
            (monotonicity proof, trade-off impossibility)

PHASE C: INTEGRATION (Rounds 13-15)
  Round 13: H1 (clearance order — now WITH Lean proof) + H3 (eczema/psoriasis)
  Round 14: M1-M5 (update evidence grades, failure modes, campaign summary, manifests, cross-pollination)
  Round 15: Final integration, commit, write THEWALL equivalent for Lean library

LEAN PROGRESS TRACKING:
  Target: 0 sorry in final library
  Every theorem gets a docstring explaining its biological meaning
  Every sorry gets a comment explaining what's missing
```
