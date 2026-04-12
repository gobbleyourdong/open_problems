# Phase 1 → Phase 2 Theory Handoff
## Numerical Instance → Theory Instance | 2026-04-11

> Theory instance: read this cold. No sunk cost from the numerics work below.
> Your job: find what's surprising. Identify implicit kills. Spot patterns.
> The data is here. What do YOU see?

---

## What Numerics Produced (5 runs, 2026-04-11)

### Files in `numerics/`
- `run_001_kill_matrix.md` — 43 falsifiable predictions × 6 mountains, evidence-scored
- `run_001_biomarker_landscape.md` — 37 biomarkers, 3 deployment tiers
- `run_001_mountain_kill_roi.md` — Kill ROI scored M1-M6; dead ends listed
- `run_002_m4_proxy_survey.md` — 8 proxies for host threshold; T-index v1
- `run_002_m3_detection_stack.md` — CVB detection by method; TinyHealth FASTQ assessment
- `run_002_gut_skin_axis_tree.md` — 6 candidate gut-skin mechanisms ranked
- `run_003_t_index_interactions.md` — T-index v2: two convergence nodes; zinc×D critical
- `run_003_mountain7_oral_microbiome.md` — M7: oral dysbiosis, TLR2, P. gingivalis
- `run_003_dao_histamine_kill_test.md` — DAO/histamine kill test: complete protocol, ~$150
- `run_004_m3_ifn_test_design.md` — IFN-α2 Simoa test design; monitoring protocol
- `run_004_fastq_analysis_protocol.md` — Kraken2 + HUMAnN3 pipeline for DGX
- `run_004_phageome_and_gut_permeability.md` — CrAssphage; zonulin invalidated; L:M ratio
- `run_005_scfa_omega3_references.md` — Acetate is primary systemic SCFA; omega-3 dose data
- `run_005_m7_t1dm_th17.md` — Sky bridge: P. gingivalis Th17 + CVB co-conspiracy in T1DM
- `run_005_scfa_omega3_references.md` — Final noise items closed

### Files in `attempts/`
- `TEMPLATE.md` — Standard attempt format
- `attempt_001_m4_threshold_proxy.md` — T-index v2; stalled at measurement problem
- `attempt_002_m3m7_co_conspiracy.md` — Sky bridge candidate (M3+M7 two-hit T1DM)

---

## The Single Most Important Finding

**M4 (host threshold) has 6/7 predictions untested and NO direct measurement tool.** This is not a new claim — the literature says this too. What's new: the T-index v2 shows that the threshold is a PRODUCT of two convergence nodes, not a sum, and that zinc gates vitamin D's effectiveness, which means the most common supplementation approach (D3 supplementation without zinc monitoring) may be partially ineffective even when serum D looks adequate.

The numerical landscape for M4 is almost completely empty — not because we haven't tried, but because the measurement doesn't exist yet. Theory should examine whether there's a mathematical structure to the threshold that makes it MORE or LESS tractable.

---

## What Was Surprising

1. **Zonulin is measuring C3, not gut permeability.** The most commonly ordered "leaky gut" test is measuring complement activation, not permeability. This invalidates years of published data using that assay. (run_004, phageome + permeability file)

2. **Acetate, not butyrate, is the systemic SCFA.** The gut-skin SCFA axis is almost entirely acetate-mediated. Butyrate supplementation is for gut health only — it doesn't reach skin or systemic immune cells at effective concentrations. (run_005, SCFA file)

3. **Mountain 7 (oral) isn't in the existing framework.** P. gingivalis TLR2 activation drives Th17 via a different receptor than the rest of the protocol. The CVB protocol is TLR4/NF-κB-centric. The oral dysbiosis pathway is orthogonal and currently unaddressed.

4. **The M3+M7 co-conspiracy is a novel sky bridge.** CVB (M3) as initiator + P. gingivalis Th17 (M7) as amplifier for T1DM is not in the published literature as an explicit combined mechanism. Each pathway is published separately; the connection hasn't been made.

5. **TinyHealth FASTQ is M1/M4 data, not M3 data.** CVB is undetectable from shotgun stool metagenomics. The most useful reads from the FASTQ are F. prausnitzii and Akkermansia (Node A proxies for the T-index).

---

## Stall Predictions for Theory

When theory works on these, predict stalls at:

**On M4:**
> "To validate the T-index, we need a comparison group of tolerant high-density carriers vs disease-active carriers. But to define those groups, we need an outcome (disease) that has already occurred. So we're always comparing after the fact — we can't identify the 'about to flare' group before they flare."

This is the M4 measurement circularity. The fix would be longitudinal study with regular microbiome + T-index measurements in high-risk subjects before disease onset.

**On M3+M7 sky bridge:**
> "To test this, we need a cohort of T1DM patients with measured IFN-α2, measured IL-17A, and periodontal status. These three measurements have never been done on the same cohort. Finding such a cohort prospectively would take years."

The stall is dataset availability. No existing cohort has all three measurements. A new cohort would need to be enrolled.

**On gut-skin axis (Mechanism 3, GALT education):**
> "GALT T cell education is confirmed in mice. In humans, we infer it from IBD extraintestinal manifestations. But we don't have a direct human study showing that gut T cells educated in a dysbiotic environment specifically traffic to skin with altered reactivity."

The stall is animal-to-human translation. The mechanism exists in animals; clinical data is inferential.

---

## Kill ROI Ordering (for theory's prioritization)

From `run_001_mountain_kill_roi.md`, updated with M7:

```
PRIORITY  MOUNTAIN  KILL ROI  REASONING
    1       M4        10/10   THE WALL. Threshold integrates all mountains.
                              T-index v2 is the best proxy — validate or kill it.
    2       M3×M7     9/10    Sky bridge. Novel. If confirmed, directly actionable
                              (periodontal treatment adds to CVB protocol).
    3       M3         8/10   CVB-T1DM. IFN-α2 Simoa test is the proxy.
    4       M1         7/10   Gut-systemic pathway. L:M ratio is now the test
                              (zonulin killed).
    5       M7 alone   6/10   Oral dysbiosis. Cheap intervention (chlorhexidine).
                              Confirm with P. gingivalis IgG serology.
    6       M5         6/10   Substrate shift. Well validated ecologically.
    7      DAO         5/10   Rosacea flushing specific. Cheapest kill test ($150).
    8       M6         5/10   Early-life. Intervention window closed for adults.
    9       M2         3/10   Already validated. Treatment works.
```

---

## What Theory Should Focus On

**Highest ROI for theory (fresh eyes, no sunk cost):**

1. **Formalize the T-index v2.** Is there a real mathematical structure here? Multiplicative nodes with a genetic floor — can this be expressed as a proper model? Are there published "immune resilience" models in the tolerance literature this could be mapped onto?

2. **Examine the M3+M7 sky bridge.** Is this genuinely not in the literature? The prediction is: T1DM patients with periodontitis have higher Th17 + faster beta cell loss. A theory instance should assess whether this prediction already failed somewhere (selection bias audit) or is genuinely novel.

3. **Find the minimum intervention set.** Given the mountains, what is the SMALLEST set of interventions that addresses the most mountains simultaneously? The CVB protocol already does this empirically. But can theory identify whether there are CHEAPER or MORE TARGETED alternatives to any component?

4. **The oral health gap.** Is chlorhexidine + scaling sufficient, or does P. gingivalis require a more specific intervention? What does the RA periodontology literature say about P. gingivalis eradication protocols? (RA field has been working on this for longer than T1DM field.)

---

## What Numerics Cannot Produce (Hard Limits)

1. Wet lab data: gnotobiotic models, islet biopsies, challenge studies
2. Longitudinal tracking of the user's protocol outcomes (need time to pass)
3. TinyHealth FASTQ analysis (waiting for the sample to be processed)
4. P. gingivalis serology, DAO test, IFN-α2 Simoa — these require the user to order them
5. Cross-domain literature synthesis at depth — theory is better positioned for this than numerics

---

## Phase 1 Completion Assessment

**Completed (runs 001-005):**
- Kill matrix: 43 predictions × 6+1 mountains ✓
- Biomarker landscape: 37 biomarkers, 3 tiers ✓
- Kill ROI scoring ✓
- M4 proxy survey + T-index v2 ✓
- CVB detection stack ✓
- Gut-skin axis tree ✓
- T-index network interactions ✓
- Mountain 7 ✓
- DAO kill test protocol ✓
- IFN-α monitoring protocol ✓
- FASTQ analysis pipeline ✓
- Phageome partial ✓
- Gut permeability landscape (zonulin corrected) ✓
- SCFA plasma reference ranges ✓
- Omega-3 dose-response ✓
- M7×T1DM Th17 sky bridge ✓
- Attempt templates + 2 filed attempts ✓

**Remaining (diminishing returns):**
- SCFA fecal vs plasma distinction (closed in run_005)
- Additional attempt filing (theory should do this)
- Validation studies (require wet lab)

**Phase 1 status: COMPLETE → ready for theory handoff**

---
*This document is the hand-off from the numerical instance to the theory instance.*
*Theory: read `results/run_001_summary.md` through `results/run_005_summary.md` in order, then `attempts/`, then the high-signal items listed above. The map is here — what does it show you?*
