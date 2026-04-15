# Blepharitis / Demodex Ocular Cluster

One-stop reference for the Demodex → anterior blepharitis → meibomian
gland dysfunction → chalazion continuum. Created 2026-04-15 in response
to the operator's request to explore the demodex/rosacea ocular axis and
tea tree oil evidence.

## Directory map

```
medical/blepharitis/
├── README.md                     ← this file (synthesis + protocol)
├── PROBLEM.md                    ← scope + Phase 0 shape-check
├── gap.md                        ← open questions by type
├── attempts/
│   ├── attempt_001_ocular_axis_biology.md
│   ├── attempt_002_tea_tree_oil_evidence.md
│   ├── attempt_003_diagnosis_testing_pathway.md
│   ├── attempt_004_acaricidal_pharmacopoeia.md
│   ├── attempt_005_reinfestation_dynamics.md
│   ├── attempt_006_chronic_inflammation_after_clearance.md
│   └── attempt_007_species_differential.md
├── papers/
│   └── key_references.md         ← ~30 citations grouped by topic
├── certs/
│   ├── cert_001_pediatric_chalazion_demodex.md       ← ≥60% attribution
│   ├── cert_002_collarette_sensitivity_specificity.md ← ~85%/95%
│   └── cert_003_terpinen4ol_active_compound.md        ← T4O isolate = the acaricide
├── numerics/
│   └── demodex_decay_curves.py   ← 4 regimens fitted to published data
└── results/
    └── demodex_decay_curves.png  ← kinetic comparison plot
```

## The core claim

**Anterior blepharitis, meibomian gland dysfunction (MGD), and chalazion
— typically treated as three separate problems — share one upstream
driver: Demodex infestation on the eyelid.** D. folliculorum in the
lash follicle drives anterior disease; D. brevis in the meibomian gland
drives posterior disease and chalazion. The downstream inflammation
loop (KLK5 → LL-37 → NF-κB) becomes self-sustaining after chronic mite
presence, which is why acaricide alone often isn't sufficient for
chronic rosacea-blepharitis.

## The clinical protocol (compact version)

### Step 1 — Diagnose

Slit-lamp for cylindrical collarettes (30-second exam). If present,
patient has anterior Demodex. If absent but MGD / recurrent chalazion /
foreign-body symptoms, suspect posterior D. brevis.

### Step 2 — Assign phenotype (attempt_007)

- **A** anterior-dominant (collarettes, lash loss, itching)
- **B** posterior-dominant (MGD, chalazion recurrence, dry eye)
- **C** mixed / ocular rosacea with facial involvement
- **D** corneal-involved (photophobia, marginal infiltrates — specialty referral)

### Step 3 — Treat by phenotype

| Phenotype | Primary regimen | Adjunct | Expected timeline |
|-----------|-----------------|---------|-------------------|
| A | 5% T4O wipes nightly (Cliradex) + 50% TTO in-office weekly × 4–6 | Hypochlorous acid lid spray | Collarette clearance wk 4–6 |
| B | Lotilaner 0.25% BID × 6 wks (Xdemvy) OR TTO wipes nightly + warm compress + gland expression | Omega-3 1–2 g/day | TBUT improves wk 4–8 |
| C | TTO wipes + topical ivermectin facial (Soolantra) + doxycycline 40 mg sub-antimicrobial × 12 wks | Hypochlorous spray | Full effect wk 12 |
| D | Oral ivermectin 200 µg/kg × 2 doses + lotilaner + doxycycline 100 mg → 40 mg + specialty dry-eye management | Specialty oversight | Months; ophthalmology-led |

### Step 4 — Household decontamination (attempt_005)

Pillowcases at ≥60 °C every 2 days during treatment. Replace pillow if
>2 years old. Discard eye makeup at treatment start. Co-treat
bed-sharing partners. Total cost ~$120–220 one-time vs $1500+ for a
failed drug course.

### Step 5 — Chronic inflammation management (attempt_006)

If symptoms persist after mite clearance:
- Doxycycline 40 mg sub-antimicrobial daily (highest-leverage single
  agent for chronic ocular rosacea)
- Omega-3 continuing
- IPL for refractory telangiectasia
- Topical calcineurin inhibitor for periocular refractory

### Step 6 — Maintenance

TTO wipes 2–3×/week indefinite. Re-induct at 6 weeks if symptoms
recur. Meibography annually to track gland architecture if dropout
is measurable.

## What this directory establishes

1. **The 30-second collarette exam is the highest-ROI diagnostic step.**
   (cert_002)
2. **≥60% of pediatric chalazion is Demodex-attributable.** Standard
   "idiopathic chalazion" teaching is wrong at that fraction.
   (cert_001)
3. **Terpinen-4-ol is the active acaricide in tea tree oil**, not TTO
   as a mixture. 1,8-cineole is an irritant with no acaricidal benefit.
   (cert_003)
4. **Three concurrent causes of "treatment failure"** need to be
   distinguished:
   - Route mismatch (topical wipe vs drop vs oral — attempt_007)
   - Chronic inflammation independent of mite status (attempt_006)
   - Reinfestation from untreated reservoirs (attempt_005)
5. **The protocol collapses to a stepped therapy by phenotype**, not a
   single recommendation for all blepharitis.

## Where this fits in the broader repo

- **Dysbiosis / rosacea mechanism:** `../dysbiosis/numerics/run_046_demodex_rosacea_nlrp3.md` covers the *B. oleronius* → TLR4 → NLRP3 cascade at facial skin; the same cascade applies at the lid margin. The eyelid is facial skin with a different anatomic substrate.
- **Perioral dermatitis:** `../perioral_dermatitis/attempts/attempt_005_demodex_destruction_natural_compounds.md` has the pediatric-specific TTO safety analysis that complements the adult-ocular focus here.
- **T1DM axis:** the insulin/IGF-1 → sebum → Demodex-substrate pathway in `../dysbiosis/results/protocol_integration.md` M5 diet arm connects to "why rosacea is common in T1DM patients." Demodex is the downstream amplifier of the metabolic upstream.

## Where this framework has known limits

- **Non-Demodex blepharitis exists.** Seborrheic blepharitis (Malassezia
  + Staphylococcus variant) is a distinct differential that looks similar
  but responds to different therapy. Not yet covered in this directory —
  candidate attempt_008.
- **Cases without mite involvement genuinely occur.** Pure Sjögren's,
  graft-vs-host, atopic keratoconjunctivitis — Demodex is not the driver.
  The framework is specific to cases where Demodex is upstream; requires
  the diagnostic step to distinguish.
- **Meibomian gland dropout is irreversible once established.** Early
  intervention prevents; nothing known restores. This is the urgency
  argument for screening before dropout is advanced.
- **No head-to-head RCT exists for TTO + lotilaner combination or TTO +
  oral ivermectin combination.** The mechanism argument supports both
  combinations; the trial evidence is per-agent.

## Open work (gap.md remaining)

- **B3** Meibography dropout vs treatment-start regression — requires
  published meibography dataset; numerics candidate.
- **B5** B. oleronius biomarker — research only; no clinical assay.
- **B6** TTO + ivermectin combo trial — mechanistically justified, not
  yet conducted.
- **D3** Seborrheic (Malassezia) blepharitis as differential — candidate
  attempt_008.
- Cert candidates: doxycycline 40 mg sub-antimicrobial evidence, adult
  recurrent chalazion ≥80% Demodex.

## Phase 0 verdict reminder

This is a **behavioral wall** problem (per PROBLEM.md Phase 0 shape-check):
mechanism is known, treatments exist, the obstruction is clinical
adoption (ophthalmology under-screens) and patient adherence (daily
lid hygiene + household decontamination for 6+ weeks). Further analytic
work has diminishing returns past this directory's current content. The
highest-leverage next moves are:

1. Patient self-advocacy ("please check for collarettes") at the point
   of care
2. Clinical education for ophthalmology/optometry trainees on the
   30-second collarette exam
3. Protocol adherence scaffolding (checklists, calendar reminders,
   partner co-treatment conversations)

None of those are method work; they are operator / patient / clinician
work. This directory is the written substrate that those efforts
depend on.

---

*Filed: 2026-04-15 | README.md | Synthesis of attempts 001–007, certs 001–003, numerics*
*Total directory size at time of writing: 7 attempts + 3 certs + 1 numerics + 1 plot + references + PROBLEM + gap*
