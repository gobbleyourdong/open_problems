#!/usr/bin/env python3
"""
Dysbiosis-framework analyzer — turns Bracken/Kraken output into the framework's
own constructs with transparent, inspectable math (no DIAMOND, no black box).

Computes: the 6 Run-004 metrics + transparent functional indices (butyrate
capacity, H2S/sulfate-reducers, hexa-vs-penta LPS) + the Node-A Treg proxy,
each flagged against framework thresholds, with the contributing taxa shown.

Usage:
  python3 framework_analyze.py [--results DIR]
Defaults to ../results relative to this file. Pure stdlib.
"""
import argparse, json, os, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from taxon_functions import FUNCTIONS, PHYLUM_SYNONYMS, THRESHOLDS  # noqa


def load_bracken(path):
    """Return [{name, pct, reads}] from a Bracken table (skips header)."""
    rows = []
    if not os.path.exists(path):
        return rows
    with open(path) as f:
        for line in f:
            p = line.rstrip("\n").split("\t")
            if len(p) < 7 or p[0] == "name":
                continue
            try:
                rows.append({"name": p[0], "reads": int(p[5]), "pct": float(p[6]) * 100})
            except ValueError:
                continue
    return rows


def category_summary(species, category):
    """Sum relative abundance over taxa matching a function category (dedup per taxon)."""
    patterns = FUNCTIONS[category]
    contributors = {}
    for sp in species:
        nlow = sp["name"].lower()
        best_w = None
        for sub, w, _note in patterns:
            if sub in nlow:
                best_w = w if best_w is None else max(best_w, w)
        if best_w is not None:
            contributors[sp["name"]] = (sp["pct"], best_w)
    total_pct = sum(v[0] for v in contributors.values())
    weighted = sum(v[0] * v[1] for v in contributors.values())
    top = sorted(contributors.items(), key=lambda kv: kv[1][0], reverse=True)
    return {
        "pct": round(total_pct, 3),
        "weighted_index": round(weighted, 3),
        "n_taxa": len(contributors),
        "top": [(n, round(p, 3)) for n, (p, _w) in top[:6]],
    }


def find_species(species, sub):
    sub = sub.lower()
    hits = [s for s in species if sub in s["name"].lower()]
    return round(sum(h["pct"] for h in hits), 3), [(h["name"], round(h["pct"], 3)) for h in hits]


def phylum_pct(phyla, key):
    syns = PHYLUM_SYNONYMS[key]
    for ph in phyla:
        if any(s in ph["name"].lower() for s in syns):
            return round(ph["pct"], 3)
    return 0.0


def crassphage(kraken_report):
    """Detect CrAssphage / crAss-like phage from the kraken report."""
    if not os.path.exists(kraken_report):
        return {"detected": False, "lines": []}
    found = []
    with open(kraken_report) as f:
        for line in f:
            low = line.lower()
            if "crassvir" in low or "crass-like" in low or "crassphage" in low or "caudoviric" in low:
                p = line.split("\t")
                if len(p) >= 6:
                    found.append({"name": p[5].strip(), "reads": int(p[2]), "pct": float(p[0])})
    return {"detected": any("crass" in x["name"].lower() for x in found), "lines": found}


def flag(value, healthy=None, concerning_below=None, healthy_below=None, concerning_above=None):
    if concerning_below is not None and value < concerning_below:
        return "RED"
    if healthy is not None and value >= healthy:
        return "GREEN"
    if concerning_above is not None and value > concerning_above:
        return "RED"
    if healthy_below is not None and value <= healthy_below:
        return "GREEN"
    return "AMBER"


def main():
    ap = argparse.ArgumentParser()
    here = Path(__file__).resolve().parent
    ap.add_argument("--results", default=str(here.parent / "results"))
    a = ap.parse_args()
    R = Path(a.results)

    species = load_bracken(R / "bracken_species.txt")
    phyla = load_bracken(R / "bracken_phylum.txt")
    if not species:
        sys.exit(f"no bracken_species.txt in {R}")

    # ---- the 6 Run-004 metrics ----
    fprau_pct, fprau_hits = find_species(species, "faecalibacterium prausnitzii")
    fprau_genus, _ = find_species(species, "faecalibacterium")
    akk_pct, akk_hits = find_species(species, "akkermansia")
    prot_pct = phylum_pct(phyla, "proteobacteria")
    hist = category_summary(species, "histamine_producers")
    crass = crassphage(R / "kraken_report.txt")
    candida_pct, candida_hits = find_species(species, "candida")

    # ---- transparent functional indices ----
    butyrate = category_summary(species, "butyrate_producers")
    h2s = category_summary(species, "sulfate_reducers_h2s")
    hexa = category_summary(species, "hexa_lps_proinflammatory")
    penta = category_summary(species, "penta_lps_immunoinhibitory")
    hexa_penta_ratio = round(hexa["pct"] / (hexa["pct"] + penta["pct"]), 3) if (hexa["pct"] + penta["pct"]) else 0.0
    mucin = category_summary(species, "mucin_degraders")

    # ---- Node A (Treg) proxy: butyrate keystones present ----
    node_a = round(fprau_pct + akk_pct, 3)

    metrics = {
        "f_prausnitzii_pct": {"value": fprau_pct, "genus_pct": fprau_genus,
                              "flag": flag(fprau_pct, **THRESHOLDS["f_prausnitzii_pct"]), "taxa": fprau_hits},
        "akkermansia_pct":   {"value": akk_pct, "flag": flag(akk_pct, **THRESHOLDS["akkermansia_pct"]), "taxa": akk_hits},
        "proteobacteria_pct":{"value": prot_pct, "flag": flag(prot_pct, **THRESHOLDS["proteobacteria_pct"])},
        "histamine_producers_pct": {"value": hist["pct"], "flag": flag(hist["pct"], **THRESHOLDS["histamine_pct"]), "top": hist["top"]},
        "crassphage": crass,
        "candida_pct": {"value": candida_pct, "taxa": candida_hits},
    }
    indices = {
        "butyrate_capacity_pct": {"value": butyrate["pct"], "weighted": butyrate["weighted_index"],
                                  "flag": flag(butyrate["pct"], **THRESHOLDS["butyrate_capacity_pct"]), "top": butyrate["top"]},
        "h2s_sulfate_reducer_pct": {"value": h2s["pct"], "flag": flag(h2s["pct"], **THRESHOLDS["sulfate_reducer_pct"]), "top": h2s["top"]},
        "hexa_lps_pct": {"value": hexa["pct"], "top": hexa["top"]},
        "penta_lps_pct": {"value": penta["pct"], "top": penta["top"]},
        "hexa_penta_lps_ratio": {"value": hexa_penta_ratio, "flag": flag(hexa_penta_ratio, **THRESHOLDS["hexa_penta_ratio"])},
        "mucin_degraders_pct": {"value": mucin["pct"], "top": mucin["top"]},
        "node_a_treg_proxy_pct": {"value": node_a, "note": "F. prausnitzii + Akkermansia (butyrate/barrier keystones)"},
    }
    out = {"metrics": metrics, "indices": indices,
           "note": "Relative abundances among classified microbial reads (Bracken fraction_total_reads). Indices are our transparent taxon->function sums; see taxon_functions.py."}

    (R / "P0_framework.json").write_text(json.dumps(out, indent=2))

    # ---- markdown report ----
    def fl(x):  # emoji flag
        return {"GREEN": "🟢", "AMBER": "🟡", "RED": "🔴"}.get(x, "")
    L = []
    L.append("# P0 — Framework-Native Microbiome Report")
    L.append("> Generated by `tools/framework_analyze.py` from Bracken output. Transparent math, no DIAMOND/black box.")
    L.append("> Abundances are relative to **classified microbial reads**.\n")
    L.append("## The 6 metrics")
    L.append(f"- {fl(metrics['f_prausnitzii_pct']['flag'])} **F. prausnitzii**: {fprau_pct}% (genus {fprau_genus}%) — Node A Treg proxy")
    L.append(f"- {fl(metrics['akkermansia_pct']['flag'])} **Akkermansia**: {akk_pct}%")
    L.append(f"- {fl(metrics['proteobacteria_pct']['flag'])} **Proteobacteria**: {prot_pct}%")
    L.append(f"- {fl(metrics['histamine_producers_pct']['flag'])} **Histamine producers**: {hist['pct']}% {hist['top'] or ''}")
    L.append(f"- {'🟢' if crass['detected'] else '🔴'} **CrAssphage**: {'detected' if crass['detected'] else 'not detected'} ({len(crass['lines'])} viral lines)")
    L.append(f"- {'🟢' if candida_pct < 0.5 else '🔴'} **Candida/fungi**: {candida_pct}%")
    L.append("\n## Transparent functional indices (our math)")
    L.append(f"- {fl(indices['butyrate_capacity_pct']['flag'])} **Butyrate capacity**: {butyrate['pct']}% of microbiome are butyrate producers → {butyrate['top'][:4]}")
    L.append(f"- {fl(indices['h2s_sulfate_reducer_pct']['flag'])} **H₂S / sulfate-reducers**: {h2s['pct']}% → {h2s['top'] or 'none detected'}")
    L.append(f"- {fl(indices['hexa_penta_lps_ratio']['flag'])} **Hexa:penta LPS ratio**: {hexa_penta_ratio}  (hexa {hexa['pct']}% / penta {penta['pct']}%)")
    L.append(f"  - hexa (pro-inflammatory): {hexa['top'][:3]}")
    L.append(f"  - penta (immuno-inhibitory): {penta['top'][:3]}")
    L.append(f"- **Mucin degraders**: {mucin['pct']}% → {mucin['top'][:4]}")
    L.append(f"- **Node A (Treg) proxy**: {node_a}% (F. prausnitzii + Akkermansia)")
    L.append("\n_Thresholds & taxon→function tables: `tools/taxon_functions.py` (extensible, cited)._")
    (R / "P0_framework_report.md").write_text("\n".join(L) + "\n")
    print("\n".join(L))
    print(f"\n[wrote {R/'P0_framework_report.md'} and P0_framework.json]")


if __name__ == "__main__":
    main()
