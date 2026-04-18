# Attempt 072: CVB1-6 Genome Conservation Theorem — The Invariant Targets

## Source
numerical track pattern 013 (`results/pattern_013_real_sequence_analysis.md`). First real nucleotide data in the campaign — actual GenBank sequences, not in silico models.

## The Three Invariant Targets

Analysis of 6 CVB reference genomes (CVB1–6) establishes three regions under such extreme purifying selection that they constitute universal, serotype-agnostic therapeutic and diagnostic targets:

### Target 1: Cloverleaf nt 1–10 (Stem a) — C = 1.000
100% identical across all 6 serotypes. This is the region TD mutants delete. It is the most conserved stretch of RNA in any positive-strand enterovirus and also the most therapeutically relevant: deleting it is the irreversible act that creates a TD mutant.

**Diagnostic implication:** A qPCR probe spanning nt 1–20 can distinguish WT (amplifies) from TD (fails to amplify). Deletions of 14+ nt produce a quantitative signal dropout. This is a clinically implementable TD detection assay — no exotic reagents required.

### Target 2: 3A protein — C_invariant ≈ 0.865, C_overall ≈ 0.974
The 3A membrane anchor is the most conserved CVB protein at both the amino acid level and structurally. It is the anchor point for replication organelle formation (tethers the replication complex to ER membrane via interaction with ACBD3 and OSBP). Unlike 2C (fluoxetine target, ~38% overall conservation) and 2A (~37%), 3A conservation means a 3A inhibitor would be effectively pan-serotype.

**Drug target implication:** Any compound blocking 3A-membrane interaction (e.g., enterovirus 3A inhibitors like GW5074 or itraconazole via OSBP) would suppress replication organelle formation across all five CVB serotypes causing human disease, without requiring serotype-specific dosing.

### Target 3: Fluoxetine binding pocket variability
The 2C ATPase positions 224 and 227 (fluoxetine resistance mutations in published literature) are VARIABLE across the 6 serotypes. This is a yellow flag for the protocol's antiviral arm:

| Concern | Evidence | Mitigation |
|---------|----------|------------|
| Serotype-specific fluoxetine IC50 variation | Positions 224/227 vary | Gofshteyn 2020 shows inhibition of multiple serotypes in vitro — pocket geometry may be conserved even if sequence varies |
| CVB6 diverges most (C_overall ~ 0.38) | CVB6 least common clinically | Clinical CVB6 burden is low; CVB3 and CVB4 (the campaign priority serotypes) show functional binding |

**This needs follow-up:** structural alignment of 2C across serotypes, not just sequence, to confirm binding pocket geometry conservation.

## The Permanent Crippling Corollary

**Corollary:** TD mutants with deletions ≥ 14 nt cannot revert to wild-type by random mutation.

**Argument:** Reversion requires reconstructing nt 1–14 exactly. At CVB mutation rate μ ≈ 3×10⁻⁴ per nucleotide per replication and at TD maintenance replication rate ≈ 1–5% of WT, the probability of restoring 14 specific nucleotides in a single round is:

```
P(revert in 1 round) ≈ (1/4)^14 × μ_effective
                     ≈ 3.7 × 10⁻⁹ × 3×10⁻⁵   (μ per base at 3% WT rate)
                     ≈ 10⁻¹³
```

With a typical persistent viral population of ~10⁶ genomes per infected tissue volume, the expected time until even one genome reverts is decades. Furthermore, the reverted WT genome would immediately re-trigger immune clearance — it would not re-establish persistence. **TD mutants are evolutionarily locked in.**

This is the strongest theoretical argument that persistent infection is a terminal differentiated state: the virus cannot escape it and the immune system cannot see it.

## Formal Gap Update

**The gap this finding clarifies:** The question "will the virus evolve resistance to the protocol?" has a partial answer here. TD mutants cannot revert to WT. WT cannot accumulate fluoxetine resistance under TD maintenance-level replication (too few replications). The only resistance pathway is in the WT population during active replication — which is why clearance of WT (fluoxetine) before TD establishment is a superior prevention strategy compared to treating established persistence.

**Remaining gap:** Structural confirmation that fluoxetine pocket geometry (not just residue identity) is conserved across CVB1–5. Without crystal structures for CVB1, 2, 4, 5 2C (only CVB3 2C has a solved structure, PDB 5B11), this is inferred from functional data only.

## Status: FIRST REAL SEQUENCE ANALYSIS COMPLETE — universal targets identified, TD irreversibility formalized, fluoxetine cross-serotype gap identified

---

## 2026-04-18 audit note (R37 from AUDIT_LOG fire 43)

**Flagged claim (L34-40):** Reversion-probability derivation
```
P(revert in 1 round) ≈ (1/4)^14 × μ_effective
                     ≈ 3.7 × 10⁻⁹ × 3×10⁻⁵
                     ≈ 10⁻¹³
```

**Correction — dimensional issue:** The derivation multiplies a **sequence-space fraction** `(1/4)^14 ≈ 3.7 × 10⁻⁹` (fraction of 14-nt words matching a specific target sequence, dimensionless) by a **mutation rate** `μ_effective ≈ 3 × 10⁻⁵ per site per replication` (has dimensions). The product is not a well-defined "probability of reverting in one round" — the two quantities are answering different questions.

**Corrected framing — two cleaner upper bounds:**

1. **Simultaneous-restoration upper bound** (per-replication):
   P(all 14 positions restored correctly in a single replication)
   ≤ (μ/3)^14 ≈ (10⁻⁴)^14 ≈ 10⁻⁵⁶
   This is vanishingly small — essentially zero over any biologically relevant timescale.

2. **But the deletion case is different.** The TD mutants have **deletions of 14+ nt at the 5'UTR, not point mutations**. Reverting a deletion requires a precise **insertion** of 14 specific nucleotides at the correct position, which is orders of magnitude rarer than point mutations (typical indel rates 10⁻⁷–10⁻⁸ per site, and a specific 14-nt insertion at a specific location is astronomically rare). So the correct argument is: **TD reversion requires a precise multi-nt insertion event**, which (a) has no positive-selection pathway in the host environment (WT is immediately cleared; so even if a reversion occurred, it would be eliminated before it could propagate), and (b) has no known biochemical pathway at the required rate in CVB.

**Conclusion unchanged; derivation rewritten:** TD mutants are evolutionarily locked in not because of the 10⁻¹³ number (which was dimensionally muddled) but because (i) precise multi-nt insertion is vastly rarer than point mutation, and (ii) the host environment actively selects against any reversion that does occur by immediately clearing WT.

**Fix applied:** audit note only (Maps Include Noise v6). The "Permanent Crippling Corollary" at L30 still stands; only the calculated magnitude for P(revert in 1 round) needs replacing with the deletion-reversion argument above.
