---
file_id: "[535]"
table_title: "Average Shot Length (ASL) Benchmarks by Era and Genre"
governing_standard: "Cinematic Metric Histograms"
archetype: "F"
---

# [535] ASL reference benchmarks across genres and tempo targets

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `Cinematic Metric Histograms`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Average Shot Length (ASL) Benchmarks by Era and Genre`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Era / Format | Genre | Target ASL (Seconds) | Frames / Shot (24fps) | Pacing Description |
|---|---|---|---|---|
| Golden Age Hollywood (1930-1950) | Classic Drama | 8.0s – 12.0s | 192 – 288 frames | Proscenium staging, long takes |
| Modern Theatrical (1990-2010) | Mainstream Drama | 4.0s – 6.0s | 96 – 144 frames | Dynamic coverage, continuity |
| Modern Action (2015-Present) | Fast Action / Chase | 1.5s – 2.5s | 36 – 60 frames | Frenetic, multi-camera kinetic cuts |
| Television Commercial | 30s Brand Spot | 1.0s – 1.8s | 24 – 43 frames | High density information transfer |
| Social Video (TikTok / Reels) | Short-Form UGC | 0.8s – 1.4s | 19 – 34 frames | Ultra-compressed dopamine pacing |
| Art House / Slow Cinema | Meditative Drama | 15.0s – 60.0s | 360 – 1440 frames | Deep observation, real-time cadence |

## 3. Deterministic Mathematical Formulation
$ASL = \frac{\text{Total Running Time (seconds)}}{\text{Total Number of Cuts}}$. Standard deviation $\sigma_{ASL} < 0.5 \times ASL$ indicates rhythmic monotony.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: A well-paced sequence modulates ASL over time: alternating between tight bursts (low ASL) and resting shots (high ASL).
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
