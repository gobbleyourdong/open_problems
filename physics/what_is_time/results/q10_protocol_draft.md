# Q10 Hypothermia Protocol — Draft v0

**Purpose:** test the TemperatureSP prediction Q10 = 1.68 for the specious
present. This is the single sharpest falsifier for the Kramers neural-clock
claim (Level 3 of the causal chain in FINAL_ANSWER.md). If Q10 ∉ [1.4, 2.0],
the Kramers mechanism is excluded and the chain's Level 3 fails.

This draft is a research-planning document, not an IRB submission. It
identifies what is measurable, what is impractical, and where the lowest-cost
falsifier lives.

## The prediction in measurable form

From `results/sp_temperature_testable.md`:

- SP(310K) = 2.56 s (baseline)
- SP(306K) = 3.18 s (+24% at 33°C)
- SP(315K) = 1.97 s (−23% at 42°C)
- Q10 (per 10 K) = 1.68–1.77

What to measure: **temporal order judgment (TOJ) threshold**, operationalized
as the minimum SOA (stimulus onset asynchrony) at which a subject correctly
orders two brief stimuli at 75% accuracy. TOJ threshold scales inversely
with B (the K-bandwidth), hence proportional to SP. A 24% SP increase at
33°C predicts a 24% TOJ-threshold increase.

## Three routes to data, ranked by feasibility

### Route A (highest leverage, lowest cost): meta-analysis of existing TOJ + body-temperature studies

The psychophysics literature contains TOJ and simultaneity judgment data
across body-temperature manipulations: fever cohorts, therapeutic
hypothermia post-cardiac-arrest (TTM-33 vs TTM-36 trials), cold-water
immersion studies, circadian-cycle data with core temp tracked. A
meta-analysis regressing TOJ threshold on body core temperature across
these studies gives a Q10 estimate with CI **without new data collection**.

Target: identify 10+ studies with paired TOJ/SJ data and core body temp.
Extract {T_core, TOJ_threshold, sample_size}. Fit TOJ = TOJ₀ · exp(−ΔE/kT)
on log scale. Report Q10 with 95% CI. If [1.4, 2.0] ∌ CI: Kramers excluded.

Effort: ~20 hours literature search + stats. No IRB.

### Route B (cleanest, moderate cost): fever observational study

Fever is a naturally occurring 2–4 K temperature excursion with minimal
confounds if subjects are healthy-otherwise and tested at baseline +
peak. Within-subject design eliminates inter-subject variance.

Design: n = 20 healthy adults, recruited during seasonal flu/cold outbreak
(Oct–Mar). Each subject completes TOJ battery (2 visual, 2 auditory,
2 audiovisual conditions, adaptive staircase, ~20 min total) at baseline
and again at peak fever (T_core > 38.5°C). Core temp measured
tympanically.

Primary analysis: paired t-test on log(TOJ threshold) vs log(T_core). Q10
estimated from the slope. Power analysis: at expected 23% effect and
measured within-subject TOJ variance σ² ≈ 0.05 (log-scale, from
psychophysics literature), n=20 gives >90% power at α=0.05.

Effort: IRB (~3 months), recruitment (~6 months during fever season),
data collection + analysis (~3 months). Low risk, standard psychophysics
equipment.

### Route C (gold standard, highest cost): therapeutic hypothermia collaboration

Collaborate with a targeted-temperature-management ICU program. Patients
undergoing TTM-33 (post-cardiac-arrest or neonatal HIE) are cooled to
33°C for 24h then rewarmed. The window for conscious TOJ testing is
narrow (sedation confounds), but the pre-sedation + post-rewarming
time points give a within-subject comparison at 37°C vs a thermoneutral
control.

Ethical complication: patients are critically ill; cognitive testing is
not routine in this population. Better framing: TOJ measured as part of a
standard cognitive recovery battery post-rewarming vs. 24h later, with
core temp monitored throughout rewarming. The rewarming from 33→37°C
produces the clean single-subject Q10 curve we want.

Effort: 12–18 months for collaboration + ethics + recruitment. Requires
a clinical co-investigator.

## Recommendation

**Do Route A first.** It's the fastest falsifier and costs no new data
collection. If the meta-analytic Q10 CI excludes [1.4, 2.0], the Kramers
mechanism is already falsified and Routes B/C are moot. If Q10 CI falls
inside [1.4, 2.0], Route B is the confirmatory study.

## What this protocol does not establish

- The Q10 prediction is for SP, not for cognitive speed generally. Many
  temperature-sensitive cognitive measures have Q10 = 2–4 (enzymatic
  kinetics dominate). The TOJ/SJ measurement is specifically chosen
  because it depends most directly on the K-bandwidth B; other cognitive
  tasks mix multiple temperature-sensitive processes.
- Falsification of Q10 = 1.68 falsifies the **neural-Kramers** claim at
  Level 3 of the causal chain. It does not touch Levels 1–2 (entropy
  arrow, Lyapunov irreversibility) which are thermodynamically independent,
  or Levels 4–5 (compression, Page-Wootters).

## Primary references to collect for Route A

- Targeted Temperature Management (TTM) trials: TTM (Nielsen 2013, NEJM),
  HYPERION (Lascarrou 2019), HACA (Bernard 2002) — search for TOJ or SJ
  outcomes in neurocognitive follow-up batteries.
- Fever/sepsis cognition studies with temporal tasks (Ely et al., ICU
  delirium literature).
- Diurnal temperature variation × time perception (Aschoff, Wittmann &
  Lehnhoff 2005, Campbell-Sills on CBT).
- Cold-water immersion and time perception (few studies; Nakamura et al.).

## Tag

Protocol draft v0. Three data routes ranked. Recommend meta-analysis
first (20h, no new data). This doc is a placeholder for a proper
methods writeup once Route A returns a preliminary estimate.
