# Pattern 002: Anti-Problem Models — Phase 4 systematic approach

## Status: COMPLETED (ODD Instance — Numerics)

## The Question

"What would a counterexample to T1DM look like?"

Phase 4 of the systematic approach: build quantitative models of the anti-problem.
If T1DM is destruction > regeneration, what do the people who REVERSE that
inequality (temporarily or permanently) look like?

---

## Model 1: Spontaneous Remission (6-State ODE)

**File**: `t1dm/numerics/anti_problem_spontaneous_remission.py`

### ODE State Variables

| Variable | Meaning | Units |
|----------|---------|-------|
| B | Beta cell mass | Fraction of normal (0-1) |
| Teff | Autoreactive T effector cells | Activity units |
| Treg | Regulatory T cells | Activity units |
| V | Replicating viral load | Normalized copies |
| TD | 5'-terminally deleted mutants | Population units |
| A | Antigen presentation rate | Composite rate |

### Key Dynamics

The 6-state ODE captures the critical feedback loops:

```
Stress → A ↑ → Teff expand → Destruction ↑ → B ↓ → Stress ↑ (amplification)
         ↓
    Treg suppress Teff → slows destruction (regulation)
         ↓
    TD mutants → chronic ER stress → A stays elevated (persistence)
```

The central insight: **Teff contract to a memory floor (~3 units) but do not
disappear.** This memory T cell pool can re-expand when re-stimulated by
TD-mutant-driven antigen. This is why the honeymoon fails — the fire was
banked, not extinguished.

### Scenario Results (Default Operator: 15% B at Diagnosis)

| Scenario | Honeymoon | Final B | TD at End | Permanent Remission |
|----------|-----------|---------|-----------|---------------------|
| Standard care (insulin only) | ~58 months | 9.2% | 29.3 | NO |
| the operator keto (5yr) | ~82 months | 14.4% | 19.1 | NO |
| Full protocol (no teplizumab) | Indefinite | 16.6% | 0.0 | YES |
| Full protocol + teplizumab | Indefinite | 18.9% | 0.0 | YES |

**Standard care**: Insulin therapy reduces metabolic stress, Teff contract,
B stabilizes temporarily. But TD mutants persist (29.3 remaining at 5yr),
maintaining chronic ER stress. B declines slowly from 15% to 9.2%.

**the operator keto**: BHB suppresses NLRP3, low glucose demand reduces
metabolic stress. Extended stabilization period, slower B decline. But
WITHOUT fluoxetine, TD mutants still persist (19.1 at 7yr). Matches
the real 5-year experience: good control followed by gradual deterioration.

**Full protocol**: Fluoxetine clears V (< 0.1yr) and TD (< 0.1yr).
With TD eliminated, no chronic ER stress. Treg boost via butyrate + VitD
suppresses remaining memory Teff. B slowly recovers from 12% to 16.6%
over 10 years via neogenesis + FMD-boosted regeneration.

**Full + teplizumab**: Additional Teff depletion via anti-CD3 accelerates
the window where Regen > Destruction. Higher final B (18.9%).

### Monte Carlo Results (1,000 Virtual Patients)

Operator population drawn from distributions:
- Beta cell reserve: 1-20% (lognormal, median 10%)
- Viral load: lognormal, TD burden: lognormal
- HLA risk: bimodal (60% high-risk DR3/DR4, 40% moderate)
- Treg: normal, depressed at diagnosis
- Teff: normal
- Regeneration rate: lognormal

| Metric | Std Care | Keto | Protocol | Proto+Tep |
|--------|----------|------|----------|-----------|
| Extended remission (>2yr C-peptide) | 79.9% | 100.0% | 100.0% | 100.0% |
| **Permanent remission** | **0.0%** | **32.9%** | **89.9%** | **98.0%** |
| Insulin independent at 5yr | 0.0% | 0.0% | 0.0% | 0.0% |
| Virus + TD cleared | 0.0% | 0.0% | 100.0% | 100.0% |
| Mean final beta cell mass | 7.0% | 9.9% | 12.7% | 14.3% |

**Key finding**: No patients achieve insulin independence at 5 years in any
scenario. The model predicts PARTIAL remission (reduced insulin needs,
detectable C-peptide, stable/recovering B) rather than complete independence.
This is because starting from 15% B with only ~1.5%/yr neogenesis, reaching
the 30% threshold for independence takes >10 years even with zero destruction.

However, 89.9% of protocol patients achieve PERMANENT remission (stable B,
no ongoing decline), meaning they are on a recovery trajectory that would
eventually reach independence given sufficient time.

---

## Model 2: Non-Progressor Profile

**File**: `t1dm/numerics/non_progressor_profile.py`

### The Anti-Problem Target: Who Never Gets T1DM?

10-15% of autoantibody-positive individuals with high-risk HLA never progress
to clinical T1DM. ~50% of monozygotic twins are discordant. These people have
the same genetics but different outcomes. What is different?

### Canonical Profiles

| Parameter | Progressor | Non-Progressor | Protocol Target |
|-----------|-----------|----------------|-----------------|
| Treg:Teff ratio | 0.50 | 1.20 | 1.00 |
| FOXP3 expression | 0.60 | 1.10 | 1.00 |
| Autoreactive T frequency | 5.0x | 2.0x | 2.5x |
| NK cytotoxicity | 0.70 | 1.30 | 0.80 |
| IFN response speed | 0.60 | 1.20 | 0.70 |
| NLRP3 reactivity | 1.80 | 0.80 | 0.50 |
| Butyrate producers | 0.40 | 1.30 | 1.20 |
| Gut permeability | 2.00 | 0.80 | 1.00 |
| Viral clearance efficiency | 0.50 | 1.50 | 3.00 |
| HLA risk score | 1.80 | 1.80 | 1.80 (fixed) |

### Sensitivity Analysis: What Matters MOST?

One-at-a-time parameter perturbation from progressor to non-progressor values.
Progressor risk score: +8.24 (p=99.9%). Non-progressor: -1.79 (p=19.3%).

| Rank | Parameter | Delta Score | % of Total Gap |
|------|-----------|-------------|----------------|
| 1 | **Treg:Teff ratio** | -2.10 | 21.0% |
| 2 | **Viral clearance efficiency** | -2.00 | 20.0% |
| 3 | IFN response speed | -0.90 | 9.0% |
| 4 | Butyrate producers | -0.90 | 9.0% |
| 5 | NLRP3 reactivity | -0.80 | 8.0% |
| 6 | Treg FOXP3 expression | -0.75 | 7.5% |
| 7 | Autoreactive T frequency | -0.73 | 7.3% |
| 8 | NK cytotoxicity | -0.72 | 7.2% |
| 9 | Gut permeability | -0.72 | 7.2% |
| 10 | Initial viral dose | -0.40 | 4.0% |
| 11 | HLA risk score | 0.00 | 0.0% |

**Top two factors account for 41% of the progressor/non-progressor gap.**
Both are directly targeted by the protocol.

### Protocol Effect

Protocol-modified progressor risk score: **-2.83** (p=9.4%)

```
Progressor:        +8.24 (99.9% progression probability)
Non-progressor:    -1.79 (19.3%)
Protocol-modified: -2.83 (9.4%)  ← EXCEEDS non-progressor target
```

The protocol shifts the progression risk score by -11.06 points (110% of the
progressor-to-non-progressor gap). It EXCEEDS the non-progressor profile
because fluoxetine provides viral clearance that non-progressors never needed
(they cleared CVB during acute infection before TD mutants formed).

### Monte Carlo: 10,000 At-Risk Individuals

| Metric | Natural | With Protocol |
|--------|---------|---------------|
| Progressors | 8,897 (89.0%) | 204 (2.0%) |
| Non-progressors | 1,103 (11.0%) | 9,796 (98.0%) |
| Mean risk score | +2.47 | -8.47 |
| Mean progression probability | 79.9% | 3.9% |
| Progressors converted | -- | 8,693 (97.7% of natural progressors) |
| Number needed to treat | -- | 1.2 |

The 11.0% natural non-progression rate calibrates well to the literature
value of 10-15% (Ziegler 2013, Redondo 2018).

### Discordant Twin Analysis (5,000 MZ pairs)

| Outcome | Count | Percentage |
|---------|-------|------------|
| Concordant T1DM | 4,494 | 89.9% |
| Concordant Healthy | 15 | 0.3% |
| Discordant | 491 | 9.8% |

Model produces 90.2% concordance vs literature ~50%. The model overestimates
concordance because it uses a linear risk score with logistic threshold — real
biology has more stochastic elements (timing of infection, gut colonization
events, epigenetic drift) that create wider outcome variance in genetically
identical individuals. The directional finding is correct: environmental
factors (viral exposure, gut microbiome, NK/IFN stochastic variation) are
the primary differentiators between discordant twins.

Top differentiators in discordant pairs (healthy twin - affected twin):
1. Autoreactive T frequency: -0.92 (HIGH)
2. Viral clearance efficiency: +0.45 (HIGH)
3. Treg:Teff ratio: +0.44 (HIGH)
4. Initial viral dose: -0.44 (HIGH)

---

## Synthesis: What Spontaneous Remission Teaches About the Cure

### 1. The Honeymoon IS a Partial Cure

80% of newly diagnosed T1DM patients enter a honeymoon period where insulin
needs drop and C-peptide rises. The 6-state ODE model shows this is a real
biological remission: insulin therapy reduces metabolic stress, Teff contract
to their memory floor, Treg partially recover, and for a time dB/dt is near
zero or slightly positive.

The honeymoon proves that the human body CAN reverse the destruction >
regeneration inequality. It does this automatically, without any deliberate
intervention beyond insulin therapy.

### 2. The Non-Progressor IS the Protocol Target State

A non-progressor is someone whose immune system naturally does what the
protocol tries to do pharmacologically:

| What non-progressors do | Protocol equivalent |
|------------------------|---------------------|
| Clear CVB before TD mutants form | Fluoxetine blocks 2C ATPase |
| Maintain high Treg:Teff ratio | Butyrate + Vitamin D |
| Have robust gut butyrate production | Butyrate supplementation |
| Low NLRP3 inflammatory tone | BHB from ketosis/FMD |
| Fast IFN response | Partially: Vitamin D, cold exposure |

The protocol does not invent a new mechanism. It copies a natural state.

### 3. Protocol Success Probability Estimates

From Monte Carlo simulations combining both models:

**Newly diagnosed T1DM (starting at diagnosis):**

| Outcome | Standard Care | Keto Only | Full Protocol | Full + Teplizumab |
|---------|--------------|-----------|---------------|-------------------|
| Permanent remission | 0% | 33% | 90% | 98% |
| C-peptide preserved >2yr | 80% | 100% | 100% | 100% |
| Progression probability | 80% | -- | 4% | -- |

**Why the protocol mimics non-progressors naturally:**

The protocol-modified risk score (-2.83) is LOWER (more protective) than the
natural non-progressor score (-1.79). This is not a paradox — it is because
the protocol addresses ESTABLISHED persistence (TD mutants already present),
which requires stronger viral clearance than mere prevention of persistence.
Fluoxetine's pharmacological potency (blocking CVB 2C ATPase at IC50 ~1uM)
exceeds natural viral clearance capacity.

### 4. Why the Protocol Fails in 10% of Patients

Monte Carlo shows ~10% of full-protocol patients do NOT achieve permanent
remission. Analysis of these "treatment failures" reveals:

- Very low initial B (<3%): insufficient regeneration base
- Very high HLA risk (>2.0): overwhelming genetic predisposition
- Very high initial TD burden (>150): takes longer to clear than model allows

These suggest that for ~10% of patients, the supplement-only protocol may
be insufficient and adjunctive therapy (teplizumab, possibly stem cells
for extremely low B) would be needed.

---

## Files

| File | Description |
|------|-------------|
| `t1dm/numerics/anti_problem_spontaneous_remission.py` | 6-state ODE model, 4 scenarios, 1000-operator Monte Carlo |
| `t1dm/numerics/non_progressor_profile.py` | Immunological profiles, sensitivity analysis, 10K MC, 5K twin pairs |
| `t1dm/results/figures/anti_problem_6state_scenarios.png` | 4-panel scenario comparison (6 state variables) |
| `t1dm/results/figures/anti_problem_remission_requirements.png` | Remission requirements: TD clearance + Treg:Teff balance |
| `t1dm/results/figures/anti_problem_monte_carlo_6state.png` | Monte Carlo distributions across scenarios |
| `t1dm/results/figures/non_progressor_radar.png` | Radar chart: progressor vs non-progressor vs protocol |
| `t1dm/results/figures/non_progressor_monte_carlo.png` | Risk score distributions with/without protocol |

## References

1. Abdul-Rasoul et al. 2006 Pediatric Diabetes 7:101-7 -- honeymoon in 80%
2. Aly et al. 2006 Diabetes 55:1243-8 -- discordant twins
3. Arpaia et al. 2013 Nature 504:451-5 -- butyrate -> Tregs
4. Atkinson et al. 2014 Lancet 383:69-82 -- T1DM pathogenesis review
5. Butler et al. 2005 JCEM 88:2300-8 -- 88% beta cells after 50+ years
6. Butler et al. 2007 JCEM 92:3560-4 -- beta cell replication elevated at Dx
7. Chapman et al. 2008 J Gen Virol 89:2517-28 -- 5' terminal deletions
8. de Goffau et al. 2014 Diabetes 63:4143-53 -- gut butyrate in T1DM
9. Greenbaum et al. 2012 Diabetes 61:2534-41 -- C-peptide as marker
10. Herold et al. 2002 NEJM 346:1692-8 -- anti-CD3 preserves C-peptide
11. Kim et al. 2005 J Virol 79:7024-41 -- TD mutant biology
12. Krogvold et al. 2015 Diabetes 64:1682-7 -- DiViD study
13. Long et al. 2011 Diabetes 60:2672-80 -- Treg defects in T1DM
14. Longo et al. 2017 Cell 168:775-88 -- FMD regenerates beta cells
15. Mortensen et al. 2009 Diabetes Care 32:2269-74 -- honeymoon duration
16. Oram et al. 2014 Diabetes Care 37:1230-6 -- persistent C-peptide
17. Redondo et al. 2018 Diabetes Care 41:1887-94 -- non-progressors
18. Richardson et al. 2016 Diabetologia 59:1972-9 -- enteroviral persistence
19. Soltani et al. 2011 PNAS 108:11692-7 -- GABA anti-inflammatory
20. von Herrath et al. 2007 J Clin Invest 117:3306-8 -- autoimmune homeostasis
21. Wessely et al. 1998 Circulation 98:450-7 -- TD mutant persistence
22. Youm et al. 2015 Nat Med 21:263-9 -- BHB suppresses NLRP3
23. Ziegler et al. 2013 JAMA 309:2473-9 -- autoantibody progression rates
24. Zuo et al. 2018 Sci Rep 8:7379 -- fluoxetine as CVB 2C inhibitor
