#!/usr/bin/env python3
"""Generate a daily summary PDF of all open_problems activity.

Scans git log for the last 24 hours, counts files changed per domain,
lists key findings, and renders to a single PDF that overwrites itself.

Usage:
  python ~/open_problems/daily_report.py
  # Output: ~/open_problems/DAILY_REPORT.pdf (always overwritten)
"""

import subprocess
import os
import json
from datetime import datetime, timedelta
from collections import defaultdict

# Try reportlab
try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units import inch
    from reportlab.lib import colors
    from reportlab.platypus import (
        SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, HRFlowable
    )
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_CENTER, TA_LEFT
    HAS_REPORTLAB = True
except ImportError:
    HAS_REPORTLAB = False
    print("reportlab not installed, generating markdown instead")

REPO = os.path.expanduser("~/open_problems")
OUTPUT_PDF = os.path.join(REPO, "DAILY_REPORT.pdf")
OUTPUT_MD = os.path.join(REPO, "DAILY_REPORT.md")


def git_log_24h():
    """Get commits from the last 24 hours."""
    since = (datetime.now() - timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%S")
    result = subprocess.run(
        ["git", "-C", REPO, "log", f"--since={since}", "--format=%H|%ai|%s", "--no-merges"],
        capture_output=True, text=True
    )
    commits = []
    for line in result.stdout.strip().split("\n"):
        if "|" in line:
            parts = line.split("|", 2)
            if len(parts) == 3:
                commits.append({"hash": parts[0][:8], "date": parts[1].strip(), "msg": parts[2].strip()})
    return commits


def git_diff_stats_24h():
    """Get file change stats from the last 24 hours."""
    since = (datetime.now() - timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%S")
    result = subprocess.run(
        ["git", "-C", REPO, "log", f"--since={since}", "--format=", "--name-only", "--no-merges"],
        capture_output=True, text=True
    )
    files = [f for f in result.stdout.strip().split("\n") if f.strip()]
    return files


def categorize_files(files):
    """Categorize changed files by domain."""
    cats = defaultdict(list)
    for f in files:
        if f.startswith("math/"):
            problem = f.split("/")[1] if len(f.split("/")) > 1 else "root"
            cats[f"math/{problem}"].append(f)
        elif f.startswith("medical/"):
            disease = f.split("/")[1] if len(f.split("/")) > 1 else "root"
            cats[f"medical/{disease}"].append(f)
        elif f.startswith("physics/"):
            question = f.split("/")[1] if len(f.split("/")) > 1 else "root"
            cats[f"physics/{question}"].append(f)
        elif f.startswith("philosophy/"):
            question = f.split("/")[1] if len(f.split("/")) > 1 else "root"
            cats[f"philosophy/{question}"].append(f)
        else:
            cats["root"].append(f)
    return dict(cats)


def count_lean_theorems():
    """Count lean theorems across the repo, excluding .lake build caches."""
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
    """Count sorry instances in lean files, excluding .lake build caches."""
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


def generate_md(commits, files, categories, lean_count, sorry_count):
    """Generate markdown report."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        f"# Daily Report — {now}",
        "",
        f"**Commits (24h):** {len(commits)}",
        f"**Files changed:** {len(set(files))}",
        f"**Lean theorems (total):** {lean_count}",
        f"**Sorry count:** {sorry_count}",
        "",
        "## Activity by Domain",
        "",
        "| Domain | Files Changed |",
        "|--------|:------------:|",
    ]
    for cat in sorted(categories.keys()):
        lines.append(f"| `{cat}` | {len(categories[cat])} |")

    lines.extend(["", "## Commits", "", "| Hash | Time | Message |", "|------|------|---------|"])
    for c in commits[:30]:
        msg = c["msg"][:80]
        time_short = c["date"].split(" ")[1][:5] if " " in c["date"] else c["date"]
        lines.append(f"| `{c['hash']}` | {time_short} | {msg} |")
    if len(commits) > 30:
        lines.append(f"| ... | | +{len(commits)-30} more |")

    lines.extend([
        "",
        "## Key Metrics",
        "",
        f"- **7 Clay Millennium Prize Problems** active",
        f"- **15 CVB diseases** mapped",
        f"- **6 physics** tier-0 questions scaffolded",
        f"- **9 philosophy** tier-0 questions scaffolded",
        f"- **{lean_count} Lean theorems**, {sorry_count} sorry",
        "",
        "---",
        f"*Generated {now} by daily_report.py*",
    ])
    return "\n".join(lines)


def generate_pdf(md_content, commits, files, categories, lean_count, sorry_count):
    """Generate PDF report using reportlab."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    doc = SimpleDocTemplate(OUTPUT_PDF, pagesize=letter,
                            topMargin=0.5*inch, bottomMargin=0.5*inch,
                            leftMargin=0.6*inch, rightMargin=0.6*inch)
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('Title2', parent=styles['Title'], fontSize=18, spaceAfter=4)
    subtitle_style = ParagraphStyle('Sub', parent=styles['Normal'], fontSize=10,
                                    textColor=colors.HexColor('#555555'), alignment=TA_CENTER)
    section_style = ParagraphStyle('Section', parent=styles['Heading2'], fontSize=13,
                                    spaceBefore=10, spaceAfter=4)
    cell_style = ParagraphStyle('Cell', parent=styles['Normal'], fontSize=8.5, leading=10)
    metric_style = ParagraphStyle('Metric', parent=styles['Normal'], fontSize=10, spaceBefore=2)

    header_bg = colors.HexColor('#1a1a2e')

    story = []
    story.append(Paragraph("ALL YOUR PROBLEMS ARE BELONG TO US", title_style))
    story.append(Paragraph(f"Daily Report — {now}", subtitle_style))
    story.append(Spacer(1, 10))

    # Key metrics
    story.append(Paragraph("Key Metrics", section_style))
    metrics_data = [
        ["Commits (24h)", str(len(commits))],
        ["Files changed", str(len(set(files)))],
        ["Lean theorems", str(lean_count)],
        ["Sorry count", str(sorry_count)],
        ["Clay problems", "7"],
        ["CVB diseases", "15"],
        ["Physics questions", "6"],
        ["Philosophy questions", "9"],
    ]
    t = Table(metrics_data, colWidths=[3*inch, 1.5*inch])
    t.setStyle(TableStyle([
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t)
    story.append(Spacer(1, 10))

    # Activity by domain
    story.append(Paragraph("Activity by Domain", section_style))
    domain_data = [["Domain", "Files"]]
    for cat in sorted(categories.keys()):
        domain_data.append([cat, str(len(categories[cat]))])
    if domain_data:
        t2 = Table(domain_data, colWidths=[4*inch, 1*inch], repeatRows=1)
        t2.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), header_bg),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8.5),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
            ('TOPPADDING', (0, 0), (-1, -1), 2),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ]))
        story.append(t2)
    story.append(Spacer(1, 10))

    # Recent commits
    story.append(Paragraph("Recent Commits", section_style))
    commit_data = [["Hash", "Time", "Message"]]
    for c in commits[:25]:
        time_short = c["date"].split(" ")[1][:5] if " " in c["date"] else ""
        msg = c["msg"][:70]
        commit_data.append([c["hash"], time_short, Paragraph(msg, cell_style)])
    t3 = Table(commit_data, colWidths=[0.7*inch, 0.6*inch, 5.5*inch], repeatRows=1)
    t3.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), header_bg),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 7.5),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(t3)

    story.append(Spacer(1, 15))
    story.append(Paragraph(f"Generated {now} by daily_report.py",
                            ParagraphStyle('Footer', parent=styles['Normal'],
                                          fontSize=7, textColor=colors.HexColor('#888888'),
                                          alignment=TA_CENTER)))

    doc.build(story)
    return OUTPUT_PDF


def main():
    commits = git_log_24h()
    files = git_diff_stats_24h()
    categories = categorize_files(files)
    lean_count = count_lean_theorems()
    sorry_count = count_sorry()

    md = generate_md(commits, files, categories, lean_count, sorry_count)

    if HAS_REPORTLAB:
        pdf_path = generate_pdf(md, commits, files, categories, lean_count, sorry_count)
        print(f"PDF: {pdf_path}")
    else:
        with open(OUTPUT_MD, "w") as f:
            f.write(md)
        print(f"MD: {OUTPUT_MD}")

    print(f"  {len(commits)} commits, {len(set(files))} files, {lean_count} theorems, {sorry_count} sorry")


if __name__ == "__main__":
    main()
