# attempt_004 — The Aggregation Problem: Trade-offs, Weightings, and the Residual Gap

**Date:** 2026-04-10
**Status:** Phase 3 convergence. The Pareto requirement from attempt_003 is too strong — many genuine moral norms involve trade-offs. Generalizing to weighted welfare improvement reveals that the AGGREGATION PROBLEM is the true residual gap: which weighting of entities' welfare is correct? The compression account does not resolve this — it precisely LOCATES it. The remaining moral disagreement IS the aggregation disagreement, and this is the gap that becomes theorem-shaped.

## Cross-reference

- **attempt_003** — welfare games with Pareto improvement
- **lean/AggregationProblem.lean** — formalizes the aggregation lattice
- **numerics/aggregation_divergence.py** — tests where different aggregation schemes disagree

## The problem: Pareto is too strong

Attempt_003 defined welfare-relevant regularity as Pareto-improving: following the regularity makes no entity worse off and at least one better off. This is clean but it fails on a large class of core moral situations:

| Situation | Why it fails Pareto |
|-----------|-------------------|
| Trolley problem | Diverting kills one to save five — the one is worse off |
| Taxation for redistribution | Some taxpayers are worse off (less money) |
| Punishment of offenders | The offender is worse off |
| Just war | Combatants are worse off |
| Quarantine | The quarantined are worse off (liberty restricted) |
| Eminent domain | Property owner is worse off |
| Draft/conscription | The conscripted are worse off |

These are all paradigmatic moral situations where moral norms apply. A framework that can only handle Pareto cases misses them entirely. The Pareto requirement must be relaxed.

## Generalization: welfare-weighted improvement

**Definition (Welfare aggregation function).** A function W : (Entity → ℝ) → ℝ that maps welfare profiles (a welfare level for each entity) to a single aggregate welfare number. Different moral traditions correspond to different W:

| Tradition | Aggregation W | Compression |
|-----------|--------------|-------------|
| **Classical utilitarianism** | W = Σ wₑ (equal weight sum) | Maximally compressed: one operation (sum), zero parameters |
| **Weighted utilitarianism** | W = Σ αₑ wₑ | One parameter per entity (the weight αₑ) |
| **Rawlsian maximin** | W = min{wₑ} | Compressed as a single operation (min), zero parameters |
| **Prioritarianism** | W = Σ f(wₑ) where f is concave | One function parameter (f), gives extra weight to worse-off |
| **Rights-based/deontological** | W = −∞ if any rights violated, else Σ wₑ | Compressed as a constraint: one predicate (rights_violated) |
| **Threshold** | W = Σ wₑ if all wₑ ≥ threshold, else −∞ | One parameter (threshold) |

**Definition (Welfare-relevant regularity, generalized).** Given an aggregation function W, a regularity R in welfare game G is W-welfare-relevant if:
- There exist action profiles a, a' with a satisfying R and a' violating R
- W(welfare(a)) > W(welfare(a'))
- That is: following R improves aggregate welfare under W

**Key observation.** Pareto improvement is the special case where ALL aggregation functions agree (if no entity is worse off and one is better off, every reasonable W increases). Trade-off cases are where aggregation functions DISAGREE.

## The aggregation problem IS the residual gap

The moral disagreements that the compression account has not resolved — trolley dilemmas, the limits of redistribution, punishment theory, just war theory — are EXACTLY the cases where different aggregation functions disagree.

**Theorem-shaped claim:** For any set of moral norms N, define:
- **Pareto core:** norms where all reasonable aggregation functions agree
- **Aggregation frontier:** norms where different aggregation functions disagree

Then:
1. The Pareto core corresponds to norms with NEAR-UNIVERSAL cross-cultural agreement
2. The aggregation frontier corresponds to norms with HIGH cross-cultural disagreement
3. The disagreement at the frontier is STRUCTURED: it clusters by aggregation family

This is a precise, testable prediction that the numerics should verify.

## Which aggregation is "correct"?

The compression account's answer: **this is not a question that has a unique answer, and recognizing this is a contribution, not a failure.**

Different aggregation functions are different compressions of the welfare landscape. Each is optimal under different assumptions about the structure of the moral domain:

- **Utilitarianism** is compression-optimal when entities are interchangeable (no morally relevant differences between them)
- **Rawlsian maximin** is compression-optimal when the worst-off entity's welfare dominates the moral landscape (extreme inequality is the primary regularity to track)
- **Rights-based** is compression-optimal when certain welfare thresholds are lexicographically prior (violating them produces catastrophic outcomes that dominate all other considerations)
- **Prioritarianism** is compression-optimal when welfare has diminishing marginal moral weight (helping the worst-off produces more welfare-improvement per unit of intervention)

The compression account does not pick one aggregation function as "the" correct one. It says:
1. Within each aggregation family, compression predicts moral salience (confirmed for the Pareto core)
2. Between aggregation families, the choice depends on which structural assumptions about the moral domain are correct
3. The structural assumptions are empirically contestable (how unequal is welfare? Are there lexicographic thresholds?)
4. Therefore the aggregation disagreement is a factual disagreement about the structure of the welfare landscape, not a metaphysical disagreement about the nature of morality

**This is moral realism that is honest about its limits.** The moral facts (welfare regularities) are real. The compression of them into norms is real. But the optimal aggregation depends on empirical features of the welfare landscape that are contested.

## The trolley problem, precisely

The trolley problem is the canonical case where aggregation functions disagree:

- **Utilitarian:** Divert the trolley (5 lives > 1 life under equal-weight sum)
- **Deontological/rights-based:** Don't divert (the one person's right not to be killed as a means is lexicographically prior)

Under the compression account:
- Both positions are tracking real welfare regularities
- The disagreement is about which aggregation function correctly compresses the relevant welfare landscape
- The utilitarian assumes entities are interchangeable → sum is the right compression
- The deontologist assumes rights violations are catastrophic → constraint is the right compression
- The empirical question is: in the actual welfare landscape, do rights violations produce catastrophic downstream effects that outweigh the local welfare gain? If yes, the deontological compression is more accurate. If no, the utilitarian compression is.

**This is progress.** The trolley problem stops being a metaphysical dilemma about the nature of morality and becomes an empirical question about the structure of welfare cascades. Do rights violations really cascade? The compression account says: check.

## Predictions

**P10 (new, falsifiable).** Moral agreement should cluster in the Pareto core and disagreement should cluster at the aggregation frontier. Specifically:
- Norms where all aggregation functions agree (Pareto-improving) → cross-cultural agreement > 80%
- Norms where aggregation functions disagree (trade-off cases) → cross-cultural agreement 40-60%
- The PATTERN of disagreement at the frontier should cluster by aggregation family (cultures that agree on one trade-off should agree on others that use the same aggregation)

**P11 (new, falsifiable).** Within each aggregation family, compression still predicts moral salience. The backbone correlation (r ≈ +0.6 to +0.8) should hold within-family, even though between-family comparisons show disagreement.

**P12 (new, testable against literature).** Expertise in a moral domain should shift aggregation preferences toward the aggregation function that best compresses the domain's welfare structure. Medical ethicists should lean utilitarian (because medicine is about maximizing welfare across interchangeable patients). Criminal justice experts should lean rights-based (because criminal justice welfare landscapes have sharp thresholds). Environmental ethicists should lean prioritarian (because environmental welfare has extreme inequality between present and future).

## The gap, fully mapped

After four attempts, the gap in what_is_good has the following shape:

```
                    ┌─────────────────────────────────┐
                    │  WELFARE-RELEVANT REGULARITIES   │
                    │  (real, game-theoretically precise)│
                    └──────────────┬──────────────────┘
                                   │
                    ┌──────────────┴──────────────────┐
                    │                                   │
            ┌───────▼────────┐              ┌──────────▼──────────┐
            │  PARETO CORE   │              │ AGGREGATION FRONTIER │
            │  (all W agree) │              │  (W's disagree)      │
            │  HIGH AGREEMENT│              │  STRUCTURED DISAGR.  │
            │  r=+0.841      │              │  ← THE GAP           │
            └────────────────┘              └─────────────────────┘
                                                      │
                                    ┌─────────────────┴──────────┐
                                    │                              │
                            ┌───────▼────────┐         ┌──────────▼──────────┐
                            │ AGGREGATION    │         │ PHENOMENAL MORAL    │
                            │ CHOICE         │         │ MOTIVATION          │
                            │ (empirical Q   │         │ (inherits mind fork)│
                            │ about welfare  │         │ R2, R4              │
                            │ landscape)     │         │                     │
                            └────────────────┘         └─────────────────────┘
```

The left branch (aggregation choice) is an empirical question about welfare structure.
The right branch (phenomenal motivation) inherits the mind fork.
Neither is a metaphysical mystery. Both are tractable.

## Status

Phase 3 convergence for what_is_good. The gap is now theorem-shaped:
- The Pareto core is handled (r=+0.841)
- The aggregation frontier is precisely located
- The aggregation disagreement is reclassified as empirical, not metaphysical
- The phenomenal residue inherits α/β/γ
- Three new predictions (P10, P11, P12) are testable
