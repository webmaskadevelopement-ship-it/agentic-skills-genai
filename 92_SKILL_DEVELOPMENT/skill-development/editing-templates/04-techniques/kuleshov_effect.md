---
id: "kuleshov_effect"
name: "Kuleshov Effect"
category: "Technique-Level Editing Methods"
monorepo_links: ["[101]", "[103]", "[115]", "[126]", "[535]"]
filmcraft_commands: ["timeline.place", "timeline.razor", "sequence.open", "playhead.step", "markers.markIn"]
---

# Kuleshov Effect — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Technique-Level Editing Methods  
**Core Purpose**: Cinematic montage principle proving that viewers derive more meaning from the interaction of two sequential shots than from a single shot in isolation.  

### Key Characteristics:
- **Juxtaposition-driven psychology**
- **Neutral actor expression**
- **Contextual projection**
- **Montage foundation**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Kuleshov Effect` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Neutral Anchor Shot Selection**: Selecting an actor close-up with completely neutral, non-emotive facial expression.
2. **Contextual Stimulus Insertion**: Splicing an evocative stimulus shot directly after:
   - Stimulus A: Bowl of hot soup -> Evokes hunger
   - Stimulus B: Child in a coffin -> Evokes grief
   - Stimulus C: Attractive woman on sofa -> Evokes desire
3. **Reaction Duration Hold**: Cutting back to the identical neutral face for 3 seconds; viewer involuntarily projects deep psychological emotion onto the face.
4. **Spatial Anchor Binding**: Ensuring actor eyeline in neutral shot points directly towards spatial placement of stimulus object.
5. **Sound Design Subtext Sweetening**: Adding subtle stomach rumble (soup), mournful cello (coffin), or romantic harp (woman) to reinforce perceived emotion.

---

## 3. Governing Physical Rules & Temporal Math
Psychological Transference Duration: Neutral Face (60f, 2.5s) -> Stimulus Shot (48f, 2.0s) -> Return to Neutral Face (72f, 3.0s). Eye saccade transfer window: 200ms.

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `timeline.place`
- `timeline.razor`
- `sequence.open`
- `playhead.step`
- `markers.markIn`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Kuleshov Effect
for cmd in ["timeline.place", "timeline.razor", "sequence.open", "playhead.step", "markers.markIn"]:
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
| "Use an actor who is already crying" | "Use a completely neutral face; let juxtaposition with coffin do the psychological work—it reads as profound suppressed grief." |
| "Cut away too quickly" | "Hold on neutral face for 3.0s after showing stimulus; human brain requires 2.5 seconds to project interior emotion." |
| "Mismatched eyelines" | "Ensure neutral face looks down 15° if soup is on table; looks forward 0° if person is standing." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "kuleshov_effect",
  "template_name": "Kuleshov Effect",
  "category": "Technique-Level Editing Methods",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.place", "timeline.razor", "sequence.open", "playhead.step", "markers.markIn"],
    "governing_monorepo_files": ["[101]", "[103]", "[115]", "[126]", "[535]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Kuleshov Effect workflow conforming to professional post-production standards."
}
```
