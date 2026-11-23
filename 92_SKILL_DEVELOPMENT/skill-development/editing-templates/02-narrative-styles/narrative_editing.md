---
id: "narrative_editing"
name: "Narrative Storytelling Editing"
category: "Narrative & Structural Editing Styles"
monorepo_links: ["[016]", "[101]", "[115]", "[126]", "[489]"]
filmcraft_commands: ["timeline.place", "timeline.trim", "sequence.open", "markers.markIn", "markers.markOut"]
---

# Narrative Storytelling Editing — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Narrative & Structural Editing Styles  
**Core Purpose**: Editing completely subservient to narrative arc, subtext, character evolution, and thematic pacing.  

### Key Characteristics:
- **Story-first pacing**
- **Character arc alignment**
- **Emotional cadence**
- **Subtext amplification**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Narrative Storytelling Editing` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Scene Narrative Goal Identification**: Defining the dramatic question of every scene before laying the first cut on the timeline.
2. **Pacing Modulation by Beat**: Expanding pauses when characters withhold truth; contracting pauses during high-stakes tactical negotiations.
3. **Subtextual Visual Planting**: Cutting to silent details (trembling hand, ticking clock, wedding ring) to convey unspoken interior stakes.
4. **Scene Transition Bridges**: Designing thematic sound bridges and match cuts that propel audience curiosity into subsequent scene.
5. **Overall Structural Arc Shaping**: Trimming redundant expository beats to ensure the sequence accelerates towards climax without narrative drag.

---

## 3. Governing Physical Rules & Temporal Math
Three-Act Proportionality: Act 1 (25% runtime), Act 2 (50% runtime), Act 3 (25% runtime). Inciting incident at 10-12% TRT; Midpoint at 50% TRT; Climax at 85-90% TRT.

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `timeline.place`
- `timeline.trim`
- `sequence.open`
- `markers.markIn`
- `markers.markOut`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Narrative Storytelling Editing
for cmd in ["timeline.place", "timeline.trim", "sequence.open", "markers.markIn", "markers.markOut"]:
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
| "Cut the script scenes in order" | "Re-sequence Scene 12 and 14: open on the aftermath to create suspense; reveal backstory via intercut dialogue flashback." |
| "Trim silence" | "Preserve 1200ms pregnant silence between question and answer to demonstrate character internal dilemma and emotional hesitation." |
| "Make it dramatic" | "Cut away from speaker at climax of sentence; linger on protagonist's face as the consequences of the words register." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "narrative_editing",
  "template_name": "Narrative Storytelling Editing",
  "category": "Narrative & Structural Editing Styles",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.place", "timeline.trim", "sequence.open", "markers.markIn", "markers.markOut"],
    "governing_monorepo_files": ["[016]", "[101]", "[115]", "[126]", "[489]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Narrative Storytelling Editing workflow conforming to professional post-production standards."
}
```
