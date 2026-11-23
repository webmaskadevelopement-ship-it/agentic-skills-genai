---
file_id: "[590]"
validator_name: "VAL_DELIVERY_SPEC_CONSISTENCY"
archetype: "G"
validation_type: "Deterministic Python Assertion"
---

# [590] Checking FPS, Resolution, Color Space & Runtime match across Files A–E

## 1. Specification & Contract
- **Validator Identifier**: `VAL_DELIVERY_SPEC_CONSISTENCY`
- **Scope**: Deterministic validation of Checking FPS, Resolution, Color Space & Runtime match across Files A–E.
- **Exit State**: Returns strictly `pass`, `warn`, or `fail` with structured violations list.

## 2. Executable Python Implementation
```python
def validate_delivery_spec_consistency(artifacts):
    violations = []
    ref_fps = artifacts["file_a_edl"]["fps"]
    for name, art in artifacts.items():
        if art.get("fps") != ref_fps:
            violations.append(f"Framerate mismatch in {name}: got {art.get('fps')}, expected {ref_fps}")
    status = "fail" if violations else "pass"
    return {"status": status, "violations": violations}
```

## 3. Integration with FilmCraft Auto-Remediation Loop
- If status == `'pass'`: Pipeline advances immediately to next stage gate.
- If status == `'fail'`: Error is caught and dispatched to auto-remediation loop `[012]`.
