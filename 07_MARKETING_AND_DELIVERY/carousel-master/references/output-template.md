# Output Contract — TWO LAYERS + decisions block

**Layer 1 — Brand Lock**: one compact JSON the user reviews. Never pasted into an image model.
**Layer 2 — Generation Prompts** (mode by engine — see model-playbook.md):
- **Mode B — MASTER PROMPT** (default; Google AI Studio / Flow multi-image): ONE JSON block for the whole deck.
- **Mode A — per-slide blocks** (single-image surfaces): one JSON block per slide, ≤12 fields, ≤200 tokens.

**Ready-to-ship standard:** text BAKED (exact copy), logo from the user's uploaded reference (never redrawn). Slides arrive finished and publishable. Exact-brand-font demands → PLATE mode switch (closing line 4), never an extra question.

## Layer 1 — Brand Lock (ONE fenced json block, ≤60 lines)

```json
{
  "carousel_meta": {
    "brand": "", "campaign": "", "platform": "", "aspect_ratio": "",
    "resolution": "", "slide_count": 0, "target_engine": "",
    "design_essence": "one line: the deck's thesis + its 1-2 DEFINING techniques",
    "text_policy": "baked | plates"
  },
  "brand_lock": {
    "palette": { "primary": "#", "secondary": "#", "accent": "#", "background": "#", "text": "#", "rules": "60/30/10 distribution + forbidden combos" },
    "typography": { "display": "family + weight", "body": "family", "script_accent": "or none", "headline_px": "range @1080w", "body_px": "≥36", "case_rules": "" },
    "logo_law": "uploaded reference only; reproduce exactly; never redraw",
    "series_marker": "element + position + size",
    "tone_words": ["", "", ""],
    "locked_fields": ["palette", "typography", "marker", "logo law", "verbatim copy"],
    "assumed_fields": ["every [ASSUMED] decision listed here"]
  },
  "design_system": {
    "primary_style_block": "from parameter-library.md",
    "defining_techniques": ["the 1-2 counterfactual-tested moves"],
    "continuity_thread": "one motif + how the last slide pays it off",
    "layout_system": "grid pattern + margins + safe zones",
    "palette_application": "60/30/10 mapping",
    "photography_treatment": "grade sentence, VERBATIM-repeated per slide",
    "variation_budget": "anchors + background modes planned across slides",
    "swipe_cue_system": "one system, named"
  }
}
```

Rules: ≤60 lines. No `slides[]` — slide content lives in Layer 2. `[ASSUMED]` tags live here and in `assumed_fields` only. Slide 1 as existing video → note in `carousel_meta`, never emit a prompt for it.

## Layer 2 Mode B — MASTER PROMPT (default, ≤500 words)

```json
{
  "task": "Generate N finished Instagram carousel slides, one image per slide object, 4:5 portrait, 1080x1350, <medium/quality line>",
  "reference_images": {
    "image_1_logo": "reproduce EXACTLY as supplied — never redraw, restyle, or approximate; preserve proportions, colors, lettering",
    "image_2_style_ref": "mood/grade/composition structure ONLY — every color, typeface and brand element comes from the rules below and OVERRIDES the reference",
    "image_3_product": "GLOBAL IDENTITY LOCK: preserve exact shape, proportions, materials, finish, color relationships, and label graphics as photographed physical parts"
  },
  "style_system": {
    "photography": "<one line: medium, lens, light, grade sentence — repeated verbatim per slide>",
    "text_zone": "<scrim spec: e.g. black scrim 0.85 opacity left third, text contrast ≥4.5:1 after scrim>",
    "typography": "<stack: display style + px range, script accent, body ≥36px, flush-left, caps rules>",
    "series_marker": "<exact element + position + size, identical every slide>",
    "color_rules": "60% ground / 30% secondary / 10% accent; accent marks ONE thing per slide; photos natural, never accent-filtered",
    "safe_zones": "keep top 10% and bottom 10% free of text, logos and UI"
  },
  "slides": [
    {
      "n": 1, "role": "hook",
      "headline": { "text": "EXACT COPY ≤8 WORDS", "style": "treatment", "position": "zone + px" },
      "script_line": "or null",
      "body": "≤2 trimmed sentences",
      "image": "ONE vivid scene: subject + action + lens + light + surface",
      "layout": "anchor choice + where type sits + where subject sits",
      "swipe_cue": "this slide's beat of the cue system"
    }
  ],
  "quality_bar": "ready to publish — every word spelled exactly as given, flush-left body blocks, no narrow ragged columns, consistent marker and margins across all slides"
}
```

Rules: slide objects carry only what DIFFERS (headline/body/image/layout/swipe_cue; `style_line` only for script-accent slides). Paired slides state the match explicitly ("identical treatment to slide N"). >8 slides → split into two master prompts (slides 1–5, 6–N) sharing the identical `style_system`. Existing-video slide 1 → start graphic slides at n:2 labeled "graphic 1 of 5 (deck slide 2)".

## Layer 2 Mode A — per-slide block (fallback; ≤12 fields, ≤200 tokens)

```json
{
  "format": "carousel slide N of M, 4:5, 1080x1350",
  "image": "ONE vivid scene: subject + action + lens + light + surface + grade",
  "headline": { "text": "EXACT COPY", "style": "treatment + px", "position": "zone" },
  "script_accent": { "text": "", "style": "", "position": "" },
  "series_marker": "exact recurring element + position, identical every slide",
  "support_text": { "text": "", "position": "" },
  "logo": "from uploaded image — reproduce exactly, position + clear space",
  "layout": "anchor + type zone + subject zone",
  "mood": "3-5 words",
  "continuity": "this slide's thread beat + swipe cue",
  "avoid": "≤6 concrete exclusions"
}
```

No `n/a` fields — drop them. All strings are machine instructions. Upload the logo alongside every generation.

## Closing lines (exactly four, after the prompts)

1. Paste note: "Paste into Google AI Studio/Flow with the logo (and any product/style refs) uploaded alongside. If your surface returns one image per run, run per slide." (Engine-specific variants in model-playbook.md §1.)
2. `[ASSUMED]` count + where they live (the lock).
3. "Run it — if a slide is off, tell me its number + what's wrong; I'll issue surgical fixes, zero drift."
4. PLATE switch (only when exact brand fonts matter): "PLATE mode: I re-issue these as clean imagery with empty text zones + a handoff spec (copy, fonts, sizes, positions) for your editor."

Then the **Decisions & Assumptions** block (≤5 bullets, per inference-checklist.md §4). Then STOP — no essays.

## Worked example — one Mode A block (Choolaah Ch.05 slide 3, ~180 tokens)

```json
{
  "format": "carousel slide 3 of 6, 4:5, 1080x1350",
  "image": "85mm close-up photograph: chicken tikka skewers drawn from a clay tandoor, glistening marinade, honest char gradients, ember glow from below, smoke curling through dark background, natural documentary color, subtle film grain",
  "headline": { "text": "CHICKEN TIKKA", "style": "ultra-condensed bold uppercase, campaign orange, ~120px", "position": "top-left on black scrim" },
  "script_accent": { "text": "The Magic of the Tandoor", "style": "white handwritten script ~52px with orange brush underline", "position": "under headline" },
  "series_marker": "top-left corner, identical every slide: slim orange bar + orange caps 'CHAPTER 05' + white script 'Indian Diaries with Simran'",
  "support_text": { "text": "Marinated chicken. Intense heat. Smoky, charred edges.", "position": "scrim, white sans 40px, flush-left" },
  "logo": "none this slide",
  "layout": "scrim-panel left third; food owns right two-thirds, ember glow lower frame",
  "mood": "warm, alive, appetizing, documentary",
  "continuity": "fire-and-smoke thread; smoke edge-peek toward slide 4",
  "avoid": "restaurant names, misspelled words, orange filter over photo, sterile studio light, text over busy areas without scrim"
}
```
