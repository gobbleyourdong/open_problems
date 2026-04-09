#!/usr/bin/env python3
"""
CVB 2C ATPase Deep Analysis — numerical track Script 3
Map the fluoxetine allosteric binding pocket across serotypes.
Analyze 3A protein ACBD3-binding motif conservation.
Fetch the actual 2C crystal structure data.

T1DM systematic approach — Mountain 4 numerics
"""

import os
import json
from Bio import Entrez, SeqIO

Entrez.email = "sigma.method@research.org"

SEQ_DIR = os.path.join(os.path.dirname(__file__), "sequences")
RES_DIR = os.path.join(os.path.dirname(__file__), "results")

def load_genomes():
    """Load previously fetched genomes."""
    records = {}
    for fname in sorted(os.listdir(SEQ_DIR)):
        if fname.endswith(".fasta") and not fname.endswith("_5utr.fasta"):
            name = fname.split("_")[0]
            if name.startswith("CVB"):
                record = SeqIO.read(os.path.join(SEQ_DIR, fname), "fasta")
                records[name] = record
    return records

def extract_polyprotein(records):
    """Re-fetch GenBank records to get CDS annotations."""
    accessions = {
        "CVB1": "M16560.1", "CVB2": "AF085363.1", "CVB3": "M33854.1",
        "CVB4": "X05690.1", "CVB5": "JX276378.1", "CVB6": "AF105342.1",
    }

    proteins = {}
    for name, acc in accessions.items():
        try:
            handle = Entrez.efetch(db="nucleotide", id=acc, rettype="gb", retmode="text")
            record = SeqIO.read(handle, "genbank")
            handle.close()

            for feature in record.features:
                if feature.type == "CDS":
                    product = feature.qualifiers.get("product", [""])[0].lower()
                    if "polyprotein" in product or not product:
                        poly_nt = feature.extract(record.seq)
                        poly_aa = str(poly_nt.translate()).rstrip("*")
                        proteins[name] = poly_aa
                        print(f"{name}: polyprotein {len(poly_aa)} aa")
                        break

                # Also check for mat_peptide annotations
                if feature.type == "mat_peptide":
                    product = feature.qualifiers.get("product", [""])[0]
                    if "2C" in product:
                        seq_2c = str(feature.extract(record.seq).translate()).rstrip("*")
                        proteins[f"{name}_2C"] = seq_2c
                    elif "3A" in product:
                        seq_3a = str(feature.extract(record.seq).translate()).rstrip("*")
                        proteins[f"{name}_3A"] = seq_3a

        except Exception as e:
            print(f"  {name}: ERROR {e}")

    return proteins

def extract_2c_from_polyprotein(proteins):
    """Extract 2C region from polyprotein using known boundaries."""
    # CVB3 Nancy (reference): 2C starts at polyprotein position ~1174, length 329aa
    # This is approximate — varies by serotype by a few residues

    print("\n=== 2C ATPase EXTRACTION ===")
    print("Using CVB3 Nancy as reference. 2C ≈ aa 1174-1503 of polyprotein.\n")

    seqs_2c = {}
    for name, poly in proteins.items():
        if "_2C" in name:
            # Already extracted via mat_peptide
            seqs_2c[name.replace("_2C", "")] = poly
            continue
        if "_" in name:
            continue

        # Find 2C by searching for conserved GxxGxGKS motif (Walker A box)
        # This is the ATPase active site — present in ALL enterovirus 2C proteins
        walker_a = "GK"  # simplified search
        for i in range(len(poly) - 350):
            segment = poly[i:i+329]
            # Look for the GXXGXGKS Walker A motif
            if "GKSL" in segment or "GKST" in segment or "GKSV" in segment:
                seqs_2c[name] = segment
                print(f"{name}: 2C extracted at polyprotein position {i}-{i+329}")
                break

        if name not in seqs_2c:
            # Fallback: use approximate position
            seqs_2c[name] = poly[1174:1503]
            print(f"{name}: 2C extracted at default position 1174-1503")

    return seqs_2c

def analyze_2c_pocket(seqs_2c):
    """Map the fluoxetine allosteric binding pocket residues."""
    print("\n=== FLUOXETINE ALLOSTERIC POCKET ANALYSIS ===")
    print("From Sci Adv 2022 (PDB structure of CVB3 2C + S-fluoxetine):")
    print("The allosteric pocket is a hydrophobic cavity in the C-terminal domain.\n")

    # Known pocket-lining residues from the crystal structure (CVB3 numbering)
    # From Büttner et al. / Musharrafieh et al. / Sci Adv 2022
    # These are APPROXIMATE — exact residues from the PDB structure
    # The pocket is lined by hydrophobic residues in helices α6-α8
    pocket_region_start = 220  # approximate start of the allosteric pocket region
    pocket_region_end = 310    # approximate end

    print("2C C-terminal region alignment (aa 220-310, pocket region):\n")

    names = sorted(seqs_2c.keys())
    ref = "CVB3"

    if ref not in seqs_2c:
        ref = names[0]

    ref_seq = seqs_2c[ref]
    pocket = ref_seq[pocket_region_start:pocket_region_end]

    print(f"{'Name':>6}  {'Pocket region (aa 220-310)':}")
    print("-" * 100)
    for name in names:
        seq = seqs_2c[name]
        region = seq[pocket_region_start:pocket_region_end]
        # Mark differences from reference
        diff_str = ""
        for i, (a, b) in enumerate(zip(pocket, region)):
            if a == b:
                diff_str += "."
            else:
                diff_str += b
        print(f"{name:>6}  {region}")
        if name != ref:
            print(f"{'diff':>6}  {diff_str}")

    # Count conserved positions
    min_len = min(len(seqs_2c[n][pocket_region_start:pocket_region_end]) for n in names)
    conserved = 0
    variable_positions = []
    for i in range(min_len):
        residues = set(seqs_2c[n][pocket_region_start + i] for n in names)
        if len(residues) == 1:
            conserved += 1
        else:
            variable_positions.append((pocket_region_start + i, residues))

    print(f"\nPocket region conservation: {conserved}/{min_len} ({conserved/min_len*100:.1f}%)")
    if variable_positions:
        print(f"Variable positions ({len(variable_positions)}):")
        for pos, residues in variable_positions[:20]:
            print(f"  Position {pos}: {', '.join(sorted(residues))}")

    return conserved, min_len, variable_positions

def analyze_3a(proteins):
    """Extract and analyze 3A protein (recruits ACBD3 → PI4KB)."""
    print("\n=== 3A PROTEIN ANALYSIS (ACBD3 RECRUITMENT) ===")
    print("3A is the membrane anchor that recruits the OSBP pathway.\n")

    seqs_3a = {}
    for name, poly in proteins.items():
        if "_3A" in name:
            seqs_3a[name.replace("_3A", "")] = poly
            continue
        if "_" in name:
            continue
        # 3A follows 2C in the polyprotein, ~89 aa
        seqs_3a[name] = poly[1503:1592]

    names = sorted(seqs_3a.keys())
    print(f"{'Name':>6}  {'3A sequence (~89 aa)':}")
    print("-" * 100)
    for name in names:
        print(f"{name:>6}  {seqs_3a[name]}")

    # Pairwise identity
    print("\n3A pairwise identity:")
    for i in range(len(names)):
        for j in range(i+1, len(names)):
            s1, s2 = seqs_3a[names[i]], seqs_3a[names[j]]
            min_len = min(len(s1), len(s2))
            matches = sum(1 for a, b in zip(s1[:min_len], s2[:min_len]) if a == b)
            print(f"  {names[i]} vs {names[j]}: {matches/min_len*100:.1f}%")

    # The ACBD3-binding region is in the N-terminal ~60 residues of 3A
    print("\n3A N-terminal region (ACBD3-binding, first 60 aa):")
    for name in names:
        print(f"  {name}: {seqs_3a[name][:60]}")

    return seqs_3a

def walker_box_analysis(seqs_2c):
    """Find and compare Walker A and B boxes (ATPase active site)."""
    print("\n=== WALKER BOX ANALYSIS (ATPase ACTIVE SITE) ===")
    print("Walker A: GxxGxGK[ST] — ATP binding")
    print("Walker B: DExx — ATP hydrolysis / Mg2+ coordination\n")

    for name in sorted(seqs_2c.keys()):
        seq = seqs_2c[name]
        # Find Walker A (GxxGxGK)
        for i in range(len(seq) - 7):
            if seq[i] == 'G' and seq[i+3] == 'G' and seq[i+5] == 'G' and seq[i+6] == 'K':
                print(f"{name} Walker A at pos {i}: {seq[i:i+8]}")
                break

        # Find Walker B / DEAD/DEXX motif
        for i in range(len(seq) - 4):
            if seq[i:i+2] == 'DE':
                context = seq[max(0,i-3):i+7]
                # Only report if in the right region (after Walker A)
                if i > 100:
                    print(f"{name} Walker B at pos {i}: {seq[i:i+4]} (context: {context})")
                    break

def full_2c_alignment(seqs_2c):
    """Full 2C alignment with conservation per position."""
    print("\n=== FULL 2C ALIGNMENT STATISTICS ===")

    names = sorted(seqs_2c.keys())
    min_len = min(len(seqs_2c[n]) for n in names)

    # Per-position conservation
    fully_conserved = 0
    conservative_sub = 0  # same physicochemical class
    variable = 0

    hydrophobic = set("AILMFWVP")
    polar = set("STNQ")
    charged_pos = set("RKH")
    charged_neg = set("DE")

    for i in range(min_len):
        residues = set(seqs_2c[n][i] for n in names)
        if len(residues) == 1:
            fully_conserved += 1
        elif all(r in hydrophobic for r in residues) or \
             all(r in polar for r in residues) or \
             all(r in charged_pos for r in residues) or \
             all(r in charged_neg for r in residues):
            conservative_sub += 1
        else:
            variable += 1

    print(f"Aligned length: {min_len} aa")
    print(f"Fully conserved: {fully_conserved}/{min_len} ({fully_conserved/min_len*100:.1f}%)")
    print(f"Conservative substitution: {conservative_sub}/{min_len} ({conservative_sub/min_len*100:.1f}%)")
    print(f"Variable: {variable}/{min_len} ({variable/min_len*100:.1f}%)")
    print(f"Functionally conserved (identical + conservative): {fully_conserved+conservative_sub}/{min_len} "
          f"({(fully_conserved+conservative_sub)/min_len*100:.1f}%)")

    return {
        "fully_conserved": fully_conserved,
        "conservative": conservative_sub,
        "variable": variable,
        "total": min_len,
    }

def main():
    print("=" * 70)
    print("CVB 2C ATPase & 3A PROTEIN ANALYSIS")
    print("=" * 70)

    # Fetch annotated records
    proteins = extract_polyprotein({})

    # Extract 2C
    seqs_2c = extract_2c_from_polyprotein(proteins)

    if not seqs_2c:
        print("ERROR: Could not extract 2C sequences.")
        return

    # Full alignment stats
    stats = full_2c_alignment(seqs_2c)

    # Walker box analysis
    walker_box_analysis(seqs_2c)

    # Pocket analysis
    conserved, total, variable = analyze_2c_pocket(seqs_2c)

    # 3A analysis
    seqs_3a = analyze_3a(proteins)

    # Save results
    results = {
        "2c_conservation": stats,
        "pocket_conservation": {"conserved": conserved, "total": total},
        "serotypes_analyzed": list(seqs_2c.keys()),
    }
    with open(os.path.join(RES_DIR, "protein_2c_analysis.json"), "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to {os.path.join(RES_DIR, 'protein_2c_analysis.json')}")

    # Save 2C sequences as FASTA
    with open(os.path.join(SEQ_DIR, "all_2C_proteins.fasta"), "w") as f:
        for name in sorted(seqs_2c.keys()):
            f.write(f">{name}_2C\n{seqs_2c[name]}\n")
    print(f"2C sequences saved to {os.path.join(SEQ_DIR, 'all_2C_proteins.fasta')}")

    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)

if __name__ == "__main__":
    main()
