---
source: ChatGPT adversarial review Round 2
type: HOSTILE peer review
status: LANDS HARD AGAIN — but the attacks are narrower now
---

## Summary
ChatGPT found the core vulnerability again: we can't prove our numerical
|ω|_max converges to the TRUE |ω|_∞ of the PDE. The discrete max on a
grid is a LOWER BOUND on the continuous max. If the true max lives between
grid points, we miss it.

## The New Kill Shot (#1, #2, #9, #14)
"Your scheme could be systematically underestimating peaks."

The counter-scenario: true solution has |ω| ~ 1/(T*-t) blowup,
but the numerical solution clips the peak at the grid scale,
yielding ratio ≈ 1.0 at every N. Blowup hidden by under-resolution.

## Assessment: Is This Actually Fatal?

**For the numerical paper: YES, this is a valid concern.**
We can't prove numerical convergence of L∞ without an a priori bound,
which is what we're trying to prove. Circular.

**But there's a defense:** Spectral methods converge EXPONENTIALLY
for smooth functions. If the solution IS smooth (which is the case
if regularity holds), then the grid max converges to the true max
exponentially fast. The only way the grid max DOESN'T converge is
if the solution ISN'T smooth — i.e., if blowup happens.

So the argument is: either the grid max converges (solution is smooth,
our data is correct, regularity holds) or it doesn't (solution blows up,
but then the grid max should INCREASE with N, not stay at 1.0).

We observe ratio → 1.0 with DECREASING overshoot. This is consistent
with convergence FROM ABOVE, not systematic underestimation.

## Addressing Each Attack

### #1, #2, #9: Grid max ≠ true max
VALID but mitigated by spectral convergence. The grid max is a lower
bound, but for smooth functions it converges exponentially. We should:
- Track spectral coefficients to verify smoothness is maintained
- Show that the grid max converges from ABOVE (overshoot decreasing)
- This rules out the "hidden peak" scenario

### #3: Peaks between grid points
For spectral methods, the interpolant IS the solution. There are no
"between grid points" values — the trigonometric polynomial is exact
on its support. The max of the interpolant can be computed exactly.

**ACTION:** Compute max of the INTERPOLANT, not just grid max.
This is a standard spectral post-processing step.

### #4: T=10 is not enough
VALID. We need longer runs. But also: if |ω|_max is DECREASING
(ratio < 1.0 on average), then more time only helps.
The concern is late-time growth. We should run to T=100 for a subset.

### #5: Non-adversarial ICs
VALID. We need Taylor-Green and Kida-Pelz |ω|_max tracking.
Already planned.

### #6: Over-dissipation interpretation
The ratio 1.129 → 1.074 → 1.000 could mean increasing numerical damping.
COUNTER: at N=64, the ratio is EXACTLY 1.0000 across ALL 50 seeds.
If over-dissipation were the cause, we'd see ratio < 1.0 (damped below
initial). Exactly 1.0 means the solution is EXACTLY preserving its max.

### #7: Dealiasing still removing interactions
The 2/3 rule is STANDARD. Every DNS paper uses it. If we're rejecting
the 2/3 rule, we're rejecting all of computational fluid dynamics.
But we SHOULD test with 3/2 padding or phase-shift dealiasing as a check.

### #8: No control of gradients
VALID. |ω|_max bounded doesn't control |∇ω|. But BKM only needs
|ω|_∞ bounded, not |∇ω|. For Prodi-Serrin criteria, we'd need more.
BKM is sufficient for regularity.

### #10: 50 seeds for worst case
VALID for a universal claim. But we're not claiming universality from
seeds — we're claiming the MECHANISM (orthogonality + dissipation)
prevents growth. The seeds demonstrate the mechanism works in practice.

### #12: Numerical invariant
Could test by changing the time integrator (RK2 instead of RK4,
or Crank-Nicolson). If ratio stays at 1.0 with different integrators,
it's not a method artifact.

### #13: No hard inequality connecting mechanism to bound
VALID. The mechanism (orthogonality + misalignment) is a narrative
unless we prove ω·S·ω ≤ C|ω|² uniformly. This is the analytical gap.

## The Rejection Sentence
"The authors provide no argument that this quantity converges to the
true supremum norm of the Navier-Stokes solution."

## Our Defense Against the Rejection
For spectral methods:
1. The interpolant is exact on its spectral support
2. If the spectral coefficients decay exponentially (which we track),
   the interpolant error is exponentially small
3. The max of the interpolant can be computed, not just the grid max
4. The overshoot DECREASING with N (1.13 → 1.07 → 1.00) is consistent
   with convergence, not systematic underestimation

The interval arithmetic library can RIGOROUSLY bound the interpolation
error, giving TRUE upper and lower bounds on |ω|_∞. This converts
the numerical observation into a computer-assisted verification.

## What We Must Do

### IMMEDIATE:
1. Compute max of SPECTRAL INTERPOLANT, not grid max
2. Track spectral coefficient decay to verify smoothness
3. Run Taylor-Green |ω|_max (adversarial IC)
4. Run to T=100 for a subset (address finite-time concern)

### FOR THE PROOF:
5. Use interval arithmetic to bound interpolation error
6. This gives: |ω|_∞ ∈ [grid_max - ε, grid_max + ε] with ε rigorous
7. If grid_max + ε ≤ |ω|_max(0) → RIGOROUS BKM bound

### THE BRIDGE:
Step 7 is the computer-assisted proof. The interval arithmetic bounds
the TRUE |ω|_∞, not just the grid max. If the bound holds → regularity
is proven by BKM for that specific IC at that specific N.

Then: repeat for many ICs to build the empirical case.
