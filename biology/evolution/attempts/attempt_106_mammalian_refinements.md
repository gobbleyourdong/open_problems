# attempt_106 — Mammalian Refinements: Class Switching, Germinal Centers, and Viviparity

> Sixth attempt in the 100-series. The jawed-vertebrate adaptive
> system (attempt_105) was already fully operational by ~450 Ma. What
> did mammals (~200 Ma and later) add? Three elaborations stand out:
> (1) dedicated class switching for antibody isotype versatility,
> (2) germinal centers with organized affinity maturation, and (3) a
> maternal-fetal immunological relationship that handles the paradox
> of carrying a genetically distinct organism inside. A fourth
> elaboration — cancer immunosurveillance via NK/NKT — also
> crystallizes in this window.

---

## The mammalian lineage

Mammals are synapsid amniotes whose direct lineage diverged from
reptiles ~320 Ma (synapsid/sauropsid split). True mammals
(Mammaliaformes → Mammalia) emerged in the Triassic ~230-200 Ma.

Three modern groups:
- **Monotremes** (platypus, echidna) — egg-laying, basal.
- **Marsupials** (kangaroos, opossums) — pouch development after
  short gestation.
- **Eutherian/Placental mammals** — extended viviparity with invasive
  placenta. 94% of living mammal species.

The three groups give us a comparative window on mammalian
immunological innovation. Features shared across all three
represent ancestral-mammal innovations; features eutherian-specific
reflect placental-lineage specialization.

## Ancestral mammalian innovations (all three groups)

### 1. Class switching recombination (CSR)

In jawed-vertebrate B cells, the Ig heavy chain is first expressed
as IgM (and IgD via alternative splicing). Mammalian B cells (and,
to a lesser extent, non-mammalian tetrapods) can SWITCH the
constant region to IgG, IgA, IgE (mammals) or IgY (birds, reptiles).
Each isotype has distinct effector properties:

- **IgM**: first antibody made; pentameric; good complement activator.
- **IgG**: four subclasses (IgG1-4 in humans); main serum antibody;
  placental transfer (eutherians); opsonizes for phagocytes.
- **IgA**: secreted at mucosal surfaces; dimeric in secretions;
  handles gut/respiratory mucosa.
- **IgE**: low abundance; binds mast cells and basophils; anti-parasite
  + allergic responses.

CSR is catalyzed by AID (activation-induced cytidine deaminase), which
introduces uracils in switch regions; the uracils are processed by
mismatch repair and base excision repair machinery to produce
double-strand breaks; non-homologous end-joining religates the cut
ends, looping out the intervening constant-region DNA.

Discovery:
**Muramatsu M, Kinoshita K, Fagarasan S, Yamada S, Shinkai Y,
Honjo T (2000).** "Class switch recombination and hypermutation
require activation-induced cytidine deaminase (AID), a potential
RNA editing enzyme." *Cell* 102:553-563. PMID 11007474.

**Revy P, Muto T, Levy Y, Geissmann F, Plebani A, Sanal O, Catalan
N, Forveille M, Dufourcq-Labelouse R, Gennery A, Tezcan I, Ersoy F,
Kayserili H, Ugazio AG, Brousse N, Muramatsu M, Notarangelo LD,
Kinoshita K, Honjo T, Fischer A, Durandy A (2000).** "Activation-
induced cytidine deaminase (AID) deficiency causes the
autosomal recessive form of the Hyper-IgM syndrome (HIGM2)."
*Cell* 102:565-575. PMID 11007475.

Same issue of Cell, complementary findings: the knockout mouse
(Muramatsu) and the human patient (Revy) converged on AID as the key
enzyme. Patients with AID deficiency (HIGM2) cannot produce IgG,
IgA, or IgE — only IgM.

### 2. Somatic hypermutation (SHM) in germinal centers

Also AID-dependent. After antigen activation, B cells enter germinal
centers (specialized structures in secondary lymphoid tissues) where
they undergo SHM of their V-region exons. Affinity-maturation:
selection for higher-affinity variants over successive rounds.

### 3. Germinal centers

Anatomically distinct structures (dark zone + light zone) in
lymph nodes and spleen where B-T cooperation produces class switching
and affinity maturation. Germinal centers are pan-mammalian but have
analogs in birds and reptiles (bursa of Fabricius in birds).

Reference: **Victora GD, Nussenzweig MC (2022).** "Germinal Centers."
*Annu Rev Immunol* 40:413-442. PMID 35113731.

### 4. Dedicated mucosal immunity

Mammals developed distinct mucosal-immunity machinery:
- Gut-associated lymphoid tissue (GALT) including Peyer's patches
- IgA secretion across epithelia via polymeric Ig receptor (pIgR)
- M cells for antigen sampling from gut lumen
- Regulatory T cells (Tregs) for tolerance of food and microbiome
  antigens

### 5. Milk and the immune transfer to neonate

Lactation is a synapsid/mammalian innovation (pre-dates placentation
in some lineages). Milk contains maternal IgA, lactoferrin,
lysozyme, and cytokines that protect the neonate's gut.

## Eutherian-specific innovations

### 1. FcRn-mediated transplacental IgG transfer

In eutherian mammals, maternal IgG crosses the placenta into fetal
circulation, giving the newborn pre-made antibodies against
pathogens the mother has encountered. Mechanism:

**FcRn (neonatal Fc receptor)** is an MHC class I-like molecule that
binds IgG at acidic pH (endosomes) and releases at neutral pH
(extracellular). This allows transcytosis of IgG across placental
trophoblasts and, in neonates, across intestinal enterocytes.

**Simister NE, Mostov KE (1989).** "An Fc receptor structurally related
to MHC class I antigens." *Nature* 337:184-187. PMID 2911353. Original
FcRn characterization.

**Roopenian DC, Akilesh S (2007).** "FcRn: the neonatal Fc receptor
comes of age." *Nat Rev Immunol* 7:715-725. PMID 17703228. Definitive
review.

FcRn also determines IgG half-life in serum: FcRn bound IgG is
recycled rather than lysosomally degraded. This is why IgG has a
~21-day half-life (vs ~6 days for IgA, ~5 days for IgM). Therapeutic
antibodies exploit this for once-weekly or once-monthly dosing.

### 2. Placental tolerance: the central mammalian immunological paradox

An eutherian placenta contains fetal tissue expressing PATERNAL MHC
molecules (from the father's contribution to the fetal genome). This
is essentially an allograft. Why doesn't the maternal immune system
reject it?

Mechanisms (partly understood):
- **Trophoblast MHC avoidance**: placental trophoblasts at the
  maternal interface express low/absent classical MHC class I;
  instead they express HLA-G (nonclassical, low-polymorphism,
  immunosuppressive).
- **Uterine NK cell tolerance**: decidual NK cells are
  abundant but have altered inhibitory receptor repertoire; they
  interact with HLA-G and DO NOT kill trophoblasts; they actually
  support placental vascular remodeling.
- **Treg enrichment at maternal-fetal interface**: regulatory T cells
  expanded; programmed local suppression.
- **Indoleamine 2,3-dioxygenase (IDO) expression** by trophoblast:
  depletes tryptophan locally, inhibiting T cell activation.
- **Programmed cell death ligand** (PD-L1) expression at interface.

Reference: **Erlebacher A (2013).** "Immunology of the maternal-fetal
interface." *Annu Rev Immunol* 31:387-411. PMID 23298207.

This is why **anti-PD-1 / anti-PD-L1 checkpoint inhibitor drugs can
cause adverse pregnancy outcomes**: they disrupt the same pathway
that placental tolerance relies on.

### 3. Syncytin: retroviral co-option for placenta

The syncytiotrophoblast layer of the placenta is formed by fusion of
trophoblast cells into a multinucleate syncytium. Fusion is mediated
by syncytin-1 (and syncytin-2 in primates; ERVs elsewhere).

**Syncytin-1 is derived from a retroviral env gene** of a HERV-W
integration event in the primate lineage ~25-40 Ma. The retroviral
fusion protein was repurposed for host-host cell fusion.

Reference: **Mi S, Lee X, Li X, Veldman GM, Finnerty H, Racie L,
LaVallie E, Tang XY, Edouard P, Howes S, Keith JC Jr, McCoy JM
(2000).** "Syncytin is a captive retroviral envelope protein involved
in human placental morphogenesis." *Nature* 403:785-789. PMID
10693809.

Remarkable fact: **every mammalian placenta with syncytial
trophoblasts relies on a co-opted retroviral fusion protein, but
the specific retrovirus varies by lineage.** Mice use a different
ERV-derived syncytin (syncytin-A) than primates. Ruminants use yet
another. Multiple independent retroviral captures for the same
placental function — the ultimate example of persistent-virus
coevolution with host physiology (links to attempt_107 and the
001-series HERV theme).

## Mammalian innate refinements

### NK cell education

Natural killer (NK) cells were known in mammals for decades before
their "missing self" principle (Ljunggren & Kärre 1990) clarified
their role: NK cells kill targets LACKING MHC class I, catching
virus-infected cells that have downregulated MHC to escape T cell
recognition.

NK cells undergo "education" in bone marrow: they acquire inhibitory
receptors (NKG2A, KIR in humans, Ly49 in mice) matched to the host's
MHC alleles. This allows them to recognize "self" MHC and be
inhibited by it.

Reference: **Karre K (2008).** "Natural killer cell recognition of
missing self." *Nat Immunol* 9:477-480. PMID 18425103. Retrospective
on the missing-self principle.

### KIR-HLA coevolution

Killer-cell Immunoglobulin-like Receptors (KIRs) on human NK cells
bind HLA-C and some HLA-B. KIR gene family expanded specifically in
primates; KIR loci are highly polymorphic, parallel to HLA loci.

KIR-HLA coevolution was driven by persistent viruses (especially
HCMV). See attempt_107 for the full treatment.

### Plasmacytoid dendritic cells (pDCs)

pDCs are specialized dendritic cells that produce massive amounts of
type I interferon in response to viral nucleic acids via TLR7/9. They
are a mammalian innovation; reptiles have related cells but less
specialized.

## The cost of mammalian immunity

Mammals pay a metabolic price for their elaborate immune system.
Estimated: 2-5% of total energy expenditure in a resting human goes
to maintaining lymphoid tissue, bone marrow hematopoiesis, and
antibody production.

Mammalian-specific immunological diseases:
- **Autoimmune diseases** with HLA associations (T1DM, MS, RA, lupus)
- **Allergic disease** (IgE-mediated) — especially prevalent in
  modern humans; hygiene hypothesis invokes evolutionary mismatch
  between Th2-skewed immunity and modern clean environments.
- **Pregnancy complications** (preeclampsia, recurrent miscarriage) —
  maternal-fetal immune miscommunication.
- **Graft-versus-host disease** after bone marrow transplant —
  mature donor T cells attacking recipient tissue.

## Why the elaborations happened when they did

### Viviparity pressure

Longer gestation → longer immunological coexistence of maternal and
fetal tissues → stronger selection for placental tolerance mechanisms.
Eutherian mammals with ~9-month (human) or longer gestations show the
most elaborate maternal-fetal immunology.

### Endothermy

Warm-blooded animals are more hospitable to pathogens (higher
replication rates at 37°C for many bacteria and viruses). Active
endothermy selects for more sophisticated immunity.

### Hair + milk + parental care

Extended neonatal care means longer windows for horizontal transmission
between parent and offspring. IgG placental transfer and IgA milk
transfer protect during this window.

### Social group size

Mammals (especially primates) live in social groups where persistent
viruses can circulate. HCMV, EBV, HPV, HHV-6 exploitation of this
ecology feeds back into host HLA/KIR evolution (attempt_107).

## Open questions

1. **Monotreme immunology**: limited characterization. Do they have
   CSR? Germinal centers? FcRn? These questions matter for dating
   mammalian innovations.

2. **Marsupial vs eutherian placentation immunology**: marsupials have
   shorter gestation and pouch-based development; their maternal-fetal
   immune negotiation is less studied but likely uses different
   mechanisms.

3. **Why eosinophils and basophils?** These cells handle parasites
   and allergic responses. Their elaboration in mammals vs other
   vertebrates is under-studied.

4. **Lineage-specific HERV-syncytin captures**: has been studied in
   primates, mice, ruminants. Are there other mammalian lineages
   with yet different syncytin origins?

## Links to other attempts

- attempt_100 (framework): populates "mammals (~200 Ma)" row.
- attempt_105 (jawed adaptive): established the CSR-capable Ig
  framework that mammals elaborated.
- attempt_107 (persistent-virus coevolution, next): HCMV's role in
  driving KIR-HLA coevolution; HERV syncytin capture; the direct
  bridge to 001-series attempts on persistent viruses.

## Key sources

Primary:
- Simister NE, Mostov KE 1989 *Nature* 337:184 (FcRn). PMID 2911353.
- Mi S et al. 2000 *Nature* 403:785 (Syncytin from HERV-W). PMID 10693809.
- Muramatsu M et al. 2000 *Cell* 102:553 (AID required for CSR and SHM).
  PMID 11007474.
- Revy P et al. 2000 *Cell* 102:565 (AID deficiency = HIGM2). PMID 11007475.

Reviews:
- Roopenian DC, Akilesh S 2007 *Nat Rev Immunol* 7:715 (FcRn).
  PMID 17703228.
- Karre K 2008 *Nat Immunol* 9:477 (missing self). PMID 18425103.
- Erlebacher A 2013 *Annu Rev Immunol* 31:387 (maternal-fetal
  interface). PMID 23298207.
- Victora GD, Nussenzweig MC 2022 *Annu Rev Immunol* 40:413
  (germinal centers). PMID 35113731.

Historical:
- Ljunggren HG, Kärre K 1990 *Immunol Today* 11:237 (missing-self
  hypothesis).

---

## Gap opened

- **Monotreme immunology data gap**: the deepest-branching living
  mammals are understudied. Filling this gap would clarify which
  mammalian innovations are ancestral vs derived.
- **Placental tolerance mechanism integration**: IDO, PD-L1, HLA-G,
  uterine NK, Tregs — these are individually characterized but
  their relative contributions and interactions are partly open.
- **Syncytin captures in non-primate lineages**: each lineage's
  specific ERV source could be a window into its ancient retroviral
  history.

## Status

Complete. attempt_107 (persistent-virus coevolution: the bridge to
001-series) is next — the closing attempt of the 100-series that
cross-links immune-system evolution to the parallel work on
persistent human viruses.

---

*Filed: 2026-04-15 | biology/evolution/attempts/attempt_106*
*Follows: attempts 100, 101, 102, 103, 104, 105.*
*Parallel-instance convention: 100-199 range; 001-099 is other instance's scope.*
