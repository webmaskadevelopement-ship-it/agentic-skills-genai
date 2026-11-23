---
file_id: "[604]"
adapter_name: "ADAPTER_AVID_SUBCAP"
archetype: "G"
bridge_type: "NLE/DAW Automation Bridge"
---

# [604] Generating Avid `.txt` SubCap timed blocks from Subtitle Engine

## 1. Adapter Purpose & Bridge Architecture
- **Adapter Identifier**: `ADAPTER_AVID_SUBCAP`
- **Description**: Avid SubCap Timed Text Generator.
- **Bridge Target**: Integrates the autonomous post-production monorepo with professional NLE/DAW finishing platforms.

## 2. Executable Automation Script / Recipe
```
def emit_avid_subcap(cues):
    lines = ["<begin subtitles>"]
    for c in cues:
        lines.append(f"{c['start_tc']}\t{c['end_tc']}\t{' '.join(c['lines'])}")
    lines.append("<end subtitles>")
    return "\n".join(lines)
```

## 3. FilmCraft Control Protocol Interoperability
- Maps directly to FilmCraft MCP bridge socket on port 9876.
- Preserves 254,016,000,000 ticks/sec timeline timebase across interchange formats.
