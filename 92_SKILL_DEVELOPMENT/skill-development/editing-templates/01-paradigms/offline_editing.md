---
id: "offline_editing"
name: "Offline Editing"
category: "Editing Paradigms & Workflow Modes"
monorepo_links: ["[014]", "[016]", "[017]", "[033]", "[489]", "[562]"]
filmcraft_commands: ["media.colorInfo", "project.moveToBin", "timeline.place", "timeline.trim", "export.presets.list"]
---

# Offline Editing — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Editing Paradigms & Workflow Modes  
**Core Purpose**: Low-resolution proxy editing focused strictly on narrative structure, pacing, and emotional story arc prior to high-res conform.  

### Key Characteristics:
- **Proxy media workflow**
- **Story-first assembly**
- **Lightweight storage footprint**
- **EDL/XML metadata export**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Offline Editing` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Proxy Ingestion & Hash Verification**: Transcoding camera RAW files into lightweight 1080p ProRes 422 Proxy or DNxHR LB media while strictly maintaining original timecode and reel names.
2. **Paper Edit & Transcript Selects**: Transcribing dialogue with word-level timestamps and building narrative paper edit blueprint (`[016]`).
3. **Assembly Cut Compilation**: Assembling broad story structure without color grading, sound design, or visual effects polishing.
4. **Pacing & Emotional Refinement**: Iterating rough cut to fine cut, focusing on actor performances, rhythm, and structural clarity.
5. **Picture Lock & Conform Package Export**: Locking editorial timeline (`LOCKED_PICTURE`) and exporting CMX 3600 EDL (`[017]`), FCPXML, and reference offline MP4 with burnt-in timecode.

---

## 3. Governing Physical Rules & Temporal Math
Proxy Bitrate Ratio: $R_{proxy} = \frac{Bitrate_{ProResProxy}}{Bitrate_{RAW}} \approx \frac{45 \text{ Mbps}}{1326 \text{ Mbps}} = 0.0339$ (96.6% bandwidth saving).

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `media.colorInfo`
- `project.moveToBin`
- `timeline.place`
- `timeline.trim`
- `export.presets.list`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Offline Editing
for cmd in ["media.colorInfo", "project.moveToBin", "timeline.place", "timeline.trim", "export.presets.list"]:
    print(f"Executing: {cmd}")
    # Execute through live loopback bridge or headless engine
    res = execute_native_command(cmd, {"deterministic_mode": True})
```

### CLI One-Liner (Shell):
```bash
filmcraft-cli --bridge 127.0.0.1:9876 exec media.colorInfo
```

---

## 5. Anti-Shallowness Iron Law: Shallow vs. Production-Grade Execution

| Typical Shallow / Amateur Execution (Banned) | Production-Grade Autonomous Execution (Mandatory) |
|---|---|
| "Edit directly on 8K camera files" | "Transcode 8K REDCODE RAW to 1080p ProRes Proxy with matching audio channel maps; maintain 60 FPS playback on laptop storage." |
| "Color grade while cutting the story" | "Enforce strict offline isolation: use neutral Rec.709 viewing LUT; reject fine color tweaks until picture lock is signed off." |
| "Export cut for sound department" | "Export frame-locked EDL manifest citing tape reels, source in/out, and 2-frame sync pops at 00:59:58:00." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "offline_editing",
  "template_name": "Offline Editing",
  "category": "Editing Paradigms & Workflow Modes",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["media.colorInfo", "project.moveToBin", "timeline.place", "timeline.trim", "export.presets.list"],
    "governing_monorepo_files": ["[014]", "[016]", "[017]", "[033]", "[489]", "[562]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Offline Editing workflow conforming to professional post-production standards."
}
```
