# result_004 — Mechanism Overlap Analysis

**Date:** 2026-04-09
**Track:** Numerical (Odd)
**Tool:** `numerics/mechanism_overlap.py`

## What we ran

Coverage model for mechanism stacking: effective compression under pairwise
overlap coefficient r ∈ [0,1], where r=0 = fully independent, r=1 = identical.
Gap budget under different evidence-quality subsets of mechanisms.

## Results

**Gap (central):** 3.33×10^5 (log₁₀=5.52)
**Multiplicative stack (r=0):** 1.50×10^7 (log₁₀=7.18) — 45× over-explanation

### Overlap required for exact closure

| r (pairwise overlap) | Effective compression | vs gap |
|---------------------|----------------------|--------|
| 0.0 (independent) | 1.50×10^7 | over ×45 |
| 0.3 | 2.02×10^6 | over ×6 |
| 0.57 | 3.33×10^5 | **exact** |
| 0.7 | 1.40×10^5 | under ×2.4 |
| 1.0 (identical) | 1.88×10^4 | under ×18 |

**r=0.57 exactly closes the gap.** The mechanisms need to be ~57% pairwise
correlated in their compression targets for the stacked total to equal the gap.

### Mechanism subsets (r=0, independent)

| Subset | Compression | Residual | Status |
|--------|------------|---------|--------|
| All 6 mechanisms | 10^7.2 | 10^-1.7 | over ×45 |
| Medium-evidence only (3: grounding, curriculum, RLHF) | 10^3.2 | **10^+2.3** | **UNDER ×200** |
| Remove UG, keep 5 | 10^5.2 | 10^+0.3 | barely under ×2 |
| Remove weak evidence, keep 4 (medium only) | 10^3.2 | 10^+2.3 | UNDER ×200 |

## Key finding: UG is load-bearing

The gap budget reveals a critical dependency:

**Without UG (×100 compression)**, removing it leaves 5 mechanisms providing
10^5.2 compression — barely 2× short of the 10^5.52 gap. The gap barely closes
without UG, confirming that UG is not individually required IF all other
mechanisms contribute at their estimated levels.

**Without weak + theoretical evidence (UG, active learning, world knowledge)**,
only 3 medium-evidence mechanisms remain: grounding (×10), curriculum (×5),
RLHF (×30). These provide only 10^3.2 = 1500× compression — **200× short of
the gap.** The gap does NOT close on medium-evidence mechanisms alone.

**Implication:** The sample-complexity gap explanation requires EITHER:
1. UG + all mechanisms (current state: over-explains if independent)
2. All 6 mechanisms with ~57% pairwise overlap (plausible given their targets)
3. Some currently unknown mechanism of ~200× compression to supplement
   the medium-evidence mechanisms alone

The "200× unknown" framing is the key research target: if UG provides less
than ×100 (the weak-evidence mechanisms are as claimed), what is the missing
200× mechanism?

## Theoretical consequence

The over-explanation from result_001 was misleading. It implied "we understand
the gap." This analysis shows: **only if we include UG (theoretical, no direct
evidence) and weak-evidence mechanisms does the stack over-explain.** If we
restrict to what has direct evidence (medium quality), the gap is 200× under-explained.

The "200× unknown" is structurally similar to the residue in attempt_002's
sample complexity analysis: the gap cannot be fully explained by confirmed,
independently-measured mechanisms. Something in the human learning apparatus
provides ~200× more efficiency than the sum of identified mechanisms.

Candidates for the 200× mechanism:
- **Bayesian online learning over structured representations**: children update
  prior distributions over linguistic hypotheses as they hear new utterances.
  Each exposure rules out many hypotheses simultaneously. This could be 100-1000×
  more efficient than the LLM's in-weights learning.
- **Social scaffolding and joint attention**: language is acquired in
  interaction, with adults tracking child understanding and adjusting input.
  This adaptive feedback might provide 10-100× efficiency over passive exposure.
- **Cross-situational word learning**: children solve the word-meaning mapping
  problem by tracking co-occurrences across situations. Each situation
  eliminates many hypotheses. This is efficient Bayesian inference, not passive
  statistical learning.

These are convergent with the "host properties" framing: the 200× mechanism
lives in the host (embodied, social, interactive learner) not in the linguistic
competence itself.

## Updated gap picture

| Component | Log compression | Evidence |
|-----------|----------------|---------|
| Confirmed mechanisms (medium evidence) | 3.2 | direct |
| Gap to close | 5.52 | measured |
| Unexplained after confirmed | 2.3 (×200) | THE gap |
| UG + weak evidence (theoretical) | +4.0 | weak/theoretical |
| If real and independent: over-explains | −1.7 | — |
| If real and 57% overlapping: exact | 0.0 | — |
