#!/usr/bin/env python3
"""Generate PDF lab order for the patient — clean, professional, no overflow."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Table, TableStyle,
                                 Paragraph, Spacer, PageBreak)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def p(text, style):
    """Wrap text in Paragraph for table cells to handle word wrap."""
    return Paragraph(text, style)

def build_pdf():
    doc = SimpleDocTemplate(
        "~/Downloads/T1DM_Lab_Panel.pdf",
        pagesize=letter,
        topMargin=0.4*inch,
        bottomMargin=0.4*inch,
        leftMargin=0.5*inch,
        rightMargin=0.5*inch,
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle('T', parent=styles['Title'], fontSize=14, spaceAfter=2, leading=16)
    subtitle_style = ParagraphStyle('Sub', parent=styles['Normal'], fontSize=9, textColor=colors.HexColor('#333333'), spaceAfter=8, leading=11)
    heading_style = ParagraphStyle('H2', parent=styles['Heading2'], fontSize=11, spaceBefore=12, spaceAfter=4, textColor=colors.HexColor('#1a5276'))
    body_style = ParagraphStyle('Body', parent=styles['Normal'], fontSize=8.5, leading=11)
    cell_style = ParagraphStyle('Cell', parent=styles['Normal'], fontSize=7.5, leading=9.5)
    cell_bold = ParagraphStyle('CellB', parent=cell_style, fontName='Helvetica-Bold')
    small_style = ParagraphStyle('Small', parent=styles['Normal'], fontSize=7, leading=9, textColor=colors.grey)
    inst_style = ParagraphStyle('Inst', parent=styles['Normal'], fontSize=8.5, leading=11, spaceBefore=2)

    elements = []

    # Title
    elements.append(Paragraph("Comprehensive Assessment Panel — Type 1 Diabetes", title_style))
    elements.append(Paragraph(
        "<b>Patient:</b> Adult male, Dx 12/2019. C-peptide 0.9 ng/mL at diagnosis. "
        "5-year insulin-free remission on ketogenic diet (2020-2024). "
        "Currently 2u Humalog/meal, 18:6 intermittent fasting, 15-20g carbs/meal. "
        "Evaluating residual beta cell function and autoimmune status for potential "
        "disease-modifying intervention.", subtitle_style))

    # ─── TIER 1 ───
    elements.append(Paragraph("Tier 1 — Standard Endocrine / Metabolic Panel", heading_style))
    elements.append(Paragraph("Standard-of-care labs for T1DM assessment. Fasting 12hr required for C-peptide, insulin, lipids.", body_style))
    elements.append(Spacer(1, 4))

    header = [p("<b>Test</b>", cell_bold), p("<b>Code</b>", cell_bold), p("<b>Rationale</b>", cell_bold)]

    tier1_data = [
        header,
        [p("Fasting C-Peptide", cell_bold), p("004051", cell_style),
         p("Quantify residual beta cell function. Prior level 0.9 ng/mL at Dx (Dec 2019). Patient sustained insulin independence for 5 years, suggesting significant residual mass. Current level determines intervention path.", cell_style)],
        [p("GAD65 Antibodies", cell_bold), p("164350", cell_style),
         p("Confirm autoimmune etiology. Most common autoantibody in adult-onset T1DM. Elevated GADA correlates with slower functional decline in some populations.", cell_style)],
        [p("IA-2 Antibodies", cell_bold), p("164355", cell_style),
         p("Progression marker. Combined with ZnT8, identifies rapid progressors. Important for disease staging.", cell_style)],
        [p("ZnT8 Antibodies", cell_bold), p("164382", cell_style),
         p("Present in 60-80% at onset. Completes the autoantibody panel for full staging.", cell_style)],
        [p("Insulin Autoantibodies", cell_bold), p("086215", cell_style),
         p("Completes the standard 4-antibody T1DM panel. Earliest marker in childhood onset.", cell_style)],
        [p("TSH", cell_bold), p("004259", cell_style),
         p("ADA-recommended annual screening. Autoimmune thyroid disease co-occurs in 17-30% of T1DM patients.", cell_style)],
        [p("Free T4", cell_bold), p("001974", cell_style),
         p("Quantifies thyroid function if TSH abnormal. Subclinical hypothyroidism affects lipid metabolism.", cell_style)],
        [p("TPO Antibodies", cell_bold), p("006676", cell_style),
         p("Confirms Hashimoto's thyroiditis. Shared HLA susceptibility with T1DM. Relevant to lipid panel interpretation.", cell_style)],
        [p("25-OH Vitamin D", cell_bold), p("081950", cell_style),
         p("Immunomodulatory assessment. Promotes Treg differentiation, suppresses Th1/Th17. Inverse correlation with T1DM incidence well-established. Target 50-70 ng/mL.", cell_style)],
        [p("hsCRP", cell_bold), p("120766", cell_style),
         p("Baseline systemic inflammation marker. Elevated levels may indicate ongoing immune activation.", cell_style)],
        [p("Lipid Panel (full)", cell_bold), p("303756", cell_style),
         p("Known elevated cholesterol. Full fractionation (total, LDL, HDL, VLDL, TG) to characterize profile. Patient reports high total with low LDL/VLDL.", cell_style)],
        [p("HbA1c", cell_bold), p("001453", cell_style),
         p("Glycemic control baseline for tracking improvement over time.", cell_style)],
        [p("Fasting Insulin", cell_bold), p("004333", cell_style),
         p("Enables HOMA-B and HOMA-IR calculation. Distinguishes residual beta cell function from insulin resistance.", cell_style)],
    ]

    t1 = Table(tier1_data, colWidths=[1.2*inch, 0.7*inch, 5.1*inch], repeatRows=1)
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a5276')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f7f9fa')]),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    elements.append(t1)

    # ─── TIER 2 ───
    elements.append(Paragraph("Tier 2 — Gut-Immune-Metabolic Assessment", heading_style))
    elements.append(Paragraph("Functional medicine labs assessing gut permeability, microbiome composition, and metabolic markers relevant to autoimmune modulation.", body_style))
    elements.append(Spacer(1, 4))

    tier2_data = [
        [p("<b>Test</b>", cell_bold), p("<b>Source</b>", cell_bold), p("<b>Rationale</b>", cell_bold)],
        [p("Serum D-Lactate", cell_bold), p("Genova /<br/>Doctor's Data", cell_style),
         p("D-lactate produced by gut bacteria (Lactobacillus, Streptococcus, Klebsiella) is poorly metabolized by human L-LDH. Elevated D-lactate may drive inappropriate hepatic gluconeogenesis, increasing glucose beyond dietary intake — an occult source of beta cell stress. May partly explain the patient's keto remission (D-lactate producers starved of substrate).", cell_style)],
        [p("Microbiome 16S<br/>Sequencing", cell_bold), p("Viome /<br/>Ombre /<br/>GI-MAP", cell_style),
         p("Profiles bacterial composition. Key targets: (1) D-lactate-producing species abundance, (2) butyrate-producing species (Faecalibacterium, Roseburia) — butyrate is an HDAC inhibitor that promotes FOXP3 expression and Treg differentiation, (3) overall diversity as a marker of gut immune health.", cell_style)],
        [p("Proinsulin:C-peptide<br/>Ratio", cell_bold), p("Specialty<br/>endocrine lab", cell_style),
         p("Elevated ratio indicates beta cell endoplasmic reticulum stress. Stressed beta cells produce neoantigens that amplify autoimmune targeting (Butler, Nat Rev Endocrinol 2021). If elevated, beta cell rest strategies are prioritized.", cell_style)],
        [p("Zonulin", cell_bold), p("Genova /<br/>Vibrant Wellness", cell_style),
         p("Marker of intestinal permeability. Elevated in T1DM and pre-T1DM. Guides decision on gut barrier repair interventions (L-glutamine, zinc carnosine, butyrate) prior to immune modulation.", cell_style)],
    ]

    t2 = Table(tier2_data, colWidths=[1.2*inch, 0.9*inch, 4.9*inch], repeatRows=1)
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a6e3e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f5faf7')]),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    elements.append(t2)

    # ─── TIER 3 ───
    elements.append(Paragraph("Tier 3 — Virology / Research (if accessible)", heading_style))
    elements.append(Paragraph("Investigational markers for persistent enteroviral infection as a driver of ongoing autoimmunity. Academic or research lab access may be required.", body_style))
    elements.append(Spacer(1, 4))

    tier3_data = [
        [p("<b>Test</b>", cell_bold), p("<b>Source</b>", cell_bold), p("<b>Rationale</b>", cell_bold)],
        [p("Enteroviral VP1<br/>(stool RT-PCR)", cell_bold), p("Research<br/>virology lab", cell_style),
         p("Detects active Coxsackievirus B shedding. The DiViD study detected enteroviral protein in pancreatic tissue of 6/6 T1DM patients. Stool PCR is a non-invasive proxy for persistent infection.", cell_style)],
        [p("Serum IFN-alpha", cell_bold), p("Quest 36718 /<br/>research lab", cell_style),
         p("Chronic elevation indicates persistent viral stimulation of innate immune pathways (TLR3/RIG-I/MDA5). Marker of ongoing viral-immune interaction in the pancreas.", cell_style)],
        [p("Anti-CVB<br/>Neutralizing Ab", cell_bold), p("Research<br/>virology lab", cell_style),
         p("Neutralizing antibodies (against VP1 surface epitopes) are protective. Low neutralizing titers relative to total anti-CVB antibodies may indicate a non-protective, potentially enhancement-prone immune response (Soppela et al., J Biomed Sci 2026).", cell_style)],
    ]

    t3 = Table(tier3_data, colWidths=[1.2*inch, 0.9*inch, 4.9*inch], repeatRows=1)
    t3.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#6c3483')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#faf5fd')]),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    elements.append(t3)

    # ─── DECISION MATRIX ───
    elements.append(Paragraph("C-Peptide Decision Matrix", heading_style))

    dec_data = [
        [p("<b>Fasting C-Peptide</b>", cell_bold), p("<b>Interpretation</b>", cell_bold), p("<b>Suggested Path</b>", cell_bold)],
        [p("> 0.5 ng/mL", cell_bold), p("Significant residual beta cell function", cell_style),
         p("Nutritional + supplemental approach with monitoring. Fasting-mimicking diet cycles, gut optimization, vitamin D repletion. Quarterly C-peptide tracking.", cell_style)],
        [p("0.2 - 0.5 ng/mL", cell_bold), p("Moderate residual function", cell_style),
         p("More aggressive protocol: above plus GLP-1 agonist (semaglutide), consider teplizumab referral. 9-18 month timeline.", cell_style)],
        [p("< 0.2 ng/mL", cell_bold), p("Minimal residual function", cell_style),
         p("Full protocol including immune modulation referral. Cell therapy (stem cell / islet) remains an option if regenerative approaches insufficient.", cell_style)],
    ]

    td = Table(dec_data, colWidths=[1.2*inch, 2.2*inch, 3.6*inch], repeatRows=1)
    td.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c3e50')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f2f3f4')]),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    elements.append(td)

    # ─── INSTRUCTIONS ───
    elements.append(Paragraph("Instructions", heading_style))
    elements.append(Paragraph("1. Fast 12 hours overnight before blood draw (water permitted).", inst_style))
    elements.append(Paragraph("2. Tier 1 tests can be performed at any LabCorp or Quest location with physician requisition.", inst_style))
    elements.append(Paragraph("3. Tier 2 tests require specialty lab kits ordered through the supervising physician.", inst_style))
    elements.append(Paragraph("4. A stimulated C-peptide (mixed meal tolerance test) is more informative than fasting C-peptide but requires a clinic setting with timed blood draws. If feasible, this is preferred.", inst_style))
    elements.append(Paragraph("5. Microbiome sequencing is a separate stool sample kit (Viome or Ombre, ~$150, ordered online). Results take 2-3 weeks.", inst_style))

    elements.append(Spacer(1, 10))
    elements.append(Paragraph(
        "<b>References:</b> Butler AE et al. <i>Diabetologia</i> 2005;48:2221 (beta cell persistence in long-standing T1DM). "
        "Cheng CW et al. <i>Cell</i> 2017;168:775 (fasting-mimicking diet and beta cell regeneration). "
        "Soppela S et al. <i>J Biomed Sci</i> 2026;33:34 (CVB1 VLP vaccine, antibody-dependent enhancement). "
        "DiViD Intervention Study, <i>Nature Medicine</i> 2023 (antiviral C-peptide preservation). "
        "Butler PC, <i>Nat Rev Endocrinol</i> 2021 (beta cell stress as autoimmune amplifier).",
        small_style))

    doc.build(elements)
    print("PDF saved to ~/Downloads/T1DM_Lab_Panel.pdf")

if __name__ == "__main__":
    build_pdf()
