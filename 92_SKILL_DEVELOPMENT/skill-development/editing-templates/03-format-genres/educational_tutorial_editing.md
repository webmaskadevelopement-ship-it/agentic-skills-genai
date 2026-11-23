---
id: "educational_tutorial_editing"
name: "Educational / Tutorial Editing"
category: "Format & Genre-Specific Editing"
monorepo_links: ["[101]", "[335]", "[378]", "[454]", "[557]"]
filmcraft_commands: ["timeline.place", "graphics.newText", "masks.add", "essentialSound.set", "export.presets.save"]
---

# Educational / Tutorial Editing — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Format & Genre-Specific Editing  
**Core Purpose**: Instructional editing that sequences learning steps, highlights critical data, and maximizes cognitive retention and comprehension.  

### Key Characteristics:
- **Step-by-step numbering**
- **On-screen callouts & highlights**
- **Pause-and-explain pacing**
- **Recap summary chaptering**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Educational / Tutorial Editing` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Cognitive Step Sequencing**: Chunking lesson material into discrete pedagogical modules (Step 1, Step 2, Step 3) with title dividers.
2. **Callout & Spotlight Highlighting**: Darkening background by 40% and highlighting active software button, circuit component, or math formula.
3. **Pacing for Comprehension**: Pausing timeline video for 2 seconds after introducing complex diagrams to allow learner visual scanning.
4. **Picture-in-Picture (PiP) Layout**: Framing instructor in corner webcam circle while dedicating 85% raster to high-resolution tutorial workspace.
5. **Review & Summary Chaptering**: Assembling end-of-lesson recap bullet points; embedding interactive chapter marks into export file.

---

## 3. Governing Physical Rules & Temporal Math
Visual-Auditory Redundancy: On-screen key takeaway text must appear within 3 frames of instructor vocalizing concept. Hold duration $= 5\text{s}$ minimum.

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `timeline.place`
- `graphics.newText`
- `masks.add`
- `essentialSound.set`
- `export.presets.save`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Educational / Tutorial Editing
for cmd in ["timeline.place", "graphics.newText", "masks.add", "essentialSound.set", "export.presets.save"]:
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
| "Let instructor talk without visual aid" | "Generate on-screen summary card with exact bullet points synchronized with vocal enumeration." |
| "Show tiny unreadable screen text" | "Zoom screen capture 2.0x directly onto mouse cursor position during detailed software configuration." |
| "Rush through difficult concepts" | "Insert 1.5-second visual pause after complex formulas; add subtle audio ding to reinforce key takeaway." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "educational_tutorial_editing",
  "template_name": "Educational / Tutorial Editing",
  "category": "Format & Genre-Specific Editing",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.place", "graphics.newText", "masks.add", "essentialSound.set", "export.presets.save"],
    "governing_monorepo_files": ["[101]", "[335]", "[378]", "[454]", "[557]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Educational / Tutorial Editing workflow conforming to professional post-production standards."
}
```
