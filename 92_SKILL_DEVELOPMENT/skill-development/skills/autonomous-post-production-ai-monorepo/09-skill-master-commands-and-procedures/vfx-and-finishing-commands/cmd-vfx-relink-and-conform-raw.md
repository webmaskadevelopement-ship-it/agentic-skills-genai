---
file_id: "[523]"
command_name: "CMD_VFX_RELINK_AND_CONFORM_RAW"
filmcraft_bridge_command: "project.relink_raw"
input_schema_lock: "[027]"
validation_gate: "[589]"
error_code: "ERR_RAW_FILE_UNRESOLVED"
archetype: "E"
---

# [523] Command Spec: `RELINK_AND_CONFORM_RAW`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_VFX_RELINK_AND_CONFORM_RAW`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `project.relink_raw`
- **Input Parameters**:
  - `offline_edl, raw_dir`
- **Return Artifact**:
  - `conformed_raw_timeline` (conforming strictly to schema `[027]`)
- **Error Exceptions**:
  - `ERR_RAW_FILE_UNRESOLVED` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_VFX_RELINK_AND_CONFORM_RAW`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[027]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "project.relink_raw",
  "parameters": {
    "inputs": "offline_edl, raw_dir",
    "schema_target": "[027]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (offline_edl, raw_dir).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (conformed_raw_timeline).
7. Invoke post-condition validator [589].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_RAW_FILE_UNRESOLVED and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[589]` returns status `pass`.
- Zero violations detected in `conformed_raw_timeline`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_RAW_FILE_UNRESOLVED` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[027]` | Re-serialize with strict validator | 1 retry failure |
