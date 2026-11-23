# FilmCraft CLI Engine & Autonomous Skill Routing Bridge

## Executive Overview & Architectural Contract

This document establishes the bidirectional execution contract between the **Autonomous Post-Production Monorepo** (720 files, `[001]` through `[720]`) and the **FilmCraft Open-Source Video Editing Application** (701 native engine commands, headless CLI, and live GUI loopback control).

Every post-production decision made by an autonomous agent—whether calculating an editorial cut on transient, neutralizing a color temperature cast, ducking underscore music, or snapping subtitle cues—is mathematically resolved under the Monorepo specifications and deterministically dispatched to FilmCraft through this bridge.

---

## 1. Dual-Mode Execution Topology

FilmCraft supports two interoperable execution modes governed by this bridge:

```
  [ Autonomous Post-Production Monorepo Skills ([001]-[720]) ]
                              │
                              ▼
  [ FilmCraft Skill Bridge Layer (filmcraft_cli_bridge.py) ]
                              │
            ┌─────────────────┴─────────────────┐
            ▼                                   ▼
   MODE A: LIVE GUI BRIDGE             MODE B: HEADLESS ENGINE
   (filmcraft --control 9876)          (filmcraft-cli --project <p>)
   • Real-time visual feedback         • High-speed background renders
   • Live timeline scrubbing           • Batch transcoding & proxying
   • Interactive user pairing          • Headless CI/CD test passes
   • Socket JSON-RPC over loopback     • Direct project file serialization
```

---

## 2. Directory of Accepted FilmCraft Commands (701 Native Commands)

FilmCraft exposes **701 native engine commands** divided across **42 functional subsystems**. All commands accept integer ticks (`254,016,000,000` ticks/sec) or fractional seconds (`seconds=12.5`), track indices, or JSON parameter payloads.

| Functional Subsystem | Command Count | Primary Domain Responsibility | Monorepo Cluster Mapping |
|---|---|---|---|
| `audio.*` | **5** | Subsystem governing `audio` | Cluster 04: Sound Design & Mixing (`[267]`–`[334]`) & Voiceover Sync |
| `captions.*` | **22** | Subsystem governing `captions` | Cluster 05: Subtitling & Captioning (`[335]`–`[377]`) & Cmds `[507]`–`[514]` |
| `clip.*` | **57** | Subsystem governing `clip` | Cluster 01: Ingest (`[031]`–`[100]`) & Cluster 02: Editorial (`[101]`–`[176]`) |
| `clipMixer.*` | **4** | Subsystem governing `clipMixer` | Cluster 04: Sound Design & Mixing (`[267]`–`[334]`) & Cmd `[517]` |
| `color.*` | **1** | Subsystem governing `color` | Cluster 03: Color Grading & Look Dev (`[177]`–`[266]`) |
| `command.*` | **1** | Subsystem governing `command` | General Post-Production Support / Utilities |
| `edit.*` | **39** | Subsystem governing `edit` | Cluster 02: Editorial Craft (`[101]`–`[176]`) |
| `effects.*` | **16** | Subsystem governing `effects` | Cluster 03: Color (`[177]`), Cluster 04: Sound (`[267]`), Cluster 06: VFX (`[378]`) |
| `essentialSound.*` | **9** | Subsystem governing `essentialSound` | Cluster 04: Sound Design & Mixing (`[267]`–`[334]`) & Cmds `[515]`, `[519]` |
| `events.*` | **2** | Subsystem governing `events` | General Post-Production Support / Utilities |
| `export.*` | **19** | Subsystem governing `export` | Cluster 07: Finishing, Mastering & QC (`[410]`–`[453]`) & Cmds `[525]`–`[529]` |
| `file.*` | **57** | Subsystem governing `file` | Cluster 00: Governance (`[001]`–`[030]`) & Cluster 01: Ingest (`[031]`–`[100]`) |
| `fonts.*` | **1** | Subsystem governing `fonts` | General Post-Production Support / Utilities |
| `graphics.*` | **82** | Subsystem governing `graphics` | Cluster 06: VFX & Motion Graphics (`[378]`–`[409]`) & Lower Thirds |
| `help.*` | **1** | Subsystem governing `help` | General Post-Production Support / Utilities |
| `history.*` | **1** | Subsystem governing `history` | General Post-Production Support / Utilities |
| `jobs.*` | **2** | Subsystem governing `jobs` | Cluster 07: Finishing & Background Queue (`[410]`–`[453]`) |
| `labels.*` | **4** | Subsystem governing `labels` | General Post-Production Support / Utilities |
| `lumetri.*` | **7** | Subsystem governing `lumetri` | Cluster 03: Color Grading & Look Dev (`[177]`–`[266]`) & Cmds `[497]`–`[506]` |
| `lut.*` | **4** | Subsystem governing `lut` | Cluster 03: Color Grading & Look Dev (`[177]`–`[266]`) & Cmd `[504]` |
| `markers.*` | **32** | Subsystem governing `markers` | Cluster 02: Editorial Craft (`[101]`–`[176]`) & Cluster 05: Subtitling (`[335]`–`[377]`) |
| `masks.*` | **12** | Subsystem governing `masks` | Cluster 03: Color Qualifiers & Cluster 06: VFX Clean Plates |
| `media.*` | **17** | Subsystem governing `media` | Cluster 01: Ingest (`[031]`–`[100]`) & Cluster 06: Online Conform (`[523]`) |
| `mediaBrowser.*` | **10** | Subsystem governing `mediaBrowser` | Cluster 01: Ingest (`[031]`–`[100]`) |
| `mediaCache.*` | **2** | Subsystem governing `mediaCache` | General Post-Production Support / Utilities |
| `metadata.*` | **2** | Subsystem governing `metadata` | General Post-Production Support / Utilities |
| `mixer.*` | **20** | Subsystem governing `mixer` | Cluster 04: Sound Design & Mixing (`[267]`–`[334]`) & Cmds `[515]`–`[522]` |
| `multicam.*` | **35** | Subsystem governing `multicam` | Cluster 01: Ingest & Assistant Editing (`[031]`–`[100]`) & Cmd `[482]` |
| `perf.*` | **1** | Subsystem governing `perf` | Cluster 11: Validation (`[566]`–`[592]`) & Telemetry Logging |
| `playhead.*` | **14** | Subsystem governing `playhead` | Cluster 02: Editorial Craft (`[101]`–`[176]`) & Precision Navigation |
| `prefs.*` | **4** | Subsystem governing `prefs` | General Post-Production Support / Utilities |
| `presets.*` | **7** | Subsystem governing `presets` | General Post-Production Support / Utilities |
| `project.*` | **40** | Subsystem governing `project` | Cluster 00: Governance (`[001]`–`[030]`) & Cluster 01: Ingest (`[031]`–`[100]`) |
| `scopes.*` | **1** | Subsystem governing `scopes` | Cluster 03: Color Grading & Look Dev (`[177]`–`[266]`) & Cmd `[498]` |
| `sequence.*` | **45** | Subsystem governing `sequence` | Cluster 02: Editorial Craft (`[101]`–`[176]`) & Cluster 07: Finishing (`[410]`–`[453]`) |
| `shortcuts.*` | **16** | Subsystem governing `shortcuts` | General Post-Production Support / Utilities |
| `source.*` | **7** | Subsystem governing `source` | General Post-Production Support / Utilities |
| `state.*` | **1** | Subsystem governing `state` | Cluster 00: Governance & Cross-Department DAG (`[001]`–`[002]`) |
| `timeline.*` | **56** | Subsystem governing `timeline` | Cluster 02: Editorial Craft (`[101]`–`[176]`) & Master Cmds (`[486]`–`[496]`) |
| `transcript.*` | **14** | Subsystem governing `transcript` | Cluster 01: Ingest (`[031]`–`[100]`) & Cluster 05: Subtitling (`[335]`–`[377]`) |
| `trim.*` | **24** | Subsystem governing `trim` | Cluster 02: Editorial Craft (`[101]`–`[176]`) & Master Cmds (`[491]`, `[492]`) |
| `tts.*` | **7** | Subsystem governing `tts` | Cluster 04: Sound Design & Mixing (`[267]`–`[334]`) & Scratch ADR |

---

## 3. Subsystem Deep-Dive & Representative Command Signatures

### 3.Audio Subsystem: `audio.*` (5 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `audio.voiceover.settings` | Voice-Over Record Settings | Direct Engine | `{"source":str?,"inputChannel":n?,"name":str?,"countdownSoundCues":bool?,"prerollSeconds":f64?,"postrollSeconds":f64?}` | `-` |
| `audio.voiceover.start` | Start Voice-over Recording | Direct Engine | `{"track":"A1"|id?,"time":ticks?,"preroll":seconds?}` | `-` |
| `audio.voiceover.sync` | Sync Voice-over Capture | Direct Engine | `{"time":ticks?}` | `-` |
| `audio.voiceover.stop` | Stop Voice-over Recording | Direct Engine | `{"time":ticks?,"dir":str?,"discard":bool?}` | `-` |
| `audio.toggleScrubbing` | Toggle Audio During Scrubbing | Direct Engine | `{}` | `Shift+S` |

### 3.Captions Subsystem: `captions.*` (22 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `captions.newTrack` | Add New Caption Track… | Sequence > Captions | `{"format":"Subtitle|CEA-608|CEA-708|Teletext","name":str?,"language":str?}` | `Cmd+Alt+A` |
| `captions.deleteTrack` | Delete Caption Track | Direct Engine | `{"track":id|"C1"}` | `-` |
| `captions.setTrack` | Caption Track Settings | Direct Engine | `{"track":id|"C1","name":str?,"format":str?,"language":str?,"enabled":bool?,"locked":bool?,"syncLock":bool?}` | `-` |
| `captions.setStyle` | Caption Track Style | Direct Engine | `{"track":id|"C1","font":str?,"size":f32?,"color":"#rrggbb[aa]"?,"background":bool?,"backgroundColor":"#rrggbbaa"?,"align":"left|center|right"?,"anchor":"top|middle|bottom"?,"margin":0..0.45 (fraction of frame height)?,"lineSpacing":f32?,"outline":f32?,"outlineColor":str?,"reset":bool?}` | `-` |
| `captions.add` | Add Caption at Playhead | Sequence > Captions | `{"track":id|"C1"?,"text":str?,"time":ticks?,"seconds":f64?,"durationSeconds":f64=3}` | `Cmd+Alt+C` |
| `captions.split` | Split Caption | Direct Engine | `{"caption":id?,"time":ticks?}` | `-` |
| `captions.merge` | Merge Captions | Direct Engine | `{"captions":[id]?}` | `-` |
| `captions.setText` | Edit Caption Text | Direct Engine | `{"caption":id?,"text":str?,"speaker":str|null?}` | `-` |
| `captions.setTimes` | Set Caption In/Out | Direct Engine | `{"caption":id?,"startTime|startFrame|startSeconds|startTimecode":…,"endTime|endFrame|endSeconds|endTimecode":…}` | `-` |
| `captions.trim` | Trim Caption | Direct Engine | `{"caption":id,"edge":"in|out","delta":ticks|"deltaFrames":i64}` | `-` |
| `captions.move` | Move Captions | Direct Engine | `{"captions":[id]?,"delta":ticks|"deltaFrames":i64}` | `-` |
| `captions.delete` | Delete Captions | Direct Engine | `{"captions":[id]?,"ripple":bool=false}` | `-` |
| ... *and 10 additional `captions.*` commands* | ... | ... | ... | ... |

### 3.Clip Subsystem: `clip.*` (57 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `clip.rename` | Rename… | Clip | `{"clip":id?,"item":id?,"name":str}` | `-` |
| `clip.makeSubclip` | Make Subclip… | Clip | `{"item":id?,"clip":id?,"name":str?,"start":ticks?,"end":ticks?,"startFrame":i64?,"endFrame":i64?,"restrictTrims":bool=true}` | `Cmd+U` |
| `clip.editSubclip` | Edit Subclip… | Clip | `{"item":id?,"start":ticks?,"end":ticks?,"startFrame":i64?,"endFrame":i64?,"restrictTrims":bool?,"convertToMaster":bool?}` | `-` |
| `clip.editOffline` | Edit Offline… | Clip | `{"item":id?,"mediaName":str?,"tapeName":str?,"description":str?,"scene":str?,"shot":str?,"logNote":str?}` | `-` |
| `clip.sourceSettings` | Source Settings… | Clip | `{"item":id?}` | `-` |
| `clip.audioChannels` | Audio Channels… | Clip > Modify | `{"items":[id]?,"format":"mono|stereo|5.1|adaptive","clips":[[channel]]?,"channels":[channel]?}` | `Shift+G` |
| `clip.interpretFootage` | Interpret Footage… | Clip > Modify | `{"items":[id]?,"colorSpace":"auto"|"<color space id>"?,"pixelAspect":[num,den]|"file"?}` | `-` |
| `clip.modifyTimecode` | Timecode… | Clip > Modify | `{"item":id?,"timecode":"HH:MM:SS:FF"?,"frame":i64?,"tapeName":str?,"reset":bool?}` | `-` |
| `clip.frameHoldOptions` | Frame Hold Options… | Clip > Video Options | `{"clips":[id]?,"enabled":bool=true,"holdOn":"sourceTimecode|sequenceTime|in|out|playhead","time":ticks?,"timecode":str?,"holdFilters":bool=false}` | `-` |
| `clip.frameHold` | Add Frame Hold | Clip > Video Options | `{"clips":[id]?,"time":ticks?}` | `-` |
| `clip.insertFrameHoldSegment` | Insert Frame Hold Segment | Clip > Video Options | `{"clip":id?,"time":ticks?,"seconds":f64=2}` | `-` |
| `clip.fieldOptions` | Field Options… | Clip > Video Options | `{"clips":[id]?,"reverseFieldDominance":bool=false,"processing":"none|alwaysDeinterlace|flickerRemoval"}` | `-` |
| ... *and 45 additional `clip.*` commands* | ... | ... | ... | ... |

### 3.Clipmixer Subsystem: `clipMixer.*` (4 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `clipMixer.set` | Audio Clip Mixer Adjust | Direct Engine | `{"clip":id,"effect":"volume"|"panner","param":"level"|"balance","value":f64,"keyframe":bool?,"time":ticks?,"begin":bool?}` | `-` |
| `clipMixer.setMode` | Audio Clip Mixer Automation Mode | Direct Engine | `{"track":"A1"|id,"mode":"Off|Read|Latch|Touch|Write"}` | `-` |
| `clipMixer.touch` | Touch Clip Mixer Control | Direct Engine | `{"track":"A1"|id,"lane":"volume|pan","value":f64,"time":ticks?}` | `-` |
| `clipMixer.release` | Release Clip Mixer Control | Direct Engine | `{"track":"A1"|id,"lane":"volume|pan","time":ticks?}` | `-` |

### 3.Color Subsystem: `color.*` (1 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `color.spaces` | List Colour Spaces | Direct Engine | `{}` | `-` |

### 3.Command Subsystem: `command.*` (1 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `command.list` | List Commands | Direct Engine | `{}` | `-` |

### 3.Edit Subsystem: `edit.*` (39 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `edit.undo` | Undo | Edit | `{}` | `Cmd+Z` |
| `edit.redo` | Redo | Edit | `{}` | `Cmd+Shift+Z` |
| `edit.cut` | Cut | Edit | `{}` | `Cmd+X` |
| `edit.copy` | Copy | Edit | `{}` | `Cmd+C` |
| `edit.paste` | Paste | Edit | `{}` | `Cmd+V` |
| `edit.pasteInsert` | Paste Insert | Edit | `{}` | `Cmd+Shift+V` |
| `edit.pasteAttributes` | Paste Attributes… | Edit | `{"clips":[id]?,"motion":bool=true,"opacity":bool=true,"timeRemapping":bool=true,"volume":bool=true,"channelVolume":bool=true,"panner":bool=true,"effects":bool|[effectId]=true,"scaleTimes":bool=true}` | `Cmd+Alt+V` |
| `edit.removeAttributes` | Remove Attributes… | Edit | `{"clips":[id]?,"motion":bool=true,"opacity":bool=true,"timeRemapping":bool=true,"volume":bool=true,"channelVolume":bool=true,"panner":bool=true,"effects":bool|[effectId]=true}` | `-` |
| `edit.clear` | Clear | Edit | `{"clips":[id]?}` | `Backspace` |
| `edit.rippleDelete` | Ripple Delete | Edit | `{"clips":[id]?}` | `Shift+Delete` |
| `edit.rippleDeleteHead` | Ripple Delete Head Frame | Edit | `{"clips":[id]?,"clip":id?}` | `-` |
| `edit.selectAll` | Select All | Edit | `{}` | `Cmd+A` |
| ... *and 27 additional `edit.*` commands* | ... | ... | ... | ... |

### 3.Effects Subsystem: `effects.*` (16 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `effects.apply` | Apply Effect | Direct Engine | `{"clips":[id]?,"effect":"gaussian_blur|Gaussian Blur|…"}` | `-` |
| `effects.remove` | Remove Effect | Direct Engine | `{"clip":id,"index":n}` | `-` |
| `effects.select` | Select Effect | Direct Engine | `{"clip":id,"effect":index|id}|{"none":true}` | `-` |
| `effects.setParam` | Set Effect Parameter | Direct Engine | `{"clip":id,"effect":"motion"|index,"param":str,"mask":n?,"value":num|[x,y]|"#rrggbb"|bool|path|"option name" (a choice takes its index or its name),"time":ticks? (where the keyframe goes when the parameter is animated, kept there even outside the clip; default: the playhead, pinned to the clip; a parameter that is not animated gets a new static value whatever the time),"keyframe":bool? (true: write a keyframe at `time` and animate the parameter),"merge":bool|key?,"begin":bool?}` | `-` |
| `effects.toggleAnimation` | Toggle Animation | Direct Engine | `{"clip":id,"effect":str|index,"param":str,"mask":n?}` | `-` |
| `effects.toggleEnabled` | Toggle Effect | Direct Engine | `{"clip":id,"index":n}` | `-` |
| `effects.reset` | Reset Effect | Direct Engine | `{"clip":id,"index":n}` | `-` |
| `effects.resetParam` | Reset Parameter | Direct Engine | `{"clip":id,"effect":str|index,"param":str}` | `-` |
| `effects.addKeyframe` | Add/Remove Keyframe | Direct Engine | `{"clip":id,"effect":str|index,"param":str,"mask":n?,"time":ticks?}` | `-` |
| `effects.deleteKeyframe` | Delete Keyframe | Direct Engine | `{"clip":id,"effect":str|index,"param":str,"mediaTime":ticks}` | `-` |
| `effects.moveKeyframe` | Move Keyframe | Direct Engine | `{"clip":id,"effect":str|index,"param":str,"mediaTime":ticks,"to":ticks,"value":any?,"merge":bool?,"begin":bool?}` | `-` |
| `effects.moveKeyframes` | Move Keyframes | Direct Engine | `{"keyframes":[{"clip":id,"effect":index,"param":str,"mask":n?,"time":mediaTicks}],"delta":timelineTicks}` | `-` |
| ... *and 4 additional `effects.*` commands* | ... | ... | ... | ... |

### 3.Essentialsound Subsystem: `essentialSound.*` (9 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `essentialSound.inspect` | Inspect Essential Sound | Direct Engine | `{"clips":[id]?}` | `-` |
| `essentialSound.setType` | Set Audio Type | Direct Engine | `{"clips":[id]?,"type":"dialogue|music|sfx|ambience"}` | `-` |
| `essentialSound.clearType` | Clear Audio Type | Direct Engine | `{"clips":[id]?}` | `-` |
| `essentialSound.set` | Essential Sound Setting | Direct Engine | `{"clips":[id]?,"key":"repair.noise.on|repair.noise.amount|repair.humHz|clarity.eqPreset|creative.reverbPreset|ducking.reduceDb|volume.levelDb|mute|…","value":any,"values":{key:value}?,"begin":bool?}` | `-` |
| `essentialSound.applyPreset` | Apply Sound Preset | Direct Engine | `{"clips":[id]?,"preset":str,"type":"dialogue|music|sfx|ambience"?}` | `-` |
| `essentialSound.savePreset` | Save Sound Preset | Direct Engine | `{"clips":[id]?,"name":str}` | `-` |
| `essentialSound.deletePreset` | Delete Sound Preset | Direct Engine | `{"name":str,"type":"dialogue|music|sfx|ambience"?}` | `-` |
| `essentialSound.autoMatch` | Auto-Match Loudness | Direct Engine | `{"clips":[id]?,"target":lufs?}` | `-` |
| `essentialSound.generateDucking` | Generate Ducking Keyframes | Direct Engine | `{"clips":[id]?}` | `-` |

### 3.Events Subsystem: `events.*` (2 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `events.list` | List Events | Direct Engine | `{"level":"info|warning|error"?,"since":id?}` | `-` |
| `events.clear` | Clear All Events | Direct Engine | `{}` | `-` |

### 3.Export Subsystem: `export.*` (19 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `export.presets.list` | List Export Presets | Direct Engine | `{"query":str?,"category":str?,"format":str?,"favorites":bool?}` | `-` |
| `export.presets.get` | Get Export Preset | Direct Engine | `{"name":str}` | `-` |
| `export.presets.save` | Save Export Preset | Direct Engine | `{"name":str,"from":str?,"settings":ExportSettings?,"category":str?,"description":str?,"overwrite":bool=true, …flat overrides}` | `-` |
| `export.presets.delete` | Delete Export Preset | Direct Engine | `{"name":str}` | `-` |
| `export.presets.favorite` | Favorite Export Preset | Direct Engine | `{"name":str,"favorite":bool?}` | `-` |
| `export.presets.import` | Import Export Presets | Direct Engine | `{"path":str}` | `-` |
| `export.presets.export` | Export Export Presets | Direct Engine | `{"path":str,"names":[str]?}` | `-` |
| `export.formats` | List Export Formats | Direct Engine | `{}` | `-` |
| `export.resolve` | Resolve Export Settings | Direct Engine | `{…settings params, "path":str?}` | `-` |
| `export.queue.add` | Send to Export Queue | Direct Engine | `{…settings params,"path":str|dir?,"sequences":[id]?,"ranges":[range]?,"start":bool?,"wait":bool?}` | `Alt+Shift+M` |
| `export.queue.list` | List Export Queue | Direct Engine | `{}` | `-` |
| `export.queue.start` | Start Export Queue | Direct Engine | `{"wait":bool=false}` | `-` |
| ... *and 7 additional `export.*` commands* | ... | ... | ... | ... |

### 3.File Subsystem: `file.*` (57 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `file.newProject` | Project… | File > New | `{"name":str}` | `Cmd+Alt+N` |
| `file.openDemoProject` | Demo Project | File > New | `{}` | `-` |
| `file.newSequence` | Sequence… | File > New | `{"name":str,"width":u32=1920,"height":u32=1080,"fps":f64=23.976,"sampleRate":u32=48000,"video":n=3,"audio":n=3,"mix":"Stereo|Mono|5.1|Adaptive"?,"trackType":"Standard|Mono|5.1|Adaptive"?,"fromItem":itemId?,"fromItems":[itemId]?}` | `Cmd+N` |
| `file.newSequenceFromClip` | Sequence From Clip | File > New | `{"items":[id]?}` | `-` |
| `file.newBin` | Bin | File > New | `{"name":str,"parent":binId?}` | `Cmd+B` |
| `file.newBinFromSelection` | Bin From Selection | File > New | `{"items":[id]?,"name":str?}` | `Shift+B` |
| `file.newSearchBin` | Search Bin | File > New | `{"name":str?,"column":str?,"operator":str?,"text":str?,"rows":[..]?,"matchAll":bool?,"caseSensitive":bool?}` | `-` |
| `file.newOfflineFile` | Offline File… | File > New | `{"name":str?,"fileName":str?,"tapeName":str?,"video":bool=true,"audio":bool=true,"width":u32?,"height":u32?,"fps":f64?,"sampleRate":u32=48000,"channels":u32=2,"timecode":"HH:MM:SS:FF"?,"seconds":f64=10,"description":str?}` | `-` |
| `file.newAdjustmentLayer` | Adjustment Layer… | File > New | `{"seconds":f64=5}` | `-` |
| `file.newBarsAndTone` | Bars and Tone… | File > New | `{"seconds":f64=10}` | `-` |
| `file.newBlackVideo` | Black Video… | File > New | `{"seconds":f64}` | `-` |
| `file.newColorMatte` | Color Matte… | File > New | `{"color":"#rrggbb","seconds":f64}` | `-` |
| ... *and 45 additional `file.*` commands* | ... | ... | ... | ... |

### 3.Fonts Subsystem: `fonts.*` (1 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `fonts.list` | List Fonts | Direct Engine | `{"system":bool=true (scan the system font folders)}` | `-` |

### 3.Graphics Subsystem: `graphics.*` (82 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `graphics.newText` | Text | Graphics and Titles > New Layer | `{"text":str="New Text","position":[x,y]? (point text: its alignment point on the first baseline; with `box`: the box's top-left corner),"box":[w,h]? (paragraph text wrapped in a box this size),"clip":id?,"newClip":bool?,"vertical":bool=false,"size":px=100,"font":str?,"fontStyle":str?,"seconds":f64=5,"track":index?,"time":ticks?}` | `Cmd+T` |
| `graphics.newShape` | Shape | Direct Engine | `{"shape":"rectangle|ellipse|polygon|path","position":[x,y]? (the shape's centre),"size":[w,h]=[400,200],"points":[[x,y],…]?,"clip":id? (add the shape to this graphic),"seconds":f64=5,"track":index?,"time":ticks?}` | `-` |
| `graphics.setText` | Edit Text | Direct Engine | `{"clip":id?,"layer":n|name?,"text":str,"merge":bool? (coalesce with the previous Edit Text undo step)}` | `-` |
| `graphics.set` | Set Graphic Properties | Direct Engine | `{"clip":id?,"layer":n|name?,"props":{"font":"Inter","font_style":"Bold","size":120,"align":"center","tracking":50,"leading":0,"fill_color":"#ffcc00","stroke":true,"stroke_width":6,"background":true,"shadow":true,"position":[x,y],"scale":100,"rotation":0,"opacity":100,…},"time":ticks?,"merge":bool?,"begin":bool?}` | `-` |
| `graphics.setTextType` | Text Layer Type | Direct Engine | `{"clip":id?,"layer":n|name?,"type":"point|paragraph" (point: no box, handles scale the text; paragraph: the text wraps in a box that handles resize)}` | `-` |
| `graphics.selectLayer` | Select Graphic Layer | Direct Engine | `{"clip":id?,"layers":[n]}` | `-` |
| `graphics.deleteLayer` | Delete Graphic Layer | Direct Engine | `{"clip":id?,"layer":n?}` | `-` |
| `graphics.arrangeLayer` | Arrange Graphic Layer | Direct Engine | `{"clip":id?,"layer":n?,"to":"front|back|forward|backward"|index}` | `-` |
| `graphics.align` | Align Layers | Direct Engine | `{"clip":id?,"layers":[n]?,"align":"left|hcenter|right|top|vcenter|bottom","to":"frame|group|selection"="frame" (frame: each layer; group: the layers' union; one layer always aligns to the frame)}` | `-` |
| `graphics.distribute` | Distribute Layers | Direct Engine | `{"clip":id?,"layers":[n] (3 or more)?,"axis":"horizontal|vertical","space":bool=false (equal gaps instead of equal centre spacing)}` | `-` |
| `graphics.list` | List Graphic Layers | Direct Engine | `{"clip":id?}` | `-` |
| `graphics.newVerticalText` | Vertical Text | Graphics and Titles > New Layer | `{"text":str="New Text","position":[x,y]?,"clip":id?,"size":px=100,"seconds":f64=5,"time":ticks?}` | `-` |
| ... *and 70 additional `graphics.*` commands* | ... | ... | ... | ... |

### 3.Help Subsystem: `help.*` (1 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `help.systemReport` | System Compatibility Report | Direct Engine | `{}` | `-` |

### 3.History Subsystem: `history.*` (1 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `history.list` | List History | Direct Engine | `{}` | `-` |

### 3.Jobs Subsystem: `jobs.*` (2 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `jobs.list` | List Jobs | Direct Engine | `{}` | `-` |
| `jobs.cancel` | Cancel Job | Direct Engine | `{"job":id}` | `-` |

### 3.Labels Subsystem: `labels.*` (4 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `labels.presets` | Label Color Presets | Direct Engine | `{}` | `-` |
| `labels.importPreset` | Import Label Color Preset | Direct Engine | `{"path":str}` | `-` |
| `labels.exportPreset` | Export Label Color Preset | Direct Engine | `{"path":str}` | `-` |
| `labels.deletePreset` | Delete Label Color Preset | Direct Engine | `{"name":str}` | `-` |

### 3.Lumetri Subsystem: `lumetri.*` (7 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `lumetri.presets` | List Lumetri Presets | Direct Engine | `{"folder":str?}` | `-` |
| `lumetri.applyPreset` | Apply Lumetri Preset | Direct Engine | `{"name":str,"clips":[id]?}` | `-` |
| `lumetri.presetThumbnails` | Lumetri Preset Thumbnails | Direct Engine | `{"folder":str?,"names":[str]?,"width":n=160,"columns":n=4,"path":str?}` | `-` |
| `lumetri.setInputLut` | Set Input LUT | Direct Engine | `{"clip":id?,"lut":"lib:<id>"|"builtin:<id>"|""?,"path":str?}` | `-` |
| `lumetri.setLook` | Set Creative Look | Direct Engine | `{"clip":id?,"lut":"lib:<id>"|"builtin:<id>"|""?,"path":str?}` | `-` |
| `lumetri.applyMatch` | Apply Match | Direct Engine | `{"clip":id?,"referenceTime":ticks?|"referenceFrame":n?|"referenceTimecode":str?,"faceDetection":bool=true}` | `-` |
| `lumetri.setSection` | Toggle Lumetri Section | Direct Engine | `{"clip":id?,"section":"basic"|"creative"|"curves"|"wheels"|"hsl"|"vignette","on":bool?}` | `-` |

### 3.Lut Subsystem: `lut.*` (4 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `lut.import` | Import LUT… | Direct Engine | `{"path":str,"name":str?}` | `-` |
| `lut.list` | List LUTs | Direct Engine | `{}` | `-` |
| `lut.remove` | Remove LUT | Direct Engine | `{"id":str}` | `-` |
| `lut.export` | Export LUT | Direct Engine | `{"lut":"lib:<id>"|"builtin:<id>","path":str,"format":"cube"|"3dl"?}` | `-` |

### 3.Markers Subsystem: `markers.*` (32 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `markers.markIn` | Mark In | Markers | `{"time":ticks?,"frame":i64?,"seconds":f64?,"timecode":str?,"target":"program|source"}` | `I` |
| `markers.markOut` | Mark Out | Markers | `{"time":ticks?,"frame":i64?,"seconds":f64?,"timecode":str?,"target":"program|source"}` | `O` |
| `markers.markClip` | Mark Clip | Markers | `{}` | `X` |
| `markers.markSelection` | Mark Selection | Markers | `{}` | `/` |
| `markers.markSplitVideoIn` | Video In | Markers > Mark Split | `{"time":ticks?,"frame":i64?,"seconds":f64?,"timecode":str?,"target":"program|source"}` | `-` |
| `markers.markSplitVideoOut` | Video Out | Markers > Mark Split | `{"time":ticks?,"frame":i64?,"seconds":f64?,"timecode":str?,"target":"program|source"}` | `-` |
| `markers.markSplitAudioIn` | Audio In | Markers > Mark Split | `{"time":ticks?,"frame":i64?,"seconds":f64?,"timecode":str?,"target":"program|source"}` | `-` |
| `markers.markSplitAudioOut` | Audio Out | Markers > Mark Split | `{"time":ticks?,"frame":i64?,"seconds":f64?,"timecode":str?,"target":"program|source"}` | `-` |
| `markers.goToIn` | Go to In | Markers | `{"target":"program|source"}` | `Shift+I` |
| `markers.goToOut` | Go to Out | Markers | `{"target":"program|source"}` | `Shift+O` |
| `markers.goToSplitVideoIn` | Video In | Markers > Go to Split | `{"target":"program|source"}` | `-` |
| `markers.goToSplitVideoOut` | Video Out | Markers > Go to Split | `{"target":"program|source"}` | `-` |
| ... *and 20 additional `markers.*` commands* | ... | ... | ... | ... |

### 3.Masks Subsystem: `masks.*` (12 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `masks.add` | Create Mask | Direct Engine | `{"clip":id?,"effect":index|id?="opacity","shape":"ellipse"|"polygon"|"rectangle"|"bezier","path":[[x,y]…]|{vertices}?,"center":[x,y]?,"size":[w,h]?,"cornerRadius":px?}` | `-` |
| `masks.remove` | Delete Mask | Direct Engine | `{"clip":id?,"effect":index|id?,"mask":n?}` | `-` |
| `masks.set` | Change Mask | Direct Engine | `{"clip":id?,"effect":index|id?,"mask":n?,"name":str?,"inverted":bool?,"mode":"none|add|subtract|intersect|lighten|darken|difference"?,"trackMethod":"position|positionRotation|positionScaleRotation"?,"feather":px?,"opacity":pct?,"expansion":px?,"path":path?,"time":ticks?,"merge":key?}` | `-` |
| `masks.moveVertex` | Move Mask Vertex | Direct Engine | `{"clip":id?,"effect":index|id?,"mask":n?,"vertex":n,"handle":"point"|"in"|"out"?,"to":[x,y]?|"delta":[dx,dy]?,"breakHandles":bool?,"merge":key?}` | `-` |
| `masks.translate` | Move Mask | Direct Engine | `{"clip":id?,"effect":index|id?,"mask":n?,"delta":[dx,dy],"merge":key?}` | `-` |
| `masks.addVertex` | Add Mask Vertex | Direct Engine | `{"clip":id?,"effect":index|id?,"mask":n?,"after":n,"at":[x,y]}` | `-` |
| `masks.removeVertex` | Delete Mask Vertex | Direct Engine | `{"clip":id?,"effect":index|id?,"mask":n?,"vertex":n}` | `-` |
| `masks.track` | Track Selected Mask | Direct Engine | `{"clip":id?,"effect":index|id?,"mask":n?,"direction":"forward"|"backward"?,"frames":n?,"method":"position|positionRotation|positionScaleRotation"?,"wait":bool?}` | `-` |
| `masks.toggleVertexSmooth` | Convert Mask Vertex | Direct Engine | `{"clip":id?,"effect":index|id?,"mask":n?,"vertex":n}` | `-` |
| `masks.roundCorners` | Round Mask Corners | Direct Engine | `{"clip":id?,"effect":index|id?,"mask":n?,"radius":px,"vertices":[n]?}` | `-` |
| `masks.select` | Select Mask | Direct Engine | `{"clip":id,"effect":index|id,"mask":n}|{"none":true}` | `-` |
| `masks.list` | List Masks | Direct Engine | `{"clip":id?,"time":ticks?}` | `-` |

### 3.Media Subsystem: `media.*` (17 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `media.colorInfo` | Media Colour Info | Direct Engine | `{"item":id}` | `-` |
| `media.findMissing` | Find Missing Media | Direct Engine | `{}` | `-` |
| `media.status` | Media Status | Direct Engine | `{"item":id?}` | `-` |
| `media.linkMedia` | Link Media… | File | `{}  (opens the Link Media dialog; agents use media.relink / media.autoRelink)` | `-` |
| `media.relink` | Relink Media | Direct Engine | `{"item":id,"path":str,"force":bool=false,"relinkOthers":bool=true,"alignTimecode":bool=false,"match":{"fileName":bool,"extension":bool,"clipId":bool,"duration":bool,"mediaStart":bool,"metadata":bool}?}` | `-` |
| `media.refreshChanged` | Refresh Changed Media | Direct Engine | `{}` | `-` |
| `media.replaceFootage` | Replace Footage… | Direct Engine | `{"item":id,"path":str}` | `-` |
| `media.autoRelink` | Relink Moved Media | Direct Engine | `{"from":str,"to":str}|{"folder":str} + match options` | `-` |
| `media.search` | Search for Media | Direct Engine | `{"folder":str,"item":id?,"exactName":bool=true}` | `-` |
| `media.makeOffline` | Make Offline… | File | `{"items":[id]?,"deleteFiles":bool=false}` | `-` |
| `media.offlineAll` | Offline All | Direct Engine | `{}  (leave every missing file offline and close the Link Media dialog)` | `-` |
| `media.createProxies` | Create Proxies… | Clip > Proxy | `{"items":[id]?,"preset":"prores_proxy_quarter|prores_proxy_half|prores_lt_half|h264_quarter|h264_half","destination":str?,"attach":bool=true,"wait":bool=false}` | `-` |
| ... *and 5 additional `media.*` commands* | ... | ... | ... | ... |

### 3.Mediabrowser Subsystem: `mediaBrowser.*` (10 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `mediaBrowser.roots` | Media Browser Locations | Direct Engine | `{}` | `-` |
| `mediaBrowser.list` | List Directory | Direct Engine | `{"path":str?,"fileTypes":str?}` | `-` |
| `mediaBrowser.navigate` | Go to Directory | Direct Engine | `{"path":str} | {"back":true} | {"forward":true} | {"up":true}` | `-` |
| `mediaBrowser.select` | Select Files | Direct Engine | `{"paths":[str]}` | `-` |
| `mediaBrowser.favorite` | Add to Favorites | Direct Engine | `{"path":str?,"remove":bool?}` | `-` |
| `mediaBrowser.clearRecent` | Clear Recent Directories | Direct Engine | `{}` | `-` |
| `mediaBrowser.settings` | Media Browser Settings | Direct Engine | `{"fileTypes":"all|video|audio|image|project|caption|<ext>"?,"view":"list|thumbnails"?,"columns":[str]?,"importAsImageSequence":bool?,"hoverScrub":bool?,"thumbnailSize":f32?}` | `-` |
| `mediaBrowser.import` | Import | Direct Engine | `{"paths":[str]?,"bin":binId?,"imageSequence":bool?}` | `-` |
| `mediaBrowser.openInSource` | Open In Source Monitor | Direct Engine | `{"path":str?}` | `-` |
| `mediaBrowser.probe` | Media File Properties | Direct Engine | `{"path":str}` | `-` |

### 3.Mediacache Subsystem: `mediaCache.*` (2 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `mediaCache.info` | Media Cache Info | Direct Engine | `{}` | `-` |
| `mediaCache.clean` | Delete Media Cache Files | Direct Engine | `{"all":bool?}` | `-` |

### 3.Metadata Subsystem: `metadata.*` (2 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `metadata.get` | Get Metadata | Direct Engine | `{"item":id?,"clip":id?}` | `-` |
| `metadata.set` | Edit Metadata | Direct Engine | `{"item":id?,"clip":id?,"field":"Name|Label|Description|Scene|Shot|Log Note|Comment|Tape Name|Client|Camera Angle|…","value":str} | {"item":id?,"fields":{name:str}}` | `-` |

### 3.Mixer Subsystem: `mixer.*` (20 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `mixer.addSubmix` | Add Audio Submix Track | Sequence | `{"name":str?,"channels":"Mono|Stereo|5.1"?}` | `-` |
| `mixer.inspect` | Inspect Audio Track Mixer | Direct Engine | `{"time":ticks?}` | `-` |
| `mixer.setStrip` | Track Mixer Settings | Direct Engine | `{"strip":"A1"|"S1"|"Mix"|id,"name":str?,"volumeDb":f64?,"pan":f64?,"muted":bool?,"solo":bool?,"recordArm":bool?,"soloSafe":bool?,"mode":"Off|Read|Latch|Touch|Write"?,"output":"Mix"|"S1"?,"inputMap":"Stereo|Left|Right|Swap|Mono"?,"channels":"Mono|Stereo|5.1"?}` | `-` |
| `mixer.setValue` | Set Mixer Control | Direct Engine | `{"strip":"A1"|"S1"|"Mix"|id,"lane":"volume|pan|mute|send.<i>.level|fx.<slot>.<param>","value":f64,"time":ticks?}` | `-` |
| `mixer.touch` | Touch Mixer Control | Direct Engine | `{"strip":"A1"|"S1"|"Mix"|id,"lane":"volume|pan|mute|send.<i>.level|fx.<slot>.<param>","value":f64,"time":ticks?}` | `-` |
| `mixer.release` | Release Mixer Control | Direct Engine | `{"strip":"A1"|"S1"|"Mix"|id,"lane":str?,"time":ticks?}` | `-` |
| `mixer.recordStart` | Start Automation Pass | Direct Engine | `{"time":ticks?}` | `-` |
| `mixer.recordStop` | Write Automation | Direct Engine | `{"time":ticks?}` | `-` |
| `mixer.deleteSubmix` | Delete Submix Track | Direct Engine | `{"strip":"S1"|id}` | `-` |
| `mixer.addInsert` | Add Track Effect | Direct Engine | `{"strip":"A1"|"S1"|"Mix"|id,"effect":str,"slot":n?,"postFader":bool?}` | `-` |
| `mixer.removeInsert` | Remove Track Effect | Direct Engine | `{"strip":"A1"|"S1"|"Mix"|id,"slot":n}` | `-` |
| `mixer.setInsert` | Track Effect Settings | Direct Engine | `{"strip":"A1"|"S1"|"Mix"|id,"slot":n,"enabled":bool?,"postFader":bool?,"params":{id:value}?}` | `-` |
| ... *and 8 additional `mixer.*` commands* | ... | ... | ... | ... |

### 3.Multicam Subsystem: `multicam.*` (35 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `multicam.switchAngle` | Switch Multi-Camera Angle | Direct Engine | `{"camera":1..16 (shown order)|"angle":0-based,"clips":[id]?,"time":ticks?,"videoOnly":bool?,"audioOnly":bool?}` | `-` |
| `multicam.recordStart` | Start Multi-Camera Recording | Direct Engine | `{"time":ticks?}` | `-` |
| `multicam.cut` | Cut to Camera | Direct Engine | `{"camera":1..16|"angle":0-based,"time":ticks?,"videoOnly":bool?}` | `-` |
| `multicam.recordStop` | Stop Multi-Camera Recording | Direct Engine | `{"time":ticks?}` | `-` |
| `multicam.audioFollowsVideo` | Multi-Camera Audio Follows Video | Direct Engine | `{"enabled":bool?}` | `-` |
| `multicam.editCameras` | Edit Cameras… | Direct Engine | `{"sequence":id?,"cameras":[{"angle":0-based,"name":str?,"enabled":bool?}]?,"audio":"camera1|all|switch"?}` | `-` |
| `multicam.cutToCamera` | Cut to Camera | Direct Engine | `{"camera":1..16|"angle":0-based,"time":ticks?,"videoOnly":bool?}` | `-` |
| `multicam.gridLayout` | Multi-Camera Layout | Direct Engine | `{"layout":"auto|2x2|3x3|4x4"}` | `-` |
| `multicam.page` | Multi-Camera Page | Direct Engine | `{"page":0-based|"next"|"prev"}` | `-` |
| `multicam.nextPage` | Next Multi-Camera Page | Direct Engine | `{}` | `-` |
| `multicam.prevPage` | Previous Multi-Camera Page | Direct Engine | `{}` | `-` |
| `multicam.selectionTopDown` | Multi-Camera Selection Top Down | Direct Engine | `{"enabled":bool?}` | `-` |
| ... *and 23 additional `multicam.*` commands* | ... | ... | ... | ... |

### 3.Perf Subsystem: `perf.*` (1 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `perf.stats` | Performance Statistics | Direct Engine | `{}` | `-` |

### 3.Playhead Subsystem: `playhead.*` (14 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `playhead.set` | Set Playhead | Direct Engine | `{"time":ticks|"frame":i64|"seconds":f64|"timecode":str}` | `-` |
| `playhead.step` | Step Frames | Direct Engine | `{"frames":i64}` | `-` |
| `playhead.stepForward` | Step Forward One Frame | Direct Engine | `{}` | `Right` |
| `playhead.stepBack` | Step Back One Frame | Direct Engine | `{}` | `Left` |
| `playhead.stepForward5` | Step Forward Five Frames | Direct Engine | `{}` | `Shift+Right` |
| `playhead.stepBack5` | Step Back Five Frames | Direct Engine | `{}` | `Shift+Left` |
| `playhead.nextEdit` | Go to Next Edit Point | Direct Engine | `{}` | `Down` |
| `playhead.prevEdit` | Go to Previous Edit Point | Direct Engine | `{}` | `Up` |
| `playhead.start` | Go to Sequence Start | Direct Engine | `{}` | `Home` |
| `playhead.end` | Go to Sequence End | Direct Engine | `{}` | `End` |
| `playhead.nextEditAnyTrack` | Go to Next Edit Point on Any Track | Direct Engine | `{}` | `Shift+Down` |
| `playhead.prevEditAnyTrack` | Go to Previous Edit Point on Any Track | Direct Engine | `{}` | `Shift+Up` |
| ... *and 2 additional `playhead.*` commands* | ... | ... | ... | ... |

### 3.Prefs Subsystem: `prefs.*` (4 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `prefs.get` | Get Preferences | Direct Engine | `{"key":str?}` | `-` |
| `prefs.set` | Set Preferences | Direct Engine | `{"key":str,"value":any}|{"values":{key:value}}` | `-` |
| `prefs.reset` | Reset Preferences | Direct Engine | `{"category":str?}` | `-` |
| `prefs.schema` | Settings Schema | Direct Engine | `{"category":str?}` | `-` |

### 3.Presets Subsystem: `presets.*` (7 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `presets.list` | List Effect Presets | Direct Engine | `{}` | `-` |
| `presets.save` | Save Preset | Direct Engine | `{"clip":id?,"effects":[index]?,"name":str,"description":str?,"keyframes":"scale"|"anchorIn"|"anchorOut"|"none"?}` | `-` |
| `presets.apply` | Apply Preset | Direct Engine | `{"preset":str,"clips":[id]?}` | `-` |
| `presets.delete` | Delete Preset | Direct Engine | `{"name":str}` | `-` |
| `presets.rename` | Rename Preset | Direct Engine | `{"name":str,"to":str}` | `-` |
| `presets.export` | Export Presets | Direct Engine | `{"path":str,"names":[str]?}` | `-` |
| `presets.import` | Import Presets | Direct Engine | `{"path":str}` | `-` |

### 3.Project Subsystem: `project.*` (40 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `project.matteColor` | Color Matte Color… | Direct Engine | `{"item":id?,"color":"#rrggbb"}` | `-` |
| `project.select` | Select Project Items | Direct Engine | `{"items":[id]}` | `-` |
| `project.delete` | Clear | Direct Engine | `{"items":[id]?}` | `Delete` |
| `project.moveToBin` | Move to Bin | Direct Engine | `{"items":[id|binId]?,"bin":binId|null}` | `-` |
| `project.setMarks` | Set Source In/Out | Direct Engine | `{"item":id,"in":ticks?|null,"out":ticks?|null}` | `-` |
| `project.inspect` | Inspect Project | Direct Engine | `{}` | `-` |
| `project.ingestSettings` | Ingest Settings… | File > Project Settings | `{"enabled":bool?,"action":"copy|transcode|createProxies|copyAndCreateProxies"?,"destination":str?,"preset":str?}` | `-` |
| `project.notes` | Get Project Notes | Direct Engine | `{}` | `-` |
| `project.setNotes` | Edit Project Notes | Direct Engine | `{"text":str,"merge":str?}` | `-` |
| `project.view.get` | Project Panel View | Direct Engine | `{}` | `-` |
| `project.view.set` | Set Project Panel View | Direct Engine | `{"view":"list|icon|freeform"?,"iconSize":f32?,"fontSize":"small|medium|large|extraLarge"?,"previewArea":bool?,"thumbnails":bool?,"thumbnailsShowEffects":bool?,"hoverScrub":bool?,"thumbnailControlsAllDevices":bool?,"iconSort":column|{"column":str,"descending":bool}?}` | `-` |
| `project.columns.list` | List Project Columns | Direct Engine | `{}` | `-` |
| ... *and 28 additional `project.*` commands* | ... | ... | ... | ... |

### 3.Scopes Subsystem: `scopes.*` (1 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `scopes.read` | Read Lumetri Scopes | Direct Engine | `{"scopes":["waveform","parade","histogram","vectorscopeYuv","vectorscopeHls"]?,"waveformType":"rgb|luma|yc|ycNoChroma"?,"paradeType":"rgb|yuv|rgbWhite"?,"colorSpace":"auto|601|709|2100"?,"clamp":bool=true,"columns":n=8,"peaks":n=8,"bins":bool=true,"scale":0.5,"time":ticks?|"frame"|"seconds"|"timecode"}` | `-` |

### 3.Sequence Subsystem: `sequence.*` (45 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `sequence.revealInProject` | Reveal Sequence in Project | Direct Engine | `{"item":id?}` | `-` |
| `sequence.open` | Open in Timeline | Direct Engine | `{"item":id}` | `-` |
| `sequence.close` | Close Sequence | Direct Engine | `{"item":id?}` | `Cmd+W` |
| `sequence.closeOthers` | Close Other Timeline Panels | Direct Engine | `{"item":id?}` | `-` |
| `sequence.moveTab` | Move Sequence Tab | Direct Engine | `{"item":id?,"index":int}` | `-` |
| `sequence.settings` | Sequence Settings… | Sequence | `{"width":u32?,"height":u32?,"fps":f64?,"name":str?,"sampleRate":u32?,"mix":"Stereo|Mono|5.1|Adaptive"?,"dropFrame":bool?,"maxRenderQuality":bool?,"workingSpace":"rec709"|"rec2100-pq"|"rec2100-hlg"?,"wideGamut":bool?,"autoToneMap":bool?,"scaleMotion":bool=false}` | `-` |
| `sequence.renderEffectsInToOut` | Render Effects In to Out | Sequence | `{"wait":bool=false}` | `Enter` |
| `sequence.renderInToOut` | Render In to Out | Sequence | `{"wait":bool=false}` | `-` |
| `sequence.renderSelection` | Render Selection | Sequence | `{"wait":bool=false}` | `-` |
| `sequence.renderAudio` | Render Audio | Sequence | `{"wait":bool=false}` | `-` |
| `sequence.deleteRenderFiles` | Delete Render Files | Sequence | `{}` | `-` |
| `sequence.deleteRenderFilesInToOut` | Delete Render Files In to Out | Sequence | `{}` | `-` |
| ... *and 33 additional `sequence.*` commands* | ... | ... | ... | ... |

### 3.Shortcuts Subsystem: `shortcuts.*` (16 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `shortcuts.list` | List Keyboard Shortcuts | Direct Engine | `{"query":str?,"panel":str?,"assigned":bool?,"platform":"mac|windows|linux"?}` | `-` |
| `shortcuts.get` | Get Shortcuts of a Command | Direct Engine | `{"command":id,"platform":str?}` | `-` |
| `shortcuts.set` | Assign Shortcut | Direct Engine | `{"command":id,"keys":"Cmd+Shift+K","panel":str?,"add":bool?,"keepConflicts":bool?}` | `-` |
| `shortcuts.clear` | Clear Shortcut | Direct Engine | `{"command":id,"keys":str?,"panel":str?}` | `-` |
| `shortcuts.undo` | Undo Shortcut Change | Direct Engine | `{}` | `-` |
| `shortcuts.redo` | Redo Shortcut Change | Direct Engine | `{}` | `-` |
| `shortcuts.conflicts` | Shortcut Conflicts | Direct Engine | `{"platform":"mac|windows|linux"?}` | `-` |
| `shortcuts.forKey` | Shortcuts on a Key | Direct Engine | `{"key":"K","platform":str?}` | `-` |
| `shortcuts.resolve` | Resolve Shortcut | Direct Engine | `{"keys":str,"panel":str?,"platform":str?}` | `-` |
| `shortcuts.presets` | Keyboard Shortcut Presets | Direct Engine | `{}` | `-` |
| `shortcuts.loadPreset` | Load Shortcut Preset | Direct Engine | `{"name":str}` | `-` |
| `shortcuts.savePreset` | Save Shortcut Preset As | Direct Engine | `{"name":str}` | `-` |
| ... *and 4 additional `shortcuts.*` commands* | ... | ... | ... | ... |

### 3.Source Subsystem: `source.*` (7 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `source.open` | Open in Source Monitor | Direct Engine | `{"item":id?,"clip":id?}` | `-` |
| `source.close` | Close | Direct Engine | `{}` | `-` |
| `source.closeAll` | Close All | Direct Engine | `{}` | `-` |
| `source.setPlayhead` | Set Source Playhead | Direct Engine | `{"time":ticks|"frame":i64|"seconds":f64}` | `-` |
| `source.inspect` | Inspect Source Monitor | Direct Engine | `{}` | `-` |
| `source.insert` | Insert | Clip | `{}` | `,` |
| `source.overwrite` | Overwrite | Clip | `{}` | `.` |

### 3.State Subsystem: `state.*` (1 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `state.inspect` | Inspect Editor State | Direct Engine | `{}` | `-` |

### 3.Timeline Subsystem: `timeline.*` (56 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `timeline.place` | Place Clip | Direct Engine | `{"item":id|"items":[id] (back to back, one undo step),"track":"V1"|id|"A1" (sound only)|"new" (a video track after the last)?,"audioTrack":"A1"|id|"new"?,"time":ticks|"frame":i64|"seconds":f64,"insert":bool,"sourceIn":ticks?,"duration":ticks?,"video":bool=true,"audio":bool=true}` | `-` |
| `timeline.select` | Select Clips | Direct Engine | `{"clips":[id],"transitions":[id]?,"add":bool,"toggle":bool,"linked":bool?}` | `-` |
| `timeline.selectGap` | Select Gap | Direct Engine | `{"track":"V1"|id,"time":ticks|"frame":n|"seconds":f}` | `-` |
| `timeline.move` | Move Clips | Direct Engine | `{"moves":[{"clip":id,"track":id|"V2"|"new" (after the last of its kind),"time":ticks}],"insert":bool,"linked":bool?,"copy":bool?}` | `-` |
| `timeline.trim` | Trim Edit | Direct Engine | `{"clip":id,"edge":"in|out","mode":"regular|ripple","delta":ticks|"deltaFrames":i64}` | `-` |
| `timeline.roll` | Rolling Edit | Direct Engine | `{"left":id,"right":id,"delta":ticks|"deltaFrames":i64,"followLinks"?:bool}` | `-` |
| `timeline.slip` | Slip | Direct Engine | `{"clip":id,"delta":ticks|"deltaFrames":i64}` | `-` |
| `timeline.slide` | Slide | Direct Engine | `{"clip":id,"delta":ticks|"deltaFrames":i64}` | `-` |
| `timeline.rateStretch` | Rate Stretch | Direct Engine | `{"clip":id,"edge":"in|out","delta":ticks}` | `-` |
| `timeline.razor` | Razor | Direct Engine | `{"time":ticks,"track":"V1"|id?,"clip":id?}` | `-` |
| `timeline.setTrack` | Track Settings | Direct Engine | `{"track":"V1"|id,"locked":bool?,"syncLock":bool?,"enabled":bool?,"muted":bool?,"solo":bool?,"name":str?,"volumeDb":f64?,"pan":f64?}` | `-` |
| `timeline.setTargeting` | Track Targeting | Direct Engine | `{"track":"V1"|id,"targeted":bool?,"sourcePatch":bool?}` | `-` |
| ... *and 44 additional `timeline.*` commands* | ... | ... | ... | ... |

### 3.Transcript Subsystem: `transcript.*` (14 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `transcript.generate` | Transcribe… | Sequence > Transcript | `{"items":[id]?,"model":"whisper-base"?,"language":"en|auto"?,"diarize":bool?,"maxSpeakers":n?}` | `-` |
| `transcript.set` | Import Transcript | Direct Engine | `{"item":id,"transcript":{"language":str,"speakers":[{"name":str}],"words":[{"text":str,"start":tick,"end":tick,"speaker":n?}]}}` | `-` |
| `transcript.delete` | Delete Transcript | Sequence > Transcript | `{"items":[id]?}` | `-` |
| `transcript.inspect` | Inspect Transcript | Direct Engine | `{"paragraphGapSeconds":f?}` | `-` |
| `transcript.search` | Search Transcript | Direct Engine | `{"query":str}` | `-` |
| `transcript.models` | List Speech Models | Direct Engine | `{}` | `-` |
| `transcript.downloadModel` | Download Speech Model | Direct Engine | `{"model":"whisper-base"?}` | `-` |
| `transcript.select` | Mark Selected Text | Direct Engine | `{"from":word,"to":word?}` | `-` |
| `transcript.extract` | Extract Selected Text | Direct Engine | `{"from":word,"to":word?}` | `-` |
| `transcript.lift` | Lift Selected Text | Direct Engine | `{"from":word,"to":word?}` | `-` |
| `transcript.renameSpeaker` | Rename Speaker… | Direct Engine | `{"speaker":"Speaker 1"|index,"name":str,"item":id?}` | `-` |
| `transcript.removePauses` | Remove Pauses | Sequence > Transcript | `{"minSeconds":f?,"keepSeconds":f?}` | `-` |
| ... *and 2 additional `transcript.*` commands* | ... | ... | ... | ... |

### 3.Trim Subsystem: `trim.*` (24 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `trim.edit` | Trim Edit | Sequence | `{}` | `Shift+T` |
| `trim.applyDefaultTransition` | Apply Default Transitions to Selection | Sequence | `{"clips":[id]?}` | `Shift+D` |
| `trim.selectEditPoint` | Select Edit Point | Direct Engine | `{"clip":id,"edge":"in|out","kind":"trim|ripple|roll","add":bool?}` | `-` |
| `trim.selectNearest` | Select Nearest Edit Point | Direct Engine | `{"kind":"rippleIn|rippleOut|roll|trimIn|trimOut"}` | `-` |
| `trim.clear` | Clear Edit Point Selection | Direct Engine | `{}` | `-` |
| `trim.toggleType` | Toggle Trim Type | Direct Engine | `{}` | `Ctrl+T` |
| `trim.backward` | Trim Backward | Direct Engine | `{}` | `Alt+Left` |
| `trim.forward` | Trim Forward | Direct Engine | `{}` | `Alt+Right` |
| `trim.backwardMany` | Trim Backward Many | Direct Engine | `{}` | `Alt+Shift+Left` |
| `trim.forwardMany` | Trim Forward Many | Direct Engine | `{}` | `Alt+Shift+Right` |
| `trim.shuttle` | Dynamic Trim (Shuttle) | Direct Engine | `{"direction":"forward|reverse","slow":bool?,"clock":seconds}` | `-` |
| `trim.shuttleStop` | Dynamic Trim Stop | Direct Engine | `{"clock":seconds?}` | `-` |
| ... *and 12 additional `trim.*` commands* | ... | ... | ... | ... |

### 3.Tts Subsystem: `tts.*` (7 commands)

| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |
|---|---|---|---|---|
| `tts.voices` | List Narration Voices | Direct Engine | `{}` | `-` |
| `tts.preview` | Preview Narration | Direct Engine | `{"text":str?,"voice":str?,"pitch":"default"?,"pace":f64?,"sample":bool?,"clip":id?,"path":str?}` | `-` |
| `tts.create` | New Narration | Direct Engine | `{"text":str,"voice":str?,"pitch":"extraLow|low|default|high|extraHigh"?,"pace":0.5..2?,"time":ticks?,"track":"A1"|id?,"dir":str?}` | `-` |
| `tts.edit` | Edit Narration | Direct Engine | `{"clip":id?,"text":str?,"voice":str?,"pitch":str?,"pace":f64?,"dir":str?}` | `-` |
| `tts.inspect` | Inspect Narration | Direct Engine | `{"clip":id?,"item":id?}` | `-` |
| `tts.render` | Synthesize Narration | Direct Engine | `{"text":str?,"voice":str?,"pitch":str?,"pace":f64?,"sample":bool?,"clip":id?,"wait":bool?}` | `-` |
| `tts.downloadVoices` | Download Natural Voices | Direct Engine | `{"wait":bool?}` | `-` |

---

## 4. Master Skill Command Translation Matrix ([480]–[529])

The 50 Skill Master Commands defined in Cluster 09 are mapped directly to native FilmCraft CLI execution via `filmcraft_cli_bridge.py`:

| Skill Master Command | FilmCraft CLI Action | Bound Native Commands | Parameter Translation | Schema Lock Verification |
|---|---|---|---|---|
| `CMD_INGEST_VERIFY_MEDIA_HASHES` [480] | `filmcraft-cli probe` | `media.status`, `events.list` | `media_path`, algorithm (`xxHash64`) | `[014]` Ingest Manifest |
| `CMD_INGEST_PARSE_CAMERA_METADATA` [481] | `filmcraft-cli probe` | `media.colorInfo`, `metadata.get` | Sensor gamut, ISO, white balance | `[014]` Ingest Manifest |
| `CMD_INGEST_SYNC_MULTICAM_AND_AUDIO` [482] | `filmcraft-cli exec` | `multicam.switchAngle`, `multicam.audioFollowsVideo` | Waveform cross-correlation offset | `[014]` Sync Map |
| `CMD_INGEST_LOAD_TIMED_TRANSCRIPT` [483] | `filmcraft-cli exec` | `transcript.generate`, `transcript.inspect` | ASR word/phoneme millisecond bounds | `[015]` Word-Level Transcript |
| `CMD_EDIT_COMPILE_ASSEMBLY_SEQUENCE` [490] | `filmcraft-cli exec` | `timeline.place`, `sequence.open` | `clip_id`, `start_smpte`, `end_smpte` | `[017]` EDL Cut Manifest |
| `CMD_EDIT_REFINE_ROUGH_TO_FINE_CUT` [491] | `filmcraft-cli exec` | `timeline.razor`, `timeline.move`, `timeline.trim` | Micro-trims in integer frames | `[017]` EDL Cut Manifest |
| `CMD_EDIT_CALCULATE_JL_SPLIT_TRANSITIONS` [492] | `filmcraft-cli exec` | `trim.edit`, `markers.markSplitVideoIn` | Audio lead/lag offset `[-14..+18]` frames | `[017]` EDL Cut Manifest |
| `CMD_COLOR_ANALYZE_SCOPES` [498] | `filmcraft-cli exec` | `scopes.read` | Real-time waveform & vectorscope telemetry | `[019]` Color Grade Spec |
| `CMD_COLOR_SET_PRIMARY_BALANCE` [500] | `filmcraft-cli exec` | `lumetri.setLook`, `effects.setParam` | Lift, Gamma, Gain, Offset RGB | `[019]` Color Grade Spec |
| `CMD_COLOR_APPLY_FILM_LOOK_AND_FX` [504] | `filmcraft-cli exec` | `lut.import`, `lumetri.setInputLut` | Kodak 2383 / Print profile, Halation radius | `[019]` Color Grade Spec |
| `CMD_SUB_SEGMENT_CUES` [507] | `filmcraft-cli exec` | `captions.newTrack`, `captions.add` | `start_tc`, `end_tc`, text lines | `[021]` Timed-Text Cue List |
| `CMD_SUB_SNAP_TO_SHOT_CHANGES` [510] | `filmcraft-cli exec` | `playhead.step`, `captions.add` | Snap to cut if gap in `[2..11]` frames | `[021]` Timed-Text Cue List |
| `CMD_SOUND_CLEAN_AND_LEVEL_DIALOGUE` [515] | `filmcraft-cli exec` | `essentialSound.setType`, `essentialSound.set` | Dialogue RMS leveling, noise floor clamp | `[023]` Dialogue EDL |
| `CMD_SOUND_ALIGN_MUSIC_AND_DUCKING` [519] | `filmcraft-cli exec` | `essentialSound.set`, `mixer.setValue` | Sidechain ducking `-4.0dB` to `-6.0dB` | `[025]` Mix Specification |
| `CMD_SOUND_CALIBRATE_LUFS_AND_TRUE_PEAK` [520] | `filmcraft-cli exec` | `mixer.inspect`, `mixer.setValue` | `-23.0 LUFS` integrated, `-1.0 dBTP` ceiling | `[025]` Mix Specification |
| `CMD_FINISH_CONFIGURE_MASTER_CODEC` [525] | `filmcraft-cli exec` | `export.presets.save`, `export.presets.list` | ProRes 422 HQ / DNxHR HQX, NCLC tags | `[028]` Delivery Spec |
| `CMD_FINISH_RUN_AUTOMATED_QC_GATES` [527] | `filmcraft-cli exec` | `scopes.read`, `mixer.inspect`, `perf.stats` | Gamut, flash frame, and loudness audit | `[029]` QC Gate Report |

---

## 5. Programmatic Execution Recipes

### Recipe A: Executing a Timeline Razor Cut from Python
```python
from filmcraft_cli_bridge import execute_native_command

# Cut active timeline at exactly 10.5 seconds (or frame 252 at 24fps)
result = execute_native_command('timeline.razor', {'seconds': 10.5})
if result['returncode'] == 0:
    print('Razor cut successful:', result['stdout'])
else:
    print('Cut error:', result['stderr'])
```

### Recipe B: Invoking a Skill Master Command
```python
from filmcraft_cli_bridge import route_skill_command

# Execute Skill Master Command [491] to refine edit
res = route_skill_command('CMD_EDIT_REFINE_ROUGH_TO_FINE_CUT', {'seconds': 14.25})
print('Route status:', res['status'])
```

### Recipe C: Shell One-Liner via CLI
```bash
# Query active timeline scopes directly through live GUI
filmcraft-cli --bridge 127.0.0.1:9876 exec scopes.read

# Apply Lumetri look preset
filmcraft-cli --bridge 127.0.0.1:9876 exec lumetri.applyPreset '{"preset":"WarmCinematic_D60"}'
```

---

## 6. Auto-Remediation Feedback Loop

When a FilmCraft CLI execution returns non-zero (`returncode != 0`), the bridge automatically converts the error into a structured exception code routed to `[012] Error Taxonomy and Auto-Remediation Loop`:
1. **Parameter Out of Range**: Normalized against Parameter Reference Tables `[530]`–`[565]`.
2. **Missing Media / Offline Frame**: Rerouted to `[027] Online Conform Relink Map`.
3. **Loudness / Gamut Excursion**: Clamped by `[248]` Soft-Clip Gamut or `[325]` Brickwall Limiter.
4. **3rd Failure Escalation**: Pauses execution and requests human review under `[006]` Human-in-the-Loop Escalation Matrix.
