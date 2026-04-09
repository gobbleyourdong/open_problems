#!/usr/bin/env python3
"""
GSE57781 — CVB3 Infection of Human iPSC-Derived Cardiomyocytes

Study: "Human iPSC-Derived Cardiomyocytes as In Vitro Model for CVB3-Induced
       Myocarditis and Antiviral Drug Screening" (Sharma 2014 or similar)

Data: GSE57781_series_matrix.txt — microarray expression data
Format: GEO series matrix format (TSV)
Cell type: Human iPSC-derived cardiomyocytes (most physiologically relevant
           human cell model for CVB3 cardiac infection)

Advantage over PANC-1 (GSE184831):
- CARDIAC cells (not pancreatic)
- Relevant for myocarditis/DCM arm of campaign
- iPSC-derived = human genetic background
- CVB3 (cardiotropic serotype)

Campaign questions:
1. Is DMD (dystrophin) suppressed in CVB3-infected cardiomyocytes? (predicted -32× from PANC-1)
2. Is LAMP2 suppressed? (same mechanism, different cell type)
3. Is FOXP1 suppressed? (cardiac relevance confirmed?)
4. Is NLRP3/CASP1 signature consistent with PANC-1 and ME/CFS findings?
5. Any cardiomyocyte-specific CVB3 effects not seen in PANC-1?
"""

import os
import sys
import json
import re
import gzip
from collections import defaultdict

DATA_DIR = os.path.join(os.path.dirname(__file__), "transcriptomics")
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "..", "results")

# Campaign genes — same list as other analyses for cross-study comparison
CAMPAIGN_GENES = {
    "key_cvb_targets": ["DMD", "CXADR", "CD55"],  # dystrophin, CVB receptors
    "lamp2_autophagy": ["LAMP2", "LAMP1", "ATG7", "ATG12", "AMBRA1", "BECN1"],
    "foxp1_treg": ["FOXP1", "FOXP3"],
    "nlrp3": ["NLRP3", "CASP1", "IL18", "IL1B"],
    "nfkb": ["NFKB1", "NFKB2", "RELA", "TNF", "CCL2"],
    "er_stress": ["HSPA5", "DDIT3", "ATF6", "XBP1"],
    "ifn_signaling": ["IFIT1", "IFIT2", "IFIT3", "MX1", "STAT1", "STAT2", "IFNB1", "IRF3", "DDX58", "IFIH1"],
    "osbp_pi4k": ["OSBP", "PI4KB"],
    "mitochondrial": ["MT-ND1", "MT-ND2", "MT-ND3", "MT-ND4", "MT-ND5", "MT-CO2"],
    "cardiac_specific": ["MYH7", "MYH6", "TNNT2", "TNNI3", "SCN5A", "CACNA1C", "PLN"],
}

ALL_GENES = list({g for gs in CAMPAIGN_GENES.values() for g in gs})


def parse_series_matrix(filepath):
    """Parse GEO series matrix file format."""
    print(f"Parsing: {filepath}")

    sample_info = {}
    gene_data = defaultdict(dict)
    gene_symbols = {}
    sample_titles = {}

    opener = gzip.open if filepath.endswith('.gz') else open

    with opener(filepath, 'rt', encoding='utf-8', errors='replace') as f:
        in_table = False
        headers = None
        sample_geo_accessions = []
        sample_titles_list = []

        for line in f:
            line = line.strip()

            if line.startswith('!Sample_geo_accession'):
                parts = line.split('\t')
                sample_geo_accessions = [p.strip('"') for p in parts[1:]]

            elif line.startswith('!Sample_title'):
                parts = line.split('\t')
                sample_titles_list = [p.strip('"') for p in parts[1:]]

            elif line == '!series_matrix_table_begin':
                in_table = True
                continue

            elif line == '!series_matrix_table_end':
                in_table = False
                break

            elif in_table:
                parts = line.split('\t')
                if headers is None:
                    headers = parts  # First line = probe IDs header
                    continue

                if len(parts) < 2:
                    continue

                probe_id = parts[0].strip('"')
                try:
                    values = [float(p.strip('"')) for p in parts[1:] if p.strip('"')]
                except ValueError:
                    continue

                if values and headers:
                    for i, val in enumerate(values):
                        if i < len(sample_geo_accessions):
                            sample_id = sample_geo_accessions[i]
                            gene_data[probe_id][sample_id] = val

    # Map sample IDs to titles
    for i, acc in enumerate(sample_geo_accessions):
        if i < len(sample_titles_list):
            sample_titles[acc] = sample_titles_list[i]

    return dict(gene_data), sample_titles, sample_geo_accessions


def parse_probe_gene_mapping(filepath):
    """Extract probe-to-gene mapping from series matrix annotation lines."""
    probe_to_gene = {}
    opener = gzip.open if filepath.endswith('.gz') else open

    with opener(filepath, 'rt', encoding='utf-8', errors='replace') as f:
        for line in f:
            line = line.strip()
            # Look for annotation with gene symbols
            if 'GENE_SYMBOL' in line or 'gene_symbol' in line.lower():
                # GEO often has this in platform annotations
                parts = line.split('\t')
                if len(parts) >= 2:
                    probe_id = parts[0].strip('"! ')
                    gene = parts[-1].strip('"')
                    if gene and gene != 'Gene Symbol':
                        probe_to_gene[probe_id] = gene

    return probe_to_gene


def run_analysis():
    matrix_file = os.path.join(DATA_DIR, "GSE57781_series_matrix.txt")
    matrix_gz = matrix_file + ".gz"

    # Prefer uncompressed if available
    use_file = matrix_file if os.path.exists(matrix_file) else matrix_gz

    if not os.path.exists(use_file):
        print(f"ERROR: GSE57781 series matrix not found at {use_file}")
        return

    gene_data, sample_titles, sample_ids = parse_series_matrix(use_file)

    print(f"\nLoaded: {len(gene_data)} probes, {len(sample_ids)} samples")
    print("\nSamples:")
    for sid, title in sample_titles.items():
        print(f"  {sid}: {title}")

    # Identify CVB3-infected vs control samples from titles
    cvb_samples = []
    ctrl_samples = []

    for sid, title in sample_titles.items():
        title_lower = title.lower()
        if 'cvb' in title_lower or 'infected' in title_lower or 'virus' in title_lower:
            cvb_samples.append(sid)
        elif 'control' in title_lower or 'mock' in title_lower or 'uninfected' in title_lower:
            ctrl_samples.append(sid)
        else:
            print(f"  Unclassified: {sid} = {title}")

    print(f"\nCVB3-infected: {len(cvb_samples)} samples: {cvb_samples}")
    print(f"Controls: {len(ctrl_samples)} samples: {ctrl_samples}")

    if not cvb_samples or not ctrl_samples:
        print("\nWARNING: Could not classify samples by title. Printing all titles for manual inspection.")
        for sid, title in sorted(sample_titles.items()):
            print(f"  {sid}: {title}")
        return

    # For microarray: search for campaign genes by probe ID or gene name in data
    # The series matrix may include gene symbols in probe IDs or adjacent annotation
    # Try to find probes matching our gene list by searching probe IDs

    results = {
        "study": "GSE57781",
        "cell_type": "Human iPSC-derived cardiomyocytes",
        "virus": "CVB3",
        "n_probes": len(gene_data),
        "n_samples_cvb": len(cvb_samples),
        "n_samples_ctrl": len(ctrl_samples),
        "campaign_gene_results": {},
        "notes": []
    }

    import numpy as np

    # Compute fold changes for probes where gene names match
    # This is approximate for microarray without proper probe annotation
    found_genes = {}

    for probe_id, sample_values in gene_data.items():
        # Some GSE series matrices include gene symbol in probe ID
        for gene in ALL_GENES:
            if gene.upper() in probe_id.upper():
                cvb_vals = [sample_values.get(s) for s in cvb_samples if sample_values.get(s) is not None]
                ctrl_vals = [sample_values.get(s) for s in ctrl_samples if sample_values.get(s) is not None]

                if cvb_vals and ctrl_vals:
                    cvb_mean = np.mean(cvb_vals)
                    ctrl_mean = np.mean(ctrl_vals)
                    if ctrl_mean > 0:
                        log2fc = np.log2(cvb_mean / ctrl_mean)
                        if gene not in found_genes or abs(log2fc) > abs(found_genes[gene]['log2FC']):
                            found_genes[gene] = {
                                'probe_id': probe_id,
                                'cvb_mean': float(cvb_mean),
                                'ctrl_mean': float(ctrl_mean),
                                'log2FC': float(log2fc),
                                'direction': 'UP' if log2fc > 0.3 else ('DOWN' if log2fc < -0.3 else 'UNCHANGED')
                            }

    results['campaign_gene_results'] = found_genes

    print(f"\n=== Key Campaign Genes in CVB3 iPSC Cardiomyocytes ===")
    priority_genes = ['DMD', 'LAMP2', 'FOXP1', 'NLRP3', 'NFKB1', 'TNF', 'IFIT1',
                      'STAT1', 'ATG7', 'CXADR', 'OSBP', 'PI4KB', 'MT-ND3']

    for gene in priority_genes:
        if gene in found_genes:
            r = found_genes[gene]
            direction_symbol = "↑" if r['direction'] == 'UP' else ("↓" if r['direction'] == 'DOWN' else "~")
            print(f"  {gene:15s} {direction_symbol} log2FC={r['log2FC']:+.2f}")
        else:
            print(f"  {gene:15s} [not found by probe ID matching — may need GPL annotation]")

    # Save results
    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_path = os.path.join(RESULTS_DIR, "gse57781_cardiac_cvb3_analysis.json")
    with open(out_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nResults saved: {out_path}")

    print("\nNOTE: This is a microarray dataset. Probe-to-gene mapping may be incomplete.")
    print("For full analysis, download the platform annotation file (GPL identifier from study page)")
    print("and map probe IDs to gene symbols.")

    print("\nKey questions this dataset can answer:")
    print("1. Is DMD suppressed in CVB3-infected human cardiomyocytes?")
    print("   (If yes: confirms 2A protease DMD cleavage in CARDIAC cells, not just PANC-1)")
    print("2. Is LAMP2 suppressed?")
    print("   (If yes: confirms LAMP2 block mechanism in cardiac cells)")
    print("3. Is FOXP1 suppressed?")
    print("   (If yes: FOXP1 mechanism active in cardiomyocytes → explains autoimmune myocarditis)")
    print("4. Any cardiomyocyte-specific CVB3 effects?")
    print("   (e.g., cardiac ion channel disruption: SCN5A, CACNA1C, TNNT2)")

    return results


if __name__ == "__main__":
    run_analysis()
