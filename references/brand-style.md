# Brand Style — STRICT (fonts + colours)

These rules are mandatory for every image (Slots 2–9 + EBC). No other fonts or colours may be used. The Main image is always product-only on pure white (see `sop/amazon-image-policy.md`).

## Fonts — STRICT (from the live site, 23–24 Nov 2026)
| Use | Font | Setting |
|---|---|---|
| **Headings** (every image headline) | **Bodoni Moda Italic** (Google Font) | Italic 400, high-contrast Didone; **sentence case** like the site ("Worn, not shown"), never all caps; normal letter-spacing |
| **Everything else**: labels, callouts, measurements, body lines, footer | **Jost** (Google Font) | Labels: Medium 500, UPPERCASE, letter-spacing 0.15–0.2em. Body: Regular 400, sentence case. Big numbers: Light 300 |

- Site reference: `reference-sets/brand-info/site-heading-font_Bodoni-Moda-Italic.png` (homepage image headline, CSS `--d1-serif`).
- Max one heading per image. Never set labels or body text in Bodoni; never set the heading in Jost.
- The theme settings ("serif" / Helvetica) and Wix Madefor Text (old product pages) are NOT brand fonts for Amazon.
- In Canva, lock Bodoni Moda Italic + Jost in the brand kit.

## Font colours — STRICT (all text on all images)
Text may ONLY be one of these four:
| Text colour | HEX | Use |
|---|---|---|
| Black | `#1C1C1C` (or `#000000`) | Headlines, labels, body on white or light gray |
| White | `#FFFFFF` | Any text on red, black or a photo |
| Gray | `#3A3A3A` | Secondary text and captions on white or light gray |
| X.S Red | `#560C0D` | Small-caps eyebrow labels, numbers, accents on white or light gray. Never for body text, never on a dark background |

- **No other text colour, ever:** no gold or tan text, no cream or warm white, no brown, no pink, no colour taken from the product.
- Lines, rules, icons and dimension arrows follow the same four colours.
- Contrast: black, gray or red text only on white / `#F2F2F2`; white text only on red / black / dark photo areas. Gray text never on red or black.
- In Canva, lock these four as the brand kit's only text colours.

## Colour palette — ONLY these
| Role | Colour | HEX |
|------|--------|-----|
| Black (text, icons, lines) | Website text black | `#1C1C1C` |
| Pure black (accents, deep backgrounds) | Black | `#000000` |
| White (backgrounds, reversed text) | White | `#FFFFFF` |
| Gray (secondary backgrounds, dividers) | Light gray | `#F2F2F2` |
| Gray (secondary text, icons) | Dark gray | `#3A3A3A` |
| Text on red | Warm white is NOT allowed — use pure white | `#FFFFFF` |
| Red (model backgrounds) | Deep oxblood red, sampled from the approved XSavage model images | `#560C0D` (shadows down to `#410608`; lit centre of a gradient may reach `#A0282A`) |

Rules:
- No other colours in backgrounds, text, icons, shapes or props. No cream, blush, gold-coloured text, gradients of other hues.
- Product colours (metal/stone) are shown true-to-life and are the only exception.
- Red is used for the model background images. It is not used for body text.
- Lifestyle scenes: background, props and clothing must fall within black / white / gray / brand red.

## Style block (paste into `{STYLE_BLOCK}`)
`premium minimalist fine-jewellery photography, strict monochrome palette of black, white and gray with brand red only where specified, clean modern luxury aesthetic, soft diffused studio light, high-end editorial e-commerce, consistent with SALLY SKOUFIS brand`

Model-slot add-on: `deep oxblood brand-red background (#560C0D), soft studio light, subtle gradient, model wearing black or white clothing`

## Fixed layout elements
- Text position, margins (≥5% safe area) and sizes identical across all slots — copy from the benchmark set.
- Icons: thin-line, single colour `#1C1C1C` (or `#FFFFFF` on dark/red).
- Models: **X.S models only** (`reference-sets/xs-models/`). No other people, no stock or AI-invented faces. Natural skin, minimal makeup, black/white/gray clothing; any other jewellery must be X.S product.
- Logo (if used): small, black or white only, same corner every slot. Never on Main.

## Approved red benchmark
`reference-sets/XSAVAGE-BLACK-RHODIUM/01_on-model_red.jpg` and `02_promise_red-plinth.jpg` — match this red exactly.
Red accent text (small caps labels, numbers) on white/gray backgrounds is allowed in `#560C0D`, as seen in 03–05.
