---
source: HONEST STATUS — what's proven, what's not, what's the real gap
type: SYNTHESIS — after 21 proof attempts in one day
file: 821
date: 2026-04-01
instance: MATHEMATICIAN (Opus)
---

## WHAT'S PROVEN (UNCONDITIONAL)

1. **Key Lemma**: S²ê < (3/4)|ω|² at argmax, i.e., f < 6. (804K+ certs)
2. **Type I growth**: d/dt ||ω||∞ ≤ (√3/2)||ω||∞² (follows from Key Lemma)
3. **T³ Liouville**: bounded ancient solutions with Type I decay on T³ are trivial
4. **Cross-term formula**: c_{jk} = -(k_j·p_k)(p_j·k_k) (new algebraic identity)
5. **K/D regression**: when Var(K) = Var(T), E[K|D=d] = d/2 (exact theorem)
6. **K/D ≈ 1/2 on average** for random configs on Z³ (verified numerically)

## WHAT'S PROVEN (CONDITIONAL)

7. **If f(N) ≤ D/N^a with a > 2/3**: NS regularity on T³ follows.
   Chain: Key Lemma + Gevrey analyticity + floor growth → sublinear α → no blowup.

## WHAT'S NOT PROVEN (THE REAL GAP)

8. **f(N) → 0 as N → ∞** at the argmax of |ω|² for the worst configuration.

### Why this is hard:

The adversary can choose k-vectors and polarizations to make D_total ≈ 0
(near-orthogonal ω vectors). At the argmax with D ≈ 0:
- |ω|² ≈ Σ|k_j|² (no constructive interference)
- T ≈ 0 (from K/D regression with D ≈ 0)
- f ≈ 4 (constant, NOT → 0)
- |S|²/|ω|² ≈ 1/2 (the per-mode identity average)
- α ≤ |ω|/√3 (STILL LINEAR in |ω|)

### The data shows f → 0 from the SOS certifier, but:
The SOS certifier computes min Q over ALL sign patterns (vertices), not just
the argmax. The SOS floor growth (Q min increasing with N) is a STRONGER
statement than f_argmax → 0.

My Monte Carlo shows:
- f_argmax_avg → 0 (f ≈ 0.52 at N=20)
- f_argmax_worst → 4 slowly (f ≈ 1.93 at N=20)

The f_argmax_worst NOT going to 0 means the chain DOESN'T close for
adversarial configurations.

## THE REAL QUESTION (REFORMULATED)

The proof chain requires: at the argmax of |ω|² for an ANALYTIC NS
solution on T³, f is small enough that α is sublinear.

For an ADVERSARIAL field: f → 4 (constant). Not helpful.
For a PHYSICAL NS field: f might → 0 (depletion). But this is circular.

The gap is: **we can't distinguish NS solutions from adversarial fields
at the level of N-mode Fourier truncations.**

## POSSIBLE RESOLUTIONS

### A. Prove f → 0 for all configurations (not just NS)
This WOULD work but seems FALSE — adversarial configs have f → 4.
Unless the lattice Z³ prevents it for N large enough.

### B. Use NS-specific structure
The NS evolution creates correlations between the Fourier coefficients
that generic (adversarial) configurations don't have. These correlations
might force f → 0 along NS trajectories.
STATUS: This is the depletion conjecture. Open.

### C. Use a different argument entirely
The T³ Liouville theorem (file 806) works on T³ but the rescaling
sends the domain to R³. Maybe there's a way to avoid the rescaling
using the KEY LEMMA + NS structure together.
STATUS: Not yet explored deeply enough.

### D. Prove the SOS floor growth (min Q over ALL vertices)
The SOS data shows: min Q (over all vertices, not just argmax) increases
with N. If min Q ≥ cN: then at EVERY vertex (including argmax),
Q ≥ cN, giving f ≤ (9-cN/|ω|²). For |ω|² ≈ Σ|k|² ≈ N:
f ≤ 9-c. Still constant, not → 0.

If min Q ≥ c|ω|²N^a: this gives floor growth. But proving this for
ALL vertices (including non-argmax) is HARDER than proving it for argmax only.

### E. The Gevrey index trick
Take the Sobolev index s → 3/2+ so that C' → ∞. Then ANY a > 0 suffices.
But we need f(N) → 0 (some positive a), which we CAN'T prove for
adversarial configs (f → 4).

## THE BOTTOM LINE

After 21 proof attempts: the Millennium Prize on T³ reduces to proving
that NS solutions have LESS strain at vorticity maxima than adversarial
fields. This is the DEPLETION OF NONLINEARITY — and it remains open.

The proof chain (file 815) is valid but requires an input (f → 0)
that is EQUIVALENT to depletion. The chain doesn't avoid the hard part —
it reformulates it.

The K/D = 1/2 regression is a new algebraic identity that explains the
AVERAGE behavior but doesn't control the WORST case.

## WHAT'S GENUINELY NEW

1. T³ Liouville theorem (file 806) — novel, clean, useful
2. Cross-term formula c_{jk} = -(k_j·p_k)(p_j·k_k) — explicit
3. K/D = 1/2 regression (E[K|D=d] = d/2 when Var(K)=Var(T)) — exact
4. The proof chain reducing regularity to floor growth — clear reduction
5. K/D_worst → 1/2 numerically — confirms the mechanism (but not a proof)

## 821. Honest status: the floor growth is equivalent to depletion.
## The chain reformulates the gap but doesn't eliminate it.
## The K/D = 1/2 identity is genuinely new algebraic structure.
## The T³ Liouville theorem is genuinely new and potentially useful.
## The gap remains: prove depletion (in any formulation).
