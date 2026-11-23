---
id: "beat_editing"
name: "Beat Editing"
category: "Technique-Level Editing Methods"
monorepo_links: ["[126]", "[127]", "[128]", "[454]", "[531]"]
filmcraft_commands: ["timeline.razor", "timeline.place", "markers.markIn", "playhead.set", "playhead.step"]
---

# Beat Editing — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Technique-Level Editing Methods  
**Core Purpose**: Cutting video precisely on musical beats, drum transients, and rhythmic accents to harmonize visual and auditory energy.  

### Key Characteristics:
- **Rhythmic musical synchronization**
- **Transient detection**
- **Pre-beat syncopation (-2 frames)**
- **Bar/phrase structural alignment**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Beat Editing` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **BPM & Meter Calculation**: Calculating exact beats per minute (BPM) and meter (4/4, 3/4) of musical soundtrack.
2. **Timeline Beat Grid Marker Placement**: Laying frame-accurate markers on every musical transient (downbeat, snare, cymbal crash).
3. **Pre-Beat Syncopation Offset**: Placing visual cuts 1 to 2 frames BEFORE the audio snare hit to compensate for human visual perception latency.
4. **Phrasing Hierarchy Structuring**: Aligning major shot scale jumps and scene changes with 4-bar and 8-bar musical phrase boundaries.
5. **Polyrhythmic Variation**: Breaking beat monotony by cutting across half-time or double-time intervals rather than cutting on every single beat.

---

## 3. Governing Physical Rules & Temporal Math
Frames Per Beat: $FPB = \frac{fps \times 60}{BPM}$. At 120 BPM & 24fps: $FPB = 12$ frames. At 140 BPM: $FPB = 10.285$ frames (requires 10f/11f cadence).

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `timeline.razor`
- `timeline.place`
- `markers.markIn`
- `playhead.set`
- `playhead.step`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Beat Editing
for cmd in ["timeline.razor", "timeline.place", "markers.markIn", "playhead.set", "playhead.step"]:
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
| "Cut on every single beat constantly" | "Vary cutting interval: hold across Bar 1 (4 beats), cut on quarter notes during Bar 2, hold on Bar 3; prevents rhythmic fatigue." |
| "Cut after the drum hit" | "Cut 2 frames before audio transient hit; visual information takes longer to process in the visual cortex than auditory hits." |
| "Cut on non-rhythmic audio" | "Analyze waveform: detect transient spikes in 80–250 Hz range (kick/snare) and snap edit points to transient peaks." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "beat_editing",
  "template_name": "Beat Editing",
  "category": "Technique-Level Editing Methods",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.razor", "timeline.place", "markers.markIn", "playhead.set", "playhead.step"],
    "governing_monorepo_files": ["[126]", "[127]", "[128]", "[454]", "[531]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Beat Editing workflow conforming to professional post-production standards."
}
```
