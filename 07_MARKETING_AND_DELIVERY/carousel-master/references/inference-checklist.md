# INFERENCE CHECKLIST — zero-intake extraction

The system NEVER asks preference questions. It infers from what the user drops, decides with conservative professional defaults, and states its decisions after delivery. The ONLY allowed stop: **no script/content exists at all** — then ask ONCE for topic + key points (a bare-bones draft is acceptable too, marked assumed), and never again.

## 1. Extraction map (run silently against the dropped materials)

**From anything brand-related (guidelines doc, brand mention, past prompts, website text):**
- Brand name + exact spelling (copy verbatim — never re-spell)
- Palette evidence: stated hexes; colors named in prose; colors implied by refs; else industry-appropriate palette (tag [ASSUMED])
- Typography evidence: named fonts; type descriptions ("tall condensed bold uppercase"); else derive from tone (tag [ASSUMED])
- Logo: file mentioned/uploaded → reference law; only described → instruct upload; absent → text wordmark treatment (tag [ASSUMED])
- Tone words (3) + forbidden clichés if stated

**From references (described in words, named past styles, or attached images):**
- Medium (photo / illustration / 3D / type-led / mixed) → style block selection
- 3–7 essence keywords (concrete: "torn kraft, riso misregistration, ember-lit macro")
- Era/grade cues, lighting language, texture language
- What to AVOID (stated + inferred from what refs reject)

**From the script/content (headlines, beats, captions):**
- Slide list: hook → points → CTA; if the script lacks a CTA beat, append a CTA slide and tag it [ASSUMED]
- Verbatim headlines/support per slide (trim only per type law: headline ≤8 words, body ≤40)
- CTA text; footnote claims to suppress (unverified history, prices)

**From context (platform, model, assets):**
- Platform/ratio: stated → use; else IG 4:5 1080x1350 [ASSUMED]
- Engine: stated → lock it; else Google AI Studio master-prompt mode [ASSUMED]
- Uploaded files inventory: logo? product shots? past slides? font files? — each becomes a role-labeled reference

## 2. GRILL self-interrogation (from the prompt-builder discipline; internal, silent)

Aggressively inspect the resolved brief for: ambiguity (which of two meanings?), contradictions (script vs brand doc?), missing production details (what would a photographer ask?), unwanted model freedom (where will the engine invent?), identity drift (what must stay locked?), geometry/artifact risks (what garbles text?). Resolve EVERY gap with a conservative professional default. Do not surface the questions — surface the decisions.

**Conflict precedence:** client's explicit copy > brand guidelines > past approved style > references > industry defaults. A brief's "avoid" list overrides everything.

## 3. Defaults library (apply without asking; tag [ASSUMED] in the lock)

| Missing | Default |
|---|---|
| Platform/ratio | IG 4:5, 1080x1350 |
| Engine | Google AI Studio / Nano Banana Pro, master-prompt mode |
| Palette | From refs; else industry-appropriate (60/30/10 structured, accent from brand world) |
| Typography | Display + body pair matched to tone; script accent only if series identity suggests it |
| Text policy | BAKED (ready-to-ship standard); PLATE mode one-line switch if exact brand fonts are non-negotiable |
| Marker | Recurring element invented from brand world (bar + chapter label + series script line), top-left, ≥24px |
| Slide count | From script beats; hook + points + CTA structure |
| Continuity thread | One motif from the design essence (object/color/marker payoff) |
| Language | English (non-Latin scripts → recommend PLATE mode for those lines) |
| Swipe cue | Edge-peek or index dots in marker zone |

## 4. Decide-with-motive output (after delivery, 5 bullets max)

Format: `[Element]: [decision] — because [trace to brief/brand/reference/craft law]. [ASSUMED]` where inferred. Example:
- "Scrims left third — headline sits over busy street photography; 4.5:1 contrast after scrim."
- "4:5 IG — unstated, platform-standard for carousels [ASSUMED]."
- "Paneer slide mirrors chicken slide's lens/DOF — brief demands a deliberate pair."

## 5. Boundaries of inference

Never infer: factual claims (history, prices, statistics) — copy or omit. Never alter: real people's faces/attire. Never approximate: a supplied logo. If brand data exists as a FILE (guidelines PDF), its explicit rules are `fixed`; everything you invent is `proposed` and revisable.
