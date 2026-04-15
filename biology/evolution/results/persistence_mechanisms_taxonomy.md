# Persistence-Mechanism Class Taxonomy — Synthesis

> Closes the per-organism series (attempts 002–010). Formalizes the
> 7 persistence-mechanism classes that emerged across viral,
> bacterial, and eukaryotic organisms. Derives the framework's
> predictions in a unified form, identifies boundary cases, and
> names organism types not yet covered that may reveal additional
> classes.
>
> **VERIFICATION STATUS:** this synthesis depends on the per-organism
> attempts' content. Each per-organism attempt has undergone one or
> more audit passes (see `medical/blepharitis/results/claim_audit_2026-04-15.md`
> for 4 batches, ~45 claims, ~44% verified / 47% corrected). The
> synthesis framework itself is at operator-call confidence — it's
> a structure derived from the organism set, not a verified empirical
> claim.

---

## The 7 classes

Each class is defined by a distinct mechanism for maintaining
long-term intra-host presence without clearance. The classes are not
mutually exclusive — some organisms use primary + secondary
mechanisms.

### Class 1 — Encoded latency with programmatic quiescence

- **Definition:** organism encodes a transcriptional program that
  silences most of its genome during dormancy, maintained via
  episomal or low-activity state
- **Examples:** EBV (4-program model in B-cells), HCMV (myeloid
  latency + counter-immunology), HSV (neural latency), VZV (ganglion
  latency), KSHV
- **Signatures:**
  - Large coded genome (typically >100 kb) devoted partly to latency
    machinery
  - Specific gene sets for episomal maintenance (EBNA-1 for EBV;
    LANA for KSHV)
  - Reactivation triggered by defined host signals (cell
    differentiation, stress, immunosuppression)
  - Tight species-specificity
- **Prediction test:** larger genomes predict more-elaborate latency
  machinery → confirmed across herpesvirus family
- **Framework strength:** strong — α/β/γ herpesvirus subfamilies all
  fit

### Class 2 — Mutation-driven replication-defective persistent form

- **Definition:** within-host evolution produces a genetic variant
  that replicates inefficiently + is immunologically silent, while
  the ancestral virus clears; the variant persists as the host
  reservoir
- **Examples:** CVB (5'-UTR-deleted), possibly other picornaviruses
  in certain tissue contexts
- **Signatures:**
  - Small genome (no encoded latency machinery)
  - Requires long-lived infected cells as reservoir
    (cardiomyocytes, β-cells, neurons)
  - Reactivation via recombination with intact co-infecting virus
  - Weak host specificity (can use tropism of ancestral virus)
- **Prediction test:** RNA viruses would use this mechanism more
  often than DNA viruses given their mutation rate → consistent
- **Framework strength:** mid — documented for CVB, suggested for
  others (EV-71?, HCV quasispecies?), not as universally applicable
  as class 1

### Class 3 — Lifecycle-differentiation compartmentalization

- **Definition:** organism times virion / progeny production to a
  host compartment physically separated from immune surveillance,
  exploiting host-cell differentiation to achieve spatial + temporal
  immune evasion
- **Examples:** HPV (basal/suprabasal/cornified epithelium
  differentiation)
- **Signatures:**
  - Small genome (no encoded latency)
  - Strict epithelial tropism
  - Virion production in the outermost, about-to-be-shed layers
  - Keratinocyte-like host-cell substrate required
- **Prediction test:** only works for viruses with access to
  differentiating epithelium → mostly one family (Papillomaviridae);
  possibly Polyomaviridae at a weaker form
- **Framework strength:** medium — single major example but
  mechanism is clean; likely extends to some skin/mucosal viruses

### Class 4 — Antigenic variation

- **Definition:** organism continuously varies surface antigens
  during chronic replication, staying ahead of adaptive immunity
- **Examples:** HIV (env gene hypervariability), HCV (E1/E2),
  possibly Trypanosoma (VSG variation in protozoa)
- **Signatures:**
  - Active chronic replication (no latent phase in the classic sense)
  - High mutation rate or gene-switching machinery
  - Large antigenic-variation "library" encoded in genome
  - Escape from humoral immunity is primary
- **Prediction test:** works only if mutation rate or recombination
  frequency exceeds immune-response specificity
- **Framework strength:** medium in human-persistent-organism
  context; stronger in protozoal chronic infections (malaria,
  trypanosomiasis) not on the current list

### Class 5 — Chromosomal integration with germline transmission

- **Definition:** viral genome integrates into host chromosome (at
  specific loci), maintained through mitosis + sometimes meiosis,
  producing vertical germline inheritance
- **Examples:** HHV-6A and HHV-6B (ciHHV-6), at a different timescale
  HERVs (endogenous retroviruses — fully integrated, lost
  infectivity)
- **Signatures:**
  - Integration at defined chromosomal locations (telomeric for
    HHV-6; various for retroviruses)
  - Mendelian inheritance pattern in integrated cases
  - Transitional state between virus and host
  - May or may not retain reactivation capability
- **Prediction test:** germline-transmitting viruses should show
  population-level carrier frequency + inheritance patterns matching
  integration rate → HHV-6 fits at ~1% population frequency; HERVs
  are the historical end-state
- **Framework strength:** unique case in current human persistent
  viruses — HHV-6 is the only active example

### Class 6 — Chronic active colonization with host-tolerance induction

- **Definition:** organism actively replicates continuously in a
  physically protected niche (anaerobic pocket, mucosal layer),
  encoding effectors that induce host immune tolerance rather than
  evading clearance
- **Examples:** *H. pylori* (gastric mucus layer; urease + VacA +
  CagA), *P. gingivalis* (periodontal pocket; gingipains), *C. acnes*
  (pilosebaceous unit; phylotype-dependent)
- **Signatures:**
  - Moderate genome (~1.5–3 Mb for bacteria; proportionally sized
    for other organisms)
  - Physically inaccessible niche (mucus, biofilm, anaerobic pocket)
  - Encoded immune-tolerance effectors (complement cleavage, cytokine
    degradation, NF-κB manipulation)
  - Often strain-dependent pathogenicity (Cag+/- H. pylori, C. acnes
    phylotypes)
  - Bacterial-dominant class
- **Prediction test:** should generalize to other anaerobic/mucosal
  bacterial chronic infections → consistent for M. tuberculosis
  (latent TB), Treponema pallidum (latent syphilis)
- **Framework strength:** strong — 3 organisms confirmed + good
  extensibility to bacterial pathogens broadly

### Class 7 — Obligate host-dependent multicellular eukaryote

- **Definition:** eukaryotic organism (animal, fungal, protozoan)
  cannot live free; depends on a specific host substrate; has
  reductive-genome signature from loss of free-living-capacity genes
- **Examples:** Demodex (arthropod; reductive genome + lipid-
  dependent), Malassezia (yeast; FAS pathway lost + lipid-dependent),
  and others NOT on the current list: *Pediculus* lice, *Sarcoptes*
  scabies, *Enterobius* pinworm
- **Signatures:**
  - Reductive genome relative to free-living relatives
  - Absolute host-substrate dependence (sebum, blood, skin, etc.)
  - Strict or near-strict host specificity
  - Density-dependent pathogenesis (low = commensal, high = disease)
  - Vertical + intimate-contact transmission
  - Long coevolutionary timescale (millions to hundreds of millions
    of years)
- **Prediction test:** any obligate multicellular ectoparasite or
  endoparasite should show reductive-genome + strict host-specificity
  → consistent (lice, fleas, ticks, tapeworms all show this)
- **Framework strength:** strong and highly generalizable across
  multicellular parasites

---

## What the taxonomy predicts

### Prediction 1 — persistence requires genome specialization

Applies to all 7 classes but in opposite directions:
- Viruses classes 1, 3, 5 — coded-latency/integration machinery
  (HPV is an exception at 8 kb; uses host machinery instead)
- Bacteria class 6 — moderate genome with immune-manipulation
  effectors
- Eukaryotes class 7 — genome reduction via loss of free-living
  machinery

**The universal signature is specialization**, measurable in either
direction.

### Prediction 2 — persistence requires species-specificity + long coevolution

All 10 organisms in the current framework show strict or near-strict
human specificity. The exceptions are Malassezia pachydermatis (can
cross between humans and dogs) and CVB (some swine reservoir), both
at relatively weak cross-species penetration.

**Without long coevolution, persistence doesn't establish.** Acute
zoonotic infections (e.g., influenza spillover from birds) are acute
precisely because they haven't coevolved.

### Prediction 3 — disease is typically post-transmission and
therefore evolutionarily incidental

For viruses and bacteria: transmission precedes chronic disease in
all 8 cases examined. For Demodex: transmission is mother-to-infant
before density rises enough to cause symptoms. For Malassezia +
C. acnes: same.

**Chronic disease is not under strong organism-side selection in any
persistent organism.** This has important clinical implications —
treatment doesn't drive rapid evolution toward reduced virulence
because virulence is already irrelevant to organism fitness.

### Prediction 4 — class determines therapeutic options

| Class | Therapeutic options | Example |
|-------|---------------------|---------|
| 1 | Antiviral affecting replication / reactivation; prophylactic vaccination | HSV — valacyclovir; HPV — Gardasil |
| 2 | Host-cell-level antivirals; reactivation prevention | CVB — fluoxetine repurposed |
| 3 | Prophylactic vaccination (blocks infection); lesion-level treatment | HPV — Gardasil + LEEP |
| 4 | Suppressive antivirals (no cure); combination therapy | HIV — cART |
| 5 | Cannot eradicate; limited reactivation management | HHV-6 — ganciclovir in transplant |
| 6 | Antibiotic clearance + niche-restoration + tolerance-breakers | H. pylori — PPI+triple antibiotic |
| 7 | Host-site treatment (acaricide/antifungal); density reduction | Demodex — ivermectin/TTO; Malassezia — ketoconazole |

**Class prediction: therapeutic success is inversely proportional
to persistence-mechanism sophistication.** Class 1 (encoded latency)
and class 5 (integration) are the hardest to cure; class 6 (chronic
colonization) and class 7 (obligate parasite) are more tractable
with direct organism-clearance agents.

### Prediction 5 — class predicts which diseases scale with modernity

- Class 6 bacterial: H. pylori ↓ with sanitation; P. gingivalis ↑
  with Western diet. **Direction depends on the specific dietary/
  hygienic intervention.**
- Class 7 ectoparasite: Demodex ↑ with Western diet (sebum
  substrate). Malassezia ↑ similarly. **Modern conditions favor
  class-7 pathogens where free lipid availability increases.**
- Viral classes (1, 3, 5): mostly neutral to hygiene; small
  reductions from delayed-transmission effects (increasing age of
  first infection sometimes worsens disease, as in CVB/T1DM).

**Modernity shifts persistent-organism composition in predictable
ways by class.**

---

## Boundary cases and edge organisms

### Mycobacterium tuberculosis (latent TB)

Fits class 6 (chronic colonization with granuloma-mediated immune
tolerance) but the intracellular aspect (within macrophages) blurs
toward class 7 (obligate host-dependent). Suggests class 6 + class
7 form a spectrum for host-dependent organisms.

### HERV (human endogenous retroviruses)

Fully integrated class-5 organisms that lost infectivity and are now
host-genome content. Not "persistent organisms" in the active sense
— they are the terminal state of class-5 evolution. Some HERVs
retain partial gene expression (syncytin-1, co-opted for placenta)
— repurposed rather than persistent.

### Plasmodium falciparum (malaria)

Chronic infection in some contexts (P. vivax hypnozoites); uses
antigenic variation (class 4, via VSG-like PfEMP1). Not on the
current framework list (different disease context) but would fit
class 4 if added.

### Toxoplasma gondii

Chronic intracellular parasite in tissue cysts; highly prevalent
(~30% global seroprevalence); mostly asymptomatic. Class 6-like
(chronic + tolerance) but with protozoal life cycle. Another
boundary case.

### Trypanosoma cruzi (Chagas disease)

Chronic intracellular infection with antigenic variation (class 4
elements); slow chronic cardiac / GI manifestations decades post-
acute phase. Fits class 4 + class 7 hybrid.

**These organisms reinforce that classes 4, 6, 7 apply to protozoa
and intracellular pathogens, not just the 10-organism list.**

---

## Classes not covered — what's missing?

The current 10-organism list represents humans-only, common
organisms. Missing entries that would populate additional classes
or edge cases:

1. **HIV-1 / HIV-2** — class 4 (antigenic variation) + class 5
   (integration, though not germline). Not included because the
   operator's scope was "persistent organisms driving chronic
   disease" and HIV is aggressively treated.
2. **HBV** — complex: episomal cccDNA + partial integration. Would
   add a class 1+5 hybrid case.
3. **HCV** — class 4 dominant. Now largely curable with DAAs, so
   less persistent-organism-framework-relevant in modern contexts.
4. **M. tuberculosis** — class 6 with granuloma biology.
5. **Toxoplasma, Plasmodium, Trypanosoma** — protozoal class 4 / 6
   / 7 hybrids.
6. **Strongyloides** — human soil-transmitted helminth with
   autoinfection (decades-long internal persistence); fits class 7.
7. **Candida albicans** — opportunistic; class 7 potential.

Adding any of these would refine the taxonomy but wouldn't require
new classes — the 7 classes cover the persistence-mechanism
space broadly.

---

## Open theoretical questions

1. **Are 7 classes enough, or is there an 8th that's missing?**
   Candidate: **biofilm-based chronic infection** as a distinct
   mechanism (Pseudomonas in cystic fibrosis, polymicrobial
   periodontitis). Could argue it's a subclass of 6, or a
   separate 8. Leaving at 7 for now.

2. **Do all classes coexist over evolutionary time, or do some
   dominate in specific host contexts?** Hypothesis: viral
   persistence dominated early (deep coevolution); bacterial
   persistence rose with agriculture (anaerobic-niche expansion);
   eukaryotic persistence has been stable since mammalian
   emergence.

3. **Is the framework symmetric — can it predict which organisms
   WILL evolve persistence?** Testing this would require
   retrospective analysis: did the now-persistent organisms have
   characteristic features before persistence evolved? Ancient-DNA
   studies on pre-persistence ancestors would clarify.

4. **Do classes correlate with disease severity or chronicity
   trajectory?** Class 1 (encoded latency) produces some of the
   most severe remote disease (EBV → MS, HCMV → congenital); class 7
   (obligate parasite) produces the mildest on average. Is there a
   mechanistic reason for the correlation, or is it a selection
   artifact of what gets studied?

5. **Why has human evolution not closed any of these persistent
   infections over ~300,000 years of anatomically modern humans?**
   The answer is partly co-evolutionary — tolerance is cheaper than
   clearance for the host too — but this deserves deeper analysis.

---

## Therapeutic implications across classes

A key cross-class observation from `medical/blepharitis/attempt_006`
and `medical/persistent_organisms/PROBLEM.md`: the **two-phase
therapeutic architecture (clearance + anti-inflammatory adjunct)
applies universally across the 7 classes**, with the specific agents
differing:

| Class | Primary clearance agent | Adjunct anti-inflammatory |
|-------|------------------------|---------------------------|
| 1 | Antivirals (acyclovir, ganciclovir); vaccines | Symptom management; specific targeting (rituximab for EBV-MS) |
| 2 | Cellular antivirals (fluoxetine repurposed, nucleoside analogs) | NLRP3 suppressors; metabolic support |
| 3 | Local lesion treatment; prophylactic vaccination | Post-exposure management |
| 4 | Combination antivirals (class-crossed) | ART adjuncts |
| 5 | Cannot clear reliably | Reactivation management |
| 6 | Antibiotics; anti-protease therapeutics | Doxycycline 40mg, anti-inflammatory |
| 7 | Acaricide / antifungal | Doxycycline 40mg, omega-3, barrier repair |

**The doxycycline 40 mg sub-antimicrobial appears across classes 6
and 7 for a single-drug mechanism (MMP-9 inhibition, anti-
inflammatory independent of antimicrobial effect).** This is the
cleanest cross-class therapeutic unification in the framework. It's
a direction worth formalizing further as a second results-level
synthesis.

---

## Status of the biology/evolution directory

- `PROBLEM.md` — scope (viral subset initially, expanded to all
  persistent organisms after operator update)
- `attempts/attempt_001_persistence_as_strategy.md` — cross-cutting
  framework; needs updates to reference the 7-class taxonomy
- `attempts/attempt_002_cvb_evolution.md` through
  `attempts/attempt_010_malassezia_cutibacterium_evolution.md` —
  10 per-organism attempts (some with audit updates)
- `results/persistence_mechanisms_taxonomy.md` — **this note**

### Recommended next synthesis work

1. **Host-side coevolution attempt** — HLA, KIR, TRIM5α, HERV, TLR
   polymorphism signatures across the persistent-organism set
2. **Therapeutic convergence synthesis** — systematic documentation
   of cross-organism drug repurposing (doxycycline 40 mg being the
   clearest; others likely)
3. **Modernity trajectory analysis** — which organisms rising vs
   declining under current conditions, and what this predicts for
   chronic-disease burden over 50–100 year horizons
4. **Class-1/7 boundary cases** — M. tuberculosis, Toxoplasma,
   Trypanosoma as framework extensions
5. **Update attempt_001** with the 7-class taxonomy references

These are aggregate / synthesis directions, not per-organism deep
dives. The 10-organism per-organism series is complete.

---

*Filed: 2026-04-15 | biology/evolution/results/persistence_mechanisms_taxonomy.md*
*Closes the per-organism series; opens the synthesis phase*
*Depends on: attempts 001–010; needs audit pass on specific class-boundary claims*
