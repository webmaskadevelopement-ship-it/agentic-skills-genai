---
id: "animation_editing"
name: "Animation Editing"
category: "Format & Genre-Specific Editing"
monorepo_links: ["[017]", "[101]", "[306]", "[454]", "[531]"]
filmcraft_commands: ["timeline.place", "timeline.razor", "clip.speedDuration", "audio.voiceover.sync", "export.presets.save"]
---

# Animation Editing — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Format & Genre-Specific Editing  
**Core Purpose**: Precision editing of animated assets (2D/3D/Anime) where timing, pose-to-pose holds, animatic pre-vis, and dialogue sync are frame-absolute.  

### Key Characteristics:
- **Frame-exact timing holds**
- **Pre-vis animatic assembly**
- **Scratch track lip-sync lock**
- **Sound-driven kinetic impact**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Animation Editing` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Storyboard & Animatic Assembly**: Cutting static storyboard panels to scratch audio track to establish scene timing before animation begins.
2. **Slug & Frame Hold Trimming**: Adjusting hold frames on key poses by 1-frame and 2-frame increments to perfect comedic or dramatic timing.
3. **Scratch to Final Audio Conform**: Relinking scratch dialogue to final studio voice recordings, adjusting animation timing to match vocal cadence.
4. **Action Impact Accentuation**: Inserting 1-frame white flash or screen shake on giant anime/3D impacts to enhance kinetic hit weight.
5. **Compositing Pass Conform**: Conforming background plates, character ink-and-paint layers, and lighting passes into final timeline master.

---

## 3. Governing Physical Rules & Temporal Math
Ones and Twos Timing: Animation on 1s (24 fps - fast action), Animation on 2s (12 unique drawings/sec held 2 frames each - dialogue/character).

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `timeline.place`
- `timeline.razor`
- `clip.speedDuration`
- `audio.voiceover.sync`
- `export.presets.save`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Animation Editing
for cmd in ["timeline.place", "timeline.razor", "clip.speedDuration", "audio.voiceover.sync", "export.presets.save"]:
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
| "Cut animation like live action" | "Respect animation frame holds: never cut on an intermediate tween drawing; cut on key anticipation pose or settled extreme." |
| "Add sound effects after final render" | "Build Foley and whoosh cues into the animatic stage; animators require exact audio transient timings to draw action." |
| "Ignore frame cadence" | "Verify 24.000 fps project cadence so 2s and 1s drawing holds remain uniform without 3:2 pull-down stutter." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "animation_editing",
  "template_name": "Animation Editing",
  "category": "Format & Genre-Specific Editing",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.place", "timeline.razor", "clip.speedDuration", "audio.voiceover.sync", "export.presets.save"],
    "governing_monorepo_files": ["[017]", "[101]", "[306]", "[454]", "[531]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Animation Editing workflow conforming to professional post-production standards."
}
```
