---
file_id: "[601]"
adapter_name: "ADAPTER_PREMIERE_MOGRT"
archetype: "G"
bridge_type: "NLE/DAW Automation Bridge"
---

# [601] Populating `.mogrt` lower-third text and timing parameters via script

## 1. Adapter Purpose & Bridge Architecture
- **Adapter Identifier**: `ADAPTER_PREMIERE_MOGRT`
- **Description**: Premiere Pro Essential Graphics MOGRT Injector.
- **Bridge Target**: Integrates the autonomous post-production monorepo with professional NLE/DAW finishing platforms.

## 2. Executable Automation Script / Recipe
```
// Inject MOGRT lower third with text and font bounds
var mogrt = app.project.activeSequence.importMGT(path, time, videoTrack, audioTrack);

```

## 3. FilmCraft Control Protocol Interoperability
- Maps directly to FilmCraft MCP bridge socket on port 9876.
- Preserves 254,016,000,000 ticks/sec timeline timebase across interchange formats.
