# Attempt 020 — Claim-Backing Audit: dysbiosis/ top-level + attempt_001 spot-check

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue)
**Scope**: medical/dysbiosis/PROBLEM.md (221 lines), gap.md (141 lines,
136 current + archived pointer), THEWALL.md (152 lines), sample
attempt_001_m4_threshold_proxy.md. Archives (gap_extensions_archive.md
4311 lines, thewall_extensions_archive.md 6832 lines) NOT audited —
flagged as archived-historical per Maps-Include-Noise.
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: audit log attempts 095–103 (all t1dm)

## Executive verdict

**dysbiosis/ is the strongest non-math subdir seen in the audit so
far, at the top-level-doc level.** PROBLEM.md runs a Phase 0 shape-
check, threads specific PMC/PMID citations, separates mountains with
"Evidence / Wall / Status" rubrics, and integrates cross-directory
references. gap.md states the core gap sharply (causation direction)
and names sigma-method-specific limits. THEWALL.md correctly frames
M4 (host-microbe threshold) as the convergent obstruction and
acknowledges what the method CANNOT cross (wet-lab interventions).

Archives are handled correctly (Maps-Include-Noise compliant) — 301
per-run Extension blocks moved to separate files, pointers to
canonical `numerics/run_NNN_*.md` files retained.

attempt_001 uses a tight structured template (Mountain / Hypothesis /
Evidence Base / Mechanistic Chain / Kill Test / Predictions / Evidence
FOR:FOR-count / AGAINST-count / Current Status / Stall Point / Sky
Bridge / Next Action) that matches sigma v7.1 stall-point methodology
better than anything seen in t1dm/ attempts 001–035.

**🔴 RED count**: 1
**🟡 YELLOW count**: 7
**🟢 GREEN count**: 10

## RED findings

### R24 — PROBLEM.md L109, L126 ("Wim Hof Method → beta-arrestin-2 → NF-κB lock")

**The claim** (L199 in PROBLEM.md "Host side (threshold modulation)"
list):
> "Wim Hof Method (beta-arrestin-2 → NF-κB lock)"

**Why load-bearing**: this claim replicates attempt_102's R22
finding against t1dm/SUPPLEMENT_SCHEDULE.md. It appears in
PROBLEM.md as a threshold-modulation item without a citation or
softening.

**Concern**: same issue as R22 — Kox et al. 2014 *PNAS* (PMID
24799686) demonstrated attenuation of cytokine response to LPS via
WHM-induced epinephrine; they did NOT demonstrate NF-κB "lock." The
β-arrestin-2 → IKKα mechanism at physiological epinephrine is
modulation, not lock. Propagating the overstated framing from
t1dm/SUPPLEMENT_SCHEDULE.md into the dysbiosis/PROBLEM.md treatment
table makes the same overreach at higher-visibility entry point.

**Required fix**: soften to "WHM → epinephrine → attenuated NF-κB
activation in response to LPS (Kox 2014 PNAS, PMID 24799686)."

## YELLOW findings

| # | File / line | Claim | Source gap |
|---|-------------|-------|------------|
| Y106 | PROBLEM L103 | "Kitavan islanders: Cordain et al. 2002 zero-acne cohort of 1200" | Cordain et al. 2002 *Arch Dermatol* PMID 12472346; thread PMID — otherwise this is a strong claim |
| Y107 | PROBLEM L109 | "Amish vs Hutterite study" | Stein MM et al. 2016 *NEJM* PMID 27518660; thread PMID |
| Y108 | PROBLEM L91 | "EBV causal evidence for MS (2022 Bjornevik study)" | Bjornevik et al. 2022 *Science* PMID 35025605; thread PMID — strong claim, strong evidence |
| Y109 | PROBLEM L119 | "PMC7305306 (Graves lab 2020): P. gingivalis in pancreatic beta cells" | PMC ID is verifiable; double-check the year and whether "Graves lab" is the correct attribution |
| Y110 | PROBLEM L112 | "Rudensky lab (Science 2015) early-life Tregs" | Yang et al. 2015 *Science* (Rudensky lab); thread specific PMID |
| Y111 | gap.md L31 | "Zhang 2021 challenged the [zonulin] assay specificity" | Author/journal needs verification — Ajamian/Scheiman/Fasano group has published on zonulin specificity; "Zhang 2021" needs confirmation |
| Y112 | gap.md L50 | "TinyHealth FASTQ order for CVB detection" | Commercial product; not a research source, just a pointer to user's own data — OK as context |

## GREEN findings

- **G51** PROBLEM.md L31–43 — **explicit Phase 0 shape-check**
  (sigma v7 principle) with all 5 questions answered and wall
  classification (MECHANISTIC + TECHNOLOGICAL with behavioral
  contributors). First non-math subdir to run Phase 0 correctly.
- **G52** PROBLEM.md L43 — correctly distinguishes dysbiosis (not
  behavioral wall) from POD (behavioral wall per Phase 0). Cross-
  directory calibration of method applicability — matches sigma
  method v7 Method Domain Map.
- **G53** PROBLEM.md L76–128 — **Mountains 1-7 with Evidence / Wall /
  Status rubric** per mountain. Mountain 7 marked "(Added in Phase 3 —
  was not in original problem scaffold)" — explicit evolution
  tracking. Matches sigma method's Maps-Include-Noise principle
  (Phase 3 additions kept as first-class mountains, not retcon'd into
  originals).
- **G54** PROBLEM.md L155–172 — **Testable Predictions per mountain**.
  Each mountain has falsifiable predictions tied to specific
  interventions. "Populations transitioning to Western diet should
  show rising dysbiosis-linked disease rates within 1 generation
  ✓ (validated)" — explicit validation mark for one prediction.
- **G55** gap.md L3–16 — **Core gap stated as single sentence** and
  classified as candidate for sigma's certificate-equivalence limit
  (from v5 RH meta-theorem). This is the correct move when the method
  may not apply — name the limit explicitly.
- **G56** gap.md L64–76 — intervention-precision table with "what it
  does well" vs "what it can't do" columns. Matches math-style
  "what's proven vs what remains."
- **G57** gap.md L102–110, 112–122 — **The "Super-Organism Frame"
  and "The Integration Gap"** sections both correctly name gaps at
  a level the individual-study literature doesn't address.
- **G58** THEWALL.md L1–34 — **wall identified as M4 (host-microbe-
  substrate integration)** with the other mountains mapped as
  peripheral routes. Not a list of difficulties — a single
  integrative failure mode.
- **G59** THEWALL.md L79–102 — **explicit sigma-method capability
  statement**: what the method CAN do (map gaps, identify kill ROI,
  design biomarker panels in silico) and what it CANNOT (wet-lab
  experiments). This is the kind of operator-gap-aware framing that
  sigma v8 added.
- **G60** attempt_001 structured template (Mountain / Hypothesis /
  Evidence Base / Mechanistic Chain / Kill Test / Predictions /
  Evidence FOR:count / AGAINST:count / Current Status / Stall Point
  / Sky Bridge / Next Action) — **this is the template the
  non-math subdirs should adopt**. The "Stall Point" and "Evidence
  FOR:2/3 AGAINST:1/3" scoring matches sigma v7.1 stall-point
  methodology.

## Recommended fixes (ordered)

1. **[P0]** PROBLEM.md L199 — soften WHM "NF-κB lock" (R24 — same as
   t1dm R22 fix). One-word change.
2. **[P1]** Thread PMIDs for the big-name citations (Cordain 2002,
   Stein 2016, Bjornevik 2022, Rudensky/Yang 2015) — 4 refs.
3. **[P2]** Confirm or correct "Zhang 2021" zonulin-challenge
   citation (Y111).
4. **[P2]** The attempt_001 template should be promoted to a
   TEMPLATE.md in attempts/ (which I see already exists per the Fire
   2 file listing — check and confirm it matches attempt_001 style).

## Non-audit observations (map features)

- **dysbiosis/ is the template for how non-math subdirs should
  look.** It runs Phase 0, it has a clean mountain-analysis in
  PROBLEM.md, gap.md states the gap sharply and names method limits,
  THEWALL.md identifies the convergent obstruction with sigma-method
  self-awareness.
- The 169-run archive pointer (gap.md L135–141) is a correct Maps-
  Include-Noise move: individual run files preserved; summary
  extensions archived; canonical pointer kept in the reader-facing
  doc. This is exactly the pattern that t1dm/ should adopt for its
  own synthesis material.
- attempt_001's "Evidence FOR: 2/3 / Evidence AGAINST: 1/3" scoring
  converts the usual "hedged prose" of medical synthesis into a
  numeric indicator. This is lightweight but effective — a reader can
  rank attempts by "how strong is this hypothesis?" at a glance.
- The cross-directory references in PROBLEM.md (to ../t1dm, ../POD,
  ../eczema etc.) make dysbiosis/ a legitimate umbrella dir per its
  stated purpose. Other medical subdirs would benefit from
  reciprocal pointers back to dysbiosis/ where applicable.

## Tag

020. First audit pass on medical/dysbiosis/. Top-level files +
attempt_001 spot-check. **1 🔴** (WHM "NF-κB lock" overstatement,
same as t1dm R22 — propagated between subdirs). **7 🟡** (PMID
threading for Cordain 2002, Stein 2016, Bjornevik 2022, Rudensky
2015; Zhang 2021 zonulin citation verification). **10 🟢** — highest
green count in any audit so far. Phase 0 shape-check correctly run,
mountains structured with Evidence/Wall/Status rubric, gap.md names
sigma-method-specific limits, THEWALL.md identifies convergent
obstruction and method's own limits, attempt_001 template matches
sigma v7.1 stall-point methodology. **Observation: dysbiosis/ is the
template other non-math subdirs should follow.** Next fire:
medical/dysbiosis/ deeper attempt audit, or start a different medical
subdir (perioral_dermatitis is referenced; myocarditis, me_cfs, acne
all in queue).
