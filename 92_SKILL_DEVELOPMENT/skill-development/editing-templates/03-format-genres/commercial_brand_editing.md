---
id: "commercial_brand_editing"
name: "Commercial / Brand Video Editing"
category: "Format & Genre-Specific Editing"
monorepo_links: ["[028]", "[101]", "[126]", "[455]", "[535]"]
filmcraft_commands: ["timeline.place", "timeline.razor", "effects.apply", "scopes.read", "export.presets.save"]
---

# Commercial / Brand Video Editing — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Format & Genre-Specific Editing  
**Core Purpose**: High-impact, cinematic storytelling for advertisements and brand films operating under strict duration limits (15s, 30s, 60s) and messaging priorities.  

### Key Characteristics:
- **High-density visual storytelling**
- **Precise duration enforcement**
- **Emotional hook in first 3 seconds**
- **Hero product focus**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Commercial / Brand Video Editing` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Three-Second Hook Construction**: Placing visually arrestive, high-curiosity hero shot in frames 0 to 72 (first 3 seconds).
2. **Rhythmic Beat Matching**: Synchronizing visual cuts to bespoke commercial score, building tension towards 20-second product reveal.
3. **Hero Product Presentation**: Dedicating minimum 6 seconds (144 frames) to crisp, high-production beauty lighting shots of the product.
4. **Sound Design Impact Stems**: Layering sub-bass drops, riser sweeps, and pristine foley (can opening, engine purr) to elicit visceral response.
5. **Call-to-Action (CTA) End Card Locking**: Holding branded end card with legal disclaimer for exactly 72 frames (3.0 seconds) at conclusion.

---

## 3. Governing Physical Rules & Temporal Math
Hard Broadcast Slot Durations: 15s (360 frames @ 24fps), 30s (720 frames), 60s (1440 frames). First frame of action at 01:00:00:00; last frame at 01:00:29:23.

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `timeline.place`
- `timeline.razor`
- `effects.apply`
- `scopes.read`
- `export.presets.save`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Commercial / Brand Video Editing
for cmd in ["timeline.place", "timeline.razor", "effects.apply", "scopes.read", "export.presets.save"]:
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
| "Make a 30-second video that is 31 seconds" | "Enforce frame-exact 720-frame limit; trim 1 frame from each of 24 shots to eliminate 1-second overrun without harming story." |
| "Put product at the end only" | "Introduce visual brand signature within first 5 seconds; reinforce product utility at midpoint; lock hero logo on final 3-second card." |
| "Make it fast-paced" | "Modulate pace: 1.2s ASL in problem setup, slow to 3.0s beauty shot at product reveal, rapid 0.8s montage in feature recap." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "commercial_brand_editing",
  "template_name": "Commercial / Brand Video Editing",
  "category": "Format & Genre-Specific Editing",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.place", "timeline.razor", "effects.apply", "scopes.read", "export.presets.save"],
    "governing_monorepo_files": ["[028]", "[101]", "[126]", "[455]", "[535]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Commercial / Brand Video Editing workflow conforming to professional post-production standards."
}
```
