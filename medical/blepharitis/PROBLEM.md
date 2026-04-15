# Blepharitis — Demodex-driven ocular surface disease

## Scope

This directory covers the **Demodex → anterior blepharitis → meibomian gland
dysfunction (MGD) → chalazion** continuum on the eyelid. The three clinical
entities are usually treated as separate problems. They share a single
upstream driver — *Demodex folliculorum* at the lash base and *Demodex
brevis* in the meibomian gland — and respond to a single class of
intervention (acaricidal lid hygiene with terpinen-4-ol).

Cross-linked content already in the repo:

| Source | What it covers | What it does not cover |
|--------|---------------|------------------------|
| `medical/dysbiosis/numerics/run_046_demodex_rosacea_nlrp3.md` | Demodex → *B. oleronius* → TLR4 → NLRP3 in rosacea skin; ivermectin dual mechanism | Ocular surface; tea tree oil |
| `medical/perioral_dermatitis/attempts/attempt_005_demodex_destruction_natural_compounds.md` | Acaricidal natural compounds (TTO, sulfur, neem, manuka) for pediatric POD | Adult ocular surface; chalazion; MGD |

This directory fills the gap between those two.

## The three clinical entities

### Anterior blepharitis (Demodex folliculorum)

- Mite in the lash follicle; cylindrical dandruff (collarettes) at the lash base is pathognomonic (Gao 2005).
- Symptoms: itching, burning, crusting, eyelash loss, recurrent stye.
- Prevalence of Demodex infestation in chronic blepharitis: 70–100% (Gao 2005, Kheirkhah 2007, Zhao 2012).
- Prevalence in asymptomatic adults: rises with age (0 in children; >90% by age 70 — Post 1963). Density, not presence, is disease-defining.

### Posterior blepharitis / MGD (Demodex brevis)

- Mite in the meibomian gland duct and acinus; blocks lipid secretion.
- Meibum loss → evaporative dry eye; lipid substrate changes → bacterial/saponification cascade.
- Chalazion is the downstream nodule: obstructed meibomian gland → lipogranulomatous inflammation.
- D. brevis is consistently found in meibomian glands of chalazion patients (Liang 2018, Kabataş 2017), at higher rates than in controls.

### Chalazion

- Sterile lipogranuloma from obstructed meibomian gland.
- "Idiopathic" in standard ophthalmology teaching, but a large fraction are Demodex-associated (Liang 2014 — 69% of pediatric chalazion had Demodex; Yam 2014 — recurrence drops with lid hygiene + acaricidal treatment).
- Standard treatment (warm compress → intralesional triamcinolone → incision & curettage) addresses the lipogranuloma but not the infestation driver, which is why chalazia recur on the same or adjacent lash lines.

## Why one framework

All three feed a common loop:

```
Demodex density ↑ (sebum-rich substrate, age, rosacea, immunosuppression,
                     androgen-driven sebum, or ocular surface IgG defect)
      ↓
Mechanical + B. oleronius TLR4 + cuticle chitin Dectin-1/TLR2 triggers
      ↓
Lid-margin inflammation (anterior blepharitis)
      +
Meibomian gland obstruction by mites + lipid modification (posterior blepharitis / MGD)
      ↓
Evaporative dry eye + lipid-granuloma (chalazion) + rosacea skin involvement
      ↓
Chronic lid-margin inflammation → further barrier defect → Demodex density ↑ (self-reinforcing)
```

Breaking the loop at the mite reduces all three downstream entities
simultaneously. This is empirically observed: tea tree oil lid scrubs
produce measurable improvement in blepharitis symptoms (Gao 2007), MGD
parameters (Koo 2012), chalazion recurrence (Liang 2018), and rosacea
erythema when facial skin is also treated (van Zuuren 2019 systematic
review).

## Phase 0 shape-check

| Question | Answer |
|----------|--------|
| Known mechanism? | **Yes** — *Demodex* density + *B. oleronius* endosymbiont + host-response amplification are well characterized |
| Effective treatments exist? | **Yes** — 50% tea tree oil lid scrubs (TheraTears, Cliradex, Blephadex Eyelid Wipes, in-office BlephEx debridement), topical ivermectin, oral ivermectin for refractory cases |
| Can the wall be crossed by new information? | **No — adoption wall, not mechanism wall.** Ophthalmology guidelines still under-screen for Demodex; most blepharitis patients are offered warm compress + tear drops only |
| Crossing requires recurring human action? | **Yes** — daily lid hygiene for 6+ weeks minimum, ongoing maintenance 2–3×/week |
| Predecessors? | Gao 2005 defined cylindrical collarettes; dozens of trials since; ophthalmology slowly adopting |

**Classification: BEHAVIORAL WALL with MECHANISTIC COMPLETENESS.** This is the
canonical v7 Phase 0 behavioral-wall case. The science is done; the
obstruction is clinical recognition (physicians not testing for Demodex) +
patient adherence (6–12 weeks of nightly lid scrubs to reach therapeutic
effect). The method's output should be recognition artifacts and adherence
scaffolding, not more mechanism runs.

## Directory structure

```
medical/blepharitis/
├── PROBLEM.md                     ← this file
├── gap.md                         ← open questions (to be written)
├── attempts/                      ← numbered analyses
├── papers/                        ← key reference list
├── numerics/                      ← any computational work
├── results/                       ← findings
└── certs/                         ← evidence certificates
```

## Status

Created 2026-04-15 as a new directory. First attempts will cover:

1. `attempt_001_ocular_axis_biology.md` — how anterior blepharitis, MGD, and chalazion share Demodex as the upstream driver; species partitioning (D. folliculorum lash-base vs D. brevis gland); host factors (androgen-driven sebum, rosacea comorbidity, age); the *B. oleronius* bridge to rosacea skin.
2. `attempt_002_tea_tree_oil_evidence.md` — clinical trial synthesis for terpinen-4-ol (T4O), dose-response data, available formulations (50% TTO scrubs, 5% T4O wipes, Cliradex, Blephadex), safety envelope, comparative efficacy vs topical ivermectin and oral ivermectin.

---

*Filed: 2026-04-15 | New category, first pass | Scope: Demodex → blepharitis → MGD → chalazion continuum*
*Links to: dysbiosis/run_046 (rosacea mechanism), POD/attempt_005 (TTO pediatric safety)*
