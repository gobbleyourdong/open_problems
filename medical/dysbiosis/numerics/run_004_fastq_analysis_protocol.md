# TinyHealth FASTQ Analysis Protocol
## Run 004 | Numerical Instance | 2026-04-11

> Actionable steps to extract the 6 key metrics from TinyHealth shotgun metagenomics FASTQ.
> Assumes DGX Spark (128GB RAM, GPU available) — well-resourced for bioinformatics.

---

## What to Expect in the FASTQ

TinyHealth shotgun metagenomics = ~20-50 million paired-end reads (150bp each) from stool DNA.
Typical breakdown:
- ~60-70% human reads (filter out)
- ~20-30% bacterial reads (the useful fraction)
- ~0.5-2% fungal reads
- ~0.1-1% viral/phage reads (CrAssphage dominant)

---

## Required Software (all free, all on Linux)

```bash
# Install with conda (recommended)
conda create -n metagenomics python=3.10
conda activate metagenomics

conda install -c bioconda fastqc trimmomatic fastp
conda install -c bioconda bowtie2 samtools
conda install -c bioconda kraken2 bracken
conda install -c bioconda metaphlan  # version 4
conda install -c bioconda humann     # version 3
conda install -c bioconda virsorter2  # optional, phage
```

**Database downloads (one-time, ~100-200GB):**
```bash
# Kraken2 standard database (bacteria + archaea + viruses + human)
kraken2-build --standard --db ~/databases/k2_standard --threads 16

# Bracken database
bracken-build -d ~/databases/k2_standard -t 16 -l 150

# MetaPhlAn4 database
metaphlan --install --bowtie2db ~/databases/metaphlan4

# HUMAnN3 databases
humann_databases --download chocophlan full ~/databases/humann3
humann_databases --download uniref uniref90_diamond ~/databases/humann3
```

---

## Analysis Pipeline

### Step 1: Quality Control
```bash
fastqc sample_R1.fastq.gz sample_R2.fastq.gz -o ./qc/ -t 8
# Check: per-base quality (should be >Q30), adapter contamination, duplication
```

### Step 2: Adapter Trimming
```bash
fastp \
  -i sample_R1.fastq.gz -I sample_R2.fastq.gz \
  -o trimmed_R1.fastq.gz -O trimmed_R2.fastq.gz \
  --detect_adapter_for_pe \
  --qualified_quality_phred 20 \
  --length_required 50 \
  --json fastp_report.json \
  --thread 8
```

### Step 3: Remove Human Reads
```bash
# Download human genome index (one-time): ~15GB
# https://benlangmead.github.io/aws-indexes/bowtie

bowtie2 \
  -x ~/databases/human_GRCh38/GRCh38_index \
  -1 trimmed_R1.fastq.gz -2 trimmed_R2.fastq.gz \
  --un-conc-gz nonhuman_%.fastq.gz \
  -S /dev/null \
  --very-sensitive \
  --threads 16

# nonhuman_1.fastq.gz and nonhuman_2.fastq.gz are the microbial reads
```

### Step 4: Taxonomic Classification (Kraken2 + Bracken)
```bash
kraken2 \
  --db ~/databases/k2_standard \
  --paired nonhuman_1.fastq.gz nonhuman_2.fastq.gz \
  --output kraken_raw.txt \
  --report kraken_report.txt \
  --threads 16 \
  --confidence 0.1  # reduce false positives

# Bracken: re-estimate abundances at species level
bracken \
  -d ~/databases/k2_standard \
  -i kraken_report.txt \
  -o bracken_species.txt \
  -l S \
  -t 10  # minimum read threshold
```

### Step 5: Extract the 6 Key Metrics
```bash
# Save this as extract_key_metrics.sh

# 1. F. prausnitzii
echo "=== F. prausnitzii ==="
grep "Faecalibacterium prausnitzii" bracken_species.txt | awk '{print $7}' 
# Column 7 = fraction of total reads. Multiply by 100 for %.

# 2. Akkermansia muciniphila
echo "=== Akkermansia muciniphila ==="
grep "Akkermansia muciniphila" bracken_species.txt | awk '{print $7}'

# 3. Proteobacteria %
echo "=== Proteobacteria % ==="
grep "	Proteobacteria	" kraken_report.txt | awk '{print $1, $2}'

# 4. Histamine producers
echo "=== Histamine producers ==="
grep -E "Morganella morganii|Klebsiella pneumoniae|Klebsiella oxytoca" bracken_species.txt

# 5. CrAssphage (Bacteroides phage)
echo "=== CrAssphage ==="
grep -i "crass" bracken_report.txt
grep -i "crAss" kraken_report.txt

# 6. Candida
echo "=== Candida/Fungi ==="
grep "Candida" bracken_species.txt
grep "Malassezia" bracken_species.txt  # usually not in gut but check
```

### Step 6: Functional Profiling (Butyrate Pathway)
```bash
# Merge paired reads for HUMAnN3
cat nonhuman_1.fastq.gz nonhuman_2.fastq.gz > merged_nonhuman.fastq.gz

humann3 \
  --input merged_nonhuman.fastq.gz \
  --output humann3_output/ \
  --threads 16 \
  --metaphlan-options "--bowtie2db ~/databases/metaphlan4"

# After HUMAnN3 completes:
# Check for butyrate pathway: PWY-5676 (acetyl-CoA fermentation to butanoate)
grep "PWY-5676" humann3_output/merged_nonhuman_pathabundance.tsv

# Also check:
# BUTANAL-BUTANOL-PWY (butanol fermentation)
# P162-PWY (hydrogen production)
# butyrate kinase gene (buk) and butyryl-CoA:acetate CoA-transferase (but)
grep -i "but" humann3_output/merged_nonhuman_genefamilies.tsv | grep -i "transferase"
```

### Step 7: Phage Detection (optional, advanced)
```bash
# Assemble contigs first (requires ~8GB RAM, ~30 min on DGX)
metaspades.py \
  -1 nonhuman_1.fastq.gz -2 nonhuman_2.fastq.gz \
  -o spades_assembly/ \
  --threads 16 \
  --memory 64

# Run VirSorter2 on assembled contigs
virsorter2 \
  -i spades_assembly/contigs.fasta \
  -o virsorter2_output/ \
  --include-groups dsDNAphage,ssDNA,NCLDV,RNA,lavidaviridae \
  -j 16 \
  --min-score 0.5 \
  --min-length 1500
```

---

## Expected Output Interpretation

| Metric | Healthy range | Concerning | Action |
|--------|--------------|-----------|--------|
| F. prausnitzii % | >5% | <1% | Tributyrin/butyrate supplement; high-fiber diet |
| Akkermansia % | Detectable (>0.1%) | Absent or <0.01% | Polyphenol-rich diet (cranberry, pomegranate); metformin raises Akkermansia |
| Proteobacteria % | <10% | >20% | Significant dysbiosis; investigate source (SIBO?) |
| Morganella / Klebsiella | Low/absent | Detected | Run DAO kill test (Run 003 protocol) |
| CrAssphage | Detectable | Absent | Low Bacteroides phage = less Bacteroides density control |
| Candida | <0.1% | >0.5% | Consider antifungal, reduce sugar/dairy |

---

## If You Don't Want to Run Bioinformatics Yourself

**Option A:** Use TinyHealth's dashboard — they report F. prausnitzii and Akkermansia already. Sufficient for basic M4 proxy check.

**Option B:** Send FASTQ to: 
- One Codex (onecodex.com) — upload FASTQ, get interactive report (~$50-100)
- Strainly / MicrobiomePrescription — upload FASTQ, get analysis
- CosmosID — commercial service for shotgun metagenomics

**Option C:** Run on DGX Spark directly — recommended for phage analysis (needs the assembly step which requires more compute than most laptops).

---

## DGX-Specific Advantages

The DGX Spark has 128GB RAM and the GB10 Blackwell GPU. Key benefits:
- Kraken2 + Bracken: fits entire k2_standard database in RAM → ~5× faster classification vs disk-based
- MetaSPAdes assembly: RAM-intensive; 128GB handles most gut samples without memlimit issues
- Parallelization: all tools support `--threads 16-32`; DGX can run full pipeline in ~2-4 hours vs ~12-24h on laptop

Recommended to activate venv and run in job queue:
```bash
python3 ~/ComfyUI/jobs/spark_job.py shell "conda activate metagenomics && bash /path/to/pipeline.sh"
```

---
*Run 004 FASTQ protocol: complete bioinformatics pipeline. DGX Spark can run in-RAM for fast classification. Quick option: TinyHealth dashboard already has F.prausnitzii + Akkermansia. Advanced: full pipeline for phage detection via VirSorter2.*
