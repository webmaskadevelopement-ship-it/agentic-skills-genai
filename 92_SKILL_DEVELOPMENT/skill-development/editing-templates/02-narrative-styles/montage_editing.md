---
id: "montage_editing"
name: "Montage Editing"
category: "Narrative & Structural Editing Styles"
monorepo_links: ["[126]", "[127]", "[128]", "[534]", "[535]"]
filmcraft_commands: ["timeline.place", "timeline.razor", "trim.applyDefaultTransition", "sequence.open", "effects.apply"]
---

# Montage Editing — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Narrative & Structural Editing Styles  
**Core Purpose**: Juxtaposition of discontinuous shots to compress time, generate new conceptual meaning, or produce heightened emotional rhythm.  

### Key Characteristics:
- **Discontinuous cuts**
- **Symbolic juxtaposition**
- **Time compression**
- **Rhythmic/intellectual impact**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Montage Editing` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Conceptual Spine Architecture**: Defining montage thesis (Training Progression, Emotional Collapse, Passage of Decades).
2. **Rhythmic Quantization**: Quantizing visual cut points to musical quarter notes or 1/8th note transients in audio bed.
3. **Temporal Ellipsis Structuring**: Arranging shots non-sequentially, dropping chronological dead time between training milestones or narrative events.
4. **Graphic & Directional Contrast**: Alternating screen direction (left-to-right sweep followed by right-to-left punch) to heighten visual excitement.
5. **Dissolve & Optical Blending**: Layering 12–24 frame cross-dissolves, light leaks, or speed-ramped transitions between distinct temporal phases.

---

## 3. Governing Physical Rules & Temporal Math
ASL Exponential Decay Curve: $ASL(t) = ASL_0 \cdot e^{-\lambda t}$. Shot durations decrease from 72 frames (3.0s) down to 12 frames (0.5s).

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `timeline.place`
- `timeline.razor`
- `trim.applyDefaultTransition`
- `sequence.open`
- `effects.apply`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Montage Editing
for cmd in ["timeline.place", "timeline.razor", "trim.applyDefaultTransition", "sequence.open", "effects.apply"]:
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
| "Make a training montage" | "Structure 45-second sequence with 3 distinct musical acts: Act 1 struggle (ASL 2.8s), Act 2 breakthrough (ASL 1.6s), Act 3 peak mastery (ASL 0.75s)." |
| "Cut shots fast to music" | "Align cuts exactly 2 frames before musical snare transient (pre-beat anticipation) so visual perception lands simultaneously with auditory strike." |
| "Blend scenes together" | "Apply equal-power optical crossfades in 32-bit linear floating point space to prevent dirty dark luminance dip in mid-dissolve." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "montage_editing",
  "template_name": "Montage Editing",
  "category": "Narrative & Structural Editing Styles",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.place", "timeline.razor", "trim.applyDefaultTransition", "sequence.open", "effects.apply"],
    "governing_monorepo_files": ["[126]", "[127]", "[128]", "[534]", "[535]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Montage Editing workflow conforming to professional post-production standards."
}
```
