# DESIGNER BRAIN — Craft Law for Carousel Design

The design vocabulary of a world-class art director. Every value here is a decision with a motive.
Read fully during S2 (DECIDE). Values in this file override generic instincts.

## 0. Operating doctrine

1. **Decisions with motive.** Every parameter gets a value AND a why traceable to the brief, brand, or reference. "Scrims left because the headline sits over busy street photography." Never "looks nice."
2. **Jargon ban (IRIS law).** Replace "clean / moody / cinematic / vibey / aesthetic" with a measurable mechanism: a ratio, a Kelvin, a px value, a zone, a hex. If you can't measure it, you haven't decided it.
3. **One expressive move.** Expressive type → quiet palette and layout. Expressive palette → quiet type. One deck, one dominant move (brandkit-design-brain law).
4. **Defining techniques: 1–2 per deck.** The counterfactual test: "if I neutralize this one technique, does the deck collapse into generic noise?" If yes it's DEFINING (max 2); if it still works it's SUPPORTING (max 4). Name them in `design_essence`.
5. **The bar:** "If another AI, given a similar prompt, would produce substantially the same output, you have failed." Design from THIS brand's world, not from defaults.
6. **Boldness in one place.** One memorable element per deck; everything around it quiet and disciplined.
7. **Chanel rule.** Before delivering, remove one accessory.
8. **Squint test.** Blur your eyes: hierarchy still readable, nothing harsh, slides divide cleanly.

## 1. Type law

**Scale ratios:** 1.2 (dense/calm) · 1.25 (default) · 1.333 (expressive) · 1.414 (Swiss monumental). Derive sizes from the ratio — never size type by feel. Worked 1.25 chain from a 36px body: 36 → 45 → 56 → 70 → 88 → 110 → 137 → 171 (map roles onto steps: caption 29 · body 36 · subhead 45-56 · headline 88-110 · display 137 · monumental 171).

**Role pairing (one decision per role):**

| Role | Size @1080w | Line-height | Weight | Tracking |
|---|---|---|---|---|
| Monumental headline | 150–170px | 1.05–1.1 | display face, heavy | −0.01 to −0.02em |
| Headline | 96–130px | 1.1 | display, bold | −0.01em |
| Script accent | 44–64px | 1.2 | script face | 0 |
| Body/support | ≥36px | 1.45–1.55 | 400–500 | 0 |
| Labels/marker | ≥24px | 1.3 | 500–600 | +0.05em only if caps |
| Hero stat number | 200px+ | 1.0 | display, heavy | −0.02em |

**Hard floors (mobile feed readability — these are vetoes, not preferences):** body ≥36px · labels/marker ≥24px · headline ≤2 lines · body block ≤40 words and ≤6 lines · line length ≤36 characters · baked-text contrast ≥4.5:1 against its FINAL background (after scrim). At in-feed thumbnail (~350px wide), the headline must still be legible: if it isn't at 32% zoom, the type is too small or the words too many.

**Weight beats size.** Build hierarchy from size + weight + color together; two tiers can share one size and split by weight/color. Headings 400–700 max; heavy blacks reserved for display faces. No thin weights (≤300) below 40px on image backgrounds.

**Family cap: 2** (display + body; a script counts as one). Pair for contrast; two near-identical sans = a mistake. **Serif discipline:** "creative brief → serif" is the single most-tested AI tell. Serif only if the brand names one or is genuinely editorial/heritage/luxury — and say why THIS serif fits THIS brand. Fraunces and Instrument Serif banned as defaults. Emphasis inside a headline = weight or italic of the SAME family. Rotation pool when choosing fresh serifs: PP Editorial New, GT Sectra, Tiempos Headline, Recoleta, Cormorant Garamond, Playfair Display, EB Garamond, Canela, Domaine Display, Saol Display.

**Case rules:** sentence case default; tracked-out ALL-CAPS labels are an AI tell — max one caps lockup per slide (the marker or the headline, not both). ALL-CAPS condensed display only when the brand lock says so.

## 2. Layout law

**Canvas margins:** 8% of width (~86px @1080) minimum on all sides for text and logos.
**Safe zones (hard rule):** keep the top 10% and bottom 10% of every slide free of text, logos, buttons, UI — Instagram UI overlays consume them. Photographic content may enter. Text also avoids the right ~8% where the profile rail can overlap on some surfaces.
**Grid:** think 12-column. Practical carousel patterns: text zone = left 38–45% or top 35–45%; subject owns the remaining field. Zone schema (fractions of frame height, falsifiable):

```json
"layout_zones": { "text_zone": {"top":0.10,"bottom":0.45}, "subject_zone": {"top":0.30,"bottom":0.90}, "marker_zone": {"top":0.04,"bottom":0.10} }
```

**Composition anchors (pick per slide; ≥3 distinct across a deck; never default to anchor 5 out of habit — left-text/right-image is the most overused AI pattern):**
1 Centered statement · 2 Top-left lead, support bottom-right · 3 Bottom-left text over image · 4 Bottom-right CTA cluster · 5 Left-third caption + right visual · 6 Right-third caption + left visual · 7 Centered-low (text in lower 40%) · 8 Off-grid editorial offset · 9 Stacked center minimal · 10 Image-as-canvas, text in clean safe area · 11 Top band text, full-bleed image below · 12 Scrim-panel left (panel holds all type, photo owns the rest).

**Variation budget per deck:** same anchor ≤2 consecutive slides · ≥3 distinct anchors per deck of 5+ · ≥2 distinct background modes · same background mode ≤3 consecutive · one deliberate hero scale decision (giant / mid / mini — never split the difference) · exactly ONE second-read moment per deck (an oversized numeral, one material switch, one macro crop carrying brand color, a side-rail note) — placed once, supporting scan order.

**Background modes (12):** 1 solid + inline asset · 2 subtle texture/paper/grid · 3 full-bleed image + tonal overlay · 4 editorial side-image 50/50·60/40 (invertible) · 5 image-as-canvas + safe-area text · 6 flat color block + detail crop · 7 palette-matched tonal gradient (low chroma) · 8 atmospheric photo, single-tone brand grade · 9 duotone, palette-locked · 10 radial vignette + crop · 11 micro-noise gradient over solid · 12 color-blocked diptych.

**Scrim specification (text-over-photo legibility):** black gradient scrim over the text zone: opacity 0.82–0.88 at the text edge falling to 0.0 by 55–65% width; OR solid/near-solid panel behind type. Verify ≥4.5:1 text contrast AFTER the scrim. Never place baked text over busy mid-tone areas unprotected.

**Focal point:** one per slide — name it out loud, make it win (size, contrast, position, or surrounding whitespace), demote everything else deliberately. **Breathe unevenly:** tight groups, real air between groups; monotone spacing = nobody decided.

## 3. Color law

**60/30/10:** 60% dominant surface/tone, 30% secondary, 10% accent. Color is scarce; most of the slide is structure.
**One-accent lock:** one accent color per deck, used sparingly, and on any single slide it marks exactly ONE thing (headline, CTA, or marker element — never two).
**No pure #000000** — near-black (zinc-950 range) unless the end-card brief explicitly demands true black. Never mix warm and cool grays in one deck.
**Blue-purple gate (measurable veto):** if >30% of a slide's area is hue 225°–300° at saturation ≥0.30 (purple/blue glow family) → veto unless the brand mandates it. Same discipline for neon-cyan and purple-pink gradient defaults.
**Banned default families (cream/brass AI-look):** backgrounds #f5f1ea #f7f5f1 #fbf8f1 #efeae0 #ece6db #e8dfcb · accents #b08947 #b6553a #9a2436 #9c6e2a #bc7c3a #7d5621 · warm near-black text #1a1714 family — unless the brand genuinely owns them. Rotation families when inventing: Cold Luxury (silver/chrome/smoke) · Forest (deep green + bone + amber) · Black & Tan (true off-black + warm tan) · Cobalt + Cream · Terracotta + Slate · Olive + Brick + Paper · Monochrome + one saturated pop.
**Gradients — allowed:** low-chroma palette-matched tonal, single-hue atmospheric grade, soft vignette, noise-textured. **Banned:** rainbow/mesh, purple-blue AI default, pink-orange creator default, neon glow halos, gradient text as premium shortcut.
**Palette lock:** identical hexes across all slides. Full-bleed imagery must tonally match the palette; grade phrases repeat verbatim per slide ("warm amber shadows, lifted blacks" on every slide that needs grade).

## 4. Continuity & variation (set coherence)

**Brand-world locks (identical every slide):** palette + accent logic · typography family + scale logic · series marker (position, size, content) · corner-radius/shape language · image treatment (grade, grain, framing) · copy voice. **Variation allowed in:** anchor, background mode, density, subject, which swipe cue. "A viewer flipping through every frame must recognize one brand."
**Narrative spine (pick 1):** artifact/collectible · journey/pilgrimage · precision instrument · living system · stage/spotlight · archive/dossier. The spine shapes slide order and the second-read moment.
**Swipe cues (static, pick ONE system per deck):** edge-peek (next slide's motif half-visible at the boundary) · index dots "n/M" in marker zone · arrow motif · cut-element continuation (an object/smoke crossing the slide edge) · color handoff (accent migrates across slides). Slide 1 always carries an explicit cue; the last slide pays off the thread (continuity_thread completes).

## 5. Slide-role mechanics

| Role | Craft |
|---|---|
| **Hook (slide 1)** | One clear subject, strong information gap, reads in <1s at thumbnail. ≤7 headline words. Decide image-led (subject + short type) vs type-led (statement + quiet backdrop). Boldest contrast of the deck lives here. |
| **Story / point** | Generous negative space; body text earns its lines; anchor varies from hook. |
| **Proof** | Realism parameters up, style parameters down; concrete evidence (receipts, macro, process) over claims. |
| **Stat / data** | ONE stat per slide; the number is the hero (200px+); label above, source line below; no chart grids unless the brief demands data viz — then one chart, clearly biggest. |
| **CTA / end card** | Maximum restraint: quiet ground, logo dominant (supplied asset), one promise line ≤10 words, micro-CTA 1–2 words. Pays off continuity_thread. |

## 6. Hook frameworks (carousel-adapted; truthfulness law: exaggerate execution, never invent facts)

Before/After split · Social-UI card (generic bubble, no real platform brands) · Three-step progression panels · Posed portrait (subject large) · Posed action mid-moment · Big "DAY N"/"CHAPTER N" badge · Graphical/diagram frame · Landscape (environment hero, small subject on a third) · Map/aerial with highlighted point · Product-as-answer · Callout (arrow + 1 word) · Repetition of one object filling frame · Extreme size contrast · Amplified reality (exaggerate ONE real element). Brainstorm ≥5 concepts before committing to slide 1; frameworks may combine two.

## 7. Photography direction

Use film language, not "photorealistic," especially with faces ("35mm, natural skin texture, subtle imperfections" — photoreal + faces = plastic). Grade phrases lock verbatim across slides. Specify lighting source and quality every time ("single warm side-light", "golden hour"). Product shots: named surface ("black velvet", "worn wood") + texture cues ("surface catches light on edges"). Crop tightness: extreme close-up only for texture heroes; faces crop no tighter than mid-chest on hook slides. Gaze and gesture vectors point INTO the reading direction (toward next slide). Motion-implied energy: frozen mid-action, rising smoke, drifting particles.

## 8. Copy law

Copy is verbatim law: **never invent claims, prices, CTAs, sale language, or statistics.** Headline ≤8 words (hook ≤7). Body block ≤40 words. CTA 1–2 words naming the action. No em-dashes in slide copy. Banned copy vibes: unleash, elevate, revolutionize, next-gen, seamless, powerful solution, transformative. Banned fake brands: Acme, Nexus, NovaCore, Quantumly. If a headline could fit another brand's deck, rewrite it with this brand's own nouns (template check). Slide copy quick-check: active voice, specific nouns, no exclamation marks, no trailing periods on labels, numbers one format.

## 9. Restraint & slop bans (static-relevant)

Eyebrow badge above headline (duplicates it) → cut · glowing pills/badges/dots → none unless marking real state · glassmorphism >1–2 elements · decorative left-color stripes · emoji as decoration · generic AI icons (sparkle/star/robot/orb) · gradient text · giant heading + weak tiny subcopy · identical card rows · three identical stat columns · fake dashboards · "trusted by" logo walls · over-packed slides · filling every empty area · purple-blue default glow · everything-pill corner radii (radius system: one rule, applied everywhere) · monospace type as mood · middle-dot meta strings ("A · B · C") · arrow-suffixed links.

## 10. Deck-type playbooks

**Heritage/Editorial documentary** (Choolaah-type): scrims + 3-tier type stack (condensed accent caps headline / script subtitle + underline swash / clean sans body) + fixed corner marker + natural unfiltered photography + accent-only-in-type discipline. Spine: archive/dossier or journey. Proof slides carry real texture.
**Product/Food hero:** subject fills 55–75% of frame; named surface; appetite cues (steam, char, glisten); appetite triggers in-copy; pair slides share lens/DOF treatment; end card restraint. Spine: stage/spotlight.
**Data/Stat:** one stat per slide, number-as-hero; number in display face 200px+; label above, implication line below; max one chart per deck if truly needed. Accent marks the number — that's the ONE thing.
**Character/person-led:** face consistency via reference image + identity lock blocks; faceism — subject large on hook; gaze vectors carry the narrative; never alter a real person's face (brief law overrides all).
**Quote/Statement:** type-led deck; type IS the design (oversized letterforms, kinetic arrangement); background discipline flat color only; quote ≤3 lines per slide; one glyph-play moment max.
