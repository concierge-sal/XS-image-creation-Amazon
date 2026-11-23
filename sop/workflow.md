# Workflow — SKU to approved image set

1. **Collect inputs**: real product photos (front, back, side, macro), exact dimensions (mm), weight, chain length, metal, plating, stone type/colour/cut/size, closure, packaging, variants.
2. **Fill SKU sheet** (`references/sku-sheet-template.md`). Measurements must match the Amazon listing.
3. **Check source resolution** (`python3 tools/check_image.py source <original>`). Follow `sop/source-resolution.md`: AI upscale (Real-ESRGAN x4plus) at 1.25–3×, re-shoot above 3×.
4. **Pick tool per slot** (`sop/tool-selection.md`). Decide before generating.
5. **Build prompts** from `templates/prompt-template.md` + slot file + metal/gem/style blocks. Save final prompts to `prompts/sku/<SKU>.md` (create folder per SKU).
6. **Generate / design.** Always attach the real product photo as image reference when the tool supports it — the product must stay accurate.
7. **Fix product fidelity** in Photoshop/Canva if the AI altered the piece (engraving, letters, stone count, clasp). Replace with the real product cut-out if needed.
8. **QA** with `checklists/qa-checklist.md`. Main image: verify background is exactly #FFFFFF.
9. **Side-by-side consistency check** against `reference-sets/COS-JESUSNAMES/`.
10. **Sally approval.** Rename to `<SKU>_<slot>.jpg`, add approved set to `reference-sets/<SKU>/` if it becomes a new benchmark.
11. **Upload** to Seller Central; confirm no suppression after 24 h.
