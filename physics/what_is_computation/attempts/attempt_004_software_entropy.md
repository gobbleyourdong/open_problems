# attempt_004 — Software Entropy: Is All Software Doomed to Abandonware?

**Date:** 2026-04-09
**Status:** Open. The conjecture has a measurable decay component (Lehman's laws, real data) and a surprising counterexample class (software that achieves "crystallization"). The interesting question is whether crystallization is rare or universal in the long run.

## The question

Does software maintainability tend monotonically to zero over time, such that every non-trivial software artifact eventually becomes abandonware? Or is there a stable state — a crystallized form that no longer requires maintenance because it has matched its niche perfectly?

Equivalently: is there a thermodynamics-shaped law for software ("software entropy always increases") or is this metaphor wrong?

## The conjecture (formal)

Let S be a software artifact. Let M(S, t) be the "maintainability" of S at time t, defined as the cost per unit of continued correct functioning. Let E(t) be the "environment" of S at time t (OS, hardware, dependencies, user expectations, regulatory requirements). Let D(S, E) be the "distance" between S's assumptions and the current environment.

**Conjecture (M → 0):** For any non-trivial software artifact S, in the absence of active maintenance, D(S, E(t)) is non-decreasing in t, and M(S, t) is non-increasing. In the limit, either:
1. M(S, t) → 0 as t → ∞ (the software becomes abandonware), OR
2. D(S, E(t)) reaches a fixed point where the environment stops drifting relative to S's assumptions (crystallization)

The conjecture is that case 1 is the generic outcome and case 2 is rare.

## The underlying argument (the pessimistic case)

1. **Environment drift.** Operating systems upgrade, compilers change, libraries update, hardware evolves, user expectations shift. Every change in the environment can break software that depended on the previous state.

2. **Dependency rot.** Every dependency in S is itself a software artifact subject to the same decay. The failure probability compounds: if S has n dependencies each with annual failure probability p, S's annual failure probability is 1 - (1-p)^n ≈ np for small p.

3. **Knowledge loss.** The people who wrote S will leave, retire, or forget. The cost of maintaining S without its authors is strictly higher than the cost with them. Documentation helps but does not fully substitute.

4. **Accidental complexity accumulation.** Each bug fix, feature addition, or workaround adds complexity that does not correspond to increased functionality (Brooks, accidental vs essential complexity). Over time, the ratio of accidental to essential complexity grows, making every subsequent change more expensive.

5. **Lehman's laws of software evolution** (empirically observed): "As a system evolves, its complexity increases unless work is done to maintain or reduce it." This is a direct statement of the entropy analogy.

Combining (1)-(5): without constant maintenance energy input, software artifacts become less functional. Maintenance energy is finite (bounded by interest and resources). When maintenance energy drops below the decay rate, the artifact drifts into unmaintainability, then abandonware.

## Counterexamples: the crystallized software

Several real software artifacts have remained functional and largely unchanged for decades. These are counterexamples to the generic conjecture:

### TeX / LaTeX
- **Age:** Knuth released TeX in 1978, declared it essentially complete in 1989. Bug fix versions use base-10 digits of pi (current version: 3.14159265...).
- **Maintainability proxy:** TeX 3.x has been maintained by a tiny team with minimal effort for 35+ years.
- **Why it works:** Knuth explicitly designed TeX to be "finished." He froze the feature set, documented the implementation, and declared bug fixes the only allowed changes. The environment (academic typesetting) has drifted, but TeX's niche has remained stable.

### SQLite
- **Age:** 2000, still actively maintained but remarkably stable.
- **Maintainability proxy:** a single primary author with a small team has maintained SQLite across 25 years and ~150B deployed instances.
- **Why it works:** deliberately conservative design, extensive test coverage, public-domain license enabling mirrors. The niche (embedded database) is stable.

### POSIX tools (awk, sed, grep, make)
- **Age:** 1970s-80s origins. Core versions still work.
- **Maintainability proxy:** minimal ongoing changes, works across decades of OS updates.
- **Why it works:** standardized interface. The POSIX standard froze the API surface, so environment changes below that level don't affect the tools above.

### Classic games with preserved source
- **Wolfenstein 3D, Doom:** id Software released source code. Ports exist for nearly every platform. The games run today, 30+ years later.
- **Why it works:** open source + cross-platform re-implementations (source ports) + finite scope (no feature creep possible because the game is "done").

## Characterizing crystallization

Looking at the counterexamples, the common features of crystallized software are:

1. **Explicit completeness.** The author declared the software done. No new features, only bug fixes. Knuth did this for TeX; SQLite has a "no new features without strong reason" policy.

2. **Standardized interface.** The software's API surface is frozen or matches a widely-adopted standard. Changes below the API don't affect the software.

3. **Small dependency footprint.** Crystallized software has few or no dependencies, or dependencies that are themselves crystallized (POSIX interface, C standard library).

4. **Cross-platform portability via re-implementation.** When the original platform disappears, the source is portable enough that ports exist.

5. **Stable niche.** The problem the software solves has not changed and is unlikely to change. Academic typesetting, embedded databases, text processing — these niches are stable.

## The refined conjecture

**Refined conjecture:** Most software artifacts drift to abandonware because they lack the five crystallization features. Crystallized software is rare but not impossible, and when it exists it violates the entropy-always-increases metaphor.

Sub-conjectures:

1. **The crystallization fraction is small:** f(crystallized) / f(all software) < 0.01 over long time scales.
2. **Crystallization requires DELIBERATE design for it:** software that crystallizes did so because its authors wanted it to. Accidental crystallization is near-zero.
3. **Modern software is LESS crystallizable than 1970s-90s software:** dependencies are heavier, APIs are less stable, the "standard" platform targets are narrower. If true, the entropy-always-increases metaphor is becoming MORE accurate, not less.

## The abandonware attractor

Even without crystallization, some abandoned software enters a "durable abandonware" state where it still runs but is no longer maintained. Emulators keep 30-year-old games running. Virtual machines run OS/2. The "running" is environment-mediated — the abandonware runs IN a preserving environment that itself is maintained.

This suggests a hierarchy: the base environment (OS, VMs, emulators) needs active maintenance, but software above it can be preserved without direct maintenance. The entropy claim shifts: "software entropy always increases UNLESS the environment actively preserves it."

## What would a proof look like

A rigorous treatment would:
1. Define M(S, t) precisely — what unit measures "maintainability"?
2. Collect empirical data on real software artifacts over 20+ year spans.
3. Fit decay curves for non-crystallized software.
4. Prove the five crystallization features are necessary (any crystallized software has all five) and near-sufficient.
5. Characterize the environment-preservation hierarchy formally.

Steps 2-3 are data analysis. Step 1 is definitional. Steps 4-5 are where the interesting structural work lives.

## Meta-observation

Software entropy is NOT thermodynamic entropy — the analogy is loose. Thermodynamic entropy is a physical quantity with conservation laws. Software "entropy" is a statistical tendency under observed conditions, not a physical law. The claim "software entropy always increases" is empirical, not axiomatic, and it has known counterexamples. The rigorous form is "without maintenance energy, software in MOST niches decays toward abandonware" — quantifying "most" is the interesting work.

## Sky bridges

- **what_is_information** (S/K bifurcation) — software is K-content with implicit environment assumptions. Decay happens when the environment diverges from the assumptions.
- **what_is_life** (autopoiesis) — crystallized software resembles biological species in a stable niche. Abandonware resembles extinction. The metaphor suggests software ecology as a frame.
- **what_is_computation** (this directory) — software is the canonical example of a computation artifact. Its lifecycle is a case study of computational-artifact dynamics.
- **digital_goods** (adjacent, attempt_003) — related but orthogonal. Digital_goods asks about VALUE; software_entropy asks about FUNCTION. A good can lose value while still functioning; software can lose function while still having (nostalgic) value.

## Numerical followups (to add to ../numerics/)

- `lehman_laws_fit.py` — fit Lehman's law #6 (continuing growth) against open-source repos
- `dependency_rot_simulation.py` — monte carlo simulation of dependency failure compounding
- `crystallization_features_audit.py` — score a sample of open-source projects on the five crystallization features and correlate with their age

## Status

Open. The pessimistic case is well-supported by Lehman's laws and real observation. The counterexamples (TeX, SQLite, POSIX) are real but rare. The refined conjecture says crystallization is rare and deliberate. The fraction and the rate are empirical questions that can be answered with data analysis, not with pure theory.
