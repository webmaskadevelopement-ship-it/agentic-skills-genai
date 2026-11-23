---
id: "music_video_editing"
name: "Music Video Editing"
category: "Format & Genre-Specific Editing"
monorepo_links: ["[126]", "[177]", "[378]", "[454]", "[531]"]
filmcraft_commands: ["timeline.sync_tracks", "timeline.razor", "effects.apply", "sequence.open", "scopes.read"]
---

# Music Video Editing — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Format & Genre-Specific Editing  
**Core Purpose**: Rhythm-led, visually experimental editing where musical structure, lyrical themes, and performance sync dictate cut points and visual energy.  

### Key Characteristics:
- **Absolute beat synchronization**
- **Performance lip-sync lock**
- **Narrative + performance intercut**
- **Stylized color & optical effects**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Music Video Editing` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Multi-Take Lip-Sync Grouping**: Aligning all performance takes to master song audio track using waveform cross-correlation (`[482]`).
2. **Musical Structure Mapping**: Marking song sections: Intro (Bars 1–8), Verse 1 (Bars 9–24), Chorus 1 (Bars 25–40), Bridge, Guitar Solo, Outro.
3. **Performance to Narrative Intercut**: Laying locked lip-sync performance on V1; cutting to conceptual narrative storyline on V2 during instrumental breaks.
4. **Rhythmic Beat Quantization**: Cutting on snare hits, kick drums, or bass drops; utilizing syncopated 1-frame leading cuts for heightened kinetic drive.
5. **Speed Ramping & Stylized Optical Transitions**: Applying 200% to 50% speed ramps during camera moves; layering flash frames and film burns on chorus drops.

---

## 3. Governing Physical Rules & Temporal Math
BPM Frame Division: At 120 BPM and 24 fps: 1 Beat $= \frac{60 \times 24}{120} = 12$ frames. 1 Bar (4 beats) $= 48$ frames. Cut intervals quantized to $6, 12, 24,$ or $48$ frames.

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `timeline.sync_tracks`
- `timeline.razor`
- `effects.apply`
- `sequence.open`
- `scopes.read`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Music Video Editing
for cmd in ["timeline.sync_tracks", "timeline.razor", "effects.apply", "sequence.open", "scopes.read"]:
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
| "Cut on every drum beat" | "Vary cutting rhythm: cut every 4 bars during introspective verses; accelerate to quarter-note cuts on driving choruses." |
| "Show singer singing the whole song" | "Weave performance with conceptual B-roll: show singer on key emotional lyrics, cut away to symbolic visual on instrumental fills." |
| "Use generic transitions" | "Use camera whip pans and kinetic speed ramps that follow performer body motion across edit points." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "music_video_editing",
  "template_name": "Music Video Editing",
  "category": "Format & Genre-Specific Editing",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.sync_tracks", "timeline.razor", "effects.apply", "sequence.open", "scopes.read"],
    "governing_monorepo_files": ["[126]", "[177]", "[378]", "[454]", "[531]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Music Video Editing workflow conforming to professional post-production standards."
}
```
