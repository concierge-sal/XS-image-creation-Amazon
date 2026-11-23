# X.S Collection — reference

**XS by SALLY SKOUFIS™**. Full product data (SKU, finish, size, weight, material, price, Myer flag): `references/xs-catalogue.csv`.
Source: Shopify Admin, pulled 23 Nov 2026. All X.S products are **DRAFT** in Shopify. Re-pull before launch if anything changes.

## Launch
- **Amazon AU** is the priority, then **TikTok Shop US**, late 2026.
- Amazon AU listings are **fulfilled by merchant (FBM)**, not FBA.
- Creatives are kept in the Drive folder **"XS_Amazon_Creatives"**. Studio originals live in each product's Drive folder (e.g. "X.Sculpt Huggie Grande Earrings - SUE24C027 - 7 x 20mm").
- Image style must match the approved COS-JESUSNAMES set. Brand rules: `references/brand-style.md`.

## Amazon finish names (use on Amazon, not the Shopify names)
| Shopify variant name | Amazon name |
|---|---|
| 18K Gold Plated Brass / 18K Gold Vermeil / Premium Gold Plated | **Gold Toned** (titles, highlights, bullets, description: everywhere) |
| Premium Silver Rhodium / Silver Plated Brass / Silver Rhodium Plate | **Silver Rhodium** |
| Premium Black Rhodium / Black Plated Brass / Black Rhodium Plate | **Black Rhodium** |

- Avoid the word "plated" in Amazon names.
- Keep **brass** out of the Item Highlights; disclose it in the bullets and description.
- Image text must use the same names as the listing. Put "Gold Toned" on images, not "18K Gold Plated". ⚠ The XSculpt Grande Huggie prompt sheet still says "18K Gold Plated" and must be switched to "Gold Toned".

## Claims: never on Amazon images or listing text (unless documented)
Every Shopify X.S description includes **"Hypoallergenic"**, **"Sustainably Sourced & Developed"** and **"Fine Artisanal Craftsmanship"**. All three are excluded (see `sop/amazon-image-policy.md`). Allowed facts: material, finish, size, weight, closure type, what's in the box.

## The range (72 products, 218 finish variants)
| Family | Products (size from Shopify) |
|---|---|
| **XSavage** | Earrings 4×25mm (11.2g) · Grande 4×30mm (13.58g) · Ring 4mm fascia |
| **XSculpt** | Petite Huggie 4.5×12mm · Huggie 5.5×15mm · Grande Huggie 7×20mm (10.58g) · Ear Cuff 3×10mm · Ring 4.7mm · Grande Ring 7mm |
| **XSense** | Earrings 3×20mm oval · Grande 3×24mm oval · Petite 3×15mm · Huggie 3×11mm · Petite Huggie 1.5×10mm · Ear Cuffs (Single 6×11 / 7×12, Double 4×12, Tri 6×12, Quad 10×12mm) |
| **XSharp** | Earrings 4×29mm drop · Fine 3×22mm · Huggie 2×11mm · Bold Huggie 3×11mm · Ear Cuffs (4×10, Bold 5×11, Fine 2×10, Trio 9×12mm) |
| **XSlick** | Earrings 3×30mm · Oval 16×22mm · Huggie 1.2×12mm · Petite Huggie 1.2×9mm · Petite Hoop 1.3×15mm · Grande Hoop 1.3×23mm · Ear Cuff 5×11mm |
| **XSlim** | Ear Cuff 2×11mm |
| **XSmoke** | Earrings 2×20mm · Grande 45mm |
| **XSolid** | Petite 3×14mm · Earrings 5×16mm · Grande 6×31mm (16.13g, heaviest) · Ear Cuff 5×15mm |
| **XSonic** | Earrings 20mm · Grande 2×20mm · Petite 15mm · Huggie 1.8×10mm · Helix 2×8mm (0.74g) · Ear Cuff 2×12mm |
| **XStreet** | Earrings 4×31mm · Petite 3×21mm · Petite Hoop 4×20mm · Grande Hoop 4×40mm · Ear Cuff 3×11mm · Ring 3mm · Grande Ring 4mm |
| **XStud** | Earrings 4×26mm · Ear Cuff 2×12mm · Petite Ear Cuff 2×12mm · Grande Ear Cuff 2.5×19mm |
| **XStyle** | Earrings 2.5×20mm · Grande 2.5×25mm · Petite 2.5×15mm · Ear Cuff 2×12mm · Grande Ear Cuff 2×20mm · Cuff Climber 10×25mm |
| **XSurge** | Earrings 3×30mm · Petite 3×20mm |
| **XSway** | Petite Hoop 3×20mm · Hoop 3×25mm · Grande Hoop 3×30mm · Ear Cuff 3×14mm · Climber 3×24mm |
| **XSChain** | Necklace (no size or SKU yet) |

- Rings: US 6 / 7 / 8 / Bespoke.
- On Myer (tag "Sell on Myer"): XSavage, XSavage Grande, XSculpt Huggie (Petite / Standard / Grande), XSharp, XSolid / Grande / Ear Cuff, XStreet Petite and Petite Hoop, XStud.

## Size & weight notes
- **Size** is the "W × H/diameter" line from each Shopify description. Use it for Slot 4 (size image) **after measuring the real piece**.
- **Weight** is the Shopify shipping weight in grams (first variant). Confirm whether it's per piece or per pair before it goes on any image or listing.

## Data issues to fix before listing (all flagged in the CSV `notes` / `material_per_description` columns)
1. **Material conflicts (18 rows):** some gold variants are named "Gold Plated Brass" but the description says "925 Sterling Silver Base, 18K Gold Vermeil" (e.g. XSense Petite, XStyle Petite, XSlick Petite Hoop, XSlim / XSharp / XSharp Bold / XSlick ear cuffs, XSonic Earrings). Several others list two base metals ("925 Sterling Silver Base … Plated Brass"). **Confirm the real base metal per SKU.** It changes the Amazon name and what images may say.
2. **XStud Ear Cuff black:** size 2.5×19mm vs 2×12mm for the other finishes.
3. **No weight (18 rows)**, mostly the 0717052… barcodes and the no-SKU items.
4. **No SKU:** XSharp Fine Ear Cuff (gold), XSense Ear Cuff SUF21I211 (all 3), XSway Hoop (one silver listing), XSChain Necklace.
5. **Possible duplicates:** XSense Ear Cuff (two listings, 6×11 vs 7×12mm: may be two designs), XSharp Huggie gold ×2, XSharp Fine silver ×2 (one description says black), XSway Hoop silver ×2.
6. **Price $0.00** on 113 rows. Price checks: XSculpt Grande Huggie black $180 vs $130; XStreet Grande Ring $50 < XStreet Ring $60; XStyle Grande Ear Cuff $35 < XStyle Ear Cuff $40; XSolid Ear Cuff gold $90 vs $60.
7. **Barcodes:** most SKUs are 9363472… GTINs; ten use 0717052… barcodes. Check those are valid GS1 GTINs before Amazon.

Excluded from the catalogue: "New Mould Ear Cuff" prototypes and Voglio Bene items (not X.S).
