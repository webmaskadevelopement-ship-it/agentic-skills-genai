# Video generation model notes

Distilled from `higgsfield-generate/SKILL.md` (v0.14.0) and `COOKBOOK.md` — only the parts that transfer to any video generator. Full original docs live in this folder (`media-inputs.md`, `workflows.md`) and `../model-catalog.md`.

## Model routing — what each video model is for

- **Seedance 2.5** (`seedance_2_5`) — flagship: multi-shot with consistent identity, motion-heavy clips, image-to-video, video editing, video extension. 4–30s, up to 1080p. Modes: `t2v` (text only, accepts no media) / `omni_reference` (all reference inputs incl. start+end frames) / `video_edit` / `video_extension`.
- **Seedance 2.0** — when native 4K is required.
- **Kling 3.0** — start+end frame transitions (first→last-frame morph). `kling3_0_turbo` — cheaper/faster, single start frame.
- **Veo 3.1** (and Lite) — single start frame, max 1 reference.
- **Grok Video 1.5** — one `--start-image` or one `--image`, 2–15s, up to 1080p without reference media.
- **Gemini Omni Flash 1.1** — three modes: reference-to-video / image-to-video (start+end) / video edit. Never mix frame slots with reference slots.
- **Cinema Studio 4.0** — cinematic look.

## i2v frame roles

- `start_image` = first frame; `end_image` = last frame (supported by Kling 3.0, Seedance 2.x, marketing_studio_video).
- The prompt describes **motion**, not the static frame — the model already has it. Verbs: "camera dollies in", "the dancer spins", "smoke rises slowly".
- Single-frame models (Grok, Veo, Kling Turbo, Kling 2.6) reject extra references.

## Audio roles in video models

- `seedance_2_0`: audio input via media role `audio` (reference/lipsync) — distinct from generating output audio.
- `seedance_2_5`: `audio_references` in `omni_reference` mode.

## Ad-video craft (Marketing Studio concepts)

- **Hook** = the opening angle; its text is *prepended* to the prompt, not a replacement for it.
- **Modes**: `ugc` (default) / `ugc_how_to` / `ugc_unboxing` / `product_showcase` / `product_review` / `tv_spot` / `wild_card` / `virtual_try_on` (+ `ugc_virtual_try_on`).

## Video QC rubric (from Virality Predictor)

Their analysis model scores a finished video on: overall score, **peak hook second**, sustain %, strongest region, and Default Mode (high = mind-wandering risk). As a self-review checklist for any video: does the hook land by ~1s, does attention sustain through the middle, is there anything that invites drifting away.

## Transferable production patterns (COOKBOOK.md)

- **Cheap-first iteration**: draft on the cheapest/fastest model; switch to the flagship only once the direction is confirmed.
- **Timestamped filenames** (`yyyy-mm-dd-hh-mm-ss-name.ext`) so generations stay traceable across sessions.

## Two video *edit* capabilities worth knowing exist

- **Sketch-at-timestamp editing** (`draw_to_video`): edit a source video by supplying an edited/sketched frame at a timestamp + instruction ("make the jacket red"). Equivalent tools: generative video editing in Runway/Pika, or re-generating the segment.
- **Reframe**: change a finished video's aspect ratio (16:9 → 9:16) and resolution.
