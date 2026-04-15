# attempt_001 — Thymus Anatomy, Ontogeny, and Cellular Architecture

> Opening attempt in the thymus research thread. Establishes what the
> thymus is, where and when it forms, and how it is organized at the
> cellular level. Sets up subsequent attempts on T cell selection
> (002), involution (003+), and regeneration (009+).

---

## Where it sits

The human thymus is a bilobed organ in the upper anterior mediastinum,
behind the sternum and above the heart. In a child it can extend up
into the neck. After puberty it progressively shrinks (involution) and
is largely replaced by adipose tissue in adults — though active
thymic epithelium persists at low levels in residual islands lifelong.

## Embryonic origin

The thymus develops from the third pharyngeal pouch endoderm in
mammals. Around weeks 4-6 of human gestation, the third pouch gives
rise to two structures: the thymus (anterior) and the inferior
parathyroid gland (posterior). DiGeorge syndrome (22q11 deletion)
disrupts this neural-crest-dependent development and produces
varying degrees of athymia + parathyroid hypoplasia.

In comparative biology, the pharyngeal-pouch origin is conserved
across all jawed vertebrates: the thymus emerges from pharyngeal
endoderm in fish, amphibians, reptiles, birds, and mammals. Different
species use different specific pouches (pouch 3 in mammals, pouches
3-4 in birds, pouches 1-7 in some fish), but the underlying
endodermal-derivation logic is preserved across ~450 million years.

Reference: **Boehm T, Bleul CC (2007).** "The evolutionary history of
lymphoid organs." *Nature Immunology* 8:131-135. PMID 17242688.

## Cellular architecture: cortex and medulla

A mature thymic lobule has two regions distinguishable in section:

### Cortex (outer)

- Densely packed with immature thymocytes (CD4-CD8 double-negative
  through CD4+CD8+ double-positive stages).
- Cortical thymic epithelial cells (cTECs) provide the supporting
  network and present self-peptides on MHC class I and class II.
- Most thymocytes (~95%) die here via apoptosis: those that fail to
  rearrange a functional TCR, those whose TCR cannot recognize self-
  MHC at all (failure of positive selection).

### Medulla (inner)

- Less densely packed with more mature thymocytes (single-positive
  CD4 or CD8).
- Medullary thymic epithelial cells (mTECs) express thousands of
  tissue-restricted antigens (TRAs) — proteins normally produced in
  liver, pancreas, brain, etc. — under control of the master
  transcription factor AIRE (autoimmune regulator).
- T cells whose TCRs strongly bind these self-antigens are deleted
  (negative selection) or diverted into the regulatory T cell
  (Foxp3+ Treg) lineage.
- The medulla also contains thymic dendritic cells (DCs) that
  contribute to negative selection.

The cortex-to-medulla migration of developing thymocytes is the
**central tolerance pipeline**: enter at outer cortex, traverse
inward through positive then negative selection, exit from medulla
as a naive single-positive T cell.

## Cellular populations in detail

### Thymic epithelial cells (TECs)

The functional core. Two main subsets:

- **cTECs (cortical TECs)**: express thymoproteasome subunit β5t
  (encoded by PSMB11), which generates a unique peptide repertoire
  for MHC class I. β5t-deficient mice have severely reduced CD8+
  T cell production — cortical β5t is needed to positively select
  CD8+ T cells.
- **mTECs (medullary TECs)**: express AIRE, which drives promiscuous
  expression of tissue-restricted antigens. mTECs also express
  Fezf2 (the other major TRA-driving transcription factor, working
  in parallel to AIRE).

Both cTECs and mTECs derive from a common bipotent **TEC progenitor**
that expresses FOXN1. FOXN1 is the master transcription factor for
the entire TEC lineage — without it, the thymic primordium forms but
cannot recruit hematopoietic precursors and cannot mature into a
functional thymus.

Reference: **Nowell CS et al. (2011).** "Foxn1 regulates lineage
progression in cortical and medullary thymic epithelial cells but is
dispensable for medullary sublineage divergence." *PLoS Genetics*
7:e1002348.

The "nude mouse" (Foxn1 null mutant) is the classic athymic mouse
model. Nude mice have:
- No fur (FOXN1 is also expressed in skin epithelium)
- Vestigial thymic primordium that never develops
- No mature T cells
- Severe combined immunodeficiency

A homologous human FOXN1 null mutation produces the same phenotype:
**Nude/SCID syndrome** with congenital alopecia and severe T cell
deficiency. Discovered by Markert et al.; treated by thymic
transplantation.

### Thymocytes (developing T cells)

Hematopoietic precursors enter the thymus from blood (via cortico-
medullary junction). They progress through stages defined by surface
marker expression:

- **DN1 → DN4 (double-negative)**: CD4-CD8-, in cortex. Begin TCR β
  chain rearrangement.
- **DP (double-positive)**: CD4+CD8+, after pre-TCR signaling. Most
  cells here. Test TCRαβ for self-MHC recognition (positive
  selection).
- **SP (single-positive)**: CD4+CD8- (helper) or CD4-CD8+ (cytotoxic).
  Move to medulla. Test for self-tolerance (negative selection +
  Treg diversion).
- **Mature naive T cells**: exit thymus into periphery.

The rate of cell death during this pipeline is staggering: of the
~50 million daily DP thymocytes in a young adult, only ~1-2% emerge
as mature T cells. Thymopoiesis is profligate by design — the
selection pressure is intense.

### Thymic dendritic cells

Two main populations:
- Conventional DCs (cDCs) derived from blood precursors.
- Plasmacytoid DCs (pDCs).

They concentrate in the medulla, capture self-antigens (some
acquired from mTECs via cross-presentation), and contribute to
negative selection.

### Thymic B cells

A small but important population in the medulla. Express AIRE-induced
self-antigens via cross-presentation to T cells. Deletion of these
B cells alters Treg generation in mice.

## Thymic stromal architecture

Beyond the cellular populations, the thymus has unique stromal
features:

- **Hassall's corpuscles** (medulla): concentric whorls of mature mTECs.
  Function partly contested; current view: produce TSLP that supports
  Treg generation.
- **Vasculature**: blood-thymus barrier maintained at the cortex,
  isolating developing thymocytes from peripheral antigens.
- **Mesenchymal cells**: fibroblasts, vasculature-supporting cells,
  contributing to TEC niche maintenance.

## Quantitative output

In a young adult human, the thymus produces roughly:
- **5-10 × 10⁹** new naive T cells per year (estimated from TREC
  measurements)
- About **1-2% of the total peripheral T cell pool** is renewed
  yearly in young adults.

By age 60-70, this drops by >90%. Most of the elderly T cell pool
is maintained by **homeostatic peripheral expansion** of memory
cells, not by thymic output.

## TREC measurement: the molecular ruler

T cell Receptor Excision Circles (TRECs) are extrachromosomal DNA
products of V(D)J recombination at the TCR locus. They:
- Form during TCR rearrangement in the thymus
- Are stable but DO NOT replicate
- Therefore dilute as a T cell divides peripherally

TREC content per T cell is a quantitative measure of "recent thymic
emigrants." Used clinically:
- Newborn screening for SCID (TREC-low → no thymic output → severe
  immunodeficiency)
- Aging research (TREC level falls with age, tracking thymic
  involution)
- Bone marrow transplant follow-up (TREC recovery indicates thymic
  function returning)

Reference: **Douek DC et al. (1998).** "Changes in thymic function
with age and during the treatment of HIV infection." *Nature*
396:690-695. PMID 9872319. The classic paper introducing TREC for
human thymic-output measurement.

## Variation across vertebrate classes

A note on diversity from `biology/evolution/`:

- **Cartilaginous fish** (sharks, rays): true thymus, similar
  cortex/medulla. Slow involution.
- **Bony fish**: thymus often bilateral in pharyngeal area. Many
  species show seasonal fluctuations rather than dramatic
  age-involution.
- **Amphibians**: thymus undergoes substantial remodeling at
  metamorphosis; some species show seasonal cycles.
- **Reptiles**: highly variable; many show seasonal thymus
  fluctuations in addition to age-involution.
- **Birds**: have both thymus and Bursa of Fabricius (B cell
  development organ). Bursa typically involutes earlier than
  thymus in chickens.
- **Mammals**: dramatic and early involution, especially in humans.

Mammalian thymus involution is not the universal vertebrate pattern.
It's a mammalian-specific life-history adaptation.

## Open at this stage

- How exactly do FOXN1 expression levels regulate thymic activity?
  (Address in attempt_006.)
- What controls the timing of involution onset (puberty in many
  mammals, but signaling specifics)? (Attempt_004.)
- Can adult thymus be regrown to youthful function? (Attempt_009.)

## Status

Foundation document. Subsequent attempts go deeper on selection
mechanisms (002), involution (003-005), regulatory factors
(006-008), and regeneration (009+).

## Key sources

Primary:
- **Douek DC et al. 1998 *Nature* 396:690** (TRECs measure thymic
  output). PMID 9872319.
- **Boehm T, Bleul CC 2007 *Nat Immunol* 8:131** (lymphoid organ
  evolutionary history). PMID 17242688.

Reviews:
- Anderson G, Takahama Y 2012 *Trends in Immunology* 33:256
  (thymic epithelial cells and central tolerance).
- Vaidya HJ et al. 2016 *Front Immunol* 7:163 (FOXN1 in thymus
  organogenesis and development). PMID 27378598.

---

*Filed: 2026-04-15 | biology/thymus/attempts/attempt_001*
*First in the thymus research thread.*
