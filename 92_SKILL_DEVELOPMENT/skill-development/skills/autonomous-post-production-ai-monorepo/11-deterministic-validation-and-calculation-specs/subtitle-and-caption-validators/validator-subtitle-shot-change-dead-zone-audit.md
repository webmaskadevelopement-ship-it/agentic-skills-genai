---
file_id: "[582]"
validator_name: "VAL_SUBTITLE_DEAD_ZONE"
archetype: "G"
validation_type: "Deterministic Python Assertion"
---

# [582] Cross-checking every cue in/out timestamp against EDL cut points

## 1. Specification & Contract
- **Validator Identifier**: `VAL_SUBTITLE_DEAD_ZONE`
- **Scope**: Deterministic validation of Cross-checking every cue in/out timestamp against EDL cut points.
- **Exit State**: Returns strictly `pass`, `warn`, or `fail` with structured violations list.

## 2. Executable Python Implementation
```python
def validate_shot_change_dead_zone(cue_start_frames, cut_frames):
    violations = []
    for cue_f in cue_start_frames:
        for cut_f in cut_frames:
            gap = cue_f - cut_f
            if 2 <= gap <= 11:
                violations.append(f"Cue at frame {cue_f} violates dead-zone ({gap} frames post-cut at {cut_f})")
    status = "fail" if violations else "pass"
    return {"status": status, "violations": violations}
```

## 3. Integration with FilmCraft Auto-Remediation Loop
- If status == `'pass'`: Pipeline advances immediately to next stage gate.
- If status == `'fail'`: Error is caught and dispatched to auto-remediation loop `[012]`.
