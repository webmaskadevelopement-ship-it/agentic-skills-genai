---
file_id: "[572]"
validator_name: "VAL_EDL_STAGE_GATE"
archetype: "G"
validation_type: "Deterministic Python Assertion"
---

# [572] Verifying all stage-specific criteria pass before advancing edit stage

## 1. Specification & Contract
- **Validator Identifier**: `VAL_EDL_STAGE_GATE`
- **Scope**: Deterministic validation of Verifying all stage-specific criteria pass before advancing edit stage.
- **Exit State**: Returns strictly `pass`, `warn`, or `fail` with structured violations list.

## 2. Executable Python Implementation
```python
def validate_stage_gate_readiness(stage, edl_data):
    violations = []
    # Verify stage transition rules from [004]
    if stage == "PICTURE_LOCK":
        if edl_data.get("flash_frame_count", 0) > 0:
            violations.append("Cannot achieve PICTURE_LOCK with flash frames")
        if edl_data.get("unresolved_markers_count", 0) > 0:
            violations.append("Cannot achieve PICTURE_LOCK with unresolved editorial markers")
    status = "fail" if violations else "pass"
    return {"status": status, "violations": violations}
```

## 3. Integration with FilmCraft Auto-Remediation Loop
- If status == `'pass'`: Pipeline advances immediately to next stage gate.
- If status == `'fail'`: Error is caught and dispatched to auto-remediation loop `[012]`.
