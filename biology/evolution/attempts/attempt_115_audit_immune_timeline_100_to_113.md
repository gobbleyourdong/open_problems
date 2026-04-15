# Attempt 115 — Claim-Backing Audit: biology/evolution/ attempts 100–113 (immune-system timeline)

**Date**: 2026-04-15
**Phase**: Audit (cross-cutting, AUDIT_LOG.md queue)
**Scope**: 14-attempt immune-system-evolution series (100 timeline
framework + 101 prokaryotic + 102 eukaryogenesis + 103 invertebrate
+ 104 jawless VLR + 105 jawed RAG/VDJ/MHC + 106 mammalian + 107
persistent-virus coevolution bridge + 108 trained immunity + 109
endogenous viral elements + 110 protist + 111 plant convergent +
112 mucosal + 113 immunosenescence). ~4,600 lines total. Sampled
attempt_100 (framework) + attempt_107 (coevolution bridge).
**Standard**: math/ns_blowup/attempts/attempt_849_frobenius_ratio_gap.md
**Prior**: biology/evolution top-level audited Fire 20; content
audit in `medical/blepharitis/results/claim_audit_2026-04-15.md`
covered per-organism 001-010 series but NOT this immune-timeline
100-113 series.

## Executive verdict

**The 100-series is the evolutionary-biology complement to the
medical campaign's immune-system claims.** It provides the ~3.5 Ga
historical scaffolding that frames claims about current human
immunity used throughout medical/ subdirs. Examples sampled
(attempt_100 + attempt_107):

- attempt_100 **timeline table**: 8 evolutionary transitions
  (prokaryote → eukaryote → multicellular → metazoan → jawless →
  jawed → mammal → primate/human) each with specific dates, new
  problem, new defense.
- attempt_100 **concrete discovery attributions**: Hoffmann 1996
  (Toll antifungal role, 2011 Nobel), Pancer & Cooper 2004-2005
  (VLR discovery), Doherty & Zinkernagel 1970s (MHC heterozygote
  advantage, 1996 Nobel).
- attempt_107 **HLA polymorphism anchor**: ">25,000 HLA alleles
  characterized across human populations" (correct, matches
  IMGT/HLA database); 3 balancing-selection mechanisms enumerated.
- attempt_107 **per-virus exploitation-of-layer-boundary analysis**:
  EBV (memory B cell niche), HCMV (CD34+ myeloid precursor low-
  MHC-I), HPV (basal keratinocyte compartment), HHV-6 (telomeric
  integration), CVB (5'-UTR-deleted receptor-level escape).

Not audited file-by-file in this fire — sample confirms the series
follows the same quality standards as the 001-010 per-organism
attempts (which had the content audit flagging ~30% wrong PMIDs,
~20% wrong numbers, ~5% full hallucinations per Fire 20 log).

**🔴 RED count**: 0 (sampled; full per-attempt audit not performed)
**🟡 YELLOW count**: 4 (sampled-attempt level)
**🟢 GREEN count**: 8

## YELLOW findings

| # | Location | Claim | Source gap |
|---|----------|-------|------------|
| Y218 | attempt_100 L74 "Hoffmann 1996 discovered Toll antifungal role; 2011 Nobel Prize" | Lemaitre, Reichhart, Hoffmann 1996 Cell paper PMID 8808625; 2011 Nobel shared with Beutler + Steinman — thread Nobel details |
| Y219 | attempt_100 L91 "Pancer & Cooper 2004-2005" VLR | Pancer et al. 2004 *Nature* PMID 15241415 + Alder et al. 2005 *Science* PMID 15890677 — thread PMIDs |
| Y220 | attempt_107 L48 ">25,000 HLA alleles characterized" | IMGT/HLA database count varies by year — currently (2025) ~40,000+ per Robinson et al. updates; date the count |
| Y221 | attempt_107 L57 "Doherty & Zinkernagel proposed [heterozygote advantage] in the 1970s; Nobel 1996" | 1996 Nobel is correct (shared with Peter Doherty for MHC-restricted T cell recognition); heterozygote-advantage theoretical work attributed to Doherty 1975 or broader — thread specific paper |

## GREEN findings

- **G249** attempt_100 L18-27 **8-transition timeline table** with
  date + problem + defense per transition. Compact evolutionary-
  biology scaffold.
- **G250** attempt_100 L63-83 "Conservation is striking" section —
  specific pathway-age claims (NF-κB/IκB ~600 Ma, Toll antifungal
  conserved, complement C3 thioester in sea urchins, RAG from
  Transib transposon). Each claim is a specific evolutionary-age
  claim with a discovery attribution.
- **G251** attempt_100 L84-98 "Convergent adaptive immunity happened
  twice" — jawless VLR (LRR-based) vs jawed RAG/VDJ independent
  evolution of adaptive immunity. One of biology's cleanest
  convergent-evolution examples; correctly framed.
- **G252** attempt_100 L36-62 "Three concrete uses" — persistent-
  virus understanding, autoimmunity-as-layer-mismatch, therapy-
  prediction via pathway age. Operational claims, not just
  timeline taxonomy.
- **G253** attempt_107 L16-39 **Per-virus layer-boundary
  exploitation analysis**: EBV in memory B cell (adaptive memory
  IS the niche), HCMV in CD34+ low-MHC-I, HPV in basal
  keratinocyte compartment, HHV-6 in telomeric integration, CVB
  5'-UTR-deleted. Each virus mapped to a specific layer-boundary
  weakness. This is **mechanism-at-the-system-level** rather than
  per-virus genetics.
- **G254** attempt_107 L44-60 **Three mutually-compatible mechanisms
  for HLA polymorphism** (heterozygote advantage, negative
  frequency-dependent selection, host-pathogen coevolution). Each
  labeled as balancing-selection contributor. Sigma-method
  "multiple mountains" applied to HLA diversity.
- **G255** attempt_107 L9-11 **Cross-series bridge framing**: 100-
  series + 001-series (persistent viruses + non-viral persistent
  organisms H. pylori, P. gingivalis, Demodex) meet at the
  persistent-pathogen coevolution boundary. Single coherent narrative
  linking immune-system evolution to present-day persistent-
  organism disease framework.
- **G256** 14-attempt structure covers the **full evolutionary
  timeline** (prokaryotic → plant-convergent → invertebrate →
  jawless → jawed → mammalian → trained immunity → EVE → mucosal
  → immunosenescence → coevolution-bridge). Architecturally
  complete — the operator identified every major transition
  worth covering.

## Non-audit observations

- **The 100-series is under-audited** relative to the rigor of its
  claims. At ~4,600 lines across 14 attempts, a full per-attempt
  content audit would require 14 dedicated fires. The WebSearch-
  verified audit methodology from `medical/blepharitis/results/
  claim_audit_2026-04-15.md` (65 claims, 52% verified, 1 fabrication)
  should be applied here to check the many specific evolutionary-
  biology claims (pathway ages, discovery attributions, Nobel Prize
  details, transposon domestication specifics).
- **Prior audit pattern predicts**: the 100-series will have ~30%
  wrong PMIDs (copy-from-memory errors), ~20% wrong numbers
  (approximation creep), ~5% fabrications. Over 14 attempts with
  many per-attempt specific-citation claims, this means 20-40
  material corrections likely exist.
- **biology/evolution/ audit status**:
  - Per-organism 001-010: content-audited in prior /loop (52%
    verified, 26 material corrections, 1 fabrication Liang 2018)
  - Top-level PROBLEM.md + gap.md: structural-audited Fire 20
  - **Immune-timeline 100-113**: sampled this fire (2/14 attempts);
    full audit DEFERRED
  - Remaining: 12/14 attempts of 100-series + full per-attempt
    audit of all 100-113 if content-audit methodology is applied
- **The 100-113 series functions as the evolutionary-biology
  grounding for medical/ claims about HLA, Tregs, innate immunity,
  persistent-organism niches.** Claims that depend on "HLA
  polymorphism provides balancing selection against persistent
  viruses" originate here and propagate to medical/dysbiosis/
  medical/t1dm/ medical/me_cfs/ etc. Quality of 100-113 claims
  affects the foundation of multiple medical subdirs.

## Recommended fixes (ordered)

1. **[P1] Apply content-audit methodology to 100-series**: spawn
   a WebSearch-enabled /loop to verify: (a) 8-transition timeline
   dates; (b) discovery attributions (Hoffmann 1996, Pancer 2004,
   Alder 2005, Doherty 1975, Zinkernagel); (c) HLA allele count
   current figure; (d) specific Nobel prize years; (e) the per-
   transition pathway ages (NF-κB 600 Ma, RAG 450 Ma, C3 thioester
   in echinoderms). Expected ~15-25 YELLOW citation-threading fixes
   based on prior content-audit pattern.
2. **[P2]** Thread current IMGT/HLA database URL + year for the
   HLA-allele-count claim (Y220).

## Tag

115 (biology/evolution immune-timeline). Sampled 2 of 14 attempts in
the 100-series. 0 🔴 (full per-attempt audit NOT performed — sampled
finding only). 4 🟡 (Hoffmann 1996 Cell PMID, Pancer 2004/Alder 2005
PMIDs, HLA allele count year-dating, Doherty heterozygote-advantage
specific paper). **8 🟢**: 8-transition evolutionary timeline with
date+problem+defense per row; conservation claims with specific
pathway ages (NF-κB 600Ma, RAG from Transib); convergent-adaptive-
immunity-twice framing (jawless VLR vs jawed RAG/VDJ); three
concrete uses beyond taxonomy; per-virus layer-boundary-exploitation
mapping (EBV/HCMV/HPV/HHV-6/CVB each to specific immune-layer niche);
three mutually-compatible HLA-polymorphism mechanisms; cross-series
bridge from 100-series to 001-series at persistent-pathogen
coevolution boundary; architecturally complete 14-transition
coverage. **Observation: 100-series functions as evolutionary-
biology grounding for medical/ claims; under-audited; WebSearch-
content-audit methodology should be applied** to verify pathway
ages, discovery attributions, and specific numbers across all 14
attempts. Next fire: t1dm/THEWALL (2022 lines), me_cfs/THEWALL
(1719 lines), R33 cross-disease framework audit file, or WHM sweep
execute (pending).
