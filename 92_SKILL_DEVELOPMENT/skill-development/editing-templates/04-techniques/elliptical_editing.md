---
id: "elliptical_editing"
name: "Elliptical Editing"
category: "Technique-Level Editing Methods"
monorepo_links: ["[101]", "[115]", "[116]", "[126]", "[535]"]
filmcraft_commands: ["timeline.place", "timeline.razor", "trim.edit", "sequence.open", "markers.markIn"]
---

# Elliptical Editing — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Technique-Level Editing Methods  
**Core Purpose**: Deliberately omitting portions of an action, time period, or journey to accelerate narrative progression and invite viewer intellectual inference.  

### Key Characteristics:
- **Time omission**
- **Narrative acceleration**
- **Audience inference**
- **Action economy**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Elliptical Editing` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Dead Action Elimination**: Identifying routine mechanical actions (walking down hallway, driving to airport, waiting in line) and purging them.
2. **Boundary Anchor Definition**: Establishing clean departure anchor (Character locks front door) and arrival anchor (Character steps into Paris hotel room).
3. **Sound Bridge Continuity**: Using unified departing audio (airport announcement chime) to span across cut into the new geographical location.
4. **Lighting & Wardrobe Progression**: Signifying elapsed time through change in light (sun to night) or costume state (wet coat hanging up).
5. **Respecting Audience Cognitive Ability**: Trusting the audience to understand that time elapsed without requiring cheesy clocks or calendar pages.

---

## 3. Governing Physical Rules & Temporal Math
Elliptical Efficiency Ratio: $E = \frac{T_{real}}{T_{screen}} \ge 10:1$. E.g., a 2-hour flight depicted in 6 seconds (144 frames) across 2 shots.

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
- `sequence.open`
- `markers.markIn`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Elliptical Editing
for cmd in ["timeline.place", "timeline.razor", "trim.edit", "sequence.open", "markers.markIn"]:
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
| "Show every second of character walking to car" | "Cut from character picking up car keys in kitchen directly to car pulling up to the crime scene." |
| "Use a spinning clock or calendar" | "Indicate passage of time naturally: cut from full whiskey glass to empty glass with morning light on table." |
| "Cut out essential story beats" | "Omit only physical transit and routine mechanics; never omit character decision-making or emotional beats." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "elliptical_editing",
  "template_name": "Elliptical Editing",
  "category": "Technique-Level Editing Methods",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.place", "timeline.razor", "trim.edit", "sequence.open", "markers.markIn"],
    "governing_monorepo_files": ["[101]", "[115]", "[116]", "[126]", "[535]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Elliptical Editing workflow conforming to professional post-production standards."
}
```
