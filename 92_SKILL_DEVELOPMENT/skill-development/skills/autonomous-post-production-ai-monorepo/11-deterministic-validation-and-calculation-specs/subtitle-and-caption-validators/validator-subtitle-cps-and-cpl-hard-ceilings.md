---
file_id: "[580]"
validator_name: "VAL_SUBTITLE_CPS_CPL"
archetype: "G"
validation_type: "Deterministic Python Assertion"
---

# [580] Flagging every cue where `cps > limit` or `cpl > limit`

## 1. Specification & Contract
- **Validator Identifier**: `VAL_SUBTITLE_CPS_CPL`
- **Scope**: Deterministic validation of Flagging every cue where `cps > limit` or `cpl > limit`.
- **Exit State**: Returns strictly `pass`, `warn`, or `fail` with structured violations list.

## 2. Executable Python Implementation
```python
def validate_subtitle_cps_cpl(cues, max_cps=20.0, max_cpl=42):
    violations = []
    for c in cues:
        if c["cps"] > max_cps:
            violations.append(f"Cue {c['cue_index']}: CPS {c['cps']} exceeds {max_cps}")
        for l in c.get("lines", []):
            if len(l) > max_cpl:
                violations.append(f"Cue {c['cue_index']}: line length {len(l)} exceeds {max_cpl} CPL")
    status = "fail" if violations else "pass"
    return {"status": status, "violations": violations}
```

## 3. Integration with FilmCraft Auto-Remediation Loop
- If status == `'pass'`: Pipeline advances immediately to next stage gate.
- If status == `'fail'`: Error is caught and dispatched to auto-remediation loop `[012]`.
