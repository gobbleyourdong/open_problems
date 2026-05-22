"""
Curated taxon -> function knowledge base for the dysbiosis framework analyzer.

This is the heart of "our own tools": instead of HUMAnN/DIAMOND gene-level search
(dead on aarch64) or TinyHealth's opaque proprietary indices, we map taxa to
functions transparently and compute the framework's constructs from Bracken
relative abundances ourselves. Every entry carries a short evidence note.

Matching is by lowercased substring on the Bracken species name. `weight` lets
strong producers count more than incidental ones (default 1.0). Extend freely —
this table IS the tool's knowledge; keep it cited.
"""

# Each category: list of (match_substring, weight, note)
FUNCTIONS = {
    "butyrate_producers": [
        ("faecalibacterium prausnitzii", 1.5, "flagship colonic butyrate producer; Node A"),
        ("roseburia", 1.2, "major butyrate producer (faecis/intestinalis/hominis/inulinivorans)"),
        ("agathobacter rectalis", 1.2, "ex-Eubacterium rectale; major butyrate producer"),
        ("anaerobutyricum hallii", 1.0, "ex-Eubacterium hallii; butyrate + propionate"),
        ("anaerostipes", 1.0, "lactate->butyrate cross-feeder"),
        ("coprococcus", 0.8, "butyrate producer (catus/comes/eutactus)"),
        ("eubacterium ramulus", 0.6, "butyrate; flavonoid-degrading"),
        ("butyricicoccus", 0.8, "butyrate producer"),
        ("butyrivibrio", 0.6, "butyrate producer"),
        ("subdoligranulum", 0.8, "F. prausnitzii relative; butyrate"),
        ("faecalibacterium", 1.2, "genus-level butyrate (non-prausnitzii spp.)"),
    ],
    "sulfate_reducers_h2s": [
        ("bilophila wadsworthia", 1.5, "taurine/bile -> H2S; bloom on high-fat diet"),
        ("desulfovibrio", 1.5, "dissimilatory sulfate reduction -> H2S"),
        ("fusobacterium", 0.8, "cysteine-derived H2S"),
        ("desulfobacter", 1.2, "sulfate reducer"),
        ("desulfomonas", 1.0, "sulfate reducer"),
    ],
    "hexa_lps_proinflammatory": [   # Enterobacteriaceae/Proteobacteria: hexa-acylated lipid A, strong TLR4
        ("escherichia", 1.2, "hexa-acylated LPS; strong TLR4 agonist"),
        ("klebsiella", 1.2, "hexa-acylated LPS"),
        ("enterobacter", 1.0, "hexa-acylated LPS"),
        ("citrobacter", 1.0, "hexa-acylated LPS"),
        ("salmonella", 1.2, "hexa-acylated LPS"),
        ("proteus", 1.0, "hexa-acylated LPS"),
        ("shigella", 1.2, "hexa-acylated LPS (Enterobacteriaceae)"),
        ("pseudomonas", 0.8, "penta/hexa mixed; TLR4-active"),
        ("morganella", 1.0, "Enterobacteriaceae LPS"),
        ("hafnia", 0.8, "Enterobacteriaceae LPS"),
    ],
    "penta_lps_immunoinhibitory": [  # Bacteroidetes: penta-acylated lipid A, weak/antagonist TLR4
        ("bacteroides", 1.0, "penta-acylated LPS; weak TLR4 / antagonist"),
        ("phocaeicola", 1.0, "ex-Bacteroides; penta-acylated LPS"),
        ("parabacteroides", 1.0, "penta-acylated LPS"),
        ("prevotella", 1.0, "penta-acylated LPS"),
        ("alistipes", 0.8, "Bacteroidetes; under-acylated LPS"),
        ("porphyromonas", 0.8, "penta/tetra-acylated LPS"),
    ],
    "mucin_degraders": [
        ("akkermansia muciniphila", 1.5, "mucin specialist; barrier keystone (Amuc_1100/TLR2)"),
        ("ruminococcus gnavus", 1.0, "mucin degrader; can be pro-inflammatory in bloom"),
        ("ruminococcus torques", 0.8, "mucin degrader"),
        ("bacteroides thetaiotaomicron", 0.8, "versatile incl. mucin glycans"),
        ("bacteroides fragilis", 0.6, "mucin-associated"),
        ("barnesiella", 0.6, "mucin-associated"),
    ],
    "histamine_producers": [
        ("morganella morganii", 1.5, "strong histamine producer (HDC)"),
        ("klebsiella pneumoniae", 1.2, "histamine producer"),
        ("klebsiella oxytoca", 1.0, "histamine producer"),
        ("enterobacter", 0.8, "histamine producer"),
        ("citrobacter", 0.6, "histamine producer"),
        ("enterococcus faecalis", 0.6, "tyramine/histamine"),
        ("limosilactobacillus reuteri", 0.5, "histamine via hdc (strain-dependent)"),
    ],
    "beneficial_keystones": [
        ("akkermansia muciniphila", 1.5, "barrier + metabolic keystone"),
        ("faecalibacterium prausnitzii", 1.5, "anti-inflammatory butyrate keystone"),
        ("bifidobacterium", 1.0, "beneficial; HMO/fiber fermenter"),
        ("lactobacillus", 0.6, "beneficial fermenter"),
        ("lacticaseibacillus rhamnosus", 0.6, "probiotic"),
    ],
}

# Phylum-name synonyms (NCBI/GTDB drift) so the engine finds Proteobacteria etc.
PHYLUM_SYNONYMS = {
    "proteobacteria": ["proteobacteria", "pseudomonadota"],
    "bacteroidota":   ["bacteroidota", "bacteroidetes"],
    "firmicutes":     ["firmicutes", "bacillota"],
    "actinobacteria": ["actinobacteria", "actinomycetota", "actinobacteriota"],
}

# Framework thresholds (healthy / concerning) for flagging — from run_004 + literature.
THRESHOLDS = {
    "f_prausnitzii_pct":   {"healthy": 5.0,  "concerning_below": 1.0},
    "akkermansia_pct":     {"healthy": 0.1,  "concerning_below": 0.01},
    "proteobacteria_pct":  {"healthy_below": 10.0, "concerning_above": 20.0},
    "butyrate_capacity_pct": {"healthy": 10.0, "concerning_below": 5.0},
    "hexa_penta_ratio":    {"healthy_below": 0.25, "concerning_above": 0.6},
    "sulfate_reducer_pct": {"healthy_below": 0.5,  "concerning_above": 2.0},
    "histamine_pct":       {"healthy_below": 0.1,  "concerning_above": 0.5},
}
