# attempt_110 — Protist Immunity and Antigenic Variation in Parasitic Eukaryotes

> Third extension after the main sweep (100-107) and earlier extensions
> on trained immunity (108) and non-retroviral EVEs (109). This
> attempt fills the gap between attempt_102 (eukaryogenesis, ~2 Ga)
> and attempt_103 (invertebrate metazoan innate, ~700-500 Ma) by
> examining unicellular eukaryotes (protists). Two quite different
> aspects appear: (1) Dictyostelium and related social amoebae have
> developed innate-immunity-like sentinel cells analogous to
> metazoan phagocytes, (2) parasitic protists (Trypanosoma,
> Plasmodium, others) have evolved elaborate antigenic-variation
> mechanisms specifically to DEFEAT host adaptive immunity. The
> protist lineage thus shows both the "early innate" side and the
> "counter-adaptive" side of the host-pathogen arms race.

---

## Protists as an evolutionary link

Protists are paraphyletic — "eukaryotes that aren't fungi, plants, or
animals." Dozens of lineages, spanning diverse cellular and ecological
niches. From an immunity standpoint, they occupy a unique position:

- **Free-living protists** (Dictyostelium, Paramecium, Acanthamoeba,
  Tetrahymena, choanoflagellates): single cells or simple colonies.
  Face bacterial predators, viruses, and sometimes each other.
  Develop PHAGOCYTIC and RECOGNITION strategies that prefigure
  metazoan innate immunity.
- **Parasitic protists** (Trypanosoma, Plasmodium, Leishmania,
  Trichomonas, Toxoplasma): inhabit metazoan hosts. Must EVADE host
  immunity. Develop antigenic-variation, intracellular-hiding, and
  immune-modulation strategies at an extreme level.

Both sides illuminate the host-pathogen arms race at a deep
evolutionary level.

## Dictyostelium: the social amoeba immunity model

### Life cycle overview

*Dictyostelium discoideum* alternates between:
- **Solitary amoeba phase**: individual cells feed on bacteria via
  phagocytosis, reproduce by binary fission.
- **Multicellular slug phase** (upon starvation): ~100,000 cells
  aggregate, migrate as a multicellular slug, then form a fruiting
  body with spores.

### Sentinel cells

Within the migrating slug, ~1% of cells become **sentinel (S) cells**
that circulate through the slug body, phagocytose invading bacteria,
produce extracellular traps, and are shed behind the slug as it
migrates. They provide innate-immunity-like defense for the
multicellular body.

Reference: **Chen G, Zhuchenko O, Kuspa A (2007).** "Immune-like
phagocyte activity in the social amoeba." *Science* 317:678-681.
PMID 17673666. Discovery paper for sentinel cells.

### Molecular recognition: TirA

Dictyostelium sentinel cells express **TirA**, a protein with a
Toll/IL-1 receptor (TIR) domain, and **SlrA**, a leucine-rich-repeat
(LRR) protein. Both are enriched in sentinel cells and upregulated
upon bacterial infection (*Legionella pneumophila* tested experimentally).

The TIR domain is the same fold used in mammalian TLR signaling
(attempt_103: the Toll pathway). Its presence in Dictyostelium —
phylogenetically deep in eukaryotes, pre-metazoan — suggests the
TIR-domain signaling module originated BEFORE the origin of animals.
It was repurposed for immunity in multiple eukaryotic lineages
independently or inherited from a deeper common ancestor (still
debated).

Reference: **Chen G, Liu B, Chou PH, Lin S, Manseau J, Zhuchenko O,
Kuspa A (2013).** "Microbial recognition and inflammation-like
behavior by social amoeba sentinel cells." — plus several
follow-up studies from the Kuspa/Shaulsky labs.

### Extracellular traps

Sentinel cells produce extracellular traps made of DNA + histones +
bactericidal proteins, STRUCTURALLY AND FUNCTIONALLY analogous to
neutrophil extracellular traps (NETs) in mammals. This parallel was
surprising — NETs had been thought metazoan-specific. The existence
of amoeba-ETs indicates that this antimicrobial strategy is >1 Ga
old, predating the protist-metazoan split.

### NADPH oxidase and ROS

Dictyostelium encodes NADPH oxidase (NoxA) that produces reactive
oxygen species for antimicrobial killing. NADPH oxidases are deeply
conserved across eukaryotes and are used in phagocyte respiratory
burst in both amoebae and metazoans.

### Ecological context

Dictyostelium provides a living "model amoeba" for understanding:
- How a unicellular eukaryote handles bacterial predators.
- How a multicellular protist-derived organism coordinates
  defense across a cell collective (via sentinel cells).
- Which innate-immunity molecular modules predate metazoans.

## Parasitic protists: antigenic variation

Parasitic protists living in metazoan hosts have evolved extreme
adaptations for evading host adaptive immunity. The most elaborate
is **antigenic variation** — continuous, coordinated switching of
the surface coat so that host antibodies become obsolete.

### Trypanosoma brucei VSG system

African trypanosomes (*T. brucei* and relatives), causative agents
of sleeping sickness, are covered by a dense coat of **variant
surface glycoprotein (VSG)**. Each cell expresses ONE VSG at a
time, from a repertoire of ~2000 VSG genes in the genome.

Mechanism (per Horn 2014 and subsequent work):
- ~15 **expression sites (ES)** exist, each telomeric. Only ONE ES
  is active at a time ("monoallelic expression").
- The active ES is transcribed in a unique sub-nuclear structure
  called the **expression site body** (ESB).
- **Antigenic variation** occurs via:
  - **In situ switching**: active ES is silenced and a different ES
    is activated, moving to the ESB.
  - **Gene conversion**: the VSG in the active ES is over-written by
    a different VSG copied from silent arrays elsewhere in the
    genome.
- Switching rate is ~10⁻³ per cell per generation — enough for the
  population to stay ahead of host antibody response but slow enough
  that individual cells aren't constantly remaking their coat.

Reference: **Horn D (2014).** "Antigenic variation in African
trypanosomes." *Molecular and Biochemical Parasitology* 195:123-129.
PMID 24859277.

More recent: **Faria J, Luzak V, Müller LS, Brink BG, Hutchinson S,
Glover L, Siegel TN, Horn D (2019).** "Monoallelic expression and
epigenetic inheritance sustained by a Trypanosoma brucei variant
surface glycoprotein exclusion complex." *Nature Communications*
10:3023. PMID 31289266. Identification of VEX1/VEX2 exclusion
complex sustaining monoallelic VSG expression.

### Plasmodium var gene / PfEMP1 system

Malaria parasites (*Plasmodium falciparum*) express PfEMP1
(*P. falciparum* Erythrocyte Membrane Protein 1) on the surface of
infected red blood cells. PfEMP1 is encoded by a family of ~60 *var*
genes; only one is expressed at a time; switching occurs through
epigenetic silencing/activation of var loci. Similar to the
trypanosome VSG system but with different molecular machinery.

Reference: **Guizetti J, Scherf A (2013).** "Silence, activate,
poise and switch! Mechanisms of antigenic variation in Plasmodium
falciparum." *Cellular Microbiology* 15:718-726. PMID 23351305.

### Giardia and Trichomonas variable surface proteins

*Giardia lamblia* has ~190 variant-specific surface protein (VSP)
genes, only one expressed at a time. Switching frequency ~6×10⁻⁴
per generation.

### Paramecium surface antigens (i-antigens)

Free-living ciliates also express surface antigens that can switch
— in *Paramecium tetraurelia*, the i-antigen system. Whether this
is anti-predator (amoebae, other eukaryotic predators) or anti-viral
is unclear; clearly not targeting vertebrate adaptive immunity
(paramecia don't live in vertebrates). Suggests antigenic variation
evolved BEFORE encounter with adaptive immunity — possibly as a
general predator/phage evasion mechanism.

## Unifying themes

### Antigenic variation is pan-eukaryotic

From Paramecium to Plasmodium, unrelated unicellular eukaryotes have
evolved remarkably convergent "one-at-a-time expression of
one-of-many genes" solutions. This suggests antigenic variation is
an old strategy in the eukaryotic lineage, possibly predating
specific targeting of vertebrate adaptive immunity.

### Phagocytosis + recognition is also pan-eukaryotic

Dictyostelium's TirA + SlrA + NoxA triad mirrors mammalian
TLR + LRR + NADPH-oxidase trios used by neutrophils and macrophages.
The molecular modules existed in eukaryotic ancestors; different
lineages elaborated them differently.

### Specialized cell types emerged before metazoa

Dictyostelium's sentinel-cell differentiation (1% of slug cells)
shows that cell-type specialization for defense pre-dates animal
multicellularity.

## Contrasts with metazoan immunity

| Feature | Protists | Metazoans |
|---------|----------|-----------|
| Recognition | TirA, LRR proteins, NoxA | TLRs, NLRs, NADPH oxidase, complement |
| Effector cells | Sentinel cells (Dictyostelium) | Macrophages, neutrophils, eosinophils |
| Antimicrobial | Extracellular traps (proto-NETs), ROS | NETs, ROS, AMPs, complement |
| Against adaptive immunity | Antigenic variation (parasitic) | N/A (metazoans HAVE adaptive immunity) |
| Multi-cellular coordination | Partial (slug-stage Dicty) | Full (lymph/blood + signal networks) |

## Why protist immunity matters for the 100-series framework

1. **The TIR domain signaling module pre-dates animals.** attempt_103
   placed Toll pathway at ~600 Ma (metazoan emergence). Dictyostelium
   TirA pushes some version of the module deeper, possibly to the
   common ancestor of Amoebozoa + Opisthokonts (~1-1.5 Ga).

2. **Antigenic variation is a deep eukaryotic strategy.** Not just
   an invention of trypanosomes to defeat adaptive immunity — rather,
   a broader strategy that happens to be especially useful against
   adaptive immunity because of its specificity.

3. **Multicellular coordination of defense predates animals.** The
   sentinel-cell specialization in Dictyostelium shows that division
   of immune labor can emerge in simple multicellular contexts.

## Open questions

1. **When did TIR-domain signaling originate?** If it was in a
   pre-Amoebozoa + pre-Opisthokonta eukaryotic ancestor, it's
   ≥1.5 Ga old. If it was convergent between Amoebozoa and
   metazoans, both independently discovered the module. Current
   phylogenetic evidence leans toward shared ancestry.

2. **Why did free-living ciliates evolve surface-antigen switching?**
   The host-defense explanation works for parasites but not for
   Paramecium. Ecological explanation needed.

3. **How much of trypanosome / Plasmodium antigenic variation is
   actually useful against adaptive immunity versus against innate
   immunity (complement, phagocytic recognition)?** Different
   lineages may have different selective drivers.

4. **Is there "pro-adaptive immunity" in any protist lineage?** No
   protist is known to have anything resembling clonal lymphocyte-
   like adaptive immunity. Trained immunity (attempt_108) may be
   closer to a pan-eukaryotic analog.

## Links to other attempts

- attempt_101 (prokaryotic): CRISPR + Abi + RM systems have
  different molecular basis than protist defenses; common strategy
  at the functional level (distinguish self/non-self, kill invaders).
- attempt_102 (eukaryogenesis): protists inherited bacterial-lineage
  autophagy and apoptosis machinery; added TIR-domain signaling
  and LRR recognition as novelty.
- attempt_103 (invertebrate metazoan innate): protist TirA/LRR/NoxA
  is directly antecedent to metazoan Toll/LRR-receptors/NADPH-oxidase.
  This attempt fills the gap between 102 and 103.
- attempt_107 (persistent-virus coevolution): metazoan persistent
  viruses parallel protist parasites in strategy (evade adaptive
  immunity). The evasion strategies differ in mechanism but
  converge functionally.

## Key sources

Primary:
- **Chen G, Zhuchenko O, Kuspa A 2007 *Science* 317:678** (sentinel
  cells in Dictyostelium). PMID 17673666.
- **Chen G et al. 2013** on Dictyostelium sentinel-cell TirA
  signaling during *Legionella pneumophila* infection.
- **Horn D 2014 *Mol Biochem Parasitol* 195:123** (African
  trypanosome antigenic variation). PMID 24859277.
- **Faria J et al. 2019 *Nat Commun* 10:3023** (VEX1/VEX2 monoallelic
  exclusion complex). PMID 31289266.
- **Guizetti J, Scherf A 2013 *Cell Microbiol* 15:718** (PfEMP1
  switching in *Plasmodium falciparum*). PMID 23351305.

Reviews:
- Dunn JD, Bosmani C, Barisch C, Raykov L, Lefrançois LH, Cardenal-
  Muñoz E, López-Jiménez AT, Soldati T 2017 *Frontiers in
  Immunology* 9:1906 "Eat Prey, Live: Dictyostelium as a model
  for cell-autonomous defenses." PMID 30619239 (Frontiers article).

---

## Gap opened

- **Phylogenetic depth of TIR-domain immunity**: better sampling
  across protist lineages (ciliates, rhodophytes, stramenopiles)
  would clarify how widely TIR-domain signaling was deployed in
  immune contexts before animals.
- **Mechanism of protist antigenic variation in predator (not
  host-immune) context**: the free-living ciliate surface-antigen
  switching is under-studied. Ecological driver partly unclear.
- **Protist antivirus mechanisms**: RNAi is present but
  characterization is thin; new protist defense systems (analogous
  to bacterial CBASS, CRISPR) may await discovery in diverse
  protist lineages.

## Status

Extension complete. The 100-series now has:
- 8 main-sweep attempts (100-107)
- 3 extensions (108 trained immunity, 109 non-retroviral EVEs,
  110 protist immunity)
- gap.md
- 4 audit rounds on 10 attempts (100-109); this is attempt 11
  (attempt_110) which will need auditing in a future round.

Additional extensions for 111+ could cover: mucosal immunology
evolution; placental tolerance comparative genetics by mammalian
lineage; host-commensal coevolution.

---

*Filed: 2026-04-15 | biology/evolution/attempts/attempt_110*
*Extension after main sweep; fills the gap between attempts 102 (eukaryogenesis)*
*and 103 (invertebrate metazoan).*
*Parallel-instance convention: 100-199 range; 001-099 is other instance's scope.*
