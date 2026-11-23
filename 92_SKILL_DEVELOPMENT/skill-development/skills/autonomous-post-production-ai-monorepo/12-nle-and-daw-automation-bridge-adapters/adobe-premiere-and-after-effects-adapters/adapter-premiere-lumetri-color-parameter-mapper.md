---
file_id: "[600]"
adapter_name: "ADAPTER_PREMIERE_LUMETRI"
archetype: "G"
bridge_type: "NLE/DAW Automation Bridge"
---

# [600] Mapping Grade Spec JSON values to Lumetri Color intrinsic component

## 1. Adapter Purpose & Bridge Architecture
- **Adapter Identifier**: `ADAPTER_PREMIERE_LUMETRI`
- **Description**: Premiere Pro Lumetri Color Parameter Mapper.
- **Bridge Target**: Integrates the autonomous post-production monorepo with professional NLE/DAW finishing platforms.

## 2. Executable Automation Script / Recipe
```
// Map JSON Grade Spec to Premiere Lumetri Component
var trackItem = app.project.activeSequence.videoTracks[0].clips[0];
var lumetri = trackItem.components[1];

```

## 3. FilmCraft Control Protocol Interoperability
- Maps directly to FilmCraft MCP bridge socket on port 9876.
- Preserves 254,016,000,000 ticks/sec timeline timebase across interchange formats.
