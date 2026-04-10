# attempt_003 — Welfare Games: Sharpening R1 and the Moral Emotions

**Date:** 2026-04-10
**Status:** Phase 2→3 transition. Gives a precise game-theoretic definition of "welfare-relevant interaction regularity" that is strictly more general than cooperation, strictly more specific than "any regularity," and falsifiable. Also addresses R4 (moral emotions as compression-domain signatures).

## Cross-reference

- **attempt_001** — cooperation-compression account (original claim)
- **attempt_002** — six hard objections; corrected claim → welfare-relevant expansion
- **lean/WelfareGames.lean** — formalizes the welfare game framework
- **numerics/welfare_vs_cooperation.py** — tests whether welfare-game score is a better predictor than cooperation-game score

## The problem: R1

From gap.md: *"The welfare-relevant expansion is broader but potentially less falsifiable than 'cooperation facts.' Can it be made game-theoretically precise?"*

The risk is real. "Welfare-relevant interaction regularities" could be unfalsifiably broad if it means "any regularity that anyone cares about." To be scientific, the definition must be:

1. **Strictly more general** than cooperation (covers the O1 cases that forced the expansion)
2. **Strictly more specific** than "any regularity" (excludes non-moral regularities)
3. **Falsifiable** (makes predictions that could be wrong)

## The definition: welfare games

A **welfare game** generalizes a strategic game by dropping the requirement that all entities are strategic agents:

**Definition (Strategic game).** A tuple ⟨N, (Aᵢ)ᵢ∈N, (uᵢ)ᵢ∈N⟩ where N is a set of agents, Aᵢ is agent i's action set, and uᵢ : ∏Aⱼ → ℝ is agent i's utility function. All entities in N are strategic — they choose actions to maximize their utility.

**Definition (Welfare game).** A tuple ⟨A, E, (Aₐ)ₐ∈A, (wₑ)ₑ∈E⟩ where:
- **A** is a set of agents (entities that choose actions)
- **E** is a set of entities with welfare (A ⊆ E; entities need not be agents)
- **Aₐ** is agent a's action set
- **wₑ : ∏Aₐ → ℝ** is entity e's welfare function (maps action profiles to welfare levels)

The key difference: **E can contain non-agent entities** — animals, future persons, ecosystems, anything with a welfare function. An animal has a welfare function (wₑ maps human actions to the animal's welfare) but is not in A (it does not choose strategic actions).

A **cooperation game** is a welfare game where A = E (every entity is a strategic agent). This is the special case that attempt_001 analyzed.

**Definition (Welfare-relevant regularity).** A regularity R in the space of action profiles such that:
- There exist action profiles a, a' with a satisfying R and a' violating R
- For all entities e ∈ E: wₑ(a) ≥ wₑ(a'), with strict inequality for at least one e
- That is: following R produces a weak Pareto improvement over violating R

**Definition (Moral norm).** A compressed description of a welfare-relevant regularity.

## Why this is strictly more general than cooperation

| Moral domain | Cooperation game? | Welfare game? | Why |
|-------------|-------------------|---------------|-----|
| Don't steal from neighbors | Yes (A = E = {you, neighbor}) | Yes | Both strategic agents |
| Don't torture animals | **No** (animal ∉ A) | Yes (animal ∈ E, has wₑ) | Animal has welfare but isn't strategic |
| Protect future generations | **No** (future persons ∉ A) | Yes (future persons ∈ E) | Future persons have welfare functions |
| Preserve ecosystems | **No** (ecosystem ∉ A) | Yes (ecosystem ∈ E) | Ecosystem has welfare-like function |
| Reciprocity | Yes | Yes | Standard cooperation game |

Every cooperation norm is a welfare norm (because cooperation games are welfare games with A = E). Not every welfare norm is a cooperation norm. The expansion is a strict generalization.

## Why this is strictly more specific than "any regularity"

The definition requires:
1. **Entities with welfare functions** — excludes regularities about non-welfare things (mathematical regularities, physical constants, aesthetic patterns)
2. **Pareto improvement** — excludes regularities where following the rule makes some entity worse off with no compensating improvement
3. **Action-dependence** — excludes regularities that hold regardless of what agents do (natural laws, logical truths)

**Falsifiability test.** The definition predicts that moral norms should NOT emerge for regularities that are:
- Not action-dependent (you can't have a moral norm about gravity)
- Not welfare-relevant (you can't have a moral norm about prime numbers)
- Not Pareto-improving (a "norm" that helps some but hurts others equally is not a moral norm but a political preference)

If we find strong, universal moral norms that are not welfare-relevant by this definition, the account is falsified.

## Predictions that distinguish welfare from cooperation

**P8 (new, falsifiable).** The correlation between welfare-game score and moral salience should be HIGHER than the correlation between cooperation-game score and moral salience. Specifically:
- For the O1 scenarios (animal welfare, future generations, ecosystems): welfare-game score should predict moral salience where cooperation-game score fails
- For standard cooperation scenarios: both scores should predict equally well

If r(welfare_score, moral_salience) ≤ r(cooperation_score, moral_salience), the welfare expansion is unnecessary and should be dropped (Occam's razor).

**P9 (new, falsifiable).** Moral norms about entities with welfare functions but without strategic agency (animals, future persons) should show:
- Lower cross-cultural convergence than cooperation norms (because the cooperation enforcement mechanism — reputation, punishment — is weaker)
- But positive convergence nonetheless (because the welfare regularity is real)
- The convergence should correlate with the strength of the welfare function (animals that can visibly suffer → stronger norms than animals that cannot)

If non-strategic-entity norms show ZERO convergence, the welfare expansion fails.

## R4: Moral emotions as compression-domain signatures

The second residue from gap.md: why does guilt feel different from shame, from indignation, from moral disgust?

Under the compression account, each moral emotion is the self-model's phenomenal report of a specific kind of compression failure or success in the welfare domain. The different phenomenological characters correspond to different compression domains:

| Emotion | Compression domain | What the self-model reports |
|---------|-------------------|---------------------------|
| **Guilt** | Own-action welfare impact | "My action violated a welfare-relevant regularity I track" |
| **Shame** | Self-model coherence | "My action is inconsistent with the self-model's moral commitments" |
| **Indignation** | Other-action welfare impact | "Another agent's action violated a welfare regularity I track" |
| **Moral disgust** | Purity/contamination | "An entity is in a state that violates body-integrity compression heuristics" |
| **Moral admiration** | Instance compression | "An agent's action instantiated a welfare regularity with extreme compression efficiency" |
| **Moral elevation** | Norm expansion | "I observe a compression refinement — a more universal rule being applied" |

**The claim:** Moral emotions differ because they compress different aspects of the welfare game:
- **Guilt vs indignation**: same regularity violated, different agent (self vs other)
- **Guilt vs shame**: different compression domain (welfare impact vs self-model coherence)
- **Admiration vs obligation**: same norm, different compression level (instance vs rule)
- **Moral disgust**: a heuristic compression from the body-integrity domain, evolutionarily repurposed for moral contexts (Haidt's moral foundations, purity dimension)

**Falsifiability.** The compression account predicts that moral emotions should be functionally dissociable along the domain lines above. Specifically:
- Guilt and indignation should activate overlapping neural circuits (same regularity) with different self/other attribution
- Shame should activate self-model circuits more than guilt does
- Moral disgust should activate disgust circuits (insula) — this is already confirmed (Chapman & Anderson 2013)

**What the compression account does NOT explain.** Why any of these functional states have phenomenal character at all. This inherits R2 and the mind fork. The compression account explains the STRUCTURE of moral emotions (why there are exactly these categories, how they relate) but not the EXISTENCE of moral phenomenology (which is the α/β/γ question).

## The welfare game formalism resolves three open issues

### 1. The kin selection outlier (from result_001)

Kin selection scored highest compression (1.75) but moderate moral salience (7.0). Under the welfare game framework: kin selection is a cooperation game restricted to kin (A = E = {kin}). It has high compression within its restricted entity set but low scope universality (few entities). The welfare-game score penalizes narrow entity sets, so kin selection scores lower on welfare than on cooperation — correctly predicting its moderate moral salience.

### 2. The fairness norm compression anomaly

Fairness scored highest moral salience (9.5) but moderate compression (0.80). Under welfare games: fairness norms track a welfare regularity across ALL entities (E = everyone), not just strategic agents. The welfare-game score boosts fairness because its entity set is maximal. The cooperation-game score undervalues fairness because it only counts strategic agents.

### 3. The moral progress direction (from attempt_002)

Moral progress = expanding E. Abolition expanded E from {free persons} to {all persons}. Animal rights expands E from {persons} to {sentient beings}. Each expansion is a welfare-game refinement: same compression, broader entity set, more regularities captured.

## Status

R1 is now sharpened: welfare-relevant interaction regularities have a precise game-theoretic definition that is strictly more general than cooperation, strictly more specific than "any regularity," and falsifiable via P8 and P9. R4 has a structural account (domain signatures) whose phenomenal aspect inherits the mind fork. Two new predictions (P8, P9) are testable against the existing moral scenario corpus.
