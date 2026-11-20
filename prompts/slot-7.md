# Slot 7 — Variants / Styling

**Benchmark:** `reference-sets/COS-JESUSNAMES/slot 7 approved.jpg` — open it next to your draft.

## SLOT_BLOCK
```
variants arranged in a neat row or grid on neutral background, identical lighting and angle for each
```

## Full prompt
```
[SUBJECT] {PRODUCT_TYPE}: {PRODUCT_DESCRIPTION}
[METAL] {METAL_BLOCK}
[GEMS] {GEM_BLOCK}
[SLOT] variants arranged in a neat row or grid on neutral background, identical lighting and angle for each
[STYLE] {STYLE_BLOCK}
[FIDELITY] reproduce the reference product exactly; do not redesign
[OUTPUT] 1:1, 2000x2000 px, photorealistic
[NEGATIVE] Amazon negative block from templates/prompt-template.md
```

## Slot rules
- Show only variants actually offered; label each in Canva
- If no variants: second on-model angle
- Run `checklists/qa-checklist.md` before approval.
