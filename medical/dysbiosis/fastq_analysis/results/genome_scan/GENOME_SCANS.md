# Targeted Genome Scans (bowtie2 read mapping, 2026-05-22)

Direct mapping of all 18.7M trimmed reads against specific reference genomes.

## Coxsackievirus B1 — PX470093.1 (7,375 bp, RNA enterovirus)
- **0 reads mapped, 0% genome covered, 0.00% alignment.**
- Expected: CVB is a (+)ssRNA virus; this is a **DNA** shotgun library → RNA viruses are physically
  absent (no reverse transcription). **A 0 here is an assay blind spot, NOT evidence CVB is absent
  from the gut.** Testing CVB requires RNA metatranscriptomics / RT-PCR, or serology (anti-CVB
  neutralizing Ab / VP1 — the framework's M3 stack). The FASTQ cannot address the CVB→T1DM question.

## Akkermansia muciniphila MucT — NC_010655.1 (2.6 Mb)
- **826 reads mapped but only 0.34% genome breadth** at 0.04× depth.
- <1% scattered breadth = spurious cross-mapping from other taxa, not real presence (a present
  organism shows contiguous coverage across most of the genome even at low abundance).
- **Verdict: true absence** — not below-detection. Akkermansia 0% now confirmed by 4 methods
  (dashboard, Kraken2, sylph, direct mapping) and shown to be genuinely absent.

*Method: bowtie2 --no-unal vs reference; samtools coverage. Pipeline points at any accession.*
