---
file_id: "[599]"
adapter_name: "ADAPTER_PREMIERE_EXTENDSCRIPT"
archetype: "G"
bridge_type: "NLE/DAW Automation Bridge"
---

# [599] Building Premiere `qe.project` and `app.project.sequences` from EDL

## 1. Adapter Purpose & Bridge Architecture
- **Adapter Identifier**: `ADAPTER_PREMIERE_EXTENDSCRIPT`
- **Description**: Premiere Pro ExtendScript/UXP Sequence Builder.
- **Bridge Target**: Integrates the autonomous post-production monorepo with professional NLE/DAW finishing platforms.

## 2. Executable Automation Script / Recipe
```
// Premiere Pro ExtendScript Sequence Builder
var seq = app.project.createNewSequence("FILMCRAFT_EXPORT", "FCRFT_ID");
// Iterate events and insert clips

```

## 3. FilmCraft Control Protocol Interoperability
- Maps directly to FilmCraft MCP bridge socket on port 9876.
- Preserves 254,016,000,000 ticks/sec timeline timebase across interchange formats.
