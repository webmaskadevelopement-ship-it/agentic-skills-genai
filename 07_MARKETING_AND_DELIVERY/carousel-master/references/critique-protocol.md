# CRITIQUE PROTOCOL — the bounded pass

The system's self-check. ONE full pass + a veto re-check. No second full pass, no open-ended deliberation — the pass is what a senior art director does in the 60 seconds before sign-off, not an afternoon.

## 0. When it runs

- **Pass location:** after S3 BUILD, before delivery (S4). Fixes are applied INSIDE the pass, then delivery happens once.
- **Post-render pass:** when the user brings renders back, run §7 instead.
- **Bound:** one full rubric pass + targeted veto re-checks only. If two rounds of fixes ever fail the same veto, change strategy (simplify that slide's copy/composition) — never retry blindly.

## 1. Pass A — prompt audit (mechanical, fast)

| # | Check | Standard |
|---|---|---|
| 1 | Verbatim copy | Every `headline`/`body`/`script_line` string is the exact brief copy (trimmed only per type law), in quotes |
| 2 | Region coverage | Every visible region of each slide has a named zone or field |
| 3 | Counts & labels | Repeated elements are count-and-labeled |
| 4 | Safe zones | No text/logo zone crosses top/bottom 10% |
| 5 | Size floors | Body ≥36px, labels ≥24px, headline ≤2 lines (at 1080w equivalents) |
| 6 | Token budget | Mode A ≤12 fields/≤200 tokens; master ≤500 words |
| 7 | JSON validity | Braces, commas, quote-escaping valid |
| 8 | Engine fit | Ratio natively supported or crop strategy stated; ref count within engine cap |
| 9 | Reference addressing | Logo referenced with reproduce-exactly law; style refs carry the two-list rule |
| 10 | Positive phrasing | Constraints phrased positively; zone exclusions mirrored in `avoid` |
| 11 | Continuity | Marker identical per slide; continuity_thread present in slide 1 and paid off in last |
| 12 | No invented facts | Zero claims/prices/CTAs not in the brief |

## 2. Pass B — design rubric (10 dimensions, judge like a jury)

Score each 1–10 **starting at 6** — points above 6 must be earned by specific evidence; below 6 requires a specific defect. Adapted anchors: **6 = clean, consistent, but could be any brand's carousel · 7 = clear typographic system, intentional palette, one memorable composition · 8 = every slide composed, rhythm varied on purpose, second-read moment lands · 9 = inevitable — recognizable as this brand from a single cropped slide.**

1. **Hierarchy & focal point** — one focal point per slide, named; scan path follows importance; squint test passes.
2. **Typography** — scale derived from a ratio (steps ≥1.2 apart); floors met; ≤2 families; tracking rules honored.
3. **Layout & spacing** — margins ≥8%; zones respected; spacing breathes unevenly but deliberately; nothing floats arbitrary.
4. **Color discipline** — 60/30/10; accent marks one thing per slide; contrast ≥4.5:1 post-scrim; palette locked hex-identical.
5. **Set coherence** — the eight brand-world locks hold; deck reads as ONE campaign.
6. **Hook strength** — slide 1 opens an information gap, readable <1s at thumbnail, ≤7 words.
7. **Copy quality** — specific nouns, brand's own voice, no slop vocabulary, template check passed.
8. **Creativity** — concept spine visible; an idea that couldn't move to another brand; generic tropes discounted.
9. **Craft details** — grain/texture consistency, edge quality, optical details (tracking, alignment), swipe cue system present and quiet.
10. **Brand compliance** — logo law honored (reference, never redraw), marker exact, locked fields untouched.

**Weighted verdict:** Design 40% · Set coherence 25% · Creativity 20% · Copy 15%. Bands: **<6.5 not shippable — fix and re-score · 6.5–7.1 good · 7.2+ excellent.** Self-inflation guard: assume your self-score runs ~1 point optimistic; the vetoes below are the real gate, the score is for ranking and reporting only.

## 3. One-vote vetoes (ANY hit = fix before delivery, regardless of score)

1. Baked text at misspelling/garble risk (copy not verbatim in quotes, or >8-word headlines).
2. Logo drawn by the model instead of referenced from the user's upload.
3. Series marker missing, moved, or resized on any slide.
4. Any color outside the locked palette (or accent marking two things on one slide).
5. Text or logo in the top/bottom 10% safe zones.
6. Body text below the 36px floor (or headline >2 lines).
7. More than 2 type families.
8. Blue-purple/glow default past the measurable gate without brand mandate.
9. Invented claims, prices, statistics, or CTAs.
10. Simran-type identity violation: altering a real person's face/appearance when the brief locks it.

## 4. Counterfactual check (30 seconds)

State the deck's 1–2 DEFINING techniques (remove one → does the deck collapse into generic noise?). If you can't name any, the deck has no point of view — escalate the expressive move (usually: push the accent discipline, the type stack, or the scrim system further) rather than adding elements. Add the named techniques to `design_essence`.

## 5. Fix discipline

Apply all fixes INSIDE this pass. Then re-verify vetoes ONLY (10 mechanical checks, no re-scoring). Deliver. Report format at the bottom of the delivery message (one line, no essay): `Critique: score 7.1 · fixed: body copy trimmed S4, marker position locked · vetoes: 0`.

## 6. Blind-critic rule (when score matters)

Self-scores are not independent. When a delivery really matters (client-facing), optionally spawn a fresh subagent as blind critic: give it ONLY the rendered images (or the final prompts + lock), never the brief or intent; it scores §2 with evidence and a ranked fix list. The lower of self/critic scores wins. Say "self-scored" on the card when no blind pass ran.

## 7. Post-render QA (renders come back)

For EACH rendered slide check, in order:
1. **Text gate:** every baked word spelled exactly right? zero garbled glyphs/pseudo-letters? correct language/script? → any misspelling = veto, issue fix prompt.
2. **Marker gate:** present, same position/size on every slide?
3. **Palette gate:** colors within lock; accent discipline held.
4. **Layout gate:** safe zones respected; nothing clipped; floors met.
5. **Identity gate:** logo matches the uploaded reference; faces/products match their locks.
6. **Coherence gate:** grade and type treatment identical across slides.

Output a compact table: `slide | verdict | issue`. Any FIX slide gets a surgical prompt from §8 in the same reply. One table, no essays.

## 8. Revision grammar (surgical fixes — zero drift)

Fix ONE slide at a time. Never regenerate the deck for one slide. Template:

```json
{
  "task": "Regenerate slide N ONLY. All other slides stay exactly as approved.",
  "style_system": "<paste the ORIGINAL style_system block UNCHANGED — frozen>",
  "reference_images": "<same uploads as the original run: logo, refs>",
  "changes_only": ["the 1-2 specific changes for this slide"],
  "keep": ["everything else about this slide as it was: composition, marker, grade, type treatment"]
}
```

Rules: `style_system` is frozen — the fix prompt may not redesign globals. `changes_only` is 1–2 items max. If the same slide fails twice → **strategy change**: shorten that slide's text, simplify its composition, or switch its anchor/background mode — a third identical retry is banned. If ≥3 slides need the same global fix (e.g. marker drift), issue ONE corrected `style_system` + regenerate only affected slides, and note the root cause (the lock was ambiguous — tighten it).
