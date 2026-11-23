---
id: "wedding_event_editing"
name: "Wedding / Event Editing"
category: "Format & Genre-Specific Editing"
monorepo_links: ["[031]", "[101]", "[177]", "[267]", "[454]"]
filmcraft_commands: ["timeline.sync_tracks", "multicam.switchAngle", "lumetri.setLook", "mixer.setValue", "export.presets.save"]
---

# Wedding / Event Editing — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Format & Genre-Specific Editing  
**Core Purpose**: Emotion-driven cinematic narrative editing of milestone live events, combining romantic vows, speeches, and multi-camera ceremony coverage.  

### Key Characteristics:
- **Emotional highlight sequencing**
- **Speech audio voiceover bed**
- **Multi-cam ceremony sync**
- **Romantic slow-motion montage**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Wedding / Event Editing` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Ceremony Multi-Camera Sync**: Synchronizing 3+ camera angles with groom lavalier and officiant podium audio tracks.
2. **Vows Audio Bed Foundation**: Selecting heartfelt lines from private vows or father-of-the-bride toasts to serve as narrative voiceover spine.
3. **Montage Intercutting**: Weaving vows voiceover over slow-motion (60p to 24p) preparation footage, dress reveals, and guest emotional tears.
4. **Cinematic Golden Hour Grading**: Applying warm, creamy highlight roll-offs, soft halation around bride veil, and flattering skin tone grading.
5. **High-Energy Reception Climax**: Transitioning from romantic acoustic strings to upbeat dance floor celebration with kinetic beat-matched cuts.

---

## 3. Governing Physical Rules & Temporal Math
Ceremony Multi-Cam Sync Parity: $\Delta t = 0$ frames across Cam A (Wide), Cam B (Groom), Cam C (Bride), and master lavalier audio recorder.

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `timeline.sync_tracks`
- `multicam.switchAngle`
- `lumetri.setLook`
- `mixer.setValue`
- `export.presets.save`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Wedding / Event Editing
for cmd in ["timeline.sync_tracks", "multicam.switchAngle", "lumetri.setLook", "mixer.setValue", "export.presets.save"]:
    print(f"Executing: {cmd}")
    # Execute through live loopback bridge or headless engine
    res = execute_native_command(cmd, {"deterministic_mode": True})
```

### CLI One-Liner (Shell):
```bash
filmcraft-cli --bridge 127.0.0.1:9876 exec timeline.sync_tracks
```

---

## 5. Anti-Shallowness Iron Law: Shallow vs. Production-Grade Execution

| Typical Shallow / Amateur Execution (Banned) | Production-Grade Autonomous Execution (Mandatory) |
|---|---|
| "Play the entire 45-minute ceremony straight" | "Distill 45-minute ceremony into 5-minute cinematic film; interweave vows over couple photoshoot and reception." |
| "Leave bad camera shake in slow mo" | "Stabilize handheld camera footage with warp stabilizer; trim out focus hunting frames before couple eye contact settles." |
| "Use cheesy video transitions" | "Rely entirely on elegant straight cuts and occasional soft 12-frame dissolves; avoid heart wipes and spinning transitions." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "wedding_event_editing",
  "template_name": "Wedding / Event Editing",
  "category": "Format & Genre-Specific Editing",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.sync_tracks", "multicam.switchAngle", "lumetri.setLook", "mixer.setValue", "export.presets.save"],
    "governing_monorepo_files": ["[031]", "[101]", "[177]", "[267]", "[454]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Wedding / Event Editing workflow conforming to professional post-production standards."
}
```
