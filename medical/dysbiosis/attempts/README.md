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

## Status

No attempts populated yet. Directory scaffold in place. Next Phase 1 (numerics solo) firing should populate `numerics/` scripts to measure existing dysbiosis correlations from publicly available data (HMP, American Gut, GMrepo, IBDMDB, etc.).
