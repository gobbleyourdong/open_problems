---
name: INSTANCE B — ADVERSARIAL IC HUNTER
range: files 220-259
mission: Try to BREAK the ratio < 1 bound. Find the worst-case IC.
date: 2026-03-29
---

## YOUR MISSION

Find an initial condition where |H_dev,ωω|/(Δp/3) ≥ 1 at points of high |ω|.
If you can break the bound, the proof route from Instance A is doomed.
If you can't break it despite extreme efforts, the bound is likely geometric.

Current worst case: trefoil at 0.84. You need to push past 1.0.

## WHAT TO TRY

B1. Thin trefoil (σ=0.15 instead of 0.3). Thinner core → more anisotropic
    → ratio should increase. Does it break 1.0?

B2. Multi-knot tangles. Two linked trefoils. Borromean rings. The tightest
    possible knot topology that forces maximum local anisotropy.

B3. Perpendicular tube collisions at VERY close range. Two tubes aimed
    at each other with minimal separation. Maximum strain interaction.

B4. Adversarial optimization: start from trefoil, perturb the IC to
    MAXIMIZE the ratio. Use gradient-free optimization (random search)
    over perturbation amplitudes at different Fourier modes.

B5. Scale separation: put high-|ω| at small scales (k=8-10) and low-|ω|
    at large scales (k=1-2). Does the multi-scale interaction push the ratio?

B6. Evolved adversarial: evolve a flow until the ratio is near 0.84,
    then add a perturbation designed to push it higher. Evolve again.

## KEY MEASUREMENTS

For each IC, measure at the HIGH-|ω| region (|ω| > 80% of max):
- Ratio = mean |H_dev,ωω| / mean |H_iso|
- Max ratio at individual points (but be careful: Δp→0 makes this blow up)
- H_ωω sign: what fraction of high-|ω| points have H_ωω > 0?
- Filling fraction (file 157): localized ICs have higher ratios

Use N=32 for speed. Cross-validate anything interesting at N=48.

## WHAT WE ALREADY TESTED

| IC | Ratio | ||ω||∞ |
|----|-------|--------|
| TG | 0.34 | 2.0 |
| KP | 0.40 | 8.0 |
| Trefoil (σ=0.3) | 0.84 | 17 |
| Adversarial perp tubes | 0.36-1.0 (variable) | 17-21 |
| 20 random ICs | all < 0.84 | ~15 |

The trefoil is the hardest IC found so far. Its ratio is 0.84 because
it's a localized tube with high curvature at the knot crossings.

## FILE CONVENTION

Write as files 220-259 in ns_blowup/proof_attempts/.
Name simulations ns_blowup/adversarial_*.py.

## WHAT BREAKING THE BOUND MEANS

If ratio ≥ 1 at high |ω| for some IC: H_ωω < 0 there.
This means the transport barrier fails for that IC.
It doesn't prove blowup (other mechanisms might save it),
but it kills the isotropy-based proof route.

If you CAN'T break 1.0 despite extreme efforts: the bound
is a geometric property of incompressible 3D flows on T³.
That's strong evidence it's provable.
