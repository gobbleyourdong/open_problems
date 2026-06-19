# gap.md — Alpha-Gal Syndrome: mountain analysis → THE gap

> Sigma Phase 0/3 artifact. Rolling-start: written from context + spot-checked against the
> 2024–2025 literature (PMIDs in `PROBLEM.md` / `papers/REFERENCES.md`). Single-instance,
> **Tier 1** (per v9.1 replication ladder) — capture, not canon.

## The mountains (independent approaches that each see part of the gap)

**M1 — The epitope is settled.** α-gal, necessary + sufficient, proven from two directions
(cetuximab Fab + dietary meat). *This mountain is fully climbed.* It tells us WHAT the immune
system reacts to; it does not tell us why the reaction becomes IgE.

**M2 — Antigen delivery is mapped.** Tick saliva carries α-gal glycolipids/glycoproteins and
co-delivers a Th2-skewing milieu. *Climbed to the saliva; not yet to the switch.* We know the
antigen arrives with adjuvant; we don't know which salivary component is the *tolerance-breaking*
signal vs. mere bystander.

**M3 — The output phenotype is characterized.** Th2-skewed, tick-protein-specific T cells; IgE
class-switch; basophil/mast effector arm. *Climbed at the readout end.* We can see the IgE; we
cannot yet explain the *decision* to class-switch to IgE rather than maintain the lifelong
IgG/IgM anti-Gal tolerance state.

**M4 — Delayed kinetics has a model.** Lipid-bound α-gal → digestion/chylomicron lag → 2–6 h.
*Partially climbed (plausible, unproven).* A clean mechanism here would also explain cofactor
dependence (alcohol, exercise, NSAIDs lowering the reaction threshold).

**M5 — Susceptibility is patterned but unexplained.** Not everyone bitten sensitizes; **blood
group B/AB correlates with lower risk** (non-B/AB ~5× more likely diagnosed — Ann Allergy 2024,
S1081120624000747 ✅; mechanism: B antigen = α-gal minus a fucose → B/AB tolerance lowers
anti-α-gal IgE) — though a military cohort found this non-significant (JACI 2022, ✅ counter); atopy
and bite burden also matter. *Barely climbed.* The host-side filter on who converts is open. This
directly feeds sub-hypothesis #3 (anti-Gal repertoire diversion): if B/AB tolerance lowers the IgE
ceiling, the pre-existing anti-Gal repertoire IS load-bearing for the switch.

## THE GAP (where the mountains converge)

> **The molecular trigger — in tick saliva and host context — that breaks pre-existing α-gal
> tolerance and routes the anti-α-gal B-cell response to IgE class-switch instead of the
> homeostatic IgG/IgM.**

Every mountain stops at the same cliff: we have the antigen (M1), the delivery vehicle (M2), and
the pathogenic output (M3), but **not the causal step between a normal anti-Gal IgG/IgM repertoire
and a pathogenic α-gal-IgE one.** M4 and M5 are downstream/host-side faces of the same cliff
(kinetics and susceptibility are governed by whatever that switch is).

**Why this is THE gap (the unlock test):** solve it and the downstream questions fall out —
- **Predict** who will sensitize after a bite (M5) → targeted surveillance/avoidance.
- **Design** a tolerizing or switch-blocking intervention (the only current "treatment" is
  lifelong avoidance + epinephrine).
- **Explain** cofactor-gated, delayed reactions (M4) mechanistically.
- **Generalize** to the broader question the CVB campaign also circles from the other side:
  *what converts a tolerated antigen into an IgE/autoimmune target?* (cross-pollination note —
  **not** shared etiology).

## Candidate sub-hypotheses to attack (Phase 1/2 seeds — all 🔴 unproven)

1. **Salivary adjuvant identity.** Which saliva component (prostaglandin E2, specific
   lipids/glycolipids, a protein immunomodulator) is the IgE-switch driver vs. bystander?
   *Falsifier:* depleting/blocking the candidate in a model abolishes IgE-switch while α-gal
   delivery continues.
2. **Glycolipid (not glycoprotein) as the switch-critical carrier.** Lipid presentation
   (CD1-restricted / iNKT help) may be what biases IgE. *Falsifier:* protein-only α-gal
   delivery sensitizes equally.
3. **Anti-Gal repertoire diversion.** The pre-existing high anti-Gal IgG/IgM may seed the
   IgE switch via existing memory B cells rather than naive priming. *Falsifier:* anti-Gal-low
   individuals sensitize at the same rate/titer.
4. **Cofactor-gated absorption (M4).** Reaction threshold set by chylomicron α-gal flux, not by
   IgE titer alone. *Falsifier:* reaction severity tracks IgE titer independent of fat
   intake/alcohol/exercise.

## Next fires (if this campaign is worked)

- **Phase 1 (Odd / brute force):** glycomic + salivary-proteome literature sweep → table the
  candidate switch-drivers (M2) with evidence grade each. Land in `results/`.
- **Phase 1 (Even / theory):** formalize the tolerance-state → IgE-state transition as a
  decision the immune system makes; enumerate what signals could flip it. If a *structural*
  property emerges (e.g., "every proposed switch-driver is also present in non-sensitizing bites"),
  formalize THAT instead (v6 Phase-1 meta-analysis amendment).
- **Phase 4b content audit:** verify the Galili/GGTA1 claim (🟡 #2) and the blood-group-B
  protection claim before either becomes load-bearing.
