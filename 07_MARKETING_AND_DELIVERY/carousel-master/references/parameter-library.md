# Parameter Library — the harness engine

The agent never designs parameters from zero. It SELECTS blocks and FILLS values. This file is the look-vocabulary; using it is what keeps the job fast.

**Precedence:** craft VALUES (type sizes, scale ratios, spacing, safe zones, color distribution, floors) come from `designer-brain.md` and always win. The blocks below select the LOOK; the brain supplies the numbers.

## Allocation rules

1. The **CORE block** is always present — merged into `design_system`, values identical on every slide. Fill its craft values from designer-brain.md law, not by feel.
2. Pick **ONE primary style block** via the selection table below. Its params go into each slide's `style_params`.
3. Optionally borrow ≤5 individual params from other blocks as accents (e.g. one `halftone_print` inside a photoreal deck). Label the borrow in `design_system.style_notes`.
4. Only if a needed parameter exists nowhere: invent a maximum of 5 custom ones, prefixed `custom_`.
5. Every value you fill must trace to intake (brand, reference, or script). No trace → strong default + `[ASSUMED]`.
6. **The library is the thinking layer, not the paste layer.** Distill each slide's chosen blocks down to ≤12 plain-instruction fields for its paste block (see output-template.md). Parameters that don't survive distillation served as decision scaffolding — that is their job. Never paste this file's raw parameter sets into an image model.

---

## CORE block (always present — lives in `design_system`)

| Param | Type | Notes |
|---|---|---|
| `composition` | text | overall framing system for the deck |
| `layout_grid` | enum | `centered` / `rule-of-thirds` / `left-aligned editorial` / `split` / `full-bleed` / `modular` |
| `visual_hierarchy` | text | what the eye hits 1st, 2nd, 3rd |
| `negative_space` | enum | `minimal` / `balanced` / `generous` |
| `focal_point_policy` | text | where the subject sits per slide |
| `lighting` | text | e.g. "soft directional daylight", "rim-lit dramatic" |
| `contrast` | enum | `low` / `medium` / `high` / `extreme` |
| `saturation` | enum | `muted` / `natural` / `vivid` / `hyper` |
| `grain_texture` | enum | `none` / `subtle film grain` / `heavy analog grain` / `digital noise` |
| `edge_treatment` | text | borders, bleed, frame style |
| `depth_layering` | text | foreground/mid/background stacking |
| `palette_application` | text | HOW the locked palette distributes (e.g. "70% cream ground, 20% coffee-brown type, 10% teal accent") |
| `typography_treatment` | text | weight, case, tracking rules from the brand lock |
| `render_quality` | enum | `standard` / `high-fidelity` / `maximum detail` |
| `style_strength` | 0-100 | how hard the style block pushes |
| `fidelity_to_reference` | 0-100 | how strictly reference look is mirrored (i2v denoise analog) |
| `continuity_thread` | text | the one element carrying across all slides |

## Style blocks (pick ONE primary)

### 1. `mixed_media`
*Use when: references show collage/tearing/paint-photo layering; scrapbook energy.*

`base_medium`, `secondary_medium`, `tertiary_medium`, `collage_density` (sparse→dense), `torn_paper_edges` (clean→rough), `paper_texture`, `paper_type` (kraft/newsprint/vintage card/watercolor), `canvas_weave`, `brush_stroke_style`, `brush_stroke_density`, `paint_opacity`, `paint_drips`, `ink_line_weight`, `ink_bleed`, `charcoal_smudge`, `watercolor_bloom`, `acrylic_impasto`, `gesso_underlayer`, `tape_strips`, `staples_stitches`, `photo_fragment_integration`, `halftone_print`, `risograph_misregistration`, `screenprint_overlay`, `xerox_degradation`, `typewriter_text_elements`, `handwriting_scribbles`, `sticker_elements`, `geometric_shapes`, `color_bleed`, `chaos_factor` (0-100), `layer_blend_mode`

### 2. `flat_vector_brand`
*Use when: clean corporate/startup look, Bitmoji-ish characters, flat illustration.*

`vector_style` (flat / cel-shaded / gradient-flat), `line_weight` (none→bold outline), `character_proportions` (realistic / stylized / chibi), `shape_language` (geometric / organic / angular), `shading` (flat / soft-gradient / two-tone), `pattern_fills`, `icon_density`, `spot_illustrations`, `background_treatment` (solid / subtle-pattern / geometric-stage), `stroke_consistency`, `depth_cues` (overlap / scale / none), `mascot_presence` (none / recurring / hero)

### 3. `photoreal_editorial`
*Use when: magazine-grade real-world imagery, "living portrait" painted-photo worlds.*

`photographic_medium` (35mm / 85mm portrait / medium-format), `depth_of_field`, `skin_texture_fidelity`, `fabric_rendering`, `set_dressing_density`, `prop_realism`, `color_grade` (e.g. "warm amber shadows"), `painterly_overlay` (none→heavy), `frame_within_frame`, `gaze_direction`, `pose_energy` (still / mid-action), `environment_era`, `atmosphere_haze`

### 4. `product_hero`
*Use when: the product/food is the star; Choolaah-style appetite shots.*

`hero_placement`, `surface_material`, `steam_freshness_cues`, `gloss_satin_levels`, `garnish_styling`, `cross_section_reveal` (0-100), `hero_scale_in_frame`, `background_support` (clean / contextual-scene / patterned), `shadow_softness`, `appetite_appeal_triggers`, `packaging_visibility`, `splash_motion_frozen`

### 5. `vintage_scrapbook`
*Use when: Analog Generation-style archival memory aesthetic.*

`era_anchor` (1900s-1990s), `photo_aging` (sepia / faded-kodachrome / b&w-yellowed), `corner_mounts`, `polaroid_frames`, `handwritten_captions`, `adhesive_tape`, `photo_corners`, `album_page_texture`, `date_stamp_inscription`, `ephemera` (tickets/stamps/labels), `document_fold_creases`, `memory_narrative_layout`

### 6. `bold_typographic`
*Use when: words are the hero; statement slides, quote carousels.*

`type_scale_ratio` (e.g. 10:1), `display_weight` (light→black), `case_treatment`, `kinetic_type_arrangement` (stacked / diagonal / exploded / masked), `type_as_image_moments`, `highlight_marker_style`, `underline_strike_accents`, `background_discipline` (flat-color only), `max_type_colors`, `readability_floor` (min size vs canvas), `glyph_play` (swashes / tight-tracking / negative-space)

### 7. `cinematic_photographic`
*Use when: moody film-still energy, storytelling decks, luxury tone.*

`aspect_feel` (anamorphic / spherical), `film_stock_emulation`, `black_level`, `highlight_rolloff`, `practical_light_sources`, `weather_atmosphere`, `color_contrast_pairs` (teal-orange etc.), `subject_isolation`, `lens_flare_discipline`, `grayscale_option`, `subtitle_space_reservation`

### 8. `surreal_concept`
*Use when: attention-grabbing conceptual imagery, metaphor slides, "wait what?" hooks.*

`concept_twist` (one-line visual metaphor), `scale_violation`, `gravity_logic` (real / broken), `material_swap` (e.g. "liquid metal fruit"), `impossible_joins`, `dream_palette_shift`, `floating_elements`, `reality_anchor` (one real element to ground it), `surprise_budget` (0-100)

### 9. `frame_break_dimensional`
*Use when: subject breaks the frame/edge — Choolaeh court-lock v3 energy, extension effects.*

`break_direction` (top / side / multiple), `break_depth_layers`, `cutout_cleanliness`, `drop_shadow_drama`, `overlap_order` (foreground element in FRONT of type), `background_plane` (flat / environment), `edge_continuation` (subject continues onto next slide), `dimensional_parallax` (none / subtle / strong)

### 10. `scrim_editorial_documentary` — PROVEN DEFAULT
*Use when: photographic documentary/editorial food or culture decks. Validated 2026-11-05: this exact system outperformed a raw-brief baseline in live generation (consistent campaign feel + finished typeset look).*

`scrim` (soft black gradient over left/top of photo for the text zone), `type_stack` (3 tiers: condensed bold UPPERCASE headline in accent color → handwritten script subtitle in white with accent-color brush underline swash → clean sans body in white, flush-left), `corner_marker` (recurring series element — bar + caps + script — identical position/size every slide), `photography_treatment` (extreme close-ups, real texture/char, natural unfiltered color, ember/directional warmth, subtle film grain), `accent_discipline` (accent color ONLY in type + marker + brand elements, never as a photo filter), `end_card_mode` (final slide = pure black ground, logo dominant, no photography)

The 3-tier type stack + fixed corner marker + scrim IS the campaign look — when references show any of these, pick this block.

---

## Selection table (essence → block)

| Essence keywords in references/tone | Primary block |
|---|---|
| collage, torn, layered, paper, craft | `mixed_media` |
| flat, clean, mascot, startup, vector | `flat_vector_brand` |
| editorial, portrait, painted-photo, magazine | `photoreal_editorial` |
| food, product, appetites, hero shot, menu | `product_hero` |
| archive, memory, old photos, family album | `vintage_scrapbook` |
| quote, statement, words-first, manifesto | `bold_typographic` |
| moody, film-still, luxury, cinematic | `cinematic_photographic` |
| metaphor, surreal, twist, unexpected | `surreal_concept` |
| breaks frame, pops out, extends edge, dimensional | `frame_break_dimensional` |

Ambiguous → pick the block matching the DOMINANT medium (photo vs illustration vs type), borrow accents from the secondary pull.

## Slide-role value shifts

Within one deck, the SAME blocks shift by role — this is the craft layer:

| Role | Shifts |
|---|---|
| `hook` (slide 1) | `style_strength` +15-20, `contrast` up one notch, boldest focal point, curiosity gap in composition |
| `story` / `point` | balanced values, `negative_space` generous for text |
| `proof` | realism params up, style params slightly down |
| `offer` / `cta` (last) | accent color maxed, `visual_hierarchy` = offer first, `continuity_thread` pays off |
