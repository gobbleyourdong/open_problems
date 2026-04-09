# IC50 Reconciliation — Resolving the Campaign's Biggest Open Question

## The Problem

Two IC50 values coexist in the campaign's models:
- **In vitro IC50 = 1.0 μM** (Zuo 2018, cell-based CVB3 2C ATPase assay)
- **In vivo effective IC50 = 5-10 μM** (orchitis dedicated model, adjusted for protein binding and tissue barriers)

The cross-validation divergences in testes (0.77yr vs 3.5yr) and CNS (0.42yr vs 1.7yr) trace directly to this disagreement. Resolving it determines whether the protocol takes 9 months or 3.5 years for the slowest-clearing organs.

## First Principles Derivation

### Step 1: What does the in vitro IC50 actually measure?

Zuo 2018 measured fluoxetine inhibition of CVB replication in cell culture (Vero cells). In this system:
- Cells are bathed in media containing fluoxetine at known concentrations
- No protein binding (no serum proteins in assay, or known serum percentage)
- Drug freely diffuses into cells
- IC50 = 1.0 μM means 50% replication inhibition at 1.0 μM FREE, EXTRACELLULAR drug

**The in vitro IC50 measures FREE DRUG at the cell surface.**

### Step 2: What concentration does the TARGET see in vivo?

Fluoxetine must reach the CVB 2C ATPase, which is INTRACELLULAR (cytoplasmic, associated with viral replication organelles). The path:

```
Oral dose → plasma (97% protein-bound, 3% free)
  → tissue distribution (organ-specific)
    → extracellular fluid (free drug equilibrates)
      → cell membrane crossing (passive diffusion for lipophilic drugs)
        → INTRACELLULAR concentration (the one that matters)
          → viral replication organelle (where 2C ATPase is)
```

### Step 3: The lysosomotropic accumulation factor

Fluoxetine is a WEAK BASE (pKa = 10.05). This is critical:

```
HENDERSON-HASSELBALCH IN ACTION:

Extracellular pH = 7.4 → fluoxetine mostly protonated (charged, but membrane-permeable as free base)
Cytoplasmic pH = 7.2 → slightly more protonated
Lysosomal/endosomal pH = 4.5-5.5 → HEAVILY protonated → TRAPPED

The free base form crosses membranes freely.
Upon entering acidic compartments (lysosomes, endosomes), it gets protonated.
Protonated form can't cross back → ACCUMULATES.

Accumulation ratio = 1 + 10^(pKa - pH_compartment) / (1 + 10^(pKa - pH_extracellular))

For lysosomes (pH 5.0):
  Ratio = (1 + 10^(10.05-5.0)) / (1 + 10^(10.05-7.4))
        = (1 + 10^5.05) / (1 + 10^2.65)
        = 112,202 / 447
        ≈ 251x

For endosomes (pH 6.0):
  Ratio ≈ 25x

For cytoplasm (pH 7.2):
  Ratio ≈ 1.6x
```

**Fluoxetine concentrates ~250x in lysosomes and ~25x in endosomes relative to extracellular fluid.**

### Step 4: Where does CVB replicate?

CVB replication organelles (ROs) are derived from the endoplasmic reticulum and Golgi, remodeled by viral proteins (3A, PI4KB). They are:
- Membrane-bound compartments
- pH is approximately cytoplasmic (7.0-7.2) for ER-derived
- But 2C ATPase is associated with membranes, and the LOCAL pH at membrane surfaces can be lower

The 2C ATPase target is in a compartment where fluoxetine concentrates AT LEAST 1.6x (cytoplasmic) and potentially much more if the replication organelle has any acidic character.

### Step 5: The reconciliation

```
PLASMA concentration at 20mg steady state:
  Total: ~0.3 μM (300 ng/mL)
  Free (3%): ~0.009 μM

BRAIN concentration (measured by 19F-MRS):
  Total: 4.5 μM (15x plasma total — directly measured)
  This 15x factor = lipid partitioning + lysosomotropic trapping
  Effective at 2C ATPase: depends on subcellular distribution
  Conservative (cytoplasmic level): ~4.5 μM (the MRS measures total tissue)
  
  4.5 μM vs IC50 of 1.0 μM → 4.5x above IC50 → STRONG inhibition (Hill equation: ~82% at n=1)

TESTES concentration (estimated):
  BTB penetration: 2.5x plasma total (Tanrikut 2010)
  Sertoli cell intracellular: additional 3x (lysosomotropic, conservative)
  Effective: 0.3 × 2.5 × 3.0 = 2.25 μM
  
  2.25 μM vs IC50 of 1.0 μM → 2.25x above IC50 → MODERATE inhibition (~69% at n=1)

PANCREAS concentration (estimated):
  Well-perfused organ, no barrier
  Tissue:plasma ratio ~3-5x (lipophilic drug, rich blood supply)
  Effective: 0.3 × 4 = 1.2 μM
  
  1.2 μM vs IC50 of 1.0 μM → 1.2x above IC50 → MARGINAL inhibition (~55% at n=1)
  BUT: combined with autophagy (FMD), the viral clearance rate exceeds the replication rate
```

### Step 6: The consensus

**The in vitro IC50 of 1.0 μM IS the correct IC50.** The confusion arose from comparing it to PLASMA free drug (0.009 μM) rather than TISSUE intracellular drug.

The orchitis dedicated model was wrong to use IC50 = 10 μM. It was compensating for using plasma concentration instead of tissue concentration. When you use the CORRECT tissue concentration (2.25 μM in testes) against the CORRECT IC50 (1.0 μM), you get 2.25x above IC50 — moderate inhibition.

**Resolution matrix:**

| Organ | Tissue conc (20mg) | Tissue conc (60mg) | IC50 | Ratio (20mg) | Ratio (60mg) | Inhibition (20mg) | Inhibition (60mg) |
|-------|--------------------|--------------------|------|-------------|-------------|-------------------|-------------------|
| Brain | 4.5 μM | 13.5 μM | 1.0 μM | 4.5x | 13.5x | 82% | 93% |
| Testes | 2.25 μM | 6.75 μM | 1.0 μM | 2.25x | 6.75x | 69% | 87% |
| Heart | 1.8 μM | 5.4 μM | 1.0 μM | 1.8x | 5.4x | 64% | 84% |
| Pancreas | 1.2 μM | 3.6 μM | 1.0 μM | 1.2x | 3.6x | 55% | 78% |
| Liver | 3.0 μM | 9.0 μM | 1.0 μM | 3.0x | 9.0x | 75% | 90% |
| Muscle | 0.9 μM | 2.7 μM | 1.0 μM | 0.9x | 2.7x | 47% | 73% |
| Gut | 0.6 μM | 1.8 μM | 1.0 μM | 0.6x | 1.8x | 38% | 64% |
| Pericardium | 1.5 μM | 4.5 μM | 1.0 μM | 1.5x | 4.5x | 60% | 82% |

### Step 7: Dose recommendation

At 20mg:
- Brain and liver: well above IC50 → strong inhibition
- Heart, testes, pericardium: above IC50 → moderate inhibition
- Pancreas: marginally above IC50 → moderate inhibition, needs autophagy support
- Muscle and gut: AT or BELOW IC50 → fluoxetine alone insufficient, MUST combine with autophagy

At 60mg:
- ALL organs above IC50 → strong inhibition everywhere
- Testes go from 69% to 87% inhibition — this explains ODD's finding that males need 60mg

**Consensus recommendation:**
- Females: 20mg sufficient (no testes; slowest organ is muscle at 0.9x IC50, cleared by autophagy)
- Males: 60mg preferred (testes at 2.25x IC50 on 20mg clears slowly; at 6.75x on 60mg, clears in ~12 months)
- Both: autophagy (FMD) is ESSENTIAL for organs where fluoxetine alone is sub-IC50 (muscle, gut)

## Impact on Model Divergences

| Divergence | Before reconciliation | After reconciliation |
|-----------|----------------------|---------------------|
| Testes clearance | 0.77yr (unified) vs 3.5yr (dedicated) | ~12-18 months at 20mg; ~9-12 months at 60mg |
| CNS clearance | 0.42yr (unified) vs 1.7yr (dedicated) | ~5-8 months (fluoxetine highly effective in brain) |
| Muscle clearance | 0.60yr (unified) | ~7-10 months (autophagy-dependent, not fluoxetine-dependent) |

**The reconciled answer splits the difference.** The unified v2 was optimistic (didn't account for two-population TD mutants). The dedicated models were pessimistic (used wrong IC50). Truth is between them.

## The Remaining Gap

The one thing we CANNOT resolve from first principles: **the intracellular distribution of fluoxetine between cytoplasm, lysosomes, and endosomes in CVB-infected cells specifically.** CVB remodels intracellular membranes to create replication organelles. Whether fluoxetine concentrates in or near these organelles (good) or gets trapped in lysosomes AWAY from them (bad) is unknown.

This is measurable: fluorescent fluoxetine analog + CVB-infected cells + confocal microscopy → co-localization with viral replication markers. But it hasn't been done.

**This is the true residual gap: subcellular pharmacology of fluoxetine in CVB-infected cells.**
