# [009] Cross-Department Ripple Propagation Protocol

## 1. Purpose & Governing Principle
When an editorial trim occurs in Cluster 02 (`[101]`), it causes a non-linear temporal displacement across all downstream departments. This document defines the exact mathematical transformation matrix that updates:
1. Color Grade Nodes & Keyframe Timestamps (`[177]`)
2. Dialogue Cuts, Room Tone, and Foley Tracks (`[267]`)
3. VFX Plate Handles and Comp Range Manifests (`[378]`)
4. Timed-Text Subtitle Cues and Shot-Change Snapping (`[335]`)

## 2. Mathematical Ripple Equation
Let an EDL cut event $E_k$ be modified at record timecode $T_{rec}(k)$ with delta $\Delta F$ (in integer frames):
$$\Delta F = F_{new} - F_{old}$$

For every downstream event $i$ across all tracks where $T_{start}(i) > T_{rec}(k)$:
$$T_{start}'(i) = T_{start}(i) + \Delta F$$
$$T_{end}'(i) = T_{end}(i) + \Delta F$$

If $T_{start}(i) \le T_{rec}(k) < T_{end}(i)$ (event overlaps the trim boundary):
- **Video/Color**: Adjust clip head/tail by $\Delta F$ frames while keeping source timecode anchor locked:
  $$TC_{src\_out}' = TC_{src\_out} + \Delta F$$
- **Audio**: Apply a ripple edit if track is locked, or split and insert synthesized room-tone fill if gap is created:
  $$Duration_{fill} = |\Delta F| 	imes 	ext{frame\_duration}$$
- **Subtitles**: If trim boundary intersects a subtitle cue $[C_{in}, C_{out}]$, re-evaluate subtitle duration:
  $$D_{new} = C_{out}' - C_{in}'$$
  If $D_{new} < 20 	ext{ frames}$ (833ms at 24fps), trigger auto-resegmentation under `[341]`.

## 3. Departmental Notification DAG
```
     [Editorial Trim ΔF]
              |
     +--------+--------+
     |                 |
     v                 v
[Color Reposition]  [Sound Track Ripple]
     |                 |
     v                 v
[VFX Plate Check]   [Subtitle Retiming & Snap]
     |                 |
     +--------+--------+
              |
              v
     [Consolidated Conform Audit]
```
