---
id: "non_linear_editing"
name: "Non-Linear Editing (NLE)"
category: "Editing Paradigms & Workflow Modes"
monorepo_links: ["[001]", "[010]", "[017]", "[490]", "[538]", "[593]"]
filmcraft_commands: ["timeline.place", "timeline.razor", "timeline.move", "timeline.trim", "sequence.open", "edit.undo"]
---

# Non-Linear Editing (NLE) — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Editing Paradigms & Workflow Modes  
**Core Purpose**: Computer-based editing allowing random access to any frame without sequential restriction on a layered timeline.  

### Key Characteristics:
- **Random access**
- **Layered multi-track timeline**
- **Non-destructive pointer references**
- **Real-time effects**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Non-Linear Editing (NLE)` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Database Pointer Referencing**: Importing source media as metadata pointer references; source disk files remain untouched.
2. **Multi-Track Spatial Layering**: Stacking video tracks (V1 Primary Story, V2 Cutaways, V3 Graphics) and audio tracks (A1-A2 DX, A3-A4 FX, A5-A6 MX).
3. **Dynamic Ripple & Roll Trimming**: Adjusting cut points bidirectionally without moving or re-recording downstream assets.
4. **Real-Time Digital Signal Processing**: Calculating opacity blends, scale transforms, and audio pan laws in GPU memory buffers.
5. **Timeline State Versioning**: Serializing timeline state as an immutable Directed Acyclic Graph (DAG) with full undo/redo tree.

---

## 3. Governing Physical Rules & Temporal Math
Random Access Temporal Index: $Tick_{pos} = Frame \times 10,594,560,000$. Non-destructive pointer: $\text{Pointer} = (ClipID, SrcIn, SrcOut, RecIn, RecOut)$.

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `timeline.place`
- `timeline.razor`
- `timeline.move`
- `timeline.trim`
- `sequence.open`
- `edit.undo`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Non-Linear Editing (NLE)
for cmd in ["timeline.place", "timeline.razor", "timeline.move", "timeline.trim", "sequence.open", "edit.undo"]:
    print(f"Executing: {cmd}")
    # Execute through live loopback bridge or headless engine
    res = execute_native_command(cmd, {"deterministic_mode": True})
```

### CLI One-Liner (Shell):
```bash
filmcraft-cli --bridge 127.0.0.1:9876 exec timeline.place
```

---

## 5. Anti-Shallowness Iron Law: Shallow vs. Production-Grade Execution

| Typical Shallow / Amateur Execution (Banned) | Production-Grade Autonomous Execution (Mandatory) |
|---|---|
| "Move a clip on the timeline" | "Execute deterministic 3-point overwrite edit on V1, calculating source in/out and snapping to active playhead frame." |
| "Split a clip" | "Invoke `timeline.razor` at exact playhead tick, preserving clip gain automation and Lumetri color node tree on both split segments." |
| "Delete a gap" | "Execute `timeline.selectGap` and `edit.rippleDelete`, pulling all downstream synchronous audio/video events backward by gap frame count." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "non_linear_editing",
  "template_name": "Non-Linear Editing (NLE)",
  "category": "Editing Paradigms & Workflow Modes",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.place", "timeline.razor", "timeline.move", "timeline.trim", "sequence.open", "edit.undo"],
    "governing_monorepo_files": ["[001]", "[010]", "[017]", "[490]", "[538]", "[593]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Non-Linear Editing (NLE) workflow conforming to professional post-production standards."
}
```
