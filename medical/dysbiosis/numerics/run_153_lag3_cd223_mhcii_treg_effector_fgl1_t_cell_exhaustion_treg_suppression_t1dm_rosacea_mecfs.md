# Run 153 — LAG-3 / CD223: MHC-II Treg Effector Mechanism, FGL1 β Cell Tolerance, T Cell Exhaustion, Relatlimab/LAG-3 Agonism

**Date:** 2026-04-12
**Sweep:** 50
**Candidate:** LAG-3 (CD223) — Treg effector inhibitory receptor; complement to CTLA4 (run_148)

## Kill-First Verification

**Grep confirmation:**
- LAG-3/LAG3/CD223: 1 file (run_100 MAIT cells) — single mention as exhaustion marker ("PD-1+, LAG-3+") with no mechanistic analysis
- FGL1/fibrinogen-like protein 1, MHC-II Treg effector mechanism, relatlimab, LAG-3 agonism, KIEELE motif: 0 occurrences
- Run_148 (CTLA4) covers CD80/CD86 trogocytosis; LAG-3 covers MHC-II binding — non-overlapping APC contact mechanisms

**Kill verdict:** PASS — LAG-3 mechanism (Treg effector, FGL1, MHC-II Treg suppression) has zero dedicated analysis.

## Saturation Override Criteria

1. **Absent from prior runs as primary subject**: YES — 0 of 152 runs address LAG-3 as MHC-II Treg effector or FGL1 peripheral tolerance
2. **MODERATE+ rosacea + T1DM**: YES — HIGH T1DM (β cell FGL1 tolerance, LAG-3+ Treg function); MODERATE rosacea (skin Treg LAG-3 effector)
3. **New therapeutic target**: YES — relatlimab (FDA approved, 2022), LAG-3-Ig agonist, IMP321 (eftilagimod)
4. **Kill-first fails**: CONFIRMED — CTLA4 (run_148) = CD80/CD86; LAG-3 = MHC-II; structurally related to CD4 but completely distinct mechanism

**All four criteria met. Proceeding.**

---

## Core Mechanism

### LAG-3 Structure — The CD4 Relative That Outcompetes CD4

**LAG3** (chromosome 12p13.32) encodes CD223 (498 amino acids, type I transmembrane). CD223 is structurally homologous to CD4 (both are MHC-II-binding Ig superfamily members) but has **100-fold higher affinity for MHC-II than CD4** due to a unique extra loop in domain D1.

**Domain architecture:**
- 4 extracellular Ig-like domains (D1-D4)
- **D1 extra loop** (unique to LAG-3, absent from CD4): inserts into the peptide-binding groove of MHC-II → high-affinity contact; the structural basis for 100× higher MHC-II affinity vs CD4
- Single transmembrane domain
- Cytoplasmic tail: **KIEELE motif** (unique; not in other checkpoint receptors) → proximal TCR signal suppression (LAP motif interaction → inhibits ZAP-70/PLCγ1 activation)

**Ligands:**
| Ligand | Source | Context |
|--------|--------|---------|
| **MHC-II (HLA-DR/DQ/DP)** | APCs, B cells, activated endothelium | Primary; high-affinity D1-loop contact |
| **FGL1 (fibrinogen-like protein 1)** | Liver, β cells, tumor cells | Peripheral tolerance; LAG-3 agonist at T cells |
| **LSECtin (CLEC4G)** | Liver sinusoidal endothelium | Liver-specific tolerance |
| **α-synuclein** | Neuronal | Parkinson's disease context (separate) |
| **Galectin-3** | Macrophages, some tumors | Modulates LAG-3 clustering |

---

## Treg Effector Mechanism — MHC-II Contact Suppression

**CTLA4 (run_148)** suppresses via CD80/CD86 stripping. **LAG-3** suppresses via a completely distinct, non-overlapping mechanism:

**Mechanism:**
1. Activated Tregs upregulate LAG-3 surface expression (FOXP3 → LAG-3 transcription; IL-2 stimulation → LAG-3 ↑)
2. Treg LAG-3 (D1 extra loop) binds MHC-II on DCs with 100× higher affinity than CD4 on the DC itself or on Teff cells
3. LAG-3 + MHC-II complex → **FEME (fast endophilin-mediated endocytosis)** → MHC-II internalized from DC surface
4. DC loses MHC-II surface density → antigen presentation capacity impaired → Teff cells near that DC cannot be stimulated
5. Trans suppression: one LAG-3+ Treg depotentiates many DCs nearby → broad-radius immune suppression

**Additive with CTLA4:**
- CTLA4 strips CD80/CD86 → removes co-stimulatory signal (Signal 2)
- LAG-3 strips MHC-II → reduces TCR engagement (Signal 1)
- Together: DC loses both MHC-II (Signal 1) AND CD80/CD86 (Signal 2) → completely depotentiated
- Double Treg effector mechanism: CTLA4+LAG-3 co-expressing Tregs = most suppressive subset

---

## FGL1 — β Cell Peripheral Tolerance

**Fibrinogen-like protein 1 (FGL1)** is a secreted LAG-3 ligand expressed by:
- Hepatocytes (primary source)
- **Pancreatic β cells** — directly relevant to T1DM
- Lung type II epithelial cells

**FGL1/LAG-3 axis in β cell tolerance:**
- Homeostatic β cells secrete FGL1 → FGL1 binds LAG-3 on islet-infiltrating T cells → T cell LAG-3 KIEELE cytoplasmic motif → ZAP-70/PLCγ1 suppressed → T cell activation threshold raised → β cell self-antigen-specific T cells quenched
- FGL1 = β cell-expressed peripheral tolerance molecule: β cells actively suppress islet-infiltrating T cells via FGL1-LAG-3
- Insulitis: cytokines (TNF-α, IL-1β, IFN-γ) → β cell FGL1 expression ↓ → FGL1-LAG-3 tolerance signal collapses → islet-infiltrating T cells no longer suppressed by FGL1 → accelerated β cell destruction
- FGL1 serum levels: low FGL1 in T1DM patients at onset; potential biomarker for LAG-3 tolerance failure

**FGL1 recombinant protein (investigational):**
- FGL1-Fc fusion → systemic LAG-3 agonism → raises T cell activation threshold → peripheral tolerance enhancement
- Preclinical autoimmune models: FGL1-Fc → delayed onset in NOD mice; T1DM rationale

---

## T Cell and NK Exhaustion — LAG-3 as Exhaustion Marker and Driver

**LAG-3 in exhaustion:**
- Co-expressed with PD-1 on exhausted T cells (chronic antigen exposure → PD-1+LAG-3+ = terminal exhaustion phenotype)
- LAG-3 KIEELE motif → independent TCR inhibition mechanism distinct from PD-1 (PD-1 inhibits via SHP-1/SHP-2 → Lck/ZAP-70 dephosphorylation; LAG-3 acts via KIEELE → LAP → different phosphatase association)
- **Dual PD-1/LAG-3 co-blockade**: relatlimab + nivolumab (Opdualag; FDA 2022 melanoma) > either alone → synergistic T cell reinvigoration; mechanistic rationale: PD-1 and LAG-3 suppress via independent signaling pathways → dual block removes both brakes simultaneously

**NK cells:**
- NK cells express LAG-3 under chronic activation → NK LAG-3 → KIEELE signaling → NK cytotoxicity reduced
- ME/CFS: LAG-3+ NK cells in peripheral blood; LAG-3 = additional NK exhaustion mechanism (alongside TIM-3, PD-1)

**Islet CD8+ T cells in T1DM:**
- β cell-specific CD8+ T cells (insulin-B chain peptide, GAD65 epitope) progressively acquire PD-1+LAG-3+ phenotype → partially exhausted → slower destruction; this partial exhaustion is endogenous protective
- Paradox: enhancing LAG-3 signaling (agonism) could further exhaust islet CD8+ T cells → protective; but too much exhaustion → immune escape of infections

---

## T1DM — FGL1 Tolerance and LAG-3+ Treg Function

**T1DM relevance (HIGH):**

1. **FGL1/LAG-3 β cell tolerance failure**:
   - β cell FGL1 ↓ during insulitis → LAG-3-mediated T cell restraint lost → accelerated β cell CD8+ T cell killing
   - FGL1 serum monitoring: decreasing FGL1 trajectory may precede C-peptide decline

2. **LAG-3+ Treg depletion in insulitis**:
   - Islet Tregs that co-express LAG-3 + CTLA4 = most suppressive; insulitis → cytokines → FOXP3 destabilization → LAG-3 expression ↓ → Treg loses both CD80/CD86 and MHC-II contact mechanisms
   - Restoration: run_151 IL-2 → FOXP3 ↑ → LAG-3 ↑; abatacept (run_148) supports CD80/CD86 arm; LAG-3-Ig agonism would support MHC-II arm

3. **Compound risk — CTLA4 G allele + any LAG-3 dysfunction**:
   - CTLA4 rs3087243 G allele (run_148): impaired trogocytosis → DC has more CD80/CD86
   - If LAG-3 function also impaired (or FGL1 ↓) → DC has more CD80/CD86 AND more MHC-II → fully stimulatory DC → maximal effector activation

4. **Four-arm Treg restoration (runs 148+150+151+153)**:
   - CNS1 induction (TGF-β/SMAD3, run_150)
   - Treg expansion (IL-2/CD25, run_151)  
   - CD80/CD86 contact suppression (CTLA4/abatacept, run_148)
   - **MHC-II contact suppression** (LAG-3/FGL1, run_153) — newly added
   - All four Treg effector layers now mapped

---

## Rosacea — Skin Treg LAG-3 Function

**MODERATE relevance:**
- Skin tissue Tregs (CD103+ FOXP3+): express LAG-3 in inflammatory skin; LAG-3 enables Treg-DC contact suppression in dermis
- Rosacea APCs: activated skin DCs present Demodex/LL-37 antigens on MHC-II → skin Treg LAG-3 can strip MHC-II from these DCs → reduces antigen presentation → Th17 suppression
- LAG-3 deficit in skin (from FOXP3 destabilization) → skin DCs retain MHC-II → more Th17/Th1 activation → rosacea amplification
- IMP321 (eftilagimod α; LAG-3-Ig): clinical agent that binds MHC-II on APCs → mimics LAG-3+ Treg contact → APC suppression; potential off-label rosacea rationale for severe refractory cases

---

## ME/CFS — NK LAG-3 Exhaustion

**MODERATE relevance:**
- NK cells in ME/CFS: LAG-3 overexpressed on NK cells from ME/CFS patients (Brenu 2012: elevated inhibitory receptors on NK cells)
- LAG-3+PD-1+TIM-3+ NK: triple-exhausted NK phenotype → NK cytotoxicity severely impaired → viral persistence → ME/CFS perpetuation
- Three converging NK exhaustion mechanisms (runs 150+151+153):
  - TGF-β → NKG2D mRNA destabilization (run_150)
  - IL-2 deficiency → NK dimeric receptor understimulation (run_151)
  - LAG-3 overexpression → KIEELE-mediated NK inhibition (run_153)
- Relatlimab analog (anti-LAG-3): could partially restore NK function in ME/CFS — unexplored but mechanistically grounded

---

## Therapeutic Targets

### Relatlimab (Anti-LAG-3, LAG-3 Antagonist)
- Anti-LAG-3 monoclonal antibody (BMS-986016)
- Opdualag (relatlimab + nivolumab): FDA approved 2022 for melanoma
- Blocks LAG-3-MHC-II interaction → reinvigorates exhausted T cells and NK cells
- Autoimmune risk: relatlimab could impair Treg function (Tregs use LAG-3 as effector) → autoimmune irAE monitoring required
- T1DM context: relatlimab-type agents in T1DM would WORSEN disease (removes Treg LAG-3 effector mechanism); avoid in T1DM

### IMP321 (Eftilagimod α — LAG-3-Ig Agonist/MHC-II Competitor)
- Soluble LAG-3-Ig fusion → binds MHC-II on APCs → APC activation paradoxically for cancer immunotherapy (different mechanism from Treg LAG-3)
- In autoimmune context: unclear if IMP321 (APC-binding) helps or hurts; distinct from Treg LAG-3 expression

### FGL1-Fc Fusion (LAG-3 Agonist on T Cells)
- FGL1-Fc → binds LAG-3 on T cells → KIEELE signaling → T cell inhibition → peripheral tolerance
- Directly restores β cell FGL1 function without requiring β cell survival
- Preclinical T1DM: FGL1-Fc delay of T1DM onset in NOD mice; Phase 1 concept stage

### LAG-3 Recombinant Protein (enhancing Treg function)
- Strategy: stimulate Tregs to upregulate LAG-3 via low-dose IL-2 (run_151) → FOXP3 → LAG-3 ↑ → more LAG-3+ MHC-II-stripping Tregs

---

## Cross-Axis Integrations

- **run_148** (CTLA4/abatacept): CTLA4 strips CD80/CD86 (co-stimulatory); LAG-3 strips MHC-II (antigen-presenting); non-overlapping → additive; four-arm Treg restoration now complete
- **run_150** (TGF-β/SMAD3): TGF-β induces LAG-3 expression on iTregs; SMAD3 → LAG-3 promoter binding (potential); TGF-β/CNS1-induced iTregs should express both CTLA4 and LAG-3 for full suppressive function
- **run_151** (IL-2 cytokine): IL-2 → FOXP3 ↑ → LAG-3 ↑ on Tregs; IL-2 is the proximal signal for LAG-3 Treg upregulation; low-dose IL-2 expands LAG-3+ Tregs specifically
- **run_152** (PTPN22/LYP): both LYP and LAG-3 suppress TCR proximal signaling but at different nodes; LYP: enzymatic dephosphorylation of ZAP-70/Lck; LAG-3: KIEELE motif-mediated inhibitory signaling; additive when co-expressed on Tregs
- **run_102** (NKG2D/NKG2DL): NK exhaustion convergence; NKG2D (NK activation, run_102) + LAG-3 (NK inhibition, run_153) constitute opposing NK regulation axes; TGF-β (run_150) additionally suppresses NKG2D
- **run_096** (caspase-4, HMGB1): HMGB1-LAG-3 interaction? LAG-3 can bind certain HMGB1 complexes (HMGB1-nucleosome); LAG-3+ pDCs = low IFN-α producers (HMGB1-LAG-3 on pDCs dampens IFN-α)

---

## Summary Integration

LAG-3 completes the Treg effector architecture alongside CTLA4 (run_148): CTLA4 = CD80/CD86 stripping (Signal 2), LAG-3 = MHC-II stripping (Signal 1) — two independent APC-contact mechanisms that together fully depotentiate DCs. The FGL1/β cell peripheral tolerance mechanism is the most T1DM-specific LAG-3 function: β cells actively suppress islet-infiltrating T cells via secreted FGL1 → LAG-3 on T cells; this tolerance signal collapses with insulitis-driven FGL1 ↓. FGL1-Fc fusion offers a novel approach to restore β cell-specific peripheral tolerance without requiring β cell survival. NK exhaustion via LAG-3 adds a third NK suppression mechanism in ME/CFS (alongside TGF-β/NKG2D and IL-2 deficiency). The four-arm Treg restoration protocol (CNS1 + CD25 + CD80/CD86 + MHC-II) now covers all mechanistically validated Treg effector arms.

---

*One-hundred-and-forty-sixth extension | LAG-3-CD223-lymphocyte-activation-gene-3 12p13.32 D1-extra-loop-MHC-II-100x-affinity KIEELE-cytoplasmic-motif ZAP70-PLCγ1-suppression FGL1-fibrinogen-like-protein-1-β-cell ligand-MHC-II-FGL1-LSECtin Treg-LAG-3-MHC-II-stripping FEME-endocytosis-MHC-II CTLA4-LAG-3-additive-dual-APC-contact β-cell-FGL1-tolerance-failure insulitis-FGL1-↓ FGL1-Fc-peripheral-tolerance T-cell-exhaustion-PD1-LAG3-co-expression KIEELE-independent-from-PD1 relatlimab-anti-LAG3-Opdualag-FDA2022 IMP321-eftilagimod-LAG3-Ig NK-LAG3-exhaustion ME-CFS run148-CTLA4-additive run150-TGFβ-LAG3-iTreg run151-IL2-FOXP3-LAG3 run152-LYP-additive four-arm-Treg-protocol | run_153 | Framework at SATURATION + 42: 153 runs*