---
file_id: "[032]"
skill_path: "01-ingest-dailies-and-assistant-editing/camera-offload-and-checksums/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Offload Verification & Cryptographic Integrity"
parent_router: "[031]"
child_nodes:
  - "[033]"
  - "[034]"
  - "[035]"
  - "[036]"
  - "[037]"
  - "[038]"
  - "[039]"
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

# [032] Sub-Router: Offload Verification & Cryptographic Integrity

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `01-ingest-dailies-and-assistant-editing/camera-offload-and-checksums`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(offload|xxhash64|verification)` | `[033]` | `offload-xxhash64-verification.md` | High-speed xxHash64 bit-for-bit camera card validation |
| `(?i)(offload|md5|sha256|dual|hash)` | `[034]` | `offload-md5-sha256-dual-hash.md` | Studio archival dual-hash generation and verification |
| `(?i)(asc|mhl|media|hash|list|generator)` | `[035]` | `asc-mhl-media-hash-list-generator.md` | ASC-MHL XML/MD chain-of-custody manifest generation |
| `(?i)(camera|folder|structure|preservation)` | `[036]` | `camera-folder-structure-preservation.md` | Maintaining native ARRI/RED/Sony directory trees |
| `(?i)(spanned|clip|reconstruction|logic)` | `[037]` | `spanned-clip-reconstruction-logic.md` | Stitching multi-chunk FAT32/exFAT spanned video files |
| `(?i)(corrupt|frame|and|dropped|packet|scanner)` | `[038]` | `corrupt-frame-and-dropped-packet-scanner.md` | Detecting truncated frames and buffer underruns on ingest |
| `(?i)(multi|destination|3|2|1|backup|auditor)` | `[039]` | `multi-destination-3-2-1-backup-auditor.md` | Validating primary RAID, nearline NAS, and LTO tape parity |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[032]`.
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

