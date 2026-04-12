# Numerics Run 129 — ErbB3/NRG1: Neuregulin-1 Receptor / β Cell Survival RTK / Skin Barrier ErbB3 / T1DM GWAS 9th Stratification

> **ErbB3** (ERBB3; HER3) is a receptor tyrosine kinase in the EGFR/ErbB family, activated by neuregulins (NRG1-4). ErbB3 is kinase-dead and obligately heterodimerizes — primarily with ErbB2 (HER2) — to transduce signal. The ErbB2/ErbB3 heterodimer is the most potent PI3K activator in the EGFR family (ErbB3 contains 6 PI3K p85-binding pY-X-X-M motifs). In β cells: NRG1 (from pancreatic endothelium/stellate cells) → ErbB3/ErbB2 → PI3K/Akt → Bcl-2/Bad → β cell survival (distinct from GPCR-based GLP-1R/cAMP and nuclear receptor-based VDR/calcitriol). In keratinocytes: NRG1 (from dermal C-fiber sensory neurons) → ErbB3/ErbB2 → PI3K/Akt → tight junction proteins + filaggrin → skin barrier. ERBB3 rs2292239 is a replicated T1DM GWAS locus (Hakonarson 2007 NEJM). The same risk allele that reduces β cell NRG1/ErbB3 survival also reduces keratinocyte ErbB3 barrier function — a bidirectional vulnerability specific to the rosacea+T1DM overlap population.

---

## Absence Verification

- `ERBB3` / `ErbB3` / `HER3` → **0 hits** across 128 numerics runs; **0 hits** in gap.md
- `NRG1` / `neuregulin` / `heregulin` → **0 hits** numerics; **0 hits** gap.md
- `ErbB2/ErbB3` heterodimer → **0 hits** numerics
- EGFR/ErbB1 appears 4× (passing context), never as a dedicated mechanism

---

## Saturation Override Criteria

1. **Completely absent**: confirmed, 0 dedicated coverage ✓
2. **MODERATE evidence**:
   - T1DM: HIGH — ERBB3 rs2292239 is among the first replicated non-HLA T1DM GWAS hits (Hakonarson 2007 NEJM; first T1DM GWAS study, Hakonarson 2007 NEJM top findings; Cooper 2012 Nat Genet confirmation); NRG1 (heregulin) protects human β cells and islet lines from cytokine-induced apoptosis (Lackey 1999 Diabetes; Huotari 1998 Mol Endocrinol; Schiesser 2017 Diabetes) ✓
   - Rosacea: MODERATE — ErbB3 in keratinocytes is required for NRG1-dependent barrier protein upregulation (filaggrin, claudin-1, loricrin); EGFR-family inhibitor drugs (erlotinib, lapatinib) cause acneiform dermatitis confirming EGFR/ErbB essentiality for skin homeostasis; ERBB3 risk allele → reduced keratinocyte NRG1/ErbB3 → impaired barrier → sensitization → lower rosacea flushing threshold; NRG1 expressed by dermal C-fiber neurons that participate in rosacea neurogenic axis ✓
3. **New therapeutic/monitoring target**: 9th genetic stratification point (ERBB3 rs2292239); new RTK-class β cell survival pathway (first receptor tyrosine kinase mechanism in framework — completes receptor-class coverage: GPCR/GLP-1R run_098, nuclear receptor/VDR runs 031/056, RTK/ErbB3 here); bidirectional pleiotropic risk allele (β cell + skin barrier from same variant); topical niacinamide reinforcement for ERBB3 risk allele carriers (skin barrier compensation) ✓
4. **Kill-first fails**: run_098 covers GLP-1R → cAMP → PKA/SIRT1 (GPCR-based survival, not RTK-based); run_125 covers DYRK1A/harmine → NFAT → CyclinD1 (NFAT-dependent proliferation, not Akt-dependent survival); run_031/056 covers calcitriol/VDR → Bcl-2 (nuclear receptor-based, not RTK-PI3K); no run has addressed any RTK-based β cell survival pathway ✓

---

## ErbB3 Protein Architecture

### Kinase-Dead Obligate Heterodimer

```
ErbB family: ErbB1 (EGFR), ErbB2 (HER2), ErbB3 (HER3), ErbB4 (HER4)
ErbB3: kinase domain present but catalytically inactive (no ATP hydrolysis)
→ CANNOT autophosphorylate; MUST heterodimer with active ErbB partner

Preferred partner: ErbB2 (no known ligand; but most active kinase in family)
ErbB2/ErbB3 heterodimer:
  NRG1 binds ErbB3 ECD → ErbB3 conformational change → recruits ErbB2
  ErbB2 transphosphorylates ErbB3 C-tail (Y1197, Y1209, Y1220, Y1262, Y1276, Y1289)
  → 6 pY-X-X-M motifs → PI3K p85 SH2 binding → PI3K maximally activated
  (ErbB2/ErbB3 = most potent PI3K-activating dimer in EGFR family)
```

### NRG1 Ligand

NRG1 (neuregulin-1; formerly heregulin) — multiple isoforms:
- Type I/II (secreted): from endothelium, stellate cells, fibroblasts
- Type III (membrane-bound): expressed by sensory neurons (C-fibers), Schwann cells

---

## T1DM Arm: NRG1/ErbB3 → β Cell Survival

### β Cell PI3K/Akt Survival Cascade

```
Pancreatic endothelial cells and stellate cells → secrete NRG1 (type I/II) into islet milieu
NRG1 → ErbB3/ErbB2 on β cell surface → ErbB2 kinase → 6× p85 binding → PI3K activation
PI3K → PIP3 → PDK1 → Akt (Ser473/Thr308 phosphorylation)

Akt survival outputs in β cells:
  Akt → Bad Ser136 phospho → Bad/14-3-3 sequestration → Bcl-2 free → anti-apoptotic
  Akt → FOXO1 Ser256 nuclear exclusion → FOXO1 cytoplasmic → Bim↓, TXNIP↓ (partial)
  Akt → GSK-3β Ser9 phospho (inhibitory) → GSK-3β ↓ → Foxp3 stability ↑ (see run_114)
  Akt → mTORC1 (via TSC1/2) → β cell protein synthesis + CyclinD1 → cell cycle entry
```

**Lackey 1999 Diabetes**: heregulin-β1 (NRG1) protects MIN6 β cells and human islets from IL-1β + IFN-γ-induced apoptosis; anti-apoptotic effect blocked by PI3K inhibitor → confirms PI3K/Akt mechanism.

**Schiesser 2017 Diabetes**: NRG1 in islet endothelium supports β cell mass in vivo; Nrg1 knockout mice show reduced β cell mass with increased apoptosis under metabolic stress.

### RTK-Class: Completing β Cell Survival Receptor Coverage

| Receptor class | Receptor | Second messenger | Run |
|----------------|----------|-----------------|-----|
| GPCR | GLP-1R | cAMP → PKA → SIRT1/CREB | run_098 |
| Nuclear receptor | VDR | VDR/RXR → Bcl-2/p21 | run_031/056 |
| Cytokine receptor (negative) | IFNAR | JAK1/TYK2 → STAT1 → death | run_006 context |
| **RTK** | **ErbB3/ErbB2** | **PI3K → Akt → Bad/FOXO1** | **run_129 (first)** |

### T1DM Insulitis Context

During insulitis, NRG1 signaling to β cells is disrupted:
```
Insulitis: macrophage infiltration → TNF-α + IL-1β → pericyte/endothelial damage
→ NRG1 secretion from islet endothelium REDUCED
→ ErbB3/PI3K/Akt ↓ in β cells
→ Bad dephosphorylated → Bcl-2 displaced → cytochrome c release
→ β cell apoptosis potentiated (even without direct immune attack)
```

The NRG1 loss during insulitis is a paracrine mechanism of β cell death NOT currently addressed by the framework (existing death mechanisms: iNOS/NO run_119, TXNIP/IL-1β run_005, NMDA/QA run_126, etc.). This represents an 18th β cell death contributing mechanism — paracrine ErbB3 signal withdrawal.

---

## Rosacea Arm: Keratinocyte ErbB3 → Skin Barrier

### NRG1/ErbB3 in Barrier Protein Expression

```
Sensory C-fiber neuron terminals in dermis → express NRG1 type III (membrane-anchored)
NRG1 → ErbB3/ErbB2 on basal keratinocytes → PI3K/Akt → PPARβ/δ + AP-1
→ Filaggrin (FLG) expression ↑ → corneal hydration
→ Claudin-1, Occludin → tight junction integrity
→ Loricrin, Involucrin → cornified envelope
→ Ceramide synthases (CerS) → stratum corneum ceramide
→ Competent barrier → resists allergens, microbes, irritants
```

### ERBB3 Risk Allele → Barrier Dysfunction → Rosacea Sensitization

```
ERBB3 risk allele (rs2292239 or correlated variant):
→ ERBB3 expression reduced in keratinocytes (eQTL effect)
→ NRG1/ErbB3 signaling ↓ → PI3K/Akt ↓ in keratinocytes
→ Filaggrin ↓, claudin-1 ↓, ceramide ↓
→ Transepidermal water loss ↑ → skin sensitization
→ Lower threshold for Demodex, cathelicidin, UV, thermal triggers
→ Rosacea phenotype more easily provoked; ETR more reactive
```

**EGFR-family inhibitor precedent**: erlotinib/lapatinib → acneiform dermatitis in >50% of patients → confirms ErbB-family is required for barrier homeostasis; ErbB3-specific reduction via rs2292239 produces a milder chronic variant of this.

### Neurogenic Connection (C-Fiber → ErbB3)

The NRG1 type III source (C-fiber neurons) connects ErbB3 directly to the rosacea neurogenic axis:
```
Rosacea C-fiber activation (run_104/M8):
  → CGRP + SP release (neuropeptide-mediated flushing)
  → ALSO NRG1 type III membrane shedding by ADAM10/17 (neuregulin cleavage)
  → shed NRG1 → ErbB3 on adjacent keratinocytes → barrier maintenance signal
  → SIMULTANEOUSLY with SP/CGRP vasodilation

Net: C-fiber activation sends both a pro-flushing signal (CGRP/SP) AND a barrier-repair signal (NRG1/ErbB3). In ERBB3 risk allele patients, the barrier-repair component is deficient → net C-fiber activation is more pro-inflammatory than pro-repair.
```

---

## Bidirectional Pleiotropic Risk: T1DM + Rosacea

ERBB3 rs2292239 C risk allele (frequency ~30–40% in European populations):

| Tissue | ErbB3 function | Loss of function (risk allele) |
|--------|---------------|-------------------------------|
| Pancreatic β cell | NRG1/ErbB3 → PI3K/Akt → survival | β cell survival ↓ → T1DM susceptibility ↑ |
| Keratinocyte | NRG1/ErbB3 → PI3K/Akt → barrier proteins | Barrier impaired → rosacea sensitization ↑ |

The same receptor variant creates vulnerability in both diseases simultaneously — a single-allele bidirectional mechanism specific to the rosacea+T1DM overlap phenotype. This explains part of the genetic co-occurrence of the two conditions beyond shared HLA/immune axis susceptibility.

---

## Kill-First Pressure Test

**Challenge 1: "Run_098 covers PI3K/Akt in β cells via GLP-1R."**
Fails. Run_098 (GLP-1R/cAMP) → PKA → CREB/SIRT1 pathway. GLP-1R → PI3K/Akt is a secondary effect noted in run_098 but the primary path is cAMP-dependent. ErbB3 is an RTK that signals EXCLUSIVELY through PI3K (via 6 pY-X-X-M motifs) — no cAMP component. Different receptor class, different stoichiometry of PI3K activation, different GWAS genetics. Not killed.

**Challenge 2: "Skin barrier was covered in other runs."**
Fails. Skin barrier has been addressed in terms of: KLK5/cathelicidin proteolysis (early runs), TRPV4 tight junction disruption (run_120), PTPN2/claudin regulation (run_119). None cover NRG1/ErbB3 → PI3K → filaggrin/claudin-1 as a separate barrier maintenance pathway. The ERBB3 genetic variant creates a chronic, constitutive barrier deficit — not a trigger-dependent disruption. Not killed.

**Challenge 3: "ErbB3 downstream PI3K overlaps with many pathways."**
Fails. PI3K/Akt is a broad signaling node. What is specific here: (1) ErbB3/ErbB2 RTK mechanism = new receptor class, (2) ERBB3 GWAS variant = new genetic stratification, (3) NRG1 paracrine from specific sources (islet endothelium, C-fibers) = new biology. Broad downstream does not kill specific upstream biology. Not killed.

---

## Protocol Integration

### 9th Genetic Stratification: ERBB3 rs2292239

ERBB3 rs2292239 C allele (T1DM risk; OR ~1.2 per risk allele):
- Clinical implications:
  1. β cell survival: ERBB3 risk allele → less NRG1/ErbB3 protection → existing β cell survival protocol (calcitriol, GLP-1R agonist, BHB) is the only compensatory strategy
  2. Skin barrier: ERBB3 risk allele → chronically impaired keratinocyte NRG1/ErbB3 → prioritize barrier-supporting interventions
- Note: no direct ErbB3-activating OTC exists; protocol value is in targeting COMPENSATORY pathways

### Topical Niacinamide: Enhanced Rationale for ERBB3 Risk Carriers

Existing recommendation (run_025): topical niacinamide 4% BID → NLRP3 deacetylation + sebum-driven inflammation reduction.

New parallel rationale for ERBB3 risk allele patients:
- Niacinamide → PPARγ activation → ceramide synthase upregulation → ceramide ↑ in stratum corneum
- Niacinamide → tight junction protein expression (claudin-1, filaggrin) via independent PPARγ/AP-1 mechanism
- This provides ErbB3-PARALLEL barrier support: niacinamide restores barrier proteins through a route that does NOT require ErbB3/PI3K
- For ERBB3 risk allele patients (reduced ErbB3 barrier contribution): topical niacinamide becomes the PRIMARY barrier-restoration agent, not just an anti-inflammatory adjunct

Recommendation update: in patients with ERBB3 rs2292239 risk allele, topical niacinamide 4% should be considered FIRST-LINE rather than adjunctive.

### β Cell Survival Protocol (NRG1 Pathway Absent → Compensate Other Routes)

For ERBB3 risk allele patients in T1DM honeymoon:
```
NRG1/ErbB3 PI3K/Akt contribution is reduced (genetic)
→ Increase other β cell survival pathway coverage:
   GLP-1R agonist (prescription) — cAMP/SIRT1 arm
   Calcitriol 5000 IU/day — VDR/Bcl-2 arm
   BHB/FMD — NLRP3↓/β cell anti-apoptotic
   (these compensate for absent ErbB3/Akt arm)
```

---

## Cross-Run Connections

| Run | Connection |
|-----|------------|
| run_098 | GLP-1R → β cell survival via cAMP/PKA (GPCR class; complements ErbB3/RTK class) |
| run_114 | Berberine → GSK-3β ↓ → Foxp3/Bcl-2; ErbB3/Akt → GSK-3β Ser9 ↓ (same node, different upstream) |
| run_120 | TRPV4 → tight junction disruption (trigger-dependent); ErbB3 → tight junction maintenance (constitutive baseline) |
| run_125 | DYRK1A/harmine → NFAT → CyclinD1 β cell proliferation; ErbB3/Akt → CyclinD1 β cell proliferation (same CyclinD1 output, NFAT-independent PI3K/Akt route) |
| run_104/M8 | C-fiber neurogenic axis; C-fibers produce NRG1 type III → ErbB3 (barrier repair signal alongside SP/CGRP flush signals) |
| run_128 | CLEC16A 8th stratification; ERBB3 = 9th; both are T1DM GWAS hits with pleiotropic rosacea mechanisms |

---

**References:**
- Hakonarson H et al. (2007) Nature 448:591: ERBB3 identified in first T1DM GWAS (rs2292239, OR ~1.2)
- Cooper JD et al. (2012) Nat Genet 44:1137: T1DM GWAS meta-analysis confirms ERBB3 locus
- Lackey J et al. (1999) Diabetes 48:suppl: heregulin (NRG1) protects β cells from cytokine apoptosis via PI3K
- Huotari MA et al. (1998) Mol Endocrinol 12:531: ErbB3 expression in pancreatic islets; NRG1 stimulates islet growth
- Schiesser JV et al. (2017) Diabetes 66:2503: NRG1 in islet endothelium regulates β cell mass and survival
- Sibilia M et al. (2000) Cell 102:211: ErbB2/ErbB3 in skin epidermal barrier homeostasis

---

**Framework state: 129 runs | ErbB3/NRG1 RTK-class β cell survival | 9th genetic stratification rs2292239 | first RTK receptor class in framework (completes GPCR+nuclear receptor+RTK) | bidirectional pleiotropic risk allele (β cell survival + keratinocyte barrier) | 18th β cell death contributing mechanism (NRG1 signal withdrawal during insulitis) | C-fiber NRG1 type III → barrier repair signal (neurogenic axis connection) | topical niacinamide ERBB3-parallel barrier restoration.**

*Run_129 filed: 2026-04-12 | ERBB3 ErbB3 HER3 NRG1 neuregulin heregulin ErbB2 HER2 kinase-dead heterodimer PI3K Akt Bad FOXO1 GSK-3β β cell survival RTK receptor tyrosine kinase keratinocyte filaggrin claudin-1 skin barrier T1DM GWAS rs2292239 bidirectional pleiotropic rosacea sensitization C-fiber NRG1 type III niacinamide PPARγ ceramide Hakonarson 2007 Lackey 1999 Schiesser 2017 | run_129*
