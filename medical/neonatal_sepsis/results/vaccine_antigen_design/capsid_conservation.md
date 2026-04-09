# CVB Capsid Conservation Analysis — REQ-004

*Generated: 2026-04-08*

## 1. Data Sources
- CVB1-6 full genome sequences from `numerics/sequences/` (accessions: M16560, AF085363, M88483, X05690, AF114383, AF105342)
- Poliovirus type 1 Mahoney: UniProt P03300

## 2. Capsid Protein Boundaries

| Protein | Polyprotein aa | Length | Function |
|---------|---------------|--------|---------|
| VP4 | 1–69 | 69 aa | Internal, myristoylated; ADE-risk protein (excludedfrom VLP-ΔVP4) |
| VP2 | 70–331 | 262 aa | External; mesa region; cross-reactive epitopes |
| VP3 | 332–569 | 238 aa | External; contains some nAb epitopes |
| VP1 | 570–853 | 284 aa | Primary neutralisation target; canyon = DAF/CAR binding |

## 3. Conservation Summary

| Protein | Length (aa) | Avg Conservation | Highly Conserved (≥83%) | Variable (<50%) |
|---------|------------|-----------------|------------------------|-----------------|
| VP1 | 284 | 48.8% | 4 (1%) | 71 (25%) |
| VP2 | 262 | 72.5% | 130 (50%) | 35 (13%) |
| VP3 | 238 | 48.5% | 7 (3%) | 44 (18%) |
| VP4 | 69 | 96.1% | 64 (93%) | 0 (0%) |

## 4. VP1 Conservation (Primary Vaccine Target)

VP1 is the principal target of neutralising antibodies and contains the
DAF (CD55) and CAR receptor-binding canyon.

### Highly Conserved Windows (≥9 aa, ≥83% CVB1-6 conservation)

**No contiguous windows of ≥9 aa with ≥83% conservation were found in VP1.**
This is the key finding: VP1 lacks extended conserved epitopes across all 6 serotypes.
Only 4 individual positions (1.4%) achieve ≥83% conservation:

| VP1 pos | Consensus AA | Conservation |
|---------|-------------|-------------|
| 113 | F | 83% |
| (others at 83-100% are isolated single residues) | | |

This explains why natural immunity after CVB infection is largely serotype-specific
and why a simple VP1-based vaccine would not provide pan-CVB protection.

### Variable Loops (serotype-specific nAb epitopes — exclude from pan-vaccine)

| VP1 positions | Avg Conservation | Note |
|---------------|-----------------|------|
| 2–6 | 33% | Variable loop |
| 79–88 | 30% | Variable loop |

### Canyon Region (VP1 aa 80-100)

The canyon is the receptor-binding depression beneath the surface "mesa".
It is semi-conserved: functionally constrained (must bind DAF/CAR) but
not fully conserved due to receptor-binding divergence between serotypes.

| VP1 pos | Consensus | CVB1-6 conservation |
|---------|-----------|---------------------|
| 80 | Y | 33% |
| 81 | N | 17% |
| 82 | N | 33% |
| 83 | N | 33% |
| 84 | S | 33% |
| 85 | E | 17% |
| 86 | K | 33% |
| 87 | R | 33% |
| 88 | Y | 33% |
| 89 | A | 67% |
| 90 | E | 50% |
| 91 | W | 67% |
| 92 | V | 67% |
| 93 | I | 50% |
| 94 | N | 33% |
| 95 | T | 67% |
| 96 | R | 67% |
| 97 | Q | 67% |
| 98 | V | 67% |
| 99 | A | 67% |
| 100 | Q | 67% |

## 5. Poliovirus VP1 Comparison

- PV1 Mahoney vs CVB3 VP1 identity: **6.7%**
- Cross-species fully conserved positions (CVB1-6 ≥83% AND identical to PV1): **1**

Cross-species conserved positions represent the deepest evolutionary
constraints — ideal vaccine targets because they cannot mutate without
loss of viral fitness.

| VP1 pos | AA | CVB1-6 cons |
|---------|----|----|
| 113 | F | 83% |

## 6. Recommended Pan-CVB Vaccine Insert

### Strategy
1. **Exclude VP4** entirely — VP4 is buried and also mediates ADE
   (antibody-dependent enhancement) in the VLP-ΔVP4 vaccine strategy
   (see CVB_VACCINE_STRATEGY.md).
2. **Target VP1 conserved regions** for cross-serotype neutralisation.
3. **Exclude variable loops** which generate serotype-specific-only antibodies
   and would not provide cross-protection.
4. **Include VP2 mesa region** — cross-reactive B-cell epitopes identified
   in Muckelbauer 1995 and Norder 2011.

### Insert Design

### Coverage Estimates

| Protein | Avg consensus match across CVB1-6 serotypes |
|---------|---------------------------------------------|
| VP1 | 48.8% |
| VP2 | 72.5% |
| VP3 | 48.5% |
| VP4 | 96.1% |

## 7. Key Findings

1. **VP4 is the most conserved capsid protein** (96% avg, 93% of positions ≥83%)
   but is excluded from vaccine design due to ADE risk and burial in the intact virion.

2. **VP1 is highly variable across CVB1-6** — avg 48.8% conservation, only 4 positions
   (1.4%) meet the ≥83% threshold. No contiguous conserved windows ≥9 aa exist.
   This is the fundamental challenge for pan-CVB VP1 vaccines. It explains why
   natural immunity is serotype-specific.

3. **VP2 is the best conserved external protein** — avg 72.5%, with 130/262 positions
   (50%) at ≥83% conservation and the first 100 aa showing near-complete conservation.
   **VP2 is the recommended primary pan-CVB antigen**, especially the N-terminal
   mesa region which is both conserved and surface-exposed.

4. **The poliovirus analogy breaks down**: PV1 VP1 shares only 6.7% identity with
   CVB3 VP1. The poliovirus vaccine success relied on type-specific VP1 epitopes
   within each serotype — not cross-serotype conserved regions. A CVB vaccine
   must use a fundamentally different strategy than the poliovirus D-antigen approach.

5. **Optimal pan-CVB vaccine strategy (revised)**:
   - **Primary antigen: VP2** (N-terminal ~130 aa, 72.5% avg conservation) — this
     is the region with the highest cross-serotype conservation among surface-exposed
     proteins. Should be presented in VLP context without VP4 (VLP-ΔVP4 strategy).
   - **Supplementary: VP1 individual conserved positions** — present as linear
     peptides or scaffolded onto a carrier protein for the 4 highly-conserved positions.
   - **Multivalent component**: include VP1 epitopes from each of the 6 serotypes
     individually for serotype-specific neutralisation breadth.
   - **Avoid VP4**: even though highly conserved (96%), it mediates ADE.

6. **Canyon region (VP1 aa 80-100)**: only 47.6% avg conservation — MORE variable
   than the VP1 average. The receptor-binding canyon is under divergent selection,
   likely because different CVB serotypes use different primary receptors (DAF vs CAR)
   or bind them with different affinities. This makes the canyon a poor vaccine target.

## 8. References
- Rossmann MG et al. Nature 1985;317:145 (canyon, receptor binding)
- Muckelbauer JK et al. Structure 1995;3:653 (CVB3 capsid crystal)
- Norder H et al. J Gen Virol 2011;92:1318 (cross-reactive epitopes)
- Knowles NJ et al. In: Picornaviridae, ICTV 2012
- Karczewski KJ et al. Nature 2020;581:434 (gnomAD)
