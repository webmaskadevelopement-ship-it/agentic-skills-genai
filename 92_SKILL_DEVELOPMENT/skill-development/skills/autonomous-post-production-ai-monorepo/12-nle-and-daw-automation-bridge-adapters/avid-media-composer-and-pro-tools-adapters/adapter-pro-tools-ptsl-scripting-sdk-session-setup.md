---
file_id: "[605]"
adapter_name: "ADAPTER_PRO_TOOLS_PTSL"
archetype: "G"
bridge_type: "NLE/DAW Automation Bridge"
---

# [605] Automating Pro Tools track creation, AAF import, and stem bounce via PTSL

## 1. Adapter Purpose & Bridge Architecture
- **Adapter Identifier**: `ADAPTER_PRO_TOOLS_PTSL`
- **Description**: Pro Tools Scripting SDK (PTSL) Bridge.
- **Bridge Target**: Integrates the autonomous post-production monorepo with professional NLE/DAW finishing platforms.

## 2. Executable Automation Script / Recipe
```
import grpc
# Connect to Pro Tools PTSL IPC Socket
# Execute ImportAAF, CreateTracks, BounceStems

```

## 3. FilmCraft Control Protocol Interoperability
- Maps directly to FilmCraft MCP bridge socket on port 9876.
- Preserves 254,016,000,000 ticks/sec timeline timebase across interchange formats.
