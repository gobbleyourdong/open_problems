# Cross-Validation Report: Dedicated Models vs Unified v2

Date: 2026-04-08
Models compared: 7 dedicated organ models + 1 unified 8-compartment model

## Summary

- Comparable metrics: 23
- MATCH: 13 (57%)
- CLOSE: 5 (22%)
- DIVERGENT: 5 (22%)
- Overall concordance: 78%

**Assessment: Models are MOSTLY consistent. Some reconciliation needed.**

## Key Divergences

### Heart (DCM, long-term): Time to clear virus with treatment (full protocol)
- Dedicated: 2.0 years
- Unified v2: 0.37 years
- Analysis: IMPORTANT DIVERGENCE. The DCM model predicts ~2 years for meaningful cardiac recovery even with treatment, while unified v2 predicts viral clearance in 0.37 years. RECONCILIATION: These measure different things. Unified v2 measures VIRAL clearance (V+TD < 1). DCM model measures CARDIAC RECOVERY (EF 

### Skeletal Muscle (ME/CFS): T cell exhaustion at steady state
- Dedicated: 0.45 fraction (0-1)
- Unified v2: 0.15 fraction initial
- Analysis: The ME/CFS dedicated model predicts HIGHER exhaustion (0.45) than the unified v2 starting point (0.15). RECONCILIATION: The ME/CFS model focuses specifically on multi-site chronic infection where exhaustion is a central feature (Wherry 2015: multi-organ chronic infection drives exhaustion). The unif

### Testes (Orchitis): Effective fluoxetine concentration in testes at 20mg dose
- Dedicated: 6.0 uM (intracellular)
- Unified v2: 2.25 uM (effective)
- Analysis: IMPORTANT: Different IC50 values! The orchitis model uses IC50=10 uM (in vivo adjusted for protein binding etc), while unified v2 uses IC50=1.0 uM (in vitro cell culture, Zuo 2018). Despite the 2.7x difference in effective concentration, the Hill equation outputs are SIMILAR because of the compensat

### Testes (Orchitis): Time to clear testes with full protocol
- Dedicated: 3.5 years
- Unified v2: 0.77 years
- Analysis: MAJOR DIVERGENCE (4.5x difference). The orchitis dedicated model predicts ~3.5 years; the unified v2 predicts ~9 months. ROOT CAUSE: Different drug effect assumptions (see IC50 divergence above). The unified v2 has 69% drug inhibition in testes vs orchitis model's 22%. Also: the orchitis model has a

### CNS (Encephalitis): Time to clear CNS with full protocol
- Dedicated: 1.7 years
- Unified v2: 0.42 years
- Analysis: SIGNIFICANT DIVERGENCE (4x difference). Similar to the testes discrepancy. ROOT CAUSE: The dedicated CNS model has a two-population structure (85% sensitive + 15% resistant TD mutants) with resistant_drug_efficacy=0.25, creating a slow-clearing tail. The unified v2 has a single TD population with td

## Recommendations

1. Harmonize IC50 to 3-5 uM consensus (in vivo adjusted)
2. Add two-population TD model to unified v2 (sensitive + resistant)
3. Calibrate T cell exhaustion initial conditions per disease
4. Add structural recovery lag for heart compartment
