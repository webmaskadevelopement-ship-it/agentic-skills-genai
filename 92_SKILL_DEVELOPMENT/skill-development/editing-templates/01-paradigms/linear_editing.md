---
id: "linear_editing"
name: "Linear Editing"
category: "Editing Paradigms & Workflow Modes"
monorepo_links: ["[001]", "[008]", "[017]", "[531]", "[537]"]
filmcraft_commands: ["timeline.place", "timeline.move", "markers.markIn", "markers.markOut", "export.presets.save"]
---

# Linear Editing — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Editing Paradigms & Workflow Modes  
**Core Purpose**: Sequential editing on videotape where shots must be assembled in order from beginning to end.  

### Key Characteristics:
- **Sequential assembly**
- **Tape-based workflow**
- **No random access**
- **Generation loss risk**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Linear Editing` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Reel Indexing & Head Prep**: Striping timecode onto master tape; pre-rolling 5 seconds of black and 2-pop reference bars.
2. **Sequential Source Logging**: Marking source IN and OUT points on playback VTR via frame-accurate timecode counter.
3. **Assemble vs. Insert Mode Selection**: Engaging Assemble edit (re-recording video, audio, and control track simultaneously) or Insert edit (preserving pre-recorded control track).
4. **Preroll Pre-Sync**: Synchronizing playback and record machines with 5-second preroll to lock servo capstan speed before cut head activates.
5. **Irreversible Record Head Committal**: Committing edit physically onto magnetic oxide tape at the active record in point.

---

## 3. Governing Physical Rules & Temporal Math
Cumulative Tape Duration: $T_{rec} = \sum_{i=1}^{n} (T_{out}(i) - T_{in}(i))$. Insertion into middle requires full reel re-assembly.

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `timeline.place`
- `timeline.move`
- `markers.markIn`
- `markers.markOut`
- `export.presets.save`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Linear Editing
for cmd in ["timeline.place", "timeline.move", "markers.markIn", "markers.markOut", "export.presets.save"]:
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
| "Put the clips in order" | "Execute strict chronological assemble pass ensuring continuous SMPTE LTC/VITC timecode with zero control-track dropouts." |
| "Fix a cut in the middle" | "Acknowledge linear physics: replacing a 4-second clip with a 5-second clip overwrites 1 second of downstream footage; execute insert edit or re-dub reel." |
| "Check video signal" | "Calibrate VTR output through vectorscope and waveform monitor: 0 IRE black setup, 100 IRE peak white, 40 IRE color burst." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "linear_editing",
  "template_name": "Linear Editing",
  "category": "Editing Paradigms & Workflow Modes",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.place", "timeline.move", "markers.markIn", "markers.markOut", "export.presets.save"],
    "governing_monorepo_files": ["[001]", "[008]", "[017]", "[531]", "[537]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Linear Editing workflow conforming to professional post-production standards."
}
```
