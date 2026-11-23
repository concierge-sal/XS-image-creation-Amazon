# Slot 3 — On-Model

**Benchmark:** `reference-sets/COS-JESUSNAMES/slot 3 approved.jpg` — open it next to your draft.

## SLOT_BLOCK
```
worn by an adult female model, cropped to {neckline/ear/wrist/hand}, natural skin, black or white top, product in sharp focus as the hero, soft studio light, solid brand-red background
```

## Full prompt
```
[SUBJECT] {PRODUCT_TYPE}: {PRODUCT_DESCRIPTION}
[METAL] {METAL_BLOCK}
[GEMS] {GEM_BLOCK}
[SLOT] worn by an adult female model, cropped to {neckline/ear/wrist/hand}, natural skin, black or white top, product in sharp focus as the hero, soft studio light, solid brand-red background
[STYLE] {STYLE_BLOCK}
[FIDELITY] reproduce the reference product exactly; do not redesign
[OUTPUT] 1:1, 2000x2000 px, photorealistic
[NEGATIVE] Amazon negative block from templates/prompt-template.md
```

## Model rule (mandatory)
Use ONLY the X.S model (`reference-sets/xs-models/`). Prefer editing a real X.S model photo (fit the product on her ear). For generation, attach the model photo as the identity reference and add: `the same woman as the reference model image (identical face, freckles, blonde hair, skin tone); do not change her identity`.

## Slot rules
- No suggestive pose or styling
- Product scale on body must be realistic
- Run `checklists/qa-checklist.md` before approval.
