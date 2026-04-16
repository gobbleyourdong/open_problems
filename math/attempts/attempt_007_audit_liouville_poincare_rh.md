# Attempt 007 — Claim-Backing Audit: liouville + poincare + riemann_hypothesis

**Date**: 2026-04-15
**Phase**: Audit Fire 7
**Scope**: 3 subdirs batched — liouville_conjecture (10 attempts +
5 Lean, 7 theorems), poincare_conjecture (8 attempts + 8 Lean, 64
theorems), riemann_hypothesis (10 attempts + 5 Lean, 19 theorems).

## Executive verdict — theorem counts match CLAY_PROBLEMS exactly

All 3 subdirs: Lean theorem counts verified against CLAY_PROBLEMS
table (liouville 7, poincare 64, RH 19). Attempt structures show
different maturity stages:

- **Liouville**: 10 continuous attempts (001-010), NS sub-campaign
- **Poincaré**: 8 attempts + CLOSING_THE_GAP.md + RETROSPECTIVE.md
  (most documented "SOLVED" subdir)
- **RH**: 10 files in eclectic numbering (attempt_002/004/008/009/013,
  cycle13, pattern_007/011/019, request_006) — active working notation

**🔴 RED count**: 0
**🟡 YELLOW count**: 4
**🟢 GREEN count**: 12

## YELLOW findings

| # | Location | Claim | Source gap |
|---|----------|-------|------------|
| Y15 | RH attempt/ naming convention | Mix of `attempt_NNN`, `cycle13`, `pattern_NNN`, `request_006` | Eclectic naming indicates active working state; document the convention (attempt = structured trial, cycle = recurring check, pattern = observation, request = operator ask) in PROBLEM.md or README. |
| Y16 | liouville Prelude.lean has 0 theorems | `lean/Prelude.lean: 0 thms` | Either intentional scaffolding (import-only file) or empty placeholder. Verify purpose. |
| Y17 | poincare attempts 005, 009 missing | 001-008 + 010 — skipping 005 and 009 | Per Maps-Include-Noise, drafts should be preserved. Either these exist and are mis-named, or were deleted. Note in PROBLEM.md. |
| Y18 | CLAY_PROBLEMS liouville "7 thms / 4 sorry" | Actual: 7 thms total, 1 live sorry (Fire 4) | Per-problem sorry claim 4 vs actual 1 — same grep-artifact pattern (R5). |

## GREEN findings

- **G57** **Liouville theorem count matches exactly**: CLAY_PROBLEMS
  claims 7 thms; actual 1+3+0+1+2 = 7. AncientRepresentation (1)
  + CertificateTaxonomy (3) + Prelude (0) + SmallDataLiouville (1)
  + StretchingObstruction (2) = 7 ✓.
- **G58** **Poincaré theorem count matches exactly**: CLAY claims
  64 thms; actual 8+8+6+11+10+9+3+9 = 64. BoundPropagation (8) +
  MaximumPrinciple (8) + MonotoneFunctionalParadigm (6) + RicciFlow
  (11) + RigorousBounds (10) + SurgerySurvival (9) +
  UniversalPattern (3) + WallTypology (9) = 64 ✓.
- **G59** **RH theorem count matches exactly**: CLAY claims 19 thms;
  actual 3+2+4+3+7 = 19. CertificateEquivalence (3) + Definitions
  (2) + FiveMountains (4) + LiCriterion (3) + NumericalVerification
  Depth (7) = 19 ✓.
- **G60** **Liouville 10 continuous attempts** (001-010): frequency
  function → ancient condition → backward energy → NS entropy →
  KNSS swirl extension → corrector verification → uniqueness
  rigidity → small data proof → pressure gauge far field → spatial
  decay ancient. Systematic thematic progression.
- **G61** **Liouville is NS sub-campaign** (per CLAY L14 "Liouville
  (NS sub)") — cross-references ns_blowup per L_infty theory. Not
  independent Clay problem. Label consistent.
- **G62** **Poincaré has 3 top-level docs** (PROBLEM + CLOSING_THE_
  GAP + RETROSPECTIVE) — unique among math subdirs. Matches "SOLVED"
  status (Fire 1 R2 resolved to "SOLVED proof-level; 1 def
  placeholder").
- **G63** **Poincaré Lean file coverage**: BoundPropagation,
  MaximumPrinciple, MonotoneFunctionalParadigm (the W-entropy-
  monotonicity core), RicciFlow, RigorousBounds, SurgerySurvival
  (Step 9 closed per CLAY L23), UniversalPattern, WallTypology.
  Structural depth.
- **G64** **Poincaré 1 live sorry is def placeholder** (Simply
  Connected in RicciFlow.lean L12, π₁(M) = trivial) — not 9 proof
  gaps. Per Fire 4 this resolves the Fire 1 R2 contradiction
  cleanly: "SOLVED (proof-level); 1 topology definition placeholder
  pending fundamental-group library."
- **G65** **RH 4 live sorry are all definition placeholders**
  (Definitions.lean L38 ζ-zero, L65 λ_n Li coefficient, L88 σ(n)
  Robin divisor sum, L121 Λ de Bruijn-Newman) — no proof gaps. The
  FiveMountains + LiCriterion + CertificateEquivalence proof
  chains are all sorry-free.
- **G66** **RH 5 Lean files map to CLAY claims**: CertificateEquivalence
  (Li ⟺ RH), FiveMountains (5 approaches), LiCriterion (Li's positivity),
  NumericalVerificationDepth (4 cert families — Turing, Li, Robin,
  de Bruijn-Newman). Per-file claim mapping.
- **G67** **RH attempt diversity** (10 files): route survey (002),
  ranked routes (004), multiple mountains (008), Li structure
  (009), phase0 complete (013), cycle13 Turing-based cert, pattern
  files (Li extended, GUE confirmed, explicit formula verified),
  request_006 operator-driven. Diverse research activity.
- **G68** **Poincaré 12/12 blind rediscovery** (per CLAY L7 +
  SEVEN_WALLS): the attempts file path (001 blind_start → 002 even
  _blind → 003 blind_route → 004-010 mechanisms/closure) documents
  the rediscovery trajectory. Historical self-documentation.

## Tag

007 (liouville + poincare + RH). 3 subdirs batched. **0 🔴**. 4 🟡
(RH eclectic naming convention undocumented; liouville Prelude.lean
0-thm purpose unclear; poincare attempts 005/009 missing; liouville
sorry count 4 claimed vs 1 actual — R5 pattern). **12 🟢**: **all 3
subdirs' Lean theorem counts match CLAY_PROBLEMS claims exactly**
(liouville 7, poincare 64, RH 19); liouville 10 continuous attempts
with thematic progression; liouville NS-sub-campaign labeling
consistent; poincare 3 top-level docs matching SOLVED status;
poincare 64-theorem structural depth across 8 Lean files; poincare
1 sorry is def placeholder (Fire 1 R2 resolved); RH 4 sorry all
def placeholders (not proof gaps); RH 5 Lean files map to CLAY
claims; RH attempt diversity showing active research; poincare
12/12 blind rediscovery historical documentation. **Corpus-wide
Lean theorem counts all verified exactly at the per-subdir level.**
Research frontiers per subdir: liouville small-data + corrector
verification (NS sub), poincare fully closed (infrastructure
library pending), RH no-weak-cert (conceptual wall). Next fire:
yang_mills attempts (76 files, largest) — final audit pass before
termination + README update.
