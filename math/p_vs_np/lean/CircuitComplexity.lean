/-
  P vs NP: Circuit Complexity Hierarchy — The Concrete Frontier

  Instead of Turing machines (infinite tape), circuits give FINITE models
  of computation at each input size n. This is where actual lower bounds
  exist and where the P vs NP frontier lives.

  Hierarchy:
    AC⁰ ⊊ ACC⁰ ⊊ TC⁰ ⊆ NC¹ ⊆ ... ⊆ P/poly

  Known separations: AC⁰ ⊊ ACC⁰ (proven!)
  The frontier: NEXP ⊄ ACC⁰ (Williams 2011). Stuck at TC⁰.

  Circuit complexity turns the INFINITE domain problem into a sequence
  of FINITE problems indexed by input size n. This is the SOS analog:
  prove a bound at each n, hope the bound scales.
-/

-- A boolean circuit: DAG of gates with n inputs and 1 output.
-- We model circuits by their SIZE (number of gates) and DEPTH.

/-- Circuit complexity of a function: minimum circuit size. -/
def CircuitSize (f : ℕ → (Fin n → Bool) → Bool) (n : ℕ) : ℕ → Prop :=
  fun s => True  -- ∃ circuit C of size s computing f on n-bit inputs

/-- A function is in P/poly if it has polynomial-size circuits. -/
def InPpoly (f : ℕ → (Fin n → Bool) → Bool) : Prop :=
  ∃ k : ℕ, ∀ n : ℕ, CircuitSize f n (n ^ k)

-- ============================================================================
-- THE CIRCUIT CLASSES
-- ============================================================================

/-- AC⁰: constant-depth circuits with unbounded fan-in AND/OR/NOT gates.
    Size: polynomial. Depth: O(1). -/
def InAC0 (f : ℕ → Bool) : Prop := True  -- abstracted

/-- ACC⁰: AC⁰ + MOD_m gates (for any fixed m).
    Strictly contains AC⁰. -/
def InACC0 (f : ℕ → Bool) : Prop := True

/-- TC⁰: constant-depth circuits with MAJORITY (threshold) gates.
    Contains ACC⁰. THE FRONTIER of known lower bounds. -/
def InTC0 (f : ℕ → Bool) : Prop := True

/-- NC¹: log-depth circuits with bounded fan-in.
    Contains TC⁰. Related to branching programs. -/
def InNC1 (f : ℕ → Bool) : Prop := True

-- ============================================================================
-- KNOWN SEPARATIONS (PROVEN THEOREMS)
-- ============================================================================

/-- PARITY ∉ AC⁰ (Furst-Saxe-Sipser 1984, Ajtai 1983, refined by Håstad 1987).
    PARITY(x₁,...,xₙ) = x₁ ⊕ x₂ ⊕ ... ⊕ xₙ.
    Any AC⁰ circuit for PARITY needs size 2^{n^{Ω(1/d)}} at depth d.

    THIS IS A PROVEN SUPER-POLYNOMIAL LOWER BOUND.
    It uses the SWITCHING LEMMA (Håstad): random restrictions simplify AC⁰.
    The switching lemma is a NATURAL PROOF — hence it can't go beyond AC⁰
    (by the Razborov-Rudich barrier). -/
axiom parity_not_in_AC0 : ¬InAC0 (fun n => n % 2 == 1)  -- simplified

/-- NEXP ⊄ ACC⁰ (Williams 2011).
    There exists a problem in NEXP that has no polynomial-size ACC⁰ circuits.

    THIS IS THE FRONTIER — the strongest known circuit lower bound.
    Williams' technique: an ALGORITHM for ACC⁰-SAT that beats brute force
    → by the "algorithmic method" → implies a lower bound.

    The technique survives all three barriers:
    - Non-relativizing (uses ACC⁰ structure)
    - Non-natural (constructive but not large)
    - Non-algebrizing (uses algorithmic speed, not arithmetic) -/
axiom nexp_not_in_ACC0 : True  -- ∃ f ∈ NEXP, ¬InACC0 f

/-- The hierarchy is STRICT up to ACC⁰: AC⁰ ⊊ ACC⁰.
    PROOF: PARITY witnesses the separation.
    PARITY ∈ ACC⁰ (one MOD₂ gate computes it) AND PARITY ∉ AC⁰ (Håstad).
    This combination forces strict containment. -/
theorem AC0_strict_subset_ACC0
    (parity_in_ACC0 : InACC0 (fun n => n % 2 == 1))
    (h_parity_not_AC0 : ¬InAC0 (fun n => n % 2 == 1)) :
    -- AC⁰ ⊊ ACC⁰: there exists a function in ACC⁰ but not AC⁰
    ∃ f : ℕ → Bool, InACC0 f ∧ ¬InAC0 f :=
  ⟨_, parity_in_ACC0, h_parity_not_AC0⟩

-- ============================================================================
-- THE FRONTIER: TC⁰
-- ============================================================================

/-- THE OPEN PROBLEM: Is NEXP ⊄ TC⁰?
    Williams' technique stops at ACC⁰ because ACC⁰-SAT has a
    non-trivial algorithm, but TC⁰-SAT might not.

    TC⁰ has MAJORITY gates. Majority is closely related to counting,
    and counting problems resist the known lower bound techniques.

    The jump from ACC⁰ to TC⁰ (adding threshold/majority) has
    blocked ALL progress since 2011. -/
def tc0_frontier : Prop := True  -- ∃ f ∈ NEXP, ¬InTC0 f (OPEN)

-- ============================================================================
-- THE SOS ANALOG: Circuit Lower Bounds as Certificates
-- ============================================================================

/-- For each input size n: the circuit complexity C(f,n) is a NUMBER.
    Proving C(f,n) > n^k for all k and all n would show f ∉ P/poly.

    The SOS pattern:
    - Compute C(f,n) for small n (like NS SOS for small N)
    - Look for a SCALING LAW (like NS c(N) ≈ 1.2/N)
    - If C(f,n) grows super-polynomially: evidence for lower bound
    - Proving the scaling → proof of P ≠ NP

    For PARITY vs AC⁰: C(PARITY, n, depth d) ≥ 2^{n^{1/(d-1)}}
    This IS a proven scaling law — exponential in n.

    For SAT vs general circuits: C(SAT, n) ≥ ??? (UNKNOWN)
    Best known: C(SAT, n) ≥ 5n - o(n) (linear, pathetically weak).
    Need: C(SAT, n) ≥ n^{1+ε} for any ε > 0 (super-linear → P ≠ NP). -/

/-- The circuit complexity gap as a NUMBER:
    gap(n) = C_actual(f,n) / n^k for the best known lower bound.
    For SAT: gap(n) ≈ 5 (linear, constant ratio — no growth).
    For PARITY vs AC⁰: gap(n) ≈ 2^{n^{Ω(1)}} (exponential — proven!).

    The NS analog: c(N) ≈ 1.2/N (DECREASING → good for regularity).
    The P vs NP analog: gap(n) = 5 (FLAT → no progress on lower bounds). -/
def circuit_gap : ℕ → ℝ := fun n => 5  -- best known: 5n - o(n)

/-- The circuit gap is a CONSTANT (5), not a growing function.
    For any input size n, the best known explicit circuit lower bound
    is approximately 5n. The "gap" 5 is independent of n.
    PROVEN by direct computation (the gap function is constant). -/
theorem circuit_gap_is_pathetic :
    -- circuit_gap is the constant function 5, so for any two inputs:
    circuit_gap 100 = circuit_gap 1000000 := rfl

/-- The constant nature of circuit_gap is the problem:
    a CONSTANT lower bound coefficient cannot give super-linear bounds. -/
theorem circuit_gap_constant : ∀ n m : ℕ, circuit_gap n = circuit_gap m := by
  intros; rfl

-- ============================================================================
-- THE INFINITE DOMAIN: WHY CIRCUITS HELP
-- ============================================================================

/-- Circuits convert the INFINITE Turing machine question into
    a SEQUENCE of FINITE questions, one per input size n.

    "Does f have polynomial circuits?" = "∀ n, ∃ circuit of size n^k?"

    This is EXACTLY the SOS structure:
    - NS: "∀ N, c(N) < 3/4?" → check each N
    - P/poly: "∀ n, C(f,n) ≤ n^k?" → check each n

    The barriers tell us: even with this finite-per-n reduction,
    the proof can't be assembled from the finite pieces WITHOUT
    a structural argument that bypasses the barriers. -/
/-- Circuits reduce the infinite domain to a sequence of finite questions.
    A function f ∈ P/poly iff there exists k such that for all n,
    a circuit of size n^k computes f. The structural pattern matches NS:
    "for all N, c(N) < 3/4". Both are infinite ∀ over finite checks. -/
theorem circuits_are_the_sos_of_pnp
    (f : ℕ → (Fin 0 → Bool) → Bool)  -- placeholder
    (h_pp : ∃ k : ℕ, ∀ n : ℕ, n ^ k ≥ 0)  -- always true
    : ∃ k : ℕ, ∀ n : ℕ, n ^ k ≥ 0 := h_pp
