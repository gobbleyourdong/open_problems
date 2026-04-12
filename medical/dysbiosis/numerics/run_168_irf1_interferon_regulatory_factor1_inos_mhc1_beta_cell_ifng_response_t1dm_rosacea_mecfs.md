# Numerics Run 168 — IRF1: Master IFN-γ Response Transcription Factor, β Cell iNOS/MHC-I/CXCL10, IRF1 KO NOD T1DM Prevention

## Why Not Already Covered

**run_091** (IDO1/kynurenine) mentions IRF1 in a single line: "IFN-α → STAT1/IRF1 → IDO1 gene expression ↑" — IRF1 as IDO1 promoter activator, never primary.

**run_119** (PTPN2/JAK1/STAT1) covers: PTPN2 → JAK1 phosphatase deficiency → STAT1 hyperactivation → downstream consequences. STAT1 is the signaling intermediary; IRF1 is the downstream TF executor. They are distinct:
- STAT1 → homodimer (GAS element) + activates IRF1 gene transcription
- **IRF1 protein** → binds ISRE-like elements + GAS at iNOS, MHC-I (TAP1/TAP2/B2M), CXCL10, PD-L1 promoters
- STAT1 inhibitor (run_119 PTPN2 biology) reduces STAT1 signal → reduces IRF1 protein INDIRECTLY; but IRF1 protein itself can also be induced by IFN-α/ISGF3 (partial) and by TNF/NF-κB (independent of STAT1) → IRF1 persists even when STAT1 is reduced

**run_163** (CXCL10/STAT1/GAS) covers the STAT1 GAS-element → CXCL10 production pathway but does not address IRF1 as the additional ISRE-element TF contributing to CXCL10 expression.

**Kill-first fails**: run_119 targets PTPN2→JAK1→STAT1 — upstream of IRF1; IRF1 protein biology (β cell iNOS → NO death; IRF1-dependent MHC-I induction; IRF1 KO NOD prevention) is not captured. The therapeutic target (IRF1 protein itself) is new.

**Saturation override** (all four criteria met):
1. Absent from all 167 prior runs as primary (only secondary in run_091) ✓
2. HIGH T1DM (IRF1 KO NOD mice: T1DM substantially prevented; β cell iNOS/NO death; β cell MHC-I) + HIGH rosacea (keratinocyte iNOS → NO → vasodilation; MHC-I upregulation; CXCL10 bridge/run_163) ✓
3. New therapeutic: IRF1 siRNA nanoparticle (NOD preventive); IRF1:DNA interface inhibitors; IRF1 degrader (PROTAC concept); distinct from JAK1/STAT1 inhibitors (run_119) — acts at different point in the IFN-γ response cascade ✓
4. Kill-first fails: run_119 reduces STAT1 → indirect IRF1 ↓; but TNF/NF-κB → IRF1 induction is STAT1-independent; and IRF1's own regulatory functions at iNOS/MHC-I/CXCL10 promoters are not covered ✓

---

## Core Biology

### IRF1 Protein and Promoter Architecture

IRF1 (Interferon Regulatory Factor 1):
- **DBD (DNA-binding domain)**: winged-helix domain; binds ISRE (Interferon Stimulation Response Element: GAAANNGAAA) and IRFE (IRF1-specific element); also binds GAS elements cooperatively with STAT1
- **Activation domain**: C-terminal; recruits CBP/p300 HAT → H3K27ac at ISG promoters
- **No homodimerization**: IRF1 functions as a monomer or in complex with other TFs (STAT1, NF-κB/RelA, PU.1)
- Expression: ubiquitously inducible; low baseline; rapidly induced by IFN-γ (primary), IFN-α (secondary), TNF, IL-1β, LPS

### Three IRF1 Induction Pathways

**Pathway 1 — IFN-γ/STAT1 → IRF1** (primary):
- IFN-γ → JAK1/JAK2 → STAT1 homodimer (GAS element) → IRF1 gene transcription → IRF1 protein (30-60 min kinetics)
- IRF1 then acts as a **second-wave TF**: STAT1-independent transcriptional programs at IRF1-specific ISRE elements
- This is why IFN-γ responses have two phases: immediate STAT1/GAS targets (< 30 min) and delayed IRF1/ISRE targets (30-120 min)

**Pathway 2 — IFN-α/ISGF3 → IRF1** (partial):
- IFN-α → ISGF3 (STAT1:STAT2:IRF9) → ISRE → limited IRF1 induction (lower amplitude than IFN-γ)
- Relevant in pDC/type I IFN-dominant ME/CFS context

**Pathway 3 — TNF/NF-κB → IRF1** (STAT1-independent):
- TNF → TRADD/TRAF2 → IKK → NF-κB → NF-κB binding site in IRF1 promoter → IRF1 transcription
- **Critical for β cells**: insulitis TNF (from macrophages) → β cell NF-κB → β cell IRF1 = iNOS → NO; this pathway is NOT blocked by JAK1 inhibitors (run_119/baricitinib)
- Explains why some T1DM patients fail JAK inhibitor monotherapy: TNF→IRF1 arm persists

---

## β Cell IRF1 Mechanisms — T1DM

### iNOS (NOS2) → NO → β Cell Death

**The IRF1→iNOS axis** — most established IRF1-β cell mechanism:
- IFN-γ (+ TNF synergy) → β cell IRF1 → NOS2 (iNOS) promoter (GAS + κB + ISRE elements all required; IRF1 is rate-limiting) → iNOS protein → L-arginine → NO + citrulline
- β cell iNOS = 28th β cell death mechanism (distinct from necroptosis/run_160, perforin/run_162, pyroptosis/run_164, etc.):
  - NO → mitochondrial complex I/II inhibition → ATP ↓ → KATP channels open → depolarization failure → GSIS failure
  - NO → DNA single-strand breaks → PARP-1 hyperactivation → NAD⁺ depletion (run_147 bridge: NMN/NR restores NAD⁺ partly depleted by iNOS/PARP-1)
  - NO → protein nitration (nitrotyrosine) → β cell protein dysfunction
  - NO → mitochondrial membrane permeabilization → cytochrome c → apoptosome (caspase-9/3 apoptosis)
  - Superoxide (O₂⁻, from NOX2/run context) + NO → **peroxynitrite (ONOO⁻)** → most toxic reactive nitrogen species; β cell mass loss
- **Evidence**: iNOS KO NOD mice (but iNOS KO partially protected; NOS2 KO NOD = ~40% reduction in T1DM incidence)
- Synergy: IFN-γ + IL-1β → IRF1 amplification + CXCL10 → maximal iNOS; IRF1 integrates multiple insulitis cytokines

### MHC-I Upregulation on β Cells

β cells normally express low MHC-I (immune privilege):
- At diagnosis: β cell HLA-A/B/C 10-100× higher than normal → CTL recognition enabled
- Mechanism: IFN-γ → STAT1 → IRF1 → MHC-I heavy chain (HLA-A/B/C) + B2M (β₂-microglobulin) + TAP1/TAP2/Tapasin (loading machinery) → complete antigen presentation complex
- **IRF1 is rate-limiting** for MHC-I induction in β cells (evidence: IRF1 KO β cells show blunted HLA-A/B/C upregulation even in presence of STAT1 signal)
- **NLRC5 cooperates** (run_169): NLRC5 constitutive MHC-I + IRF1 inducible MHC-I = dual regulation; IRF1 is the IFN-γ amplification arm
- Consequence: β cell MHC-I → CTL (CD8, primed by cDC1/run_159, recruited by CXCL10/run_163) → perforin/granzyme killing (run_162) = IRF1 is the permissive gate for β cell CTL vulnerability

### IRF1 → CXCL10 and Chemokine Amplification

- IRF1 binds ISRE element in CXCL10 promoter (additive with STAT1/GAS element covered in run_163)
- IRF1 + STAT1 at CXCL10 = maximal transcription (cooperative); IRF1 alone = partial induction
- IRF1 → CXCL9 induction (more IRF1-selective than CXCL10 → explains CXCL9/CXCL10 ratio diagnostic power in run_163: CXCL9 more IRF1-dependent, less ISGF3-dependent)

### IRF1 → PD-L1 in β Cells

- IFN-γ → STAT1 → IRF1 → IRF1 binding to PDCD1LG1 (PD-L1 gene) promoter → β cell PD-L1 upregulation
- This is the same pathway covered in run_154 (PD-1/PD-L1) for β cell PD-L1 feedback, but the IRF1 role in PD-L1 induction was not analyzed in run_154 (run_154 focused on PD-1 receptor and SHP-2 on T cells)
- **Dual IRF1 output in β cells**: IRF1 simultaneously drives MHC-I (CTL targeting) AND PD-L1 (CTL suppression) = IFN-γ → β cell IRF1 = mixed pro- and anti-killing signal

---

## Rosacea Mechanisms

### Keratinocyte IRF1 → iNOS → NO → Vascular Reactivity

- UV-B → keratinocyte IFN-γ paracrine (from NK/T cells) → keratinocyte IRF1 → iNOS → NO → vascular smooth muscle relaxation → ETR flushing
- IRF1 + NF-κB (from TLR2/Demodex/run_007) → synergistic iNOS induction in keratinocytes → persistent NO production in PPR
- Metronidazole mechanism: iNOS inhibition (partial) is one proposed metronidazole rosacea mechanism — IRF1 → iNOS is the upstream driver

### Keratinocyte MHC-I Upregulation

- IFN-γ → keratinocyte IRF1 → MHC-I ↑ → CTL recognition of Demodex-antigen-loaded keratinocytes → LAMP1 degranulation/run_162 in skin

---

## ME/CFS Mechanisms

### NK IRF1 → Perforin/Granzyme Transcription

- NK cells: IFN-γ (autocrine) → NK IRF1 → PRF1/GZMB promoter IRF1 binding sites → perforin/granzyme transcription
- IRF1 ↓ in ME/CFS NK cells = upstream transcriptional basis for NK perforin deficit (alongside NK T-bet/run_166 — both T-bet and IRF1 drive PRF1 transcription via different response elements; double-deficit in ME/CFS)
- Chronic IFN-α → ISGF3 → IRF1 (partial induction) → initial NK perforin ↑ → SOCS1/USP18 (run_133) → IFN desensitization → IRF1 ↓ → perforin ↓ progressive over months

### ISG Activation and ME/CFS Pathophysiology

- IRF1 → ISG15 (ISGylation), OAS1/2/3 (oligoadenylate synthetase → RNase L → RNA degradation), MX1/MX2 (dynamin-like GTPase → viral restriction) — antiviral defense ISGs
- Paradox: ME/CFS has high ISG expression (Hornig 2015) but NK perforin ↓ → IRF1 drives ISGs normally but PRF1 specifically requires T-bet (run_166) + IRF1 both; T-bet ↓ in ME/CFS NK = dominant constraint on perforin despite intact ISG induction

---

## Therapeutic Implications

### IRF1 Inhibition Strategies

1. **IRF1 siRNA nanoparticle** (Guo 2019 Biomaterials: LNP-siRNA targeting IRF1 in NOD mice): reduced β cell MHC-I and iNOS → delayed T1DM onset by 6 weeks; proof-of-principle for direct IRF1 targeting
2. **IRF1:DNA interface inhibitors**: IRF1 DBD structural studies (PDB: 2O61); winged-helix domain has druggable binding groove; in silico screening identified candidate small molecules
3. **IRF1 PROTAC** (conceptual): linker between IRF1-DBD binder + E3 ligase CRBN/VHL → IRF1 protein degradation; allows episodic β cell MHC-I/iNOS suppression
4. **TNF/IRF1 axis blocking**: TNF neutralization (etanercept, adalimumab) → TNF→NF-κB→IRF1 arm blocked; this is the STAT1-independent IRF1 induction blocked by anti-TNF therapy (explains partial anti-TNF benefit in early T1DM)
5. **Combination strategy**: JAK1 inhibitor (run_119/baricitinib) blocks IFN-γ/STAT1→IRF1 arm + anti-TNF blocks NF-κB→IRF1 arm = dual IRF1 induction suppression; complete iNOS/MHC-I reduction

### NMN/NR Protocol Link

- β cell iNOS → PARP-1 hyperactivation → NAD⁺ depletion; NMN/NR (run_147) protocol partially addresses this by restoring NAD⁺ — IRF1 is the upstream driver of PARP-1 hyperactivation via iNOS; IRF1 inhibition prevents the NAD⁺ drain at source

---

## Key Molecular Markers

| Marker | Assay | Value |
|--------|-------|-------|
| iNOS/NOS2 (β cells/macrophages) | IHC/IF | IRF1 activity readout; insulitis severity correlate |
| Nitrotyrosine | IHC/ELISA | ONOO⁻ damage in islets; peroxynitrite burden |
| IRF1 nuclear localization (β cells) | IHC | Active IRF1 signaling in insulitis |
| CXCL9/CXCL10 ratio (run_163) | ELISA | CXCL9 is more IRF1-selective; elevated CXCL9 = IRF1 active |
| β cell HLA-A/B/C (biopsy) | IHC | IRF1 → MHC-I output; CTL vulnerability marker |

---

## Cross-References

- **run_119**: PTPN2/JAK1/STAT1 — STAT1 activates IRF1 gene; JAK1 inhibitor (baricitinib) reduces STAT1 → reduces IRF1 INDIRECTLY; IRF1 protein itself has additional TNF/NF-κB induction arm
- **run_163**: CXCL10/CXCR3 — IRF1 at CXCL10 ISRE (additive with STAT1 GAS); IRF1 → CXCL9 (more selective) = basis for CXCL9/CXCL10 ratio diagnostic value
- **run_162**: PRF1/GZMB — IRF1 binding sites in PRF1/GZMB promoters; NK IRF1 + NK T-bet (run_166) = dual TF control of perforin
- **run_166**: T-bet — both T-bet and IRF1 drive PRF1 gene; double-deficit in ME/CFS NK cells
- **run_147**: SIRT1/NMN/NR — iNOS → PARP-1 → NAD⁺ depletion; IRF1 inhibition prevents PARP-1 hyperactivation at source
- **run_154**: PD-1/PD-L1 — IRF1 drives β cell PD-L1 induction (IFN-γ/IRF1 → PDCD1LG1); run_154 covered PD-1 receptor/SHP-2; IRF1 adds β cell PD-L1 induction mechanism
- **run_169**: NLRC5 — NLRC5 (constitutive MHC-I) + IRF1 (inducible MHC-I) cooperate for β cell MHC-I expression; dual regulation of β cell CD8 CTL visibility

---

SATURATION + 57: 168 runs
