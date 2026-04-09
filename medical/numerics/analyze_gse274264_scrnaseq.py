#!/usr/bin/env python3
"""
GSE274264 — scRNA-seq of Primary Human Pancreatic Islets with CVB3

Study design:
- Multiple patients (patient1, patient2, ...) x conditions (control, CVB3, PolyIC)
- Timepoints: 24hr and 48hr post-infection
- Data format: 10x Genomics barcodes/features/matrix (MTX format)
- Critical advantage over GSE184831: PRIMARY HUMAN ISLETS (not PANC-1 cell line)

Analysis goals:
1. Confirm FOXP1 suppression in primary islets (harder to dismiss than cell line)
2. Confirm LAMP2 suppression in primary islets
3. Identify cell-type-specific responses (scRNA-seq allows beta vs alpha vs delta)
4. Find DMD expression across cell types
5. Look for CXADR (CVB receptor) dynamics
6. Compare 24hr vs 48hr infection — acute vs early persistence

This script uses scanpy for single-cell analysis. Output: results/gse274264_analysis.json
"""

import os
import sys
import json
import warnings
warnings.filterwarnings('ignore')

try:
    import numpy as np
    import scanpy as sc
    import pandas as pd
    from scipy.io import mmread
    from scipy.sparse import csr_matrix
    import gzip
    HAS_SCANPY = True
except ImportError:
    HAS_SCANPY = False
    print("scanpy/scipy not available — install with: pip install scanpy scipy pandas")

DATA_DIR = os.path.join(os.path.dirname(__file__), "transcriptomics", "GSE274264")
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "..", "results")

# Campaign genes of interest (from patterns 013-017)
CAMPAIGN_GENES = {
    # TD persistence evidence
    "viral_sensors": ["DDX58", "IFIH1", "MAVS", "TLR3"],
    "ifn_signaling": ["STAT1", "STAT2", "STAT4", "IRF1", "IRF3", "IFNB1",
                      "IFIT1", "IFIT2", "IFIT3", "MX1", "RSAD2"],
    # Autophagy (LAMP2 block mechanism)
    "autophagy": ["ATG7", "ATG12", "AMBRA1", "LAMP1", "LAMP2", "TFEB",
                  "BECN1", "ULK1", "MAP1LC3A", "MAP1LC3B", "SQSTM1"],
    # FOXP1 — the key new finding
    "treg_foxp1": ["FOXP1", "FOXP3", "IL2RA", "CTLA4", "IKZF2"],
    # 2A protease target
    "dystrophin": ["DMD"],
    # CVB receptors
    "cvb_receptors": ["CXADR", "CD55", "DAF"],
    # OSBP/PI4K pathway (fluoxetine target)
    "osbp_pathway": ["OSBP", "PI4KB", "PI4KA", "SEC14L2"],
    # NF-kB / inflammation
    "inflammation": ["NFKB1", "NFKB2", "RELA", "TNF", "IL6", "IL1B",
                     "NLRP3", "CASP1", "IL18"],
    # Mitochondrial (MT-encoded — from ME/CFS validation)
    "mitochondrial": ["MT-ND1", "MT-ND2", "MT-ND3", "MT-ND4", "MT-ND5",
                      "MT-ND6", "MT-CO2", "MT-CO1"],
    # Beta cell identity
    "beta_cell": ["INS", "PDX1", "NKX6-1", "MAFA", "GCG", "SST", "PPY"],
    # ER stress
    "er_stress": ["HSPA5", "DDIT3", "ATF6", "HERPUD1", "DNAJB9", "XBP1"],
}

ALL_GENES = [g for genes in CAMPAIGN_GENES.values() for g in genes]
ALL_GENES = list(dict.fromkeys(ALL_GENES))  # deduplicate preserving order


def load_sample(sample_id, data_dir):
    """Load a 10x Genomics MTX sample into an AnnData object."""
    sample_dir = data_dir  # all samples in same dir
    # Find files for this sample
    prefix = os.path.join(data_dir, f"{sample_id}_")
    barcodes_f = prefix + "barcodes.tsv.gz"
    features_f = prefix + "features.tsv.gz"
    matrix_f = prefix + "matrix.mtx.gz"

    if not os.path.exists(matrix_f):
        return None

    # Read matrix
    with gzip.open(matrix_f, 'rb') as f:
        mat = mmread(f)

    # Read barcodes
    with gzip.open(barcodes_f, 'rt') as f:
        barcodes = [line.strip() for line in f]

    # Read features
    with gzip.open(features_f, 'rt') as f:
        features = [line.strip().split('\t') for line in f]
    gene_ids = [r[0] for r in features]
    gene_names = [r[1] if len(r) > 1 else r[0] for r in features]

    import anndata
    adata = anndata.AnnData(
        X=csr_matrix(mat.T),  # cells x genes
        obs=pd.DataFrame(index=barcodes),
        var=pd.DataFrame({'gene_ids': gene_ids, 'gene_names': gene_names},
                         index=gene_names)
    )
    return adata


def analyze_condition_comparison(adata, ctrl_label, cvb_label):
    """Compare CVB3 vs control: mean expression of campaign genes."""
    results = {}
    for group_name, genes in CAMPAIGN_GENES.items():
        group_results = {}
        for gene in genes:
            if gene not in adata.var_names:
                continue
            ctrl_mask = adata.obs['condition'] == ctrl_label
            cvb_mask = adata.obs['condition'] == cvb_label
            if ctrl_mask.sum() == 0 or cvb_mask.sum() == 0:
                continue
            ctrl_expr = np.array(adata[ctrl_mask, gene].X.todense()).flatten()
            cvb_expr = np.array(adata[cvb_mask, gene].X.todense()).flatten()
            ctrl_mean = float(np.mean(ctrl_expr))
            cvb_mean = float(np.mean(cvb_expr))
            if ctrl_mean > 0.01:
                log2fc = float(np.log2((cvb_mean + 0.01) / (ctrl_mean + 0.01)))
            else:
                log2fc = 0.0
            group_results[gene] = {
                "ctrl_mean": ctrl_mean,
                "cvb_mean": cvb_mean,
                "log2FC": log2fc,
                "n_ctrl_cells": int(ctrl_mask.sum()),
                "n_cvb_cells": int(cvb_mask.sum()),
            }
        results[group_name] = group_results
    return results


def run_analysis():
    if not HAS_SCANPY:
        print("Required packages not available.")
        return

    try:
        import anndata
    except ImportError:
        print("anndata not available. Install: pip install anndata")
        return

    print("Loading GSE274264 primary human islet scRNA-seq data...")
    print("This is PRIMARY human tissue — highest quality data in the campaign.")

    # Enumerate all sample files
    samples = {}
    for fname in sorted(os.listdir(DATA_DIR)):
        if fname.endswith("_barcodes.tsv.gz"):
            sample_id = fname.replace("_barcodes.tsv.gz", "")
            # Parse sample metadata from ID
            # Format: GSMxxxxxxx_patientN_NNhr_condition
            parts = sample_id.split("_")
            if len(parts) >= 4:
                patient = parts[1]  # patientN
                timepoint = parts[2]  # NNhr
                condition = parts[3]  # control/CVB3/PolyIC
                samples[sample_id] = {
                    "patient": patient,
                    "timepoint": timepoint,
                    "condition": condition,
                    "path": os.path.join(DATA_DIR, sample_id)
                }

    print(f"Found {len(samples)} samples: {list(samples.keys())[:3]}...")

    # Load all samples
    adatas = []
    for sid, meta in samples.items():
        adata = load_sample(sid, DATA_DIR)
        if adata is None:
            continue
        adata.obs['sample'] = sid
        adata.obs['patient'] = meta['patient']
        adata.obs['timepoint'] = meta['timepoint']
        adata.obs['condition'] = meta['condition']
        adatas.append(adata)
        print(f"  Loaded {sid}: {adata.n_obs} cells x {adata.n_vars} genes")

    if not adatas:
        print("No samples loaded. Check data directory.")
        return

    # Concatenate
    adata_all = anndata.concat(adatas, label='sample_id',
                               keys=[a.obs['sample'].iloc[0] for a in adatas])
    print(f"\nCombined dataset: {adata_all.n_obs} cells x {adata_all.n_vars} genes")

    # Basic QC
    sc.pp.filter_cells(adata_all, min_genes=200)
    sc.pp.filter_genes(adata_all, min_cells=3)
    print(f"After QC: {adata_all.n_obs} cells x {adata_all.n_vars} genes")

    # Normalize
    sc.pp.normalize_total(adata_all, target_sum=1e4)
    sc.pp.log1p(adata_all)

    # Key analysis: CVB3 vs control at 24hr and 48hr
    results = {
        "study": "GSE274264",
        "tissue": "PRIMARY human pancreatic islets (multiple donors)",
        "key_advantage": "Primary tissue vs PANC-1 cell line (GSE184831) — higher clinical relevance",
        "n_cells_total": int(adata_all.n_obs),
        "n_genes": int(adata_all.n_vars),
        "conditions": list(adata_all.obs['condition'].unique()),
        "timepoints": list(adata_all.obs['timepoint'].unique()),
        "patients": list(adata_all.obs['patient'].unique()),
        "comparisons": {}
    }

    # Compare CVB3 vs control at each timepoint
    for tp in ['24hr', '48hr']:
        tp_data = adata_all[adata_all.obs['timepoint'] == tp]
        if tp_data.n_obs < 10:
            continue
        comparison = analyze_condition_comparison(tp_data, 'control', 'CVB3')
        results['comparisons'][f"CVB3_vs_ctrl_{tp}"] = comparison

        # Report key genes
        print(f"\n=== {tp}: CVB3 vs Control ===")
        key_genes = ['FOXP1', 'LAMP2', 'DMD', 'CXADR', 'NFKB1', 'ATG7',
                     'IFIT1', 'DDX58', 'NLRP3', 'MT-ND3', 'INS', 'PI4KB']
        for gene in key_genes:
            for group, group_results in comparison.items():
                if gene in group_results:
                    r = group_results[gene]
                    direction = "↑" if r['log2FC'] > 0.3 else ("↓" if r['log2FC'] < -0.3 else "~")
                    print(f"  {gene:15s} {direction} log2FC={r['log2FC']:+.2f} "
                          f"(ctrl={r['ctrl_mean']:.2f}, cvb={r['cvb_mean']:.2f})")
                    break

    # Cell type annotation (rough, based on marker genes)
    beta_markers = ['INS', 'PDX1', 'NKX6-1']
    alpha_markers = ['GCG', 'ARX']
    available_beta = [g for g in beta_markers if g in adata_all.var_names]
    if available_beta:
        results['cell_type_notes'] = f"Beta cell markers available: {available_beta}"
        print(f"\nBeta cell markers available: {available_beta}")
        # Simple score
        sc.tl.score_genes(adata_all, gene_list=available_beta,
                          score_name='beta_score')
        results['median_beta_score_by_condition'] = {
            cond: float(adata_all[adata_all.obs['condition'] == cond].obs['beta_score'].median())
            for cond in adata_all.obs['condition'].unique()
        }

    # Validate FOXP1 finding
    if 'FOXP1' in adata_all.var_names:
        foxp1_by_cond = {}
        for cond in adata_all.obs['condition'].unique():
            mask = adata_all.obs['condition'] == cond
            vals = np.array(adata_all[mask, 'FOXP1'].X.todense()).flatten()
            foxp1_by_cond[cond] = {
                'mean': float(np.mean(vals)),
                'pct_nonzero': float(np.mean(vals > 0) * 100),
                'n_cells': int(mask.sum())
            }
        results['foxp1_validation'] = foxp1_by_cond
        print(f"\nFOXP1 expression by condition:")
        for cond, stats in foxp1_by_cond.items():
            print(f"  {cond}: mean={stats['mean']:.3f}, % expressing={stats['pct_nonzero']:.1f}%")

    # Save results
    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_path = os.path.join(RESULTS_DIR, "gse274264_primary_islet_analysis.json")
    with open(out_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nResults saved to: {out_path}")
    print("\nKey questions answered by this analysis:")
    print("1. Is FOXP1 suppressed in PRIMARY human islets (not just PANC-1)?")
    print("   → If yes: FOXP1 mechanism is clinical-grade, not artifact of cell line")
    print("2. Is LAMP2 suppressed in primary islets?")
    print("   → If yes: trehalose protocol addition is validated in human tissue")
    print("3. Is DMD destroyed in primary islets?")
    print("   → If yes: all CVB patients with islet infection have cardiac risk")
    print("4. Do beta cells vs other cell types respond differently?")
    print("   → scRNA-seq allows cell-type-specific vulnerability mapping")
    return results


if __name__ == "__main__":
    run_analysis()
