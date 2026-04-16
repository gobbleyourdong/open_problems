# Attempt 108 — Audit of t1dm/attempts 064 + 072 + 077 (gap.md-cited anchors)

**Date**: 2026-04-16
**Phase**: Audit (continues AUDIT_LOG.md queue, follows Fire 10 spot-check of 046/051/055 and Fire 58 sample of 080/089/092)
**Scope**: 3 attempts named in gap.md as load-bearing:
attempt_064 (crown_jewel inequality Lean target),
attempt_072 (CVB genome conservation + permanent-crippling corollary),
attempt_077 (non-progressor state vector anti-problem).
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: Fire 10 established post-036 quality step-change; Fire 58
confirmed gradient continues to late-range. This fire samples the
two Lean-target attempts (064, 077) + one sequence-backbone attempt
(072).

## Executive verdict

All 3 attempts structurally sound. attempt_064 and attempt_077 are
math-standard formalizations with explicit "What this proves /
What this doesn't prove" sections, pre-registered falsifications,
and measurable convergence criteria. attempt_072 is the sequence
backbone anchor (previously content-verified by Fire 43).

**🔴 RED count**: 0 (but R37 from Fire 43 confirmed in-file)
**🟡 YELLOW count**: 6
**🟢 GREEN count**: 10

## Key observations

### attempt_064 — crown_jewel inequality formalization

L120-126 shows `sorry -- to be filled in lean/Theorems/InequalityReversal.lean`.
Fire 41 reported the actual `InequalityReversal.lean:42` is complete
with 0 sorry. Both can be true: attempt_064 is the mathematical
formalization at the point it was written; the Lean file was
proved afterward. **Suggests a gap.md cross-link pointing from
attempt_064 to the completed Lean file would close the loop**.

### attempt_072 — CVB genome conservation

Reversion probability derivation L34-42: `(1/4)^14 × μ_effective
≈ 3.7×10⁻⁹ × 3×10⁻⁵ ≈ 10⁻¹³`. **This is the source of R37 flagged
at Fire 43** ("reversion-probability formula 10⁻¹³ dimensionally
muddled"). The concern: (1/4)^14 gives the probability of RANDOM
reconstruction of a specific 14-mer, NOT the probability of
reversion given an existing deletion. The conclusion (TD mutants
cannot revert on practical timescales) is right; the derivation
conflates fixation probability with mutation rate. **R37 stands,
confirmed in-file here.** Fix is inline in attempt_072 rather than
a new fire-level flag.

### attempt_077 — non-progressor anti-problem

Cleanest anti-problem formalization in the non-math corpus:
7-dimensional state vector, per-dimension measurable proxy,
quantified ε-closeness convergence criterion (ε<0.20, 85-92%
predicted), and **4 pre-registered falsifying observations**
(PD-1/Tim-3 elevated at month 12 / FOXP3+ cells don't increase /
MT-ND3 cfRNA unchanged / enteroviral RT-PCR still positive). This
is sigma-method Phase 4 applied at the operator-trajectory level.

## YELLOW findings

| # | Location | Issue |
|---|----------|-------|
| Y313 | attempt_064 L114 | Soltani 2011 GABA mouse-to-human extrapolation — no PMID threaded. |
| Y314 | attempt_064 L34 | "67 years of autoimmunity → Teff exhausted (15% reduction)" — operator-specific number, uncited. |
| Y315 | attempt_064 L120-126 | Lean-target file `lean/Theorems/InequalityReversal.lean` cross-link missing (Fire 41 shows it's proven; attempt_064 leaves a `sorry` placeholder). |
| Y316 | attempt_072 L25 | Gofshteyn 2020 multi-serotype inhibition cited — no PMID. |
| Y317 | attempt_072 L50 | PDB 5B11 for CVB3 2C structure referenced — direct PDB verification missing. |
| Y318 | attempt_077 L77 | "ODD's anti_problem_cross_disease.py at month 12: state vector is 78-88% close" — numerics script output cited but not linked to a specific file. |

## GREEN findings

- **G281** attempt_064 L103-110: Explicit "What This Proves" + "What This Doesn't Prove" section structure — rare in non-math corpus.
- **G282** attempt_064 L93-100: Monte Carlo P(R>D by month 12) and P(B*>0.30 at 3yr) probability table across 4 initial-B bins (2-5%/5-10%/10-20%/>20%) from 2000 virtual patients.
- **G283** attempt_064 L102: "Critical threshold: B_initial > 2%" — specific falsifiable clinical criterion derivable from the math.
- **G284** attempt_072 L23-27: "Concern / Evidence / Mitigation" 3-column table for fluoxetine cross-serotype variation — risk-rated engagement rather than dismissal.
- **G285** attempt_072 L44: "TD mutants are evolutionarily locked in" claim restated as falsifiable ("the reverted WT genome would immediately re-trigger immune clearance").
- **G286** attempt_072 L48-50: Explicit "Remaining gap" naming STRUCTURAL confirmation (not just sequence) as the next required work item.
- **G287** attempt_077 L14-24: 7-dimensional non-progressor state vector table with (Non-progressor value / Active disease / Protocol target) per-row — matches sigma anti-problem Phase 4 pattern.
- **G288** attempt_077 L58-67: Measurable-proxy table (7 state dimensions × what-assay-measures-it) — actionable clinical endpoints.
- **G289** attempt_077 L69-79: Quantified convergence criterion `ε = ||state_patient - state_non_progressor|| < 0.20` with ODD-derived 78-88% computed baseline + 85-92% post-protocol-augmentation prediction.
- **G290** attempt_077 L81-89: Pre-registered falsifying observations — 4 specific measurable signals that would kill the protocol's claim if not seen at month 12.

## Non-audit observations

- **064 and 077 are Lean-formalization-targets**. Both reference specific `.lean` files. Verifying the Lean files' proof state would close 3 Y-flags (Y315 + gap.md-cited claims).
- **Prior content-audit R37 (Fire 43) concern is in attempt_072**, confirmed. The conclusion stands; the derivation should be replaced with a fixation-probability estimate rather than a random-reconstruction estimate.
- **t1dm post-036 quality step-change** continues in these attempts — matches Fire 10 and Fire 58 observations.

## Recommended fixes (ordered)

1. **[P1]** Cross-link attempt_064 to `lean/Theorems/InequalityReversal.lean` with Fire 41 audit-note. Closes Y315.
2. **[P2]** Inline fix to attempt_072 reversion-probability derivation (replace (1/4)^14 reasoning with fixation-probability framing). Closes R37.
3. **[P3]** Thread PMIDs for Soltani 2011 GABA, Gofshteyn 2020 fluoxetine cross-serotype.

## Tag

108 (t1dm/ key anchors 064/072/077). 0 🔴 new (R37 confirmed in-file). 6 🟡 (PMID gaps, Lean cross-link gap, operator-number provenance). 10 🟢 (What-proves/doesn't, Monte Carlo table, critical-B threshold, mitigation table, explicit remaining-gap, measurable-proxy table, quantified ε-closeness, pre-registered falsifications). Confirms post-036 quality step-change holds through the gap.md-cited anchor attempts. Next fire: Lean backbone grep-verification (Y315 closure) or t1dm 047-050/052-054/065-070/081-088 stride sample.

---

*Filed: 2026-04-16 | medical/t1dm/attempts/attempt_108*
*Continues Fire 10 (046/051/055) + Fire 58 (080/089/092) spot-check methodology.*
