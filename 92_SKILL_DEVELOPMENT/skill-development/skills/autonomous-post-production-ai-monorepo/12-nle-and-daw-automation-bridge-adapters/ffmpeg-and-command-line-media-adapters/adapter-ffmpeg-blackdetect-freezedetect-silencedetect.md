---
file_id: "[609]"
adapter_name: "ADAPTER_FFMPEG_QC_DETECTORS"
archetype: "G"
bridge_type: "NLE/DAW Automation Bridge"
---

# [609] Extracting machine-readable QC anomaly timestamps via libavfilter

## 1. Adapter Purpose & Bridge Architecture
- **Adapter Identifier**: `ADAPTER_FFMPEG_QC_DETECTORS`
- **Description**: FFmpeg blackdetect, freezedetect, silencedetect Analyzer.
- **Bridge Target**: Integrates the autonomous post-production monorepo with professional NLE/DAW finishing platforms.

## 2. Executable Automation Script / Recipe
```
ffmpeg -i master.mov -vf "blackdetect=d=0.1:pix_th=0.10,freezedetect=n=-60dB:d=2" -af "silencedetect=n=-60dB:d=1" -f null -
```

## 3. FilmCraft Control Protocol Interoperability
- Maps directly to FilmCraft MCP bridge socket on port 9876.
- Preserves 254,016,000,000 ticks/sec timeline timebase across interchange formats.
