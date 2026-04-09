# Proof Attempts Summary

## The #1 Question To Resolve
**Does Q diagonalize in Fourier space for divergence-free fields?**

- If YES → Nemotron's proof closes with standard tools (eigenvalue |k|² - ν|k|⁴)
- If NO → Need Manus's heavier machinery (Latala's inequality for trilinear chaos)

Gemini says Q is cubic (suggests no diagonalization).
Nemotron claims cross-terms cancel (diagonalization).
Manus says trilinear, no diagonalization.
Grok sidesteps the issue with spectral convergence.

This is a COMPUTATION we can check in 10 minutes. Do it first.

## Ranking

### 1. Nemotron (004) — IF diagonalization holds
Complete 6-step proof. Theorem statement. Clean. Uses Hoeffding + Levy's lemma.
Risk: the diagonalization claim may be wrong (3 of 5 respondents say Q is trilinear).

### 2. Manus (005) — IF diagonalization fails
Most mathematically rigorous. Handles trilinear structure correctly.
Two tracks (deterministic + probabilistic). Cites relevant literature.
Risk: spectral condition α > d may be marginal for our setup.

### 3. ChatGPT (006) — Best Intuition
Clearest physical explanation: "alignment rarity in high dimensions."
Riesz transform bounds. High-codimension event argument.
Also explains the Taylor-Green plateau (symmetric ICs preserve alignment).
Risk: less detailed, no theorem statement.

### 4. Grok (002) — Fallback
4-step proof via spectral convergence + superlevel geometry.
Doesn't depend on diagonalization. Step 1 (Q_cont ≤ 0) is the assumption.
Risk: Step 1 is essentially the regularity assumption.

### 5. Gemini (001) — Framework
Large deviation + concentration of measure. Good framework but less precise.
Identifies the right paradigm (random fields) but doesn't close the proof.

### 6. Mistral (003) — Supporting
Rayleigh quotient + spectral decomposition. Good intuition but wrong on
polynomial vs exponential decay. Best used for supplementary ideas.

## Consensus Across Models
- 4/5 agree Q is trilinear (cubic in ω), not quadratic. Nemotron is the outlier.
- All agree the mechanism is: dissipation (high-k) dominates stretching (low-k)
- All agree exponential decay comes from concentration of measure or large deviations
- The divergence-free constraint is identified as crucial by all
- ChatGPT uniquely explains WHY symmetric ICs plateau: alignment is preserved by symmetry

## Key References To Add
- Latala (2006) — moments and tails of Gaussian chaoses
- Farhat, Grujic, Leitmeyer (2018) — depletion of nonlinearity in NS
- Logvinenko-Sereda theorem — discrete uncertainty principle

## Overnight Results (10 files, 007-017)

### Resolved Questions
1. **Diagonalization**: FAILS. Q is trilinear, not diagonal. (007)
2. **Latala bound**: FAILS. σ₃ ~ N^4, grows too fast. (009, 010)
3. **Single-mode orthogonality**: PROVEN. ω ⊥ S eigenvector always. cos²θ = 0. (014)
4. **Variance decay**: OBSERVED. var(stretch) drops from N=4 to N=16. (015)
5. **Decorrelation**: PARTIAL. Not Gaussian (kurtosis=10) but variance still decays. (015)

### Proven Lemmas
- **Lemma 1**: Single-mode stretching = 0 (ω exactly perpendicular to strain eigenvector)
- **Lemma 2** (from literature): max enstrophy amplification ≤ C E₀^{3/2}
- **Lemma 3** (standard): Spatial fraction concentrates via Hoeffding

### Surviving Proof Paths (Ranked)
1. **E^{3/2} bound + spatial concentration** (017) — uses ESTABLISHED results
   - Polynomial pointwise bound from known enstrophy estimate
   - Exponential upgrade via Hoeffding on spatial average
   - Cleanest path — builds on published, peer-reviewed bounds

2. **Alignment rarity + phase lag** (011, 013) — geometric argument
   - Single-mode orthogonality provides the mechanism
   - Counting independent alignment constraints gives exp(-cN)
   - Needs decorrelation formalized

3. **Variance decay + Chebyshev** (016) — direct computational approach
   - var(stretch) decreases with N (observed, need to prove)
   - Chebyshev gives polynomial, concentration upgrades to exponential
   - The WHY of variance decay traces to Lemma 1

### Key Literature Found
- arXiv 1909.00041: Maximum enstrophy amplification E₀^{3/2} (usable bound)
- arXiv 2602.15670: Optimal enstrophy bounds, Feb 2026 (must read)
- arXiv 2601.08862: Lagrangian phase lag in strain-vorticity alignment
- arXiv 2409.13125: Anti-twist mechanism regularizes NS turbulence
- Constantin: "depletion of nonlinearity" (established framework)

### The One Remaining Gap
All paths converge to the same question:
**Why does the pointwise stretching-to-dissipation ratio vanish at high resolution?**
- Lemma 1 says single modes contribute zero stretching
- Multi-mode stretching involves triadic convolutions with random phases
- The variance of these convolutions DECAYS (observed) because the
  orthogonality creates systematic cancellation
- Formalizing this cancellation is the last step
