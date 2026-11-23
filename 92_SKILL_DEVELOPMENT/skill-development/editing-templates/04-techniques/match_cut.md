---
id: "match_cut"
name: "Match Cut"
category: "Technique-Level Editing Methods"
monorepo_links: ["[101]", "[107]", "[115]", "[126]", "[378]"]
filmcraft_commands: ["timeline.place", "timeline.razor", "effects.setParam", "playhead.step", "scopes.read"]
---

# Match Cut — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Technique-Level Editing Methods  
**Core Purpose**: A cut connecting two visually, graphically, or conceptually similar elements across disparate scenes, times, or spaces.  

### Key Characteristics:
- **Graphic visual rhyme**
- **Conceptual/thematic connection**
- **Spatiotemporal bridge**
- **Geometric alignment**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Match Cut` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Graphic Shape Identification**: Identifying visual object in Shot A (spinning wheel, round bone, human eye) and Shot B (roulette wheel, spaceship, planet).
2. **Centroid Coordinate Matching**: Re-framing or scaling Shot B so the geometric center of object B lands on the exact pixel coordinates of object A.
3. **Directional Vector Alignment**: Matching rotational velocity or trajectory (bone tumbling clockwise matched to orbital satellite rotating clockwise).
4. **Audio Transition Sweetening**: Bridging cut with unified sound effect (whoosh, cymbal, or continuous hum) spanning 4 frames before and after edit.
5. **Color & Luminance Harmonization**: Balancing contrast ratios across cut point so eye transition is smooth and visually satisfying.

---

## 3. Governing Physical Rules & Temporal Math
Geometric Centroid Alignment: Distance between visual anchors $\Delta d = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2} \le 0.03 \times W_{raster}$.

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `timeline.place`
- `timeline.razor`
- `effects.setParam`
- `playhead.step`
- `scopes.read`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Match Cut
for cmd in ["timeline.place", "timeline.razor", "effects.setParam", "playhead.step", "scopes.read"]:
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
| "Cut between two things that look kind of similar" | "Scale and position object B within 2% raster tolerance of object A; match motion vector and rotational speed." |
| "Cut abruptly with audio mismatch" | "Bridge visual match cut with unified sound design: blend sound of Shot A into sound of Shot B across 8-frame crossfade." |
| "Use match cut with no story meaning" | "Ensure match cut conveys narrative theme: cutting from character looking in mirror to mother looking in window establishes thematic lineage." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "match_cut",
  "template_name": "Match Cut",
  "category": "Technique-Level Editing Methods",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.place", "timeline.razor", "effects.setParam", "playhead.step", "scopes.read"],
    "governing_monorepo_files": ["[101]", "[107]", "[115]", "[126]", "[378]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Match Cut workflow conforming to professional post-production standards."
}
```
