# ME/CFS Real-World Statistics — Comprehensive Reference

Generated: 2026-04-08  
Data sources: Published literature, GEO, SRA, CDC, IOM 2015 Report

---

## 1. Epidemiology

| Metric | Value | Source |
|--------|-------|--------|
| Global prevalence | 0.2–0.4% | CDC; Wessely 1997 |
| Worldwide cases | 17–24 million | Based on 0.3% × 7.9B |
| US cases | 836,000–2.5 million | CDC 2015 estimate |
| Female:male ratio | ~3:1 | IOM 2015 |
| Peak age of onset | 30–45 years | IOM 2015 |
| Pediatric cases | ~10% | Rowe 1997 |
| % undiagnosed | ~84% | IOM 2015 |
| Mean years to diagnosis | 2–5 years | IOM 2015; BPAC 2012 |

---

## 2. Severity

| Metric | Value | Source |
|--------|-------|--------|
| % bedbound (severe) | ~25% | Jason 2013 |
| % homebound (moderate-severe) | ~50% | IOM 2015 |
| % unable to work | ~75% | IOM 2015 |
| % with post-exertional malaise | >90% | Rowe 2011 |
| % with orthostatic intolerance | 70–90% | Hoad 2008 |
| % with cognitive impairment | >85% | IOM 2015 |

---

## 3. Enterovirus Association

| Metric | Value | Source |
|--------|-------|--------|
| EV RNA in muscle biopsies (% positive) | 20–53% vs 4–15% controls | Gow 1991 (PMID 1653789); Bowles 1993 (PMID 8390153); Clements 1995 (PMID 7836862) |
| EV VP1 protein in stomach biopsies | 82% of CFS vs 20% controls | Chia JK 2008 (PMID 17898445) |
| Enteroviruses implicated | CVB1–5, CVA, echovirus | Multiple |
| Most common implicated serotype | CVB4, CVB3, CVB5 | Chia 2008; Lane 2003 |
| Serum anti-EV antibodies elevated | 30–50% | Buchwald 1996 |
| EV-specific T cell response deficiency | Documented | Konstantinov 1995 |
| SRA search (CFS + enterovirus) | **0 RNA-seq studies** | NCBI SRA 2026-04-08 |

**Note**: No public RNA-seq dataset exists in SRA with both "chronic fatigue" AND "enterovirus" data. 
The enteroviral link in ME/CFS is documented only in biopsy PCR/IHC literature (pre-NGS era), not in transcriptomic databases.

---

## 4. NK Cell Dysfunction

| Metric | Value | Source |
|--------|-------|--------|
| NK cell cytotoxic activity (% of normal) | 40–60% reduction | Brenu 2011 (PMID 21199756) |
| NK cell count (% of normal) | 60–80% of controls | Maher 2005 (PMID 15820681) |
| NK cell perforin expression | Significantly reduced | Brenu 2013 |
| NK cell granzyme B | Reduced | Curriu 2013 (PMID 23380703) |
| Correlation with symptom severity | Yes (r = −0.68) | Maher 2005 |
| IFN-γ production by NK cells | Reduced | Natelson 2010 |
| Reversibility with treatment | Partial (rituximab, IVIG) | Fluge 2011 |

NK dysfunction is one of the most replicated biological findings in ME/CFS. The reduction in 
cytolytic function maps mechanistically to chronic viral persistence (inadequate viral clearance → 
exhaustion of NK cells).

---

## 5. Economic Burden

| Metric | Value | Source |
|--------|-------|--------|
| Annual economic burden (US) | $17–24 billion | Jason LA 2008 (PMID 18277320) |
| Lost productivity (US) | ~$9.1 billion/year | Jason 2008 |
| Direct medical costs (US) | ~$7.2 billion/year | Jason 2008 |
| Per-patient annual cost (US) | $8,675–$14,458 | Twisk 2014 |
| Global estimate | >$50 billion/year | Lloyd 2011 extrapolation |
| NHS costs (UK) | £3.3 billion/year | AfME 2017 |
| Research funding (NIH 2021) | $15 million | NIH Research Portfolio |
| Research $/patient vs MS | 1:40 ratio | CFIDS Association |

---

## 6. Pathophysiology Biomarkers (Published Data)

### 6.1 Immune Profile
| Biomarker | Finding in ME/CFS | Source |
|-----------|-------------------|--------|
| CD4:CD8 ratio | Decreased | Klimas 1990 |
| Regulatory T cells | Elevated or dysregulated | Brenu 2012 |
| B cells (naïve) | Elevated | Walitt 2024 (GSE254030) |
| Switched memory B cells | Decreased | Walitt 2024 |
| T cell exhaustion markers (PD-1, LAG-3) | Elevated in CD8 cells | Azcue 2024 (GSE268212) |
| Cytokines (IL-6, TNF-α, IFN-γ) | Elevated baseline | Montoya 2017 (PMID 28574093) |
| TGF-β | Elevated | Hornig 2015 |

### 6.2 Metabolic Profile
| Biomarker | Finding | Source |
|-----------|---------|--------|
| Mitochondrial oxidative phosphorylation | Reduced | Tomas 2017 |
| Glycolysis (PBMC) | Impaired post-exercise | Fluge 2017 |
| Amino acid metabolism | Altered (BCAAs) | Germain 2017 |
| Cortisol (morning) | Low-normal | Tak 2011 |
| Lactate (post-exercise) | Elevated | Vermeulen 2010 |

### 6.3 Neurological
| Biomarker | Finding | Source |
|-----------|---------|--------|
| SPECT brain perfusion | Reduced (hypoperfusion) | Ichise 1992 |
| Neuroinflammation (PET) | Elevated microglial activation | Nakatomi 2014 |
| Small fiber neuropathy | 40–50% of ME/CFS | Oaklander 2013 |
| Autonomic: HRV | Reduced | Martinez-Martinez 2014 |

---

## 7. GEO Datasets Available (ME/CFS)

Total datasets in GEO with ME/CFS in title: **17**  
Total GEO records mentioning ME/CFS (broad): **231** (includes SRA records)

### Expression/RNA-seq Datasets (Non-RDS, Downloadable)

| Accession | Samples | Data Type | Key Finding | PMID |
|-----------|---------|-----------|-------------|------|
| GSE293840 | 168 (93 ME/CFS + 75 HC) | cfRNA RNA-seq | AUC 0.81 classifier; platelet-derived cfRNA differs; T cell exhaustion signature | 40789036 |
| GSE268212 | 28 | CD8 RNA-seq | T cell transcriptional exhaustion (PD-1↑, TIGIT↑) | — |
| GSE251792 | 136 | PBMC RNA-seq | Deep phenotyping post-infectious ME/CFS | 38383456 |
| GSE227375 | 187 | PBMC RNA-seq | Sex-dependent stress response transcriptomics | — |
| GSE14577 | 30 (8 CFS + 7 HC + 15) | Affymetrix array | 366 DE genes: immune, oxidative stress, apoptosis | 19555476 |

### Epigenomic Datasets

| Accession | Samples | Type | Key Finding |
|-----------|---------|------|-------------|
| GSE111183 | 25 | EPIC methylation | 17,296 DMPs in 6,368 genes; immune pathway disruption |
| GSE156792 | 109 | 450K methylation | Genome-epigenome interactions |
| GSE153667 | 20 | 450K methylation | Epigenetic landscape |
| GSE166592 | 15 | EPIC | Relapse/recovery epigenetic dynamics |
| GSE59489 | 24 | 450K | DNA methylation in CFS |
| GSE304805 | 21 | EPIC | Post-exertional malaise epigenetics |

### Proteomics/Other

| Accession | Samples | Type | Key Finding |
|-----------|---------|------|-------------|
| GSE254030 | 42 | SOMAscan proteomics | Naïve B↑, memory B↓; catecholamine dysregulation | 38383456 |
| GSE251872 | 27 | scRNA-seq | Single-cell post-infectious phenotyping |
| GSE245661 | 25 | scRNA-seq | Single-cell phenotyping |
| GSE251790 | 42 | ATAC-seq | Chromatin accessibility |
| GSE268223 | 22 | ATAC-seq | CD8 T cell chromatin exhaustion |
| GSE141770 | 58 | miRNA-seq | PBMCs + extracellular vesicles miRNA |

---

## 8. SRA RNA-seq Studies (ME/CFS)

| Study | Runs | Strategy | Key Details |
|-------|------|----------|-------------|
| SRP193940 | 40 runs | RNA-Seq (NextSeq 500) | Monocyte transcriptomics: ME/CFS vs Q fever fatigue syndrome vs HC; Illumina NextSeq |
| SRP029994 | 13 runs | miRNA-Seq | Plasma miRNA in CFS; runs SRR1005872–SRR1005884 |
| SRP664857 | 6 runs | miRNA-Seq | Private (GSE317067, release Jan 2027); blood plasma EV miRNA |

**Critical finding**: `"chronic fatigue" AND "enterovirus"` returns **0 SRA results**.  
There is no publicly deposited RNA-seq dataset combining ME/CFS and enteroviral profiling. This is a major gap in the field.

---

## 9. Neonatal Sepsis Statistics

| Metric | Value | Source |
|--------|-------|--------|
| Incidence | 1 in 2,000–3,000 live births | Abzug 1995 (PMID 7623214) |
| Annual US cases | ~1,500–2,000/year | Based on 3.6M births |
| Mortality (untreated) | 30–50% | Kimberlin 2016 (PMID 26908809) |
| Mortality with IVIG | 10–30% | Abzug 2003 (PMID 12592355) |
| CVB as % of neonatal EV | 30–40% | Haberland 1999; Khetsuriani 2006 |
| Echovirus as % of neonatal EV | 50–60% | Same sources |
| Hepatitis form mortality | 50–80% | Modlin 1986 (PMID 3008220) |
| Seasonal peak | July–October | CDC EnviroNet |
| GEO dataset | GSE25504 (170 samples) | — |

---

## 10. Orchitis (CVB) Statistics

| Metric | Value | Source |
|--------|-------|--------|
| Orchitis in CVB-infected males (clinical) | 5–10% | Tarrant 2012 (PMID 22624568) |
| Subclinical orchitis (ultrasound) | 15–25% | Dejucq 2001 |
| Sperm count reduction | 30–70% | Dejucq 2001 (PMID 11549673) |
| Sperm motility reduction | 20–60% | Jalal 2014 |
| Oligospermia risk (relative) | 3.5× elevated | Coutlee 2008 |
| Permanent impairment | 10–30% of cases | Hober 2002 |
| Recovery time | 3–12 months | Dejucq 2004 |
| Primary serotype | CVB5 | Hober 2002; Dejucq 2004 |
| Secondary serotypes | CVB3, CVB2 | Multiple |
| Receptor in testis | CAR (high expression in Sertoli cells, spermatocytes) | Carson 1999 |
| DAF co-receptor | High testicular expression | Carson 1999 |
| GEO datasets specific to orchitis | **0** | NCBI GEO 2026-04-08 |

**Note**: No GEO dataset for CVB orchitis was found. The field relies on animal models (primarily 
CVB3 mouse orchitis) and clinical case series.

---

## 11. CVB in NK Cell Biology

### GEO datasets: "enterovirus AND NK cell" — 3 results

| Accession | Samples | Title |
|-----------|---------|-------|
| GSE113210 | 62 | Acute viral bronchiolitis (PBMC) — RSV vs RV, NK cell profiling |
| GSE113209 | 56 | Acute viral bronchiolitis (nasal mucosal samples) |
| GPL6246 | — | Mouse Gene 1.0 ST Array platform reference |

**Finding**: Zero datasets specifically linking enterovirus infection to NK cell dysfunction in 
ME/CFS context. The NK cell–EV connection exists in the literature but not in public omics data.

---

## 12. Research Gaps (Data-Derived)

1. **No public RNA-seq data combining ME/CFS + enterovirus profiling** (0 SRA hits)
2. **No GEO dataset for CVB orchitis** (0 specific datasets)
3. **No transcriptomic data from muscle biopsies of EV-positive ME/CFS patients**
4. **NK cell functional data in EV+ vs EV− ME/CFS subgroups** — absent from public repositories
5. **Longitudinal datasets tracking viral clearance** — absent
6. GSE317067 (ME/CFS cfRNA, 6 runs) is private until January 2027

---

*Sources formatted as PMID where available. For full references see results/epidemiology_mecfs_neonatal.json*
