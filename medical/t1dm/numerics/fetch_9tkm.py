#!/usr/bin/env python3
"""
Fetch and Analyze PDB 9tkm — First-Ever CVB Atomic Structure
Released April 8, 2026. EMD-56033. CVB1 VLP∆VP4.

Run this AFTER April 8 when the embargo lifts.

T1DM systematic approach — Mountain 4 numerics
"""

import os
import sys
import json
from datetime import datetime

SEQ_DIR = os.path.join(os.path.dirname(__file__), "sequences")
RES_DIR = os.path.join(os.path.dirname(__file__), "results")
STRUCT_DIR = os.path.join(os.path.dirname(__file__), "structures")
os.makedirs(STRUCT_DIR, exist_ok=True)

def check_date():
    """Check if the data should be available."""
    today = datetime.now().strftime("%Y-%m-%d")
    if today < "2026-04-08":
        print(f"WARNING: Today is {today}. PDB 9tkm releases April 8, 2026.")
        print("The download may fail if the embargo hasn't lifted yet.\n")
    else:
        print(f"Today is {today}. PDB 9tkm should be available.\n")

def fetch_pdb():
    """Fetch 9tkm from RCSB PDB."""
    import urllib.request

    pdb_url = "https://files.rcsb.org/download/9tkm.pdb"
    cif_url = "https://files.rcsb.org/download/9tkm.cif"

    pdb_path = os.path.join(STRUCT_DIR, "9tkm.pdb")
    cif_path = os.path.join(STRUCT_DIR, "9tkm.cif")

    for url, path, fmt in [(pdb_url, pdb_path, "PDB"), (cif_url, cif_path, "mmCIF")]:
        try:
            print(f"Fetching {fmt} from {url}...")
            urllib.request.urlretrieve(url, path)
            size = os.path.getsize(path)
            print(f"  Saved: {path} ({size:,} bytes)")
        except Exception as e:
            print(f"  FAILED: {e}")
            print(f"  (May still be embargoed. Try again after April 8.)")

    return pdb_path if os.path.exists(pdb_path) else None

def fetch_emdb():
    """Fetch EMD-56033 density map."""
    import urllib.request

    map_url = "https://ftp.ebi.ac.uk/pub/databases/emdb/structures/EMD-56033/map/emd_56033.map.gz"
    map_path = os.path.join(STRUCT_DIR, "emd_56033.map.gz")

    try:
        print(f"Fetching EMDB map from {map_url}...")
        urllib.request.urlretrieve(map_url, map_path)
        size = os.path.getsize(map_path)
        print(f"  Saved: {map_path} ({size:,} bytes)")
    except Exception as e:
        print(f"  FAILED: {e}")

def analyze_pdb(pdb_path):
    """Basic analysis of the CVB1 VLP∆VP4 structure."""
    try:
        from Bio.PDB import PDBParser
        parser = PDBParser(QUIET=True)
        structure = parser.get_structure("9tkm", pdb_path)
    except ImportError:
        print("Biopython PDB parser not available. Using text parsing.\n")
        analyze_pdb_text(pdb_path)
        return
    except Exception as e:
        print(f"PDB parsing failed: {e}. Using text parsing.\n")
        analyze_pdb_text(pdb_path)
        return

    model = structure[0]

    print("\n=== PDB 9tkm STRUCTURE ANALYSIS ===")
    print("CVB1 VLP∆VP4 — First-ever CVB atomic structure\n")

    chains = list(model.get_chains())
    print(f"Chains: {len(chains)}")
    for chain in chains:
        residues = [r for r in chain.get_residues() if r.get_id()[0] == ' ']
        atoms = list(chain.get_atoms())
        print(f"  Chain {chain.id}: {len(residues)} residues, {len(atoms)} atoms")

    total_atoms = sum(1 for _ in model.get_atoms())
    total_residues = sum(1 for r in model.get_residues() if r.get_id()[0] == ' ')
    print(f"\nTotal: {total_residues} residues, {total_atoms} atoms")

    # Extract capsid protein sequences
    print("\n=== CAPSID PROTEIN SEQUENCES (from structure) ===")
    for chain in chains:
        seq = ""
        from Bio.PDB.Polypeptide import three_to_one
        for residue in chain.get_residues():
            if residue.get_id()[0] == ' ':
                try:
                    seq += three_to_one(residue.get_resname())
                except KeyError:
                    seq += 'X'
        if len(seq) > 10:
            print(f"Chain {chain.id}: {len(seq)} aa")
            print(f"  First 50: {seq[:50]}...")
            # Save
            with open(os.path.join(SEQ_DIR, f"9tkm_chain{chain.id}.fasta"), "w") as f:
                f.write(f">9tkm_chain_{chain.id}\n{seq}\n")

    # Look for ligands
    print("\n=== LIGANDS / POCKET FACTORS ===")
    for chain in chains:
        for residue in chain.get_residues():
            het_flag = residue.get_id()[0]
            if het_flag not in (' ', 'W'):  # Not protein, not water
                print(f"  Chain {chain.id}: {residue.get_resname()} at {residue.get_id()}")

def analyze_pdb_text(pdb_path):
    """Fallback text-based PDB analysis."""
    print("\n=== PDB 9tkm TEXT ANALYSIS ===\n")

    chains = set()
    atoms = 0
    residues = set()
    hetams = []

    with open(pdb_path) as f:
        for line in f:
            if line.startswith("ATOM"):
                atoms += 1
                chain = line[21]
                resnum = line[22:26].strip()
                chains.add(chain)
                residues.add((chain, resnum))
            elif line.startswith("HETATM"):
                resname = line[17:20].strip()
                chain = line[21]
                if resname != "HOH":
                    hetams.append((chain, resname, line[22:26].strip()))
            elif line.startswith("TITLE"):
                print(f"TITLE: {line[10:].strip()}")

    print(f"\nChains: {sorted(chains)}")
    print(f"Total atoms: {atoms}")
    print(f"Total residues: {len(residues)}")

    # Per-chain residue count
    for c in sorted(chains):
        n = sum(1 for ch, _ in residues if ch == c)
        print(f"  Chain {c}: {n} residues")

    if hetams:
        print(f"\nLigands/heteroatoms:")
        seen = set()
        for ch, name, num in hetams:
            key = (ch, name)
            if key not in seen:
                print(f"  Chain {ch}: {name}")
                seen.add(key)

def compare_to_our_sequences():
    """Compare 9tkm chains to our CVB1 extracted proteins."""
    print("\n=== COMPARISON TO OUR SEQUENCE DATA ===")
    print("We extracted VP1, 2C, 3A from CVB1 polyprotein (M16560.1)")
    print("9tkm contains VP1, VP2, VP3 (no VP4 — it's the ∆VP4 construct)")
    print()
    print("Key questions:")
    print("1. Does the VP1 in 9tkm match our CVB1 VP1 extraction?")
    print("2. Where is the VP1 hydrophobic pocket in the structure?")
    print("3. Are there pocket factors (fatty acids) visible?")
    print("4. What does the VP4 DELETION look like structurally?")
    print("5. Can we map the PALXA epitope (ADE-causing) on the surface?")

def main():
    print("=" * 70)
    print("PDB 9tkm — FIRST-EVER CVB ATOMIC STRUCTURE")
    print("CVB1 VLP∆VP4 (Soppela et al. 2026, J Biomed Sci)")
    print("EMD-56033 | PDB 9tkm | Released April 8, 2026")
    print("=" * 70)

    check_date()

    # Try to fetch
    pdb_path = fetch_pdb()

    if pdb_path and os.path.getsize(pdb_path) > 1000:
        analyze_pdb(pdb_path)
        compare_to_our_sequences()
    else:
        print("\nStructure not yet available. Pipeline ready for when it drops.")
        print("Re-run this script after April 8, 2026.")
        compare_to_our_sequences()

    # Try EMDB
    fetch_emdb()

    print("\n" + "=" * 70)
    print("PIPELINE READY")
    print("=" * 70)

if __name__ == "__main__":
    main()
