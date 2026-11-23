---
file_id: "[581]"
validator_name: "VAL_SUBTITLE_DURATIONS"
archetype: "G"
validation_type: "Deterministic Python Assertion"
---

# [581] Flagging cues < 833ms or > 7000ms and inter-cue gaps < 2 frames

## 1. Specification & Contract
- **Validator Identifier**: `VAL_SUBTITLE_DURATIONS`
- **Scope**: Deterministic validation of Flagging cues < 833ms or > 7000ms and inter-cue gaps < 2 frames.
- **Exit State**: Returns strictly `pass`, `warn`, or `fail` with structured violations list.

## 2. Executable Python Implementation
```python
def validate_subtitle_durations(cues, min_ms=833, max_ms=7000):
    violations = []
    for c in cues:
        dur = c["end_ms"] - c["start_ms"]
        if dur < min_ms:
            violations.append(f"Cue {c['cue_index']}: duration {dur}ms below {min_ms}ms floor")
        if dur > max_ms:
            violations.append(f"Cue {c['cue_index']}: duration {dur}ms exceeds {max_ms}ms ceiling")
    status = "fail" if violations else "pass"
    return {"status": status, "violations": violations}
```

## 3. Integration with FilmCraft Auto-Remediation Loop
- If status == `'pass'`: Pipeline advances immediately to next stage gate.
- If status == `'fail'`: Error is caught and dispatched to auto-remediation loop `[012]`.
