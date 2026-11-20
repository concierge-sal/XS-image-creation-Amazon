# EBC / A+ Content

**Benchmark:** `reference-sets/COS-JESUSNAMES/EBC.jpg` — open it next to your draft.

## SLOT_BLOCK
```
wide banner composition at A+ module ratio (e.g. 970x600), product + lifestyle, generous negative space for headline
```

## Full prompt
```
[SUBJECT] {PRODUCT_TYPE}: {PRODUCT_DESCRIPTION}
[METAL] {METAL_BLOCK}
[GEMS] {GEM_BLOCK}
[SLOT] wide banner composition at A+ module ratio (e.g. 970x600), product + lifestyle, generous negative space for headline
[STYLE] {STYLE_BLOCK}
[FIDELITY] reproduce the reference product exactly; do not redesign
[OUTPUT] 1:1, 2000x2000 px, photorealistic
[NEGATIVE] Amazon negative block from templates/prompt-template.md
```

## Slot rules
- Confirm module sizes in Seller Central
- No pricing, promo, shipping, warranty, competitor or review content
- Add alt text per module
- Run `checklists/qa-checklist.md` before approval.
