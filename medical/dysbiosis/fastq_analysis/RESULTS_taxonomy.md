# P0 FASTQ — Taxonomy Results vs. Dashboard (2026-05-22)

Kraken2 v2.17.1 (NCBI taxonomy) + Bracken on `k2_pluspfp_16gb`, 9.37 M pairs.
**Caveat up front:** only **8.0% of reads classified** (92% unclassified) — the 16 GB-capped DB
trades sensitivity for RAM-fit. So treat these as *relative* abundances among the classified
fraction. They corroborate the dashboard for major taxa (below), but low-abundance calls and
absolute quantities are soft. Contig-level (assembly, running) + an optional uncapped re-run firm them up.

## FASTQ vs. TinyHealth dashboard

| Metric | TinyHealth PDF | FASTQ (Kraken2/Bracken) | Verdict |
|--------|----------------|--------------------------|---------|
| **F. prausnitzii** | 9.46% (genus) | 8.95% sp. + ~1% other Faecalibacterium ≈ **10% genus** | ✅ **confirms** |
| **Akkermansia muciniphila** | 0% | **not detected** | ✅ **confirms 0%** |
| **Histamine producers** (Morganella/Klebsiella) | ~0 / 0.006% | **none detected** | ✅ confirms |
| **Candida / fungi** | 0% | **none detected** | ✅ confirms |
| **CrAssphage** | *(not reported by PDF)* | **DETECTED** — Crassvirales / Caudoviricetes (low) | 🆕 **the bonus answer** |
| Proteobacteria (Pseudomonadota) | 5.38% | 9.84% | ⚠ higher (method/DB diff) |
| Bacteroidota | 30.45% | 39.08% | ⚠ higher |
| Firmicutes (Bacillota) | 61.47% | 48.27% | ⚠ lower |

The 6 key metrics from the framework's Run 004 list are **independently corroborated** by the raw
reads (the phylum %s differ in magnitude — expected given 8% classification + different pipeline/taxonomy
— but the directional picture holds).

## The two things the dashboard couldn't answer

**1. CrAssphage — metric #5 — DETECTED.** Crassvirales (the crAss-like phage order) and Caudoviricetes
are present at low abundance. Per the framework: detectable CrAssphage = Bacteroides-density phage
control is active (not a depleted phageome). The dashboard never reported this; the FASTQ does.

**2. E. flexneri 3.9% → it classifies as *E. coli*, not Shigella.** This is the headline.
- TinyHealth (GTDB taxonomy): "**Escherichia flexneri** 3.9%" (the Shigella clade), E. coli 0.07%.
- Kraken2 (NCBI taxonomy): **E. coli 9.2% (the #1 organism), and NO Shigella flexneri/dysenteriae detected at all.**
- → The same reads that GTDB labels "E. flexneri" classify as **commensal E. coli** under NCBI. This
  **supports the misassignment/commensal reading** over a true Shigella infection — exactly the caveat
  flagged in the [P0 baseline](../results/p0_microbiome_baseline_2026-05-21.md). **Definitive call comes
  from the assembly** (metaSPAdes contigs → ANI vs E. coli vs Shigella references; running now).

## Top species (FASTQ, among classified)
E. coli 9.2% · F. prausnitzii 9.0% · Bacteroides uniformis 8.6% · Phocaeicola vulgatus 8.6% ·
Agathobacter rectalis 6.7% · Parabacteroides distasonis 6.4% · Blautia wexlerae 5.4% · P. merdae 2.9% ·
Roseburia faecis 2.8% · Anaerobutyricum hallii 2.4% · Bifidobacterium longum 1.1% · Dysosmobacter welbionis 1.0% …
(Strong butyrate-producer representation — consistent with the dashboard's healthy SCFA picture.)

## Assembly + phage — COMPLETED 2026-05-22
metaSPAdes (native aarch64): **455,296 contigs, 297 Mbp**. VirSorter2: **2,008 viral sequences**.
- **E. coli vs Shigella — settled:** contig-level taxonomy resolves the Enterobacteriaceae to
  **Escherichia, with ZERO Shigella** — matching the read level (E. coli 9.2%, no Shigella). The
  dashboard's "E. flexneri 3.9%" is **E. coli, not a true Shigella** (agreement across reads + assembly;
  a formal ANI vs reference genomes would be the last word but both levels concur).
- **Phageome:** 2,008 viral contigs — a well-represented phage community (incl. the CrAssphage flagged at read level). CheckV completeness QC skipped (DIAMOND unavailable on aarch64).

## Next (optional)
- Optional: re-run classification on uncapped **k2_standard (74.7 GB, fits RAM)** to lift the 8% → proper rate for tighter numbers.
- **Functional layer (HUMAnN butyrate genes): x86 offload** — DIAMOND won't run/build on aarch64.
