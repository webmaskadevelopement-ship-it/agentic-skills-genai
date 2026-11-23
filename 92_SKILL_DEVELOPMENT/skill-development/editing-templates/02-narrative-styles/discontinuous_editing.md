---
id: "discontinuous_editing"
name: "Discontinuous / Elliptical Editing"
category: "Narrative & Structural Editing Styles"
monorepo_links: ["[115]", "[116]", "[117]", "[532]", "[536]"]
filmcraft_commands: ["timeline.razor", "timeline.move", "timeline.selectGap", "edit.rippleDelete", "playhead.step"]
---

# Discontinuous / Elliptical Editing — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Narrative & Structural Editing Styles  
**Core Purpose**: Deliberate omission of time, space, or action to accelerate rhythm, inject stylistic energy, or emphasize psychological fragmentation.  

### Key Characteristics:
- **Ellipses**
- **Jump cuts**
- **Spatial displacement**
- **Fractured time**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Discontinuous / Elliptical Editing` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Temporal Compression via Jump Cuts**: Slicing out 1–3 second increments within a continuous take to compress a 30-second action into 6 kinetic seconds.
2. **Spatial Disorientation Traps**: Cutting between non-continuous locations while maintaining audio stream continuity.
3. **Rhythmic Staccato Pacing**: Generating rapid bursts of 6-frame to 12-frame cuts to simulate adrenaline, panic, or hyper-caffeinated energy.
4. **False Continuity Bridges**: Linking unrelated actions across disparate scenes using identical sound effects or visual gestures.
5. **Audience Active Inference Engagement**: Leaving narrative gaps that force the viewer's brain to bridge the missing story information.

---

## 3. Governing Physical Rules & Temporal Math
Elliptical Time Gap: $\Delta T_{omitted} = T_{action\_full} - T_{screen}$. Jump cut angle threshold: $\Delta \theta < 30^\circ$ with focal length delta $\Delta f < 10\text{mm}$.

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `timeline.razor`
- `timeline.move`
- `timeline.selectGap`
- `edit.rippleDelete`
- `playhead.step`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Discontinuous / Elliptical Editing
for cmd in ["timeline.razor", "timeline.move", "timeline.selectGap", "edit.rippleDelete", "playhead.step"]:
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
| "Add jump cuts everywhere" | "Apply jump cuts exclusively to repetitive mechanical actions (packing suitcase, walking up stairs); excise 1.5s per cut; maintain audio room tone." |
| "Skip time randomly" | "Excise 45 minutes of real time across cut: actor exits car in daylight, cut to actor opening apartment door in twilight with street lamp on." |
| "Make cuts snappy" | "Cut precisely on head turns and body pivots: cut 2 frames before head reaches turn apex, landing on next location 1 frame after turn." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "discontinuous_editing",
  "template_name": "Discontinuous / Elliptical Editing",
  "category": "Narrative & Structural Editing Styles",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.razor", "timeline.move", "timeline.selectGap", "edit.rippleDelete", "playhead.step"],
    "governing_monorepo_files": ["[115]", "[116]", "[117]", "[532]", "[536]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Discontinuous / Elliptical Editing workflow conforming to professional post-production standards."
}
```
