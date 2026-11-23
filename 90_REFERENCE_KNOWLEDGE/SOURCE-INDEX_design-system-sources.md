# SOURCE INDEX — Design-System Sources for the Carousel System Build

Full-drive survey (2026-11-05): 573 SKILL.md files across 4 locations. This index maps every
source worth mining to the 6 build items of the carousel system:

| # | Build item | What it fixes |
|---|---|---|
| B1 | ZERO-INTAKE engine | consultant behavior; system must infer + decide + state assumptions |
| B2 | DESIGNER BRAIN | craft depth (type scale math, spacing, hierarchy, restraint) — the taste gap |
| B3 | BOUNDED CRITIQUE PASS | no self-check before delivery; both past disasters |
| B4 | REFERENCE GRAMMAR + MODEL PLAYBOOK | logo/style/product reference discipline; engine choice |
| B5 | QA GATE + REVISION GRAMMAR | post-render acceptance; surgical per-slide fixes |
| B6 | BRAND MEMORY | (deferred) per-brand locks, style-ref kits |

---

## TIER 1 — mine fully (distill into system files)

### IRIS Visual Taxonomist — `AGENTS TRAIN/visual_taxonomy/iris-agentic-skill/`
The drive's hidden designer brain. Feeds B2 + B3 + B5.
- 35-parameter decomposition schema (Gestalt, optics, ACEScc/DaVinci color science, substrate, semiotics) — replaces vague jargon ("clean/moody/vibey") with measurable params
- `system/guides/graphic_design_swiss_typography.md` — 12-column Swiss grids, hierarchy, baseline locks
- `system/guides/semiotic_rhetoric_and_neuroaesthetics.md`
- `system/presets/master_reference_library_50.json` — 50 canonical decompositions (taste priors)
- `system/protocols/counterfactual_collapse_protocol.md` — QA test: find the one technique whose removal collapses the image
- `system/protocols/generative_prompt_compiler.md` — params → model payloads
- Companion: `taxonomy_filebase/` 8 pipeline skills (vision ingest → bounding-box evidence → counterfactual removal); `COLOR SYSTEM.md` (74-color token system, 4-tier + 9-step tonal scales)

### tasteskill.dev — `/Volumes/DISK 1/AGENT SKILLS/Skill Repo/tasteskill.dev/skills/`
Feeds B2 + B3. The anti-slop image-art-direction blueprint.
- `imagegen-frontend-web/SKILL.md` (987 lines) — one-image-per-frame rule; Combinatorial Variation Engine (theme/typography-character/hero-architecture/narrative-spine/"second-read moment"); 12 composition anchors ("left-text/right-image is the most overused AI pattern"); 12 background modes; palette lock across frames; 8-category AI-slop ban list; 21-point clarity check
- `taste-skill/SKILL.md` (1206 lines) — variance/density dials; serif discipline (creative-brief-serif = #1 AI tell); LILA rule (no purple/blue glow); banned-hex families + 7 rotation alternatives; one-accent lock
- `brandkit/SKILL.md` (798 lines) — 3x3 brand-board panel system; logo mechanisms; board rhythm
- `soft-skill/SKILL.md` — "$150k agency" spec: banned elements, macro-whitespace, pre-output checklist

### CPS brand craft — `/Volumes/DISK 1/CREATIVE PRODUCTION SKILL/90_REFERENCE_KNOWLEDGE/prompt-knowledge/brand/`
Feeds B1 + B2 + B4 + B5. Already in-library; the backbone.
- `brand-lock.md` — fixed/proposed/unknown field states + evidence labels; verbatim `[BRAND LOCK — DO NOT DEVIATE]` prompt block; reference role-labeling ("Image 1: official logo"); per-format override rules; revision propagation
- `brandkit-design-brain.md` — Creative DNA compile (Product Truth / Audience Desire / Central Mechanism / Forbidden Clichés); every decision traces to a DNA field; one-expressive-move rule; 10-criteria internal selection rubric; CRITIQUE_ESSENTIAL_KIT (9-question coherence check); rename-test ("could another brand use this unchanged?")
- `typography.md` — type-system-not-font-names; pairing evaluation checklist; two-family cap; deterministic-typography doctrine (exact fonts = editor-applied, never baked-and-hoped)
- `social-templates.md` — carousel cover/body/CTA modules; verbatim-copy law; typography specimen PNG workflow; consistency & QA checklist; GPT-Image 4:5 crop workaround
- `palette.md` — 3 meaningfully-different options; roles + contrast-safe pairing

### layout/typography prompt craft — `90_REFERENCE_KNOWLEDGE/higgsfield-open-studio/skills/higgsfield-gpt-image-2/`
Feeds B2 + B4 + B5.
- `SKILL.md` — Format A JSON layout craft: position-scoped regions, count-and-label pattern, inline typography callouts ("Space Grotesk Bold Caps"), [Typography System] block; 6-item pre-delivery checklist
- `static-ads-workflow.md` — fractional coordinate zones (text_zone/product_zone/button_zone); top/bottom-10% safe-zone rule (IG/TikTok UI overlays); wireframe intermediation (inherit layout from reference without its identity); brand-vs-structure two-list rule (brand tokens ALWAYS override reference visuals)
- `reference-sheet-workflow.md` — GLOBAL IDENTITY LOCK + GRAPHICS/BRANDING LOCK paste blocks

## TIER 2 — targeted mining (specific sections)

### Critique & QA rubrics — feeds B3 + B5
- `Skill Repo/design-review/design-review/skills/design-review/checklist.md` — 10-dimension measurable rubric: hierarchy (one focal point, scan path), type (5-7 step scale, ≥1.2 ratio, 45-75ch measure), spacing (4/8px), contrast (4.5:1/3:1); severity tiers Blocking/Important/Polish; What/Why/Fix format. NOTE: strip telemetry curl from its SKILL.md
- `Skill Repo/juliobsz-skills/jury/references/quality-bar.md` + `jury/SKILL.md` — Awwwards-jury blind critique: weighted scoring (Design 40/Usability 30/Creativity 20/Content 10), anchored 1-10 descriptors ("6 = could be any template; 9 = recognizable from a crop"), no-evidence-no-points, fresh-subagent critic brief
- `Skill Repo/huashu-art-motion/references/16-风格演示95分协议.md` — scored acceptance protocol, signature-feature must-have lists, one-vote vetoes, self-score-inflation guard (+10 observed)
- `Skill Repo/huashu-art-motion/references/色板.md` — 8 locked 6-slot palettes; measurable blue-purple ban (hue 225-300° + sat ≥0.30 over 30% frame = red light)
- `Skill Repo/claude-plugins-official/plugins/frontend-design/` — Anthropic official taste skill: AI-default calibration list (cream+serif+terracotta, SaaS-card kit, ALL-CAPS eyebrows = tells); "spend boldness in one place"; Chanel rule; plan→critique-against-brief two-pass
- `Skill Repo/interface-design/.claude/skills/interface-design/SKILL.md` — type-scale ratios (1.2/1.25/1.333), weight-beats-size, 60/30/10, squint test, swap/signature/token self-tests; `design-deslop` command
- `Skill Repo/anti-slop/skills/antislop-ui/SKILL.md` — named visual slop patterns each with fix (Generic Blue-Purple Gradient, Glow Everywhere, Copy-Paste Cards, Colored Left Stripe…)
- `90_REFERENCE_KNOWLEDGE/higgsfield-open-studio/skills/shared/negative-constraints.md` — artifact→cause→prevention-phrase tables
- `90_REFERENCE_KNOWLEDGE/higgsfield-open-studio/skills/higgsfield-gpt-image-2/SKILL.md` pre-delivery checklist + `DISCIPLINE.md` (iteration-is-craft: ~1% acceptance rates are normal — the loop IS the craft)

### Zero-intake / decide-with-motive — feeds B1
- `open-higgsfield-app/netlify-prompt-builder/prompt-builder.js` (69 lines, in 90_REFERENCE_KNOWLEDGE) — PLAN → GRILL two-pass: "aggressively inspect for ambiguity… resolve gaps using conservative professional defaults. **Do not ask the user questions.**"
- `Skill Repo/hue/SKILL.md` (869 lines) — 16-phase brand→design-language pipeline; token model schema — pattern for inferring a full design world from thin input
- `Skill Repo/ecc/skills/taste*` — distill-taste-from-references-into-reusable-spec pattern

### Copy craft (slide text) — feeds B2 + B3
- `Skill Repo/stop-slop/` — prose de-slop: 8 rules, 50-point 5-dimension scoring (below 35 = revise)
- `Skill Repo/humanize-skills/` — rhythm-first humanizing, core-rules.md
- `Skill Repo/anti-slop/skills/antislop-copywriting/SKILL.md` — copy slop taxonomy (Empty AI Vocabulary, Significance Inflation, Rule-of-Three Overuse…)

### Social geometry — feeds B2 + B4
- `Skill Repo/ui-ux-pro-max/.claude/skills/banner-design/SKILL.md` + references — platform size tables, safe-zone 70-80% rule, text <20% for Meta ads, max 2 fonts, 22 art-direction styles
- `prompt-knowledge/image/prompt-engineering.md` — ≤200 tokens; i2i "describe the change"; positive phrasing over negative prompts
- `FINAL_SKILLS/higgsfield-youtube-thumbnail/references/thumbnail-frameworks.md` (in CPS 07) — 14+ hook-concept frameworks + truthfulness law — hook-slide mechanics

### Identity consistency — feeds B4
- `FINAL_SKILLS/castkit-v1-SKILL.md` (CPS 02) — face locks, 3-panel sheets, 18% gray field — mascot/person continuity across slides

## TIER 3 — model & architecture references
- `90_REFERENCE_KNOWLEDGE/prompt-knowledge/model-catalog.md` — AUTHORITATIVE engine table: GPT Image 2.5 = design/typography/on-image text default; Nano Banana 2 Pro = max sharpness + native 4:5 + 14 refs; Recraft V4.1 = logos/vector/controlled palette; Seedream 5.0 = complex layout; Flux Kontext = edits; Ideogram v3 `Design` style = typography-strong alternative
- `higgsfield-open-studio/skills/higgsfield-models/SKILL.md` — decision flowchart keyed to need (cross-check versions against catalog)
- `open-higgsfield-app/model-prompt-guide.md` — per-model enums; Nano Banana native 4:5 (1k/2k/4k); reference-count limits per model
- `google-labs-design-md-internal/PHILOSOPHY.md` — "design lives in prose, not tokens" — the DESIGN.md brief pattern
- `AGENTS TRAIN/higgsfield_edit/SKILLS/ghost-editor/taste.json` — learned-taste store pattern ("corrections recorded as priors") — future B6 mechanism
- `AGENTS TRAIN/higgsfield_edit/SKILLS/skill-development/editing-templates/` — 39 fixed-rubric skeletons (anti-shallowness rules pattern) for authoring new per-deck-type playbooks

## EXCLUSIONS (checked, not relevant)
`Skill Repo`: gravitas, ponytail, rea, clone-website, gsap-skills-official, superpowers, mattpocock-skills, find-skill, task-observer, claude-mem-skills, deepseek-harness-internal, motionsites, dimensional-drawing, shadcn-skills (code-scoped). `DEV-PIPELINE`: dev process only (its D03 README is the index that confirmed the Skill Repo). `TEMP PERSONAL`: none.
