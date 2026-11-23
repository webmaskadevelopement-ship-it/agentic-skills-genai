---
id: "jump_cut"
name: "Jump Cut"
category: "Technique-Level Editing Methods"
monorepo_links: ["[115]", "[116]", "[126]", "[536]", "[641]"]
filmcraft_commands: ["timeline.razor", "timeline.selectGap", "edit.rippleDelete", "playhead.step", "essentialSound.set"]
---

# Jump Cut — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Technique-Level Editing Methods  
**Core Purpose**: A discontinuous cut within the same shot or setup that violates the 30-degree rule, creating a deliberate temporal jump.  

### Key Characteristics:
- **Temporal ellipsis**
- **30-degree rule violation**
- **Pacing acceleration**
- **Stylistic self-awareness**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Jump Cut` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Continuous Take Selection**: Identifying single static or tracking take containing repetitive action or rambling monologue.
2. **Ellipsis Extraction Points**: Slicing timeline at pause points; deleting 0.5s to 3.0s chunks of dead time while keeping subject in same framing.
3. **Audio Crossfade Bridging**: Applying 2-frame equal-power crossfades at every jump cut boundary to eliminate audio clicks and pops.
4. **Cadence Rhythm Shaping**: Spacing jump cuts at structured rhythmic intervals (every 1.5 to 2.5 seconds) to create deliberate modern cadence.
5. **Scale Alternation (Optional)**: Punching in 110% on every second jump cut to create dynamic depth rhythm.

---

## 3. Governing Physical Rules & Temporal Math
Jump Cut Ellipsis Duration: Minimum temporal omission $\Delta t \ge 12$ frames ($500\text{ms}$) to prevent appearing as an accidental film splice glitch.

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `timeline.razor`
- `timeline.selectGap`
- `edit.rippleDelete`
- `playhead.step`
- `essentialSound.set`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Jump Cut
for cmd in ["timeline.razor", "timeline.selectGap", "edit.rippleDelete", "playhead.step", "essentialSound.set"]:
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
| "Leave 1-frame micro-gaps" | "Ensure cut omission is at least 12 frames; micro-jumps of 2–3 frames look like dropped video frames or corrupt encoding." |
| "Let audio pop at every cut" | "Insert 2-frame crossfade at zero-crossing points on audio track; keep room tone bed continuous on secondary track." |
| "Jump cut emotional crying scenes" | "Reserve jump cuts for comedy, vlogs, or temporal compression; avoid jump cuts in serious dramatic continuity scenes." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "jump_cut",
  "template_name": "Jump Cut",
  "category": "Technique-Level Editing Methods",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.razor", "timeline.selectGap", "edit.rippleDelete", "playhead.step", "essentialSound.set"],
    "governing_monorepo_files": ["[115]", "[116]", "[126]", "[536]", "[641]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Jump Cut workflow conforming to professional post-production standards."
}
```
