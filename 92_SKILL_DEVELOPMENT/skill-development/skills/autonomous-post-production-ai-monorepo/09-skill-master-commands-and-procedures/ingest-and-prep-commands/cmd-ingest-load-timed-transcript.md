---
file_id: "[483]"
command_name: "CMD_INGEST_LOAD_TIMED_TRANSCRIPT"
filmcraft_bridge_command: "media.import_transcript"
input_schema_lock: "[015]"
validation_gate: "[570]"
error_code: "ERR_ALIGNMENT_DRIFT"
archetype: "E"
---

# [483] Command Spec: `LOAD_TIMED_TRANSCRIPT`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_INGEST_LOAD_TIMED_TRANSCRIPT`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `media.import_transcript`
- **Input Parameters**:
  - `transcript_file, media_id`
- **Return Artifact**:
  - `phoneme_alignment` (conforming strictly to schema `[015]`)
- **Error Exceptions**:
  - `ERR_ALIGNMENT_DRIFT` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_INGEST_LOAD_TIMED_TRANSCRIPT`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[015]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "media.import_transcript",
  "parameters": {
    "inputs": "transcript_file, media_id",
    "schema_target": "[015]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (transcript_file, media_id).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (phoneme_alignment).
7. Invoke post-condition validator [570].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_ALIGNMENT_DRIFT and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[570]` returns status `pass`.
- Zero violations detected in `phoneme_alignment`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_ALIGNMENT_DRIFT` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[015]` | Re-serialize with strict validator | 1 retry failure |
