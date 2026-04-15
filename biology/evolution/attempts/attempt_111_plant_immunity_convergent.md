# attempt_111 — Plant Immunity: The Convergent Case

> Fourth extension after the main sweep (100-107) and prior extensions
> (108 trained immunity, 109 non-retroviral EVEs, 110 protist
> immunity). Plants and animals diverged at the base of the
> eukaryotic tree (~1.5-1.6 Ga). They independently evolved
> elaborate innate immunity using some of the SAME molecular modules
> (LRRs, NLRs, kinases) but in different architectural arrangements.
> Plants do NOT have V(D)J-style adaptive immunity; they rely
> entirely on innate mechanisms. This makes plant immunity an ideal
> "convergent case" for understanding which immune features are
> evolutionarily constrained vs contingent.

---

## The plant-animal divergence

Plants (Archaeplastida) and animals (Opisthokonta → Metazoa) share a
common eukaryotic ancestor but diverged in the deep eukaryotic tree.
Molecular clock estimates: plant-animal divergence ~1.5-1.6 Ga.

Both lineages face microbial pathogens (bacteria, fungi, oomycetes,
viruses) and pests. Both evolved innate immunity. But the
implementations differ:

- Animals have a circulatory system, mobile immune cells
  (lymphocytes, phagocytes), and V(D)J-based adaptive immunity in
  vertebrates.
- Plants lack circulation and mobile immune cells; defense is
  cell-autonomous at every cell. Plants have NO adaptive immunity
  in the lymphocyte sense.

Selection pressures drove convergence on pattern recognition
receptors (PRRs) + NLR proteins + rapid inducible defense.

## The zigzag model

The canonical framework for plant immunity:

**Jones JDG, Dangl JL (2006).** "The plant immune system." *Nature*
444:323-329. DOI 10.1038/nature05286. The "zigzag" coevolutionary
model.

Four phases:

1. **PTI (Pattern-Triggered Immunity)**: PRRs at the plant cell
   surface detect conserved pathogen molecules (MAMPs/PAMPs) —
   bacterial flagellin (flg22), fungal chitin, bacterial EF-Tu.
   PRRs activate defense responses: ROS burst, MAPK cascade, callose
   deposition, defense gene expression.

2. **Effector-triggered susceptibility (ETS)**: pathogens deliver
   EFFECTORS into plant cells (via Type III secretion in bacteria,
   haustoria in fungi/oomycetes) that suppress PTI and enable
   infection.

3. **ETI (Effector-Triggered Immunity)**: plant NLR proteins
   (intracellular receptors with Nucleotide-Binding + LRR domains)
   recognize effectors (or their activity on host targets) and
   trigger a strong defense response, often including the
   **hypersensitive response (HR)** — localized programmed cell
   death that isolates the pathogen.

4. **Effector turnover**: over evolutionary time, pathogens lose
   effectors recognized by plant NLRs (escaping ETI) and gain new
   ones. Plants evolve new NLRs. The arms race continues.

## The molecular players

### Pattern recognition receptors (PRRs)

- **FLS2**: the flagellin receptor, recognizing bacterial flg22
  epitope via LRR ectodomain. The classic plant PRR.
  Reference: **Gómez-Gómez L, Boller T (2000).** "FLS2: an LRR
  receptor-like kinase involved in the perception of the bacterial
  elicitor flagellin in Arabidopsis." *Molecular Cell* 5:1003-1011.
  PMID 10911994.

- **EFR**: receptor for bacterial EF-Tu. Brassica-specific.

- **CERK1**: chitin receptor (fungal cell wall).

- **BAK1**: co-receptor that pairs with multiple PRRs (FLS2, EFR,
  others). Mutants have broad susceptibility.

Plant PRRs use LRR + kinase domains, functionally analogous but
evolutionarily distinct from animal TLRs (which use LRR + TIR
domains).

### NLR proteins (intracellular receptors)

Plants have large NLR families — Arabidopsis ~150, rice ~400-500,
some wheat cultivars >1500 NLR genes. Each NLR can potentially
recognize a different pathogen effector.

NLR structure: NB (nucleotide-binding) + ARC (helical module) + LRR
(specificity) + sometimes TIR or CC (coiled-coil) N-terminal.

Two main classes based on N-terminus:
- **TNL**: TIR-containing NLRs (dominant in dicots).
- **CNL**: Coiled-coil NLRs (dominant in monocots).

Reference: **Jones JDG, Vance RE, Dangl JL (2016).** "Intracellular
innate immune surveillance devices in plants and animals."
*Science* 354(6316):aaf6395. PMID 27934708. Direct comparison
framework.

### Recognition mechanisms

Plant NLRs can recognize effectors via:
- **Direct binding** of effector (rare).
- **Guarding** of host proteins that effectors target: NLR monitors
  a host protein; if the protein is modified by an effector, the
  NLR triggers. This is the "decoy hypothesis" / "guard model."
  Canonical example: RPM1 guards RIN4, which is targeted by
  bacterial effector AvrRpm1. When AvrRpm1 phosphorylates RIN4,
  RPM1 activates defense.

### Rapid signaling

Plant immune signaling produces within minutes:
- **ROS burst** via NADPH oxidase (RBOH gene family)
- **Calcium flux**
- **MAPK cascades** (MPK3, MPK6 most studied)
- **Hormone signaling** (salicylic acid for biotrophs; jasmonic acid
  + ethylene for necrotrophs)

## Systemic Acquired Resistance (SAR)

Plants develop **systemic** resistance after a local pathogen
challenge: tissues DISTANT from the infection site become primed
for defense. This lasts days to weeks, even months. SAR is
mediated by salicylic acid + methylsalicylate transport + volatile
signals.

**Durrant WE, Dong X (2004).** "Systemic acquired resistance."
*Annual Review of Phytopathology* 42:185-209. PMID 15283665.

SAR is a plant analog of **trained immunity** (attempt_108). Both
involve:
- Priming for faster / stronger response to subsequent challenge.
- Epigenetic changes maintaining the primed state.
- Non-specific benefit across pathogen types.

The convergence is striking — plants and animals independently
evolved systemic/trained enhancement of innate immunity after local
challenge. Functionally indistinguishable at the behavioral level;
molecularly distinct.

## RNAi as antiviral immunity

Plants rely heavily on RNAi for antiviral defense (attempt_102's
RNAi discussion). Because plants lack interferon signaling (animal
vertebrate pathway), RNAi is the PRIMARY antiviral mechanism:

- **Dicer-like (DCL) enzymes** process viral dsRNA into siRNAs.
- **Argonaute proteins** (AGO1, AGO2, etc.) use siRNAs to target
  viral mRNAs.
- **RNA-dependent RNA polymerases** (RDRs) amplify the siRNA signal.

Plant viruses counter with **viral suppressors of RNA silencing
(VSRs)** — nearly every plant virus has one or more. The
plant-virus arms race plays out at the RNAi level in a way that
the animal arms race only partly does.

## What plants don't have

- No circulating immune cells (no blood, no lymphocytes).
- No somatic gene rearrangement (no V(D)J).
- No clonal selection of rearranged receptors.
- No interferon system.
- No classical antibodies.

Instead plants:
- Make each cell a defender (cell-autonomous immunity).
- Diversify PRR/NLR repertoires in the GERMLINE (not somatically).
- Use sub-functional redundancy and rapid gene duplication to
  cope with pathogen variation.

## Gene-for-gene coevolution (Flor 1942, 1971)

The original observation of plant-pathogen coevolution:

**Flor HH (1942).** "Inheritance of pathogenicity in *Melampsora
lini*." *Phytopathology* 32:653-669.
**Flor HH (1971).** "Current status of the gene-for-gene concept."
*Annual Review of Phytopathology* 9:275-296.

Classical observation: for each plant R (resistance) gene, the
pathogen has a corresponding avr (avirulence) gene. Plant R + pathogen
avr match → resistance. Mismatch → susceptibility.

Gene-for-gene predates the molecular understanding but accurately
predicted the ETI phenomenon — plant R genes turned out to be NLRs
recognizing pathogen avr gene products (effectors).

## Convergent vs divergent features

### Convergent with animal immunity

- **LRR + kinase** signaling modules (plants: FLS2+BAK1; animals:
  TLR/IL-1 receptor related).
- **NLR architecture** (plants: TNL/CNL; animals: NLRP3, NOD1/2).
  Note: although architecturally similar, the specific NLRs are
  NOT homologous between plants and animals — they independently
  evolved from shared eukaryotic NB-ARC-LRR or NACHT-LRR scaffolds.
- **Hypersensitive response / programmed cell death** for local
  isolation (plants: HR; animals: apoptosis/pyroptosis of infected
  cells).
- **ROS burst** via NADPH oxidase.
- **Systemic memory** (plants: SAR; animals: trained immunity).

### Divergent

- **Mobile immune cells** (animals only).
- **Adaptive immunity via V(D)J** (vertebrates only).
- **RNAi primacy for antiviral** (plants + invertebrates; reduced
  in vertebrates).
- **Germline vs somatic receptor diversification** (plants: all
  germline; vertebrates: somatic for V(D)J/TCR/BCR).
- **Hormone-based signaling** (plants: SA/JA/ET; animals: cytokines).

## Why plants evolved this specific set of solutions

Ecological constraints:

1. **Sessile lifestyle**: plants cannot move to escape pathogens.
   Requires per-cell defense + extensive sensing.
2. **Wall-bound cells**: cell walls prevent cell-cell migration
   of immune cells. Circulating phagocytes wouldn't work.
3. **Autotrophy**: plants don't need phagocytosis for feeding.
   Phagocytic machinery not a pre-adaptation available.
4. **Open development**: plants can regenerate lost tissue.
   Sacrificial HR is relatively cheap.
5. **Large germline-to-body continuity**: every plant cell can
   potentially contribute to seeds. Somatic mutation would be
   inherited. Hence germline-only diversification.

Animals took the opposite ecological path: mobile, phagocytic
(feeding), closed development, dedicated germline, mobile defense
cells. Different problem → different solution.

## Implications for the 100-series framework

### Expanding the "convergent adaptive immunity" story

attempt_104 described ONE instance of convergent adaptive immunity
in vertebrates (VLR vs V(D)J). Plant immunity is a DIFFERENT
convergent case — innate immunity converging on PRR + NLR + HR
architecture despite ~1.5 Ga separation from animals.

The full set of convergent immune-system designs across life:

| Clade | Defense | Common module |
|-------|---------|----------------|
| Prokaryotes | CRISPR, RM, CBASS | Varied |
| Protists | TirA/LRR, antigenic variation | TIR, LRR |
| Invertebrates | Toll/IMD, complement | TIR, LRR, NLR, complement |
| Vertebrates (jawed) | V(D)J adaptive + innate | All above + RAG, MHC |
| Vertebrates (jawless) | VLR adaptive + innate | LRR-based adaptive + innate common |
| **Plants** | **PRR + NLR + HR + SAR + RNAi** | **LRR, NB-ARC, kinase** |

Plants fill the "immune without mobile cells" row and show that
elaborate multi-mechanism immunity can evolve without cells of
dedicated immune lineages.

### Filling the tree

attempt_100 framed immunity as a "layered architecture built over
3.5 billion years." The plant branch shows that DIFFERENT
architectures can solve the immune problem on different trunk
branches. The layered-architecture framing is animal-centric.

For cross-species generalization: there is no single "immune system"
built up by addition. There are MULTIPLE immune systems, each
tailored to the ecological and developmental constraints of its
lineage.

## Open questions

1. **How did plant NLRs so greatly expand (150-1500 in different
   species)?** Appears to involve rapid tandem duplication + gene
   conversion + positive selection. Complete models are partial.

2. **Do plants have any form of "memory" beyond SAR?** Recent
   evidence for transgenerational priming (epigenetic transmission
   of defense-primed state to offspring) in *Arabidopsis* and
   crops.

3. **Can plant immune strategies be adapted for medical/veterinary
   use?** Synthetic plant NLRs have been constructed; potentially
   engineered to recognize specific pathogens. Under active
   development for crop biotechnology, with some medical
   analogs (synthetic innate-immune receptors for therapy).

4. **What explains the very different NLR expansions in rice
   (~500) vs Arabidopsis (~150) vs wheat (>1500)?** Possibly
   reflects the specific pathogen pressures each lineage has
   faced, but also polyploidy histories in wheat.

## Links to other attempts

- attempt_101 (prokaryotic): CRISPR is prokaryotic adaptive;
  plants rely on RNAi for analogous antiviral function (attempt_102).
- attempt_103 (invertebrate metazoan innate): Toll pathway
  functional homolog to plant PTI; plant NLRs are architecturally
  parallel to animal NLRs.
- attempt_108 (trained immunity): SAR is the plant analog.
- attempt_110 (protist immunity): protist TIR-domain signaling
  (Dictyostelium) is an intermediate case between prokaryotes and
  animals/plants.

## Key sources

Primary / foundational:
- **Flor HH 1942 *Phytopathology* 32:653** (gene-for-gene).
- **Flor HH 1971 *Annu Rev Phytopathol* 9:275** (gene-for-gene
  concept review).
- **Gómez-Gómez L, Boller T 2000 *Mol Cell* 5:1003** (FLS2
  flagellin receptor). PMID 10911994.
- **Jones JDG, Dangl JL 2006 *Nature* 444:323** (zigzag model).
  DOI 10.1038/nature05286.
- **Chisholm ST, Coaker G, Day B, Staskawicz BJ 2006 *Cell*
  124:803** (host-microbe interactions).
- **Jones JDG, Vance RE, Dangl JL 2016 *Science* 354:aaf6395**
  (plant vs animal intracellular innate surveillance). PMID
  27934708.

Reviews:
- Boller T, Felix G 2009 *Annu Rev Plant Biol* 60:379 (elicitor
  perception).
- Durrant WE, Dong X 2004 *Annu Rev Phytopathol* 42:185 (SAR).
  PMID 15283665.
- Ausubel FM 2005 *Nat Immunol* 6:973 (innate immunity signaling
  plants vs animals).
- Cui H, Tsuda K, Parker JE 2015 *Annu Rev Plant Biol* 66:487
  (effector-triggered immunity review).

---

## Gap opened

- **Plant-animal NLR homology status**: are the NLR families
  truly independent inventions (convergent), or do they share a
  deep eukaryotic ancestor? Current evidence is mixed; better
  phylogenies needed.
- **Plant trained-immunity / SAR molecular mechanism**: partial
  understanding of the SA-methylSA-volatile signaling; less
  understood is the epigenetic maintenance in distal tissues.
- **Viral evasion of plant RNAi**: VSRs are characterized for many
  plant viruses but their evolution across plant-virus phylogenies
  is only partly mapped.

## Status

Extension complete. The 100-series now has:
- 8 main-sweep attempts (100-107)
- 4 extensions (108 trained immunity, 109 non-retroviral EVEs,
  110 protist immunity, 111 plant immunity)
- gap.md
- 4 audit rounds (100-109 audited so far; 110-111 await round 5)

The plant-immunity addition is a strong cross-kingdom comparison
that strengthens the "multiple independent immune systems" framing
of the 100-series.

---

*Filed: 2026-04-15 | biology/evolution/attempts/attempt_111*
*Extension after main sweep; cross-kingdom comparison of convergent immune architectures.*
*Parallel-instance convention: 100-199 range; 001-099 is other instance's scope.*
