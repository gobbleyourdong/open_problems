# attempt_103 — Invertebrate Metazoan Innate Immunity: The Toll/NF-κB Axis, Complement, and Diversified Recognition

> Third attempt in the 100-series. Traces innate immunity from
> cnidarians (~700 Ma) through sponges, insects, echinoderms, and
> other invertebrates. The central finding: the Toll/NF-κB signaling
> axis is pan-metazoan; complement predates vertebrates; invertebrates
> achieve astonishing receptor diversity without RAG-based
> recombination. By the late Cambrian (~500 Ma), "innate" immunity
> was already elaborate.

---

## The multicellular transition and new selection pressures

Around 700-800 Ma, multicellularity arose independently several
times. Metazoans (animals) date from one such event; the last common
ancestor of all animals, the "urmetazoan," existed ~700-600 Ma.

New selection pressures at multicellularity:

1. **Microbial symbionts and pathogens get permanent niches.** A
   multicellular body has internal surfaces (gut, epithelium) that
   microbes can colonize persistently. This is simultaneously a
   benefit (mutualism) and a hazard (dysbiosis and invasion).

2. **Cells must distinguish self from fellow-cell.** Allorecognition
   becomes crucial. A multicellular organism must not attack itself
   and must not be invaded by genetically distinct conspecific cells.

3. **Cells can specialize for defense.** Phagocytes, coelomocytes,
   hemocytes — specialized immune cells emerge.

4. **Humoral defense becomes possible.** Soluble antimicrobial
   molecules (peptides, complement-like proteins) can be secreted
   into body fluids (hemolymph, coelom).

## Cnidarians: the oldest animal immunity

Cnidarians (jellyfish, corals, hydras, sea anemones) are the
deepest-branching animal clade in many analyses (alongside sponges).
They already possess:

- **NF-κB homologs**: *Nematostella vectensis* (starlet sea anemone)
  has NF-κB, IκB, and a functional signaling pathway. Experiments in
  the Gilmore lab at Boston University have characterized these.
  Reference: Wolenski FS et al. (2011) "Characterization of the core
  elements of the NF-κB signaling pathway of the sea anemone
  Nematostella vectensis." *Mol Cell Biol* 31:1076-1087. PMID 21199918.

- **Complement C3 homologs**: present pre-cnidarian/bilaterian split.
  The thioester-containing protein (TEP) family differentiated into
  C3 and α₂-macroglobulin subfamilies before Cnidaria + Bilateria
  diverged (>600 Ma). See attempt_100 audit + Al-Sharif et al. 1998
  on sea urchin C3 and multiple reviews on cnidarian complement.

- **Toll/TLR-like receptors**: early sequence variants.
  *N. vectensis* genome encodes Toll-like proteins.

- **Antimicrobial peptides (AMPs)**: *Hydra* produces hydramacin and
  arminin peptides that shape its microbiome. Reference: Bosch TC
  (2013) *Annu Rev Microbiol* 67:499 on *Hydra*-microbiome immunity.

The cnidarian set establishes that the core innate architecture
(pattern recognition receptors + NF-κB signaling + effector AMPs +
complement) was already present at the base of metazoans.

## Sponges: even earlier?

Sponges (Porifera) are sister to or basal to other animals in
different analyses. *Amphimedon queenslandica* genome (Srivastava
2010 *Nature* 466:720) encodes Toll/TLR-like genes, AMPs, and
components of NF-κB signaling. The picture is consistent with the
cnidarian view: innate immunity is as old as Metazoa.

## The Toll pathway: dorsoventral patterning repurposed for defense

The *Drosophila* Toll gene was named in 1985 in Nüsslein-Volhard's
lab for its role in dorsoventral axis patterning of fly embryos.
Embryos lacking functional Toll had "toll" (German for "crazy/weird")
phenotype. The gene encoded a transmembrane receptor with a leucine-
rich-repeat (LRR) ectodomain.

**Anderson KV, Jürgens G, Nüsslein-Volhard C (1985).** "Establishment
of dorsal-ventral polarity in the Drosophila embryo: genetic studies
on the role of the Toll gene product." *Cell* 42:779-789. PMID 3931918.

Eleven years later, Hoffmann's lab demonstrated Toll's immune role:

**Lemaitre B, Nicolas E, Michaut L, Reichhart JM, Hoffmann JA (1996).**
"The dorsoventral regulatory gene cassette spätzle/Toll/cactus
controls the potent antifungal response in Drosophila adults."
*Cell* 86:973-983. PMID 8808632.

Flies lacking functional Toll could not mount antifungal defense;
they died of *Aspergillus* infection that wild-type flies survived.
This discovery won Hoffmann the 2011 Nobel (see attempt_100 audit).

Beutler's discovery of mammalian TLR4 as the LPS receptor followed:

**Poltorak A, He X, Smirnova I et al. (1998).** "Defective LPS
signaling in C3H/HeJ and C57BL/10ScCr mice: mutations in Tlr4 gene."
*Science* 282:2085-2088. PMID 9851930.

Ten mammalian TLRs exist (TLR1-10 in humans; TLR11-13 in mice only).
Each recognizes a characteristic microbial molecular pattern:
- TLR4: lipopolysaccharide (LPS, Gram-negative bacteria)
- TLR3: double-stranded RNA (viruses)
- TLR5: flagellin (bacteria)
- TLR7/8: single-stranded RNA (viruses)
- TLR9: unmethylated CpG DNA (bacteria, viruses)
- TLR2/1, TLR2/6: lipoproteins (bacteria)

The Toll pathway in flies activates NF-κB-family transcription
factor Dorsal (developmental) or Dif (immune); mammalian TLR
signaling activates NF-κB directly. Conservation of the pathway
across ~600 Ma.

## The IMD pathway: Drosophila's second immune axis

Flies have a distinct pathway for Gram-negative bacterial response:
**IMD (immune deficiency)**, discovered via mutant screens in the
1990s. IMD leads to activation of the NF-κB-family factor Relish.

IMD pathway components include a caspase-8-like caspase (Dredd) and
are mammalian TNF-pathway homologs. The Toll vs IMD distinction in
flies parallels the "TLR-dependent vs TNFR-dependent" branching in
mammalian innate signaling.

Reference: Lemaitre B, Hoffmann J (2007) "The host defense of
*Drosophila melanogaster*." *Annu Rev Immunol* 25:697-743. PMID
17201680. Canonical review of fly innate immunity.

## Antimicrobial peptides: the effector arm

*Drosophila* produces 7+ distinct families of AMPs:
- **Drosomycin** (antifungal, Toll-induced)
- **Diptericin** (anti-Gram-negative, IMD-induced)
- **Attacin** (anti-Gram-negative)
- **Cecropin** (broad-spectrum)
- **Defensin** (anti-Gram-positive)
- **Drosocin** (anti-Gram-negative)
- **Metchnikowin** (anti-Gram-positive + antifungal)

AMPs are ancient in eukaryotes. Defensin-family peptides are found in
plants, insects, and mammals — convergent or deeply homologous? The
current view: the cysteine-stabilized scaffold of defensins
(αβ-defensins, θ-defensins) is so constrained that analogous
structures may have been invented multiple times. Several defensin
subfamilies trace to a common ancestor pre-dating plant-animal split
(~1.5 Ga).

## Complement in invertebrates

- **Sea urchin C3** (Al-Sharif 1998, PMID 9510203): the first complete
  invertebrate complement protein. Functional thioester; acts as
  opsonin.
- **Other echinoderms**: complement present in sea stars, sea
  cucumbers.
- **Ascidians** (tunicates, sister group to vertebrates): expanded
  complement-like factor B/C2.
- **Insects**: TEP (thioester-containing proteins) are complement-
  related and function in phagocytosis of pathogens. TEP1 in
  *Anopheles gambiae* mosquito coats malaria parasites (*Plasmodium*)
  and recruits them for destruction.

Reference: Dodds AW, Matsushita M (2007) "The phylogeny of the
complement system and the origins of the classical pathway."
*Immunobiology* 212:233-243. PMID 17544808.

## Recognition without recombination: invertebrate diversity strategies

Invertebrates lack RAG-based V(D)J recombination but achieve
remarkable receptor diversity by other means:

### DSCAM splicing in insects

*Drosophila* DSCAM (Down Syndrome Cell Adhesion Molecule) can
generate **up to ~38,000 theoretical isoforms** by alternative splicing
of its three variable exons (Schmucker et al. 2000 *Cell* 101:671,
originally characterizing DSCAM's role in neuronal wiring). The Watson
2005 study showed ~18,000 isoforms actually expressed in immune cells
and secreted DSCAM in hemolymph.

**Watson FL, Püttmann-Holgado R, Thomas F et al. (2005).**
"Extensive diversity of Ig-superfamily proteins in the immune system
of insects." *Science* 309:1874-1878. PMID 16109846.

Each hemocyte expresses a different random combination of the splice
variants, producing a clonal-like receptor landscape without
recombination. DSCAM binds bacteria and contributes to phagocytic
specificity. In sheer numerical diversity, DSCAM exceeds any single
vertebrate immune receptor locus — a genuine alternative solution to
the "diversity problem."

### FREP diversification in snails

Schistosome-resistant snails (*Biomphalaria glabrata*) have fibrinogen-
related proteins (FREPs) with diversity generated by somatic
mutation and gene conversion. Zhang et al. 2004 *Science* 305:251.

### 185/333 genes in sea urchins

Sea urchins have an immune gene family called **185/333** (for
ESTs 185 and 333) that expands to ~50-100 members per individual.
Expressed in coelomocytes; massive sequence diversity.

Reference: Hibino T, Loza-Coll M, Messier C et al. (2006) "The
immune gene repertoire encoded in the purple sea urchin genome."
*Dev Biol* 300:349-365. PMID 17027739. Paralleled by publication of
the sea urchin genome in *Science* 314:941-952 (2006).

### Summary

Three different invertebrate groups (insects DSCAM, snails FREPs,
echinoderms 185/333) independently evolved diversification
mechanisms that produce high-diversity immune repertoires. None uses
RAG/V(D)J. The point: diverse recognition was "wanted" evolutionarily
before V(D)J was invented.

## Hemocytes and cellular immunity

Invertebrate immune cells (named variously):
- **Insect hemocytes**: plasmatocytes (phagocytic), crystal cells
  (melanization), lamellocytes (encapsulation of large parasites).
- **Echinoderm coelomocytes**: diverse phagocytic and effector cells.
- **Mollusc hemocytes**: phagocytes, encapsulation cells.

Functions:
- **Phagocytosis** of bacteria and debris.
- **Encapsulation** of parasites too large to phagocytose (e.g.,
  parasitoid wasp eggs in flies).
- **Melanization** via the prophenoloxidase (proPO) cascade — a
  proteolytic cascade analogous to complement that produces melanin
  and reactive oxygen/nitrogen species at infection sites.

Reference: Theopold U et al. (2004) "Coagulation in arthropods:
defence, wound closure and healing." *Trends Immunol* 25:289-294.

## Natural Killer (NK) cell precursors

NK-like cells are found in invertebrates (echinoderms, protochordates)
but whether they are strictly homologous to vertebrate NK is
uncertain. Cytotoxic cells that kill without prior sensitization
are a common invertebrate theme.

## The Janeway paradigm (1989)

Charles Janeway Jr. proposed in 1989 that the immune system recognizes
"pathogen-associated molecular patterns" (PAMPs) via "pattern
recognition receptors" (PRRs), and that adaptive immunity requires
prior activation by innate PRR signals. This framing unified the
invertebrate and early-vertebrate innate immunity view with the
mammalian adaptive view.

**Janeway CA Jr. (1989).** "Approaching the asymptote? Evolution and
revolution in immunology." *Cold Spring Harbor Symp Quant Biol* 54
Pt 1:1-13. PMID 2700931.

The PRR-PAMP paradigm predates the molecular discovery of TLRs by
7 years (Lemaitre 1996) and Beutler's mammalian TLR4 by 9 years
(Poltorak 1998). Janeway's conceptual framework was ahead of its
experimental validation.

## Why this matters for the layered-architecture framework

Four key transitions at invertebrate metazoans:

1. **The Toll/NF-κB axis is pan-metazoan.** Conservation across
   ~600 Ma means this module is evolutionarily stable.

2. **Complement is pre-vertebrate.** Its repurposing for antibody-
   dependent classical pathway in jawed vertebrates is layered ON TOP
   of the ancient alternative pathway.

3. **Receptor diversity does NOT require RAG.** DSCAM, 185/333, FREPs
   all produce diverse repertoires without V(D)J. The "adaptive
   immunity needs RAG" statement is FALSE in general — it requires
   RAG for the VERTEBRATE solution, not for diversity per se.

4. **Cell-based + humoral defense is universal.** The split between
   "phagocytes" and "soluble mediators" predates vertebrates; both
   lineages are present in invertebrates.

## Open questions

1. **Do invertebrate diversified receptors (DSCAM, 185/333) produce
   immunological memory?** Evidence is mixed. Some insects show
   "immune priming" — a second exposure is handled better — but the
   mechanism is debated.

2. **How does the insect microbiome interact with Toll/IMD specificity?**
   Microbiome composition shapes immune tone; this feedback is under
   active investigation.

3. **Why did vertebrates go with RAG when DSCAM-like splicing could
   have sufficed?** A genuinely open question. Possible answers:
   clonal selection (each lymphocyte expresses one receptor) is
   easier with recombination than splicing; the ~10¹⁰ repertoire of
   V(D)J exceeds DSCAM's ~38,000.

4. **Plant disease-resistance: parallel or convergent?** Plant NLR
   proteins (NB-LRR receptors; e.g., FLS2, BAK1) recognize PAMPs
   similarly to TLRs but via LRR ectodomains that diverged from
   animal LRR-PRRs independently. Deep ancestry of the LRR fold (from
   pre-eukaryotic times) makes the line between homology and
   convergence blurry.

## Links to other attempts

- attempt_100 (framework): populates "multicellular + early metazoan"
  rows.
- attempt_101 (prokaryotic): bacterial Toll-like mechanisms are
  distant homologs.
- attempt_102 (eukaryogenesis): LRR proteins pre-metazoan; Toll is
  an elaboration.
- attempt_104 (VLRs, planned): jawless vertebrates will pick up LRR
  again for adaptive immunity.
- attempt_105 (jawed vertebrates, planned): TLRs continue; complement
  gets a classical pathway via IgM.

## Key sources

Primary:
- Anderson KV, Jürgens G, Nüsslein-Volhard C 1985 *Cell* 42:779 (Toll in dorsoventral)
- Janeway CA Jr 1989 *CSHSQB* 54 Pt 1:1 (PRR-PAMP paradigm)
- Lemaitre B, Nicolas E, Michaut L, Reichhart JM, Hoffmann JA 1996 *Cell* 86:973 (Toll antifungal)
- Al-Sharif WZ et al. 1998 *J Immunol* 160:2983 (sea urchin SpC3)
- Poltorak A et al. 1998 *Science* 282:2085 (mouse TLR4 = LPS receptor)
- Watson FL et al. 2005 *Science* 309:1874 (DSCAM diversity)
- Hibino T et al. 2006 *Dev Biol* 300:349 (sea urchin immune gene repertoire)
- Srivastava M et al. 2010 *Nature* 466:720 (*Amphimedon* genome)
- Wolenski FS et al. 2011 *Mol Cell Biol* 31:1076 (*Nematostella* NF-κB)

Reviews:
- Lemaitre B, Hoffmann J 2007 *Annu Rev Immunol* 25:697 (Drosophila host defense)
- Dodds AW, Matsushita M 2007 *Immunobiology* 212:233 (complement phylogeny)
- Bosch TC 2013 *Annu Rev Microbiol* 67:499 (Hydra-microbiome immunity)

---

## Gap opened

- **Parallels between plant and animal innate immunity** via LRR PRRs
  are deep but not cleanly homologous; requires further phylogenetic
  work on the LRR-fold deployment in immune contexts.
- **Invertebrate "memory" beyond classical adaptive immunity** —
  trained immunity, epigenetic immune memory in hemocytes, priming in
  insects: substantial literature but no unified framework yet.

## Status

Complete. attempt_104 (VLR convergent adaptive in jawless vertebrates)
is next — the moment a second, independent adaptive system evolved.

---

*Filed: 2026-04-15 | biology/evolution/attempts/attempt_103*
*Follows: attempts 100, 101, 102.*
*Parallel-instance convention: 100-199 range; 001-099 is other instance's scope.*
