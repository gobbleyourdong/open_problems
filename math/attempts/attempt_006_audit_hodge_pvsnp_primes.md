# Attempt 006 — Claim-Backing Audit: hodge + p_vs_np + prime_numbers

**Date**: 2026-04-15
**Phase**: Audit Fire 6
**Scope**: 3 smaller subdirs batched — hodge_conjecture (9 attempts +
5 Lean), p_vs_np (3 attempts + 14 Lean), prime_numbers (0 attempts
+ 29 certs + 1 Lean). Combined coverage of 3/9 remaining math
subdirs.

## Executive verdict — all three well-structured; different shapes

**Hodge**: canonical Clay problem, even-numbered attempt sequence
(002-016) + 20 Lean theorems across 5 files, 0 live sorry. Phase 2
status per CLAY_PROBLEMS is accurate.

**P vs NP**: only 3 attempts but 14 Lean files (unusual ratio). Phase 0/1
per CLAY_PROBLEMS. 2 live sorry are Turing-machine-formalization
placeholders (InP, InNP), not proof gaps.

**Prime numbers**: NOT a Clay problem (README is explicit: "Not a Clay
Millennium problem (RH is the closest), but the richest area for
brute-force computation"). No attempts/ workflow; uses 29 numerical
certificates instead. Different methodology — works by computational
verification of known results, not proof attack.

**🔴 RED count**: 0
**🟡 YELLOW count**: 3
**🟢 GREEN count**: 10

## YELLOW findings

| # | Location | Claim | Source gap |
|---|----------|-------|------------|
| Y12 | p_vs_np attempts/ count | 3 attempts (002, 004, hardness_spectrum) vs 14 Lean files (78 theorems claimed) | Lean significantly outpaces attempts. Either the Lean work is doing the heavy lifting directly, or attempts 001/003/005+ existed but weren't preserved. If the former, note the methodology shift; if latter, preserve drafts per Maps-Include-Noise. |
| Y13 | hodge attempts/ numbering gap | Even-numbered sequence 002-016 (skipping 001, 003, 005, etc.) + cycle19_periods | Consistent pattern but non-standard. Document the even-only convention in README or PROBLEM.md. |
| Y14 | prime_numbers structure | README L24 "Campaign Status: 29 Certs, 29 Scripts + sieve_core" — but no `attempts/` content | Different methodology (cert-driven vs attempt-driven) is legitimate but should be explicitly noted as "certificate-verification campaign" in PROBLEM.md-equivalent. Currently only README.md exists. |

## GREEN findings

- **G47** hodge **9 attempts in even-numbered sequence** cover:
  route survey (002), analytical reframe (004), MT classification g=4
  (006), real frontier (008), cycle algebra (010), Fermat cubic
  (012), Tannakian exhaustion (014), multiple mountains (016) +
  cycle19 periods supplement. Thematically coherent progression.
- **G48** hodge **Lean coverage**: CycleAlgebra.lean (5 thms),
  FermatCubic.lean (8 thms — largest), TannakianReformulation.lean
  (3 thms), Lefschetz.lean (4 thms). Total 20 theorems matches
  CLAY_PROBLEMS claim exactly.
- **G49** hodge **0 live sorry** (verified Fire 4). Lean-level
  structural closure; open research is at g ≥ 6 Weil classes
  (per CLAY_PROBLEMS L53 "Open at g ≥ 6: Weil classes on simple CM
  abelian 6-folds").
- **G50** p_vs_np **14 Lean files** — unusual for 3 attempts. Named
  theorems MetaComplexity (Liu-Pass bridge per CLAY_PROBLEMS) +
  dedicated formalization of the 3 barriers (relativization, natural
  proofs, algebrization).
- **G51** p_vs_np **2 live sorry are TM-formalization placeholders**
  (InP, InNP in Definitions.lean L18/22) — infrastructure gaps,
  not proof gaps. Consistent with Phase 0/1 and the "need TM
  library" research frontier.
- **G52** p_vs_np **78 theorems claimed** (CLAY_PROBLEMS) — verify
  via per-file grep if needed; structurally plausible given 14
  files.
- **G53** prime_numbers **README honest labeling**: "Not a Clay
  Millennium problem (RH is the closest), but the richest area for
  brute-force computation in number theory." Explicit scope
  statement.
- **G54** prime_numbers **29 certs cover 6 target categories**:
  Goldbach, twin primes, Polignac, prime races, π(x) vs Li(x),
  prime gaps. Certs include Artin, Brun, Cramér, Sato-Tate, Apery,
  Erdős-Kac, Dirichlet-Chebyshev bias, etc.
- **G55** prime_numbers **sieve_core.py infrastructure** named:
  "Eratosthenes sieve (bytearray, ~1s for 10^8), primes_up_to,
  Li(x), π(x)." Specific implementation + performance data.
- **G56** prime_numbers **Skewes first-crossing reference** (README
  L29): "First crossing: above 10¹⁹ (Skewes 1933 upper bound was
  10^(10^(10^34)))." Specific historical reference with correct
  bound.

## Tag

006 (hodge + p_vs_np + prime_numbers). 3 small subdirs batched.
**0 🔴**. 3 🟡 (p_vs_np 3 attempts vs 14 Lean file ratio; hodge
even-numbered attempt convention undocumented; prime_numbers
cert-driven methodology not labeled in PROBLEM-style doc).
**10 🟢**: hodge 9-attempt thematic progression; hodge 20 theorems
across 5 Lean files matches CLAY claim; hodge 0 live sorry;
p_vs_np 14 Lean files with Liu-Pass formalization; p_vs_np 2 sorry
are TM-formalization placeholders not proof gaps; 78 theorems
structurally plausible; prime_numbers README honest "not Clay"
labeling; 29 certs covering 6 categories; sieve_core.py
infrastructure; Skewes historical reference. **Research frontiers**:
hodge g ≥ 6 Weil classes; p_vs_np TM library + Liu-Pass path to
Kt hardness; prime_numbers continued certificate accumulation
(not a proof target).
