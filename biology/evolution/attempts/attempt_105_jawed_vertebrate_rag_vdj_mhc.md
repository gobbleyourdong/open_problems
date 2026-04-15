# attempt_105 — Jawed Vertebrate Adaptive Immunity: RAG, V(D)J, MHC

> Fifth attempt in the 100-series. Around 450 million years ago, in
> the common ancestor of all jawed vertebrates, three events
> coalesced to produce the adaptive immune system that modern
> immunology textbooks describe: (1) domestication of a Transib-
> family transposon into the RAG1/RAG2 recombinase; (2) two rounds
> of whole-genome duplication (2R); (3) clonal expansion of
> lymphocytes carrying rearranged receptors. This architecture has
> been conserved — with elaborations — from cartilaginous fish to
> humans. Everything downstream in this series runs on this
> machinery.

---

## The phylogenetic landscape at ~450 Ma

The gnathostome (jawed vertebrate) ancestor appeared ~450-420 Ma.
Modern jawed vertebrates split into:

- **Chondrichthyes** (cartilaginous fish: sharks, rays, chimaeras) —
  earliest-diverging living gnathostomes. Have the full adaptive
  immunity package already.
- **Osteichthyes** (bony fish): further split into Actinopterygii
  (ray-finned fish) and Sarcopterygii (lobe-finned fish +
  tetrapods).
- **Tetrapods**: amphibians, reptiles (including birds), mammals.

All jawed vertebrates share:
- RAG1/RAG2 genes for V(D)J recombination
- Immunoglobulin-superfamily antigen receptors (BCR, TCR)
- MHC class I and class II
- B and T lymphocyte lineages
- Thymus (pharyngeal pouch-derived)
- Bone marrow / hematopoietic tissue

These are the **five core vertebrate adaptive immunity components.**
Their joint presence defines the system.

## The RAG transposon story

### Origin

As noted in attempt_100 (audit-verified) and attempt_104, RAG1 and
RAG2 were domesticated from a Transib-family transposon:

**Liu C, Yang Y, Schatz DG, Xu Y, Gao Y (2019).** "Transposon
molecular domestication and the evolution of the RAG recombinase."
*Nature* 569:79-84. PMID 30971819. Provides structural evidence for
the RAG1/RAG2 → Transib ancestry and identifies the jawed-vertebrate-
specific adaptations that suppressed the transposase activity.

Earlier foundational work:
- **Agrawal A, Eastman QM, Schatz DG (1998).** "Transposition
  mediated by RAG1 and RAG2 and its implications for the evolution
  of the immune system." *Nature* 394:744-751. PMID 9723617. First
  experimental demonstration that RAG proteins can catalyze
  transposition in vitro — the "smoking gun" for their transposon
  origin.
- **Kapitonov VV, Jurka J (2005).** "RAG1 core and V(D)J recombination
  signal sequences were derived from Transib transposons." *PLoS
  Biology* 3:e181. PMID 15898832. Identified Transib as the specific
  source via sequence alignment.

### The domestication event

In the common ancestor of jawed vertebrates, a Transib-like transposon
(already carrying a RAG1-like recombinase) integrated into a host
locus that contained an Ig-superfamily-fold gene. Subsequent evolution:

1. The transposon's terminal inverted repeats (TIRs) became the
   RSS (recombination signal sequences) flanking V, D, and J segments.
2. The RAG1-like ORF was "captured" by the host genome.
3. A RAG2 component was acquired (possibly from another mobile
   element, possibly host-derived) and joined RAG1.
4. Key mutations in RAG1 (arginine 848) and RAG2 (acidic hinge)
   suppressed the transposon's "cut and paste" activity, locking
   the enzyme into a "cut only" role for V(D)J recombination.

Result: a recombinase that breaks double-stranded DNA at specific
signals but does not re-insert the excised fragment elsewhere. The
excised fragment is discarded; the remaining gene segments are
religated by the host's NHEJ (non-homologous end joining) machinery.

### Why Transib rather than another transposon

The Transib family has specific features suited to "domestication":
- Target site duplication pattern compatible with RSS architecture.
- DDE catalytic triad in the transposase — also used by the later
  RAG1.
- Short, simple transposons that don't carry extensive protein-
  coding overhead.

Other transposon families could have provided similar raw material;
the historical accident is that Transib was the one that happened
to land in the right genomic context at the right time.

## V(D)J recombination: the mechanism

Discovered by Susumu Tonegawa (Nobel Prize 1987):

**Tonegawa S (1983).** "Somatic generation of antibody diversity."
*Nature* 302:575-581. PMID 6300689. Review of the V(D)J principle
that Tonegawa's lab established through the late 1970s and early
1980s using cDNA / genomic DNA comparisons in myeloma cells.

### Gene segment architecture

A heavy-chain immunoglobulin (IgH) locus in a mammal has:
- ~40 V (variable) gene segments
- ~23 D (diversity) gene segments (heavy chain only)
- ~6 J (joining) gene segments
- Constant region (µ, δ, γ, ε, α isotypes for antibody class)

At the DNA level in a B cell precursor, one V, one D, and one J
segment are joined through RAG-mediated double-strand breaks +
NHEJ religation. The resulting VDJ exon encodes the antibody's
heavy-chain variable region.

Light chains (κ, λ) undergo VJ recombination (no D segment).

TCR chains (α, β, γ, δ) undergo similar V(D)J recombination at
T-cell receptor loci.

### Diversity sources

- **Combinatorial diversity**: V × D × J × (H vs L chain) gives
  ~10⁶ possible combinations for IgH. Multiply by the independent
  light-chain choice for ~10⁸ naive BCR diversity.
- **Junctional diversity**: RAG-mediated cuts produce variable end
  processing. TdT (terminal deoxynucleotidyl transferase) adds
  random nucleotides ("N regions") at joining points. Contributes
  another ~10³.
- **Somatic hypermutation** (SHM): in activated B cells, AID
  (activation-induced cytidine deaminase) introduces point mutations
  in V region exons during germinal center reactions, affinity-
  maturing the antibody response.

Combined repertoire capacity: ~10¹¹ possible BCRs, with ~10¹²-10¹³
theoretical maximum including SHM. Observed diversity in a human:
~10⁹ distinct BCR sequences at any one time.

## The MHC: antigen presentation

### Class I and class II

Two families of MHC molecules evolved in the common ancestor of
jawed vertebrates:

- **MHC class I**: expressed on all nucleated cells. Presents
  peptides from intracellular proteins (including viral proteins
  synthesized inside the cell) to CD8+ cytotoxic T cells.
- **MHC class II**: expressed primarily on professional antigen-
  presenting cells (dendritic cells, macrophages, B cells). Presents
  peptides from extracellular / phagocytosed proteins to CD4+ helper
  T cells.

The distinct roles reflect distinct peptide-loading pathways:
- Class I: proteasomal degradation of cytosolic proteins → TAP
  transporter → ER loading onto class I.
- Class II: endolysosomal degradation of internalized proteins →
  loading onto class II in a late endosome / MIIC compartment.

### Evolutionary origin

Jawless vertebrates lack MHC entirely. Jawed vertebrates have both
classes. The molecular origin involves Ig-superfamily domains that
existed pre-split, but the specific peptide-binding architecture is
gnathostome-specific.

Reference: **Kaufman J (2018).** "Unfinished business: evolution of
the MHC and the adaptive immune system of jawed vertebrates." *Annu
Rev Immunol* 36:383-409. PMID 29677478. Excellent modern review
tracing MHC class I and II origin, including the "minimal essential
MHC" model.

Sharks are the earliest-diverging living jawed vertebrates with
full MHC class I and II loci. This places the MHC invention at or
before the cartilaginous-fish split (~420 Ma).

### The 2R hypothesis

Jawed vertebrates show evidence of two rounds of whole-genome
duplication (2R) early in their lineage:

**Ohno S (1970).** *Evolution by gene duplication.* Springer-Verlag.
Original hypothesis that vertebrate genomes underwent 2-4 rounds of
polyploidization.

Modern view: 2 rounds in jawed vertebrates, with a third (3R) in
teleost fishes. Evidence: many gene families have four paralogs in
gnathostomes that align with single-copy genes in invertebrates.

Implication for immunity: the RAG transposon's initial landing
event was followed by 2R, giving the ancestral gnathostome FOUR
copies of each initial immune-relevant gene. Subsequent sub-
functionalization produced class I vs class II MHC, the multiple
lymphocyte receptor loci, etc.

Reference: **Flajnik MF, Kasahara M (2010).** "Origin and evolution
of the adaptive immune system: genetic events and selective
pressures." *Nat Rev Genet* 11:47-59. PMID 19997068. [Verified in
attempt_100 audit.]

## B and T lymphocyte lineages

### B cells

- Develop in bone marrow (or bone-marrow-equivalent hematopoietic
  tissue in fish).
- Express BCR (surface Ig).
- Upon activation, differentiate into plasma cells that secrete
  antibodies.
- Some persist as memory B cells.

### T cells

- Develop in thymus (pharyngeal pouch-derived).
- Express TCR (αβ-TCR or γδ-TCR).
- Undergo positive and negative selection in thymus.
- αβ-T cells split into CD4+ helper and CD8+ cytotoxic lineages
  based on MHC class II vs class I recognition during thymic
  selection.
- γδ-T cells have varied roles including tissue surveillance and
  gut immunity.

### Thymic selection

Key innovation: the thymus performs **central tolerance**. T cells
that bind self-peptide/self-MHC too strongly are deleted (negative
selection). T cells that cannot bind self-MHC at all are also
deleted (positive selection). Only cells with moderate affinity
for self-MHC (sufficient for surveillance but not auto-reactive)
survive.

This is the solution to the autoimmune-risk problem inherent in
randomly-generated receptors: most randomly-generated TCRs WILL
recognize self. Eliminating those in the thymus protects against
autoimmunity.

Reference: **von Boehmer H (2005).** "Mechanisms of suppression by
suppressor T cells." *Nat Immunol* 6:338-344. And: Kyewski B,
Klein L (2006) *Annu Rev Immunol* 24:571 on central tolerance.

## Cartilaginous fish: the earliest living model

Shark immunology is a major window on ancestral gnathostome adaptive
immunity. Findings:

- Sharks have class I and class II MHC with the same basic
  architecture as mammalian MHC.
- Shark BCR has three H-chain isotypes: IgM (similar to mammalian
  IgM), IgW (similar to mammalian IgD), IgNAR (a single-chain
  "nanobody"-like shark-specific innovation).
- Sharks have TCR αβ and γδ with V(D)J recombination.
- Sharks have somatic hypermutation AND class-switching precursors.

The IgNAR (Immunoglobulin New Antigen Receptor) is a shark
innovation: a heavy-chain-only antibody without light chain,
analogous to camelid VHH "nanobodies" that evolved independently
in camels/llamas.

Reference: **Dooley H, Flajnik MF (2006).** "Antibody repertoire
development in cartilaginous fish." *Dev Comp Immunol* 30:43-56.
PMID 16146649.

## Why this architecture was evolutionarily successful

1. **Essentially unlimited repertoire** (~10⁹-10¹¹ distinct
   receptors per individual): outruns any pathogen's ability to
   evolve antigenic variation fast enough.

2. **Memory**: clonal expansion of antigen-responding lymphocytes
   provides faster, stronger response to repeat infections.

3. **MHC-based sampling**: every cell broadcasts its intracellular
   state via class I peptide presentation. Viral infection is
   visible. Tumor neoantigens are potentially visible.

4. **Self-tolerance via thymic selection**: autoimmunity is
   controlled (imperfectly, as seen in modern disease).

5. **Compatibility with innate immunity**: TLR signals gate B and T
   cell activation; innate + adaptive is a layered system where
   the young layer is controlled by the old.

## Costs of the architecture

1. **Risk of autoimmune disease**: ~5% of humans develop clinically
   significant autoimmunity.

2. **Risk of lymphoproliferative disease**: B and T cell cancers
   (lymphomas, leukemias) result from defects in clonal control.

3. **Immune privilege constraints**: eyes, testes, CNS must restrict
   immunity to avoid damage; pathogens that reach those sites
   (herpesviruses in CNS; CVB in pancreatic islets; see 001-series)
   persist there.

4. **Allograft incompatibility**: MHC polymorphism means transplants
   between unrelated individuals are rejected. Required discovery
   of immunosuppression for transplant medicine.

5. **Metabolic cost**: thymus, bone marrow, lymphoid tissue mass
   represent substantial ongoing investment.

## Key evolutionary question: why RAG not DSCAM?

Why did jawed vertebrates go with RAG-V(D)J instead of something
like DSCAM-style alternative splicing (attempt_103)?

Candidate answers:
- **Clonal allelic exclusion**: V(D)J produces exactly one rearranged
  allele per cell. Splicing-based diversity would have all cells
  expressing all variants. The clonal model requires a
  "commitment" step that V(D)J provides naturally.
- **Gene conversion-free diversity**: V(D)J doesn't rely on the
  template strand being present; it's a clean recombination. DSCAM
  splicing requires specific splice factor regulation that gets
  complex with >10^4 variants.
- **Transposon availability**: the Transib transposon happened to
  be available. If evolution had used a different scaffold, who
  knows.

No clean answer — partly historical accident.

## Open questions

1. **When exactly did MHC evolve?** Placoderms (jawed fish that went
   extinct at end-Devonian) might have had early-stage MHC. Genomic
   study would require ancient DNA that is likely unavailable.

2. **What happened to unsuccessful gnathostome adaptive-immunity
   variants?** Were there lineages that tried V(D)J without MHC,
   or without 2R, and went extinct? Fossil record is silent on
   immune genes.

3. **Why did RAG transposition activity remain suppressed but not
   abolished?** Liu 2019 showed suppression is >1000× but not zero.
   Occasional RAG-mediated re-activation of cryptic recombination
   signal sequences drives some chromosomal translocations in
   lymphomas. A relic of the transposon past.

4. **How do bony fish (teleost) elaborations of the basic system
   (e.g., fish IgT mucosal antibody, expanded MHC class I loci in
   zebrafish) compare across taxa?** Active area.

## Links to other attempts

- attempt_100 (framework): populates "jawed vertebrates (~450 Ma)"
  row.
- attempt_104 (jawless VLR): the parallel solution in sister lineage.
- attempt_106 (mammalian, next): class switching, germinal centers,
  placental tolerance elaborations.
- attempt_107 (persistent-virus coevolution): how MHC polymorphism
  was shaped by viral selection. Bridges to 001-series.

## Key sources

Primary / foundational:
- Ohno S 1970 *Evolution by Gene Duplication* (Springer) — 2R
  hypothesis.
- Tonegawa S 1983 *Nature* 302:575 (V(D)J; Nobel 1987). PMID 6300689.
- Agrawal A et al. 1998 *Nature* 394:744 (RAG-mediated transposition
  in vitro). PMID 9723617.
- Kapitonov VV, Jurka J 2005 *PLoS Biol* 3:e181 (RAG from Transib).
  PMID 15898832.
- Dooley H, Flajnik MF 2006 *Dev Comp Immunol* 30:43 (shark antibody
  development). PMID 16146649.
- Flajnik MF, Kasahara M 2010 *Nat Rev Genet* 11:47 — VERIFIED.
- Huang S et al. 2016 on amphioxus active RAG transposon.
- Liu C et al. 2019 *Nature* 569:79 (RAG domestication structure).
  PMID 30971819.

Reviews:
- Kaufman J 2018 *Annu Rev Immunol* 36:383 (MHC evolution).
  PMID 29677478.
- Cooper MD, Alder MN 2006 *Cell* 124:815 (adaptive immunity
  evolution).

Historical:
- Nobel Prize 1987 (Tonegawa — V(D)J recombination).
- Nobel Prize 1996 (Doherty + Zinkernagel — MHC-restricted antigen
  recognition).

---

## Gap opened

- **Pre-RAG state reconstruction**: a common-ancestor model of
  gnathostome lymphocytes BEFORE the RAG transposon domesticated
  would clarify what "raw material" was there. Amphioxus (the
  sister to vertebrates + cephalochordates) still has an active
  RAG-like transposon, giving us a window (Huang 2016).

- **Why MHC polymorphism is so extreme**: this is covered more
  deeply in attempt_107; here, mention that the peptide-binding
  groove is under very strong balancing selection, yielding >25,000
  HLA alleles in modern humans.

## Status

Complete. attempt_106 (mammalian refinements: class switching,
germinal centers, maternal transfer, placental tolerance) is next.

---

*Filed: 2026-04-15 | biology/evolution/attempts/attempt_105*
*Follows: attempts 100, 101, 102, 103, 104.*
*Parallel-instance convention: 100-199 range; 001-099 is other instance's scope.*
