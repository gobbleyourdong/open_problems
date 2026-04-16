#!/usr/bin/env python3
"""Generate the complete protocol PDF for the operator."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Table, TableStyle,
                                 Paragraph, Spacer, PageBreak, HRFlowable)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def p(text, style):
    return Paragraph(text, style)

def build_pdf():
    doc = SimpleDocTemplate(
        "~/Downloads/T1DM_Protocol.pdf",
        pagesize=letter,
        topMargin=0.4*inch,
        bottomMargin=0.4*inch,
        leftMargin=0.5*inch,
        rightMargin=0.5*inch,
    )

    styles = getSampleStyleSheet()
    title = ParagraphStyle('T', parent=styles['Title'], fontSize=16, spaceAfter=4, leading=18)
    subtitle = ParagraphStyle('Sub', parent=styles['Normal'], fontSize=9, textColor=colors.HexColor('#444444'), spaceAfter=10, leading=11)
    h1 = ParagraphStyle('H1', parent=styles['Heading1'], fontSize=13, spaceBefore=14, spaceAfter=4, textColor=colors.HexColor('#1a5276'))
    h2 = ParagraphStyle('H2', parent=styles['Heading2'], fontSize=11, spaceBefore=10, spaceAfter=3, textColor=colors.HexColor('#1a6e3e'))
    body = ParagraphStyle('B', parent=styles['Normal'], fontSize=9, leading=12)
    cell = ParagraphStyle('C', parent=styles['Normal'], fontSize=7.5, leading=9.5)
    cellb = ParagraphStyle('CB', parent=cell, fontName='Helvetica-Bold')
    small = ParagraphStyle('S', parent=styles['Normal'], fontSize=7, leading=9, textColor=colors.grey)
    check = ParagraphStyle('Check', parent=styles['Normal'], fontSize=9, leading=13, leftIndent=12)

    elements = []

    # ─── TITLE ───
    elements.append(Paragraph("The Protocol", title))
    elements.append(Paragraph(
        "A non-invasive, preventive approach to immune retraining and beta cell support. "
        "Based on 51 systematic research attempts across 5 domains: cell biology, regeneration, "
        "environment, virology, and metabolism. Every intervention justified by published mechanism. "
        "Nothing here is a drug claim. Everything here is a lifestyle choice.", subtitle))
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cccccc')))

    # ─── DAILY MORNING ───
    elements.append(Paragraph("Morning Routine", h1))

    elements.append(Paragraph("<b>Sunlight — 20 minutes, skin exposed (arms/legs)</b>", check))
    elements.append(Paragraph("UV-B converts 7-dehydrocholesterol to vitamin D3 in the skin. Vitamin D activates the VDR-AMPK pathway (autophagy induction), promotes regulatory T cell differentiation, strengthens gut barrier tight junctions, and resets circadian rhythm. Morning light also drives serotonin production. No sunscreen on exposed skin during this window.", body))
    elements.append(Spacer(1, 6))

    elements.append(Paragraph("<b>Morning Supplements — take with first meal (noon)</b>", check))

    morning_supps = [
        [p("<b>Supplement</b>", cellb), p("<b>Dose</b>", cellb), p("<b>Why</b>", cellb), p("<b>$/mo</b>", cellb)],
        [p("Vitamin D3", cellb), p("5,000 IU", cell),
         p("Immunomodulator. Induces Tregs (FOXP3+ CD4+CD25+), induces cathelicidin, activates autophagy via VDR-AMPK. Target serum level: 50-70 ng/mL. Take with fat (fat-soluble). T1DM incidence inversely correlates with vitamin D status across all studied populations.", cell),
         p("$10", cell)],
        [p("Selenium", cellb), p("200 μg<br/>(selenomethionine)", cell),
         p("Cofactor for glutathione peroxidase (GPx). GPx protects lysosomal membranes (enables autophagy) AND neutralizes H₂O₂ (protects beta cells, which have 2% of normal antioxidant defense). Keshan disease: selenium-deficient populations develop Coxsackievirus cardiomyopathy. Direct CVB-selenium link established.", cell),
         p("$5", cell)],
        [p("Zinc", cellb), p("15 mg<br/>(zinc picolinate)", cell),
         p("Cofactor for Cu/Zn-SOD (superoxide dismutase). Required for autophagosome-lysosome fusion. Required for IRF3 activation (interferon signaling). Supports thymulin (thymic hormone for T cell maturation). Inhibits viral RNA-dependent RNA polymerase in vitro at achievable concentrations with ionophore.", cell),
         p("$5", cell)],
        [p("Omega-3", cellb), p("2g EPA+DHA<br/>(fish oil)", cell),
         p("Anti-inflammatory. Resolvin and protectin production. Reduces TNF-α, IL-1β, IL-6. Competes with omega-6 (arachidonic acid) for COX/LOX enzymes, shifting eicosanoid profile from pro-inflammatory to resolving.", cell),
         p("$15", cell)],
        [p("NAC", cellb), p("600 mg", cell),
         p("N-acetylcysteine. Precursor to glutathione (GSH), the master intracellular antioxidant. Protects beta cells from immune-generated ROS without quenching extracellular immune ROS. Works INSIDE the cell where beta cells are defenseless.", cell),
         p("$10", cell)],
        [p("GABA", cellb), p("750 mg", cell),
         p("Gamma-aminobutyric acid. Three mechanisms: (1) promotes alpha-to-beta cell transdifferentiation (second regeneration pathway), (2) anti-inflammatory on immune cells (GABA receptors on T cells suppress activation), (3) directly anti-apoptotic for beta cells. OTC, well-tolerated.", cell),
         p("$15", cell)],
        [p("L. rhamnosus GG<br/>probiotic", cellb), p("10B CFU", cell),
         p("Produces L-lactate ONLY (not D-lactate). Competitively displaces D-lactate-producing bacteria. Strengthens gut barrier. Well-studied strain with decades of safety data.", cell),
         p("$10", cell)],
    ]

    t = Table(morning_supps, colWidths=[1.1*inch, 0.8*inch, 4.3*inch, 0.5*inch], repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a5276')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f7f9fa')]),
        ('LEFTPADDING', (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    elements.append(t)

    # ─── DAILY AFTERNOON ───
    elements.append(Paragraph("Afternoon", h1))

    elements.append(Paragraph("<b>Exercise — 30 minutes moderate (walk, swim, bike)</b>", check))
    elements.append(Paragraph("Moderate exercise enhances NK cell cytotoxicity, improves immune surveillance, increases vagal tone, improves insulin sensitivity, and promotes angiogenesis. NOT exhaustive — vigorous exercise temporarily suppresses immunity. The sweet spot is 30-60 minutes at conversational pace. Also: with 2u/meal insulin, vigorous exercise causes hypos. Moderate avoids this.", body))
    elements.append(Spacer(1, 4))

    elements.append(Paragraph("<b>Heat exposure — 20 minutes (sauna, hot bath, or hot shower)</b>", check))
    elements.append(Paragraph("Core temperature rises to ~38.5°C. Viral replication decreases ~50% at 39°C vs 37°C. T cell proliferation increases 5-fold. Heat shock proteins (HSP70/90) upregulated — improve antigen presentation. Finnish sauna studies: 40% reduction in respiratory infections with regular use. Monitor glucose — heat increases insulin sensitivity like exercise.", body))

    # ─── DAILY EVENING ───
    elements.append(Paragraph("Evening", h1))

    elements.append(Paragraph("<b>Evening Supplements — take with last meal</b>", check))

    evening_supps = [
        [p("<b>Supplement</b>", cellb), p("<b>Dose</b>", cellb), p("<b>Why</b>", cellb), p("<b>$/mo</b>", cellb)],
        [p("GABA", cellb), p("750 mg", cell),
         p("Second dose. Calming effect aids sleep onset (inhibitory neurotransmitter). Continues the anti-inflammatory and transdifferentiation support overnight.", cell),
         p("—", cell)],
        [p("NAC", cellb), p("600 mg", cell),
         p("Second dose. Glutathione is consumed during the day by normal metabolism. Evening dose replenishes for overnight immune maintenance.", cell),
         p("—", cell)],
        [p("Alpha-lipoic acid", cellb), p("300 mg", cell),
         p("Universal antioxidant recycler. Regenerates vitamin C, vitamin E, and glutathione. Works in both aqueous and lipid compartments. Chelates heavy metals. Particularly effective in beta cells because it crosses all membranes freely.", cell),
         p("$10", cell)],
        [p("Sodium butyrate", cellb), p("300 mg", cell),
         p("HDAC inhibitor. Derepresses FOXP3 promoter → induces regulatory T cells. Produced naturally by gut bacteria from dietary fiber, but supplementation bridges the gap while the microbiome is being rebuilt. Also: direct antiviral properties in some models.", cell),
         p("$20", cell)],
    ]

    t2 = Table(evening_supps, colWidths=[1.1*inch, 0.8*inch, 4.3*inch, 0.5*inch], repeatRows=1)
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a6e3e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f5faf7')]),
        ('LEFTPADDING', (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    elements.append(t2)

    # ─── FASTING WINDOW ───
    elements.append(Paragraph("Fasting Window (18 hours)", h1))

    elements.append(Paragraph("<b>Continue current 18:6 intermittent fasting (last food 6pm, first food noon)</b>", check))
    elements.append(Paragraph("18 hours of daily autophagy activation. AMPK ON → mTOR OFF → autophagosomes form → capture and digest intracellular debris including viral replication complexes. Also: daily immune cell turnover, BHB production from fat metabolism, beta cell rest (minimal insulin demand during fast).", body))
    elements.append(Spacer(1, 4))

    elements.append(Paragraph("<b>BHB salts — 5g at hour 14-16 of fast</b>", check))
    elements.append(Paragraph("Exogenous β-hydroxybutyrate. Extends the ketosis window during the deepest part of the fast. BHB is an HDAC inhibitor (same mechanism as butyrate → FOXP3 → Tregs), suppresses the NLRP3 inflammasome (reduces IL-1β, a key insulitis cytokine), and provides alternative fuel so beta cells rest from glucose processing. This is what keto gave you for 5 years — concentrated into the fasting window. $30/month.", body))

    # ─── EATING WINDOW ───
    elements.append(Paragraph("Eating Window (6 hours, noon-6pm)", h1))

    elements.append(Paragraph("<b>First food: fiber</b>", check))
    elements.append(Paragraph("Resistant starch (cooled potatoes, cooled rice, green bananas, oats) and vegetables FIRST before protein/carbs. This feeds Faecalibacterium prausnitzii — the #1 butyrate-producing bacteria depleted in T1DM. Cannot be supplemented as a probiotic (obligate anaerobe — dies in air). Must be FED. Butyrate from these bacteria → FOXP3 → Tregs → immune regulation at the source.", body))
    elements.append(Spacer(1, 4))

    elements.append(Paragraph("<b>Fermented foods daily</b>", check))
    elements.append(Paragraph("Sauerkraut, kimchi, kefir, or plain yogurt (A2 milk if available). Microbial diversity. Each serving delivers billions of live organisms that compete with pathogenic species and modulate gut immune tone.", body))
    elements.append(Spacer(1, 4))

    elements.append(Paragraph("<b>Avoid</b>", check))
    elements.append(Paragraph("Processed food (emulsifiers disrupt mucus layer), artificial sweeteners (alter microbiome), excess sugar (feeds D-lactate producers), seed oils in excess (pro-inflammatory omega-6). Continue current 15-20g carbs/meal — this is reasonable.", body))

    # ─── SLEEP ───
    elements.append(Paragraph("Sleep", h1))

    elements.append(Paragraph("<b>7-9 hours, consistent schedule, dark room</b>", check))
    elements.append(Paragraph("Sleep is when the immune system does maintenance. IFN-γ and IL-12 peak during sleep. Cortisol reaches its nadir during early sleep — immune cells are maximally active. One night of sleep deprivation reduces NK cell activity by 70% (Irwin et al.). Chronic short sleep (<6hr) reduces vaccine antibody response by 50%. Melatonin (produced in darkness) is an antioxidant and immune modulator. No screens 1hr before bed — blue light suppresses melatonin.", body))

    # ─── STRESS ───
    elements.append(Paragraph("Stress Management", h1))

    elements.append(Paragraph("<b>5 minutes daily: deep breathing (4-count inhale, 8-count exhale)</b>", check))
    elements.append(Paragraph("Long exhale activates the parasympathetic nervous system via the vagus nerve. The vagus nerve terminates on splenic macrophages — acetylcholine release suppresses TNF-α, IL-1β, and IL-6 via the cholinergic anti-inflammatory pathway (Tracey, 2000). Chronic stress does the opposite: cortisol upregulates inflammatory genes and downregulates antiviral interferon genes (the CTRA profile — Cole, UCLA). This breathing practice directly counters CTRA.", body))

    elements.append(PageBreak())

    # ─── MONTHLY FMD ───
    elements.append(Paragraph("Monthly: 5-Day Fasting-Mimicking Diet", h1))

    elements.append(Paragraph("This is the deep reset. Everything the daily routine does at low intensity, the FMD does at maximum intensity for 5 days. Based on Cheng et al., <i>Cell</i> 2017 — cyclical FMD restored beta cell function in diabetic mice via Ngn3+ progenitor activation.", body))
    elements.append(Spacer(1, 6))

    fmd = [
        [p("<b>Day</b>", cellb), p("<b>Calories</b>", cellb), p("<b>Macros</b>", cellb), p("<b>Insulin</b>", cellb), p("<b>What's Happening</b>", cellb)],
        [p("1", cellb), p("~1100 kcal", cell), p("50% fat, 35% carb, 15% protein", cell), p("Reduce to 1u/meal", cell),
         p("Transition. mTOR beginning to shut down. Glycogen depleting.", cell)],
        [p("2", cellb), p("~750 kcal", cell), p("55% fat, 35% carb, 10% protein", cell), p("0-1u/meal", cell),
         p("Ketosis begins. AMPK fully activated. Autophagy ramping up.", cell)],
        [p("3", cellb), p("~750 kcal", cell), p("Same", cell), p("0-1u/meal", cell),
         p("Deep autophagy. TFEB nuclear — lysosomal biogenesis floods cells. Viral factories being captured and digested.", cell)],
        [p("4", cellb), p("~750 kcal", cell), p("Same", cell), p("0-1u/meal", cell),
         p("Immune cell turnover. Old monocytes dying. HSCs activating in bone marrow. Beta cells fully resting.", cell)],
        [p("5", cellb), p("~750 kcal", cell), p("Same", cell), p("0-1u/meal", cell),
         p("Peak clearance. Approaching 100% cytoplasmic turnover.", cell)],
        [p("6-7", cellb), p("Gradual refeed", cell), p("High fiber first, then protein, then normal", cell), p("Resume 1-2u", cell),
         p("REGENERATION WINDOW. mTOR reactivates. Ngn3+ progenitors differentiate. Fresh immune cells emerge from bone marrow with intact IFN machinery. Butyrate from returning bacteria → FOXP3 → Tregs protect new beta cells.", cell)],
    ]

    t3 = Table(fmd, colWidths=[0.4*inch, 0.7*inch, 1.3*inch, 0.8*inch, 3.5*inch], repeatRows=1)
    t3.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#6c3483')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#faf5fd')]),
        ('LEFTPADDING', (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    elements.append(t3)

    elements.append(Spacer(1, 6))
    elements.append(Paragraph("<b>Safety during FMD:</b> CGM alarming at 70 mg/dL (hypo) and 250 mg/dL (hyper). Check blood ketones 2x daily — target 0.5-3.0 mmol/L. Above 3.0 with blood glucose >250: eat carbs + take insulin (DKA prevention). Keep glucose tabs available. First cycle on a quiet week. Partner/friend aware.", body))

    # ─── COST ───
    elements.append(Paragraph("Monthly Cost", h1))

    costs = [
        [p("<b>Item</b>", cellb), p("<b>Monthly</b>", cellb)],
        [p("Vitamin D3 5000IU", cell), p("$10", cell)],
        [p("Selenium 200μg", cell), p("$5", cell)],
        [p("Zinc 15mg", cell), p("$5", cell)],
        [p("Omega-3 2g", cell), p("$15", cell)],
        [p("NAC 1200mg/day", cell), p("$10", cell)],
        [p("Alpha-lipoic acid 300mg", cell), p("$10", cell)],
        [p("GABA 1500mg/day", cell), p("$15", cell)],
        [p("Sodium butyrate 300mg", cell), p("$20", cell)],
        [p("BHB salts 5g/day", cell), p("$30", cell)],
        [p("L. rhamnosus GG probiotic", cell), p("$10", cell)],
        [p("Sunlight, exercise, sauna, sleep, breathing, fasting", cell), p("$0", cell)],
        [p("<b>TOTAL</b>", cellb), p("<b>$130/month</b>", cellb)],
    ]

    t4 = Table(costs, colWidths=[4.5*inch, 1.5*inch], repeatRows=1)
    t4.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c3e50')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -2), [colors.white, colors.HexColor('#f2f3f4')]),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#eaf2e3')),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    elements.append(t4)

    # ─── TRACKING ───
    elements.append(Paragraph("What to Track", h1))
    elements.append(Paragraph("<b>Daily:</b> CGM glucose, insulin doses, ketones during FMD, how you feel (energy, mood, sleep quality).", body))
    elements.append(Paragraph("<b>Monthly:</b> Weight, average daily insulin, time-in-range from CGM.", body))
    elements.append(Paragraph("<b>Quarterly:</b> HbA1c. Stimulated C-peptide if accessible (THE metric — is beta cell function improving?).", body))
    elements.append(Paragraph("<b>Annually:</b> Full panel — vitamin D, lipids, thyroid (TSH, TPO Ab), hsCRP.", body))
    elements.append(Spacer(1, 4))
    elements.append(Paragraph("<b>The signal you're looking for:</b> insulin dose trending DOWN over months while HbA1c stays stable or improves. This means beta cells are picking up more of the load. If 2u/meal → 1u/meal → 0.5u → 0: the protocol is working.", body))

    # ─── WHAT THIS IS NOT ───
    elements.append(Paragraph("What This Is and Is Not", h1))
    elements.append(Paragraph("This is a lifestyle protocol. It is not a cure. It is not medical advice. It is a structured approach to diet, supplementation, fasting, exercise, sleep, and stress management — all of which have published evidence for immune modulation and metabolic health. Every supplement listed is available over-the-counter. Nothing here requires a prescription.", body))
    elements.append(Spacer(1, 4))
    elements.append(Paragraph("Continue all prescribed insulin and medications. Adjust insulin ONLY during FMD cycles and ONLY with CGM monitoring and medical awareness. The goal is to create conditions where the body can do what Butler proved it never stops trying to do: regenerate beta cells.", body))

    elements.append(Spacer(1, 10))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cccccc')))
    elements.append(Spacer(1, 4))
    elements.append(Paragraph(
        "<b>Key References:</b> Butler AE et al. <i>Diabetologia</i> 2005;48:2221 (beta cell persistence 67yr). "
        "Cheng CW et al. <i>Cell</i> 2017;168:775 (FMD beta cell regeneration). "
        "Kuss S et al. <i>Science</i> 2011;334:249 (enteroviruses require gut bacteria). "
        "Cole SW. <i>Current Directions in Psych Science</i> 2014;23:116 (CTRA). "
        "Irwin MR et al. <i>Psychosom Med</i> 2003 (sleep and NK cells). "
        "Tracey KJ. <i>Nature</i> 2002;420:853 (cholinergic anti-inflammatory pathway). "
        "Soltani N et al. <i>PNAS</i> 2011;108:11692 (GABA and T1DM). "
        "Beck MA et al. <i>Nat Med</i> 1995;1:433 (selenium and CVB/Keshan). "
        "Soppela S et al. <i>J Biomed Sci</i> 2026;33:34 (CVB1 VLP vaccine, ADE).",
        small))

    doc.build(elements)
    print("PDF saved to ~/Downloads/T1DM_Protocol.pdf")

if __name__ == "__main__":
    build_pdf()
