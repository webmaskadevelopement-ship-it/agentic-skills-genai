---
id: "continuity_editing"
name: "Continuity Editing (Invisible Editing)"
category: "Narrative & Structural Editing Styles"
monorepo_links: ["[101]", "[103]", "[105]", "[536]", "[571]"]
filmcraft_commands: ["timeline.place", "timeline.razor", "trim.edit", "playhead.step", "markers.markIn"]
---

# Continuity Editing (Invisible Editing) — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Narrative & Structural Editing Styles  
**Core Purpose**: A style that hides the cut to maintain seamless spatial and temporal coherence, dominant in classical narrative cinema.  

### Key Characteristics:
- **Invisible cuts**
- **Narrative dominance**
- **Spatial consistency**
- **Shot/reverse shot**
- **180° rule compliance**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Continuity Editing (Invisible Editing)` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Establishing Spatial Geography**: Cutting from wide Master shot to establish spatial relationships of characters and key props.
2. **180-Degree Action Axis Enforcement**: Maintaining camera placement strictly on one side of the invisible line of action to preserve screen direction.
3. **Eyeline Vector Matching**: Aligning gaze trajectories across shot/reverse shot pairs so actor A looks camera-right and actor B looks camera-left.
4. **Cutting on Kinetic Action**: Splitting edit during actor's physical movement (opening door, standing up, drinking coffee) to conceal cut point.
5. **Smooth Audio Lead Integration**: Employing J/L split edits (4–8 frames audio lead) to mask visual cut transitions behind continuous dialogue speech.

---

## 3. Governing Physical Rules & Temporal Math
Eyeline Screen Parity: $|y_{eye\_A} - y_{eye\_B}| \le 0.05 \times H_{screen}$. 180° Action Axis: $\theta_{camera} \in [0^\circ, 180^\circ]$ on consistent vector $\vec{V}_{action}$.

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

# Execute core operational commands for Continuity Editing (Invisible Editing)
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
| "Cut between actors talking" | "Cut on listener reaction 6 frames prior to character B speaking; ensure character B's eyeline intersects character A's gaze vector at 15° off-lens axis." |
| "Switch angles on action" | "Cut on middle of physical gesture (e.g. glass lifted 40% from table); overlap 2 frames on incoming angle to ensure fluid perceptual momentum." |
| "Keep the scene smooth" | "Audit 180° line across coverage: flag any reversed eyelines and insert neutral head-on cutaway or reverse footage orientation." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "continuity_editing",
  "template_name": "Continuity Editing (Invisible Editing)",
  "category": "Narrative & Structural Editing Styles",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.place", "timeline.razor", "trim.edit", "playhead.step", "markers.markIn"],
    "governing_monorepo_files": ["[101]", "[103]", "[105]", "[536]", "[571]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Continuity Editing (Invisible Editing) workflow conforming to professional post-production standards."
}
```
