# results/quantum_sim_findings.md — Quantum Simulation Cost: Does a Quantum Simulator Escape the Holographic Bound?

**Date:** 2026-04-09
**Script:** `numerics/quantum_simulation_cost.py`
**Setup:** Quantum vs classical simulation cost, holographic bound on qubits, minimum faithful resolution

## Setup

`simulation_cost.py` showed that a classical Planck-resolution simulation of the observable
universe requires ~10^248 bits — exceeding the holographic bound of ~10^124 bits.
`lv_bounds.py` showed that LIV constraints (FERMI GRB 090510) rule out any simulator cell
larger than l_P (linear LIV exceeded by 7.2×), so the simulator must use Planck cells.

**New question:** can a QUANTUM simulator do better? A quantum computer with n qubits can
represent a superposition of 2^n classical states simultaneously. Does this let a quantum
simulation escape the holographic bound?

The answer is no, for three independent reasons: Hamiltonian dimension, 3D volume-law
entanglement, and the holographic bound applying equally to qubits and classical bits.

## Full Results

### Physical parameters

| Quantity | Value |
|---|---|
| Planck length l_P | 1.616×10⁻³⁵ m |
| Observable universe radius r_obs | 4.40×10²⁶ m |
| N_cells (Planck lattice) | 10^184.9 |
| Holographic bound S_holo | 10^123.5 bits = 10^123.5 qubits |
| Universe age / t_P (timesteps) | 10^60.9 |

### Classical vs quantum simulation cost comparison

| Approach | Cost (log₁₀ bits/qubits) | vs Holographic Budget |
|---|---|---|
| Classical (minimal, 1 bit/cell/step) | 10^185 | 10^61× over budget |
| Classical (realistic, 384 bits/cell/step) | 10^188 | 10^64× over budget |
| Quantum (Hamiltonian, d=2 per site) | 10^185 | 10^61× over budget |
| Holographic budget (max qubits/bits) | 10^124 | = budget |
| Min faithful resolution (classical or quantum) | l_eff ≈ 4.7×10⁻¹⁵ m | ~femtometer (4.7× fm) |

**The quantum simulation cost is the same order of magnitude as the classical cost.**
Neither can achieve Planck-resolution within the holographic budget.

### Minimum faithful resolution within holographic budget

Budget: 10^124 qubits (the holographic bound).
Constraint: N_cells(l_eff) = (r_obs / l_eff)³ ≤ 10^124.
Solution:

```
log10(l_eff) = (log10(V_obs) - log10(S_holo)) / 3
             = (80.6 - 123.5) / 3
             = −14.32
l_eff_min    = 10^{−14.32} m ≈ 4.74×10⁻¹⁵ m
```

| Comparison | Value |
|---|---|
| l_eff / l_P | 2.9×10²⁰ |
| l_eff / femtometer | 4.7 |
| l_eff / proton radius | 5.6 |
| l_eff / classical electron radius | 1.7 |

**The minimum faithful resolution is ~5 femtometers — squarely in the nuclear-physics regime.**
Any simulation (classical or quantum) that fits within the observable universe's information
budget cannot resolve structure below the femtometer scale.

## Finding 1: Quantum simulation at Planck resolution needs the same number of qubits as classical bits

Hamiltonian simulation of a d-state lattice with L sites requires L × log₂(d) qubits — one
qubit per site (d=2 minimal model). For a Planck-scale lattice:

- L = N_cells = V_obs / l_P³ = 10^{184.9} sites
- Qubits needed: 10^{184.9}

This is IDENTICAL to the classical 1 bit/cell cost. The quantum simulation gains nothing
in terms of state-space representation for a 3D lattice. The Hilbert space dimension is
2^{N_cells} ≈ 10^{10^185}, but you need all N_cells qubits to span it — you cannot
compress the lattice representation.

## Finding 2: 3D volume-law entanglement rules out tensor-network compression

The only known quantum compression strategy for simulation is tensor networks:
- **1D systems with area law** (MPS/DMRG): entanglement entropy S(A) ~ constant.
  Bond dimension χ stays polynomial → O(D × d × χ²) parameters. Efficient.
- **2D systems**: area law S(A) ~ perimeter(A). PEPS requires exponentially large χ in practice.
- **3D systems with volume law**: S(A) ∝ vol(A). No polynomial-parameter representation exists.

The observable universe is a 3D system with generic (volume-law) entanglement. There is no
tensor-network parametrization that reduces the 10^185 qubit requirement. The quantum simulation
cost is irreducibly exponential in the volume.

## Finding 3: The holographic bound applies equally to classical bits and qubits

The holographic bound is a statement about ENTROPY, not about whether that entropy is
stored classically or quantum mechanically:

- S_max = π R² / l_P² ≈ 10^{123.5} bits (for R = r_obs)
- A qubit has at most 1 bit of von Neumann entropy (S = −Tr(ρ log₂ ρ) ≤ 1 for a single qubit)
- Therefore: max_qubits ≤ S_max ≈ 10^{123.5}

This is the same number as the classical bit bound. A quantum simulator does not escape
the holographic constraint by being quantum — the constraint is about entropy capacity,
not encoding scheme.

**The gap:** 10^{185} qubits needed vs 10^{124} qubits available = 10^{61} times more
than the universe can store.

## Finding 4: The 'superposition economy' argument fails

The naive hope: "log₂(10^{185}) ≈ 615 qubits can represent a superposition over all
10^{185} Planck cells, so we need only ~615 qubits."

This fails for four independent reasons:

1. **Readout cost:** extracting all 2^N amplitudes from N qubits requires 2^N measurements.
   The information gain from the superposition can only be accessed by exponential work.

2. **Born rule collapse:** each measurement collapses the wavefunction to a single classical
   outcome. A single "run" of the quantum simulator yields only O(log N) bits of information
   about the 2^N-dimensional state.

3. **State preparation cost:** specifying an arbitrary superposition of 10^{185} classical
   states requires specifying ~2^{10^185} complex amplitudes. The classical overhead of
   PREPARING the initial state dominates.

4. **Gate complexity:** each time-evolution step applies a unitary U = exp(−i H dt).
   For a local Hamiltonian with N_cells sites, this requires O(N_cells) gate operations.
   There is no known way to skip timesteps for generic Hamiltonians (no quantum speedup
   beyond √T in specific oracle models; for physics simulation, T steps are required).

The quantum advantage for simulation of QUANTUM systems (vs classical simulation of quantum
systems) is that classical simulation requires 2^N_cells bits of memory, while a quantum
simulation requires only N_cells qubits. But this advantage applies when simulating a
quantum system on a quantum computer. For the simulation hypothesis, the simulated system
is already classical (or quantum-but-described-by-the-holographic-bound), so the advantage
disappears.

## Finding 5: The simulation hypothesis is informationally self-defeating (combined result)

Combining `lv_bounds.py` and this script:

1. **From lv_bounds.py:** LIV constraints (GRB 090510) rule out any simulator with cells
   larger than l_P. The simulator must use Planck-scale cells or finer.

2. **From this script:** Planck-scale simulation requires 10^{185} bits/qubits per timestep,
   which is 10^{61}× the holographic budget of the observable universe.

3. **Combined:** the simulation must use Planck cells (by LIV) but cannot fit in the observable
   universe at Planck precision (by holographic bound). If the simulator is INSIDE the observable
   universe, it is impossible. If it is OUTSIDE, it is not constrained by our holographic bound —
   but then the simulation hypothesis becomes unfalsifiable: no observation can constrain a
   simulator with different physics.

4. **The only escape:** the simulator operates at resolution l_eff ≥ ~5 fm (femtometer scale)
   and is not constrained to use Planck cells. But LIV bounds already rule out any
   discretization artifact larger than l_P. A femtometer-scale simulator would produce
   enormous Lorentz violations (~10^{20}× the Planck-scale LIV bound) — ruled out at
   extraordinary confidence.

**The simulation hypothesis, in any form consistent with all current observations, requires
a simulator that either:**
- (a) fits within the observable universe but cannot store its own state (impossible), or
- (b) is outside the observable universe and unconstrained by any measurement (unfalsifiable).

## Comparison with simulation_cost.py findings

| Finding | simulation_cost.py | quantum_simulation_cost.py |
|---|---|---|
| Planck classical bits/step | 10^187 | — |
| Planck qubit cost | — | 10^185 (same order) |
| Holographic budget | 10^124 bits | 10^124 qubits (identical) |
| Excess | 10^63 | 10^61 |
| Minimum resolution | not computed | **~5 fm (femtometer)** |
| Quantum escape? | not addressed | **No — three independent reasons** |

## Sky bridges (numerical)

- **physics/simulation_cost.py** — classical simulation established the 10^248-bit cost for
  full Planck-precision history. This script sharpens it: the per-timestep STATE cost is
  10^185 bits, and quantum simulation does not reduce this.
- **physics/lv_bounds.py** — LIV constraints force the simulator to use Planck cells.
  The combined impossibility proof is: LIV requires Planck cells, holographic bound forbids
  Planck-cell simulation (classically or quantum). The hypothesis is self-defeating.
- **physics/what_is_computation** — the minimum faithful resolution (~5 fm) is in the
  nuclear-physics regime. Any computation the universe "runs on itself" is coarser than
  nuclear structure. QCD (which describes nuclear physics) is already at the edge of what
  a holographic-budget simulator could represent faithfully.
- **physics/what_is_information** — the holographic bound as an information bound is shared
  between S-information (thermodynamic) and quantum information (von Neumann entropy). The
  equivalence of the two bounds here (same number for bits and qubits) reflects the
  covariant entropy bound applying to all forms of information.

## Status

Phase 2 numerics. The classical impossibility result is confirmed quantum-mechanically:

1. Quantum simulation at Planck resolution requires 10^185 qubits — same order as classical bits.
2. The holographic bound caps both at 10^124, leaving a 10^61 deficit.
3. 3D volume-law entanglement prevents tensor-network compression.
4. The minimum faithful resolution within the holographic budget is ~5 fm (femtometer).
5. Combining with LIV bounds: the simulation hypothesis is either informationally impossible
   (simulator inside the universe) or unfalsifiable (simulator outside).

The numerical track has established that the simulation hypothesis in its strongest (Planck-scale)
form is ruled out by information theory alone — independently of computational complexity,
energy requirements, or technological limitations.
