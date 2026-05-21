# Akkermansia muciniphila — Source-Audited Monograph

> Living reference doc, built by a /loop campaign (job 3d2d841d, started 2026-05-21).
> Goal: know *everything* about Akkermansia — identity, why it matters, how it evolved,
> how it's replenished, how it's destroyed — with every claim audited against primary sources.
> Motivated by P0's baseline: **Akkermansia 0%** (see [P0 baseline](results/p0_microbiome_baseline_2026-05-21.md)).
> Extends the mechanism work in [run_026](numerics/run_026_akkermansia_muciniphila.md).

**Verification legend:** ✓ verified against primary/secondary source this campaign ·
⚠ asserted in internal run_026, primary source not yet re-pulled · ☐ queued for verification.

---

## 1. Identity & Biology ✓ (fire 1)

| Property | Value | Source |
|----------|-------|--------|
| Discovered | 2004, Muriel Derrien & Willem de Vos, Wageningen Univ. (NL) | ✓ IJSEM 2004 |
| Type strain | **MucT** (= ATCC BAA-835 = CIP 107961) | ✓ |
| Phylum | **Verrucomicrobiota** (PVC superphylum: Planctomycetes–Verrucomicrobia–Chlamydiae) | ✓ |
| Morphology | Gram-negative, strictly anaerobic, non-motile, non-spore-forming, oval; grows singly/in pairs; forms a capsule and aggregates on mucin | ✓ |
| Isolation | Dilution-to-extinction of feces in anaerobic medium with **gastric mucin as sole C + N source** | ✓ |
| Substrate range | Mucin (preferred); limited sugars (N-acetylglucosamine, N-acetylgalactosamine, glucose) only with a protein source, at lower rate/density than on mucin | ✓ |
| Genome | Single circular chromosome **2.66 Mbp**; only ~29% gene overlap with closest Verrucomicrobia relatives (deeply branched) | ✓ |
| Abundance | "Abundant resident" of the human gut — typically **~1–4%** of fecal microbiota in healthy adults | ✓ |
| Niche | Lives *in the mucus layer* between lumen and epithelium — a structurally privileged position | ⚠ run_026 |

**One-line essence:** a deeply-branched, mucin-specialist anaerobe that lives in the mucus
layer and eats the host's own mucin glycoproteins as its primary carbon/nitrogen source.

---

## 2. Why It Matters ⚠/☐ (carried from run_026; primary re-verification queued)

Three independent mechanistic paths (detail in [run_026](numerics/run_026_akkermansia_muciniphila.md)):

1. **Amuc_1100 → TLR2 → barrier.** Outer-membrane protein Amuc_1100 signals through TLR2 →
   tight-junction upregulation (ZO-1, occludin, claudin-3) → tighter barrier, less portal LPS.
   Heat-stable → **pasteurized** Akkermansia retains the effect. ⚠ (Plovier 2017 *Nat Microbiol* — ☐ re-verify)
2. **Trophic chain → F. prausnitzii → butyrate.** Akkermansia degrades MUC2 → releases mucin
   oligosaccharides → cross-feeds F. prausnitzii (which can't process intact mucin) → butyrate →
   Foxp3/VDR (Treg) axis. ⚠
3. **Physical mucus barrier.** Net mucus *turnover* maintained (stimulates goblet MUC2) → keeps
   luminal bacteria physically distant from epithelium. ⚠

**Disease associations (☐ each PMID to re-verify):**
- Depleted in T1DM, obesity, IBD, rosacea, psoriasis.
- Depletion **precedes** T1DM onset (DIABIMMUNE / Vatanen 2016 *Cell*). ⚠
- Only gut bacterium besides F. prausnitzii with **human RCT** evidence in metabolic disease:
  pasteurized A. muciniphila 3.8×10¹⁰/day × 3 mo → ↑insulin sensitivity, ↓permeability markers
  (Depommier 2019 *Nat Med*). ⚠
- ☐ **Cancer immunotherapy:** Akkermansia abundance associated with anti-PD-1 response
  (Routy 2018 *Science*) — verify in a later fire.

---

## 3. Evolution & Phylogeny ✓ (fire 1)

- **Ancient lineage.** Verrucomicrobiota is a deeply-branched phylum; Akkermansia sits on a
  deep branch (only ~29% gene overlap with nearest relatives). ✓
- **Mucin degradation is the ancestral innovation.** It's the founding adaptation of the genus —
  the trait that let Akkermansia colonize the vertebrate mucosal niche as a symbiont. ✓
  (PMC10540074 "early evolutionary adaptations… to the vertebrate gut"; Tandfonline 2021
  "evolution and competitive strategies")
- **Conserved mucin machinery across mammals.** ~75 of 78 mucin-degradation genes are conserved
  across genomes from different mammalian hosts → low genomic divergence → Akkermansia favors the
  mucosal niche *independent of host species*. ✓
- **Enzymatic arsenal.** Type-strain genome encodes **61 secreted proteins** predicted for mucin
  degradation; glycoside-hydrolase content tracks the phylogeny — deepest branches carry 2 copies
  of family **GH84**, recently diverged lineages 0–1. ✓ (a clean evolutionary signal)
- **Horizontal gene transfer.** HGT detected, mostly from other Gram-negative gut bacteria or
  unknown sources — consistent with niche adaptation. ✓

**Evolutionary read:** Akkermansia is an old mucosa specialist whose entire competitive strategy
is built on hydrolyzing host mucin. The conservation of its mucin toolkit across mammals says the
host–symbiont relationship is deep and stable — this isn't a recent or facultative gut tourist.

---

## 4. How It's Replenished ✓ partial (fire 1 — to deepen)

- **Polyphenols** — cranberry, pomegranate (ellagitannins), grape seed, green tea; the most
  reproducible dietary expander (Anhê 2015). ✓ (PMC6223323 dietary-strategies review)
- **Prebiotic fiber** — inulin/FOS feed the trophic chain (mucin synthesis needs galactose
  precursors). ⚠ run_026 (☐ confirm dose-response)
- **Pasteurized A. muciniphila supplement** — Depommier 2019 dose (3.8×10¹⁰/day). ⚠
- **Metformin** raises Akkermansia (recurring finding; mechanism ☐).
- **HMOs in infancy** — A. muciniphila grows on human milk, expresses glycan-degrading enzymes;
  betaine in breast milk ↑ neonatal Akkermansia. ✓ (Sci Rep 2020; PMC8823629) — *but* feeding-type
  effect on adult Akkermansia is weak/conflicting (see P0 chain analysis).
- ☐ Caloric restriction / fasting, fish oil / omega-3 — queued.

---

## 5. How It's Destroyed ✓ partial (fire 1 — to deepen)

- **Broad-spectrum antibiotics** — Akkermansia is antibiotic-sensitive; **takes months to
  recover**; penicillin *selects for mutant variants* with compromised host-benefit function. ✓
  (PMC11804010, 2025) — **likely the dominant driver of P0's 0%** given the elevated resistance signature.
- **Western diet** (high-fat / low-fiber) — substrate starvation + mucus changes. ⚠ (☐ primary)
- ☐ **Alcohol** — reported to lower Akkermansia (verify; Grander 2018?).
- ☐ **Emulsifiers** (carboxymethylcellulose, polysorbate-80) — mucus/microbiota disruption
  (Chassaing 2015?) — verify.

---

## Verification queue (next fires)

1. ☐ Re-pull primary sources for §2 (Plovier 2017, Depommier 2019, Vatanen 2016, Routy 2018) — exact numbers + journals.
2. ☐ §4 deepen: fasting/CR, omega-3, inulin dose-response, NEXT-GEN probiotic regulatory status.
3. ☐ §5 deepen: alcohol, emulsifiers, bile acids, age-related decline — with primary sources.
4. ☐ Strain-level: Akkermansia phylogroups (AmI–AmIV); are some more barrier-protective?
5. ☐ The mucin paradox: when does mucin degradation *thin* vs *thicken* the layer? (fiber-dependence)

---

*Fire 1 (2026-05-21): established doc; §1 Identity and §3 Evolution fully source-verified;
§2/§4/§5 seeded from run_026 + campaign searches with verification flags. /loop job 3d2d841d.*

### Sources (fire 1)
- [A. muciniphila gen. nov. — IJSEM 2004 (Derrien)](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.02873-0)
- [The mucin degrader A. muciniphila is an abundant resident (PMC2258631)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2258631/)
- [Genome of A. muciniphila, dedicated mucin degrader (PMC3048395)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3048395/)
- [Early evolutionary adaptations to the vertebrate gut (PMC10540074)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10540074/)
- [Evolution and competitive strategies of A. muciniphila (PMC8920140)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8920140/)
- [A. muciniphila: biology, ecology, host interactions (Nat Rev Microbiol 2024)](https://www.nature.com/articles/s41579-024-01106-1)
- [Dietary strategies to promote Akkermansia (PMC6223323)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6223323/)
- [Antibiotic-associated changes in Akkermansia (PMC11804010)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11804010/)
- [Akkermansia uses HMOs in early life (Sci Rep 2020)](https://www.nature.com/articles/s41598-020-71113-8)
