#!/usr/bin/env bash
# P0 FASTQ — taxonomy classification + key-metric extraction
# Run after fastp (qc/CXD568_trim_*.fastq.gz) and DB download (k2_pluspfp_16gb).
set -euo pipefail
source ~/miniforge3/etc/profile.d/conda.sh && conda activate mgx_core

A=~/open_problems/medical/dysbiosis/fastq_analysis
DB=~/databases/k2_pluspfp_16gb
R1=$A/qc/CXD568_trim_1.fastq.gz
R2=$A/qc/CXD568_trim_2.fastq.gz
OUT=$A/results
mkdir -p "$OUT"
THREADS=16

echo "[$(date +%H:%M:%S)] kraken2 classify (conf 0.1)…"
# We only need the --report for Bracken + metrics; skip per-read output (/dev/null).
kraken2 --db "$DB" --paired "$R1" "$R2" \
  --threads $THREADS --confidence 0.1 \
  --report "$OUT/kraken_report.txt" --output /dev/null 2> "$OUT/kraken.log"

echo "[$(date +%H:%M:%S)] bracken (species, r=150)…"
RL=150; [ -f "$DB/database${RL}mers.kmer_distrib" ] || RL=$(ls "$DB"/database*mers.kmer_distrib 2>/dev/null | sed -E 's/.*database([0-9]+)mers.*/\1/' | sort -n | tail -1)
bracken -d "$DB" -i "$OUT/kraken_report.txt" -o "$OUT/bracken_species.txt" -r "$RL" -l S -t 10 2> "$OUT/bracken.log"
bracken -d "$DB" -i "$OUT/kraken_report.txt" -o "$OUT/bracken_phylum.txt" -r "$RL" -l P -t 10 2>> "$OUT/bracken.log" || true

echo "[$(date +%H:%M:%S)] extracting key metrics → $OUT/P0_metrics.txt"
{
echo "=== P0 FASTQ key metrics (kit CXD568) — $(date) ==="
echo "# bracken fraction_total_reads is the last column; ×100 = %"
echo
echo "--- 1. F. prausnitzii (Node A / Treg proxy) ---"; grep -i "Faecalibacterium prausnitzii" "$OUT/bracken_species.txt" || echo "  not detected"
echo "--- 2. Akkermansia muciniphila ---";              grep -i "Akkermansia muciniphila"    "$OUT/bracken_species.txt" || echo "  not detected (matches PDF 0%)"
echo "--- 3. Proteobacteria (phylum) ---";              grep -iE "Proteobacteria|Pseudomonadota" "$OUT/bracken_phylum.txt" || grep -iP "\tP\t.*(Proteobacteria|Pseudomonadota)" "$OUT/kraken_report.txt" || echo "  see kraken_report"
echo "--- 4. Histamine producers ---";                  grep -iE "Morganella morganii|Klebsiella pneumoniae|Klebsiella oxytoca" "$OUT/bracken_species.txt" || echo "  none detected"
echo "--- 5. CrAssphage / Bacteroides phage (the bonus metric the PDF lacked) ---"; grep -iE "crass|uncultured crAssphage|Caudovir" "$OUT/kraken_report.txt" || echo "  not detected in kraken report"
echo "--- 6. Candida / fungi ---";                      grep -iE "Candida|Malassezia|Saccharomyces|Aspergillus" "$OUT/bracken_species.txt" || echo "  none detected"
echo
echo "--- E. flexneri / Shigella vs E. coli (the 3.9% question) ---"
grep -iE "Shigella flexneri|Shigella dysenteriae|Shigella sonnei|Escherichia coli|Escherichia flexneri|Escherichia dysenteriae" "$OUT/bracken_species.txt" || echo "  none detected"
echo "  (note: Kraken/GTDB resolve Escherichia vs Shigella differently than TinyHealth; assembly step = definitive)"
echo
echo "--- top 25 species by abundance ---"; sort -t$'\t' -k7 -gr "$OUT/bracken_species.txt" 2>/dev/null | head -25 | awk -F'\t' '{printf "  %-45s %s%%\n",$1,$7*100}'
} > "$OUT/P0_metrics.txt"
cat "$OUT/P0_metrics.txt"
echo "[$(date +%H:%M:%S)] DONE — $OUT/P0_metrics.txt"
