# MPA-RFC-RI: Realizer Interface

**Status:** Draft v0.1 — first thin-RFC pass.
**Targets:** [v9 (compressed)](../framework/v9_compressed.md), [RFC-1 v0.2](MPA-RFC-1_Spec-Object.md) (spec-object input), [RFC-S v0.2](MPA-RFC-S_Scale-Management.md) (intents at realizer junction), [RFC-2 v0.1](MPA-RFC-2_FDR-Signatures.md) (signature targets), [RFC-V v0.1](MPA-RFC-V_Reference-Vocabulary.md) (canonical labels).
**Companion:** [Architectural Block-In v0.2](../architecture/MPA_Architectural_Block-In.md), [`reference-drivers/surface-code-qec.md`](../reference-drivers/surface-code-qec.md), [RFC-3 v0.1](MPA-RFC-3_Consistency-Completeness.md).

---

## 0. Foundational principles

Inherits the five from the [Architectural Block-In](../architecture/MPA_Architectural_Block-In.md). RFC-RI sits at the realizer junction (RFC-S §3): canonical representation is observer-relative, intent-flagged, demand-envelope-bounded.

## 1. Object

The **realizer-interface document** is the artifact that compilation emits from a spec object + intent, and that a substrate-specific realizer consumes to find substrate parameters realizing the canonical structure at the declared intent. It is the output-device-transform analog from color management — the contract between the canonical working space and a substrate-specific realizer.

## 2. Shape

```
R_doc = (spec_ref, intent, canonical_snapshot, signature_targets, acceptance, realizer_class_target)
```

| Field | Content |
|---|---|
| `spec_ref` | Spec-object ID (RFC-1) |
| `intent` | One of {I1..I5} (RFC-V §2) |
| `canonical_snapshot` | The spec's canonical representation at the spec-declared $\tau_{obs}$, projected through `intent`'s mapping operation (RFC-S §3) |
| `signature_targets` | Per-spec-object expected FDR signatures (RFC-2 schema) — what the realized substrate must produce |
| `acceptance` | Per-intent forward + round-trip thresholds (RFC-S §5 metric table) |
| `realizer_class_target` | Substrate class the realizer must implement; must match an available driver's `substrate_class` |

Schema in [Appendix A](#appendix-a-schema).

## 3. Invariants

A realizer-interface document is **valid** iff:

1. **Spec resolution.** `spec_ref` resolves to a valid spec object (RFC-1 §3).
2. **Intent-conformance.** `canonical_snapshot` reflects `intent`'s mapping operation on out-of-gamut content per RFC-S §3 (e.g., scaled-uniform under I1; unmodified-but-rejected under I2 if any element is out-of-gamut).
3. **Acceptance declaration.** `acceptance` carries forward and round-trip thresholds appropriate to `intent`'s metric (RFC-S §5).
4. **Cross-artifact consistency.** Constellation satisfies [RFC-3](MPA-RFC-3_Consistency-Completeness.md) §3 (C-rules: spec gamut, intent compatibility, realizer class, persistence depth) and §4 (K1: signature-target completeness).

## 4. Operations

| Operation | Signature |
|---|---|
| Compile | $\text{spec} \times \text{intent} \to R_\text{doc}$ — produced by mpa-character or equivalent authoring environment |
| Validate | $R_\text{doc} \to \{\text{valid}, \text{diagnostics}[]\}$ — preserves §3 |
| Realize | $R_\text{doc} \times \text{realizer} \to (\text{substrate parameters}, \text{predicted substrate-native data})$ — substrate-specific |
| Realizer-side round-trip | $R_\text{doc} \times \text{realized substrate} \to \text{measured signatures}$ — compared to `signature_targets` per RFC-S §5 |

The realizer itself is substrate-specific (one per substrate class, paired with a driver of the same class). The interface document is universal.

## 5. Falsifiers

A document is **invalid** if:

- Schema violation (Appendix A).
- `spec_ref` resolves to an invalid spec.
- `intent` not in {I1..I5}.
- `canonical_snapshot` does not reflect `intent`'s mapping operation (e.g., out-of-gamut content unscaled under I1; adjusted under I2).
- Missing `signature_targets` for any spec-object element.
- Missing `acceptance` thresholds for the declared `intent`.
- `realizer_class_target` has no compatible driver, or compatible driver's envelope does not cover the spec's $(\tau_{obs}, D)$.

## 6. Pointer

| What | Where |
|---|---|
| Spec-object structure (compilation input) | [RFC-1 §2](MPA-RFC-1_Spec-Object.md) |
| Intent semantics + gamut-mapping ops + per-intent metrics | [RFC-S §3, §5](MPA-RFC-S_Scale-Management.md) |
| Signature-target schema | [RFC-2 §2](MPA-RFC-2_FDR-Signatures.md) |
| Driver-profile structure (realizer's pair) | [RFC-S §4](MPA-RFC-S_Scale-Management.md) + [`reference-drivers/surface-code-qec.md`](../reference-drivers/surface-code-qec.md) |
| Canonical labels | [RFC-V](MPA-RFC-V_Reference-Vocabulary.md) |

---

## Appendix A: Schema

JSON Schema at [`schema/realizer-interface.v0.1.json`](../schema/realizer-interface.v0.1.json). §2 mirrors the schema's field structure as a reading aid.

```
realizer_interface_doc = {
  spec_ref: <spec object id>,
  intent: one_of(I1, I2, I3, I4, I5),
  canonical_snapshot: <spec's canonical representation at declared tau_obs, intent-projected>,
  signature_targets: [<RFC-2 fdr_signature instance>, ...],
  acceptance: {
    forward_threshold: <per-intent metric value>,
    round_trip_threshold: <per-intent metric value>
  },
  realizer_class_target: <substrate_class identifier>
}
```

## Appendix B: What this RFC does not specify (deferred)

- **Realizer search algorithms.** How a substrate-specific realizer finds substrate parameters is implementation-specific; out of protocol scope.
- **Reference-target governance** (Block-In open). Which substrates are realizer-ready / reference targets — operational discipline, not protocol-layer.
- **Conversion-gain measurement** (Block-In open). Whether a realizer "clarifies" substrate behavior beyond meeting acceptance thresholds — operational. One natural form: round-trip distance reduction across driver / realizer iterations (RFC-S §5 metric improving as the pair is refined).
- **Predicted-observables format.** Substrate-native; lives in the substrate's driver / realizer pair, not in the universal interface document.

## Appendix C: Open

1. **Multi-substrate compilation.** A spec may target a class of substrates rather than one. Whether `realizer_class_target` admits union types or requires a single class is open; v0.1 commits to single class.
2. **Intent-tuple compilation.** RFC-S §3 admits intent composition (union-of-preserved-invariants rule). Whether `R_doc` carries one intent or a tuple is open; v0.1 commits to one.

---

## Versioning

| Version | Status | Change |
|---|---|---|
| **v0.1** | **current** | First thin-RFC pass. Realizer-interface document shape, invariants, operations. Reference-target governance and conversion-gain measurement gestured at in Appendix B; remain Block-In open. |

**Compatibility.** Within v0.x: schema additions only. Removal of fields requires v1.0+ revision.

## Page-budget self-check

Target: ≤1 page (CLAUDE.md table for RFC-S/RFC-2/RFC-3/RFC-RI).

Body §0–§6 ≈ 55 lines. Appendices A–C ≈ 22 lines. Versioning + self-check ≈ 10 lines. **Total ≈ 1.7 pages — over target by ~⅔ page.**

**Debt-marker.** (a) closed by RFC-3 v0.1: §3 inv. 3 + inv. 5 collapsed into new inv. 4 (RFC-3 reference); §3 dropped from five to four invariants. (b) §6 Pointer remains wider than other RFCs — operational, since RFC-RI is downstream of five distinct artifacts; revisable in v0.2 if RFC-V centralization absorbs more of the labels currently routed through §6. (c) Appendix B Block-In gestures stand (reference-target governance, conversion-gain measurement) — these are operational discipline, not absorbable into protocol RFCs.
