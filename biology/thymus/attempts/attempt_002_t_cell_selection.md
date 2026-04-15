# attempt_002 — T Cell Selection: Positive, Negative, AIRE, and Treg Generation

> Second attempt in the thymus thread. attempt_001 established what
> the thymus IS (anatomy, ontogeny, cell types). This attempt
> establishes what it DOES at the cellular decision level: how
> roughly 50 million daily double-positive thymocytes get filtered
> down to ~1-2% functional, self-tolerant T cells exiting to the
> periphery.

---

## The selection problem

A young adult thymus generates ~50 million double-positive (DP)
thymocytes per day. Each carries a randomly-assembled TCR. The
selection problem the thymus solves:

1. **Positive selection**: keep only TCRs that can recognize self-MHC
   well enough to function. ~95-98% of DP thymocytes fail this and
   die by neglect (no signal → apoptosis).
2. **Negative selection**: of those that pass, delete TCRs that bind
   self-peptide/self-MHC TOO strongly (would attack self → apoptosis).
3. **Lineage commitment**: positively-selected cells commit to CD4
   (helper) or CD8 (cytotoxic) lineage based on which MHC class
   their TCR engaged.
4. **Regulatory diversion**: a subset of CD4+ cells with intermediate-
   high TCR affinity for self-antigen are diverted to the Foxp3+
   regulatory T cell lineage instead of being deleted.

End result: of the ~50M daily DPs, ~1-2% emerge as mature naive T
cells. The other 49M die in the thymus.

This profligate strategy is the price of a randomly-generated
receptor repertoire that is vast, specific, AND self-tolerant.

## Positive selection

### Mechanism

Cortical thymic epithelial cells (cTECs) present self-peptides on
MHC class I and class II. DP thymocytes scan these via their newly-
formed αβ-TCR. Outcomes:

- **No signal** (TCR can't engage self-MHC at all): cell dies by
  neglect. This is the fate of most DPs.
- **Weak signal** (TCR recognizes self-MHC but doesn't strongly
  engage self-peptide): cell receives survival signal, proceeds to
  next stage. This is positive selection.
- **Strong signal** at this stage: typically does not yet cause
  deletion in the cortex; depends on tissue context.

### The role of cTEC-specific machinery

cTECs use specialized machinery that other cells don't:

- **Thymoproteasome** (β5t subunit, encoded by PSMB11): generates a
  unique peptide repertoire for MHC class I. Different from the
  immunoproteasome used by professional APCs.
- **Cathepsin L** (instead of cathepsin S used elsewhere): generates
  MHC class II peptides with different cleavage preferences.
- **TSSP** (thymus-specific serine protease).

This means DP thymocytes are positively selected on a peptide
repertoire SLIGHTLY DIFFERENT from what they will encounter in the
periphery on professional APCs. The biological rationale: select for
TCRs with weak self-affinity (the cTEC-presented peptides are rarely
the strongest binders), leaving room to upgrade to stronger
recognition of pathogen peptides in the periphery.

Reference: **Murata S et al. (2007).** "Regulation of CD8+ T cell
development by thymus-specific proteasomes." *Science* 316:1349-1353.
PMID 17540904. Discovery of β5t and the thymoproteasome's role.

### Lineage commitment

Positively-selected DP thymocytes become single-positive (SP) by
extinguishing one of CD4 or CD8 based on which MHC class their TCR
engaged:

- TCR engaged MHC class I → CD8+ SP (cytotoxic lineage)
- TCR engaged MHC class II → CD4+ SP (helper lineage)

Mechanistically driven by ThPOK (CD4 commitment) and Runx3 (CD8
commitment) transcription factors.

## Negative selection

After positive selection in the cortex, SP thymocytes migrate to the
medulla. Here the selection scenario inverts: signals are now searching
for cells whose TCR binds self too STRONGLY.

### The agents of negative selection

Several cell types contribute:
- **mTECs** (medullary TECs): express thousands of tissue-restricted
  antigens via AIRE.
- **Thymic dendritic cells**: cross-present antigens including some
  acquired from mTECs.
- **B cells**: small thymic medulla population, contribute to
  presenting some antigens.

### AIRE: the autoimmune regulator

AIRE is the linchpin. It is a transcription factor expressed almost
exclusively in mTECs, where it drives **promiscuous expression** of
~3000-4000 tissue-restricted antigens (TRAs) — proteins normally
expressed only in specific peripheral organs (insulin from pancreas,
thyroglobulin from thyroid, myelin proteins from CNS, etc.).

Each individual mTEC expresses only a SMALL FRACTION of these TRAs at
any given time (estimated 1-3% of TRAs per mTEC at any moment). The
mTEC population collectively covers the full TRA repertoire through
this cell-by-cell sampling. A developing thymocyte traversing the
medulla encounters many mTECs and is exposed to most TRAs.

Reference: **Anderson MS et al. (2002).** "Projection of an
immunological self shadow within the thymus by the aire protein."
*Science* 298:1395-1401. PMID 12376594. The foundational paper
establishing AIRE's role in TRA expression.

### APECED: AIRE deficiency in humans

Loss-of-function mutations in AIRE cause **APECED** (Autoimmune
Polyendocrinopathy-Candidiasis-Ectodermal Dystrophy), also called
APS-1 (Autoimmune Polyglandular Syndrome type 1).

Clinical features:
- Multi-organ autoimmunity (most common: hypoparathyroidism,
  Addison's disease/adrenal failure, type 1 diabetes, hypothyroidism)
- Chronic mucocutaneous candidiasis (driven by neutralizing
  autoantibodies against IL-17 and IL-22)
- Ectodermal dystrophy (nail and dental defects)

APECED is the **canonical proof** that central tolerance via AIRE
prevents autoimmunity. Disrupt AIRE in humans → broad autoimmune
disease across multiple organs whose antigens AIRE was supposed to
present.

Reference: **Nagamine K et al. (1997).** "Positional cloning of the
APECED gene." *Nature Genetics* 17:393-398. PMID 9398839. AIRE
identification via positional cloning of APECED kindreds.

### Fezf2: the parallel TRA-driving transcription factor

In addition to AIRE, mTECs use **Fezf2** to drive a partly distinct
set of TRAs. Fezf2-deficient mice develop autoimmunity affecting a
different set of organs than AIRE-deficient mice. The two
transcription factors operate in parallel.

Reference: **Takaba H et al. (2015).** "Fezf2 orchestrates a
thymic program of self-antigen expression for immune tolerance."
*Cell* 163:975-987. PMID 26544942.

### Outcome of strong TCR signal

A thymocyte whose TCR strongly engages an mTEC- or DC-presented
self-antigen has three possible fates:

1. **Apoptosis** (clonal deletion) — the most common outcome for
   strongly-self-reactive TCRs.
2. **Treg differentiation** — see next section.
3. **Anergy / functional inactivation** — minor pathway.

The choice depends on the strength of TCR signal, co-stimulation,
cytokine context, and the developmental stage at which signal occurs.

## Regulatory T cell (Treg) generation in the thymus

A subset of CD4+ thymocytes with intermediate-to-strong TCR affinity
for self-antigen are NOT deleted but instead develop into thymic
**Foxp3+ regulatory T cells (tTregs)**.

### Mechanism

- Strong-but-not-too-strong TCR signal (in the "intermediate-high"
  affinity range) primes thymocytes for the Treg lineage.
- TGF-β signaling protects from apoptosis and drives Foxp3 expression.
- IL-2 / CD25 signaling supports Treg precursor expansion.
- Hassall's corpuscle-derived TSLP supports the Treg differentiation
  niche.

The "Goldilocks zone" of TCR affinity:
- **Low affinity** → naive conventional T cell exits to periphery.
- **Intermediate-high affinity** → Treg differentiation.
- **Very high affinity** → clonal deletion.

This means the Treg compartment is enriched for self-reactive TCRs.
Tregs are SPECIFICALLY tuned to recognize self-antigens — and their
function is to suppress immune responses to those self-antigens
peripherally.

Reference: **Bautista JL et al. (2009).** "Intraclonal competition
limits the fate determination of regulatory T cells in the thymus."
*Nature Immunology* 10:610-617. PMID 19430476. Demonstrates that the
size of the niche limits Treg generation per clone.

### tTreg vs pTreg

Two main Treg sources:
- **tTreg (thymic Treg)**: generated in thymus during development.
  Self-antigen specific. Stable Foxp3+ phenotype.
- **pTreg (peripheral Treg)**: induced in peripheral tissues from
  naive CD4+ T cells in tolerogenic contexts (e.g., gut, where
  microbial-antigen-driven Treg generation occurs — see
  attempt_112 of biology/evolution/).

Both are Foxp3+ but have somewhat different functional profiles
and distribution.

## Quantitative consequences

- Of the ~50 M daily DPs, ~95-98% die by neglect (failure of
  positive selection).
- Of the ~5% that pass positive selection, ~50% die in negative
  selection.
- ~3-5% of starting DPs make it out as mature naive SPs.
- A small fraction (~3-5% of CD4+ SPs) are tTregs.
- Daily naive T cell output in young adult: ~1-3 million per day
  (estimated, varies by age and species).

The mature naive T cell repertoire in a young adult is ~10⁹ unique
TCRs across the body, accumulated over years of thymic output and
maintained by homeostatic peripheral expansion.

## How selection failures cause autoimmunity

Selection failures happen and accumulate with age. Three failure
modes:

1. **AIRE-dependent**: failure of mTEC TRA expression (APECED in
   humans; partial in some sporadic autoimmunity).
2. **TCR-affinity threshold drift**: with age and chronic
   inflammation, the "deletion vs Treg vs survival" thresholds shift;
   more potentially-autoreactive cells escape.
3. **Peripheral checkpoint failures**: even properly-selected T cells
   can become pathogenic if peripheral tolerance mechanisms fail
   (PD-1, CTLA-4, Treg suppression).

Most common autoimmune disorders are genetically associated with HLA
alleles that present specific self-peptides — a clue that thymic
selection on a particular HLA background creates the disease-prone
TCR repertoire.

This explains why HLA is the strongest genetic risk factor for many
autoimmune diseases: HLA determines what self-peptides cTECs and
mTECs present, which determines which TCRs are positively/negatively
selected, which determines what autoimmune targets are vulnerable.

## Why this matters for the thymus thread

For attempts on involution and regeneration:
- Thymic selection requires **functional cTECs and mTECs**, not just
  thymocyte production.
- mTECs are particularly vulnerable to involution — AIRE-expressing
  mTECs decline faster than other thymic populations with age.
- Regeneration strategies need to restore not just thymocyte
  development but also the mTEC/AIRE compartment to maintain
  central tolerance.

A naive-T-cell-output increase WITHOUT proper central tolerance
restoration could in principle increase autoimmune risk. This is a
real concern for some thymic-regeneration interventions.

## Open at this stage

- Why does intermediate-affinity TCR signaling sometimes drive Treg
  fate and sometimes drive deletion? The "decision boundary" is not
  fully understood at the molecular level.
- Are there other TRA-driving transcription factors beyond AIRE
  and Fezf2 awaiting discovery?
- How does mTEC AIRE expression decline with age, and is it
  recoverable? (Address in attempts 003-005.)

## Status

Foundation for selection mechanisms. attempt_003 will cover
involution: mechanisms of thymic shrinkage with age.

## Key sources

Primary:
- **Nagamine K et al. 1997 *Nat Genet* 17:393** (AIRE positional
  cloning). PMID 9398839.
- **Anderson MS et al. 2002 *Science* 298:1395** (AIRE drives
  immunological self-projection). PMID 12376594.
- **Murata S et al. 2007 *Science* 316:1349** (thymoproteasome).
  PMID 17540904.
- **Bautista JL et al. 2009 *Nat Immunol* 10:610** (intraclonal
  competition limits Treg fate). PMID 19430476.
- **Takaba H et al. 2015 *Cell* 163:975** (Fezf2 parallel TRA
  driver). PMID 26544942.

Reviews:
- Klein L, Kyewski B, Allen PM, Hogquist KA 2014 *Nat Rev Immunol*
  14:377 (positive and negative selection).
- Abramson J, Anderson G 2017 *Annu Rev Immunol* 35:85 (thymic
  epithelial cells).

---

## Gap opened

- **Decision rules at intermediate TCR affinity**: deletion vs Treg
  vs anergy partly characterized but molecular threshold unclear.
- **mTEC stem cell dynamics with age**: how AIRE+ mTEC pools
  decline and whether they can be regenerated is the key question
  for adult thymic restoration.
- **HLA-disease associations through thymic selection lens**:
  which HLA alleles create which auto-peptide-vulnerable repertoires
  is mostly unmapped at single-peptide resolution.

## Status

Complete. attempt_003 (involution mechanisms) is next.

---

*Filed: 2026-04-15 | biology/thymus/attempts/attempt_002*
*Follows: attempt_001 (anatomy and architecture).*
