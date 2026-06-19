# Alpha-Gal Syndrome — the tolerance-break / IgE class-switch problem

> **Standalone entry. NOT part of the CVB campaign** (see `../MEDICAL_PROBLEMS.md`).
> Filed under `medical/` for tooling, but it shares no pathogen, mechanism, or thesis with
> the Coxsackievirus B network. It rhymes with the campaign only at the abstract level
> (*tolerance break → immunopathology*) — that resemblance is a cross-pollination note, not a
> claim of shared etiology.

> **VERIFICATION STATUS** (per Sigma v9.1 PMID discipline): claims below carry markers —
> ✅ spot-checked against a primary source this session · 🟡 well-established / textbook, not
> re-verified this session · 🔴 inference / hypothesis, explicitly unproven. Citations are
> real references returned by literature search 2026-06-18; full list in `papers/REFERENCES.md`.

---

## Formal statement

Alpha-gal syndrome (AGS) is an acquired IgE-mediated allergy to the oligosaccharide
**galactose-α-1,3-galactose (α-gal)**, presenting as **delayed** (2–6 h) anaphylaxis,
urticaria, angioedema, or GI symptoms after ingestion of **non-primate mammalian products**
(red meat; sometimes dairy/gelatin), and immediate reactions to α-gal-bearing drugs
(e.g. cetuximab). Sensitization is causally linked to **tick bites**.

**The problem (the wound lattice):** humans carry *pre-existing tolerance* to α-gal —
we cannot synthesize it (the GGTA1 gene is evolutionarily inactivated) and instead carry
high-titer **anti-α-gal IgG/IgM** "natural antibodies" with no pathology. A tick bite converts
this benign state into a pathogenic **IgE** response against the *same* glycan. **What molecular
event, in tick saliva and host context, breaks tolerance and routes the anti-α-gal response to
IgE class-switch instead of the normal IgG/IgM?** That conversion is the unsolved core.

---

## Known results (the foundation — Phase 1 layer)

1. **The epitope is the glycan, and it is necessary + sufficient.** ✅
   The discovery came from two independent directions converging on the *same* sugar:
   cetuximab anaphylaxis (α-gal on the Fab of the mAb heavy chain) and delayed red-meat
   anaphylaxis. IgE specific for α-gal is causal in both.
   *Chung CH et al., NEJM 2008;358(11):1109–17 (PMID 18337601).* ✅

2. **Humans are α-gal-null by evolution.** ✅ *(Phase-4b cleared 2026-06-18)*
   **GGTA1** (α-1,3-galactosyltransferase) was inactivated in ancestral catarrhines **~28 Mya**,
   as **two independent events** in apes and in Old-World monkeys after their divergence (humans
   carry a frame-shift/exon-deletion pseudogene). Humans therefore make no α-gal and instead carry
   abundant **natural anti-Gal IgG/IgM** constituting **~1% of circulating immunoglobulins**
   (some sources 1–5% of IgM+IgG), produced lifelong via continuous stimulation by gut-flora
   glycans (*Klebsiella*, *E. coli*, *Serratia*). This is the baseline *tolerance/immunity* state
   AGS perturbs. *Galili & Swanson, PNAS 1991 (PMID 1908095); Galili, Immunol Cell Biol 2005 (PMID
   16266320); Galili, anti-Gal evolution/pathophysiology review (PMID 7504839).*
   *(Note for Phase 2: anti-Gal being **E. coli**-stimulated is a stray thread back to the gut/
   E. coli microbiome work — flagged, not pursued.)*

3. **Ticks deliver α-gal in saliva.** ✅
   N-linked glycan + glycolipid analysis confirms α-gal in the saliva/salivary glands of
   *Amblyomma americanum* (lone star) and *Ixodes scapularis*. The bite co-delivers the antigen
   **plus** a Th2-skewing salivary milieu.
   *Saliva α-gal glycolipid ID, Ticks Tick Borne Dis 2024 (ScienceDirect S1877959X24000773).* ✅

4. **The response is Th2-skewed and IgE class-switched.** ✅
   T cells specific for tick proteins carry a strong Th2 signal; the bite drives type-2 immunity
   and B-cell IgE class-switch. ~80% of suspected-AGS patients report tick bites and have higher
   α-gal IgE than non-bitten controls.
   *Platts-Mills TAE et al., "The Immunology of Alpha-Gal Syndrome," Immunological Reviews 2025
   (doi:10.1111/imr.70035).* ✅

5. **The "delayed" kinetics has a leading (unproven) explanation.** 🔴/🟡
   2–6 h lag is hypothesized to reflect **lipid-bound α-gal** (glycolipids/glycoproteins)
   requiring digestion and chylomicron processing before the epitope reaches circulation —
   distinct from classic protein food allergens that react in minutes.
   *Review: "Galactose-α-1,3-Galactose: Atypical Food Allergen or Model IgE Hypersensitivity?"
   PMC6028928.* (Plausible, not definitively proven — 🔴 on causality.)

6. **Rising incidence + range tracks the vector.** ✅
   AGS is increasing and spreading with tick range; sensitization now documented from
   *I. scapularis* bites well outside the classic lone-star Southeast.
   *CDC EID 2025;31(4): AGS after I. scapularis bite, Maine 2014–2023.* ✅

---

## Phase 0 shape-check (recorded)

- **Wall type: mechanistic, with a behavioral overlay.** The core is a *missing mechanism*
  (the tolerance-break / IgE-switch trigger) → standard pipeline applies. The overlay is
  behavioral: sensitization needs repeated bites, and current management is pure avoidance —
  so a "cure" has a compliance/exposure dimension, not only a molecular one. Note it; don't let
  the behavioral overlay masquerade as the wall (cf. perioral-dermatitis cautionary case).
- **Multiple-mountains test: PASSES.** Several independent lines (cetuximab, meat, saliva
  glycomics, Th2 T-cell phenotyping, delayed-kinetics lipid model) all detect the *same* object
  — the α-gal epitope and its IgE conversion. Convergent invariants → the method fits.

## The gap

See `gap.md` for the mountain analysis and the single named gap.

## Index exposure (the motivating real-world instance)

See `results/index_exposure_2026-06.md` — household lone-star nymph bite, 2026-06-17, which is
why this problem is live rather than abstract.
