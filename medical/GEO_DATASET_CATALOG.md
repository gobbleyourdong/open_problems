# GEO Dataset Catalog — CVB Disease Network

**Generated:** 2026-04-08
**Source searches:** `~/open_problems/medical/numerics/geo_t1dm_cvb_search.json`, `~/open_problems/medical/results/geo_cardiac_cvb_search.json`, `epidemiology_all_diseases.json`
**Download log:** `~/open_problems/medical/numerics/geo_download_log.json`

Legend: [DOWNLOADED] = data on disk | [IDENTIFIED] = found in search, not yet downloaded | [PLATFORM] = array platform record, not a study

---

## T1DM / Beta Cell / Pancreatic Islet Datasets

### Human — High Priority

| Accession | Title | N Samples | Organism | Type | Status |
|-----------|-------|-----------|----------|------|--------|
| **GSE274264** | Coxsackievirus B infection invokes unique cell-type-specific responses in primary human pancreatic islets | 10 | H. sapiens | RNA-seq | [DOWNLOADED] |
| **GSE278756** | Viral triggers of T1D: Effects of Coxsackie B virus on transcriptome of trophoblast and pancreatic beta cell lines | 15 | H. sapiens | RNA-seq + small-RNA-seq | [DOWNLOADED] |
| **GSE247808** | Vascularized Macrophage-Islet Organoids: beta cell Pyroptosis upon CVB4 infection [snATACseq] | 3 | H. sapiens | snATAC-seq | [DOWNLOADED] |
| **GSE247807** | Vascularized Macrophage-Islet Organoids: beta cell Pyroptosis upon CVB4 infection [scRNAseq VMI] | 3 | H. sapiens | scRNA-seq | [DOWNLOADED] |
| **GSE247806** | Vascularized Macrophage-Islet Organoids: beta cell Pyroptosis upon CVB4 infection [scRNAseq islets] | 10 | H. sapiens | scRNA-seq | [DOWNLOADED] |
| **GSE247805** | Vascularized Macrophage-Islet Organoids: beta cell Pyroptosis upon CVB4 infection [bulk RNAseq] | 6 | H. sapiens | Bulk RNA-seq | [DOWNLOADED] |
| **GSE214851** | ADAR1-dependent editing in human beta-cells transcriptome diversity during inflammation | 6 | H. sapiens | RNA-seq | [DOWNLOADED] |
| **GSE184831** | Persistent Coxsackievirus B1 infection — extensive transcriptome changes in pancreatic cell line | 9 | H. sapiens | RNA-seq | [DOWNLOADED] |

**Notes on GSE278756:** Samples include EndoC-betaH1 (beta cell line) and Sw.71 (trophoblast) infected with CVB4-JVB and CVB4-E2 strains. Individual sample records GSM8554349-GSM8554362 in download log (not yet downloaded — are constituent samples of the series).

**Notes on GSE247805-247808:** Four linked datasets from one study — CVB4 + SARS-CoV-2 comparison in macrophage-islet organoids. snATAC provides chromatin accessibility data complementing scRNA.

---

## Cardiac CVB Datasets (Myocarditis / DCM)

### Human

| Accession | Title | N Samples | Organism | Type | Status |
|-----------|-------|-----------|----------|------|--------|
| **GSE57781** | Human iPSC-Derived Cardiomyocytes as In Vitro Model for CVB3-Induced Myocarditis and Antiviral Drug Screening | 4 | H. sapiens | Microarray | [IDENTIFIED] |

### Mouse (CVB3 model)

| Accession | Title | N Samples | Organism | Type | Status |
|-----------|-------|-----------|----------|------|--------|
| GSE261940 | Soluble ST2 induces cardiac contractile dysfunction during fulminant myocarditis | 20 | M. musculus | RNA-seq | [IDENTIFIED] |
| GSE248521 | GPR15-mediated T cell recruitment during acute viral myocarditis | 31 | M. musculus | RNA-seq + other | [IDENTIFIED] |
| GSE174458 | Cellular landscape and transcriptome of viral myocarditis (single-cell RNA-seq) | 4 | M. musculus | scRNA-seq | [IDENTIFIED] |
| GSE35182 | Sex differences: acute (10 dpi) and chronic/DCM (90 dpi) CVB3 myocarditis | 24 | M. musculus | Microarray | [IDENTIFIED] |
| GDS4436 | Sex effect on chronic CVB3-induced myocarditis: heart | 12 | M. musculus | Microarray | [IDENTIFIED] |
| GDS4311 | Sex effect on acute CVB3-induced myocarditis: heart | 12 | M. musculus | Microarray | [IDENTIFIED] |
| GSE19496 | CVB3 infection of AJ, B10.A, CSS3, B6.chr3AJ mouse strains (heart, day 4) | 24 | M. musculus | Microarray | [IDENTIFIED] |
| GSE26630 | Sex differences in innate immune response to CVB3 (12hr post infection) | 20 | M. musculus | Microarray | [IDENTIFIED] |
| GSE1457 | CVB3 infection and cardiac function | 7 | M. musculus | Microarray | [IDENTIFIED] |
| GDS1032 | CVB3 infection effect on hearts: time course | 6 | M. musculus | Microarray | [IDENTIFIED] |

**Priority download recommendation:** GSE174458 (scRNA-seq, cellular landscape), GSE35182 (acute vs chronic DCM comparison), GSE57781 (human iPSC — only human cardiac CVB dataset).

---

## Neurological CVB Datasets (Aseptic Meningitis / Encephalitis)

### Human — High Priority

| Accession | Title | N Samples | Organism | Type | Status | Relevance |
|-----------|-------|-----------|----------|------|--------|-----------|
| **GSE133378** | Diagnosing enterovirus meningitis via blood transcriptomics: alternative for lumbar puncture? | **476** | H. sapiens | RNA-seq | [IDENTIFIED] | VERY HIGH — largest human dataset |
| **GSE269413** | CVB3 infection in iPSC-derived brain-like endothelial cells (BBB penetration) | 12 | H. sapiens | RNA-seq | [IDENTIFIED] | HIGH — CVB3 BBB mechanism |
| GSE146890 | Polar infection of Echovirus 30 at blood-CSF barrier | 15 | H. sapiens | RNA-seq | [IDENTIFIED] | HIGH — blood-CSF barrier |
| GSE15323 | Differentially expressed genes induced by EV71 infection | 9 | H. sapiens | Microarray | [IDENTIFIED] | MODERATE — EV71, related enterovirus |

### Mouse (CVB/enterovirus CNS model)

| Accession | Title | N Samples | Organism | Type | Status |
|-----------|-------|-----------|----------|------|--------|
| GSE280993 | Enhanced RNAi vs innate antiviral immunity in vivo (smallRNA-Seq spleen) | 8 | M. musculus | small RNA-seq | [IDENTIFIED] |
| GSE273336 | Enhanced RNAi vs innate antiviral immunity in vivo (organs small RNA-Seq) | 28 | M. musculus | small RNA-seq | [IDENTIFIED] |
| GSE273334 | Enhanced RNAi vs innate antiviral immunity (ESCs TrapR small RNA-Seq) | 16 | M. musculus | small RNA-seq | [IDENTIFIED] |
| GSE273331 | Enhanced RNAi vs innate antiviral immunity (ESCs small RNA-Seq) | 34 | M. musculus | small RNA-seq | [IDENTIFIED] |

### Gerbil (EV71/CA16 brainstem model)

| Accession | Title | N Samples | Organism | Type | Status |
|-----------|-------|-----------|----------|------|--------|
| GSE123550 | Transcriptome of brainstem in gerbils with EV71-infection-induced HFMD | 6 | M. unguiculatus | RNA-seq | [DOWNLOADED] |
| GSE121971 | Transcriptome of brainstem in gerbils with CA16-infection-induced HFMD | 6 | M. unguiculatus | RNA-seq | [DOWNLOADED] |

**Priority download recommendation:** GSE133378 (n=476, human meningitis diagnosis — this is the most clinically actionable dataset in the entire catalog), GSE269413 (CVB3 BBB mechanism, human iPSC).

---

## ME/CFS Datasets

No CVB-specific GEO datasets found in searches. The ME/CFS GEO literature is dominated by immune profiling (NK cell studies) without enteroviral isolation.

**Gap:** A stool CVB PCR + muscle biopsy transcriptomics study in ME/CFS patients has not been published. This is the critical missing dataset.

---

## Pleurodynia / Pericarditis / Pancreatitis / Hepatitis / Orchitis / Neonatal Sepsis

No GEO datasets found for any of these CVB diseases in targeted searches.

**Why:** These diseases are studied clinically (case series, cohorts) rather than transcriptomically. CVB is rarely typed in routine workups for these conditions.

**Implication:** The transcriptomic literature for CVB is heavily biased toward T1DM/pancreatic biology and cardiac CVB3 models. 7 of the 12 CVB diseases have zero transcriptomic data in GEO.

---

## Summary by Disease

| Disease | GEO Datasets Found | Human Datasets | Downloaded | Key Gap |
|---------|-------------------|----------------|------------|---------|
| T1DM | 8+ | 8 (all human) | 8 | Individual samples not yet pulled from GSE278756 |
| Myocarditis | 20 | 1 (GSE57781) | 0 | 19 mouse studies, only 1 human (iPSC) |
| DCM | Overlap with myocarditis | 0 | 0 | GSE35182 has 90-dpi DCM data (mouse) |
| ME/CFS | 0 | 0 | 0 | Entire field missing |
| Aseptic Meningitis | 4 | 3 | 0 | GSE133378 (n=476) not yet downloaded |
| Encephalitis | 4 (2 platform only) | 1 | 0 | GSE269413 (CVB3 BBB) not yet downloaded |
| Hepatitis | 0 | 0 | 0 | No data exists |
| Pancreatitis | 0 | 0 | 0 | No data exists |
| Pericarditis | 0 | 0 | 0 | No data exists |
| Pleurodynia | 0 | 0 | 0 | No data exists |
| Orchitis | 0 | 0 | 0 | No data exists |
| Neonatal Sepsis | 0 | 0 | 0 | No data exists |

---

## Priority Download Queue

Ordered by scientific value:

1. **GSE133378** (Meningitis, n=476 human) — Largest human enteroviral dataset; blood transcriptomics as LP alternative; immediately translatable
2. **GSE57781** (Myocarditis, human iPSC) — Only human-derived cardiac CVB3 transcriptomics
3. **GSE269413** (Encephalitis, CVB3 BBB mechanism, human iPSC) — BBB penetration is a critical pharmacokinetic question
4. **GSE174458** (Myocarditis, scRNA-seq mouse) — Cellular landscape at single-cell resolution
5. **GSE35182** (Myocarditis → DCM, mouse, acute vs chronic) — Temporal comparison of acute myocarditis vs DCM end-stage

---

## Search Queries That Found Nothing

These negative results are informative — they confirm absence of data:

| Query | Database | Result |
|-------|----------|--------|
| "enterovirus" AND "pancreatitis" | GEO DataSets | 0 results |
| "enterovirus" AND "pericarditis" | GEO DataSets | 0 results |
| "coxsackievirus" AND "hepatitis" | GEO DataSets | 0 results |
| "coxsackievirus" AND "pancreatitis" | GEO DataSets | 0 results |
| "CVB" AND "T1DM" | GEO DataSets | 0 results |

Source: `epidemiology_all_diseases.json` (geo_searches section), `geo_t1dm_cvb_search.json`

---

## How to Download a Dataset

```bash
# Activate environment
source ~/ComfyUI/comfyui-env/bin/activate

# Python via GEOparse
pip install GEOparse
python3 -c "import GEOparse; gse = GEOparse.get_GEO('GSE133378', destdir='~/open_problems/medical/numerics/geo_data/')"

# Or via NCBI datasets tool
# GSE accessions map to SRA run accessions in ~/open_problems/medical/results/sra_cardiac_cvb_runs.json
```

Downloaded data location: `~/open_problems/medical/numerics/` (transcriptomics/ subdirectory for processed data)
