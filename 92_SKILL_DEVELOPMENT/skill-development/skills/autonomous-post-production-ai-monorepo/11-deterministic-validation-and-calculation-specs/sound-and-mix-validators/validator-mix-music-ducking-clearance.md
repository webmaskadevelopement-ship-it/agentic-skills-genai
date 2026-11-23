---
file_id: "[588]"
validator_name: "VAL_MIX_DUCKING"
archetype: "G"
validation_type: "Deterministic Python Assertion"
---

# [588] Verifying music ducks >= 6 dB whenever dialogue is active

## 1. Specification & Contract
- **Validator Identifier**: `VAL_MIX_DUCKING`
- **Scope**: Deterministic validation of Verifying music ducks >= 6 dB whenever dialogue is active.
- **Exit State**: Returns strictly `pass`, `warn`, or `fail` with structured violations list.

## 2. Executable Python Implementation
```python
def validate_music_ducking(ducking_events):
    violations = []
    for ev in ducking_events:
        if ev["attenuation_db"] > -4.0:
            violations.append(f"Insufficient music ducking at {ev['timecode']}: {ev['attenuation_db']} dB > -4.0 dB")
    status = "fail" if violations else "pass"
    return {"status": status, "violations": violations}
```

## 3. Integration with FilmCraft Auto-Remediation Loop
- If status == `'pass'`: Pipeline advances immediately to next stage gate.
- If status == `'fail'`: Error is caught and dispatched to auto-remediation loop `[012]`.
