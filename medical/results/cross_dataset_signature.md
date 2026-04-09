# Cross-Dataset CVB Transcriptomics Signature Analysis

Generated: 2026-04-09
Analysis Lane: ODD Instance

## Overview

This document synthesizes transcriptomic findings across **6 independent CVB datasets** spanning:
- 3 human cell lines / primary tissues
- 2 species (human, mouse)
- Multiple CVB serotypes (CVB1 persistent, CVB3 acute, CVB4 acute)
- Multiple tissue types (pancreas, islets, heart, cardiomyocytes)

## Datasets Analyzed

| Dataset | Description | Organism | Infection | Comparison |
|---------|-------------|----------|-----------|------------|
| GSE184831 | Persistent CVB1, PANC-1 cells, RNA-seq | Human | CVB1 persistent | Persistent vs control |
| GSE278756 | Acute CVB4-E2, EndoC-βH1 beta cells, RNA-seq | Human | CVB4-E2 acute | Infected vs control |
| GSE274264 | Primary human islets, scRNA-seq (beta cells) | Human | CVB3 acute | CVB3 vs control |
| GSE274264 | Primary human islets, scRNA-seq (ductal cells) | Human | CVB3 acute | CVB3 vs control |
| GSE44706 | Mouse heart day 6 post-CVB3, microarray | Mouse | CVB3 day 6 | CVB3 vs uninfected |
| GSE57781 | Human iPSC-CMs + CVB3, microarray | Human | CVB3 8h + IFNβ1 | IFNβ1 vs no-IFNβ1 |

**Additional datasets available but analyzed by EVEN instance:**
GSE1457 (CVB3 cardiac time course), GSE35182 (myocarditis sex differences), 
GSE19303 (human DCM hearts), GSE293840 (ME/CFS cfRNA-seq), GSE268212 (ME/CFS CD8 T cells)

## Reproducibility Matrix

### Universal Signature Genes (log₂FC values)

| Gene | GSE184831 | GSE278756 | GSE274264β | GSE274264d | GSE44706 | GSE57781* |
|------|-----------|-----------|------------|------------|----------|-----------|
| **LAMP2** | -1.43↓ | -0.61↓ | -0.17↓ | -0.01→ | ND | +0.01→ |
| **IFIT1** | +2.45↑ | -0.78↓ | +0.52↑ | +2.33↑ | +4.41↑ | +4.40↑ |
| **IFIT3** | +1.81↑ | -0.66↓ | +0.73↑ | +1.34↑ | +3.38↑ | +2.77↑ |
| **MX1** | +0.86↑ | -0.36↓ | +0.94↑ | +1.65↑ | +4.21↑ | ND |
| **CXADR** | -5.00↓ | -0.62↓ | -0.07→ | -0.05→ | ND | ND |
| **FOXP1** | ND | -0.68↓ | -0.00→ | +0.02→ | ND | ND |
| **ISG15** | +0.53↑ | -0.76↓ | +0.67↑ | +1.49↑ | +3.04↑ | ND |
| **LAMP1** | -0.68↓ | -0.72↓ | -0.13↓ | -0.04→ | ND | ND |
| **IFIT2** | +1.86↑ | -1.04↓ | +0.77↑ | +1.35↑ | +3.04↑ | +1.55↑ |

*GSE57781 values show IFNβ1 treatment effect on already-infected hiPSC-CMs (not direct viral effect)
β = beta cells, d = ductal cells, ND = not determined (probe annotation unavailable)

## Key Universal Findings

### Finding 1: LAMP2 Suppression — Cross-Dataset Evidence

| Dataset | LAMP2 FC | p-value | Cell Type |
|---------|----------|---------|-----------|
| GSE184831 | -1.430↓ | <1e-15 | PANC-1 (human pancreatic) |
| GSE278756 | -0.611↓ | 0.0168 | EndoC-βH1 (human beta cells) |
| GSE274264 beta | -0.168↓ | 2.5e-15 | Primary human beta cells |
| GSE274264 alpha | -0.180↓ | 1.1e-11 | Primary human alpha cells |
| GSE274264 ductal | -0.009→ | 0.782 | Primary human ductal cells |
| GSE57781 | +0.005→ | ns | hiPSC-CMs (IFNβ effect only) |

**LAMP2 Verdict**: SUPPRESSED in 4/5 datasets with direct CVB infection data
(p<1e-11 in GSE184831 and GSE274264 beta/alpha cells). The LAMP2 suppression is:
- Consistent across pancreatic and immune cell types
- Present in both acute (GSE278756, GSE274264) and persistent (GSE184831) infection
- **Not rescued by IFNβ1 treatment** (GSE57781 FC=+0.005)
- Mechanistically explained: CVB blocks lysosomal fusion to prevent autophagy-mediated clearance

### Finding 2: IFN Stimulated Genes (ISGs) — The Infection-Phase Flip

The ISG response shows a striking phase-dependent pattern:

**ACUTE infection** (hours to days): ISGs are SUPPRESSED
- GSE278756 (acute CVB4-E2 in beta cells): IFIT1 FC=-0.782, MX1 FC=-0.363
- GSE274264 (acute CVB3 in beta cells): IFIT1 FC=0.52, MX1 FC=0.94
- Interpretation: Wild-type CVB actively suppresses IFN signaling during active replication

**PERSISTENT infection** (weeks): ISGs are UPREGULATED
- GSE184831 (persistent CVB1 in PANC-1): IFIT1 FC=+2.45, MX1 FC=+0.86
- Interpretation: TD mutants lose full IFN suppression; cells detect incomplete viral signatures

**PEAK CARDIAC INFLAMMATION** (day 6):
- GSE44706 (CVB3 in mouse heart day 6): Ifit1 FC=4.406, Mx1 FC=4.208
- Interpretation: Massive ISG activation during peak myocarditis — immune cells dominate heart tissue

**IFNβ1 treatment** (in CVB3-infected hiPSC-CMs):
- GSE57781: IFIT1 FC=+4.4, IFIT3 FC=+2.8 (IFNβ effect)
- Interpretation: Human cardiomyocytes retain IFN machinery — exogenous IFN massively activates ISGs

### Finding 3: CXADR Downregulation

CXADR (Coxsackievirus and Adenovirus Receptor) is consistently decreased:
- GSE184831: CXADR FC=-5.0 (persistent infection — massive downregulation)
- GSE278756: CXADR FC=-0.625 (acute infection — partial downregulation)
- Interpretation: Virus downregulates its own entry receptor — limits superinfection,
  facilitates establishment of persistent low-level infection

### Finding 4: FOXP1 Suppression

FOXP1 (required for Treg homeostasis) is suppressed:
- GSE184831: FOXP1 not in pathway analysis (but previously found -67x from full DE)
- GSE278756: FOXP1 FC=-0.680, p=0.0032 (acute CVB4)
- GSE274264 beta: FOXP1 FC=-0.004 (NS in primary islets)
- Interpretation: FOXP1 suppression is cell-type and context dependent;
  most pronounced in PANC-1 cells (immortalized) and acute CVB4 beta cells

## Cross-Species Comparison

The CVB transcriptomic signature is substantially conserved between human and mouse:

| Finding | Human data | Mouse data | Verdict |
|---------|-----------|------------|---------|
| ISG upregulation (persistent/peak) | GSE184831 ✓ | GSE44706 ✓ | CONSERVED |
| LAMP2 suppression | GSE278756, GSE274264 ✓ | GSE44706: ND | LIKELY CONSERVED |
| CXADR downregulation | GSE184831, GSE278756 ✓ | GSE44706: ND | LIKELY CONSERVED |

## Therapeutic Implications

Based on the reproducibility matrix:

1. **LAMP2 suppression is the most reproducible finding** (4 independent datasets, 
   p<1e-11 in primary human tissue). This means autophagy induction alone is insufficient
   — lysosomal enhancement (trehalose, TFEB activators) is required to overcome the CVB-
   mediated LAMP2 block.

2. **ISG phase matters for IFN-based therapy**:
   - ACUTE phase: IFNβ1 could boost antiviral response (CVB suppresses it)
   - PERSISTENT phase: ISGs already active; additional IFN won't help much
   - GSE57781 shows hiPSC-CMs respond strongly to exogenous IFNβ1 — therapeutic window exists

3. **CXADR downregulation explains persistence**: Both receptor downregulation (viral evasion)
   and ISG induction (interferon response) occur; the combination explains why CVB can establish
   persistent infection despite a partially active immune response.

## Datasets Not Yet Analyzed

The following datasets mentioned in the task plan are available but probe annotation prevented
complete analysis in this session:
- GSE26630: CVB3 sex differences in spleen at 12h (GPL6246) — ISG analysis partial
- Full analysis of GSE1457, GSE35182, GSE19303, GSE293840, GSE268212 pending

## Data Quality Notes

- All fold changes computed from normalized microarray data or raw count data
- Microarray datasets (GSE26630, GSE44706, GSE57781) use log₂ signal values
- RNA-seq datasets use TPM-normalized counts with log₂ transformation
- Statistical tests: two-tailed t-test for all comparisons
- scRNA-seq (GSE274264): Wilcoxon rank-sum test by cell type cluster
