# attempt_100 — Immune System Evolution: Timeline and Cross-Cutting Framework

> Opening attempt in the 100-series. Parallel-instance work from the
> 001-099 series on persistent-virus evolution. This track asks: how
> did the human immune system come to have the architecture it does?
> What earlier problems did each layer solve, and what can persistent
> viruses tell us about its remaining limits?

---

## The claim

The vertebrate immune system is a **layered architecture built over
3.5 billion years**. Each layer was added to solve a problem the
previous layers could not handle at a new scale of biological
organization:

| Time | Transition | New problem | New defense |
|------|-----------|-------------|-------------|
| ~3.5 Ga | Prokaryotic life | Bacteriophage predation | Restriction-modification, CRISPR-Cas, abortive infection, toxin-antitoxin |
| ~2.0 Ga | Eukaryogenesis | Intracellular survival; mitochondrial integration | Autophagy, RNA interference, inflammasome precursors |
| ~1.0 Ga | Multicellularity | Cell-cell recognition; kin discrimination | Allorecognition loci, apoptosis, phagocytic amoebocytes |
| ~600 Ma | Early metazoans | Microbial colonization of large body plans | Toll-like receptors, complement, NK-like cytotoxicity |
| ~500 Ma | Jawless vertebrates | Pathogen escape via antigenic variation | Variable Lymphocyte Receptors (LRR-based, convergent adaptive) |
| ~450 Ma | Jawed vertebrates | Arms race with rapidly-evolving pathogens | RAG-based V(D)J recombination, MHC, B/T cells |
| ~200 Ma | Mammals | Placental viviparity + extended infancy | Class switching, germinal centers, maternal IgG transfer |
| ~30-100 Ma | Primates and humans | Persistent virus coevolution | HLA polymorphism, KIR-HLA coadaptation, TRIM5/APOBEC |

Each layer is still operational in the modern human: innate (layers
1–4) runs in minutes, adaptive (layers 5–6) in days, tissue-specific
adaptations (layer 7–8) over weeks. When disease appears, it is most
often a failure at the boundary between layers — too much inflammation
from the innate side, or too little specificity from the adaptive side.

## Why this framing matters

Three concrete uses:

1. **Understanding persistent viruses.** The parallel 001-series
   attempts argue that persistent viruses (EBV, CVB, HCMV, HPV, HHV-6)
   persist by exploiting layer boundaries. EBV sits in memory B cells
   — the very cells whose normal function is persistence of adaptive
   memory. HCMV sits in myeloid precursors that don't express MHC-I
   strongly. HPV sits in basal keratinocytes that rarely encounter
   immune surveillance. Persistence is not a "failure" of the immune
   system; it is a successful exploitation of a niche that evolution
   produced for other reasons.

2. **Understanding autoimmunity.** Many autoimmune disorders
   (rheumatoid arthritis, T1DM, MS, lupus) can be read as
   layer-mismatch disorders: adaptive immunity targeting self-antigens
   that innate immunity should not have presented. The evolutionary
   layering clarifies WHICH parts of the system are mismatch-prone:
   notably the HLA-adaptive interface, which is under continual
   positive selection by persistent viruses.

3. **Predicting where new therapies can work.** A therapy that targets
   a layer N process (e.g., TNF blockade at the innate layer) has
   different expected consequences than one at layer N+1 (e.g., CD20
   B-cell depletion at the adaptive layer). Understanding the timeline
   helps predict off-target effects from the evolutionary age of the
   targeted pathway.

## Key architectural observations across the transitions

### Conservation is striking

Several pathways span the entire tree of life from prokaryotes to
humans:

- **NF-κB-like signaling**: analogous transcription-factor-inhibitor
  pairs appear in cnidarians (NF-κB/IκB), insects (Dorsal/Cactus), and
  vertebrates (NF-κB/IκB). The module is ~600 Ma old.
- **Toll pathway**: originally a dorsoventral patterning gene in flies
  (Toll was named for fly development, not immunity); Hoffmann 1996
  discovered its antifungal role in *Drosophila*, winning the 2011
  Nobel Prize. Mammalian Toll-like receptors are orthologs.
- **Complement**: the C3 thioester bond is present in sea-urchin
  complement-like molecules; the system predates vertebrates.
- **RAG recombinase**: derived from a transposable element (Transib
  family). The RAG1/RAG2 genes are a domesticated transposon,
  integrated into the jawed-vertebrate genome ~450 Ma.

### Convergent adaptive immunity happened twice

Around 500 Ma, TWO independent adaptive immune systems evolved in
vertebrates:

1. **Jawless vertebrates (lampreys, hagfish)**: VLR (Variable Lymphocyte
   Receptor) system, using leucine-rich-repeat (LRR) diversification.
   Discovered by Pancer & Cooper 2004-2005.
2. **Jawed vertebrates (sharks onward)**: V(D)J recombination using
   immunoglobulin-superfamily domains, via the RAG transposon.

Both systems produce clonal lymphocytes with unique receptors;
both select for self-tolerance; both generate memory. The molecular
machinery is completely different. This is one of biology's cleanest
examples of convergent evolution at the system level.

**Why evolution did it twice in parallel**: the selection pressure
(pathogen antigenic variation) was strong enough around the jawed/
jawless split (~500 Ma) to drive two independent solutions.

### Most of "immunity" is tolerance

A common modern framing: the central problem for the immune system is
not recognition but tolerance. Peripheral tolerance mechanisms
(Treg cells, anergy, PD-1/PD-L1 checkpoints) are extensive in
mammals and younger in evolutionary terms than the effector machinery
they restrain. The pattern suggests: recognition was easier to evolve;
restraint was harder.

This has clinical implications: checkpoint inhibitor cancer
therapies (anti-PD-1, anti-CTLA-4) work by removing evolved
restraint, releasing adaptive immunity against tumor antigens.
The fact that this works as often as it does suggests the
adaptive system is chronically held back from operating at maximum
aggression — a feature, not a bug, because uncontrolled adaptive
immunity would destroy the host.

## Predictions this framework makes

If the layered-architecture view is correct, we should see:

1. **Immune pathways deeper in the tree of life should be more
   conserved across species than shallower ones.** CRISPR-Cas is
   prokaryote-only; Toll-signaling is pan-metazoan; V(D)J is only
   jawed vertebrate. Prediction: knockouts of deep pathways should
   be universally lethal; knockouts of shallow ones more variable.
   Observed: TLR knockouts in mice are viable with specific
   pathogen vulnerabilities; V(D)J knockouts (Rag1/Rag2-null SCID)
   are lethal without sterile environment.

2. **Persistent viruses should target layer boundaries.** As discussed
   above — concrete evidence in the 001-series attempts.

3. **Autoimmune disease susceptibility should correlate with HLA
   polymorphism.** HLA is the most polymorphic locus in the human
   genome, driven by persistent-virus selection. Most autoimmune
   diseases have HLA associations as their strongest genetic
   risk factor. T1DM (HLA-DR3/DR4), MS (HLA-DRB1*15:01), AS
   (HLA-B27), celiac (DQ2/DQ8). This is predicted by the model
   (the adaptive-innate interface is where mismatch manifests).

4. **Ancient immune pathways should be exploitable by therapies
   without causing total immunosuppression.** Drugs like colchicine
   (targeting NLRP3 / gouty arthritis pathway — ancient inflammasome
   biology) can be used long-term without the massive vulnerability
   that comes with modern biologics (rituximab = anti-CD20 B-cell
   depletion — young pathway, big hole when blocked).

## What the attempts 101-107 will cover

- **attempt_101**: Prokaryotic immunity — CRISPR-Cas discovery,
  mechanism, classification (Makarova 2020 scheme), plus
  restriction-modification, toxin-antitoxin, and abortive infection.
  ~3.5 Ga timescale.

- **attempt_102**: Eukaryogenesis and early innate — the
  autophagy/mitophagy machinery, RNA interference as an antiviral,
  why eukaryotic cells need a different defense model.
  ~2.0 Ga timescale.

- **attempt_103**: Invertebrate metazoan innate — *Drosophila* Toll
  as the seminal discovery, sea urchin complement, insect hemocytes.
  ~600 Ma to ~500 Ma.

- **attempt_104**: Convergent adaptive in jawless vertebrates — VLR
  system, LRR diversification in lampreys (Pancer & Cooper 2004).
  ~500 Ma.

- **attempt_105**: RAG, V(D)J, MHC in jawed vertebrates — origin as
  transposon domestication (Kasahara 2007; Huang 2016); genomic
  evidence from cartilaginous fish. ~450 Ma.

- **attempt_106**: Mammalian refinements — class switching,
  germinal centers, maternal IgG transfer, the special case of
  placental tolerance. ~200 Ma to ~150 Ma.

- **attempt_107**: Persistent-virus coevolution — HLA polymorphism,
  KIR-HLA coadaptation, TRIM5α, APOBEC3G. Cross-links to the
  001-series attempts. ~30 Ma onward.

Each will follow a common structure: (a) phylogenetic placement, (b)
molecular mechanisms with modern understanding, (c) what problem the
transition solved, (d) what it could NOT solve (setting up the next
layer), (e) disease / dysfunction signatures in modern organisms, (f)
key sources from published primary literature.

## Methodological cautions

Several common pitfalls to avoid in this series:

1. **Deep-time dates are provisional.** Molecular-clock estimates for
   events >500 Ma have large uncertainty (factor of 2 not uncommon).
   Cite the source whenever possible; use qualitative "around X Ga"
   unless a specific study with CI is being referenced.

2. **"Primitive" is loaded.** Modern lampreys are not primitive
   vertebrates; they are modern vertebrates descended from a
   jawless-vertebrate ancestor. Their VLR system has also evolved for
   ~500 Ma, just along a different line. Avoid the connotation.

3. **Absence of evidence in fossil record ≠ absence of evolution.**
   Soft tissues including immune organs leave almost no fossils.
   Most evolutionary timing comes from molecular phylogenetics.

4. **Convergent vs homologous.** Care with claiming "the same pathway
   existed in X" when what is meant is "a functionally similar
   pathway." NF-κB in cnidarians IS homologous. Toll in flies and
   TLRs in humans ARE homologous. VLRs and Igs are NOT homologous
   (convergent).

5. **Cross-linking to medical/ work.** The 001-series attempts and
   the medical/ directory have established specific claims about
   persistent viruses and disease mechanism. The 100-series should
   cite those for mechanism-level detail; the 100-series should
   AVOID re-deriving conclusions already carefully established
   elsewhere in the repo.

## What this attempt does NOT do

- Doesn't claim a unified theory of immunity. The "layered
  architecture" is a useful framing, not an ontology.
- Doesn't settle controversies about RAG origin specifics. The
  transposon-derivation view has strong evidence but details (when,
  which Transib family member) are active research.
- Doesn't reduce the immune system to its adaptive component. The
  innate layer carries most of the actual protection; adaptive is an
  add-on.

---

## Gap opened by this attempt

- **Structural**: no single figure or timeline diagram exists in the
  subdirectory yet; should be built up as attempts 101-107 accumulate.
- **Empirical**: lacking in primary citations; this attempt is a
  framework; attempts 101-107 will have specific sources.
- **Cross-referential**: no cross-links yet to attempts 001/002 of the
  other instance; those should appear in attempt_107 explicitly.

## Status

Framework attempt only. Next iterations: populate specific transitions.

---

*Filed: 2026-04-15 | biology/evolution/attempts/attempt_100*
*Parallel-instance convention: this attempt belongs to the 100-199 range; 001-099 is the other instance's scope.*
*Companion: biology/evolution/PROBLEM.md; biology/evolution/attempts/attempt_001_persistence_as_strategy.md (cross-references expected but the 100-series does not modify 001-series files).*
