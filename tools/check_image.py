#!/usr/bin/env python3
"""Amazon image pre-flight: source scale factor, MAIN background/fill, and sharpness at full size.

Usage:
  python3 tools/check_image.py source  <source_file>                 # how much upscale will MAIN need?
  python3 tools/check_image.py main    <final_2000x2000.jpg> [source] # MAIN compliance + sharpness
  python3 tools/check_image.py sharp   <any_final_image>               # 1:1 check + sharpness + 100% crops
  python3 tools/check_image.py square  <image>                         # strict 1:1 2000x2000 check only

Writes 100%-size crops to ./qa_crops/<name>_crop*.png. Open them and inspect at 100% zoom (never judge
sharpness on a scaled-down preview). Needs: numpy, Pillow (opencv optional).
"""
import sys, os
import numpy as np
from PIL import Image

TARGET = 2000          # Amazon MAIN canvas
FILL = 0.85            # min product fill (longest side)
NEED = int(TARGET * FILL)  # 1700 px product on longest side

def product_bbox(im):
    if im.mode in ("RGBA", "LA") or "transparency" in im.info:
        a = np.array(im.convert("RGBA"))[:, :, 3]
        ys, xs = np.where(a > 8)
    else:
        g = np.array(im.convert("L"))
        ys, xs = np.where(g < 246)
    if len(xs) == 0:
        return None
    return xs.min(), ys.min(), xs.max() + 1, ys.max() + 1

def flatten(im):
    if im.mode in ("RGBA", "LA") or "transparency" in im.info:
        im = im.convert("RGBA")
        bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
        return Image.alpha_composite(bg, im).convert("RGB")
    return im.convert("RGB")

def laplacian_var(gray):
    g = gray.astype(np.float32)
    lap = (-4 * g[1:-1, 1:-1] + g[:-2, 1:-1] + g[2:, 1:-1] + g[1:-1, :-2] + g[1:-1, 2:])
    return float(lap.var())

def edge_sharpness(img, box):
    """Laplacian variance on the product region only (higher = sharper)."""
    g = np.array(img.convert("L").crop(box))
    return laplacian_var(g)

def scale_verdict(f):
    if f <= 1.25:
        return "OK - plain high-quality resize (Lanczos) is fine"
    if f <= 2.0:
        return "UPSCALE - use AI upscale (Real-ESRGAN x4plus / Photoshop Super Resolution), then downsize to fit"
    if f <= 3.0:
        return "HIGH RISK - AI upscale required; re-shoot strongly preferred; detail is rebuilt, not native"
    return "RE-SHOOT - source too small (> 3x). AI upscale only as a labelled interim; re-shoot at high res"

def cmd_source(path):
    im = Image.open(path)
    b = product_bbox(im)
    pw, ph = b[2] - b[0], b[3] - b[1]
    f = NEED / max(pw, ph)
    print(f"{os.path.basename(path)}: file {im.size[0]}x{im.size[1]}, product {pw}x{ph} px")
    print(f"  scale needed for 85% MAIN fill: {f:.2f}x  ->  {scale_verdict(f)}")
    return f

def crops(img, box, name, n=3):
    os.makedirs("qa_crops", exist_ok=True)
    x0, y0, x1, y1 = box
    w = h = 400
    pts = [((x0 + x1) // 2, (y0 + y1) // 2), (x0 + (x1 - x0) // 4, y0 + (y1 - y0) // 4), (x1 - (x1 - x0) // 4, y0 + (y1 - y0) // 3)]
    for i, (cx, cy) in enumerate(pts[:n], 1):
        c = img.crop((cx - w // 2, cy - h // 2, cx + w // 2, cy + h // 2))
        p = f"qa_crops/{name}_crop{i}.png"
        c.save(p)
        print(f"  100% crop -> {p}")

def check_square(im, name):
    w, h = im.size
    if (w, h) == (TARGET, TARGET):
        print(f"  1:1 OK ({w}x{h})"); return True
    print(f"  FAIL 1:1 rule: {w}x{h}, must be exactly {TARGET}x{TARGET} (strict square)"); return False

def cmd_sharp(path, quiet=False, final=True):
    im = Image.open(path)
    if final:
        check_square(im, path)
    rgb = flatten(im)
    b = product_bbox(im) or (0, 0, *rgb.size)
    s = edge_sharpness(rgb, b)
    verdict = "SHARP" if s >= 150 else ("CHECK - soft" if s >= 60 else "FAIL - blurry")
    print(f"{os.path.basename(path)}: sharpness (Laplacian var on product) = {s:.0f}  ->  {verdict}")
    print("  Thresholds are a guide: <60 fail, 60-150 inspect, >=150 pass. Always confirm by eye at 100%.")
    crops(rgb, b, os.path.splitext(os.path.basename(path))[0])
    return s

def cmd_main(path, source=None):
    im = Image.open(path)
    rgb = flatten(im)
    ok = True
    ok &= check_square(rgb, path)
    a = np.array(rgb)
    border = np.concatenate([a[:5].reshape(-1, 3), a[-5:].reshape(-1, 3), a[:, :5].reshape(-1, 3), a[:, -5:].reshape(-1, 3)])
    nonwhite = (border != 255).any(axis=1).mean()
    print(f"  border pixels not pure #FFFFFF: {nonwhite*100:.2f}%  ->  {'OK' if nonwhite == 0 else 'FAIL'}")
    ok &= nonwhite == 0
    g = np.array(rgb.convert("L"))
    ys, xs = np.where(g < 250)
    fill = max(xs.max() - xs.min(), ys.max() - ys.min()) / TARGET
    print(f"  product fill (longest side): {fill*100:.0f}%  ->  {'OK' if fill >= FILL else 'FAIL'}")
    ok &= fill >= FILL
    s = cmd_sharp(path, final=False)
    if source:
        # Polished metal has few edges, so absolute scores run low even when sharp.
        # When the source is given, judge the final against the source instead.
        f = cmd_source(source)
        src = Image.open(source)
        s0 = edge_sharpness(flatten(src), product_bbox(src))
        ratio = s / s0 if s0 else 0
        print(f"  sharpness vs source: {s:.0f} / {s0:.0f} = {ratio:.2f}  ->  {'OK' if ratio >= 0.8 else 'FAIL - softer than source: AI-upscale or re-shoot'}")
        ok &= ratio >= 0.8
        if f > 1.25:
            print("  NOTE: source needed >1.25x. If AI-upscaled, compare stones/facets/marks against the original at 100%: no invented or missing detail.")
    else:
        ok &= s >= 60
    print("RESULT:", "PASS (confirm crops by eye)" if ok else "FAIL")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    mode, path = sys.argv[1], sys.argv[2]
    {"source": lambda: cmd_source(path),
     "sharp": lambda: cmd_sharp(path),
     "square": lambda: sys.exit(0 if check_square(Image.open(path), path) else 1),
     "main": lambda: cmd_main(path, sys.argv[3] if len(sys.argv) > 3 else None)}[mode]()
