---
file_id: "[586]"
validator_name: "VAL_MIX_LOUDNESS"
archetype: "G"
validation_type: "Deterministic Python Assertion"
---

# [586] Verifying target LUFS matches platform spec and True Peak <= ceiling

## 1. Specification & Contract
- **Validator Identifier**: `VAL_MIX_LOUDNESS`
- **Scope**: Deterministic validation of Verifying target LUFS matches platform spec and True Peak <= ceiling.
- **Exit State**: Returns strictly `pass`, `warn`, or `fail` with structured violations list.

## 2. Executable Python Implementation
```python
def validate_mix_loudness(integrated_lufs, true_peak_dbtp, target_lufs=-23.0, max_dbtp=-1.0):
    violations = []
    if abs(integrated_lufs - target_lufs) > 0.5:
        violations.append(f"Integrated loudness {integrated_lufs} LUFS exceeds ±0.5 LU tolerance from {target_lufs}")
    if true_peak_dbtp > max_dbtp:
        violations.append(f"True Peak {true_peak_dbtp} dBTP exceeds {max_dbtp} dBTP ceiling")
    status = "fail" if violations else "pass"
    return {"status": status, "violations": violations}
```

## 3. Integration with FilmCraft Auto-Remediation Loop
- If status == `'pass'`: Pipeline advances immediately to next stage gate.
- If status == `'fail'`: Error is caught and dispatched to auto-remediation loop `[012]`.
