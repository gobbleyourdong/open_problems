# Model: Treg/Th2 Bistability in Atopic Dermatitis

## The Coupled System

```
Five state variables:
  B(t) = barrier integrity [0,1]
  T2(t) = Th2 activity (IL-4/IL-13 production rate, arbitrary units)
  Tr(t) = Treg suppressive capacity (FOXP3+ cell frequency × function)
  S(t) = S. aureus density on skin (CFU/cm²)
  I(t) = itch/scratch intensity (drives mechanical barrier damage)

EQUATIONS (qualitative ODEs):

dB/dt = k_repair × (1 + Emollient) × (B_max - B)     [barrier repair toward max]
      - k_scratch × I × B                               [scratch damages barrier]
      - k_IL4 × T2 × B                                  [IL-4 suppresses filaggrin → barrier weakens]

dT2/dt = k_prime × (1 - B) × Ag                        [antigen entry through broken barrier → Th2 priming]
       + k_staph × S × SuperAg                          [S. aureus superantigen → polyclonal Th2]
       + k_TSLP × (1 - B)                               [barrier breach → TSLP → Th2]
       - k_suppress × Tr × T2                           [Tregs suppress Th2]

dTr/dt = k_butyrate × [Butyrate]                        [butyrate → FOXP3 → Tregs]
       + k_vitD × [VitD]                                 [vitamin D → Treg differentiation]
       + k_BHB × [BHB]                                   [BHB → HDAC → pro-Treg epigenetics]
       + k_IL10 × [IL-10]                                [IL-10 → STAT3 → FOXP3]
       - k_consume × T2 × Tr                             [Tregs consumed/exhausted suppressing active Th2]

dS/dt = k_colonize × (1 - B) × (S_max - S)             [colonizes broken barrier]
      - k_cathelicidin × LL37 × S                        [cathelicidin kills S. aureus]
      - k_bleach × BleachBath × S                        [bleach bath decolonization]
      - k_compete × Commensals × S                       [commensal bacteria compete]

dI/dt = k_IL31 × T2                                      [IL-31 from Th2 → itch]
      - k_moisturize × Emollient                         [emollients reduce itch]
      - k_antiH × Antihistamine                          [antihistamine reduces itch]
```

## Steady States

### Disease attractor
```
B = 0.3 (barrier compromised)
T2 = HIGH (Th2 dominant, IL-4/IL-13 elevated)
Tr = LOW (insufficient to suppress T2, depleted by chronic suppression attempts)
S = HIGH (S. aureus colonizing damaged barrier)
I = HIGH (IL-31 from T2 → constant itch → scratching → barrier damage)

Self-reinforcing:
  Low B → more antigen entry → more T2
  High T2 → IL-4 suppresses FLG → lower B
  High T2 → IL-31 → high I → scratching → lower B
  Low B → S. aureus colonizes → superantigen → more T2
  High T2 consumes Tr → Tr stays low
```

### Health attractor
```
B = 0.9 (barrier mostly intact, even with FLG mutation — other barrier proteins compensate)
T2 = LOW (present but suppressed by Tr)
Tr = ADEQUATE (not exhausted — T2 is low so less suppression needed)
S = LOW (intact barrier + cathelicidin + commensal competition)
I = LOW (low T2 → low IL-31 → minimal itch)

Self-reinforcing:
  High B → less antigen entry → less T2 priming
  Low T2 → FLG not suppressed → B maintained
  Low T2 → low IL-31 → no itch → no scratching → B maintained
  High B → S. aureus can't colonize → no superantigen
  Low T2 → Tr not exhausted → Tr adequate
```

## The Separatrix

The system tips from health → disease when:

```
T2 × (1-B) > Tr × k_suppress

In words: when Th2 activity × barrier breach exceeds Treg capacity to suppress.

This can happen via:
  1. T2 surge (allergen exposure, infection, stress) with Tr constant
  2. Tr drop (gut dysbiosis, vitamin D deficiency, antibiotics) with T2 constant
  3. B drop (skin trauma, harsh soaps, dry climate) amplifying T2 priming
  4. S surge (antibiotic eliminates commensal competition → S. aureus blooms)

Once past the separatrix: positive feedback loops engage → disease steady state
Getting back requires pushing MULTIPLE variables simultaneously
```

## Intervention Map

| Intervention | Variables pushed | Magnitude |
|-------------|-----------------|-----------|
| Butyrate | Tr ↑ | Moderate |
| Vitamin D | Tr ↑, S ↓ (via cathelicidin) | Moderate-Strong |
| BHB | Tr ↑ (NLRP3 → less IL-1β → less Th2 amplification) | Modest |
| Prebiotics/probiotics | Tr ↑ (via butyrate production) | Gradual |
| Emollients | B ↑, I ↓ | Moderate (maintenance) |
| Bleach baths | S ↓↓ | Strong (acute) |
| WHM → IL-10 | Tr ↑ (IL-10 → FOXP3) | Unknown |
| Dupilumab | T2 ↓↓↓ (blocks IL-4/IL-13 receptor) | Very strong |

**The protocol pushes Tr ↑, S ↓, I ↓, B ↑ (via emollients). The only variable it doesn't directly push is T2 ↓ — that's achieved indirectly via Tr ↑.**

If the Treg boost is insufficient to suppress T2 past the separatrix: dupilumab directly blocks T2 effector cytokines, forcibly pushing the system across.

## Convergence with ME/CFS Model

| Feature | ME/CFS model | Eczema model |
|---------|-------------|-------------|
| Number of state variables | 6 (V, I, N, M, A, F) | 5 (B, T2, Tr, S, I) |
| Bistable? | Yes | Yes |
| Why single interventions fail | System snaps back | Same |
| Key variable | V (viral load) | Tr (Treg capacity) |
| Rate-limiting intervention | NK restoration | Treg restoration |
| Protocol addresses | All 6 variables | 4 of 5 variables (not T2 directly) |
| Threshold crossing strategy | Push all simultaneously | Push all simultaneously |

**Same mathematical structure, different biological variables.** The systematic approach's insight — that chronic diseases are bistable attractors requiring multi-variable intervention — applies across the entire campaign.
