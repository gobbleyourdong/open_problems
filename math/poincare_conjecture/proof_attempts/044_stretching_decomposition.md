---
source: Formal decomposition of stretching at x* using single-mode orthogonality
approach: Exact decomposition → constraint → Lagrange bound → N_eff conjecture
status: PARTIAL — decomposition proved, N_eff scaling under test
---

## Exact Stretching Decomposition (PROVED)

At x* where |ω| achieves its max, with ê = ω(x*)/|ω(x*)|:

### Step 1: Mode-by-mode strain contribution

S(x*) = Σ_k S_k(x*) where S_k is the Biot-Savart strain from mode k.

Each S_k is a 3×3 real symmetric traceless matrix with eigenvalues (λ_k, 0, -λ_k).
The zero eigenvector is ω̂_k_dir = ω_k(x*)/|ω_k(x*)| (single-mode lemma).

### Step 2: Decompose ê relative to each mode

ê = cos(α_k) ω̂_k_dir + sin(α_k) n_k

where α_k = angle between ê and mode k's vorticity direction at x*.

### Step 3: Compute stretching contribution

```
ê · S_k · ê = sin²(α_k) × λ_k × cos(2φ_k)
```

where φ_k is the angle of n_k within S_k's non-null eigenplane.

**Proof:**
- cos²(α_k) term: ω̂_k_dir · S_k · ω̂_k_dir = 0 (lemma)
- Cross term: ω̂_k_dir · S_k · n_k = (S_k ω̂_k_dir) · n_k = 0 (eigenvector with eigenvalue 0)
- sin²(α_k) term: n_k · S_k · n_k = λ_k cos²(φ_k) - λ_k sin²(φ_k) = λ_k cos(2φ_k)
□

### Step 4: Total stretching

```
ê · S(x*) · ê = Σ_k sin²(α_k) × λ_k × cos(2φ_k)
```

This is EXACT. Three factors per mode:
- **sin²(α_k)**: misalignment between ê and mode k's vorticity (0 to 1)
- **λ_k**: strain magnitude from mode k (positive, from Biot-Savart)
- **cos(2φ_k)**: alignment within the perpendicular plane (-1 to +1)

## The Constraint (PROVED)

From the definition ω(x*) = Σ_k ω_k(x*):

```
Σ_k a_k cos(α_k) = 1    (*)
```

where a_k = |ω_k(x*)|/|ω(x*)|.

**Proof:** Take ê · ω(x*) = |ω(x*)| and expand. □

## Three Sources of Depletion

The stretching Σ sin²(α_k) λ_k cos(2φ_k) is reduced below its theoretical
maximum Σ λ_k by three independent mechanisms:

### 1. Null-space depletion (from sin²(α_k) < 1)
The dominant modes have large a_k, which forces cos(α_k) ≥ a_k/Σa_j
(roughly), making sin²(α_k) < 1. The mode that contributes most to
|ω(x*)| contributes LEAST to the stretching.

From Lagrange multiplier optimization of Σ(1-cos²α_k)λ_k subject to (*):
```
Minimum depletion ≥ 1 / Σ_k (a_k²/λ_k) > 0
```

### 2. Sign cancellation (from cos(2φ_k) ≠ +1 for all k)
Different modes have different perpendicular planes (because different k
gives different Biot-Savart geometry). The direction n_k points differently
in each mode's plane. For cos(2φ_k) = +1 for ALL k, n_k must consistently
align with the stretching eigenvector of each S_k — but these point in
different directions.

When φ_k is effectively random: Σ λ_k cos(2φ_k) ~ √(Σ λ_k²) << Σ λ_k

### 3. Maximum constraint (|ω(x*+r)| ≤ |ω(x*)|)
From Buaria: stretching depends on the TWIST of remote vorticity.
Near x*, ω ≈ |ω_max| ê, so twist ≈ 0. The near-field contribution
to stretching is suppressed.

## The N_eff Conjecture

Define: N_eff = (Σ |ω_k(x*)|)² / Σ |ω_k(x*)|² (participation ratio)

**Conjecture:** cos²θ(x*) ≤ C / N_eff^β for some β > 0

GPT suggests β = 1. The argument: more participating modes → harder to
align ê with principal strain → cos²θ shrinks.

### Initial data (t=0, static IC):
```
N=16:  N_eff=638,  cos²θ=0.31,  product=197
N=32:  N_eff=1854, cos²θ=0.27,  product=498
N=64:  N_eff=1859, cos²θ=0.18,  product=337
N=128: N_eff=1856, cos²θ=0.31,  product=567
```

**Problem:** N_eff is constant (~1855) for N ≥ 32 because the IC has
fixed k ≤ 8 content. The cos²θ variation is from different random
seeds and grid resolution effects, not from N_eff changes.

### What the time-evolution data should show:
At later times (t > 0), the NS dynamics cascade energy to higher k,
creating new modes. N_eff should GROW with time. If cos²θ simultaneously
SHRINKS, the conjecture has teeth.

Running on Spark now: N_eff at t=0, 2, 5, 10 for N=16, 32, 64, 128.

## The Two Possible Proof Paths

### Path A: N_eff grows → cos²θ shrinks (dynamic depletion)
If the energy cascade increases N_eff monotonically, and cos²θ ~ 1/N_eff,
then for long enough time, the stretching becomes sub-quadratic:
ê · S · ê ~ |ω|² / N_eff → 0 as N_eff → ∞

This gives regularity via Gronwall.

Problem: N_eff growth depends on the DYNAMICS, not just kinematics.
Need to prove N_eff is monotone increasing along NS trajectories.

### Path B: Geometric depletion (static, resolution-independent)
The cos²θ decrease from 0.37 (N=32) to 0.18 (N=64) might be purely
a RESOLUTION effect: at low N, the maximum point isn't well-resolved,
inflating cos²θ. The true value might be some fixed constant < 1/3
(where 1/3 = random alignment) for ALL smooth div-free fields.

If cos²θ ≤ c < 1 universally, then:
ê · S · ê ≤ c × λ₁ ≤ c × C ||ω||_∞

This gives d/dt ||ω||_∞ ≤ c C ||ω||_∞² - ν × (diffusion)

This is STILL quadratic growth, so Gronwall still gives finite-time
blowup potential. Depletion by a constant factor alone is NOT enough.

### Path C: Combined — depletion + viscosity
At the maximum point: d/dt(|ω|²/2) = ω·S·ω - ν|∇ω|²

The VISCOUS term ν|∇ω|² at the maximum provides additional help.
At x*, the Hessian of |ω|² is negative semidefinite, which constrains
the relationship between |∇ω|² and |ω|².

If we can show: ω·S·ω ≤ (1-δ) × ν|∇ω|² for some δ > 0
(stretching is always less than dissipation by a margin),
then |ω|_max is non-increasing, which is exactly what our data shows.

This would use BOTH the geometric depletion AND the viscosity,
which is consistent with our ν-sweep data: the ratio is 1.0000
for ν ≥ 10⁻⁵ and only slightly above 1 for Euler.

## What the Data Says vs What the Proof Needs

| Observation | Data | Proof Status |
|------------|------|-------------|
| ratio = 1.0000 for curl noise | 50 seeds, N=128 | Needs explanation |
| ratio decreases with N | 1.13→1.07→1.00 | Resolution convergence |
| cos²θ < 1/3 at x* | N=64 mean=0.18 | Measured, not proved |
| Euler ratio ≈ 1.001 at N=128 | 50 seeds | Geometric bound |
| TG ratio > 1 (transient) | N=128 max=4.95 | Expected physics |

## Next Steps
1. N_eff time evolution data (running on Spark)
2. If N_eff grows and product stabilizes → formalize Path A
3. If product is all over the place → Path B or C
4. Either way: write the exact decomposition theorem for the paper
