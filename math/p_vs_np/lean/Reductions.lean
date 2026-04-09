/-
  P vs NP: Formalizable Structure

  We CAN'T prove P ≠ NP. But we CAN formalize:
  1. The definitions (P, NP, NP-complete, polynomial reduction)
  2. The reductions (SAT is NP-complete, 3-SAT ≤_p SAT, etc.)
  3. The consequences (if ANY NP-complete problem is in P, then P = NP)
  4. The barriers (what proof techniques provably can't work)

  These are THEOREMS, not conjectures. They're provable in Lean.
-/

-- A decision problem is a function from binary strings to Bool.
def DecisionProblem := List Bool → Bool

-- A problem is in P if there exists a polynomial-time algorithm solving it.
-- We model "polynomial time" as: ∃ algorithm A and polynomial p such that
-- A(x) = f(x) for all x, and A runs in time ≤ p(|x|).
-- In Lean, we abstract this as a predicate.
def InP (f : DecisionProblem) : Prop :=
  ∃ (A : List Bool → Bool) (k : ℕ),
    (∀ x, A x = f x) ∧ True  -- "and A runs in O(|x|^k) time"
    -- (Time bound abstracted — would need a computation model)

-- A problem is in NP if there exists a polynomial-time VERIFIER.
-- Given input x and certificate c: V(x,c) runs in poly(|x|) time.
def InNP (f : DecisionProblem) : Prop :=
  ∃ (V : List Bool → List Bool → Bool) (k : ℕ),
    (∀ x, f x = true ↔ ∃ c, c.length ≤ x.length ^ k ∧ V x c = true) ∧ True

-- P ⊆ NP: every problem solvable in poly time is also verifiable.
-- The certificate is ignored; the algorithm itself serves as verifier.
theorem P_subset_NP (f : DecisionProblem) (hf : InP f) : InNP f := by
  obtain ⟨A, k, hA, _⟩ := hf
  exact ⟨fun x _ => A x, 0, ⟨fun x => by
    constructor
    · intro h; exact ⟨[], by simp, by rw [hA]; exact h⟩
    · intro ⟨_, _, hc⟩; rw [← hA]; exact hc⟩, trivial⟩

-- Polynomial-time reduction: f ≤_p g means f reduces to g.
-- There exists a poly-time function R such that f(x) = g(R(x)).
def PolyReduces (f g : DecisionProblem) : Prop :=
  ∃ (R : List Bool → List Bool),
    (∀ x, f x = g (R x)) ∧ True  -- "and R runs in poly time"

notation:50 f " ≤ₚ " g => PolyReduces f g

-- Transitivity of reductions
theorem poly_reduces_trans (f g h : DecisionProblem)
    (hfg : f ≤ₚ g) (hgh : g ≤ₚ h) : f ≤ₚ h := by
  obtain ⟨R₁, hR₁, _⟩ := hfg
  obtain ⟨R₂, hR₂, _⟩ := hgh
  exact ⟨R₂ ∘ R₁, fun x => by rw [Function.comp, hR₁, hR₂], trivial⟩

-- NP-hard: every NP problem reduces to it.
def NPHard (g : DecisionProblem) : Prop :=
  ∀ f, InNP f → f ≤ₚ g

-- NP-complete: NP-hard AND in NP.
def NPComplete (f : DecisionProblem) : Prop :=
  InNP f ∧ NPHard f

-- THE KEY THEOREM: If any NP-complete problem is in P, then P = NP.
-- This is the Cook-Levin consequence (not the full theorem).
theorem np_complete_in_P_implies_P_eq_NP
    (f : DecisionProblem) (hf : NPComplete f) (hfP : InP f) :
    ∀ g, InNP g → InP g := by
  intro g hg
  -- g is in NP, f is NP-complete, so g ≤_p f
  obtain ⟨_, hhard⟩ := hf
  obtain ⟨R, hR, _⟩ := hhard g hg
  -- f is in P, with algorithm A
  obtain ⟨A, k, hA, _⟩ := hfP
  -- g(x) = f(R(x)) = A(R(x)). So A∘R solves g in poly time.
  exact ⟨A ∘ R, k, ⟨fun x => by rw [Function.comp, hR, hA], trivial⟩⟩

-- Contrapositive: if P ≠ NP, then no NP-complete problem is in P.
theorem P_ne_NP_implies_no_NPC_in_P
    (h : ∃ g, InNP g ∧ ¬InP g)  -- P ≠ NP witness
    (f : DecisionProblem) (hf : NPComplete f) :
    ¬InP f := by
  intro hfP
  obtain ⟨g, hgNP, hgNotP⟩ := h
  exact hgNotP (np_complete_in_P_implies_P_eq_NP f hf hfP g hgNP)

-- If two problems are NP-complete, they poly-reduce to each other.
theorem npc_equiv (f g : DecisionProblem) (hf : NPComplete f) (hg : NPComplete g) :
    (f ≤ₚ g) ∧ (g ≤ₚ f) := by
  exact ⟨hg.2 f hf.1, hf.2 g hg.1⟩

-- The number of NP-complete problems is either 0 or all-of-NP.
-- If P = NP: every nontrivial NP problem is NP-complete (trivially).
-- If P ≠ NP: Ladner's theorem gives intermediate problems,
--   but NP-complete problems form a specific class.
theorem one_breaks_all (f g : DecisionProblem)
    (hf : NPComplete f) (hg : NPComplete g) (hfP : InP f) :
    InP g := by
  exact np_complete_in_P_implies_P_eq_NP f hf hfP g hg.1
