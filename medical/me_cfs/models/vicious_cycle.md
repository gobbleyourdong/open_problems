# Model: The ME/CFS Vicious Cycle — Formalized

## The Core Cycle

```
┌──────────────────────────────────────────────────────────────┐
│                    THE VICIOUS CYCLE                          │
│                                                              │
│   CVB TD mutants in muscle/CNS/gut                          │
│        │                                                     │
│        ▼                                                     │
│   Low-grade inflammation (IL-1β, IL-6, TNF-α)              │
│        │                                                     │
│        ├──▶ Microglial activation ──▶ Brain fog, cognition ↓│
│        ├──▶ Mitochondrial damage ──▶ ATP production ↓       │
│        └──▶ NK cell exhaustion ──▶ Viral clearance ↓        │
│                                        │                     │
│                                        ▼                     │
│                              More TD mutants survive          │
│                                        │                     │
│                                        ▼                     │
│                              More inflammation               │
│                                    (LOOP CLOSES)             │
│                                                              │
│   AMPLIFIER: Post-Exertional Malaise (PEM)                  │
│        │                                                     │
│        Activity ──▶ Muscle contraction ──▶ Metabolic demand  │
│                     on infected cells ──▶ Cell stress/death  │
│                     ──▶ DAMP release ──▶ Inflammation spike  │
│                     ──▶ CRASH (24-72 hour delayed onset)     │
│                                                              │
│   DECONDITIONING TRAP:                                       │
│        │                                                     │
│        Fatigue ──▶ Less activity ──▶ Less AMPK activation    │
│        ──▶ Less autophagy ──▶ More TD mutant survival        │
│        ──▶ More inflammation ──▶ More fatigue                │
│                    (SECOND LOOP)                             │
└──────────────────────────────────────────────────────────────┘
```

## State Variables

```
V(t) = TD mutant viral load (copies/g tissue)
I(t) = Inflammatory cytokine level (composite: IL-1β + IL-6 + TNF-α)
N(t) = NK cell functional capacity (% of normal cytotoxicity)
M(t) = Mitochondrial function (% of normal ATP production)
A(t) = Autophagy rate (autophagosomes formed/cleared per hour)
F(t) = Functional capacity (% of normal activity tolerance)

COUPLED EQUATIONS (qualitative):

dV/dt = +k_replicate × V - k_clear × N × V - k_autophagy × A × V
        [replication]     [NK killing]        [autophagy clearance]

dI/dt = +k_inflam × V - k_resolve × N - k_suppress × Tregs
        [viral PAMPs]  [NK-mediated]    [Treg-mediated]
                       [resolution]     [suppression]

dN/dt = -k_exhaust × V × N + k_restore × Sleep × Se × Zn - k_mito × (1-M) × N
        [exhaustion from    [restoration from              [metabolic impairment
         chronic stimulation] sleep + nutrients]            limits NK function]

dM/dt = -k_damage × I + k_repair × CoQ10 × NAD
        [inflammatory     [mitochondrial repair
         damage]           substrates]

dA/dt = +k_ampk × Fasting × SGLT2i - k_hijack × V × 3C
        [autophagy induction]        [viral hijacking of autophagy]

dF/dt = +k_recover × M × (1 - V/V_max) - k_pem × Activity × V
        [function recovery when         [PEM: activity in presence
         mito works and virus low]       of virus → crash]
```

## Steady States

### Disease Steady State (untreated ME/CFS)
```
V = HIGH (TD mutants persist)
I = ELEVATED (chronic low-grade)
N = LOW (40-60% of normal — exhausted)
M = LOW (mitochondrial dysfunction)
A = LOW (hijacked by 3C + deconditioning reduces AMPK)
F = LOW (20-50% of normal activity tolerance)

All six variables are stuck in unfavorable positions.
Each one holds the others in place.
This is why ME/CFS doesn't spontaneously resolve — the steady state is STABLE.
```

### Recovery Steady State (target)
```
V = ZERO (TD mutants cleared)
I = NORMAL (no viral driver)
N = NORMAL (restored)
M = NORMAL (repaired)
A = NORMAL (not hijacked)
F = NORMAL (full activity tolerance)

Also stable — once the virus is cleared, all variables normalize.
```

### The Bistability Problem
The system has TWO stable steady states (disease and health) with an UNSTABLE threshold between them. The protocol must push ENOUGH variables past the threshold simultaneously to flip the system from disease to health.

**Pushing just one variable doesn't work:**
- Fluoxetine alone (reduces V): viral load drops but NK still exhausted, autophagy still hijacked → virus bounces back
- Exercise alone (increases A via AMPK): PEM triggers crash → worse
- NK restoration alone (increases N): NK cells kill some infected cells but mitochondria can't support sustained killing → partial improvement then stall

**The protocol pushes ALL SIX simultaneously:**
- Fluoxetine → V ↓
- FMD → A ↑↑ (overwhelms 3C hijacking)
- Cold exposure + sleep + Se/Zn → N ↑
- CoQ10 + NR → M ↑
- BHB + butyrate + vitamin D → I ↓
- All of the above → F ↑ (slowly, after viral load drops)

## The Phase Transition Model

```
PHASE 1 (Weeks 1-8): FOUNDATION
  Push N, M, I without triggering PEM
  ├── Supplements (Se, Zn, CoQ10, D-ribose, vitamin D, omega-3, butyrate)
  ├── Sleep optimization
  ├── NO exercise, NO fasting yet
  └── Variables moving: N ↑ (slowly), M ↑ (slowly), I ↓ (slightly)

PHASE 2 (Weeks 9-16): ANTIVIRAL + AUTOPHAGY
  Now attack V and A
  ├── Fluoxetine (V ↓)
  ├── Time-restricted eating → FMD (A ↑↑)
  ├── Cold exposure (N ↑↑, I ↓)
  └── Variables moving: V ↓↓, A ↑↑, N ↑↑

PHASE 3 (Weeks 17-24): THRESHOLD CROSSING
  If V has dropped sufficiently:
  ├── Inflammation resolves (I → normal)
  ├── NK cells recover fully (N → normal)
  ├── Mitochondria repair (M → normal)
  ├── PEM threshold rises (can tolerate more activity)
  └── Variables approaching recovery steady state

PHASE 4 (Weeks 25+): RECONDITIONING
  NOW exercise is safe (V is low, PEM threshold is high)
  ├── Gradual activity increase
  ├── AMPK from exercise maintains autophagy
  ├── Positive feedback: activity → fitness → more activity
  └── System settles into recovery steady state
```

## The Critical Question: Is the Threshold Crossable?

The protocol works IF the combined intervention pushes all variables past the unstable threshold. This depends on:

1. **Initial viral load** — higher V requires stronger push
2. **Duration of illness** — longer duration → more NK exhaustion → harder to restore
3. **Mitochondrial damage extent** — some may be irreversible (mtDNA mutations)
4. **Autoimmune component** — if autoantibodies are established, viral clearance alone insufficient

**Prediction**: patients with <5 years ME/CFS, detectable enteroviral RNA (confirming CVB etiology), and no autoantibodies have the best chance of crossing the threshold. Long-duration patients with multiple autoantibodies may need additional immune modulation (LDN, low-dose IL-2).
