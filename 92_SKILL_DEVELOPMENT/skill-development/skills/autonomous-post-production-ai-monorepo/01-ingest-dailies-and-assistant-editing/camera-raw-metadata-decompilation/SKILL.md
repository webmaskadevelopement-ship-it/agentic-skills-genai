---
file_id: "[040]"
skill_path: "01-ingest-dailies-and-assistant-editing/camera-raw-metadata-decompilation/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Native Camera Sensor & Lens Metadata Extraction"
parent_router: "[031]"
child_nodes:
  - "[041]"
  - "[042]"
  - "[043]"
  - "[044]"
  - "[045]"
  - "[046]"
  - "[047]"
  - "[048]"
  - "[049]"
  - "[050]"
schema_locks:
  - "[017]"
  - "[019]"
  - "[022]"
  - "[025]"
  - "[028]"
master_commands:
  - "EMIT_EDL_MANIFEST"
  - "EMIT_GRADE_SPEC"
  - "EMIT_COMPLIANCE_REPORT"
  - "EMIT_MIX_SPEC"
  - "EMIT_DELIVERY_SPEC"
validation_gates:
  - "[566]"
---

# [040] Sub-Router: Native Camera Sensor & Lens Metadata Extraction

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `01-ingest-dailies-and-assistant-editing/camera-raw-metadata-decompilation`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(arri|alexa|35|minilf|arriraw|mxf|parser)` | `[041]` | `arri-alexa-35-minilf-arriraw-mxf-parser.md` | Extracting Exposure Index, WB, Tint, ND & LDS-2 from ARRI |
| `(?i)(red|r3d|ipp2|metadata|decompiler)` | `[042]` | `red-r3d-ipp2-metadata-decompiler.md` | Extracting ISO, Kelvin, FLUT, Shadow, CDL & compression ratio |
| `(?i)(sony|venice|xocn|mxf|metadata|parser)` | `[043]` | `sony-venice-xocn-mxf-metadata-parser.md` | Extracting Dual Base ISO, User LUT, Anamorphic Desqueeze |
| `(?i)(blackmagic|braw|sidecar|and|header|parser)` | `[044]` | `blackmagic-braw-sidecar-and-header-parser.md` | Extracting Gen 5 Color Science, Constant Quality/Bitrate parameters |
| `(?i)(canon|cinema|raw|light|crm|parser)` | `[045]` | `canon-cinema-raw-light-crm-parser.md` | Extracting Canon Log 2/3, Gamut, Neutral Density & Dual Pixel AF |
| `(?i)(panasonic|varicam|vraw|vlog|parser)` | `[046]` | `panasonic-varicam-vraw-vlog-parser.md` | Extracting Native 800/5000 ISO & V-Gamut metadata flags |
| `(?i)(apple|prores|raw|atomos|header|parser)` | `[047]` | `apple-prores-raw-atomos-header-parser.md` | Extracting sensor-native WB and ISO conversion tags |
| `(?i)(cooke|i|technology|lens|metadata|extractor)` | `[048]` | `cooke-i-technology-lens-metadata-extractor.md` | Frame-by-frame focal length, T-stop, focus distance & hyperfocal |
| `(?i)(zeiss|extended|data|xd|shading|vignette|parser)` | `[049]` | `zeiss-extended-data-xd-shading-vignette-parser.md` | Extracting lens distortion and shading compensation profiles |
| `(?i)(anamorphic|squeeze|factor|normalization)` | `[050]` | `anamorphic-squeeze-factor-normalization.md` | Normalizing 1.3x, 1.5x, 1.8x, and 2.0x pixel aspect ratios |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[040]`.
2. Identify the target leaf file among child nodes and load exactly 1 to 3 relevant child files.
3. Load the corresponding Parameter Reference Table from Cluster 10 (`[530]`–`[565]`).
4. Load the target Schema Lock file from Cluster 00 (`[014]`–`[030]`).
5. Explicitly declare loaded file IDs at the top of the operational response.

## 4. Stage-Gate Precondition Contract

Before executing tasks routed by this gateway:
- Upstream stage gates specified in `[004] stage-gate-progression-protocol.md` must record verified status.
- Any input artifact must pass its mapped schema validation gate before mutation.
- Timeline modifications must compute frame offsets in integer frames or 254,016,000,000 FilmCraft ticks.

## 5. Evidence-Gated Output Contract

All output emitted under this router must comply with `[005] evidence-gated-reasoning-contract.md`:
- Cites exact empirical scope values, loudness meters, phoneme timestamps, or frame numbers.
- Banned phrases ('warm look', 'smooth cut', 'natural mix') result in immediate rejection.

## 6. Escalation & Edge-Case Fallback Table

| Failure Mode | Detection Signature | Escalation Target | Resolution |
|---|---|---|---|
| Parameter Out of Bounds | Validator gate status == 'fail' | `[012]` Auto-Remediation | Recalculate parameters |
| Subjective Aesthetic Ambiguity | Conflicting creative options | `[006]` Taste-Gate | Present 2–3 structured options |
| Upstream Incomplete Data | Missing input telemetry | `[684]` Studio Defaults | Assign deterministic standard |

