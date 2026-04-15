# Phase 0 Re-Check — Dysbiosis after 170 Runs

> Sigma v7: "check whether the wall type discovered in Phase 3 matches the
> shape-check prediction from Phase 0. If they don't match, the mismatch
> itself is a finding worth documenting."
>
> Scope: dysbiosis framework, current state at run 170. The original Phase 0
> shape-check lives inside `../PROBLEM.md` (pre-run 1) and classified the wall
> as MECHANISTIC + TECHNOLOGICAL with behavioral contributors, standard
> sigma pipeline. This note re-runs the questionnaire against what the
> pipeline actually produced.

---

## Questionnaire at +170 Runs

### 1. Is there a known mechanism? (original: partial)

At 170 runs, mechanistic coverage is past saturation. Protocol_integration.md
self-declared FRAMEWORK STATUS: COMPLETE at run 111; runs 112–170 did not
modify the protocol nor produce kills (the kill-ritual was a novelty check,
not a falsifier — see `confirmation_bias_audit.md`). Mechanism enumeration is
no longer the bottleneck.

**Now:** known to enumeration-saturation. Not the wall.

### 2. Do effective treatments/solutions exist? (original: partial; narrow niches)

At 170 runs, a full integrated protocol exists (6250 lines, 9 modules, T-index
biomarker panel, intervention arms per mountain). The protocol has not been
executed and measured in any subject yet. "Effective" cannot be answered
without exactly that execution-measurement step.

**Now:** protocol exists on paper; effectiveness is untested. Not the wall,
but the question shape has changed from "do we know what to do" to "does
the thing we wrote down actually work."

### 3. Can the wall be crossed by producing new information or tools? (original: yes)

The wall can still be crossed by new information, but not by more mechanism
runs. The information needed is:

- IFN-α2 Simoa + I-FABP + HLA genotype measurements in the user (per decisive
  test from 2026-04-12 audit)
- Gnotobiotic or RCT data on the specific T-index panel (out of method domain —
  PROBLEM.md already flagged this as "wet-lab work the method does not do")
- Independent-instance or external-literature kill of specific mechanism
  claims (the kill-ritual did not and structurally cannot do this)

**Now:** the productive new information is measurement data on a specific
subject, not more mechanism enumeration. The loop's output surface and the
remaining gap are misaligned.

### 4. Does crossing require changes in recurring human action? (original: partial)

The protocol has arms that require: dietary change, probiotic adherence,
periodontal treatment, supplement schedule, repeat bloodwork, physician
coordination. Compliance + physician-review + re-measurement are **the
critical path** between "protocol exists" and "dysbiosis reduced in this
subject."

**Now:** yes, materially. The behavioral contribution the original Phase 0
labeled as minor is now the binding constraint, because the mechanistic
output is saturated and execution has not happened.

### 5. Who has tried to cross this wall already? (original: huge field)

At population level, the field continues. At single-subject level (the
operator as subject), the loop + operator produced the mountains, the protocol,
the biomarker panel, the decisive-test design — and then the loop continued
producing runs 112–170 instead of executing the test. That continuation is
itself a finding: without external data feedback, the loop defaults to the
behavior it can execute (generate), not the behavior that would cross the
wall (measure, revise).

---

## Classification Shift

| Phase | Wall type | Binding constraint |
|-------|-----------|--------------------|
| Pre-run 1 (PROBLEM.md) | Mechanistic + technological | What's the mechanism? |
| Run 111 (protocol "COMPLETE") | Transitioning | Is the protocol right? |
| Run 170 (now) | **Mixed, behavioral-majority** | Will the subject execute and measure? Will the measurements refute / confirm? |

The original classification was correct for its time. Between run 111 and run
170, the wall type changed and the loop did not. Runs 112–170 were attacking
the original mechanistic wall that had already fallen behind them.

This matches the sigma v7 canonical example: perioral dermatitis. "Four
mountains were climbed before Phase 3 revealed the wall was caregiver
compliance — not a missing mechanism." Dysbiosis did 170 mountains before the
wall-shape change became visible. Same pattern, longer tail.

---

## Implications

1. **Stop loop-generating mechanism runs.** The mountain map is complete (9
   mountains integrated, all cross-bridges drawn). More runs do not move the
   needle — they are Phase 2 output for a Phase 4 problem.

2. **Route to execution, not enumeration.** The binding action items are:
   - Order IFN-α2 Simoa, I-FABP, HLA genotype, Tregs flow, ferritin panel
     (the T-index v3/v4 baseline from protocol_integration.md Part 1)
   - Physician review of the protocol document
   - Schedule re-measurement interval (proposed in the protocol) and honor it
   - Record compliance honestly against the protocol arms

   These are behavioral / logistical, not computational. The method's output
   for this phase is coordination artifacts (checklists, calendar events,
   order forms), not more mechanism text.

3. **Acknowledge out-of-domain steps.** Gnotobiotic / RCT / challenge-study
   confirmation is wet-lab work. The method can design the test, predict its
   outcome, and interpret the result — but it cannot execute it. This is the
   `PROBLEM.md` Phase 0 caveat reaching its limit.

4. **Light the "stop" signal on kill-vocabulary.** The kill-ritual finding
   (separate note) is a symptom; the Phase 0 mismatch is the cause. With no
   external data feedback loop, the only kill-predicate left is "novel vs
   prior runs," which is why the word drifted. Re-wiring kill to external
   data (decisive test results, literature counterexamples from an
   independent-instance pass) closes the drift at its source.

---

## What a v9 Would Learn from This

Candidate meta-entry for the Method Domain Map: **saturation drift wall.** When
a framework's mechanistic output saturates before the subject's execution
capacity catches up, the loop keeps generating on the original wall long after
that wall has moved. Indicator: kill-verdict rate approaches 0, novelty-vs-prior
approaches the kill predicate, cross-mountain integration stops producing new
bridges, protocol document stops changing. Remedy: Phase 0 re-check on a
schedule, not on intuition.

---

*Filed: 2026-04-14 | Phase 0 re-check, +170 runs | Sigma v7 shape-check applied to its own campaign*
*Companion note: standing_wave_150_170.md (upstream); confirmation_bias_audit.md (kill-ritual finding)*
*No changes to individual run files — per v6 Maps Include Noise, they remain as historical map features*
