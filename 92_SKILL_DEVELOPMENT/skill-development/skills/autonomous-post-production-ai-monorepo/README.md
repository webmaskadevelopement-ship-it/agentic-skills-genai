# Autonomous Post-Production AI Monorepo

> **720-File Production-Grade Knowledge Base, Skill Execution Engine & Autonomous Finishing Pipeline for Professional Film, Television, Commercials, and Digital Video.**

---

## 1. System Identity & Anti-Shallowness Constitution

This repository governs the complete post-production workflow through **720 deterministic, math-backed, and schema-locked markdown skills** (`[001]` through `[720]`).

### The Anti-Shallowness Iron Law
Under no circumstances does any skill or runtime output in this monorepo emit vague or unanchored advice. Every statement is strictly bound to measurable physical, colorimetric, acoustic, or temporal parameters:
* **Color**: Cites Waveform IRE bounds (black floor 2–5 IRE, specular ceiling 95–99 IRE), Vectorscope 123° I-line skin alignment, and RGB Parade channel balance.
* **Editorial**: Cites exact frame math, Walter Murch Rule of Six weighting, millisecond dead pause thresholds, and explicit take selection/disqualification rationale.
* **Sound**: Cites ITU-R BS.1770-4 integrated loudness (-23.0 LUFS EBU / -24.0 LKFS ATSC / -27.0 LKFS Netflix), True Peak dBTP ceilings, and mathematical DME stem parity.
* **Subtitles**: Cites Characters Per Second (CPS <= 20.0), Characters Per Line (CPL <= 42), millisecond duration bounds [833ms, 7000ms], and shot-change dead zone snapping [2..11 frames].
* **Finishing**: Enforces all 9 Automated Quality Control (QC) Gates before master release sign-off.

---

## 2. Directory Architecture & Cluster Index

```
autonomous-post-production-ai-monorepo/
│
├── [001] SKILL.md                                  # Master Root Router, Intent Classifier & Global Contract
├── [002] AGENTS.md                                 # Multi-Agent Swarm Topology, Department Hand-offs & State Machine
├── [003] README.md                                 # System Architecture, Execution Pipeline & Monorepo Index
│
├── 00-governance-and-schemas/                      # [004]–[030] Stage-gate rules, evidence contracts & JSON Schema locks
├── 01-ingest-dailies-and-assistant-editing/        # [031]–[100] Checksum offload, camera metadata, sync & bin architecture
├── 02-editorial-craft-selects-and-pacing/          # [101]–[176] Selects scoring, Murch Rule of Six, J/L cuts & EDL manifests
├── 03-color-grading-and-look-development/          # [177]–[266] ACES/DWG transforms, 12-node pipeline, scopes & film looks
├── 04-sound-design-dialogue-foley-and-mixing/      # [267]–[334] Dialogue restoration, foley, ducking & LUFS mastering
├── 05-subtitling-captioning-and-localization/      # [335]–[377] CPS/CPL math, syntactic breaks, SDH, SRT/VTT/IMSC1
├── 06-vfx-motion-graphics-cleanup-and-conforming/  # [378]–[409] RAW relinking, EXR plate pulls, roto & safe areas
├── 07-finishing-mastering-and-automated-qc/        # [410]–[453] Mezzanine codecs, leaders/2-pops & 9 Automated QC Gates
├── 08-specialized-genre-and-format-playbooks/      # [454]–[478] Narrative cinema, documentary, commercials & YouTube
├── 09-skill-master-commands-and-procedures/        # [479]–[529] 50 Deterministic Skill Master Commands
├── 10-fine-grained-parameter-reference-tables/     # [530]–[565] 35 Constant lookup matrices (SMPTE, Kelvin, LUFS, etc.)
├── 11-deterministic-validation-and-calculation-specs/ # [566]–[592] 26 Executable Python validation assertion gates
├── 12-nle-and-daw-automation-bridge-adapters/      # [593]–[610] Resolve, Premiere, Avid, Pro Tools & FilmCraft MCP bridges
├── 13-production-grade-golden-examples-and-templates/ # [611]–[633] 22 Unabridged few-shot exemplars (Files A–E)
└── 14-edge-cases-troubleshooting-and-recovery-protocols/ # [634]–[720] Anomaly remediation & system meta-orchestration
```

---

## 3. The 5 Core Master Deliverables

Every production milestone emits schema-locked JSON manifests accompanied by human-readable Markdown spec sheets:

| Deliverable | Description | Primary Router | Schema Lock | Master Command | Validator Gate |
|---|---|---|---|---|---|
| **File A** | **Edit Decision List (EDL) / Cut Manifest** | `[101]` | `[017]` | `EMIT_EDL_MANIFEST` (`[496]`) | `[567]`–`[572]` |
| **File B** | **Color Grading Specification** | `[177]` | `[019]` | `EMIT_GRADE_SPEC` (`[506]`) | `[573]`–`[578]` |
| **File C** | **Subtitle / Timed Text & Compliance Report** | `[335]` | `[021]`/`[022]` | `EMIT_COMPLIANCE_REPORT` (`[514]`) | `[579]`–`[584]` |
| **File D** | **Sound Design & Mix Specification** | `[267]` | `[023]`–`[025]` | `EMIT_MIX_SPEC` (`[522]`) | `[585]`–`[589]` |
| **File E** | **Master Delivery & Finishing Spec Sheet** | `[410]` | `[028]`–`[030]` | `EMIT_DELIVERY_SPEC` (`[529]`) | `[590]`–`[592]` |

---

## 4. Live NLE Execution via FilmCraft MCP Bridge

This monorepo is natively integrated with **FilmCraft Desktop Video Editor** over Model Context Protocol (MCP):
* **Engine Commands**: The 50 Skill Master Commands (`[480]`–`[529]`) map directly into FilmCraft's 701 engine commands via `command_run` and `command_batch`.
* **GUI Driving**: The AI agent uses synthetic UI tools (`ui_elements`, `ui_click`, `ui_drag`, `ui_key`, `ui_type`) to control the timeline, panels, and scopes live on your monitor.
* **Visual Telemetry**: The agent verifies every cut and grade in real time via `ui_screenshot` and `render_preview`.

---

## 5. Editing Taxonomy Templates & Command Routing Directory

- **39-Style Editing Taxonomy Templates**: [editing-templates/INDEX.md](file:///Volumes/DISK%201/AGENTS%20TRAIN/EDITING_SYSTEM/skill-development/editing-templates/INDEX.md)
  - 4 Paradigms (Linear, NLE, Offline, Online)
  - 6 Narrative Styles (Continuity, Montage, Classical, Experimental, Narrative, Discontinuous)
  - 14 Format Genres (Documentary, Podcast, Vlog, Broadcast News, Commercial, Social 9:16, Trailer, Reality TV, Music Video, Sports, Corporate, Educational, Wedding, Animation)
  - 15 Technique-Level Methods (Cut on Action, Jump Cut, Match Cut, Parallel, Shot/Reverse Shot, J/L Cut, Kuleshov, Cross-Cutting, Optical Wipes, Split Screen, Speed Ramping, Beat Editing, Kinetic Typography, Contrast, Elliptical)
- **FilmCraft 701-Command Bridge Specification**: [FILMCRAFT_COMMAND_ROUTING_BRIDGE.md](file:///Volumes/DISK%201/AGENTS%20TRAIN/EDITING_SYSTEM/skill-development/skills/autonomous-post-production-ai-monorepo/FILMCRAFT_COMMAND_ROUTING_BRIDGE.md)
- **Python CLI Bridge Engine**: [filmcraft_cli_bridge.py](file:///Volumes/DISK%201/AGENTS%20TRAIN/EDITING_SYSTEM/filmcraft_cli_bridge.py)

