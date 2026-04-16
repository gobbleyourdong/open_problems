# Attempt 005 — Claim-Backing Audit: birch_swinnerton_dyer

**Date**: 2026-04-15
**Phase**: Audit Fire 5
**Scope**: BSD subdir full pass — PROBLEM.md (39L), gap.md (118L),
THEWALL.md (92L), 4 attempts (334L), 2 Lean files, attempt_006
multi-mountain framework.

## Executive verdict — BSD is well-structured but Phase 1

BSD has 0 live sorry, well-documented 5-mountains framework, coherent
wall identification ("Heegner gives ONE point, nobody can give TWO"),
and Lean formalization that correctly axiomatizes the algebraic core
while leaving construction methods external. Attempts numbering is
gapped (002, 006, cycle17, request_004) suggesting some historical
drafts not preserved as map features.

**🔴 RED count**: 0
**🟡 YELLOW count**: 3
**🟢 GREEN count**: 8

## YELLOW findings

| # | Location | Claim | Source gap |
|---|----------|-------|------------|
| Y9 | attempts/ numbering gap | attempt_002, 006, cycle17, request_004 — attempts 001, 003-005 missing | Either the series was non-sequential or drafts were deleted. Per Maps-Include-Noise, rejected drafts should be preserved. If genuinely non-sequential, add a README.md note explaining the numbering scheme. |
| Y10 | final_proof/ directory is empty | `final_proof/` present but 0 files | Directory scaffolded but unused. Remove if premature, or mark as "pending proof" per sigma method directory hygiene. |
| Y11 | Lean uses axioms for all core objects (Point, Point.add, Point.smul, heightPairing) | Structural-framework approach — axiomatizes the ECM interface rather than building from mathlib | Legitimate scaffolding but should document explicitly: this file is a structural skeleton, not a computable formalization. Link to mathlib EllipticCurve once it exists, or note the axiomatic approach in file docstring. |

## GREEN findings

- **G39** THEWALL.md **"In one sentence: No construction produces two
  independent rational points on an elliptic curve from L-function
  data. Gross-Zagier gives one. Nobody can give two."** — exemplary
  single-sentence wall articulation.
- **G40** THEWALL.md **rank / points-needed / available / status
  table** — Phase 0 shape-check at the subdir level with per-rank
  status.
- **G41** attempt_006 **5-mountain framework**: M1 Arithmetic
  geometry (current, stuck at rank 1) + M2 Analytic number theory
  (L-function moments, Keating-Snaith pair conjectures) + M3
  Topology (Mazur number fields ↔ 3-manifolds, Selmer ↔ linking) +
  M4 Physics (string theory, mirror symmetry, CY periods) + M5
  Computation (descent generators). Each mountain with specific
  tools + gap view + underground connections to M1.
- **G42** gap.md **per-rank status breakdown**: rank 0 proved
  (Kolyvagin 1990 + Kato 2004), rank 1 proved (Gross-Zagier 1986 +
  Kolyvagin), rank ≥ 2 "NOTHING is known." Honest state labeling.
- **G43** gap.md **specific theorem attribution**: Kolyvagin 1990
  Euler systems, Kato 2004 alternative, Gross-Zagier 1986 formula
  L'(E,1) = c·ĥ(P_K), Bhargava-Shankar 2010-2015 average rank ≤ 1.5,
  Jetchev-Skinner-Wan 2017 full BSD at all-but-finitely-many primes,
  Bhargava-Skinner-Zhang 2014 66.48% of E/Q satisfy BSD. Major
  literature results cited with year + names.
- **G44** attempt_006 **M2 "higher Gross-Zagier" insight**: "A
  SECOND-moment Gross-Zagier would give L'' = regulator of TWO points.
  This is the 'higher Gross-Zagier' everyone wants." Specific
  research target named, not just "open problem."
- **G45** **RankTwoStructure.lean** structurally sound: `Point` +
  `LinearlyIndependent` + `RankGeTwo` + `Regulator` + `Second
  OrderGrossZagier` + `any_method_gives_rank_two` + `unified_rank_
  two_criterion` + `RankTwoConstructionProblem`. Axiom-based
  scaffolding with clear conceptual chain.
- **G46** **0 live sorry in BSD** (verified Fire 4) — Lean is
  complete at the structural level. Research gap is at the
  construction-method level (outside Lean scope).

## Tag

005 (BSD). **0 🔴**. 3 🟡 (attempts numbering gap 001/003-005
missing; empty final_proof/; Lean axiom-based scaffolding not
documented in file). **8 🟢**: single-sentence wall articulation;
per-rank status table; 5-mountains framework with per-mountain
tools/gap/underground-connections; per-rank status breakdown with
Kolyvagin/Kato/Gross-Zagier/Bhargava attributions; "higher
Gross-Zagier" research target named; RankTwoStructure.lean
structural chain; 0 live sorry. **BSD research frontier**: the
rank-2 construction via higher Gross-Zagier (M2) or topological
Selmer linking (M3) — both concrete directions. BSD is at Lean
structural closure awaiting genius insight at the construction level.
