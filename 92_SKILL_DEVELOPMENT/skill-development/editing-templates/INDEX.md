# Master Directory: 39 Autonomous Editing Skill Templates

This directory contains **39 comprehensive, production-grade editing skill templates** categorized across:
1. **Editing Paradigms & Workflow Modes** (`01-paradigms/` - 4 files)
2. **Narrative & Structural Editing Styles** (`02-narrative-styles/` - 6 files)
3. **Format & Genre-Specific Editing** (`03-format-genres/` - 14 files)
4. **Technique-Level Editing Methods** (`04-techniques/` - 15 files)

Every template details the exact theoretical foundation, step-by-step procedure, mathematical formulas, FilmCraft CLI command bindings, and anti-shallowness execution rules.

---

## Editing Paradigms & Workflow Modes (`01-paradigms/`)

| Template ID | Name | Description | Key Monorepo Links | FilmCraft Commands | File Link |
|---|---|---|---|---|---|
| `linear_editing` | **Linear Editing** | Sequential editing on videotape where shots must be assembled in order from beginning to end. | [001], [008], [017] | `timeline.place`, `timeline.move` | [linear_editing.md](01-paradigms/linear_editing.md) |
| `non_linear_editing` | **Non-Linear Editing (NLE)** | Computer-based editing allowing random access to any frame without sequential restriction on a layered timeline. | [001], [010], [017] | `timeline.place`, `timeline.razor` | [non_linear_editing.md](01-paradigms/non_linear_editing.md) |
| `offline_editing` | **Offline Editing** | Low-resolution proxy editing focused strictly on narrative structure, pacing, and emotional story arc prior to high-res conform. | [014], [016], [017] | `media.colorInfo`, `project.moveToBin` | [offline_editing.md](01-paradigms/offline_editing.md) |
| `online_editing` | **Online Editing / Finishing** | High-resolution conform, optical effects recreation, titling, color space mastering, and deliverable package finishing. | [027], [028], [029] | `media.relink`, `media.linkMedia` | [online_editing.md](01-paradigms/online_editing.md) |

## Narrative & Structural Editing Styles (`02-narrative-styles/`)

| Template ID | Name | Description | Key Monorepo Links | FilmCraft Commands | File Link |
|---|---|---|---|---|---|
| `continuity_editing` | **Continuity Editing (Invisible Editing)** | A style that hides the cut to maintain seamless spatial and temporal coherence, dominant in classical narrative cinema. | [101], [103], [105] | `timeline.place`, `timeline.razor` | [continuity_editing.md](02-narrative-styles/continuity_editing.md) |
| `montage_editing` | **Montage Editing** | Juxtaposition of discontinuous shots to compress time, generate new conceptual meaning, or produce heightened emotional rhythm. | [126], [127], [128] | `timeline.place`, `timeline.razor` | [montage_editing.md](02-narrative-styles/montage_editing.md) |
| `classical_editing` | **Classical Editing** | Refined classical Hollywood grammar emphasizing dramatic emphasis, viewer guidance, and emotional punctuation within seamless continuity. | [101], [102], [108] | `timeline.place`, `timeline.trim` | [classical_editing.md](02-narrative-styles/classical_editing.md) |
| `experimental_editing` | **Experimental / Avant-Garde Editing** | Non-traditional, discontinuous editing that challenges conventional perception, narrative structure, and temporal linearity. | [167], [168], [170] | `timeline.razor`, `timeline.move` | [experimental_editing.md](02-narrative-styles/experimental_editing.md) |
| `narrative_editing` | **Narrative Storytelling Editing** | Editing completely subservient to narrative arc, subtext, character evolution, and thematic pacing. | [016], [101], [115] | `timeline.place`, `timeline.trim` | [narrative_editing.md](02-narrative-styles/narrative_editing.md) |
| `discontinuous_editing` | **Discontinuous / Elliptical Editing** | Deliberate omission of time, space, or action to accelerate rhythm, inject stylistic energy, or emphasize psychological fragmentation. | [115], [116], [117] | `timeline.razor`, `timeline.move` | [discontinuous_editing.md](02-narrative-styles/discontinuous_editing.md) |

## Format & Genre-Specific Editing (`03-format-genres/`)

| Template ID | Name | Description | Key Monorepo Links | FilmCraft Commands | File Link |
|---|---|---|---|---|---|
| `documentary_editing` | **Documentary Editing** | Story construction from non-fiction raw footage, interviews, verité scenes, and archival assets following an assembly-to-fine-cut arc. | [016], [031], [101] | `transcript.generate`, `transcript.search` | [documentary_editing.md](03-format-genres/documentary_editing.md) |
| `podcast_editing` | **Podcast Editing** | Audio-first or multi-camera video editing focused on pristine dialogue clarity, speaker turn-taking, and viewer retention with zero visual friction. | [031], [267], [285] | `multicam.switchAngle`, `multicam.audioFollowsVideo` | [podcast_editing.md](03-format-genres/podcast_editing.md) |
| `vlog_editing` | **Vlog / Slice-of-Life Editing** | Personality-driven, high-retention editing incorporating rapid jump cuts, comedic crash zooms, sound design accents, and direct audience address. | [115], [126], [306] | `timeline.razor`, `timeline.trim` | [vlog_editing.md](03-format-genres/vlog_editing.md) |
| `broadcast_news_editing` | **Broadcast News Editing** | Ultra-fast turnaround editing for television news packages, soundbites, and live cut-ins under rigid broadcast timing and ethical standards. | [011], [028], [101] | `timeline.place`, `timeline.trim` | [broadcast_news_editing.md](03-format-genres/broadcast_news_editing.md) |
| `commercial_brand_editing` | **Commercial / Brand Video Editing** | High-impact, cinematic storytelling for advertisements and brand films operating under strict duration limits (15s, 30s, 60s) and messaging priorities. | [028], [101], [126] | `timeline.place`, `timeline.razor` | [commercial_brand_editing.md](03-format-genres/commercial_brand_editing.md) |
| `social_media_editing` | **Social-First Editing** | Platform-native editing optimized for vertical formats (9:16), instant psychological hooks, kinetic auto-captions, and retention algorithms. | [335], [473], [557] | `sequence.open`, `timeline.place` | [social_media_editing.md](03-format-genres/social_media_editing.md) |
| `trailer_editing` | **Trailer Editing** | High-impact promotional editing that condenses a full narrative into an escalating 3-act sequence driven by tension, sound design, and title hits. | [126], [306], [455] | `timeline.place`, `timeline.razor` | [trailer_editing.md](03-format-genres/trailer_editing.md) |
| `reality_tv_editing` | **Reality TV Editing** | Story producing from hundreds of hours of raw multi-camera footage, creating drama through confessionals, reaction cutaways, and sound futz. | [031], [101], [115] | `multicam.switchAngle`, `timeline.place` | [reality_tv_editing.md](03-format-genres/reality_tv_editing.md) |
| `music_video_editing` | **Music Video Editing** | Rhythm-led, visually experimental editing where musical structure, lyrical themes, and performance sync dictate cut points and visual energy. | [126], [177], [378] | `timeline.sync_tracks`, `timeline.razor` | [music_video_editing.md](03-format-genres/music_video_editing.md) |
| `sports_editing` | **Sports Editing** | Kinetic, action-emphasized editing highlighting athletic mastery, physical collision, speed transitions, and high-stakes emotional climaxes. | [101], [126], [306] | `clip.speedDuration`, `timeline.place` | [sports_editing.md](03-format-genres/sports_editing.md) |
| `corporate_industrial_editing` | **Corporate / Industrial Editing** | Polished, clear, information-first editing for enterprise training, internal communications, B2B product marketing, and investor updates. | [011], [028], [101] | `timeline.place`, `timeline.trim` | [corporate_industrial_editing.md](03-format-genres/corporate_industrial_editing.md) |
| `educational_tutorial_editing` | **Educational / Tutorial Editing** | Instructional editing that sequences learning steps, highlights critical data, and maximizes cognitive retention and comprehension. | [101], [335], [378] | `timeline.place`, `graphics.newText` | [educational_tutorial_editing.md](03-format-genres/educational_tutorial_editing.md) |
| `wedding_event_editing` | **Wedding / Event Editing** | Emotion-driven cinematic narrative editing of milestone live events, combining romantic vows, speeches, and multi-camera ceremony coverage. | [031], [101], [177] | `timeline.sync_tracks`, `multicam.switchAngle` | [wedding_event_editing.md](03-format-genres/wedding_event_editing.md) |
| `animation_editing` | **Animation Editing** | Precision editing of animated assets (2D/3D/Anime) where timing, pose-to-pose holds, animatic pre-vis, and dialogue sync are frame-absolute. | [017], [101], [306] | `timeline.place`, `timeline.razor` | [animation_editing.md](03-format-genres/animation_editing.md) |

## Technique-Level Editing Methods (`04-techniques/`)

| Template ID | Name | Description | Key Monorepo Links | FilmCraft Commands | File Link |
|---|---|---|---|---|---|
| `cutting_on_action` | **Cutting on Action / Match on Action** | Cutting from one shot to another during a physical action to mask the edit, maintaining kinetic momentum and visual continuity. | [101], [104], [115] | `timeline.razor`, `trim.edit` | [cutting_on_action.md](04-techniques/cutting_on_action.md) |
| `jump_cut` | **Jump Cut** | A discontinuous cut within the same shot or setup that violates the 30-degree rule, creating a deliberate temporal jump. | [115], [116], [126] | `timeline.razor`, `timeline.selectGap` | [jump_cut.md](04-techniques/jump_cut.md) |
| `match_cut` | **Match Cut** | A cut connecting two visually, graphically, or conceptually similar elements across disparate scenes, times, or spaces. | [101], [107], [115] | `timeline.place`, `timeline.razor` | [match_cut.md](04-techniques/match_cut.md) |
| `parallel_editing` | **Parallel Editing / Cross-Cutting** | Alternating between two or more simultaneous narrative lines in different locations to build suspense, thematic comparison, or climactic collision. | [101], [115], [126] | `timeline.place`, `timeline.razor` | [parallel_editing.md](04-techniques/parallel_editing.md) |
| `shot_reverse_shot` | **Shot/Reverse Shot** | Alternating camera angles between two conversational partners, maintaining eyeline consistency, shoulder placement, and spatial geometry. | [101], [103], [115] | `timeline.place`, `timeline.razor` | [shot_reverse_shot.md](04-techniques/shot_reverse_shot.md) |
| `j_cut_l_cut` | **J-Cut and L-Cut (Split Edits)** | Split editing technique where audio and video transition at different temporal moments, creating smooth narrative flow and natural dialogue. | [017], [101], [115] | `trim.edit`, `markers.markSplitVideoIn` | [j_cut_l_cut.md](04-techniques/j_cut_l_cut.md) |
| `kuleshov_effect` | **Kuleshov Effect** | Cinematic montage principle proving that viewers derive more meaning from the interaction of two sequential shots than from a single shot in isolation. | [101], [103], [115] | `timeline.place`, `timeline.razor` | [kuleshov_effect.md](04-techniques/kuleshov_effect.md) |
| `cross_cutting` | **Cross-Cutting (Parallel Action)** | Intercutting between actions occurring at the same time in different locations to build suspense, establish narrative ties, and accelerate tempo. | [101], [115], [126] | `timeline.place`, `timeline.razor` | [cross_cutting.md](04-techniques/cross_cutting.md) |
| `fade_wipe_iris` | **Fade / Wipe / Iris Optical Transitions** | Optical transition effects used to signal major temporal, spatial, or emotional transitions with distinct stylistic or era-specific connotations. | [101], [126], [534] | `timeline.add_transition`, `trim.applyDefaultTransition` | [fade_wipe_iris.md](04-techniques/fade_wipe_iris.md) |
| `split_screen` | **Split Screen** | Displaying multiple simultaneous visual streams on screen, used for phone conversations, parallel action, comparison, or graphic energy. | [101], [378], [454] | `timeline.place`, `masks.add` | [split_screen.md](04-techniques/split_screen.md) |
| `speed_ramping` | **Speed Ramping / Time Remapping** | Seamless dynamic acceleration and deceleration of playback speed within a single shot for emphasis, kinetic excitement, and impact. | [101], [126], [378] | `clip.speedDuration`, `effects.setParam` | [speed_ramping.md](04-techniques/speed_ramping.md) |
| `beat_editing` | **Beat Editing** | Cutting video precisely on musical beats, drum transients, and rhythmic accents to harmonize visual and auditory energy. | [126], [127], [128] | `timeline.razor`, `timeline.place` | [beat_editing.md](04-techniques/beat_editing.md) |
| `typography_editing` | **Typography / Kinetic Text Editing** | Fast-paced, text-driven editing that transcribes spoken dialogue into dynamic on-screen text with kinetic motion for maximum engagement. | [021], [335], [349] | `graphics.newText`, `graphics.setText` | [typography_editing.md](04-techniques/typography_editing.md) |
| `contrast_editing` | **Contrast Editing** | Cutting between opposing scenarios, moods, visual scales, or soundscapes to create intense thematic, emotional, or intellectual contrast. | [101], [115], [126] | `timeline.place`, `timeline.razor` | [contrast_editing.md](04-techniques/contrast_editing.md) |
| `elliptical_editing` | **Elliptical Editing** | Deliberately omitting portions of an action, time period, or journey to accelerate narrative progression and invite viewer intellectual inference. | [101], [115], [116] | `timeline.place`, `timeline.razor` | [elliptical_editing.md](04-techniques/elliptical_editing.md) |

