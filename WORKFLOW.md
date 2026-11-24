# AI Film Production Workflow — End-to-End SOP

A step-by-step production pipeline for AI-assisted filmmaking. Synthesized from:

- The **AI Filmmaking Workflow SOP** (data ingestion → JSON prompt contracts → storyboard/pre-vis → hero generation → video routing → QC), and
- This library's own proven pipeline (production_agent studio engine + stage skills), as exercised on real productions (e.g. EP1 "The Iron Grip" build: world research doctrine, look bible, master shot prompts, VO pack, smart-cut hallucination control, generated-plates registry).

**How to use:** follow phases in order. Every phase has a **gate** — do not proceed until its outputs are locked. Route to the matching skill from `SKILL.md` at each step; this file is the *order*, the skills are the *method*.

---

## Phase Map

| Phase | Name | Output gate |
|---|---|---|
| 0 | Route & Setup | Workspace tree + engine/skill choice locked |
| 1 | Ingestion | All inputs consolidated, GIGO-proofed |
| 2 | Canon & Contract Layer | Look/World/Prop/Character masters + shot-prompt contracts |
| 3 | Storyboarding & Pre-Vis | Storyboard JSON + pre-vis grid approved |
| 4 | Hero & Asset Generation | Director visual lock + client sign-off |
| 5 | Video Generation Routing | Per-shot model + prompt routing decided |
| 6 | Generation & Hallucination Control | Clips generated per shot card |
| 7 | Post-Production & QC | Final review pass → editorial assembly |
| 8 | Marketing & Delivery | Package shipped |

---

## Phase 0 — Route & Setup

1. **Decide engine vs. stage skills.**
   - Whole film/episode from a story (Hindi PDF supported) → `00_STUDIO_ENGINE/production_agent/` (its 3-step gate: Template → Mode → Departments).
   - Single deliverable (one scene, one shot, one plate, one reel) → route directly via `SKILL.md` fast tables.
2. **Create the workspace tree** (`production_agent` style):
   ```
   workspace/projects/{PROJECT_TITLE}/
   ├── 00_Project_Bible_and_Canonical_State/
   ├── 01_Creative_Master_Suite/
   ├── 02_Technical_Master_Suite/
   ├── 03_Production_Logs_and_Audits/
   └── 04_Generated_Plates/          # generated asset registry
   ```
3. **Lock the project slate:** title, format (vertical 9:16 / horizontal 16:9), runtime, episode/series placement, target model family (probe model first — per-project, e.g. Seedance 2.5 vs flash-tier).

> **Gate 0:** workspace exists, project title sanitized, model family probed.

---

## Phase 1 — Ingestion

**Rule: consolidate all scene data before touching any model. Garbage in, garbage out.**

1. **Collect the source script / shot breakdown** (`.pdf`, `.txt`, `.docx`, or plain text). If it's a Hindi PDF, ingest via `production_agent` subsystem 00.
2. **Gather the six canonical inputs** (per the SOP's Step 1):
   - Shot angle; size/duration
   - Scene description
   - Color grading scheme
   - Director's visual references
   - Character/location/environment sheets (if any exist)
   - Production constraints (era, speed doctrine, props, vehicles, legal/safety notes)
3. **Build the World Research Doctrine** (binding, not optional): era locks, geography/measurements, vehicle specs, period signage, character visual DNA + NEVER-list — per-prompt CRITICAL block later, never doc-header only.
4. **Audit completeness** before writing any prompt (anti-truncation, zero placeholders).

> **Gate 1:** a consolidated input pack exists (script + references + doctrine) with no missing fields.

---

## Phase 2 — Canon & Contract Layer

Generate the **programmable rules** every downstream model will follow. These are the "rigidly formatted JSON" of the SOP's Step 2 — for us, the master documents.

1. **Story Bible / Canon** — `01_STORY_AND_CANON/story-bible-builder/` (or production_agent subsystem 00 with UUID registries). Locks characters, world, timeline.
2. **Look Bible** — grade scheme, palette locks, lens/emulsion language (`06_LOOK_AND_CINEMATOGRAPHY/anamorphic-look.md`).
3. **World / Location Masters + Shop Compositions** — per-scene plates, coverage angles, people-in-scene stills (`03_WORLDS_AND_PLATES/scenecraft-v1-SKILL.md`).
4. **Character / Vehicle / Prop sheets** — face locks, costume canon, plate text rules (`02_CHARACTERS_AND_CASTING/castkit-v1-SKILL.md`).
5. **Master Shot Prompts** — one per shot, with `@character` tags, acting blocks, motion direction + speed in visible world, era-lock CRITICAL block.

> **Gate 2:** all masters exist and are consistent (no contradictions between look, world, sheets).

---

## Phase 3 — Storyboarding & Pre-Vis

1. **Parse the shot breakdown → strict JSON** — use `92_SKILL_DEVELOPMENT/storyboard-parser-full-updated-skill-instruction-set.md`:
   - Provide the **storyboard template image** — it is the single source of truth for JSON parameter names/nesting/order/count.
   - Every shot object fills every template field; no missing keys, no placeholders, no `null`/`"N/A"`.
   - Run the mandatory internal self-check before output.
2. **Generate the storyboard visual grid** — input the JSON + template into your storyboard generator (Google Flow Agent per the SOP) or an image model of choice.
3. **Assemble pre-vis** — export board assets into a centralized pre-vis file (FigJam or equivalent). **Each frame must include its metadata:** camera angle & lens, voiceover line, short scene description.
4. **Approval gate** — director + client review the pre-vis grid before any hero generation.

> **Gate 3:** approved storyboard grid with per-frame metadata. No unapproved frame proceeds.

---

## Phase 4 — Hero & Asset Generation

1. **Generate hero images** on the **approved** storyboards only (image models on the board assets).
2. **Paste final images back into the pre-vis/FigJam file** for director visual lock and client sign-off.
3. **Register generated plates** — save to `04_Generated_Plates/` with a registry (character/scene/version); reuse locked plates as i2v/i2i references later.
4. **Character & scene locks** — for any character needing consistency across shots, produce the castkit sheet + character training set *before* video generation.

> **Gate 4:** hero images + plates signed off and registered; locks finalized.

---

## Phase 5 — Video Generation Routing

Route each shot to a model by task shape (SOP Step 6 table, extended with this library's stack):

| Model / Tool | Route here when… | Best for |
|---|---|---|
| **Google Flow** | Default routing | Cinematic realism, accurate physics, base narrative shots |
| **Kling** | Heavy lip-sync or complex motion | Character motion, multi-scene continuity |
| **Higgsfield AI (soul models)** | Precise camera control or edge cases | Character consistency, safety-filter tolerance, minor tweaks |
| **Seedance 2.5 Prompt Writer** | Any Seedance prompt — consult first | Full production-grade video prompts (`04_VIDEO_DIRECTION/`) |
| **shotcaller-v1** | One production-grade prompt, one clip, maximum control | Lipsync, extensions, strobe, dialogue from pasted script |
| **timed-prompts** | Multi-shot TIMECODED structure | Match cuts, cross-location continuity, 16:9→9:16 reframe |
| **Veo-class tools** | Default to menace-via-staging | Weapon/gunfire/injury chains get flag-filtered — stage around them |

**Per-shot prompt rules (non-negotiable):**
- One subject per shot, one camera intent.
- **Era/period lock as a per-prompt CRITICAL block**, never doc-header only.
- Motion direction + speed stated in visible world terms (e.g. "forward at 80 km/h").
- Hands pre-clamped; physics contacts happen **at the cut**; stage what models can't do.

> **Gate 5:** every shot has a routed model + a prompt matching its storyboard card.

---

## Phase 6 — Generation & Hallucination Control

1. **Generate per shot card**, one shot at a time. The storyboard card is the truth on double-fail.
2. **Smart-cut discipline** — when a shot needs multiple camera planes, split at the cut (`002A/B` style); never morph multi-plane moves inside one generation.
3. **Character consistency verification** — check plate text, face locks, costume canon against the sheets; if a generation breaks a lock, re-roll with the locked reference (never accept a broken plate "for now").
4. **Audit against the NEVER-list** (AI-bias corrections from the world doctrine).
5. **Risk audit** — for long sequences, run the full-clip risk audit (e.g. 35-clip) before assembly; flag shots needing regen or post-fix.

> **Gate 6:** all clips exist, match their cards, and pass the consistency audit.

---

## Phase 7 — Post-Production & QC

**Final review pass on all clips before editorial assembly:**

- [ ] Temporal consistency — no morphing or melting backgrounds
- [ ] Motion blur artifacts — none at cut points
- [ ] Lip-sync accuracy — matches VO/script
- [ ] Color & lighting — adheres to the original grading scheme
- [ ] Grade flip / freeze / boom (if used) are intentional edits, not generation artifacts

Then assemble:

1. **Editorial assembly / edit** — `08_POST_PRODUCTION_AND_EDITING/` (`ffmpeg-skill/` for cuts/reframes/captions/loudness; `ghost-editor/` for reels; `editorial-film-edit/` for soft archival; monorepo for pro-depth finishing + QC gates).
2. **Voiceover mix** — VO pack (Hindi + EN + cuesheet) timed to the cut; real runtime governs, not the script page math.
3. **Master exports** — per-platform (9:16, 16:9, 1:1), loudness normalized, captions embedded if required.

> **Gate 7:** final review pass clean; masters exported.

---

## Phase 8 — Marketing & Delivery

1. **Thumbnails / covers** — `07_MARKETING_AND_DELIVERY/higgsfield-youtube-thumbnail/`.
2. **Carousel / social deck** — `carousel-master/` (brand lock + references + script → one master JSON).
3. **Series consistency** — reuse palette/typography from brand references (`90_REFERENCE_KNOWLEDGE/prompt-knowledge/brand/`).

> **Gate 8:** package delivered with thumbnails, covers, and brand-consistent assets.

---

## Appendix A — Watermark Management (Google Flow)

Google Flow embeds a visible moving logo + invisible SynthID fingerprint. Cropping ruins framing. Use one of:

| Method | How it works | Notes | Limitation |
|---|---|---|
| **Google AI Ultra — official route** | Upgrade account tier; 720P video + 1080P upscale; watermark removed natively in Flow UI | If it persists, clear cache and re-login to force backend sync | Costly (~25000) |
| **Reverse-Alpha Blending — post route** | Tools like Erasio use local WebCodecs to mathematically reverse the alpha-blend — original pixels untouched, no re-encode | Keeps SynthID intact for AI-labeling compliance | Time consuming (~15 sec bulk per video) |
| **API Access — developer route** | Bypass the web UI; pipe JSON prompts directly into Google's API via AI Studio | API outputs are watermark-free by default | High management + bulk API |

---

## Appendix B — Reference Links

| Element | Reference resource |
|---|---|
| Camera Angle | [frameset.app/search](https://frameset.app/search) · [aicameracontrol.com](https://aicameracontrol.com/) · [eyecannndy.com](https://eyecannndy.com/) |
| Camera Movement | [aicameramovements.com/#finder](https://aicameramovements.com/#finder) |
| Emotion System | [animationreference.org/categories](https://animationreference.org/categories) |
| Color Grading | Visual image references / grade sheets |
| Character Sheet | Visual reference or idea → castkit sheet |
| Global Environment Values | Visual reference / script / set design → GEV.md |
| Negative Prompt | Maintain per model family |

---

## Appendix C — Gate Checklist (quick reference)

| Gate | Question |
|---|---|
| 0 | Workspace + route locked? |
| 1 | All inputs consolidated, no missing fields? |
| 2 | Canon/look/world/sheet masters consistent? |
| 3 | Storyboard grid approved with per-frame metadata? |
| 4 | Hero images signed off, plates registered? |
| 5 | Every shot routed + prompted per its card? |
| 6 | All clips match cards + pass consistency audit? |
| 7 | Final QC clean, masters exported? |
| 8 | Marketing package shipped? |
