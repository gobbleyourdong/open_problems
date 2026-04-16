# Attempt 120 — Claim-Backing Audit: biology/evolution/results/persistence_mechanisms_taxonomy.md

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue, Fire 48)
**Scope**: biology/evolution/results/persistence_mechanisms_taxonomy.md
(411L, full read L1-411). First synthesis-note audit after closing
per-organism series.
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: Fire 47 audited attempt_001 framework + addendum. This
file is the detailed 7-class taxonomy the addendum references.

## Executive verdict

**Taxonomy synthesis is solid framework backbone** — per-class
structure (Definition → Examples → Signatures → Prediction test →
Framework strength) applied uniformly across 7 classes. 5 predictions
derived from the taxonomy (genome specialization, species-specificity
+ long coevolution, disease-incidental-post-transmission, class-
determines-therapeutic-options, class-predicts-modernity-trajectory).
Boundary cases + missing-organism sections explicit about what's out-
of-scope.

**Two version-drift inconsistencies** against attempt_001 addendum
(Fire 47):

1. **Audit-numbers disagreement**: this file L10-16 claims "4 batches,
   ~45 claims, ~44% verified / 47% corrected" citing
   `medical/blepharitis/results/claim_audit_2026-04-15.md`;
   attempt_001 addendum L417-419 claims "6 batches, 65 claims,
   ~52% fully verified, ~48% with corrections". These numbers
   don't match. Either (a) taxonomy note was written before
   attempt_001 addendum and the audit progressed 4→6 batches /
   45→65 claims between them; or (b) the two files refer to
   different audit efforts. Worth reconciling.
2. **Stale "status" section**: L381-402 says `attempts/attempt_001
   — cross-cutting framework; needs updates to reference the 7-class
   taxonomy` and lists 4 recommended-next-syntheses (host-side
   coevolution, therapeutic convergence, modernity trajectory, class-
   boundary cases). **All 4 recommended-next items now exist** as
   `results/host_coevolution.md` + `therapeutic_convergence.md` +
   `modernity_trajectory.md` + `class_boundary_cases.md`; attempt_001
   addendum (Fire 47) has added the 7-class taxonomy reference. So
   the "recommended next work" list is stale — already done.

**🔴 RED count**: 0
**🟡 YELLOW count**: 5
**🟢 GREEN count**: 11

## RED / YELLOW findings

| # | Location | Claim | Source gap |
|---|----------|-------|------------|
| Y275 | L10-16 vs attempt_001 L417-419 | Audit numbers disagree: taxonomy says "4 batches, ~45 claims, ~44%/47%"; attempt_001 addendum says "6 batches, 65 claims, ~52%/~48%" | Reconcile — either date-progression or cross-effort conflation |
| Y276 | L381-402 "Status" + "Recommended next synthesis work" section | 4 recommended items (host-coevolution/therapeutic-convergence/modernity/class-boundary) all now DONE as separate results/ files; attempt_001 addendum done | Update "Status" section to reflect synthesis-phase completion |
| Y277 | L267-270 "Plasmodium... uses antigenic variation (class 4, via VSG-like PfEMP1)" | Mechanism mashing | **VSG is Trypanosoma's mechanism; PfEMP1 is P. falciparum's; P. vivax uses hypnozoites (class 1-like dormancy) NOT PfEMP1**. Fix attribution: "P. falciparum uses antigenic variation (class 4) via var gene switching of PfEMP1; P. vivax uses hypnozoites (class 1-like dormancy)". |
| Y278 | L176-187 Prediction 1 "persistence requires genome specialization" | Applied to "HPV is an exception at 8 kb; uses host machinery instead" | 8 kb HPV exception is real but the "uses host machinery" description is vague — HPV uses host differentiation for compartmentalization (class 3); the prediction reformulation should say "OR exploits host-lifecycle" as third form of specialization |
| Y279 | L225-229 "therapeutic success is inversely proportional to persistence-mechanism sophistication" | Strong quantitative claim | Support: class 1 latency/class 5 integration = hard-to-cure (established); class 6 chronic-colonization/class 7 obligate-parasite = more tractable (partly established, but ivermectin-resistant head lice suggest class 7 can evolve around drugs quickly — counter-example) |

## GREEN findings

- **G369** **Per-class 5-line structure applied uniformly** across
  all 7 classes: Definition + Examples + Signatures (multi-bullet)
  + Prediction test + Framework strength. Taxonomic discipline —
  each class has same epistemic treatment.
- **G370** **Framework strength column is honest**: Class 1 strong,
  Class 2 "mid — documented for CVB, suggested for others (EV-71?,
  HCV quasispecies?), not as universally applicable", Class 3
  "medium — single major example", Class 4 "medium in human-
  persistent-organism context; stronger in protozoal", Class 5
  "unique case in current human persistent viruses", Class 6 "strong",
  Class 7 "strong and highly generalizable". Per-class confidence
  calibration.
- **G371** **Prediction test built into each class** — not separately-
  listed success/failure metric. Example: Class 1 "larger genomes
  predict more-elaborate latency machinery → confirmed across
  herpesvirus family". Prediction + in-class confirmation linked.
- **G372** **Prediction 4 therapeutic-options table** (L215-224):
  per-class primary clearance agent + adjunct anti-inflammatory
  + example drug. Clinical-decision-path table. Matches attempt_001
  addendum L370-375 therapeutic-convergence-table.
- **G373** **Prediction 5 modernity trajectory** with explicit
  organism-direction claims: H. pylori ↓ with sanitation; P. gingivalis
  ↑ with Western diet; Demodex ↑ with Western diet (sebum); Malassezia
  ↑ similarly; viral classes mostly neutral. Class-specific modernity
  behavior predictable.
- **G374** **Boundary cases section** (L248-287): MTB (class 6+7
  spectrum), HERV (terminal state of class 5), Plasmodium (class 4
  if added), Toxoplasma (class 6-like with protozoal lifecycle),
  T. cruzi (class 4+7 hybrid). Hybrid-organism explicit handling.
- **G375** **"Classes not covered" section** (L290-313): 7 missing
  organism categories listed (HIV/HIV-2, HBV complex hybrid, HCV
  class 4, MTB class 6, Toxoplasma/Plasmodium/Trypanosoma protozoa,
  Strongyloides, Candida). **Honest scope-labeling**: what's in +
  what's explicitly out + what minor refinements adding them would
  require. L311-313: "Adding any of these would refine the taxonomy
  but wouldn't require new classes — the 7 classes cover the
  persistence-mechanism space broadly." Framework confidence claim
  backed by 16+ organism coverage.
- **G376** **Open theoretical questions** L317-348: 5 specific
  testable/unresolved questions — is 7 enough, do classes coexist
  over evolutionary time, is framework symmetric (predicts WILL
  persistence evolve), do classes correlate with disease severity,
  why hasn't human evolution closed these. Research-agenda quality.
- **G377** L352-375 **two-phase therapeutic architecture universal
  across classes** with doxycycline-40mg-MMP9-inhibition unifying
  classes 6+7. Single-drug cross-class therapeutic unification is
  the framework's cleanest clinical prediction — recommended for
  second-level synthesis.
- **G378** **Verification status with specific cross-audit reference**
  L10-16: "~45 claims" across "4 batches" with ~44% verified /
  47% corrected. File-level audit-provenance tagging. Even though
  the numbers diverge from attempt_001 (Y275), the practice is
  sound — synthesis notes cite their audit backing explicitly.
- **G379** **Biofilm considered-and-rejected** L319-323 (Open Q1):
  "Candidate: biofilm-based chronic infection as a distinct
  mechanism (Pseudomonas in CF, polymicrobial periodontitis).
  Could argue it's a subclass of 6, or a separate 8. Leaving at
  7 for now." Matches attempt_001 addendum's biofilm decision —
  cross-file consistency on rejected expansions.

## Recommended fixes (ordered)

1. **[P1]** Y277 — fix Plasmodium mechanism mashing. P. falciparum
   uses PfEMP1 var gene antigenic variation (class 4); P. vivax uses
   hypnozoites (class 1-like); they are not the same mechanism. One-
   sentence fix.
2. **[P2]** Y275 — reconcile audit numbers (4-batch/45-claim/44%
   vs 6-batch/65-claim/52%) either by dating the two snapshots or
   by cross-linking the audit sources. The taxonomy note and
   attempt_001 addendum should share a single audit-provenance
   anchor.
3. **[P2]** Y276 — update Status section and "Recommended next
   synthesis work" list — 4/4 recommended items now done as
   separate results/ files; attempt_001 addendum added taxonomy
   ref. List is stale.
4. **[P3]** Y278 — Prediction 1 reformulation should include
   "OR exploits host-lifecycle" as third form of genome-
   specialization to cleanly include HPV's 8 kb / lifecycle
   compartmentalization case.
5. **[P3]** Y279 — add ivermectin-resistant head lice as counter-
   example for "class 7 more tractable than class 1" claim.

## Non-audit observations

- **The taxonomy file is structurally sound** but has **version-
  drift against attempt_001 addendum**. This is expected when two
  synthesis files are worked in parallel — one evolves faster than
  the other. The audit-numbers disagreement (Y275) and stale "Status"
  section (Y276) are both version-drift artifacts, not errors of
  substance.
- **Plasmodium mechanism-mashing (Y277)** is the one substantive
  fix — mechanisms from 2-3 different organisms (VSG from Trypanosoma,
  PfEMP1 from P. falciparum, hypnozoites from P. vivax) are
  conflated in a single sentence. Fix is precise and 1-sentence
  length. This is the kind of error a WebSearch-based content audit
  would catch (prior `claim_audit_2026-04-15.md` might already have
  caught it in rounds 2-5 — worth checking).
- **The framework-strength honesty** (per-class "strong / medium /
  mid / unique" labeling) is sigma-method confirmation-bias-audit-
  compliant. Classes aren't all equally well-supported; the synthesis
  says so.
- **4 recommended-next-synthesis items all now done** as separate
  results/ files. The biology/evolution synthesis phase has
  essentially completed its own roadmap — next-level work is
  audit + consolidation, not new synthesis notes.
- **Next highest-leverage audit targets**: `host_coevolution.md`
  (378L) is likely strongest remaining synthesis note because it
  anchors the framework's host-side half. The 5 audit_100series
  round files are also high-value — they represent the prior audit
  methodology with specific claim counts.

## Tag

120 (biology/evolution/results/persistence_mechanisms_taxonomy.md).
411-line full read. **0 🔴**. 5 🟡: **audit-numbers version-drift**
(this file 4 batch/45 claim/44%-47% vs attempt_001 addendum 6 batch/
65 claim/52%-48% — reconcile provenance); **stale Status section**
(4 recommended-next-syntheses all done as results/ files;
attempt_001 addendum added taxonomy ref); **Plasmodium mechanism-
mashing** (VSG=Trypanosoma, PfEMP1=P.falciparum, hypnozoites=P.vivax
all conflated in one sentence — substantive fix required);
Prediction 1 could add "OR exploits host-lifecycle" as third genome-
specialization form for HPV; Prediction 4 "therapeutic success
inversely proportional to sophistication" counter-example
(ivermectin-resistant head lice). **11 🟢**: per-class 5-line
structure applied uniformly across 7 classes; **framework-strength
column honest per-class confidence calibration** (strong/medium/mid/
unique); prediction-test built into each class; Prediction 4
therapeutic-options table with per-class primary clearance + adjunct;
Prediction 5 modernity-trajectory organism-direction claims; boundary
cases section handling hybrid organisms (MTB 6+7, T. cruzi 4+7,
etc.); **"Classes not covered" explicit scope-labeling** (7 missing
organism categories named, framework confidence backed by 16+
organism coverage); 5 open theoretical questions with research-
agenda quality; two-phase therapeutic architecture universal-across-
classes with doxycycline-40mg unifying classes 6+7; verification
status with specific cross-audit reference (~45 claims / 4 batches);
**biofilm considered-and-rejected with cross-file consistency to
attempt_001 addendum**. **Observation**: synthesis phase has
completed its roadmap — 4/4 recommended-next-items done as separate
results/ files. Next-level work is audit + consolidation, not new
synthesis. **Recommendation**: next fires target `host_coevolution.md`
(378L, framework's host-side half) or the 5 `audit_100series_20260415*.
md` round files (1097L, preserved audit methodology). Dysbiosis
numerics, WHM sweep (pending op), or loop termination remain
alternatives.
