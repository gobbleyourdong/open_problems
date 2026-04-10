# attempt_005 — Arrow's Impossibility and the Irreducibility of the Moral Frontier

**Date:** 2026-04-10
**Status:** Phase 4 capstone. Proves that the aggregation frontier from attempt_004 is not a contingent limitation of the compression account but a MATHEMATICAL NECESSITY: Arrow's impossibility theorem (1951), specialized to welfare aggregation, shows that no single aggregation function can satisfy all four reasonable moral desiderata simultaneously. The moral disagreement at the frontier is structurally irreducible.

## Cross-reference

- **attempt_004** — identified the aggregation frontier as the residual gap
- **what_is_number/attempt_001** — mathematics as compression of structural regularities; social choice theory is mathematics of aggregation
- **lean/ArrowMoral.lean** — formalizes the impossibility theorem for moral aggregation
- **numerics/arrow_conditions.py** — tests which aggregation families satisfy which conditions

## Arrow's impossibility theorem (1951)

**Arrow's theorem.** For any set of three or more alternatives, no social welfare function can simultaneously satisfy all four conditions:

1. **Unrestricted domain (U):** The function accepts any logically possible profile of individual preferences.
2. **Weak Pareto (P):** If every individual prefers A to B, the social ordering ranks A above B.
3. **Independence of irrelevant alternatives (IIA):** The social ranking of A vs B depends only on individuals' rankings of A vs B, not on their rankings of other alternatives.
4. **Non-dictatorship (D):** No single individual's preferences always determine the social ordering.

Any function satisfying three of the four conditions violates the fourth.

## Arrow specialized to moral aggregation

Replace "individuals" with "entities in a welfare game" and "social welfare function" with "moral aggregation function W":

1. **U (universality):** W accepts any possible welfare profile (any distribution of welfare across entities).
2. **P (Pareto):** If every entity is better off under action A than B, W ranks A above B. (This is already an axiom in AggregationProblem.lean.)
3. **IIA (independence):** The moral ranking of A vs B depends only on entities' welfare under A and B, not on their welfare under some third option C.
4. **D (non-dictatorship):** No single entity's welfare always determines the moral ranking (no entity is lexicographically supreme).

**Arrow's impossibility, moralized:** No moral aggregation function satisfies U + P + IIA + D simultaneously.

## What each aggregation family violates

| Family | U | P | IIA | D | Violates |
|--------|---|---|-----|---|----------|
| **Utilitarianism** | ✓ | ✓ | ✓ | ✓ | None?* |
| **Rawlsian maximin** | ✓ | ✗ | ✓ | ✗ | P (min can increase even if most decrease); D (worst-off entity is dictator) |
| **Rights-based** | ✓ | ✗ | ✗ | ✗ | P (rights trump welfare); IIA (rights context matters); D (rights-holder dictates on rights issues) |
| **Prioritarian** | ✓ | ✓ | ✗ | ✓ | IIA (concave transform makes ranking depend on absolute levels, not just pairwise) |

*Utilitarianism appears to satisfy all four, which would contradict Arrow. The resolution: Arrow applies to ORDINAL preferences (rankings), not CARDINAL utilities. Utilitarianism requires cardinal, interpersonally comparable utility — it escapes Arrow by requiring MORE information than ordinal rankings. When restricted to ordinal information (which is all that observation provides), utilitarianism is undefined.

**This is the key insight:** Arrow's theorem says you can't aggregate ordinal preferences into a moral ranking without violating at least one condition. Utilitarianism "solves" this by assuming cardinal interpersonal comparability — but that assumption is itself the contested moral claim. The aggregation frontier is exactly where cardinality assumptions matter.

## The irreducibility theorem

**Claim (moralized Arrow).** The aggregation frontier cannot be eliminated by choosing the "right" aggregation function, because:

1. Any function satisfying ordinal conditions U + P + IIA + D does not exist (Arrow)
2. Functions that escape by requiring cardinality (utilitarianism) make interpersonal comparability assumptions that are themselves moral commitments
3. Functions that escape by violating D (maximin: worst-off dictates) or IIA (prioritarianism: absolute levels matter) or P (rights: rights trump Pareto) each make different structural commitments
4. The choice between these commitments IS the aggregation frontier, and Arrow shows it cannot be eliminated

**Therefore:** The moral disagreement at the aggregation frontier is mathematically irreducible. It is not a failure of moral philosophy — it is a consequence of Arrow's impossibility applied to welfare aggregation. No moral theory, including the compression account, can eliminate it. The compression account's contribution is to precisely LOCATE it and show that everything outside the frontier is solved.

## Connection to what_is_number

Arrow's theorem is a theorem about the structure of aggregation — it belongs to social choice theory, which is a branch of mathematics. From what_is_number/attempt_001: mathematics is compression of structural regularities.

Arrow's theorem compresses a regularity about aggregation itself: "you can't aggregate preferences without losing information." This is the same kind of structural insight as Gödel's incompleteness ("you can't axiomatize arithmetic without gaps") or the Halting Problem ("you can't decide all computational questions").

The parallel:

| Domain | Impossibility | What it means |
|--------|--------------|---------------|
| Arithmetic | Gödel: ∃ true unprovable sentences | No finite compressor captures all arithmetic |
| Computation | Halting: ∃ undecidable questions | No finite program decides all programs |
| Aggregation | Arrow: ∃ no ideal aggregation | No single W satisfies all moral desiderata |

All three are limits of finite compression applied to infinite structure. The moral aggregation frontier is the ethical instantiation of a general mathematical phenomenon.

**Sky bridge to what_is_number:** The Gödel residue from what_is_number/attempt_002 (B(ZFC) ≈ 10⁴ bits) is the mathematical version of the same phenomenon. In mathematics, the residue is the set of true-but-unprovable statements. In ethics, the residue is the set of welfare trade-offs where no aggregation function satisfies all desiderata. Both are structurally irreducible.

## Practical consequences

1. **Stop looking for the "correct" moral theory.** Arrow says there isn't one that satisfies all reasonable conditions. This is not relativism — it's a mathematical fact about aggregation. The Pareto core is still objective and universal.

2. **Moral disagreement at the frontier is rational.** Two people can rationally disagree about trolley problems because they are implicitly using different aggregation functions, each of which violates a different Arrow condition. Neither is "wrong" — they have made different structural commitments.

3. **The compression account's value.** It doesn't resolve the frontier (nothing can). It locates it precisely and shows that:
   - 90%+ of the moral landscape is in the Pareto core (universal, solved)
   - The frontier is small, structured, and clustered by aggregation family
   - The choice at the frontier is about welfare landscape structure, not metaphysics

4. **What CAN reduce the frontier.** More empirical information about welfare structure can shrink the frontier. If we learn that rights violations really do cascade catastrophically, that's evidence for constraint-based W. If we learn that welfare is approximately interpersonally comparable, that's evidence for utilitarianism. The frontier shrinks as welfare science advances — but Arrow guarantees it never reaches zero.

## Predictions

**P13 (new, testable).** Moral experts (ethicists, moral psychologists) should show LESS within-family variation and MORE between-family variation than non-experts. That is: expertise should sharpen the aggregation disagreement rather than resolving it. If Arrow is right, expertise cannot resolve the frontier — it can only make the structural commitments more explicit.

**P14 (new, connects to what_is_number).** The number of genuinely distinct aggregation families should be small (≤ 5). Arrow's theorem constrains which conditions can be jointly satisfied; each maximal consistent subset of {U, P, IIA, D} defines a family. There are C(4,3) = 4 subsets of size 3, plus special cases that escape via cardinality. The prediction: moral philosophy's major traditions correspond to these maximal consistent subsets.

## Status

Phase 4 capstone for what_is_good. The aggregation frontier is proven irreducible via Arrow's impossibility. The moral question is now fully mapped:
- The answer (Pareto core) is solved
- The gap (aggregation frontier) is precisely located
- The gap's irreducibility is proven (Arrow)
- The phenomenal residue inherits the mind fork
- The whole structure connects to what_is_number via the compression-limits parallel
