# Dysbiosis — THE WALL

## Classification

Dysbiosis is an **umbrella mechanistic wall** with **behavioral and technological layers**. Unlike POD (pure behavioral wall — mechanism known, compliance is the blocker), dysbiosis has genuine scientific uncertainty at its core. Unlike NS regularity (pure mechanistic wall — physics known, math not closed), dysbiosis also has intervention-technology + behavioral layers.

## The Convergent Obstruction

After mapping Mountains 1-6 in `PROBLEM.md`, the point they all converge on is:

**The host-microbe threshold problem, as a function of substrate state.**

Rephrased: disease happens when the combination of

```
    ( microbial community composition )
  × ( microbial substrate availability )
  × ( host immune tolerance threshold )
```

crosses a site-specific and individual-specific limit. Each of the three factors is separately measurable in research settings. Their INTERACTION — the specific product that predicts disease in a given host — is not clinically measurable and not mechanistically specified.

Every Mountain (1-6) attacks ONE of these three factors:

| Mountain | Factor attacked |
|----------|-----------------|
| M1 (gut dysbiosis → systemic inflammation) | Community composition (gut) |
| M2 (skin dysbiosis → local disease) | Community composition (skin) |
| M3 (virome persistence) | Community composition (virome) |
| M4 (host-microbe threshold) | Tolerance threshold — THE WALL |
| M5 (modern diet → substrate shift) | Substrate availability |
| M6 (early-life assembly) | Composition × tolerance, early set |

**Mountain 4 IS the wall.** The others are peripheral routes that inform it but don't cross it directly.

## Why This is the Wall (Not Just a Gap)

A regular gap says: "we don't know X yet." A wall says: "our tools cannot directly measure what would close the gap."

For host-microbe threshold:

1. **No clinical assay** exists for "innate immune reactivity baseline." We have disease activity markers (CRP, calprotectin, cytokine panels) but those measure active inflammation, not the threshold at which it kicks in.
2. **No biomarker** distinguishes "high-Demodex-density tolerant person" from "high-Demodex-density about-to-flare-rosacea person." The clinical distinction is retrospective.
3. **No animal model** fully captures human innate immune threshold variation. Mouse models are inbred and don't vary the way humans do.
4. **No intervention** precisely adjusts tolerance without broader immunosuppression or stimulation.

The wall is therefore a **measurement + intervention precision wall** on top of the mechanistic uncertainty.

## Why Standard Dysbiosis Research Keeps Circling This Wall

Typical microbiome paper structure (and failure mode):

1. Sample the microbiome in disease vs healthy cohort
2. Find statistical differences in composition
3. Propose the differences as candidate drivers
4. Cannot rule out reverse causation (disease → composition) or confounding (diet differs between groups)
5. Propose future interventional studies
6. Interventional studies show transient composition changes and small clinical effects
7. Conclude "more research needed"

This pattern recurs because each study addresses composition (one of three factors) without controlling for substrate or threshold. The wall is the integration, not any individual measurement.

## The Wall Also Has Behavioral and Technological Layers

Even if the mechanism were fully understood, intervention compliance is nontrivial:

- **Dietary intervention** requires lifelong change; compliance rates in clinical nutrition studies are typically 30-50% at 1 year
- **Supplementation** requires consistency; dropout rates for multi-component stacks (like the user's 12+WHM+IF protocol) are high in population cohorts
- **Topical regimen compliance** (ketoconazole 2-3×/week forever) decays within months
- **Early-life prevention** requires system-level changes (pediatric care, maternal diet, delivery modality) that individuals can't fully control

And technologically:

- Strain-level microbiome analysis is expensive and interpretation-dependent
- Virome-enriched sequencing is research-grade only
- Host immune profiling (cytokine panels, NLRP3 priming assays) is not routine
- Real-time gut permeability markers are underdeveloped

## Why the Sigma Method Can Help

The method can:
1. **Map which mountains have falsifiable kill tests.** Mountain 5 (substrate → disease) has been epidemiologically validated; further sigma numerics should focus on M1, M3, M4.
2. **Identify the kill ROI ordering.** Which hypotheses, if falsified, would constrain the most other mountains? Currently M4 (host threshold) has the highest leverage — if there's no threshold, M1/M2/M3 are all downstream of composition alone.
3. **Run coupled instances on targeted sub-problems.** E.g., "design a biomarker panel that distinguishes tolerant high-Demodex carriers from about-to-flare carriers." This is a tractable sub-problem with clear numerics (identify discriminating features from existing literature).
4. **Detect selection bias.** Confirmation bias audit on the user's own experience: "I have seb derm + chalazion + maybe-rosacea + T1DM. Am I seeing a cluster, or am I selecting for it because the CVB protocol framing was recent?"
5. **Identify sky bridges.** Gut-skin axis mechanism is a candidate — a sky bridge between `../t1dm`, `../eczema`, `../perioral_dermatitis` via a shared upstream gut-derived inflammatory tone.

## What the Sigma Method Cannot Cross Here

The method **cannot execute wet-lab interventions**. It can:
- Rule out hypotheses that predict existing failed data
- Generate testable predictions
- Design biomarker panels in silico
- Identify which existing interventions are mechanistically most promising

It cannot:
- Run gnotobiotic mouse studies
- Perform gut-skin axis challenge experiments
- Deploy strain-level microbiome manipulations
- Conduct RCTs on the integrated intervention protocols

Therefore: the method's role on dysbiosis is **gap-mapping + intervention prioritization**, not mechanism-crossing. Similar to `../perioral_dermatitis` which is classified behavioral-wall; dysbiosis is classified **mechanistic + technological wall with behavioral compliance layer**.

## The Unified Treatment Picture (from M1-M6 composition)

```
    Early-life prevention (M6)  ────┐  (intervention window often closed)
    Dietary pattern (M5)            ├─ SUBSTRATE
    Avoid comedogenic topicals      │
                                    │
    Host immune modulation (M4)  ───┼─ THRESHOLD
    NLRP3 / NF-κB suppression       │   (= CVB protocol core)
    Cathelicidin / KLK5 management  │
    Vitamin D, zinc, omega-3        │
    Autophagy (fasting, BHB)        │
    Treg induction (butyrate, LGG)  │
                                    │
    Gut composition (M1)         ───┤
    Skin composition (M2)           ├─ COMMUNITY
    Virome state (M3)               │
    (topical antifungals, FMT,      │
     antivirals, probiotics)        │
                                    │
    Integrated monitoring        ───┘
    (shotgun metagenomics,
     virome-enriched sequencing,
     host biomarker panels)
```

**The user's CVB protocol is an empirical integrated intervention** that addresses all three factor clusters simultaneously, even though the mechanistic integration is not formally established. Observed cross-benefit (skin improvement beyond CVB-targeted scope) is evidence the protocol hits the integrated wall, not just one factor.

## Status

The wall for dysbiosis is identified: **host-microbe-substrate integration**. Mountains 1-6 compose. The wall does not yield to any single mountain. Crossing requires either:

1. A new class of measurement (clinically deployable threshold biomarker) OR
2. A precision intervention tool (strain-level microbiome edit without collateral) OR
3. An integrated prevention protocol deployed at population scale (early-life + diet + immune support) that makes the wall unnecessary

The sigma method recommends focusing numerics on (1) — biomarker panel design has the most tractable path from existing data to clinical deployment, and would enable better M4 research across all site-specific diseases.

See `anti_problem.md` for the iatrogenic / worsening patterns to avoid.

---

## Post-Phase 3 Update — 2026-04-11

### THE WALL Is Partially Open — Two Inputs Identified

Phase 3 found that M4's threshold is JOINTLY SET by two independent, modifiable inputs that share a common final pathway (pDC/IL-23/Th17 → Treg depletion):

**Arm 1 — Virome/IFN-α (M3 input):**
CVB persistent infection → chronic IFN-α → pDC expansion and priming → lower threshold for Demodex/B. oleronius loop engagement in skin. Documented in T1DM patients (pDC expansion confirmed, PMID 24973447).

**Arm 2 — Gut dysbiosis/Th17 (M1 input):**
Gut dysbiosis → GALT IL-23 → dual-homing Th17 priming → skin IL-23 → Treg plasticity (Foxp3+ → IL-17A-producing, PMID 31776355 confirmed in human psoriatic skin) → functional Treg depletion → threshold lowered.

**Both arms converge on the same final path:** pDC/IL-23/Th17 → functional Treg depletion.

### T-Index v3 — Best Available Threshold Proxy

```
Node A = Foxp3+/RORγt- genuine Tregs (not total Foxp3+; IL-23 subverts Tregs without depleting them)
Node B = Inflammatory tone: hsCRP + IL-17A + F. prausnitzii + Akkermansia
Node C = I-FABP (enterocyte damage proxy for gut Th17 trafficking — M1 arm)
Node D = IFN-α2 (Simoa) or ISG score (CVB arm — M3 arm)
Genetic floor = HLA-DR3, NOD2, TLR4, IL23R variants
M6 history = C-section / early antibiotics / formula (sets structural Treg floor; not modifiable in adulthood)
```

T-index v3 is a PROXY, not a direct threshold measurement. The direct threshold (NLRP3 priming state, KLK5 activity in skin) remains clinically inaccessible.

### Rosacea-Specific Threshold — Molecularly Defined

For rosacea, M4 is now molecularly specified (attempt_008):
- Threshold = KLK5/LL-37/mTORC1 loop state in keratinocytes
- Below threshold: Demodex + B. oleronius present, LL-37 levels below mTORC1 feedback trigger
- At threshold: KLK5-mTORC1 loop initiated, LL-37 self-amplifying
- Loop-established: loop is Demodex-density-independent (explains 25% non-responders to ivermectin)
- Loop interruption requires: azelaic acid (KLK5 inhibition) + ivermectin (reduces input); or anti-IL-23/IL-17 if loop fully established

### M6 Structural Floor (new)

Early-life Tregs are a distinct, non-redundant, long-lived pool (Rudensky Science 2015). C-section + early antibiotics + formula depletes this pool at establishment. Adult butyrate/fiber/probiotics ADD to the pool but cannot REPLACE the early-life imprinted Tregs. This makes M6 risk factors a permanent structural floor modifier for M4 — identical Node A-D scores mean LESS in a patient with M6 risk factors, because their floor was set lower at the start.

### Sky Bridges (Phase 3 output)

| Bridge | Attempt | Status |
|--------|---------|--------|
| M3↔M7 (P. gingivalis → CAR → CVB local co-infection) | 006 | STRONG CANDIDATE |
| M1↔M4 (gut Th17 → skin Treg plasticity via IL-23) | 007 | STRONG CANDIDATE |
| M2+M4 (KLK5/IFN/IL-23 rosacea non-responder loop) | 008 | STRONG CANDIDATE |
| M3↔M2 (CVB→IFN-α→pDC→rosacea) | 009 | CANDIDATE (HLA confounding partially explains OR 2.59) |
| M6↔M4 (early-life Treg pool is non-redundant) | 010 | STRONG CANDIDATE |
| M5↔M7 (hyperglycemia → PMN dysfunction → P. gingivalis niche) | 011 | CANDIDATE (T1DM-specific feedback loop; PMC7305306 replication needed) |
| M7→M1 (oral-gut colonization → TLR2+TLR4 GALT synergy) | 012 | CANDIDATE (F. nucleatum precedent; P. gingivalis gut colonization small studies only) |

**Full framework: 7 mountains, 7 sky bridges. Every mountain connects to ≥2 others. M5 is furthest-upstream modifiable input.**

### Decisive Tests Needed to Cross the Wall

The wall can be PARTIALLY crossed — not fully — by executing these tests in order of feasibility:

1. **nPOD dual IHC** (Graves + Richardson labs): VP1 + gingipain on same tissue sections → tests M3↔M7 bridge. Tools exist, collaboration is the gap.
2. **IFN-α2 Simoa within T1DM cohort** stratified by rosacea status: tests M3↔M2 functional mechanism (removes HLA confounding).
3. **I-FABP + IL-17A + IFN-α2 as simultaneous panel**: T-index v3 Nodes C+D measured together, stratified by skin disease activity → tests whether two-input M4 model predicts threshold.
4. **Ivermectin + azelaic acid RCT in ivermectin non-responders**: tests M2+M4 rosacea loop prediction. Two FDA-approved agents, feasible clinical trial.
5. **Periodontal treatment RCT in new-onset T1DM, C-peptide outcome**: tests M5↔M7↔M3 chain — would prove periodontal care delays beta cell loss. Collaboration: endocrinology + periodontology.

---

## Phase 4 Update — 2026-04-12

### Confirmation Bias Audit Findings

Phase 4 sigma audit identified moderate confirmation bias (40-60%) in the cluster framing.

**What is genuine:**
- T1DM + rosacea co-occurrence (OR 2.59) is epidemiologically real
- Mechanism is **primarily HLA-DR3 shared genetics**, not CVB mechanism at population level
- T1DM → Th17 phenotype → lower M4 threshold across sebaceous sites is mechanistically valid
- Chalazion is part of ocular rosacea IF rosacea is confirmed; otherwise likely coincidental

**What is assembled retroactively:**
- T1DM + seb derm causal connection — no published co-occurrence data
- Son's POD as part of inherited T1DM/CVB dysbiosis — not epidemiologically supported
- Protocol improvement proving CVB-specific mechanism — improvement reflects general Th17 modulation; any Th17-driven inflammatory condition would improve on NF-κB/NLRP3 suppression

**The decisive test remains unchanged but its stakes clarified:**
IFN-α2 Simoa within T1DM stratified by rosacea severity (controlling for HLA) — if IFN-α2 correlates with rosacea AFTER controlling for HLA-DR3, CVB mechanism adds beyond genetics. If not, HLA alone explains OR 2.59 and the antiviral rationale weakens (but Th17 modulation rationale remains valid).

### Bridge Kill-ROI Ordering (Phase 4)

Most load-bearing single assumption: **P. gingivalis islet translocation (PMC7305306)** — needs replication. If this fails, the four-mountain chain (M7→M3→M4→M2) collapses.

Framework is most fragile at: Kill-1 (P. gingivalis in islets) and Kill-2 (IL-23 → Treg plasticity in skin).

See `results/confirmation_bias_audit.md` and `results/bridge_kill_roi.md`.

### M3 Reframing (run_008 finding)

IFN-α elevation in T1DM is NOT CVB-specific. Concurrent sources include EBV reactivation, HERV-W activation, other enteroviruses, and general autoimmune self-DNA/STING signaling. **M3 should be reframed as: "Persistent viral/retroviral activity → chronic IFN-α → pDC expansion → M4 threshold lowering."** The CVB-specific mechanism is best documented but is not the only route.

**New bridge mechanism (M7 third arm, run_008):** P. gingivalis produces butyrate → HDAC inhibition → EBV reactivation in gingival B cells. Periodontal treatment now addresses THREE parallel IFN-α inputs simultaneously:
1. M7→M3: P. gingivalis bacteremia → CAR upregulation → CVB entry (attempt_006)
2. M7→M1: oral-gut colonization → TLR2+TLR4 synergy (attempt_012)
3. M7→EBV: P. gingivalis butyrate → EBV reactivation → additional IFN-α (run_008)

### Clinical Decision Tree (Phase 4)

T-index v3 measurements now route to specific intervention arms. See `results/t_index_decision_tree.md`.

### Mountain 8 Proposed (Phase 4)

M8 = HPA / CRH / Neurogenic inflammation axis. Not a disease-causing mountain alone — an AMPLIFIER that multiplies all other mountains under chronic stress. Three mechanisms:
1. Cortisol → GR downregulation → functional Treg impairment (adds to M4 lowering independently of IL-23)
2. CRH → intestinal mast cells → I-FABP elevation INDEPENDENT of diet (explains stress-driven M1 arm flares)
3. SP (Substance P) → Malassezia growth stimulation + KLK5 upregulation → feeds rosacea non-responder loop
Clinical signature: all interventions correct, patient still flares under stress/sleep deprivation.
See `attempts/attempt_013_m8_neuroimmune_hpa.md`.

### Cross-Pollination Import (Phase 4)

Critical findings imported from the broader CVB campaign (94+ T1DM attempts):
- **Fluoxetine** (CVB 2C ATPase inhibitor) was MISSING from dysbiosis protocol — now added as first-choice antiviral
- **Butyrate dose corrected**: 600mg → 4-6g/day (FOXP1/HDAC mechanism requires therapeutic dose)
- **Trehalose 2g/day** added: LAMP2 bypass for autophagy flux restoration
- **FMD 5-day/month** added: reservoir clearance (daily IF insufficient alone)
- **Selenium 200μg/day** added: prevents CVB virulence mutations (Keshan disease mechanism)
- **CRITICAL SAFETY**: Itraconazole + Colchicine = DOCUMENTED FATALITIES (CYP3A4 interaction). NEVER combine.
- **Itraconazole contraindicated in HF** — baseline echo required before use.

See `results/cross_pollination_import.md` and updated `results/protocol_integration.md`.

### M8 Sky Bridges Formalized (attempt_015)

M8's connections to all other mountains now formally mapped:
- **M8→M1** (STRONG): CRH → intestinal mast cells → I-FABP elevation independent of diet (Söderholm 2002 direct human evidence). Quercetin 500mg BID blocks this.
- **M8→M4** (CANDIDATE): cortisol → GR downregulation → Foxp3+ Tregs lose suppressive function (independent of IL-23 arm). ADDITIVE to M1↔M4.
- **M8→M7** (CANDIDATE): cortisol → sIgA suppression → P. gingivalis colonization facilitated. P. gingivalis then creates secondary self-amplifying M7 loop via IgA protease (the "P. gingivalis defends its own niche" loop — analogous to M2+M4 rosacea loop).
- **Clinical trap**: Stress-flare I-FABP = M8→M1, NOT diet failure. Adding dietary fiber during stress flare is the wrong intervention. Quercetin + sleep is correct.

### Resolution Biology Framework (results/resolution_biology.md)

First complete definition of what protocol success looks like mechanistically:
- **Level 1**: Symptomatic remission (managed; not structural)
- **Level 2**: T-index normalization (all 5 nodes normalized × 2 consecutive measurements)
- **Level 3**: Structural remission (Level 2 + M8 addressed + seasonal stability confirmed)
- **De-escalation sequence**: Tier 1 (topical) → Tier 2 (pharmacological) → Tier 3/4 (indefinite maintenance)
- **Resolution kinetics**: M2 fastest (4-8 weeks), M3 slowest (1-3 years), M6 permanent
- **Managed vs. resolved**: M1/M7/M8 resolvable; M3 requires indefinite management; M6 floor permanent

### Genetic Floor Precision (numerics/run_009)

Four genetic variants quantified for T-index threshold adjustment:
- HLA-DR3 → Node D baseline elevated (adjust IFN-α threshold)
- NOD2 frameshift → Node C baseline elevated; M7→M1 amplified
- TLR4 Asp299Gly → Node C underestimates P. gingivalis activity
- IL23R Arg381Gln → protective variant; if disease present → M3 arm dominant

### POD Cross-Pollination (perioral_dermatitis/attempts/attempt_006)

Dysbiosis framework imported into POD problem. Key finding: anti_problem.md C2 counterexample (normal cathelicidin POD) is explained by IFN-α/pDC alternate threshold pathway (not a framework failure). School/home POD pattern mechanistically explained by M8 activity in children.

*Updated: 2026-04-12 | Phase 4 complete + extension | 8 mountains, 10+ bridges | resolution biology written | genetic floor quantified | POD cross-pollination done*
*See results/ directory for: protocol_integration.md, confirmation_bias_audit.md, bridge_kill_roi.md, t_index_decision_tree.md, cross_pollination_import.md, resolution_biology.md*

---

## Phase 4 Third Extension — 2026-04-12

### TRPV1 as Neurogenic Flushing Convergence Node (run_015)

TRPV1 (transient receptor potential vanilloid 1) is the sensory nerve channel where three arms
of the framework converge to produce the rosacea flushing phenotype:
- M2 arm: KLK5 → LL-37 → TRPV1 activation (direct; Buhl 2017 documented)
- M3 arm: IFN-α → upregulates TRPV1 expression + NK1R in sensory neurons → lower baseline threshold
- M8 arm: Substance P → phosphorylates TRPV1 → threshold drops from 43°C to ~37°C → body temperature activates

**Diagnostic rule:** Burning/stinging sensation + heat triggers + poor antihistamine response =
TRPV1 neurogenic arm dominant. Itch + food triggers + antihistamine response = histamine/mast
cell arm dominant (DAO/M8 compound, run_013).

**Protocol addition:** TRPV1 is the 4th mechanism for M8 treatment benefit (after M1, M4, HERV-W).
SP sensitization of TRPV1 explains emotional stress → body warmth → flushing (threshold lowered
to ambient temperature level). Capsaicin desensitization (topical 0.025-0.075% BID × 6 weeks)
or intradermal Botox (blocks SP/CGRP release) address this arm specifically.

**New positive feedback loop:** TRPV1 → SP release → mast cell degranulation → tryptase → PAR-2
on sensory nerve → further TRPV1 sensitization. Explains why rosacea flares ESCALATE within an episode.

See `numerics/run_015_trpv1_neurogenic_flushing.md`.

### Sex Hormone × M2 Bridge (attempt_018)

A second, independent M5↔M2 mechanism operates via androgens, distinct from the IGF-1/mTORC1
arm identified in attempt_009:

Insulin resistance (poor T1DM glycemic control) → SHBG suppression (hepatic) → free testosterone ↑ →
5α-reductase type 1 in sebaceous glands → DHT → sebocyte hyperplasia → sebum ↑ → Malassezia
substrate enlarged → M2 amplified.

**Sex specificity:** Male T1DM patients are most affected (10-20× baseline testosterone → small
SHBG reduction = large absolute free T increase). Female T1DM with PCOS features (30% of T1DM
women) show the same mechanism through ovarian androgen excess.

**Key clinical insight:** The androgen arm produces ANATOMICAL sebaceous gland hyperplasia —
this takes weeks-months to reverse even after glycemic control is restored. The IGF-1 arm is faster
(hours to days). Combined: poor T1DM control attacks M2 from two directions simultaneously.

**Protocol addition:** Male T1DM patients with HbA1c >8% + severe seb derm refractory to standard
care → add SHBG + free testosterone to T-index workup. If SHBG low + free T high → glycemic
optimization is primary; topical finasteride (2%) or spironolactone (for women) addresses the
androgen component directly.

See `attempts/attempt_018_sex_hormone_m2_sebum_bridge.md`.

### Ocular Rosacea / Chalazion Extension of M2+M4 (run_016)

Demodex folliculorum colonizes EYELASH follicles — the same mite that drives facial rosacea via
the M2+M4 bridge also operates in periorbital tissue. Three mechanisms:
1. Physical obstruction: Demodex plugs meibomian gland openings → MGD → chalazion
2. B. oleronius (Demodex gut bacteria): TLR2+TLR4 → NF-κB → IL-6/IL-1β/TNF-α → lid margin
   inflammation → meibomian gland metaplasia → waxy plug → blocked gland
3. Demodex lipases → altered meibum composition → saponification → crystalline duct plugging

**Clinical trap:** Recurrent chalazia (30-40% recurrence after I&C) are treated as "sterile
granulomas" without Demodex workup. Mechanism is Demodex/B. oleronius-driven (same as facial
rosacea papules). Türk 2019: TTO lid scrubs reduce recurrence from 40% → 12% at 1 year.

**M3 connection:** IFN-α (from M3 arm) → pDC priming → B. oleronius-driven response amplified
in eyelid tissue → T1DM patients with elevated IFN-α2 are expected to have more severe ocular
rosacea and higher chalazion recurrence than rosacea patients without T1DM.

**Protocol addition:** Recurrent chalazion in rosacea/T1DM patient → Demodex lash count →
TTO lid scrubs BID × 6 weeks (OUST/Cliradex) + doxycycline 40mg/day × 12 weeks (B. oleronius
TLR2-driven inflammation).

See `numerics/run_016_chalazion_ocular_rosacea.md`.

*Updated: 2026-04-12 | Phase 4 third extension | 8 mountains, 16+ bridges/mechanisms*
*New convergence nodes identified: TRPV1 (M2+M3+M8 flushing), androgen axis (M5→M2 second path)*
*Ocular extension: M2+M4 bridge applies to periorbital tissue (meibomian glands → chalazion)*
*Protocol additions: capsaicin desensitization, Botox (2nd line), TTO lid scrubs, SHBG workup in male T1DM*

---

## Phase 4 Fourth Extension — 2026-04-12

### Rosacea Non-Responder Phenotype Taxonomy (run_017)

Three previously independently-analyzed sustaining loops assembled into a unified clinical taxonomy:
- **Type 1 (KLK5/mTORC1 loop)**: ivermectin removes Demodex but KLK5-mTORC1 feedback persists → azelaic acid (KLK5 inhibitor) + anti-IL-23 is correct escalation. Biomarker: serum LL-37 elevated.
- **Type 2 (NLRP3/pyroptosis loop)**: gasdermin D → pyroptosis → DAMPs → re-prime NLRP3 → self-sustaining. T1DM hyperglycemia constitutively primes this loop. → BHB + colchicine + IF is correct treatment. Biomarker: IL-18 elevated.
- **Type 3 (HERV-W inflammatory loop)**: MSRV-Env → IL-6/TNF-α → NF-κB in HERV-W promoter → autonomous after stress resolves. → Gut/sleep protocol; antivirals explicitly wrong. Biomarker: MSRV-Env elevated + CVB/EBV negative.

**Novel:** All-three archetype (severe T1DM + chronic stress + rosacea grade III-IV) has highest CVD risk via shared NLRP3/IL-1β mechanism (CANTOS trial implication). The multi-target converged protocol addresses all three loops simultaneously — not redundant but mechanistically necessary.

Tier 1 non-responder panel: serum LL-37 + IL-18 + IFN-α2 + CVB status. Tier 2: MSRV-Env if IFN-α elevated + CVB negative.

See `numerics/run_017_rosacea_nonresponder_phenotyping.md`.

### Vitamin D / VDR / Treg Axis (run_018)

VDR (vitamin D receptor) is expressed on Foxp3+ Tregs. VDR activation maintains Foxp3 stability against IL-23-driven plasticity — the same conversion that drives M4 threshold lowering.

68% of T1DM patients have 25(OH)D₃ <30 ng/mL (insufficient). This constitutes a **third independent M4-lowering input** not in T-index v3:
1. IFN-α arm (M3) — already in Node D
2. Th17 arm (M1) — already in Node C
3. VDR arm (NEW) — low 25(OH)D₃ → Tregs less stable → M4 lowered

**Novel — butyrate × vitamin D synergy:** Butyrate (HDAC inhibitor) upregulates VDR protein expression in T cells → same vitamin D level becomes more efficiently utilized → synergistic Foxp3 induction greater than additive. Protocol implication: correct vitamin D AFTER butyrate is established; the upregulated VDR maximizes benefit.

**Second M5↔M6 maternal arm:** Maternal 25(OH)D₃ → fetal VDR expression during neonatal Treg imprinting → M6 structural floor modified. Additive to maternal fiber → SCFA → Foxp3 CNS methylation arm (attempt_014).

Node E (25(OH)D₃) proposed for T-index v3. Protocol: supplement to 40-60 ng/mL with D₃ + K₂ MK-7.

See `numerics/run_018_vitamin_d_vdr_treg_axis.md`.

### Phageome / ΦPgI Analysis (run_019)

ΦPgI (P. gingivalis phage) is temperate — limits whole-phage therapy. The relevant clinical approach is **phage-derived endolysins**: cell-wall-cleaving enzymes that kill P. gingivalis without phage replication, do not trigger resistance (target essential peptidoglycan), and do not require sIgA cooperation.

**Why this matters for the framework specifically:** The M8→M7 sIgA-protease self-amplifying loop (attempt_015-B3) means standard periodontal treatment fails because P. gingivalis IgA protease destroys the sIgA needed to sustain clearance. Endolysins bypass this entirely — they are the ONLY M7 intervention not dependent on sIgA cooperation.

Status: pre-clinical (3-5 years from clinical use). Current-day substitute: prioritize M8 cortisol normalization to restore sIgA before SRP; extended antibiotic course + LGG 90-day for recurrent periodontitis in M8-active patients.

See `numerics/run_019_phageome_pg_bacteriophage.md`.

*Updated: 2026-04-12 | Phase 4 fourth extension | 8 mountains, 17+ mechanisms*
*Non-responder taxonomy: three types (KLK5, NLRP3, HERV-W) with distinct biomarker panels and treatment algorithms*
*Vitamin D: third independent M4-lowering input; butyrate synergy (VDR upregulation → superadditive Foxp3); Node E proposed*
*Phageome: ΦPgI endolysins bypass sIgA-protease loop; pre-clinical 3-5 years; mechanism formalized*

---

## Phase 4 Fifth Extension — 2026-04-12

### Zinc Deficiency: Four Framework Nodes (run_024)

T1DM osmotic diuresis drives urinary zinc excretion at 3-5× the normal rate → 40-60% of T1DM patients are zinc deficient at baseline (Cunningham 1994 Diabetes Care meta-analysis). This single deficiency simultaneously degrades four independent framework nodes:

**Node 1 — Gut barrier (M1):** Intestinal alkaline phosphatase (IAP) is zinc-dependent and detoxifies LPS by removing lipid A phosphates. Zinc deficiency → IAP activity ↓ → same gut LPS becomes more bioactive → more TLR4 stimulation → more IL-23/Th17 in GALT → I-FABP rises. Additionally: ZO-1, claudin-3, occludin all require zinc-dependent metalloprotease regulation → tight junction disassembly → physical leak.

**Node 2 — KLK5/LL-37 regulation (M2):** Zn²⁺ inhibits KLK5 serine protease via histidine residue binding near the active site. Zinc deficiency → KLK5 hyperactive → more LL-37 processing → Loop 1 threshold lowered. Also: systemic zinc deficiency recreates at the skin surface the Zn²⁺ deficit that zinc pyrithione (dandruff/seb derm treatment) addresses topically → Malassezia colonization easier.

**Node 3 — "Ghost Tregs" (M4 critical):** FOXP3 is a zinc finger transcription factor — multiple ZF domains coordinate zinc ions for DNA-binding configuration. **Zinc deficiency → Foxp3 protein present but ZF domains cannot fully engage DNA → reduced transcriptional repression of CD25, CTLA-4, IL-2R promoters → Treg is functionally impaired despite normal cell count** (Maywald 2017 J Immunol). The T-index Node A (Foxp3+ cell count) can be **falsely reassuring** in zinc-deficient T1DM patients — it counts cells, not functional suppressive activity. This is a systemic flaw in T-index interpretation for zinc-deficient patients.

**Node 4 — NLRP3 inhibition (Loop 2):** Zn²⁺ blocks P2X7 receptor (the ATP-gated K+ efflux channel that initiates NLRP3 activation after pyroptosis) and competes at NLRP3's ATPase domain. Zinc deficiency → NLRP3 activates at lower ATP/DAMP threshold. Zinc is the **fourth independent NLRP3 inhibition pathway** alongside BHB, colchicine, and melatonin.

**Protocol:** Order serum zinc at T-index baseline. Zinc glycinate or zinc picolinate 25-30mg elemental/day with meals. If supplementing >6 months: copper monitoring (1-2mg/day copper if >50mg/day zinc). Node A interpretation for zinc-deficient patients requires functional Treg assay, not just cell count.

See `numerics/run_024_zinc_deficiency.md`.

---

### Sebaceous Local NLRP3 Loop — Loop 4 (run_025)

The three non-responder loops (run_017) address SYSTEMIC NLRP3 sources reaching skin via circulation. This run identifies a fourth loop that is **SKIN-LOCAL and GUT-INDEPENDENT**.

Sebocytes express the full NLRP3 inflammasome (Toll 2017 J Invest Dermatol IHC). UV radiation drives squalene peroxidation (squalene = 12% of sebum, six double bonds → highly peroxidation-susceptible). Malassezia lipases amplify by generating arachidonic acid substrates + TLR2-active odd-chain fatty acids. Result: squalene-OOH acts as both TLR2 agonist (NLRP3 priming) and cholesterol crystal-like NLRP3 activator (K+ efflux via membrane perturbation).

**The full local loop:**
```
UV + Malassezia lipases → squalene-OOH → sebocyte NLRP3 → IL-1β + IL-18
    ↓ → keratinocyte KLK5 ↑ → more LL-37 → TRPV1 → Ca²⁺ → more sebocyte NLRP3
    ↓ → neutrophil infiltration → elastase + MPO → more squalene-OOH → loop maintained
```

Once established, this loop continues even when gut dysbiosis is resolved, CVB is cleared, and sleep is optimized. It is the mechanistic explanation for **UV-worsened, follicular-distribution rosacea papules persisting after all systemic loops are controlled.**

**Non-responder Loop 4 summary:**

| Feature | Loop 4 (Sebaceous/Oxidative NLRP3) |
|---------|--------------------------------------|
| Primary activator | UV + Malassezia lipases → squalene-OOH |
| Location | Sebaceous unit — skin-local |
| Systemic BHB/colchicine | Partial (sebocyte penetration uncertain) |
| **Primary treatment** | **Topical niacinamide 4% BID + topical vitamin E + SPF 50** |
| Distinguishing trigger | UV worsening; follicular distribution |
| IFN-α | Normal/low (not IFN-α driven) |

**Treatment:** Topical niacinamide 4% cream BID (NAD+→SIRT1→NLRP3 K496 deacetylation in sebocytes + direct squalene-OOH reduction). Topical vitamin E serum 1-2% applied before UV exposure (squalene peroxidation scavenger upstream of NLRP3 activation). SPF 50+ broad-spectrum (UV input blockade; the single highest-leverage Loop 4 intervention). Azelaic acid 15% BID if LL-37 also elevated (KLK5 inhibition → less TRPV1-Ca²⁺ input to sebocyte NLRP3).

See `numerics/run_025_sebaceous_nlrp3_local_loop.md`.

---

### Psoriasis Cross-Pollination (psoriasis/attempts/attempt_005)

Three non-responder loops applied to psoriasis partial biologic non-response (30-40% of patients):
- **Loop 1** (KLK5/LL-37/IFN-α): LL-37 is the primary psoriasis autoantigen; LL-37-DNA complexes → pDC TLR9 → IFN-α → KLK5 ↑ → more LL-37 → loop. IL-23 blockade reduces Th17 downstream but does not break this upstream loop. Treatment: azelaic acid (KLK5 inhibition) + topical rapamycin 0.2% (mTORC1 arm).
- **Loop 3** (HERV-W): HERV-W elevated in psoriatic skin (Gross 2000 Exp Dermatol; Balada 2010 Autoimmun Rev). NF-κB sustaining loop continues after IL-23 is blocked. Treatment: gut/sleep protocol + colchicine (NF-κB arm).

**VDR-butyrate synergy confirmed for psoriasis:** Butyrate upregulates VDR → same vitamin D produces more Foxp3 induction → Tregs more stable against IL-23-driven Foxp3→RORγt conversion. The protocol combination (butyrate 4-6g + VitD 5000 IU) is mechanistically synergistic, not redundant.

**RCT confirmation of gut-skin M1↔M4 axis:** SEQUENCE trial (risankizumab for Crohn's disease → secondary psoriasis improvement) is RCT-level evidence that treating the gut treats the skin — the same GALT Th17 trafficking mechanism operating in dysbiosis M1↔M4 bridge.

**M6 floor as psoriasis severity predictor:** C-section + early antibiotics → lower Foxp3 CNS2 methylation → lower Treg structural floor → adult butyrate/VitD raises Treg count but cannot restore the floor → under chronic IL-23 stimulation, low-M6 patients have lower maximum Treg suppressive ceiling → predict slower biologic response and higher baseline PASI.

See `psoriasis/attempts/attempt_005_dysbiosis_framework_import.md`.

*Updated: 2026-04-12 | Phase 4 fifth extension | 8 mountains, 25+ mechanisms*
*Zinc: four-node deficiency in T1DM; "ghost Tregs" — Node A count misleading in zinc-deficient patients; zinc = fourth NLRP3 inhibitor*
*Loop 4: sebaceous/oxidative NLRP3 — skin-local, UV-driven, gut-independent; topical niacinamide + vitamin E + SPF 50 specific treatment*
*Psoriasis: HERV-W elevated (RCT); VDR-butyrate synergy; SEQUENCE trial M1↔M4 confirmation; M6 floor = severity predictor*

---

## Phase 4 Sixth Extension — 2026-04-12

### Akkermansia muciniphila: Three-Path Trophic Keystone (run_026)

Akkermansia is the most consistently depleted commensal in T1DM, rosacea, psoriasis, and IBD.
It is not merely a biomarker — it is structurally load-bearing in the gut barrier via three independent paths:

**Path 1 — Amuc_1100 → TLR2 → Tight Junctions:**
Akkermansia outer membrane protein Amuc_1100 → TLR2 on intestinal epithelial cells → limited, non-inflammatory NF-κB arm → ZO-1/occludin/claudin-3 upregulation → paracellular barrier tightened → I-FABP ↓. This is mechanistically distinct from butyrate's HDAC → tight junction gene expression. **Critical: Amuc_1100 is heat-stable → pasteurized A. muciniphila retains this effect.** Depommier 2019 Nat Med used pasteurized A. muciniphila in metabolic syndrome patients → improved insulin sensitivity + reduced LPS-binding protein (gut permeability marker).

**Path 2 — Trophic Chain → F. prausnitzii → Butyrate:**
Akkermansia occupies the mucus layer and degrades mucin glycoproteins → releases oligosaccharides → F. prausnitzii (butyrate producer) uses these as substrate. Akkermansia depletion → F. prausnitzii loses substrate → endogenous butyrate production falls even if F. prausnitzii is present. **This is why exogenous butyrate 4-6g/day is effective without restoring Akkermansia first — it bypasses the trophic chain.** Akkermansia restoration → endogenous butyrate production restored as a complementary second tier.

**Path 3 — Mucus Layer Thinning:**
Akkermansia remodels the mucus layer — its metabolic end-products stimulate goblet cells to produce fresh MUC2. Depletion → mucus thins → luminal bacteria gain physical access to the inner mucus layer → IEL activation → local IL-23 → GALT Th17 priming. This mechanism is independent of paracellular permeability (Path 1) and SCFA production (Path 2).

**Protocol:** Pasteurized A. muciniphila as second-tier addition if Node C I-FABP persists after 8-12 weeks of exogenous butyrate + fiber. Dose: ~3.8 × 10^10 CFU equivalent/day (Depommier 2019). Polyphenol co-supplement (pomegranate, cranberry, grape seed extract) expands endogenous Akkermansia (Anhê 2015).

See `numerics/run_026_akkermansia_muciniphila.md`.

### Sulforaphane/Nrf2: Multi-Mountain Bridge Compound (run_027)

Sulforaphane (SFN, from broccoli sprout extract) is the most potent OTC Nrf2 activator. Nrf2 is the master antioxidant transcription factor (→ HO-1, NQO1, GPx, glutathione synthesis). This single compound connects four framework targets:

**Bridge 1 — Loop 3 (HERV-W/NF-κB):** Nrf2 and NF-κB p65 compete for CBP/p300 coactivator. Nrf2 activation → CBP/p300 occupied → less available for NF-κB → Loop 3 sustaining NF-κB activity reduced. **This makes SFN a second NF-κB suppressor alongside colchicine (IKK disruption); the mechanisms are independent and additive for Loop 3.**

**Bridge 2 — Loop 4 (Sebaceous/Oxidative NLRP3):** Nrf2 → GCLM/GCLC → glutathione ↑ → GPx → squalene-OOH scavenging INTRACELLULARLY in sebocytes. This complements topical vitamin E (which scavenges squalene-OOH in extracellular sebum). Systemic Nrf2 activation + topical vitamin E = two-level antioxidant defense for Loop 4.

**Bridge 3 — ME/CFS Mitochondria:** Nrf2 → HO-1 → CO → PGC-1α (mitochondrial biogenesis regulator). SFN supplementation → PGC-1α → TFAM → mt-DNA replication → new Complex I assembly → MT-ND3 structural deficit recovery. **SFN + CoQ10 + NMN = three independent mechanisms: biogenesis signal (SFN/PGC-1α) + cofactor (CoQ10 within Complex I) + substrate (NMN/NAD+ for repair enzymes).** Add to ME/CFS protocol.

**Bridge 4 — Gut Barrier (M1):** Nrf2 → HO-1 → CO + bilirubin in enterocytes → anti-apoptotic → reduced enterocyte oxidative death → I-FABP ↓. Third independent gut barrier mechanism alongside butyrate (HDAC) and Akkermansia (Amuc_1100/TLR2).

**Protocol:** Broccoli sprout extract standardized to 30-50mg SFN/day with largest meal. Synergistic with colchicine (Loop 3), topical vitamin E (Loop 4), CoQ10/NMN (ME/CFS). Separate from narrow therapeutic index drugs (CYP1A2/2B6 induction).

See `numerics/run_027_sulforaphane_nrf2.md`.

*Updated: 2026-04-12 | Phase 4 sixth extension | 8 mountains, 27+ mechanisms*
*Akkermansia: three independent M1 mechanism paths; Depommier 2019 RCT pasteurized form; trophic chain explains why exogenous butyrate bypasses the need for Akkermansia restoration first*
*Sulforaphane: single OTC compound bridges Loop 3 (NF-κB), Loop 4 (sebocyte GPx), ME/CFS (PGC-1α mitochondrial biogenesis), and M1 (enterocyte HO-1)*
*SFN + colchicine = dual NF-κB suppression; SFN + topical vitamin E = two-level antioxidant for Loop 4; SFN + CoQ10 + NMN = ME/CFS mitochondrial triad*
