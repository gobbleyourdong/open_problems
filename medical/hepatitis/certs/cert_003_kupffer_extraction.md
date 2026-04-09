# cert_003_kupffer_extraction

**Claim:** Kupffer cells, together with hepatocytes, extract approximately 85–95% of circulating viral/particulate material per hepatic pass under normal physiological conditions.

## Status: SUPPORTED (with important caveats on particle type and saturation)

## Evidence

### Primary source
Bilzer M, Roggel F, Gerbes AL.
"Role of Kupffer cells in host defense and liver disease."
*Liver International* 2006; 26(10):1175–1186. doi:10.1111/j.1478-3231.2006.01342.x

**Key data from Bilzer 2006:**
- Kupffer cells constitute ~80–90% of all tissue-fixed macrophages in the body
- Estimated 3×10^9 Kupffer cells in adult human liver
- Primary function: phagocytosis of particulate matter, bacteria, endotoxin, and opsonised particles from portal blood
- Extraction efficiency for latex beads and bacteria: 85–99% per pass reported in animal models
- Colloidal carbon particle extraction: >95% per pass (classic liver reticuloendothelial function assay)

### Hepatic extraction of viruses and particles — supporting literature

**Smedsrød B et al.** Scand J Gastroenterol 1990; 25(3):261–271.
- Sinusoidal endothelial cells (LSEC) together with Kupffer cells clear colloidal particles efficiently
- LSEC contributes receptor-mediated endocytosis; Kupffer cells contribute Fc/complement receptor phagocytosis
- Combined first-pass extraction of opsonised particles: ~85–95%

**Crispe IN.** "The liver as a lymphoid organ." *Annual Review of Immunology* 2009; 27:147–163.
- Liver sinusoidal architecture designed for maximal contact between blood-borne antigens and resident immune cells
- Sinusoidal transit time 1–2 seconds provides sufficient contact time for phagocytosis at normal portal flow

**Vollmar B, Menger MD.** "The hepatic microcirculation: mechanistic contributions and therapeutic targets in liver injury and repair." *Physiological Reviews* 2009; 89(4):1269–1339.
- Portal blood flow ~1.0–1.2 L/min (can reach 1.5 L/min)
- Sinusoidal diameter: 5–10 µm — forces cells and particles into close contact with lining cells
- This architecture is the structural basis for high extraction efficiency

### Quantitative parameterisation

| Condition | Kupffer activation | Estimated E_kupffer | Basis |
|-----------|-------------------|--------------------|----|
| Healthy adult | 1.0 (baseline) | 85–95% | Bilzer 2006, Smedsrød 1990 |
| Kupffer activation (Vit D, IFN) | 1.5–2.5× | >95% | Macrophage activation literature |
| Fluoxetine (Sigma-1 receptor) | ~2× | ~95% | Model estimate (Kupffer SERT/Sig1R expression) |
| NAFLD/NASH | 0.4–0.6× | 50–70% | Vidyarthi 2020 (NAFLD model) |
| Alcohol (chronic) | 0.3–0.5× | 40–65% | Gao 2019 (Kupffer depletion) |
| Neonatal (immature) | 0.3–0.4× | 30–55% | Extrapolated from developmental data |
| Overwhelmed (very high viral load) | 1.0 (saturated) | drops to 50–70% | Michaelis-Menten saturation |

### Caveat: Non-enveloped virus vs opsonised particles
CVB is non-enveloped; complement fixation is less efficient than for enveloped viruses.
Without anti-CVB IgG: extraction efficiency likely lower end (85–88%).
With anti-CVB IgG (IVIG or post-infection): IgG-opsonised CVB cleared via FcγR → efficiency rises toward 92–98%.
This is the mechanistic basis for why IVIG enhances clearance in neonatal CVB sepsis.

## Model parameters used in kupffer_extraction_model.py
- Kupffer cell count: 3.0×10^9
- Vmax (saturation): 25 particles/cell/min
- KM (half-saturation): 1.0×10^5 particles/mL portal blood
- Baseline activation: 1.0 → produces 85–95% extraction at low-to-moderate portal loads
- Fluoxetine activation: 2.2 → produces >95% even at moderate loads

## Confidence: MODERATE-HIGH
The 85–95% figure is well-established for particulate matter and bacteria. Direct measurement for CVB specifically is not available in humans. The value is extrapolated from Kupffer cell particle extraction studies plus in vitro viral phagocytosis data. The saturation kinetics (Michaelis-Menten) are model assumptions calibrated to produce physiologically plausible steady-state systemic viremia levels.
