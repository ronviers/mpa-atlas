# MPA Architectural Block-In

**Status:** v0.2 — block-in level (broad strokes, not detailed specification). v0.2 promotes three additional principles to foundational status: demand-bounded sufficiency, singular working-space path, thin-RFC discipline.
**Purpose:** Capture the architectural commitments made this session at a resolution sufficient for the next session to work from
**Companion artifacts:** [RFC-1 (Spec Object)](../rfcs/MPA-RFC-1_Spec-Object.md); [RFC-S Block-In (Scale Management)](../rfcs/MPA-RFC-S_Scale-Management_Block-In.md); [v9 framework](../framework/v9_MPA_A_Driven-Dissipative_Synthesis_with_Boolean_Limit.md)

---

## What this document is

A block-in, in the VFX sense: the architecture sketched at low resolution covering the whole scope, before any single piece is detailed. Polygonal block-in before sculpting — the right shapes are in the right places, surfaces aren't refined yet. The next session refines specific pieces against this block-in.

---

## The session's strategic shift

**Started:** build a substrate translator, point it at substrates with rich data (habit extinction, glass, QEC, etc.).

**Shifted to:** specify MPA's input contract first via RFC-style protocol, *then* build the translator against the contract, *then* point it at substrates. Reasoning: auto-generated drivers without a fixed input contract reproduce the Lakatosian failure mode — drivers fit locally while the framework's belt grows to absorb whatever it sees, making MPA unfalsifiable in the bad way.

**Sharpened with:** two architectural disciplines borrowed from VFX/compositing.

**Color management** as the model for substrate-neutral working space. The framework distinguishes scene-referred / working / display-referred analogs cleanly: substrate-native (the world), canonical representation (the working space the framework operates in), realizer outputs (substrate-specific predictions). Transforms between layers are declared, named, versioned, swappable.

**Observer-driven scale management** as the model for handling MPA's intrinsic multi-scale structure. Scale is not a property of objects in the spec; it is a property of the observer's framing. As $\tau_{obs}$ moves, the canonical representation auto-remaps so the framework stays in a tractable regime. The artist works always in a workable space because the camera handles scale management.

These are coupled disciplines. Working-space neutrality without scale management gets a clean canonical representation that fights you the moment you cross scales. Scale management without working-space neutrality gets smooth scale handling but no shared substrate-neutral layer to do work in. Together they're the foundation.

---

## Foundational principles (consolidated)

The architectural commitments below are load-bearing. RFCs do not re-derive them; they declare adherence and let mechanical validation enforce. The block-in carries the long-form treatment; the RFCs carry the operational consequences.

### 1. Color-management discipline (substrate-neutral working space)

Three layers — substrate-native, canonical representation, realizer-output — with declared, named, versioned, swappable transforms between them. The canonical representation is substrate-neutral by construction. (Body of this document, "The three-layer architecture.")

### 2. Observer-driven scale management

$\tau_{obs}$ is the camera. Canonical representation is observer-relative; cross-scale composition is camera motion, not transform invocation. No scale-class taxonomy baked into the framework. (Body of this document, "The observer is the scale manager.")

### 3. Demand-bounded sufficiency — *the MPA is not the bottleneck*

Precedent: a CD samples at 44.1 kHz because human ears stop hearing past ~20 kHz, not because that's the maximum the medium could support. The format is sized to the demand, not to maximal fidelity to the source.

The framework commits to *enough* representation for the demand placed on it, not maximal faithfulness to the substrate. Drivers declare a demand envelope (which signatures must read at which precision at which observer positions); the canonical representation is sized to it. Past the envelope, the framework is silent — not because it can't carry more, but because the demand doesn't ask for more.

Consequence: MPA is not the bottleneck on substrate fidelity. Substrates carry whatever fidelity they carry; the framework reads only what the demand needs. Drivers don't claim unbounded fidelity; they declare an envelope they're calibrated for.

Lands in: RFC-1's foundational principles section (as a principle); RFC-1 §3 invariant 7 (every spec object declares a demand envelope); RFC-S §2 with a parallel subsection on the demand side; the driver profile schema (drivers declare a demand envelope they cover).

### 4. Singular working-space path

Within an RFC version, exactly one canonical-representation shape. Plurality lives where it legitimately belongs:

- **Drivers** — substrate-conditional plurality. One driver per substrate class.
- **Realizer-interface intent flags** — user-intent-conditional plurality. A small, deliberate enumeration (analog of color management's perceptual / relative / absolute / saturation), explicitly declared in the realizer-interface RFC, never grown organically.
- **Version succession** — time-conditional plurality. RFC-1 v0.1 → v0.2 → v1.0. Versioning, not branching. No RFC-1A vs RFC-1B at any moment.

Not at the working-space layer. Workstations, DCC apps, and color management protocols carry decades of dropdown baggage because they grew up serving constituencies; we have no constituencies and we refuse to grow the baggage. The framing the user named: *peel*, not scrape — peel away the legacy paths down to the singular working path.

Lands in: every RFC's structure (one shape per version); RFC-V (one canonical name per concept, no synonyms); CI-level checks once they exist (reject specs that introduce alternative working-space shapes within a version).

### 5. Thin-RFC discipline — *it was never brittle if it never broke*

Exchange surfaces are written at gross-underengineering resolution by design. Not less rigorous, not phoned-in: deliberately thin where standards bodies are thick, because the forces that thicken standards bodies' protocols don't apply to us yet:

- No legacy interop. There is no v8.5 we owe compatibility to.
- No multi-stakeholder negotiation. Single program, single author per artifact.
- No defensive MUST/SHOULD/MAY granularity needed at N=1 implementer.
- No edge-case enumeration upfront. The algebra is in v9; the protocol declares invariants and lets v9 carry the cases.

What the protocols *do* contain:
1. **Object** — what artifact this governs (1 sentence)
2. **Shape** — typed declaration / schema
3. **Invariants** — numbered list, ≤7 where possible
4. **Operations** — what you can do with it, what they preserve
5. **Falsifiers** — what makes a candidate invalid
6. **Pointer** — which v9 sections carry the formal derivation

Half a page per object is the target; growth past it is debt that requires explicit justification (a comment naming what force pushed past brevity, with a revert-when-force-passes commitment).

Justification: brittleness is a measurement against actual stress. A thin protocol that holds under the stress it actually encounters is correctly underspecified, not negligently so. *It was never brittle if it never broke.* When something breaks, we thicken the relevant spot — that spot only, that break only, with a debt-marker. The defensive instincts that grew ICC v4 to ~120 pages are real; we don't import them prophylactically.

Failure modes acknowledged: Markdown / HTTP/1.0 / CSV are warnings — short spec + thin substrate = ambiguity everywhere. We avoid this trap because **v9 is rigorous**: the protocols can be thin because the framework underneath is dense. v9 (~80 pages) carries the rigor; the RFCs carry the contract. Together they're the right total weight, distributed correctly.

Lands in: every RFC structure (six-field template); explicit page-budget targets per RFC; the RFC review discipline (reject growth past budget without debt-marker).

### Coupling between principles

The five principles are coupled, not independent:

- **Demand-bounded sufficiency** sets *how much* the framework commits to per object.
- **Singular working-space path** sets *how many shapes* of representation exist (one).
- **Thin-RFC discipline** sets *how much exchange contract* governs the shape (minimum for sufficiency).

Sufficiency without the singular path: the framework still has to negotiate which shape is in scope. Singular path without sufficiency: the one shape is over-specified. Either without thin-RFC discipline: the protocol bloats to defend a shape and a sufficiency claim that don't need defending yet. Together they form a compact discipline: one shape, sized to demand, contracted thinly.

---

## The three-layer architecture

```
   Substrate-native layer
        ↑↓  driver / IDT-analog
   Canonical representation (working space)
        ↑↓  realizer interface / ODT-analog
   Realizer-output layer
```

### Substrate-native layer

The world. Substrate-specific sensors, native units, native dynamics. The driver-RFC interface is where MPA meets reality. Examples: surface-code syndrome streams, habit-extinction trial data, dielectric relaxation measurements, neural firing rasters.

The framework makes no commitments at this layer; substrates do what substrates do.

### Canonical representation (working space)

MPA-native. The typed objects v9 already specifies — trail vectors, vertex regimes, edges with shear, subgraphs with $k_{\text{frust}}$, drive $D$, observer kernel $\tau_{obs}$, persistence profile $P$. Tightened by RFC-1 and successors.

Properties (declared, load-bearing):
- Substrate-neutral by construction
- Closed under operator action ($\Sigma = \{C, S, K, R\}$)
- Always in a workable regime *because the observer determines the framing*
- Versioned (drivers and realizers commit to a canonical-representation version)

The working space is where the framework's machinery operates — Theorem 9 mechanical checks, capacity envelope checks, persistence verification, signature target checking. All of these live here. Tools downstream of this layer (translator, compiler) operate against the canonical representation, not against substrate-native.

### Realizer-output layer

Substrate-specific outputs: signature target documents, predicted observables, gamut-checked compilation results. The realizer interface RFC defines this layer's contract.

Intent-flagged: realizer outputs declare what they preserve from the canonical representation (regime structure? absolute drives? relative shear ratios?) so the user's intent is explicit. Color management's gamut-mapping intent flags (perceptual / relative colorimetric / absolute / saturation) are the precedent. MPA's intent flags will be different in content but the same in role.

---

## The observer is the scale manager

This is the load-bearing principle of the new architecture.

### The Maya wish, restated for MPA

An artist working in Maya wants the camera to handle scale automatically — frame the toy, you're working at toy-scale; frame the mountain, you're working at mountain-scale; the working space auto-remaps so you're always in a comfortable numerical range. Scale is on the camera, not on the objects. (This is not currently how Maya works; it is how artists wish it worked.)

### MPA's analog

$\tau_{obs}$ is the camera. The spec author declares the observer's framing — a band, a schedule, a trajectory — and the canonical representation is *defined relative to that framing*. Vertex regimes, edge $\gamma$ values, subgraph $k_{\text{frust}}$ applicability — all of these are observer-relative quantities. The framework auto-remaps as $\tau_{obs}$ moves so the working space stays tractable.

### What this gives us

**No scale-class taxonomy.** No `{fast, mid, slow}` or `{micro, meso, macro}` enumeration baked into the framework. Each spec works in its own observer-space; the framework doesn't pre-commit to a taxonomy that any specific substrate would find wrong.

**The persistence profile reads naturally as a camera trajectory.** $\{\tau_{obs}^{(n)}\}$ is the sequence of observer positions. Each ascent $n$ is a camera move (widening the kernel). The contraction operator $\mathcal{C}_n$ is the *view-change* — what happens to the canonical representation as the camera moves from position $n$ to position $n+1$. $\varepsilon_n$ is the loss budget for that view-change. The structure was already in v9; what's new is reading it as observer trajectory rather than as static multi-scale layering.

**Cross-scale composition becomes camera motion, not transform invocation.** Specs that span scales aren't doing scale-mixing in the dangerous Maya sense; they're declaring how the observer moves through $\tau_{obs}$-space. The artist never has to think "this vertex is at scale class X, this edge is at scale class Y, what's the transform" — they think "here's where the camera is, here's where it moves to, here's what should survive the move."

**The driver problem clarifies.** A driver isn't a one-shot translation from substrate-native to canonical at a single observer position. A driver is a *translation field over observer-position space* — it specifies how substrate-native data becomes canonical at every observer position the substrate exposes, and how the translation evolves as the observer moves. This is more demanding than the previous framing but it's the real shape of the problem.

### Where the Maya analogy strains

In Maya, auto-remap is multiplicative — a single scale factor handles it cleanly. In MPA, the remap as $\tau_{obs}$ changes is substrate-conditional and intentionally lossy. Regimes can change ($c \to s$ as $\tau_{obs}$ widens), structures can dissolve, the lossy contraction operator means information is genuinely thrown away by design.

So "auto-remap" can't be a one-line rule applied uniformly; it's substrate-specific logic that lives in drivers. The framework commits to the *interface* (observer position determines canonical representation; drivers handle the remap as observer moves) but not to a universal mechanism.

This is fine. The interface commitment is what matters for substrate neutrality; the substrate-specific logic is what drivers are for.

---

## What this means for the spec object

The $(V, E, \Gamma, D, \tau_{obs}, P)$ structure is preserved. What changes is how to read it.

- All elements are *implicitly observer-relative*. Already true in v9 (scale-relativity); now load-bearing.
- $\tau_{obs}$ becomes more central than RFC-1 draft 0.1 treated it. It's not just one of six fields; it's the *framing field* that defines the observer's position and the canonical representation's calibration. Other fields are read relative to it.
- $P$ becomes the camera trajectory. Already true in spirit; now explicit.
- The spec author writes in observer-relative terms throughout. The framework provides discipline to ensure observer-relativity is consistent across the spec.

RFC-1 needs revision (planned: v0.2) to make these implicit commitments load-bearing. The revision adds a foundational "Architectural framing" section near the top declaring color-management discipline and observer-driven scale management as principles, and rewrites §6 (observer kernel) and §7 (persistence profile) to reflect the camera/trajectory reading.

---

## What this means for drivers

A driver is no longer a single function `substrate_native → canonical`. A driver is a structured object specifying:

1. **Scope.** Which substrate-class the driver covers, what observer-position range it supports, which observables it can read from substrate-native. (Frontend gamut.)
2. **Translation field.** How substrate-native maps to canonical at every supported observer position. (The IDT, varying with observer.)
3. **Remap behavior.** How the translation evolves as the observer moves. (The auto-remap rule, substrate-specific.)
4. **Signature target outputs.** What predicted observables the driver claims at each observer position. (For round-trip checking.)
5. **Versioning.** Driver version + canonical-representation version + MPA-RFC version targeted.
6. **Reference-substrate validation.** For each driver, the calibration substrate it's been validated against.

This is more structured than the previous framing, but the structure is what makes drivers checkable. The conversion-gain criterion (does running through this driver clarify substrate behavior?) becomes one of several driver-quality measures alongside round-trip fidelity, scope coverage, and consistency-contract compliance.

---

## Reference substrates

Color management uses reference targets (Macbeth charts, calibration suites) that any new pipeline component is validated against. MPA needs analogs.

**Surface-code QEC** is the first reference substrate, because v9 §5 already gives the empirical validation (Cugliandolo–Kurchan aging diagonal at sub-threshold) and Appendix F gives the by-hand reading rules. Any new driver should be checkable against the surface-code reference: produce its driver, run it on the canonical surface-code data, confirm the same FDR signatures emerge.

**Habit extinction** is the candidate second reference substrate, for the behavioral domain. Decades of clean acquisition / extinction / spontaneous-recovery / reinstatement data; structure maps cleanly onto trail-vector decay and mentor pumping; field has been receptive to formal models. The previous session identified this as the right first behavioral driver target; the block-in promotes it to *reference target* status — used to validate every subsequent behavioral-domain driver.

**Glass / structural relaxation** as a third reference target eventually, because the data is overwhelming and the field has battled the relevant questions for forty years. But not until QEC and habit extinction are stable references; the block-in says don't take on glass before the references are solid.

---

## v9 corrections needed

Two intervention points (paste-ready instructions provided in chat earlier this session):

1. **Notation disambiguation** between operator $C$ (try-merge, $\in \Sigma$) and compression operator $\mathcal{C}$ (Compression Axiom). v9 distinguishes typographically but doesn't state the convention. Small, paste-ready.
2. **Architectural framing layer-in** — observer-as-camera and working-space-discipline — as principles in the body of v9. This is heavier than the notation fix and should wait until RFC-1 v0.2 is stable, then back-port the language to v9.

---

## Open questions (carried forward)

**From v9 (still open):**
- Metric on trail-class space (required for $\varepsilon_n$ to have a precise meaning beyond operator-norm convention)
- Per-regime universality invariants (the cross-substrate transfer evidence is the strongest signal so far)
- Formal coarse-graining map at RG-literature rigor

**From this session and follow-ons (newly opened or sharpened, now promoted to foundational principles — see "Foundational principles (consolidated)" above):**
- *Demand-bounded sufficiency.* Now principle #3.
- *Singular working-space path.* Now principle #4. *Peel*, not scrape — the workstations-traverse-narrow-paths observation, applied to protocols.
- *Thin-RFC discipline.* Now principle #5. Gross-underengineering-by-design at exchange surfaces. Half a page per object as target. *It was never brittle if it never broke.*

**From this session (still open):**
- *Auto-remap mechanics:* substrate-specific logic lives in drivers, but is there a universal *form* the substrate-specific logic takes? Color management has a small set of mathematical structures — matrices, 3D LUTs, perceptual models — that all transforms instance. MPA's might too, but we don't know yet.
- *Reference-target standardization:* who decides which substrates are reference targets, on what criteria, with what versioning?
- *Conversion-gain measurement:* how to operationalize "this driver clarifies substrate behavior" as a falsifiable criterion?
- *Intent flags for realizer outputs:* full enumeration deferred. At least four candidates parallel to color's perceptual / relative / absolute / saturation. What's the analog set for MPA?
- *Versioning protocol depth:* RFC-V will canonicalize, but the substantive question is which artifacts are versioned (the canonical representation? individual drivers? individual realizers? the RFC sequence?). Decision deferred but flagged as bake-in risk.

---

## Status of sessional artifacts

| Artifact | Status | Location |
|---|---|---|
| RFC-1 draft 0.1 (Spec Object) | Produced; needs revision | [`rfcs/MPA-RFC-1_Spec-Object.md`](../rfcs/MPA-RFC-1_Spec-Object.md) |
| RFC-S block-in (Scale Management) | Block-in level | [`rfcs/MPA-RFC-S_Scale-Management_Block-In.md`](../rfcs/MPA-RFC-S_Scale-Management_Block-In.md) |
| v9 correction notes | Paste-ready (held in chat history) | — |
| Architectural block-in | This document | [`architecture/MPA_Architectural_Block-In.md`](MPA_Architectural_Block-In.md) |
| RFC-2 (FDR signatures) | Not started | — |
| RFC-3 (consistency & completeness) | Not started | — |
| RFC-V (vocabulary) | Not started | — |
| Realizer interface RFC | Not started | — |
| Surface-code reference driver | Not started; v9 has the by-hand version | — |
| Habit-extinction reference target | Identified, not characterized | — |

---

## Next session priorities

In recommended order:

1. **Apply v9 notation correction.** Small, paste-ready.
2. **RFC-1 v0.2** — *test of thin-RFC discipline.* Incorporate the five foundational principles as a foundational section. Rewrite the body against the six-field template (Object / Shape / Invariants / Operations / Falsifiers / Pointer). Target: ≤2 pages including appendices. If RFC-1 — the heaviest case, foundational and fully fielded — fits, the rest of the RFC sequence will fit easily.
3. **RFC-S thin pass.** RFC-S v0.1 is a 5,800-word block-in scoped at standards-body weight (170-200 page projection). Under thin-RFC discipline, it should rewrite to half a page or so per major object (connection space, gamut, intents, mapping, profile, pipeline, validation). The intent enumeration and round-trip protocol are the load-bearing pieces; everything else points at them or at v9.
4. **Surface-code reference driver write-up.** v9 Appendix F + §5 Figure 1 supply the content; the write-up makes it the canonical reference driver against which others are validated. Scope, translation field, demand envelope, signature target outputs, versioning.
5. **RFC-2 outline.** FDR-signature contract. Thin-RFC form from the start.
6. **Habit-extinction reference target characterization.** What data is canonical, what observer-position range the driver supports, what signature targets are expected.

Items 1–3 should land before items 4–6; the latter depend on the former being stable.

---

## Closing note

The session moved from "build the translator" to "specify the input contract first" to "specify the input contract with color-management and scale-management discipline." A follow-on session sharpened it further with three more principles — demand-bounded sufficiency, the singular working-space path, and thin-RFC discipline — none of which redirects the program; each is a tightening that closes off a way the framework could grow weight it doesn't need. The architecture as it now stands is the same shape v9 had been pointing at, with the implicit principles made explicit and load-bearing. RFC-1 v0.2 ties the five commitments together at the spec-object level and tests whether the thin-RFC discipline holds for the foundational object. Subsequent RFCs build outward from that foundation.

The framework has firmed up substantially this session. The next session inherits a coherent architecture rather than a collection of tightening proposals.

The Maya analogy is doing more work than first appearance suggests: it's not just an aesthetic for how artists want to work, it's a structural recognition that scale-relativity in v9 was always pointing at observer-driven scale management without the language to name it. Naming it is the move that converts an implicit principle into an architectural commitment — and the commitments made early are the ones that don't get baked in wrong.
