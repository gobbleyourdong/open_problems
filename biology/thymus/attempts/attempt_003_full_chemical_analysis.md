# attempt_003 — Full Chemical Analysis: Every Compound the Thymus Makes and Uses

> Inserted at user request. attempts 001-002 covered the thymus
> structurally and operationally. This attempt is the chemistry of
> what's actually being made and consumed at every step from
> hematopoietic precursor entry to mature naive T cell exit.
>
> Organized by molecular class. Each compound: structure where
> useful, source cells, target cells, function, and where it sits in
> the developmental pipeline.

---

## 1. Thymic peptide hormones (TEC-secreted, classic "thymic hormones")

These are the canonical "thymic hormones" — peptides isolated from
thymic tissue extracts in the 1970s-80s, characterized for their
ability to induce T cell maturation in cultured peripheral blood.
Their physiological roles in vivo are partly debated, but they are
real molecules made by the thymus.

### Thymosin α1 (Tα1)

- **Structure**: 28 amino acid peptide. Sequence (N→C):
  Ac-SDAAVDTSSEITTKDLKEKKEVVEEAEN-OH
- **Molecular weight**: ~3108 Da
- **N-terminus**: acetylated (Ac-Ser at position 1)
- **Source**: cleaved from a 113-aa precursor (prothymosin α) in
  thymic epithelial cells and other tissues
- **Function**: enhances T cell maturation in vitro; in vivo:
  upregulates TLR signaling, IFN-γ production, NK and dendritic cell
  activity
- **Clinical use**: licensed in 35+ countries (brand: Zadaxin) for
  hepatitis B/C adjunct therapy and as immune modulator. Approved
  doses: 1.6 mg subcutaneous, 2× weekly.

Reference: **Goldstein AL et al. (1977).** "Thymosin α1: isolation
and sequence analysis of an immunologically active thymic
polypeptide." *PNAS* 74:725-729. PMID 264694. Original
characterization.

### Thymopoietin (TP)

- **Structure**: three splice variants of the same gene (TMPO),
  molecular weights ~39, 51, 75 kDa.
- **Localization**: nuclear envelope (also called LAP2). Originally
  identified for inducing T cell differentiation; later found to
  have a structural role in nuclear lamina too.
- **Function**: thymopentin (TP5), the active 5-aa fragment with
  sequence Arg-Lys-Asp-Val-Tyr (RKDVY), reproduces most immunological
  effects.
- **Clinical use**: thymopentin (Timunox) used for immunostimulation.

Reference: **Goldstein G et al. (1979).** "Thymopoietin pentapeptide
and thymic hormone." *Science* 204:1309-1310.

### Thymulin (formerly facteur thymique sérique, FTS)

- **Structure**: nonapeptide (9 amino acids):
  H-pyroGlu-Ala-Lys-Ser-Gln-Gly-Gly-Ser-Asn-OH (pyroGlu = pyroglutamate)
- **N-terminus**: pyroglutamate (cyclized glutamine)
- **Critical feature**: BIOLOGICALLY ACTIVE ONLY WHEN BOUND TO Zn²⁺
  in 1:1 stoichiometry. Apo-thymulin is inactive; Zn-binding induces
  active conformation.
- **Source**: medullary thymic epithelial cells.
- **Function**: induces T cell differentiation in vitro; modulates
  cytokine production; influences NK activity.
- **Clinical relevance**: serum thymulin levels correlate with
  thymic activity. Decline with age (parallel to thymic involution).
  **Zinc deficiency reduces thymulin activity** — a candidate
  mechanism linking nutritional zinc to immune function (covered in
  attempt_008).

Reference: **Bach JF, Dardenne M (1973).** "Studies on thymus
products. Functional and biochemical characterization of the thymic
serum factor (FTS)." *Immunology* 25:353-366.

### Thymic humoral factor γ2 (THF-γ2)

- **Structure**: octapeptide. Sequence: Leu-Glu-Asp-Gly-Pro-Lys-Phe-Leu
- **Source**: thymic epithelium
- **Function**: T cell differentiation in vitro

(Less prominent than the three above.)

### Net hormone-output summary

The four "classic thymic hormones" share a pattern: small peptides
(5-28 aa) made by thymic epithelial cells, with documented in vitro
T-cell-maturation activity, and physiological levels that decline
with age.

Modern view: these hormones contribute to systemic immune tone but
are NOT essential for T cell development per se (T cells develop in
thymic stromal cocultures lacking them). The DLL4-Notch + cytokine
network (sections below) is doing the actual development; the
hormones are auxiliary.

---

## 2. Cytokines in the thymic microenvironment

### IL-7 (interleukin-7)

- **Structure**: 152-aa glycoprotein (after signal peptide
  cleavage), ~25 kDa. Four-helix bundle cytokine.
- **Source in thymus**: cTECs primarily, also some mTECs and
  fibroblasts.
- **Receptor**: IL-7R (IL-7Rα/CD127 + common γ chain/CD132)
- **Function**: SURVIVAL signal for DN and DP thymocytes.
  Induces antiapoptotic Bcl-2. Drives proliferation at DN2-DN4 stages.
- **Clinical relevance**: recombinant IL-7 (CYT107) tested in
  clinical trials for thymic regeneration, HIV, lymphopenia.
  See attempt_006.
- **Loss of function**: IL-7 or IL-7Rα null mice have severely
  hypoplastic thymus and SCID-like immunodeficiency. Same in humans
  (IL-7Rα mutation = SCID).

### IL-15

- **Structure**: 4-helix-bundle cytokine, ~14-15 kDa.
- **Source in thymus**: TECs, some thymic stromal cells.
- **Receptor**: IL-15Rα (high affinity), trans-presented in complex
  with the cytokine to CD8αα IELs and NK cells. Common γ chain.
- **Function**: NK cell development, CD8 memory maintenance,
  innate-like T cell development (NKT, IELs).

### KGF (keratinocyte growth factor / FGF7)

- **Structure**: ~28 kDa (194 aa precursor, mature protein ~163 aa).
  Heparin-binding fibroblast growth factor family.
- **Source in thymus**: stromal mesenchymal cells.
- **Target**: thymic epithelial cells (cTECs and mTECs).
- **Function**: TROPHIC SIGNAL for TEC proliferation and survival.
  Required for normal TEC compartment maintenance.
- **Clinical relevance**: palifermin (Kepivance) is recombinant
  human KGF, FDA-approved for chemo-induced oral mucositis. Tested
  for thymic regeneration after stem cell transplant. Doses:
  60 µg/kg/day IV. Detail in attempt_006.

Reference: **Min D et al. (2002).** "Sustained thymopoiesis and
improvement in functional immunity induced by exogenous KGF
administration in murine models of aging." *Blood* 99:4592-4600.
PMID 12036893.

### BMP4 (bone morphogenetic protein 4)

- **Structure**: ~408 aa precursor, dimerized active form ~26 kDa.
- **Source**: thymic mesenchyme.
- **Function**: required for FOXN1 induction in thymic epithelium
  during organogenesis. Also functions postnatally in TEC
  maintenance.

### TSLP (thymic stromal lymphopoietin)

- **Structure**: 159-aa precursor, mature 134-aa protein, ~18 kDa.
  Four-helix-bundle cytokine.
- **Source**: Hassall's corpuscles (specifically) and other mTECs.
- **Receptor**: TSLPR + IL-7Rα.
- **Function**: drives DC-mediated Treg generation in the medulla
  via OX40L upregulation on DCs. Bridges to peripheral allergic
  immunity (TSLP from epithelium drives Th2 responses in lung/skin
  outside the thymus).

Reference: **Watanabe N et al. (2005).** "Hassall's corpuscles
instruct dendritic cells to induce CD4+CD25+ regulatory T cells in
human thymus." *Nature* 436:1181-1185. PMID 16121185.

### TGF-β (transforming growth factor β)

- **Structure**: 25 kDa homodimer, three isoforms (TGF-β1, -β2, -β3).
- **Function in thymus**: PERMITS Treg differentiation by curbing
  negative selection; drives Foxp3 expression.

Reference: **Ouyang W et al. (2010).** "Foxo proteins cooperatively
control the differentiation of Foxp3+ regulatory T cells." *Nature
Immunology* 11:618-627. (Treg context.)

### IL-2

- **Structure**: 15 kDa. Four-helix-bundle.
- **Function in thymus**: required for tTreg precursor proliferation
  and Foxp3 stabilization. Acts via IL-2R (IL-2Rα/CD25 + IL-2Rβ +
  γc).

---

## 3. Chemokines (directing cell migration within and out of the thymus)

Thymocyte development requires precise spatial choreography. The
thymus uses chemokine gradients to direct migrations.

### CCL25 (TECK — Thymus-Expressed Chemokine)

- **Structure**: small chemokine (~10 kDa), CC-family.
- **Source in thymus**: cTECs and mTECs (abundant in cortex, also
  expressed in medulla).
- **Receptor**: CCR9 on thymocytes (and on intestinal homing T cells
  later).
- **Function**: recruits hematopoietic precursors to the thymus from
  blood; guides DN→DP migration in the cortex; positions DP cells
  for cTEC interaction.

### CXCL12 (SDF-1 — Stromal Cell-Derived Factor 1)

- **Structure**: small CXC-family chemokine, ~8-10 kDa.
- **Source**: cortical and corticomedullary junction stroma.
- **Receptor**: CXCR4 on thymocytes.
- **Function**: drives DN→DP transition; chemoattractant for early
  thymocytes. CXCR4-deficient thymocytes have defective DN
  progression.
- **Outside thymus**: same axis is critical for HIV co-receptor
  use, hematopoietic stem cell homing, embryonic development.

### CCL19 / CCL21 (medullary chemokines)

- **Structure**: CC-family chemokines, ~10 kDa each.
- **Source**: mTECs (especially CCL21).
- **Receptor**: CCR7 on positively-selected SP thymocytes.
- **Function**: directs SP thymocytes from cortex into medulla after
  positive selection. CCR7 expression is the surface signature of
  successful positive selection. Cells without CCR7 do not migrate
  to the medulla and miss negative selection.
- **Clinical resonance**: same CCR7 axis directs naive T cells from
  blood into lymph node T zones in the periphery.

### CCL21 specifically and AIRE-dependent expression

A subset of mTEC-derived chemokine signaling is AIRE-controlled,
linking the medulla's antigen-presentation function with its
chemokine-attractant function.

Reference: **Lkhagvasuren E et al. (2013).** "Lymphotoxin β
receptor regulates the development of CCL21-expressing subset of
postnatal medullary thymic epithelial cells." *J Immunol*
190:5110-5117. PMID 23585674.

---

## 4. Notch signaling: DLL4 is the master commitment ligand

### DLL4 (Delta-Like 4)

- **Structure**: ~685-aa transmembrane protein. Extracellular domain
  contains DSL (Delta-Serrate-Lag2) domain + 8 EGF repeats.
- **Source**: thymic epithelial cells (cTECs predominantly).
- **Target**: NOTCH1 receptor on hematopoietic precursors entering
  the thymus.
- **Function**: drives T cell lineage specification. Without DLL4-
  Notch1 signaling, hematopoietic precursors entering the thymus
  develop into B cells or other non-T fates instead.

### Mechanism

When DLL4 binds NOTCH1, the Notch receptor is cleaved:
- First cleavage by ADAM10/17 metalloprotease (S2 cleavage)
- Second cleavage by γ-secretase complex (S3 cleavage)
- Released **NICD (Notch intracellular domain)** translocates to
  nucleus
- NICD binds CSL/RBPJ transcription factor + Mastermind coactivator
- Drives transcription of T-cell-commitment genes (TCF7, GATA3,
  preTCRα, RAG1/RAG2)

### Stage-specific requirement

Notch signaling intensity required:
- **DN1 → DN2**: high. Loss of DLL4 here = block at DN1.
- **DN2 → DN3**: high. Maintains T-lineage commitment, suppresses
  alternative fates.
- **DN3 → DN4 → DP**: progressively decreasing.
- **DP onward**: minimal. SP cells no longer require Notch.

DLL4 binding declines from DN1 to DN4 then becomes undetectable in
DP and SP — matching the developmental dependence.

References:
- **Hozumi K et al. (2008).** "Delta-like 4 is indispensable in
  thymic environment specific for T cell development." *Journal of
  Experimental Medicine* 205:2507-2513. PMID 18824585.
- **Koch U et al. (2008).** "Delta-like 4 is the essential,
  nonredundant ligand for Notch1 during thymic T cell lineage
  commitment." *J Exp Med* 205:2515-2523. PMID 18824585.

### Other Notch ligands

DLL1 is present in thymic epithelium but is not strictly required —
DLL4 alone is sufficient. Jagged1/2 are also present; they have
modulatory but non-essential roles.

---

## 5. Lipid mediator: sphingosine-1-phosphate (S1P) for thymic egress

### S1P (sphingosine-1-phosphate)

- **Structure**: bioactive sphingolipid. Sphingosine + phosphate
  group at the 1-OH. Molecular formula C₁₈H₃₈NO₅P, MW ~379 Da.
- **Source**: red blood cells, platelets, lymph endothelial cells
  produce S1P; degraded by S1P lyase (SPL) in tissue.
- **In the thymus**: S1P is LOW in the thymic parenchyma (because
  thymic dendritic cells express SPL which degrades it) and HIGH in
  blood (because RBCs constantly export it).
- **Function**: drives THYMIC EGRESS of mature single-positive
  thymocytes.

### Mechanism

- Mature SP thymocytes upregulate the transcription factor **KLF2**
  in their final maturation stage.
- KLF2 drives expression of **S1P receptor 1 (S1PR1)** on the
  cell surface.
- The S1P gradient (low in thymic medulla, high in blood) draws
  S1PR1-expressing cells into the bloodstream.
- Cells WITHOUT KLF2 or S1PR1 cannot egress and accumulate in the
  thymic medulla.

References:
- **Matloubian M et al. (2004).** "Lymphocyte egress from thymus and
  peripheral lymphoid organs is dependent on S1P receptor 1."
  *Nature* 427:355-360. PMID 14737169.
- **Carlson CM et al. (2006).** "KLF2 is required for thymocyte
  emigration." *Journal of Experimental Medicine* 203:127-138.

### Clinical relevance: fingolimod

**Fingolimod (FTY720)** is an S1P receptor modulator used to treat
multiple sclerosis. Mechanism: it functionally inactivates S1PR1
on lymphocytes (by inducing receptor internalization). Thymocytes
and naive T cells become trapped in lymphoid organs and cannot
egress to peripheral tissue. Reduces autoreactive T cell trafficking
to the CNS.

Same molecule, opposite goal: in MS we want to BLOCK egress; in
thymic regeneration we want NORMAL egress.

---

## 6. Surface markers at each developmental stage

The "chemistry" of T cell development is also defined by what surface
proteins are being made and at what levels. The progression:

### Entry stage: ETPs / DN1

- **CD117** (c-Kit, stem cell factor receptor) — high
- **CD44** (hyaluronan receptor) — high
- **CD25** (IL-2Rα) — negative
- **CD3** complex — none
- **CCR9 + CCR7** — for thymic homing

### DN2

- **CD117** — high
- **CD44** — high
- **CD25** — gained (now positive)
- **TCRβ rearrangement** beginning

### DN3

- **CD117** — declining
- **CD44** — declining
- **CD25** — high
- **pre-TCR** complex assembly: rearranged TCRβ + invariant pTα +
  CD3 chains
- **β-selection** checkpoint: pre-TCR signal required to proceed

### DN4

- **CD25** — lost
- **Cell cycle**: massive proliferation
- **TCRα rearrangement** beginning

### DP (double-positive)

- **CD4 + CD8αβ** — both positive
- **TCRαβ + CD3** complex on surface
- **CD69** — induced upon positive selection signal
- Apoptosis-prone: ~95% die here

### SP (single-positive)

- **CD4+ or CD8+** (one extinguished)
- **CD3 + TCRαβ** — high
- **CD27, CD28** — high
- **CCR7** — induced (drives migration to medulla)
- **CD62L (L-selectin)** — induced late
- **S1PR1** — induced very late (KLF2-driven)
- **CD69** — extinguished as cell prepares to egress

### Mature naive emigrant

- **CD45RA+** (in humans), **CD45RO−**
- **CD62L+** (lymph node homing)
- **CCR7+** (LN homing)
- **CD3+CD4+ or CD3+CD8+**
- **TREC+** (recent thymic emigrant marker)

The full surface "barcode" at each stage involves ~20-30 distinct
proteins changing in concert — the chemistry of T cell development
is in large part the controlled expression and degradation of these
membrane proteins.

---

## 7. AIRE-driven tissue-restricted antigens (TRA peptides)

### The diversity

mTECs under AIRE control express ~3000-4000 distinct
tissue-restricted antigen (TRA) genes. Each protein is processed
into peptides (8-11 aa for MHC class I; 12-25 aa for MHC class II)
and displayed on MHC.

The TRA repertoire includes:
- **Insulin** (preproinsulin) — for pancreatic β-cell tolerance
- **Thyroglobulin** — for thyroid tolerance
- **Myelin basic protein, PLP** — for CNS tolerance
- **Tyrosinase, TRP1/2** — for melanocyte tolerance
- **Retinal antigens** (S-antigen, IRBP) — for ocular tolerance
- **Salivary gland proteins** — for salivary tolerance
- **Sperm-specific proteins** — for testis tolerance
- **Many enzymes, transporters, structural proteins** of every
  major organ system

### Quantitative scope

- Each individual mTEC expresses only **1-3% of total TRAs at any
  given time** (single-cell heterogeneity).
- Population coverage: any given TRA is expressed by some
  mTECs across the AIRE+ population.
- Total TRA peptide-MHC complexes presented to a thymocyte during
  its medullary residence: thousands of distinct peptides.

### Why this matters chemically

The "chemistry" of negative selection is the chemistry of
peptide-MHC binding. Each TRA peptide binds with characteristic
affinity to the host's particular MHC alleles. A TCR that engages
a given peptide-MHC with high affinity gets deleted. The effective
"forbidden list" of T cell specificities is determined by:
- Which TRAs are expressed (AIRE/Fezf2 transcription)
- Which peptides those proteins yield (proteasomal cleavage)
- Which peptides bind which MHC alleles (HLA-specific)
- Which TCRs would bind those peptide-MHCs (probabilistic)

Reference: **Sansom SN et al. (2014).** "Population and single-cell
genomics reveal the Aire dependency, relief from Polycomb silencing,
and distribution of self-antigen expression in thymic epithelia."
*Genome Research* 24:1918-1931. PMID 25224068.

---

## 8. TCR rearrangement byproducts: T cell receptor excision circles (TRECs)

### Structure

When the TCR genes undergo V(D)J recombination, the intervening DNA
between the joined gene segments is EXCISED as a circular DNA
molecule. The most-used clinical marker is **sjTREC** (signal joint
TREC), formed during δREC-ψJα rearrangement that deletes the entire
TCRδ locus during TCRα assembly.

- **Structure**: extrachromosomal circular DNA.
- **Composition**: a recombination signal sequence (RSS) joint —
  the heptamer + spacer + nonamer sequences left intact when the
  intervening DNA was looped out.
- **Stability**: TRECs are stable but DO NOT replicate. Each cell
  division dilutes them by half.
- **Use**: TREC content per T cell decreases with peripheral
  proliferation. **sjTREC level in blood is the standard quantitative
  measure of recent thymic emigration.**

### Clinical use

- **Newborn screening for SCID** (T cell receptor excision circles
  test): now standard in many developed countries since ~2008.
  TREC-low neonates are identified for confirmatory immunology.
- **Aging research**: TREC level tracks thymic involution.
- **Bone marrow transplant follow-up**: TREC recovery indicates
  thymic function returning post-transplant.

Reference: **Douek DC et al. (1998).** "Changes in thymic function
with age and during the treatment of HIV infection." *Nature*
396:690-695. PMID 9872319.

---

## 9. Selection-relevant metabolites

### Retinoic acid (vitamin A metabolite)

- **Structure**: all-trans retinoic acid (ATRA), C₂₀H₂₈O₂, MW 300.
- **Source**: thymic dendritic cells expressing RALDH (retinaldehyde
  dehydrogenase).
- **Function**: imprints gut-homing receptor (α4β7 integrin, CCR9)
  on certain T cells; supports Treg differentiation in some contexts.

### Kynurenine pathway intermediates

- **IDO (indoleamine 2,3-dioxygenase)**: enzyme that degrades
  tryptophan, expressed by some thymic and peripheral DCs.
- **Kynurenine** and its downstream metabolites: tolerogenic for T
  cells. Local tryptophan depletion + kynurenine accumulation
  curbs T cell activation.
- More peripherally important than thymically; mentioned for
  completeness.

### Glucocorticoids (locally produced)

- TECs and thymocytes themselves can produce corticosterone/cortisol.
- Local glucocorticoids modulate the threshold for negative
  selection (the "mutual antagonism" model: TCR signal vs steroid
  signal compete for cell fate).

Reference: **Vacchio MS et al. (1994).** "Steroid production in the
thymus: implications for thymocyte selection." *J Exp Med*
179:1835-1846.

---

## 10. The output: chemical signature of a mature naive T cell exiting the thymus

After ~21-28 days in the thymus, a mature naive T cell exits with:

- One uniquely-rearranged TCRαβ heterodimer (composed of one TCRα
  protein + one TCRβ protein, randomly assembled from V/D/J segments)
- Approximately 30,000-50,000 TCR molecules on the surface
- Co-receptor CD4 OR CD8αβ (lineage decision made)
- CD3 complex (γδεζ chains, signaling apparatus)
- Co-stimulatory receptors: CD28, ICOS (low), CD27
- Adhesion: CD62L, LFA-1, VLA-4
- Chemokine receptors: CCR7, CXCR4
- S1PR1 (for circulation)
- Survival cytokine receptors: IL-7Rα (for peripheral homeostatic
  maintenance)
- TCR-rearrangement TRECs in the cytoplasm (extrachromosomal DNA)
- Distinct DNA methylation pattern marking thymic origin

Mass-balance perspective: the thymus consumes ~150 μg of cellular
biomass per day in its functional adult state (~10⁹ thymocytes ×
mostly apoptosed) and releases ~1-3 mg of mature T cells (low
output relative to the input — most of the mass is lost in
selection apoptosis).

---

## Summary table of the major compounds

| Class | Specific compound | Source cells | Function |
|---|---|---|---|
| Peptide hormone | Thymosin α1 (28 aa) | TECs | Systemic T cell maturation |
| Peptide hormone | Thymopoietin (39/51/75 kDa splice forms) | TECs | T cell differentiation in vitro |
| Peptide hormone | Thymulin (9 aa, Zn-required) | mTECs | T cell differentiation; zinc-dependent |
| Cytokine | IL-7 | cTECs | Survival/proliferation of DN/DP |
| Cytokine | IL-15 | TECs | NK + memory CD8 + IEL |
| Cytokine | KGF (FGF7) | Stromal mesenchyme | TEC trophic support |
| Cytokine | BMP4 | Mesenchyme | TEC FOXN1 induction |
| Cytokine | TSLP | Hassall's corpuscles | Treg induction via DCs |
| Cytokine | TGF-β | Multiple | Treg differentiation |
| Cytokine | IL-2 | Activated cells | Treg precursor expansion |
| Chemokine | CCL25 (TECK) | cTECs/mTECs | DN→DP migration via CCR9 |
| Chemokine | CXCL12 (SDF-1) | Cortical stroma | DN→DP migration via CXCR4 |
| Chemokine | CCL19/CCL21 | mTECs | SP migration to medulla via CCR7 |
| Notch ligand | DLL4 | cTECs | T-lineage specification (essential) |
| Lipid mediator | S1P | RBCs/platelets externally; metabolized in thymus | Thymic egress via S1PR1 |
| Surface markers | CD117/CD44/CD25/CD4/CD8/CD3/CD69/CCR7/CD62L/S1PR1 | Thymocytes themselves | Stage definition + function |
| AIRE-driven | ~3000-4000 TRA proteins | mTECs | Negative selection / Treg generation |
| Metabolite | Retinoic acid | Thymic DCs | Gut-homing imprinting |
| Metabolite | Kynurenine (from IDO) | Thymic DCs | Tolerogenic |
| Metabolite | Local glucocorticoids | TECs/thymocytes | Selection threshold modulation |
| DNA byproduct | sjTREC | Thymocyte (TCRα assembly) | Marker of recent thymic emigration |

---

## What this changes for the rest of the thread

attempts 004-011 will discuss involution and regeneration. The
chemistry analysis here means we know what to monitor:

- **Regeneration evidence should include**: increased thymic IL-7,
  KGF response, recovery of DLL4 expression on TECs, increased
  sjTREC in blood, restoration of AIRE+ mTEC compartment, recovery
  of CCR7+ SP migration to medulla.
- **Adverse-outcome warnings**: TEC regeneration without proper
  AIRE/mTEC reconstitution = thymopoiesis without proper central
  tolerance = potential autoimmunity.
- **The TRIIM trial** (attempt_010) showed sjTREC recovery as one
  of its primary endpoints; that's now a meaningful chemical
  marker.

---

## Key sources

Primary:
- Goldstein AL et al. 1977 *PNAS* 74:725 (thymosin α1 sequence). PMID 264694.
- Bach JF, Dardenne M 1973 *Immunology* 25:353 (thymulin/FTS).
- Watanabe N et al. 2005 *Nature* 436:1181 (Hassall's corpuscle TSLP). PMID 16121185.
- Min D et al. 2002 *Blood* 99:4592 (KGF for thymopoiesis). PMID 12036893.
- Hozumi K et al. 2008 *J Exp Med* 205:2507 (DLL4 indispensable). PMID 18824585.
- Koch U et al. 2008 *J Exp Med* 205:2515 (DLL4 essential nonredundant).
- Matloubian M et al. 2004 *Nature* 427:355 (S1P egress). PMID 14737169.
- Douek DC et al. 1998 *Nature* 396:690 (TRECs). PMID 9872319.
- Sansom SN et al. 2014 *Genome Res* 24:1918 (Aire single-cell TRA expression). PMID 25224068.

---

## Status

Complete. Subsequent attempts (004-011) cover involution,
regeneration, and clinical interventions building on this
chemistry foundation.

---

*Filed: 2026-04-15 | biology/thymus/attempts/attempt_003*
*Inserted at user request — full chemical analysis of thymus operations.*
*Follows: attempts 001 (anatomy), 002 (selection mechanisms).*
