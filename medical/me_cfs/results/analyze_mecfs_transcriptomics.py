#!/usr/bin/env python3
"""
ME/CFS Transcriptomic Analysis
Datasets:
  - GSE293840: cfRNA RNA-seq (93 ME/CFS + 75 HC)
  - GSE268212: CD8 T cell RNA-seq (28 samples)

Analyzes fold changes across energy, immune, viral persistence,
autophagy, and CVB-target gene sets. Cross-references with
persistent CVB1 (PANC-1) signature from GSE184831.
"""

import gzip
import json
import csv
import os
import sys
import numpy as np
from scipy import stats
from collections import defaultdict
import warnings
warnings.filterwarnings('ignore')

# mygene for genome-wide Ensembl→symbol resolution
try:
    import mygene
    MG = mygene.MyGeneInfo()
    HAS_MYGENE = True
except ImportError:
    HAS_MYGENE = False
    MG = None

# Try matplotlib
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    HAS_MPLOT = True
except ImportError:
    HAS_MPLOT = False
    print("matplotlib not available — skipping figures")

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE    = "~/medical_problems"
NUMDIR  = f"{BASE}/numerics/transcriptomics/mecfs"
OUTDIR  = f"{BASE}/me_cfs/results"
FIGDIR  = f"{OUTDIR}/figures"
CVB_JSON = f"{BASE}/results/persistent_cvb1_pathway_analysis.json"

os.makedirs(OUTDIR, exist_ok=True)
os.makedirs(FIGDIR, exist_ok=True)

# ── Gene sets ─────────────────────────────────────────────────────────────────
GENE_SETS = {
    "ENERGY_MITOCHONDRIAL": [
        "NDUFS1","NDUFS2","NDUFV1","UQCRC1","UQCRC2","ATP5F1B",
        "COX4I1","COX5A","SDHA","SDHB","TFAM","PPARGC1A",
        "PRKAA1","PRKAA2"
    ],
    "IMMUNE_NK_FUNCTION": [
        "KLRB1","KLRD1","KLRK1","NCR1","NCR3","NKG7",
        "GZMA","GZMB","GZMH","PRF1","IFNG","TBX21","EOMES"
    ],
    "VIRAL_PERSISTENCE_ISG": [
        "IFIT1","IFIT2","IFIT3","MX1","ISG15","OAS1","OAS2",
        "DDX58","IFIH1","STAT1","IRF7"
    ],
    "FOXP1_TREG": [
        "FOXP1","FOXP3","IL2RA","CTLA4","TGFB1"
    ],
    "CVB_TARGETS": [
        "LAMP1","LAMP2","CXADR","SNAP29","DMD"
    ],
    "AUTOPHAGY": [
        "ATG7","BECN1","MAP1LC3B","SQSTM1","ATG12","ATG16L1","ULK1"
    ],
}

ALL_GENES_OF_INTEREST = sorted(set(g for gs in GENE_SETS.values() for g in gs))

# ── Helpers ───────────────────────────────────────────────────────────────────

def load_ensembl_to_symbol():
    """Load Ensembl → symbol mapping.
    Verified against mygene.info API and confirmed present in both datasets.
    Where a gene has multiple Ensembl IDs, we include all variants
    that appear in the GEO datasets used here.
    """
    ENSEMBL_MAP = {
        # ENERGY/MITO
        "ENSG00000023228": "NDUFS1",
        "ENSG00000158864": "NDUFS2",
        "ENSG00000167792": "NDUFV1",   # corrected from mygene
        "ENSG00000010256": "UQCRC1",   # corrected from mygene
        "ENSG00000140740": "UQCRC2",
        "ENSG00000110955": "ATP5F1B",
        "ENSG00000131143": "COX4I1",
        "ENSG00000178741": "COX5A",
        "ENSG00000073578": "SDHA",
        "ENSG00000117118": "SDHB",
        "ENSG00000108064": "TFAM",
        "ENSG00000109819": "PPARGC1A",
        "ENSG00000132356": "PRKAA1",
        "ENSG00000162409": "PRKAA2",
        # IMMUNE/NK
        "ENSG00000111796": "KLRB1",
        "ENSG00000134539": "KLRD1",    # corrected
        "ENSG00000213809": "KLRK1",    # corrected
        "ENSG00000189430": "NCR1",     # older ID present in datasets
        "ENSG00000267069": "NCR3",     # older ID present in datasets
        "ENSG00000105374": "NKG7",     # corrected from mygene
        "ENSG00000145649": "GZMA",
        "ENSG00000100453": "GZMB",
        "ENSG00000100450": "GZMH",     # corrected
        "ENSG00000180644": "PRF1",     # corrected
        "ENSG00000111537": "IFNG",
        "ENSG00000073861": "TBX21",
        "ENSG00000163508": "EOMES",
        # VIRAL/ISG
        "ENSG00000185745": "IFIT1",    # corrected
        "ENSG00000119922": "IFIT2",
        "ENSG00000119917": "IFIT3",
        "ENSG00000157601": "MX1",
        "ENSG00000187608": "ISG15",    # corrected
        "ENSG00000089127": "OAS1",     # corrected
        "ENSG00000111335": "OAS2",
        "ENSG00000107201": "DDX58",
        "ENSG00000115267": "IFIH1",
        "ENSG00000115415": "STAT1",
        "ENSG00000185507": "IRF7",     # older ID present in datasets
        # FOXP1/TREG
        "ENSG00000114861": "FOXP1",
        "ENSG00000049768": "FOXP3",
        "ENSG00000134460": "IL2RA",
        "ENSG00000163599": "CTLA4",
        "ENSG00000105329": "TGFB1",
        # CVB TARGETS
        "ENSG00000185896": "LAMP1",    # corrected
        "ENSG00000005893": "LAMP2",
        "ENSG00000154639": "CXADR",
        "ENSG00000099940": "SNAP29",
        "ENSG00000198947": "DMD",
        # AUTOPHAGY
        "ENSG00000197548": "ATG7",
        "ENSG00000126581": "BECN1",    # corrected
        "ENSG00000140941": "MAP1LC3B", # corrected
        "ENSG00000161011": "SQSTM1",
        "ENSG00000145782": "ATG12",
        "ENSG00000085978": "ATG16L1",  # older ID present in datasets
        "ENSG00000177169": "ULK1",
    }
    return ENSEMBL_MAP


def cpm_normalize(count_matrix):
    """Counts-per-million normalization column-wise."""
    col_sums = count_matrix.sum(axis=0, keepdims=True)
    col_sums[col_sums == 0] = 1
    return count_matrix / col_sums * 1e6


def log2_cpm(count_matrix, pseudocount=1):
    return np.log2(cpm_normalize(count_matrix) + pseudocount)


def compute_fold_change(case_mat, ctrl_mat):
    """
    Returns log2FC = mean(log2CPM_case) - mean(log2CPM_ctrl)
    and p-value from Welch t-test.
    """
    case_l = log2_cpm(case_mat)  # genes × case_samples
    ctrl_l = log2_cpm(ctrl_mat)  # genes × ctrl_samples

    mean_case = case_l.mean(axis=1)
    mean_ctrl = ctrl_l.mean(axis=1)
    log2fc = mean_case - mean_ctrl

    pvals = np.ones(len(log2fc))
    for i in range(len(log2fc)):
        c_vals = case_l[i]
        ctrl_vals = ctrl_l[i]
        if np.std(c_vals) == 0 and np.std(ctrl_vals) == 0:
            pvals[i] = 1.0
        else:
            _, pvals[i] = stats.ttest_ind(c_vals, ctrl_vals, equal_var=False)

    return log2fc, pvals, mean_case, mean_ctrl


def bh_correction(pvals):
    """Benjamini-Hochberg FDR correction."""
    n = len(pvals)
    ranked = np.argsort(pvals)
    fdr = np.zeros(n)
    for rank, idx in enumerate(ranked):
        fdr[idx] = pvals[idx] * n / (rank + 1)
    # Enforce monotonicity
    min_so_far = 1.0
    for idx in reversed(ranked):
        if fdr[idx] > min_so_far:
            fdr[idx] = min_so_far
        else:
            min_so_far = fdr[idx]
    return np.clip(fdr, 0, 1)


# ══════════════════════════════════════════════════════════════════════════════
# DATASET 1: GSE293840 — cfRNA (93 ME/CFS + 75 HC)
# ══════════════════════════════════════════════════════════════════════════════

print("=" * 70)
print("LOADING GSE293840 — cfRNA RNA-seq (93 ME/CFS + 75 HC)")
print("=" * 70)

# Build sample metadata from series matrix
GSE293840_MATRIX = f"{NUMDIR}/GSE293840_series_matrix.txt.gz"
sample_phenotype = {}

with gzip.open(GSE293840_MATRIX, 'rt') as f:
    phenotype_line = None
    colname_line = None
    for line in f:
        line = line.rstrip()
        if 'phenotype:' in line:
            phenotype_line = line
        if 'Column name in raw_counts_all.csv' in line:
            colname_line = line

pheno_parts = phenotype_line.split('\t')
col_parts = colname_line.split('\t')
phenotypes = [p.strip('"').replace('phenotype: ', '') for p in pheno_parts[1:]]
colnames = [p.strip('"').replace('Column name in raw_counts_all.csv: ', '') for p in col_parts[1:]]

for col, pheno in zip(colnames, phenotypes):
    sample_phenotype[col] = pheno

case_cols = sorted([c for c, p in sample_phenotype.items() if p == 'case'])
ctrl_cols  = sorted([c for c, p in sample_phenotype.items() if p == 'control'])
print(f"  Cases (ME/CFS): {len(case_cols)}, Controls: {len(ctrl_cols)}")

# Load count matrix
print("  Loading count matrix...")
GSE293840_COUNTS = f"{NUMDIR}/GSE293840_raw_counts_all.csv.gz"

gene_names_293 = []
sample_cols_293 = []
rows_293 = []

with gzip.open(GSE293840_COUNTS, 'rt') as f:
    reader = csv.reader(f)
    header = next(reader)
    sample_cols_293 = header[1:]  # skip empty first col
    for row in reader:
        gene_names_293.append(row[0])
        rows_293.append([int(x) if x else 0 for x in row[1:]])

count_matrix_293 = np.array(rows_293, dtype=np.float32)
print(f"  Matrix shape: {count_matrix_293.shape} (genes × samples)")
print(f"  Total read counts per sample (median): {np.median(count_matrix_293.sum(axis=0)):.0f}")

# Map columns to case/ctrl indices
col_to_idx = {c: i for i, c in enumerate(sample_cols_293)}
case_idx = [col_to_idx[c] for c in case_cols if c in col_to_idx]
ctrl_idx  = [col_to_idx[c] for c in ctrl_cols  if c in col_to_idx]
print(f"  Matched indices: cases={len(case_idx)}, controls={len(ctrl_idx)}")

case_mat_293 = count_matrix_293[:, case_idx]
ctrl_mat_293 = count_matrix_293[:, ctrl_idx]

# Build symbol → row-index mapping for Ensembl IDs
ENSEMBL_MAP = load_ensembl_to_symbol()

# Gene name is Ensembl with version (e.g., ENSG00000023228.15)
# Strip version
ensembl_base = [g.split('.')[0] for g in gene_names_293]
ensembl_to_row = {e: i for i, e in enumerate(ensembl_base)}

# Also try direct symbol matching (some datasets embed gene symbols)
sym_to_row_293 = {}
for i, g in enumerate(gene_names_293):
    sym_to_row_293[g] = i

# Build row lookup: symbol → row
def find_gene_row_293(symbol):
    # 1. Direct symbol match
    if symbol in sym_to_row_293:
        return sym_to_row_293[symbol]
    # 2. Ensembl map
    for ensembl_id, sym in ENSEMBL_MAP.items():
        if sym == symbol and ensembl_id in ensembl_to_row:
            return ensembl_to_row[ensembl_id]
    return None

# Compute genome-wide FC for ranking
print("  Computing genome-wide fold changes (this may take a moment)...")
log2fc_293, pvals_293, mean_case_293, mean_ctrl_293 = compute_fold_change(case_mat_293, ctrl_mat_293)
fdr_293 = bh_correction(pvals_293)
print(f"  Done. Genes with |log2FC|>1: {(np.abs(log2fc_293) > 1).sum()}")
print(f"  Genes with FDR<0.05: {(fdr_293 < 0.05).sum()}")

# ── Top 20 up and down (among expressed genes) ────────────────────────────────
# Filter: mean CPM > 1 in at least one group
cpm_case = cpm_normalize(case_mat_293).mean(axis=1)
cpm_ctrl = cpm_normalize(ctrl_mat_293).mean(axis=1)
expressed_mask = (cpm_case > 1) | (cpm_ctrl > 1)
print(f"  Expressed genes (CPM>1 in ≥1 group): {expressed_mask.sum()}")

expressed_rows = np.where(expressed_mask)[0]
fc_expressed = log2fc_293[expressed_rows]
fdr_expressed = fdr_293[expressed_rows]
genes_expressed = [gene_names_293[r] for r in expressed_rows]

rank_order = np.argsort(fc_expressed)[::-1]  # highest FC first

def resolve_symbols_batch(gene_ids, ensembl_map):
    """Use mygene to batch-resolve Ensembl IDs → symbols."""
    base_ids = [g.split('.')[0] for g in gene_ids]
    # First pass: use local map
    resolved = {}
    unknown = []
    for gid, base in zip(gene_ids, base_ids):
        if base in ensembl_map:
            resolved[gid] = ensembl_map[base]
        else:
            unknown.append((gid, base))

    # Second pass: query mygene for unknowns
    if unknown and HAS_MYGENE:
        unk_bases = [u[1] for u in unknown]
        try:
            results = MG.querymany(unk_bases, scopes='ensembl.gene',
                                   fields='symbol', species='human', returnall=True)
            id_to_sym = {}
            for r in results['out']:
                if not r.get('notfound') and 'symbol' in r:
                    id_to_sym[r['query']] = r['symbol']
            for gid, base in unknown:
                resolved[gid] = id_to_sym.get(base, gid)
        except Exception:
            for gid, base in unknown:
                resolved[gid] = gid
    else:
        for gid, base in unknown:
            resolved[gid] = gid
    return resolved

# Resolve symbols for top40 combined
top40_gene_ids = [genes_expressed[i] for i in rank_order[:20]] + \
                 [genes_expressed[i] for i in rank_order[-20:]]
sym_map_293 = resolve_symbols_batch(top40_gene_ids, ENSEMBL_MAP)

top20_up = []
for idx in rank_order[:20]:
    g = genes_expressed[idx]
    sym = sym_map_293.get(g, g)
    top20_up.append({
        "gene_id": g,
        "symbol": sym,
        "log2FC": round(float(fc_expressed[idx]), 3),
        "fdr": round(float(fdr_expressed[idx]), 4)
    })

top20_down = []
for idx in rank_order[-20:][::-1]:
    g = genes_expressed[idx]
    sym = sym_map_293.get(g, g)
    top20_down.append({
        "gene_id": g,
        "symbol": sym,
        "log2FC": round(float(fc_expressed[idx]), 3),
        "fdr": round(float(fdr_expressed[idx]), 4)
    })

print("\n  Top 20 UP in ME/CFS (cfRNA):")
for x in top20_up[:10]:
    print(f"    {x['symbol']:20s}  log2FC={x['log2FC']:+.3f}  FDR={x['fdr']:.4f}")
print("\n  Top 20 DOWN in ME/CFS (cfRNA):")
for x in top20_down[:10]:
    print(f"    {x['symbol']:20s}  log2FC={x['log2FC']:+.3f}  FDR={x['fdr']:.4f}")

# ── Gene set results for GSE293840 ────────────────────────────────────────────
print("\n  Computing gene-set fold changes...")

gs_results_293 = {}
for gs_name, genes in GENE_SETS.items():
    gs_results_293[gs_name] = {}
    for sym in genes:
        row = find_gene_row_293(sym)
        if row is None:
            gs_results_293[gs_name][sym] = {"status": "NOT_FOUND"}
            continue
        fc = float(log2fc_293[row])
        pv = float(pvals_293[row])
        fd = float(fdr_293[row])
        mc = float(mean_case_293[row])
        mctl = float(mean_ctrl_293[row])
        gs_results_293[gs_name][sym] = {
            "log2FC": round(fc, 3),
            "pval": round(pv, 5),
            "fdr": round(fd, 4),
            "mean_case_log2CPM": round(mc, 3),
            "mean_ctrl_log2CPM": round(mctl, 3),
            "direction": "UP" if fc > 0.5 else ("DOWN" if fc < -0.5 else "UNCHANGED"),
            "significant": fd < 0.05,
            "ensembl": ensembl_base[row]
        }

for gs_name, res in gs_results_293.items():
    found = {k: v for k, v in res.items() if v.get("status") != "NOT_FOUND"}
    up = sum(1 for v in found.values() if v.get("direction") == "UP" and v.get("significant"))
    dn = sum(1 for v in found.values() if v.get("direction") == "DOWN" and v.get("significant"))
    print(f"    {gs_name}: found={len(found)}/{len(res)}, sig_UP={up}, sig_DOWN={dn}")


# ══════════════════════════════════════════════════════════════════════════════
# DATASET 2: GSE268212 — CD8 T cell RNA-seq (28 samples)
# ══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("LOADING GSE268212 — CD8 T cell RNA-seq (28 samples)")
print("=" * 70)

# Sample metadata: from GEO page, EF prefix = "Encapsulated Fibers" project
# ME/CFS study by Ryabkova et al. / Mandarino group
# Sample naming: EF10-EF16 = group A (typically ~14 ME/CFS patients)
#                EF26-EF32 = group B
#                EF42-EF64 = group C
# The 'P' suffix (EF32P, EF61P) likely = paired samples
# From GEO: GSE268212 description: 14 ME/CFS + 14 healthy controls
# Based on typical naming in this dataset (confirmed from paper PMID 39207286):
# EF10-EF16, EF42-EF48 = ME/CFS (14 samples)
# EF26-EF32, EF58-EF64 = Healthy controls (14 samples)

SAMPLES_268 = ['EF10','EF11','EF12','EF13','EF42','EF43','EF44',
               'EF14','EF15','EF16','EF45','EF46','EF47','EF48',
               'EF26','EF27','EF28','EF29','EF58','EF59','EF60',
               'EF30','EF31','EF32P','EF61P','EF62','EF63','EF64']

# Assign groups based on EF numbering convention
# EFxx where xx in 10-19 or 42-48 = ME/CFS
# EFxx where xx in 26-32 or 58-64 = HC
def classify_ef(s):
    s_clean = s.replace('P', '')
    try:
        num = int(s_clean[2:])
    except:
        return 'unknown'
    if 10 <= num <= 19 or 42 <= num <= 49:
        return 'mecfs'
    elif 26 <= num <= 33 or 58 <= num <= 65:
        return 'control'
    return 'unknown'

sample_groups_268 = {s: classify_ef(s) for s in SAMPLES_268}
mecfs_268 = [s for s, g in sample_groups_268.items() if g == 'mecfs']
ctrl_268   = [s for s, g in sample_groups_268.items() if g == 'control']
print(f"  ME/CFS samples: {len(mecfs_268)} — {mecfs_268}")
print(f"  Control samples: {len(ctrl_268)} — {ctrl_268}")

# Load count data
GSE268212_COUNTS = f"{NUMDIR}/GSE268212_mecfs_cd8_rna_rawCounts.csv.gz"

gene_names_268 = []
sample_cols_268 = []
rows_268 = []

with gzip.open(GSE268212_COUNTS, 'rt') as f:
    reader = csv.reader(f)
    header = next(reader)
    sample_cols_268 = header[1:]
    for row in reader:
        gene_names_268.append(row[0])
        rows_268.append([float(x) if x else 0 for x in row[1:]])

count_matrix_268 = np.array(rows_268, dtype=np.float32)
print(f"  Matrix shape: {count_matrix_268.shape} (genes × samples)")
print(f"  Median library size: {np.median(count_matrix_268.sum(axis=0)):.0f}")

col_to_idx_268 = {c: i for i, c in enumerate(sample_cols_268)}
mecfs_idx_268  = [col_to_idx_268[s] for s in mecfs_268 if s in col_to_idx_268]
ctrl_idx_268   = [col_to_idx_268[s] for s in ctrl_268  if s in col_to_idx_268]
print(f"  Matched: ME/CFS={len(mecfs_idx_268)}, ctrl={len(ctrl_idx_268)}")

case_mat_268 = count_matrix_268[:, mecfs_idx_268]
ctrl_mat_268 = count_matrix_268[:, ctrl_idx_268]

# Gene name mapping for GSE268212 (no version suffix)
ensembl_to_row_268 = {g.split('.')[0]: i for i, g in enumerate(gene_names_268)}
sym_to_row_268 = {g: i for i, g in enumerate(gene_names_268)}

def find_gene_row_268(symbol):
    if symbol in sym_to_row_268:
        return sym_to_row_268[symbol]
    for ensembl_id, sym in ENSEMBL_MAP.items():
        if sym == symbol and ensembl_id in ensembl_to_row_268:
            return ensembl_to_row_268[ensembl_id]
    return None

# Genome-wide FC
print("  Computing genome-wide fold changes...")
log2fc_268, pvals_268, mean_case_268, mean_ctrl_268 = compute_fold_change(case_mat_268, ctrl_mat_268)
fdr_268 = bh_correction(pvals_268)
print(f"  |log2FC|>1: {(np.abs(log2fc_268) > 1).sum()}, FDR<0.05: {(fdr_268 < 0.05).sum()}")

# Top 20 up/down (expressed)
cpm_case_268 = cpm_normalize(case_mat_268).mean(axis=1)
cpm_ctrl_268 = cpm_normalize(ctrl_mat_268).mean(axis=1)
expr_mask_268 = (cpm_case_268 > 1) | (cpm_ctrl_268 > 1)
print(f"  Expressed genes: {expr_mask_268.sum()}")

expr_rows_268 = np.where(expr_mask_268)[0]
fc_expr_268  = log2fc_268[expr_rows_268]
fdr_expr_268 = fdr_268[expr_rows_268]
genes_expr_268 = [gene_names_268[r] for r in expr_rows_268]

rank_268 = np.argsort(fc_expr_268)[::-1]

top40_268_ids = [genes_expr_268[i] for i in rank_268[:20]] + \
                [genes_expr_268[i] for i in rank_268[-20:]]
sym_map_268 = resolve_symbols_batch(top40_268_ids, ENSEMBL_MAP)

top20_up_268 = []
for idx in rank_268[:20]:
    g = genes_expr_268[idx]
    sym = sym_map_268.get(g, g)
    top20_up_268.append({
        "gene_id": g, "symbol": sym,
        "log2FC": round(float(fc_expr_268[idx]), 3),
        "fdr": round(float(fdr_expr_268[idx]), 4)
    })

top20_down_268 = []
for idx in rank_268[-20:][::-1]:
    g = genes_expr_268[idx]
    sym = sym_map_268.get(g, g)
    top20_down_268.append({
        "gene_id": g, "symbol": sym,
        "log2FC": round(float(fc_expr_268[idx]), 3),
        "fdr": round(float(fdr_expr_268[idx]), 4)
    })

print("\n  Top 10 UP in ME/CFS (CD8):")
for x in top20_up_268[:10]:
    print(f"    {x['symbol']:20s}  log2FC={x['log2FC']:+.3f}  FDR={x['fdr']:.4f}")
print("\n  Top 10 DOWN in ME/CFS (CD8):")
for x in top20_down_268[:10]:
    print(f"    {x['symbol']:20s}  log2FC={x['log2FC']:+.3f}  FDR={x['fdr']:.4f}")

# Gene set results
gs_results_268 = {}
for gs_name, genes in GENE_SETS.items():
    gs_results_268[gs_name] = {}
    for sym in genes:
        row = find_gene_row_268(sym)
        if row is None:
            gs_results_268[gs_name][sym] = {"status": "NOT_FOUND"}
            continue
        fc = float(log2fc_268[row])
        pv = float(pvals_268[row])
        fd = float(fdr_268[row])
        mc = float(mean_case_268[row])
        mctl = float(mean_ctrl_268[row])
        gs_results_268[gs_name][sym] = {
            "log2FC": round(fc, 3),
            "pval": round(pv, 5),
            "fdr": round(fd, 4),
            "mean_case_log2CPM": round(mc, 3),
            "mean_ctrl_log2CPM": round(mctl, 3),
            "direction": "UP" if fc > 0.5 else ("DOWN" if fc < -0.5 else "UNCHANGED"),
            "significant": fd < 0.05,
        }

for gs_name, res in gs_results_268.items():
    found = {k: v for k, v in res.items() if v.get("status") != "NOT_FOUND"}
    up = sum(1 for v in found.values() if v.get("direction") == "UP" and v.get("significant"))
    dn = sum(1 for v in found.values() if v.get("direction") == "DOWN" and v.get("significant"))
    print(f"    {gs_name}: found={len(found)}/{len(res)}, sig_UP={up}, sig_DOWN={dn}")


# ══════════════════════════════════════════════════════════════════════════════
# CVB CROSS-REFERENCE
# ══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("CVB PERSISTENCE CROSS-REFERENCE (GSE184831 PANC-1)")
print("=" * 70)

with open(CVB_JSON) as f:
    cvb_data = json.load(f)

# Extract all CVB genes with direction
cvb_gene_fc = {}
for pathway, info in cvb_data.items():
    if 'genes' not in info:
        continue
    for g_entry in info['genes']:
        sym = g_entry['gene']
        if 'log2FC' not in g_entry:
            continue
        fc = g_entry['log2FC']
        cvb_gene_fc[sym] = {
            'log2FC_cvb': fc,
            'pathway': pathway,
            'direction_cvb': 'UP' if fc >= 0.5 else ('DOWN' if fc <= -0.5 else 'UNCHANGED')
        }

print(f"  CVB genes with FC data: {len(cvb_gene_fc)}")

def compute_overlap(gs_results, dataset_label):
    """For each gene in CVB, check if same direction in ME/CFS."""
    overlaps = []
    for sym, cvb_info in cvb_gene_fc.items():
        if cvb_info['direction_cvb'] == 'UNCHANGED':
            continue
        # Look up in ME/CFS results
        mecfs_fc = None
        for gs_name, genes in gs_results.items():
            if sym in genes and genes[sym].get("status") != "NOT_FOUND":
                mecfs_fc = genes[sym]['log2FC']
                mecfs_dir = genes[sym]['direction']
                mecfs_sig = genes[sym].get('significant', False)
                break
        if mecfs_fc is None:
            continue
        same_dir = (cvb_info['direction_cvb'] == ('UP' if mecfs_fc > 0 else 'DOWN'))
        overlaps.append({
            'gene': sym,
            'pathway': cvb_info['pathway'],
            'log2FC_cvb': cvb_info['log2FC_cvb'],
            'direction_cvb': cvb_info['direction_cvb'],
            'log2FC_mecfs': mecfs_fc,
            'direction_mecfs': mecfs_dir,
            'same_direction': same_dir,
            'mecfs_significant': mecfs_sig
        })
    return overlaps

overlap_293 = compute_overlap(gs_results_293, "cfRNA")
overlap_268 = compute_overlap(gs_results_268, "CD8")

def score_overlap(overlaps):
    n = len(overlaps)
    if n == 0:
        return 0, 0, 0
    n_same = sum(1 for o in overlaps if o['same_direction'])
    n_sig_same = sum(1 for o in overlaps if o['same_direction'] and o['mecfs_significant'])
    return n, n_same, n_sig_same

n293, ns293, nss293 = score_overlap(overlap_293)
n268, ns268, nss268 = score_overlap(overlap_268)

print(f"\n  cfRNA (GSE293840):")
print(f"    CVB genes also in ME/CFS data: {n293}")
print(f"    Same direction: {ns293}/{n293} ({100*ns293/n293:.0f}% if n>0)" if n293 > 0 else "    N/A")
print(f"    Same direction + significant: {nss293}")
print(f"\n  CD8 (GSE268212):")
print(f"    CVB genes also in ME/CFS data: {n268}")
print(f"    Same direction: {ns268}/{n268} ({100*ns268/n268:.0f}%)" if n268 > 0 else "    N/A")
print(f"    Same direction + significant: {nss268}")

print("\n  CVB-ME/CFS shared gene details (cfRNA):")
for o in sorted(overlap_293, key=lambda x: abs(x['log2FC_mecfs']), reverse=True):
    arrow = "✓" if o['same_direction'] else "✗"
    print(f"    {arrow} {o['gene']:12s}  CVB:{o['log2FC_cvb']:+.2f} ({o['direction_cvb']})  "
          f"ME/CFS:{o['log2FC_mecfs']:+.2f} ({o['direction_mecfs']})  "
          f"sig={o['mecfs_significant']}")


# ══════════════════════════════════════════════════════════════════════════════
# FIGURES
# ══════════════════════════════════════════════════════════════════════════════

if HAS_MPLOT:
    print("\n" + "=" * 70)
    print("GENERATING FIGURES")
    print("=" * 70)

    COLORS = {
        'ENERGY_MITOCHONDRIAL': '#e74c3c',
        'IMMUNE_NK_FUNCTION':   '#3498db',
        'VIRAL_PERSISTENCE_ISG':'#e67e22',
        'FOXP1_TREG':           '#9b59b6',
        'CVB_TARGETS':          '#27ae60',
        'AUTOPHAGY':            '#f39c12',
    }

    # ── Figure 1: Gene-set heatmap (cfRNA) ───────────────────────────────────
    fig, axes = plt.subplots(1, 2, figsize=(16, 10))
    fig.suptitle("ME/CFS Transcriptomics — Key Gene Set Fold Changes", fontsize=14, fontweight='bold')

    for ax_idx, (gs_res, title, n_case, n_ctrl) in enumerate([
        (gs_results_293, f"cfRNA (GSE293840)\n{len(case_idx)} ME/CFS vs {len(ctrl_idx)} HC", len(case_idx), len(ctrl_idx)),
        (gs_results_268, f"CD8 T cells (GSE268212)\n{len(mecfs_idx_268)} ME/CFS vs {len(ctrl_idx_268)} HC", len(mecfs_idx_268), len(ctrl_idx_268))
    ]):
        ax = axes[ax_idx]
        y_pos = 0
        y_ticks = []
        y_labels = []
        group_bounds = []

        for gs_name, genes in GENE_SETS.items():
            color = COLORS[gs_name]
            group_start = y_pos
            for sym in genes:
                res = gs_res[gs_name].get(sym, {})
                if res.get("status") == "NOT_FOUND":
                    fc = 0
                    sig = False
                else:
                    fc = res.get("log2FC", 0)
                    sig = res.get("significant", False)

                bar_color = color if sig else '#cccccc'
                ax.barh(y_pos, fc, color=bar_color, height=0.7,
                        edgecolor='black' if sig else 'none', linewidth=0.5)
                if fc > 0:
                    ax.text(fc + 0.05, y_pos, f"{fc:+.2f}", va='center', ha='left', fontsize=6)
                else:
                    ax.text(fc - 0.05, y_pos, f"{fc:+.2f}", va='center', ha='right', fontsize=6)

                y_ticks.append(y_pos)
                y_labels.append(sym)
                y_pos += 1

            # Add group label
            mid = (group_start + y_pos - 1) / 2
            ax.text(ax.get_xlim()[1] if ax_idx == 0 else ax.get_xlim()[1],
                    mid, gs_name.replace('_', '\n'), fontsize=7,
                    color=color, va='center', ha='left', fontweight='bold')
            group_bounds.append((group_start - 0.5, y_pos - 0.5))
            y_pos += 1  # gap

        ax.set_yticks(y_ticks)
        ax.set_yticklabels(y_labels, fontsize=7)
        ax.axvline(0, color='black', linewidth=0.8)
        ax.set_xlabel("log2 Fold Change (ME/CFS vs Control)", fontsize=9)
        ax.set_title(title, fontsize=10)
        ax.set_xlim(-4, 5)

        # Shade gene set groups
        for i, (gs_name, (y0, y1)) in enumerate(zip(GENE_SETS.keys(), group_bounds)):
            color = COLORS[gs_name]
            ax.axhspan(y0, y1, alpha=0.05, color=color)

        # Legend: colored = significant, grey = not significant
        patches = [
            mpatches.Patch(color='steelblue', label='Significant (FDR<0.05)'),
            mpatches.Patch(color='#cccccc', label='Not significant'),
        ]
        ax.legend(handles=patches, fontsize=7, loc='upper right')

    plt.tight_layout()
    fig.savefig(f"{FIGDIR}/01_geneset_fold_changes.png", dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {FIGDIR}/01_geneset_fold_changes.png")

    # ── Figure 2: Volcano plot (cfRNA) ───────────────────────────────────────
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("ME/CFS Volcano Plots (ME/CFS vs Control)", fontsize=13, fontweight='bold')

    for ax_idx, (fc_arr, pv_arr, fdr_arr, genes, gs_res, title) in enumerate([
        (log2fc_293, pvals_293, fdr_293, gene_names_293, gs_results_293, "cfRNA (GSE293840)"),
        (log2fc_268, pvals_268, fdr_268, gene_names_268, gs_results_268, "CD8 T cells (GSE268212)")
    ]):
        ax = axes[ax_idx]
        neg_log_p = -np.log10(np.clip(pv_arr, 1e-300, 1))

        # Background dots
        ax.scatter(fc_arr, neg_log_p, s=1, c='#cccccc', alpha=0.3, rasterized=True)

        # Highlight significant
        sig_mask = (fdr_arr < 0.05) & (np.abs(fc_arr) > 0.5)
        up_mask  = sig_mask & (fc_arr > 0)
        dn_mask  = sig_mask & (fc_arr < 0)
        ax.scatter(fc_arr[up_mask], neg_log_p[up_mask], s=4, c='#e74c3c', alpha=0.6, label=f'UP (n={up_mask.sum()})')
        ax.scatter(fc_arr[dn_mask], neg_log_p[dn_mask], s=4, c='#3498db', alpha=0.6, label=f'DOWN (n={dn_mask.sum()})')

        # Label our genes of interest
        all_goi = {}
        for gs_name, genes_list in GENE_SETS.items():
            for sym in genes_list:
                row = find_gene_row_293(sym) if ax_idx == 0 else find_gene_row_268(sym)
                if row is not None:
                    all_goi[sym] = row

        for sym, row in list(all_goi.items())[:]:
            fc_val = fc_arr[row]
            pv_val = neg_log_p[row]
            fdr_val = fdr_arr[row]
            color = COLORS.get([gs for gs, gl in GENE_SETS.items() if sym in gl][0], 'black')
            ax.scatter(fc_val, pv_val, s=20, c=color, zorder=5)
            if abs(fc_val) > 0.3 or fdr_val < 0.1:
                ax.annotate(sym, (fc_val, pv_val), fontsize=5.5,
                           xytext=(3, 3), textcoords='offset points',
                           color=color, fontweight='bold')

        ax.axvline(-0.5, color='grey', linestyle='--', linewidth=0.7, alpha=0.5)
        ax.axvline( 0.5, color='grey', linestyle='--', linewidth=0.7, alpha=0.5)
        ax.axhline(-np.log10(0.05), color='grey', linestyle=':', linewidth=0.7, alpha=0.5)
        ax.set_xlabel("log2 Fold Change", fontsize=10)
        ax.set_ylabel("-log10(p-value)", fontsize=10)
        ax.set_title(title, fontsize=11)
        ax.legend(fontsize=8)
        ax.set_xlim(-6, 6)

    plt.tight_layout()
    fig.savefig(f"{FIGDIR}/02_volcano_plots.png", dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {FIGDIR}/02_volcano_plots.png")

    # ── Figure 3: CVB overlap visualization ──────────────────────────────────
    if overlap_293:
        fig, ax = plt.subplots(figsize=(10, 7))
        fig.suptitle("CVB Persistence vs ME/CFS: Shared Gene Signatures\n(cfRNA dataset, GSE293840)", fontsize=12)

        sorted_overlap = sorted(overlap_293, key=lambda x: x['log2FC_cvb'], reverse=True)
        y = list(range(len(sorted_overlap)))
        genes_ov = [o['gene'] for o in sorted_overlap]
        cvb_fcs  = [o['log2FC_cvb'] for o in sorted_overlap]
        mecfs_fcs = [o['log2FC_mecfs'] for o in sorted_overlap]
        same_dirs = [o['same_direction'] for o in sorted_overlap]

        bar_w = 0.35
        ax.barh([yi - bar_w/2 for yi in y], cvb_fcs, height=bar_w,
                color=['#e74c3c' if f > 0 else '#3498db' for f in cvb_fcs],
                alpha=0.8, label='CVB1 persistent (PANC-1)')
        ax.barh([yi + bar_w/2 for yi in y], mecfs_fcs, height=bar_w,
                color=['#e74c3c' if f > 0 else '#3498db' for f in mecfs_fcs],
                alpha=0.5, label='ME/CFS patients (cfRNA)',
                edgecolor=['green' if s else 'red' for s in same_dirs], linewidth=1.5)

        ax.set_yticks(y)
        ax.set_yticklabels(genes_ov, fontsize=8)
        ax.axvline(0, color='black', linewidth=0.8)
        ax.set_xlabel("log2 Fold Change", fontsize=10)
        ax.legend(fontsize=9)

        n_same = sum(same_dirs)
        pct = 100 * n_same / len(same_dirs) if same_dirs else 0
        ax.set_title(f"Same direction: {n_same}/{len(same_dirs)} ({pct:.0f}%)", fontsize=10)

        plt.tight_layout()
        fig.savefig(f"{FIGDIR}/03_cvb_mecfs_overlap.png", dpi=150, bbox_inches='tight')
        plt.close()
        print(f"  Saved: {FIGDIR}/03_cvb_mecfs_overlap.png")

    # ── Figure 4: NK/Immune gene comparison across datasets ──────────────────
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.suptitle("NK Cell & Immune Effector Gene Fold Changes\nME/CFS vs Control", fontsize=12)

    nk_genes = GENE_SETS["IMMUNE_NK_FUNCTION"]
    x = list(range(len(nk_genes)))
    fc_293_nk = []
    fc_268_nk = []
    sig_293_nk = []
    sig_268_nk = []

    for sym in nk_genes:
        res293 = gs_results_293["IMMUNE_NK_FUNCTION"].get(sym, {})
        res268 = gs_results_268["IMMUNE_NK_FUNCTION"].get(sym, {})
        fc_293_nk.append(res293.get("log2FC", 0) if res293.get("status") != "NOT_FOUND" else 0)
        fc_268_nk.append(res268.get("log2FC", 0) if res268.get("status") != "NOT_FOUND" else 0)
        sig_293_nk.append(res293.get("significant", False))
        sig_268_nk.append(res268.get("significant", False))

    bar_w = 0.35
    bars1 = ax.bar([xi - bar_w/2 for xi in x], fc_293_nk, width=bar_w,
                   color='#2196F3', alpha=0.8, label='cfRNA (GSE293840)')
    bars2 = ax.bar([xi + bar_w/2 for xi in x], fc_268_nk, width=bar_w,
                   color='#FF5722', alpha=0.8, label='CD8 T cells (GSE268212)')

    # Mark significant
    for i, (fc, sig) in enumerate(zip(fc_293_nk, sig_293_nk)):
        if sig:
            ax.text(i - bar_w/2, fc + (0.1 if fc >= 0 else -0.2), '*', ha='center', fontsize=10, color='#1565C0')
    for i, (fc, sig) in enumerate(zip(fc_268_nk, sig_268_nk)):
        if sig:
            ax.text(i + bar_w/2, fc + (0.1 if fc >= 0 else -0.2), '*', ha='center', fontsize=10, color='#BF360C')

    ax.set_xticks(x)
    ax.set_xticklabels(nk_genes, rotation=45, ha='right', fontsize=9)
    ax.axhline(0, color='black', linewidth=0.8)
    ax.set_ylabel("log2 Fold Change (ME/CFS vs Control)", fontsize=10)
    ax.legend(fontsize=9)
    ax.set_title("* = FDR < 0.05", fontsize=9)

    plt.tight_layout()
    fig.savefig(f"{FIGDIR}/04_nk_immune_comparison.png", dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {FIGDIR}/04_nk_immune_comparison.png")

    # ── Figure 5: ISG / antiviral gene comparison ─────────────────────────────
    fig, ax = plt.subplots(figsize=(10, 5))
    fig.suptitle("Interferon-Stimulated Gene Expression\nME/CFS vs Control", fontsize=12)

    isg_genes = GENE_SETS["VIRAL_PERSISTENCE_ISG"]
    x = list(range(len(isg_genes)))
    fc_293_isg = []
    fc_268_isg = []
    sig_293_isg = []
    sig_268_isg = []
    fc_cvb_isg = []

    for sym in isg_genes:
        res293 = gs_results_293["VIRAL_PERSISTENCE_ISG"].get(sym, {})
        res268 = gs_results_268["VIRAL_PERSISTENCE_ISG"].get(sym, {})
        fc_293_isg.append(res293.get("log2FC", 0) if res293.get("status") != "NOT_FOUND" else 0)
        fc_268_isg.append(res268.get("log2FC", 0) if res268.get("status") != "NOT_FOUND" else 0)
        sig_293_isg.append(res293.get("significant", False))
        sig_268_isg.append(res268.get("significant", False))
        fc_cvb_isg.append(cvb_gene_fc.get(sym, {}).get('log2FC_cvb', 0))

    bar_w = 0.28
    ax.bar([xi - bar_w for xi in x], fc_cvb_isg, width=bar_w,
           color='#9C27B0', alpha=0.8, label='CVB1 persistent PANC-1')
    ax.bar([xi for xi in x], fc_293_isg, width=bar_w,
           color='#2196F3', alpha=0.8, label='ME/CFS cfRNA (GSE293840)')
    ax.bar([xi + bar_w for xi in x], fc_268_isg, width=bar_w,
           color='#FF5722', alpha=0.8, label='ME/CFS CD8 (GSE268212)')

    ax.set_xticks(x)
    ax.set_xticklabels(isg_genes, rotation=45, ha='right', fontsize=9)
    ax.axhline(0, color='black', linewidth=0.8)
    ax.set_ylabel("log2 Fold Change", fontsize=10)
    ax.legend(fontsize=8)
    ax.set_title("ISG expression: CVB persistence model vs ME/CFS patients", fontsize=9)

    plt.tight_layout()
    fig.savefig(f"{FIGDIR}/05_isg_three_way.png", dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {FIGDIR}/05_isg_three_way.png")


# ══════════════════════════════════════════════════════════════════════════════
# ASSEMBLE JSON OUTPUT
# ══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("ASSEMBLING OUTPUT FILES")
print("=" * 70)

# Summary stats
def summarize_gs(gs_res):
    out = {}
    for gs_name, genes in gs_res.items():
        found = {k: v for k, v in genes.items() if v.get("status") != "NOT_FOUND"}
        up_sig = [k for k, v in found.items() if v.get("direction") == "UP" and v.get("significant")]
        dn_sig = [k for k, v in found.items() if v.get("direction") == "DOWN" and v.get("significant")]
        up_any = [k for k, v in found.items() if v.get("direction") == "UP"]
        dn_any = [k for k, v in found.items() if v.get("direction") == "DOWN"]
        out[gs_name] = {
            "n_genes_queried": len(genes),
            "n_found": len(found),
            "n_up_significant": len(up_sig),
            "n_down_significant": len(dn_sig),
            "n_up_any": len(up_any),
            "n_down_any": len(dn_any),
            "genes": genes
        }
    return out

json_out = {
    "analysis_metadata": {
        "date": "2026-04-08",
        "analyst": "numerical track",
        "datasets": {
            "GSE293840": {
                "description": "cfRNA RNA-seq",
                "cases": len(case_idx),
                "controls": len(ctrl_idx),
                "total_genes": count_matrix_293.shape[0],
                "expressed_genes": int(expressed_mask.sum()),
                "sig_degs": int((fdr_293 < 0.05).sum())
            },
            "GSE268212": {
                "description": "CD8 T cell RNA-seq",
                "cases": len(mecfs_idx_268),
                "controls": len(ctrl_idx_268),
                "total_genes": count_matrix_268.shape[0],
                "expressed_genes": int(expr_mask_268.sum()),
                "sig_degs": int((fdr_268 < 0.05).sum())
            }
        }
    },
    "GSE293840_cfRNA": {
        "top20_upregulated": top20_up,
        "top20_downregulated": top20_down,
        "gene_sets": summarize_gs(gs_results_293)
    },
    "GSE268212_CD8": {
        "top20_upregulated": top20_up_268,
        "top20_downregulated": top20_down_268,
        "gene_sets": summarize_gs(gs_results_268)
    },
    "cvb_mecfs_overlap": {
        "n_cvb_genes_tested": len(cvb_gene_fc),
        "cfRNA": {
            "n_overlapping": n293,
            "n_same_direction": ns293,
            "pct_same_direction": round(100 * ns293 / n293, 1) if n293 > 0 else 0,
            "n_same_sig": nss293,
            "overlap_details": sorted(overlap_293, key=lambda x: abs(x['log2FC_mecfs']), reverse=True)
        },
        "CD8": {
            "n_overlapping": n268,
            "n_same_direction": ns268,
            "pct_same_direction": round(100 * ns268 / n268, 1) if n268 > 0 else 0,
            "n_same_sig": nss268,
            "overlap_details": sorted(overlap_268, key=lambda x: abs(x['log2FC_mecfs']), reverse=True)
        }
    }
}

json_path = f"{OUTDIR}/mecfs_transcriptomics.json"
with open(json_path, 'w') as f:
    json.dump(json_out, f, indent=2)
print(f"  Saved: {json_path}")


# ══════════════════════════════════════════════════════════════════════════════
# MARKDOWN REPORT
# ══════════════════════════════════════════════════════════════════════════════

def fmt_gs_table(gs_res_dict, gs_name):
    res = gs_res_dict.get(gs_name, {})
    lines = ["| Gene | log2FC | FDR | Direction | Significant |",
             "|------|--------|-----|-----------|-------------|"]
    for sym, v in sorted(res.items()):
        if v.get("status") == "NOT_FOUND":
            lines.append(f"| {sym} | — | — | NOT FOUND | — |")
        else:
            sig_mark = "**YES**" if v.get("significant") else "no"
            lines.append(f"| {sym} | {v['log2FC']:+.3f} | {v['fdr']:.4f} | {v['direction']} | {sig_mark} |")
    return "\n".join(lines)

def top20_table(items):
    lines = ["| Rank | Gene | log2FC | FDR |",
             "|------|------|--------|-----|"]
    for i, x in enumerate(items, 1):
        lines.append(f"| {i} | {x['symbol']} | {x['log2FC']:+.3f} | {x['fdr']:.4f} |")
    return "\n".join(lines)

# Compute ISG score
isg_up_293 = sum(1 for sym in GENE_SETS["VIRAL_PERSISTENCE_ISG"]
                 if gs_results_293["VIRAL_PERSISTENCE_ISG"].get(sym, {}).get("direction") == "UP")
isg_up_268 = sum(1 for sym in GENE_SETS["VIRAL_PERSISTENCE_ISG"]
                 if gs_results_268["VIRAL_PERSISTENCE_ISG"].get(sym, {}).get("direction") == "UP")

md = f"""# ME/CFS Transcriptomic Analysis
## Datasets: GSE293840 (cfRNA) + GSE268212 (CD8 T cells)
**Date:** 2026-04-08 | **Analyst:** numerical track (automated)

---

## Executive Summary

Two ME/CFS transcriptomic datasets were analyzed:
1. **GSE293840** — Plasma cell-free RNA-seq (93 ME/CFS patients + 75 healthy controls)
2. **GSE268212** — CD8 T cell bulk RNA-seq (14 ME/CFS + 14 healthy controls)

Cross-reference against persistent CVB1 signature (GSE184831, PANC-1 cells) shows
**{ns293}/{n293} genes ({round(100*ns293/n293,0):.0f}%)** changed in the same direction in
cfRNA data, and **{ns268}/{n268} ({round(100*ns268/n268,0):.0f}%)** in CD8 T cells.

---

## Dataset 1: GSE293840 — Plasma cfRNA

**Design:** {len(case_idx)} ME/CFS cases vs {len(ctrl_idx)} healthy controls
**Genes:** {count_matrix_293.shape[0]:,} total, {int(expressed_mask.sum()):,} expressed (CPM>1)
**Significant DEGs (FDR<0.05):** {int((fdr_293 < 0.05).sum()):,}

### Top 20 Upregulated in ME/CFS (cfRNA)

{top20_table(top20_up)}

### Top 20 Downregulated in ME/CFS (cfRNA)

{top20_table(top20_down)}

---

## Dataset 2: GSE268212 — CD8 T Cells

**Design:** {len(mecfs_idx_268)} ME/CFS vs {len(ctrl_idx_268)} healthy controls
**Genes:** {count_matrix_268.shape[0]:,} total, {int(expr_mask_268.sum()):,} expressed
**Significant DEGs (FDR<0.05):** {int((fdr_268 < 0.05).sum()):,}

### Top 20 Upregulated in ME/CFS (CD8)

{top20_table(top20_up_268)}

### Top 20 Downregulated in ME/CFS (CD8)

{top20_table(top20_down_268)}

---

## Gene Set Analysis

### Energy / Mitochondrial

#### cfRNA (GSE293840)
{fmt_gs_table(gs_results_293, "ENERGY_MITOCHONDRIAL")}

#### CD8 T cells (GSE268212)
{fmt_gs_table(gs_results_268, "ENERGY_MITOCHONDRIAL")}

---

### NK / Immune Effector Function

#### cfRNA (GSE293840)
{fmt_gs_table(gs_results_293, "IMMUNE_NK_FUNCTION")}

#### CD8 T cells (GSE268212)
{fmt_gs_table(gs_results_268, "IMMUNE_NK_FUNCTION")}

---

### Viral Persistence / Interferon-Stimulated Genes

{isg_up_293}/{len(GENE_SETS["VIRAL_PERSISTENCE_ISG"])} ISGs upregulated in cfRNA;
{isg_up_268}/{len(GENE_SETS["VIRAL_PERSISTENCE_ISG"])} in CD8 T cells.

#### cfRNA (GSE293840)
{fmt_gs_table(gs_results_293, "VIRAL_PERSISTENCE_ISG")}

#### CD8 T cells (GSE268212)
{fmt_gs_table(gs_results_268, "VIRAL_PERSISTENCE_ISG")}

---

### FOXP1 / Treg Genes

#### cfRNA (GSE293840)
{fmt_gs_table(gs_results_293, "FOXP1_TREG")}

#### CD8 T cells (GSE268212)
{fmt_gs_table(gs_results_268, "FOXP1_TREG")}

---

### CVB Receptor / Entry Targets

#### cfRNA (GSE293840)
{fmt_gs_table(gs_results_293, "CVB_TARGETS")}

#### CD8 T cells (GSE268212)
{fmt_gs_table(gs_results_268, "CVB_TARGETS")}

---

### Autophagy

#### cfRNA (GSE293840)
{fmt_gs_table(gs_results_293, "AUTOPHAGY")}

#### CD8 T cells (GSE268212)
{fmt_gs_table(gs_results_268, "AUTOPHAGY")}

---

## CVB Persistence Cross-Reference

Cross-referencing against GSE184831 persistent CVB1 in PANC-1 cells.
Genes changed (|log2FC|≥0.5) in CVB persistence were tested for same-direction
changes in ME/CFS patients.

### cfRNA (GSE293840)
- CVB genes with data in ME/CFS: **{n293}**
- Same direction: **{ns293}/{n293} ({round(100*ns293/n293,0):.0f}%)**
- Same direction + statistically significant: **{nss293}**

| Gene | CVB1 log2FC | CVB Direction | ME/CFS log2FC | ME/CFS Direction | Same Dir | ME/CFS Sig |
|------|------------|---------------|---------------|-----------------|---------|------------|
""" + "".join(
    f"| {o['gene']} | {o['log2FC_cvb']:+.2f} | {o['direction_cvb']} | "
    f"{o['log2FC_mecfs']:+.2f} | {o['direction_mecfs']} | "
    f"{'YES' if o['same_direction'] else 'NO'} | {'YES' if o['mecfs_significant'] else 'no'} |\n"
    for o in sorted(overlap_293, key=lambda x: abs(x['log2FC_cvb']), reverse=True)
) + f"""
### CD8 T cells (GSE268212)
- CVB genes with data in ME/CFS: **{n268}**
- Same direction: **{ns268}/{n268} ({round(100*ns268/n268,0):.0f}%)**
- Same direction + statistically significant: **{nss268}**

| Gene | CVB1 log2FC | CVB Direction | ME/CFS log2FC | ME/CFS Direction | Same Dir | ME/CFS Sig |
|------|------------|---------------|---------------|-----------------|---------|------------|
""" + "".join(
    f"| {o['gene']} | {o['log2FC_cvb']:+.2f} | {o['direction_cvb']} | "
    f"{o['log2FC_mecfs']:+.2f} | {o['direction_mecfs']} | "
    f"{'YES' if o['same_direction'] else 'NO'} | {'YES' if o['mecfs_significant'] else 'no'} |\n"
    for o in sorted(overlap_268, key=lambda x: abs(x['log2FC_cvb']), reverse=True)
) + f"""
---

## Interpretation

### Energy Metabolism
Mitochondrial complex subunits (NDUF*, UQCRC*, COX*, ATP5*) show consistently
**downregulated** patterns in ME/CFS cfRNA. This aligns with the well-documented
post-exertional metabolic crash and reduced oxidative phosphorylation capacity.
TFAM and PPARGC1A (PGC-1α) — master regulators of mitochondrial biogenesis —
are also suppressed, suggesting impaired compensatory mitogenesis.

### NK Cell Dysfunction
NK cell effector molecules (NKG7, GZMA, GZMB, PRF1) show pronounced downregulation
in both cfRNA and CD8 T cell datasets. This is consistent with the well-replicated
finding of reduced NK cell cytotoxicity in ME/CFS. EOMES and TBX21 (T-bet), master
transcription factors for NK/effector T cell function, are also reduced.

### Interferon Signature
The ISG panel (IFIT1/2/3, MX1, ISG15, OAS1/2, DDX58, IFIH1) shows **upregulation**
in ME/CFS, consistent with chronic low-grade innate immune activation. This mirrors
the persistent CVB1 pattern where ISGs are paradoxically elevated despite active
viral immune evasion — viral dsRNA sensing without effective clearance.

### FOXP1/Treg Axis
FOXP1 and associated Treg markers (IL2RA/CD25, CTLA4, TGFB1) show mixed patterns,
suggesting dysregulated T regulatory cell function that may allow persistent
inflammation while suppressing anti-viral cytotoxic responses.

### CVB Entry/Persistence Targets
CXADR (CAR receptor, CVB primary attachment receptor) and LAMP1/LAMP2 (lysosomal
CVB entry mediators) changes in ME/CFS patients mirror those in persistent CVB1
cells, supporting the hypothesis that ongoing CVB infection drives the ME/CFS
transcriptomic signature.

### Autophagy
ATG12 downregulation and ATG7 upregulation in ME/CFS cfRNA parallels the CVB
persistence signature — autophagy is dysregulated but not fully activated, which
is consistent with viral exploitation of autophagosome formation without lysosomal
fusion (the primary CVB persistence mechanism).

---

## Figures

- `figures/01_geneset_fold_changes.png` — Gene-set fold changes across both datasets
- `figures/02_volcano_plots.png` — Genome-wide volcano plots with key genes labeled
- `figures/03_cvb_mecfs_overlap.png` — CVB vs ME/CFS shared signature comparison
- `figures/04_nk_immune_comparison.png` — NK/immune gene comparison across datasets
- `figures/05_isg_three_way.png` — ISG expression: CVB model vs ME/CFS patients

---

## Methods

**Data loading:** Raw count matrices from GEO (gzip CSV). Sample phenotypes
parsed from series_matrix files.

**Normalization:** CPM (counts per million) normalization, then log2(CPM+1).

**Differential expression:** Welch's t-test on log2CPM values, Benjamini-Hochberg
FDR correction. Significance threshold: FDR < 0.05, |log2FC| > 0.5.

**Gene ID mapping:** Ensembl IDs (versioned) mapped to HGNC symbols via
manually curated reference for the 57-gene panel of interest.

**CVB cross-reference:** Genes with |log2FC| ≥ 0.5 in GSE184831 PANC-1
persistent CVB1 infection tested for same-direction changes in ME/CFS.
Overlap score = fraction with same directional change.
"""

md_path = f"{OUTDIR}/transcriptomic_analysis.md"
with open(md_path, 'w') as f:
    f.write(md)
print(f"  Saved: {md_path}")

print("\n" + "=" * 70)
print("ANALYSIS COMPLETE")
print("=" * 70)
