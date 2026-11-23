---
file_id: "[533]"
table_title: "J-Cut and L-Cut Frame Offset Ranges by Genre"
governing_standard: "Narrative Editorial Pacing Conventions"
archetype: "F"
---

# [533] Standard audio lead/trail frame counts across drama, doc, comedy

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `Narrative Editorial Pacing Conventions`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `J-Cut and L-Cut Frame Offset Ranges by Genre`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Genre | Edit Type | Audio Lead / Trail (Frames @ 24fps) | Temporal Offset (ms) | Typical Motivation |
|---|---|---|---|---|
| Drama / Dialogue | J-Cut (Audio First) | -6 to -14 frames | -250ms to -580ms | Anticipate emotional reaction |
| Drama / Dialogue | L-Cut (Video First) | +8 to +18 frames | +330ms to +750ms | Linger on reaction while speaker speaks |
| Comedy / Sitcom | J-Cut (Punchline) | -3 to -6 frames | -125ms to -250ms | Rapid reaction snap |
| Action / Thriller | J-Cut (Impact SFX) | -4 to -8 frames | -160ms to -330ms | Audio teaser preceding visual cut |
| Documentary | L-Cut (Interview Bed) | +12 to +36 frames | +500ms to +1500ms | B-roll covers continuous dialogue |
| Horror / Suspense | J-Cut (Stinger) | -8 to -16 frames | -330ms to -660ms | Shock / fear induction prior to reveal |

## 3. Deterministic Mathematical Formulation
$\Delta T_{audio} = Record_{in}(audio) - Record_{in}(video)$. J-Cut: $\Delta T < 0$. L-Cut: $\Delta T > 0$.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Verify that audio head handles exist on source media before scheduling a negative J-cut offset.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
