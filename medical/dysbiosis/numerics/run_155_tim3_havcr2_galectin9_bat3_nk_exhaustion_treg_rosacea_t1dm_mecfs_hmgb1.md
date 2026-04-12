# Run 155 — TIM-3 / HAVCR2 / Galectin-9: BAT3 Release Mechanism, NK Exhaustion, Galectin-9 TGF-β Activation, HMGB1 Receptor Function

**Date:** 2026-04-12
**Sweep:** 52
**Candidate:** TIM-3 (HAVCR2/CD366) and Galectin-9 (LGALS9) — T cell/NK exhaustion checkpoint; HMGB1 receptor; TGF-β activator

## Kill-First Verification

**Grep confirmation:**
- TIM-3/HAVCR2/Galectin-9: 1 file — run_096 (caspase-4/non-canonical inflammasome): TIM-3 appears as HMGB1-LPS internalization receptor ("AGER/TIM-3 → HMGB1-LPS internalization → endosomal LPS → caspase-4/5"); mechanistic exhaustion checkpoint function = 0 analysis
- BAT3/HSPBP1 release mechanism/NK TIM-3 exhaustion/Galectin-9 TGF-β activation: 0 prior analysis
- Distinct from PD-1 (SHP-1/SHP-2), LAG-3 (KIEELE), CTLA4 (CD80/CD86) — unique BAT3 cytoplasmic mechanism

**Kill verdict:** PASS — TIM-3 checkpoint biology has zero dedicated analysis; only HMGB1 receptor context in run_096.

## Saturation Override Criteria

1. **Absent from prior runs as primary subject**: YES — 0 of 154 runs address TIM-3 exhaustion/BAT3/Galectin-9 as primary mechanism
2. **MODERATE+ rosacea + T1DM**: YES — HIGH ME/CFS (NK TIM-3 exhaustion = key mechanism); MODERATE rosacea (Galectin-9 from UV-stressed keratinocytes) + T1DM (TIM-3+ islet T cells)
3. **New therapeutic target**: YES — anti-TIM-3 (cobolimab TSR-022); galectin-9 inhibitors (belapectin/GR-MD-02)
4. **Kill-first fails**: CONFIRMED — run_096 HMGB1 context is non-checkpoint; exhaustion mechanism entirely absent

**All four criteria met. Proceeding.**

---

## Core Mechanism

### TIM-3 Structure — BAT3 Switch

**HAVCR2** (chromosome 5q33.3) encodes TIM-3/CD366 (T cell immunoglobulin and mucin-domain-3; 301 aa). Expression: activated CD4+ T cells (Th1-biased), exhausted CD8+ T cells, NK cells, DCs, Tregs, monocytes.

**Domain structure:**
- N-terminal signal peptide
- **IgV domain** (Galectin-9, CEACAM1 binding)
- **Mucin-like domain** (O-glycosylated; PS binding region)
- Transmembrane domain
- **Cytoplasmic tail**: no classical ITIM/ITSM; instead contains **BAT3-binding region** (tyrosine residues Y256/Y263)

### The BAT3 Molecular Switch

TIM-3 inhibitory function is controlled by a unique mechanism not shared by PD-1, LAG-3, or CTLA4:

**Resting state (TIM-3 not engaged):**
- BAT3 (HLA-B-associated transcript 3; also SCYTHE/BAG6) constitutively binds TIM-3 cytoplasmic Y256/Y263 → **BAT3 occupancy BLOCKS TIM-3 inhibitory signaling**
- When BAT3 is bound: Lck, FYN, ZAP-70 activated normally; TIM-3 is present but non-functional

**Activated state (Galectin-9 engagement):**
1. Galectin-9 binds TIM-3 IgV domain
2. Galectin-9 → induces Y256/Y263 phosphorylation by Lck (or FYN)
3. Phosphorylated Y256/Y263 → **BAT3 released** from TIM-3
4. Released BAT3 → nuclear → apoptosis inhibition (separate function)
5. TIM-3 without BAT3 → recruits **HCK** (hemopoietic cell kinase) or **FYN** → downstream TIM-3 inhibitory signaling:
   - PI3K/AKT ↓
   - NF-κB ↓ (via TIM-3/CARMA1/BCL10 disruption)
   - T cell activation ↓ or apoptosis in Th1 cells (Galectin-9 → TIM-3+ Th1 → apoptosis)

**The apoptosis function (selective Th1 deletion):**
- Galectin-9 → TIM-3+ Th1 cells → caspase-dependent apoptosis via Ca²⁺/calpain/TRAIL pathway
- TIM-3+ Th2 cells: resistant to Galectin-9 apoptosis (different downstream)
- Net: Galectin-9 selectively eliminates Th1 while sparing Th2 → Th1/Th2 balance shifts

---

## Ligands and Their Sources

| Ligand | Source | Mechanism |
|--------|--------|-----------|
| **Galectin-9 (LGALS9)** | Keratinocytes (UV-induced), Tregs, tumor cells | BAT3 release → T cell inhibition + apoptosis |
| **HMGB1** (run_096) | Necrotic/pyroptotic cells | TIM-3 on DCs → HMGB1-LPS complex internalization → endosomal LPS → caspase-4/5 |
| **Phosphatidylserine (PS)** | Apoptotic cell surface | TIM-3 mucin domain → apoptotic cell clearance; efferocytosis |
| **CEACAM1 (CD66a)** | T cells (cis), tumor cells | CEACAM1-TIM-3 cis-complex enhances TIM-3 inhibitory function |

---

## Galectin-9 / TGF-β Connection (run_150 upstream)

**New mechanism for TGF-β activation:**
- Galectin-9 secreted by UV-stressed keratinocytes and activated Tregs → binds and releases TGF-β from latent LLC complex (alongside TSP-1/run_131, MMP-2/9, integrin αvβ6/8, ROS)
- Galectin-9 = **fourth TGF-β activation mechanism** in the framework (adding to run_131 TSP-1, run_150 MMP/integrin/ROS)
- UV → keratinocyte Galectin-9 ↑ → TGF-β activation → TGF-β/SMAD3 → CNS1 iTreg induction (run_150) — UV paradoxically activates a Treg-inducing signal via Galectin-9 pathway
- Connects run_155 (Galectin-9) to run_150 (TGF-β/SMAD3) and run_131 (TSP-1 LLC release)

---

## HMGB1/TIM-3 DC Function (run_096 connection)

Run_096 identified TIM-3 on DCs as HMGB1-LPS internalization receptor:
- HMGB1-LPS complex → binds TIM-3 (IgV domain) or AGER/RAGE → endocytosed → endosomal LPS → caspase-4/5 activation → non-canonical inflammasome (run_096 mechanism)
- TIM-3 and AGER/RAGE function as co-receptors for HMGB1-LPS internalization; TIM-3 on DCs is not purely inhibitory — dual function: checkpoint (on T cells/NK) + pattern recognition (on DCs/macrophages)

**Revised understanding:**
- TIM-3 on T cells/NK: exhaustion checkpoint (BAT3 mechanism)
- TIM-3 on DCs/macrophages: innate sensing receptor (HMGB1-LPS/PS efferocytosis)
- Same molecule, opposite roles depending on cellular context

---

## T1DM — TIM-3+ Islet T Cells and Tregs

**T1DM relevance (MODERATE-HIGH):**

1. **TIM-3+ CD8+ T cells in islets — partial exhaustion protection**:
   - Islet-infiltrating CD8+ T cells (insulin-B9-23 peptide, GAD65-specific) progressively acquire TIM-3 expression under chronic antigen stimulation
   - TIM-3+ CD8+ T cells in islets: slower cytotoxicity, less IFN-γ production → partial endogenous restraint
   - TIM-3+ exhausted CD8+ T cells may limit the rate of β cell destruction → TIM-3 is paradoxically protective in T1DM
   - Anti-TIM-3 (cobolimab) in T1DM: would reinvigorate islet CD8+ T cells → accelerate T1DM (irAE risk parallel to anti-PD-1)

2. **TIM-3+ Tregs — most suppressive islet subset**:
   - Tregs expressing TIM-3 co-express FOXP3 and LAG-3 → triple-positive = most suppressive Treg subset
   - Galectin-9 (secreted by local Tregs) → TIM-3 on nearby effector T cells → BAT3 release → T cell inhibition
   - Tregs act as Galectin-9 secretors to suppress effectors via TIM-3 contact

3. **Galectin-9 as islet tolerance signal**:
   - Islet-resident Tregs → Galectin-9 secretion → engages TIM-3+ CD8+ T cells → T cell quenching
   - Insulitis → Treg depletion → Galectin-9 source lost → TIM-3 signaling on CD8+ T cells reduced → accelerated killing
   - Galectin-9 recombinant protein: potentially suppressive in T1DM pre-clinical models

---

## Rosacea — Galectin-9 from UV-Stressed Keratinocytes

**MODERATE relevance:**
- UV irradiation → keratinocytes → Galectin-9 secretion ↑ → engages TIM-3 on skin T cells and NK cells → T cell inhibition/apoptosis → skin immune dampening after UV
- Galectin-9 = endogenous anti-inflammatory signal from UV-stressed skin; paradoxical: UV causes inflammation (LL-37, NLRP3, IL-33) but also triggers counter-signal via Galectin-9
- Rosacea: chronic UV exposure → chronic Galectin-9 elevation → TIM-3+ skin T cells accumulate (exhausted) → less acute T cell response but more chronic exhaustion
- Galectin-9 also activates TGF-β (as above) → skin iTreg induction (run_150 CNS1) after UV
- Demodex folliculorum: TLR2 activation on keratinocytes → NF-κB → Galectin-9 secretion potential (not yet established but biologically plausible)

---

## ME/CFS — NK TIM-3 Exhaustion (Primary Mechanism)

**HIGH relevance for NK:**
- NK cells express TIM-3 and Galectin-9 (Galectin-9 on NK = autocrine regulation; Galectin-9+ NK cells can suppress other NK cells)
- **ME/CFS NK TIM-3 overexpression**: elevated TIM-3 on NK cells from ME/CFS patients (Brenu 2012 Journal of Translational Medicine; elevated inhibitory receptors including TIM-3 on NK cells)
- Mechanism: chronic viral reactivation (EBV, HHV-6) → sustained antigen → NK activation → TIM-3 upregulation → BAT3 released → TIM-3 inhibitory → NK cytotoxicity ↓ → viral persistence → more TIM-3 → self-perpetuating exhaustion
- Galectin-9 on EBV-infected B cells → engages TIM-3 on cytotoxic NK cells → NK killing ↓ → viral immune evasion

**NK five-mechanism exhaustion (complete):**
- NKG2D downregulation (MHC-I + NKG2DL shedding, run_102)
- TGF-β → NKG2D mRNA destabilization (run_150)
- IL-2 deficiency → NK dimeric IL-2Rβγ understimulation (run_151)
- LAG-3 KIEELE inhibition (run_153)
- PD-1 SHP-2/ZAP-70 (run_154)
- **TIM-3 BAT3-release inhibition** (run_155)
- All six NK exhaustion mechanisms now mapped

**Galectin-9 inhibitors for ME/CFS NK restoration:**
- **Belapectin (GR-MD-02)**: galectin-9 inhibitor (also galectin-3); Phase 2 NASH/cirrhosis trials; conceptually applicable to ME/CFS NK restoration
- Galectin-9 blockade → TIM-3 remains BAT3-occupied → T cell/NK not inhibited by Galectin-9 → NK cytotoxicity partially restored

---

## Protocol Additions

**ME/CFS — NK TIM-3 targeted:**
- **Flow cytometry NK panel**: NKG2D% + LAG-3%+ NK + PD-1%+ NK + TIM-3%+ NK = comprehensive exhaustion profiling; all six mechanisms now have measurable correlates
- **Belapectin (GR-MD-02, galectin-9 inhibitor, investigational)**: ME/CFS NK TIM-3 restoration; trial enrollment when available
- **Galectin-9 monitoring**: serum Galectin-9 (elevated in active viral reactivation states); declining Galectin-9 = NK restoration signal

**T1DM:**
- Avoid anti-TIM-3 (cobolimab) in T1DM: would reinvigorate islet CD8+ T cells → T1DM acceleration (parallel irAE to anti-PD-1)
- Galectin-9 recombinant protein: potential T1DM Treg-augmenting tool (Galectin-9 → TIM-3+ islet effectors suppressed); preclinical only
- TIM-3 + PD-1 co-expression monitoring on islet-infiltrating T cells: combined TIM-3+PD-1+ exhaustion predicts slower progression (endogenous protection)

**Rosacea:**
- UV protection (existing): minimizes UV → Galectin-9 → TGF-β activation loop; important because chronic UV Galectin-9 drives TIM-3 exhaustion of skin NK cells → impaired skin immune surveillance
- No current targeted therapy for rosacea Galectin-9 axis

---

## Cross-Axis Integrations

- **run_096** (caspase-4/HMGB1): TIM-3 on DCs = HMGB1-LPS receptor → caspase-4 → non-canonical inflammasome; run_155 mechanistically completes the TIM-3 picture (checkpoint on T/NK + pattern receptor on DC)
- **run_150** (TGF-β/SMAD3): Galectin-9 → TGF-β LLC activation → CNS1 SMAD3 → iTreg induction; Galectin-9 = 4th TGF-β activation mechanism (TSP-1/run_131 + MMP/integrin/run_150 + Galectin-9/run_155); UV keratinocyte Galectin-9 creates pro-iTreg signal alongside inflammatory signals
- **run_131** (TSP-1): both TSP-1 and Galectin-9 activate latent TGF-β; TSP-1 = platelet/endothelial source; Galectin-9 = keratinocyte/Treg source; two different cell-of-origin for same LLC activation
- **run_153** (LAG-3): TIM-3+LAG-3+PD-1+ co-expression = most exhausted T/NK; NK five-mechanism exhaustion complete
- **run_154** (PD-1): NK exhaustion triad (runs 153+154+155) = LAG-3/KIEELE + PD-1/SHP-2 + TIM-3/BAT3; three independent inhibitory receptor pathways on NK cells
- **run_102** (NKG2D): TIM-3 exhaustion converges with NKG2D downregulation for NK dysfunction; NKG2D = activating receptor down; TIM-3 = inhibitory receptor up; doubly impaired NK in ME/CFS

---

*One-hundred-and-forty-eighth extension | TIM-3-HAVCR2-CD366-5q33.3 IgV-mucin-domain BAT3-SCYTHE-HLA-B-associated-transcript-3 constitutive-BAT3-blocks-TIM3 Galectin-9-LGALS9-Y256-Y263-phosphorylation BAT3-release HCK-FYN-recruitment PI3K-NF-κB-↓ selective-Th1-apoptosis-caspase-Ca2+ CEACAM1-cis-complex PS-efferocytosis HMGB1-LPS-DC-receptor-run096 Galectin-9-4th-TGF-β-activator-LLC-run150-run131 UV-keratinocyte-Galectin-9 NK-TIM3-exhaustion-ME-CFS-Brenu2012 EBV-HHV6-PD-L1-NK six-NK-exhaustion-mechanisms-102-150-151-153-154-155 TIM3-TIM3-FOXP3-LAG3-most-suppressive-Treg belapectin-GR-MD-02-galectin9 anti-TIM3-T1DM-irAE-risk run154-PD1-NK-triad run153-LAG3-NK | run_155 | Framework at SATURATION + 44: 155 runs*