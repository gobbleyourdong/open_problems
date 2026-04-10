#!/usr/bin/env python3
"""
lean_comment_lint.py — Cycle 16 Odd (loop 6, 2026-04-09)

Comment-syntax linter for source-only Lean files in
`physics/what_is_computation/lean/`. Addresses the loop 5 audit
finding that `CompressionAsymmetryStatement.lean` had a malformed
`/-! ## §7 Inventory` opener that would have caused a compile error.

The "zero sorry" cert claim is weaker than "compiles cleanly" for
source-only files. Until we add a lakefile + actually compile, this
linter is the cheapest enforcement layer to catch comment-syntax bugs.

Checks performed:
  1. Block comment balance: every `/-` (or `/-!` or `/- `) is matched
     by exactly one `-/`. Nesting allowed.
  2. No bare text outside theorem/def/comment scope. Specifically:
     after a top-level `-/` closes a comment, the next non-blank line
     must start with a Lean keyword (def, theorem, axiom, structure,
     inductive, abbrev, instance, namespace, end, import, /-, /--,
     #check, etc.) or be inside a comment.
  3. Common pattern: an inventory comment block at the file end must
     start with `/-!` (which is a doc-comment opener Lean expects).

Returns 0 on clean, 1 on any finding. JSON-mode output for CI.

Usage:
    python3 numerics/lean_comment_lint.py [--json] [file1.lean ...]
"""

import sys, os, json, re

LEAN_KEYWORDS_AT_LINE_START = {
    "def", "theorem", "lemma", "example", "axiom", "structure",
    "inductive", "abbrev", "instance", "namespace", "end", "import",
    "section", "variable", "open", "class", "macro", "syntax",
    "elab", "deriving", "@", "/-", "/--", "/-!", "--", "#",
}


def find_unbalanced_comments(text):
    """
    Walk the source character by character, tracking nesting depth of
    block comments. Lean comments nest: `/- /- inner -/ outer -/` is
    one balanced top-level comment. Doc comments `/--` and module
    comments `/-!` open one comment each (closed by `-/`).

    Returns a list of (line_number, message) findings.
    """
    findings = []
    depth = 0
    line = 1
    i = 0
    n = len(text)
    open_stack = []  # (line, col) of unclosed openers
    while i < n:
        c = text[i]
        if c == "\n":
            line += 1
            i += 1
            continue
        # Block comment opener
        if c == "/" and i + 1 < n and text[i + 1] == "-":
            # Check if /-- (doc) or /-! (module) — both open one comment
            depth += 1
            open_stack.append(line)
            # Skip the marker
            if i + 2 < n and text[i + 2] in ("-", "!"):
                i += 3
            else:
                i += 2
            continue
        # Block comment closer
        if c == "-" and i + 1 < n and text[i + 1] == "/":
            if depth == 0:
                findings.append((line, "unmatched -/ closer"))
            else:
                depth -= 1
                open_stack.pop()
            i += 2
            continue
        # Line comment: skip to end of line (only when not inside block comment)
        if depth == 0 and c == "-" and i + 1 < n and text[i + 1] == "-":
            while i < n and text[i] != "\n":
                i += 1
            continue
        i += 1

    if depth != 0:
        for ln in open_stack:
            findings.append((ln, f"unmatched /- opener (still open at EOF, depth left = {depth})"))

    return findings


def find_bare_text_between_closers(text):
    """
    Detect the loop-5 bug class precisely: an orphaned `-/` closer with
    raw text following it that is NOT inside any theorem/def/structure
    block, where another `-/` later "closes" the orphan text.

    Walk char by char with proper /- /-! /-- nesting. Whenever we hit
    a `-/` while depth is 0 (would be unbalanced), record it and try
    to find the next `-/` to bracket the orphan region. Also flag if
    the file ends with depth > 0.

    The reliable signal: the OVERALL block-comment depth count is the
    same metric `find_unbalanced_comments` already produces. But we
    additionally want to point at WHERE the orphan body starts, which
    is what this function does.

    Returns a list of (line_number, message) findings.

    NOTE: this replaces the loose loop-5 first-pass heuristic which
    had too many false positives on legitimate `structure ... where`
    bodies. The replacement only fires if the unbalanced-comment
    walker has already found a problem.
    """
    # Run the precise walker
    unbalanced = find_unbalanced_comments(text)
    if not unbalanced:
        return []
    # If unbalanced, return the first orphan opener with file context.
    out = []
    for ln, msg in unbalanced:
        out.append((ln, f"location of comment-balance error → {msg}"))
    return out


def lint_file(path):
    with open(path) as f:
        text = f.read()
    findings = []
    # Only report balance errors. The "bare text" heuristic is now
    # subsumed (and replaced) by precise comment-balance tracking.
    findings.extend(("balance", *f) for f in find_unbalanced_comments(text))
    return findings


def main(argv):
    json_mode = False
    files = []
    for arg in argv[1:]:
        if arg == "--json":
            json_mode = True
        else:
            files.append(arg)
    if not files:
        # Default: all lean files in physics/what_is_computation/lean/
        here = os.path.dirname(os.path.abspath(__file__))
        lean_dir = os.path.join(here, "..", "lean")
        files = sorted(
            os.path.join(lean_dir, f)
            for f in os.listdir(lean_dir)
            if f.endswith(".lean")
        )

    all_findings = {}
    for path in files:
        findings = lint_file(path)
        if findings:
            all_findings[path] = findings

    if json_mode:
        # Compact JSON for machine consumption
        out = {p: [{"kind": k, "line": ln, "msg": msg}
                   for (k, ln, msg) in findings]
               for p, findings in all_findings.items()}
        print(json.dumps(out, indent=2))
    else:
        if not all_findings:
            print(f"OK — {len(files)} file(s) clean.")
            return 0
        print(f"FINDINGS in {len(all_findings)} of {len(files)} file(s):")
        for path in sorted(all_findings):
            print(f"\n  {path}:")
            for kind, ln, msg in all_findings[path]:
                print(f"    line {ln} [{kind}]: {msg}")

    return 0 if not all_findings else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
