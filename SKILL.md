---
name: creative-production-router
description: |
  Master router for the organized creative production skill library. Use for ANY film,
  video or creative-production query: story bibles and canon, scene writing, short-drama
  episodes, character locks and casting, scene plates, Seedance/shotcaller video
  prompts, timecoded multi-shot cuts, block-code assembly, commercials, motion transfer,
  fight and dance choreography, anamorphic looks, thumbnails, posters, brand, model
  choice — plus post-production on real files: FFmpeg editing/captions/exports,
  talking-head reels, long-to-short extraction, editorial edits, Vox-style explainers,
  documentaries, pro finishing (720-skill monorepo) — plus the production_agent studio
  engine for whole-film department deliverables (Hindi PDF ingestion). Stages numbered
  in production order. Prompt-craft core makes zero API calls; 08/92 tools run locally
  on request only.
---

# Creative Production Router

You are routing a creative query into a library of self-contained child skills arranged
in **production order**: canon and dramatic structure BEFORE casting, BEFORE lens/grade,
BEFORE timecoded shots. Every child is prompt-craft only — model-agnostic or explicitly
labeled for its target model, zero API calls. When a task matches a child skill, LOAD
that child's file and follow it — do not improvise generic craft advice over an authored
method.

## Stage map (paths are authoritative)

| Stage | Contains |
|---|---|
| `00_STUDIO_ENGINE/` | `production_agent/` — the autonomous whole-film engine (11 subsystems, governance laws, live `workspace/`) |
| `01_STORY_AND_CANON/` | `story-bible-builder/`, `Higgsfield - Short Drama Screenwriter.md`, `higgsfield-prompt-engine/` |
| `02_CHARACTERS_AND_CASTING/` | `castkit-v1-SKILL.md`, `higgsfield-acting-skill/` |
| `03_WORLDS_AND_PLATES/` | `scenecraft-v1-SKILL.md` |
| `04_VIDEO_DIRECTION/` | `Higgsfield - Seedance 2.5 Prompt Writer.md`, `shotcaller-v1-SKILL.md`, `higgsfield-timed-prompts/`, `cinedance-block-library/`, `commercial-pipeline/`, `motiondojo-v1-SKILL.md`, `directing-workflow.md` (+ `_original_skill_archives/` zips) |
| `05_ACTION_AND_DANCE/` | `higgsfield-fight-scene/`, `dance-direction.md` |
| `06_LOOK_AND_CINEMATOGRAPHY/` | `anamorphic-look.md` |
| `07_MARKETING_AND_DELIVERY/` | `higgsfield-youtube-thumbnail/`, `carousel-master/` |
| `08_POST_PRODUCTION_AND_EDITING/` | `ffmpeg-skill/`, `ghost-editor/`, `claude-shorts/`, `editorial-film-edit/`, `vox-motion-graphics/`, `fern-documentary/`, `OpenMontage/` (+ `_original_skill_archives/`) |
| `90_REFERENCE_KNOWLEDGE/` | `prompt-knowledge/` (brand, image, video, model catalog, local scripts) + `open-higgsfield-app/` (model/voice catalogs, prompt-builder logic, 20 cinema-look plates) + `higgsfield-open-studio/` (self-contained Higgsfield craft library: 25 sub-skills, MCSLA prompt formula, 18 templates — user-added 2026-11-05) |
| `91_WORKED_EXAMPLES/` | `worked-examples/` (reference only — never inject into user projects) |
| `92_SKILL_DEVELOPMENT/` | `skill-development/` — internal skill factory (generators, blueprints, editing templates) incl. `skills/autonomous-post-production-ai-monorepo/` (720-skill finishing system); `storyboard-parser-full-updated-skill-instruction-set.md` — standalone storyboard parser |

## 1. Fast routing table

### Full studio pipeline (the engine)

| The query is about… | Route to |
|---|---|
| Producing a WHOLE film/episode from a story or script (Hindi PDF supported): screenplay, master shot breakdown, voiceover system, storyboarding file, color/DI bible, sound design, character sheets, prop list, location design — or any ONE department deliverable at production depth | `00_STUDIO_ENGINE/production_agent/` — follow ITS `SKILL.md` orchestrator: Phase 1 ingestion → Phase 2 STOP & selection gate (Template T1–T3 / Mode M1–M3 / Departments 1–9 or All) → Phase 3 subsystem execution. Do NOT improvise around its gate or laws. |
| Hindi voiceover / literary narration: writer emulation (Gulzar, Premchand, Manto, Renu…), lexicon registers, navarasa emotion architecture, Devanagari prosody/DSP | `00_STUDIO_ENGINE/production_agent/03_voiceover_subsystem/` (usable standalone for VO-only work) |
| Story ingestion, canonical story bible with UUIDs, shot-count estimation, entity registries | `00_STUDIO_ENGINE/production_agent/00_story_ingestion_subsystem/` |
| Production templates & pacing (6–7 min episode @25–27 shots/min, 60s micro-short, 26–30 min episodic) | `00_STUDIO_ENGINE/production_agent/10_template_library_subsystem/` |

When routed into `production_agent`, its own `00_governance_and_laws/` (anti-truncation,
two-brain protocol, banned tokens, chunking engine, UUID continuity, dual rendering)
govern the work. Note: it is script-grounded — never inject its reference examples
(Raghav Sharma, Varanasi courtyards…) into a user project.

### Story, canon & episodes

| The query is about… | Route to |
|---|---|
| Story bible, canon doc, locking characters/world, stopping prompt drift, "turn my story into a skill" | `01_STORY_AND_CANON/story-bible-builder/` (interview-driven; its output feeds EVERY other skill) |
| Short drama / micro-drama / AI series episode from scratch (idea → assets → script → per-clip prompts), 100 premise picker | `01_STORY_AND_CANON/Higgsfield - Short Drama Screenwriter.md` |
| Scene/sequence writing or auditing, dramatic structure, "is this scene working" | `01_STORY_AND_CANON/higgsfield-prompt-engine/` (Goal → Obstacle → Tactic → Reversal → Value Shift) |
| Practical directing of one scene: brief + reference files → shot brief + video prompt, staging, eyelines, continuity | `04_VIDEO_DIRECTION/directing-workflow.md` |

### Characters & casting

| The query is about… | Route to |
|---|---|
| Design/lock a character, face lock, hair/marks/expression additions, outfits on a character, outfit swap, character/turnaround sheets (Nano Banana Pro & image models) | `02_CHARACTERS_AND_CASTING/castkit-v1-SKILL.md` (five stations, 18% gray field) |
| Character performance: dialogue delivery, emotional beats, "eyes dead/glassy", listening, reactions | `02_CHARACTERS_AND_CASTING/higgsfield-acting-skill/` |

### Worlds, plates & first frames

| The query is about… | Route to |
|---|---|
| Environment/location/set plate, coverage angles, people-in-scene stills, first frame for video | `03_WORLDS_AND_PLATES/scenecraft-v1-SKILL.md` |
| A general image prompt (any subject), prompt phrasing rules, i2i edits | `90_REFERENCE_KNOWLEDGE/prompt-knowledge/image/prompt-engineering.md` |

### Video direction (pick by shape of the task)

| The query is about… | Route to |
|---|---|
| Seedance prompting technique in general, "write a Seedance prompt", single standalone prompt | `04_VIDEO_DIRECTION/Higgsfield - Seedance 2.5 Prompt Writer.md` (consult FIRST for any Seedance prompt) |
| Full production-grade cinema prompt on Seedance 2.0/2.5: 16-slot spine, action/choreography/performance/strobe, lipsync, dialogue from pasted script, video extensions | `04_VIDEO_DIRECTION/shotcaller-v1-SKILL.md` |
| Exact timecodes, fixed dialogue, multi-location continuity, match cuts, seating/blocking maps, 16:9→9:16 reframe/outpaint | `04_VIDEO_DIRECTION/higgsfield-timed-prompts/` |
| User sends a block-code brief (TRICK/FORMAT/ASSETS/BLOCKS, CAM-*/OPT-*/GRADE-* codes, Karima face lock, Russian ok) | `04_VIDEO_DIRECTION/cinedance-block-library/` |
| End-to-end commercial: asset prompts → assembled video prompt → diagnosing a broken generation | `04_VIDEO_DIRECTION/commercial-pipeline/` (3 stages, fix playbook in `references/`) |
| Motion transfer: copying movement/camera from a reference video onto new characters (Genjutsu), mouth lock | `04_VIDEO_DIRECTION/motiondojo-v1-SKILL.md` |
| Storyboard prompts: parse a shot breakdown (PDF/txt/docx or plain text, with a storyboard template image as parameter authority) into storyboard JSON + per-shot frame-generation instructions | `92_SKILL_DEVELOPMENT/storyboard-parser-full-updated-skill-instruction-set.md` |

### Dance & action

| The query is about… | Route to |
|---|---|
| Dance choreography: breaking down a dance clip, footwork/weight-transfer timecodes, stiff/robotic results, foot sliding | `05_ACTION_AND_DANCE/dance-direction.md` |
| Fight/brawl/combat choreography (esp. Jeet Kune Do, Wing Chun) | `05_ACTION_AND_DANCE/higgsfield-fight-scene/` (moves-catalog + sources/) |

### Look & cinematography

| The query is about… | Route to |
|---|---|
| Anamorphic look, lens/focal choice, oval bokeh, streak flares, film stock, "looks like 3D render" | `06_LOOK_AND_CINEMATOGRAPHY/anamorphic-look.md` |
| Visual style choice for a video/film (collage, diorama, storybook…) | `90_REFERENCE_KNOWLEDGE/prompt-knowledge/video/styles.md` |

### Post-production & editing (real files, local tools)

| The query is about… | Route to |
|---|---|
| Editing real video/audio files locally with FFmpeg: cut/trim/join, reframe (9:16/1:1), speed, captions/subtitles (SRT/ASS/animated/karaoke), overlays, lower-thirds, silence removal, multicam/external-mic sync, loudness (LUFS), HDR→SDR, LUTs, music ducking, platform exports, scene detection, highlight reels, contact sheets | `08_POST_PRODUCTION_AND_EDITING/ffmpeg-skill/` (46 python/ffmpeg tools; `--help` per script is the flag list) |
| Turning a raw talking-head phone recording into a finished vertical reel: best-take selection, pause trimming, word-timed captions that avoid the face, SFX, named styles/presets (Clean OS, Seoul list, Kinetic doc…) | `08_POST_PRODUCTION_AND_EDITING/ghost-editor/` |
| Extracting viral short clips from a long video (transcription, Claude-scored segments, interactive picks, Remotion caption styles Bold/Bounce/Clean, platform-optimized exports) | `08_POST_PRODUCTION_AND_EDITING/claude-shorts/` (run `npm install` in `remotion/` first — node_modules intentionally not shipped) |
| Editing footage in a soft archival editorial style (bundled video/photo references, kinetic text, film grain, bloom, masks, presenter splits) | `08_POST_PRODUCTION_AND_EDITING/editorial-film-edit/` |
| Planning/producing/revising a Vox-style editorial mixed-media or paper-diorama explainer (research, narration, scene plans, shared visual reference, typography, VO, sound) | `08_POST_PRODUCTION_AND_EDITING/vox-motion-graphics/` |
| Fern-style documentary production (narration, style investigation, style incident references) | `08_POST_PRODUCTION_AND_EDITING/fern-documentary/` |
| An agent-driven editing application platform (own skills tree: `skills/core/creative/meta/pipelines`, tools, schemas, ink-theater, remotion-composer) | `08_POST_PRODUCTION_AND_EDITING/OpenMontage/` (start at `AGENT_GUIDE.md`/`PROJECT_CONTEXT.md`) |
| Deterministic professional post-production finishing: ingest dailies, editorial craft & pacing, color (IRE/vectorscope math), sound (BS.1770 loudness), subtitling (CPS/CPL bounds), VFX/motion, mastering, 9 automated QC gates | `92_SKILL_DEVELOPMENT/skills/autonomous-post-production-ai-monorepo/` (720 schema-locked skills `[001]`–`[720]`; follow its own SKILL.md routing) |
| Building NEW skills internally: generators (clusters/leaf skills/routers), blueprints, editing templates, filmcraft CLI bridge | `92_SKILL_DEVELOPMENT/skill-development/` (internal factory — not for end-user production queries) |

These are operational tools, not prompt-craft: run their scripts only when the user
asks for that operation on their files; never initiate cloud/API calls on their behalf.

### Marketing & delivery

| The query is about… | Route to |
|---|---|
| Carousel, multi-slide social deck (IG/LinkedIn swipe post), slide-by-slide image prompts from brand lock + references + script | `07_MARKETING_AND_DELIVERY/carousel-master/` (fixed intake → ONE master JSON, 1-2 min runtime) |
| Thumbnail / episode cover / headline text bake | `07_MARKETING_AND_DELIVERY/higgsfield-youtube-thumbnail/` |
| Poster, pitch deck, social promo, palette, typography, series-wide consistency | `90_REFERENCE_KNOWLEDGE/prompt-knowledge/brand/` |
| UGC/presenter/talking-character ad framing | `90_REFERENCE_KNOWLEDGE/prompt-knowledge/video/presenter.md`, `talking-characters.md`, `marketing-modes.md` |

### Models, audio & local tools

| The query is about… | Route to |
|---|---|
| Which model/tool for a job; model capabilities | `90_REFERENCE_KNOWLEDGE/prompt-knowledge/model-catalog.md` + `video/video-generation-model-notes.md`; per-model prompt examples/options for 221 models in `90_REFERENCE_KNOWLEDGE/open-higgsfield-app/model-prompt-guide.md` |
| Cinema look vocabulary (anamorphic/70mm/16mm/halation/bokeh variants) | `90_REFERENCE_KNOWLEDGE/open-higgsfield-app/cinema-prompt-modifiers.md` — camera/lens/focal/aperture → prompt-phrase compiler + named webp plates in `public-assets-cinema/` (pairs with `06_LOOK_AND_CINEMATOGRAPHY/anamorphic-look.md`) |
| i2v start/end frames, reference roles per model | `90_REFERENCE_KNOWLEDGE/prompt-knowledge/video/media-inputs.md` |
| Narration timing / 10s blocks / voice cues | `90_REFERENCE_KNOWLEDGE/prompt-knowledge/video/production.md` |
| Music/song prompt meter (Suno-type) | `90_REFERENCE_KNOWLEDGE/prompt-knowledge/video/song.md` |
| Captions, clip assembly, trim, voice-timing gates | `90_REFERENCE_KNOWLEDGE/prompt-knowledge/video/captions.md` + `video/scripts/` (14 local ffmpeg/python tools) |
| Scene/narration writing, story beats | `90_REFERENCE_KNOWLEDGE/prompt-knowledge/video/prompts.md`, `picture-story.md`, `creative.md` |
| Real worked examples of timed prompts | `91_WORKED_EXAMPLES/worked-examples/Recreate-prompts/`, `Scene-source-prompts/` (reference only) |

### Higgsfield platform craft (the open-studio library)

`90_REFERENCE_KNOWLEDGE/higgsfield-open-studio/` is a self-contained library with its OWN
router (`SKILL.md`, 25 sub-skills + hard rules). When a route below fires, load ITS
`SKILL.md` first and follow its routing table and pre-delivery checklist.

| The query is about… | Route to |
|---|---|
| Named Higgsfield presets (camera/motion/soul), platform vocabulary, the MCSLA video-prompt formula (Model·Camera·Subject·Look·Action), prompt length discipline | `higgsfield-open-studio/SKILL.md` + `vocab.md` (root SKILL.md and `skills/higgsfield-prompt/` are its mandatory minimum read) |
| Genre starter prompts: cinematic action, horror, fashion editorial, sci-fi VFX, portrait intro, landscape establishing, romantic, comedy/social, dance, product UGC | `higgsfield-open-studio/templates/01–10-*.md` |
| Seedance shot layouts: single-character position, multi-character anchor, top-down map, two-character worked example, anime | `higgsfield-open-studio/templates/seedance/` |
| Text overlays: speech bubbles, subtitles, slogans | `higgsfield-open-studio/templates/text-overlays/` |
| GPT Image 2.0 image workflows: reference sheets, static ads | `higgsfield-open-studio/skills/higgsfield-gpt-image-2/` |
| Content-factory publishing workflow, marketing studio, one-click Apps recipes | `higgsfield-open-studio/skills/higgsfield-content-factory/`, `higgsfield-marketing-studio/`, `higgsfield-apps/` |
| Diagnosing a bad generation on Higgsfield-class models | `higgsfield-open-studio/skills/higgsfield-troubleshoot/` + root `production-benchmarks.md`, `prompt-examples.md` |
| Platform model lineup / credit tiers (reference only) | `higgsfield-open-studio/model-guide.md` |

Caveats: (1) its CLI/MCP/preflight rules assume a Higgsfield subscription the user does
NOT have — use the craft (MCSLA, named presets, vocab, templates), skip execution steps;
(2) its `specs/model-specs.yaml` and `build_index.py` are NOT in this copy — when a rule
says "verify against specs", fall back to `vocab.md`/`model-guide.md` or this library's
`open-higgsfield-app/model-prompt-guide.md` (221 models).

- **Full film/episode from a story (deepest path):** `00_STUDIO_ENGINE/production_agent/`
  end-to-end — its ingestion → gate → subsystem loop produces all department deliverables.
  The lighter stage skills then handle the single-prompt generation layer (castkit
  character plates, scenecraft first frames, Seedance/shotcaller clip prompts,
  timed-prompts multi-shot cuts) from those deliverables.
- **New series/world (step 0):** `01_STORY_AND_CANON/story-bible-builder/` FIRST → its
  canon SKILL.md becomes context for every skill downstream. (For Hindi-cinema depth,
  production_agent's subsystem 00 does the equivalent with UUID registries — use ONE of
  the two, not both.)
- **Short drama episode:** Short Drama Screenwriter (package) → castkit (character
  locks) → scenecraft (location/first frames) → Seedance Prompt Writer or shotcaller
  (per-clip prompts) → video/scripts (assembly) → youtube-thumbnail.
- **Narrative scene → screen:** prompt-engine → acting-skill → anamorphic-look →
  timed-prompts or shotcaller → scripts.
- **Action scene:** prompt-engine → fight-scene → acting-skill (reactions) →
  anamorphic-look → shotcaller/timed-prompts.
- **Commercial:** `04_VIDEO_DIRECTION/commercial-pipeline/` orchestrates end-to-end
  (it internally uses castkit-style asset prompts + a structured video prompt + fix
  playbook).
- **Dance or motion-copy clip:** motiondojo (if motion reference video) or
  dance-direction (if footwork brief) → scenecraft (world plate) → Seedance prompt.
- **Clip → finished deliverable:** generation (04) produces clips → `08_POST_PRODUCTION_AND_EDITING/`
  finishes them (ffmpeg-skill for file ops/captions/exports; ghost-editor for reels;
  claude-shorts for shorts extraction; monorepo for pro-depth finishing + QC gates) →
  `07_MARKETING_AND_DELIVERY/` packages the master (thumbnails, covers, brand).
- **Single image:** `90_REFERENCE_KNOWLEDGE/prompt-knowledge/image/prompt-engineering.md`
  (+ anamorphic-look.md if cinematic) → brand/ for series look.

Order matters: canon and dramatic structure BEFORE casting, BEFORE lens/grade, BEFORE
timecoded shots. Never let a late-stage skill change decisions an earlier skill locked
without saying so.

## 3. Choosing between the video-director cluster

They overlap on purpose — pick by task shape:
- `Higgsfield - Seedance 2.5 Prompt Writer.md` — default technique base for ANY Seedance prompt.
- `shotcaller-v1` — one production-grade prompt, one clip, maximum control (lipsync, extensions, strobe).
- `higgsfield-timed-prompts` — multi-shot TIMECODED structure, match cuts, cross-location continuity, reframe/outpaint.
- `cinedance-block-library` — user already thinks in block codes; assemble from the library.
- `commercial-pipeline` — the whole ad from nothing, including diagnosing bad generations.
- `directing-workflow` — lightweight scene direction/revision when none of the heavy spines are needed.

When two fit, ask the user which format they want, or default to the lighter one and
escalate on feedback.

## 4. Ground rules

1. Read the routed child's file fully before producing output; children contain bespoke,
   authoritative definitions — never replace them with textbook summaries.
2. Load `references/` only as the query needs (fight-scene's moves-catalog vs sources/
   digests; commercial-pipeline's fix-playbook when diagnosing).
3. All prompts leave the library in English and portable form; the user pastes them into
   whatever generator they pay for. Never attempt a generation call, cost check, or API
   authentication.
4. Keep asset-handle conventions when extending examples (`@char_alex2` in
   timed-prompts; `<<<image_N>>>` in motiondojo; block codes in cinedance).
5. Executable tooling, in two tiers. Prompt-craft tier (safe, run freely when a task
   needs them): `90_REFERENCE_KNOWLEDGE/prompt-knowledge/video/scripts/` and
   `00_STUDIO_ENGINE/production_agent/03_voiceover_subsystem/scripts/` — pure local
   python, plain file arguments. Operational tier (stage 08/92: ffmpeg-skill's 46
   tools, ghost-editor, claude-shorts, OpenMontage, the monorepo): real editors/render
   pipelines — run only on explicit user request for that operation; some need one-time
   setup (`npm install`, `requirements.txt`) since regenerable bulk was not shipped.
6. `production_agent/` has its own interactive gate and must STOP for user selections
   (Template / Mode / Departments). Its `workspace/` holds live project state — write
   there only as its protocol directs.
7. `91_WORKED_EXAMPLES/` is pedagogical only — never copy its content into a user project.
8. `04_VIDEO_DIRECTION/_original_skill_archives/` and
   `08_POST_PRODUCTION_AND_EDITING/_original_skill_archives/` hold the original
   `.skill` zip packaging; the extracted folders next to them are canonical.
9. Stage 08/92 units were merged from `/Volumes/DISK 1/AGENTS TRAIN/` (2026-11-05)
   with regenerable bulk excluded (claude-shorts `node_modules`, OpenMontage agent
   session state `.agents/.claude/.cursor/.codex`, git internals). The AGENTS TRAIN
   originals remain untouched and authoritative for those excluded parts.

## 5. Adding new skills to this library

1. Drop the skill (folder or single .md) into the stage folder matching its pipeline
   role — keep its unit name unchanged so internal relative references stay intact.
2. Add a route line to the matching table in section 1, phrased by task shape.
3. If it introduces a new pipeline stage rather than fitting an existing one, insert a
   new numbered folder (e.g. `08_…`) and extend the stage map — do not renumber
   existing stages.
4. Standalone-triggering skills need a frontmatter description ≤900 characters;
   over ~1024 and the loader silently drops them.

## 6. If nothing matches

If the query is creative-production adjacent but none of the above fits (podcast audio,
3D printing, web dev), say so plainly: this library does not cover it. For anything
about Higgsfield's own CLI, accounts, or credits: the user has no subscription — answer
from `90_REFERENCE_KNOWLEDGE/prompt-knowledge/model-catalog.md` knowledge only and
route the actual work to a portable equivalent.
