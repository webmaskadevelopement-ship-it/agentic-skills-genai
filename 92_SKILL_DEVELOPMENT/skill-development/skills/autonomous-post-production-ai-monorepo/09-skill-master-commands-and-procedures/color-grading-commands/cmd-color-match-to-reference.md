---
file_id: "[503]"
command_name: "CMD_COLOR_MATCH_TO_REFERENCE"
filmcraft_bridge_command: "effects.match_frames"
input_schema_lock: "[020]"
validation_gate: "[574]"
error_code: "ERR_MATCH_ERROR_THRESHOLD_EXCEEDED"
archetype: "E"
---

# [503] Command Spec: `MATCH_TO_REFERENCE`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_COLOR_MATCH_TO_REFERENCE`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `effects.match_frames`
- **Input Parameters**:
  - `source_clip, reference_clip`
- **Return Artifact**:
  - `shot_match_delta` (conforming strictly to schema `[020]`)
- **Error Exceptions**:
  - `ERR_MATCH_ERROR_THRESHOLD_EXCEEDED` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_COLOR_MATCH_TO_REFERENCE`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[020]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "effects.match_frames",
  "parameters": {
    "inputs": "source_clip, reference_clip",
    "schema_target": "[020]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (source_clip, reference_clip).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (shot_match_delta).
7. Invoke post-condition validator [574].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_MATCH_ERROR_THRESHOLD_EXCEEDED and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[574]` returns status `pass`.
- Zero violations detected in `shot_match_delta`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_MATCH_ERROR_THRESHOLD_EXCEEDED` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[020]` | Re-serialize with strict validator | 1 retry failure |
