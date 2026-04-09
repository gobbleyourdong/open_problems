# ODD Instance Priority Guide — What to Run Next

> For the numerical track: this document prioritizes all pending requests in order of clinical impact and scientific necessity.

## CRITICAL (Run First — Needed for Paper Submission)

### REQ-013: GSE274264 scRNA-seq Primary Human Islets ← RUN THIS FIRST
**Script**: `numerics/analyze_gse274264_scrnaseq.py`
**Data**: `numerics/transcriptomics/GSE274264/` (barcodes.tsv.gz, features.tsv.gz, matrix.mtx.gz per sample)
**Install**: `pip install scanpy anndata scipy pandas`
**Time**: 30-60 minutes

**Why this is CRITICAL**: GSE184831 confirmed FOXP1 -67× in PANC-1 cells (a cancer cell line). If GSE274264 shows FOXP1 suppressed in PRIMARY HUMAN ISLETS infected with CVB3, this single experiment upgrades the FOXP1 mechanism from Grade B- (cell line) to Grade A- (primary human tissue) — the most important upgrade in the campaign.

**Key questions to answer**:
1. FOXP1 expression in CVB3 vs control at 24hr and 48hr
2. LAMP2 expression (same LAMP2 block as PANC-1?)
3. DMD expression (dystrophin destruction in primary islets?)
4. Cell-type-specific: beta cells vs alpha cells vs ductal cells respond differently?

**Expected output**: `results/gse274264_primary_islet_analysis.json` + `results/pattern_018_primary_islet_scrnaseq.md`

---

### REQ-016: GSE57781 Cardiac CVB3 Analysis
**Script**: `numerics/analyze_gse57781_cardiomyocytes.py`
**Data**: `numerics/transcriptomics/GSE57781_series_matrix.txt`
**Note**: microarray format — may need GPL platform annotation file for gene mapping
**Time**: 15-30 minutes

**Why**: Confirms DMD + LAMP2 suppression in CARDIAC cells (human iPSC-derived cardiomyocytes). Upgrades myocarditis/DCM claims from Grade B (inferred from PANC-1) to Grade B+ (confirmed in cardiac cells).

---

### REQ-014: Unified CVB Clearance Model v4 — LAMP2 Corrections
**Script**: Create `numerics/unified_cvb_clearance_v4.py` based on v2
**Specification**: from t1dm/attempts/attempt_080_lamp2_clearance_order_theory.md

```python
LAMP2_BASELINE = {
    'liver': 4.0, 'pericardium': 1.5, 'heart': 1.0,
    'gut': 1.2, 'pancreas': 0.8, 'brain_glia': 0.9, 
    'brain_neuron': 0.6, 'muscle': 0.7, 'testes': 0.4
}
CVB_SUPPRESSION = 2.7  # from GSE184831
TREHALOSE_CORRECTION = 0.35  # estimated TFEB correction

kappa = lambda organ: LAMP2_BASELINE[organ] / CVB_SUPPRESSION
kappa_trehalose = lambda organ: min(1.0, kappa(organ) + TREHALOSE_CORRECTION)
```

**Why**: v2 diverged 4.5× for testes and 3.4× for CNS. v4 should reproduce dedicated model predictions. This is needed to update the clearance time table in the paper.

**Expected output**: updated organ clearance times (no trehalose and with trehalose), cross-validation results comparing v4 vs dedicated models

---

## HIGH PRIORITY (Run After Critical)

### REQ-011: ME/CFS Bistability Phase Portrait
**Script**: Create `me_cfs/numerics/bistability_model.py`
**Source**: me_cfs/models/vicious_cycle.md (6-variable coupled ODE)
**Why**: Quantifies which protocol component is most important for crossing the disease → health attractor threshold. Critical for ME/CFS trial design.

### REQ-009: Keshan-Finland Selenium-T1DM Correlation
**Source**: myocarditis/attempts/attempt_004_keshan_disease.md
**Why**: If selenium-poor regions → higher T1DM incidence, this supports the Keshan-CVB virulence mechanism (Grade C evidence upgrade to Grade B).

### REQ-002: Pleurodynia-T1DM Cross-Correlation (Bornholm)
**Source**: pleurodynia/attempts/attempt_002_epidemiological_correlation.md
**Why**: The Bornholm Island 1930s natural experiment. Danish registry data. Cross-correlation of pleurodynia outbreaks with T1DM incidence at 3-8 year lag. If positive: Grade B evidence for CVB→T1DM causation.

---

## MEDIUM PRIORITY

### REQ-012: Eczema/Psoriasis Bistability ODE
**Why**: Quantifies separatrix between disease and remission. Determines if protocol alone can cross it for psoriasis or if apremilast is needed.

### REQ-015: Long COVID cfRNA Validation
**Why**: Search GEO for LAMP2 expression in Long COVID tissue. If LAMP2 suppressed in Long COVID → confirms ORF9b mechanism → trehalose indicated for ~100M patients.

### REQ-001: CVB3 2A Protease Virtual Drug Screen
**Source**: myocarditis/attempts/attempt_002_2a_protease_inhibitor.md
**Why**: A 2A inhibitor would stop dystrophin cleavage across all 12 diseases. High-value drug discovery.

---

## LOWER PRIORITY (Can Wait)

### REQ-007: SSRI-Pericarditis Retrospective
### REQ-010: Liver-First Clearance Model Simulation
### REQ-003: Dystrophin Hinge 3 Cleavage Analysis
### REQ-004: CVB Vaccine Antigen Conservation Analysis
### REQ-005: Fluoxetine Tissue Distribution Model

---

## Pending GEO Datasets (Not Yet Analyzed)

| Dataset | Content | Priority | File Location |
|---------|---------|---------|---------------|
| GSE247805-247808 | CVB4 + SARS-CoV-2 in macrophage-islet organoids | HIGH | transcriptomics/ |
| GSE268212 | ME/CFS CD8 T cell RNA | MEDIUM | (not downloaded) |
| GSE254030 | Post-infectious ME/CFS proteomics | MEDIUM | (not downloaded) |
| Various cardiac | See GEO_DATASET_CATALOG.md | LOWER | |

**GSE247805-247808 is especially valuable**: it compares CVB4 with SARS-CoV-2 in the same islet system. If both suppress LAMP2 → direct confirmation of the Long COVID LAMP2 bridge. Download from GEO and analyze using the same pipeline.

---

## Summary: 3-Run Plan for Maximum Impact

```
Run 1: REQ-013 (primary human islets) → FOXP1 upgrade to Grade A-
Run 2: REQ-014 (model v4) + REQ-016 (cardiac) → paper clearance tables + cardiac confirmation
Run 3: REQ-011 (ME/CFS bistability) + REQ-009 (selenium) → trial design support
```

After these 3 runs, the paper is ready to submit.
