#!/usr/bin/env python3
"""Generate a printable PDF supplement schedule."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

output_path = "~/Downloads/CVB_Protocol_Schedule.pdf"

doc = SimpleDocTemplate(
    output_path,
    pagesize=letter,
    topMargin=0.5*inch,
    bottomMargin=0.5*inch,
    leftMargin=0.6*inch,
    rightMargin=0.6*inch,
)

styles = getSampleStyleSheet()
title_style = ParagraphStyle('Title2', parent=styles['Title'], fontSize=18, spaceAfter=2)
section_style = ParagraphStyle('Section', parent=styles['Heading2'], fontSize=13,
                                textColor=colors.HexColor('#1a1a2e'), spaceBefore=10, spaceAfter=4)
note_style = ParagraphStyle('Note', parent=styles['Normal'], fontSize=8,
                            textColor=colors.HexColor('#555555'), spaceBefore=2)
rule_style = ParagraphStyle('Rule', parent=styles['Normal'], fontSize=8.5,
                            spaceBefore=1, spaceAfter=1, leftIndent=10)
cell_style = ParagraphStyle('Cell', parent=styles['Normal'], fontSize=9, leading=11)
bold_cell = ParagraphStyle('BoldCell', parent=cell_style, fontName='Helvetica-Bold')
small_style = ParagraphStyle('Small', parent=styles['Normal'], fontSize=7.5,
                              textColor=colors.HexColor('#666666'))

story = []

# Title
story.append(Paragraph("CVB Protocol — Daily Supplement Schedule", title_style))
story.append(Paragraph("the patient | Updated 2026-04-08 | 12 supplements + WHM + 18:6 IF", note_style))
story.append(Spacer(1, 8))

# Color scheme
header_bg = colors.HexColor('#1a1a2e')
header_fg = colors.white
morning_bg = colors.HexColor('#e8f4f8')
bhb_bg = colors.HexColor('#fff3e0')
meal1_bg = colors.HexColor('#e8f5e9')
meal2_bg = colors.HexColor('#f3e5f5')
bed_bg = colors.HexColor('#fce4ec')

def make_table(data, col_widths, bg_color):
    t = Table(data, colWidths=col_widths, repeatRows=1)
    style_cmds = [
        ('BACKGROUND', (0, 0), (-1, 0), header_bg),
        ('TEXTCOLOR', (0, 0), (-1, 0), header_fg),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTSIZE', (0, 1), (-1, -1), 8.5),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
    ]
    for i in range(1, len(data)):
        style_cmds.append(('BACKGROUND', (0, i), (-1, i), bg_color))
    t.setStyle(TableStyle(style_cmds))
    return t

w = 7.0 * inch  # total table width

# MORNING FASTED
story.append(Paragraph("MORNING FASTED (7-8am)", section_style))
data = [
    ['Supplement', 'Dose', 'Why'],
    ['NAC (Thorne)', '500mg', 'Glutathione. Lysosomal protection. ROS->NF-\u03baB block.'],
    ['Alpha-Lipoic Acid (Thorne)', '1 cap', 'Insulin sensitizer + universal antioxidant.'],
    ['LGG Probiotic (SuperSmart)', '1 cap (10B CFU)', 'Treg induction in gut. Empty stomach = survives acid.'],
    ['Complete Biotic (Healus)', '1 cap', 'Tributyrin = butyrate prodrug. HDAC->FOXP3->Tregs.'],
]
story.append(make_table(data, [2.0*inch, 1.2*inch, 3.8*inch], morning_bg))

# BHB WINDOW
story.append(Paragraph("BHB WINDOW (hour 14-16 of fast, ~10-11am)", section_style))
data = [
    ['Supplement', 'Dose', 'Why'],
    ['BHB Salts (Nutricost)', '1 scoop in water', 'NLRP3 BLOCKED. Prevents K+ efflux + ASC assembly. Target >1mM.'],
]
story.append(make_table(data, [2.0*inch, 1.2*inch, 3.8*inch], bhb_bg))

# MEAL 1
story.append(Paragraph("WITH FIRST MEAL (12-1pm, breaking fast)", section_style))
data = [
    ['Supplement', 'Dose', 'Why'],
    ['D3+K2 (Sports Research)', '1 softgel (5000IU/100mcg)', 'Fat-soluble. VDR->AMPK. K2 directs Ca to bones.'],
    ['Omega-3 (Sports Research)', '2 softgels (2080mg)', 'NF-\u03baB Signal 1 suppression + resolvins.'],
    ['Selenium (Thorne)', '200mcg', 'GPx cofactor. Lysosomal membrane protection.'],
    ['Zinc Picolinate (Thorne)', '15mg', 'Autophagosome-lysosome fusion cofactor.'],
    ['GABA (Pharma GABA)', '250mg', 'GABA-R on immune cells. Treg support.'],
    ['Berberine (Thorne)', '500mg', 'AMPK + glucose spike blunting + indirect OSBP.'],
    ['Red Yeast Rice+CoQ10 (Thorne)', '1 cap', 'First dose. Cuts cholesterol supply to virus.'],
]
story.append(make_table(data, [2.0*inch, 1.4*inch, 3.6*inch], meal1_bg))

# MEAL 2
story.append(Paragraph("WITH LAST MEAL (6-7pm)", section_style))
data = [
    ['Supplement', 'Dose', 'Why'],
    ['Berberine (Thorne)', '500mg', 'Second dose. Postprandial glucose + AMPK.'],
    ['GABA (Pharma GABA)', '250mg', 'Second dose. Calming into evening.'],
    ['Red Yeast Rice+CoQ10 (Thorne)', '1 cap', 'Second dose. Cholesterol synth peaks at night.'],
]
story.append(make_table(data, [2.2*inch, 1.2*inch, 3.6*inch], meal2_bg))

# BEFORE BED
story.append(Paragraph("BEFORE BED (9-10pm)", section_style))
data = [
    ['Activity', 'Duration', 'Mechanism'],
    ['WHM Breathing', '3 rounds (~10 min)', 'Epinephrine locks NF-kB via beta-arrestin-2 pathway.'],
    ['Cold Shower (optional)', '30-60 sec cold', 'Norepinephrine mobilizes NK cells.'],
]
story.append(make_table(data, [2.0*inch, 1.4*inch, 3.6*inch], bed_bg))

story.append(Spacer(1, 10))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cccccc')))
story.append(Spacer(1, 6))

# TARGETS TABLE
story.append(Paragraph("WHAT THIS STACK HITS", section_style))
data = [
    ['CVB Target', 'Supplements Attacking It'],
    ['OSBP cholesterol delivery', 'Berberine (indirect), Red Yeast Rice (synth block)'],
    ['NLRP3 inflammasome', 'BHB (direct Signal 2), Omega-3 (Signal 1), NAC (ROS->NF-\u03baB)'],
    ['NF-\u03baB transcription', 'WHM (epinephrine), Omega-3, NAC, Vitamin D'],
    ['Autophagy / TFEB', '18:6 IF (mTOR off), Berberine (AMPK), BHB (HDAC), Vit D'],
    ['Lysosomal function', 'Selenium (GPx), Zinc (fusion), NAC (glutathione)'],
    ['Treg / immune tolerance', 'GABA, LGG, Tributyrin/butyrate (FOXP3), Vitamin D'],
    ['Beta cell protection', 'ALA (insulin sensitivity), all anti-inflammatory above'],
]
story.append(make_table(data, [2.0*inch, 5.0*inch], colors.HexColor('#f5f5f5')))

story.append(Spacer(1, 8))

# RULES
story.append(Paragraph("RULES", section_style))
rules = [
    "1. D3 and Omega-3 WITH fat \u2014 won't absorb without it",
    "2. Zinc WITH food \u2014 causes nausea on empty stomach",
    "3. NAC and ALA AWAY from food \u2014 amino acid competition reduces absorption",
    "4. LGG on empty stomach \u2014 delayed-release capsule helps survive acid",
    "5. BHB during fasting window \u2014 maximizes NLRP3 block when autophagy peaks",
    "6. Red Yeast Rice at DINNER \u2014 cholesterol synthesis peaks at night",
    "7. Berberine WITH meals \u2014 GI upset fasted + blunts glucose spike",
    "8. WHM BEFORE BED \u2014 not after meals (diaphragm needs room)",
    "9. NEVER skip WHM \u2014 only intervention that LOCKS NF-\u03baB completely",
]
for r in rules:
    story.append(Paragraph(r, rule_style))

story.append(Spacer(1, 8))
story.append(Paragraph("One virus. Twelve diseases. One protocol.",
                        ParagraphStyle('Footer', parent=styles['Normal'],
                                       fontSize=9, fontName='Helvetica-BoldOblique',
                                       alignment=TA_CENTER, textColor=colors.HexColor('#1a1a2e'))))

doc.build(story)
print(f"PDF saved to {output_path}")
