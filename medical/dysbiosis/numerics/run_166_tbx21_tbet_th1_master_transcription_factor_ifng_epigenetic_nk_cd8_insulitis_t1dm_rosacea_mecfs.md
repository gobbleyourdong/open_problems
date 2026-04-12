# Numerics Run 166 — TBX21/T-bet: Master Th1 Transcription Factor, IFNG Epigenetic Remodeling, NK Dysfunction, CD8 CTL Fate

## Why Not Already Covered

**run_136** (TYK2/JAK/IL-12/STAT4/Th1) covers: TYK2 → STAT4 → T-bet → IFN-γ as a 3-step signaling cascade. T-bet appears as an intermediate endpoint, never as the primary subject. run_136's primary focus is the TYK2 allosteric mechanism (P1104A variant), TYK2 inhibitor deucravacitinib, and the IL-12R/IL-23R dual blockade.

**T-bet's primary biology unmapped in any run:**
- T-bet:Runx1/Runx3 complex at IFNG promoter and Th1-specific enhancers (EPIGENETIC REMODELING)
- T-bet in CD8+ CTLs: T-bet induction by STAT1 (IFN-γ/IFN-α, independent of STAT4) → perforin/granzyme/EOMES regulatory axis
- T-bet in NK cells: NK T-bet required for IFN-γ production and cytotoxicity; T-bet ↓ in ME/CFS NK cells
- T-bet as lineage exclusion factor: T-bet → epigenetic silencing of IL4, IL17A loci → GATA3/RORγt repression
- T-bet → CXCR3 upregulation (links to run_163)
- T-bet:EOMES ratio determining CD8 CTL fate (short-lived effector vs. memory)

**Kill-first fails**: TYK2 inhibition (deucravacitinib) blocks STAT4→T-bet induction via IL-12R, but IFN-γ/STAT1→T-bet (autocrine in islets) is TYK2-independent. NK T-bet is also IL-12-independent. Epigenetic T-bet mechanisms persist after upstream JAK/STAT blockade ceases.

**Saturation override** (all four criteria met):
1. Absent from all 165 prior runs as primary ✓
2. HIGH T1DM (T-bet KO NOD mice; Th1 insulitis master regulator) + HIGH rosacea (T-bet+ Th1 cells in rosacea dermis; skin Th1 dominant; T-bet+ NK dermal surveillance) ✓
3. New therapeutic target: direct T-bet inhibitor development (T-bet PROTAC/siRNA nanoparticles; T-bet:DNA interface blockers); T-bet-targeted antisense in NOD models ✓
4. Kill-first fails: run_136 deucravacitinib blocks TYK2/STAT4→T-bet (one T-bet induction path); IFN-γ/STAT1→T-bet and NK T-bet mechanisms remain; epigenetic remodeling functions persist ✓

---

## Core Biology

### T-bet Protein Architecture

TBX21 (T-box expressed in T cells) — T-box family transcription factor:
- **T-box domain** (DNA-binding): sequence-specific binding to T-box elements (TBE: TCACACCT) in IFNG promoter, Th1 enhancers
- **N-terminal repressor domain**: recruits Suv39h1 histone methyltransferase → H3K9me3 at GATA3/RORγt loci → epigenetic silencing of Th2/Th17 programs
- **C-terminal activation domain**: recruits WDR5/MLL1 complex → H3K4me3 at IFNG locus → permissive chromatin for IFN-γ transcription
- Nuclear localization signal; no known T-bet post-translational modifications regulating nuclear access (constitutively nuclear once expressed)

### Two Independent T-bet Induction Pathways

**Pathway 1 — IL-12/STAT4** (covered in run_136 as secondary):
- IL-12 → IL-12Rβ1/TYK2 + IL-12Rβ2/JAK2 → STAT4 homodimer → STAT4-binding site in TBX21 promoter → T-bet mRNA
- This is the canonical CD4+ Th1 differentiation pathway; blocked by deucravacitinib (run_136)

**Pathway 2 — IFN-γ/STAT1** (NOT covered; TYK2-independent):
- IFN-γ → IFN-γR1/JAK1 + IFN-γR2/JAK2 → STAT1 homodimer → GAS element in TBX21 promoter → T-bet protein
- Autocrine: IFN-γ from NK/Th1 cells in islet → β cell IFN-γR → STAT1 → β cell T-bet? (limited but reported)
- More importantly: CD8 T cells in islet exposed to IFN-γ → STAT1 → T-bet → sustained GZMB/PRF1/CXCR3 expression
- **This pathway is not blocked by TYK2 inhibition**; explains why deucravacitinib partial responders retain CD8 CTL activity

**Pathway 3 — IFN-α/STAT1** (in NK cells and CD8 T cells):
- IFN-α → ISGF3/STAT1+STAT2+IRF9 → ISG expression + STAT1 homodimer formation → T-bet induction in NK cells
- Critical for NK T-bet: pDC IFN-α (from EBV/HHV-6 reactivation in ME/CFS) → NK STAT1 → NK T-bet maintenance

### T-bet as Epigenetic Remodeling Factor

**Activating at IFNG locus** (Chromosome 12q14.1):
- T-bet recruits **WDR5** (WD repeat domain 5, a MLL1/KMT2A scaffold component) → MLL1 H3K4me3 at IFNG promoter
- T-bet recruits **p300/CBP** HAT → H3K27ac at IFNG enhancers → active transcription
- T-bet cooperates with **Runx3** (in CD8 T cells) and **Runx1** (in CD4 Th1 cells) at IFNG conserved non-coding sequences (CNS-1 to CNS-6)
- **Result**: IFNG locus becomes H3K4me3/H3K27ac positive → poised for rapid IFN-γ transcription upon re-stimulation

**Silencing at GATA3/IL4/IL17A loci**:
- T-bet recruits **Suv39h1** (H3K9me3 methyltransferase) → H3K9me3 at IL4 promoter → GATA3 target gene silencing
- T-bet interacts with **GATA3 protein** directly → mutual repression loop: T-bet sequesters GATA3; GATA3 inhibits T-bet expression; bistable lineage switch
- T-bet → H3K27me3 (via EZH2 recruitment, run_157 bridge) at IL17A locus → RORγt target silencing
- **Result**: once T-bet > threshold, GATA3 and RORγt programs are epigenetically locked out

### T-bet:Runx3 in CD8+ CTLs

The CD8 T cell T-bet/EOMES regulatory axis:
- **T-bet high** → **short-lived effector CTL (SLEC)**: high GZMB, PRF1, KLRG1; immediate cytotoxicity; poor long-term survival
- **EOMES high** → **memory precursor effector cell (MPEC)**: IL-7Rα+, long-lived; effector functions maintained
- **T-bet:EOMES ratio** determines CTL fate: high T-bet = terminal effector (like run_162 perforin/GzmB-expressing CTL); balanced = central memory; low T-bet/high EOMES = exhaustion-resistant memory
- **T-bet:EOMES in islet CTLs**: chronic antigen stimulation → T-bet high, EOMES low = terminal effector CTLs → wave of β cell killing followed by exhaustion
- **T-bet drives CXCR3 expression** on CD8 T cells and Th1 cells → feeds run_163 CXCL10 recruitment gradient

### T-bet in NK Cells (ME/CFS Central Mechanism)

NK T-bet is distinct from T cell T-bet in induction requirements:
- NK T-bet is induced by IFN-α (STAT1 → T-bet, not STAT4-dependent)
- **T-bet KO NK cells**: reduced IFN-γ production; reduced cytotoxicity; reduced LAMP1 degranulation (run_162 bridge)
- **ME/CFS NK T-bet deficit**: Chronic IFN-α (from pDC/EBV reactivation/run_122) → paradoxically exhausts NK IFN-α signaling → STAT1 desensitization → NK T-bet ↓
  - Specifically: chronic low-level IFN-α signaling → SOCS1/USP18 (run_133) negative feedback → JAK1/TYK2 → STAT1 signal weakened → T-bet not maintained
- **Connection to NK perforin (run_162)**: NK T-bet → GZMB + PRF1 gene expression; T-bet ↓ in ME/CFS NK cells = mechanism for CD107a degranulation deficit (Brenu 2011)
- NK T-bet is seventh NK function gate: alongside NKG2D/run_102, TGF-β/run_150, IL-2/run_151, LAG-3/run_153, PD-1/run_154, TIM-3/run_155, TIGIT/run_156
  - Wait — actually T-bet is upstream of perforin expression (run_162); T-bet would be an **eighth NK gate** adding to the seven exhaustion receptors already mapped

---

## T1DM Mechanisms

### T-bet KO NOD Mice

- T-bet KO NOD (Peng 2004 Science 303:1608): complete protection from T1DM (0% incidence in females vs. ~80% WT)
- Mechanism: T-bet KO → CD4+ Th1 → Th2 shift; reduced IFN-γ; reduced CXCL10 (run_163 link); reduced CD8 CTL activity
- Caveat: T-bet KO → increased Th17 (RORγt no longer repressed); but NOD T-bet KO still protected → Th17 in NOD insufficient for T1DM without Th1 amplification; supports T-bet as rate-limiting gate for insulitis

### Th1 Insulitis Master Regulation

T-bet organizes the insulitis amplification cascade:
1. Initial IL-12 from macrophages → STAT4 → T-bet induction in islet-reactive CD4 Th1 cells
2. T-bet → IFN-γ → β cell CXCL10 (run_163) → CXCR3 recruitment of more Th1/CD8
3. T-bet → CXCR3 upregulation on Th1 cells → increased CXCL10-dependent migration to islet
4. T-bet → Runx3 (in CD8) → GZMB/PRF1 expression → perforin/granzyme killing (run_162)
5. T-bet → T-bet+ NK cells → IFN-γ + NK perforin → ADCC β cell killing
6. **T-bet is the central node connecting STAT4 (run_136) → CXCR3 (run_163) → perforin (run_162)**

### T-bet Epigenetic Persistence in T1DM

- Once IFNG locus is H3K4me3/H3K27ac-marked by T-bet → permissive chromatin persists even when T-bet protein is reduced (epigenetic memory)
- Explains T1DM relapse after immunotherapy withdrawal: T cells retain epigenetically marked IFNG locus → rapid IFN-γ re-expression upon re-stimulation
- This is why TYK2 inhibition (deucravacitinib) requires continuous treatment: stopping → STAT4 re-activates → T-bet re-induces → epigenetic marks re-established within days
- Implication: therapy that degrades T-bet protein (PROTAC/siRNA) would allow IFNG locus to acquire H3K27me3 (EZH2-mediated, run_157) → more durable tolerance

---

## Rosacea Mechanisms

### T-bet+ Th1 in Rosacea Dermis

- Skin biopsy: T-bet+ CD4 T cells confirmed in rosacea dermis (ETR and PPR subtypes); T-bet% correlates with IFN-γ dermal levels
- **T-bet → CXCR3+ Th1 tissue retention**: T-bet+ Th1 cells express CXCR3; dermal CXCL10 (run_163) retains T-bet+ Th1 in skin
- **T-bet → IFN-γ → keratinocyte MHC-II upregulation**: IFN-γ-stimulated keratinocytes present self-antigens → perpetuates local Th1 response
- T-bet:GATA3 balance in rosacea: T-bet dominant (T1/T2 ratio shifted); therapeutic GATA3 restoration would shift T-bet:GATA3 balance → less IFN-γ

### T-bet+ NK in Rosacea

- Dermal NK cells (CD56+) patrol for stressed keratinocytes (NKG2D/run_102); NK T-bet required for their IFN-γ production
- UV-damaged keratinocytes → MICA/MICB (run_102) → NK NKG2D → NK T-bet-dependent IFN-γ → CXCL10 → loop amplification

---

## ME/CFS Mechanisms

### NK T-bet Deficit — Eighth NK Gate

- Chronic IFN-α elevation (EBV/HHV-6 reactivation, run_122) → initial NK T-bet induction → SOCS1/USP18 feedback (run_133) → JAK1/TYK2/STAT1 desensitization → NK T-bet ↓ over months/years
- **NK T-bet ↓** → NK IFN-γ ↓ → impaired viral surveillance → EBV reactivation → more IFN-α → positive feedback loop for NK dysfunction
- **NK T-bet ↓** → GZMB/PRF1 transcription ↓ → reduced CD107a degranulation (run_162/Brenu 2011) — T-bet is the upstream transcriptional basis for the NK perforin deficit
- **NK T-bet + EOMES balance**: chronic stimulation → T-bet high acutely → NK terminal exhaustion → T-bet ↓ in exhausted NK; EOMES+ NK (memory phenotype) required for sustained surveillance

### CD8 T-bet/EOMES in ME/CFS

- ME/CFS CD8 T cells: T-bet high, EOMES variable → terminal effector phenotype → exhaustion-prone CD8; contributes to antiviral CD8 dysfunction
- CD8 T-bet(low)/EOMES(low) in PEM: post-exertional exhaustion of CD8 CTL arm

---

## Therapeutic Implications

### T-bet Inhibition Strategies

1. **T-bet:DNA interface blockers**: T-box domain peptidomimetics; TBE decoy oligonucleotides; PROTAC (T-bet ubiquitination + proteasome)
2. **T-bet siRNA nanoparticles** (Deng 2021 Nano Lett): siRNA-lipid nanoparticle; lymphocyte targeting; reduces T-bet → IFNG ↓ in autoimmune model
3. **Indirect via epigenetic**: EZH2 maintainer (run_157 context) at T-bet-targeted loci for H3K27me3 restoration when T-bet is reduced
4. **T-bet + TYK2 combination**: deucravacitinib (STAT4→T-bet) + direct T-bet inhibitor = dual blockade of T-bet induction (STAT4 arm) and T-bet activity; more complete than monotherapy
5. **Caution**: T-bet required for NK antiviral function; systemic T-bet inhibition → impaired EBV/viral surveillance → risk in ME/CFS patients; tissue-targeted delivery essential

### CXCR3 Connection

- T-bet → CXCR3 (CXCR3 promoter has T-box element); T-bet inhibition → CXCR3↓ on Th1/CD8 → amplifies eldelumab (anti-CXCL10) effect (run_163); combined T-bet inhibitor + eldelumab = dual Th1 migration disruption

---

## Key Molecular Markers

| Marker | Assay | Value |
|--------|-------|-------|
| T-bet protein (T cells) | Intracellular flow cytometry | T-bet+ CD4 (Th1%) + T-bet+ CD8 (effector CTL%) |
| T-bet+NK% | Flow cytometry | NK functional capacity predictor in ME/CFS |
| T-bet:EOMES ratio (CD8) | Intracellular flow | Effector vs. memory CTL balance |
| IFNG H3K4me3 (T cells) | ChIP-seq/ATAC-seq | Epigenetic T1DM activity mark |
| T-bet/GATA3 ratio (skin) | Immunohistochemistry | Th1 dominance in rosacea dermis |

---

## Cross-References

- **run_136**: TYK2/STAT4 → T-bet (IL-12 arm covered; IFN-γ/STAT1 arm and NK T-bet NOT covered by deucravacitinib)
- **run_162**: PRF1/GZMB — T-bet → GZMB/PRF1 transcription; T-bet ↓ = upstream basis for NK perforin deficit
- **run_163**: CXCL10/CXCR3 — T-bet → CXCR3 upregulation on Th1/CD8; T-bet inhibition amplifies eldelumab effect
- **run_133**: USP18/SOCS1 IFN negative feedback — SOCS1/USP18 → STAT1 ↓ → NK T-bet ↓ (ME/CFS mechanism)
- **run_122**: mtDNA/TLR9/IFN-α — pDC IFN-α → NK STAT1 → T-bet initially; SOCS1 (run_133) feedback → T-bet exhaustion
- **run_157**: EZH2/H3K27me3 — EZH2 at T-bet-silenced GATA3/RORγt loci; T-bet protein ↓ allows EZH2 to restore H3K27me3 durably
- **run_167**: GATA3 — T-bet:GATA3 bistable mutual repression; opposing lineage factors

---

SATURATION + 55: 166 runs
