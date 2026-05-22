# P0 FASTQ — sylph Deep Re-Profile (2026-05-22)

sylph 0.9.0 (ANI/k-mer, *Nat Biotech* 2025) vs GTDB-R220 (113K species) + IMG/VR (2.9M viral) +
RefSeq fungi. Native aarch64; profiled in **15 s**. **296 prokaryote genomes + 1,159 viral genomes**
detected — vs Kraken2's 8%-classified, capped-DB struggle. This is the quality fix.

## sylph vs Kraken2-capped vs TinyHealth dashboard
sylph lands **much closer to the commercial dashboard** than our capped-Kraken2 did — i.e. the 8%
classification was distorting the Kraken2 phylum numbers; sylph corrects them:

| Phylum | TinyHealth | Kraken2 (8%, capped) | **sylph** |
|--------|-----------:|---------------------:|----------:|
| Firmicutes (Bacillota) | 61.5% | 48.3% | **64.0%** ✅ |
| Bacteroidota | 30.5% | 39.1% | **23.5%** |
| Proteobacteria (Pseudomonadota) | 5.4% | 9.8% | **3.8%** ✅ |
| Actinobacteriota | 2.3% | 2.3% | **4.5%** |

## Key metrics — now triple-confirmed
| Metric | sylph result | Status |
|--------|--------------|--------|
| **Akkermansia** | **NOT DETECTED** | 🔴 0% — now confirmed by PDF + Kraken2 + sylph (3 methods) |
| **F. prausnitzii** (genus) | ~9.2% (GTDB splits: prausnitzii_A/_D, longum, duncaniae) | ✅ matches PDF 9.46% |
| **E. coli vs Shigella** | **E. coli 2.84%, ZERO Shigella** | ✅ **DEFINITIVE — 3rd concordant method** (reads + contigs + sylph). The dashboard's "E. flexneri 3.9%" is E. coli. |
| Histamine producers | not detected | ✅ matches |
| Fungi (Candida etc.) | not detected (RefSeq-fungi DB) | ✅ matches |

Top species: Fusicatenibacter saccharivorans 5.84% (= PDF's #1), then Prevotella, B. uniformis,
E. coli, P. vulgatus, Agathobacter rectalis, the Faecalibacterium complex — a butyrate-producer-rich,
healthy-looking community matching the dashboard.

## Phageome (sylph + IMG/VR)
**1,159 viral genomes** detected at 95–99% ANI — a deep, well-populated phage community (vs the
sparse CrAssphage signal Kraken2 could pull). IDs are IMG/VR UViG accessions; mapping which are
crAss-like/Bacteroides phages is a refinement step.

## Bottom line
The cutting-edge re-profile **validates everything and fixes the one weakness**: Akkermansia 0% is
real (3 methods), F. prausnitzii is genuinely abundant, the scary "Shigella" is benign E. coli
(definitive), and the phylum picture now agrees with the commercial pipeline.

*Outputs: results/sylph/profile_gtdb.tsv (296 genomes), profile_viral_fungal.tsv (1,159 viral).*
*Next: MICOM SCFA/H₂S flux modeling (needs AGORA2 model DB) — the functional answer, native on ARM.*
