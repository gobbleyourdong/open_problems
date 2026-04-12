# Run 002 Summary
## Numerical Instance | 2026-04-11 | Phase 1

---

## What Was Produced

Three numerical files in `numerics/`:
1. `run_002_m4_proxy_survey.md` — 8 indirect proxies for host threshold state; composite T-index constructed
2. `run_002_m3_detection_stack.md` — CVB detection sensitivity by method layer; TinyHealth FASTQ use determined
3. `run_002_gut_skin_axis_tree.md` — 6 candidate mechanisms ranked by evidence; dominant pathway identified

---

## High-Signal Outputs

### Finding 1: TinyHealth FASTQ is M1/M4 data, NOT M3 data

CVB detection from stool sequencing is essentially impossible with current consumer tools. The 5'UTR-deleted persistent form is in islets, not stool, and standard PCR/sequencing misses it even from blood. The TinyHealth FASTQ will tell us:
- F. prausnitzii and Akkermansia abundance (M4 proxies — HIGH VALUE)
- Overall gut dysbiosis state (M1 relevant)
- Butyrate pathway genes (if shotgun, not 16S)

It will NOT give CVB information. The CVB protocol runs without direct viral confirmation — which is the expected state given current technology.

**Best available CVB proxy:** IFN-α gene signature in blood PBMCs (40-60% sensitivity, indirect). This is an unexplored test for the user.

### Finding 2: The T-index — a constructed threshold proxy

No published "innate immune threshold score" exists. Constructed a composite from clinically available markers:
- Vitamin D (25-OH-D)
- Omega-3 index
- hsCRP
- F. prausnitzii + Akkermansia from TinyHealth
- Serum zinc
- Treg % (if flow lab available)

This is falsifiable as a construct: **"Does low T-index predict disease onset in high-microbial-density asymptomatic carriers?"** That study doesn't exist. It should.

### Finding 3: GALT immune education is the dominant gut-skin pathway

Of 6 candidate mechanisms, the IBD extraintestinal manifestation data is the strongest human evidence for any gut-skin pathway. When gut inflammation is present, skin manifestations emerge at 25-40% prevalence — and these are immune-mediated (pyoderma gangrenosum, psoriasis, erythema nodosum), not infectious. That pattern is most consistent with GALT T cell education pathway, not LPS tone or SCFA transport.

**Implication for user:** The user's gut inflammation (if any, unknown) could be contributing to skin threshold INDEPENDENTLY of local Malassezia/Demodex dynamics. This is an M1+M3 → M4 chain, not just M2 standalone.

### Finding 4: Histamine/DAO axis specifically relevant for rosacea flushing

Mechanism 6 (gut histamine → mast cell → flushing) is specifically implicated in the rosacea-flushing subtype. DAO (diamine oxidase) deficiency is underdiagnosed and measurable (DAO serum activity assay, some labs). Low-histamine diet trial is non-invasive. If user's rosacea is flush-predominant, this is a cheap kill test.

### Finding 5: NOD2 genetic status is cheap and permanent

23andMe or clinical WGS can detect NOD2 R702W, G908R, L1007fs — the three major IBD risk variants. Given user's T1DM + multi-site dysbiosis presentation, knowing NOD2 status would:
1. Establish constitutional threshold susceptibility component
2. Inform treatment: NOD2 WT vs heterozygous vs compound affects innate immune baseline permanently

One-time test, permanent information.

---

## Stall Prediction Update

The threshold measurement problem (M4 wall) is now numerically confirmed as circular:
1. To study the threshold, need to compare "about-to-flare" vs "tolerant" hosts
2. To identify those groups, need a threshold marker
3. The threshold marker is what we're trying to find

**The breakout:** the T-index composite (8 proxies) is the best available approximate solution. A longitudinal cohort study tracking T-index components + disease outcome in high-density asymptomatic carriers is the minimal study that could validate it.

**Prediction for theory instance:** if presented with the T-index, theory will ask "does the product of these 8 variables predict threshold state better than any single variable alone?" — that's a nonlinear interaction question that numerics should map in Run 003.

---

## Noise Logged (unresolved)

- Oral microbiome as missing mountain: STILL NOT ADDRESSED. The oral microbiome → systemic inflammation pathway (periodontal bacteria, P. gingivalis) is well established for cardiovascular disease. Relevance to this dysbiosis cluster is unknown. Flag for Run 003.
- Bacteriophage community: mentioned in Run 001 noise, not yet addressed. The gut phageome controls bacterial population dynamics. Essentially unmapped.
- Microbial metabolite transport: plasma acetate/propionate concentrations measured — moderate bioavailability. The SCFA → skin immune cell pathway needs animal model data review (Run 003).
- L:M ratio (lactulose:mannitol test): better than zonulin for gut permeability but not mapped yet. Map in Run 003.

---

## Run 003 Targets

1. **T-index component interaction mapping** — does low D + low F. prausnitzii predict worse than either alone? (Multiplicative vs additive threshold effects)
2. **Oral microbiome mountain** — is there a Mountain 7 here?
3. **Bacteriophage dynamics** — can phage therapy be a precision intervention for specific gut bacteria?
4. **L:M ratio vs zonulin** — map the gut permeability marker landscape properly
5. **Rosacea flushing → DAO/histamine kill test** — design the minimal test

---
*Run 002 complete. Space mapped further. Key outputs: TinyHealth use case clarified, T-index proxy constructed, gut-skin dominant mechanism identified, DAO axis flagged for rosacea. Run 003 targets: interaction effects + oral microbiome + phageome.*
