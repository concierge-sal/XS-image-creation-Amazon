#!/usr/bin/env python3
"""Build Slot 2 (detail close-up) for XSculpt Grande Huggie 18K Gold (SKU 9363472000109)
from the studio file Sandy_2902.jpg. Works with any size of that same shot (2576 or 4000 px):
all positions are relative to the image width.

No pixel is enlarged more than MAX_SCALE (1.25x) from the source, per sop/source-resolution.md.
Text is NOT added here (brand fonts live in Canva); see prompts/sku/9363472000109.md for the copy.

Usage: python3 tools/build_slot2_xsculpt.py <Sandy_2902.jpg> <out.jpg>
"""
import sys
from PIL import Image, ImageDraw, ImageFilter

MAX_SCALE = 1.25
INK = (28, 28, 28)        # #1C1C1C
W = 2000

src = Image.open(sys.argv[1]).convert("RGB")
k = src.width / 2576.0    # coordinates below were measured on the 2576 px copy

def box(x0, y0, x1, y1):
    return tuple(int(v * k) for v in (x0, y0, x1, y1))

canvas = Image.new("RGB", (W, W), (255, 255, 255))
d = ImageDraw.Draw(canvas)

# 1) Hero: the front-facing (left) earring, reflection excluded.
hero_src = box(470, 660, 1250, 1545)
hero = src.crop(hero_src)
target_h = 700   # hero kept small so insets read as ~1.6x closer
s = min(target_h / hero.height, MAX_SCALE)
hero = hero.resize((round(hero.width * s), round(hero.height * s)), Image.LANCZOS)
hx, hy = 150, 700
canvas.paste(hero, (hx, hy))

def to_canvas(px, py):
    """Map a point measured on the 2576 copy into the hero on the canvas."""
    return hx + (px * k - hero_src[0]) * s, hy + (py * k - hero_src[1]) * s

# 2) Two round insets cropped from the source at <= MAX_SCALE.
D = 800
insets = [  # (centre on 2576 copy, inset centre on canvas, hero anchor on 2576 copy)
    ((1062, 835), (1470, 560), (1075, 890)),    # hinge + maker's mark
    ((1010, 1215), (1470, 1440), (1090, 1215)), # textured inner wall
]
for (cx, cy), (ox, oy), (ax, ay) in insets:
    half = D / MAX_SCALE / 2 * k
    crop = src.crop((int(cx * k - half), int(cy * k - half), int(cx * k + half), int(cy * k + half)))
    crop = crop.resize((D, D), Image.LANCZOS)
    mask = Image.new("L", (D * 4, D * 4), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, D * 4 - 1, D * 4 - 1), fill=255)
    mask = mask.resize((D, D), Image.LANCZOS)
    canvas.paste(crop, (ox - D // 2, oy - D // 2), mask)
    d.ellipse((ox - D // 2, oy - D // 2, ox + D // 2, oy + D // 2), outline=INK, width=3)
    # leader line from the hero detail to the inset edge
    x0, y0 = to_canvas(ax, ay)
    x1, y1 = ox - D // 2, oy
    d.line((x0, y0, x1, y1), fill=INK, width=3)
    d.ellipse((x0 - 9, y0 - 9, x0 + 9, y0 + 9), fill=(255, 255, 255), outline=INK, width=3)

canvas = canvas.filter(ImageFilter.UnsharpMask(radius=1.2, percent=50, threshold=2))
canvas.save(sys.argv[2], quality=95, subsampling=0)
print(f"hero scale {s:.2f}x, inset scale {MAX_SCALE:.2f}x (source width {src.width})")
