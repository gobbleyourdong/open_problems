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
- Depletion **precedes** T1DM onset. ⚠ **CORRECTION (fire 5):** run_026 cited "DIABIMMUNE /
  Vatanen 2016 *Cell*" for this — but **Vatanen 2016 is the LPS-immunogenicity paper** (next
  bullet), *not* the Akkermansia-precedence source. The DIABIMMUNE T1D-progression paper is
  **Kostic 2015** *Cell Host Microbe* (≈25% diversity drop before seroconversion); Akkermansia-
  specific reductions trace to **de Goffau 2013** *Diabetes* + TEDDY (**Vatanen 2018 / Stewart
  2018** *Nature*). ☐ pull exact Akkermansia pre-seroconversion numbers next fire.
- **LPS immunogenicity — the *actual* Vatanen 2016 finding, and a direct P0 cross-link.** ✓
  Vatanen 2016 *Cell* 165:842-853: *Bacteroides*-dominant infants' **penta-acylated LPS is
  immuno-inhibitory** and fails to educate the infant immune system, vs *E. coli* **hexa-acylated
  LPS** (immunostimulatory, protective) — implicated in higher T1DM in Finnish/Estonian vs
  Russian-Karelian children. **⚠ Tension to resolve:** here hexa-LPS in *early life* is
  *protective* (immune education), whereas P0's framework treats **Hexa-LPS index 94** as
  chronically *pro-inflammatory* (TLR4/M1) in *adulthood*. Same molecule, opposite valence by
  life-stage — flagged for its own analysis (see [P0 baseline](results/p0_microbiome_baseline_2026-05-21.md)).
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

## 4. How It's Replenished — verified (fire 4)

> Ranked by evidence strength / P0-actionability. **Key distinction (links to §5 paradox):** the
> levers below raise Akkermansia *with* mucus support (goblet/mucin stimulation, polyphenol
> substrate) — a "good" rise — unlike the fiber-starvation bloom that erodes the barrier. Aim for
> abundance-*with*-fiber, not abundance alone.

- **Polyphenols** ✓ — the most reproducible dietary expander. Cranberry extract → ↑Akkermansia +
  protection from diet-induced obesity/insulin resistance/inflammation (**Anhê 2014 *Gut*** —
  *run_026 said "2015"; corrected*); Concord grape polyphenols → ↑A. muciniphila, attenuate HFD
  metabolic syndrome (Roopchand 2015 *Diabetes*). Also pomegranate ellagitannins, green tea.
  **→ P0: highest-yield, lowest-risk first move.**
- **Metformin** ✓ — ↑A. muciniphila + ↑mucin-producing **goblet cells**, improves glucose
  homeostasis in HFD mice; proposed as a mechanism of metformin's antidiabetic effect (Shin 2014
  *Gut*, PMID 23804561). Bidirectional goblet↔Akkermansia loop. (Not indicated for P0 absent T2DM.)
- **Pasteurized A. muciniphila supplement** ✓ — **10¹⁰ cells/day** (Depommier 2019; *not* the
  3.8×10¹⁰ run_026 stated). Pasteurized > live. The direct restoration route. **→ P0: run_026's
  second-tier add if barrier markers persist.**
- **Intermittent fasting** ✓ — Ramadan-style IF ↑A. muciniphila + Bacteroides fragilis group in
  humans (preliminary, PMC6924600); IF + Akkermansia potentiate FOLFOX antitumor efficacy (mouse).
- **ω-3 PUFA (EPA/DHA, fish oil)** ✓ — enhances mucin-niche / mucolytic species incl. Akkermansia;
  1-wk EPA/DHA supplementation modulates the human luminal mucin niche (PMC9481098). Modest/short-term.
- **Prebiotic fiber (inulin/FOS)** ⚠ — feeds the trophic chain; *and* (per §5 paradox) supplies the
  fiber that keeps Akkermansia's mucin use as turnover not erosion. ☐ dose-response.
- **HMOs in infancy** ✓ — A. muciniphila grows on human milk; breast-milk betaine ↑ neonatal
  Akkermansia (Sci Rep 2020; PMC8823629). *But* the feeding-type effect on **adult** Akkermansia is
  weak/conflicting (see P0 chain analysis — neonatal feeding is not the cause of P0's 0%).

---

## 5. How It's Destroyed — mostly verified (fire 3)

- **Broad-spectrum antibiotics** ✓ — Akkermansia is antibiotic-sensitive; **months to recover**;
  penicillin *selects for mutant variants* with compromised host-benefit function (PMC11804010,
  2025). **Likely the dominant driver of P0's 0%** given the elevated resistance signature.
- **Dietary emulsifiers** ✓ — carboxymethylcellulose (CMC) + polysorbate-80 (P80) at low doses →
  ↓microbiota–epithelium distance via **mucus degradation**, low-grade inflammation, metabolic
  syndrome (Chassaing 2015 *Nature* 519:92-96, PMID 25731162). Follow-up: emulsifiers **deplete
  Akkermansia**, and oral A. muciniphila *prevents* the CMC/P80 phenotype (hyperphagia, weight
  gain, dysglycemia) — so the relationship is causal *and* therapeutically reversible. ✓ (PMC10086484)
- **Alcohol** ✓ — ethanol → prominent decline in A. muciniphila; alcoholic-steatohepatitis
  patients have ↓ fecal Akkermansia; supplementation restores it and ↓gut leakiness + hepatic
  injury (Grander 2018, PMID 28550049). ✓
- **Western high-fat diet** ⚠ — high-fat feeding lowers Akkermansia in most rodent models. But
  the **low-fiber** half is *not* simple depletion — see the paradox below.

### ⚠ The Mucin Paradox — abundance and benefit decouple (resolves queue #5) ✓

Desai 2016 *Cell* (167(5):1339-53, PMID 27863247): under **dietary fiber deprivation**, the
microbiota switches to **mucus as an alternative carbon source** (↑CAZymes, sulfatases,
proteases), and mucin-degraders **including A. muciniphila proliferate** while the colonic mucus
barrier *erodes* → enhanced enteric-pathogen susceptibility (*C. rodentium*).

**Implication — two non-obvious consequences:**
1. **More Akkermansia is not always good.** In fiber-starvation it can *rise in abundance while
   the mucus layer thins*. Abundance ≠ barrier benefit; the benefit is fiber-context-dependent.
2. **Bears directly on P0's chain.** "Zero Akkermansia → thin mucus" is too simple in both
   directions: you can have *thin mucus with high Akkermansia* (fiber-starved) — so neither
   Akkermansia level nor mucus thickness cleanly predicts the other. The barrier outcome depends
   on **fiber availability gating what Akkermansia does to mucin** (degrade-and-erode vs
   degrade-and-turn-over). Reconciles with run_026's "net turnover maintained" — that holds only
   *with adequate fiber*.

---

## 6. Strain-Level Structure — phylogroups (fire 5) ✓

"Akkermansia muciniphila" is not one organism. Human isolates split into **four species-level
phylogroups — AmI, AmII, AmIII, AmIV** (AmI further → AmIa/AmIb) (Becken/Guo 2021 *mBio*, PMID 34006653):

| Phylogroup | Prevalence (n=1617 human fecal) | Notable traits |
|------------|-------------------------------|----------------|
| **AmI** (incl. type strain MucT) | **47%** (most common) | smaller genomes; **lacks B12 synthesis genes**; in humans + mice |
| **AmII** | 27% | larger genome; **synthesizes corrin rings → vitamin B12** (outcompetes when B12 precursors scarce); defective assimilatory sulfate reduction; **human-only** |
| **AmIII** | 24% | KEGG-similar to AmII; **human-only** |
| **AmIV** | rare | larger genome; defective assimilatory sulfate reduction; humans + mice |

Genomes span **2.6–3.3 Mb**. The phylogroups differ in **intestinal abundance, metabolism,
physicochemical properties, and immune-activation capacity** — meaning two people both "positive
for A. muciniphila" can carry functionally different organisms.

**Why this matters for P0 / the framework:** "Akkermansia 0%" on a genus-level dashboard erases
this structure. If/when restoration is attempted, *which phylogroup* colonizes may matter (B12
production, sulfate handling, immune activation differ). ☐ Open: are specific phylogroups more
barrier-protective / more Amuc_1100-active? Not yet resolved in the literature.

---

## Verification queue

1. ✓ §2 primaries — Plovier 2017, Depommier 2019, Routy 2018 verified (fire 2; 3 run_026 errors fixed).
   Vatanen 2016 audited (fire 5): it is the **LPS-immunogenicity** paper, *mis-cited* in run_026 for
   Akkermansia precedence. ☐ remaining: **Kostic 2015 / de Goffau 2013 / TEDDY** exact Akkermansia
   pre-seroconversion numbers; the **2026 *Nat Med*** RCT; resolve the **hexa-LPS life-stage valence** tension.
2. ✓ §4 — polyphenols (Anhê 2014/Roopchand 2015), metformin (Shin 2014), IF, ω-3, supplement verified (fire 4).
   ☐ remaining: inulin/FOS dose-response, next-gen probiotic regulatory status.
3. ✓ §5 — antibiotics, emulsifiers (Chassaing 2015), alcohol (Grander 2018) verified (fire 3).
   ☐ remaining: bile acids, age-related decline.
4. ✓ Strain-level phylogroups AmI–AmIV documented (§6, fire 5). ☐ open: which phylogroup is most barrier-protective / Amuc_1100-active?
5. ✓ The mucin paradox resolved (fire 3, Desai 2016): abundance ≠ benefit; fiber gates degrade-and-erode vs degrade-and-turn-over.

---

*Fire 1 (2026-05-21): established doc; §1 Identity and §3 Evolution fully source-verified;
§2/§4/§5 seeded from run_026 + campaign searches with verification flags. /loop job 3d2d841d.*
*Fire 2 (2026-05-21): §2 hardened — Plovier 2017 (Nat Med, TLR2/claudin-3/occludin + 5-HT bonus),
Depommier 2019 (n=32 pilot, 10¹⁰/day, pasteurized>live), Routy 2018 (anti-PD-1, IL-12) verified;
fixed 3 citation/dose errors in run_026. Vatanen 2016 + 2026 RCT queued.*
*Fire 3 (2026-05-21): §5 Destruction verified — antibiotics, emulsifiers (Chassaing 2015),
alcohol (Grander 2018); resolved the mucin paradox (Desai 2016) — abundance ≠ barrier benefit,
fiber-gated — which complicates P0's "zero Akker → thin mucus" link in both directions.*
*Fire 4 (2026-05-21): §4 Replenishment verified + evidence-ranked — polyphenols (Anhê 2014 Gut,
corrected from "2015"; Roopchand 2015), metformin (Shin 2014, goblet-cell loop), IF, ω-3,
pasteurized supplement (10¹⁰/day). P0 first move = polyphenols. 4th run_026 citation fix.*
*Fire 5 (2026-05-21): §6 strain phylogroups AmI–AmIV added (Becken/Guo 2021 mBio). 5th run_026
fix — biggest yet: Vatanen 2016 Cell is the LPS-immunogenicity paper, MIS-CITED for Akkermansia
T1DM-precedence (→ Kostic 2015 / de Goffau / TEDDY). Surfaced hexa-LPS life-stage valence tension
(protective in infancy vs P0's pro-inflammatory Hexa-LPS 94 in adulthood).*

### Sources (fire 5)
- [Vatanen 2016 — variation in microbiome LPS immunogenicity contributes to autoimmunity, Cell](https://www.cell.com/cell/fulltext/S0092-8674(16)30493-7)
- [Kostic 2015 — DIABIMMUNE: infant gut microbiome dynamics & progression to T1D, Cell Host Microbe](https://www.cell.com/cell-host-microbe/fulltext/S1931-3128(15)00021-9)
- [Vatanen 2018 — gut microbiome in early-onset T1D, TEDDY study, Nature](https://www.nature.com/articles/s41586-018-0620-2)
- [Becken/Guo 2021 — genotypic & phenotypic diversity of human A. muciniphila isolates (phylogroups), mBio (PMID 34006653)](https://pubmed.ncbi.nlm.nih.gov/34006653/)

### Sources (fire 4)
- [Anhê 2014 — cranberry polyphenol ↑Akkermansia, anti-obesity, Gut](https://www.researchgate.net/publication/264390771)
- [Roopchand 2015 — grape polyphenols ↑A. muciniphila, attenuate HFD metabolic syndrome, Diabetes (PMC4512228)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4512228/)
- [Shin 2014 — metformin ↑Akkermansia + goblet cells, glucose homeostasis, Gut (PMID 23804561)](https://pubmed.ncbi.nlm.nih.gov/23804561/)
- [Islamic intermittent fasting ↑A. muciniphila (PMC6924600)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6924600/)
- [ω-3 EPA/DHA modulates human luminal mucin niche incl. Akkermansia (PMC9481098)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9481098/)
- [Dietary strategies to promote Akkermansia — review (PMC6223323)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6223323/)

### Sources (fire 3)
- [Chassaing 2015 — dietary emulsifiers, microbiota, colitis/metabolic syndrome, Nature (PMID 25731162)](https://www.nature.com/articles/nature14232)
- [A. muciniphila counteracts emulsifier (CMC/P80) harm (PMC10086484)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10086484/)
- [Desai 2016 — fiber-deprived microbiota degrades colonic mucus barrier, Cell (PMID 27863247)](https://pubmed.ncbi.nlm.nih.gov/27863247/)
- [Grander 2018 — recovery of ethanol-induced Akkermansia depletion ameliorates ALD (PMID 28550049)](https://pubmed.ncbi.nlm.nih.gov/28550049/)

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
