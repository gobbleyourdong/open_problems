#!/usr/bin/env bash
# P0 FASTQ — HUMAnN3 functional profiling. RUN ON AN x86_64 HOST (e.g. Vast.ai).
# DIAMOND has no working aarch64 build, so the functional layer is offloaded off the Spark.
#
# Prereqs on the x86 box:
#   - copy the trimmed reads over:  qc/CXD568_trim_1.fastq.gz, qc/CXD568_trim_2.fastq.gz
#   - ~120 GB free disk (ChocoPhlAn ~16GB + UniRef90 diamond ~34GB + MetaPhlAn ~22GB)
#   - run:  bash 04_humann_x86.sh /path/to/reads_dir /path/to/work_dir
set -euo pipefail
READS=${1:?usage: 04_humann_x86.sh <reads_dir> <work_dir>}
WORK=${2:?usage: 04_humann_x86.sh <reads_dir> <work_dir>}
DB="$WORK/databases"; OUT="$WORK/humann_out"; mkdir -p "$DB" "$OUT"
THREADS=$(nproc)

# guard: this must run on x86_64 (DIAMOND requirement)
[ "$(uname -m)" = "x86_64" ] || { echo "ERROR: run this on x86_64 (got $(uname -m)). DIAMOND needs it."; exit 2; }

# 1. miniforge + clean humann env (x86 bioconda builds are mutually consistent)
if [ ! -d "$HOME/miniforge3" ]; then
  curl -fsSL -o /tmp/mf.sh https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
  bash /tmp/mf.sh -b -p "$HOME/miniforge3"
fi
source "$HOME/miniforge3/etc/profile.d/conda.sh"
mamba env list | grep -q '^humann ' || mamba create -n humann -y -c conda-forge -c bioconda humann metaphlan diamond
conda activate humann
diamond version   # sanity: must run (x86)

# 2. databases
metaphlan --install --db_dir "$DB/metaphlan4"
humann_databases --download chocophlan full "$DB/humann3"
humann_databases --download uniref uniref90_diamond "$DB/humann3"
humann_config --update database_folders nucleotide "$DB/humann3/chocophlan"
humann_config --update database_folders protein "$DB/humann3/uniref"

# 3. HUMAnN takes a single fastq → concatenate the pair
CAT="$WORK/CXD568_merged.fastq.gz"
[ -f "$CAT" ] || cat "$READS/CXD568_trim_1.fastq.gz" "$READS/CXD568_trim_2.fastq.gz" > "$CAT"

# 4. run
humann --input "$CAT" --output "$OUT" --threads "$THREADS" \
  --metaphlan-options "--bowtie2db $DB/metaphlan4"

# 5. the questions for P0 — does the H₂S 92 impair butyrate USE despite ok production?
PA=$(ls "$OUT"/*_pathabundance.tsv); GF=$(ls "$OUT"/*_genefamilies.tsv)
{
echo "=== P0 HUMAnN functional — butyrate axis ==="
echo "--- PWY-5676 (acetyl-CoA → butanoate; the butyrate pathway) ---"; grep -i "PWY-5676" "$PA" || echo "  not found"
echo "--- BUTANAL/BUTANOL + hydrogen pathways ---"; grep -iE "BUTANAL|butanol|P162-PWY" "$PA" || echo "  none"
echo "--- butyrate genes: buk (kinase) + but (butyryl-CoA:acetate CoA-transferase) ---"
grep -iE "butyrate kinase|butyryl-CoA" "$GF" | head || echo "  none flagged by name"
} > "$OUT/P0_butyrate_functional.txt"
cat "$OUT/P0_butyrate_functional.txt"
echo "DONE → $OUT/P0_butyrate_functional.txt"
