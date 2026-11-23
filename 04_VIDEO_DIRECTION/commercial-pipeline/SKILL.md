---
name: commercial-pipeline
description: End-to-end workflow for producing a short AI commercial or branded film — planning the reference assets, writing the image prompts that generate them, writing the multi-segment video prompt that assembles them, and diagnosing what broke between generations. Use this whenever the user is working toward an ad, commercial, brand film, product video, promo, spot, or teaser with an AI video model (Seedance, Veo, Kling, Sora, Runway and similar), including when they only ask for one small piece of it — a product shot on white, a character sheet, a location plate, a machine reference, a video prompt, or a fix for a generation that came out wrong. Trigger even when the user never says "commercial" and just asks for something like "a burger in a box on white" or "make the box stop moving between shots", because those are stages of this pipeline and the house rules still apply.
---

# Commercial pipeline

A three-stage workflow for making short branded films with reference-driven video models. Every stage produces one artifact and names the next.

```
STAGE 1  ASSETS       image prompts → reference images, one per element
STAGE 2  VIDEO PROMPT one long structured prompt that assembles them
STAGE 3  FIXES        diagnose a bad generation, rewrite only what broke
```

The pipeline exists because video models cannot hold identity, geography and continuity from prose alone. Identity is moved out of the video prompt and into images. What remains in the video prompt is behaviour, timing and rules.

## Reading order

Read the reference file for the stage you are in. Do not read all of them.

| File | Read when |
|---|---|
| `references/asset-prompts.md` | Writing any image prompt — product, character, location, prop, machine |
| `references/video-prompt.md` | Writing or rewriting the video prompt |
| `references/fix-playbook.md` | The user reports a problem with a generation |
| `references/example-commercial.md` | Before writing a video prompt from scratch, for density and tone |

## How to behave

**Produce first, ask second.** The user asking for "a product on white" wants the prompt, not a discovery call. Write it, state assumptions in one line at the end, and let them correct. Ask a question only when the answer changes the whole artifact and cannot be assumed.

**One artifact per turn.** Deliver the current stage, then name the next stage in one line. Do not run ahead into stages the user has not reached.

**Every prompt goes in a single code block**, plain text, no markdown formatting inside it. The user is pasting this into a generation tool. Commentary lives outside the block.

**Always name the model and always say batch 4.** Identical prompts diverge hard. One generation tells you nothing about whether the prompt is good.

**Always say what to judge the batch on** — three or four specific checks, in priority order. Never "pick the one you like best". A batch judged on prettiness selects for the wrong thing and the next iteration inherits it.

**Talk to the user in their language.** The prompts themselves stay in English regardless — that is what the models are trained on.

## Stage 1 — assets

Plan the full asset list before generating anything. A typical short commercial needs five to eight references:

- **Hero product** — the thing being sold, on pure white
- **Second product state** — if the film has a before/after, transformation or reveal
- **Characters** — one three-view sheet each, flat lighting
- **Location** — the set, empty of the action, lit the way the film will be lit
- **Machine or hero prop** — anything large or mechanical that the story turns on
- **Logo** — never generate this, use the client file

Each asset is a separate prompt and a separate batch. Full craft rules in `references/asset-prompts.md`. The rules that matter most:

- **References carry identity, prompts carry behaviour.** Do not bake camera drama into a reference. Product and character references get flat ambient light so they survive every lighting state in the film. The location is the exception — it does not move, so it establishes the lighting design.
- **Paired assets share paragraphs verbatim.** If a before and after must read as the same object, the packaging or material paragraph is copied word for word between the two image prompts. Designing them separately guarantees they will not match.
- **Scale lives in the video prompt, not the image.** Generate the machine at normal size and override it in its reference line later.

## Stage 2 — the video prompt

One long structured prompt in a fixed section order. Full architecture in `references/video-prompt.md`, worked example in `references/example-commercial.md`.

```
SCENE CONTEXT · ACTIVE REFERENCES · LOCATION MAP · GEOMETRY LOCK
FIRST FRAME AND SPATIAL BLOCKING · FORMAT MODE · EDIT ACCELERATION LOCK
OPTICS · LIGHTING PROGRESSION · CAMERA · ACTION TIMING
PHYSICS · AUDIO · POSITIVE LOCKS · global style tail
```

Spatial rules before camera style. Optics before aesthetic language. Lighting is a lock, not decoration. Everything critical appears twice — once where it applies, once in POSITIVE LOCKS.

**Assign the reference handles yourself.** The user should never have to work out which reference belongs in which segment.

**Write the assets you actually have, not the ones you planned.** Generated characters rarely match the brief exactly. Rewrite every reference line to describe what is in the image. A reference line describing a moustache that did not generate is worse than no reference line.

## Stage 3 — fixes

When the user reports a problem: name the failure, apply the fix, rewrite **only** the affected sections, say what to re-batch. Never re-roll an unchanged prompt.

The master rule, and the highest-value lesson in the whole workflow:

> **If something keeps breaking between cuts, stop describing it better inside every shot. Give it its own lock.**

Position, orientation, facing, speed, where a character stands, how fast the edit moves — anything that must survive multiple cuts gets promoted out of the segment descriptions into a named rule of its own, stated in absolutes. Adding more careful description inside each of sixteen segments does not work.

Full failure catalogue in `references/fix-playbook.md`.

## The complexity budget

Every prompt has one. Once a prompt is generating clean results, one more brilliant idea often just gives the model one more thing to get wrong. Individually good changes can add up to a worse film — more emotion means more character consistency to hold, more elaborate food shots mean more physics to get right, more camera variety means more instructions to follow.

Expect roughly ten generations for a thirty-second film, of which only three or four are actual prompt changes. The rest are re-rolls of a version already liked. When a version is clean, stop and ship it. If a change made things worse, revert to the last clean version rather than trying to fix forward.
