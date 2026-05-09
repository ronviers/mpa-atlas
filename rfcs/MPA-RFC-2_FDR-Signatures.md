# MPA-RFC-2: FDR-Signature Contract

**Status:** Draft v0.1 — first thin-RFC pass (no block-in stage, per Block-In §Next-session priorities).
**Targets:** [v9 (compressed, operational)](../framework/v9_compressed.md). Per-regime parametric shapes + universality-invariant table are the load-bearing imports.
**Companion:** [Architectural Block-In v0.2](../architecture/MPA_Architectural_Block-In.md), [RFC-1 v0.2](MPA-RFC-1_Spec-Object.md), [RFC-S v0.2](MPA-RFC-S_Scale-Management.md), [`reference-drivers/surface-code-qec.md`](../reference-drivers/surface-code-qec.md), [RFC-3 v0.1](MPA-RFC-3_Consistency-Completeness.md), [RFC-V v0.1](MPA-RFC-V_Reference-Vocabulary.md), [RFC-RI v0.1](MPA-RFC-RI_Realizer-Interface.md)

---

## 0. Foundational principles

Inherits the five principles from the [Architectural Block-In](../architecture/MPA_Architectural_Block-In.md), declared (not re-derived):

1. **Color-management discipline.** Three layers; transforms declared, named, versioned, swappable.
2. **Observer-driven scale management.** $\tau_{obs}$ is the camera; signatures are observer-relative.
3. **Demand-bounded sufficiency.** Signature precision sized to declared demand. **The MPA is not the bottleneck.**
4. **Singular working-space path.** Within an RFC version, exactly one signature shape per regime class.
5. **Thin-RFC discipline.** *It was never brittle if it never broke.*

---

## 1. Object

An **FDR signature** is the parametric-plot shape and universality-invariant tuple emitted per spec object (vertex / edge / subgraph) at a declared observer kernel. It is the cross-substrate identifier of regime class — what realizers measure to confirm a substrate hosts the canonical structure a spec requires.

## 2. Shape

```
S_FDR = (object_ref, regime_class, parametric_plot, universality_tuple, observer_kernel, measurement_envelope)
```

| Field | Content |
|---|---|
| `object_ref` | Vertex / edge / subgraph ID in the spec object (RFC-1) |
| `regime_class` | One of $\{c, s, r, k_{\text{frust}}\}$ |
| `parametric_plot` | Sampled curve $(\chi(\tau), C(0)-C(\tau))$ at declared resolution |
| `universality_tuple` | Per-regime invariants from v9 §Fluctuation-dissipation signatures (regime-conditional set; see Invariant 2) |
| `observer_kernel` | $\tau_{obs}$ at which the signature was measured |
| `measurement_envelope` | Subset of the driver's `operating_envelope` (RFC-S §4) covering this measurement |

Schema in [Appendix A](#appendix-a-schema).

## 3. Invariants

A signature is **valid** iff:

1. **Object-typed.** `object_ref` resolves to a typed object in a valid spec; `regime_class` matches the object's type (vertex regimes use $\{c, s, r\}$; subgraphs use $\{k_{\text{frust}}\}$).
2. **Universality-tuple completeness.** Tuple carries the regime-conditional invariants per [RFC-V §2](MPA-RFC-V_Reference-Vocabulary.md) (which inherits from v9 §Fluctuation-dissipation signatures).
3. **Within-class.** Measured invariants fall within the substrate-specific tolerance the driver profile declares.
4. **Observer-relativity.** Measured at the spec-declared $\tau_{obs}$; cross-band declarations are separate signatures.
5. **Envelope-respect.** `measurement_envelope` ⊆ driver's `operating_envelope`.
6. **Sampling adequacy.** `parametric_plot` sample density resolves the universality tuple to the declared precision.
7. **Domain.** $X_c, X_r \in [0, 1]$; $\alpha_s$ within Cugliandolo–Kurchan envelope; $P_s \in [0, 1]$; $N_f \in [-1, 0]$.

## 4. Operations

| Operation | Signature |
|---|---|
| Measure | $\text{spec} \times \text{driver} \to S_{\text{FDR}}[]$ — driver produces signatures from substrate-native data |
| Validate | $S_{\text{FDR}} \to \{\text{valid}, \text{diagnostics}[]\}$ — preserves §3 |
| Compare per intent | $S_{\text{FDR}}^A \times S_{\text{FDR}}^B \times \text{intent} \to \text{distance}$ — intent-specific metric (RFC-S §5) |
| Round-trip check | RFC-S §5 protocol (forward + round-trip thresholds against reference dataset) |

Operations are intent-neutral except *Compare*, which carries an intent declared at the comparison call.

## 5. Falsifiers

A signature is **invalid** if any of:

- Schema violation (Appendix A).
- `regime_class` / object-type mismatch.
- `universality_tuple` missing fields required by `regime_class`.
- Sampling below the resolution required for the declared precision.
- `measurement_envelope` outside the driver's `operating_envelope`.
- Domain violation per Invariant 7.

## 6. Pointer

| What | Where |
|---|---|
| Per-regime parametric shapes + universality-invariant table $\{X_c, \alpha_s, P_s, X_r, N_f\}$ | [v9 §Fluctuation-dissipation signatures](../framework/v9_compressed.md) |
| Substrate-conditional reading rules (Markovian sign, detection-event preprocessing) | v9 §Substrate-conditional reading rules |
| Surface-code load-bearing reference (Cugliandolo–Kurchan $s$-aging) | v9 §FDR (surface-code paragraph) + [`reference-drivers/surface-code-qec.md`](../reference-drivers/surface-code-qec.md) |
| Trail-class metric $\rho$ (used in I5 intra-class distance) | v9 §Compression Axiom |
| Per-intent comparison semantics | [RFC-S §3](MPA-RFC-S_Scale-Management.md) (intents) + §5 (round-trip metrics) |

---

## Appendix A: Schema

JSON Schema at [`schema/fdr-signature.v0.1.json`](../schema/fdr-signature.v0.1.json). §2 mirrors the schema's field structure as a reading aid.

```
fdr_signature = {
  object_ref: <vertex|edge|subgraph id>,
  regime_class: one_of(c, s, r, k_frust),
  parametric_plot: { samples: [{tau, chi, C0_minus_C}, ...] },
  universality_tuple: {
    X_c?: float,                  # if regime_class == c
    alpha_s?: float, P_s?: float, # if regime_class == s
    X_r?: float,                  # if regime_class == r
    N_f?: float                   # if regime_class == k_frust
  },
  observer_kernel: <tau_obs spec>,
  measurement_envelope: <RFC-S §4 operating_envelope subset>
}
```

## Appendix B: What this RFC does not specify (deferred)

- **Per-substrate measurement protocols** → driver profile (RFC-S §4) `operating_envelope` and `reference_outputs`.
- **Acceptance thresholds per intent** → driver profile, validated via RFC-S §5 round-trip.
- **Cross-substrate signature comparison at a meta level** → RFC-3 (consistency & completeness).
- **Multi-loop $k_{\text{frust}}$ signatures.** v9 carries the single-loop transient-negative shape ($N_f$); multi-loop / hyperedge frustration may have richer signatures. Open until a substrate instances them.

## Appendix C: Open

1. **Universality-class boundary.** Categorical agreement is the load-bearing test (RFC-S §5 I5); intra-class numerical bounds are substrate-specific. Cross-substrate boundary characterization is open — currently relies on driver-declared tolerance.
2. **$\alpha_s$ measurement form.** v9 §FDR specifies "slope of aging segment" without committing to log-log vs. linear (CK ratio reading). RFC-2 inherits the agnostic form; v0.2 may canonicalize once a second reference substrate (habit-extinction) provides comparison data.

---

## Versioning

| Version | Status | Change |
|---|---|---|
| **v0.1** | **current** | First thin-RFC pass. Universality tuple anchored on v9 §FDR per-regime invariants. |

**Compatibility.** Within v0.x: schema additions only. Removal of universality-tuple fields requires v1.0+ revision.

## Page-budget self-check

Target: ≤1 page (CLAUDE.md table for RFC-S/RFC-2/RFC-3/RFC-RI).

Body §0–§6 ≈ 50 lines. Appendices A–C ≈ 25 lines. Versioning + self-check ≈ 12 lines. **Total ≈ 1.5 pages — over target by ½ page.**

**Debt-marker.** §3 invariant 2 inline-enumeration debt closed by RFC-V v0.1 §2 (per-regime invariant labels canonicalized; inv. 2 collapsed to a single-line RFC-V reference). Remaining over-target is general universality-tuple machinery (Appendices, Pointer table, domain-bounds invariant 7) that is genuinely operational content for an FDR-signature reader; revisable in v0.2 if RFC-3 (consistency & completeness) absorbs the cross-RFC pointer surface.
