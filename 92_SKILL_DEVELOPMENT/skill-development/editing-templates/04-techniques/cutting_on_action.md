---
id: "cutting_on_action"
name: "Cutting on Action / Match on Action"
category: "Technique-Level Editing Methods"
monorepo_links: ["[101]", "[104]", "[115]", "[536]", "[571]"]
filmcraft_commands: ["timeline.razor", "trim.edit", "playhead.step", "markers.markIn", "markers.markOut"]
---

# Cutting on Action / Match on Action — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Technique-Level Editing Methods  
**Core Purpose**: Cutting from one shot to another during a physical action to mask the edit, maintaining kinetic momentum and visual continuity.  

### Key Characteristics:
- **Action continuity**
- **Invisible transition**
- **Perceptual momentum**
- **Vector alignment**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Cutting on Action / Match on Action` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Action Apex Identification**: Locating the peak velocity frame of a subject's physical gesture (fist punch, opening car door, sitting in chair).
2. **Outgoing Cut Placement**: Slicing the outgoing shot 30% to 50% into the physical movement, while action is in full kinetic flight.
3. **Incoming Cut Matching**: Finding the matching spatial position on the secondary camera angle; picking up action at identical 30% to 50% progression.
4. **Two-Frame Momentum Overlap**: Overlapping 1–2 frames of movement on incoming shot so the eye perceives unbroken physical flow without stutter.
5. **Screen Direction Consistency Verification**: Verifying the direction of action (left-to-right sweep) remains continuous across cut boundary.

---

## 3. Governing Physical Rules & Temporal Math
Perceptual Overlap Offset: Overlap physical motion by 1 to 2 frames across the cut to compensate for human saccadic visual readjustment delay ($150\text{ms}$).

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `timeline.razor`
- `trim.edit`
- `playhead.step`
- `markers.markIn`
- `markers.markOut`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Cutting on Action / Match on Action
for cmd in ["timeline.razor", "trim.edit", "playhead.step", "markers.markIn", "markers.markOut"]:
    print(f"Executing: {cmd}")
    # Execute through live loopback bridge or headless engine
    res = execute_native_command(cmd, {"deterministic_mode": True})
```

### CLI One-Liner (Shell):
```bash
filmcraft-cli --bridge 127.0.0.1:9876 exec timeline.razor
```

---

## 5. Anti-Shallowness Iron Law: Shallow vs. Production-Grade Execution

| Typical Shallow / Amateur Execution (Banned) | Production-Grade Autonomous Execution (Mandatory) |
|---|---|
| "Cut after the person finishes sitting down" | "Cut mid-descent when subject is halfway into chair; complete sitting action on incoming tight angle." |
| "Cut on identical exact frame" | "Overlap 2 frames of physical motion on incoming shot to satisfy retinal persistence and ensure fluid perceptual flow." |
| "Cut across opposing screen directions" | "Ensure momentum vector matches: if character punches screen-right, incoming close-up must travel screen-right." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "cutting_on_action",
  "template_name": "Cutting on Action / Match on Action",
  "category": "Technique-Level Editing Methods",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.razor", "trim.edit", "playhead.step", "markers.markIn", "markers.markOut"],
    "governing_monorepo_files": ["[101]", "[104]", "[115]", "[536]", "[571]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Cutting on Action / Match on Action workflow conforming to professional post-production standards."
}
```
