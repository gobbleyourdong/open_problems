# REQ-003: Dystrophin Hinge 3 Cleavage Site Analysis

## Date: 2026-04-09
## Source: ODD_INSTANCE_REQUESTS.md REQ-003

## Results

### Sequence retrieval
- Human dystrophin (UniProt P11532, DMD_HUMAN): **3685 amino acids**
- Full sequence retrieved successfully from UniProt REST API

### Hinge 3 region (AA 2027-2117, 91 residues)
```
2027: DFEDLFKQEESLKNIKDSLQQSSGRIDIIHSKKTAALQSATPVERVKLQEALSQLDFQWE
2087: KVNKMYKDRQGRFDRSVEKWRRFHYDIKIFN
```

Composition:
- Proline: **1.1%** (1/91) — NOT proline-rich as expected for a "hinge"
- Glycine: 2.2% (2/91) — low
- Charged (D+E+K+R): **36.3%** — highly charged, hydrophilic
- Hydrophobic (A+V+L+I+M+F+W): 33.0%

**Surprise: Hinge 3 is NOT a classic proline-rich flexible hinge.** It's a
charged, somewhat rigid region. The flexibility may come from the lack of
regular secondary structure rather than proline content.

### GxxG motif search
- Total GxxG motifs in full dystrophin: **3** (very few for a 3685 AA protein)
- GxxG motifs in Hinge 3 (AA 2027-2117): **0**
- GxxG motifs near known 2A cleavage site (AA 2286-2305): **0**

**The 2A protease does NOT use GxxG on dystrophin.** GxxG is the 2A
auto-catalytic motif (self-cleavage at the polyprotein), not the substrate
recognition motif. On dystrophin, 2A recognizes a different sequence context.

### Known 2A cleavage site (Badorff et al. 1999)
- Cleavage between AA 2295-2296
- Surrounding sequence (AA 2286-2305): **EEQDKLENKLKQTNLQWIKV**
- This is in the rod domain, DOWNSTREAM of Hinge 3
- The region is glutamate/lysine-rich (charged), not a canonical protease site

### Implications for drug design
1. **A 2A inhibitor must target the 2A active site** (on the viral protease),
   not a sequence motif on dystrophin. The substrate recognition is likely
   structural (3D fold) rather than sequence-based.
2. **Polymorphisms in the cleavage region** could affect susceptibility to
   CVB-induced DCM. Individuals with mutations at AA 2290-2300 might be
   resistant. This needs gnomAD/dbSNP cross-reference (next step).
3. **The Hinge 3 region itself is not the cleavage target** — it's 170 AA
   upstream. The cleavage disrupts spectrin-like repeat connections in the
   rod domain, not the hinge flexibility.

## Next steps
- [ ] gnomAD API query for polymorphisms at AA 2290-2300
- [ ] AlphaFold structure prediction for the cleavage region
- [ ] Literature search for 2A substrate specificity studies
- [ ] Cross-reference with REQ-001 (2A protease virtual screen)
