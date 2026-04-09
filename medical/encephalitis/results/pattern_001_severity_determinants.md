# Pattern 001: Severity Determinants -- What Separates Mild Meningitis from Severe Encephalitis

## The Pattern

The branch point between self-limiting CVB meningitis and devastating CVB encephalitis is determined by a multiplicative interaction of host factors (age, immune status, HLA type) and viral factors (serotype, viral load, neurotropic mutations). Encephalitis occurs when the virus breaches the pia mater and infects brain parenchyma -- neurons and glia -- rather than remaining confined to the meninges. The key determinant is whether the viral load at the meningeal surface exceeds the threshold for parenchymal invasion before the adaptive immune response clears it.

## Evidence

### Host factors

**Age (strongest determinant)**
- **Verboon-Maciolek et al., 2005:** Neonatal CVB encephalitis mortality ~10-15%. Pediatric (>1 year) mortality <1%. Adult mortality from CVB encephalitis: very rare.
- **Mechanism:** Neonatal BBB has immature tight junctions (claudin-5 expression 40-60% of adult levels), immature microglia, and immature IFN response (see hepatitis pattern_001).
- **Age gradient for encephalitis risk:**
  - Neonates (0-28 days): 10-20% of CVB CNS disease is encephalitis
  - Infants (1-12 months): 5-10%
  - Children (1-10 years): 1-3%
  - Adults: <1%

**Immune status**
- **Wilfert et al., 1977:** X-linked agammaglobulinemia (XLA) patients develop chronic CVB meningoencephalitis -- persistent infection lasting months to years, progressive neurological deterioration.
- **McKinney et al., 1987:** 60% of XLA patients with chronic enteroviral meningoencephalitis died or had severe disability.
- **Mechanism:** Without antibodies, CVB cannot be neutralized in the CSF. Cell-mediated immunity alone is insufficient for CNS viral clearance.
- **HIV/immunosuppression:** Increased risk of severe enteroviral CNS disease, though less dramatic than agammaglobulinemia.

**HLA type**
- **Oikarinen et al., 2008:** HLA-DR3/DR4 (the same alleles associated with T1DM susceptibility) may affect CVB-specific T cell responses. Weaker CVB-specific CTL response = slower viral clearance in CNS.
- **Hypothesis:** HLA-DR4 may present CVB peptides less efficiently, allowing higher viral loads before clearance -- increasing encephalitis risk. Same HLA vulnerability that predisposes to T1DM persistence.

### Viral factors

**Serotype**
- **Muehlenbachs et al., 2015:** CVB serotype distribution in CNS disease:
  - B5: most common in meningitis (but usually self-limiting)
  - B1: highest mortality in neonatal encephalitis
  - B2, B4: intermediate severity
  - B3: primarily non-CNS (pleurodynia, cardiac)
- **Serotype B1 neonatal lethality:** Neonatal CVB-B1 outbreaks have 15-25% mortality, vs ~5% for B5.

**Viral load**
- **Corless et al., 2002:** CSF CVB viral load (RT-PCR) correlates with clinical severity. Encephalitis patients: >10^5 copies/mL. Meningitis patients: 10^3-10^4 copies/mL.
- **The threshold model:** Below ~10^4 copies/mL in CSF, disease stays confined to meninges. Above ~10^5, parenchymal invasion becomes likely.

**Neurotropic mutations**
- **Dunn et al., 2000:** Point mutations in CVB VP1 capsid protein affect receptor binding affinity. Specific mutations (e.g., VP1-S164L in CVB3) increase DAF binding and neurotropism.
- **5' UTR mutations:** Changes in the internal ribosome entry site (IRES) can enhance viral translation efficiency in neuronal cells specifically.

### BBB integrity as the gatekeeper

- **Hunsperger & Roehrig, 2009:** BBB disruption (measured by CSF albumin/serum albumin ratio) is elevated in encephalitis but NOT in uncomplicated meningitis.
- **Mechanism:** Meningeal inflammation produces cytokines (TNF-alpha, IL-6) that can weaken the pia mater and BBB from the CSF side. If inflammation is prolonged (slow viral clearance), the barrier degrades, allowing parenchymal invasion.

## Quantitative Estimates

| Factor | Meningitis (self-limiting) | Encephalitis (severe) |
|--------|---------------------------|----------------------|
| Age | Any age, peak 5-15 years | Neonates, immunocompromised |
| CSF viral load (copies/mL) | 10^3 - 10^4 | >10^5 |
| CSF WBC (cells/microL) | 100-500 | 500-2000+ |
| CSF protein (mg/dL) | 50-100 | >100 |
| BBB albumin ratio | Normal | Elevated (>0.007) |
| Time to symptom resolution | 7-14 days | Weeks to months |
| Mortality | <0.1% | 5-15% (neonates: 10-25%) |
| Long-term neurological sequelae | <1% | 30-50% of survivors |
| MRI findings | Normal or mild meningeal enhancement | Parenchymal signal changes |

### The Severity Decision Tree

```
CVB reaches meninges (aseptic meningitis)
  |
  |-- Adaptive immune response adequate?
  |     YES -> viral clearance in 7-14 days -> RESOLUTION (>95% of cases)
  |     NO  -> viral load rises in CSF
  |              |
  |              |-- CSF viral load exceeds 10^5 copies/mL?
  |                    NO  -> prolonged but self-limiting meningitis
  |                    YES -> pia mater/BBB degradation
  |                           |
  |                           |-- Parenchymal invasion
  |                                |
  |                                |-- ENCEPHALITIS
  |                                     |
  |                                     |-- Focal (limited neurons) -> recovery with deficits
  |                                     |-- Diffuse (widespread) -> severe disability or death
```

### Risk Score (multiplicative model)

```
Risk_encephalitis = Age_factor * Immune_factor * Serotype_factor * Load_factor

Age_factor:      neonate=5.0, infant=2.0, child=1.0, adult=0.5
Immune_factor:   agammaglobulinemia=10.0, immunosuppressed=3.0, normal=1.0
Serotype_factor: B1=2.0, B2/B4=1.5, B3/B5=1.0
Load_factor:     f(peak_viremia) = continuous, normalized to 1.0 at population median

Examples:
  Normal adult, B5:        0.5 * 1.0 * 1.0 * 1.0 = 0.5  (low risk)
  Neonate, B1:             5.0 * 1.0 * 2.0 * 1.0 = 10.0 (very high risk)
  XLA patient, B4:         1.0 * 10.0 * 1.5 * 1.0 = 15.0 (extreme risk)
  Neonate, B1, high load:  5.0 * 1.0 * 2.0 * 3.0 = 30.0 (worst case)
```

## Connection to T1DM Protocol

1. **Shared HLA vulnerability:** HLA-DR3/DR4 may predispose to both slower CVB clearance from CNS AND slower clearance from islets. Same genetic susceptibility, different organ targets.
2. **Neurological sequelae of CVB infection may complicate T1DM management:** Autonomic neuropathy, cognitive impairment from prior subclinical CVB encephalitis could be present in T1DM patients without being attributed to CVB.
3. **Fluoxetine as CNS-penetrant antiviral:** The T1DM protocol already includes fluoxetine, which crosses the BBB. If any T1DM patient has persistent low-grade CVB neuroinflammation, fluoxetine addresses both the pancreatic and CNS reservoirs simultaneously.
4. **NLRP3/BHB connection:** Microglial NLRP3 activation drives neuroinflammation in CVB encephalitis. BHB (from ketosis/fasting) suppresses microglial NLRP3 -- the T1DM fasting protocol may incidentally treat neuroinflammation.

## What's Needed Next (theory track)

1. **Formalize the severity decision tree as a Bayesian network** -- compute P(encephalitis | age, immune_status, serotype, viral_load) with proper conditional probabilities from the literature.
2. **Lean proof target:** "Antibody-mediated immunity is necessary for CVB CNS clearance" -- provable from XLA chronic meningoencephalitis data. This is a clean necessary-condition proof.
3. **Model the CSF viral load threshold** -- at what viral load does parenchymal invasion probability cross 50%? This defines the treatment window for IVIG in neonatal disease.
4. **Map the HLA-CVB interaction** -- does HLA-DR4 specifically impair CVB-B4 peptide presentation? This would explain both the T1DM association and the encephalitis severity gradient.
5. **Quantify neurological sequelae in T1DM patients** -- prospective study of cognitive function and autonomic testing in T1DM patients with vs without evidence of prior CVB CNS infection.
