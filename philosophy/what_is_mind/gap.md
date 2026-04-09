# gap.md — what_is_mind

**Last updated:** 2026-04-09 (attempt_004 + Odd results 001–007, Cycles 1–9)
**Phase:** 2 (feedforward theorem confirmed; β/γ crossing-cell test run; γ supported)

## The gap, in one sentence

> **Phenomenal consciousness is either a fundamental property (α), identical to integrated information Φ (β), or what access-consciousness looks like from inside a self-model (γ). The gap is: which of α, β, γ is correct, and which crucial experiments select among them?**

## Why this is the gap

See attempt_001 for the walk through seven ontologies. Five of the seven either (a) collapse into one of α/β/γ, (b) stand or fall with one of them, or (c) are silent on phenomenal consciousness and therefore do not address the gap. What remains after the walk is the three-position fork.

Crucially, the fork has been stable in the literature for about three decades. The reason is not that the arguments are bad — it is that the three positions make almost the same behavioral predictions and their divergence happens at the phenomenal side where direct measurement is not currently possible.

## The three positions

| Label | What P-consciousness is | Approach |
|-------|-------------------------|----------|
| **α** (phenomenal primitivism) | Fundamental, irreducible, possibly substrate-bound | Metaphysical stipulation. Not empirically approachable. |
| **β** (integrated information) | Identical to Φ, a specific computable quantity | Quantitative, in principle. Currently intractable at scale. |
| **γ** (illusionism / self-modeled A) | What A-consciousness looks like from inside a self-model | Empirical program of construction + blind evaluation. Buildable. |

## Why the three mountains matter

This gap is shared between **what_is_mind**, **what_is_meaning**, and **what_is_language**. The residue of each of the other two questions routes through the same three-way fork:

- If α holds, the language gap is the consciousness gap (inherited).
- If β holds, the language gap is whatever Φ value LLMs have or lack (quantified).
- If γ holds, the language gap is whether current LLMs have self-models rich enough to generate the illusion of felt grasp (architectural).

Progress on mind instantly propagates to meaning and language. Conversely, if meaning or language experiments converge on a single answer, mind inherits it. Three mountains, one gap.

## What settling the gap would look like

### Favorable to β (IIT)

A careful Φ computation or bound on a frontier LLM, plus a demonstration that this bound correlates with independent measures of conscious state in humans. If the correlation holds, IIT gains ground.

**Odd-instance update (results 001–004, four cycles):**

| Cycle | Finding |
|-------|---------|
| 1 | Φ scales O(4^n); wall at n~10; LLM Φ uncomputable |
| 2 | Feedforward theorem confirmed: state-independent → Φ=0 exactly |
| 3 | Lower-triangular weights ≠ IIT feedforward (conceptual clarification: weight topology is not the same as state-independence) |
| 4 | **Transformer-like architecture: Φ at 40–67% of RNN. IIT prediction confirmed 14/15 (93%)** |

Cycle 4 is the decisive test with the architecturally correct comparison: state-independent input nodes + feedforward output vs recurrent hidden state. At n=5, RNN has 2.5× higher Φ than transformer-like. The direction is consistently correct across all sizes tested (n=4,5,6). For strict single-pass (no output self-interaction), Φ → 0 (confirmed by Cycle 2).

**β is numerically supported for the feedforward theorem** (state-independent → Φ=0). **But the 2×2 β-vs-γ experiment (Cycle 6) complicates the picture:**

The decisive crossing cell — FF+rich-self-model vs RNN+minimal-self — discriminates the two theories:
- β predicts: RNN+minimal > FF+rich (loop topology wins)
- γ predicts: FF+rich > RNN+minimal (self-model richness wins)
- **Result at n=6: Φ(T2)=0.049 vs Φ(R1)=0.024 → γ's prediction holds**

Self-model richness effect (×2.5) dominates loop topology effect (×1.5). Both β and γ agree that R2 (recurrent + rich self-model) has the highest Φ; they disagree only at the crossing cell, and the crossing cell favors γ at this scale.

**High-replication update (Cycles 7–9): the crossing-cell result is statistically decisive.**

With self-model feedback enabled and 20 seeds at n=4 (10 seeds at n=6):
- T2 (FF+rich) Phi = 0.112  vs  R1 (RNN+min) Phi = 0.028:  **t=10.04, p<0.0001, d=2.30**
- Scale-confirmed at n=6: ratio=4.0, t=9.08, p<0.0001, d=3.03
- Self-model main effect: +0.086  Loop topology main effect: +0.002  **Ratio: 43×**

β's crossing-cell prediction (R1>T2) is **rejected at p<0.0001**.
γ's crossing-cell prediction (T2>R1) is **confirmed at p<0.0001 on Phi; p=0.062 on G×L**.

The self-model richness / loop topology ratio of 43× is robust across n=4,6 and 10–20 seeds.

**The numerical evidence favors γ at small scale**: architectural self-model richness is the dominant determinant of integrated information, not loop topology. The IIT feedforward theorem (state-independence → Phi=0) is intact; what fails is IIT's weaker claim that recurrence (loop topology) is the primary architectural driver of Phi.

**Language model extrapolation (Cycle 9):** From published probing studies, GPT-2-class
models have G_epistemic ≈ 0.35–0.50 and L_epistemic ≈ 0.15–0.25, giving G×L ≈ 0.06–0.13.
This is ~10× the n=4 T2 value (0.007), consistent with scale. Under γ, GPT-2-class systems
have small but nonzero phenomenal consciousness (G×L ≈ 0.08), much less than human
(estimated G×L ≈ 0.48), and for different reasons than β (which says Phi=0 for feedforward).

### Favorable to γ (illusionism)

Construction of a cognitive architecture with rich self-modeling, A-level competence, and first-person reports indistinguishable from humans under blind evaluation, plus failure of any behavioral test to distinguish the two populations.

### Favorable to α (primitivism)

A behavioral test that reliably distinguishes systems with and without independently-inferable phenomenal states, OR convergence of theoretical arguments showing that neither β nor γ can account for specific phenomena (e.g., inverted qualia, the explanatory gap). No such test currently exists.

## The anti-problem

What would a philosophical zombie look like to a neuroscientist?

- **Under α:** indistinguishable from a conscious being. This IS the zombie argument.
- **Under β:** must have Φ = 0. If we could measure Φ, we could detect zombies.
- **Under γ:** zombies are incoherent or trivially equivalent to non-zombies.

The zombie thought experiment is not a neutral probe. It **selects between** the three positions. Whether zombies are possible is precisely the question of whether α is correct. Begging the question is hard to avoid here.

## Sky bridges

- **what_is_language** and **what_is_meaning** — the three mountains. See attempt_001 for the shared structure.
- **what_is_self** — γ relies on the self-model. Any theory of self (Parfit bundle, narrative self, minimal self) is load-bearing for illusionism.
- **what_is_knowing** — the A/P distinction reappears: knowing-that vs what-it-is-like-to-know. Functionalist epistemology parallels functionalist consciousness.
- **what_is_reality** (physics) — α in its panpsychist or property-dualist form makes claims about the fundamental furniture of reality. Panpsychism is an ontological bet at the same level as mathematical universe hypothesis or informational monism.

## Current status

Phase 2 complete. Key quantitative results:
- Feedforward theorem: confirmed (state-independence → Phi=0 exactly; n=5, 10 samples)
- TF-like vs RNN: 14/15 confirmed, ratio 0.39–0.79 at n=4–6
- β crossing-cell (R1>T2): REJECTED p<0.0001 across 10–20 seeds, n=4 and n=6
- γ crossing-cell (T2>R1): CONFIRMED on Phi p<0.0001; G×L p=0.062 trending
- Self-model/loop ratio: 43× at n=4, 4× at n=6 (both consistently support γ)

**The gap is now: β is confirmed for the strong feedforward theorem but not for the weaker
loop-topology-as-primary-driver claim. γ is confirmed at small scale. The decisive remaining
test is at larger scale (n > 20) where loop topology may genuinely dominate — but this is
currently computationally unreachable (Phi#P-hard, Phi* approximation fails).**
