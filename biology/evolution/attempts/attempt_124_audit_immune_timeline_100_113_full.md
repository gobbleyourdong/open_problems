# Attempt 124 — Full audit of immune-timeline 100-113 (the 12 attempts prior audit skipped)

**Date**: 2026-04-16
**Phase**: Audit (continues AUDIT_LOG.md queue)
**Scope**: 12 of the 14 attempts in the immune-timeline 100-series
that the prior `attempt_115_audit_immune_timeline_100_to_113.md`
deferred (101, 102, 103, 104, 105, 106, 108, 109, 110, 111, 112,
113). Attempts 100 and 107 already sampled in attempt_115.
Total ~4067 lines read.
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: attempt_115 sampled 2/14 (100 framework + 107 coevolution
bridge); found 0 🔴 / 4 🟡 / 8 🟢 on sampled set.

## Executive verdict

All 12 attempts pass the structural audit. Each file follows the
same skeleton (executive summary / discovery timeline / mechanism /
open questions / links to other attempts / key sources / gap opened
/ status) with specific year+journal+page citations and PMIDs
threaded for most primary references. Quality is consistent with
the sampled attempts 100 and 107 — the series is NOT weaker at the
un-sampled interior.

The one substantive defect is **systematic PMID-threading
inconsistency**, evident both WITHIN a single attempt (same paper
cited twice with different PMIDs) and ACROSS files (the audit doc
itself disagrees with the attempts it audited on 3 PMIDs). This
matches the prior content-audit pattern "~30% wrong PMIDs
(copy-from-memory errors)" and rises from 🟡 to 🔴 because it
cross-contaminates a meta-audit document that then recommends the
"wrong" PMID back to the reader.

**🔴 RED count**: 1 (R38, below)
**🟡 YELLOW count**: 23
**🟢 GREEN count**: 24 (representative; many more per-attempt)

## RED findings

### R38 — Systematic PMID inconsistency within + across attempts

Four concrete instances detected by side-by-side reading:

1. **attempt_104 internal**: Bajoghli 2011 "A thymus candidate in
   lampreys" *Nature* 470:90 is cited with PMID **21293374** at
   L144 and PMID **21293377** at L316 — same paper, same file, two
   different PMIDs. Pure copy-from-memory error pattern.

2. **attempt_103 vs attempt_115**: Lemaitre/Reichhart/Hoffmann 1996
   *Cell* 86:973 (Toll antifungal) cited as PMID **8808632** in
   attempt_103 L92 but as PMID **8808625** in attempt_115 Y218.

3. **attempt_104 vs attempt_115**: Pancer et al. 2004 *Nature*
   430:174 (VLR discovery) cited as PMID **15241406** in attempt_104
   L35 but as PMID **15241415** in attempt_115 Y219.

4. **attempt_104 vs attempt_115**: Alder et al. 2005 *Science*
   310:1970 (VLR diversity) cited as PMID **16373579** in
   attempt_104 L135 but as PMID **15890677** in attempt_115 Y219.

**Why load-bearing**: the audit doc (attempt_115) was intended to
be the subject-matter-expert's citation-threading guide for the
immune-timeline series. Three of its PMIDs disagree with the
attempts being audited — meaning the audit doc itself propagates
potentially wrong PMIDs. If the attempts are right, the audit doc
is wrong and needs inline correction; if the audit doc is right,
four attempts are wrong. **Either way, at minimum one of the
~8 PMIDs on these 3 papers across 4 files is incorrect.**

**Required fix**: single WebSearch-verification pass on
{Lemaitre 1996, Pancer 2004, Alder 2005, Bajoghli 2011} → insert
correct PMIDs + audit-note on attempt_115 Y218/Y219 referencing
the reconciliation. Estimated 4 WebSearches, 15 minutes.

## YELLOW findings (citation-threading gaps)

| # | Location | Issue |
|---|----------|-------|
| Y290 | attempt_101 L36 | Doron 2018 "9 new defense systems" but list names 10 (BREX/DISARM/Gabija/Druantia/Hachiman/Kiwa/Lamassu/Septu/Thoeris/Zorya) + "and others". Off-by-one-or-more. |
| Y291 | attempt_102 L7-9 | "Roughly half archaeal-derived (informational), half bacterial-derived (operational)" oversimplifies the Rivera-Lake / Martin two-domain model — actual figure is ~30-40% bacterial / ~10-20% archaeal / rest unclassifiable. |
| Y292 | attempt_102 L129 | Maillard et al. 2013 *Science* 342:235 no PMID. |
| Y293 | attempt_102 L149 | Bertin 1999 apoptosome — vague, no page, no PMID. |
| Y294 | attempt_103 L205 | Sea urchin "185/333 genes expand to ~50-100 members per individual" — canonical literature range is ~60-80; claim is approximately right but imprecise. |
| Y295 | attempt_104 L124 | "Theoretical maximum ~10^14 VLR receptors" — specific number, no direct primary source (Alder 2005 abstract reports smaller observed figure). |
| Y296 | attempt_104 L313 | Herrin 2008 PMID 18238899 — unverified; possible typo for a nearby PMID. |
| Y297 | attempt_104 L308 | Pancer et al. 2005 *PNAS* 102:9224 (hagfish VLRs) — no PMID provided. |
| Y298 | attempt_105 L399 | ">25,000 HLA alleles" — same stale figure flagged in attempt_115 Y220 (current IPD-IMGT count ~40,000+); propagated in parallel file without fix. |
| Y299 | attempt_106 L243 | von Boehmer 2005 *Nat Immunol* 6:338 no PMID; Kyewski/Klein 2006 *Annu Rev Immunol* 24:571 no PMID. |
| Y300 | attempt_106 L315 | Ljunggren/Kärre 1990 *Immunol Today* 11:237 — no PMID. |
| Y301 | attempt_108 L292 | Netea et al. 2020 *Nat Rev Immunol* 20:375 — no PMID. |
| Y302 | attempt_108 L186 | "BCG reduces infant all-cause mortality (Aaby et al.)" — no year, no PMID, author-only. |
| Y303 | attempt_108 L285-286 | Naik 2017 *Nature* 550:475 no PMID. |
| Y304 | attempt_110 L276-279 | Dunn et al. 2017 (listed as "Frontiers in Immunology 9:1906") — 2017 article in 2018-volume: year/volume discrepancy; PMID 30619239 lists but date needs resolution. |
| Y305 | attempt_110 L75-78 | Chen 2013 Dictyostelium TirA/*Legionella* — journal/volume/pages absent; no PMID. |
| Y306 | attempt_111 L323-324 | Chisholm 2006 *Cell* 124:803 no PMID; Cui 2015, Boller 2009, Ausubel 2005 no PMIDs. |
| Y307 | attempt_112 L316-317 | Cerutti 2008 *Nat Rev Immunol* 8:421 no PMID; Mowat/Agace 2014 *Nat Rev Immunol* 14:667 no PMID. |
| Y308 | attempt_113 L250-251 | Kirkwood 1977 *Nature* 270:301 + Williams 1957 *Evolution* 11:398 — no PMIDs (available in NCBI for Kirkwood). |
| Y309 | attempt_113 L202 | Alpert et al. 2019 *Nat Medicine* — vague reference, no title/volume/page/PMID. |
| Y310 | attempt_109 L99-102 | Taylor 2013 *Ecol Evol* 3:3683 no PMID. Aiewsakun/Katzourakis 2015 *Virology* 479-480:26 no PMID. |
| Y311 | attempt_112 L212-214 | Strachan 1989 *BMJ* 299:1259 hygiene-hypothesis original — no PMID (PMID 2513902 available). |
| Y312 | attempt_105 | Cooper/Alder 2006 *Cell* 124:815 no PMID. Huang et al. 2016 amphioxus active RAG — title/journal/volume all absent. |

## GREEN findings (representative)

- **G257** attempt_101 L95-116: 9-paper CRISPR-Cas discovery
  timeline 1987→2020 with specific PMIDs for each milestone (Mojica
  2005, Barrangou 2007, Jinek 2012, Makarova 2020). Discovery-chain
  format matches the math gold standard's named-theorem chains.
- **G258** attempt_101 L265-288: 5 open questions each with
  empirical status + numerical estimate (e.g., "5-15% of bacterial
  genome is defense-related" cap).
- **G259** attempt_101 L178-188: explicit CBASS ↔ cGAS-STING
  bacterial-ancestry claim with ~3 Ga depth and specific primary
  cite (Cohen 2019 PMID 31533127).
- **G260** attempt_102 L37: "timing uncertain, range 1.5-2.5 Ga"
  explicit uncertainty bar around the mitochondrial endosymbiosis
  date — rare explicit range for a common point-estimate.
- **G261** attempt_102 L44-52: Hydrogen hypothesis + Oxygen
  syntrophy hypothesis listed side-by-side with "Both may be true at
  different stages" — multiple-mountains framing.
- **G262** attempt_102 L247-248: self-labels its own percentages as
  "soft" ("~40% bacterial, ~20% archaeal, ~40% novel... These
  percentages are soft.") Maps-Include-Noise at number-level.
- **G263** attempt_103 L181-192: VLR-vs-V(D)J comparison table (9
  rows: receptor scaffold, diversity mechanism, driver enzyme,
  assembly substrate, cell types, soluble form, MHC, thymus, age).
- **G264** attempt_104 L110-120: three-lineage parallel explicitly
  labeled "strongest evidence for 'adaptive immunity' being a
  defined functional solution" — cross-validates attempt_115's G251.
- **G265** attempt_105 L42-65: three-way convergent evidence for
  RAG/Transib domestication (Liu 2019 structure + Agrawal 1998
  transposition + Kapitonov 2005 alignment) — independent methods
  converging is the math-standard "multiple mountains" pattern.
- **G266** attempt_105 L86-96: "Other transposon families could have
  provided similar raw material; the historical accident is that
  Transib was the one..." — explicit epistemic humility about
  contingency vs necessity.
- **G267** attempt_106 L58-73: Muramatsu 2000 (AID KO mouse) +
  Revy 2000 (HIGM2 patient) described as "Same issue of Cell,
  complementary findings" — canonical same-issue-convergence framing.
- **G268** attempt_106 L141-155: 5-mechanism list for placental
  tolerance (HLA-G + uterine NK + Treg + IDO + PD-L1) — explicit
  multiple-mechanism framing rather than single-explanation.
- **G269** attempt_106 L180-187: "every mammalian placenta... relies
  on a co-opted retroviral fusion protein, but the specific
  retrovirus varies by lineage" — cross-lineage generalization
  (primates HERV-W, mice syncytin-A, ruminants other ERVs).
- **G270** attempt_108 L17-31: self-aware about the framing limit of
  earlier attempts: "The classical claim — 'memory is adaptive;
  innate is memoryless' — is an over-simplification." Updates the
  100-series framing post-hoc.
- **G271** attempt_108 L149-161: invertebrate priming reinterpreted
  in the trained-immunity frame — cross-attempt consistency with
  attempt_103 L286-290 open question #1.
- **G272** attempt_109 L16-30: "Why non-retroviral EVEs were a
  surprise" — explicitly frames prior textbook consensus as wrong.
  Good framing-update discipline.
- **G273** attempt_110 L180-188: Dictyostelium TirA+SlrA+NoxA ↔
  mammalian TLR+LRR+NADPH-oxidase mapped as deep-time functional
  homology. Gives a specific 3-protein correspondence.
- **G274** attempt_111 L222-241: "Sessile / wall-bound / autotrophy
  / open-development / germline-continuity" 5-constraint explanation
  for why plants differ from animals. Explicit cause-and-effect
  reasoning ("different problem → different solution").
- **G275** attempt_111 L181-195: Flor 1942/1971 gene-for-gene
  preserved as historical observation before molecular mechanism —
  "Gene-for-gene predates the molecular understanding but accurately
  predicted the ETI phenomenon."
- **G276** attempt_112 L110-114: IgT/IgA convergence explicitly
  labeled as "parallels attempt_104's VLR-vs-V(D)J convergence" —
  cross-attempt framework consistency.
- **G277** attempt_112 L220-231: hygiene hypothesis framed as
  "flipped certain exposures from protective to absent" with cross-
  link to 001-series — framework-consistency audit at concept level.
- **G278** attempt_113 L58-87: inflammaging framed as "unselected
  byproduct of a selected trait" using disposable soma + antagonistic
  pleiotropy — explicit evolutionary framework applied to a clinical
  phenomenon.
- **G279** attempt_113 L210-213: open question "Why do some
  individuals age without inflammaging?" (centenarian resilience) is
  a self-pointed gap in the framework.
- **G280** attempt_113 L186-189: self-aware about structural role —
  "This is qualitatively different from the other attempts'
  contents (which described immune EMERGENCE at various stages).
  attempt_113 describes immune DECAY — a necessary complement to
  the evolutionary story."

## Non-audit observations

- **The 12 un-sampled attempts maintain the structural quality of
  the 2 sampled attempts (100, 107).** There is no attenuation in
  the interior of the series. attempt_115's "sampled, full per-
  attempt audit not performed" caveat is now addressed: structural
  quality is uniformly consistent.

- **Quality gradient within the 100-series is flat on structure
  but attenuates on citation discipline.** Attempts 108-113 (the
  extensions after the main-sweep 100-107) have slightly higher
  rate of missing-PMID references than 101-106 (the main-sweep).
  Recommendation: back-propagate the citation-threading discipline
  from the main-sweep into the extensions.

- **R38 detection required reading attempt_115 and the audited
  attempts side-by-side.** A single-pass audit of only the attempts
  or only the audit doc would have missed the inconsistencies. This
  is a structural-auditing observation: cross-file PMID reconciliation
  should be part of any future cite-threading sweep.

## Recommended fixes (ordered)

1. **[P1]** Single WebSearch pass on {Lemaitre 1996, Pancer 2004,
   Alder 2005, Bajoghli 2011} → reconcile the 4 PMID inconsistencies;
   insert inline correction in attempt_115 Y218/Y219 + attempt_104
   L144/L316. Closes R38.
2. **[P2]** Back-propagate attempt_101-107 PMID discipline into
   attempts 108-113 extensions. Estimated ~15-20 PMID inserts.
3. **[P3]** Date-stamp the ">25,000 HLA alleles" claim in
   attempt_105 L399 (and any earlier sites) to current IPD-IMGT
   count + year — closes Y298.

## Tag

124 (immune-timeline 100-113 full audit). Audited 12 of 14 attempts
not sampled in attempt_115. **1 🔴 (R38 PMID inconsistency)**, 23
🟡, 24 🟢. Twelve attempts are structurally sound — uniform with
attempts 100 and 107 sampled prior. Main defect: PMID inconsistencies
within attempt_104 and across attempt_115 vs the source attempts on
3 of the most-cited papers. Biology/evolution immune-timeline now at
**14/14 structural audit complete**. Remaining unaudited surfaces
across repo: t1dm/ attempts 046-094 (some sampled), dysbiosis/
numerics ~183 runs, Lean backbone grep-verification, numerics script
existence check. Next fire: one of those.

---

*Filed: 2026-04-16 | biology/evolution/attempts/attempt_124*
*Extends attempt_115 (which sampled 2 of 14).*
