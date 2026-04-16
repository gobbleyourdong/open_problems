# Attempt 008 — Claim-Backing Audit: yang_mills attempts (76 files)

**Date**: 2026-04-15
**Phase**: Audit Fire 8
**Scope**: yang_mills attempts/ layer (76 files, 10,457L) + 3 top-
level docs (PROBLEM 113L + gap 142L + THEWALL 315L = 570L). Largest
math subdir by far. Sampled THEWALL + newest attempts (060-065).

## Executive verdict — yang_mills is the most active math campaign

**yang_mills is the primary active math campaign** in the corpus.
76 attempts span 000_sigma_method_transfer → attempt_065_key_
combinatorial_lemma (very recent, dated 2026-04-15). THEWALL.md
matches non-math THEWALL discipline: "What We Proved" table (8 rows)
+ "What We Killed" table (6 dead ends with kill reasons + attempt
references) + one-sentence wall articulation.

**Current research frontier** (per attempts 060-065): the A₄(⟨Tr(P)·
Tr(Q)⟩) counting lemma for strong-coupling GC > 0 closure. attempt_
063 sets up the counting framework; 064/065 execute. This is live
work as of the audit date.

**🔴 RED count**: 0
**🟡 YELLOW count**: 3
**🟢 GREEN count**: 11

## YELLOW findings

| # | Location | Claim | Source gap |
|---|----------|-------|------------|
| Y19 | yang_mills attempts numbering | 000 sigma_method, 001 gap_analysis, attempt_002-065 + pattern_NNN, request_NNN, summary_NNN | Multi-convention naming (attempt / pattern / request / summary) without a documented legend. Create README.md in attempts/ noting the scheme. |
| Y20 | THEWALL.md L3 "50 even-instance proof attempts, 7 research agents, 16 Lean proofs, 7 dead ends formalized, 40+ papers digested, and 9 routes explored" | Specific tally | Verify counts — 50 attempts vs current 76 attempts (outdated?); 16 Lean proofs vs current 23 Lean files (outdated). Update or date the snapshot. |
| Y21 | attempt_063 L2 "Phase: 5 (Executing the outstanding calculation from attempt_062)" | Phase 5 labeling | Sigma method Phase 5 is self-applicability audit, not execution. Verify this is the right phase label, or if it's a yang_mills-local phase numbering. |

## GREEN findings

- **G69** **76 attempts** is the largest research output in the math
  corpus (more than ns_blowup's 19 despite ns_blowup being the Lean-
  focus subdir). yang_mills is the **active theory frontier**.
- **G70** THEWALL.md **"What We Proved" table** (8 rows): Finite
  lattice mass gap (FiniteLatticeGap.lean, Krein-Rutman); plaquette
  positive correlation (SpectralPositivity.lean, Lehmann); center
  decomposition identity (CenterDecomposition.lean, exact algebra);
  (5.15) ⟺ ordering (CenterDecomposition.lean); negative covariance
  → BC comparison (VortexCost.lean); MK coefficients → 0 (MKDecim
  ation.lean, squeeze); strong coupling (Osterwalder-Seiler 1978);
  (5.15) at step n₀ (attempt_028). **Per-result file + method
  citation** — math-standard claim backing.
- **G71** THEWALL.md **"What We Killed" table** (6 rows with kill
  reasons + attempt references): Lee-Yang/Fisher zeros (no gauge
  analog, attempts 007-008); spin foam positivity (6j mixed signs,
  008); Balaban direct (large field exp vs linear, 005); FKG for
  SU(2) (not distributive lattice, 020); convexity interpolation
  (convex ≠ analytic counterexample, 010); Faddeev-Niemi
  topological (circular, 026). **Maps-Include-Noise at the wall
  level** — dead ends preserved with kill reasons.
- **G72** attempt_063 **recent active work** (dated 2026-04-15):
  specific counting framework for A₄(⟨Tr(P)·Tr(Q)⟩) using character
  expansion on surfaces. Detailed combinatorial setup — this is
  the kind of work that closes the strong-coupling GC > 0 gap.
- **G73** THEWALL.md **one-sentence wall**: "No known method
  propagates the vortex free energy F_v > 0 from strong to weak
  coupling" (truncated at my sample; matches CLAY_PROBLEMS YM
  framing about the intermediate β regime).
- **G74** **Attempt theme diversity**: gap_analysis, peter_weyl,
  center_decomposition, interpolation_proof, plaqprod_counting,
  gc_c4_is_positive, key_combinatorial_lemma, two_loop_verified
  (pattern_061), etc. Multi-technique attack.
- **G75** **Matches Fire 3 findings**: 23 Lean files, 2 live sorry
  (Bessel axiom placeholder), all claimed theorems present. The
  attempts layer drives the Lean formalization layer — attempts
  prove lemmas, which get formalized, which feed back into new
  attempts.
- **G76** **Active working notation** (pattern_NNN, request_NNN,
  summary_NNN) matches the RH pattern (Fire 7 Y15). Suggests a
  cross-subdir working convention worth documenting.
- **G77** **Options framework**: CLAY_PROBLEMS L38 "Option 1
  ACTIVATED: HoeffdingCertificate.lean wires GC vol scaling (66σ)"
  — supported by attempt path in yang_mills/attempts/ showing the
  option-selection process. Options aren't declared ex nihilo;
  they're worked out through attempts.
- **G78** **76 attempts averaging 138L each** — substantial per-
  attempt depth. Largest attempt (001_gap_analysis 708L) is the
  foundational analysis; subsequent work averages 100-250L per
  file.
- **G79** **cross-reference to Lean**: attempt_028 referenced in
  THEWALL.md for (5.15) step n₀; attempts 005/007/008/010/020/026
  referenced in kill table. Attempts are load-bearing references,
  not standalone notes.

## Tag

008 (yang_mills attempts). Largest math subdir — 76 attempts / 10,457L
+ 3 top-level docs (570L). Sampled THEWALL + latest attempts
(060-065, dated 2026-04-15). **0 🔴**. 3 🟡 (multi-convention
naming without legend; THEWALL snapshot counts "50 attempts / 16
Lean proofs" stale vs current 76/23; Phase 5 label in attempt_063
needs verification). **11 🟢**: **76 attempts is the largest math
research output** (active theory frontier); THEWALL "What We Proved"
8-row table with per-result file+method citation; THEWALL "What We
Killed" 6-row table with kill reasons + attempt refs (Maps-Include-
Noise); attempt_063 recent active work on A₄(⟨Tr(P)·Tr(Q)⟩) closing
strong-coupling gap; one-sentence wall articulation; attempt theme
diversity (gap analysis, Peter-Weyl, center decomp, interpolation,
plaqprod counting, combinatorial lemmas, two-loop); matches Fire 3
Lean findings; active working notation (pattern/request/summary)
consistent with RH; options framework worked out through attempts
not declared; 76-attempt substantial per-attempt depth (138L avg);
cross-reference to Lean via attempt numbers. **Research frontier**:
A₄(⟨Tr(P)·Tr(Q)⟩) counting lemma (attempts 063-065) → close strong-
coupling GC > 0 → combined with weak-coupling (attempt_056) + Option 1
HoeffdingCertificate → full mass gap. This is the live math research
fire in the corpus. **Math audit approaching termination**: all 9
subdirs now covered (Fires 2-8). Fire 9 can be termination assessment
+ README update preparation.
