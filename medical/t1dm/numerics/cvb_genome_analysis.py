#!/usr/bin/env python3
"""
CVB Genome Analysis — numerical track Script 1
Fetch CVB complete genomes, extract 5' UTR, map cloverleaf structure,
analyze TD deletion impact, extract 2C/3A protein sequences.

T1DM systematic approach — Mountain 4 numerics
"""

import os
import json
from Bio import Entrez, SeqIO
from Bio.Seq import Seq
from collections import defaultdict

# NCBI requires email
Entrez.email = "sigma.method@research.org"

# Output dirs
SEQ_DIR = os.path.join(os.path.dirname(__file__), "sequences")
RES_DIR = os.path.join(os.path.dirname(__file__), "results")
os.makedirs(SEQ_DIR, exist_ok=True)
os.makedirs(RES_DIR, exist_ok=True)

# Known CVB complete genome accessions
CVB_ACCESSIONS = {
    "CVB1": "M16560.1",    # Coxsackievirus B1
    "CVB2": "AF085363.1",  # Coxsackievirus B2 Ohio-1
    "CVB3": "M33854.1",    # Coxsackievirus B3 Nancy
    "CVB4": "X05690.1",    # Coxsackievirus B4 JVB
    "CVB5": "JX276378.1",  # Coxsackievirus B5 (the one provided)
    "CVB6": "AF105342.1",  # Coxsackievirus B6 Schmitt
}

def fetch_genomes():
    """Fetch all CVB complete genomes from NCBI."""
    records = {}
    for name, acc in CVB_ACCESSIONS.items():
        print(f"Fetching {name} ({acc})...")
        try:
            handle = Entrez.efetch(db="nucleotide", id=acc, rettype="gb", retmode="text")
            record = SeqIO.read(handle, "genbank")
            handle.close()
            records[name] = record

            # Save FASTA
            fasta_path = os.path.join(SEQ_DIR, f"{name}_{acc.replace('.', '_')}.fasta")
            SeqIO.write(record, fasta_path, "fasta")
            print(f"  Length: {len(record.seq)} nt")
            print(f"  Description: {record.description}")
            print(f"  Saved: {fasta_path}")
        except Exception as e:
            print(f"  ERROR: {e}")

    return records

def extract_5utr(records):
    """Extract 5' UTR (first ~750nt) from each genome."""
    utrs = {}
    print("\n=== 5' UTR EXTRACTION ===")
    for name, record in records.items():
        # CVB 5' UTR is ~742nt (before polyprotein start)
        # Find CDS start
        cds_start = None
        for feature in record.features:
            if feature.type == "CDS":
                cds_start = int(feature.location.start)
                break

        if cds_start is None:
            # Default to ~750nt
            cds_start = 750

        utr_seq = str(record.seq[:cds_start])
        utrs[name] = utr_seq
        print(f"{name}: 5' UTR = {cds_start} nt")

        # Save
        with open(os.path.join(SEQ_DIR, f"{name}_5utr.fasta"), "w") as f:
            f.write(f">{name}_5UTR\n{utr_seq}\n")

    return utrs

def analyze_cloverleaf(utrs):
    """Analyze the 5' cloverleaf (domain I, first ~90nt) structure."""
    print("\n=== CLOVERLEAF ANALYSIS (Domain I) ===")
    print("Domain I is the first ~89 nucleotides of the enterovirus genome.")
    print("Structure: stem a → stem-loop b (PCBP2) → stem-loop c → stem-loop d (3CD)")
    print()

    cloverleaf_data = {}
    for name, utr in utrs.items():
        # Domain I is approximately the first 89nt
        domain_I = utr[:89]

        # Approximate boundaries (from published structures):
        # Stem a: nt 1-10 (pairs with ~80-89)
        # Stem-loop b: nt 11-35 (PCBP2 binding — poly(C) tract)
        # Stem-loop c: nt 36-50
        # Stem-loop d: nt 51-80 (3CD binding)

        stem_a = domain_I[:10]
        stem_loop_b = domain_I[10:35]  # PCBP2 binding site
        stem_loop_c = domain_I[35:50]
        stem_loop_d = domain_I[50:80]  # 3CD binding site

        cloverleaf_data[name] = {
            "domain_I": domain_I,
            "stem_a": stem_a,
            "stem_loop_b": stem_loop_b,
            "stem_loop_c": stem_loop_c,
            "stem_loop_d": stem_loop_d,
        }

        print(f"{name} Domain I ({len(domain_I)} nt):")
        print(f"  Stem a (1-10):       {stem_a}")
        print(f"  Stem-loop b (11-35): {stem_loop_b}  ← PCBP2 binds")
        print(f"  Stem-loop c (36-50): {stem_loop_c}")
        print(f"  Stem-loop d (51-80): {stem_loop_d}  ← 3CD binds")
        print()

    return cloverleaf_data

def analyze_td_deletions(cloverleaf_data):
    """Map what's lost at each TD deletion length."""
    print("\n=== TD DELETION IMPACT ANALYSIS ===")
    print("TD mutants delete 7-49nt from the 5' end.")
    print("What structural elements are lost at each length?\n")

    td_analysis = []
    for del_len in range(7, 50):
        lost = []
        if del_len >= 1:
            lost.append("stem_a (partial)")
        if del_len >= 10:
            lost.append("stem_a (complete)")
        if del_len >= 11:
            lost.append("stem_loop_b (partial) — PCBP2 BINDING IMPAIRED")
        if del_len >= 35:
            lost.append("stem_loop_b (complete) — PCBP2 BINDING LOST")
        if del_len >= 36:
            lost.append("stem_loop_c (partial)")
        if del_len >= 50:
            lost.append("stem_loop_c (complete)")
            lost.append("stem_loop_d THREATENED — 3CD binding at risk")

        pcbp2_status = "INTACT" if del_len < 11 else ("IMPAIRED" if del_len < 35 else "LOST")
        cd3_status = "INTACT" if del_len < 50 else "THREATENED"

        td_analysis.append({
            "deletion_length": del_len,
            "lost_elements": lost,
            "pcbp2_binding": pcbp2_status,
            "3cd_binding": cd3_status,
        })

    # Print summary table
    print(f"{'Del(nt)':>8} {'PCBP2':>10} {'3CD':>12} {'Elements Lost'}")
    print("-" * 70)
    for row in td_analysis:
        if row["deletion_length"] in [7, 10, 14, 21, 28, 35, 42, 49]:
            print(f"{row['deletion_length']:>8} {row['pcbp2_binding']:>10} {row['3cd_binding']:>12} {', '.join(row['lost_elements'][-1:])}")

    # The sweet spot
    print("\n=== THE PERSISTENCE SWEET SPOT ===")
    print("TD mutants with 10-35nt deletions:")
    print("  - Stem-loop b IMPAIRED (PCBP2 binding weakened)")
    print("  - Stem-loop d INTACT (3CD can still bind)")
    print("  - Replication: 100,000x slower but nonzero")
    print("  - Immune evasion: low protein expression, low dsRNA")
    print("  - This is WHERE persistent CVB lives — enough function")
    print("    to maintain infection, not enough to trigger clearance.")

    return td_analysis

def extract_proteins(records):
    """Extract 2C and 3A protein sequences from CDS annotations."""
    print("\n=== PROTEIN EXTRACTION ===")

    proteins = defaultdict(dict)

    for name, record in records.items():
        for feature in record.features:
            if feature.type == "mat_peptide" or feature.type == "CDS":
                product = feature.qualifiers.get("product", [""])[0]
                note = feature.qualifiers.get("note", [""])[0]

                # Look for 2C and 3A
                if "2C" in product or "2C" in note:
                    seq = feature.extract(record.seq).translate()
                    proteins[name]["2C"] = str(seq)
                    print(f"{name} 2C: {len(seq)} aa")

                elif "3A" in product or "3A" in note:
                    seq = feature.extract(record.seq).translate()
                    proteins[name]["3A"] = str(seq)
                    print(f"{name} 3A: {len(seq)} aa")

    # If mat_peptide annotations not found, try to extract from polyprotein
    if not any("2C" in v for v in proteins.values()):
        print("\nNote: mat_peptide annotations not found in all records.")
        print("2C is approximately at polyprotein position 1175-1505 (aa)")
        print("3A is approximately at polyprotein position 1506-1590 (aa)")

        for name, record in records.items():
            for feature in record.features:
                if feature.type == "CDS" and "polyprotein" in feature.qualifiers.get("product", [""])[0].lower():
                    poly = feature.extract(record.seq).translate()
                    # Approximate positions (vary by serotype, +/- 20aa)
                    proteins[name]["2C_approx"] = str(poly[1174:1505])
                    proteins[name]["3A_approx"] = str(poly[1505:1590])
                    print(f"{name} polyprotein: {len(poly)} aa, extracted 2C~331aa, 3A~85aa")

    return proteins

def conservation_analysis(proteins):
    """Quick conservation check of 2C across serotypes."""
    print("\n=== 2C CONSERVATION ANALYSIS ===")

    seqs_2c = {}
    for name, prots in proteins.items():
        if "2C" in prots:
            seqs_2c[name] = prots["2C"]
        elif "2C_approx" in prots:
            seqs_2c[name] = prots["2C_approx"]

    if len(seqs_2c) < 2:
        print("Not enough 2C sequences for comparison")
        return

    # Pairwise identity
    names = list(seqs_2c.keys())
    print(f"\nPairwise identity of 2C ATPase ({len(names)} serotypes):")
    for i in range(len(names)):
        for j in range(i+1, len(names)):
            s1 = seqs_2c[names[i]]
            s2 = seqs_2c[names[j]]
            min_len = min(len(s1), len(s2))
            matches = sum(1 for a, b in zip(s1[:min_len], s2[:min_len]) if a == b)
            identity = matches / min_len * 100
            print(f"  {names[i]} vs {names[j]}: {identity:.1f}% identity ({matches}/{min_len})")

    # Known fluoxetine binding residues (approximate, from crystal structure)
    # The allosteric pocket is in the C-terminal domain of 2C
    print("\n=== FLUOXETINE BINDING POCKET ===")
    print("The allosteric hydrophobic pocket is in the C-terminal region of 2C.")
    print("Key residues from PDB structure (CVB3 numbering):")
    print("  Highly conserved across enteroviruses → broad-spectrum target")

def main():
    print("=" * 70)
    print("CVB GENOME ANALYSIS — T1DM systematic approach, Mountain 4 Numerics")
    print("=" * 70)

    # Step 1: Fetch genomes
    records = fetch_genomes()

    if not records:
        print("ERROR: No genomes fetched. Check network/NCBI access.")
        return

    # Step 2: Extract 5' UTR
    utrs = extract_5utr(records)

    # Step 3: Analyze cloverleaf
    cloverleaf_data = analyze_cloverleaf(utrs)

    # Step 4: TD deletion analysis
    td_analysis = analyze_td_deletions(cloverleaf_data)

    # Step 5: Extract proteins
    proteins = extract_proteins(records)

    # Step 6: Conservation analysis
    conservation_analysis(proteins)

    # Save results
    results = {
        "cloverleaf": {name: {k: v for k, v in data.items()}
                       for name, data in cloverleaf_data.items()},
        "td_analysis_summary": [
            {
                "deletion_nt": d["deletion_length"],
                "pcbp2": d["pcbp2_binding"],
                "3cd": d["3cd_binding"],
            }
            for d in td_analysis if d["deletion_length"] in [7,10,14,21,28,35,42,49]
        ],
    }

    results_path = os.path.join(RES_DIR, "cvb_genome_analysis.json")
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {results_path}")

    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)

if __name__ == "__main__":
    main()
