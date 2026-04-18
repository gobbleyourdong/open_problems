# Verified References — ME/CFS Corpus

> **Purpose**: central PMID-threaded reference list for the me_cfs
> subdir. Companion to `medical/dysbiosis/VERIFIED_REFS.md` and
> `medical/t1dm/VERIFIED_REFS.md`. Addresses YELLOW flags from
> AUDIT_LOG Fires 13 and 36.
>
> **Started**: 2026-04-18 Fire 84.

## Verified entries

### Brenu 2011 (cross-ref — in dysbiosis/VERIFIED_REFS.md)

See `medical/dysbiosis/VERIFIED_REFS.md` §"Brenu 2011" for the full
entry. PMID **21619669**, *J Transl Med* 9:81. NK/CD56bright
cytotoxicity reduction in CFS/ME. Primary citation for ME/CFS
NK-dysfunction biomarker panel.

---

### Naviaux 2016 (cross-ref — in dysbiosis/VERIFIED_REFS.md)

See `medical/dysbiosis/VERIFIED_REFS.md` §"Naviaux 2016" for the full
entry. PMID **27573827**, *PNAS* 113(37):E5472-5480. Metabolic
features of CFS, dauer-like hypometabolic state. Note 2017
correction PMID 28439011.

---

### IOM 2015 Report ✅ (CDC-referenced ME/CFS diagnostic criteria + prevalence)

**Institute of Medicine (US) Committee on the Diagnostic Criteria for
Myalgic Encephalomyelitis/Chronic Fatigue Syndrome.**
*Beyond Myalgic Encephalomyelitis/Chronic Fatigue Syndrome: Redefining
an Illness.*
Washington (DC): National Academies Press (US); 2015 Feb 10.
**PMID: 25695122**

**Use in corpus**: primary source for the **836,000–2.5M US
prevalence** figure cited in me_cfs/PROBLEM.md ("~2.5M Americans")
— **the 2.5M figure is the upper bound of the IOM range**, not a
point estimate. Also primary source for the SEID (Systemic Exertion
Intolerance Disease) naming + 3-required-symptoms diagnostic
framework currently used by CDC.

⚠️ **Note on me_cfs/PROBLEM.md**: the "2.5M" figure should be cited as
"836,000–2.5M per IOM 2015 report, PMID 25695122" with the range
made explicit. Currently the PROBLEM.md states only the upper bound
without range or source; this is a YELLOW citation-gap the R27
audit note at `medical/me_cfs/PROBLEM.md` already flagged.

**Cross-subdir**: me_cfs/ primary.

---

### Younger 2013 ✅ (LDN fibromyalgia RCT — **year correction from Fire 36 AUDIT_LOG**)

**Younger J, Noor N, McCue R, Mackey S.**
*Low-dose naltrexone for the treatment of fibromyalgia: findings of a
small, randomized, double-blind, placebo-controlled, counterbalanced,
crossover trial assessing daily pain levels.*
**Arthritis Rheum** 2013;65(2):529–538.
**PMID: 23359310**  **DOI: 10.1002/art.37734**

⚠️ **Year correction**: AUDIT_LOG Fire 36 Y-flag listed this as
"LDN Bolton/Younger 2018" — this is another **FM1a year-drift case**.
Correct citation is Younger **2013** (not 2018), and the first
author is Younger (not Bolton). The n=31 pilot RCT showed LDN at
4.5 mg/day produced 28.8% pain reduction vs 18.0% placebo (p=0.016).

**Use in corpus**: primary reference for LDN mechanism + preliminary
efficacy in fibromyalgia (used in me_cfs/THEWALL.md LDN section as
"Bolton/Younger 2018" — should be corrected to Younger 2013 PMID
23359310). Later ME/CFS-specific LDN work (Polo 2019, Cabanas 2021)
exists but this is the foundational RCT.

**Cross-subdir**: me_cfs/ primary; t1dm/ (LDN cross-disease
anti-inflammatory adjunct).

---

## Queue (next fires)

| Citation | Likely paper | Notes |
|----------|-------------|-------|
| GSE293840 | NCBI GEO dataset | Reference to public dataset, not a paper; needs accession-URL threading |
| MT-ND3, PRF1, STAT2 effect sizes | per-gene transcriptomic measurements | Likely from GSE293840 analysis scripts; needs local-file-based verification |
| CFS/ME DAMPs + TRPV1 | various | Pending |

## Audit history

- **2026-04-18 Fire 84**: Started file with 2 verified direct
  entries (IOM 2015, Younger 2013) + 2 cross-refs to dysbiosis
  VERIFIED_REFS (Brenu 2011, Naviaux 2016). **Year-drift correction**:
  AUDIT_LOG Fire 36 cited "Bolton/Younger 2018" for LDN but actual
  is Younger 2013 (5-year drift + author-drift). Another FM1a case
  validating the case study.
