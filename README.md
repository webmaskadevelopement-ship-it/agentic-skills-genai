# CREATIVE PRODUCTION SKILL — Organized Production Library (v1)

The organized clone of the AI film production skill library (source of truth:
`/Volumes/DISK 1/DATA/WEB SERIES PRODUCTION/SKILL_DATA/FINAL_SKILLS/`, cloned 2026-11-05).
Everything here works **without any Higgsfield account, CLI, or subscription** — prompts
are model-agnostic or explicitly labeled for their target model; stop before any
generation call and hand the prompt to the user.

Routing lives in [`SKILL.md`](SKILL.md) (`creative-production-router`) — read it first.

Provenance: [higgsfield-ai/skills](https://github.com/higgsfield-ai/skills) (2026-10-30)
+ bespoke film-craft skills (2026-10-30) + Joey's production suite & standalone skills
(2026-10-31). See `LICENSE`.

## Stage order = production order

Skills are numbered by where they sit in the production lifecycle. Canon and dramatic
structure come BEFORE casting, BEFORE lens/grade, BEFORE timecoded shots — a later stage
never silently overrides a decision an earlier stage locked.

| Stage | Role | Skills |
|---|---|---|
| `00_STUDIO_ENGINE/` | Whole-film/episode engine | `production_agent/` (11 subsystems + governance + live workspace) |
| `01_STORY_AND_CANON/` | Story, script, canon | `story-bible-builder/`, Short Drama Screenwriter, `higgsfield-prompt-engine/` |
| `02_CHARACTERS_AND_CASTING/` | Faces & performance | `castkit-v1-SKILL.md`, `higgsfield-acting-skill/` |
| `03_WORLDS_AND_PLATES/` | Locations & first frames | `scenecraft-v1-SKILL.md` |
| `04_VIDEO_DIRECTION/` | Clip & cut prompts | Seedance 2.5 Prompt Writer, `shotcaller-v1-SKILL.md`, `higgsfield-timed-prompts/`, `cinedance-block-library/`, `commercial-pipeline/`, `motiondojo-v1-SKILL.md`, `directing-workflow.md` |
| `05_ACTION_AND_DANCE/` | Choreography | `higgsfield-fight-scene/`, `dance-direction.md` |
| `06_LOOK_AND_CINEMATOGRAPHY/` | Lens & grade | `anamorphic-look.md` |
| `07_MARKETING_AND_DELIVERY/` | Packaging | `higgsfield-youtube-thumbnail/` |
| `08_POST_PRODUCTION_AND_EDITING/` | Real-file editing & finishing | `ffmpeg-skill/`, `ghost-editor/`, `claude-shorts/`, `editorial-film-edit/`, `vox-motion-graphics/`, `fern-documentary/`, `OpenMontage/` |
| `90_REFERENCE_KNOWLEDGE/` | Cross-stage reference | `prompt-knowledge/` + `open-higgsfield-app/` (catalogs, distilled guides, cinema plates) + `higgsfield-open-studio/` (25-skill Higgsfield craft library, MCSLA, templates) |
| `91_WORKED_EXAMPLES/` | Pedagogy only | `worked-examples/` (renamed from `_TEMP_MOVE/`) |
| `92_SKILL_DEVELOPMENT/` | Internal skill factory | `skill-development/` (generators, blueprints, editing templates + the 720-skill post-production monorepo) |

High numbers (`90`+) keep reference/meta tiers after the production stages so new
production stages (`09_…`) can slot in without renumbering.

## Notes on this clone

- `production_agent/.git` (19 MB repo internals) was intentionally excluded; `.gitignore`
  kept. Everything else is a verified 1:1 copy (459/459 files).
- `cinedance-block-library/` and `commercial-pipeline/` are **extracted** from their
  original `.skill` zips (kept in `04_VIDEO_DIRECTION/_original_skill_archives/`); the
  extracted folders are canonical.
- `README copy.md` (a superseded draft) was not carried over.
- The source library at `SKILL_DATA/` is untouched and still the live system: the global
  `production-agent` skill (`~/.zcode/skills/production-agent/`) routes there. Rewire it
  to this folder when this becomes the canonical home.

## AGENTS TRAIN merge (2026-11-05)

Second merge wave, from `/Volumes/DISK 1/AGENTS TRAIN/` (originals untouched):

- `web_series_production/production_agent` — diffed against `00_STUDIO_ENGINE/production_agent`
  before copying: **identical** (257/257 files, zero content differences). Nothing cloned.
  Its `production_agent 2.zip` is a snapshot of the same content; `temp/` holds dev
  artifacts of it (backup zip, blueprints, legacy subsystem schemas) — not cloned.
- `higgsfield_edit/SKILLS` — 8 units cloned into the two new stages:
  - **08_POST_PRODUCTION_AND_EDITING**: ffmpeg-skill, ghost-editor, claude-shorts,
    editorial-film-edit (folder was "Claude edit skill", renamed to its declared skill
    name), vox-motion-graphics, fern-documentary (extracted from `.skill` zip, original
    kept in `_original_skill_archives/`), OpenMontage.
  - **92_SKILL_DEVELOPMENT**: skill-development (skill factory whole, monorepo inside
    where its generators expect it).
- Exclusions (regenerable/session bulk only): claude-shorts `remotion/node_modules`
  (794 MB — restore with `npm install`; `package.json` + lockfile shipped), OpenMontage
  `.agents/.claude/.cursor/.codex` session state (63 MB), and git internals.
- Unlike stages 00–07, stage 08/92 skills are **operational tools** (local python/
  ffmpeg/node pipelines), not just prompt-craft — see ground rule 5 in `SKILL.md`.

## GitHub merge (2026-11-05)

Third wave, from `github.com/Autom8AI/Open-Higgsfield-AI` (MIT):

- The repo contains **no SKILL files** (verified across all branches and 86 commits of
  history — only README.md and project_knowledge.md ever existed). The prompt guidance
  lives in code + README, so it was **distilled into two md guides** inside
  `90_REFERENCE_KNOWLEDGE/open-higgsfield-app/`:
  `model-prompt-guide.md` (**221 models**, per-model prompt descriptions/examples/options,
  generated from the studio's 261 KB model catalog) and `cinema-prompt-modifiers.md`
  (camera/lens/focal/aperture → prompt-phrase compiler, tag banks, genre starters).
  Raw assets kept alongside: model/voice catalogs, prompt-builder code, app docs, and
  20 named cinema-look webp plates. App code was not taken. See its `INDEX.md`.

## User-added: higgsfield-open-studio (2026-11-05)

Placed directly into `90_REFERENCE_KNOWLEDGE/` by the user. A self-contained
Higgsfield-craft library (60 files, 6 MB): own `SKILL.md` router with a pre-delivery
checklist (routing line, mandatory reads, named-vocabulary verification), the **MCSLA**
video-prompt formula (Model·Camera·Subject·Look·Action), 25 sub-skills (prompt, camera,
motion, seedance, soul, cinema, gpt-image-2, content-factory, marketing-studio,
troubleshoot, …), 18 templates (10 genre starters + 5 seedance layouts + 3 text
overlays), plus `vocab.md`, `model-guide.md`, `prompt-examples.md`,
`production-benchmarks.md`, `photodump-presets.md`, `DISCIPLINE.md`, generated
`INDEX.md` (heading anchors). Its CLI/MCP/preflight rules assume a Higgsfield
subscription (user has none — use the craft, skip execution); `specs/model-specs.yaml`
and `build_index.py` are not in the copy (fall back to `vocab.md`/`model-guide.md`).

## Adding a new skill

1. Pick the stage folder matching its pipeline role; drop the skill in with its unit
   name unchanged (internal relative references must stay intact).
2. Add a route line to the matching table in `SKILL.md`.
3. New pipeline role → new numbered folder (`08_…`), extend the stage map; never
   renumber existing stages.
4. Standalone-triggering skills: frontmatter description ≤900 characters (over ~1024 the
   loader silently drops the skill).
