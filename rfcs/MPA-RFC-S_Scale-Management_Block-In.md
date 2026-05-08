# MPA-RFC-S: Scale Management Specification (Block-In)

**Status:** Block-in v0.1
**Purpose:** Enumerate, at sufficient resolution to evaluate scope, the infrastructure required to actually port color-management discipline into MPA — rather than gesturing at it.
**Companion:** Architectural Block-In v0.1; RFC-1 draft 0.1

---

## 0. What this document is, and what it confronts

The Architectural Block-In declared "observer-driven scale management" as a foundational principle and used color management as the analog. This document confronts what that actually requires.

Color management is not a discipline. It is an infrastructure stack assembled over forty years by working scientists and standards bodies. The ICC v4 specification is ~120 pages of formal definitions, supplemented by hundreds of pages of related documentation (gamut mapping research, characterization protocols, pipeline composition rules). To port it to MPA means producing analogs for *each* of its infrastructural components, not adopting its vocabulary.

This document is a block-in: every component of the stack is enumerated, with a real proposal at low resolution where one exists, and explicit acknowledgment where the work is harder than that. Some sections will look more developed than others; that's accurate, not an artifact of fatigue. The final section gives an honest scope estimate.

The point is to let the work be evaluated, not approved.

---

## 1. The Connection Space

In ICC, the Profile Connection Space (PCS) — CIE XYZ or LAB — is the device-independent interchange medium. Every transform passes through it. ICC profiles aren't direct device-to-device transforms; they're profiles *to and from PCS*. This is what makes the system composable.

For MPA, the connection space is the canonical representation specified by RFC-1, with the additional commitment that it serves as the universal interchange medium between input transforms (drivers) and output transforms (realizers).

### 1.1 Connection space invariants

A connection space is defined not just by its content but by its *invariants* — the quantities that all admissible transforms preserve. For MPA, the proposed invariants at each observer position are:

- **Vertex regime partition.** The function $\rho_p: V \to \{c, s, r\}$ at observer position $p$. Any default-admissible transform $T$ preserves this: $\rho_p(T(v)) = \rho_p(v)$ for all $v \in V$.
- **Edge type partition.** The function $\eta_p: E \to \{\text{coop}, \text{ortho}, \text{conflict}\}$ at observer position $p$, induced by $\text{sign}(\gamma_{AB})$. Preserved structurally.
- **Topological invariants.** $k_{\text{frust}}$ on declared subgraphs. Preserved exactly (it is a topological invariant of the coupling graph per v9).
- **Trail-class equivalence relation.** The equivalence classes under the meta-ledger flow at level $n$. Preserved as a partition: $T(\sim_A) \subseteq \sim_B$.

A transform that preserves these is admissible without intent declaration. A transform that violates any of them is admissible only when an intent is declared that authorizes the violation.

### 1.2 Layered connection-space structure

Because the canonical representation is observer-relative (per the Architectural Block-In), the connection space is layered:

- *At each observer position $p$,* a graph with regime/type/$k_{\text{frust}}$/equivalence structure.
- *Across observer positions,* the auto-remap structure carrying the canonical representation from one position to another.

Both layers have invariants. Single-position transforms preserve the position's local invariants. Cross-position transforms (auto-remaps) preserve the trajectory invariants — which include the persistence profile structure and the contraction ordering.

### 1.3 Open

Whether the proposed invariant set is complete is itself a design question. In particular: should the *capacity envelope* $|\Gamma^*| \leq \sqrt{2D/\alpha\gamma_{\min}d_{\text{avg}}}$ be a connection-space invariant or a gamut-level constraint? Argument for invariant: it's a structural property of canonical representations. Argument against: it depends on $D$, which is a varying parameter rather than a structural feature. Open.

### 1.4 What's settled vs. open here

Settled: the connection space is layered, observer-relative, has declared invariants. Open: the precise invariant set, especially capacity envelope's status. **Confidence: medium-high on shape, medium on specifics.**

---

## 2. Gamut

For a substrate class $S$, the gamut $G(S)$ is the reachable region of canonical-representation configurations the substrate can physically produce or sustain. It is the analog of a device's color gamut.

### 2.1 Gamut as a multi-dimensional region

$G(S)$ lives in:

- **Drive space:** $[D_{\min}(S, p), D_{\max}(S, p)]$ at each observer position $p$.
- **Observer space:** the range of observer positions $\Pi(S)$ at which the substrate yields valid measurements.
- **Shear-profile space:** which $\gamma$-distributions are physically realizable. This is a region in the space of functions $E \to \mathbb{R}$, constrained by the substrate's microstructure.
- **Trail-class hosting space:** which canonical structures the substrate can sustain. A categorical constraint — some substrates can't host certain trail-class structures regardless of drive.
- **Persistence-tower depth:** $N(S)$, the maximum measurable ascent level.

So $G(S) \subseteq \mathbb{R}^{|\Pi(S)|} \times \Pi(S) \times \Sigma_\gamma(S) \times \Sigma_{\text{trail}}(S) \times \mathbb{N}$ — a complicated region, generally not convex, with substrate-specific topology.

### 2.2 Gamut characterization protocol

To characterize $G(S)$ for a substrate class:

1. Sweep drive across achievable range at multiple observer positions; record valid measurements.
2. Sweep observer position across substrate's accessible range; identify $\Pi(S)$.
3. Vary substrate parameters that map to $\gamma$; characterize $\Sigma_\gamma(S)$.
4. Apply observable coarse-graining at successive ascent levels; determine $N(S)$.
5. Identify trail-class hosting capabilities by attempting canonical representations of varying structure.

The gamut $G(S)$ is the (appropriately defined) hull of measured reachable points, with boundary behavior characterized at each face.

### 2.3 In-gamut tests

Given a spec $\Sigma$ and a substrate gamut $G(S)$:

- *Component-wise test:* every component of $\Sigma$ is in the corresponding factor of $G(S)$.
- *Joint test:* $\Sigma$ as a whole lies in $G(S)$ (component-wise + interaction effects).

A spec passing component-wise but failing jointly is "marginally out-of-gamut" — each requested feature is achievable individually, but the substrate cannot sustain them simultaneously. This is a real failure mode and intent must declare handling.

### 2.4 What's settled vs. open here

Settled: gamut is multi-dimensional, characterization is multi-sweep, in-gamut testing has component-wise and joint forms. Open: the actual hull structure (convex? simply-connected? wildly non-convex?) is substrate-specific and probably can't be assumed in general; the characterization protocol's depth depends on substrate type. **Confidence: high on structure, medium on practical characterization.**

---

## 3. Rendering Intents

This is the section that exposes most directly whether the color-management infrastructure ports.

In ICC, four standard intents — perceptual, relative colorimetric, absolute colorimetric, saturation — each preserve a different invariant when content is out-of-gamut. Each has a precise mathematical definition.

For MPA, the proposed intent family has five members. The fifth is unique to MPA because the persistence profile is a structural axis color management lacks.

### 3.1 Intent-1: Regime-Preserving (analog: perceptual)

**Preserves:** vertex regime partition, edge type partition, topological invariants ($k_{\text{frust}}$), persistence-profile shape.
**Sacrifices:** absolute drive values, absolute $\gamma$ values, absolute $\lambda$ values.
**Operation:** when out-of-gamut on drive: find scaling factor $s \in (0, 1]$ such that $s \cdot \Sigma$ lies in $G(S)$ on all components. Apply uniformly: all drives scaled by $s$, all $\gamma$ values scaled by $s$, $\lambda$ values scaled accordingly. Regime structure preserved by construction (scaling preserves $\text{sign}(\lambda + D)$ and $\text{sign}(D - \lambda)$).
**Use case:** the spec author cares about *what kind of structure exists* rather than absolute parameter values. Most artistic/exploratory work falls here.

### 3.2 Intent-2: Drive-Faithful (analog: absolute colorimetric)

**Preserves:** exact $D$ values, exact $\gamma$ values, exact $\lambda$ values for in-gamut content.
**Sacrifices:** completeness — out-of-gamut content is rejected or hard-clipped, with explicit reporting.
**Operation:** $T(\Sigma) = \Sigma \cap G(S)$. If $\Sigma \not\subseteq G(S)$, the result is a partial spec with explicit out-of-gamut declaration on each excluded component. No silent adjustments.
**Use case:** comparing measurements across substrates at fixed parameters; substrate validation; absolute calibration work.

### 3.3 Intent-3: Capacity-Preserving (analog: saturation)

**Preserves:** $|\Gamma^*|$ size and pattern of sustainable subgraphs.
**Sacrifices:** absolute drive level, regime relationships at non-sustained subgraphs.
**Operation:** when spec's sustainable subgraph exceeds substrate capacity, apply density-reduction operation: uniformly thin edge structure (or apply appropriate pattern-preserving reduction) until capacity envelope is satisfied. Preserves "vividness" of structural pattern at the cost of completeness.
**Use case:** rich-structure substrates where the structural pattern is the artifact of interest; comparison studies of substrates with different capacities at matched structural pattern.

### 3.4 Intent-4: Persistence-Preserving (no color analog)

**Preserves:** the persistence profile shape — the sequence $\{\varepsilon_n\}$ pattern, the survival declarations $\{S_n\}$, the contraction ordering.
**Sacrifices:** absolute drives, regime relationships at any single observer position, $\gamma$ specifics.
**Operation:** when spec requests persistence to depth $N$ exceeding substrate's measurable depth $N(S)$:
- For $n \leq N(S)$: use measured $\varepsilon_n$.
- For $N(S) < n \leq N$: extrapolate $\varepsilon_n$ from observed contraction trajectory, with explicit uncertainty bound $\sigma_n$ that grows with $n - N(S)$.
- Survival declarations $S_n$ at extrapolated levels are flagged "unverified."

When other components exceed gamut, those are scaled to maintain persistence-profile shape rather than absolute values.
**Use case:** multi-scale studies where the cross-scale structure is the artifact of interest; theoretical analyses where the tower's shape matters more than its absolute parameters; cross-substrate comparison at matched persistence profiles.

This intent is unique to MPA. Color management has nothing analogous because the persistence profile has no color analog.

### 3.5 Intent-5: Signature-Preserving (analog: relative colorimetric)

**Preserves:** FDR signature shape — qualitative curve type (unit-slope, aging diagonal, suppressed locus, transient negative response) at each spec element.
**Sacrifices:** exact signature parameters (slopes, plateaus, decay rates).
**Operation:** when exact requested signature isn't realizable, find substrate-realizable signature with same qualitative category. Requires a similarity metric on signature curves; provisional definition: signatures are equivalent if they share Cugliandolo–Kurchan universality class (specifics deferred to RFC-2).
**Use case:** dynamical-class studies; substrate identification work where the question is which universality class the substrate sits in rather than its specific parameters.

### 3.6 Intent composition

Whether intents compose is open. In color, the four standard intents are alternatives — you pick one for a given transform. In MPA, the five intents have different scopes and might compose:

- "Regime-preserving + capacity-preserving" — preserve both regime relationships and capacity, sacrificing only absolute drives. Possibly coherent if the substrate's gamut admits it.
- "Persistence-preserving + signature-preserving" — preserve both the multi-scale structure and the dynamical class. Possibly coherent in a narrower domain.
- "Drive-faithful + anything else" — incoherent; drive-faithful refuses to adjust, so it can't compose with intents that adjust.

A composition algebra for MPA intents is RFC-S-detail level work. Block-in proposal: composition is admissible iff the composed intents preserve a non-conflicting union of invariants. Specifics deferred.

### 3.7 What's settled vs. open here

Settled: the five-intent family covers the natural axes (regime, drive, capacity, persistence, signature). Open: composition rules; whether five is exactly right or whether a finer enumeration emerges; the similarity metric for signature-preserving intent. **Confidence: high that the family covers the right axes; medium on whether five is the canonical count.**

---

## 4. Gamut Mapping Operations

For each intent, the actual mathematical operation when content is out-of-gamut. Block-in proposals:

### 4.1 Regime-preserving mapping

For drive out-of-gamut: scaling factor $s = \min_p \frac{D_{\max}(S, p)}{D_{\text{requested}}(p)}$, applied uniformly. For multi-component out-of-gamut: $s$ is the binding constraint across all components. For shear-profile out-of-gamut: scale $\gamma$-profile to fit envelope, preserving sign structure.

Edge cases: if the binding constraint differs across observer positions (substrate has different $D_{\max}$ at different $p$), the scaling factor varies with observer — yielding a non-uniform scaling that requires care to maintain regime-partition consistency under auto-remap. This is a real complication.

### 4.2 Drive-faithful mapping

Hard rejection on out-of-gamut: $T(\Sigma) = \Sigma$ if $\Sigma \subseteq G(S)$, else reject with full diagnostic listing every out-of-gamut component. No partial result by default. Optional partial-result mode returns $\Sigma \cap G(S)$ with explicit "reduced spec" labeling.

### 4.3 Capacity-preserving mapping

When $|\Gamma^*_{\text{requested}}| > |\Gamma^*_{\text{achievable}}|$: apply pattern-preserving density reduction. Block-in proposal: identify the sparsest representative of the requested structural pattern (lowest edge density that retains topological character) and use that. Implementation requires defining "pattern representative" precisely — open.

For shear-profile-based capacity violations: redistribute $\gamma$ to reduce $\gamma_{\min}$ (the binding term in the capacity formula) while preserving relative shear ratios.

### 4.4 Persistence-preserving mapping

For $n > N(S)$: extrapolation using a parametric model fit to observed $\{\varepsilon_n\}_{n=0}^{N(S)}$. Block-in proposal: fit log-linear model $\log \varepsilon_n = a + bn$ to observed contraction sequence; extrapolate forward with confidence interval. Alternative models (geometric, power-law) may fit some substrates better — open question whether RFC-S commits to one model or admits a family.

Survival declarations at extrapolated levels: flagged unverified, with uncertainty quantified.

### 4.5 Signature-preserving mapping

When exact signature not realizable: find nearest realizable signature in same universality class. Requires similarity metric on signature curves; provisional definition uses category labels (aging-diagonal, unit-slope, etc.) as the primary partition, with intra-category distance defined by curve-fitting parameters.

### 4.6 What's settled vs. open here

Settled: each intent has a specifiable operation. Open: several specific mathematical questions (extrapolation model family, capacity-pattern representative, signature similarity metric) are open at RFC-S-detail level. **Confidence: high on operations existing; medium on canonical mathematical forms.**

---

## 5. Characterization vs. Calibration

In color, this is a crisp distinction. Characterization is *what the device does* (the ICC profile). Calibration is *getting the device into a known reference state* (so the profile remains valid). Both are required; they're separate operations performed at different cadences.

For MPA, the analogs:

### 5.1 Characterization

Building the driver. Producing the artifact that specifies how substrate-native data maps to canonical representation across the substrate's full operating envelope. One-time research effort per substrate class. Output: a driver profile (§6).

### 5.2 Calibration

Ensuring the substrate is in the operating regime where the characterization holds. Per-experiment procedural step. Output: substrate state confirmation, plus go/no-go for driver applicability.

What MPA calibration involves:

- *Initial state verification* — substrate's starting configuration matches characterization assumptions.
- *Operating parameter confirmation* — temperature, drive history, prior trajectory through observer-space match characterized envelope.
- *Measurement protocol verification* — sampling rate, kernel width, integration window match characterization assumptions.

### 5.3 The crisp distinction

A substrate that is *characterized but not calibrated* has a driver but the driver cannot be trusted on the current measurement (substrate is in wrong operating regime). A substrate that is *calibrated but not characterized* is in a known state but no driver exists — the canonical representation cannot be produced.

This distinction matters because it tells you what kind of work is needed at different times. Characterization is a research effort; calibration is procedural.

### 5.4 Where this distinction strains

For physical substrates (QEC, glass), calibration is operationally similar to color — set the substrate to known external conditions, verify, proceed. For behavioral substrates (habit extinction), "operating conditions" are fuzzier: subject's prior conditioning history, stress state, time-of-day effects. Calibration here is closer to "matched sample" methodology in behavioral science, and the analog is real but messier.

For substrates that are themselves products of training or evolution (neural networks during training, evolved biological systems), the very concept of "calibration" needs reformulation. The substrate's "operating regime" *changes during use*. This is an open problem and may require an extension of the framework.

### 5.5 What's settled vs. open here

Settled: the distinction maps cleanly to physical substrates. Open: how to handle substrates whose operating regime changes during measurement; how to formalize calibration for behavioral substrates. **Confidence: high for physical, medium-low for behavioral, low for evolving substrates.**

---

## 6. Driver Profile Structure

The artifact format that drivers produce. Analog of the ICC profile binary format — though unlike ICC, MPA's profile format will likely be structured text (JSON-like or YAML-like) rather than binary, given its smaller scale and need for human inspection.

Block-in specification:

```yaml
DriverProfile:
  header:
    profile_version: <semver>
    target_mpa_rfc_version: <list of RFCs targeted>
    substrate_class: <identifier>
    characterization_date: <ISO8601 timestamp>
    characterization_authority: <who/what produced this>
    validation_history:
      - reference_substrate: <identifier>
        validation_date: <timestamp>
        round_trip_error: <metric value>
        passing: <bool>

  operating_envelope:
    initial_conditions: <substrate state requirements>
    parameter_ranges: <external parameters with valid ranges>
    measurement_protocol: <required sampling, kernel, integration>

  gamut:
    drive_range:
      per_observer_position:
        - position: <τ_obs spec>
          D_min: <value>
          D_max: <value>
    observer_range:
      Π(S): <observer position bounds>
    shear_profile_envelope:
      <substrate-specific characterization>
    trail_class_support:
      <hostable canonical structures>
    persistence_depth:
      N(S): <integer>
      contraction_rate_observed: <fitted model>

  translation_field:
    substrate_to_canonical:
      function_specification: <how to produce canonical from native>
      parameterization: <observer-position-keyed>
    canonical_to_substrate:
      function_specification: <how to produce native predictions from canonical>
      parameterization: <observer-position-keyed>
    auto_remap_rule:
      formal_specification: <how translation evolves with τ_obs>
      derivation: <substrate-physics-grounded>

  intents:
    - name: <Intent-N name>
      supported: <bool>
      gamut_mapping_operation: <implementation>
      sacrifice_declaration: <what's lost>
      use_cases: <suggested>

  reference_outputs:
    - canonical_test_input: <reference data>
      expected_substrate_response: <expected output>
      tolerance: <metric>

  metadata:
    characterization_methodology: <prose>
    known_limitations: <list>
    versioning_history: <changelog>
    deprecation_notes: <if applicable>
```

### 6.1 Rationale for each section

- *Header:* identification, traceability, validation lineage.
- *Operating envelope:* the calibration prerequisites (per §5).
- *Gamut:* what the substrate can do (per §2).
- *Translation field:* the actual driver function (per the Architectural Block-In's "translation field over observer-space").
- *Intents:* which intents are supported and how (per §3, §4).
- *Reference outputs:* round-trip validation data (per §8).
- *Metadata:* engineering hygiene.

### 6.2 Profile composability

Drivers should be composable in the sense that two drivers for related substrate classes can be chained or compared. Block-in proposal: profiles in the same substrate-class family share format and can be diff'd; profiles for different classes can both feed the same canonical representation if their gamuts overlap.

### 6.3 What's settled vs. open here

Settled: the format covers the necessary content; structured-text format is appropriate. Open: specific schema (JSON Schema? Protocol Buffers? bespoke?); validation tooling; profile composability semantics. **Confidence: high.**

---

## 7. Pipeline Composition

How transforms chain. This is the section where the color analogy strains hardest.

### 7.1 The color pipeline

A standard color pipeline: source profile → working space → look transform(s) → output profile → display profile. Each transform declares an intent. Composition is well-defined because all transforms operate on the same type (color values) and the PCS provides the pivot.

### 7.2 The MPA pipeline

```
substrate-native data
    ↓ [driver translation, intent-declared]
canonical representation (at observer position p)
    ↓ [auto-remap, intent-declared]
canonical representation (at observer position p')
    ↓ [operator action C/S/K/R, intent-neutral]
canonical representation (modified, at p')
    ↓ [realizer interface, intent-declared]
realizer output (substrate-specific predictions)
```

Intent declarations occur at four kinds of junctions: driver translation, auto-remap (across observer positions), realizer interface, and any cross-substrate composition.

### 7.3 The type-changing problem

Color pipelines compose easily because every stage operates on color values. MPA pipelines change types: substrate-native data has substrate-specific types; canonical representation has canonical types; realizer outputs have substrate-specific (target-substrate) types. The composition rules of color don't directly transfer.

Block-in proposal: compose pipelines through the canonical representation as pivot. Just as ICC profiles compose via PCS, MPA pipelines compose via canonical representation. The type-change happens at exactly two boundaries (driver and realizer), and both are intent-declared.

### 7.4 Intent propagation

When intents are declared at multiple junctions, do they propagate or are they re-declared?

*Color rule:* intents are typically declared once per pipeline; the same intent applies throughout.

*MPA proposal:* intents are declared per-junction by default, with explicit propagation declarations available. The auto-remap junction's intent is particularly sensitive — it affects how the canonical representation evolves across observer positions, and a regime-preserving auto-remap differs substantially from a drive-faithful auto-remap.

Compatibility rule: intents at adjacent junctions must be *compatible* — they preserve a non-conflicting union of invariants. Drive-faithful followed by regime-preserving is incompatible (the first refuses to adjust, the second presupposes adjustment is possible).

### 7.5 Working transforms (operator action)

Operator actions (C, S, K, R applied within canonical representation) are intent-neutral by construction. They preserve connection-space invariants because operator algebra is closed in the canonical representation per RFC-1. So they don't require intent declarations; they sit between intent-declared junctions without breaking the compositional structure.

### 7.6 What's settled vs. open here

Settled: compose through canonical representation; type changes happen at driver/realizer boundaries; operator actions are intent-neutral. **Genuinely open and harder than other sections:** intent propagation rules across type-changing transforms, especially when auto-remap is involved; compatibility checking between adjacent intents; whether some intent compositions reduce to single equivalent intents (analogous to ICC's pipeline reduction). **Confidence: medium on shape, low on specifics. This section will require the most work at full RFC-S resolution.**

---

## 8. Round-Trip Validation

Formal protocol for checking whether a driver produces correct output.

### 8.1 The protocol

1. **Reference data preparation.** A canonical reference dataset is established for a substrate class — substrate-native data with known-correct canonical representation. Surface code QEC and habit extinction are the proposed first two reference datasets.
2. **Forward translation.** The driver under test produces canonical representation from reference substrate-native data.
3. **Comparison to reference canonical.** Driver output compared to known-correct canonical. Deviations measured by metric defined per intent (e.g., regime-partition agreement for regime-preserving intent).
4. **Backward translation.** A reference realizer applied to driver's canonical output, producing predicted substrate-native data.
5. **Round-trip comparison.** Predicted vs. original substrate-native data, comparison metric defined per intent.
6. **Acceptance.** Driver passes if forward error and round-trip error both fall below specified thresholds for all reference datasets the driver claims to support.

### 8.2 The reference-substrate problem

Here is a real difficulty: round-trip validation requires a "known-correct" canonical representation for the reference substrate. Where does that come from?

*Option A:* a hand-derived canonical representation, produced by an expert reading the substrate manually (the way v9 Appendix F gives surface-code reading rules by hand). This is the bootstrap option — the first reference is hand-built, subsequent drivers are validated against it.

*Option B:* a reference driver produced by a trusted methodology, treated as authoritative. Bootstrap problem: the reference driver itself needs validation against something.

*Option C:* multiple independent drivers for the same substrate, validated by inter-driver agreement. Stronger than either A or B alone but doesn't help with the first substrate.

Block-in proposal: use Option A for the first reference per substrate domain (surface code QEC for physical, habit extinction for behavioral), produced by hand from v9 Appendix F or analogous expert reading. Subsequent drivers validated against these. Eventually transition to Option C as multiple drivers exist for each domain.

### 8.3 Comparison metrics per intent

Different intents preserve different invariants, so different metrics apply:

- *Regime-preserving:* Hamming distance on regime partition; agreement count on edge type partition.
- *Drive-faithful:* L2 distance on drive vector; max deviation on $\gamma$ values.
- *Capacity-preserving:* deviation in $|\Gamma^*|$; structural-pattern similarity (graph isomorphism family).
- *Persistence-preserving:* sequence distance on $\{\varepsilon_n\}$; survival-declaration agreement.
- *Signature-preserving:* category agreement on signature universality class; intra-category parameter distance.

These metrics are RFC-S-detail level; block-in just establishes that each intent has a corresponding metric.

### 8.4 What's settled vs. open here

Settled: protocol structure; reference-substrate strategy; per-intent metric framework. Open: the actual reference dataset construction (substantial effort per substrate domain); acceptance thresholds (substrate-specific and currently arbitrary). **Confidence: high on structure, medium on practical implementation.**

---

## 9. Edge Cases

The un-glamorous engineering that determines whether the system works in practice.

### 9.1 Critical-threshold boundary (regime transitions)

At $\lambda \approx \pm D$, the regime is on the boundary between $c$/$s$ or $s$/$r$. Small perturbations flip the reading.

**Block-in handling:** declare a "transition zone" of width $\delta$ around each regime boundary; regime reading within the zone is undefined; intents must declare zone policy. Default policy: regime-preserving treats zone as part of the wider category; drive-faithful reports zone membership as ambiguous.

The width $\delta$ is substrate-specific and characterized by gamut measurement.

### 9.2 Capacity boundary

At $|\Gamma^*| \approx \sqrt{2D/\alpha\gamma_{\min}d_{\text{avg}}}$, the substrate is at its capacity limit. Marginal subgraphs may or may not sustain.

**Block-in handling:** similar transition zone; capacity-preserving intent has explicit boundary policy (preserve pattern, accept marginal sustainability with diagnostic).

### 9.3 Theorem-9 boundary

At $\gamma_{AB} \approx D$ for $\gamma_{AB} > 0$, joint commitment is marginal. RFC-1 §8.2 already flags this mechanically.

**Block-in handling:** Theorem-9 boundary policy depends on intent. Drive-faithful flags as out-of-spec. Regime-preserving applies scale factor. Capacity-preserving redistributes $\gamma$ to keep below boundary. Each intent's gamut mapping operation handles this case explicitly.

### 9.4 Persistence-tower edge

$\varepsilon_n$ approaching 1 — the Complexity Wall analog from v9 Appendix G.

**Block-in handling:** spec declares whether this is acceptable terminal level (Complexity Wall is the spec's intent) or failure (spec assumes deeper tower than substrate supports). Persistence-preserving intent extrapolates with growing uncertainty as boundary approached; other intents may reject specs that approach the wall.

### 9.5 Lower-bound edge cases

$\varepsilon_n = 0$: perfect contraction. Probably non-physical (information must be lost across coarse-graining steps spanning real scales). **Block-in handling:** treat as "absolute black" of MPA — declare a substrate-specific minimum admissible $\varepsilon_n^{\min}$ based on substrate physics; reject specs requesting lower.

$D = 0$: no drive. Trivial case; substrate is in classical Boolean limit (per v9). **Block-in handling:** specs requesting $D = 0$ are valid only at $\mathcal{M}_2$ subset of canonical representation; reject specs with $s$-regime vertices at $D = 0$.

$D \to \infty$: the Boolean limit per v9. **Block-in handling:** specs at this limit reduce to classical propositional logic; full MPA machinery is unnecessary; recommend Boolean export per Substrate_Synthesizer.md.

### 9.6 Multi-band incompatibility

A spec declares regime $c$ at band 1 and $r$ at band 2 such that the auto-remap from 1 to 2 cannot produce this transition.

**Block-in handling:** scale-relativity invariants per RFC-1 §8.3 catch this. Out-of-bound transitions are rejected with diagnostic; intent does not authorize violations of scale-relativity axioms.

### 9.7 What's settled vs. open here

Settled: the edge cases are enumerated; each has a block-in handling proposal. Open: specific transition-zone widths per substrate; minimum admissible $\varepsilon_n$ values; the question of whether scale-relativity violations can ever be admitted under any intent (probably no, but worth confirming). **Confidence: high on enumeration, medium on specific values.**

---

## 10. Reference Operating Conditions

Each substrate class has an operating envelope. Drivers characterize substrate behavior *within that envelope*. Outside, drivers are invalid.

### 10.1 What operating conditions include

- *Initial state.* Substrate's starting configuration before measurement begins. For physical substrates: temperature, pressure, mechanical configuration. For behavioral substrates: subject history, training status. For computational substrates: initialization seed, prior weights.
- *External parameters.* What the environment supplies. For QEC: error rate model, syndrome extraction protocol. For glass: cooling rate, aging time. For habit extinction: prior conditioning schedule, deprivation level.
- *Measurement protocol.* How the substrate is observed. Sampling rate, kernel width, integration window, observer-position trajectory.

### 10.2 The operating-envelope declaration

Driver profile (§6) carries operating envelope declaration. Calibration (§5) verifies actual conditions match. Outside the envelope, the driver gives wrong answers — not random, not noisy: confidently wrong, in the way an out-of-condition device gives systematically biased color readings.

### 10.3 What about substrates that change during measurement?

Genuine open problem. For substrates whose operating conditions evolve during use (training neural networks, evolving biological systems, organisms during learning), the static-envelope model fails. Possibilities:

*Option A:* multiple drivers for different "operating regimes," with regime detection and driver switching.
*Option B:* trajectory-aware drivers that explicitly include the substrate's evolution as part of the translation field.
*Option C:* declare such substrates outside MPA's scope until the framework extends.

This is a real frontier and likely affects which substrates can be validly characterized in early MPA work. Block-in recommendation: start with substrates whose operating envelopes are stable (QEC, habit-extinction with controlled protocols, structural glass at fixed temperature). Defer evolving-substrate problem to later RFC.

### 10.4 What's settled vs. open here

Settled: operating envelope is declared, calibration verifies, out-of-envelope gives wrong answers. Open: handling of evolving substrates. **Confidence: high for stable substrates, low for evolving ones.**

---

## 11. Open Questions and Honest Bounds

Consolidated map of where this block-in is firm and where it isn't.
 add the demand-bounded sufficiency principle to the architectural block-in's "Open questions (carried forward)" → promote to "Newly opened or sharpened," with a note that it should land in RFC-1 v0.2's foundational principles section. That way it's captured in the artifact stack before it can drift back out.

### 11.1 What I think is settled

- The architectural shape (connection space + gamut + intents + mapping operations + profiles + pipelines + validation + edge cases + operating conditions). This is the right list of components.
- The five-intent family covers the natural axes of "what gets preserved when content is out-of-gamut."
- Connection-space invariants exist and are layered (per-position + cross-position).
- Profile structure is approximately right at the field level.
- Round-trip validation has a workable protocol.
- Edge cases are at least enumerated.

### 11.2 What I'm less sure about

- The exact connection-space invariant set. Capacity envelope's status as invariant vs. gamut-constraint is genuinely open.
- Whether the intent family is exactly five or whether finer enumeration emerges.
- Pipeline composition with type-changing transforms — color's rules don't directly transfer; MPA needs its own composition algebra and I've sketched it but not derived it.
- Auto-remap interaction with intents — the most subtle question, possibly the section that most needs deeper work.
- Practical gamut characterization for substrates with non-convex or non-simply-connected gamuts.

### 11.3 What requires substantive research, not just specification

- Trail-class space metric (open from v9; blocks several intent definitions from being fully precise).
- Mathematical structure of auto-remap operations across substrate classes — are there universal forms (matrix-like, LUT-like, perceptual-model-like) or is it irreducibly substrate-specific?
- Reference dataset construction for habit extinction (the QEC reference is more straightforward via v9 Appendix F; behavioral domain is harder).
- Calibration formalization for behavioral substrates.
- Evolving-substrate handling.

### 11.4 What might mean we hit the ceiling

Three concerns:

*First,* if the mathematical structure of auto-remap operations turns out to be irreducibly substrate-specific with no universal form, then the framework can specify the *interface* (drivers must implement auto-remap) but cannot provide *infrastructure* (shared mathematical machinery). This would still be useful — it's what color management mostly is — but it would be a weaker claim than "MPA provides substrate-neutral working space" might suggest.

*Second,* if calibration cannot be cleanly formalized for behavioral and evolving substrates, then half the substrate domains MPA might want to address (and arguably the most interesting ones — neuroscience, machine learning, biology under selection) sit outside the framework's clean coverage. The framework still works for physical substrates, but its reach is narrower.

*Third,* if pipeline composition with type-changing transforms turns out to require tools beyond what color management provides — category-theoretic composition, dependent types, something heavier — then the analog isn't just "color management for MPA" but "color management plus non-trivial type theory." Doable, but a heavier lift than the block-in pretends.

None of these is a ceiling I can confirm without more work. But they're the candidates. The next few months of substantive work on RFC-S would probably resolve which (if any) is real.

### 11.5 What I'd commit to right now

The block-in's structure (this document's section list) is the right shape. The five-intent family is approximately right. Connection space + gamut + profile + round-trip validation are tractable. Pipeline composition and evolving-substrate handling are where I'd expect to need additional theoretical machinery beyond color-management analogs.

That last point matters: this is not "port color management to MPA." It's "port color management to MPA, *and* develop additional machinery for the parts where color management is insufficient." The latter is the work the block-in honestly identifies and doesn't undersell.

---

## 12. Scope Estimate

The honest accounting.

### 12.1 What this document is, in lines and weight

This block-in is approximately 5,800 words. It covers ten infrastructure components at a resolution sufficient to identify the work but not to specify it.

### 12.2 What full RFC-S would be

At a resolution comparable to ICC v4:

| Section | Block-in length | Full RFC-S target |
|---|---|---|
| 1. Connection Space | ~600 words | 15-20 pages |
| 2. Gamut | ~500 words | 10-15 pages |
| 3. Rendering Intents | ~900 words | 25-30 pages |
| 4. Gamut Mapping Operations | ~500 words | 20 pages |
| 5. Characterization vs. Calibration | ~400 words | 10 pages |
| 6. Driver Profile Structure | ~500 words | 15 pages |
| 7. Pipeline Composition | ~600 words | 15-20 pages |
| 8. Round-Trip Validation | ~500 words | 10 pages |
| 9. Edge Cases | ~600 words | 15 pages |
| 10. Operating Conditions | ~400 words | 5-10 pages |
| Appendices, examples, schema specs | — | 30-40 pages |
| **Total** | **~5,800 words** | **170-200 pages** |

This is the scale of a major engineering standard. ICC v4 is ~120 pages of core spec; the supporting documentation (gamut mapping research, characterization protocols, profile examples, validation tools) is much larger.


### 12.3 What's worth front-loading vs. deferring

*Front-load (block-in to draft 0.1 within next several sessions):*
- Connection space invariant set finalization
- Gamut characterization protocol with concrete examples for surface code QEC
- Driver profile schema (testable artifact format)
- Round-trip validation protocol with surface code QEC reference

*Defer to RFC-S 0.2 or later:*
- Full intent composition algebra
- Pipeline composition with type-changing transforms (the genuinely hard section)
- Evolving-substrate handling
- Behavioral-substrate calibration formalization

This ordering keeps the work-stream productive: front-loaded items are tractable and produce shippable artifacts; deferred items require theoretical development and are appropriately stage-gated behind the front-loaded work.

### 12.4 What this means for the immediate next session

The Architectural Block-In's priority list said "RFC-1 v0.2 next." That's still right. But RFC-1 v0.2 should not pretend to incorporate scale management as finished. It should declare scale management as a principle whose specification is RFC-S, the way ICC-aware color tools declare ICC compliance and reference the spec.

RFC-S advances in parallel with RFC-2 (FDR signatures) and RFC-3 (consistency). All three feed RFC-1 revisions over time as their content stabilizes.

This is multi-document, multi-session, multi-month work. It is also tractable work: each component is specifiable, the architectural shape is right, the infrastructure can be built piece by piece.

---

## 13. Closing

The block-in is honest about scope. RFC-S is real infrastructure work, comparable in weight to porting any major engineering standard to a new domain. It's not a session of writing; it's a research and specification program of months to years.

But it's not unbounded. Each component has a tractable specification path. The hardest sections (pipeline composition, evolving substrates) are identified explicitly, not hidden. The five-intent family covers the natural design space. The reference-substrate strategy gives a concrete bootstrap.

If we hit a ceiling, my best guess for where is the auto-remap mathematical structure — whether it has any universal form or is irreducibly substrate-specific. Resolving that requires building two or three reference drivers (surface code, habit extinction, possibly glass) and comparing their auto-remap logic. That's empirical work, not pure specification, and it can run in parallel with this document's continued development.

The session's objective — a look at what's coming — is delivered. The work is large, the work is real, the work is approximately mappable. The framework's ambition matches the size of the infrastructure required to support it. Whether to proceed is a strategic decision; whether it's possible is, at this resolution, a yes.

Not a ceiling yet.
