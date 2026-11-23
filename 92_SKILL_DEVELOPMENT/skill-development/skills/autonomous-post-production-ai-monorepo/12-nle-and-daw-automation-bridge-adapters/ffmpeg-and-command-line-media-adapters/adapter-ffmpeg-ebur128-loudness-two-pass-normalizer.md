---
file_id: "[608]"
adapter_name: "ADAPTER_FFMPEG_LOUDNORM"
archetype: "G"
bridge_type: "NLE/DAW Automation Bridge"
---

# [608] Running `ebur128` analysis pass + `loudnorm` linear/dynamic execution

## 1. Adapter Purpose & Bridge Architecture
- **Adapter Identifier**: `ADAPTER_FFMPEG_LOUDNORM`
- **Description**: FFmpeg EBU R128 Two-Pass Loudness Normalizer.
- **Bridge Target**: Integrates the autonomous post-production monorepo with professional NLE/DAW finishing platforms.

## 2. Executable Automation Script / Recipe
```
ffmpeg -i mix_input.wav -af loudnorm=I=-23.0:LRA=7.0:TP=-1.0:print_format=json -f null -
ffmpeg -i mix_input.wav -af loudnorm=I=-23.0:LRA=7.0:TP=-1.0:measured_I=-21.5:measured_TP=-0.4:linear=true normalized_mix.wav
```

## 3. FilmCraft Control Protocol Interoperability
- Maps directly to FilmCraft MCP bridge socket on port 9876.
- Preserves 254,016,000,000 ticks/sec timeline timebase across interchange formats.
