# Yang-Mills Mass Gap — Numerical Experiments Plan

**Date**: 2026-04-07
**Machine**: DGX Spark (GB10 Blackwell, 128.5GB unified memory)
**Goal**: Computational certification of the mass gap in 4D SU(2) pure gauge theory,
preceding any analytical proof attempt.

---

## 1. What We Measure and How

### 1.1 The Mass Gap on the Lattice

The mass gap Delta is the energy of the lightest glueball state (quantum numbers
J^PC = 0++). On a Euclidean lattice with spacing a, the mass gap appears as the
exponential decay rate of gauge-invariant correlators:

```
C(t) = <O(t) O(0)> ~ A * exp(-m_gap * t)   as t -> infinity
```

where O is a gauge-invariant operator with 0++ quantum numbers and m_gap is the
mass gap in lattice units (dimensionless: am_phys).

### 1.2 Operators for Mass Gap Measurement

**Plaquette-plaquette correlator** (simplest):
```
O(t) = sum_{x,i<j} Re Tr P_{ij}(x,t)
```
where P_{ij}(x,t) is the 1x1 Wilson loop (plaquette) in the (i,j) plane at spatial
position x and Euclidean time t. Sum over all spatial positions projects onto zero
spatial momentum (p=0), which is required to isolate the mass gap.

**Blocked/smeared operators** (better overlap with ground state):
- APE smearing: replace spatial links with weighted average of link + staples
- Variational method: build a basis of operators {O_1,...,O_N} with different
  smearing levels, solve the generalized eigenvalue problem (GEVP)
  C(t) v = lambda(t,t0) C(t0) v
  to extract excited states cleanly.

**Wilson loops W(R,T)** (for string tension):
```
W(R,T) ~ exp(-sigma * R * T)    (area law => confinement)
W(R,T) ~ exp(-V(R) * T)         (V(R) = sigma*R + ... for large R)
```
The string tension sigma is related to but distinct from the mass gap.
Ratio: m_gap / sqrt(sigma) ~ 3.5-4.0 for SU(2) in the continuum limit.

**Polyakov loop correlator** (finite temperature):
```
<L(x) L*(y)> ~ exp(-V(|x-y|) / T)
```
where L(x) = Tr prod_{t} U_0(x,t) is the Polyakov loop.

### 1.3 Extracting the Mass

From the zero-momentum projected correlator C(t):

1. **Effective mass**: m_eff(t) = -ln(C(t+1)/C(t))
   - Should plateau at m_gap for large t
   - In practice, need t > 2-3 to see plateau on coarse lattices

2. **Cosh fit** (for periodic time direction of extent N_t):
   C(t) = A * [exp(-m*t) + exp(-m*(N_t-t))]
   Fit for A, m over a time range where excited states have decayed.

3. **GEVP** (variational): eigenvalues lambda_n(t,t0) ~ exp(-m_n*(t-t0))
   Gives the full low-lying spectrum, not just the ground state.

---

## 2. Standard Parameters from the Literature

### 2.1 Wilson Action for SU(2)

```
S_W = beta * sum_{plaquettes} (1 - (1/2) Re Tr U_P)
```

where beta = 4 / g^2 (for SU(2): beta = 2N/g^2 = 4/g^2) and U_P is the ordered
product of four SU(2) link matrices around the plaquette.

### 2.2 Reference Glueball Masses (from arXiv:2402.03959)

| beta | Volume  | a*sqrt(sigma)  | a*m_G (0++)  | m_G/sqrt(sigma) |
|------|---------|-----------------|--------------|-----------------|
| 2.0  | 10^4    | 0.637(7)        | 1.69(25)     | 2.65(40)        |
| 2.2  | 10^4    | 0.486(3)        | 1.37(9)      | 2.83(19)        |
| 2.4  | 16^4    | 0.287(2)        | 0.85(5)      | 2.98(19)        |
| 2.6  | 24^4    | 0.167(10)       | 0.59(2)      | 3.56(23)        |
| cont.| --      | --              | --           | ~3.7(3)         |

Key observation: as beta increases (lattice gets finer), am_G decreases but
m_G/sqrt(sigma) increases toward its continuum value of approximately 3.7.

### 2.3 Standard Simulation Parameters

**Coarse lattice (quick tests)**:
- beta = 2.2, volume = 8^4 to 12^4
- a ~ 0.18 fm (if sqrt(sigma) ~ 440 MeV)
- am_gap ~ 1.3-1.4 (easily measurable, large signal)
- ~1000 configurations sufficient for 5-10% accuracy

**Medium lattice (scaling study)**:
- beta = 2.4, volume = 16^4 to 20^4
- a ~ 0.11 fm
- am_gap ~ 0.85 (signal decays faster, need more statistics)
- ~2000-5000 configurations

**Fine lattice (approaching continuum)**:
- beta = 2.5-2.6, volume = 24^4 to 32^4
- a ~ 0.06-0.09 fm
- am_gap ~ 0.5-0.7 (challenging, significant noise)
- ~5000-10000 configurations
- Critical slowing down becomes noticeable

---

## 3. Scaling Toward the Continuum

### 3.1 Asymptotic Scaling Formula

The lattice spacing a depends on the bare coupling g^2 = 4/beta through
the two-loop renormalization group equation:

```
a * Lambda_L = (b0 * g^2)^(-b1/(2*b0^2)) * exp(-1/(2*b0*g^2))
```

where for SU(2) pure gauge theory:
```
b0 = 11 / (24 * pi^2)   = 0.04658...    [one-loop]
b1 = 17 / (24 * pi^2)^2 = 0.003097...   [two-loop]
```

These come from the universal beta-function coefficients for SU(N_c) with n_f=0:
```
beta_0 = (11/3) * N_c             =>  22/3   for SU(2)
beta_1 = (34/3) * N_c^2           =>  136/3  for SU(2)
```
with b0 = beta_0/(16*pi^2), b1 = beta_1/(16*pi^2)^2.

### 3.2 Continuum Limit of Observables

A physical mass m_phys in the continuum relates to the lattice measurement as:

```
m_phys = (am_latt) / a = (am_latt) * Lambda_L / (a * Lambda_L)
```

The universal ratio for SU(2):
```
sqrt(sigma) / Lambda_L  ~ 57.5(2.5)      (lattice Lambda, Wilson action)
m_0++ / Lambda_L        ~ 210(20)         (from continuum extrapolation)
m_0++ / sqrt(sigma)     ~ 3.7(3)          (continuum limit)
```

### 3.3 Scaling Test Protocol

To demonstrate continuum scaling:

1. Compute am_gap at beta = 2.2, 2.3, 2.4, 2.5, 2.6
2. Compute a*sqrt(sigma) at the same beta values (from Creutz ratios or potential fits)
3. Form the dimensionless ratio r = m_gap / sqrt(sigma) at each beta
4. Verify r converges to a constant as beta -> infinity (a -> 0)
5. Compare with the two-loop scaling formula: deviations should be O(a^2) corrections

Expected behavior:
```
r(beta=2.2) ~ 2.8
r(beta=2.4) ~ 3.0
r(beta=2.6) ~ 3.5
r(continuum) ~ 3.7
```

The approach to the continuum is from below, with ~20% corrections at beta=2.2.

---

## 4. What Fits on a Single GPU (GB10 Blackwell, 128GB)

### 4.1 Memory per Configuration

An SU(2) matrix is a 2x2 unitary matrix with det=1, parameterizable as:
```
U = a0*I + i*(a1*sigma_1 + a2*sigma_2 + a3*sigma_3)
```
with a0^2 + a1^2 + a2^2 + a3^2 = 1. Storage: 4 real numbers per link.

For a 4D lattice of size L^4:
- Sites: L^4
- Links per site: 4 (one per direction mu=0,1,2,3)
- Reals per link: 4 (quaternion parameterization)
- Bytes per link: 4 * 8 = 32 bytes (float64)

**Memory per gauge configuration = L^4 * 4 * 32 bytes**

| Lattice  | Sites    | Links     | Config (f64) | Config (f32) |
|----------|----------|-----------|--------------|--------------|
| 8^4      | 4,096    | 16,384    | 0.5 MB       | 0.25 MB      |
| 12^4     | 20,736   | 82,944    | 2.5 MB       | 1.3 MB       |
| 16^4     | 65,536   | 262,144   | 8.0 MB       | 4.0 MB       |
| 24^4     | 331,776  | 1,327,104 | 40.5 MB      | 20.3 MB      |
| 32^4     | 1,048,576| 4,194,304 | 128 MB       | 64 MB        |
| 48^4     | 5,308,416| 21,233,664| 648 MB       | 324 MB       |
| 64^4     | 16,777,216|67,108,864| 2.0 GB       | 1.0 GB       |
| 96^4     | 84,934,656|339,738,624|10.4 GB      | 5.2 GB       |
| 128^4    | 268,435,456|1,073,741,824|32.8 GB   | 16.4 GB      |

### 4.2 Working Memory During Updates

The heatbath algorithm updates one link at a time, needing:
- Current configuration: 1x config size
- Staples buffer (6 staples per link in 4D): negligible per-link
- Random number state: negligible
- Correlator accumulators: ~L^3 complex numbers per time slice

For the variational method / GEVP:
- Correlation matrix C_ij(t) for ~5-10 operators: ~100 * N_t complex numbers
- Smeared configurations: multiply config size by number of smearing levels (~3-5)

**Total working memory estimate: ~5-10x one configuration size**

| Lattice | Working memory (f64) | Fits in 128GB? |
|---------|---------------------|----------------|
| 8^4     | 5 MB                | Trivially      |
| 16^4    | 80 MB               | Trivially      |
| 32^4    | 1.3 GB              | Easily         |
| 48^4    | 6.5 GB              | Yes            |
| 64^4    | 20 GB               | Yes            |
| 96^4    | 100 GB              | Barely (f64)   |
| 128^4   | 320 GB              | No             |

**Conclusion**: The GB10 can handle up to 64^4 comfortably, 96^4 in float32.
For SU(2), 64^4 at beta=2.6 is a genuinely useful lattice -- this would be
competitive with published results from the 2000s decade.

### 4.3 Update Cost Estimates

**Heatbath sweep** (one full update of all links):
- 4 * L^4 links to update
- Per link: compute 6 staples (each = 5 SU(2) multiplications) + KP sampling
- SU(2) multiply: ~40 FLOPs (4x4 real multiplies + adds)
- Per link: ~6*5*40 + 100 (sampling) ~ 1300 FLOPs
- Per sweep: 4 * L^4 * 1300 FLOPs

| Lattice | FLOPs/sweep  | Time @ 100 GFLOPS (est.) |
|---------|-------------|--------------------------|
| 8^4     | 21 MFLOP    | 0.2 ms                   |
| 16^4    | 341 MFLOP   | 3.4 ms                   |
| 32^4    | 5.5 GFLOP   | 55 ms                    |
| 48^4    | 27.6 GFLOP  | 0.28 s                   |
| 64^4    | 87.2 GFLOP  | 0.87 s                   |

Note: 100 GFLOPS is conservative for the GB10 in a PyTorch implementation.
A hand-tuned CUDA kernel could be 5-10x faster. Published GPU implementations
on older hardware (Fermi era, 2011) achieved 110 GFLOPS for SU(2) heatbath.
The GB10 should be substantially faster.

**Typical simulation budget**:
- Thermalization: 500-2000 sweeps (with overrelaxation: 1 heatbath + 3-5 OR sweeps)
- Measurement separation: 10-50 combined sweeps (to reduce autocorrelation)
- Total configurations: 1000-10000
- Total sweeps: ~10K-200K

| Lattice | Sweeps  | Wall time (conservative) |
|---------|---------|--------------------------|
| 16^4    | 50,000  | 3 minutes                |
| 32^4    | 50,000  | 45 minutes               |
| 48^4    | 50,000  | 4 hours                  |
| 64^4    | 50,000  | 12 hours                 |

**These are very achievable on the Spark.**

### 4.4 Overrelaxation

For SU(2), overrelaxation is trivial: given staple sum S, replace U -> S_bar * U^{-1} * S_bar
where S_bar = S / |S|. This is a microcanonical reflection that preserves the action
exactly but decorrelates the Markov chain. Standard recipe: 1 heatbath + 4 overrelaxation
sweeps per combined update. Cost: same as heatbath per sweep.

---

## 5. Python/PyTorch Implementation Sketch

### 5.1 Core Data Structure

```python
import torch

class LatticeGauge:
    """4D SU(2) lattice gauge field using quaternion representation."""

    def __init__(self, L: int, T: int = None, device='cuda', dtype=torch.float64):
        T = T or L
        # U[mu, t, x, y, z, 4] -- quaternion (a0, a1, a2, a3)
        # a0^2 + a1^2 + a2^2 + a3^2 = 1
        self.L = L
        self.T = T
        self.U = torch.zeros(4, T, L, L, L, 4, device=device, dtype=dtype)
        # Initialize to identity (cold start): a0=1, rest=0
        self.U[:, :, :, :, :, 0] = 1.0

    def hot_start(self):
        """Random SU(2) initialization."""
        self.U.normal_()
        # Project to unit quaternion
        norm = self.U.norm(dim=-1, keepdim=True)
        self.U /= norm
```

### 5.2 SU(2) Quaternion Algebra

```python
def su2_mul(a, b):
    """Multiply two SU(2) elements in quaternion form. a, b: [..., 4]."""
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return torch.stack([
        a0*b0 - a1*b1 - a2*b2 - a3*b3,
        a0*b1 + a1*b0 + a2*b3 - a3*b2,
        a0*b2 - a1*b3 + a2*b0 + a3*b1,
        a0*b3 + a1*b2 - a2*b1 + a3*b0,
    ], dim=-1)

def su2_dag(a):
    """Hermitian conjugate of SU(2) = (a0, -a1, -a2, -a3)."""
    return a * torch.tensor([1, -1, -1, -1], device=a.device, dtype=a.dtype)

def su2_trace(a):
    """Re Tr(U) = 2*a0 for SU(2) in fundamental rep."""
    return 2 * a[..., 0]
```

### 5.3 Staple Computation (Fully Vectorized)

```python
def compute_staples(U, mu):
    """
    Compute the sum of 6 staples for all links in direction mu.
    Staple for plaquette in (mu, nu) plane:
      Forward: U_nu(x+mu) * U_mu^dag(x+nu) * U_nu^dag(x)
      Backward: U_nu^dag(x+mu-nu) * U_mu^dag(x-nu) * U_nu(x-nu)

    Returns: tensor of shape [T, L, L, L, 4] (quaternion)
    """
    staple_sum = torch.zeros_like(U[mu])
    for nu in range(4):
        if nu == mu:
            continue
        # Forward staple
        U_nu_shifted = torch.roll(U[nu], shifts=-1, dims=mu)     # U_nu(x+mu)
        U_mu_shifted = torch.roll(U[mu], shifts=-1, dims=nu)     # U_mu(x+nu)
        # staple = U_nu(x+mu) * U_mu^dag(x+nu) * U_nu^dag(x)
        s = su2_mul(U_nu_shifted, su2_mul(su2_dag(U_mu_shifted), su2_dag(U[nu])))
        staple_sum += s

        # Backward staple
        U_nu_back = torch.roll(U[nu], shifts=1, dims=nu)         # U_nu(x-nu)
        U_nu_shifted_back = torch.roll(
            torch.roll(U[nu], shifts=-1, dims=mu), shifts=1, dims=nu
        )                                                          # U_nu(x+mu-nu)
        U_mu_back = torch.roll(U[mu], shifts=1, dims=nu)         # U_mu(x-nu)
        # staple = U_nu^dag(x+mu-nu) * U_mu^dag(x-nu) * U_nu(x-nu)
        s = su2_mul(su2_dag(U_nu_shifted_back),
                    su2_mul(su2_dag(U_mu_back), U_nu_back))
        staple_sum += s

    return staple_sum
```

Note: the `dims=mu` argument for torch.roll maps direction mu to tensor dimension:
mu=0 -> dim 0 (T), mu=1 -> dim 1 (X), mu=2 -> dim 2 (Y), mu=3 -> dim 3 (Z).

### 5.4 Wilson Action

```python
def wilson_action(U, beta):
    """Compute Wilson action S = beta * sum_P (1 - (1/2) Re Tr U_P)."""
    S = 0.0
    for mu in range(4):
        for nu in range(mu + 1, 4):
            # U_P = U_mu(x) * U_nu(x+mu) * U_mu^dag(x+nu) * U_nu^dag(x)
            U_nu_shifted = torch.roll(U[nu], shifts=-1, dims=mu)
            U_mu_shifted = torch.roll(U[mu], shifts=-1, dims=nu)
            plaq = su2_mul(U[mu],
                    su2_mul(U_nu_shifted,
                    su2_mul(su2_dag(U_mu_shifted),
                            su2_dag(U[nu]))))
            S += (1.0 - plaq[..., 0]).sum()  # (1 - (1/2)*ReTr) = (1 - a0)
    return beta * S
```

### 5.5 Kennedy-Pendleton Heatbath

```python
def heatbath_update(U, mu, beta):
    """
    Kennedy-Pendleton heatbath update for all links in direction mu.
    Generate U_new from p(U) ~ exp((beta/2) Re Tr(U * S))
    where S is the staple sum.
    """
    S = compute_staples(U, mu)
    # k = |S| (quaternion norm of staple sum)
    k = S.norm(dim=-1, keepdim=True)
    # S_hat = S / |S| (unit quaternion)
    S_hat = S / k.clamp(min=1e-10)

    # Sample a0 from p(a0) ~ sqrt(1-a0^2) * exp(beta * k * a0)
    # Kennedy-Pendleton: use rejection method
    k_flat = k.squeeze(-1)
    shape = k_flat.shape
    device = k_flat.device
    dtype = k_flat.dtype

    a0 = torch.zeros(shape, device=device, dtype=dtype)
    done = torch.zeros(shape, dtype=torch.bool, device=device)

    while not done.all():
        # Generate candidate: x = exp(-2*beta*k) to 1, uniform
        r = torch.rand(shape, device=device, dtype=dtype)
        bk = beta * k_flat / 2.0  # effective coupling
        x = torch.exp(-2.0 * bk) + r * (1.0 - torch.exp(-2.0 * bk))
        candidate = 1.0 + torch.log(x) / bk
        # Reject with probability 1 - sqrt(1 - candidate^2)
        reject_prob = 1.0 - torch.sqrt((1.0 - candidate**2).clamp(min=0))
        accept = torch.rand(shape, device=device, dtype=dtype) > reject_prob
        accept = accept & ~done
        a0[accept] = candidate[accept]
        done = done | accept

    # Generate random direction for (a1, a2, a3) on sphere of radius sqrt(1-a0^2)
    r_vec = torch.randn(*shape, 3, device=device, dtype=dtype)
    r_vec = r_vec / r_vec.norm(dim=-1, keepdim=True)
    r_mag = torch.sqrt((1.0 - a0**2).clamp(min=0)).unsqueeze(-1)
    a_vec = r_vec * r_mag

    # New quaternion before rotation
    U_new = torch.cat([a0.unsqueeze(-1), a_vec], dim=-1)

    # The sampled element is relative to S_hat: actual U = U_new * S_hat^dag
    U[mu] = su2_mul(U_new, su2_dag(S_hat))
```

### 5.6 Overrelaxation

```python
def overrelaxation_update(U, mu):
    """Microcanonical overrelaxation: U -> S_hat * U^dag * S_hat."""
    S = compute_staples(U, mu)
    k = S.norm(dim=-1, keepdim=True)
    S_hat = S / k.clamp(min=1e-10)
    U[mu] = su2_mul(S_hat, su2_mul(su2_dag(U[mu]), S_hat))
```

### 5.7 Correlator Measurement

```python
def plaquette_correlator(U, smearing_steps=0):
    """
    Measure zero-momentum 0++ correlator from plaquette operator.
    Returns C(t) for t = 0, ..., T-1.
    """
    # O(t) = sum_{x,y,z} sum_{i<j spatial} Re Tr P_{ij}(x,t)
    # For 0++: sum over all spatial plaquettes at fixed t
    O_t = torch.zeros(U.shape[1], device=U[0].device, dtype=U[0].dtype)
    for i in range(1, 4):  # spatial directions
        for j in range(i + 1, 4):
            U_j_shifted = torch.roll(U[j], shifts=-1, dims=i)
            U_i_shifted = torch.roll(U[i], shifts=-1, dims=j)
            plaq = su2_mul(U[i],
                    su2_mul(U_j_shifted,
                    su2_mul(su2_dag(U_i_shifted),
                            su2_dag(U[j]))))
            # Sum over spatial volume, keep time index
            O_t += plaq[..., 0].sum(dim=(1, 2, 3))  # sum over x,y,z

    # Connected correlator: C(dt) = <O(t) O(t+dt)> - <O>^2
    O_mean = O_t.mean()
    O_fluct = O_t - O_mean
    T = O_t.shape[0]
    C = torch.zeros(T, device=O_t.device, dtype=O_t.dtype)
    for dt in range(T):
        C[dt] = (O_fluct * torch.roll(O_fluct, shifts=-dt, dims=0)).mean()
    return C

def effective_mass(C):
    """m_eff(t) = -ln(C(t+1)/C(t)) for positive C."""
    ratio = C[1:] / C[:-1]
    return -torch.log(ratio.clamp(min=1e-30))
```

### 5.8 Existing Libraries

| Library | Language | SU(2) | GPU | Notes |
|---------|----------|-------|-----|-------|
| pyQCD   | Python/C++ | Yes (via codegen) | No | Small-scale, pedagogical |
| GPT (lehner/gpt) | Python/C++ | Yes | Yes (Grid) | Full production, MPI+OpenMP+SIMD |
| LatticeQCD.jl | Julia | SU(2)/SU(3) | Partial | 4D, clean implementation |
| LQCD (alfredricker) | Python | SU(2)/SU(3) | No | Pure Python, heatbath reference |
| SU2-Heatbath | C++/Jupyter | SU(2) | No | Reproduces Creutz results |
| Custom PyTorch | Python | Any | Yes | What we build here |

**Recommendation**: Write our own in PyTorch for maximum flexibility and GPU
utilization on the Spark. Use the existing repos as correctness references.
Validate against known beta=2.2 results before attempting anything new.

---

## 6. Experiment Plan (Phased)

### Phase 1: Validation (Week 1) — "Does our code work?"

**Experiment 1.1**: Cold start, thermalization check
- Lattice: 8^4, beta = 2.2
- 1000 heatbath sweeps, measure average plaquette every sweep
- Target: <P> = 0.5768(1) at beta=2.2 (well-known value)
- Time: seconds

**Experiment 1.2**: Plaquette correlator, mass gap extraction
- Lattice: 8^4, beta = 2.2
- 1 HB + 4 OR per combined sweep, 500 thermalization, 5000 measurements
- Measure C(t), extract m_eff
- Target: am_gap ~ 1.3-1.4 (compare with published: 1.37(9))
- Time: ~1 minute

**Experiment 1.3**: Wilson loop, string tension
- Same configurations as 1.2
- Measure W(R,T) for R,T = 1,...,4
- Extract Creutz ratios: chi(R,T) = -ln(W(R,T)*W(R-1,T-1) / W(R-1,T)*W(R,T-1))
- Target: a^2*sigma ~ 0.236(3) at beta=2.2
- Time: ~1 minute

### Phase 2: Scaling Study (Week 2) — "Does it scale correctly?"

**Experiment 2.1**: Multi-beta mass gap
- beta = 2.0, 2.2, 2.3, 2.4, 2.5, 2.6
- Lattice sizes: 8^4, 10^4, 12^4, 16^4, 20^4, 24^4 (respectively)
- 1 HB + 4 OR, 1000 thermalization, 5000 measurements each
- Extract am_gap and a^2*sigma at each beta
- Form r(beta) = m_gap / sqrt(sigma) and verify approach to continuum

**Experiment 2.2**: Finite-volume check
- beta = 2.4, lattice sizes: 12^4, 16^4, 20^4, 24^4
- Verify mass gap is volume-independent (m*L >> 1 required, roughly L > 4/m)
- At beta=2.4, am~0.85, so need L > 5. All sizes should agree.

**Experiment 2.3**: Asymptotic scaling verification
- Plot ln(am_gap) vs 1/beta
- Compare slope with two-loop prediction
- Quantify scaling violations (expect ~10% at beta=2.2, ~3% at beta=2.6)

### Phase 3: Production (Week 3-4) — "Push the limits"

**Experiment 3.1**: Large-volume precision measurement
- beta = 2.5, lattice = 32^4
- 2000 thermalization + 10000 measurements (1 HB + 4 OR per measurement)
- APE smearing + GEVP with 4-5 operators
- Target: 2-3% measurement of am_gap
- Time: ~4-8 hours

**Experiment 3.2**: Maximum lattice
- beta = 2.6, lattice = 48^4
- 5000 thermalization + 20000 measurements
- Target: precision m_gap measurement approaching continuum
- Time: ~2-3 days

**Experiment 3.3**: Excited state spectrum
- beta = 2.4, lattice = 24^4
- GEVP with operators in different J^PC channels
- Target: first 3-4 glueball masses (0++, 2++, 0-+)
- Verify m(2++) / m(0++) ~ 1.4 (known ratio for SU(2))

---

## 7. Rigorous Computation Targets

### 7.1 What Would Count as a "Certificate"?

The mass gap problem requires a PROOF, not a measurement. Monte Carlo gives
statistical evidence, not mathematical certainty. The rigorous analog requires:

1. **Exact transfer matrix diagonalization** for small lattices
2. **Interval arithmetic** bounds on eigenvalues
3. **Rigorous error control** in the continuum extrapolation

### 7.2 Transfer Matrix Approach

The transfer matrix T acts on the Hilbert space H of gauge-invariant states
on a spatial slice. For SU(2) on an L^3 spatial lattice:

```
dim(H) = infinite (continuous gauge group)
```

But after gauge-fixing and truncation (character expansion), the Hilbert space
can be made finite-dimensional. For SU(2), the Peter-Weyl decomposition gives
a basis labeled by spins j = 0, 1/2, 1, 3/2, ... on each link.

Truncation at j_max:
- States per link: (2*j_max + 1) independent characters
- Links per spatial slice: 3 * L^3
- Gauge constraints: one per site (Gauss law)
- dim(H_trunc) ~ (2*j_max + 1)^(3*L^3) / (2*j_max + 1)^(L^3)
               = (2*j_max + 1)^(2*L^3)

| L  | j_max | dim(H_trunc)     | Feasible? |
|----|-------|------------------|-----------|
| 2  | 1     | 3^16 = 43M       | Yes (sparse eigenvalue) |
| 2  | 2     | 5^16 = 1.5e11    | Maybe (Lanczos, months) |
| 2  | 3     | 7^16 = 3.3e13    | No        |
| 3  | 1     | 3^54 = 5.8e25    | No        |

**Conclusion**: Exact diagonalization is feasible only for L=2 with j_max=1 (or maybe 2).
This is a 2^3 = 8-site spatial lattice with 24 links and 8 gauge constraints.

### 7.3 Interval Arithmetic Spectral Bound

For the L=2, j_max=1 truncated transfer matrix:

1. **Construct T** exactly as a ~43M x 43M sparse matrix
2. **Compute top 2 eigenvalues** using verified Lanczos (with interval arithmetic)
3. **Gap = -ln(lambda_1/lambda_0)** gives the mass gap at finite lattice spacing
4. **Bound truncation error**: show higher-j contributions are exponentially suppressed
   at strong enough coupling (this uses analyticity of the heat kernel on SU(2))

The truncation error bound is the key difficulty. At strong coupling (small beta),
the character expansion converges geometrically: contributions at spin j are
suppressed by (beta/4)^(2j). For beta=2.0, the j=1 term is already suppressed
by a factor of ~0.25 relative to j=0.

### 7.4 The Strong Coupling Certificate

Chatterjee (2020) proved rigorously that all lattice gauge theories with compact
gauge group have a mass gap at strong coupling (small beta), and Wilson loops
satisfy the area law. The bound is:

```
Mass gap >= c / a    for beta < beta_c(L)
```

where beta_c is an explicit (but very small) threshold. The gap between this
rigorous beta_c and the physical beta ~ 2.2-2.6 is enormous.

**Our target**: Push the rigorous bound to larger beta using computer-assisted
methods on finite lattices, then extrapolate.

### 7.5 Adversarial Search Analog

For Navier-Stokes, the adversarial search looks for initial data that might blow up.
The Yang-Mills analog:

**"Find a gauge configuration where the transfer matrix gap is smallest."**

This translates to:
- Fix beta and lattice size
- Among all possible boundary conditions / twisted configurations, find the one
  that minimizes the spectral gap of the transfer matrix
- If we can show the minimum gap is still positive, that's a certificate

For small lattices (L=2), this is a finite-dimensional optimization problem
that could be attacked with interval arithmetic + branch-and-bound.

### 7.6 Realistic Rigorous Targets

| Target | Method | Feasibility | Timeline |
|--------|--------|-------------|----------|
| Verify m_gap > 0 at beta=1.0, L=2 | Transfer matrix + interval arith. | HIGH | 2-4 weeks |
| Verify m_gap > 0 at beta=1.5, L=2 | Same + truncation bound | MEDIUM | 1-2 months |
| Verify m_gap > 0 at beta=2.0, L=2 | Needs j_max=2 or better bounds | HARD | Unknown |
| Strong coupling bound for any L | Cluster expansion (Chatterjee-style) | MEDIUM | Analytical |
| Continuum extrapolation with error | Requires multiple lattice sizes | VERY HARD | Long-term |

---

## 8. Summary: What's Achievable

### Immediate (1-2 weeks)
- Working 4D SU(2) lattice code in PyTorch on the Spark
- Validated mass gap measurement at beta=2.2 (matching published values)
- Scaling study across 5-6 beta values demonstrating continuum approach
- Glueball spectrum for 0++, 2++, 0-+ states

### Medium-term (1-2 months)
- Precision measurement at beta=2.5-2.6 on 32^4 and 48^4 lattices
- Transfer matrix construction for L=2 spatial lattice
- Interval arithmetic spectral bound at strong coupling (beta=1.0-1.5)
- Truncation error analysis for the character expansion

### Aspirational (3-6 months)
- Computer-assisted proof of mass gap > 0 at beta=2.0 on L=2
- Lean formalization of the lattice transfer matrix definitions
- Rigorous continuum extrapolation framework
- Connection to the Balaban RG program (Route 1 from attempt_001)

### The honest assessment
The numerical experiments (Phases 1-3) are straightforward and achievable.
The Spark can handle lattice sizes up to 48^4 or 64^4 for SU(2), which is
competitive with dedicated lattice gauge theory groups from ~2010.

The rigorous certificates (Section 7) are much harder. The fundamental obstacle
is that rigorous methods only work at strong coupling (small beta), while the
physical continuum limit is at weak coupling (large beta). Bridging this gap
is essentially the Clay Millennium Prize problem itself. But establishing
rigorous results on L=2 lattices at moderate coupling would be genuinely new
and could inform the analytical approach.

---

## References

Key papers consulted:
- arXiv:2402.03959 — SU(2) dark glueball lattice analysis (2024), contains
  the beta/mass/string tension table used in Section 2.2
- arXiv:2106.00364 — Athenodorou & Teper, SU(N) glueball spectrum (2021),
  definitive scaling study for N=2 through 12
- arXiv:1003.3219 — General heatbath algorithm for pure lattice gauge theory
- Chatterjee, "Yang-Mills on the lattice: New results and open problems"
  (slides, Harvard 2025)
- Tong, "Lattice Gauge Theory" (Cambridge lecture notes, Chapter 4)
- arXiv:1010.4834 — SU(2) lattice gauge theory on Fermi GPUs (2011)

Software references:
- pyQCD: github.com/mspraggs/pyQCD
- GPT: github.com/lehner/gpt
- LQCD: github.com/alfredricker/LQCD
- SU2-Heatbath: github.com/AddingAddict/SU2-Heatbath
