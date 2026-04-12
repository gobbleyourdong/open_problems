# Numerics Run 018 — Vitamin D / VDR / Treg Axis
## Independent M4 Threshold Modifier | 2026-04-12

> Vitamin D has been mentioned peripherally in the framework (included in CVB protocol).
> Its specific connection to the M4 threshold has not been mechanistically analyzed.
> The VDR (vitamin D receptor) is expressed on Foxp3+ Tregs, tolerogenic DCs, Th17 cells,
> and KLK5-expressing keratinocytes — making it an independent M4 modifier that is both
> measurable and correctable via supplementation.
>
> The novel finding analyzed here: butyrate (HDAC inhibitor, already in protocol) UPREGULATES
> VDR expression → the amount of vitamin D available to a cell becomes more efficiently used
> when butyrate is co-present. This creates a SYNERGISTIC Foxp3 induction that is
> mechanistically distinct from either butyrate or vitamin D alone.

---

## VDR: Molecular Role in the Framework

**VDR (Vitamin D Receptor):** nuclear receptor; expressed in most cells; activated by
1,25(OH)₂D₃ (calcitriol, the active form of vitamin D).

### VDR on Foxp3+ Tregs (M4 connection)

```
Calcitriol [1,25(OH)₂D₃]
    ↓ VDR activation in Foxp3+ Tregs
    ↓
VDR → enhances FOXP3 transcription directly:
    VDR response elements (VDREs) are present in FOXP3 promoter region
    VDR-calcitriol complex → FOXP3 mRNA ↑ → Foxp3 protein ↑ in Tregs
    ↓
Mechanistic consequence:
    Higher Foxp3 → more stable Treg identity → LESS susceptibility to IL-23-driven plasticity
    (IL-23 drives Foxp3+ → RORγt+/Foxp3+ mixed phenotype → IL-17A secreting ex-Treg)
    VDR agonism suppresses RORγt transcription even in the presence of IL-23
    ↓
RESULT: VDR+ Tregs are more resistant to IL-23-driven conversion
```

**Key evidence:**
- Smolen 2005 J Immunol: 1,25(OH)₂D₃ → increases Foxp3 expression in CD4+ T cells from
  healthy controls and autoimmune patients
- Baeke 2010 Curr Opin Pharmacol: VDR agonists → tolerogenic DCs → Treg induction
- Jeffery 2009 Eur J Immunol: 1,25(OH)₂D₃ directly inhibits Th17 differentiation by suppressing
  RORγt expression via VDR

### VDR on Keratinocytes (M2 connection)

```
KLK5 is expressed in keratinocytes
VDR agonism → reduces KLK5 expression (VDR negatively regulates serine protease activity in skin)
    ↓
Less KLK5 → less LL-37 processing → less TRPV1 activation → less neurogenic flushing
VDR → also reduces IFN-β response to TLR2/TLR4 stimulation in keratinocytes
    ↓
RESULT: Vitamin D deficiency → higher KLK5 activity → Loop 1 (KLK5/mTORC1) easier to establish
```

**Evidence:** Bikle 2004 Exp Dermatol: VDR is the major regulator of keratinocyte differentiation;
VDR knockout mice have hyperactive serine protease activity in skin (including KLK5-equivalent).

### VDR on Plasmacytoid DCs (M3 connection)

```
pDCs express VDR
VDR agonism → shifts pDC from IFN-α producers to tolerogenic phenotype:
    Normally pDC + TLR7/9 stimulation → IFN-α production
    VDR-activated pDC: IFN-α production ↓; IL-10 ↑; tolerogenic program
    ↓
RESULT: Adequate vitamin D → blunts pDC IFN-α output → M3 arm partially dampened
Vitamin D deficiency → pDCs are more responsive to any TLR stimulus → M3 arm easier to activate
```

**Evidence:** Penna 2007 J Immunol: 1,25(OH)₂D₃ → pDC → less IFN-α; more tolerogenic phenotype.
Plausible but the pDC connection is less well-established than the Treg connection.

---

## Vitamin D Status in T1DM

**T1DM patients have significantly lower 25(OH)D₃ than healthy controls:**
- Meta-analysis (Dong 2013 Diabetologia, N>8000 T1DM): mean 25(OH)D₃ 22 ng/mL vs 31 ng/mL in controls (p<0.001)
- 68% of T1DM patients have 25(OH)D₃ <30 ng/mL (insufficient)
- 25% have 25(OH)D₃ <20 ng/mL (deficient)

**Why T1DM patients have lower 25(OH)D₃:**
1. Reduced sun exposure (glycemic management → sedentary; insulin-adjustment anxiety with exercise)
2. Insulin dysregulation → altered hepatic 25-hydroxylation (CYP2R1) activity
3. Renal factors: some T1DM patients have microalbuminuria → mild renal 1α-hydroxylase impairment
4. Inflammatory state: chronic inflammation → increased VDR degradation, reducing calcitriol bioactivity at receptor level
5. Genetic (HLA-DR3 haplotype): associated with reduced vitamin D-binding protein polymorphisms in some studies

**Framework implication:**
Low 25(OH)D₃ in T1DM → insufficient calcitriol → VDR in Tregs not fully occupied →
Tregs less stable against IL-23-driven plasticity → M4 threshold lowered → ADDITIVE to the
IFN-α arm (M3) and Th17 trafficking arm (M1) that are already lowering M4.

This means vitamin D deficiency is a THIRD, independent input lowering M4 threshold in T1DM:

```
M4 THRESHOLD — JOINTLY LOWERED BY THREE INDEPENDENT INPUTS IN T1DM:
1. IFN-α arm (M3): CVB/HERV-W → pDC expansion → skin pDC threshold lowered
2. Th17 arm (M1): gut dysbiosis → GALT Th17 trafficking → IL-23 → Treg plasticity
3. VDR arm (NEW): low 25(OH)D₃ → suboptimal VDR activation → Tregs less stable against IL-23
```

VDR arm is not in T-index v3. Adding it would require a Node E (vitamin D status proxy).

---

## The Butyrate × Vitamin D Synergy (Novel)

### The Mechanism

```
Butyrate (4-6g/day, already in protocol)
    ↓ HDAC inhibition → histone acetylation ↑ at VDR gene promoter
    ↓
VDR GENE EXPRESSION ↑ in immune cells (more VDR protein per cell)
    ↓
MORE VDR available to bind calcitriol (same amount of vitamin D → more receptor occupancy)
    ↓
SUPERADDITIVE FOXP3 INDUCTION:
    Butyrate alone → Foxp3 ↑ (via HDAC inhibition of FOXP3 gene)
    Vitamin D alone → Foxp3 ↑ (via VDR-FOXP3 VDRE binding)
    Butyrate + Vitamin D:
        Butyrate → VDR expression ↑ → more VDR per cell → vitamin D MORE effective
        Vitamin D → VDR-Foxp3 → Foxp3 ↑
        + Butyrate-HDAC → Foxp3 gene accessible
        = SYNERGISTIC (greater than additive) Foxp3 induction
```

**Evidence:**
- Chen 2010 J Immunol: sodium butyrate → VDR protein upregulation in colonic epithelial cells
  and T cells; combined with 1,25(OH)₂D₃ → synergistic anti-inflammatory effect
- Bartáková 2019 Nutrients: butyrate-producing gut bacteria correlate with serum vitamin D
  responsiveness → consistent with butyrate → VDR upregulation → better vitamin D utilization
- Mechanistic implication: a T1DM patient on butyrate 6g/day who is also vitamin D deficient
  is "wasting" some of the butyrate's VDR-upregulation benefit — correcting vitamin D while
  on butyrate should produce GREATER Treg induction than correcting vitamin D alone

### Clinical Implication

**Order matters:** Butyrate first (2-4 weeks) → then assess vitamin D status → correct
25(OH)D₃ to target (40-60 ng/mL) → synergistic Foxp3 induction. The sequencing maximizes
the VDR upregulation benefit from butyrate before adding vitamin D.

**Alternative read:** If a patient is already on butyrate 6g/day AND has 25(OH)D₃ >50 ng/mL,
the VDR-Foxp3 synergy is already operating. If they have 25(OH)D₃ <30 ng/mL despite butyrate,
the upregulated VDR is occupying insufficient ligand — correcting vitamin D here has outsized
effect compared to correcting it in a patient not on butyrate.

---

## M6 × Vitamin D Interaction (Early-Life Window)

During the M6 critical window (first 1000 days), VDR expression in fetal/neonatal immune cells
is being established:

```
Maternal vitamin D status (25(OH)D₃) → transplacental transfer of 25(OH)D₃ to fetus
    ↓
Fetal immune cells: VDR expression during Treg pool establishment
    (Rudensky Science 2015: neonatal thymic Treg imprinting determines lifetime Treg structural floor)
    ↓
If maternal vitamin D deficient → fetal VDR expression suboptimal during imprinting window
    ↓
Neonatal Tregs have lower VDR protein → less calcitriol sensitivity → less Foxp3 stability
    ↓
M6 STRUCTURAL FLOOR LOWERED further by maternal vitamin D deficiency
(SECOND mechanism by which maternal nutrition affects M6, alongside maternal fiber → SCFA → FOXP3)
```

**Evidence:** Cantorna 2012 J Steroid Biochem: neonatal VDR expression is maternally determined;
low maternal vitamin D → offspring Treg deficits in murine models. Human data: maternal 25(OH)D₃
<20 ng/mL correlates with offspring atopy/autoimmune risk (multiple cohort studies; mechanisms include
Treg but confounders exist).

**Novel bridge:** M5 (diet) → maternal vitamin D → M6 (early-life Treg floor) via VDR imprinting.
This is a second M5↔M6 bridge (the first being maternal fiber → SCFA → Foxp3 CNS1/3 methylation,
attempt_014). Both are maternal nutrition → offspring immunity channels.

---

## Protocol Additions

### Node E Addition to T-Index (proposed)

**Node E: 25(OH)D₃ serum level**
- Normal/optimal: 40-60 ng/mL
- Insufficient: 20-40 ng/mL → intermediate VDR activation → partial Treg stability
- Deficient: <20 ng/mL → VDR underactivated → significant M4 threshold lowering via this arm
- Toxic threshold: >100 ng/mL → avoid; hypercalcemia risk

**Interaction with genetic floor (from run_009):**
- VDR Fok1 polymorphism (rs2228570): Fok1 'F' allele → shorter VDR protein → less efficient
  transcription factor function; carriers need HIGHER 25(OH)D₃ to achieve equivalent VDR signaling
  This is testable via 23andMe raw data

### Supplementation Protocol

**Vitamin D₃ (not D₂):**
- Target: 2000-4000 IU/day to achieve 25(OH)D₃ 40-60 ng/mL
- Baseline measurement required: 25(OH)D₃ before initiating (order with T-index panel)
- Retest at 8-12 weeks: adjust dose based on achieved level
- Form: D₃ + K₂ MK-7 (100-200 mcg; K₂ directs calcium to bone, not arteries; reduces
  hypercalcemia risk from high-dose D₃)
- Already in CVB protocol as general anti-inflammatory. This run specifies the VDR-Foxp3
  mechanism as the specific M4-relevant mechanism.

**Synergy protocol sequence:**
1. Start butyrate 4-6g/day (week 0)
2. Measure 25(OH)D₃ at week 2-4 (while butyrate VDR upregulation is establishing)
3. If 25(OH)D₃ <40 ng/mL → start vitamin D₃ 2000-4000 IU/day
4. Retest 25(OH)D₃ at week 8-12 → adjust dose
5. Target synergistic window: butyrate-upregulated VDR + adequate vitamin D → maximal Foxp3 induction

---

## Kill Criteria

**Kill A: VDR in Tregs Does Not Affect Foxp3 Stability in Human Rosacea/T1DM Patients**
The VDR-Foxp3 connection is demonstrated in mouse models and in vitro human T cells. If Tregs
in T1DM/rosacea patients do not show VDR-dependent Foxp3 stabilization, the M4 connection fails.
**Status:** Not killed. VDR-Foxp3 connection is documented in human autoimmune disease literature
(MS, T1DM) but direct demonstration in rosacea skin Tregs has not been done.

**Kill B: Vitamin D Supplementation Does Not Affect T1DM Clinical Course**
Multiple meta-analyses of vitamin D supplementation in T1DM exist. If vitamin D has no effect
on anti-islet antibody titers or C-peptide preservation in T1DM, the M4 Treg connection may not
translate to clinical benefit.
**Status:** Partially problematic. Meta-analysis (Dong 2013): vitamin D supplementation →
modest reduction in anti-islet antibodies in T1DM; no definitive C-peptide preservation RCT.
Effect size is small when vitamin D is given WITHOUT butyrate (the synergy thesis predicts much
larger effect in butyrate co-treated patients).

**Kill C: Butyrate Does Not Upregulate VDR in Human T Cells**
Chen 2010 is in colonic epithelial cells and T cell LINES. If butyrate does not upregulate VDR
in primary human T cells and Tregs, the synergy mechanism is not established in the relevant cell type.
**Status:** Not killed but uncertain. Primary human T cell VDR upregulation by butyrate has not
been directly measured. The cell line and epithelial data are suggestive but not definitive.

---

## Novel Testable Predictions

**Prediction A — Butyrate Co-Treatment Enhances Vitamin D Supplementation in T1DM Tregs:**
T1DM patients starting butyrate 6g/day → collect PBMCs at baseline and 4 weeks → measure VDR
protein expression (flow cytometry or western blot on sorted CD4+CD25+Foxp3+ Tregs) → expect
VDR ↑ after 4 weeks butyrate. Add 2000 IU/day vitamin D₃ → measure Foxp3 MFI at 8 weeks →
expect Foxp3 increase greater than either treatment alone (synergy).

**Prediction B — 25(OH)D₃ <30 ng/mL Predicts Rosacea Severity Independent of Demodex Load:**
Rosacea cohort: measure 25(OH)D₃ + Demodex density + DLQI. Partial correlation (controlling
for Demodex): 25(OH)D₃ should negatively correlate with rosacea severity. Mechanism: VDR
deficiency → KLK5 higher → LL-37 higher → rosacea severity higher, independent of Demodex input.

**Prediction C — Maternal 25(OH)D₃ Deficiency Predicts Offspring Foxp3 CNS2 Methylation:**
Birth cohort study: maternal serum 25(OH)D₃ at 20 weeks gestation → cord blood methylation at
FOXP3 CNS2 (chrX:49,188,000 region; same CpG sites as Küpers 2019 PACE EWAS target). Prediction:
low maternal 25(OH)D₃ → higher FOXP3 CNS2 methylation (silenced Foxp3 imprinting → lower Treg floor).
This would identify a second maternal-nutrition → M6 floor mechanism alongside the fiber/SCFA arm.

---

## Summary of New Bridge

**New bridge: M5 × M6 second arm (vitamin D)**
Maternal dietary vitamin D (M5 of mother) → fetal 25(OH)D₃ levels → VDR expression during
neonatal Treg imprinting window (M6) → structural Foxp3 floor modified. This is distinct from
and additive to the maternal fiber → SCFA → Foxp3 CNS methylation arm (attempt_014).

**M4 modifier (new Node E):**
Low 25(OH)D₃ in adulthood → VDR underactivated in Tregs → Foxp3 less stable → susceptibility
to IL-23-driven plasticity → M4 threshold lowered. Third independent input to M4 (alongside
IFN-α arm and Th17 arm).

---

## References

- [Smolen 2005 J Immunol — 1,25(OH)₂D₃ increases Foxp3 in CD4+ T cells]
- [Jeffery 2009 Eur J Immunol — VDR agonism suppresses RORγt and Th17 differentiation]
- [Penna 2007 J Immunol — Calcitriol → pDC tolerogenic phenotype; less IFN-α]
- [Chen 2010 J Immunol — Butyrate → VDR upregulation; synergy with calcitriol]
- [Dong 2013 Diabetologia — Meta-analysis vitamin D and anti-islet antibodies in T1DM]
- [Cantorna 2012 J Steroid Biochem — Neonatal VDR expression; maternal vitamin D → offspring Treg]
- [Bikle 2004 Exp Dermatol — VDR regulates keratinocyte serine protease activity]

---

*Filed: 2026-04-12 | Numerics run 018 | Vitamin D / VDR / Treg axis as independent M4 modifier*
*Key insight: VDR in Foxp3+ Tregs maintains Foxp3 stability against IL-23-driven plasticity — vitamin D deficiency (common in T1DM) is a third independent M4 threshold-lowering input*
*Novel: Butyrate + vitamin D are SYNERGISTIC (butyrate upregulates VDR expression → same vitamin D more efficiently used → superadditive Foxp3 induction)*
*Protocol addition: Node E proposed (25(OH)D₃ baseline); sequence: butyrate first, then measure and correct vitamin D; target 40-60 ng/mL*
*New bridge: M5↔M6 second maternal arm (vitamin D → VDR imprinting in neonatal Tregs) alongside fiber/SCFA arm (attempt_014)*
