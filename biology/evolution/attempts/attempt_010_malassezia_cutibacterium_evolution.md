# attempt_010 — Malassezia and Cutibacterium acnes: The Sebaceous Ecosystem Completed

> Final per-organism attempt. Malassezia (fungal yeast) and
> *Cutibacterium acnes* (Gram-positive bacterium) are near-universal
> skin-resident commensals that share the sebaceous/follicular niche
> with Demodex (attempt_009). Together they form the sebaceous-site
> persistent-organism ecosystem that underlies rosacea, blepharitis,
> acne, and seborrheic dermatitis.
>
> **VERIFICATION STATUS:** generated from trained priors; genome
> sizes, species counts, and strain-phylotype disease associations
> are structurally reliable but specific numeric figures + PMIDs
> flagged for audit.
>
> Cross-cutting framework: attempt_001. This attempt closes the
> per-organism series.

---

## Combined scope and rationale

Malassezia and C. acnes are typically treated in different clinical
and research communities (dermatology-mycology vs dermatology-
bacteriology). **Evolutionarily they are parallel stories** — both
are lipid-dependent skin specialists with reductive genomes, both
show density-dependent pathogenesis, both coexist with Demodex on
the same sebaceous sites. Treating them together in one attempt
makes the ecosystem-level pattern visible.

---

# Part A — Malassezia (fungal)

## Phylogenetic placement

**Domain:** Eukaryota
**Kingdom:** Fungi
**Phylum:** Basidiomycota
**Class:** Malasseziomycetes (erected in 2015 to accommodate the
  genus; previously Ustilaginomycetes)
**Order:** Malasseziales
**Family:** Malasseziaceae
**Genus:** *Malassezia*

**Species on human skin** (as of current taxonomy, ~18 species
in the genus):
- ***M. globosa*** — dominant on scalp, chest, back; central
  seborrheic-dermatitis driver
- ***M. restricta*** — co-dominant in seb-derm; dandruff
- ***M. furfur*** — bloodstream infections in preterm infants on
  lipid TPN; pityriasis versicolor
- ***M. sympodialis*** — common
- ***M. dermatis*** — atopic-dermatitis associations
- ***M. pachydermatis*** — primarily on dogs; zoonotic potential
  (hospital outbreaks in NICUs via healthcare-worker pet exposure)
- Additional species: *M. slooffii*, *M. japonica*, *M. yamatoensis*,
  *M. obtusa*, *M. nana*, *M. caprae*

**Coevolution:** Malassezia is on all mammals examined; genus
diversification mirrors mammal phylogeny. Species-host specificity
is moderate — tighter than opportunistic pathogens, looser than
Demodex. Human Malassezia has been present since before hominin
divergence; specific human species emerged during primate evolution.

## Reductive genome — mirror of Demodex

**Malassezia genomes are small for fungi** — ~7–9 Mb across species
(cf. baker's yeast *Saccharomyces cerevisiae* ~12 Mb;
*Cryptococcus neoformans* ~19 Mb).

The diagnostic feature: **Malassezia has lost the fatty acid
synthase (FAS) pathway** — cannot synthesize its own lipids.
Therefore:
- Absolutely lipid-dependent (obligate lipophilic lifestyle)
- Cannot grow on carbohydrate-only media in lab (requires olive oil,
  Tween-80, or similar in culture media)
- Reliant on host sebum as sole lipid source
- Unable to colonize non-sebaceous body sites

This FAS loss is the functional equivalent of Demodex losing
biosynthetic pathways (attempt_009). **Reductive genome +
obligate-host-substrate = class 7 persistence-mechanism signature**
— same mechanism class as Demodex, different organism.

## Niche: the sebaceous-rich skin

Malassezia is concentrated at sites with high sebaceous gland
density:
- Scalp, forehead, eyebrows (strong *M. globosa* + *M. restricta*)
- Nasolabial folds, external ear canal
- Chest + upper back
- Meibomian glands (eyelid — cross-link to blepharitis)
- Outer ear

Malassezia does NOT colonize:
- Plantar / palmar skin (no sebum)
- Oral cavity (different niche)
- Lower GI tract (under debate — some recent reports of gut
  Malassezia; consensus is skin-restricted for the major species)

## Disease portfolio

1. **Seborrheic dermatitis** (including dandruff) — strongest
   association; *M. globosa* + *M. restricta* drive the process
   via lipase-mediated oleic acid release
2. **Pityriasis versicolor** (tinea versicolor) — hypopigmented
   patches; *M. furfur* dominant
3. **Malassezia folliculitis** — follicular pustules resembling
   acne but antifungal-responsive
4. **Atopic dermatitis** — contributes to flares, especially on
   head/neck phenotype
5. **Psoriasis** — modulates disease; contributing factor
6. **Seborrheic blepharitis** — posterior and mixed blepharitis
   (cross-link to `medical/blepharitis/attempt_008`)
7. **Neonatal cephalic pustulosis** — Malassezia-associated
   pustular eruption in newborns
8. **Preterm-infant bloodstream infection** (on lipid TPN) —
   serious but restricted clinical setting
9. **Parkinson's disease seborrheic phenotype** — Parkinson's
   patients commonly have severe seb-derm; mechanism via decreased
   facial motor tone + altered sebum

## Pathogenesis mechanism

Malassezia produces lipases that cleave host triglycerides into free
fatty acids. The key irritant: **oleic acid** (an unsaturated free
fatty acid) penetrates the stratum corneum, disrupts barrier
function, and activates inflammation:

```
Malassezia lipases on sebum triglycerides
    ↓
Free fatty acid release (oleic acid prominent)
    ↓
Stratum corneum barrier disruption
    ↓
Keratinocyte pattern recognition activation (TLR2?)
    ↓
Inflammation + hyperproliferation + desquamation
    ↓
Seborrheic-dermatitis-phenotype skin
```

This is distinct from Demodex (which triggers inflammation via
B. oleronius endosymbiont → TLR4/NLRP3) and from C. acnes (which
uses porphyrin production + biofilm).

## Density-dependent pathogenesis (same pattern as Demodex)

Malassezia is universally present on adult skin at low density
without disease. Pathogenesis emerges when density rises via:
- Excess sebum (androgens, insulin, diet)
- Skin barrier defect
- Immune modulation (steroid use, immunosuppression)
- High-humidity environments
- Parkinson's disease (reduced facial motor activity)

---

# Part B — Cutibacterium acnes (bacterial)

## Phylogenetic placement

**Domain:** Bacteria
**Phylum:** Actinomycetota (formerly Actinobacteria)
**Class:** Actinomycetia
**Order:** Propionibacteriales
**Family:** Propionibacteriaceae
**Genus:** *Cutibacterium* (renamed from *Propionibacterium* in 2016)
**Species:** *Cutibacterium acnes*

**The 2016 rename** (Scholz + Kilian) split the classical
Propionibacterium genus into Propionibacterium (dairy-associated),
Cutibacterium (human skin — *C. acnes*, *C. avidum*, *C. granulosum*),
and Acidipropionibacterium. The rename reflects distinct ecology and
phylogeny.

**Strain diversity within C. acnes** — this is the key insight:
C. acnes is not one organism but a set of strains with very
different disease associations:

| Phylotype | Typical association |
|-----------|---------------------|
| **IA1** | Inflammatory acne (the classical "acne phylotype") |
| **IA2** | Less associated with acne |
| **IB** | Variable; some inflammatory signals |
| **IC** | Less common |
| **II** | Commensal; opportunistic infections (prosthetic joint, cardiac) |
| **III** | Commensal; occasional opportunistic infections |

**Disease is phylotype-specific within the same species.** IA1-dominant
individuals develop acne; II/III-dominant individuals rarely do.
This is distinct from the "organism present = disease" framing that
worked for H. pylori but not for C. acnes.

## Genome

- **~2.5 Mb** circular chromosome
- Fermentative anaerobe (produces propionic acid + acetate from
  sugar metabolism — original genus name rationale)
- Microaerotolerant at sebum-buried follicle depths
- Genome plasticity: linear plasmids vary by strain; tight-junction-
  adhesion loci vary
- Core genome is ~2.2 Mb with ~0.3 Mb accessory content per strain

## Niche: the pilosebaceous unit

C. acnes lives in the follicular pore, often at significant depth
(below the aerobic skin surface). Sebum is its substrate. Like
Malassezia, it requires the sebaceous environment — but its
substrate is the sebum itself (glycerol and small lipids) rather
than hydrolysis products.

## Pathogenesis — acne biology

Acne vulgaris pathogenesis:

```
Increased sebum production (androgens, IGF-1, diet)
    ↓
Hyperkeratinization of pilosebaceous follicle opening
    ↓
Micro-comedone formation (closed follicle)
    ↓
Anaerobic environment within comedone
    ↓
C. acnes (IA1 phylotype) proliferation
    ↓
Porphyrin production + lipase activity + biofilm
    ↓
TLR2 activation on sebaceous cells + neutrophil recruitment
    ↓
Inflammatory papule/pustule
```

C. acnes is part of the normal follicular flora even in non-acne
people. The transition to acne requires:
1. Sebum hyperproduction
2. Follicular plugging
3. IA1 phylotype dominance (or another pro-inflammatory phylotype)

## Disease portfolio

1. **Acne vulgaris** — the canonical association
2. **Post-surgical prosthetic joint infection** — phylotype II/III
   strains; chronic low-grade infection common after shoulder
   replacement
3. **Endocarditis** (rare)
4. **Seborrheic dermatitis** (contributor alongside Malassezia)
5. **Rosacea** (contributor via biofilm at lid-margin and face)
6. **Sarcoidosis** (debated association; some Japanese studies)
7. **Sciatica/disc infection** — controversial; C. acnes has been
   isolated from discectomy specimens at higher rates than expected

## Persistence mechanism — class 6 with strain-level stratification

C. acnes uses **class 6 (chronic active colonization + host-tolerance
induction)** like H. pylori and P. gingivalis — but with a crucial
addition: **strain-level variation determines commensal vs pathogen
outcome within the same species**.

This is analogous to Cag-positive vs Cag-negative H. pylori strains,
but more pronounced in C. acnes because the phylotype structure is
more complex and better-characterized.

**Framework update:** class 6 organisms frequently show
strain-level disease partitioning. Future work on the framework
should explicitly split "chronic active colonization" into
strain-dependent variations.

---

# Part C — Ecosystem interactions and combined implications

## The sebaceous-site triad

Demodex + Malassezia + C. acnes form an **ecosystem on sebaceous
skin**. They share niche and substrate, overlap in body sites, and
collectively produce the clinical phenotypes:

| Disease | Demodex | Malassezia | C. acnes |
|---------|:-------:|:----------:|:--------:|
| Acne vulgaris | — | — | ★★★ |
| Rosacea | ★★★ | ★ | ★★ |
| Anterior blepharitis (Demodex type) | ★★★ | ★ | — |
| Seborrheic blepharitis | — | ★★★ | ★ |
| Seborrheic dermatitis / dandruff | ★ | ★★★ | ★ |
| Perioral dermatitis (candidate Demodex) | ★★ | ★ | ★ |
| Pityriasis versicolor | — | ★★★ | — |
| Malassezia folliculitis | — | ★★★ | — |

**Clinical implication:** the same sebaceous-rich zone in a single
patient can host all three organisms simultaneously, with disease
phenotype depending on which dominates (and which strain dominates
for C. acnes). Treatment protocols that address the entire
ecosystem (e.g., TTO for Demodex + ketoconazole for Malassezia +
benzoyl peroxide for C. acnes) can resolve mixed-phenotype disease
where single-organism treatment underperforms. The multi-organism
lid-margin framework in `medical/blepharitis/attempt_008` is one
instantiation of this pattern.

## Shared evolutionary features

| Feature | Demodex | Malassezia | C. acnes |
|---------|:-------:|:----------:|:--------:|
| Reductive genome (specialization) | ✓ | ✓ | ~ |
| Lipid-dependent lifestyle | ✓ | ✓ | ✓ |
| Sebaceous niche | ✓ | ✓ | ✓ |
| Density-dependent pathogenesis | ✓ | ✓ | ✓ (+ strain-dep) |
| Near-universal adult colonization | ✓ | ✓ | ✓ |
| Strict or near-strict human specificity | ✓ | ◐ | ✓ |
| Vertical transmission (mother-child) | ✓ | ✓ | ✓ |

All three show the signatures of long coevolution with human skin.
All three are essentially impossible to eradicate and would not be
net beneficial to eradicate — low-density colonization appears to
be benign or beneficial.

## Class 7 re-examined

With Malassezia and Demodex both occupying class 7 (obligate
lipid-dependent skin symbiont with reductive genome) across two
kingdoms (Animalia + Fungi), the class is robust. It is
characterized by:

1. Loss of biosynthetic pathways for substrate precursors (FAS loss
   in Malassezia; amino acid biosynthesis loss in Demodex)
2. Absolute dependence on host substrate (sebum)
3. Strict or near-strict host specificity
4. Density-dependent pathogenesis
5. Vertical + intimate-contact transmission

Class 7 applies equally well to lice (arthropod, reductive-genome,
host-feather/fur-dependent) and possibly to hookworms, scabies.

## Ecosystem vs single-organism pathogen framework

The persistent-organism framework (medical/persistent_organisms/)
treats Demodex, Malassezia, C. acnes as three separate rows. The
evolutionary analysis suggests they should be **treated as one
ecosystem** on sebaceous skin, analogous to how the dysbiosis
framework treats gut microbes as a composite rather than splitting
into individual organism rows.

This is a framework refinement: **some persistent organisms cluster
into ecosystem-level units, where the clinical phenotype depends on
the balance of the whole community**. Gut dysbiosis is the obvious
example; sebaceous-skin dysbiosis (rosacea / acne / seb-derm / POD)
is the skin analog.

---

# Part D — Comparison across all 10 attempts

## Updated structural table (complete 9 organisms)

| Organism | Class | Genome | Kingdom | Disease range | Unique feature |
|----------|-------|--------|---------|---------------|----------------|
| CVB | 2 Mutation | 7.4 kb | Virus (RNA) | T1DM, DCM, ME/CFS | Persistent form from 5'-UTR deletion |
| EBV | 1 Encoded latency | 172 kb | Virus (DNA) | MS, lymphomas, CFS | 4-program B-cell latency; MS causation |
| HPV | 3 Lifecycle coupling | 8 kb | Virus (DNA) | Cervical/oral cancer | Vaccine-era selection |
| HCMV | 1+ Latency + immunology | 235 kb | Virus (DNA) | CMV disease, congenital | Largest genome; NK/KIR driver |
| HHV-6 | 5 Germline integration | 160 kb | Virus (DNA) | MS (partial), DRESS | Only germline-transmitting virus |
| H. pylori | 6 Chronic + tolerance | 1.7 Mb | Bacterium (G-neg) | Ulcer, cancer, protective GERD | Migration tracker; protective effects |
| P. gingivalis | 6 Chronic + tolerance | 2.3 Mb | Bacterium (G-neg) | Periodontitis + 6 remote diseases | Broadest remote-disease portfolio |
| Demodex | 7 Obligate ectoparasite | ~80 Mb | Animal (arthropod) | Rosacea, blepharitis, POD | Reductive genome + 3-tier symbiosis |
| **Malassezia** | **7 Obligate lipid-dep eukaryote** | **~8 Mb** | **Fungus (yeast)** | **Seb-derm, dandruff, PV, folliculitis** | **FAS pathway loss; Parkinson's link** |
| **C. acnes** | **6 Chronic + strain-dep** | **2.5 Mb** | **Bacterium (G-pos)** | **Acne + opportunistic + rosacea contrib** | **Phylotype-specific disease outcome** |

**Framework coverage:**
- **3 kingdoms** (Virus via viruses, Bacteria, Eukarya)
- **7 distinct persistence-mechanism classes**
- **Genome size range**: 7.4 kb (CVB) to ~80 Mb (Demodex) — 10,000×
- **Host range**: strict-human to humans+animals
- **Disease range**: acute → chronic → cancer → behavioral

The persistent-organism framework holds across this entire scope.
The shared themes (ancient coevolution, host-specificity, density-
dependent or strain-dependent pathogenesis, disease-as-incidental-
to-organism-fitness) apply with minor per-organism adjustments.

## What's next for biology/evolution/

The per-organism series is complete for the 8 (now 9-10) organisms
in the persistent-organism framework. Natural extensions:

1. **Meta-theorem synthesis** (results/): formalize the
   persistence-mechanism class taxonomy (1–7); derive the
   framework's predictions systematically.
2. **Cross-organism therapeutic convergence analysis**: the
   doxycycline 40 mg finding (rosacea + blepharitis + periodontitis +
   ocular rosacea) + broader patterns of shared anti-inflammatory
   adjuncts across organism classes.
3. **Host-immunity coevolution attempt** — HLA, KIR, TRIM5α,
   HERV, TLR polymorphism patterns driven by this organism set.
4. **Comparative-timeline analysis** — H. pylori declining vs
   P. gingivalis + Demodex rising: how modern environment shifts
   the persistent-organism composition, what this predicts for
   chronic-disease trajectories over the next century.

These are aggregate / synthesis directions rather than per-organism
deep dives.

---

*Filed: 2026-04-15 | biology/evolution/attempts/attempt_010*
*Closes the per-organism series (attempts 002–010 spanning 10 organisms).*
*Companions: attempts 001 (framework), 002–009 (per-organism)*

**Key references (corrected 2026-04-15 audit):**
- Xu J et al. 2007 PNAS 104(47):18730-18735 (PMID 18000048) —
  Malassezia globosa + restricta genomes; FAS pathway absence confirmed
- Wang Q-M et al. 2015 Studies in Mycology 81:55-83 (PMID 25737592)
  — Malasseziomycetes class erection
- Scholz CFP & Kilian M 2016 IJSEM 66(11):4422-4432 — Cutibacterium
  rename from Propionibacterium
- **C. acnes phylotype scheme:** McDowell et al. 2005 (I/II/III);
  Lomholt & Kilian 2010 + McDowell et al. 2012 enhanced MLST
  (IA1/IA2/IB/IC subdivision). [Earlier write-up cited Tomida 2013
  for the phylotype scheme; corrected — Tomida 2013 is strain-level
  genomics, not the phylotype nomenclature.]
- Dagnelie et al. 2019 (PMID 31299116) + Dréno 2018 (PMID 29894579)
  — IA1 84–96% in acne lesions vs ~36–42% in healthy skin; loss of
  phylotype diversity is a driver, not IA1 abundance alone
