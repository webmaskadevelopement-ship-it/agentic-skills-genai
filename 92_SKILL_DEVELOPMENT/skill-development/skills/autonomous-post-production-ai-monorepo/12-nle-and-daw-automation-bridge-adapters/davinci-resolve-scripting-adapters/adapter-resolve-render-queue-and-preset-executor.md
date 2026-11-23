---
file_id: "[597]"
adapter_name: "ADAPTER_RESOLVE_RENDER_QUEUE"
archetype: "G"
bridge_type: "NLE/DAW Automation Bridge"
---

# [597] Automating Deliver page render jobs, codecs, and filename tokens

## 1. Adapter Purpose & Bridge Architecture
- **Adapter Identifier**: `ADAPTER_RESOLVE_RENDER_QUEUE`
- **Description**: DaVinci Resolve Render Queue & Preset Executor.
- **Bridge Target**: Integrates the autonomous post-production monorepo with professional NLE/DAW finishing platforms.

## 2. Executable Automation Script / Recipe
```
def configure_render_job(project, target_dir, codec="ProRes422HQ"):
    project.SetRenderSettings({"TargetDir": target_dir, "CustomName": "MASTER_v01"})
    project.AddRenderJob()
    project.StartRendering()
```

## 3. FilmCraft Control Protocol Interoperability
- Maps directly to FilmCraft MCP bridge socket on port 9876.
- Preserves 254,016,000,000 ticks/sec timeline timebase across interchange formats.
