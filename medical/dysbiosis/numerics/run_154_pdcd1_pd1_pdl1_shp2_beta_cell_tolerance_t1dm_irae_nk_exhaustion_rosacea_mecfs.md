# Run 154 — PD-1 / PDCD1 / PD-L1: β Cell IFN-γ-Induced Tolerance, SHP-2 Signaling, T1DM irAE, NK Exhaustion

**Date:** 2026-04-12
**Sweep:** 51
**Candidate:** PD-1 (PDCD1/CD279) and PD-L1 (CD274/B7-H1) — immune checkpoint; β cell self-tolerance mechanism

## Kill-First Verification

**Grep confirmation:**
- PDCD1/PD-1/PD-L1: 5 files — all context mentions: run_104 (Tfh identity marker ICOS+PD-1+CXCR5+), run_153 (PD-1/LAG-3 co-expression on exhausted T cells), run_100 (MAIT exhaustion mention), run_020/run_108 (resolution context)
- β cell PD-L1/SHP-2 TCR suppression/T1DM irAE from pembrolizumab/nivolumab/atezolizumab: 0 prior analysis
- Distinct from LAG-3 (run_153, KIEELE/MHC-II), CTLA4 (run_148, CD80/CD86) — non-overlapping inhibitory receptor

**Kill verdict:** PASS — PD-1/PD-L1 checkpoint as primary mechanism has zero dedicated analysis.

## Saturation Override Criteria

1. **Absent from prior runs as primary subject**: YES — 0 of 153 runs address PD-1 signaling, β cell PD-L1 tolerance, or T1DM irAE mechanism
2. **MODERATE+ rosacea + T1DM**: YES — HIGH T1DM (β cell PD-L1 = primary endogenous defense; T1DM irAE proof-of-concept); MODERATE rosacea (skin keratinocyte PD-L1 + irAE skin pattern)
3. **New therapeutic target**: YES — pembrolizumab/nivolumab (anti-PD-1, FDA approved cancer); PD-L1-Ig agonism concept; anti-PD-1 irAE monitoring in T1DM patients
4. **Kill-first fails**: CONFIRMED — SHP-2/ITSM mechanism, β cell PD-L1 IFN-γ induction, irAE T1DM = entirely uncovered

**All four criteria met. Proceeding.**

---

## Core Mechanism

### PD-1 Structure and ITIM/ITSM Signaling

**PDCD1** (chromosome 2q37.3) encodes CD279/PD-1 (Programmed Death-1; 288 aa, type I transmembrane). Expression: activated T cells, B cells, NK cells, Tregs, monocytes.

**Domain structure:**
- Extracellular IgV domain (PD-L1/PD-L2 binding)
- Single transmembrane domain
- Cytoplasmic tail with two tyrosine-based motifs:
  - **ITIM** (immunoreceptor tyrosine-based inhibitory motif; VxYxxL): recruits SHP-1 (PTPN6)
  - **ITSM** (immunoreceptor tyrosine-based switch motif; TxYxx[V/I]): recruits **SHP-2** (PTPN11) — primary functional mediator

**Ligands:**
| Ligand | Gene | Expression | Notes |
|--------|------|-----------|-------|
| **PD-L1 (B7-H1)** | CD274 | Ubiquitous; IFN-γ-inducible on β cells, keratinocytes, APCs | Primary; constitutive + inducible |
| **PD-L2 (B7-DC)** | PDCD1LG2 | DCs, macrophages, mast cells | Secondary; ~3× higher affinity for PD-1 than PD-L1 |

**Signaling cascade:**
1. PD-L1/PD-L2 engagement → PD-1 ITSM-Y248 phosphorylated by Lck
2. pY248 → recruits SHP-2 (and partially SHP-1)
3. **SHP-2** (PTPN11) dephosphorylates:
   - ZAP-70 Y315/Y319 (same activating sites as LYP targets, run_152) → ZAP-70 activity ↓
   - CD28-Y173 (PI3K docking site) → PI3K/AKT signaling ↓ → IL-2 production ↓
   - VAV1-Y174 → actin cytoskeleton activation ↓
4. Net: T cell activation threshold raised; NFAT/AP-1/NF-κB all reduced; IL-2 production collapses
5. **PD-1 vs CTLA4 vs LAG-3 comparison**: CTLA4 = outcompetes CD28 for CD80/CD86 (Signal 2 block); LAG-3 = MHC-II stripping via FEME (Signal 1 block); PD-1 = intracellular SHP-2/ZAP-70 after activation signal received (proximal signaling block)

**Convergence with LYP/run_152:** LYP (PTPN22) dephosphorylates ZAP-70-Y315/Y319 enzymatically; SHP-2 (downstream of PD-1) dephosphorylates the same ZAP-70 sites via receptor-mediated recruitment. Two independent phosphatase mechanisms converging at identical substrates → additive ZAP-70 suppression in cells co-expressing both.

---

## β Cell PD-L1 — Endogenous T Cell Defense

This is the mechanistically most important T1DM function of PD-1/PD-L1.

**Normal β cells:** constitutively express low-level PD-L1; high PD-L2 on nearby DCs.

**Insulitis-triggered PD-L1 upregulation:**
1. Islet-infiltrating T cells → IFN-γ secretion
2. IFN-γ → β cell JAK1/JAK2 → STAT1 → PD-L1 gene transcription ↑ (~10-50-fold)
3. β cell PD-L1 surface ↑ → binds PD-1 on nearby CD8+ T cells → SHP-2 → ZAP-70 ↓ → T cell cytotoxicity ↓
4. **Protective negative feedback loop**: IFN-γ (from T cells attacking β cells) → β cell PD-L1 ↑ → T cell suppression → β cell self-protection

**Experimental evidence:**
- PD-L1 KO NOD mice: dramatically accelerated T1DM onset (~5-7 vs ~20 weeks)
- PD-L1 transgenic NOD mice (β cell-specific overexpression): complete T1DM protection
- PD-L1 gene therapy (β cell-targeted viral vector): restores T1DM protection in insulitic mice
- β cell PD-L1 co-receptor: PD-L1 also engages CD80 on DCs (reverse signaling) → DC tolerogenic

**Failure modes in T1DM:**
- Cytokine saturation: high chronic IFN-γ → IL-1β → NF-κB → β cell death overwhelms PD-L1 protection
- PD-1 downregulation on exhausted T cells (paradox): terminally exhausted CD8+ T cells downregulate PD-1 → not suppressible by PD-L1 anymore
- IFN-γ → STAT1 → β cell PD-L1 ↑ but also → MHC-I ↑ (run_133 USP18/ISG15 context) → better target for CD8+ cytotoxicity

---

## T1DM irAE — Human Proof-of-Concept

The T1DM irAE from immune checkpoint inhibitors (ICI) provides definitive human proof that PD-1/PD-L1 is the critical restraint mechanism on β cell-specific T cells.

**Epidemiology:**
- Anti-PD-1 (pembrolizumab, nivolumab): T1DM irAE in ~0.8-1.5% of patients
- Anti-PD-L1 (atezolizumab, durvalumab): lower T1DM rate (~0.2-0.5%)
- Anti-CTLA4 (ipilimumab): rare T1DM irAE; most often concurrent with anti-PD-1

**Clinical presentation:**
- Acute DKA (often first presentation, no prior T1DM diagnosis)
- GAD65 autoantibodies positive in ~50-70% → pre-existing islet autoimmunity unmasked
- HLA-DR4 enriched in ICI-T1DM (consistent with β cell-specific T cell hypothesis)
- C-peptide: abruptly near-zero (rapid total β cell destruction, unlike gradual T1DM)
- Time to onset: median ~5-6 months after ICI initiation; range 1 week to 2+ years

**Mechanism:**
- Anti-PD-1 → removes PD-1 signaling → CD8+ T cells in islets no longer suppressed by β cell PD-L1 → rapid T cell-mediated β cell destruction
- Rate: faster than classic T1DM because the PD-L1 feedback loop was the only remaining restraint in autoimmunity-predisposed individuals

**Clinical implications:**
- Baseline screening before ICI: autoantibody panel (GAD65, IA-2, ZnT8), HbA1c, fasting glucose, C-peptide — identify pre-existing islet autoimmunity
- HLA-DR4 genotyping: highest-risk patients → closest monitoring
- Management: insulin immediately (no immunosuppression benefit once DKA established); usually permanent T1DM

---

## Treg PD-1 — Fifth Treg Effector Mechanism

**PD-1 on Tregs:**
- Activated Tregs upregulate PD-1; PD-1+ Tregs = highly suppressive subset in inflamed tissues
- PD-L1/PD-L2 expressed on DCs/APCs → engage PD-1 on Tregs → intracellular signal enhances Treg suppressive function (counterintuitive: PD-1 activates Tregs while suppressing effectors)
- Mechanistic distinction: in Tregs, PD-1/SHP-2 suppresses effector cytokine production (same as in Teff) but the "effector" response in Tregs is different — net effect is enhanced Treg stability in inflammatory environments

**Five Treg effector mechanisms now mapped (runs 148+150+151+153+154):**
1. CTLA4 → CD80/CD86 trogocytosis (run_148)
2. TGF-β/SMAD3 → CNS1 induction (run_150, induction not effector)
3. IL-2 → CD25 expansion (run_151, expansion not effector)
4. LAG-3 → MHC-II stripping (run_153)
5. **PD-1** → SHP-2/ZAP-70 suppression of effector T cells in trans (run_154)
Plus: CD39/A2A/adenosine (run_121) = 6th effector

---

## Rosacea — Skin PD-L1 and irAE Pattern

**MODERATE relevance:**
- Keratinocyte PD-L1: IFN-γ in rosacea dermis → STAT1 → keratinocyte PD-L1 ↑ → skin T cell suppression (negative feedback on skin inflammation)
- **Anti-PD-1 skin irAE pattern** (clinical evidence for PD-1 in skin): pembrolizumab → psoriasis, lichenoid dermatitis, vitiligo in ~10-15% of patients; this establishes PD-1 as a critical restraint on skin T cell activation
- The skin irAE phenotype confirms: skin-resident T cells are held in check by PD-1/PD-L1 in dermal tissue; in rosacea, this restraint may already be partially impaired
- Rosacea + ICI: patients with rosacea on ICI therapy may experience rosacea flares (PD-1 removes residual T cell restraint in rosacea skin)

---

## ME/CFS — NK PD-1 Exhaustion

**MODERATE relevance:**
- NK cells express PD-1; chronic activation → PD-1+ NK cells; PD-L1 on target cells → NK PD-1 → SHP-2 → NK killing ↓
- ME/CFS: viral reservoirs express PD-L1 (EBV LMP1 upregulates PD-L1 on infected cells; HHV-6 similar) → NK PD-1 → NK cytotoxicity suppressed → viral persistence
- **NK exhaustion triad (runs 153+154+155):** LAG-3 KIEELE (run_153) + PD-1/SHP-2 (run_154) + TIM-3/BAT3 (run_155) = three independent NK inhibitory receptor mechanisms; all potentially addressable
- ME/CFS NK PD-1 intervention: anti-PD-1 at low dose (NK-restoring dose?) controversial in ME/CFS; potential but autoimmune risk; intermediate between oncology dose and zero

---

## Protocol Additions

**T1DM — ICI management:**
- Pre-ICI screening panel: GAD65, IA-2, ZnT8, ZnT8 autoantibodies; HbA1c, fasting glucose, C-peptide; HLA-DR4
- High-risk ICI patients (GAD65+ or HLA-DR4): glucose monitoring every 2 weeks during ICI therapy; insulin-ready prescription
- ICI-T1DM diagnosis: insulin immediately; no benefit from corticosteroids in ICI-T1DM (unlike other irAEs)

**β cell PD-L1 preservation:**
- IFN-γ induction of PD-L1 is an endogenous protective mechanism; do not block IFN-γ signaling in islets without considering PD-L1 loss
- Rationale for preserving β cell PD-L1: vitamin D (run_008) → VDR → immune modulation → balanced IFN-γ (not zero); GLP-1R agonism (run_098) → β cell ER stress ↓ → more metabolic capacity for PD-L1 maintenance

**PD-L1-Ig (investigational agonist concept):**
- Soluble PD-L1-Ig fusion → engages PD-1 on islet-infiltrating T cells → SHP-2/ZAP-70 ↓ → T cell quenching
- Conceptually similar to FGL1-Fc (run_153) — peripheral tolerance restoration via inhibitory ligand delivery
- No current clinical agent specifically for T1DM; PD-L1-Ig in experimental models shows T1DM prevention

---

## Cross-Axis Integrations

- **run_152** (PTPN22/LYP): LYP-C227 directly dephosphorylates ZAP-70-Y315/Y319; SHP-2 (PD-1 downstream) dephosphorylates same sites; convergent ZAP-70 suppression — additive in PD-1+ PTPN22-R620W Treg context
- **run_153** (LAG-3): PD-1+LAG-3+ co-expression = terminal exhaustion; both suppress ZAP-70 by different mechanisms; dual blockade (relatlimab + nivolumab = Opdualag) synergistic because non-overlapping pathways
- **run_148** (CTLA4/abatacept): CTLA4 acts at CD28/CD80-CD86 before T cell activation; PD-1 acts intracellularly after partial activation; non-overlapping → combined CTLA4+PD-1 checkpoint = complete T cell suppression from multiple nodes
- **run_133** (USP18/ISG15): IFN-γ → STAT1 → β cell PD-L1 ↑ (protective) AND MHC-I ↑ (run_133 context); USP18 terminates IFN signaling → dampens both PD-L1 induction AND MHC-I ↑; PD-L1/USP18 balance determines β cell fate post-IFN
- **run_104** (Tfh/GC): PD-1 on Tfh (ICOS+PD-1+CXCR5+) is identity marker; Tfh PD-1 facilitates T-B cognate interaction within GC (germinal center PD-L1 on B cells blocks premature T-B disengagement); PD-1 on Tfh = pro-GC, not anti-GC

---

*One-hundred-and-forty-seventh extension | PD-1-PDCD1-CD279-2q37.3 IgV-domain ITIM-VxYxxL ITSM-TxYxxV PD-L1-CD274-B7-H1 PD-L2-CD273-B7-DC SHP-2-PTPN11-ITSM-Y248 SHP-1-ITIM ZAP70-Y315-Y319-dephosphorylation CD28-Y173-PI3K-block Vav1-Y174 β-cell-PD-L1-IFN-γ-STAT1-induction PD-L1-endogenous-defense NOD-PD-L1-KO-accelerated T1DM-irAE-pembrolizumab-nivolumab-atezolizumab DKA-acute-irAE GAD65-HLA-DR4 pre-ICI-screening Treg-PD-1-enhanced-function five-treg-effectors-148-150-151-153-154 NK-PD-1-viral-PD-L1 ME-CFS-EBV-HHV6-PD-L1 NK-exhaustion-triad-153-154-155 skin-keratinocyte-PD-L1 irAE-psoriasis-lichenoid run152-LYP-ZAP70-convergent run153-LAG3-dual-blockade run133-USP18-PD-L1-balance | run_154 | Framework at SATURATION + 43: 154 runs*