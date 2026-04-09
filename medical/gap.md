# Campaign Gap — After EVEN + ODD Instance Convergence

## Previous Gap (pre-ODD)
"The protocol is mechanistically sound but clinically unproven. The three data points needed are: the patient's C-peptide, pericarditis trial, fluoxetine PK modeling."

## Current Gap (post-ODD, post-IC50 reconciliation)

The numerical track built the computational framework. The IC50 reconciliation resolved the biggest model divergence. The gap has narrowed to TWO remaining uncertainties:

### Gap 1: Subcellular pharmacology of fluoxetine in CVB-infected cells
**What**: fluoxetine concentrates intracellularly via lysosomotropic trapping. But CVB remodels intracellular membranes to create replication organelles. Does fluoxetine accumulate NEAR the 2C ATPase target (good) or get trapped in lysosomes AWAY from it (bad)?

**Why it matters**: determines whether the IC50 reconciliation (which assumes fluoxetine reaches the target) is correct. If fluoxetine is lysosomally trapped away from viral ROs, effective concentrations may be lower than calculated.

**How to close it**: fluorescent fluoxetine analog + CVB-infected cells + confocal microscopy → co-localization with VP1 or dsRNA markers. One experiment.

**Impact if wrong**: fluoxetine arm weakens. Autophagy arm and anti-inflammatory arm still work. Protocol degrades from 8/8 organ clearance to 6/8 (muscle and gut, which are autophagy-dependent anyway).

### Gap 2: Clinical validation (unchanged)
**What**: no human has been treated with the full protocol. the patient's C-peptide and the pericarditis trial remain the validation path.

**Why it matters**: all models are theoretical until a patient is measured.

**How to close it**: blood draw (C-peptide) and/or pericarditis RCT.

## What Is No Longer a Gap

| Former gap | Resolved by | Resolution |
|-----------|------------|-----------|
| Fluoxetine dose adequacy | IC50 reconciliation + ODD PK correction | 20mg sufficient for brain/liver/heart; 60mg for testes. Lysosomotropic accumulation explains high tissue concentrations. |
| Autophagy overwhelms hijacking | ODD unified model v2 | Autophagy alone clears 6/8 organs in the model. Combined with fluoxetine: 8/8. |
| Clearance order | ODD v2 + cross-validation | Liver → pericardium → heart → CNS → gut → pancreas → muscle → testes. Robust under parameter perturbation. |
| Multi-organ clearance | ODD unified model v2 | All 8 organs clear with full protocol. Female ~7 months, male ~9-18 months. |
| HLA risk stratification | ODD HLA model | DR3/DR4 paradox: protects heart while endangering pancreas. No HLA genotype universally protective. |
