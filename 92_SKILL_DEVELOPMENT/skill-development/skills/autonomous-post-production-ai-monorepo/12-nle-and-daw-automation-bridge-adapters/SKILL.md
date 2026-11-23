---
file_id: "[593]"
skill_path: "12-nle-and-daw-automation-bridge-adapters/SKILL.md"
role: "Department Router: NLE & DAW Automation Bridge Adapters"
parent_router: "[001]"
child_nodes:
  - "[594]" # adapter-resolve-python-lua-project-and-media-pool
  - "[595]" # adapter-resolve-timeline-assembly-from-json-edl
  - "[596]" # adapter-resolve-color-node-graph-and-cdl-injector
  - "[597]" # adapter-resolve-render-queue-and-preset-executor
  - "[598]" # adapter-resolve-fairlight-audio-track-and-lufs
  - "[599]" # adapter-premiere-extendscript-uxp-sequence-builder
  - "[600]" # adapter-premiere-lumetri-color-parameter-mapper
  - "[601]" # adapter-premiere-essential-graphics-mogrt-injector
  - "[602]" # adapter-after-effects-aerender-vfx-comp-automator
  - "[603]" # adapter-avid-ale-avid-log-exchange-generator
  - "[604]" # adapter-avid-subcap-ds-caption-file-generator
  - "[605]" # adapter-pro-tools-ptsl-scripting-sdk-session-setup
  - "[606]" # adapter-pro-tools-clip-gain-and-eq3-automation
  - "[607]" # adapter-ffmpeg-frame-accurate-proxy-and-burnin
  - "[608]" # adapter-ffmpeg-ebur128-loudness-two-pass-normalizer
  - "[609]" # adapter-ffmpeg-blackdetect-freezedetect-silencedetect
  - "[610]" # adapter-openeffects-ofx-and-ociocheck-cli-bridge
schema_locks:
  - "[017]"
  - "[019]"
  - "[022]"
  - "[025]"
  - "[028]"
---

# [593] Department Router: NLE & DAW Automation Bridge Adapters

## 1. Operational Boundary & Bridge Overview

This department translates schema-locked JSON specifications (Files A through E) into **executable host commands, automation scripts, and native API calls** across professional post-production software:
* **FilmCraft (Native MCP Bridge)**: Direct JSON-RPC execution via stdio/TCP control port 9876.
* **DaVinci Resolve (`[594]`–`[598]`)**: Python 3 / Lua `DaVinciResolveScript` APIs for Media Pool, Timeline, Color Nodes, Fairlight, and Deliver.
* **Adobe Premiere & After Effects (`[599]`–`[602]`)**: ExtendScript / UXP sequence assembly, Lumetri parameter mapping, and headless `aerender`.
* **Avid Media Composer & Pro Tools (`[603]`–`[606]`)**: ALE logs, SubCap captions, and Pro Tools Scripting SDK (PTSL gRPC).
* **FFmpeg & OCIO CLI (`[607]`–`[610]`)**: Frame-accurate proxy burn-ins, EBU R128 loudness normalization, and automated black/freeze/silence QC scanning.

---

## 2. Host Application Dispatch Matrix

| Target Host NLE/DAW | Input Specification | Adapter Script File | Execution Mechanism | Telemetry Output |
|---|---|---|---|---|
| **FilmCraft (Live GUI)** | Files A, B, C, D | `filmcraft-mcp-bridge.py` | Native MCP tool calls (`command_run`, `ui_click`, `ui_drag`) | Real-time GUI viewport update & PNG screenshots |
| **DaVinci Resolve** | File A (`[017]`), File B (`[019]`) | `[594]`, `[595]`, `[596]` | Python `resolve.GetMediaPool().AppendToTimeline()` | Timeline Item IDs & DRX node grade tree |
| **Resolve Fairlight** | File D (`[025]`) | `[598]` | Python Fairlight Bus & Track Level API | Bus LUFS meter verification |
| **Adobe Premiere Pro** | File A (`[017]`), File B (`[019]`) | `[599]`, `[600]` | ExtendScript `qe.project.newSequence()` & Lumetri map | Active sequence item tracks & Lumetri effect params |
| **Avid Pro Tools** | File D (`[025]`) | `[605]`, `[606]` | PTSL gRPC protobuf `CreateSession` & `ImportAAF` | Pro Tools track allocation & clip-gain automation |
| **FFmpeg CLI** | Files A–E | `[607]`, `[608]`, `[609]` | Headless subprocess execution | Transcoded media files & machine-readable QC logs |

---

## 3. FilmCraft Native MCP Bridge Protocol

When executing inside FilmCraft, the agent maps commands directly without exporting intermediate XML/EDL files:
1. `timeline.place`: Ingests `event_id`, `item`, `track`, `seconds` / `ticks`.
2. `timeline.razor`: Ingests `seconds` or `timecode` to split clips.
3. `edit.rippleDelete`: Excises selected range and closes gap instantly.
4. `effects.apply` & `effects.setParam`: Ingests `clip`, `effect: "lumetri"`, `param`, `value`.
5. `ui_elements` & `ui_click`: Drives panels, buttons, and workspaces in the live desktop app.
6. `render_preview` & `ui_screenshot`: Visual verification loop.

---

## 4. Master FilmCraft 701-Command Bridge Directory

For the complete catalog of all 701 native FilmCraft commands, parameter schemas, and the 50 Master Command routing matrix, refer to:
- [FILMCRAFT_COMMAND_ROUTING_BRIDGE.md](file:///Volumes/DISK%201/AGENTS%20TRAIN/EDITING_SYSTEM/skill-development/skills/autonomous-post-production-ai-monorepo/FILMCRAFT_COMMAND_ROUTING_BRIDGE.md)
- [filmcraft_cli_bridge.py](file:///Volumes/DISK%201/AGENTS%20TRAIN/EDITING_SYSTEM/filmcraft_cli_bridge.py)

