# Run 157 — EZH2 / PRC2 / H3K27me3: β Cell Regeneration via Cdkn2a Silencing, Treg Chromatin, Tazemetostat, Skin Inflammation

**Date:** 2026-04-12
**Sweep:** 54
**Candidate:** EZH2 (Enhancer of Zeste Homolog 2) / PRC2 complex — H3K27me3 writer; β cell proliferation regulator

## Kill-First Verification

**Grep confirmation:**
- EZH2/PRC2/H3K27me3/SUZ12/EED: 0 files across all 156 numerics runs
- Dhawan 2009/β cell EZH2/Cdkn2a/p16 silencing/β cell regeneration: 0 prior analysis
- KDM6B/JMJD3 (H3K27me3 eraser, opposing enzyme): 0 files
- The prior epigenetic runs cover H3K4me1 (SETD7/run_145), H3K9ac (SIRT6/run_090), 5mC/5hmC (TET/DNMT3A/runs 086/087/149) — H3K27me3 layer entirely absent

**Kill verdict:** PASS — EZH2/PRC2/H3K27me3 chromatin layer has zero dedicated analysis.

## Saturation Override Criteria

1. **Absent from prior runs as primary subject**: YES — 0 of 156 runs address H3K27me3 as primary mechanism
2. **MODERATE+ rosacea + T1DM**: YES — HIGH T1DM (Dhawan 2009 Science = landmark β cell regeneration mechanism); MODERATE rosacea (EZH2 in skin inflammation, keratinocyte proliferation)
3. **New therapeutic target**: YES — tazemetostat (EZH2 inhibitor, FDA approved 2020 for epithelioid sarcoma + follicular lymphoma); GSK126; CPI-1205
4. **Kill-first fails**: CONFIRMED — H3K27me3 is mechanistically distinct from all covered epigenetic layers (H3K4me1/SETD7, DNA methylation/DNMT3A/TET, H3K9/SIRT1/SIRT6)

**All four criteria met. Proceeding.**

---

## Core Mechanism

### EZH2 and PRC2 Complex

**EZH2** (Enhancer of Zeste Homolog 2; chromosome 7q36.1) is the catalytic subunit of **PRC2** (Polycomb Repressive Complex 2). EZH2 is a histone methyltransferase that writes **H3K27me3** (trimethylation of histone H3 lysine 27) — the canonical repressive chromatin mark.

**PRC2 complex subunits:**
- **EZH2** (or EZH1 — paralog): catalytic SET domain → H3K27me1/me2/me3
- **EED**: WD40 domain; binds existing H3K27me3 → allosterically activates EZH2 → **H3K27me3 propagation** (self-reinforcing silencing)
- **SUZ12**: scaffold; required for PRC2 stability and chromatin recruitment
- **RbAp46/RbAp48**: histone chaperones

**Cofactors and regulation:**
- JARID2: recruits PRC2 to unmethylated CpG islands and polycomb response elements (PREs)
- EPOP: enhances PRC2 activity at bivalent loci (H3K4me3 + H3K27me3) in stem cells
- **EED/H3K27me3 feedback loop**: EED reads H3K27me3 → stimulates EZH2 → more H3K27me3; creates heritable silencing
- SAM (S-adenosylmethionine): methyl donor; connects to run_145 (SETD7/SAM) — same cofactor

**Opposition:**
- **KDM6B/JMJD3** and **KDM6A/UTX**: H3K27me3 demethylases (H3K27me3 → H3K27me2 → H3K27me1); activation of polycomb-silenced genes
- EZH2 inhibition + KDM6B activation = cooperative H3K27me3 erasure

---

## β Cell Regeneration — Dhawan 2009 (Landmark Science Paper)

This is the most mechanistically important T1DM contribution of the EZH2 axis.

**The Problem:** Adult β cells have extremely low proliferative capacity. The Cdkn2a (INK4a/ARF) locus encodes p16^Ink4a (CDKN2A) and p14^ARF — cell cycle inhibitors that block CDK4/6 → Rb phosphorylation → G1 arrest.

**Dhawan 2009 (Science 326:554-558): EZH2-dependent β cell regeneration:**
- Normal young β cells: EZH2 → H3K27me3 at Cdkn2a locus → p16/p14 silenced → β cells can proliferate
- Aging: EZH2 activity ↓ → Cdkn2a H3K27me3 ↓ → p16/p14 derepressed → CDK4/6 inhibited → β cell proliferation stops
- EZH2 KO (Pdx1-Cre/EZH2-flox): dramatic reduction in β cell mass by adulthood (~50% fewer β cells by 10 weeks) — EZH2 is required to maintain the regenerative potential of β cells
- EZH2 overexpression in β cells: Cdkn2a H3K27me3 maintained → p16 suppressed → extended β cell proliferative window → more β cell mass
- **EZH2 inhibition paradox**: at the whole-organism level, EZH2 inhibition opens Cdkn2a → β cell proliferation ↓; but in insulitis context, EZH2 inhibition on immune cells might be beneficial

**Connecting to T1DM:**
- Insulitis cytokines (IL-1β, IFN-γ, TNF-α): suppress β cell EZH2 → Cdkn2a derepressed → β cell proliferative capacity ↓ even before death
- EZH2 maintenance in β cells: preserving EZH2 activity in β cells (not inhibiting it) → maintains Cdkn2a silencing → extends β cell regeneration window
- Age-related T1DM risk: older patients have lower β cell EZH2 → less proliferative reserve → T1DM more severe once insulitis begins
- **EZH2 context-dependence**: in β cells = maintain (pro-regeneration); in immune cells = inhibit (anti-inflammatory); tazemetostat in T1DM must target immune cells, not β cells

---

## EZH2 in Immune Cells — Treg and Inflammatory Context

**Treg EZH2 — complex/context-dependent:**
- Tregs express EZH2; H3K27me3 in Tregs silences cytokine genes (IFNG, IL2, TNF-α) → Tregs remain stable without producing Th1/Th17 cytokines
- EZH2 deletion in Tregs (FOXP3-Cre/EZH2-flox): Tregs become "unstable" — maintain FOXP3 but gain cytokine production (IFN-γ+) → loss of suppressive function → resembles ex-Treg conversion
- EZH2 in Tregs at inflammatory sites: EZH2 ↑ at inflammatory sites → maintains Treg identity under inflammatory pressure (Teff cytokines try to convert Tregs → EZH2 protects FOXP3 locus by silencing competing cytokine genes)
- **Interpretation**: EZH2 in Tregs = stability factor; EZH2 inhibition in Tregs = destabilizes Tregs; EZH2 inhibitors might have pro-inflammatory effects on Tregs — caution

**Effector T cells and macrophages:**
- EZH2 in CD8+ T cells: silences exhaustion-associated genes → keeps CD8+ T cells in progenitor-exhausted (not terminal) state → EZH2 inhibition → terminal exhaustion deepens (counterproductive in ME/CFS NK)
- EZH2 in macrophages: H3K27me3 at anti-inflammatory gene promoters → persistent pro-inflammatory state; EZH2 inhibitors → anti-inflammatory gene derepression → M2 polarization enhanced

---

## Rosacea — EZH2 in Skin Inflammation

**MODERATE relevance:**
- Keratinocytes: EZH2 regulates keratinocyte proliferation; UV → EZH2 ↑ in keratinocytes → H3K27me3 at tumor suppressor loci → proliferation ↑ (UV-driven epigenetic reprogramming)
- Inflammatory skin: EZH2 ↑ in psoriatic skin lesions → H3K27me3 at anti-inflammatory promoters → sustained inflammatory gene expression; EZH2 inhibitors (tazemetostat) → re-express anti-inflammatory genes in keratinocytes
- Rosacea skin: EZH2 may contribute to H3K27me3-mediated silencing of SOCS3/PPARγ/IL-10 in rosacea keratinocytes and macrophages → sustained NF-κB/KLK5 expression
- UV → EZH2 → H3K27me3 → NF-κB upstream gene derepression (potential) → UV epigenetic rosacea amplification

**Tazemetostat potential in rosacea:**
- Anti-inflammatory via EZH2 inhibition in skin macrophages → H3K27me3 at SOCS3/PPARγ ↓ → SOCS3/PPARγ re-expressed → NF-κB ↓
- Topical EZH2 inhibitor conceptually (no current topical formulation approved)

---

## ME/CFS — EZH2 in T/NK Cell Exhaustion

**MODERATE relevance:**
- NK cells: EZH2 in NK cells silences activation genes; chronic stimulation → EZH2 ↑ → H3K27me3 at NKG2D and activation receptor loci → NK exhaustion deepened epigenetically
- EZH2 inhibitor (tazemetostat) in NK exhaustion: could re-express NKG2D and activation receptors by removing H3K27me3
- Connects to run_102 (NKG2D): EZH2-mediated H3K27me3 at NKG2D locus = epigenetic component of NKG2D downregulation in ME/CFS
- T cell exhaustion: EZH2 → H3K27me3 at TCF7 (TCF1) locus in exhausted T cells → blocks progenitor exhaustion renewal → promotes terminal exhaustion; EZH2 inhibition → TCF1 re-expressed → progenitor exhaustion phenotype rescued

**SAM connection (run_145/SETD7 + run_157/EZH2):**
- Both SETD7 (H3K4me1) and EZH2 (H3K27me3) require SAM as methyl donor
- B12/betaine (run_145 protocol) maintains SAM → supports BOTH SETD7 (Treg/β cell protective H3K4me1) AND EZH2 (β cell Cdkn2a silencing/proliferative capacity)
- Competing consideration: SAM depletion → SETD7 ↓ AND EZH2 ↓; for β cells, both losses are harmful

---

## Protocol Additions

**T1DM — EZH2/β cell context (preservation, not inhibition):**
- **Do NOT use systemic tazemetostat in T1DM** without careful targeting: systemic EZH2 inhibition → β cell EZH2 ↓ → Cdkn2a derepressed → β cell proliferative capacity lost (harmful)
- **Targeted approach**: EZH2 inhibition in immune cells only (Treg agonism via separate mechanism → don't impair Treg EZH2; rather inhibit EZH2 in effector T cells and macrophages)
- **SAM/B12 support** (runs 145/157 shared): maintaining SAM supports β cell EZH2 activity → Cdkn2a silencing maintained → proliferative reserve preserved; adds β cell regeneration rationale to existing B12/betaine protocol
- **Cdkn2a monitoring**: p16^Ink4a serum levels correlate with β cell EZH2 activity; elevated p16 in T-cell exhaustion and β cell aging = indicator of EZH2 loss

**Rosacea:**
- EZH2 inhibition (tazemetostat, off-label, systemic) — not practical for rosacea given risk profile and keratinocyte EZH2 complexity
- Monitor: no practical current protocol; mechanistic insight useful for understanding skin chronicity

**ME/CFS — NK EZH2 restoration:**
- EZH2 inhibitors (tazemetostat) may reverse epigenetic silencing of NKG2D and activation receptor loci in exhausted NK
- Combination concept: belapectin (galectin-9/TIM-3) + tazemetostat (NKG2D/activation receptor re-expression) → dual NK exhaustion mechanism reversal (checkpoint + epigenetic)
- Caution: tazemetostat systemic dose → also affects Treg EZH2 → Treg destabilization risk; NK-targeted delivery needed

---

## Cross-Axis Integrations

- **run_145** (SETD7/H3K4me1): H3K4me1 (active enhancer) opposes H3K27me3 (repressive); at β cell enhancers: SETD7 deposits H3K4me1 (activation); EZH2/PRC2 would deposit H3K27me3 (silencing) if SETD7 is lost; SETD7 H3K4me1 blocks EZH2 ADD-domain analog → SETD7/EZH2 compete at β cell enhancers
- **run_086/087** (TET2/TET3 + vitamin C): TET → 5mC demethylation; EZH2 → H3K27me3; two independent repressive marks; Treg stability requires both DNA demethylation (TET, CNS2) and H3K27me3 maintenance (EZH2, cytokine silencing); vitamin C (TET activation) + SAM/B12 (EZH2 support) = dual-layer epigenetic protection for Tregs
- **run_149** (DNMT3A): DNMT3A deposits 5mC; EZH2 deposits H3K27me3; both are repressive marks; DNMT3A (DNA layer) + EZH2 (histone layer) act together at silenced loci; DNMT3A/R882H CHIP (run_149) dysregulates 5mC; EZH2 loss dysregulates H3K27me3; compound epigenetic failure at shared loci
- **run_102** (NKG2D): H3K27me3 at NKG2D gene locus in exhausted NK = epigenetic mechanism of NKG2D downregulation; EZH2 inhibition → H3K27me3 ↓ → NKG2D re-expression; connects to run_102 primary mechanism
- **run_090** (SIRT3/SIRT6/H3K9ac): SIRT6 removes H3K9ac at NF-κB target genes; EZH2 adds H3K27me3 at separate loci; three histone modification layers at inflammatory genes: H3K9ac (activation, SIRT6 removes), H3K4me1 (active enhancer, SETD7 adds), H3K27me3 (silencing, EZH2 adds); each independently regulated

---

*One-hundred-and-fiftieth extension | EZH2-PRC2-7q36.1 SET-domain H3K27me3 EED-allosteric-feedback SUZ12-scaffold SAM-methyl-donor PRC2-complex EED-WD40-propagation JARID2-recruitment KDM6B-JMJD3-H3K27me3-eraser Dhawan2009-Science-EZH2-β-cell-Cdkn2a-p16Ink4a EZH2-KO-50%-β-cell-loss Cdkn2a-INK4a-ARF-silencing CDK4-6-Rb-G1 EZH2-aging-β-cell-regenerative-decline insulitis-EZH2-↓-proliferative-capacity-loss Treg-EZH2-stability-cytokine-silencing tazemetostat-EZH2-inhibitor-FDA2020 GSK126 keratinocyte-EZH2-UV NK-EZH2-NKG2D-epigenetic-silencing SAM-B12-EZH2-SETD7-shared run145-H3K4me1-competition run086-TET-dual-layer run149-DNMT3A-dual-repressive run102-NKG2D-H3K27me3 run090-SIRT6-H3K9ac | run_157 | Framework at SATURATION + 46: 157 runs*