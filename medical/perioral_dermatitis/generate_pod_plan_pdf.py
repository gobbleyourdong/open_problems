#!/usr/bin/env python3
"""Generate the POD_Plan.pdf for caregiver reference.

Mirrors the style of ~/Downloads/Eczema_Plan.pdf — centered title,
bold section headers, horizontal rules between sections, a simple
cost table. Plain-English summary of the 4-mountain integrated POD
treatment protocol in a form a caregiver can actually use.

Usage: python generate_pod_plan_pdf.py
Output: ~/Downloads/POD_Plan.pdf
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle,
    KeepTogether,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

OUTPUT_PDF = os.path.expanduser("~/Downloads/POD_Plan.pdf")


def build_styles():
    base = getSampleStyleSheet()
    styles = {}
    styles["title"] = ParagraphStyle(
        "Title", parent=base["Title"], fontSize=22, spaceAfter=16,
        alignment=TA_CENTER, textColor=colors.black,
        fontName="Helvetica-Bold",
    )
    styles["h2"] = ParagraphStyle(
        "H2", parent=base["Heading2"], fontSize=14, spaceBefore=14,
        spaceAfter=6, textColor=colors.HexColor("#333333"),
        fontName="Helvetica-Bold",
    )
    styles["h3"] = ParagraphStyle(
        "H3", parent=base["Heading3"], fontSize=12, spaceBefore=10,
        spaceAfter=4, textColor=colors.HexColor("#222222"),
        fontName="Helvetica-Bold",
    )
    styles["body"] = ParagraphStyle(
        "Body", parent=base["Normal"], fontSize=10.5, leading=14,
        spaceAfter=6, textColor=colors.HexColor("#1a1a1a"),
        fontName="Helvetica",
    )
    styles["bullet"] = ParagraphStyle(
        "Bullet", parent=base["Normal"], fontSize=10, leading=13,
        leftIndent=18, bulletIndent=6, spaceAfter=3,
        textColor=colors.HexColor("#1a1a1a"), fontName="Helvetica",
    )
    styles["ref"] = ParagraphStyle(
        "Ref", parent=base["Normal"], fontSize=9, leading=12,
        textColor=colors.HexColor("#444444"), fontName="Helvetica",
    )
    return styles


def hr():
    return HRFlowable(
        width="100%", thickness=0.6, color=colors.HexColor("#cccccc"),
        spaceBefore=4, spaceAfter=8,
    )


def build_story(s):
    story = []

    # Title
    story.append(Paragraph("Perioral Dermatitis Plan", s["title"]))

    # What's going on
    story.append(Paragraph("What's going on", s["h2"]))
    story.append(Paragraph(
        "Perioral dermatitis is a rash around the mouth — small red bumps, "
        "sometimes pustules, sometimes a mild burning sensation. It is NOT "
        "eczema (usually not itchy) and NOT acne (no comedones). The classic "
        "diagnostic sign is a narrow clear zone of unaffected skin directly "
        "next to the lip border. Pediatric cases have been rising since the "
        "1990s.",
        s["body"]))
    story.append(Paragraph(
        "POD has several overlapping contributors: toothpaste ingredients "
        "(fluoride, the SLS foaming agent, mint and cinnamon flavorings), "
        "lip balms, cosmetics, sunscreens, and Demodex mites (which live "
        "on everyone's face and multiply when the local immune system is "
        "off balance). The protocol below addresses multiple contributors "
        "at once. It is stricter than what most dermatologists prescribe, "
        "but it works when followed.",
        s["body"]))
    story.append(Paragraph(
        "<b>Important note about topical steroids:</b> if a topical steroid "
        "(hydrocortisone, fluticasone, desonide, mometasone, triamcinolone, "
        "clobetasol, anything ending in -one or -olone) has been applied to "
        "the rash — even OTC hydrocortisone — it should come off the face "
        "completely. Steroids on the face cause a rebound cycle in POD. "
        "If no topical steroid has been in the rotation for this rash, "
        "skip the rebound-flare section later in this document; the "
        "protocol will be simpler.",
        s["body"]))
    story.append(hr())

    # 1. Metronidazole
    story.append(Paragraph(
        "1. Metronidazole 0.75% — the current treatment", s["h3"]))
    story.append(Paragraph(
        "<b>What:</b> Metronidazole 0.75% (brand names MetroGel, MetroCream, "
        "MetroLotion). Prescription. Not a steroid. First-line topical "
        "treatment for perioral dermatitis in children.",
        s["body"]))
    story.append(Paragraph(
        "<b>Why:</b> Metronidazole reduces the local inflammatory response "
        "and has mild anti-Demodex activity (Demodex is a mite that can "
        "contribute to POD). It is safe for children and does NOT cause "
        "the rebound cycle that steroids cause.",
        s["body"]))
    story.append(Paragraph(
        "<b>How:</b> Thin layer twice daily on the affected area after "
        "gently washing the face with plain water or CeraVe Hydrating "
        "Cleanser. Expect to use for 4–6 weeks before full effect. Apply "
        "to the surrounding skin, not the lips themselves.",
        s["body"]))
    story.append(Paragraph(
        "<b>Important — gel vs cream vs lotion:</b> if the prescription "
        "is for the <b>gel</b> and it stings when applied, call the "
        "pediatrician and ask for the <b>cream</b> or <b>lotion</b> "
        "formulation instead. Same drug, gentler vehicle. The gel uses "
        "an alcohol base that stings on inflamed skin. The cream and "
        "lotion do not. Kids' faces tolerate the cream/lotion much better.",
        s["body"]))
    story.append(Paragraph(
        "<b>Cost:</b> ~$15–30 with insurance, up to $60 without. Generic "
        "metronidazole is widely available.",
        s["body"]))
    story.append(hr())

    # 2. Non-fluoride toothpaste
    story.append(Paragraph(
        "2. Switch to non-fluoride, SLS-free, unflavored toothpaste",
        s["h3"]))
    story.append(Paragraph(
        "<b>What:</b> Look for these labels on the tube: &quot;SLS-free,&quot; "
        "&quot;fluoride-free,&quot; and unflavored or very mild flavor. "
        "Examples that work: Tom's of Maine toddler training toothpaste, "
        "Hello fluoride-free kids toothpaste, or plain baking-soda toothpaste. "
        "Read the ingredient list; if you see &quot;sodium lauryl sulfate&quot; "
        "or cinnamon/mint flavorings, pick a different one.",
        s["body"]))
    story.append(Paragraph(
        "<b>Why:</b> Fluoride, SLS (the foaming agent), cinnamaldehyde, and "
        "mint oils are documented triggers for perioral dermatitis. During "
        "brushing, tiny amounts of toothpaste migrate from the lips onto the "
        "surrounding skin, where they dry and deposit — exactly where POD "
        "appears. Twice-daily exposure is the suspected driver of much "
        "pediatric POD.",
        s["body"]))
    story.append(Paragraph(
        "<b>How:</b> Do a strict 4-week trial with no fluoride/SLS. Rinse "
        "the face with plain water after brushing to wash off any residual "
        "paste. If the rash improves, keep the swap; if not, you can add "
        "fluoride back later.",
        s["body"]))
    story.append(Paragraph("<b>Cost:</b> ~$5–8 per tube", s["body"]))
    story.append(hr())

    # 3. CeraVe (was 4)
    story.append(Paragraph(
        "3. CeraVe Moisturizing Cream — barrier repair", s["h3"]))
    story.append(Paragraph(
        "<b>What:</b> CeraVe Moisturizing Cream (the tub) or Daily "
        "Moisturizing Lotion. <b>AVOID:</b> CeraVe SA Cream or SA Lotion "
        "(contain salicylic acid, will sting). <b>AVOID:</b> CeraVe Healing "
        "Ointment around the mouth (too occlusive for POD — fine on the lips "
        "themselves, not on the surrounding skin).",
        s["body"]))
    story.append(Paragraph(
        "<b>Why:</b> Ceramides repair the skin barrier without trapping "
        "follicular contents. Unlike heavy petroleum-based ointments "
        "(Aquaphor, Vaseline), ceramide creams do not worsen POD by "
        "occluding the pilosebaceous units.",
        s["body"]))
    story.append(Paragraph(
        "<b>How:</b> Thin layer once or twice a day on the face. Do not "
        "overapply — POD often responds better to less product, not more. "
        "The goal is barrier support, not coverage.",
        s["body"]))
    story.append(Paragraph("<b>Cost:</b> ~$15/month", s["body"]))
    story.append(hr())

    # 4. Vitamin D (was 5)
    story.append(Paragraph(
        "4. Vitamin D — keep the current dose, do not megadose", s["h3"]))
    story.append(Paragraph(
        "<b>What:</b> Standard pediatric vitamin D supplementation "
        "(400–1000 IU/day depending on age). <b>Do not switch to &quot;high "
        "dose&quot; (2000+ IU/day) during an active POD flare.</b>",
        s["body"]))
    story.append(Paragraph(
        "<b>Why:</b> Vitamin D is broadly beneficial for immune function and "
        "bone health and can stay in the protocol. There is a specific "
        "theoretical concern at HIGH doses: vitamin D upregulates a skin "
        "antimicrobial peptide called cathelicidin, which can worsen "
        "perioral dermatitis and rosacea when dysregulated. At standard "
        "pediatric doses, this effect is small enough to ignore. At high "
        "doses during an active flare, it can matter.",
        s["body"]))
    story.append(Paragraph(
        "<b>How:</b> Continue whatever dose you were already using from the "
        "eczema protocol. Do not add a high-dose supplement during the POD "
        "treatment phase.",
        s["body"]))
    story.append(Paragraph(
        "<b>Cost:</b> ~$10/month (continue existing)", s["body"]))
    story.append(hr())

    # 5. Sulfur soap
    story.append(Paragraph(
        "5. Sulfur soap — natural anti-Demodex, safe for kids", s["h3"]))
    story.append(Paragraph(
        "<b>What:</b> A mild sulfur soap bar (De La Cruz sulfur ointment, "
        "Grandpa's Pine Tar &amp; Sulfur soap, or any 6–10% precipitated "
        "sulfur soap). Available at most drugstores and Amazon. OTC, no "
        "prescription needed.",
        s["body"]))
    story.append(Paragraph(
        "<b>Why:</b> Sulfur kills Demodex mites (tiny face mites that can "
        "contribute to POD). It has been used safely on children for over "
        "a century for scabies and other skin conditions. Unlike tea tree "
        "oil, sulfur is <b>non-toxic if accidentally ingested</b> in tiny "
        "amounts — important for a child who puts hands and toys in his "
        "mouth.",
        s["body"]))
    story.append(Paragraph(
        "<b>How:</b> Lather gently on the affected area once a day (morning "
        "or evening). Leave for 30 seconds. Rinse thoroughly. Follow with "
        "metronidazole, then CeraVe. Continue for 2–4 weeks.",
        s["body"]))
    story.append(Paragraph(
        "<b>The drawback:</b> it smells like rotten eggs. The smell "
        "dissipates after rinsing. Some kids don't mind; others protest. "
        "Worth trying.",
        s["body"]))
    story.append(Paragraph("<b>Cost:</b> ~$5–10", s["body"]))
    story.append(hr())

    # 6. Probiotic
    story.append(Paragraph("6. Probiotic — keep the current one", s["h3"]))
    story.append(Paragraph(
        "<b>What:</b> Whatever probiotic is already in use from the eczema "
        "protocol (Culturelle Kids or equivalent).",
        s["body"]))
    story.append(Paragraph(
        "<b>Why:</b> Probiotics do not directly treat POD, but they do not "
        "harm it either. The gut-skin axis is stronger in eczema than in "
        "POD, but if there is any atopic tendency (allergies, eczema, "
        "asthma), probiotics help the underlying propensity.",
        s["body"]))
    story.append(Paragraph(
        "<b>Cost:</b> ~$20/month (continue existing)", s["body"]))
    story.append(hr())

    # 7. Mid-day face wash
    story.append(Paragraph(
        "7. Mid-day face wash — clear daytime buildup", s["h3"]))
    story.append(Paragraph(
        "<b>What:</b> A gentle face wash around lunchtime or right after "
        "school — just plain water on a soft cloth, or a CeraVe Hydrating "
        "Cleanser wipe.",
        s["body"]))
    story.append(Paragraph(
        "<b>Why:</b> The rash is best in the morning and worst in the "
        "evening. That pattern means daytime contactants (toothpaste "
        "residue, food residue, paint, dirt, hand-transferred contaminants) "
        "accumulate on the skin through the day. A mid-day wash resets the "
        "accumulation clock. This is especially important on school days.",
        s["body"]))
    story.append(Paragraph(
        "<b>How:</b> Gently wipe the perioral area with a damp soft cloth. "
        "No scrubbing. Pat dry. Apply a thin layer of CeraVe. Takes "
        "30 seconds. Can be done by a teacher's aide or school nurse if "
        "arranged.",
        s["body"]))
    story.append(Paragraph("<b>Cost:</b> Free", s["body"]))
    story.append(hr())

    # Investigate the school trigger
    story.append(Paragraph(
        "Investigate the School Trigger", s["h2"]))
    story.append(Paragraph(
        "The rash going away during a week at home and returning at school "
        "is a near-diagnostic signal that something in the school "
        "environment is a trigger. Ask the teacher specifically about:",
        s["body"]))
    story.append(Paragraph(
        "<b>Classroom soap</b> — what brand is at the sink? Many school "
        "soaps contain fragrance, SLS, or antibacterial agents that can "
        "trigger POD. Send him with his own fragrance-free soap if possible.",
        s["bullet"]))
    story.append(Paragraph(
        "<b>Hand sanitizer</b> — alcohol-based sanitizers are very drying "
        "and can irritate perioral skin when transferred by hand. Send him "
        "with a gentle, fragrance-free hand sanitizer or soap instead.",
        s["bullet"]))
    story.append(Paragraph(
        "<b>Post-lunch tooth brushing</b> — some schools have a post-lunch "
        "brushing program with school-provided toothpaste (fluoride, SLS, "
        "flavored). If so, send him with his own non-fluoride, SLS-free "
        "paste.",
        s["bullet"]))
    story.append(Paragraph(
        "<b>Art supplies</b> — paints, markers, play-doh, slime, glitter "
        "glue — anything that gets on hands and then transfers to the face. "
        "Which activities does he do on the days it's worst?",
        s["bullet"]))
    story.append(Paragraph(
        "<b>Toys he mouths</b> — identify specific toys and either clean "
        "them frequently, remove them from his access, or provide a safe "
        "dedicated chew item instead.",
        s["bullet"]))
    story.append(Paragraph(
        "<b>Desk and surface cleaners</b> — industrial cleaning sprays "
        "used on desks leave residue that transfers to hands and then "
        "face.",
        s["bullet"]))
    story.append(hr())

    # Breaking the rubbing and mouthing loops
    story.append(Paragraph(
        "Breaking the Rubbing and Mouthing Loops", s["h2"]))
    story.append(Paragraph(
        "These two behaviors are probably the biggest daily amplifiers of "
        "the rash. Each can be interrupted with replacement strategies "
        "that work better than just saying &quot;stop.&quot;",
        s["body"]))
    story.append(Paragraph(
        "<b>Hand rubbing:</b> He rubs the rash with the back of his hand "
        "when it's irritated. Each rub transfers hand contaminants to "
        "inflamed skin AND mechanically damages the barrier.",
        s["body"]))
    story.append(Paragraph(
        "Interventions:", s["body"]))
    story.append(Paragraph(
        "A fabric wristband or small Band-Aid on the back of the rubbing "
        "hand — acts as a tactile reminder (he feels the band before he "
        "touches his face)",
        s["bullet"]))
    story.append(Paragraph(
        "A fidget toy or squeeze ball to hold when he feels the urge",
        s["bullet"]))
    story.append(Paragraph(
        "Frequent thin moisturizer on the rash area — reduces the dryness "
        "and itch that drives the rubbing in the first place",
        s["bullet"]))
    story.append(Paragraph(
        "Short fingernails (less trauma from any scratching)",
        s["bullet"]))
    story.append(Paragraph(
        "Praise when he resists the urge (positive reinforcement)",
        s["bullet"]))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "<b>Toy mouthing:</b> Toys carry other kids' saliva, plastic "
        "residue, cleaning products, and dirt. Every toy-in-mouth episode "
        "transfers contaminants to hands and face.",
        s["body"]))
    story.append(Paragraph(
        "Interventions:", s["body"]))
    story.append(Paragraph(
        "Offer a sanctioned chew item: food-grade silicone chewy, chilled "
        "teether (if age-appropriate), or crunchy snacks at regular times",
        s["bullet"]))
    story.append(Paragraph(
        "Identify which toys he prefers to mouth — either clean them "
        "more frequently or swap for a safe alternative",
        s["bullet"]))
    story.append(Paragraph(
        "Consider whether the mouthing is sensory-seeking, anxiety, or "
        "just habit — replacement strategies (give him something TO chew) "
        "usually work better than prohibition",
        s["bullet"]))
    story.append(hr())

    # Timeline of improvement (no rebound — no steroid being withdrawn)
    story.append(Paragraph("Timeline of improvement", s["h2"]))
    story.append(Paragraph(
        "Metronidazole is slow. It does not produce dramatic overnight "
        "improvement. Here is what to expect when the protocol is followed:",
        s["body"]))
    story.append(Paragraph(
        "<b>Week 1:</b> Mild reduction in redness. New bumps may still form. "
        "Patience required.",
        s["bullet"]))
    story.append(Paragraph(
        "<b>Weeks 2–3:</b> Pustules start drying up. Fewer new bumps. The "
        "clear zone at the lip border may become more obvious as surrounding "
        "redness fades.",
        s["bullet"]))
    story.append(Paragraph(
        "<b>Weeks 4–6:</b> Noticeable overall improvement. Skin texture "
        "smoothing. Residual pink marks may persist even after papules are "
        "gone — those fade over weeks.",
        s["bullet"]))
    story.append(Paragraph(
        "<b>Call the pediatrician if:</b> the rash is getting dramatically "
        "worse rather than slowly improving, there is fever, the skin is "
        "weeping honey-colored crust (possible bacterial infection), or "
        "the child is in real discomfort.",
        s["body"]))
    story.append(hr())

    # If metronidazole isn't enough
    story.append(Paragraph(
        "If the metronidazole isn't enough after 4–6 weeks", s["h2"]))
    story.append(Paragraph(
        "Ask the pediatrician about one of these next-line options:",
        s["body"]))
    story.append(Paragraph(
        "<b>Topical pimecrolimus (Elidel)</b> — non-steroid calcineurin "
        "inhibitor, safe for children's faces. Can replace or supplement "
        "metronidazole. (You may have had this before. If so, the derm "
        "can re-prescribe.)",
        s["bullet"]))
    story.append(Paragraph(
        "<b>Oral azithromycin</b> — a 5–10 day course. Standard "
        "second-line for pediatric POD. Oral tetracyclines (doxycycline, "
        "minocycline) are contraindicated in children under 8.",
        s["bullet"]))
    story.append(Paragraph(
        "<b>Topical ivermectin (Soolantra)</b> — anti-Demodex cream. "
        "FDA-approved for rosacea in adults, used off-label in pediatric "
        "POD. If the POD is Demodex-driven, this can work when "
        "metronidazole alone is not enough.",
        s["bullet"]))
    story.append(hr())

    # What to avoid
    story.append(Paragraph("What to Avoid", s["h2"]))
    story.append(Paragraph(
        "<b>Any topical steroid on the face going forward</b> — "
        "hydrocortisone, fluticasone, desonide, mometasone, triamcinolone, "
        "betamethasone, clobetasol, or anything ending in -one or -olone. "
        "Even OTC hydrocortisone 1% should stay off the face. Steroids "
        "perpetuate POD even when they initially seem to help.",
        s["bullet"]))
    story.append(Paragraph(
        "<b>Heavy occlusive products around the mouth</b> — Aquaphor, "
        "Vaseline, thick petroleum jelly. Fine ON the lips themselves, not "
        "on the surrounding skin.",
        s["bullet"]))
    story.append(Paragraph(
        "<b>Fluoride toothpaste</b> — at least during the treatment phase.",
        s["bullet"]))
    story.append(Paragraph(
        "<b>Cosmetics, tinted lip balms, perfumed sunscreens on the affected "
        "area</b> — during treatment.",
        s["bullet"]))
    story.append(Paragraph(
        "<b>Any old cream from the dermatologist that wasn't specifically "
        "prescribed for POD.</b> If you are not sure what it does, do not "
        "use it. Label the tubes you DO use.",
        s["bullet"]))
    story.append(hr())

    # Cost table
    story.append(Paragraph("Total Monthly Cost", s["h2"]))
    cost_data = [
        ["Item", "Cost"],
        ["Metronidazole 0.75% (cream/lotion)", "~$15–30"],
        ["Non-fluoride, SLS-free toothpaste", "~$8"],
        ["Sulfur soap", "~$5–10"],
        ["CeraVe Moisturizing Cream", "~$15"],
        ["Vitamin D (continue from eczema plan)", "~$10"],
        ["Probiotic (continue from eczema plan)", "~$20"],
        ["Total", "~$75–95/month"],
    ]
    table = Table(cost_data, colWidths=[3.0 * inch, 1.8 * inch])
    table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e5e5e5")),
        ("BACKGROUND", (0, -1), (-1, -1), colors.HexColor("#f5f5f5")),
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.HexColor("#1a1a1a")),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("ALIGN", (1, 0), (1, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#cccccc")),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(table)
    story.append(hr())

    # The Key Idea
    story.append(Paragraph("The Key Idea", s["h2"]))
    story.append(Paragraph(
        "Most POD treatment is a cycle of &quot;which cream do we try "
        "next?&quot; The real question is &quot;what keeps bringing it "
        "back?&quot; There are three things happening at the same time:",
        s["body"]))
    story.append(Paragraph(
        "<b>Toothpaste residue lands on the skin twice daily</b> — swap "
        "to non-fluoride, SLS-free, unflavored",
        s["bullet"]))
    story.append(Paragraph(
        "<b>Demodex mites multiply when local immunity is off balance</b> "
        "— metronidazole reduces both mites and inflammation",
        s["bullet"]))
    story.append(Paragraph(
        "<b>The skin barrier needs gentle repair</b> — ceramide "
        "moisturizer, not heavy occlusives",
        s["bullet"]))
    story.append(Paragraph(
        "Address all three at once, and the cycle breaks. Metronidazole "
        "is slow — expect 4–6 weeks to full improvement, not overnight "
        "results. If the kid ever has a topical steroid prescribed for "
        "this rash, refuse it politely and ask for a non-steroid "
        "alternative — steroids on the face perpetuate POD rather than "
        "treating it.",
        s["body"]))
    story.append(hr())

    # References
    story.append(Paragraph("References", s["h2"]))
    refs = [
        "Tempark &amp; Shwayder 2014 — Perioral dermatitis: a review (Pediatric Dermatology)",
        "Weber &amp; Kowalzick 2012 — Perioral dermatitis in children (JDDG)",
        "Two et al. 2015 — Rosacea, sebaceous gland activity, and Demodex (Clinics in Dermatology)",
        "Del Rosso &amp; Webster 2007 — Sub-antimicrobial doxycycline in rosacea (Cutis)",
        "Hengge et al. 2006 — Adverse effects of topical glucocorticosteroids (JAAD)",
        "Schwarz et al. 2001 — Childhood perioral dermatitis (Pediatric Dermatology)",
        "Reinholz et al. 2016 — Pathogenesis and clinical presentation of rosacea (JDDG)",
    ]
    for r in refs:
        story.append(Paragraph(r, s["ref"]))

    return story


def main():
    doc = SimpleDocTemplate(
        OUTPUT_PDF, pagesize=letter,
        topMargin=0.7 * inch, bottomMargin=0.7 * inch,
        leftMargin=0.9 * inch, rightMargin=0.9 * inch,
        title="Perioral Dermatitis Plan",
        author="open_problems medical",
    )
    styles = build_styles()
    story = build_story(styles)
    doc.build(story)
    print(f"PDF: {OUTPUT_PDF}")
    size = os.path.getsize(OUTPUT_PDF)
    print(f"  size: {size} bytes ({size/1024:.1f} KB)")


if __name__ == "__main__":
    main()
