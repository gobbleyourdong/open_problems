#!/usr/bin/env python3
"""
Analysis of GSE293840 — ME/CFS cell-free RNA (cfRNA) plasma profiling
n=93 ME/CFS + n=75 healthy sedentary controls (168 total)

Published: cfRNA-based ML classifier achieved AUC 0.81, accuracy 77%
Paper finding: elevated plasmacytoid DC, monocyte, T cell-derived cfRNA in ME/CFS;
signatures of cytokine signaling and T cell exhaustion.

Our question: do the ME/CFS vs control differences validate the CVB campaign
model of ME/CFS as chronic low-grade inflammation + mitochondrial dysfunction +
NK/T-cell exhaustion driven by persistent viral infection?

Key predictions to test:
1. IFN pathway elevated (chronic low-grade viral stimulus) — IFIT1/2/3, MX1, ISG15
2. T cell exhaustion markers elevated — PDCD1, LAG3, TIGIT, HAVCR2 (Tim3)
3. NK cell dysfunction markers — KLRK1 (NKG2D), NCR1, PRF1
4. Mitochondrial dysfunction — MT-ND1, NDUFA, ATP5 genes
5. Inflammasome — NLRP3, CASP1, IL1B, IL18
6. Enteroviral receptors (tissue damage markers) — CXADR, CD55
7. Butyrate/Treg axis — FOXP3, IL10
8. Cytokine signaling — IL6, TNF, IFNG, CXCL10
"""

import gzip
import csv
import numpy as np
import json
import re
from collections import defaultdict
from scipy import stats
import os

DATA_DIR = "/home/jb/open_problems/medical/numerics/transcriptomics/mecfs"
COUNTS_FILE = os.path.join(DATA_DIR, "GSE293840_raw_counts_all.csv.gz")
META_FILE = os.path.join(DATA_DIR, "GSE293840_series_matrix.txt.gz")
OUT_DIR = "/home/jb/open_problems/medical/me_cfs/results"
os.makedirs(OUT_DIR, exist_ok=True)

# ─── Target genes (Ensembl IDs) ───────────────────────────────────────────
# We need ENSG to HGNC mapping. Counts file has ENSG IDs.
# Hardcode the ones we care about using known Ensembl gene IDs.
TARGETS = {
    # IFN response — predicted UP in chronic viral stimulus
    "ENSG00000185745": "IFIT1",
    "ENSG00000119922": "IFIT2",
    "ENSG00000119917": "IFIT3",
    "ENSG00000157601": "MX1",
    "ENSG00000188641": "DPYD",   # placeholder -- will skip if not found
    "ENSG00000187608": "ISG15",
    "ENSG00000115267": "IFIH1",  # MDA5
    "ENSG00000107201": "DDX58",  # RIG-I
    "ENSG00000126709": "IFI6",
    "ENSG00000126602": "TRAP1",
    "ENSG00000115415": "STAT1",
    "ENSG00000170581": "STAT2",

    # T cell exhaustion markers — predicted UP
    "ENSG00000188389": "PDCD1",   # PD-1
    "ENSG00000089692": "LAG3",
    "ENSG00000181847": "TIGIT",
    "ENSG00000135077": "HAVCR2",  # Tim-3
    "ENSG00000178562": "CD28",
    "ENSG00000120217": "CD274",   # PD-L1
    "ENSG00000163599": "CTLA4",

    # NK cell function
    "ENSG00000213809": "KLRK1",   # NKG2D
    "ENSG00000189430": "NCR1",    # NKp46
    "ENSG00000180644": "PRF1",    # perforin
    "ENSG00000145649": "GZMA",
    "ENSG00000100453": "GZMB",

    # Inflammasome
    "ENSG00000162711": "NLRP3",
    "ENSG00000137752": "CASP1",
    "ENSG00000125538": "IL1B",
    "ENSG00000150782": "IL18",
    "ENSG00000105639": "JAK3",

    # Mitochondrial complex I, ATP synthase, MT-encoded
    "ENSG00000198888": "MT-ND1",
    "ENSG00000198763": "MT-ND2",
    "ENSG00000198938": "MT-CO3",
    "ENSG00000198899": "MT-ATP6",
    "ENSG00000198786": "MT-ND5",
    "ENSG00000198712": "MT-CO2",
    "ENSG00000198804": "MT-CO1",
    "ENSG00000198695": "MT-ND6",
    "ENSG00000198840": "MT-ND3",
    "ENSG00000212907": "MT-ND4L",
    "ENSG00000198886": "MT-ND4",
    "ENSG00000198727": "MT-CYB",

    # Cytokines
    "ENSG00000136244": "IL6",
    "ENSG00000232810": "TNF",
    "ENSG00000111537": "IFNG",
    "ENSG00000169245": "CXCL10",
    "ENSG00000204252": "HLA-DOA",
    "ENSG00000125347": "IRF1",
    "ENSG00000138378": "STAT4",

    # Treg / butyrate axis
    "ENSG00000049768": "FOXP3",
    "ENSG00000136634": "IL10",
    "ENSG00000136514": "RTP4",
    "ENSG00000114019": "AMOTL2",

    # Enteroviral receptors
    "ENSG00000154639": "CXADR",
    "ENSG00000196352": "CD55",

    # Autophagy (campaign model)
    "ENSG00000197548": "ATG7",
    "ENSG00000107815": "TWNK",
    "ENSG00000005022": "SLC25A5",
    "ENSG00000005194": "CIAPIN1",

    # BDCA markers (plasmacytoid DC) — paper mentioned these
    "ENSG00000164399": "IL3",
    "ENSG00000085265": "FCN1",   # monocyte marker
    "ENSG00000203747": "FCGR3A", # CD16 NK/mono
    "ENSG00000132952": "USPL1",
}

print(f"Loading metadata from {META_FILE}...")

# ─── Parse metadata (sample titles encode case/control) ─────────────────
sample_labels = {}  # sample_name -> "ME/CFS" or "healthy"
with gzip.open(META_FILE, 'rt') as f:
    for line in f:
        if line.startswith('!Sample_title'):
            fields = line.strip().split('\t')[1:]
            for field in fields:
                field = field.strip().strip('"')
                # "Plasma cell-free RNA, RNA seq for subject: cfs_cfrna_001, healthy control"
                m = re.match(r'.*subject:\s*(cfs_cfrna_\d+),\s*(.+)$', field)
                if m:
                    sample_id = m.group(1)
                    label = m.group(2).strip()
                    if 'ME/CFS' in label or 'ME/CSF' in label or 'patient' in label.lower():
                        sample_labels[sample_id] = 'ME/CFS'
                    else:
                        sample_labels[sample_id] = 'control'
            break

n_case = sum(1 for v in sample_labels.values() if v == 'ME/CFS')
n_ctrl = sum(1 for v in sample_labels.values() if v == 'control')
print(f"Parsed labels: {n_case} ME/CFS patients, {n_ctrl} healthy controls")
print(f"Total labeled: {len(sample_labels)}")

# ─── Load counts (only target genes + all samples) ─────────────────────
print(f"\nLoading target gene counts from {COUNTS_FILE}...")

# First pass: read sample headers
with gzip.open(COUNTS_FILE, 'rt') as f:
    header = f.readline().strip().split(',')
    samples = header[1:]  # first col is gene ID

# Map sample names to normalized form
# counts file uses "cfs_cfrna_1" (no leading zero), metadata uses "cfs_cfrna_001"
def normalize_sample(name):
    m = re.match(r'(cfs_cfrna_)(\d+)$', name)
    if m:
        return f"{m.group(1)}{int(m.group(2)):03d}"
    return name

sample_normalized = [normalize_sample(s) for s in samples]

# Find case/control indices
case_indices = [i for i, s in enumerate(sample_normalized) if sample_labels.get(s) == 'ME/CFS']
ctrl_indices = [i for i, s in enumerate(sample_normalized) if sample_labels.get(s) == 'control']

print(f"Case indices: {len(case_indices)} | Control indices: {len(ctrl_indices)}")
print(f"Unmatched: {len(samples) - len(case_indices) - len(ctrl_indices)}")

# Second pass: read only target gene rows
print("\nReading counts for target genes...")
gene_data = {}
with gzip.open(COUNTS_FILE, 'rt') as f:
    header = f.readline()
    for line in f:
        parts = line.strip().split(',')
        gene_id = parts[0].split('.')[0]  # strip version
        if gene_id in TARGETS:
            try:
                counts = np.array([float(x) if x else 0 for x in parts[1:]])
                gene_data[gene_id] = counts
            except ValueError:
                pass

print(f"Found {len(gene_data)} / {len(TARGETS)} target genes in counts file")

# ─── CPM normalization (simple library size normalization) ─────────────
print("\nNormalizing (CPM)...")

# Compute library sizes from target genes is unreliable; use a rough proxy.
# Better: compute total counts across all genes in the file (third pass)
print("Computing library sizes...")
lib_sizes = np.zeros(len(samples))
with gzip.open(COUNTS_FILE, 'rt') as f:
    header = f.readline()
    for line in f:
        parts = line.strip().split(',')
        try:
            counts = np.array([float(x) if x else 0 for x in parts[1:]])
            lib_sizes += counts
        except ValueError:
            continue

print(f"Library sizes: median {np.median(lib_sizes):.0f}, range {lib_sizes.min():.0f}-{lib_sizes.max():.0f}")

# CPM + log2(CPM + 1)
def to_logcpm(counts, libs):
    cpm = 1e6 * counts / np.maximum(libs, 1)
    return np.log2(cpm + 1)

# ─── Differential expression ───────────────────────────────────────────
print("\nComputing differential expression (ME/CFS vs control)...")
results = []
for gene_id, counts in gene_data.items():
    logcpm = to_logcpm(counts, lib_sizes)
    case_vals = logcpm[case_indices]
    ctrl_vals = logcpm[ctrl_indices]
    if len(case_vals) == 0 or len(ctrl_vals) == 0:
        continue
    log2fc = np.mean(case_vals) - np.mean(ctrl_vals)
    # Welch's t-test
    tstat, pval = stats.ttest_ind(case_vals, ctrl_vals, equal_var=False)
    results.append({
        'ensg': gene_id,
        'symbol': TARGETS[gene_id],
        'log2fc': float(log2fc),
        'fc': float(2**log2fc),
        'pvalue': float(pval),
        'case_mean_logcpm': float(np.mean(case_vals)),
        'ctrl_mean_logcpm': float(np.mean(ctrl_vals)),
        'case_n_nonzero': int(np.sum(counts[case_indices] > 0)),
        'ctrl_n_nonzero': int(np.sum(counts[ctrl_indices] > 0)),
    })

# Sort by absolute log2FC
results.sort(key=lambda r: -abs(r['log2fc']))

# ─── Report ───────────────────────────────────────────
print("\n" + "="*80)
print("ME/CFS cfRNA — Top differentially expressed target genes")
print("="*80)
print(f"{'Symbol':<10} {'log2FC':>8} {'FC':>8} {'p-value':>10} {'direction':<10}")
print("-"*80)

for r in results[:40]:
    direction = "UP" if r['log2fc'] > 0 else "DOWN"
    sig = "*" if r['pvalue'] < 0.05 else " "
    print(f"{r['symbol']:<10} {r['log2fc']:+8.3f} {r['fc']:>8.3f} {r['pvalue']:>10.4f} {direction}{sig}")

# ─── Save JSON ───────────────────────────────────────────
output = {
    'dataset': 'GSE293840',
    'description': 'Plasma cell-free RNA, ME/CFS vs healthy controls',
    'n_cases': len(case_indices),
    'n_controls': len(ctrl_indices),
    'total_samples': len(samples),
    'unmatched_samples': len(samples) - len(case_indices) - len(ctrl_indices),
    'target_genes_found': len(gene_data),
    'target_genes_queried': len(TARGETS),
    'results': results,
}

out_json = os.path.join(OUT_DIR, 'mecfs_cfrna_analysis.json')
with open(out_json, 'w') as f:
    json.dump(output, f, indent=2)
print(f"\nResults saved to {out_json}")

# Significant genes
sig_results = [r for r in results if r['pvalue'] < 0.05]
print(f"\nSignificant genes (p<0.05): {len(sig_results)}/{len(results)}")
for r in sig_results:
    direction = "UP" if r['log2fc'] > 0 else "DOWN"
    print(f"  {r['symbol']:<10} log2FC={r['log2fc']:+.3f} FC={r['fc']:.2f}x p={r['pvalue']:.4f} {direction}")
