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


def generate_pdf(commits, new_files, highlights, lean_count, sorry_count):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    cats = categorize_files(new_files)

    doc = SimpleDocTemplate(OUTPUT_PDF, pagesize=letter,
                            topMargin=0.4*inch, bottomMargin=0.3*inch,
                            leftMargin=0.5*inch, rightMargin=0.5*inch)

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('T', parent=styles['Title'], fontSize=16, spaceAfter=2)
    sub_style = ParagraphStyle('Sub', parent=styles['Normal'], fontSize=9,
                               textColor=colors.HexColor('#666'), alignment=TA_CENTER, spaceAfter=6)
    section_style = ParagraphStyle('Sec', parent=styles['Heading3'], fontSize=11,
                                   textColor=colors.HexColor('#1a1a2e'), spaceBefore=8, spaceAfter=3)
    item_style = ParagraphStyle('Item', parent=styles['Normal'], fontSize=8, leading=10,
                                leftIndent=10, spaceBefore=1)
    metric_style = ParagraphStyle('Met', parent=styles['Normal'], fontSize=9)
    footer_style = ParagraphStyle('Foot', parent=styles['Normal'], fontSize=7,
                                  textColor=colors.HexColor('#999'), alignment=TA_CENTER)

    accent = colors.HexColor('#6b21a8')
    header_bg = colors.HexColor('#1a1a2e')

    story = []

    # Header
    story.append(Paragraph("ALL YOUR PROBLEMS — Daily Highlights", title_style))
    story.append(Paragraph(f"{now} | {len(commits)} commits | {len(set(new_files))} new files", sub_style))

    # Metrics bar
    metrics = [
        ["Lean Theorems", str(lean_count), "Sorry", str(sorry_count),
         "Commits (24h)", str(len(commits)), "New Files", str(len(set(new_files)))]
    ]
    t = Table(metrics, colWidths=[1.1*inch, 0.6*inch, 0.6*inch, 0.5*inch,
                                   1.1*inch, 0.6*inch, 0.8*inch, 0.6*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#f3e8ff')),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('FONTNAME', (2, 0), (2, 0), 'Helvetica-Bold'),
        ('FONTNAME', (4, 0), (4, 0), 'Helvetica-Bold'),
        ('FONTNAME', (6, 0), (6, 0), 'Helvetica-Bold'),
        ('ALIGN', (1, 0), (1, 0), 'CENTER'),
        ('ALIGN', (3, 0), (3, 0), 'CENTER'),
        ('ALIGN', (5, 0), (5, 0), 'CENTER'),
        ('ALIGN', (7, 0), (7, 0), 'CENTER'),
        ('TEXTCOLOR', (1, 0), (1, 0), accent),
        ('TEXTCOLOR', (3, 0), (3, 0), colors.red if sorry_count > 0 else colors.green),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#d8b4fe')),
        ('TOPPADDING', (0, 0), (-1, 0), 4),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 4),
    ]))
    story.append(t)
    story.append(Spacer(1, 6))

    # Domain activity bar
    if cats:
        story.append(Paragraph("Activity by Domain", section_style))
        domain_items = []
        for domain in sorted(cats.keys()):
            bar_len = min(cats[domain], 40)
            bar = chr(9608) * bar_len
            domain_items.append([domain, str(cats[domain]), bar])
        dt = Table(domain_items, colWidths=[1.2*inch, 0.5*inch, 5*inch])
        dt.setStyle(TableStyle([
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('TEXTCOLOR', (2, 0), (2, -1), accent),
            ('TOPPADDING', (0, 0), (-1, -1), 1),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ]))
        story.append(dt)
        story.append(Spacer(1, 4))

    # Highlight sections — only show non-empty ones
    sections = [
        ("New Lean Theorems", highlights["lean"], colors.HexColor('#059669')),
        ("Certificates & Verifications", highlights["certs"], colors.HexColor('#0284c7')),
        ("Key Findings", highlights["findings"], accent),
        ("New Numerics / Datasets", highlights["datasets"], colors.HexColor('#d97706')),
        ("Medical Progress", highlights["diseases"], colors.HexColor('#dc2626')),
        ("Physics & Philosophy", highlights["physics"], colors.HexColor('#7c3aed')),
    ]

    for sec_title, items, sec_color in sections:
        if not items:
            continue
        story.append(Paragraph(f'<font color="#{sec_color.hexval()[2:]}">{chr(9632)}</font> {sec_title}',
                               section_style))
        for item in items[:6]:
            # Escape XML entities
            safe = item.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            story.append(Paragraph(f'<font color="#666">{chr(8226)}</font> {safe}', item_style))

    # Top commits (compact)
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#e5e7eb')))
    story.append(Paragraph("Recent Commits", section_style))

    commit_lines = []
    for c in commits[:12]:
        time_short = c["date"].split(" ")[1][:5] if " " in c["date"] else ""
        msg = c["msg"][:75]
        safe_msg = msg.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        commit_lines.append(
            Paragraph(f'<font color="#999" size="7">{c["hash"]} {time_short}</font> '
                      f'<font size="7.5">{safe_msg}</font>', item_style)
        )
    for cl in commit_lines:
        story.append(cl)

    if len(commits) > 12:
        story.append(Paragraph(f'<font color="#999" size="7">... +{len(commits)-12} more</font>',
                               item_style))

    # Footer
    story.append(Spacer(1, 8))
    story.append(Paragraph(f"Generated {now} | gobbleyourdong/open_problems | turbogranny",
                           footer_style))

    doc.build(story)
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
