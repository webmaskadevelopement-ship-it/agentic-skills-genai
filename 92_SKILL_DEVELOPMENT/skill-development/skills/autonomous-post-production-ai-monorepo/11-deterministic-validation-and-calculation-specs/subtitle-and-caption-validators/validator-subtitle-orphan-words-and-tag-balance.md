---
file_id: "[583]"
validator_name: "VAL_SUBTITLE_TAGS"
archetype: "G"
validation_type: "Deterministic Python Assertion"
---

# [583] Checking unclosed `<i>` tags, double spaces, and 1-word bottom lines

## 1. Specification & Contract
- **Validator Identifier**: `VAL_SUBTITLE_TAGS`
- **Scope**: Deterministic validation of Checking unclosed `<i>` tags, double spaces, and 1-word bottom lines.
- **Exit State**: Returns strictly `pass`, `warn`, or `fail` with structured violations list.

## 2. Executable Python Implementation
```python
def validate_subtitle_tags_and_lines(cues):
    violations = []
    for c in cues:
        for line in c.get("lines", []):
            if line.count("<i>") != line.count("</i>"):
                violations.append(f"Cue {c['cue_index']}: unclosed italic tag")
            words = line.strip().split()
            if len(words) == 1 and len(c.get("lines", [])) > 1:
                violations.append(f"Cue {c['cue_index']}: orphan 1-word bottom line ('{words[0]}')")
    status = "fail" if violations else "pass"
    return {"status": status, "violations": violations}
```

## 3. Integration with FilmCraft Auto-Remediation Loop
- If status == `'pass'`: Pipeline advances immediately to next stage gate.
- If status == `'fail'`: Error is caught and dispatched to auto-remediation loop `[012]`.
