"""
cardiac_cascade_timing.py
=========================
Quantitative time constants for the CVB cardiac cascade:
from viral entry to fibrosis and DCM onset.

All values are from published literature cited inline.

References:
  - Badorff et al. 1999 (Nat Med) — dystrophin loss Western blot 24-48h
  - Badorff et al. 2000 (J Clin Invest) — 2A protease onset 2-4h
  - Kandolf et al. 1985 (PNAS) — CVB3 replication kinetics in cardiomyocytes
  - Martino et al. 1994 (Circulation) — NK recruitment day 3
  - Opavsky et al. 1999 (JCI) — CD8 infiltration day 5-7
  - Kawai 1999 (Jpn Circ J) — peak morbidity day 7-9
  - Pauschinger et al. 2000 — fibrosis onset day 10-14
  - Callon et al. 2022 (preprint/Nat Comm) — TD mutant detection from day 3
  - Knowlton et al. 1996 — CVB3 burst size
  - Coyne & Bergelson 2006 (Cell) — CAR internalization kinetics
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import os

# ============================================================
# SECTION 1: TIME CONSTANTS TABLE
# ============================================================

# All times in hours post-infection (hpi)
CASCADE_EVENTS = [
    # (event_name, t_start_h, t_peak_h, t_end_h, category, color, ref)
    # -------- VIRAL ENTRY & REPLICATION --------
    ("CAR binding / endocytosis",       0,    0.5,    1.0,   "viral",   "#e74c3c",
     "Bergelson 1997 (Science)"),

    ("CAR internalization (cell locked in)",  2,    3.0,    4.0,   "viral",   "#c0392b",
     "Coyne & Bergelson 2006 (Cell); t½ ~2-4h"),

    ("Genome release + translation",    1,    2.0,    4.0,   "viral",   "#e74c3c",
     "Kandolf 1985"),

    ("2A protease activity onset",      2,    3.0,    4.0,   "viral",   "#e74c3c",
     "Badorff 2000 (JCI); autocatalytic cleavage 2-4h"),

    ("First progeny virions",           4,    6.0,    8.0,   "viral",   "#c0392b",
     "Kandolf 1985; Knowlton 1996 — first progeny 4-6h"),

    ("Burst release (lysis)",           6,   10.0,   14.0,  "viral",   "#c0392b",
     "Knowlton 1996; burst size 10³-10⁵ PFU/cell"),

    # -------- MOLECULAR DAMAGE --------
    ("eIF4G cleavage (host translation stop)", 2,  3.0,  6.0, "molecular", "#8e44ad",
     "Badorff 2000; eIF4G cleaved within 2h of 2A onset"),

    ("Dystrophin cleavage detectable",  24,  36.0,   48.0,  "molecular", "#6c3483",
     "Badorff 1999 (Nat Med); Western blot 24-48h"),

    ("50% dystrophin loss",             48,  72.0,   96.0,  "molecular", "#6c3483",
     "Badorff 1999; estimated from cleavage kinetics"),

    ("DGC complex disassembly",         24,  48.0,   72.0,  "molecular", "#9b59b6",
     "Badorff 1999; follows dystrophin loss"),

    # -------- IMMUNE RESPONSE --------
    ("Type I IFN response (IFN-α/β)",    4,   8.0,   24.0,  "immune",   "#27ae60",
     "Kawai 1999; innate antiviral onset"),

    ("NK cell recruitment to myocardium",  60,  72.0,  120.0, "immune",  "#2ecc71",
     "Martino 1994 (Circulation); detectable at 72h"),

    ("Macrophage infiltration",         24,  72.0,  120.0,  "immune",   "#1abc9c",
     "Kawai 1999"),

    ("CD8+ T cell infiltration",        120, 144.0, 192.0,  "immune",   "#16a085",
     "Opavsky 1999 (JCI); day 5-7"),

    ("Anti-cardiac myosin Ab (autoimmune)", 168, 216.0, 336.0, "immune", "#0e6655",
     "Wolfgram 1985; IgG peak ~day 10-14"),

    ("Peak inflammatory morbidity",     144, 180.0, 216.0,  "immune",   "#117a65",
     "Kawai 1999; day 7-9 (168-216h)"),

    # -------- TD MUTANTS & CHRONIC PHASE --------
    ("TD mutant formation begins",       48,  72.0,  120.0, "chronic",  "#d35400",
     "Lindberg 1992; 5' deletion events"),

    ("TD mutant detectable (PCR)",       72,  96.0,  168.0, "chronic",  "#e67e22",
     "Callon 2022; from day 3 (72h)"),

    ("TD mutant persistence established",240, 336.0, 720.0, "chronic",  "#e67e22",
     "Cunningham 2003; weeks post-infection"),

    # -------- FIBROSIS / REMODELING --------
    ("Myofibroblast differentiation",   240, 288.0, 360.0,  "fibrosis", "#2980b9",
     "Pauschinger 2000; day 10-14"),

    ("Collagen deposition (fibrosis)",  240, 336.0, 504.0,  "fibrosis", "#1a5276",
     "Pauschinger 2000; day 10-14"),
]

# Convert hours to days for display
print("=" * 75)
print("CVB CARDIAC CASCADE — TIME CONSTANTS")
print("=" * 75)
print(f"\n  {'Event':45s}  {'Onset(h)':>8s}  {'Peak(h)':>8s}  {'Ref'}")
print("  " + "-" * 95)
for event in CASCADE_EVENTS:
    name, t_start, t_peak, t_end, cat, color, ref = event
    print(f"  {name:45s}  {t_start:>8.0f}h  {t_peak:>6.0f}h  {ref[:40]}")

# ============================================================
# SECTION 2: VIRAL KINETICS PARAMETERS
# ============================================================

print("\n" + "=" * 65)
print("CVB3 REPLICATION KINETICS PARAMETERS")
print("=" * 65)

# Kandolf 1985 / Knowlton 1996
burst_size_low  = 1e3   # PFU/cell (conservative)
burst_size_high = 1e5   # PFU/cell
burst_size_geom = np.sqrt(burst_size_low * burst_size_high)  # geometric mean

# CVB3 replication cycle
t_first_progeny_h    = 5.0     # hours
t_burst_h            = 10.0    # mean lysis time
t_eclipse_h          = 4.0     # eclipse period (before first progeny)

# Peak tissue viral load
peak_viral_load_per_g = 1e8    # copies/g heart tissue (Knowlton 1996)

print(f"\n  First progeny virions:   {t_first_progeny_h} h  (Kandolf 1985)")
print(f"  Burst size:              {burst_size_low:.0e} - {burst_size_high:.0e} PFU/cell")
print(f"  Burst size (geom mean):  {burst_size_geom:.0e} PFU/cell")
print(f"  Eclipse period:          {t_eclipse_h} h")
print(f"  Lysis time:              {t_burst_h} h")
print(f"  Peak tissue load:        {peak_viral_load_per_g:.0e} copies/g tissue  (Knowlton 1996)")

# Viral growth model (simple exponential until peak, then immune control)
def viral_replication(t_h, t_peak_h=72, t_clear_h=200):
    """
    Simplified biphasic viral kinetics:
    - Exponential growth phase until t_peak
    - Immune clearance phase after t_peak (exponential decay)
    """
    if t_h <= t_first_progeny_h:
        return 0
    elif t_h <= t_peak_h:
        # Exponential growth from single infected cell
        k_grow = np.log(peak_viral_load_per_g / burst_size_geom) / (t_peak_h - t_first_progeny_h)
        return burst_size_geom * np.exp(k_grow * (t_h - t_first_progeny_h))
    else:
        # Immune clearance
        k_clear = np.log(100) / (t_clear_h - t_peak_h)  # 100-fold drop in clearance window
        return peak_viral_load_per_g * np.exp(-k_clear * (t_h - t_peak_h))

# CAR internalization kinetics
print("\n" + "=" * 65)
print("CAR RECEPTOR INTERNALIZATION")
print("=" * 65)
t_half_CAR_h = 3.0   # Coyne & Bergelson 2006: t½ ~2-4h
k_CAR_intern = np.log(2) / t_half_CAR_h
print(f"\n  CAR internalization t½:  {t_half_CAR_h} h  (Coyne & Bergelson 2006)")
print(f"  k_CAR_intern:            {k_CAR_intern:.3f} /h")
t_CAR_50pct  = t_half_CAR_h
t_CAR_90pct  = np.log(10) / k_CAR_intern
print(f"  50% internalized at:     {t_CAR_50pct:.1f} h")
print(f"  90% internalized at:     {t_CAR_90pct:.1f} h  → cell is 'locked in'")

# ============================================================
# SECTION 3: FIGURE — CASCADE TIMELINE
# ============================================================

fig, (ax_timeline, ax_viral) = plt.subplots(2, 1, figsize=(16, 11),
                                              gridspec_kw={'height_ratios': [3, 1]})
fig.suptitle('CVB Cardiac Cascade — Complete Timeline\n'
             '(Badorff 1999, Kandolf 1985, Martino 1994, Opavsky 1999, Kawai 1999, Callon 2022)',
             fontsize=12, y=1.01)

# Category y-offsets (from bottom to top of timeline)
category_order = ['viral', 'molecular', 'immune', 'chronic', 'fibrosis']
category_labels = {
    'viral':     'Viral replication',
    'molecular': 'Molecular damage',
    'immune':    'Immune response',
    'chronic':   'TD mutant / chronic',
    'fibrosis':  'Fibrosis / remodeling',
}
cat_y = {cat: i * 1.5 for i, cat in enumerate(category_order)}
cat_colors = {
    'viral':     '#e74c3c',
    'molecular': '#8e44ad',
    'immune':    '#27ae60',
    'chronic':   '#e67e22',
    'fibrosis':  '#2980b9',
}

# Time axis: 0 to 720h (30 days)
t_max_h = 720
t_max_days = t_max_h / 24

# Group events by category to assign vertical sub-positions
from collections import defaultdict
cat_event_count = defaultdict(int)
cat_event_idx = defaultdict(int)

# Count events per category
for event in CASCADE_EVENTS:
    cat_event_count[event[4]] += 1

# Draw each event as a horizontal bar
y_step = 0.35  # vertical spacing within category
for event in CASCADE_EVENTS:
    name, t_start, t_peak, t_end, cat, color, ref = event
    y_base = cat_y[cat]
    sub_idx = cat_event_idx[cat]
    y = y_base + sub_idx * y_step
    cat_event_idx[cat] += 1

    t_s = min(t_start, t_max_h)
    t_e = min(t_end, t_max_h)
    t_p = min(t_peak, t_max_h)

    # Draw bar
    ax_timeline.barh(y, t_e - t_s, left=t_s, height=0.25,
                     color=color, alpha=0.75, edgecolor='white', linewidth=0.5)
    # Peak marker
    ax_timeline.plot(t_p, y + 0.125, 'v', color='black', ms=4, alpha=0.7)
    # Label
    ax_timeline.text(t_e + 4, y + 0.05, name, fontsize=6.5, va='center',
                     color='black', clip_on=True)

# Category labels on left
for cat, y_base in cat_y.items():
    n = cat_event_count[cat]
    y_mid = y_base + (n - 1) * y_step / 2 + 0.125
    ax_timeline.text(-15, y_mid, category_labels[cat], fontsize=9,
                     va='center', ha='right', color=cat_colors[cat],
                     fontweight='bold')

# Vertical gridlines at key timepoints
key_times_h = [24, 48, 72, 120, 168, 240, 336]
for t in key_times_h:
    ax_timeline.axvline(t, color='lightgrey', lw=0.8, ls=':')
    ax_timeline.text(t, -0.5, f'{t//24}d', fontsize=7, ha='center',
                     color='grey', va='top')

# Highlight peak morbidity window (day 7-9 = 168-216h)
ax_timeline.axvspan(168, 216, color='red', alpha=0.06, label='Peak morbidity (day 7-9)')
ax_timeline.axvspan(240, 336, color='blue', alpha=0.05, label='Fibrosis onset (day 10-14)')

ax_timeline.set_xlim(-30, t_max_h + 80)
ax_timeline.set_ylim(-1, max(cat_y.values()) + cat_event_count[category_order[-1]] * y_step + 0.5)
ax_timeline.set_xlabel('Time post-infection (hours)', fontsize=10)
ax_timeline.set_title('A. CVB Cardiac Cascade Timeline')
ax_timeline.set_yticks([])
ax_timeline.grid(True, axis='x', alpha=0.2)

# Legend patches
patches = [mpatches.Patch(color=cat_colors[c], label=category_labels[c])
           for c in category_order]
patches.append(mpatches.Patch(color='red', alpha=0.3, label='Peak morbidity window'))
patches.append(mpatches.Patch(color='blue', alpha=0.3, label='Fibrosis onset'))
ax_timeline.legend(handles=patches, loc='upper left', fontsize=7, ncol=2)

# --- Viral kinetics panel ---
t_range = np.linspace(0, t_max_h, 2000)
viral_t = [viral_replication(t) for t in t_range]
ax_viral.semilogy(t_range, [max(v, 1) for v in viral_t], color='#e74c3c', lw=2.5)
ax_viral.axhline(peak_viral_load_per_g, color='red', ls='--', lw=1.2, alpha=0.5,
                 label=f'Peak = 10⁸ copies/g (Knowlton 1996)')
ax_viral.axvline(72, color='grey', ls=':', lw=1.2)
ax_viral.text(72, 10, 'Peak\n(~3 days)', fontsize=7, ha='center', color='grey')
ax_viral.axvspan(4, 14, color='orange', alpha=0.2, label='First progeny (4-6h)')

# Mark burst size range
ax_viral.axhline(burst_size_geom, color='orange', ls=':', lw=1.5,
                 label=f'Single cell burst = {burst_size_geom:.0e} PFU')

ax_viral.set_xlabel('Time post-infection (hours)', fontsize=10)
ax_viral.set_ylabel('Viral copies / g tissue', fontsize=9)
ax_viral.set_title('B. CVB3 Replication Kinetics (Kandolf 1985, Knowlton 1996)')
ax_viral.set_xlim(0, t_max_h)
ax_viral.legend(fontsize=8)
ax_viral.grid(True, alpha=0.3)

# Mark key time points for x-axis (days)
ax2 = ax_viral.twiny()
ax2.set_xlim(ax_viral.get_xlim())
day_ticks_h = [0, 24, 48, 72, 120, 168, 240, 336, 480, 720]
ax2.set_xticks(day_ticks_h)
ax2.set_xticklabels([f'{t//24}d' for t in day_ticks_h], fontsize=7)
ax2.set_xlabel('Days post-infection', fontsize=9)

plt.tight_layout()
out_dir = os.path.dirname(os.path.abspath(__file__))
results_dir = os.path.join(out_dir, '..', 'results')
fig_path = os.path.join(results_dir, 'cardiac_cascade_timing.png')
plt.savefig(fig_path, dpi=150, bbox_inches='tight')
print(f"\nFigure saved to: {fig_path}")
plt.close()

# ============================================================
# SECTION 4: PARAMETER SUMMARY
# ============================================================

print("\n" + "=" * 65)
print("PARAMETER SUMMARY TABLE")
print("=" * 65)
params = {
    'CAR_internalization_t_half (h)':     t_half_CAR_h,
    'first_progeny_time (h)':             t_first_progeny_h,
    'burst_size_min (PFU/cell)':          burst_size_low,
    'burst_size_max (PFU/cell)':          burst_size_high,
    'burst_size_geom_mean (PFU/cell)':    round(burst_size_geom),
    'eclipse_period (h)':                 t_eclipse_h,
    'lysis_time (h)':                     t_burst_h,
    'peak_tissue_load (copies/g)':        peak_viral_load_per_g,
    '2A_protease_onset (h)':              2.0,
    'dystrophin_loss_detectable (h)':     24.0,
    'NK_recruitment (h)':                 72.0,
    'CD8_infiltration (h)':               120.0,
    'peak_morbidity_start (h)':           144.0,
    'fibrosis_onset (h)':                 240.0,
    'TD_mutant_detectable (h)':           72.0,
}
for k, v in params.items():
    print(f"  {k:<45s}  {v}")

print("\nDone.")
