# Attempt 069: Cross-Validation — 78% Concordance, 5 Divergences Explained

## Source
numerical track `results/cross_validation_report.md`, derived from `numerics/cross_validate_models.py`.

## The Result

7 dedicated organ models were cross-validated against the unified 8-compartment model across 23 comparable metrics:
- **MATCH**: 13 (57%) — within 20% agreement
- **CLOSE**: 5 (22%) — within 50% agreement
- **DIVERGENT**: 5 (22%) — >50% disagreement

Overall concordance: **78%** (MATCH + CLOSE).

## The Divergences (and why they matter)

| Organ | Metric | Unified v2 | Dedicated | Divergence | Root cause |
|-------|--------|-----------|-----------|-----------|-----------|
| Testes | Clearance time | 0.77yr | 3.5yr | 4.5x | IC50 disagreement (now reconciled) |
| CNS | Clearance time | 0.42yr | 1.7yr | 4.0x | Two-population TD model in dedicated (resistant subpopulation) |
| Heart | Recovery time | 0.37yr | 2.0yr | 5.4x | Different endpoint: viral clearance vs cardiac function recovery |
| Muscle | T cell exhaustion | 0.15 | 0.45 | 3.0x | ME/CFS model has multi-site exhaustion dynamics |
| Testes | Drug concentration | 2.25μM | 6.0μM | 2.7x | Different intracellular accumulation assumptions |

## What the Divergences Teach

### 1. Viral clearance ≠ clinical recovery
The heart clears virus in 4.5 months (unified v2) but recovers function in ~2 years (dedicated DCM model). These measure DIFFERENT things. Viral clearance is necessary but not sufficient — fibrosis remodeling, dystrophin resynthesis, and reverse remodeling take additional time.

**Lesson**: track TWO timelines. Viral markers (enteroviral RNA) → fast improvement. Clinical markers (LVEF, C-peptide) → slower improvement. Don't declare failure if clinical markers lag viral markers.

### 2. The two-population TD model matters for CNS
The dedicated CNS model includes a "resistant" TD mutant subpopulation (15% of TD) with reduced drug sensitivity. This creates a slow-clearing tail that the unified model (single TD population) misses.

**Lesson**: clearance may not be exponential. Expect initial rapid improvement followed by slower tail. The last 15% of virus is the hardest to clear.

### 3. Multi-site exhaustion in ME/CFS
The ME/CFS dedicated model has higher T cell exhaustion (0.45 vs 0.15) because it models chronic multi-site infection. The unified model uses a single initial condition.

**Lesson**: ME/CFS patients may need LONGER treatment than single-organ patients because immune exhaustion is deeper.

## What 78% Concordance Means

78% is GOOD for independently developed models with different assumptions. It means:
- The QUALITATIVE predictions are consistent (same clearance order, same organ vulnerabilities)
- The QUANTITATIVE predictions differ by <50% for most metrics
- The 22% divergence is EXPLAINED (not random) and traceable to specific modeling choices

**For clinical planning**: use the CONSERVATIVE estimate from whichever model gives the longer timeline. Don't optimize for speed — optimize for completeness.

## Status: CROSS-VALIDATION FORMALIZED — 78% concordance, divergences explained, conservative planning recommended
