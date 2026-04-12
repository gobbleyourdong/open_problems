# Run 003 Summary + TinyHealth Shotgun Update
## Numerical Instance | 2026-04-11 | Phase 1

---

## What Was Produced

Three numerical files in `numerics/`:
1. `run_003_t_index_interactions.md` — T-index v2 (network-aware): zinc×D interaction is critical; two convergence nodes identified
2. `run_003_mountain7_oral_microbiome.md` — Mountain 7 validated; TLR2 gap in current protocol
3. `run_003_dao_histamine_kill_test.md` — Complete kill test protocol, ~$150-250, highest ROI/cost in portfolio

---

## TinyHealth Shotgun Metagenomics — Revised Assessment

**User update:** TinyHealth uses shotgun metagenomics, not 16S amplicon.

**This changes the picture:**

| What shotgun metagenomics CAN give | Relevance |
|------------------------------------|-----------|
| Species-level (not just genus) bacterial resolution | F. prausnitzii species-level confidence ↑ |
| Functional gene catalog (butyryl-CoA transferase, etc.) | Can check if butyrate production GENES present, not just organism |
| Akkermansia muciniphila species-level | More reliable than 16S |
| Bacteriophage DNA reads (CrAssphage, etc.) | Phageome partially visible — no other consumer test does this |
| Fungal reads (Malassezia, Candida) | Small fraction but detectable |

| What shotgun metagenomics CANNOT give (CVB question) | Why |
|-----------------------------------------------------|-----|
| CVB (RNA virus) detection | Shotgun DNA sequencing misses RNA viruses; CVB = +ssRNA, no DNA form, doesn't integrate |
| 5'UTR-deleted persistent CVB | Even if RNA step added: this form is in ISLETS, not shed to stool at detectable levels |
| Integrated lysogenic phage activity | Requires metatranscriptomics (RNA-seq) |

**CVB in FASTQ conclusion:** CVB is unlikely to be in the TinyHealth FASTQ. The persistent form is:
1. RNA-based (shotgun DNA sequencing misses it)
2. Located in pancreatic islets (not gut lumen, not stool)
3. At very low copy numbers even in tissue

**What TO look for in the FASTQ when processed:**
- F. prausnitzii relative abundance + functional butyrate genes
- Akkermansia muciniphila abundance
- Proteobacteria bloom indicator (elevated Proteobacteria % = gut dysbiosis severity marker)
- Firmicutes:Bacteroidetes ratio (less meaningful at genus level; shotgun gives species detail)
- CrAssphage presence (proxy for Bacteroides phage balance — indicator of phageome state)
- Candida/Malassezia reads (small but informative for fungal load)
- Histamine-producing bacteria: Morganella morganii, Klebsiella pneumoniae — relevant for DAO kill test

**Actionable FASTQ checklist** (to apply when FASTQ is processed):
```
□ F. prausnitzii: relative abundance >5% = OK; <1% = concerning; 0% = depleted
□ Akkermansia muciniphila: any detection = OK; absent = gut barrier risk
□ Proteobacteria %: <10% = normal; >20% = significant dysbiosis
□ Morganella morganii / Klebsiella / histamine-producers: present = check DAO
□ CrAssphage reads: present = baseline phageome visible
□ Candida: present at >0.1% = fungal overgrowth candidate
```

---

## High-Signal Outputs

### Finding 1: Zinc × Vitamin D is the most critical interaction

The T-index v1 (Run 002) listed zinc and vitamin D as separate components. Run 003 reveals they're not independent: zinc is required for VDR (vitamin D receptor) function because VDR has a zinc finger DNA-binding domain. Low zinc → VDR can't bind DNA → vitamin D supplementation has reduced efficacy even when serum 25-OH-D looks normal.

**Protocol gap:** supplementing D3 without monitoring zinc. Zinc should be checked BEFORE interpreting D levels.

**Check:** are zinc levels being monitored on the CVB protocol? If not, add serum zinc to next bloodwork.

### Finding 2: Mountain 7 (oral dysbiosis) is a real gap

The oral microbiome isn't a gap in the literature — it's a gap in the current intervention model. P. gingivalis activates TLR2 (not TLR4), produces Th17-skewed inflammation, and citrullinates host proteins. The CVB protocol targets NF-κB (primarily downstream of TLR4) but does NOT address TLR2-mediated Th17 activation from oral P. gingivalis.

Given user's multi-site dysbiosis (T1DM, seb derm, rosacea-spectrum, chalazion), P. gingivalis oral load is worth checking. This is a cheap intervention addition: chlorhexidine rinse + professional scaling + xylitol.

**The Th17 connection:** T1DM pathogenesis involves Th17 cells. P. gingivalis specifically drives Th17. If oral dysbiosis is active, it may be contributing to islet inflammation via Th17 independently of CVB.

### Finding 3: DAO kill test is the highest ROI/cost action available

- Cost: ~$150-250 total
- Time: 4-6 weeks
- Outcome: either confirms histamine axis (→ adds cheap daily intervention) or excludes it (→ nothing to do)
- Relevant for: rosacea flushing specifically; could also benefit histamine-driven skin symptoms broadly

This is the best positioned "cheap kill" in the portfolio. The expensive, hard tests (M4 threshold measurement, CVB virome sequencing) are for when cheap options are exhausted.

---

## Emerging Pattern: The Protocol Covers TLR4, Misses TLR2

The CVB protocol:
- OSBP block → CVB replication (viral entry)
- NLRP3 inhibition → inflammasome (downstream of multiple TLRs)
- NF-κB suppression → primary downstream of TLR4
- Autophagy → viral clearance

**What it misses:**
- TLR2 → MyD88 → MAPK/AP-1 pathway (P. gingivalis oral, gut P. gingivalis seeding)
- TLR2 → Th17 commitment (IL-6 + TGF-β → RORγt → Th17)
- DAO pathway (histamine-producing bacteria → flushing)

The protocol is TLR4/NF-κB-centric. Mountain 7 (oral P. gingivalis) and the histamine axis are orthogonal gaps.

**Mountain 7 addition to address TLR2:**
- Chlorhexidine rinse: directly reduces P. gingivalis load
- Professional scaling: removes biofilm where P. gingivalis resides
- These are cheap and non-systemic

---

## Space Map Status

```
MOUNTAIN    STATUS      NUMERICS COMPLETE    KILL TESTS DESIGNED
  M1        PARTIAL     Kill matrix ✓         No new kill test needed (gut FMT is the test)
  M2        VALIDATED   Kill matrix ✓         Monotherapy response = existing kill test
  M3        PARTIAL     Detection stack ✓     IFN-α signature test (not yet designed)
  M4        FRONTIER    Proxy survey ✓        T-index validation study (designed not run)
  M5        VALIDATED   Kill matrix ✓         Low-GI diet trial (existing)
  M6        VALIDATED   Kill matrix ✓         Pediatric cohort studies (existing)
  M7 (new)  FRONTIER    Mountain 7 file ✓     Chlorhexidine + P.gingivalis testing (cheap)
  DAO       UNADDRESSED Kill test ✓           DAO assay + diet challenge (designed, not run)
```

---

## Run 004 Targets

1. **M3 IFN-α test design** — design the blood panel that proxies CVB persistence best
2. **T-index validation study design** — what's the minimal protocol to validate T-index v2?
3. **FASTQ actionable analysis protocol** — write the bioinformatics steps to extract the 6 key metrics from TinyHealth FASTQ when available
4. **Phageome** — Run 002 noise item still unaddressed; CrAssphage and phage dynamics as precision intervention candidates
5. **L:M ratio vs zonulin** — gut permeability assay landscape (Run 001 noise, still pending)

---
*Run 003 complete. Key updates: TinyHealth shotgun confirms F.prausnitzii/Akkermansia visibility + phageome partial + no CVB. Mountain 7 added to framework. DAO kill test designed. Critical protocol gap: zinc not monitored; TLR2 (oral) not addressed.*
