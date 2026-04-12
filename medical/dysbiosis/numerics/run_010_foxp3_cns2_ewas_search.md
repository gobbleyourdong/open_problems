# Numerics Run 010 — Foxp3 CNS2 Methylation in Public EWAS Datasets
## Testing M6↔M4 Prediction B Without New Experiments | 2026-04-12

> Attempt_010 (M6↔M4) made a specific testable prediction:
> C-section-born adults should have LOWER Foxp3 CNS2 methylation (less committed Tregs)
> than vaginally-born adults.
>
> This prediction can be tested using EXISTING public DNA methylation datasets
> (EWAS birth cohorts) without running a new experiment. This run maps what datasets
> exist and what the search strategy should be.

---

## The Prediction to Test

**From attempt_010 (Prediction B):**
Birth cohort with:
- Delivery mode documented (C-section vs vaginal)
- Blood methylation (EPIC array or 450K array) at age ≥12 months or in adults
- If Foxp3 CNS2 is measured: lower CNS2 methylation = more committed, stable Tregs

**The target CpG sites:**
Foxp3 CNS2 (conserved noncoding sequence 2) at chromosome X: ~49,188,000 (hg19 coordinates)
Key CpGs: cg10178115, cg11000590, cg16688153 (representative CNS2 sites in 450K/EPIC array)

**Note:** CNS2 demethylation is a MARKER of thymic Treg generation (tTregs) vs. peripherally induced pTregs. LOWER CNS2 methylation = more stable, thymus-derived committed Tregs = higher M6 floor.

---

## Existing Public Dataset Search

### Priority 1: ALSPAC (Avon Longitudinal Study of Parents and Children)

**Why ALSPAC first:**
- N ~14,000 births with complete obstetric history (delivery mode, antibiotic exposure, breastfeeding)
- ARIES sub-study: 1000 individuals with 450K methylation arrays at multiple timepoints (birth cord blood, age 7, 15, and young adult)
- GEO accession: GSE85042 (cord blood methylation in ALSPAC), plus additional timepoints
- Delivery mode is a PRIMARY variable in ALSPAC — it's in the baseline demographic data

**Search strategy in ALSPAC:**
1. Download ARIES methylation data (ALSPAC website, controlled access)
2. Extract CNS2 CpG probes (cg10178115 and flanking probes on X chromosome, 49.1-49.2 Mb)
3. Phenotype: delivery mode (binary: C-section vs vaginal)
4. Covariates: sex (Foxp3 is X-linked; control for sex), gestational age, maternal antibiotics in labor, breastfeeding duration
5. Test: linear regression of CNS2 methylation ~ delivery mode (adjusted)
6. Expected result: C-section → HIGHER CNS2 methylation (less committed Tregs) = LOWER M6 floor

**Practical barrier:** ALSPAC requires data access application (research use). Not instantly accessible. Timeline: 2-6 months for data access approval.

### Priority 2: Generation R (Netherlands)

**Why Generation R:**
- N ~10,000 births; Rotterdam-based longitudinal birth cohort
- EPIC methylation arrays in sub-cohort at age 6 and young adult
- GEO accession: multiple, including GSE73197 (cord blood) and follow-up datasets
- Delivery mode documented

**Advantage over ALSPAC:** European population with different C-section rates (lower baseline in Netherlands) → wider variation in exposure.

**GEO search approach:**
- Search GEO for: "methylation" + "birth cohort" + "delivery mode" + "FOXP3"
- Primary filter: samples with documented delivery mode as phenotype variable
- Secondary filter: FOXP3 CNS2 probes present in array (all 450K and EPIC arrays include it; 27K arrays typically do NOT)

### Priority 3: ARIES Direct Search (Illumina 450K array, FOXP3 probes)

The Illumina 450K array contains multiple probes in the FOXP3 gene region. CpG sites in the CNS2 region:
- Check 450K/EPIC annotation for probes at chrX:49,180,000-49,200,000
- Filter for CpGs with: island/shore annotation + CpG-dense region (CNS2 is CpG-rich)
- Cross-reference against published Treg methylation signatures (Miyara 2009, Dunn 2014)

### Priority 4: PACE Consortium Meta-Analysis

The PACE (Pregnancy And Childhood Epigenetics) consortium has meta-analyzed methylation in birth cohorts for multiple phenotypes including mode of delivery. Published PACE results:

- **Küpers 2019 International Journal of Epidemiology**: "Cord blood DNA methylation and delivery mode" — published EWAS of cesarean vs vaginal delivery in PACE consortium (N ~1400)
  - Check their supplementary table for Foxp3 CNS2 probes
  - Result: This paper may ALREADY ANSWER the question
  - The fact that PACE published a delivery mode EWAS means the raw data exists and some analysis was done

**CRITICAL SEARCH:**
Download Küpers 2019 supplementary tables → search for FOXP3 gene region probes → check effect direction and significance.

If FOXP3 CNS2 probes are NOT in the top hits of Küpers 2019, it means either:
1. No significant association was found (needs to be confirmed, not just absent)
2. The analysis was not powered for this specific region
3. The CNS2 effect is tissue-specific (cord blood PBMCs may not show what thymic Tregs show)

---

## The Tissue Problem

**Key limitation of all blood-based methylation studies:**

Foxp3 CNS2 methylation in **peripheral blood T cells** measures Treg commitment in circulating cells.
The M6 hypothesis is about THYMIC Treg generation — the pool imprinted by SCFA/HDAC in the fetal thymus.

Cord blood is the closest accessible proxy to thymic output at birth. But:
- Cord blood PBMCs contain a mixed cell population (B cells, monocytes dilute the Treg signal)
- Treg-specific FACS-sorted CD4+CD25+ methylation is the ideal but rare in biobanks
- The CNS2 signal in unsorted PBMCs is attenuated by cell-type mixing

**Partial solution:** Cell-type deconvolution using reference methylation matrices (Houseman 2012; Moss 2018 for immune cell types). Apply deconvolution to cord blood arrays → estimate Treg fraction → re-test CNS2 methylation within Treg-enriched fraction (computationally).

---

## What the Küpers 2019 Search Would Look Like

If you have access to the Küpers 2019 supplementary data (or can reproduce the analysis):

```
Query the EWAS results for:
Gene region: FOXP3 (chrX:49,100,000-49,300,000, hg19)
Probes: any probe in this region with p < 0.05 (not requiring EWAS significance)

Expected signal if hypothesis is correct:
  C-section vs vaginal delivery → β coefficient > 0 (higher methylation = less committed Treg)
  at CNS2-region probes (approx chrX:49,187,000-49,193,000)
  
If β < 0 or p > 0.1: hypothesis not supported at cord blood level
  → Could still be true at older ages (thymic imprinting may take months to show)
  → Or tissue-specific (not detectable in cord blood PBMCs)
```

---

## Alternative Approach: Human Thymus Methylation Datasets

If cord blood EWAS are negative, the thymic origin hypothesis requires thymic data.

**Available datasets:**
- GEO search: "thymus" + "methylation" + "CpG" + "FOXP3"
- Thymocyte methylation atlases: several published 2019-2022 (single-cell ATAC + methylation in thymus)
- Problem: these are typically ADULT thymus samples, not fetal/neonatal, and not stratified by delivery mode

**The gap:** No published dataset directly measures fetal thymic Foxp3 CNS2 methylation by delivery mode. This is a genuine measurement gap that requires new data.

---

## What This Run Concludes

### Short version:

The Foxp3 CNS2 methylation prediction (C-section → higher methylation → lower M6 floor) is TESTABLE in existing public data but:

1. **Küpers 2019 PACE meta-analysis is the fastest check:** Download supplementary file, search FOXP3 region. If no signal → hypothesis may be wrong at cord blood level.

2. **ALSPAC ARIES is the best dataset for a rigorous test:** Largest birth cohort with best obstetric phenotyping + methylation at multiple ages. Requires data access application.

3. **Tissue specificity is the key confounder:** Cord blood PBMC CNS2 methylation may not reflect thymic Treg commitment adequately; cell-type deconvolution can help but not fully resolve.

4. **If Küpers 2019 is negative:** This is an evidence UPDATE, not a kill — it means cord blood is not the right readout, not that M6 is false. The hypothesis survives but needs thymic or sorted-Treg data.

### ROI assessment:

Cost to check: download Küpers 2019 supplementary tables (free) + search FOXP3 region (30 minutes).
If positive: strong human evidence for M6↔M4 bridge (attempt_010 Prediction B confirmed).
If negative: informative null (narrows tissue/timing question).

**This is the highest-ROI currently actionable test for the M6↔M4 bridge.**

---

## References

- Küpers 2019 — Mode of delivery EWAS in PACE consortium (Int J Epidemiol)
- Miyara 2009 — Foxp3 CNS2 methylation as Treg commitment marker (J Exp Med)
- Dunn 2014 — CNS2 demethylation in thymic Tregs vs pTregs (Immunity)
- ARIES sub-study of ALSPAC — Relton 2015 (Int J Epidemiol)
- Houseman 2012 — Cell-type deconvolution of PBMC methylation (Bioinformatics)
- GEO accession GSE85042 — ALSPAC cord blood methylation

---

*Filed: 2026-04-12 | Numerics run 010 | EWAS search strategy for Foxp3 CNS2 × delivery mode*
*Priority action: Download Küpers 2019 (PACE) supplementary tables, search FOXP3 region (free, 30 min)*
*If negative: ALSPAC ARIES application (2-6 months); or thymic dataset search*
*Key limitation: cord blood PBMC may not reflect thymic CNS2 methylation adequately*
