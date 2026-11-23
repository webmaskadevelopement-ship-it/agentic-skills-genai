---
file_id: "[519]"
command_name: "CMD_SOUND_ALIGN_MUSIC_AND_DUCKING"
filmcraft_bridge_command: "audio.apply_ducking"
input_schema_lock: "[025]"
validation_gate: "[587]"
error_code: "ERR_DUCKING_PUMPING_DETECTED"
archetype: "E"
---

# [519] Command Spec: `ALIGN_MUSIC_AND_DUCKING`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_SOUND_ALIGN_MUSIC_AND_DUCKING`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `audio.apply_ducking`
- **Input Parameters**:
  - `dialogue_stem, music_stem, duck_db`
- **Return Artifact**:
  - `ducked_music_manifest` (conforming strictly to schema `[025]`)
- **Error Exceptions**:
  - `ERR_DUCKING_PUMPING_DETECTED` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_SOUND_ALIGN_MUSIC_AND_DUCKING`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[025]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "audio.apply_ducking",
  "parameters": {
    "inputs": "dialogue_stem, music_stem, duck_db",
    "schema_target": "[025]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (dialogue_stem, music_stem, duck_db).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (ducked_music_manifest).
7. Invoke post-condition validator [587].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_DUCKING_PUMPING_DETECTED and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[587]` returns status `pass`.
- Zero violations detected in `ducked_music_manifest`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_DUCKING_PUMPING_DETECTED` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[025]` | Re-serialize with strict validator | 1 retry failure |
