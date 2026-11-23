---
file_id: "[513]"
command_name: "CMD_SUB_GENERATE_FORMAT"
filmcraft_bridge_command: "subtitle.export_file"
input_schema_lock: "[021]"
validation_gate: "[579]"
error_code: "ERR_SERIALIZATION_FAILED"
archetype: "E"
---

# [513] Command Spec: `GENERATE_FORMAT`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_SUB_GENERATE_FORMAT`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `subtitle.export_file`
- **Input Parameters**:
  - `cue_list, format_type`
- **Return Artifact**:
  - `formatted_timed_text_file` (conforming strictly to schema `[021]`)
- **Error Exceptions**:
  - `ERR_SERIALIZATION_FAILED` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_SUB_GENERATE_FORMAT`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[021]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "subtitle.export_file",
  "parameters": {
    "inputs": "cue_list, format_type",
    "schema_target": "[021]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (cue_list, format_type).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (formatted_timed_text_file).
7. Invoke post-condition validator [579].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_SERIALIZATION_FAILED and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[579]` returns status `pass`.
- Zero violations detected in `formatted_timed_text_file`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_SERIALIZATION_FAILED` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[021]` | Re-serialize with strict validator | 1 retry failure |
