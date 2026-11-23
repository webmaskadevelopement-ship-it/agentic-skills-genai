---
id: "broadcast_news_editing"
name: "Broadcast News Editing"
category: "Format & Genre-Specific Editing"
monorepo_links: ["[011]", "[028]", "[101]", "[410]", "[553]"]
filmcraft_commands: ["timeline.place", "timeline.trim", "graphics.setText", "mixer.setValue", "export.presets.save"]
---

# Broadcast News Editing — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Format & Genre-Specific Editing  
**Core Purpose**: Ultra-fast turnaround editing for television news packages, soundbites, and live cut-ins under rigid broadcast timing and ethical standards.  

### Key Characteristics:
- **Reporter voiceover + soundbites**
- **B-roll wallpaper coverage**
- **Standardized lower thirds**
- **Frame-accurate slot duration**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Broadcast News Editing` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Voiceover Ingest & Scratch Alignment**: Laying reporter narration track on A1; verifying overall runtime conforms to exact broadcast block time.
2. **Key Soundbite Selection**: Spotting critical 8–12 second eyewitness or official soundbites and locking their timeline positions.
3. **B-Roll Wallpaper Assembly**: Laying relevant topical B-roll on V1 covering voiceover; never letting a shot hold longer than 3.5 seconds.
4. **Graphics & Lower-Third Insertion**: Inserting official news graphic bugs, locator lower-thirds ('WASHINGTON, D.C.'), and subject title cards.
5. **Broadcast Audio Calibration**: Setting reporter voiceover to -24.0 LUFS (ATSC A/85) or -23.0 LUFS (EBU R128); keeping natural sound bed (nat sound) at -12dB relative to voice.

---

## 3. Governing Physical Rules & Temporal Math
Standard Package Runtime: Exactly 01:30:00 (90 seconds = 2160 frames at 24fps / 2700 frames at 30fps). Soundbite duration: 8 to 14 seconds.

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
- `mixer.setValue`
- `export.presets.save`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Broadcast News Editing
for cmd in ["timeline.place", "timeline.trim", "graphics.setText", "mixer.setValue", "export.presets.save"]:
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
| "Make it look cinematic" | "Reject stylized film LUTs; enforce standard Rec.709 legal broadcast range (64–940 CV) with accurate daylight white balance." |
| "Let soundbites run long" | "Trim soundbite to core declarative sentence (10s max); cut out rambling lead-in; cover edit with reporter B-roll cutaway." |
| "Deliver whenever ready" | "Enforce hard time lock: package must time out to exactly 01:28:15 to allow 01:45 anchor wrap within 90-second commercial block." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "broadcast_news_editing",
  "template_name": "Broadcast News Editing",
  "category": "Format & Genre-Specific Editing",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.place", "timeline.trim", "graphics.setText", "mixer.setValue", "export.presets.save"],
    "governing_monorepo_files": ["[011]", "[028]", "[101]", "[410]", "[553]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Broadcast News Editing workflow conforming to professional post-production standards."
}
```
