# MPA-RFC-S: Scale Management

**Status:** Draft v0.2 — first thin-RFC pass. (v0.1 preserved at [`MPA-RFC-S_Scale-Management_Block-In.md`](MPA-RFC-S_Scale-Management_Block-In.md) as honest-scope reference; not authoritative.)
**Targets:** [v9 (compressed, operational)](../framework/v9_compressed.md). Compression Axiom + operator algebra are the load-bearing imports.
**Companion:** [Architectural Block-In v0.2](../architecture/MPA_Architectural_Block-In.md), [RFC-1 v0.2](MPA-RFC-1_Spec-Object.md), [RFC-2 v0.1](MPA-RFC-2_FDR-Signatures.md), [RFC-RI v0.1](MPA-RFC-RI_Realizer-Interface.md)

---

## 0. Foundational principles

This RFC inherits five principles from the [Architectural Block-In](../architecture/MPA_Architectural_Block-In.md), declared (not re-derived):

1. **Color-management discipline.** Three layers (substrate-native / canonical / realizer-output); transforms declared, named, versioned, swappable.
2. **Observer-driven scale management.** $\tau_{obs}$ is the camera; canonical representation is observer-relative.
3. **Demand-bounded sufficiency.** Canonical representation sized to declared demand. **The MPA is not the bottleneck.**
4. **Singular working-space path.** Within an RFC version, exactly one shape. Plurality lives in drivers, intent flags, and version succession.
5. **Thin-RFC discipline.** *It was never brittle if it never broke.*

RFC-S adds one principle, internal to scale management:

6. **RG flow as foundational structure.** Scale-management semantics derive from the renormalization-group flow defined by v9's Compression Axiom (Wilson–Kadanoff + Banach contraction at $\epsilon < 1$). The canonical representation, substrate gamut, intent operations, and behavior at boundary points are *positions in or trajectories under this flow*, not finite-engineering analogs reconstructed from color management. Color management is a finite discipline; MPA scale management is infinite. Infinity-machinery is imported directly, not patched on case-by-case.

---

## 1. Canonical representation (at observer position $p$)

The canonical representation at $p = \tau_{obs}$ is **the fixed-point set of the Compression Axiom's RG flow** at level $n$, restricted to the substrate's reachable trajectory.

| Object | Reading under RG flow |
|---|---|
| Vertex regime $\{c, s, r\}$ | Fixed-point structure: $c$ and $r$ stable; $s$ metastable. |
| Edge $\gamma$ sign | Cooperativity class; preserved at fixed $\tau_{obs}$. |
| Subgraph $k_{\text{frust}}$ | RG-invariant on substrates carrying it; topological. |
| Trail-class equivalence | Equivalence classes under the flow; cardinality $\tau_{obs}$-dependent. |

Cross-position structure (auto-remap as $\tau_{obs}$ moves) **is the flow trajectory itself**; the driver supplies the rule that realizes it (form open — see Appendix B). Specifying the canonical representation at one $p$ plus the contraction $\mathcal{C}_n$ specifies it everywhere along the trajectory.

**Pointer:** v9 §Compression Axiom; §Three typed objects; §Boolean section.

---

## 2. Substrate gamut

A substrate's gamut is **the image of its RG trajectory** in canonical-representation space, parametrized by $(\tau_{obs}, D)$ — the locus the substrate's flow can traverse. Characterized by trajectory shape, not by multi-dimensional region enumeration.

| Axis | Substrate-declared content |
|---|---|
| $D$-range | $[D_{\min}(p), D_{\max}(p)]$ at each $p$, from the substrate's $(\Phi^*, \kappa)$ envelope. |
| $\tau_{obs}$-range | $\Pi(S)$, observer positions yielding valid canonical readings. |
| Persistence depth | $N(S)$, maximum measurable ascent before $\epsilon \to 1$ or signal floors. |
| Reachable trail-class structure | Which fixed-point patterns the trajectory visits. |

A spec is **in-gamut** at operating $(\tau_{obs}, D)$ iff its $(V, E, \Gamma, D, \tau_{obs}, P)$ corresponds to points along the substrate's trajectory. Out-of-gamut handling is intent-determined (§3).

**Pointer:** v9 §Setting; §Capacity; §Falloff profile; Appendix G (Convergent Tower).

---

## 3. Intents

Five intents enumerate which canonical-representation invariants are preserved when a spec is out-of-gamut. **The intent determines the mapping operation**: scale uniformly along the gamut to fit, preserving the named invariant. (Rule, not per-intent operation table.)

| # | Name | Preserves | Sacrifices | Color analog |
|---|---|---|---|---|
| I1 | Regime-preserving | Vertex regime partition; edge-type partition; $k_{\text{frust}}$; persistence-profile shape | Absolute $D$, $\gamma$, $\lambda$ | Perceptual |
| I2 | Drive-faithful | Exact $D$, $\gamma$, $\lambda$ on in-gamut content | Completeness (out-of-gamut rejected, diagnostic-listed) | Absolute colorimetric |
| I3 | Capacity-preserving | $\|\Gamma^*\|$ and structural pattern of sustainable subgraphs | Absolute drive level; non-sustained regime relationships | Saturation |
| I4 | Persistence-preserving | $\{\varepsilon_n\}$ shape; $\{S_n\}$ survival declarations; contraction ordering | Absolute drives; single-position regime relationships | (none — MPA-unique) |
| I5 | Signature-preserving | FDR-signature universality class (per regime / subgraph) | Exact signature parameters | Relative colorimetric |

**Where intents are declared.** At type-changing junctions (driver, auto-remap, realizer). Operator actions ($C, S, K, R$) inside canonical space are intent-neutral by construction — they preserve canonical-representation invariants because the algebra is closed (RG-flow associativity).

**Composition.** Two adjacent intents compose iff their preserved-invariant sets union without conflict. I2 (drive-faithful) does not compose with adjusting intents. Composition algebra beyond this rule is deferred (Appendix B).

**Pointer:** v9 §Operators; §Fluctuation-dissipation signatures (I5 universality classes); Appendix F (substrate-conditional reading).

---

## 4. Driver profile

The artifact a driver produces. Field enumeration here; machine-readable schema in [Appendix A](#appendix-a-schema). Operating envelope is folded in as a driver-profile section, not its own RFC section.

| Section | Content |
|---|---|
| `header` | profile_version, target_rfc_versions, substrate_class, characterization_date, authority, validation_history |
| `operating_envelope` | initial_conditions, parameter_ranges, measurement_protocol — what calibration must verify |
| `gamut` | $D$-range; observer-range $\Pi(S)$; shear-profile envelope; trail-class support; persistence depth $N(S)$; contraction-rate fit |
| `translation_field` | substrate-to-canonical and canonical-to-substrate maps, parametrized by $\tau_{obs}$; auto-remap rule (form open — Appendix B) |
| `intents` | per-intent: supported (bool); gamut-mapping operation; sacrifice declaration; use cases |
| `reference_outputs` | canonical test inputs with expected substrate responses + tolerance, for round-trip validation |
| `metadata` | methodology; known limitations; versioning history |

**Characterization vs. calibration.** Characterization produces the driver profile (one-time per substrate class). Calibration verifies the substrate is in the declared `operating_envelope` (per-experiment). A characterized-but-uncalibrated substrate has a profile that cannot be trusted on the current measurement; a calibrated-but-uncharacterized substrate has no profile at all.

**Pointer:** v9 §Substrate-conditional reading rules; Architectural Block-In §"What this means for drivers."

---

## 5. Round-trip validation

A driver is accepted iff forward and round-trip errors fall below intent-specific thresholds on every reference dataset the driver claims to support.

**Protocol:**

1. **Reference.** Canonical reference dataset for the substrate class. (Surface-code QEC and habit-extinction are the proposed first two; see Architectural Block-In §"Reference substrates.")
2. **Forward.** Driver under test produces canonical representation from reference substrate-native data.
3. **Forward comparison.** Driver output vs. known-correct canonical representation, intent-specific metric.
4. **Backward.** Reference realizer applied to driver's canonical output, producing predicted substrate-native data.
5. **Round-trip comparison.** Predicted vs. original substrate-native data, intent-specific metric.
6. **Acceptance.** Forward and round-trip errors both below thresholds, for every supported intent / dataset.

**Per-intent metric (forward and round-trip share the metric):**

| Intent | Metric |
|---|---|
| I1 regime-preserving | Hamming distance on regime partition; agreement on edge-type partition |
| I2 drive-faithful | $L^2$ on drive vector; $\max$ deviation on $\gamma$ |
| I3 capacity-preserving | $\|\Gamma^*\|$ deviation; structural-pattern similarity (graph-isomorphism family) |
| I4 persistence-preserving | Sequence distance on $\{\varepsilon_n\}$; survival-declaration agreement |
| I5 signature-preserving | Universality-class agreement; intra-class parameter distance |

**Reference-substrate bootstrap.** First reference per substrate domain is hand-built from v9 by-hand reading (v9 §5 + Appendix F for surface-code QEC). Subsequent drivers are validated against it. Multi-driver agreement supersedes single-reference validation once multiple drivers exist.

**Pointer:** v9 §5 (surface-code identification); Appendix F (substrate-conditional reading); [RFC-2 v0.1](MPA-RFC-2_FDR-Signatures.md) canonicalizes I5 metrics.

---

## 6. Behavior at compactification points

Boundary parameter values are *points in the compactified parameter space*, not separate edge cases per intent. Behavior is specified once per point; the intent's preserved invariant fixes its action at the point.

| Point | Physical reading | Default policy |
|---|---|---|
| $\epsilon \to 1$ | Complexity Wall (v9 Appendix G). Tower fails to converge; further ascent thermodynamically forbidden. | Spec must declare wall-acceptance (terminal level) or fail. I4 extrapolates with growing $\sigma_n$; others reject. |
| $D \to \infty$ | Boolean limit. Canonical representation collapses to $\mathcal{M}_2 \cong \mathbb{B}$. | Specs reduce to classical propositional logic; full operator algebra unnecessary. Recommend Boolean export. |
| $D = 0$ | No drive. Only $\mathcal{M}_2$ subset admissible (no $s$-regime). | Reject specs with $s$-regime vertices at $D = 0$. |
| $\tau_{obs} \to 0$ | Microscopic limit. Substrate-native granularity dominates; $\Pi(S)$ floor governs. | Below the driver's stated floor, the driver is invalid. |
| $\tau_{obs} \to \infty$ | Fully coarse-grained. All structure migrates to $r$. | Spec's persistence profile must terminate; else flag as exceeding $N(S)$. |
| $\lambda = \pm D$ | Regime-transition boundary. Reading ambiguous within transition zone of substrate-characterized width $\delta$. | Zone reading undefined. I1 widens to next category; I2 reports ambiguous; substrate declares $\delta$ in its driver profile. |
| $\gamma_{AB} > 0 \wedge D < \gamma_{AB}$ | Theorem-9 boundary. Joint commitment infeasible. | RFC-1 mechanical check flags. Intent-determined: I2 hard-flags, I1 scales, I3 redistributes $\gamma$. |

**Pointer:** v9 Theorem 9 (joint-commitment threshold); Appendix G (Convergent Tower / Complexity Wall); §Boolean section.

---

## Appendix A: Schema

Driver-profile schema is the canonical exchange shape. Machine-readable schema at [`schema/driver-profile.v0.2.json`](../schema/driver-profile.v0.2.json). §4 mirrors the schema's field structure as a reading aid; v0.1's YAML sketch (v0.1 §6) remains a non-authoritative reference.

## Appendix B: Open

Items the next revision absorbs as needed:

1. **Auto-remap form: function vs. generator.** v0.1 specifies auto-remap as a finite remap function. RG-thinking suggests the *infinitesimal* (tangent-flow) form: drivers specify the rule for small $\tau_{obs}$ changes; finite remaps are integrated. Open whether all substrate classes admit clean infinitesimal rules and whether integration is tractable. v0.2 admits both forms; v0.3 may canonicalize.
2. **Intent composition algebra past the union rule.** §3 declares "union of preserved invariants without conflict." Whether this rule covers all admissible compositions is unverified at v0.2. If v0.3 needs a small composition table, that is the place a debt-marker would land — and the place sheaves (handoff Tier 3) might earn their weight.
3. **Lower-bound $\varepsilon_n$.** $\varepsilon = 0$ is non-physical (information must be lost across real-scale coarse-graining). Substrate-specific $\varepsilon_n^{\min}$ declared in driver profile; form of declaration open.
4. **Observable sufficiency in round-trip validation.** §5 assumes the backward map is invertible enough to validate; §4's `reference_outputs` are the inputs that drive it. Neither states *which observables jointly constrain which canonical-representation axes*. Concrete force: an inversion against a single-mode gFDR locus constrains the vertex regime but is rank-deficient on the edge $\gamma$ — the round-trip would pass while leaving an axis untouched. v0.3 should add an observable-coverage obligation: a driver's `reference_outputs` must jointly constrain every canonical axis it claims to support. (Surfaced by the mpa-auditor mock-dataset slice; see that repo's `docs/rfc-s-integration-notes.md`.)

(Trail-class metric and per-regime universality invariants closed in v9 between v0.2 and the next RFC-S revision: $\rho$ in §Compression Axiom, $\{X_c, \alpha_s, P_s, X_r, N_f\}$ in §Fluctuation-dissipation signatures. RFC-S §3 I5's intra-class metric and §5 round-trip per-intent metrics now reference these directly; v0.3 will tighten the §3 / §5 wording to point at the v9 invariants by name.)

## Appendix C: What this RFC does not specify (deferred)

- **Behavioral / evolving substrates.** Substrates whose operating envelope evolves during measurement (training neural networks, evolving biological systems) do not admit a static driver profile. Out of scope. Future RFC-Beh or extension axis.
- **Sheaf-theoretic pipeline composition.** Tier-3 import (handoff §"Infinity-machinery available, ranked by fit"). Not earning weight at v0.2; reserve for v0.3 if §3's union rule proves insufficient.
- **Coalgebraic trail-class equivalence.** Reserve for when v9's open trail-class metric question becomes blocking.
- **Reference-target standardization governance.** Who declares which substrates are reference targets, on what criteria — operational, not protocol-layer.

---

## Versioning

| Version | Status | Change |
|---|---|---|
| v0.1 (Block-In) | preserved as honest-scope reference | Standards-body weight; ~5,800 words; 170–200-page projection. |
| **v0.2** | **current** | Thin-pass rewrite. RG flow as foundational structure (§0 principle 6). Six body sections at half-page weight. Edge cases collapsed under compactification. |

**Compatibility.** Within v0.x: schema additions only. Removal of intents or change to compactification-point semantics requires v1.0+ revision. Drivers declare which RFC-S version they target.

## Page-budget self-check

Target: ≤5 pages including appendices (handoff §"What success looks like").

Body §0–§6 ≈ 3 pages; appendices A–C ≈ ½ page; versioning + self-check ≈ ¼ page. **Total ≈ 4 pages. Pass.**

For comparison: v0.1 ran ~620 lines of body and projected 170–200 pages at full ICC-v4-comparable resolution. The thin pass collapses 13 v0.1 sections to 6 active sections + 3 appendices. Compression mechanisms: RG flow + Banach contraction handle infinite coarse-graining as a single import (§0.6); compactification handles boundary behavior as points-in-space (§6); the five-intent table (§3) and round-trip protocol (§5) are preserved at full weight as the load-bearing exchange artifacts.

**Debt-markers.** None at v0.2. Pipeline composition — the handoff's flagged candidate to break the budget — was held to §3's intent-composition union rule plus deferral in Appendix C. If that rule proves insufficient against actual stress, v0.3 will carry a debt-marker naming the break and may import sheaves.
