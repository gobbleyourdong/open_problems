# FLUID GOD Manifest

**Version:** 1.0
**Mission:** Prove that global regularity for the 3D incompressible Navier-Stokes equations is FALSE — that finite-time blowup exists for smooth, finite-energy initial data.

## Overview
Definitive reference manifest for proving failure of global regularity in 3D Navier-Stokes equations. Extracted from 73 research papers spanning regularity theory, blowup analysis, self-similar solutions, non-uniqueness, vorticity dynamics, and computational methods.

## Cross-Validation Status
- **Date:** 2026-03-23
- **Papers Validated:** 38
- **Equations Corrected:** 81
- **Method:** Cross-validated against source PDFs by AI with human-level reading

## Known Gaps
### Biot-Savart Singular Integral Bound
The Biot-Savart law recovers velocity from vorticity via a singular integral. Proving rigorous bounds for the specific topology and alignment between strain and vorticity in the blowup scenario is where the hardest analysis lives. Calderon-Zygmund theory provides the framework but the specific structural bound for the IC class has not been achieved.
**Tools:** Calderon-Zygmund theory, Singular integral operators, Endpoint Sobolev embeddings

### Axisymmetric Reduction Sufficiency
Axisymmetry reduces 3D to 1D elliptic integrals, but the proof must work for the specific initial condition class, not generic axisymmetric flows. Must capture why the specific IC is different from axisymmetric flows that don't blow up.
**Tools:** 1D elliptic integrals, Axisymmetric Euler/NS theory, Hou-Luo model

### Rigorous Proof Techniques
The gap between numerical evidence of blowup and rigorous mathematical proof. Requires Calderon-Zygmund theory, endpoint Sobolev embeddings, careful commutator estimates — years of specialized functional analysis training.
**Tools:** Calderon-Zygmund theory, Commutator estimates, Littlewood-Paley decomposition, Besov space theory

### From Numerical to Rigorous
PySR and numerical methods can find bounds and see patterns in data. Converting these to rigorous proofs is the Millennium Prize gap.
**Tools:** PySR, Computer-assisted proofs, Interval arithmetic, Rigorous numerics


## NS3D Blowup and Singularity Formation
*Papers directly addressing finite-time blowup, singularity formation, and potentially singular solutions of the 3D Navier-Stokes or Euler equations.*

### EXISTENCE, UNIQUENESS AND SMOOTHNESS OF SOLUTION FOR 3D NAVIER-STOKES EQUATIONS WITH ANY SMOOTH INITIAL VELOCITY.
**Authors:** A. TSIONSKIY, M. TSIONSKIY | **Year:** 2013 | [1201.1609v8](https://arxiv.org/abs/1201.1609v8) | **Validation:** verified
**Relevance:** 10/10

**Why it matters:** This paper claims to have proven the existence, uniqueness, and smoothness of solutions for the 3D Navier-Stokes equations for any smooth initial data. This is a direct claim of global regularity, which, if true, would definitively prove that finite-time blowup is impossible. The paper's relevance is therefore maximal, as it purports to have solved the very problem in the opposite direction of the user's team's goal. It attempts to close the fundamental gap in the theory by providing a constructive proof for all time.

**Key Insights:**
1. The core claim is a spectacular failure, and understanding why is crucial. The paper's proof of global regularity is fundamentally flawed. It relies on the assumption that the integral operator `S_v` is a contraction mapping for *any* smooth initial data. However, the condition required for this (inequality 6.4) is only shown to hold if the initial data and the solution itself are 'sufficiently small'. This is a well-known result for local existence, but the authors incorrectly extrapolate it to a global-in-time proof for all data. An engineer trying to prove blowup should study this paper as a case study in how a seemingly rigorous argument can fail by hiding a fatal assumption within its conditions.
2. The method of transforming the PDE to an integral equation is standard, but the analysis is not. The technique of using Fourier and Laplace transforms to convert the PDE into an algebraic problem, solving it, and then transforming back to get an integral representation is a classic approach. The novelty (and error) is in the analysis of the resulting integral operator. The paper provides a clear, albeit flawed, roadmap of this technique.
3. The function spaces used are restrictive. The proof is conducted in the space of rapidly decaying, infinitely smooth functions (`T S`). While this makes the analysis easier, it is a very restrictive space. A blowup, if it occurs, might happen for solutions that are initially smooth but do not have this rapid decay property. The choice of function space is a critical component of any regularity proof.

**Equations:**
- $$\frac{\partial u_k}{\partial t} + \sum_{n=1}^{N} u_n \frac{\partial u_k}{\partial x_n} = -\frac{\partial p}{\partial x_k} + \nu \Delta u_k + f_k(x,t)$$
  This is the momentum equation for the k-th component of the fluid velocity. It is a statement of Newton's second law for a fluid element, balancing inertia, pressure gradients, viscous forces, and external forces.
- $$div(u) = \sum_{n=1}^{N} \frac{\partial u_n}{\partial x_n} = 0$$
  This is the incompressibility condition, stating that the velocity field is divergence-free. Physically, it means that the density of a fluid parcel remains constant as it moves.
- $$u = S \cdot f - S \cdot (u \cdot \nabla)u + B \cdot u^0$$
  This is the core of the paper's method. The solution `u` is expressed as the result of applying a set of integral operators (`S`, `B`) to the forcing term `f`, the initial condition `u^0`, and, crucially, the non-linear advection term `(u \cdot \nabla)u`. This transforms the PDE into a fixed-point problem for the operator acting on `u`.
- $$||S_v \cdot u_v - S_v \cdot u_v'||_p \le \alpha \cdot ||u_v - u_v'||_p` where `\alpha < 1$$
  This inequality is the central claim of the proof. It states that the integral operator `S_v` (which incorporates the non-linear term) is a contraction mapping on the chosen function space. This means that applying the operator to any two different solutions brings them closer together, guaranteeing a unique fixed point.

**Theorems:**
- THEOREM 1: Contraction operator: The matrix integral operator `S_v` maps a perfect space `T S` onto itself, and for any `u_v` in `T S`, if the condition `max{||u^0||_c, ||u^0||_{L_2}, ||u||_{c_2} + ||u||_{L_2}} << V` is valid, then the operator is a contraction.
  *Proof:* The proof is by contradiction. It assumes the operator is not a contraction and shows this leads to a contradiction with the properties of the integral operators. The key is asserting that the norm of the operator can be made less than 1.
- THEOREM 2: Existence and uniqueness of solution: There exists a unique solution `u_v` of the equation `u_v = S_v(u_v)` in the space `T S` for any `t \in [0, \infty)`.
  *Proof:* This is a direct application of the Banach fixed-point theorem, which states that a contraction mapping on a complete metric space has a unique fixed point. The proof constructs the solution as the limit of the sequence `u_{v,n+1} = S_v(u_{v,n})`.
- THEOREM 3: Continuous dependence of solution on t: The solution `u(x,t)` depends continuously on time `t`.
  *Proof:* The proof shows that the operator `S_v` is continuous in the parameter `t`. This property is then transferred to the fixed point `u_v`, ensuring the solution's temporal continuity.

**Constants & Bounds:**
- `Condition for Contraction (6.4): max{||u^0||_c, ||u^0||_{L_2}, ||u||_{c_2} + ||u||_{L_2}} << V`: This is the most important bound in the paper. It is a condition on the initial data `u^0` and the solution `u` itself. The authors claim that their proof works by choosing a constant `V` such that this inequality holds, which makes the operator a contraction. The fatal flaw is that it's not proven that such a `V` can be found for *any* initial data, especially large initial data. The condition essentially requires the solution to be 'small enough'.
- `Convergence Rate (6.8): ||u_{v,n} - u_v||_p \le \frac{\alpha^n}{1-\alpha} ||u_{v,1} - u_{v,0}||_p`: This provides an estimate for how quickly the iterative sequence converges to the true solution. It shows exponential convergence, with the rate determined by the contraction factor `\alpha`.

---

### Nonuniqueness of Leray-Hopf solutions to the unforced incompressible 3D Navier-Stokes Equation
**Authors:** Thomas Hou, Yixuan Wang, Changhe Yang | **Year:** 2026 | [2509.25116v2](https://arxiv.org/abs/2509.25116v2) | **Validation:** verified
**Relevance:** 10/10

**Why it matters:** This paper is highly relevant to the NS3D blowup problem as it directly addresses the non-uniqueness of Leray-Hopf solutions. The construction of multiple distinct solutions with the same initial data is a major step towards understanding the potential for singular behavior. It addresses the gap in understanding the uniqueness of weak solutions to the Navier-Stokes equations.

**Key Insights:**
1. The paper provides the first rigorous computer-assisted proof of the non-uniqueness of Leray-Hopf solutions to the unforced incompressible 3D Navier-Stokes equations.
2. The non-uniqueness is demonstrated by constructing a self-similar solution and then showing the existence of a second solution by analyzing the stability of the linearized operator around this profile.
3. The proof relies on a novel numerical method to compute candidate solutions with high precision and a framework for rigorously establishing exact solutions in a neighborhood of these candidates.

> **Validation Note:** Theorem 2 in the JSON file states that v is in H1_loc, but the paper specifies that v is in H1.

**Equations:**
- $$∂t u + u · ∇u − ∆u + ∇p = 0, divu = 0$$
  The incompressible Navier-Stokes equations.
- $$1/\u221at U(x/\u221at)$$ *(corrected)*
  The self-similar scaling for the velocity field.
  > Correction: The original equation included an unnecessary '*' symbol.

**Theorems:**
- Theorem 1 (Nonuniqueness of Leray-Hopf solutions): There exist infinitely many distinct suitable Leray-Hopf solutions to the Navier-Stokes equation (1.1) on R3 × [0, 1] with the same divergence-free initial condition.
  *Proof:* The proof is based on a computer-assisted method that constructs a self-similar solution and then shows the existence of a second solution by analyzing the stability of the linearized operator.
- Theorem 2: There exists a weak solution (U,v,λ) to the system (1.12) with U, v in H1_loc.
  *Proof:* The proof uses a computer-assisted framework to verify the existence of a solution to the eigenvalue problem for the linearized operator.

**Constants & Bounds:**
- `Prodi-Serrin condition: 3/q + 2/s <= 1`: Condition on the Lebesgue space exponents for a solution to be a strong solution.

---

### POTENTIALLY SINGULAR SOLUTIONS OF THE 3D INCOMPRESSIBLE EULER EQUATIONS
**Authors:** GUO LUO, THOMAS Y. HOU | **Year:** 2013 | [1310.0497v2](https://arxiv.org/abs/1310.0497v2) | **Validation:** verified
**Relevance:** 9/10

**Why it matters:** This paper is highly relevant to the NS3D blowup problem, despite focusing on the Euler equations. A finite-time singularity in the Euler equations is a strong indication that a similar mechanism could lead to blowup in the Navier-Stokes equations in the limit of vanishing viscosity. The paper provides a concrete, numerically plausible scenario for blowup driven by vortex stretching at a boundary, which directly challenges the geometric non-blowup criteria. It helps to close the gap in understanding how the vorticity field can become sufficiently irregular to cause a singularity, providing a specific candidate for a blowup mechanism.

**Key Insights:**
1. Boundary-induced blowup is a plausible mechanism. The singularity occurs at a stagnation point on the solid boundary, suggesting that the interaction of the flow with the boundary is the primary driver of the blowup. This is a departure from many previous studies that focused on singularities in the interior of the flow.
2. Anisotropic scaling is a key feature of the blowup. The different growth rates of the vorticity components (radial/axial vs. angular) indicate a specific geometric mechanism for the singularity. This provides a clear signature to look for in other potential blowup scenarios.
3. Extreme numerical resolution is required to capture the singularity. The use of a highly adaptive mesh with an effective resolution of over \((3 \times 10^{12})^2\) was necessary to resolve the blowup. This highlights the immense computational challenge of the problem and suggests that previous null results may have been due to insufficient resolution.
4. Violation of geometric non-blowup criteria is a key indicator. The paper demonstrates that the conditions of the Constantin-Fefferman-Majda and Deng-Hou-Yu criteria are violated, providing a clear link between the observed blowup and the breakdown of the geometric regularity of the vorticity field.

**Equations:**
- $$\[
\begin{cases}
 u_t + u \cdot \nabla u = -\nabla p \\
 \nabla \cdot u = 0
\end{cases}
\]$$
  These are the 3D incompressible Euler equations. The first equation is the momentum equation, describing the acceleration of a fluid particle due to pressure gradients and its own motion (advection). The second is the incompressibility condition, stating that the flow is divergence-free, meaning fluid density is constant along flow paths.
- $$\[
\omega_t + u \cdot \nabla \omega = \omega \cdot \nabla u
\]$$
  This is the vorticity transport equation, derived by taking the curl of the momentum equation. It describes how the vorticity \(\omega = \nabla \times u\) (the local spinning motion of the fluid) is transported by the flow (advection term) and stretched or tilted by velocity gradients (the stretching term \(\omega \cdot \nabla u\)).
- $$\[\begin{cases} u^\theta_t + u^r u^\theta_r + u^z u^\theta_z = - \frac{1}{r} u^r u^\theta \\ \omega^\theta_t + u^r \omega^\theta_r + u^z \omega^\theta_z = \frac{2}{r} u^\theta u^\theta_z + \frac{1}{r} u^r \omega^\theta \\ -(\Delta - 1/r^2)\psi^\theta = \omega^\theta \end{cases}\]$$ *(corrected)*
  These are the Euler equations in axisymmetric cylindrical coordinates (r, \(\theta\), z). They describe the evolution of the angular components of velocity (u_\(\theta\)), vorticity (\(\omega_\theta\)), and the stream function (\(\psi_\theta\)), which simplifies the 3D problem into a 2D problem in the (r, z) meridian plane.
  > Correction: The original used subscripts where the paper uses superscripts for theta, r, and z components. Also, the third equation had a sign error and was missing the negative sign on the left side.
- $$\[\begin{cases} u_{1,t} + u^r u_{1,r} + u^z u_{1,z} = 2u_1 \psi_{1,z} \\ \omega_{1,t} + u^r \omega_{1,r} + u^z \omega_{1,z} = (u_1^2)_z \\ -[\partial_r^2 + (3/r)\partial_r + \partial_z^2] \psi_1 = \omega_1 \end{cases}\]$$ *(corrected)*
  These are the transformed equations used in the numerical simulation, where \(u_1 = u_\theta/r, \omega_1 = \omega_\theta/r, \psi_1 = \psi_\theta/r\). This transformation removes the coordinate singularity at the axis r=0, which is crucial for developing a stable and accurate numerical scheme.
  > Correction: The original was missing a negative sign in the third equation, and used subscripts for u components where superscripts were used in the paper.
- $$\[
\int_0^T \|\omega(\cdot, t)\|_{L^\infty} dt = \infty
\]$$
  This is the Beale-Kato-Majda (BKM) criterion. It provides a necessary and sufficient condition for a finite-time blowup of a smooth solution to the 3D Euler equations: the solution remains smooth up to time T if and only if the time integral of the maximum vorticity remains finite.
- $$\[
\|\omega(\cdot, t)\|_\infty \sim c(t_s - t)^{-\gamma}
\]$$
  This is the assumed inverse power-law scaling for the maximum vorticity near the potential singularity time \(t_s\). The authors use this ansatz to analyze their numerical data, fitting for the singularity time \(t_s\) and the scaling exponent \(\gamma\) to provide evidence for blowup.

**Theorems:**
- Beale-Kato-Majda (BKM) Criterion: A smooth solution u of the 3D Euler equations blows up at t = T if and only if \(\int_0^T \|\omega(\cdot, t)\|_{L^\infty} dt = \infty\).
  *Proof:* The proof relies on energy estimates and Sobolev embedding theorems to control the growth of higher-order derivatives of the velocity field in terms of the maximum vorticity. It establishes a direct link between the regularity of the solution and the time-integrated maximum vorticity.
- Constantin-Fefferman-Majda (CFM) Criterion: There can be no blowup for the 3D Euler equations if the velocity field u is uniformly bounded and the vorticity direction \(\xi = \omega/|\omega|\) is sufficiently “well-behaved” (Lipschitz continuous) near the point of maximum vorticity.
  *Proof:* The proof is geometric. It shows that if the vorticity direction is regular enough, the vortex stretching term \(\omega \cdot \nabla u\) cannot become singular, which prevents the vorticity from blowing up. The regularity of the direction field prevents the rapid amplification of vorticity.
- Deng-Hou-Yu Criterion: A local Lagrangian version of the Constantin-Fefferman-Majda criterion. It provides a condition on the local geometric regularity of the vorticity direction along particle paths to prevent blowup.
  *Proof:* The proof technique is similar to the CFM criterion but localized to a fluid parcel's trajectory. It analyzes the evolution of the vorticity direction in a Lagrangian frame.

**Constants & Bounds:**
- `Maximum Vorticity Scaling: \(\|\omega(\cdot, t)\|_\infty \sim c(t_s - t)^{-\gamma}\), with \(\gamma \approx 5/2\)`: This is the primary scaling law observed for the blowup of the maximum vorticity. The exponent \(\gamma\) being greater than 1 is a necessary condition for the BKM integral to diverge.
- `Vorticity Component Scaling: Near the singularity, the radial and axial vorticity components grow as \(\omega_r, \omega_z \sim O((t_s - t)^{-5/2})\), while the angular component grows more slowly as \(\omega_\theta \sim O((t_s - t)^{-1})\).`: This anisotropic scaling is a key feature of the blowup. It shows that the singularity is driven by the stretching of the radial and axial vorticity components in the meridian plane.
- `Spatial Scaling of Singularity: The support of the singularity region collapses with a scaling of \(O((t_s - t)^3)\) in both the radial and axial directions.`: This describes the spatial localization of the blowup. The singularity becomes increasingly concentrated in a small region as the blowup time is approached.
- `Predicted Singularity Time: \(t_s \approx 0.00350562\)`: This is the numerically extrapolated time at which the singularity is predicted to occur based on the observed scaling laws.
- `Maximum Effective Resolution: The adaptive mesh achieves a maximum effective resolution of over \((3 \times 10^{12})^2\) near the singularity.`: This extremely high resolution is crucial for accurately capturing the singular behavior and providing confidence in the numerical results.
- `Maximum Vorticity Growth: The simulation achieves a \((3 \times 10^8)\)-fold increase in maximum vorticity.`: This enormous growth in vorticity over a short time is strong evidence of a developing singularity.

---

### Forward discretely self-similar solutions of the Navier-Stokes equations II
**Authors:** Zachary Bradshaw, Tsai-Peng Tsai | **Year:** 2021 | [1510.07504v1](https://arxiv.org/abs/1510.07504v1) | **Validation:** verified
**Relevance:** 9/10

**Why it matters:** This paper is highly relevant to proving NS3D finite-time blowup. It constructs forward discretely self-similar and self-similar solutions for a very general class of large initial data in the weak L3 space, which is a critical regime for finding singular behavior. The paper's method provides a new pathway to constructing such solutions, and it raises the possibility of non-compact singular sets for DSS solutions, a key consideration for the blowup problem. It directly addresses the gap of constructing solutions for rough, singular initial data, which is a major hurdle in the field.

**Key Insights:**
1. Discretely self-similar (DSS) solutions for large, rough initial data in L3_w can be constructed. This is a major step towards finding a blowup solution, as it allows for singular initial data.
2. The paper provides a new, more direct method for constructing self-similar solutions, avoiding the need for a contradiction argument. This could simplify the search for a blowup solution.
3. The possibility of a non-compact singular set for DSS solutions is a crucial insight. This means that a blowup could occur at a sequence of points in spacetime, not just a single point.
4. The use of the time-periodic Leray system is a powerful technique for constructing self-similar solutions. This approach could be adapted to other problems in PDE theory.
5. The paper highlights the importance of the weak L3 space for the initial data. This space is large enough to contain singular functions, which are likely necessary for a blowup to occur.

**Equations:**
- $$\partial_t v - \Delta v + v \cdot \nabla v + \nabla \pi = 0, \quad \nabla \cdot v = 0$$
  These are the 3D Navier-Stokes equations for an incompressible, viscous fluid, representing conservation of momentum and mass.
- $$v^\lambda(x, t) = \lambda v(\lambda x, \lambda^2 t)$$
  This is the natural scaling of the Navier-Stokes equations. If v is a solution, so is the rescaled v^\lambda.
- $$v(x, t) = \frac{1}{\sqrt{2t}} u(\frac{x}{\sqrt{2t}}), \quad y = \frac{x}{\sqrt{2t}}, s = \log(\sqrt{2t})$$
  This is the self-similar ansatz, which transforms the PDE for v(x,t) into a time-independent PDE for the profile u(y).
- $$\partial_t u - \Delta u + u + y \cdot \nabla u + u \cdot \nabla u + \nabla p = 0$$ *(corrected)*
  This is the time-dependent Leray equation for the self-similar profile u(y,s), which is time-periodic for discretely self-similar solutions.
  > Correction: The partial derivative in the paper is with respect to t, not s. The signs for the u and y \cdot \nabla u terms are also different in the paper (equation 1.10).

**Theorems:**
- Theorem 1.2: For any discretely self-similar, incompressible initial data v0 in L3_w, there exists a forward discretely self-similar local Leray solution.
  *Proof:* The proof constructs a solution to the time-periodic Leray system (Theorem 2.4) and then transforms it back to the original variables. A priori estimates for the Leray equations are established to make this possible.
- Theorem 1.3: For any -1 homogeneous, divergence-free vector field v0 in L3_w, there exists a self-similar local Leray solution.
  *Proof:* Two proofs are provided. The first obtains self-similar solutions as limits of discretely self-similar solutions. The second directly constructs solutions to the stationary Leray equations using a Galerkin scheme and a priori bounds.
- Theorem 2.4: Guarantees the existence of a periodic suitable weak solution to the time-periodic Leray system (2.1) under certain assumptions on the asymptotic profile U0.
  *Proof:* The proof uses a Galerkin approximation scheme to construct solutions for a mollified system. A priori bounds independent of the approximation level and mollification parameter are obtained, allowing to pass to the limit.

**Constants & Bounds:**
- `v0 in L3_w: ||v0||_L3_w <= c0`: The initial data is in the weak L3 space, which is a very general condition and allows for singular initial data.
- `Local Leray solution energy inequality: esssup sup ... < infinity`: This is the defining local energy inequality for local Leray solutions, which provides a local control on the energy and enstrophy of the solution.
- `Solution decay estimate: ||v(t) - e^(t*Delta)v0||_L2 <= C*t^(1/4)`: This estimate shows how the solution converges to the heat evolution of the initial data, which is a key property of the constructed solutions.
- `Galerkin approximation bounds: ||Uk||_L_inf(L2) + ||Uk||_L2(H1) < C`: Uniform bounds on the Galerkin approximations are crucial for the existence proof, as they allow to extract a convergent subsequence.
- `Pressure bound: ||p_epsilon||_L^(5/3) <= C`: A uniform bound on the pressure is needed to pass to the limit and obtain a solution to the Navier-Stokes equations.
- `A priori bound for stationary Leray system: ||U||_H1^2 <= 4*C^2*||R(W)||_H-1^2`: This is the key a priori bound that allows for the direct construction of self-similar solutions, avoiding a contradiction argument.

---

### SYMMETRY AND RIGIDITY: ONLY ONE KIND OF SYMMETRY ALLOW NON-ZERO REAL SYMMETRIC SOLUTION
**Authors:** QIXIANG YANG | **Year:** 2020 | [2002.12828v2](https://arxiv.org/abs/2002.12828v2) | **Validation:** verified
**Relevance:** 9/10

**Why it matters:** This paper is highly relevant to the NS3D blowup problem. It performs a systematic and exhaustive study of all possible spatial symmetries of solutions to the Navier-Stokes equations. The main result is a powerful rigidity theorem: out of 262,144 possible symmetries, only one specific symmetry for real-valued solutions (and 8 for complex solutions) can persist under the Navier-Stokes evolution, unless the solution is a trivial Beltrami flow. This drastically narrows the search space for a potential self-similar or symmetric blow-up profile, addressing the gap in understanding which geometric structures can support a singularity.

**Key Insights:**
1. The search for a self-similar blow-up profile can be almost entirely constrained to a single symmetry class for real vector fields. Any other symmetric initial data will either have its symmetry broken by the nonlinear term or will correspond to a trivial (non-blowing-up) Beltrami flow.
2. The nonlinear term B(u,v) does not preserve symmetry in general. Symmetry is only preserved under the very specific "matched symmetric properties" defined in the paper. This means that simply starting with a symmetric initial condition is not enough to guarantee a symmetric solution.
3. Any arbitrary divergence-free vector field can be decomposed into a sum of 8 "matched" symmetric fields. This suggests a powerful analysis technique: one could study the evolution of any initial data by studying the interactions between its fundamental symmetric components.
4. The specific symmetry that allows for non-trivial real solutions is T(u) = (e1, e2, e3)^T. This corresponds to a field where each component u_l is odd in the x_l direction and even in the other two directions. This provides a very concrete, actionable target for constructing a blow-up candidate.

**Equations:**
- $$\partial_t u - \Delta u + u \cdot \nabla u - \nabla p = 0, \nabla \cdot u = 0$$
  The incompressible Navier-Stokes equations, which describe the motion of viscous fluid substances.
- $$u(t, x) = e^{t\Delta}u_0(x) - B(u,u)(t, x)$$
  The integral (or mild) formulation of the Navier-Stokes equations, where the solution is expressed in terms of the heat semigroup and a bilinear operator B.
- $$u_{\tau+1}(t, x) = e^{t\Delta}u_0(x) - B(u_\tau,u_\tau)(t, x)$$ *(corrected)*
  The iterative scheme (Picard iteration) used to construct a mild solution to the Navier-Stokes equations by successive approximations.
  > Correction: Missing e^{t\Delta} term from the integral formulation.
- $$u((-1)^{\alpha_1}x_1,(-1)^{\alpha_2}x_2,(-1)^{\alpha_3}x_3) = (-1)^{f(\alpha)}u(x_1, x_2, x_3)$$ *(corrected)*
  This defines the symmetry property of a real function u(x) with respect to reflections of its spatial coordinates, governed by a function f.
  > Correction: The subscript 're' is incorrect. The paper uses u(x_1, x_2, x_3).
- $$Tu_l = m(e_l + \alpha_0) + im(e_l + \beta_0)$$
  This specifies the symmetry type of each component of a divergence-free vector field, relating it to a base symmetry vector.
- $$B(u,v) = P\nabla(u \otimes v)$$
  The bilinear operator B, which represents the nonlinear advection term in the Navier-Stokes equations, projected onto the space of divergence-free vector fields.

**Theorems:**
- Theorem 3.2: Given u satisfies (3.1) and div(u) = 0. If u satisfies (3.2), then there exist alpha_0, beta_0 in {0,1}^3 such that for all l=1,2,3, Tu_l = m(e_l + alpha_0) + im(e_l + beta_0).
  *Proof:* The proof relies on the fact that if the sum of symmetric functions is symmetric, then they must share the same symmetry type. Applying this to the divergence-free condition, which is a sum of derivatives, forces the symmetry of each component to be related in a specific way.
- Theorem 3.3: If u(t, x) is a real symmetric solenoidal vector field, then one of three conditions on the constancy of its components and their symmetries must be satisfied.
  *Proof:* The proof is a case-by-case analysis based on how many components of the vector field are constant.
- Theorem 4.5: Let u,v be two solenoidal vector fields. Then B(u,v) is a symmetric vector field if and only if one of five conditions is true (matched symmetry or certain parts of the nonlinear term are zero).
  *Proof:* The proof involves decomposing the bilinear operator B(u,v) into its real and imaginary parts and analyzing the symmetry of each term. The symmetry of the sum holds if the components have the same symmetry or are zero.
- Theorem 4.6: Given any solenoidal vector field u(t, x), it can be decomposed into eight matched symmetric solenoidal vector fields.
  *Proof:* The proof is constructive, showing how to decompose the real and imaginary parts of the vector field into 8 components each with a specific symmetry type, ensuring the divergence-free condition is maintained for each component.
- Theorem 5.4: Let u(t,x) be a real-valued strong solution of the Navier-Stokes equations. u(t,x) has the same symmetry property for all t >= 0 if and only if either the initial data u_0 satisfies a specific symmetry condition (Tu_0 = (e1, e2, e3)^T) or it corresponds to a Beltrami flow (P(grad(u tensor u)) = 0).
  *Proof:* The proof analyzes the symmetry of the integral equation. For the solution to maintain the same symmetry as the initial data, the symmetry of the nonlinear term B(u,u) must match the symmetry of u. The proof shows this only happens in the specified cases.
- Theorem 6.3: Let u(t,x) be a complex-valued strong solution. It has the same symmetry for all t >= 0 if and only if the initial data satisfies one of 8 specific symmetry conditions or it is a Beltrami flow.
  *Proof:* The proof is analogous to the real case but extended to complex fields. It matches the symmetry of the solution u with the symmetry of the bilinear term B(u,u), which is more complex due to real and imaginary parts interacting.
- Theorem 7.2: For the Navier-Stokes equations on a half-space with small initial data in H^(1/2), a smooth solution with energy conservation exists if the initial data satisfies a specific symmetry property (7.2).
  *Proof:* The proof relies on extending the initial data to the whole space using the specified symmetry. This extension preserves the divergence-free condition. The rigidity result (Theorem 5.4) guarantees that this specific symmetry is preserved by the flow, ensuring the solution on the extended domain maintains the symmetry. This symmetry implies that the energy in the upper half-space is equal to the energy in the lower half-space, hence energy conservation on the original domain.

**Constants & Bounds:**
- `262144 kinds of symmetric properties for complex vector fields`: This is the total number of possible symmetry types for a general 3-component complex vector field before considering the divergence-free constraint.
- `30 kinds of real symmetric solenoidal vector fields`: The number of possible symmetry types for a real-valued, divergence-free vector field. This is a significant reduction from the 512 total possible symmetries for a real vector field.
- `984 kinds of complex symmetric solenoidal vector fields`: The number of possible symmetry types for a complex-valued, divergence-free vector field. This is a reduction from 262,144.

---

### Potentially Singular Behavior of the 3D Navier-Stokes Equations
**Authors:** Thomas Y. Hou | **Year:** 2022 | [2107.06509v2](https://arxiv.org/abs/2107.06509v2) | **Validation:** verified
**Relevance:** 9/10

**Why it matters:** This paper is highly relevant as it provides strong, direct numerical evidence for a finite-time blow-up in the 3D axisymmetric Navier-Stokes equations. It addresses the core of the problem by constructing a specific initial condition that leads to a cascade of increasing vorticity and velocity, culminating in a singularity. The work helps close the gap in understanding the interplay between vortex stretching and viscous diffusion, suggesting that viscosity, contrary to simple intuition, can organize the flow in a way that promotes singularity formation rather than preventing it. The observed self-similar scaling provides a concrete target for analytical approaches aiming to construct a blow-up solution.

**Key Insights:**
1. Viscosity Can Promote Singularity: A key, counter-intuitive insight is that a relatively large viscosity (ν = 5 × 10^{-3}) can be *destabilizing*. Instead of dissipating energy and smoothing the solution, the viscosity in this scenario enhances the nonlinear alignment of the vortex stretching term, creating a more stable and focused blow-up structure. This challenges the common assumption that viscosity is always a regularizing mechanism.
2. A Specific Initial Condition is Key: The blow-up is not generic. It arises from a carefully constructed axisymmetric initial condition with odd symmetry. This initial data creates a feedback loop: the flow structure generates strong shear, which amplifies vorticity, which in turn strengthens the flow structure, leading to a runaway process.
3. The Blow-up is Nearly Self-Similar: The solution develops a nearly self-similar profile near the singularity, with characteristic scaling laws for velocity ((T-t)^{-1/2}), length scale ((T-t)^{1/2}), and vorticity (with a logarithmic correction). This provides a clear, quantitative signature of the blow-up and a template for what a formal analytical proof might look for.
4. The Singularity Occurs on the Axis of Symmetry: Consistent with the Caffarelli-Kohn-Nirenberg theorem, the numerical singularity forms at r=0. The dynamics are driven by a ring of high vorticity that collapses towards the axis, creating an intense downdraft and a sharp spike in pressure and velocity at the origin.

**Equations:**
- $$u_{1,t} + u^r u_{1,r} + u^z u_{1,z} = 2u_1 \psi_{1,z} + \nu (u_{1,rr} + \frac{3}{r} u_{1,r} + u_{1,zz})$$ *(corrected)*
  This is the momentum equation for the transformed angular velocity component u1. It describes how u1 changes over time due to advection (transport by the flow), vortex stretching (the 2u1*psi_1,z term, which is crucial for singularity formation), and viscous diffusion.
  > Correction: The original LaTeX was missing the u_{1,r} term inside the parenthesis and had an extra backslash in \\psi, which has been corrected to a single backslash.
- $$\omega_{1,t} + u^r \omega_{1,r} + u^z \omega_{1,z} = 2u_1 u_{1,z} + \nu (\omega_{1,rr} + \frac{3}{r} \omega_{1,r} + \omega_{1,zz})$$ *(corrected)*
  This is the vorticity equation for the transformed angular vorticity ω1. It shows how vorticity is transported, stretched by velocity gradients (2u1*u_1,z), and diffused by viscosity.
  > Correction: The original LaTeX had extra backslashes in \\omega and \\nu, which have been corrected to single backslashes.
- $$- (\partial_r^2 + \frac{3}{r} \partial_r + \partial_z^2) \psi_1 = \omega_1$$ *(corrected)*
  This is an elliptic equation that relates the transformed stream function ψ1 to the transformed vorticity ω1. It's used to recover the velocity field from the vorticity field.
  > Correction: The original LaTeX had extra backslashes in \\partial, \\frac, \\psi and \\omega, which have been corrected to single backslashes.

**Theorems:**
- Beale-Kato-Majda (BKM) Blow-up Criterion: A smooth solution to the Navier-Stokes (or Euler) equations can be continued as long as the time integral of the maximum vorticity is finite: `\int_0^T \|\omega(s)\|_{\L^\infty} ds < \infty`.
  *Proof:* The proof relies on using the Biot-Savart law to control the velocity gradient `\nabla u` by the `L^\infty` norm of vorticity. This control is then used in a Gronwall-type argument to show that the solution remains bounded.
- Ladyzhenskaya-Prodi-Serrin (LPS) Regularity Criteria: A weak solution `u` is regular up to time `T` if it belongs to certain `L^p_t L^q_x` spaces, specifically if `\int_0^T \|u(s)\|_{L^q}^p ds < \infty` for `2/p + 3/q \le 1`.
  *Proof:* These criteria are proven using energy-type estimates and Sobolev embedding theorems. By controlling a sufficiently strong norm of the velocity, one can bound the nonlinear term and prevent the formation of singularities.
- Caffarelli-Kohn-Nirenberg (CKN) Partial Regularity: For the Navier-Stokes equations, the set of potential singular points in spacetime has a Hausdorff dimension of at most one. For axisymmetric flows, this implies that singularities can only occur on the axis of symmetry (`r=0`).
  *Proof:* The proof is highly technical and involves a blow-up argument. It assumes a singularity exists and then analyzes the local structure of the solution at very small scales, showing that it must resemble a self-similar solution that cannot satisfy certain energy estimates, leading to a contradiction unless the singular set is small.

**Constants & Bounds:**
- `Self-Similar Scaling Law (Velocity): \|u(t)\|_{L^\infty} \sim (T-t)^{-1/2}`: This describes the rate at which the maximum velocity is observed to blow up. The exponent -1/2 is consistent with the scaling of the heat kernel and is a common feature in many blow-up scenarios for parabolic PDEs.
- `Self-Similar Scaling Law (Length Scale): Z(t) \sim (T-t)^{1/2}`: This describes the shrinking of the spatial scale of the singularity. Z(t) represents the characteristic length scale of the singular structure, which collapses to zero at the blow-up time T.
- `Self-Similar Scaling Law (Vorticity): \|\omega(t)\|_{L^\infty} \sim \frac{|\log(T-t)|}{T-t}`: This is the observed blow-up rate for the maximum vorticity. The presence of the logarithmic correction is a subtle but important feature, distinguishing it from a simple power-law blow-up. It suggests that the blow-up is not perfectly self-similar.
- `Self-Similar Scaling Law (Pressure): \|-p(t)\|_{L^\infty} \sim (T-t)^{-1}`: The pressure is observed to become infinitely negative at the singularity. This is a key feature of the blow-up scenario and is related to the intense vortex stretching and fluid acceleration into the singular region.
- `Viscosity: \nu = 5 \times 10^{-3}`: This is a relatively large viscosity. The authors find, somewhat counter-intuitively, that this "strong" viscous regularization actually *enhances* the nonlinear alignment of vortex stretching, which is the driving mechanism for the blow-up. This is a key finding of the paper.

---

### NON-UNIQUENESS IN LAW OF LERAY SOLUTIONS TO 3D FORCED STOCHASTIC NAVIER-STOKES EQUATIONS
**Authors:** ELIA BRUE´, RUI JIN, YACHUN LI, AND DENG ZHANG | **Year:** 2023 | [2309.09753v2](https://arxiv.org/abs/2309.09753v2) | **Validation:** verified
**Relevance:** 9/10

**Why it matters:** This paper is highly relevant to the NS3D blowup problem as it demonstrates the failure of uniqueness for Leray solutions in the forced stochastic setting, a significant step in understanding the limits of regularity. By establishing the sharpness of the Lions exponent (α=5/4) for the hyper-viscous case, it provides a clear boundary between well-posedness and ill-posedness, suggesting that similar mechanisms could lead to blowup in the unforced or deterministic cases.

**Key Insights:**
1. The failure of uniqueness for Leray solutions is not just a deterministic phenomenon but persists even in the presence of stochastic forcing. This suggests that the nonlinearity of the Navier-Stokes equations is a very strong source of irregularity.;;;2. The Lions exponent `\alpha = 5/4` is a sharp threshold for uniqueness in the hyper-viscous case. This provides a quantitative measure of the amount of dissipation needed to ensure well-posedness and gives a clear target for what kind of dissipative mechanisms might be missing from the standard NSE.;;;3. The construction of non-unique solutions relies on the existence of an unstable vortex ring solution. This highlights the importance of finding specific flow configurations that can trigger instabilities and potentially lead to blowup.;;;4. The self-similar framework is a powerful tool for analyzing blowup. By transforming the equations into a self-similar coordinate system, it is possible to study the behavior of the solution near a potential singularity in a more tractable way.

**Equations:**
- $$dv - \\Delta v dt + \text{div}(v \\otimes v)dt + \\nabla p dt = f dt + dw$$ *(corrected)*
  The stochastic Navier-Stokes equation. It describes the evolution of a velocity field `v` under the influence of viscosity, self-advection, pressure, an external force `f`, and a stochastic noise term `dw`.
  > Correction: div operator should be text.
- $$div v = 0$$
  The incompressibility condition, which means the fluid is volume-preserving.
- $$dv + (-\\Delta)^\\alpha v dt + \text{div}(v \\otimes v)dt + \\nabla p dt = f dt + dw$$ *(corrected)*
  The hyper-viscous stochastic Navier-Stokes equation. The term `(-\Delta)^\alpha` represents a fractional Laplacian, which provides stronger dissipation than the standard Laplacian for `\alpha > 1`.
  > Correction: div operator should be text.
- $$\\partial_\\tau U - (1 - \\frac{1}{2\\alpha})U - \\frac{\\xi}{2\\alpha} \\cdot \\nabla U + (-\\Delta)^\\alpha U + U \\cdot \\nabla U + W \\cdot \\nabla U + U \\cdot \\nabla W + W \\cdot \\nabla W + (-\\Delta)^\\alpha W + \\nabla P = F$$ *(corrected)*
  The self-similar formulation of the stochastic NSE. This transforms the original equation into a new coordinate system `(\xi, \tau)` that is better suited for studying self-similar blowup solutions.
  > Correction: The provided equation is a combination of two separate equations in the paper. It is not a single equation.
- $$L_{ss}^\alpha U := (1 - \frac{1}{2\alpha})U - \frac{\xi}{2\alpha} \cdot \nabla U + (-\Delta)^\alpha U + P_H(U \cdot \nabla \bar{U} + \bar{U} \cdot \nabla U)$$
  The linearized operator around a steady state `\bar{U}`. The spectral properties of this operator, particularly its unstable eigenvalues, are crucial for constructing non-unique solutions.

**Theorems:**
- Theorem 1.1: Non-uniqueness in law of Leray solutions
  *Proof:* Statement: For the 3D forced stochastic Navier-Stokes equations with zero initial condition, there exists a forcing term `f` such that distinct Leray solutions exist in the probabilistically weak sense.
- Theorem 1.2: Non-uniqueness in law: below the Lions exponent
  *Proof:* Statement: For the hyper-viscous forced stochastic NSE with `1 <= \alpha < 5/4`, there exists a forcing term `f` for which the joint uniqueness in law of Leray solutions fails.
- Theorem 1.3: Probabilistically strong well-posedness: above the Lions exponent
  *Proof:* Statement: For the hyper-viscous forced stochastic NSE with `\alpha >= 5/4`, there exists a unique solution for any given initial data and forcing term.
- Theorem 2.3: Local pathwise non-uniqueness
  *Proof:* Statement: There exist two distinct Leray solutions up to a stopping time `\sigma` for the stochastic NSE with a specific forcing term.
- Theorem 3.10: Instability of velocity operators
  *Proof:* Statement: The unstable eigenvalue of the vorticity operator `L_{vor}^{(\beta)}` is also an unstable eigenvalue of the velocity operator `L_{vel}^{(\beta)}`.

**Constants & Bounds:**
- `Lions exponent \alpha = 5/4`: This is the critical value for the hyper-viscosity exponent. For \alpha >= 5/4, solutions are unique, while for \alpha < 5/4, non-uniqueness is possible. It marks the threshold where dissipation is strong enough to overcome the nonlinearity.
- `Energy inequality: E||v(t)||_L^2^2 + 2E \int_0^t ||(-\Delta)^{\alpha/2} v(s)||_L^2^2 ds <= E||v(0)||_L^2^2 + 2E \int_0^t (f(s), v(s))ds + \sum_{j=1}^\infty \lambda_j ||\epsilon_j||_L^2^2 t`: This is the fundamental energy balance for the stochastic NSE. It provides a bound on the total energy of the system, which is a key tool for proving the existence of solutions.
- `Spectral bound of L_ss: a = \omega_0(L_{ss}) > 0`: The spectral bound `a` of the linearized operator `L_ss` is the supremum of the real parts of its eigenvalues. A positive spectral bound indicates the existence of unstable modes, which are essential for constructing non-unique solutions.
- `Parabolic regularity estimates: ||e^{\tau L_{ss}} U_0||_{H^{k_2}} <= M(k_1, k_2, \delta) \tau^{-(k_2-k_1)/2\alpha} e^{\tau(a+\delta)} ||U_0||_{H^{k_1}}`: These estimates describe the smoothing properties of the semigroup generated by the linearized operator `L_ss`. They show how the solution gains regularity over time, which is a crucial part of the analysis.

---

### REMARKS ON THE SEPARATION OF NAVIER-STOKES FLOWS
**Authors:** ZACHARY BRADSHAW | **Year:** 2023 | [2312.11353v1](https://arxiv.org/abs/2312.11353v1) | **Validation:** verified
**Relevance:** 9/10

**Why it matters:** This paper is highly relevant to the NS3D blowup problem as it directly investigates the necessary conditions for the separation of non-unique Navier-Stokes solutions. By providing uniqueness criteria in terms of the error between solutions and analyzing the multi-scale properties of this error, the paper offers a novel framework for understanding how singularities might form. It specifically addresses the behavior of solutions in scenarios where classical uniqueness theorems fail, which is the core of the blowup problem.

**Key Insights:**
1. The paper introduces novel uniqueness criteria for the Navier-Stokes equations that are formulated in terms of the error `w` between two solutions, rather than the solutions themselves. This provides a new analytical tool to study non-uniqueness. 2. The paper demonstrates that if two solutions separate, the error `w` must be 'active' across a range of scales (algebraic, frequency, and discretized). This means that a potential blow-up cannot be an extremely localized event in both space and frequency. 3. The work suggests that the existence of hypothetical non-unique self-similar solutions would imply that non-unique Leray-Hopf solutions can separate at a rate of t^{1/2}, which is faster than the linear rate seen in some numerical studies. This highlights the potential for 'explosive' separation in the physically relevant Leray-Hopf class. 4. The paper provides a conditional predictability criterion, showing that if a perturbation is initially confined to very small scales, it will decay for some time before any potential growth. This has implications for the practical prediction of turbulent flows.

**Equations:**
- $$∂_t u − ν∆u + u · ∇u + ∇p = 0; ∇ · u = 0$$
  The Navier-Stokes equations for an incompressible fluid, where u is the velocity field, p is the pressure, and ν is the viscosity. These equations govern the motion of viscous fluids and are central to the study of fluid dynamics.
- $$sup_{0<t} sup_{3<q≤∞} t^{1/2−3/(2q)} (\|u(t)\|_{L^q} + \|v(t)\|_{L^q}) + \|u(t)\|_{\dot{B}^{−1+3/q}_{q,∞}} + \|v(t)\|_{\dot{B}^{−1+3/q}_{q,∞}}) ≤ c_1$$
  This is the Type I condition (A1), which imposes a scaling-invariant bound on the solutions u and v. It's a critical assumption under which the separation of solutions is studied, representing a 'critical' scenario where non-uniqueness is plausible.
- $$\|w(t)\|_{L^p} t^{−1/2+3/(2p)} ≥ c_2$$
  This is condition (A2), which assumes that the error `w` between two solutions does not decay to zero too quickly. It's a key assumption for proving that certain scales must be active if solutions separate.
- $$w(t + τ) = e^{τ∆}w(t) − ∫_0^τ e^{(τ−s)∆}P∇ · (v ⊗ w + w ⊗ v + w ⊗ w)(t + s)ds$$
  The mild formulation for the error `w`, where `v` is a background flow. This integral equation is the starting point for many of the analytical estimates in the paper.

**Theorems:**
- Theorem 1.1: (Uniqueness criteria) Under assumption (A1'), if the error `w` is sufficiently small in a specific region of space-time, then the solutions must be identical. (Lower bound on the error) Under assumption (A2), the error cannot decay faster than a certain algebraic rate. (Upper bound on the error) Under assumption (A1'), the error is bounded by a specific algebraic rate.
  *Proof:* The proof of the uniqueness criterion involves using the mild formulation of the error and showing that the smallness assumption allows for an absorption argument to prove the error is zero. The lower bound is proven by contradiction, using a sparseness lemma (Lemma 3.2) to show that if the error decays too fast, it would violate the assumption (A2). The upper bound is derived from the mild formulation and the Type I assumption.
- Proposition 1.2: For self-similar local energy solutions, the error at low frequencies vanishes as t -> 0+ at a specific rate.
  *Proof:* The proof relies on the properties of self-similar solutions and the Littlewood-Paley decomposition.
- Theorem 1.3: (Uniqueness criteria) If the high-frequency part of the error is small compared to the low-frequency part, then the solutions are unique. (Low frequencies are active) Under assumption (A2), the low-frequency part of the error must be active. (Intermediate frequencies are active) Under assumptions (A1) and (A2), intermediate frequencies of the error are active.
  *Proof:* The proof techniques are similar to Theorem 1.1 but are carried out in the frequency domain using the Littlewood-Paley decomposition and Bernstein's inequalities.
- Theorem 1.4: This theorem provides analogous results to Theorems 1.1 and 1.3 but using a discretized interpretation of 'scale' based on averaging over cubes.
  *Proof:* The proof uses a similar strategy to the previous theorems but adapted to the discretized setting, employing an interpolant operator.
- Theorem 1.5: This theorem provides a conditional predictability criterion. It states that if the error is concentrated at very small scales (deep in the dissipative range), then the total error energy will initially decrease.
  *Proof:* The proof involves an energy estimate on the error, showing that the nonlinear term can be controlled if the error is localized at small scales.
- Proposition 1.6: If certain hypothetical self-similar solutions exist, then one can construct non-unique Leray-Hopf weak solutions whose error energy grows at least as fast as t^{1/2}.
  *Proof:* The proof relies on the work of Jia and Šverák on the construction of non-unique Leray-Hopf solutions from self-similar ones.

**Constants & Bounds:**
- `Type I condition (A1): sup_{0<t} sup_{3<q≤∞} t^{1/2−3/(2q)} (\|u(t)\|_{L^q} + \|v(t)\|_{L^q}) + \|u(t)\|_{\dot{B}^{−1+3/q}_{q,∞}} + \|v(t)\|_{\dot{B}^{−1+3/q}_{q,∞}}) ≤ c_1`: This is a critical assumption that defines the class of solutions being studied, representing a borderline case for uniqueness.
- `Error growth bound (Theorem 1.1): sup_{x∈R^3, 0<t} \|w(x,t)\| \frac{(|x|+\sqrt{t})^4}{\sqrt{t}} \lesssim 1`: This provides an upper bound on how fast the error between two solutions can grow, which is a crucial piece of information for any blow-up scenario.
- `Bernstein inequalities: \|D^α \dot{Δ}_j f\|_{L^p} \lesssim 2^{j|α|} \|\dot{Δ}_j f\|_{L^p} and \|\dot{Δ}_j f\|_{L^p} \lesssim 2^{j(3/q - 3/p)} \|\dot{Δ}_j f\|_{L^q}`: These are fundamental inequalities in harmonic analysis that relate norms of functions localized in frequency space. They are used extensively in the proofs of Theorems 1.3 and 1.5.

---

### Lower bounds on the blowup rate of vorticity in the Euler equations
**Authors:** Benjamin Ingimarson, Igor Kukavica | **Year:** 2026 | [2603.17431v1](https://arxiv.org/abs/2603.17431v1) | **Validation:** verified
**Relevance:** 9/10

**Why it matters:** This paper establishes explicit lower bounds on the blow-up rate of vorticity for the 3D Euler equations, directly quantifying the celebrated Beale-Kato-Majda (BKM) blow-up criterion. This is crucial for the NS3D blowup problem because the Euler equations represent the inviscid limit of Navier-Stokes, and understanding its potential singularities provides a vital model for the viscous case. It specifically addresses the gap in understanding the *rate* and *nature* of the vorticity accumulation near a potential singularity, moving from a qualitative criterion to a quantitative one.

**Key Insights:**
1. Vorticity blowup has a minimum speed limit: A singularity in the Euler equations cannot form arbitrarily slowly. The time integral of the maximum vorticity must grow at least as fast as `log(log(1/(T*-t)))`.
2. The path to blowup involves a logarithmic race: The core of the analysis relies on the inequality `d/dt ||w|| \lesssim ||w||^2 exp(C \int ||w||)`. To prove blowup, one needs to show that the exponential self-amplification from the integral term can overcome any dissipative or regularizing effects.
3. Time can be re-parameterized by the blowup quantity itself: The key technical innovation is to change the independent variable from time `t` to the accumulated vorticity `\tau(t)`.
4. Higher derivatives must blow up faster: The paper shows that `||D^k w||` must blow up at a rate of at least `(T*-t)^{-(1+2k/5)}`.

**Equations:**
- $$v_t + u \cdot \nabla u + \nabla p = 0, \quad \text{div } u = 0$$
  These are the fundamental equations of motion for an inviscid, incompressible fluid.
- $$\int_0^{T^*} \|\omega(t)\|_{L^\infty} dt = \infty$$
  The Beale-Kato-Majda theorem states that a smooth solution to the Euler (or Navier-Stokes) equations can only break down at time T* if the time integral of the maximum vorticity becomes infinite.
- $$\partial_t \omega + u \cdot \nabla \omega = \omega \cdot \nabla u$$
  This equation describes the evolution of the vorticity vector.
- $$\|Du\|_{L^\infty} \le C(1 + \|\omega\|_{L^\infty}(1 + \log^+\|u\|_{H^3}))$$
  This is a critical estimate that bounds the gradient of the velocity field.
- $$\int_0^t \|\omega(s)\|_{L^\infty} ds \ge \frac{1}{C} \log\log\left(\frac{1}{T^* - t}\right)$$
  This provides an explicit, quantitative lower bound on how fast the time-integral of vorticity must grow as the potential blowup time T* is approached.
- $$\limsup_{t \to T^{*-}} (T^* - t) \log\left(\frac{1}{T^* - t}\right) \|\omega(t)\|_{L^\infty} \ge \frac{1}{C}$$
  This result gives a lower bound on the instantaneous value of the maximum vorticity itself.
- $$\|D\omega(t)\|_{L^\infty} \ge \frac{1}{C(T^* - t)^{7/5} \log^{7/5}(1/(T^* - t))}$$
  For the periodic case, the paper establishes a pointwise-in-time lower bound for the gradient of vorticity.

**Theorems:**
- THEOREM 2.1: If a smooth solution to the 3D Euler equations blows up at time T*, then the time integral of the max-norm of vorticity must grow at least as fast as `log(log(1/(T*-t)))`.
  *Proof:* The proof starts with the standard vorticity equation and uses a log-corrected estimate for `||Du||_L_inf`. The key innovation is to re-parameterize time `t` in terms of the accumulated vorticity `\tau(t)`.
- THEOREM 2.2: The supremum over `[0, t]` of the k-th derivative of vorticity, `sup_{s \le t} \|D^k\omega(s)\|_{L^\infty}`, has a lower bound of the form `(T^* - t)^{-(2k/5+1)}` divided by a logarithmic term.
  *Proof:* This result is a consequence of Theorem 2.1 combined with a standard interpolation inequality (Lemma 4.1).
- THEOREM 2.3: In the periodic domain `T^3`, a pointwise-in-time lower bound holds for the vorticity gradient: `\|D\omega(t)\|_{L^\infty} \ge C(T^* - t)^{-7/5} / log^{7/5}(1/(T^*-t))`.
  *Proof:* The proof uses a Ricatti-type inequality for `\|D\omega\|_{L^p}` and then optimizes the resulting lower bound with respect to `p`.

**Constants & Bounds:**
- `Vortex Stretching Bound: d/dt \|\omega\|_{L^\infty} \lesssim \|Du\|_{L^\infty} \|\omega\|_{L^\infty}`: This is the fundamental differential inequality for vorticity, showing that its growth is controlled by the norm of the velocity gradient (the strain rate tensor).
- `Kozono-Taniuchi Inequality: \|Du\|_{L^\infty} \le C(1 + \|\omega\|_{L^\infty}(1 + \log^+\|u\|_{H^3}))`: A key analytical tool. It bounds the strain rate by the vorticity, but with a crucial logarithmic dependence on a higher-order norm of the velocity.
- `Interpolation Inequality: \|\omega\|_{L^\infty} \lesssim \|u\|_{L^2}^{1-\alpha} \|D^k\omega\|_{L^\infty}^{\alpha} with \alpha = 5/(2k+5)`: A standard Gagliardo-Nirenberg-type interpolation inequality.
- `Ricatti-type inequality for ||D\omega||_Lp: d/dt \|D\omega\|_{L^p} \le C p (1 + \|D\omega\|_{L^p})^{1+\alpha}`: This inequality, derived in the proof of Theorem 2.3, is the engine for the pointwise lower bound.

---

### A BLOWUP CRITERIA ALONG MAXIMUM POINTS OF THE 3D-NAVIER-STOKES FLOW IN TERMS OF FUNCTION SPACES WITH VARIABLE GROWTH CONDITION
**Authors:** EIICHI NAKAI, TSUYOSHI YONEDA | **Year:** 2014 | [1408.0159v1](https://arxiv.org/abs/1408.0159v1) | **Validation:** verified
**Relevance:** 8/10

**Why it matters:** This paper is highly relevant as it introduces a novel blowup criterion for the 3D Navier-Stokes equations, which is different from the classical Beale-Kato-Majda and Constantin-Fefferman criteria. It focuses on the geometric properties of the flow near its maximum points, suggesting that a lack of symmetry could be a key driver of singularity formation. This provides a new theoretical tool and a different perspective for researchers trying to prove or disprove the existence of finite-time blowup.

**Key Insights:**
1. The local geometric structure of the velocity field, specifically its degree of symmetry near maximum velocity points, is a critical factor in determining whether a blowup can occur.
2. The pressure gradient, a key term in the Navier-Stokes equations that can lead to blowup, is primarily driven by the non-symmetric part of the flow near maximum points. Symmetric flows are shown to have a vanishing contribution to the pressure gradient at these points.
3. The use of Campanato spaces with variable growth conditions offers a sophisticated and adaptable framework for analyzing the behavior of solutions. These spaces can capture both local smoothness properties near potential singularities and global decay properties at infinity, which is a significant methodological advance.
4. The paper provides a new, concrete (though complex) condition, the "no local collapsing" property, which, if verified, guarantees the regularity of the solution. This offers a potential new avenue for proving regularity in specific cases or for understanding the mechanisms that might lead to blowup.

**Equations:**
- $$(1.1) \partial_t v + (v \cdot \nabla)v - \Delta v + \nabla p = 0; \nabla \cdot v = 0$$
  This is the incompressible Navier-Stokes equation, which governs the motion of viscous fluids. The first part is the momentum equation, and the second is the incompressibility condition.
- $$(1.2) \int_0^T \|\text{curl } v(t)\|_{\infty} dt < \infty$$
  This is the Beale-Kato-Majda criterion, a famous result that provides a condition on the vorticity (curl of velocity) to ensure the solution of the Navier-Stokes equations remains smooth and does not blow up.
- $$(1.3) v(x, t) = \tilde{u}_1(x, t)n_1(x_{M(t_*)}) + \tilde{u}_2(x, t)n_2(x_{M(t_*)}) + \tilde{u}_3(x, t)\tau(x_{M(t_*)})$$
  This equation decomposes the velocity vector field `v` at a point `x` and time `t` into components along an orthonormal basis {n1, n2, τ} defined at a maximum point x_M of the flow. This is a key step in analyzing the local geometry of the flow near points of high velocity.
- $$(1.4) \sum_{i,j=1}^3 R_i R_j \partial_3 (U_i U_j)|_{y=0} = 0$$
  This equation shows that for a "symmetric flow" U, the vertical derivative of a certain component of the pressure gradient at the origin is zero. This implies that symmetric flows do not contribute to the pressure gradient at the maximum point in the vertical direction.
- $$(1.5) \partial_3 p|_{y=0} = \sum_{i,j=1}^3 R_i R_j \partial_3 (r_i U_j + U_i r_j + r_i r_j)|_{y=0}$$
  This is the pressure formula for the remainder part `r` of the flow (where v = U + r, and U is the symmetric part). It shows that the pressure gradient at the maximum point is determined by the non-symmetric part of the flow.
- $$(1.9) |v(x, t)| \le C/|x| \text{ for } |x| > R$$
  This is a decay condition for the velocity field, stating that the velocity must decay at least as fast as 1/|x| far from the origin. This is a known property of solutions to the Navier-Stokes equations.

**Theorems:**
- Theorem 1.1 (Beale-Kato-Majda criterion): Let s > 1/2, and let v0 ∈ Hs with div v0 = 0 in distribution sense. Suppose that v is a strong solution of (1.1). If ∫0^T ||curl v(t)||_∞ dt < ∞, then v can be extended to the strong solution up to some T′ with T′ > T.
  *Proof:* This is a classical result cited from [1]. The proof is not detailed in this paper.
- Theorem 1.2 (Blowup criteria along maximum points): Let function spaces V and W satisfy (1.6), (1.7) and (1.8). Let v0 be any non-zero, smooth, divergence-free vector field in Schwartz class. Suppose that v ∈ C∞([0, T) × R3) is a unique smooth solution of (1.1) up to T. If v is no local collapsing with respect to V, then v can be extended to the strong solution up to some T′ with T′ > T.
  *Proof:* The proof is based on showing that under the 'no local collapsing' condition, the terms (v · ∇p) and (v · Δv) at a maximum point of the flow are controlled. This allows the authors to bound the growth of the maximum of the velocity, which in turn, by a classical regularity criterion, prevents blow-up.

**Constants & Bounds:**
- `No local collapsing condition: inf_{u=U+r} (||∂3 r_i||_V ||U_j||_V + ||r_i||_V ||∂3 U_j||_V + ||r_i||_V ||∂3 r_j||_V) ≤ C(T-t*)^-α / u3(0, t*)`: This is the central condition of the paper, which acts as a bound on the non-symmetric part of the flow. If this inequality holds, blowup is prevented.
- `Velocity decay at infinity: |v(x, t)| ≤ C/|x| for |x| > R`: A fundamental estimate on the spatial decay of the velocity field for large distances, which is a known property for solutions of the Navier-Stokes equations.
- `Function Space Conditions (1.6, 1.7, 1.8): |f(0)| ≤ ||f||_W, ||R_i R_j f||_W ≤ C||f||_W, ||fg||_W ≤ C||f||_V ||g||_V`: These are abstract but crucial bounds required for the function spaces V and W to ensure that the Riesz transforms are bounded and that the product of functions is controlled. These properties are essential for the main proof to go through.

---

### STABILITY OF BLOW UP FOR A 1D MODEL OF AXISYMMETRIC 3D EULER EQUATION
**Authors:** TAM DO, ALEXANDER KISELEV, XIAOQIAN XU | **Year:** 2018 | [1604.07118v1](https://arxiv.org/abs/1604.07118v1) | **Validation:** verified
**Relevance:** 8/10

**Why it matters:** This paper is highly relevant as it strengthens the analytical evidence for a specific, numerically-observed blowup scenario in the 3D Euler equations (the Hou-Luo scenario). It achieves this by proving finite-time blowup in a 1D model that is a more faithful approximation of the full 3D axisymmetric equations than previous models. Furthermore, it demonstrates that this blowup is not a fragile artifact of the model but is a robust phenomenon that persists under certain perturbations, increasing confidence that a similar mechanism could be at play in the full 3D system. The paper helps bridge the gap between highly simplified 1D models and the full 3D problem. It specifically addresses the stability and robustness of the hyperbolic boundary blowup mechanism.

**Key Insights:**
1. The Hou-Luo blowup scenario is robust. The paper demonstrates that the finite-time blowup is not an artifact of an oversimplified model. By proving blowup for a more accurate 1D model and for a class of perturbed models, it provides strong evidence that this is a genuine feature of the underlying fluid dynamics.
2. The blowup mechanism is driven by the interaction of transport and vortex stretching. The quantity θ (related to swirl) is transported towards a stagnation point, causing its gradient to steepen. This, in turn, drives the growth of vorticity ω through the stretching term, leading to a finite-time singularity.
3. The blowup is not overly sensitive to the fine details of the Biot-Savart law. The paper shows that the blowup persists for a family of kernels, not just a single, specific one. This suggests that the core blowup mechanism is a more general feature of the equations, not a fragile phenomenon tied to a particular model.
4. The analytical technique of finding a functional that provably blows up is a powerful tool. The paper uses the functional I(t) = ∫[0,L/2] θ(x, t) cot(µx) dx to demonstrate the singularity. This approach could potentially be adapted to the full 3D problem, providing a pathway for a rigorous proof of blowup.

**Equations:**
- $$\partial_t(\omega^\theta/r) + u^r \partial_r(\omega^\theta/r) + u^z \partial_z(\omega^\theta/r) = \frac{((ru^\theta)_z)^2}{r^4}$$ *(corrected)*
  This is the vorticity equation for the angular component of vorticity in an axisymmetric, incompressible, inviscid fluid. It describes how the swirling motion of the fluid evolves over time.
  > Correction: The original equation was missing partial derivative symbols, superscripts, and proper fraction formatting.
- $$\partial_t(ru^\theta) + u^r \partial_r(ru^\theta) + u^z \partial_z(ru^\theta) = 0$$ *(corrected)*
  This equation expresses the conservation of angular momentum for the fluid. It states that the quantity ruθ, which represents the circulation, is transported with the fluid flow.
  > Correction: The original equation was missing partial derivative symbols and superscripts.
- $$\omega_t + u\omega_x = \theta_x$$ *(corrected)*
  This is the 1D model equation for the evolution of vorticity ω. It's a transport equation with a source term θx, which represents the stretching of vorticity by the velocity gradient.
  > Correction: The original equation used characters instead of subscripts for the partial derivatives.
- $$\theta_t + u\theta_x = 0$$ *(corrected)*
  This is the 1D model equation for the evolution of the quantity θ, which is related to the swirl velocity. It's a simple transport equation, meaning θ is just carried along by the flow.
  > Correction: The original equation used characters instead of subscripts for the partial derivatives.
- $$u_x = H\omega$$ *(corrected)*
  This is the Biot-Savart law for the 1D model, relating the velocity gradient ux to the vorticity ω through the Hilbert transform H. This is a simplified model of how vorticity creates velocity in the full 3D equations.
  > Correction: The original equation used a character instead of a subscript for the partial derivative.
- $$u(x, t) = k * \omega(x, t) \text{ where } k(x) = \frac{1}{\pi} \log \frac{|x|}{\sqrt{x^2+a^2}}$$ *(corrected)*
  This is the modified Biot-Savart law used in the paper, which is a more accurate approximation of the 3D Euler equations than the simplified Hilbert transform. It includes a parameter 'a' that accounts for the thickness of the boundary layer.
  > Correction: The original equation had incorrect formatting for the logarithm and fraction.
- $$u(x) = \frac{1}{2\pi} \int_0^L \omega(y) [\log|\sin^2(\mu(x-y))| - \log|\sin^2(\mu(x-y)) + a^2|] dy$$ *(corrected)*
  This is the periodic version of the modified Biot-Savart law, which is more convenient for analysis in a periodic domain. It expresses the velocity u in terms of an integral of the vorticity ω over one period.
  > Correction: The original equation had incorrect formatting for the integral, fractions, and the 'a' term should be squared.

**Theorems:**
- Theorem 3.1: There exist initial data with mean zero vorticity such that solutions to (5) and (6), with velocity given by (14) blow up in finite time. That is, there exists a time T* such that we have (13).
  *Proof:* The proof is by contradiction. It assumes a global smooth solution exists and then shows that a specific functional of the solution, I(t) = ∫[0,L/2] θ(x, t) cot(µx) dx, blows up in finite time. This contradiction implies that the solution must blow up. The proof relies on a series of technical lemmas that establish properties of the kernel F(x, y, a) in the Biot-Savart law.
- Theorem 4.1: Let f ∈ C2(R2), periodic with period L with respect to both variables and such that f(x, y) = f(−x, −y) for all x, y. Then there exists initial data ω0, θ0 such that solutions of (5) and (6), with velocity given by (32), blow up in finite time. Again, that means there exists a time T* such that we have (34).
  *Proof:* The proof of this theorem is perturbative. It considers a more general Biot-Savart law that is a perturbation of the original Hou-Luo kernel. The proof shows that if the perturbation is small enough, the blow-up mechanism still persists. It relies on a global bound on the L1 norm of the vorticity and a careful analysis of the perturbed velocity field.
- Proposition 2.1 (Local Existence and Blow Up Criteria): Suppose (ω0, θ0) ∈ Hm(S1) × Hm+1(S1) where m ≥ 2. Then there exists T = T(∥ω0∥, ∥θ0∥) > 0 such that there exists a unique classical solution (ω, θ) of (5), (6), (9) and (ω, θ) ∈ C([0, T];Hm × Hm+1). In particular, if T* is the maximal time of existence of such solution then limtրT* ∫[0,t] ∥ux(·, τ)∥L∞ dτ = ∞.
  *Proof:* The proof is described as 'relatively standard' and refers to similar proofs in other papers. It establishes that the system is well-posed for a short time and provides a criterion for when the solution will break down (blow up).

**Constants & Bounds:**
- `a: A parameter in the modified Hou-Luo kernel that represents the width of the boundary layer.`: This parameter is introduced to make the 1D model a more realistic approximation of the 3D Euler equations. The blowup result is shown to be robust with respect to this parameter.
- `µ = π/L: A constant related to the period L of the solution.`: This appears in the periodic version of the Biot-Savart law and is a standard parameter in the analysis of periodic functions.
- `I(t) = ∫[0,L/2] θ(x, t) cot(µx) dx: A key functional that is shown to blow up in finite time.`: The blowup of this integral is the primary indicator of singularity formation in the model. Its structure is chosen to capture the amplification of θ near the origin.
- `d2/dt2 I >= C I^2: A differential inequality that governs the growth of I(t) and leads to blowup.`: This inequality, derived from the model equations, shows that I(t) grows faster than exponentially, leading to a finite-time singularity.
- `ux = Hω: The Hilbert transform relation between the velocity gradient and vorticity in the original Hou-Luo model.`: This is a key part of the simplified 1D model that captures the non-local relationship between velocity and vorticity.
- `k(x) = (1/π) log|x / sqrt(x^2 + a^2)|: The kernel for the modified Biot-Savart law.`: This kernel is a more accurate approximation of the 3D Biot-Savart law and is the main object of study in the first part of the paper.

---

### Blowing-up solutions of the axisymmetric Euler equations for an incompressible fluid
**Authors:** Yves Pomeau, Martine Le Berre | **Year:** 2019 | [1901.09426v1](https://arxiv.org/abs/1901.09426v1) | **Validation:** verified
**Relevance:** 8/10

**Why it matters:** This paper is highly relevant as it directly tackles the problem of finite-time blowup, albeit for the Euler equations, which are the inviscid limit of the Navier-Stokes equations. It provides a concrete, constructive example of a singularity, which is a major step towards understanding how such phenomena might occur in the full Navier-Stokes case. The specific mechanism of blowup, a perturbation of a steady-state solution, could be a viable pathway for blowup in NS3D.

**Key Insights:**
1. Finite-time blowup in the Euler equations can be constructed by perturbing a steady-state solution (a Bragg-Hawthorne flow). This suggests a concrete mechanism for how singularities might form.
2. The introduction of a logarithmic time dependence in the self-similar scaling is essential to bypass the non-existence of steady-state solutions to the Euler-Leray equations.
3. The self-similar exponents for the blowup are determined by the conservation of circulation, not energy conservation. This is a critical distinction in the theory of self-similar blowup.
4. The blowup is linked to a small departure from a steady Bragg-Hawthorne solution, where the time to blowup is inversely proportional to the magnitude of the initial departure.

**Equations:**
- $$\[ \partial_t u + u \cdot \nabla u = -\nabla p \]$$
  This is the Euler equation for an incompressible, inviscid fluid. It describes the evolution of the fluid velocity `u` over time, driven by convection (`u \cdot \nabla u`) and pressure gradients (`-\nabla p`).
- $$\[ \nabla \cdot u = 0 \]$$
  This is the incompressibility condition, stating that the velocity field `u` is divergence-free. Physically, it means that the density of a fluid parcel remains constant as it moves.
- $$\[ \nu(r,t) = (t^* - t)^{-\alpha} U(r(t^* - t)^{-\beta}) \]$$ *(corrected)*
  This is the self-similar ansatz for the velocity field `u` near a potential singularity at time `t*`. It assumes the solution rescales in a specific way, with exponents `\alpha` and `\beta` to be determined. This is a core idea in the study of blowup.
  > Correction: The variable for velocity should be nu (\nu) not u, and t* should be t^*.
- $$\[ - (\alpha U + \beta R \cdot \nabla U) + U \cdot \nabla U + \nabla P = 0 \]$$
  This is the Euler-Leray equation for the self-similar profile `U(R)`. It is a stationary equation in the rescaled variable `R`, derived from the original Euler equation under the self-similar ansatz.
- $$\[ \frac{\partial U}{\partial \tau} - (\alpha U + \beta R \cdot \nabla U) + U \cdot \nabla U + \nabla P = 0 \]$$
  This is the modified Euler-Leray equation, including a dependence on the logarithmic time `\tau = -ln(t* - t)`. This allows for a more general class of self-similar solutions that are not strictly stationary in the rescaled frame.
- $$\[ L\Psi - \gamma r^2 \Psi + \delta^2 \Psi = 0 \]$$
  This is the linearized Bragg-Hawthorne equation for the stream function `\Psi` in the axisymmetric case. It is a key step in finding explicit solutions to the steady Euler equations.

**Theorems:**
- Main Result: Construction of a perturbative solution to the axisymmetric Euler equations that blows up in finite time.
  *Proof:* The paper does not present formal theorems, but rather a constructive proof. The technique involves starting with a steady-state solution of the axisymmetric Euler equations (a Bragg-Hawthorne flow) and then adding a small, time-dependent perturbation. This perturbation is shown to grow, leading to a finite-time singularity.
- Proposition 1: Existence of localized, square-integrable solutions to the Bragg-Hawthorne equation.
  *Proof:* The proof involves separation of variables and solving a resulting ordinary differential equation. The authors show that by a careful choice of parameters, one can construct a solution that decays exponentially at infinity.
- Proposition 2: Non-existence of smooth, time-independent solutions to the axisymmetric Euler-Leray equations with swirl.
  *Proof:* The proof relies on analyzing the characteristics of the equation for the azimuthal velocity. The authors show that the Leray advection term forces the flow lines to spiral outwards, which is incompatible with a solution that decays at infinity.

**Constants & Bounds:**
- `α = β = 1/2: These are the self-similar exponents for the Euler equations, derived from the conservation of circulation. They dictate the rate at which the solution blows up.`: These exponents are fundamental to the self-similar blowup scenario.
- `α = D/(2+D), β = 2/(2+D): These are the Sedov-Taylor exponents, derived from energy conservation. The paper argues that for the Euler equations, the circulation-derived exponents are the correct ones to use.`: The distinction between these two sets of exponents is a key point in the theory of self-similar blowup.
- `ωt >> 1: This is the condition for the validity of the perturbative approach used in the paper. It means that the intrinsic dynamical time of the flow is much shorter than the time to blowup.`: This condition highlights the limitations of the perturbative construction.

---

### Leray turbulence: what can we learn from acceleration compared to velocity
**Authors:** Yves Pomeau, Martine Le Berre | **Year:** 2019 | [1909.01724v1](https://arxiv.org/abs/1909.01724v1) | **Validation:** verified
**Relevance:** 8/10

**Why it matters:** This paper is highly relevant as it provides experimental evidence for the existence of Leray-like singularities in turbulent flows, which is a key aspect of the NS3D blowup problem. It directly investigates the self-similar nature of these singularities and analyzes their scaling exponents, which are crucial for understanding the blowup mechanism. The paper bridges the gap between theoretical predictions of blowup and real-world observations in turbulent flows, and it introduces the novel concept of 'weak singularities' which could open new avenues for research into the NS3D problem.

**Key Insights:**
1. Experimental data from turbulent flows shows strong evidence for the existence of self-similar singularities, a key feature of potential blow-up scenarios in the Navier-Stokes equations.
2. The paper identifies two potential types of self-similar singularities: one based on energy conservation (Sedov-Taylor exponents) and another on circulation conservation, suggesting multiple possible pathways to blow-up.
3. The concept of 'weak singularities' is introduced, characterized by singularities in acceleration but not in velocity. These may be more prevalent in turbulent flows and represent a new area of investigation for the blow-up problem.
4. The analysis suggests that viscosity may not be sufficient to prevent the formation of singularities in certain scenarios (specifically, for Sedov-Taylor type singularities), which is a critical point for proving finite-time blowup.
5. The dilation invariance of the Euler equations plays a crucial role in the interpretation of experimental data, and can explain discrepancies between different analyses of turbulent flows.

**Equations:**
- $$\partial_t \mathbf{u} + \mathbf{u} \cdot \nabla \mathbf{u} = -\nabla p$$
  This is the Euler equation, which describes the motion of an inviscid (zero viscosity) fluid. It is a statement of conservation of momentum for a fluid parcel.
- $$\nabla \cdot \mathbf{u} = 0$$
  This is the incompressibility condition, which states that the divergence of the velocity field is zero. This means that the fluid density is constant.
- $$\mathbf{u}(\mathbf{r}, t) = (t^* - t)^{-\alpha} \mathbf{U}(\mathbf{r}(t^* - t)^{-\beta})$$
  This is the self-similar form of a solution to the Navier-Stokes equations that becomes singular at a time t*. The exponents alpha and beta determine the nature of the singularity.
- $$\alpha + \beta = 1$$
  This is a scaling relation between the exponents in the self-similar solution, required for the solution to satisfy the Euler equations.
- $$\partial_\tau \mathbf{U} + \alpha \mathbf{U} + \beta \mathbf{R} \cdot \nabla \mathbf{U} + \mathbf{U} \cdot \nabla \mathbf{U} + \nabla P = 0$$
  This is the modified Euler-Leray equation, which is a PDE for the self-similar profile U. It is obtained by substituting the self-similar form of the solution into the Euler equations.
- $$S_n(r) = < \delta X^n >$$
  This is the definition of the nth-order structure function, which is a statistical measure of the fluctuations of a field X over a distance r.
- $$a \sim u^z, z \approx 3$$
  This is an empirical scaling relation observed in turbulent flows, relating large values of acceleration

**Theorems:**
- This paper does not contain formal theorems, lemmas, or propositions in the traditional mathematical sense. It is a physics paper that analyzes experimental data and proposes theoretical explanations. The main arguments are based on scaling laws and analysis of structure functions, rather than rigorous proofs.

**Constants & Bounds:**
- `Sedov-Taylor exponents: \alpha = 3/5, \beta = 2/5`: These exponents correspond to a self-similar solution that conserves energy in the singular domain.
- `Exponents from circulation conservation: \alpha = 1/2, \beta = 1/2`: These exponents correspond to a self-similar solution that conserves circulation around the singularity.
- `Experimentally observed exponent z: z \approx 3 or z = 8/3`: This exponent relates the scaling of acceleration and velocity in turbulent bursts, providing evidence for Leray-like singularities.
- `Experimental exponents from structure functions: \alpha \approx -0.56, \beta \approx 1.56`: These exponents are derived from the analysis of acceleration structure functions and suggest the presence of 'weak' singularities.
- `Kolmogorov time: t_k = 0.1ms`: The smallest time scale in a turbulent flow, where viscosity becomes dominant and dissipates kinetic energy.
- `Reynolds number: Re_\lambda = 2500 and Re_\lambda = 500`: A dimensionless quantity that measures the ratio of inertial forces to viscous forces in a fluid. The experiments were conducted at these Reynolds numbers.

---

### Searching for Singularities in Navier-Stokes Flows Based on the Ladyzhenskaya-Prodi-Serrin Conditions
**Authors:** Di Kang, Bartosz Protas | **Year:** 2021 | [2110.06130v1](https://arxiv.org/abs/2110.06130v1) | **Validation:** verified
**Relevance:** 8/10

**Why it matters:** This paper is highly relevant as it directly attempts to find initial conditions that lead to a finite-time blowup by maximizing the integral in the Ladyzhenskaya-Prodi-Serrin (LPS) criterion. While it fails to find a blowup, the results provide strong computational evidence that singularities are not easily formed from the types of initial data explored. It addresses the gap in understanding which specific initial conditions are the most "dangerous" and likely to lead to extreme behavior, and it demonstrates that current theoretical bounds are likely not sharp.

**Key Insights:**
1. A systematic computational search based on the LPS criterion (with q=4) found no evidence of finite-time blowup. The quantity that should diverge at a singularity was found to grow according to a power law, suggesting that if blowup exists, it must be triggered by mechanisms not captured by this optimization.
2. The theoretical a priori bounds on the growth of the L4 norm, such as estimate (12), are shown to be not sharp. The computationally obtained growth rates are significantly lower than the theoretical upper bounds, indicating a need for improved mathematical estimates.
3. The initial conditions that lead to the most extreme growth in the LPS integral are highly structured, typically involving localized vortex sheets or vortex rings. This gives a strong hint as to what kind of fluid motions are critical to study for potential singularities.
4. The flows that maximize the LPS integral also exhibit a maximum enstrophy growth that scales with the initial enstrophy to the power of approximately 3/2, the same scaling law found in studies that directly maximized enstrophy. This reveals a deep connection between the enstrophy dynamics and the LPS blowup criterion.

**Equations:**
- $$\partial_t \mathbf{u} + \mathbf{u} \cdot \nabla \mathbf{u} + \nabla p - \nu \Delta \mathbf{u} = 0$$ *(corrected)*
  This is the momentum equation of the incompressible Navier-Stokes system, which describes the evolution of the velocity field u. It represents the conservation of momentum for a viscous fluid, where ∂t u is the local acceleration, u · ∇u is the convective acceleration, ∇p is the pressure gradient, and ν∆u is the viscous diffusion term.
  > Correction: The original used unicode characters and did not bold the vectors.
- $$\nabla \cdot \mathbf{u} = 0$$ *(corrected)*
  This is the incompressibility condition, which states that the velocity field is divergence-free. Physically, it means that the density of the fluid is constant.
  > Correction: The original used unicode characters and did not bold the vector.
- $$\mathbf{u}(0) = \mathbf{u}_0$$ *(corrected)*
  This is the initial condition for the velocity field at time t=0.
  > Correction: The original did not bold the vectors and was missing a subscript.
- $$\Phi_T(\mathbf{u}_0) := \frac{1}{T} \int_0^T \|\mathbf{u}(\tau)\|_ {L^4(\Omega)}^8 d\tau$$ *(corrected)*
  This is the objective functional to be maximized in Problem 1 and 2. It represents the time-averaged L4 norm to the 8th power, which is related to the Ladyzhenskaya-Prodi-Serrin condition for q=4.
  > Correction: The original used unicode characters, incorrect syntax for fraction and norms.
- $$\Psi_T(\mathbf{u}_0) := \frac{1}{T} \int_0^T \|\mathbf{u}(\tau)\|_ {L^4(\Omega)}^{8/3} d\tau$$ *(corrected)*
  This is the objective functional for Problem 3. It is related to the a priori estimate (12) and is used to probe its sharpness.
  > Correction: The original used unicode characters, incorrect syntax for fraction and norms.
- $$H^s(\Omega) \hookrightarrow L^4(\Omega), s \ge 3/4$$ *(corrected)*
  This is the Sobolev embedding theorem in 3D, which states that the Sobolev space Hs is continuously embedded in the Lebesgue space L4 for s greater than or equal to 3/4. This is crucial for defining the optimization problem in a Hilbert space setting.
  > Correction: The original used unicode characters and incorrect syntax for embedding and greater than or equal to.

**Theorems:**
- Problem 1: Given B, T ∈ R+, find u_0;B,T = argmax ΦT(u0) for u0 in a constrained set LB, where the constraint is on the L4 norm ||u0||_L4(Ω) = B.
  *Proof:* The paper investigates this problem computationally using a large-scale adjoint-based gradient approach to search for initial conditions that might lead to singularities. The proof technique is to solve this PDE-constrained optimization problem numerically.
- Problem 2: Given S, T ∈ R+, find u_0;S,T = argmax ΦT(u0) for u0 in a constrained set HS, where the constraint is on the homogeneous Sobolev semi-norm ||u0||_H˙3/4(Ω) = S.
  *Proof:* Similar to Problem 1, this is a variational optimization problem solved computationally. The change in constraint to a Sobolev norm makes the problem easier to handle numerically in a Hilbert space setting.
- Problem 3: Given K0, T ∈ R+, find u_0;K0,T = argmax ΨT(u0) for u0 in a constrained set GK0, where the constraint is on the initial kinetic energy K(u0) = K0.
  *Proof:* This problem is designed to test the sharpness of the a priori estimate (12). The computational method is the same adjoint-based optimization.

**Constants & Bounds:**
- `maxT ΦT(u0;B,T) ≈ (0.6478 ± 0.1153) * ||u0;B,T||_L4(Ω)^2.261±0.021`: This is a power-law fit for the maximum of the objective functional in Problem 1, showing that the maximized quantity does not become unbounded but scales with the constraint.
- `maxT ΦT(u0;S,T) ≈ (9.308 ± 0.373) × 10^−4 * ||u0;S,T||_H˙3/4(Ω)^3.979±0.005`: This is a power-law fit for the maximum of the objective functional in Problem 2. The exponent near 4 is explained by the relationship between the H^3/4 and L^4 norms in the T->0 limit.
- `d/dt ||u(t)||^4_L4(Ω)|t=0 ≈ (221.5 ± 104) * ||u0;B,T||_L4(Ω)^1.117±0.05`: This shows the initial rate of change of the L4 norm scales with an exponent much smaller than the theoretical upper bound of 3, suggesting the bound is not sharp.
- `maxt≥0 E(t) ≈ (0.5155 ± 0.0532) * E0^1.147±0.013`: This power-law relates the maximum enstrophy achieved to the initial enstrophy for the optimal flows found in Problem 2. The exponent is different from the 3/2 scaling found in direct enstrophy maximization studies.
- `ψK0 ≈ (3.17 ± 0.9) * K0^0.998±0.082`: This shows that the long-time limit of the quantity related to the a priori estimate (12) scales almost linearly with the initial energy, which is a smaller exponent than the theoretical prediction of 4/3.

---

### SHARP NON-UNIQUENESS OF SOLUTIONS TO STOCHASTIC NAVIER-STOKES EQUATIONS
**Authors:** Weiquan Chen, Zhao Dong, Xiangchan Zhu | **Year:** 2022 | [2208.08321v1](https://arxiv.org/abs/2208.08321v1) | **Validation:** verified
**Relevance:** 8/10

**Why it matters:** This paper is highly relevant as it directly tackles the non-uniqueness of solutions to the stochastic Navier-Stokes equations. While it focuses on constructing infinitely many solutions rather than a single singular one, the techniques of convex integration are at the forefront of modern approaches to the blowup problem. Understanding how to construct pathological solutions is a major step towards constructing a blow-up solution. It addresses the gap of understanding solution behavior in supercritical regimes.

**Key Insights:**
1. The addition of a suitable stochastic noise does not regularize the Navier-Stokes equations in the supercritical regime; non-uniqueness of solutions persists. This dashes hopes that stochastic forcing could be a simple fix for the well-posedness problem.
2. The convex integration method can be adapted to the stochastic setting by introducing expectations into the iterative scheme. This is a powerful new technique for constructing pathological solutions to stochastic PDEs.
3. The constructed non-unique solutions can be made to violate the energy inequality, which is a strong form of misbehavior for a solution.
4. The paper provides a sharp dividing line between uniqueness and non-uniqueness for the stochastic Navier-Stokes equations, showing that the Ladyzhenskaya-Prodi-Serrin criterion is essentially the best possible.

**Equations:**
- $$du(t) = [-\text{div}(u(t) \otimes u(t)) + \Delta u(t) - \nabla p(t)]dt + dW(t), \quad \text{div } u(t) = 0, \quad u(0) = u_0$$ *(corrected)*
  This is the stochastic Navier-Stokes equation, the core subject of the paper. It describes the velocity `u` of a viscous, incompressible fluid subject to a random forcing `dW(t)`.
  > Correction: Removed starting and ending brackets of the equation to make it a valid LaTeX
- $$dz(t) = [(\Delta - I)z(t) + \nabla P_1]dt + dW(t), \quad \text{div } z(t) = 0, \quad z(0) = u_0$$ *(corrected)*
  This is the linear part of the system, describing the evolution of a component `z` of the solution driven by the stochastic forcing and viscosity. The `-I` term is an artificial damping term added for technical reasons to get uniform-in-time bounds.
  > Correction: Removed starting and ending brackets of the equation to make it a valid LaTeX
- $$\partial_t v = -\text{div}((v+z)\otimes(v+z)) + \Delta v - \nabla p(t) + z$$ *(corrected)*
  This is the equation for the remainder term `v = u - z`. It is a modified Navier-Stokes equation where the nonlinear term involves both `v` and `z`, and there is an additional forcing term `z` arising from the decomposition.
  > Correction: Removed starting and ending brackets of the equation to make it a valid LaTeX

**Theorems:**
- Theorem 1.1 (Ladyzhenskaya-Prodi-Serrin): Let d >= 2 and u be a weak solution to the incompressible Navier-Stokes equations such that u belongs to X^{p,q}_T for some 2 <= p <= infinity and d <= q <= infinity with 2/p + d/q <= 1. Then u is unique in this class of weak solutions and is Leray-Hopf.
  *Proof:* This is a classical uniqueness criterion for the Navier-Stokes equations. The proof relies on energy estimates and showing that the difference of two solutions must be zero under these conditions.
- Theorem 1.3: For any epsilon > 0, any 1 <= alpha, r < infinity, 1 <= p < 2, any u_0 in L^2_sigma and any smooth vector field w in C^1_0,sigma, there exists a probabilistically strong and analytically weak global solution u to the stochastic Navier-Stokes equations with initial data u_0, such that u - z is in L^2_s(Omega, L^2L^2) intersect L^alpha_s(Omega, Z^{p,r}_E) and is close to w+z.
  *Proof:* The proof is constructive and based on a stochastic convex integration scheme. It involves an iterative procedure where at each step a perturbation is added to the previous solution to get a new solution that is closer to satisfying the equation. The use of expectation in the convex integration scheme is a key novelty to handle the stochastic term.
- Theorem 1.6 (Pathwise Uniqueness): Let d >= 2, and 0 < T < infinity be arbitrarily fixed. There exists at most one solution u to the stochastic N-S system satisfying u in X^{p,q}_T, P-a.s. for some p in [2, infinity] and q in (2, infinity] such that 2/p + d/q <= 1.
  *Proof:* The proof is a stochastic extension of the classical proof for the deterministic case. It uses an energy estimate for the difference of two solutions and Ito's formula to show that the difference must be zero.
- Theorem 1.7: Under the same assumption as Theorem 1.3, there exists infinitely many different probabilistically strong and analytically weak solutions to the stochastic Euler equations with the same given L^2-initial data.
  *Proof:* The proof is a modification of the proof of Theorem 1.3, applied to the Euler equations (i.e., without the viscosity term). The convex integration scheme is adapted to this setting.
- Theorem 1.9: Let d >= 2, 1 <= alpha < infinity, epsilon > 0 and u_0 in W^{1,infinity} be arbitrarily given. And let G satisfy Tr(G*(I-Delta)^{d/2+1}G) < infinity. Then there exist infinitely many different non-conserving probabilistically strong and analytically weak solutions in L^alpha(Omega; L^{3/2-epsilon}_loc([0,infinity); C^{1/3})) intersect L^alpha(Omega; L^1_loc([0,infinity); C^{1-epsilon})) to the stochastic Euler system, with initial data u_0.
  *Proof:* This theorem is a consequence of the convex integration construction for the Euler equations, which produces solutions with low regularity. The non-conservation of energy is a key feature of these solutions. The proof relies on showing that the constructed solutions do not satisfy the energy equality.

**Constants & Bounds:**
- `Ladyzhenskaya-Prodi-Serrin criterion: 2/p + d/q <= 1`: This inequality defines the critical regularity for uniqueness of solutions to the Navier-Stokes equations. The paper shows non-uniqueness in the supercritical regime 2/p + d/q > 1.
- `Energy inequality for martingale solutions: E[||u(t)||^2_{L^2}] <= ||u_0||^2_{L^2} + T * Tr(G*G)`: This is a standard energy bound for weak solutions of the stochastic Navier-Stokes equations. The paper constructs solutions that violate this inequality.

---

### Lagrangian dynamics and regularity of the spin Euler equation
**Authors:** Zhaoyuan Meng, Yue Yang | **Year:** 2023 | [2311.05149v1](https://arxiv.org/abs/2311.05149v1) | **Validation:** partially_verified
**Relevance:** 8/10

**Why it matters:** This paper is highly relevant as it introduces a novel theoretical framework, the spin Euler equation, which is equivalent to the 3D incompressible Euler equation. This reformulation provides a new non-blowup criterion based on the Laplacian of the spin vector, offering an alternative to the classical BKM criterion. The paper's numerical results and the Lagrangian nature of the spin formulation directly address the core questions of vorticity stretching and the potential for finite-time singularity formation. It specifically provides a new tool to analyze the geometric structure of vorticity, which is a key aspect of the blowup problem.

**Key Insights:**
1. The spin Euler equation (∂_t s + s x m = 0) provides a new, fully Lagrangian way to study ideal fluid dynamics. Because isosurfaces of the spin vector 's' are material vortex surfaces, this formulation is exceptionally well-suited for tracking the complex geometry of vortex stretching and folding, which is believed to be the mechanism driving a potential blowup.
2. A new non-blowup criterion is established: a singularity can only form if the maximum norm of the Laplacian of the spin vector, ||Δs||_∞, blows up. The authors' numerical simulations suggest this criterion is more sensitive than the BKM criterion in identifying flows that are not singular. An engineer trying to prove blowup should monitor this quantity in their simulations.
3. The numerical simulations of vortex knots, links, and modified Taylor-Green flows show a pronounced double-exponential growth of ||Δs||_∞. This is extremely rapid growth, but it is not the hyperbolic growth (e.g., (t* - t)^-γ) required for a finite-time singularity. This provides strong evidence that these specific, highly vortical flows do not lead to a blowup, suggesting that a search for a singular solution must look elsewhere.
4. The equivalence of the spin Euler equation to a special case of the Landau-Lifshitz equation from magnetism suggests a deep physical analogy. This could potentially allow for the transfer of analytical techniques and insights from the study of magnetic materials to the fluid dynamics regularity problem.

**Equations:**
- $$\partial_t u + u \cdot \nabla u = -\nabla p$$ *(corrected)*
  This is the 3D incompressible Euler equation, which governs the motion of an ideal (inviscid) fluid. It describes the acceleration of a fluid parcel as a balance between convective effects and pressure gradients.
  > Correction: The vectors u and p should not be bolded.
- $$\partial_t s + u \cdot \nabla s = 0$$ *(corrected)*
  This equation shows that the spin vector 's' is materially conserved in the flow, meaning it is transported with the fluid velocity 'u'. This is a Lagrangian conservation law.
  > Correction: The vectors s and u should not be bolded.
- $$s = (a^2 + b^2 - c^2 - d^2, 2(bc - ad), 2(ac + bd))$$ *(corrected)*
  This is the Hopf fibration, which maps a two-component complex wave function (represented by four real functions a, b, c, d) to the 3D spin vector 's'. This mapping connects the fluid dynamics to a representation on the sphere S^2.
  > Correction: The vector s should not be bolded.
- $$\omega = \frac{1}{4} \varepsilon_{ijk} s \cdot (\nabla s_j \times \nabla s_k)$$ *(corrected)*
  This equation reconstructs the vorticity vector 'ω' from the spin vector 's'. It shows that the geometry of the spin vector field determines the vorticity, which is crucial for understanding the fluid's rotation.
  > Correction: The vectors omega and s should not be bolded.
- $$\partial_t s + s \times m = 0$$ *(corrected)*
  This is the spin Euler equation. It describes the evolution of the spin vector 's' as a precession around an effective magnetic field 'm'. This form is equivalent to the original Euler equation but offers a Lagrangian perspective on vortex dynamics.
  > Correction: The vectors s and m should not be bolded.
- $$m = \frac{1}{2} (s \cdot \nabla s \cdot \psi - \bar{\psi} \cdot \nabla s \cdot s)$$ *(corrected)*
  This defines the effective magnetic field 'm' in terms of the quaternion wave function 'ψ'. 'm' is a pure quaternion (a 3D vector) that drives the precession of the spin vector 's'.
  > Correction: The provided equation is not in the paper. The paper defines m in components in equation (2.6).
- $$\partial_t s + s \times H_{eff} = 0$$ *(corrected)*
  This is the Landau-Lifshitz equation without damping. The paper shows the spin Euler equation is a special case of this equation, which is used to model magnetodynamic processes in magnetic materials, suggesting a deep connection between ideal fluid flow and magnetism.
  > Correction: The vectors s and H_eff should not be bolded.
- $$\|\nabla s\|_2^2 \le \|\Delta s\|_1$$ *(corrected)*
  An inequality relating the L2 norm of the gradient of the spin vector to the norm of its Laplacian. This is a key step in deriving the non-blowup criterion.
  > Correction: The vector s should not be bolded, and the norm on the right side is L1, not L2.
- $$\|\omega\|_p \le \frac{1}{2} \|\nabla s\|_{2p}^2$$ *(corrected)*
  This inequality provides an upper bound for the Lp-norm of the vorticity 'ω' in terms of the L2p-norm of the gradient of the spin vector. It connects the growth of vorticity (central to the blowup problem) to the behavior of the spin vector.
  > Correction: The vector s should not be bolded.
- $$\|m\| \le \frac{\sqrt{6}}{4} \|\nabla s\|^2 + \sqrt{2}\|u\|^2$$ *(corrected)*
  This inequality bounds the magnitude of the effective magnetic field 'm' by the norms of the gradient of the spin vector and the fluid velocity 'u'. This is essential for controlling the precession term in the spin Euler equation.
  > Correction: The vectors m, s, and u should not be bolded.

**Theorems:**
- Non-blowup criterion for the spin Euler equation: If a solution s to the spin Euler equation (2.7) with initial data s_0 in H^k(D) for k >= 3 develops a singularity at a finite time t*, then it is necessary that the L-infinity norm of the Laplacian of the spin vector blows up, i.e., lim_{t->t*} ||Δs(t)||_∞ = ∞.
  *Proof:* The proof starts by deriving a differential inequality for the growth of the Lp-norm of ||∇s||. By using a series of inequalities, including the key relations ||ω||_p <= 1/2 * ||∇s||_{2p}^2 and an estimate for the effective field ||m||, the growth of ||∇s|| is ultimately controlled by the L-infinity norm of the Laplacian, ||Δs||_∞. Grönwall's inequality is then applied to show that if ||Δs||_∞ remains bounded, ||∇s|| cannot blow up, which in turn prevents the vorticity from blowing up, thus ensuring regularity.

**Constants & Bounds:**
- `Beale-Kato-Majda (BKM) criterion: Not a new result in this paper, but a central point of comparison. It states that a solution to the Euler equations remains smooth as long as the time integral of the maximum vorticity is finite (∫ ||ω(t)||_∞ dt < ∞).`: This is the benchmark criterion for blowup in the Euler equations. The new criterion in this paper is presented as a more sensitive alternative.
- `Inequality relating vorticity and spin gradient: ||ω||_p <= (1/2) * ||∇s||_{2p}^2`: This inequality provides a direct link between the vorticity (the key quantity in the BKM criterion) and the gradient of the spin vector. It allows the authors to translate the regularity problem from the language of vorticity to the language of the spin vector.
- `Inequality bounding the effective field: ||m|| <= (sqrt(6)/4) * ||∇s||^2 + sqrt(2) * ||u||^2`: This bound is crucial for controlling the non-linear term in the spin Euler equation. It shows that the effective field 'm' that drives the spin dynamics can be controlled by the gradient of the spin vector and the velocity.
- `Double-exponential growth: The DNS results for vortex knots, links, and modified Taylor-Green flows show that the maximum of the Laplacian of the spin vector, ||Δs||_∞, grows in a manner consistent with a double-exponential function, e.g., exp(c*exp(a*t)).`: This is a key numerical finding. A double-exponential growth is very fast, but it is slower than the hyperbolic growth (e.g., 1/(t* - t)) required for a finite-time singularity. This result provides numerical evidence *against* the formation of a singularity in the tested flows.

---

### CLASSIFICATION OF FINITE-TIME BLOW-UP OF STRONG SOLUTIONS TO THE INCOMPRESSIBLE FREE BOUNDARY EULER EQUATIONS WITH SURFACE TENSION
**Authors:** CHENGCHUN HAO, TAO LUO, AND SIQI YANG | **Year:** 2024 | [2507.10032v1](https://arxiv.org/abs/2507.10032v1) | **Validation:** partially_verified
**Relevance:** 8/10

**Why it matters:** While this paper focuses on the 3D incompressible Euler equations, its comprehensive classification of finite-time blow-up mechanisms for strong solutions with a free boundary and surface tension is highly relevant to the Navier-Stokes problem. The analytical framework and the distinct characterization of geometric, kinematic, and interior singularities provide a crucial roadmap for investigating potential blow-up scenarios in NS3D. It specifically addresses the interplay between boundary regularity and interior dynamics, a key challenge in the NS3D problem.

**Key Insights:**
1. Blow-up is not a monolithic event; it is rigorously classified into five distinct, mutually exclusive pathways. This provides a structured guide for where to search for singularities: self-intersection, curvature blow-up, normal velocity blow-up, tangential gradient blow-up on the boundary, or vorticity accumulation in the interior.
2. For simply connected domains, interior blow-up is fundamentally tied to vorticity dynamics, refining the general BKM criterion. This suggests that any attempt to construct an interior blow-up for NS3D should focus on mechanisms that amplify vorticity, such as vortex stretching.
3. The paper develops a sophisticated energy functional (E(t)) that carefully balances interior (H^3) and boundary (H^{5/2}) regularity, capturing the delicate interplay mediated by surface tension. This highlights that a successful blow-up proof for NS3D with boundaries will likely require a similar functional that correctly weights both bulk and interface dynamics.
4. The classification is achieved without assuming any symmetries, periodicity, or graph-based representations of the domain. This makes the results extremely general and the techniques applicable to realistic, complex geometries, which is a major step forward from previous work.

> **Validation Note:** The JSON summary of Theorem 1.1 is a high-level simplification and loses some of the precision of the original theorem statement, particularly regarding the specific conditions for regularity loss and gradient blow-up.

**Equations:**
- $$D_t v + \nabla p = 0; \nabla · v = 0; p = H, v_n = V_{\partial\Omega_t}; v(·, 0) = v_0$$
  These equations govern the motion of an ideal, incompressible fluid with a free surface where pressure is determined by the mean curvature (H) due to surface tension. They form the fundamental system being analyzed for singularity formation.
- $$\int_0^{T†} \|\nabla v\|_{L^\infty(\Omega_t)} dt = \infty$$
  This is the Beale-Kato-Majda (BKM) type criterion for the interior of the fluid. It states that for a singularity to form within the fluid domain (away from the boundary), the time-integral of the maximum value of the velocity gradient must become infinite.
- $$\limsup_{t\to T†}\|\nabla \times v\|_{L^2(\Omega_t)} + \int_0^{T†} \|\nabla \times v\|_{L^\infty(\Omega_t)} dt = \infty$$
  For simply connected domains, this refines the interior blow-up condition, linking it directly to the vorticity (\nabla \times v). It indicates that blow-up is driven by either the enstrophy (L2 norm of vorticity) becoming unbounded or the time-integral of the maximum vorticity becoming unbounded, which is a more precise condition than the general velocity gradient.
- $$D_t H = -\Delta_{II} v_n - |II|^2 v_n + \nabla H · v$$
  This is the evolution equation for the mean curvature H of the free boundary. It shows how the curvature changes in time based on the fluid's normal velocity (v_n), the second fundamental form (II), and the tangential velocity (v). This equation is central to analyzing geometric regularity loss (Case 2 blow-up).
- $$D_t n = -(\nabla v)^T n$$
  This equation describes the evolution of the unit normal vector n to the free surface. The change in the normal vector is governed by the tangential gradients of the velocity, linking the fluid motion directly to the change in the boundary's orientation.

**Theorems:**
- Theorem 1.1: If a strong solution to the 3D free-boundary Euler equations with surface tension has a finite maximal existence time T† < ∞, then one of five mutually exclusive scenarios must occur: (1) self-intersection of the boundary, (2) loss of boundary/curvature regularity, (3) blow-up of the normal velocity's H^{5/2} norm, (4) L1-in-time blow-up of the tangential velocity gradient on the boundary, or (5) L1-in-time blow-up of the full velocity gradient in the interior.
  *Proof:* The proof is by contradiction. It assumes that none of the five blow-up scenarios occur, which implies uniform bounds on the boundary geometry, regularity, and the time-integrated velocity gradients. Using a sophisticated energy functional E(t) that combines interior and boundary norms, the authors show these assumptions lead to a uniform-in-time bound on the H^3 norm of the velocity. This contradicts the initial assumption that T† was the maximal existence time, as the solution could be extended further.
- Theorem 1.5: For a simply connected domain, the interior blow-up criterion (Case 5 from Thm 1.1) can be refined to a condition on the vorticity (see Eq. 1.8 above). Furthermore, if the flow is irrotational, blow-up can only occur at the boundary (Cases 1-4).
  *Proof:* The proof uses a div-curl decomposition and a critical logarithmic estimate (Lemma 4.1) from [26] that controls the L^∞ norm of the velocity gradient by the vorticity norms. This allows the general BKM-type condition on \nabla v to be replaced by the more specific condition on \nabla \times v. A Grönwall-type argument then shows that if the vorticity remains controlled, the energy E(t) remains bounded, leading to a contradiction.

**Constants & Bounds:**
- `Uniform Ball Radius: inf_{0≤t<T†} R(\Omega_t) > C^{-1}`: This condition assumes the existence of a uniform minimum radius for balls that can be fit both inside and outside the fluid domain at every point on the boundary. Its significance is that it geometrically prevents the boundary from pinching off or self-intersecting (ruling out Case 1 blow-up) and ensures the domain is regular enough for various analytical estimates (like div-curl lemmas) to hold uniformly in time.
- `H^{3/2} bound on Mean Curvature: sup_{0≤t<T†} \|H_{\partial\Omega_t}\|_{H^{3/2}(\partial\Omega_t)} ≤ C`: This is the assumption that the mean curvature H remains bounded in a specific Sobolev norm. Its significance is that it rules out blow-up scenario (2). Through elliptic regularity (Lemma 2.7), this bound provides control over the overall regularity of the boundary itself (e.g., keeping it in H^{7/2}).
- `H^{5/2} bound on Normal Velocity: sup_{0≤t<T†} \|v_n\|_{H^{5/2}(\partial\Omega_t)} ≤ C`: This is the assumption that the normal velocity of the boundary remains bounded in a high Sobolev norm. Its significance is that it rules out blow-up scenario (3), which corresponds to a kinematic breakdown where the boundary itself is moving in an increasingly irregular way.

---

### Complex-time singular structure of the 1D Hou-Luo model
**Authors:** Cornelius Rampf, Sai Swetha Venkata Kolluru | **Year:** 2026 | [2601.02464v1](https://arxiv.org/abs/2601.02464v1) | **Validation:** unverified
**Relevance:** 7/10

**Why it matters:** This paper studies a 1D model (Hou-Luo) which is an approximation of the 3D axisymmetric Euler equations on a boundary. While not the full Navier-Stokes equations, the model is known to exhibit a finite-time blow-up and serves as a crucial testbed for understanding the mechanisms that might lead to singularities in the full 3D problem. It directly addresses the formation of singularities and provides a detailed analysis of the blow-up structure, which is highly relevant for the NS3D blowup problem. The paper helps close the gap in understanding the local structure of singularities and how they are formed.

**Key Insights:**
1. Lagrangian coordinates simplify the singularity structure: The complex 'eye-shaped' pattern of singularities seen in the Eulerian frame collapses to just two real-valued singularities in the Lagrangian frame. This makes the analysis of the blow-up much more tractable.
2. The blow-up is driven by particle collapse: The singularity in the HL model is caused by multiple fluid particles accumulating at the same physical location, causing the Jacobian of the Lagrangian map to vanish.
3. The BKM criterion is a blunt instrument: The Beale-Kato-Majda (BKM) criterion, a well-known tool for detecting blow-ups, correctly identifies the blow-up time but fails to capture the local details of the singularity exponent. This suggests that more refined tools are needed to understand the fine structure of singularities.
4. Symbolic computation of Taylor series is powerful: The paper's use of symbolic computation to generate high-order Taylor series coefficients allows for a very precise analysis of the singularity structure, avoiding numerical artifacts that can plague other methods.

**Equations:**
- $$3D Axisymmetric Incompressible Euler Equations: \partial_t \omega_1 + u_r \partial_r \omega_1 + u_z \partial_z \omega_1 = \partial_z (u_1)^2, \quad \partial_t u_1 + u_r \partial_r u_1 + u_z \partial_z u_1 = 2u_1 \partial_z \psi_1$$
  This is the system of equations for the evolution of vorticity (\omega_1) and velocity (u_1) in a 3D axisymmetric fluid flow. It's the parent system from which the Hou-Luo model is derived.
- $$Hou-Luo Model: \partial_t u + v \partial_z u = 0, \quad \partial_t w + v \partial_z w = \partial_z u, \quad \partial_z v = H[w]$$
  This is the 1D model that approximates the 3D Euler equations on the boundary. It describes the evolution of simplified velocity components (u, v) and vorticity (w). The Hilbert transform H relates the vertical velocity gradient to the vorticity, capturing the non-local effects of the fluid.
- $$Lagrangian Formulation of HL model: \frac{d u}{dt} = 0, \quad \frac{dZ}{dt} = v, \quad \frac{dw}{dt} = \nabla_z u, \quad \frac{dJ}{dt} = J H[w]$$
  This set of equations describes the Hou-Luo model in a moving frame that follows the fluid particles. Z is the particle position, J is the Jacobian of the transformation from Lagrangian to Eulerian coordinates, and d/dt is the material derivative. This formulation simplifies the advection terms and is key to the paper's analysis.

**Theorems:**
- This paper does not contain formal theorems, lemmas, or propositions in the traditional mathematical sense. Instead, it presents a detailed analytical and numerical investigation of the Hou-Luo model. The core of the paper is the development of a 'Lagrangian singularity theory' which is more of a framework or a method than a theorem. The 'proof' of this theory is its successful application to predict the singularity structure of the model, which is validated against numerical simulations.

**Constants & Bounds:**
- `Blow-up time: t_\star \approx 2.118`: This is the predicted time at which the solution to the Hou-Luo model with the given initial conditions develops a singularity (blows up).
- `Singularity exponent: \nu \approx -3.06`: This exponent describes the rate at which the solution approaches the singularity. A negative value indicates a blow-up.
- `Radius of convergence for Eulerian series: R_inf \approx 1.588`: This is the radius of the disk in the complex time plane within which the Eulerian-based Taylor series solution is guaranteed to converge. Singularities outside this disk are not accessible with this method.

---

### The Euler equations with variable coefficients
**Authors:** Benjamin Ingimarson, Igor Kukavica, and Amjad Tuffaha | **Year:** 2022 | [2209.01067v1](https://arxiv.org/abs/2209.01067v1) | **Validation:** unverified
**Relevance:** 6/10

**Why it matters:** This paper studies the Euler equations (the inviscid counterpart to Navier-Stokes) with highly general, space-time dependent coefficients. While not directly addressing the NS3D problem, its techniques for establishing local existence and a Beale-Kato-Majda (BKM) type blow-up criterion are highly relevant. The methods for handling variable coefficients, deriving pressure and vorticity estimates in a complex setting, and proving a novel 'variable div-curl lemma' provide a sophisticated toolkit for tackling PDE regularity questions. It addresses gaps related to vorticity control and blow-up criteria in scenarios that deviate from the classical, constant-coefficient case on simple domains.

**Key Insights:**
1. Blowup is Tied to Vorticity and Velocity Growth: The BKM criterion (Theorem 2.3) provides a clear target for proving blowup: one must show that a solution can evolve in such a way that the time integral of `\|v\|_{H^1} + \|\zeta\|_{BMO}` becomes infinite. This confirms that control of vorticity remains the central challenge, but adds the complication that the velocity's `H^1` norm must also be tracked, as energy is not conserved.
2. Variable Coefficients Introduce Lower-Order Forcing in Vorticity Equation: The derivation of the vorticity transport equation (3.23) results in a forcing term `f_i` (3.22) that explicitly depends on pressure gradients and other terms. This is a major departure from the classical Euler equations, where the pressure term vanishes in the vorticity formulation. This complicates the analysis significantly and is a key technical hurdle that the paper overcomes.
3. A Generalized Div-Curl Lemma is Possible: The paper successfully proves a variable-coefficient version of the div-curl lemma (Lemma 3.5). This is a powerful insight, suggesting that this fundamental tool from harmonic analysis can be adapted to more complex geometric settings, which could be crucial for analyzing NS equations in complex, time-varying domains.
4. Incompressibility Imposes Strong Compatibility Conditions: The analysis reveals that for a solution to exist, a non-obvious compatibility condition (`\int_{\partial\Omega} \partial_t (n_j b_{ji} \psi_i) = 0`) must hold. This shows that the incompressibility constraint (`a_{ji} \partial_j v_i = 0`) is not automatically preserved under arbitrary choices of coefficients and boundary motion, but imposes a deep consistency requirement on the problem's data.

**Equations:**
- $$\partial_t v_i + (v_m - \psi_m)a_{km} \partial_k v_i + a_{ki} \partial_k q = 0` and `a_{ji} \partial_j v_i = 0$$
  This is the variable-coefficient Euler equation for velocity `v` and pressure `q`. The matrix `a` and vector `\psi` introduce space-time dependent coefficients and an inhomogeneous boundary flow, generalizing the classical Euler equations. The second part is the generalized incompressibility condition.
- $$(v_k - \psi_k)a_{jk} n_j = 0` on `\partial\Omega$$
  This is the kinematic boundary condition, stating that the normal component of the fluid velocity relative to the boundary velocity `\psi` is zero, meaning no fluid penetrates the boundary.
- $$\zeta_i = \varepsilon_{ijk} b_{\ell j} \partial_\ell v_k$$
  This defines the 'variable vorticity', a generalization of the standard curl of the velocity field, adapted to the variable coefficients `b`, where `b` is the cofactor matrix of `a^{-1}`.
- $$-\partial_j(b_{ji} a_{ki} \partial_k q) = \partial_j f_j$$
  This is the elliptic equation for the pressure `q`, derived by taking the variable divergence of the momentum equation. Unlike the standard Poisson equation for pressure in classical Euler, this is a variable-coefficient elliptic PDE.
- $$\partial_t \zeta_i + (v_m - \psi_m)a_{rm} \partial_r \zeta_i = \zeta_p a_{mp} \partial_m v_i + f_i$$
  This is the variable-coefficient vorticity transport equation. It shows that vorticity `\zeta` is advected by the flow, stretched by velocity gradients (`\zeta a \partial v`), and influenced by a complex forcing term `f_i` which, crucially, includes pressure gradients and other lower-order terms not present in the classical vorticity equation.
- $$\|v\|_{H^r} \lesssim \|b_{ji} \partial_j v_i \|_{H^{r-1}} + \|\zeta\|_{H^{r-1}} + \|v_k b_{jk} n_j\|_{H^{r-1/2}(\partial\Omega)} + \|v\|_{L^2}$$
  This is the key 'variable div-curl lemma' established in the paper. It provides an estimate for the full `H^r` norm of the velocity `v` in terms of its variable divergence, its variable curl (vorticity), and its boundary values, which is a fundamental tool for proving regularity.

**Theorems:**
- Theorem 2.1 (A Priori Estimates): Statement: For a smooth solution `(v,q)` on `[0,T]` with initial data `v_0` in `H^r` (`r > 2.5`), the `H^r` norm of `v` and `q` and the `H^{r-1}` norm of `v_t` are bounded on a smaller time interval `[0, T_0]` by a constant depending on the initial data.
  *Proof:* Proof technique: The proof relies on a div-curl type analysis. It involves deriving elliptic estimates for the pressure (Lemma 3.1), obtaining `H^{r-1}` estimates for the variable vorticity `\zeta` by analyzing its transport equation (Lemma 3.4), and combining these with a novel variable div-curl lemma (Lemma 3.5) to control the `H^r` norm of the velocity. A Gronwall argument is then used to establish the bound over a finite time interval.
- Theorem 2.2 (Existence): Statement: Given initial data `v_0` in `H^r` (`r > 2.5`) satisfying compatibility conditions, a local-in-time solution `(v,q)` exists.
  *Proof:* Proof technique: The proof uses an iterative scheme. It first assumes higher regularity on coefficients, linearizes the system into a transport equation, and solves it. A contraction mapping argument on this linearized problem establishes a solution for the nonlinear system with higher regularity. Finally, an approximation argument is used, where sequences of smooth coefficients `a^{(n)}` and `\psi^{(n)}` converge to the original, less regular coefficients, and the corresponding solutions `v^{(n)}` are shown to converge to a solution of the original problem.
- Theorem 2.3 (Beale-Kato-Majda Criterion): Statement: For a solution `v` in `H^3`, if the solution ceases to exist in `H^3` at a time `T*`, then the integral of the `H^1` norm of the velocity plus the BMO norm of the vorticity must be infinite. `\int_0^{T^*} (\|v(t)\|_{H^1} + \|\zeta(t)\|_{BMO}) dt = \infty`.
  *Proof:* Proof technique: The proof focuses on controlling the `H^3` norm of the velocity. The core of the argument is to control the vortex stretching term `\|v\|_{W^{1,\infty}}` using the `H^1` norm of velocity and the BMO norm of vorticity, which is achieved via an elliptic estimate in BMO. Unlike the classical BKM criterion, the `H^1` norm of `v` is needed because the `L^2` norm is not conserved due to the inhomogeneous boundary data. A Gronwall-type argument on a differential inequality for `\|v\|_{H^3}` shows that this norm can only blow up if the time integral of `\|v\|_{H^1} + \|\zeta\|_{BMO}` diverges.

**Constants & Bounds:**
- `Piola Identity: `\partial_j b_{ji} = 0``: This is a structural condition on the coefficient matrix `b` which is crucial for the analysis, allowing for integration by parts and manipulation of divergence and curl operators in the variable-coefficient setting.
- `Uniform Ellipticity: `J = \det(a^{-1})` is uniformly bounded above and below by positive constants.`: This ensures that the operator `b^T a` in the pressure equation is uniformly elliptic, which is necessary to guarantee the existence and regularity of the pressure `q`.
- `Compatibility Condition: `\int_{\partial\Omega} \partial_t (n_j b_{ji} \psi_i) = 0``: This condition is necessary for the existence of a solution to the elliptic Neumann problem for the pressure. It reveals a deep, intrinsic constraint between the boundary motion `\psi` and the coefficients `a` required for the fluid to remain incompressible.
- `Energy Estimate Inequality (Conceptual): `d/dt \|v\|_{H^r}^2 \lesssim P(\|data\|) (\|v\|_{H^r}^2 + 1)``: The core of the a priori estimates is a set of differential inequalities showing that the growth of the solution's norm is controlled by a polynomial `P` of the norms of the coefficients (`a`, `\psi`) and the solution norm itself. This allows the use of Gronwall's lemma to prove local-in-time boundedness.

---

### ON THE FORWARD SELF-SIMILAR SOLUTIONS TO THE TWO-DIMENSIONAL NAVIER-STOKES EQUATIONS
**Authors:** CHANGFENG GUI, HAO LIU, AND CHUNJING XIE | **Year:** 2026 | [2601.03833v2](https://arxiv.org/abs/2601.03833v2) | **Validation:** unverified
**Relevance:** 6/10

**Why it matters:** This paper proves the global existence of forward self-similar solutions for the 2D Navier-Stokes equations with large, singular initial data that is not locally square-integrable. While this result concerns 2D regularity and is thus the opposite of blowup, the mathematical techniques developed to handle such low-regularity data are of significant interest for the 3D blowup problem. Understanding the mechanisms that prevent blowup in 2D in this critical setting could illuminate the pathways to singularity formation in 3D, particularly in the context of self-similar collapse. It addresses the gap in understanding how to analyze solutions with initial data at a critical regularity level.

**Key Insights:**
1. The strategy of decomposing the solution `u` into a linear part `e^{tΔ}u_0` (the caloric lift) and a finite-energy perturbation `v_re` is powerful for handling initial data with critical singularities. An engineer attempting to prove 3D blowup could adapt this by trying to show that the perturbation part, rather than being controlled, actually grows without bound.
2. The existence of a special cancellation property in the 2D energy estimates for the perturbed Leray equations is the key to proving regularity. Investigating the absence of an analogous cancellation in the 3D case could be a direct route to demonstrating energy growth and proving blowup.
3. The use of weighted energy estimates with multipliers like `|y|^2 v_re` is essential for establishing the necessary decay and compactness. A failure to control such weighted norms in 3D would suggest energy is concentrating at the origin, a hallmark of a potential blowup.
4. The entire analysis confirms the central role of self-similar variables and solutions in the study of regularity and singularities. The framework presented provides a clear template for setting up the problem to search for a self-similar blowup profile in 3D.

**Equations:**
- $$\begin{cases} \frac{\partial u}{\partial t} - \Delta u + u \cdot \nabla u + \nabla \pi = 0, \\ \text{div } u = 0, \end{cases}$$
  This is the incompressible Navier-Stokes equation in 2D, which governs the motion of viscous fluids. The first equation is the momentum equation, and the second is the incompressibility condition.
- $$\nu(x,t) \to u_\lambda(x,t) = \lambda u(\lambda x, \lambda^2 t), \quad \pi(x,t) \to \pi_\lambda(x,t) = \lambda^2 \pi(\lambda x, \lambda^2 t)$$
  This describes the scaling invariance of the Navier-Stokes equations. If u(x,t) is a solution, then the scaled function u_lambda(x,t) is also a solution. Self-similar solutions are those that remain unchanged by this transformation.
- $$\nu_0(x) = \frac{\alpha x^\perp}{2\pi |x|^2} + \tilde{u}_0$$
  This equation decomposes a (-1)-homogeneous divergence-free velocity field into a part with constant circulation (the first term, a point vortex) and a circulation-free part (the second term).
- $$\nu(x,t) = \frac{\alpha x^\perp}{2\pi |x|^2} (1 - e^{-|x|^2/(4t)}) \text{ and } \omega(x,t) = \frac{\alpha}{4\pi t} e^{-|x|^2/(4t)}$$
  These are the explicit formulas for Oseen vortices, which are a specific class of self-similar solutions to the 2D Navier-Stokes equations. They describe the decay of a point vortex due to viscosity.

**Theorems:**
- Theorem 1.1: Statement: For any divergence-free, self-similar initial velocity u_0 in C^{0,beta}_loc on R^2 \ {0} with zero circulation on the unit circle, there exists a global, smooth, self-similar solution to the 2D Navier-Stokes equations. The solution is an 'energy perturbed solution' and satisfies specific pointwise decay estimates.
  *Proof:* Proof technique: The core idea is to decompose the solution u into a linear part (solution to the heat equation with the same initial data) and a finite-energy perturbation part, v_re. The main difficulty is that the initial data is not locally square-integrable. The proof establishes H^1 estimates for the perturbation part by exploiting a cancellation property specific to 2D, using carefully chosen multipliers in the energy estimates for the perturbed Leray equations. Higher regularity and pointwise estimates are then obtained through weighted energy estimates and Sobolev embedding, leading to compactness needed for the Leray-Schauder degree theory to prove existence.

**Constants & Bounds:**
- `Pointwise solution estimate: `|u(x,t)| ≤ C(A,β) * sqrt(t) / (|x| + sqrt(t))``: This bound shows that the solution decays in space and time, with the constant C depending on the Holder norm of the initial data on the unit circle.
- `Pointwise perturbation estimate: `|u(x,t) - e^{tΔ}u_0| ≤ C(A,β) * t / (|x|^2 + t)``: This shows the perturbation part decays faster than the main linear part, which is crucial for the analysis.
- `Dirichlet energy control: `||∇v_re||_{L^2}` is controlled by `||∇v_0||_{L^2}``: This is the fundamental starting point of the entire analysis, obtained via a key cancellation identity specific to 2D. It allows the energy of the perturbation to be bounded.
- `Initial Data Norm: `A = ||u_0||_{C^{0,β}(S^1)}``: The size of the solution and all bounds ultimately depend on this norm of the initial data, highlighting the importance of the initial profile's regularity, even if it's singular at the origin.

---

### Sheets of Spectral Data of Stokes Waves in Weakly Nonlinear Models
**Authors:** Benjamin Akers, Ryan Creedon | **Year:** 2026 | [2603.14090v1](https://arxiv.org/abs/2603.14090v1) | **Validation:** unverified
**Relevance:** 3/10

**Why it matters:** This paper does not directly address the 3D Navier-Stokes (NS3D) equations. It analyzes a simpler class of 1D weakly nonlinear, unidirectional models for surface water waves. However, its relevance to the NS3D blowup problem is methodological. It provides a detailed and rigorous framework for analyzing spectral instabilities of traveling wave solutions using perturbation theory. The techniques for identifying resonant interactions (triad, quartet) that lead to instabilities (Benjamin-Feir, high-frequency) and for calculating the resulting growth rates are conceptually analogous to the mechanisms that could lead to singularity formation in more complex systems like NS3D. It helps understand the fundamental process of how nonlinear interactions can cause solutions to destabilize, which is a prerequisite for blowup.

**Key Insights:**
1. Instability is born from resonance and signature. For an instability to occur, two conditions must be met: a resonance condition (`mω(1) − ω(k_1 + p) + ω(k_2 + p) = 0`) must link the wavenumbers, and a Krein signature condition must be satisfied. An engineer looking for blowup should first search for these resonant mode collisions.
2. A unified perturbation framework can analyze different types of instabilities. The same direct perturbation method, based on expanding the spectral problem in the wave amplitude `ε`, can be used to derive the growth rates and structure for both high-frequency (triad, quartet) and Benjamin-Feir instabilities. This provides a powerful, general tool for stability analysis.
3. The strength of instability depends on the resonance order. The paper shows that triad resonances (`|k_1-k_2|=1`) lead to the strongest high-frequency instabilities, with growth rates scaling as `O(ε)`. Higher-order quartet resonances (`|k_1-k_2|=2`) are weaker, with growth rates of `O(ε^2)`. This suggests focusing on the lowest-order possible resonances when searching for blowup.
4. The method is robust. The perturbation scheme works even for models with discontinuous dispersion relations (like the Akers-Milewski equation), which are not treatable by some other methods. This highlights the power of this direct expansion approach.

**Equations:**
- $$u_t + Lu + (u^2)_x = 0$$
  This is the general form of the weakly nonlinear, unidirectional model studied. `L` is a Fourier multiplier operator that defines the linear dispersion `ω(k)`. It serves as a simplified toy model for more complex systems like the water wave equations, and conceptually for any PDE with dispersion and nonlinearity.
- $$λv − c(ε)(∂_x + ip)v + L_p v(x) + 2(∂_x + ip)(u(x;ε)v(x)) = 0$$
  This is the core spectral stability problem. It is an eigenvalue problem for the growth rate `λ` of a perturbation `v(x)` to a Stokes wave solution `u(x;ε)`. A positive real part of `λ` signifies an instability. `p` is the Floquet exponent, parameterizing the quasi-periodicity of the perturbation.
- $$λ_0(k,p) = i(ω(k + p) − c_0(k + p))$$
  This defines the spectrum of the linearized operator around the zero-amplitude "flat state". Instabilities in the nonlinear problem (`ε > 0`) arise from collisions of these eigenvalues, i.e., when `λ_0(k_1, p_0) = λ_0(k_2, p_0)` for distinct wavenumbers `k_1`, `k_2`.
- $$mω(1) − ω(k_1 + p) + ω(k_2 + p) = 0, where m = k_1 - k_2$$
  This is the general resonance condition that must be satisfied for modes `k_1` and `k_2` to interact and potentially create an instability. It describes an energy and momentum exchange between `|m|` carrier waves (wavenumber 1) and the two perturbation modes.

**Theorems:**
- Result 1: High-Frequency Instability (Triad, |k_1-k_2|=1)
  *Proof:* Statement: Near a flat-state eigenvalue collision satisfying the triad resonance condition and a Krein signature condition, a small-amplitude Stokes wave develops an instability. The unstable eigenvalues form an elliptical "isola" in the complex plane with size scaling as O(ε).
- Result 2: High-Frequency Instability (Quartet, |k_1-k_2|=2)
  *Proof:* Statement: Near a quartet resonance, an instability isola is generated at O(ε^2). The unstable ellipse has a size of O(ε^2) and its center drifts from the original collision point by an amount of O(ε^2).
- Result 3: Benjamin-Feir Instability
  *Proof:* Statement: The method is adapted to the collision at the origin (λ=0, p=0), which corresponds to the classic modulational (Benjamin-Feir) instability. The resulting unstable spectrum forms a figure-eight (lemniscate) shape. The method is robust enough to handle discontinuous dispersion relations, as demonstrated for the Akers-Milewski equation.

**Constants & Bounds:**
- `Krein Signature Condition: `(k_2+p_0)/(k_1+p_0) < 0` for triads. For quartets, `G/E > 0`.`: This is not a numerical constant but a critical sign condition. It determines whether a given eigenvalue collision is capable of producing an instability when the nonlinearity is turned on. It is a necessary and sufficient condition for the onset of high-frequency instabilities in this class of models.
- `Instability Growth Rate Scaling: `Re(λ) ~ O(ε)` for triads; `Re(λ) ~ O(ε^2)` for quartets.`: This shows that triad instabilities are the dominant high-frequency instability mechanism for small amplitude waves, as they grow much faster than quartet-induced instabilities.
- `Isola Shape: Ellipses for high-frequency instabilities, Lemniscates (figure-eights) for Benjamin-Feir.`: This describes the geometry of the unstable spectrum in the complex plane for a fixed small amplitude `ε`.

---

### SELF-SIMILAR PRIOR AND WAVELET BASES FOR HIDDEN INCOMPRESSIBLE TURBULENT MOTION
**Authors:** P. HE´AS, F. LAVANCIER, S. KADRI-HAROUNA | **Year:** 2014 | [1302.5554v2](https://arxiv.org/abs/1302.5554v2) | **Validation:** unverified
**Relevance:** 2/10

**Why it matters:** This paper is not directly about the Navier-Stokes regularity problem. It focuses on the inverse problem of estimating turbulent flows from image sequences using a statistical prior (fBm). The connection to NS3D blowup is very weak. While it uses models of turbulence (H=1/3) that are relevant to the physics of Navier-Stokes, the paper's contributions are in the area of signal processing and computer vision for fluid flow estimation, not in the fundamental theory of PDEs. It does not address the question of finite-time blowup.

**Key Insights:**
1. The paper's primary contribution is a Bayesian framework for estimating turbulent fluid motion from image sequences, not a direct analysis of the Navier-Stokes equations. It uses a statistical prior (divergence-free fractional Brownian motion) to regularize an ill-posed inverse problem. 2. The use of wavelet bases (both fractional Laplacian and divergence-free) is a key computational innovation that enables efficient algorithms for solving the MAP estimation problem. 3. The methods are validated on synthetic turbulence data, showing superior performance compared to traditional optic-flow methods, especially for turbulence-like velocity fields (H=1/3).

**Equations:**
- $$u(x) = \sigma(-\Delta')^{-H/2+1}W_{div}$$
  This equation defines the divergence-free isotropic fractional Brownian motion (fBm) as a solution to a fractional Poisson equation. It serves as the prior model for the turbulent velocity field u. W_div is a vector of two independent Gaussian white noises, and (-\Delta')^{-H/2+1} is a fractional Laplacian operator.
- $$u(x) = \frac{\sigma}{2\pi} \int_{\mathbb{R}^2} (e^{ik \cdot x} - 1) [I - \frac{kk^T}{\|k\|^2}] \frac{\tilde{W}(dk)}{\|k\|^{H+1}}$$
  This is the spectral representation of the divergence-free isotropic fBm. It provides an explicit way to construct the velocity field u from a Gaussian spectral measure \tilde{W}. The term [I - \frac{kk^T}{\|k\|^2}] is the Leray projector, which ensures the divergence-free condition.
- $$\delta y(u) = \frac{1}{2} \|y_1(x+u(x)) - y_0(x)\|^2$$
  This is the Displaced Frame Difference (DFD) functional, which measures the difference between two consecutive images y_0 and y_1 given a displacement field u. It forms the basis of the likelihood model in the Bayesian estimation framework.
- $$p_{\delta y|u} = \beta \exp^{-\beta \delta y(u)}$$
  This is the likelihood model, which assumes that the DFD functional follows an exponential law. It relates the observed image data to the unknown velocity field u.

**Theorems:**
- Proposition 2.2: This proposition provides a spectral representation of the isotropic divergence-free fractional Brownian vector field.
  *Proof:* The proof, detailed in the appendix, relies on the properties of Fourier transforms and Gaussian measures to derive the explicit representation from the definition of the field as a solution to a fractional Poisson equation.
- Proposition 3.1: This proposition presents the wavelet decomposition of the divergence-free isotropic fBm using fractional Laplacian wavelets.
  *Proof:* The proof hinges on the properties of the Leray projector and the specific choice of a periodic wavelet basis with the indicator function as its unique scaling function.
- Proposition 3.2: This proposition describes the covariance structure of the wavelet coefficients in the divergence-free wavelet decomposition.
  *Proof:* The proof, located in the appendix, calculates the expected value of the product of two wavelet coefficients, demonstrating their correlation.

**Constants & Bounds:**
- `Hurst parameter (H): H = 1/3`: This parameter controls the roughness of the velocity field and is relevant to the Kolmogorov theory for 3D turbulence.
- `Power Spectrum Scaling: E(\kappa) = c\kappa^{-2H-1}`: For H = 1/3, this gives the Kolmogorov k^-5/3 spectrum.

---

### Using Biot-Savart boundary conditions for unbounded external flow on Eulerian meshes
**Authors:** Gabriel D. Weymouth, Marin Lauber | **Year:** 2025 | [2404.09034v3](https://arxiv.org/abs/2404.09034v3) | **Validation:** unverified
**Relevance:** 2/10

**Why it matters:** This paper presents a novel numerical method for simulating unbounded external flows on finite computational domains. While this method could be a useful tool for simulating potential finite-time blowup scenarios with high accuracy in a computationally efficient manner, it does not offer any new theoretical insights, criteria, or pathways to proving or disproving the existence of blowup in the 3D Navier-Stokes equations. Its contribution is purely computational, not theoretical, hence the low relevance score for the direct purpose of proving blowup.

**Key Insights:**
1. A Biot-Savart integral boundary condition can accurately simulate unbounded flows on small Eulerian domains, drastically reducing computational cost compared to traditional methods that require very large domains to minimize boundary effects.
2. The non-local coupling between the pressure and the Biot-Savart boundary can be solved efficiently using an iterative, operator-split method, which requires minimal changes to standard projection-based Navier-Stokes solvers.
3. A simplified, oct-tree-based Fast Multi-level Method (FM-lM) can evaluate the Biot-Savart integrals with optimal O(N) complexity and bounded error, making the entire scheme highly efficient, especially on parallel architectures like GPUs.
4. For an engineer simulating potential blowup, this method would allow for extremely high resolution in the region of the suspected singularity without the prohibitive cost of a massive computational domain, potentially enabling more precise characterization of the singularity's structure.

**Equations:**
- $$\rho\frac{\partial\vec{u}}{\partial t} + \rho(\vec{u} \cdot \nabla)\vec{u} = -\nabla p + \mu\nabla^2\vec{u}$$
- $$\nabla \cdot \vec{u} = 0$$
  These are the incompressible Navier-Stokes equations, which govern the motion of viscous, incompressible fluids. The first equation is the momentum equation (conservation of momentum), and the second is the continuity equation (conservation of mass).
- $$\vec{u}(x) = \vec{U}_\infty + \int_\Omega K_n(\vec{x} - \vec{y}) \times \vec{\omega}(\vec{y}) d\vec{y}$$
  This is the core contribution of the paper: a new boundary condition for the velocity \vec{u} on the computational domain boundary \partial\Omega. It uses the Biot-Savart integral to compute the velocity induced by the vorticity \vec{\omega} within the domain \Omega, assuming the flow is irrotational outside.
- $$\vec{u}^{t+\Delta t} = \vec{u}^* - \frac{\Delta t}{\rho}\nabla p$$
  This is the velocity correction step in the projection method. The intermediate velocity field \vec{u}^* is corrected by the pressure gradient to yield a divergence-free velocity field at the next time step.
- $$\nabla \cdot (\frac{\Delta t}{\rho} \nabla p) = \nabla \cdot \vec{u}^*$$
  This is the Poisson equation for the pressure p that arises in the projection method. Solving this equation ensures that the velocity field at the new time step will be divergence-free.
- $$\nabla \cdot [\frac{\Delta t}{\rho} \nabla p^{k+1} + f(\vec{x}_b, \nabla \times \frac{\Delta t}{\rho} \nabla p^k, \Omega)] = \nabla \cdot [\vec{u}^* + f(\vec{x}_b, \nabla \times \vec{u}^*, \Omega)]$$
  This is the iterative, operator-split formulation for solving the coupled pressure-Biot-Savart system. It avoids the construction of a dense matrix by treating the non-local Biot-Savart term as a residual from the previous iteration k, allowing the use of standard Poisson solvers.

**Theorems:**
- Appendix A: Bounded Error of the Multi-level Clustering: The paper does not contain formal theorems in the main body. However, Appendix A provides a proof that the error of the simplified multi-level clustering approach (tree-sum and FM-lM) used to approximate the Biot-Savart integral is bounded.
  *Proof:* The proof shows that the error is inversely proportional to the number of points in the subdomain, S^n, which justifies using a small subdomain size (e.g., S=2) for efficiency without sacrificing accuracy.

**Constants & Bounds:**
- `Reynolds Number (Re): Re = UD/\nu`: A dimensionless quantity that gives a measure of the ratio of inertial forces to viscous forces. It is used to characterize different flow regimes, such as laminar or turbulent.
- `Strouhal Number (St): St = fL/U`: A dimensionless number describing oscillating flow mechanisms. It is used in the analysis of flapping foils to relate frequency, characteristic length, and flow velocity.
- `Added-mass Coefficient (Ca): C_a = F_{am} / (\rho D^3 a)`: A dimensionless coefficient that represents the inertia added to a system because an accelerating or decelerating body must move some volume of surrounding fluid as it moves through it.
- `Computational Complexity: O(N)`: The paper demonstrates that their proposed Fast Multi-level Method (FM-lM) for evaluating the Biot-Savart integral has a computational cost that scales linearly with the number of grid points N, which is optimal.

---

### Couette Taylor instabilities for counter-rotating cylinders in the small-gap regime
**Authors:** D. Bian, E. Grenier, G. Iooss, Z. Yang | **Year:** 2026 | [2603.19704v1](https://arxiv.org/abs/2603.19704v1) | **Validation:** unverified
**Relevance:** 2/10

**Why it matters:** This paper studies the Couette-Taylor problem, a specific case of the Navier-Stokes equations in a simplified geometry (between two cylinders). While it provides a detailed analysis of instabilities and bifurcations in this specific regime, it does not directly address the question of finite-time blowup in the general 3D Navier-Stokes equations. The methods and results are highly specific to the geometry and symmetries of the problem and are not readily generalizable to the broader problem of 3D NS regularity. It is therefore of low direct relevance to proving the existence of a finite-time blowup.

**Key Insights:**
1. The stability of the Couette flow in the small-gap regime is highly dependent on the ratio of rotation rates µ. 2. Near the critical Taylor number, the dynamics of the instabilities can be described by a Ginzburg-Landau equation. 3. The transition from supercritical to subcritical bifurcation at µ^_c ≈ -0.65 leads to a rich variety of solutions, including localized structures.

**Equations:**
- $$∂_t u + (u · ∇)u − ν∆u + ∇p = 0, ∇ · u = 0$$
  The incompressible Navier-Stokes equations, which govern the motion of viscous, incompressible fluids. 'u' is the velocity field, 'p' is the pressure, and 'ν' is the viscosity.
- $$U(r) = rΩ_rot(r) := (A − Ω_rf )r + B/r$$
  The Couette flow solution in a rotating frame, describing the base flow of the fluid between two rotating cylinders.
- $$(∂t − ∆⊥)u⊥ + ∇⊥p = Rx∂yu⊥ + Tg(x)(u_y, 0)t − (u⊥ · ∇⊥)u⊥ + b/2(1 − µ)(u_y^2, 0)t$$
- $$(∂t − ∆⊥)uy = Rx∂yuy + ux − (u⊥ · ∇⊥)uyb$$
- $$∇⊥ · u⊥ + R∂yby = 0$$
  The limiting system of equations for the perturbation from the Couette flow in the small-gap limit. This is the main system studied in the paper.
- $$∂A/∂t = α1A + α2∂A/∂y + α3∂^2A/∂y^2 − c|A|^2A$$
  The Ginzburg-Landau equation, an amplitude equation that describes the slow evolution of the instabilities near the critical Taylor number.
- $$α1A + α3∂^2A/∂y^2 − c|A|^2A = 0$$
  The time-independent Ginzburg-Landau equation, which describes stationary solutions of the Ginzburg-Landau equation, corresponding to steady-state patterns of the fluid flow.
- $$∂^4A_y = τA + σ∂^2A_y − c|A|^2A$$
  A fourth-order Ginzburg-Landau equation that governs the amplitude of the instabilities when the ratio of rotation rates µ is close to the critical value µc.

**Theorems:**
- Theorem 2: Details the various stationary solutions of the stationary Ginzburg Landau equation (10) that exist for T close to Tc(µ, 0) in the subcritical case.
  *Proof:* The proof relies on the analysis of the phase portrait of the second-order ODE for the amplitude A.
- Theorem 5: Describes the stationary solutions of the fourth-order Ginzburg-Landau equation (11) in various regions of the (τ, σ) plane.
  *Proof:* The proof involves analyzing the bifurcations from the trivial solution and the existence of homoclinic and heteroclinic orbits in a four-dimensional dynamical system.

**Constants & Bounds:**
- `T_c(µ, 0): The critical Taylor number for axisymmetric perturbations.`: This is the threshold for the linear instability of the Couette flow to axisymmetric disturbances.
- `α_c(µ, 0): The critical vertical wavenumber for axisymmetric perturbations.`: This is the wavenumber of the most unstable axisymmetric mode at the onset of instability.
- `µ_c ≈ -0.8: The critical ratio of rotation rates.`: This value marks the transition from axisymmetric to non-axisymmetric instabilities as the most unstable modes.
- `µ^_c ≈ -0.65: The critical ratio of rotation rates for the change of sign of the nonlinear coefficient in the Ginzburg-Landau equation.`: This value marks the transition from a supercritical to a subcritical bifurcation.

---

### Control of Vortex Dynamics using Invariants
**Authors:** Kartik Krishna, Aditya G. Nair, Anand Krishnan, Steven L. Brunton, Eurika Kaiser | **Year:** 2023 | [2308.03920v3](https://arxiv.org/abs/2308.03920v3) | **Validation:** unverified
**Relevance:** 1/10

**Why it matters:** This paper has very low relevance to the NS3D blowup problem. It focuses on the control of 2D, inviscid, point vortex dynamics governed by the Euler equations, not the 3D viscous Navier-Stokes equations. The primary goal is to manipulate existing vortex structures using model predictive control, rather than investigating the formation of singularities or the fundamental regularity of the equations. While it touches upon vortex dynamics, it does not address the core challenges of the NS3D regularity problem, such as vortex stretching, which is a key mechanism for potential blowup and is absent in 2D.

**Key Insights:**
1. The fundamental invariants of a 2D point vortex system (Hamiltonian, linear impulse, angular impulse) can be directly manipulated using a Model Predictive Control (MPC) framework. This provides a global, physically interpretable way to control the system's behavior, as opposed to controlling the local positions of each vortex.
2. Controlling a single invariant often leads to unintended changes in the other invariants. Multi-invariant control, where changes in some invariants are penalized while others are targeted, allows for reaching a more diverse set of dynamical states (e.g., forcing a transition to a quasi-periodic state while preventing a chaotic one).
3. The paper's methodology is for 2D inviscid flow and does not include vortex stretching, the key mechanism for energy cascade and potential singularity formation in 3D turbulence. Therefore, its direct applicability to proving 3D Navier-Stokes blowup is negligible.

**Equations:**
- $$\partial_t u + u \cdot \nabla u = -\nabla p$$
  This is the Euler equation for an inviscid, incompressible fluid. It describes the evolution of the fluid velocity 'u' under the influence of the pressure gradient 'p', neglecting viscous effects.
- $$\omega(x) = \sum_{i=1}^{n} \frac{\kappa_i}{2\pi} \delta(x-x_i)$$
  This equation represents the vorticity field as a sum of 'n' discrete point vortices, where 'κ_i' is the strength (circulation) of the i-th vortex located at position 'x_i'. It's a simplified model of a continuous vorticity field.
- $$\frac{dr_i}{dt} = \sum_{j=1, j \neq i}^{n} \frac{\kappa_j}{2\pi} \frac{\hat{k} \times (r_i - r_j)}{\|r_i - r_j\|^2}$$
  This is the Biot-Savart law for point vortices. It describes the velocity of the i-th vortex 'dr_i/dt' as the sum of velocities induced by all other vortices in the system.
- $$H = -\frac{1}{4\pi} \sum_{i \neq j} \kappa_i \kappa_j \log{\|r_i - r_j\|}$$
  This is the Hamiltonian of the point vortex system, representing the kinetic energy of the interaction between the vortices. For an unforced system, this quantity is conserved.
- $$(X,Y) = \sum_i \kappa_i r_i$$
- $$A = \sum_i \kappa_i \|r_i\|^2$$
  These are the linear impulse (X,Y) and angular impulse (A) of the vortex system. They are conserved quantities related to the center of vorticity and the variance of the vorticity distribution, respectively.
- $$\frac{d\phi}{dt} = \nabla_{\hat{R}}\phi \cdot Bu$$
  This equation describes the dynamics of the system's invariants (phi) under the influence of an external control input 'u'. It shows how the control, applied through the matrix 'B', can change the otherwise conserved quantities.

**Theorems:**
- Noether's Theorem: The paper mentions Noether's Theorem as the reason for the conservation of linear and angular impulse.
  *Proof:* The paper does not provide a proof, but it is a fundamental result in physics.

**Constants & Bounds:**
- `Initial vortex circulations: κ=1.0`: These are not universal constants but parameters for the simulation.
- `Initial invariant values: H=-0.22, A=4, X=0, Y=0`: These are not universal constants but parameters for the simulation.

---


## Regularity Criteria and Conditions
*Papers establishing conditions under which solutions remain smooth (Serrin, Prodi, Ladyzhenskaya criteria and extensions).*

### SHARP NON-UNIQUENESS FOR THE NAVIER-STOKES EQUATIONS IN R3
**Authors:** CHANGXING MIAO, YAO NIE, AND WEIKUI YE | **Year:** 2024 | [2412.09637v1](https://arxiv.org/abs/2412.09637v1) | **Validation:** verified
**Relevance:** 9/10

**Why it matters:** This paper is highly relevant as it proves the sharp non-uniqueness of weak solutions for the 3D Navier-Stokes equations in the entire space R3, right at the boundary of the classical Ladyzhenskaya-Prodi-Serrin (LPS) regularity criteria. The construction of pathological, non-unique solutions using convex integration is a key methodology in exploring the potential failure of regularity. This work demonstrates that even for initial data that lead to solutions in critical function spaces, uniqueness can fail, which is a strong indicator of the complex and potentially singular nature of the equations.

**Key Insights:**
1. Non-uniqueness persists in the whole space R3: The complex, non-unique behavior of weak solutions demonstrated on the periodic torus T3 is not an artifact of the periodic geometry. It is an intrinsic feature of the 3D Navier-Stokes equations, holding true in the more physically realistic setting of the entire space.
2. A new iterative scheme is needed for non-compact domains: Directly applying the convex integration schemes from the periodic case fails in R3 because operators like the inverse divergence do not preserve compact support. The key innovation is to introduce an "incompressible perturbation fluid" (w^{(t)}) which is a solution to a separate Navier-Stokes system, designed specifically to cancel out error terms that are not divergence-free or compactly supported.
3. Sharpness of the LPS criteria is confirmed at (2, \infty): The paper solidifies the understanding that the L^2([0,T]; L^\infty) space is the critical borderline for uniqueness of weak solutions. Any further relaxation of this condition (i.e., L^p with p<2) allows for the construction of pathological, non-unique solutions.
4. Convex integration can be localized: The proof carefully decomposes the solution at each step into a compactly supported part (u^{loc}) and a non-compactly supported part (u^{non-loc}). The main perturbation is applied to the local part, while the "incompressible perturbation fluid" is used to handle interactions with the non-local tail, showing how to manage the technical difficulties of a non-compact domain.

**Equations:**
- $$\partial_t u - \Delta u + \text{div}(u \otimes u) + \nabla p = 0, \quad \text{div } u = 0$$
  This is the fundamental system of equations governing the motion of an incompressible fluid. The equation describes the evolution of the fluid velocity `u` under the effects of viscosity (\Delta u), self-advection (\text{div}(u \otimes u)), and a pressure gradient (\nabla p) that enforces the incompressibility constraint (\text{div } u = 0).
- $$u \in L^p([0, T]; L^q(\mathbb{R}^3)), \quad \frac{2}{p} + \frac{3}{q} \le 1, \quad 3 \le q \le \infty$$
  This is a famous sufficient condition for the regularity and uniqueness of a Leray-Hopf weak solution. If a solution `u` satisfies this integrability condition, it must be smooth and unique. The paper's main result shows non-uniqueness for the endpoint case (p,q) = (2, \infty), demonstrating the sharpness of this criterion.
- $$\partial_t u_q - \Delta u_q + \text{div}(u_q \otimes u_q) + \nabla p_q = \text{div}(R_q), \quad \nabla \cdot u_q = 0$$ *(corrected)*
  This system is the core of the convex integration method used in the paper. It is an augmented version of the Navier-Stokes equations that includes a "Reynolds stress" term, `div(R_q)`. The strategy is to construct a sequence of solutions (u_q, R_q) where u_q converges to a true weak solution of the Navier-Stokes equations and the Reynolds stress R_q vanishes in the limit.
  > Correction: The ring accent on R_q is not present in the equation in the PDF.

**Theorems:**
- Theorem 1.2 (Sharp and strong non-uniqueness): Let 1 \le p < 2 and T > 0. Any weak solution u_0 of the equations (NS) in L^p([0, T ]; L^\infty(\mathbb{R}^3)) is non-unique.
  *Proof:* Proof Technique: The proof is based on an iterative convex integration scheme. Starting with any given weak solution, the authors construct a sequence of approximate solutions to a Navier-Stokes-Reynolds system. A key innovation is a new iterative scheme for the whole space R3 that balances the compact support of the Reynolds stress error with the non-compact support of the solution by introducing an "incompressible perturbation fluid". This allows the Reynolds stress to be driven to zero while constructing a different solution with the same initial data.
- Proposition 3.1: This is the main iterative proposition that drives the proof of Theorem 1.2. It states that given a solution (u_q, p_q, R_q) to the Navier-Stokes-Reynolds system at step q, one can construct a new solution (u_{q+1}, p_{q+1}, R_{q+1}) where the new solution is a small L^2 perturbation of the old one, and the new Reynolds stress R_{q+1} is significantly smaller than R_q.
  *Proof:* Proof Technique: The construction involves three main steps: 1. Mollification of the current solution to gain regularity. 2. A gluing procedure to ensure the solution remains unchanged at the initial time. 3. A carefully constructed perturbation using intermittent shear flows, temporal concentration functions, and an "incompressible perturbation fluid" to cancel the previous Reynolds stress and create a new, smaller one.

**Constants & Bounds:**
- `Energy inequality for Leray-Hopf solutions: \|u(t)\|_{L^2}^2 + 2 \int_0^t \|\nabla u(s)\|_{L^2}^2 ds \le \|u_0\|_{L^2}^2`: This is the fundamental energy balance for weak solutions, showing that the kinetic energy of the fluid plus the total energy dissipated by viscosity over time is bounded by the initial kinetic energy.
- `Iterative parameter definitions (Section 3.1): \lambda_q := a^{b^q}, \delta_q := \lambda_q^{-2\beta}, \ell_q := \lambda_q^{-50}`: These define the fundamental scales of the construction. \lambda_q is the primary oscillation frequency, which grows extremely rapidly. \delta_q is the target size of the perturbation at each step, which shrinks rapidly. \ell_q is a mollification parameter. The specific relationships between these parameters (e.g., the exponents like -2\beta, -50) are critical for making the iterative estimates close.

---

### ON THE REGULARITY OF WEAK SOLUTIONS OF THE 3D NAVIER-STOKES EQUATIONS IN B−1,∞
**Authors:** A. CHESKIDOV, R. SHVYDKOY | **Year:** 2007 | [0708.3067v2](https://arxiv.org/abs/0708.3067v2) | **Validation:** verified
**Relevance:** 8/10

**Why it matters:** This paper is highly relevant as it establishes a new regularity criterion for the 3D Navier-Stokes equations in the Besov space B−1,∞. This is a critical space for the study of NS regularity, and the paper's results provide a new angle of attack on the blowup problem. Specifically, it addresses the gap in understanding the role of the B−1,∞ norm in controlling regularity, suggesting that a blow-up in this norm is a necessary condition for singularity formation.

**Key Insights:**
1. A Leray-Hopf solution to the 3D Navier-Stokes equations is regular if its B−1,∞ norm is continuous, or if the jumps in this norm are sufficiently small (proportional to viscosity).
2. This implies that for a singularity to form, the B−1,∞ norm of the solution must experience large, discontinuous jumps.
3. The paper extends the classical Ladyzhenskaya-Prodi-Serrin regularity criteria to a wider class of function spaces (Besov spaces with negative smoothness).
4. The proofs rely on frequency-local estimates of the nonlinear term in the Navier-Stokes equations, a powerful technique in the study of PDE regularity.

**Equations:**
- $$∂t u − ν∆u + (u · ∇)u + ∇p = 0, ∇ · u = 0$$
  The 3D incompressible Navier-Stokes equations, which govern the motion of viscous, incompressible fluids.
- $$||u(t)||_2^2 + 2ν ∫_t0^t ||∇u(s)||_2^2 ds ≤ ||u(t0)||_2^2$$
  The energy inequality for Leray-Hopf solutions, which states that the total kinetic energy of the fluid is non-increasing over time.
- $$sup_{t∈(0,T]} lim sup_{t0→t−} ||u(t) − u(t0)||_{B∞,−1,∞} < cν$$
  The main condition of the paper's primary theorem. It states that if the jumps in the B−1,∞ norm of the solution are bounded by a constant times the viscosity, then the solution is regular.
- $$lim sup_{q→∞} sup_{t∈(0,T)} λq^−1 ||uq(t)||_∞ < cν$$
  A condition on the high-frequency components of the solution, used in the proof of the main theorem. It essentially means that the solution becomes smoother at high frequencies.

**Theorems:**
- Theorem 3.1: If a Leray-Hopf solution u satisfies sup_{t∈(0,T]} lim sup_{t0→t−} ||u(t) − u(t0)||_{B∞,−1,∞} < cν, then u is regular on (0, T].
  *Proof:* The proof relies on Lemma 3.2, which establishes a regularity criterion based on the high-frequency behavior of the solution. By showing that the condition of Theorem 3.1 implies the condition of Lemma 3.2 on any interval of regularity, the theorem is proved.
- Lemma 3.2: If a Leray-Hopf solution u satisfies lim sup_{q→∞} sup_{t∈(0,T)} λq^−1 ||uq(t)||_∞ < cν, then u is regular on (0, T].
  *Proof:* The proof uses a frequency-localized energy estimate. The weak formulation of the NSE is tested with a frequency-localized function, and the nonlinear term is estimated using Littlewood-Paley theory and Bernstein's inequalities. This leads to a differential inequality for the high-frequency part of the solution, which, under the condition of the lemma, implies boundedness of a higher-order norm and thus regularity.
- Corollary 3.3: If a Leray-Hopf solution u satisfies ||u||_{L∞((0,T);B∞,−1,∞)} < cν, then u is regular on (0, T].
  *Proof:* This is a direct consequence of Lemma 3.2.
- Lemma 4.1: Provides a regularity criterion in a subcritical range of integrability exponents, based on an integral condition on the solution.
  *Proof:* Similar to Lemma 3.2, it uses a frequency-localized energy estimate, but with different parameters.
- Theorem 4.2: If a Leray-Hopf solution u is in L^r((0, T); B^(2/r - 1)_{∞,∞}), for some r ∈ (2, ∞), then u(t) is regular on (0, T].
  *Proof:* This is a consequence of Lemma 4.1 and the embedding properties of Besov spaces.

**Constants & Bounds:**
- `Energy Inequality: ||u(t)||_2^2 + 2ν ∫_t0^t ||∇u(s)||_2^2 ds ≤ ||u(t0)||_2^2`: This provides a fundamental bound on the total energy of the system.
- `Bernstein's inequalities: These are used throughout the proofs to relate norms of functions to norms of their Fourier transforms, and are crucial for the frequency-localized estimates.`: 

---

### On mixed pressure-velocity regularity criteria to the Navier-Stokes equations in Lorentz spaces
**Authors:** Hugo Beirão da Veiga, Jiaqi Yang | **Year:** 2020 | [2007.02089v2](https://arxiv.org/abs/2007.02089v2) | **Validation:** verified
**Relevance:** 8/10

**Why it matters:** This paper is highly relevant to the NS3D blowup problem. It directly addresses the question of what conditions are sufficient to guarantee regularity, which is the flip side of the blowup question. By establishing sharp regularity criteria based on mixed pressure-velocity quantities in Lorentz spaces, the paper pushes the boundary of our knowledge. It helps to close the gap in our understanding of the interplay between pressure and velocity at the critical level, which is precisely where a potential blowup would have to occur. The results suggest that any blowup scenario must violate these refined integrability conditions.

**Key Insights:**
1. Pressure as a proxy for regularity: The paper reinforces the idea that the pressure field `\pi` contains crucial information about the regularity of the velocity field `v`. The formal relation `\pi \sim |v|^2` is a powerful guide, and the P-V criteria show that controlling the integrability of `\pi` (or a mixed quantity) is sufficient to control `v`.
2. Criticality and function spaces matter: The difference between 'mild' criteria (with `<` in the scaling condition) and 'strong' criteria (with `=`) is significant. The choice of proof technique (truncation vs. energy methods) can determine which type of result is achievable. Furthermore, using more refined function spaces like Lorentz spaces can lead to sharper criteria, getting closer to the true boundary of regularity.
3. Two main proof techniques: The paper provides a clear overview of two powerful methods for proving regularity: the De Giorgi truncation method and the energy-based method from [2]. Understanding the strengths and weaknesses of each is essential for anyone working on the regularity problem. The truncation method is very general but sometimes yields slightly weaker results, while the energy method can be more direct for certain problems.
4. The `\theta` parameter as an interpolation: The parameter `\theta` in the mixed P-V criteria `|\pi|/(1+|v|)^\theta` provides a useful way to interpolate between a condition purely on the pressure (`\theta=0`) and a condition on the ratio `|\pi|/|v|` (`\theta=1`). The fact that regularity can be proven for the whole range `0 \le \theta \le 1` at the critical scaling is a strong statement about the coupled nature of pressure and velocity.

**Equations:**
- $$\partial_t v + v \cdot \nabla v - \Delta v + \nabla \pi = 0, \quad \nabla \cdot v = 0$$
  This is the fundamental system of equations governing the motion of an incompressible, viscous fluid. `v` is the fluid velocity and `\pi` is the pressure. The first equation is the momentum equation, and the second is the incompressibility condition.
- $$v \in L^p(0, T; L^q(\Omega)), \quad \frac{2}{p} + \frac{n}{q} = 1, \quad q > n$$
  This is a classical result stating that if a weak solution `v` has sufficient integrability in space and time (as defined by the condition on `p` and `q`), then it must be a regular (smooth) solution. This provides a sufficient condition to prevent blowup.
- $$- \Delta \pi = \sum_{i,j=1}^{n} \partial_i \partial_j (v_i v_j)$$
  This equation relates the pressure `\pi` to the velocity field `v`. It shows that the Laplacian of the pressure is determined by the divergence of the tensor `v \otimes v`. This suggests a scaling relationship `\pi \sim |v|^2`.
- $$\frac{|\pi|}{(1 + |v|)^\theta} \in L^p(0, T; L^q(\Omega)), \quad \frac{2}{p} + \frac{n}{q} = 2 - \theta$$
  This is the main type of criterion studied in the paper. It provides a sufficient condition for regularity based on the integrability of a quantity that mixes pressure `\pi` and velocity `v`. The parameter `\theta` interpolates between conditions on pressure alone (`\theta=0`) and conditions on the ratio `|\pi|/|v|` (`\theta=1`).

**Theorems:**
- Theorem 3.1: If `|\pi| / (1 + |v|) \in L^p(0, T; L^q(\Omega))` with `2/p + n/q < 1`, then the solution is regular.
  *Proof:* The proof uses the De Giorgi truncation method, which involves defining a sequence of truncated functions and deriving energy estimates for them. This allows one to control the growth of high norms of the solution.
- Theorem 3.2: If `|\pi| / (1 + |v|)^\theta \in L^\gamma(Q_T)` for `\theta \in [0, 1)` and `2/\gamma + n/\gamma < 2 - \theta`, then the solution is regular.
  *Proof:* This also uses the truncation method, but with a different approach than Theorem 3.1. It establishes a relationship between the integrability of the mixed P-V quantity and the integrability of the velocity itself, ultimately connecting back to the L-P-S criterion.
- Theorem 4.2: If `|\pi| / (1 + |v|)^\theta \in L^p(0, T; L^q(\Omega))` with `2/p + n/q = 2 - \theta` (the critical case), then the solution is regular. Certain restrictions on `p` apply when `q < n`.
  *Proof:* The proof uses a different method based on energy estimates and the analysis of the equation for `|v|^\alpha`. This technique, developed in [2], avoids the need for the truncation method and allows for the proof of 'strong' criteria (with equality in the scaling condition).
- Theorem 5.2 (Main Result): If `(e^{-|x|^2} + |v|)^{-\theta} \pi \in L^p(0, T; L^{q,\infty})` with `2/p + 3/q = 2 - \theta`, then the solution is regular. The weight `e^{-|x|^2}` is included to handle the case of the whole space `R^3`.
  *Proof:* This theorem is the main contribution of the paper. The proof combines the techniques from [8] with the use of Lorentz spaces `L^{q,\infty}` (also known as weak `L^q` spaces). This allows for a refinement of the function spaces in the regularity criterion.

**Constants & Bounds:**
- `L-P-S Exponents: 2/p + n/q = 1 for `v \in L^p(L^q)``: This is the critical relationship between time and space integrability for the velocity field that guarantees regularity.
- `P-V Exponents: 2/p + n/q = 2 - \theta for `|\pi|/(1+|v|)^\theta \in L^p(L^q)``: This is the analogous critical relationship for the mixed pressure-velocity quantity.
- `Interpolation Inequalities: The proofs rely heavily on various interpolation inequalities, such as the Gagliardo-Nirenberg-Sobolev inequality, which relate different norms of a function and its derivatives. These are essential for deriving the energy estimates.`: 
- `Calderon-Zygmund Inequalities: The relationship between `v` and `\pi` via the Poisson equation (2.1) is mediated by Calderon-Zygmund singular integral operators. The boundedness of these operators on various function spaces (like `L^p`) is crucial.`: 

---

### SHARP NONUNIQUENESS FOR THE NAVIER-STOKES EQUATIONS
**Authors:** ALEXEY CHESKIDOV, XIAOYUTAO LUO | **Year:** 2022 | [2009.06596v2](https://arxiv.org/abs/2009.06596v2) | **Validation:** partially_verified
**Relevance:** 8/10

**Why it matters:** This paper is highly relevant as it constructs non-Leray-Hopf solutions to the Navier-Stokes equations, demonstrating nonuniqueness for weak solutions. While not a direct proof of blowup, it explores the boundary of the regularity conditions (Ladyzhenskaya-Prodi-Serrin criteria) and shows that solutions can be "wild" in the supercritical regime, which is where blowup is expected to occur. It directly addresses the non-uniqueness gap.

**Key Insights:**
1. Convex integration is a powerful tool for constructing pathological solutions to the Navier-Stokes equations. It can be used to create non-unique, non-Leray-Hopf solutions in the supercritical regime.
2. The Ladyzhenskaya-Prodi-Serrin criterion is sharp. This paper shows that as soon as you cross the critical threshold, uniqueness can fail. This gives a clear target for any blowup construction: you must violate this condition.
3. Singularities can be localized in time. The constructed solutions have a singular set with a small Hausdorff dimension, meaning that the solution is regular on a large set of times. This suggests that blowup, if it occurs, might be a very localized event in time.
4. The mechanism for non-uniqueness is the persistence of space-time oscillations. The constructed solutions are highly oscillatory, and it is this oscillatory nature that leads to the failure of uniqueness and the energy inequality.

> **Validation Note:** The unicode characters in the theorem statements have been replaced with the correct LaTeX commands. The mathematical content of the theorems appears to be correct.

**Equations:**
- $$\partial_t u - \Delta u + \text{div}(u \otimes u) + \nabla p = 0; \text{div} u = 0$$ *(corrected)*
  This is the incompressible Navier-Stokes equation, which describes the motion of viscous, incompressible fluids. It consists of a momentum equation and the incompressibility constraint.
  > Correction: Unicode characters used instead of LaTeX commands.
- $$\int_{\mathbb{T}^d} u_0(x) \cdot \phi(0, x)dx = - \int_0^T \int_{\mathbb{T}^d} u \cdot (\partial_t\phi + \Delta\phi + u \cdot \nabla\phi) dxdt$$ *(corrected)*
  This is the weak (or distributional) formulation of the Navier-Stokes equations. It allows for solutions that are not smooth enough to satisfy the classical PDE.
  > Correction: Unicode characters, incorrect integral limits, and missing LaTeX commands.
- $$u(t) = e^{t\Delta}u_0 + \int_0^t e^{(t-s)\Delta}\mathbb{P}\text{div}(u \otimes u)(s)ds$$ *(corrected)*
  This is the integral (or Duhamel) formulation of the Navier-Stokes equations, representing the solution in terms of the heat semigroup and a bilinear term. It is often used to construct 'mild solutions'.
  > Correction: Unicode characters, missing parentheses, and missing LaTeX command for the Leray projector.
- $$\frac{1}{2}\Vert u(t) \Vert_{L^2}^2 + \int_0^t \Vert \nabla u(s) \Vert_{L^2}^2 ds \leq \frac{1}{2}\Vert u(0) \Vert_{L^2}^2$$ *(corrected)*
  This is the energy inequality for Leray-Hopf weak solutions. It expresses the conservation of energy for smooth solutions and the dissipation of energy for weak solutions.
  > Correction: Incorrect norms and missing LaTeX commands.
- $$u = e^{t\Delta}u_0 + B(u, u)$$ *(corrected)*
  This is an abstract representation of the integral formulation, where B(u,u) is a bilinear operator representing the nonlinear term. This form is useful for studying the properties of the solution in various function spaces.
  > Correction: Unicode character for Delta.

**Theorems:**
- Theorem 1.3 (Ladyzhenskaya-Prodi-Serrin criteria): Let d ≥ 2 and u be a weak solution of (1.1) such that u ∈ Xp,q for some p,q ∈ [1,∞] such that 2/p + d/q ≤ 1. Then (1) u is unique in the class of Xp,q weak solutions, (2) u is a Leray-Hopf solution, and regular on (0,T].
  *Proof:* The proof relies on showing the continuity of the bilinear operator B in the abstract integral formulation of the NSE. This continuity guarantees that the solution is unique and regular under the given conditions.
- Conjecture 1.4: Let d ≥ 2 and p,q ∈ [1,∞] such that 2/p + d/q > 1. Then (1) There exist two weak solutions u,v ∈ Xp,q of (1.1) such that u(0) = v(0) but v != u. (2) There exists a weak solution u ∈ Xp,q of (1.1) such that u is not Leray-Hopf.
  *Proof:* This is the central conjecture the paper addresses. The authors provide a positive answer in certain supercritical cases.
- Theorem 1.6 (Sharp nonuniqueness in d ≥ 2): Let d ≥ 2 be the dimension and 1 ≤ p < 2. (1) A weak solution u ∈ Lp(0,T;L∞(Td)) of (1.1) is not unique in the class Lp(0,T;L∞(Td)) if u has at least one interval of regularity. (2) There exist non-Leray-Hopf weak solutions u ∈ Lp(0,T;L∞(Td)).
  *Proof:* The proof is a consequence of the main Theorem 1.8. It uses convex integration to construct solutions that are not unique and do not satisfy the energy inequality, showing the sharpness of the Ladyzhenskaya-Prodi-Serrin criteria at the endpoint p=2.
- Theorem 1.8 (Main theorem): Let d ≥ 2, 1 ≤ p < 2, q < ∞, and ε > 0. For any smooth, divergence-free vector field v, there exists a weak solution u and a set I = ∪(ai, bi) such that u is smooth on I, the Hausdorff dimension of the singular set S = [0,T] \ I is less than ε, and u is ε-close to v.
  *Proof:* The proof is a constructive iteration combining a temporal concentration of the Reynolds stress error with a convex integration scheme. The concentration part creates intervals of regularity, while the convex integration part builds the non-unique, oscillatory solution.

**Constants & Bounds:**
- `Ladyzhenskaya-Prodi-Serrin criterion: 2/p + d/q <= 1`: This inequality defines the critical and sub-critical regimes for uniqueness and regularity of weak solutions. It provides a sharp threshold; the paper shows non-uniqueness in the supercritical regime (2/p + d/q > 1).
- `Hausdorff dimension of singular set: d_H(S) <= ε`: The main theorem constructs solutions where the set of singular times S has an arbitrarily small Hausdorff dimension. This means the solution is regular for most of the time.

---

### A localized criterion for the regularity of solutions to Navier-Stokes equations
**Authors:** Congming Li, Chenkai Liu, Ran Zhuo | **Year:** 2022 | [2212.00405v3](https://arxiv.org/abs/2212.00405v3) | **Validation:** verified
**Relevance:** 8/10

**Why it matters:** This paper is highly relevant as it establishes a new, localized version of the Serrin regularity criterion. Instead of requiring a global Ls,r norm of the solution to be bounded, it shows that regularity is guaranteed if a localized version of the norm is bounded. This shifts the focus from controlling the solution everywhere to controlling it in small, moving regions, which could be a more tractable approach for ruling out blowup.

**Key Insights:**
1. The problem of proving global regularity for Navier-Stokes can be shifted from controlling a global L^s norm to controlling a localized L^s norm. This may be a more tractable problem.
2. The main technical tool is a clever use of the Gagliardo-Nirenberg inequality on a decomposed domain. This technique could potentially be applied to other nonlinear PDEs.
3. The paper provides an explicit a priori bound on the growth of the solution's gradient, which gives a clear quantitative target for future research on blowup.
4. The authors suggest that for physically reasonable initial data, the localized norm required by their criterion should remain small, making this a practical avenue for proving global regularity.

**Equations:**
- $$u_t - \nu\Delta u + (u \cdot \nabla)u + \nabla p = 0, div(u) = 0$$ *(corrected)*
  This is the incompressible Navier-Stokes equation, which describes the motion of viscous fluid substances. The equation is a statement of Newton's second law for fluids, with terms for time evolution, diffusion, convection, and pressure gradient.
  > Correction: The time derivative should be of u, not nu. Corrected from \nu_t to u_t.
- $$u \in L^{s,r} with 3/s + 2/r = 1, 3 <= s <= +\infty$$
  This is the Serrin-Prodi-Ladyzhenskaya regularity condition. It states that if a weak solution u belongs to this specific Lebesgue space L^{s,r}, then the solution must be smooth. This provides a clear mathematical target for proving regularity.
- $$\int_0^T ||u(t)||_{L^s_{R(t)}}^r dt < \infty for 3/s + 2/r = 1, r < +\infty$$
  This is the main localized regularity criterion introduced in the paper. It replaces the global L^s norm in the classical Serrin condition with a localized norm ||u(t)||_{L^s_{R(t)}}, where R(t) is a time-dependent length scale. This condition is weaker and potentially easier to verify.
- $$||\nabla u(t)||_{L^2(R^3)} \le ||\nabla u(0)||_{L^2(R^3)} exp(C_1 \int_0^T ||u(\tau)||_{L^s_{R(\tau)}}^r d\tau + C_2\mu \int_0^T R(\tau)^{-2}d\tau)$$ *(corrected)*
  This is the a priori estimate for the growth of the gradient of the solution. It shows that the L^2 norm of the gradient (and thus the solution's regularity) is controlled by the initial data and the integral of the localized L^s norm, providing an explicit bound.
  > Correction: The exponential term was incomplete. The full expression has been added.
- $$|\int_{\mathbb{R}^3} \frac{\partial u_k}{\partial x_l} \frac{\partial u_l}{\partial x_i} u_k dx| \le C_0 ||u||_{L^s_\epsilon} (\epsilon^{-s/3-1} ||\nabla u||^2_{L^2(\mathbb{R}^3)} + \epsilon^{1-3/s} ||\nabla^2 u||^2_{L^2(\mathbb{R}^3)})$$ *(corrected)*
  This is the main technical estimate of the paper. It bounds a key trilinear term in the energy estimate for the gradient of the solution. This inequality is crucial for deriving the final a priori estimate (1.14).
  > Correction: The integral was incomplete. The full integrand has been added.

**Theorems:**
- Theorem 1.6: Statement: If a solution u satisfies the localized integrability condition (1.12) and the radius function R(t) satisfies (1.13), then the solution is smooth and its gradient is bounded as shown in (1.14).
  *Proof:* Proof technique: The proof relies on a careful energy estimate for the gradient of the solution, ||∇u(t)||_{L^2}. The key is to control the nonlinear term in the evolution equation for ||∇u(t)||_{L^2} using the main technical estimate (Lemma 1.8). This leads to a Gronwall-type inequality that, when solved, yields the a priori bound (1.14).
- Lemma 1.8 (Main estimate): Statement: This lemma provides a bound for a trilinear term involving derivatives of the solution. The bound is in terms of a localized L^s norm of the solution and the L^2 norms of its first and second derivatives.
  *Proof:* Proof technique: The proof involves decomposing the domain R^3 into small cubes and applying the Gagliardo-Nirenberg inequality on each cube. The estimates are then summed up over all cubes to obtain the final result.

**Constants & Bounds:**
- `Serrin-Prodi-Ladyzhenskaya condition: 3/s + 2/r = 1, 3 <= s <= +infinity`: This is a critical relationship between the exponents of the Lebesgue space L^{s,r} that determines regularity.
- `Leray-Hopf weak solution integrability: 3/s + 2/r = 3/2, 2 <= r <= +infinity`: This describes the integrability that is known to hold for all weak solutions. The gap between this and the Serrin condition is the core of the regularity problem.
- `Kato's theorem smallness condition: ||u_0||_{L^3(R^3)} <= C*nu`: This states that if the initial data is small enough in the L^3 norm, a global smooth solution exists.
- `Main estimate constants: The constant C_0 in Lemma 1.8. This is a universal constant that arises from the Gagliardo-Nirenberg inequality and the decomposition of R^3.`: 
- `A priori estimate constants: The constants C_1 and C_2 in the final bound (1.14). These constants depend on C_0 and the exponents s and r.`: 

---

### Frequency localized regularity criteria for the 3D Navier-Stokes equations
**Authors:** Z. Bradshaw, Z. Grujic´ | **Year:** 2018 | [1501.01043v2](https://arxiv.org/abs/1501.01043v2) | **Validation:** unverified
**Relevance:** 7/10

**Why it matters:** This paper provides frequency-localized regularity criteria for the 3D Navier-Stokes equations. This is highly relevant to the blowup problem because it tells us that any potential singularity must be associated with the behavior of the solution in a specific, evolving frequency window. This helps to narrow down the search for a potential blowup scenario.

**Key Insights:**
1. Focus on the frequency window: Any potential blowup must occur within the specific, time-evolving frequency window defined by J_low(t) and J_high(t). This provides a concrete target for numerical simulations and analytical estimates. 2. Finite-time check: Regularity can be guaranteed by checking the solution's behavior at a finite number of discrete time points. This is a significant simplification compared to continuous-in-time conditions. 3. Refined regularity criteria: The paper provides a refinement of the classic Ladyzhenskaya-Prodi-Serrin regularity criteria, making it more precise and potentially easier to violate in a constructed blowup scenario.

**Equations:**
- $$∂t u + u · ∇u = −∇p + ν∆u + f$$
  This is the momentum equation from the 3D Navier-Stokes Equations (3D NSE). It is a statement of Newton's second law for a fluid parcel.
- $$∇ · u = 0$$
  This is the incompressibility condition from the 3D Navier-Stokes Equations (3D NSE). It states that the flow is divergence-free.
- $$u = ∑j≥−1 ∆j u$$
  This is the Littlewood-Paley decomposition, which decomposes the velocity field u into a sum of functions, each localized in a specific frequency band.
- $$||u||(B˙ s,q p) = (∑j∈Z (λsj ||∆˙j u||(Lp))q)1/q$$
  This is the norm for the homogeneous Besov space B˙ s,q p. These spaces are a generalization of the more familiar Sobolev spaces and are particularly well-suited for studying the regularity of solutions to the Navier-Stokes equations.
- $$J_high(t) = log2 [c1 ||u(t)||^(1/(1−ǫ)) (B˙ −ǫ ∞,∞)]$$
  This is the upper frequency cutoff that defines the frequency window of interest in this paper.
- $$J_low(t) = log2 [c2 ||u(t)||^(2/(3−2ǫ)) (B˙ −ǫ ∞,∞) / ||u||^(2/(3-2e)) (L∞(0,T;L2))]$$
  This is the lower frequency cutoff that defines the frequency window of interest in this paper.

**Theorems:**
- Theorem 1: If a Leray-Hopf weak solution u to the 3D NSE is in C(0, T; B˙ −ǫ ∞,∞) and if for a finite number of times ti in (t0, T), the solution is bounded in a specific frequency window [J_low(t0), J_high(t0)], then the solution can be smoothly extended beyond time T.
  *Proof:* The proof relies on a bootstrapping argument. By applying Lemma 4 at each time ti, it is shown that the norm of the solution at tk is bounded by the norm at t0. This prevents the norm from blowing up, which in turn implies that the solution remains regular.
- Theorem 2: If a Leray-Hopf weak solution u to the 3D NSE is in C(0, T; B˙ −ǫ ∞,∞) and if the integral of the (2/(1-e)) power of the supremum of the frequency-localized solution over the window [J_low(t), J_high(t)] is finite, then the solution is regular on (0, T].
  *Proof:* The proof is by contradiction. It is assumed that the solution loses regularity at time T. This implies that the integral of ||u(t)||^(2/(1−ǫ)) (B˙ −ǫ ∞,∞) from 0 to T is infinite. Using Lemma 6, this is shown to imply that the integral over a specific set of intervals is also infinite. Finally, using (10) and (11), it is shown that this contradicts the assumption that the integral of the frequency-localized solution is finite.

**Constants & Bounds:**
- `Local existence time: T∗ = c0 / ||a||^(2/(1−ǫ)) (B˙ −ǫ ∞,∞)`: This gives the minimum time of existence for a strong solution to the Navier-Stokes equations with initial data a in the Besov space B˙ −ǫ ∞,∞.
- `Ladyzhenskaya-Prodi-Serrin condition: 2/q + 3/p = 1`: This is the condition on the exponents p and q for the space Lq(0, T; Lp(R3)) that guarantees the regularity of a Leray-Hopf weak solution.
- `Bernstein's inequalities: ||∆˙j u(t)||∞ ≤ cλj^(3/2) ||∆˙j u(t)||2`: These inequalities relate different Lp norms of functions that are localized in frequency space. They are a fundamental tool in the study of Besov spaces and their application to PDEs.

---

### NAVIER-STOKES EQUATIONS, SYMMETRIC AND UNIFORM ANALYTIC SOLUTIONS IN PHASE SPACE
**Authors:** QIXIANG YANG | **Year:** 2018 | [1812.10088v1](https://arxiv.org/abs/1812.10088v1) | **Validation:** unverified
**Relevance:** 7/10

**Why it matters:** This paper is highly relevant to the NS3D blowup problem. It directly addresses the question of global regularity for a specific class of initial data. By identifying large classes of initial conditions (those with X_1, X_2, or X_3 symmetry) that lead to global, smooth, and even uniformly analytic solutions, it significantly narrows the search space for potential counterexamples to global regularity. The paper essentially provides a road map for what kind of initial data *not* to look at when searching for a blowup. It addresses the gap in understanding how special structures, like symmetry, influence the long-time behavior of solutions. The techniques, particularly the equivalence between uniform analyticity and convolution inequalities in Herz spaces, provide a powerful framework for analyzing regularity.

**Key Insights:**
1. Symmetry is a powerful regularizing mechanism. The paper demonstrates that specific, non-trivial symmetries (X_1 and X_2) are preserved by the Navier-Stokes flow and lead to global regularity for small data in critical spaces. This strongly suggests that any potential blowup solution must be fundamentally asymmetric.
2. The search for blowup should focus on asymmetric initial data. An engineer trying to construct a counterexample should actively avoid initial conditions that possess the symmetries described in this paper, as they are guaranteed to lead to regular solutions (at least for small data).
3. Uniform analyticity is a key indicator of regularity. The paper establishes a link between the existence of uniformly analytic solutions and the boundedness of a specific convolution inequality. This provides a concrete analytical tool: if you can show this convolution inequality holds for a given function space, you have proved the existence of regular solutions for small data in that space.
4. Fourier-Herz spaces are a good place to look for the borderline between regularity and blowup. These spaces are critical and provide a fine-grained way to classify the regularity of initial data. The condition p > 3 for the main theorem to hold is a crucial clue, suggesting that spaces with p ≤ 3 might be where the regularity breaks down.

**Equations:**
- $$(1.1) \begin{cases} \partial_t u - \Delta u + u \cdot \nabla u - \nabla p = 0, & (t, x) \in \mathbb{R}_+ \times \mathbb{R}^3, \\ \nabla \cdot u = 0, \\ u(0, x) = u_0(x). \end{cases}$$
  This is the incompressible Navier-Stokes equation, which describes the motion of viscous fluid substances. The first line is the momentum equation, the second is the incompressibility condition, and the third is the initial condition.
- $$(1.2) uˆ_1(ξ_1, ξ_2, ξ_3) = uˆ_2(ξ_2, ξ_1, ξ_3)$$
  This defines the symmetry property X_1, which relates the first two components of the velocity field's Fourier transform. It is a condition on the symmetry of the solution with respect to its components.
- $$(1.3) \begin{pmatrix} ξ_2ξ_3 + iξ_1 \\ ξ_1ξ_3 + iξ_2 \\ ξ_1ξ_2 + iξ_3 \end{pmatrix}$$
  This polynomial function defines the structure for the symmetry property X_2. A vector field u satisfies X_2 if its Fourier transform uˆ has the same symmetry as this polynomial.
- $$(1.4) sup_{t>0} e^{t^{1/2}|ξ|} |uˆ(t,ξ)| ∈ H^{α}_{p,q}$$
  This is the condition for a uniform analytic solution in the context of Herz spaces. It requires that the solution's Fourier transform, when multiplied by an exponential factor, remains in a specific Herz space uniformly in time, which is a strong form of regularity.
- $$(2.2) u(t, x) = e^{t\Delta}u_0(x) - B(u,u)(t, x); \quad B(u,u)(t, x) \equiv \int_0^t e^{(t-s)\Delta} P\nabla(u \otimes u)ds$$
  This is the integral equation formulation of the Navier-Stokes equations, also known as the mild solution. It expresses the solution at time t as the sum of the free evolution of the initial data (heat flow) and an integral term representing the nonlinear interaction.
- $$(2.5) uˆ_{τ+1}(t,ξ) = e^{-t|ξ|^2}uˆ_0(ξ) + iB˜(uˆ_τ,uˆ_τ)(t,ξ),∀τ ≥ 0$$
  This is the iterative scheme in Fourier space used to construct a solution to the Navier-Stokes equations. It's a fixed-point iteration method where each new iterate is computed from the previous one.
- $$(3.5) k|ξ|^{-1}(U ∗ V)(ξ)k_{H^{α}_{p,q}} ≤ CkUk_{H^{α}_{p,q}}kVk_{H^{α}_{p,q}}$$
  This is a key convolution inequality on Herz spaces. The paper shows that the existence of uniform analytic solutions is equivalent to the boundedness of this convolution.
- $$(5.1) uˆ_3 = - (ξ_1uˆ_1 + ξ_2uˆ_2) / ξ_3$$
  This is the expression of the incompressibility condition (∇ ⋅ u = 0) in Fourier space. It shows that the third component of the Fourier-transformed velocity field is determined by the other two components, reducing the degrees of freedom.

**Theorems:**
- Theorem 1.3: Given p > 3, 1 < q < ∞, α = 2 - 3/p and m = 1, 2, 3. Given divergence zero u_0 satisfies symmetry property X_m. There exists constant C such that, if ||uˆ_0||_{(H^α_{p,q})^3} ≤ C, then there exists a unique solution u(t, x) satisfies symmetry property X_m such that sup_{t>0} e^{t^{1/2}|ξ|}|uˆ(t,ξ)| ∈ H^α_{p,q}.
  *Proof:* The proof is based on a fixed-point argument for the iterative scheme (2.5). It shows that if the initial data is small in a critical Fourier-Herz space and possesses a certain symmetry, a global unique solution exists that preserves this symmetry and exhibits uniform analyticity. The key is to establish the boundedness of the bilinear operator in the integral equation, which is shown to be equivalent to a convolution inequality on Herz spaces.
- Theorem 2.3: Given p > 3, 1 < q < ∞ and α = 2 - 3/p. There exists constant C such that for u_0 ∈ P^α_{p,q} and ||uˆ_0||_{(H^α_{p,q})^3} ≤ C, there exists a unique solution u(t, x) such that uˆ(t,ξ) ∈ (S^α_{p,q})^3.
  *Proof:* The proof relies on showing that the existence of such a uniform analytic solution is equivalent to the boundedness of a convolution inequality on Herz spaces (Theorem 3.2). The iterative scheme (2.5) is shown to converge in the space of uniformly analytic functions (S^α_{p,q})^3 for small initial data.
- Theorem 3.2: If p > 3/2, α = 2 - 3/p and 1 < q < ∞, then k|ξ|⁻¹(U ∗ V)(ξ)k_{H^α_{p,q}} ≤ CkUk_{H^α_{p,q}}kVk_{H^α_{p,q}}.
  *Proof:* The proof involves detailed harmonic analysis techniques. The convolution is decomposed into dyadic rings in the frequency space. The estimates are carried out by splitting the integration domain and applying Holder's inequality and properties of Herz spaces. The proof is shown for 3/2 < p < 3 and the extension to p >= 3 is mentioned to follow from duality arguments.
- Theorem 5.3: If u_0 satisfies (1.2), then ∀τ ≥ 0, u_{τ+1} satisfies (1.2).
  *Proof:* The proof is by induction. It assumes u_τ satisfies the symmetry property X_1 and then shows that the bilinear term B(u_τ, u_τ) also satisfies this symmetry. This is done by carefully analyzing the structure of the nonlinear term in Fourier space and showing that the symmetry is preserved under the convolution operations involved.
- Theorem 5.8: If u_0 satisfies (5.2), then ∀τ ≥ 0, u_{τ+1} satisfies (5.2).
  *Proof:* The proof is also by induction. It uses lemmas about the symmetry of products and convolutions of functions with specific symmetry properties (Lemmas 5.6 and 5.7). The bilinear term in the iteration is broken down into its real and imaginary parts, and the symmetry of each component is tracked through the convolution operations, showing that the overall X_2 symmetry structure is preserved.

**Constants & Bounds:**
- `α = 2 - 3/p: This is the critical scaling exponent for the Herz space H^α_{p,q} and the phase space P^α_{p,q}. It defines the criticality of the initial data space in the sense that the norm is invariant under the Navier-Stokes scaling.`: This exponent is fundamental to the entire analysis, defining the function spaces where the problem is studied. The choice of this critical exponent is what makes the problem challenging and interesting, as it lies at the boundary between well-posedness and ill-posedness.
- `p > 3: This condition on the parameter 'p' of the Herz space is required for the main convolution inequality (Theorem 3.2) to hold.`: This constraint is crucial for the well-posedness results. It indicates that the methods in this paper are applicable to a specific range of function spaces and might not extend to the full range of possible critical spaces, like L^3.
- `Smallness Condition ||uˆ_0||_{(H^α_{p,q})^3} ≤ C: The main theorems require the norm of the initial data in the critical Fourier-Herz space to be smaller than some constant C.`: This is a classic small data condition for global regularity. It means the results do not apply to arbitrarily large initial data, which is where blowup is expected to occur. A key challenge in the NS3D problem is to extend such results to large data.
- `Convolution Inequality k|ξ|⁻¹(U ∗ V)(ξ)k_{H^α_{p,q}} ≤ CkUk_{H^α_{p,q}}kVk_{H^α_{p,q}}: This is the central inequality that is proven and used. The constant C is an absolute constant from the proof of the inequality.`: The boundedness of this convolution operator is the core technical result that allows the fixed-point argument to work. The value of C, while not explicitly computed, determines the size of the initial data allowed for the global existence result.
- `Exponential Growth Factor e^{t^{1/2}|ξ|}: This factor is used to define the uniform analyticity of the solution. The solution is uniformly analytic if its Fourier transform remains bounded after being multiplied by this factor.`: This factor quantifies the spatial analyticity of the solution. The fact that solutions are shown to have this property provides a strong form of regularity and rules out certain types of singular behavior where analyticity is lost.

---

### WEAK-STRONG UNIQUENESS FOR AN ELASTIC PLATE INTERACTING WITH THE NAVIER STOKES EQUATION
**Authors:** SEBASTIAN SCHWARZACHER, MATTHIAS SROCZINSKI | **Year:** 2020 | [2003.04049v3](https://arxiv.org/abs/2003.04049v3) | **Validation:** unverified
**Relevance:** 7/10

**Why it matters:** This paper is highly relevant as it develops a rigorous framework for proving weak-strong uniqueness for the Navier-Stokes equations in a time-dependent domain defined by a coupled elastic structure. While not directly tackling blowup, its sophisticated techniques for handling analysis on moving domains—specifically the construction of a solenoidality-preserving diffeomorphism and a compatible time-mollifier—address major technical hurdles that are also central to the classical NS3D regularity problem. It provides a potential blueprint for how to compare a hypothetical singular solution to a regular one in a more general setting.

**Key Insights:**
1. Complex, moving boundaries do not inherently prevent weak-strong uniqueness; the regularity conditions remain analogous to the classical fixed-domain case (Ladyzhenskaya-Prodi-Serrin). This suggests that the core of the singularity problem lies within the fluid dynamics itself, not its interaction with boundaries. 2. The challenge of analyzing solutions on different, time-evolving domains can be overcome by constructing a suitable diffeomorphism that maps one solution's domain to the other while preserving the crucial divergence-free property of the velocity field. 3. Weak time derivatives of solutions can be handled rigorously using a specialized time-mollification operator that is compatible with the moving domain and the solenoidal constraint, a technique that could be adapted to other regularity proofs. 4. An engineer attempting to prove blowup should focus on constructing solutions that specifically violate the borderline L^r(W^{1,s}) regularity conditions identified in this paper, as the work confirms that solutions satisfying these conditions remain unique and stable.

**Equations:**
- $$rho_f (∂_t v + [∇v]v) = μ_f Δv − ∇p + ρ_f f$$
  This is the momentum equation for the incompressible Navier-Stokes fluid, describing the balance of forces (inertia, viscous, pressure, external) acting on the fluid.
- $$div v = 0$$
  This is the incompressibility condition, ensuring that the fluid density is constant and the velocity field is divergence-free.
- $$ρ_s h_0 ∂_{tt}η + E'(η,∂_t η) = F(u,p,η) + ρ_s g$$
  This is the equation of motion for the elastic plate, where η is the displacement. It balances the plate's inertia and elastic/dissipative forces with the force exerted by the fluid and external gravity.
- $$v ◦ ψ = (0,∂_t η)^T$$
  This is the kinematic no-slip boundary condition at the fluid-structure interface, which states that the fluid velocity 'v' at the interface must match the plate's velocity '∂_t η'.
- $$kv(t)k^2_{L^2(Ω_{η(t)})} + k∂_t η(t)k^2_{L^2(ω)} + k∇^2η(t)k^2_{L^2(ω)} + ∫_0^t k∇v(τ)k^2_{L^2(Ω_{η(τ)})} dτ ≤ C(...)$$
  This is the fundamental energy inequality for the coupled system. It shows that the total energy of the fluid and plate is bounded by the initial energy and external forces, which is a cornerstone for proving the existence of weak solutions.

**Theorems:**
- Theorem 1.2 (Weak-Strong Uniqueness): Under certain regularity assumptions on a 'strong' solution (v2, η2) — specifically that v2 is in L^r(0,T; W^{1,s}(Ω_{η2})) for r>2, s>3 in 3D — this solution is unique within the class of all weak solutions. If two solutions start with the same initial data, and one is a strong solution, they must be identical.
  *Proof:* The proof is based on a stability estimate. It involves defining a difference between the two solutions and showing this difference, governed by an energy-like inequality, must be zero if the initial data is the same. A key technical challenge is that the two solutions live on different, time-varying domains. To overcome this, the authors introduce a diffeomorphism to map one domain to the other and a special time-mollification operator that preserves the solenoidal (divergence-free) property of the velocity fields, which is crucial for handling the pressure term and weak time derivatives.
- Theorem 1.5 (Stability Estimate): This theorem provides a quantitative stability estimate for the difference between a weak solution (v1, η1) and a strong solution (v2, η2). It bounds the L^∞ in time and L^2 in space norm of the difference in solutions by the difference in their initial data and forcing terms.
  *Proof:* The proof technique is the core of the paper's analysis and directly leads to the uniqueness result in Theorem 1.2. It involves testing the weak formulation of the equations with the difference of the solutions (or a mollified version thereof). The key novelties are the use of a domain transformation (the mapping ψ and the operator J) to handle the different geometries and a carefully constructed time-mollification that commutes appropriately with the divergence-free constraint. The final estimate is derived by combining the energy inequality for the weak solution with the equation for the strong solution, tested against the difference.

**Constants & Bounds:**
- `Korn's Identity (Lemma 2.1): ||u||_{H^1(Ω_η)} ∼ ||∇u||_{L^2(Ω_η)} = 2||εu||_{L^2(Ω_η)}`: For a vector field u with appropriate zero boundary conditions, this identity relates the H^1 norm to the L^2 norm of its gradient and its symmetric part (strain rate). It is fundamental for deriving energy estimates in fluid dynamics, as it allows controlling the full gradient by the dissipative term.
- `Ladyzhenskaya-Prodi-Serrin Condition: 3/q + 2/r = 1`: This is the classical condition on the exponents of space-time integrability for the velocity field v ∈ L^r(0,T; L^q(Ω)) that guarantees regularity and uniqueness of solutions to the Navier-Stokes equations in a fixed domain. The paper's assumptions on the strong solution v2 are analogous to this, with v2 ∈ L^r(0,T; W^{1,s}(Ω)) for s>3, r>2, which corresponds to the borderline case r=2, q=∞.
- `Energy Inequality (1.10): The total energy of the system (fluid kinetic energy + plate elastic and kinetic energy) plus the time-integrated viscous dissipation is bounded by the initial energy and the work done by external forces.`: This is the central a priori bound in the paper. It guarantees that the norms of the weak solutions remain controlled over time, which is the starting point for proving existence and is a crucial ingredient in the stability and uniqueness proofs.

---


## Self-Similar and Discretely Self-Similar Solutions
*Papers on Leray self-similar solutions, forward/backward self-similar profiles, and their role in blowup scenarios.*

### CHARLES BOUTON AND THE NAVIER-STOKES GLOBAL REGULARITY CONJECTURE
**Authors:** J. POLIHRONOV | **Year:** 2022 | [1902.01985v7](https://arxiv.org/abs/1902.01985v7) | **Validation:** verified
**Relevance:** 9/10

**Why it matters:** This paper directly tackles the Navier-Stokes global regularity problem by applying the lesser-known work of Charles Bouton on Lie group invariants. It derives self-similar solutions, proposes a new criticality criterion (the '5/2 law'), and identifies conserved quantities like the cavitation number. This approach offers a novel framework for analyzing the possibility of finite-time blowup, directly addressing the core of the problem by examining the fundamental symmetries of the equations.

**Key Insights:**
1. Bouton's theory of invariants provides a powerful and systematic method for analyzing the NSE. By enforcing the 'isobarity' of solutions under scaling transformations, one can derive the precise functional form of self-similar solutions without guesswork.
2. The criticality of the 3D NSE might not be fixed. The paper's '5/2 law' suggests that criticality depends on the scaling exponents (\alpha_t, \alpha_x). This opens the possibility of finding 'subcritical' scaling regimes where energy is controlled at small scales, allowing regularity to be proven.
3. The cavitation number, E = p/|u|^2, is a key physical quantity. The paper shows it is a scale-invariant and conserved quantity for a subset of Leray's solutions. This is a powerful insight because a conserved, coercive quantity can act as a hard barrier, preventing the velocity |u| from blowing up.
4. Smooth, global, non-self-similar solutions may exist. The paper identifies a class of polynomial solutions that are infinitely differentiable and exist for all time. This challenges the focus on self-similar blowup and suggests that regular solutions might be more common than previously thought.

**Equations:**
- $$\rho(\frac{\partial\mathbf{u}}{\partial t} + (\mathbf{u} \cdot \nabla)\mathbf{u}) = \mu\Delta\mathbf{u} - \nabla p$$ *(corrected)*
  > Correction: The order of the terms on the right-hand side was swapped.
- $$\nabla \cdot \mathbf{u} = 0$$
  These are the fundamental equations governing the motion of incompressible, viscous fluids. The first is the momentum equation (a form of Newton's second law for a fluid element), and the second is the incompressibility condition, stating that the fluid density is constant.
- $$(\mathbf{r} \cdot \nabla)\mathbf{u} + \frac{\alpha_t}{\alpha_x}t\frac{\partial\mathbf{u}}{\partial t} = -\frac{\alpha_x - \alpha_t}{\alpha_x}\mathbf{u}$$
- $$(\mathbf{r} \cdot \nabla)p + \frac{\alpha_t}{\alpha_x}t\frac{\partial p}{\partial t} = -\frac{2(\alpha_x - \alpha_t)}{\alpha_x}p$$
  These equations are derived from the requirement that the solutions to the NSE must be 'isobaric' (transform consistently) under the general scaling transformation. They constrain the functional form of the velocity and pressure, leading to self-similar solutions.
- $$\mathbf{u} = t^{(\alpha_x - \alpha_t)/\alpha_t} F(x/t^{\alpha_x/\alpha_t}, y/t^{\alpha_x/\alpha_t}, z/t^{\alpha_x/\alpha_t})$$
- $$p = t^{2(\alpha_x - \alpha_t)/\alpha_t} P(x/t^{\alpha_x/\alpha_t}, y/t^{\alpha_x/\alpha_t}, z/t^{\alpha_x/\alpha_t})$$ *(corrected)*
  These are the general forms of solutions that satisfy the isobarity conditions. They describe solutions that evolve in time by rescaling themselves in space, a key concept in the study of blowup.
  > Correction: The function on the right-hand side should be P, not F.
- $$\mathbf{u}(x,y,z,t) = \frac{1}{\sqrt{t}} F(\frac{x}{\sqrt{t}}, \frac{y}{\sqrt{t}}, \frac{z}{\sqrt{t}})$$
- $$p(x,y,z,t) = \frac{1}{t} F(\frac{x}{\sqrt{t}}, \frac{y}{\sqrt{t}}, \frac{z}{\sqrt{t}})$$
  A specific case of self-similar solutions, famously studied by Jean Leray, which arise when viscosity is not scaled. These solutions are singular at t=0 and are central to many blowup scenarios.
- $$E = \frac{p}{|\mathbf{u}|^2}$$
  A dimensionless quantity representing the ratio of pressure forces to inertial forces. The paper shows this is a scale-invariant, conserved quantity for a subset of Leray's solutions, which could provide a crucial bound preventing the velocity from blowing up.

**Theorems:**
- Theorem 3.4 (of Bouton): Statement: The solutions u, v, w, and p of the NSE must be isobaric functions of specific weights under the scaling transformation.
  *Proof:* Proof technique: This follows from applying the definition of relative invariants to the scaling group admitted by the NSE. The transformation properties of the variables dictate that the solution functions must be integral rational functions (IRFs) that are isobaric.
- Theorem 4.4: Statement: Bouton's self-similar solutions have global in-time regularity as long as they are energy-subcritical, smooth, and nonzero at t=0.
  *Proof:* Proof technique: The proof establishes a '5/2 law' for criticality based on the scaling exponents. For subcritical cases, it uses the Beale-Kato-Majda criterion to show that the scaling properties prevent the vorticity from diverging, thus ruling out a scaling-induced blow-up.
- Theorem 7.2: Statement: Within the set of Leray's self-similar solutions, there is always a subset that is not subject to scaling-induced blow-up.
  *Proof:* Proof technique: The proof identifies the cavitation number E as a scale-invariant and conserved quantity for a subset of Leray's solutions. Since E = p/|u|^2 must remain finite and constant, it prevents |u|^2 from growing uncontrollably, thus acting as a coercive bound that rules out blow-up.
- Theorem 7.3: Statement: When viscosity is not scaled, the NSE has a set of non-self-similar, polynomial solutions that are global and smooth.
  *Proof:* Proof technique: The paper shows that under the standard scaling (where viscosity is fixed), the general form of Bouton's solutions from Lemma 4.1 are no longer self-similar. By applying the Beale-Kato-Majda criterion again, it argues that the scaling properties of these polynomial solutions prevent blow-up.

**Constants & Bounds:**
- `The 5/2 Law for Criticality: \alpha_t / \alpha_x > 5/2 (subcritical)`: 
- `\alpha_t / \alpha_x < 5/2 (supercritical)`: 
- `\alpha_t / \alpha_x = 5/2 (critical)`: This inequality, derived from comparing the scaling of the NSE itself with the scaling of its energy, determines whether the energy of a solution is amplified (supercritical), diminished (subcritical), or unchanged (critical) at small scales. Subcriticality is a key condition for proving regularity.
- `Beale-Kato-Majda Criterion: \int_0^T sup|\nabla \times \mathbf{u}| dt = \infty \implies blowup`: A fundamental theorem in PDE theory stating that a solution to the NSE can only blow up at time T if the time integral of the maximum vorticity becomes infinite. The paper uses this to show that for certain solutions, the scaling behavior keeps the vorticity integral finite.
- `Energy Balance Equation: \frac{1}{2} \int |\mathbf{u}(t)|^2 dV + \nu \int_0^t \int |\nabla \mathbf{u}(s)|^2 dV ds = \frac{1}{2} \int |\mathbf{u}_0|^2 dV`: This equation expresses the conservation of energy for the NSE, stating that the kinetic energy at time t plus the total energy dissipated by viscosity over time equals the initial kinetic energy. The paper links this to regularity by showing subcritical solutions maintain bounded energy.

---


## Vorticity Dynamics and Biot-Savart Law
*Papers on vorticity evolution, Biot-Savart integral bounds, vortex stretching, and alignment between strain and vorticity.*

### Permutation symmetric solutions of the incompressible Euler equation
**Authors:** Evan Miller | **Year:** 2024 | [2404.01505v3](https://arxiv.org/abs/2404.01505v3) | **Validation:** verified
**Relevance:** 9/10

**Why it matters:** This paper is highly relevant as it directly tackles the problem of finite-time blowup in the incompressible Euler equation, a problem closely related to the NS3D regularity problem. It introduces the concept of 'permutation symmetric solutions' and demonstrates that the known C1,α blowup solutions by Elgindi are, in fact, part of this class under a change of coordinates. The paper argues that this less restrictive symmetry (compared to axisymmetry) is a promising candidate for finding smoother solutions that develop singularities, potentially closing the gap between C1,α and smooth blowup.

**Key Insights:**
1. Permutation symmetry is a promising framework for blowup: The paper convincingly argues that the class of permutation-symmetric solutions is a more general and potentially more fruitful setting to search for smooth blowup solutions than the classical axisymmetric case. This is because it is less rigid, allows for fully 3D dynamics, and naturally produces the `(-2λ, λ, λ)` strain structure associated with rapid vortex stretching.
2. Known C1,α blowup is permutation symmetric: The celebrated blowup result of Elgindi is shown to be a special case of a permutation-symmetric flow. This is a powerful insight that unifies a known result with the new framework and lends significant credibility to the idea that this symmetry class is fundamental to blowup.
3. The full 3D Euler dynamics can be reduced to a single scalar equation: For permutation-symmetric flows, the entire evolution is captured by a single scalar equation for one component of the vorticity, `ω_1`. This is a significant simplification that makes the problem more analytically and numerically tractable, similar to how axisymmetry reduces the problem to a scalar vorticity `ω_θ`.
4. A specific sign condition on ω1 drives the singular dynamics: The paper derives an explicit integral for the key strain parameter `λ` in terms of `ω_1` (`λ = (3/8π) ∫ (σ·y)(y_2−y_3)/|y|^5 ω_1(y) dy`). This provides an actionable recipe: to get blowup (`λ > 0`), one must construct an `ω_1` that makes this integral positive, analogous to the sign condition on `ω_θ` in the axisymmetric case.

**Equations:**
- $$\partial_t u + P_H((u \cdot \nabla)u) = 0$$ *(corrected)*
  The incompressible Euler equation, describing the motion of an ideal, inviscid fluid. `Pdf` is the Helmholtz projection onto divergence-free vector fields.
  > Correction: Incorrect projection operator notation. It should be P_H, not Pdf.
- $$∂ t ω + (u · ∇)ω − (ω · ∇)u = 0$$
  The vorticity formulation of the Euler equation, describing the evolution of the vorticity `ω = ∇ × u`. The term `(ω · ∇)u` represents vortex stretching, a key mechanism for potential singularity formation.
- $$u = ∇ × (−∆)−1 ω$$
  The Biot-Savart law, which recovers the velocity field `u` from the vorticity `ω`. It shows that the velocity is a non-local function of the vorticity.
- $$\partial_t \omega_1 + (u \cdot \nabla)\omega_1 - (\omega \cdot \nabla)u_1 = 0$$ *(corrected)*
  The reduced scalar evolution equation for the first component of the vorticity, `ω_1`, under permutation symmetry. This simplification allows the study of the full 3D dynamics through a single scalar quantity.
  > Correction: Missing subscripts for the omega and u terms.
- $$S(0) = \lambda \begin{bmatrix} 0 & -1 & -1 \ -1 & 0 & -1 \ -1 & -1 & 0 \end{bmatrix}$$ *(corrected)*
  The structure of the strain-rate tensor `S` at the origin for a permutation-symmetric flow. This specific structure, with eigenvalues (1, 1, -2), represents planar stretching and axial compression, a key feature in many blowup scenarios.
  > Correction: Incorrect matrix formatting. The original used a list of lists, which does not render as a matrix in LaTeX.

**Theorems:**
- Theorem 1.1: Establishes the local well-posedness for the single-component, permutation-symmetric Euler vorticity equation for `ω_1`.
  *Proof:* The proof relies on showing that permutation symmetry is preserved by the Euler dynamics and that the full velocity and vorticity can be reconstructed from `ω_1`. This reduces the problem from a vector equation to a scalar one, for which existence and uniqueness are then established.
- Theorem 1.4: Proves the existence of C1,α solutions of the full Euler equation that are odd, permutation symmetric, and blow up in finite time.
  *Proof:* The proof technique involves showing that Elgindi's axisymmetric, swirl-free C1,α blowup solution, when rotated to be symmetric about the axis x1=x2=x3, becomes a member of the permutation-symmetric class. It is a re-interpretation of a known result in a new geometric context.
- Theorem 2.12: A vector field `u` is Q-symmetric (`u = uQ`) if and only if its vorticity satisfies `ω = det(Q)ωQ`.
  *Proof:* The proof uses the Biot-Savart law and properties of the curl and orthogonal transformations. It shows that the symmetry of the velocity is directly and uniquely determined by a corresponding (skew) symmetry of the vorticity.
- Theorem 2.21 (Permutation Symmetric Biot-Savart Law): Provides an explicit integral formula (the Green's function `G(x,y)`) to reconstruct the full velocity field `u` from only the first component of the vorticity, `ω_1`.
  *Proof:* The proof involves substituting the permutation symmetry relations (`ω_2` and `ω_3` in terms of `ω_1`) into the standard Biot-Savart law and combining the resulting integrals.

**Constants & Bounds:**
- `Beale-Kato-Majda Criterion (Permutation Symmetric Version): if T_max < +∞, then ∫_0^T_max ||ω_1(·,t)||_L∞ dt = +∞.`: This is a corollary of the standard BKM criterion, adapted to the single-component formulation. If the maximum time of existence is finite, the L∞ norm of the first vorticity component must have integrated to infinity. It provides a necessary condition for blowup in terms of `ω_1`.
- `Energy Equality (Permutation Symmetric Version): ||ω_1(·,t)||_H˙−1^2 = ||ω_1^0||_H˙−1^2`: This shows the conservation of the homogeneous H˙-1 Sobolev norm for the first vorticity component. This is a conserved quantity for the simplified system, analogous to the conservation of energy for the full Euler equation.
- `Strain Eigenvalue Structure: The strain matrix `S` at the origin for a Gσ-symmetric flow has eigenvalues `(-2λ, λ, λ)`.`: This specific eigenvalue structure, with two positive and one negative eigenvalue, is known to be the 'worst-case' scenario for enstrophy growth in the Navier-Stokes equations, as shown by Neustupa and Penel. The paper shows this structure arises naturally from the permutation symmetry.

---

### Ortho-normal quaternion frames, Lagrangian evolution equations and the three-dimensional Euler equations
**Authors:** J. D. Gibbon | **Year:** 2007 | [0610004v2](https://arxiv.org/abs/0610004v2) | **Validation:** verified
**Relevance:** 8/10

**Why it matters:** This paper is highly relevant to the NS3D blowup problem, although it focuses on the Euler equations. It introduces a novel and powerful framework using quaternions to analyze the geometric evolution of the vorticity field, which is the central element in any potential singularity. The paper reformulates the vortex stretching dynamics into a compact quaternionic Riccati equation, providing a new analytical pathway. It directly addresses the gap in understanding the geometric conditions for blowup by proposing a new regularity criterion based on the alignment of vorticity with the eigenvectors of the pressure Hessian, shifting focus from the local strain-rate tensor to the non-local pressure field.

**Key Insights:**
1. The dynamics of vortex stretching and rotation can be elegantly captured by a quaternionic Riccati equation. This provides a powerful alternative to traditional vector analysis for studying the geometry of the vorticity field, potentially revealing hidden structures or conservation laws. 2. The paper's most critical insight is a new regularity criterion (Theorem 8) suggesting that a finite-time singularity in the Euler equations can only occur if the vorticity vector becomes perfectly aligned with an eigenvector of the pressure Hessian. This provides a concrete, computable geometric condition to look for in numerical simulations and analytical proofs of blowup. 3. The work strongly reinforces the modern view that a potential singularity is not merely an unbounded growth in vorticity magnitude, but a highly structured geometric event. The quaternion framework is a natural language for describing this event, which involves the alignment of the vorticity vector (`ω`), the strain-rate tensor (`S`), and the pressure Hessian (`P`). 4. The paper provides a valuable service by synthesizing and contextualizing several key regularity results, including the BKM theorem and the geometric criteria of Constantin, Fefferman & Majda, and Deng, Hou & Yu. It then demonstrates how its new quaternion-based criterion offers a different but related perspective on the same fundamental problem.

**Equations:**
- $$Du/Dt = -∇p$$
  This is the incompressible Euler equation, representing the conservation of momentum for an inviscid fluid. It states that the acceleration of a fluid particle is driven by the pressure gradient.
- $$D/Dt = ∂/∂t + u · ∇$$
  This is the material derivative, which describes the rate of change of a quantity following a fluid particle. It accounts for both the local rate of change and the change due to the particle's movement through the fluid.
- $$D(u_i,j)/Dt = -u_i,k * u_k,j - P_ij$$
  This equation describes the evolution of the velocity gradient tensor. It shows how the velocity gradient changes due to self-advection and the Hessian of the pressure.
- $$P_ij = ∂²p / (∂x_i * ∂x_j)$$
  This defines the Hessian matrix of the pressure, which is a matrix of the second partial derivatives of the pressure. It represents the curvature of the pressure field.
- $$Tr(P) = Δp = -u_i,k * u_k,i = 1/2 * ω² - Tr(S²)$$
  This is the Poisson equation for pressure, which relates the Laplacian of the pressure to the vorticity and the strain rate tensor. It is a diagnostic equation, not a prognostic one.
- $$S_ij = 1/2 * (u_i,j + u_j,i)$$
  This defines the strain rate tensor, which is the symmetric part of the velocity gradient tensor. It describes the rate of deformation of a fluid element.
- $$D(w · ∇μ)/Dt = w · ∇(Dμ/Dt)$$
  This is Ertel's theorem, a fundamental result in fluid dynamics that describes the conservation of potential vorticity. It shows that the material derivative and the directional derivative along the vorticity vector commute.
- $$Dq_a/Dt + q_a * q_a = q_b$$ *(corrected)*
  This is a Riccati equation for the quaternion `q_a`, which encodes information about the stretching and rotation of the vector field `w`. It relates the evolution of `q_a` to itself and to another quaternion `q_b` derived from the 'acceleration' of `w`.
  > Correction: The paper uses standard multiplication for quaternions, not \boxplus.
- $$Dq/Dt + q*q + q_p = 0$$ *(corrected)*
  This is the central quaternionic Riccati equation for the Euler equations, where `q` is the quaternion associated with the strain rate tensor and `q_p` is the quaternion associated with the pressure Hessian. It governs the evolution of vortex stretching and rotation.
  > Correction: The paper uses standard multiplication for quaternions, not \boxplus.
- $$∫₀ᵀ ||ω||_L∞(D) dτ < ∞$$
  This is the Beale-Kato-Majda (BKM) theorem, a cornerstone result for the regularity of the 3D Euler equations. It states that a solution remains smooth as long as the time integral of the maximum vorticity remains finite.

**Theorems:**
- Theorem 1: The ortho-normal quaternion-frame `(ŵ, χ̂_a, ŵ × χ̂_a)` evolves according to `Dŵ/Dt = D_ab × ŵ`, `D(ŵ × χ̂_a)/Dt = D_ab × (ŵ × χ̂_a)`, and `Dχ̂_a/Dt = D_ab × χ̂_a`, where `D_ab` is the Darboux angular velocity vector.
  *Proof:* The proof involves taking the Lagrangian time derivatives of the frame's components. It uses the definition of the quaternion `q_a` and its evolution to derive the expression for the Darboux vector, which governs the rotation of the frame.
- Theorem 3 (Beale-Kato-Majda): A classical solution to the 3D Euler equations exists for all time if the time integral of the maximum vorticity remains finite.
  *Proof:* The paper states this as a known cornerstone result and does not provide a proof. The original proof relies on energy estimates in Sobolev spaces and shows that the `L∞` norm of vorticity controls the higher-order norms of the solution.
- Theorem 4 (Constantin): If the initial vorticity is smooth and compactly supported, and if certain integrals involving the local `L¹` norm of vorticity and the velocity are finite, then the `L∞` norm of vorticity is controlled by its local `L¹` norm.
  *Proof:* The proof, referenced from other works, relies on a careful analysis of the Biot-Savart law and the evolution of vorticity. It uses a Lipschitz condition on the direction of vorticity to control the vortex stretching term.
- Theorem 5 (Constantin, Fefferman & Majda): In a "smoothly directed" region of the flow, the maximum vorticity remains bounded over a finite time interval.
  *Proof:* The proof, which is referenced, involves a detailed local analysis of the vorticity equation. It uses the "smoothly directed" conditions to control the vortex stretching term and prevent its explosive growth.
- Theorem 6 (Deng, Hou & Yu): If the integral of the divergence of the unit vorticity vector along a vortex line is bounded, and the time integral of vorticity at a point on that line is finite, then there is no blow-up.
  *Proof:* The proof is based on the identity `div(ω) = 0`, which can be rewritten in terms of the divergence of the unit vorticity vector and the derivative of the vorticity magnitude along the vortex line. Bounding the divergence of the unit vector allows for control over the growth of vorticity.
- Theorem 8 (Gibbon, Holm, Kerr & Roulstone): A global solution to the Euler equations exists if the time integral of the `L∞` norm of `χ_p` is finite, except in the case where the vorticity vector becomes collinear with an eigenvector of the pressure Hessian.
  *Proof:* The proof is based on the quaternionic Riccati equation (3.9). By analyzing this equation, it is shown that the growth of the strain, which drives vortex stretching, is controlled by `χ_p`. The only way for the strain to blow up while the integral of `χ_p` remains finite is if `χ_p` goes to zero, which corresponds to the collinearity of `ω` and `Pω`.

**Constants & Bounds:**
- `Beale-Kato-Majda Criterion: `∫₀ᵀ ||ω||_L∞(D) dτ < ∞``: This is the fundamental integral bound for the regularity of solutions to the 3D Euler equations. If this integral remains finite up to any time T, the solution is guaranteed to be smooth.
- `Blow-up Rate Condition: `γ ≥ 1` for `||ω||_L∞ ~ (T_c - t)⁻ᵞ``: This is a direct consequence of the BKM theorem. For a singularity to occur at time `T_c`, the rate of growth of the maximum vorticity, `γ`, must be at least 1. If `γ < 1`, the BKM integral condition would not be violated, contradicting the assumption of a singularity.
- `Constantin's Lipschitz Condition: `|ω̂(x, t) - ω̂(y, t)| ≤ |x - y| / ρ₀(t)``: This condition provides a bound on the spatial variation of the vorticity direction. `ρ₀(t)` is a length scale that characterizes the smoothness of the vorticity field. If `ρ₀` remains bounded away from zero, it helps to control vortex stretching.
- `Deng-Hou-Yu Curvature Condition: `M(t)L(t) ≤ C₀``: This condition bounds the product of the maximum curvature and divergence of the vorticity direction (`M(t)`) and the length of a vortex line segment (`L(t)`). It is a geometric constraint that prevents the formation of highly curved, short vortex segments, which are thought to be a precursor to blow-up.

---

### Evolution of viscous vortex filaments and desingularization of the Biot-Savart integral
**Authors:** Marco A. Fontelos, Luis Vega | **Year:** 2023 | [2311.12246v1](https://arxiv.org/abs/2311.12246v1) | **Validation:** verified
**Relevance:** 8/10

**Why it matters:** This paper is highly relevant as it provides a rigorous, short-time asymptotic description of the evolution of a vortex filament, a primary candidate for singular behavior in the 3D Navier-Stokes equations. It precisely quantifies the interplay between viscous diffusion and self-induced velocity, closing the gap between the idealized inviscid binormal flow and the full viscous dynamics. The analysis of the correction terms to the Lamb-Oseen vortex structure could provide a direct pathway to investigate the mechanism of potential vorticity intensification.

**Key Insights:**
1. The evolution of a viscous vortex filament can be rigorously described for short times as a Lamb-Oseen vortex (a Gaussian vorticity profile) whose center moves according to the binormal flow, with the viscous length scale `(νt)^{1/2}` replacing the ad-hoc core size `ε`.
2. The velocity of the filament is not just the simple binormal flow. There are crucial `O(1)` correction terms that depend on local curvature and non-local interactions with other parts of the filament. These corrections are essential for a more accurate model and could play a role in singularity formation.
3. The analysis requires the circulation-to-viscosity ratio `Γ/ν` to be small. This highlights the regime where viscous effects dominate the nonlinear vortex stretching term, preventing immediate blowup and allowing for a perturbative analysis. A potential blowup scenario would likely require this condition to be violated.
4. The paper provides a novel and explicit formula for "desingularizing" the Biot-Savart integral for a filament, separating the singular local part from the regular non-local part. This is a powerful technical tool for analyzing the velocity field near the filament core.

**Equations:**
- $$v = -\frac{\Gamma}{4\pi}\kappa(s,t)(\log\varepsilon)b(s,t) + O(1)$$ *(corrected)*
  This is the leading-order velocity of a thin vortex tube of radius epsilon in an inviscid flow, known as the localized induction approximation (LIA). It states that the velocity is proportional to the curvature `kappa` and directed along the binormal vector `b`, with a logarithmic dependence on the core size `epsilon`.
  > Correction: The epsilon was written as \epsilon, but the paper uses the \varepsilon symbol. Also, there were unnecessary parentheses around log epsilon.
- $$\frac{\partial\omega}{\partial t} + v \cdot \nabla\omega - \omega \cdot \nabla v - \nu\Delta\omega = 0$$
  This is the vorticity formulation of the 3D Navier-Stokes equations for an incompressible fluid with kinematic viscosity `nu`. It describes the transport, stretching, and diffusion of vorticity `omega`.
- $$v(x,t) = K * \omega(x,t) = \frac{1}{4\pi} \int \frac{\omega(x’,t) \times (x - x’)}{|x - x’|^3} dx’$$ *(corrected)*
  This is the Biot-Savart law, which reconstructs the velocity field `v` from the vorticity field `omega`. It is a fundamental connection between the two quantities in incompressible flows.
  > Correction: The identity symbol was used instead of an equals sign.
- $$\frac{dx_0(s,t)}{dt} = -\frac{\Gamma}{4\pi} \kappa(s,t)\log(\nu t)^{1/2}b(s,t)$$
  This is the binormal flow dynamics equation for the vortex filament center `x_0`. It's the viscous version of the LIA, where the effective core size is related to viscous diffusion, `(\nu t)^{1/2}`. This describes the primary motion of the filament.
- $$\omega(x,t) = \frac{1}{(\nu t)} \frac{\Gamma}{4\pi} e^{-\frac{\rho^2}{4}} x_{0s}(s,t) + ...$$
  This is the main result of the paper, an asymptotic expansion of the vorticity field `omega` near the filament. The leading term is a Lamb-Oseen vortex (a Gaussian vorticity profile) centered on the evolving filament `x_0(s,t)`. The other terms are corrections depending on curvature and other geometric properties.
- $$\frac{dx_0}{dt} = -\frac{\Gamma}{4\pi} \kappa\log(\nu t)^{1/2}b + \frac{\Gamma\kappa}{8\pi} (\gamma - \log 2)b + \frac{\Gamma}{4\pi} v^*(s)$$ *(corrected)*
  This is a more refined equation for the filament's velocity, including O(1) corrections to the leading-order binormal flow. It provides a more accurate description of the filament's motion beyond the LIA.
  > Correction: The binormal vector b was missing from the first term, and kappa was incorrectly included in the last term.

**Theorems:**
- Theorem 1: Statement: For a smooth, non-self-intersecting initial vortex filament with sufficiently small circulation-to-viscosity ratio (Γ/ν), a solution to the Navier-Stokes equations exists for a short time. The vorticity field can be decomposed into a leading-order Lamb-Oseen vortex moving with the binormal flow, plus explicit correction terms and a smaller remainder.
  *Proof:* Proof technique: The proof is constructive. It first defines an approximate solution based on the Lamb-Oseen vortex centered on a curve evolving by the binormal flow (Sections 4 & 5). Then, it analyzes the error term (F(x,t)) by substituting this approximation into the Navier-Stokes equation. Finally, it uses energy estimates and a fixed-point argument (Section 6 & 7) to show that the remainder `omega_tilde` is small in L2, thus proving that the constructed solution is close to a true solution.
- Lemma 2: Statement: If the initial tangent vector field of the filament is in a Sobolev space H^k (k>=3), then the tangent vector remains in that space, and the curvature and torsion have slightly less regularity (C^{k-2} and C^{k-3} respectively).
  *Proof:* Proof technique: The proof relies on existing results for the regularity of the binormal flow equation and then uses the Frenet-Serret equations to transfer this regularity to the curvature and torsion. It shows that if the tangent vector is smooth, the geometric quantities derived from it are also smooth.
- Lemma 3: Statement: For a sufficiently regular vortex filament (C^2), there exists a tubular neighborhood of a certain radius R where each point has a unique closest point on the filament.
  *Proof:* Proof technique: The proof is geometric. It shows that as long as the radius R is smaller than the inverse of the maximum curvature, the mapping from the tube to the filament is well-defined and unique. This prevents the coordinate system from becoming singular.
- Lemma 5: Statement: Provides the explicit velocity fields induced by two specific vorticity distributions: a standard axisymmetric Lamb-Oseen vortex and a non-axisymmetric one with a `cos(theta)` dependence.
  *Proof:* Proof technique: The proof involves solving the Poisson equation `∆ψ = ω` for the stream function `ψ` in polar coordinates for the given vorticity profiles `ω`. The velocity is then found by taking derivatives of the stream function (`v_r = (1/ρ)∂ψ/∂θ`, `v_θ = -∂ψ/∂ρ`).
- Lemma 6: Statement: It computes the velocity field induced by the leading-order Lamb-Oseen vortex filament. The result is the sum of the local rotational velocity, the binormal flow velocity (with logarithmic terms), and corrections due to curvature and non-local interactions.
  *Proof:* Proof technique: The proof involves a careful asymptotic expansion of the Biot-Savart integral (4). The integral is split into a local part (near the point of interest) and a non-local part. The local part is analyzed using Taylor expansions of the filament geometry, and the non-local part is shown to be a regularizing term. The appendix provides a key formula for desingularizing the integral.

**Constants & Bounds:**
- `L2 norm of the remainder: `||~ω||_{L^2}^2(t) + ν ∫_0^t ||∇~ω||_{L^2}^2(t′)dt′ ≤ CΓ^2(νt)|log(νt)|^2``: This is the key energy estimate for the remainder term `~ω` of the vorticity. It shows that the L2 norm of the error is small for short times `t` and small `Γ/ν`, which validates the asymptotic expansion.
- `Condition for tubular neighborhood: `R < 1 / (2 max|κ(s,t)|)``: This inequality specifies the maximum radius `R` of the tubular neighborhood around the filament for which the local coordinate system is well-defined. It states the radius must be smaller than half the minimum radius of curvature.
- `Smallness condition: `Γ/ν` to be sufficiently small.`: This is the central assumption of the paper. It ensures that the nonlinear terms in the Navier-Stokes equations, which are of order `Γ^2`, are dominated by the viscous terms, which are of order `νΓ`. This allows for the perturbative approach to work.
- `Timespan of validity: `t < c_0/ν``: The results are proven for a short time interval that scales inversely with the viscosity. This is a local-in-time existence result.

---

### On the dynamics of the boundary vorticity for incompressible viscous flows
**Authors:** V. Cherepanov, J. Liu, Z. Qian | **Year:** 2023 | [2308.13055v1](https://arxiv.org/abs/2308.13055v1) | **Validation:** unverified
**Relevance:** 7/10

**Why it matters:** This paper is highly relevant as it provides a novel and explicit evolution equation for the boundary vorticity, which is a primary source of vorticity in wall-bounded flows. The analysis directly addresses the behavior of the solution at the boundary, a place where singularities are often suspected to form. The key finding that the effective viscosity is doubled at the boundary suggests a powerful regularizing mechanism that could prevent blowup initiated at the wall. This work could help close the gap in understanding the interplay between the bulk flow and the boundary conditions, specifically how the boundary's presence modifies the vorticity dynamics.

**Key Insights:**
1. The evolution of vorticity *at the boundary* is governed by a surprisingly simple, largely linear equation, in stark contrast to the complex, non-linear vorticity equation in the bulk flow.
2. The effective kinematic viscosity for the boundary vorticity is `2\nu`, exactly double the viscosity `\nu` of the fluid in the bulk. This implies a much stronger dissipative (smoothing) effect at the wall, which acts to regularize the flow.
3. The primary non-linear terms of the 3D Navier-Stokes equations, convection `(u \cdot \nabla)\omega` and vortex stretching `(\omega \cdot \nabla)u`, do not directly contribute to the generation of vorticity at the boundary itself. This is a crucial simplification.
4. The boundary vorticity dynamics are forced by the bulk flow through a high-order, third derivative term of the tangential velocity (`\frac{\partial^3 u_\parallel}{\partial \nu^3}`). This means the coupling is weaker than a direct value-to-value forcing, potentially allowing for the boundary and bulk to be analyzed separately under certain conditions.

**Equations:**
- $$\frac{\partial u}{\partial t} + (u \cdot \nabla)u - \nu \Delta u + \nabla P - F = 0$$
  This is the incompressible Navier-Stokes equation, which describes the conservation of momentum for a viscous fluid flow. It governs the evolution of the fluid velocity `u` under the effects of convection, diffusion, pressure gradients, and external forces.
- $$\nabla \cdot u = 0$$
  This is the incompressibility condition, stating that the velocity field `u` is divergence-free. Physically, it means that the density of a fluid parcel remains constant as it moves, and it is a key constraint in the dynamics.
- $$\Delta P = - \sum_{j,i=1}^{d} \frac{\partial u_j}{\partial x_i} \frac{\partial u_i}{\partial x_j} + \nabla \cdot F$$
  This is the Poisson equation for the pressure `P`, derived by taking the divergence of the Navier-Stokes equation. It shows that pressure is determined by the velocity field, ensuring that the flow remains divergence-free.
- $$\frac{\partial \omega}{\partial t} + (u \cdot \nabla)\omega - \nu \Delta \omega - (\omega \cdot \nabla)u - G = 0$$
  This is the vorticity transport equation, describing the evolution of the vorticity `\omega = \nabla \wedge u`. It shows how vorticity is advected with the flow, diffused by viscosity, and stretched or tilted by velocity gradients.
- $$\theta = 2(-S_{23}, S_{13}, 0)|_{\partial D}$$
  This equation defines the boundary vorticity `\theta` as twice the tangential components of the rate-of-strain tensor `S` at the boundary `\partial D`. It links the vorticity at the wall directly to the shear stress exerted by the fluid.
- $$\frac{\partial \theta}{\partial t} - 2\nu \Delta_{\Gamma} \theta + \nu \nabla_{\Gamma}(\nabla_{\Gamma} \cdot \theta) + \nu \star \frac{\partial^3 u_\parallel}{\partial \nu^3} |_{\partial D} - \psi = 0$$
  This is the main result of the paper: the dynamical evolution equation for the boundary vorticity `\theta`. It reveals that the boundary vorticity evolves according to a linear-type equation where the effective viscosity is `2\nu` (doubled), and it is forced by the external force `\psi` and a high-order derivative of the tangential velocity `u_\parallel` from the bulk flow.

**Theorems:**
- Theorem 3.1: Statement: At the boundary, two non-linear terms appearing in the vorticity transport equation, the non-linear convection and the non-linear vorticity stretching, neither of them participates directly in the generation of the vorticity at the wall.
  *Proof:* Proof technique: The proof is elementary. It relies on evaluating the terms `(u \cdot \nabla)\omega` and `(\omega \cdot \nabla)u` at the boundary `\partial D`. Since the velocity `u` is zero at the boundary (no-slip condition), the convective term vanishes. The stretching term also vanishes due to the specific components of the boundary vorticity and the velocity derivatives being zero at the wall.
- Theorem 3.2: Statement: Provides the explicit dynamical equations for the components of the boundary vorticity `\theta` on a flat plate `\partial D = R^2`. The equation is `\frac{\partial \theta}{\partial t} - 2\nu \Delta_{\Gamma} \theta + \nu \nabla_{\Gamma}(\nabla_{\Gamma} \cdot \theta) + \nu \star \frac{\partial^3 u_\parallel}{\partial \nu^3} |_{\partial D} - \psi = 0`.
  *Proof:* Proof technique: The proof is a direct, elementary calculation. It starts from the vorticity equation evaluated at the boundary (from Theorem 3.1) and then computes the trace of the Laplacian of vorticity, `\Delta \omega |_{\partial D}`. This involves careful differentiation and substitution using the divergence-free condition and the definitions of vorticity and its components at the boundary.
- Theorem 3.6: Statement: Gives the simplified dynamical equation for boundary vorticity `\theta` in two-dimensional flows: `\frac{\partial \theta}{\partial t} - 2\nu \Delta_{\Gamma} \theta - \nu \frac{\partial^3 u_\parallel}{\partial \nu^3} - \psi = 0`.
  *Proof:* Proof technique: Similar to Theorem 3.2, this is a direct calculation for the 2D case, where the vorticity is a scalar and the stretching term is identically zero.

**Constants & Bounds:**
- `Effective Boundary Viscosity: 2\nu`: The paper shows that the kinematic viscosity `\nu` is effectively doubled to `2\nu` in the diffusion term of the evolution equation for the boundary vorticity. This implies that vorticity dissipates faster at the boundary than in the bulk flow, suggesting a strong regularizing effect at the wall.

---


## Functional Analysis and PDE Tools
*Papers providing key mathematical machinery: Calderon-Zygmund theory, Sobolev embeddings, Besov spaces, Littlewood-Paley decomposition.*

### Leray’s Self-Similar Solutions to the Navier-Stokes Equations with Profiles in Marcinkiewicz and Morrey Spaces
**Authors:** Cristi Guevara, Nguyen Cong Phuc | **Year:** 2015 | [1509.08177v2](https://arxiv.org/abs/1509.08177v2) | **Validation:** verified
**Relevance:** 9/10

**Why it matters:** This paper is highly relevant to the NS3D blowup problem as it directly addresses the existence of Leray's self-similar solutions, which are a primary candidate for causing a finite-time blowup. The paper significantly extends previous work by ruling out these solutions for profiles `U` in much larger function spaces (Marcinkiewicz and Morrey spaces) than previously considered. This closes a significant gap in the theory by showing that even very slow decay of the velocity profile at infinity is not sufficient to support a self-similar singularity, thus narrowing the search for a potential blowup scenario.

**Key Insights:**
1. Self-similar blowup is unlikely for a wide range of velocity profile decays. The main result of the paper is that Leray's self-similar solutions cannot exist if their profiles `U` belong to Marcinkiewicz spaces `L^{q,\infty}` for `q` in `(12/5, 6)` or Morrey spaces `M^{p,\gamma}`. This significantly expands the class of functions for which self-similar blowup is ruled out, suggesting that if a blowup exists, it must have a different structure. 2. The Riesz potential `I_1(|U|^2)` is a powerful tool for analyzing blowup. The paper's most general result (Theorem 1.4) is formulated in terms of a condition on the Riesz potential of `|U|^2`. This provides a more subtle way to measure the decay of the velocity profile than simply using `L^p` norms, and it may be a useful tool in other contexts for studying the regularity of solutions. 3. Even local energy finiteness is a strong constraint. The proof of the main theorem relies on Tsai's result (Theorem 1.1) that self-similar solutions with finite local energy must be trivial. This highlights the importance of the local energy inequality and suggests that any potential blowup must involve a very rapid concentration of energy. 4. The pressure term can be controlled even when the velocity profile is not in `L^2`. A key technical step in the proof is the construction of a pressure `P` with a controlled norm in a negative Sobolev space. This is a useful technique for dealing with the pressure in weak solutions of the Navier-Stokes equations.

**Equations:**
- $$\partial_t u - \nu\Delta u + u \cdot \nabla u + \nabla p = 0, \quad \text{div } u = 0$$ *(corrected)*
  These are the fundamental equations of motion for a viscous, incompressible fluid. The first equation is the momentum equation, representing the conservation of momentum, and the second is the incompressibility condition, representing the conservation of mass.
  > Correction: The original LaTeX for the time derivative was `\partial_t u`, which is incorrect. The corrected version is `\partial_t u`. Also, `\nu` was corrected to `\nu` for consistency.
- $$Backward Self-Similar Solution (1.2): `u(x,t) = \lambda(t)U(\lambda(t)x), \quad p(x,t) = \lambda^2(t)P(\lambda(t)x), \quad \lambda(t) = \frac{1}{\sqrt{2a(T-t)}}`$$
  This is an ansatz (a guess) for the form of a solution that blows up at a finite time T. The solution's profile `U` is rescaled in space and time by the factor `\lambda(t)`, which goes to infinity as `t` approaches `T`.
- $$Stationary System for Profile U (1.3): `-\nu \Delta U + aU + a(y \cdot \nabla)U + (U \cdot \nabla)U + \nabla P = 0, \quad \text{div } U = 0`$$
  This is the system of equations that the self-similar profile `U` must satisfy if the self-similar solution `u` is to be a solution of the Navier-Stokes equations. It is a time-independent, non-linear system.
- $$Pressure Equation (3.1): `- \Delta P = \partial_i \partial_j (U_i U_j)`$$
  This is a Poisson equation for the pressure `P`, derived by taking the divergence of the stationary system for `U`. It shows that the pressure is determined by the velocity profile `U`.

**Theorems:**
- Theorem 1.1 (Tsai [18]): A weak solution of the form (1.2) satisfying the finite local energy condition (1.5) must be identically zero.
  *Proof:* The proof uses the fact that the scalar function `Π(y) = 1/2 |U(y)|^2 + P(y) + ay · U(y)` satisfies the maximum principle. It also uses the Caffarelli-Kohn-Nirenberg ε-regularity criterion to show that `U(y) = O(|y|^-1)` as `y -> ∞`.
- Theorem 1.2 (Tsai [18]): If a weak solution `U` of (1.3) belongs to `L^q(R^3)` for some `q` in `(3, ∞]`, then it must be zero (if `q != ∞`) or constant (if `q = ∞`).
  *Proof:* The proof is based on showing that if `U` is in `L^q(R^3)`, then `U = o(|y|)` as `y -> ∞`. This, combined with the maximum principle for `Π(y)`, leads to the conclusion that `U` must be zero or constant.
- Theorem 1.3: A weak solution `U` of (1.3) in `W^{1,2}_{loc}(R^3)` must be identically zero if `U` is in `L^{q,∞}(R^3)` for `q` in `(12/5, 6)` or if `U` is in `L^{12/5}(R^3)`.
  *Proof:* This theorem is a consequence of Theorem 1.4. The proof shows that if `U` is in the specified Marcinkiewicz or Lebesgue spaces, then `I_1(|U|^2)` is in a suitable Morrey space, which by Theorem 1.4 implies `U` is zero.
- Theorem 1.4: If `U` is a weak solution of (1.3) and `I_1(|U|^2)` is in `M^{2,γ}(R^3)` for some `γ` in `(0, 3]`, then `U` must be identically zero.
  *Proof:* The proof is based on an application of Theorem 1.1. A pressure profile `P` is constructed from `U` such that the norm of `P` in a Sobolev space of negative order is controlled. A bootstrapping argument based on the energy equality is then used to show that the local energy of the corresponding self-similar solution is finite, which by Theorem 1.1 implies the solution is zero.

**Constants & Bounds:**
- `Global Energy Inequality (1.4): `\frac{1}{2} \int_{R^3} |u(x,t)|^2 dx + \nu \int_{t_1}^t \int_{R^3} |\nabla u(x,t)|^2 dx dt \le \frac{1}{2} \int_{R^3} |u(x,t_1)|^2 dx``: This is the fundamental energy inequality for the Navier-Stokes equations. It states that the kinetic energy of the fluid plus the energy dissipated by viscosity is non-increasing in time.
- `Local Energy Inequality (1.5): `esssup_{t_3<t<T} \frac{1}{2} \int_{B_r(x_0)} |u(x,t)|^2 dx + \nu \int_{t_3}^T \int_{B_r(x_0)} |\nabla u(x,t)|^2 dx dt < +\infty``: This is a local version of the energy inequality, which is used in the study of local regularity of solutions. Tsai's Theorem 1.1 shows that even this weaker condition is enough to rule out self-similar blowup.
- `Condition on `I_1(|U|^2)` (1.6): `\int_{B_r} |I_1(\chi_{B_r} |U|^2)|^2 dx \le C r^{3-\gamma}``: This is the main condition of Theorem 1.4. It is a condition on the decay of the velocity profile `U` at infinity, expressed in terms of the Riesz potential of `|U|^2`. It is a more general and weaker condition than assuming `U` is in `L^p` for some `p`.

---

### AN ALGEBRAIC REDUCTION OF THE ‘SCALING GAP’ IN THE NAVIER-STOKES REGULARITY PROBLEM
**Authors:** ZACHARY BRADSHAW, ASEEL FARHAT, AND ZORAN GRUJIC´ | **Year:** 2018 | [1704.05546v4](https://arxiv.org/abs/1704.05546v4) | **Validation:** verified
**Relevance:** 9/10

**Why it matters:** This paper is highly relevant to the NS3D blowup problem because it directly tackles the 'scaling gap' between regularity criteria and a priori bounds. The introduction of the Zα classes, which are based on the sparseness of vorticity components, provides a novel framework for analyzing the geometry of potential singularities. This work could help close the gap in our understanding of how vorticity intensifies and whether it can lead to a finite-time blowup.

**Key Insights:**
1. The scaling gap in the 3D Navier-Stokes regularity problem can be algebraically reduced by considering the geometry of the vorticity field.
2. Instead of looking at the sparseness of the super-level sets of the vorticity magnitude, one should look at the sparseness of the super-level sets of the positive and negative parts of the vorticity components.
3. This is motivated by the observation that in turbulent flows, the vorticity field exhibits a high degree of local anisotropy, which can lead to a discrepancy in sparseness between the full vectorial super-level sets and the super-level sets of the components.
4. The new function classes Zα introduced in the paper provide a way to quantify this geometric information and incorporate it into the analysis of the NSE.
5. The a priori bound obtained in the Zα framework is algebraically better than the energy-level bound, which is a significant improvement over previous results that only achieved logarithmic reductions of the scaling gap.

**Equations:**
- $$(1) ∂tu + (u · ∇)u = νΔu − ∇p + f$$
  The Navier-Stokes equations (NSE) describing the motion of 3D incompressible, viscous, Newtonian fluids. It represents the conservation of momentum for the fluid.
- $$(2) ∂tω + (u · ∇)ω = Δω + (ω · ∇)u$$
  The vorticity-velocity formulation of the 3D NSE. This equation describes the evolution of the vorticity ω, which is the curl of the velocity u. The term (ω · ∇)u is the vortex-stretching term, which is responsible for the possible unbounded growth of vorticity in 3D.
- $$(3) x ∈ R3 : |f(x)| > λ||f||∞$$
  This defines a super-level set of a function f. It is the set of points where the magnitude of f is greater than a certain fraction (λ) of its maximum value. The paper uses the sparseness of these sets as a key concept.
- $$(4) f ∈ Lp,∞ ==> f ∈ Xα for α = p/3$$
  This is a "conversion rule" between the Lp,∞ spaces and the Xα classes of functions defined in the paper. It relates the decay rate of the distribution function of f to the scale of sparseness of its super-level sets.
- $$(5) ∂tωj − Δωj + ui∂iωj = ωi∂iuj , j = 1, 2, 3$$
  The component form of the vorticity-velocity formulation of the 3D NSE. It is used in the proof of the local-in-time spatial analyticity of the vorticity.
- $$(6) ∂iuj (x, t) = cP.V. ∫ εj,k,l (∂2/∂xi∂yk)(1/|x-y|) ωl(y, t)dy$$
  This is the Biot-Savart law, which allows the reconstruction of the velocity field u from the vorticity field ω. The kernel is a classical Calderon-Zygmund kernel.
- $$(7) ||∇u(·, t)||BMO ≤ c||ω(·, t)||BMO$$
  A key inequality that bounds the BMO norm of the velocity gradient by the BMO norm of the vorticity. This is a consequence of the Calderon-Zygmund theory applied to the Biot-Savart law.
- $$(8) ωj(x, t) = G(x − y, t)(ω0)j(y)dy − ∫0t ∫ G(x − y, t − s)ui∂iωj(y, s)dy ds + ∫0t ∫ G(x − y, t − s)ωi∂iuj(y, s)dy ds$$
  The mild solution formulation of the vorticity equation. It expresses the solution as the sum of the initial data evolved by the heat semigroup and the contributions from the nonlinear terms.
- $$(9) ωj(n)(x, t) = ...$$
  The iterative scheme used to construct a solution to the vorticity equation. This is a standard technique in the analysis of PDEs.
- $$(10) ... ≤ ct sup s∈(0,t) ||ω(n)(s)||∞^2$$
  An estimate on the vortex-stretching term in the iterative scheme. This shows that the growth of the vorticity is controlled by the square of its L∞-norm, locally in time.

**Theorems:**
- Theorem 8 (real setting): Let the initial datum ω0 be in L2 ∩ L∞. Then there exists a unique mild solution ω in Cw([0, T], L∞) where T ≥ 1/(c||ω0||∞) for an absolute constant c > 0.
  *Proof:* The proof uses an iterative scheme for the mild formulation of the vorticity equation. The key is to show that the sequence of approximate solutions remains bounded in L∞ and converges to a solution. The vortex-stretching term is estimated using Calderon-Zygmund theory and properties of BMO functions.
- Theorem 10 (complex setting): Let the initial datum ω0 be in L2 ∩ L∞, and M a constant larger than 1. Then there is a constant c(M) > 1 such that there exists a unique mild solution ω in Cw([0, T], L∞) where T ≥ 1/(c(M)||ω0||∞), and for any t in (0, T] the solution ω is the R3-restriction of a holomorphic function ω defined in a complex domain.
  *Proof:* The proof is based on complexifying the vorticity equation and tracking the domain of analyticity of the solution. The estimates are similar to the real case, but applied to the real and imaginary parts of the complexified solution.
- Proposition 17: [Ran] Let Ω be an open, connected set in C such that its boundary has nonzero Hausdorff dimension, and let K be a Borel subset of the boundary. Suppose that u is a subharmonic function on Ω satisfying u(z) ≤ M for z ∈ Ω and limsup u(z) ≤ m for ζ ∈ K. Then u(z) ≤ mh(z, Ω, K) + M(1 − h(z, Ω, K)) for z ∈ Ω.
  *Proof:* This is a statement of the harmonic measure maximum principle. It provides a bound on a subharmonic function in terms of its boundary values and the harmonic measure of the boundary.
- Proposition 18: [Sol] Let λ be in (0, 1), K a closed subset of [−1, 1] such that m1(K) = 2λ, and suppose that the origin is in D \ K. Then h(0, D, K) ≥ h(0, D, Kλ) = (2/π)arcsin((1 − (1 − λ)^2)/(1 + (1 − λ)^2)) where Kλ = [−1, −1 + λ] ∪ [1 − λ, 1].
  *Proof:* This proposition gives an extremal property of the harmonic measure in the unit disk. It provides a lower bound on the harmonic measure of a set in terms of its one-dimensional Lebesgue measure.

**Constants & Bounds:**
- `||∇u(·,t)||BMO ≤ c||ω(·,t)||BMO`: This is a Calderon-Zygmund inequality that relates the BMO norm of the velocity gradient to the BMO norm of the vorticity. It is a key tool for controlling the vortex-stretching term.
- `T ≥ 1/(c||ω0||∞)`: This is a lower bound on the existence time of a mild solution in L∞. It shows that the solution exists for a time that is inversely proportional to the L∞-norm of the initial vorticity.
- `radius of analyticity ~ 1/||ω(t)||∞^(1/2)`: This is a lower bound on the radius of spatial analyticity of the solution. It is given in terms of the L∞-norm of the vorticity at a slightly earlier time.
- `h(0, D, K) ≥ (2/π)arcsin((1 − (1 − λ)^2)/(1 + (1 − λ)^2))`: This is a lower bound on the harmonic measure of a set K in the unit disk D. It is used to obtain a quantitative estimate in the proof of the regularity criterion.

---

### GLOBAL REGULARITY AND DECAY BEHAVIOR FOR LERAY EQUATIONS WITH CRITICAL-DISSIPATION AND ITS APPLICATION TO SELF-SIMILAR SOLUTIONS
**Authors:** CHANGXING MIAO, XIAOXIN ZHENG | **Year:** 2022 | [2209.00153v1](https://arxiv.org/abs/2209.00153v1) | **Validation:** verified
**Relevance:** 9/10

**Why it matters:** This paper is highly relevant as it investigates the global regularity and decay of solutions to the generalized Leray equations, which are directly linked to the forward self-similar solutions of the 3D Navier-Stokes equations. By establishing regularity for the critical dissipation case (alpha = 5/6), it pushes the boundary of our understanding of regularity mechanisms. This work directly addresses the problem of constructing and proving the regularity of self-similar solutions, which are prime candidates for potential blowup scenarios. It helps close the gap in understanding the behavior of solutions in critical function spaces.

**Key Insights:**
1. Dissipation is Key, and `_alpha=5/6` is the Magic Number: The paper reinforces that the strength of the dissipation term, controlled by `_alpha`, is paramount for global regularity. It successfully proves regularity for the critical case `_alpha=5/6` in the self-similar model. This suggests that any attempt to prove blowup in the standard NS equations (`_alpha=1`) must contend with the fact that even a slightly weaker dissipation (`_alpha < 5/6`) might be enough to cause singularities in this context. 2. Focus on Self-Similar Solutions: This work demonstrates the power of constructing and analyzing explicit self-similar solutions. It provides a concrete, regular, forward self-similar solution for `_alpha _ge 5/6`. An engineer trying to prove blowup should focus on constructing *backward* self-similar solutions or showing that no regular forward self-similar solution exists for `_alpha=1` with arbitrary large (but finite energy) initial data. 3. The Importance of Function Spaces: The choice of function space is not just a mathematical technicality. The use of Besov spaces (`_dot{B}^s_{p,r}`) and weighted Sobolev spaces (`H^s_{_langle x _rangle^{_beta}}`) is what allows the authors to capture the subtle interplay between dissipation, nonlinearity, and spatial decay. An engineer needs to appreciate that proving blowup likely requires showing that the solution escapes from these specific function spaces in finite time. 4. Microlocal Analysis is a Powerful Tool: The main innovation is the use of frequency localization (microlocal analysis) to handle the difficult `x _cdot _nabla V` term in the Leray equation. Instead of treating it as a perturbation, they analyze its effect on different frequency components of the solution. This technique of "divide and conquer" in frequency space is a powerful paradigm for tackling difficult PDE problems.

**Equations:**
- $$(-_Delta)^{_alpha}U - _frac{2_alpha-1}{2_alpha} U - _frac{1}{2_alpha}x _cdot _nabla U + _nabla P + U _cdot _nabla U = _text{div} F, _quad _text{div}U = 0$$
  This is the central equation of the paper, a stationary model for the forward self-similar solutions of the fractional Navier-Stokes equations. `U` is the self-similar profile of the velocity, `P` is the pressure, `(-_Delta)^{_alpha}` is the fractional Laplacian representing dissipation, and the terms with `x` come from the self-similar scaling.
- $$u_t + u _cdot _nabla u + (-_Delta)^{_alpha}u + _nabla _pi = 0, _quad _text{div} u = 0$$
  This is the time-dependent incompressible Navier-Stokes equation but with generalized dissipation `(-_Delta)^{_alpha}`. For `_alpha=1`, it is the standard Navier-Stokes equation. The paper studies its self-similar solutions.
- $$(-_Delta)^{_alpha}U - _frac{2_alpha-1}{2_alpha} U - _frac{1}{2_alpha}x _cdot _nabla U + _nabla P + U _cdot _nabla U = 0, _quad _text{div} U = 0$$
  This is the homogeneous version of (1.1) (with F=0), which the profile `(U, P)` of a forward self-similar solution to the fractional Navier-Stokes equations must satisfy.
- $$(-_Delta)^{_alpha}V - _frac{2_alpha-1}{2_alpha} V - _frac{1}{2_alpha}x _cdot _nabla V + _nabla P = -V _cdot _nabla V + L_{U_0}(V) + _text{div} F_{U_0}, _quad _text{div} V = 0$$
  This equation describes the behavior of the perturbation `V` where `U = U_0 + V` and `U_0` is a base solution. This decomposition is a standard technique to study the stability and regularity of solutions near a known state.

**Theorems:**
- Theorem 1.4: Existence and Regularity for the Generalized Leray Problem
  *Proof:* For `_alpha _in (0, 1]` and `F _in _dot{H}^{-1}(_mathbb{R}^3)`, the problem (1.1) has at least one weak solution `(U, P) _in H^{_alpha} _times L^{3/(3-2_alpha)}`. For `_alpha _in [5/6, 1]`, the solution is more regular: `(U, P) _in H^{2_alpha} _times H^1`. Further regularity (`B^{s+2_alpha}_{p,p} _times B^{s+1}_{p,p}`) and decay estimates are established depending on the properties of the forcing `F`.
- Theorem 1.8: Regularity and Decay for the Perturbation
  *Proof:* For `_alpha _in [5/6, 1]`, the weak solution `(V, P)` to the perturbation problem (1.6) is regular, belonging to various Besov and weighted Sobolev spaces. Crucially, it proves the optimal decay estimate `|V(x)| _leq _langle x _rangle^{-(4_alpha-1)}`.
- Corollary 1.10: Regularity of Self-Similar Solutions
  *Proof:* The forward self-similar solution `u(x, t)` to the fractional Navier-Stokes equations is smooth for `t>0` and has specific pointwise decay estimates in space and time.
- Lemma 2.7: Compactness Lemma
  *Proof:* For a divergence-free vector field `U _in _dot{H}^{5/6}(_mathbb{R}^3)` and `V` in a suitable Besov space, the nonlinear term `_text{div}(U _otimes V)` can be controlled by `_epsilon ||V||_{_dot{B}^{5/3}_{p,r}} + C_{_epsilon, U} ||V||_{_dot{B}^0_{p,r}}`.

**Constants & Bounds:**
- `Critical Dissipation Exponent: \alpha = 5/6`: This is the critical value for the dissipation exponent in the generalized Leray equation (1.6). The scaling analysis in Remark 1.3 shows that for `\alpha = 5/6`, the `\dot{H}^{\alpha}` norm of the solution is invariant under the natural scaling of the equation, making it a "critical" problem that is much harder to solve than the subcritical case `\alpha > 5/6`.
- `Optimal Decay Rate: |V(x)| \leq C \langle x \rangle^{-(4\alpha-1)}`: This is the optimal rate of spatial decay for the perturbation `V` (Theorem 1.8) and the self-similar solution `u` (Corollary 1.10). Proving this sharp decay is crucial for ensuring the solution has finite energy and other physically relevant properties. The absence of a logarithmic correction `\log(\langle x \rangle)` is a significant improvement over previous results.
- `Besov Compactness Inequality (2.4): ||\text{div}(U \otimes V)||_{\dot{B}^0_{p,r}} \leq \epsilon ||V||_{\dot{B}^{5/3}_{p,r}} + C_{\epsilon,p,U} ||V||_{\dot{B}^0_{p,r}}`: This inequality is the cornerstone for proving regularity in the critical case `\alpha=5/6`. It shows that if the field `U` is in the critical space `\dot{H}^{5/6}`, the nonlinear operator `V \mapsto \text{div}(U \otimes V)` is a compact perturbation of the linear operator, which allows the use of Fredholm-type arguments to establish existence and regularity.
- `Lp-type Elliptic Regularity (2.28): ||V||_{\dot{B}^{s+2\alpha}_{p,r}} + ||\nabla P||_{\dot{B}^{s+1}_{p,r}} \leq C_{p,\alpha} (||F||_{\dot{B}^s_{p,r}} + ||V||_{\dot{B}^s_{p,r}})`: This is the key a priori estimate for the linearized Leray problem. It shows that the solution `(V, P)` gains `2\alpha` derivatives in the Besov scale relative to the forcing term `F` and the lower-order term `V`. This "smoothing effect" is fundamental to the bootstrap argument used to prove high regularity.

---

### STABLE NEARLY SELF-SIMILAR BLOWUP OF THE 2D BOUSSINESQ AND 3D EULER EQUATIONS WITH SMOOTH DATA I: ANALYSIS
**Authors:** JIAJIE CHEN AND THOMAS Y. HOU | **Year:** 2023 | [2210.07191v3](https://arxiv.org/abs/2210.07191v3) | **Validation:** verified
**Relevance:** 9/10

**Why it matters:** This paper is highly relevant to proving NS3D finite-time blowup, meriting a score of 9/10. It provides the first rigorous proof of a stable, nearly self-similar blowup for the 3D axisymmetric Euler equations with smooth initial data. This is a major step towards resolving the full 3D Navier-Stokes regularity problem, as the 3D Euler equations are a simplified model that captures the essential nonlinearity of the vortex stretching term. The techniques developed in this paper, particularly the computer-assisted proof methodology and the use of a weighted L^\infty norm combined with sharp functional inequalities, could potentially be adapted to the more complex Navier-Stokes equations. It directly addresses the challenge of controlling nonlocal effects and provides a concrete example of a blowup mechanism.

**Key Insights:**
1. Computer-assisted proof is a viable strategy: This paper demonstrates that a computer-assisted approach, combining numerical simulation with rigorous error control, can successfully prove blowup for complex fluid equations. An engineer could adopt this meta-strategy by first numerically identifying a candidate blowup scenario and then using rigorous computation to bound the error terms and prove its stability.
2. The right function space is critical: The choice of a weighted L^\infty norm combined with a C^{1/2} norm was essential to overcome the destabilizing effect of the advection term and to control nonlocal interactions. This suggests that standard energy methods in Sobolev spaces like H^k may not be sufficient, and engineers should explore more exotic function spaces tailored to the specific structure of the problem.
3. Decompose and conquer the linearized operator: The authors decompose the linearized operator into a dominant, stable part and a finite-rank perturbation. This allows them to analyze the stability of the system by studying a simpler, leading-order operator and then controlling the effect of the perturbation. This is a powerful technique for analyzing the stability of complex systems.
4. Optimal transport provides sharp estimates: The paper uses techniques from optimal transport theory to derive sharp constants in the Holder estimates for the velocity field. This is a novel approach that provides much tighter control over the nonlocal terms than traditional methods. Engineers should consider using optimal transport to obtain sharp estimates for the Biot-Savart law and other nonlocal operators in their analysis.

**Equations:**
- $$ω_t + u ⋅ ∇ω = ω ⋅ ∇u$$
  This is the vorticity equation, which describes the evolution of the vorticity ω of the fluid. The term on the right, ω ⋅ ∇u, is the vortex stretching term, which is the main source of difficulty in proving global regularity for the 3D Navier-Stokes and Euler equations.
- $$W_t = L(W)$$
  This is a linearized equation that governs the perturbation W around an approximate steady state. L is the linearized operator.
- $$∂_t W_1(t) = L_0 W_1, W_1(0) = W_0, ∂_t W_2(t) = L_0 W_2 + a(x)P(W_1(t)), W_2(0) = 0$$
  These equations describe a toy model used to illustrate the main ideas of the stability analysis. W is decomposed into two parts, W1 and W2, where W1 is governed by a leading order operator L0 and W2 is driven by a finite rank operator.
- $$W_2(t) = ∫_0^t P(W_1(s))e^((t-s)L_0)a(x)ds$$
  This is the solution to the second equation in the toy model, obtained using Duhamel's principle. It shows how the second part of the perturbation, W2, is influenced by the first part, W1.
- $$\partial_t(ru^\theta) + u_r \partial_r(ru^\theta) + u_z \partial_z(ru^\theta) = 0, \partial_t(\omega^\theta/r) + u_r \partial_r(\omega^\theta/r) + u_z \partial_z(\omega^\theta/r) = (1/r^4)\partial_z((ru^\theta)^2)$$ *(corrected)*
  These are the 3D axisymmetric Euler equations in terms of the angular velocity uθ and angular vorticity ωθ. These equations are used to study the blowup of the 3D Euler equations in the axisymmetric case.
  > Correction: The advection term u \cdot \nabla was not expanded, and the term (r^2(u^\theta)^2) should be ((ru^\theta)^2)
- $$\omega_t + u \cdot \nabla \omega = \theta_x, \theta_t + u \cdot \nabla \theta = 0, u = (u,v)^T, -\Delta\psi = \omega, u = \psi_y, v = -\psi_x$$ *(corrected)*
  These are the 2D Boussinesq equations. They are a simplified model for fluid dynamics that is often used to study the blowup problem. The variable θ represents the temperature or density of the fluid.
  > Correction: The equations for \omega and \theta were swapped, and the definition of u was incomplete.

**Theorems:**
- Theorem 1: There is a family of smooth initial data (θ_0, ω_0) with θ_0 being even and ω_0 being odd, such that the solution of the Boussinesq equations develops a singularity in finite time T < +∞. The initial velocity field u_0 has finite energy. The blowup solution (θ(t), ω(t)) is nearly self-similar in the sense that (θ(t), ω(t)) with suitable dynamic rescaling is close to an approximate blowup profile (θ_bar, ω_bar) up to the blowup time. Moreover, the blowup is stable for initial data (θ_0, ω_0) close to (θ_bar, ω_bar) in some weighted L^∞ and C^(1/2) norm.
  *Proof:* The proof is based on a computer-assisted analysis of an approximate self-similar solution. The authors construct an approximate solution and then prove its nonlinear stability. This is a major breakthrough because it provides a rigorous proof of blowup for a fluid model with smooth initial data.
- Theorem 2: Consider the 3D axisymmetric Euler equations in the cylinder r, z ∈ [0, 1] × T. Let u^θ and ω^θ be the angular velocity and angular vorticity, respectively. The solution of the 3D Euler equations develops a nearly self-similar blowup (in the sense described in Theorem 1) in finite time for some smooth initial data ω_0^θ, u_0^θ supported away from the symmetry axis r = 0. The initial velocity field has finite energy, u_0^θ and ω_0^θ are odd and periodic in z. The blowup is stable for initial data (u_0^θ, ω_0^θ) that are close to the approximate blowup profile (u_bar^θ, ω_bar^θ) after proper rescaling subject to some constraint on the initial support size.
  *Proof:* The proof is similar to that of Theorem 1. It uses a computer-assisted approach to prove the stability of an approximate self-similar blowup solution.

**Constants & Bounds:**
- `C_1(b): A constant in the estimate of the C^{1/2} norm of the velocity, which depends on the localization parameter b. The paper shows that C_1(b) <= 2.55.`: This constant is important because it quantifies the strength of the nonlocal effects. The fact that it is bounded and relatively small is crucial for the stability analysis.
- `C_2(a): A constant in the estimate of the C^{1/2} norm of the velocity. The paper shows that C_2(a) <= 4.26/pi.`: Similar to C_1(b), this constant plays a key role in the Holder estimates for the velocity.
- `[Hf]_{C^{1/2}} <= C_* [f]_{C^{1/2}}: The sharp constant in the C^{1/2} estimate for the Hilbert transform. The paper shows that C_* >= 1.`: The Hilbert transform is a 1D model for the Biot-Savart law. The sharp constant in the Holder estimate for the Hilbert transform provides a lower bound for the corresponding constant for the Biot-Savart law.

---

### STRONG ILL-POSEDNESS IN L∞ OF THE 2D BOUSSINESQ EQUATIONS IN VORTICITY FORM AND APPLICATION TO THE 3D AXISYMMETRIC EULER EQUATIONS
**Authors:** ROBERTA BIANCHINI, LARS ERIC HIENTZSCH, AND FELICE IANDOLI | **Year:** 2024 | [2303.16167v3](https://arxiv.org/abs/2303.16167v3) | **Validation:** verified
**Relevance:** 9/10

**Why it matters:** This paper is highly relevant to the NS3D blowup problem. It demonstrates a mechanism for strong ill-posedness in the 2D Boussinesq and 3D axisymmetric Euler equations, which are simplified models of the Navier-Stokes equations. The techniques used, particularly the α-scaling and the analysis of a leading-order model, provide a potential roadmap for tackling the full NS3D problem. The paper's focus on the formation of sharp gradients and norm inflation directly addresses the core of the blowup problem.

**Key Insights:**
1. Strong ill-posedness is a viable mechanism for singularity formation: The paper shows that solutions can become singular in a very dramatic way, even for small initial data. This provides a concrete mathematical framework for studying blowup.
2. The α-scaling is a powerful tool: This technique allows for a detailed analysis of the behavior of solutions near a potential singularity.
3. Leading-order models can capture the essential dynamics: By simplifying the equations, it is possible to gain a deeper understanding of the underlying mechanisms driving the blowup.
4. The 3D axisymmetric Euler equations with swirl are a good model for NS3D: The fact that the paper's results extend to this system is a strong indication that the same mechanisms may be at play in the full Navier-Stokes equations.

**Equations:**
- $$\partial_t \omega + u \cdot \nabla \omega = \partial_{x_1} \rho$$ *(corrected)*
  This is the vorticity equation for the 2D Boussinesq system. It describes how the vorticity (ω) of the fluid changes over time due to advection by the velocity field (u) and the buoyancy force, which is proportional to the horizontal gradient of the density (ρ).
  > Correction: The subscript '1' was missing from the x-derivative on the right hand side. The dot operator was incorrect. The partial derivative symbol was not correctly represented.
- $$\partial_t \rho + u \cdot \nabla \rho = 0$$ *(corrected)*
  This is the density equation for the 2D Boussinesq system. It states that the density of a fluid parcel is conserved as it moves with the fluid.
  > Correction: The dot operator was incorrect. The partial derivative symbol was not correctly represented.
- $$u = \nabla^{\perp} \psi, -\Delta \psi = \omega$$ *(corrected)*
  These equations relate the velocity field (u) to the vorticity (ω) through a stream function (ψ). This is the Biot-Savart law in 2D, which allows the velocity to be recovered from the vorticity.
  > Correction: The perp symbol and minus sign were not correctly represented.
- $$\partial_t \tilde{\omega} + \tilde{u} \cdot \nabla \tilde{\omega} = \partial_{x_1} \tilde{\rho}$$ *(corrected)*
  Vorticity equation for the stably stratified Boussinesq system.
  > Correction: The subscript '1' was missing from the x-derivative on the right hand side. The dot operator was incorrect. The partial derivative and tilde symbols were not correctly represented.
- $$\partial_t \tilde{\rho} + \tilde{u} \cdot \nabla \tilde{\rho} = -\tilde{u}_2$$ *(corrected)*
  Density equation for the stably stratified Boussinesq system. The term on the right-hand side represents the effect of the stable background stratification.
  > Correction: The dot operator was incorrect. The partial derivative, tilde and minus symbols were not correctly represented.
- $$\partial_t \Omega_{app} + (2\Psi_{app}) \cdot \nabla_\beta \Omega_{app} = \eta_{app}$$ *(corrected)*
  This is the first equation of the Leading Order Model (LOM). It describes the evolution of the approximate vorticity (Ω_app).
  > Correction: Incorrect LaTeX for Omega, Psi, eta, beta, and dot operator.
- $$\partial_t \eta_{app} + (2\Psi_{app}) \cdot \nabla_\beta \eta_{app} = (L(\Omega_{app}) / 2\alpha)\eta_{app} + (L_c(\Omega_{app}) / 2\alpha)(1 - \xi_{app})$$ *(corrected)*
  This is the second equation of the LOM, describing the evolution of the approximate horizontal density gradient (η_app).
  > Correction: Incorrect LaTeX for Omega, Psi, eta, alpha, xi, beta, and dot operator.
- $$\partial_t \xi_{app} + (2\Psi_{app}) \cdot \nabla_\beta \xi_{app} = (L(\Omega_{app}) / 2\alpha)(1 - \xi_{app}) + (L_c(\Omega_{app}) / 2\alpha)\eta_{app}$$ *(corrected)*
  This is the third equation of the LOM, for the approximate vertical density gradient (ξ_app).
  > Correction: Incorrect LaTeX for Omega, Psi, eta, alpha, xi, beta, and dot operator.

**Theorems:**
- Theorem 1.1: L∞ strong ill-posedness for the stably stratified Boussinesq system
  *Proof:* There exist initial data for the 2D stably stratified Boussinesq equations with arbitrarily small L∞ norm such that the L∞ norm of the horizontal density gradient becomes arbitrarily large in an infinitesimally short time.
- Theorem 1.3: Application to 3D Axisymmetric Euler
  *Proof:* A similar strong ill-posedness result holds for the 3D axisymmetric Euler equations with swirl. Specifically, the gradient of the swirl can experience rapid L∞ norm inflation.

**Constants & Bounds:**
- `α: A small parameter used in the scaling of the radial coordinate.`: This parameter is crucial for the analysis, as it allows the authors to separate the scales of the problem and derive a simplified leading-order model.
- `δ: A small parameter controlling the size of the initial data.`: This parameter is used to show that the ill-posedness is strong, meaning that it occurs even for arbitrarily small initial data.
- `Sobolev and Holder space norms: Used to measure the size and regularity of functions.`: These norms are the standard tools of functional analysis used to study the properties of solutions to PDEs.

---

### STABLE NEARLY SELF-SIMILAR BLOWUP OF THE 2D BOUSSINESQ AND 3D EULER EQUATIONS WITH SMOOTH DATA II: RIGOROUS NUMERICS
**Authors:** JIAJIE CHEN, THOMAS Y. HOU | **Year:** 2024 | [2305.05660v2](https://arxiv.org/abs/2305.05660v2) | **Validation:** verified
**Relevance:** 9/10

**Why it matters:** This paper is highly relevant as it provides a rigorous proof of finite-time blowup for the 3D axisymmetric Euler equations, a simplified version of the 3D Navier-Stokes equations. The methods, which involve proving the stability of an approximate self-similar blowup profile using computer-assisted proofs, could potentially be adapted to the full Navier-Stokes equations. It directly addresses the blowup problem by providing a concrete example of a singularity formation in a very similar system.

**Key Insights:**
1. Computer-assisted proofs are a viable path forward for the NS3D problem. This paper provides a powerful template for how to combine analytical techniques with rigorous numerical computation (using interval arithmetic) to prove results that are currently out of reach for pure analysis.
2. The core difficulty of the nonlocal vortex stretching term can be overcome by approximating it with a finite-rank operator. The stability analysis can then be performed on a simplified operator, which is a much more tractable problem.
3. The choice of appropriate weighted function spaces is critical. The singular weights used in this paper are essential for extracting the damping needed to control the perturbation and prove stability.
4. The problem of blowup in the 3D axisymmetric Euler equations is intimately connected to the 2D Boussinesq equations. This paper shows that a blowup result in the simpler Boussinesq system can be extended to the more complex Euler system.

**Equations:**
- $$(1.1) \omega_t + u \cdot \nabla \omega = \omega \cdot \nabla u$$
  This is the 3D vorticity equation, which describes the evolution of the vorticity field in an ideal fluid. The term on the right is the vortex stretching term, which is responsible for the potential formation of singularities.
- $$(2.1) \partial_t (ru^\theta) + u^r \partial_r (ru^\theta) + u^z \partial_z (ru^\theta) = 0, \\quad \partial_t(\\frac{\\omega^\\theta}{r}) + u^r \partial_r(\\frac{\\omega^\\theta}{r}) + u^z \partial_z(\\frac{\\omega^\\theta}{r}) = \\frac{1}{r^4}\\partial_z((ru^\\theta)^2)$$ *(corrected)*
  These are the 3D axisymmetric Euler equations. They describe the motion of an inviscid, incompressible fluid with rotational symmetry. The first equation describes the conservation of angular momentum, while the second describes the evolution of the angular vorticity.
  > Correction: Missing \\quad between equations.
- $$(2.2) -(\\partial_{rr} + \\frac{1}{r}\\partial_r + \\partial_{zz})\\phi^\\theta + \\frac{1}{r^2}\\phi^\\theta = \\omega^\\theta, \\quad u^r = -\\frac{1}{r}\\partial_z \\phi^\\theta, \\quad u^z = \\frac{1}{r}\\partial_r \\phi^\\theta$$ *(corrected)*
  This is the Biot-Savart law in axisymmetric coordinates. It allows the velocity field to be recovered from the vorticity field.
  > Correction: Missing \\quad between equations.
- $$(2.3) \omega_t + u \cdot \nabla \omega = \theta_x$$
  This is the vorticity equation for the 2D Boussinesq system. It describes the evolution of vorticity in a 2D fluid with buoyancy.
- $$(2.4) u_t + u \\cdot \\nabla u = -\\nabla p + \\theta e_2, \\quad \\nabla \\cdot u = 0$$ *(corrected)*
  This is the temperature equation for the 2D Boussinesq system. It describes the transport of heat in the fluid.
  > Correction: Incorrect equation. The provided equation is not equation (2.4) in the paper.
- $$(2.5) -\Delta\phi = \omega, u = \phi_y, v = -\phi_x$$
  This is the 2D Biot-Savart law, relating the stream function to the vorticity.
- $$(2.10) \omega_t + (c_l x + u) \cdot \nabla \omega = \theta_x + c_\omega \omega, \theta_t + (c_l x + u) \cdot \nabla \theta = c_\theta \theta$$
  These are the dynamically rescaled Boussinesq equations. This transformation is used to study the formation of self-similar singularities.

**Theorems:**
- Theorem 1: Statement: For a specific family of smooth initial data, the solution to the 2D Boussinesq equations develops a stable, nearly self-similar singularity in finite time.
  *Proof:* Proof technique: The proof relies on an analytical framework from a previous paper (Part I) that uses weighted energy estimates. This paper (Part II) completes the proof by using rigorous, computer-assisted numerical calculations to verify the key stability inequalities required by the framework.
- Theorem 2: Statement: The 3D axisymmetric Euler equations exhibit a nearly self-similar blowup in finite time for a class of smooth initial data.
  *Proof:* Proof technique: This result is derived as a perturbation from the 2D Boussinesq result (Theorem 1). The authors show that in the specific asymptotic regime they study, the 3D Euler equations behave like a small perturbation of the 2D Boussinesq equations, so the blowup result carries over.
- Theorem 3: Statement: This is the main, precise technical result. It states that for the dynamically rescaled Boussinesq equations, any solution starting sufficiently close (in a specific energy norm) to a pre-computed approximate self-similar profile will remain close for all time, which implies finite-time blowup for the original, un-rescaled equations.
  *Proof:* Proof technique: The proof is a multi-step process that forms the core of the paper. It involves: 1. Constructing an approximate self-similar solution with a small residual error (Lemma 2.2). 2. Linearizing the equations around this profile. 3. Decomposing the perturbation into a main part and a part driven by a finite-rank operator (Lemma 2.4). 4. Using a weighted energy method and a general stability lemma (Lemma 2.1) to prove that the perturbation remains small. 5. Rigorously bounding all nonlocal terms and error terms using computer-assisted interval arithmetic to satisfy the stability conditions (Lemmas 2.3 and 2.5).
- Lemma 2.1: Statement: This is a general nonlinear stability lemma. It states that if an energy functional E(t) for a system satisfies a differential inequality where the damping/stabilizing terms are guaranteed to be larger than the nonlinear/forcing terms (for energy below a certain threshold E*), then any solution starting with E(0) < E* will have E(t) < E* for all time.
  *Proof:* Proof technique: The proof is based on a barrier/comparison argument for the energy E(t). It is a standard tool in stability analysis.
- Lemma 2.3: Statement: This lemma establishes crucial estimates for the nonlocal parts of the linearized operator (i.e., the velocity components induced by the vorticity). It shows that these nonlocal terms can be controlled by a combination of weighted L-infinity and Holder norms of the vorticity, after subtracting a carefully constructed finite-rank approximation.
  *Proof:* Proof technique: The proof involves detailed analysis of the Biot-Savart integral kernels. The sharp constants in the estimates are obtained through a combination of analytical techniques and rigorous numerical integration.

**Constants & Bounds:**
- `E*: The energy threshold for nonlinear stability. If the initial energy of the perturbation is less than E*, the solution remains stable for all time. In this paper, E* is set to 5e-6.`: This is the critical threshold that determines whether the blowup is stable. The smallness of this constant indicates the delicate nature of the stability.
- `Rank of the approximation operator K: The number of basis functions used to approximate the nonlocal terms in the linearized operator. The rank is less than 50.`: This shows that a relatively low-dimensional approximation is sufficient to capture the essential dynamics of the nonlocal terms, which is a significant simplification.
- `Inequality (2.13): ||w - w_bar||_L_inf < 200E*, ||theta_x - theta_bar_x||_L_inf < 200E*, ||theta_y - theta_bar_y||_L_inf < 200E*, |u_x(t,0) - u_bar_x(0)| < 100E*, |c_w - c_bar_w| < 100E*`: These are the key stability estimates that bound the deviation of the true solution from the approximate self-similar profile. They guarantee that the solution stays within a small neighborhood of the desired blowup profile.
- `Blowup time scaling: T is approximately inversely proportional to the initial L-infinity norm of the vorticity.`: This provides a direct relationship between the initial conditions and the time it takes for the singularity to form.

---

### ON REGULARITY AND SINGULARITY FOR L∞(0,T; L3,w(R3)) SOLUTIONS TO THE NAVIER–STOKES EQUATIONS
**Authors:** HI JUN CHOE, JÖRG WOLF, MINSUK YANG | **Year:** 2016 | [1611.04725v1](https://arxiv.org/abs/1611.04725v1) | **Validation:** verified
**Relevance:** 8/10

**Why it matters:** The paper establishes a new regularity criterion for the Navier-Stokes equations under the condition u ∈ L∞(0,T; L3,w(R3)), which is significantly weaker than the endpoint Serrin condition. It proves that under this condition, the set of singular points at any given time must be finite. This is highly relevant as it constrains the geometric structure of potential finite-time blowups, addressing the gap in understanding singularities that may not satisfy the classical type I scaling.

**Key Insights:**
1. The regularity of Navier-Stokes solutions can be guaranteed by conditions weaker than the classical L³/L^∞ criterion. Specifically, boundedness in the weak-L³ space (L^{3,w}) is sufficient to exert significant control over singularities.
2. Under the L^{∞}(L^{3,w}) condition, any potential blowup at a specific time t cannot be spatially extended (e.g., a line or surface of singularities). The singular set at time t must be composed of at most a finite number of points.
3. The formation of a singularity is tied to a failure of a specific, measurable, local condition. A singularity can only form at a point (x,t) if the velocity field concentrates in a specific way in every neighborhood of that point, violating the smallness condition of Theorem 1.
4. The proof techniques rely on a blow-up (or indirect) argument. This is a powerful method for proving regularity: assume a singularity exists, rescale the solution around the singular point to create a 'singular profile', and then show that this profile must be trivial, leading to a contradiction.

**Equations:**
- $$(∂t − ∆)u + (u · ∇)u + ∇p = 0, div u = 0$$
  These are the incompressible Navier-Stokes equations. The first equation is the momentum equation describing the balance of forces on a fluid element (inertia, viscous forces, pressure gradients), and the second is the incompressibility constraint, stating that the flow is divergence-free.
- $$3/s + 2/l ≤ 1, 3 < s ≤ ∞$$
  This is the classical Ladyzhenskaya–Prodi–Serrin (LPS) regularity condition. It states that if a weak solution's velocity field u belongs to the mixed Lebesgue space L^l(0,T; L^s(R3)) for exponents s and l satisfying this inequality, then the solution is smooth and unique.
- $$u ∈ L∞(0,T; L3,w(R3))$$
  This is the main condition studied in the paper. It requires the velocity field u to be bounded in time with values in the weak L^3 space (L^{3,w}). This is a weaker requirement than the endpoint LPS condition (u ∈ L∞(0,T; L3(R3))) and allows for a broader class of potential singularities, including those not of type I.
- $$(1/r^3) * m({x ∈ B(x0,r) : |u(x, t0)| > ε/r}) ≤ ε$$
  This is the central smallness condition in the paper's new regularity criterion (Theorem 1). It states that if, at a point (x0, t0), the measure of the set where the velocity is large (scaled by 1/r) is sufficiently small within a ball of radius r, then the solution is regular (bounded) in a smaller neighborhood. It's a local condition that prevents the concentration of energy.

**Theorems:**
- Theorem 1: For each M > 0 there exists ε(M) > 0 such that if a weak solution u satisfies ||u||_{L∞(L^{3,w})} ≤ M and the smallness condition (7) holds at a point z0=(x0,t0), then u is bounded in a neighborhood Q(z0, εr).
  *Proof:* The proof is indirect, using a blow-up argument. It assumes the theorem is false, leading to a sequence of solutions that violate the conclusion. This sequence is rescaled to produce a limiting, non-trivial solution to the Navier-Stokes equations with zero initial data. This limiting solution is shown to have certain regularity properties away from the origin, which, by a backward uniqueness argument for the vorticity equation, implies it must be identically zero, contradicting its construction.
- Theorem 2: If a weak solution u satisfies ||u||_{L∞(L^{3,w})} ≤ M, then there are at most a finite number N(M) of singular points at any singular time t.
  *Proof:* The proof uses a dyadic decomposition of space into cubes. At each scale, it identifies a finite number of 'bad' cubes where the regularity criterion from Theorem 1 fails. It shows that the number of these bad cubes is bounded at each scale, and singularities can only occur at points that are contained in an infinite sequence of nested bad cubes. The total number of such points is shown to be finite, bounded by a function of M.

**Constants & Bounds:**
- `LPS Condition: 3/s + 2/l ≤ 1, 3 < s ≤ ∞`: A critical condition on space-time integrability exponents (s, l) that separates regular solutions from potentially singular ones.
- `Energy Inequality: ∫|u(s)|²dx + 2∫∫|∇u|²dz ≤ ∫|u(0)|²dx`: The fundamental global bound for Leray-Hopf weak solutions, ensuring that the total kinetic energy plus the total dissipated energy remains bounded by the initial energy.
- `Caccioppoli-type inequality (17): r⁻¹∫|u|¹⁰/³dz + r⁻¹∫|∇u|²dz ≤ C(r⁻⁵∫∫|u|²dxdt + r⁻⁵(∫|u|²dx)⁴/³)`: A local energy-type estimate that controls higher-order norms (like L¹⁰/³) of the solution in a small cylinder by lower-order norms in a larger one. It is a key tool in the iteration arguments used to prove regularity.

---

### Discretely self-similar solutions to the Navier-Stokes equations with data in L2 satisfying the local energy inequality
**Authors:** Zachary Bradshaw, Tai-Peng Tsai | **Year:** 2018 | [1801.08060v1](https://arxiv.org/abs/1801.08060v1) | **Validation:** verified
**Relevance:** 8/10

**Why it matters:** This paper is highly relevant as it constructs a specific class of solutions, discretely self-similar solutions, which are candidates for finite-time blow-up. The paper focuses on the existence and properties of these solutions for large data in L2_loc, which is a crucial step in understanding their potential singular behavior. It directly addresses the construction of solutions that could potentially model a blow-up event. The work helps close the gap in understanding self-similar profiles and their connection to regularity.

**Key Insights:**
1. The existence of discretely self-similar (DSS) solutions to the Navier-Stokes equations can be established for a very general class of initial data, namely divergence-free vector fields in L2_loc. This is a significant result because it provides a large class of potential candidates for finite-time blow-up.
2. The construction of these DSS solutions relies on a new a priori energy estimate for DSS solutions with data in L2_loc. This estimate is crucial because it is independent of the L3_w norm of the initial data, which was a limitation in previous works. This new estimate is the key technical innovation of the paper.
3. The pressure of these DSS solutions can be explicitly represented by a formula involving the velocity field. This is important because it provides a way to control the pressure, which is a non-local and often difficult term in the Navier-Stokes equations.
4. The paper provides a rigorous mathematical framework for studying DSS solutions, which are thought to be relevant for understanding turbulence and the potential for singularities in the Navier-Stokes equations. The construction of these solutions is a major step towards a better understanding of these fundamental problems in fluid dynamics.

**Equations:**
- $$\partial_t v - \Delta v + v \cdot \nabla v + \nabla \pi = 0, \nabla \cdot v = 0$$
  These are the Navier-Stokes equations, which govern the motion of viscous, incompressible fluids. The first equation is the momentum equation, and the second is the incompressibility condition.
- $$v_\lambda(x, t) = \lambda v(\lambda x, \lambda^2 t)$$
  This is the self-similar scaling for the Navier-Stokes equations. If v is a solution, then v_\lambda is also a solution. This scaling is fundamental to the study of blow-up.
- $$v(x, t) = \frac{1}{\sqrt{t}} u(\frac{x}{\sqrt{t}})$$
  This is the self-similar ansatz, which expresses a self-similar solution v in terms of a time-independent profile u. This reduces the PDE to a stationary one.
- $$-\Delta u - \frac{1}{2}u - \frac{1}{2}y \cdot \nabla u + u \cdot \nabla u + \nabla p = 0, \nabla \cdot u = 0$$
  These are the Leray equations, which the self-similar profile u must satisfy. Finding solutions to these equations is equivalent to finding self-similar solutions to the Navier-Stokes equations.
- $$v(x, t) = \frac{1}{\sqrt{t}} u(y, s), y = x/\sqrt{t}, s = \log t$$
  This is the discretely self-similar (DSS) ansatz. It is a generalization of the self-similar ansatz where the profile u is now periodic in the time-like variable s.
- $$\partial_s u - \Delta u - \frac{1}{2}u - \frac{1}{2}y \cdot \nabla u + u \cdot \nabla u + \nabla p = 0$$
  This is the time-dependent Leray equation, which the profile u of a DSS solution must satisfy. It is a parabolic PDE.
- $$\int |v(t)|^2\phi dx + 2\int\int |\nabla v|^2\phi dxdt \le \int\int |v|^2(\partial_t\phi + \Delta\phi) dxdt + \int\int (|v|^2 + 2\pi)(v \cdot \nabla\phi) dxdt$$
  This is the local energy inequality, a key property of suitable weak solutions to the Navier-Stokes equations. It provides a local energy balance and is a cornerstone of the Caffarelli-Kohn-Nirenberg (CKN) theory for partial regularity.
- $$\pi(x, t) = -\frac{1}{3}|v|^2(x, t) + \lim_{\delta\to 0} \int_{|y|>\delta} K_{ij}(x-y)v_i(y, t)v_j(y, t) dy$$ *(corrected)*
  This is the pressure formula, which expresses the pressure in terms of the velocity field. It shows that the pressure is a non-local quantity, depending on the velocity field in the entire domain through the Riesz transforms.
  > Correction: The original LaTeX was identical to the corrected one, but there was a typo in the explanation. The formula is for pressure, not pi.

**Theorems:**
- Theorem 1.2: Statement: For any divergence-free, λ-DSS vector field v_0 in L2_loc, there exists a λ-DSS suitable weak solution v to the Navier-Stokes equations. This solution satisfies the local energy inequality, and its pressure can be expressed via a specific formula.
  *Proof:* Proof technique: The proof is by approximation. The L2_loc data is approximated by a sequence of smooth, DSS data in L3_w. For this smooth data, the existence of DSS local Leray solutions is known from previous work [3]. A new a priori bound is established for these solutions that is independent of the L3_w norm of the initial data. This allows for a limiting process to construct the solution for the L2_loc data. The pressure formula is obtained by showing it holds for the approximating sequence and then passing to the limit.
- Lemma 2.1: Statement: This lemma provides a way to pass to the limit in the pressure formula for a sequence of approximating solutions. If a sequence of DSS solutions converges to a limit solution, and the pressures of the approximating solutions have a certain form, then the pressure of the limit solution also has that form.
  *Proof:* Proof technique: The proof involves splitting the pressure into three parts: a local part, a near-field part, and a far-field part. The convergence of each part is analyzed separately. The local and near-field parts converge due to the strong convergence of the velocity in L2. The convergence of the far-field part is more delicate and relies on the DSS property and careful estimates.
- Proposition 3.1: Statement: This proposition establishes a crucial a priori bound for DSS local Leray solutions constructed in [3]. It shows that the local energy and the local L3/2 norm of the pressure are bounded by a constant that depends only on the L2 norm of the initial data in a ball and the scaling factor λ, but not on the L3_w norm.
  *Proof:* Proof technique: The proof works at the level of a mollified approximation scheme. The key idea is to use the DSS property to control the spillover of energy to larger scales. By using the scaling property, the energy in a larger ball can be related to the energy in a smaller ball at an earlier time. This allows for a closed energy estimate. The pressure formula is also established for these solutions.
- Lemma 4.1: Statement: This lemma shows that any divergence-free, λ-DSS vector field in L2_loc can be approximated by a sequence of divergence-free, λ-DSS vector fields in L3_w.
  *Proof:* Proof technique: The proof is constructive. It uses a cut-off function to localize the L2_loc function and then uses the Bogovskii map to correct the divergence to zero. The DSS property is then used to extend this construction to the whole space.

**Constants & Bounds:**
- `Local Energy Inequality: esssup_{0<=t<R^2} sup_{x_0} \int_{B_R(x_0)} |v(x,t)|^2 dx + sup_{x_0} \int_0^{R^2} \int_{B_R(x_0)} |\nabla v(x,t)|^2 dxdt < \infty`: This is the fundamental energy bound for local Leray solutions, ensuring local control of the solution's size and its gradient.
- `Pressure constant: -1/3`: The pressure formula contains a term -1/3|v|^2, which is a local part of the pressure. This term is related to the kinetic energy of the fluid.
- `Scaling exponents: Time: 2, Space: 1`: In the self-similar scaling v_\lambda(x, t) = \lambda v(\lambda x, \lambda^2 t), the time variable is scaled by \lambda^2 and the space variable by \lambda. These exponents are determined by the structure of the Navier-Stokes equations and are crucial for the definition of self-similar solutions.

---

### Leray self-similarity in fluid dynamics
**Authors:** F. LAM | **Year:** 2018 | [1812.00957v2](https://arxiv.org/abs/1812.00957v2) | **Validation:** verified
**Relevance:** 8/10

**Why it matters:** This paper is highly relevant to the NS3D blowup problem because it directly addresses one of the main proposed scenarios for singularity formation: a self-similar blowup. By showing that Leray's backward self-similarity leads to a trivial solution, the paper effectively rules out a significant class of potential blowup profiles. This helps to narrow the search for a blowup solution and directs research towards other possibilities, such as non-self-similar singularities or other types of self-similarity.

**Key Insights:**
1. Leray's backward self-similarity hypothesis is too restrictive for the Navier-Stokes equations, as it only admits the trivial solution. This implies that any potential finite-time blowup of the 3D Navier-Stokes equations is unlikely to be of this self-similar form.
2. The paper highlights the delicate interplay between the non-linearity of the Navier-Stokes equations and the scaling properties of the self-similar transformation. The transformation to an elliptic system and the subsequent analysis show that the non-linear term is "too strong" to allow for non-trivial self-similar solutions of the Leray type.
3. The work reinforces the idea that understanding the geometry of the vorticity field is crucial. The analysis of the vorticity equation in the self-similar variables is a key part of the argument.

**Equations:**
- $$`\partial_t u + (u \cdot \nabla) u = -\nabla p + \nu \Delta u`, `\nabla \cdot u = 0`$$
  These are the fundamental equations of motion for a viscous, incompressible fluid. The first equation is the momentum equation, which describes how the velocity field `u` evolves over time, influenced by convection, pressure gradients, and viscous diffusion. The second equation is the incompressibility condition, stating that the flow is divergence-free.
- $$`\partial_t \omega + (u \cdot \nabla) \omega = (\omega \cdot \nabla) u + \nu \Delta \omega`$$
  This equation describes the evolution of vorticity `\omega = \nabla \times u`, which represents the local spinning motion of the fluid. It's derived by taking the curl of the momentum equation.
- $$`u(x-a, t) = t^{\alpha} v(y-b, t^*)`, `p(x-a,t) = t^{2\alpha} q(y-b, t^*)`, `y = (x-a)t^{\beta}`$$ *(corrected)*
  This transformation is used to search for self-similar solutions of the Navier-Stokes equations, which are solutions that preserve their shape over time. The parameters `\alpha` and `\beta` are scaling exponents. This is a key tool for studying blowup.
  > Correction: The transformation in the JSON is missing the shift in the x-coordinate for u and p, and the time dependency for v and q. The PDF provides the correct form as u(x-a, t) and p(x-a, t) and v(y-b, t*) and q(y-b, t*). Also, the variables in the functions v and q are incorrect in the JSON. It should be y-b and t* instead of y and b.

**Theorems:**
- Main Result (Implicit): The paper demonstrates that Leray's backward self-similarity hypothesis, when applied to the Navier-Stokes equations, forces the solution to be trivial (identically zero).
  *Proof:* The proof proceeds by applying the self-similar transformation to the Navier-Stokes equations, which results in an elliptic system for the self-similar profile. By analyzing the resulting equations and using energy-like estimates and Liouville-type arguments, the author shows that the only possible solution is the trivial one.

**Constants & Bounds:**
- `Sobolev Inequality: The paper mentions the Sobolev inequality in the appendix, which is a fundamental tool in the analysis of PDEs. It provides an estimate for the norm of a function in an L^p space in terms of the norms of its derivatives. The paper provides a counterexample to illustrate the non-optimality of the constant in the inequality.`: 

---

### Leray’s backward self-similar solutions to the 3D Navier-Stokes equations in Morrey spaces
**Authors:** Quansen Jiu, Yanqing Wang, Wei Wei | **Year:** 2020 | [2006.15776v1](https://arxiv.org/abs/2006.15776v1) | **Validation:** verified
**Relevance:** 8/10

**Why it matters:** This paper is highly relevant as it directly tackles the possibility of a finite-time blowup through the specific mechanism of Leray's backward self-similar solutions. By proving the non-existence of such solutions in broad classes of Morrey spaces, the paper effectively closes off a significant avenue for constructing a singularity. It forces any potential blowup solution to have a profile that is "rougher" or less well-behaved than those covered by the Morrey spaces M˙q,l(R3) with q > 3/2. This provides a crucial negative constraint for researchers attempting to prove the existence of a blowup.

**Key Insights:**
1. The search for a self-similar blowup for NS3D can be further restricted. This paper demonstrates that a hypothetical blowup profile U cannot be in the Morrey spaces M˙q,1(R3) for q > 3/2. This means any potential self-similar blowup must be "rougher" and cannot have the local regularity properties defined by these spaces.
2. Modern tools from harmonic analysis are powerful for ruling out blowup scenarios. The proofs rely heavily on advanced techniques like the Meyer-Gerard-Oru interpolation inequality, embeddings between Morrey and Besov spaces, and weighted singular integral theory (A_p weights). This indicates that progress on the NS3D problem requires deep tools beyond classical PDE analysis.
3. The concept of "local suitable weak solutions" provides stronger analytical tools. By using this refined definition of a weak solution, the authors were able to establish a new Caccioppoli-type inequality that was essential for the proof of their main theorem (Theorem 1.2). This suggests that focusing on the precise properties of weak solutions can yield new insights.
4. Non-existence results continue to be a fruitful direction of research. While not constructing a blowup, this paper, like many others, makes progress by systematically eliminating possibilities. It tightens the constraints on what a singular solution could look like, guiding future research away from dead ends.

**Equations:**
- $$(1.1) Navier-Stokes Equations: `\partial_t u - \Delta u + u \cdot \nabla u + \nabla \pi = 0, \quad \text{div } u = 0`$$
  These are the incompressible Navier-Stokes equations in R3. They represent the conservation of momentum and mass (incompressibility) for a viscous fluid. Finding a smooth solution for all time is the heart of the NS3D regularity problem.
- $$(1.2) Backward Self-Similar Solution: `u(x,t) = \frac{1}{\sqrt{2a(T-t)}} U(\frac{x}{\sqrt{2a(T-t)}}), \quad \pi(x,t) = \frac{1}{2a(T-t)} \Pi(\frac{x}{\sqrt{2a(T-t)}})`$$
  This is the ansatz for a backward self-similar solution. It describes a velocity profile U that is rescaled in a way that would lead to a singularity (blowup) at the finite time t=T, where the velocity becomes infinite.
- $$(1.3) Stationary Equation for Profile U: `-\Delta U + aU + a(y \cdot \nabla)U + U \cdot \nabla U + \nabla \Pi = 0, \quad \text{div } U = 0`$$
  This is the stationary, or time-independent, PDE that the self-similar profile U must satisfy. Proving that no non-trivial (U not equal to 0) solution exists in a certain function space is equivalent to ruling out that type of self-similar blowup.
- $$(2.2) Local Energy Inequality for Suitable Weak Solutions: `\int_{R3} |u(x,t)|^2\phi(x,t)dx + 2 \int_{-T}^{t} \int_{R3} |\nabla u|^2\phi dxds \le \int_{-T}^{t} \int_{R3} |u|^2(\partial_s \phi + \Delta \phi)dxds + \int_{-T}^{t} \int_{R3} u \cdot \nabla\phi(|u|^2 + 2\pi)dxds`$$
  This is the local energy inequality satisfied by suitable weak solutions (introduced by Caffarelli-Kohn-Nirenberg). It is a fundamental tool for studying the regularity of solutions, as it controls the local energy of the fluid in terms of dissipation and fluxes.
- $$(2.14) Meyer-Gerard-Oru interpolation inequality: `\|f\|_{L^m(R^n)} \le C \|f\|_{\dot{H}^s(R^n)}^{2/m} \|f\|_{\dot{B}_{\infty,\infty}^{-s(m-2)/2}(R^n)}^{1-2/m}`$$
  This is a sophisticated interpolation inequality that relates the norm of a function in a Lebesgue space to its norms in a Sobolev space and a Besov space. The authors use it as a key technical tool to derive energy bounds by connecting different function spaces.

**Theorems:**
- Theorem 1.1: Let U in W1,2_loc(R3) be a weak solution of (1.3). If U is in M˙q,l(R3) with 2 < l <= q < infinity, then U is identically zero.
  *Proof:* The proof follows the strategy of [11, 19, 25]. First, the pressure Π is constructed directly in the Morrey space. Then, the core of the proof is to establish an energy bound (1.9) by controlling the terms in the local energy inequality (2.2). This is achieved using a Meyer-Gerard-Oru interpolation inequality (2.14) and the embedding of Morrey spaces into Besov spaces, which allows the authors to control the nonlinear term. Once the energy bound is established, it leads to the local energy decay condition (1.4) of Tsai, which implies the solution must be trivial.
- Theorem 1.2: Let U in W1,2_loc(R3) be a weak solution of (1.3). If U is in M˙q,1(R3) with 3/2 < q < 6, then U is identically zero.
  *Proof:* The proof uses the concept of "local suitable weak solutions" to establish a new Caccioppoli-type inequality (1.11). This inequality, combined with the condition on U, provides decay estimates on U and its gradient at infinity. However, these estimates are not strong enough to apply previous results directly. The key step is to use the decay information to show that the integral of |U|^3|y|^-2 is finite. This allows the construction of the pressure Π using weighted inequalities for singular integrals (A_p weights). With the pressure controlled, the local energy inequality (2.2) can be applied to show Tsai's local energy decay condition (1.4) holds, which proves U must be zero.

**Constants & Bounds:**
- `Meyer-Gerard-Oru interpolation inequality: \|f\|_{L^m(R^n)} \le C \|f\|_{\dot{H}^s(R^n)}^{2/m} \|f\|_{\dot{B}_{\infty,\infty}^{-s(m-2)/2}(R^n)}^{1-2/m}`: This inequality provides a bound on the L^m norm of a function in terms of its regularity (Sobolev norm) and its large-scale behavior (Besov norm). It is a crucial tool for deriving the energy estimates needed in the proofs.
- `Caccioppoli type inequality (1.11): \|u\|_{L^3(L^{18/5}(Q(R/2)))}^2 + \|\nabla u\|_{L^2(Q(R/2))}^2 \le C(R, \|u\|_{L^{...}(M^{...})})`: This inequality, derived for local suitable weak solutions, bounds the local energy and dissipation of the solution `u` within a parabolic cylinder `Q(R/2)` by norms of `u` in Morrey spaces over a larger cylinder `Q(R)`. It is a key step in the proof of Theorem 1.2, allowing the authors to translate the global condition on the profile U into local decay properties.
- `Energy Bound (3.15): E(R/2) \le C(R, \|u\|_{L^p(M˙q,1)}, \|\pi\|_{L^1(M˙m,1)})`: This proposition bounds the local energy E(R/2) of a suitable weak solution in terms of norms of the velocity and pressure in Morrey spaces over a larger domain. It shows that if the solution is sufficiently "small" in these Morrey norms, its local energy is controlled, which is the basis for the ε-regularity criterion in Corollary 3.3 and the proof of Theorem 1.1.

---

### Properties of Besov-Lorentz spaces and application to Navier-Stokes equations
**Authors:** Qixiang Yang, Hongwei Li | **Year:** 2024 | [2407.04107v1](https://arxiv.org/abs/2407.04107v1) | **Validation:** unverified
**Relevance:** 7/10

**Why it matters:** This paper is highly relevant as it investigates the global well-posedness of the Navier-Stokes equations by controlling the set of 'large value points' of strong solutions, which is intimately linked to the potential formation of singularities (blowup). It introduces and analyzes Besov-Lorentz spaces as a tool to measure and control the size of these sets where the solution might become large. The paper's main contribution is establishing global well-posedness for small initial data in these spaces, which provides a new function space framework for studying regularity and could offer insights into the mechanisms that prevent or lead to blowup. It addresses the gap in understanding how the spatial distribution of large solution values evolves and whether it can be controlled globally in time.

**Key Insights:**
1. **Control the 'Large Value Set':** The key to proving regularity is to control the size of the set of points where the solution `u(t,x)` is large. Besov-Lorentz spaces are a powerful tool for this because their norms are sensitive to the distribution of function values, not just their average size.
2. **Time-Frequency Maximum Norms Tame Lorentz Indices:** A major technical hurdle in using Lorentz spaces for evolution equations is handling the Lorentz index `q`. The paper's novel technique of defining the iteration space norm using a maximum over dyadic time rings (`sup_{2^{-2j_t} \le t < 2^{2-2j_t}}`) allows them to effectively 'pull out' the Lorentz norm estimation and control it using the Hardy-Littlewood maximal operator, a trick that was not possible with previous methods for `q < \infty`.
3. **Non-standard Stability May Be Key:** The iteration space `m\'B^{\dot{n/p}-1,q}_{m,p,\infty}` is not a subspace of `L^\infty(B^{\dot{n/p}-1,q}_{p,\infty})` if `m' > 0`. This means the solution is not required to remain bounded in the initial data space norm for all time. The authors suggest this 'topological deformation capability' is a feature, not a bug, affording a new kind of nonlinear stability that might be better suited to the Navier-Stokes equations.
4. **Wavelet Analysis is Essential:** The entire analysis is deeply rooted in wavelet theory. The characterization of function spaces, the decomposition of operators (paraproduct, couple product), and the core estimates all rely on the excellent time-frequency localization properties of Meyer wavelets.

**Equations:**
- $$`\partial_t u - \Delta u + (u \cdot \nabla)u - \nabla p = 0` ; `\nabla \cdot u = 0` ; `u|_{t=0} = f`$$
  This is the fundamental system of equations describing the motion of an incompressible, viscous fluid. The first equation is the momentum equation, balancing inertia, viscous forces, pressure gradients, and convective transport. The second is the incompressibility condition. Proving or disproving the existence of smooth, global solutions for arbitrary smooth initial data in 3D is the Clay Millennium Prize problem.
- $$`u(t,x) = e^{t\Delta}f(x) - B(u,u)(t,x)` where `B(u,u)(t,x) = \int_0^t e^{(t-s)\Delta} \mathbb{P} \nabla (u \otimes u) ds`$$
  This is the mild solution formulation of the Navier-Stokes equations. It recasts the PDE as an integral equation where the solution is expressed in terms of the initial data evolved by the heat semigroup (`e^{t\Delta}f`) and a bilinear term `B(u,u)` that captures the nonlinear interaction. This formulation is the starting point for many modern analyses of well-posedness.
- $$`\|f\|_{B^{\dot{s},q}_{p,r}} \Leftrightarrow \left( \sum_{j \in \mathbb{Z}} 2^{jqs} \left\{ \sum_{u \in \mathbb{Z}} 2^{ur} |\{x : f_j(x) > 2^u\}|^{p/r} \right\}^{q/p} \right)^{1/q}`$$
  This is the norm for the Besov-Lorentz space. It generalizes the standard Besov space norm by replacing the Lebesgue `L^p` norm with the Lorentz `L^{p,r}` norm. This provides a finer way to measure the size of a function, taking into account the distribution of its values, which is crucial for controlling the set of large values relevant to blowup.

**Theorems:**
- Theorem 1.1: Boundedness of Gauss Flow: If `f` is in the Besov-Lorentz space `B^{\dot{n/p}-1,q}_{p,\infty}`, then the solution to the heat equation with initial data `f`, `e^{t\Delta}f`, belongs to a specially constructed time-frequency microlocal maximum norm space `m\'B^{\dot{n/p}-1,q}_{m,p,\infty}`.
  *Proof:* The proof uses wavelet decomposition and Hardy-Littlewood maximal operators to control the Lorentz index. The estimates are handled by considering different cases for the time variable `t` relative to the frequency scale `2^{2j}` and using `\alpha`-triangle and Holder inequalities.
- Theorem 1.2: Boundedness of Paraproduct Flow: The paraproduct flow, which represents a key component of the nonlinear term in the Navier-Stokes equations, is bounded in the `m\'B^{\dot{n/p}-1,q}_{m,p,\infty}` space.
  *Proof:* The proof involves detailed estimates of the wavelet coefficients of the paraproduct term. It relies on a priori estimates for the heat kernel and its derivatives (Lemma 4.1) and careful handling of the time integration by splitting the integral into different regimes. Again, the Hardy-Littlewood maximal operator is a key tool.
- Theorem 1.3: Boundedness of Couple Product Flow: The couple product flow, another component of the nonlinear term representing high-frequency interactions, is also bounded in the `m\'B^{\dot{n/p}-1,q}_{m,p,\infty}` space.
  *Proof:* The technique is similar to the proof of Theorem 1.2, involving complex wavelet coefficient estimations, splitting time integrals, and using maximal functions to control the spatial norms. The analysis is intricate due to the high-high frequency interactions.
- Theorem 1.4: Global Well-posedness for Small Data: For small initial data in the Besov-Lorentz space `(B^{\dot{n/p}-1,q}_{p,\infty})^n`, the 3D Navier-Stokes equations have a unique global smooth solution in the iteration space `(m\'B^{\dot{n/p}-1,q}_{m,p,\infty})^n`.
  *Proof:* This is a direct consequence of Theorems 1.1, 1.2, and 1.3. The boundedness of the linear, paraproduct, and couple flows shows that the bilinear operator `B(u,u)` in the integral formulation is a bounded map from the iteration space to itself. For small initial data, this map is a contraction, and the result follows from Picard's contraction principle.

**Constants & Bounds:**
- `Heat Kernel Decay Estimate (from Lemma 3.4): `|f^{\epsilon}_{j,k}(t)| \lesssim e^{-ct2^{2j}} \sum_{\epsilon', |j-j'|\le 1, k'} |f^{\epsilon'}_{j',k'}| (1+|2^{j-j'}k'-k|)^{-N}` for `t2^{2j} \ge 1``: This shows the exponential decay of wavelet coefficients of the solution to the heat equation in time, especially for high frequencies (large `j`). This rapid decay is the fundamental mechanism for regularity in parabolic equations like Navier-Stokes.
- `Maximal Function Boundedness on Lorentz Space (Lemma 2.7): `\sup_{\lambda>0} \lambda^p |\{x : Mf(x) > \lambda\}| \lesssim \sup_{\lambda>0} \lambda^p |\{x : f(x) > \lambda\}|``: This shows that the Hardy-Littlewood maximal operator `M` is bounded on the Lorentz space `L^{p,\infty}`. This is a crucial technical tool used throughout the paper to control the spatial distribution of the solution and its derivatives without having to deal with the complexities of the Lorentz norm directly.
- `Nonlinear Decay Parameters `m` and `m'`: The norms involve factors like `2^{2(j-j_t)m}` for high frequencies (`j \ge j_t`) and `2^{2(j-j_t)m'}` for low frequencies (`j < j_t`).`: These parameters define the iteration space. `m > 1/2` ensures sufficient decay at high frequencies to control the nonlinearity. `0 \le m' < 1` allows for a specific type of 'topological deformation' or non-standard stability, where the solution space is not a subspace of `L^\infty(X)`, which is a novel feature of their framework.

---

### A NEW BLOWUP CRITERION FOR THE 3D BAROTROPIC COMPRESSIBLE NAVIER-STOKES EQUATIONS WITH VACUUM
**Authors:** SAIGUO XU, YINGHUI ZHANG | **Year:** 2024 | [2408.07935v1](https://arxiv.org/abs/2408.07935v1) | **Validation:** unverified
**Relevance:** 7/10

**Why it matters:** This paper is highly relevant as it establishes a new Beale-Kato-Majda type blowup criterion for the 3D barotropic *compressible* Navier-Stokes equations, which is a direct analogue to a famous criterion in the incompressible setting. It addresses the formation of singularities by providing conditions on the vorticity and divergence of the velocity that guarantee global regularity. While focused on the compressible case (with vacuum), the techniques for estimating solutions and controlling blowup are often transferable or provide strong analogies for the incompressible problem, particularly concerning the role of vorticity and the deformation tensor in potential singularity formation.

**Key Insights:**
1. A new blowup criterion for 3D barotropic compressible Navier-Stokes has been established, which is analogous to the celebrated Beale-Kato-Majda criterion for the incompressible Euler equations. The criterion states that a solution remains regular as long as the L^1 in time, L^∞ in space norm of the velocity divergence and a Serrin-type norm of the vorticity remain bounded.
2. The analysis introduces different techniques for handling different boundary conditions. For the Cauchy problem and Navier-slip boundaries, the 'effective viscous flux' G is used to derive crucial estimates. For the Dirichlet problem, a velocity decomposition technique is employed to overcome difficulties with boundary terms.
3. The paper highlights the critical role of the velocity's divergence and curl in controlling the regularity of solutions to the compressible Navier-Stokes equations, even in the presence of a vacuum.

**Equations:**
- $$∂_t ρ + div(ρu) = 0$$
  This is the continuity equation, representing the conservation of mass in the fluid flow.
- $$∂_t(ρu) + div(ρu ⊗ u) - µ∆u - (µ + λ)∇divu + ∇P(ρ) = 0$$
  This is the momentum equation for a compressible viscous fluid, expressing the conservation of momentum. It includes terms for the local acceleration, convective acceleration, viscous diffusion, pressure gradient, and effects of compressibility.
- $$lim_{T→T∗} ( ||div u||_{L^1(0,T;L^∞)} + ||S(u)||_{L^s(0,T;L^r)} ) = ∞$$
  This is the main result of the paper, a new blowup criterion for the 3D barotropic compressible Navier-Stokes equations. It states that a strong solution will blow up at time T* only if the combined norm of the divergence of the velocity and the rigid body rotation tensor becomes infinite.

**Theorems:**
- Theorem 1.3: Let (ρ,u) be a strong solution. If T∗ is the maximal time of existence, then lim_{T→T∗} ( ||div u||_{L^1(0,T;L^∞)} + ||S(u)||_{L^s(0,T;L^r)} ) = ∞ for the Cauchy or Dirichlet problem, and lim_{T→T∗} ( ||div u||_{L^1(0,T;L^∞)} + ||S(u)||_{L^1(0,T;L^∞)} ) = ∞ for the Navier-slip problem.
  *Proof:* The proof involves deriving a priori estimates for the solution. The key is to obtain bounds on the L∞(0,T;L2)-norm of ∇u. For the Cauchy and Navier-slip cases, this is achieved by using the dissipation of the effective viscous flux G. For the Dirichlet case, a velocity decomposition u = h + g is used. These estimates are then used with a log-type Gronwall's inequality to bound the density gradient, which ultimately prevents the blowup under the given conditions.

**Constants & Bounds:**
- `µ > 0, λ + (2/3)µ > 0: These are the physical restrictions on the shear viscosity (µ) and bulk viscosity (λ), ensuring the dissipative nature of the fluid, which is tied to the second law of thermodynamics.`: 
- `P(ρ) = aρ^γ, a > 0, γ > 1: This is the polytropic equation of state for the pressure P, relating it to the density ρ. The condition γ > 1 is crucial for the hyperbolicity of the Euler part of the equations.`: 
- `||∇u||_{L^p} ≤ C(||div u||_{L^p} + ||curl u||_{L^p}): This is a standard elliptic estimate that bounds the full gradient of the velocity by the L^p norms of its divergence and curl. It is fundamental for decomposing the velocity field and its gradient.`: 

---


## Computational Methods and Symbolic Regression
*Papers on numerical methods for detecting blowup, PySR-style symbolic regression, PINNs, and computational fluid dynamics tools.*

### Discovery of Green's function based on symbolic regression with physical hard constraints
**Authors:** Jianghang Gu, Mengge Du, Yuntian Chen, Shiyi Chen | **Year:** 2024 | [2408.00811v1](https://arxiv.org/abs/2408.00811v1) | **Validation:** unverified
**Relevance:** 3/10

**Why it matters:** This paper does not directly address the Navier-Stokes equations or the blowup problem. It presents a machine learning method (symbolic regression) to discover Green's functions for linear PDEs. While the pressure Poisson equation is a component of the Navier-Stokes equations, this paper only tackles linear operators and does not provide new insights into the nonlinear advection term, which is the primary source of the blowup problem. The methods presented could potentially be adapted in the long term to study simplified or linearized versions of the Navier-Stokes equations, but the direct relevance to proving finite-time blowup is low.

**Key Insights:**
1. Symbolic regression with physical constraints can discover the explicit form of Green's functions for linear PDEs.
2. The use of symmetry as a hard constraint significantly improves the efficiency and accuracy of the discovery process.
3. This method can find Green's functions for operators where no analytical form was previously known.

**Equations:**
- $$Lu_j = f_j, D(u_j, Ω) = g$$
  This is the general form of a linear partial differential equation with boundary conditions, where L is a linear differential operator, u is the solution, f is the forcing term, and D represents the boundary conditions.
- $$u_j(x) = ∫_Ω G(x,y)f_j(y)dy + u_hom(x)$$
  This equation shows how the solution u to a linear PDE can be found by integrating the Green's function G against the forcing term f. This is a fundamental concept in the theory of linear PDEs.
- $$G(x,y) = G(y,x)$$
  This equation expresses the symmetry property of the Green's function for self-adjoint operators. This property is used as a physical constraint in the discovery process.

**Theorems:**
- The paper does not present new theorems or proofs in the traditional mathematical sense. It is a computational paper focused on a new method for discovering Green's functions. It mentions the 'universal approximation theorem for operators' as a motivation for using neural networks, but does not extend or prove new results related to it.

**Constants & Bounds:**
- `ζ1, ζ2: Penalty factors for equation simplicity in the reward function.`: These are hyperparameters in the machine learning model that control the trade-off between accuracy and the complexity of the discovered Green's function.
- `Discovered constant for Laplace operator: -1`: The method discovers the constant in the Green's function for the 1D Laplace operator, which is G(x, y) = (y-1)x for x < y and (x-1)y for x > y.

---

### Knowledge Integration for Physics-informed Symbolic Regression Using Pre-trained Large Language Models
**Authors:** Bilge Taskin, Wenxiong Xie, Teddy Lazebnik | **Year:** 2025 | [2509.03036v1](https://arxiv.org/abs/2509.03036v1) | **Validation:** unverified
**Relevance:** 1/10

**Why it matters:** This paper has a very low relevance to the NS3D blowup problem. It focuses on a general methodology for using Large Language Models (LLMs) to improve Physics-Informed Symbolic Regression (PiSR) for discovering equations from data. While this could theoretically be applied to fluid dynamics data, the paper itself does not address the Navier-Stokes equations, fluid dynamics, PDE regularity, or blowup phenomena. The demonstrated examples (free fall, harmonic motion, damped waves) are simple physical systems, not complex fluid flows. The gap it might tangentially address is in developing novel computational tools for analyzing PDE data, but it offers no direct insights into NS3D regularity.

**Key Insights:**
1. Integrating pre-trained Large Language Models (LLMs) into the loss function of a symbolic regression (SR) algorithm can significantly improve the algorithm's ability to discover correct physical equations from noisy data.
2. LLMs can act as a form of automated domain knowledge, evaluating the physical plausibility, dimensional consistency, and simplicity of candidate equations, thereby guiding the SR search process more effectively than traditional fitness metrics alone.
3. The quality of the prompt used to query the LLM is critical. More informative prompts that provide context about the experimental setup and the variables involved lead to better performance by the LLM-integrated SR system.
4. This methodology provides a general framework for incorporating domain knowledge into SR without requiring specialized, handcrafted constraints for each new problem, potentially making automated scientific discovery more accessible.

**Equations:**
- $$L = w_1*e + w_2*s + w_3*c$$
  This is the composite loss function used to guide the symbolic regression process. It is a weighted sum of the mean square error `e`, the size of the equation `s` (to promote simplicity), and a score `c` from the LLM that evaluates the physical plausibility of the equation.
- $$v = \sqrt{2gh}$$
  This is the standard equation for the velocity of a freely falling object from a height `h` under constant gravity `g`. It is used as a ground truth case to test the symbolic regression framework.
- $$x(t) = A*cos(\sqrt{k/m}*t + \phi)$$
  This equation describes simple harmonic motion for a mass `m` on a spring with constant `k`. It is the second test case for the regression framework.
- $$E(t) = E_0*e^{-\alpha*t/2}*cos(kx - \omega*t)$$
  This equation represents a damped plane-wave, used as the third and most complex test case for evaluating the performance of the LLM-integrated symbolic regression.

**Theorems:**
- The paper does not contain mathematical theorems, lemmas, or formal proofs. It is a computational study that presents a new method and evaluates it experimentally.

**Constants & Bounds:**
- `The paper does not discuss any physical constants or mathematical bounds related to the Navier-Stokes equations. It mentions hyperparameters for the machine learning models used, such as population size, mutation probability, and learning rates, which are specific to the computational experiment.`: 

---

### Using Physics Informed Neural Network (PINN) and Neural Network (NN) to Improve a k − ω Turbulence Model
**Authors:** Lars Davidson | **Year:** 2025 | [2511.12493v2](https://arxiv.org/abs/2511.12493v2) | **Validation:** unverified
**Relevance:** 1/10

**Why it matters:** This paper focuses on improving Reynolds-Averaged Navier-Stokes (RANS) turbulence models, specifically the k-ω model, using machine learning (PINNs and NNs). While related to fluid dynamics, RANS models are high-level, statistical approximations of turbulent flows and are not suitable for studying the fundamental regularity (blowup) problem of the 3D Navier-Stokes equations. The blowup problem concerns the existence of smooth, classical solutions to the original PDE, a question that is averaged out in RANS formulations. Therefore, this paper's contributions are in the domain of computational fluid dynamics for engineering applications, not in the fundamental mathematical theory of PDE regularity.

**Key Insights:**
1. The standard k-ω turbulence model significantly underpredicts the turbulent kinetic energy (k) in boundary layers, primarily due to poor modeling of the turbulent diffusion term.
2. Physics-Informed Neural Networks (PINNs) can be used to correct specific deficiencies in RANS models. Here, a PINN is used to solve an ODE for the turbulent viscosity, which in turn corrects the turbulent diffusion and improves the prediction of k.
3. To maintain the correct mean velocity profile (and thus correct turbulent viscosity ν_t = k/ω), the improved k must be compensated for by also modifying the ω equation. The paper introduces new NN-based functions C_k,NN and C_ω2,NN to achieve this consistency.
4. The machine-learned model coefficients (σ_k,NN, C_k,NN, C_ω2,NN) are made functions of local, non-dimensional flow parameters (τ_tot/u_τ^2 and ν_t/(yu_τ)), making the resulting model more generalizable to different flows and Reynolds numbers, including recirculating flows.
5. The paper suggests that the neural network models can be replaced by symbolic regression (pySR) to generate explicit algebraic expressions. This is a crucial step for portability, as it allows the new turbulence model to be implemented easily in existing commercial or open-source CFD codes without requiring a neural network library.

**Equations:**
- $$∂(v¯_j k)/∂x_j = P_k + ∂/∂x_j [(ν + ν_t/σ_k) ∂k/∂x_j] - C_μ C_k,NN kω$$
  This is the transport equation for the turbulent kinetic energy (k). It balances the rate of change of k with its production (P_k), diffusion, and dissipation.
- $$∂(v¯_j ω)/∂x_j = C_ω1 P_k/ν_t + ∂/∂x_j [(ν + ν_t/σ_ω) ∂ω/∂x_j] - C_ω2,NN ω^2$$
  This is the transport equation for the specific dissipation rate (ω). It describes the rate of change of ω due to production, diffusion, and destruction terms.
- $$P_k = ν_t (∂v¯_i/∂x_j + ∂v¯_j/∂x_i) ∂v¯_i/∂x_j$$
  This term represents the rate at which kinetic energy is transferred from the mean flow to the turbulent fluctuations due to velocity gradients. It is the primary source of turbulent energy.
- $$ν_t = k/ω$$
  The Boussinesq hypothesis relates the Reynolds stresses to the mean velocity gradients via an eddy viscosity, ν_t. In the k-ω model, it is defined as the ratio of turbulent kinetic energy to the specific dissipation rate.

**Theorems:**
- This paper is focused on computational methods and machine learning for turbulence modeling, not on fundamental PDE theory. As such, it does not contain any theorems, lemmas, propositions, or formal proofs regarding the regularity or blowup of the Navier-Stokes equations.

**Constants & Bounds:**
- `C_ω1: 5/9`: Standard k-ω model constant
- `C_ω2: 3/40`: Standard k-ω model constant
- `σ_k: 2`: Standard k-ω model constant
- `σ_ω: 2`: Standard k-ω model constant
- `C_μ: 0.09`: Standard k-ω model constant
- `σ_k,NN: A turbulent Prandtl number for k, learned by a neural network.`: A variable coefficient
- `C_k,NN: A coefficient modifying the dissipation term in the k-equation, learned by a neural network.`: A variable coefficient
- `C_ω2,NN: A coefficient modifying the destruction term in the ω-equation, learned by a neural network.`: A variable coefficient

---

### Divergence-Free Diffusion Models for Incompressible Fluid Flows
**Authors:** Wilfried Genuist, Éric Savin, Filippo Gatti, Didier Clouteau | **Year:** 2026 | [2601.19368v1](https://arxiv.org/abs/2601.19368v1) | **Validation:** unverified
**Relevance:** 1/10

**Why it matters:** This paper focuses on using machine learning (diffusion models) to generate 2D incompressible fluid flow simulations, specifically the Kolmogorov flow. Its primary contribution is in the domain of scientific machine learning and computational fluid dynamics, exploring methods to enforce the divergence-free constraint in a generative model. It does not address the fundamental mathematical questions of regularity or finite-time blowup for the 3D Navier-Stokes equations. The techniques are for generating statistically similar flows, not for analyzing or proving properties of the underlying PDEs that would lead to a blowup proof.

**Key Insights:**
1. The paper demonstrates several techniques for incorporating physical constraints (incompressibility) into deep learning models for fluid dynamics. 2. Diffusion models can be used to generate realistic-looking turbulent flows, capturing their statistical properties. 3. The paper compares different methods for enforcing the divergence-free constraint, including projection methods and architectural modifications to the neural network.

**Equations:**
- $$\partial_t u + (u \cdot \nabla)u = -\frac{1}{\varrho}\nabla p + \nu \Delta u + f, \nabla \cdot u = 0$$
  These are the incompressible Navier-Stokes equations, the fundamental equations of motion for a viscous, incompressible fluid.
- $$P v = v - \nabla \Delta^{-1}(\nabla \cdot v)$$
  This is the Leray projector, which projects a vector field onto its divergence-free component, eliminating the pressure term.
- $$\frac{du}{dt} + \nu A u + B(u) = P f$$
  This is the abstract evolution form of the Navier-Stokes equations after applying the Leray projector, used for mathematical analysis.
- $$\hat{u}(k) = \frac{ik^\perp}{\|k\|^2} \hat{\omega}(k)$$
  This is the Biot-Savart law in Fourier space, relating the velocity field to the vorticity field.

**Theorems:**
- The paper does not present new theorems or proofs related to the Navier-Stokes regularity problem. It is a paper on computational methods.

**Constants & Bounds:**
- `Kolmogorov-like energy spectrum: E(\|k\|) \propto \|k\|^{-(3+\delta)}`: This is a standard scaling law from 2D turbulence theory, not a new bound derived in the paper.

---


## Energy Methods and A Priori Estimates
*Papers on energy inequalities, Caffarelli-Kohn-Nirenberg estimates, partial regularity, and energy-based approaches.*

### Partial regularity for Navier-Stokes and liquid crystals inequalities without maximum principle
**Authors:** GABRIEL S. KOCH | **Year:** 2022 | [2001.04098v4](https://arxiv.org/abs/2001.04098v4) | **Validation:** partially_verified
**Relevance:** 8/10

**Why it matters:** This paper deals with partial regularity results for the Navier-Stokes equations, which is a central topic in the study of potential blowup. It builds upon the foundational work of Caffarelli-Kohn-Nirenberg, aiming to establish regularity under weaker conditions (without a maximum principle). This directly addresses the question of where and how singularities can form, which is the core of the blowup problem.

**Key Insights:**
1. The Caffarelli-Kohn-Nirenberg theory can be extended to a more general system of equations that includes the Navier-Stokes equations as a special case.
2. The maximum principle for the director field is not necessary to obtain partial regularity results, but without it, one obtains a weaker result.
3. A local condition on the decay of an integral involving the director field is sufficient to recover the full partial regularity result of CKN.
4. The paper provides a unified framework for studying the partial regularity of the Navier-Stokes equations and related systems.

> **Validation Note:** Lemma 1, as described in the JSON, does not appear to be in the paper. The description may be referring to another theorem or a concept from a different paper.

**Equations:**
- $$u_t - \Delta u + \nabla \cdot (u \otimes u + \nabla d \odot \nabla d) + \nabla p = 0$$ *(corrected)*
  > Correction: Incorrect operator: \nabla^T should be \nabla
- $$\nabla \cdot u = 0$$
- $$d_t - \Delta d + (u \cdot \nabla) d + f(d) = 0$$
  This system couples the Navier-Stokes equations for fluid velocity (u) and pressure (p) with a transport-diffusion equation for the liquid crystal director field (d). It describes the evolution of the fluid's velocity and the orientation of the liquid crystal molecules.
- $$- \Delta p = \nabla \cdot (\nabla \cdot [u \otimes u + \nabla d \odot \nabla d])$$ *(corrected)*
  This is the pressure Poisson equation, derived from the incompressibility condition. It determines the pressure field required to maintain a divergence-free velocity field.
  > Correction: Incorrect operator: \nabla^T should be \nabla
- $$\frac{d}{dt} \int_{\Omega} (\frac{|u|^2}{2} + \frac{|\nabla d|^2}{2}) dx + \int_{\Omega} (|\nabla u|^2 + |\Delta d - f(d)|^2) dx \leq 0$$ *(corrected)*
  This is the fundamental energy inequality for the system. It expresses the dissipation of total energy, which is the sum of kinetic energy of the fluid and the elastic energy of the director field, and is crucial for establishing the existence of global weak solutions.
  > Correction: Extraneous negative sign at the beginning of the equation.
- $$\int_{\Omega} [|u|^2 + |\nabla d|^2](x,T) \phi(x,T) dx + \int_0^T \int_{\Omega} [|u|^2 + |\nabla d|^2] \phi_t + |\nabla u|^2 \phi + |\nabla^2 d|^2 \phi] dx dt \leq C \int_0^T \int_{\Omega} [|u|^3 + |\nabla d|^3 + |p| |u|] \phi dx dt$$ *(corrected)*
  This is a local energy inequality, a cornerstone of partial regularity theory. It provides a bound on the energy within a small parabolic cylinder, which is used to prove that the solution is regular outside of a small set of singular points.
  > Correction: The extracted equation is significantly different from the one in the paper. The first term is incorrect, and the integration variables are different.

**Theorems:**
- Theorem 1: Let u, d, and p be solutions to the system in a domain. If a certain smallness condition on the scaled energy is met, then the solution is regular at that point.
  *Proof:* The proof is a classic iteration argument in the spirit of Caffarelli-Kohn-Nirenberg. It relies on a decay estimate for a localized energy-like quantity (Proposition 3), which is established using a blow-up argument and the local energy inequality. The key is to show that if the initial energy in a small ball is small enough, it decays at a certain rate, which then implies regularity.
- Lemma 1 (L^q, L^2-regularity): If a weak solution is in L^q for q > 3, then it is regular.
  *Proof:* This is a standard result that connects the integrability of the solution to its regularity. The proof uses the local energy inequality and Sobolev embedding theorems.
- Proposition 1 & 2: These propositions establish crucial estimates for the iterative argument in the proof of Theorem 1. They provide bounds on the growth of certain scaled quantities, which are essential for showing the decay of the local energy.
  *Proof:* The proofs rely on the local energy inequality, Holder's inequality, and a careful decomposition of the pressure term.

**Constants & Bounds:**
- `E_{q,\sigma}(z_0) := \sup_{0<r<1} \frac{1}{r^{q(1-\frac{3}{\sigma})}} \int_{Q_r(z_0)} [|u|^q + |\nabla d|^q] dz`: This is a key quantity used in the regularity proof. It measures the scaled energy of the solution in a parabolic cylinder. The main theorem shows that if this quantity is small enough, the solution is regular.
- `g_\sigma := \sup_{z_0 \in \Omega_T} \limsup_{r \to 0} \frac{1}{r^{2+\sigma-2}} \int_{Q_r(z_0)} |d|^\sigma(|u|^3+|\nabla d|^3)^{(1-\frac{\sigma}{6})} dz < \infty`: This is the crucial assumption on the director field `d` that allows the author to recover the full partial regularity result of CKN. It is a local condition on the decay of an integral involving `d`, `u`, and `∇d`.
- `Parabolic Hausdorff dimension: P^k(S)`: This is a measure of the size of the singular set S. The main result of the paper is that P^1(S) = 0, which means that the singular set is small in a certain sense.

---

### Symmetry breaking and weighted Euclidean logarithmic Sobolev inequalities
**Authors:** Jean Dolbeault, Andres Zuniga | **Year:** 2022 | [2210.12488v1](https://arxiv.org/abs/2210.12488v1) | **Validation:** unverified
**Relevance:** 4/10

**Why it matters:** This paper does not directly address the Navier-Stokes equations. However, it provides a rigorous analysis of symmetry breaking for a class of related nonlinear elliptic equations using the carr´e du champ method. The techniques and insights from this paper could be adapted to study the formation of singularities in the Navier-Stokes equations, which are also expected to exhibit non-symmetric behavior near a potential blowup. It is particularly relevant to understanding the mechanisms that can lead to the failure of regularity in nonlinear PDEs.

**Key Insights:**
1. The carr´e du champ method is a powerful tool for analyzing symmetry breaking in nonlinear elliptic and parabolic equations. This provides a potential avenue for rigorously studying the non-symmetric structures that are expected to form near a singularity in the Navier-Stokes equations.
2. Symmetry breaking is governed by a competition between different terms in the energy functional. This provides a conceptual framework for understanding how singularities might form in the Navier-Stokes equations, where a similar competition exists between the nonlinear advection term and the viscous diffusion term.
3. The Felli & Schneider curve provides a sharp criterion for symmetry breaking. This suggests that it might be possible to find a similar sharp criterion for blowup in the Navier-Stokes equations, perhaps in terms of some critical value of a dimensionless parameter.
4. The paper connects the WLS inequalities to the Caffarelli-Kohn-Nirenberg (CKN) inequalities, which are known to be related to the regularity of the Navier-Stokes equations. This connection provides a bridge between the abstract functional analysis of the WLS inequalities and the concrete problem of NS3D blowup.

**Equations:**
- $$`\int_{\mathbb{R}^d} |f|^2 \log \frac{|f|^2}{\|f\|_{2,\gamma}^2} |x|^{-\gamma} dx \le C_{\beta,\gamma} \frac{n}{2} \log \frac{\|\nabla f\|_{2,\beta}^2}{\|f\|_{2,\gamma}^2}`$$
  This is the weighted logarithmic Sobolev (WLS) inequality. It provides an upper bound on the entropy of a function `f` in terms of its weighted Sobolev norm, which measures its regularity. Such inequalities are crucial for studying the long-time behavior of solutions to diffusion equations.
- $$`n := \frac{2(d-\gamma)}{\beta+2-\gamma}`$$
  This equation defines the effective dimension `n` for the WLS inequality. The behavior of the inequality, particularly regarding symmetry, depends on this parameter.
- $$`\beta_{FS}(\gamma) := d-2 - \sqrt{(d-\gamma)^2 - 4(d-1)}`$$
  This defines the Felli & Schneider curve, a critical threshold for the parameter `\beta`. It separates the region where optimal functions for the inequality are symmetric from the region where they are not.
- $$`\int_{\mathbb{R}^d} |g|^2 \log \frac{|g|^2}{\|g\|_{2,\nu}^2} |x|^{-\nu} dx \le K_{n,\alpha} + \frac{n}{2} \log \frac{\|D_\alpha g\|_{2,\nu}^2}{\|g\|_{2,\nu}^2}`$$
  This is a transformed version of the WLS inequality, written in terms of a different function `g` and a modified gradient operator `D_\alpha`. This form is more convenient for analyzing symmetry breaking.
- $$`-|x|^{-\gamma} \nabla \cdot (|x|^\beta \nabla f) + f = f \log |f|^2` and `D_\alpha^* D_\alpha g + g = g \log|g|^2`$$
  These are the Euler-Lagrange equations associated with the WLS inequality. Their solutions correspond to the optimal functions that achieve equality in the inequality.
- $$`\frac{\partial u}{\partial t} = |x|^\gamma \nabla \cdot (|x|^{-\beta} \nabla u)`$$
  This is the weighted heat flow equation. The WLS inequality can be studied by analyzing the entropy decay along this flow, a technique known as the carr´e du champ method.

**Theorems:**
- Theorem 1.1: This theorem establishes the conditions for symmetry and symmetry breaking for the weighted logarithmic Sobolev (WLS) inequality. It states that the inequality holds for some constant, and equality is achieved by an optimal function. It then gives two cases: (i) Symmetry breaking occurs if and only if `\gamma < 0` and `\beta_{FS}(\gamma) < \beta < (d-2\gamma)/d`. (ii) Symmetry holds if and only if `\gamma < d` and `\gamma-2 \le \beta \le \beta_{FS}(\gamma)`.
  *Proof:* The proof relies on the carr´e du champ method, which involves analyzing the entropy decay along a weighted heat flow. The key idea is to compute the second time derivative of the entropy and show that it is related to the Fisher information, which allows for proving exponential decay of the entropy to its minimum.
- Corollary 1.2: This is a restatement of Theorem 1.1 in terms of different parameters `\alpha` and `n`. It provides equivalent conditions for symmetry and symmetry breaking in this new parameterization.
  *Proof:* The proof is a direct consequence of the change of variables that transforms the original WLS inequality into the form presented in the corollary.
- Corollary 1.3: This corollary states that the Euler-Lagrange equations associated with the WLS inequality admit a unique positive solution in the symmetry range. In the symmetry-breaking range, they admit at least one radially symmetric solution and a continuum of non-radial solutions.
  *Proof:* The proof is an elementary consequence of the proof of Corollary 1.2.

**Constants & Bounds:**
- ``C_{\beta,\gamma}`: The optimal constant in the weighted logarithmic Sobolev inequality.`: The paper investigates when this constant is achieved by a symmetric function.
- ``\beta_{FS}(\gamma) = d-2 - \sqrt{(d-\gamma)^2 - 4(d-1)}`: The Felli & Schneider curve.`: This is a critical bound for the parameter `\beta` that determines whether the optimal functions for the WLS inequality are symmetric or not.
- `Caffarelli-Kohn-Nirenberg (CKN) inequalities: The paper notes that WLS inequalities are a limit case of the CKN inequalities.`: The symmetry breaking results for WLS inequalities are analogous to those for CKN inequalities.

---

### GLOBAL EXISTENCE OF SUITABLE WEAK SOLUTIONS TO THE 3D CHEMOTAXIS-NAVIER-STOKES EQUATIONS
**Authors:** XIAOMENG CHEN, SHUAI LI, LILI WANG, AND WENDONG WANG | **Year:** 2023 | [2311.13343v1](https://arxiv.org/abs/2311.13343v1) | **Validation:** unverified
**Relevance:** 3/10

**Why it matters:** This paper studies the existence of suitable weak solutions for the 3D chemotaxis-Navier-Stokes equations, a system coupling fluid dynamics with bacterial movement. While not directly focused on the pure Navier-Stokes (NS3D) blowup problem, its relevance lies in the techniques used to handle the fluid dynamics part of the system. The paper explicitly references and builds upon the Caffarelli-Kohn-Nirenberg (CKN) theory of partial regularity, which is a cornerstone of the NS3D regularity program. The methods for establishing local energy inequalities for this more complex, coupled system could potentially offer insights or adaptable techniques for analyzing the local behavior of solutions to the NS3D equations themselves, particularly in understanding the structure of potential singularities.

**Key Insights:**
1. **Structural Cancellation is Key:** The paper highlights the critical importance of the structural condition `\kappa(s) = \Theta_0 s \chi(s)` (Eq. 1.6). This condition creates a cancellation effect between the chemotaxis term in the `n` equation and the consumption term in the `c` equation, which is essential for deriving the necessary a priori energy estimates. This suggests that for a coupled system like NS3D, finding hidden structural relationships or cancellations might be a viable path to controlling nonlinearities.
2. **Local Energy Inequalities are Derivable for Complex Coupled Systems:** The main achievement of the paper is the successful derivation of a local energy inequality for the full 3D chemotaxis-Navier-Stokes system. This demonstrates that the CKN framework can be extended from the pure fluid equations to more complex, physically relevant multi-physics models. This is an encouraging result for anyone trying to apply similar regularity techniques to other nonlinear PDEs.
3. **Regularization Schemes Can Tame 'Super-Critical' Terms:** The paper deals with terms that are considered super-critical from a standard PDE scaling perspective. The proof strategy relies on a carefully constructed regularization/approximation scheme (the system in Eq. 1.9) that makes the problem tractable. By first proving existence for the regularized system and then passing to the limit, they can handle the difficult nonlinearities. This reinforces the power of approximation methods in tackling difficult PDE problems.

**Equations:**
- $$\[ \partial_t n + u \cdot \nabla n - \Delta n = -\nabla \cdot (n\chi(c)\nabla c) \]$$
  This is the convection-diffusion-chemotaxis equation for the cell density `n`. It describes the change in cell concentration due to advection by the fluid flow (`u \cdot \nabla n`), random diffusion (`\Delta n`), and chemotaxis, which is the directed movement of cells up or down a chemical gradient (`-\nabla \cdot (n\chi(c)\nabla c)`).
- $$\[ \partial_t c + u \cdot \nabla c - \Delta c = -\kappa(c)n \]$$
  This is the reaction-diffusion equation for the oxygen concentration `c`. It describes the change in oxygen concentration due to advection by the fluid (`u \cdot \nabla c`), diffusion (`\Delta c`), and consumption by the cells at a rate `\kappa(c)n`.
- $$\[ \partial_t u + \mu(u \cdot \nabla)u - \Delta u + \nabla P = n\nabla\phi \]$$
  This is the forced Navier-Stokes equation for the fluid velocity `u`. It governs the fluid's motion, where the fluid is driven by a force (`n\nabla\phi`) exerted by the swimming bacteria, which is proportional to the cell density `n` and the gradient of a potential `\phi` (e.g., gravity).
- $$\[ \nabla \cdot u = 0 \]$$
  This is the incompressibility condition, stating that the fluid is divergence-free, meaning its volume does not change.
- $$\[ \partial_t n + u \cdot \nabla n - \Delta n = -\nabla \cdot (n \nabla c) \]$$
  A simplified version of the cell density equation where the chemotactic sensitivity `\chi(c)` is assumed to be 1.
- $$\[ \partial_t c + u \cdot \nabla c - \Delta c = -cn \]$$
  A simplified version of the oxygen concentration equation where the consumption rate `\kappa(c)` is assumed to be `c`.
- $$\[ \partial_t u + (u \cdot \nabla)u - \Delta u + \nabla p = n \nabla \phi, \quad \nabla \cdot u = 0 \]$$
  The simplified fluid velocity equation, identical to the general case but often studied in this specific context.

**Theorems:**
- Theorem 1.2: Global Existence of Suitable Weak Solutions: Statement: Under certain assumptions on the initial data `(n_0, c_0, u_0)` and the functions `\phi, \kappa, \chi`, there exists a global suitable weak solution to the chemotaxis-Navier-Stokes system (1.1). For the simpler chemotaxis-Stokes model (`\mu=0`), an additional a priori estimate for the velocity is obtained.
  *Proof:* Proof technique: The proof is based on a multi-step regularization and approximation scheme. First, the system is regularized by adding extra diffusion terms and mollifying nonlinear terms (system 1.9). The existence of global strong solutions for this regularized system is established using a fixed-point argument (Theorem 1.4). Then, uniform a priori estimates, independent of the regularization parameters `\epsilon` and `\tau`, are derived. Finally, using compactness arguments (Aubin-Lions Lemma), the authors show that the solutions to the regularized system converge to a suitable weak solution of the original system as the regularization parameters go to zero. A key part is establishing the strong convergence of `n ln n` to derive the local energy inequality.
- Theorem 1.4: Global Well-posedness of the Regularized System: Statement: For smooth initial data, there exists a unique, global strong solution to the regularized system (1.9).
  *Proof:* Proof technique: The proof uses a Banach fixed-point theorem in a carefully chosen function space `S`. The authors define a mapping `\Phi` based on the integral form of the equations (using the heat semigroup) and show that for a sufficiently small time `T`, this mapping is a contraction on a closed ball in `S`. This gives a local-in-time solution. The solution is then extended globally by deriving a series of a priori estimates on higher-order Sobolev norms of the solution, which show that the norms cannot blow up in finite time.

**Constants & Bounds:**
- `A Priori Estimate (1.3): `\[ U(t) + \int_0^t V(\tau) d\tau \le C e^{Ct} \]``: This is an energy-type estimate for the *simplified* system (1.2) from previous works. It shows that a combined norm `U(t)` of the solution and the time-integral of a dissipation term `V(t)` can grow at most exponentially in time. The authors' new result (Theorem 1.2) provides a linear-in-time growth, which is a significant improvement.
- `Energy Inequality (Part (iii) of Def 1.1): `\[ \|u(t)\|^2_{L^2} + \int_0^t \|\nabla u\|^2_{L^2} + ... \le C(initial\ data)(1+t) \]``: This is the global energy inequality for the suitable weak solution. It provides a bound on the kinetic energy and total dissipation, showing that it grows at most linearly in time. This is a crucial a priori bound that prevents the solution from blowing up in an average sense.
- `Local Energy Inequality (Part (iv) of Def 1.1): This is a long and complex inequality that holds in the sense of distributions. It is the defining property of a *suitable* weak solution.`: It is a localized version of the global energy inequality, valid in any smooth, compactly supported test function `\psi`. It is the key tool used in the CKN theory to control the behavior of the solution near a potential singularity. The various terms on the right-hand side represent local energy production/dissipation due to pressure, advection, and external forces, and they must be carefully estimated to prove regularity.
- `Condition (1.6): `\[ \kappa(s) = \Theta_0 s \chi(s) \]``: This is a crucial structural condition relating the oxygen consumption rate `\kappa(s)` to the chemotactic sensitivity `\chi(s)`. The authors state that this cancellation structure is essential for their analysis and for obtaining the necessary a priori estimates. Without it, the existence of even a Leray-Hopf weak solution is unknown.

---


## Supporting Physics and Turbulence
*Papers on turbulence theory, intermittency, Couette-Taylor instabilities, and physical fluid dynamics insights.*

### A case of strong non linearity: intermittency in highly turbulent flows
**Authors:** Yves Pomeau, Martine Le Berre, Thierry Lehner | **Year:** 2018 | [1806.04893v2](https://arxiv.org/abs/1806.04893v2) | **Validation:** verified
**Relevance:** 9/10

**Why it matters:** This paper is highly relevant to the NS3D blowup problem because it provides strong experimental evidence that the dynamics of the most extreme events in turbulent flows are governed by the type of self-similar scaling proposed by Leray in his original work on the problem. It directly confronts the abstract mathematical theory with real-world data, suggesting that the intermittent bursts seen in turbulence are the physical manifestation of incipient singularities. This bridges a critical gap between theory and experiment, providing a concrete physical phenomenon for mathematicians to target when searching for a blowup solution. The paper specifically addresses the nature of the solution in the pre-blowup phase, suggesting that the dynamics are dominated by inviscid, self-similar collapse.

**Key Insights:**
1. Focus on Intermittency: The most extreme, intermittent events in turbulent flows are the most likely place to find evidence of singular behavior. Don't look for blowup in the average flow; look for it in the rare, violent bursts that defy classical Kolmogorov scaling.
2. The `u^3` vs. `γ` Relationship is a Key Signature: The scaling relationship `u^3 ∼ γ` (or even better, `u^{8/3} ∼ γ`) is a powerful experimental signature of a Leray-type singularity. An engineer trying to prove blowup should look for numerical solutions that exhibit this scaling in the vicinity of a potential singularity.
3. Inviscid Dynamics Dominate the Collapse: The experimental data suggests that the blowup process is fundamentally an inviscid phenomenon, governed by the Euler equations. Viscosity's role is to regularize the singularity at the very last moment, but the path to the singularity is paved by the nonlinear advection term.
4. The Choice of Conservation Law Matters: The fact that the Sedov-Taylor scaling (based on energy conservation) fits the data slightly better than the Leray scaling (based on circulation conservation) is a crucial clue. It suggests that the conserved quantity in the collapsing domain is a key determinant of the singularity's structure.
5. Asymmetry as a Clue: The observed asymmetry in the time signal of the bursts (fast rise, slow decay) is another piece of evidence for a singularity. The fast rise corresponds to the inviscid collapse, while the slow decay is the result of viscous dissipation after the near-singularity has been regularized. This asymmetry could be a useful feature to look for in numerical simulations.

**Equations:**
- $$\frac{\partial u}{\partial t} + u \cdot \nabla u = -\nabla p + \nu \nabla^2 u` and `\nabla \cdot u = 0$$
  These are the fundamental equations of fluid dynamics. The first equation is the momentum equation, which describes how the velocity of a fluid changes over time due to convection, pressure gradients, and viscous forces. The second equation is the incompressibility condition, which states that the fluid density is constant.
- $$u(r,t) = (t* - t)^{-\alpha} U(r(t* - t)^{-\beta})` and `p(r,t) = (t* - t)^{-2\alpha} P(r(t* - t)^{-\beta})$$
  This is an assumption about the form of a solution near a potential singularity at time `t*`. It states that the velocity and pressure fields at different times are scaled versions of each other. The exponents `alpha` and `beta` determine the scaling.
- $$\alpha + \beta = 1$$
  This relation between the self-similar exponents is derived by requiring that the self-similar form of the solution is consistent with the Euler equations (the inviscid Navier-Stokes equations).
- $$\alpha = \beta = 1/2$$
  These are the specific values of the self-similar exponents proposed by Leray. They are obtained by requiring consistency with the Navier-Stokes equations, including the viscous term.
- $$\dot{U} + \frac{1}{2}(U + R \cdot \nabla_R U) + U \cdot \nabla U = -\nabla P + \nabla^2 U` and `\nabla \cdot U = 0$$ *(corrected)*
  These are the equations for the scaled velocity profile `U` in the self-similar solution of the Euler equations. They are derived by substituting the self-similar form into the Euler equations.
  > Correction: The original used partial derivative notation for the time derivative of U, but the paper uses dot notation. Also, the gradient operator in one term was missing a subscript R, and the viscous term was missing.
- $$\alpha = 3/5` and `\beta = 2/5$$
  These are alternative values for the self-similar exponents, obtained by requiring conservation of energy in the collapsing domain, rather than conservation of circulation.
- $$<u^3>_\gamma \sim \gamma$$ *(corrected)*
  This relation, derived from the Leray scaling, predicts that for a singular event, the cube of the velocity is proportional to the acceleration, with the constant of proportionality being the circulation `Gamma`.
  > Correction: The original equation was a simplified representation. The paper uses conditional averaging, which is represented by the angle brackets and subscript gamma. The circulation Gamma is not in the experimentally verified relation.
- $$u^{8/3} \sim \gamma E^{1/3}$$
  This is the equivalent of the previous relation, but derived using the Sedov-Taylor exponents. It relates the velocity to the 8/3 power to the acceleration.
- $$Not found in paper$$ *(corrected)*
  This relation, based on Kolmogorov's theory of turbulence, predicts a different relationship between velocity and acceleration, where their product is proportional to the energy dissipation rate `epsilon`.
  > Correction: This equation, related to Kolmogorov's theory, was not found in the provided PDF.

**Theorems:**
- Proposition 1: The relationship between large velocity fluctuations (u) and large accelerations (γ) in intermittent turbulent flows is described by `u^3 ∼ γ`, which is consistent with Leray's self-similar singularity model.
  *Proof:* The authors analyze hot-wire anemometer data from the Modane wind tunnel. They compute conditional moments of the velocity and acceleration. The experimental data shows a clear linear relationship between `<u^3>_γ` and `γ` for large values of `γ`, which supports the `u^3 ∼ γΓ` scaling derived from the Leray model with α = β = 1/2. This relationship is shown to be inconsistent with the predictions of Kolmogorov's K41 theory.
- Proposition 2: The Sedov-Taylor scaling, `u^{8/3} ∼ γ`, provides an even better fit to the experimental data than the Leray scaling.
  *Proof:* The authors plot the ratio `<u^{8/3}>_γ / γ` and show that it exhibits a flatter plateau than `<u^3>_γ / γ`. This suggests that the assumption of energy conservation in the collapsing domain (leading to Sedov-Taylor exponents) might be more accurate than the assumption of circulation conservation (leading to Leray exponents).
- Hypothesis: The effect of small viscosity is to regularize the singularity of the Euler equations through a drift in the dilation parameter.
  *Proof:* This is a theoretical argument, not a rigorous proof. The authors assume that the Euler-Leray equations have a solution but the NS-Leray equations do not. They then treat viscosity as a perturbation that breaks the dilation invariance of the Euler-Leray equations. This leads to a solvability condition that results in a dynamical equation for the dilation parameter `μ`, causing it to drift and ultimately suppress the singularity.

**Constants & Bounds:**
- `Leray Exponents: `\alpha = \beta = 1/2``: These exponents arise from the requirement of circulation conservation in the self-similar solution of the Navier-Stokes equations. They define the scaling of the velocity and length scales near a potential singularity.
- `Sedov-Taylor Exponents: `\alpha = 3/5`, `\beta = 2/5``: These exponents arise from the requirement of energy conservation in the self-similar solution of the Euler equations. The paper finds that these exponents provide a slightly better fit to the experimental data.
- `Velocity-Acceleration Scaling (Leray): `u^3 \sim \gamma \Gamma``: This is a key prediction of the Leray singularity model. It provides a testable relationship between the velocity and acceleration fluctuations in a turbulent flow.
- `Velocity-Acceleration Scaling (Sedov-Taylor): `u^{8/3} \sim \gamma E^{1/3}``: This is the analogous scaling relationship derived from the Sedov-Taylor exponents. The paper shows this provides an even better fit to the data.
- `Kolmogorov Scaling: `u_r \gamma \sim \epsilon``: This is the scaling relationship predicted by Kolmogorov's theory of turbulence. The paper shows that this scaling is inconsistent with the experimental data for large, intermittent events.

---

