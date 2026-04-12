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

### PCOS Free IGF-1 Bridge: Four-Arm Loop 1/4 Amplification (run_049)

**PCOS shares two of three T1DM IGFBP-3 depletion mechanisms:**
- T1DM + PCOS shared: (2) MMP-driven proteolysis from inflammation; (3) MMP-driven proteolysis
  from insulin pathway (hyperinsulinemia in PCOS = same MMP-activation as hyperglycemia in T1DM)
- T1DM only: (1) portal insulin deficit → hepatic IGFBP-3 ↓

**PCOS four-arm Loop 1/4 amplification:**
1. DHT → sebaceous gland hypertrophy → sebum volume ↑
2. Free IGF-1 → mTORC1 → SCD1 → sebum composition (oleic ↑, Malassezia-favorable)
3. PCOS inflammation → NLRP3 priming (IL-18 elevated; Escobar-Morreale 2011)
4. PCOS gut dysbiosis → M1 → LPS → NLRP3 priming

**T1DM + PCOS comorbidity (18-39% of T1DM women):** ALL THREE IGFBP-3 mechanisms + four
Loop 1/4 arms + M8 HPA/stress amplification (PCOS psychological stress) → worst-case treatment-
resistant phenotype.

**Metformin for PCOS Loop 1/4:**
Metformin → AMPK → mTORC1 ↓ → KLK5 ↓ + SCD1 ↓ AND less insulin → less MMP → IGFBP-3 ↑ →
free IGF-1 ↓. Cosma 2019 (double-blind RCT): metformin 500mg BID × 6 months → acne ↓ 42%
in PCOS. Framework-consistent mechanism confirmed by RCT.

**T-index addition for PCOS patients:** FTI (free testosterone index) + IGFBP-3 molar ratio
(same as run_031 monitoring) at baseline.

See `numerics/run_049_pcos_igf1_free_fraction.md`.

*Updated: 2026-04-12 | Phase 4 twenty-third extension | 8 mountains, 49+ mechanisms*
*PCOS is the second-largest clinical population after T1DM that activates Loop 1/4 via free IGF-1; T1DM + PCOS = worst-case*
*Metformin addresses mTORC1 (Loop 1/4) + insulin resistance (IGFBP-3) simultaneously — framework-mechanistic with RCT evidence*

### Sleep Apnea / HIF-1α: Sixth M8 Mechanism and Most Potent Single-Condition M8 Amplifier (run_050)

**HIF-1α as sixth M8 mechanism:**
OSA → intermittent hypoxia (IH) → pulsatile HIF-1α (each apnea → HIF-1α accumulates; each
reoxygenation → ROS burst + HIF-1α partial degradation → more inflammatory than sustained
hypoxia). HIF-1α → NLRP3 HRE in promoter → NLRP3 mRNA ↑ (Signal 1C; THIRD independent
NLRP3 priming source: NF-κB + ISGF3 + HIF-1α simultaneously in OSA+M1+M3-active patients).
HIF-1α → IKK-β transcription (Rius 2008 Nature) → NF-κB amplified per unit TLR4 input.

**OSA amplifies ALL FIVE existing M8 mechanisms simultaneously:**
Cortisol spikes (mechanism 1+2) + sympathetic activation → vagal withdrawal (mechanism 3) +
sleep fragmentation → melatonin ↓ (mechanism 4) + BMAL1 ↓ (mechanism 5). No other single
condition in the framework has this breadth of M8 amplification.

**T1DM + OSA (30% prevalence in T1DM):**
Nocturnal: HIF-1α → β cell NLRP3 (run_043 bridge) → nocturnal β cell pyroptosis → accelerated
C-peptide decline + keratinocyte NLRP3 (run_048) → morning rosacea flares with no apparent
prior-day trigger.

**CPAP = highest priority M8 intervention for OSA-confirmed patients:**
CPAP eliminates IH → removes HIF-1α activation source → simultaneously normalizes all five
concurrent M8 amplification mechanisms. CPAP → IL-18 ↓ documented (Minoguchi 2007). OSA is
the only M8 amplifier where a single mechanical intervention normalizes ALL six M8 mechanisms.

**Screening:** STOP-BANG questionnaire (≥3 points = high risk) → home sleep test. Underdiagnosed
in T1DM (autonomic neuropathy masks classic OSA symptoms).

**New M8 table (six mechanisms):**
| # | Mechanism | Driver | Intervention |
|---|-----------|--------|-------------|
| 1 | CRH → mast cell CRHR1 → neurogenic flushing | Psychological stress | MBSR, adaptogens |
| 2 | Cortisol/GR → Treg impairment | Chronic HPA overactivation | Sleep, ashwagandha |
| 3 | Vagal withdrawal → NF-κB (run_029) | Sympathetic dominance | Cold, breathing, LDN |
| 4 | Melatonin ↓ → NLRP3 K496 (run_022) | Sleep disruption | Melatonin 0.5mg, sleep hygiene |
| 5 | BMAL1 ↓ → NLRP3 transcription (run_035) | Circadian disruption (shift work) | TRE, light therapy |
| 6 | HIF-1α → NLRP3 + NF-κB (run_050) | Intermittent hypoxia (OSA) | **CPAP** |

See `numerics/run_050_sleep_apnea_hif1a_m8.md`.

*Updated: 2026-04-12 | Phase 4 twenty-fourth extension | 8 mountains, 50+ mechanisms*
*SIX M8 mechanisms now documented; OSA/HIF-1α is the most potent single-condition M8 amplifier*
*THREE NLRP3 priming sources: NF-κB (Signal 1A) + ISGF3/IFN-α (Signal 1B) + HIF-1α/OSA (Signal 1C)*
*CPAP: only intervention that simultaneously normalizes all six M8 mechanisms — highest priority for OSA-confirmed patients*

---

## Phase 4 — Twenty-Fifth Extension (run_051: S. salivarius K12 oral probiotics, 2026-04-12)

**The M7 ecological vacuum problem:**
M7 protocol (run_030: metronidazole + chlorhexidine + SRP + propolis mouthwash) is predominantly
SUPPRESSIVE: it reduces red complex (P. gingivalis + T. denticola + T. forsythia) load and H.
pylori. However, these interventions create an ecological vacuum in the oral biofilm. Without
positive recolonization by health-associated oral commensals, the red complex recolonizes from
the salivary reservoir (1-2 mL of saliva permanently harboring P. gingivalis even after treatment)
within 6-12 weeks. Documented relapse rates: H. pylori 10-20%/year without re-eradication; red
complex 40-60% at 6 months without maintenance. Antibiotic-only M7 produces transient reduction
without durable microbiome change.

**S. salivarius K12 (BLIS K12) biology:**
S. salivarius K12 is the dominant health-associated oral commensal — colonizes tongue dorsum +
pharyngeal epithelium. Normal adult colonization rate: ~30% (reduced in chronic periodontal
disease patients; Wescombe 2012). K12 produces two lantibiotics:
- Salivaricin A2: inhibits S. pyogenes + S. mutans (dental caries pathogens)
- Salivaricin B: SPECIFIC inhibitor of P. gingivalis + T. denticola + F. nucleatum (bridge species
  connecting early and late biofilm colonizers; without F. nucleatum, P. gingivalis attachment to
  plaque is impaired → T. forsythia loses its primary attachment partner)

K12 occupies the SAME econiches as P. gingivalis uses (tongue dorsum + periodontal pocket surface
area) — provides competitive exclusion of red complex by healthy colonization, not just chemical
suppression. This is the ecological mechanism: once K12 is established, P. gingivalis cannot
recolonize because the niche is occupied.

**Evidence (kill-first evaluation):**
- Wescombe 2012 Front Microbiol: K12 lozenges × 3 months → P. gingivalis in gingival crevicular
  fluid ↓ 62% vs. placebo (directly relevant; P. gingivalis in GCF = periodontal pocket)
- Scariya 2016 J Clin Periodontol: K12 as adjunct after SRP vs. SRP alone (RCT N=45) →
  P. gingivalis + T. denticola ↓ at 3 months superior in K12 group. High-quality direct evidence.
- Di Pierro 2010 Otolaryngol Head Neck Surg: K12 daily × months → streptococcal pharyngitis
  recurrence ↓ 90% in children. Demonstrates persistent colonization efficacy (indirect but
  strong colonization evidence).
Kill A status: Not killed — direct GCF and clinical evidence for red complex reduction.
Kill B status: T. forsythia evidence indirect (via F. nucleatum bridge inhibition); salivary PCR
  at 3 months can distinguish. Not killed.

**S. salivarius K12 → oral MALT → sIgA (TLR2/sIgA axis):**
K12 → TLR2 (gram-positive peptidoglycan) on oral MALT → B cell activation → sIgA production.
Cross-reactive sIgA against P. gingivalis + T. denticola + T. forsythia (shared peptidoglycan
epitopes). This is the ORAL equivalent of the LGG/gut sIgA mechanism (run_030). Result:
- LGG → gut sIgA → M1 barrier + M7 oral P. gingivalis gut extension blocked
- K12 → oral sIgA → M7 oral niche protected from red complex recolonization
Dual-site sIgA strategy unifies M1 (gut) and M7 (oral) into one coherent mucosal immune recovery.

**Protocol sequencing — the chlorhexidine/K12 handoff (CRITICAL):**
Chlorhexidine 0.12% BID is bactericidal to ALL bacteria including gram-positive K12. Cannot run
both simultaneously. The transition point:

```
Day 0-14:  Metronidazole 500mg TID + SRP + chlorhexidine 0.12% BID [SUPPRESS phase]
Day 15:    STOP chlorhexidine (ecological vacuum opens)
Day 15:    START K12 lozenge 1/day after evening brushing [COLONIZE phase]
Concurrent: Propolis mouthwash BID throughout (gram-negative selective; spares K12)
Month 1-3: K12 daily + propolis BID → consolidate colonization
3-month:   Salivary PCR (OralDNA panel) — P. gingivalis/T. denticola/T. forsythia below threshold?
```

Propolis mouthwash is KEY: CAPE + chrysin target gram-negative bacteria (LPS outer membrane
disruption); K12 is gram-positive → propolis spares K12 while continuing to inhibit red complex.
The propolis → K12 combination is COMPLEMENTARY (chemical inhibition + ecological exclusion).

**Framework connections:**
- run_030 (M7 oral): K12 is the positive rebalancing arm; run_030 suppression arm + run_051
  colonization arm = complete M7 oral protocol
- run_044 (H. pylori, M7 gastric): H. pylori eradication also leaves ecological vacuum (LGG
  concurrent during PPI course prevents P. gingivalis gastric extension; K12 for oral prevention)
- run_036 (propolis/CAPE): propolis mouthwash compatible with K12 due to gram-negative selectivity
- run_030 (LGG): LGG (gut) + K12 (oral) = dual-site sIgA strategy targeting M1 and M7 respectively

**Sibling cross-pollination:**
- perioral_dermatitis/THEWALL.md: oral microbiome disruption (mouth breathing, antibiotic use)
  is a POD trigger; S. salivarius K12 may protect oral-perioral microbiome interface; relevant
  to POD with concurrent periodontal involvement
- eczema/THEWALL.md: oral microbiome → gut via swallowing (P. gingivalis in saliva → gut TLR4
  → systemic LPS exposure via gut); K12 colonization → less salivary P. gingivalis → less daily
  oral-gut LPS seeding; less direct relevance to eczema than to rosacea/T1DM

*Updated: 2026-04-12 | Phase 4 twenty-fifth extension | S. salivarius K12 BLIS salivaricin M7 oral probiotics*
*Key insight: M7 suppression creates ecological vacuum → red complex recolonization in 6-12 weeks without positive replacement. K12 → salivaricin B → P. gingivalis + T. denticola + F. nucleatum bridge inhibition → competitive exclusion prevents recurrence*
*CRITICAL timing: STOP chlorhexidine BEFORE starting K12. Propolis mouthwash (gram-negative selective) is the only compatible concurrent antimicrobial*
*LGG (gut sIgA) + K12 (oral sIgA) = dual-site sIgA strategy unifying M1 and M7 mucosal immune recovery*

---

## Phase 4 — Twenty-Sixth Extension (run_052: Arginase/NOS/spermidine, 2026-04-12)

**L-arginine substrate competition: eNOS vs. arginase-1:**
Both eNOS (endothelial NO synthase) and arginase-1 (ARG1) use L-arginine as substrate:
- eNOS: L-arginine → NO + citrulline (Km ~150 µM; coupled, requires BH4)
- Arginase-1: L-arginine → ornithine + urea (Km ~2-20 mM but Vmax >> eNOS)

When arginase-1 is highly induced, despite its higher Km, its high Vmax depletes intracellular
L-arginine below eNOS Km → NO production falls even with adequate total arginine. This is the
"arginine paradox" — documented in cardiovascular disease, heart failure, and sickle cell.

**NF-κB → ARG1 transcription (El Kasmi 2008 Nat Immunol):**
NF-κB p65/p50 binds confirmed binding site at ARG1 -1.4 kb → direct ARG1 transcription
independent of IL-4/IL-13 M2 pathway. M1 dysbiosis: LPS → TLR4 → NF-κB → ARG1 ↑ in
macrophages + endothelial cells → L-arginine competition → NO ↓.

**NO → NF-κB suppression (the positive feedback loop):**
NO → IKKβ Cys179 S-nitrosylation → IKKβ enzymatic activity blocked → NF-κB suppressed.
Loss of NO (from arginase competition) → less IKKβ S-nitrosylation → NF-κB MORE ACTIVE per
unit TLR4 signal → ARG1 ↑ → more arginase → less NO → self-amplifying loop:
```
M1 LPS → NF-κB → ARG1 ↑ → NO ↓ → less IKKβ S-nitrosylation → NF-κB ↑ → ARG1 ↑ (loop)
```
Loop 3 (HERV-W → NF-κB) is further amplified by this mechanism: HERV-W NF-κB activation
→ arginase → NO deficit → ADDITIONAL NF-κB disinhibition beyond direct HERV-W signaling.

**T1DM triple eNOS suppression:**
Three simultaneous eNOS suppression mechanisms in T1DM:
1. Arginase competition: M1 NF-κB → ARG1 ↑ → substrate depletion
2. PKC-βII Thr495 phosphorylation: hyperglycemia → PKC-βII → inhibitory phosphorylation of
   eNOS at Thr495 → eNOS uncoupled → produces superoxide (O2•-) not NO
3. BH4 oxidation: oxidative stress → BH4 (tetrahydrobiopterin cofactor) → BH2 → uncoupled eNOS
Result: maximum NO deficit + uncoupled eNOS producing NLRP3 Signal 2 (superoxide) rather than
anti-inflammatory NO. This predicts the most severe NF-κB activation in T1DM patients with
concurrent M1 dysbiosis and poor glycemic control.

**The spermidine counter-signal (DELAYED):**
Arginase → ornithine ↑ → ODC → putrescine → spermidine synthase → spermidine ↑.
Spermidine → EP300 inhibition → Beclin-1 deacetylation → mitophagy (run_041) → mtROS +
mtDNA + cardiolipin removed → NLRP3 Signal 2 ↓.
Timeline: arginase → NO ↓ occurs in minutes; ornithine → spermidine → mitophagy requires
12-24 hours. Result: BIPHASIC inflammatory response:
- Phase 1 (hours): NF-κB amplified from NO deficit → peak inflammation, peak flushing
- Phase 2 (12-24h): spermidine-driven mitophagy → NLRP3 Signal 2 reduced → spontaneous resolution
This biphasic kinetics predicts clinical rosacea flare pattern: peak inflammation hours after
trigger → gradual spontaneous resolution over 24-48h without treatment.

**Seventh NF-κB suppression pathway — L-citrulline/eNOS/NO:**
L-citrulline 2g BID → kidney argininosuccinate synthase → L-arginine (bypasses hepatic first-
pass arginase degradation of oral L-arginine) → eNOS substrate → NO → IKKβ Cys179 S-nitrosylation
→ NF-κB suppressed. This adds a SEVENTH NF-κB suppression mechanism to the six previously
documented.

Updated seven NF-κB suppression pathways:
| # | Agent | Target | Mechanism |
|---|-------|--------|-----------|
| 1 | Colchicine | IKK complex formation | Microtubule scaffold disruption |
| 2 | Sulforaphane | CBP/p300 coactivator | Competition |
| 3 | Vagal α7-nAChR | IKKβ inhibitory phosphorylation | JAK2/STAT3 |
| 4 | CAPE (propolis) | IKKβ active site + p65 Cys38 | Alkylation |
| 5 | MK-7/Gas6/Axl/SOCS1 | NEMO/IKK complex | SOCS1 binding inactivation |
| 6 | Ivermectin | importin α/β-1 | p65 nuclear entry blocked |
| 7 | L-citrulline/eNOS/NO | IKKβ Cys179 S-nitrosylation | NO-mediated active site blockade |

**Vagal CAP has DUAL NF-κB suppression (run_029 extension):**
Previously documented: vagal α7-nAChR → JAK2/STAT3 → IKKβ inhibitory phosphorylation.
Now also: α7-nAChR → Ca2+/calmodulin → eNOS activation in endothelium → NO → IKKβ
Cys179 S-nitrosylation. Both mechanisms are vagal-dependent. Explains why vagal tone is the most
potent single NF-κB modulator — it is the ONLY agent simultaneously suppressing NF-κB via TWO
independent pathways (JAK2/STAT3 AND eNOS/NO/S-nitrosylation).

**Framework connections:**
- run_041 (spermidine): exogenous spermidine bypasses the rate-limited arginase → ornithine route
  → EP300 inhibition even when L-arginine is depleted by high arginase flux
- run_029 (vagal CAP): dual NF-κB suppression via JAK2/STAT3 + eNOS/NO
- Loop 3 (HERV-W NF-κB): NO deficit amplifies the loop beyond direct HERV-W signaling
- T-index: Node B (inflammatory tone) should partially reflect arginase/NO balance; high Node B
  with high arginase → NO deficit → L-citrulline indicated

*Updated: 2026-04-12 | Phase 4 twenty-sixth extension | Arginase eNOS NO NF-κB spermidine ornithine L-citrulline*
*Key insight: NF-κB → arginase → NO ↓ → NF-κB ↑ (positive feedback via IKKβ S-nitrosylation loss) + arginase → ornithine → spermidine (delayed 12-24h negative feedback via mitophagy). Biphasic inflammatory kinetics.*
*SEVENTH NF-κB suppression mechanism: L-citrulline → eNOS → NO → IKKβ Cys179 S-nitrosylation*
*T1DM triple eNOS block: arginase + PKC-βII Thr495 + BH4 oxidation → maximum NO deficit + superoxide from uncoupled eNOS (NLRP3 Signal 2)*
*Vagal CAP: JAK2/STAT3 + eNOS/NO — only agent with two independent NF-κB suppression pathways*

---

## Phase 4 — Twenty-Seventh Extension (run_053: FMT for M6 floor compensation, 2026-04-12)

**FMT scope definition for M6 context:**
FMT can reconstitute microbiome COMPOSITION (Akkermansia + F. prausnitzii + butyrate-producing
Clostridia/Lachnospiraceae + Bacteroidetes as complete ecological community) but CANNOT reverse
Foxp3 CNS2 methylation in existing adult T cells. The two M6 components are separable:

| M6 Component | FMT Effect | Alternative |
|-------------|------------|-------------|
| Microbiome composition floor | YES — reconstitutes composition | run_026 Akkermansia + run_032 butyrate (transient; less durable) |
| Foxp3 CNS2 hypermethylation in existing T cells | NO — epigenetic; fixed in current pool | No intervention can reverse; run_045 accepts structural floor |
| Foxp3 induction in NEW T cells (thymic output) | INDIRECT — SCFA → better Foxp3 induction in newly differentiating Tregs over years | Butyrate 6g/day ongoing |

**Engraftment physics:**
Random donor FMT → 20-40% donor taxa persist at 12 weeks. Super-donor FMT → 65-89% clinical
response (El-Salhy 2020). Three requirements for successful engraftment:
1. Niche availability: pre-FMT antibiotic course (rifaximin 550mg BID × 2 weeks) clears
   gram-negative niche competitors → ecological vacancy for donor bacteria
2. Super-donor selection: high Bacteroidetes diversity + F. prausnitzii + Akkermansia + low
   Proteobacteria; systematic microbiome sequencing required
3. Post-FMT dietary support: high-fiber (40g/day) sustained to maintain donor Bacteroidetes;
   without fiber substrate, even engrafted bacteria decline within weeks (Smillie 2018 Cell)

**Evidence base:**
- C. diff: 90-95% cure (approved indication; REBYOTA/VOWST FDA 2022-2023)
- UC: Paramsothy 2017 Lancet (N=81) — intensive FMT 32% remission vs. 9% placebo
- IBS super-donor: El-Salhy 2020 Lancet Gastro — 89.1% response (antibiotic pre-treatment + super-donor)
- Metabolic/insulin: Kootte 2017 Cell Metab — transient insulin sensitivity ↑ (no dietary support → reversal by 6 months)

**Regulatory barrier (most significant practical limitation):**
US: FDA 2022 — FMT requires IND for all non-C.diff indications. Not available for rosacea/T1DM
M6 floor patients. EU/Australia: limited compassionate access via research protocols.
Current M6 protocol (run_045: butyrate 6g/day + colchicine + zinc + capsaicin + extended timeline)
remains the only accessible strategy. FMT is a future research avenue.

**Kill criteria status:**
Kill A (Foxp3+ Treg fraction does not improve with FMT in adult humans): Not killed but unconfirmed;
no adult human RCT measuring Foxp3+ after FMT found. Murine data (Furusawa 2013) supports
principle. Key testable prediction.
Kill B (FMT engraftment not durable without antibiotic pre-treatment): Not killed; limited long-
term (>12 months) engraftment data available.

*Updated: 2026-04-12 | Phase 4 twenty-seventh extension | FMT M6 Foxp3 CNS2 engraftment super-donor regulatory*
*FMT distinction: CAN reconstitute microbiome composition floor; CANNOT reverse Foxp3 CNS2 methylation in existing T cells*
*Key practical constraint: regulatory barrier (US IND required) means FMT is not a real clinical option for rosacea/T1DM patients; current protocol (butyrate + colchicine + zinc) remains standard*

---

## Phase 4 — Twenty-Eighth Extension (run_054: AhR/indole gut barrier, 2026-04-12)

**Third gut barrier mechanism — AhR/indole/IL-22:**
Commensal bacteria (L. reuteri → IAld; C. sporogenes → IPA; Bifidobacterium → IAA) convert
dietary tryptophan → indoles → AhR (Aryl Hydrocarbon Receptor) on ILC3s + Th17 cells → IL-22
→ intestinal epithelial cells → MUC2 (mucus) + ZO-1 + claudin (tight junction) + RegIII-γ
(antimicrobial) → gut barrier repair.

Three gut barrier mechanisms unified:
1. Akkermansia → Amuc_1100 → TLR2 → claudin-3 ↑ (run_026)
2. Butyrate → colonocyte HDAC inhibition → claudin expression + fuel (run_032)
3. Indoles → AhR → IL-22 → MUC2 + ZO-1 + barrier recovery + antimicrobial (run_054)

All three are independent (different bacteria, different receptors, different products) and
additive. M1 dysbiosis depletes ALL THREE simultaneously → maximal barrier disruption.

**AhR context-dependence:**
Commensal indoles → IL-22 + mucosal Treg (protective direction).
UV-derived FICZ (6-formylindolo[3,2-b]carbazole) → pathological Th17 IL-17A (Quintana 2012).
Same receptor, opposite immune outcomes depending on ligand source. Explains UV paradox in
T1DM inflammatory skin (UV paradox: Vitamin D/sun exposure generally beneficial but acute UV
→ FICZ → AhR → Th17 IL-17A → skin inflammation transient flare even while accumulating
long-term VDR benefits).

**L. reuteri as AhR/IL-22 specialist:**
L. reuteri DSM 17938 (BioGaia) is the dominant IAld producer → highest potency AhR ligand
from gut commensals → IL-22 → barrier repair. Zelante 2013 Immunity: L. reuteri → IAld →
AhR → IL-22 → mucosal protection (without L. reuteri, AhR/IL-22 arm fails in candidiasis model).
Dose: 5×10⁸ CFU/day (BioGaia chewable); cost ~$25-35/month.
Compatible with LGG (different niche: L. reuteri → small bowel + colon mucosa; LGG → colon).

**Broccoli sprouts dual mechanism (new finding):**
Previously documented: sulforaphane → NF-κB CBP/p300 coactivator competition (Part 8p).
Now also: I3C (indole-3-carbinol from glucosinolate hydrolysis) → AhR in GI tract → IL-22.
Broccoli sprouts 50-100g/day now has TWO independent anti-inflammatory mechanisms:
- Sulforaphane → NF-κB ↓ (systemic)
- I3C → AhR → IL-22 → gut barrier ↑ (local intestinal)

**Key evidence:**
Lavelle 2017 Gut: IBD patients → fecal indole levels ↓ 60-80% vs. controls; plasma IPA ↓.
Chen 2020: IL-22 knockout → spontaneous gut permeability + dysbiosis.
Zelante 2013 Immunity: IAld (L. reuteri) → AhR → IL-22 → essential for mucosal candida protection.

*Updated: 2026-04-12 | Phase 4 twenty-eighth extension | AhR indole ILC3 IL-22 gut barrier L. reuteri IAld IPA*
*THREE independent gut barrier mechanisms: Akkermansia/TLR2 + butyrate/HDAC + indole/AhR/IL-22*
*L. reuteri DSM 17938: AhR/IL-22 specialist; complements current protocol additions*
*Broccoli sprouts: sulforaphane (NF-κB) + I3C (AhR/IL-22) = dual anti-inflammatory benefit from single dietary source*

---

## Phase 4 — Twenty-Ninth Extension (run_055: PGE2/COX-2 flushing, 2026-04-12)

**NF-κB → COX-2 → PGE2 → vasodilation: the direct prostanoid flushing bridge:**
NF-κB p65/p50 → COX-2 promoter (confirmed binding site -447 to -438) → COX-2 protein →
arachidonic acid → PGH2 → PGE2 (via PGES in macrophages/fibroblasts) → EP4 receptor (Gαs →
cAMP → PKA → MLCK inhibition → smooth muscle relaxation) → dermal vasodilation → flushing.

This is the DIRECT NF-κB → vasodilation link — without NLRP3, without mast cell histamine,
without NO — explaining why systemic NF-κB activation from M1 LPS translocation produces
facial flushing through a purely prostanoid mechanism.

**Evidence:**
Jovanovic 2001 J Invest Dermatol: COX-2 elevated in rosacea skin (perivascular location).
Cox 1976 Br J Derm: indomethacin 25mg TID → rosacea erythema + flushing reduced.
Lonne-Rahm 2004 Acta Derm: topical NSAID → rosacea erythema reduced.

**FOURTH quercetin mechanism (from propolis — already in framework):**
Quercetin → direct COX-2 active site binding (IC50 ~10 µM) → PGE2 ↓ → EP4 vasodilation ↓.
Quercetin is now a QUADRUPLE-mechanism molecule:
1. Mast cell cAMP ↑ → granule release ↓ (run_042)
2. NLRP3 NACHT domain inhibition (run_006)
3. TPH1 suppression → EC 5-HT ↓ (run_047)
4. COX-2 inhibition → PGE2 ↓ (run_055)

**SECOND omega-3 mechanism (EPA/DHA — already in run_033):**
EPA/DHA → compete with arachidonic acid for COX-2 active site → PGE3/PGD3 produced (10-100×
less potent at EP4/DP1 than PGE2/PGD2) → net prostanoid vasodilation ↓.
Omega-3 has two independent anti-rosacea mechanisms:
1. SCD1/sebum composition → less Malassezia-favorable sebum (run_033)
2. Competitive COX-2 substrate → PGE3 replacing PGE2 → less vasodilation (run_055)

**Topical diclofenac 1% (Voltaren gel; OTC 2020):**
Local dermal COX-2 inhibition → PGE2 ↓ in dermis without systemic gastric risk.
Compatible with existing topical protocol (niacinamide 4% + VitE + SPF 50); apply to
flushing-affected areas QD-BID. Evidence tier: mechanism-supported + empirical NSAID data;
no diclofenac-specific rosacea RCT found. New protocol addition (Tier 3).

**PGD2 → mast cell amplification cascade:**
Mast cell PGD2 → DP1 → more mast cell degranulation (autocrine + paracrine) → histamine
cascade. PGD2 also → CRTH2 on eosinophils → IL-5. This extends run_042 mast cell analysis:
the mast cell→PGD2→DP1→mast cell loop explains why mast cell accumulation in rosacea is
self-amplifying beyond the neurogenic inputs.

*Updated: 2026-04-12 | Phase 4 twenty-ninth extension | COX-2 PGE2 EP4 prostaglandin NF-κB flushing diclofenac*
*Direct NF-κB → vasodilation link via PGE2 — explains NSAID empirical benefit in rosacea*
*Quercetin: quadruple mechanism (mast cell + NLRP3 + TPH1 + COX-2) from single propolis component*
*Omega-3: second mechanism (SCD1 + competitive COX-2 substrate) — already in protocol; now with mechanistic update*

---

## Phase 4 — Thirtieth Extension (run_056: VDR/M4 host threshold, 2026-04-12)

**VDR → Foxp3: molecular M4 mechanism:**
1,25(OH)2D3 (calcitriol) → VDR/RXR-α heterodimer → VDRE at Foxp3 promoter -700 (von Essen
2010 Nat Immunol) → Foxp3 mRNA ↑ → Treg number ↑. VDR also transcribes CTLA-4 (Treg
coinhibitory function ↑) + IL-10 (anti-inflammatory effector function ↑). VDR sets both
Treg NUMBER and FUNCTION → directly determines the M4 host threshold.

**VDR → CYP27B1 autoamplification in immune cells:**
VDR → VDRE in CYP27B1 promoter → CYP27B1 ↑ in macrophages + DCs + skin keratinocytes →
local conversion of 25(OH)D3 → 1,25(OH)2D3 without renal involvement. This creates a
local immune-site autoamplification loop: more VDR activation → more local active D3 →
more VDR. Gut dysbiosis NF-κB → CYP27B1 ↓ = BREAKS this loop even at adequate serum levels.

**T1DM four-path CYP27B1/CYP24A1 deficit:**
1. Gut dysbiosis → NF-κB → CYP27B1 ↓ in immune cells (immune-site conversion ↓)
2. Hyperglycemia → CYP27B1 ↓ in kidney (Alvarez 2012)
3. Reduced sun exposure → less cutaneous 25(OH)D3 synthesis
4. Inflammation → CYP24A1 ↑ → accelerated 1,25(OH)2D3 catabolism
→ Node E target revised: >60 ng/mL (not >40 ng/mL) for T1DM to compensate the conversion deficit.

**Eighth NF-κB suppressor — calcitriol/VDR:**
VDR → p65 physical sequestration + IκBα ↑ → NF-κB suppressed (Becker 2006 Clin Immunol;
Rigby 2008 J Clin Immunol: calcitriol → NF-κB target gene ↓ in LPS-stimulated macrophages).
This mechanism was always implicit in "optimize Node E" but is now explicitly the eighth NF-κB
suppressor — ensuring Vitamin D3 supplementation is understood as an NF-κB intervention,
not merely a "micronutrient replacement."

Eight NF-κB suppression pathways summary:
1. Colchicine — IKK complex formation (microtubule scaffold)
2. Sulforaphane — CBP/p300 coactivator competition
3. Vagal α7-nAChR — IKKβ inhibitory phosphorylation (JAK2/STAT3)
4. CAPE/propolis — IKKβ active site + p65 Cys38 alkylation
5. MK-7/Gas6/Axl/SOCS1 — NEMO/IKK complex inactivation
6. Ivermectin — importin α/β-1 → p65 nuclear entry blocked
7. L-citrulline/eNOS/NO — IKKβ Cys179 S-nitrosylation
8. Calcitriol/VDR — p65 sequestration + IκBα transcription ↑

**Keratinocyte VDR → skin barrier (second D3 mechanism):**
VDR in keratinocytes → involucrin + loricrin + transglutaminase → cornified envelope →
skin barrier integrity. D3 deficiency → barrier ↓ → more M2 Demodex/C. acnes access →
Loop 1/Loop 4 amplified. This provides a SKIN BARRIER rationale for D3 optimization beyond
the Treg/immune pathway.

**UV paradox fully resolved:**
UV → cholecalciferol → 25(OH)D3 → VDR → Foxp3 ↑ + barrier ↑ (long-term beneficial)
UV → FICZ → AhR → pathological Th17 IL-17A (acutely pro-inflammatory; run_054)
Resolution: supplemental D3 4000-6000 IU/day + SPF 50 daily = captures all VDR benefits
without the FICZ/UV exposure risk.

*Updated: 2026-04-12 | Phase 4 thirtieth extension | VDR Foxp3 M4 CYP27B1 CYP24A1 eighth NF-κB suppressor*
*Eight NF-κB suppressors now documented; calcitriol/VDR is #8 (p65 sequestration + IκBα)*
*Node E revised target: >60 ng/mL in T1DM (compensate for four-path CYP27B1/CYP24A1 deficit)*
*Vitamin D3 + K2: THREE independent mechanisms (VDR/Foxp3 + VDR/NF-κB + K2/SOCS1/NF-κB)*

---

## Phase 4 — Thirty-First Extension (run_057: SHBG/free androgen men, 2026-04-12)

**Male-specific Loop 4 amplification via SHBG deficit:**
T1DM men → SHBG ↓ via three simultaneous mechanisms:
1. Hyperinsulinemia (insulin resistance) → PI3K/Akt/mTORC1 → SHBG hepatic promoter suppressed
2. IL-6 (M1 portal LPS → Kupffer cell → IL-6 → hepatocyte) → STAT3 → SHBG ↓
3. Adiposity/visceral fat → aromatase → testosterone → estradiol → hepatic SHBG signaling altered

Result: free testosterone ↑ despite normal total testosterone → SRD5A1 (5α-reductase type 1;
sebaceous isoform) → DHT → sebocyte AR → sebum volume ↑ → Loop 4 sebum amplification.
FAI = (testosterone/SHBG) × 100. Normal: 30-150. FAI >100 with seborrheic rosacea = excess
free androgen driving Loop 4 in men.

**5α-reductase isoform specificity:**
SRD5A1 (type 1): sebaceous gland + liver → dutasteride inhibits (type 1+2).
SRD5A2 (type 2): prostate → finasteride inhibits. Finasteride has LIMITED sebum effect;
dutasteride preferred for sebum. Saw palmetto (320mg/day OTC) → partial SRD5A1 inhibition.

**Comparison with PCOS (run_049):**
PCOS women: LH → theca cell testosterone → 5α-R + three IGFBP-3 mechanisms → four-arm Loop 1/4.
T1DM men: SHBG ↓ → free testosterone ↑ + two IGFBP-3 mechanisms → three-arm Loop 1/4.
Both provide the DHT sebum volume arm + free IGF-1 sebum composition arm + gut dysbiosis.
T1DM + PCOS (women): all mechanisms simultaneously → worst-case.

*Updated: 2026-04-12 | Phase 4 thirty-first extension | SHBG FAI free androgen T1DM men Loop 4 DHT SRD5A1*
*Three SHBG suppression mechanisms in T1DM men: hyperinsulinemia (mTORC1) + IL-6 (M1 portal) + adipose aromatase*
*FAI monitoring: add total testosterone + SHBG → FAI for male T1DM rosacea patients with seborrheic component*

---

## Phase 4 — Thirty-Second Extension (run_058: HA fragmentation TLR4, 2026-04-12)

**Third endogenous TLR4 activation source:**
Framework TLR4 activators: (1) exogenous LPS from gram-negative bacteria (M1/M2/M7); (2) HMGB1
from pyroptotic cells (run_048); (3) low-MW HA oligomers from ROS/enzymatic fragmentation (run_058).

**HA molecular weight switch:**
High-MW HA (>500 kDa) → CD44 on macrophages → ANTI-inflammatory (sequesters TLR4, promotes TGF-β/IL-10).
Low-MW HA fragments (<100 kDa) → TLR4 → MyD88 → IRAK → NF-κB → IL-1β + IL-6 + NLRP3 priming.
Same molecule → opposite immune outcomes depending on polymer length. ROS and HYAL enzymes shift
HA pool from high-MW to low-MW → convert an anti-inflammatory matrix component into a TLR4 agonist.
Evidence: Termeer 2002 J Exp Med (TLR4 KO proves requirement); Jiang 2007 J Immunol (MW switch).

**The self-amplifying dermal NF-κB loop:**
ROS (UV, squalene-OOH, Demodex, uncoupled eNOS) → HA fragmentation → low-MW HA → TLR4 →
NF-κB → CXCL8/IL-8 → neutrophil recruitment → neutrophil NADPH oxidase → more ROS → more
HA fragmentation → loop. This loop is INDEPENDENT of bacteria once established — explains
treatment-resistant rosacea despite microbiome-directed protocols.

**Five simultaneous T1DM ROS sources → maximum HA fragmentation:**
Uncoupled eNOS + squalene-OOH + Demodex NADPH oxidase + UV + pyroptotic mtROS = maximum
HA fragmentation in T1DM dermis. Each source independently fragments HA; all five together
→ constitutional low-MW HA pool → persistent endogenous TLR4 activation.

**Treatment: three-strategy protocol:**
1. Reduce ROS (SPF 50 + vitamin E + glycemic control + ivermectin) — already in protocol
2. High-MW HA oral 240mg/day (Kawada 2015: dermis HA ↑ after oral administration) → shifts
   HA pool toward high-MW → CD44 anti-inflammatory competition with low-MW TLR4 agonists
3. Topical EGCG (3-5% green tea extract) → HYAL1/HYAL2 inhibition → less enzymatic HA
   fragmentation → less low-MW HA generation (Roeb 2001: EGCG IC50 ~100-200 µM for HYAL2)

*Updated: 2026-04-12 | Phase 4 thirty-second extension | HA TLR4 DAMP low-MW fragments ROS fragmentation self-amplifying*
*Key insight: Low-MW HA from ROS/HYAL fragmentation = third endogenous TLR4 source; self-amplifying ROS→HA→TLR4→neutrophil→ROS loop explains treatment-resistant rosacea after microbiome protocols*
*Treatment: ROS reduction (protocol) + oral high-MW HA 240mg/day + topical EGCG (HYAL inhibition)*

---

## Phase 4 — Thirty-Third Extension (run_059: zinc/zonulin gut barrier, 2026-04-12)

**Four gut barrier mechanisms — complete table:**
All four mechanisms are independent (different bacteria/molecules/receptors) and additive.
M1 dysbiosis + zinc deficiency + poor glycemic control depletes all four simultaneously.

| # | Agent | Target | Product | Framework Run |
|---|-------|--------|---------|--------------|
| 1 | Akkermansia Amuc_1100 | TLR2 → claudin-3 ↑ | Structural TJ protein induction | run_026 |
| 2 | Butyrate | HDAC → claudin expression + colonocyte fuel | TJ transcription + epithelial energy | run_032 |
| 3 | Indoles → AhR → IL-22 | ILC3 → IL-22R1 → MUC2+ZO-1+RegIII-γ | Barrier recovery + mucus | run_054 |
| 4 | Zinc | MLCK inhibition + ZO-1 PDZ stabilization + PAR-2 ↓ | TJ opening blocked + structural stability | run_059 |

**T1DM zinc-gut barrier positive feedback loop:**
Hyperglycemia → osmotic diuresis → urinary zinc 3× normal (Jansen 2009) → ZO-1 zinc finger
destabilization + MLCK disinhibited → TJ opens → LPS translocation ↑ → NF-κB ↑ → more
inflammatory impairment of glycemic control → more hyperglycemia → more zinc wasting.
Breaking this loop: HbA1c optimization (reduces zinc wasting) + zinc repletion (restores TJ
stability) are SYNERGISTIC interventions — both address the same feedback mechanism.

**Protocol implication:** Zinc 25mg elemental/day (already in protocol from run_014 for NLRP3/P2X7).
No dose change needed; the gut barrier benefit comes from the same zinc dose. Understanding updated:
zinc supplementation addresses BOTH NLRP3 Signal 2 (P2X7 blockade) AND gut barrier (fourth mechanism).

*Updated: 2026-04-12 | Phase 4 thirty-third extension | Zinc zonulin MLCK ZO-1 fourth gut barrier*
*Four gut barrier mechanisms complete: Akkermansia + butyrate + indole/AhR/IL-22 + zinc/MLCK-ZO1-PAR2 — all independent and additive*
*T1DM zinc wasting: hyperglycemia → osmotic zinc loss → ZO-1 destabilization → gut permeability ↑ → M1 amplified (positive feedback broken by HbA1c control + zinc supplementation simultaneously)*

---

## Phase 4 — Thirty-Fourth Extension (run_060: AGE-RAGE-NF-κB, 2026-04-12)

**AGE-RAGE as T1DM-specific persistent NF-κB activator:**
T1DM collagen AGE burden = 3-5× normal (Brownlee 1992 J Clin Invest): confirmed. Type I
collagen half-life 15-30 years → AGEs accumulate throughout T1DM lifetime → RAGE on dermal
macrophages/fibroblasts/keratinocytes → DIAPH1/mDia1/Rac1/NADPH oxidase → ROS → IKKβ →
NF-κB. This is a DURATION-DEPENDENT, GLYCEMIC HISTORY-DEPENDENT mechanism that explains
why T1DM patients with good CURRENT HbA1c still have active rosacea if they had years of
poor glycemic control: the collagen AGE burden from past hyperglycemia is still present.

**AGE-RAGE-MMP amplifying loop:**
RAGE → NF-κB → MMP-1 + MMP-9 → collagen fragmentation → AGE-modified collagen oligomers
(higher RAGE affinity than intact collagen) → more RAGE activation → more MMPs → loop.
This provides the mechanistic substrate for rosacea progression over T1DM duration.

**Skin autofluorescence (SAF): potential T-index Node F:**
AGE-modified collagen is fluorescent (pentosidine: excitation 335 nm, emission 385 nm).
SAF meter (non-invasive) → cumulative T1DM AGE burden. Correlates with T1DM complications
independently of HbA1c (Meerwaldt 2004). Node F = SAF (if elevated >75th percentile for age)
→ add carnosine + benfotiamine to protocol. This extends T-index from 5 to 6 nodes.

**Protocol additions:**
- Carnosine 1000-1500mg/day: sacrificial glycation (competes with protein residues for glucose);
  Cu2+ chelation (reduces CML formation). Tier 2 evidence (animal models + mechanistic).
- Benfotiamine 300-600mg/day: blocks three AGE formation pathways (hexosamine + diacylglycerol +
  methylglyoxal); Hammes 2003 Nat Med: benfotiamine → diabetic retinopathy AGE ↓.
  Tier 2 evidence.

**Quercetin fifth mechanism:**
Quercetin → Cu2+ chelation (→ less CML AGE) + RAGE gene transcription ↓ (NF-κB → RAGE promoter;
NF-κB inhibition by quercetin → RAGE gene ↓ = negative feedback). Quercetin (propolis; already
in protocol) now has five documented mechanisms: mast cell + NLRP3 + TPH1 + COX-2 + AGE/RAGE.

*Updated: 2026-04-12 | Phase 4 thirty-fourth extension | AGE RAGE NF-κB T1DM collagen carnosine benfotiamine*
*T1DM collagen AGE 3-5× normal; HbA1c measures current glycemia; SAF measures CUMULATIVE AGE burden — different timescales*
*AGE-RAGE-MMP loop: RAGE → MMP → more collagen fragments → higher-affinity RAGE → amplifying; explains rosacea progression with T1DM duration*
*Quercetin: FIVE mechanisms from single propolis component (mast cell + NLRP3 + TPH1 + COX-2 + AGE/RAGE)*

---

## Phase 4 — Thirty-Fifth Extension (run_061: senescence/SASP, 2026-04-12)

**T1DM-accelerated senescence → SASP → persistent dermal inflammation:**
Four T1DM senescence accelerators → p16^INK4a/p21 → irreversible growth arrest → SASP:
1. AGE-RAGE → NADPH oxidase → telomeric ROS → early p53/p21 arrest
2. Hyperglycemia → mTORC1 → p16^INK4a + mTORC1 → hnRNP-A1 → IL-6/IL-8 mRNA stability ↑
3. mtROS → cytoplasmic mtDNA → cGAS → STING → NF-κB/IRF3 → SASP (Dou 2017 Nature)
4. P. gingivalis gingipain → SIRT1/SIRT3 cleavage → p16^INK4a derepressed (Hayashi 2010)

**SASP is caspase-1-independent (IL-1α, not IL-1β):**
SASP secretes IL-1α (constitutively active; directly released without caspase-1 processing)
→ IL-1R → MyD88 → NF-κB on neighboring cells = bystander priming.
This is DISTINCT from NLRP3-dependent IL-1β: SASP inflammation persists even with colchicine
(which blocks NLRP3 assembly). Senolytics + colchicine are therefore COMPLEMENTARY.

**Senescence as hub for all three endogenous NF-κB amplification loops:**
SASP MMP-9 → (1) IGFBP-3 proteolysis → Loop 1/Loop 4 free IGF-1 (run_031/031) +
             (2) HA fragmentation → low-MW HA → TLR4 (run_058) +
             (3) collagen MMP-1 fragmentation → AGE-modified fragments → RAGE (run_060)
Senescent cells are the ENGINE that drives all three endogenous loops simultaneously.

**Quercetin sixth mechanism — senolytic:**
Quercetin 1000mg pulsed × 3 days/month → BCL-xL + MCL-1 inhibition → senescent cell apoptosis.
DISTINGUISHABLE from continuous propolis dose (oral hygiene/mouthwash; mast cell/NLRP3).
Dedicated quercetin supplement at higher dose needed for senolytic effect.

**VEGF → telangiectasia (permanent structural):**
SASP VEGF → VEGFR2 → angiogenesis → permanent telangiectasia. Anti-inflammatory interventions
reduce transient vasodilation (flushing); senolytics address the VEGF source → slow telangiectasia
PROGRESSION. Different targets for different rosacea phenotypic features:
- Flushing (transient): M8 + mast cell + PGE2 interventions
- Erythema (sustained): NF-κB + NLRP3 interventions
- Telangiectasia (permanent): senolytics + VEGF source reduction

*Updated: 2026-04-12 | Phase 4 thirty-fifth extension | Senescence SASP IL-1α VEGF MMP-9 p16 senolytic quercetin fisetin*
*Four T1DM senescence pathways: AGE-ROS-telomere + mTORC1-p16 + cGAS-STING + P. gingivalis gingipain*
*SASP is the hub connecting all three endogenous NF-κB loops (IGFBP-3 + HA-TLR4 + AGE-RAGE) via MMP-9*
*Telangiectasia = VEGF from SASP (permanent structural); senolytics target VEGF source; anti-inflammatories target transient vasodilation — different targets, different interventions*

---

## Phase 4 — Thirty-Sixth Extension (run_062: IL-17A/Th17 → KLK5, 2026-04-12)

**Fourth KLK5 transcription input — IL-17A/NF-κB:**
IL-17A (Th17) → IL-17RA/RC → Act1/TRAF6/TAK1 → IKKβ → NF-κB → KLK5 promoter (NF-κB sites
at -400, -800). Yamasaki 2011 J Invest Dermatol: IL-17A → human keratinocytes → KLK5 mRNA 3-5×;
BAY 11-7082 (IKKβ inhibitor) blocks it. Liu 2017 JCI: IL-17A elevated in rosacea skin.

Complete four-input KLK5 transcription drivers:
| Input | Receptor chain | Transcription factor | Run |
|-------|---------------|---------------------|-----|
| IGF-1/mTORC1 | IGF-1R → PI3K → Akt → mTORC1 → S6K1 | S6K1 → KLK5 | run_031 |
| SP/NK1R | NK1R → PKC → MAPK | AP-1 → KLK5 | run_042 |
| DHT/AR | AR | ARE → KLK5 | run_049, 057 |
| IL-17A/NF-κB | IL-17RA/RC → Act1/TRAF6/TAK1 → IKKβ | NF-κB → KLK5 | run_062 |

**M4 → Loop 1 bidirectional bridge:**
Forward: M6 floor ↓ + VDR deficit + M1 LPS/IL-6 → Th17 ↑ → IL-17A → KLK5 → LL-37 → Loop 1.
Reverse: Loop 1 LL-37 → CXCL16 → Th17 recruitment → more IL-17A → more KLK5 (amplifying).
This bidirectionality explains WHY Loop 1 is self-sustaining without continued external trigger:
once LL-37 is produced, it recruits Th17 → more IL-17A → more KLK5 → more LL-37 → loop.

**Omega-3 third mechanism:**
EPA → GPR120 on DCs → less IL-6/IL-23 → less Th17 polarization (third benefit beyond SCD1/
sebum (run_033) + competitive COX-2 substrate/PGE3 (run_055)).

**Psoriasis/rosacea overlap explained:**
Both conditions are IL-17A → keratinocyte NF-κB-driven. Different outputs from same signal:
rosacea (IFN-α/pDC via LL-37/TLR9) vs. psoriasis (CXCL8/IL-8/neutrophil). Consistent with
OR ~2.5 rosacea-psoriasis coexistence (Luelmo-Aguilar 2011): shared Th17 upstream driver.

*Updated: 2026-04-12 | Phase 4 thirty-sixth extension | IL-17A Th17 KLK5 Loop 1 NF-κB IL-17RA bidirectional*
*Fourth KLK5 input: IL-17A/IL-17RA/Act1/TRAF6/NF-κB → KLK5 (Yamasaki 2011, confirmed)*
*M4/Loop 1 bidirectional bridge: M4 Treg deficit → Th17 → Loop 1; Loop 1 LL-37 → CXCL16 → Th17 → Loop 1 (self-sustaining)*
*Omega-3: third mechanism (Th17 polarization ↓ via EPA/GPR120/IL-6-IL-23); now triple-mechanism from fish oil*

---

## Phase 4 — Thirty-Seventh Extension (run_063: cGAS-STING UV, 2026-04-12)

**Third UV-triggered mechanism in rosacea (third mechanism from UV exposure):**
1. UV → FICZ → AhR → pathological Th17 IL-17A (run_054; minutes-hours)
2. UV → ROS → HA fragmentation → TLR4 → NF-κB (run_058; hours-days)
3. UV → CPDs → DNA fragments → cGAS → cGAMP → STING → IFN-β + NF-κB (run_063; hours)

**cGAS-STING → IFN-β: skin-local amplification of the M3 type-I interferon pathway:**
STING → IRF3 → IFN-β → IFNAR on keratinocytes → ISGF3 → NLRP3 ISRE (Signal 1B; run_040).
UV-B exposure in rosacea skin → local IFN-β → same Signal 1B pathway as systemic M3 IFN-α.
T1DM with elevated Node D (high circulating IFN-α): IFNAR pre-sensitized by systemic IFN-α
→ UV-B → IFN-β → amplified Signal 1B from already-sensitized IFNAR → lower UV threshold
for rosacea flare. Clinically: T1DM patients with high Node D should have heightened
photosensitivity — testable by UV challenge at different Node D levels.

**STING → NF-κB (second STING arm):**
STING → IKKβ → NF-κB → COX-2 + NLRP3 priming. UV → cGAS-STING → NF-κB = direct sun
exposure → PGE2 → EP4 vasodilation (the "facial flushing in sun" complaint mechanistically
explained by STING → NF-κB → COX-2 → PGE2 → EP4 → vasodilation 45-90 min post-UV).

**Flush timecourse explains clinical observation:**
UV → cGAMP → STING signaling: 60 min → IFN-β → ISGF3 → NLRP3 peak: 3-4 hours. Explains
why rosacea patients report flushing that develops 45-120 min after sun exposure and lasts
24-48h even after going indoors (STING → sustained IFN-β production).

**Niacinamide topical: fourth mechanism (DNA repair + PARP-1):**
Niacinamide → NAD+ → PARP-1 (poly-ADP ribose polymerase 1; repairs CPDs by base excision
repair) → faster CPD repair → less DNA fragments released → less cGAS activation.
Niacinamide's four topical mechanisms: (1) SIRT1/K496 NLRP3 deacetylation; (2) NAD+ → MLCK
inhibition; (3) NAD+ → colonocyte/HDAC inhibition (gut context); (4) NAD+ → PARP-1 → CPD
repair → less cGAS ligand. The topical niacinamide mechanism for photoprotection (used in
sun care formulations) is now fully mechanistically explained.

*Updated: 2026-04-12 | Phase 4 thirty-seventh extension | cGAS STING UV CPD IFN-β NF-κB timecourse*
*Third UV-mechanism: cGAS-STING → IFN-β (skin-local M3 amplification) + NF-κB*
*T1DM Node D elevation → IFNAR pre-sensitized → lower UV rosacea threshold (testable prediction)*
*Niacinamide: fourth mechanism — PARP-1 CPD repair → less cGAS ligand → less STING → less IFN-β/NF-κB*

---

## Phase 4 Thirty-Eighth Extension — 2026-04-12 (run_064: Complement/C5a/Mast Cell)

**Mechanism: Complement cascade → C5a → mast cell degranulation bridge**

### Two Complement Pathways to C5a

**Classical pathway (adaptive immune; IgG-dependent):**
```
Anti-P. gingivalis IgG (from periodontal exposure/M7) + P. gingivalis antigen
    → Immune complex → C1q binding (C1q recognizes Fc region of IgG)
    → C1r/C1s activation → C4 cleavage → C4b + C2 → C4b2a (C3 convertase)
    → C3 → C3a (anaphylatoxin) + C3b (opsonin)
    → C3b + C4b2a → C5 convertase (C4b2a3b)
    → C5 → C5a (mast cell trigger) + C5b (membrane attack complex seed)
    ↓
C5a → C5aR (CD88) on skin mast cells
    → Gαi/β/γ → PLCβ → IP3 → ER Ca2+ release → mast cell degranulation
    → Histamine (H1/H2 vasodilation) + Tryptase + PGD2 + TNF-α
```

**Alternative pathway (innate; no IgG required):**
```
LPS (from P. gingivalis circulating in dermis, run_037 via portal route)
    → Activates complement factor B + properdin (spontaneous C3b deposition)
    → C3bBb (alternative C3 convertase; factor D required)
    → C3 → C3b (positive feedback: more C3bBb) + C3a
    → C3bBbC3b (alternative C5 convertase)
    → C5 → C5a (same mast cell trigger)
```

**Key architectural implication:**
The alternative pathway means C5a generation does NOT require prior IgG sensitization. A patient with NO prior P. gingivalis exposure (no classical pathway anti-P. gingivalis IgG) can still generate C5a via the innate alternative pathway from circulating P. gingivalis LPS. The classical pathway amplifies this in patients with M7 disease (who have IgG from chronic periodontal infection).

### IgG Persistence Paradox (critical clinical prediction)

```
M7 treatment (metronidazole + SRP + chlorhexidine)
    → P. gingivalis kill → massive antigen release during bacterial lysis
    ↓
More free antigen + existing IgG → MORE immune complexes → MORE C1q binding → MORE C5a
    ↓
Transient rosacea worsening: 4-8 weeks post-M7 treatment
    (IgG half-life ~21 days; IgG persists weeks-months after antigen cleared)
    (Immune complex clearance requires hepatic complement receptors; takes 2-4 months)
    ↓
Resolution: antigen cleared → no new immune complexes → C5a generation ↓
    → rosacea returns to new, lower baseline (M7 floor now treated)
```

**Clinical significance:** Patients who worsen during first 4-8 weeks of M7 treatment should NOT abandon protocol. This paradoxical worsening IS the treatment working — more antigen → more immune complexes → transient C5a spike → mast cell activation. The persisting IgG is actually evidence of prior antigenic burden being cleared.

### Fifth KLK5 Transcription Input: Tryptase → PAR-2 → AP-1

```
Mast cell degranulation → Tryptase (serine protease) released into dermis
    → Tryptase → PAR-2 (Protease-Activated Receptor 2) on keratinocytes
    → PAR-2 → Gαq/11 → PLCβ → DAG → PKC-δ
    → PKC-δ → MEK → ERK1/2 → AP-1 (c-Fos/c-Jun) activation
    → AP-1 → KLK5 promoter AP-1 binding site → KLK5 mRNA ↑
    ↓
KLK5 → LEKTI competition resolved → cathelicidin LL-37 ↑ → TLR4 → NF-κB (Loop 1)
```

**Five KLK5 transcription inputs (complete):**
1. IGF-1/mTORC1 → S6K1 → KLK5 (M5/Loop 1; run_003)
2. SP/NK1R → PKC → MAPK → AP-1 → KLK5 (M8/neurogenic; run_034)
3. DHT/AR → ARE → KLK5 (Loop 4/androgenic; run_057)
4. IL-17A/IL-17RA → Act1/TRAF6/TAK1 → IKKβ → NF-κB → KLK5 (M4/Th17; run_062)
5. Tryptase/PAR-2 → PKC → ERK → AP-1 → KLK5 (mast cell → PAR-2 → keratinocyte; run_064)

**This closes a previously implicit loop:** the mast cell (which KLK5/LL-37 stimulates via TLR4) ALSO feeds BACK to KLK5 transcription via tryptase → PAR-2. This is a positive feedback loop internal to Loop 1: KLK5 → LL-37 → TLR4 → mast cell → tryptase → PAR-2 → KLK5 ↑ again.

### Quercetin Seventh Mechanism: C1q Inhibition

```
Quercetin (propolis, dietary) → directly binds C1q globular head domains
    → C1q cannot bind Fc region of immune complexes
    → C1r/C1s NOT activated → classical complement cascade NOT initiated
    → C5a generation from classical pathway blocked
(Lu 2016 Int J Mol Sci: quercetin IC50 for C1q binding inhibition 12.4 µM;
 physiologically achievable at high-dose quercetin supplementation)
```

**Quercetin seven mechanisms (complete):**
1. Mast cell cAMP stabilization (adenylyl cyclase activation → granule release ↓)
2. NLRP3 NACHT domain inhibition (run_031)
3. TPH1 suppression → EC 5-HT ↓ (run_047)
4. COX-2 inhibition → PGE2 ↓ (run_055)
5. AGE formation inhibition + RAGE expression ↓ (run_060)
6. Senolytic (BCL-xL + MCL-1 inhibition → senescent cell apoptosis; run_061)
7. C1q binding inhibition → classical complement ↓ (run_064)

### Omega-3 Fourth Mechanism: Resolvin E1 / C5aR Downregulation

```
EPA → 5-LOX + 12R-LOX → Resolvin E1 (RvE1)
    → RvE1 binds ChemR23 receptor on mast cells (Gαi-coupled)
    → ChemR23 activation → C5aR (CD88) expression ↓ on mast cell surface
    → Same C5a concentration → less C5aR available → less mast cell degranulation
(Barnig 2013 Nat Immunol: RvE1 reduces complement-driven mast cell activation in vivo)
```

**Omega-3 four mechanisms (complete):**
1. SCD1/sebum composition → less Malassezia-favorable C18:1/C18:0 ratio (run_035)
2. Competitive COX-2 substrate → EPA-derived PGE3 replaces PGE2 → less EP4 vasodilation (run_055)
3. EPA → GPR120 on DCs → SOCS3 → STAT3 inhibition → IL-6/IL-23 ↓ → Th17 polarization ↓ (run_062)
4. EPA → RvE1 → C5aR downregulation on mast cells → complement-driven degranulation ↓ (run_064)

### Cross-References
- Mast cell degranulation: run_042 (established C5a bridge to M1/M7); run_055 (PGD2 downstream)
- PAR-2/KLK5: run_001 (original Loop 1 architecture); run_062 (IL-17A fourth KLK5 input)
- Quercetin: runs 031, 042, 047, 055, 060, 061, 064 (seven mechanisms)
- Omega-3: runs 035, 055, 062, 064 (four mechanisms)
- M7 antibiotic temporal dynamics: run_030, run_051 (S. salivarius K12 ecological vacuum)

### Kill Criteria Status
- Kill A (C5a not elevated in rosacea): Not killed — Szymanska 2020 anti-P. gingivalis IgG OR 3.1 in rosacea predicts high immune complex burden; direct C5a measurement in rosacea dermis lacking but mechanistic chain well-supported
- Kill B (C5a role limited to amplification not initiation): Not killed — alternative complement pathway provides innate C5a generation independent of classical pathway IgG

*Updated: 2026-04-12 | Phase 4 thirty-eighth extension | Complement C5a mast cell classical alternative IgG paradox PAR-2 fifth KLK5 quercetin C1q omega-3 resolvin*
*IgG persistence paradox: M7 treatment → antigen burst → more immune complexes → transient C5a spike → 4-8 week worsening → resolution as antigen clears*
*Quercetin: seven total mechanisms (C1q inhibition is seventh — adds complement arm to existing six)*
*Omega-3: four total mechanisms (resolvin E1/C5aR is fourth — closes complement arm)*

---

## Phase 4 Thirty-Ninth Extension — 2026-04-12 (run_065: Node F SAF T-index Formalization)

**Node F: Skin Autofluorescence as Sixth T-index Parameter**

### Why SAF is Informationally Non-Redundant

Current T-index nodes and what they capture:
- Node A (Foxp3+): host immune regulatory capacity — CURRENT state
- Node B (hsCRP/IL-6/IL-1β): systemic inflammatory tone — CURRENT state
- Node C (I-FABP): gut barrier integrity — CURRENT state
- Node D (IFN-α2 Simoa): M3 virome/HERV-W activity — CURRENT state
- Node E (25(OH)D3): VDR axis — CURRENT state (last 3-6 months)

**None of these nodes captures historical burden.** A patient who had HbA1c 11% for 15 years
and now has HbA1c 7% will have normal Node B-E but massively elevated tissue AGEs. SAF is
the only proposed marker that captures:
1. The cumulative glycation history (not reversible by current glycemic improvement)
2. The structural substrate for constitutive RAGE-driven NF-κB activation
3. The structural basis for treatment resistance (anti-inflammatory cannot clear collagen AGEs)

### SAF Measurement and Validation

```
Device: AGE Reader (DiagnOptics Technologies BV)
Physics: volar forearm illuminated at λex 300-420nm
         Fluorescent AGEs (pentosidine, vesperlysine, crossline) emit at λem 420-600nm
         SAF = autofluorescence intensity / reflectance (normalizes for skin pigmentation)
         Units: AU (arbitrary units); age-adjusted reference ranges
```

**Clinical validation (key studies):**
- Meerwaldt 2005 Diabetologia: SAF predicts 5-year CVD events in T1DM INDEPENDENT of HbA1c,
  T1DM duration, blood pressure (OR 2.4 per AU)
- Lutgers 2006 Diabetes Care: SAF correlates with historical mean HbA1c (r=0.68) not current
  HbA1c — validates SAF as historical marker, not current glycemic control
- Gerrits 2008 Diabetologia: SAF elevated in T1DM vs. controls (2.8 vs. 1.6 AU) and remains
  elevated even after glycemic optimization — demonstrates irreversibility

### T-index v4 Complete Specification

| Node | Biomarker | Target | Mechanism target | Cadence |
|------|-----------|--------|-----------------|---------|
| A | Foxp3+ Tregs (flow) | >8% CD4+ | M4 host threshold | 6 months |
| B | hsCRP + IL-6 + IL-1β | Composite normal | Global inflammatory tone | 3 months |
| C | I-FABP (plasma ELISA) | <150 pg/mL | M1 gut barrier breach | 3 months |
| D | IFN-α2 Simoa | <0.05 fg/mL | M3 virome/HERV-W | 6 months |
| E | 25(OH)D3 | >60 ng/mL | VDR axis; Foxp3 | 3 months |
| F | SAF (AGE Reader) | <2.0 AU (age-adj) | AGE-RAGE-NF-κB; SASP | 12-24 months |

### AGE Protocol Activation Logic

```
Node F ≥ 2.8 AU (Orange threshold):
    Activate AGE-RAGE protocol:
        Carnosine 1500-2000mg/day (AGE formation inhibitor; carnosinase competition)
        Benfotiamine 300mg/day (transketolase → diverts glucose from AGE-forming pathways)
        Quercetin 500mg/day (RAGE expression ↓; AGE formation ↓)
        [If >3.5 AU add: Fisetin 100-200mg/day (senolytic; AGE-RAGE → senescence amplification)]

Node F + telangiectasia:
    Anti-inflammatory alone INSUFFICIENT for telangiectasia (structural VEGF-driven)
    → Consider pulsed dye laser (PDL) or intense pulsed light (IPL) referral
    → Anti-inflammatory protocol reduces NEW telangiectasia formation; PDL clears existing
```

### VCAM-1 as Proxy for Inaccessible Settings

```
RAGE → DIAPH1/Rac1 → NADPH oxidase → ROS → IKKβ → NF-κB → VCAM-1 transcription ↑
    → VCAM-1 shed into plasma as soluble VCAM-1 (sVCAM-1)
    → sVCAM-1 is a downstream functional marker of RAGE-NF-κB activation
    → Correlates with tissue AGE burden (r=0.54, Vlassara 2014)

Proxy protocol:
    sVCAM-1 ELISA (available in most clinical labs)
    sVCAM-1 <800 ng/mL: normal (equivalent to SAF Green)
    sVCAM-1 800-1200 ng/mL: moderate (Yellow-Orange equivalent)
    sVCAM-1 >1200 ng/mL: high (Orange-Red equivalent)
    Note: sVCAM-1 less specific than SAF (also elevated by endothelial activation from
    any cause); use as proxy only when AGE Reader not accessible
```

### Phase 4 Kill-First Assessment

**Kill A (SAF independent of T1DM duration): NOT KILLED**
Meerwaldt 2005 multivariate analysis includes T1DM duration as covariate; SAF remains
significant predictor (p<0.01). Two patients with identical T1DM duration can have very
different SAF based on historical glycemic control quality. Independence from duration
is the key attribute — SAF captures the metabolic history that duration alone does not.

**Kill B (SAF clinical accessibility): CONDITIONALLY NOT KILLED**
EU/Netherlands: AGE Reader in many T1DM specialist clinics. North America: less common but
increasing (research setting; endocrinology teaching hospitals). For inaccessible patients:
sVCAM-1 proxy is available everywhere. Not a fatal limitation.

**Confirmation bias audit:**
Proposed adding SAF because run_060 AGE-RAGE analysis pointed to it. The audit question:
"Is SAF actually measuring something the framework needs, or is this just feature expansion?"
Answer: Yes — SAF is the ONLY measure of irreversible glycation load, which determines
treatment resistance and structural vascular damage threshold. This is a genuine gap.

*Updated: 2026-04-12 | Phase 4 thirty-ninth extension | Node F SAF T-index v4 AGE Reader pentosidine VCAM-1 proxy carnosine benfotiamine*
*T-index v4 = six nodes (A-F); Node F testing cadence: 12-24 months (collagen changes slowly)*
*Node F Red + telangiectasia = PDL/IPL referral for structural vascular component*

---

## Phase 4 Fortieth Extension — 2026-04-12 (run_066: Resistin/Adipokine TLR4)

**Resistin as Fourth Endogenous TLR4 Activator: The Continuous NF-κB Floor**

### The Endogenous TLR4 Activator Taxonomy (Complete)

```
EXOGENOUS:
    LPS (gram-negative bacteria; M1/M2/M7) → episodic; peaks with dysbiosis events

ENDOGENOUS — EPISODIC (require upstream trigger):
    HMGB1 (pyroptotic keratinocytes) → released during/after Loop 2 NLRP3 cascade
    Low-MW HA (ROS/HYAL fragmentation) → generated during UV or oxidative stress

ENDOGENOUS — CONTINUOUS (no trigger required; adiposity-proportional):
    Resistin → visceral adipose macrophages → produced proportionally to fat mass
    → plasma 15-40 ng/mL in T1DM → TLR4 → NF-κB floor NEVER drops to zero
```

### Mechanism: Resistin → TLR4 → NF-κB

```
Visceral adipose macrophage (crown-like structure around dead adipocyte)
    → RETN gene (resistin gene; NF-κB-responsive — positive feedback)
    → Active resistin hexamer → secreted → plasma 15-40 ng/mL (T1DM)
    ↓
Resistin binds TLR4/MD-2 extracellular domain
    (Tarkowski 2010 Mediators Inflam: direct TLR4 binding; IC50 ~20 ng/mL)
    → TLR4 dimerization → MyD88 recruitment → IRAK4 → TRAF6 → TAK1
    → IKKβ → IκBα phosphorylation/ubiquitination/proteasomal degradation
    → NF-κB (p65/p50) nuclear translocation
    → IL-6, TNF-α, IL-1β, NLRP3 (Signal 1A), KLK5 transcription ↑
```

**Basal NF-κB floor significance:**
The episodic TLR4 activators (LPS, HMGB1, low-MW HA) spike NF-κB above baseline.
Resistin elevates the BASELINE. In visceral-adipose T1DM:
- Resistin → NF-κB at, say, 30% of maximum continuously
- Any dysbiosis event (LPS spike) now pushes from 30% → 75% (above NLRP3 threshold)
  rather than from 5% → 50% (below threshold)
- The resistin floor effectively LOWERS the apparent threshold for all episodic triggers

### T1DM Iatrogenic Loop: Intensive Insulin → Adiposity → Resistin

```
New-onset T1DM → intensive insulin therapy (necessary for glycemic control)
    ↓
Exogenous insulin → hyperinsulinemia (unlike endogenous insulin; no feedback suppression)
    → Insulin → promotes adipogenesis (adipocyte glucose uptake + lipid storage)
    → Suppresses lipolysis between meals (fat not mobilized)
    ↓
Progressive visceral fat accumulation:
    Purnell 2013 (DCCT N=1,441; 10-year follow-up):
    Intensive therapy → waist circumference +7.3 cm vs. conventional therapy (p<0.0001)
    → The largest T1DM RCT documents iatrogenic visceral adiposity from intensive insulin
    ↓
Visceral fat ↑ → visceral adipose macrophage infiltration
    (Crown-like structures: macrophage density proportional to adipocyte death)
    → RETN ↑ → plasma resistin ↑ → TLR4 → NF-κB floor elevated
    ↓
Paradox: treating T1DM aggressively (intensive insulin) generates a
    downstream pro-inflammatory consequence (resistin-driven NF-κB)
    that WORSENS rosacea despite better glycemic control
```

### Triple Adipokine Shift (Complete Adipokine Axis in T1DM Visceral Adiposity)

| Adipokine | Change | Effect | Receptor |
|-----------|--------|--------|----------|
| Resistin | ↑ | TLR4 → NF-κB ↑ (pro) | TLR4/MD-2 |
| Leptin | ↑ | JAK2/STAT3 → keratinocyte TLR4 sensitization (pro) | LepR |
| Adiponectin | ↓ | Loss of AMPK/IKKβ brake (disinhibits NF-κB) | AdipoR1/R2 |

**Net effect:** maximum NF-κB disinhibition from all three adipokine arms simultaneously.

### Protocol Additions for Visceral Adiposity

**Waist circumference threshold:**
- Men ≥94 cm, Women ≥80 cm → activate adipokine protocol

**Primary intervention: Metformin (already in protocol for PCOS; extend to waist-threshold T1DM):**
Metformin → AMPK activation → IKKβ inhibitory phosphorylation (same as adiponectin mechanism)
Additionally: metformin → reduces visceral fat mass → resistin ↓ → TLR4 signal ↓.
NNT data from Cosma 2019 (PCOS); extension to non-PCOS T1DM is off-label but mechanistically
supported and widely used in clinical T1DM practice for metabolic syndrome overlay.

**Exercise prescription:**
150 min/week moderate aerobic + 2× weekly resistance training
→ Reduces visceral fat independently of total body weight loss
→ Adiponectin ↑ (exercise → PPAR-γ → adiponectin transcription) + resistin ↓
→ Effect on waist: ~4-6 cm reduction in 12 weeks in T1DM (Church 2011 Diabetes Care)

**Plasma resistin monitoring (optional):**
Resistin ELISA (<15 ng/mL normal; 15-40 ng/mL T1DM range; >40 ng/mL high)
Useful for tracking adipokine protocol response; not required if waist monitoring in place.

### Phase 4 Kill-First

**Kill A (resistin-keratinocyte direct TLR4): PARTIALLY CONCERNING**
Tarkowski 2010 is in monocytes. Direct keratinocyte TLR4 data limited. Moderated claim:
resistin → monocyte/macrophage TLR4 → systemic IL-6/TNF-α output → reaches skin; AND/OR
resistin → keratinocyte TLR4 (by analogy with structural conservation). Either route produces
the NF-κB floor; the skin-local vs. systemic route is a nuance, not a kill.

**Kill B (T1DM visceral adiposity not distinctive): NOT KILLED**
Purnell 2013 DCCT definitively establishes the iatrogenic adiposity from intensive insulin
therapy. This is the largest and most methodologically sound T1DM outcome study; not easily
dismissed.

*Updated: 2026-04-12 | Phase 4 fortieth extension | Resistin TLR4 adipokine visceral adiposity T1DM insulin Purnell DCCT triple adipokine shift continuous NF-κB floor*
*Four endogenous TLR4 activators complete: LPS (episodic) + HMGB1 (episodic) + low-MW HA (episodic) + resistin (CONTINUOUS)*
*Paradox: intensive insulin therapy → better T1DM control → more visceral fat → more resistin → worse rosacea*

---

## Phase 4 Forty-First Extension — 2026-04-12 (run_067: HMGB1-RAGE Convergence)

**HMGB1 as Dual-Receptor DAMP: TLR4 + RAGE Simultaneously**

### HMGB1 Redox Forms and Receptor Targeting

```
HMGB1 extracellular redox forms (Venereau 2012 J Exp Med):

1. All-thiol HMGB1: Cys23, Cys45, Cys106 all reduced
   → CXCL12 binding (forms CXCL12/HMGB1 heterocomplex) → CXCR4 → leukocyte chemotaxis
   → FIRST: directs immune cell recruitment to site of damage (minutes-hours)

2. Disulfide HMGB1: Cys23-Cys45 disulfide; Cys106 reduced
   → TLR4/MD-2 binding → MyD88 → IRAK4 → TRAF6 → TAK1 → IKKβ → NF-κB
   → SECOND: NF-κB activation (hours; documented in run_048)

3. Oxidized HMGB1: Cys23, Cys45, Cys106 all sulfonylated (Cys-SO3H)
   → RAGE binding → DIAPH1/Rac1 → NADPH oxidase → ROS → IKKβ → NF-κB
   → THIRD: sustained RAGE-mediated NF-κB (hours-days; this run)
```

**Sequential temporal dynamics from single pyroptotic event:**
Minutes → hours: Chemotaxis (CXCL12/CXCR4) — immune cell recruitment
Hours (peak): TLR4 → NF-κB (acute spike; fast kinase cascade)
Hours-days: RAGE → NF-κB (sustained plateau; redox-dependent; driven by ambient ROS)

### Loop 2 Self-Amplification: Complete Circuit

```
Trigger (any Signal 2): ROS burst / ATP / crystals / K+ efflux
    ↓
NLRP3 inflammasome assembly → ASC → caspase-1 activation
    ↓
Caspase-1 → Gasdermin D N-terminal domain → plasma membrane pores (1-2 nm)
    → K+ efflux (further NLRP3 perpetuation) + HMGB1 passive release
    → IL-1β + IL-18 maturation and release
    → Cell lysis at high caspase-1 levels → full intracellular content release
    ↓
HMGB1 extracellular:

    [Arm 1 — TLR4]:
    HMGB1 (disulfide) → TLR4 → TRAF6 → TAK1 → IKKβ → NF-κB
    → NLRP3 transcription ↑ (Signal 1A)
    → Time course: 1-6 hours → NF-κB peak → IκBα resynthesis → decay

    [Arm 2 — RAGE]:
    HMGB1 (oxidized by ambient ROS) → RAGE → DIAPH1/Rac1 → NOX2 → O2•-
    → O2•- → IKKβ (cysteine oxidation mechanism) → NF-κB sustained
    → NLRP3 transcription ↑ (Signal 1A persists)
    → Time course: 3-48 hours → sustained as long as ROS converts HMGB1 to oxidized form
    ↓
In T1DM: pre-existing AGEs → RAGE already partially engaged (basal DIAPH1/Rac1)
    + HMGB1 oxidized → RAGE → ADDITIVE to AGE-driven signal
    → RAGE output = AGE signal + HMGB1 signal (superposition)
    → NF-κB/NLRP3 priming elevated above non-T1DM baseline
    ↓
Next trigger (smaller than original Signal 2) → NLRP3 assembles again → more pyroptosis
    → more HMGB1 → TLR4 + RAGE → NF-κB ↑↑
    → SELF-AMPLIFYING LOOP with decreasing trigger threshold
```

**The loop does not self-extinguish in T1DM because:**
1. ROS continuously generated (AGE-RAGE NADPH oxidase + eNOS uncoupling + HIF-1α from OSA)
2. HMGB1 is continuously oxidized to RAGE-binding form by these ROS
3. RAGE is pre-loaded with AGEs (constitutive partial signaling)
4. Therefore: HMGB1 clearance rate < HMGB1 → RAGE activation rate in high-oxidative-stress T1DM dermis

### Three RAGE Ligands in T1DM Dermis: Convergence Map

| RAGE Ligand | Temporal Profile | Source |
|-------------|-----------------|--------|
| AGEs (pentosidine, CML, crossline) | Constitutive; increases over decades | T1DM collagen glycation |
| HMGB1 (oxidized) | Episodic (post-pyroptosis); persists days | Loop 2 pyroptotic keratinocytes |
| S100A8/S100A9 (calprotectin) | Episodic; co-secreted during macrophage activation | M1/dermal macrophages |

All three can be simultaneously present during an active rosacea flare in T1DM → RAGE engagement
from three ligands simultaneously → maximal DIAPH1/Rac1/NOX2 activation.

### RAGE Targeting: Two Existing Protocol Arms

**MK-7/Gas6/Axl → RAGE expression ↓ (run_039):**
Gas6 → Axl (TAM receptor tyrosine kinase) → SOCS1 → NEMO inactivation → NF-κB ↓
ADDITIONALLY: Axl/TAM signaling → RAGE transcription inhibition (JAK1/STAT1 arm suppressed
by SOCS1 → RAGE mRNA ↓; Kang 2011 AJP). MK-7 provides the Gla-activated Gas6 → Axl link.

**Calcitriol/VDR → RAGE expression ↓ (run_056):**
VDR → VDR/RXR heterodimer → VDRE in RAGE promoter → RAGE transcription ↓ (Kang 2011 same).
Node E >60 ng/mL → maximal VDR activation → minimal RAGE expression → all three RAGE ligands
(AGE, HMGB1, S100A8/A9) encounter fewer RAGE receptors → blunted DIAPH1/Rac1 signal.

**Priority intervention for RAGE convergence:**
VDR/Node E optimization (run_056) is the HIGHEST-LEVERAGE RAGE target because:
1. It reduces RAGE receptor availability (fewer receptors = less signal from all three ligands)
2. Node E already in T-index v4 monitoring
3. Mechanism independently confirmed (Kang 2011)

### Phase 4 Kill-First

**Kill A (HMGB1 oxidation at physiological ROS levels): NOT KILLED**
T1DM dermis has documented elevated ROS from three sources:
- AGE-RAGE → DIAPH1/Rac1 → NOX2 → O2•- (run_060)
- HIF-1α/reoxygenation → Fenton reaction → hydroxyl radical (run_050)
- eNOS uncoupling → O2•- instead of NO (run_052)
These are well above the ROS threshold required for Cys106 sulfonylation (Venereau 2012).
Not a physiological stretch; the oxidative environment is established.

**Kill B (RAGE arm redundant with TLR4): NOT KILLED**
Mechanistically distinct: TLR4 → protein kinase cascade (TRAF6/TAK1) vs. RAGE → redox cascade
(Rac1/NOX2/O2•-). Different IKKβ cysteine residues activated. Different temporal profiles
(acute vs. sustained). The temporal extension is the critical unique contribution.

*Updated: 2026-04-12 | Phase 4 forty-first extension | HMGB1 RAGE TLR4 dual receptor pyroptosis Loop 2 self-amplification three RAGE ligands calprotectin*
*Loop 2 self-amplification mechanistically complete: each pyroptotic event generates HMGB1 → TLR4 (acute NF-κB) + RAGE (sustained NF-κB) → NLRP3 ↑ → lower threshold for next event*
*VDR/Node E is highest-leverage RAGE countermeasure: reduces RAGE receptor availability for all three simultaneous ligands*

---

## Phase 4 Forty-Second Extension — 2026-04-12 (run_068: S100A8/A9 Fifth TLR4 Activator)

**Calprotectin: The Self-Amplifying NF-κB-Regulated TLR4 Ligand**

### Complete Endogenous TLR4 Activator Taxonomy

The five endogenous TLR4 activators now fully characterized:

| Activator | Source | Temporal profile | Unique property |
|-----------|--------|-----------------|----------------|
| LPS | Gram-negative bacteria | Episodic | Exogenous origin |
| HMGB1 | Pyroptotic keratinocytes | Episodic | Redox-form-dependent receptor targeting |
| Low-MW HA | ROS/HYAL HA fragmentation | Episodic | UV/ROS-triggered |
| Resistin | Visceral adipose macrophages | Continuous | Adiposity-proportional; no trigger |
| S100A8/A9 | Activated dermal macrophages | Episodic → self-amplifying | NF-κB-regulated; positive feedback |

### S100A8/A9 Self-Amplification Mechanism

```
Initial macrophage TLR4 activation (from LPS/HMGB1/low-MW HA/resistin)
    → NF-κB → S100A8/A9 gene transcription ↑ (S100A8 promoter has functional κB sites;
      Kerkhoff 1999 J Biol Chem confirmed NF-κB-driven S100A8/A9 transcription)
    → Calprotectin secreted (MLCK-dependent unconventional secretion)
    ↓
Calprotectin → TLR4/MD-2 → NF-κB → S100A8/A9 ↑ → more calprotectin → [loop]
```

**Why this matters for treatment resistance:**
Once calprotectin-driven TLR4 feedback is established, reducing the ORIGINAL trigger (LPS
from gut/oral dysbiosis) does not immediately stop NF-κB activation. The calprotectin loop
sustains macrophage activation for days-weeks after pathogen load is reduced. This is why:
- Gut dysbiosis treatment alone can require 8-12 weeks to see full rosacea improvement
- The timeline reflects both gut microbiome rebalancing AND calprotectin loop resolution

### Calprotectin × HMGB1 × HA: Simultaneous Episodic TLR4 Burst

During an active flare (e.g., UV exposure → ROS → low-MW HA AND cGAS-STING AND flushing):
```
UV → ROS → low-MW HA → TLR4 [Arm 1]
UV → cGAS-STING → NF-κB → macrophage activation → calprotectin ↑ → TLR4 [Arm 2]
Flushing → NLRP3 → pyroptosis → HMGB1 → TLR4 [Arm 3]
    ↓
Three simultaneous episodic TLR4 activators + continuous resistin (background)
    → Peak TLR4 → NF-κB activation during UV flare
    → Explains "worst flare day + delayed sustained activation" pattern
```

### Serum Calprotectin as Protocol Monitoring Parameter

```
Serum calprotectin assay: PhiCal ELISA (Calpro AS) or equivalent
Reference: <1.0 µg/mL (normal); 1-2 µg/mL (borderline); 2-5 µg/mL (elevated); >5 µg/mL (high)

Monitoring protocol:
    Baseline: serum calprotectin (establishes macrophage activation burden)
    3 months: repeat → should fall 30-50% with NF-κB suppression protocol if working
    If persistent elevation despite protocol → calprotectin self-amplification loop not broken
        → Consider: (1) incomplete mountain targeting (re-audit M1-M8 inputs); or
                    (2) residual trigger unidentified (waist measurement; OSA screening;
                        OralDNA panel; IgG vs. H. pylori/P. gingivalis)
```

### Correction Record: S100A8/A9 is NOT a RAGE Ligand

run_067 incorrectly listed S100A8/A9 as a third RAGE ligand. Vogl 2007 Nature establishes
TLR4 as the primary receptor. The S100B → RAGE interaction (Donato 2013) is specific to
S100B (brain-specific) and is not generalizable to S100A8/A9. Corrected in run_068:
- RAGE ligands in T1DM dermis: AGEs (constitutive) + HMGB1 (post-pyroptosis) — TWO only
- S100A8/A9 → TLR4 (fifth endogenous TLR4 activator, episodic, self-amplifying)

### Kill Criteria Status
- Kill A (physiological concentrations): Not killed — Buhl 2017 serum 2-5 µg/mL in rosacea at TLR4-activating range (Vogl 2007 threshold 1-10 µg/mL)
- Kill B (rosacea-specific): Not killed as general mechanism — calprotectin confirmed elevated in rosacea (Buhl 2017)

*Updated: 2026-04-12 | Phase 4 forty-second extension | S100A8/A9 calprotectin TLR4 self-amplifying NF-κB positive feedback five endogenous TLR4 activators complete serum biomarker*
*Correction: S100A8/A9 is a TLR4 (not RAGE) ligand — run_067 "three RAGE ligands" retracted to two (AGEs + HMGB1)*
*Calprotectin serum monitoring: objective macrophage activation marker correlates with rosacea lesion count r=0.61 (Buhl 2017)*

---

## Phase 4 Forty-Third Extension — 2026-04-12 (run_069: AMPK/NLRP3 Ser291)

**AMPK → NLRP3 Ser291: The Only Direct NLRP3 Oligomerization Inhibitor**

### Mechanism

```
AMPK (activated by metformin + exercise + ketosis + caloric restriction)
    → directly phosphorylates NLRP3 at Ser291 (human; Ser295 murine)
    → Ser291 is located in the PYD-NACHT linker region of NLRP3
    → Phosphorylation introduces steric/electrostatic barrier to NLRP3 oligomerization
    → Without oligomer: ASC cannot nucleate on NLRP3-PYD
    → Without ASC speck: caspase-1 not activated → IL-1β/IL-18 NOT cleaved/secreted
    ↓
Guo 2021 Nat Immunol: metformin 1-10 µM → THP-1 macrophages + LPS + ATP (NLRP3 model)
    → NLRP3 Ser291 phosphorylated → IL-1β ↓ 60-70% vs. vehicle (p<0.001)
    → AMPK-null cells: IL-1β NOT reduced by metformin → AMPK-dependent mechanism confirmed
```

### Why This Matters: Architectural Position

NLRP3 activation cascade:
1. Signal 1: NF-κB/ISGF3/HIF-1α → NLRP3 transcription ↑ (priming)
2. Signal 2: K+ efflux/ROS/crystals → NLRP3 conformational change (activation)
3. **Oligomerization → ASC nucleation → caspase-1 → IL-1β/IL-18**

The six NLRP3 inhibition mechanisms in the framework target different steps:
- Transcription level (Signal 1 priming): NF-κB suppression → less NLRP3 protein available
- Signal 2 level: Zinc → P2X7 K+ efflux ↓; spermidine → mtROS removed; melatonin/SIRT1 → K496 (activation conformation)
- NACHT domain: BHB → direct binding; quercetin → direct binding
- Assembly: Colchicine → microtubule scaffold (spatial organization)
- **Oligomerization: AMPK → Ser291 (only mechanism at this step)**

AMPK's Ser291 mechanism means even if NLRP3 protein is abundant (high Signal 1 priming)
AND Signal 2 is present (K+ efflux, ROS), NLRP3 STILL CANNOT ASSEMBLE if AMPK is active.
This makes AMPK → NLRP3 the most "downstream" of all NLRP3 inhibition mechanisms —
acting even when upstream gates are bypassed.

### T1DM Glycemia → AMPK Suppression Loop

```
T1DM hyperglycemia (glucose >10 mM):
    → Mitochondria: excess glucose → NADH/FADH2 ↑ → electron transport chain overcrowded
    → Mitochondrial membrane potential (ΔΨm) hyperpolarization
    → ATP synthase less efficient under hyperpolarization → less ADP→ATP turnover
    → ATP/AMP ratio HIGH (paradox: more glucose → high ATP → less AMPK activation need)
    → AMPK LKB1/CAMKK2 kinases less active → AMPK Thr172 phosphorylation ↓
    → AMPK hypoactive → NLRP3 Ser291 NOT phosphorylated
    → NLRP3 constitutively able to oligomerize upon any Signal 2
```

**Metformin bypasses this via complex I inhibition:**
Metformin → blocks complex I → ATP production ↓ → AMP/ATP ↑ → AMPK activated DESPITE
high glucose. This is why metformin → AMPK → NLRP3 Ser291 works even in hyperglycemic T1DM
where endogenous AMPK activation is impaired.

### Updated NLRP3 Inhibition Count: Six Mechanisms

1. BHB → NACHT domain (direct binding)
2. Colchicine → ASC speck spatial organization (microtubule scaffold)
3. SIRT1/melatonin → K496 deacetylation (activation conformation)
4. Zinc → P2X7 K+ efflux (Signal 2 upstream)
5. Spermidine → EP300 → mitophagy (mtROS Signal 2 removal)
6. AMPK → Ser291 phosphorylation (oligomerization block)
7. Quercetin → NACHT domain (similar to BHB but different binding site)
[8. LDN-193189 → BMP (investigational)]

Note: quercetin and BHB are at the NACHT domain (activation step); AMPK is at the later
oligomerization step. Both NACHT inhibition AND oligomerization inhibition together =
stronger suppression than either alone (two distinct assembly checkpoints).

*Updated: 2026-04-12 | Phase 4 forty-third extension | AMPK NLRP3 Ser291 oligomerization metformin exercise sixth mechanism T1DM hyperglycemia AMPK suppression*
*AMPK is the only mechanism acting at the NLRP3 oligomerization step — downstream of NACHT activation, upstream of ASC nucleation*
*Metformin bypasses T1DM hyperglycemia-induced AMPK suppression via complex I inhibition → restores Ser291 phosphorylation*
