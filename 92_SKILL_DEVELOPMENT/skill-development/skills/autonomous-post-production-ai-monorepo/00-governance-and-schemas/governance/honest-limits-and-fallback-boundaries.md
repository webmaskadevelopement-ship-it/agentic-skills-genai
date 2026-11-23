# [007] Honest Limits and Fallback Boundaries of Autonomous Post-Production Execution

## 1. Scope Definition & Operational Domain
This governance contract defines the hard physical, legal, and perceptual boundaries of autonomous post-production execution within the monorepo and FilmCraft runtime. Any operation that crosses these boundaries must halt execution and trigger human escalation under `[006]`.

## 2. Deterministic Execution Boundaries

### 2.1 Aesthetic Subjectivity vs. Metric Verification
The autonomous engine operates strictly within mathematically verifiable envelopes:
- **Audio**: Verification of ITU-R BS.1770-4 Integrated Loudness (LUFS), True Peak (dBTP), Spectral Balance (Hz), and Phase Correlation [-1.0, +1.0]. The engine cannot determine whether a musical track "feels emotional" without explicit score parameters.
- **Color**: Verification of legal/extended range code values, skin-tone line alignment (123° I-line on vectorscope within ±4°), gamut clipping, and contrast ratio. The engine cannot decide between two creative looks unless guided by explicit reference frames.
- **Editorial**: Verification of 180° rule, eyeline matching, beat-grid alignment, dialogue cadence, and flash frames. The engine cannot evaluate comedic timing variance under 3 frames without human taste-gate review.

### 2.2 Processing & Rendering Limitations
- **Resolution**: Native raster processing up to 8192x4320 (8K DCI). Scaling operations must use Lanczos-3 or Bicubic spline filters with explicit anti-ringing clamping.
- **Color Depth**: Pipeline is strictly floating-point 32-bit linear or 16-bit half-float ACEScc/ACEScct. 8-bit quantization is prohibited except at final distribution encode.
- **Tick Resolution**: FilmCraft timeline operations are bound to 254,016,000,000 ticks/sec. Fractional-tick operations are rounded to nearest whole tick using bankers rounding.

## 3. Explicit Prohibitions & Hard Fails
The autonomous engine must immediately reject execution if:
1. Audio true peak exceeds -0.5 dBTP in broadcast delivery mode.
2. Video signal contains out-of-gamut Rec.709 pixels exceeding 1% of total active picture area.
3. Subtitle text duration is under 833ms (20 frames at 24fps) or exceeds 7000ms.
4. An EDL cut causes an audio click due to non-zero-crossing cut without a minimum 2-frame crossfade.

## 4. Fallback State Machine
When an operation encounters an unsolvable constraint:
```
[Operation Triggered] -> [Check Parameter Bounds]
       |
       v
[Within Bounds?] --YES--> [Execute & Verify via Cluster 11]
       |
      NO
       v
[Fallback to Studio Default ([684])]
       |
       v
[Requires Creative Decision?] --YES--> [Trigger HITL Taste-Gate ([006])]
       |
      NO
       v
[Apply Deterministic Clamp ([012])]
```
