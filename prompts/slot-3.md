# Slot 3 — On-Model

**Benchmark:** `reference-sets/COS-JESUSNAMES/slot 3 approved.jpg` — open it next to your draft.

## SLOT_BLOCK
```
worn by an adult female model, cropped to {neckline/ear/wrist/hand}, natural skin, neutral top, product in sharp focus as the hero, soft daylight
```

## Full prompt
```
[SUBJECT] {PRODUCT_TYPE}: {PRODUCT_DESCRIPTION}
[METAL] {METAL_BLOCK}
[GEMS] {GEM_BLOCK}
[SLOT] worn by an adult female model, cropped to {neckline/ear/wrist/hand}, natural skin, neutral top, product in sharp focus as the hero, soft daylight
[STYLE] {STYLE_BLOCK}
[FIDELITY] reproduce the reference product exactly; do not redesign
[OUTPUT] 1:1, 2000x2000 px, photorealistic
[NEGATIVE] Amazon negative block from templates/prompt-template.md
```

## Slot rules
- No suggestive pose or styling
- Product scale on body must be realistic
- Run `checklists/qa-checklist.md` before approval.
