# Attempt 001 — M4 Host Threshold Proxy Measurement
## Mountain 4 — Host-Microbe Threshold

---

## Mountain
M4 — Host-microbe threshold (tolerance problem)

## Hypothesis
A composite index of clinically measurable proxies (T-index v2: vitamin D × zinc, F. prausnitzii, Akkermansia, omega-3 index, hsCRP) predicts disease onset in hosts with identical high microbial density (Demodex >100/cm² or Malassezia overgrowth), with the product of Node A (Treg proxy) and Node B (inflammatory tone proxy) predicting better than either node alone.

## Evidence Base (from numerics)
- numerics/run_001_kill_matrix.md, M4 section (6/7 predictions untested)
- numerics/run_002_m4_proxy_survey.md (8 proxies mapped, T-index v1)
- numerics/run_003_t_index_interactions.md (T-index v2, zinc×D critical interaction, two convergence nodes)

## Mechanistic Chain
```
Genetic floor (NOD2/TLR4 SNPs)
     ↓
Node A (Treg induction capacity):
  Vitamin D [gated by zinc] → VDR → FOXP3
  F. prausnitzii → butyrate → HDAC → FOXP3 amplification
  Akkermansia → mucin → barrier → less inflammatory Treg depletion
     × 
Node B (inflammatory tone):
  Omega-3 → resolvin [gated by vitamin D/15-LOX]
  Zinc → NLRP3 regulation
  hsCRP (inverse) → systemic NF-κB baseline
     =
THRESHOLD STATE
     ↓
Same microbial density:
  Low T-index → disease
  High T-index → tolerant carrier (no disease)
```

## Kill Test
**Kill criterion:** T-index v2 does NOT significantly differentiate disease-active from tolerant carriers in hosts with matched high microbial density.

**Data required:** Cross-sectional study: 50 rosacea-active high-Demodex vs 50 tolerant high-Demodex hosts. Measure all T-index components. Compare group means. If no significant difference → T-index v2 is not a valid threshold proxy.

**Status: UNTESTED — validation study not yet run**

## Supporting Predictions
1. Zinc deficiency will impair vitamin D's threshold-raising effects even when 25-OH-D is in the "normal" range
2. F. prausnitzii depletion in TinyHealth FASTQ will correlate with disease activity across the user's multi-site dysbiosis cluster
3. The Node A × Node B multiplicative product will predict disease state better than either node's linear sum (logistic regression comparison)
4. Low T-index patients will have lower Treg % (blood) than high T-index patients matched for disease state

## Evidence FOR: 2/3
Genetic associations (NOD2, TLR4, NLRP3) establish that host threshold is genetically variable. IBD extraintestinal manifestations establish that immune calibration affects remote-site disease. T-index proxies are individually validated in separate disease contexts (vitamin D + T1DM, F. prausnitzii + IBD, etc.).

## Evidence AGAINST: 1/3
No direct human study has validated the composite. The zinc×D interaction is biochemically established but not clinically validated for disease prediction. Threshold state could be tissue-specific (blood Tregs ≠ skin Tregs ≠ gut Tregs).

## Current Status
[x] STALLED — stuck at: measurement problem. No clinical assay for direct threshold state. T-index v2 is the best available proxy but requires a validation study to use confidently.

## Stall Point
The threshold is a CELLULAR STATE (NLRP3 primed vs resting in tissue) that cannot be externally queried without tissue biopsy. All proxies are indirect. The validation study (100 subjects, all T-index components) exists as a design but not as executed research. This is the method's limit — it can identify the gap but not close it without wet lab work.

## Sky Bridge Target
SKY BRIDGE CANDIDATE: M4 (threshold) ↔ M7 (oral P. gingivalis Th17)
P. gingivalis drives Th17 via TLR2→AP-1 pathway. Elevated Th17 reduces Treg:Th17 ratio → lowers threshold. If P. gingivalis oral load is high, it's actively pulling the threshold DOWN independent of the T-index nutritional proxies. This means T-index v2 is incomplete without oral dysbiosis state.

**Extension needed:** Add P. gingivalis seropositivity as Node C (Th17 amplification) to T-index v3.

## Next Action for Theory
1. Formalize: can the T-index be expressed as a proper mathematical model? f(Node_A × Node_B × Genetic_Floor) — what's the functional form?
2. Identify: are there published "dysbiosis resilience" studies that already proxy-test something like T-index without naming it?
3. Sky bridge: does the T1DM literature have any multi-variable threshold models that could be adapted?
4. Propose: what single intervention would MOST predictably raise T-index from low to adequate, and what's the fastest timeline?

---
*Attempt filed: 2026-04-11 | Instance: numerics (Phase 1 deposit for theory)*
