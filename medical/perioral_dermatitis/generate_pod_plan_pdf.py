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
        "Here is the key thing to understand: <b>most pediatric perioral "
        "dermatitis is caused or perpetuated by topical steroid creams.</b> "
        "The steroid helps for a few days, the rash comes back worse when you "
        "stop, you (or the doctor) reapply, and the cycle becomes chronic. "
        "The cure requires completely stopping the steroid and tolerating "
        "1–3 weeks of visible worsening before improvement begins. That "
        "&quot;it gets worse before it gets better&quot; phase is the hardest "
        "part of the protocol — and the reason most kids end up with chronic "
        "POD is that parents and pediatricians cannot tolerate watching the "
        "rash flare and reapply the steroid.",
        s["body"]))
    story.append(Paragraph(
        "There are also other contributors: toothpaste ingredients (fluoride, "
        "the SLS foaming agent, mint and cinnamon flavorings), lip balms, "
        "cosmetics, sunscreens, and Demodex mites (which live on everyone's "
        "face and multiply when the local immune system is suppressed by "
        "steroids). The protocol below addresses all of these at once. It is "
        "stricter than what most dermatologists prescribe, but it works when "
        "followed.",
        s["body"]))
    story.append(hr())

    # 1. Stop the fluticasone
    story.append(Paragraph("1. Stop the fluticasone — #1 priority", s["h3"]))
    story.append(Paragraph(
        "<b>Why:</b> Fluticasone is a topical corticosteroid. Steroids on a "
        "child's face cause or perpetuate POD via a rebound cycle: helps "
        "short-term, flares worse when stopped, leading to reapplication and "
        "chronicity. The steroid is the problem, not the treatment.",
        s["body"]))
    story.append(Paragraph(
        "<b>How:</b> Stop applying it completely. Do not put it back on even "
        "if the rash looks worse over the next 1–3 weeks. The worsening IS "
        "the treatment working.",
        s["body"]))
    story.append(Paragraph("<b>Cost:</b> Free (stopping something)", s["body"]))
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

    # 3. Metronidazole cream
    story.append(Paragraph(
        "3. Metronidazole cream 0.75% (prescription)", s["h3"]))
    story.append(Paragraph(
        "<b>What:</b> MetroCream or MetroLotion — the 0.75% formulation. "
        "<b>Ask for the cream or lotion, NOT the gel.</b> The gel uses an "
        "alcohol vehicle that stings on already-inflamed skin. The cream is "
        "much better tolerated for children's faces.",
        s["body"]))
    story.append(Paragraph(
        "<b>Why:</b> Metronidazole is the first-line topical treatment for "
        "POD. It reduces local inflammation, has mild anti-Demodex activity, "
        "and is not a steroid (so no rebound cycle). It is safe for children.",
        s["body"]))
    story.append(Paragraph(
        "<b>How:</b> Thin layer twice daily on the affected area. Apply after "
        "washing the face with plain water or CeraVe Hydrating Cleanser. "
        "Expect to use it for 4–6 weeks. Do not use it on the lips themselves, "
        "only on the surrounding skin where the rash is.",
        s["body"]))
    story.append(Paragraph(
        "<b>Cost:</b> ~$15–30 with insurance, up to $60 without. Generic "
        "metronidazole is widely available.", s["body"]))
    story.append(hr())

    # 4. CeraVe
    story.append(Paragraph(
        "4. CeraVe Moisturizing Cream — barrier repair", s["h3"]))
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

    # 5. Vitamin D
    story.append(Paragraph(
        "5. Vitamin D — keep the current dose, do not megadose", s["h3"]))
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

    # For the rebound flare
    story.append(Paragraph("For the Rebound Flare — the hard part", s["h2"]))
    story.append(Paragraph(
        "This is the part where most people give up and restart the steroid. "
        "If you do, the cycle resets and nothing works. Hold the line.",
        s["body"]))
    story.append(Paragraph(
        "<b>Days 1–7:</b> The rash will look worse. Redness increases. New "
        "bumps may appear. This is the treatment working, not failing.",
        s["bullet"]))
    story.append(Paragraph(
        "<b>Days 7–14:</b> The rash plateaus at its worst. You will be very "
        "tempted to put the fluticasone back on. <b>Do not.</b>",
        s["bullet"]))
    story.append(Paragraph(
        "<b>Days 14–21:</b> First signs of improvement. Redness starts "
        "fading. New bumps stop forming.",
        s["bullet"]))
    story.append(Paragraph(
        "<b>Weeks 3–6:</b> Rapid improvement. The clear zone around the "
        "lips expands. The rash resolves.",
        s["bullet"]))
    story.append(Paragraph(
        "<b>Call the pediatrician if:</b> fever, skin is weeping honey-colored "
        "crust (possible bacterial infection), or the child is losing sleep "
        "from pain. Otherwise, continue the protocol through the worsening "
        "phase.",
        s["body"]))
    story.append(hr())

    # If metronidazole isn't enough
    story.append(Paragraph(
        "If the metronidazole isn't enough after 4 weeks", s["h2"]))
    story.append(Paragraph(
        "Ask the pediatrician about one of these next-line options:",
        s["body"]))
    story.append(Paragraph(
        "<b>Topical pimecrolimus (Elidel)</b> — non-steroid "
        "anti-inflammatory, safe for children's faces. Can replace or "
        "supplement metronidazole.",
        s["bullet"]))
    story.append(Paragraph(
        "<b>Oral azithromycin</b> — a 5–10 day course. Standard "
        "second-line for pediatric POD. Oral tetracyclines (doxycycline, "
        "minocycline) are contraindicated in children under 8.",
        s["bullet"]))
    story.append(hr())

    # What to avoid
    story.append(Paragraph("What to Avoid", s["h2"]))
    story.append(Paragraph(
        "<b>Any topical steroid on the face</b> — hydrocortisone, fluticasone, "
        "desonide, mometasone, triamcinolone, betamethasone, clobetasol, or "
        "anything ending in -one or -olone. Even over-the-counter "
        "hydrocortisone 1% should come off.",
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
        ["Stop fluticasone", "$0"],
        ["Non-fluoride toothpaste", "~$8"],
        ["Metronidazole cream", "~$15–30"],
        ["CeraVe moisturizer", "~$15"],
        ["Vitamin D", "~$10 (continue)"],
        ["Probiotic", "~$20 (continue)"],
        ["Total", "~$70/month"],
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

    # What to expect
    story.append(Paragraph("What to Expect", s["h2"]))
    story.append(Paragraph(
        "<b>Weeks 1–2:</b> Rash looks worse (rebound flare). Hardest part. "
        "Hold the line.", s["bullet"]))
    story.append(Paragraph(
        "<b>Week 2–3:</b> Worst of the flare plateaus. Do not reapply the "
        "steroid.", s["bullet"]))
    story.append(Paragraph(
        "<b>Weeks 3–6:</b> Rapid improvement. Clear zone expands. Rash "
        "fades.", s["bullet"]))
    story.append(Paragraph(
        "<b>Months 2–3:</b> Complete or near-complete resolution if all "
        "triggers were addressed.", s["bullet"]))
    story.append(Paragraph(
        "<b>Long-term:</b> Avoid topical steroids on the face permanently. "
        "If a new rash appears, get it properly diagnosed before putting "
        "anything on it.",
        s["bullet"]))
    story.append(hr())

    # The Key Idea
    story.append(Paragraph("The Key Idea", s["h2"]))
    story.append(Paragraph(
        "Most POD treatment is a cycle of &quot;which cream do we try next?&quot; "
        "The real question is &quot;what keeps bringing it back?&quot; There "
        "are four things happening at the same time:",
        s["body"]))
    story.append(Paragraph(
        "<b>The steroid cream is the cause, not the cure</b> — stop it and "
        "tolerate the rebound",
        s["bullet"]))
    story.append(Paragraph(
        "<b>Toothpaste residue lands on the skin twice daily</b> — swap to "
        "non-fluoride, SLS-free, unflavored",
        s["bullet"]))
    story.append(Paragraph(
        "<b>Demodex mites multiply when local immunity is suppressed</b> — "
        "metronidazole reduces both mites and inflammation",
        s["bullet"]))
    story.append(Paragraph(
        "<b>The skin barrier needs gentle repair</b> — ceramide moisturizer, "
        "not heavy occlusives",
        s["bullet"]))
    story.append(Paragraph(
        "Address all four at once, and the cycle breaks. The mechanism is "
        "understood and the drugs work — the reason POD becomes chronic is "
        "that the treatment requires tolerating 1–3 weeks of visible "
        "worsening, and without written expectations most parents reapply "
        "the steroid during that window.",
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
