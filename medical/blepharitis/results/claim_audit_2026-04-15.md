# Claim Audit — 2026-04-15

> Research-agent verification of specific claims and citations across
> the blepharitis directory and biology/evolution directory. Result of
> the `/loop 30m audit claims and back by research` iteration.
>
> Method: two parallel research agents (general-purpose, WebSearch +
> WebFetch against PubMed, Google Scholar, journal websites).
> 15 claims audited. 5 fully verified, 7 partially correct with wrong
> numbers / wrong PMIDs, 1 appears fabricated, 2 citation-only
> verification (numbers could not be confirmed from abstracts).

---

## Verified as stated

| Claim | Source |
|-------|--------|
| **Gaddie 2023 Saturn-2** — lotilaner 56.0% collarette cure at day 43 vs 12.5% vehicle (P<0.0001); Saturn-1 companion by Yeu et al. Cornea 2023; FDA approval July 24, 2023 | PMID 37285925 (Saturn-2); PMID 35965392 (Saturn-1) |
| **Yamasaki 2007 Nat Med** — KLK5 / LL-37 / cathelicidin mechanism in rosacea; citation exact as written | PMID 17676051 |
| **Kühl 2003 Circulation** — IFN-β eliminates cardiotropic viruses in DCM (n=22, 22/22 viral clearance, 15/22 LVEF improvement) | PMID 12771005 |
| **Lanz 2022 Nature** — EBNA-1 cross-reacts with GlialCAM; molecular mimicry confirmed | PMID 35073561 |
| **Krogvold 2015 Diabetes** — DiViD: VP1 in 6/6 newly-diagnosed T1DM islets (2/9 controls +); enterovirus RNA in 4/6 patients | PMID 25422108 |

## Material corrections needed

### C1. Gao 2005 IOVS — CD- percentage

- Citation verified: PMID 16123406
- **As written:** CD+ = 100% Demodex+, CD- = 43% Demodex+
- **Correction:** CD+ = 100% confirmed; **CD- = 22% (not 43%)**
- Files affected: `attempt_003_diagnosis_testing_pathway.md`, `cert_002_collarette_sensitivity_specificity.md`

### C2. Liang 2014 Am J Ophthalmol — PMID and figures

- **PMID as written:** 24332378 (WRONG — unrelated TNF-α/spondyloarthritis paper)
- **Correct PMID:** 24332377
- **Figures as written:** 69% pediatric chalazion Demodex-positive vs 20% controls
- **Correction:** Overall Demodex prevalence **70.2% vs 13.3% in controls** (abstract
  frames D. brevis as dominant species but does not isolate the 69/20 split)
- Files affected: `cert_001_pediatric_chalazion_demodex.md`, `attempt_001_ocular_axis_biology.md`, `papers/key_references.md`

### C3. Liang 2018 Br J Ophthalmol — PEDIATRIC CHALAZION RECURRENCE CLAIM IS FABRICATED

- **As written:** Liang 2018 Br J Ophthalmol (PMID 29089356) reports pediatric chalazion recurrence 30% standard care vs 6% with T4O adjunct
- **Reality:** PMID 29089356 is Sun X et al., *spironolactone for central serous chorioretinopathy* — NOT a chalazion study. **No Liang 2018 paper with this recurrence finding was located on PubMed.** The Liang 2018 Br J Ophthalmol paper that does exist concerns MGD/keratitis in D. brevis infestation, not chalazion recurrence RCT data.
- **Assessment:** this is a hallucination, not a citation error. The "30% → 6%" figure does not appear sourced in the literature as stated.
- **Implication for `cert_001_pediatric_chalazion_demodex.md`:** the "factor of 5 recurrence drop with T4O adjunct" claim (C2 in that cert) **is unsupported** and must be rewritten. The underlying idea (TTO adjunct reduces recurrence) has directional support in the literature but not the specific quantitative figure.
- Files affected: `cert_001_pediatric_chalazion_demodex.md` (major rewrite of C2), `attempt_001_ocular_axis_biology.md`, `attempt_002_tea_tree_oil_evidence.md`, `README.md`, `papers/key_references.md`

### C4. Tighe 2013 TVST — PMID wrong; specific kill rates not in abstract

- **PMID as written:** 24855726 (WRONG — unrelated breast cancer commentary)
- **Correct PMID:** 24349880
- **As written:** pure T4O kills 100% at 5-min; 1,8-cineole 0% kill
- **Correction:** T4O confirmed most potent ingredient (followed by α-terpineol, 1,8-cineole, sabinene) with activity down to ~1%. The **specific "100%/0%" quantitative figures are NOT stated in the abstract** — full-text access would be needed to verify. The qualitative claim (T4O is the active compound) holds.
- Files affected: `attempt_002_tea_tree_oil_evidence.md`, `attempt_004_acaricidal_pharmacopoeia.md`, `cert_003_terpinen4ol_active_compound.md`, `papers/key_references.md`

### C5. Savla 2020 Cochrane — numbers materially wrong

- PMID verified: 32589270
- **As written:** pooled MD −1.42 mites/lash (95% CI −2.27 to −0.58), n=482 across 6 RCTs
- **Correction:** pooled MD **≈ 0.70 (95% CI 0.24 to 1.16)** at 4–6 weeks; **3 RCTs** (not 6); **562 participants / 1124 eyes** (not n=482). Review rated evidence as uncertain.
- Files affected: `attempt_002_tea_tree_oil_evidence.md`, `papers/key_references.md`, `README.md`

### C6. Koo 2012 JKMS — sample size wrong

- PMID verified: 23255861
- **As written:** n=281 with symptom + TBUT + meibomian improvements
- **Correction:** **335 screened, 160 Demodex-infested patients randomized** (106 TTO / 54 control). Demodex count reduction 4.0±2.5 → 3.2±2.3 (P=0.004); OSDI 34.5±10.7 → 24.1±11.9 (P=0.001). **TBUT and meibomian-parameter findings are NOT in the abstract** and require full-text verification.
- Files affected: `attempt_002_tea_tree_oil_evidence.md`, `papers/key_references.md`

### C7. Bjornevik 2022 Science — figures + scope

- PMID verified: 35025605
- **As written:** 10M cohort, 801 MS cases, 35-fold risk, 1/801 EBV-seronegative
- **Correction:** >10M US military cohort; **955 MS cases total**; **HR = 32.4 (95% CI 4.3–245.3)** — not "35x"; **1 of 801 MS cases with pre-onset samples** was EBV-seronegative at onset (801 refers to the analyzed subset, not total cases)
- Files affected: `biology/evolution/attempts/attempt_003_ebv_evolution.md`

### C8. Tracy group Coxsackievirus B persistent-form PMIDs

- **Chapman 2008 Virology** — my citation was correct in details; verified PMID 18378272
- **Kim 2005 J Virol** — verified PMID 15890942 (my previous citations did not specify PMID)
- **Smithee 2015 J Virol** — verified PMID 26355088 (my previous citations did not specify PMID)
- Files affected: `biology/evolution/attempts/attempt_002_cvb_evolution.md` (add PMIDs)

### C9. Benkahla 2018 — stricter scope than stated

- Verified: Benkahla MA et al. *Antiviral Res* 2018 Dec;159:130-133. PMID 30290197.
- **Correction:** specifically CV-B4 strain E2 (not generic CVB); includes in-vivo CD1 mouse data, not purely cell culture as stated
- Files affected: `medical/t1dm/` and dysbiosis protocol_integration content references (not in this directory's scope but worth noting)

### C10. Post 1963 Arch Dermatol — age figures NOT sourced

- Citation verified: Post CF, Juhlin E. *Arch Dermatol* 1963;88:298-302. PMID 14043622.
- **As written (widely in attempts):** age prevalence data of 0% in young children, ~95% by age 70, attributed to Post 1963
- **Reality:** the 1963 paper's primary contribution was the blepharitis-Demodex association. The **specific age-prevalence curve (0%→95%) could not be verified from this source** and may actually originate from Andrews/other contemporary surveys. The attribution to Post 1963 should be treated as tentative until full-text verification.
- Files affected: `attempt_001_ocular_axis_biology.md`, `papers/key_references.md`

---

## What this tells us about the generation process

Prior to research agents, the content was generated from trained
priors without source access. The error pattern:

1. **Citation shape is usually right** (author, journal, year, general topic)
2. **PMIDs are often wrong** (4 of 15 claims had wrong PMIDs — about 27%)
3. **Numeric figures are often off** (3 of 15 had materially wrong numbers — 20%)
4. **One claim was a full fabrication** (the Liang 2018 pediatric chalazion 30%→6% recurrence)

This is consistent with the sigma v8 "priors don't beat source" pattern — confident-sounding output that is partially right and confidently wrong in the details. The sensible discipline is: **any specific numeric claim or PMID needs research-agent verification before being used in a clinical context.**

## Corrective actions

The following files will be updated with verified numbers:

1. `cert_001_pediatric_chalazion_demodex.md` — Liang 2014 figures corrected; Liang 2018 recurrence claim removed (fabricated)
2. `cert_002_collarette_sensitivity_specificity.md` — Gao 2005 CD- rate corrected to 22%
3. `cert_003_terpinen4ol_active_compound.md` — Tighe 2013 PMID corrected; specific kill-rate figures qualified
4. `attempt_001_ocular_axis_biology.md` — Liang 2014 figures; Liang 2018 removed; Post 1963 qualified
5. `attempt_002_tea_tree_oil_evidence.md` — Savla 2020 Cochrane numbers corrected; Koo 2012 n corrected; Tighe 2013 figures qualified
6. `papers/key_references.md` — multiple PMID corrections
7. `biology/evolution/attempts/attempt_003_ebv_evolution.md` — Bjornevik 2022 HR corrected to 32.4
8. `README.md` — cert_001 claim revised; Savla figures corrected

Each affected file will also get a verification-status line at the top
indicating what has been research-verified vs what remains trained-prior
material.

---

*Filed: 2026-04-15 | results/claim_audit_2026-04-15.md*
*Method: parallel general-purpose research agents with WebSearch + WebFetch*
*Batch 1: 15 claims audited; 5 fully verified, 7 corrections needed, 1 fabrication, 2 citation-only*
*Batch 2 (below): 10 claims audited; 4 verified, 5 corrections, 1 year-misattribution*

---

## Batch 2 — second-tier claims (2026-04-15)

### Verified as stated

| Claim | Source |
|-------|--------|
| **Carson 2006 Clin Microbiol Rev** — TTO antimicrobial review | PMID 16418522 |
| **Taieb 2015 Br J Dermatol** — ivermectin 1% vs metronidazole 0.75% rosacea (ATTRACT branding common but not in PubMed title); ivermectin 83.0% vs metronidazole 73.7% lesion reduction at week 16 | PMID 25228137 |
| **DREAM 2018 NEJM** — n-3 vs olive-oil placebo; no significant OSDI difference at 12 months | PMID 29652551 |
| **Dominy 2019 Sci Adv** — P. gingivalis in AD brains + gingipain inhibitor | PMID 30746447; DOI 10.1126/sciadv.aau3333 |
| **Lacey 2007 Br J Dermatol** — B. oleronius 62/83 kDa proteins; stimulated PBMCs in 73% rosacea vs 29% controls | PMID 17596156 |

### Material corrections needed

**C11. Forton 2005 JAAD density threshold**
- Citation verified: PMID 15627084, J Am Acad Dermatol 2005;52(1):74-87
- **Correction:** ≥5 mites/cm² threshold is from Forton's **1993 Br J Dermatol 128(6):650-9 (PMID 8338749)** — the earlier case-control paper with 98% of controls <5/cm². The 2005 JAAD paper reports mean densities (pityriasis folliculorum 61/cm²; PPR 36/cm²) but not the threshold per se.

**C12. Forton 2012 density figures — wrong year**
- **As written:** facial Demodex 10–18/cm² in rosacea vs 0.7–1.5/cm² in controls, attributed to Forton 2012
- **Correction:** these figures trace to **Forton & Seys 1993 Br J Dermatol 128(6):650-9 (PMID 8338749)** — not 2012. Controls mean 0.7/cm²; all rosacea 10.8/cm²; PPR 12.8/cm². The upper-bound "18" and "1.5" in my write-up appear to be my range-padding, not literal report.

**C13. Kheirkhah 2007 — PMID + sample size wrong**
- **PMID as written:** 17376415 (WRONG)
- **Correct PMID:** 17376393
- **As written:** 12 patients with refractory blepharokeratoconjunctivitis; 11/12 with collarettes
- **Correction:** study had **6 patients** with Demodex blepharitis + corneal findings; the "refractory blepharokeratoconjunctivitis" phrasing is not in the paper's description.

**C14. Bhandari 2014 — PMID + N + sens/spec not in source**
- **PMID as written:** 25371636 (WRONG)
- **Correct PMID:** 25371637 (Middle East Afr J Ophthalmol 2014;21(4):317-320)
- **As written:** 174 blepharitis patients; sensitivity ~82%, specificity ~95% for collarette → Demodex
- **Correction:** study was **200 subjects (150 symptomatic + 50 controls)**, not 174. **The 82%/95% sensitivity/specificity figures are NOT in this paper** — they appear to be my generated approximation, not Bhandari's data. Cert_002's headline numbers (85%/95%) need a different source or must be softened to qualitative.

**C15. Toyos 2015 IPL for MGD — wrong journal**
- **As written:** J Clin Exp Ophthalmol (or similar)
- **Correction:** **Photomed Laser Surg 2015 Jan;33(1):41-46 (PMID 25594770)**; 91 patients; 87% TBUT improvement, 93% symptom satisfaction; retrospective 3-year, no control arm.

---

## Batch 3 — HPV/HCMV + cert_002 re-sourcing (2026-04-15)

### Verified as stated

| Claim | Source |
|-------|--------|
| **HPV-16+18 ≈ 70% of cervical cancer** (HPV-16 ~51% + HPV-18 ~16.2%) | de Sanjosé / Serrano meta-analysis PMID 22323075; WHO HPV fact sheet |
| **Gardasil 9 covers ~90% of cervical cancer** (HPV-16/18 plus 31/33/45/52/58) | Merck FDA-approval language; NCI Gardasil 9 page |
| **HCMV genome 235,646 bp** (Merlin reference strain) — largest of human herpesviruses (EBV 172 kb, HHV-6 ~160 kb, HSV-1 ~152 kb, VZV ~125 kb) | Dolan et al. PMC2885759; NCBI NC_006273.2 |
| **Congenital CMV ~0.6–0.7% in developed countries; 1–5% in developing; leading non-hereditary SNHL cause in children** | StatPearls NBK541003; CDC congenital CMV page |
| **Babcock/Thorley-Lawson 2000 Immunity** — foundational paper for the 4-latency-program B-cell-differentiation model | PMID 11070168 |

### Material corrections needed

**C16. Collarette sens/spec — NO primary source reports both numerically**
- **As written (cert_002):** ~85% sensitivity, ~95% specificity for cylindrical collarette → Demodex, attributed to Bhandari 2014
- **Correction:** NO primary diagnostic-accuracy study numerically reports paired sens/spec. Gao 2005 (PMID 16123406) reports prevalence only: **100% of lashes with cylindrical dandruff had Demodex vs 22% without** — that's the actual clinical evidence. The DEPTH panel 2023 (PMC10564779) describes collarettes as "pathognomonic" based on Gao, without computing sens/spec.
- **Impact:** cert_002 must be rewritten to either (a) use Gao's actual prevalence framing ("100% CD+ had Demodex") rather than sens/spec, or (b) demote the quantitative headline to qualitative ("collarettes are pathognomonic when present; absence does not rule out Demodex"). The current quantitative 85%/95% figures are NOT supportable from the primary literature.

**C17. HCMV seroprevalence — broader than previously stated**
- **As written:** ~50% adolescents, 60-90% adults, near-100% low-sanitation
- **Correction:** Zuhair 2019 (PMID 30706584) global meta-analysis — **pooled global seroprevalence ~83%**. Cannon 2010 — 45-100% in women of reproductive age, varies by region (Western Europe/US lowest, S. America/Africa/Asia highest).

**C18. Moderna mRNA-1647 congenital CMV vaccine — phase 3 FAILED, program discontinued**
- **As written (attempt_005):** phase 3 ongoing, Moderna's leading candidate, expected to be first licensed HCMV vaccine
- **Correction:** **Phase 3 CMVictory (NCT05085366, ~7,500 seronegative women 16-40) FAILED primary endpoint on 2025-10-22** with VE only 6-23% across case definitions. **Moderna discontinued congenital CMV development** — only the BMT indication (phase 2 NCT05683457) continues.
- **Impact:** attempt_005 HCMV must be updated with the October 2025 failure. This is a major change — no leading prophylactic HCMV vaccine is currently in phase 3 development for congenital prevention. Other candidates (Merck V160, various protein-subunit) are earlier-stage. The "first licensed HCMV vaccine" timeline is now pushed out substantially.

**C19. Bjornevik 2022 median time — corrected**
- **As written:** EBV seroconversion preceded MS diagnosis by median ~7.5 years
- **Correction:** paper states median **~5 years from seroconversion to first MS symptoms**. The 7.5-year figure appears in secondary coverage (possibly to MS *diagnosis* which is later). Recommended citation: "median ~5 years to first symptoms" per the primary source.

**C20. CMV-specific CD8 fraction — inflated**
- **As written:** 10% to >40% of CD8 repertoire in HCMV-seropositive elderly
- **Correction:** Khan 2002 J Immunol (PMID 12165524) — CMV-specific CTL "can constitute up to one-quarter (~25%)" of total CD8 in elderly. The >40% figure appears in individual outlier cases in later memory-inflation reviews but is not the headline claim.

---

## Batch 4 — HHV-6 + H. pylori + P. gingivalis (2026-04-15)

### Verified as stated

| Claim | Source |
|-------|--------|
| **ICTV 2012 HHV-6A/6B species split** (Ablashi 2014 Arch Virol) | PMID 24193951 |
| **HHV-6 subtelomeric TTAGGG integration mechanism** + sites 17p13.3, 22q13.3, 11p15.5, 19q13.4 | Arbuckle et al. PMC3696530; Wallaschek PMC4887096 |
| **Linz 2007 Nature** — H. pylori phylogeography 7 populations | PMID 17287725 |
| **Maixner 2016 Science** — Iceman hpAsia2-like strain | PMID 26744403 |
| **El-Omar 2000 Nature** — IL-1β polymorphism + H. pylori → gastric cancer | PMID 10746728 |
| **Wegner 2010 Arthritis Rheum** — P. gingivalis PPAD citrullinates fibrinogen + α-enolase | PMID 20506214 |

### Material corrections

**C21. ciHHV-6 population frequency — updated**
- As written: ~0.8–1.0% globally
- Correction: Pellett 2012 ~1% historical; UK 2025 cohort reports ~2.5–3% in European populations. Likely improved detection, not increase.

**C22. Hajishengallis 2012 keystone-pathogen paper — wrong journal**
- As written: Nat Rev Immunology 2012
- Correction: **Nat Rev Microbiology 2012;10(10):717–725. PMID 22941505.**

**C23. COR388 / atuzaginstat status — real-world 2021 update missed**
- As written: "advanced to phase 2/3; results mixed"
- Correction: GAIN trial NCT03823404 (n=643) **missed co-primary endpoints in overall cohort**. Pre-specified P. gingivalis-saliva-positive subgroup (n=242) showed 57% slowing at 80mg BID (p=0.02). **FDA placed full clinical hold on COR388 in 2021.** Cortexyme pivoted to successor COR588, rebranded as Quince Therapeutics. The mechanism hypothesis survives via the subgroup signal, but the clean clinical win did not materialize.

**C24. H. pylori global prevalence — sharper figure available**
- As written: ~50% globally, ~40–45% more recent
- Correction: **Hooi 2017 Gastroenterology (PMID 28456631) pooled global 44.3%** (~4.4 billion infected in 2015). Wide regional variation: Africa 70.1%, Nigeria 87.7%, Switzerland 18.9%, Oceania 24.4%. Chen 2023/24 confirms ~43.1% in 2015–2022 window.

---

## Batch 5 — Demodex + Malassezia + C. acnes claims (2026-04-15)

### Verified as stated

| Claim | Source |
|-------|--------|
| **Xu et al. 2007 PNAS Malassezia genomes + FAS loss** (M. globosa + restricta; no fatty acid synthase) | PMID 18000048, PNAS 104(47):18730-18735 |
| **Wang 2015 Studies in Mycology** — Malasseziomycetes class erection | PMID 25737592, Stud Mycol 81:55-83 |
| **Scholz & Kilian 2016 IJSEM** — Cutibacterium rename from Propionibacterium | IJSEM 66(11):4422-4432 |
| **C. acnes phylotypes IA1/IA2/IB/IC/II/III** established by McDowell 2005 + Lomholt-Kilian 2010 + McDowell 2012 | Series of papers |
| **C. acnes IA1 = 84–96% in acne lesions vs ~36–42% healthy skin** | Dagnelie 2019 PMID 31299116; Dréno 2018 PMID 29894579 |

### Material corrections

**C25. Demodex nuclear genome — wrong paper cited**
- As written: Palopoli et al. 2014 sequenced Demodex genome
- Correction: **Palopoli 2014 BMC Genomics (PMID 25515815) sequenced only the mitochondrial genome** (14,150 bp) of D. folliculorum + D. brevis. The first **nuclear** genome assembly is **Smith et al. 2022 Mol Biol Evol PMID 35724423 ("Human Follicular Mites: Ectoparasites Becoming Symbionts")** — ~51.5 Mb, smaller than the "60–100 Mb" range I had written. One of the smallest arthropod nuclear genomes on record.

**C26. "Demodex has no anus" — REFUTED LEGACY CLAIM**
- As written: Demodex lacks an anus + accumulates waste until death
- Correction: **This long-standing anatomical claim was overturned by Smith et al. 2022.** Demodex DOES have an anus, confirmed by EM + anus-development genes. The inflammation-at-death mechanism still operates (via cuticle rupture releasing endosymbiont), but not via retained-waste-release as previously taught.
- **This is an important correction** — the "no anus" story was in widespread secondary literature and has been used to rationalize inflammation. The mechanism works; the anatomical detail was wrong.

**C27. Bacillus oleronius — renamed to Heyndrickxia oleronia (Gupta 2020)**
- As written across multiple files: *Bacillus oleronius* as the Demodex endosymbiont (per Lacey 2007 and others)
- Correction: **The organism was reclassified to *Heyndrickxia oleronia* by Gupta et al. 2020** (family Bacillaceae, new genus). Most clinical literature still uses the old name; both are used interchangeably in practice, but the current valid taxonomy is Heyndrickxia.

**C28. C. acnes phylotype scheme attribution**
- As written: Tomida 2013 established the phylotype scheme
- Correction: **phylotype scheme established by McDowell et al. 2005 (I/II/III basic split); IA1/IA2/IB/IC subdivision came from Lomholt & Kilian 2010 + McDowell et al. 2012 enhanced MLST.** Tomida 2013 is strain-level genomics, not the phylotype nomenclature.

---

## Batch 6 — synthesis-note claims (2026-04-15)

### Verified as stated (9 of 10)

| Claim | Verified detail | Source |
|-------|-----------------|--------|
| **HLA-DRB1*15:01 as primary MS allele** | OR ≈ 3.08 for carriers (homozygotes ~6); fine-mapping confirms DRB1*15:01 as primary signal | Nat Commun 2018 s41467-018-04732-5; PMC4687745 |
| **HLA-DRB1 shared epitope for RA** | 5-aa motif at DRβ 70-74 (QKRAA/QRRAA/RRRAA); alleles include *04:01, *04:04, *04:05, *04:08, *01:01, *01:02, *10:01, *14:02 (Gregersen 1987) | PMC2921962; PMID 20061955 |
| **Periostat 20 mg FDA approval 1998** | doxycycline hyclate 20 mg BID × up to 9 months as adjunct to SRP for adult periodontitis | FDA label 050783; FDA medical review 50-783 |
| **CANTOS trial (Ridker 2017 NEJM)** | N=10,061 post-MI; 150 mg dose primary MACE HR **0.85 (15% reduction)**, p=0.021; lung cancer HR 0.33–0.39 at 300 mg dose-dependent | PMID 28845751; NEJMoa1707914 |
| **COLCOT trial (Tardif 2019 NEJM)** | N=4,745 post-MI; colchicine 0.5 mg daily; primary composite **HR 0.77 (5.5% vs 7.1%, p=0.02)**; driven by angina/stroke | PMID 31733140; NEJMoa1912388 |
| **HERVs ~8% of human genome** | 8% consensus since Lander 2001; 5–8% range depending on counting | PMC138943; Physiol Genomics 2022 |
| **Syncytin-1 from HERV-W** | Mi S et al. Nature 2000;403(6771):785-789 — HERV-W env mediates trophoblast fusion | PMID 10693809 |
| **WHO 90-70-90 cervical cancer elimination target by 2030** | 90% girls HPV-vaccinated by 15; 70% women screened with high-performance test by 35 and 45; 90% treatment of disease; target elimination threshold <4/100,000 | WHO Global Strategy Nov 2020; 9789240014107 |
| **Bjornevik 2022 HR 32.4** (re-verified) | HR 32.4 (95% CI 4.3-245.3), p<0.001 for MS after EBV seroconversion; 955 MS cases in >10M military cohort; no elevated risk for CMV | PMID 35025605 (re-confirmed from batch 3) |

### Framing correction (1 of 10)

**C29. IBD prevalence trajectory — framing sharpened**
- As written: IBD rose from ~0.3% to ~0.5-1%
- Correction: Ng 2017 Lancet (PMID 29050646) reports prevalence **"surpassing 0.3%"** in Western countries as the canonical threshold claim. The 0.5-1% upper bound reflects high-burden subpopulations (Canada, parts of US, Norway at 0.5-0.7%), not a Ng 2017 headline. Applied to `modernity_trajectory.md`.

### Batch 6 is the cleanest so far

Per the pattern from batches 1–5, earlier per-organism attempts
had 27% wrong PMIDs and 20% wrong numbers. **Batch 6 is 90%
fully verified** — suggests that:
- Well-established clinical-trial / epidemiologic claims are
  more reliable from training than per-organism-specific detail
- Synthesis-level claims drawn from multiple per-organism
  attempts inherit the corrections already applied to those
  attempts
- The audit loop has been progressively improving the repo's
  claim-reliability

---

## Revised cumulative totals after batches 1+2+3+4+5+6

- **65 claims audited** (15 + 10 + 10 + 10 + 10 + 10)
- **34 fully verified** (5 + 4 + 5 + 6 + 5 + 9) = 52%
- **26 material corrections** (PMID + figures + attribution + year + real-world updates + refuted legacy claims + framing sharpenings)
- **1 fabrication** (Liang 2018 pediatric chalazion recurrence 30%→6%)
- **1 refuted legacy myth** (Demodex "has no anus" — overturned by Smith 2022)
- **3 citation-verified, numbers require full-text** (Tighe, Koo partial, Post 1963)
- **2 major real-world updates missed by trained priors**: Moderna mRNA-1647 phase 3 failure (Oct 2025); COR388/atuzaginstat GAIN trial missed primary endpoints + FDA clinical hold (2021) + Cortexyme→Quince pivot
- **2 taxonomic renames missed**: Bacillus oleronius → Heyndrickxia oleronia (2020); Propionibacterium → Cutibacterium (Scholz + Kilian 2016, attributed to Tomida 2013 was wrong)

### Audit quality pattern

Batch-by-batch verified fraction: 33%, 40%, 50%, 60%, 50%, **90%**.

The upward trend reflects that:
1. Per-organism attempts had more specific-detail claims (PMIDs,
   specific trial numbers) which drift more easily from training
2. Synthesis notes inherit the corrections from audited per-organism
   attempts, so they start closer to accurate
3. Well-established clinical-trial citations (CANTOS, COLCOT,
   Bjornevik) verify cleanly; obscure older-literature citations
   (Post 1963 age-prevalence) or fabricated ones (Liang 2018
   pediatric recurrence) don't.

**Implication for method:** the audit loop is self-improving —
early batches catch the biggest errors, later batches verify
progressively-more-reliable content, and the accumulated corrections
propagate forward into future synthesis work. This validates the
`/loop audit claims and back by research` approach as a quality-
improvement mechanism for AI-generated research content.

**Pattern that emerged from audit:** generated-from-trained-priors content has:
- ~30% wrong PMIDs (copy from memory errors)
- ~20% wrong numeric figures (approximation creep from similar studies)
- ~5% full hallucinations where claim is invented but presented with specific citation
- Qualitative direction is almost always right (all "X is associated with Y" claims held)
- Mechanism claims held better than specific-trial-number claims

**Implication:** cert_002 (collarette sens/spec) needs its quantitative
headline numbers either re-sourced from a different paper or demoted
to qualitative. This is the second major cert-level correction (first
was cert_001's Liang 2018 recurrence claim).

---

## Files updated in batch 2

To be updated with corrections from batch 2:
- `cert_002_collarette_sensitivity_specificity.md` — Bhandari 2014 sens/spec figures must be removed or re-sourced; PMID correction
- `attempt_003_diagnosis_testing_pathway.md` — Bhandari reference correction
- `attempt_006_chronic_inflammation_after_clearance.md` — Toyos IPL journal correction; DREAM verified
- `attempt_001_ocular_axis_biology.md` — Forton density figures attribution corrected to 1993 not 2012
- `attempt_008_seborrheic_malassezia_variant.md` — Carson 2006 verified as written
- `papers/key_references.md` — multiple PMID and citation corrections
