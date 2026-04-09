---
source: Nemotron
approach: Complete 6-step proof via Fourier diagonalization + concentration of measure
status: MOST COMPLETE — provides a full theorem statement and proof outline
---

## Summary
Nemotron provides the most detailed proof of all responses. It includes a theorem statement and a 6-step proof that claims to close the argument. This is the strongest candidate for the paper.

## The Theorem (Nemotron's formulation)
For any ω_N in the divergence-free subspace V_N with fixed energy ||ω||² = E₀:
```
(1/N^d) · #{x : Q(x) > 0} ≤ C · exp(-cN)
```
where C, c depend only on ν, d, and E₀.

## The 6 Steps

### Step A: Fourier Representation
Q diagonalizes in Fourier space:
```
Q_ω = (1/N^d) Σ_{k≠0} (|k|² - ν|k|⁴) |ω̂_k|²
```
KEY CLAIM: The cross-terms cancel because of divergence-free projection.
The eigenvalue at mode k is: λ(k) = |k|² - ν|k|⁴

**This is the critical equation.** If correct, the proof is straightforward.

### Step B: Low/High Split
Choose cutoff K* = N^α (with 0 < α < 1/2).
- High modes (|k| > K*): λ(k) = |k|² - ν|k|⁴ ≤ -ν|k|⁴/2 for |k| ≥ √(2/ν)
- Bound: Q_H ≤ -c₀ K*² ||ω||²
- Low modes: |Q_L| ≤ K*² ||ω||²
- Combined: Q < 0 unless low-frequency energy is anomalously large

### Step C: Low-Frequency Energy Bound
Using Hoeffding's inequality on independent Fourier phases:
```
P(E_L ≥ τ) ≤ exp(-c₁ N^d τ²)
```
With threshold τ_N = c₀ K*²/2 and K* = N^α:
```
P(E_L ≥ τ_N) ≤ exp(-c₂ N^{d-4α})
```
For α < 1/2 and d = 3: exponent = 3 - 4α > 1. Exponential decay.

### Step D: Pointwise Negativity
If low-frequency energy < threshold, then Q(x) < 0 at EVERY grid point.

### Step E: Concentration of Measure
Levy's lemma: the fraction function F(ω) = (1/N^d)#{Q > 0} is Lipschitz
on the energy sphere, so it concentrates around its mean exponentially.
```
P(|F - EF| > t) ≤ 2 exp(-c N^d t² / ||F||_Lip²)
```
The Lipschitz constant is bounded independent of N.

### Step F: Combine
Mean of F is exponentially small (Step C) + F concentrates (Step E) → F itself is exponentially small for ALL ω.

## Critical Assessment

### STRENGTHS
1. **Complete theorem with proof** — not just a strategy
2. **Deterministic conclusion** — Step E upgrades from probabilistic to ALL fields
3. **The diagonalization (Step A)** is the key simplification
4. **Standard tools** — Hoeffding, Levy's lemma, Parseval
5. **Matches our data** — predicts exp(-cN) which is what we observe

### POTENTIAL ISSUES
1. **Step A: Does Q actually diagonalize?** The claim that cross-terms cancel due to div-free is the crux. The stretching ω·S·ω involves S which depends on ω via Biot-Savart. In Fourier space, ω·S·ω is a CONVOLUTION, not a diagonal multiplication. The diagonalization claim needs careful verification.

2. **The eigenvalue λ(k) = |k|² - ν|k|⁴**: This comes from the stretching symbol being |k|² and the diffusion being ν|k|⁴. But the stretching symbol for ω·S·ω is NOT simply |k|² — it involves the full tensorial structure of the Biot-Savart kernel. Nemotron may be oversimplifying the symbol.

3. **Step E: Lipschitz constant** — claimed to be bounded independent of N. This needs verification. The function F counts indicator functions, which are not smooth. The Lipschitz constant could grow with N.

4. **Fixed energy assumption**: The proof assumes ||ω||² = E₀ is fixed. Our simulations don't fix the energy — the IC energy varies with seed. But this is minor — we can normalize.

### THE BIG QUESTION
Does Q diagonalize in Fourier space for divergence-free fields?

If YES → this proof closes with standard tools.
If NO → the convolution structure makes Steps B-D much harder.

This is the ONE thing to check. If the diagonalization holds, Nemotron has essentially solved it.

## Action Items
1. **VERIFY STEP A**: Check if ω·S·ω diagonalizes for div-free fields
   - Write out the full convolution explicitly
   - Check if div-free constraint kills the cross-terms
   - This is a computation, not a conceptual question
2. If Step A holds: write the full proof following Nemotron's outline
3. If Step A fails: use Grok's fallback (frequency decomposition + Bernstein)
4. Check the Lipschitz constant bound in Step E
5. Compare the predicted decay rate to our measured N_d ≈ 8

## Verdict
If Step A is correct, this IS the proof. The whole argument reduces to:
"Q diagonalizes, the eigenvalue at each mode is |k|² - ν|k|⁴, diffusion dominates at high k, concentration of measure handles the low k, done."

That would be the cleanest proof of NS regularity ever proposed.
Check Step A immediately.
