---
file_id: "[595]"
adapter_name: "ADAPTER_RESOLVE_TIMELINE_ASSEMBLY"
archetype: "G"
bridge_type: "NLE/DAW Automation Bridge"
---

# [595] Executing `AppendToTimeline` with frame-exact startFrame/endFrame

## 1. Adapter Purpose & Bridge Architecture
- **Adapter Identifier**: `ADAPTER_RESOLVE_TIMELINE_ASSEMBLY`
- **Description**: DaVinci Resolve Timeline Assembly from JSON EDL.
- **Bridge Target**: Integrates the autonomous post-production monorepo with professional NLE/DAW finishing platforms.

## 2. Executable Automation Script / Recipe
```
def assemble_timeline(resolve, edl_json):
    project = resolve.GetProjectManager().GetCurrentProject()
    media_pool = project.GetMediaPool()
    timeline = media_pool.CreateEmptyTimeline(edl_json["sequence_name"])
    # Append events frame-accurately
    for ev in edl_json["events"]:
        clip = media_pool.GetRootFolder().GetClipList()[0]
        media_pool.AppendToTimeline([{
            "mediaPoolItem": clip,
            "startFrame": ev["source_in_frames"],
            "endFrame": ev["source_out_frames"]
        }])
    return timeline
```

## 3. FilmCraft Control Protocol Interoperability
- Maps directly to FilmCraft MCP bridge socket on port 9876.
- Preserves 254,016,000,000 ticks/sec timeline timebase across interchange formats.
