---
file_id: "[556]"
table_title: "Audio Sample Rate and Bit Depth Data Rates"
governing_standard: "AES3 / EBU Tech 3280 Digital Audio"
archetype: "F"
---

# [556] Uncompressed PCM bitrates for 16/24/32-bit float across 44.1–192 kHz

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `AES3 / EBU Tech 3280 Digital Audio`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Audio Sample Rate and Bit Depth Data Rates`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Sample Rate (kHz) | Bit Depth | Channels | Bitrate (kbps) | Megabytes / Minute | Gigabytes / Hour | Application |
|---|---|---|---|---|---|---|
| 44.1 kHz | 16-bit | 2 (Stereo) | 1,411.2 kbps | 10.58 MB/min | 0.635 GB/hr | CD Redbook Audio |
| 48.0 kHz | 24-bit | 1 (Mono) | 1,152.0 kbps | 8.64 MB/min | 0.518 GB/hr | Film/TV Dialogue Track |
| 48.0 kHz | 24-bit | 2 (Stereo) | 2,304.0 kbps | 17.28 MB/min | 1.037 GB/hr | Film/TV Stereo Delivery |
| 48.0 kHz | 24-bit | 6 (5.1 Surround) | 6,912.0 kbps | 51.84 MB/min | 3.110 GB/hr | 5.1 Print Master Stem |
| 96.0 kHz | 24-bit | 2 (Stereo) | 4,608.0 kbps | 34.56 MB/min | 2.074 GB/hr | High-Res Foley / FX Capture |
| 192.0 kHz | 32-bit Float | 1 (Mono) | 6,144.0 kbps | 46.08 MB/min | 2.765 GB/hr | Ultrasonic Sound Design Pitching |

## 3. Deterministic Mathematical Formulation
$Bitrate = SampleRate \times BitDepth \times Channels$. $Storage_{GB/hr} = \frac{Bitrate \times 3600}{8 \times 10^9}$.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: FilmCraft standard project sample rate is locked to 48.0 kHz 24-bit PCM across all stems.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
