# Amazon Image Policy — HARD RULES

If anything in a prompt, template or generated image conflicts with this file, **remove it**. No exceptions.
(Amazon updates rules — re-check Seller Central "Product image requirements" + the Jewellery category style guide each quarter.)

## All images
- Format: JPEG (preferred), PNG, TIFF, or non-animated GIF. sRGB colour.
- Size: min **1000 px** on the longest side (enables zoom); target **2000 × 2000 px** square (1:1). Max 10,000 px.
- Must show the **actual product being sold** — accurate colour, metal, stone, size, finish. No AI "beautifying" that changes the product.
- No: Amazon logos/trademarks or anything resembling them (incl. "Amazon's Choice", "Best Seller", "Prime" badges).
- No: watermarks, borders, placeholder text, blurry/pixelated/jagged images.
- No: nudity or sexually suggestive imagery. Models must be fully appropriate.
- No: other brands' logos or products in frame.
- No: unsupported claims — "#1", "best", "guaranteed", "hypoallergenic" (unless certified & documented), "solid gold" (unless it is), "waterproof", medical/healing claims, "lifetime", competitor comparisons, price, discounts, "free shipping", "sale".
- No: contact details, URLs, QR codes, social handles.
- Religious/name pieces (e.g. Jesus names): respectful presentation only; no claims of spiritual/protective effects.

## Aspect ratio — STRICT 1:1 (every listing image)
- **Main and Slots 2–9 are exactly square: 2000 × 2000 px.** No portrait (3:4, 4:5), no landscape, no "near-square".
- Build on a square canvas from the start: generate at 1:1, set Canva to 2000×2000. Never crop a portrait or landscape result down to square afterwards (it cuts the product or the text).
- Square sources: if the source is not square, extend the background (pure #FFFFFF on Main) to square. Never stretch or squash the product.
- Exception only where Amazon fixes the size: A+/EBC modules use Amazon's module dimensions (see A+ / EBC below).
- `tools/check_image.py` fails any listing image that is not exactly 2000×2000.

## MAIN image (strictest)
- **Pure white background RGB 255,255,255.** No gradient, no off-white, no shadows that read grey patches (soft natural contact shadow only).
- Product fills **≥ 85%** of the frame.
- **Product only**: no text, no logos, no graphics, no badges, no colour swatches, no inset images, no props, no packaging (unless sold), no gift box unless included.
- **Jewellery: no model / mannequin / bust / hand** on the main image.
- Show the full product, not cropped, in focus, professionally lit. One unit only (unless a set is sold).
- No multiple views of the same item.

## Secondary images (Slots 2–9)
- Lifestyle, on-model, scale, detail, infographic text allowed.
- Text must be factual, legible on mobile, and match the listing attributes exactly.
- Props must not be confused as included. If not included, keep them clearly secondary or state "not included" isn't needed — just don't make them look sold.
- Models: adult, appropriate, product clearly the hero.
- Size/scale images must be **accurate** — dimensions match the listing.

## A+ / EBC
- Module dimensions per A+ spec (e.g. Standard Image Header 970 × 600; Image & Text 300 × 300 / 220 × 220; Comparison 150 × 300). Confirm in Seller Central before export.
- No pricing, promotions, time-sensitive language, shipping info, warranty/guarantee claims, competitor references, customer reviews/quotes, or external links.
- Text in images must also be readable and not the only place for critical info (add alt text).

## Exclusion protocol
When a reference (incl. COS-JESUSNAMES) contains something non-compliant, **do not replicate it** — note it in the SKU sheet under "Excluded for policy" and carry on.
