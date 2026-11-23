---
id: "experimental_editing"
name: "Experimental / Avant-Garde Editing"
category: "Narrative & Structural Editing Styles"
monorepo_links: ["[167]", "[168]", "[170]", "[444]", "[535]"]
filmcraft_commands: ["timeline.razor", "timeline.move", "effects.apply", "sequence.open", "scopes.read"]
---

# Experimental / Avant-Garde Editing — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Narrative & Structural Editing Styles  
**Core Purpose**: Non-traditional, discontinuous editing that challenges conventional perception, narrative structure, and temporal linearity.  

### Key Characteristics:
- **Discontinuity**
- **Abstract/associative logic**
- **Self-reflexive cuts**
- **Rhythmic strobe/flash frames**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Experimental / Avant-Garde Editing` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Deconstruction of Continuity**: Deliberately violating 180° line, jump-cutting identical angles, and ignoring spatial continuity.
2. **Associative / Metaphorical Cutting**: Cutting from character distress to abstract industrial machinery, microscopic cellular flow, or archival textures.
3. **Rhythmic Flash Frame Splicing**: Splicing 1-frame and 2-frame single-frame flashes of subliminal imagery into dialogue scenes.
4. **Asynchronous Audio De-Coupling**: Running ambient audio or dialogue from scene C over visual footage from scene A, forcing cognitive viewer synthesis.
5. **Materiality & Optical Degradation**: Injecting digital grain spikes, frame repeat stutters, and color phase inversions.

---

## 3. Governing Physical Rules & Temporal Math
Strobe Frequency Safety Bound: Flash frequency must NOT exceed 3 Hz for luminance excursions > 20 nits to guarantee ITU-R BT.1702 / Harding PSE safety compliance.

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `timeline.razor`
- `timeline.move`
- `effects.apply`
- `sequence.open`
- `scopes.read`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Experimental / Avant-Garde Editing
for cmd in ["timeline.razor", "timeline.move", "effects.apply", "sequence.open", "scopes.read"]:
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
| "Randomly cut weird stuff" | "Execute structured associative montage linking eye dilation to solar flare using graphic shape match at center raster coordinates (960, 540)." |
| "Add flash frames" | "Verify single-frame white flashes do not exceed Harding PSE flash limits; cap flash luma at 85 IRE and pace intervals > 350ms apart." |
| "Mismatched sound" | "De-couple audio track by +4.8 seconds; align character vocal sigh with visual shot of falling rain to establish psychological disassociation." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "experimental_editing",
  "template_name": "Experimental / Avant-Garde Editing",
  "category": "Narrative & Structural Editing Styles",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.razor", "timeline.move", "effects.apply", "sequence.open", "scopes.read"],
    "governing_monorepo_files": ["[167]", "[168]", "[170]", "[444]", "[535]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Experimental / Avant-Garde Editing workflow conforming to professional post-production standards."
}
```
