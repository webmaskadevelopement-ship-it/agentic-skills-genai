---
file_id: "[574]"
validator_name: "VAL_GRADE_LGG_BOUNDS"
archetype: "G"
validation_type: "Deterministic Python Assertion"
---

# [574] Verifying RGB lift/gamma/gain offsets stay within physically sane bounds

## 1. Specification & Contract
- **Validator Identifier**: `VAL_GRADE_LGG_BOUNDS`
- **Scope**: Deterministic validation of Verifying RGB lift/gamma/gain offsets stay within physically sane bounds.
- **Exit State**: Returns strictly `pass`, `warn`, or `fail` with structured violations list.

## 2. Executable Python Implementation
```python
def validate_lgg_bounds(adjustments):
    violations = []
    lift = adjustments.get("lift_rgb", [0, 0, 0])
    gain = adjustments.get("gain_rgb", [1, 1, 1])
    for ch, val in zip(["R", "G", "B"], lift):
        if val < -0.20 or val > 0.20:
            violations.append(f"Lift {ch} = {val} out of bounds [-0.20, +0.20]")
    for ch, val in zip(["R", "G", "B"], gain):
        if val < 0.50 or val > 2.00:
            violations.append(f"Gain {ch} = {val} out of bounds [0.50, 2.00]")
    status = "fail" if violations else "pass"
    return {"status": status, "violations": violations}
```

## 3. Integration with FilmCraft Auto-Remediation Loop
- If status == `'pass'`: Pipeline advances immediately to next stage gate.
- If status == `'fail'`: Error is caught and dispatched to auto-remediation loop `[012]`.
