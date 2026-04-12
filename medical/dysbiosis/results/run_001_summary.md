# Run 001 Summary — Space Mapping Pass
## Numerical Instance | 2026-04-11 | Phase 1

---

## What Was Produced

Three numerical files in `numerics/`:
1. `run_001_kill_matrix.md` — 43 falsifiable predictions across 6 mountains, evidence-scored
2. `run_001_biomarker_landscape.md` — 37 biomarkers across 3 deployment tiers
3. `run_001_mountain_kill_roi.md` — kill ROI scoring 1-10 per mountain, priority ranking, dead ends

---

## High-Signal Outputs (for Theory to review)

### Finding 1: M4 is structurally isolated
Of 43 predictions mapped, M4 has 7 predictions — and 6/7 are UNTESTED. Every other mountain has at least 2-3 validated predictions. M4 (the wall) is the only mountain where the numerical landscape is essentially empty. This is not because M4 isn't important — it's because we have NO TOOLS to measure it directly.

**Implication:** any approach to M4 that depends on direct threshold measurement is blocked. Proxy strategies are the only numerical path.

### Finding 2: Stall cluster predicted around KLK5 / cathelicidin
The mechanistic chain for M4 is:
```
Microbial density → KLK5 activation → LL-37 cleavage → pro-inflammatory fragments → NLRP3 priming → inflammation
```
Every step is lab-proven. The gap is that KLK5 measurement requires biopsy, and NLRP3 priming requires ex vivo PBMC stimulation. Neither is clinical-scale.

If this method is run as coupled instances, predict: theory instance will stall here. The algebraic obstruction is "the threshold variable is hidden inside a cellular state that can't be externally queried."

### Finding 3: EBV-MS evidence is 3/3 causal quality
Bjornevik 2022 is the highest-quality evidence in the entire dysbiosis field — prospective military cohort, 10 million subjects, MS risk 32× after EBV seroconversion, 0 seronegative MS in cohort. This predicts MS should be reclassified as a viral-triggered autoimmune disease. CVB-T1DM is at ~2/3 strength by the same criteria.

**Sky bridge candidate:** if both MS and T1DM are virus-triggered autoimmune diseases, and the user has T1DM, then EBV monitoring + EBV vaccine (Moderna trial) may be relevant cross-condition.

### Finding 4: The dead-end kill list
From the kill matrix: 5 concrete dead ends where further numerics produce zero ROI:
- 16S correlation studies (saturated)
- Kitavan replication (already validated)
- Zonulin as permeability marker (contested)
- Probiotic RCTs for systemic inflammation (effect sizes too small)
- Re-proving Malassezia/Demodex causation (done)

**These should NOT be where numerical effort goes.**

### Finding 5: User's protocol as cross-kill-test
The user's CVB protocol empirically hits M3 (OSBP cholesterol block targeting CVB), M4 (NLRP3 inhibition, NF-κB suppression), and M5 (IF, diet) simultaneously. The observed SKIN improvement (a M2 outcome) from a protocol framed as M3-targeted is:
- Consistent with: integrated model where gut/virome inflammatory priming lowers skin threshold (M4 effect)
- Also consistent with: cross-reactive improvement from reduced systemic inflammation (M1 pathway)
- NOT easily explained by: local skin microbiome change (no topical antifungal in protocol)

This N=1 observation is consistent with the integrated model and specifically inconsistent with skin-dysbiosis-as-independent (i.e., M2 alone cannot explain the cross-site improvement).

---

## Stall Prediction for Coupled Instance

When theory reads this data, predict the stall point will be:

> "To test P4.3 (host intervention improves disease without composition change), we need a controlled comparison between composition-identical hosts at different threshold states. But we have no way to assign hosts to 'threshold states' without an outcome already occurring."

This is circular: you need the threshold assay to study the threshold. The assay doesn't exist because nobody has a threshold assay to validate against. This is the wall expressed numerically.

---

## Next Numerical Targets (Run 002)

1. **M3 deep: CVB detection sensitivity analysis**
   - Stool vs islet tissue: how much signal is lost at each sampling step?
   - What does the TinyHealth FASTQ (when available) provide for CVB 5'UTR?
   - Compare detection protocols: standard shotgun vs virome-enriched vs RT-PCR for 5'UTR

2. **M4 proxy survey: what correlates with threshold state indirectly?**
   - Vitamin D levels (cathelicidin regulation proxy)
   - Blood Treg frequency (CD4+CD25+FOXP3+) in published cohorts — rosacea, seb derm, IBD
   - IL-10 / TGF-β ratio as Treg output proxy
   - Serum butyrate as proxy for Treg induction

3. **Gut-skin axis mechanistic tree**
   - Map all 6 candidate mechanisms from gap.md
   - Which have supporting intervention data?
   - Which can be tested with existing clinical tools?

4. **Kill test design for M4**
   - Design the minimal experiment that would establish whether host threshold is real
   - What cohort? What measurement? What would constitute falsification?

---

## Noise Logged (did not resolve, log for map completeness)

- Zonulin controversy: is there any newer data post-Zhang 2021 that rehabilitates it? (did not check)
- L:M ratio (lactulose:mannitol) — older gut permeability test, should map its sensitivity/specificity
- Microbial metabolite transport (butyrate in blood) — plasma butyrate concentrations published? What are typical ranges?
- Bacteriophage community — any published disease associations? (essentially unmapped)
- Oral microbiome contribution — gap.md doesn't mention it. Missing mountain?

---
*Run 001 complete. Space mapped at coarse resolution. Dense evidence cluster: M2, M5, M6 (all validated). Evidence desert: M4. Priority target for Run 002: M4 proxy search + M3 detection stack.*
