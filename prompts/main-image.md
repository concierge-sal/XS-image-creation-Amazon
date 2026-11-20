# Main Image

**Benchmark:** `reference-sets/COS-JESUSNAMES/main image approved.jpg` — open it next to your draft.

## SLOT_BLOCK
```
product only, centred, front-facing hero angle, filling 85-90% of frame, chain arranged neatly in a soft symmetrical curve, pure white background RGB 255,255,255, soft natural contact shadow only, even studio lighting
```

## Full prompt
```
[SUBJECT] {PRODUCT_TYPE}: {PRODUCT_DESCRIPTION}
[METAL] {METAL_BLOCK}
[GEMS] {GEM_BLOCK}
[SLOT] product only, centred, front-facing hero angle, filling 85-90% of frame, chain arranged neatly in a soft symmetrical curve, pure white background RGB 255,255,255, soft natural contact shadow only, even studio lighting
[STYLE] {STYLE_BLOCK}
[FIDELITY] reproduce the reference product exactly; do not redesign
[OUTPUT] 1:1, 2000x2000 px, photorealistic
[NEGATIVE] Amazon negative block from templates/prompt-template.md
```

## Slot rules
- Background exactly #FFFFFF (check with eyedropper)
- No text, logo, props, model, hand, bust, packaging
- Product ≥85% of frame, uncropped
- Best built from real product cut-out, not AI
- Run `checklists/qa-checklist.md` before approval.
