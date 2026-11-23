---
file_id: "[579]"
validator_name: "VAL_SUBTITLE_SCHEMA"
archetype: "G"
validation_type: "Deterministic Python Assertion"
---

# [579] Verifying sequential numbering and non-overlapping monotonic cue times

## 1. Specification & Contract
- **Validator Identifier**: `VAL_SUBTITLE_SCHEMA`
- **Scope**: Deterministic validation of Verifying sequential numbering and non-overlapping monotonic cue times.
- **Exit State**: Returns strictly `pass`, `warn`, or `fail` with structured violations list.

## 2. Executable Python Implementation
```python
def validate_subtitle_schema(cues):
    violations = []
    for i in range(len(cues)):
        if cues[i]["cue_index"] != i + 1:
            violations.append(f"Cue index out of sequence at {i}: got {cues[i]['cue_index']}, expected {i+1}")
        if i < len(cues) - 1:
            if cues[i]["end_ms"] > cues[i+1]["start_ms"]:
                violations.append(f"Temporal overlap between cue {i+1} and {i+2}")
    status = "fail" if violations else "pass"
    return {"status": status, "violations": violations}
```

## 3. Integration with FilmCraft Auto-Remediation Loop
- If status == `'pass'`: Pipeline advances immediately to next stage gate.
- If status == `'fail'`: Error is caught and dispatched to auto-remediation loop `[012]`.
