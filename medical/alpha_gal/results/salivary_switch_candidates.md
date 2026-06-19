# Salivary IgE-switch candidates — Phase 1 (Odd lane) graded table

> Sigma Phase 1 deliverable. Each candidate is a proposed driver of the **tolerance→IgE-switch**
> gap (`../gap.md`). Columns: evidence grade · primary citation (real PMID/DOI only) · **bystander
> test** = "is it ALSO present in non-sensitizing bites?" (if yes → necessary-at-most, not
> sufficient). Tier 1 (single-instance). **STATUS: COMPLETE** — all four sub-hyps graded +
> synthesis (2026-06-18, fire 4).

## Sub-hypothesis #1 — Salivary adjuvant identity (which saliva component drives the IgE switch?)

| Candidate | Grade | Primary citation | Bystander test | Falsifier (gap.md #1) |
|---|---|---|---|---|
| **Prostaglandin E2 (PGE2)** — triggers Ig class-switch to anti-α-Gal **IgE** B cells; promotes Th2 | **Moderate** (named mechanism, repeated across reviews; not yet causally isolated in vivo for AGS) | Frontiers Allergy 2021, "The α-Gal Syndrome and Potential Mechanisms," PMC8974695 (doi 10.3389/falgy.2021.783279) | **YES — present in many tick species' saliva incl. non-AGS bites** → PGE2 is a plausible *necessary adjuvant but not sufficient* alone | Deplete/block PGE2 in a model → IgE-switch abolished while α-gal delivery continues |
| **Sphingomyelinase + cysteine-protease inhibitors** — Th2-profile induction | **Weak/contextual** (Th2-skewing documented; not α-gal-IgE-specific) | "Modulation of host immunity by tick saliva," ScienceDirect S1874391915300610 (review) | YES — generic tick-saliva immunomodulators | Same as above; lower prior than PGE2 |

## Sub-hypothesis #2 — Glycolipid (not glycoprotein) as the switch-critical carrier

| Candidate | Grade | Primary citation | Bystander test | Falsifier (gap.md #2) |
|---|---|---|---|---|
| **α-gal glycolipids (iGb3Cer / Gb3) in saliva → CD1d→iNKT→IL-4** | **Emerging, with FUNCTIONAL support** — phospholipase-silenced salivary-gland extract **reduces basophil activation (BAT)**, implicating the lipid fraction causally | Lone-star saliva α-gal glycolipid ID: Ticks Tick Borne Dis 2024, ScienceDirect S1877959X24000773; preprint bioRxiv 2024.02.22.581476 | **OPEN** — whether these glycolipids appear in non-*sensitizing* bites not yet measured (key experiment) | Protein-only α-gal delivery sensitizes equally → lipid arm not switch-critical |
| **iNKT/CD1d lipid presentation → abundant IL-4** (the IgE-biasing cytokine) | **Moderate (mechanistic)** | Frontiers Allergy 2021, PMC8974695 | OPEN (same as above) | Block CD1d/iNKT → IgE-switch persists |

## Sub-hypothesis #3 — Anti-Gal repertoire diversion (pre-existing memory seeds the IgE switch)

| Candidate | Grade | Primary citation | Bystander test | Falsifier (gap.md #3) |
|---|---|---|---|---|
| **α-gal-glycoproteins engage pre-existing anti-α-Gal memory B cells (anti-Gal BCR)** rather than naive priming | **Moderate** — mechanistic model + indirect host-genetics support | Frontiers Allergy 2021, PMC8974695; *Environmental & Molecular Drivers of AGS*, PMC6554561 | N/A (host-side, not a saliva component) | anti-Gal-low individuals sensitize at equal rate/titer |
| **Blood-group-B/AB tolerance lowers the anti-α-gal IgE ceiling** (B antigen = α-gal − fucose) | **Moderate** — case-control (non-B/AB ~5× risk) **with** a non-significant military-cohort counter | Ann Allergy 2024, S1081120624000747; counter: JACI 2022, S0091-6749(22)01952-2 | N/A (host-side) | If B/AB confers no IgE-ceiling difference in a powered cohort → diversion model weakened |

## Sub-hypothesis #4 — Cofactor-gated absorption (the *elicitation* face: why delayed + variable)

> Addresses gap.md M4 — the downstream/elicitation axis (why 2–6 h, why variable severity), not the
> sensitization switch itself. Included for completeness of the four sub-hypotheses.

| Candidate | Grade | Primary citation | Bystander test | Falsifier (gap.md #4) |
|---|---|---|---|---|
| **Chylomicron lipid kinetics** — α-gal on glycolipids → packaged into chylomicrons → lymph → transition to small LDL particles that exit vasculature to interstitial mast cells hours later | **Moderate (leading model)** — explains the 2–6 h delay; mechanistic, not yet directly imaged | Perioperative Considerations in AGS, PMC10902671; α-gal atypical-allergen review PMC6028928 (ref 6) | N/A (host digestion axis) | Reaction severity tracks IgE titer **independent** of fat intake/transit → kinetics not rate-limiting |
| **Cofactors: exercise / alcohol / NSAID** lower the mast-cell threshold (NSAID via COX→**PGE2**) | **Moderate** — consistent clinical pattern + basophil/mast mechanism | Cofactor-dependent food allergy mechanisms, Frontiers Immunol 2020, PMC7925840 | N/A | Cofactor-controlled challenge shows no threshold shift |

**Cross-link worth flagging:** PGE2 appears at BOTH ends — as the salivary adjuvant driving IgE
class-switch (#1, sensitization) and as the COX-pathway node NSAIDs hit to modulate the mast-cell
threshold (#4, elicitation). Same molecule, two phases. (Note, not a unification claim.)

## Synthesis — which sub-hypothesis does the current evidence favor?

**Favored switch driver: #2 (glycolipid → CD1d/iNKT → IL-4).** It is the *only* candidate with
**functional/causal data** — phospholipase-silencing the salivary-gland lipid fraction measurably
**reduces basophil activation** — whereas #1 (PGE2) is a named adjuvant that **fails the bystander
test as a sole driver** (it is present in non-sensitizing tick saliva). The best-supported model is
therefore **combinatorial, not single-factor**:

1. **Sensitization (the switch):** glycolipid-borne α-gal presented via **CD1d to iNKT cells → IL-4**
   (#2), with salivary **PGE2 as the required class-switch adjuvant** (#1) → anti-α-gal **IgE**.
2. **Host filter (#3):** the pre-existing anti-Gal repertoire / blood-group-B-AB tolerance state sets
   *who* converts and the IgE ceiling.
3. **Elicitation (#4):** chylomicron lipid kinetics + cofactors set *when* (2–6 h) and *how severely*.

**The single highest-value Phase-2 experiment** (the bystander test that's still OPEN for #2):
**measure whether the saliva α-gal glycolipids (iGb3Cer/Gb3) are present in *non-sensitizing* tick
bites.** If absent in non-sensitizers but present in sensitizers, #2 is promoted from "favored" to
"switch-critical." That experiment is the gate to Phase 2.

*Tier 1, single-instance. All grades are literature-based, not bench-confirmed.*
