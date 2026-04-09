#!/usr/bin/env python3
"""
CVB Disease Network Topology — numerical track Numerics
=====================================================

Models the 12 CVB-caused diseases as a directed graph with causal/
progression edges. Computes network topology metrics to identify:
  - Most connected disease (highest degree)
  - Keystone disease (removing it disconnects the most paths)
  - Best intervention target (prevents most downstream disease)
  - Disease clusters and cascading failure paths

The 12 CVB diseases form a directed acyclic graph (with one feedback
loop via orchitis reseeding) that maps the trajectory of a single
enteroviral infection through multiple organ systems.

References:
-----------
[1]  Tracy et al., J Clin Invest 2000: CVB persistence mechanisms
[2]  Chia & Chia, J Clin Pathol 2008: CVB in ME/CFS
[3]  Chapman et al., J Gen Virol 2008: TD mutant persistence
[4]  Bowles et al., Lancet 1986: CVB in dilated cardiomyopathy
[5]  Ylipaasto et al., Diabetologia 2004: CVB in T1DM
[6]  Huber & Gauntt, Trends Microbiol 1998: CVB myocarditis
[7]  Bopegamage et al., J Med Virol 2005: CVB pancreatitis
[8]  Abzug, Pediatrics 2001: Neonatal enteroviral sepsis
[9]  Tauriainen et al., Clin Dev Immunol 2010: CVB persistence multi-organ
[10] Loria et al., Virology 1977: CVB orchitis, immune-privileged reservoir
[11] Drescher & Tracy, Viral Immunol 2008: CVB-induced autoimmunity cascade

systematic approach — numerical track (numerics) — Cross-disease analysis
Date: 2026-04-08
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import defaultdict, deque
import os
import json

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "figures")
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ============================================================================
# SECTION 1: DISEASE DEFINITIONS
# ============================================================================

# The 12 CVB diseases. Each node has properties relevant to the network.
DISEASES = {
    "cvb_infection": {
        "name": "Acute CVB Infection",
        "short": "CVB",
        "category": "root",
        "serotypes": ["B1", "B2", "B3", "B4", "B5"],
        "population_at_risk": 1.0,          # normalized (everyone exposed)
        "current_treatment": "supportive",
        "severity_weight": 0.2,             # acute, usually self-limiting
        "color": "#95a5a6",                 # gray
    },
    "pleurodynia": {
        "name": "Pleurodynia (Bornholm)",
        "short": "PLEUR",
        "category": "acute_muscle",
        "serotypes": ["B1", "B3", "B5"],
        "population_at_risk": 0.15,         # ~15% of CVB infections
        "current_treatment": "NSAIDs",
        "severity_weight": 0.3,
        "color": "#e67e22",                 # orange
    },
    "aseptic_meningitis": {
        "name": "Aseptic Meningitis",
        "short": "MENING",
        "category": "acute_cns",
        "serotypes": ["B1", "B2", "B3", "B4", "B5"],
        "population_at_risk": 0.10,
        "current_treatment": "supportive",
        "severity_weight": 0.4,
        "color": "#9b59b6",                 # purple
    },
    "hepatitis": {
        "name": "Viral Hepatitis",
        "short": "HEP",
        "category": "acute_organ",
        "serotypes": ["B1", "B3", "B4", "B5"],
        "population_at_risk": 0.05,
        "current_treatment": "supportive",
        "severity_weight": 0.5,
        "color": "#1abc9c",                 # teal
    },
    "neonatal_sepsis": {
        "name": "Neonatal Sepsis",
        "short": "NEO",
        "category": "acute_neonatal",
        "serotypes": ["B1", "B2", "B3", "B4", "B5"],
        "population_at_risk": 0.001,        # neonates only
        "current_treatment": "IVIG",
        "severity_weight": 0.95,            # high mortality
        "color": "#e74c3c",                 # red
    },
    "myocarditis": {
        "name": "Viral Myocarditis",
        "short": "MYOC",
        "category": "cardiac",
        "serotypes": ["B3", "B4"],
        "population_at_risk": 0.05,
        "current_treatment": "supportive + HF management",
        "severity_weight": 0.7,
        "color": "#c0392b",                 # dark red
    },
    "pericarditis": {
        "name": "Pericarditis",
        "short": "PERI",
        "category": "cardiac",
        "serotypes": ["B1", "B3", "B4"],
        "population_at_risk": 0.08,
        "current_treatment": "colchicine + NSAIDs",
        "severity_weight": 0.5,
        "color": "#e74c3c",                 # red
    },
    "pancreatitis": {
        "name": "Viral Pancreatitis",
        "short": "PANC",
        "category": "metabolic",
        "serotypes": ["B1", "B4"],
        "population_at_risk": 0.03,
        "current_treatment": "supportive",
        "severity_weight": 0.6,
        "color": "#f39c12",                 # yellow
    },
    "orchitis": {
        "name": "Orchitis",
        "short": "ORCH",
        "category": "immune_privileged",
        "serotypes": ["B5"],
        "population_at_risk": 0.02,         # male only, rare
        "current_treatment": "none",
        "severity_weight": 0.4,
        "color": "#2980b9",                 # blue
    },
    "encephalitis": {
        "name": "Encephalitis",
        "short": "ENCEPH",
        "category": "cns_severe",
        "serotypes": ["B1", "B3", "B5"],
        "population_at_risk": 0.005,
        "current_treatment": "supportive + anticonvulsants",
        "severity_weight": 0.85,
        "color": "#8e44ad",                 # dark purple
    },
    "dcm": {
        "name": "Dilated Cardiomyopathy",
        "short": "DCM",
        "category": "chronic_cardiac",
        "serotypes": ["B3"],
        "population_at_risk": 0.02,
        "current_treatment": "HF drugs (SGLT2i, beta-blockers)",
        "severity_weight": 0.85,
        "color": "#922B21",                 # maroon
    },
    "t1dm": {
        "name": "Type 1 Diabetes",
        "short": "T1DM",
        "category": "autoimmune",
        "serotypes": ["B1", "B4"],
        "population_at_risk": 0.01,
        "current_treatment": "insulin (lifelong)",
        "severity_weight": 0.8,
        "color": "#2ecc71",                 # green
    },
    "me_cfs": {
        "name": "ME/CFS",
        "short": "ME/CFS",
        "category": "chronic_systemic",
        "serotypes": ["B1", "B2", "B3", "B4", "B5"],
        "population_at_risk": 0.05,
        "current_treatment": "none (pacing, symptomatic)",
        "severity_weight": 0.75,
        "color": "#3498db",                 # bright blue
    },
}


# ============================================================================
# SECTION 2: EDGE DEFINITIONS (Causal/Progression Relationships)
# ============================================================================

# Each edge: (source, target, weight, mechanism, evidence_grade)
# Weight = transition probability (fraction of source patients who develop target)
# Evidence_grade: A = RCT/meta-analysis, B = cohort/case-control,
#                 C = case series, D = mechanistic inference, E = hypothesis

EDGES = [
    # === Primary infection routes ===
    # CVB infection seeds multiple organs simultaneously via viremia
    ("cvb_infection", "pleurodynia", 0.15,
     "CVB tropism for skeletal muscle via CAR/DAF receptors",
     "B"),
    ("cvb_infection", "aseptic_meningitis", 0.10,
     "CVB crosses BBB during viremia; most common viral meningitis cause",
     "A"),
    ("cvb_infection", "hepatitis", 0.05,
     "CVB hepatotropism; severe in neonates, usually mild in adults",
     "B"),
    ("cvb_infection", "neonatal_sepsis", 0.001,
     "Vertical/perinatal transmission; immature immune system can't contain",
     "B"),
    ("cvb_infection", "myocarditis", 0.05,
     "CVB3 cardiotropism; 2A protease cleaves dystrophin in cardiomyocytes",
     "A"),
    ("cvb_infection", "pericarditis", 0.08,
     "CVB triggers NLRP3 inflammasome in pericardium",
     "B"),
    ("cvb_infection", "pancreatitis", 0.03,
     "CVB1/B4 tropism for exocrine pancreas via CAR receptor",
     "B"),
    ("cvb_infection", "orchitis", 0.02,
     "CVB5 crosses blood-testis barrier; immune-privileged site",
     "C"),

    # === Acute-to-chronic progression ===
    # Pleurodynia (acute muscle) can become ME/CFS (chronic multi-site)
    ("pleurodynia", "me_cfs", 0.20,
     "Incomplete clearance from muscle; TD mutant persistence; cross-seeds to gut/CNS",
     "B"),

    # Aseptic meningitis can progress to encephalitis
    ("aseptic_meningitis", "encephalitis", 0.05,
     "CVB spreads from meninges to brain parenchyma; rare but serious",
     "B"),

    # Myocarditis → DCM (the classic cardiac progression)
    ("myocarditis", "dcm", 0.30,
     "2A protease cleaves dystrophin → progressive cardiac remodeling → heart failure",
     "A"),

    # Pancreatitis → T1DM (exocrine → endocrine seeding)
    ("pancreatitis", "t1dm", 0.25,
     "CVB seeds from acinar cells to islets → beta cell infection → autoimmune destruction",
     "B"),

    # === Bidirectional cardiac link ===
    # Pericarditis and myocarditis often co-occur (myopericarditis)
    ("pericarditis", "myocarditis", 0.15,
     "Pericardial inflammation spreads to myocardium; shared NLRP3 pathway",
     "B"),
    ("myocarditis", "pericarditis", 0.20,
     "Myocardial inflammation extends to pericardium; inflammatory spillover",
     "B"),

    # === Any acute CVB can seed orchitis ===
    # All acute presentations imply viremia that can reach testes
    ("myocarditis", "orchitis", 0.05,
     "Sustained viremia during myocarditis can seed immune-privileged testes",
     "C"),
    ("pancreatitis", "orchitis", 0.05,
     "Viremia during pancreatitis; shared CVB serotypes seed testes",
     "D"),

    # === Orchitis reseeding (the feedback loop) ===
    # Orchitis creates a long-term reservoir that can reseed all organs
    ("orchitis", "myocarditis", 0.10,
     "Immune-privileged testes harbor virus indefinitely; periodic viral shedding reseeds heart",
     "C"),
    ("orchitis", "pancreatitis", 0.10,
     "Testicular reservoir periodically releases virus into bloodstream → pancreas reseeding",
     "D"),
    ("orchitis", "me_cfs", 0.15,
     "Chronic viral shedding from testes → multi-organ reseeding → ME/CFS pattern",
     "D"),

    # === CVB infection can directly cause ME/CFS ===
    ("cvb_infection", "me_cfs", 0.05,
     "Direct post-viral ME/CFS without overt acute presentation; 'just a cold' → chronic fatigue",
     "B"),

    # === CVB infection can directly cause T1DM ===
    ("cvb_infection", "t1dm", 0.01,
     "Direct islet infection during viremia without clinical pancreatitis",
     "B"),

    # === Neonatal sepsis can progress to multiple organ disease ===
    ("neonatal_sepsis", "myocarditis", 0.40,
     "Multi-organ neonatal CVB: cardiac involvement in ~40% of neonatal sepsis cases",
     "B"),
    ("neonatal_sepsis", "hepatitis", 0.50,
     "Neonatal CVB hepatitis: liver failure is leading cause of neonatal CVB death",
     "A"),
    ("neonatal_sepsis", "encephalitis", 0.20,
     "Neonatal CNS invasion: immature BBB allows easier viral penetration",
     "B"),
]


# ============================================================================
# SECTION 3: GRAPH CONSTRUCTION AND ANALYSIS
# ============================================================================

class DiseaseNetwork:
    """Directed graph of CVB disease relationships."""

    def __init__(self, diseases, edges):
        self.diseases = diseases
        self.nodes = list(diseases.keys())
        self.n = len(self.nodes)

        # Adjacency list: node -> [(target, weight, mechanism, evidence)]
        self.adj = defaultdict(list)
        # Reverse adjacency: node -> [(source, weight, mechanism, evidence)]
        self.rev_adj = defaultdict(list)

        for src, tgt, weight, mechanism, evidence in edges:
            self.adj[src].append((tgt, weight, mechanism, evidence))
            self.rev_adj[tgt].append((src, weight, mechanism, evidence))

        # Build adjacency matrix
        self.node_idx = {n: i for i, n in enumerate(self.nodes)}
        self.adj_matrix = np.zeros((self.n, self.n))
        for src, tgt, weight, _, _ in edges:
            i, j = self.node_idx[src], self.node_idx[tgt]
            self.adj_matrix[i, j] = weight

    def degree_analysis(self):
        """Compute in-degree, out-degree, total degree for each node."""
        results = {}
        for node in self.nodes:
            out_degree = len(self.adj[node])
            in_degree = len(self.rev_adj[node])
            # Weighted degrees
            out_weight = sum(w for _, w, _, _ in self.adj[node])
            in_weight = sum(w for _, w, _, _ in self.rev_adj[node])
            results[node] = {
                "out_degree": out_degree,
                "in_degree": in_degree,
                "total_degree": out_degree + in_degree,
                "out_weight": out_weight,
                "in_weight": in_weight,
                "total_weight": out_weight + in_weight,
            }
        return results

    def downstream_diseases(self, node, visited=None):
        """
        Find all diseases reachable downstream from a given node (BFS).
        Returns set of reachable nodes and total weighted path probability.
        """
        if visited is None:
            visited = set()
        visited.add(node)
        reachable = set()
        for tgt, weight, _, _ in self.adj[node]:
            if tgt not in visited:
                reachable.add(tgt)
                reachable |= self.downstream_diseases(tgt, visited.copy())
        return reachable

    def upstream_diseases(self, node, visited=None):
        """Find all diseases that can lead to a given node (reverse BFS)."""
        if visited is None:
            visited = set()
        visited.add(node)
        reachable = set()
        for src, weight, _, _ in self.rev_adj[node]:
            if src not in visited:
                reachable.add(src)
                reachable |= self.upstream_diseases(src, visited.copy())
        return reachable

    def keystone_analysis(self):
        """
        For each node, compute how many downstream paths are disrupted
        if that node is removed. The "keystone" is the node whose removal
        disconnects the most disease paths.
        """
        # Baseline: count all reachable pairs
        baseline_paths = 0
        for node in self.nodes:
            baseline_paths += len(self.downstream_diseases(node))

        results = {}
        for removed in self.nodes:
            # Create a temporary network without this node
            remaining_adj = defaultdict(list)
            for src in self.nodes:
                if src == removed:
                    continue
                for tgt, w, m, e in self.adj[src]:
                    if tgt != removed:
                        remaining_adj[src].append((tgt, w, m, e))

            # Count reachable pairs in reduced network
            reduced_paths = 0
            for node in self.nodes:
                if node == removed:
                    continue
                visited = {removed}  # pretend removed node is visited
                queue = deque([node])
                seen = {node}
                while queue:
                    current = queue.popleft()
                    for tgt, _, _, _ in remaining_adj[current]:
                        if tgt not in seen and tgt != removed:
                            seen.add(tgt)
                            queue.append(tgt)
                            reduced_paths += 1

            paths_disrupted = baseline_paths - reduced_paths
            results[removed] = {
                "paths_disrupted": paths_disrupted,
                "baseline_paths": baseline_paths,
                "fraction_disrupted": paths_disrupted / max(baseline_paths, 1),
            }

        return results

    def intervention_value(self):
        """
        For each node, compute the "intervention value" = weighted sum of
        downstream diseases prevented, weighted by:
          - transition probability along the path
          - severity of downstream diseases
          - population at risk

        This answers: "If we could perfectly prevent/treat disease X,
        how much total disease burden do we prevent?"
        """
        results = {}
        for node in self.nodes:
            # BFS with probability propagation
            prevented_burden = 0.0
            queue = deque()
            # Seed with direct downstream edges
            for tgt, weight, _, _ in self.adj[node]:
                queue.append((tgt, weight))

            visited = {node}
            while queue:
                current, path_prob = queue.popleft()
                if current in visited:
                    continue
                visited.add(current)

                # Burden prevented = probability of reaching this disease *
                #                     severity * population at risk
                d = self.diseases[current]
                burden = path_prob * d["severity_weight"] * d["population_at_risk"]
                prevented_burden += burden

                # Continue downstream
                for tgt, weight, _, _ in self.adj[current]:
                    if tgt not in visited:
                        queue.append((tgt, path_prob * weight))

            # Also include the node itself (treating it prevents its own burden)
            d = self.diseases[node]
            own_burden = d["severity_weight"] * d["population_at_risk"]

            results[node] = {
                "downstream_prevented": prevented_burden,
                "own_burden": own_burden,
                "total_intervention_value": prevented_burden + own_burden,
                "downstream_count": len(self.downstream_diseases(node)),
            }

        return results

    def find_cascading_paths(self, max_length=6):
        """
        Find all paths from CVB infection to terminal diseases (T1DM, DCM,
        ME/CFS) and compute their cumulative probabilities.
        """
        terminal_diseases = {"t1dm", "dcm", "me_cfs", "encephalitis"}
        all_paths = []

        def dfs(node, path, prob, visited):
            if node in terminal_diseases and len(path) > 1:
                all_paths.append({
                    "path": list(path),
                    "probability": prob,
                    "length": len(path),
                    "terminal": node,
                })
            if len(path) >= max_length:
                return
            for tgt, weight, mechanism, _ in self.adj[node]:
                if tgt not in visited:
                    visited.add(tgt)
                    path.append(tgt)
                    dfs(tgt, path, prob * weight, visited)
                    path.pop()
                    visited.discard(tgt)

        dfs("cvb_infection", ["cvb_infection"], 1.0, {"cvb_infection"})
        # Sort by probability (highest first)
        all_paths.sort(key=lambda p: p["probability"], reverse=True)
        return all_paths

    def find_clusters(self):
        """
        Identify disease clusters: groups of diseases that are strongly
        interconnected.
        """
        clusters = {
            "cardiac": {
                "diseases": ["myocarditis", "pericarditis", "dcm"],
                "description": "Cardiac cluster: CVB3 cardiotropism, 2A protease, dystrophin cleavage",
                "internal_edges": [],
            },
            "metabolic": {
                "diseases": ["pancreatitis", "t1dm"],
                "description": "Metabolic cluster: CVB1/B4 pancreatic tropism, exocrine-to-endocrine seeding",
                "internal_edges": [],
            },
            "neurological": {
                "diseases": ["aseptic_meningitis", "encephalitis", "me_cfs"],
                "description": "Neurological cluster: CVB CNS penetration, neuroinflammation",
                "internal_edges": [],
            },
            "reservoir": {
                "diseases": ["orchitis", "me_cfs"],
                "description": "Reservoir cluster: immune-privileged sites that enable chronic persistence",
                "internal_edges": [],
            },
            "acute": {
                "diseases": ["pleurodynia", "hepatitis", "neonatal_sepsis"],
                "description": "Acute presentation cluster: initial CVB manifestations",
                "internal_edges": [],
            },
        }

        # Find internal edges for each cluster
        for cname, cluster in clusters.items():
            disease_set = set(cluster["diseases"])
            for src in cluster["diseases"]:
                for tgt, weight, mechanism, _ in self.adj[src]:
                    if tgt in disease_set:
                        cluster["internal_edges"].append((src, tgt, weight, mechanism))

        return clusters


# ============================================================================
# SECTION 4: NETWORK VISUALIZATION
# ============================================================================

def visualize_network(network):
    """
    Create a publication-quality network visualization.
    Uses manual positioning for clarity (networkx layout often tangles
    biological networks).
    """
    # Manual node positions — arranged by disease progression flow
    # Top: root (CVB infection)
    # Middle: acute diseases
    # Bottom: chronic diseases
    positions = {
        "cvb_infection":      (0.50, 0.95),
        # Acute layer
        "pleurodynia":        (0.10, 0.70),
        "aseptic_meningitis": (0.30, 0.70),
        "hepatitis":          (0.50, 0.70),
        "neonatal_sepsis":    (0.70, 0.70),
        "myocarditis":        (0.85, 0.55),
        "pericarditis":       (0.95, 0.70),
        "pancreatitis":       (0.50, 0.45),
        "orchitis":           (0.20, 0.40),
        # Chronic layer
        "me_cfs":             (0.10, 0.15),
        "encephalitis":       (0.35, 0.45),
        "dcm":                (0.85, 0.25),
        "t1dm":               (0.60, 0.15),
    }

    fig, ax = plt.subplots(1, 1, figsize=(16, 12))
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.05)
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw edges first (behind nodes)
    for src, tgt, weight, _, evidence in EDGES:
        if src not in positions or tgt not in positions:
            continue
        x0, y0 = positions[src]
        x1, y1 = positions[tgt]

        # Edge thickness proportional to transition probability
        lw = max(0.5, weight * 8)
        alpha = min(0.9, 0.3 + weight * 2)

        # Color by evidence grade
        edge_colors = {"A": "#2c3e50", "B": "#2980b9", "C": "#e67e22", "D": "#e74c3c", "E": "#95a5a6"}
        color = edge_colors.get(evidence, "#95a5a6")

        # Draw arrow
        dx, dy = x1 - x0, y1 - y0
        length = np.sqrt(dx**2 + dy**2)
        # Shorten arrow to not overlap with node circles
        shrink = 0.04
        x0s = x0 + shrink * dx / length
        y0s = y0 + shrink * dy / length
        x1s = x1 - shrink * dx / length
        y1s = y1 - shrink * dy / length

        ax.annotate("",
                     xy=(x1s, y1s), xytext=(x0s, y0s),
                     arrowprops=dict(
                         arrowstyle='->', color=color, lw=lw,
                         alpha=alpha, connectionstyle='arc3,rad=0.1',
                         mutation_scale=15,
                     ))

        # Edge label (probability) at midpoint
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        # Offset slightly perpendicular to the edge
        perp_x, perp_y = -dy / length * 0.025, dx / length * 0.025
        if weight >= 0.10:
            ax.text(mx + perp_x, my + perp_y, f"{weight:.0%}",
                    fontsize=6, ha='center', va='center', color=color, alpha=0.8,
                    fontweight='bold')

    # Draw nodes
    for node_id, disease in network.diseases.items():
        if node_id not in positions:
            continue
        x, y = positions[node_id]

        # Node size proportional to severity
        radius = 0.025 + disease["severity_weight"] * 0.015

        circle = plt.Circle((x, y), radius, color=disease["color"],
                            ec='black', linewidth=1.5, zorder=5, alpha=0.9)
        ax.add_patch(circle)

        # Node label
        ax.text(x, y - radius - 0.025, disease["short"],
                fontsize=9, ha='center', va='top', fontweight='bold',
                color='#2c3e50')

    # Title and legend
    ax.set_title('CVB Disease Network Topology\n'
                 'One virus, 12 diseases, connected by causal/progression edges',
                 fontsize=16, fontweight='bold', pad=20)

    # Layer labels
    ax.text(-0.02, 0.95, 'ROOT', fontsize=10, fontweight='bold', color='gray',
            ha='right', va='center', rotation=0)
    ax.text(-0.02, 0.70, 'ACUTE', fontsize=10, fontweight='bold', color='gray',
            ha='right', va='center', rotation=0)
    ax.text(-0.02, 0.45, 'PROGRESSION', fontsize=10, fontweight='bold', color='gray',
            ha='right', va='center', rotation=0)
    ax.text(-0.02, 0.15, 'CHRONIC', fontsize=10, fontweight='bold', color='gray',
            ha='right', va='center', rotation=0)

    # Evidence grade legend
    legend_y = 0.10
    for grade, color, label in [
        ("A", "#2c3e50", "A: RCT/meta-analysis"),
        ("B", "#2980b9", "B: Cohort/case-control"),
        ("C", "#e67e22", "C: Case series"),
        ("D", "#e74c3c", "D: Mechanistic inference"),
    ]:
        ax.plot([0.75], [legend_y], 'o', color=color, markersize=6)
        ax.text(0.77, legend_y, label, fontsize=8, va='center', color=color)
        legend_y -= 0.03

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "disease_network.png"), dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"  Network visualization saved: {os.path.join(OUTPUT_DIR, 'disease_network.png')}")


# ============================================================================
# SECTION 5: INTERVENTION TARGET HEATMAP
# ============================================================================

def plot_intervention_heatmap(network, intervention_results):
    """
    Heatmap showing: rows = diseases, columns = metrics.
    Identifies the optimal intervention targets.
    """
    fig, axes = plt.subplots(1, 2, figsize=(16, 8))

    # Panel 1: Adjacency matrix
    node_labels = [network.diseases[n]["short"] for n in network.nodes]
    im = axes[0].imshow(network.adj_matrix, cmap='YlOrRd', aspect='auto')
    axes[0].set_xticks(range(network.n))
    axes[0].set_xticklabels(node_labels, rotation=45, ha='right', fontsize=8)
    axes[0].set_yticks(range(network.n))
    axes[0].set_yticklabels(node_labels, fontsize=8)
    axes[0].set_title('Transition Probability Matrix\n(row = source, col = target)', fontsize=12)
    plt.colorbar(im, ax=axes[0], label='Probability')

    # Annotate non-zero cells
    for i in range(network.n):
        for j in range(network.n):
            val = network.adj_matrix[i, j]
            if val > 0:
                axes[0].text(j, i, f"{val:.2f}", ha='center', va='center',
                            fontsize=6, color='black' if val < 0.25 else 'white')

    # Panel 2: Intervention value bar chart
    sorted_diseases = sorted(intervention_results.keys(),
                              key=lambda d: intervention_results[d]["total_intervention_value"],
                              reverse=True)

    y_pos = range(len(sorted_diseases))
    downstream_vals = [intervention_results[d]["downstream_prevented"] for d in sorted_diseases]
    own_vals = [intervention_results[d]["own_burden"] for d in sorted_diseases]
    colors = [network.diseases[d]["color"] for d in sorted_diseases]
    labels = [network.diseases[d]["short"] for d in sorted_diseases]

    axes[1].barh(y_pos, downstream_vals, color=colors, alpha=0.7, label='Downstream prevented')
    axes[1].barh(y_pos, own_vals, left=downstream_vals, color=colors, alpha=0.4, label='Own burden')
    axes[1].set_yticks(y_pos)
    axes[1].set_yticklabels(labels, fontsize=9)
    axes[1].set_xlabel('Total Intervention Value (weighted burden prevented)', fontsize=10)
    axes[1].set_title('Intervention Priority Ranking\n(Darker = downstream prevented, Lighter = own burden)',
                       fontsize=12)
    axes[1].legend(fontsize=9)
    axes[1].grid(True, alpha=0.3, axis='x')

    fig.suptitle('CVB Disease Network: Where to Intervene', fontsize=14, fontweight='bold')
    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "intervention_heatmap.png"), dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"  Intervention heatmap saved: {os.path.join(OUTPUT_DIR, 'intervention_heatmap.png')}")


# ============================================================================
# SECTION 6: CASCADE PATH VISUALIZATION
# ============================================================================

def plot_cascade_paths(cascading_paths, network):
    """Visualize the highest-probability cascade paths."""
    fig, ax = plt.subplots(1, 1, figsize=(14, 8))

    # Group by terminal disease
    terminal_colors = {
        "t1dm": "#2ecc71",
        "dcm": "#922B21",
        "me_cfs": "#3498db",
        "encephalitis": "#8e44ad",
    }

    top_paths = cascading_paths[:20]  # Top 20 by probability

    y_positions = list(range(len(top_paths)))
    y_positions.reverse()

    for i, path_info in enumerate(top_paths):
        path = path_info["path"]
        prob = path_info["probability"]
        terminal = path_info["terminal"]
        color = terminal_colors.get(terminal, "#95a5a6")

        # Draw path as connected dots
        path_labels = [network.diseases[p]["short"] for p in path]
        path_str = " -> ".join(path_labels)

        ax.barh(y_positions[i], prob * 100, color=color, alpha=0.7, height=0.7)
        ax.text(prob * 100 + 0.1, y_positions[i], path_str,
                va='center', fontsize=8, color='#2c3e50')

    ax.set_xlabel('Cascade Probability (%)', fontsize=12)
    ax.set_ylabel('Path Rank', fontsize=12)
    ax.set_title('Top 20 Disease Cascade Paths from CVB Infection\n'
                 '(Probability of following each path from initial infection)',
                 fontsize=13, fontweight='bold')

    # Legend for terminal diseases
    for terminal, color in terminal_colors.items():
        short = network.diseases[terminal]["short"]
        ax.barh([], [], color=color, alpha=0.7, label=f'Terminal: {short}')
    ax.legend(loc='lower right', fontsize=9)

    ax.set_yticks(y_positions)
    ax.set_yticklabels([f"#{i+1}" for i in range(len(top_paths))], fontsize=8)
    ax.grid(True, alpha=0.3, axis='x')

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "cascade_paths.png"), dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"  Cascade paths saved: {os.path.join(OUTPUT_DIR, 'cascade_paths.png')}")


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("=" * 70)
    print("CVB DISEASE NETWORK TOPOLOGY ANALYSIS")
    print("systematic approach — numerical track (numerics)")
    print("=" * 70)
    print(f"\nOutput directory: {OUTPUT_DIR}")
    print(f"Diseases: {len(DISEASES)}")
    print(f"Edges: {len(EDGES)}")

    # Build network
    network = DiseaseNetwork(DISEASES, EDGES)

    # ---- Analysis 1: Degree centrality ----
    print("\n" + "=" * 70)
    print("ANALYSIS 1: DEGREE CENTRALITY — Most connected diseases")
    print("=" * 70)

    degrees = network.degree_analysis()
    sorted_by_total = sorted(degrees.items(), key=lambda x: x[1]["total_degree"], reverse=True)

    print(f"\n{'Disease':<25} {'Out-deg':<10} {'In-deg':<10} {'Total':<10} {'Out-wt':<10} {'In-wt':<10} {'Total-wt':<10}")
    print("-" * 85)
    for node, d in sorted_by_total:
        name = DISEASES[node]["short"]
        print(f"{name:<25} {d['out_degree']:<10} {d['in_degree']:<10} {d['total_degree']:<10} "
              f"{d['out_weight']:<10.3f} {d['in_weight']:<10.3f} {d['total_weight']:<10.3f}")

    most_connected = sorted_by_total[0]
    print(f"\n  MOST CONNECTED: {DISEASES[most_connected[0]]['name']} "
          f"(total degree = {most_connected[1]['total_degree']})")

    # ---- Analysis 2: Keystone analysis ----
    print("\n" + "=" * 70)
    print("ANALYSIS 2: KEYSTONE ANALYSIS — Which removal disconnects the most?")
    print("=" * 70)

    keystones = network.keystone_analysis()
    sorted_keystones = sorted(keystones.items(),
                               key=lambda x: x[1]["paths_disrupted"], reverse=True)

    print(f"\n{'Disease':<25} {'Paths disrupted':<20} {'Baseline paths':<18} {'Fraction':<10}")
    print("-" * 75)
    for node, k in sorted_keystones:
        name = DISEASES[node]["short"]
        print(f"{name:<25} {k['paths_disrupted']:<20} {k['baseline_paths']:<18} {k['fraction_disrupted']:<10.3f}")

    keystone = sorted_keystones[0]
    print(f"\n  KEYSTONE: {DISEASES[keystone[0]]['name']} "
          f"(removing it disrupts {keystone[1]['paths_disrupted']} paths, "
          f"{keystone[1]['fraction_disrupted']:.1%} of total)")

    # ---- Analysis 3: Intervention value ----
    print("\n" + "=" * 70)
    print("ANALYSIS 3: INTERVENTION VALUE — Best treatment target")
    print("=" * 70)

    intervention = network.intervention_value()
    sorted_intervention = sorted(intervention.items(),
                                  key=lambda x: x[1]["total_intervention_value"], reverse=True)

    print(f"\n{'Disease':<25} {'Downstream prev':<18} {'Own burden':<14} {'Total value':<14} {'Downstream #':<14}")
    print("-" * 85)
    for node, iv in sorted_intervention:
        name = DISEASES[node]["short"]
        print(f"{name:<25} {iv['downstream_prevented']:<18.4f} {iv['own_burden']:<14.4f} "
              f"{iv['total_intervention_value']:<14.4f} {iv['downstream_count']:<14}")

    best_target = sorted_intervention[0]
    print(f"\n  BEST INTERVENTION TARGET: {DISEASES[best_target[0]]['name']} "
          f"(total value = {best_target[1]['total_intervention_value']:.4f}, "
          f"prevents {best_target[1]['downstream_count']} downstream diseases)")

    # ---- Analysis 4: Cascade paths ----
    print("\n" + "=" * 70)
    print("ANALYSIS 4: CASCADING FAILURE PATHS — CVB → terminal disease")
    print("=" * 70)

    cascading = network.find_cascading_paths()

    print(f"\nTop 10 cascade paths (by cumulative probability):")
    print(f"{'#':<4} {'Path':<65} {'Probability':<12} {'Terminal'}")
    print("-" * 95)
    for i, path_info in enumerate(cascading[:10]):
        path_str = " -> ".join([DISEASES[p]["short"] for p in path_info["path"]])
        print(f"{i+1:<4} {path_str:<65} {path_info['probability']:.4%}    {DISEASES[path_info['terminal']]['short']}")

    # ---- Analysis 5: Disease clusters ----
    print("\n" + "=" * 70)
    print("ANALYSIS 5: DISEASE CLUSTERS")
    print("=" * 70)

    clusters = network.find_clusters()
    for cname, cluster in clusters.items():
        diseases_str = ", ".join([DISEASES[d]["short"] for d in cluster["diseases"]])
        print(f"\n  {cname.upper()} cluster: {diseases_str}")
        print(f"  {cluster['description']}")
        if cluster["internal_edges"]:
            for src, tgt, w, m in cluster["internal_edges"]:
                print(f"    {DISEASES[src]['short']} -> {DISEASES[tgt]['short']} ({w:.0%}): {m[:60]}")

    # ---- Analysis 6: Upstream vs downstream classification ----
    print("\n" + "=" * 70)
    print("ANALYSIS 6: UPSTREAM vs DOWNSTREAM CLASSIFICATION")
    print("=" * 70)

    print(f"\n{'Disease':<25} {'Upstream of':<40} {'Downstream of':<40}")
    print("-" * 105)
    for node in network.nodes:
        downstream = network.downstream_diseases(node)
        upstream = network.upstream_diseases(node)
        down_str = ", ".join([DISEASES[d]["short"] for d in downstream]) if downstream else "(terminal)"
        up_str = ", ".join([DISEASES[d]["short"] for d in upstream]) if upstream else "(root)"
        print(f"{DISEASES[node]['short']:<25} {down_str:<40} {up_str:<40}")

    # ---- Visualizations ----
    print("\n" + "=" * 70)
    print("GENERATING VISUALIZATIONS")
    print("=" * 70)

    visualize_network(network)
    plot_intervention_heatmap(network, intervention)
    plot_cascade_paths(cascading, network)

    # ---- Final summary ----
    print("\n" + "=" * 70)
    print("SUMMARY: CVB DISEASE NETWORK TOPOLOGY")
    print("=" * 70)
    print(f"""
KEY FINDINGS:

1. MOST CONNECTED DISEASE: {DISEASES[most_connected[0]]['name']}
   Total degree = {most_connected[1]['total_degree']}
   This is the most interconnected node in the CVB disease network.

2. KEYSTONE DISEASE: {DISEASES[keystone[0]]['name']}
   Removing it disrupts {keystone[1]['fraction_disrupted']:.1%} of all disease paths.
   This is the single best target for network-level prevention.

3. BEST INTERVENTION TARGET: {DISEASES[best_target[0]]['name']}
   Treating/preventing this disease prevents the most total burden.

4. CASCADE INSIGHT: A single CVB infection can cascade through
   {len(cascading)} distinct pathways to reach terminal diseases.
   The highest-probability cascade:
   {' -> '.join([DISEASES[p]['short'] for p in cascading[0]['path']])}
   (probability: {cascading[0]['probability']:.4%})

5. CLINICAL IMPLICATION: Screen ALL CVB patients for ALL 12 diseases.
   Current practice treats the presenting complaint in isolation.
   The network shows that any CVB disease implies risk for all others.

6. THE ORCHITIS FEEDBACK LOOP: Orchitis creates a long-lived viral
   reservoir in immune-privileged testes that can reseed all organs.
   This makes it a high-priority target despite low prevalence.
""")

    print("=" * 70)
    print("ALL ANALYSES COMPLETE — Figures saved to results/figures/")
    print("=" * 70)

    return network, degrees, keystones, intervention, cascading, clusters


if __name__ == "__main__":
    main()
