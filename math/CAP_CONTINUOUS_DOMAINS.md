# Computer-Assisted Proofs on Continuous and Infinite Domains

## Comprehensive Survey for Millennium Prize Applications

**Date**: 2026-04-07
**Context**: Yang-Mills (SU(2) on R^4), Navier-Stokes (R^3 / T^3), Riemann Hypothesis (entire function on C)
**Focus**: Practical techniques implementable in Python with rigorous error bounds

---

## Table of Contents

1. [The Core Problem](#1-the-core-problem)
2. [Interval Arithmetic on Function Spaces](#2-interval-arithmetic-on-function-spaces)
3. [Computer-Assisted Proofs for PDEs](#3-computer-assisted-proofs-for-pdes)
4. [Finite-to-Infinite Extension Techniques](#4-finite-to-infinite-extension-techniques)
5. [Gauge Theory / Lie Groups](#5-gauge-theory--lie-groups)
6. [Noncompact Domains (R^n)](#6-noncompact-domains-rn)
7. [Success Stories](#7-success-stories)
8. [Practical Python Implementation](#8-practical-python-implementation)
9. [Application Map: Which Technique for Which Problem](#9-application-map)

---

## 1. The Core Problem

We have three Millennium Prize problems. Each hits the same wall:

| Problem | Domain | Key Object | Why Brute Force Fails |
|---------|--------|------------|----------------------|
| Yang-Mills | SU(2) (compact 3-manifold) x Z^4 lattice | Transfer matrix T(beta) | Group is continuous; lattice is infinite |
| Navier-Stokes | R^3 or T^3 | Velocity field u(x,t) | Infinite Fourier modes; continuous time |
| Riemann Hypothesis | C (complex plane) | zeta(s) | Infinitely many zeros; continuous domain |

**The fundamental challenge**: proving something holds EVERYWHERE in a continuous set,
not just at sample points. This requires certified enclosures, not approximations.

### What "rigorous" means

A computation is rigorous if:
1. Every floating-point operation uses DIRECTED ROUNDING (round-down for lower bounds,
   round-up for upper bounds)
2. All truncations (Fourier, Taylor, Galerkin) have CERTIFIED REMAINDER BOUNDS
3. The final inequality is MACHINE-VERIFIED (the interval [lo, hi] with lo > 0 proves
   positivity)

Our existing `ns_blowup/interval.py` does (1) using `np.nextafter`. But we lack (2)
and (3) for function spaces.

---

## 2. Interval Arithmetic on Function Spaces

### 2.1 Taylor Model Arithmetic

**Core idea**: Represent a function f on [a,b] as f(x) = P(x) + Delta, where P is a
polynomial of degree n and Delta is an INTERVAL containing the remainder.

```
Taylor Model: TM(f) = (P_n(x), [delta_lo, delta_hi])

Guarantee: for ALL x in [a,b], f(x) in P_n(x) + [delta_lo, delta_hi]
```

**Why this is better than plain interval arithmetic**: Plain IA on "x * (1-x)" over
[0,1] gives [0,1]*[0,1] = [0,1], but the true range is [0, 0.25]. Taylor models
track the polynomial structure symbolically and only intervalize the remainder.

**Operations on Taylor models**:
- Addition: (P1, D1) + (P2, D2) = (P1+P2, D1+D2)
- Multiplication: (P1, D1) * (P2, D2) = (trunc_n(P1*P2), D1*B(P2) + D2*B(P1) + D1*D2 + remainder)
  where B(P) bounds P on the domain and trunc_n keeps degree <= n
- Composition: chain rule on polynomials + remainder propagation
- Division, sqrt, exp, etc.: via Taylor expansion + interval remainder

**Wrapping effect**: The key advantage over plain intervals. Taylor models resist the
"wrapping effect" because polynomial correlations between variables are preserved
symbolically. Only truly nonlinear/truncation errors go into Delta.

**Convergence**: For analytic f on [a,b], the remainder Delta shrinks as O(h^{n+1})
where h = b-a is the domain width. Subdivide [a,b] into M pieces for O((h/M)^{n+1}).

**Tools**:
- TaylorModels.jl (Julia): mature, well-tested
- INTLAB (MATLAB): Rump's toolbox, has Taylor model support
- Custom Python: straightforward to build on our interval.py

**Relevance to our problems**:
- NS: Enclose the nonlinear term u . grad(u) as a Taylor model in Fourier coefficients
- YM: Enclose Bessel functions I_n(beta) in the character expansion
- RH: Enclose zeta(s) along the critical strip using Taylor models in Im(s)

### 2.2 Chebyshev Polynomial Enclosures

**Core idea**: Expand f in Chebyshev polynomials T_k(x) on [a,b]. The Chebyshev
coefficients decay like O(rho^{-k}) for analytic f, where rho is the Bernstein
ellipse radius. Truncate at degree N, bound the tail.

```
f(x) = sum_{k=0}^{N} c_k T_k(x) + R_N(x)

|R_N(x)| <= sum_{k=N+1}^{infty} |c_k| <= C * rho^{-N} / (rho - 1)
```

**Why Chebyshev over Taylor**:
- Near-minimax approximation (within factor of (4/pi)*ln(N) of optimal)
- No Runge phenomenon (unlike high-degree Taylor at equispaced points)
- Coefficients computable via FFT in O(N log N)
- Rigorous tail bound from coefficient decay rate

**Validated Chebyshev method (Brisebarre-Joldes)**:
1. Compute Chebyshev coefficients c_0, ..., c_N using interval FFT
2. Each c_k is an interval (from rounding during FFT)
3. Bound |c_k| for k > N using analyticity (Bernstein ellipse argument)
4. Total enclosure: polynomial with interval coefficients + tail bound

**Python implementation**: mpmath has `chebyfit()` which returns max absolute error.
For rigorous use, replace all operations with interval arithmetic.

**Relevance**:
- RH: Approximate zeta(1/2 + it) by Chebyshev polynomials in t over [0, T], with
  rigorous tail bound. Verify no zeros leave the critical line.
- NS: Chebyshev-in-time, Fourier-in-space discretization with validated bounds

### 2.3 Verified ODE Solvers

Three major libraries exist for RIGOROUS ODE integration:

**CAPD (Computer Assisted Proofs in Dynamics)**:
- C++ library from Jagiellonian University (Kapela, Zgliczynski, Wilczak)
- Lohner algorithm: Taylor method + QR wrapping for enclosure propagation
- Handles stiff systems via implicit methods
- Used in Tucker's Lorenz proof
- Computes rigorous C^k bounds on the flow map

**VNODE-LP (Validated Numerics for ODE, Lohner-Prothero)**:
- C++ solver by Nedialkov (McMaster)
- Interval Hermite-Obreschkoff methods (high order)
- Produces guaranteed enclosures of ODE solution at each time step
- Handles initial value problems on [t0, t_final]
- Tight enclosures even over long time intervals

**AWA (Automatic Workbench for Analysis)**:
- Older tool, less maintained
- Automatic differentiation + interval arithmetic

**The Lohner algorithm (core of CAPD and VNODE)**:
```
Input: ODE y' = f(y), initial enclosure Y_0, time step h
1. Compute rough enclosure Y_rough containing solution for [t, t+h]
   (using Picard-Lindelof or mean value theorem)
2. Compute Taylor coefficients of solution using automatic differentiation
3. Tight enclosure: Y(t+h) = sum_{k=0}^{p} h^k f^[k](Y_0) + h^{p+1} f^[p+1](Y_rough)
4. QR-factored coordinate change to minimize wrapping
```

**Python situation**: No native Python verified ODE solver exists. Options:
- Call CAPD/VNODE via subprocess or ctypes
- Use mpmath with manual error tracking (slow but works)
- Build a basic Lohner algorithm on our interval.py (feasible for low dimensions)

**Relevance**:
- NS (Leray frame): Integrate the Leray-rescaled PDE forward with rigorous bounds
  to find/exclude periodic orbits. This is exactly the Newton-Krylov plan but with
  certified integration.
- YM: Integrate the RG flow of coupling constants with rigorous bounds

---

## 3. Computer-Assisted Proofs for PDEs

### 3.1 The General Framework (Nakao-Plum-Watanabe)

**The bible**: "Numerical Verification Methods and Computer-Assisted Proofs for
Partial Differential Equations" (Nakao, Plum, Watanabe, 2019, Springer). This is
THE reference for everything below.

**The meta-algorithm**:
```
1. Compute an APPROXIMATE solution u_h (finite element, spectral, etc.)
2. Define a fixed-point operator T such that u = T(u) iff u solves the PDE
3. Define the Newton-like operator:
     T_N(u) = u - A^{-1}(F(u))
   where A approximates the Frechet derivative F'(u_h)
4. Show T_N is a CONTRACTION on a ball B(u_h, r) in a Banach space
5. By Banach fixed-point theorem: unique solution exists in B(u_h, r)
```

The key technical challenges are:
- Constructing A^{-1} (need to invert the approximate linearization rigorously)
- Bounding ||T_N(u) - T_N(v)|| (the contraction constant)
- Bounding ||T_N(u_h) - u_h|| (the defect / residual)

### 3.2 The Plum Method (Eigenvalue Enclosure/Exclosure)

**Problem**: To verify that the linearized operator L = F'(u_h) is invertible, we
need to know its eigenvalues don't cross zero. For infinite-dimensional operators,
this requires:

1. **Enclosure**: Compute rigorous bounds on eigenvalues of the Galerkin
   approximation L_N (N x N matrix). Use interval arithmetic for the eigenvalue
   computation.

2. **Exclosure**: Prove no eigenvalues exist in certain regions of C. The key
   inequality:
   ```
   ||L u - lambda u|| >= delta(lambda) * ||u||
   ```
   for all u in the domain of L and for lambda in the exclosure region.

3. **Infinite-dimensional gap**: Bound the distance between eigenvalues of L_N and
   the true operator L using a priori estimates:
   ```
   |lambda_k(L) - lambda_k(L_N)| <= C * h^{2s} / k^{2s/d}
   ```
   where h is the mesh size, s is the Sobolev regularity, d is the dimension.

**The Plum recipe for semilinear elliptic BVP -Delta u + g(u) = 0**:
```
1. Compute u_h (FEM approximation)
2. Linearize: L = -Delta + g'(u_h)
3. Compute eigenvalues of L_N (Galerkin) with interval arithmetic
4. Bound gap between L_N eigenvalues and L eigenvalues
5. If smallest eigenvalue of L bounded away from 0: L is invertible
6. Bound ||(L)^{-1}|| using eigenvalue lower bound
7. Verify contraction: ||I - A^{-1}L|| < 1 on B(u_h, r)
```

**Relevance**:
- NS stationary: Prove existence of stationary NS solutions in 3D (Watanabe 2021
  did this for specific domains)
- YM: The transfer matrix is a positive operator. Bounding its spectral gap is
  exactly eigenvalue enclosure.

### 3.3 The Nakao Method (Finite Element + Constructive Estimates)

**Key innovation**: Avoid computing eigenvalue enclosures entirely by using
constructive a priori error estimates for FEM.

**Setup**: Solve -Delta u = f on domain Omega with Dirichlet BC.

The Nakao method uses:
```
1. Compute u_h (FEM solution on mesh with size h)
2. Compute residual: rho = f - (-Delta u_h) [in some negative Sobolev norm]
3. Use CONSTRUCTIVE Poincare/Aubin-Nitsche inequalities:
     ||u - u_h||_{H^1} <= C_P * h * ||rho||_{L^2}
   where C_P is a COMPUTABLE constant (not just "some C")
4. For the nonlinear problem: use the contraction mapping theorem
   with these computable constants
```

**Why "constructive" matters**: Classical PDE theory says ||u - u_h|| = O(h^k) with
"some constant C." That's useless for a proof. Nakao's method computes C EXPLICITLY.

**Relevance**:
- NS: The Stokes operator on T^3 has KNOWN eigenvalues (|k|^2 for each Fourier mode).
  The Poincare constant is 1/(2*pi) on the unit torus. These are exact, no computation
  needed. This makes NS on T^3 the easiest domain for Nakao-type methods.
- YM: The lattice Laplacian has known eigenvalues. Constructive estimates are feasible.

### 3.4 The Radii Polynomial Approach (Lessard, van den Berg, Mireles-James)

**This is the most powerful modern technique for CAP on PDEs.**

**Core idea**: Reformulate the PDE as a zero-finding problem F(x) = 0 in a Banach
space of sequences (Fourier/Chebyshev coefficients). Apply a Newton-like operator
and verify contraction using the "radii polynomial."

**Setup**:
```
Banach space: X = l^1_s = {(a_k)_{k in Z^d} : ||a||_s = sum |a_k| * |k|^s < infty}
              (weighted l^1 space with algebraic weight |k|^s)

PDE: F(a) = 0  where a = (a_k) are Fourier coefficients

Newton operator: T(a) = a - A * F(a)
                 where A approximates (DF(a_bar))^{-1} at numerical solution a_bar
```

**The radii polynomial**:
```
Define three bounds:
  Y_0 = ||T(a_bar) - a_bar|| = ||A * F(a_bar)||   (defect)
  Z_0 = ||I - A * DF(a_bar)||                       (approximate inverse quality)
  Z_1(r) = sup_{||b||<=r} ||A * (DF(a_bar + b) - DF(a_bar))||  (nonlinearity)

The radii polynomial: p(r) = Z_1 * r^2 + (Z_0 - 1) * r + Y_0

If p(r) < 0 for some r > 0, then:
  - T is a contraction on B(a_bar, r)
  - By Banach FPT, unique solution exists in B(a_bar, r)
  - The solution is at most r away from our numerical approximation
```

**Why this works for infinite dimensions**:
- The approximate inverse A is a FINITE matrix (N x N) plus the identity on modes > N
  (the "tail" is handled by the diagonal dominance of the Laplacian)
- Z_0 splits into a FINITE part (interval arithmetic on N x N matrix) and a TAIL part
  (analytic bound using algebraic decay of coefficients)
- Z_1 involves bounding convolutions, which is where l^1_s pays off
  (convolution in l^1_s is just multiplication of norms)

**The recipe**:
```python
# Pseudocode for radii polynomial approach
def verify_solution(a_bar, N, s):
    """a_bar: numerical Fourier coefficients (N modes)
       N: truncation, s: Sobolev weight"""

    # Step 1: Compute approximate inverse A (N x N + tail)
    DF_N = compute_jacobian(a_bar, N)  # N x N matrix, interval arithmetic
    A_N = interval_inverse(DF_N)        # rigorous inverse

    # Step 2: Y_0 bound (defect)
    residual = A_N @ F(a_bar)  # interval arithmetic
    Y0 = interval_norm(residual, s)  # ||A*F(a_bar)||_s

    # Step 3: Z_0 bound (approximate inverse quality)
    # Finite part: ||I_N - A_N * DF_N(a_bar)||
    Z0_finite = interval_operator_norm(eye(N) - A_N @ DF_N)
    # Tail part: ||I_tail - tail(DF)||, using Laplacian dominance
    Z0_tail = bound_tail_inverse_defect(a_bar, N, s)
    Z0 = max(Z0_finite, Z0_tail)

    # Step 4: Z_1 bound (nonlinearity)
    Z1 = bound_nonlinear_variation(a_bar, N, s)

    # Step 5: Check radii polynomial
    # p(r) = Z1*r^2 + (Z0-1)*r + Y0 < 0?
    discriminant = (1-Z0)**2 - 4*Z1*Y0
    if discriminant > 0 and Z0 < 1:
        r_min = ((1-Z0) - sqrt(discriminant)) / (2*Z1)
        r_max = ((1-Z0) + sqrt(discriminant)) / (2*Z1)
        return True, r_min  # Solution exists in B(a_bar, r_min)
    return False, None
```

**Key papers**:
- van den Berg, Lessard, "Rigorous numerics in dynamics" (2015)
- Hungria, Lessard, Mireles-James, "Rigorous numerics for analytic solutions" (2017)
- Lessard, "Rigorous Numerics for ill-posed PDEs: Periodic Orbits in the Boussinesq
  Equation" (2017) — proves PERIODIC ORBITS exist using radii polynomial

**Relevance**:
- **NS periodic orbits in Leray frame**: This is the EXACT technique needed for our
  Newton-Krylov plan. Instead of just numerically finding periodic orbits, PROVE they
  exist using the radii polynomial. A periodic orbit in Leray frame = DSS blowup.
- **YM transfer matrix fixed point**: The dominant eigenfunction of the transfer matrix
  satisfies T*psi = lambda*psi. Reformulate as F(psi, lambda) = 0 and apply radii
  polynomial.

### 3.5 Homotopy Continuation with Rigorous Bounds

**Core idea**: Connect an easy problem (whose solutions are known) to the hard problem
via a continuous parameter t in [0,1]. Track solutions as t varies.

```
H(x, t) = (1-t) * G(x) + t * F(x)

G(x) = 0 has known solutions x_0^(1), ..., x_0^(k)
F(x) = 0 is the target problem
```

**Making it rigorous (Krawczyk method)**:
At each step along the homotopy, verify the solution still exists using interval
Newton or radii polynomial. This certifies the path from t=0 to t=1.

**Bifurcation detection**: If the Jacobian becomes singular along the path, the
solution may bifurcate. Interval methods detect this (the Krawczyk test fails).

**Tools**: PHCpack, Bertini (numerical), alphaCertified (rigorous certification)

**Relevance**:
- YM: Homotopy from strong coupling (beta -> 0, mass gap proven by OS cluster
  expansion) to weak coupling (beta -> infinity, mass gap from asymptotic freedom).
  If no bifurcation along the path => mass gap for ALL beta. This is essentially
  the convexity/analyticity route (Route 3 in gap.md).

---

## 4. Finite-to-Infinite Extension Techniques

This is the CRITICAL section. Every CAP method works on finitely many degrees of
freedom. The question is: how do you extend the finite certificate to infinity?

### 4.1 Galerkin Truncation + Tail Bounds

**The standard approach for spectral methods on PDEs.**

Decompose the solution: u = u_N + u_tail, where u_N has N Fourier modes and u_tail
is the remainder.

**Step 1: Solve the Galerkin system** (N modes, interval arithmetic)
```
P_N F(u_N) = 0   (project PDE onto first N modes)
```

**Step 2: Bound the tail** using the equation for u_tail:
```
(I - P_N) F(u_N + u_tail) = 0

=> L_tail u_tail = -(I - P_N) F(u_N) - (I - P_N) N(u_N, u_tail)
```
where L_tail is the linear part (Laplacian on high modes) and N is the nonlinearity.

**Step 3: The key inequality**:
```
||u_tail||_s <= ||(L_tail)^{-1}|| * (||(I-P_N) F(u_N)||_s + C * ||u_tail||_s^2)
```

For elliptic operators, ||(L_tail)^{-1}|| ~ 1/lambda_{N+1} where lambda_{N+1} is
the (N+1)-th eigenvalue. Since lambda_k ~ k^2 (Laplacian), the tail inverse shrinks
like 1/N^2.

**The boot**: If N is large enough, the quadratic term is small and the inequality
gives ||u_tail||_s <= C/N^{2-d/2} (roughly). This makes the tail negligible.

**Relevance**:
- **NS on T^3**: lambda_k = 4*pi^2*|k|^2. The eigenvalues are KNOWN EXACTLY.
  ||L_tail^{-1}|| = 1/(4*pi^2*(N+1)^2). Take N = 100: tail inverse < 0.00003.
  The tail is TINY. This is why NS on T^3 is the best setting for CAP.
- **YM character expansion**: lambda_j = j(j+1) (Casimir). Same structure.

### 4.2 Lyapunov Functions via SOS + SDP

**For proving stability/boundedness of dynamical systems.**

**Core idea**: Find a polynomial V(x) >= 0 with dV/dt <= -epsilon*V along trajectories.
The search for V is cast as a Sum-of-Squares (SOS) feasibility problem, solved by
semidefinite programming (SDP).

```
V(x) = x^T Q x   (quadratic Lyapunov, simplest case)

Require: V(x) >= 0     <=> Q is positive semidefinite
         dV/dt <= 0     <=> some LMI condition

For polynomial systems x' = f(x):
  dV/dt = grad(V) . f(x)   (a polynomial if V and f are polynomials)

  dV/dt is SOS-negative  <=> it can be written as -sum of squares
  <=> there exists a PSD matrix such that dV/dt = -z^T M z
  <=> M is feasible in an SDP
```

**Scaling to PDEs**: For Galerkin truncations, the state space is R^N (N Fourier
modes). The Lyapunov function is polynomial in the Fourier coefficients. SOS
certificates scale as O(N^{2d}) where d is the polynomial degree — expensive but
feasible for moderate N.

**Tools**:
- SOSTOOLS (MATLAB) — automates SOS -> SDP conversion
- DSOS/SDSOS (Ahmadi-Majumdar) — scalable alternatives using LP instead of SDP
- scs, MOSEK — fast SDP solvers callable from Python (via cvxpy)

**Relevance**:
- **NS**: Prove enstrophy bounds for the Galerkin-truncated NS equations using SOS
  Lyapunov. This gives rigorous energy estimates for N modes. Combined with tail
  bounds (4.1), extends to the full PDE.
- **This is what our 1.33M SOS certificates do** for the strain-vorticity problem,
  but those are FINITE. The extension to infinite modes requires the Galerkin + tail
  framework.

### 4.3 Compactness Arguments

**The physicist's favorite trick, made rigorous.**

**Rellich-Kondrachov**: The embedding H^1(Omega) -> L^2(Omega) is COMPACT for
bounded Omega. This means: bounded sequences in H^1 have convergent subsequences
in L^2.

**How to use it for finite-to-infinite extension**:
```
1. Prove an a priori bound: ||u||_{H^1} <= M  (using energy estimates + interval arith)
2. By Rellich-Kondrachov: the set {u : ||u||_{H^1} <= M} is compact in L^2
3. Compact sets can be covered by FINITELY many balls
4. Check the property on each ball (finite computation!)
```

**Quantitative compactness**: Need to know HOW MANY balls. The covering number
N(epsilon, K, L^2) for K = {u : ||u||_{H^s} <= M} in L^2 satisfies:
```
log N(epsilon, K, L^2) ~ M^{d/s} / epsilon^{d/s}   (Kolmogorov-Tikhonov)
```
For d=3, s=1: N ~ (M/epsilon)^3. Manageable if M is moderate.

**Relevance**:
- **NS regularity**: If ||omega||_{L^2} <= M (bounded enstrophy), the set of possible
  velocity fields is compact. Finitely many checks suffice.
- **YM on finite lattice**: The gauge group SU(2)^{|edges|} is COMPACT. No need for
  compactness arguments — the domain is already compact. The challenge is the
  INFINITE VOLUME limit.

### 4.4 Bootstrapping

**Prove a bound on N modes, use it to bound mode N+1, iterate.**

**The induction scheme**:
```
Base case: ||u_k|| <= B_k for k = 1, ..., N  (by direct computation)

Inductive step: The PDE for mode N+1 is:
  (lambda_{N+1} + partial_t) u_{N+1} = sum_{j+k=N+1} c_{jk} u_j u_k

  => |u_{N+1}| <= (1/lambda_{N+1}) * sum_{j+k=N+1} |c_{jk}| |u_j| |u_k|
                <= (1/lambda_{N+1}) * C * (max_{k<=N} B_k)^2

  If lambda_{N+1} grows fast enough (like (N+1)^2 for Laplacian),
  B_{N+1} = C * B_N^2 / (N+1)^2 < B_N for large N.
```

**When it works**: When the linear part (eigenvalues) grows faster than the
nonlinear coupling can feed energy to high modes. This is exactly the condition
for regularity in PDEs.

**When it fails**: When energy cascades to high modes (turbulence). The nonlinear
coupling overwhelms the dissipation. This is the NS blowup question.

**Relevance**:
- **NS**: Bootstrap works IF you can prove the enstrophy stays bounded. The open
  question is precisely whether the bootstrap closes.
- **YM (Balaban)**: The Balaban program IS a bootstrap over RG scales. It fails
  because the large-field entropy grows exponentially (attempt_005). The bootstrap
  doesn't close after infinitely many steps.

---

## 5. Gauge Theory / Lie Groups

### 5.1 Peter-Weyl Expansion on Compact Groups

**The Fourier transform for Lie groups.**

For G = SU(2), any L^2 class function f : G -> C expands as:
```
f(U) = sum_{j=0,1/2,1,...} d_j * c_j * chi_j(U)

where:
  j = spin label (j = 0, 1/2, 1, 3/2, ...)
  d_j = 2j+1 (dimension of irrep)
  chi_j = character of spin-j representation
  c_j = Fourier-Peter-Weyl coefficient
```

For the lattice gauge theory heat kernel (Wilson action):
```
exp(beta/2 * Tr(U)) = sum_j d_j * a_j(beta) * chi_j(U)

a_j(beta) = I_{2j+1}(beta) / I_1(beta)   (Bessel function ratio)
```

**This is what `numerics/su2_character_expansion.py` computes.** The coefficients
a_j(beta) decay EXPONENTIALLY for large j:
```
a_j(beta) ~ (beta / (4j+2))^{2j+1} * exp(beta) / I_1(beta)

For j >> beta: a_j(beta) ~ (e*beta/(4j))^{2j}  (Stirling)
```

### 5.2 Representation-Theoretic Truncation with Remainder Bounds

**Key technique**: Truncate the Peter-Weyl expansion at j_max and RIGOROUSLY bound
the remainder.

```
f(U) = sum_{j=0}^{j_max} d_j c_j chi_j(U) + R_{j_max}(U)

|R_{j_max}| <= sum_{j > j_max} d_j |c_j| |chi_j(U)|
             <= sum_{j > j_max} d_j^2 |c_j|     (since |chi_j(U)| <= d_j)
```

For the Wilson action: |c_j| = a_j(beta) and the tail sum converges geometrically:
```
|R_{j_max}| <= sum_{j > j_max} (2j+1)^2 * a_j(beta)

For j_max >> beta: the sum is bounded by C * (e*beta/(4*j_max))^{2*j_max}
```

**This means**: for fixed beta, choosing j_max = O(beta) gives EXPONENTIALLY small
remainder. The Peter-Weyl truncation is incredibly efficient for compact groups.

**Rigorous implementation**:
```python
# Bound the tail of the Peter-Weyl expansion
def bound_pw_tail(beta, j_max):
    """Rigorous upper bound on sum_{j > j_max} d_j^2 * a_j(beta)."""
    # Use interval arithmetic for Bessel functions
    I1 = interval_bessel_i(1, beta)
    tail = Interval(0)
    # Sum until terms are below machine epsilon
    for j_idx in range(2*j_max + 1, 200):
        j = j_idx / 2
        d_j = Interval(2*j + 1)
        I_n = interval_bessel_i(int(2*j+1), beta)
        term = d_j**2 * I_n / I1
        tail = tail + term
        if term.hi < 1e-100:
            break
    # Bound remaining geometric tail
    tail = tail + geometric_tail_bound(beta, j_idx)
    return tail
```

**Relevance**:
- **YM transfer matrix**: The transfer matrix in the character basis is BLOCK DIAGONAL
  (one block per representation j). Each block is finite-dimensional. Truncating at
  j_max gives a finite matrix whose spectral gap approximates the true gap, with
  rigorous error from the tail bound.
- **YM partition function**: Z = product over plaquettes of character expansion sums.
  Truncate each sum and bound the error.

### 5.3 Heat Kernel Bounds on Compact Lie Groups

The heat kernel on SU(2) (with bi-invariant metric) has an explicit expansion:
```
K_t(U) = sum_j d_j^2 * exp(-t * j(j+1)) * chi_j(U) / d_j

where j(j+1) is the Casimir eigenvalue (Laplacian on SU(2)).
```

**Exponential decay in j**: The factor exp(-t * j(j+1)) decays faster than any
polynomial. For fixed t > 0, only O(1/sqrt(t)) terms contribute significantly.

**Relevance**: The Wilson action at coupling beta corresponds to heat kernel at
time t = 1/beta. At weak coupling (large beta, small t), many representations
contribute. At strong coupling (small beta, large t), only j=0 matters.

### 5.4 Character Expansion Convergence Rates

**Key result for YM**: The convergence rate of the character expansion determines
how many modes we need for a given accuracy.

For SU(2) with Wilson action at coupling beta:
```
Number of significant modes: j_max ~ sqrt(beta)   (from Bessel asymptotics)

Truncation error at j_max: ~ exp(-c * j_max^2 / beta)
```

For the Tomboulis inequality (5.15), we need to compare Z and Z+ to relative
precision better than their gap. If Z/Z+ = 1 + delta, we need truncation error
<< delta. At weak coupling, delta shrinks, requiring more modes.

**The MK decimation makes this worse**: After k decimation steps, the effective
coupling changes and the required j_max may grow. Need to track truncation error
through the entire RG flow.

---

## 6. Noncompact Domains (R^n)

### 6.1 Weighted Sobolev Spaces

**Problem**: On R^n, the Sobolev embedding H^1 -> L^2 is NOT compact (no
Rellich-Kondrachov). Solutions can "escape to infinity."

**Fix**: Use weighted norms that penalize behavior at infinity:
```
||u||_{H^s_w}^2 = integral |u(x)|^2 * w(x)^2 * (1 + |x|^2)^s dx

Common weights:
  w(x) = (1 + |x|^2)^{-alpha/2}   (polynomial decay)
  w(x) = exp(-|x|^2/2)             (Gaussian)
  w(x) = (1 + |x|)^{-n}            (critical decay)
```

**Compact embedding**: H^s_w(R^n) -> L^2_w(R^n) IS compact if the weight decays
fast enough (roughly, w -> 0 at infinity).

**Relevance**:
- **YM on R^4**: Physical solutions have finite action: S = integral |F|^2 d^4x < infty.
  This is a weighted L^2 condition. The finite-action condition provides the compactness
  needed for the infinite-volume limit.
- **NS on R^3**: Solutions with finite energy live in L^2(R^3). The energy inequality
  provides compactness in time.

### 6.2 Kelvin Transform (Compactify R^n -> S^n)

**The conformal trick**: The Kelvin transform K maps R^n to itself via inversion
through the unit sphere:
```
K: x -> x / |x|^2

u(x) -> u_hat(y) = |y|^{2-n} * u(y / |y|^2)
```

For R^4 -> S^4: The stereographic projection compactifies R^4 to the 4-sphere.
The Yang-Mills equations are CONFORMALLY INVARIANT in 4D:
```
The YM action integral |F|^2 d^4x is invariant under conformal maps.
```

This means: a solution on R^4 with finite action maps to a solution on S^4, and
vice versa. S^4 is COMPACT, so we can use all the compact-domain tools.

**Relevance**:
- **YM**: Instantons on R^4 correspond to connections on S^4 via the BPST construction.
  The mass gap question on R^4 can potentially be reformulated on S^4. BUT: the
  lattice regularization doesn't respect conformal symmetry, so this helps only for
  the continuum theory.

### 6.3 Self-Similar Variables

**Transform the PDE so that blowup maps to a bounded problem.**

For NS in Leray self-similar variables:
```
Physical: u(x, t), x in R^3, t in [0, T*)
Leray:    U(xi, tau), xi = x/sqrt(T*-t), tau = -ln(T*-t)

Physical blowup (t -> T*) becomes tau -> infinity in Leray frame.
Type I blowup: U -> fixed point (steady state)
Type II blowup: U -> periodic orbit
```

**Key advantage**: In Leray coordinates, the spatial domain is still R^3 but the
solution is BOUNDED (if it converges to a self-similar profile). The self-similar
profile decays at spatial infinity like |xi|^{-1} (from dimensional analysis).

**Chen-Hou (2023) used this**: Their proof of Euler blowup works in self-similar
coordinates. The profile lives on a COMPACT spatial domain (after weighted truncation).
They used computer-assisted bounds on integrals in these coordinates.

**Relevance**:
- **NS**: Our Newton-Krylov plan works in Leray frame. The radii polynomial approach
  (Section 3.4) can verify periodic orbits in this frame, constituting a CAP of
  (Type II) blowup.

### 6.4 Finite Element Methods with Artificial Boundaries

**For computation on R^n: truncate to a large ball B_R, impose approximate BC.**

The artificial boundary condition on |x| = R:
```
Exact: Dirichlet-to-Neumann map (nonlocal, expensive)
Approximate: absorbing BC, PML (perfectly matched layer), or
             matched asymptotic: u ~ c/|x|^{n-2} for |x| >> 1
```

**Rigorous version**: Solve on B_R with exact error bound for the artificial BC:
```
||u - u_R||_{H^1(B_R)} <= C * R^{-(n-2+s)}

where s depends on the decay rate of the solution.
```

For fast-decaying solutions (exponential), R doesn't need to be very large.

**Relevance**:
- **YM infinite volume**: The lattice on Z^4 is approximated by a lattice on
  [-L, L]^4. The error from finite volume decays exponentially with L IF the
  mass gap exists (exponential clustering). This is circular for proving the gap,
  but useful for COMPUTING it with controlled error.

---

## 7. Success Stories

### 7.1 Tucker (2002): The Lorenz Attractor

**Problem**: Prove the Lorenz system has a strange attractor.
**Domain**: R^3 (continuous, noncompact, chaotic dynamics)

**Method**:
1. Define a cross-section (Poincare section) for the flow
2. Enclose the return map on the cross-section using rigorous ODE integration
3. Subdivide the cross-section into small boxes
4. For each box, integrate the ODE forward using interval Lohner algorithm
5. Verify the return map satisfies conditions for a strange attractor
   (expansion > 1, specific symbolic dynamics)

**Key technical challenge**: Near the origin, the ODE is stiff. Tucker used
NORMAL FORM COORDINATES near the equilibrium (analytical transformation that
makes the flow approximately linear, allowing much larger time steps).

**Computation**: About 30,000 boxes, each requiring a rigorous ODE integration.
Total runtime: hours on 2002 hardware.

**Lesson for us**: The subdivision + interval integration approach handles R^3
by working on a compact cross-section. The flow maps the cross-section to itself
(trapping region). No need to handle all of R^3.

### 7.2 Hales (2005/2014): Kepler Conjecture (Flyspeck)

**Problem**: Prove the densest sphere packing in R^3 is FCC (face-centered cubic).
**Domain**: R^3 (continuous positions of infinitely many spheres)

**Method** (two stages):
1. **Reduction to finite cases**: Hales proved that any packing can be decomposed
   into Delaunay cells, and the optimization over cell shapes reduces to ~5000
   finite combinatorial cases.
2. **Each case**: Minimize a function of ~150 continuous variables subject to
   constraints. Solved ~100,000 linear programs. Verified ~1000 nonlinear
   inequalities.

**The Flyspeck formal verification** (2014):
- All ~1000 nonlinear inequalities verified using interval arithmetic in HOL Light
- ~5000 CPU hours for the nonlinear verification
- Linear programs verified using a separate certifier

**Lesson for us**: The key was the REDUCTION step — showing that a continuous,
infinite problem reduces to finitely many continuous optimization problems, each
on a compact domain. For YM, the analog would be: reduce the mass gap to finitely
many representation-theoretic inequalities.

### 7.3 Fefferman-Seco (1994): Atomic Energy Asymptotics

**Problem**: Prove the Dirac-Schwinger conjecture on the asymptotic energy of
large atoms: E(Z) = -c_1 Z^{7/3} + c_2 Z^2 - c_3 Z^{5/3} + o(Z^{5/3}).
**Domain**: R^3, quantum mechanics of Z electrons

**Method**:
1. Reduce to a 1D Schrodinger eigenvalue problem (spherical symmetry)
2. Use WKB approximation + Van der Corput exponential sum techniques
3. Rigorous remainder bounds on the WKB expansion
4. Computer-assisted verification of specific inequalities on the remainder

**Key insight**: The "computer-assisted" part was bounding oscillatory sums of
the form sum exp(i*f(n)) using Van der Corput lemmas with rigorous constants.
This required explicit error bounds on the WKB turning points and eigenvalues.

**Lesson for us**: Even for continuous problems on R^3, the proof reduces to
bounding finitely many EXPLICIT quantities. The computer verifies these bounds.

### 7.4 Chen-Hou (2023): Euler Blowup

**Problem**: Prove finite-time singularity formation for 3D Euler equations with
smooth initial data.
**Domain**: [0,1] x [0,1] (r, z coordinates), axisymmetric

**Method**:
1. Find approximate self-similar blowup profile numerically
2. Linearize around the profile in self-similar coordinates
3. Construct approximate space-time solutions (computer-assisted)
4. Prove nonlinear stability using sharp weighted energy estimates
5. Rigorous bounds on integrals (operator norms, inner products)
   using interval arithmetic

**Key innovation**: They did NOT use standard interval ODE integration. Instead,
they built approximate solutions analytically (polynomial in self-similar variables)
and bounded residuals using integral estimates with interval arithmetic. This is
closer to the Nakao method than to Tucker's approach.

**Lesson for us**: The state of the art for PDE blowup proofs uses:
- Self-similar coordinates (Section 6.3)
- Polynomial approximation with rigorous residuals (Section 2.1)
- Integral bounds via interval arithmetic (our interval.py)
- Sharp functional inequalities (optimal transport, etc.)

**What they did NOT do**: Extend to NS. The viscous term creates a singular
perturbation in self-similar coordinates (Section 6.3). This is our open problem.

### 7.5 Watanabe et al. (2021): 3D Stationary Navier-Stokes

**Problem**: Prove existence of stationary solutions to NS on specific 3D domains.
**Domain**: Bounded 3D domain Omega

**Method**: Nakao method (Section 3.3) with:
1. FEM approximation of the stationary NS solution
2. Quantitative error estimates for Stokes eigenvalue problem
3. Fixed-point theorem verification with explicit constants
4. Interval arithmetic for all linear algebra

**Lesson for us**: CAP for 3D NS EXISTS. It works for stationary solutions on
bounded domains. The extension to the time-dependent problem and to blowup is
the frontier.

### 7.6 Platt (2021): Riemann Hypothesis to Height 3 * 10^12

**Problem**: Verify all zeros of zeta(s) with 0 < Im(s) < 3*10^12 lie on Re(s) = 1/2.
**Domain**: Critical strip (continuous, but reduced to counting problem)

**Method**:
1. Compute Z(t) = exp(i*theta(t)) * zeta(1/2 + it) (the Hardy Z-function)
2. Z(t) is real for real t. Zeros of zeta on the critical line = sign changes of Z(t)
3. Count sign changes of Z(t) for t in [0, T] (rigorous, using interval arithmetic)
4. Compare with N(T) = number of zeros with Im(s) < T (from the argument principle)
5. If sign changes = N(T), all zeros are on the critical line up to height T

**Key computation**: Evaluate Z(t) at ~10^12 points using Riemann-Siegel formula
with rigorous error bounds. Each evaluation needs O(sqrt(T)) operations.

**Lesson for us**: The RH verification is "just" a massive interval arithmetic
computation on an explicit formula. No PDE theory needed. The challenge is SCALE,
not methodology. Current verification height could likely be pushed higher with
more compute (GPU?).

---

## 8. Practical Python Implementation

### 8.1 Our Current Tools

We already have `ns_blowup/interval.py` — a basic interval arithmetic library with:
- Directed rounding via `np.nextafter` (1-ULP tight)
- +, -, *, /, integer powers, sqrt
- Comparison operators

**Missing for serious CAP work**:
- [ ] Transcendental functions (exp, log, sin, cos) with rigorous bounds
- [ ] Bessel functions with rigorous bounds (needed for YM character expansion)
- [ ] Interval linear algebra (matrix multiply, solve, eigenvalues)
- [ ] Taylor model arithmetic
- [ ] Chebyshev enclosure
- [ ] Automatic differentiation with intervals

### 8.2 Recommended Library Stack

**Tier 1: Use immediately (Python, minimal setup)**
```
mpmath           — arbitrary precision arithmetic, has interval mode
                   (directed rounding is "heuristic" — off by ≤2 ULP)
numpy            — fast array operations (not rigorous, use for floats only)
scipy.linalg     — eigenvalue computation (not rigorous, use as approximate)
cvxpy + MOSEK    — SDP solver for SOS certificates
```

**Tier 2: Use for rigorous results (requires C binding)**
```
arb/FLINT        — ball arithmetic, ALL transcendental functions rigorously bounded
                   Python binding via python-flint: pip install python-flint
                   THIS IS THE BEST OPTION for rigorous special functions
                   (Bessel, zeta, hypergeometric, etc.)
CAPD             — rigorous ODE integration (C++, call via subprocess)
```

**Tier 3: If we need maximum power (different ecosystem)**
```
TaylorModels.jl  — Julia, best Taylor model implementation
IntervalArithmetic.jl — Julia, IEEE 1788 compliant
Isabelle/HOL     — formal verification of interval computations
```

### 8.3 Upgrading interval.py for Function Spaces

```python
# Proposed additions to interval.py

class Interval:
    # ... existing code ...

    def exp(self):
        """Rigorous exp([lo, hi]) = [exp(lo)-eps, exp(hi)+eps]."""
        lo = self._round_down(math.exp(self.lo))
        hi = self._round_up(math.exp(self.hi))
        return Interval(lo, hi)

    def log(self):
        """Rigorous log([lo, hi]) for positive intervals."""
        if self.lo <= 0:
            raise ValueError("log of non-positive interval")
        lo = self._round_down(math.log(self.lo))
        hi = self._round_up(math.log(self.hi))
        return Interval(lo, hi)

    def sin(self):
        """Rigorous sin, handling monotonicity and extrema."""
        # Need to check if [lo, hi] contains any pi/2 + k*pi
        # ... (complex but doable)
        pass

    def cos(self):
        """Rigorous cos."""
        pass

class TaylorModel:
    """Taylor model: polynomial P(x) + interval remainder Delta.

    Guarantees: for all x in domain, f(x) in P(x) + Delta.
    """
    def __init__(self, coeffs, remainder, domain):
        """
        coeffs: list of Interval coefficients [c_0, c_1, ..., c_n]
                representing P(x) = c_0 + c_1*(x-mid) + c_2*(x-mid)^2 + ...
        remainder: Interval containing the truncation error
        domain: Interval [a, b]
        """
        self.coeffs = coeffs
        self.remainder = remainder
        self.domain = domain
        self.order = len(coeffs) - 1

    def evaluate(self, x):
        """Evaluate the Taylor model at interval x.

        Returns an Interval enclosing f(x).
        """
        mid = self.domain.mid
        h = x - Interval(mid)
        result = Interval(0)
        h_power = Interval(1)
        for c in self.coeffs:
            result = result + c * h_power
            h_power = h_power * h
        return result + self.remainder

    def bound(self):
        """Bound the Taylor model over its entire domain.

        Returns Interval enclosing range of f on domain.
        """
        return self.evaluate(self.domain)

    def __add__(self, other):
        """Add two Taylor models."""
        assert self.domain.lo == other.domain.lo  # same domain
        n = max(self.order, other.order)
        coeffs = []
        for k in range(n + 1):
            c1 = self.coeffs[k] if k <= self.order else Interval(0)
            c2 = other.coeffs[k] if k <= other.order else Interval(0)
            coeffs.append(c1 + c2)
        return TaylorModel(coeffs, self.remainder + other.remainder, self.domain)

    def __mul__(self, other):
        """Multiply two Taylor models (truncate to max order)."""
        n = self.order  # truncation order
        coeffs = [Interval(0)] * (n + 1)
        # Polynomial part
        for i in range(n + 1):
            for j in range(n + 1):
                if i + j <= n:
                    c1 = self.coeffs[i] if i <= self.order else Interval(0)
                    c2 = other.coeffs[j] if j <= other.order else Interval(0)
                    coeffs[i + j] = coeffs[i + j] + c1 * c2
        # Remainder: bound the truncated terms + cross terms with remainders
        B_self = self.bound()
        B_other = other.bound()
        trunc_rem = Interval(0)  # TODO: bound truncated polynomial terms
        cross_rem = abs(B_self) * other.remainder + abs(B_other) * self.remainder
        total_rem = trunc_rem + cross_rem + self.remainder * other.remainder
        return TaylorModel(coeffs, total_rem, self.domain)


class FourierEnclosure:
    """Rigorous enclosure of a function in Fourier space.

    f(x) = sum_{|k| <= N} a_k e^{ikx} + R_N(x)

    where a_k are Interval coefficients and R_N is bounded.
    """
    def __init__(self, coeffs_dict, tail_bound, domain_dim):
        """
        coeffs_dict: {k: Interval} for |k| <= N
        tail_bound: Interval bounding ||R_N||_{l^1}
        domain_dim: spatial dimension
        """
        self.coeffs = coeffs_dict
        self.tail_bound = tail_bound
        self.dim = domain_dim

    def l1_norm(self, weight_s=0):
        """Compute ||f||_{l^1_s} = sum |a_k| * |k|^s."""
        total = Interval(0)
        for k, ak in self.coeffs.items():
            k_norm = sum(ki**2 for ki in k) ** 0.5 if isinstance(k, tuple) else abs(k)
            weight = max(1, k_norm) ** weight_s
            total = total + abs(ak) * Interval(weight)
        total = total + self.tail_bound
        return total

    def convolve(self, other):
        """Rigorous convolution (multiplication in physical space).

        Uses: ||f*g||_{l^1} <= ||f||_{l^1} * ||g||_{l^1}  (Young's inequality)
        """
        # Finite part: direct convolution
        new_coeffs = {}
        for k1, a1 in self.coeffs.items():
            for k2, a2 in other.coeffs.items():
                k_sum = tuple(k1i + k2i for k1i, k2i in zip(
                    (k1,) if not isinstance(k1, tuple) else k1,
                    (k2,) if not isinstance(k2, tuple) else k2
                ))
                if k_sum in new_coeffs:
                    new_coeffs[k_sum] = new_coeffs[k_sum] + a1 * a2
                else:
                    new_coeffs[k_sum] = a1 * a2

        # Tail: bound cross-terms and tail-tail
        finite_l1 = sum(abs(a) for a in self.coeffs.values())
        other_finite_l1 = sum(abs(a) for a in other.coeffs.values())
        tail = (finite_l1 * other.tail_bound +
                other_finite_l1 * self.tail_bound +
                self.tail_bound * other.tail_bound)

        return FourierEnclosure(new_coeffs, tail, self.dim)
```

### 8.4 Using python-flint/arb for Rigorous Special Functions

```python
# pip install python-flint
from flint import arb, acb

# Rigorous Bessel function (for YM character expansion)
def rigorous_bessel_i(n, beta, prec=128):
    """Compute I_n(beta) with rigorous error bounds.

    Returns (midpoint, radius) such that true value in [mid-rad, mid+rad].
    """
    # arb library tracks error automatically
    x = arb(beta, prec=prec)
    # Use the hypergeometric representation
    # I_n(x) = (x/2)^n / Gamma(n+1) * 0F1(;n+1; x^2/4)
    result = x.bessel_i(n)  # built-in rigorous Bessel
    return float(result.mid()), float(result.rad())

# Rigorous zeta function (for RH verification)
def rigorous_zeta(s_real, s_imag, prec=128):
    """Compute zeta(s) with rigorous error bounds."""
    s = acb(s_real, s_imag, prec=prec)
    z = s.zeta()
    return (float(z.real.mid()), float(z.real.rad()),
            float(z.imag.mid()), float(z.imag.rad()))
```

---

## 9. Application Map: Which Technique for Which Problem

### Yang-Mills Mass Gap

| Sub-problem | Technique | Section | Feasibility |
|-------------|-----------|---------|-------------|
| Character expansion coefficients | Rigorous Bessel via arb/FLINT | 5.2, 8.4 | READY |
| Transfer matrix spectral gap (finite lattice) | Interval eigenvalue enclosure (Plum) | 3.2 | READY |
| Peter-Weyl truncation error | Tail bounds from Bessel asymptotics | 5.2 | READY |
| Tomboulis (5.15) at specific beta | Interval arithmetic on partition functions | 5.4 | IN PROGRESS |
| Mass gap for all beta (homotopy) | Homotopy continuation from strong to weak coupling | 3.5 | HARD |
| Infinite volume limit | Exponential clustering + compactness | 6.1, 4.3 | OPEN |
| Balaban large field bounds | Bootstrap over RG scales | 4.4 | BLOCKED (attempt_005) |

**Recommended next step**: Implement the radii polynomial approach (3.4) for the
transfer matrix eigenfunction problem. The transfer matrix in the character basis is
a specific infinite matrix. The Galerkin truncation (finite j_max) gives an approximate
eigenvalue. The tail bound (5.2) controls the error. If the gap between eigenvalue 0
and eigenvalue 1 is larger than the tail error, the mass gap is PROVEN for that beta.

### Navier-Stokes Regularity/Blowup

| Sub-problem | Technique | Section | Feasibility |
|-------------|-----------|---------|-------------|
| SOS certificates for strain bound | SOS + SDP (Lyapunov) | 4.2 | DONE (1.33M certs) |
| Galerkin truncation error | Tail bounds from Laplacian eigenvalues | 4.1 | READY |
| Periodic orbit in Leray frame | Radii polynomial + Fourier enclosure | 3.4 | FEASIBLE |
| Stationary solution existence (3D) | Nakao method | 3.3 | DONE (Watanabe 2021) |
| Euler blowup proof extension to NS | Self-similar variables + CAP | 6.3, 7.4 | OPEN |
| Enstrophy bound bootstrap | Inductive bound on Fourier modes | 4.4 | THE OPEN PROBLEM |

**Recommended next step**: Implement the Fourier enclosure (FourierEnclosure class
above) for the Galerkin-truncated NS equations on T^3. Use the radii polynomial
approach to verify that specific equilibria or periodic orbits exist. Start with
the Kolmogorov flow (explicit steady state, well-studied stability).

### Riemann Hypothesis

| Sub-problem | Technique | Section | Feasibility |
|-------------|-----------|---------|-------------|
| Verify zeros to height T | Interval evaluation of Hardy Z-function | 7.6 | DONE to 3*10^12 |
| de Bruijn-Newman constant | Heat flow of xi function with rigorous bounds | 7.6 | Lambda <= 0.22 |
| Zero-free regions | Chebyshev enclosure of log(zeta) | 2.2 | FEASIBLE |
| Function enclosure on critical strip | Taylor models in Im(s) | 2.1 | FEASIBLE |

**Recommended next step**: Use arb/FLINT to verify zeros of zeta to higher precision
in regions of interest. The python-flint binding gives rigorous zeta values. The
bottleneck is computational, not methodological.

---

## Key Takeaways

1. **The radii polynomial approach is the most general and powerful technique** for
   our problems. It works in Banach spaces of sequences (Fourier, character expansion),
   handles both elliptic and parabolic PDEs, and produces machine-checkable certificates.

2. **Tail bounds are the bridge from finite to infinite**. For NS on T^3, the Laplacian
   eigenvalues are known exactly. For YM with Peter-Weyl, Bessel function asymptotics
   give exponential tail decay. In both cases, taking enough modes makes the tail
   negligible.

3. **Our interval.py needs upgrades** but the basic framework is sound. Priority
   additions: transcendental functions (exp, log, trig), interval linear algebra,
   and a Taylor model class.

4. **arb/FLINT via python-flint** is the best practical tool for rigorous special
   function evaluation. It covers Bessel functions (YM), zeta functions (RH), and
   all standard transcendentals.

5. **The fundamental obstruction in YM is not computational** — it's the infinite-volume
   limit (Balaban's large field entropy problem). CAP can certify the mass gap for
   FINITE lattices and FIXED coupling. Extending to all couplings requires either
   homotopy continuation or a new analytical idea.

6. **For NS blowup, Chen-Hou's approach is the template**: self-similar coordinates +
   polynomial approximation + rigorous integral bounds. Extending this to NS requires
   handling the viscous singular perturbation — an unsolved analytical problem that
   CAP alone cannot solve.

---

## References

### Foundational
- Nakao, Plum, Watanabe. "Numerical Verification Methods and Computer-Assisted
  Proofs for PDEs." Springer, 2019.
- Tucker. "A rigorous ODE solver and Smale's 14th problem." Found. Comp. Math., 2002.
- Hales et al. "A formal proof of the Kepler conjecture." Forum of Math., Pi, 2017.

### Radii Polynomial / Rigorous Numerics
- van den Berg, Lessard. "Rigorous numerics in dynamics." Notices AMS, 2015.
- Hungria, Lessard, Mireles-James. "Rigorous numerics for analytic solutions of
  differential equations: the radii polynomial approach." 2017.
- Lessard. "Rigorous Numerics for ill-posed PDEs." ARMA, 2017.

### Navier-Stokes CAP
- Watanabe et al. "Computer-assisted proof for the stationary solution existence of
  the Navier-Stokes equation over 3D domains." arXiv:2101.03727, 2021.
- Chen, Hou. "Stable nearly self-similar blowup of the 2D Boussinesq and 3D Euler
  equations." Parts I (analysis) and II (rigorous numerics), 2023.

### Yang-Mills / Gauge Theory
- Tomboulis. "Confinement for all values of the coupling in 4D SU(2) lattice gauge
  theory." arXiv:0707.2179, 2007.
- Balaban. "The variational problem and background fields in renormalization group
  method for lattice gauge theories." CMP 109, 1987.

### Interval Arithmetic / Tools
- arb/FLINT: https://arblib.org/ (ball arithmetic, Python via python-flint)
- CAPD: http://capd.ii.uj.edu.pl/ (rigorous ODE integration)
- VNODE-LP: https://www.cas.mcmaster.ca/~nedialk/vnodelp/ (validated ODE solver)
- mpmath: https://mpmath.org/ (arbitrary precision, heuristic intervals)

### Riemann Hypothesis
- Platt. "The Riemann hypothesis is true up to 3*10^12." Bull. London Math. Soc., 2021.
- Rodgers, Tao. "The de Bruijn-Newman constant is non-negative." Forum of Math., Pi, 2020.
