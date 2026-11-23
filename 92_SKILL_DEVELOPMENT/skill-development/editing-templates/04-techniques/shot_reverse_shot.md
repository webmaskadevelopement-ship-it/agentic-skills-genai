---
id: "shot_reverse_shot"
name: "Shot/Reverse Shot"
category: "Technique-Level Editing Methods"
monorepo_links: ["[101]", "[103]", "[115]", "[536]", "[541]"]
filmcraft_commands: ["timeline.place", "timeline.razor", "trim.edit", "playhead.step", "markers.markIn"]
---

# Shot/Reverse Shot — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Technique-Level Editing Methods  
**Core Purpose**: Alternating camera angles between two conversational partners, maintaining eyeline consistency, shoulder placement, and spatial geometry.  

### Key Characteristics:
- **Conversational coverage**
- **Eyeline consistency**
- **Over-the-shoulder framing**
- **Reaction shot timing**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Shot/Reverse Shot` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **A/B Coverage Verification**: Ensuring focal length (e.g. 50mm on both), distance, and depth-of-field are calibrated between OTS Character A and OTS Character B.
2. **180-Degree Axis Lock**: Confirming camera never crosses the eyeline axis connecting the two characters.
3. **Turn-Taking Cut Cadence**: Cutting to speaking character on sentence start; holding on listening character when dialogue involves accusation or confession.
4. **J/L-Cut Speech Overlaps**: Overlapping audio dialogue by 6–10 frames across cuts so speaker change occurs naturally.
5. **Focal Tightening on Climax**: Transitioning from wide Over-the-Shoulder framing to tight single close-ups as emotional conflict escalates.

---

## 3. Governing Physical Rules & Temporal Math
Eyeline Rule: Character A on left looks screen-right ($+15^\circ$ to $+25^\circ$ off lens); Character B on right looks screen-left ($-15^\circ$ to $-25^\circ$). Pupil height delta $\le 3\%$.

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `timeline.place`
- `timeline.razor`
- `trim.edit`
- `playhead.step`
- `markers.markIn`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Shot/Reverse Shot
for cmd in ["timeline.place", "timeline.razor", "trim.edit", "playhead.step", "markers.markIn"]:
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
| "Cut strictly ping-pong to whoever speaks" | "Hold on listener reaction during major emotional lines; let dialogue play off-screen (L-cut) for 18 frames." |
| "Mismatched eye level" | "Verify pupil screen coordinates: match character A pupil Y-height within 30 pixels of character B pupil Y-height." |
| "Cross the 180 axis" | "Enforce axis lock: character A must consistently occupy left third of screen and look right; character B occupies right third and looks left." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "shot_reverse_shot",
  "template_name": "Shot/Reverse Shot",
  "category": "Technique-Level Editing Methods",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.place", "timeline.razor", "trim.edit", "playhead.step", "markers.markIn"],
    "governing_monorepo_files": ["[101]", "[103]", "[115]", "[536]", "[541]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Shot/Reverse Shot workflow conforming to professional post-production standards."
}
```
