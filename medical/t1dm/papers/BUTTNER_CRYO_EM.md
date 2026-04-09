# Büttner et al. 2022 — Cryo-EM Structure of CV-A6 Virion

**Citation:** Büttner CR, Spurný R, Füzik T, Plevka P. "Cryo-electron microscopy and image classification reveal the existence and structure of the coxsackievirus A6 virion." *Communications Biology* 5:898 (2022). DOI: 10.1038/s42003-022-03863-2

**PDB IDs:** 7QW9 (virion), 7QVX (altered particle), 7QVY (empty particle)
**EMDB IDs:** EMD-14186, EMD-14183, EMD-14184
**Resolution:** 2.68Å (virion), 2.50Å (altered), 2.82Å (empty)

## Key Structural Data

### Capsid Architecture
- 60 protomers, pseudo-T=3 icosahedral symmetry
- VP1: pentamers at fivefold axes (blue in figures)
- VP2: green, VP3: red — form heterohexamers at threefold axes
- VP4: 69 residues, internal, myristylated (attached to N-terminus via myristic acid)
- Virion radius: 130Å. Altered particle: 135Å (5.1Å expansion during uncoating)

### VP1 Hydrophobic Pocket
- Central cavity in VP1 β-sandwich ("canyon floor")
- Contains a POCKET FACTOR: stearic acid (C-18 fatty acid), modeled as STE
- Pocket factor interacts with 19 amino acids (Val11, Leu14, Ala15 of VP1; Ser23, Thr24, Ile25, Asn26 of VP4; others)
- Pocket factor STABILIZES the capsid in its native compact conformation
- **Expulsion of pocket factor = capsid destabilization = genome release = infection begins**
- This is where capsid-binding drugs (pleconaril, pocapavir) bind — they REPLACE the pocket factor and LOCK the capsid closed

### Capsid-Genome Contacts
- Trp38 of VP2 forms π-π stacking interactions with RNA bases (guanine)
- RNA density follows icosahedral symmetry at twofold axes
- Genome packaging is ORDERED — RNA contacts capsid at specific positions
- This ordered packaging may be important for the TD mutant persistence: altered RNA packaging could affect which genomes get into exosomes vs stay intracellular

### Uncoating Pathway (Entry)
1. Virion (compact, 130Å, pocket factor present) binds receptor
2. Pocket factor expelled → capsid expands to 135Å (altered particle)
3. VP4 externalizes → forms pore in host cell membrane
4. RNA genome released through capsid opening at twofold axis
5. Empty capsid (no RNA, no VP4) left behind

### Infectious Unit Ratio
- Purified CV-A6: 1 infectious unit per 500 particles
- This means 99.8% of viral particles are NON-INFECTIOUS
- For TD mutants (even slower assembly): the ratio may be even worse
- This extreme inefficiency is why TD mutants persist at such low levels

## Relevance to T1DM / CVB Research

### 1. The pocket factor = cholesterol connection
- The VP1 pocket contains a FATTY ACID (stearic acid)
- Pocket factor occupancy requires the right lipid composition in the membrane
- OSBP-mediated cholesterol delivery to replication organelles may influence which lipids are available as pocket factors
- Itraconazole (OSBP inhibitor) → altered membrane lipid composition → altered pocket factor availability → defective capsid assembly?

### 2. Capsid-binding drugs vs TD mutants
- Pleconaril binds the VP1 pocket → locks capsid → blocks uncoating
- But TD mutants use exosomal egress → less capsid-dependent
- HOWEVER: when TD mutant genomes are transmitted via PS-vesicles, they STILL need to be packaged in capsids inside those vesicles
- So capsid assembly is still required for TD mutant spread — just not for their lytic exit
- Pleconaril could block REINFECTION even if it doesn't block egress

### 3. Cross-serotype structure
- CV-A6 shares >69% sequence identity with CV-A16, EV-A71, CV-A10
- Capsid protomer structures superimpose with r.m.s.d. <0.65Å for >92% of atoms
- The VP1 pocket is STRUCTURALLY CONSERVED even when sequence varies
- This means pocket-binding drugs designed for one serotype may work on others
- Same principle as the 2C allosteric pocket conservation we found in our alignment (95-98%)

### 4. Vaccine implications
- Surface loops (BC, HI on VP1) differ between serotypes → explain low cross-protection
- The C-terminal arm of VP1 in CV-A6 extends across the particle surface (unique)
- This arm is ANTIGENIC — important for vaccine design targeting CV-A6 specifically
- For CVB (our target): similar capsid architecture but different surface loop conformations

## PDB Structures to Fetch for Further Analysis

| PDB ID | What | Resolution |
|--------|------|-----------|
| 7QW9 | CV-A6 virion | 2.68Å |
| 7QVX | CV-A6 altered particle | 2.50Å |
| 7QVY | CV-A6 empty particle | 2.82Å |
| 5X54 (5XS4) | CV-A6 altered (previous) | — |
| **To find** | CVB3 2C ATPase + fluoxetine | — |
| **To find** | CVB3 3Dpol + VPg | 3CDW |

## Status: STRUCTURAL DATA ACQUIRED — connects capsid architecture to drug targeting
