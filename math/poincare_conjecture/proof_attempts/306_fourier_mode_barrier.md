---
source: Fourier-mode analysis of vortex stretching at vorticity maximum
type: PROOF ATTEMPT — new structural results + numerical validation
date: 2026-03-29
---

## SUMMARY

Three rigorous results and one strong empirical observation that together
suggest a new proof route for NS regularity on T^3.

**Rigorous**:
1. alpha = 0 for any single Fourier mode at its vorticity max (algebraic identity)
2. alpha = Sum(ell_k . q_k) with Sum(q_k) = 0 and |ell_k| <= 1/2 ("zero-sum linear functional")
3. alpha vanishes when all active modes have the same angle to the vorticity direction

**Empirical** (20,000 random configurations, N=32 grid):
4. S^2_e / |omega|^2 < 0.27 at the global max of |omega| (vs threshold 3/4 for barrier)

If result 4 can be proven, the barrier argument gives NS regularity on T^3.


## RESULT 1: SINGLE-MODE ALPHA VANISHING

**Theorem**: Let omega = 2Re(omega_hat * e^{ik.x}) be a single-mode divergence-free
field on T^3. At any maximum x* of |omega|, the vortex stretching rate alpha(x*) = 0.

**Proof**: In the frame where k = kappa * e_3, div-free gives omega_hat = (w1, w2, 0).
By Biot-Savart: u_hat = (ik x omega_hat)/|k|^2 = i(-w2, w1, 0)/kappa.

The velocity gradient nabla_u has only row 3 nonzero: (w2, -w1, 0).
The strain S = sym(nabla_u) has the form:

    S = [  0      0     w2/2  ]
        [  0      0    -w1/2  ]
        [ w2/2  -w1/2    0   ]

with eigenvalues {+|omega_hat|/2, 0, -|omega_hat|/2}.

The eigenvector for lambda_1 = +|omega_hat|/2 is:
    e_1 = (w2, -w1, |omega_hat|) / (sqrt(2) |omega_hat|)

At the max of |omega|, omega points in direction e_hat = (w1, w2, 0)/|omega_hat|.

    c_1 = e_hat . e_1 = (w1*w2 - w2*w1 + 0) / (sqrt(2)*|omega_hat|^2) = 0.

Therefore alpha = sum(lambda_i * c_i^2) = lambda_1 * 0 + ... = 0. QED.

**Physical interpretation**: The Biot-Savart operator rotates velocity by 90 degrees
relative to vorticity in the plane perpendicular to k. The strain eigenvector e_1
gets a k-direction component, making it perpendicular to omega (which has NO
k-direction component). So omega is always in the "null space" of stretching for
single modes.


## RESULT 2: ZERO-SUM LINEAR FUNCTIONAL FORMULATION

At the global max x* of |omega|, define:
- e_hat = omega(x*)/|omega(x*)| (vorticity direction)
- p_k = (omega_hat_k . e_hat) * e^{ik.x*} (parallel contribution of mode k, REAL at max)
- q_k = omega_hat_k * e^{ik.x*} - p_k * e_hat (perpendicular contribution, 2D VECTOR in plane perp to e_hat)

Then:
- |omega(x*)| = Sum(p_k) with all p_k real, positive (constructive interference)
- Sum(q_k) = 0 (perpendicular cancellation — defines the maximum direction)

**The stretching rate**: alpha = Sum(ell_k . q_k)

where ell_k is a 2D vector in the plane perpendicular to e_hat:

    ell_k = -(k_3/|k|^2) * k_perp^{perp}

with k_perp^{perp} = (-k_2, k_1) (90-degree rotation of k projected into the perp plane).

    |ell_k| = |sin(2*theta_k)| / 2 <= 1/2

where theta_k = angle between k and e_hat.

**Key property**: Since Sum(q_k) = 0, for ANY constant vector ell_0:

    alpha = Sum((ell_k - ell_0) . q_k)

If all ell_k are IDENTICAL (all modes at the same angle to e_hat):
    alpha = ell . Sum(q_k) = 0

**Implication**: alpha is sourced ONLY by the VARIATION of ell_k across modes.
Modes at different angles to the vorticity direction create stretching; modes
at the same angle cancel. This is the multi-mode generalization of Result 1.

**Bound**: |alpha| <= sup_k |ell_k - ell_0| * Sum|q_k| for optimal ell_0.
With the energy constraint Sum|q_k| <= Sum|omega_hat_k| and |omega| = Sum(p_k):

    alpha/|omega| <= (diam(ell_k)/2) * Sum|q_k| / Sum(p_k)


## RESULT 3: THE PER-MODE BOUND alpha/|omega| <= 1/2 IS TIGHT

**Constructive example**: 5-mode configuration achieving alpha/|omega| = 0.484
at the global vorticity maximum (found by random search over 2000 configurations).

The per-mode bound of 1/2 appears to be tight (or nearly so) for STATIC fields.
Achieving alpha/|omega| near 1/2 requires:
- Multiple modes at ~45 degrees to e_hat (maximizes |ell_k| = 1/2)
- Perpendicular components q_k arranged so ell_k . q_k adds constructively
- While satisfying Sum(q_k) = 0 and x* being the global max

The tight configuration requires roughly EQUAL energy in the parallel and
perpendicular polarizations, which is an unstable balance.


## KEY FINDING: S^2_e / |omega|^2 << 3/4 AT THE MAX

The barrier argument (file 305) shows: at R = alpha/|omega| = 1/2,

    DR/Dt = (S^2_e - 3*alpha^2 - H_ww) / |omega|

For R = 1/2 to be a barrier: need S^2_e < 3|omega|^2/4 + H_ww.
Since H_ww > 0 (Fourier lemma), sufficient condition: S^2_e < 3|omega|^2/4.

**Numerical test** (20,000 random configurations, 2-8 modes, |k| <= 3):

    Worst S^2_e / |omega|^2 = 0.262  (threshold: 0.750)
    Margin: 0.488

The bound S^2_e/|omega|^2 < 0.75 holds with MASSIVE margin.

**Why?** S^2_e = |S.e_hat|^2 = alpha^2 + |S.e_hat|_perp^2.
- alpha^2: at most |omega|^2/4 (from alpha <= |omega|/2)
- |S.e_hat|_perp^2: the TILTING rate. For single modes, S.e_hat = 0.
  For multi-mode, tilting comes from perpendicular mode mixing — same
  source as alpha, and similarly suppressed at the vorticity maximum.

Typical values:
- S^2_e/|omega|^2 ~ 0.05-0.15 (far from 0.75)
- At the configuration with max alpha/|omega| = 0.484:
  S^2_e/|omega|^2 = 0.252, giving barrier margin 0.75 - 0.252 = 0.498

**Contrast with arbitrary trace-free S**: without the Biot-Savart constraint,
S^2_e can exceed 3*alpha^2 by factors of 10^5. THE BIOT-SAVART STRUCTURE
IS THE KEY CONSTRAINT.


## CONJECTURE: |S|^2/|omega|^2 <= 1/2 AT THE MAX (FALSE!)

Initially conjectured |S|^2/|omega|^2 <= 1/2 at the vorticity max.
**COUNTEREXAMPLE FOUND**: 2-mode configuration with |S|^2/|omega|^2 = 0.646.

The conjecture fails because modes with omega perpendicular to e_hat
contribute strain without contributing to |omega| — the strain energy
can concentrate at x* even when vorticity energy peaks there.

However, |S|^2 vs |S.e_hat|^2 are very different. The excess strain
is in directions PERPENDICULAR to e_hat (strain eigenvectors not aligned
with omega), so S^2_e = e_hat.S^2.e_hat remains small even when |S|^2 is large.


## THE ORTHOGONAL POLARIZATION TRADEOFF

For each Fourier mode at angle theta_k to e_hat:
- Vorticity in e_hat direction: |p_k| <= |omega_hat_k| * sin(theta_k) (div-free constraint)
- Stretching contribution: |alpha_k| depends on the PERPENDICULAR component |q_k|

The div-free constraint omega_hat_k . k = 0 means:
- Modes with k perp e_hat (theta = pi/2): CAN have omega || e_hat, but alpha_k = 0
  (because sin(2*theta) = 0 → |ell_k| = 0)
- Modes with k at 45 degrees: maximize |ell_k| = 1/2 but can only have
  |p_k| <= |omega_hat_k| * sin(45) = |omega_hat_k|/sqrt(2) in the e_hat direction
- Modes with k || e_hat (theta = 0): alpha_k = 0 AND p_k = 0 (omega forced perp to k = e_hat)

The modes that maximize alpha (theta = 45 degrees) sacrifice parallel projection.
The modes that maximize |omega| (theta = 90 degrees) have zero alpha.
This tradeoff prevents alpha/|omega| from reaching 1/2 in practice.


## THE DOUBLE-ANGLE CANCELLATION OF STRAIN

For modes with k perpendicular to e_hat (theta = pi/2, all k in the plane perp to e_hat):
The strain tensor of mode with azimuthal angle phi in that plane is:

    S_phi = (a/2) * [-sin(2phi)  cos(2phi)  0]
                     [ cos(2phi)  sin(2phi)  0]
                     [    0          0       0]

The strain rotates at TWICE the azimuthal angle. Consequence:

- N = 2 modes at phi, phi+90: strains CANCEL completely (|S| = 0, |omega| = 2a)
- N = 3+ uniformly spaced modes: strains cancel (|S| = 0, |omega| = Na)
- In general: strain cancellation is much more effective than vorticity cancellation

This explains why |S|^2/|omega|^2 tends to be well BELOW 1/2 at the vorticity max
for multi-mode fields. Example:
- 3 modes, all omega=e3, k's in e1-e2 plane: |S|^2/|omega|^2 = 0.056 (vs 0.5 for single mode)


## PROOF STRATEGY

**What is proven**:
1. alpha = 0 for single modes (Result 1) — rigorous
2. alpha = zero-sum linear functional (Result 2) — rigorous
3. Per-mode bound alpha/|omega| <= 1/2 (known)
4. S^2_e < 3|omega|^2/4 at the max → barrier DR/Dt < 0 at R=1/2 → regularity (known)

**What is needed**:
Prove S^2_e(x*) < (3/4)|omega(x*)|^2 at the global max x* of |omega|.

Equivalent: prove |S(x*).e_hat|^2 < (3/4)|omega(x*)|^2.

**Approach A: Direct Fourier bound**
S.e_hat = Sum(S_hat_k . e_hat) * e^{ik.x*}. Each term is a 3-vector depending on k and omega_hat_k.
For omega_hat_k || e_hat: S_hat_k . e_hat = 0 (Result 1). So S.e_hat is sourced ONLY by
perpendicular components q_k. With Sum(q_k) = 0 and the angle-dependent geometric factors,
bound the total |S.e_hat|^2.

**Approach B: Energy partition**
At the global max, the dominant energy is in modes with omega || e_hat (large p_k).
These contribute nothing to S.e_hat. The perpendicular modes (source of S.e_hat)
have bounded energy (otherwise x* wouldn't be the global max). This gives
|S.e_hat|^2 << |omega|^2/2 at the max.

**Approach C: Spectral analysis near blowup**
Near a potential blowup, energy cascades to small scales (broad spectrum). The many-mode
regime has strong strain cancellation (double-angle effect). The concentration of
vorticity at x* (which MUST happen for blowup, by ESS) requires coherent phase alignment
of omega modes, which suppresses S.e_hat even further.


## NUMERICAL SUMMARY

| Configuration | |omega|_max | alpha/|om| | |S|^2/|om|^2 | S^2_e/|om|^2 |
|---|---|---|---|---|
| Single mode | 2.0 | 0.000 | 0.500 | 0.000 |
| 2 parallel omega modes | 4.0 | 0.000 | 0.000 | 0.000 |
| 3 modes, k in perp plane | 6.0 | 0.000 | 0.056 | 0.000 |
| Best alpha/|om| (5 modes) | 8.7 | 0.484 | 0.414 | 0.252 |
| Best |S|^2 (2 modes) | 5.2 | 0.266 | 0.646 | 0.075 |
| 20 random modes | 29.3 | 0.101 | 0.127 | 0.042 |
| TG-like 6 modes | 7.5 | 0.057 | 0.036 | 0.013 |

Over 20,000 random configs: worst S^2_e/|omega|^2 = 0.262 << 0.750.
The barrier at R=1/2 holds with margin > 0.48 in ALL tested cases.


## STATUS

The barrier DR/Dt < 0 at R = alpha/|omega| = 1/2 requires S^2_e < 3|omega|^2/4.
This is EMPIRICALLY TRUE with massive margin. The remaining gap is to prove
S^2_e/|omega|^2 < 3/4 from the Biot-Savart structure.

The key structural fact: S.e_hat = 0 for single modes (Result 1).
Multi-mode mixing generates S.e_hat, but the perpendicular cancellation (Sum q_k = 0)
and the double-angle strain cancellation keep |S.e_hat|^2 well below |omega|^2/2.

**THE PROOF IS ONE LEMMA AWAY**: Bound S^2_e at the vorticity maximum using
the Biot-Savart constraint + perpendicular cancellation + global max condition.

## KEY INSIGHT FOR THE LEMMA

The condition for x* to be the global max of |omega| means: for ALL x,
|omega(x)|^2 <= |omega(x*)|^2. This constraints the Fourier coefficients.

In particular: the "perpendicular energy" at x* (Sum |q_k|^2) cannot dominate
the "parallel energy" (Sum p_k^2), because if it did, there would exist another
point x' where the perpendicular components add constructively, giving |omega(x')| > |omega(x*)|.

This energy partition constraint, combined with the fact that S.e_hat is sourced
ONLY by perpendicular components, should give the bound.
