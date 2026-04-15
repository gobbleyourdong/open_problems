# attempt_006 — Human Herpesviruses 6A and 6B: Chromosomal Integration and Germline Transmission

> Per-virus deep dive. HHV-6 is the only herpesvirus (and one of very
> few human viruses of any kind) that routinely **integrates into the
> host chromosome** — including germline chromosomes that pass to
> offspring. This puts it at the boundary between virus and
> endogenous retrovirus, and makes it the most unusual entry on the
> persistent-organism list.
>
> **VERIFICATION STATUS:** generated from trained priors with
> structural claims at high confidence; specific numeric figures
> (ciHHV-6 population frequency ~1%, roseola seroprevalence by age,
> DRESS association strength) flagged for audit-loop verification.
>
> Cross-cutting: attempt_001. Companions: attempts 002–005 (CVB, EBV,
> HPV, HCMV).

---

## Phylogenetic placement

**Family:** Herpesviridae
**Subfamily:** Betaherpesvirinae (β-herpesvirus, same as HCMV and HHV-7)
**Genus:** Roseolovirus
**Species:**
- **Human betaherpesvirus 6A (HHV-6A)**
- **Human betaherpesvirus 6B (HHV-6B)**

HHV-6A and HHV-6B were originally considered variants of a single
species ("HHV-6 variant A" and "variant B"). In 2012 the
International Committee on Taxonomy of Viruses (ICTV) **reclassified
them as distinct species** based on sequence divergence (~10%),
differential tropism, and different disease profiles.

**Subfamily context:** roseoloviruses are β-herpesviruses that share
lymphoid/myeloid tropism with HCMV but use different specific cell
types. HHV-7 is a closely related third roseolovirus with its own
human disease profile (some roseola in older children, lymph node
enlargement).

**Coevolution:** like all herpesviruses, HHV-6 shows deep cospeciation
with primates — the roseolovirus lineage dates to ~180–220 Ma. The
HHV-6A/6B split within hominids is more recent.

## Genome architecture

- **~160 kb dsDNA linear genome**
- Smaller than HCMV (235 kb) but larger than HHV-7
- Encodes ~80–100 proteins
- Important structural feature: **terminal direct repeats (DRs) at
  both ends of the genome, each containing subtelomeric-like (TTAGGG)n
  repeats** — this is the mechanism enabler for chromosomal integration

The terminal repeats are the key evolutionary innovation for this
virus. They mimic host telomere sequence, which allows homologous
recombination-mediated integration at subtelomeric chromosomal
regions.

## The chromosomal integration mechanism (ciHHV-6)

**Most human herpesviruses persist as episomes** — circular
extrachromosomal DNA in the host nucleus (see EBV attempt_003).
HHV-6 is the exception: it **routinely integrates into the host
chromosome** via its subtelomeric repeats.

```
HHV-6 infects a cell
    ↓
Viral genome establishes episome (primary latency, like other herpesviruses)
    ↓
Occasionally: viral terminal (TTAGGG)n repeats recombine with host
    subtelomeric repeats
    ↓
Integration — entire viral genome becomes part of host chromosome
    near the telomere (most often 17p, 22q, 11p, 19q in reports)
    ↓
Viral genome is now vertically inherited with host chromosome
    through normal mitosis + meiosis
```

**If integration occurs in germline cells, the virus passes to
offspring as a Mendelian locus.** This produces individuals with
**chromosomally-integrated HHV-6 (ciHHV-6)** in every nucleated cell
of their body.

**Population frequency of ciHHV-6:**
- **Historical estimate ~1% globally** (Pellett 2012 Rev Med Virol,
  PMID 22052666); regional variation (Japan historically lower at
  ~0.2%)
- **Recent UK cohort data (JVirol 2025) shows higher prevalence
  ~2.5–3% in European populations** than the Pellett 2012 estimate
  — likely reflects better detection methods rather than true
  increase
- ciHHV-6B is more common than ciHHV-6A
- Detected via PCR quantitative thresholds — ciHHV-6 individuals
  consistently show one viral copy per host cell, distinguishable
  from active infection

**Implications of ciHHV-6:**

1. **Germline transmission to offspring** — Mendelian inheritance of
   a human virus. Offspring of a ciHHV-6 parent has 50% chance of
   inheriting the integrated virus.
2. **Confounds PCR-based viral load assessment** — a PCR-positive
   person may be a ciHHV-6 carrier (not replicating, just inherited)
   rather than acutely infected. Clinical interpretation requires
   caution.
3. **Can theoretically reactivate** — integrated viral genome may
   produce full virions under certain conditions ("rescue"). Reported
   in some organ transplant contexts.
4. **Fitness consequences debated** — ciHHV-6 carriers may have
   slightly elevated rates of specific conditions (angina,
   hypothyroidism reported in some studies) but causation is unclear.

**Evolutionary status:**

ciHHV-6 represents a **transitional state between exogenous virus
and endogenous provirus**. It is not a HERV (human endogenous
retrovirus) — those are retroviruses that integrated tens of
millions of years ago and have lost replicative capacity. ciHHV-6
is a DNA virus that integrated orders of magnitude more recently,
retains its full genome, and can potentially reactivate. It is the
closest example to "HERV-in-progress" we have for a DNA virus.

From the attempt_001 framework: this is **a fifth persistence
mechanism class** not covered in the original 4:

- Encoded latency (herpesvirus standard — EBV, HCMV episomal)
- Mutation-driven replication defect (CVB 5'-UTR)
- Lifecycle-differentiation coupling (HPV)
- Antigenic variation (HIV, HCV)
- **Chromosomal integration with germline transmission (HHV-6)** —
  ultimate persistence via becoming part of the host

**The updated attempt_001 claim:** persistence strategies form a
spectrum from "stay adjacent to the host" (episomal latency, low-
level replication) through "stay with the host cells" (mutation-
driven defective, lifecycle coupling) to "become the host"
(integration, germline transmission). HHV-6 is furthest along this
spectrum toward full integration.

## Primary infection and acute disease

**HHV-6B:** causes **roseola infantum** (exanthem subitum, sixth
disease) — the primary infection in infants and young children.
Classic presentation: high fever for 3–5 days, then fever breaks and
diffuse macular rash appears. Usually self-limited.

**Seroprevalence timing:**
- Near-universal by age 2–3 (primary infection in early childhood)
- Most adults are HHV-6 seropositive (~95%+)
- Horizontal transmission primarily via saliva (maternal + caregiver)

**HHV-6A:** unlike HHV-6B, HHV-6A primary infection has no clearly
defined acute syndrome. Most ciHHV-6 carriers and many adults are
seropositive for HHV-6A but the primary infection event is typically
subclinical or unrecognized.

## Latency reservoirs

- **T cells** (primary) — both CD4 and CD8 populations
- **Monocytes and macrophages** — tissue-resident latency
- **Salivary glands** — sustained low-level shedding
- **CNS** — astrocytes, oligodendrocytes (CNS-resident latency is
  unusual depth for a herpesvirus; α-herpesviruses have neural
  latency but β usually doesn't go that deep)
- **Integrated form (ciHHV-6)** — present in every cell of carriers

The CNS latency reservoir is mechanistically important for several
reported HHV-6 disease associations (below).

## Disease spectrum

Primary infection (HHV-6B): roseola in infants, usually benign.

Reactivation / secondary disease:

1. **Hematopoietic stem cell transplant recipients** — HHV-6
   reactivation is common, frequently causes limbic encephalitis
   (altered mental status, short-term memory loss, seizures), and
   can be severe. Ganciclovir / foscarnet sometimes used.
2. **Drug Reaction with Eosinophilia and Systemic Symptoms (DRESS)
   syndrome** — HHV-6 reactivation is a defining feature in a
   subset of DRESS cases. The causal relationship (does HHV-6
   reactivation cause DRESS severity, or does DRESS-drug immune
   dysregulation cause HHV-6 reactivation?) is debated.
3. **Multiple sclerosis** — HHV-6A specifically has been associated
   with MS in some studies; found in MS lesions on immunostaining;
   causal role is debated and almost certainly secondary to EBV
   (which has clear causal evidence per attempt_003 Bjornevik 2022)
4. **Chronic fatigue syndrome / ME-CFS** — HHV-6 reactivation cited
   in some patients; not uniformly supported
5. **Autoimmune thyroid disease** — some HHV-6 association data,
   uncertain causation
6. **Mesial temporal lobe epilepsy** — HHV-6B detected in resected
   temporal lobe tissue at higher rates than controls in some
   series; mechanism unclear

## HHV-6A vs HHV-6B phenotype differences

| Trait | HHV-6A | HHV-6B |
|-------|--------|--------|
| Primary disease | Less defined; often subclinical | Roseola in infants |
| Receptor | CD46 (alternative: CD134) | CD134 (TNFR-superfamily) |
| Integration frequency | Common; ciHHV-6A in ~0.2% | More common; ciHHV-6B in ~0.8% |
| CNS tropism | Stronger (implicated in MS) | Present but less pronounced |
| Cell culture | Prefers T cell lines | Prefers different T cell lines |
| Genome similarity | 90%+ with 6B | (reference) |

The ICTV split was driven by this set of consistent phenotypic
differences accumulating over two decades of research.

## Predictions from attempt_001 framework

1. **Transmission-mode + niche clustering:** salivary + chromosomal
   integration; T-cell latency. Unusual because of the integration
   mode. Partial fit. ◐
2. **Larger genome:** 160 kb — consistent with β-herpesvirus and
   the encoded-latency pattern. ✓
3. **Species-specific:** strict in humans. ✓
4. **Low mutation rate during latency:** yes — integrated form has
   no active replication; episomal latency also quiescent. ✓
5. **Ancient DNA:** aDNA recovery theoretically possible for
   integrated form (would appear as host-genome material). ? not
   clearly documented
6. **Vaccination prevents but doesn't cure:** no vaccine in
   development; not testable. N/A

HHV-6 strains the framework on prediction 1 (transmission mode) and
prediction 6 (vaccination status) because the integration mechanism
is unique and no vaccine effort is active.

## Open questions specific to HHV-6

1. **Is ciHHV-6 fitness-neutral, slightly deleterious, or
   occasionally beneficial?** The ~1% population frequency is stable,
   suggesting near-neutrality. But specific-condition associations
   (angina, hypothyroidism) hint at mild-to-moderate selection
   pressure. Resolution requires population-scale genetic-risk
   studies.
2. **Can ciHHV-6 reactivate clinically, and how often?** Reports
   exist in HSCT settings but quantitative risk is poorly defined.
3. **What fraction of "HHV-6 + disease X" studies are confounded
   by ciHHV-6?** PCR signals from ciHHV-6 carriers can mimic active
   infection. Many older HHV-6 association studies may be
   overestimating replication-competent disease contribution.
4. **Is HHV-6A a real contributor to MS beyond EBV?** With
   Bjornevik 2022 establishing EBV causation, HHV-6A's role (if any)
   is secondary and needs careful disentanglement.
5. **What drives the germline transmission rate (~0.1% per
   generation)?** If higher than expected from integration events
   at known per-generation rate, suggests positive selection of
   integrated variants; if lower, suggests negative selection.
6. **Why do β-herpesviruses (HCMV, HHV-6, HHV-7) share
   myeloid-lineage latency + broad tropism but differ so sharply in
   integration vs episomal strategy?** The HHV-6 integration
   mechanism is not clearly derived from HCMV or HHV-7 ancestry —
   it may be an innovation within the roseolovirus genus.

## Updated structural comparison (5 viruses now)

| Virus | Persistence mechanism | Genome | Tropism | Unique feature |
|-------|-----------------------|--------|---------|----------------|
| CVB | Mutation (5'-UTR del) | 7.4 kb ssRNA+ | Pancreas, heart, muscle | RNA virus with persistent form |
| EBV | Encoded latency (4 programs) | 172 kb dsDNA | B-cell | MS causation (Bjornevik 2022) |
| HPV | Lifecycle-differentiation coupling | 8 kb dsDNA | Epithelium | Gardasil selection experiment |
| HCMV | Encoded latency + counter-immunology | 235 kb dsDNA (largest) | Myeloid + broad | Strongest NK/KIR driver; Moderna vax failed 2025 |
| **HHV-6** | **Chromosomal integration with germline transmission** | **160 kb dsDNA** | **T-cell + CNS + integrated-everywhere** | **Only germline-transmitting human virus** |

**Framework updates from this attempt:**

1. **Persistence forms a spectrum** from adjacent-to-host (episomal
   latency) to become-the-host (integration with germline
   transmission). HHV-6 is the furthest along this spectrum.
2. **The five original persistence-mechanism classes in attempt_001**
   (latency, integration, chronic replication, antigenic variation,
   + life-cycle compartmentalization from attempt_004) can be
   unified under this spectrum.
3. **Germline-integrated viruses blur the virus/host boundary** —
   HERVs are the end-state of this process; ciHHV-6 is mid-process.
   The Linnaean taxonomy that treats "virus" and "host" as distinct
   becomes inadequate for these cases.

---

## Status of viral attempts (2026-04-15)

- attempt_001 — persistence-as-strategy (cross-cutting framework)
- attempt_002 — CVB (mutation-driven persistence)
- attempt_003 — EBV (encoded latency, MS causation)
- attempt_004 — HPV (lifecycle coupling, vaccine-era selection)
- attempt_005 — HCMV (largest genome, NK/KIR driver, vaccine
  failed 2025-10)
- **attempt_006 — HHV-6 (this attempt; germline integration)**

**Viral quintet for the persistent-organism framework is complete.**
Next candidates (non-viral per operator's broader scope):

- attempt_007 — *Helicobacter pylori* (gastric bacterial persistence)
- attempt_008 — *Porphyromonas gingivalis* (periodontal)
- attempt_009 — Demodex mite (arthropod coevolution with
  mammalian skin)
- attempt_010 — *Malassezia* + *Cutibacterium acnes* (sebaceous
  skin commensals)
- (composite gut dysbiosis is arguably too broad for a single
  attempt)

---

*Filed: 2026-04-15 | biology/evolution/attempts/attempt_006*
*Companions: attempts 001–005; needs audit pass on specific figures*
*Verification target: ciHHV-6 global frequency, HHV-6A vs 6B split details, DRESS-HHV-6 causal evidence strength*
