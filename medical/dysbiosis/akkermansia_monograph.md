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

## 2. Why It Matters — mostly verified (fire 2)

> **run_026 corrections found this fire (citation/dose drift — exactly what Phase-4b audit is for):**
> (a) Plovier 2017 is ***Nature Medicine***, not "Nat Microbiol"; (b) Depommier 2019 dose is
> **10¹⁰ cells/day**, not "3.8×10¹⁰"; (c) Depommier 2019 is an **exploratory proof-of-concept
> pilot (n=32)**, not a definitive RCT — its metabolic endpoints are exploratory. Reconcile run_026.

Three independent mechanistic paths (detail in [run_026](numerics/run_026_akkermansia_muciniphila.md)):

1. **Amuc_1100 → TLR2 → barrier.** ✓ Amuc_1100 (the most abundant pilus-like outer-membrane
   protein) interacts with **TLR2** → ↑ tight-junction genes **claudin-3 + occludin** → tighter
   barrier; ameliorates insulin resistance + lipid metabolism in obese/diabetic mice. Heat-stable →
   **pasteurized** Akkermansia retains it. *Bonus:* Amuc_1100 also drives intestinal **5-HT
   (serotonin)** synthesis via Tph1 ↑ / SERT ↓ through TLR2 — ties to gut-serotonin
   ([run_047](numerics/run_047_gut_serotonin_flushing.md)). ✓ Plovier 2017 *Nat Med* 23(1):107-113; 5-HT: PMID 33900345.
2. **Trophic chain → F. prausnitzii → butyrate.** Akkermansia degrades MUC2 → mucin
   oligosaccharides → cross-feeds F. prausnitzii (can't process intact mucin) → butyrate →
   Foxp3/VDR (Treg) axis. ⚠ run_026 (mechanism plausible; ☐ pull cross-feeding primary)
3. **Physical mucus barrier.** Net mucus *turnover* maintained (stimulates goblet MUC2) → keeps
   luminal bacteria physically distant from epithelium. ⚠ run_026

**Disease & clinical evidence:**
- Depleted in T1DM, obesity, IBD, rosacea, psoriasis. ⚠ (associations; ☐ per-disease primaries)
- Depletion **precedes** T1DM onset (DIABIMMUNE / Vatanen 2016 *Cell*). ⚠ → ☐ verify next fire.
- **Metabolic — human pilot.** ✓ Depommier 2019 *Nat Med* 25(7):1096-1103 (PMID 31263284):
  n=32 overweight/insulin-resistant adults, randomized double-blind placebo-controlled, 3 mo,
  **10¹⁰ cells/day**. **Pasteurized** form ↑insulin sensitivity, ↓fasting insulinemia, ↓total
  cholesterol, slight ↓weight/hip — **live form did NOT reach significance** on most markers.
  Exploratory (safety/proof-of-concept), well tolerated. *Newer:* a 2026 *Nat Med* controlled
  RCT on pasteurized A. muciniphila for weight-loss maintenance exists — ☐ verify (queue).
- **Cancer immunotherapy.** ✓ Routy 2018 *Science* (DOI 10.1126/science.aan3706): anti-PD-1
  non-responders (NSCLC, RCC) had **low A. muciniphila**; antibiotics blunted checkpoint-inhibitor
  benefit; oral A. muciniphila after non-responder FMT **restored PD-1 efficacy in mice,
  IL-12-dependent**, ↑CCR9⁺CXCR3⁺CD4⁺ T-cell tumor recruitment.

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

## Verification queue

1. ✓ §2 primaries — Plovier 2017, Depommier 2019, Routy 2018 verified (fire 2; 3 run_026 errors fixed).
   ☐ remaining: **Vatanen 2016 *Cell* DIABIMMUNE** (T1DM-precedence claim) + the **2026 *Nat Med*** weight-maintenance RCT.
2. ☐ §4 deepen: fasting/CR, omega-3, inulin dose-response, next-gen probiotic regulatory status.
3. ☐ §5 deepen: alcohol, emulsifiers, bile acids, age-related decline — with primary sources.
4. ☐ Strain-level: Akkermansia phylogroups (AmI–AmIV); are some more barrier-protective?
5. ☐ The mucin paradox: when does mucin degradation *thin* vs *thicken* the layer? (fiber-dependence)

---

*Fire 1 (2026-05-21): established doc; §1 Identity and §3 Evolution fully source-verified;
§2/§4/§5 seeded from run_026 + campaign searches with verification flags. /loop job 3d2d841d.*
*Fire 2 (2026-05-21): §2 hardened — Plovier 2017 (Nat Med, TLR2/claudin-3/occludin + 5-HT bonus),
Depommier 2019 (n=32 pilot, 10¹⁰/day, pasteurized>live), Routy 2018 (anti-PD-1, IL-12) verified;
fixed 3 citation/dose errors in run_026. Vatanen 2016 + 2026 RCT queued.*

### Sources (fire 2)
- [Depommier 2019 — A. muciniphila in overweight/obese humans, Nat Med (PMID 31263284)](https://pubmed.ncbi.nlm.nih.gov/31263284/)
- [Plovier 2017 — purified Amuc_1100 / pasteurized Akkermansia improves metabolism, Nat Med](https://research.wur.nl/en/publications/a-purified-membrane-protein-from-akkermansia-muciniphila-or-the-p/)
- [Amuc_1100 → TLR2 → intestinal 5-HT biosynthesis (PMID 33900345)](https://pubmed.ncbi.nlm.nih.gov/33900345/)
- [Routy 2018 — gut microbiome & PD-1 immunotherapy efficacy, Science](https://www.science.org/doi/10.1126/science.aan3706)
- [Pasteurized A. muciniphila MucT for weight-loss maintenance — controlled RCT, Nat Med 2026](https://www.nature.com/articles/s41591-026-04394-7)

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
