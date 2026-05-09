# Handoff: protocol tool

**Status:** Planning document for the protocol tool — software that operates on mpa-atlas artifacts.
**Audience:** A future Claude (or human) coming into this work cold.
**Companion:** All RFCs ([RFC-1](../rfcs/MPA-RFC-1_Spec-Object.md), [RFC-2](../rfcs/MPA-RFC-2_FDR-Signatures.md), [RFC-3](../rfcs/MPA-RFC-3_Consistency-Completeness.md), [RFC-S](../rfcs/MPA-RFC-S_Scale-Management.md), [RFC-V](../rfcs/MPA-RFC-V_Reference-Vocabulary.md), [RFC-RI](../rfcs/MPA-RFC-RI_Realizer-Interface.md)), [Architectural Block-In](MPA_Architectural_Block-In.md) (especially §3 DBS bidirectionality), [`reference-drivers/`](../reference-drivers/), [`schema/`](../schema/).

---

## Goal

Produce a tool that operates on the mpa-atlas protocol artifacts. The tool is the practical surface that mpa-character (the authoring environment) and substrate-implementation drivers (in `mpc-*` and `mpa-*`repos) compose against. It mechanizes what the RFCs declare: validation, compilation, round-trip checking, driver discovery, characterization-gap reporting.

## Where it lives

Probably a separate repo (`mpa-tool`, `mpa-cli`, or similar). Not inside mpa-atlas — mpa-atlas is the protocol repo; tool is downstream of protocol. Cross-repo dependency: tool reads schema files + RFC documents from mpa-atlas, plus driver profiles from `mpc-*` repos and reference drivers from mpa-atlas.

## What the tool does (components)

These can be built incrementally; each is independently useful.

### 1. Single-artifact validator

Takes one document (spec object, FDR signature, driver profile, R_doc) and validates against:
- The corresponding JSON Schema at [`schema/`](../schema/) (`spec-object.v0.2.json`, `fdr-signature.v0.1.json`, `driver-profile.v0.2.json`, `realizer-interface.v0.1.json`).
- The RFC's §3 invariants where they extend beyond schema (e.g., domain bounds, mechanical Theorem-9 check for spec objects per RFC-1 §4).

Output: valid / invalid + diagnostics naming the violated invariant.

### 2. Constellation validator

Takes a constellation `{spec, driver_profile, signatures, R_doc}` and runs:
- Per-artifact validation (§1) for each.
- [RFC-3 §3](../rfcs/MPA-RFC-3_Consistency-Completeness.md) C-rules (cross-artifact consistency: spec ⊆ driver gamut, intent compatibility, etc.).
- [RFC-3 §4](../rfcs/MPA-RFC-3_Consistency-Completeness.md) K-rules (cross-artifact completeness: signature_targets cover spec elements, etc.).

Output: valid constellation / invalid + named C# / K# diagnostics.

### 3. Compiler

`spec object × intent → R_doc` per [RFC-1 §4](../rfcs/MPA-RFC-1_Spec-Object.md) Compile operation + [RFC-RI](../rfcs/MPA-RFC-RI_Realizer-Interface.md). The compiler:
- Validates the spec object first.
- Projects the canonical representation through the intent's mapping operation per RFC-S §3 (e.g., scale-uniform under I1).
- Generates `signature_targets` per spec-object element, anchoring on the relevant driver profile's reference_outputs.
- Sets `acceptance` thresholds per RFC-S §5 metric.
- Emits the R_doc.

### 4. Round-trip checker

`R_doc × measured signatures → diagnostics`. Reads the substrate's actually-produced FDR signatures and compares against `R_doc.signature_targets` per the intent's metric (RFC-S §5). Outputs forward-error and round-trip-error per signature; flags any threshold violation.

### 5. Driver discoverer (DBS-backward)

Pointed at unknown / partially-known data: given some substrate-native data + optional metadata, iterate available driver profiles to find compatible ones. For each candidate driver:
- Check `gamut` envelope coverage.
- Check `operating_envelope` calibration prerequisites.
- Score match.

Returns: ranked list of candidate drivers + per-driver coverage summary.

### 6. Characterization-gap reporter (DBS-backward)

Pointed at data with no compatible driver: rather than failing generically, declare what would be needed.

- Scan v9 §Substrate-conditional reading rules + reference-drivers/ for the closest substrate class.
- Declare: which characterization fields are missing (no $D$-range estimate; no $\tau_{obs}$-range; no shear-profile envelope; etc.).
- Suggest: characterization protocol from the closest reference driver.

This is the **informed silence** the Block-In §3 DBS bidirectionality describes. The tool is the operational vehicle for the principle's backward direction.

### 7. Vocabulary checker

Reads any document and validates label use against [RFC-V](../rfcs/MPA-RFC-V_Reference-Vocabulary.md):
- Cross-cutting labels (RFC-V §2) must match canonical form.
- Per-domain labels (RFC-V §3) must match the authority pointer.
- Disambiguation rules (RFC-V §4) must be respected ($C$ vs $\mathcal{C}$, $\epsilon$ vs $\varepsilon_n$).

Lightweight; useful for CI on the mpa-atlas repo itself + downstream repos.

## Architecture notes

- **The tool does not encode v9's mathematical content.** v9 is the rigor source; the tool relies on driver profiles to bridge substrate-native to canonical. If you find yourself implementing operator algebra inside the tool, stop — that's a driver's job (or v9's, if it's truly substrate-neutral).
- **Mechanical-only validation.** RFC-3 §6 and Block-In §"Where the rigor actually lives" both say validation is mechanical, no human judgment. Every C# and K# rule is computable from artifact contents.
- **Modular.** Each component is independently invocable. The tool's UX could be a CLI subcommand per component, or a single workflow that composes them.
- **Schema-driven.** Use the JSON Schema files (when they ship) as the validator's source-of-truth. RFC content is operational reference; schemas are the machine-readable form.
- **Streaming-friendly.** For round-trip checking on real measurement data, avoid loading entire datasets into memory. Drivers' `operating_envelope.measurement_protocol` describes the data shape.

## What's out of scope

- **Substrate-specific realization.** Realizer search algorithms (find substrate parameters that produce the canonical structure) are substrate-specific; they live in `mpc-*` driver / realizer pairs, not in the tool.
- **Building drivers.** That's substrate-research work (per `handoff_habit-extinction_reference-driver.md` and similar).
- **Encoding v9's content.** v9 is the rigor source; the tool reads driver profiles, not v9 directly (except for substrate-conditional reading rules in §6 characterization-gap reports).
- **Authoring environments.** mpa-character is the authoring environment; the tool is the validator / compiler / checker, not the editor.

## Failure modes to watch

- **Encoding v9 in the tool.** The tool should read driver profiles, not implement substrate-conditional reading rules itself.
- **Building substrate-specific logic.** All substrate-specific logic lives in drivers. The tool is substrate-neutral by construction.
- **Failing on unknown data instead of declaring gaps gracefully.** DBS-backward (Block-In §3) is the discipline. Pointed at unknown data, the tool *characterizes the gap*, not just rejects.
- **Pretending to validate cross-artifact consistency without all artifacts.** RFC-3 needs a constellation. Single-artifact validation is §1; constellation validation is §2. Don't conflate.
- **Bloating beyond the seven components.** If you find yourself adding a new top-level component, ask which RFC it serves. If none, it's probably substrate-specific (driver) or authoring (mpa-character).
- **Silently using stale schemas / RFCs.** Tool should declare which RFC versions it targets; warn or fail on version mismatch.

## Completion criteria

The tool is "v0.1 complete" when:

- Components 1, 2, and 7 (single-artifact, constellation, vocabulary validation) work end-to-end against the existing mpa-atlas artifacts (RFC-1 v0.2 spec objects, RFC-2 v0.1 signatures, RFC-S v0.2 driver profiles, RFC-RI v0.1 R_docs, RFC-V v0.1 vocabulary).
- Components 3 and 4 (compile, round-trip) work against the surface-code reference driver: compile a spec for surface-code QEC, produce an R_doc, round-trip against the reference dataset.
- Components 5 and 6 (driver discovery, gap reporter) work against at least the surface-code reference driver as the only target; returns informative gap reports on data the driver doesn't cover.

The tool is "v0.2 ready" when habit-extinction reference driver lands and components 3–6 work cross-substrate (compile against either reference driver; gap-report references the closest substrate class).

## Effort estimate

Several days to weeks of software engineering, depending on language / framework choice and how much CI / testing scaffolding gets built. Components 1, 2, and 7 are the smallest (validation against schemas + simple predicates). Component 3 (compile) is the largest (intent-projection logic). Components 5 and 6 (DBS-backward) are research-flavored — they need substrate-class-taxonomy reading from v9 + reference-drivers/.

## Why this matters

Without the tool, the protocol is prose. With the tool, the protocol is checkable. Every claim a spec author or driver maker makes can be mechanically verified before compile / realize / round-trip. The tool is the place where thin-RFC discipline pays off — the protocols are thin because mechanical validation enforces what prose would otherwise enforce. Without the tool, that bet is unhedged.

## Related

- `handoff_v9_architectural-backport.md` — adds the foundational principles to v9's body. Independent; no coordination needed.
- `handoff_habit-extinction_reference-driver.md` — second reference driver. Tool can be v0.1 with one reference; v0.2 with two.
