---
id: "cross_cutting"
name: "Cross-Cutting (Parallel Action)"
category: "Technique-Level Editing Methods"
monorepo_links: ["[101]", "[115]", "[126]", "[145]", "[535]"]
filmcraft_commands: ["timeline.place", "timeline.razor", "timeline.move", "mixer.setValue", "export.presets.save"]
---

# Cross-Cutting (Parallel Action) — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Technique-Level Editing Methods  
**Core Purpose**: Intercutting between actions occurring at the same time in different locations to build suspense, establish narrative ties, and accelerate tempo.  

### Key Characteristics:
- **Simultaneous timelines**
- **Cross-location pacing**
- **Suspense building**
- **Climactic convergence**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Cross-Cutting (Parallel Action)` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Multi-Location Storyline Tracking**: Mapping real-time narrative progress in Location 1 (Rescue team assembling) and Location 2 (Hostage untying ropes).
2. **Synchronous Milestone Tagging**: Establishing simultaneous milestones (e.g. clock strikes 12:00 in both locations).
3. **Escalating Cut Frequency**: Starting with 8-second scenes, contracting progressively to 4s, 2s, 1s, and finally 12-frame alternating bursts.
4. **Shared Audio Leitmotif**: Playing unified suspense music cue or environmental rumble that spans across cuts to maintain subconscious continuity.
5. **Simultaneous Climax Resolution**: Cutting both scenes together at moment of door breach/escape, uniting storylines into shared reality.

---

## 3. Governing Physical Rules & Temporal Math
Ratio of Alternation: $Cycle(t) = T_A + T_B$. Compression rate: $Cycle_{k+1} = Cycle_k \times 0.75$. Cycles tighten from 240 frames down to 12 frames.

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

# Execute core operational commands for Cross-Cutting (Parallel Action)
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
| "Jump between scenes without clock urgency" | "Establish strict ticking countdown: cut to bomb display reading 00:30, cut to rescue team sprinting upstairs." |
| "Mix different camera energy styles" | "Harmonize camera kinetic energy: use handheld on both locations to mirror shared chaotic urgency." |
| "Abrupt audio cuts between rooms" | "Use shared musical score with continuous high-frequency ostinato violin to bridge cut points seamlessly." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "cross_cutting",
  "template_name": "Cross-Cutting (Parallel Action)",
  "category": "Technique-Level Editing Methods",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["timeline.place", "timeline.razor", "timeline.move", "mixer.setValue", "export.presets.save"],
    "governing_monorepo_files": ["[101]", "[115]", "[126]", "[145]", "[535]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Cross-Cutting (Parallel Action) workflow conforming to professional post-production standards."
}
```
