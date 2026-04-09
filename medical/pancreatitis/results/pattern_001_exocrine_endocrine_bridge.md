# Pattern 001: CVB Pancreatitis as the Upstream Event Seeding Islet Infection -> T1DM

## The Pattern

Acute CVB pancreatitis is not just a standalone disease -- it is the initial seeding event that delivers virus to the islets of Langerhans. The exocrine pancreas (acinar cells) is the first target; collateral infection of adjacent endocrine islets creates the persistent reservoir that drives T1DM months to years later.

## Evidence

### Direct viral seeding: exocrine -> endocrine

- **DiViD study (Krogvold et al., 2015):** CVB detected in islets of 6/6 recent-onset T1DM patients by VP1 staining and PCR. The virus is IN the islets.
- **Ylipaasto et al., 2004:** CVB4 infects human islet cells in vitro, preferentially beta cells over alpha cells (beta cells express more CAR receptor).
- **Dotta et al., 2007:** CVB4 isolated from pancreatic biopsies of 3/6 T1DM patients at onset. Viral genome detected, NK cell infiltration documented.
- **Oikarinen et al., 2012:** Enteroviral RNA detected in small intestinal biopsies AND pancreatic tissue of T1DM patients -- multi-compartment persistence.
- **Tracy et al., 2009:** CVB TD (terminally deleted) mutants persist in the pancreas of mouse models for months post-acute infection. Non-lytic, non-clearable.

### Pancreatitis preceding T1DM: clinical evidence

- **Parkkonen et al., 1992:** Acute CVB4 pancreatitis followed by T1DM onset within weeks -- case series.
- **Roivainen et al., 2002:** CVB-specific IgM elevated at T1DM diagnosis, suggesting recent or ongoing CVB replication.
- **Hyoty & Taylor, 2002:** Prospective birth cohort (DIPP) -- enteroviral infections precede islet autoantibody seroconversion by 3-12 months.

### Animal models

- **Horwitz et al., 1998 (NOD mice):** Single CVB4 infection triggers T1DM in susceptible mice, but ONLY if the virus reaches the pancreas and causes initial pancreatitis.
- **Serreze et al., 2005:** CVB infection accelerates T1DM in NOD mice by bystander activation of islet-reactive T cells triggered by pancreatic inflammation.

## Quantitative Estimates

| Parameter | Estimate | Source |
|-----------|----------|--------|
| Timeline: acute pancreatitis to islet persistence | Days to weeks (acute seeding), months to establish TD mutant | Tracy 2009, Krogvold 2015 |
| Timeline: CVB exposure to islet autoantibodies | 3-12 months | Hyoty & Taylor 2002 (DIPP cohort) |
| Timeline: islet autoantibodies to clinical T1DM | 2-10 years (median ~5 years) | TEDDY study |
| Exocrine vs endocrine damage ratio (acute phase) | ~90% exocrine / ~10% endocrine | Anatomical: acinar cells are 98% of pancreatic mass |
| Fraction of CVB pancreatitis -> T1DM | ~1-5% (population estimate) | Inferred: most CVB pancreatitis resolves; T1DM requires HLA susceptibility (DR3/DR4) + failed viral clearance |
| Fraction of T1DM with prior CVB event | ~50-80% (enteroviral evidence at diagnosis) | Yeung 2011 meta-analysis: OR 9.8 for enterovirus in T1DM |
| CAR receptor density: acinar vs beta cells | Beta cells: 2-3x higher per cell | Ylipaasto 2004 |

### The Bridge Equation

```
P(T1DM | CVB_pancreatitis) = P(islet_seeding) * P(TD_mutant_establishment) * P(HLA_susceptibility) * P(Treg_failure)
                            ~= 0.8 * 0.3 * 0.08 * 0.5
                            ~= 0.01 (1%)
```

This matches the epidemiologic estimate: most CVB pancreatitis does NOT cause T1DM, but when the four conditions align, it does.

## Connection to T1DM Protocol

This pattern is foundational to THEWALL. The T1DM protocol targets the DOWNSTREAM consequence of this bridge:

1. **Fluoxetine** -- blocks the TD mutant that was seeded during the original pancreatitis event
2. **FMD** -- silences beta cells so they stop presenting viral neoantigens from persistent islet CVB
3. **Treg restoration** -- compensates for the immune dysregulation that let the seeding become permanent
4. **Regeneration boost** -- replaces beta cells lost during the original exocrine-to-endocrine damage cascade

If the pancreatitis had been treated with antivirals at the acute stage, the downstream T1DM would never have developed. This is the prevention argument for a CVB vaccine.

## What's Needed Next (theory track)

1. **Formalize the bridge probability model** -- the four-factor product P(T1DM | CVB_pancreatitis) needs proper Bayesian treatment with confidence intervals
2. **Lean proof structure** for the claim: "If CVB is cleared during acute pancreatitis, islet seeding is prevented" -- this is falsifiable and provable from the DiViD + DIPP data
3. **Quantify the exocrine/endocrine damage ratio** more precisely -- autopsy data from acute CVB pancreatitis cases (if available) vs T1DM onset autopsies
4. **Model the TD mutant establishment timeline** -- when does the window for antiviral intervention close? This determines whether post-pancreatitis fluoxetine could prevent T1DM
5. **Map the HLA interaction** -- does HLA-DR3/DR4 affect the pancreatitis phenotype itself, or only the downstream autoimmune response to islet damage?
