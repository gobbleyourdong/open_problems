# Post-audit remediation summary (2026-04-15 → 2026-04-18)

This file replaces the prior `AUDIT_LOG.md` / `AUDIT_SYNTHESIS_2026-04-15.md` /
`WHM_NFkB_CROSS_SUBDIR_FIX.md` tracking artifacts (all removed 2026-04-18 once
their findings landed in source files). Per-attempt `attempt_NNN_audit*.md`
files and inline `## 2026-04-18 audit note` sections still reference specific
"fires" from the old log — those are provenance tags for where the finding
originated, and the content of each audit note is self-contained.

## What the audit produced

- **71 audit fires** (62 non-math + 9 math) over 2026-04-15, catalogued 37 🔴
  RED, ~255 🟡 YELLOW, ~400 🟢 GREEN findings across
  medical/biology/physics/philosophy subdirs.
- **12 top-tier documents** identified as matching the `math/ns_blowup` gold
  standard (CLINICAL_BRIEF, EVIDENCE_GRADES, DRUG_SAFETY_MATRIX, FAILURE_MODES,
  FOR_YOUR_DOCTOR, medical/THEWALL, pericarditis/THEWALL, t1dm/gap.md,
  physics/what_is_time/gap.md, biology/evolution/attempt_001, biology/
  evolution/results/therapeutic_convergence, blepharitis/attempt_007).
- **Math Lean state recounted** under strict regex (not `grep -c sorry` which
  inflates 4.5× from self-report comment hits). **Actual: 19 live sorry across
  117 files; 9 proof-tactic sorry all in `ns_blowup/Blowup.lean` +
  `Challenge.lean` — the actual research frontier.**

## What the 2026-04-18 remediation fixed

### RED findings — all 37 closed

Every 🔴 RED finding now has a `## 2026-04-18 audit note` section in the
offending file (Maps-Include-Noise v6 — original wording kept above a dated
separator). Fixes include:

- **WHM NF-κB sweep** — 12 coordinated edits across 7 files in 4 subdirs
  replacing "NF-κB lockdown" (overstated) with "attenuated NF-κB activation
  (Kox 2014 *PNAS* PMID 24799686)" — closes R22/R24/R26/R29/R34.
- **t1dm attempt corrections** with verified PMIDs — Herold 2019 *NEJM* PMID
  31180194, Yeung 2011 *BMJ* PMID 21292721, Krogvold 2015 PMID 25475435,
  Meier/Butler 2005 *Diabetologia* PMID 16205882 (disambiguated from Butler
  2003 T2DM PMID 12502499), TRIGR 2018 *JAMA* PMID 30027203, Pescovitz 2009
  *NEJM* PMID 19915291, Longo 2017 *Cell* PMID 28683282.
- **physics/README** — "parameter-free" claim corrected to honest two-input
  framing (ΔE ≈ 16.58 kT + chain parameters) per what_is_time/gap.md.
- **persistent_organisms/PROBLEM** — COR388/atuzaginstat inline update
  noting GAIN 2021 failure + Cortexyme → Quince pivot.
- **t1dm/PROBLEM.md** — Phase-0 scaffold banner added pointing readers to
  `gap.md` for current Phase 4/5 state.

### v9.1 discipline propagated to 21 framework-shaped docs

Every framework-shaped and tier-0 doc in the corpus now carries explicit
`Would falsify` + `Prior art` sections per `~/SIGMA_METHOD.md` v9.1 C5/D2:

- 3 cross-subdir framework audits (K-framework physics, α/β/γ philosophy,
  Treg-NLRP3 medical)
- All 9 philosophy gap.md (mind, good, knowing, language, meaning, number,
  self, beauty, life)
- All 7 physics gap.md (time already top-tier; nothing, information,
  self_reference + umbrella notes for reality, change, computation)
- 4 heavy-use medical/bio gap.md (dysbiosis, me_cfs, blepharitis,
  biology/evolution)

### Citation discipline — VERIFIED_REFS.md pattern

**5 subdirs** now carry central PMID-threaded reference files:

| File | Entries | Status |
|------|---------|--------|
| `medical/dysbiosis/VERIFIED_REFS.md` | 20 top-cited refs | 10 ✅ / 3 FM1a year-drift / 1 FM1b journal-drift / 6 candidates / 1 deferred |
| `medical/t1dm/VERIFIED_REFS.md` | 9 refs | 8 ✅ / 1 unresolved |
| `medical/blepharitis/VERIFIED_REFS.md` | 6 refs | 6 ✅ (Koo/Zhao FM1d author-drift alias disambiguated) |
| `medical/me_cfs/VERIFIED_REFS.md` | 4 refs | 4 ✅ (Younger 2013 year-drift corrected from Fire 36 "2018") |
| `biology/evolution/VERIFIED_REFS.md` | 3 canonical evo-immunology refs | 2 ✅ / 1 deferred (+ 2 recursive audit-layer PMID errors corrected) |

**Rule**: per-run / per-attempt files can cite "Author Year, see
VERIFIED_REFS.md" rather than re-specifying PMIDs each time.

### Case study filed

Method-development finding: **citation drift is a Claude-specific
stale-prior failure mode (FM1a/b/c/d)** — year-drift, journal-drift,
fabrication, author-drift. Documented in
`~/sigma/case_studies/citation_year_drift_001.md` (250+ lines with
taxonomy + corrective principles + recursive-validation findings).
Rates in sampled dysbiosis/t1dm/blepharitis/me_cfs/biology-evolution
corpora: ~35–40% total drift, ~53–60% clean verification.

### Philosophy preservation

Per operator decision 2026-04-18: **philosophy/ preserved in full** (9
subdirs, all attempts/gap.md/numerics/lean intact). Original intent of
"blow away" revised after per-subdir audit revealed empirical results
sharper than much published philosophy-of-mind/language/metaethics.

## What is NOT resolved

- **Küpers 2019 PACE EWAS** — permanently deferred (external data access
  required); carried as map-feature per Maps-Include-Noise.
- **Candidate fabrications**: Faulkner 2017, Bystrom 2008, Barrett 2009,
  Cheng 2014, Shim 2021 (+ Buhl 2017 ambiguous) — no matching papers
  located by WebSearch; flagged in per-subdir VERIFIED_REFS files.
- **Long-tail per-attempt citations** across persistent_organisms + medical
  top-level docs + biology/evolution 100-113 — covered by the content-audit
  at `medical/blepharitis/results/claim_audit_2026-04-15.md` (65 claims,
  ~52% verified, 1 full fabrication Liang 2018 pediatric chalazion).

## Where the tracking artifacts went

Removed 2026-04-18:

- `AUDIT_LOG.md` — 88 fires of per-fire tracking (62 original audit + 13
  remediation + 13 README-update). Contents absorbed into:
  - Per-attempt audit notes (content)
  - Per-subdir VERIFIED_REFS.md (PMID threading)
  - This file (summary)
  - `~/sigma/case_studies/citation_year_drift_001.md` (method-development)
- `AUDIT_SYNTHESIS_2026-04-15.md` — mid-campaign synthesis, superseded by
  the above.
- `WHM_NFkB_CROSS_SUBDIR_FIX.md` — executed 2026-04-18; 12 edits landed in
  source files (dysbiosis/PROBLEM L199, t1dm/SUPPLEMENT_SCHEDULE L74,
  t1dm/print_schedule.py L122+L158, psoriasis/PROBLEM L49,
  PATIENT_ZERO_TIMELINE L251, plus 🟡 softening at 4 attempt files).

The math audit was archived at `math/attempts/dropped_audit_2026-04-18/`
per the v6 precedent (9 fires + synthesis).

## How to trace a specific finding

Audit notes in attempt files reference "R# from AUDIT_LOG fire N" or
"Y### from Fire N" as provenance. Since the fire log is removed, the
fire number is only useful if you need the meta-context; the finding
itself is self-contained in the audit note.

For PMID verification of a specific reference: start with the relevant
`VERIFIED_REFS.md` in the subdir; if the reference is not there, the
content audit at `medical/blepharitis/results/claim_audit_2026-04-15.md`
covered 65 biology/evolution + blepharitis claims.
