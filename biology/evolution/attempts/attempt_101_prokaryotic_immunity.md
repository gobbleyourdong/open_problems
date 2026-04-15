# attempt_101 — Prokaryotic Immunity: The First 3 Billion Years

> First layer of the layered-architecture framework from attempt_100.
> Prokaryotes (archaea + bacteria) have been fighting viruses (phages)
> and mobile genetic elements for ~3.5 billion years. Their defense
> systems are more numerous, more diverse, and more recently
> discovered than typical textbooks suggest. A modern bacterium carries
> 5-10 distinct anti-phage systems simultaneously.

---

## The scale of the problem

Bacteriophages are the most abundant biological entities on Earth:
~10³¹ phages globally, ~10⁹ per mL of seawater, ~10¹⁰ per gram of
soil. Phage-bacteria predator-prey dynamics drive 10²⁴ phage infections
per second in the oceans alone.

Selection pressure on anti-phage systems has been relentless for
the entire history of cellular life. What appears as "many parallel
defense layers" in modern prokaryotes is the accumulated stack of
solutions that worked; the ones that didn't work are extinct.

## The defense-systems landscape (modern view)

The last decade has dramatically expanded the catalog. Pre-2018, the
textbook view was: restriction-modification (RM), CRISPR-Cas,
abortive infection (Abi), and toxin-antitoxin (TA). Post-2018, driven
largely by Rotem Sorek's lab and others doing systematic bioinformatic
and experimental discovery, dozens more systems are recognized.

Major discovery papers:
- **Doron S et al. (2018).** "Systematic discovery of antiphage defense
  systems in the microbial pangenome." *Science* 359(6379):eaar4120.
  PMID 29371424. Identified 9 new defense systems (BREX, DISARM, Gabija,
  Druantia, Hachiman, Kiwa, Lamassu, Septu, Thoeris, Zorya, and others).
- **Gao L et al. (2020).** "Diverse enzymatic activities mediate
  antiviral immunity in prokaryotes." *Science* 369(6507):1077-1084.
  Revealed CBASS (cyclic-oligonucleotide-based anti-phage signaling
  system) — prokaryotic analog of the cGAS-STING innate pathway.
- **Bernheim A, Sorek R (2020).** "The pan-immune system of bacteria:
  antiviral defence as a community resource." *Nat Rev Microbiol*
  18:113-119. DOI 10.1038/s41579-019-0278-2.

The "pan-immune system" framing is the best modern view: individual
bacteria carry a subset of defense systems; populations collectively
present a diverse-and-redundant defense suite that phages must
navigate. Horizontal gene transfer of defense modules between strains
is a major dynamic.

## System 1: Restriction-modification (RM) — the ur-immunity

### Discovery

Werner Arber, Hamilton Smith, and Daniel Nathans shared the 1978 Nobel
Prize in Physiology or Medicine for "the discovery of restriction
enzymes and their application to problems of molecular genetics."
Arber's work (with Dussoix) in the early 1960s established that
certain bacteria "restrict" incoming phage DNA — cleaving foreign DNA
while protecting self-DNA via methylation.

### Mechanism

- A methyltransferase methylates specific recognition sequences on
  host DNA (self-tag).
- A restriction endonuclease cleaves the same recognition sequences
  when UNmethylated (foreign).
- Invading phage DNA enters the cell unmethylated; the restriction
  enzyme shreds it before replication completes.

### Classification

Four major types (I, II, III, IV) based on subunit composition, cleavage
mechanism, and cofactor requirements. Type II (ex: EcoRI) is the
familiar "cuts at specific sequences" enzyme that launched molecular
cloning; Types I, III, IV have more complex architectures.

### Evolutionary significance

RM systems are **universally present** across bacteria and archaea,
often in multiple copies per genome. They predate CRISPR-Cas
phylogenetically and represent the baseline defense layer. RM is
short-term "innate" immunity: immediate, non-adaptive, based on
distinguishing self (methylated) from non-self (unmethylated).

Limitations: phages that acquire host methylation (via transient
encounters, or by encoding their own methyltransferase) escape RM.
This creates an evolutionary arms race but not adaptive memory — RM
cannot "remember" past infections.

## System 2: CRISPR-Cas — adaptive immunity in bacteria

### Discovery timeline

- **1987**: Ishino Y et al. (*J Bacteriol* 169:5429). First observation
  of the 29-nt repeats in *E. coli* iap gene; function unknown.
- **2002**: Jansen R et al. coin the term "CRISPR" (Clustered Regularly
  Interspaced Short Palindromic Repeats) and identify associated Cas genes.
- **2005**: Mojica FJ et al. (*J Mol Evol* 60:174). PMID 15791728. The
  **foreign-origin hypothesis**: spacer sequences between the repeats
  match phage and plasmid DNA. Proposed CRISPR is an immune system.
- **2007**: Barrangou R et al. (*Science* 315:1709). PMID 17379808.
  Experimental demonstration in *Streptococcus thermophilus*:
  inserting a phage-derived spacer into CRISPR confers resistance to
  that phage; removing it restores sensitivity.
- **2008**: Brouns SJ et al. (*Science* 321:960) identify the Cascade
  complex in *E. coli* (Type I system). Marraffini & Sontheimer
  (*Science* 322:1843) show DNA (not just RNA) is targeted.
- **2011**: Deltcheva E et al. (*Nature* 471:602) identify tracrRNA in
  *S. pyogenes* Type II system.
- **2012**: Jinek M et al. (*Science* 337:816). PMID 22745249. The
  key programmability demonstration: Cas9 + sgRNA cleaves any target
  DNA sequence. Opens genome editing applications.
- **2020**: Makarova KS et al. (*Nat Rev Microbiol* 18:67). PMID
  31857715. Modern comprehensive classification: 2 classes, 6 types
  (I, II, III, IV, V, VI), 33+ subtypes.

### Mechanism (simplified)

Three phases:

1. **Adaptation (spacer acquisition)**: Cas1-Cas2 complex captures
   fragments of foreign DNA and integrates them as new spacers at the
   leader end of the CRISPR array. The bacterium now has a "memory" of
   this invader.

2. **Expression (crRNA biogenesis)**: the CRISPR array is transcribed
   as a long pre-crRNA; processing enzymes cleave it into mature
   crRNAs, each carrying one spacer sequence.

3. **Interference (target cleavage)**: crRNA guides an effector
   complex (Cascade for Type I; Cas9 for Type II; Cas12a/Cas13 for V/VI)
   to foreign DNA or RNA matching the spacer. The effector cleaves the
   target.

### Why it qualifies as "adaptive" immunity

CRISPR-Cas has the three hallmarks of adaptive immunity:
- **Specificity**: spacer sequence determines target.
- **Memory**: integrated spacers persist across generations.
- **Self/non-self discrimination**: self DNA doesn't match any spacer
  (and PAM sequences on foreign DNA distinguish targets).

It is the ONLY prokaryotic system with these three features. This is
why CRISPR-Cas is sometimes described as the bacterial/archaeal
"adaptive immune system" — even though its molecular machinery is
completely unrelated to vertebrate VLR or V(D)J systems (independent
evolutionary origin).

### Classification (Makarova 2020)

- **Class 1** (Types I, III, IV): effector is a multi-subunit complex
  (Cascade or Csm/Cmr).
- **Class 2** (Types II, V, VI): effector is a single large protein.
  - Type II: Cas9 (DNA, dual RuvC+HNH nucleases)
  - Type V: Cas12 family (DNA, single RuvC-like nuclease)
  - Type VI: Cas13 family (RNA, HEPN nucleases)

Class 2 systems are the basis of modern genome editing; Class 1 is
more common in nature and likely more ancient.

## System 3: Abortive infection (Abi) — sacrifice the infected cell

Abi systems detect phage infection and kill the infected cell before
the phage completes its replication cycle. The infected cell dies; the
neighboring uninfected cells in the colony survive.

This is altruistic defense at the cell level: analogous to programmed
cell death (apoptosis) in metazoans. In a clonal microbial population,
killing one infected cell to save many kin is favored by kin selection.

Examples: Rex system of phage lambda lysogens; RM systems can also
act as Abi if they're overwhelmed. Many of the new defense systems
discovered since 2018 (e.g., Thoeris, CBASS) operate as Abi — they
trigger widespread cellular damage (NAD+ depletion, membrane
permeabilization) when phage infection is detected.

**CBASS (Cyclic Oligonucleotide-Based Anti-phage Signaling System)**:
a prokaryotic homolog of the mammalian cGAS-STING pathway. A cyclase
(cGAS-like) detects phage infection and synthesizes a cyclic
oligonucleotide second messenger, which activates an effector (often
a phospholipase or nuclease) that kills the cell. This is one of the
most striking findings of the post-2018 defense-systems wave: the
cGAS-STING pathway in human innate immunity has bacterial ancestry
~3 billion years deep.

Reference: Cohen D et al. (2019) "Cyclic GMP-AMP signalling protects
bacteria against viral infection." *Nature* 574:691-695. PMID 31533127.

## System 4: Toxin-antitoxin (TA) — poison the invader

TA systems encode a toxin (usually protein, sometimes RNA) and an
antitoxin that neutralizes it. Under normal conditions, antitoxin is
abundant and keeps toxin inert. Under stress (phage infection, nutrient
starvation), antitoxin degrades faster than toxin; free toxin damages
the cell (e.g., mRNA endoribonucleases cleaving cellular transcripts,
DNA gyrase inhibitors halting replication).

The cell can survive the TA activation if the stress abates; otherwise
it dies. TA systems are widespread in plasmids (where they act as
plasmid-maintenance "addiction" modules) and chromosomes (where they
contribute to phage defense and persistence).

Types I-VIII TA systems are classified by the biochemistry of toxin
and antitoxin (protein-protein, RNA-protein, RNA-RNA, etc.).

## System 5: BREX, DISARM, Gabija, Thoeris, Zorya, and the new frontier

The 2018-2023 wave of systematic anti-phage defense discovery has
identified 60+ distinct defense systems beyond the textbook four. Most
have partially-characterized mechanisms:

- **BREX (Bacteriophage Exclusion)**: methylation-based, but distinct
  from RM — methylates at specific sequences and excludes phage at a
  post-adsorption step.
- **DISARM**: phospholipase-based protection.
- **Gabija**: nuclease system, likely degrades phage DNA.
- **Thoeris**: NADase-based Abi system; triggers NAD+ depletion on
  phage infection.
- **Zorya**: proton-motive-force-coupled system.
- **Druantia, Hachiman, Kiwa, Lamassu, Septu**: various activities.

Reference: https://defensefinder.mdmparis.fr — the Abby 2023 online
database currently lists ~150 defense system families with tools to
detect them in any bacterial genome.

## Retron and Pycsar systems

- **Retron** systems (Millman 2020): reverse-transcriptase-containing
  defenses that produce multicopy single-stranded DNA (msDNA) as an
  immune signal. Trigger cell death on phage infection.
  Reference: Millman A et al. (2020) "Bacterial Retrons Function In
  Anti-Phage Defense." *Cell* 183:1551. PMID 33157039.

- **Pycsar** (Tal 2021): pyrimidine-based cyclic signaling, cousin of
  CBASS. Operates similarly but uses cyclic UMP/CMP instead of cyclic
  GMP/AMP.

## Why this matters for the layered-architecture framework

Prokaryotic immunity has FOUR properties that persist up the tree:

1. **Distinguishing self from non-self**: methylation in RM is the
   first molecular implementation of the self-tag concept that MHC
   later elaborates in vertebrates.

2. **Memory via sequence-specific recognition**: CRISPR spacers
   presage the antigen-specific memory of B/T cells. Different
   molecular mechanism (DNA spacers vs TCR/BCR), same functional role.

3. **Altruistic cell death as a defense strategy**: Abi systems
   foreshadow apoptosis and pyroptosis. Killing an infected cell to
   save the colony/tissue is 3 Ga old.

4. **Conserved second-messenger signaling**: CBASS → cGAS-STING.
   The cyclic dinucleotide signaling architecture is preserved across
   the entire cellular tree of life.

These are not "homologies in the strict cladistic sense" in all cases
— some are convergent solutions to the same selection pressure — but
the recurrence of the underlying themes reveals which defense
strategies are evolutionarily stable.

## Open questions

1. **Why do different bacterial strains carry such different defense
   repertoires?** A *Pseudomonas* strain and an *E. coli* strain might
   share only 2-3 of their 8 anti-phage systems. Is this driven by
   specific local phage communities, or by fitness trade-offs?

2. **Is there a limit to how many defense systems a single cell can
   carry?** Each system costs energy, imposes risk of autoimmunity
   (own DNA being restricted, own toxin leaking). Estimated cap: ~12
   systems per genome.

3. **How did phage-defense-system diversity co-evolve with phage
   counter-defense?** Phages encode anti-CRISPR proteins (Acrs, first
   found by Davidson lab 2013). The arms race has produced rich
   structural diversity on both sides.

4. **What fraction of bacterial genomes encodes defense?** Recent
   estimates: 5-15% of a typical bacterial genome is defense-related.
   This is a substantial energetic commitment.

5. **How do "novel" defense systems keep being discovered?** The
   pre-2018 view (4 main systems) was wrong by an order of magnitude.
   Are we now near completion, or will another 60 systems be found by
   2030?

## Links to other attempts

- attempt_100 (framework): this attempt populates the "prokaryotic
  layer (~3.5 Ga)" row of the timeline.
- attempt_102 (eukaryogenesis, planned): mitochondrial ancestors were
  bacteria — they brought their defense systems. Autophagy and
  apoptosis in eukaryotes have bacterial-lineage roots.
- attempt_107 (persistent-virus coevolution, planned): the cGAS-STING /
  CBASS homology is the deepest immunity-relevant cross-link.

## Key sources

Primary:
- Mojica FJ et al. 2005 *J Mol Evol* 60:174 (CRISPR foreign-origin hypothesis)
- Barrangou R et al. 2007 *Science* 315:1709 (CRISPR functional demo)
- Jinek M et al. 2012 *Science* 337:816 (programmable Cas9)
- Makarova KS et al. 2020 *Nat Rev Microbiol* 18:67 (classification)
- Doron S et al. 2018 *Science* 359:eaar4120 (9 new defense systems)
- Cohen D et al. 2019 *Nature* 574:691 (CBASS / cyclic GMP-AMP in bacteria)
- Gao L et al. 2020 *Science* 369:1077 (enzymatic diversity of defenses)
- Millman A et al. 2020 *Cell* 183:1551 (Retrons as anti-phage)

Reviews:
- Bernheim A, Sorek R 2020 *Nat Rev Microbiol* 18:113 (pan-immune system)
- Koonin EV, Makarova KS 2022 *Nat Rev Microbiol* 20:711 (evolutionary
  classification of CRISPR-Cas)

Historical:
- Arber W, Dussoix D 1962 *J Mol Biol* 5:18 (restriction-modification)
- Nobel Prize 1978 (Arber, Smith, Nathans — restriction enzymes)

---

## Gap opened

- **Structural**: prokaryotic defense is FAR richer than textbook
  presentations. Downstream attempts that reach for "bacterial
  homologs of X" should consult Sorek-lab and Makarova-lab catalogs,
  not pre-2018 reviews.
- **Cross-kingdom**: the cGAS-STING pathway in metazoan innate
  immunity has bacterial ancestry (CBASS, ~3 Ga). This should be
  cited in attempt_103 / attempt_107 when that pathway is discussed.

## Status

Complete. attempt_102 (eukaryogenesis + early innate emergence) is
next.

---

*Filed: 2026-04-15 | biology/evolution/attempts/attempt_101*
*Follows: attempt_100 (framework)*
*Parallel-instance convention: 100-199 range; 001-099 is other instance's scope.*
