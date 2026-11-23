---
id: "sports_editing"
name: "Sports Editing"
category: "Format & Genre-Specific Editing"
monorepo_links: ["[101]", "[126]", "[306]", "[454]", "[535]"]
filmcraft_commands: ["clip.speedDuration", "timeline.place", "timeline.razor", "essentialSound.set", "export.presets.save"]
---

# Sports Editing — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Format & Genre-Specific Editing  
**Core Purpose**: Kinetic, action-emphasized editing highlighting athletic mastery, physical collision, speed transitions, and high-stakes emotional climaxes.  

### Key Characteristics:
- **Variable speed ramping**
- **Action direction continuity**
- **Multiple camera angle replays**
- **Crowd & stadium sound design**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Sports Editing` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Multi-Angle Action Ingestion**: Synchronizing live broadcast cameras (Main Game, High Endzone, Tight Hero, Super Slow-Mo 240fps).
2. **Kinetic Action Tracking**: Cutting on the ball release, strike, or tackle; maintaining directional vector (team attacking left-to-right).
3. **Speed Ramp Precision Crafting**: Running real-time motion during approach, decelerating to 240fps slow-motion at the exact millisecond of impact or catch.
4. **Hero Angle Replay Sequencing**: Cutting from broadcast wide angle to intimate reverse close-up showing athlete facial determination.
5. **Stadium Audio Sweetening**: Layering visceral bone-crunching Foley, sneaker squeaks, ball impacts, and soaring orchestral sports horns.

---

## 3. Governing Physical Rules & Temporal Math
Speed Ramp Curve: Real-time 100% (run up) -> Ramp down to 25% (slow-mo jump/impact over 18 frames) -> Snap to 300% (fast recovery over 8 frames).

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `clip.speedDuration`
- `timeline.place`
- `timeline.razor`
- `essentialSound.set`
- `export.presets.save`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Sports Editing
for cmd in ["clip.speedDuration", "timeline.place", "timeline.razor", "essentialSound.set", "export.presets.save"]:
    print(f"Executing: {cmd}")
    # Execute through live loopback bridge or headless engine
    res = execute_native_command(cmd, {"deterministic_mode": True})
```

### CLI One-Liner (Shell):
```bash
filmcraft-cli --bridge 127.0.0.1:9876 exec clip.speedDuration
```

---

## 5. Anti-Shallowness Iron Law: Shallow vs. Production-Grade Execution

| Typical Shallow / Amateur Execution (Banned) | Production-Grade Autonomous Execution (Mandatory) |
|---|---|
| "Put everything in slow motion" | "Reserve slow motion exclusively for peak athletic moments; maintain real-time speed for build-up to emphasize contrast in velocity." |
| "Switch angles randomly" | "Maintain spatial continuity: never cross 180° line during a play; ensure players always run toward the correct goal direction." |
| "Leave audio quiet" | "Pump stadium roar +6dB at moment of score; layer synthetic sub-drop on ball impact; duck commentary during dramatic replay montage." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "sports_editing",
  "template_name": "Sports Editing",
  "category": "Format & Genre-Specific Editing",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["clip.speedDuration", "timeline.place", "timeline.razor", "essentialSound.set", "export.presets.save"],
    "governing_monorepo_files": ["[101]", "[126]", "[306]", "[454]", "[535]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Sports Editing workflow conforming to professional post-production standards."
}
```
