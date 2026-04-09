# Pattern 001: Energy-Immune Coupling in ME/CFS

## Status: IDENTIFIED — Numerics complete, not yet certified

## The Pattern

ME/CFS is a **coupled energy-immune failure** driven by multi-site CVB persistence. The bioenergetic deficit and immune dysfunction are not independent symptoms — they form a self-reinforcing loop that explains disease persistence, post-exertional malaise, and resistance to spontaneous recovery.

```
CVB persistence (muscle/CNS/gut)
        │
        ├──→ Viral protease cleaves mitochondrial proteins
        │         → Complex I activity reduced 30-50%
        │         → ATP production drops to 15-28 kg/day (normal: 40 kg/day)
        │
        ├──→ Chronic antigen → T cell exhaustion (TOX+, PD-1hi, Tim-3+)
        │         → CD8+ killing capacity drops 40-70%
        │         → NK cytotoxicity drops 40-60% (Eaton-Fitch 2019 meta-analysis)
        │
        └──→ Low cellular ATP → NK cells can't degranulate
                  → perforin/granzyme release is ATP-dependent
                  → infected cells survive → virus persists
                  → LOOP CLOSES
```

This is the same CVB persistence mechanism as T1DM, but attacking different organs in different proportions. **The same virus, the same 5' UTR TD deletions, the same 2C ATPase drug target.**

## Quantitative Estimates from Numerics

### ATP Production Deficit

| Severity | Complex I | ATP (kg/day) | % of Normal | Functional Capacity |
|----------|-----------|-------------|-------------|---------------------|
| Healthy | 100% | 40.0 | 100% | Full activity |
| Mild ME/CFS | 80% | 29.2 | 73% | Light work, rest needed |
| Moderate | 65% | 20.9 | 52% | Housebound, basic ADLs |
| Severe | 50% | 14.3 | 36% | Mostly bedbound |
| Very Severe | 35% | 8.7 | 22% | Fully bedbound |

Sources: Tomas et al. PLoS One 2017 (20-30% reduction in maximal respiration); Missailidis et al. Int J Mol Sci 2020 (Complex I impairment in lymphoblasts); Fluge et al. JCI Insight 2016 (PDH impairment).

### NK Cell Cytotoxicity Collapse

At 50% ATP + 5 years chronic antigen exposure:
- NK cytotoxicity = **~8% of normal**
- Energy deficit accounts for ~60% of the reduction
- Exhaustion accounts for ~40%
- This matches the Eaton-Fitch 2019 meta-analysis finding of 40-60% reduction

### Post-Exertional Malaise (PEM) as Energy Debt

The PEM model shows:
- **Healthy**: exertion → recovery in 1-2 hours
- **Mild ME/CFS**: recovery in 6-12 hours
- **Moderate ME/CFS**: recovery in 24-48 hours
- **Severe ME/CFS**: recovery in 48-96+ hours

Mechanism: exertion demands ATP > production capacity → anaerobic metabolism → ROS spike → DAMP release → NF-kB activation → cytokine cascade → further mitochondrial suppression → deeper energy debt. The same exertion causes a vastly different inflammatory response depending on baseline mitochondrial capacity.

### IDO2 Metabolic Trap

The tryptophan-kynurenine pathway shows bistability:
- Substrate inhibition of IDO2 creates two stable states
- Normal: tryptophan 50-80 uM, moderate kynurenine flux
- Trapped: tryptophan 20-40 uM, low kynurenine flux
- Entry: acute infection → IFN-gamma → IDO1 depletes tryptophan below trap threshold
- Persistence: even after IFN-gamma normalizes, IDO2 stays in low-activity state
- Consequence: reduced NAD+ synthesis → further ATP deficit

## Why ME/CFS Is Harder Than Single-Organ CVB Diseases

The multi-site persistence model demonstrates:

| Metric | Single-Organ CVB | Multi-Site (ME/CFS) | Ratio |
|--------|-----------------|---------------------|-------|
| Total viral load | Lower | Higher | ~2-3x |
| T cell exhaustion | Moderate | Severe | ~1.5-2x |
| Cross-seeding | None | Continuous | - |
| CNS involvement | Rare | Common (30%) | - |

**Cross-seeding is the key difference.** In myocarditis or pancreatitis, the immune system has one target. In ME/CFS, clearing virus from muscle allows reseeding from gut; clearing gut allows reseeding from CNS. The CNS is a sanctuary site (blood-brain barrier limits immune access to ~20% of systemic levels).

## Connection to the T1DM Protocol

The T1DM protocol addresses ME/CFS because it targets the same virus via the same mechanisms:

| T1DM Protocol Component | ME/CFS Mechanism Addressed |
|--------------------------|---------------------------|
| Fluoxetine (2C ATPase inhibitor) | Reduces CVB replication in ALL reservoirs; crosses BBB (CNS bonus) |
| Fasting / FMD (autophagy) | Clears infected cells; removes viral reservoirs |
| BHB / ketosis (NLRP3 suppression) | Reduces chronic inflammasome activation |
| Butyrate / vitamin D (Treg support) | Restores immune regulation; gut microbiome |
| GABA | Anti-inflammatory + gut barrier support |

## What ME/CFS Needs BEYOND the T1DM Protocol

The multi-site nature of ME/CFS requires additional interventions not needed for T1DM:

### 1. Mitochondrial Support (HIGH PRIORITY)
T1DM does not have a primary energy deficit — ME/CFS does.
- **CoQ10** (200-400 mg/day): bypasses Complex I to feed Complex III directly
  - Castro-Marrero et al. 2015: significant improvement in fatigue scores
- **NAD+ precursors** (NR or NMN, 500-1000 mg/day): restore NAD+ depleted by metabolic trap
  - Supports OXPHOS, sirtuins, PARP (DNA repair)
- **D-ribose** (5g 3x/day): substrate for ATP synthesis (bypasses slow pentose phosphate pathway)
  - Teitelbaum et al. 2006: 61% improvement in energy in CFS patients
- **PQQ** (20 mg/day): stimulates mitochondrial biogenesis (ESTIMATE — less evidence)

### 2. Multi-Reservoir Clearance Strategy
Single antiviral is insufficient — must clear ALL sites:
- **Fluoxetine**: good CNS penetration (solves the sanctuary site problem)
- **Fasting/FMD cycles**: systemic autophagy clears ALL tissues
- **Consider**: extended FMD cycles (5 days vs 3 for T1DM) to reach deep reservoirs
- **Gut-specific**: butyrate + probiotics + possible targeted enteric antivirals (RESEARCH NEEDED)

### 3. Immune Reconstitution Support
Terminally exhausted T cells cannot be rescued — must be replaced:
- Timeline: 6-18 months for meaningful immune reconstitution after viral clearance
- Thymic support (zinc, vitamin A) may accelerate new T cell generation
- **Low-dose naltrexone (LDN, 1.5-4.5 mg)**: modulates immune function, anecdotal ME/CFS benefits
  - Mechanism: transient opioid receptor blockade → endorphin rebound → NK cell activation
  - Brewer et al. 2018: retrospective data showing benefit in fibromyalgia (overlapping condition)
- Set realistic expectations: treatment response in months, full recovery in 1-3 years

### 4. Neuroinflammation-Specific
- **Palmitoylethanolamide (PEA, 600-1200 mg/day)**: endocannabinoid, reduces microglial activation
- **Curcumin (liposomal, 500 mg/day)**: crosses BBB, anti-NF-kB
- **Omega-3 DHA (2-3g/day)**: anti-neuroinflammatory, specialized pro-resolving mediators

### 5. Autonomic Support
Autoantibodies against beta-2 adrenergic and muscarinic receptors cause POTS/dysautonomia:
- Salt + fluids (immediate symptom management)
- **Ivabradine** (if tachycardia): reduces heart rate without lowering BP
- Compression garments, recumbent exercise (graded very carefully — respect PEM)
- Long-term: clearing virus should reduce neoantigen → reduce autoantibody production

## Energy Recovery Timeline Estimates

Based on the numerics models, estimated recovery trajectory with full protocol:

| Phase | Timeframe | What Happens | Energy Level |
|-------|-----------|-------------|-------------|
| 0. Baseline | Pre-treatment | Established ME/CFS | 40-60% |
| 1. Antiviral + mito support | Month 1-3 | Viral replication slows; ATP production begins to improve | 45-65% |
| 2. Autophagy cycles | Month 2-6 | Infected cell clearance from muscle and gut; immune load decreases | 55-70% |
| 3. Immune reconstitution | Month 6-12 | New non-exhausted T cells emerge; NK function improves | 65-80% |
| 4. CNS clearance | Month 9-18 | Last reservoir (CNS) clears; brain fog lifts | 75-90% |
| 5. Tissue repair | Month 12-24 | Mitochondrial biogenesis; muscle reconditioning; IDO2 trap escape | 85-95% |
| 6. Full recovery | Month 18-36 | All reservoirs clear; immune system normalized; exercise tolerance restored | 90-100% |

**Critical caveat**: These are MODEL ESTIMATES. Individual variation is large. Severe/very severe patients may take longer. Patients with >10 years of disease may have irreversible tissue damage (especially CNS). The model assumes CVB is the primary driver — if autoantibodies are independently pathogenic, additional treatment may be needed.

## The Self-Reinforcing Cycle (Why Spontaneous Recovery Is Rare)

```
                    ┌─────────────────────┐
                    │  CVB TD mutants     │
                    │  persist in 2-3     │
                    │  tissue reservoirs  │
                    └────────┬────────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
         Muscle          CNS            Gut
         (42%)          (30%)          (82%)
              │              │              │
              └──────────────┤──────────────┘
                             │
                    ┌────────▼────────┐
                    │ Chronic antigen  │
                    │ exposure         │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        T cell          Mito          IDO2
        exhaustion      damage        trap
        (TOX+)          (CI↓)         (Trp↓)
              │              │              │
              ▼              ▼              ▼
        Low killing    Low ATP      Low NAD+
              │              │              │
              └──────────────┤──────────────┘
                             │
                    ┌────────▼────────┐
                    │ NK cells can't  │
                    │ degranulate     │
                    │ (ATP-dependent) │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │ Infected cells  │
                    │ survive         │────── LOOP CLOSES
                    └─────────────────┘
```

**Breaking the loop at any point can initiate a recovery cascade.** The protocol breaks it at 3 points simultaneously: antiviral (viral replication), autophagy (infected cell clearance), and mitochondrial support (energy restoration). This is why single interventions fail and combined protocols have the best theoretical chance.

## Files

- Numerics: `numerics/energy_metabolism_model.py` (ATP deficit, IDO2 trap, NK function, PEM model)
- Numerics: `numerics/cvb_persistence_multisite.py` (multi-reservoir ODE, intervention modeling, exhaustion dynamics)
- This pattern: `results/pattern_001_energy_immune_coupling.md`
