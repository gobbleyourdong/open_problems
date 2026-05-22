# P0 FASTQ Full-Analysis — Build Status

Kit CXD568 · paired-end shotgun · **9,370,422 read pairs / 2.71 Gbp** · 151 bp · NovaSeq X · Q30 95.1%.
All tooling runs **native aarch64** on the Spark (no emulation/offload needed).
Host DNA negligible (PDF: 0.023%) → no host-removal step.

## Pipeline build
- [x] Stage FASTQ (symlink) + read/base counts
- [x] Verify aarch64 tool availability — core **and** heavy all native
- [x] `mgx_core` env (kraken2 2.17.1, bracken, fastp, bowtie2, samtools, fastqc)
- [x] fastp QC/trim → `qc/CXD568_trim_{1,2}.fastq.gz` (18,740,832 reads kept; only 12 dropped)
- [~] Kraken2 DB `k2_pluspfp_16gb` download (~10.5 GB, in progress)
- [~] `mgx_heavy` env (humann, metaphlan, spades, virsorter2, checkv) — building
- [ ] MetaPhlAn4 DB (`metaphlan --install`)
- [ ] HUMAnN3 DBs (ChocoPhlAn + UniRef90 — the big one)
- [ ] VirSorter2 + CheckV DB setup
- [ ] **RUN: `scripts/02_classify_extract.sh`** → 6 metrics + CrAssphage + E. flexneri/Shigella
- [ ] RUN: HUMAnN3 functional (butyrate PWY-5676; confirms H₂S-vs-butyrate)
- [ ] RUN: metaSPAdes + VirSorter2 (definitive E. flexneri-vs-E. coli strain + phageome + AMR genes)

## Layout
- `raw/` — symlinked FASTQ · `qc/` — fastp trimmed + reports · `results/` — outputs · `scripts/` — pipeline
- DB choice: 16 GB-capped pluspfp (fits 106 GB RAM → fast) over the 164 GB full index (exceeds RAM).

## The questions this answers (that the PDF couldn't)
1. **CrAssphage** — the 6th metric, absent from the dashboard
2. **E. flexneri 3.9% — real Shigella or misassigned E. coli?** (assembly step settles it)
3. Butyrate-pathway genes (is the H₂S 92 impairing butyrate *use*?)
4. AMR gene classes → which past antibiotics → confirms the Akkermansia-0% cause
5. Independent confirmation of the 6 dashboard metrics from raw reads
