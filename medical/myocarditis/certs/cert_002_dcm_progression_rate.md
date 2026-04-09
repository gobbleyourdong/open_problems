# Certificate 002: Viral Myocarditis to DCM Progression Rate

## Claim

Approximately 30-40% of biopsy-confirmed viral myocarditis cases progress to dilated cardiomyopathy (DCM). The remainder (~60-70%) resolve spontaneously with full or near-full recovery of ventricular function. Progression is associated with persistent viral genome detection and ongoing immune activation.

## Sources

1. **Caforio ALP, Pankuweit S, Arbustini E et al. (2013)** "Current state of knowledge on aetiology, diagnosis, management, and therapy of myocarditis: a position statement of the European Society of Cardiology Working Group on Myocardial and Pericardial Diseases." *Eur Heart J* 34:2636-2648. Reports ~30% progression to DCM in the European Myocarditis Registry.
2. **Mason JW, O'Connell the operator, Herskowitz A et al. (2003)** "A clinical trial of immunosuppressive therapy for myocarditis." *N Engl J Med* 332:269-275 (with 2003 long-term follow-up data). The Myocarditis Treatment Trial showed ~33% of patients developed DCM at long-term follow-up.
3. **Kuhl U, Pauschinger M, Seeberg B et al. (2005)** "Viral persistence in the myocardium is associated with progressive cardiac dysfunction." *Circulation* 112:1965-1970. Demonstrated that patients with persistent viral genomes in EMB had significantly worse outcomes: 40% progressed to DCM vs 15% of virus-negative patients.

## Cross-Verification

- **European cohorts**: ESC Working Group data (Caforio 2013) and German Heart Centre series (Kuhl 2005) independently report 30-40% progression.
- **North American cohorts**: Myocarditis Treatment Trial (Mason 1995/2003) reports ~33% progression, consistent with European data.
- **Virus-positive vs virus-negative**: Kuhl 2005 provides a critical sub-analysis: 40% progression in virus-positive vs 15% in virus-negative. This strongly supports the viral persistence mechanism.
- **Definition dependence**: The exact percentage depends on how "myocarditis" is defined (Dallas criteria vs immunohistochemical vs CMR-based), which accounts for the 30-40% range rather than a single number.
- **Natural history bias**: These numbers come from biopsy-confirmed cases (sicker population). The true population-wide progression rate may be lower if subclinical cases are included.

## Confidence

**MODERATE-HIGH** -- The 30-40% range is consistent across multiple large cohorts on two continents over 20+ years. The main uncertainty is definitional: biopsy-confirmed cohorts are inherently biased toward more severe cases. However, for the purpose of modeling CVB-induced DCM (our use case), these biopsied populations are the relevant denominator.

## Connection

This progression rate is the central parameter in the acute-to-chronic transition model (pattern_001). The 30-40% who progress represent the population in which TD mutants "win the race" against immune clearance. The complement (60-70% who resolve) represents successful clearance. This ratio constrains the TD mutant formation rate and immune clearance rate parameters in the ODE model. For the unified CVB thesis: if the same TD mutant formation occurs in pancreatic islets (CVB4), the analogous "progression rate" to T1DM should be estimable from these cardiac parameters with organ-specific adjustments.

## Numerical Values

| Parameter | Value | Units | Source |
|-----------|-------|-------|--------|
| Overall progression rate (myocarditis to DCM) | 30-40 | % | Caforio 2013, Mason 2003 |
| Progression rate (virus-positive EMB) | ~40 | % | Kuhl 2005 |
| Progression rate (virus-negative EMB) | ~15 | % | Kuhl 2005 |
| Spontaneous resolution rate | 60-70 | % | Derived (complement) |
| Time to DCM diagnosis from acute myocarditis | 5-15 | years (median ~10) | Hershberger 2013 |
| Risk ratio (virus-positive vs negative) | ~2.7 | dimensionless | Kuhl 2005 |

These values parameterize the branching probability in the acute-to-chronic transition model and calibrate the immune clearance efficiency parameter.
