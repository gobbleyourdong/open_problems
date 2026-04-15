# attempt_003 — Epstein-Barr Virus: Deep Coevolution, B-Cell Latency, and MS

> Per-virus deep dive. Of all the persistent human viruses, EBV has
> the strongest coevolutionary signature with hominins (and broader
> vertebrates) and the most sophisticated latency machinery. It is
> also the one virus on the persistent-organism list with
> near-universal human prevalence (~95% by adulthood) and a recently
> proven causal role in a major chronic disease (MS, Bjornevik 2022
> *Science*).

---

## Phylogenetic placement

**Family:** Herpesviridae
**Subfamily:** Gammaherpesvirinae (γ-herpesvirus)
**Genus:** Lymphocryptovirus
**Species:** Human gammaherpesvirus 4 (HHV-4 / EBV)

**The γ-herpesvirus lineage** is one of three herpesvirus subfamilies
(α-, β-, γ-). Each has a characteristic tropism:
- α-herpesviruses (HSV-1/2, VZV) — epithelial and neural latency
- β-herpesviruses (HCMV, HHV-6, HHV-7) — myeloid and lymphoid
- γ-herpesviruses (EBV, KSHV) — lymphoid, with oncogenic potential

**Coevolution with vertebrates:** the herpesvirus family is *ancient*
— estimated >400 million years coexistence with vertebrate hosts. The
three subfamilies diverged ~180–220 Ma. Herpesviruses and their hosts
have cospeciated to a remarkable degree: each mammalian species
typically carries its own herpesvirus repertoire (2–8 species),
evolving with the host.

**Coevolution with hominins:** EBV likely cospeciated with primates
for ~40 Ma. The virus's sister taxa in great apes (chimpanzee
lymphocryptovirus, gorilla lymphocryptovirus) have 80–90% genome
identity with EBV and occupy the same B-cell niche. The split of
human EBV from the chimpanzee lineage is roughly synchronous with the
hominid-hominin split.

**Strains within EBV:**
- **EBV-1 (type 1)** — dominant globally; higher transforming
  efficiency in vitro
- **EBV-2 (type 2)** — more prevalent in sub-Saharan Africa, parts of
  South America and Papua New Guinea; differs primarily in EBNA-2 and
  EBNA-3A/3B/3C genes

The two strains diverged relatively recently within hominin history —
possibly during the out-of-Africa expansion. Substitution rate is low
by RNA-virus standards but nontrivial.

## Genome architecture

- **~172 kb double-stranded linear DNA** (among the largest viral
  genomes)
- Encodes ~85 proteins plus ~40 non-coding RNAs (EBERs, BART miRNAs)
- During latency, the genome circularizes into an extrachromosomal
  **episome** maintained in host nucleus
- Replicates during the lytic cycle via the Ori-Lyt origin; during
  latency via Ori-P origin + EBNA-1 tether to host chromosomes

Large genome is characteristic of persistent viruses — the latency
machinery costs coding capacity (attempt_001 prediction 2 — holds
strongly for EBV).

## The four latency programs (Thorley-Lawson model)

EBV has evolved four distinct latency states, each with a different
gene-expression pattern, each suited to a different B-cell
differentiation stage. **This is the central elegant thing about EBV:
it doesn't just hide in B cells — it rides the normal B-cell
differentiation pathway as cover.**

### Latency III — "Growth program"

- Genes expressed: EBNA-1, 2, 3A, 3B, 3C, LP + LMP1, 2A, 2B +
  EBERs + BART
- Context: newly-infected naive B cell
- Effect: drives B-cell proliferation (mimicking antigen-driven
  activation)
- Immune visibility: high — highly antigenic; CD8+ T cells kill
  these cells readily in immunocompetent hosts
- Persists in: immunosuppressed patients (organ transplant, HIV);
  produces PTLD (post-transplant lymphoproliferative disease)

### Latency II — "Default program"

- Genes: EBNA-1, LMP1, LMP2A, LMP2B + EBERs
- Context: germinal center B cell
- Effect: mimics CD40 + BCR signaling → germinal center survival
- Immune visibility: moderate (LMPs are targetable)
- Persists in: nasopharyngeal carcinoma (epithelial setting), Hodgkin
  lymphoma

### Latency I — "Burkitt program"

- Genes: EBNA-1 only + EBERs
- Context: memory B cell
- Effect: genome maintenance only; no active driver
- Immune visibility: low (EBNA-1 has GAr repeats that block
  proteasomal processing → evades MHC-I presentation)
- Persists in: Burkitt lymphoma cells (with c-MYC translocation driving
  proliferation externally)

### Latency 0 — "True latency"

- Genes: none expressed (or just EBERs)
- Context: resting memory B cell in peripheral circulation
- Effect: complete dormancy; genome is episomal and maintained
  through cell division only when B cell divides
- Immune visibility: essentially zero — no viral proteins produced
- Persists in: the normal lifelong reservoir in every seropositive
  human

**The evolutionary genius:** latency 0 is indistinguishable from
normal memory B-cell biology. The virus uses the host's memory-B-cell
homeostasis as its survival mechanism. Memory B cells live for
decades; EBV lives with them.

When a resting memory B cell gets a BCR signal + CD40 signal (as in
any normal immune response), it can enter germinal center → plasma
cell differentiation. EBV reactivation piggybacks on this: some
memory B cells carrying EBV episomes reactivate → lytic cycle in
plasma cells → virion production → transmission via saliva. The virus
has aligned its lytic cycle with the normal plasma-cell
differentiation event.

## Transmission and shedding

- Primary route: saliva (oral secretions during kissing, sharing
  utensils, small-child mother-baby contact)
- Most primary infection happens in early childhood in low-SES
  populations (subclinical) or in adolescence in high-SES populations
  (infectious mononucleosis — the delayed-infection syndrome)
- Lifelong intermittent shedding in saliva at ~10⁴–10⁶ copies/mL
  from reactivating memory-B-cell → plasma-cell events
- Shedding happens in virtually all seropositive individuals,
  throughout life

This fits the attempt_001 framework perfectly:
- Low-frequency transmission (saliva exchange is not that frequent)
- Long host lifespan (decades of opportunity)
- Immune-tolerant niche (resting memory B cell)
- Large genome encoding the latency machinery
- Species-specific (all these traits are evolved for human B-cell
  biology)

## Disease as incidental — strong form

Lifelong persistent EBV in B cells is the norm. The diseases EBV
causes are uncommon side-effects:

| Disease | Fraction of EBV+ humans affected |
|---------|:--------------------------------:|
| Infectious mononucleosis | ~25% (of those infected post-early-childhood) |
| Hodgkin lymphoma | ~0.001% |
| Burkitt lymphoma | <0.01% (except endemic form in malarial regions) |
| Nasopharyngeal carcinoma | ~0.003% (much higher in Southeast Asia) |
| Post-transplant lymphoproliferative disease | varies with transplant type |
| Multiple sclerosis | ~0.1% |
| Chronic active EBV (CAEBV) | very rare |
| Hemophagocytic lymphohistiocytosis | very rare |

99%+ of EBV carriers never develop any of these. The virus transmits
long before any of these diseases appear. The diseases are, from an
evolutionary perspective, irrelevant to EBV fitness.

**The coevolutionary consequence:** EBV has not been selected to
"become less oncogenic" because oncogenesis is post-transmission.
Human immune systems have instead been selected to tolerate EBV
rather than clear it. Seronegativity (never infected) is
evolutionarily unusual and currently rising with improved hygiene.

## MS causation — the 2022 inflection point

**Bjornevik K, Cortese M, Healy BC, et al.** *Longitudinal analysis
reveals high prevalence of Epstein-Barr virus associated with multiple
sclerosis.* *Science* 2022 Jan 21;375(6578):296–301. PMID: 35025605.
DOI: 10.1126/science.abj8222.

- >10 million US military personnel cohort followed over 20 years
- **955 MS cases total** (earlier write-up stated 801, which refers
  to the subset with pre-onset samples analyzed)
- **Hazard ratio = 32.4 (95% CI 4.3–245.3)** for MS after EBV
  seroconversion (earlier write-up stated "35-fold" — corrected to
  32.4 per 2026-04-15 claim audit)
- **Primary-source figure: median ~5 years from estimated
  seroconversion to first MS symptoms** (the "~7.5 years to diagnosis"
  figure cited earlier appears in secondary coverage; prefer the
  5-year-to-first-symptoms primary figure)
- Only **1 of 801 MS cases with pre-onset samples** was EBV-negative
  at MS onset
- Longitudinal design controls for most confounders; the data are
  consistent with EBV as a *necessary cause* of MS

This is the cleanest causal demonstration for any persistent-virus →
chronic-disease link. It reframes MS from "multifactorial autoimmune
disease of unknown cause" to "EBV-driven B-cell–mediated autoimmune
demyelination in genetically-susceptible hosts."

**Mechanism candidates:**
- **Molecular mimicry:** Lanz 2022 *Nature* showed anti-EBNA-1
  antibodies cross-react with glial cell adhesion molecule (GlialCAM) —
  a myelin-associated protein. EBV antibody response fires on
  self-tissue.
- **B-cell biology:** chronic EBV in memory B cells → aberrant
  germinal center–like structures in CNS → ectopic lymphoid follicles
  in meninges that are seen histologically in MS
- **Autoreactive B cells:** EBV infection of autoreactive B cells
  (normally deleted) rescues them from apoptosis, allowing
  self-antigen presentation to T cells

**Therapeutic implication:** anti-CD20 therapy (rituximab,
ocrelizumab, ofatumumab) — which depletes memory B cells including
EBV-carrying ones — is highly effective for relapsing MS. This is
now understood as partly acting on the EBV reservoir. Direct
anti-EBV strategies (adoptive T-cell transfer targeting EBV
antigens; EBV-specific vaccine) are in development.

## Other EBV-associated chronic syndromes

Emerging evidence also connects EBV to:

- **Systemic lupus erythematosus** — higher seroprevalence and
  reactivation; mechanism debated
- **Rheumatoid arthritis** — EBV found in synovial B cells at higher
  frequency
- **Sjögren's syndrome** — EBV in salivary gland epithelium
- **Post-viral fatigue / ME/CFS** — EBV reactivation cited as a
  contributor in some patients; not all ME/CFS is EBV-driven
- **Chronic fatigue post-mononucleosis** — a fraction of IM patients
  develop long-term fatigue syndrome

## Why no effective EBV vaccine yet

Despite EBV being the largest chronic-disease pathogen on this list,
no licensed vaccine exists. Challenges:

1. **Which antigen(s)?** gp350 (envelope glycoprotein) is the
   dominant neutralizing target — phase 2 gp350-subunit vaccine
   (GlaxoSmithKline, ~2007) reduced IM incidence but did NOT prevent
   infection. Partial protection is complex for a virus where
   persistence establishes in days.
2. **Which program to target?** Lytic-cycle antigens (gp350, BZLF1)
   are targets during transmission; latency antigens (EBNA-1, LMPs)
   are targets during persistence. A good vaccine may need both.
3. **Which goal?** Preventing primary infection? Preventing MS?
   Preventing lymphoma? The trial endpoints differ substantially and
   imply different designs.
4. **Current trials:** Moderna mRNA EBV vaccine (mRNA-1189) in phase 1;
   NIH-led gp350-nanoparticle vaccine (also phase 1). Target
   indications range from IM prevention to MS risk reduction.

Expected timeline: efficacious EBV vaccine is possible within 10–20
years. Whether it would reduce MS incidence depends on whether
vaccination prevents infection vs merely reduces severity — and on how
early in life vaccination occurs (must precede seroconversion to
prevent establishment).

## Host-genetic modifiers

Strong human genetic determinants of EBV outcomes:

- **HLA-DR15 / HLA-DRB1*15:01** — the primary MS susceptibility allele;
  synergizes with EBV infection
- **HLA-A*02:01** — CD8+ T-cell response to EBV peptides; protective
- **X-linked lymphoproliferative disease (XLP)** — SH2D1A/SAP mutation
  → fatal EBV on primary infection; the extreme case of failed
  tolerance
- **Polygenic MS risk (~200+ loci)** — most involve immune regulation;
  synergize with EBV

HLA coevolution with EBV is observable at population level. The HLA
allele distributions differ between populations with different EBV
strain distributions and different timings of primary infection.
This is the strongest coevolutionary signature of any human virus.

## Selection pressures now

1. **Hygiene gradient.** Delayed primary infection (adolescence vs
   early childhood) → IM → higher MS risk. Modern sanitation +
   reduced sibship size has raised the average age of primary
   infection in developed countries. MS incidence is rising in
   parallel — consistent with the hygiene-delay hypothesis.
2. **Immunosuppression.** Organ transplantation (increasing in
   prevalence) → EBV lymphoproliferative disease from latency III
   reactivation. Pharmaceutical and surgical advances create novel
   EBV-vulnerable populations.
3. **HIV.** EBV lymphomas are AIDS-defining; coinfection dynamics
   will shift with continued ART progress.
4. **Future vaccination.** If mRNA-1189 works, population-scale EBV
   vaccination would be the first time EBV has faced strong
   selection pressure in modern history. Prediction: virus will
   not evolve fast enough to escape within decades.

## Predictions from attempt_001 framework — applied to EBV

1. **Clusters by transmission mode + niche:** salivary, lymphoid
   latency → same cluster as HCMV, HHV-6/7. ✓ textbook
2. **Large genome:** 172 kb — among largest viral genomes; encodes
   extensive latency machinery. ✓ strongly
3. **Species-specific:** strictly human; chimpanzee has sister
   lymphocryptovirus; no zoonotic overlap. ✓ strongly
4. **Low mutation rate during latency:** yes — episomal replication
   coupled to host cell division, no viral polymerase errors during
   host S-phase. ✓
5. **Ancient DNA:** EBV aDNA has been recovered from archaeological
   specimens. ✓
6. **Vaccination prevents but doesn't cure:** consistent with gp350
   phase 2 partial protection; therapeutic-vaccine concepts for
   established latency are aspirational. ✓

## Open questions for EBV specifically

1. **Is MS 100% EBV-caused?** Bjornevik 2022 found only 1 of 801 MS
   cases was EBV-seronegative at diagnosis — is that 1 a genuine
   exception or serology false-negative? Causation without 100%
   necessity is still causation but the picture is cleaner if EBV is
   universally necessary.
2. **Why do some EBV-infected people get MS and most don't?** HLA and
   polygenic risk explain much but not all. Is there a subset of
   strains (EBV-1 vs -2 vs regional sub-lineages) with differential
   MS-inducing potential?
3. **Can MS be prevented by EBV vaccination?** Trial design is
   challenging given decades-long latent period. mRNA-1189 won't
   answer this for 15+ years.
4. **What is the optimal anti-EBV therapy for established MS?**
   Anti-CD20 (B-cell depletion) works but is not specific to
   EBV-carriers. T-cell therapy (EBV-specific CTL) shows promise but
   is experimental.
5. **Does EBV reactivation drive disease flares?** MRI-active MS
   correlates with EBV shedding in some studies. Clarifying this
   could lead to reactivation-suppression strategies.

## Links to existing repo work

- `medical/me_cfs/` — post-viral fatigue; EBV + other candidates
- `medical/dysbiosis/results/protocol_integration.md` — does NOT
  currently address EBV (dysbiosis framework is gut + skin + pancreas
  focused; EBV is lymphoid)
- `medical/persistent_organisms/PROBLEM.md` — EBV row

The repo does not yet have a dedicated `medical/ms/` (multiple
sclerosis) directory, but should if EBV-MS research continues to
expand. Candidate for future creation by the operator.

## Key sources

- Bjornevik 2022 Science — the MS causation paper
- Lanz 2022 Nature — molecular mimicry anti-EBNA-1 vs GlialCAM
- Thorley-Lawson DA et al. 2007–ongoing — latency program framework
- Cohen JI et al. — EBV reviews at NIAID
- Longnecker R, Kieff E, Cohen JI. *Epstein-Barr virus.* Fields
  Virology chapter
- Moderna / NIH gp350 vaccine trial documents

---

*Filed: 2026-04-15 | biology/evolution/attempts/attempt_003*
*Companions: attempt_001 (framework), attempt_002 (CVB)*
*Next: attempt_004 HPV, attempt_005 HCMV, attempt_006 HHV-6, plus non-viral organisms if scope expands*
