# attempt_002 — Coxsackievirus B: Evolution and the 5'-UTR-Deleted Persistent Form

> Per-virus deep dive following the cross-cutting framework in
> attempt_001. CVB is the best-documented case of an RNA virus whose
> *persistent* form is genetically distinct from its *acute* form —
> a rare instance where the evolutionary transition between the two
> life histories is observable in real patients.

---

## Phylogenetic placement

**Family:** Picornaviridae
**Genus:** *Enterovirus*
**Species:** Enterovirus B (EV-B)
**Members of EV-B:** 6 Coxsackievirus B serotypes (CVB1–CVB6), ~30
echoviruses, several other coxsackie A members, some enterovirus numbers

EV-B is one of four human enterovirus species (A–D). Poliovirus sits in
EV-C; most "hand-foot-mouth" enteroviruses are in EV-A (CVA16, EV-A71);
EV-D68 (pandemic respiratory disease 2014+) is EV-D.

Closest relatives: the echoviruses share capsid architecture with CVBs;
the boundary between "Coxsackievirus B" and "echovirus" is somewhat
arbitrary and based on historical serotyping rather than clean genome
phylogeny. Modern classification often treats them together.

**Primate-coevolution timescale:** picornaviruses are ancient — the
family diverged from other positive-strand RNA viruses hundreds of
millions of years ago. But individual enterovirus lineages turn over
faster. CVB serotypes as we know them are likely 1000s–10,000s of
years old in humans, with continuing evolution. There is no deep
hominin-specific coevolution signature for CVB specifically, unlike
herpesviruses.

**Zoonotic bridge:** pigs carry related swine enteroviruses (porcine
teschovirus, EV-G). CVB3 infects and replicates in pig tissue in
experimental settings. This is unusual for picornaviruses (which
often narrowly host-restrict) and keeps the door open for zoonotic
reintroduction or cross-reservoir recombination.

## Genome architecture

```
5'-UTR (~742 nt) — IRES regulating translation — [P1 capsid: VP4-VP2-VP3-VP1] — [P2: 2A-2B-2C] — [P3: 3A-3B(VPg)-3C(protease)-3D(RdRp)] — 3'-UTR — poly(A)
```

~7.4 kb, single-strand positive-sense RNA. One polyprotein translated
from an internal ribosome entry site (IRES) in the 5'-UTR, then
cleaved by viral proteases into ~12 mature proteins.

The IRES in the 5'-UTR is both a functional necessity (no 5'-cap,
cap-independent translation) and the site of the key persistence
mechanism (see below).

## Acute infection — the default

Typical CVB infection:

1. Fecal-oral transmission (also respiratory droplet in some cases)
2. Replication in intestinal epithelium
3. Primary viremia
4. Tissue tropism: pancreas (acinar + islet cells), heart
   (cardiomyocytes), skeletal muscle, CNS, pleura
5. Secondary viremia
6. Symptomatic phase — often mild or asymptomatic; in some: myocarditis,
   pericarditis, pleurodynia (Bornholm disease), aseptic meningitis,
   neonatal sepsis, hand-foot-mouth–like syndrome
7. Immune clearance — antibody-mediated (neutralizing Ig) + cell-mediated
   (CD8+ T cells against infected cells)
8. Lifelong serotype-specific immunity (but not cross-protective across
   the 6 serotypes)

Most CVB infections follow this pattern and end in days-to-weeks.
The virus is, by default, acute-and-cleared — picornaviral baseline.

## Persistent infection — the exception

A minority of CVB infections do NOT resolve. The virus continues to
replicate at very low levels in certain tissues for months to years:

- **Pancreatic islets** → chronic β-cell stress → contribution to T1DM
- **Cardiomyocytes** → chronic inflammation → dilated cardiomyopathy
- **Skeletal muscle** → post-viral myalgia → ME/CFS (suspected)

The DiViD intervention study (Krogvold 2015 *Diabetes*) detected
enteroviral protein in islets of 6/6 newly-diagnosed T1DM patients
they biopsied. Kühl 2003 (*Circulation*) found enteroviral RNA in the
hearts of DCM patients and showed IFN-β therapy cleared it with
LVEF improvement.

The key question: *is the persistent virus the same as the acute virus,
or is it genetically distinct?*

## The 5'-UTR-deleted (TD) form — Tracy group's discovery

**Chapman NM, Kim KS, Drescher KM, Oka K, Tracy S.** *5' terminal
deletions in the genome of a coxsackievirus B2 strain occurred naturally
in human heart.* Virology 2008;375:480–491.

**Kim KS, Tracy S, Tapprich W, Bailey J, Lee CK, Kim K, Barry WH,
Chapman NM.** *5'-Terminal deletions occur in coxsackievirus B3
during replication in murine hearts and cardiac myocyte cultures and
correlate with encapsidation of negative-strand viral RNA.* J Virol
2005;79:7024–7041.

**Smithee S, Tracy S, Chapman NM.** *Mutational disruption of cis-acting
replication element 2C in coxsackievirus B3 leads to 5' terminal genomic
deletions.* J Virol 2015;89:11761–11772.

The persistent form of CVB has a deletion at the 5' end of the genome
— typically 8–50 nucleotides removed from the extreme 5' terminus.
This deletion:

- **Destroys the 5' cloverleaf secondary structure** needed for
  replication
- **Does NOT destroy the IRES** (which sits downstream, ~100 nt deeper)
- Produces virus that can still be translated (IRES works) but
  replicates inefficiently (no cloverleaf = no plus-strand synthesis
  primer)
- Predominantly makes *negative-strand* RNA that is stable in cells
  but does not produce full virions
- Evades immune detection because virion production is low — minimal
  surface antigen exposure

**This is a form of picornaviral latency by mutation**: the virus
genome is still present and minimally active, but it has given up
infectivity in exchange for stability. It can re-emerge by
recombination with a full-length co-infecting enterovirus, which
restores the 5' cloverleaf.

Evolutionarily: this is a *derived* state selected within a host, not
the ancestral transmitted form. Each persistence event likely begins
with a standard acute infection that generates 5'-UTR deletions at
low frequency, and those deletion mutants get selected for by immune
pressure — the ones that replicate hardest get cleared, the slow
replicators hide.

## Why CVB specifically evolved this trick

Most picornaviruses don't persist. Why CVB?

**Candidate explanations:**

1. **Tissue tropism.** CVB goes to tissues with high cell turnover (gut
   epithelium) AND tissues with very low turnover (cardiomyocytes,
   pancreatic β-cells). The non-turnover tissues are the persistence
   reservoirs — once the virus gets in, the infected cells persist
   too, and the virus goes along for the ride.

2. **Cellular receptor ubiquity.** CVB uses CAR (coxsackievirus and
   adenovirus receptor) plus DAF (decay-accelerating factor). CAR is
   expressed on cardiomyocytes, β-cells, and other persistence-relevant
   cells. Wide host-cell tropism gives many niches where persistence
   can take hold.

3. **Innate immune modulation.** CVB-encoded proteases (2Apro, 3Cpro)
   cleave host innate immunity components (MAVS, TRIF, NEMO). Persistent
   cells may have reduced innate signaling, allowing continued
   low-level viral presence.

4. **The 5'-UTR deletion mutation is reachable.** 8–50 nt deletions at
   the genome terminus happen stochastically during replication;
   RNA-dependent RNA polymerase (RdRp, 3Dpol) errors include these
   end-deletions. If the selection environment favors persistence, the
   mutation is not rare enough to be unobservable.

## Disease as incidental (the evolutionary framing)

Per attempt_001's cross-cutting argument: CVB chronic disease
(T1DM, DCM, ME/CFS) is not under virus-side selection because the
virus has already transmitted before disease manifests.

Evidence:
- T1DM appears months to years after initial CVB exposure
- DCM can take years to decades
- Transmission is acute-phase fecal-oral, well before chronic disease
- The 5'-UTR-deleted persistent virus *doesn't* transmit (no infectious
  virions in significant numbers)

**Implication:** the chronic disease burden of CVB persistence
is evolutionarily invisible to the virus. This means:

- There is no selection pressure on CVB to reduce T1DM incidence,
  ever. It will not "evolve to be less virulent" in the clinical sense.
- A future CVB vaccine (one is in trials: PRV-101 from Provention Bio)
  would prevent acute infection and therefore prevent the persistence
  cascade. This is the only available lever.
- Targeted antivirals (fluoxetine has shown in-vitro CVB activity;
  Benkahla 2018) could clear persistent virus if delivered with
  sufficient CNS/pancreatic/cardiac penetration.

## Current selection pressures

Modern selection on CVB:

1. **Sanitation** — fecal-oral transmission is harder in
   modern-plumbing societies. Delays age of first infection.
   *Evolutionary consequence*: CVB exposure age is rising, and later
   first-infection is associated with more severe disease (paralleling
   the polio hygiene-hypothesis story).
2. **Hygiene hypothesis convergence** — the same sanitation argument
   may explain rising T1DM incidence in developed countries if
   delayed-first-exposure is more likely to cause persistence.
3. **No widespread CVB vaccination yet.** PRV-101 is in phase 1
   (complete 2022) + phase 2. If widely deployed, would apply strong
   selection pressure on CVB serotype composition.
4. **Population mobility** — global travel, continuous reseeding of
   serotypes across populations. Prevents local extinction; also
   spreads new recombinants.
5. **Agricultural pig-human interface** — swine reservoirs for related
   enteroviruses create ongoing risk of recombinant emergence.

## Predictions from the framework

Applying the 6 predictions of attempt_001:

1. **Cluster by transmission mode:** CVB is fecal-oral (acute phase) +
   no transmission during persistence → does not fit the "low-intensity
   bodily-fluid" persistent-virus profile of herpesviruses. The
   persistence is atypical for the virus's transmission mode. ✓ partial
2. **Larger genomes for persistent viruses:** CVB is only 7.4 kb, tiny.
   It persists by *mutation* (5'-UTR deletion) not by *coded latency
   machinery*. Fits the "antigenic variation + mutation" mechanism
   class (#4 in attempt_001) rather than classical latency. ✓ consistent
3. **Species-specificity:** moderate — humans primary, some swine.
   Less narrowly restricted than herpesviruses. ✓ consistent
4. **Lower mutation rate during latency:** yes — 5'-UTR-deleted form
   replicates inefficiently, fewer rounds per unit time. ✓ yes
5. **Ancient DNA availability:** CVB aDNA is harder than DNA viruses
   (RNA degrades faster); limited recovery. ✓ prediction holds
   conservatively
6. **Vaccination provides durable prevention but not cure:** PRV-101
   data support this pattern. ✓ (provisional, phase 2 data pending)

## Open questions specific to CVB

1. **What fraction of CVB infections generate persistent 5'-UTR-
   deleted forms?** Tracy group data suggests it's non-trivial but
   the exact fraction varies by tissue and host. Quantitative estimates
   from population-level studies are needed.

2. **How often does the persistent form re-emerge into replication-
   competent virus via recombination?** The 5'-UTR-deleted form is
   replication-suppressed but recombination with full-length genome
   can restore it. Frequency of this reactivation-by-recombination is
   unknown.

3. **Does vaccination against acute CVB prevent persistence?** In
   principle yes — no acute infection, no persistence cascade. In
   practice, if vaccine is incomplete (e.g., misses a serotype), could
   persistence arise from breakthrough infection?

4. **What is the host genetic basis for who persists vs who clears?**
   HLA stratification is the most-studied; other factors (TLR3
   mutations, MDA5 variants) are candidate contributors.

5. **Is ME/CFS truly CVB-driven or is it a broader enterovirus family
   effect?** Some ME/CFS literature points at enteroviruses without
   narrowing to CVB specifically. Distinguishing CVB1–6 contributions
   from broader enterovirus-B-species would sharpen the picture.

## Links to existing repo work

- `medical/t1dm/` — extensive attempts on CVB → T1DM pathway; DiViD
  data; fluoxetine antiviral rationale; FMD regeneration
- `medical/myocarditis/`, `medical/pericarditis/`, `medical/dilated_cardiomyopathy/`
  — CVB cardiac consequences
- `medical/pancreatitis/` — acute pancreatic involvement
- `medical/pleurodynia/` — Bornholm disease (muscle involvement)
- `medical/neonatal_sepsis/` — vertical / perinatal CVB
- `medical/me_cfs/` — post-viral fatigue candidate
- `medical/dysbiosis/results/protocol_integration.md` — treatment
  integration with CVB antiviral + anti-inflammatory components
- `medical/persistent_organisms/PROBLEM.md` — medical-side framework

Per organism cross-link: this directory's attempt_001 established the
evolution-side frame; this attempt_002 populates the CVB row.
attempts 003 (EBV), 004 (HPV), 005 (HCMV), 006 (HHV-6) will follow.

## Key sources

- Chapman 2008 Virology; Kim 2005 J Virol; Smithee 2015 J Virol (Tracy
  group on 5'-UTR-deleted form)
- Krogvold 2015 Diabetes (DiViD intervention study)
- Kühl 2003 Circulation (enteroviral RNA in DCM hearts)
- Benkahla 2018 (fluoxetine as CVB antiviral in cells)
- Zell 2017 Arch Virol (enterovirus taxonomy)
- Harvala 2018 J Clin Virol (CVB epidemiology)
- Stone 2021 Nature Rev Endocrinol (CVB and T1DM review)
- Hyoty 2002 Ann Med (early enterovirus + T1DM review)

---

*Filed: 2026-04-15 | biology/evolution/attempts/attempt_002*
*Depends on: attempt_001 (cross-cutting framework)*
*Companions: medical/persistent_organisms/PROBLEM.md; medical/t1dm/ + related disease directories*
