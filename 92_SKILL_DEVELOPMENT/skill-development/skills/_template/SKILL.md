---
name: professional-editing-skill-template
description: Production-grade template for building autonomous editing skills. Dispatches to FilmCraft MCP and CLI commands, enforces SMPTE/EBU/ITU standards, and integrates the 39-style Editing Taxonomy.
---

# Professional Post-Production Skill Template

## 1. Skill Identity & Purpose
This template provides the standardized, non-shallow engineering structure for authoring autonomous post-production editing skills.
It links:
1. **The 39 Editing Taxonomy Templates** ([editing-templates/INDEX.md](file:///Volumes/DISK%201/AGENTS%20TRAIN/EDITING_SYSTEM/skill-development/editing-templates/INDEX.md))
2. **The 720-File Autonomous Post-Production Monorepo** ([autonomous-post-production-ai-monorepo](file:///Volumes/DISK%201/AGENTS%20TRAIN/EDITING_SYSTEM/skill-development/skills/autonomous-post-production-ai-monorepo))
3. **FilmCraft Native CLI & MCP Commands** (701 commands mapped via [FILMCRAFT_COMMAND_ROUTING_BRIDGE.md](file:///Volumes/DISK%201/AGENTS%20TRAIN/EDITING_SYSTEM/skill-development/skills/autonomous-post-production-ai-monorepo/FILMCRAFT_COMMAND_ROUTING_BRIDGE.md))

---

## 2. Universal 6-Phase Execution Workflow

### Phase 1: Telemetry & State Inspection
Before modifying any timeline:
- Inspect active sequence via `sequence_inspect` or `filmcraft_cli_bridge.py inspect sequence`.
- Query current playhead tick: $T = Frame \times 10,594,560,000$ (at 23.976 fps).
- Extract source audio/video parameters (sample rate, channels, color space, middle grey IRE).

### Phase 2: Narrative & Temporal Math Calculation
- Quantize cut points to integer frames and musical beat boundaries (BPM division).
- Calculate J/L split edit frame offsets:
  - Audio Lead (J-Cut): $-8$ to $-16$ frames.
  - Video Lead (L-Cut): $+10$ to $+24$ frames.
- Enforce 180° action axis and eyeline pupil height parity ($\le 3\%$ delta).

### Phase 3: FilmCraft Native Command Dispatch
- Execute deterministic edits via `filmcraft_cli_bridge.py` or MCP `command_run`:
  ```python
  from filmcraft_cli_bridge import execute_native_command
  
  # Razor cut at specific second/timecode
  execute_native_command("timeline.razor", {"seconds": 12.5})
  
  # Trim edit points with handles
  execute_native_command("trim.edit", {"type": "ripple", "frames": -4})
  ```

### Phase 4: Acoustic Continuity & Dialogue Leveling
- Bridge all cuts with minimum 2-to-4 frame equal-power cosine crossfades at zero-crossing points.
- Fill dialogue gaps with synthesized room-tone prints.
- Calibrate integrated loudness to $-23.0\text{ LUFS}$ (EBU R128) or $-16.0\text{ LUFS}$ (Podcast) with True Peak ceiling $\le -1.0\text{ dBTP}$.

### Phase 5: Color Space & Optical Finishing
- Apply primary balance (Lift, Gamma, Gain, Offset) keeping skin tones locked on the $123^\circ$ I-line vectorscope.
- Check legal range code values: 10-bit Legal (64–940 CV) or Full Data (0–1023 CV).
- Render visual previews via `render_preview` or `render_frame`.

### Phase 6: Deterministic Validation & Sign-Off
- Run mapped Cluster 11 validator (`[566]`–`[592]`).
- Verify zero flash frames, zero timecode non-monotonicities, and 100% schema compliance.
- Emit final schema-locked manifest (Files A, B, C, D, or E).

---

## 3. Anti-Shallowness Iron Law

| Amateur / Shallow AI Advice (Strictly Banned) | Autonomous Senior Editor Execution (Mandatory) |
|---|---|
| "Cut out pauses to make it faster" | "Excise dead pauses exceeding 500ms; preserve 200–400ms natural breath pauses; bridge seams with 4-frame room-tone crossfades." |
| "Apply a cinematic color grade" | "Apply ACEScct CST; set Node 02 exposure gain +0.8 EV; place skin centroid at 123° vectorscope I-line with 32% saturation." |
| "Add background music" | "Duck underscore music by -5.0 dBFS whenever dialogue RMS exceeds -36 dBFS; filter music with dynamic EQ notch at 1.5–3.5 kHz." |

---

## 4. Bridge & Command Reference
- **CLI Bridge Module**: `python3 filmcraft_cli_bridge.py exec <command_id> '<params>'`
- **Full Command Directory**: [FILMCRAFT_COMMAND_ROUTING_BRIDGE.md](file:///Volumes/DISK%201/AGENTS%20TRAIN/EDITING_SYSTEM/skill-development/skills/autonomous-post-production-ai-monorepo/FILMCRAFT_COMMAND_ROUTING_BRIDGE.md)
- **39 Editing Templates**: [editing-templates/INDEX.md](file:///Volumes/DISK%201/AGENTS%20TRAIN/EDITING_SYSTEM/skill-development/editing-templates/INDEX.md)
