---
name: vox-collage
description: Make premium Vox-style mixed-media paper collage animations with Higgsfield for any topic (a place, brand, product, explainer or story), any length from about 10 to 60 seconds and any format (1:1, 4:5, 16:9, 9:16), with or without an AI narrator. Plans a storyboard from the brief, generates black and white halftone cutouts, a gold sun, colour photo strips and a blue poster with Higgsfield image models, then animates them in code in the Higgsfield sandbox with torn paper transitions and sound effects. Use whenever someone asks for a Vox style video, paper collage animation, mixed media or editorial collage animation, cut-out animation or "an animation like this" for their next video, even if they only give a topic.
---

# Vox Collage animation

Created by Kayo (@learnwithkayo). This skill turns a brief into a finished collage animation in one fixed premium style. The starter kit contains a complete 15 second example (Dubai): a hero landmark rises on grey paper with a big serif title, the camera pushes into a torn sky strip, a plane flies a dashed route, a skyline of cutouts pops up over a gold disc with woodblock waves, hands lift a vintage camera and photo strips fan out of the lens, then a shutter flash lands on a final collage with a gold sun, reaching hands and a blue poster. Use those scenes as building blocks and shape the video around what the person actually wants to say.

Everything runs through the Higgsfield connector: images are generated in Higgsfield and the animation is rendered in the Higgsfield sandbox with the starter kit. The person describes the video; you handle the rest.

## What you need

- The Higgsfield connector in Claude, with these tools: `generate_image_batch`, `jobs_wait`, `remove_background`, `sandbox_exec`, `media_upload`, `media_confirm`, `show_result` (plus `show_generation_by_ids`). If they are missing, tell the person to connect Higgsfield once (Settings, Connectors, add Higgsfield) and stop there.
- Starter kit (animation code, fonts, generic cutouts), downloaded inside the sandbox:
  `https://d2ol7oe51mr4n9.cloudfront.net/user_30H1zSfYpPzNAWpGwWm2DdKzS5V/96025e4c-f8a4-4d68-a80d-1685a56ca841.gz`
  The same code is in this skill's `kit/` folder as a fallback (see "If the kit link fails").

## 1. Brief (one message, only what is missing)

Ask these together, with the default in brackets so the person can just say "go":
- What is the video about? A place, a brand, a product, an explainer, a story. What is the one thing the viewer should remember?
- Length? (15 seconds) Anything from about 10 to 60 seconds.
- Format? (1:1, made for split-screen reels) 4:5, 16:9 or 9:16. In 9:16 the collage sits on the bottom and the top stays open for captions.
- Voice? (none, they talk over it) Or an AI narrator from a script they give you or you write.
- Optional: title word, brand colours for the disc and poster, anything that must appear (logo text, a product, a person's city).

Then go. Do not ask for approval between steps; show the generated images and the stills as you go.

## 2. Storyboard: the style is fixed, the story is not

The kit's `fx_template.js` is one finished example: 15 seconds, five scenes, built for a place. Treat it as a library of scenes in the right style, not as the only video you can make. Plan a storyboard that fits the brief first, then make the code match it.

Scene library already in the template (reuse, reorder, repeat, shorten or drop any of them):
- **A, hero rise:** one big cutout rises on grey paper, serif title drops in letter by letter, torn sky strip slides in with birds, mono caption types out. Great opener.
- **B, flight:** push into a grainy sky, the vehicle flies a dashed route, torn paper edges top and bottom. Good for travel, growth, "from here to there".
- **C, pop-up row:** up to six cutouts spring up over a gold disc, waves roll in, something sails across. Good for "many things", a lineup, a product range, a skyline.
- **D, camera fan:** hands lift a vintage camera and photo strips fan out of the lens with text along the edges. Good for "moments", a portfolio, behind the scenes.
- **E, finale collage:** everything together on sky with the gold sun, reaching hands, a blue poster with a two-line slogan. Good closer.

For an explainer or a longer video, add scenes in the same visual grammar by copying a scene function and changing its contents, for example: a big number that counts up next to a cutout, a headline in the serif over a torn photo print, a then/now split with a torn divider, a dotted route over an old paper map, a list of three labels slapping in one by one. One idea per scene, about 2 to 4 seconds each, and a new movement every half second to a second so it never feels static.

The look that must stay the same in every video (this is what makes it premium):
- Black and white halftone photo cutouts with a thin white paper border and a soft shadow. Colour only in the photo strips, the gold sun or disc and the cobalt poster. No other accent colours, no red, no handwritten or marker fonts.
- Warm grey crumpled paper and a grainy grey-blue sky as the only backgrounds, plus film grain and a soft vignette.
- Type: Abril Fatface for big titles, IBM Plex Mono for small captions, Anton for the poster.
- Smooth eased motion with a little overshoot, slow camera push in every scene, one hero element at a time on lots of empty paper.
- Transitions from the template: push into the sky strip, horizontal paper rip, paper sheet sliding in, camera shutter flash. Vary them.
- Sound: recorded effects only (whoosh, paper hits, type ticks, camera shutter), timed to every entrance.

If narration is wanted: write the script first (short lines, one per scene), make the voiceover with Higgsfield text to speech (`generate_audio`), measure each line with ffprobe in the sandbox and set every scene's duration to its line. Mix it in at the end (see step 5).

## 3. Plan the cast and the words

List every image the storyboard needs. For the template's five scenes these are the slots below; for your own scenes add whatever they need (a photo for a headline scene, two cutouts for a then/now split, a paper map). Keep 15 or fewer new images per video.

| Slot | What it is | Good choice |
|---|---|---|
| hero | the single most iconic subject, tall and vertical works best | Burj Khalifa, Eiffel Tower, a bottle, a rocket |
| lm1 | medium landmark, back left | Dubai Frame |
| lm2 | tall slim landmark | Cayan Tower |
| lm3 | tall landmark | Emirates Towers |
| lm4 | medium landmark, right | Burj Al Arab |
| lm5 | wide and low, sits in front | Museum of the Future |
| strip1..strip5 | five colour photos for the camera fan, left to right; strip3 is the centre and appears first | night skyline, desert, hero from below, old town, a market |
| mover (optional) | small thing that travels across the waves | the kit ships a sail boat; replace it or keep it |

For a product or brand, use products, packaging, the founder's city, factory, team moments. Keep it visual.

Words (all go into `comp/config.json`):
- `title`: one word, uppercase, ideally 4 to 8 letters (auto-fits).
- `heroCaption`: e.g. "BURJ KHALIFA / 828 M". `coords`: real coordinates of the hero.
- `skyCaption`, `skylineCaption`, `edgeLeft` (max about 28 characters), `edgeRight` (max about 24), `corner1`, `corner2`.
- `poster`: two short lines in capitals, each up to 8 or 9 characters, e.g. ["CITY", "OF GOLD"].
Check every fact, number and coordinate with a quick web search before using it. Wrong numbers on screen are the fastest way to lose trust.

## 4. Generate the images (one batch)

Use `generate_image_batch` with model `nano_banana_pro`, `resolution: "2k"`, up to 12 requests. Do not attach style references (they leak extra objects into the cutouts). Prompt templates:

Cutouts (hero, lm1 to lm5, optional mover), aspect 9:16 for tall subjects, 2:3 or 4:3 for wider ones:
```
Editorial collage cutout: [SUBJECT, full subject visible from base to top]. Black and white daylight photograph with rich contrast and a fine visible halftone print texture. Cut out along its silhouette with a thin clean white paper border. Isolated on a flat solid dark green background. No other buildings, no shadow, no text.
```
Photo strips (strip1 to strip5), aspect 9:16:
```
Vertical photograph shot on grainy colour film: [SCENE], [light and mood], heavy film grain. Fills the frame edge to edge. No text, no logos.
```
Then `jobs_wait` (groups of up to 12) and show them once with `show_generation_by_ids`. Look at every image. Regenerate any cutout that is cropped, has extra objects, text, or a busy background.

Run `remove_background` on hero, lm1 to lm5 and the mover (not on the strips). The account allows about 8 jobs at once; if you get a rate limit, wait for a few to finish and send the rest. Wait for them with `jobs_wait` and keep every result URL.

Optional, only if the topic needs it: a different `band` (the bottom strip, default is Japanese woodblock waves) or `ornament` (default gold sun). Generate them as cutouts the same way.

## 5. Build in the Higgsfield sandbox

Everything below runs with `sandbox_exec`. Commands time out after 120 s, so keep each call focused. Start every call with:
```
export HF_WORKFLOWS=${HF_WORKFLOWS:-/home/user/.higgsfield/workflows}; source "$HF_WORKFLOWS/katana/scripts/rr.sh" >/dev/null 2>&1; rr_ws <slug> >/dev/null; cd "$W"
```
(`<slug>` is a short name like `vox-tokyo`.) The first call also sets up the workspace and pulls in the images:
```
curl -fsSL 'https://d2ol7oe51mr4n9.cloudfront.net/user_30H1zSfYpPzNAWpGwWm2DdKzS5V/96025e4c-f8a4-4d68-a80d-1685a56ca841.gz' -o kit.tar.gz && tar -xzf kit.tar.gz
mkdir -p comp/img comp/fonts audio out qa gen
cp kit/fx_template.js comp/fx.js && cp kit/fonts/*.ttf comp/fonts/ && cp kit/img/* comp/img/
python3 kit/make_edl.py 1:1 > comp/edl.json          # or 4:5, 16:9, 9:16
curl -fsSL '<hero bg-removed url>' -o gen/hero.png   # same for lm1..lm5, mover, strip1..strip5
for n in hero lm1 lm2 lm3 lm4 lm5; do python3 kit/prep_assets.py cut gen/$n.png $n; done
for i in 1 2 3 4 5; do python3 kit/prep_assets.py flat gen/strip$i.png strip$i --crop 0; done
python3 kit/prep_assets.py tip hero                   # prints the spire position -> heroTip
```
If you generated a new mover, band or ornament, cut it to `mover`, `band` or `ornament` the same way (it replaces the kit default).

Write `comp/config.json` with a quoted heredoc (`cat > comp/config.json <<'EOF'`):
```json
{
 "title": "DUBAI",
 "heroCaption": "BURJ KHALIFA / 828 M",
 "coords": "25.1972° N  55.2744° E",
 "skyCaption": "DXB / THE WORLD",
 "skylineCaption": "SKYLINE / 2026",
 "edgeLeft": "DUBAI · UNITED ARAB EMIRATES",
 "edgeRight": "25.2048° N · 55.2708° E",
 "corner1": "DUBAI, UAE",
 "corner2": "NO.01 // 2026",
 "poster": ["CITY", "OF GOLD"],
 "colors": {"disc": "#efbd2b", "poster": "#2552b8"},
 "heroTip": 0.496,
 "moverBW": true,
 "moverFlip": false
}
```
Any field can be left empty (`""`) to hide it. Brand colours only change the disc and the poster; keep the black and white cutouts, that contrast is what makes it look premium.

### Matching the code to your storyboard

If the storyboard is exactly the template's five scenes at 15 seconds, skip this. Otherwise edit the files in the sandbox (python string replacements or a rewritten scene function in a quoted heredoc):
- **Scene order and timing:** the `draw()` function at the bottom of `comp/fx.js` picks the scene by time, and each scene has a start constant (`TB`, `TC`, `TD`, `TE`). Change the boundaries, reorder, repeat a scene with different images, or add your new scene functions. Keep each transition about 0.3 to 0.4 seconds.
- **Images per scene:** scenes read images by name from `IM` (file names in `comp/img` without extension). Add new names to `NAMES` at the top of the file. New text can come from new keys in `config.json` (`C.yourKey`).
- **Length:** in `comp/edl.json` set `canvas.frames` to seconds x 30 and the shot's `t1` to the seconds. In `kit/render.sh` change `--dur 15.0` to the new length.
- **Sound:** move the times in `kit/cues.json` with the scenes (each entry is `{"t": seconds, "cat": ...}`; categories: whoosh, longwhoosh, hit, boom, type, ui_blip, flash). Every entrance gets one sound, every transition a whoosh, the shutter flash uses `flash/cam__photo.ogg`.
- **Narration:** put the voiceover at `audio/vo.wav` (48 kHz). After `render.sh full` builds `audio/sfx_bed.wav`, mix them yourself and render again: `ffmpeg -y -i audio/vo.wav -i audio/sfx_bed.wav -filter_complex "[0:a]aresample=48000[v];[1:a]volume=0.6[s];[v][s]amix=inputs=2:normalize=0:duration=longest,alimiter=limit=0.84:level=disabled" -c:a aac -b:a 256k audio/sfx.m4a`, then rerun the render and delivery lines from `render.sh` without rebuilding the bed.

## 6. Check stills, then render

```
bash kit/render.sh stills
```
then look at `qa/stills.jpg` with `sandbox_exec` `image_paths`. The default twelve frames cover the 15 second template; for your own storyboard pass your own times, at least one per scene plus one inside every transition (`bash kit/render.sh stills 0.2s,1.5s,...`). Check: the hero tip lines up (adjust `heroTip`), the title is fully visible, no cutout shows a green or black fringe (regenerate or re-cut it), the poster and edge text fit, text is spelled right. Fix and re-run stills until clean.

Full render (about a minute), in the background:
```
rr_bg logs/full.log bash kit/render.sh full
```
Poll in the next call with `tail -n 5 logs/full.log` until it prints `DONE out/final.mp4`.

## 7. Deliver

1. `media_upload` with `filename: "<slug>.mp4"`, `content_type: "video/mp4"`.
2. In the sandbox: `rr_put out/final.mp4 '<upload_url>' video/mp4` (must print HTTP 200).
3. `media_confirm` with `type: "video"`, then `show_result` with that `media_id`.
Tell the person what is in the video in two or three lines and give the link. Offer quick variations: another topic, brand colours, a different format.

## How it is built (for edits)

- `comp/fx.js` draws all five scenes on a 1080x1080 stage: A hero rise + title + sky strip (0 to 3.1 s), B sky + plane (3 to 5.2 s), C skyline over the gold disc + waves (5 to 8.5 s), D camera fan (8.4 to 11.2 s), E hero collage (11.2 to 15 s). Timings and positions live in each scene function (`sA` to `sE`); text and colours never need code changes.
- Sound effects come from the recorded CC0 library in the sandbox, cued in `kit/cues.json`. There is no music or voiceover on purpose: the creator talks over it. Do not synthesise sounds in code.
- The render engine is the Katana compositor that ships in every Higgsfield sandbox (`$HF_WORKFLOWS/katana/scripts`).

## If the kit link fails

Copy this skill's `kit/` files into the sandbox with quoted heredocs (`cat > kit/fx_template.js <<'EOF' ... EOF`, same for `make_edl.py`, `prep_assets.py`, `render.sh`, `cues.json`). Download the fonts from Google Fonts on GitHub (`https://raw.githubusercontent.com/google/fonts/main/ofl/abrilfatface/AbrilFatface-Regular.ttf`, `ofl/ibmplexmono/IBMPlexMono-Regular.ttf`, `ofl/ibmplexmono/IBMPlexMono-Medium.ttf`, `ofl/anton/Anton-Regular.ttf`) into `comp/fonts/`. Generate the generic pieces too: `paper` (flat scan of warm light grey crumpled paper, edge to edge), `sky` (grainy grey-blue sky photo, edge to edge), `ornament` (gold-leaf sun ornament with wavy rays, colour cutout), `vehicle` (passenger jet, nose pointing left, black and white cutout), `band` (wide band of woodblock-print ocean waves, cutout), `hands` (two hands holding a vintage film camera seen from behind, lens up, wrists at the bottom, black and white cutout), `reach` (several arms reaching to the right, black and white cutout). For `hands`, run `prep_assets.py tip hands` and put the numbers in config as `lensX` and `lensY`.
