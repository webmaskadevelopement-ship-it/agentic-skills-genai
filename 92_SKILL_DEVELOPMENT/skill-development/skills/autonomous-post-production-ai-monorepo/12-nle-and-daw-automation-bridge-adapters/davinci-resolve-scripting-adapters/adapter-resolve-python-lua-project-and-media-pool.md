---
file_id: "[594]"
adapter_name: "ADAPTER_RESOLVE_MEDIA_POOL"
archetype: "G"
bridge_type: "NLE/DAW Automation Bridge"
---

# [594] Driving `DaVinciResolveScript` MediaPool, Folder, and Timeline APIs

## 1. Adapter Purpose & Bridge Architecture
- **Adapter Identifier**: `ADAPTER_RESOLVE_MEDIA_POOL`
- **Description**: DaVinci Resolve Python/Lua Project & Media Pool Automator.
- **Bridge Target**: Integrates the autonomous post-production monorepo with professional NLE/DAW finishing platforms.

## 2. Executable Automation Script / Recipe
```
import DaVinciResolveScript as dvr
resolve = dvr.scriptapp("Resolve")
project_manager = resolve.GetProjectManager()
project = project_manager.GetCurrentProject()
media_pool = project.GetMediaPool()
root_folder = media_pool.GetRootFolder()
# Autonomous ingestion & folder setup
print(f"Connected to DaVinci Resolve project: {project.GetName()}")
```

## 3. FilmCraft Control Protocol Interoperability
- Maps directly to FilmCraft MCP bridge socket on port 9876.
- Preserves 254,016,000,000 ticks/sec timeline timebase across interchange formats.
