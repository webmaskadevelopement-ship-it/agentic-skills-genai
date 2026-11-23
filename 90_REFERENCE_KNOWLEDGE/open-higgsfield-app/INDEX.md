# open-higgsfield-app — reference extraction

Curated pull from [Autom8AI/Open-Higgsfield-AI](https://github.com/Autom8AI/Open-Higgsfield-AI)
(cloned 2026-11-05, MIT). **The repo contains no SKILL files** — it is a self-hostable
generation studio app (Electron/Next/Vite + Netlify functions, Muapi.ai engine, 20+ models:
Flux, SDXL, Ideogram…). Only its knowledge-bearing assets were taken; app code was not.
The prompt guidance lives in code and the README, so it was **distilled into two readable
md guides** (below) — verified across all branches and git history: no other md files
ever existed in the repo.

## Distilled md guides (the prompt payload)

| File | What it is |
|---|---|
| `model-prompt-guide.md` | **221 models** across t2i/t2v/i2i/i2v/v2v/lipsync — per-model prompt field description, real example prompts, option enums (aspect ratios, durations, resolutions, modes). Generated from `src-lib/studio-models.full-catalog.js` |
| `cinema-prompt-modifiers.md` | The cinema prompt compiler: camera/lens/focal/aperture → injected prompt phrases, fixed assembly template, enhance tag banks, genre starter prompts |

## Raw files kept alongside

| File | What it is |
|---|---|
| `README.md` | App overview + model lineup (provenance) |
| `project_knowledge.md` | App architecture/API patterns doc |
| `models_dump.json` | Raw model dump (67 KB) |
| `data/models.json` | Model catalog as used by the app |
| `data/voices.json` | Voice catalog (feed for voiceover/model-choice work) |
| `src-lib/studio-models.full-catalog.js` | Richest model definitions (261 KB) — params, capabilities |
| `src-lib/models.js` | Lighter model list (Vite app) |
| `src-lib/promptUtils.js` | How the studio builds prompts programmatically |
| `netlify-prompt-builder/prompt-builder.js` | Server-side structured prompt assembly |
| `public-assets-cinema/*.webp` | 20 cinema-look reference plates: anamorphic (classic/compact), 70mm, 16mm, S35, halation, swirl bokeh, tilt, macro, f/1.4–f/11, vintage/70s/warm primes |

## Use in this library

- Model/voice questions → supplements `../prompt-knowledge/model-catalog.md`
- The 20 cinema plates are a named taxonomy of lens/format looks → pairs with
  `06_LOOK_AND_CINEMATOGRAPHY/anamorphic-look.md` (text-only sessions: use the
  filenames as the look vocabulary)
- `promptUtils.js` + `prompt-builder.js` show a structured multi-model prompt
  assembly approach — useful when designing portable prompt templates
