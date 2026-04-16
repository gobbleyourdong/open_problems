# Attempt 121 — Claim-Backing Audit: biology/evolution/results/host_coevolution.md

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue, Fire 49)
**Scope**: biology/evolution/results/host_coevolution.md (378L, full
read). Second synthesis-note audit after taxonomy (Fire 48).
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: Fire 48 audited taxonomy — structural + content patterns.
Expecting similar structure here.

## Executive verdict

**Host-side framework solid and well-sourced in specific places.**
7 categories of coevolution covered (HLA I+II, KIR, restriction
factors, HERVs, cytokine polymorphisms, innate-immunity receptors,
blood group antigens) with per-category tables showing organism-to-
gene pairings. The composite-picture table (L267-278) maps each of
the 10 organisms to its primary host-gene coevolution signal —
clean synthesis of attempts 002-010.

**Key improvement over taxonomy.md**: this file contains an
**in-text PMID with "verified in audit" annotation** — L195: "IL-1B
-31T/C, -511C/T · El-Omar 2000 Nature PMID 10746728 (verified in
audit)". This is the clearest single example in biology/evolution/
synthesis of inline citation-plus-audit-provenance.

**Same stale-status-list issue as taxonomy.md (Y276)**: L357-372
"What's still needed in biology/evolution/" lists items 3-6 all
now DONE (therapeutic_convergence.md + modernity_trajectory.md +
class_boundary_cases.md + attempt_001 addendum). Parallel
version-drift artifact.

**🔴 RED count**: 0
**🟡 YELLOW count**: 5
**🟢 GREEN count**: 12

## YELLOW findings

| # | Location | Claim | Source gap |
|---|----------|-------|------------|
| Y280 | L357-372 "What's still needed" section | Items 3-6 (therapeutic convergence / modernity trajectory / class-boundary / attempt_001 update) all marked remaining | All 4 now DONE — parallel stale status to taxonomy.md Y276. Update to mark complete. |
| Y281 | L11-14 "Five of those attempts have had audit passes; 5 are still at trained-prior level" | Audit-pass count | Per Fires 44-46 my structural audit covered 9/9 per-organism attempts; per `audit_100series_*_round{1..5}.md` prior content audit covered some. Specific claim "5 audited / 5 unaudited" needs reconciling with actual audit state. |
| Y282 | L64 "(>20,000 alleles at HLA-B)" | Allele count | IPD-IMGT/HLA database (latest 2024-2025 release) lists HLA-B at ~19,000 alleles — close but verify current count; "over 20,000" may be rounded up |
| Y283 | L139 "TRIM5α ... human TRIM5α distinct from chimp/gorilla" | Specific paper | Sawyer 2005 PMID 15780005 "Positive selection of primate TRIM5alpha identifies a critical species-specific retroviral restriction domain" — thread PMID |
| Y284 | L120-124 "Memory-like NK cells... discovered through HCMV studies" | Foundational paper | Sun 2009 Nature PMID 19136945 "Adaptive immune features of natural killer cells" + Lopez-Vergès 2011 PNAS PMID 21876173 expansion of NKG2C+ NK cells in CMV+ individuals — thread PMIDs |

## GREEN findings

- **G380** **Per-category coverage 7-section structure**: HLA class
  I → HLA class II → KIR/NK → intrinsic restriction factors →
  HERVs → cytokine polymorphisms → innate-immunity receptors →
  blood group antigens. 7 distinct coevolutionary axes mapped.
- **G381** **Composite-picture table** (L267-278): 10 organisms
  × primary host-gene coevolution signal. Synthesis-level
  organism-to-gene map. Matches attempt_001 addendum principle B
  (host-coevolution-common-hubs).
- **G382** **Inline PMID + "verified in audit" annotation** (L195):
  "IL-1B -31T/C, -511C/T · El-Omar 2000 Nature PMID 10746728
  (verified in audit)". Cleanest example in biology/evolution/
  synthesis of citation-plus-audit-provenance. Should be
  replicated across other claims in the file.
- **G383** **Per-HLA-class organism mapping tables** (L71-76 for
  class I / L88-93 for class II): specific allele names with
  organism pairings — HIV B*57/B*27 protective, EBV HLA-DR15
  (DRB1*15:01) MS susceptibility, P. gingivalis HLA-DRB1 shared
  epitope RA, T1DM-via-CVB HLA-DR3+DR4. Math-standard specificity
  in allele names.
- **G384** **"The argument is not 'every immune polymorphism is
  persistent-organism driven'"** L46-51 — **honest scope-limiting
  statement**: "other forces (acute zoonoses, parasitic infections
  outside the list, non-immune selection) matter too. The argument
  is that the persistent-organism set is a major co-driver
  alongside these other forces." Prevents over-attribution.
- **G385** **Intrinsic restriction factor table** (L137-145) — 7
  factors with specific targets + evidence-of-positive-selection:
  TRIM5α, APOBEC3G, BST-2/tetherin, SAMHD1, MX1, SERINC5, GBP
  proteins. "Molecular trench warfare" framing.
- **G386** **HERV section dual framing** (L158-184): HERVs as
  terminal state of class 5 + HERVs as active contributors
  (syncytin-1 placental, HERV-W-Env temelimab/GNbAC1 MS trial).
  Non-reductive treatment.
- **G387** **Cytokine polymorphism table** L193-203 with per-
  polymorphism persistent-organism context. IL-1B El-Omar 2000
  PMID 10746728 explicit; others (IL-1RN, IL-6 -174G/C, TNF
  -308A/G, TLR2, TLR4 Asp299Gly, NOD2, IL-23R/IL-17, NLRP3) by
  gene name with mechanistic context.
- **G388** **Innate-immunity receptor section** (L212-238): TLR2/
  TLR4/CLEC7A/NOD1-2/NLRP3 with per-receptor organism-context.
  Specifically NLRP3 central-to-Demodex-B.oleronius-rosacea
  with cross-link to `medical/dysbiosis/run_046`.
- **G389** **Blood group antigens as bacterial-adhesion modulators**
  (L241-255) — 4th category of host-side selection beyond the
  "classic" immune genes. H. pylori BabA-Lewis-b, norovirus
  secretor/Lewis, ABO regional distribution. Non-immune
  coevolutionary signal.
- **G390** **4 predictions + 5 open questions** (L292-338): top-
  of-its-class research-agenda structure. Prediction 3 "drugs
  targeting shared immunogenetic hubs should have cross-disease
  efficacy" ties directly to attempt_001 addendum principle C
  (therapeutic convergence with doxycycline 40mg). Cross-file
  prediction-consistency.
- **G391** Self-awareness of own audit state (L11-14): "Five of
  those attempts have had audit passes; 5 are still at trained-
  prior level. Specific effect sizes and PMIDs require audit-loop
  verification." Honest labeling of incomplete audit coverage.

## Recommended fixes (ordered)

1. **[P2]** Y280 — update "What's still needed" L357-372 to mark
   items 3-6 as ✅ DONE (parallel to taxonomy.md fix). The "Items
   3-6 remain" claim is false since all 4 referenced files exist.
2. **[P2]** Thread PMIDs for TRIM5α (Sawyer 2005 PMID 15780005)
   + memory-like NK HCMV (Sun 2009 PMID 19136945, Lopez-Vergès
   2011 PMID 21876173). Extend the "(verified in audit)" pattern
   from IL-1B/El-Omar to other claims.
3. **[P3]** Y281 — reconcile "5/10 attempts audited" claim against
   current state (9/9 structural + prior content-audit-rounds).
4. **[P3]** Y282 — verify HLA-B allele count against current
   IPD-IMGT/HLA release; >20,000 may be slightly high.

## Non-audit observations

- **"Verified in audit" annotation pattern** (G382, L195) is the
  single cleanest citation-plus-provenance tag in the biology/
  evolution synthesis corpus. If applied consistently across the
  cytokine polymorphism table (L193-203) and the other specific
  claims in this file, it would become the gold-standard template
  for cross-document audit integration.
- **host_coevolution.md + persistence_mechanisms_taxonomy.md
  together constitute the framework's two-sided foundation**:
  taxonomy = organism-side (7 classes); host_coevolution = host-
  side (7 gene categories). Both 378-411 lines; both have per-
  category structured tables; both have composite-picture synthesis;
  both have predictions + open questions. Parallel discipline.
- **The composite-picture table** (G381, L267-278) is effectively
  a **two-way mapping** against the taxonomy.md table: taxonomy
  gives organism→class; host_coevolution gives organism→host-gene.
  Combined, one can read "class 1 EBV → HLA-DR15+class-I-CTL",
  "class 6 H. pylori → HLA-DQ+IL-1B+Lewis", "class 7 Demodex →
  TLR2+cathelicidin". Two-way read is non-trivial synthesis output.
- **The stale status-list pattern** (Y280 here, Y276 at taxonomy.md)
  suggests a **natural next maintenance pass** — both synthesis
  notes' "what's still needed" sections should be bulk-updated
  together. The two files were written before the other synthesis
  notes existed; now that the synthesis phase is complete, both
  status sections can be bulk-marked DONE.
- **attempt_001 addendum principle B** ("host-coevolution common
  hubs: HLA-DRB1, TLR2, IL-1β, NLRP3 repeatedly named across the
  persistent-organism set") is backed by this file's composite-
  picture table. Y273 from Fire 47 (asking for specific cross-
  organism mapping) is **resolved here** — the composite table
  provides exactly that mapping.

## Tag

121 (biology/evolution/results/host_coevolution.md). 378L full read.
**0 🔴**. 5 🟡 (stale "What's still needed" section marking items
3-6 remaining when all 4 now exist as separate files; "5/10 audited"
claim needs reconciling with actual audit state; HLA-B allele count
>20,000 slightly high vs IPD-IMGT current; TRIM5α Sawyer 2005 PMID
15780005 thread; memory-like NK Sun 2009 PMID 19136945 + Lopez-
Vergès 2011 PMID 21876173 thread). **12 🟢**: 7-category
coevolution structure (HLA I+II/KIR/restriction-factors/HERVs/
cytokines/innate-receptors/blood-groups); composite-picture 10-
organism×host-gene table; **inline PMID + "verified in audit"
annotation** (El-Omar 2000 PMID 10746728) = **cleanest citation-
plus-provenance tag in biology/evolution/ synthesis corpus**;
per-HLA-class allele-specific mapping (HIV B*57/B*27 protective,
EBV HLA-DR15/DRB1*15:01 MS, P. gingivalis HLA-DRB1 shared epitope
RA, T1DM HLA-DR3+DR4); honest scope-limiting disclaimer L46-51 (not
every immune polymorphism is persistent-organism driven); intrinsic
restriction factor 7-factor table with positive-selection evidence;
HERV dual-framing (terminal class 5 + active co-opted syncytin-1/
MS-trial temelimab); cytokine polymorphism + innate-receptor
per-organism mapping; blood group as non-immune coevolutionary
signal (H. pylori BabA-Lewis-b); 4 predictions + 5 open questions;
self-awareness of incomplete audit coverage L11-14; **resolves
Fire 47 Y273** (HLA-DRB1/TLR2/IL-1β/NLRP3 cross-organism specific
mapping now documented in composite table). **Observation**:
host_coevolution + taxonomy form framework's **two-sided foundation**
(organism-side + host-side, both ~400L, parallel structure). Composite
table enables two-way organism→class AND organism→host-gene read.
"Verified in audit" pattern should be replicated across other claims.
Both files have parallel stale status-list issues — bulk-update
recommended. Next fire: `therapeutic_convergence.md` (358L —
doxycycline 40mg cross-class mechanism), `modernity_trajectory.md`
(347L), `class_boundary_cases.md` (360L), 5 `audit_100series_round
{1..5}.md` files (1097L preserving prior audit methodology),
dysbiosis numerics, WHM sweep (pending op), or loop termination.
