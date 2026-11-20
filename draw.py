#!/usr/bin/env python3
"""Draw THE WORLD - Friday 20 November 2026 newspaper front page (1024x1024).

Own work, drawn with PIL from the verified news of 20 Nov 2026.
Eight stories: Myanmar ICJ ruling (lead), Shenzhen summit, Kyiv strikes,
Riyadh PIF Tower, Hormuz tanker, Poland airspace breach, COP31, markets.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (20, 20, 22)
RED = (178, 24, 24)
DARKRED = (140, 16, 16)
GREY = (90, 86, 78)
CARD = (255, 255, 255)
LINE = (180, 172, 156)
BLUE = (28, 68, 128)
GOLD = (196, 138, 28)
GREEN = (34, 120, 70)
ORANGE = (224, 110, 20)

FDIR = "/usr/share/fonts/truetype/noto/"
SERIF_BLACK = FDIR + "NotoSerif-Black.ttf"
SERIF_BOLD = FDIR + "NotoSerif-Bold.ttf"
SANS = FDIR + "NotoSans-Regular.ttf"
SANS_BOLD = FDIR + "NotoSans-Bold.ttf"
SANS_BLACK = FDIR + "NotoSans-Black.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap to the given pixel width."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit_lines(draw, text, fnt_path, start_size, width, max_lines, min_size=10):
    """Shrink font until text fits in max_lines; return (font, lines)."""
    size = start_size
    while size >= min_size:
        fnt = font(fnt_path, size)
        lines = wrap(draw, text, fnt, width)
        if len(lines) <= max_lines:
            return fnt, lines
        size -= 1
    fnt = font(fnt_path, min_size)
    return fnt, wrap(draw, text, fnt, width)[:max_lines]


def draw_text_lines(draw, lines, fnt, x, y, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


# ---------------- icons (all drawn with PIL primitives) ----------------

def icon_scales(d, cx, cy, s, col):
    # pole, crossbar, two pans
    d.line([(cx, cy - 42 * s), (cx, cy + 38 * s)], fill=col, width=max(3, int(5 * s)))
    d.line([(cx - 52 * s, cy - 30 * s), (cx + 52 * s, cy - 30 * s)], fill=col, width=max(3, int(5 * s)))
    d.ellipse([cx - 8 * s, cy - 52 * s, cx + 8 * s, cy - 36 * s], fill=GOLD)
    for sx in (-52 * s, 52 * s):
        d.line([(cx + sx, cy - 30 * s), (cx + sx, cy - 6 * s)], fill=col, width=max(2, int(3 * s)))
        d.line([(cx + sx - 16 * s, cy - 6 * s), (cx + sx, cy + 16 * s)], fill=col, width=max(2, int(3 * s)))
        d.line([(cx + sx + 16 * s, cy - 6 * s), (cx + sx, cy + 16 * s)], fill=col, width=max(2, int(3 * s)))
        d.pieslice([cx + sx - 20 * s, cy - 2 * s, cx + sx + 20 * s, cy + 30 * s], 0, 180, fill=(210, 205, 190), outline=col, width=max(2, int(3 * s)))
    d.line([(cx - 26 * s, cy + 38 * s), (cx + 26 * s, cy + 38 * s)], fill=col, width=max(3, int(5 * s)))


def icon_flags(d, cx, cy, s):
    # three flags on poles above a round table
    cols = [(178, 24, 24), (28, 68, 128), (196, 138, 28)]
    for i, c in enumerate(cols):
        x = cx + (i - 1) * 44 * s
        d.line([(x, cy - 44 * s), (x, cy + 6 * s)], fill=INK, width=max(2, int(3 * s)))
        d.polygon([(x, cy - 44 * s), (x + 30 * s, cy - 34 * s), (x, cy - 24 * s)], fill=c)
    d.ellipse([cx - 58 * s, cy + 6 * s, cx + 58 * s, cy + 26 * s], fill=(120, 84, 52))
    d.rectangle([cx - 6 * s, cy + 26 * s, cx + 6 * s, cy + 46 * s], fill=(120, 84, 52))


def icon_missile(d, cx, cy, s):
    # big missile diving onto a bridge arc, blast star at impact
    d.arc([cx - 62 * s, cy + 2 * s, cx + 62 * s, cy + 62 * s], 180, 360, fill=BLUE, width=max(3, int(5 * s)))
    d.line([(cx - 62 * s, cy + 32 * s), (cx + 62 * s, cy + 32 * s)], fill=BLUE, width=max(2, int(3 * s)))
    for bx in (-40, 40):
        d.line([(cx + bx * s, cy + 32 * s), (cx + bx * s, cy + 50 * s)], fill=BLUE, width=max(2, int(3 * s)))
    # missile body: thick diagonal line, nose down-right toward the bridge
    d.line([(cx - 42 * s, cy - 44 * s), (cx - 6 * s, cy - 8 * s)], fill=RED, width=max(5, int(10 * s)))
    d.polygon([(cx - 6 * s, cy - 8 * s), (cx - 16 * s, cy - 18 * s), (cx - 2 * s, cy - 20 * s)], fill=DARKRED)
    # fins at the tail
    d.polygon([(cx - 42 * s, cy - 44 * s), (cx - 52 * s, cy - 30 * s), (cx - 46 * s, cy - 52 * s)], fill=DARKRED)
    d.polygon([(cx - 42 * s, cy - 44 * s), (cx - 28 * s, cy - 54 * s), (cx - 50 * s, cy - 50 * s)], fill=DARKRED)
    # exhaust flame at the tail
    d.polygon([(cx - 44 * s, cy - 46 * s), (cx - 58 * s, cy - 58 * s), (cx - 52 * s, cy - 42 * s)], fill=ORANGE)
    # blast star at impact point
    import math
    bx, by = cx + 4 * s, cy + 18 * s
    for a in range(8):
        ang = a * math.pi / 4
        x1 = bx + 24 * s * math.cos(ang)
        y1 = by + 24 * s * math.sin(ang)
        x2 = bx + 9 * s * math.cos(ang)
        y2 = by + 9 * s * math.sin(ang)
        d.line([(x2, y2), (x1, y1)], fill=ORANGE, width=max(2, int(4 * s)))
    d.ellipse([bx - 9 * s, by - 9 * s, bx + 9 * s, by + 9 * s], fill=GOLD)


def icon_tower(d, cx, cy, s):
    # tall skyscraper, bent top, broken windows
    d.polygon([(cx - 22 * s, cy + 48 * s), (cx - 16 * s, cy - 46 * s), (cx + 16 * s, cy - 46 * s), (cx + 22 * s, cy + 48 * s)], fill=(70, 90, 120))
    d.polygon([(cx - 16 * s, cy - 46 * s), (cx + 2 * s, cy - 58 * s), (cx + 16 * s, cy - 46 * s)], fill=(50, 68, 96))
    for r in range(6):
        y = cy - 30 * s + r * 13 * s
        for c in range(3):
            x = cx - 13 * s + c * 11 * s
            col = (240, 220, 120) if (r + c) % 3 else (200, 210, 225)
            d.rectangle([x, y, x + 7 * s, y + 7 * s], fill=col)
    # crack + smoke
    d.line([(cx + 4 * s, cy - 40 * s), (cx + 14 * s, cy - 26 * s), (cx + 6 * s, cy - 14 * s)], fill=RED, width=max(2, int(3 * s)))
    d.ellipse([cx + 18 * s, cy - 62 * s, cx + 34 * s, cy - 46 * s], fill=(150, 150, 150))
    d.ellipse([cx + 28 * s, cy - 72 * s, cx + 40 * s, cy - 60 * s], fill=(170, 170, 170))


def icon_tanker(d, cx, cy, s):
    # tanker hull on waves with flames
    d.polygon([(cx - 62 * s, cy + 8 * s), (cx + 62 * s, cy + 8 * s), (cx + 48 * s, cy + 34 * s), (cx - 48 * s, cy + 34 * s)], fill=(140, 30, 30))
    d.rectangle([cx - 30 * s, cy - 12 * s, cx + 6 * s, cy + 8 * s], fill=(200, 200, 200))
    d.rectangle([cx + 14 * s, cy - 22 * s, cx + 26 * s, cy + 8 * s], fill=(90, 90, 90))
    for fx, fh in ((-14, 26), (0, 34), (14, 24)):
        d.polygon([(cx + (fx - 9) * s, cy - 12 * s), (cx + fx * s, cy - 12 * s - fh * s),
                   (cx + (fx + 9) * s, cy - 12 * s)], fill=ORANGE)
    d.arc([cx - 66 * s, cy + 38 * s, cx - 20 * s, cy + 52 * s], 0, 180, fill=BLUE, width=max(2, int(3 * s)))
    d.arc([cx - 10 * s, cy + 38 * s, cx + 36 * s, cy + 52 * s], 0, 180, fill=BLUE, width=max(2, int(3 * s)))
    d.arc([cx + 40 * s, cy + 38 * s, cx + 70 * s, cy + 52 * s], 0, 180, fill=BLUE, width=max(2, int(3 * s)))


def icon_border(d, cx, cy, s):
    # missile crossing a dashed border, NATO-style compass star
    d.line([(cx - 66 * s, cy + 30 * s), (cx + 66 * s, cy + 30 * s)], fill=INK, width=max(2, int(3 * s)))
    for i in range(7):
        x = cx - 60 * s + i * 20 * s
        d.line([(x, cy + 30 * s), (x + 10 * s, cy + 30 * s)], fill=RED, width=max(3, int(5 * s)))
    d.line([(cx - 44 * s, cy - 34 * s), (cx - 4 * s, cy - 6 * s)], fill=RED, width=max(5, int(10 * s)))
    d.polygon([(cx - 4 * s, cy - 6 * s), (cx - 14 * s, cy - 16 * s), (cx + 2 * s, cy - 18 * s)], fill=DARKRED)
    d.polygon([(cx - 44 * s, cy - 34 * s), (cx - 54 * s, cy - 20 * s), (cx - 48 * s, cy - 42 * s)], fill=DARKRED)
    d.polygon([(cx - 46 * s, cy - 36 * s), (cx - 60 * s, cy - 48 * s), (cx - 54 * s, cy - 32 * s)], fill=ORANGE)
    # compass star
    sx, sy = cx + 38 * s, cy - 22 * s
    d.polygon([(sx, sy - 20 * s), (sx + 5 * s, sy - 5 * s), (sx + 20 * s, sy), (sx + 5 * s, sy + 5 * s),
               (sx, sy + 20 * s), (sx - 5 * s, sy + 5 * s), (sx - 20 * s, sy), (sx - 5 * s, sy - 5 * s)], fill=BLUE)


def icon_climate(d, cx, cy, s):
    # globe with leaf, oil drop crossed out
    d.ellipse([cx - 46 * s, cy - 40 * s, cx + 10 * s, cy + 16 * s], outline=GREEN, width=max(3, int(4 * s)))
    d.arc([cx - 46 * s, cy - 40 * s, cx + 10 * s, cy + 16 * s], 200, 340, fill=GREEN, width=max(2, int(3 * s)))
    d.ellipse([cx - 34 * s, cy - 28 * s, cx - 10 * s, cy - 8 * s], fill=GREEN)
    d.ellipse([cx - 26 * s, cy + 0 * s, cx - 4 * s, cy + 12 * s], fill=(120, 190, 140))
    d.ellipse([cx - 40 * s, cy - 12 * s, cx - 28 * s, cy - 2 * s], fill=(120, 190, 140))
    # oil drop with red X
    dx, dy = cx + 38 * s, cy - 6 * s
    d.ellipse([dx - 16 * s, dy - 6 * s, dx + 16 * s, dy + 26 * s], fill=(40, 40, 40))
    d.polygon([(dx, dy - 28 * s), (dx - 16 * s, dy - 4 * s), (dx + 16 * s, dy - 4 * s)], fill=(40, 40, 40))
    d.line([(dx - 22 * s, dy - 22 * s), (dx + 22 * s, dy + 22 * s)], fill=RED, width=max(3, int(5 * s)))
    d.line([(dx - 22 * s, dy + 22 * s), (dx + 22 * s, dy - 22 * s)], fill=RED, width=max(3, int(5 * s)))


def icon_chart(d, cx, cy, s):
    # falling red arrow over bars
    bars = [(-52, 18), (-30, 30), (-8, 12), (14, 26), (36, 8)]
    for bx, bh in bars:
        d.rectangle([cx + bx * s, cy + 34 * s - bh * s, cx + (bx + 16) * s, cy + 34 * s], fill=(120, 120, 120))
    pts = [(cx - 58 * s, cy - 34 * s), (cx - 28 * s, cy - 18 * s), (cx - 2 * s, cy - 28 * s),
           (cx + 26 * s, cy - 6 * s), (cx + 56 * s, cy + 18 * s)]
    d.line(pts, fill=RED, width=max(3, int(5 * s)))
    d.polygon([(cx + 56 * s, cy + 18 * s), (cx + 34 * s, cy + 12 * s), (cx + 50 * s, cy + 34 * s)], fill=RED)


# ---------------- page ----------------

def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 24  # margin

    # --- masthead ---
    d.rectangle([0, 0, W, 92], fill=(26, 26, 30))
    f_title = font(SERIF_BLACK, 60)
    d.text((W // 2, 4), "THE WORLD", font=f_title, fill=(247, 243, 232), anchor="ma")
    f_date = font(SANS_BOLD, 19)
    d.text((W // 2, 66), "FRIDAY  -  20 NOVEMBER 2026", font=f_date, fill=(220, 180, 60), anchor="ma")
    d.line([(M, 92), (W - M, 92)], fill=RED, width=4)

    # --- tagline strip ---
    f_tag = font(SANS_BOLD, 14)
    d.text((W // 2, 98), "ONE DAY  -  EIGHT STORIES THAT DEFINED IT", font=f_tag, fill=GREY, anchor="ma")

    # --- lead card ---
    lx, ly, lw, lh = M, 122, W - 2 * M, 204
    d.rectangle([lx, ly, lx + lw, ly + lh], fill=CARD, outline=LINE, width=2)
    d.rectangle([lx, ly, lx + lw, ly + 6], fill=RED)
    icon_scales(d, lx + 92, ly + 108, 1.05, INK)
    tx = lx + 196
    tw = lx + lw - 18 - tx
    f_kick = font(SANS_BLACK, 17)
    d.text((tx, ly + 16), "THE HAGUE  -  WORLD COURT", font=f_kick, fill=RED)
    f_h, h_lines = fit_lines(d, "WORLD COURT FINDS MYANMAR GUILTY OF GENOCIDE",
                             SERIF_BLACK, 40, tw, 2)
    y = draw_text_lines(d, h_lines, f_h, tx, ly + 42, INK, int(f_h.size * 1.08))
    f_s, s_lines = fit_lines(d, "The ICJ ruled 9-6 that Myanmar committed genocide against the "
                             "Rohingya in its 2016-17 clearance operations - the first genocide "
                             "finding against a state. About 10,000 were killed and some 400 "
                             "villages destroyed. The court ordered reparations and the return "
                             "of the displaced.",
                             SANS, 17, tw, 3)
    draw_text_lines(d, s_lines, f_s, tx, y + 8, (50, 48, 44), int(f_s.size * 1.25))

    # --- story cards ---
    stories = [
        ("SHENZHEN  -  SUMMIT", "TRUMP, XI AND PUTIN SIGN PEACE PLEDGE",
         "First-ever three-way summit at Kylin Villa: the leaders declared a nuclear war "
         "'cannot be won and must never be fought'. No breakthrough on Ukraine, Iran, "
         "Taiwan or trade.", icon_flags, 0.72),
        ("KYIV  -  WAR", "RUSSIA HITS KYIV IN BIGGEST STRIKE OF THE YEAR",
         "110+ missiles and 400+ drones overnight; three Dnipro bridges hit, 8 killed, "
         "28 hurt. Hours after Putin left the Shenzhen summit.", icon_missile, 0.72),
        ("RIYADH  -  MIDDLE EAST", "HOUTHI MISSILE HITS RIYADH'S TALLEST TOWER",
         "The 80-storey PIF Tower, HQ of Saudi Arabia's wealth fund, took hits "
         "across 7-8 floors. No injuries; the district was closed.", icon_tower, 0.72),
        ("HORMUZ  -  TANKER ABLAZE", "TANKER ABLAZE AFTER STRIKE IN THE STRAIT",
         "A tanker caught fire after a projectile hit 8 miles off Oman's Khasab, UKMTO "
         "says. Iran claims mines hit two supertankers - unverified.", icon_tanker, 0.72),
        ("POLAND  -  NATO BREACH", "RUSSIAN MISSILES BREACH NATO AIRSPACE",
         "A Kh-101 cruise missile spent about 3 minutes over Poland before falling near "
         "Nowy Lipowiec. Jets scrambled; no shots fired. Tusk calls it a provocation.",
         icon_border, 0.72),
        ("ANTALYA  -  COP31", "COP31 DRAFT DROPS FOSSIL FUELS",
         "The Antalya draft strips all fossil-fuel phase-out language, swapping it for "
         "electrification and carbon capture. First COP to admit a 1.5C overshoot.",
         icon_climate, 0.72),
        ("MARKETS  -  STOCKS SLIDE", "NIKKEI DIVES AS STOCKS SLIDE AGAIN",
         "Nikkei -4.8%, Kospi -4.7%, S&P 500 -2%, Dow -2.19% to 49,097. SoftBank -16%. "
         "Anthropic +17% on its record $81B debut, then slid.", icon_chart, 0.72),
    ]

    rows = [
        (336, 196, [0, 1]),
        (542, 196, [2, 3, 4]),
        (748, 196, [5, 6]),
    ]
    G = 14
    for ry, rh, idxs in rows:
        n = len(idxs)
        cw = (W - 2 * M - G * (n - 1)) // n
        for i, si in enumerate(idxs):
            x = M + i * (cw + G)
            kicker, headline, summary, icon_fn, sc = stories[si]
            d.rectangle([x, ry, x + cw, ry + rh], fill=CARD, outline=LINE, width=2)
            d.rectangle([x, ry, x + cw, ry + 5], fill=RED)
            # icon band
            icon_fn(d, x + cw // 2, ry + 44, sc)
            d.line([(x + 14, ry + 84), (x + cw - 14, ry + 84)], fill=LINE, width=1)
            px, pw = x + 14, cw - 28
            f_k = font(SANS_BLACK, 13)
            d.text((px, ry + 92), kicker, font=f_k, fill=RED)
            f_h, h_lines = fit_lines(d, headline, SERIF_BLACK, 21, pw, 2)
            y = draw_text_lines(d, h_lines, f_h, px, ry + 110, INK, int(f_h.size * 1.05))
            f_s, s_lines = fit_lines(d, summary, SANS, 13, pw, 2)
            draw_text_lines(d, s_lines, f_s, px, y + 4, (50, 48, 44), int(f_s.size * 1.22))

    # --- footer ---
    d.line([(M, 954), (W - M, 954)], fill=INK, width=2)
    f_f = font(SANS_BOLD, 15)
    d.text((M, 962), "FRIDAY 20 NOVEMBER 2026", font=f_f, fill=INK)
    d.text((W - M, 962), "8 STORIES  -  THE WORLD IN ONE DAY", font=f_f, fill=INK, anchor="ra")

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
