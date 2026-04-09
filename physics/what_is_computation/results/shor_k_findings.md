# results/shor_k_findings.md — Shor's Algorithm and K-Structure

**Date:** 2026-04-09
**Script:** `numerics/shor_k_structure.py`
**Data:** `results/shor_k_data.json`
**Extends:** `results/grover_findings.md` (Grover doubling period = 2 variables)
**Addresses:** `gap.md` residual question R3

---

## Setup

The script compares three complexity regimes for factoring an n-bit number N = 2^n:

- **Classical trial division:** O(2^(n/2)) — check divisors up to sqrt(N)
- **General number field sieve (NFS):** exp(c * n^(1/3) * (ln n)^(2/3)) — subexponential
- **Quantum Shor:** O(n^2 * log n * log log n) — polynomial in n
- **Grover (unstructured search baseline):** O(pi/4 * 2^(n/2)) — same exponent as trial division

Additionally, the script demonstrates period-finding on f(x) = 7^x mod 15 (the canonical
Shor example) and connects the results to K-information structure.

---

## Finding 1: Shor is exponentially faster than classical — the speedup is not Grover-like

The speedup of Shor over trial division grows as 2^(n/2) / n^2 — exponential in n:

| n (bits) | Trial division | Shor ops | Speedup (Trial/Shor) |
|----------|---------------|----------|---------------------|
| 10 | 3.2e+01 | 701 | 0.046× (Shor is slower at small n) |
| 20 | 1.0e+03 | 4,170 | 0.25× |
| 30 | 3.3e+04 | 11,316 | 2.9× |
| 40 | 1.0e+06 | 22,653 | 46× |
| 50 | 3.4e+07 | 38,548 | 871× |
| 100 | 1.1e+15 | 194,951 | 5.8e+09× |

At n=100, trial division requires ~10^15 operations while Shor requires ~2×10^5 — a speedup
of nearly 10^10. This is exponential growth: each 10 bits added multiplies the speedup by ~32.

Grover on the same problem gives speedup ~1.27× over trial division at every n — barely any
advantage, because Grover reduces the exponent from 2^n to 2^(n/2) but trial division already
operates at 2^(n/2). Both trial division and Grover search at the same asymptotic scaling.

---

## Finding 2: The Grover/Classical ratio is constant (~1.27×) for factoring

| n | Grover/Trial speedup |
|---|---------------------|
| 10 | 1.27× |
| 20 | 1.27× |
| 50 | 1.27× |
| 100 | 1.27× |

This constant arises because:
- Trial division: O(sqrt(N)) = O(2^(n/2)) operations
- Grover on n-bit search space: O(pi/4 * 2^(n/2)) queries

Both scale identically (O(2^(n/2))). Grover cannot help with factoring beyond the constant
pi/4 ≈ 0.785 prefactor — the exponent is unchanged. The speedup is a constant factor, not
exponential.

**This is the key distinction:** Shor's speedup over classical grows as ~10^10 at n=100;
Grover's speedup over classical stays at ~1.27× at all n.

---

## Finding 3: K-structure demonstration — f(x) = 7^x mod 15

The function f(x) = 7^x mod 15 produces:

```
x=0-7:   1   7   4  13   1   7   4  13
x=8-15:  1   7   4  13   1   7   4  13
...
```

**Period r = 4** — verified: f(x + 4) = f(x) for all x in [0, 36).

- r = 4 divides phi(15) = phi(3) × phi(5) = 2 × 4 = 8. (True)
- 7^4 mod 15 = 1. (True — the period terminates at the identity.)
- From r = 4: gcd(7^2 - 1, 15) = gcd(3, 15) = **3** and gcd(7^2 + 1, 15) = gcd(5, 15) = **5**.
- Recovery: 15 = 3 × 5. Correct.

**Classical birthday-paradox period-finding:** found collision at step 4 (O(sqrt(4)) = 2 expected).

**Quantum QFT cost:** O(n^2) = 16 gates for n = ceil(log2(15)) = 4 qubits. One Fourier-sampling
measurement suffices to identify a frequency multiple of M/r, from which r is recovered classically
via continued-fraction approximation.

**DFT magnitudes:** The discrete Fourier transform of the f(x) sequence shows a large peak at
k=10 (corresponding to period candidate r=4), with all other bins near zero. This is the signature
of periodic K-structure: a flat K-landscape would have uniform DFT magnitudes.

---

## Finding 4: The K-structure hierarchy (updated from Grover findings)

Combining Grover findings with Shor findings yields a three-tier K-structure hierarchy:

| K-structure type | Example | Classical cost | Quantum cost | Doubling period |
|-----------------|---------|----------------|--------------|-----------------|
| None (flat) | Unstructured search | O(2^n) | O(2^(n/2)) Grover | 2 variables |
| Logical (local) | 3-SAT | O(2^n) hard | O(2^(n/2)) Grover bound | ~14 vars (DPLL) |
| Periodic group orbit | Factoring, DL | O(exp(n^(1/3))) NFS | O(n^2) Shor | infinity (polynomial) |

"Doubling period = infinity" for Shor means the operation count does not double as n grows by
a fixed amount — it grows polynomially, so the exponential doubling period is undefined.
The exponent has collapsed to zero.

---

## Finding 5: Two qualitatively distinct modes of quantum advantage

**Mode 1: Amplitude amplification (Grover)**
- Prerequisite: any binary oracle (yes/no membership test)
- K-structure required: NONE
- Speedup mechanism: quantum interference rotates target amplitude by O(1/sqrt(N)) per step
- Result: exponent halved (2^n → 2^(n/2))
- Doubling period: 1 variable → 2 variables
- This is a SUBSTRATE effect: the quantum hardware performs parallel amplitude testing

**Mode 2: Fourier sampling (Shor)**
- Prerequisite: periodic function over a group (Z_N*, Z_p, elliptic curve group)
- K-structure required: global periodicity (multiplicative order)
- Speedup mechanism: QFT maps periodic superposition to peaked frequency distribution; ONE measurement identifies period
- Result: exponent collapses to polynomial (exponential → n^2)
- This is a SUBSTRATE × K-STRUCTURE effect: quantum amplitudes encode all evaluations implicitly; QFT extracts global periodicity in O(n^2) gates

**The interaction is multiplicative, not additive:**
- Quantum substrate alone (no K-structure) → Grover advantage (~constant factor at fixed classical exponent)
- Quantum substrate + periodic K-structure → Shor advantage (exponent collapses entirely)

---

## Implications for gap.md R3

**R3:** What does BQP strictly containing P imply about the substrate-dependence of K-manipulation?

The Shor/Grover comparison extends the Grover answer from a quantitative to a qualitative distinction:

**1. BQP contains problems at TWO levels of K-structure advantage.**

The Grover findings showed BQP ⊃ P implies quantum hardware accesses K-manipulations with
a halved exponent for unstructured search — a substrate-dependent constant in the exponent.

The Shor findings show there is a second regime: BQP contains polynomial-time solutions for
problems with periodic group K-structure, where classical algorithms are subexponential or
exponential. This is not a constant-in-exponent substrate effect — it is a complete collapse
of the exponent. The K-structure and the quantum substrate together achieve what neither alone can:

- K-structure alone (no quantum): classical algorithms find periods in O(sqrt(r)) via birthday paradox — still exponential
- Quantum alone (no K-structure): Grover gives O(2^(n/2)) — exponent halved but not collapsed
- K-structure + quantum: Shor gives O(n^2) — exponent collapses to polynomial

**2. The substrate-dependence is K-structure-conditional.**

Grover's substrate-dependence: universal. Any problem with a binary oracle benefits.
Shor's substrate-dependence: conditional on the problem having group-periodic K-structure.

This means BQP's advantage over P is not uniform — it is concentrated in the subclass of
problems with algebraic K-structure (abelian hidden subgroup problems). The broader structure
of BQP vs P is: quantum hardware is a specialized K-structure detector, not a general speedup engine.

**3. P ≠ NP remains intact, for the right structural reason.**

Factoring is in NP ∩ co-NP but is not NP-complete. The periodic group structure (Z_N*) that
Shor exploits is a GLOBAL algebraic K-structure. NP-completeness (3-SAT, graph coloring, etc.)
is characterized by clause-level or local K-structure — no global period exists. This is why:

- Shor solves factoring: global periodic K-structure is Fourier-extractable
- Grover provides the only quantum speedup on 3-SAT: no global period, only local clause K-gradients
- P ≠ NP is likely safe from quantum algorithms: NP-complete problems lack the algebraic K-structure that quantum Fourier sampling can exploit

**4. Physical interpretation of substrate-dependence.**

Classical computation manipulates K-information sequentially: evaluate f(x), compare, store.
Finding a period of length r requires either:
- Sequential scan: O(r) evaluations
- Birthday paradox: O(sqrt(r)) evaluations — the only classical shortcut

Quantum computation manipulates K-information via physical amplitude interference:
- The state |psi> = sum_{x=0}^{Q-1} |x>|f(x)> is prepared in O(n) oracle calls
- The QFT on the x-register costs O(n^2) gates and transforms the periodic superposition into a peaked distribution over multiples of Q/r
- ONE measurement extracts a frequency; continued-fraction approximation recovers r
- Total cost: O(n^2) — polynomial in the number of bits, exponentially better than classical

The substrate-dependence is: quantum amplitudes physically realize the 2^n-dimensional state
vector implicitly (without storing 2^n numbers explicitly). The QFT on this vector costs O(n^2)
gates because quantum coherence is the computational resource — interference performs the
Fourier analysis for free, using the physical dynamics of the quantum substrate.

**5. Updated K-structure hierarchy (complete picture):**

```
K-structure level:   None           Local/logical    Global periodic
                      |                  |                 |
Classical cost:      O(2^n)        O(2^(n/14)) DPLL   O(exp(n^(1/3))) NFS
Quantum cost:        O(2^(n/2))    O(2^(n/2)) bound   O(n^2) Shor
Quantum advantage:   2^(n/2)       ~2^(n/2)           exp(n^(1/3)) / n^2
Doubling period:     2 vars        ~14 vars (classic)  undefined (poly)
```

The striking result: DPLL (structured classical, k~14) already surpasses Grover (quantum,
unstructured, k=2) for logical K-structure. But no classical algorithm approaches Shor for
global periodic K-structure. The boundary that matters is not "classical vs quantum" but
"global algebraic K-structure vs everything else."

---

## Summary for R3 (complete answer)

> BQP ⊃ P implies two levels of substrate-dependent K-manipulation:
>
> (1) Amplitude amplification: quantum substrate alone halves the exponent for any
>     unstructured search (k: 1 → 2 doubling period). This is a universal but
>     bounded substrate advantage.
>
> (2) Fourier sampling: quantum substrate combined with periodic group K-structure
>     collapses the exponent entirely to polynomial. Shor's algorithm is the
>     canonical example: factoring goes from exp(n^(1/3)) to n^2. This is a
>     conditional, K-structure-dependent advantage — not available for NP-complete
>     problems which lack global algebraic periodicity.
>
> The substrate-dependence of K-manipulation is therefore K-structure-conditional.
> Quantum hardware is a periodic-K-structure detector; the physical dynamics of
> quantum coherence implement Fourier analysis of the computational landscape in
> O(n^2) gates. Classical hardware must search for the K-structure, paying O(sqrt(r))
> for the best classical period-finding algorithm. This asymmetry is exponential and
> is the root of Shor's exponential advantage — not quantum parallelism per se, but
> quantum Fourier sampling of an algebraically structured K-landscape.

---

## Caveats

1. **Shor's algorithm requires coherent quantum hardware.** The O(n^2 log n) gate count
   assumes fault-tolerant quantum computation with negligible decoherence. Real hardware
   imposes error rates that require error correction, increasing the physical qubit count
   by factors of 10^3–10^4. The asymptotic advantage is real; the practical threshold for
   cryptographically relevant n (~2048 bits) requires millions of physical qubits.

2. **NFS complexity is heuristic.** The NFS exponent formula is asymptotically correct but
   heuristically derived; the constant c is not proven. For n < 512 bits, other algorithms
   (Pollard's rho, elliptic curve method) may outperform NFS in practice.

3. **Shor's small-n performance.** At n=10–20, Shor's constant factors make it slower than
   trial division. The crossover occurs around n=25–30. This is an artefact of the asymptotic
   analysis; actual quantum circuit overhead would push the crossover further.

4. **The DFT demonstration is classical.** The script computes a classical DFT of the period
   function values, not a quantum QFT on superposed amplitudes. The classical DFT on M samples
   requires O(M log M) operations (FFT); the quantum QFT on n qubits requires O(n^2) gates.
   The classical DFT is shown to illustrate that the period is visible in frequency space;
   the quantum speedup is that the QFT is applied to a superposition that implicitly encodes
   all M = 2^n samples at once.

5. **Hidden subgroup problem generality.** Shor's algorithm solves the abelian hidden subgroup
   problem (HSP). Non-abelian HSP (graph isomorphism, shortest lattice vector) is open — quantum
   Fourier sampling does not straightforwardly extend. This limits the K-structure classes for
   which the Shor-type exponential advantage is known.
