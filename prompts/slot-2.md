# Slot 2 — Detail / Close-up

**Benchmark:** `reference-sets/COS-JESUSNAMES/Slot 2 approved.jpg` — open it next to your draft.

## SLOT_BLOCK
```
macro close-up at 3/4 angle showing metal finish, stone setting and craftsmanship, white or light gray (#F2F2F2) backdrop, shallow depth of field
```

## Full prompt
```
[SUBJECT] {PRODUCT_TYPE}: {PRODUCT_DESCRIPTION}
[METAL] {METAL_BLOCK}
[GEMS] {GEM_BLOCK}
[SLOT] macro close-up at 3/4 angle showing metal finish, stone setting and craftsmanship, white or light gray (#F2F2F2) backdrop, shallow depth of field
[STYLE] {STYLE_BLOCK}
[FIDELITY] reproduce the reference product exactly; do not redesign
[OUTPUT] 1:1, 2000x2000 px, photorealistic
[NEGATIVE] Amazon negative block from templates/prompt-template.md
```

## Detail visibility (mandatory)
- The purpose of this slot is that pavé stones, facets, hinge and maker's mark are clearly visible on a phone. The detail area fills ≥ 50% of the frame.
- Source must be a high-res macro photo or a native ≥2048 px generation. Never enlarge a crop of the MAIN.
- Add `ultra-sharp macro detail, every pavé stone individually defined, crisp facet edges, legible maker's mark` to the prompt.
- Upscale (Real-ESRGAN x4plus) BEFORE adding text, then run `tools/check_image.py sharp` and inspect at 100%.

## Slot rules
- Optional 2–3 factual callouts added in Canva (e.g. metal, stone)
- Lettering/engraving must be the real product
- Run `checklists/qa-checklist.md` before approval.
