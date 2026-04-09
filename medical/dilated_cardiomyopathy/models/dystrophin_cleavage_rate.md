# Model: Dystrophin Cleavage Rate — The DCM Clock

## The Core Equation

```
d(D)/dt = k_synth - k_cleave × [2A] × D

Where:
  D = fraction of intact dystrophin per cardiomyocyte (0 to 1)
  k_synth = dystrophin synthesis rate (constitutive, ~0.02/day in healthy cells)
  k_cleave = 2A protease catalytic rate for dystrophin hinge 3
  [2A] = 2A protease concentration (function of TD mutant load)
```

## Three Regimes

### Regime 1: No Infection (healthy heart)
```
[2A] = 0
d(D)/dt = k_synth > 0
D = 1.0 (steady state — full dystrophin complement)
DGC complex intact, sarcolemma stable
```

### Regime 2: Acute Infection (wild-type CVB)
```
[2A] = HIGH (10⁸ virions/g → massive 2A production)
k_cleave × [2A] >> k_synth
d(D)/dt << 0
D drops rapidly (hours to days)
DGC collapses → sarcolemma tears → cardiomyocyte death (acute myocarditis)
```

### Regime 3: Persistent Infection (TD mutants — THE DCM REGIME)
```
[2A] = LOW but nonzero (TD mutants replicate 100,000x slower)
k_cleave × [2A] ≈ k_synth (approximately balanced)

If k_cleave × [2A] slightly > k_synth:
  D declines SLOWLY (months to years)
  DGC partially intact → sarcolemma weakened but functional
  Each contraction cycle: small probability of tear at weakened sites
  CUMULATIVE over thousands of daily contractions:
    Some cardiomyocytes die → replaced by fibrosis
    Surviving cardiomyocytes compensate (hypertrophy)
    Until compensation fails → clinical DCM

If k_cleave × [2A] slightly < k_synth:
  D stable or slowly recovering
  Heart compensates indefinitely → subclinical, never progresses
  THIS MAY EXPLAIN WHY NOT ALL CVB PERSISTENCE → DCM
```

## The Threshold Model

```
D_critical = ~0.5 (estimated)

Above D_critical: DGC mostly intact, sarcolemma stable, cardiomyocyte survives
Below D_critical: DGC too disrupted, sarcolemma tears during contraction → cell death

The rate at which D crosses D_critical determines:
  - Time from infection to clinical DCM (years to decades)
  - Whether clinical DCM develops at all
  - Response to antiviral therapy (if D hasn't crossed threshold, full recovery possible)
```

## What Determines [2A]?

```
[2A] = f(TD_mutant_load × translation_efficiency)

TD_mutant_load depends on:
  1. Initial wild-type viral load (more virus → more TD mutant generation events)
  2. Host immune response (NK cells, IFN → clear some TD mutants)
  3. Autophagy rate (higher autophagy → fewer surviving TD mutants)
  4. Time since infection (TD mutants are stable — they accumulate)

translation_efficiency:
  TD mutants have disrupted 5' cloverleaf → IRES-dependent translation
  Translation is SLOWER but NOT ZERO
  2A is still produced — just at lower rate
  Rate is sufficient to exceed dystrophin synthesis over months/years
```

## Intervention Points on the Model

| Intervention | Effect on equation | Timescale |
|-------------|-------------------|-----------|
| Fluoxetine | Blocks 2C ATPase → TD mutant replication stops → [2A] decays as existing virus degrades | Weeks (viral RNA half-life) |
| FMD/autophagy | Clears TD mutant-harboring cells → [2A] drops | Days (per FMD cycle) |
| SGLT2i | Enhances autophagy → [2A] drops; also anti-fibrotic | Continuous (daily) |
| Hypothetical 2A inhibitor | k_cleave → 0 regardless of [2A] → D recovers immediately | Hours (direct enzyme inhibition) |
| No intervention | [2A] stays constant → D slowly declines → DCM progresses | Years |

## The Recovery Prediction

If CVB is cleared (fluoxetine + autophagy → [2A] → 0):
```
d(D)/dt = k_synth > 0 (positive!)

D recovers at rate k_synth ≈ 0.02/day
Time to full dystrophin recovery: ~50 days

IF D had not crossed D_critical in most cardiomyocytes:
  DGC reassembles → sarcolemma stabilizes → no more cell death
  Existing fibrosis remains but doesn't progress
  Heart function stabilizes or improves (reverse remodeling)

IF D had crossed D_critical in many cardiomyocytes:
  Those cells are already dead → replaced by fibrosis
  Remaining cells recover → partial improvement
  Need anti-fibrotic + possibly regenerative therapy for full recovery
```

## The Measurable Proxy

We can't directly measure dystrophin in vivo without biopsy. But:

```
Troponin-I release = f(cardiomyocyte death rate) = f(sarcolemma tear rate)
                   = f(D approaching D_critical in individual cells)

PREDICTION:
  Pre-treatment: low-grade persistent troponin elevation (hsTnI 10-50 ng/L)
  During treatment: troponin normalizes as [2A] drops and D recovers
  Post-treatment: troponin stable at normal (<14 ng/L)

  Troponin trajectory is the surrogate for dystrophin recovery.
```

## Connection to Duchenne Muscular Dystrophy

DMD is caused by genetic dystrophin ABSENCE (mutations in DMD gene).
CVB-DCM is caused by dystrophin CLEAVAGE (2A protease cuts functional protein).

Key difference: in DMD, dystrophin is never made. In CVB-DCM, dystrophin IS made but is continuously destroyed.

**This means CVB-DCM is REVERSIBLE if the protease is stopped.**
DMD is not reversible (without gene therapy).

CVB-DCM patients who clear the virus should see dystrophin recovery and DGC reassembly.
DMD patients cannot — their gene doesn't make the protein.

This is profoundly hopeful: CVB-DCM, unlike genetic DCM, has a clearable cause.
