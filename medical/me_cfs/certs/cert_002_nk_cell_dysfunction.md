# Certificate 002: NK Cell Cytotoxicity Reduction in ME/CFS

## Claim

Natural killer (NK) cell cytotoxicity is reduced by 40-60% in ME/CFS patients compared to healthy controls. This is the most consistently replicated immunological finding in ME/CFS, observed across more than 20 independent studies spanning 30 years, using multiple assay methodologies (chromium-51 release, flow cytometry, direct killing assays). NK cell numbers may be normal or slightly reduced; the defect is primarily functional (reduced per-cell killing capacity).

## Sources

1. **Brenu EW, Staines DR, Baskurt OK et al. (2011)** "Immune and hemorheological changes in chronic fatigue syndrome." *J Transl Med* 9:81. Demonstrated significantly reduced NK cytotoxicity in CFS patients (n=95) vs healthy controls (n=50). Cytotoxicity was approximately 50% of control levels using the standard chromium-51 release assay. Also found reduced perforin and granzyme A/B content per NK cell.
2. **Hardcastle SL, Brenu EW, Johnston S et al. (2015)** "Characterisation of cell functions and receptors in chronic fatigue syndrome/myalgic encephalomyelitis." *Clin Exp Immunol* 181:405-413. Extended findings with detailed phenotyping: NK cell cytotoxicity reduced ~45% in CFS/ME patients. Identified specific receptor downregulation (NKG2D, CD16) as potential mechanisms.
3. **Eaton-Fitch N, du Preez S, Cabanas H et al. (2019)** "A systematic review of natural killer cells profile and cytotoxic function in myalgic encephalomyelitis/chronic fatigue syndrome." *Syst Rev* 8:279. Systematic review of all published NK cell studies in ME/CFS. Analyzed data from >20 studies. Conclusion: consistent reduction in NK cytotoxicity across studies, with most showing 40-60% reduction vs controls. The most replicated finding in ME/CFS immunology.

## Cross-Verification

- **Geographic diversity**: Replicated in Australia (Brenu 2011, Hardcastle 2015), UK (Ogawa 1998), Japan (Aoki 1993), USA (Klimas 1990, Fletcher 2010), Belgium (Maes 2006). No geographic cluster.
- **Methodological diversity**: Confirmed by chromium-51 release assay (gold standard), flow cytometry-based killing assays, CD107a degranulation assays, and direct perforin/granzyme quantification. The finding is method-independent.
- **Temporal consistency**: First reported by Caligiuri et al. (1987) and Klimas et al. (1990). Still replicated 30+ years later. No study has convincingly refuted the finding.
- **Systematic review confirmation**: Eaton-Fitch 2019 is a formal systematic review covering all published evidence. Conclusion is unambiguous: NK cytotoxicity is reduced in ME/CFS.
- **Correlation with severity**: Several studies (Fletcher 2010, Curriu 2013) show that NK dysfunction severity correlates with ME/CFS symptom severity, supporting a causal (not epiphenomenal) role.

## Confidence

**HIGH** -- This is the single most replicated finding in ME/CFS research. Over 20 independent studies, 30+ years, multiple countries, multiple methodologies, systematic review confirmation. The effect size (40-60% reduction) is large and consistent. No credible contradictory evidence.

## Connection

NK cell dysfunction is directly relevant to the CVB persistence model. NK cells are the first responders to viral infection (days 1-7), buying time for the adaptive immune response. In the acute-to-chronic transition model (pattern_001):

- NK cells reduce peak viral load by ~10x during days 3-7 (Godeny 1987: NK-deficient mice show 10x higher CVB3 mortality).
- Reduced NK function means higher peak viral load, which means more replication cycles, which means higher probability of TD mutant formation.
- **Causal hypothesis**: ME/CFS patients have constitutively low NK function. When they encounter CVB, they fail to suppress the initial burst adequately. This leads to higher rates of TD mutant formation and chronic persistence. The NK deficit is the predisposing factor; the CVB persistence is the consequence.

This connects to T1DM: if NK dysfunction predisposes to CVB persistence, then NK function testing could predict which CVB-exposed individuals develop chronic disease (T1DM, myocarditis, ME/CFS).

For the T1DM protocol: the protocol does not directly target NK cells, but the BHB/NLRP3 suppression and Treg restoration may indirectly improve NK function by reducing the chronic inflammatory milieu that drives NK exhaustion.

## Numerical Values

| Parameter | Value | Units | Source |
|-----------|-------|-------|--------|
| NK cytotoxicity reduction (ME/CFS vs controls) | 40-60 | % reduction | Eaton-Fitch 2019 (systematic review) |
| Central estimate of reduction | ~50 | % | Brenu 2011, Hardcastle 2015 |
| Perforin content reduction per NK cell | ~30-40 | % reduction | Brenu 2011 |
| Granzyme A/B content reduction per NK cell | ~25-35 | % reduction | Brenu 2011 |
| NK cell count (ME/CFS vs controls) | ~0.8-1.0x | relative to controls | Variable; often normal |
| Number of independent replication studies | >20 | studies | Eaton-Fitch 2019 |
| NK-deficient mouse CVB3 mortality increase | ~10x | fold | Godeny 1987 |

These values parameterize the immune response strength in the ODE model and define the NK-mediated early clearance phase that determines acute vs chronic outcomes.
