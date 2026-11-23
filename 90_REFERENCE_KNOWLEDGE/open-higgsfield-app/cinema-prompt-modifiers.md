# Cinema Prompt Modifiers — camera-choice → prompt-text compiler

Distilled from the Open-Higgsfield-AI Cinema Studio (`src/lib/promptUtils.js`, pulled
2026-11-05). The studio's method: pick a camera, lens, focal length and aperture from
curated lists, and each choice injects a fixed prompt phrase. The final prompt is
assembled in a fixed order. Fully portable — works in any generator, not just their app.

## Assembly template

```
{base prompt}, shot on a {camera}, using a {lens} at {focal}mm ({perspective}),
aperture {aperture}, {aperture effect}, cinematic lighting, natural color science,
high dynamic range, professional photography, ultra-detailed, 8K resolution
```

## Camera → prompt text

| Choice | Injected phrase |
|---|---|
| Modular 8K Digital | `modular 8K digital cinema camera` |
| Full-Frame Cine Digital | `full-frame digital cinema camera` |
| Grand Format 70mm Film | `grand format 70mm film camera` |
| Studio Digital S35 | `Super 35 studio digital camera` |
| Classic 16mm Film | `classic 16mm film camera` |
| Premium Large Format Digital | `premium large-format digital cinema camera` |

## Lens → prompt text

| Choice | Injected phrase |
|---|---|
| Creative Tilt Lens | `creative tilt lens effect` |
| Compact Anamorphic | `compact anamorphic lens` |
| Extreme Macro | `extreme macro lens` |
| 70s Cinema Prime | `1970s cinema prime lens` |
| Classic Anamorphic | `classic anamorphic lens` |
| Premium Modern Prime | `premium modern prime lens` |
| Warm Cinema Prime | `warm-toned cinema prime lens` |
| Swirl Bokeh Portrait | `swirl bokeh portrait lens` |
| Vintage Prime | `vintage prime lens` |
| Halation Diffusion | `halation diffusion filter` |
| Clinical Sharp Prime | `ultra-sharp clinical prime lens` |

Visual plates for every lens/camera look: `../public-assets-cinema/` (webp per look).

## Focal length → perspective phrase

| Focal | Injected phrase |
|---|---|
| 8mm | `ultra-wide perspective` |
| 14mm | `wide-angle perspective` |
| 24mm | `wide-angle dynamic perspective` |
| 35mm | `natural cinematic perspective` |
| 50mm | `standard portrait perspective` |
| 85mm | `classic portrait perspective` |

## Aperture → depth effect

| Aperture | Injected phrase |
|---|---|
| f/1.4 | `shallow depth of field, creamy bokeh` |
| f/4 | `balanced depth of field` |
| f/11 | `deep focus clarity, sharp foreground to background` |

## Enhance tag banks (drop-in modifiers)

- **Quality:** professional photography · ultra-detailed · 8K resolution · high dynamic
  range · award-winning
- **Lighting:** cinematic lighting · golden hour · dramatic studio lighting · soft
  diffused light · neon glow · volumetric rays
- **Mood:** moody atmosphere · serene and peaceful · epic and dramatic · warm and cozy ·
  dark and mysterious
- **Style:** photorealistic · oil painting style · watercolor · digital art · concept
  art · anime style · cyberpunk aesthetic

## Quick-start prompts (genre starters)

| Genre | Prompt |
|---|---|
| Portrait | Professional portrait photograph, shallow depth of field, soft studio lighting, 85mm lens |
| Landscape | Breathtaking landscape photograph, golden hour, wide angle, dramatic clouds, 4K |
| Product | Commercial product photography, clean white background, studio lighting, professional |
| Fantasy | Epic fantasy scene, magical atmosphere, volumetric lighting, highly detailed, concept art |
| Sci-Fi | Futuristic sci-fi environment, neon lights, cyberpunk city, rain reflections, cinematic |
| Food | Professional food photography, appetizing, warm lighting, shallow depth of field, editorial |
| Architecture | Architectural photography, dramatic angles, clean lines, modern design, professional |
| Fashion | High fashion editorial, avant-garde styling, studio lighting, Vogue aesthetic, professional |

## Worked example

Base: `lone rider on a rain-soaked Lucknow street at night`
Choices: Grand Format 70mm Film · Classic Anamorphic · 35mm · f/1.4 →

> lone rider on a rain-soaked Lucknow street at night, shot on a grand format 70mm film
> camera, using a classic anamorphic lens at 35mm (natural cinematic perspective),
> aperture f/1.4, shallow depth of field, creamy bokeh, cinematic lighting, natural
> color science, high dynamic range, professional photography, ultra-detailed, 8K resolution
