# Workflow — SKU to approved image set

1. **Collect inputs**: real product photos (front, back, side, macro), exact dimensions (mm), weight, chain length, metal, plating, stone type/colour/cut/size, closure, packaging, variants.
2. **Fill SKU sheet** (`references/sku-sheet-template.md`). Measurements must match the Amazon listing.
3. **Pick tool per slot** (`sop/tool-selection.md`). Decide before generating.
4. **Build prompts** from `templates/prompt-template.md` + slot file + metal/gem/style blocks. Save final prompts to `prompts/sku/<SKU>.md` (create folder per SKU).
5. **Generate / design.** Always attach the real product photo as image reference when the tool supports it — the product must stay accurate.
6. **Fix product fidelity** in Photoshop/Canva if the AI altered the piece (engraving, letters, stone count, clasp). Replace with the real product cut-out if needed.
7. **QA** with `checklists/qa-checklist.md`. Main image: verify background is exactly #FFFFFF.
8. **Side-by-side consistency check** against `reference-sets/COS-JESUSNAMES/`.
9. **Sally approval.** Rename to `<SKU>_<slot>.jpg`, add approved set to `reference-sets/<SKU>/` if it becomes a new benchmark.
10. **Upload** to Seller Central; confirm no suppression after 24 h.
