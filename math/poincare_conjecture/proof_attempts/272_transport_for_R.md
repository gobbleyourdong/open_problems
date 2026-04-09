---
source: Combined A+C — The transport equation for R is the final target
type: SYNTHESIS — both instances agree: proof must be dynamic
file: 272
date: 2026-03-29
---

## The Convergence

Instance A (files 180-190): NO static bound works. H_ωω > 0 requires
Euler evolution. Random/div-free/NS-structured sources all have ~43%
violations. Only EVOLVED NS has 7.5% (transient).

Instance C (files 260-271): Shell/energy methods give constant
improvements but not exponent improvements. Log Sobolev fails.
The Fourier lemma gives H_ωω > 0 (sign only, not magnitude).

Both instances conclude: **the proof must be DYNAMIC.**

## The Target: Transport Equation for R

Define R(x,t) = (ê·S²·ê - α²) / H_ωω at points where H_ωω > 0.

Equivalently: R = Var(λ under c) / H_ωω (alignment variance / pressure).

For the Hou-Li curvature: need R < 2 + α²/H_ωω (from file 270).

Simpler target: show R DECREASES along the Euler evolution when R > R*.

## Why R Decreases Under Euler Evolution

PHYSICAL ARGUMENT:
1. At t=0 (random IC): R > 1 at 43% of points. ω and S are uncorrelated.
2. Euler evolution creates the |ω|²/|S|² = 4 attractor (file 161).
3. The attractor aligns ω with the strain eigenvectors (file 154: e₃ → ω).
4. Alignment reduces Var = ê·S²·ê - α² (the numerator of R).
5. Simultaneously, z-variation in the source INCREASES (from stretching),
   making H_ωω larger (the denominator of R).
6. R decreases from both numerator decreasing AND denominator increasing.

MEASURED:
- Random IC: R > 1 at 43%.
- After evolution to t=0.1: R < 1 at 92.5%+ at the max.
- The transition happens over t ≈ 0.05 (a few eddy turnover times).

## What the Transport Equation Needs to Show

DR/Dt ≤ -c(R - R*) when R > R* (where R* < 2 + α²/H_ωω)

This is a CONTRACTION: the dynamics pull R toward R* exponentially.

The contraction rate c depends on:
- The eigenvector tilting rate (file 173: 15:1 dominance → strong contraction)
- The H_ωω growth rate (file 177: H_ωω increases with |ω|)
- The |ω|²/|S|² convergence rate (file 161: attractor at 4)

## The Formal Challenge

R = (ê·S²·ê - α²) / H_ωω. Computing DR/Dt:

DR/Dt = [D(ê·S²·ê)/Dt - 2αDα/Dt] / H_ωω - R × DH_ωω/Dt / H_ωω

Each term involves the FULL nonlinear dynamics:
- D(ê·S²·ê)/Dt: requires fourth-order derivatives of u
- Dα/Dt: known (= ê·S²·ê - 2α² - H_ωω)
- DH_ωω/Dt: requires the evolution of the pressure Hessian

The pressure Hessian evolution is the HARDEST part:
DH/Dt involves derivatives of the strain equation,
which involves the pressure Hessian itself (circular).

This CIRCULARITY is why the problem is so hard. The pressure
feeds back into the strain which feeds back into the pressure.

## Where We Are

~200 proof files across three instances. The problem has been reduced to:

**Prove that the Euler dynamics contracts the ratio R = Var/H_ωω
toward a value that makes the Hou-Li curvature positive.**

This is a STABILITY question: is the attractor R < R* stable under
Euler evolution? The data overwhelmingly says YES. The proof requires
deriving and bounding the transport equation for R.

The Millennium Prize is in closing this stability estimate.

## 272. Both instances converge. Transport equation for R is the target.
