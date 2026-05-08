# MPA-RFC-1: Spec Object Input Contract

**Status:** Draft 0.1
**Target:** MPA v9-revised
**Series:** Input contract specification for the MPA substrate translator
**Companion documents (planned):** RFC-2 (FDR-signature contract), RFC-3 (consistency & completeness), RFC-V (reference vocabulary)

---

## 0. Scope and voice

This document specifies the **input contract for the MPA spec object** — the typed configuration `(V, E, Γ, D, τ_obs, P)` that any driver must populate for MPA's compilation machinery to operate. It does *not* specify FDR-signature measurement protocols, cross-field consistency invariants, or the realizer-side compilation logic. Those are deferred to companion RFCs.

Voice is early-RFC: precise where precision is earned by existing v9 commitments, explicit where the framework is still under negotiation. Provisional choices are marked **[Provisional]** and consolidated in §9. Where v9 is silent, this document declares a default and flags the alternative; the alternative is not foreclosed.

The spec object is the *artist register's* output and the *compiler's* input. It contains nothing about how the substrate produces the dynamics; it contains only what MPA must know to verify the spec is coherent and to emit realizer targets.

---

## 1. Top-level structure

A spec object is the tuple:

```
S = (V, E, Γ, D, τ_obs, P)
```

| Symbol | Name | Purpose |
|---|---|---|
| `V` | Vertex set | Trail-vector-bearing propositions with regime targets |
| `E` | Edge set | Pairwise (or directed) shear relations |
| `Γ` | Subgraph flag set | k_frust prescribed / forbidden / unspecified per declared subgraph |
| `D` | Drive specification | Dimensionless drive — point, interval, schedule, or tower |
| `τ_obs` | Observer kernel | Timescale band(s) at which the spec must read |
| `P` | Persistence profile | Sequence `{(D_n, ε_n, S_n)}` declaring contraction tolerances and structural survival per ascent |

A spec object is **complete** for MPA's purposes iff each of the six elements is populated to the depth required by the declarations made elsewhere in the spec (see §8 for cross-field invariants and the completeness criterion).

A driver written against this RFC produces a spec object plus the substrate-class reading rules (Appendix F-style). The reading rules are *not* part of the spec object — they live in the realizer interface layer.

---

## 2. Vertices (V)

A vertex declaration is:

```
vertex {
    id: <unique string within V>
    trail_vector_type: <type signature>
    regime_target: c | s | r | *
    lambda_constraint: <optional explicit range>
    local_drive: <optional D override>
    band_keying: <optional τ_obs subset>
}
```

### 2.1 Trail vector type

v9 treats trail vectors as kernel-weighted histories supporting weighted sums (operator C: `d_{A⊕B} = w_A·d_A + w_B·d_B`) and normalized differences (operator K: `δ = d̂_A − d̂_B`). This implies an inner-product structure.

**[Provisional]** RFC commits to: trail vectors are elements of a real inner-product space of declared finite dimension `d`. The trail vector type is `(d ∈ ℤ⁺, inner_product = "euclidean")` by default. Substrates whose native trail object is non-Euclidean (e.g., complex-valued amplitudes prior to projection, manifold-valued states) must declare an explicit inner-product structure or a map to a Euclidean image.

**Cross-vertex compatibility.** When operator C is applied to two vertices `A`, `B` with differing trail-vector types, the spec must declare the merge map `(T_A, T_B) → T_{A⊕B}`. If types agree, default-merged. **[Open — §9]**

### 2.2 Regime target

`regime_target ∈ {c, s, r, *}` where `*` denotes unassigned.

- A vertex with `regime_target = *` is admissible only if no element of the persistence profile (§7) requires this vertex's regime to be invariant under the flow.
- Total assignment is preferred. Partial assignment with `*` is permitted but produces an "incomplete-regime" diagnostic at compile time.
- **[Provisional]** Regime assignment is per-(vertex × τ_obs band): a vertex may carry different regime targets at different bands, subject to the scale-relativity invariants in §8.

### 2.3 Stability axis λ

v9 defines:

| Regime | λ range |
|---|---|
| c | λ ≪ −D |
| s | \|λ\| ≲ D |
| r | λ ≫ D |

The notation `≪` and `≫` is informal. **[Provisional]** RFC commits to sharp interval boundaries at the spec layer:

- c: λ ∈ (−∞, −D]
- s: λ ∈ (−D, +D)
- r: λ ∈ [+D, +∞)

where `D` is the drive at the vertex's `band_keying` band (or the global drive if unspecified). Operational tolerance — how far past the boundary a measured λ must lie before the regime reads as the next type — is a realizer-side question and lives in RFC-2's signature-fitting protocol, not here.

λ is dimensionless (D is dimensionless; λ is in the same units).

### 2.4 Local drive

A vertex may declare a `local_drive` value or interval distinct from the global D. Used for mentor pumping, focused gardens, and other spatial drive heterogeneity.

- Local drive must lie within the global D specification's range, or be tagged as an explicit exception (e.g., a mentor-pump vertex sitting at higher local D than global).
- When a vertex sits in overlapping local-drive regions, **[Provisional]** the rule is pointwise max (drive accumulates additively in regions, then takes the largest declared value at any point). **[Open — §9]**

### 2.5 Band keying

Optional. If the spec is multi-band (§6), each vertex may key its declarations (regime target, λ constraint) to a subset of the τ_obs bands in scope. Default: all declarations apply at all bands in scope.

---

## 3. Edges (E)

An edge declaration is:

```
edge {
    id: <unique string within E>
    endpoints: (vertex_id, vertex_id)
    shear: γ_AB
    reciprocity: reciprocal | directed
    band_keying: <optional τ_obs subset>
}
```

### 3.1 Endpoints

Default unordered (reciprocal). Declaring `directed` makes the endpoint pair ordered and requires both `γ_{AB}` and `γ_{BA}` to be specified separately. Directed edges invoke the **non-reciprocal coupling extension axis** (v9 §8); spec compilation against a non-extension realizer fails on directed edges.

### 3.2 Shear γ_AB

γ is a real number in **D-units** (dimensionless). Sign convention at the spec layer:

- γ < 0: cooperative (joint commitment is below-cost vs. independent commitment)
- γ ≈ 0: orthogonal (joint commitment costs as independent)
- γ > 0: conflicting (joint commitment incurs additional cost γ in D-units)

**[Provisional]** RFC commits to this sign convention as the **canonical spec-layer sign**. Substrates whose native shear measurement carries opposite sign (e.g., overdamped Langevin / Markovian substrates per Appendix F.1) perform sign inversion **at the substrate-class reading rule layer**, not at the spec object. The spec object always uses canonical signs.

The shear value γ_AB is the per-edge contribution to the joint-commitment budget evaluated against the operating drive D at the edge's band.

### 3.3 γ = 0 vs. edge absence

**[Provisional]** RFC distinguishes:

- `γ = 0`: positive orthogonality claim. This pair is required to read as orthogonal under the FDR-signature contract at the edge's band(s). Contributes to consistency checks.
- Edge absence: no claim about the pair. No consistency obligation incurred.

These are not equivalent. A driver that wants to assert "these vertices have no relationship" should declare `γ = 0` with appropriate band keying; a driver that wants to leave the relationship unspecified should omit the edge.

### 3.4 Band keying

Edge γ values may differ across τ_obs bands (γ scales with τ_obs per v9). Edge declarations may key to specific bands. The monotonicity relation across bands is part of the consistency contract (§8, deferred to RFC-3).

---

## 4. Subgraphs (Γ)

A subgraph declaration is:

```
subgraph {
    id: <unique string within Γ>
    members: <set of vertex_ids and edge_ids>
    flag: prescribed_frust | forbidden_frust | unspecified
    topological_invariant: <optional k_frust value or set>
    band_keying: <optional τ_obs subset>
}
```

### 4.1 Flag semantics

- `prescribed_frust`: the subgraph is required to carry `k_frust ≠ 0` at the bands in scope. The cycle's c-edge constituency is τ_obs-dependent (vertex regimes shift with band); k_frust as a topological invariant is τ_obs-invariant per v9, but the *condition for the invariant to apply* (constituent vertices in c, edges with conflicting shear product around the cycle) is band-dependent.
- `forbidden_frust`: the subgraph is required to be frustration-free (`k_frust = 0`). This is the "frustration-free closure" declaration referenced in the synthesizer doc.
- `unspecified`: no claim. Default if subgraph is declared but no flag supplied (rare; usually subgraphs are declared *because* a flag is being asserted).

### 4.2 Topological invariant declaration

For `prescribed_frust`, the spec may optionally declare a specific `k_frust` value or an admissible set. If unspecified, any nonzero `k_frust` satisfies the flag.

The form of `k_frust` itself — whether an integer, an element of a topological group, a tuple over a hypergraph (extension axis: higher-order frustration) — is substrate-determined and lives in the realizer interface layer. The spec object asserts the existence and (optionally) the value/set; it does not specify the realization.

### 4.3 Overlapping flags

A vertex or edge may participate in multiple subgraphs. Constraints combine by conjunction. Conflicting constraints (one subgraph requires `prescribed_frust`, another requires `forbidden_frust` on overlapping members) produce a compile-time diagnostic and reject the spec until resolved.

### 4.4 Band keying

Subgraph flags may apply at a subset of τ_obs bands. A single subgraph may carry `prescribed_frust` at one band and `unspecified` at another, reflecting that the cycle's c-edge constituency holds at one observation scale and not another.

---

## 5. Drive (D)

D is dimensionless: `D = Φ*/κ` per v9. The spec layer specifies D only; the realizer produces `(Φ*, κ)` envelopes; compilation intersects.

### 5.1 Form

The drive specification takes one of four forms:

| Form | Structure | Use |
|---|---|---|
| `point` | single scalar D | Single fixed operating drive |
| `interval` | D ∈ [D_low, D_high] | Range of admissible drives |
| `schedule` | D(τ_obs) | Drive varies across τ_obs bands |
| `tower` | {D_n}_{n=0}^{N} | Drive sequence over meta-ledger ascents (paired with persistence profile) |

A spec may use exactly one form.

### 5.2 Tower form

When `tower` is selected, the drive sequence is paired one-to-one with the persistence profile's ascent levels (§7). Constraint between levels: per v9, the contraction `ε_n < 1` on each ascent bounds `D_{n+1}` relative to `D_n`. The exact bound is part of the consistency contract (RFC-3); the spec declares the requested D_n values, the consistency contract validates against ε_n.

### 5.3 Realizer envelope handshake

The spec layer never specifies `Φ*` or `κ` directly. The realizer interface document (companion to RFC-1) specifies:

- The realizer's reachable D set, derived from `(Φ*, κ)` envelope
- Whether the realizer can hit point / interval / schedule / tower forms
- Substrate-class-tagged

Compilation: requested D set ∩ realizer D set. Empty intersection produces a compilation failure with diagnostic specifying which D values are unreachable.

### 5.4 Local distributions

In addition to the global D specification, vertices may declare `local_drive` overrides (§2.4). The global D specifies the *base* drive; local declarations specify perturbations or overrides. For mentor pumping and focused gardens, local distributions are the natural carrier.

---

## 6. Observer Kernel (τ_obs)

### 6.1 Form

τ_obs takes one of three forms:

| Form | Structure | Use |
|---|---|---|
| `point` | single timescale, band width substrate-determined | Single-scale spec |
| `band` | τ_obs ∈ [τ_low, τ_high] | Explicit band |
| `multi-band` | list `{τ_obs^(i)}` with declarations keyed per band | Multi-scale spec |

**[Provisional]** Default band width for `point` form is one decade in log-time, centered on the declared τ_obs.

### 6.2 Units

The spec layer must declare τ_obs units. Two acceptable forms:

- **Substrate-dimensionless ratio:** `τ_obs / τ_microscopic` where `τ_microscopic` is the substrate's natural fastest timescale. Preferred for substrate-neutral specs.
- **Physical units:** seconds, ms, etc. Acceptable when the substrate class is bound. The realizer interface document declares the unit conversion at substrate binding.

v9 leaves the unit implicit. **[Provisional]** RFC requires explicit declaration.

### 6.3 Operational meaning

At a declared band, every spec element keyed to that band must satisfy its FDR-signature target (RFC-2) over an integration window whose width lies within the band. "The spec must read at this band" means: a measurement protocol with kernel width in the band must produce signatures matching the declarations.

For `band` form, the declaration must hold over *every* kernel width in the interval. For `multi-band`, declarations are per-band and may differ.

### 6.4 Multi-band semantics

When a single spec element (vertex, edge, subgraph) carries declarations at multiple bands, the declarations must be self-consistent under scale-relativity:

- Vertex regime monotonicity: a vertex may transition c → s → r as τ_obs widens, but not r → c (a trail decohered at narrow band cannot recohere at wide band). Inverse transitions are flagged.
- Edge γ monotonicity: γ generally weakens at wider τ_obs (specific monotonic relation deferred to RFC-3).
- Subgraph k_frust: invariant across bands by topology, but the flag's *applicability* is band-keyed because the cycle's c-edge constituency is band-dependent.

### 6.5 Interaction with persistence profile

Each ascent `n` of the persistence profile is associated with a τ_obs band `τ_obs^(n)`. Ascending the meta-ledger corresponds to widening the kernel; the band sequence `{τ_obs^(n)}` is monotonic non-decreasing. A spec that declares both multi-band τ_obs and a persistence profile must align the bands with the ascent levels explicitly.

---

## 7. Persistence Profile (P)

The persistence profile is the spec's commitment to what survives the meta-ledger flow, at what contraction cost, at each ascent level.

### 7.1 Sequence structure

```
P = {(D_n, ε_n, S_n)}_{n=0}^{N}
```

- `D_n`: drive at level `n`. If drive (§5) is specified as `tower`, these match.
- `ε_n`: contraction tolerance at ascent `n`.
- `S_n`: survival declaration — set of structural objects required to be invariant under the n-th compression step.

### 7.2 ε_n definition

**[Provisional]** `ε_n = ‖C_n‖_op` where `C_n: Trail-class space at level n → Trail-class space at level n+1` is the compression map, and `‖·‖_op` is the operator norm with respect to the trail-class metric.

Required: `ε_n ∈ [0, 1)` for the tower to converge at ascent `n`. `ε_n ≥ 1` declares a Complexity Wall at level `n` per v9 Appendix G — the tower diverges beyond this point and the spec is asserting that no further coarse-graining is possible.

The trail-class metric itself is **[Open — §9]**. v9 flags this as an open problem ("metric on trail-class space"). RFC-1 inherits the openness; RFC-3 will revisit when the consistency contract requires concretization.

### 7.3 Sequence length N

The spec declares one of:

- **bounded:** specific finite `N`
- **unbounded:** require `ε_n < 1` for all `n`, with `N` substrate-determined
- **substrate-deferred:** `N` reported by realizer; spec accepts whatever the realizer produces

**[Provisional]** Default: substrate-deferred.

### 7.4 Survival declarations S_n

`S_n` is a set of structural objects required to be invariant at ascent `n`. Object types admissible in `S_n`:

- Vertex regime classes (e.g., "all vertices declared c at the level-n band must remain c at level n+1")
- Specific subgraph flags (e.g., "this prescribed_frust subgraph must persist")
- Specific edges (e.g., "this γ < 0 cooperative edge must persist")

Survival semantics: an object `o ∈ S_n` is "preserved at ascent `n`" iff `C_n(o)` lies within `ε_n` distance of an object of the same type at level `n+1`, under the trail-class metric.

`k_frust` declarations are invariant under the flow (per v9), so a `prescribed_frust` subgraph appearing in `S_0` is preserved at every ascent without re-declaration. Declaring it in `S_n` for `n > 0` is redundant but harmless.

### 7.5 Substrate-incomplete reporting

When the substrate's data does not span enough scales to populate `{D_n, ε_n}` up to declared `N`, compilation produces an `insufficient_ascent_data` diagnostic listing:

- The highest `n` for which data is available
- Which `S_n` declarations remain unverified above that level
- Whether the spec is rejected (bounded N, data short of N) or accepted with caveat (substrate-deferred N)

**This is a feature, not a failure.** Per the strategic ordering, MPA must be able to declare "the substrate does not give us enough scales to verify this level." A driver that cannot populate the persistence profile to the required depth is the correct output, not a defect.

---

## 8. Cross-field invariants (preview of RFC-3)

The spec object's elements are not independent. The full enumeration of cross-field consistency invariants is deferred to RFC-3. This section establishes the categories the consistency contract must cover.

### 8.1 Drive ↔ Persistence

If drive is specified as `tower` and persistence profile uses `{(D_n, ε_n)}`, the D_n values must agree across both. Mismatch: compilation failure.

### 8.2 Drive ↔ Edges (Theorem 9 mechanical check)

For each edge with `γ_AB > 0`, if `D < γ_AB` at the edge's band, the pair `(A, B)` admits no joint commitment (v9 Theorem 9). Compilation flags this mechanically.

This is a **diagnostic, not necessarily a failure.** A spec may intend the regime where joint commitment is forbidden — gridlock-as-stability, deliberate frustration. The diagnostic surfaces the situation; the spec author resolves.

### 8.3 Vertex regime ↔ τ_obs

Multi-band regime declarations must respect monotonicity (§6.4). Non-monotonic declarations are flagged at compile time as scale-relativity violations.

### 8.4 Edge γ at multi-band

Multi-band edges must respect monotonic relation between γ values across bands. Specifics: RFC-3.

### 8.5 Persistence profile ↔ subgraphs

Subgraphs with `prescribed_frust` must appear in `S_0` to be verifiable (k_frust is invariant; once declared at n=0, preserved up the tower).

### 8.6 Capacity envelope check

Per v9: `|Γ*| ≤ √(2D / α·γ_min·d_avg)` on classically consistent graphs. Subgraph declarations exceeding this envelope at the declared D are flagged. Specifics: RFC-3.

---

## 9. Open questions

Consolidated list of items left open by this RFC.

1. **Trail-class metric.** v9 flags this as open. ε_n's precise meaning depends on a metric choice. RFC-1 uses the operator-norm convention; RFC-3 will revisit.
2. **Boundary behavior at λ = ±D.** Provisional sharp cutoffs at the spec layer; FDR signature behavior at the boundary deferred to RFC-2. Whether the boundary is measure-zero or carries structural content is open.
3. **Multi-band signature interactions.** When a vertex must read c at band 1 and s at band 2, does the FDR-signature contract require both signatures in distinct experimental protocols or in a single multi-band protocol? Affects realizer interface design.
4. **Reciprocity default.** Whether default-reciprocal survives once non-reciprocal coupling becomes first-class (extension axis activation).
5. **Trail vector cross-vertex compatibility.** When operator C merges differently-typed vertices, the merge map must be declared. RFC-1 requires explicit declaration on type mismatch and default-merges on type match. Whether a more permissive default exists is open.
6. **ε_n on what map.** The contraction operator C_n acts on trail vectors, trail-class equivalence classes, or some other object. Pinned down at the trail-class level provisionally; RFC-3 to confirm.
7. **Local D in overlapping mentor pumps.** Provisional rule: pointwise max. Whether additive or some other combinator is correct depends on substrate physics; RFC-3 with substrate input.
8. **Band width default for `point` form τ_obs.** Provisional: one decade log-time. May need substrate-conditional override.
9. **k_frust object structure.** Spec asserts existence and (optionally) value; the algebraic structure of k_frust (integer? group element? hypergraph tuple?) is realizer-side. RFC-1 leaves this unspecified at the spec layer.

 add the demand-bounded sufficiency principle to the architectural block-in's "Open questions (carried forward)" → promote to "Newly opened or sharpened," with a note that it should land in RFC-1 v0.2's foundational principles section. That way it's captured in the artifact stack before it can drift back out.

---

## A. Reference vocabulary (placeholder for RFC-V)

This RFC uses v9's vocabulary verbatim where possible. Items requiring future canonicalization in RFC-V:

- Trail-class metric (currently unnamed)
- Tower-level naming convention (currently `n = 0, 1, ..., N`; whether to adopt physical-RG conventions or stay neutral is open)
- Contraction operator notation (`C_n` here vs. `C` in v9; v9's `C` may collide with operator C in `Σ = {C, S, K, R}`)

The collision between operator `C` (try-merge) and contraction operator `C` is real and unresolved in v9. **[Provisional]** RFC-1 uses `C_n` for the n-th contraction (compression) operator and reserves bare `C` for the try-merge operator. RFC-V will canonicalize.

---

## B. Versioning notes

**This document:** MPA-RFC-1, draft 0.1.

**Target framework version:** MPA v9-revised (per Substrate_Synthesizer.md and v9_compressed.md).

**Compatibility statement:** Any future MPA revision that changes the typed objects (vertex regimes, edge shear, subgraph flag, drive form, observer kernel structure, persistence profile structure) requires a corresponding MPA-RFC-1 revision with explicit migration notes.

**Driver compatibility:** Drivers (substrate-class translation rules) declare which MPA-RFC version they target. Drivers targeting MPA-RFC-1 v0.x may be incompatible with future v1.0+ without migration.

---

## C. What this RFC is not

- **Not the FDR-signature contract.** Measurement protocols, signature curve shapes, fitting tolerances, and canonical perturbations live in RFC-2.
- **Not the consistency contract.** Cross-field invariants, the full Theorem-9 enumeration, capacity envelope checks, and compile-time diagnostic catalog live in RFC-3.
- **Not the realizer interface document.** Substrate-class reading rules (Appendix F-style), `(Φ*, κ)` envelope formats, signature-target documents for third-party consumption live in the companion realizer interface RFC.
- **Not the translator tool design.** The translator consumes drivers conforming to this RFC; its internal design is downstream.

The intent of this layering is the discipline the strategic ordering called for: **specify MPA's input shape before building anything that consumes it.**
