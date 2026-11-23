---
id: "classical_editing"
name: "Classical Editing"
category: "Narrative & Structural Editing Styles"
monorepo_links: ["[101]", "[102]", "[108]", "[535]", "[536]"]
filmcraft_commands: ["timeline.place", "timeline.trim", "playhead.set", "markers.markIn", "markers.markOut"]
---

# Classical Editing — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Narrative & Structural Editing Styles  
**Core Purpose**: Refined classical Hollywood grammar emphasizing dramatic emphasis, viewer guidance, and emotional punctuation within seamless continuity.  

### Key Characteristics:
- **Dramatic hierarchy**
- **Selective detail emphasis**
- **Purposeful shot scaling**
- **Subtle psychological pacing**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Classical Editing` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Hierarchical Coverage Progression**: Starting wide, stepping inward to medium shots as conflict brews, and saving extreme close-ups for emotional climax.
2. **Pacing Proportionality**: Allocating longer shot durations (5–8 seconds) during dramatic discovery, compressing to rapid exchanges (1.5–2.5 seconds) during confrontation.
3. **Gaze & Reaction Prioritization**: Holding on the listening character's face during critical dialogue revelations to capture psychological realization.
4. **Symmetrical Coverage Balancing**: Ensuring lens focal length, camera distance, and depth of field are matched between opposing over-the-shoulder angles.
5. **Resolution Cutaway Pull-Back**: Cutting back out to wider master shot as dramatic tension resolves, releasing viewer emotional pressure.

---

## 3. Governing Physical Rules & Temporal Math
Shot Scale Hierarchy: Master (LS) -> Two-Shot (MS) -> Over-the-Shoulder (MCU) -> Choker Close-Up (CU). Progression monotonically tightens as emotional stakes peak.

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `timeline.place`
- `timeline.trim`
- `playhead.set`
- `markers.markIn`
- `markers.markOut`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Classical Editing
for cmd in ["timeline.place", "timeline.trim", "playhead.set", "markers.markIn", "markers.markOut"]:
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
| "Cut to whoever is talking" | "Hold 18 frames on silent listener as emotional revelation lands; do not cut to speaker until dialogue hits second phrase." |
| "Use close-ups" | "Hold medium shots until moment of deception; cut to 85mm tight close-up exactly when character tells lie to reveal eye micro-expression." |
| "End the dialogue scene" | "Pull back to wide master 3 seconds before scene terminates, establishing character distance and loneliness before dissolving to black." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "classical_editing",
  "template_name": "Classical Editing",
  "category": "Narrative & Structural Editing Styles",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.place", "timeline.trim", "playhead.set", "markers.markIn", "markers.markOut"],
    "governing_monorepo_files": ["[101]", "[102]", "[108]", "[535]", "[536]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Classical Editing workflow conforming to professional post-production standards."
}
```
