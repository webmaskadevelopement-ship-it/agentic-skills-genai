---
file_id: "[480]"
command_name: "CMD_INGEST_VERIFY_MEDIA_HASHES"
filmcraft_bridge_command: "media.verify_hash"
input_schema_lock: "[014]"
validation_gate: "[567]"
error_code: "ERR_HASH_MISMATCH"
archetype: "E"
---

# [480] Command Spec: `VERIFY_MEDIA_HASHES`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_INGEST_VERIFY_MEDIA_HASHES`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `media.verify_hash`
- **Input Parameters**:
  - `media_path, algorithm`
- **Return Artifact**:
  - `hash_manifest` (conforming strictly to schema `[014]`)
- **Error Exceptions**:
  - `ERR_HASH_MISMATCH` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_INGEST_VERIFY_MEDIA_HASHES`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[014]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "media.verify_hash",
  "parameters": {
    "inputs": "media_path, algorithm",
    "schema_target": "[014]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (media_path, algorithm).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (hash_manifest).
7. Invoke post-condition validator [567].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_HASH_MISMATCH and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[567]` returns status `pass`.
- Zero violations detected in `hash_manifest`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_HASH_MISMATCH` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[014]` | Re-serialize with strict validator | 1 retry failure |
