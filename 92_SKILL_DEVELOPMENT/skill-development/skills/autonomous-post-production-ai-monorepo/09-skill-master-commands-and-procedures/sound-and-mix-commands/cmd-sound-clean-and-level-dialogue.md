---
file_id: "[515]"
command_name: "CMD_SOUND_CLEAN_AND_LEVEL_DIALOGUE"
filmcraft_bridge_command: "audio.denoise_and_level"
input_schema_lock: "[023]"
validation_gate: "[585]"
error_code: "ERR_PHASE_DISTORTION"
archetype: "E"
---

# [515] Command Spec: `CLEAN_AND_LEVEL_DIALOGUE`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_SOUND_CLEAN_AND_LEVEL_DIALOGUE`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `audio.denoise_and_level`
- **Input Parameters**:
  - `dialogue_track, noise_profile`
- **Return Artifact**:
  - `leveled_dialogue_manifest` (conforming strictly to schema `[023]`)
- **Error Exceptions**:
  - `ERR_PHASE_DISTORTION` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_SOUND_CLEAN_AND_LEVEL_DIALOGUE`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[023]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "audio.denoise_and_level",
  "parameters": {
    "inputs": "dialogue_track, noise_profile",
    "schema_target": "[023]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (dialogue_track, noise_profile).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (leveled_dialogue_manifest).
7. Invoke post-condition validator [585].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_PHASE_DISTORTION and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[585]` returns status `pass`.
- Zero violations detected in `leveled_dialogue_manifest`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_PHASE_DISTORTION` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[023]` | Re-serialize with strict validator | 1 retry failure |
