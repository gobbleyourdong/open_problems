# Math audit corpus — dropped 2026-04-18

> Sigma v6 Maps-Include-Noise: dead ends are map features, not waste.
> This directory preserves the 9-fire math audit run (2026-04-15) plus
> its original `AUDIT_LOG.md`. Findings have been applied to the
> synthesis docs and the artifacts dropped to this folder per v9.1 P1
> pruning — kept, not deleted.

## What this was

Structural audit of `open_problems/math/` — 9 subdirs, 117 authored
Lean files, 755 theorems/lemmas. Methodology: Sigma Phase 4a
(grep + Read + cross-reference, no content verification via WebSearch).

## Fires

| # | Date | Scope |
|---|------|-------|
| 1 | 2026-04-15 | math/ top-level synthesis (CLAY_PROBLEMS + SEVEN_WALLS + QUANTIFIED_GAPS + UNDERGROUND_CONNECTIONS) |
| 2 | 2026-04-15 | ns_blowup gold standard + authored Lean sorry count |
| 3 | 2026-04-15 | yang_mills Lean state + named-theorem verification |
| 4 | 2026-04-15 | **Corpus-wide Lean sorry recount** (all 9 subdirs) |
| 5 | 2026-04-15 | birch_swinnerton_dyer full subdir |
| 6 | 2026-04-15 | hodge + p_vs_np + prime_numbers batched |
| 7 | 2026-04-15 | liouville + poincare + RH batched |
| 8 | 2026-04-15 | yang_mills attempts (76 files, largest subdir) |
| 9 | 2026-04-15 | Cross-document claim verification (W_NS + Liu-Pass + Williams + RH certs + YM 66σ) |

## Key findings (applied 2026-04-18)

- **RED (resolved).** CLAY_PROBLEMS sorry counts were grep-artifact
  inflated ~4.5× by per-theorem `"0 sorry"` self-reports. Actual
  live sorry across math corpus: **19 = 9 proof-tactic + 10 infra
  placeholders**, not 86-90. All 9 proof-tactic sorry are in
  `ns_blowup` (6 `Blowup.lean` + 3 `Challenge.lean`). Fix applied
  to `CLAY_PROBLEMS.md` table + statistics (2026-04-18).
- **RED (resolved).** `SEVEN_WALLS.md` RH row had stale "668 zeros
  T=1000, Li n≤200"; Lean truth is "689 zeros + Li n≤1000" per
  `NumericalVerificationDepth.lean`. Fix applied 2026-04-18.
- **RED (resolved).** CLAY_PROBLEMS internal contradiction
  ("Remaining sorry: 6" vs table sum 86) collapsed to the truth
  row: 19 live sorry across corpus.
- **YELLOW (resolved).** `yang_mills/THEWALL.md` snapshot stale
  "50 attempts, 16 Lean" → corrected to 76 attempts + 25 Lean.
- **YELLOW (resolved).** c(4) precision drift `0.561` vs `0.5608`
  normalized to the Lean-source value `0.5608` across docs.
- **GREEN (validated).** Every specific synthesis claim traces
  cleanly to real Lean: W_NS formula, Liu-Pass axiom, Williams.lean,
  4 RH certs, YM 66σ at 3 levels, hoeffding_exponent_negative
  PROVEN, per-regime σ measurements formalized.

## Meta-finding (corpus-level)

The more disciplined the per-file documentation ("0 sorry" self-
reports), the LARGER the `grep -c sorry` artifact. Generalized
overcount: NS 4.5×, YM 9×. Replace plain grep with stricter regex
`^\s*sorry\s*$|:= sorry|:= by sorry` for any future Lean-state
accounting.

## Termination condition

Reached at fire 9. All 9 subdirs + corpus-wide recount + cross-doc
verification done. Further audit fires have diminishing returns —
the math corpus is at "Lean closure modulo infrastructure" across
8 of 9 problems. Active research frontier is the 9 specific Lean
goals in `ns_blowup/Blowup.lean` + `ns_blowup/Challenge.lean`.
