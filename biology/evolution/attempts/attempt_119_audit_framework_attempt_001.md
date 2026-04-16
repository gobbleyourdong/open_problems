# Attempt 119 — Claim-Backing Audit: biology/evolution attempt_001 (framework + addendum)

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue, Fire 47)
**Scope**: biology/evolution/attempts/attempt_001_persistence_as_strategy.md
(450 lines, full read L1-120 + L120-296 + L296-450). Paired survey of
`biology/evolution/results/` directory confirming the 5 synthesis
files referenced in addendum exist (persistence_mechanisms_taxonomy
411L, host_coevolution 378L, therapeutic_convergence 358L,
modernity_trajectory 347L, class_boundary_cases 360L; total 1854
lines of synthesis ancillary) plus 5 `audit_100series_20260415*.md`
round files (1097 lines, 5 rounds) that cover the prior WebSearch
content audit.
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: Fire 46 recommended "consolidate 3 framework updates
(004/006/009) into attempt_001 or framework-synthesis attempt."

## Executive verdict — CONSOLIDATION ALREADY DONE

**Fire 46's recommendation is already fulfilled.** attempt_001 has a
**"Framework Refinement After Per-Organism Series" addendum** (L288-444,
157 lines) added 2026-04-15 that consolidates:

- Original **4-class framework** → **7-class taxonomy** (addendum
  L297-321) with explicit mapping of each class to per-organism
  attempts (001: herpesviruses latency; 002: CVB mutation; 003: EBV
  encoded latency; 004: HPV lifecycle; 005: HIV/HHV-6 integration;
  006: chronic active H. pylori / P. gingivalis / C. acnes; 007:
  obligate-host Demodex / Malassezia / M. leprae)
- **Prediction #2 REFORMULATED** (L330-336) — old "larger genomes"
  → new "genome SPECIALIZATION (either expansion OR contraction)".
  This is exactly Fire 44's G331 observation propagated into the
  framework doc, with explicit old-vs-new marked.
- **Five additional framework principles A–E** (L347-388): Disease-
  as-incidental near-universal; host-coevolution common hubs (HLA-
  DRB1/TLR2/IL-1β/NLRP3); therapeutic convergence (doxycycline 40mg
  across classes 6-7); modernity shift (H. pylori declining vs
  Demodex/Malassezia/P. gingivalis rising); classes not mutually
  exclusive (T. cruzi = 4+7, T. pallidum = 6+4).

**The framework doc is in exemplary shape.** The addendum is
sigma-method-compliant: preserves original 4-class formulation in
Maps-Include-Noise fashion, explicitly marks reformulations, references
5 detailed synthesis-notes files for per-principle depth, names
6 boundary cases beyond the 10-organism core.

**🔴 RED count**: 0
**🟡 YELLOW count**: 4
**🟢 GREEN count**: 12

## YELLOW findings

| # | Location | Claim | Source gap |
|---|----------|-------|------------|
| Y271 | L417-419 "Audit passes (6 batches, 65 claims, ~52% fully verified, ~48% with corrections)" | Specific numbers | Thread to `results/audit_100series_20260415*.md` (5 round files) + prior `claim_audit_2026-04-15.md` — verify 6-batch count and 52%/48% split |
| Y272 | L429 "audit-loop continuation — the audit loop (30m cron)" | cron interval | **Cron is 10m not 30m per user's /loop spec** — minor version-drift inconsistency; update addendum |
| Y273 | L360-361 "HLA-DRB1, TLR2, IL-1β, NLRP3 are repeatedly named across the persistent-organism set" | Specific cross-organism mapping | Thread each gene to specific per-organism attempts (e.g., TLR2 → attempt_009 Demodex L321; NLRP3 → run_046 cross-reference) |
| Y274 | L288-295 addendum references "6 boundary cases (MTB, M. leprae, T. pallidum, Toxoplasma, T. cruzi, P. vivax)" | Boundary cases | Not yet audited — defer to next fire targeting `class_boundary_cases.md` (360L) |

## GREEN findings

- **G356** attempt_001 **4→7 class taxonomy expansion preserved
  in Maps-Include-Noise fashion**: original 4-class formulation
  L81-146 retained as-is; addendum L297-321 adds 3 new classes with
  explicit "(new)" markers on #3 lifecycle-compartmentalization, #5
  chromosomal-integration-with-germline, #6 chronic-active-
  colonization, #7 obligate-host-dependent-reductive-genome. Old
  framework preserved, new layered on top.
- **G357** addendum **prediction #2 reformulation with explicit old-
  vs-new**: "Original: Larger genomes for persistent viruses. The
  original claim fails for HPV (8 kb) and Demodex (~51 Mb nuclear
  — reductive, not expanded). Corrected claim: persistent organisms
  show genome SPECIALIZATION relative to free-living relatives —
  either expansion or contraction". **Kill-first discipline at
  framework level**: failing prediction kept + reformulated, not
  silently replaced.
- **G358** addendum **5 additional framework principles (A-E)
  with per-principle synthesis-file references**: A disease-as-
  incidental near-universal → no file; B host-coevolution common
  hubs → `results/host_coevolution.md`; C therapeutic convergence
  → `results/therapeutic_convergence.md`; D modernity trajectory
  → `results/modernity_trajectory.md`; E class-boundary hybrids →
  `results/class_boundary_cases.md`. **Each synthesis claim has a
  dedicated file** — claim-to-source traceability at framework level.
- **G359** addendum L390-415 **directory-state tree diagram** showing
  full biology/evolution/ structure after synthesis phase — attempts
  (001-010), results/ (5 files named), papers/numerics/certs/
  (empty, honestly labeled). Self-documenting subdir state.
- **G360** addendum **cross-audit self-reference** (L417-419):
  "Audit passes (6 batches, 65 claims, ~52% fully verified, ~48%
  with corrections) have improved claim reliability across the
  directory." Framework attempt cites its own audit history
  inline — matches the attempt_008 "Dominy 2019 verified in batch
  2 audit" pattern from Fire 46. **Cross-audit integration**
  working at framework level.
- **G361** L204-245 **6 framework predictions made upfront** (before
  per-organism work began) with explicit "should see" language,
  then **per-prediction verdicts added in addendum** (L328-345) with
  ✓ / REFORMULATED / confirmation per prediction. Pre-registered
  predictions → post-hoc evaluation with honest success/failure
  labels. Matches math-standard testability discipline.
- **G362** L154-173 **"Disease is evolutionarily incidental to virus
  fitness"** claim with 4 examples (HPV cervical cancer post-
  transmission; EBV MS decades post-mono; CVB T1DM months-years
  post-acute; HCMV congenital vs salivary) + clinical corollary
  ("reducing chronic-disease burden does not drive virus evolution
  toward lower virulence"). **Operationally useful**: informs
  therapy design, matches the "this virus will not evolve around
  fluoxetine quickly" reasoning in medical/t1dm.
- **G363** L175-202 **host-side coevolution inventory** — HLA
  polymorphism, KIR-HLA, TRIM5α/APOBEC3G/BST-2/SAMHD1/MX1,
  HERVs (8% of human genome), syncytin-1 co-option. 5-layer
  host-side adaptive fingerprint with specific gene names.
- **G364** addendum principle **E "Classes are not mutually
  exclusive"** with specific hybrid examples: T. cruzi class 4 +
  class 7; T. pallidum 6 + 4 + phased; Plasmodium 4 + class-1-
  like hypnozoite. Honest acknowledgment of taxonomy-imperfect-
  fit at framework level.
- **G365** addendum **"What remains open" section** (L423-439) —
  4 specific next-steps: update PROBLEM.md to reflect expanded
  scope, audit-loop continuation, cross-organism therapeutic trial
  synthesis, 8th-class consideration (biofilm was considered AND
  REJECTED). **Kill-ROI at framework level**: explicit what-next
  + explicit what-was-considered-and-rejected.
- **G366** **5 results/ synthesis notes exist at full line-count**
  (persistence_mechanisms_taxonomy 411, host_coevolution 378,
  therapeutic_convergence 358, modernity_trajectory 347, class_
  boundary_cases 360 = **1854 total lines**). The referenced
  synthesis infrastructure is real, not placeholder.
- **G367** **5 `audit_100series_20260415*.md` round files exist**
  (261+202+204+228+202 = 1097 lines) covering the prior
  WebSearch-based content audit in 5 rounds. Per-round audit
  artifact trail preserved in `results/` for future reference.
- **G368** L3-6 **attempt's self-described purpose**: "Cross-
  cutting analysis before per-virus attempts. Establishes what
  'persistence' means as an evolutionary trait and what selection
  conditions produce it. Sets up the comparative framework that
  attempts 002-005 (per-virus) will populate." — sigma-v5
  anti-problem framing at the framework level (persistence as
  evolutionary strategy, not "how do viruses persist" as
  mechanism-list).

## Recommended fixes (ordered)

1. **[P2]** Fix cron-interval version drift — addendum L429 says
   "30m cron" but actual audit loop is 10m. Minor edit.
2. **[P2]** Thread the 5 `audit_100series_20260415*.md` round files
   + prior `claim_audit_2026-04-15.md` explicitly in addendum
   L417-419 audit-pass reference (Y271). Path would be:
   `results/audit_100series_20260415.md` (round 1) through `_round5.md`.
3. **[P3]** Thread per-organism attempt references for HLA-DRB1 /
   TLR2 / IL-1β / NLRP3 "repeatedly named across persistent-organism
   set" claim (Y273) — explicit cross-refs to attempts 002/003/007/
   008/009 or run_046.
4. **[P3]** Audit the 5 synthesis notes (1854 lines total) and the
   5 audit_100series round files (1097 lines) — these haven't been
   structurally audited yet. Defer to subsequent fires.

## Non-audit observations

- **attempt_001 + addendum is arguably the strongest non-math
  framework doc in the corpus**. It has: (i) upfront 4-class
  framework + 6 predictions; (ii) retrospective addendum expanding
  to 7 classes with marked reformulations; (iii) 5 detailed
  synthesis-note files for per-principle depth; (iv) cross-audit
  self-reference; (v) 4-item explicit open-questions list. The
  only comparable math-side doc is `math/ns_blowup/attempts/
  attempt_849_frobenius_ratio_gap.md` which is the standard.
- **The existence of 5 `audit_100series_20260415*.md` round files**
  is significant — this is a prior in-corpus audit methodology
  (5 rounds, each 200+ lines) matching the pattern the current
  /loop audit is implementing. Cross-audit continuity: the
  biology/evolution/ subdir has its own internal audit trail
  ALREADY.
- **Framework principles A–E together constitute a higher-order
  framework claim** that stands independent of the 7-class
  taxonomy. Even if the 7-class structure needed revision, A-E
  are general-purpose claims applicable to any persistent-
  organism set: disease-incidental, common-hub coevolution,
  therapeutic-convergence, modernity-trajectory-shift,
  class-hybrids-are-common. **Principle-level claims, not
  taxonomy-level claims.**
- **The "biofilm rejected as class-6 subcategory" note** (L436-439)
  is noteworthy Maps-Include-Noise: a considered-and-rejected
  framework expansion is documented, not omitted. Future persistent-
  organism candidates that force a biofilm-class reopening would
  be motivated against that explicit prior rejection.
- **Recommended next fires** target the 5 synthesis notes
  (persistence_mechanisms_taxonomy → host_coevolution →
  therapeutic_convergence → modernity_trajectory → class_boundary_
  cases) and the 5 audit_100series round files. The framework
  doc is done; its ancillary infrastructure is the remaining
  audit surface.

## Tag

119 (biology/evolution framework). Audited attempt_001 + 157-line
addendum. **Fire 46's "consolidate 3 framework updates" recommendation
ALREADY FULFILLED in addendum** — 4→7 class taxonomy with per-class
(new) markers, prediction #2 REFORMULATED old-vs-new (genome-
specialization replacing "larger genomes"), 5 principles A-E with
per-principle synthesis-note file references. **0 🔴**. 4 🟡 (30m-
vs-10m cron version drift, 6-batch/65-claim/~52% audit numbers need
thread to 5 audit_100series round files, HLA-DRB1/TLR2/IL-1β/NLRP3
cross-organism specific mapping, 6 boundary cases not yet audited).
**12 🟢**: 4→7 class taxonomy Maps-Include-Noise (originals preserved,
new classes marked); prediction #2 kill-first reformulation with
explicit old-vs-new; 5 framework principles A–E each with dedicated
synthesis-note file; directory-state tree diagram; **cross-audit self-
reference** (matches attempt_008 pattern — cross-audit integration
working at framework level); 6 predictions pre-registered then
✓/REFORMULATED-labeled; disease-incidental claim with 4 examples +
clinical corollary; host-side coevolution inventory (HLA/KIR/TRIM5α/
HERV/syncytin); principle E honest class-hybrid examples (T. cruzi
4+7, T. pallidum 6+4); kill-ROI "What remains open" (4 specific
next-steps including biofilm-considered-and-rejected); **5 synthesis
notes exist at 1854 lines** (infrastructure real); **5 audit round
files exist at 1097 lines** (prior audit methodology preserved);
anti-problem framing at cross-cutting level. **Observation**: attempt_
001 + addendum is the strongest non-math framework doc in the corpus
— comparable to math/ns_blowup/attempt_849 as gold-standard
template. Next fire: `results/persistence_mechanisms_taxonomy.md`
(411L) + `host_coevolution.md` (378L) first, or one of the 5 audit
round files, or dysbiosis numerics, or WHM sweep (pending op), or
loop termination.
