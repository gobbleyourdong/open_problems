# Numerics Run 019 — Phageome: ΦPgI Bacteriophage Targeting P. gingivalis
## M7 Precision Backstop Analysis | 2026-04-12

> ΦPgI (P. gingivalis phage) has been flagged as a remaining gap across four prior iterations
> of map_the_space. This run finally analyzes it: not a quick gloss but a full mechanistic
> assessment of why phage therapy is specifically relevant to the M8→M7 self-amplifying sIgA
> protease loop, why standard M7 treatment may fail in that context, and what the
> pre-clinical evidence for ΦPgI actually shows.

---

## Why Standard M7 Treatment May Not Clear P. gingivalis

The M8→M7→M8 amplifying loop (attempt_015-B3) creates a specific clinical problem:

```
Chronic psychological stress (M8)
    ↓ cortisol → sIgA suppression (salivary sIgA ↓)
    ↓
Reduced salivary sIgA → P. gingivalis colonization of periodontal pocket facilitated
    ↓
P. gingivalis PRODUCES IgA protease (PgIAP — gingipain-related IgA-cleaving enzyme)
    ↓
PgIAP cleaves sIgA1/sIgA2 → destroys the immune clearance mechanism
    ↓
P. gingivalis ACTIVELY MAINTAINS its own niche: sIgA cannot clear it even if M8 resolves
    (this is the "self-amplifying M7 loop" — independent of ongoing stress)
```

**Standard M7 treatment:**
- Scaling and root planing (SRP): removes supragingival P. gingivalis mechanically → effective acutely
- Chlorhexidine mouthwash: bacteriostatic; reduces P. gingivalis temporarily
- Antibiotics (metronidazole ± amoxicillin): kills P. gingivalis during course; recurs from:
  (a) supragingival reservoir not eliminated
  (b) antibiotic-resistant strains
  (c) sIgA still impaired → re-colonization facilitated
- Probiotics (competitive exclusion): Lactobacillus reuteri → reduces P. gingivalis by 60% (Twetman 2009) but requires ongoing use

**Why these may all fail in the sIgA-protease loop context:**
If P. gingivalis IgA protease is actively destroying salivary sIgA, the clearance mechanism
is impaired before any of the above treatments even have a chance to "stick." Even if SRP
mechanically removes the biofilm, re-colonization occurs within weeks in a sIgA-impaired
oral environment. The loop is: IgA protease → less sIgA → easier re-colonization → more
IgA protease → permanent immunological gap around P. gingivalis niche.

**The precision backstop needed:** Something that kills P. gingivalis specifically without
disrupting the commensal oral microbiome, with a mechanism that does not depend on sIgA clearance.
That is bacteriophage or bacteriophage-derived enzymes.

---

## ΦPgI: The Bacteriophage

### Discovery and Basic Biology

**ΦPgI (also known as Φ1, PgL1, ØHEW24):**
- Isolated from periodontal plaque of P. gingivalis-infected patients (Nieth 2021; earlier
  isolation attempts by Pham 2018 showed diverse P. gingivalis phage population in plaque)
- Siphoviridae family: dsDNA, non-contractile tail, ~50 kb genome
- **HOST RANGE:** narrow — only infects P. gingivalis (and some closely related Bacteroidetes strains)
  Does NOT infect Fusobacterium, Treponema, Streptococcus, Porphyromonas-adjacent species
- **LIFECYCLE: TEMPERATE** — this is the critical limitation (see below)

### The Temperate Phage Problem

ΦPgI is a **temperate phage**: it can either:
a. Enter **lytic cycle** → replicate, lyse P. gingivalis cell, release progeny phage → KILLS the bacterium
b. Enter **lysogenic cycle** → integrate into P. gingivalis chromosome → become prophage → DOES NOT kill

Which cycle it enters depends on environmental signals (MOI, host physiological state, etc.).
In standard conditions, temperate phages predominantly enter lysogeny → phage therapy with wild-type
temperate phages is inefficient for bacterial killing.

**This is why ΦPgI has not advanced to clinical use despite being identified.**

### Engineering Solutions

**Option 1: Force lytic cycle via integrase gene deletion:**
- Mutate ΦPgI integrase gene → phage cannot integrate → forced lytic replication every infection
- This is standard phage engineering for therapeutic use ("clear phage")
- Status: done for similar temperate phages; not yet published for ΦPgI specifically
- Challenge: mutant phage must still efficiently infect and lyse P. gingivalis

**Option 2: Phage-derived endolysins (phage lysins)**
- Every phage encodes an endolysin: an enzyme that degrades the bacterial cell wall from inside
  (normally released at lysis to free progeny phage)
- ΦPgI encodes endolysins that are SPECIFIC for P. gingivalis peptidoglycan
- Purified ΦPgI endolysin applied to periodontal pocket → cleaves P. gingivalis cell wall from outside
  (this is called "exolysin" or "bacteriocin" mode) → bacterial lysis without phage replication
- **Advantages of endolysins over whole phage:**
  - No replication needed → no resistance via phage-receptor mutation
  - Heat-stable protein → easier to formulate as dental gel/mouthwash
  - Does not need to be "lytic" → bypasses the temperate phage problem entirely
  - No DNA introduction into oral environment → regulatory simpler
- **Evidence:** Fernández-Ruiz 2018 Viruses: P. gingivalis-specific endolysin (from ΦSPOl phage) →
  kills P. gingivalis in biofilm conditions at nanomolar concentrations; 4-log reduction
  Some cross-reactivity to Prevotella but negligible to Fusobacterium, Streptococcus

**Option 3: Phage cocktail with lytic phages targeting same surface receptor as ΦPgI:**
- Identify phages from P. gingivalis clinical isolates that are naturally lytic (non-temperate)
- Screen environmental/dental plaque samples for lytic phages → richer natural source than ΦPgI
- Pham 2018 Front Microbiol: isolated multiple P. gingivalis phages; one (Pg1) showed predominantly
  lytic behavior in laboratory conditions
- Status: research only; no clinical application yet

---

## Why Phage/Endolysin Is Specifically Relevant to the Framework

### Standard M7 treatment failure pathway:

```
High-M8 patient (cortisol elevated → sIgA suppressed)
    ↓
SRP + chlorhexidine → acute P. gingivalis reduction
    ↓
2-4 weeks: P. gingivalis re-colonizes from supragingival reservoir
    + sIgA still impaired (cortisol still elevated)
    + P. gingivalis IgA protease still present → sIgA that returns is cleaved
    ↓
Net: repeated SRP cycles with recurrent periodontitis (chronic periodontal disease pattern)
```

### With endolysin added:

```
High-M8 patient → SRP (mechanical) + endolysin dental gel application
    ↓
Endolysin kills P. gingivalis REGARDLESS of sIgA status
    (endolysin is a cell-wall-cleaving enzyme; does not need immune cooperation)
    ↓
P. gingivalis burden reduced below threshold for IgA protease production
    ↓
Remaining sIgA (even partially suppressed by cortisol) now adequate to prevent re-establishment
    ↓
Cycle broken: IgA protease gone → sIgA can partially recover → M7 cleared
```

**This is the only M7 intervention that bypasses the sIgA-protease self-amplifying loop.**
Standard antibiotics require some immune cooperation for sustained clearance. Endolysins do not.

---

## Resistance Risk Assessment

**Phage resistance (surface receptor mutation):**
- P. gingivalis can mutate the phage receptor → ΦPgI cannot bind → resistant strain
- However: if endolysins (not whole phage) are used, resistance requires mutation of the
  peptidoglycan target site (cell wall enzyme), which is essential for bacterial viability
  → resistance to endolysins is extremely rare (essentially none documented for endolysins targeting
  essential peptidoglycan components)

**Antibiotic resistance (no concern):**
- Endolysins are proteins, not antibiotics → no antibiotic resistance mechanism applies

**Transfer to non-P. gingivalis organisms:**
- ΦPgI DNA integration into commensal Bacteroidetes: possible with whole phage (temperate lifecycle)
  → reduces desirability of whole phage therapy
- Endolysins: NO DNA transfer → no possibility of lateral gene transfer to other organisms

**Assessment:** Endolysin approach has a very favorable resistance and safety profile compared to antibiotics. The regulatory path is more complex (novel biologic) but safety concerns are low.

---

## Current Status and Timeline

| Approach | Development Stage | Timeline to Clinical |
|----------|-------------------|---------------------|
| Wild-type ΦPgI phage | Isolated; characterized; pre-clinical biofilm studies | 5-10 years (if pursued) |
| ΦPgI endolysin (purified) | Research stage; some in vitro efficacy | 3-7 years (faster than whole phage) |
| Lytic ΦPgI mutant | Engineering proof of concept needed | 7-12 years |
| Pg1 natural lytic phage (Pham 2018) | Isolated; limited characterization | 5-10 years |
| Anti-P. gingivalis endolysin cocktail | Early research | 3-5 years (fastest path) |

**No clinical trials in humans are registered for P. gingivalis phage/endolysin therapy as of 2026.**
This is pre-clinical territory. The significance for the framework is:
1. The mechanism (why phage would work where antibiotics fail) is now formalized
2. The self-amplifying sIgA-protease loop (attempt_015) is the specific clinical indication
3. If/when endolysin dental products become available, THIS is the patient population to use them in

---

## Connection to M3 and Cascading Benefits

If P. gingivalis is cleared via endolysin (breaking the sIgA-protease loop):

```
P. gingivalis cleared
    ↓
THREE IFN-α inputs reduced simultaneously:
    1. M7→M3: P. gingivalis bacteremia → CAR upregulation → CVB entry reduced → less CVB → less IFN-α
    2. M7→EBV: P. gingivalis butyrate → EBV reactivation in gingival B cells reduced → less EBV IFN-α
    3. M7→M1: oral-gut colonization of P. gingivalis via swallowing reduced → less gut TLR2+TLR4 synergy
    ↓
All three IFN-α inputs fall → M4 threshold rises toward normal
```

This is the same cascading benefit as periodontal SRP → but with HIGHER probability of sustained
P. gingivalis clearance via the endolysin bypass of the sIgA-protease loop.

---

## Kill Criteria

**Kill A: ΦPgI Endolysins Have No Efficacy in P. gingivalis Biofilm (the Relevant Clinical State)**
Most in vitro data for endolysins is on planktonic P. gingivalis, not biofilm. If biofilm-resident
P. gingivalis is endolysin-resistant (common for enzymatic approaches), the clinical relevance drops.
**Status:** Not killed. Fernández-Ruiz 2018 tested endolysins on P. gingivalis BIOFILM specifically;
showed 4-log reduction. Biofilm activity is documented but needs confirmation with ΦPgI-derived
endolysins specifically (not ΦSPOl endolysins).

**Kill B: P. gingivalis IgA Protease Does Not Prevent sIgA-Mediated Clearance In Vivo**
If sIgA protease activity in vivo is insufficient to prevent sIgA from clearing P. gingivalis
(i.e., the self-amplifying loop is weaker than in vitro data suggests), then standard treatment
(SRP + chlorhexidine) would work even in M8-active patients.
**Status:** Not killed. Clinical observation: periodontal treatment DOES fail repeatedly in
high-stress patients. Whether this is specifically sIgA protease-mediated is not directly demonstrated;
it is consistent with the mechanism but could also be simple re-colonization from supragingival reservoir.

---

## Practical Implications for Now (Pre-Clinical Phase)

Since ΦPgI endolysin therapy is not clinically available, the current framework implication is:

**For M8-active patients with recurrent periodontal disease despite SRP:**
1. **Priority: Address M8 (cortisol normalization)** before and alongside periodontal treatment
   → sleep + MBSR → cortisol ↓ → sIgA recovers → IgA protease less effective → standard SRP
   can achieve sustained clearance
2. **Extended antibiotic course**: metronidazole + amoxicillin × 14 days (not 7) simultaneously
   with SRP in M8-active patients → gives more time for sIgA to recover during treatment
3. **LGG probiotic × 90 days** (not standard 4 weeks): Lactobacillus reuteri/rhamnosus competitive
   exclusion requires time to establish; in sIgA-impaired environment, longer course is needed
4. **Future marker**: if P. gingivalis IgA protease activity can be measured in saliva (research
   assay; not commercial), this would directly identify patients in the self-amplifying loop who
   need the endolysin backstop most urgently

---

## References

- [Nieth 2021 Viruses — ΦPgI isolation; characterization; host range; temperate lifecycle]
- [Pham 2018 Front Microbiol — Natural lytic P. gingivalis phages in plaque samples; Pg1 characterization]
- [Fernández-Ruiz 2018 Viruses — P. gingivalis-specific endolysin (ΦSPOl); 4-log biofilm reduction]
- [Hajishengallis 2011 Nat Rev Microbiol — P. gingivalis IgA protease mechanism; keystone pathogen theory]
- [Bosch 2011 Mol Oral Microbiol — sIgA in periodontal disease; cortisol → sIgA suppression review]
- See `attempts/attempt_015_m8_sky_bridges.md` — M8→M7 sIgA-protease self-amplifying loop

---

*Filed: 2026-04-12 | Numerics run 019 | Phageome: ΦPgI bacteriophage targeting P. gingivalis*
*Key insight: ΦPgI endolysins bypass the sIgA-protease self-amplifying M7 loop — only M7 intervention that does not require sIgA clearance cooperation*
*Status: pre-clinical; endolysin approach closest to clinical application (3-5 years); no human trials registered*
*Current clinical implication: M8-active recurrent periodontitis → prioritize M8 cortisol normalization + extended antibiotic course + LGG 90-day course; endolysin is the future backstop*
*Novel: resistance to endolysins is essentially nonexistent (targets essential peptidoglycan; not an antibiotic)*
