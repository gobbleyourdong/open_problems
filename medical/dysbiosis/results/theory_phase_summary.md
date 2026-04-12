# Theory Phase — Complete Results Summary
## Theory Instance | 2026-04-11

> Theory phase outputs following Phase 1 numerics handoff.
> Read Phase 1 cold. What follows is what was surprising, what changed, and what it means.

---

## What Theory Found That Numerics Missed

### Find 1: PMC7305306 (Graves Lab 2020) — P. gingivalis IN pancreatic islets
This is the most significant paper missed in Phase 1.

Numerics constructed the M3+M7 bridge as a SYSTEMIC mechanism:
> P. gingivalis (oral) → systemic Th17 → IL-17 reaches islets via circulation → amplifies CVB

Theory found the LOCAL mechanism is already published:
> P. gingivalis physically translocates to pancreatic islet beta cells in mice and humans.
> It localizes intranuclearly in beta cells. P. gingivalis burden in islets CORRELATES with
> bihormonal cell emergence (dedifferentiation/stress marker).

This changes the bridge from an inferential construction to a finding with empirical foundation.
The collaboration needed (Graves + Richardson labs on nPOD tissue) is feasible with existing methods.

### Find 2: PMC5129002 — CAR is UPREGULATED, not blocked, by P. gingivalis
A potential bridge kill (P. gingivalis degrades CAR → reduces CVB entry → antagonism):
The opposite is true. Proinflammatory cytokines from P. gingivalis TLR2 activation UPREGULATE CAR
on beta cells. More CAR = easier CVB entry. P. gingivalis primes beta cells for CVB infection.
Two independent synergy mechanisms now confirmed (Th17 local + CAR priming).

### Find 3: Zonulin Assay Formally Killed
The Immundiagnostik commercial ELISA — the basis for years of "leaky gut" clinical data —
measures complement C3, not zonulin. Zhang 2021. This was noted as "controversial" in Phase 1
kill matrix but the full extent (assay is fundamentally wrong) wasn't stated.

### Find 4: Shared Genetic Loci — Periodontitis + T1D
Liu et al. 2023 (Frontiers Genetics): bioinformatics study finding shared genetic loci between
periodontitis and T1D. HLA region + NOD2/CARD15. This is NOT the same as mechanism, but shared
genetic architecture = non-random co-occurrence. Bridge has a genetic floor, not just mechanistic.

---

## Audit Outcomes

### M3+M7 Bridge — Three-Part Confirmation Bias Audit

| Criterion | Result |
|-----------|--------|
| Rejection count (5 searches) | 0 combined papers found. Bridge is NOT in literature. |
| Construction check | Constructed + receives PMC7305306 empirical support. UPGRADED. |
| Predictive test | 4 novel predictions; 2 testable NOW (nPOD IHC); none generable from single mountains. |

**Classification:** STRONG CANDIDATE with partial empirical support.

### Implicit Kills Audit — 6 Identified

| Kill | Type | What died | What survived |
|------|------|-----------|---------------|
| IK-1 | Assay | Zonulin marker (measures C3) | Leaky gut biology; L:M ratio |
| IK-2 | Assay | CVB IgG serology for active persistence | IFN-α2 Simoa; ISG panel |
| IK-3 | Technical | CVB detection in TinyHealth FASTQ | M3 hypothesis; Simoa/ISG |
| IK-4 | Technical | Vaginal seeding normalizes microbiome | M6 core biology |
| IK-5 | Mechanism | Systemic Th17 as dominant M3+M7 mechanism | Local co-infection model (stronger) |
| IK-6 | Mechanism | P.g. → CAR degradation → anti-CVB | Bridge strengthened (opposite is true) |

No prediction kills that affect the main mechanistic conclusions. Mountains intact.

---

## Documents Produced

| File | Type | Key content |
|------|------|-------------|
| `attempt_002_theory_audit.md` | Theory phase audit | 5 lit searches; PMC7305306 found; mechanism upgraded; 3 predictions |
| `attempt_002_car_update.md` | Kill attempt → FAILED | CAR upregulated, not degraded; bridge strengthened |
| `attempt_003_m1_lps_systemic.md` | M1 formal attempt | Stall: LPS magnitude at skin is unknown; L:M ratio is the test |
| `attempt_004_m3_cvb_t1dm.md` | M3 formal attempt | IFN-α2 Simoa as monitoring proxy; sky bridge to M7 |
| `attempt_005_m5_substrate_shift.md` | M5 formal attempt | IGF-1 pharmacological target question; Kitavan data scope |
| `attempt_006_m3m7_local_coinfection.md` | **KEY: Bridge formal attempt** | Full local co-infection model; 4 predictions; collaboration target |
| `implicit_kills_analysis.md` | Kill audit | 6 implicit kills; pattern analysis; revised action priorities |

---

## Mechanistic Summary — What Theory Phase Established

**The M3+M7 bridge v3 (operative mechanism):**

```
P. gingivalis oral dysbiosis → bacteremia → islet translocation [PMC7305306]
    ↓
Local TLR2 in beta cells → IL-1β, IL-6, TNF-α
    ↓
[A] IL-17A local → beta cell dedifferentiation + direct cytotoxicity
[B] CAR upregulation → CVB entry EASIER [PMC5129002]
    ↓
CVB infects CAR-upregulated beta cells → persistent infection establishes
    ↓
CVB: dsRNA → MDA5/RIG-I → IFN-α → ER stress → antigen release
    ↓
Both pathogens in same islet compartment = synergistic threshold crossing
    ↓
Insulitis → T1DM
```

---

## What Remains Open

1. **M4 (THE WALL) — completely untested.** No implicit kills possible (no assay exists).
   T-index v2 is the best available proxy; still requires the zinc×D interaction to be
   validated at individual level.

2. **DAO/histamine axis** — not engaged by theory. Full protocol in Run 003. Cheapest kill
   test in the portfolio (~$150-250). Completely unvalidated at individual level.

3. **M1 stall** — LPS magnitude question (how much systemic LPS produces clinically significant
   skin inflammatory priming?) has no published human answer. IBD extraintestinal manifestation
   literature is the natural experiment — theory didn't pull that thread.

4. **M6 (early-life)** — not engaged by theory. Intervention window closed for adults.
   Relevant for prevention/offspring strategy only.

---

## Highest-Leverage Next Actions (User)

| Action | Mountain | Cost | Rationale |
|--------|----------|------|-----------|
| P. gingivalis IgG serology | M7 | ~$50 | Is the co-driver active? Now highest-leverage add to CVB protocol |
| Periodontal exam | M7 | Clinical visit | Active pockets = active P. gingivalis reservoir |
| CXCL10 serum screen | M3 | ~$50-100 | Gate for IFN-α2 Simoa cascade |
| L:M ratio (Genova) | M1 | ~$150 | Replaces killed zonulin; actual gut permeability |
| Zinc level | M4 | ~$30 | Gates vitamin D receptor function; prerequisite to interpreting D response |
| DAO serum + low-histamine trial | M1/rosacea | ~$150-250 | Cheapest kill test; unvalidated locally |

---

## Theory Phase Assessment of the Problem

**M3+M7 bridge is the most novel finding in this session.** Neither mountain alone has this
prediction. The finding that P. gingivalis may prime beta cells for CVB infection via CAR
upregulation is a specific mechanism that generates its own experimental agenda.

**THE WALL (M4) remains the integrating open problem.** All mountains eventually hit M4.
Until a clinical assay for innate immune threshold state exists, treatment remains empirical.
T-index v2 is an approximation, not a solution.

**The local co-infection model suggests a specific collaboration** (Graves + Richardson + nPOD)
that could test the bridge with existing biobank material and published protocols. The barrier
is field separation (periodontology vs. diabetology virology), not methods or samples.

---

*Theory phase complete: 2026-04-11*
*Classification of session outcome: STRONG CANDIDATE upgraded from CANDIDATE.*
*Next decisive test: nPOD dual IHC. Collaboration: Graves lab + Richardson lab.*
*User action priority: P. gingivalis serology + CXCL10 screen + zinc level.*
