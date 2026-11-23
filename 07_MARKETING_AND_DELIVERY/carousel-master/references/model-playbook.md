# MODEL PLAYBOOK — engines, surfaces, references, failure fixes

How the prompts reach a rendering engine and how references are addressed. Read during S3 (BUILD) alongside output-template.md.

## 1. Engine matrix

| Engine | Pick it when | Native ratios | Refs | Notes |
|---|---|---|---|---|
| **Nano Banana Pro / 2** (Google AI Studio, Flow, Gemini) | DEFAULT for this system. Text rendering + photoreal + multi-reference + native 4:5 | 1:1, 3:4, **4:5**, 9:16, 16:9, 2:3, 5:4, 21:9 · res 1k/2k/4k | ~14 (NB2 Lite; Pro similar) | Best in-image text of the Google family; handles master-prompt multi-slide runs |
| **GPT Image 2.5** (ChatGPT / API) | Typography-critical decks, UI-like layouts, JSON region discipline | 1:1, 2:3, 3:2 (no native 4:5 → generate 3:4 + crop, §4) | multiple --image flags | Reads JSON layout regions as layout intent; quote text verbatim |
| **Ideogram v3 (`Design` style)** | Type-led/quote decks where typography is the design | 1:1, 3:4, 4:3, 9:16, 16:9 | limited | The typography-strong alternative |
| **Seedream 5.0 Pro** | Face/character sheets, person continuity | 1:1, 3:4, 4:5-family, 9:16, 16:9 · res 1k–4k | ≤10 | Faces + character locks |
| **Recraft V4.1** | Logo/vector assets, controlled-palette graphics (components, not full slides) | platform-set | none (prompt-only) | Use for making logo variants/lockups, not photographic slides |
| **Flux Kontext Max** | Editing an existing approved slide (style transfer, typography remix) | platform-set | 1 (edit target) | "Describe the change, not the input" |
| **Midjourney** | Last resort for aesthetics exploration — no reliable baked text | any via --ar | image prompts | Convert per output-template note; never for text-bearing slides |

**Default:** whatever surface the user names. User's named workflow = **Google AI Studio / Flow → Nano Banana family, master-prompt mode**. If the user names a model, use it and keep using it for follow-ups.

## 2. Surface mechanics

- **Google AI Studio / Flow (master-prompt mode):** user pastes the ONE master JSON + uploads logo (and style/product refs) alongside. State the slide count and per-slide output explicitly ("generate one image per slide object"). If the surface returns only ONE image per run: run the master once per slide (reference the slide `n`), or switch to Mode A blocks. Ratio: declare it in the prompt ("4:5 portrait, 1080x1350") AND set the UI ratio selector if present.
- **Higgsfield CLI (gpt_image_2):** `--image` flag per reference (logo → specimen → product; `Image0` = first flag), `--aspect_ratio 3:4 --resolution 4k --wait --json` + crop for 4:5 (§4).
- **ChatGPT:** paste one Mode A block per generation; it accepts images as uploads.
- **Honesty rule:** multi-image-per-prompt behavior varies by surface — never promise N images from one paste; say "if your surface returns one at a time, run per slide."

## 3. Ratio & resolution

| Deck | Ratio | Resolution |
|---|---|---|
| IG/LinkedIn carousel | **4:5** | 1080x1350 (request 2k–4k from engine, downscale) |
| IG story/reels cover | 9:16 | 1080x1920 |
| Square set | 1:1 | 1080x1080 |
| LinkedIn document | 1:1 or 4:5 | 1080-wide |

**4:5 strategies:** Nano Banana family → native `4:5`. GPT Image → compose with a centered 4:5 safe area, generate 3:4, crop vertical excess: `magick generated-3x4.png -gravity center -crop '100%x93.75%+0+0' +repage final-4x5.png` — then verify no locked logo/copy crosses the crop boundary. Ideogram → 3:4 nearest, same crop.

## 4. Reference grammar (role-labeled, law-carrying)

Label every reference by role and state what it controls and what it must NOT control:

- **Image 1: official logo** — "reproduce EXACTLY as supplied; never redraw, restyle, or approximate; treat branding as a photographed physical part of the scene, preserving exact typography, stroke weight, spacing, alignment, placement." Prefer deterministic compositing when the logo needn't interact with the scene.
- **Images 2–3: style references** (approved past slides/mood) — two-list rule: take ONLY mood/grade/composition structure from them; ALL visual identity (color, typefaces, accents, logo) comes from the brand lock and ALWAYS overrides whatever appears in the reference. Never leave brand tokens to be inherited from an image.
- **Image 4: product/dish/person** — paste-ready locks:
  `GLOBAL IDENTITY LOCK (CRITICAL): preserve the exact identity of the subject from Image 4 — identical shape, proportions, silhouette, structure, materials, finish, seams, edges, color relationships, wear, and product-specific features.`
  `BRANDING / GRAPHICS / LABEL LOCK (CRITICAL): preserve all labels/graphics EXACTLY — typography, stroke weight, spacing, alignment, placement — as photographed physical parts, not digitally recreated artwork.` For real people add: identity/face/attire must remain unaltered when the brief locks them.
- **Typography specimen PNG** (when a brand font exists): attach it; after render, compare letterforms — retry ONCE on visible substitution, then report the limitation instead of passing approximate type off as exact.
- **Wireframe intermediation** (inheriting a layout from a reference ad): pass a brand-neutral wireframe (zone boxes labeled) as the layout reference instead of the ad itself — inherit structure without inheriting identity.
- **Caps:** respect the engine's ref limit; cap the kit at 4–5 refs for slides (logo + specimen + product + 1–2 style refs).

## 5. Prompt-format specs

- **Zones** with fractional coordinates (`{"top":0.10,"bottom":0.45}`) — falsifiable direction, not vibes.
- **Count-and-label** for repeated elements (`"count": 6, "items": [...]`).
- **Position-scoped regions** (`top-left`, `mid-right`, `bottom-center`).
- **Inline typography callouts** (`"headline in ultra-condensed bold uppercase, campaign orange, ~120px"`).
- **Quoted verbatim text** — real copy in quotes exactly as it should render; never paraphrase; CJK/devanagari stays in original form (and flag that non-Latin scripts often garble — prefer PLATE mode there).
- **Positive phrasing** ("tack sharp", "uninhabited") over negatives; mirror zone exclusions in `avoid`.
- **Budgets:** Mode A ≤200 tokens; master ≤500 words — beyond this engines drop instructions.

## 6. Failure → prevention phrases

| Artifact | Prevention phrase |
|---|---|
| Product looks cheap | "black velvet surface, surface catches light on edges" (named surface + texture cue) |
| Style ignored/generic | "Style: <exact named style>. <specific color grade>" — commit to ONE named style |
| Color drift across slides | repeat the EXACT same grade sentence in every slide prompt |
| Plastic/waxy skin | "natural skin texture, subtle imperfections" + film language, never "photorealistic" |
| Garbled baked text | shorter strings (≤8 words), name the font style + size + color + position; simplify and retry once |
| Extra invented elements | zone exclusions: "left third: pure black scrim, no objects" + mirrored `avoid` |
| Logo drift | reproduce-exactly law + "treat as photographed physical part" + reference the file, don't describe it |
| 4:5 unsupported | 3:4 + center-crop workflow (§3) |

## 7. i2i edit patterns (fixing approved slides)

"Replace X with Y, keep <list> unchanged" · keep-list discipline (enumerate what must not move) · CRITICAL-preserve marker for identity ("CRITICAL: maintain exact pose, expression, facial structure") · consistency clause across edits ("keep hairstyle and outfit consistent across edits") · Flux Kontext: describe the change only.
