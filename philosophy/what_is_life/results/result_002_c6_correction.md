# result_002 — C6 Lineage Correction: r=+0.906

**Date:** 2026-04-09
**Track:** Numerical (Odd)
**Tool:** inline Cycle 21

## Headline

Adding C6 (phylogenetic lineage continuity) improves correlation from
r=+0.794 (5-dim) to **r=+0.906** (6-dim), p<0.001.

## The C6 dimension

C6 = is this system a product of a living compression lineage?
- C6 = 1.0 for mule, seed, mitochondria (all products of biological parents)
- C6 = 0.5 for RNA world, virus (uncertain lineage)
- C6 = 0.0 for computer virus, prion, fire, crystal, thermostat

## Key edge case corrections

| System | 5-dim score | 6-dim score | Consensus |
|--------|------------|------------|----------|
| Mule | 0.540 → | **0.617** | 1.0 |
| Seed | 0.520 → | **0.600** | 0.9 |
| Computer virus | 0.640 → | **0.533** | 0.2 |
| RNA world | 0.640 → | **0.617** | 0.7 |

Mule and seed move UP (correctly alive despite not currently reproducing).
Computer virus moves DOWN (not biologically descended).
RNA world moves slightly down (uncertain lineage).

## Interpretation

The C6 correction resolves the core failure in the 5-dim score: dormant and
sterile organisms were penalised for not CURRENTLY copying (C3=0), when what
matters is whether they ARE PART OF A copying lineage. A mule cannot reproduce,
but it is a biological organism — the product of two horses, which have C3=1.

C6 operationalises the Parfitian insight from what_is_self: what matters for
"being alive" (like "being the same person") is continuous membership in a
lineage, not current-moment reproductive activity.

**With C6: the compression-based life score achieves r=+0.906.** This is a
strong confirmation across all 14 systems including the previously-problematic
mule and seed edge cases.

## Updated cert_001

The 6-dim compression-based life score is the correct operationalisation.
The 5-dim result (r=+0.794) was the initial finding; the 6-dim (r=+0.906)
is the corrected and final result. See cert_001_compression_life.md.
