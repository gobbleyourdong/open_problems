# Verified References — Biology/Evolution Corpus

> **Purpose**: central PMID-threaded reference list for the biology/evolution
> subdir, particularly the immune-timeline 100-113 series and the
> per-organism coevolution attempts. Companion to dysbiosis/t1dm/
> blepharitis/me_cfs VERIFIED_REFS files.
>
> **Related prior audit**: `medical/blepharitis/results/claim_audit_2026-04-15.md`
> performed a 65-claim content audit on biology/evolution attempts 001-010
> + blepharitis at ~52% verification rate. This file adds the 100-113
> immune-timeline series references + corrects Fire 34 AUDIT_LOG PMIDs.
>
> **Started**: 2026-04-18 Fire 87.

## ⚠️ Recursive audit-error note

AUDIT_LOG.md Fire 34 cited PMIDs for these canonical evolutionary-
immunology papers. **WebSearch verification at Fire 87 revealed the
Fire 34 PMIDs were wrong for at least 2 of 3 references checked** —
another instance of the recursive audit-layer drift pattern
documented in `~/sigma/case_studies/citation_year_drift_001.md`
(corrective operator emitting FM1c-class errors). Corrections below.

## Verified entries

### Lemaitre/Hoffmann 1996 ✅ (Drosophila Toll antifungal defense — **corpus/audit cites "Hoffmann" but first author is Lemaitre**)

**Lemaitre B, Nicolas E, Michaut L, Reichhart JM, Hoffmann JA.**
*The dorsoventral regulatory gene cassette spätzle/Toll/cactus controls
the potent antifungal response in Drosophila adults.*
**Cell** 1996;86(6):973–983.
**PMID: 8808632**  **DOI: 10.1016/s0092-8674(00)80172-5**

⚠️ **Fire 34 AUDIT_LOG cited PMID 8808625** — **WRONG** (off by 7
digits). Correct PMID is **8808632**.

⚠️ **FM1d author-drift**: the corpus cites this paper as "Hoffmann
1996" but the **first author is Lemaitre B**; Hoffmann JA is the
senior/last author. This is one of the most famous cases of last-
author-as-lab-PI getting memorialized in citations; common in the
evolutionary-immunology literature. The corrective form in
evolution/attempts should be "Lemaitre et al. 1996 *Cell* PMID
8808632" or (if emphasizing the lab) "Hoffmann lab 1996" without
listing Hoffmann as first author.

**Use in corpus**: landmark paper establishing **Toll pathway as
antifungal innate-immunity defense in Drosophila** — the discovery
that led to mammalian TLR discovery + Hoffmann's 2011 Nobel Prize
(shared with Beutler and Steinman). Primary citation for the
600-Ma NF-κB pathway ancient-origin claim in attempt_107 and the
jawless-vs-jawed convergent-adaptive-immunity story in attempt_100.

**Cross-subdir**: biology/evolution/ primary (immune-timeline 100-113);
persistent_organisms/ (ancient-innate-immunity architecture).

---

### Pancer 2004 ✅ (lamprey VLR, somatic diversification)

**Pancer Z, Amemiya CT, Ehrhardt GR, Ceitlin J, Gartland GL, Cooper MD.**
*Somatic diversification of variable lymphocyte receptors in the
agnathan sea lamprey.*
**Nature** 2004;430(6996):174–180.
**PMID: 15241406**  **DOI: 10.1038/nature02740**

⚠️ **Fire 34 AUDIT_LOG cited PMID 15241415** — **WRONG** (off by 9
digits). Correct PMID is **15241406**.

**Use in corpus**: first report of **VLR (variable lymphocyte
receptors) in jawless vertebrates** — established that lampreys
generate adaptive immunity via LRR-module rearrangement, distinct
from jawed-vertebrate V(D)J recombination. Primary citation for
the "convergent-adaptive-immunity-twice" framing in attempt_100
immune-timeline and for the jawless-vs-jawed evolutionary-split
discussion.

**Cross-subdir**: biology/evolution/ primary; persistent_organisms/
(adaptive-immunity origins).

---

### Alder 2005 🔍 (VLRA/VLRB, LRR-cassette diversity — PMID needs direct PubMed lookup)

**Alder MN, Rogozin IB, Iyer LM, Glazko GV, Cooper MD, Pancer Z.**
*Diversity and function of adaptive immune receptors in a jawless
vertebrate.*
**Science** 2005;310(5756):1970–1973.
**DOI: 10.1126/science.1119420**

⚠️ **Fire 34 AUDIT_LOG cited PMID 15890677** — WebSearch did not
directly return this PMID; the Science-volume-310 entry requires
PubMed direct-lookup confirmation. A later Alder 2008 *Nat Immunol*
paper PMID 18246071 on "Antibody responses of VLRs in lamprey" is
distinct from this 2005 *Science* paper. Per-run files citing
"Alder 2005" should verify PubMed confirms PMID 15890677 for the
Science paper; if not, flag as FM1c candidate.

**Use in corpus**: extension of Pancer 2004 — establishes **two
distinct VLR types (VLRA and VLRB)** in jawless vertebrates,
LRR-cassette combinatorial assembly, and structural distinctness
from jawed-vertebrate antibodies. Primary citation for the
"adaptive immunity evolved twice with different mechanisms"
framing.

**Cross-subdir**: biology/evolution/ primary.

---

## Queue (next fires if Task 6 continues)

Additional immune-timeline canonical references flagged at Fire 34:
- HLA allele count year-dating 40k vs 25k — needs specific citation
- Doherty-Zinkernagel heterozygote-advantage (1975 Nature Nobel work)
- ERV-syncytin papers (Mi 2000, Blaise 2003) — already cited inline
  at biology/evolution/gap.md v9.1 addendum

Per-organism attempt references (attempts 001-010) were WebSearch-
audited by prior /loop iteration at 52% verification rate; further
coverage is lower-priority.

## Audit history

- **2026-04-18 Fire 87**: Started file with 3 canonical evolutionary-
  immunology references. ⚠️ **Discovered that Fire 34 AUDIT_LOG cited
  wrong PMIDs for Hoffmann 1996 (8808625 → 8808632) and Pancer 2004
  (15241415 → 15241406)**. Both off by small digit-differences, but
  wrong PMIDs still fail PubMed lookup. Also identified **FM1d author-
  drift on "Hoffmann 1996"** — the first author is Lemaitre B; Hoffmann
  JA is senior/last author. This is the famous last-author-as-lab-PI
  pattern; the corrective form is "Lemaitre et al. 1996." **Recursive
  audit-layer drift pattern continues**: Fire 34 was itself a structural
  audit, its PMIDs were not WebSearch-verified at write-time, and 2/3
  sample are wrong. Validates the case study's recommendation that
  audit notes themselves are load-bearing content requiring PMID
  verification. Alder 2005 Fire-34-PMID flagged for direct PubMed
  verification (could not confirm via WebSearch this fire).
