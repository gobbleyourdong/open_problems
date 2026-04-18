# Verified References — T1DM Corpus

> **Purpose**: central PMID-threaded reference list for the t1dm/ corpus.
> Companion to `medical/dysbiosis/VERIFIED_REFS.md`; same pattern,
> different subdir. Addresses Y334-Y347 from AUDIT_LOG Fire 67 and
> YELLOW-flags from earlier fires (2-10).
>
> **Method**: WebSearch-verified PMIDs per sigma v9 Three-Source
> Triangulation (Phase 4b Content Audit).
>
> **Discipline** per `~/sigma/case_studies/citation_year_drift_001.md`:
> flag pre-2010 author-year citations as likely drifted; flag journal
> assertions as possibly drifted (FM1b); flag unresolved citations as
> candidate fabrications (FM1c). **My own R9 audit note at
> `attempts/attempt_027_mountain1_you_dont_need_cells.md` exhibited
> the exact FM1b + FM1c pattern** — corrected this fire.
>
> **Status**: Started 2026-04-18 Fire 82. In progress.

## Verified entries

### Meier/Butler 2005 ✅ (cited in attempt_043, attempt_027 R9-correction, THEWALL)

**Meier JJ, Bhushan A, Butler AE, Rizza RA, Butler PC.**
*Sustained β-cell apoptosis in patients with long-standing type 1
diabetes: indirect evidence for islet regeneration?*
**Diabetologia** 2005;48(11):2221–2228.
**PMID: 16205882**  **DOI: 10.1007/s00125-005-1949-2**

⚠️ **Corrects R9 audit note at attempt_027** (originally filed 2026-04-18
Fire 72 with wrong PMID 16186398 and wrong journal *Diabetes*). PMID
16186398 is actually Butler AE et al. 2003 *Diabetes* on **T2DM
β-cell deficit** — a different paper on a different disease. R9
audit note corrected in place.

**Use in corpus**: 42 T1DM autopsies, **88% insulin-positive residual
cells**, elevated β-cell apoptosis rates, **key evidence for ongoing
β-cell regeneration** in long-standing T1DM. Primary citation for
R > D inequality model + anti-problem framing (what do non-progressors
look like).

**Cross-subdir**: t1dm/ primary; persistent_organisms/ (β-cell residual);
me_cfs/ (cross-disease regeneration framing).

---

### Kuss 2011 ✅ (cited in attempt_049, THEWALL, cross-disease framework audit)

**Kuss SK, Best GT, Etheredge CA, Pruijssers AJ, Frierson JM, Hooper LV,
Dermody TS, Pfeiffer JK.**
*Intestinal microbiota promote enteric virus replication and systemic
pathogenesis.*
**Science** 2011;334(6053):249–252.
**PMID: 21998395**  **DOI: 10.1126/science.1211057**

**Use in corpus**: antibiotic-depletion of intestinal microbiota before
poliovirus inoculation reduced viral replication and systemic
pathogenesis. **First demonstration that enteric viruses require gut
bacteria for efficient replication**. Load-bearing for the "dysbiosis
→ enteroviral niche" cross-subdir thesis; linked to CVB/T1DM by
analogy (CVB is also an enterovirus).

**Cross-subdir**: t1dm/ (Mountain 3 antiviral); dysbiosis/ runs invoking
enteroviral-microbiome coupling; me_cfs/ (CVB/EBV persistence + gut
dysbiosis cross-talk); myocarditis/ (CVB).

---

### Cuervo 2004 ✅ (cited in attempt_086, LAMP2 / chaperone-mediated autophagy claims)

**Cuervo AM, Stefanis L, Fredenburg R, Lansbury PT, Sulzer D.**
*Impaired degradation of mutant α-synuclein by chaperone-mediated
autophagy.*
**Science** 2004;305(5688):1292–1295.
**PMID: 15333840**  **DOI: 10.1126/science.1101738**

**Use in corpus**: canonical CMA/LAMP2a mechanism paper. Wild-type
α-synuclein translocates to lysosomes via LAMP2a for degradation;
mutant α-synuclein blocks LAMP2a and impairs CMA substrate
degradation. **Primary reference for LAMP2a-as-CMA-receptor mechanism**
used in t1dm/ attempt_086 cross-disease extension (CMA receptor
defects link β-cell fate with Parkinson's-like mechanisms) and in
GSE184831 LAMP2 -2.7× transcriptomic finding interpretation.

**Cross-subdir**: t1dm/ (β-cell CMA); dysbiosis/ runs invoking
autophagy pathway; me_cfs/ (LAMP2-PBMC surrogate for CMA per gap.md
v9.1 addendum).

---

### Chapman 2008 ✅ (cited in attempt_041, attempt_072, sequence-backbone claims)

**Chapman NM, Kim KS, Drescher KM, Oka K, Tracy S.**
*5′ terminal deletions in the genome of a coxsackievirus B2 strain
occurred naturally in human heart.*
**Virology** 2008;375(2):480–491.
**PMID: 18378272**  **DOI: 10.1016/j.virol.2008.02.030**

**Use in corpus**: **first report of naturally-occurring 5' terminal
deletions (TD) in human enterovirus** isolates (22–36 nt from a fatal
CVB-myocarditis case, Japan 2002). Foundation for the TD-mutant
persistence mechanism in t1dm/attempt_072 reversion-probability
analysis and the myocarditis/DCM persistence model.

**Related**: Chapman NM et al. 2005 *J Virol* PMID 15890942 on CVB3 TD
in murine heart — the mouse-model predecessor paper establishing
encapsidation of negative-strand RNA correlated with TD formation.

**Cross-subdir**: t1dm/ (TD mutant persistence); myocarditis/ +
dilated_cardiomyopathy/ (cardiac CVB TD); pericarditis/ (TD
persistence in recurrent pericarditis rationale).

---

### Butler 2003 ✅ (T2DM β-cell-deficit paper — **disambiguated from Meier/Butler 2005 T1DM**)

**Butler AE, Janson J, Bonner-Weir S, Ritzel R, Rizza RA, Butler PC.**
*β-cell deficit and increased β-cell apoptosis in humans with type 2 diabetes.*
**Diabetes** 2003;52(1):102–110.
**PMID: 12502499**  **DOI: 10.2337/diabetes.52.1.102**

⚠️ **Disambiguation flag**: This is the **T2DM β-cell autopsy paper**
(n=124: 91 obese, 33 lean). Commonly confused with **Meier/Butler 2005
*Diabetologia* PMID 16205882** which is the **T1DM** 42-autopsy paper
(see above). The corpus's "Butler 2003" citations should specifically
reference T2DM β-cell deficit (40% in IFG, 63% in T2DM obese; 10-fold
β-cell apoptosis in lean T2DM vs controls); any T1DM-context citation
of "Butler 2003" is likely FM1a year-drift from Meier/Butler 2005.

**Use in corpus**: primary reference for β-cell apoptosis rate data
that also gets invoked in T1DM cross-comparisons. T2DM parallel to
Meier/Butler 2005 T1DM.

**Cross-subdir**: t1dm/ (T1DM vs T2DM comparative); dysbiosis/ runs
invoking β-cell state-transition models.

---

### Mukherjee 2011 ✅ (7 corpus citations)

**Mukherjee A, Morosky SA, Delorme-Axford E, Dybdahl-Sissoko N, Oberste MS,
Wang T, Coyne CB.**
*The coxsackievirus B 3Cpro protease cleaves MAVS and TRIF to attenuate
host type I interferon and apoptotic signaling.*
**PLoS Pathog** 2011;7(3):e1001311.
**PMID: 21436888**  **DOI: 10.1371/journal.ppat.1001311**

**Use in corpus**: mechanism paper showing CVB 3C protease **cleaves
MAVS and TRIF** — the two key adaptors for antiviral type-I IFN
signaling. MAVS cleavage occurs in the proline-rich region and
relocalizes it from the mitochondrial membrane, ablating downstream
signaling. Primary reference for "CVB evades innate immunity" claims
in t1dm/ (Mountain 4 molecular detail) and for mitochondrial-damage-
from-viral-protease in me_cfs/ (Naviaux-CDR cross-link).

**Cross-subdir**: t1dm/ (CVB innate-immune evasion); myocarditis/
(MAVS cleavage in cardiac CVB); me_cfs/ (mitochondrial damage from
chronic viral protease activity).

---

### Burgett 2011 ✅ (OSW-1 / OSBP natural-product paper)

**Burgett AWG, Poulsen TB, Wangkanont K, Anderson DR, Kikuchi C,
Shimada K, Okubo S, Fortner KC, Mimaki Y, Kuroda M, Murphy JP,
Schwalb DJ, Petrella EC, Cornella-Taracido I, Schirle M, Tallarico JA,
Shair MD.**
*Natural products reveal cancer cell dependence on oxysterol-binding
proteins.*
**Nat Chem Biol** 2011;7(9):639–647.
**PMC: PMC3158287**  **DOI: 10.1038/nchembio.625**

⚠️ PMID not confirmed via WebSearch this fire (DOI + PMC ID + journal +
volume all verified; PMID verification deferred to avoid FM1c
fabrication from guessing). Per-run files should cite DOI until PMID
is directly verified on PubMed.

**Use in corpus**: identifies OSBP as cellular target of OSW-1 (and
cephalostatin, ritterazine, schweinfurthin). Primary reference for
OSBP-as-cholesterol-transfer-target in t1dm/ Mountain-5 + the OSBP
pathway cross-linking cholesterol synthesis (red yeast rice → OSW-1
→ CVB replication complex per Strating 2015 *Cell Rep*).

**Cross-subdir**: t1dm/ (Mountain 5 cholesterol-virus axis, primarily
attempt_055 OSBP target); dysbiosis/ (OSBP pathway runs).

---

### Karjalainen 1992 ✅ (NEJM, T1DM/BSA cow's-milk molecular mimicry seminal paper)

**Karjalainen J, Martin JM, Knip M, Ilonen J, Robinson BH, Savilahti E,
Akerblom HK, Dosch HM.**
*A bovine albumin peptide as a possible trigger of insulin-dependent
diabetes mellitus.*
**N Engl J Med** 1992;327(5):302–307.
**PMID: 1377788**  **DOI: 10.1056/NEJM199207303270502**

**Use in corpus**: canonical cow's-milk / BSA / ABBOS-peptide /
molecular-mimicry hypothesis paper for T1DM. Primary reference for
the Hit 1 (A1 casein / BCM-7 / cow's milk) hypothesis in t1dm/
attempt_033 + R10 audit note that flagged the hypothesis as
TRIGR-null. Per R10: the hypothesis is not causally established at
trial level (TRIGR 2018 null), but Karjalainen 1992 is the canonical
source for the antibody-level association.

**Cross-subdir**: t1dm/ (Mountain 4 Hit 1); dysbiosis/ runs invoking
cow's-milk/gut axis.

---

### Faulkner 2017 🔍 — unresolved (candidate FM1c fabrication or year-drift)

**Problem**: WebSearch for "Faulkner 2017 hot bath hyperthermia enterovirus
antiviral mechanism" returned no matching Faulkner-authored 2017 paper.
The general hyperthermia-antiviral literature includes older papers
(Heron 1991 PMID 1965095 on hyperthermia vs viral infections in vitro)
and more recent papers on TRPV1/hyperthermia mechanisms (Zelenay 2020,
Kimura 2023 on body-temperature resistance to influenza/SARS).

**Candidate**: (i) year-drift from a Faulkner paper in a different
year; (ii) author-drift; (iii) **possible fabrication** (FM1c class).

**Action recommended**: per-run files citing "Faulkner 2017" should be
content-level audited. If the claim is hyperthermia blocking enterovirus
replication in vitro, cite Heron 1991 PMID 1965095 or Kimura 2023 (if
the claim is about body-temp dependent host resistance, which is a
different mechanism).

---

## Queue (next fires)

Additional t1dm Y-flags to verify from AUDIT_LOG Fires 2-67:

| Citation | Likely paper | Priority |
|----------|-------------|----------|
| Butler 2003 | 42-autopsy T1DM predecessor or T2DM β-cell-deficit | High (disambiguate year/journal) |
| Faulkner 2017 | hot-bath hyperthermia + CVB | Medium |
| Mukherjee 2011 | CVB-MAVS cleavage | Medium |
| Burgett 2011 | OSW-1 natural product | Medium |
| Palmer 2006 | filaggrin (but this is eczema, cross-subdir) | Low (not t1dm primary) |
| Soppela VLP-ΔVP4 | enteroviral vaccine | High (load-bearing for attempt_042 ADE rationale) |
| Longo 2017 Cell | already closed R14 audit note, verified correct | ✅ (PMID 28683282) |
| Karjalainen 1992 NEJM | cow's milk / BCM-7 | Medium |
| Kim 2008 J Virol | CVB TD-enterovirus | Medium |

Additional domains beyond t1dm:
- me_cfs/ (6 Y-flags): CDC 2.5M, GSE293840, Bolton/Younger 2018 LDN
- blepharitis/ (8 Y-flags): Gao 2005 (done as Forton cross-ref),
  Kheirkhah 2007, Zhao 2012, Kabataş 2017, Koo 2012, van Zuuren 2019,
  Lacey 2007, Maastricht H. pylori
- biology/evolution per-organism 100-113 series

## Audit history

- **2026-04-18 Fire 82**: Started file with 4 verified entries
  (Meier/Butler 2005, Kuss 2011, Cuervo 2004, Chapman 2008). Fixed
  in-place R9 audit note at attempt_027 where my own correction
  carried FM1b+FM1c drift (wrong PMID + wrong journal). **Meta-
  finding**: the audit-discipline itself can propagate drift without
  WebSearch-at-write-time; this validates `~/sigma/case_studies/
  citation_year_drift_001.md` at a recursive level — even the
  corrective operator exhibits the pattern it corrects.
- **2026-04-18 Fire 83**: Added 4 verified + 1 unresolved.
  **Butler 2003** PMID **12502499** *Diabetes* T2DM β-cell deficit
  (disambiguated from Meier/Butler 2005 T1DM PMID 16205882).
  **Mukherjee 2011** PMID **21436888** *PLoS Pathog* CVB 3C protease
  cleaves MAVS/TRIF. **Burgett 2011** *Nat Chem Biol* PMC3158287
  DOI 10.1038/nchembio.625 OSW-1/OSBP natural-product discovery
  (PMID verification deferred to avoid FM1c fabrication from
  guessing). **Karjalainen 1992** PMID **1377788** *NEJM* canonical
  BSA-peptide/T1DM molecular-mimicry seminal paper. **Faulkner 2017**
  unresolved — candidate FM1c fabrication (no matching paper
  located). Cumulative t1dm/VERIFIED_REFS: 8 verified / 1 unresolved.
  Pattern continues: **of the 4 pre-2010 author-years processed
  across Fires 82-83 (Butler 2003, Kuss 2011 is 2011, Cuervo 2004,
  Chapman 2008, Karjalainen 1992, Burgett 2011), 0 exhibited FM1a
  year-drift in this batch** — corpus may cite these with correct
  years, or the t1dm corpus is less drift-prone than dysbiosis
  (which had 15% year-drift rate). Small-sample caution applies.
