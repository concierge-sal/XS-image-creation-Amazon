# AMAZON/TIK TOK — Initial X.S Capsule Release (48 products)

Source: Shopify collection `amazon-x-s-capsule` (48 products, all DRAFT), pulled 23 Nov 2026.

- **`index.csv`**: one row per product: handle, product, Shopify finish, **Amazon finish name**, SKU(s), price AUD, size, weight, number of images, main reference link, warnings.
- **`<handle>.md`**: one file per product: facts, allowed claims, every Shopify image link, and which image to attach as the product reference.

## How to attach references in ChatGPT
The image files are on Shopify's CDN (public links). This workspace cannot download them, so the links are stored here.
1. Open the link from the product's `.md` file and save the image.
2. In ChatGPT, attach the saved **file** (paperclip). A pasted link is not loaded as an image reference.
3. Always attach image #1 (the pack shot) as the product reference. Add the gold, silver or black metal reference for the colour.
4. Use the prompt structure in `prompts/sku/9363472000109_chatgpt.md` (swap in the product's name, size and finish from its `.md` file).

## ⚠ Check before use (23 products flagged)
- **Wrong-product filenames:** several products' first image is named after another product, e.g. all XSavage entries use `SS-XStyleEarrings…` / `SS-XStyleGrande…`, XSolid Ear Cuff uses `…XSTYLE-GRANDE-EARCUFF…`, XSculpt Ear Cuff uses `SS-XSenseEarCuff…`. Open each one and confirm it really shows the listed product before attaching it.
- **"Vermeil" filenames:** some gold images are named "Gold Vermeil" while the product is "Gold Plated Brass". Check the colour matches, and never write "vermeil" on images.
- Every description includes "Hypoallergenic", "Sustainably Sourced & Developed" and "Fine Artisanal Craftsmanship". None of these may appear on Amazon images or listings.
