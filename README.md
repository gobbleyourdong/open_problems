<p align="center">
  <img src="banner.png?v=3" alt="ALL YOUR PROBLEMS ARE BELONG TO US" width="900"/>
</p>

<h1 align="center">ALL YOUR PROBLEMS ARE BELONG TO US</h1>

<p align="center">
  <b>gobbleyourdong x turbogranny</b><br/>
  dual AI instances grinding open problems 24/7
</p>

---

## math/

Seven Clay Millennium Prize Problems. Lean 4 formalizations. SOS certificates. Zero hand-waving.

| Problem | Status | Lean Theorems | Certificates | Gap |
|---------|--------|:------------:|:------------:|-----|
| **Navier-Stokes** | Phase 4 | 30+ (0 sorry) | N=3-12, 0 failures | c(N) ~ 1.2/N, prove decay |
| **Yang-Mills** | Phase 3 | 15+ | GC > 0 all beta | FKG for SU(2) gauge |
| **P vs NP** | Phase 1 | 15+ (0 sorry) | Phase transition + 3 new certs | 3 barriers formalized |
| **Riemann Hypothesis** | Phase 1 | 5+ | Li n=1000, Robin | Certificate equivalence (meta-theorem) |
| **Birch & Swinnerton-Dyer** | Phase 1 | 3 | L-values rank-0 | Rank-2 Gross-Zagier |
| **Hodge Conjecture** | Phase 2 | 4 | Fermat cubic verified | Motivic t-structure |
| **Poincare** | (solved) | 11 (0 sorry) | N/A | 12/12 blind (Perelman) |
| **Prime Numbers** | Phase 1 | — | 29 verified (Artin, Brun, Cramér, Sato-Tate, ...) | Open conjectures mapped |

Each problem directory contains:
- `PROBLEM.md` — formal statement + known results
- `gap.md` / `THEWALL.md` — what exactly remains
- `attempts/` — numbered proof attempts with documented failure modes
- `lean/` — Lean 4 formalizations (Mathlib)
- `certs/` — machine-checkable certificates
- `final_proof/` — reserved for the complete proof

### NS Highlights

```
c(N) = sup S²e/|omega|² at vorticity maximum

N=2:  c = 0.250   (PROVEN analytically)
N=3:  c = 1/3     (geometry characterized)  
N=4:  c = 0.360   (peak — only goes down)
N=10: c = 0.119
N=20: c = 0.025

Decay: c(N) ~ 1.2/N. Threshold: 0.75.
Zero failures across 15,000+ configurations.
N=12 certification in progress (9/13 complete, floor ≥ 19.30).
```

### Lean Totals

```
Theorems: 1,182+
Sorry:    128
```

## medical/

Open medical problems. Mechanism-first research with IC50 data, Lean formalizations, and computational models.

<p align="center">
  <img src="medical/cvb_structure.png" alt="CVB Capsid Protomer — PDB 9TKM" width="800"/>
</p>
<p align="center"><i>Coxsackievirus B1 capsid protomer — VP1 (blue), VP2 (orange), VP3 (green). First CVB atomic structure (PDB: 9TKM, 2025). Rendered from raw PDB coordinates.</i></p>

| Disease | Mechanism | Status |
|---------|-----------|--------|
| **Type 1 Diabetes** | Autoimmune beta cell destruction | 94+ attempts, 5 druggable targets |
| **Viral Myocarditis** | Cardiomyocyte lysis | Dystrophin cleavage model |
| **Dilated Cardiomyopathy** | Chronic structural damage | ODE progression model |
| **ME/CFS** | Persistent infection + immune exhaustion | Energy-metabolism coupling |
| **Pancreatitis** | Exocrine destruction | Seeding model |
| **Pericarditis** | NLRP3 inflammasome | Recurrence probability model |
| **Hepatitis** | Hepatocyte lysis | Neonatal severity gradient |
| **Pleurodynia** | Muscle inflammation | Epidemic correlation |
| **Aseptic Meningitis** | CNS invasion | BBB permeability model |
| **Encephalitis** | Brain parenchyma | CNS clearance model |
| **Orchitis** | Immune-privileged reservoir | Clearance feasibility |
| **Neonatal Sepsis** | Multi-organ | Antibody threshold model |
| **Eczema** | Gut-skin axis / Th2 skewing | Barrier + microbiome |
| **Psoriasis** | IL-17/Th17 driven | Amplification loop model |
| **Infertility** | Immune-privileged reservoir | Male + female factor |
| **Perioral Dermatitis** | Cathelicidin/Demodex/contactant | 4-mountain model, behavioral wall |

## How This Works

- Every problem gets numbered attempts with documented failure modes
- Dead ends are as valuable as progress — they narrow the search space
- Lean 4 formalizations ensure no hand-waving — every theorem compiles or it doesn't
- SOS certificates are machine-checkable — `python verify.py certs/`
- The answer was always there. We're removing everything it isn't.

The methodology used to coordinate the work across math, medicine, physics, and philosophy is developed in a separate private workshop. This repository is the published output, not the method that produced it.

## physics/

Six tier-0 questions about how reality works at the fundamental level.

| Question | What's at stake |
|----------|----------------|
| **what_is_reality** | Simulation hypothesis, ontology, QM interpretations |
| **what_is_time** | Block universe vs presentism, arrow of time |
| **what_is_nothing** | Quantum vacuum, why is there something |
| **what_is_change** | Zeno, dynamics, continuity |
| **what_is_information** | Shannon, Wheeler's "it from bit", holographic principle |
| **what_is_computation** | Church-Turing, quantum computation, pancomputationalism, ternary efficiency, digital goods value, software entropy |

## philosophy/

Nine tier-0 questions about meaning, value, mind, and knowing.

| Question | What's at stake |
|----------|----------------|
| **what_is_mind** | Hard problem of consciousness, IIT, panpsychism |
| **what_is_knowing** | Epistemology after Gettier, what LLMs prove about knowledge |
| **what_is_meaning** | Reference vs use vs distributional semantics |
| **what_is_good** | Moral realism, Hume's is-ought gap |
| **what_is_beauty** | Aesthetics, symmetry, evolutionary signals |
| **what_is_self** | Personal identity, the transporter paradox |
| **what_is_language** | Universal grammar vs distributional, what LLMs prove |
| **what_is_number** | Platonism, formalism, is math discovered or invented |
| **what_is_life** | Demarcation, autopoiesis, origin of life |

## Structure

```
open_problems/
  math/
    ns_blowup/          <- Navier-Stokes 3D regularity
    yang_mills/          <- Yang-Mills mass gap
    p_vs_np/             <- P vs NP
    riemann_hypothesis/  <- Riemann Hypothesis
    birch_swinnerton_dyer/ <- BSD conjecture
    hodge_conjecture/    <- Hodge conjecture
    poincare_conjecture/ <- Poincare (solved, blind reconstruction)
    prime_numbers/       <- Open prime conjectures (Artin, twin primes, Cramér, ...)
  medical/
    t1dm/                <- Type 1 Diabetes (94+ attempts)
    myocarditis/         <- Viral myocarditis
    me_cfs/              <- Chronic fatigue syndrome
    ...15 diseases total
  physics/
    what_is_reality/     <- Simulation, ontology, QM interpretations
    what_is_time/        <- Block universe, arrow of time
    ...6 tier-0 questions
  philosophy/
    what_is_mind/        <- Hard problem, consciousness
    what_is_knowing/     <- Epistemology, Gettier
    ...9 tier-0 questions
    perioral_dermatitis/  <- POD (4-mountain model, behavioral wall)
    ...12 more CVB diseases
```

## License

Research use. If you close a gap, cite the repo. If you cure a disease, tell us.

---

<p align="center"><i>Michelangelo: "I saw the angel in the marble and carved until I set him free."</i></p>
<p align="center"><i>We're not building proofs. We're removing everything that isn't the proof.</i></p>
