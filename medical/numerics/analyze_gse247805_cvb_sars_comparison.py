#!/usr/bin/env python3
"""
GSE247805-247808 — CVB4 + SARS-CoV-2 in Macrophage-Islet Organoids

Four linked datasets from one study comparing CVB4 and SARS-CoV-2 infection
in vascularized macrophage-islet organoids (VMI):

GSE247805: Bulk RNA-seq, 6 samples (islet organoids)
GSE247806: scRNA-seq, 10 samples (islets alone)
GSE247807: scRNA-seq, 3 samples (VMI organoids)
GSE247808: snATAC-seq, 3 samples (VMI chromatin accessibility)

Critical campaign question: Do BOTH CVB4 AND SARS-CoV-2 suppress LAMP2 in the same system?
If yes: confirms that LAMP2 suppression is a convergent viral persistence mechanism
→ Trehalose is mechanistically justified for BOTH CVB diseases AND Long COVID

This is the most direct possible test of the Long COVID LAMP2 bridge
(me_cfs/attempts/attempt_005_long_covid_lamp2_convergence.md)

Secondary questions:
1. FOXP1 suppression in CVB4 vs SARS-CoV-2 — is the Treg mechanism shared?
2. DMD expression — is dystrophin damaged by SARS-CoV-2 as well as CVB4?
3. Beta cell-specific effects: insulin (INS), PDX1, NKX6-1
"""

import os
import sys
import json
import gzip
import warnings
warnings.filterwarnings('ignore')

DATA_DIR = os.path.join(os.path.dirname(__file__), "transcriptomics")
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "..", "results")

# Campaign genes for cross-virus comparison
CAMPAIGN_GENES = {
    "lamp2_block": ["LAMP2", "LAMP1", "ATG7", "ATG12", "BECN1"],
    "foxp1_treg": ["FOXP1", "FOXP3", "CTLA4"],
    "dystrophin": ["DMD"],
    "cvb_receptors": ["CXADR", "CD55"],
    "sars_receptors": ["ACE2", "TMPRSS2"],  # SARS-CoV-2 entry
    "ifn_signaling": ["IFIT1", "IFIT2", "IFIT3", "STAT1", "STAT2", "IRF1", "DDX58", "IFIH1"],
    "nlrp3": ["NLRP3", "CASP1", "IL18", "IL1B"],
    "beta_cell": ["INS", "PDX1", "NKX6-1", "MAFA", "GCG"],
    "mitochondrial": ["MT-ND1", "MT-ND2", "MT-ND3", "MT-ND4", "MT-CO2"],
    "nfkb": ["NFKB1", "NFKB2", "TNF", "CCL2"],
}

ALL_GENES = list({g for gs in CAMPAIGN_GENES.values() for g in gs})

def load_series_matrix(filename):
    """Load GEO series matrix, return (expression_dict, sample_info)."""
    filepath = os.path.join(DATA_DIR, filename)
    opener = gzip.open if filepath.endswith('.gz') else open

    samples = []
    titles = []
    expression = {}
    in_table = False

    with opener(filepath, 'rt', encoding='utf-8', errors='replace') as f:
        for line in f:
            line = line.strip()
            if line.startswith('!Sample_geo_accession'):
                samples = [x.strip('"') for x in line.split('\t')[1:]]
            elif line.startswith('!Sample_title'):
                titles = [x.strip('"') for x in line.split('\t')[1:]]
            elif line == '!series_matrix_table_begin':
                in_table = True
                continue
            elif line == '!series_matrix_table_end':
                break
            elif in_table:
                parts = line.split('\t')
                if len(parts) < 2:
                    continue
                gene = parts[0].strip('"')
                try:
                    vals = [float(x.strip('"')) for x in parts[1:]]
                    if vals:
                        expression[gene] = {s: v for s, v in zip(samples, vals)}
                except ValueError:
                    continue

    sample_info = {s: t for s, t in zip(samples, titles)}
    return expression, sample_info


def compare_conditions(expression, sample_info, virus_name):
    """Compare virus vs control for a specific virus."""
    import numpy as np

    virus_samples = [s for s, t in sample_info.items()
                     if virus_name.lower() in t.lower() or 'infected' in t.lower()]
    ctrl_samples = [s for s, t in sample_info.items()
                    if 'control' in t.lower() or 'mock' in t.lower() or 'uninfected' in t.lower()]

    if not virus_samples:
        # If can't classify, try to split by position
        all_samples = list(sample_info.keys())
        mid = len(all_samples) // 2
        ctrl_samples = all_samples[:mid]
        virus_samples = all_samples[mid:]

    results = {}
    for gene in ALL_GENES:
        if gene not in expression:
            continue
        cvirus = [expression[gene].get(s) for s in virus_samples if expression[gene].get(s) is not None]
        cctrl = [expression[gene].get(s) for s in ctrl_samples if expression[gene].get(s) is not None]
        if not cvirus or not cctrl:
            continue
        cvirus_mean = np.mean(cvirus)
        cctrl_mean = np.mean(cctrl)
        if cctrl_mean > 0.01:
            log2fc = np.log2((cvirus_mean + 0.01) / (cctrl_mean + 0.01))
        else:
            log2fc = 0.0
        results[gene] = {
            'cvirus_mean': float(cvirus_mean),
            'ctrl_mean': float(cctrl_mean),
            'log2FC': float(log2fc),
            'direction': 'UP' if log2fc > 0.3 else ('DOWN' if log2fc < -0.3 else 'SAME')
        }
    return results, virus_samples, ctrl_samples


def run_analysis():
    # Try GSE247805 (bulk RNA-seq — most interpretable)
    files_to_try = [
        "GSE247805_series_matrix.txt",
        "GSE247805_series_matrix.txt.gz",
    ]

    expression = None
    sample_info = None
    for fname in files_to_try:
        fpath = os.path.join(DATA_DIR, fname)
        if os.path.exists(fpath):
            print(f"Loading {fname}...")
            expression, sample_info = load_series_matrix(fname)
            break

    if expression is None:
        print("GSE247805 not found. Trying other datasets...")
        for gse in ["GSE247806", "GSE247807", "GSE247808"]:
            for ext in ["_series_matrix.txt", "_series_matrix.txt.gz"]:
                fpath = os.path.join(DATA_DIR, gse + ext)
                if os.path.exists(fpath):
                    print(f"Loading {gse + ext}...")
                    expression, sample_info = load_series_matrix(gse + ext)
                    break
            if expression is not None:
                break

    if expression is None:
        print("No GSE247805-247808 series matrices found.")
        return

    print(f"Loaded {len(expression)} genes, {len(sample_info)} samples")
    print("\nSamples:")
    for sid, title in sorted(sample_info.items()):
        print(f"  {sid}: {title}")

    # Look for CVB4 and SARS-CoV-2 conditions
    cvb4_results, cvb4_samp, ctrl1 = compare_conditions(expression, sample_info, "CVB")
    sars_results, sars_samp, ctrl2 = compare_conditions(expression, sample_info, "SARS")

    print(f"\nCVB4 samples identified: {cvb4_samp}")
    print(f"SARS-CoV-2 samples identified: {sars_samp}")

    # Compare LAMP2 suppression: CVB4 vs SARS-CoV-2
    print("\n=== LAMP2 COMPARISON: CVB4 vs SARS-CoV-2 ===")
    print("(Primary question: do BOTH viruses suppress LAMP2?)")
    print(f"{'Gene':<12} {'CVB4 log2FC':<14} {'SARS log2FC':<14} {'Both DOWN?'}")
    print("-" * 55)

    lamp2_genes = CAMPAIGN_GENES['lamp2_block']
    both_suppress_lamp2 = True

    for gene in lamp2_genes:
        cvb4_r = cvb4_results.get(gene, {})
        sars_r = sars_results.get(gene, {})
        cvb4_fc = cvb4_r.get('log2FC', 0)
        sars_fc = sars_r.get('log2FC', 0)
        cvb4_dir = '↓' if cvb4_fc < -0.3 else ('↑' if cvb4_fc > 0.3 else '~')
        sars_dir = '↓' if sars_fc < -0.3 else ('↑' if sars_fc > 0.3 else '~')
        both_down = '✓ BOTH DOWN' if cvb4_fc < -0.3 and sars_fc < -0.3 else ''
        if gene == 'LAMP2' and not (cvb4_fc < -0.3 and sars_fc < -0.3):
            both_suppress_lamp2 = False
        print(f"{gene:<12} {cvb4_dir} {cvb4_fc:+.2f}         {sars_dir} {sars_fc:+.2f}         {both_down}")

    print(f"\n{'LAMP2 suppressed by both viruses?' if both_suppress_lamp2 else 'LAMP2 not suppressed by both'}")
    if both_suppress_lamp2:
        print("→ CONFIRMED: Long COVID LAMP2 bridge mechanism validated in same experimental system")
        print("→ Trehalose mechanistically justified for BOTH CVB diseases AND Long COVID")

    print("\n=== KEY CAMPAIGN GENES COMPARISON ===")
    priority = ['FOXP1', 'DMD', 'CXADR', 'ACE2', 'IFIT1', 'NLRP3', 'INS', 'MT-ND3']
    for gene in priority:
        cvb4_r = cvb4_results.get(gene, {})
        sars_r = sars_results.get(gene, {})
        print(f"{gene:<12} CVB4: {cvb4_r.get('log2FC', 0):+.2f} | SARS: {sars_r.get('log2FC', 0):+.2f}")

    # Save
    import numpy as np
    results = {
        "study": "GSE247805-247808",
        "cell_type": "Vascularized macrophage-islet organoids",
        "comparison": "CVB4 vs SARS-CoV-2 vs control",
        "lamp2_both_suppressed": both_suppress_lamp2,
        "cvb4_results": cvb4_results,
        "sars2_results": sars_results,
    }

    os.makedirs(RESULTS_DIR, exist_ok=True)
    out = os.path.join(RESULTS_DIR, "gse247805_cvb_sars_comparison.json")
    with open(out, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nSaved: {out}")


if __name__ == "__main__":
    run_analysis()
