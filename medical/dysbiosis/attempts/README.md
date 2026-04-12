# Dysbiosis — Mountain Attempts

Numbered attempts at climbing each Mountain from `../PROBLEM.md`. Follow the sigma convention: one file per attempt, named `attempt_NNN_brief_description.md`.

## Attempt Template

```markdown
# Attempt NNN — Mountain X — Brief Description

## The Mountain
Which mountain from PROBLEM.md. Restate the claim in one sentence.

## The Approach
What specific route up this mountain is being tried.

## The Kill-First Test
What prediction does this approach make that would be falsified by existing data?
Run this first. If it fails, the approach is ruled out.

## Numerical / Evidential Support
What does existing literature show? Link papers, studies, cohort data.
Include BOTH supporting and contradictory evidence.

## Specific Predictions (testable)
If this mountain is correct, X, Y, Z should be observable.
Include at least one prediction that could be CHECKED against existing data.

## Status
- [ ] Approach articulated
- [ ] Kill-first test run
- [ ] Supporting literature catalogued
- [ ] Contradicting literature catalogued  
- [ ] Predictions checked against existing data
- [ ] Verdict: SURVIVED / KILLED / INCONCLUSIVE

## Next Steps
If survived: what specific study/analysis advances the mountain?
If killed: what does the kill imply for the other mountains?
If inconclusive: what additional data would resolve it?
```

## Priority Order (by Kill ROI)

The mountains are ranked by how much constraint a successful kill would place on the other mountains:

1. **Mountain 4** (host-microbe threshold) — if killed (shown that density alone predicts disease), Mountains 1/2/3 become simpler. If confirmed (shown that density alone does NOT predict), threshold measurement becomes the central frontier.

2. **Mountain 5** (modern diet substrate shift) — large existing literature. A sigma attempt here could synthesize Kitavan-type populational data + recent mechanistic studies. Medium kill ROI because diet is already accepted as a contributor; the question is dominance.

3. **Mountain 3** (virome persistence) — technically challenging but high-ROI. If persistent low-titer viruses drive chronic autoimmunity broadly, the implications reach T1DM, MS, CFS, PCOS, and many more. User's CVB protocol implicitly tests this.

4. **Mountain 1** (gut dysbiosis → systemic inflammation via LPS) — well-studied. An attempt here should focus on whether LPS translocation is the mechanism vs a marker.

5. **Mountain 2** (skin dysbiosis → local disease) — narrow scope. Already well-validated for specific conditions (seb derm, rosacea, acne). Kill ROI is lower because direct evidence exists.

6. **Mountain 6** (early-life assembly) — high-impact but hardest to act on (window often closed for adults). Attempts here should focus on pediatric prevention implications for the user's son.

## Cross-Pollination with Existing Directories

Any dysbiosis attempt should check:

- `../t1dm/` for gut dysbiosis + islet-tropic virus overlap
- `../perioral_dermatitis/` for skin dysbiosis + sebaceous overlap (user's son's condition)
- `../eczema/` for atopic dermatitis + Staph overgrowth + barrier dysfunction
- `../psoriasis/` for autoimmune skin + gut-skin axis
- `../me_cfs/` for chronic viral + immune dysregulation
- `../cvb_disease_network.json` for the CVB-mapped disease network

## Status — Updated 2026-04-12 (Post-Phase 4 + M8 Integration)

### Attempts Index

| File | Mountain(s) | Type | Status |
|------|------------|------|--------|
| attempt_001_m4_threshold_proxy.md | M4 | Threshold proxy design | SURVIVED |
| attempt_002_m3m7_co_conspiracy.md | M3+M7 | Initial co-conspiracy (superseded) | REVISED (see 006) |
| attempt_002_theory_audit.md | All | Theory phase audit | COMPLETED |
| attempt_002_car_update.md | M7 | CAR mechanism update | CORRECTION (IK-6) |
| attempt_003_m1_lps_systemic.md | M1 | LPS systemic mechanism | SURVIVED (mechanism revised: GALT > LPS) |
| attempt_004_m3_cvb_t1dm.md | M3 | CVB persistence T1DM | SURVIVED |
| attempt_005_m5_substrate_shift.md | M5 | Diet substrate shift | SURVIVED (Kitavan scope corrected) |
| implicit_kills_analysis.md | All | 6 implicit kills catalogued | COMPLETED |
| attempt_006_m3m7_local_coinfection.md | M3+M7 | **Sky bridge** — local islet co-infection | STRONG CANDIDATE |
| attempt_007_m1m4_galt_threshold.md | M1↔M4 | **Sky bridge** — GALT Th17 → skin Treg | STRONG CANDIDATE |
| attempt_008_rosacea_nonresponder_loop.md | M2+M4 | **Sky bridge** — KLK5/IFN/IL-23 loop | STRONG CANDIDATE |
| attempt_009_m3_m2_ifn_bridge.md | M3↔M2 | **Sky bridge** — CVB → pDC → rosacea | CANDIDATE (HLA partial kill) |
| attempt_010_m6_m4_treg_window.md | M6↔M4 | **Sky bridge** — early-life Treg floor | STRONG CANDIDATE |
| attempt_011_m5_m7_diet_oral_chain.md | M5↔M7 | **Sky bridge** — hyperglycemia → PMN → P.g. | CANDIDATE |
| attempt_012_m7_m1_oral_gut_axis.md | M7→M1 | **Sky bridge** — oral-gut colonization TLR2+TLR4 | CANDIDATE |
| attempt_013_m8_neuroimmune_hpa.md | M8 | **New mountain** — HPA/CRH/neurogenic (amplifier) | STRONG CANDIDATE (amplifier) |
| attempt_014_m5_m6_maternal_treg.md | M5↔M6 | **Sky bridge** — maternal fiber → fetal Treg floor | STRONG CANDIDATE |
| attempt_015_m8_sky_bridges.md | M8→M4/M1/M7 | **Sky bridges** — M8 formal connections (3 bridges) | M8→M1: STRONG; M8→M4/M7: CANDIDATE |
| attempt_016_m1_m8_bidirectional_loop.md | M1→M8 | **Sky bridge** — gut dysbiosis → HPA dysregulation (bottom-up, closes loop) | CANDIDATE (Sudo 2004 GF mouse; human data limited) |

**8 mountains. 12+ sky bridges. M1↔M8 is a closed bidirectional loop. Novel: M6 × M8 interaction — early-life dysbiosis permanently reduces HPA dampening capacity.**

See `../results/phase3_synthesis.md` for the complete mountain connection map and bridge evidence table.
See `../results/protocol_integration.md` for the complete actionable protocol synthesis.
See `../results/resolution_biology.md` for protocol de-escalation criteria and remission definitions.
See `../results/bridge_kill_roi.md` for kill-ROI ordering of bridges (most fragile: PMC7305306).
