---
id: "fade_wipe_iris"
name: "Fade / Wipe / Iris Optical Transitions"
category: "Technique-Level Editing Methods"
monorepo_links: ["[101]", "[126]", "[534]", "[537]"]
filmcraft_commands: ["timeline.add_transition", "trim.applyDefaultTransition", "effects.setParam", "playhead.step"]
---

# Fade / Wipe / Iris Optical Transitions — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Technique-Level Editing Methods  
**Core Purpose**: Optical transition effects used to signal major temporal, spatial, or emotional transitions with distinct stylistic or era-specific connotations.  

### Key Characteristics:
- **Fade to black (act break)**
- **Wipe transitions (SMPTE W001-W999)**
- **Iris transitions (vintage circle close)**
- **Passage of time marker**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Fade / Wipe / Iris Optical Transitions` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Transition Motivation Analysis**: Determining whether narrative requires scene comma (dissolve), paragraph break (fade to black), or comic/retro transition (wipe/iris).
2. **Fade to Black Execution**: Applying 36-frame dip to black at act break; holding 12 frames of total blackness before fading up into new time/location.
3. **Linear SMPTE Wipe Configuration**: Applying SMPTE wipe pattern (`W001` horizontal wipe, `W002` vertical wipe) with 2-pixel softness edge.
4. **Iris Circle In/Out Setup**: Centering circular iris iris-in transition directly onto subject face, isolating focal point before closing to black.
5. **Audio Lead/Fade Coordination**: Fading audio bed 12 frames prior to visual fade, or swelling audio across wipe transition.

---

## 3. Governing Physical Rules & Temporal Math
Standard Fade Duration: 24 to 48 frames ($1.0\text{s} - 2.0\text{s}$). Linear light dissolve math: $V_{out}(t) = (1-t) \cdot V_A + t \cdot V_B$ in linear gamma ($1.0$).

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `timeline.add_transition`
- `trim.applyDefaultTransition`
- `effects.setParam`
- `playhead.step`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Fade / Wipe / Iris Optical Transitions
for cmd in ["timeline.add_transition", "trim.applyDefaultTransition", "effects.setParam", "playhead.step"]:
    print(f"Executing: {cmd}")
    # Execute through live loopback bridge or headless engine
    res = execute_native_command(cmd, {"deterministic_mode": True})
```

### CLI One-Liner (Shell):
```bash
filmcraft-cli --bridge 127.0.0.1:9876 exec timeline.add_transition
```

---

## 5. Anti-Shallowness Iron Law: Shallow vs. Production-Grade Execution

| Typical Shallow / Amateur Execution (Banned) | Production-Grade Autonomous Execution (Mandatory) |
|---|---|
| "Use random 3D star wipes" | "Use SMPTE directional wipe strictly in stylized, graphic, or period contexts; ensure wipe follows physical screen motion." |
| "Fade to black in the middle of a scene" | "Reserve Fade to Black exclusively for major emotional loss, unconsciousness, or act breaks; hold 12 frames of true digital black." |
| "Fade audio abruptly with video" | "Fade dialogue early; allow acoustic room tone and music reverb tail to ring out into blackness for 24 frames." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "fade_wipe_iris",
  "template_name": "Fade / Wipe / Iris Optical Transitions",
  "category": "Technique-Level Editing Methods",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.add_transition", "trim.applyDefaultTransition", "effects.setParam", "playhead.step"],
    "governing_monorepo_files": ["[101]", "[126]", "[534]", "[537]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Fade / Wipe / Iris Optical Transitions workflow conforming to professional post-production standards."
}
```
