# attempt_107 — Persistent-Virus Coevolution: Bridge to the 001-Series

> Seventh and final attempt in the planned 100-series. This is the
> **bridge document** connecting immune-system-evolution
> (100-series, from ~3.5 Ga prokaryotic defense to ~200 Ma mammalian
> elaborations) to the parallel 001-series on persistent human
> viruses (CVB, EBV, HPV, HCMV, HHV-6, plus non-viral persistent
> organisms: H. pylori, P. gingivalis, Demodex). The two tracks meet
> here: persistent pathogens have been THE dominant selection
> pressure on primate and human adaptive immunity over the last
> ~100-30 Ma.

---

## Recap: the layered architecture meets persistent pathogens

From attempt_100's framework: vertebrate immunity is a stack of
evolutionary layers, each added to solve a problem the previous layer
could not handle. Persistent viruses exploit the BOUNDARIES between
layers. Specific examples:

- **EBV**: hides in memory B cells — the very cells whose adaptive
  function is to persist. The adaptive layer's memory mechanism IS
  the niche.
- **HCMV**: hides in myeloid precursors (CD34+) that express low
  MHC class I. The innate-to-adaptive handoff is the weak point.
- **HPV**: hides in basal keratinocytes, below the epithelial
  surface where immune surveillance is limited. Compartment-based
  escape.
- **HHV-6**: integrates into telomeric regions in a small fraction of
  hosts. The genomic-integration layer (ancient, dating to our LUCA
  heritage, CRISPR-like in spirit) is exploited via a eukaryotic
  analog.
- **CVB**: makes 5'-UTR-deleted persistent variants that replicate at
  minimal level, under the radar. Receptor-level mutation escape.

Each is a different molecular solution to the same strategic problem
(stay alive inside a host with elaborate adaptive immunity). Together
they map out the limit surface of vertebrate adaptive immunity.

## HLA polymorphism as the central coevolution signal

### Mechanism of balancing selection

The MHC (in humans: HLA) locus is the most polymorphic region of the
human genome. >25,000 HLA alleles have been characterized across
human populations. The polymorphism is not random; it is concentrated
in the peptide-binding groove — the amino acid residues that actually
touch pathogen-derived peptides.

Three mutually-compatible mechanisms maintain this diversity:

1. **Heterozygote advantage**: HLA heterozygotes present a larger
   peptide repertoire than homozygotes. Broader repertoire = better
   chance of detecting any given pathogen. Heterozygotes have higher
   fitness under pathogen pressure (Doherty & Zinkernagel proposed
   this in the 1970s; Nobel 1996).

2. **Negative frequency-dependent selection (rare-allele advantage)**:
   common HLA alleles are escape targets for pathogens; rare alleles
   escape pathogen countermeasures. As an allele becomes common, it
   becomes less effective; rare alleles then become advantageous.
   Oscillation maintains diversity.

3. **Fluctuating selection**: different pathogens favor different
   alleles at different times. Over evolutionary time, no allele
   is persistently best.

Reference: **Hedrick PW (2002).** "Pathogenic defense and pathogen-
mediated balancing selection in the major histocompatibility
complex." *Evolution* 56(10):1902-1908. PMID 12449481. Classic
population-genetics framing of these mechanisms.

### Evolutionary rate of HLA

The peptide-binding groove residues show dN/dS >> 1 (nonsynonymous
substitutions far outnumber synonymous), evidence of strong positive
selection. This signature is concentrated in the specific codons
that encode groove residues, not spread across the protein. Detected
in all mammalian MHC loci studied.

### Which pathogens drove HLA evolution?

Persistent viruses contribute disproportionately:
- **Herpesviruses** (EBV, HCMV, HHV-6): long coevolution, chronic
  antigen exposure, many latency-associated proteins.
- **Retroviruses** (HERV ancestors, modern HIV): integrate into host
  genome; severe fitness consequences for inability to suppress.
- **HBV, HCV**: hepatitis persistence drives HLA class I
  diversification around liver antigens.

Acute viruses (influenza, measles) impose strong EPIDEMIC selection
but contribute less to LONG-TERM balancing selection because the
selection episodes are transient.

Reference: **Borghans JA et al. (2004).** "MHC polymorphism under
host-pathogen coevolution." *Immunogenetics* 55:732-739.

## KIR-HLA coevolution

### The NK cell recognition system

Natural killer cells use Killer-cell Immunoglobulin-like Receptors
(KIRs) to recognize HLA class I on target cells. Inhibitory KIRs
ligating self-HLA tell NK cells "don't kill this cell." Activating
KIRs do the opposite.

Viruses that DOWNREGULATE HLA class I to escape T cell recognition
(EBV, HCMV, HIV, HPV all do this) become VISIBLE to NK cells —
missing self. The virus-host arms race involves both T-cell-evasion
and NK-cell-evasion, which push in opposite directions.

### KIR locus polymorphism

KIR is extraordinarily polymorphic (both in copy number and allelic
diversity), parallel to HLA. KIR genes are absent in some
individuals' genomes entirely (copy-number variation). Two broad
haplotypes (A and B) differ in activating vs inhibitory KIR content.

### The HCMV driver

HCMV encodes multiple proteins (UL18, UL40, US2-11) that manipulate
host HLA. HCMV carriage may be THE dominant selective driver of KIR
diversity in humans.

Reference: **Parham P, Moffett A (2013).** "Variable NK cell receptors
and their MHC class I ligands in immunity, reproduction and human
evolution." *Nature Reviews Immunology* 13:133-144. PMID 23334245.
Canonical review.

The **pregnancy connection** is striking: KIR genotype affects
pregnancy outcome. Mothers with "KIR AA" (homozygous for A
haplotypes, fewer activating KIRs) and "HLA-C2+" fetus have higher
rates of preeclampsia. The NK-cell-mediated trophoblast invasion
regulation is the link. So KIR-HLA coevolution has dual driver:
viral pressure (especially HCMV) + reproductive success.

## HERV integrations: the retroviral fossil record

8%+ of the human genome is retroviral in origin (HERVs), per
attempt_100 audit. The implications:

### As fossils of past infections

Most HERV integrations happened 100-40 Ma (primate-specific and
older-mammalian lineages). Some HERV-K HML-2 elements integrated
within the last 200,000 years — recent in evolutionary terms.

Each HERV family's phylogenetic distribution across species tells us
when the original retrovirus was circulating in that lineage. This
is a unique window into deep viral history.

### As current antivirals

Some HERVs are still transcribed; their Env proteins can block
infection by related exogenous retroviruses via receptor interference.
Fv1 and Fv4 loci in mice provide such resistance to murine leukemia
virus; similar elements exist in humans.

### As co-opted functions

- **Syncytin-1 and syncytin-2** in primate placenta (from HERV-W
  and HERV-FRD respectively; see attempt_106).
- **Innate immune regulation**: HERV-K and other HERV transcripts
  are pattern-recognition substrates for cGAS, TLR3, MDA5. In some
  cancers and autoimmune diseases, HERV transcript activation is
  a mechanism driving inflammation.

Reference: **Grandi N, Tramontano E (2018).** "Human Endogenous
Retroviruses Are Ancient Acquired Elements Still Shaping Innate
Immune Responses." *Front Immunol* 9:2039. PMID 30250464.

## Host restriction factors under positive selection

Primate and human genomes contain many antiviral "restriction factors"
— intrinsic intracellular proteins that block viral replication.
Classical examples:

### TRIM5α

Interferes with retroviral capsid uncoating. Different primates have
different TRIM5α variants adapted to block different retroviruses.
Owl monkey TRIM5α is a chimera with cyclophilin A (TRIMCyp), an
independent solution to the same problem.

Reference: **Sawyer SL, Wu LI, Emerman M, Malik HS (2005).** "Positive
selection of primate TRIM5α identifies a critical species-specific
retroviral restriction domain." *PNAS* 102:2832-2837. PMID 15689398.

TRIM5α's SPRY domain shows extreme positive selection in primates
— one of the fastest-evolving protein domains known in human. The
driver: coevolving retroviruses.

### APOBEC3G

Cytidine deaminase that hypermutates retroviral cDNA during reverse
transcription. HIV Vif protein counters APOBEC3G by degrading it.

Reference: **Sheehy AM, Gaddis NC, Choi JD, Malim MH (2002).** "Isolation
of a human gene that inhibits HIV-1 infection and is suppressed by the
viral Vif protein." *Nature* 418:646-650. PMID 12167863.

### Tetherin / BST-2

Physically tethers budding virions to the cell surface. HIV Vpu
counters tetherin. Other viruses have their own antagonists.

Reference: **Neil SJ, Zang T, Bieniasz PD (2008).** "Tetherin inhibits
retrovirus release and is antagonized by HIV-1 Vpu." *Nature* 451:
425-430. PMID 18200009.

### SAMHD1

Depletes dNTP pools in quiescent cells, starving reverse transcription.
HIV-2 Vpx counters. HIV-1 cannot, explaining part of its restricted
cell-type tropism.

### The positive-selection signature

Most host restriction factors show strong positive selection
signatures in primate phylogenies — dN/dS >> 1 at specific residues.
These residues are typically the ones that directly contact viral
proteins. The pattern is an arms race: as virus evolves to evade,
host evolves to re-target.

Reference: **Compton AA, Emerman M (2013).** "Convergence and
divergence in the evolution of the APOBEC3G-Vif interaction reveal
ancient origins of simian immunodeficiency viruses." *PLoS
Pathog* 9:e1003135. PMID 23359341.

## Specific cross-links to the 001-series

### CVB (attempt_002 of 001-series)

CVB does NOT directly drive HLA evolution on the same timescale as
herpesviruses because acute clearance is the norm. But the minority
of hosts who develop persistent 5'-UTR-deleted CVB form a lineage-
specific reservoir.

Relevant HLA: HLA-DR3/DR4 associations with T1DM (see attempt_001
of 001-series + medical/t1dm/).

### EBV (attempt_003 of 001-series)

EBV exploits the memory B cell niche. Relevant HLA: HLA-DRB1*15:01
is a strong risk allele for MS; EBV is now the best-evidenced
environmental trigger for MS (Bjornevik 2022 Science; cited in
001-series). The HLA-EBV coevolution is ancient and strong.

### HPV (attempt_004 of 001-series)

HPV species-specificity is extreme; each primate lineage has its
own HPV types. Host-HPV coevolution may be as old as the primates
themselves (>60 Ma).

### HCMV (attempt_005 of 001-series)

HCMV is THE dominant driver of human KIR diversity (Parham & Moffett
2013). The KIR-HLA-C2 interaction is shaped primarily by HCMV.

### HHV-6 (attempt_006 of 001-series)

Chromosomally-integrated HHV-6 (ciHHV-6) in ~1% of the population
is the most extreme example of viral-genome integration into a
modern human immune-relevant locus.

### Non-viral persistent organisms (attempts 007-009)

H. pylori, P. gingivalis, Demodex: these drive HLA through different
antigenic exposures. The HLA-B27/ankylosing spondylitis association
may involve gut microbial antigen mimicry. The 001-series expansion
to non-viral persistent organisms extends the coevolution story
beyond viruses.

## Open questions

1. **How will vaccination against persistent viruses reshape HLA
   evolution?** HPV vaccination is the first-ever human-directed
   selection pressure ON a persistent virus. As HPV-16/18 diminish
   in vaccinated populations, HLA alleles tuned to those types may
   become less advantageous. Evolutionary time needed to see effects:
   centuries to millennia.

2. **Why do some persistent viruses not drive HLA as strongly as
   others?** HCMV is the strongest KIR driver; EBV is the strongest
   HLA-class-II driver. What makes some viruses more "coevolutionarily
   potent" than others?

3. **Can HERV activation reactivate old immune pathways?** Some
   evidence that HERV transcription in response to modern pathogens
   (SARS-CoV-2, for example) reactivates ancient antiviral signals.
   Worth investigating.

4. **Does the 001-series expansion to bacteria (H. pylori, P.
   gingivalis) and arthropods (Demodex) need additional
   coevolution-signature analyses?** Yes — the 100-series has mostly
   focused on virus-driven HLA evolution. Microbial and parasite-
   driven HLA and innate-receptor evolution is understudied in
   this repo.

## The layered-architecture closure

The 100-series started with prokaryotic immunity (attempt_101) ~3.5
Ga. It closes here with primate HLA polymorphism ~30 Ma. The
intervening ~3.47 billion years built the stack of defenses that
modern humans carry.

Key unifying theme: **every layer of immunity coevolved with
particular classes of pathogens.** Restriction-modification with
phages, TLRs with bacterial PAMPs, V(D)J with pathogen diversity,
HLA with persistent viruses. Immunity is not a SYSTEM evolved in
isolation — it is a reaction to specific selection pressures at
specific times.

The next 100-400 years of immune evolution will be shaped by:
- Human-directed selection (vaccines, antivirals)
- Pathogen-emergence driven by changes in ecology, climate, human
  density, mobility
- Genetic-modification tools (CRISPR editing) creating novel selection
  on human germline

The pace of change will exceed anything in the 3.5 Ga history of
immune evolution. We are now the selection pressure.

## Links to other attempts

- attempt_100 (framework): this is the final "current age" row of the
  timeline table.
- attempts 101-106: all feed into this attempt's cross-layer
  observations.
- **001-series** (persistent-virus framework): this attempt is the
  100-series' explicit bridge to that framework. Every specific
  persistent virus discussed in the 001-series has its HLA/KIR/HERV
  coevolution signature briefly summarized here.

## Key sources

Primary / foundational:
- Doherty PC, Zinkernagel RM 1975 *Lancet* 1:1406 (MHC restriction,
  Nobel 1996).
- Hedrick PW 2002 *Evolution* 56:1902 (MHC balancing selection). PMID
  12449481.
- Sheehy AM, Gaddis NC, Choi JD, Malim MH 2002 *Nature* 418:646
  (APOBEC3G). PMID 12167863.
- Sawyer SL et al. 2005 *PNAS* 102:2832 (TRIM5α positive selection).
  PMID 15689398.
- Neil SJ, Zang T, Bieniasz PD 2008 *Nature* 451:425 (tetherin).
  PMID 18200009.
- Compton AA, Emerman M 2013 *PLoS Pathog* 9:e1003135 (APOBEC3G-Vif
  arms race). PMID 23359341.
- Parham P, Moffett A 2013 *Nat Rev Immunol* 13:133 (KIR-HLA
  coevolution). PMID 23334245.

Reviews:
- Grandi N, Tramontano E 2018 *Front Immunol* 9:2039 (HERV shaping
  innate responses). PMID 30250464.
- Borghans JA et al. 2004 *Immunogenetics* 55:732 (MHC polymorphism
  under host-pathogen coevolution).

Cross-reference to 001-series:
- attempt_001 of 001-series (persistence as strategy)
- attempts 002-006 (CVB, EBV, HPV, HCMV, HHV-6 specifically)
- Optional: attempts 007-009 (H. pylori, P. gingivalis, Demodex —
  non-viral persistent organisms, which extend the coevolution
  theme to bacteria and arthropods)

---

## Gap opened (for future attempts or cross-track work)

- **Microbial-and-parasite-driven HLA evolution** — understudied
  compared to virus-driven.
- **Vaccine-driven selection as a future driver** — HPV vaccination
  is a natural experiment; Ebola and COVID vaccination add more.
  How will modern medical intervention affect the HLA trajectory?
- **Trained immunity and heritable epigenetic changes** — whether
  these bridge adaptive and innate in a way that provides
  trans-generational protection against specific persistent
  organisms.

## Status

Complete. **This closes the planned 100-series.** attempts 108-199
remain available for extensions (e.g., protist immunity, cnidarian-
specific details, non-retroviral endogenous viral elements, host-
commensal immunology). The 100-series framework is done.

---

*Filed: 2026-04-15 | biology/evolution/attempts/attempt_107*
*Follows: attempts 100, 101, 102, 103, 104, 105, 106.*
*Parallel-instance convention: 100-199 range; 001-099 is other instance's scope.*
*Explicit bridge to 001-series completed.*
