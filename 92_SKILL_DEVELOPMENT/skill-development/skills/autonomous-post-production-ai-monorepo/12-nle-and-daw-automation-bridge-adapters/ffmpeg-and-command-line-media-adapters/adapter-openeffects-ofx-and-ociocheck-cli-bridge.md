---
file_id: "[610]"
adapter_name: "ADAPTER_OCIO_CLI"
archetype: "G"
bridge_type: "NLE/DAW Automation Bridge"
---

# [610] Running OpenColorIO `ociocheck` and `ociobakelut` verification

## 1. Adapter Purpose & Bridge Architecture
- **Adapter Identifier**: `ADAPTER_OCIO_CLI`
- **Description**: OpenColorIO CLI & ociocheck Verification Bridge.
- **Bridge Target**: Integrates the autonomous post-production monorepo with professional NLE/DAW finishing platforms.

## 2. Executable Automation Script / Recipe
```
ociocheck --iconfig config.ocio
ociobakelut --iconfig config.ocio --inputspace "ACES - ACEScc" --outputspace "Output - Rec.709" --format text lut.cube
```

## 3. FilmCraft Control Protocol Interoperability
- Maps directly to FilmCraft MCP bridge socket on port 9876.
- Preserves 254,016,000,000 ticks/sec timeline timebase across interchange formats.
