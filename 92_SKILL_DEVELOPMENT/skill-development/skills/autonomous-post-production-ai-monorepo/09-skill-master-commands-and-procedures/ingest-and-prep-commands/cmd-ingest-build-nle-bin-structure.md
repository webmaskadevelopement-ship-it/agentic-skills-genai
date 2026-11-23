---
file_id: "[485]"
command_name: "CMD_INGEST_BUILD_NLE_BIN_STRUCTURE"
filmcraft_bridge_command: "project.create_bin"
input_schema_lock: "[014]"
validation_gate: "[567]"
error_code: "ERR_BIN_CREATION_FAILED"
archetype: "E"
---

# [485] Command Spec: `BUILD_NLE_BIN_STRUCTURE`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_INGEST_BUILD_NLE_BIN_STRUCTURE`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `project.create_bin`
- **Input Parameters**:
  - `taxonomy_rule, project_id`
- **Return Artifact**:
  - `bin_hierarchy` (conforming strictly to schema `[014]`)
- **Error Exceptions**:
  - `ERR_BIN_CREATION_FAILED` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_INGEST_BUILD_NLE_BIN_STRUCTURE`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[014]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "project.create_bin",
  "parameters": {
    "inputs": "taxonomy_rule, project_id",
    "schema_target": "[014]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (taxonomy_rule, project_id).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (bin_hierarchy).
7. Invoke post-condition validator [567].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_BIN_CREATION_FAILED and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[567]` returns status `pass`.
- Zero violations detected in `bin_hierarchy`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_BIN_CREATION_FAILED` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[014]` | Re-serialize with strict validator | 1 retry failure |
