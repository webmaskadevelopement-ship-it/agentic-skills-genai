---
id: "online_editing"
name: "Online Editing / Finishing"
category: "Editing Paradigms & Workflow Modes"
monorepo_links: ["[027]", "[028]", "[029]", "[410]", "[523]", "[589]"]
filmcraft_commands: ["media.relink", "media.linkMedia", "effects.apply", "scopes.read", "export.presets.save", "render"]
---

# Online Editing / Finishing — Autonomous Post-Production Skill Template

## 1. Executive Summary & Aesthetic Theory
**Category**: Editing Paradigms & Workflow Modes  
**Core Purpose**: High-resolution conform, optical effects recreation, titling, color space mastering, and deliverable package finishing.  

### Key Characteristics:
- **Conform from EDL/XML**
- **High-res RAW media relink**
- **Color & VFX finishing integration**
- **QC compliance verification**

### Perceptual & Cognitive Rationale:
In world-class post-production, `Online Editing / Finishing` is not merely a mechanical cut or layout; it is a psychological contract with the human perceptual system. Human visual saccades, short-term auditory memory buffers, and emotional pattern recognition dictate exactly when, how, and why this editing approach succeeds.

---

## 2. What Exactly is Done (Step-by-Step Procedure)
1. **Conform & Media Relinking**: Ingesting offline EDL/XML, replacing 1080p proxy files with camera original RAW (ARRIRAW, REDCODE, BRAW) using reel name and timecode parity.
2. **Optical & Retime Verification**: Verifying speed ramps, optical flow interpolations, and scaling transforms against offline reference video.
3. **VFX & Title Plate Integration**: Dropping final 16-bit half-float ACEScg EXR visual effects comp plates and mastering title typography.
4. **Color Master Conform**: Linking color grading specifications (`[019]`) and applying final CST output transforms (e.g. ACEScct to Rec.709 or P3-D65).
5. **Quality Control & Master Package Export**: Running automated QC gates (`[591]`), inserting 2-pop leaders, and rendering ProRes 4444 XQ master, IMF, or DCP.

---

## 3. Governing Physical Rules & Temporal Math
Scaling Transformation: $S = \frac{Height_{master}}{Height_{offline}} = \frac{2160}{1080} = 2.0x$. Transform matrix computed via Lanczos-3 interpolation.

### Operational Boundaries & Thresholds:
- **Timebase Compliance**: Quantized strictly to FilmCraft master clock (`254,016,000,000 ticks/sec`).
- **Framerate Compatibility**: Validated across SMPTE standard timebases (23.976, 24.0, 25.0, 29.97, 59.94 fps).
- **Audio Crossfades**: Mandatory 2 to 4 frame equal-power crossfades at edit seams to eliminate digital zero-crossing clicks.

---

## 4. Native FilmCraft CLI & MCP Implementation Recipe

### Bound FilmCraft Commands:
- `media.relink`
- `media.linkMedia`
- `effects.apply`
- `scopes.read`
- `export.presets.save`
- `render`

### Execution Recipe (Python CLI Bridge):
```python
from filmcraft_cli_bridge import execute_native_command, route_skill_command

# Execute core operational commands for Online Editing / Finishing
for cmd in ["media.relink", "media.linkMedia", "effects.apply", "scopes.read", "export.presets.save", "render"]:
    print(f"Executing: {cmd}")
    # Execute through live loopback bridge or headless engine
    res = execute_native_command(cmd, {"deterministic_mode": True})
```

### CLI One-Liner (Shell):
```bash
filmcraft-cli --bridge 127.0.0.1:9876 exec media.relink
```

---

## 5. Anti-Shallowness Iron Law: Shallow vs. Production-Grade Execution

| Typical Shallow / Amateur Execution (Banned) | Production-Grade Autonomous Execution (Mandatory) |
|---|---|
| "Just export the timeline" | "Execute bit-for-bit conform audit: verify zero offline proxy clips remain, frame rates match 23.976 fps, and pixel aspect is 1.0 square." |
| "Put titles on top" | "Verify all on-screen titles sit strictly inside 80% title-safe area and text luminance conforms to 203 nit diffuse white limit in HDR." |
| "Check the render" | "Inspect output via automated QC report `[029]`: check for dropped frames, Harding PSE flash safety, and EBU R128 loudness compliance." |

---

## 6. Edge Cases & Auto-Remediation Protocols
- **Anomaly Detection**: If execution results in temporal discontinuity or audio phasing, route immediately to `[012] Error Taxonomy and Auto-Remediation Loop`.
- **Subjective Taste Ambiguity**: If multiple creative options share equal confidence scores, trigger human taste-gate via `[006] Human-in-the-Loop Escalation Matrix`.
- **Downstream Ripple**: Propagate all timeline modifications to Color (`[177]`), Sound (`[267]`), and Subtitles (`[335]`) using `[009] Cross-Department Ripple Propagation`.

---

## 7. Concrete Machine-Readable Output Artifact (JSON)
```json
{
  "template_id": "online_editing",
  "template_name": "Online Editing / Finishing",
  "category": "Editing Paradigms & Workflow Modes",
  "status": "PRODUCTION_VERIFIED",
  "execution_metrics": {
    "filmcraft_commands": ["media.relink", "media.linkMedia", "effects.apply", "scopes.read", "export.presets.save", "render"],
    "governing_monorepo_files": ["[027]", "[028]", "[029]", "[410]", "[523]", "[589]"],
    "deterministic_verification": true
  },
  "selection_rationale": "Executed deterministic Online Editing / Finishing workflow conforming to professional post-production standards."
}
```
