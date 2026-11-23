---
file_id: "[552]"
table_title: "Foley and SFX Relative Mix Levels Below Dialogue Reference"
governing_standard: "Film Re-Recording Mix Conventions"
archetype: "F"
---

# [552] Typical dBFS placement of footsteps, cloth, impacts, and beds below DX

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `Film Re-Recording Mix Conventions`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Foley and SFX Relative Mix Levels Below Dialogue Reference`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Audio Category | Target Level Relative to Dialogue | Typical RMS (dBFS) | Peak Target (dBFS) | Spatial Placement |
|---|---|---|---|---|
| Hero Dialogue (Anchor) | 0.0 dB (Reference) | -24 to -18 dBFS | -8 to -4 dBFS | Center Channel (C) |
| Footsteps (Hard Surface) | -12 to -16 dB | -34 to -30 dBFS | -18 dBFS | Panned to character position |
| Cloth Movement / Rustle | -18 to -24 dB | -42 to -36 dBFS | -24 dBFS | Center / Stereo pair |
| Hand Props (Cup, Keys, Door) | -8 to -14 dB | -30 to -24 dBFS | -12 dBFS | Point source at action |
| Room Tone / Ambience Bed | -24 to -32 dB | -48 to -40 dBFS | -32 dBFS | Wide Stereo / 5.1 Surround |
| Heavy Impacts / Explosions | +4 to +8 dB (Above DX) | -16 to -12 dBFS | -1.5 dBFS | L/C/R + LFE Subwoofer (+10dB) |
| Underscore Music Bed | -10 to -14 dB | -32 to -26 dBFS | -14 dBFS | L/R + Surround (Center notched) |

## 3. Deterministic Mathematical Formulation
Summed stem power: $L_{total} = 10 \log_{10}\left(10^{L_{DX}/10} + 10^{L_{MX}/10} + 10^{L_{FX}/10}\right)$.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Foley must sit behind dialogue; if Foley causes dialogue to duck, Foley is mixed at least 4dB too hot.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
