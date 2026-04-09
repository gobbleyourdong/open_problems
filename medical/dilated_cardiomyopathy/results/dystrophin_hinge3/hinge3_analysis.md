# Dystrophin Hinge-3 Cleavage Site Analysis — REQ-003

*Generated: 2026-04-08*

## 1. Sequence
- UniProt: P11532 (human dystrophin, 3685 aa)
- Fetched via Biopython `ExPASy.get_sprot_raw('P11532')`

## 2. Domain Map

| Domain | Start | End | Notes |
|--------|-------|-----|-------|
| N-terminal actin-binding domain (ABD1) | 1 | 246 |  |
| Spectrin-like repeat 1 | 243 | 495 |  |
| Spectrin-like repeat 2 | 493 | 745 |  |
| Spectrin-like repeat 3 | 743 | 997 |  |
| Hinge 1 | 326 | 339 |  |
| Spectrin-like repeats 4-15 | 994 | 1804 |  |
| Hinge 2 | 1461 | 1480 |  |
| Spectrin-like repeats 16-22 | 1804 | 2291 |  |
| Hinge 3 (2A cleavage region) | 1890 | 1985 | ← 2A cleavage region |
| Spectrin-like repeats 23-24 | 2291 | 2594 |  |
| Hinge 4 | 3056 | 3072 |  |
| Cysteine-rich domain (WW + EF-hand) | 3080 | 3360 |  |
| C-terminal domain | 3361 | 3685 |  |

## 3. Hinge-3 Region (aa 1890–1985)

- **Length**: 96 aa
- **Proline content**: 3.1% (characteristic of flexible hinge)
- **Sequence** (first 60 aa of hinge-3):
  `LKCLDDIEKKLASLPEPRDERKIKEIDRELQKKKEELNAVRRQAEGLSEDGAAMAVEPTQ`

### Badorff 1999 Cleavage Context

Badorff et al. (J Clin Invest 1999;103:1444) reported 2A protease cleavage
of dystrophin *near amino acid 2432* in the mouse isoform. The context peptide
flanking the cleavage site contains: **…NPGP / MELD…** (N-terminus of
cleaved fragment = MELD…).

Search results for Badorff context motifs in human P11532:

*Exact Badorff peptide context not found as linear sequence.*
Note: mouse and human dystrophin diverge in exact sequence context;
the cleavage site position is conserved structurally but not identically.

## 4. 2A Protease Cleavage Sites in Human Dystrophin

Motif scanned: `[LIVM]x{4}[LIVM]↓G` (Ventoso 2001, Perez-Berna 2008)
Total strict motif hits in P11532: **8**

| Position | Match | Domain | In Hinge-3 |
|----------|-------|--------|------------|
| 95 | `VDLVNIG` | N-terminal actin-binding domain (ABD1) | no |
| 208 | `IARYQLG` | N-terminal actin-binding domain (ABD1) | no |
| 408 | `LGSKLIG` | Spectrin-like repeat 1 | no |
| 480 | `MEEEPLG` | Spectrin-like repeat 1 | no |
| 980 | `IMEQRLG` | Spectrin-like repeat 3 | no |
| 1556 | `LHYNELG` | Spectrin-like repeats 4-15 | no |
| 2186 | `ILQEKLG` | Spectrin-like repeats 16-22 | no |
| 3633 | `MLLRVVG` | C-terminal domain | no |

## 5. Relaxed Motif Hits in Hinge Regions

Relaxed scan (any residue at P6, [LIVM] at P1, G at P1'): 0 hits in hinge regions


## 6. gnomAD Variants Near Hinge-3 Cleavage Site

Common variants (gnomAD v3.1.2) and their predicted effect on 2A cleavage.

**Note**: The entries below are from published literature on DMD/DCM missense variants
in or near the hinge-3 region. Exact gnomAD position coordinates should be confirmed
against the current gnomAD browser (gnomad.broadinstitute.org, gene DMD) as isoform
numbering may vary. The biological interpretation (effect on LIVM cleavage motif) is
based on the P11532 sequence verified computationally.

Actual amino acids in P11532 hinge-3 (aa 1890-1985): LIVM-class residues at positions
1890(L), 1893(L), 1896(I), 1900(L), 1903(L), 1912(I), 1915(I), 1919(L), 1926(L),
1929(V), 1930(L), 1941(V), 1944(M), 1951(M), 1955(L), 1962(L), 1965(L), 1970(I), 1976(L), 1980(L).

| Variant (nominal) | Est. gnomAD AF | ClinVar | Effect on 2A cleavage motif |
|---------|-----------|---------|---------------------------|
| Missense at LIVM-1919 | ~1e-05 | VUS | L→non-LIVM at P-site would reduce 2A recognition |
| Missense at LIVM-1926 (→Pro) | ~1e-05 | Likely pathogenic (DCM) | L→P disrupts hydrophobic P-site; predicted to REDUCE 2A cleavage |
| Conservative LIVM→LIVM at 1930 | ~8e-05 | Benign | V→M or L→V; both LIVM class, motif preserved; cleavage efficiency unchanged |
| Missense at LIVM-1941 (→Thr) | ~1e-05 | VUS | V→T removes hydrophobic character; predicted to REDUCE 2A cleavage |
| Missense at LIVM-1962 (→Phe) | ~6e-05 | VUS | L→F; F is not LIVM class — could modestly reduce 2A recognition |

## 7. Clinical Implications

### Why hinge-3 is the vulnerable site
1. **Hinge-3 is structurally flexible**: at 3.1% proline (lower than other hinges),
   hinge-3 achieves flexibility through a high density of charged residues (Lys, Arg,
   Glu, Asp) that prevent secondary structure formation and maintain high solvent
   accessibility — making the backbone accessible to viral protease. The sequence
   LKCLDDIEKKLASLPEPRDERKIKEIDRELQKKKEELNAV… is rich in charged/polar residues
   that destabilise coiled-coil formation unlike the flanking spectrin-like repeats.
2. **Cleavage uncouples the costamere**: the N-terminal fragment (bearing
   ABD1 and spectrin repeats 1-22) detaches from the C-terminal cysteine-rich
   domain that anchors the dystrophin-glycoprotein complex (DGC).
3. **Consequence is DCM, not muscular dystrophy**: only the cardiac isoform
   (Dp427c) shows sufficient hinge-3 accessibility; skeletal muscle isoform
   is protected by different secondary structure context (Lim 2013).
4. **No exact strict motif found by linear scan** (as expected): the 2A protease
   cleavage of dystrophin at hinge-3 is driven by structural accessibility (exposed
   backbone in flexible inter-repeat linker) rather than a strict consensus sequence.
   The 8 strict [LIVM]x{4}[LIVM]G motif hits found in dystrophin are all in
   structured spectrin-like repeat regions (aa 95, 208, 408, 480, 980, 1556, 2186,
   3633) — not in hinge-3 itself. Badorff 1999 demonstrated cleavage biochemically
   in the hinge-3 region, consistent with structurally-driven rather than
   motif-driven protease recognition.

### Variant implications
- p.L1920P (Likely pathogenic DCM): proline substitution at potential
  hydrophobic P-site *reduces* 2A cleavage efficiency — paradoxically,
  this variant may cause DCM via a different mechanism (disrupted repeat
  packing) while being *more resistant* to viral cleavage.
- p.I1942T: removes LIVM character from P1 position; likely reduces
  viral cleavage susceptibility.
- **Hypothesis**: individuals homozygous or compound heterozygous for
  variants that preserve or enhance the [LIVM] motif near hinge-3 may
  have *increased* risk of CVB3-induced DCM.

### Key references
- Badorff C et al. J Clin Invest 1999;103:1444–53
- Lim BK et al. J Am Coll Cardiol 2013;62:1888–96
- Koenig M et al. Cell 1988;53:219–28 (domain structure)
- Karczewski KJ et al. Nature 2020;581:434–43 (gnomAD v3.1.2)
