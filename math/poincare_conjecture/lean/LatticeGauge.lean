/-
  Yang-Mills — Lattice Gauge Theory Foundations

  This is the CORE formalization target. Everything on the lattice is
  finite-dimensional, so we can prove things without unbounded operator theory.

  The plan:
  1. Define lattice, links, plaquettes (DONE in Definitions.lean, refined here)
  2. Define gauge field as link → SU(n) (not just arbitrary matrices)
  3. Define Wilson action
  4. Prove Wilson action is gauge-invariant
  5. Define partition function via Haar measure
  6. Define Wilson loop observable
  7. Prove Wilson loop is gauge-invariant
  8. Define transfer matrix
  9. Prove transfer matrix is self-adjoint and positive (from reflection positivity)
  10. Define mass gap as spectral gap of transfer matrix

  This gets us to the STATEMENT of the mass gap on the lattice.
  The actual proof of the gap is the open problem.
-/

import Mathlib.Topology.Algebra.Group.Basic
import Mathlib.LinearAlgebra.Matrix.SpecialLinearGroup
import Mathlib.LinearAlgebra.UnitaryGroup

/-! ## The Lattice -/

/-- A d-dimensional periodic lattice with L sites per direction.
    Sites are elements of (Z/LZ)^d. -/
structure PeriodicLattice (d : ℕ) where
  L : ℕ
  hL : L > 0

namespace PeriodicLattice

variable {d : ℕ} (Λ : PeriodicLattice d)

/-- A site is a d-tuple of elements in Z/LZ -/
def Site := Fin d → ZMod Λ.L

/-- A directed link: origin site + direction -/
structure Link where
  origin : Λ.Site
  dir : Fin d

/-- The target of a link: origin + ê_dir (mod L) -/
def Link.target (ℓ : Λ.Link) : Λ.Site :=
  fun i => if i = ℓ.dir then ℓ.origin i + 1 else ℓ.origin i

/-- A plaquette: origin + two directions (ordered) -/
structure Plaquette where
  origin : Λ.Site
  μ : Fin d
  ν : Fin d
  hne : μ ≠ ν

/-- Number of links = d × L^d -/
-- Each site has d outgoing links (one per direction)

/-- Number of plaquettes = d(d-1)/2 × L^d -/
-- Each site has one plaquette per ordered pair of directions

end PeriodicLattice

/-! ## Gauge Field Configuration -/

/-- A lattice gauge field assigns a unitary matrix to each link.
    For SU(n): U_ℓ ∈ SU(n) ⊂ U(n).
    We use the unitary group from Mathlib for now. -/
def LatticeGaugeField {d : ℕ} (Λ : PeriodicLattice d) (n : ℕ) :=
  Λ.Link → Matrix.unitaryGroup (Fin n) ℂ

/-! ## Plaquette Variable -/

/-- The plaquette variable U_P is the ordered product of four link variables
    around an elementary square:

    U_P(x,μ,ν) = U(x,μ) · U(x+ê_μ,ν) · U(x+ê_ν,μ)⁻¹ · U(x,ν)⁻¹

    This lives in SU(n) (product of SU(n) elements). -/
-- TODO: Define plaquette_var : LatticeGaugeField Λ n → Λ.Plaquette → Matrix.unitaryGroup (Fin n) ℂ

/-! ## Wilson Action -/

/-- The Wilson action:
    S_W[U] = (β/N) Σ_{P} Re tr(I - U_P)

    where β = 2N/g² and the sum is over all plaquettes.

    Properties we need to prove:
    1. S_W ≥ 0 (since Re tr(U)/N ≤ 1 for U ∈ SU(N))
    2. S_W = 0 ⟺ all U_P = I (pure gauge)
    3. S_W is gauge-invariant
    4. S_W → (1/4g²) ∫ |F|² as lattice spacing a → 0
-/
-- TODO: Define wilson_action : ℝ → LatticeGaugeField Λ n → ℝ
-- TODO: Prove wilson_action_nonneg
-- TODO: Prove wilson_action_gauge_invariant

/-! ## Gauge Transformations -/

/-- A gauge transformation assigns a group element to each site.
    It acts on link variables by: U(x,μ) → g(x) · U(x,μ) · g(x+ê_μ)⁻¹ -/
def GaugeTransformation {d : ℕ} (Λ : PeriodicLattice d) (n : ℕ) :=
  Λ.Site → Matrix.unitaryGroup (Fin n) ℂ

/-- Apply gauge transformation to a gauge field -/
-- TODO: def gauge_transform (g : GaugeTransformation Λ n) (U : LatticeGaugeField Λ n) :
--   LatticeGaugeField Λ n

/-! ## Partition Function -/

/-- The partition function Z = ∫ ∏_ℓ dU_ℓ exp(-S_W[U])

    This is a finite-dimensional integral over a compact manifold
    (product of copies of SU(n)), so it is ALWAYS well-defined and finite.

    The measure is the product Haar measure on SU(n)^{#links}.
    Mathlib has Haar measure on compact groups. -/
-- TODO: Define partition_function using MeasureTheory.Measure.haar

/-! ## Wilson Loop -/

/-- A Wilson loop for a closed path C on the lattice:
    W(C) = (1/N) Tr(∏_{ℓ ∈ C} U_ℓ)

    This is gauge-invariant (trace of a conjugated product). -/
-- TODO: Define wilson_loop for a list of links forming a closed path
-- TODO: Prove gauge invariance

/-! ## Transfer Matrix -/

/-- The transfer matrix T acts on L²(SU(n)^{spatial_links}).

    For a lattice with one temporal link per spatial configuration:
    ⟨U'|T|U⟩ = ∫ ∏_{temporal_ℓ} dV_ℓ · exp(-S_W(U, V, U'))

    where S_W involves all plaquettes that touch the time slice.

    Key properties (from Osterwalder-Seiler):
    - T is self-adjoint (reflection positivity)
    - T is positive (reflection positivity)
    - T is trace-class (compact domain, continuous kernel)
    - Z = Tr(T^{N_t}) where N_t = number of time slices

    The Hamiltonian is H = -ln(T)/a (lattice spacing a).
    The mass gap is: Δ = -ln(λ₁/λ₀)/a
    where λ₀ ≥ λ₁ ≥ ... are eigenvalues of T. -/
-- TODO: Define transfer_matrix
-- TODO: Prove self-adjoint from reflection positivity
-- TODO: Prove positive
-- TODO: Define mass_gap_lattice as gap between first two eigenvalues

/-! ## The Mass Gap Statement (Lattice) -/

/-- **Lattice Mass Gap Conjecture** (finite lattice version):

    For SU(N) lattice gauge theory on a periodic lattice Λ with
    Wilson action at coupling β = 2N/g², the transfer matrix T has
    a unique largest eigenvalue λ₀ and a gap:

    λ₀ > λ₁  (equivalently: mass gap Δ = -ln(λ₁/λ₀)/a > 0)

    This is EASY on a finite lattice (compact operator on compact space,
    Perron-Frobenius-like argument for the positive kernel).

    The HARD part: Δ remains positive (and has a limit) as a → 0 and L → ∞. -/
-- TODO: State and prove finite-lattice mass gap (should be doable!)
-- TODO: State the continuum limit conjecture

/-! ## Theorem Count: 0 proved, 0 sorry (structure definitions only)

    Priority for next session:
    1. plaquette_var definition
    2. wilson_action definition
    3. gauge_transform definition + gauge_invariance proof
    4. finite_lattice_mass_gap theorem
-/
