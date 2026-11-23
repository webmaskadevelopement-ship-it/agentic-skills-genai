---
file_id: "[495]"
command_name: "CMD_EDIT_VALIDATE_EDL_TIMECODE_MONOTONICITY"
filmcraft_bridge_command: "timeline.verify_tc"
input_schema_lock: "[017]"
validation_gate: "[566]"
error_code: "ERR_NON_MONOTONIC_TIMECODE"
archetype: "E"
---

# [495] Command Spec: `VALIDATE_EDL_TIMECODE_MONOTONICITY`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_EDIT_VALIDATE_EDL_TIMECODE_MONOTONICITY`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `timeline.verify_tc`
- **Input Parameters**:
  - `edl_manifest`
- **Return Artifact**:
  - `monotonicity_report` (conforming strictly to schema `[017]`)
- **Error Exceptions**:
  - `ERR_NON_MONOTONIC_TIMECODE` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_EDIT_VALIDATE_EDL_TIMECODE_MONOTONICITY`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[017]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "timeline.verify_tc",
  "parameters": {
    "inputs": "edl_manifest",
    "schema_target": "[017]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (edl_manifest).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (monotonicity_report).
7. Invoke post-condition validator [566].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_NON_MONOTONIC_TIMECODE and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[566]` returns status `pass`.
- Zero violations detected in `monotonicity_report`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_NON_MONOTONIC_TIMECODE` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[017]` | Re-serialize with strict validator | 1 retry failure |
