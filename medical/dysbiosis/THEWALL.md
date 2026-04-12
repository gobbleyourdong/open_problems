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
