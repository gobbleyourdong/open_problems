# attempt_108 — Trained Immunity: Memory in the Innate Layer

> Extension to the 100-series after the main sweep (100-107) closed.
> The innate-adaptive dichotomy, as presented in the earlier attempts,
> treats memory as an adaptive-lineage feature. This attempt
> documents an active research frontier where that framing is
> partially wrong: innate immune cells (monocytes, NK cells, ILCs)
> can acquire long-term functional reprogramming after challenge.
> The reprogramming is epigenetic, not genetic; it lasts weeks to
> months; it changes responsiveness to subsequent heterologous
> challenges. This matters evolutionarily (it is present across many
> invertebrate lineages) and clinically (BCG-induced non-specific
> protection; COVID vaccine heterologous effects).

---

## The classical dichotomy and its cracks

The framing used in attempts 100-107:
- **Innate immunity**: fast, non-specific, no memory. PRRs encoded
  in germline, same receptors on all cells, fixed repertoire.
- **Adaptive immunity**: slow first response, specific, with memory.
  Clonal lymphocytes with rearranged receptors.

The crack: starting around 2011, studies showed that innate cells
(trained monocytes, memory-like NK cells) could exhibit ENHANCED
responses to a SECOND exposure — even to a DIFFERENT pathogen than
the first — lasting days to months after the initial challenge. This
doesn't fit the classical definition of innate immunity, but it
isn't adaptive immunity either: no clonal selection, no receptor
rearrangement, no antigen specificity in the classical sense.

The term "trained immunity" was proposed to name this phenomenon:

**Netea MG, Quintin J, van der Meer JW (2011).** "Trained immunity:
a memory for innate host defense." *Cell Host & Microbe* 9:355-361.
PMID 21575907.

## The key experimental demonstrations

### BCG and heterologous protection

**Kleinnijenhuis J, Quintin J, Preijers F et al. (2012).** "Bacille
Calmette-Guerin induces NOD2-dependent nonspecific protection from
reinfection via epigenetic reprogramming of monocytes." *PNAS*
109:17537-17542. PMID 22988082.

BCG (bacillus Calmette-Guérin, the attenuated TB vaccine) has been
known for decades to provide non-specific protection against
infections beyond TB — reduced infant mortality in low-income
countries, reduced adult respiratory infections, and (in some
trials) protection against cancer and COVID-19. The Kleinnijenhuis
study showed the mechanism: monocytes from BCG-vaccinated humans
produced elevated cytokines (TNF, IL-1β, IL-6) in response to
unrelated pathogens (*Candida albicans*, *Staphylococcus aureus*),
mediated via epigenetic reprogramming of the monocyte chromatin.

### Beta-glucan training

**Quintin J, Saeed S, Martens JH et al. (2012).** "Candida albicans
infection affords protection against reinfection via functional
reprogramming of monocytes." *Cell Host & Microbe* 12:223-232.
PMID 22901542.

β-glucan from fungal cell walls, given to mice, protected them from
subsequent bacterial sepsis. The protection required dectin-1 and
downstream Akt/mTOR/HIF-1α signaling and was mediated by epigenetic
changes in monocyte inflammatory genes.

### The epigenetic basis

**Saeed S, Quintin J, Kerstens HH et al. (2014).** "Epigenetic
programming of monocyte-to-macrophage differentiation and trained
innate immunity." *Science* 345:1251086. PMID 25258085.

ChIP-seq analysis of BCG- and β-glucan-trained monocytes showed
persistent changes in:
- H3K4me3 (activating histone mark) at promoters of inflammation genes
- H3K27ac (enhancer activation) at inflammatory gene enhancers
- H3K4me1 (primed-enhancer mark) at genes that will respond faster on
  second challenge

The chromatin changes last 3-12 months in human monocytes; in bone
marrow progenitors they can last years.

### Central trained immunity: the bone marrow reservoir

**Mitroulis I, Ruppova K, Wang B et al. (2018).** "Modulation of
myelopoiesis progenitors is an integral component of trained
immunity." *Cell* 172:147-161.e12. PMID 29328910.

Trained immunity is not just on mature circulating monocytes (which
die and turn over in weeks). It is ALSO imprinted on hematopoietic
stem and progenitor cells (HSPCs) in the bone marrow, which then
produce "trained" daughter monocytes for months to years after the
initial stimulus.

This is the mechanistic link between short-lived circulating
monocytes and the multi-year epidemiological effects of BCG.

## Cell types with trained immunity

Documented in:

- **Monocytes and macrophages**: most studied. BCG, β-glucan, LPS
  (low-dose), oxidized LDL, virus exposures can train.
- **NK cells**: so-called "memory NK cells" — expand and persist
  after viral infection, especially HCMV. Sun, Beilke & Lanier 2009
  *Nature* 457:557. PMID 19136945.
- **Innate lymphoid cells (ILCs)**: evidence for ILC2 memory-like
  behavior.
- **Dendritic cells**: less studied; some evidence for training.
- **Epithelial stem cells**: skin and gut stem cells can acquire
  chronic inflammatory memory. Naik 2017 *Nature* 550:475 on skin
  epidermal stem cell memory of inflammation.

## Mechanisms

Three partially-overlapping mechanisms:

### 1. Epigenetic reprogramming

- H3K4me3 gain at inflammatory gene promoters
- H3K27ac gain at enhancers
- DNA methylation changes (less well-characterized)
- Chromatin remains "primed" for rapid re-activation upon second
  challenge

### 2. Metabolic rewiring

Trained monocytes shift toward glycolysis over oxidative
phosphorylation (Warburg-like). Key nodes:
- mTOR/HIF-1α activation
- Fumarate accumulation (via TCA cycle modulation)
- Mevalonate pathway intermediates

**Cheng SC, Quintin J et al. (2014).** "mTOR- and HIF-1α-mediated
aerobic glycolysis as metabolic basis for trained immunity."
*Science* 345:1250684. PMID 25258083.

### 3. Bone marrow progenitor imprinting

Described above (Mitroulis 2018). Central trained immunity provides
the durable substrate for multi-year protection despite short
monocyte half-life.

## Evolutionary distribution

### Invertebrate "priming"

Many invertebrates show enhanced resistance after sublethal exposure
to a pathogen. Examples:
- Insects (beetles, fruit flies): Toll-pathway-dependent priming
  lasting through development.
- Crustaceans (shrimp, crab): "immune memory" against WSSV virus
  and *Vibrio* bacteria.
- Echinoderms: priming in sea urchins for subsequent challenge.

These phenomena preceded the "trained immunity" name by decades;
they are now re-interpreted in the trained-immunity framework.

### Implication for the layered architecture framework

The classical claim — "memory is adaptive; innate is memoryless" —
is an over-simplification. Memory-like behavior at the functional
level has deep evolutionary roots, pre-dating RAG-based V(D)J. The
trained-immunity framework unifies:
- Invertebrate priming
- Vertebrate innate-cell reprogramming after BCG
- Plant "systemic acquired resistance" (SAR)
- Potentially even elements of prokaryotic phage memory (CRISPR,
  though that's more formally analogous to adaptive memory)

**"Memory" as a functional property has multiple molecular
implementations**, just as "adaptive immunity" does (attempt_104 on
VLR vs V(D)J parallelism).

## Clinical relevance

### BCG beyond TB

- **Bladder cancer**: intravesical BCG is standard treatment for
  non-muscle-invasive bladder cancer. Likely mediated by trained
  immunity of local myeloid cells.
- **Non-specific mortality reduction**: in infants, BCG reduces
  all-cause mortality beyond the TB-specific effect (Aaby et al.).
- **COVID-19 trials**: BRACE, ACTIVATE-2 and other trials testing
  BCG for COVID-19 prevention had mixed results. Partial evidence
  of reduced severity in some populations.

### Risk side: chronic inflammation

Trained immunity can be MALADAPTIVE:
- **Atherosclerosis**: oxidized LDL trains monocytes to become
  pro-inflammatory; trained foam cells drive plaque progression.
- **Autoinflammatory disease**: some conditions may involve
  pathological trained immunity.
- **Persistent-infection consequences**: in chronic CVB, EBV, HCV
  carriers, trained immunity may contribute to chronic
  inflammation (cross-link to 001-series).

Reference: **Mulder WJM, Ochando J, Joosten LAB, Fayad ZA, Netea MG
(2019).** "Therapeutic targeting of trained immunity." *Nature
Reviews Drug Discovery* 18:553-566. PMID 31296970.

### Vaccine implications

If trained immunity contributes substantially to vaccine protection,
it may explain:
- Heterologous vaccine effects (one vaccine protecting against
  unrelated pathogens).
- Variable vaccine efficacy in different populations (prior
  microbial exposures affecting baseline trained status).
- Potential for "training vaccines" that broadly protect via
  innate reprogramming rather than specific antigen.

## Open questions

1. **How long does trained immunity last in bone marrow progenitors?**
   Estimates range from months to years; human data limited.
   Direct testing requires sequential bone marrow biopsies, which
   is invasive.

2. **What is the "training repertoire"?** Given that adaptive
   immunity has specific receptor-antigen binding, does trained
   immunity have analogous specificity, or is it more generic
   ("primed for inflammation, not primed for specific pathogen")?

3. **Is trained immunity heritable across generations?** Some evidence
   in insects (transgenerational immune priming) and preliminary
   mouse data. Much less clear in humans.

4. **Is the BCG-COVID-19 association real?** Meta-analyses conflict.
   May depend on BCG strain (several exist), timing relative to
   infection, host genetics.

5. **Can we therapeutically induce or suppress trained immunity in
   a controlled way?** Current clinical trials testing β-glucan
   for cancer immunotherapy, oxidized-LDL blockade for
   atherosclerosis. Early days.

## Why this wasn't in attempts 103-107

The trained-immunity framework crystallized ~2012 and is still
consolidating. Attempts 103 (invertebrate innate) and 106 (mammalian
refinements) gave hints — invertebrate priming in 103, monocyte
differentiation in 106 — but the unifying framework of trained
immunity hadn't been developed at the level that it deserved a
single-attempt treatment. This 108 attempt fills that gap.

## Links to other attempts

- attempt_100 (framework): trained immunity IS a layer-bending
  phenomenon that the strict layered architecture doesn't cleanly
  accommodate. The framework is approximately right but not
  exhaustively so.
- attempt_103 (invertebrate innate): insect priming is a deep
  evolutionary form of trained immunity.
- attempt_106 (mammalian): monocyte/macrophage biology is where
  trained immunity manifests most clearly in modern humans.
- attempt_107 (persistent-virus coevolution): chronic
  persistent-virus carriage may drive chronic trained-immunity
  reprogramming, contributing to chronic inflammatory disease.
- **001-series** (persistent organisms): H. pylori chronic carriage,
  P. gingivalis, Demodex infestation all likely drive chronic
  trained-immunity changes in local myeloid populations.

## Key sources

Primary:
- Netea MG, Quintin J, van der Meer JW 2011 *Cell Host Microbe*
  9:355 (term coined). PMID 21575907.
- Kleinnijenhuis J et al. 2012 *PNAS* 109:17537 (BCG epigenetic
  reprogramming). PMID 22988082.
- Quintin J et al. 2012 *Cell Host Microbe* 12:223 (β-glucan).
  PMID 22901542.
- Saeed S, Quintin J et al. 2014 *Science* 345:1251086 (epigenetic
  programming). PMID 25258085.
- Cheng SC et al. 2014 *Science* 345:1250684 (metabolic basis).
  PMID 25258083.
- Sun JC, Beilke JN, Lanier LL 2009 *Nature* 457:557 (adaptive-like
  NK memory). PMID 19136945.
- Mitroulis I et al. 2018 *Cell* 172:147 (bone marrow progenitor
  imprinting). PMID 29328910.
- Naik S et al. 2017 *Nature* 550:475 (inflammatory memory in
  skin stem cells).

Reviews:
- Mulder WJM et al. 2019 *Nat Rev Drug Discov* 18:553 (therapeutic
  targeting). PMID 31296970.
- Netea MG et al. 2020 *Nature Rev Immunol* 20:375 (defining
  trained immunity and its role in health and disease).

---

## Gap opened

- **Quantifying trained immunity contribution to vaccine
  protection** remains hard. For any specific vaccine, distinguishing
  antigen-specific memory from non-specific trained effects requires
  heterologous-challenge experiments that are ethically
  constrained in humans.
- **Trained immunity in chronic persistent-infection contexts**:
  H. pylori, EBV, HCMV, HCV carriage likely reshape trained
  baseline for decades. Systematic study of this would cross-link
  the 001-series and 100-series in a new way.

## Status

Extension attempt complete. The 100-series core sweep was 100-107;
108+ are optional extensions to specific frontier topics. Further
extensions might cover: non-retroviral endogenous viral elements,
mucosal immunology evolution, placental-tolerance genetics by
lineage, host-commensal coevolution.

---

*Filed: 2026-04-15 | biology/evolution/attempts/attempt_108*
*Extension after the main 100-107 sweep; independent from the 001-series.*
*Parallel-instance convention: 100-199 range; 001-099 is other instance's scope.*
