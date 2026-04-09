#!/usr/bin/env python3
"""
GSE25504 — Blood transcriptomics of neonatal sepsis
35 uninfected controls vs 28 infected neonates
Illumina HT-12 v4.0 microarray
Normalization: already pre-normalized (signal intensity values)

Tests the neonatal sepsis campaign model (pattern 001 etc.):
- IFN response in neonates (likely blunted — immature immunity)
- Inflammasome activation
- Kupffer-cell-equivalent innate immune genes
- Maternal antibody response (no Ig repertoire available in cfRNA)
- Specific CVB targets: dystrophin, CXADR
- Mitochondrial function (neonatal sepsis is a mitochondrial crisis)
- Markers of septic multi-organ involvement: cardiac (troponin TNNT2, TNNI3),
  hepatic (ALB, AFP), renal (UMOD)
"""

import gzip
import numpy as np
import json
import re
from scipy import stats
import os

DATA = "~/open_problems/medical/numerics/transcriptomics/neonatal_sepsis/GSE25504_fixed.txt.gz"
OUT = "~/open_problems/medical/neonatal_sepsis/results"
os.makedirs(OUT, exist_ok=True)

# Target gene symbols — HGNC
TARGETS = {
    # IFN response (predicted BLUNTED in neonates — campaign insight)
    "IFIT1": "IFN type I response",
    "IFIT2": "IFN type I response",
    "IFIT3": "IFN type I response",
    "MX1": "IFN antiviral ISG",
    "ISG15": "IFN antiviral ISG",
    "OAS1": "IFN antiviral ISG",
    "OAS2": "IFN antiviral ISG",
    "IFI6": "IFN antiviral ISG",
    "IFI27": "IFN antiviral ISG",
    "RSAD2": "Viperin — antiviral",
    "DDX58": "RIG-I cytoplasmic sensor",
    "IFIH1": "MDA5 cytoplasmic sensor",
    "STAT1": "IFN transcription",
    "STAT2": "IFN type I transcription",
    "IRF1": "IFN regulatory factor",
    "IRF7": "IFN master regulator",

    # Inflammasome — predicted active in sepsis
    "NLRP3": "Inflammasome",
    "CASP1": "Inflammasome effector",
    "IL1B": "Inflammasome cytokine",
    "IL18": "Inflammasome cytokine",

    # Cytokines — expected elevated
    "TNF": "TNF-alpha",
    "IL6": "IL-6 key sepsis biomarker",
    "IL10": "Anti-inflammatory (compensatory)",
    "CXCL10": "IFN-gamma-induced chemokine",
    "CXCL9": "IFN-gamma-induced chemokine",
    "CCL2": "Monocyte chemoattractant",
    "CXCL8": "IL-8 neutrophil chemoattractant",

    # Neutrophil activation
    "ELANE": "Neutrophil elastase",
    "MPO": "Myeloperoxidase",
    "DEFA1": "Defensin-alpha-1",
    "S100A8": "Calprotectin",
    "S100A9": "Calprotectin",
    "LCN2": "NGAL",
    "FCN1": "Ficolin-1 monocyte (top ME/CFS hit)",

    # Complement
    "C1QA": "Complement C1q",
    "C1QB": "Complement C1q",
    "C3": "Complement C3",

    # Treg
    "FOXP3": "Treg master regulator",

    # T cell exhaustion markers (unlikely in neonatal sepsis but test)
    "PDCD1": "PD-1",
    "LAG3": "LAG-3",

    # NK cell function
    "PRF1": "Perforin",
    "GZMB": "Granzyme B",
    "NCAM1": "CD56 NK marker",

    # Mitochondrial crisis markers
    "PPARGC1A": "PGC-1alpha mitochondrial biogenesis master regulator",
    "TFAM": "Mitochondrial transcription factor",
    "NRF1": "Nuclear respiratory factor",
    "COX4I1": "Cytochrome c oxidase subunit 4",
    "NDUFA1": "NADH dehydrogenase (Complex I)",
    "NDUFB1": "NADH dehydrogenase (Complex I)",
    "UQCRQ": "Ubiquinol-cytochrome c reductase (Complex III)",
    "ATP5A1": "ATP synthase alpha",
    "BCL2L13": "Mitophagy",

    # Apoptosis
    "CASP3": "Effector caspase",
    "BAX": "Pro-apoptotic",
    "BCL2": "Anti-apoptotic",
    "BID": "BH3-only pro-apoptotic",

    # Autophagy (campaign)
    "ATG7": "Autophagy E1",
    "LC3B": "LC3B (MAP1LC3B)",
    "MAP1LC3B": "LC3B",
    "BECN1": "Beclin-1",
    "SQSTM1": "p62",
    "LAMP1": "Lysosomal marker",
    "LAMP2": "Lysosomal membrane (CVB target)",

    # CVB / enteroviral receptors
    "CXADR": "CVB receptor",
    "CD55": "DAF alternative CVB receptor",

    # CVB 2A protease target
    "DMD": "Dystrophin (cleaved by CVB 2A)",

    # Cardiac injury markers
    "TNNT2": "Cardiac troponin T",
    "TNNI3": "Cardiac troponin I",
    "NPPB": "BNP heart failure marker",

    # Hepatic injury
    "ALB": "Albumin — liver function",
    "AFP": "Alpha-fetoprotein — neonatal liver marker",

    # Maternal-fetal biology
    "HLA-G": "Non-classical MHC fetal tolerance",
    "CGA": "Chorionic gonadotropin alpha",
}

print("Loading GSE25504 neonatal sepsis transcriptomics...")
print(f"Data: {DATA}")

header = None
sample_cols = []
sample_labels = []
symbol_col = None

rows_by_symbol = {}

with gzip.open(DATA, 'rt') as f:
    header = f.readline().rstrip('\n').split('\t')
    # Sample columns: Con_* and Inf* (including Inf075 no underscore)
    for i, h in enumerate(header):
        if h.startswith('Con_'):
            sample_cols.append(i)
            sample_labels.append('Control')
        elif h.startswith('Inf_') or (h.startswith('Inf') and h[3:4].isdigit()):
            sample_cols.append(i)
            sample_labels.append('Infected')
        elif h == 'SYMBOL':
            symbol_col = i

    print(f"Found {len([l for l in sample_labels if l=='Control'])} controls")
    print(f"Found {len([l for l in sample_labels if l=='Infected'])} infected")
    print(f"Symbol column: {symbol_col}")

    # Read data rows
    for line in f:
        parts = line.rstrip('\n').split('\t')
        if len(parts) <= symbol_col:
            continue
        sym = parts[symbol_col].strip() if symbol_col else ''
        if sym in TARGETS:
            try:
                values = []
                for i in sample_cols:
                    v = parts[i].strip()
                    values.append(float(v) if v else 0)
                values = np.array(values)
                if sym not in rows_by_symbol:
                    rows_by_symbol[sym] = []
                rows_by_symbol[sym].append(values)
            except (ValueError, IndexError):
                continue

print(f"\nFound data for {len(rows_by_symbol)} / {len(TARGETS)} target genes")

# Average multiple probes per gene
sample_labels_arr = np.array(sample_labels)
ctrl_idx = np.where(sample_labels_arr == 'Control')[0]
inf_idx = np.where(sample_labels_arr == 'Infected')[0]

print(f"\nDifferential expression: Infected (n={len(inf_idx)}) vs Control (n={len(ctrl_idx)})")

# The data values look like linear Illumina signals (80-130 range)
# Best approach: log2 after floor, then t-test
results = []
for sym, probe_data in rows_by_symbol.items():
    # Average across probes for each sample
    merged = np.mean(np.array(probe_data), axis=0)
    # Log2 transform (add floor to handle small/zero values)
    log_vals = np.log2(np.maximum(merged, 1) + 1)
    ctrl_vals = log_vals[ctrl_idx]
    inf_vals = log_vals[inf_idx]
    log2fc = np.mean(inf_vals) - np.mean(ctrl_vals)
    t, p = stats.ttest_ind(inf_vals, ctrl_vals, equal_var=False)
    results.append({
        'symbol': sym,
        'description': TARGETS[sym],
        'log2fc': float(log2fc),
        'fc': float(2**log2fc),
        'pvalue': float(p),
        'ctrl_mean': float(np.mean(ctrl_vals)),
        'inf_mean': float(np.mean(inf_vals)),
        'n_probes': len(probe_data),
    })

results.sort(key=lambda r: -abs(r['log2fc']))

# Report
print("\n" + "="*85)
print("NEONATAL SEPSIS (GSE25504) — Target gene analysis")
print("="*85)
print(f"{'Symbol':<12} {'log2FC':>8} {'FC':>8} {'p':>10}  {'dir':<6} Description")
print("-"*85)
for r in results:
    direction = "UP" if r['log2fc'] > 0 else "DOWN"
    sig = "*" if r['pvalue'] < 0.05 else " "
    print(f"{r['symbol']:<12} {r['log2fc']:+8.3f} {r['fc']:>8.3f} {r['pvalue']:>10.4e}  {direction:<5}{sig} {r['description']}")

# Significant hits
sig_count = sum(1 for r in results if r['pvalue'] < 0.05)
print(f"\nSignificant (p<0.05): {sig_count}/{len(results)}")

# Bonferroni threshold
bonf = 0.05 / len(results)
strict = sum(1 for r in results if r['pvalue'] < bonf)
print(f"Bonferroni-strict (p<{bonf:.2e}): {strict}/{len(results)}")

output = {
    'dataset': 'GSE25504',
    'description': 'Neonatal sepsis whole blood transcriptomics',
    'n_controls': int(len(ctrl_idx)),
    'n_infected': int(len(inf_idx)),
    'target_genes_queried': len(TARGETS),
    'target_genes_found': len(results),
    'significant_nominal': int(sig_count),
    'significant_bonferroni': int(strict),
    'bonferroni_threshold': float(bonf),
    'results': results,
}

with open(os.path.join(OUT, 'gse25504_analysis.json'), 'w') as f:
    json.dump(output, f, indent=2)

print(f"\nResults saved to {OUT}/gse25504_analysis.json")
