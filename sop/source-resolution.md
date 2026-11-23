# Source Resolution & Upscaling — HARD RULE

**Problem:** cropping to 85% fill fixes the layout, not the pixels. When a product is small in the source file, enlarging it to fill a 2000×2000 MAIN tears edges and hides pavé, facets and maker's marks.
Seen on the **Edge** ear cuff (bands ~379×382 px → 4.4× upscale) and the **Destiny** climbers (~460×1212 px). A plain resize came out blurry with torn edges. Rebuilding from the original with **Real-ESRGAN x4plus** made them sharp. That detail is *rebuilt* by AI, not native high-res.

## Step 1 — Measure before you build
```
python3 tools/check_image.py source <original_file>
```
Product needs **1700 px on its longest side** (85% of 2000). Scale factor = 1700 ÷ product's longest side in the source.

| Scale needed | Action |
|---|---|
| ≤ 1.25× | High-quality resize (Lanczos / Photoshop "Preserve Details 2.0"), then light unsharp mask (radius ~1.5, 60–70%, threshold 2) |
| 1.25–2× | **AI upscale first:** Real-ESRGAN x4plus (Upscayl desktop app or `realesrgan-ncnn-vulkan -n realesrgan-x4plus`), or Photoshop Super Resolution. Then downsize to fit. Never enlarge with a plain resize. |
| 2–3× | AI upscale required **and** a re-shoot is strongly preferred. Flag the SKU sheet: "AI-rebuilt detail". |
| > 3× | **Re-shoot at high resolution.** AI upscale only as a labelled interim (e.g. Edge 4.4×), replaced once the re-shoot arrives. |

Always upscale from the **original file**, never from an already-resized or compressed copy (JPEG artefacts get upscaled too). For transparent PNGs, flatten onto #FFFFFF using the alpha channel first: hidden pixels under the transparency can be non-white.

## Step 2 — AI-rebuilt detail must match the real piece
Real-ESRGAN invents texture. At 100% zoom, compare against the original:
- Pavé stone **count and positions** identical; no merged, doubled or missing stones.
- Facets are crisp but not "plastic" or over-sharpened; no halo outlines.
- Maker's mark, hinge, clasp and engraving are legible and the correct shape.
- Metal colour unchanged: no orange or green shift.
If any of these fail, the image is not usable. Re-shoot.

## Step 3 — Sharpness check at full size (every final image)
```
python3 tools/check_image.py main  <final_MAIN.jpg> <original_source>
python3 tools/check_image.py sharp <final_slot.jpg>
```
- The script writes 100% crops to `qa_crops/`. Open them at **100% zoom**; never judge on a scaled-down preview.
- With the source given, the final must keep **≥ 0.8×** the source's sharpness score. Polished metal scores low in absolute terms, so judge it relative to the source.
- Without a source, absolute guide: < 60 fail, 60–150 inspect by eye, ≥ 150 pass.

## Step 4 — Detail visibility is a slot, not a hope
Even a sharp MAIN shows pavé at roughly real size on a phone. Every SKU with stones, facets, texture or a maker's mark gets **Slot 2 = dedicated macro close-up** (see `prompts/slot-2.md`), where the detail fills a large part of the frame. Generate or shoot it from a high-res source. Never enlarge a crop of the MAIN for this slot.

## Generation settings (any AI tool)
- Generate at native ≥ 2048 px if the tool allows; otherwise upscale with Real-ESRGAN before adding text.
- Add text in Canva **after** upscaling: upscalers smear type.
- Export JPEG quality ≥ 92, 4:4:4 (no chroma subsampling) to keep metal edges clean.
