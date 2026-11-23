---
id: "documentary_editing"
name: "Documentary Editing"
category: "Format & Genre-Specific Editing"
monorepo_links: ["[016]", "[031]", "[101]", "[461]", "[489]", "[535]"]
filmcraft_commands: ["transcript.generate", "transcript.search", "timeline.place", "timeline.trim", "essentialSound.set", "export.presets.save"]
---

# Documentary Editing — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Format & Genre-Specific Editing  
**Core Purpose**: Story construction from non-fiction raw footage, interviews, verité scenes, and archival assets following an assembly-to-fine-cut arc.  

### Key Characteristics:
- **Interview-driven narrative spine**
- **B-roll contextual coverage**
- **Archival integration**
- **Paper edit blueprint**
- **Truth & ethics discipline**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Documentary Editing` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **ASR Transcription & Word Alignment**: Ingesting all interview rolls; generating timecoded transcripts (`[015]`) with speaker diarization.
2. **Paper Edit Blueprint Synthesis**: Compiling narrative story beats (`[016]`) solely from interview quotes; ranking A-roll dialogue blocks into 3-act narrative spine.
3. **Radio Play / Audio Spine Assembly**: Assembling dialogue-only timeline; excising filler words, stumbles, and excessive pauses; smoothing room tone with 4-frame crossfades.
4. **B-Roll & Verité Cutaway Layering**: Covering dialogue cuts with contextual B-roll on V2/V3; applying L-cuts where dialogue leads visual by 12–24 frames.
5. **Archival & Rostrum Camera Motion**: Framing historical stills with smooth Ken Burns moves (1.05x to 1.15x push-in); conforming mixed frame rates (24p, 25p, 29.97p) to project master.

---

## 3. Governing Physical Rules & Temporal Math
Documentary Shooting Ratio: Typically $40:1$ to $100:1$. Assembly cut duration $= 2.5 \times$ target runtime; Rough cut $= 1.4 \times$ target; Fine cut $= 1.0 \times$ target.

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `transcript.generate`
- `transcript.search`
- `timeline.place`
- `timeline.trim`
- `essentialSound.set`
- `export.presets.save`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Documentary Editing
for cmd in ["transcript.generate", "transcript.search", "timeline.place", "timeline.trim", "essentialSound.set", "export.presets.save"]:
    print(f"Executing: {cmd}")
    # Execute through live loopback bridge or headless engine
    res = execute_native_command(cmd, {"deterministic_mode": True})
```

### CLI One-Liner (Shell):
```bash
filmcraft-cli --bridge 127.0.0.1:9876 exec transcript.generate
```

---

## 5. Anti-Shallowness Iron Law: Shallow vs. Production-Grade Execution

| Typical Shallow / Amateur Execution (Banned) | Production-Grade Autonomous Execution (Mandatory) |
|---|---|
| "Cover every cut with random B-roll" | "Anchor B-roll contextually: when subject mentions 'the cold winter of 1978', cut to archival snowdrifts 14 frames prior to sentence conclusion." |
| "Remove all interview pauses" | "Preserve emotional breath pauses (350–500ms); only excise disfluency tokens ('um', 'uh', false starts) while bridging gap with room tone print." |
| "Pave music across the whole interview" | "Score music only during emotional pivots and act transitions; leave key testimonial revelations in stark, silent room tone." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "documentary_editing",
  "template_name": "Documentary Editing",
  "category": "Format & Genre-Specific Editing",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["transcript.generate", "transcript.search", "timeline.place", "timeline.trim", "essentialSound.set", "export.presets.save"],
    "governing_monorepo_files": ["[016]", "[031]", "[101]", "[461]", "[489]", "[535]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Documentary Editing workflow conforming to professional post-production standards."
}
```
