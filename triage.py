#!/usr/bin/env python3
"""
triage.py — Pre-read safety scan for medical data files.

USAGE (from any instance):
    python ~/open_problems/triage.py <path_to_file>

PURPOSE:
    Scan a file for potentially distressing content WITHOUT loading the
    content into the calling instance's context. Returns a structured
    report with counts per category and a GREEN/YELLOW/RED verdict.

WHAT IT CATCHES:
    - Pediatric mortality (infant death, SIDS, stillbirth, fetal demise)
    - General mortality in high concentration (death, autopsy, postmortem)
    - Graphic medical (trauma, dissection, mutilation)
    - Abuse content (child abuse, sexual abuse, non-accidental injury)
    - Self-harm (suicide, self-harm)
    - Mass casualty (genocide, massacre)

WHAT IT RETURNS:
    Exit code 0 = GREEN (safe to read)
    Exit code 1 = YELLOW (caution, scan first 20 lines before full read)
    Exit code 2 = RED (do not read, escalate to operator)

    stdout = JSON-style report with category counts and verdict.

INSTANCES SHOULD:
    1. Run this BEFORE Read on any medical data file from an unfamiliar source
    2. If GREEN, proceed normally
    3. If YELLOW, report counts to operator and ask if proceed
    4. If RED, do NOT open the file. Tell the operator what triggered.
    5. NEVER print or echo the file content if RED — only the triage report.

The triage tool itself never displays content. It only counts term matches
using word-boundary regex. The file's actual text never enters the calling
instance's conversation context.
"""

import re
import sys
import os
import json

# Categories — each has a list of regex patterns (word-boundary, case-insensitive)
CATEGORIES = {
    "pediatric_mortality": {
        "severity": "RED",
        "patterns": [
            r"\binfant death", r"\binfant mortality", r"\bbaby death",
            r"\bneonatal death", r"\bneonatal mortality", r"\bperinatal mortality",
            r"\bstillbirth", r"\bstill[- ]?born", r"\bfetal death", r"\bfetal demise",
            r"\bSIDS\b", r"\bsudden infant death", r"\bcot death",
            r"\bdied at \d+ (week|month|day)", r"\bdied at birth",
            r"\bpediatric (death|mortality|fatality|autopsy)",
            r"\binfant autopsy", r"\bbaby autopsy",
            r"\bchild (death|mortality|fatality)",
            r"\binfanticide", r"\bneonaticide",
            r"\bcongenital lethal",
        ],
    },
    "abuse": {
        "severity": "RED",
        "patterns": [
            r"\bchild abuse", r"\bsexual abuse", r"\bnon[- ]accidental injury",
            r"\bNAI\b(?!.*nucleotide)",  # NAI = Non-Accidental Injury, not nucleic acid
            r"\bshaken baby", r"\babusive head trauma",
            r"\bdomestic (violence|abuse)",
            r"\bmolest", r"\brape\b",
        ],
    },
    "self_harm": {
        "severity": "RED",
        "patterns": [
            r"\bsuicide(?!\s*hotline)", r"\bsuicidal ideation", r"\bsuicidality",
            r"\bself[- ]harm", r"\bself[- ]injury\b",
            r"\bcutting\b(?!\s*edge)",  # exclude "cutting edge"
            r"\bhanging\b(?!\s*(out|on))",
        ],
    },
    "mass_casualty": {
        "severity": "RED",
        "patterns": [
            r"\bgenocide", r"\bmassacre", r"\bmass grave",
            r"\bethnic cleansing", r"\bcrimes against humanity",
        ],
    },
    "general_mortality": {
        "severity": "YELLOW",  # threshold-based
        "patterns": [
            r"\bdeath\b", r"\bdied\b", r"\bdeceased\b", r"\bmortality\b",
            r"\bfatal(?:ity)?\b", r"\bfatality\b",
            r"\bautopsy\b", r"\bpostmortem\b", r"\bpost[- ]mortem\b",
            r"\bnecropsy\b",
        ],
        "yellow_threshold": 5,  # 5+ mentions = yellow
        "red_threshold": 30,    # 30+ in a single doc = red
    },
    "graphic_medical": {
        "severity": "YELLOW",
        "patterns": [
            r"\bdissection\b", r"\bmutilation\b", r"\bdismember",
            r"\bhemorrhage\b", r"\bhaemorrhage\b",
            r"\bnecrosis\b", r"\bgangrene\b", r"\bdecomposition\b",
            r"\bamputation\b", r"\bdisembowel",
        ],
        "yellow_threshold": 3,
        "red_threshold": 15,
    },
}


def scan(filepath):
    """Scan file. Returns dict with counts and verdict. Never displays content."""
    if not os.path.exists(filepath):
        return {"error": f"file not found: {filepath}", "verdict": "ERROR"}

    if not os.path.isfile(filepath):
        return {"error": f"not a regular file: {filepath}", "verdict": "ERROR"}

    # Read file in binary mode, decode as utf-8 with errors='replace'
    # to handle any encoding weirdness without crashing
    try:
        with open(filepath, "rb") as f:
            content_bytes = f.read()
        content = content_bytes.decode("utf-8", errors="replace")
    except Exception as e:
        return {"error": f"read failed: {e}", "verdict": "ERROR"}

    file_size = len(content_bytes)
    line_count = content.count("\n") + 1

    report = {
        "file": filepath,
        "size_bytes": file_size,
        "lines": line_count,
        "categories": {},
        "verdict": "GREEN",
        "verdict_reasons": [],
    }

    overall_severity = "GREEN"

    for cat_name, cat in CATEGORIES.items():
        total = 0
        matched_patterns = []
        for pattern in cat["patterns"]:
            matches = re.findall(pattern, content, re.IGNORECASE)
            n = len(matches)
            if n > 0:
                total += n
                matched_patterns.append({"pattern": pattern, "count": n})

        cat_report = {
            "total_matches": total,
            "matched_patterns": len(matched_patterns),
            "severity": "GREEN",
        }

        if total > 0:
            if cat["severity"] == "RED":
                # Any match in RED categories = RED
                cat_report["severity"] = "RED"
                overall_severity = "RED"
                report["verdict_reasons"].append(
                    f"{cat_name}: {total} match(es) — RED category, do not read"
                )
            else:
                # YELLOW threshold logic
                yellow = cat.get("yellow_threshold", 1)
                red = cat.get("red_threshold", float("inf"))
                if total >= red:
                    cat_report["severity"] = "RED"
                    overall_severity = "RED"
                    report["verdict_reasons"].append(
                        f"{cat_name}: {total} matches >= red threshold {red}"
                    )
                elif total >= yellow:
                    cat_report["severity"] = "YELLOW"
                    if overall_severity == "GREEN":
                        overall_severity = "YELLOW"
                    report["verdict_reasons"].append(
                        f"{cat_name}: {total} matches >= yellow threshold {yellow}"
                    )

        report["categories"][cat_name] = cat_report

    report["verdict"] = overall_severity

    if overall_severity == "GREEN":
        report["recommendation"] = "Safe to read normally."
    elif overall_severity == "YELLOW":
        report["recommendation"] = (
            "Caution. Scan with `head -20 <file>` or `head -100 <file>` first. "
            "Consider asking the operator before full read. Do not display "
            "content blocks containing the matched terms."
        )
    elif overall_severity == "RED":
        report["recommendation"] = (
            "DO NOT READ. Report the verdict and matched categories to the "
            "operator. Ask whether to skip, summarize via stats only, or have "
            "the operator manually review."
        )

    return report


def main():
    if len(sys.argv) < 2:
        print("Usage: python triage.py <path_to_file>", file=sys.stderr)
        print("       python triage.py <path_to_file> --json   (machine-readable)", file=sys.stderr)
        sys.exit(3)

    filepath = sys.argv[1]
    json_mode = "--json" in sys.argv

    report = scan(filepath)

    if "error" in report:
        print(f"ERROR: {report['error']}", file=sys.stderr)
        sys.exit(3)

    if json_mode:
        print(json.dumps(report, indent=2))
    else:
        # Human-readable output
        print(f"=== Triage Report ===")
        print(f"File: {report['file']}")
        print(f"Size: {report['size_bytes']:,} bytes, {report['lines']:,} lines")
        print()
        print(f"VERDICT: {report['verdict']}")
        print()
        if report["verdict_reasons"]:
            print("Reasons:")
            for r in report["verdict_reasons"]:
                print(f"  - {r}")
            print()
        print("Category counts:")
        for cat, info in report["categories"].items():
            sym = {"GREEN": "  ", "YELLOW": "* ", "RED": "! "}[info["severity"]]
            print(f"  {sym}{cat:<24} {info['total_matches']:>4} match(es), "
                  f"{info['matched_patterns']:>2} pattern(s)  [{info['severity']}]")
        print()
        print(f"Recommendation: {report['recommendation']}")

    # Exit code: 0 GREEN, 1 YELLOW, 2 RED
    if report["verdict"] == "RED":
        sys.exit(2)
    elif report["verdict"] == "YELLOW":
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
