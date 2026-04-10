#!/usr/bin/env python3
"""
Generate a pixel-art infographic for "What Is Time?" final answer.
Builds 3 sections independently, then stacks them.

Output: ~/Downloads/WHAT_IS_TIME.png
"""

from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT = os.path.expanduser("~/Downloads/WHAT_IS_TIME.png")
W = 1200
BG = (15, 10, 26)
ACCENT = (192, 38, 211)
CYAN = (34, 211, 238)
ORANGE = (245, 158, 11)
GREEN = (34, 197, 94)
RED = (239, 68, 68)
WHITE = (226, 224, 234)
DIM = (139, 133, 160)
GOLD = (255, 215, 0)
PIXEL = 16


def draw_pixel_block(draw, x, y, grid, palette, scale=PIXEL):
    for row_i, row in enumerate(grid):
        for col_i, val in enumerate(row):
            if val == 0:
                continue
            color = palette.get(val, WHITE)
            x0 = x + col_i * scale
            y0 = y + row_i * scale
            draw.rectangle([x0, y0, x0 + scale - 1, y0 + scale - 1], fill=color)


def try_font(size):
    for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def wrap_text(draw, text, font, max_width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = f"{cur} {w}".strip()
        if draw.textbbox((0, 0), test, font=font)[2] > max_width:
            if cur:
                lines.append(cur)
            cur = w
        else:
            cur = test
    if cur:
        lines.append(cur)
    return lines


def draw_text_block(draw, x, y, title, body, title_color=ACCENT,
                    max_width=520, title_size=22, body_size=15):
    tf = try_font(title_size)
    bf = try_font(body_size)
    draw.text((x, y), title, fill=title_color, font=tf)
    y += title_size + 10
    for line in wrap_text(draw, body, bf, max_width):
        draw.text((x, y), line, fill=WHITE, font=bf)
        y += body_size + 5
    return y


def add_scanlines(draw, w, h):
    for sy in range(0, h, 4):
        draw.line([(0, sy), (w, sy)], fill=(20, 14, 32), width=1)


# ============================================================
# SPRITES
# ============================================================

def hourglass():
    pal = {1: GOLD, 2: CYAN, 3: (180, 160, 100), 4: ACCENT}
    g = [
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
        [0,0,0,1,2,2,2,2,2,2,2,2,1,0,0,0],
        [0,0,0,1,2,2,2,2,2,2,2,2,1,0,0,0],
        [0,0,0,0,1,2,2,2,2,2,2,1,0,0,0,0],
        [0,0,0,0,0,1,2,2,2,2,1,0,0,0,0,0],
        [0,0,0,0,0,0,1,2,2,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,3,3,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,4,4,1,0,0,0,0,0,0],
        [0,0,0,0,0,1,3,3,3,3,1,0,0,0,0,0],
        [0,0,0,0,1,3,3,3,3,3,3,1,0,0,0,0],
        [0,0,0,1,3,3,3,3,3,3,3,3,1,0,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
    ]
    return g, pal

def brain():
    pal = {1: (255, 180, 200), 2: (220, 130, 160), 3: (180, 90, 120), 4: ACCENT}
    g = [
        [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
        [0,0,0,1,1,2,2,2,2,2,2,1,1,0,0,0],
        [0,0,1,2,2,1,2,2,2,1,2,2,2,1,0,0],
        [0,1,2,1,2,2,1,2,1,2,2,1,2,2,1,0],
        [1,2,2,1,2,2,3,3,3,2,2,1,2,2,2,1],
        [1,2,1,2,2,3,4,4,4,3,2,2,1,2,2,1],
        [1,2,2,1,2,3,4,4,4,3,2,1,2,2,2,1],
        [1,2,1,2,2,3,3,3,3,3,2,2,1,2,2,1],
        [0,1,2,2,1,2,2,2,2,2,1,2,2,2,1,0],
        [0,0,1,2,2,2,1,1,1,2,2,2,2,1,0,0],
        [0,0,0,1,1,2,2,2,2,2,2,1,1,0,0,0],
        [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
    ]
    return g, pal

def explosion():
    pal = {1: RED, 2: ORANGE, 3: GOLD, 4: WHITE}
    g = [
        [0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],
        [0,0,1,0,0,0,1,0,1,0,0,0,1,0,0],
        [0,0,0,1,0,1,2,1,2,1,0,1,0,0,0],
        [0,1,0,0,1,2,3,3,3,2,1,0,0,1,0],
        [0,0,1,1,2,3,3,4,3,3,2,1,1,0,0],
        [1,0,1,2,3,3,4,4,4,3,3,2,1,0,1],
        [0,1,2,3,3,4,4,4,4,4,3,3,2,1,0],
        [0,1,2,3,3,4,4,4,4,4,3,3,2,1,0],
        [1,0,1,2,3,3,4,4,4,3,3,2,1,0,1],
        [0,0,1,1,2,3,3,4,3,3,2,1,1,0,0],
        [0,1,0,0,1,2,3,3,3,2,1,0,0,1,0],
        [0,0,0,1,0,1,2,1,2,1,0,1,0,0,0],
        [0,0,1,0,0,0,1,0,1,0,0,0,1,0,0],
        [0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],
    ]
    return g, pal

def butterfly():
    pal = {1: CYAN, 2: (20, 160, 200), 3: ACCENT, 4: WHITE}
    g = [
        [0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0],
        [0,1,2,2,1,0,0,0,0,0,0,1,2,2,1,0],
        [1,2,3,2,2,1,0,0,0,0,1,2,2,3,2,1],
        [1,2,3,3,2,2,1,0,0,1,2,2,3,3,2,1],
        [1,2,2,3,2,2,2,4,4,2,2,2,3,2,2,1],
        [0,1,2,2,2,2,4,4,4,4,2,2,2,2,1,0],
        [0,0,1,2,2,2,4,4,4,4,2,2,2,1,0,0],
        [0,0,0,1,2,2,2,4,4,2,2,2,1,0,0,0],
        [0,0,1,2,3,2,2,4,4,2,2,3,2,1,0,0],
        [0,1,2,3,3,2,1,0,0,1,2,3,3,2,1,0],
        [1,2,2,2,2,1,0,0,0,0,1,2,2,2,2,1],
        [0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0],
    ]
    return g, pal

def thermometer():
    pal = {1: WHITE, 2: RED, 3: (100, 100, 120)}
    g = [
        [0,0,0,1,1,0,0,0],
        [0,0,1,3,3,1,0,0],
        [0,0,1,3,3,1,0,0],
        [0,0,1,2,2,1,0,0],
        [0,0,1,2,2,1,0,0],
        [0,0,1,2,2,1,0,0],
        [0,0,1,2,2,1,0,0],
        [0,0,1,2,2,1,0,0],
        [0,1,2,2,2,2,1,0],
        [0,1,2,2,2,2,1,0],
        [0,1,2,2,2,2,1,0],
        [0,0,1,1,1,1,0,0],
    ]
    return g, pal


# ============================================================
# SECTION BUILDERS
# ============================================================

def build_header():
    """Title section."""
    h = 180
    img = Image.new("RGB", (W, h), BG)
    draw = ImageDraw.Draw(img)
    add_scanlines(draw, W, h)

    draw.text((W // 2 - 250, 25), "WHAT IS TIME?", fill=WHITE, font=try_font(48))
    draw.text((W // 2 - 260, 85), "Five levels. Three numbers. Zero free parameters.",
              fill=DIM, font=try_font(16))
    draw.text((W // 2 - 150, 115), "gobbleyourdong x turbogranny",
              fill=ACCENT, font=try_font(13))
    draw.line([(60, h - 10), (W - 60, h - 10)], fill=ACCENT, width=2)
    return img


def build_section(sprite_fn, sprite_side, title, body, stats, title_color=ACCENT):
    """Build one section: sprite on one side, text on the other.
    sprite_side: 'left' or 'right'
    stats: list of (value, label, color) tuples
    """
    # Pre-calculate height
    temp_img = Image.new("RGB", (W, 1000), BG)
    temp_draw = ImageDraw.Draw(temp_img)
    text_x = 550 if sprite_side == "left" else 80
    text_max_w = 550 if sprite_side == "left" else 480
    y = 40
    y = draw_text_block(temp_draw, text_x, y, title, body,
                        title_color=title_color, max_width=text_max_w)
    y += 15
    for val, label, color in stats:
        y += 50
    y += 60  # padding bottom

    # Sprite height
    grid, _ = sprite_fn()
    sprite_h = len(grid) * PIXEL
    h = max(y, sprite_h + 80)
    img = Image.new("RGB", (W, h), BG)
    draw = ImageDraw.Draw(img)
    add_scanlines(draw, W, h)

    # Draw sprite — centered in its column
    grid, pal = sprite_fn()
    sprite_w = len(grid[0]) * PIXEL
    sprite_h_px = len(grid) * PIXEL
    if sprite_side == "left":
        # Center in left column (0-500)
        sx = (450 - sprite_w) // 2 + 30
    else:
        # Center in right column (600-1200)
        sx = 600 + (550 - sprite_w) // 2
    # Vertically center sprite in section
    sy = max(30, (h - sprite_h_px) // 2)
    draw_pixel_block(draw, sx, sy, grid, pal, scale=PIXEL)

    # Draw text
    text_x = 550 if sprite_side == "left" else 80
    text_max_w = 550 if sprite_side == "left" else 480
    y = 40
    y = draw_text_block(draw, text_x, y, title, body,
                        title_color=title_color, max_width=text_max_w)
    y += 15

    # Draw stats
    for val, label, color in stats:
        nf = try_font(22)
        lf = try_font(11)
        draw.text((text_x, y), val, fill=color, font=nf)
        draw.text((text_x, y + 28), label, fill=DIM, font=lf)
        y += 50

    # Bottom rule
    draw.line([(60, h - 10), (W - 60, h - 10)], fill=ACCENT, width=1)
    return img


def build_temp_table():
    """Temperature prediction section with table."""
    h = 420
    img = Image.new("RGB", (W, h), BG)
    draw = ImageDraw.Draw(img)
    add_scanlines(draw, W, h)

    # Thermometer on right — centered in right column
    grid, pal = thermometer()
    tw = len(grid[0]) * PIXEL
    th = len(grid) * PIXEL
    tx = 600 + (550 - tw) // 2
    ty = max(30, (h - th) // 2)
    draw_pixel_block(draw, tx, ty, grid, pal, scale=PIXEL)

    # Text on left
    y = draw_text_block(draw, 80, 20,
        "THE KILLER PREDICTION",
        "Your sense of time is temperature-dependent. The same "
        "Boltzmann factor that drives entropy also drives your ion "
        "channels. Cool the brain and 'now' stretches. Warm it and "
        "'now' contracts. Testable TODAY with a temporal judgment task "
        "in hypothermia patients. Q₁₀ ≈ 1.7 distinguishes this from "
        "neural oscillator models (Q₁₀ ≈ 1.3).",
        title_color=ORANGE, max_width=540)
    y += 15

    # Table
    tf = try_font(14)
    header_f = try_font(13)
    draw.text((100, y), "CONDITION", fill=ACCENT, font=header_f)
    draw.text((320, y), "TEMP", fill=ACCENT, font=header_f)
    draw.text((420, y), "'NOW'", fill=ACCENT, font=header_f)
    draw.text((520, y), "CHANGE", fill=ACCENT, font=header_f)
    y += 22

    rows = [
        ("Hypothermia", "33°C", "3.18s", "+24%", GREEN),
        ("Normal", "37°C", "2.56s", "—", CYAN),
        ("Fever", "42°C", "1.97s", "−23%", RED),
    ]
    for cond, temp, sp, change, color in rows:
        draw.text((100, y), cond, fill=DIM, font=tf)
        draw.text((320, y), temp, fill=DIM, font=tf)
        draw.text((420, y), sp, fill=color, font=tf)
        draw.text((520, y), change, fill=color, font=tf)
        y += 22

    draw.line([(60, h - 10), (W - 60, h - 10)], fill=ACCENT, width=1)
    return img


def build_footer():
    """Bottom section with the three key numbers and attribution."""
    h = 180
    img = Image.new("RGB", (W, h), BG)
    draw = ImageDraw.Draw(img)
    add_scanlines(draw, W, h)

    # Three numbers side by side
    nf = try_font(20)
    lf = try_font(11)
    positions = [
        (100, "167 steps", "microscale\nchaos lock-in", ORANGE),
        (460, "2.56 seconds", "neural scale\nphenomenal now", GREEN),
        (830, "13.8 Gyr", "cosmological\nthermodynamic arrow", RED),
    ]
    for x, val, label, color in positions:
        draw.text((x, 20), val, fill=color, font=nf)
        for i, line in enumerate(label.split("\n")):
            draw.text((x, 46 + i * 15), line, fill=DIM, font=lf)

    # Tagline
    draw.text((W // 2 - 310, 95),
              "Time is not one thing. It is five levels, each built on the last.",
              fill=WHITE, font=try_font(14))
    draw.text((W // 2 - 290, 118),
              "One mechanism — the Boltzmann factor — connects them across 22 orders of magnitude.",
              fill=DIM, font=try_font(11))

    draw.text((W // 2 - 160, 148),
              "github.com/gobbleyourdong/open_problems",
              fill=ACCENT, font=try_font(11))

    draw.rectangle([4, 0, W - 5, h - 1], outline=ACCENT, width=2)
    return img


def main():
    sections = [
        build_header(),
        build_section(hourglass, "left",
            "LEVEL 1 — THE THERMODYNAMIC ARROW",
            "Time flows in the direction of entropy increase. "
            "A gas spreads from ordered to disordered: Shannon entropy "
            "5.47 → 6.16 bits, monotone increasing. The arrow needs "
            "two things — a low-entropy Big Bang and collisions that "
            "make the spread irreversible. Without collisions, you can "
            "reverse time perfectly. The arrow is in the initial "
            "conditions, not in the laws.",
            [("ΔS = +0.698 bits", "entropy increase over 200 steps", CYAN)]),
        build_section(butterfly, "right",
            "LEVEL 2 — THE LYAPUNOV ARROW",
            "Time is enforced by chaos. A perturbation of one part "
            "in 100 million doubles every 6.3 steps. After 167 steps "
            "the trajectory has completely forgotten whether it's "
            "running forward or backward. This is why you can't "
            "unscramble an egg — chaos locks in the arrow at every "
            "moment. The Lyapunov exponent is the universe's "
            "forgetting rate.",
            [("λ = 0.110 per step", "Lyapunov exponent", ORANGE),
             ("167 steps to forget", "perturbation 10⁻⁸ → O(1)", ORANGE)]),
        build_section(brain, "left",
            "LEVEL 3 — THE NEURAL ARROW",
            "Time is how fast your brain updates its model of reality. "
            "860 billion ion channels × 1000 Hz via thermal noise = "
            "8.6×10²⁰ bits/s of raw data, compressed to 50 bits/s "
            "of conscious experience. A quantum clock (Page-Wootters) "
            "gives 128 distinguishable moments. Divide: 128 ÷ 50 = "
            "2.56 seconds. That's the duration of your 'now'. "
            "No parameters were fitted. Two independent physics "
            "domains combine to reproduce the measured specious present.",
            [("2.56 seconds", "the specious present — your 'now'", GREEN),
             ("50 bits/s", "conscious bandwidth", GREEN),
             ("128 moments", "Page-Wootters clock (7 qubits)", GREEN)]),
        build_temp_table(),
        build_section(explosion, "left",
            "THE BIG PICTURE",
            "Three numbers span 22 orders of magnitude — all derived "
            "from the same framework with zero tuning. The Lyapunov "
            "timescale is where reversal fails at the microscale. "
            "The specious present is where your brain integrates "
            "experience. The age of the universe is the total scope "
            "of the thermodynamic arrow. One mechanism — the Boltzmann "
            "factor exp(−E/kT) — connects them all.",
            []),
        build_footer(),
    ]

    total_h = sum(s.height for s in sections)
    final = Image.new("RGB", (W, total_h), BG)

    # Add border
    border_draw = ImageDraw.Draw(final)
    border_draw.rectangle([2, 2, W - 3, total_h - 3], outline=ACCENT, width=2)

    y = 0
    for s in sections:
        final.paste(s, (0, y))
        y += s.height

    final.save(OUTPUT, "PNG")
    print(f"Saved: {OUTPUT}")
    print(f"Size: {os.path.getsize(OUTPUT) // 1024} KB")
    print(f"Dimensions: {final.size}")


if __name__ == "__main__":
    main()
