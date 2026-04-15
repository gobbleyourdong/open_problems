# Persistent Organisms — Cross-Organism Framework for Chronic Disease

## In one paragraph

A small number of persistent organisms — ~8, roughly CVB, Demodex,
*P. gingivalis*, EBV, *H. pylori*, HPV, *Malassezia* + *C. acnes*, and
composite gut dysbiosis — drive a large fraction of chronic human
disease. Each produces its own cluster of associated conditions, and
each responds to a shared two-phase therapeutic architecture: reduce
organism burden with a targeted clearance agent, then layer
anti-inflammatory management to quench the self-sustaining
inflammatory loop the organism initiated. Individual diseases are
instances of this pattern; this directory is the cross-cutting
synthesis.

## Files

- **`PROBLEM.md`** — full scope, organism table, Phase 0 shape-check,
  work plan
- **`README.md`** — this file; navigation + summary

## Quick reference — the 8 organisms

| Organism | Primary disease(s) | Clearance | Adjunct |
|----------|--------------------|-----------|---------|
| CVB | T1DM, myocarditis, DCM | Fluoxetine, NLRP3 suppressors | Colchicine, metabolic |
| Demodex | Rosacea, blepharitis, chalazion | TTO/T4O, ivermectin, lotilaner | Doxycycline 40 mg, omega-3 |
| *P. gingivalis* | Periodontitis, RA, Alzheimer's assoc | Periodontal therapy, antimicrobials | Doxycycline, systemic anti-inflammatory |
| EBV | MS, some lymphomas, CFS | Limited (valacyclovir weak) | Vitamin D, syndrome-specific |
| *H. pylori* | Gastric ulcer, gastric cancer | Triple/quadruple antibiotic | PPI, mucosal healing |
| HPV | Cervical, oral, anal cancers | Vaccination (prevention), topical lesion therapy | LEEP / conization |
| Malassezia + *C. acnes* | Seb derm, acne | Ketoconazole, benzoyl peroxide, retinoids | Zinc pyrithione |
| Gut dysbiosis | IBD, metabolic syndrome | Targeted antibiotics, FMT, diet | SCFA / butyrate, barrier repair |

## Where the disease-specific work lives

Each organism has per-disease directories in `medical/` that cover the
site-specific mechanism and protocol. Examples:

- CVB → `medical/t1dm/`, `medical/myocarditis/`, `medical/pericarditis/`, etc.
- Demodex → `medical/blepharitis/`, `medical/perioral_dermatitis/`
- Gut dysbiosis → `medical/dysbiosis/` (also the original home of the
  cross-organism synthesis)

This directory does not duplicate that work; it references it.

## Where the evolutionary work lives

`biology/evolution/` — companion top-level directory asking why these
organisms persist in humans at all, how they evolved to establish
long-term infection, and what the coevolutionary picture with human
immune genes looks like.

## The two-phase therapeutic architecture

The single most load-bearing observation across the 8:

**Phase 1 — Clearance.** Targeted agent kills / reduces organism
burden. Duration typically 2–6 weeks. Mechanism-driven; well-studied
per organism.

**Phase 2 — Adjunct (anti-inflammatory).** Addresses the
self-sustaining inflammatory loop that the organism initiated but
which now runs independently. Necessary because:
- KLK5 / LL-37 (rosacea/blepharitis) continue after Demodex clearance
- NLRP3 / IL-1β (T1DM) continues after CVB clearance
- Citrullination / anti-CCP (RA) continues after P. gingivalis
  treatment
- Similar patterns across each organism

Duration of adjunct: months. Often this is the longer, more
load-bearing phase. Skipping adjunct is why many "successful"
clearance treatments produce symptom regression.

## Status

Directory created 2026-04-15 in response to operator approval of
top-level persistent-organisms category. Content as of this commit:
PROBLEM.md + this README. Expansion per future iterations.

---

*Filed: 2026-04-15 | medical/persistent_organisms/README.md*
