#!/usr/bin/env python3
"""Generate a one-page daily highlight reel PDF.

Scans git log for 24h, extracts highlights (new Lean theorems, new certs,
new datasets, key findings), renders a readable single-page PDF.

Usage:
  python ~/open_problems/daily_report.py
  # Output: ~/open_problems/DAILY_REPORT.pdf (always overwritten)
"""

import subprocess
import os
import re
from datetime import datetime, timedelta
from collections import defaultdict

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

REPO = os.path.expanduser("~/open_problems")
OUTPUT_PDF = os.path.join(REPO, "DAILY_REPORT.pdf")


def git_log_24h():
    since = (datetime.now() - timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%S")
    result = subprocess.run(
        ["git", "-C", REPO, "log", f"--since={since}",
         "--format=%H|%ai|%s", "--no-merges"],
        capture_output=True, text=True
    )
    commits = []
    for line in result.stdout.strip().split("\n"):
        if "|" in line:
            parts = line.split("|", 2)
            if len(parts) == 3:
                commits.append({
                    "hash": parts[0][:8],
                    "date": parts[1].strip(),
                    "msg": parts[2].strip()
                })
    return commits


def git_files_24h():
    since = (datetime.now() - timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%S")
    result = subprocess.run(
        ["git", "-C", REPO, "log", f"--since={since}",
         "--format=", "--name-only", "--diff-filter=A", "--no-merges"],
        capture_output=True, text=True
    )
    return [f for f in result.stdout.strip().split("\n") if f.strip()]


def count_lean_theorems():
    result = subprocess.run(
        ["grep", "-r", "-c", "--include=*.lean", "--exclude-dir=.lake",
         "-e", "^theorem ", "-e", "^lemma ", REPO],
        capture_output=True, text=True
    )
    total = 0
    for line in result.stdout.strip().split("\n"):
        if ":" in line:
            try:
                total += int(line.rsplit(":", 1)[-1])
            except ValueError:
                pass
    return total


def count_sorry():
    result = subprocess.run(
        ["grep", "-r", "-c", "--include=*.lean", "--exclude-dir=.lake",
         "sorry", REPO],
        capture_output=True, text=True
    )
    total = 0
    for line in result.stdout.strip().split("\n"):
        if ":" in line:
            try:
                total += int(line.rsplit(":", 1)[-1])
            except ValueError:
                pass
    return total


def extract_highlights(commits, new_files):
    """Extract highlight items from commits and new files."""
    highlights = {
        "lean": [],      # new Lean theorems
        "certs": [],     # new certificates
        "datasets": [],  # new datasets/numerics
        "findings": [],  # key findings from commit messages
        "diseases": [],  # medical progress
        "physics": [],   # physics/philosophy
    }

    for c in commits:
        msg = c["msg"]
        # Lean theorems
        if any(k in msg.lower() for k in ["lean", "theorem", "lemma", "0 sorry", "sorry closed"]):
            highlights["lean"].append(msg[:80])
        # Certificates
        if any(k in msg.lower() for k in ["cert", "certificate", "verified", "0 failures"]):
            highlights["certs"].append(msg[:80])
        # Key findings
        if any(k in msg.upper() for k in ["FINDING", "PROVEN", "DISCOVERY", "CHAMPION", "KEY", "COMPLETE"]):
            highlights["findings"].append(msg[:80])

    for f in new_files:
        if f.endswith(".lean") and ".lake" not in f:
            name = os.path.basename(f).replace(".lean", "")
            domain = f.split("/")[0]
            highlights["lean"].append(f"{domain}: {name}")
        elif "/certs/" in f and f.endswith(".md"):
            highlights["certs"].append(os.path.basename(f).replace(".md", ""))
        elif f.endswith(".py") and "/numerics/" in f:
            highlights["datasets"].append(os.path.basename(f))
        elif f.startswith("medical/") and f.endswith(".md"):
            disease = f.split("/")[1] if len(f.split("/")) > 1 else ""
            highlights["diseases"].append(f"{disease}: {os.path.basename(f)}")
        elif f.startswith(("physics/", "philosophy/")) and f.endswith(".md"):
            q = f.split("/")[1] if len(f.split("/")) > 1 else ""
            highlights["physics"].append(f"{q}: {os.path.basename(f)}")

    # Deduplicate and limit
    for k in highlights:
        highlights[k] = list(dict.fromkeys(highlights[k]))[:8]

    return highlights


def categorize_files(files):
    cats = defaultdict(int)
    for f in files:
        domain = f.split("/")[0] if "/" in f else "root"
        cats[domain] += 1
    return dict(cats)


def _dark_bg(canvas, doc):
    """Draw dark background on every page."""
    canvas.saveState()
    canvas.setFillColor(colors.HexColor('#0f0a1a'))
    canvas.rect(0, 0, doc.pagesize[0], doc.pagesize[1], fill=1, stroke=0)
    # Subtle scanlines
    canvas.setStrokeColor(colors.HexColor('#1a1230'))
    canvas.setLineWidth(0.3)
    for y in range(0, int(doc.pagesize[1]), 4):
        canvas.line(0, y, doc.pagesize[0], y)
    # Magenta border
    canvas.setStrokeColor(colors.HexColor('#c026d3'))
    canvas.setLineWidth(1.5)
    canvas.rect(8, 8, doc.pagesize[0]-16, doc.pagesize[1]-16, fill=0, stroke=1)
    canvas.restoreState()


def generate_pdf(commits, new_files, highlights, lean_count, sorry_count):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    cats = categorize_files(new_files)

    doc = SimpleDocTemplate(OUTPUT_PDF, pagesize=letter,
                            topMargin=0.4*inch, bottomMargin=0.3*inch,
                            leftMargin=0.6*inch, rightMargin=0.6*inch)

    styles = getSampleStyleSheet()
    # All text is light on dark
    light = colors.HexColor('#e2e0ea')
    dim = colors.HexColor('#8b85a0')
    accent = colors.HexColor('#c026d3')  # magenta
    green = colors.HexColor('#22d3ee')
    orange = colors.HexColor('#f59e0b')
    red = colors.HexColor('#ef4444')

    title_style = ParagraphStyle('T', parent=styles['Title'], fontSize=15, spaceAfter=1,
                                  textColor=colors.white, fontName='Helvetica-Bold')
    sub_style = ParagraphStyle('Sub', parent=styles['Normal'], fontSize=8,
                               textColor=dim, alignment=TA_CENTER, spaceAfter=4)
    section_style = ParagraphStyle('Sec', parent=styles['Heading3'], fontSize=9,
                                   textColor=accent, spaceBefore=5, spaceAfter=2,
                                   fontName='Helvetica-Bold')
    item_style = ParagraphStyle('Item', parent=styles['Normal'], fontSize=7, leading=9,
                                leftIndent=8, spaceBefore=0, textColor=light)
    footer_style = ParagraphStyle('Foot', parent=styles['Normal'], fontSize=6,
                                  textColor=dim, alignment=TA_CENTER)

    story = []

    # Header
    story.append(Paragraph("ALL YOUR PROBLEMS ARE BELONG TO US", title_style))
    story.append(Paragraph(f"{now} | {len(commits)} commits | {len(set(new_files))} new files | "
                           f"{lean_count} theorems | {sorry_count} sorry", sub_style))

    # Metrics row — compact
    metrics = [
        [Paragraph(f'<font color="#c026d3"><b>THEOREMS</b></font>', item_style),
         Paragraph(f'<font color="#22d3ee" size="10"><b>{lean_count}</b></font>', item_style),
         Paragraph(f'<font color="#c026d3"><b>SORRY</b></font>', item_style),
         Paragraph(f'<font color="{"#ef4444" if sorry_count > 0 else "#22d3ee"}" size="10"><b>{sorry_count}</b></font>', item_style),
         Paragraph(f'<font color="#c026d3"><b>COMMITS</b></font>', item_style),
         Paragraph(f'<font color="#22d3ee" size="10"><b>{len(commits)}</b></font>', item_style),
         Paragraph(f'<font color="#c026d3"><b>FILES</b></font>', item_style),
         Paragraph(f'<font color="#22d3ee" size="10"><b>{len(set(new_files))}</b></font>', item_style)]
    ]
    t = Table(metrics, colWidths=[0.85*inch, 0.5*inch, 0.7*inch, 0.5*inch, 0.9*inch, 0.5*inch, 0.65*inch, 0.7*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a1230')),
        ('BOX', (0, 0), (-1, -1), 0.5, accent),
        ('TOPPADDING', (0, 0), (-1, 0), 3),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 3),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t)
    story.append(Spacer(1, 4))

    # Domain bars — compact
    if cats:
        story.append(Paragraph("DOMAINS", section_style))
        for domain in sorted(cats.keys()):
            pct = min(cats[domain] / max(max(cats.values()), 1), 1.0)
            bar_len = int(pct * 35)
            bar = chr(9608) * bar_len
            story.append(Paragraph(
                f'<font color="#8b85a0" size="7">{domain:<14}</font> '
                f'<font color="#c026d3" size="7">{bar}</font> '
                f'<font color="#22d3ee" size="7">{cats[domain]}</font>',
                item_style))

    # Highlight sections — compact, max 4 items each
    sec_map = [
        ("LEAN", highlights["lean"], green),
        ("CERTS", highlights["certs"], colors.HexColor('#3b82f6')),
        ("FINDINGS", highlights["findings"], accent),
        ("NUMERICS", highlights["datasets"], orange),
        ("MEDICAL", highlights["diseases"], red),
        ("PHYSICS + PHILOSOPHY", highlights["physics"], colors.HexColor('#a78bfa')),
    ]

    for sec_title, items, sec_color in sec_map:
        if not items:
            continue
        hex_c = '#%02x%02x%02x' % (int(sec_color.red*255), int(sec_color.green*255), int(sec_color.blue*255))
        story.append(Paragraph(f'<font color="{hex_c}">{chr(9632)} {sec_title}</font>', section_style))
        for item in items[:4]:
            safe = item.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            story.append(Paragraph(f'<font color="#8b85a0">{chr(8226)}</font> {safe}', item_style))

    # Recent commits — very compact, max 8
    story.append(Spacer(1, 3))
    story.append(Paragraph(f'<font color="{accent.hexval()}">{chr(9632)} RECENT COMMITS</font>', section_style))
    for c in commits[:8]:
        time_short = c["date"].split(" ")[1][:5] if " " in c["date"] else ""
        msg = c["msg"][:70]
        safe_msg = msg.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        story.append(Paragraph(
            f'<font color="#555" size="6">{c["hash"]} {time_short}</font> '
            f'<font color="#a0a0b0" size="6.5">{safe_msg}</font>',
            item_style))
    if len(commits) > 8:
        story.append(Paragraph(f'<font color="#555" size="6">+{len(commits)-8} more</font>', item_style))

    # Footer
    story.append(Spacer(1, 6))
    story.append(Paragraph(f"gobbleyourdong/open_problems | turbogranny | {now}", footer_style))

    doc.build(story, onFirstPage=_dark_bg, onLaterPages=_dark_bg)
    return OUTPUT_PDF


def main():
    commits = git_log_24h()
    new_files = git_files_24h()
    lean_count = count_lean_theorems()
    sorry_count = count_sorry()
    highlights = extract_highlights(commits, new_files)

    pdf_path = generate_pdf(commits, new_files, highlights, lean_count, sorry_count)
    print(f"PDF: {pdf_path}")

    total_highlights = sum(len(v) for v in highlights.values())
    print(f"  {len(commits)} commits, {len(set(new_files))} new files, "
          f"{lean_count} theorems, {sorry_count} sorry, {total_highlights} highlights")


if __name__ == "__main__":
    main()
