# MPA-RFC-C: Calibration

**Status:** Draft v0.2 — first thin-RFC pass. (v0.1 standards-body draft superseded; preserved in commit history.)
**Targets:** [v9 (compressed, operational)](../framework/v9_compressed.md), [character (compressed, operational)](../framework/character_compressed.md). The chit unit `ln(G₀/L)` and the fraying sequence `c → s → k → r` are the load-bearing imports.
**Companion:** [Architectural Block-In v0.2](../architecture/MPA_Architectural_Block-In.md), [RFC-1 v0.2](MPA-RFC-1_Spec-Object.md), [RFC-S v0.2](MPA-RFC-S_Scale-Management.md), [RFC-2 v0.1](MPA-RFC-2_FDR-Signatures.md).

---

## 0. Foundational principles

This RFC inherits the five principles from the [Architectural Block-In](../architecture/MPA_Architectural_Block-In.md). Declared, not re-derived.

RFC-C adds one principle, internal to calibration:

6. **Calibration is a phase, not a mode.** A driver profile is *characterized* (RFC-S §4, one-time per substrate class) before runtime ever touches the substrate. **Calibration** verifies the substrate is in the declared envelope at experiment time and produces a sealed calibration record. Runtime consumes the record; substrate drift outside the calibrated envelope retires the record and triggers re-calibration. *MPA observables are not Boolean — they age, drift, and migrate; an uncalibrated substrate has no canonical reading at all.* This is the operational form of [RULES.md](../../mpa-central/RULES.md) rule 14 (RFC-S compliance prerequisite).

---

## 1. Object

A **calibration record** certifies that a substrate's current operating point lies inside its driver profile's `operating_envelope` (RFC-S §4) and supplies the measured values for the canonical primitives that runtime will assume. It is the per-experiment artifact that admits a substrate to RFC-S runtime.

## 2. Shape

```
R = (driver_profile_ref, measurements, validation, retirement_triggers, seal)
```

| Symbol | Name | Content |
|---|---|---|
| `driver_profile_ref` | Profile pointer | `(substrate_class, profile_version)` of the RFC-S §4 driver profile this record calibrates against |
| `measurements` | Primitive measurements | Per primitive `{L, G₀, τ_obs_canonical, γ_AB}`: measured value, uncertainty, and provenance pointer to the substrate-native SOP that produced it (cessation trace, drive-sweep extrapolation, kernel-sweep gFDR sweep, perturbation-response linearity check) |
| `validation` | Round-trip evidence | Forward and backward residuals on the driver profile's `reference_outputs` at this operating point, per RFC-S §5 |
| `retirement_triggers` | Drift bounds | Per-primitive thresholds whose violation retires the record, plus substrate-native drift-clock declarations |
| `seal` | Authority + immutability | `(calibration_authority, calibration_date, substrate_state_hash, profile_version_pinned)` |

Schema is canonical: a payload conforming to the schema is a valid calibration record by definition. Machine-readable schema in [Appendix A](#appendix-a-schema).

## 3. Invariants

A calibration record is **valid** iff all of:

1. **Profile binding.** `driver_profile_ref` resolves to a current RFC-S §4 driver profile; the substrate's measured operating point lies inside that profile's `operating_envelope`.
2. **Cessation-measured `L`.** Decay rate `L` is measured during *cessation* of holding, not inferred from active-holding observables (linewidth, steady-state cost, etc.). Cessation trace is a required provenance pointer.
3. **Extrapolated `G₀`.** Unsaturated maintenance budget `G₀` is the zero-coherence-amplitude extrapolation of the holding-cost vs. drive curve. `G_sat` (steady-state cost) is not admissible as `G₀`.
4. **Swept `τ_obs`.** Canonical `τ_obs_canonical` is selected from a parametric sweep that resolves regime structure (gFDR signature class transitions visible across the swept range), not chosen by literature convention or ritual.
5. **Perturbation-measured `γ`.** Cross-saturation coefficients `γ_AB` are measured from small perturbations on `A` while observing `B` in the linear-response regime (`ε / G₀ < 0.1`). Structural-graph topology is not admissible as a substitute.
6. **Threshold verification.** A drive sweep through `ln(G₀/L) → 0` aligns the substrate's regime transitions with the chit-predicted threshold within stated `δG₀/G₀`.
7. **Sealed and immutable.** Once `seal` is populated, the record is append-only; re-calibration produces a *successor* record with a new seal. Mutation in place is invalidating.

## 4. Operations

| Operation | Signature | Preserves |
|---|---|---|
| Validate | `R → {valid, diagnostics[]}` | Invariants 1–7 |
| Admit-to-runtime | `R × runtime → admitted | rejected` | Runtime consumes only validated records (RFC-S §5 round-trip pass) |
| Drift-check | `R × current_substrate_state → in-envelope | drifted` | Detects retirement-trigger violations; cheap to run continuously |
| Retire-and-supersede | `R × R' → ordered chain` | Provenance: `R` archived, `R'` active; chain is append-only |

A calibrated substrate is admitted to RFC-S runtime; a drifted substrate has its record retired and re-enters calibration. Operations are intent-neutral (intent declarations live at type-changing junctions per [RFC-S §3](MPA-RFC-S_Scale-Management.md#3-intents)).

## 5. Falsifiers

A calibration record is **invalid** if any of:

- Schema violation (Appendix A).
- `L` measured under active holding (linewidth, steady-state — Boolean-thinking failure).
- `G₀` reported as `G_sat` without zero-amplitude extrapolation evidence.
- `τ_obs_canonical` quoted from substrate literature without sweep evidence in the record.
- `γ_AB` derived from graph topology rather than perturbation response.
- Single-point `L` measurement (no cessation trace).
- Substrate operating point outside profile's `operating_envelope` at calibration time.
- Post-seal mutation of any field without superseding the record.

## 6. Pointer

[v9 (compressed)](../framework/v9_compressed.md) and [character (compressed)](../framework/character_compressed.md) carry the formal derivation:

| What | Where |
|---|---|
| Chit unit `ln(G₀/L)`; threshold semantics | character §"Chit unit"; v9 §Boolean section |
| Fraying sequence `c → s → k → r` under threshold descent | character §"Fraying sequence" |
| FDR signatures per regime; gFDR plot conventions | v9 §Fluctuation-dissipation signatures |
| Substrate-conditional reading rules (Markovian sign, EMA preprocessing) | v9 Appendix F |
| Heat-tax tower; vertical re-calibration cost | character §"Heat-tax tower" |
| RFC-S §4 driver profile (the artifact this record calibrates against) | [RFC-S v0.2 §4](MPA-RFC-S_Scale-Management.md#4-driver-profile) |
| RFC-S §5 round-trip validation (the protocol this record supplies evidence for) | [RFC-S v0.2 §5](MPA-RFC-S_Scale-Management.md#5-round-trip-validation) |

Substrate-class measurement protocols — *how* `L` is read on QEC syndromes, *how* `G₀` is extrapolated on a glass rheometer, *which* perturbation gives a clean `γ_AB` on a Langevin substrate — live in the substrate's reference driver under [`reference-drivers/`](../reference-drivers/). RFC-C governs the exchange contract; the substrate-native rituals are reference-driver content.

---

## Appendix A: Schema

Calibration-record schema is the canonical exchange shape. Machine-readable schema at [`schema/calibration-record.v0.1.json`](../schema/calibration-record.v0.1.json). §2 mirrors the schema's field structure as a reading aid.

```
measurements        = { L:                  { value, uncertainty, sop_ref, cessation_trace_ref },
                        G_0:                { value, uncertainty, sop_ref, extrapolation_evidence_ref },
                        tau_obs_canonical:  { value, valid_range, sop_ref, sweep_evidence_ref },
                        gamma_AB:           { (A,B): { value, uncertainty, sop_ref, linearity_evidence_ref } } }
validation          = { reference_dataset_ref, forward_residuals, backward_residuals,
                        per_intent_metric_pass: { I1?, I2?, I3?, I4?, I5? } }
retirement_triggers = { L_drift_max, G_0_drift_max, gamma_drift_max,
                        cessation_failure_rule, drive_excursion_rule, regime_drift_rule,
                        substrate_native_drift_clock_ref }
seal                = { calibration_authority, calibration_date,
                        substrate_state_hash, profile_version_pinned }
```

## Appendix B: Open

Items the next revision absorbs as needed:

1. **Field-kernel `γ`.** Pairwise `γ_AB` may not capture multi-mode competition on dense substrates. v0.2 admits pairwise; v0.3 may extend to N-mode field-kernel perturbation response if a substrate's measured response is non-pairwise.
2. **Multi-timescale `L`.** Some substrates have hierarchical relaxation (β + α modes in glasses, fast leakage + slow logical decay in QEC). v0.2 takes the slowest mode as canonical `L`; explicit hierarchy support deferred until a substrate demands it.
3. **Cross-substrate joint calibration.** Whether two substrates measured jointly admit a combined record (substrate-pair `γ_AB`) is open. v0.2 records are per-substrate.

## Appendix C: What this RFC does not specify

- **Native protocol design.** How to perform randomized benchmarking, how to fit Kohlrausch–Williams–Watts relaxation, how to set DMA geometry — substrate-native disciplines. RFC-C consumes their outputs via `sop_ref`.
- **Instrument-level calibration.** Zero-gap compensation, qubit spectroscopy baseline, thermal expansion correction — SOP-layer concerns, assumed valid by RFC-C.
- **Substrate-class translation rules.** The per-primitive measurement procedures for QEC, glass, Langevin, etc. live in reference drivers ([`reference-drivers/surface-code-qec.md`](../reference-drivers/surface-code-qec.md), [`reference-drivers/structural-glass.md`](../reference-drivers/structural-glass.md), …).

---

## Versioning

| Version | Status | Change |
|---|---|---|
| v0.1 | superseded | Standards-body shape (~270 lines, six universal phases prescribed as a procedural script). |
| **v0.2** | **current** | Thin-pass rewrite under [thin-RFC discipline](../CLAUDE.md). Six-field template. The protocol object is now the calibration record (was implicit in v0.1's "Phase 6 handoff"). Substrate-class translation tables moved to `reference-drivers/`. |

**Compatibility.** Within v0.x: schema additions only. Removal of an invariant or change to retirement-trigger semantics requires v1.0+ revision. Calibration records declare which RFC-C version they target.

## Page-budget self-check

Target: ≤1 page for the calibration record (non-foundational object; per [CLAUDE.md](../CLAUDE.md) RFC discipline).

Body §0–§6 ≈ 1¼ pages; appendices A–C ≈ ¾ page; versioning + self-check ≈ ¼ page. **Total ≈ 2¼ pages. Within tolerance** — the seven invariants (matching RFC-1's foundational ceiling) plus the chit / fraying-tower references in §6 push slightly past the strict ½-page-per-object target. No debt-marker yet; if subsequent revisions shrink, the record is a candidate for the ½-page bracket.
