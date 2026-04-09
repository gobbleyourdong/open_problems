# NS Blowup — Status Report Mar 23, 2026

## The Question
Does the Γ rebound (stretching retakes the lead after viscosity briefly dominates) persist at high resolution, or is it a numerical artifact?

## The Verdict So Far: INCONCLUSIVE, LEANING TOWARD NO REBOUND

### What happened
- **Nr=64**: Γ drops to 0.123, rebounds to 0.99. α (strain from Poisson) never stops growing. Looks like blowup.
- **Nr=128 (Spark)**: Γ drops to 0.077, partial rebound to 0.096 — but UNDER-RESOLVED (spectral 0.12). Inconclusive.
- **Nr=256 (H200)**: Γ drops past 0.096 (20K run endpoint) and keeps going. α peaked at 42 and is now DECLINING to 37. Spectral pristine (0.0006). **The Poisson amplification mechanism is NOT engaging at this resolution.**

### The critical divergence: α trajectory
| Resolution | α at Γ≈0.19 | α behavior in trough | Rebound? |
|------------|-------------|---------------------|----------|
| Nr=64 | 58.5 | Monotonically increasing → 118 | YES |
| Nr=256 | 42.0 | Peaked, now declining to 37 | UNKNOWN (40K running) |

At Nr=64, α was 40% higher and climbing. At Nr=256, the resolved viscous dissipation is eating the strain that Poisson coupling generates.

### What this means for the proof
If Γ→0 at Nr=256:
- The Nr=64 rebound was a resolution artifact (under-resolved viscous structure)
- For THIS IC (Luo-Hou) at THIS ν (1e-4), viscosity wins on Spark's ν_c bracket
- Does NOT mean global regularity — could mean ν=1e-4 is above ν_c at true resolution
- Next step: try lower ν or the Hou 2022 (interior) IC

If Γ floors and rebounds at Nr=256:
- The mechanism is real, just weaker (α peaks at ~80 instead of 118)
- α declining might reverse — the Poisson spring loads more slowly at higher resolution
- The structural proof path (wider core → stronger strain) survives but with tighter margins

### Leray-rescaled findings (THESE ARE SOLID regardless of rebound)
- Ω̃ = (T*-t)·|ω| ≈ 10-12 through entire cycle → approximately self-similar in Leray coords
- γ = 0.965 (|ω| ~ (T*-t)^{-0.965}) → nearly Leray scaling (γ=1)
- P̃ = (T*-t)²·νP is nearly constant in trough → dissipation is a "wall" in Leray frame
- S̃ = (T*-t)²·S oscillates above P̃ → stretching always leads (at Nr=64)

### Spectral rank (ENCOURAGING for CAP tractability)
- Step 5K (Γ=0.56): 99% in 26 modes, 99.9% in 47 modes
- Step 10K (Γ=0.17): 99% in 33 modes, 99.9% in 232 modes
- First 50 modes capture 99.4% even in the trough
- Chen-Hou used rank<50 → our problem is same complexity
- BUT: 99.9% rank exploded 47→232 in trough → fine viscous tail growing

### H200 time remaining
- ~8 hrs on RunPod ($50 budget)
- 40K run at step ~11K, reaching new territory at step 20K (~2 hrs)
- New territory: steps 20K-40K with core width diagnostic + field checkpoints every 5K
- Will capture 20K steps of NEW data (Γ ≈ 0.096 → ???)

### Files
| Path | What |
|------|------|
| `ns_blowup/results/h200_sync/` | All H200 data synced to Spark |
| `ns_blowup/results/core_width_nr64.json` | Nr=64 core width diagnostic (S, νP, α, R) |
| `ns_blowup/results/leray_transform_nr64.json` | Leray coordinate analysis |
| `ns_blowup/results/leray_enstrophy_balance.json` | S̃/P̃ balance analysis |
| `ns_blowup/results/spectral_trend_nr256.json` | Spectral degradation prediction |
| `ns_blowup/results/gamma_asymptotic_nr256.json` | Γ→0 vs floor fit analysis |
| `ns_blowup/results/field_snapshot_step5000.json` | Spectral rank at step 5K |
| `ns_blowup/PROOF_ARSENAL.md` | 22-paper curated reference |
| `ns_blowup/FLUID_GOD_manifest.md` | 73-paper full manifest |

### Next moves (regardless of outcome)
1. Wait for 40K to reach step 20K+ (~2 hrs) → see if Γ keeps dropping or floors
2. If Γ→0: Try Hou 2022 IC (interior blowup, r=0) — this IC showed blowup at ALL ν in A100 data
3. If Γ floors: Extract Leray-rescaled profile from field checkpoints, run PySR on rescaled data
4. Either way: the Leray-rescaled analysis framework + spectral rank data is reusable infrastructure
