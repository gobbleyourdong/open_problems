# attempt_004 — Human Papillomavirus: Ancient Coevolution, Type Diversity, and Vaccine-Era Selection

> Per-virus deep dive. HPV is the only persistent organism on the
> list where **prophylactic vaccination is already deployed at scale**
> — Gardasil 9 since 2014 — and therefore the only one where we can
> observe real-time evolutionary response to strong selection
> pressure.
>
> **VERIFICATION STATUS:** generated primarily from trained priors;
> specific numeric figures and citations flagged below have been
> hedged or marked for verification in the parallel audit loop. The
> structural/qualitative claims are reliable; specific trial
> percentages and vaccine-efficacy figures should be verified against
> source before use in clinical or manuscript contexts.
>
> Cross-cutting framework: attempt_001 (persistence-as-strategy).
> Companion per-virus: attempt_002 (CVB), attempt_003 (EBV).

---

## Phylogenetic placement

**Family:** Papillomaviridae
**Host range:** Papillomaviruses infect essentially all amniotes —
humans, other mammals, birds, reptiles. Each species hosts its own
repertoire. This is one of the most cospeciated viral families known.

**Human types:** >200 HPV "types" identified (type is a classification
based on L1 gene sequence similarity; distinct types differ by >10%
in L1 nucleotide sequence). Organized into 5 genera:

- **Alphapapillomavirus (α-HPV)** — mucosal + some cutaneous; includes
  all high-risk oncogenic types and the low-risk genital-wart types
- **Betapapillomavirus (β-HPV)** — skin commensals; most common on
  normal skin; some associated with non-melanoma skin cancer in
  immunocompromised (EV/epidermodysplasia verruciformis pattern)
- **Gammapapillomavirus (γ-HPV)** — cutaneous; common warts
- **Mupapillomavirus (μ-HPV)** — plantar warts and similar
- **Nupapillomavirus (ν-HPV)** — a single type (HPV-41)

**Coevolution timescale:** the papillomavirus-host cospeciation record
extends hundreds of millions of years. Estimates of mammalian papillomavirus
diversification are >100 Ma. **Strict species-specificity** — HPV
types do not cross-infect other species under normal conditions.
Attempts to infect non-human primate cells with HPV-16 fail at
multiple steps. This is the strongest cospeciation signature of any
virus family on the persistent-organism list.

## Genome and lifecycle

- **~8 kb circular dsDNA** — among the smallest persistent-virus
  genomes on the list
- ~8 protein-coding genes: E1 (helicase), E2 (transcription regulator),
  E4 (late), E5/E6/E7 (oncoproteins in HR types), L1 (major capsid),
  L2 (minor capsid)
- Non-enveloped icosahedral capsid

**The lifecycle is tied to epithelial differentiation** — this is the
key evolutionary innovation:

```
HPV enters basal epithelial cells via microabrasions
    ↓
Episomal genome established in basal layer (low copy number, ~50-200)
    ↓
Basal cell divides — HPV replicates once per host-cell cycle (E1/E2)
    ↓
Daughter cell enters suprabasal / differentiation zone
    ↓
High-level viral gene expression begins (E4, E5, E6, E7)
    ↓
In the stratum granulosum / corneum layers: L1/L2 expression + virion assembly
    ↓
Mature virions released in shed keratinocytes
```

The virus times virion production to the outermost, about-to-be-shed
layers of epithelium — which are:
1. Far from immune surveillance (cornified layer)
2. About to be lost anyway (no fitness cost to cell if virus kills it)
3. Abundant extracellular surface area for transmission

**This is a fundamentally different persistence mechanism from the
viruses covered so far:**
- Not true latency (like EBV)
- Not mutation-driven replication defect (like CVB)
- Not chromosomal integration by default (though integration does
  occur in cancer progression)
- Rather: **life-cycle-linked spatial and temporal compartmentalization**

## High-risk vs low-risk types

Within α-HPV, a sharp phenotypic distinction:

**High-risk (HR) — oncogenic:**
- HPV-16, 18 — dominant cervical cancer etiology
- HPV-31, 33, 45, 52, 58 — covered by Gardasil 9
- HPV-35, 39, 51, 56, 59, 68 — less common but still classified HR

**Low-risk (LR) — benign:**
- HPV-6, 11 — >90% of genital warts and laryngeal papillomas
- HPV-40, 42, 43, 44, 54, 61, 70, 72, 81 — other benign types

The molecular distinction between HR and LR is concentrated in E6 and
E7 oncoprotein functions:

**E6 (HR types):**
- Binds p53 via E6AP (E6-associated protein)
- Recruits E6AP's E3 ubiquitin ligase activity → p53 polyubiquitination
  → proteasomal degradation
- Loss of p53 means apoptosis and cell-cycle arrest signals are
  disabled
- LR E6 binds p53 weakly and does not efficiently drive degradation

**E7 (HR types):**
- Binds Rb (retinoblastoma protein)
- Displaces E2F from Rb → E2F-driven cell-cycle entry (S-phase)
- HR-E7 binds Rb with much higher affinity than LR-E7
- Also binds p107, p130, HDACs — multiple cell-cycle regulators affected

**The E6/E7 partnership produces:**
- S-phase entry without the normal checkpoint controls
- Blocked apoptosis despite DNA damage accumulation
- Genomic instability
- Over time: mutation accumulation → malignant transformation

Evolutionarily, E6 and E7 of HR types are optimized for one thing:
driving differentiation-committed keratinocytes BACK into S-phase so
the virus can replicate in a non-dividing cellular environment.
Cancer is the accidental consequence when this happens in basal cells
(via integration-triggered dysregulation) rather than in the intended
suprabasal differentiation zone.

## Integration — the cancer switch

In most HPV infections, the genome stays **episomal** (circular,
extrachromosomal, low copy number). The normal lifecycle never
integrates.

In a subset of HR-HPV infections (particularly HPV-16 and HPV-18),
the genome **integrates into the host chromosome**. Integration
typically:

1. Breaks the circular genome in the E2 gene
2. Destroys the E2 transcription factor that normally represses E6/E7
3. Results in constitutive high-level E6/E7 expression
4. Eliminates the late-genes / virion-production phase
5. Produces a replication-deficient but oncogene-expressing cell

Integration is **strongly associated with malignant progression** but
is not technically required — some cervical cancers remain episomal.
In HPV-positive oropharyngeal cancer, integration is less common than
in cervical cancer (more remain episomal). The stepwise model:

```
Infection with HR-HPV (episomal)
    ↓
Persistent infection (months to years)
    ↓
Cervical intraepithelial neoplasia grades 1 → 2 → 3 (CIN1 → CIN2 → CIN3)
    ↓
Genomic integration (in a subset of cells)
    ↓
Invasive carcinoma
```

The full process typically takes 10–20 years from initial infection
to invasive disease. The long timescale matches the persistence-
mechanism expectation from attempt_001.

## Disease-as-incidental framing

Like the other persistent viruses: HPV has already transmitted before
cancer appears. Sexually-transmitted HR-HPV typically reaches sexual
partners before malignant progression, so **cervical cancer is
evolutionarily invisible to HPV fitness**.

Several consequences:

1. **HPV has not been selected for reduced oncogenicity** over the
   time scales relevant to its human host-switching. Cancer is a
   post-transmission side-effect.
2. **HPV 16 and 18 are not obviously "losing" vs more benign HR types**
   because no selective disadvantage exists for causing cancer.
3. **Prophylactic vaccination applies novel selection pressure** —
   Gardasil prevents new infections of covered types. This is the
   first major selection pressure HPV has ever faced from humans.

## The Gardasil / vaccine era

**Vaccination timeline:**
- Gardasil 4 (HPV-6, 11, 16, 18) — licensed ~2006
- Cervarix (HPV-16, 18) — licensed ~2007
- Gardasil 9 (6, 11, 16, 18, 31, 33, 45, 52, 58) — licensed 2014

Gardasil 9 covers types responsible for approximately 90% of cervical
cancer, 90%+ of genital warts, plus substantial fractions of anal and
oropharyngeal cancer.

**The selection pressure question:** if HPV-16/18 are suppressed by
vaccination, will other HR types (31, 33, 45, etc. — also covered by
Gardasil 9) fill the niche? Will types NOT covered by Gardasil 9
(HPV-35, 39, 51, 56, 59, 68) emerge as relative-frequency winners?

**Evidence so far (as of ~2023):**
- Vaccine-type prevalence has dropped sharply in vaccinated
  populations (multiple countries; reports vary on magnitude but
  directionally consistent)
- **Type replacement is observable but modest** — non-vaccine HR types
  have risen slightly in relative frequency but not in absolute
  frequency large enough to offset the Gardasil-covered drop
- **Net HR-HPV burden has declined** in vaccinated populations
- Cross-protection (vaccine-induced immunity against related but
  non-covered types) contributes to the net decline

**Long-term prediction:**
- Decades-to-centuries scale: full HR-HPV spectrum could eventually
  reconstitute from non-vaccine types if vaccination coverage is not
  maintained or expanded
- Current trajectory: if coverage continues, HR-HPV disease burden
  should continue declining for the foreseeable future
- Evolution of vaccine-escape variants is possible but slow (DNA
  viruses mutate slowly; integration further reduces replication-
  generation turnover)

**This is the only case on the persistent-organism list where a
deployed vaccine is actively applying evolutionary pressure at
scale.** The next decades will be instructive.

## Host genetic modifiers

Strong host-side determinants of HPV outcomes:

- **HLA haplotypes** — specific HLA-DR and HLA-DQ alleles influence
  clearance probability; HLA-DRB1*13:01 and similar alleles associated
  with clearance; others (HLA-DQB1*03) associated with persistence
- **Smoking** — major environmental cofactor for progression to cancer
- **Immune suppression** (HIV, transplant, pregnancy-associated) —
  markedly increases progression rates
- **Vaginal microbiome** — *Lactobacillus crispatus*-dominant
  communities protective vs dysbiotic communities (gut-axis cross-link
  to dysbiosis framework)

## Predictions from attempt_001 framework

1. **Transmission-mode clustering:** HPV is skin/mucosal contact — low
   intensity, long duration — fits persistent-virus profile. ✓
2. **Larger genome:** 8 kb is SMALL by persistent-virus standards. HPV
   achieves persistence via lifecycle-differentiation coupling rather
   than encoded latency machinery. This is a partial exception —
   persistence is achieved with a minimal genome via clever spatial
   strategy. ◐ partial exception
3. **Species-specificity:** strict — the strongest of any virus on
   the list. ✓✓
4. **Low mutation rate during persistence:** yes — episomal form
   replicates once per host-cell-cycle; integration further reduces
   turnover. ✓
5. **Ancient DNA recovery:** HPV aDNA has been recovered from
   archaeological specimens, consistent with DNA-virus durability. ✓
6. **Vaccination prevents but doesn't cure:** strongly verified. ✓

**HPV fits the framework well except on genome-size prediction.** The
exception is interesting — it shows that persistence doesn't require
large coded machinery if lifecycle coupling can substitute.

## Open questions specific to HPV

1. **Will type replacement eventually offset Gardasil 9 coverage?**
   The current "modest type replacement" signal could evolve. Long-term
   surveillance data is needed.
2. **Can therapeutic HPV vaccines clear established persistence?**
   Multiple candidates in development (INO-3112, VB10.16, PRGN-2009).
   Early-stage trials are suggestive for CIN2/3; clearance of
   established cancer is harder.
3. **What host genetic factors gate clearance vs persistence?**
   HLA + polygenic risk is partially characterized; not complete.
4. **Will climate change or population movement shift HPV type
   geographic distributions?** HPV-18 has higher prevalence in some
   African populations; HPV-16 dominates in others. Movement of
   populations over decades could redistribute.
5. **Can vaginal microbiome manipulation reduce HR-HPV persistence?**
   Early evidence suggests *Lactobacillus*-based interventions might
   accelerate clearance. Proof-of-concept trials are in early phase.

## Links to existing repo work

- `medical/persistent_organisms/PROBLEM.md` — HPV row includes this
  two-phase therapeutic architecture (Gardasil prophylaxis +
  site-specific treatment)
- `medical/dysbiosis/` — vaginal microbiome connection; gut-
  vaginal axis
- No dedicated `medical/cervical_cancer/` or `medical/hpv/` directory
  exists — potential candidates if HPV-side work expands

## Key sources (verification status)

All of the following should be treated as "likely correct but
verify" until the audit loop passes through this attempt:

- zur Hausen H — Nobel Prize 2008 for discovering HR-HPV as cervical
  cancer etiology; canonical reviews
- Gardasil 9 pivotal trials — Joura EA et al., various 2015+ studies
- Zhai L, Tumban E — review of therapeutic vaccine candidates
- Doorbar J — canonical HPV biology reviews
- Bouvard V et al. — IARC monographs on HPV carcinogenicity
- Specific PMIDs, trial enrollment numbers, and vaccine efficacy
  percentages in this attempt should be verified before clinical /
  manuscript use

---

## Structural difference from attempts 002 and 003

CVB (attempt_002) achieves persistence by **mutation** (5'-UTR deletion).
EBV (attempt_003) achieves persistence by **encoded latency** (4
programs riding B-cell differentiation). HPV (attempt_004) achieves
persistence by **epithelial-differentiation compartmentalization** (no
encoded latency machinery; virus exploits the keratinocyte life cycle).

Three different solutions to "stay in the host without being cleared":

| Mechanism | Example | Genome burden |
|-----------|---------|---------------|
| Replication-defective mutant form | CVB 5'-UTR deleted | Small (7.4 kb) |
| Encoded latency machinery | EBV (172 kb) | Large |
| Lifecycle-differentiation coupling | HPV (8 kb) | Small |

The framework prediction that persistent viruses need large genomes
is only half right. Large genomes are one way to encode latency; HPV
shows that clever lifecycle coupling is another. CVB shows that
mutation can produce persistence in small genomes when the host
tissue is long-lived.

**Updated attempt_001 claim:** persistence requires either (a) coded
latency machinery (→ large genome), (b) lifecycle compartmentalization
(→ small genome, but restricted to epithelial hosts), or (c)
mutation-driven replication-defective form (→ small genome, requires
long-lived infected cells as reservoir).

---

*Filed: 2026-04-15 | biology/evolution/attempts/attempt_004*
*Companions: attempts 001–003; needs audit pass*
*Next candidates: HCMV (attempt_005), HHV-6 (attempt_006), H. pylori (attempt_007), Demodex evolution (attempt_008)*
