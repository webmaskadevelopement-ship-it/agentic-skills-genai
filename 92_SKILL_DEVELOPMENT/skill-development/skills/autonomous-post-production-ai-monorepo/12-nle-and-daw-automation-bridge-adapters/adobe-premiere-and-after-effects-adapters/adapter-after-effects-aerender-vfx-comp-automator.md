---
file_id: "[602]"
adapter_name: "ADAPTER_AE_AERENDER"
archetype: "G"
bridge_type: "NLE/DAW Automation Bridge"
---

# [602] Driving headless `aerender` comps from VFX turnover pull sheets

## 1. Adapter Purpose & Bridge Architecture
- **Adapter Identifier**: `ADAPTER_AE_AERENDER`
- **Description**: After Effects aerender VFX Comp Automator.
- **Bridge Target**: Integrates the autonomous post-production monorepo with professional NLE/DAW finishing platforms.

## 2. Executable Automation Script / Recipe
```
aerender -project /Volumes/DISK\ 1/VFX/SHOT01.aep -comp "COMP_MAIN" -output /Volumes/DISK\ 1/EXR/SHOT01_[#####].exr -s 1 -e 120
```

## 3. FilmCraft Control Protocol Interoperability
- Maps directly to FilmCraft MCP bridge socket on port 9876.
- Preserves 254,016,000,000 ticks/sec timeline timebase across interchange formats.
