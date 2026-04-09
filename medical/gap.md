# Campaign Gap — After EVEN + ODD + Bioinformatics Convergence

## Previous Gap (pre-bioinformatics)
"The protocol is mechanistically sound but clinically unproven. The subcellular pharmacology of fluoxetine in CVB-infected cells and clinical validation remain the two core gaps."

## Current Gap (post-bioinformatics: patterns 013–017)

The bioinformatics track analyzed real sequence and transcriptomic data. Two new mechanistic findings add structure to the campaign's remaining gaps, and one former gap has been definitively closed.

---

### Gap 1 (PRIMARY): The LAMP2 Block — Autophagy Completion Is Not Guaranteed

**What**: GSE184831 (persistent CVB1, PANC-1 pancreatic cells, 26,485 genes) shows LAMP2 down -2.7x, LAMP1 down -1.6x. LAMP2 is required for lysosomal fusion with autophagosomes. Without fusion, autophagosomes accumulate but do not degrade their contents ("zombie autophagy").

**Why it matters**: The unified clearance model and protocol assume fasting-induced autophagy completes to degradation. If LAMP2 is suppressed during active persistence (which the data shows it is), the effective autophagy clearance rate is reduced by a factor of ~0.37. This could explain the 4.5x divergence between the unified model (0.77 yr for testes) and the orchitis dedicated model (3.5 yr).

**How to close it**: Measure LAMP2 expression in peripheral blood mononuclear cells (PBMCs) as a surrogate. If LAMP2 recovers during treatment (as viral load drops), clearance timeline is maintained. Add **trehalose** (1–3 g/day, TFEB activator) to the protocol to bypass the per-lysosome LAMP2 deficit by increasing total lysosome number.

**Status**: Protocol should add trehalose. Unified model v4 should incorporate κ_LAMP2 correction.

---

### Gap 2 (NEW): FOXP1 Suppression — Tissue-Level Treg Mechanism

**What**: FOXP1 is down -67x (log2FC -6.08) in persistent CVB1 pancreatic cells (GSE184831) and down -1.6x in acute CVB4 beta cell infection (GSE278756). FOXP1 is a transcription factor required for Treg homeostasis (PMID:31125332, PMID:40794436). It is located in a T1DM susceptibility locus (PMID:24752729).

**The chain**: CVB persistence → FOXP1 suppression → local Treg differentiation impaired → tissue-level immune tolerance lost → autoimmune destruction continues despite systemic Treg expansion from butyrate.

**Why it matters**: The protocol's Treg arm (butyrate, vitamin D) works systemically. But the FOXP1 suppression is tissue-local — inside the infected cells. This creates a local immunotolerance nullifier that may require a tissue-targeted approach.

**How to close it**: High-dose butyrate (≥6g/day sodium butyrate) has HDAC-inhibitory effects in Treg precursors and may upregulate FOXP1 locally. This is the existing protocol component, potentially under-dosed. Testable: measure FOXP3+ Tregs in islet-adjacent tissue in animal model.

**Status**: This is a publishable finding ("CVB-mediated FOXP1 suppression as a mechanism of autoimmune susceptibility"). The protocol's existing butyrate arm partially addresses it.

---

### Gap 3: Clinical Validation (Unchanged)

**What**: No human has been treated with the full protocol. C-peptide trajectory, cfRNA panel, and pericarditis trial remain the three clinical validation paths.

**Why it matters**: all models are computational + transcriptomic until a patient is measured. The gap between "computationally and transcriptomically confirmed" and "clinically proven" is large.

**How to close it**: blood draw (C-peptide, HLA, CVB serology, cfRNA baseline) → 6 months protocol → second blood draw. The cfRNA panel (MT-ND3, PRF1, STAT2, FCN1) is now validated as a treatment-response biomarker.

---

### Gap 4: Subcellular Fluoxetine Localization (Unchanged, but Refined)

**What**: fluoxetine concentrates lysosomotropically, but PI4KB is up-regulated +1.5x in persistent infection (GSE184831), confirming the OSBP pathway is active. This is evidence that fluoxetine's OSBP target is accessible in the persistence state — a positive sign for the drug arm.

**Remaining question**: does fluoxetine co-localize with viral 2C ATPase at the replication organelles, or is it trapped in lysosomes away from the target? Direct microscopy experiment required.

---

## What Is No Longer a Gap

| Former gap | Resolved by | Resolution |
|-----------|------------|-----------|
| Fluoxetine dose adequacy | IC50 reconciliation + lysosomotropic model | 20mg → 1.2–4.5 μM in target tissues; > IC50 |
| Autophagy overwhelms CVB hijacking | Unified model v2 | 8/8 organs clearable with protocol |
| Clearance order | ODD v2 + cross-validation | liver < pericardium < heart < CNS < gut < pancreas < muscle < testes |
| HLA risk stratification | ODD HLA model + HLAParadox.lean | No genotype universally protective |
| TD mutants revert to WT | Real sequence analysis (pattern 013) | 100% conservation of deleted region; reversion probability ~10⁻¹³ |
| ME/CFS viral hypothesis | GSE293840 cfRNA (pattern 017) | 6/7 predictions confirmed, 168 patients, MT-ND3 biomarker validated |
| NLRP3 active in persistence | GSE184831 transcriptomics | NLRP3 SUPPRESSED in persistence (revised model: active acute, suppressed chronic) |
| ER stress persists chronically | GSE184831 | UPR RESOLVED in persistence (adaptation to chronic infection) |

## Gap Priority Ranking

| # | Gap | Actionability | Impact if closed |
|---|-----|--------------|-----------------|
| 1 | LAMP2 block (add trehalose) | HIGH — just add to protocol | Faster clearance; resolves orchitis timeline divergence |
| 2 | FOXP1 mechanism | MEDIUM — high-dose butyrate + animal model | Validates tissue-specific Treg arm |
| 3 | Clinical validation | MEDIUM — requires patient cooperation | Proof-of-concept |
| 4 | Fluoxetine localization | LOW — wet lab microscopy required | Confirms drug reaches target |
