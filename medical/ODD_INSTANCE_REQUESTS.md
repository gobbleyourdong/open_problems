# numerical track Request Queue — Computational / Numerical Tasks

> These are tasks identified by the theory track that require brute-force computation, data analysis, structural biology, or numerical work. The numerical track should work through these in priority order.

## Priority 1: Immediate Value

### REQ-001: CVB3 2A Protease Virtual Drug Screen
**Source**: myocarditis/attempts/attempt_002_2a_protease_inhibitor.md
**Task**:
1. Download CVB3 2A protease crystal structure from PDB
2. Characterize active site: pocket volume, electrostatic surface, H-bond donors/acceptors
3. Virtual screen FDA-approved drugs (DrugBank ~2,600 approved drugs) against 2A active site
4. Use AutoDock Vina or similar docking software
5. Rank hits by predicted binding affinity (kcal/mol)
6. Cross-reference with drugs safe in cardiac patients
7. Specifically test: rupintrivir analogs, HIV protease inhibitors, cysteine protease inhibitors
**Output**: `myocarditis/numerics/2a_protease_screen/` — docking results, top 20 hits with structures and predicted affinities
**Why**: A 2A inhibitor would immediately stop dystrophin cleavage in cardiac patients. If an existing drug hits, it's testable tomorrow.

### REQ-002: Pleurodynia-T1DM Epidemiological Cross-Correlation
**Source**: pleurodynia/attempts/attempt_002_epidemiological_correlation.md
**Task**:
1. Pull CDC NREVSS enteroviral surveillance data by year, serotype, region (1970-present if available)
2. Pull SEARCH/EURODIAB T1DM incidence data by year, age, region
3. Compute cross-correlation: Corr[enteroviral_cases(region, year), T1DM_incidence(region, year+τ)] for τ = 0-10 years
4. Generate heat map: correlation strength × lag × region
5. Test Bornholm Island specifically if Danish data accessible
6. Test seasonal signal: summer/fall enteroviral peaks vs winter T1DM diagnosis peaks
**Output**: `pleurodynia/numerics/epi_correlation/` — correlation matrices, heat maps, statistical tests
**Why**: If positive, this is the strongest population-level evidence for CVB→T1DM causation. Uses existing data, no new collection needed.

## Priority 2: Structural Biology

### REQ-003: Dystrophin Hinge 3 Cleavage Site Analysis
**Source**: dilated_cardiomyopathy/anti_problem.md
**Task**:
1. Get human dystrophin protein sequence (UniProt P11532)
2. Identify hinge 3 region (AA ~2000-2100)
3. Map the 2A protease cleavage site (GxxG motif)
4. Check for known polymorphisms in this region (dbSNP, gnomAD)
5. Model cleavage efficiency for each variant (if structural data allows)
6. Cross-reference: do any variants have known associations with cardiac outcomes?
**Output**: `dilated_cardiomyopathy/numerics/dystrophin_hinge3/` — sequence analysis, variant catalog, structural predictions
**Why**: If common polymorphisms affect cleavage susceptibility, this explains why only some myocarditis patients progress to DCM.

### REQ-004: CVB Serotype Conservation Analysis for Vaccine Design
**Source**: CVB_VACCINE_STRATEGY.md
**Task**:
1. Align VP1-VP3 sequences across all CVB1-5 serotypes (all available isolates)
2. Map conserved vs variable regions
3. Identify conserved neutralizing epitopes (cross-reactive between serotypes)
4. Compare VP4 across serotypes (the ADE-mediating protein excluded from VLP-ΔVP4)
5. Predict optimal multivalent vaccine insert: which VP1/VP2/VP3 regions cover all 5 serotypes?
**Output**: `neonatal_sepsis/numerics/vaccine_antigen_design/` — alignments, conservation maps, epitope predictions
**Why**: Informs the CVB vaccine antigen design. Conserved epitopes enable a single vaccine covering all serotypes.

## Priority 3: PK/PD Modeling

### REQ-005: Fluoxetine Tissue Distribution Model
**Source**: orchitis/attempts/attempt_001_reservoir_clearance.md, models/cvb_persistence_universal.md
**Task**:
1. Compile published fluoxetine tissue distribution data (autopsy studies, animal PK)
2. Model steady-state fluoxetine concentrations in:
   - Pancreas, heart, skeletal muscle, brain, liver, testes, pericardium
3. Compare tissue concentrations to CVB 2C ATPase IC50 (~10 μM estimated)
4. Identify any organs where fluoxetine concentration < IC50 (potential clearance gaps)
5. Model time to steady state in each tissue compartment
**Output**: `t1dm/numerics/fluoxetine_tissue_pk/` — tissue concentration predictions, PK model parameters
**Why**: Confirms whether 20mg oral fluoxetine achieves antiviral concentrations in ALL CVB-affected organs. If any organ falls short, dose adjustment or additional antiviral needed.

### REQ-006: FMD Autophagy Kinetics
**Source**: me_cfs/models/vicious_cycle.md
**Task**:
1. Compile autophagy flux measurements during fasting in humans (LC3-II/I ratio, p62 degradation)
2. Model autophagy activation kinetics: time from fasting onset to peak autophagy
3. Estimate TD mutant clearance rate during peak autophagy vs baseline
4. Model: how many FMD cycles to reduce TD mutant load by 90%? 99%?
5. Does time-restricted eating (16:8) provide significant autophagy vs full 5-day FMD?
**Output**: `me_cfs/numerics/autophagy_kinetics/` — clearance rate models, FMD vs TRE comparison
**Why**: Determines optimal fasting protocol intensity/frequency. ME/CFS patients may not tolerate full FMD — need to know if TRE is sufficient.

## Priority 4: Data Mining

### REQ-007: SSRI-Pericarditis Retrospective Database Query
**Source**: pericarditis/anti_problem.md
**Task**:
1. Design query for claims database (Optum, Truven, or similar):
   - Patients with ICD-10 I30.x (pericarditis) + at least 1 recurrence within 18 months
   - Stratify by SSRI prescription at time of first episode
   - Compare recurrence rates: SSRI-prescribed vs non-SSRI
   - Specifically isolate fluoxetine (most CVB-active SSRI)
2. Control for: age, sex, colchicine use, NSAID use, comorbidities
3. Sensitivity analysis: any SSRI vs fluoxetine specifically vs no SSRI
**Output**: `pericarditis/numerics/ssri_retrospective/` — query design, expected effect size, power calculation
**Why**: If fluoxetine-prescribed pericarditis patients have lower recurrence, this is observational evidence for antiviral effect. Can be done with EXISTING data, no new study needed.

### REQ-008: Butler Autopsy Data Re-Analysis
**Source**: t1dm/THEWALL.md (beta cell regeneration claim)
**Task**:
1. Obtain Butler 2003/2005 autopsy datasets (if published/available)
2. Re-analyze: beta cell mass vs disease duration, stratified by age at onset
3. Fit regeneration rate model: estimate k_regen from cross-sectional autopsy data
4. Can we extract an estimate of Destruction rate from the data?
5. What is the implied Regeneration/Destruction ratio at different disease durations?
**Output**: `t1dm/numerics/butler_reanalysis/` — fitted models, regeneration rate estimates
**Why**: Validates the core T1DM inequality model (R vs D) with real human data.

## Priority 5: Additional Requests (from EVEN runs 8-11)

### REQ-009: Keshan-Finland Selenium-T1DM Correlation
**Source**: myocarditis/attempts/attempt_004_keshan_disease.md
**Task**:
1. Compile soil selenium concentrations by region (Finland, Sweden, Denmark, Norway, UK, Germany)
2. Compile T1DM incidence by region (EURODIAB data)
3. Compile dates of national selenium supplementation programs (Finland 1984, others)
4. Correlate: selenium soil levels vs T1DM incidence by country/region
5. Test: did Finnish T1DM incidence growth slow after 1984 selenium fertilizer program?
6. Compare with countries that did NOT supplement selenium
**Output**: `myocarditis/numerics/keshan_finland/` — correlation analysis, time series plots
**Why**: If selenium-poor regions have higher T1DM, strengthens the Keshan-like mechanism for T1DM. Grade B evidence if confirmed.

### REQ-010: Liver-First Clearance Model Simulation
**Source**: hepatitis/models/portal_gatekeeper.md
**Task**:
1. Build a compartmental PK/PD model: gut → portal vein → liver → systemic → organs
2. Parameters: Kupffer cell extraction rate, hepatocyte infection rate, viral replication rate, fluoxetine tissue distribution
3. Simulate: viral load in each compartment over 12 weeks with fluoxetine 20mg
4. Test prediction: liver clears first → systemic viremia drops → organ-specific clearance follows
5. Sensitivity analysis: which parameter most affects clearance timeline?
**Output**: `hepatitis/numerics/liver_first_model/` — compartmental model code, simulation results
**Why**: Validates the predicted organ clearance sequence. If the model shows liver-first clearance, it supports the ALT-before-CRP prediction in PATIENT_ZERO_TIMELINE.

### REQ-011: ME/CFS Bistability Phase Portrait
**Source**: me_cfs/models/vicious_cycle.md
**Task**:
1. Implement the 6-variable coupled ODE system (V, I, N, M, A, F) with estimated parameters
2. Find the two stable steady states (disease and health) numerically
3. Plot phase portraits (2D projections: V vs N, V vs F, N vs M)
4. Identify the separatrix (unstable manifold between attractors)
5. Simulate: protocol intervention (step changes to parameters at t=0) — does the system cross the separatrix?
6. Sensitivity: which intervention has the largest effect on crossing the threshold?
**Output**: `me_cfs/numerics/bistability_model/` — ODE code, phase portraits, sensitivity analysis
**Why**: Moves the vicious cycle model from qualitative to quantitative. Identifies which protocol component is most critical for flipping the system to the health attractor.

### REQ-012: Eczema/Psoriasis Treg Bistability Model
**Source**: eczema/attempts/attempt_004_bioinformatics_relevance.md, psoriasis/attempts/attempt_004_bioinformatics_relevance.md
**Task** (eczema):
1. Implement 2-variable ODE: dT/dt (Treg dynamics), d(Th2)/dt (Th2 dynamics)
2. Parameters from dupilumab trial data + vitamin D/butyrate supplementation studies
3. Find stable steady states (eczema = high Th2, remission = high Treg)
4. Plot phase portrait and separatrix
5. Simulate protocol intervention: vitamin D + butyrate → Treg increase → does system cross separatrix?
6. Compare predicted EASI improvement to published dupilumab EASI response (60% at 16 weeks)

**Task** (psoriasis):
1. Same structure but Treg vs Th17 (not Th2)
2. Parameters from PALACE trial data (apremilast) + butyrate/VitD studies
3. Test: protocol alone vs protocol + apremilast (30mg BID)
4. Predict PASI improvement vs published biologic data

**Output**: `eczema/numerics/bistability_model/`, `psoriasis/numerics/bistability_model/`
**Why**: Quantifies the bistability hypothesis for co-beneficiary diseases. Determines whether the protocol alone can cross the separatrix or whether apremilast is required for psoriasis. Simpler than the ME/CFS 6-variable model — a good calibration target.

### REQ-017: GSE247805-247808 CVB4 vs SARS-CoV-2 Islet Organoid Comparison
**Script**: `numerics/analyze_gse247805_cvb_sars_comparison.py` (written this session)
**Data**: `numerics/transcriptomics/GSE247805_series_matrix.txt` (on disk)
**Primary question**: Do BOTH CVB4 AND SARS-CoV-2 suppress LAMP2 in the same system?
  - YES → Long COVID LAMP2 bridge validated → trehalose indicated for ~100M Long COVID patients
  - NO → mechanism differs → different implications for Long COVID arm
**Also check**: FOXP1, DMD, ACE2 vs CXADR dynamics
**Output**: `results/gse247805_cvb_sars_comparison.json`, `results/pattern_020_cvb_sars_lamp2_convergence.md`
**Priority**: HIGH (Long COVID bridge validation)

### REQ-016: GSE57781 Cardiac CVB3 Analysis — DMD + LAMP2 in Human Cardiomyocytes
**Source**: numerics/analyze_gse57781_cardiomyocytes.py (script written), numerics/transcriptomics/GSE57781_series_matrix.txt (data on disk)
**Task**:
1. Run `python3 numerics/analyze_gse57781_cardiomyocytes.py`
2. Note: microarray — probe ID matching may need GPL platform annotation file
3. Download GPL annotation from GEO page for GSE57781 → map probe IDs → gene symbols
4. Key questions: (a) DMD suppressed in CVB3 cardiomyocytes? (b) LAMP2 suppressed? (c) FOXP1 suppressed? (d) Cardiac-specific effects (SCN5A, TNNT2, MYH7)?

**Why CRITICAL**: GSE184831 confirmed DMD -32× in pancreatic PANC-1 cells. Confirmation in CARDIAC cells upgrades from Grade B to Grade A- for the myocarditis/DCM mechanism. Critical for the paper.
**Output**: `results/gse57781_cardiac_cvb3_analysis.json`, `results/pattern_019_cardiac_cvb3_transcriptomics.md`
**Priority**: HIGH (needed before paper submission)

### REQ-015: Long COVID cfRNA Validation — Does ORF9b Suppress LAMP2 Like CVB?
**Source**: me_cfs/attempts/attempt_005_long_covid_lamp2_convergence.md
**Task**:
1. Search GEO and literature for Long COVID cfRNA or tissue expression datasets with LAMP2 measured
2. If found: compare LAMP2 expression in Long COVID patients vs healthy controls (same approach as GSE184831)
3. Search for published LAMP2 quantification in Long COVID tissue (post-mortem lung, autopsy brain, or BAL)
4. Cross-reference with: Guo et al. 2021 (Cell Reports, PMID:34186035) — ORF9b LAMP2 suppression in vitro
5. If GEO datasets exist: download + analyze (same pipeline as transcriptomics analyses)

**Primary question**: Is LAMP2 suppressed in Long COVID tissue to a similar degree as CVB in GSE184831 (-2.7×)?
- If yes: mechanistic confirmation → trehalose is indicated for Long COVID
- If no: the mechanism differs from CVB (could still work via other routes)

**Output**: `me_cfs/results/pattern_018_long_covid_lamp2_validation.md` (or indicate no data available)
**Why**: If confirmed, this extends the campaign's trehalose recommendation to ~100M Long COVID patients with mechanistic backing. Could justify an NIH RECOVER grant application.

### REQ-013: GSE274264 scRNA-seq Primary Human Islet Analysis
**Source**: numerics/analyze_gse274264_scrnaseq.py (analysis script ready), numerics/transcriptomics/GSE274264/ (data downloaded)
**Task**:
1. Run `python3 numerics/analyze_gse274264_scrnaseq.py` (install: pip install scanpy anndata)
2. This is scRNA-seq from primary human pancreatic islets (multiple donors, 24hr + 48hr, CVB3 vs control)
3. Primary questions: (a) Is FOXP1 suppressed in primary human islets? (b) Is LAMP2 suppressed? (c) Is DMD destroyed? (d) Cell-type-specific responses (beta vs alpha vs delta)?
4. If FOXP1 is suppressed in primary tissue: FOXP1 mechanism upgrades from B- to A- (cell line data → primary human tissue data)
5. If LAMP2 is suppressed in primary tissue: trehalose protocol addition is validated in human tissue

**Output**: `results/gse274264_primary_islet_analysis.json`, `results/pattern_018_primary_islet_scrnaseq.md`
**Priority**: CRITICAL — primary human islet data is the highest-quality evidence in the campaign. Every confirmed finding upgrades from "cell line data" to "human tissue data."

### REQ-014: Unified CVB Clearance Model v4 — LAMP2-Corrected
**Source**: t1dm/attempts/attempt_080_lamp2_clearance_order_theory.md, orchitis/attempts/attempt_003, hepatitis/attempts/attempt_003, encephalitis/attempts/attempt_003
**Task**:
1. Update `numerics/unified_cvb_clearance_v2.py` (or create v4) to incorporate organ-specific LAMP2 correction factors:
   - `LAMP2_BASELINE = {'liver': 4.0, 'pericardium': 1.5, 'heart': 1.0, 'gut': 1.2, 'pancreas': 0.8, 'brain_glia': 0.9, 'brain_neuron': 0.6, 'muscle': 0.7, 'testes': 0.4}`
   - `kappa_effective(organ) = LAMP2_BASELINE[organ] / 2.7`  (2.7 = CVB suppression factor from GSE184831)
   - With trehalose: `kappa_trehalose(organ) = kappa_effective + 0.35` (estimated TFEB correction)
2. For CNS: split into two sub-compartments (glial κ=0.67 vs neuronal κ=0.22) with separate clearance curves
3. Re-run cross-validation: does LAMP2-corrected model produce better agreement with dedicated models?
4. Generate updated clearance tables: without trehalose, with trehalose
5. Sensitivity analysis: how much does trehalose correction matter at ±50% of estimated correction factor?

**Output**: `numerics/unified_cvb_clearance_v4.py`, `results/pattern_019_lamp2_corrected_clearance_v4.md`
**Why**: v2 diverges 4.5× for testes and 3.4× for CNS. v4 with LAMP2 correction should reproduce dedicated model results. This is the most important model improvement since v2.

## Formatting for numerical track

Each request should result in:
- Code in `[disease]/numerics/[task_name]/`
- Results summary in `[disease]/results/[task_name]_results.md`
- Raw data/figures in `[disease]/results/[task_name]/`
- The theory track will pick up results and formalize findings
