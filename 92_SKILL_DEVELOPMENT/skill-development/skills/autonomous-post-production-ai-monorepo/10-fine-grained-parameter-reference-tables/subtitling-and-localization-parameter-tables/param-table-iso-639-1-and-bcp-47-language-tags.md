---
file_id: "[559]"
table_title: "ISO 639-1 and BCP-47 Standardized Language Tags"
governing_standard: "IETF BCP 47 / ISO 639-1 / ISO 3166-1"
archetype: "F"
---

# [559] Standardized language and regional script tags (`es-419`, `pt-BR`, `zh-Hans`)

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `IETF BCP 47 / ISO 639-1 / ISO 3166-1`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `ISO 639-1 and BCP-47 Standardized Language Tags`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| BCP 47 Tag | Language Name | Territory / Script | Directionality | Netflix Code |
|---|---|---|---|---|
| `en-US` | English | United States | LTR | `en` |
| `en-GB` | English | United Kingdom | LTR | `en-GB` |
| `es-419` | Spanish | Latin America | LTR | `es-419` |
| `es-ES` | Spanish | Spain (Castilian) | LTR | `es-ES` |
| `pt-BR` | Portuguese | Brazil | LTR | `pt-BR` |
| `pt-PT` | Portuguese | Portugal | LTR | `pt-PT` |
| `zh-Hans` | Chinese | Simplified Hanzi | LTR | `zh-Hans` |
| `zh-Hant` | Chinese | Traditional Hanzi | LTR | `zh-Hant` |
| `ja-JP` | Japanese | Japan | LTR / Vertical | `ja` |
| `ko-KR` | Korean | South Korea | LTR | `ko` |
| `ar-SA` | Arabic | Saudi Arabia | RTL | `ar` |
| `fr-FR` | French | France | LTR | `fr` |
| `de-DE` | German | Germany | LTR | `de` |

## 3. Deterministic Mathematical Formulation
Regex validator: `^[a-z]{2,3}(-[A-Z]{2}|-[0-9]{3}|-[A-Z][a-z]{3})?$`.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Always distinguish Latin American Spanish (`es-419`) from Castilian Spanish (`es-ES`) in timed-text headers.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
