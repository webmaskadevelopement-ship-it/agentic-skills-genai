---
id: "corporate_industrial_editing"
name: "Corporate / Industrial Editing"
category: "Format & Genre-Specific Editing"
monorepo_links: ["[011]", "[028]", "[101]", "[335]", "[454]"]
filmcraft_commands: ["timeline.place", "timeline.trim", "graphics.setText", "lumetri.applyPreset", "export.presets.save"]
---

# Corporate / Industrial Editing — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Format & Genre-Specific Editing  
**Core Purpose**: Polished, clear, information-first editing for enterprise training, internal communications, B2B product marketing, and investor updates.  

### Key Characteristics:
- **Informational hierarchy**
- **Clean corporate branding**
- **Lower-third graphics**
- **Measured, professional pacing**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Corporate / Industrial Editing` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Executive Interview Cleanup**: Removing false starts, heavy breaths, and hesitation while preserving confident, authoritative cadence.
2. **Clean B-Roll Overlay**: Covering talking head with polished footage of modern office environments, customer handshakes, and product manufacturing.
3. **Brand-Compliant Graphics Packaging**: Injecting corporate brand font, approved hex color palettes, and standardized lower-third nameplates.
4. **Screen Recording & UI Framing**: Cropping software screencasts into clean laptop mockups; zooming in 1.4x on relevant mouse clicks.
5. **Neutral Professional Color & Audio**: Applying clean Rec.709 neutral color balance; keeping corporate acoustic bed sitting -26dB below dialogue.

---

## 3. Governing Physical Rules & Temporal Math
ASL: 3.5s to 5.0s. Lower Third On-Screen Duration: $Dur = \max(4.0\text{s}, 1.5\text{s} + 0.1\text{s} \times \text{chars})$. Audio LUFS: -24.0 LUFS.

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `timeline.place`
- `timeline.trim`
- `graphics.setText`
- `lumetri.applyPreset`
- `export.presets.save`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Corporate / Industrial Editing
for cmd in ["timeline.place", "timeline.trim", "graphics.setText", "lumetri.applyPreset", "export.presets.save"]:
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
| "Use flashy TikTok zooms" | "Enforce measured corporate dignity: gentle 1.05x push-in on key strategic vision statements; no disorienting crash zooms." |
| "Leave awkward executive pauses" | "Trim pauses to crisp 400ms cadence; edit around stumbles using B-roll cutaway overlays." |
| "Use random fonts" | "Bind typography strictly to brand guidelines: Inter or Roboto, title case, exact corporate primary blue accent lines." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "corporate_industrial_editing",
  "template_name": "Corporate / Industrial Editing",
  "category": "Format & Genre-Specific Editing",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.place", "timeline.trim", "graphics.setText", "lumetri.applyPreset", "export.presets.save"],
    "governing_monorepo_files": ["[011]", "[028]", "[101]", "[335]", "[454]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Corporate / Industrial Editing workflow conforming to professional post-production standards."
}
```
