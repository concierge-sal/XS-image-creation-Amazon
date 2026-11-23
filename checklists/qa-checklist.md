# QA Checklist — every image must pass every line

## Aspect ratio — STRICT 1:1
- [ ] Image is exactly 2000 × 2000 px (Main and Slots 2–9); `tools/check_image.py` shows "1:1 OK"
- [ ] Built square from the start (1:1 generation / 2000×2000 Canva canvas). Not cropped down from portrait or landscape
- [ ] Product not stretched or squashed; text and product inside the 5% safe margin of the square

## Font colours — STRICT
- [ ] Every piece of text is black #1C1C1C/#000000, white #FFFFFF, gray #3A3A3A or X.S red #560C0D. Nothing else
- [ ] No gold, tan, cream or brown text, lines, rules or icons
- [ ] Red used only for small labels and numbers on white/light gray; white on red/black; gray never on dark
- [ ] Fonts = Jost (+ Bodoni Moda Italic accent only), nothing else

## Models — X.S only
- [ ] Any person in the image is an approved X.S model from `reference-sets/xs-models/` (same face, recognisably model 01)
- [ ] AI generations used the X.S model photo as the identity reference; no invented or stock faces
- [ ] Other jewellery in shot is X.S product only; the listed product is clearly the hero
- [ ] Red background colour-matched to #560C0D

## Amazon compliance
- [ ] ≥1000 px longest side (target 2000×2000), JPEG, sRGB
- [ ] No Amazon logos/badges, watermarks, borders, URLs, QR codes, handles
- [ ] No price, promo, "sale", "best", "#1", guarantees, unverified "hypoallergenic/waterproof/solid gold", healing/spiritual claims
- [ ] No other brands or competitor references
- [ ] No nudity / suggestive content
- [ ] MAIN: pure #FFFFFF, ≥85% fill, product only, no model/hand/bust/props/text

## Resolution & sharpness (see sop/source-resolution.md)
- [ ] Ran `tools/check_image.py source` on the ORIGINAL: scale factor recorded on the SKU sheet
- [ ] ≤1.25×: Lanczos + light unsharp mask · 1.25–3×: Real-ESRGAN x4plus / Super Resolution · >3×: re-shoot (AI upscale only as a labelled interim)
- [ ] Upscaled from the original file, not a resized/compressed copy; transparent PNGs flattened onto #FFFFFF via the alpha channel
- [ ] `tools/check_image.py main` PASS: sharpness ≥ 0.8× source
- [ ] Every image inspected at 100% zoom (qa_crops/): no torn or jagged edges, no halos, no smearing
- [ ] AI-upscaled detail matches the real piece: pavé count and positions, facets, maker's mark, hinge and clasp identical; no invented texture
- [ ] Detail slot (Slot 2) actually shows the pavé / facets / mark large and crisp, from a high-res source (never an enlarged crop of the MAIN)
- [ ] Text added AFTER upscaling; JPEG ≥ 92 quality, 4:4:4

## Product accuracy
- [ ] Metal colour & finish match real product
- [ ] Stone count, cut, colour, setting match
- [ ] Lettering/engraving exactly correct
- [ ] Chain, clasp, proportions not distorted
- [ ] Dimensions shown = listing dimensions

## Same-line consistency (vs COS-JESUSNAMES)
- [ ] Fonts = Jost (+ Bodoni Moda Italic accent only), nothing else
- [ ] Colours = black, white, gray, brand red only (plus true product colours)
- [ ] Same text position, margins
- [ ] Same lighting direction & warmth
- [ ] Same icon style
- [ ] Slot order and purpose match `sop/slot-structure.md`

## Text
- [ ] Spelling checked; readable on mobile
- [ ] Every claim matches listing attributes

Sign-off: ______  Date: ______
