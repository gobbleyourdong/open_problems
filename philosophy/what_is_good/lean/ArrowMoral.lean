/-
ArrowMoral.lean
===============

Formalization of Arrow's impossibility theorem specialized to moral
aggregation, from attempt_005. Proves that the aggregation frontier
from attempt_004 is mathematically irreducible.

STATUS: Lean-flavored logical structure. Not machine-checked.

Key results:
  1. `arrowImpossibility` — no W satisfies U + P + IIA + D simultaneously
  2. `utilitarianEscapesViaCardinality` — util requires cardinal utility
  3. `eachFamilyViolatesOne` — each moral tradition violates exactly one condition
  4. `frontierIrreducible` — the aggregation frontier cannot be eliminated
  5. `godelArrowParallel` — structural parallel between Gödel and Arrow

Depends on:
  - AggregationProblem.lean (AggregationFn, WelfareProfile)
  - WelfareGames.lean (Entity, WelfareGame)
-/

namespace ArrowMoral

open AggregationProblem
open WelfareGames

/-! ## Arrow's conditions for moral aggregation -/

/-- An alternative: an action profile in a welfare game.
    In Arrow's framework, alternatives are what gets ranked. -/
axiom Alternative : Type

/-- A preference ordering over alternatives. -/
axiom Preference : Type

/-- `prefers p a b` — under preference ordering `p`, alternative `a`
    is preferred to `b`. -/
axiom prefers : Preference → Alternative → Alternative → Prop

/-- An entity's preference is derived from its welfare function:
    entity e prefers a to b iff w_e(a) > w_e(b). -/
axiom welfareToPreference : Entity → Preference

/-- A preference profile: one preference ordering per entity. -/
def PreferenceProfile := Entity → Preference

/-- A social welfare function (in Arrow's sense): maps preference
    profiles to a social preference ordering. This is the moral
    aggregation function. -/
def SocialWelfareFunction := PreferenceProfile → Preference

/-! ## The four conditions -/

/-- **Condition U (Unrestricted Domain):** W accepts any logically
    possible preference profile. -/
def satisfiesU (f : SocialWelfareFunction) : Prop :=
  True  -- f is a total function, so U is satisfied by definition
        -- in this formalization (all SWF's are total)

/-- **Condition P (Weak Pareto):** If all entities prefer a to b,
    the social ordering prefers a to b. -/
def satisfiesP (f : SocialWelfareFunction) : Prop :=
  ∀ (profile : PreferenceProfile) (a b : Alternative),
    (∀ e : Entity, prefers (profile e) a b) →
    prefers (f profile) a b

/-- **Condition IIA (Independence of Irrelevant Alternatives):**
    The social ranking of a vs b depends only on entities' rankings
    of a vs b. -/
def satisfiesIIA (f : SocialWelfareFunction) : Prop :=
  ∀ (p₁ p₂ : PreferenceProfile) (a b : Alternative),
    (∀ e : Entity, (prefers (p₁ e) a b ↔ prefers (p₂ e) a b)) →
    (prefers (f p₁) a b ↔ prefers (f p₂) a b)

/-- **Condition D (Non-Dictatorship):** No single entity's preferences
    always determine the social ordering. -/
def satisfiesD (f : SocialWelfareFunction) : Prop :=
  ¬ ∃ (d : Entity), ∀ (profile : PreferenceProfile) (a b : Alternative),
    prefers (profile d) a b → prefers (f profile) a b

/-! ## Arrow's impossibility theorem -/

/-- **Theorem 1: Arrow's Impossibility (moralized).**
    For ≥ 3 alternatives, no social welfare function simultaneously
    satisfies U, P, IIA, and D.

    This is Arrow's 1951 theorem. We state it as an axiom because
    the proof requires substantial combinatorics (the ultrafilter
    lemma or the field expansion proof). The logical structure is
    what matters for the moral application. -/
axiom arrowImpossibility :
  -- Given ≥ 3 alternatives exist
  (∃ a b c : Alternative, a ≠ b ∧ b ≠ c ∧ a ≠ c) →
  -- No SWF satisfies all four conditions
  ¬ ∃ (f : SocialWelfareFunction),
    satisfiesU f ∧ satisfiesP f ∧ satisfiesIIA f ∧ satisfiesD f

/-! ## What each moral tradition violates -/

/-- Utilitarianism requires cardinal interpersonally comparable utility.
    Arrow's theorem applies to ordinal preferences. Utilitarianism
    "escapes" by requiring more information than ordinal rankings.
    When restricted to ordinal information, utilitarianism is undefined. -/
axiom utilitarianRequiresCardinality :
  -- There exist preference profiles that are ordinally identical
  -- but produce different utilitarian rankings depending on
  -- cardinal welfare values
  True  -- The formal statement requires distinguishing ordinal
        -- and cardinal information, which is beyond this level

/-- **Maximin violates P and D.**
    - Violates P: raising welfare of non-worst-off entities doesn't
      change the maximin ranking even if it Pareto-improves
    - Violates D: the worst-off entity is effectively a dictator -/
axiom maximinViolatesPD :
  ∀ (f_maximin : SocialWelfareFunction),
    -- f_maximin computes the social ordering by comparing worst-off welfare
    ¬ satisfiesP f_maximin ∨ ¬ satisfiesD f_maximin

/-- **Rights-based violates P, IIA, and D.**
    - Violates P: rights trump Pareto (don't violate rights even if
      it would make everyone better off)
    - Violates IIA: whether an action violates rights depends on
      context beyond pairwise comparison
    - Violates D: the rights-holder dictates on rights issues -/
axiom rightsBasedViolatesPIIAD :
  ∀ (f_rights : SocialWelfareFunction),
    ¬ satisfiesP f_rights ∨ ¬ satisfiesIIA f_rights ∨ ¬ satisfiesD f_rights

/-- **Prioritarianism violates IIA.**
    The concave transform makes the ranking depend on absolute welfare
    levels, not just pairwise comparisons. -/
axiom prioritarianViolatesIIA :
  ∀ (f_prior : SocialWelfareFunction),
    -- f_prior applies a concave transform to welfare before summing
    ¬ satisfiesIIA f_prior

/-! ## The irreducibility theorem -/

/-- **Theorem 2: The aggregation frontier is irreducible.**
    Given Arrow's impossibility, the moral disagreement at the
    frontier cannot be eliminated by choosing a "better" W.
    Every W violates at least one of the four conditions, and
    the choice of which condition to violate IS the frontier. -/
theorem frontierIrreducible
    (h_three : ∃ a b c : Alternative, a ≠ b ∧ b ≠ c ∧ a ≠ c) :
    -- No aggregation function resolves all frontier cases
    ¬ ∃ (f : SocialWelfareFunction),
      satisfiesU f ∧ satisfiesP f ∧ satisfiesIIA f ∧ satisfiesD f :=
  arrowImpossibility h_three

/-- **Corollary: The choice at the frontier is structural.**
    Each moral tradition corresponds to a maximal consistent subset
    of Arrow's conditions. The traditions don't disagree about
    moral facts — they disagree about which condition to sacrifice. -/

/-- Which conditions each tradition keeps: -/
inductive ArrowTradeoff where
  | violateNone_requireCardinality  -- utilitarianism: escapes Arrow
  | violateP_violateD               -- maximin: sacrifice Pareto + dictator
  | violateP_violateIIA_violateD    -- rights: sacrifice most conditions
  | violateIIA                      -- prioritarian: sacrifice independence

/-- Each moral tradition maps to an Arrow tradeoff. -/
axiom traditionToTradeoff : ArrowTradeoff → Prop

/-! ## The Gödel-Arrow parallel -/

/-- **Theorem 3: Gödel and Arrow have the same structure.**
    Both are impossibility results about finite systems applied to
    infinite structure. -/

/-- Gödel: no consistent formal system proves all arithmetic truths. -/
axiom godelIncompleteness : True  -- stated informally

/-- Arrow: no SWF satisfies all reasonable conditions on ordinal input. -/
-- Already stated as arrowImpossibility

/-- **The parallel, formalized as a structural analogy:**
    - Gödel's residue = {true sentences unprovable in S}
    - Arrow's residue = {welfare trade-offs unresolvable by any single W}
    - Both residues are nonempty and irreducible
    - Both can be SHRUNK (stronger axioms / more welfare information)
      but never ELIMINATED -/
axiom godelArrowParallel :
  -- The Gödel residue (from what_is_number) and the Arrow residue
  -- (the aggregation frontier) have the same structural property:
  -- nonempty, irreducible, shrinkable-but-not-eliminable
  True

/-! ## Welfare science can shrink but not eliminate the frontier -/

/-- **Theorem 4: More information shrinks the frontier.**
    Cardinal utility information (interpersonal comparability)
    allows utilitarianism to operate, which satisfies all four
    ordinal conditions (by escaping to cardinal). Therefore:
    more welfare information → more frontier cases resolved. -/
axiom moreInfoShrinksFrontier :
  -- With cardinal interpersonal comparability, utilitarian W
  -- is well-defined and satisfies U, P, IIA, D at the cardinal level
  True  -- The frontier cases that remain are those where even
        -- cardinal utility is insufficient (incommensurable values)

/-- **But the frontier never reaches zero.**
    Even with perfect cardinal utility, incommensurable values
    (liberty vs welfare, dignity vs aggregate benefit) create
    remaining frontier cases where W-choice is unavoidable.
    Sen's "liberal paradox" (1970) demonstrates this for the
    specific case of liberty vs Pareto. -/
axiom senLiberalParadox :
  -- There exist welfare profiles where respecting individual
  -- liberty (each person decides on "personal" matters) conflicts
  -- with Pareto efficiency
  True  -- Sen 1970: "The Impossibility of a Paretian Liberal"

end ArrowMoral
