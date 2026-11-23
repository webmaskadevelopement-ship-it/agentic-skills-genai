---
id: "social_media_editing"
name: "Social-First Editing"
category: "Format & Genre-Specific Editing"
monorepo_links: ["[335]", "[473]", "[557]", "[563]", "[632]"]
filmcraft_commands: ["sequence.open", "timeline.place", "timeline.razor", "captions.setStyle", "export.presets.save"]
---

# Social-First Editing — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Format & Genre-Specific Editing  
**Core Purpose**: Platform-native editing optimized for vertical formats (9:16), instant psychological hooks, kinetic auto-captions, and retention algorithms.  

### Key Characteristics:
- **9:16 Vertical aspect ratio**
- **0.5-second visual hook**
- **High-contrast dynamic captions**
- **Algorithm retention pacing**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Social-First Editing` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Vertical Frame Cropping & Pan-Scan**: Centering horizontal camera footage into 9:16 vertical canvas, animating horizontal position to follow subject action.
2. **Zero-Second Hook Formulation**: Placing most shocking visual or thesis statement in the first 12 frames (500ms); zero logo animations or introductory fluff.
3. **Kinetic Caption Generation**: Generating 1-to-3 word per-cue dynamic animated subtitles placed in screen center with bright yellow/green keyword highlights.
4. **Perpetual Kinetic Motion**: Applying micro-zooms (1.0x to 1.1x slow creep), whip transitions, and visual B-roll inserts every 2 seconds to retain eye attention.
5. **Seamless Loop Crafting**: Matching audio tone and visual position of the final frame to frame 1 to create an infinite, undetectable replay loop.

---

## 3. Governing Physical Rules & Temporal Math
Active Raster: $1080 \times 1920$ (9:16). Safe Margin: Title safe within horizontal $80\%$, vertical $20\% - 80\%$ (avoiding platform UI overlays). Cut frequency: $0.8\text{s} - 1.5\text{s}$ ASL.

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `sequence.open`
- `timeline.place`
- `timeline.razor`
- `captions.setStyle`
- `export.presets.save`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Social-First Editing
for cmd in ["sequence.open", "timeline.place", "timeline.razor", "captions.setStyle", "export.presets.save"]:
    print(f"Executing: {cmd}")
    # Execute through live loopback bridge or headless engine
    res = execute_native_command(cmd, {"deterministic_mode": True})
```

### CLI One-Liner (Shell):
```bash
filmcraft-cli --bridge 127.0.0.1:9876 exec sequence.open
```

---

## 5. Anti-Shallowness Iron Law: Shallow vs. Production-Grade Execution

| Typical Shallow / Amateur Execution (Banned) | Production-Grade Autonomous Execution (Mandatory) |
|---|---|
| "Crop video to 9:16 and leave it" | "Animate horizontal pan coordinate dynamically so moving subjects stay centered within 600px middle viewing column." |
| "Add standard bottom subtitles" | "Place 2-word kinetic captions in vertical center (Y: 960px); color keywords in #FFE600 yellow; keep text out of bottom TikTok UI icon zone." |
| "Start with 'Hey guys, welcome back'" | "Excise entire opening greeting; start cold on sentence climax: 'This mistake cost me $10,000...' with accompanying text card." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "social_media_editing",
  "template_name": "Social-First Editing",
  "category": "Format & Genre-Specific Editing",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["sequence.open", "timeline.place", "timeline.razor", "captions.setStyle", "export.presets.save"],
    "governing_monorepo_files": ["[335]", "[473]", "[557]", "[563]", "[632]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Social-First Editing workflow conforming to professional post-production standards."
}
```
