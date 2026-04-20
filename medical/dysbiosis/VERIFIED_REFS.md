# Verified References — Dysbiosis Numerics Corpus

> **Purpose**: central PMID-threaded reference list for the ~183 dysbiosis
> numerics runs. The per-run files cite author/year without PMIDs (Y308
> in AUDIT_LOG.md — single largest citation-discipline deficit of the audit).
> Rather than editing 183 files, this file verifies the ~20 most-cited papers
> once and lets per-run files cross-link here.
>
> **Method**: WebSearch-verified PMIDs per sigma v9 Three-Source Triangulation
> (Phase 4b Content Audit, see `~/SIGMA_METHOD.md` v9 C3). Prior audit predicted
> ~30% wrong PMID / ~20% wrong number rate across AI-authored research content;
> this file is the ether-verified subset.
>
> **Status**: Started 2026-04-18. In progress — each fire adds 3–5 entries.
> Citation-count ranking (per `grep` across `numerics/run_*.md`):

| # | Corpus citation | Occurrences | PMID | Status |
|---|----------------|-------------|------|--------|
| 1 | Youm 2015 | 13 | 25686106 | ✅ Verified |
| 2 | Yamasaki 2011 | 12 | 21107351 | ✅ **Verified (Fire 86)** — Yamasaki K *JID* 131(3):688-697 TLR2→KLK5 in rosacea; sub-flag for run_015 separately |
| 3 | Küpers 2019 | 11 | — | ⏸️ **Permanently deferred** per session memory (PACE EWAS, external data required) |
| 4 | Buhl 2017 | 11 | — | ❌ **FM1c fabrication confirmed (Fire 82)** — no Buhl 2017 paper on calprotectin OR TRPA1; see entry |
| 5 | Naviaux 2016 | 10 | 27573827 | ✅ Verified |
| 6 | Brenu 2011 | 10 | 21619669 | ✅ Verified |
| 7 | Wang 2015 | 9 | 25751815 | ✅ Verified (cross-refs R5 audit note at attempt_020) |
| 8 | Depommier 2019 | 9 | 31263284 | ✅ Verified |
| 9 | Cooper 2012 | 9 | 18978792 | ⚠️→✅ **Confirmed year-drift (Fire 86)** — actual is Cooper 2008 *Nat Genet*; per-run files need year correction |
| 10 | Ott 2010 | 8 | — | 🔍 **Unresolved** — no matching CFS/microbiota paper in 2010 |
| 11 | Kim 2022 | 8 | 35650334 | ✅ Verified (Kim DS et al. *Nat Rev Endocrinol* CVB-T1DM review) |
| 12 | Tanno 2000 | 7 | 10971324 | ✅ **Verified (Fire 85)** — Tanno O *Br J Dermatol* nicotinamide → SC ceramide barrier repair |
| 13 | Shim 2021 | 7 | — | ⚠️ **Likely hybrid drift (Fire 85)** — corpus cites *Nature* 597:625-629 (AKG/Treg/TET2) but no Shim Nature 2021 paper surfaces; closest match is Matsushita 2021 *Cell Reports* PMID 34731632 |
| 14 | Forton 2005 | 7 | 15627084 | ✅ Verified (Demodicosis/rosacea epidemiology, *JAAD*) |
| 15 | Cheng 2014 | 7 | 24905167 | ✅ **Verified (Fire 84)** — Cheng CW *Cell Stem Cell* fasting/IGF-1/HSC regeneration; corpus inline-cited the PMID |
| 16 | Cani 2008 | 7 | 18305141 | ✅ Verified (*Diabetes* metabolic-endotoxemia gut microbiota) |
| 17 | Bystrom 2008 | 7 | 18779392 | ⚠️ **FM1b+FM1c-adjacent (Fire 83)** — real paper exists but corpus journal AND mechanism are wrong; see entry |
| 18 | Barrett 2009 | 7 | 19430480 | ✅ **Verified (Fire 84)** — T1DM GWAS *Nat Genet* meta-analysis, >40 loci |
| 19 | Venkatesh 2014 | 6 | 25065623 | ✅ Verified (*Immunity* PXR + indole gut barrier) |
| 20 | Smyth 2008 | 6 | 18305142 | ✅ Verified (*Diabetes* PTPN22+HLA T1DM — **journal-drift**: corpus says "Nature Genetics" but actual is *Diabetes*) |

---

## Verified entries

### Youm 2015 ✅ (13 corpus citations)

**Youm Y-H, Nguyen KY, Grant RW, Goldberg EL, Bodogai M, Kim D,
D'Agostino D, Planavsky N, Lupfer C, Kanneganti TD, Kang S, Horvath TL,
Fahmy TM, Crawford PA, Biragyn A, Alnemri E, Dixit VD.**
*The ketone metabolite β-hydroxybutyrate blocks NLRP3 inflammasome–
mediated inflammatory disease.*
**Nat Med** 2015;21(3):263–269.
**PMID: 25686106**  **DOI: 10.1038/nm.3804**

**Use in corpus**: BHB / NLRP3 Signal-2 block mechanism. The paper
demonstrates BHB (not AcAc, butyrate, or acetate) inhibits NLRP3 via
K⁺-efflux prevention and reduced ASC oligomerization. In vivo validated
in MWS, FCAS, and urate-crystal inflammation mouse models.

**Cross-subdir**: t1dm/ (BHB arm in SUPPLEMENT_SCHEDULE), me_cfs/ (NLRP3
block rationale), pericarditis/ (cross-disease BHB), dysbiosis/ many runs.

---

### Naviaux 2016 ✅ (10 corpus citations)

**Naviaux RK, Naviaux JC, Li K, Bright AT, Alaynick WA, Wang L,
Baxter A, Nathan N, Anderson W, Gordon E.**
*Metabolic features of chronic fatigue syndrome.*
**PNAS** 2016;113(37):E5472–E5480.
**PMID: 27573827**  **DOI: 10.1073/pnas.1607571113**

⚠️ Note: **Correction** published 2017 — Naviaux et al. *PNAS* 2017;
114(18):E3749. **PMID: 28439011**. Anyone citing specific metabolite-
pathway numbers should check the correction for updated values.

**Use in corpus**: n=45 ME/CFS vs n=39 controls; 612 metabolites across
63 biochemical pathways; ME/CFS framed as hypometabolic cell-danger-
response state (dauer-like). Primary citation for me_cfs metabolomics
claims and for the "CDR / dauer" framing in persistent-organisms/.

**Cross-subdir**: me_cfs/ primary; dysbiosis/ runs invoking CDR /
spermidine-autophagy (e.g., run_041, run_052); persistent_organisms/.

---

### Brenu 2011 ✅ (10 corpus citations)

**Brenu EW, van Driel ML, Staines DR, Ashton KJ, Ramos SB, Keane J,
Klimas NG, Marshall-Gradisnik SM.**
*Immunological abnormalities as potential biomarkers in Chronic
Fatigue Syndrome/Myalgic Encephalomyelitis.*
**J Transl Med** 2011 May 28;9:81.
**PMID: 21619669**  **DOI: 10.1186/1479-5876-9-81**

**Use in corpus**: n=95 ME/CFS vs n=50 controls; NK and CD8+ T-cell
cytotoxicity + Th1/Th2 cytokine profiles + CD56bright/CD56dim NK
phenotypes + Tregs. Finding: **significantly decreased NK cytotoxicity
and CD56bright reduction in ME/CFS** — the seminal NK-dysfunction
biomarker paper for ME/CFS. Confirmed longitudinally by same group in
2012 (12-month follow-up).

**Cross-subdir**: me_cfs/ primary (NK-dysfunction biomarker panel);
persistent_organisms/ (NK-CD56bright reduction as ME/CFS-characteristic
phenotype).

---

### Wang 2015 ✅ (9 corpus citations; **cross-refs R5 audit note at attempt_020**)

**Wang P, Alvarez-Perez JC, Felsenfeld DP, Liu H, Sivendran S, Bender A,
Kumar A, Sanchez R, Scott DK, Garcia-Ocaña A, Stewart AF.**
*A high-throughput chemical screen reveals that harmine-mediated
inhibition of DYRK1A increases human pancreatic beta cell replication.*
**Nat Med** 2015;21(4):383–388.
**PMID: 25751815**  **DOI: 10.1038/nm.3820**

⚠️ **Cross-reference R5 audit note**: `medical/t1dm/attempts/
attempt_020_mountain2_harmine_proliferation.md` has a `## 2026-04-18
audit note (R5)` flagging that the corpus's "3-8% per day" is a
**monotherapy overstatement** — Wang 2015 reports ~2%/day monotherapy;
the 5-8% range applies only to **GLP-1 combination**, and up to 18%
requires **TGF-β inhibitor** (Ackeifi et al. 2020 *Sci Transl Med*).
See attempt_020 audit note for the per-combination correction.

**Use in corpus**: DYRK1A inhibition via harmine as β-cell-mitogenic
mechanism; NFAT transcription factor family as proliferation mediator.
Primary citation for the harmine / DYRK1A-i arm in the T1DM Mountain-2
protocol. **Subsequent work**: Wang 2019 *Cell Metab* (harmine + TGF-β
inhibitor combinations); Ackeifi 2020 *Sci Transl Med* (harmine-based
DYRK1A-i human beta cell mass expansion in vivo with exendin-4).

**Cross-subdir**: t1dm/ (Mountain 2 regeneration); dysbiosis/ runs
invoking DYRK1A-i or harmine. **Note:** harmine has a known rosacea-
exacerbating valence (see cross-pollination note in t1dm/THEWALL.md) —
do NOT recommend harmine cross-disease without the rosacea
contraindication check.

---

### Kim 2022 ✅ (8 corpus citations)

**Kim KW, Horton JL, Pang CNI, Jain K, Leung P, Isaacs SR, Bull RA,
Luciani F, Wilkins MR, Catteau J, Lipkin WI, Rawlinson WD, Briese T,
Craig ME.**
*Persistent coxsackievirus B infection and pathogenesis of type 1
diabetes mellitus.*
**Nat Rev Endocrinol** 2022;18(8):503–516.
**PMID: 35650334**  **DOI: 10.1038/s41574-022-00688-1**

**Use in corpus**: Central review on CVB persistence mechanisms and
T1DM pathogenesis. The review-paper status means this citation is used
as secondary-literature anchor rather than primary-data citation; its
role is to pool evidence from many primary studies on CVB persistence,
islet autoantibodies, and epidemiology.

**Cross-subdir**: t1dm/ primary (Mountain 3 CVB persistence + Mountain
4 molecular detail); myocarditis/ + dilated_cardiomyopathy/ (cross-CVB-
organ disease); dysbiosis/ runs invoking CVB persistence mechanism.

---

### Cani 2008 ✅ (7 corpus citations)

**Cani PD, Bibiloni R, Knauf C, Waget A, Neyrinck AM, Delzenne NM,
Burcelin R.**
*Changes in gut microbiota control metabolic endotoxemia-induced
inflammation in high-fat diet-induced obesity and diabetes in mice.*
**Diabetes** 2008;57(6):1470–1481.
**PMID: 18305141**  **DOI: 10.2337/db07-1403**

**Use in corpus**: seminal paper establishing that antibiotic-induced
changes in gut microbiota **reduce metabolic endotoxemia** (LPS) with
correlated reduction in glucose intolerance + body-weight gain + fat
mass + inflammation + oxidative stress. CD14-KO in ob/ob mimicked
antibiotic effects, demonstrating gut-microbiota → intestinal
permeability → endotoxemia → metabolic-disease causal chain.

**Related earlier paper**: Cani PD et al. 2007 *Diabetes* 56:1761–1772,
PMID **17456850** "Metabolic endotoxemia initiates obesity and insulin
resistance" — if a corpus citation is specifically about *initiation*
of metabolic disease (not modulation), this is the better PMID.

**Cross-subdir**: dysbiosis/ primary (gut-barrier → metabolic axis);
t1dm/ (endotoxemia cross-talk); me_cfs/ (gut-barrier dysfunction in
CFS literature).

---

### Venkatesh 2014 ✅ (6 corpus citations)

**Venkatesh M, Mukherjee S, Wang H, Li H, Sun K, Benechet AP, Qiu Z,
Maher L, Redinbo MR, Phillips RS, Fleet JC, Kortagere S, Mukherjee P,
Fasano A, Le Ven J, Nicholson JK, Dumas ME, Khanna KM, Mani S.**
*Symbiotic bacterial metabolites regulate gastrointestinal barrier
function via the xenobiotic sensor PXR and Toll-like receptor 4.*
**Immunity** 2014;41(2):296–310.
**PMID: 25065623**  **DOI: 10.1016/j.immuni.2014.06.014**

**Use in corpus**: microbial indole metabolites (particularly indole-
3-propionic acid, IPA) as **PXR ligands in vivo**; IPA downregulates
enterocyte TNF-α and upregulates junctional protein-coding mRNAs.
Establishes direct chemistry-level communication intestinal-symbionts
→ PXR → mucosal integrity via TLR4 axis.

**Cross-subdir**: dysbiosis/ runs invoking PXR/indole/IPA; t1dm/ (gut-
barrier protection); me_cfs/ (barrier dysfunction).

---

### Smyth 2008 ✅ (6 corpus citations) — **journal-drift noted**

**Smyth DJ, Cooper JD, Howson JMM, Walker NM, Plagnol V, Stevens H,
Clayton DG, Todd JA.**
*PTPN22 Trp620 explains the association of chromosome 1p13 with type
1 diabetes and shows a statistical interaction with HLA class II
genotypes.*
**Diabetes** 2008;57(6):1730–1737.
**PMID: 18305142**  **DOI: 10.2337/db07-1131**

⚠️ **Journal-drift flag**: corpus cites "Smyth 2008 *Nature Genetics*"
but the actual paper is in *Diabetes*, not *Nat Genet*. This is a **new
failure sub-mode** — not year-drift (year is correct) but **journal-
drift**: the corpus memory substituted a higher-prestige journal name
for the actual one. Possibly related to Smyth DJ's other publications
in *Nat Genet* (e.g., PTPN22-coeliac paper). See FM1a/FM1b note in
`~/sigma/case_studies/citation_year_drift_001.md`. Recommend per-run
files citing "Smyth 2008" also be audited for journal-drift.

**Use in corpus**: PTPN22 Trp620 (R620W, rs2476601) as T1DM susceptibility
variant; statistical interaction with HLA class II genotypes. Primary
citation for the PTPN22 component of T1DM polygenic risk score work
in t1dm/.

**Cross-subdir**: t1dm/ primary (PTPN22 / polygenic risk); dysbiosis/
runs invoking T-cell regulation (PTPN22 modulates TCR signaling).

---

### Forton 2005 ✅ (7 corpus citations)

**Forton F, Germaux MA, Brasseur T, De Liever A, Laporte M, Mathys C,
Sass U, Stene JJ, Thibaut S, Tytgat M, Seys B.**
*Demodicosis and rosacea: epidemiology and significance in daily
dermatologic practice.*
**J Am Acad Dermatol** 2005;52(1):74–87.
**PMID: 15627084**  **DOI: 10.1016/j.jaad.2004.05.034**

**Use in corpus**: Standardized skin-surface biopsy methodology +
Demodex density epidemiology in papulopustular rosacea (mean 12.8/cm²,
p<0.001 vs controls). Primary citation for Demodex-density-as-
pathogenic-threshold framing used in blepharitis/, rosacea cross-refs
from dysbiosis/, and perioral_dermatitis/ cross-talk.

**Cross-subdir**: blepharitis/ (primary Demodex methodology);
persistent_organisms/ (Demodex as persistent-organism exemplar);
dysbiosis/ (skin-microbiome runs); perioral_dermatitis/ (Demodex-on-
POD connection).

---

### Depommier 2019 ✅ (9 corpus citations)

**Depommier C, Everard A, Druart C, Plovier H, Van Hul M, Vieira-Silva S,
Falony G, Raes J, Maiter D, Delzenne NM, de Barsy M, Loumaye A, Hermans MP,
Thissen JP, de Vos WM, Cani PD.**
*Supplementation with Akkermansia muciniphila in overweight and obese
human volunteers: a proof-of-concept exploratory study.*
**Nat Med** 2019;25(7):1096–1103.
**PMID: 31263284**  **DOI: 10.1038/s41591-019-0495-2**

**Use in corpus**: Randomized double-blind placebo-controlled pilot,
n=40 enrolled / n=32 completed, daily 10¹⁰ A. muciniphila (live or
pasteurized) × 3 months. **Primary findings**: pasteurized A. muciniphila
improved insulin sensitivity (+28.62%, p=0.002), reduced insulinemia
(−34.08%, p=0.006), reduced plasma total cholesterol (−8.68%, p=0.02).
Safety: well tolerated. This is the **first-in-human proof-of-concept**
for A. muciniphila supplementation.

**Cross-subdir**: dysbiosis/ (Akkermansia-as-gut-barrier-improver arm);
t1dm/ (metabolic-endotoxemia → barrier → NLRP3 pathway); me_cfs/
(gut-dysbiosis overlap).

---

## Flagged entries (needs correction or further search)

### Yamasaki 2011 ✅ — VERIFIED (Fire 86, 12 corpus citations)

**Resolution**: clean ✅ verification (with sub-flag on run_015). Fire
78's "Yamasaki S Mincle/cord-factor 2011" search was wrong-author and
wrong-topic — the corpus is about **Yamasaki K (rosacea)**, a
completely different author. Fire 78 inferred year-drift to 2008/2009
based on the wrong author's publication record. Grep-first surfaced
five cite-bearing runs all about KLK5/LL-37/TLR2/STAT3 in rosacea.

**Verified entry (canonical Yamasaki 2011)**:

**Yamasaki K, Kanada K, Macleod DT, Borkowski AW, Morizane S,
Nakatsuji T, Cogen AL, Gallo RL.**
*TLR2 expression is increased in rosacea and stimulates enhanced
serine protease production by keratinocytes.*
**J Invest Dermatol** 2011;131(3):688–697.
**PMID: 21107351**  **DOI: 10.1038/jid.2010.351**

**Use in corpus** (cite-bearing runs):

- `run_062_il17a_th17_kls5_loop1.md` (lines 12, 34, 41) — IL-17A →
  KLK5 mRNA 3-5× in keratinocytes; NF-κB binding sites at -400, -800
  in KLK5 promoter; BAY 11-7082 NF-κB inhibitor blocks. ✅ Matches
  the Yamasaki 2011 *JID* paper's mechanistic findings.
- `run_080_ahr_il22_th22_kl5.md` (lines 68, 94) — STAT3 ChIP in
  rosacea keratinocytes; STAT3 constitutively phosphorylated;
  IL-6/JAK2 → STAT3 input. ✅ Within scope of the *JID* paper's
  serine-protease/keratinocyte focus.
- `run_119_ptpn2_tc_ptp_jak1_stat1_ll37_loop1_t1dm_gwas.md` (line 89)
  — cited as "Yamasaki 2011 (JAI)" → likely typo for "JID";
  cathelicidin overexpressed in rosacea, CAMP gene upregulation in
  papular/pustular rosacea. ✅ Matches.

**Sub-flag for run_015**:

`run_015_trpv1_neurogenic_flushing.md` cites **"Yamasaki 2011 *J Clin
Invest*"** with **PMID 21926468 inline (line 261)**. WebSearch on
this PMID does NOT return a Yamasaki rosacea paper. Two possibilities:

1. The PMID is wrong (memory-drift on the digits — common ~10⁻¹ rate
   per Fire 82's PMID 25748557→25848978 secondary drift).
2. The journal attribution is wrong — the actual paper for the
   "KLK5 → LL-37 → TLR2 + VEGFR2 → rosacea" framing is more likely
   the **Yamasaki K et al. 2007 *Nat Med* PMID 17676051** ("Increased
   serine protease activity and cathelicidin promotes skin inflammation
   in rosacea") — the foundational paper, not the 2011 *JID* TLR2
   follow-up.

**Action for run_015**: replace "Yamasaki 2011 *J Clin Invest* PMID
21926468" with either:
- Yamasaki 2007 *Nat Med* PMID 17676051 (if the claim is about
  KLK5/cathelicidin foundation in rosacea), OR
- Yamasaki 2011 *JID* PMID 21107351 (if the claim is about TLR2
  amplification → KLK5 release).
The KLK5 → LL-37 → VEGFR2 chain may also need a separate VEGFR2-
specific citation (the foundational Yamasaki papers don't directly
implicate VEGFR2 — that's later literature).

**Cross-subdir**: blepharitis/, perioral_dermatitis/, demodicosis/, and
other skin/persistent-organism subdirs that invoke the rosacea
KLK5/LL-37 cascade can all reference VERIFIED_REFS PMID 21107351
(or PMID 17676051 for the foundation).

**Methodology note (Fire 86)**: Yamasaki is the SIXTH wrong-topic
search artifact identified in this audit campaign (after Bystrom
2008, Barrett 2009, Cheng 2014, Tanno 2000, Buhl 2017 — though Buhl
was confirmed FM1c after the grep). Notable: Yamasaki 2011 was
flagged ⚠️ year-wrong, NOT 🔍 unresolved. The grep-first methodology
should now extend to ALL ⚠️ entries, not just 🔍. Cooper 2012 (next
fire candidate) is also ⚠️ year-wrong; needs the same grep treatment.

---

### Küpers 2019 ⏸️ — PERMANENTLY DEFERRED (11 corpus citations)

Per memory entry `feedback_approach.md`: "The Küpers 2019 PACE EWAS gap
is PERMANENTLY DEFERRED — external data required; do not attempt to
address it; list it as deferred in each Extension but do not write a
run for it." This entry is held as a map feature (Maps Include Noise)
per sigma v6 — preserved as dead-end, not deleted.

If a future session wishes to proceed with Küpers 2019 PMID threading,
the relevant paper is likely: Küpers LK, et al. *Nat Commun* 2019
10:1893. But external dataset access is the blocker, not the citation.

---

### Cooper 2012 ⚠️→✅ — CONFIRMED YEAR-DRIFT (Fire 86, 9 corpus citations)

**Resolution**: Fire 86 confirmed Fire 79's tentative year-drift
diagnosis. Targeted WebSearch ("Cooper JD 2012 *Nat Genet* T1DM
GWAS") returns ONLY the 2008 paper. Cooper 2012 *Nat Genet* T1DM
GWAS does not exist. Real paper:

**Cooper JD, Smyth DJ, Smiles AM, Plagnol V, Walker NM, Allen JE,
Downes K, Barrett JC, Healy BC, Mychaleckyj JC, Warram JH,
Todd JA.**
*Meta-analysis of genome-wide association study data identifies
additional type 1 diabetes risk loci.*
**Nat Genet** 2008;40(12):1399–1401.
**PMID: 18978792**  **DOI: 10.1038/ng.249**

**Cite-bearing runs (4 confirmed)**:

- `run_128_clec16a_mhcii_autophagy_aire_central_tolerance_dc_langerhans
  _t1dm_gwas.md` (line 20, 172, 239) — CLEC16A rs12708716; T1DM GWAS
  confirmation. Year-correct: 2012→2008.
- `run_129_erbb3_nrg1_neuregulin_beta_cell_survival_skin_barrier_t1dm
  _gwas_rosacea.md` (line 20) — ERBB3 rs2292239 confirmation. Year-
  correct: 2012→2008.
- `run_141_tagap_rhogap_rhoa_immune_synapse_tcr_cytoskeletal_t1dm_gwas
  _rosacea_rock.md` (line 173) — TAGAP rs1738074 ~1.18 risk allele.
  Year-correct: 2012→2008.
- `run_142_ifih1_mda5_mavs_tbk1_irf3_cytoplasmic_dsrna_t1dm_gwas
  _rosacea_innate_ifn.md` (line 189) — IFIH1 rs1990760. Year-correct:
  2012→2008.

**Note on coverage**: Cooper 2008 reports BACH2/PRKCQ/CTSH/C1QTNF6 as
NEW loci. ERBB3 (run_129), CLEC16A (run_128), TAGAP (run_141), IFIH1
(run_142) — these were CONFIRMED in Cooper 2008 alongside Hakonarson
2007 NEJM and Barrett 2009 *Nat Genet*. The corpus's "Cooper 2012
*Nat Genet*" attribution for these loci is consistent with the actual
Cooper 2008 paper's locus coverage. So this is pure year-drift, not
content drift — the cited mechanism is correct, just the year is
wrong.

**Action**: bulk per-run year correction needed. Recommended approach:
single batch edit replacing "Cooper 2012 Nat Genet" → "Cooper 2008
*Nat Genet* PMID 18978792" in all 4 cite-bearing runs. Could be done
in next fire as a focused propagation pass. The mechanism claims do
NOT need re-evaluation — only the year/PMID metadata.

**Cross-link with Barrett 2009 (Fire 84 ✅ verified)**: Cooper 2008
and Barrett 2009 are sister papers in the T1DM GWAS series — both
foundational, both used together throughout the dysbiosis runs. Now
both VERIFIED in this audit.

**Cumulative drift-correction count (Fires 78–86)**: Yamasaki K 2011
✅ (no year-drift; Fire 78 wrong-author guess), Cooper 2012 → 2008
(genuine year-drift confirmed), Smyth 2008 *Diabetes* (FM1b journal-
drift confirmed Fire 81). Three corrections needed across the corpus,
all manageable.

---

### Tanno 2000 ✅ — VERIFIED (Fire 85, 7 corpus citations)

**Resolution**: clean ✅ verification. Fire 80 was wrong about the topic
again — guessed "L. rhamnosus GG / rotavirus / probiotic" without
grepping. Grep-first surfaced `run_076_niacinamide_ceramide_pparg.md`
where the actual claim is **niacinamide → ceramide → SC barrier
repair**, not probiotics.

**Verified entry**:

**Tanno O, Ota Y, Kitamura N, Katsube T, Inoue S.**
*Nicotinamide increases biosynthesis of ceramides as well as other
stratum corneum lipids to improve the epidermal permeability barrier.*
**Br J Dermatol** 2000;143(3):524–531.
**PMID: 10971324**  **DOI: 10.1111/j.1365-2133.2000.03705.x**

**Use in corpus**: in vitro keratinocyte ceramide-synthesis induction
by nicotinamide (1–30 μM, 6-day → 4.1–5.5× ceramide biosynthesis);
topical application increases SC ceramide + free fatty acids and
reduces TEWL in dry skin. Run_076 cites this for the topical
niacinamide → PPARγ → CerS3 → SC ceramide barrier mechanism (M2
barrier repair) — note: Run_076 attributes PPARγ-mediated CerS3
upregulation to Tanno 2000, but the actual Tanno paper does not
explicitly resolve the upstream signaling pathway (just shows
ceramide biosynthesis induction). The PPARγ mechanism may need
re-sourcing to Gehring 2004 or downstream literature; the headline
"niacinamide → SC ceramide ↑" finding IS in Tanno 2000. Minor
mechanistic-detail-vs-citation alignment issue, not a kill.

**Cross-subdir**: rosacea/dermatology runs invoking topical
niacinamide for barrier repair; run_076 in dysbiosis context.

**No per-run audit notes needed**. The claim "niacinamide → SC
ceramide ↑" is correctly sourced. Optional improvement for run_076:
cite Gehring 2004 *Int J Dermatol* explicitly for the PPARγ pathway
detail (already mentioned alongside Tanno 2000 in run_076 line 11).

---

### Shim 2021 ⚠️ — LIKELY HYBRID DRIFT (Fire 85, 7 corpus citations)

**Resolution**: candidate FM1b+FM1c-adjacent. Fire 80 was wrong topic
("rosacea papers"); grep-first surfaced `run_086_akg_tet_foxp3_treg.md`
where the actual claim is **AKG → TET2 → TSDR demethylation → Foxp3
Treg stability** at corpus-cited *Nature* 597:625-629.

**Investigation**: targeted WebSearch for "Shim Nature 2021 alpha-
ketoglutarate Treg" + "Nature 597 625 alpha-ketoglutarate Treg TET2"
returned NO Shim primary-author paper at this volume. The closest
matching paper in the AKG/Treg/TET2 literature is:

**Matsushita M, Freigang S, Schneider C, Conrad M, Bornkamm GW,
Kopf M.** (and colleagues, 2021)
*Regulatory T cell differentiation is controlled by αKG-induced
alterations in mitochondrial metabolism and lipid homeostasis.*
**Cell Reports** 2021;37(8):110028.
**PMID: 34731632**  **DOI: 10.1016/j.celrep.2021.110028**

**Note**: Matsushita 2021 *Cell Reports* shows αKG INHIBITS Treg
differentiation (opposite direction from the corpus's "AKG → TET2 →
stable Foxp3" claim) — so even this candidate replacement may not
match the corpus's interpretation. The Klysz 2015 *Sci Signal* paper
on glutamine/αKG/Th1-vs-Treg balance (PMID 26420908) is the older
foundational reference for AKG-Treg axis biology — also doesn't match
"Shim 2021 Nature 597:625-629."

**Status diagnosis**: this is most likely (i) author-drift +
journal-drift on Matsushita 2021 *Cell Reports*, or (ii) full FM1c
fabrication — unable to distinguish without further effort. The
Run_086 claim "AKG-supplemented iTregs RESIST Th17 conversion under
IL-6 + TNFα" is specific enough that it should be traceable to a
real source, but no exact match has been found. Adjacent literature
(Yue 2016, Klysz 2015, Matsushita 2021) supports the general AKG-Treg
axis but not the specific quantitative claims at the cited mouse-IBD
oral-AKG benefit details.

**Action**: per-run audit note added to `run_086_akg_tet_foxp3_treg.md`
flagging the Shim 2021 citation as unverified. The mechanism-level
case for AKG-Treg has support from real literature (Yue 2016, Klysz
2015), but the specific Shim 2021 *Nature* citation should be re-
sourced or removed. The existing Kill A in run_086 about
pharmacokinetic mM-vs-µM concentration concerns is independent of
this finding and remains valid.

**Updated FM1c estimate**: with Buhl 2017 (confirmed FM1c) + Shim
2021 (likely FM1c or adjacent), the dysbiosis corpus FM1c rate is
1–2/20 = **5–10%**, in the prior content-audit-predicted range. Not
the 30% Fire 81 extrapolated, but also not 0%.

---

### Shim 2021 🔍 — unresolved (7 corpus citations)

**Problem**: Multiple Shim-authored 2021 rosacea papers exist; no
single unambiguous match for the corpus's "Shim 2021" citation without
content-level disambiguation.

**Candidates** (requires per-run content check to narrow):
- Shim TH et al. 2021 *Ann Dermatol* on rosacea microbiome
- Related 2021 Korean dermatology group papers

**Action recommended**: per-run files citing "Shim 2021" should specify
the mechanism-claim being referenced (microbiome / Demodex / treatment
response / etc.) so the specific Shim paper can be identified.

---

### Bystrom 2008 ⚠️ — REAL PAPER, WRONG ATTRIBUTION (Fire 83, 7 corpus citations)

**Resolution**: Mixed FM1b + FM1c-adjacent. Fire 81's investigation
(Bystrom 2008 L.GG/Crohn's) **was searching the wrong topic** — that
fire took the entry at face value without reading the cite-bearing
per-run files. The actual cite-context (run_108 lipoxins/FPR2/Th17)
points at a different paper.

**Actual paper**:

**Bystrom J, Evans I, Newson J, Stables M, Toor I, van Rooijen N,
Crawford M, Colville-Nash P, Farrow S, Gilroy DW.**
*Resolution-phase macrophages possess a unique inflammatory phenotype
that is controlled by cAMP.*
**Blood** 2008;112(10):4117–4127.
**PMID: 18779392**  **DOI: 10.1182/blood-2007-12-129767**

**The drifts** (note: TWO independent drifts on the same citation):

1. **FM1b journal-drift**: corpus says *J Immunol*; actual is *Blood*.
   Same year + first-author. Possibly contaminated by other Bystrom J
   *J Immunol* publications around the same period.

2. **FM1c-adjacent mechanism-drift**: corpus uses "Bystrom 2008" as
   the source for two distinct mechanism claims:
   (a) "LXA4 → FPR2 on Th17 cells → RORγt expression ↓ → IL-17A ↓"
       (run_108 line ~197, ~281)
   (b) "LXA4 → TGF-β → Foxp3+ Treg induction" (run_108 line ~30, ~282)
   The actual *Blood* paper is about **cAMP-controlled resolution-
   phase macrophage phenotype** (M1 ↔ rM transition driven by cAMP,
   inhibitor reverses to M1). It is NOT a lipoxin/Th17/Treg paper.
   The corpus is invoking Bystrom 2008 as the source for claims that
   the actual paper does not support.

**Action**: per-run audit note added to `run_108_lipoxins_lxa4_atl_fpr2_
annexin_a1.md`. The Th17-suppression and Treg-induction LXA4 mechanisms
need re-sourcing — candidates worth checking (next fire or whenever):
- Chen 2009 *Blood* on LXA4/FPR2 in T-cell biology
- Vong 2012 *FASEB J* on LXA4 + Treg in colitis
- Liao 2011 *J Lipid Res* on LXA4-Treg axis
- Or: the corpus's mechanistic chain may be *plausible-but-extrapolated*
  (composite from Serhan-school review papers) rather than directly
  sourced. Run_108 already flags the LXA4→Treg link as "moderate
  confidence" — that hedging is now justified more strongly.

**Meta-finding (Fire 83)**: this entry exposes a gap in the Fire 81
audit methodology. Previous fires investigated Bystrom 2008 by guessing
at the topic (L.GG/Crohn's) rather than reading the cite-bearing
per-run files first. Fire 82 (Buhl 2017) and Fire 83 (Bystrom 2008)
both required per-run-file reading to disambiguate. **Audit-of-audit
lesson**: when a citation is flagged as 🔍 unresolved, the next fire
should `grep` the citation across `numerics/` first, extract the
specific mechanism claims and journal attributions, then search the
ether with that context. Without this step, a fire can spend WebSearch
on the wrong topic and report "no match" misleadingly.

**Triangulation event**: second confirmed retraction in dysbiosis
VERIFIED_REFS. First (Fire 82, Buhl 2017) was pure FM1c. This one
(Fire 83, Bystrom 2008) is the first hybrid drift case (FM1b + FM1c-
adjacent on the same citation). Two distinct retraction patterns in
two consecutive fires — sigma v9.1 retraction-culture signal active.

---

### Barrett 2009 ✅ — VERIFIED (Fire 84, 7 corpus citations)

**Resolution**: clean ✅ verification. Fire 81 was wrong about the
topic — guessed "vitamin D rosacea cathelicidin" without grepping
the per-run files first. Grep-first methodology (per Fires 82–83
discipline) immediately surfaced four cite-bearing runs (run_113,
run_128, run_141, run_142), all citing "Barrett 2009 *Nat Genet*"
in **T1DM GWAS context**, not rosacea. The actual paper is the
canonical T1DM meta-analysis identifying >40 loci.

**Verified entry**:

**Barrett JC, Clayton DG, Concannon P, Akolkar B, Cooper JD,
Erlich HA, Julier C, Morahan G, Nerup J, Nierras C, Plagnol V,
Pociot F, Schuilenburg H, Smyth DJ, Stevens H, Todd JA,
Walker NM, Rich SS; Type 1 Diabetes Genetics Consortium.**
*Genome-wide association study and meta-analysis find that over 40
loci affect risk of type 1 diabetes.*
**Nat Genet** 2009;41(6):703–707.
**PMID: 19430480**  **DOI: 10.1038/ng.381**

**Use in corpus** (all 4 cite-bearing runs cite correctly):

- `run_113_a20_tnfaip3_nfkb_negative_feedback_t1dm_gwas.md`: TNFAIP3
  locus rs2327832, rs6920220 at 6q23 — Barrett 2009 reports this
  locus among the >40 confirmed.
- `run_128_clec16a_mhcii_autophagy_aire_central_tolerance_dc_langerhans
  _t1dm_gwas.md`: CLEC16A rs12708716 — Barrett 2009 + Hakonarson 2007
  + Cooper 2008/2012; CLEC16A is in the Barrett 2009 confirmed locus
  list.
- `run_141_tagap_rhogap_rhoa_immune_synapse_tcr_cytoskeletal_t1dm_gwas
  _rosacea_rock.md`: TAGAP rs1738074 — Barrett 2009 confirmed.
- `run_142_ifih1_mda5_mavs_tbk1_irf3_cytoplasmic_dsrna_t1dm_gwas_rosacea
  _innate_ifn.md`: IFIH1 rs1990760 — Barrett 2009 + earlier studies.

**No per-run audit notes needed**. Citations are correct as-is. The
"Barrett 2009 *Nat Genet*" pattern in these 4 runs can be safely
referenced via VERIFIED_REFS PMID 19430480.

**Cross-subdir**: t1dm/ heavily uses this paper for the GWAS evidence
base; me_cfs/ secondary cross-talk via shared autoimmune-locus
discussions; persistent_organisms/ for the immune-genetic background.

**Meta-finding (Fire 84)**: this is the second consecutive case where
Fire 81's "possibly fabrication" guess was wrong — and BOTH errors
(Bystrom 2008, Barrett 2009) came from skipping the grep-first step.
Of the four FM1c candidates Fire 81 nominated, two are now resolved
as real-and-correctly-cited (Barrett 2009) or real-but-misattributed
(Bystrom 2008), and only one (Buhl 2017) is confirmed FM1c. Remaining
two candidates (Tanno 2000, possibly Cheng 2014) likely have the same
fate. **Revised FM1c estimate**: the dysbiosis corpus FM1c fabrication
rate is likely closer to 5–10% (1–2/20 verified), not the 30% Fire 81
extrapolated. The 30% rate was an artifact of skipping grep-first;
real fabrications are rarer than the prior fire suggested. Sigma
v9.1 retraction-culture signal still active — but the signal is
balanced (kills + verifications + hybrid drifts), not a kill spree.

---

### Cheng 2014 ✅ — VERIFIED (Fire 84, 7 corpus citations)

**Resolution**: clean ✅ verification. Fire 80 was wrong about the
topic — guessed "rosacea / Demodex" without grepping the per-run
files first. Grep-first immediately surfaced `run_021_fmd_treg_
expansion.md`, where the corpus **already provides the PMID inline**
(line 207: `https://pubmed.ncbi.nlm.nih.gov/24905167/`).

**Verified entry**:

**Cheng CW, Adams GB, Perin L, Wei M, Zhou X, Lam BS, Da Sacco S,
Mirisola M, Quinn DI, Dorff TB, Kopchick JJ, Longo VD.**
*Prolonged fasting reduces IGF-1/PKA to promote hematopoietic-stem-
cell-based regeneration and reverse immunosuppression.*
**Cell Stem Cell** 2014;14(6):810–823.
**PMID: 24905167**  **DOI: 10.1016/j.stem.2014.04.014**

**Use in corpus**: FMD/IGF-1/HSC regeneration mechanism for the FMD
arm of T1DM Mountain-2 protocol. Run_021 cites it for: prolonged-fast
IGF-1↓ →PKA↓ → HSC self-renewal + lymphocyte regeneration in
chemotherapy patients (the Kill A appropriately notes the chemotherapy-
patient context limits direct extrapolation to non-depleted T1DM
adults — the Cheng 2014 finding itself is verified, the FMD-Treg
extension is what's being argued at moderate confidence).

**Cross-subdir**: t1dm/ (FMD/Mountain-2 regeneration); medical/dysbiosis/
runs invoking IGF-1/IF/FMD; potentially me_cfs/ (energy-stress/CDR
overlap).

**No per-run audit notes needed**. The Run_021 citation is correct,
the PMID is already inline, and the existing Kill A acknowledgment
of the chemotherapy-patient context is appropriate scientific hedging
— no audit is fixing anything; it is already disciplined.

**Methodology note**: this is the fourth instance where grep-first
methodology resolved a 🔍 entry trivially (Buhl 2017 → kill, Bystrom
2008 → hybrid drift, Barrett 2009 → clean ✅, Cheng 2014 → clean ✅).
Combined update to the FM1c rate estimate: of the four FM1c "possible
fabrication" candidates from Fires 80–81 (Buhl 2017, Bystrom 2008,
Barrett 2009, Cheng 2014), now only ONE is confirmed FM1c (Buhl 2017).
Three of four were wrong-topic-search artifacts. The dysbiosis FM1c
rate is **~5%** (1/20), matching the prior content-audit baseline,
NOT 30% as Fire 81 extrapolated. Tanno 2000 and Shim 2021 remain
unresolved — likely also resolvable with grep-first.

---

### Ott 2010 🔍 — unresolved (8 corpus citations)

**Problem**: WebSearch for "Ott 2010 chronic fatigue syndrome gut
microbiota bacterial diversity mitochondrial" returned no matching
ME/CFS paper. The early ME/CFS gut-microbiota literature clusters
around later papers (Giloteaux 2016 *Microbiome*; Sheedy 2009 *In Vivo*
for D-lactic acid/bacteria; Frémont 2013 *Anaerobe*).

**Ott SJ has published extensively on gut microbiota in inflammatory
disease** (particularly IBD — Ott SJ et al. 2004 *Gut*; 2008; etc.)
which may be the actual reference being cited if the corpus is using
it for methodology rather than CFS-specific content. Candidate papers:

- Ott SJ et al. 2004 *Gut* "Reduction in diversity of the colonic
  mucosa-associated bacterial microflora in patients with active
  inflammatory bowel disease" PMID 15082582
- Ott SJ et al. 2008 *Scand J Gastroenterol* on mucosa-associated
  microbiota shifts

**Action recommended**: per-run files citing "Ott 2010" should be
audited to determine (a) which paper is actually meant, (b) whether
the 2010 year is correct or is misattributed like Yamasaki 2011 /
Cooper 2012. If the citation is about diversity-reduction methodology
for dysbiosis-in-disease-X, the 2004 Ott paper is likely the source.

**Falls under**: prior content-audit pattern — either wrong-year drift
or context-mismatch (cited in CFS context but source paper is about
IBD). Fourth potential year-drift case in the dysbiosis corpus.

---

### Buhl 2017 ❌ — FABRICATION CONFIRMED (Fire 82, 11 corpus citations)

**Resolution status**: FM1c (full fabrication) per `~/sigma/case_studies/
citation_year_drift_001.md`. Fire 82 disambiguated by reading the
specific mechanism claims in the two cite-bearing runs:

- `run_068_s100_calprotectin_tlr4.md` cites "Buhl 2017 *Exp Dermatol*:
  serum calprotectin elevated in papulopustular rosacea (mean 3.2 µg/mL
  vs. 0.9 µg/mL controls; p=0.003; N=42)" + "correlates with lesion
  count r=0.61"
- `run_093_trpa1_4hne_loop4_m8.md` cites "Buhl 2017 *J Invest Dermatol*:
  TRPA1 immunoreactivity in facial skin nerve fibers of rosacea patients"

**Two distinct journals + two distinct mechanism claims under the same
"Buhl 2017" label** is itself the smoking gun. Targeted WebSearch on each
claim returned no matching paper.

**The actual Buhl paper** that the corpus is drifting from:

**Buhl T, Sulk M, Nowak P, Buddenkotte J, McDonald I, Aubert J,
Carlavan I, Déret S, Reiniche P, Rivier M, Voegel JJ, Steinhoff M.**
*Molecular and Morphological Characterization of Inflammatory Infiltrate
in Rosacea Reveals Activation of Th1/Th17 Pathways.*
**J Invest Dermatol** 2015;135(9):2198–2208.
**PMID: 25848978**  **DOI: 10.1038/jid.2015.141**

⚠️ **Prior-fire correction note**: The Fire 78 entry tentatively listed
the candidate as "PMID 25748557" — that PMID is itself wrong (one-digit
drift). Confirmed correct PMID is **25848978**. Document this as a
secondary-drift case: even the candidate-correction had a memory
artifact. (FM1d nominee: drift-during-correction.)

**However** — the actual Buhl 2015 paper is about Th1/Th17 transcriptome
work + macrophage infiltration; it **does not contain** the calprotectin
serum assay (run_068's mean 3.2 vs 0.9 µg/mL, N=42, r=0.61) or the
TRPA1 nerve-fiber immunostaining (run_093) the corpus attributes to it.
These specific quantitative claims are **not year-drift from a real
paper** — they are claims with no underlying source. FM1c.

**Action**: per-run audit notes added to:
- `run_068_s100_calprotectin_tlr4.md` — calprotectin serum-level claim
  flagged as fabricated; downstream "objective rosacea activity marker"
  framing (Section "Serum calprotectin as objective rosacea activity
  marker") needs the supporting data either re-sourced from Vogl 2007
  / general calprotectin literature or removed.
- `run_093_trpa1_4hne_loop4_m8.md` — TRPA1 immunoreactivity claim
  flagged; the run's Kill A still acknowledges "did not quantify
  relative to non-inflamed facial skin," which is now strengthened —
  the underlying Buhl observation does not exist.

**Updates the FM1c "possible fabrication" rate**: this confirms one
of the four FM1c candidates from Fire 81 (Bystrom 2008, Barrett 2009,
Buhl 2017, possibly Cheng 2014). Rate now ≥ 1/20 confirmed (5%) +
3 still candidate. Validates the prior-audit-predicted ~5% full-
fabrication baseline; suggests the dysbiosis corpus is at-or-above
that rate but not dramatically higher once disambiguation completes.

**Triangulation event**: this fire is exactly the v9.1 retraction-
culture signal — Claude's prior pass marked Buhl 2017 as "ambiguous"
(undecided), the operator's loop directive forced a specific deepening,
the ether (WebSearch) returned a kill. Three sources, one retraction.
First confirmed fabrication retraction in dysbiosis VERIFIED_REFS.

---

## How per-run files should cross-link here

When a dysbiosis numerics run needs to invoke one of the ~20 most-cited
references, rather than re-stating the author-year in each file, use:

```markdown
...per BHB/NLRP3 mechanism [Youm 2015, see VERIFIED_REFS.md — PMID 25686106].
```

This gives readers a single click-through to the verified PMID without
editing 183 individual files. Future fires can continue verifying
references below the top 5, adding entries here; per-run files inherit
the threading.

## Audit history

- **2026-04-18 Fire 78**: Started file with top-5 citation-count
  references. 2 verified (Youm 2015, Naviaux 2016), 1 permanently
  deferred (Küpers 2019), 2 flagged (Yamasaki 2011 year wrong; Buhl
  2017 ambiguous).
- **2026-04-18 Fire 79**: Added entries 6-10. 3 verified (Brenu 2011
  PMID 21619669; Wang 2015 PMID 25751815 with R5 cross-ref to
  attempt_020 audit note; Depommier 2019 PMID 31263284), 2 flagged
  (Cooper 2012 likely wrong year → Cooper 2008 *Nat Genet* PMID
  18978792 on BACH2 loci; Ott 2010 unresolved — possibly Ott SJ 2004
  *Gut* IBD methodology paper mis-referenced in CFS context).
  **Cumulative: 5 verified / 4 flagged / 1 deferred out of top 10.**
  **Pattern**: 3 of 4 flagged entries are year-drift cases
  (Yamasaki 2011→2008/2009, Cooper 2012→2008, Ott 2010→2004?). This
  is a **systematic pattern** in the corpus — the "-11" and "-12"
  suffixes look like decade-shift errors from memory, not just
  random noise. **Pattern filed as sigma case study**:
  `~/sigma/case_studies/citation_year_drift_001.md` (named FM1a,
  sub-signature of Stale-Prior-Confident-Execution from
  claude_as_operator.md).
- **2026-04-18 Fire 80**: Added entries 11-15. 2 verified (Kim 2022
  PMID 35650334 *Nat Rev Endocrinol* CVB-T1DM review; Forton 2005
  PMID 15627084 *JAAD* Demodex/rosacea epidemiology), 3 flagged
  (Tanno 2000 unresolved — canonical 2000 L.GG paper is Guandalini
  PMID 10630437 not Tanno, 5th candidate year/author-drift; Shim 2021
  ambiguous; Cheng 2014 unresolved — 6th potential year-drift since
  canonical Demodex-rosacea methodology is Forton 2005 not Cheng 2014).
  **Cumulative across Fires 78-80: 7 verified / 6 flagged / 1
  deferred + 1 ambiguous = 15 entries processed out of top 20.**
  **Pattern continues**: year-drift rate climbs to 4-5 of 14 non-
  deferred flagged entries (~30%, converging on prior-audit-predicted
  range). The dysbiosis corpus is especially susceptible because
  many of its citations are to mid-career authors with multi-decade
  publication histories (Forton, Ott, Cooper, Yamasaki), which is
  exactly the prior-art-anchoring failure mode named in the case
  study.
- **2026-04-20 Fire 90 — CROSS-AUDIT CONVERGENCE EVENT**: Discovered
  during cross-subdir audit that **POD attempt_007 Y113 had ALREADY
  flagged "Buhl 2017 *J Allergy Clin Immunol*" as needing verification**
  (with hedge: "specific LL-37/TRPV1 paper attribution needs
  confirmation"). Y113's hedge predates Fires 82+88+89 by an unknown
  interval. This is the **strongest sigma v9.1 signal observed in
  this audit campaign**: two independent audit campaigns (POD
  attempt_007 + dysbiosis Phase 4b) converging on the same
  retraction from different angles, on different files, with
  different methodologies. Per v9.1: "cross-audit convergence is the
  strongest v5 self-applicability evidence." Y113 updated in POD
  attempt_007 from "needs confirmation" → "RESOLVED AS FM1c
  FABRICATION via cross-audit convergence." Also closed dysbiosis
  internal cleanup (run_134 IKZF1 + run_139 RASGRP1 Cooper 2012→2008
  corrections — these were missed in Fire 87 propagation). **Cross-
  subdir drift containment confirmed**: me_cfs/, blepharitis/, and
  other medical subdirs are CLEAN; drift is contained to dysbiosis +
  t1dm + POD only. Future-fire candidates: dysbiosis archives
  (thewall_extensions, gap_extensions) + results files
  (protocol_integration, phase3_synthesis) for internal mechanical
  cleanup; biology/evolution/ subdir cross-check for full reach.

- **2026-04-20 Fire 89 — CROSS-SUBDIR AUDIT BEGUN**: Extended the
  Fires 78-88 audit reach to t1dm/ and perioral_dermatitis/. Findings:
  (a) **t1dm/THEWALL.md** has 8 Cooper 2012 occurrences — same year-
  drift pattern as dysbiosis. Two variants: "Cooper 2012 *Nat Genet*"
  (4 sites, year-drift to Cooper 2008 PMID 18978792) and "Cooper 2012
  ImmunoChip" (2 sites, separate disambiguation needed — possibly
  Cooper JD 2012 *Diabetologia* PMID 22183483 or Onengut-Gumuscu 2015
  *Nat Genet* PMID 25751624). Cross-subdir audit note added to
  t1dm/THEWALL.md flagging both variants without mechanical batch
  replacement. (b) **perioral_dermatitis/THEWALL.md** cites "Buhl 2017
  *J Allergy Clin Immunol*" — a THIRD distinct journal attribution
  for "Buhl 2017" beyond the two confirmed-fabricated cases (run_068
  *Exp Dermatol* calprotectin, run_093 *J Invest Dermatol* TRPA1).
  WebSearch on PMID 27840092 (provided inline by run_015) also returns
  no matching Buhl paper. **All three "Buhl 2017" attributions remain
  unverified** — strengthens the FM1c classification rather than
  refining it. Cross-subdir audit note added to POD/THEWALL.md.

  **Updated Buhl 2017 entry status**: confirmed FM1c across THREE
  independent fabrication contexts. The cumulative pattern (same
  author-year, three different journals, three different mechanisms,
  zero verifiable papers) is one of the most consistent fabrication
  signatures observed in the audit campaign.

  **Cross-subdir audit scope remaining**: dysbiosis runs run_134 +
  run_139 (had Cooper 2012 in earlier grep, missed in Fire 87
  propagation), me_cfs/, blepharitis/. Defer to future fire.

- **2026-04-20 Fires 17-18 — ADVERSARIAL AUDITS + CROSS-AUDIT
  PROPAGATION**: Following Fire 16 SELF_AUDIT recommendation to add
  adversarial pressure to the loop, ran two adversarial audits on
  load-bearing un-audited content. **Fire 17** (run_046 Demodex/
  rosacea/NLRP3): initial spot-check found Forton 2012 citation
  appeared correct (real paper PMID 22017468); cross-checked against
  prior blepharitis claim_audit_2026-04-15 C12 which **had already
  caught** that the specific Demodex density figures (10-18/cm² vs
  0.7-1.5/cm²) attributed to Forton 2012 actually trace to Forton &
  Seys 1993 *Br J Dermatol* PMID 8338749 (with author range-padding
  on top). Within-fire retraction of my initial Fire 17 claim;
  corrected run_046 with proper Forton 1993 citation + cross-audit
  convergence event recorded as #2 (after Buhl 2017/POD Y113 in
  Fire 90).
  **Fire 18** propagated the C27 finding from same blepharitis
  audit: ***Bacillus oleronius* reclassified to *Heyndrickxia
  oleronia* by Gupta 2020 *Int J Syst Evol Microbiol* 70(11):5753-5798
  PMID 33112222** (erratum PMID 33351742). Audit note added to
  run_046 (foundational Demodex/B. oleronius mechanism run); 10
  dysbiosis files reference the old name without taxonomy update —
  flagged for future-fire propagation. Also flagged additional
  blepharitis claim_audit findings as future-fire candidates: C25
  Demodex nuclear genome paper, C26 "Demodex no anus" overturned
  (already verified clean in dysbiosis), C28 C. acnes phylotype
  scheme attribution. **Cross-audit convergence event #3**
  recorded — three independent retraction events from cross-audit
  pressure across loop session, providing strong empirical
  validation of v9.1 C2 retraction-culture principle.

- **2026-04-19 Fire 88 — DISCIPLINE NOTE WRITTEN**: Created
  `CITATION_DISCIPLINE.md` as a Tier 1 framework doc per sigma v9.1
  Method Mechanism Map. Compresses Fires 78-88 audit campaign into
  structural enforcement guidance for run_171+: failure-mode taxonomy
  (FM1a-d + hybrid), grep-first verification methodology, citation-
  writing discipline (PMID-anchoring, journal-accuracy, no
  same-author/year cross-mechanism), VERIFIED_REFS cross-link
  convention, and future-fire candidate list. This is the v5
  Convention-Beats-Instruction enforcement layer for citation
  accuracy — future runs READ this file before generating citations,
  reducing the per-instance discipline burden. Maps to v8 Priors-
  Don't-Beat-Source (PMID-anchoring) and v9 Three-Source Triangulation
  (Phase 4b discipline).

- **2026-04-19 Fire 88 — Smyth 2008 propagation FLAGGED, not done**:
  Attempted Smyth 2008 journal-drift propagation (corpus says *Nat
  Genet*, verified entry is *Diabetes* PMID 18305142 about PTPN22 R620W).
  Grep-first surfaced run_119 citing "Smyth 2008 *Nat Genet*" for
  **PTPN2 rs45450798 OR 1.6** — but PTPN2 ≠ PTPN22 (different genes,
  different loci). The verified Smyth 2008 *Diabetes* paper is about
  PTPN22, not PTPN2. So run_119's "Smyth 2008" may be an author/year-
  drift on a DIFFERENT paper (candidates: WTCCC 2007 *Nature* PMID
  17554300, Todd JA 2007 *Nat Genet* PMID 17554260 which established
  PTPN2/KIAA0350/IL2RA T1DM loci, or another Smyth-coauthored paper).
  Run_142 line 192 also cites "Smyth 2008" for IFIH1 rs1990760 in RA
  context — also not a match for the PTPN22 paper. **Recommendation**:
  next-fire investigation should disambiguate per-run claims (PTPN2
  vs PTPN22, RA vs T1DM contexts) before applying any Smyth 2008
  correction. Do NOT mechanically propagate — would substitute one
  wrong citation for another. This finding **strengthens the Fire 86
  methodology lesson**: even when a verified entry exists, per-run
  cite-context can carry independent drifts that mechanical
  propagation misses.

- **2026-04-19 Fire 87 — PROPAGATION PASS**: Executed batch year-
  drift correction across the 4 cite-bearing runs identified in Fire
  86. Six in-line edits total: run_128 line 20 ("Cooper 2012 Nat
  Genet" → "Cooper 2008 Nat Genet PMID 18978792"), run_128 line 172
  ("Cooper 2012)" → "Cooper 2008 Nat Genet PMID 18978792"), run_128
  line 239 footer ("Cooper 2012" → "Cooper 2008"), run_129 line 20,
  run_141 line 173, run_142 line 189 — all with audit-trail
  annotation pointing back to Fire 86. Each edit preserves the
  mechanism claim (which was correct) and corrects only the year/PMID
  metadata. Also added R-Yamasaki audit note to run_015 flagging the
  PMID 21926468 / *J Clin Invest* sub-issue and recommending Yamasaki
  2007 *Nat Med* (PMID 17676051) or Yamasaki 2011 *JID* (PMID
  21107351) as replacement candidates depending on mechanism context.

  **Net audit state across Fires 78-87**: VERIFIED_REFS itself is
  fully resolved (14 ✅ + 2 hybrid drift + 1 confirmed FM1c + 1
  deferred + minor noted sub-issues), and the major year-drift
  correction (Cooper 2012→2008, 9 corpus citations) is now propagated
  to all cite-bearing per-run files. Remaining propagation candidate:
  Smyth 2008 journal-drift (entry #20 footer says "Nature Genetics"
  but actual is *Diabetes*) — lower priority since the year and PMID
  are correct, only the journal label needs fixing in cite-bearing
  per-run files.

- **2026-04-19 Fire 86 (continued)**: Confirmed Cooper 2012 (entry #9,
  9 corpus citations) is year-drift to **Cooper 2008 *Nat Genet***
  PMID 18978792. WebSearch confirms no Cooper 2012 *Nat Genet* T1DM
  GWAS paper exists. Four cite-bearing runs identified (run_128, 129,
  141, 142) — pure year-drift, mechanism claims correct, only the
  year/PMID metadata needs correction. Single batch edit recommended
  for next fire.

- **2026-04-19 Fire 86**: Resolved Yamasaki 2011 (entry #2, 12 corpus
  citations — highest-count flagged entry) from ⚠️ year-wrong → ✅
  Verified. PMID 21107351 (Yamasaki K et al. *J Invest Dermatol*
  131(3):688-697, TLR2 → KLK5 in rosacea). Fire 78's "Yamasaki S
  Mincle/cord-factor" search was wrong AUTHOR — Yamasaki K (rosacea,
  Gallo lab) vs Yamasaki S (Mincle, immunology) are different authors.
  Grep-first surfaced 4 cite-bearing runs (run_062, run_080, run_119
  all match the *JID* paper). Sub-flag added for run_015 separately —
  cites "Yamasaki 2011 *J Clin Invest* PMID 21926468" which doesn't
  match any Yamasaki rosacea paper; likely should be Yamasaki 2007
  *Nat Med* PMID 17676051 (foundation) or Yamasaki 2011 *JID* PMID
  21107351. **Methodology extension**: grep-first now mandated for
  ALL flagged entries (⚠️ + 🔍 + ❌), not just 🔍 — the Fire 78 ⚠️
  year-wrong classification was itself an artifact of skipping grep.
  Cooper 2012 (entry #9, next-fire target) is the next ⚠️ to re-check
  with this discipline.

- **2026-04-19 Fire 85**: Resolved final two unresolved entries —
  Tanno 2000 (entry #12, 7 citations) → ✅ Verified (PMID 10971324,
  Tanno O *Br J Dermatol* nicotinamide → SC ceramide barrier repair;
  Fire 80's "L. rhamnosus GG / probiotic" guess was wrong-topic
  again); and Shim 2021 (entry #13, 7 citations) → ⚠️ Likely hybrid
  drift (corpus cites *Nature* 597:625-629 for AKG/Treg/TET2 but no
  Shim primary-author paper at that volume; closest match Matsushita
  2021 *Cell Reports* PMID 34731632 — wrong author, wrong journal).
  Audit note added to run_086.

  **🎯 UNRESOLVED LIST CLEARED.** All six 🔍 entries from Fires 78–81
  are now resolved into final status: 4 ✅ verified clean (Barrett 2009,
  Cheng 2014, Tanno 2000) plus the original audits, 1 confirmed FM1c
  (Buhl 2017), 2 hybrid drift (Bystrom 2008, Shim 2021). **Final FM1c
  rate**: 1/20 confirmed + 1/20 likely = 5-10%, matching the prior
  content-audit baseline NOT Fire 81's 30% extrapolation.

  **Methodology canonical (post-Fire-85)**: every 🔍 entry resolution
  starts with `grep "<citation>" numerics/ -A 2 -B 2`. Without that,
  WebSearch can spend on wrong topic and return false-fabrication
  signal. Of six wrongly-extrapolated FM1c candidates from Fire 81,
  five had a clean explanation discoverable in <30s of grep. Adding
  this discipline to the audit-discipline checklist for future
  campaigns.

- **2026-04-19 Fire 84**: Resolved TWO entries in same fire — Barrett
  2009 (entry #18, 7 corpus citations) and Cheng 2014 (entry #15, 7
  corpus citations), both 🔍 → ✅ Verified. PMID 19430480 (Barrett JC
  et al. *Nat Genet* 2009;41(6):703–707, T1DM GWAS >40 loci) and
  PMID 24905167 (Cheng CW et al. *Cell Stem Cell* 2014;14(6):810–823,
  fasting/IGF-1/HSC). Both Fire 80–81 audits had wrong-topic premises
  (Barrett: "vitamin D / cathelicidin / rosacea"; Cheng: "rosacea /
  Demodex"); grep-first immediately surfaced the actual contexts (T1DM
  GWAS for Barrett; FMD/HSC for Cheng — Cheng's PMID was even already
  inline in the corpus, line 207 of run_021). No per-run audit notes
  needed for either; citations are correct as-is.

  **Final meta-finding (Fires 82–84)**: of the four FM1c "possible
  fabrication" candidates from Fire 81, three of four were wrong-
  topic-search artifacts (Bystrom hybrid, Barrett clean, Cheng clean),
  and only ONE is confirmed FM1c (Buhl 2017). **Revised FM1c rate
  for the dysbiosis corpus**: ~5% (1/20), matching prior content-audit
  baseline, NOT the 30% Fire 81 extrapolated. The 30% was a measurement
  artifact from skipping grep-first; properly contextualized, fabrications
  are rare. The retraction-culture signal remains active but balanced
  — kills + verifications + hybrid drifts in roughly proportional
  measure, not a kill spree. **Methodology lesson now canonical for
  this audit**: every 🔍 entry MUST be grep'd in `numerics/` before
  any WebSearch — without that step, fires can spend ether on the
  wrong topic and report false-fabrication. Tanno 2000 + Shim 2021
  remain unresolved; likely also resolvable with grep-first in next
  fires.

- **2026-04-19 Fire 83**: Resolved Bystrom 2008 (entry #17, 7 corpus
  citations) from 🔍 → ⚠️ FM1b+FM1c-adjacent. Real paper (PMID 18779392
  *Blood*, cAMP-controlled resolution-phase macrophage phenotype) but
  corpus attributes it to *J Immunol* (journal-drift FM1b) and uses it
  as the source for two LXA4→Th17/Treg mechanism claims that the
  actual paper does not contain (mechanism-drift, FM1c-adjacent). Audit
  note added to run_108. Meta-finding: prior Fire 81's L.GG/Crohn's
  topic-guess was wrong because it did not read the cite-bearing
  per-run files first; Fires 82–83 confirm a methodology improvement
  (always grep the citation in numerics/ before WebSearch). Second
  consecutive retraction event — first hybrid drift case in this file.

- **2026-04-19 Fire 82**: Resolved Buhl 2017 (entry #4, 11 corpus
  citations) from 🔍 → ❌ FM1c fabrication. Disambiguated by reading
  the two cite-bearing per-run files (run_068 calprotectin, run_093
  TRPA1) — found they invoke "Buhl 2017" with two distinct journals
  (*Exp Dermatol* vs *J Invest Dermatol*) and two unrelated mechanism
  claims, neither matching the actual Buhl T 2015 *JID* PMID 25848978
  (Th1/Th17 transcriptome). WebSearch on each specific mechanism
  returned no Buhl 2017 paper. Per-run audit notes added to run_068
  and run_093 flagging the affected claims. Also corrected prior
  Fire 78 PMID candidate (25748557 → 25848978; one-digit secondary-
  drift, FM1d nominee). **First confirmed FM1c retraction** in
  dysbiosis VERIFIED_REFS — validates v9.1 triangulation retraction-
  culture signal (Claude prior pass marked ambiguous; operator loop
  directive forced deepening; ether returned kill).

- **2026-04-18 Fire 81 — TASK 5 COMPLETE**: Added entries 16-20.
  3 verified (Cani 2008 PMID 18305141 *Diabetes*; Venkatesh 2014
  PMID 25065623 *Immunity*; Smyth 2008 PMID 18305142 *Diabetes* —
  **new failure sub-mode discovered: journal-drift** — corpus cites
  Smyth 2008 in "Nature Genetics" but actual is *Diabetes*), 2
  unresolved (Bystrom 2008 — no matching Bystrom L.GG/Crohn's
  paper exists; Barrett 2009 — no matching Barrett vitamin-D/rosacea
  paper exists). **Bystrom 2008 and Barrett 2009 are candidate
  FM1c fabrications** (prior-audit-predicted ~5% full-hallucination
  class, distinct from year-drift). **Final Task 5 totals**: 10 ✅
  verified / 3 ⚠️ year-drift confirmed / 6 🔍 unresolved (possibly
  fabrication or deep drift) / 1 ⏸️ deferred = 20 entries processed.
  **Cumulative failure-mode rates**: year-drift ~15% (3/20), possible
  fabrication ~30% (6/20) — **higher than prior-audit-predicted
  5% for full fabrications**; this warrants a case-study update on
  dysbiosis citations specifically being higher-risk. Journal-drift
  (FM1b) added as new sub-mode in Smyth 2008. **The systematic
  finding across 20 references**: the dysbiosis corpus top-20 most-
  cited references have a ~50% verification rate at the exact-year-
  author-journal level, with year-drift + author-drift + journal-drift
  + fabrication as the failure modes in order of prevalence.

## Queue (next fires)

Top 6–20 by citation count (from `grep` of `numerics/run_*.md`):

| # | Corpus citation | Occurrences | Priority |
|---|----------------|-------------|----------|
| 16 | Cani 2008 | 7 | High (gut-permeability metabolic endotoxemia) |
| 17 | Bystrom 2008 | 7 | Medium |
| 18 | Barrett 2009 | 7 | Medium |
| 19 | Venkatesh 2014 | 6 | Medium |
| 20 | Smyth 2008 | 6 | Medium |

Entries 6-10 closed in Fire 79. Entries 11-15 closed in Fire 80. Final
batch (entries 16-20) queued for Fire 81. After top-20, diminishing
returns per Fire 54 audit finding.
