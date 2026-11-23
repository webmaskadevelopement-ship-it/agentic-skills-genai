---
file_id: "[019]"
skill_path: "00-governance-and-schemas/schemas/schema-color-grade-specification.md"
role: "Master Schema Lock: Color Grade Specification (File B)"
parent_router: "[001]"
department_router: "[177]"
master_commands:
  - "BUILD_NODE_GRAPH"
  - "SET_PRIMARY_BALANCE"
  - "APPLY_HSL_QUALIFIER"
  - "SHAPE_TONAL_CURVES"
  - "EMIT_GRADE_SPEC"
validators:
  - "[573]" # validator-grade-schema-and-scope-evidence
  - "[574]" # validator-grade-lift-gamma-gain-bounds
  - "[575]" # validator-grade-node-graph-topological-order
  - "[576]" # validator-grade-skin-tone-vector-tolerance
  - "[577]" # validator-grade-sdr-hdr-legal-ire-compliance
---

# [019] Master Schema Lock: Color Grade Specification (File B)

## Block 1: Schema Identity & System Binding

* **Deliverable ID**: File B — Master Color Grade Specification.
* **Governing Standard**: SMPTE ST 2084 / BT.709 / BT.2020 / ACES 1.3 Specification and RFC 8259 JSON.
* **Upstream Generator Commands**: `BUILD_NODE_GRAPH` (`[499]`), `SET_PRIMARY_BALANCE` (`[500]`), `APPLY_HSL_QUALIFIER` (`[501]`), `SHAPE_TONAL_CURVES` (`[502]`), `APPLY_FILM_LOOK_AND_FX` (`[504]`), `EMIT_GRADE_SPEC` (`[506]`).
* **Downstream Consumers**:
  - DaVinci Resolve Scripting Adapter (`[596]`): Node tree generation and CDL/DRX injection.
  - Premiere Lumetri Adapter (`[600]`): Mapping values to Lumetri parameters.
  - Final QC Gate (`[445]`): Legal IRE gamut auditing.
* **Inspection Validators**: `[573]`, `[574]`, `[575]`, `[576]`, `[577]`, `[578]`.

---

## Block 2: Formal JSON Schema (Draft 2020-12)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://autonomous-post.ai/schemas/color-grade-specification.json",
  "title": "ColorGradeSpecification",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "project",
    "shot_id",
    "scene",
    "source_color_space",
    "target_delivery",
    "scope_evidence",
    "node_graph",
    "look",
    "finishing_effects"
  ],
  "properties": {
    "project": { "type": "string", "pattern": "^[A-Za-z0-9_-]+$" },
    "shot_id": { "type": "string", "pattern": "^[A-Z0-9_-]+$" },
    "scene": { "type": "integer", "minimum": 1 },
    "source_color_space": {
      "type": "string",
      "enum": [
        "ARRI_LogC3_AWG3",
        "ARRI_LogC4_AWG4",
        "RED_Log3G10_RWG",
        "Sony_SLog3_SGamut3Cine",
        "Canon_Log2_CinemaGamut",
        "Canon_Log3_CinemaGamut",
        "BMD_Film_Gen5",
        "Panasonic_VLog_VGamut",
        "Apple_Log",
        "Rec709_Gamma24"
      ]
    },
    "target_delivery": {
      "type": "string",
      "enum": ["Rec709_Gamma24", "DCI_P3_D65", "HDR_ST2084_PQ", "HDR_BT2100_HLG"]
    },
    "scope_evidence": {
      "type": "object",
      "additionalProperties": false,
      "required": ["waveform", "vectorscope", "parade"],
      "properties": {
        "waveform": {
          "type": "object",
          "additionalProperties": false,
          "required": ["black_point_ire", "white_point_ire", "highlight_clipping", "shadow_crush"],
          "properties": {
            "black_point_ire": { "type": "number", "minimum": 0.0, "maximum": 15.0 },
            "white_point_ire": { "type": "number", "minimum": 60.0, "maximum": 105.0 },
            "highlight_clipping": { "type": "string", "enum": ["none", "controlled", "specular_only"] },
            "shadow_crush": { "type": "string", "enum": ["none", "intentional_silhouette"] }
          }
        },
        "vectorscope": {
          "type": "object",
          "additionalProperties": false,
          "required": ["skin_tone_alignment", "dominant_color_cast", "saturation_envelope"],
          "properties": {
            "skin_tone_alignment": { "type": "string", "minLength": 10 },
            "dominant_color_cast": { "type": "string", "minLength": 6 },
            "saturation_envelope": { "type": "string", "minLength": 10 }
          }
        },
        "parade": {
          "type": "object",
          "additionalProperties": false,
          "required": ["channel_balance"],
          "properties": {
            "channel_balance": { "type": "string", "minLength": 15 }
          }
        }
      }
    },
    "node_graph": {
      "type": "array",
      "minItems": 12,
      "maxItems": 12,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["node_index", "node_name", "purpose", "parameters", "notes"],
        "properties": {
          "node_index": { "type": "integer", "minimum": 1, "maximum": 12 },
          "node_name": { "type": "string", "minLength": 3 },
          "purpose": {
            "type": "string",
            "enum": [
              "input_transform",
              "exposure_offset",
              "contrast_shaping",
              "white_balance_tint",
              "skin_qualifier",
              "environment_qualifier",
              "relighting_power_windows",
              "depth_map_atmosphere",
              "creative_look_split_tone",
              "film_print_emulation",
              "optical_finishing_fx",
              "output_transform_legal_limiter"
            ]
          },
          "parameters": {
            "type": "object",
            "additionalProperties": true,
            "properties": {
              "lift_rgb": {
                "type": "array",
                "minItems": 3,
                "maxItems": 3,
                "items": { "type": "number", "minimum": -0.25, "maximum": 0.25 }
              },
              "gamma_rgb": {
                "type": "array",
                "minItems": 3,
                "maxItems": 3,
                "items": { "type": "number", "minimum": 0.5, "maximum": 2.0 }
              },
              "gain_rgb": {
                "type": "array",
                "minItems": 3,
                "maxItems": 3,
                "items": { "type": "number", "minimum": 0.5, "maximum": 2.5 }
              },
              "offset_rgb": {
                "type": "array",
                "minItems": 3,
                "maxItems": 3,
                "items": { "type": "number", "minimum": -0.25, "maximum": 0.25 }
              },
              "contrast": { "type": "number", "minimum": 0.5, "maximum": 2.0 },
              "pivot": { "type": "number", "minimum": 0.1, "maximum": 0.9 },
              "saturation": { "type": "number", "minimum": 0.0, "maximum": 2.0 }
            }
          },
          "notes": { "type": "string", "minLength": 10 }
        }
      }
    },
    "look": {
      "type": "object",
      "additionalProperties": false,
      "required": ["emulation_stock", "blend_percentage", "print_characteristics"],
      "properties": {
        "emulation_stock": { "type": "string", "minLength": 4 },
        "blend_percentage": { "type": "number", "minimum": 0.0, "maximum": 100.0 },
        "print_characteristics": { "type": "string", "minLength": 10 }
      }
    },
    "shot_match_reference": { "type": ["string", "null"] },
    "finishing_effects": {
      "type": "object",
      "additionalProperties": false,
      "required": ["halation", "bloom", "film_grain", "vignette"],
      "properties": {
        "halation": {
          "type": "object",
          "additionalProperties": false,
          "required": ["enabled", "threshold", "intensity", "radius_px", "color_hex"],
          "properties": {
            "enabled": { "type": "boolean" },
            "threshold": { "type": "number", "minimum": 0.0, "maximum": 1.0 },
            "intensity": { "type": "number", "minimum": 0.0, "maximum": 1.0 },
            "radius_px": { "type": "number", "minimum": 0.0, "maximum": 100.0 },
            "color_hex": { "type": "string", "pattern": "^#[0-9A-Fa-f]{6}$" }
          }
        },
        "bloom": {
          "type": "object",
          "additionalProperties": false,
          "required": ["enabled", "threshold", "intensity"],
          "properties": {
            "enabled": { "type": "boolean" },
            "threshold": { "type": "number", "minimum": 0.0, "maximum": 1.0 },
            "intensity": { "type": "number", "minimum": 0.0, "maximum": 1.0 }
          }
        },
        "film_grain": {
          "type": "object",
          "additionalProperties": false,
          "required": ["enabled", "stock_type", "size_um", "intensity"],
          "properties": {
            "enabled": { "type": "boolean" },
            "stock_type": { "type": "string" },
            "size_um": { "type": "number", "minimum": 8.0, "maximum": 65.0 },
            "intensity": { "type": "number", "minimum": 0.0, "maximum": 1.0 }
          }
        },
        "vignette": {
          "type": "object",
          "additionalProperties": false,
          "required": ["enabled", "amount", "softness"],
          "properties": {
            "enabled": { "type": "boolean" },
            "amount": { "type": "number", "minimum": -1.0, "maximum": 1.0 },
            "softness": { "type": "number", "minimum": 0.0, "maximum": 100.0 }
          }
        }
      }
    }
  }
}
```

---

## Block 3: Load-Bearing Evidence Fields

1. `scope_evidence`:
   - Omitting `waveform`, `vectorscope`, or `parade` triggers immediate rejection via `[573]`.
   - Cites exact IRE levels, 123° skin I-line angle, and parade R=G=B channel neutrality.
2. `node_graph` (Strict 12 Nodes):
   - Enforces the standard 12-node serial/parallel architecture (`[206]`).
   - Node 01 MUST be `input_transform` and Node 12 MUST be `output_transform_legal_limiter` (`[575]`).

---

## Block 4: Cross-Field Mathematical Invariants

1. **Primary Color Balance Function**:
   For each channel $c \in \{R, G, B\}$:
   $$C_{\text{out}} = \text{clamp}\Big( \big( (C_{\text{in}} \times \text{gain}_c) + (\text{lift}_c \times (1.0 - C_{\text{in}})) + \text{offset}_c \big)^{1.0 / \text{gamma}_c}, 0.0, 1.0 \Big)$$
2. **SDR Legal IRE Bounds**:
   $$0.0 \le \text{black\_point\_ire} < \text{white\_point\_ire} \le 100.0$$
   *(SDR diffuse white target: $80.0 \le \text{white\_point\_ire} \le 90.0$, specular ceiling $\le 99.0\text{ IRE}$)*.

---

## Block 5: Canonical Valid Payload (File B Example)

```json
{
  "project": "APOLLO_11_DOC",
  "shot_id": "SC04_SH01",
  "scene": 4,
  "source_color_space": "ARRI_LogC4_AWG4",
  "target_delivery": "Rec709_Gamma24",
  "scope_evidence": {
    "waveform": {
      "black_point_ire": 3.4,
      "white_point_ire": 94.2,
      "highlight_clipping": "controlled",
      "shadow_crush": "none"
    },
    "vectorscope": {
      "skin_tone_alignment": "123.2° directly along I-line (0.8° delta)",
      "dominant_color_cast": "Neutral (center reticle delta dU: +0.001, dV: -0.002)",
      "saturation_envelope": "26.5% radius of 75% SMPTE target"
    },
    "parade": {
      "channel_balance": "R_min=3.4, G_min=3.3, B_min=3.4 IRE; R_max=94.2, G_max=94.1, B_max=94.0 IRE"
    }
  },
  "node_graph": [
    {
      "node_index": 1,
      "node_name": "Input CST & Temporal NR",
      "purpose": "input_transform",
      "parameters": { "cst": "ARRI LogC4 -> DaVinci Wide Gamut Intermediate", "tnr_frames": 2, "tnr_luma": 4.0 },
      "notes": "Normalize sensor log curve to wide intermediate space."
    },
    {
      "node_index": 2,
      "node_name": "Exposure Offset",
      "purpose": "exposure_offset",
      "parameters": { "offset_rgb": [0.012, 0.012, 0.012] },
      "notes": "+0.45 stop linear exposure lift placing 18% grey at 0.336 DWG."
    },
    {
      "node_index": 3,
      "node_name": "Contrast & Pivot",
      "purpose": "contrast_shaping",
      "parameters": { "contrast": 1.14, "pivot": 0.336 },
      "notes": "Sigmoidal contrast curve preserving shadow roll-off."
    },
    {
      "node_index": 4,
      "node_name": "White Balance & Tint",
      "purpose": "white_balance_tint",
      "parameters": { "lift_rgb": [0.002, 0.000, -0.002], "gain_rgb": [0.985, 1.000, 1.015] },
      "notes": "Neutralize warm 4800K daylight spill on lunar surface suit."
    },
    {
      "node_index": 5,
      "node_name": "Skin Qualifier",
      "purpose": "skin_qualifier",
      "parameters": { "hue_center": 22.0, "hue_width": 28.0, "sat": [0.15, 0.65], "lum": [0.25, 0.78], "mid_detail": -12.0 },
      "notes": "Parallel 1: Align astronaut facial reflection along 123° I-line."
    },
    {
      "node_index": 6,
      "node_name": "Environment Qualifier",
      "purpose": "environment_qualifier",
      "parameters": { "hue_center": 210.0, "hue_width": 35.0, "sat_mult": 0.85 },
      "notes": "Parallel 2: Tame lunar module gold foil specular reflections."
    },
    {
      "node_index": 7,
      "node_name": "Relighting Window",
      "purpose": "relighting_power_windows",
      "parameters": { "aspect": 0.65, "softness": 55.0, "gamma_mult": 1.04 },
      "notes": "Subtle circular spotlight on astronaut helmet faceplate."
    },
    {
      "node_index": 8,
      "node_name": "Depth Atmosphere",
      "purpose": "depth_map_atmosphere",
      "parameters": { "bg_lift": -0.015, "bg_contrast": 0.96 },
      "notes": "Enhance spatial depth separation between lunar lander and deep space."
    },
    {
      "node_index": 9,
      "node_name": "Split Tone & Matrix",
      "purpose": "creative_look_split_tone",
      "parameters": { "lift_rgb": [-0.005, 0.002, 0.008], "gain_rgb": [1.025, 1.008, 0.975] },
      "notes": "Cool shadow toe with warm solar specular highlights."
    },
    {
      "node_index": 10,
      "node_name": "Kodak 2383 Print Emulation",
      "purpose": "film_print_emulation",
      "parameters": { "stock": "Kodak_2383_D60", "mix": 75.0 },
      "notes": "Photochemical print contrast with cyan high-blues."
    },
    {
      "node_index": 11,
      "node_name": "Halation & Grain",
      "purpose": "optical_finishing_fx",
      "parameters": { "halation_threshold": 0.76, "halation_intensity": 0.22, "grain_size_um": 24.0, "grain_strength": 0.18 },
      "notes": "Subtle 35mm red emulsion scatter on solar rim lights."
    },
    {
      "node_index": 12,
      "node_name": "Output CST & Legal Soft-Clip",
      "purpose": "output_transform_legal_limiter",
      "parameters": { "output_cst": "DWG Intermediate -> Rec.709 Gamma 2.4", "legal_clip": true },
      "notes": "Display transform with 0.0–100.0 IRE soft knee limiter."
    }
  ],
  "look": {
    "emulation_stock": "Kodak 2383 D60 Print Emulation",
    "blend_percentage": 75.0,
    "print_characteristics": "Steep S-curve toe at 3.4 IRE, rich cyan shadows, natural warm skin highlights."
  },
  "shot_match_reference": null,
  "finishing_effects": {
    "halation": {
      "enabled": true,
      "threshold": 0.76,
      "intensity": 0.22,
      "radius_px": 16.0,
      "color_hex": "#FF3814"
    },
    "bloom": {
      "enabled": true,
      "threshold": 0.82,
      "intensity": 0.14
    },
    "film_grain": {
      "enabled": true,
      "stock_type": "35mm_500T",
      "size_um": 24.0,
      "intensity": 0.18
    },
    "vignette": {
      "enabled": true,
      "amount": -0.15,
      "softness": 45.0
    }
  }
}
```

---

## Block 6: Canonical Invalid Payload & Error Trace

### Invalid Snippet (Missing Scopes & Node 12 Out of Order)
```json
{
  "project": "APOLLO_11_DOC",
  "shot_id": "SC04_SH01",
  "scene": 4,
  "source_color_space": "ARRI_LogC4_AWG4",
  "target_delivery": "Rec709_Gamma24",
  "scope_evidence": {
    "waveform": {
      "black_point_ire": 3.4,
      "white_point_ire": 108.5,
      "highlight_clipping": "none",
      "shadow_crush": "none"
    },
    "vectorscope": {
      "skin_tone_alignment": "good",
      "dominant_color_cast": "none",
      "saturation_envelope": "normal"
    },
    "parade": {
      "channel_balance": "balanced"
    }
  },
  "node_graph": [],
  "look": {
    "emulation_stock": "LUT",
    "blend_percentage": 100.0,
    "print_characteristics": "Cinematic"
  },
  "finishing_effects": {
    "halation": { "enabled": false, "threshold": 0.0, "intensity": 0.0, "radius_px": 0.0, "color_hex": "#000000" },
    "bloom": { "enabled": false, "threshold": 0.0, "intensity": 0.0 },
    "film_grain": { "enabled": false, "stock_type": "none", "size_um": 10.0, "intensity": 0.0 },
    "vignette": { "enabled": false, "amount": 0.0, "softness": 0.0 }
  }
}
```

### Validator Diagnostic Error Trace
```
VALIDATION FAILED: [573] validator-grade-schema-and-scope-evidence
- ERROR 1: /scope_evidence/waveform/white_point_ire: 108.5 exceeds maximum 105.0 IRE (Illegal Broadcast Excursion)
- ERROR 2: /scope_evidence/vectorscope/skin_tone_alignment: length 4 is less than minimum 10 characters (Vague aesthetic claim)
- ERROR 3: /scope_evidence/parade/channel_balance: length 8 is less than minimum 15 characters
VALIDATION FAILED: [575] validator-grade-node-graph-topological-order
- ERROR 4: /node_graph: array has 0 items, exactly 12 items required
- ERROR 5: Node 01 missing: must be "input_transform"
- ERROR 6: Node 12 missing: must be "output_transform_legal_limiter"
```
