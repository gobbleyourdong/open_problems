---
source: Analytical attempt — CZ constant improvement for strain-vorticity on div-free fields
type: PROOF ATTEMPT — three approaches, rigorous assessment of each
status: ALL THREE FAIL — exact failure points identified
date: 2026-03-26
---

# Can the CZ Constant for Strain-Vorticity Be Improved on Div-Free Fields?

## Setup

On the 3-torus T^3, let omega be a divergence-free vector field:

    omega_hat(k) . k = 0   for all k in Z^3 \ {0}

Recover velocity via Biot-Savart:

    u_hat(k) = i (k x omega_hat(k)) / |k|^2

Define strain:

    S = (nabla u + (nabla u)^T) / 2

The operator T: omega -> S is a composition of zeroth-order Calderon-Zygmund
operators (Riesz transforms). The classical CZ theorem gives:

    ||S||_{L^p} <= C_p ||omega||_{L^p}   for 1 < p < infinity

where C_p is the GENERAL CZ constant for Riesz transforms in R^3
(or its periodic analogue on T^3).

**Claim to investigate:** Does there exist epsilon > 0 such that

    ||S||_{L^p} <= (C_p - epsilon) ||omega||_{L^p}

for all divergence-free omega, specifically at p = 3?


---

## Approach 1: Fourier Multiplier Analysis

### The multiplier

For a general vector field v on T^3, the velocity is NOT given by
Biot-Savart. But for divergence-free omega, u_hat(k) = i k x omega_hat(k) / |k|^2.

The strain in Fourier space:

    S_hat(k)_{ij} = (i/2)(k_i u_hat(k)_j + k_j u_hat(k)_i)

Substituting u_hat(k) = i (k x omega_hat(k)) / |k|^2:

    S_hat(k)_{ij} = -(1/2) [k_i (k x omega_hat(k))_j + k_j (k x omega_hat(k))_i] / |k|^2

Let xi = k/|k| (unit direction). Let omega_hat(k) = a (the Fourier coefficient).
Div-free: a . xi = 0, so a lies in the 2D plane Pi_xi = {v : v . xi = 0}.

Define the multiplier map m(xi): R^3 -> Sym_0(3x3) by:

    m(xi)(a)_{ij} = -(1/2) [xi_i (xi x a)_j + xi_j (xi x a)_i]

(we factor out |k|^0, since S and omega are related by zeroth-order operators).

### Restricted vs unrestricted operator norm

The **unrestricted** operator norm of m(xi): sup over all a in R^3 with |a|=1
of |m(xi)(a)|_{Frobenius}.

The **restricted** operator norm: sup over a in Pi_xi with |a|=1 of |m(xi)(a)|_{Fro}.

**Key question:** Is ||m(xi)|_{Pi_xi}||_{op} < ||m(xi)||_{op} for all xi?

### Explicit computation

Let xi = e_3 (by rotational symmetry, WLOG). Then:

For a = (a_1, a_2, a_3):

    xi x a = e_3 x a = (-a_2, a_1, 0)

    m(xi)(a)_{ij} = -(1/2) [xi_i (xi x a)_j + xi_j (xi x a)_i]

Writing it out (xi = (0,0,1)):

    m_{11} = 0,  m_{22} = 0,  m_{33} = 0
    m_{12} = m_{21} = 0
    m_{13} = m_{31} = -(1/2)[(0)(-a_2) + (1)(a_1 * 0 ... )]

Wait, let me be more careful.

    m_{13} = -(1/2)[xi_1 (xi x a)_3 + xi_3 (xi x a)_1]
           = -(1/2)[0 * 0 + 1 * (-a_2)]
           = a_2/2

    m_{31} = m_{13} = a_2/2

    m_{23} = -(1/2)[xi_2 (xi x a)_3 + xi_3 (xi x a)_2]
           = -(1/2)[0 * 0 + 1 * a_1]
           = -a_1/2

    m_{32} = m_{23} = -a_1/2

    m_{11} = -(1/2)[xi_1 (xi x a)_1 + xi_1 (xi x a)_1] = 0
    m_{12} = -(1/2)[xi_1 (xi x a)_2 + xi_2 (xi x a)_1] = 0
    m_{22} = 0
    m_{33} = -(1/2)[xi_3 (xi x a)_3 + xi_3 (xi x a)_3] = 0

So for xi = e_3:

    m(e_3)(a) = | 0       0     a_2/2  |
                | 0       0    -a_1/2  |
                | a_2/2  -a_1/2   0    |

The Frobenius norm:

    |m(e_3)(a)|_F^2 = 2(a_2/2)^2 + 2(a_1/2)^2 = (a_1^2 + a_2^2)/2

The div-free constraint: a . xi = a_3 = 0, so a = (a_1, a_2, 0).
With |a| = 1: a_1^2 + a_2^2 = 1.

    |m(e_3)(a)|_F^2 = 1/2   (on Pi_xi, with |a|=1)

Now the UNRESTRICTED norm: allow a = (a_1, a_2, a_3) with |a|=1.
Same formula: |m(e_3)(a)|_F^2 = (a_1^2 + a_2^2)/2.
Maximum over |a|=1: take a_3 = 0, get |m|_F^2 = 1/2.

**RESULT: The restricted and unrestricted Frobenius norms are IDENTICAL.**

This is because the multiplier m(xi)(a) depends only on xi x a, and
|xi x a| = |a| sin(angle(a, xi)). The maximum of |xi x a| over |a|=1
occurs when a is perpendicular to xi, which is EXACTLY the div-free plane.

### Why this kills Approach 1

The div-free constraint a . xi = 0 forces a into Pi_xi. But the
multiplier m(xi)(a) = function of (xi x a), and |xi x a| is MAXIMIZED
when a is in Pi_xi. So the div-free constraint does NOT reduce the
pointwise multiplier norm -- it actually SELECTS the directions where
the multiplier is largest.

This is not surprising physically: the Biot-Savart law u = curl^{-1}(omega)
converts vorticity efficiently precisely BECAUSE omega is perpendicular
to k (divergence-free). If omega had a component along k, that component
would be "wasted" (it produces no velocity). So div-free omega is the
MOST efficient at producing velocity, hence strain.

**Verdict: Approach 1 FAILS. The Fourier multiplier norm is not reduced
on the div-free subspace; if anything, the div-free constraint maximizes it.**

### Important caveat about L^p vs L^2

The computation above shows the multiplier norm is not reduced pointwise
in Fourier space. For p = 2, the L^2 bound follows by Parseval and the
pointwise multiplier norm, so there is no improvement at p = 2.

For p != 2, the L^p CZ bound does NOT come from pointwise Fourier
multiplier norms. It comes from the singular kernel structure and
cancellation properties (the Hormander condition, etc.). The CZ constant
C_p involves:

    C_p = C(p) * (||m||_{L^infty} + ||nabla_xi m||_{Dini})

The L^infty norm of m on the sphere is the same whether restricted to
Pi_xi or not (as shown above). But the Dini norm of nabla_xi m might
differ on the restricted vs unrestricted domains.

However, the standard CZ theorem does not take the div-free constraint
into account in its proof -- it bounds the operator on ALL of L^p, not
on the subspace of div-free fields. The question is whether a DIFFERENT
proof technique (exploiting div-free structure) could yield a better constant.

This leads to Approach 2.


---

## Approach 2: Tracelessness of S

### The constraint

For divergence-free omega, the velocity u satisfies div(u) = 0 (from
Biot-Savart: div(u) = div(curl^{-1}(omega)) = 0). Therefore:

    tr(S) = div(u) = 0

So S is a SYMMETRIC TRACELESS 3x3 tensor (5 independent components,
not 6). The codomain of T is Sym_0(3x3), not Sym(3x3).

### Does tracelessness help?

The CZ bound ||T(omega)||_{L^p} <= C_p ||omega||_{L^p} treats T as a
map from vector fields to symmetric tensor fields. If we decompose
symmetric tensors as:

    Sym(3x3) = Sym_0(3x3) + R * Id    (traceless + trace part)

Then T maps to Sym_0 by construction. But the CZ constant C_p is defined
as the operator norm of T:

    C_p = sup_{omega != 0} ||T(omega)||_{L^p(Sym)} / ||omega||_{L^p}

If all outputs are traceless, then ||T(omega)||_{L^p(Sym)} is computed
using the Frobenius norm on symmetric tensors. The Frobenius norm does
not distinguish between traceless and traced tensors -- ||A||_F^2 = sum A_{ij}^2
regardless of tr(A).

So tracelessness does not directly reduce the norm.

### Dimensional argument (incorrect)

One might argue: the space of symmetric tensors is 6D, the space of
traceless symmetric tensors is 5D. In a random model, projecting from
6D to 5D reduces the norm by sqrt(5/6).

But this is WRONG because:
1. T already maps INTO the 5D subspace (it never produces trace).
2. The CZ constant already accounts for this -- it's the sup of the
   actual operator, not a hypothetical extension.
3. There is no "wasted" dimension to remove.

### Could tracelessness help indirectly?

The tracelessness constraint tr(S) = 0 means the eigenvalues of S
satisfy lambda_1 + lambda_2 + lambda_3 = 0. This constrains the
eigenvalue distribution: you cannot have all positive eigenvalues.

For the L^3 norm:

    ||S||_{L^3}^3 = integral |S|_F^3 dx

where |S|_F = sqrt(sum S_{ij}^2). The tracelessness means:

    |S|_F^2 = sum S_{ij}^2 = sum lambda_i^2 (in principal frame)
            = lambda_1^2 + lambda_2^2 + (lambda_1 + lambda_2)^2
            = 2(lambda_1^2 + lambda_2^2 + lambda_1 lambda_2)

This is a quadratic form in (lambda_1, lambda_2). For the general
(non-traceless) case:

    |S|_F^2 = lambda_1^2 + lambda_2^2 + lambda_3^2

without the constraint lambda_3 = -lambda_1 - lambda_2. The traceless
version has the SAME maximum over the unit sphere in eigenvalue space
(the constraint is automatically satisfied at the extremizers of the
Frobenius norm).

**Verdict: Approach 2 FAILS. Tracelessness is automatic for the strain
of a div-free field, and the CZ bound already captures the true operator
norm including this constraint. There is no "hidden" reduction.**


---

## Approach 3: Betchov Relation and Algebraic Constraints

### The Betchov identity

For a divergence-free field on T^3 (or R^3 with decay):

    integral tr(S^3) dx = -(3/4) integral omega . S . omega dx

This is an EXACT algebraic identity (proved by integration by parts,
using div(u) = 0).

### The enstrophy production connection

The enstrophy production is:

    dE/dt = integral omega . S . omega dx = -(4/3) integral tr(S^3) dx

So the enstrophy growth is controlled by tr(S^3).

### The isotropic/anisotropic decomposition of S^3

tr(S^3) = lambda_1^3 + lambda_2^3 + lambda_3^3 = 3 lambda_1 lambda_2 lambda_3
(using tr(S) = 0 and the Newton identity).

So:

    integral omega . S . omega dx = -(4/3) * 3 integral lambda_1 lambda_2 lambda_3 dx
                                   = -4 integral det(S) dx

This relates enstrophy production to the integral of det(S).

### Can this constrain the L^3 ratio?

We want: ||S||_{L^3} <= (C_3 - epsilon) ||omega||_{L^3}.

The Betchov relation gives a constraint on the INTEGRAL of omega . S . omega
in terms of the INTEGRAL of det(S). But this is a WEAK constraint:

1. It constrains the integral of a bilinear form, not the L^p norms.
2. The L^3 norms involve |S|^3 and |omega|^3, which are different
   from omega . S . omega and det(S).
3. Even if omega . S . omega is small (the integral), the individual
   norms ||S||_{L^3} and ||omega||_{L^3} can be large.

### Attempting the Holder route

By Holder: |integral omega . S . omega dx| <= ||omega||_{L^3}^2 * ||S||_{L^3}

And by Betchov: integral omega . S . omega = -4 integral det(S)

So: |integral det(S) dx| <= (1/4) ||omega||_{L^3}^2 * ||S||_{L^3}

Also by Holder on det(S) = lambda_1 lambda_2 lambda_3:

    |det(S)| <= |S|_F^3 / (3 sqrt(6))    (AM-GM on eigenvalues with tr(S)=0)

So: integral |det(S)| <= C * integral |S|^3 = C * ||S||_{L^3}^3

This gives: ||S||_{L^3}^3 >= c * |integral det(S)|

But we need an UPPER bound on ||S||_{L^3}, not a lower bound. The Betchov
relation provides a connection between omega . S . omega and det(S), but
in the wrong direction for our purposes.

### The deeper issue

The Betchov relation constrains a SINGLE integral (the enstrophy production)
in terms of another single integral (det S). These are scalar constraints
on the L^1 norm of specific nonlinear quantities. They do NOT constrain
the L^3 norms of S and omega individually.

To get ||S||_{L^3} < C ||omega||_{L^3}, we need a POINTWISE or L^p-level
improvement, not just integral-level constraints.

### Could we use Betchov + CZ iteratively?

The idea: use the CZ bound to get S from omega, then use Betchov to get
a constraint on the enstrophy production, then feed back.

But this is circular: the CZ bound gives ||S||_{L^3} <= C ||omega||_{L^3},
and Betchov gives integral(omega . S . omega) = -4 integral(det S).
The Betchov relation does NOT improve the CZ constant -- it relates
different integrals involving S and omega, but neither constrains
the L^3 ratio.

**Verdict: Approach 3 FAILS. The Betchov relation provides integral-level
algebraic constraints between S and omega, but these do not constrain
the L^p operator norm ratio that defines the CZ constant.**


---

## Approach 1b: L^p for p != 2 via Kernel Cancellation

Before concluding, let me consider a more sophisticated version of
Approach 1. The L^p CZ theory (p != 2) uses properties of the
KERNEL, not just the multiplier. The Biot-Savart kernel is:

    u(x) = (1/4pi) integral (omega(y) x (x-y)) / |x-y|^3 dy

    S_ij(x) = PV integral K_ij(x-y) omega(y) dy

where K is a 3x3-to-3x3 tensor kernel of CZ type (homogeneous degree -3,
zero mean on spheres).

For GENERAL vector fields, the CZ constant involves the L^infty norm of
the kernel's angular part on S^2, plus regularity conditions.

For DIV-FREE vector fields, we can write:

    S_ij(x) = PV integral K_ij(x-y) P_perp(y) omega(y) dy

where P_perp is the Leray projector (which is the identity on div-free fields).
Since omega is div-free, P_perp omega = omega, so this is the same operator.

The question becomes: does the COMPOSITION K . P_perp have a smaller
CZ constant than K alone?

### Why the composition does not help (for operator norm)

P_perp is a Fourier multiplier (projection onto k-perp). It is a bounded
operator on L^p with norm 1. The composition T = K . P_perp satisfies:

    ||T|| <= ||K|| * ||P_perp|| = ||K|| * 1 = ||K||

But this is an UPPER bound. Could ||T|| < ||K||?

Only if there is CANCELLATION between K and P_perp. Since P_perp is
a projection (P_perp^2 = P_perp), and K already maps div-free fields
to div-free strain (the composition K . P_perp restricted to div-free
fields IS just K restricted to div-free fields), the question reduces to:

Is the RESTRICTED operator norm ||K|_{div-free}|| < ||K||?

This is asking whether there exist non-div-free vector fields that
achieve a HIGHER ||K(f)||_{L^p} / ||f||_{L^p} ratio than any div-free field.

### The critical obstruction

For p = 2: the Fourier multiplier analysis (Approach 1) showed that
the div-free subspace MAXIMIZES the multiplier, not minimizes it.
The restricted norm equals the unrestricted norm at p = 2.

For p != 2: the CZ constant depends on the singular integral kernel,
not just the Fourier multiplier. However, the extremizers of CZ operators
are known (in many cases) to be related to the Riesz transforms of
INDICATOR functions of half-spaces and similar geometric objects.

For the Hilbert transform (1D Riesz): the best constant is known
(Pichorides 1972): C_p = max(tan(pi/2p), cot(pi/2p)). The extremizers
approach indicator functions of half-lines, which have NO div-free
constraint in 1D (div-free in 1D means constant).

In 3D: the extremizers of ||R_i R_j f||_{L^p} are not fully characterized.
But the known extremizers for individual Riesz transforms (Banuelos-Wang 1995,
Iwaniec-Martin 1996, Dragicevic-Volberg 2005) are SCALAR functions
that approximate indicators of half-spaces. When embedded as components
of vector fields, there is no reason these extremizers would be div-free.

In fact, div-free fields have the constraint hat{omega}(k) . k = 0,
which correlates different components. The CZ extremizers typically
involve a SINGLE component (omega_1 = f, omega_2 = omega_3 = 0),
which is NOT div-free (unless hat{f}(k) . k_1 = 0 for all k, which
forces f to depend only on x_2, x_3).

So it is PLAUSIBLE that the div-free constraint prevents the
CZ extremizers from being achieved. But:

### The counterargument: planar vorticity

Consider omega = (0, 0, f(x_1, x_2)) with hat{f}(k_1, k_2) arbitrary.
This is div-free since d(omega_3)/d(x_3) = 0 (and omega_1 = omega_2 = 0).

The velocity: u = curl^{-1}(omega) has components involving Riesz transforms
of f in the (x_1, x_2) plane. The strain S involves R_1 R_2 f, etc.
(2D Riesz transforms of the scalar f).

Now f is an UNCONSTRAINED scalar function on T^2 (no div-free condition
on f itself). So ||S||_{L^p} involves ||R_i R_j f||_{L^p(T^2)} with
f arbitrary. This achieves the FULL 2D CZ constant for Riesz transforms.

Since the 2D CZ constant for R_i R_j is the SAME as the 3D CZ constant
for R_i R_j (the constants depend on dimension only through the kernel
structure, and for second-order Riesz transforms, the angular parts have
the same L^infty norm in all dimensions >= 2):

**The div-free restriction does NOT reduce the CZ constant, because
planar div-free fields can approximate the CZ extremizers.**

### Explicit construction

Take omega = (0, 0, f_epsilon(x_1, x_2)) where f_epsilon approximates
the known CZ extremizer for R_1 R_2 in 2D (a function that approaches
the indicator of a quadrant, or similar).

Then omega is div-free, and:

    ||S||_{L^p} / ||omega||_{L^p} = ||R_i R_j f_epsilon||_{L^p} / ||f_epsilon||_{L^p}
                                   -> C_p as epsilon -> 0

(up to constant factors from the specific components).

**This shows the CZ constant is ACHIEVED (in the limit) by div-free fields.**


---

## Approach 3b: Structural Constraint via the Specific Operator

The approaches above treat the strain-vorticity operator as a GENERAL
CZ operator and ask whether restricting to div-free inputs helps.
But the strain-vorticity operator has specific structure beyond being CZ.

Specifically, S = (nabla u + nabla u^T)/2 where u = BS(omega). The
COMPOSITION nabla . BS is a specific combination of Riesz transforms.
The general CZ constant C_p applies to ANY CZ operator with multiplier
norm <= 1. But the specific combination might have a smaller L^p norm
than the worst-case CZ operator.

### The operator decomposition

S_{ij} = (1/2)(partial_i u_j + partial_j u_i)

where u_l = sum_m epsilon_{lmn} partial_m (-Delta)^{-1} omega_n
          = sum_m epsilon_{lmn} R_m (-Delta)^{-1/2} omega_n

Wait, more precisely: u_l = epsilon_{lmn} partial_m (-Delta)^{-1} omega_n.

So:

    partial_i u_j = epsilon_{jmn} partial_i partial_m (-Delta)^{-1} omega_n
                  = -epsilon_{jmn} R_i R_m omega_n

Therefore:

    S_{ij} = -(1/2) sum_n [epsilon_{jmn} R_i R_m + epsilon_{imn} R_j R_m] omega_n

This is a matrix of second-order Riesz transforms applied to the COMPONENTS
of omega. The CZ constant for this specific operator is:

    C_p^{S} = sup_{omega in L^p} ||S||_{L^p} / ||omega||_{L^p}

This is a SPECIFIC operator, not the worst-case CZ operator. Its constant
C_p^S could be strictly less than the general C_p for second-order Riesz
transforms R_i R_j.

### But we need to compare with the RIGHT general constant

The claim is about C_p^S (the constant for THIS specific operator) vs
C_p^{gen} (the general CZ constant). But what IS the "general CZ constant"?

If C_p^{gen} means the constant for a single R_i R_j, then C_p^S involves
a LINEAR COMBINATION of R_i R_j operators. The L^p norm of a linear
combination can be either larger or smaller than the maximum of the
individual norms.

For p = 2: ||S||_{L^2} = ||omega||_{L^2} / sqrt(2) (from Parseval and
the multiplier computation). So C_2^S = 1/sqrt(2) < 1 = C_2^{R_iR_j}.
The specific structure DOES give a smaller constant at p = 2!

But this is well-known and does not help for the regularity problem.
The regularity problem needs the L^3 (or L^{3/2} or related) bound.

For p = 3: the constant C_3^S is not known analytically. Computing it
would require the full machinery of Bellman functions or heat flow methods
for CZ operators.

### What the p = 2 calculation actually shows

At p = 2, from the multiplier (Approach 1):

    |m(xi)(a)|_F^2 = (1/2)|a x xi|^2 = (1/2)|a|^2 sin^2(angle(a,xi))

For div-free a (a . xi = 0): sin^2 = 1, so |m|_F^2 = |a|^2/2.
For unrestricted a: max is |a|^2/2 (achieved at a perp xi).

So ||S||_{L^2}^2 = (1/2) ||omega||_{L^2}^2 for div-free omega.
And the same ratio 1/2 is achieved even without the div-free constraint.

The factor 1/2 comes from the SPECIFIC structure of the operator
(the antisymmetry of cross product), not from the div-free constraint.


---

## The Fundamental Reason All Approaches Fail

The div-free constraint omega_hat(k) . k = 0 restricts omega to a
2-dimensional plane at each wavenumber k. The strain-vorticity operator
T maps this 2D plane into the 5D space of traceless symmetric tensors.

The key insight is that the div-free constraint HELPS the operator, not
hurts it. Here is why:

### The operator T factors through the div-free projection

For ANY vector field v (not necessarily div-free), define:

    u = BS(v) would be: u_hat(k) = i k x v_hat(k) / |k|^2

But k x v_hat(k) = k x P_perp v_hat(k), where P_perp is the projection
onto the plane perpendicular to k. The component of v along k does not
contribute to the cross product.

So: T(v) = T(P_perp v) for all v.

This means: ||T|| = sup_v ||T(v)||/||v|| = sup_v ||T(P_perp v)||/||v||
           <= sup_v ||T(P_perp v)||/||P_perp v|| (since ||P_perp v|| <= ||v||)
           = ||T|_{div-free}||

Wait -- this shows the OPPOSITE: ||T|_{div-free}|| >= ||T|| (the restricted
norm is at least as large as the unrestricted norm, if we define the
unrestricted operator as the same Biot-Savart formula applied to any v).

Actually, this is because the Biot-Savart formula naturally kills the
irrotational part. The operator T is not a general CZ operator on L^p(R^3 -> R^3);
it is specifically the strain-from-vorticity map, which is defined only
for the curl of something. The "general CZ constant" for this specific
operator IS the constant on div-free fields.

### The comparison is ill-posed

The claim "||S||_{L^3} <= (C - epsilon) ||omega||_{L^3} for div-free omega"
requires comparing with a constant C that applies to a LARGER class.
But what larger class?

**Option A:** C is the CZ constant for a general R_i R_j.
Then C = C_3(R_i R_j) and the question is whether the specific linear
combination in the strain operator has a smaller L^3 constant.
This is true at p = 2 (factor 1/sqrt(2)) but unknown at p = 3.
Crucially: this has NOTHING to do with the div-free constraint.
It is about the specific structure of the Biot-Savart operator.

**Option B:** C is the CZ constant for the operator T applied to
general (not div-free) vector fields.
But T is defined via Biot-Savart, which automatically projects out
the div-free part. So T on general fields equals T on div-free fields
composed with the Leray projector. Since the Leray projector has
||P||_{L^p} = 1 for 1 < p < infinity (it is a CZ operator itself),
||T|_{general}|| = ||T . P|| <= ||T|_{div-free}||.
And ||T|_{general}|| >= ||T|_{div-free}|| (div-free is a subset).
So ||T|_{general}|| = ||T|_{div-free}||. No improvement.

**Option C:** C is the classical CZ constant from the proof of
||S||_{L^3} <= C ||omega||_{L^3} that does NOT exploit div-free structure.
This C is an UPPER bound, not the true operator norm. The true operator
norm might be strictly less than this upper bound, but this is about
the TIGHTNESS of the proof, not about the div-free constraint.


---

## What About the Enstrophy Application?

Even though the CZ constant itself cannot be improved by the div-free
constraint, the APPLICATION to enstrophy evolution might still benefit.

The enstrophy evolution:

    dE/dt = integral omega . S . omega dx

This involves the BILINEAR form omega . S . omega, not just ||S||_{L^3}.

By the single-mode orthogonality (file 014): for a single Fourier mode,
omega . S . omega = 0 identically. Vortex stretching requires multi-mode
interaction.

This is a STRONGER statement than any L^p bound improvement. It says
the bilinear form omega . S . omega has special cancellation for div-free
fields that is NOT captured by the L^p operator norm.

### The bilinear form estimate

The classical bound:

    |integral omega . S . omega dx| <= ||omega||_{L^3}^2 * ||S||_{L^3}
                                     <= C_3 ||omega||_{L^3}^3

The div-free structure gives omega . S_k . omega = 0 for each individual
mode k (single-mode orthogonality). This means the integrand has
CANCELLATION that the Holder inequality does not see.

This cancellation could in principle improve the bilinear estimate:

    |integral omega . S . omega dx| <= C' ||omega||_{L^3}^3

with C' < C_3. But proving this requires estimating the bilinear form
DIRECTLY, not going through ||S||_{L^3}.

This is the content of files 014, 044, and the "decorrelation" line
of research: the multi-mode interactions have random phases that
cause cancellation in the SUM, even though each term can be large.

### The honest assessment

The single-mode orthogonality proves omega . S . omega = 0 for individual
modes. But the CROSS-mode contributions omega_k . S_l . omega_m can have
either sign. The question is whether the sum over all triadic interactions
has enough cancellation to reduce the total below the CZ * ||omega||^3 bound.

This is a DIFFERENT question from improving the CZ constant. It is about
the bilinear form omega . S . omega having special structure on div-free
fields. And it is exactly the question addressed in files 014-044.

The status (from those files): the cancellation is OBSERVED numerically
but NOT proved analytically. The gap is formalizing the "random phases"
of triadic interactions.


---

## Conclusion

**All three approaches fail to prove ||S||_{L^p} <= (C-epsilon) ||omega||_{L^p}
for div-free fields.**

### Approach 1 (Fourier multiplier): FAILS
The div-free constraint forces omega_hat(k) into the plane perpendicular
to k. The strain multiplier m(k) achieves its MAXIMUM on this plane
(because strain comes from the cross product k x omega, which is maximized
when omega is perpendicular to k). The restricted multiplier norm equals
the unrestricted norm. Furthermore, planar div-free fields (omega = (0,0,f))
can approximate the CZ extremizers, showing the full CZ constant is achieved
by div-free fields.

### Approach 2 (Tracelessness): FAILS
tr(S) = 0 is automatic and already accounted for in the operator norm.
The tracelessness reduces the dimension of the codomain from 6 to 5,
but the CZ constant already reflects the true operator, not a hypothetical
extension to 6D outputs.

### Approach 3 (Betchov relation): FAILS
The Betchov identity relates integral(omega . S . omega) to integral(det S).
These are L^1-level integral constraints that do not constrain the L^p
operator norm ratio. The Betchov identity is an algebraic identity for
div-free fields, but it operates at the wrong level (integrals of nonlinear
forms vs. L^p norms of the operator).

### The root cause

The strain-vorticity operator T: omega -> S is defined VIA the div-free
structure (Biot-Savart). The "general CZ constant" for this operator
IS the constant on div-free fields. There is no meaningful "larger class"
to compare with:
- Non-div-free omega produce the same strain as their div-free projection
  (the irrotational part is invisible to curl^{-1}).
- The CZ constant for the specific operator T is already the optimal
  constant for div-free fields.

### What DOES work (for regularity)

The productive direction is not improving the CZ CONSTANT but rather
improving the BILINEAR ESTIMATE:

    integral omega . S . omega dx <= ??? * ||omega||_{L^3}^3

The single-mode orthogonality (omega_k . S_k . omega_k = 0) provides
genuine cancellation in this bilinear form that is NOT captured by the
CZ constant. This cancellation, if quantified, could yield

    integral omega . S . omega dx <= (C_3 - epsilon) ||omega||^3

even though ||S||_{L^3} = C_3 ||omega||_{L^3} (no improvement on the
operator norm level).

This is the difference between:
- OPERATOR NORM: sup ||T(omega)||/||omega|| (cannot be improved, as shown)
- BILINEAR FORM: sup integral omega . T(omega) . omega / ||omega||^3
  (CAN potentially be improved via single-mode orthogonality)

The bilinear form is what enters the enstrophy equation. The single-mode
orthogonality kills the diagonal terms omega_k . T_k(omega_k) . omega_k = 0,
leaving only cross-terms. If the cross-terms have sufficient phase
cancellation (the "decorrelation" conjecture from files 015-021),
the bilinear form bound improves even though the operator norm does not.

**This is where the next proof attempt should focus: quantifying the
cancellation in the bilinear form integral omega . S . omega dx,
not the operator norm ||S||_{L^p}/||omega||_{L^p}.**
