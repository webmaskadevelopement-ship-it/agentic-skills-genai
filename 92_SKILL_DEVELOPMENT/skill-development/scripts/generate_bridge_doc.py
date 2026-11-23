#!/usr/bin/env python3
"""
Generate FILMCRAFT_COMMAND_ROUTING_BRIDGE.md
Documents all 701 FilmCraft commands and their bidirectional linkage
to the Autonomous Post-Production Monorepo Skills ([001]-[720]).
"""

import json
import os

COMMANDS_FILE = "/tmp/filmcraft_commands.json"
DOC_PATH = "/Volumes/DISK 1/AGENTS TRAIN/EDITING_SYSTEM/skill-development/skills/autonomous-post-production-ai-monorepo/FILMCRAFT_COMMAND_ROUTING_BRIDGE.md"

with open(COMMANDS_FILE) as f:
    cmds = json.load(f)

by_cat = {}
for c in cmds:
    prefix = c["id"].split(".")[0]
    by_cat.setdefault(prefix, []).append(c)

lines = []
lines.append("# FilmCraft CLI Engine & Autonomous Skill Routing Bridge")
lines.append("")
lines.append("## Executive Overview & Architectural Contract")
lines.append("")
lines.append("This document establishes the bidirectional execution contract between the **Autonomous Post-Production Monorepo** (720 files, `[001]` through `[720]`) and the **FilmCraft Open-Source Video Editing Application** (701 native engine commands, headless CLI, and live GUI loopback control).")
lines.append("")
lines.append("Every post-production decision made by an autonomous agent—whether calculating an editorial cut on transient, neutralizing a color temperature cast, ducking underscore music, or snapping subtitle cues—is mathematically resolved under the Monorepo specifications and deterministically dispatched to FilmCraft through this bridge.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 1. Dual-Mode Execution Topology")
lines.append("")
lines.append("FilmCraft supports two interoperable execution modes governed by this bridge:")
lines.append("")
lines.append("```")
lines.append("  [ Autonomous Post-Production Monorepo Skills ([001]-[720]) ]")
lines.append("                              │")
lines.append("                              ▼")
lines.append("  [ FilmCraft Skill Bridge Layer (filmcraft_cli_bridge.py) ]")
lines.append("                              │")
lines.append("            ┌─────────────────┴─────────────────┐")
lines.append("            ▼                                   ▼")
lines.append("   MODE A: LIVE GUI BRIDGE             MODE B: HEADLESS ENGINE")
lines.append("   (filmcraft --control 9876)          (filmcraft-cli --project <p>)")
lines.append("   • Real-time visual feedback         • High-speed background renders")
lines.append("   • Live timeline scrubbing           • Batch transcoding & proxying")
lines.append("   • Interactive user pairing          • Headless CI/CD test passes")
lines.append("   • Socket JSON-RPC over loopback     • Direct project file serialization")
lines.append("```")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 2. Directory of Accepted FilmCraft Commands (701 Native Commands)")
lines.append("")
lines.append("FilmCraft exposes **701 native engine commands** divided across **42 functional subsystems**. All commands accept integer ticks (`254,016,000,000` ticks/sec) or fractional seconds (`seconds=12.5`), track indices, or JSON parameter payloads.")
lines.append("")
lines.append("| Functional Subsystem | Command Count | Primary Domain Responsibility | Monorepo Cluster Mapping |")
lines.append("|---|---|---|---|")

cluster_map = {
    "timeline": "Cluster 02: Editorial Craft (`[101]`–`[176]`) & Master Cmds (`[486]`–`[496]`)",
    "trim": "Cluster 02: Editorial Craft (`[101]`–`[176]`) & Master Cmds (`[491]`, `[492]`)",
    "clip": "Cluster 01: Ingest (`[031]`–`[100]`) & Cluster 02: Editorial (`[101]`–`[176]`)",
    "edit": "Cluster 02: Editorial Craft (`[101]`–`[176]`)",
    "sequence": "Cluster 02: Editorial Craft (`[101]`–`[176]`) & Cluster 07: Finishing (`[410]`–`[453]`)",
    "project": "Cluster 00: Governance (`[001]`–`[030]`) & Cluster 01: Ingest (`[031]`–`[100]`)",
    "file": "Cluster 00: Governance (`[001]`–`[030]`) & Cluster 01: Ingest (`[031]`–`[100]`)",
    "multicam": "Cluster 01: Ingest & Assistant Editing (`[031]`–`[100]`) & Cmd `[482]`",
    "markers": "Cluster 02: Editorial Craft (`[101]`–`[176]`) & Cluster 05: Subtitling (`[335]`–`[377]`)",
    "playhead": "Cluster 02: Editorial Craft (`[101]`–`[176]`) & Precision Navigation",
    "lumetri": "Cluster 03: Color Grading & Look Dev (`[177]`–`[266]`) & Cmds `[497]`–`[506]`",
    "lut": "Cluster 03: Color Grading & Look Dev (`[177]`–`[266]`) & Cmd `[504]`",
    "scopes": "Cluster 03: Color Grading & Look Dev (`[177]`–`[266]`) & Cmd `[498]`",
    "color": "Cluster 03: Color Grading & Look Dev (`[177]`–`[266]`)",
    "mixer": "Cluster 04: Sound Design & Mixing (`[267]`–`[334]`) & Cmds `[515]`–`[522]`",
    "clipMixer": "Cluster 04: Sound Design & Mixing (`[267]`–`[334]`) & Cmd `[517]`",
    "essentialSound": "Cluster 04: Sound Design & Mixing (`[267]`–`[334]`) & Cmds `[515]`, `[519]`",
    "audio": "Cluster 04: Sound Design & Mixing (`[267]`–`[334]`) & Voiceover Sync",
    "tts": "Cluster 04: Sound Design & Mixing (`[267]`–`[334]`) & Scratch ADR",
    "captions": "Cluster 05: Subtitling & Captioning (`[335]`–`[377]`) & Cmds `[507]`–`[514]`",
    "transcript": "Cluster 01: Ingest (`[031]`–`[100]`) & Cluster 05: Subtitling (`[335]`–`[377]`)",
    "graphics": "Cluster 06: VFX & Motion Graphics (`[378]`–`[409]`) & Lower Thirds",
    "masks": "Cluster 03: Color Qualifiers & Cluster 06: VFX Clean Plates",
    "effects": "Cluster 03: Color (`[177]`), Cluster 04: Sound (`[267]`), Cluster 06: VFX (`[378]`)",
    "media": "Cluster 01: Ingest (`[031]`–`[100]`) & Cluster 06: Online Conform (`[523]`)",
    "mediaBrowser": "Cluster 01: Ingest (`[031]`–`[100]`)",
    "export": "Cluster 07: Finishing, Mastering & QC (`[410]`–`[453]`) & Cmds `[525]`–`[529]`",
    "jobs": "Cluster 07: Finishing & Background Queue (`[410]`–`[453]`)",
    "perf": "Cluster 11: Validation (`[566]`–`[592]`) & Telemetry Logging",
    "state": "Cluster 00: Governance & Cross-Department DAG (`[001]`–`[002]`)"
}

for cat in sorted(by_cat.keys()):
    cnt = len(by_cat[cat])
    mapped_target = cluster_map.get(cat, "General Post-Production Support / Utilities")
    lines.append(f"| `{cat}.*` | **{cnt}** | Subsystem governing `{cat}` | {mapped_target} |")

lines.append("")
lines.append("---")
lines.append("")
lines.append("## 3. Subsystem Deep-Dive & Representative Command Signatures")
lines.append("")

for cat in sorted(by_cat.keys()):
    items = by_cat[cat]
    lines.append(f"### 3.{cat.capitalize()} Subsystem: `{cat}.*` ({len(items)} commands)")
    lines.append("")
    lines.append("| Command ID | Label / Action | Menu Path | Parameter Schema | Default Shortcut |")
    lines.append("|---|---|---|---|---|")
    for it in items[:12]:
        cid = it["id"]
        lbl = it.get("label", "") or cid.split(".")[-1]
        menu = " > ".join(it.get("menu", [])) if it.get("menu") else "Direct Engine"
        params = it.get("params", "{}")
        short = it.get("shortcut", "") or "-"
        lines.append(f"| `{cid}` | {lbl} | {menu} | `{params}` | `{short}` |")
    if len(items) > 12:
        lines.append(f"| ... *and {len(items) - 12} additional `{cat}.*` commands* | ... | ... | ... | ... |")
    lines.append("")

lines.append("---")
lines.append("")
lines.append("## 4. Master Skill Command Translation Matrix ([480]–[529])")
lines.append("")
lines.append("The 50 Skill Master Commands defined in Cluster 09 are mapped directly to native FilmCraft CLI execution via `filmcraft_cli_bridge.py`:")
lines.append("")
lines.append("| Skill Master Command | FilmCraft CLI Action | Bound Native Commands | Parameter Translation | Schema Lock Verification |")
lines.append("|---|---|---|---|---|")
lines.append("| `CMD_INGEST_VERIFY_MEDIA_HASHES` [480] | `filmcraft-cli probe` | `media.status`, `events.list` | `media_path`, algorithm (`xxHash64`) | `[014]` Ingest Manifest |")
lines.append("| `CMD_INGEST_PARSE_CAMERA_METADATA` [481] | `filmcraft-cli probe` | `media.colorInfo`, `metadata.get` | Sensor gamut, ISO, white balance | `[014]` Ingest Manifest |")
lines.append("| `CMD_INGEST_SYNC_MULTICAM_AND_AUDIO` [482] | `filmcraft-cli exec` | `multicam.switchAngle`, `multicam.audioFollowsVideo` | Waveform cross-correlation offset | `[014]` Sync Map |")
lines.append("| `CMD_INGEST_LOAD_TIMED_TRANSCRIPT` [483] | `filmcraft-cli exec` | `transcript.generate`, `transcript.inspect` | ASR word/phoneme millisecond bounds | `[015]` Word-Level Transcript |")
lines.append("| `CMD_EDIT_COMPILE_ASSEMBLY_SEQUENCE` [490] | `filmcraft-cli exec` | `timeline.place`, `sequence.open` | `clip_id`, `start_smpte`, `end_smpte` | `[017]` EDL Cut Manifest |")
lines.append("| `CMD_EDIT_REFINE_ROUGH_TO_FINE_CUT` [491] | `filmcraft-cli exec` | `timeline.razor`, `timeline.move`, `timeline.trim` | Micro-trims in integer frames | `[017]` EDL Cut Manifest |")
lines.append("| `CMD_EDIT_CALCULATE_JL_SPLIT_TRANSITIONS` [492] | `filmcraft-cli exec` | `trim.edit`, `markers.markSplitVideoIn` | Audio lead/lag offset `[-14..+18]` frames | `[017]` EDL Cut Manifest |")
lines.append("| `CMD_COLOR_ANALYZE_SCOPES` [498] | `filmcraft-cli exec` | `scopes.read` | Real-time waveform & vectorscope telemetry | `[019]` Color Grade Spec |")
lines.append("| `CMD_COLOR_SET_PRIMARY_BALANCE` [500] | `filmcraft-cli exec` | `lumetri.setLook`, `effects.setParam` | Lift, Gamma, Gain, Offset RGB | `[019]` Color Grade Spec |")
lines.append("| `CMD_COLOR_APPLY_FILM_LOOK_AND_FX` [504] | `filmcraft-cli exec` | `lut.import`, `lumetri.setInputLut` | Kodak 2383 / Print profile, Halation radius | `[019]` Color Grade Spec |")
lines.append("| `CMD_SUB_SEGMENT_CUES` [507] | `filmcraft-cli exec` | `captions.newTrack`, `captions.add` | `start_tc`, `end_tc`, text lines | `[021]` Timed-Text Cue List |")
lines.append("| `CMD_SUB_SNAP_TO_SHOT_CHANGES` [510] | `filmcraft-cli exec` | `playhead.step`, `captions.add` | Snap to cut if gap in `[2..11]` frames | `[021]` Timed-Text Cue List |")
lines.append("| `CMD_SOUND_CLEAN_AND_LEVEL_DIALOGUE` [515] | `filmcraft-cli exec` | `essentialSound.setType`, `essentialSound.set` | Dialogue RMS leveling, noise floor clamp | `[023]` Dialogue EDL |")
lines.append("| `CMD_SOUND_ALIGN_MUSIC_AND_DUCKING` [519] | `filmcraft-cli exec` | `essentialSound.set`, `mixer.setValue` | Sidechain ducking `-4.0dB` to `-6.0dB` | `[025]` Mix Specification |")
lines.append("| `CMD_SOUND_CALIBRATE_LUFS_AND_TRUE_PEAK` [520] | `filmcraft-cli exec` | `mixer.inspect`, `mixer.setValue` | `-23.0 LUFS` integrated, `-1.0 dBTP` ceiling | `[025]` Mix Specification |")
lines.append("| `CMD_FINISH_CONFIGURE_MASTER_CODEC` [525] | `filmcraft-cli exec` | `export.presets.save`, `export.presets.list` | ProRes 422 HQ / DNxHR HQX, NCLC tags | `[028]` Delivery Spec |")
lines.append("| `CMD_FINISH_RUN_AUTOMATED_QC_GATES` [527] | `filmcraft-cli exec` | `scopes.read`, `mixer.inspect`, `perf.stats` | Gamut, flash frame, and loudness audit | `[029]` QC Gate Report |")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 5. Programmatic Execution Recipes")
lines.append("")
lines.append("### Recipe A: Executing a Timeline Razor Cut from Python")
lines.append("```python")
lines.append("from filmcraft_cli_bridge import execute_native_command")
lines.append("")
lines.append("# Cut active timeline at exactly 10.5 seconds (or frame 252 at 24fps)")
lines.append("result = execute_native_command('timeline.razor', {'seconds': 10.5})")
lines.append("if result['returncode'] == 0:")
lines.append("    print('Razor cut successful:', result['stdout'])")
lines.append("else:")
lines.append("    print('Cut error:', result['stderr'])")
lines.append("```")
lines.append("")
lines.append("### Recipe B: Invoking a Skill Master Command")
lines.append("```python")
lines.append("from filmcraft_cli_bridge import route_skill_command")
lines.append("")
lines.append("# Execute Skill Master Command [491] to refine edit")
lines.append("res = route_skill_command('CMD_EDIT_REFINE_ROUGH_TO_FINE_CUT', {'seconds': 14.25})")
lines.append("print('Route status:', res['status'])")
lines.append("```")
lines.append("")
lines.append("### Recipe C: Shell One-Liner via CLI")
lines.append("```bash")
lines.append("# Query active timeline scopes directly through live GUI")
lines.append("filmcraft-cli --bridge 127.0.0.1:9876 exec scopes.read")
lines.append("")
lines.append("# Apply Lumetri look preset")
lines.append("filmcraft-cli --bridge 127.0.0.1:9876 exec lumetri.applyPreset '{\"preset\":\"WarmCinematic_D60\"}'")
lines.append("```")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 6. Auto-Remediation Feedback Loop")
lines.append("")
lines.append("When a FilmCraft CLI execution returns non-zero (`returncode != 0`), the bridge automatically converts the error into a structured exception code routed to `[012] Error Taxonomy and Auto-Remediation Loop`:")
lines.append("1. **Parameter Out of Range**: Normalized against Parameter Reference Tables `[530]`–`[565]`.")
lines.append("2. **Missing Media / Offline Frame**: Rerouted to `[027] Online Conform Relink Map`.")
lines.append("3. **Loudness / Gamut Excursion**: Clamped by `[248]` Soft-Clip Gamut or `[325]` Brickwall Limiter.")
lines.append("4. **3rd Failure Escalation**: Pauses execution and requests human review under `[006]` Human-in-the-Loop Escalation Matrix.")

os.makedirs(os.path.dirname(DOC_PATH), exist_ok=True)
with open(DOC_PATH, "w") as f:
    f.write("\n".join(lines) + "\n")

print(f"Created {DOC_PATH} with {len(lines)} lines.")
