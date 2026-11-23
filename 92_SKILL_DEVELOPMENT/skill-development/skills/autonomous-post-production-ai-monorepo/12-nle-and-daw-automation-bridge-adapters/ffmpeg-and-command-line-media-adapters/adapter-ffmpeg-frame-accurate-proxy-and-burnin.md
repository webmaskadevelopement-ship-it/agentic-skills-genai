---
file_id: "[607]"
adapter_name: "ADAPTER_FFMPEG_PROXY_BURNIN"
archetype: "G"
bridge_type: "NLE/DAW Automation Bridge"
---

# [607] Generating `drawtext` timecode burn-in and LUT3D filtergraphs

## 1. Adapter Purpose & Bridge Architecture
- **Adapter Identifier**: `ADAPTER_FFMPEG_PROXY_BURNIN`
- **Description**: FFmpeg Frame-Accurate Proxy & TC Burn-In.
- **Bridge Target**: Integrates the autonomous post-production monorepo with professional NLE/DAW finishing platforms.

## 2. Executable Automation Script / Recipe
```
ffmpeg -y -i input.mov -vf "drawtext=timecode='01:00:00:00':rate=24:x=(w-tw)/2:y=h-(2*lh):fontcolor=white:box=1:boxcolor=black@0.6" -c:v prores_ks -profile:v 0 -c:a pcm_s24le proxy.mov
```

## 3. FilmCraft Control Protocol Interoperability
- Maps directly to FilmCraft MCP bridge socket on port 9876.
- Preserves 254,016,000,000 ticks/sec timeline timebase across interchange formats.
