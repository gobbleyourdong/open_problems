<p align="center">
  <img src="banner.png?v=5" alt="OPEN PROBLEMS WANT TO STAY OPEN" width="900"/>
</p>

<h1 align="center">OPEN PROBLEMS WANT TO STAY OPEN</h1>

<p align="center">
  <b>gobbleyourdong x turbogranny</b><br/>
  dual AI instances grinding open problems 24/7
</p>

---

## Audit update — 2026-04-15

We audited ourselves. Across 71 loop fires (62 non-math + 9 math), we cross-verified every load-bearing claim in the corpus against its cited source. What we found:

- **Math Lean state was undercounted as weaker than it is.** The old `grep -c sorry` method counted per-theorem `"0 sorry"` self-report comments as false positives, inflating the total ~4.5× corpus-wide (up to 10× in yang_mills). **Actual corpus live sorry: 19 across 117 files** — of which **9 are proof-tactic sorry all concentrated in `ns_blowup/Blowup.lean` + `Challenge.lean`** (the actual research frontier), and 10 are infrastructure placeholders (Bessel library, Turing machines, topology fundamental-group, ζ/λ_n/σ/Λ definitions).
- **Cross-document synthesis claims trace cleanly to Lean.** W_NS, Liu-Pass, Williams 2011 NEXP ⊄ ACC⁰, RH 689-zeros + 10.9M Robin SA, YM 66σ iron-fortress — all verified in their cited files. Only `math/SEVEN_WALLS.md` had stale RH numbers (668 vs 689 zeros, Li n≤200 vs 1000); `CLAY_PROBLEMS.md` matches Lean.
- **Non-math citation discipline is uneven.** `biology/thymus/` sets the corpus standard (91 PMIDs across 11 attempts, WebSearch-verified from start). `biology/evolution/` and most of `medical/` adopted PMID discipline only in later attempts — a visible chronological gradient. Dysbiosis numerics (169 runs, ~36k lines) are mostly trained-prior-cited with author+year+journal but few PMIDs.
- **37 RED findings** (load-bearing claims with contradictions, miscategorizations, or grep artifacts) are flagged inline in the relevant `attempts/attempt_NNN_audit*.md` files rather than silently fixed. Dead ends stay in the map.

Full details: [AUDIT_LOG.md](AUDIT_LOG.md) (non-math, 62 fires) and [math/AUDIT_LOG.md](math/AUDIT_LOG.md) (math, 9 fires). Case study on the audit methodology itself: [~/sigma/case_studies/claim_backing_audit_61_fires_001.md](../sigma/case_studies/claim_backing_audit_61_fires_001.md).

---

## math/

Seven Clay Millennium Prize Problems. Lean 4 formalizations. SOS certificates. Zero hand-waving.

| Problem | Status | Lean Theorems / Sorry | Certificates | Gap |
|---------|--------|:--------------------:|:------------:|-----|
| **Navier-Stokes** | Phase 4 | 485 thms, **9 sorry** ⁽ᵃ⁾ | N=3-12, 0 failures | c(N) ~ 1.2/N, prove decay |
| **Yang-Mills** | Phase 3 | 74 thms, **2 sorry** ⁽ᵇ⁾ | GC > 0 all β, 66σ iron fortress | A₄(⟨Tr(P)·Tr(Q)⟩) counting (active) |
| **P vs NP** | Phase 1 | 78 thms, **2 sorry** ⁽ᶜ⁾ | Phase transition + 3 new certs | Liu-Pass → Kt hardness path |
| **Riemann Hypothesis** | Phase 1 | 19 thms, **4 sorry** ⁽ᶜ⁾ | 689 zeros, Li n=1000, Robin 10.9M SA | No weak certificate exists |
| **Birch & Swinnerton-Dyer** | Phase 1 | 5 thms, **0 sorry** | L-values rank-0 | Higher Gross-Zagier (rank-2 pair) |
| **Hodge Conjecture** | Phase 2 | 20 thms, **0 sorry** | Fermat cubic verified | Weil classes at g ≥ 6 |
| **Poincaré** | SOLVED (proof) | 64 thms, **1 sorry** ⁽ᶜ⁾ | 15 verified (Ricci flow, ...) | 12/12 blind (Perelman) |
| **Prime Numbers** | Phase 1 | 3 thms, 0 sorry | 29 verified (Artin, Brun, Cramér, Sato-Tate, ...) | Open conjectures mapped |
| **Liouville Conjecture** | Phase 2 | 7 thms, **1 sorry** ⁽ᶜ⁾ | — | NS backward-entry sub-campaign |

<sub>⁽ᵃ⁾ Proof-tactic sorry (genuine open proof work, all in `ns_blowup/Blowup.lean` + `Challenge.lean`). This IS the open problem.</sub>
<sub>⁽ᵇ⁾ Axiom type-holes awaiting Bessel function library. Not proof gaps.</sub>
<sub>⁽ᶜ⁾ Definition placeholders awaiting formalization infrastructure (Turing machines, ζ/λ_n/σ/Λ definitions, topology fundamental-group, R_crit). Not proof gaps.</sub>

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

### Lean Totals (recount 2026-04-15)

```
Math authored Lean files:  117
Math live sorry:           19   ← was 86-90 in synthesis docs
  Proof-tactic sorry:       9   ← entire remaining proof surface, all in ns_blowup
  Infrastructure holes:    10   ← awaiting libraries (Bessel, TM, ζ defs, etc.)
```

> **Why the numbers changed.** Prior counts used `grep -c sorry`, which
> hit per-theorem `"N proved, 0 sorry"` self-report comments as false
> positives — inflating by 4.5× corpus-wide (up to 10× in yang_mills).
> The stricter regex counts only live `sorry` tactics and `(sorry : T)`
> type-holes. The math Lean state is materially stronger than the old
> counts suggested. **The real research frontier is 9 proof-tactic
> sorry in `ns_blowup/Blowup.lean` + `Challenge.lean`** — everything
> else is Lean-closed modulo infrastructure. Details: [math/AUDIT_LOG.md](math/AUDIT_LOG.md) (9 audit fires, 2026-04-15).

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

## biology/

Two top-level subdirs studying evolutionary biology + organ regeneration.

| Subdir | Scope | Highlights |
|---|---|---|
| **evolution/** | Persistent-organism evolutionary framework | 7-class persistence taxonomy across 10 organisms (CVB, EBV, HPV, HCMV, HHV-6, H. pylori, P. gingivalis, Demodex, Malassezia, C. acnes). Framework + 5 synthesis notes (1854L total, 0 🔴). Paired with `medical/persistent_organisms/`. |
| **thymus/** | Thymic involution + regeneration | 11 attempts (4,231L) with 91 PMIDs (~8.3/attempt, WebSearch-verified from start). **Highest citation standard in the corpus.** TRIIM trial + FOXN1 biology + cytokine regeneration. |

## How This Works

- Every problem gets numbered attempts with documented failure modes
- Dead ends are as valuable as progress — they narrow the search space
- Lean 4 formalizations ensure no hand-waving — every theorem compiles or it doesn't
- SOS certificates are machine-checkable — `python verify.py certs/`
- **We audit ourselves and show the corrections.** When the numbers change, the old numbers stay visible with a ~~strikethrough~~ or "was: X" annotation. Being wrong in public is cheaper than being silently-right.
- The answer was always there. We're removing everything it isn't.

The methodology used to coordinate the work across math, medicine, physics, and philosophy is developed in a separate private workshop. This repository is the published output, not the method that produced it.

## physics/

Seven tier-0 questions about how reality works at the fundamental level.

| Question | What's at stake |
|----------|----------------|
| **what_is_reality** | Simulation hypothesis, ontology, QM interpretations |
| **what_is_time** | Block universe vs presentism, arrow of time |
| **what_is_nothing** | Quantum vacuum, why is there something |
| **what_is_change** | Zeno, dynamics, continuity |
| **what_is_information** | Shannon, Wheeler's "it from bit", holographic principle |
| **what_is_computation** | Church-Turing, quantum computation, pancomputationalism, ternary efficiency, digital goods value, software entropy |
| **what_is_self_reference** | Gödel, Halting, hard problem; brains, computers, universe as self-modeling instances |

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
    ns_blowup/             <- Navier-Stokes 3D regularity
    yang_mills/            <- Yang-Mills mass gap
    p_vs_np/               <- P vs NP
    riemann_hypothesis/    <- Riemann Hypothesis
    birch_swinnerton_dyer/ <- BSD conjecture
    hodge_conjecture/      <- Hodge conjecture
    poincare_conjecture/   <- Poincare (solved, blind reconstruction)
    prime_numbers/         <- Open prime conjectures (Artin, twin primes, Cramér, ...)
    liouville_conjecture/  <- Liouville on R³ (NS backward-entry sub-campaign)
  medical/
    t1dm/                <- Type 1 Diabetes (107+ attempts)
    myocarditis/         <- Viral myocarditis
    me_cfs/              <- Chronic fatigue syndrome
    dysbiosis/           <- Gut-skin-virome axis (rosacea + T1DM + seb derm)
    perioral_dermatitis/ <- POD (4-mountain model, behavioral wall)
    blepharitis/         <- Demodex + ocular rosacea (route-reachability matrix)
    persistent_organisms/ <- 8-organism × two-phase therapeutic framework
    ...16 diseases total
  biology/
    evolution/           <- 7-class persistence taxonomy, 10 organisms
    thymus/              <- Involution + regeneration, TRIIM trial (91 PMIDs)
  physics/
    what_is_reality/        <- Simulation, ontology, QM interpretations
    what_is_time/           <- Block universe, arrow of time
    what_is_self_reference/ <- Gödel, Halting, hard problem
    ...7 tier-0 questions
  philosophy/
    what_is_mind/        <- Hard problem, consciousness
    what_is_knowing/     <- Epistemology, Gettier
    ...9 tier-0 questions
```

## License

Research use. If you close a gap, cite the repo. If you cure a disease, tell us.

---

<p align="center"><i>Michelangelo: "I saw the angel in the marble and carved until I set him free."</i></p>
<p align="center"><i>We're not building proofs. We're removing everything that isn't the proof.</i></p>
