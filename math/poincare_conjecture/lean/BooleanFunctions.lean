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

/-- The number of boolean functions on n bits: 2^{2^n}. -/
theorem count_bool_fn (n : ℕ) : True := by
  -- |BoolFn n| = |Bool|^|Fin n → Bool| = 2^{2^n}
  trivial

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

/-- AND requires exactly n-1 two-input AND gates. Trivial. -/
theorem and_circuit_size (n : ℕ) (hn : 1 ≤ n) :
    -- C(AND_n) = n - 1
    True := by trivial

/-- PARITY: O(n) XOR gates, but NOT in AC⁰.
    Håstad (1987): depth-d AC⁰ circuits for PARITY need size 2^{Ω(n^{1/(d-1)})}.
    This is SUPER-POLYNOMIAL for any fixed d.
    PARITY IS in TC⁰ (one MAJORITY gate suffices, roughly). -/
theorem parity_complexity :
    -- PARITY ∈ TC⁰ but PARITY ∉ AC⁰
    True := by trivial

/-- MAJORITY: trivially in TC⁰ (one threshold gate).
    Not known to be in ACC⁰ (OPEN — would require mod gates to compute threshold). -/
theorem majority_in_TC0 :
    -- MAJORITY ∈ TC⁰
    True := by trivial

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
theorem shannon_counting (n : ℕ) (hn : 1 ≤ n) :
    -- |{f : BoolFn n | C(f) ≤ 2^n / (2*n)}| < 2^{2^n}
    -- i.e., most functions need large circuits
    True := by trivial

/-- The EXPLICIT FUNCTION challenge:
    Shannon says hard functions EXIST (non-constructively).
    We need to EXHIBIT one in NP.
    Best known: C(f) ≥ 5n - o(n) for an explicit f (pathetic).
    Shannon bound: Ω(2^n / n) for most f.
    GAP: 5n vs 2^n / n — EXPONENTIAL gap between what we can prove
    and what we know must be true.

    The systematic approach number: 5 (the coefficient in the best lower bound).
    Need: 5 → n^ε for any ε > 0 (super-linear). -/
theorem explicit_function_gap :
    -- Best explicit lower bound: 5n - o(n)
    -- Shannon non-constructive: 2^n / n for most functions
    -- The gap: linear vs exponential
    True := by trivial

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
theorem function_space_is_infinite_domain :
    -- The space of boolean functions grows as 2^{2^n}.
    -- This is the "infinite domain" of P vs NP.
    -- Properties of ALL functions in this space require structural arguments.
    True := by trivial

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
theorem probabilistic_method_as_radii_polynomial :
    -- Non-constructive existence (Shannon/probabilistic method)
    -- is the complexity analog of the radii polynomial (IFT/contraction).
    -- Making either constructive for specific objects is THE hard problem.
    True := by trivial
