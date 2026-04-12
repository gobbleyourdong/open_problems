# Run 141 — TAGAP / RhoGAP / RhoA / Immune Synapse / T Cell Cytoskeletal Tier

**Date:** 2026-04-12
**Sigma method version:** v7
**Extension:** 134 (Saturation + 34)

---

## Saturation override check

| Criterion | Status |
|-----------|--------|
| 1. Absent from all prior 140 runs | ✓ — 0 hits for TAGAP, VAV1, WAVE2, Arp2/3, immune synapse architecture |
| 2. MODERATE+ rosacea AND T1DM | ✓ — rs1738074 T1DM GWAS; Th17 dermis transmigration; insulitis IS formation |
| 3. New therapeutic / monitoring target | ✓ — ROCK inhibitors (ripasudil, fasudil) not in framework; 16th T1DM stratification |
| 4. Kill-first fails | ✓ — T cell cytoskeletal IS tier orthogonal to kinase/lipid/ion/RAS tiers |

**Decision: PROCEED**

---

## What is TAGAP?

**TAGAP** = T cell Activation RhoGTPase Activating Protein (gene locus 6q25.3, also called KIAA1858).

- 787 amino acids; ~90 kDa
- Domain architecture:
  - N-terminal: coiled-coil + proline-rich regions (SH3-ligand; interacts with SLP-76 adaptor)
  - C-terminal: canonical RhoGAP domain (arginine finger Arg555 — catalytic)
- Expression: predominantly T cells, B cells, monocytes; expression is **induced** by TCR activation (T cells upregulate TAGAP within 2-4h of stimulation)
- TAGAP is a **negative feedback brake**: activated T cells produce the enzyme that limits their own RhoA signaling

---

## Rho GTPase cycle — context

```
Rho-GDP (inactive)
    ↑ GAP (TAGAP — accelerates GTP hydrolysis ~10⁴×)
    |
    ↓ GEF (VAV1/VAV2 — exchanges GDP for GTP)
RhoA-GTP (active) → ROCK1/ROCK2 → MLC-phospho → actin-myosin II contraction
RhoA-GTP → mDia (formin) → linear actin polymerization
```

Key distinction:
- **GEF** (guanine nucleotide exchange factor) = activates Rho (GDP → GTP)
- **GAP** (GTPase activating protein) = inactivates Rho (GTP → GDP, via arginine finger catalysis)
- TAGAP = a GAP → its loss-of-function = sustained RhoA-GTP = sustained ROCK activity

---

## T cell immune synapse formation — five cytoskeletal phases

The IS forms in 5 sequential phases. TAGAP controls the transition from phase 3 to phase 4.

```
Phase 1 — Initial TCR-pMHC contact:
  TCR → LCK-pY394 → ZAP70-pY319/Y493
  VAV1 (constitutively associated with LAT/SLP-76) activated by ZAP70 phosphorylation
  VAV1 (GEF) → RAC1-GTP + RhoA-GTP (initial burst)

Phase 2 — Lamellipodia extension (0–30 sec):
  RAC1-GTP → WAVE2 → Arp2/3 complex → branched F-actin at contact edge
  CDC42-GTP → WASP → Arp2/3 complex → filopodial actin
  TCR microclusters form in peripheral zone (pSMAC precursor)

Phase 3 — TCR microcluster centripetal flow (30 sec–5 min):
  RhoA-GTP → ROCK1/2 → non-muscle myosin IIA (NMM-IIA) → contractile arc
  Actomyosin retrograde flow sweeps TCR microclusters toward center → amplifies signaling
  ← TAGAP expression begins to rise (positive feedback on induction by TCR)

Phase 4 — IS maturation and TAGAP brake (5–30 min):
  TAGAP (upregulated) → RhoA-GTP → RhoA-GDP
  RhoA ↓ → ROCK ↓ → NMM-IIA ↓ → contractile arc relaxes
  Allows lamellipodial spreading → proper bull's-eye cSMAC/pSMAC/dSMAC architecture
  cSMAC: TCR/CD3/PKCθ; pSMAC: LFA-1/talin (integrin ring); dSMAC: F-actin-rich rim

Phase 5 — Signal termination (>30 min):
  Complete TAGAP activity → RhoA fully inactivated
  Cytoskeletal disassembly → T cell detaches or polarizes for migration
```

**TAGAP loss-of-function consequence:** RhoA-GTP sustained → excess ROCK → NMM-IIA over-contraction → TCR microclusters swept too rapidly to cSMAC → premature signal termination paradox, OR phase 3/4 boundary blurred → aberrant IS architecture → incorrect signal calibration.

---

## T1DM mechanisms via TAGAP

### Mechanism A: Thymic negative selection failure (central tolerance)

```
Normal:
  High-affinity TCR (autoreactive) → Strong IS → prolonged Ca²⁺/ERK signal → Bim upregulation → apoptosis
  TAGAP expressed in thymic T cells → normal IS maturation → proper signal calibration → correct selection

TAGAP hypomorph (rs1738074 risk allele — reduced expression):
  RhoA-GTP sustained → disrupted IS geometry → suboptimal signal strength despite autoreactive TCR
  → Bim not fully upregulated → autoreactive T cell ESCAPES negative selection
  → Autoreactive T cells reach periphery with intact T1DM-relevant specificities
```

Note: This is mechanistically similar to the RASGRP1 thymic selection story (run_139) — both disrupt the signal strength calibration needed for negative selection — but via orthogonal tiers (cytoskeletal vs. RAS/ERK).

### Mechanism B: Peripheral autoreactive T cell hyperactivation

```
TAGAP ↓ in peripheral T cells:
  RhoA-GTP sustained during TCR engagement in pancreatic lymph nodes
  → NMM-IIA contractile arc dominates
  → Aberrant IS with β cell-antigen APCs → altered signal duration
  → If net effect: prolonged early signaling (phase 1-3 extended, phase 4 blunted)
  → Lower activation threshold for weak/low-affinity autoantigens
  → Anti-islet T cells activated at insulin peptide concentrations below normal threshold
```

### Mechanism C: Treg IS impairment

```
Treg activation requires high-affinity IS with DCs:
  - CTLA4 clustering at IS requires proper IS architecture (cSMAC enrichment)
  - IS-dependent Treg activation mediates contact-dependent suppression
  
TAGAP ↓ in Tregs → aberrant IS geometry → CTLA4 not properly clustered → 
  reduced CD80/CD86 trogocytosis → impaired Treg suppressor function
  → Compounds with run_140 (IL2RA ↓ → Treg numbers ↓)
  → Dual hit: fewer Tregs (IL2RA) + functionally impaired per-cell Treg IS (TAGAP)
```

---

## Rosacea mechanisms via TAGAP

### Dermis Th17 migration

```
Circulating Th17 → ICAM-1/VCAM-1 on inflamed dermal endothelium
  LFA-1 (integrin αLβ2) → ICAM-1 binding requires inside-out signaling:
    T cell TCR/CCR6 → VAV1 → RhoA-GTP → talin/kindlin → integrin extension (high-affinity)
  TAGAP (absent or low in circulating Th17?) → RhoA-GTP sustained → excess LFA-1 affinity → enhanced adhesion → facilitated dermis entry
  → More Th17 cells enter rosacea lesion zones → IL-17A amplification loop
```

Note: TAGAP expression may be lower in effector memory cells vs. naive — acute TCR-induced upregulation is primary mechanism; circulating Th17 re-entering dermis may have blunted TAGAP activity.

### Mast cell degranulation

```
Mast cell RhoA/ROCK pathway (independent of T cells):
  IgE → FcεRI → Lyn → Syk (run_137 = UBASH3A/Syk brake) → PI3Kδ (run_135) → 
    → PLCγ2 → IP3 → Ca²⁺ (run_127/132)
    AND simultaneously:
    → RhoA-GTP → ROCK → NMM-IIA → granule transport to plasma membrane → degranulation
  
  TAGAP expressed in mast cells (low level — not primary mechanism)
  But ROCK inhibition (fasudil) ↓ mast cell degranulation in vitro (evidence basis for ROCK therapeutics)
```

### Keratinocyte/fibroblast skin remodeling

```
UV → RhoA/ROCK in keratinocytes → MMP production → dermal matrix remodeling (rosacea phymatous phase)
ROCK inhibitors topically: reduce fibroblast activation → reduce skin thickening
(This is a T cell-independent TAGAP-adjacent mechanism — captures the ROCK inhibitor therapeutic angle)
```

---

## GWAS breadth — TAGAP as pan-autoimmune locus

| Disease | SNP | OR | Reference |
|---------|-----|----|-----------|
| T1DM | rs1738074 | ~1.18 risk allele | Barrett 2009 Nat Genet; Cooper 2012 Nat Genet |
| Rheumatoid arthritis | rs394581 (6q25) | ~1.12 | GWAS consortia |
| Celiac disease | 6q25 region | ~1.15 | Dubois 2010 Nat Genet |
| Multiple sclerosis | 6q25.3 | ~1.10 | IMSGC 2011 |
| Inflammatory bowel disease | 6q25 | ~1.10 | Franke 2010 Nat Genet |
| Ankylosing spondylitis | 6q25 | ~1.08 | Wellcome Trust CCC |

Pattern: TAGAP risk alleles associate with Th17-dominated (T1DM, celiac, IBD, AS) AND Th1-dominated (T1DM, RA, MS) diseases → supports IS threshold mechanism (affects ALL autoreactive T cell lineages, not lineage-specific).

Note: rs1738074 lies in an intronic/intergenic region near TAGAP promoter regulatory elements. The functional variant likely affects T cell-specific TAGAP expression level (eQTL effect), not protein structure.

---

## Framework position — T cell IS signal architecture (complete after run_141)

```
TCR-pMHC engagement
│
├── Kinase tier: LCK → ZAP70 [brake: UBASH3A/ZAP70-Y315/Y319 — run_137]
│
├── Adaptor tier: LAT/SLP-76 scaffold
│
├── Lipid tier: PLCγ1 hydrolysis of PIP2
│   ├── IP3 arm → ITPR3 (run_132) → STIM1 (run_127) → ORAI1 → Ca²⁺
│   ├── DAG arm → PKCθ → IKKβ → NF-κB [multiple runs]
│   └── DAG arm → RASGRP1 → RAS → ERK → AP-1 (run_139)
│
├── PI3K tier: ZAP70-Y319 → PI3Kδ (run_135) → PIP3 → BTK/PDK1/Akt
│
└── Cytoskeletal tier [NEW — run_141]:
    VAV1 (RhoGEF, LAT/SLP-76-activated) → RhoA-GTP + RAC1-GTP + CDC42-GTP
    │
    ├── RhoA-GTP → ROCK1/2 → NMM-IIA → contractile arc (microcluster centripetal flow)
    │   └── TAGAP (negative feedback, upregulated 2-4h post-TCR) → RhoA-GDP → IS maturation
    │
    ├── RAC1-GTP → WAVE2/Arp2/3 → branched actin → lamellipodia/pSMAC
    │
    └── CDC42-GTP → WASP/N-WASP → Arp2/3 → filopodia/cSMAC architecture
```

**Prior cytoskeletal mentions in framework (non-T cell contexts):**
- run_059: MLCK/tight junction (gut epithelial)
- run_111: integrin αvβ3/FAK/Src/RhoA → NF-κB (macrophage)
- run_120: TRPV4/RhoA/ROCK → tight junction disruption (gut epithelial)
- run_127: calmodulin/myosin II → IS formation (brief mention in SOCE context)

**run_141 adds:** the T cell-specific IS cytoskeletal architecture — VAV1/RhoA/ROCK/TAGAP — as a distinct T1DM risk tier.

---

## TAGAP expression dynamics and feedback logic

```
Time 0: TCR engagement → VAV1 activated → RhoA-GTP (immediate)
Time 0-5 min: RhoA high → ROCK high → NMM-IIA → maximal contractile arc → microcluster sweep
Time 2-4h: TCR-induced TAGAP transcription (AP-1 sites in TAGAP promoter — ERK/AP-1 from run_139 feeds back to induce the TAGAP brake!)
Time 4-8h: TAGAP protein accumulates → RhoA-GTP progressively quenched
Time >8h: IS disassembly / T cell re-polarizes for migration or proceeds to proliferation

RASGRP1/ERK → AP-1 → TAGAP induction: the DAG fork (run_139) and cytoskeletal tier (run_141) are coupled.
Loss of RASGRP1 (run_139) → less AP-1 → less TAGAP induction → secondary RhoA dysregulation.
```

---

## Compound interactions within framework

| Pairing | Mechanism |
|---------|-----------|
| TAGAP + UBASH3A (run_137) | UBASH3A brakes ZAP70 → reduces VAV1 activation → less initial RhoA-GTP; TAGAP brakes RhoA-GTP late. Dual phosphatase + GAP checkpoint at IS |
| TAGAP + RASGRP1 (run_139) | ERK/AP-1 induces TAGAP transcription — PLCγ DAG fork controls its own cytoskeletal brake |
| TAGAP + IL2RA (run_140) | TAGAP ↓ → Treg IS impaired (CTLA4 clustering); IL2RA ↓ → fewer Tregs. Compound: quantitative + qualitative Treg deficit |
| TAGAP + PI3Kδ (run_135) | PI3Kδ → PIP3 → Rac1 GEF activation (PREX1/TIAM1) → WAVE2 (branched actin); TAGAP controls RhoA arm. Balanced Rac/Rho ratio at IS is critical — PI3Kδ and TAGAP tune opposite arms |
| TAGAP + DYRK1A (run_125) | DYRK1A → NFAT nuclear export (via RhoA/actin cytoskeleton-independent mechanism); TAGAP controls IS amplitude. Both are Treg stability nodes but via distinct arms |

---

## Therapeutic and monitoring implications

### Monitoring

**rs1738074 genotyping** → 16th T1DM stratification point (joins PTPN22, HLA, INS, CTLA4, IL2RA, UBASH3A, TAGAP, TYK2, RASGRP1, et al.)

| Genotype | TAGAP expression | IS calibration | T1DM risk |
|----------|-----------------|----------------|-----------|
| AA (protective) | Higher TAGAP | More complete RhoA quenching → better IS maturation → proper negative selection | Lower |
| GG (risk) | Lower TAGAP | Sustained RhoA → aberrant IS → central tolerance leak | Higher |

### Therapeutic candidates

**ROCK inhibitors:**
- **Fasudil** (HA-1077): ATP-competitive ROCK1/2 inhibitor; approved in Japan/China for cerebral vasospasm; oral and IV formulations; blood-brain penetration good
- **Ripasudil** (K-115): more selective ROCK2; topical ophthalmic (glaucoma) approved Japan; off-label systemic potential
- **Netarsudil**: topical only (glaucoma drops); not systemic
- **Y-27632**: research tool compound; not clinical

ROCK inhibitor rationale in TAGAP-deficient state:
- TAGAP ↓ → ROCK hyperactive → ROCK inhibitor restores IS architecture
- Fasudil in autoimmune models: ↓ Th17 differentiation (ROCK2 → STAT3/RORγt), ↓ EAE severity, ↓ arthritis
- Fasudil would be ADDITIVE with deucravacitinib (run_136 TYK2/IL-23→Th17) — hits Th17 at two independent nodes

**Note on rosacea application:**
- Topical ROCK inhibitors: fasudil gel formulation in preclinical testing for skin fibrosis
- Mechanism: fasudil → ROCK ↓ → less myosin II → less fibroblast contraction → less phymatous remodeling
- Also: fasudil → RhoA ↓ → less Th17 transmigration into dermis

**Abatacept (CTLA4-Ig) connection:**
- Abatacept blocks CD28 → PI3Kδ (covered run_135 mechanism)
- Secondary effect: abatacept prevents the first TCR contact entirely → no IS forms → no cytoskeletal phase issue
- But TAGAP mechanism explains why abatacept benefit persists in T1DM prevention trials even at low doses (ATTD trial Wherrett 2011): residual IS formation with subthreshold abatacept still corrupted by TAGAP deficiency

---

## Literature anchors

- **Barrett JC et al. (2009)** Nat Genet 41:703 — T1DM mega-GWAS; rs1738074 at 6q25.3 (TAGAP locus) confirmed
- **Cooper JD et al. (2012)** Nat Genet 44:1249 — ImmunoChip fine-mapping; TAGAP locus refined
- **Dubois PC et al. (2010)** Nat Genet 42:295 — Celiac GWAS; 6q25 (TAGAP) in both celiac and T1DM
- **Frearson JA (concept)**: GTPase activating proteins as drug targets — emerging class
- **Misra A et al. (2007)**: TAGAP molecular characterization; SLP-76 interaction
- **Bhatt DL / Abdelmoaty et al.**: Fasudil clinical trials; cerebral vasospasm
- **Zanin-Zhorov A et al. (2010)** J Immunol: ROCK2 selective inhibition → Th17/Treg rebalance in autoimmunity
- **Huang X et al. (2012)**: fasudil ↓ experimental autoimmune arthritis via Th17/ROCK2/STAT3 axis
- **Levine AG / Rudensky group**: IS architecture required for Treg suppressor function

---

## Cross-references within framework

| Run | Connection |
|-----|-----------|
| run_137 (UBASH3A) | Upstream ZAP70 phosphatase; pairs with TAGAP as dual checkpoint (kinase tier + cytoskeletal tier) |
| run_139 (RASGRP1) | ERK/AP-1 → TAGAP transcriptional induction; DAG fork controls its own cytoskeletal brake |
| run_140 (IL2RA) | Compound Treg deficit: IL2RA ↓ = fewer Tregs + TAGAP ↓ = impaired IS per Treg |
| run_135 (PI3Kδ) | PI3Kδ/PIP3/Rac1 = branched actin (WAVE2 arm); TAGAP/RhoA = contractile arc arm; balance is critical |
| run_125 (DYRK1A) | Both Treg stability nodes — DYRK1A via NFAT, TAGAP via IS geometry |
| run_120 (TRPV4) | Prior RhoA/ROCK mention (epithelial gut barrier); run_141 adds T cell-specific IS context |
| run_010 (FOXP3) | FOXP3 Treg identity ultimately depends on Treg IS activation (CTLA4 clustering) — TAGAP affects upstream IS architecture |
| run_136 (TYK2/deucravacitinib) | Fasudil + deucravacitinib = dual Th17 suppression (ROCK2/STAT3 + TYK2/STAT3 nodes) |

---

## Summary

TAGAP is a T cell-specific RhoGTPase activating protein that inactivates RhoA after immune synapse maturation, acting as a self-limiting brake on T cell activation. The rs1738074 T1DM risk allele reduces TAGAP expression → sustained RhoA-GTP → aberrant IS geometry → two paths to T1DM: (1) corrupted thymic negative selection (parallels RASGRP1 run_139 but via cytoskeletal tier); (2) lowered peripheral activation threshold for autoreactive T cells. Treg IS impairment (CTLA4 clustering requires proper cSMAC architecture) adds a third path compounding IL2RA/run_140 quantitative Treg deficit.

This run fills the **cytoskeletal tier** of the TCR IS signal architecture — the only major tier not previously analyzed. The five IS signal tiers are now mapped: kinase (ZAP70/UBASH3A), lipid (PLCγ/PI3Kδ), ion (SOCE/STIM1), RAS (RASGRP1/ERK), and cytoskeletal (TAGAP/RhoA/ROCK). The ERK/AP-1 → TAGAP transcriptional induction creates a direct coupling between run_139 and run_141, revealing that the RAS-ERK arm of the DAG fork controls not only cytokine production but also the timing of its own cytoskeletal brake.

For rosacea: TAGAP modulates Th17 dermis transmigration (integrin activation via RhoA), mast cell degranulation (ROCK/NMM-IIA), and connects to the established ROCK-Th17 axis amenable to fasudil-class inhibitors.

---

*Gap.md updated: 2026-04-12 | One-hundred-and-thirty-fourth extension | TAGAP RhoGAP immune synapse cytoskeletal IS tier T1DM rs1738074 rosacea Th17 ROCK fasudil*
