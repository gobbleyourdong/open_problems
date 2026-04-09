# Attempt 041: From Theory to Computation — CVB Genome Analysis

## The Data

**GenBank JX276378.1**: Complete genome of Human Coxsackievirus B5, isolate CVB5/SD/09.

This is the raw material. The actual nucleotide sequence of the virus we've been theorizing about for 40 attempts. Time to look at it.

## What We Need to Compute

### 1. Map the 5' Cloverleaf Structure
- Extract the first ~100nt of the CVB5 genome
- Predict RNA secondary structure (stem a, stem-loop b, c, d)
- Identify EXACTLY which nucleotides are in stem-loop b (PCBP2 binding site)
- Identify EXACTLY which nucleotides are in stem-loop d (3CD binding site)
- Map the TD deletion range (7-49nt): which structural elements are lost at each deletion length?

### 2. Compare Cloverleaf Across CVB Serotypes
- Fetch CVB1-6 complete genomes from GenBank
- Align the 5' UTR regions
- Identify conserved vs variable positions in the cloverleaf
- The CONSERVED positions are the ones the virus CANNOT afford to lose = druggable constraints
- The positions that TD mutants DELETE must be in the non-essential-for-persistence region

### 3. Map the 2C ATPase Sequence
- Extract the 2C coding region from each CVB serotype
- Align protein sequences
- Map the allosteric fluoxetine binding pocket residues onto the alignment
- How conserved is the binding site across serotypes?
- If highly conserved: fluoxetine should work against all CVB serotypes
- If variable: may need serotype-specific inhibitors

### 4. Map the OSBP-Interacting Viral Proteins
- Extract 3A protein sequences (recruits ACBD3 → PI4KB → OSBP)
- Identify the ACBD3-binding motif in 3A
- How conserved is this motif? Can it be disrupted?

### 5. Analyze the PS-Vesicle Egress Signals
- What viral or host sequences determine whether an autophagosome goes to lysosome vs plasma membrane?
- Are there viral protein motifs that redirect SNARE trafficking?

## The Tool: scikit-bio

Python library for bioinformatics:
- **Sequence objects**: DNA, RNA, Protein with alignment, motif finding, k-mer analysis
- **Phylogenetic trees**: compare CVB serotypes evolutionary distance
- **Statistical tests**: PERMANOVA, Mantel tests for sequence similarity vs phenotype
- **Compositional analysis**: for comparing viral populations (quasispecies analysis)

Combined with:
- **Biopython**: GenBank record parsing, NCBI Entrez API for batch sequence retrieval
- **ViennaRNA / RNAfold**: RNA secondary structure prediction for the cloverleaf
- **PyMOL / ChimeraX**: 3D visualization of 2C ATPase with fluoxetine docked

## The numerical track Should Build

This is numerics work. The theory track (me) should NOT write .py files. But I can specify what the numerical track should build:

### Script 1: `cvb_genome_fetch.py`
- Fetch all CVB1-6 complete genomes from NCBI
- Extract 5' UTR (first 750nt), 2C coding region, 3A coding region
- Save as FASTA files in `numerics/sequences/`

### Script 2: `cloverleaf_structure.py`
- Take 5' UTR sequences
- Predict secondary structure using RNAfold
- Map stem a, stem-loop b, c, d boundaries
- Visualize: which nucleotides are lost at each TD deletion length (7, 14, 21, 28, 35, 42, 49nt)
- Output: table of "deletion length → structural elements lost → proteins that can no longer bind"

### Script 3: `2c_fluoxetine_conservation.py`
- Align 2C protein sequences across CVB1-6
- Map the allosteric pocket residues (from PDB crystal structure)
- Calculate conservation score at each pocket position
- Output: "is the fluoxetine binding site conserved across all serotypes?"

### Script 4: `osbp_interaction_map.py`
- Align 3A protein sequences
- Identify ACBD3-binding residues
- Cross-reference with OSBP recruitment pathway
- Output: "can we disrupt the 3A→ACBD3→PI4KB→OSBP chain at the viral protein level?"

### Script 5: `td_mutant_simulator.py`
- Take wild-type CVB genome
- Generate all possible TD deletions (7-49nt in steps of 1)
- For each: predict cloverleaf structure, score PCBP2/3CD binding capability
- Model: replication rate as function of deletion length
- Output: "sweet spot" deletion length where virus persists maximally (enough function to replicate, enough deletion to evade immunity)

## Request for numerical track

```
REQUEST 042: Computational virology pipeline

Priority: HIGH
Justification: 40 attempts of theory need numerical grounding.
We have the GenBank accession (JX276378.1) and the analysis tools (scikit-bio, Biopython).
Time to look at the actual sequence.

Deliverables:
1. CVB1-6 complete genomes fetched and organized
2. 5' cloverleaf structure predicted and mapped
3. TD deletion structural impact table
4. 2C fluoxetine binding site conservation analysis
5. 3A-ACBD3 interaction motif conservation

Tools: scikit-bio, Biopython, ViennaRNA (RNAfold), matplotlib
Input: GenBank JX276378.1 + NCBI Entrez API
Output: numerics/sequences/, numerics/structures/, results/
```

## Status: THEORY → COMPUTATION HANDOFF — 5 scripts specified for numerical track
