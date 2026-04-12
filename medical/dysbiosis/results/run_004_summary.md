# Run 004 Summary
## Numerical Instance | 2026-04-11 | Phase 1

---

## What Was Produced

Three files in `numerics/`:
1. `run_004_m3_ifn_test_design.md` — IFN-α2 Simoa assay design; CXCL10 screen → Simoa → ISG panel cascade
2. `run_004_fastq_analysis_protocol.md` — Complete Kraken2+Bracken+HUMAnN3 pipeline; DGX Spark optimized
3. `run_004_phageome_and_gut_permeability.md` — CrAssphage dynamics; zonulin invalidated; L:M ratio as replacement

---

## High-Signal Outputs

### Finding 1: The zonulin kill — M1 kill matrix P1.2 revised

Kill matrix Run 001 scored P1.2 (zonulin correlates with dysbiosis) as 2 FOR / 2 AGAINST due to "marker controversy." Now formally resolved: the commercial Immundiagnostik kit measures complement C3, not zonulin protein. Any study using that kit for "leaky gut" is measuring inflammation activity, not permeability specifically.

**Update to kill matrix:** P1.2 evidence AGAINST = 3/3 (marker is invalid). Reframe as: "gut permeability correlates with systemic disease" (the underlying biology) — evidence FOR: L:M ratio studies, FABP2 in acute gut injury. Prediction stands; the assay was wrong.

**Practical:** don't order zonulin from functional medicine lab panels that use Immundiagnostik kit. Use Genova L:M ratio or FABP2+LBP blood panel instead.

### Finding 2: FASTQ pipeline directly runnable on DGX Spark

The DGX has 128GB RAM — the entire k2_standard database (80-90GB) fits in RAM, giving ~5× faster Kraken2 classification vs disk-based. Full pipeline: ~2-4 hours on DGX vs ~12-24h on standard laptop.

**Most important FASTQ read:** F. prausnitzii relative abundance is the single highest-value data point from the TinyHealth analysis. It's the convergence point of Node A (Treg proxy) in T-index v2.

**Phage addition:** with Kraken2's viral database included, CrAssphage reads are extractable from the same FASTQ without additional wet lab work. This is bonus data most TinyHealth users never look at.

### Finding 3: CVB monitoring protocol now complete

With the IFN-α2 Simoa assay design:
- Baseline Simoa before CVB protocol start → document starting IFN-α2 level
- 6-month repeat → if declining: antiviral component working
- 12-month repeat → trend confirmation

This turns a blind protocol into a monitored antiviral intervention. Cost: ~$150-300/timepoint. The delta (change over time) is more informative than a single snapshot.

**Sequence: CXCL10 first (cheap screen, ~$50), then Simoa if elevated (~$150-300).** If CXCL10 is normal, chronic IFN response is probably absent — skip Simoa.

### Finding 4: CrAssphage as bonus phageome proxy

TinyHealth shotgun can give partial phageome visibility at no additional cost — just run the reads through Kraken2 with viral sequences in the database. CrAssphage presence/absence reflects Bacteroides density regulation. This is a proxy for gut phageome health that no other consumer test provides.

---

## Space Map — Current Status (After 4 Runs)

```
MOUNTAIN    STATUS      FILES PRODUCED             OPEN ITEMS
  M1        PARTIAL     Kill matrix, gut-skin axis  Zonulin corrected → L:M ratio
                        permeability landscape       IFN not M1 (CVB only)
  M2        VALIDATED   Kill matrix                 20-25% monotherapy non-responders → M4
  M3        PARTIAL     Detection stack, IFN panel  IFN monitoring protocol designed
                        CVB-T1DM sky bridge          
  M4        FRONTIER    Proxy survey, T-index v2    Validation study designed; zinc×D critical
                        Interaction analysis
  M5        VALIDATED   Kill matrix                 No new items
  M6        VALIDATED   Kill matrix                 No new items
  M7 (new)  FRONTIER    Mountain 7 file             TLR2 gap in protocol; chlorhexidine addition
  DAO       DESIGNED    Kill test protocol          Not yet run
```

---

## Test Priority Ranking (Cheapest → Most Expensive, Highest Signal)

| Priority | Test | Cost | Mountain | Actionability |
|----------|------|------|----------|---------------|
| 1 | DAO serum activity | $100-200 | Gut-skin, M4 | Immediate if low: supplement + diet |
| 2 | Serum zinc | $20-40 | M4 (D×zinc) | Immediate if low: zinc supplement |
| 3 | CXCL10 serum (IP-10) | $50-100 | M3 CVB proxy | If elevated → Simoa next |
| 4 | 25-OH-D (if not recent) | $30-60 | M4 proxy | Confirm >60 ng/mL |
| 5 | F.prausnitzii + Akkermansia (TinyHealth FASTQ) | already ordered | M4 (Node A) | High-fiber diet, tributyrin |
| 6 | hsCRP (if not recent) | $10-30 | M4 (Node B) | Confirm chronic inflammation state |
| 7 | Gut permeability (L:M ratio, Genova) | $150-200 | M1 | If elevated: barrier repair |
| 8 | IFN-α2 Simoa | $150-300 | M3 | If elevated: CVB protocol validated |
| 9 | NOD2/TLR4 genotype (23andMe or WGS) | $100-500 | M4 genetic floor | Permanent; informs D×F.prausnitzii interaction |
| 10 | Treg % (flow cytometry) | $200-500 | M4 (Node A direct) | Rare, specialty lab |

---

## Noise Items — Still Pending

- **Butyrate pathway genes (HUMAnN3):** Run 004 FASTQ pipeline includes it, but haven't mapped expected results or interpretation against published gut microbiome literature in cancer/IBD. Flag for Run 005 or theory instance.
- **SCFA plasma concentrations (acetate/propionate):** butyrate mostly consumed by colonocytes, but acetate reaches systemic circulation. What are the actual published reference ranges for plasma acetate/propionate in dysbiosis conditions? Not mapped.
- **Omega-3 index vs EPA/DHA supplementation dose:** what supplementation dose achieves >8% omega-3 index? How long? Not computed.
- **Mountain 7 + T1DM Th17 connection:** P. gingivalis Th17 induction specifically in context of islet inflammation — is there published data? Flagged as potentially important but not explored.

---

## Diminishing Returns Assessment (Phase 1 Numerics Status)

After 4 runs, assessing whether Phase 1 is approaching completion:

**Well-covered (>80% of useful maps drawn):**
- Kill matrix across M1-M6 ✓
- Biomarker landscape by tier ✓
- Mountain kill ROI scoring ✓
- M4 proxy survey + T-index v2 ✓
- CVB detection stack ✓
- Gut-skin axis mechanism tree ✓
- Gut permeability assay landscape ✓
- FASTQ analysis protocol ✓
- IFN-α monitoring design ✓
- DAO kill test design ✓
- Mountain 7 (oral) ✓

**Remaining useful territory:**
- SCFA plasma reference ranges (Run 005)
- Omega-3 dose-response for omega-3 index target (Run 005)
- Mountain 7 Th17-T1DM intersection (Run 005)
- Attempt design documents (format ready for theory to use)

**Phase 1 completion estimate:** ~75-80%. One more run (005) should reach diminishing returns threshold.

---
*Run 004 complete. Zonulin invalidated (C3 artifact). IFN monitoring protocol designed. FASTQ pipeline ready for DGX. Test priority table constructed. Phase 1 ~75-80% complete: 1-2 more runs to reach theory-handoff threshold.*
