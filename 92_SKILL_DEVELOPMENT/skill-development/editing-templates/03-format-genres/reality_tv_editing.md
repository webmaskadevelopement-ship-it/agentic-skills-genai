---
id: "reality_tv_editing"
name: "Reality TV Editing"
category: "Format & Genre-Specific Editing"
monorepo_links: ["[031]", "[101]", "[115]", "[454]", "[533]"]
filmcraft_commands: ["multicam.switchAngle", "timeline.place", "timeline.razor", "essentialSound.set", "trim.edit"]
---

# Reality TV Editing — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Format & Genre-Specific Editing  
**Core Purpose**: Story producing from hundreds of hours of raw multi-camera footage, creating drama through confessionals, reaction cutaways, and sound futz.  

### Key Characteristics:
- **Story manufacturing from raw feeds**
- **Confessional / interview intercutting**
- **Reaction shot economy**
- **Dramatic stingers / rattle sounds**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Reality TV Editing` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Paper Story Mining**: Logging thousands of hours of verité feeds to isolate confrontation triggers and comedic character beats.
2. **Frankenbiting Dialogue Assembly**: Seamlessly splicing syllables and clauses from different sentences to construct clear, dramatic narrative declarations.
3. **Confessional 'Talking Head' Intercutting**: Cutting between dinner table argument and solo interview chair explaining internal motivations.
4. **Reaction Shot Juxtaposition**: Inserting eyebrow raises, eye rolls, and silent glares recorded hours earlier to heighten present scene tension.
5. **Reality Sound Accents**: Spotting metal screech stingers, reverse cymbal swells, and dramatic sub-bass drops on tense interpersonal eye contact.

---

## 3. Governing Physical Rules & Temporal Math
Reaction-to-Dialogue Ratio: For every 5 seconds of active dialogue, insert 2 seconds of silent suspicious or shocked reaction coverage from opposing cast members.

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `multicam.switchAngle`
- `timeline.place`
- `timeline.razor`
- `essentialSound.set`
- `trim.edit`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Reality TV Editing
for cmd in ["multicam.switchAngle", "timeline.place", "timeline.razor", "essentialSound.set", "trim.edit"]:
    print(f"Executing: {cmd}")
    # Execute through live loopback bridge or headless engine
    res = execute_native_command(cmd, {"deterministic_mode": True})
```

### CLI One-Liner (Shell):
```bash
filmcraft-cli --bridge 127.0.0.1:9876 exec multicam.switchAngle
```

---

## 5. Anti-Shallowness Iron Law: Shallow vs. Production-Grade Execution

| Typical Shallow / Amateur Execution (Banned) | Production-Grade Autonomous Execution (Mandatory) |
|---|---|
| "Let the argument play out naturally" | "Frankenbite conversational ramble into punchy conflict; cut to confessional explaining why the remark was offensive." |
| "Leave reaction shots in their original place" | "Mine B-roll selects for dramatic reactions (gasps, smirks) and insert them immediately following controversial statements." |
| "Keep audio untouched" | "Smooth dialogue splice points with room tone; apply high-pass futz to phone call audio; sweeten tension with reality rattle SFX." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "reality_tv_editing",
  "template_name": "Reality TV Editing",
  "category": "Format & Genre-Specific Editing",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["multicam.switchAngle", "timeline.place", "timeline.razor", "essentialSound.set", "trim.edit"],
    "governing_monorepo_files": ["[031]", "[101]", "[115]", "[454]", "[533]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Reality TV Editing workflow conforming to professional post-production standards."
}
```
