---
file_id: "[524]"
command_name: "CMD_VFX_GENERATE_EXR_PULL_SHEET"
filmcraft_bridge_command: "timeline.export_vfx_pulls"
input_schema_lock: "[026]"
validation_gate: "[588]"
error_code: "ERR_HANDLE_FRAME_UNDERRUN"
archetype: "E"
---

# [524] Command Spec: `GENERATE_EXR_PULL_SHEET`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_VFX_GENERATE_EXR_PULL_SHEET`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `timeline.export_vfx_pulls`
- **Input Parameters**:
  - `vfx_shots, handle_frames`
- **Return Artifact**:
  - `vfx_pull_manifest` (conforming strictly to schema `[026]`)
- **Error Exceptions**:
  - `ERR_HANDLE_FRAME_UNDERRUN` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_VFX_GENERATE_EXR_PULL_SHEET`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[026]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "timeline.export_vfx_pulls",
  "parameters": {
    "inputs": "vfx_shots, handle_frames",
    "schema_target": "[026]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (vfx_shots, handle_frames).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (vfx_pull_manifest).
7. Invoke post-condition validator [588].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_HANDLE_FRAME_UNDERRUN and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[588]` returns status `pass`.
- Zero violations detected in `vfx_pull_manifest`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_HANDLE_FRAME_UNDERRUN` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[026]` | Re-serialize with strict validator | 1 retry failure |
