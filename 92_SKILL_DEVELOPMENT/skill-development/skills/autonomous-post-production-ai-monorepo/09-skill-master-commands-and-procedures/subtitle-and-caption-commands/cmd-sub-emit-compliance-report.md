---
file_id: "[514]"
command_name: "CMD_SUB_EMIT_COMPLIANCE_REPORT"
filmcraft_bridge_command: "subtitle.export_report"
input_schema_lock: "[022]"
validation_gate: "[580]"
error_code: "ERR_AUDIT_GENERATION_FAILED"
archetype: "E"
---

# [514] Command Spec: `EMIT_COMPLIANCE_REPORT`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_SUB_EMIT_COMPLIANCE_REPORT`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `subtitle.export_report`
- **Input Parameters**:
  - `cue_list, ruleset`
- **Return Artifact**:
  - `file_c_subtitle_compliance_report` (conforming strictly to schema `[022]`)
- **Error Exceptions**:
  - `ERR_AUDIT_GENERATION_FAILED` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_SUB_EMIT_COMPLIANCE_REPORT`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[022]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "subtitle.export_report",
  "parameters": {
    "inputs": "cue_list, ruleset",
    "schema_target": "[022]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (cue_list, ruleset).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (file_c_subtitle_compliance_report).
7. Invoke post-condition validator [580].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_AUDIT_GENERATION_FAILED and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[580]` returns status `pass`.
- Zero violations detected in `file_c_subtitle_compliance_report`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_AUDIT_GENERATION_FAILED` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[022]` | Re-serialize with strict validator | 1 retry failure |
