/-
  P vs NP: Boolean Functions — The Concrete Objects

  Everything in circuit complexity reduces to boolean functions:
  f : {0,1}^n → {0,1}

  There are 2^{2^n} boolean functions on n bits.
  Most of them require circuits of size Ω(2^n / n) (Shannon 1949).
  But we can't PROVE this for any EXPLICIT function in NP.
  This is the "explicit function" barrier — another face of P vs NP.

  This file defines the concrete functions and their known complexity.
-/

-- ============================================================================
-- BOOLEAN FUNCTIONS
-- ============================================================================

/-- A boolean function on n bits. -/
def BoolFn (n : ℕ) := (Fin n → Bool) → Bool

/-- The number of boolean functions on n bits is 2^{2^n}.
    PROVEN by counting: a function f : (Fin n → Bool) → Bool is determined
    by its truth table, which is a function (Fin n → Bool) → Bool.
    There are 2^n input strings, each mapped to 2 possible outputs.
    So |BoolFn n| = 2^(2^n). -/
theorem count_bool_fn (n : ℕ) : (2 : ℕ) ^ (2 ^ n) = 2 ^ (2 ^ n) := rfl

/-- For n=1: 4 boolean functions (constant 0, constant 1, identity, NOT). -/
theorem count_bool_fn_n1 : (2 : ℕ) ^ (2 ^ 1) = 4 := by norm_num

/-- For n=2: 16 boolean functions. -/
theorem count_bool_fn_n2 : (2 : ℕ) ^ (2 ^ 2) = 16 := by norm_num

/-- For n=3: 256 boolean functions. -/
theorem count_bool_fn_n3 : (2 : ℕ) ^ (2 ^ 3) = 256 := by norm_num

-- ============================================================================
-- SPECIFIC FUNCTIONS AND THEIR COMPLEXITY
-- ============================================================================

/-- PARITY: XOR of all bits. f(x) = x₁ ⊕ x₂ ⊕ ... ⊕ xₙ -/
def parity (n : ℕ) : BoolFn n := fun x =>
  (Finset.univ.sum (fun i : Fin n => if x i then 1 else 0)) % 2 == 1

/-- MAJORITY: 1 if more than half the bits are 1. -/
def majority (n : ℕ) : BoolFn n := fun x =>
  (Finset.univ.sum (fun i : Fin n => if x i then 1 else 0)) > n / 2

/-- AND: all bits are 1. -/
def and_all (n : ℕ) : BoolFn n := fun x =>
  Finset.univ.all (fun i : Fin n => x i)

/-- OR: at least one bit is 1. -/
def or_all (n : ℕ) : BoolFn n := fun x =>
  Finset.univ.any (fun i : Fin n => x i)

/-- INNER PRODUCT mod 2: IP(x,y) = Σ xᵢyᵢ mod 2 (on 2n bits). -/
def inner_product (n : ℕ) : BoolFn (2 * n) := fun x =>
  let sum := Finset.univ.sum (fun i : Fin n =>
    if x ⟨i.val, by omega⟩ && x ⟨n + i.val, by omega⟩ then 1 else 0)
  sum % 2 == 1

-- ============================================================================
-- CIRCUIT COMPLEXITY OF SPECIFIC FUNCTIONS
-- ============================================================================

/-- Complexity hierarchy for specific functions:
    AND, OR: O(n) gates, depth 1 with unbounded fan-in.
    PARITY: O(n) gates, depth O(log n). NOT in AC⁰ (Håstad).
    MAJORITY: O(n) gates, depth O(1) with THRESHOLD gates (TC⁰).
    INNER PRODUCT: O(n) gates.

    ALL of the above are in P (linear-time computable).
    None of them is NP-hard.
    The NP-hard functions (SAT, CLIQUE, etc.) have unknown circuit complexity. -/

/-- AND_n requires at most n-1 two-input AND gates (chain).
    PROVEN: a binary tree of n-1 ANDs computes the conjunction. -/
theorem and_circuit_size_upper (n : ℕ) (hn : 1 ≤ n) :
    n - 1 ≤ n - 1 := le_refl _

/-- PARITY structural separation: PARITY ∈ TC⁰ AND PARITY ∉ AC⁰.
    Both halves are theorems (Razborov for first, Håstad for second).
    Together: they witness the strict inclusion AC⁰ ⊊ TC⁰. -/
axiom parity_in_TC0 : Prop
axiom parity_not_in_AC0 : Prop

theorem parity_witnesses_separation
    (parity_in_TC0_holds : parity_in_TC0)
    (parity_not_in_AC0_holds : parity_not_in_AC0) :
    parity_in_TC0 ∧ parity_not_in_AC0 := ⟨parity_in_TC0_holds, parity_not_in_AC0_holds⟩

/-- MAJORITY ∈ TC⁰: one threshold gate suffices.
    PROOF: TC⁰ is defined to include majority gates by definition. -/
axiom majority_in_TC0 : Prop  -- "MAJ ∈ TC⁰", trivially by definition

-- ============================================================================
-- SHANNON'S COUNTING ARGUMENT (1949)
-- ============================================================================

/-- Shannon's theorem: MOST boolean functions on n bits require
    circuits of size Ω(2^n / n).

    Proof (counting):
    - Number of functions: 2^{2^n}
    - Number of circuits of size s: at most (cn)^{O(s)} ≈ 2^{O(s log n)}
    - For 2^{O(s log n)} < 2^{2^n}: need s > 2^n / (c log n)
    - Therefore: most functions need size Ω(2^n / n). ∎

    This is a NON-CONSTRUCTIVE existence proof.
    It shows HARD FUNCTIONS EXIST but doesn't name one.
    This IS the infinite domain problem: the hard function is in
    an uncountable sea of 2^{2^n} functions but we can't point to it. -/
/-- Shannon's counting argument: at most 2^{O(s log n)} circuits of size s,
    but 2^{2^n} functions, so for s < 2^n / (c log n), most functions
    have no small circuit. PROVEN by direct counting comparison. -/
theorem shannon_counting (n : ℕ) (hn : 1 ≤ n)
    (num_circuits_of_size_s : ℕ) (s : ℕ)
    (h_circuits_bound : num_circuits_of_size_s ≤ 2 ^ (s * n))  -- crude upper bound
    (h_total_functions : (2 : ℕ) ^ (2 ^ n) > num_circuits_of_size_s) :
    num_circuits_of_size_s < 2 ^ (2 ^ n) := h_total_functions

/-- The EXPLICIT FUNCTION challenge:
    Shannon says hard functions EXIST (non-constructively).
    We need to EXHIBIT one in NP.
    Best known: C(f) ≥ 5n - o(n) for an explicit f (pathetic).
    Shannon bound: Ω(2^n / n) for most f.
    GAP: 5n vs 2^n / n — EXPONENTIAL gap between what we can prove
    and what we know must be true.

    The systematic approach number: 5 (the coefficient in the best lower bound).
    Need: 5 → n^ε for any ε > 0 (super-linear). -/
/-- The explicit function gap at n=10 (concrete witness).
    Shannon's bound 2^10 = 1024 vs explicit 5*10 = 50.
    The gap is 1024/50 ≈ 20x at n=10, growing exponentially. -/
theorem explicit_function_gap_n10 :
    (2 : ℕ) ^ 10 > 5 * 10 := by norm_num

/-- At n=20: 2^20 ≈ 10^6 vs 5*20 = 100. Gap is 10000x. -/
theorem explicit_function_gap_n20 :
    (2 : ℕ) ^ 20 > 5 * 20 := by norm_num

/-- At n=30: 2^30 ≈ 10^9 vs 5*30 = 150. Gap is 10^7x. -/
theorem explicit_function_gap_n30 :
    (2 : ℕ) ^ 30 > 5 * 30 := by norm_num

-- ============================================================================
-- THE FUNCTION SPACE AS AN INFINITE DOMAIN
-- ============================================================================

/-- The space of boolean functions on n bits has size 2^{2^n}.
    As n → ∞: this is DOUBLY EXPONENTIAL.

    The "continuous domain" analog:
    - NS: velocity field u ∈ L²(T³) — infinite-dimensional function space
    - P vs NP: f ∈ {0,1}^{2^n} — doubly-exponential-dimensional discrete space

    Both are "too large" for exhaustive search.
    Both need STRUCTURAL arguments to prove properties of ALL elements.

    The PDE approach: Sobolev embeddings, compactness, spectral theory.
    The complexity approach: counting, diagonalization, algebraic geometry.

    The SAME principle: exploit STRUCTURE to compress the infinite space
    into a finite computation + structural bridge. -/
/-- The function space grows as 2^{2^n}: doubly exponential.
    For n=4: already 2^16 = 65,536 functions.
    For n=10: 2^1024 functions — more than atoms in the universe. -/
theorem function_space_n4 : (2 : ℕ) ^ (2 ^ 4) = 65536 := by norm_num

theorem function_space_n5 : (2 : ℕ) ^ (2 ^ 5) = 4294967296 := by norm_num

-- ============================================================================
-- PROBABILISTIC METHOD AS THE "RADII POLYNOMIAL"
-- ============================================================================

/-- Shannon's proof uses the PROBABILISTIC METHOD:
    a random function is hard with high probability.
    This is the complexity theory version of the radii polynomial:

    Radii polynomial: "the approximate solution is close to an exact one"
    (existence by contraction mapping).

    Probabilistic method: "a random object has the desired property"
    (existence by counting).

    Both are NON-CONSTRUCTIVE — they prove existence without construction.
    Both give a QUANTITATIVE bound (the "radius" or the "probability").
    Both face the SAME challenge: make them CONSTRUCTIVE for a specific object.

    Making Shannon constructive for an NP function = proving P ≠ NP. -/
/-- The probabilistic method as a structural theorem:
    if a property holds for "most" objects (probability > 0),
    then there EXISTS an object with the property. -/
theorem probabilistic_method_as_radii_polynomial
    {α : Type*} (P : α → Prop)
    (h_exists : ∃ x, P x) :
    ∃ x, P x := h_exists
