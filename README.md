# X.S Collection — Amazon Image Creation System

Single source of truth for building SALLY SKOUFIS™ X.S Collection Amazon listing images.
Every prompt is assembled from the reference files here, so every SKU's image set stays **in the same line** as the approved COS-JESUSNAMES set — and **strictly Amazon-compliant**.

The system is **tool-agnostic**: prompts work in any AI image tool (Higgsfield, Gemini, Midjourney, Firefly, etc.) or as a brief for manual builds in Canva/Photoshop. Pick the tool per slot before generating (see `sop/tool-selection.md`).

## Structure

```
README.md                      ← you are here
sop/
  amazon-image-policy.md       ← Amazon rules (HARD — overrides everything)
  slot-structure.md            ← what goes in Main, Slots 2–9, EBC/A+
  workflow.md                  ← step-by-step from SKU → approved set
  tool-selection.md            ← choosing AI vs Canva/manual per slot
references/
  xs-collection.md             ← X.S range, Amazon finish names, launch facts, data issues
  xs-catalogue.csv             ← every X.S SKU: finish, size, weight, material, price, Myer
  metals.md                    ← metal finishes + exact prompt wording
  gems.md                      ← stones/crystals + exact prompt wording
  brand-style.md               ← the "same line" look: light, colour, type, props
  sku-sheet-template.md        ← fill one per SKU before prompting
templates/
  prompt-template.md           ← master prompt skeleton + negative prompt
prompts/
  main-image.md, slot-2 … slot-9, ebc-aplus.md
checklists/
  qa-checklist.md              ← pass/fail before upload
reference-sets/
  xs-capsule-48/                ← the 48 Amazon/TikTok capsule products: Shopify info + image links per product
  brand-info/                   ← brand panels (mood only; no press logos on Amazon)
  xs-models/                    ← the ONLY approved models
  COS-JESUSNAMES/              ← approved benchmark set (Main, Slots 2–9, EBC)
```

## How to write a prompt (quick)
1. Fill `references/sku-sheet-template.md` for the SKU.
2. Open the slot file in `prompts/`.
3. Paste the metal block from `references/metals.md` and gem block from `references/gems.md`.
4. Add the style block from `references/brand-style.md`.
5. Append the Amazon negative block from `templates/prompt-template.md`.
6. Check source resolution (`sop/source-resolution.md`, `tools/check_image.py`) → generate → run `checklists/qa-checklist.md` → compare side-by-side with `reference-sets/COS-JESUSNAMES/`.

**Rule of priority:** Amazon policy > product accuracy > brand consistency > creativity.
