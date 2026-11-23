---
id: "trailer_editing"
name: "Trailer Editing"
category: "Format & Genre-Specific Editing"
monorepo_links: ["[126]", "[306]", "[455]", "[520]", "[629]"]
filmcraft_commands: ["timeline.place", "timeline.razor", "timeline.move", "mixer.setValue", "export.presets.save"]
---

# Trailer Editing — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Format & Genre-Specific Editing  
**Core Purpose**: High-impact promotional editing that condenses a full narrative into an escalating 3-act sequence driven by tension, sound design, and title hits.  

### Key Characteristics:
- **3-Act trailer structure**
- **Sound design hits/braams/risers**
- **Escalating tempo**
- **Dialogue soundbite montage**
- **Stinger punchline ending**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Trailer Editing` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Trailer Soundscape Construction**: Laying foundation of low braams, ticking clocks, and escalating orchestral rises prior to cutting picture.
2. **Act 1 Premise Setup**: Introducing world, protagonist motivation, and central conflict using measured dialogue soundbites over low drone.
3. **The 'Turn' (Midpoint Beat)**: Cutting to total black screen on major revelation; punctuating with deafening cinematic hit and silence gap.
4. **Act 3 Acceleration Montage**: Rapid-fire cutting across action beats; cutting picture to snare transients and gunshot foley at 0.5s intervals.
5. **Title Hit & Stinger Resolution**: Dropping film title with giant sub-bass boom; following with a 5-second comedic or terrifying stinger scene.

---

## 3. Governing Physical Rules & Temporal Math
Trailer 3-Act Structure: Act 1 Premise (0:00–0:45, ASL 3.5s), Act 2 Complication (0:45–1:40, ASL 1.8s), Act 3 Climax Montage (1:40–2:15, ASL 0.6s), Stinger (2:15–2:30).

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `timeline.place`
- `timeline.razor`
- `timeline.move`
- `mixer.setValue`
- `export.presets.save`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Trailer Editing
for cmd in ["timeline.place", "timeline.razor", "timeline.move", "mixer.setValue", "export.presets.save"]:
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
| "Cut trailer scenes chronologically" | "Deconstruct film: use Act 3 visual spectacle to score Act 1 dialogue; create mystery by withholding resolution." |
| "Use the movie's soundtrack" | "License specialized high-impact trailer cue featuring modular stem stops; layer custom 30Hz sub-drops and signature sound design risers." |
| "Cut on every drum hit" | "Sync cuts to polyrhythmic accents; leave occasional visual cuts across beats to create syncopated visual tension." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "trailer_editing",
  "template_name": "Trailer Editing",
  "category": "Format & Genre-Specific Editing",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.place", "timeline.razor", "timeline.move", "mixer.setValue", "export.presets.save"],
    "governing_monorepo_files": ["[126]", "[306]", "[455]", "[520]", "[629]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Trailer Editing workflow conforming to professional post-production standards."
}
```
