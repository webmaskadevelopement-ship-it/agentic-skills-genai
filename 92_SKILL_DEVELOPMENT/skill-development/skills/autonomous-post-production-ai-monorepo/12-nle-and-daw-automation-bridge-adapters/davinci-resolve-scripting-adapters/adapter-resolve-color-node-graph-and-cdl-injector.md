---
file_id: "[596]"
adapter_name: "ADAPTER_RESOLVE_COLOR_CDL"
archetype: "G"
bridge_type: "NLE/DAW Automation Bridge"
---

# [596] Applying CDL Slope/Offset/Power/Sat and DRX grades via Resolve API

## 1. Adapter Purpose & Bridge Architecture
- **Adapter Identifier**: `ADAPTER_RESOLVE_COLOR_CDL`
- **Description**: DaVinci Resolve Color Node Graph & CDL Injector.
- **Bridge Target**: Integrates the autonomous post-production monorepo with professional NLE/DAW finishing platforms.

## 2. Executable Automation Script / Recipe
```
def apply_cdl_to_current_clip(timeline, slope, offset, power, sat):
    current_clip = timeline.GetCurrentVideoItem()
    # Apply ASC-CDL via Resolve API
    current_clip.SetCDL({"Slope": slope, "Offset": offset, "Power": power, "Saturation": str(sat)})
```

## 3. FilmCraft Control Protocol Interoperability
- Maps directly to FilmCraft MCP bridge socket on port 9876.
- Preserves 254,016,000,000 ticks/sec timeline timebase across interchange formats.
