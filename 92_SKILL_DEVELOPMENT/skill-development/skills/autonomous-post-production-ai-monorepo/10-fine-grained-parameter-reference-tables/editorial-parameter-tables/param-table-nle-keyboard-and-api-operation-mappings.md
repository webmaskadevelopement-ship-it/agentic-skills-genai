---
file_id: "[538]"
table_title: "NLE Keyboard and API Operation Mappings"
governing_standard: "Cross-Platform NLE Interchange Specification"
archetype: "F"
---

# [538] Mapping trim/slip/slide/roll/ripple operations to Resolve/Premiere/Avid

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `Cross-Platform NLE Interchange Specification`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `NLE Keyboard and API Operation Mappings`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Editing Action | FilmCraft MCP Command | DaVinci Resolve Python API | Premiere Pro ExtendScript | Avid Media Composer API |
|---|---|---|---|---|
| Insert Edit | `timeline.place` | `timeline.InsertTitle()` | `track.insertClip()` | `Track.Insert()` |
| Overwrite Edit | `timeline.overwrite` | `timeline.Overwrite()` | `track.overwriteClip()` | `Track.Overwrite()` |
| Razor / Split | `timeline.razor` | `timeline.SplitSelectedTimelineClip()` | `clip.split()` | `SubClip.Split()` |
| Ripple Delete | `timeline.ripple_delete` | `timeline.DeleteClips([clip], True)` | `clip.remove(True)` | `Track.RippleDelete()` |
| Slip Clip | `timeline.slip` | `clip.SetSourceStartFrame()` | `clip.setInPoint()` | `Clip.Slip()` |
| Roll Cut | `timeline.roll` | `timeline.RollCut()` | `clip.rollCut()` | `Track.Roll()` |
| Set Color Grade | `effects.set_wheels` | `node.SetPrimaries()` | `lumetri.setValues()` | `ColorCorrection.Set()` |

## 3. Deterministic Mathematical Formulation
Temporal frame conversion invariant: $Ticks = Frames \times \frac{254,016,000,000}{fps}$.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: FilmCraft MCP provides deterministic microsecond execution without GUI focus dependencies.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
