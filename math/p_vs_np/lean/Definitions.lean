/-
  P vs NP — Core Definitions

  The most DIFFERENT of the Clay problems.
  About computation, not equations.
-/

/-! ## 1. Turing Machines and Time Complexity

The fundamental objects: Turing machines, languages, time bounds.
-/

/-- A language is a set of binary strings -/
def Language := Set (List Bool)

/-- A language L is in P if there exists a deterministic Turing machine
    that decides L in time O(n^k) for some constant k. -/
def InP (L : Language) : Prop := sorry -- Requires TM formalization

/-- A language L is in NP if there exists a polynomial-time verifier V
    such that: x ∈ L ⟺ ∃ certificate w, |w| ≤ p(|x|), V(x,w) accepts. -/
def InNP (L : Language) : Prop := sorry -- Requires TM formalization

/-! ## 2. The P vs NP Question -/

/-- P = NP: every language in NP is also in P -/
def P_eq_NP : Prop := ∀ L : Language, InNP L → InP L

/-- P ≠ NP: there exists a language in NP that is not in P -/
def P_ne_NP : Prop := ∃ L : Language, InNP L ∧ ¬(InP L)

/-- The Clay Millennium Problem: determine whether P_eq_NP or P_ne_NP -/
-- Note: P_eq_NP ↔ ¬P_ne_NP (assuming classical logic)

/-! ## 3. NP-Completeness

SAT is NP-complete: every NP problem reduces to SAT in polynomial time.
If SAT ∈ P then P = NP. If SAT ∉ P then P ≠ NP.
-/

/-- A language L is NP-hard if every NP language poly-reduces to L -/
def NPHard (L : Language) : Prop :=
  ∀ L' : Language, InNP L' → sorry -- ∃ poly-time reduction L' ≤_p L

/-- A language is NP-complete if it's in NP and NP-hard -/
def NPComplete (L : Language) : Prop := InNP L ∧ NPHard L

/-! ## 4. Circuit Complexity (the main attack vector)

Boolean circuits: DAGs with AND, OR, NOT gates.
Size = number of gates. Depth = longest path.

P/poly: languages decidable by polynomial-SIZE circuits (not uniform).
P ⊆ P/poly. If NP ⊄ P/poly then P ≠ NP.
-/

/-- Circuit complexity: the minimum circuit size for computing f on n-bit inputs -/
-- C(f) = min{|C| : C computes f}
-- P ≠ NP ⟺ ∃ NP language L, C(L_n) = ω(n^k) for all k

/-! ## 5. The Three Barriers

These are META-THEOREMS showing that certain proof techniques CANNOT
separate P from NP.
-/

/-- Relativization barrier: there exist oracles making P=NP and P≠NP -/
axiom relativization_barrier : True -- Baker-Gill-Solovay 1975

/-- Natural proofs barrier: if OWFs exist, no natural proof separates P from NP -/
axiom natural_proofs_barrier : True -- Razborov-Rudich 1997

/-- Algebrization barrier: algebrizing techniques can't separate P from NP -/
axiom algebrization_barrier : True -- Aaronson-Wigderson 2009

/-! ## 6. Logical Properties -/

/-- P = NP and P ≠ NP are contradictory -/
theorem p_eq_np_iff_not_p_ne_np :
    P_eq_NP ↔ ¬ P_ne_NP := by
  constructor
  · intro h ⟨L, hNP, hnotP⟩; exact hnotP (h L hNP)
  · intro h L hNP
    by_contra hnotP
    exact h ⟨L, hNP, hnotP⟩

/-- If SAT is in P, then P = NP (via NP-completeness of SAT).
    This is the Cook-Levin reduction: every NP language poly-reduces to SAT.
    If SAT ∈ P, the reduction gives P-algorithms for all NP languages. -/
-- axiom cook_levin : InP SAT → P_eq_NP

/-- The contrapositive: P ≠ NP → SAT ∉ P -/
-- theorem sat_not_in_p_of_p_ne_np : P_ne_NP → ¬(InP SAT)

/-! ## Theorem Count: 1 proved (p_eq_np_iff_not_p_ne_np)
    The barriers are META-theorems, axiomatized.
    Cook-Levin needs TM formalization to state properly.
-/
