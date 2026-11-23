---
file_id: "[553]"
table_title: "Platform Loudness Targets: LUFS, LRA, and True Peak Comparison"
governing_standard: "ITU-R BS.1770-4 / EBU R128 / ATSC A/85 / Streaming Specs"
archetype: "F"
---

# [553] Master comparison matrix across 18 global broadcast and streaming specs

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `ITU-R BS.1770-4 / EBU R128 / ATSC A/85 / Streaming Specs`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Platform Loudness Targets: LUFS, LRA, and True Peak Comparison`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Delivery Platform | Integrated Target | Tolerance (LU) | Max True Peak (dBTP) | Max Loudness Range (LRA) | Max Short-Term LUFS |
|---|---|---|---|---|---|
| EBU R128 (European Broadcast) | -23.0 LUFS | ±0.5 LU | -1.0 dBTP | <= 14.0 LU | -18.0 LUFS |
| ATSC A/85 (US Broadcast) | -24.0 LUFS | ±1.0 LU | -2.0 dBTP | <= 18.0 LU | N/A |
| Netflix Streaming | -27.0 LUFS | ±1.0 LU | -2.0 dBTP | <= 14.0 LU | N/A |
| Amazon Prime Video | -24.0 LUFS | ±1.0 LU | -2.0 dBTP | <= 14.0 LU | N/A |
| Apple TV+ / iTunes | -24.0 LUFS | ±1.0 LU | -1.0 dBTP | <= 12.0 LU | N/A |
| YouTube Standard | -14.0 LUFS | ±1.0 LU | -1.0 dBTP | N/A | N/A |
| Spotify (Normal) | -14.0 LUFS | ±1.0 LU | -1.0 dBTP | N/A | N/A |
| Apple Podcasts | -16.0 LUFS | ±1.0 LU | -1.0 dBTP | N/A | N/A |
| Disney+ / Hulu | -24.0 LUFS | ±1.0 LU | -2.0 dBTP | <= 14.0 LU | N/A |

## 3. Deterministic Mathematical Formulation
Integrated loudness formula: $LUFS = -0.691 + 10 \log_{10} \sum_{i} G_i \cdot z_i$ with K-frequency weighting.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Never deliver YouTube (-14 LUFS) mix masters to broadcast or Netflix (-23 / -27 LUFS); it triggers severe rejection.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
