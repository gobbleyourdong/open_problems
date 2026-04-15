# attempt_102 — Eukaryogenesis and the Emergence of Eukaryotic Innate Defense

> Second attempt in the 100-series. Traces what happened to defense
> systems when an archaeon engulfed an alphaproteobacterium ~2 Ga ago
> and the resulting chimeric cell became the first eukaryote.
> Roughly half of eukaryotic genes are archaeal-derived (informational:
> transcription, translation); the other half are bacterial-derived
> (operational: metabolism, membranes). Defense systems were
> reinvented at least three times in this transition.

---

## The eukaryogenesis event

### Two-domain origin of eukaryotes

The long-held "three domains" (archaea, bacteria, eukaryotes) view has
shifted in the last decade to a **two-domain** view: eukaryotes arose
within the Archaea, specifically from an Asgard-archaeal lineage.

Key discovery: **Spang A et al. (2015).** "Complex archaea that bridge
the gap between prokaryotes and eukaryotes." *Nature* 521:173-179.
PMID 25945739. The Lokiarchaeota (named after a deep-sea hydrothermal
vent site near Loki's Castle) encoded proteins previously thought to
be eukaryote-specific (actin-cytoskeleton-related, membrane
trafficking).

Follow-up: **Imachi H et al. (2020).** "Isolation of an archaeon at
the prokaryote-eukaryote interface." *Nature* 577:519-525. PMID
31942073. First CULTIVATION of an Asgard archaeon (*Prometheoarchaeum
syntrophicum*) after 12 years of deep-sea sediment enrichment. Showed
these archaea form protrusions and engage in syntrophy with partners —
physical behavior consistent with an engulfment precursor.

### The mitochondrial ancestor

~2 Ga ago (timing uncertain, range 1.5-2.5 Ga), an Asgard-archaeal
host cell acquired an alphaproteobacterial endosymbiont that became
the mitochondrion. The endosymbiont's genome shrank drastically
(from ~4000 genes to ~13-40 in modern mitochondrial genomes); most of
its genes either disappeared or transferred to the host nuclear
genome.

Two competing models:
- **Hydrogen hypothesis** (Martin & Muller 1998 *Nature* 392:37): the
  host archaeon fed on H₂ produced anaerobically by the endosymbiont.
  Selects for tight metabolic coupling.
- **Oxygen syntrophy hypothesis**: the endosymbiont detoxified O₂ as
  Earth's atmosphere oxygenated (Great Oxygenation Event ~2.4 Ga).

Both may be true at different stages.

## Defense systems in the transition

### What got lost

**CRISPR-Cas**: effectively ABSENT in eukaryotes. The reasons are not
fully settled, but likely:
- CRISPR requires precise integration of spacers — the eukaryotic
  mess of introns, chromatin, and heterochromatin makes this harder.
- Eukaryotic cell size (~10-100× bacterial volume) slows the kinetics
  of phage-vs-cell encounters.
- Eukaryotes rely on RNA-based systems (RNAi) and cellular
  compartmentalization (nuclear envelope) instead.
- Cas genes are occasionally found in eukaryotic genomes but as
  decayed fragments, not functional systems.

**Restriction-modification (RM)**: effectively ABSENT in eukaryotes.
Methylation still exists (5mC, 6mA) but serves gene regulation, not
self/non-self discrimination against foreign DNA. The nuclear envelope
is a better defense against random foreign DNA than the restriction
approach.

### What got repurposed or inherited

**Autophagy (and mitophagy)**: the degradation pathway that eats
damaged organelles and proteins is universally eukaryotic. Its origin
is tied to the mitochondrial endosymbiosis — early eukaryotes
needed a way to sequester and digest residual bacterial components,
then to recycle damaged mitochondria.

- **Ohsumi Y** won the 2016 Nobel Prize in Physiology or Medicine
  "for his discoveries of mechanisms for autophagy." His key yeast
  ATG gene screens (from the 1990s) identified the core autophagy
  machinery present in all eukaryotes.
- **Mitophagy**: PINK1/Parkin pathway (in animals) and analogous
  systems in yeast (Atg32) target damaged mitochondria for autophagy.
  When a mitochondrion loses its membrane potential, PINK1 accumulates
  on the outer membrane and recruits Parkin, which ubiquitinates
  outer-membrane proteins, flagging the organelle for engulfment.
- **Xenophagy**: the adaptation of autophagy to target intracellular
  pathogens. A virus or intracellular bacterium (Salmonella, Listeria,
  Mycobacterium) that enters the cytoplasm is recognized by autophagy
  receptors (p62/SQSTM1, NDP52, OPTN) and sequestered into
  autophagosomes. Xenophagy is a key component of cell-autonomous
  innate immunity in modern eukaryotes including humans.

Reference for xenophagy review: Deretic V, Kroemer G (2022) "Autophagy
in metabolism and quality control: opposing, complementary or
interlinked functions?" *Autophagy* 18:283-292. And an earlier
classic: Levine B et al. (2011) "Autophagy in immunity and
inflammation." *Nature* 469:323-335. PMID 21248839.

### What got newly evolved

**RNA interference (RNAi)**: a eukaryote-specific antiviral and
gene-regulatory system. Discovered by Fire and Mello:

**Fire A, Mello C et al. (1998).** "Potent and specific genetic
interference by double-stranded RNA in *Caenorhabditis elegans*."
*Nature* 391:806-811. PMID 9486653. Nobel Prize 2006.

Mechanism:
- Double-stranded RNA (dsRNA) is processed by Dicer into small
  interfering RNAs (siRNAs) of ~21-23 nt.
- siRNAs are loaded into Argonaute-containing RISC complexes.
- Guide strand directs Argonaute to cleave complementary mRNAs.

As antiviral: RNA viruses replicate through dsRNA intermediates;
transposons and retroviruses produce dsRNA. RNAi detects these and
silences them. This is THE primary antiviral mechanism in plants,
fungi, and invertebrates.

Key point: in VERTEBRATES, the antiviral role of RNAi has been
partially supplanted by interferon-based responses (see attempt_103).
RNAi in vertebrates is primarily gene-regulatory (miRNA). Whether
RNAi retains antiviral function in mammals is still debated; some
evidence (Maillard et al. 2013 *Science* 342:235) suggests yes in
specific cell types.

### Apoptosis (programmed cell death)

Apoptosis is eukaryote-specific in its canonical "caspase-cascade"
form but has **homologous antecedents in prokaryotes** — including
the Abi and CBASS systems from attempt_101 that trigger cellular
destruction on viral infection. The mechanistic continuity:

- **Prokaryotic Abi**: TA toxin activation, membrane disruption, or
  NAD+ depletion on phage detection.
- **Eukaryotic apoptosis**: caspase-9 activation (via cytochrome c
  release from mitochondria) triggers caspase-3-mediated dismantling.
- **Mitochondrial involvement**: cytochrome c release from
  mitochondria is the key regulatory step. This is explained by the
  endosymbiont origin: the mitochondrion retains its ancient
  bacterial-lineage cell-death machinery, now repurposed to trigger
  host cell death.

Reference: Bertin J et al. (1999) apoptosome complex biochemistry;
more recently, Tait & Green (2010) *Nat Rev Mol Cell Biol* 11:621
for apoptotic pathway origins.

## Innate-like recognition in early eukaryotes

Early eukaryotes faced new pathogens (other eukaryotic intracellular
pathogens, viruses adapted to the larger cell) requiring new
recognition systems. Several emerged:

### cGAS-STING pathway

**cGAS** (cyclic GMP-AMP synthase) detects cytoplasmic DNA
(including viral DNA and damaged mitochondrial DNA leaking into the
cytoplasm). Upon DNA binding, cGAS produces cyclic GMP-AMP
(2'3'-cGAMP), which activates **STING** (stimulator of interferon
genes). STING triggers type I interferon production.

This pathway is ~100-500 Ma old in its vertebrate form BUT has
deeper ancestry: as noted in attempt_101, **CBASS in bacteria** is
the prokaryotic homolog (same cyclic nucleotide signaling, ~3 Ga
deep). The eukaryotic cGAS-STING pathway is likely a repurposing of
a bacterial-lineage module.

Reference: Sun L et al. (2013) "Cyclic GMP-AMP synthase is a
cytosolic DNA sensor that activates the type I interferon pathway."
*Science* 339:786-791. PMID 23258413.

### Pattern recognition receptor precursors

Leucine-rich-repeat (LRR)-containing proteins are widespread in
eukaryotes. LRRs bind diverse ligands; different LRR proteins will
later give rise to:
- TLRs (Toll-like receptors, metazoan-specific, attempt_103)
- NLRs (NOD-like receptors, including inflammasome components)
- VLRs (lamprey variable lymphocyte receptors, attempt_104)
- FLS2 and other plant disease-resistance proteins

The common LRR architecture traces to early eukaryotic LRR-containing
proteins. LRRs as a protein fold are actually much older (bacterial
LRR proteins exist), but their use in immunity expands in eukaryotes.

### The nuclear envelope as a defense

A structural point often underappreciated: the nuclear envelope
separates genome from cytoplasm. Foreign DNA that enters the cytoplasm
cannot immediately access the chromatin replication machinery. The
cytoplasm becomes a "DNA-free zone" in the steady state, so
DNA-detection pathways (cGAS) can use cytoplasmic DNA as a foreign-
detection signal.

This is an architectural defense that prokaryotes cannot have, and
cGAS-STING exploits it directly.

## The timing problem

How long did it take for eukaryotic innate defense to consolidate?
The fossil record is unhelpful for soft-tissue cellular details, but
molecular phylogeny suggests:

- Eukaryogenesis: ~2.0 Ga (uncertainty range 1.6-2.1 Ga).
- Autophagy machinery consolidation: likely concurrent with
  eukaryogenesis (needs mitophagy to manage endosymbiont).
- RNAi: present in last eukaryotic common ancestor (LECA), so pre-
  ~1.6 Ga.
- cGAS-STING in current form: later, probably animal-specific
  (~600 Ma).
- cGAS-like antecedent (from CBASS): present at eukaryogenesis.

The rate of innate-system innovation was likely fastest in the first
few hundred million years of eukaryotic history, when new selection
pressures (larger cell, intracellular pathogens) were first
encountered.

## Why this matters for the layered-architecture framework

Three key transitions at eukaryogenesis:

1. **Compartmentalization enables new defense architectures.** Nuclear
   envelope + organelles = new surfaces for recognition; intracellular
   targeting becomes possible.

2. **Repurposing of bacterial-lineage modules.** Autophagy, apoptosis,
   cGAS-like signaling, and potentially others are eukaryotic
   reworkings of prokaryotic defense themes.

3. **Loss of some prokaryotic defenses.** CRISPR-Cas and RM disappear
   because they don't fit the new cellular architecture. Evolution
   does not carry every tool forward — defense systems are reshaped
   or discarded as selection and constraint change.

This sets up attempt_103 (invertebrate metazoans), where cell-cell
communication and true multicellular defense emerge.

## Open questions

1. **What fraction of modern eukaryotic innate immunity derives from
   bacterial-lineage modules vs archaeal-lineage modules vs
   eukaryote-novel?** Current estimate: ~40% bacterial, ~20% archaeal,
   ~40% novel. These percentages are soft.

2. **Did the mitochondrion's bacterial defense systems persist inside
   the organelle?** Modern mitochondria still have a limited
   restriction-modification-like system (nuclease activity at the
   inner membrane); this is sometimes called "mitochondrial
   immunity." Little is known.

3. **Why did eukaryotes lose CRISPR-Cas if it's so effective?** The
   "too expensive in large cells" argument is plausible but not
   proven.

4. **How did xenophagy first specialize from bulk autophagy?** Needed
   recognition receptors (galectins, ubiquitin-binding proteins) that
   identify pathogen surfaces. Timing and order of these components'
   evolution is partly worked out.

## Links to other attempts

- attempt_100 (framework): this populates the "eukaryogenesis ~2 Ga"
  row.
- attempt_101 (prokaryotic): the ancestor defense systems discussed
  here (CBASS → cGAS-STING; Abi → apoptosis).
- attempt_103 (invertebrate metazoan, planned): TLRs, complement, and
  the move from single-cell to multicellular defense.

## Key sources

Primary:
- Spang A et al. 2015 *Nature* 521:173 (Lokiarchaeota)
- Imachi H et al. 2020 *Nature* 577:519 (Asgard archaeon cultivation)
- Martin W, Müller M 1998 *Nature* 392:37 (hydrogen hypothesis)
- Fire A, Mello CC et al. 1998 *Nature* 391:806 (RNAi discovery)
- Sun L et al. 2013 *Science* 339:786 (cGAS is cytosolic DNA sensor)
- Levine B et al. 2011 *Nature* 469:323 (autophagy in immunity)

Historical / Nobel:
- Nobel Prize 2006 (Fire, Mello — RNAi)
- Nobel Prize 2016 (Ohsumi — autophagy)

Reviews:
- Koonin EV, Makarova KS, Aravind L 2001 *Annu Rev Microbiol* on
  origin of eukaryotic informational machinery
- Deretic V, Kroemer G 2022 *Autophagy* 18:283 (autophagy in
  metabolism and quality control)
- Tait SWG, Green DR 2010 *Nat Rev Mol Cell Biol* 11:621 (apoptotic
  pathway biochemistry)

---

## Gap opened

- **Mitochondrial immunity**: mostly unexplored. The organelle
  retains some bacterial character; how much of its antiviral function
  (MAVS signaling, OMM dynamics) derives from ancestral bacterial
  defenses is under-studied.
- **Timing of LRR-fold immune usage**: LRRs are ancient as a fold;
  their deployment in immune sensing is concentrated at specific
  evolutionary nodes. Mapping this requires better phylogenies of
  LRR-containing proteins.

## Status

Complete. attempt_103 (invertebrate metazoan innate: TLRs, complement,
hemocytes) is next.

---

*Filed: 2026-04-15 | biology/evolution/attempts/attempt_102*
*Follows: attempts 100, 101.*
*Parallel-instance convention: 100-199 range; 001-099 is other instance's scope.*
