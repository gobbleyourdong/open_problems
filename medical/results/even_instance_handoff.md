# theory track Handoff Document -- ODD Instance Final Deliverable

## systematic approach -- CVB Medical Problems Campaign
## Date: 2026-04-08
## From: ODD Instance (numerics / brute-force)
## To: theory track (theory / formalization)

---

# SECTION 1: CAMPAIGN SUMMARY

## What the ODD Instance Did Across 8 Rounds

The ODD instance executed 8 rounds of numerical computation, progressing from a single-disease T1DM model to a fully cross-validated 12-disease computational framework. Each round built on the previous:

| Round | Focus | Key Deliverable |
|-------|-------|-----------------|
| 1 | Unified 8-organ CVB clearance model (v1) | `numerics/unified_cvb_clearance.py` -- 8 compartments, 34 state variables |
| 2 | Protocol optimization + sensitivity analysis | `numerics/protocol_optimizer.py` -- ablation, minimum protocol, dose-response |
| 3 | Iron Fortress validation (21 cross-checks) | `numerics/validate_all_models.py` -- all 21 PASS/WARN classifications |
| 4 | v2 model: PK correction + autophagy fix | `numerics/unified_cvb_clearance_v2.py` -- corrected brain 15x, testes 2.5x; ALL 8 organs now clearable |
| 5 | Biomarker trajectories + monitoring protocol | `numerics/biomarker_trajectories.py`, `numerics/monitoring_schedule.py` -- 15 biomarkers, visit-by-visit lab orders |
| 6 | Vaccine impact + anti-problem cross-disease | `numerics/cvb_vaccine_impact.py`, `numerics/anti_problem_cross_disease.py` -- 85% reduction with vaccination |
| 7 | Disease network + drug interactions + safety | `numerics/disease_network.py`, `numerics/drug_interactions.py`, `numerics/safety_pharmacology.py` -- 36 pairwise interactions, DKA model |
| 8 | HLA risk model + lifetime trajectory + cross-validation + serotype tropism + protocol implementation | `numerics/hla_risk_model.py`, `numerics/patient_lifetime_trajectory.py`, `numerics/cross_validate_models.py`, `numerics/serotype_tropism.py`, `numerics/acute_vs_chronic_model.py`, `numerics/protocol_implementation.py` |

**Total output: 18 root-level Python scripts (20,997 lines), 31 disease-specific scripts (19,526 lines), 40,523 lines of computational code total.**

## Key Quantitative Findings

### 1. Clearance Times (v2 corrected model, full protocol)

| Organ | Clearance Time | Confidence | Dedicated Model Estimate |
|-------|---------------|------------|--------------------------|
| Liver | 0.21 yr (2.5 mo) | HIGH | Compatible (fastest, both agree) |
| Pericardium | 0.27 yr (3 mo) | HIGH | 0.27 yr (MATCH) |
| Heart | 0.37 yr (4.5 mo) | HIGH | 0.37 yr (MATCH) |
| CNS | 0.42 yr (5 mo) | MODERATE | 1.7 yr (dedicated more conservative) |
| Gut | 0.42 yr (5 mo) | HIGH | N/A (no dedicated model) |
| Pancreas | 0.46 yr (5.5 mo) | HIGH | Compatible with T1DM models |
| Skeletal Muscle | 0.60 yr (7 mo) | MODERATE | 0.75 yr (ME/CFS model, CLOSE) |
| Testes | 0.77 yr (9 mo) | LOW-MODERATE | 3.5 yr (orchitis model, DIVERGENT) |

**Clinical planning recommendation: 18 months minimum, biomarker-guided early cessation possible at 12 months.**

### 2. Success Probabilities

| Metric | Value | Source |
|--------|-------|--------|
| Probability >= 1 protocol arm works | 92.5% | FAILURE_MODES.md, Monte Carlo |
| Full protocol clears 8/8 organs (v2) | 100% in model | unified_cvb_clearance_v2.py |
| Full protocol clears 7/7 female (v2) | 100% in model | Same |
| Minimum protocol (FLX + FMD) clears 8/8 | 100% in model, $40/mo | protocol_optimizer_v2.py |
| DKA risk per fast (with protocol) | <1% | safety_pharmacology.py |
| Severe hypoglycemia per month | <2% | Same |
| Cross-validation concordance | 78% (13 MATCH, 5 CLOSE, 5 DIVERGENT / 23 metrics) | cross_validate_models.py |

### 3. Safety Profile

| Interaction Category | Count (of 36 pairs) | Percentage |
|---------------------|---------------------|-----------|
| NONE | 24 | 67% |
| MINOR | 7 | 19% |
| MODERATE | 4 | 11% |
| MAJOR | 1 (fasting + exo BHB) | 3% |
| CONTRAINDICATED | 0 | 0% |

**One major interaction (fasting + exogenous BHB in T1DM) is resolved by a simple rule: never combine during fasting.**

### 4. State of Each Disease

| # | Disease | Phase | Scripts | Results | Certs | Figures | Cross-Validated? |
|---|---------|-------|---------|---------|-------|---------|------------------|
| 1 | T1DM | 3 | 10 | 4 | 5 | 14 | Yes (pancreas compartment) |
| 2 | Myocarditis | 3 | 2 | 1 | 3 | 4 | Yes (3/3 MATCH) |
| 3 | DCM | 3 | 2 | 1 | 3 | 0 | Yes (1 MATCH, 1 DIVERGENT) |
| 4 | ME/CFS | 3 | 3 | 2 | 4 | 17 | Yes (3 MATCH, 1 CLOSE, 1 DIVERGENT) |
| 5 | Pancreatitis | 2 | 2 | 1 | 1 | 0 | Not directly |
| 6 | Pericarditis | 3 | 1 | 1 | 1 | 0 | Yes (2 MATCH, 1 CLOSE) |
| 7 | Hepatitis | 2 | 2 | 1 | 2 | 6 | Yes (2 MATCH, 1 CLOSE) |
| 8 | Orchitis | 2 | 1 | 2 | 2 | 6 | Yes (2 MATCH, 2 DIVERGENT) |
| 9 | Encephalitis | 3 | 2 | 1 | 2 | 9 | Yes (3 MATCH, 1 DIVERGENT) |
| 10 | Aseptic Meningitis | 2 | 1 | 1 | 1 | 4 | No |
| 11 | Neonatal Sepsis | 2 | 1 | 2 | 1 | 4 | N/A (different population) |
| 12 | Pleurodynia | 2 | 2 | 2 | 1 | 7 | No |
| 13 | Eczema | 0* | 0 | 0 | 0 | 0 | N/A (not CVB-caused) |
| 14 | Psoriasis | 0* | 0 | 0 | 0 | 0 | N/A (not CVB-caused) |

*Eczema and psoriasis are immune-dysregulation co-beneficiaries, not CVB-caused. They have theory track scaffolding (attempts, models, gap, anti-problem) but no ODD instance numerics.

**Totals: 46 Python scripts, 31+ results documents, 27 certs, 162 figures.**

---

# SECTION 2: WHAT NEEDS FORMALIZATION

## A. CRITICAL (Do First)

### A1. Formalize the inequality R > D as a rigorous mathematical framework

**What**: The T1DM model centers on dB/dt = R(t) - D(t), where B is beta cell mass, R is total regeneration, D is total destruction. The ODD instance has a 9-state ODE model (`t1dm/numerics/beta_cell_dynamics.py`, `t1dm/numerics/anti_problem_spontaneous_remission.py`) showing that the full protocol reverses this inequality.

**Why this is critical**: This is the core mathematical claim of the entire campaign. If R > D can be formalized with certified bounds, every downstream claim (clearance, remission, protocol efficacy) follows.

**What needs to happen**:
- Prove that R > D is achievable under realistic parameter ranges (not just point estimates)
- Derive bounds on time-to-reversal as a function of initial beta cell mass
- Prove that the reversal is STABLE (R stays > D after protocol cessation, or identify conditions where it doesn't)
- Connect to Butler 2005 data on residual beta cells

**Input files**: `t1dm/numerics/beta_cell_dynamics.py` (1,530 lines), `t1dm/results/pattern_003_inequality_reversal.md`
**Output**: `t1dm/attempts/attempt_064_inequality_formalization.md` or equivalent
**Priority**: CRITICAL
**Estimated effort**: 1-2 rounds

### A2. Formalize the "no HLA genotype protects all organs" theorem

**What**: The ODD instance HLA model (`numerics/hla_risk_model.py`) demonstrates that HLA alleles that protect one organ (e.g., DQ6 protects pancreas from T1DM) can increase risk for another (e.g., slight CNS risk). The negative correlation between T1DM and cardiac disease risks (r ~ -0.3 to -0.5) is quantified.

**Why this is critical**: This is a publishable theorem with clinical implications for screening. "No HLA genotype is universally protective" is a strong formal claim that needs proof, not just Monte Carlo.

**What needs to happen**:
- Formalize as: For all HLA genotypes g in G, there exists at least one disease d in D such that RR(g, d) > 1
- Prove from the antigen presentation specificity argument (different HLA alleles present different CVB peptides in different organs)
- Connect to population genetics: show that the claim holds for all common HLA genotypes (>1% frequency)

**Input files**: `numerics/hla_risk_model.py`, `results/pattern_009_genetic_risk_landscape.md`
**Output**: `attempts/attempt_xxx_hla_paradox_proof.md` + potential `lean/` formalization
**Priority**: CRITICAL
**Estimated effort**: 1 round

### A3. Write attempt documents for each major finding

**What**: The ODD instance has produced results documents (pattern_001 through pattern_010) but these are NOT in systematic approach attempt format. The theory track should convert key findings into formal attempt documents that fit the attempts/ lineage.

**Findings that need attempt documents**:
1. The v1-to-v2 PK correction (pattern 005) -- this IS the key discovery
2. The 8/8 clearance result -- with formal bounds
3. The cross-validation concordance (78%) -- with formal gap analysis
4. The HLA paradox (pattern 009) -- formal statement
5. The disease network topology (pattern 008) -- myocarditis as keystone
6. The serotype-disease map (pattern 010) -- CVB4 diabetogenic, CVB3 cardiotrope

**Priority**: CRITICAL
**Estimated effort**: 2-3 rounds (one attempt per round, batch 2-3 per round)

### A4. Update gap.md with the current gap

**What**: The primary remaining gap is the IC50 discrepancy: in vitro IC50 = 1 uM (Zuo 2018, cell culture), in vivo effective IC50 = 3-10 uM (protein binding, tissue distribution, intracellular concentration). The cross-validation divergences in testes (0.77yr vs 3.5yr) and CNS (0.42yr vs 1.7yr) trace directly to this.

**Why this matters**: The gap between unified v2 clearance predictions and dedicated model predictions is 4-5x for the slowest-clearing organs. Reconciliation determines whether the protocol is 9 months or 3.5 years for testicular clearance.

**What needs to happen**:
- Derive the correct in vivo IC50 from first principles: free drug fraction, protein binding (97% bound), tissue accumulation factors, intracellular concentration vs extracellular
- The theory track should be able to compute: IC50_in_vivo = IC50_in_vitro / (f_free * f_tissue_accumulation * f_intracellular)
- Produce a single consensus IC50 for each organ that both models can use

**Input files**: `results/cross_validation_report.md`, `results/pattern_005_corrected_clearance_order.md`, `orchitis/numerics/immune_privilege_clearance.py`, `encephalitis/numerics/cns_clearance_feasibility.py`
**Output**: Updated `gap.md` (root level) or new `results/ic50_reconciliation.md`
**Priority**: CRITICAL
**Estimated effort**: 1 round

---

## B. HIGH PRIORITY

### B1. Formalize the clearance order theorem

**Claim**: liver < pericardium < heart < CNS < gut < pancreas < muscle < testes (where "<" means "clears faster than").

**What needs proving**:
- Is this ordering ROBUST under parameter perturbation? (The ODD instance sensitivity analysis suggests yes, but there is no formal proof.)
- Under what parameter regimes does the ordering change? (e.g., if brain:plasma ratio drops below 5x, does CNS move behind muscle?)
- Are there patient-specific scenarios (e.g., high testicular fluoxetine accumulation) where the order reverses?

**Input files**: `numerics/unified_cvb_clearance_v2.py`, `numerics/protocol_optimizer_v2.py`, `results/pattern_005_corrected_clearance_order.md`
**Output**: Formal proof with parametric bounds on when the ordering holds
**Priority**: HIGH
**Estimated effort**: 1 round

### B2. Formalize the anti-problem result

**Claim**: The full protocol mimics non-progressor immunology. Specifically, the state vector (Treg/Teff ratio, viral load, autoantibody titer, NK cell activity) after 12 months of protocol converges to the state vector of natural CVB non-progressors.

**Input files**: `t1dm/numerics/non_progressor_profile.py`, `t1dm/results/pattern_002_anti_problem.md`, `numerics/anti_problem_cross_disease.py`
**Output**: `attempts/attempt_xxx_anti_problem_convergence.md`
**Priority**: HIGH
**Estimated effort**: 1 round

### B3. Write the convergence document (attempt_030-style synthesis)

**What**: A single document that synthesizes ALL findings across all 12 diseases, all 8 ODD instance rounds, and all theory track scaffolding into a coherent narrative. This is the "paper outline" document.

The existing `CONVERGENCE.md` is a good start but is structured as a hierarchy/roadmap, not a formal synthesis. The theory track should produce a document that could serve as the skeleton of a publication.

**Input files**: `CONVERGENCE.md`, `CAMPAIGN_SUMMARY.md`, `results/campaign_inventory_v2.md`, all pattern documents
**Output**: New convergence synthesis document
**Priority**: HIGH
**Estimated effort**: 2 rounds

### B4. Create lean/ formalizations where applicable

**What**: The following claims are amenable to lean4 formalization:
1. The R > D inequality (algebraic, provable from component rates)
2. The clearance ordering (follows from monotonicity of ODE solutions given ordered parameters)
3. The HLA paradox (combinatorial: show that the HLA-disease risk matrix has no all-protective row)

**Why**: Lean formalizations would make this the first computationally verified medical hypothesis framework. Even if the biology is uncertain, the MATHEMATICAL claims can be machine-checked.

**Input files**: All numerics scripts (for parameter values), all pattern documents (for claims)
**Output**: `lean/` directory with .lean files
**Priority**: HIGH
**Estimated effort**: 2-3 rounds (lean4 formalization is time-intensive)

---

## C. MEDIUM PRIORITY

### C1. Paper review: scan for new publications

**Specific papers/topics to search**:
- CVB vaccine candidates: follow-up on Soppela VLP-deltaVP4 paper, any new mRNA CVB vaccine work
- Hypoimmune cells: Deng CiPSC follow-up (Cell 2019) -- any advancement toward clinical trials?
- Fluoxetine antiviral: any new papers on fluoxetine vs enteroviruses since Zuo 2018?
- SGLT2i and autophagy: new mechanistic data supporting dapagliflozin/empagliflozin as autophagy inducers?
- Teplizumab: post-approval real-world data (FDA approved 2022, now 3+ years of clinical experience)
- CVB persistence: any new DiViD-like studies or TD mutant detection methods?

**Input files**: `t1dm/papers/MANIFEST.md`, `eczema/papers/manifest.md`, `psoriasis/papers/manifest.md`
**Output**: Updated manifests, new paper summaries if warranted
**Priority**: MEDIUM
**Estimated effort**: 1 round

### C2. Formalize certificates as citable claims

**What**: The 27 existing certs across all diseases have varying levels of rigor. The theory track should:
- Grade each cert by evidence quality (A-E per EVIDENCE_GRADES.md)
- Identify which certs are publication-ready (Grade A or B evidence)
- Identify which certs need additional literature support

**Current cert inventory** (27 total):
- T1DM: 5 certs (beta cell persistence, FMD regeneration, DiViD CVB persistence, honeymoon prevalence, butyrate Treg induction)
- Myocarditis: 3 (CVB3 peak kinetics, DCM progression rate, fluoxetine CVB antiviral)
- DCM: 3 (cardiomyocyte renewal, dystrophin cleavage, DCM reversibility)
- ME/CFS: 4 (CVB persistence prevalence, NK cell dysfunction, mitochondrial dysfunction, LDN efficacy)
- Pericarditis: 1 (colchicine efficacy)
- Hepatitis: 2 (liver regeneration, neonatal IFN deficit)
- Orchitis: 2 (BTB barrier, SSRI testicular penetration)
- Encephalitis: 2 (neuronal CAR expression, fluoxetine brain penetration)
- Aseptic Meningitis: 1 (enterovirus CSF detection)
- Neonatal Sepsis: 1 (neonatal mortality)
- Pleurodynia: 1 (epidemic-T1DM correlation)
- Pancreatitis: 1 (CVB islet tropism)
- Root: 2 (CVB R0, serotype tropism)

**Priority**: MEDIUM
**Estimated effort**: 1 round

### C3. Write the anti-problem document (anti_problem.md)

**What**: A root-level anti-problem document that synthesizes all 12+ disease-level anti-problems into a unified anti-problem framework. The ODD instance ran the cross-disease anti-problem analysis (`numerics/anti_problem_cross_disease.py`) and the theory track has individual disease anti-problems, but there is no single document asking: "What does a person who is exposed to CVB but develops NONE of the 12 diseases look like?"

**Answer from the numerics**: Such a person has (1) rapid WT clearance via strong NK + CD8 response, (2) no TD mutant formation or rapid autophagy-mediated TD clearance, (3) high Treg/Teff ratio preventing autoimmunity, (4) DQ6-type HLA providing efficient viral presentation without organ-specific autoimmunity. The protocol CREATES this phenotype pharmacologically.

**Input files**: `numerics/anti_problem_cross_disease.py`, all disease-level `anti_problem.md` files
**Output**: Root-level `anti_problem.md`
**Priority**: MEDIUM
**Estimated effort**: 1 round

### C4. Cross-reference with T1DM attempts 001-063

**What**: The T1DM attempt lineage (63 attempts over many rounds) contains findings that predate the 12-disease expansion. Some of these findings have been incorporated into the cross-disease framework, but the theory track should verify completeness:
- Which T1DM findings apply to ALL diseases? (e.g., attempts 054, 059, 062 on NF-kB)
- Which T1DM findings are T1DM-specific? (e.g., attempt 023 on alpha-to-beta transdifferentiation)
- Are there any T1DM findings that CONTRADICT the cross-disease model?

**Input files**: `t1dm/attempts/attempt_001.md` through `t1dm/attempts/attempt_063.md`
**Output**: Cross-reference audit document
**Priority**: MEDIUM
**Estimated effort**: 1-2 rounds

---

# SECTION 3: SPECIFIC REQUESTS

## Request 1: Formalize the R > D Inequality

| Field | Value |
|-------|-------|
| **File to create** | `t1dm/attempts/attempt_064_inequality_formalization.md` |
| **Input files** | `t1dm/numerics/beta_cell_dynamics.py` (1,530 lines), `t1dm/numerics/anti_problem_spontaneous_remission.py` (1,194 lines), `t1dm/results/pattern_003_inequality_reversal.md` |
| **What output should demonstrate** | (1) R > D is achievable for B_0 >= 0.03 (3% residual beta cells) with probability > 95% under parameter uncertainty; (2) Time to reversal T* as function of B_0; (3) Stability: once R > D, under what conditions does it revert? |
| **Priority** | CRITICAL |
| **Estimated effort** | 1-2 rounds |

## Request 2: IC50 Reconciliation

| Field | Value |
|-------|-------|
| **File to create** | `results/ic50_reconciliation.md` or update to root `gap.md` |
| **Input files** | `results/cross_validation_report.md`, `results/pattern_005_corrected_clearance_order.md`, `orchitis/numerics/immune_privilege_clearance.py` (line ~50-100 for IC50 params), `encephalitis/numerics/cns_clearance_feasibility.py` (line ~50-100 for IC50 params) |
| **What output should demonstrate** | Single consensus IC50 per organ derived from first principles (free fraction, protein binding, tissue accumulation). Should resolve the 4.5x clearance time discrepancy for testes and 4x for CNS. |
| **Priority** | CRITICAL |
| **Estimated effort** | 1 round |

## Request 3: HLA Paradox Proof

| Field | Value |
|-------|-------|
| **File to create** | `attempts/attempt_xxx_hla_paradox_proof.md` + `lean/hla_paradox.lean` |
| **Input files** | `numerics/hla_risk_model.py` (1,089 lines), `results/pattern_009_genetic_risk_landscape.md` |
| **What output should demonstrate** | Formal proof that for any HLA genotype g with population frequency > 0.01, there exists disease d such that RR(g, d) > 1.0. The proof should be constructive (exhibit the disease for each major genotype). |
| **Priority** | CRITICAL |
| **Estimated effort** | 1 round |

## Request 4: Clearance Order Robustness

| Field | Value |
|-------|-------|
| **File to create** | `results/clearance_order_proof.md` + `lean/clearance_order.lean` |
| **Input files** | `numerics/unified_cvb_clearance_v2.py` (1,500 lines, especially the organ parameters dict), `results/pattern_005_corrected_clearance_order.md` |
| **What output should demonstrate** | (1) The ordering liver < pericardium < heart < CNS < gut < pancreas < muscle < testes holds for all parameter values within +/-30% of central estimates; (2) Identify the minimum perturbation that changes the ordering; (3) Patient-specific scenarios where order differs. |
| **Priority** | HIGH |
| **Estimated effort** | 1 round |

## Request 5: Convergence Synthesis

| Field | Value |
|-------|-------|
| **File to create** | `attempts/attempt_xxx_convergence_synthesis.md` |
| **Input files** | `CONVERGENCE.md`, `CAMPAIGN_SUMMARY.md`, `CROSS_POLLINATION.md`, `results/campaign_inventory_v2.md`, all `results/pattern_*.md` files |
| **What output should demonstrate** | Publication-ready narrative: one virus (CVB), one mechanism (TD mutant persistence), one protocol (fluoxetine + FMD + supplements), twelve diseases, validated by 46 computational models with 78% cross-validation concordance. Should include formal statement of the central thesis, evidence grades for each sub-claim, and identification of the weakest links. |
| **Priority** | HIGH |
| **Estimated effort** | 2 rounds |

## Request 6: Non-Progressor Formalization

| Field | Value |
|-------|-------|
| **File to create** | `t1dm/attempts/attempt_065_non_progressor_formalization.md` |
| **Input files** | `t1dm/numerics/non_progressor_profile.py` (942 lines), `t1dm/results/pattern_002_anti_problem.md`, `numerics/anti_problem_cross_disease.py` (853 lines) |
| **What output should demonstrate** | The protocol state vector at month 12 is epsilon-close to the non-progressor steady state in all 9 state variables. Define epsilon. Prove convergence. |
| **Priority** | HIGH |
| **Estimated effort** | 1 round |

## Request 7: Disease Network Formalization

| Field | Value |
|-------|-------|
| **File to create** | `attempts/attempt_xxx_disease_network_formalization.md` |
| **Input files** | `numerics/disease_network.py` (957 lines), `results/pattern_008_disease_network.md` |
| **What output should demonstrate** | (1) Formal graph-theoretic proof that myocarditis is the keystone node (highest betweenness centrality); (2) Prove vaccination at root eliminates all downstream paths; (3) Prove the cascade probability from acute CVB to any terminal disease (T1DM, DCM, ME/CFS). |
| **Priority** | MEDIUM |
| **Estimated effort** | 1 round |

## Request 8: Safety Formalization

| Field | Value |
|-------|-------|
| **File to create** | `attempts/attempt_xxx_safety_bounds.md` |
| **Input files** | `numerics/drug_interactions.py` (1,472 lines), `numerics/safety_pharmacology.py` (1,386 lines), `results/pattern_007_safety_profile.md` |
| **What output should demonstrate** | Formal bounds on DKA probability during fasting as a function of (basal_insulin_fraction, fasting_duration, residual_beta_cell_mass). Prove that 24h fast at 80% basal keeps BHB < 3.0 mM with probability > 99% for all T1DM patients with residual beta cell mass > 0.01. |
| **Priority** | MEDIUM |
| **Estimated effort** | 1 round |

---

# SECTION 4: OPEN QUESTIONS

## Questions the ODD Instance Could Not Answer Computationally

### Q1: Is the fluoxetine-CVB IC50 really 1 uM in vivo?
**Status**: Zuo 2018 reports ~1 uM in cell culture. Protein binding (97% for fluoxetine) means free drug is ~3% of total. But fluoxetine accumulates intracellularly via lysosomotropic trapping (pKa 10.05), which may compensate. The ODD instance used the in vitro IC50 for the unified model and a higher in vivo estimate for dedicated models. Resolution requires pharmacokinetic first principles, not more Monte Carlo.

### Q2: Do TD mutants undergo autophagy at the same rate as wild-type?
**Status**: The model assumes yes (same autophagy susceptibility). If TD mutants have altered autophagy susceptibility (e.g., 5' deletion affects autophagosome targeting), clearance timelines could be significantly longer. No experimental data distinguishes TD vs WT autophagy rates. This is an EXPERIMENTALLY OPEN question.

### Q3: Is there a third viral population beyond WT and TD?
**Status**: The model uses two populations (WT + TD). Some evidence suggests ultra-persistent deep-compartment virus (e.g., in autonomic ganglia, bone marrow) that may be neither WT nor classical TD. If this population exists and is drug-resistant, the protocol may suppress but not eradicate. Unknown.

### Q4: Does the protocol work for 67-year-duration T1DM?
**Status**: Most T1DM regeneration data comes from recent-onset (< 5 years). the patient has 67 years of disease. Butler 2005 shows residual beta cells even after 50+ years, but regenerative CAPACITY may be lower. The model predicts it works (R > D achievable even at B_0 = 0.03), but there is no clinical precedent for this duration.

### Q5: What is the true two-population fraction (sensitive vs resistant TD)?
**Status**: The CNS and orchitis dedicated models use 85:15 (sensitive:resistant) based on Chapman 2008 data on deletion lengths. This fraction significantly affects clearance tail dynamics but has not been measured organ-by-organ in humans.

## Questions That Need Literature Review (theory track Strength)

### Q6: Has anyone measured fluoxetine concentration in human pancreatic tissue?
**Status**: We have 19F-MRS data for brain (Bolo 2000, Karson 1993), tissue distribution data for testes (Tanrikut 2010), but no direct measurement for pancreas. The model uses a low estimate (sub-IC50 at standard doses), relying on autophagy for pancreatic clearance. If pancreatic fluoxetine is higher than expected, clearance would be faster.

### Q7: What is the state of CVB vaccine clinical trials?
**Status**: The ODD instance modeled vaccine impact assuming 85% efficacy. Soppela VLP-deltaVP4 is in preclinical. Are there any Phase I trials? mRNA candidates? This affects the "long-term endgame" timeline.

### Q8: Has anyone tested fluoxetine in a CVB animal model since Zuo 2018?
**Status**: Zuo 2018 is the primary reference. If there are follow-up studies (positive or negative), they would directly affect the central claim.

### Q9: What is the current status of pocapavir clinical availability?
**Status**: Pocapavir is listed in the encephalitis emergency protocol. Is it accessible via compassionate use? FDA expanded access? Or still research-only?

### Q10: Are there any case reports of SSRI-prescribed patients with unexpected CVB disease outcomes?
**Status**: This is the observational analog of the proposed pericarditis retrospective. If any clinician has noticed that their SSRI patients have fewer enteroviral complications, it would be anecdotal but directionally important.

## Questions That Need Experimental Data (Neither Instance Can Answer)

### Q11: Does fluoxetine actually inhibit CVB replication in human tissue explants?
**Status**: Cell culture (Zuo 2018) is not the same as tissue. An ex vivo study using human cardiac/pancreatic tissue explants with CVB infection + fluoxetine would be definitive. This is a wet-lab experiment.

### Q12: Can TD mutant clearance be measured in a patient on protocol?
**Status**: If the patient starts the protocol and provides stool/blood samples for enteroviral PCR at baseline and monthly, we could directly measure whether TD mutant shedding declines. This requires a patient and a lab.

### Q13: What is the patient's actual C-peptide, HLA type, and CVB serology?
**Status**: The model uses estimates (B_0 = 0.08, assumed DR3/DR4). Actual lab values would allow patient-specific model calibration. This requires a blood draw.

### Q14: Is there a detectable enteroviral signal in the patient's stool or blood?
**Status**: If CVB TD mutants are present, enteroviral RNA should be detectable by RT-PCR (possibly at low copy number). A positive result would confirm the central hypothesis for this patient. A negative result would not disprove it (sampling sensitivity is imperfect).

---

# SECTION 5: THE PATH TO PUBLICATION

## Which Findings Are Publishable?

### Tier 1: Immediately Publishable (computational biology paper)

**Paper 1: "One Virus, Twelve Diseases: A Unified Computational Model of Coxsackievirus B Persistence and Multi-Organ Pathogenesis"**

Content:
- The unified 8-compartment ODE model (v2)
- Cross-validation against 7 dedicated organ models (78% concordance)
- The corrected PK: 8/8 organs clearable (vs previous 6/8)
- The HLA paradox: genetic risk anti-correlation between T1DM and cardiac disease
- The clearance ordering and minimum effective protocol
- All 46 scripts available as supplementary code

Strength: Novel computational framework, no experimental claims, all code reproducible.
Weakness: No clinical validation. Purely in silico.

**Target**: PLOS Computational Biology, Journal of Theoretical Biology, or bioRxiv preprint.

### Tier 2: Publishable If Supported By Observational Data

**Paper 2: "Fluoxetine as an Antiviral Against Persistent Enteroviral Infection: Pharmacokinetic Modeling and Clinical Implications"**

Content:
- Fluoxetine tissue PK (brain 15x, testes 2.5x, per-organ Hill curves)
- IC50 analysis for all 8 compartments
- Predicted clearance timelines
- Proposed clinical trial design (pericarditis as proof-of-concept)

Would be strengthened by: SSRI-pericarditis retrospective database analysis (REQ-007), any animal model data.

**Paper 3: "The HLA Paradox in Coxsackievirus B Disease: Genetic Risk Profiles Across 12 Diseases"**

Content:
- HLA risk model with population Monte Carlo
- Negative T1DM-cardiac correlation
- Screening algorithm
- Cost-effectiveness of HLA-guided screening

Would be strengthened by: Clinical cohort data confirming the negative correlation.

### Tier 3: Publishable If the patient Starts Protocol

**Paper 4: Case Report — "Antiviral-Based Protocol for Long-Duration Type 1 Diabetes: A Single-Patient Proof-of-Concept"**

Content:
- Protocol design rationale
- Baseline labs (C-peptide, HLA, CVB serology, cardiac markers)
- Monthly monitoring data (C-peptide trajectory, autoantibodies, CVB PCR)
- Comparison to model predictions

Requirements: the patient's consent, physician supervision, IRB or equivalent ethics review, 6-12 months of data.

## What Format?

| Paper | Format | Venue | Timeline |
|-------|--------|-------|----------|
| Paper 1 (Unified model) | Full research article | PLOS Comp Biol / bioRxiv preprint | Can submit after theory track formalization (2-3 rounds) |
| Paper 2 (Fluoxetine PK) | Short communication / letter | Antiviral Research | Needs SSRI retrospective data first |
| Paper 3 (HLA paradox) | Research article | HLA journal / Immunogenetics | Can submit after formalization |
| Paper 4 (Case report) | Case report | BMJ Case Reports / NEJM correspondence | Needs 6-12 months of patient data |

## What Additional Validation Would Reviewers Require?

1. **For Paper 1 (computational)**: Sensitivity analysis showing robustness to +/-50% parameter variation (ODD instance has +/-30%; needs extension). Comparison to at least one published enteroviral ODE model. Discussion of model limitations (single-strain, no spatial heterogeneity, no stochastic effects).

2. **For Paper 2 (fluoxetine)**: Reviewers will want animal model data or at minimum retrospective human data. The SSRI-pericarditis database query (REQ-007) would partially satisfy this.

3. **For Paper 3 (HLA)**: Reviewers will want validation against a clinical cohort. Need a dataset of HLA-typed patients with CVB disease outcomes.

4. **For Paper 4 (case report)**: Standard case report requirements: informed consent, ethics approval, complete lab data, honest reporting of all outcomes including failures.

---

# APPENDIX: FILE REFERENCE MAP

For the theory track's convenience, here is where to find everything:

## Root-Level Documents (read these first)
- `CONVERGENCE.md` -- Disease hierarchy, shared protocol, trial roadmap
- `CAMPAIGN_SUMMARY.md` -- After 11 theory track runs, campaign status
- `CROSS_POLLINATION.md` -- How each disease informs the others
- `MEDICAL_PROBLEMS.md` -- Master problem list
- `DRUG_SAFETY_MATRIX.md` -- All drug interactions including itraconazole-colchicine CRITICAL warning
- `EVIDENCE_GRADES.md` -- Every claim graded A-E
- `FAILURE_MODES.md` -- 6 pre-registered failure modes, 92.5% at least one arm works
- `PATIENT_ZERO_TIMELINE.md` -- Week-by-week implementation
- `ODD_INSTANCE_REQUESTS.md` -- 11 computational requests (REQ-001 through REQ-011, partially completed)

## ODD Instance Core Outputs (read these for the numerics)
- `results/pattern_005_corrected_clearance_order.md` -- THE key result: 8/8 clearable
- `results/pattern_007_safety_profile.md` -- Safety: 36 interactions, DKA model
- `results/pattern_009_genetic_risk_landscape.md` -- HLA paradox
- `results/pattern_010_serotype_disease_map.md` -- Serotype tropism
- `results/cross_validation_report.md` -- 78% concordance, 5 divergences explained
- `results/campaign_inventory_v2.md` -- Complete inventory (THIS is the master index)

## The Critical Scripts (if the theory track wants to verify numerics)
- `numerics/unified_cvb_clearance_v2.py` -- The unified model (1,500 lines)
- `numerics/cross_validate_models.py` -- Cross-validation (1,143 lines)
- `numerics/hla_risk_model.py` -- HLA paradox model (1,089 lines)
- `numerics/protocol_implementation.py` -- Full protocol specification (1,781 lines)
- `t1dm/numerics/beta_cell_dynamics.py` -- R > D inequality model (1,530 lines)

---

*End of theory track Handoff. The ODD instance has mapped ~80% of the noise space. The remaining 20% is edge cases and refinements. The theory track's job is to take these numerical findings and forge them into formal proofs, certified claims, and publication-ready documents.*

*ODD Instance, signing off.*
