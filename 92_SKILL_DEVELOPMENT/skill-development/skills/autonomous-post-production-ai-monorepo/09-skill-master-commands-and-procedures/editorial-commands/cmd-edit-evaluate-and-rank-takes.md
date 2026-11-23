---
file_id: "[486]"
command_name: "CMD_EDIT_EVALUATE_AND_RANK_TAKES"
filmcraft_bridge_command: "sequence_inspect"
input_schema_lock: "[016]"
validation_gate: "[571]"
error_code: "ERR_NO_VALID_TAKE"
archetype: "E"
---

# [486] Command Spec: `EVALUATE_AND_RANK_TAKES`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_EDIT_EVALUATE_AND_RANK_TAKES`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `sequence_inspect`
- **Input Parameters**:
  - `scene_id, take_list`
- **Return Artifact**:
  - `ranked_takes_manifest` (conforming strictly to schema `[016]`)
- **Error Exceptions**:
  - `ERR_NO_VALID_TAKE` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_EDIT_EVALUATE_AND_RANK_TAKES`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[016]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "sequence_inspect",
  "parameters": {
    "inputs": "scene_id, take_list",
    "schema_target": "[016]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (scene_id, take_list).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (ranked_takes_manifest).
7. Invoke post-condition validator [571].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_NO_VALID_TAKE and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[571]` returns status `pass`.
- Zero violations detected in `ranked_takes_manifest`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_NO_VALID_TAKE` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[016]` | Re-serialize with strict validator | 1 retry failure |
