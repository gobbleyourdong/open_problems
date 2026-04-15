# Attempt 095 — Claim-Backing Audit: attempts 001–010

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue item 1)
**Scope**: medical/t1dm/attempts/attempt_001_teplizumab.md …
attempt_010_mrna_tolerance.md
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
(specific artifact citations, named-script-with-measurement, what-proven-vs-remains)

## Executive verdict

**Overall**: mostly 🟡 YELLOW. The ten attempts correctly identify the
right trials, the right failure modes, and the right mechanistic gaps,
but threading to sources is inconsistent. Authors + year + journal appear
for most marquee trials; PMIDs/DOIs never appear; several
material-to-the-argument numbers have no source line.

**🔴 RED count**: 2 (attempt_001 median-delay numerics, attempt_004
DIAGNODE-2 outcome summary ambiguity)
**🟡 YELLOW count**: 11 (details below)
**🟢 GREEN count**: 4 (attempt_007 Sana UP421, attempt_008 Deng CiPSC,
attempt_002 Shapiro NEJM 2000, attempt_010 LNP-CTB-GADIII)

No attempt was an overall RED — each one is substantively correct in its
high-level claims. The issue is reproducibility: a reader cannot trace
the specific numbers back to the specific paper without independent
search.

## RED findings

### R1 — attempt_001_teplizumab.md L12–13
> "Median delay: ~2 years (72.2 months teplizumab vs 24.4 months placebo)
> HR 0.41 (p=0.006)"

**Why load-bearing**: the 2-year delay and the HR are the quantitative
backbone of the "sledgehammer that buys time" conclusion. If the medians
are wrong, the "~2 years" summary is still defensible but the file's
authority on the exact numbers is not.

**The specific concern**: the Herold et al. 2019 *NEJM* TN-10 paper
(PMID: 31180194) reported median time to T1DM diagnosis of **48.4
months teplizumab vs 24.4 months placebo (HR 0.41, p=0.006)** — a
~24-month / 2-year delay. The 72.2-month figure in the attempt is
higher than the original trial report and may conflate an
extension-cohort update (Sims et al. 2021 *Sci Transl Med* or later
follow-up) with the primary endpoint. Whatever the true figure is, it
needs a named source in-line.

**Required fix**: change the number, or split into two lines:
(a) primary 2019 endpoint (Herold NEJM, PMID 31180194): median 48.4 vs
24.4 months, HR 0.41, p=0.006; (b) extended follow-up with its own
citation if 72.2 is to stand.

### R2 — attempt_004_gad_vaccine.md L10
> "DIAGNODE-2 (2021): GAD-alum injected into lymph nodes … Mixed results,
> some C-peptide preservation in HLA-selected subgroup."

**Why load-bearing**: DIAGNODE-2 is invoked as evidence that intralymphatic
delivery is worth pursuing. "Mixed results" without a primary-endpoint
verdict hides that the trial **missed its primary endpoint**. The
in-subgroup HLA-DR3-DQ2 signal was pre-specified as secondary and is
the only positive read.

**Required fix**: state primary endpoint verdict explicitly
(missed), cite Ludvigsson et al. 2021 (*Diabetes Care* or follow-up),
and say which HLA subgroup showed benefit at what effect size.

## YELLOW findings

| # | Attempt / line | Claim | Missing |
|---|----------------|-------|---------|
| Y1 | 002 L8 | "~50% insulin independence at 5 years (revised protocol)" | Source paper (Collaborative Islet Transplant Registry CITR annual reports) |
| Y2 | 002 L19 | "~8,000 deceased donor pancreases/year in the US, ~1.5M T1DM patients" | OPTN/UNOS figures year + CDC T1DM prevalence source |
| Y3 | 002 L9 | "FDA approved Lantidra (donislecel) June 2023" | FDA press release / BLA number |
| Y4 | 003 L22 | "Estimated >$500K per patient" | Any Vertex financial filing or analyst report |
| Y5 | 004 L8–9 | "Phase 2 (Ludvigsson 2008, NEJM)" + "Phase 3 (DIABGAM, 2012): FAILED primary endpoint" | PMIDs, effect sizes, primary endpoint specification |
| Y6 | 005 L7 | "Bluestone/Tang (UCSF) … Published STIM (2015)" | Should be *Sci Transl Med* 2015 — journal abbreviation is ambiguous; PMID 26606968 |
| Y7 | 005 L10 | "DIABIL-2, DF-IL2 — Tregs expand but so do other cells" | Primary refs |
| Y8 | 006 L7 | "VX-264 … DISCONTINUED March 2025" | Vertex press release or trial registry NCT |
| Y9 | 007 L11–18 | "NEJM, August 2025 … UP421 … 42-year-old man, 30+ yrs T1DM, 17 injections" | NEJM DOI / Sana press release / NCT number (currently claimed but not linked) |
| Y10 | 008 L6–13 | "Cell, 2024 … CiPSCs … 10 weeks insulin-independent" | Primary citation Wu et al. *Cell* 2024 — which issue? PMID? |
| Y11 | 010 L7 | "LNP-CTB-GADIII (J Controlled Release, 2024): NOD mice T1DM 67% → 13%, p=0.002" | DOI / PMID + number of mice per arm |

## GREEN findings (positives, for calibration)

- **G1** attempt_007_crispr_hypoimmune — Sana UP421 claim cites journal
  (NEJM), issue (August 2025), patient characteristics (42 yo, 30+ yrs
  T1DM), intervention (17 intramuscular injections), primary outcome
  (6+ mo survival, glucose-dependent C-peptide, evaded auto- AND
  allo-). This is close to math-standard — one more step (NEJM DOI)
  would be GREEN-with-cert.
- **G2** attempt_008_autologous_ipsc — Deng CiPSC claim cites journal
  (*Cell*), year (2024), method (chemical reprogramming, no Yamanaka
  factors), site (rectus sheath), specific outcomes (HbA1c ~5%, TIR
  >98%, insulin-independent by 10 weeks). Materially specific and
  verifiable.
- **G3** attempt_002_islet_transplant — Shapiro NEJM 2000 with 7/7
  patients insulin-independent at 1 year is a canonical citation; the
  follow-up revision (50% at 5 yr) needs Y1 fix but the primary anchor
  is solid.
- **G4** attempt_010_mrna_tolerance — LNP-CTB-GADIII cites journal
  (*J Controlled Release*, 2024), mechanism (CTB → GM1 binding →
  tolerogenic APC uptake), quantified effect (67%→13%, p=0.002). Good.

## Recommended fixes (ordered)

1. **[P0] attempt_001**: replace the 72.2-month figure with the Herold
   2019 NEJM primary endpoint (48.4 vs 24.4 months) or cite a specific
   later follow-up paper that reports 72.2. Add PMID 31180194.
2. **[P0] attempt_004**: state DIAGNODE-2's primary-endpoint miss
   explicitly and cite the DIAGNODE-2 primary paper.
3. **[P1] Thread all PMIDs/DOIs**: one sweep across attempts 001–010
   adding one-line `[PMID: 31180194]` tags after each author-year-journal
   citation. Use the `papers/MANIFEST.md` as the index; cross-reference.
4. **[P2] attempt_002 Y2**: either cite OPTN figures or remove the
   "mathematically impossible to scale" phrasing and replace with a
   generic "supply-constrained" claim that doesn't hinge on exact numbers.
5. **[P2] attempt_003 Y4**: the $500K figure should be attributed
   (analyst report X) or softened to "estimated to be in the high
   six-figure range per patient based on Vertex's pricing precedents for
   similar cell therapies."
6. **[P3] attempt_005 Y6**: update "STIM" to "*Sci Transl Med* 2015" to
   avoid acronym ambiguity; add PMID 26606968.

## Non-audit observations (map features worth keeping)

- The 10-attempt arc maps the T1DM "two-problem" structure cleanly:
  attempts 001/005 attack the immune side with blunt tools (anti-CD3,
  polyclonal Tregs); attempts 002/003/006 attack the beta-cell side
  (donor islets, stem cells, devices); attempts 004/009/010 attempt
  antigen-specific tolerance (GAD-alum, inverse vaccines, mRNA tolerance);
  attempt 007 does the CRISPR-cloak workaround; attempt 008 discovers
  autologous may bypass both. The convergence — "gap is immune
  protection, either via tolerance (009/010) or cloaking (007)" — is a
  genuine standing-wave pattern and should not be softened by the audit.
- Maps Include Noise: all ten attempts, including the Phase 3 failures
  (DIABGAM, DIAGNODE-2 partial, VX-264 discontinued) are preserved as
  first-class attempts rather than collapsed to a summary. This matches
  the math/ standard and should be noted as a GREEN feature for the
  directory overall.

## Tag

095. First claim-backing audit pass on t1dm/. Attempts 001–010 are
mostly 🟡 YELLOW (correctly-identified trials, correct high-level
verdicts, but PMIDs/DOIs absent and 2 specific numbers need
verification). No RED-at-whole-attempt level — each attempt's
conclusion stands. Fixes listed in priority order. Next audit fire:
t1dm attempts 011–020.
