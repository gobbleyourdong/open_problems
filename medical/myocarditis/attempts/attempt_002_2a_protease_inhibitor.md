# Attempt 002: Direct 2A Protease Inhibition — The Open Target

## The Insight

The T1DM protocol clears CVB indirectly (fluoxetine blocks replication, autophagy clears infected cells). This works for T1DM because beta cells regenerate — you just need to tip the balance.

For myocarditis/DCM, you need to stop dystrophin cleavage FAST because cardiomyocytes don't regenerate. Indirect clearance takes weeks-months. Direct 2A protease inhibition would stop cleavage in hours.

## 2A Protease Biology

- **Type**: Cysteine protease (catalytic triad: Cys109, His20, Asp38 in CVB3 numbering)
- **Size**: ~17 kDa, 150 amino acids
- **Structure**: Known — PDB entries available for CVB3 2A
- **Substrate**: Cleaves after glycine in eIF4G (Gly681-Arg682), dystrophin (hinge 3 region)
- **Specificity**: Recognizes a GxxG motif in a flexible loop context
- **Conservation**: 2A is >90% conserved across CVB1-5 serotypes → one inhibitor covers all

## Why No 2A Inhibitor Exists

1. **Small target** — 17 kDa, shallow active site, hard to drug with small molecules
2. **Cysteine protease** — reactive cysteine warheads exist but often lack selectivity
3. **No commercial interest** — CVB is "just a cold virus" (if only they knew)
4. **3C gets all the attention** — 3C protease is the replication enzyme, 2A is "just" a host-shutoff factor

## Drug Design Approaches

### Approach A: Covalent cysteine inhibitors
- Rupintrivir (AG7088) was developed for rhinovirus 3C (another picornavirus cysteine protease)
- Reached Phase 2 for rhinovirus, abandoned commercially
- Could it be repurposed or modified for 2A? Different substrate specificity but same catalytic mechanism
- **Action**: virtual screening of rupintrivir analogs against CVB3 2A active site

### Approach B: Peptide-based inhibitors
- Design peptide mimicking the dystrophin cleavage site (hinge 3)
- Modify to be non-cleavable → competitive inhibitor sitting in 2A active site
- Precedent: HIV protease inhibitors are substrate-based transition state mimics
- **Challenge**: peptide delivery, stability, cell permeability

### Approach C: Allosteric inhibitors
- 2A undergoes conformational change upon substrate binding
- Small molecule stabilizing the "closed" (inactive) conformation
- Less specific selectivity issue but harder to design de novo
- **Action**: molecular dynamics of 2A conformational states, pocket identification

### Approach D: Repurposing screen
- Screen FDA-approved drugs for 2A inhibition in vitro
- Fluorescent substrate assay: measure 2A cleavage of fluorogenic peptide ± drug candidates
- Start with: protease inhibitors (HIV PIs), cysteine protease inhibitors, known covalent drugs
- **This is the fastest path** — if an existing drug hits 2A even weakly, it's immediately testable

## The Immediate Experiment (numerical track Request)

**REQUEST TO ODD INSTANCE:**
1. Download CVB3 2A crystal structure from PDB
2. Characterize active site geometry: pocket volume, electrostatic surface, hydrogen bond donors/acceptors
3. Virtual screen FDA-approved drugs (DrugBank) against 2A active site using AutoDock/Vina
4. Rank hits by predicted binding affinity
5. Cross-reference with drugs that are already safe in cardiac patients

This is a numerics/computation task — belongs to the numerical track.

## What Success Looks Like

An existing, cheap, orally available drug that inhibits CVB 2A protease with IC50 < 10 μM.

Added to the protocol:
- Day 1: 2A inhibitor (stops dystrophin cleavage immediately)
- Day 1: Fluoxetine (stops viral replication)
- Week 1+: FMD (clears TD mutants via autophagy)
- Month 1+: full anti-inflammatory stack

**The 2A inhibitor buys time.** It's the tourniquet while the antiviral protocol does the surgery.

## Status: TARGET IDENTIFIED — needs computational screening (numerical track task)
