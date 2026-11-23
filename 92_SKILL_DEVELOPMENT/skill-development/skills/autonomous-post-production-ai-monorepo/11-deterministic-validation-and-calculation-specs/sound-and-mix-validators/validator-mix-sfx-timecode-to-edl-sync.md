---
file_id: "[589]"
validator_name: "VAL_MIX_SFX_SYNC"
archetype: "G"
validation_type: "Deterministic Python Assertion"
---

# [589] Cross-referencing Foley/SFX cue timecodes against EDL visual events

## 1. Specification & Contract
- **Validator Identifier**: `VAL_MIX_SFX_SYNC`
- **Scope**: Deterministic validation of Cross-referencing Foley/SFX cue timecodes against EDL visual events.
- **Exit State**: Returns strictly `pass`, `warn`, or `fail` with structured violations list.

## 2. Executable Python Implementation
```python
def validate_sfx_sync(sfx_cues, visual_hit_frames):
    violations = []
    for cue in sfx_cues:
        if cue["sync_frame"] not in visual_hit_frames:
            violations.append(f"SFX cue {cue['cue_id']} sync point {cue['sync_frame']} has no corresponding visual cut/action")
    status = "fail" if violations else "pass"
    return {"status": status, "violations": violations}
```

## 3. Integration with FilmCraft Auto-Remediation Loop
- If status == `'pass'`: Pipeline advances immediately to next stage gate.
- If status == `'fail'`: Error is caught and dispatched to auto-remediation loop `[012]`.
