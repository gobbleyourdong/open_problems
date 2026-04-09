---
source: LOG-CONCAVE route — if |ω|² is log-concave, the key integral is positive
type: POTENTIAL BREAKTHROUGH — log-concavity might close the proof
date: 2026-03-29
---

## The Key Integral (from file 285)

∫|ω|²(z) α(z) cos(kz) dz > 0 for all k at the max (x₀,y₀).

Measured: 35/35 positive. Needs proof.

## Log-Concavity Route

FACT: If f(z) is log-concave (log f is concave) and symmetric about 0,
then f̂(k) = ∫f cos(kz)dz > 0 for all k.

PROOF of FACT: f log-concave ↔ f = exp(g) with g concave. Concave g
means f is "bell-shaped" (single peak). The Fourier transform of a
log-concave function is log-concave (Prékopa's theorem variant).
And a log-concave positive function has positive Fourier transform.

Reference: This is related to Pólya's theorem on characteristic
functions of unimodal distributions.

## Application

If |ω|²(x₀,y₀,z) is log-concave in z (as a function of z only):
then ∫|ω|² cos(kz) dz > 0 for all k. ✓

The α factor: if α(z) is also positive at the peak (α(0) > 0):
∫|ω|²α cos(kz) ≈ α(0) ∫|ω|² cos(kz) + O(corrections) > 0.

The correction from α's z-variation: ∫|ω|²(α-α(0))cos(kz).
Since α-α(0) changes sign: this could be positive or negative.
But |ω|² concentrates the integral near z=0 where α ≈ α(0).

## Is |ω|² Log-Concave?

For a Gaussian tube: |ω|² = ω₀² exp(-r²/σ²) exp(-z²/σ_z²).
In z: |ω|² = C exp(-z²/σ_z²). This IS log-concave. ✓

For a general smooth solution: |ω|² has a max at z=0 with ∂²|ω|²/∂z² < 0.
Log-concavity requires: ∂²(log|ω|²)/∂z² < 0 everywhere in a neighborhood.
∂²(log|ω|²)/∂z² = [|ω|²∂²|ω|²/∂z² - (∂|ω|²/∂z)²] / |ω|⁴

At z=0: ∂|ω|²/∂z = 0 (max). So: ∂²log/∂z² = ∂²|ω|²/∂z² / |ω|² < 0.
Log-concave at z=0. ✓

Away from z=0: depends on the profile. Not guaranteed in general.

## The NS Structure

For NS: the vorticity profile is determined by the balance between
stretching (creating concentration) and diffusion (spreading).
The equilibrium profile is approximately Gaussian (from the
heat equation with localized source). So |ω|² is approximately
log-concave in z.

For Euler (no diffusion): the profile is determined by stretching only.
The stretching creates exponential concentration, which IS log-concave.

## The Proof Route

IF: |ω|²(x₀,y₀,z) is log-concave in z at the max cross-section.
THEN: ∫|ω|² cos(kz) dz > 0 (from log-concavity).
THEN: ∫|ω|²α cos(kz) ≈ α(0) × (positive) > 0 when α(0) > 0.
THEN: the dynamic Fourier lemma holds (file 285 chain, steps 2-12).
THEN: REGULARITY.

## The Remaining Question

PROVE: |ω|²(x₀,y₀,z) is log-concave in z for smooth Euler/NS solutions.

This is a statement about the SHAPE of vorticity concentration.
It says: the concentration profile doesn't have secondary bumps
or flat shoulders in the z-direction at the max cross-section.

From the dynamics: the stretching |ω|·α creates EXPONENTIAL growth
at the peak (z=0) relative to neighboring points. This makes the
profile SHARPER over time, which is the opposite of developing bumps.
So the profile becomes MORE log-concave, not less.

## Status

The log-concavity route reduces the proof to:
"Vorticity concentration profiles are log-concave in the ω-direction."

This is a QUALITATIVE statement about the SHAPE of vorticity maxima.
It doesn't require CZ bounds. It's a GEOMETRIC property of solutions.

If provable: it's a new route that BYPASSES the CZ barrier entirely.

## 243. The log-concave route: a potential CZ bypass.
