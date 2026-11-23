# [010] Version Control and Git Diff Timeline Specification

## 1. Specification Overview
All timeline deliverables, color specifications, mix sheets, and subtitle manifests in this monorepo are schema-locked JSON documents stored under standard Git version control. This protocol defines how timeline events are diffed, merged, and tagged.

## 2. Canonical JSON Normalization
To ensure byte-for-byte reproducible diffs:
1. Object keys must be sorted alphabetically at all nesting levels (`sort_keys=True`).
2. Indentation must be exactly 2 spaces.
3. Floating point values must be rounded to a defined precision:
   - Gain/Loudness: 2 decimal places (`-23.00`).
   - Color Wheels/Offsets: 4 decimal places (`0.0125`).
   - Timecode frames: Strict integers (`1440`).
4. Trailing line breaks must follow Unix LF (`\n`).

## 3. Timeline Diff Syntax & Conflict Resolution
When two branches diverge on an EDL cut manifest:
- **Non-overlapping cuts**: Automatically merged chronologically by `record_in`.
- **Overlapping cuts on same track**: Flagged as `TIMELINE_MERGE_CONFLICT`.
- **Resolution priority**:
  1. If tagged `LOCKED_PICTURE`, editorial changes are blocked.
  2. If untagged, the latest commit hash with passing QC validation (`[029]`) takes precedence.
