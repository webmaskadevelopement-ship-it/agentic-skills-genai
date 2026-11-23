---
file_id: "[571]"
validator_name: "VAL_EDL_NO_DUPLICATE_FRAMES"
archetype: "G"
validation_type: "Deterministic Python Assertion"
---

# [571] Detecting accidental back-to-back match-frame jump cuts on same clip

## 1. Specification & Contract
- **Validator Identifier**: `VAL_EDL_NO_DUPLICATE_FRAMES`
- **Scope**: Deterministic validation of Detecting accidental back-to-back match-frame jump cuts on same clip.
- **Exit State**: Returns strictly `pass`, `warn`, or `fail` with structured violations list.

## 2. Executable Python Implementation
```python
def validate_no_duplicate_frames(events):
    violations = []
    for i in range(len(events) - 1):
        if events[i]["source_clip"] == events[i+1]["source_clip"]:
            if events[i]["source_out_frames"] == events[i+1]["source_in_frames"]:
                violations.append(f"Accidental match-frame splice detected between event {i} and {i+1}")
    status = "fail" if violations else "pass"
    return {"status": status, "violations": violations}
```

## 3. Integration with FilmCraft Auto-Remediation Loop
- If status == `'pass'`: Pipeline advances immediately to next stage gate.
- If status == `'fail'`: Error is caught and dispatched to auto-remediation loop `[012]`.
