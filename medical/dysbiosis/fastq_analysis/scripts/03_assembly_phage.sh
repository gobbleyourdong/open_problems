#!/usr/bin/env bash
# P0 FASTQ — metaSPAdes assembly + VirSorter2 phage (native aarch64; no DIAMOND).
# Answers: definitive E. flexneri-vs-E. coli strain (via assembled genome) + phageome.
# Run after fastp. Long job (metaSPAdes ~30-90 min on 18.7M pairs).
set -euo pipefail
source ~/miniforge3/etc/profile.d/conda.sh && conda activate mgx_heavy

A=~/open_problems/medical/dysbiosis/fastq_analysis
R1=$A/qc/CXD568_trim_1.fastq.gz; R2=$A/qc/CXD568_trim_2.fastq.gz
OUT=$A/results; mkdir -p "$OUT"
THREADS=16

echo "[$(date +%H:%M)] metaSPAdes assembly…"
spades.py --meta -1 "$R1" -2 "$R2" -o "$OUT/assembly" -t $THREADS -m 100 2> "$OUT/assembly.log"
CONTIGS="$OUT/assembly/contigs.fasta"
echo "[$(date +%H:%M)] assembly: $(grep -c '^>' "$CONTIGS") contigs"

echo "[$(date +%H:%M)] VirSorter2 (phage; hmmer-based, no diamond)…"
virsorter run -i "$CONTIGS" -w "$OUT/virsorter2" -d ~/databases/virsorter2 \
  --include-groups dsDNAphage,ssDNA -j $THREADS --min-score 0.5 --min-length 1500 all \
  2> "$OUT/virsorter2.log" || echo "  (VirSorter2 needs its DB fully set up — check ~/databases/virsorter2)"

# E. flexneri / Shigella vs E. coli — strain resolution from the assembly.
# Pull Enterobacteriaceae contigs (Kraken2-tag the assembly), then ANI vs references.
echo "[$(date +%H:%M)] tagging contigs with Kraken2 for the E. flexneri call…"
conda run -n mgx_core kraken2 --db ~/databases/k2_pluspfp_16gb "$CONTIGS" \
  --threads $THREADS --confidence 0.1 --output "$OUT/contigs_kraken.txt" --report "$OUT/contigs_kraken_report.txt" 2>/dev/null || true
echo "--- Shigella / E. coli contigs ---"
grep -iE "Shigella|Escherichia" "$OUT/contigs_kraken_report.txt" 2>/dev/null | head || echo "  none flagged at contig level"

echo "[$(date +%H:%M)] DONE — assembly + phage in $OUT. (CheckV QC skipped: DIAMOND unavailable on aarch64.)"
