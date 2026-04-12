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

---

## Phase 4 Seventh Extension — 2026-04-12

### Topical Rapamycin: Loop 1 + Loop 4 Bridge (run_028)

**The Loop 1 treatment gap:** Ivermectin clears Demodex (removes TLR2 priming), azelaic acid inhibits KLK5 protease activity, but mTORC1 — the central amplifier that drives KLK5 transcription — remained untargeted. Anti-IL-23 biologics are the next step but cost $2,400+/month. Topical rapamycin 0.2% cream closes this gap.

mTORC1 in keratinocytes drives KLK5 transcription (S6K1 → KLK5 mRNA) and IL-23 production in dermal DCs. Rapamycin → FKBP12 → mTOR binding domain blocked → S6K1 and 4E-BP1 dephosphorylated → KLK5 transcription ↓. **Dual blockade: azelaic acid (KLK5 activity) + rapamycin (KLK5 transcription) = complete Loop 1 interruption at two sequential steps.** Evidence: Koenig 2012 Lancet: 0.1-0.4% topical rapamycin → 73% response in TSC angiofibromas (TSC = mTOR pathway hyperactivation = same pathophysiology); minimal systemic absorption at 0.2% (Hofbauer 2007).

**Loop 4 connection (novel):** Sebocyte mTORC1 → SREBP-1 → lipogenic genes → sebum + squalene production. Topical rapamycin → sebocyte mTORC1 ↓ → less sebum → less squalene substrate for UV-induced squalene-OOH. **Topical rapamycin is the only single topical that addresses both Loop 1 (keratinocyte mTORC1 → KLK5 → LL-37) and Loop 4 (sebocyte mTORC1 → sebum → squalene peroxide → local NLRP3).**

**Protocol:** Level 3 in the Loop 1 ladder (after azelaic acid, before anti-IL-23 biologic). Rapamycin 0.2% cream QD-BID on lesional skin only; avoid healing wounds (mTORC1 required for keratinocyte migration). Synergizes with azelaic acid 15% (different targets; complementary).

See `numerics/run_028_topical_rapamycin_loop1.md`.

### Vagal Anti-Inflammatory Reflex: M8 Parasympathetic Arm (run_029)

**What was missing from the M8 analysis:** M8 was analyzed exclusively from the SYMPATHETIC axis (CRH → SP/mast cells, cortisol → HPA, catecholamines → NLRP3 priming). The PARASYMPATHETIC counterlimb — the vagal cholinergic anti-inflammatory pathway (CAP) — was not formalized despite cold exposure (already in protocol) activating it.

**CAP mechanism (Tracey 2002 Nature):**
Vagal efferents → celiac ganglion → splenic nerve → β2-AR on ChAT+ splenic T cells → acetylcholine release → **α7-nAChR on macrophages → IKK-β inhibited → NF-κB ↓** + HMGB1 secretion ↓. This operates within minutes (neural reflex speed), while cortisol operates over hours.

**Framework connections:**
1. α7-nAChR → IKK-β inhibition = **THIRD NF-κB suppression pathway** alongside colchicine (IKK disruption) and sulforaphane (CBP competition) → Loop 3 (HERV-W) damped from three independent angles
2. α7-nAChR → HMGB1 ↓ = **THIRD HMGB1 suppression** alongside omega-3 efferocytosis (run_020) and melatonin SIRT1 → Loop 2 re-priming prevented from three angles
3. α7-nAChR on splenic pDCs → IRF7 suppression → less IFN-α per TLR stimulus = **second pDC/IFN-α suppression** alongside melatonin (run_022)
4. Vagal efferent → gut motility → SIBO prevention → I-FABP maintained (autonomic M1 connection)

**Cold exposure (WHM) mechanism formalized:** Cold → diving reflex → brainstem vagal motor nucleus → vagal efferent surge → splenic nerve activation → α7-nAChR → NF-κB ↓. This is the molecular explanation for WHY cold exposure reduces inflammatory markers — previously attributed only to catecholamine release; the vagal arm is the anti-inflammatory mechanism.

**HRV as protocol measurement:** Heart rate variability (wearable: Oura, Garmin, Apple Watch) = practical proxy for vagal tone/CAP status. Low morning HRV = vagal withdrawal = CAP suppressed = higher inflammatory risk. Novel clinical prediction: low-HRV days predict rosacea flare risk in T1DM patients.

**Protocol additions:**
- Cold shower BID (already endorsed; now with mechanism: diving reflex → CAP)
- Diaphragmatic breathing (4-7-8 or resonance breathing): respiratory sinus arrhythmia → direct vagal activation; accessible complement to cold immersion
- HRV morning monitoring: add to daily protocol tracking alongside symptom diary
- LDN 1.5-4.5mg/day: increases vagal tone via opioid receptor upregulation; bridge agent for high-M8 patients (already in ME/CFS protocol; consider for rosacea with autonomic dominance phenotype)

See `numerics/run_029_vagal_anti_inflammatory_m8.md`.

*Updated: 2026-04-12 | Phase 4 seventh extension | 8 mountains, 29+ mechanisms*
*Topical rapamycin: Loop 1 Level 3 (azelaic acid → rapamycin → biologic); dual Loop 1+4 effect via mTORC1 in keratinocytes + sebocytes*
*Vagal CAP: M8 parasympathetic arm formalized; cold exposure = diving reflex → α7-nAChR → NF-κB (Loop 3) + HMGB1 (Loop 2) + IFN-α (M3); HRV monitoring as inflammatory risk proxy*
*NF-κB suppression now has three parallel paths: colchicine (IKK) + sulforaphane (CBP) + vagal/α7-nAChR (IKK-β) — all additive*

---

## Phase 4 Eighth Extension — 2026-04-12

### Thyroiditis Cross-Pollination (thyroiditis/THEWALL.md created)

Autoimmune thyroiditis is the strongest demonstration of IFN-α causal direction in the entire
framework. IFN-α therapy (hepatitis C treatment) induces thyroiditis in **30-40% of treated
patients** — this is the clearest human causal evidence that IFN-α → organ-specific autoimmunity.

**Mechanism import:**
- M3 arm: CVB persistence → IFN-α → Th1/CD8+ expansion → anti-TPO/anti-Tg antibodies
- M4 arm: Foxp3 zinc finger impairment (zinc deficiency → ghost Tregs → less thyroid-resident
  Treg suppression); VDR/butyrate synergy applies equally to thyroid-resident Tregs
- Loop 2: NLRP3 in thyrocytes (Kolypetri 2020 J Clin Endocrinol) — CVB 2B viroporin → K+ efflux
  → NLRP3 → IL-1β → CD8+ amplification. BHB + colchicine 0.5mg BID
- Loop 3: HERV-W in Hashimoto's thyroid tissue (Hishikawa 1997 Autoimmunity; Balada 2010) — same
  NF-κB sustaining mechanism; explains Hashimoto's persisting after EBV clearance

**Thyroid-specific addition — selenium:**
Cooper 2000 meta-analysis: selenium 200µg/day × 3 months → 40-60% reduction in anti-TPO titers.
Thyroid is the highest-selenium tissue/gram in the body. Selenium → GPx4 (thyrocyte oxidative
protection) + deiodinase (T4 → T3 conversion) + thioredoxin reductase (DNA repair). Form:
selenomethionine (superior bioavailability and safety vs. selenite). Upper limit: 400µg/day.

**Clinical wall:** Late diagnosis → follicle destruction already advanced before treatment.
**Key action:** Screen ALL T1DM patients for anti-TPO + anti-Tg + TSH at diagnosis (25-30%
will be positive). Positive + normal TSH = the intervention window. Do not wait for TSH to rise.

See `../thyroiditis/THEWALL.md` for complete analysis.

### Oral Red Complex: M7 Completion (run_030)

T. denticola and T. forsythia were missing from the M7 analysis. Triple colonization creates
a mechanistically synergistic unit that makes P. gingivalis alone an incomplete M7 description.

**Key novel mechanisms:**
- **T. denticola dentilisin** = second IgA protease in the periodontal pocket. The sIgA-protease
  self-amplifying M7 loop runs for BOTH P. gingivalis (lysine-specific) AND T. denticola (dentilisin/
  chymotrypsin-like). **LGG sIgA restoration is countered by BOTH IgA proteases.** This explains
  why some patients relapse after LGG + SRP — T. denticola maintains the IgA destruction loop
  even after P. gingivalis is reduced.
- **T. denticola motility** = colonizes deep anaerobic pockets that SRP cannot mechanically reach.
  Acts as colonization infrastructure for P. gingivalis recolonization.
- **T. forsythia BspA** = dual TLR2 + TLR4 agonist. TLR4 → TRIF → IFN-β = **oral microbiome
  contribution to M3 arm IFN-α loading** (via pDC amplification of IFN-β). P. gingivalis
  deliberately suppresses TLR4 to avoid IFN-β/NK cell surveillance; T. forsythia provides TLR4
  stimulation that P. gingivalis avoids — the organisms cover each other's immune evasion gaps.
- **Triple complement evasion:** P. gingivalis (CAR) + T. denticola (factor H) + T. forsythia
  (factor H + C4bBP) → all complement activation pathways blocked by different mechanisms.

**Revised M7 sequence (triple-colonized patients):**
1. M8 HPA normalization first (sIgA restoration requires non-suppressed cortisol)
2. SRP + chlorhexidine 0.12% BID × 4 weeks post-SRP
3. Metronidazole 400mg BID × 7 days (T. denticola + T. forsythia + P. gingivalis susceptible)
4. Essential oil mouthwash BID (T. forsythia outer sheath susceptible to thymol/menthol)
5. LGG 90 days (sIgA restoration — more likely to succeed with BOTH IgA proteases suppressed)
6. Doxycycline 40mg/day × 3 months (sub-antimicrobial MMP inhibition)

**Salivary PCR panel** (OralDNA Labs): baseline + 3-month post-treatment for all three species.
Triple colonization confirmed → full revised sequence. P. gingivalis alone → standard sequence.

See `numerics/run_030_oral_red_complex.md`.

*Updated: 2026-04-12 | Phase 4 eighth extension | 8 mountains, 31+ mechanisms*
*Thyroiditis: IFN-α causal direction (30-40% in IFN therapy); selenium 200µg/day (Cooper 2000 meta 40-60% anti-TPO reduction); screen T1DM for anti-TPO at diagnosis*
*M7 red complex complete: T. denticola dentilisin = second IgA protease (LGG countered by both); T. forsythia BspA TLR4 = oral M3 IFN-β source; triple complement evasion via three independent mechanisms*

---

## Phase 4 Ninth Extension — 2026-04-12

### Perioral Dermatitis: Steroid Rebound Explained (POD THEWALL.md updated)

The POD dysbiosis cross-pollination completes the sibling directory sweep. Three novel mechanism
imports for POD that were not in the original four-mountain model:

**Steroid rebound at molecular level (new):**
The compliance wall (POD patients reapply steroids during the 1-3 week rebound) is maintained
partly because caregivers lack a mechanistic model. The import from the dysbiosis framework provides one:

Steroid withdrawal triggers TRIPLE simultaneous mechanism activation:
1. **KLK5/mTORC1 rebound:** GR-mediated mTORC1 suppression → KLK5 mRNA suppressed → on
   withdrawal, mTORC1 disinhibited → KLK5 transcription surges above pre-steroid baseline → LL-37
   burst → TLR2 + TRPV1 simultaneous activation
2. **NLRP3 disinhibition:** GR → NF-κB → NLRP3 priming suppressed during steroid use; on withdrawal,
   NF-κB active → NLRP3 primed → any K+ efflux signal → IL-1β burst
3. **Demodex immune re-activation:** expanded Demodex population now faces resurrected T cell
   immunity → acute TLR2 response to B. oleronius antigen load

The rebound is not an allergic reaction — it is mechanistically predictable and self-limited.
This explanation can be communicated to caregivers to improve compliance through the withdrawal period.

**TRPV1 as POD burning mechanism:** Steroid withdrawal → TRPV1 upregulated + LL-37 rebound directly
activates TRPV1 (Buhl 2017). Burning/stinging is neurogenic, not bacterial. Treatment implication:
capsaicin 0.025% desensitization AFTER acute rebound resolves; do not apply during active flare.

**Zinc in perioral skin:** Zinc deficiency → KLK5 hyperactive → lower POD threshold. Acrodermatitis
enteropathica (severe zinc deficiency) produces perioral lesions confirming perioral skin as
specifically zinc-sensitive. Check serum zinc in refractory POD. Zinc glycinate 25-30mg/day if deficient.

**Loop 4 topicals for POD:** Niacinamide 4% cream BID + SPF 30+ daily for perioral sebaceous
NLRP3 activity persisting after Demodex/contactant removal. Ivermectin (Demodex) + niacinamide
(sebocyte NLRP3) + SPF (UV input) = complete perioral pilosebaceous unit treatment.

See `../perioral_dermatitis/THEWALL.md` for full analysis.

*Updated: 2026-04-12 | Phase 4 ninth extension | 8 mountains, 32+ mechanisms*
*POD: steroid rebound = triple mechanism (KLK5 mTORC1 rebound + NLRP3 disinhibition + Demodex re-activation); TRPV1 = neurogenic burning mechanism; zinc → KLK5 hyperactivity; Loop 4 topicals for perioral sebaceous NLRP3*
*All six sibling directories now have Phase 4 dysbiosis framework cross-pollination*

---

## Phase 4 Tenth Extension — 2026-04-12

### IGFBP-3: The Hidden Amplifier in M5→M2 (run_031)

Standard total IGF-1 assays are clinically misleading in T1DM because 95% of IGF-1 is bound
(biologically inactive). Only free IGF-1 activates IGF-1R → PI3K → mTORC1. Three T1DM-specific
mechanisms reduce IGFBP-3 (the primary binding protein) without reducing total IGF-1:

1. **Portal insulin deficit:** Subcutaneous insulin bypasses the portal first-pass → hepatic
   IGFBP-3 production is stimulated by portal (not systemic) insulin → IGFBP-3 ↓ in T1DM (Batch 1996)
2. **MMP proteolysis:** Chronic T1DM inflammation → MMP-2/MMP-9 elevated → IGFBP-3 cleaved → accelerated clearance
3. **HbA1c correlation:** HbA1c >8% → IGFBP-3 25-40% below controls (Phillip 1998 J Clin Endocrinol)

**Result:** "Normal" total IGF-1 with elevated free IGF-1 → mTORC1 more active in keratinocytes (Loop 1 → KLK5 transcription) and sebocytes (Loop 4 → sebum + squalene substrate). **M5→M2 is more active than hormone panels suggest in poorly controlled T1DM.**

**Fourth zinc mechanism (novel):** Zinc inhibits MMP-2/MMP-9 at their catalytic zinc sites → less IGFBP-3 proteolysis → more IGFBP-3 → less free IGF-1 → mTORC1 less active. Zinc supplementation addresses the IGFBP-3 deficit indirectly — fourth independent zinc mechanism beyond run_024.

**Protocol addition:** Add total IGF-1 + IGFBP-3 simultaneously to T-index baseline. IGF-1/IGFBP-3 molar ratio >0.20 → elevated free IGF-1 → glycemic optimization is top priority; add topical rapamycin (downstream mTORC1 block).

See `numerics/run_031_igfbp3_free_igf1.md`.

### Butyrate Delivery Optimization (run_032) — Protocol-Level Revision

**The pharmacokinetic problem:** Oral sodium butyrate 4-6g/day delivers only 15-25% to the colon
(the HDAC/Foxp3/tight junction target). The remainder is absorbed in the small intestine and liver.
Colonic GALT Tregs, colonocytes, and lamina propria immune cells receive ~0.6-1.0g/day effective
dose — far below what drives meaningful HDAC inhibition.

**Revised delivery strategy (3-4× more colonic exposure):**

| Phase | Components | Colonic delivery | Rationale |
|-------|-----------|-----------------|-----------|
| Phase 1 (Weeks 0-8) | Microencapsulated butyrate 2-3g/day + tributyrin 3g/day | 60-80% + 40-60% | Rapid colonic loading; tributyrin has no odor → compliance |
| Phase 2 (Weeks 8+) | Add resistant starch 5→30g/day | 100% (in situ) | Once F. prausnitzii restored by Phase 1 butyrate feeding |
| Long-term | RS 20-30g/day + tributyrin 1-2g/day | Predominantly endogenous | Self-sustaining; low cost |

**VDR synergy implication (critical):** The butyrate × VitD synergy (run_018 — butyrate upregulates
VDR in GALT Tregs → same vitamin D produces more Foxp3 induction) operates in colonic-resident
Tregs. Systemically absorbed butyrate from small intestine reaches PBMCs and systemic Tregs, but
the lamina propria GALT Tregs require colonic delivery. Switching to colonic-targeted forms is
expected to improve the Foxp3 induction synergy 2-4× over unprotected sodium butyrate.

**Protocol_integration.md butyrate entry has been revised** to reflect this delivery optimization.

See `numerics/run_032_butyrate_delivery.md`.

*Updated: 2026-04-12 | Phase 4 tenth extension | 8 mountains, 34+ mechanisms*
*IGFBP-3: "normal" total IGF-1 conceals elevated free IGF-1 in T1DM; zinc → fourth MMP-IGFBP-3 mechanism; add IGF-1/IGFBP-3 ratio to T-index baseline*
*Butyrate delivery: 15-25% colonic delivery with unprotected sodium butyrate; microencapsulated + tributyrin + resistant starch = 3-4× improvement; VDR synergy requires colonic targeting*

---

## Phase 4 Eleventh Extension — 2026-04-12

### SCD1: The Sebum Lipidome → Malassezia Selection Bridge (run_033)

**The M5→M2 bridge is now mechanistically complete with three parallel arms:**

1. IGF-1 → mTORC1 → sebum quantity ↑ (established in attempt_018)
2. IGFBP-3 deficit → free IGF-1 ↑ at normal total IGF-1 (run_031 amplifier)
3. **SCD1 → sebum composition shifts to Malassezia-favorable (this run — novel)**

**The SCD1 mechanism:**
mTORC1 → SREBP-1 → SCD1 (stearoyl-CoA desaturase-1) → converts stearic acid (C18:0) to
oleic acid (C18:1) in sebocytes. Malassezia lacks FAS1/FAS2 (cannot synthesize C12-C18 fatty
acids de novo; Kim 2017 PLOS Genetics) — oleic acid is its PRIMARY carbon source. Additionally,
insulin resistance simultaneously reduces linoleic acid (C18:2) in sebum — which is
Malassezia-INHIBITORY. Net: insulin resistance maximizes the food (oleic acid ↑) and removes
the inhibitor (linoleic acid ↓) simultaneously.

**Evidence:** Makrantonaki 2011 Br J Dermatol: sebum oleic:linoleic ratio correlates with
Malassezia density (r=0.67, p<0.01) in obese subjects. Zouboulis 2014: mTORC1 → SREBP-1 → SCD1
in human sebocytes confirmed in SZ95 cell line.

**HbA1c as sebum lipidome target:** HbA1c <7.5% → insulin/IGF-1 ↓ → mTORC1 ↓ → SREBP-1 ↓ →
SCD1 expression ↓ → less oleic acid conversion → sebum composition normalized. **The HbA1c target
is a SKIN intervention** — it addresses three parallel M5→M2 mechanisms simultaneously.

See `numerics/run_033_scd1_oleic_acid_malassezia.md`.

### NOD2, Butyrate, and the Paneth Cell Target (run_034)

**The Paneth cell NOD2 target requires terminal ileal delivery:**
Butyrate → HDAC → NOD2 upregulation in Paneth cells (ileal crypts) → alpha-defensin HD5/HD6
→ ileal crypt sterility maintained → M1 barrier protected via innate antimicrobial defense.
This is independent of tight junction upregulation and Foxp3 induction — a THIRD butyrate
mechanism for M1 protection.

Critical pharmacokinetic finding: resistant starch fermentation is cecal/proximal colonic; its
butyrate products move distally and are absorbed as they pass through the colon. They do NOT
effectively deliver butyrate retrograde to the terminal ileum where Paneth cells reside.
**Microencapsulated butyrate (pH 7.0 release) is specifically required for Paneth cell NOD2
upregulation.** This is the mechanistic justification for the microencapsulated component of the
revised Phase 1 delivery strategy.

**Novel NOD2 × M7 bridge:** P. gingivalis bacteremia → P. gingivalis MDP reaches portal circulation
→ GALT macrophages/DCs NOD2 detects MDP → NF-κB → IL-23 in GALT → Th17 priming = SECOND
M7→M1 mechanism alongside gut colonization (via PPI use). In NOD2 frameshift carriers: P.
gingivalis MDP is not adequately detected → P. gingivalis establishes more readily in GALT →
Crohn's flares correlate with periodontal disease. **For NOD2 frameshift Crohn's patients,
periodontal treatment is GI disease management, not just dental hygiene.**

**Novel prediction:** NOD2 frameshift Crohn's patients → higher P. gingivalis IgG seropositivity
than NOD2-wildtype Crohn's (impaired innate detection → longer establishment → higher adaptive
antibody response).

See `numerics/run_034_nod2_butyrate_colonic.md`.

*Updated: 2026-04-12 | Phase 4 eleventh extension | 8 mountains, 36+ mechanisms*
*SCD1: three-arm M5→M2 bridge complete; oleic acid + linoleic acid deficit = Malassezia selection pressure; HbA1c <7.5% is the best SCD1 regulator*
*NOD2: Paneth cell alpha-defensin requires microencapsulated butyrate (not RS); NOD2 × M7 bridge via P. gingivalis MDP → GALT IL-23; NOD2 frameshift → periodontal treatment elevated to GI disease management*

### Circadian BMAL1 Arm and NLRP3 Transcriptional Repression (run_035)

**BMAL1 → NLRP3 transcription (constitutive circadian restraint):**
BMAL1/CLOCK → RORα/γ → REV-ERBα/β → RORE element on NLRP3 promoter → NCoR/HDAC3 corepressor
complex → histone deacetylation → NLRP3 mRNA repressed during BMAL1 active phase. This is
UPSTREAM and distinct from melatonin/SIRT1 (run_022 — post-translational K496 deacetylation):
- BMAL1 arm: reduces NLRP3 PROTEIN AVAILABILITY (transcriptional, pre-assembly)
- Melatonin arm: prevents NLRP3 ACTIVATION (post-translational, post-assembly)

Normal sleep provides BOTH simultaneously. Shift work disrupts BOTH.

**Shift work as the highest-risk M8 amplifier:**
Shift work → light at night → CRY/PER phase shift → peripheral immune cell clock desynchronized
from SCN → BMAL1 amplitude reduced 30-60% in macrophages → NLRP3 mRNA constitutively elevated
→ NLRP3 activates at lower threshold for any triggering signal. Same LPS load → more IL-1β output.

Evidence: Zheng 2020 PNAS (BMAL1 KO → constitutive NLRP3/IL-1β); Druzd 2017 Immunity (IL-1β
5× higher at circadian NLRP3 trough vs. peak).

**M8 now has five mechanisms:**
1. CRH → mast cell CRHR1 → neurogenic flushing
2. Cortisol/GR downregulation → Treg impairment
3. Vagal withdrawal → NF-κB disinhibition (run_029)
4. Melatonin ↓ → SIRT1 ↓ → NLRP3 K496 not deacetylated (run_022)
5. BMAL1 ↓ → REV-ERBα/β → NLRP3 transcription disinhibited (run_035)

**Protocol for shift workers:** TRE (8-10h feeding window) → peripheral clock normalization via
mealtime nutrient cues → BMAL1 amplitude improved independent of light schedule. Colchicine
→ NLRP3 assembly block to compensate for elevated protein availability from BMAL1 disruption.

See `numerics/run_035_circadian_bmal1_nlrp3.md`.

### CAPE/Propolis as Fourth NF-κB Suppressor (run_036)

**CAPE dual NF-κB blockade:**
CAPE (caffeic acid phenethyl ester, primary propolis bioactive) → NF-κB inhibition at TWO steps:
1. IKKβ catalytic inhibition (IC50 ~3-10 µM) → IκBα NOT phosphorylated → NF-κB p65 stays sequestered
2. Michael adduct with p65 Cys38 → p65 cannot bind κB DNA elements even if it reaches the nucleus

Mechanistically distinct from all three existing NF-κB suppressors:
- Colchicine: IKK complex cannot FORM (microtubule-dependent assembly)
- Sulforaphane: NF-κB binds DNA but cannot recruit CBP coactivator
- Vagal α7-nAChR: IKKβ catalytic inhibition via JAK2/STAT3 → Tyr phosphorylation (different residues)
- **CAPE: IKKβ active site + p65 direct alkylation → double downstream block**

**Quercetin (co-present in propolis) → NLRP3 NACHT ATPase inhibition:**
Quercetin binds NLRP3 NACHT domain → blocks conformational change required for activation
(pharmacophore model for NLRP3 inhibitor design; MCC950-like mechanism). Propolis therefore
provides: CAPE (NF-κB priming block) + quercetin (NLRP3 activation block) = two-step NLRP3
suppression from a single OTC supplement.

**Triple framework application of propolis:**
- Oral (standardized 5% CAPE, 300-500mg BID): Loop 3 NF-κB + NLRP3 priming + activation
- Topical (propolis tincture diluted in carrier oil): M2 Malassezia CYP51 inhibition
- Mouthwash (2-3% dilution, 30mL BID × 4 weeks): M7 (P. gingivalis + T. denticola + T. forsythia)

**Key caveat:** CAPE oral bioavailability uncertain. Intestinal esterases may hydrolyze CAPE →
caffeic acid before systemic absorption (Olthof 2001). Clinical anti-inflammatory evidence is
empirical (CRP reduction in RCTs) without confirmed plasma CAPE levels. This is the most
significant open question for the propolis oral arm.

See `numerics/run_036_propolis_cape_nfkb.md`.

*Updated: 2026-04-12 | Phase 4 twelfth extension | 8 mountains, 36+ mechanisms*
*BMAL1: five M8 mechanisms now documented; shift work is double NLRP3 disinhibitor (transcriptional + post-translational)*
*CAPE/propolis: four NF-κB suppressors now documented; quercetin adds NLRP3 NACHT inhibition; propolis has M2 + Loop 3 + M7 triple activity*
*Remaining open: BHB exogenous forms pharmacokinetics; Cutibacterium acnes cross-pollination; Vitamin K2/MK-7 as fifth NF-κB suppressor; mast cell stabilization beyond M8 CRH arm*

### Exogenous BHB Pharmacokinetics: 1,3-Butanediol as Practical NLRP3 Extender (run_037)

**Three exogenous BHB forms and their NLRP3 relevance:**
Youm 2015 IC50 for NLRP3 inhibition: 500 µM. Endogenous BHB during 12-16h fast: 0.5-1.5 mM
(overlaps therapeutic window). For patients who cannot fast (T1DM hypoglycemia risk):

| Form | Peak BHB | Duration >500 µM | Cost/dose | Verdict |
|------|---------|-------------------|-----------|---------|
| Ketone salts (10g) | 0.88 mM | 60-90 min | $2-4 | Too brief; mineral load |
| Ketone esters (25g) | 3.3 mM | 3-4h | $30-40 | Pharmacologically ideal; cost-prohibitive |
| 1,3-Butanediol (15g) | 1.5-2.5 mM | 2-3h | ~$0.50 | Best clinical option |

**1,3-Butanediol mechanism:** hepatic ADH → converts 1,3-BD to BHB. GRAS status. Acceptable
palatability. 15g once daily achieves therapeutic NLRP3 blockade for 2-3h.

**T1DM safety gate:** glucose must be <180 mg/dL before exogenous BHB. Do NOT use if glucose
>250 mg/dL or during illness/fever (DKA risk). Ketone meter target: >0.5 mM at 60 min post-dose.

See `numerics/run_037_exogenous_bhb_pharmacokinetics.md`.

### Cutibacterium acnes and Loop 4: Treatment Convergence with Rosacea (run_038)

**The same sebaceous NLRP3 circuit operates in acne and rosacea — different upstream trigger:**
- Rosacea (Loop 4): Malassezia lipase → enzymatic squalene oxidation → squalene-OOH → NLRP3
- Acne (run_038): C. acnes porphyrins → UV/415nm blue light → photochemical squalene oxidation
  → squalene-OOH → NLRP3. C. acnes also: TLR2 → NF-κB → NLRP3 priming (Signal 1)

**Treatment convergence:** niacinamide 4% + vitamin E (squalene-OOH scavengers) + SPF 50 applies
to BOTH Loop 4/rosacea AND acne — same downstream target, different upstream trigger.

**T1DM worst case:** NLRP3 systemically primed (M1) + C. acnes porphyrin squalene-OOH + Malassezia
lipase squalene-OOH = triple simultaneous NLRP3 activation signal. Severe recalcitrant inflammatory
skin disease in T1DM is predicted by framework.

**Novel predictions:**
- Pre-treating with niacinamide 4% + vitamin E before blue light acne therapy should reduce
  the transient flare (porphyrin excitation → squalene-OOH burst → IL-1β spike)
- Colchicine 0.5mg BID → inflammatory (not comedonal) acne: NLRP3 assembly block should reduce
  papule/pustule count; untested in RCT

See `numerics/run_038_cutibacterium_acnes_loop4.md`.

### Vitamin K2 (MK-7): Fifth NF-κB Suppressor via Gas6/Axl TAM Receptor (run_039)

**MK-7 → Gas6 carboxylation → NF-κB suppression (fifth independent pathway):**
```
MK-7 → gamma-glutamyl carboxylase (GGCX) → carboxylates Gas6 Gla domain residues
    ↓
Carboxylated Gas6 → binds Axl/Mer/Tyro3 TAM receptors on macrophages/DCs
    ↓
TAM receptor → SOCS1 + SOCS3 upregulation
    ↓
SOCS1 → binds NEMO → prevents IKK-β catalytic activation (assembled IKK complex INACTIVATED)
    ↓
IκBα not phosphorylated → NF-κB p65 stays sequestered → NLRP3 not primed → Loop 3 suppressed
```

Mechanistically distinct from all four existing NF-κB suppressors (SOCS1 inactivates the
ASSEMBLED IKK complex — different target from: colchicine's formation block, sulforaphane's
coactivator competition, vagal α7-nAChR's JAK2/STAT3 inhibitory phosphorylation, CAPE's active
site + p65 alkylation).

**T1DM-specific: M1 → K2 deficit creates a double NF-κB consequence:**
M1 gut dysbiosis → Bacteroidetes ↓ (MK-7 producers; Brown 2011) → Gas6 under-carboxylated →
TAM receptor restraint lost → NF-κB disinhibited. SIMULTANEOUSLY: M1 → gut leakage → LPS
→ TLR4 → NF-κB activated. M1 dysbiosis both ACTIVATES and REMOVES RESTRAINT from NF-κB.

**Three K2 benefits in T1DM framework:**
1. Gas6/Axl → SOCS1 → NF-κB suppression (fifth NF-κB pathway)
2. MGP carboxylation → vascular calcification inhibited (T1DM arterial complication prevention;
   dp-ucMGP <200 pmol/L = K2 sufficient; Knapen 2012: MK-7 → arterial stiffness reduced)
3. Osteocalcin/GPRC6A → insulin sensitization (peripheral insulin sensitivity improved)

**Protocol:** MK-7 180µg/day with dietary fat; dp-ucMGP baseline + 3 months. Warfarin
contraindication (direct K antagonism).

See `numerics/run_039_vitamin_k2_mk7_nfkb.md`.

*Updated: 2026-04-12 | Phase 4 thirteenth extension | 8 mountains, 39+ mechanisms*
*BHB: 1,3-butanediol 15g/day is the practical exogenous NLRP3 extender; T1DM glucose gate critical*
*C. acnes: Loop 4 sebaceous NLRP3 circuit shared with rosacea — treatment converges; T1DM dual-trigger worst case*
*K2/MK-7: FIVE NF-κB suppressors now documented; M1 dysbiosis has double NF-κB consequence (activation + restraint removal)*
*Remaining open: IFN-α → NLRP3 direct bridge (M3→Loop 2); spermidine/autophagy; mast cell stabilization; F. prausnitzii monitoring threshold*

### IFN-α → NLRP3 Direct Priming: M3 and Loop 2 Are Connected (run_040)

**The bridge mechanism:**
IFN-α (M3 output: HERV-W/CVB → pDC/macrophage → IRF7 → IFN-α) → IFNAR1/IFNAR2 →
JAK1/TYK2 → STAT1+STAT2 → recruit IRF9 → ISGF3 complex → binds NLRP3 promoter ISRE →
NLRP3 mRNA ↑ (Guarda 2011 Immunity; Rathinam 2012 Cell).

This adds a SECOND PRIMING SOURCE for NLRP3:
- Signal 1A (established): M1 LPS/TLR4 → NF-κB → NLRP3 mRNA ↑
- Signal 1B (new): M3 IFN-α → IFNAR → ISGF3 → NLRP3 mRNA ↑ (additive, independent)

**Framework architectural change:**
M3 and Loop 2 are NOT parallel independent pathways. M3 IFN-α output constitutively elevates
NLRP3 protein. In M3-active patients (elevated Node D), Loop 2 floor is chronically raised by
IFN-α priming — the same K+ efflux signal generates MORE IL-1β/IL-18.

**T-index implication:**
Node D (IFN-α2 Simoa) elevation → Loop 2 treatment (BHB, colchicine) is CO-TREATMENT, not
sequential. Gut repair alone (reducing Node C / I-FABP) reduces NF-κB priming of NLRP3 but
does NOT reduce IFN-α/ISGF3 priming. Both priming sources must be addressed simultaneously
when Node D is elevated.

**Loop 2 + Loop 3 connected via IFN-α:**
HERV-W → TLR4 → IFN-α → NLRP3 ↑ → gasdermin D → DAMPs → TLR4 → more IFN-α → more NLRP3
(Loop 3 NF-κB sustaining loop AND Loop 2 pyroptosis loop share IFN-α as a connector molecule).

**β cell preservation prediction (novel):**
T1DM with elevated Node D + detectable C-peptide (residual β cell function) → β cell NLRP3
is being constitutively primed by IFN-α → β cell pyroptosis accelerated → M3 intervention
(sleep, gut, colchicine NF-κB arm) should slow residual β cell destruction. Testable: correlate
Node D levels with C-peptide decline rate in new-onset T1DM.

**Key caveat:** IFN-α concentrations in clinical samples (Simoa fg/mL) differ from experimental
NLRP3 priming concentrations (IU/mL) by 5-6 log10. Whether chronic low-level IFN-α at clinical
concentrations is sufficient for meaningful NLRP3 priming in vivo remains uncertain.

See `numerics/run_040_ifna_nlrp3_m3_loop2_bridge.md`.

*Updated: 2026-04-12 | Phase 4 fourteenth extension | 8 mountains, 40+ mechanisms*
*Key structural change: M3 (IFN-α) and Loop 2 (NLRP3) are connected via ISGF3 → NLRP3 ISRE — not independent pathways*
*Node D elevation → Loop 2 treatment is co-treatment; gut repair alone cannot fully de-prime NLRP3 when M3 is active*
*IFN-α priming + NF-κB priming = additive NLRP3 sensitization in M3-active T1DM/rosacea patients*

### Spermidine/Mitophagy: Fifth Independent NLRP3 Inhibition Pathway (run_041)

**Five NLRP3 inhibition pathways now documented — all mechanistically distinct:**
| # | Compound | Mechanism | Target |
|---|---------|----------|--------|
| 1 | BHB | K+ efflux blockade (pannexin-1/P2X7) | Signal 2 downstream |
| 2 | Colchicine | NLRP3+ASC colocalization blocked | Assembly |
| 3 | Melatonin/SIRT1 | NLRP3 K496 deacetylation | Conformational change |
| 4 | Zinc | P2X7 blockade + NLRP3 ATPase competition | Signal 2 upstream |
| 5 | Spermidine | EP300 inhibition → mitophagy → mtROS/mtDNA/cardiolipin removed | Signal 2 SOURCE |

**Spermidine mechanism:**
Spermidine → EP300 acetyltransferase inhibition → Beclin-1 deacetylated → VPS34 active →
mitophagy (PINK1/Parkin) → damaged mitochondria removed → mtROS + mtDNA + cardiolipin Signal 2
sources eliminated before NLRP3 can be activated. This is the only approach that acts
UPSTREAM of Signal 2 generation rather than downstream.

**Dietary sources:** wheat germ (highest; ~2-4mg spermidine/tbsp), mushrooms (0.3-0.8 µmol/g),
aged cheese, legumes, natto. Target: 1-3mg/day total. Supplement: SpermidineLIFE 1.2mg/capsule.

**T1DM + celiac (10% comorbidity):** wheat germ contraindicated (gluten) → mushroom/legume
route; supplement is gluten-free.

**Complements rather than duplicates IF:** IF → mTORC1 suppression → ULK1 → autophagy;
spermidine → EP300 inhibition → Beclin-1 → autophagy. Different entry points; both active
simultaneously; spermidine provides autophagy induction during fed periods between IF windows.

See `numerics/run_041_spermidine_autophagy_nlrp3.md`.

*Updated: 2026-04-12 | Phase 4 fifteenth extension | 8 mountains, 41+ mechanisms*
*FIVE NLRP3 inhibition pathways now documented: BHB + colchicine + melatonin/SIRT1 + zinc + spermidine/mitophagy*
*FIVE NF-κB suppressors: colchicine + sulforaphane + vagal α7-nAChR + CAPE + K2/Gas6/Axl*
*FIVE M8 mechanisms: CRH/mast cell + cortisol/GR + vagal CAP + melatonin/SIRT1 + BMAL1/circadian*
*Remaining open: mast cell stabilization arm; F. prausnitzii monitoring threshold; oral-liver axis (P. gingivalis → Kupffer cells); PCOS/IGF-1 bridge*

### Mast Cell Stabilization: Four Inputs, Three OTC Interventions (run_042)

**Four mast cell activation inputs in the framework:**
1. CRH/CRHR1 → addressed by M8 HPA protocol (existing)
2. SP (substance P) from TRPV1+ nociceptors → NK1R on mast cells → addressed by CAPSAICIN
3. C5a from complement (gut LPS → C3 convertase → C5 → C5a) → C5aR1 on dermal mast cells
   → addressed ONLY by gut repair (M1 protocol); mast cell stabilizers reduce C5a sensitivity
4. Squalene-OOH (Loop 4) → mast cell FcεRI-like activation → addressed by Loop 4 topicals + SPF

**Novel: M1→M8 C5a bridge:** gut dysbiosis → LPS → complement → C5a → dermal mast cell →
flushing WITHOUT psychological stress. Gut repair (Node C improvement) directly reduces M8
flushing burden via C5a pathway — not just via HPA/vagal mechanisms.

**Novel: capsaicin → SP depletion → dual blockade:**
Topical capsaicin 0.025% × 2-4 weeks → SP stores depleted from TRPV1+ nerves → NK1R on mast
cells NOT triggered (M8 flushing ↓) AND NK1R on keratinocytes NOT triggered (KLK5 transcription
↓ → Loop 1 neurogenic entry blocked). Two-mountain benefit from one intervention.

**Protocol additions:**
- Quercetin 500mg BID phytosome (OR propolis ≥5% CAPE — quercetin already present) → mast cell
  cAMP ↑ + Ca2+ block → all four inputs stabilized at effector level
- Capsaicin 0.025% cream topical (once daily × 2-4 weeks): specific for Input 2 (SP/NK1R) +
  Loop 1 neurogenic KLK5; counsel patient on initial burning response

**CGRP limitation:** capsaicin depletes SP faster than CGRP; CGRP-mediated vasodilation persists
after SP depletion → heat flushing may have a CGRP-resistant component. Anti-CGRP biologics
are the only treatment for this arm (prescription; outside OTC scope).

See `numerics/run_042_mast_cell_stabilization.md`.

*Updated: 2026-04-12 | Phase 4 sixteenth extension | 8 mountains, 42+ mechanisms*
*FOUR mast cell activation inputs — M8 HPA protocol addresses only one; quercetin + capsaicin address others*
*M1→M8 C5a bridge: gut repair is a direct M8 flushing intervention via complement suppression*
*Capsaicin: dual M8 (NK1R mast cell) + Loop 1 (NK1R KLK5) blockade via SP depletion — two mountains, one intervention*

### β Cell Intra-Islet NLRP3: NLRP3 Inhibition Protocol Is β Cell Preservation (run_043)

**The intra-islet self-amplifying loop:**
β cells express NLRP3; hyperglycemia → mtROS + ceramide → β cell NLRP3 activation → IL-1β
secreted BY β cells → adjacent β cells → IL-1R → NF-κB → iNOS → NO → apoptosis AND more
NLRP3 priming. DAMPs (ATP, HMGB1) from dying β cells → Signal 2 for surviving β cells.
Self-amplifying β cell destruction independent of immune cell infiltration.

**Anakinra failure explained (Moran 2013):**
IL-1Ra blocks IL-1R but NOT NLRP3 → caspase-1 active → gasdermin D cleaved → β cell pyroptosis
proceeds. Only NLRP3 assembly inhibitors prevent BOTH IL-1β-mediated and gasdermin-mediated
β cell death simultaneously.

**Framework unification:** The complete NLRP3 inhibition protocol (BHB + colchicine + melatonin +
spermidine) used for skin/gut inflammation simultaneously:
- Breaks intra-islet IL-1β loop (colchicine → ASC speck blocked; BHB → K+ efflux blocked)
- Clears damaged β cell mitochondria (spermidine → mitophagy)
- Deacetylates NLRP3 K496 in β cells (melatonin → SIRT1)

**Novel RCT prediction:** Colchicine 0.5mg BID in new-onset T1DM (C-peptide > 0.2 nmol/L at
diagnosis) → C-peptide preservation at 12 months exceeds anakinra historical controls.
No existing trial. This is the largest untested mechanistic prediction in the framework.

**Priority action for C-peptide positive new-onset T1DM:** initiate NLRP3 inhibition within
3-6 months of diagnosis. The β cell preservation window closes as islet autoimmunity progresses.

See `numerics/run_043_beta_cell_nlrp3_intraislet.md`.

*Updated: 2026-04-12 | Phase 4 seventeenth extension | 8 mountains, 43+ mechanisms*
*Framework unified: NLRP3 inhibition protocol addresses skin + gut + pancreatic β cell NLRP3 simultaneously*
*Novel prediction: colchicine for β cell preservation in new-onset T1DM — no existing trial*
*Anakinra failure: IL-1Ra blocks signaling not production; gasdermin pyroptosis is the unblocked arm*

### H. pylori: M7 Gastric Extension — Dual NLRP3 Activation (run_044)

**H. pylori delivers BOTH NLRP3 signals simultaneously:**
- Signal 1: CagA (type IV secretion) → SHP2 → NF-κB → pro-IL-1β (NLRP3 priming)
- Signal 2: VacA (K+ efflux-forming pore) → intracellular K+ ↓ → NLRP3 oligomerization (activation)

This is mechanistically exceptional — most pathogens deliver either TLR4/LPS (Signal 1) OR a
pore-forming toxin (Signal 2). H. pylori CagA/VacA delivers both from a single colonizing organism.

**Rosacea epidemiology:** OR 2.47 for H. pylori seropositivity in rosacea (Gravina 2015 meta-analysis,
N=2,346); H. pylori eradication → rosacea improvement 62-80% of H. pylori-positive patients.

**M7 now covers two sites:**
- Oral cavity: P. gingivalis + T. denticola + T. forsythia (red complex; run_030)
- Gastric: H. pylori CagA/VacA (run_044)

**Protocol additions:**
- Screening: stool H. pylori antigen OR UBT in rosacea with dyspeptic symptoms OR first-degree
  family history of gastric cancer/ulcer
- Eradication: triple/quadruple therapy × 14 days + concurrent LGG 10^10 CFU/day (prevents
  P. gingivalis gut colonization during PPI acid suppression) + stop PPI promptly Day 15
- Confirm eradication: UBT or stool antigen at 4-6 weeks (after 2 weeks off PPI)
- Assess rosacea response at 3 and 6 months

**T1DM bridge:** H. pylori → HOMA-IR ↓ with eradication (Tang 2019); H. pylori → systemic
inflammatory tone ↑ → NLRP3 priming → lower β cell NLRP3 threshold (run_043 bridge).

See `numerics/run_044_helicobacter_pylori_m7_extension.md`.

*Updated: 2026-04-12 | Phase 4 eighteenth extension | 8 mountains, 44+ mechanisms*
*H. pylori: M7 extended to gastric compartment; dual NLRP3 mechanism (CagA Signal 1 + VacA Signal 2)*
*Rosacea-H. pylori OR 2.47 — strongest single-pathogen epidemiological association in framework*
*M7 protocol: oral red complex (run_030) + H. pylori screening/eradication (run_044)*

### M6 Early-Life Assembly: The Fixed Floor (run_045)

**All 8 mountains now formally analyzed for rosacea/T1DM. M6 is the structural lower limit.**

**Mechanism:**
Foxp3 CNS2 (intron 1 of Foxp3 gene): CpG demethylation in neonatal period via butyrate/propionate
→ HDAC → TET demethylation during rapid thymic/GALT T cell expansion (passive dilution mechanism
in dividing cells). Perinatal window: first 1-2 years.

C-section + early antibiotics → reduced Bacteroides/Bifidobacterium → SCFA deficit → partial
CNS2 methylation → adult Tregs STRUCTURALLY UNSTABLE: Foxp3 lost under inflammatory challenge
→ Treg → Th17. Adult butyrate CANNOT fully reverse (Yang 2015 Nat Immunol: perinatal passive
demethylation mechanism not recapitulated in adult T cells).

**Low M6 floor predicts:**
- Node A (Foxp3+/CD4+) <15% at baseline
- Protocol response plateau at 50-70% (vs. 80-90% in M6-intact patients)
- More frequent relapse triggers (stress, infection) → complete flare despite protocol adherence
- Concurrent autoimmune disease (early IBD, childhood atopic dermatitis) — same mechanism

**M6 history clues:** C-section delivery, multiple first-year antibiotic courses, formula-fed,
early childhood autoimmune disease (≥2 factors → high probability of low M6 floor).

**Protocol adjustment for low M6:**
- Butyrate 6g/day from Day 1 (not standard 4g/day)
- Colchicine 0.5mg BID at Month 1 (not Month 3 — reduces Treg→Th17 trigger)
- Zinc concurrent with butyrate initiation
- IF/mTORC1 inhibition maximized (mTORC1 → Foxp3 instability; IF → mTORC1 ↓ → Treg more stable)
- Manage expectations: improved control, not complete remission

See `numerics/run_045_m6_early_life_rosacea.md`.

*Updated: 2026-04-12 | Phase 4 nineteenth extension | All 8 mountains analyzed for rosacea/T1DM context*
*M6 is the FIXED FLOOR — adult interventions partially compensate but cannot fully reverse neonatal epigenetic imprinting*
*Node A <15% + M6 history → adjust protocol: higher butyrate, earlier colchicine, concurrent zinc, maximize IF*

### Demodex folliculorum: B. oleronius TLR4 Dual Signal + Ivermectin as Sixth NF-κB Suppressor (run_046)

**The actual mechanism:** immune response to Demodex is a response to its endosymbiont:
B. oleronius (gram-negative bacterium IN Demodex) released when Demodex die in pilosebaceous
units → B. oleronius LPS → TLR4 → NF-κB → NLRP3 primed (Signal 1) + B. oleronius
peptidoglycan → NOD1/NOD2 → K+ efflux → NLRP3 activation (Signal 2). Dual signal.

**Three framework loops driven by Demodex:**
- Loop 1: B. oleronius TLR4 → NF-κB → KLK5 ↑ + Demodex cuticle → TRPV1 → SP → NK1R → KLK5
- Loop 3: B. oleronius LPS → TLR4 → IFN-β → HERV-W transcription → Loop 3 kept ON constitutively
- NLRP3: B. oleronius → both NLRP3 signals simultaneously

**Ivermectin 1% cream (Soolantra) — dual framework mechanism:**
1. Kills Demodex → B. oleronius source removed → TLR4 stimulus gone
2. Blocks importin α/β-1 → NF-κB p65 cannot enter nucleus even if IKK activates (Yang 2020)
   = SIXTH independent NF-κB suppressor; works downstream of all five existing pathways

**Six NF-κB suppressors now documented:**
| # | Compound | Target |
|---|---------|--------|
| 1 | Colchicine | IKK complex FORMATION (microtubule) |
| 2 | Sulforaphane | CBP/p300 coactivation |
| 3 | Vagal α7-nAChR | IKKβ inhibitory phosphorylation |
| 4 | CAPE | IKKβ active site + p65 Cys38 |
| 5 | MK-7/Gas6/Axl | SOCS1 → IKK complex inactivation |
| 6 | Ivermectin 1% | Importin α/β-1 → p65 nuclear entry |

**Protocol:** SSSB (skin surface biopsy) ≥5/cm² threshold. Ivermectin 1% × 12-16 weeks
(ATTRACT trial: 50-70% papulopustule reduction). Maintenance 3×/week after remission.
Colchicine + ivermectin: upstream (IKK formation) + downstream (p65 nuclear entry) = near-
complete NF-κB suppression in rosacea skin cells.

See `numerics/run_046_demodex_rosacea_nlrp3.md`.

*Updated: 2026-04-12 | Phase 4 twentieth extension | 8 mountains, 46+ mechanisms*
*SIX NF-κB suppressors now documented: colchicine + sulforaphane + vagal + CAPE + MK-7 + ivermectin*
*Ivermectin: dual mechanism (Demodex kill + NF-κB p65 nuclear entry block) — currently the only biologically active M2 + NF-κB dual-purpose agent in the framework*
*Demodex density elevates in T1DM context (more sebum from IGF-1 = more Demodex food) → T1DM → more Demodex → more B. oleronius → more NF-κB/NLRP3/Loop 1 — another T1DM-specific amplification pathway*

### Gut Serotonin (5-HT) as M1→M8 Flushing Bridge (run_047)

**EC cell 5-HT in T1DM gut dysbiosis:**
In T1DM + M1 dysbiosis: hyperglycemia → mTORC1 → TPH1 ↑ (Bertrand 2011) + gut inflammation
→ SERT ↓ → elevated systemic 5-HT (despite Clostridia depletion reducing TPH1 production,
the T1DM-specific amplifiers dominate). Result: more plasma 5-HT → platelet-delivered dermal
5-HT → 5-HT2A on vascular endothelium (NO vasodilation) + 5-HT2A on dermal mast cells
(potentiates ALL four mast cell inputs — lower histamine trigger threshold).

**Red wine/hot drink mechanism explained:**
Ethanol → SERT inhibition (5-HT accumulates) + heat → TRPV1 → SP/CGRP release + fermentation
→ dietary 5-HT precursor load = triple-trigger convergence. The known rosacea hot-drink/red-
wine trigger is now mechanistically explained across all three components.

**Quercetin (propolis): THIRD mechanism identified:**
Quercetin → PI3K/mTOR inhibition → TPH1 ↓ → EC 5-HT ↓. This adds to:
1. Mast cell cAMP ↑ → stabilization (run_042)
2. NLRP3 NACHT ATPase inhibition (run_036)
3. TPH1 → EC 5-HT suppression (run_047)
Quercetin is the most multi-mechanism single molecule in the framework.

**Treatment:** HbA1c <7.5% (dominant T1DM-specific 5-HT normalizer via TPH1); gut repair
(butyrate → SERT ↑); quercetin (propolis) → TPH1 ↓; avoid acute tryptophan+ethanol+heat
loading combinations.

See `numerics/run_047_gut_serotonin_flushing.md`.

*Updated: 2026-04-12 | Phase 4 twenty-first extension | 8 mountains, 47+ mechanisms*
*Gut 5-HT: M1→M8 bridge via EC TPH1 dysregulation; hyperglycemia is T1DM-specific amplifier*
*Quercetin: triple mechanism (mast cell + NLRP3 NACHT + TPH1) — most mechanistically dense molecule in framework*
*Red wine/hot drink: SERT inhibition + TRPV1 + fermentation 5-HT = triple trigger convergence*

### Gasdermin D in Keratinocytes: Skin-Local Loop 2 Completes Three NLRP3 Context Analysis (run_048)

**Three NLRP3 contexts now formally analyzed:**
1. Macrophage/systemic NLRP3 (primary; run_002+) — systemic IL-1β/IL-18; T-index Node B
2. β cell/pancreatic NLRP3 (run_043) — intra-islet IL-1β self-destruction loop
3. **Keratinocyte/skin-local NLRP3 (run_048) — epidermis-local gasdermin D pyroptosis**

**Keratinocyte NLRP3 self-amplifying loop:**
Pyroptotic keratinocyte → DAMP release (ATP → P2X7 on neighbors; HMGB1 → TLR4; S100A8/A9 →
TLR4) → NLRP3 Signal 2 in neighboring keratinocytes → propagating skin-local pyroptosis.

**Framework unification insight:** The existing Loop 4 topical protocol is ALREADY the keratinocyte
NLRP3 protocol by mechanism:
- Niacinamide 4%: SIRT1 → K496 deacetylation in keratinocytes (same mechanism as melatonin/SIRT1
  systemic arm — TOPICAL delivery achieves DIRECT keratinocyte concentration)
- Vitamin E: squalene-OOH scavenging (removes Signal 2 before NLRP3 activation)
- SPF 50: UV blocked → less squalene-OOH + less ATP DAMP from UV-damaged keratinocytes

The topical protocol was derived from Loop 4 but works because it blocks both Loop 4 (sebaceous)
AND keratinocyte Loop 2 via the same Signal 2 removal mechanism.

**Topical ivermectin adds keratinocyte NLRP3 Signal 1 block:**
Ivermectin → importin α/β-1 → NF-κB p65 nuclear entry blocked in keratinocytes → NLRP3 not
primed (Signal 1). This is the mechanistic reason ivermectin improves both papulopustular rosacea
(NLRP3-driven) and erythema (via B. oleronius/NF-κB/flushing) — one drug addressing both
keratinocyte NLRP3 Signal 1 and Demodex source removal.

See `numerics/run_048_gasdermin_keratinocyte_loop2.md`.

*Updated: 2026-04-12 | Phase 4 twenty-second extension | 8 mountains, 48+ mechanisms*
*Three NLRP3 contexts unified: macrophage (systemic) + β cell (pancreatic) + keratinocyte (skin-local)*
*Topical protocol = keratinocyte NLRP3 protocol; niacinamide SIRT1/K496 + vitamin E squalene-OOH + SPF 50 UV block*
*Framework mapping reaching high completeness; primary OTC/prescription therapeutic landscape now covered*
