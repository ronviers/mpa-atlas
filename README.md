# mpa-atlas

> ⚠ **Read [`CLAUDE.md`](CLAUDE.md) before touching any RFC.** This repo operates under thin-RFC discipline — exchange surfaces are written at gross-underengineering resolution by design. Half a page per object is the target. *It was never brittle if it never broke.* Default standards-body instincts (defensive enumeration, MUST/SHOULD/MAY granularity, edge-case prose) are explicitly resisted. The framework underneath ([v9 compressed](framework/v9_compressed.md)) is dense; the protocols on top are thin; total weight is correctly distributed.

Protocols and framework documents for MPA (Metastable Propositional Algebra). The canonical theory, the RFC sequence that turns it into a checkable contract, and the architectural commitments that govern how those documents fit together.

mpa-atlas is upstream of every other repo in the constellation. Substrates speak to it (drivers translate substrate-native data into the canonical representation it defines); realizers consume from it (the realizer-interface RFC defines what they receive); the authoring environment ([mpa-character](../mpa-character/)) emits artifacts shaped to its spec-object protocol.

## What's here

- **[`framework/v9_compressed.md`](framework/v9_compressed.md)** — **the operational source of truth for v9.** Continuously maintained alongside the RFC sequence; every protocol revision reads from this file. Driven-dissipative synthesis, Boolean as the $D \to \infty$ limit, the meta-ledger tower, the operator algebra $\Sigma = \{C, S, K, R\}$, the Compression Axiom, the trail-class metric, per-regime universality invariants. Dense; self-contained (free-standing — the unabridged version is rebuilt from this file).
- **[`framework/v9_MPA_A_Driven-Dissipative_Synthesis_with_Boolean_Limit.md`](framework/v9_MPA_A_Driven-Dissipative_Synthesis_with_Boolean_Limit.md)** — public-facing prose-and-prior-art version. Rebuilt from the compressed file periodically; allowed to lag between rebuilds; not authoritative for operational lookups. If the two files disagree, the compressed file wins.
- **[`architecture/MPA_Architectural_Block-In.md`](architecture/MPA_Architectural_Block-In.md)** — the architectural commitments made when the program shifted from "build the translator" to "specify the input contract first." Five foundational principles: color-management discipline, observer-driven scale management, demand-bounded sufficiency, singular working-space path, thin-RFC discipline. Block-in resolution: right shapes in the right places, surfaces not yet refined. The RFCs refine specific pieces against this block-in.
- **[`architecture/handoff_*.md`](architecture/)** — pending-work planning documents (v9 architectural-backport, habit-extinction reference driver, protocol tool, operations manual, runs and libraries). Each is self-contained for an agent coming in cold. Handoffs are transient (per [CLAUDE.md](CLAUDE.md) §"Handoff lifecycle discipline" — creation rules, consumption-time orphan-content scan, deletion on completion, ≤700-word smell trigger).
- **[`rfcs/MPA-RFC-1_Spec-Object.md`](rfcs/MPA-RFC-1_Spec-Object.md)** — RFC-1, the spec-object protocol. The typed configuration $(V, E, \Gamma, D, \tau_{obs}, P, \langle\text{demand-envelope}\rangle)$ and what it means to be a valid instance. v0.2 (thin-pass; foundational principles inherited from the block-in).
- **[`rfcs/MPA-RFC-2_FDR-Signatures.md`](rfcs/MPA-RFC-2_FDR-Signatures.md)** — RFC-2, FDR-signature contract. The exchange artifact $(\text{object\_ref}, \text{regime\_class}, \text{parametric\_plot}, \text{universality\_tuple}, \tau_{obs}, \text{measurement\_envelope})$, anchored on v9's per-regime universality invariants $\{X_c, \alpha_s, P_s, X_r, N_f\}$. v0.1 thin-pass, no block-in stage.
- **[`rfcs/MPA-RFC-V_Reference-Vocabulary.md`](rfcs/MPA-RFC-V_Reference-Vocabulary.md)** — RFC-V, reference vocabulary. Canonical-label registry for cross-cutting concepts (operators, regimes, universality invariants, intents, compression-axiom symbols) + disambiguation rules ($C$ vs. $\mathcal{C}$; $\epsilon$ vs. $\varepsilon_n$). v0.1 thin-pass.
- **[`rfcs/MPA-RFC-RI_Realizer-Interface.md`](rfcs/MPA-RFC-RI_Realizer-Interface.md)** — RFC-RI, realizer interface. The output-device-transform analog: $R_\text{doc} = (\text{spec\_ref}, \text{intent}, \text{canonical\_snapshot}, \text{signature\_targets}, \text{acceptance}, \text{realizer\_class\_target})$. v0.1 thin-pass; downstream of RFC-1 / RFC-S / RFC-2 / RFC-V.
- **[`rfcs/MPA-RFC-3_Consistency-Completeness.md`](rfcs/MPA-RFC-3_Consistency-Completeness.md)** — RFC-3, consistency & completeness. Cross-artifact predicates that no single RFC owns: C1–C5 (spec ⊆ driver gamut, intent / realizer-class compatibility, persistence-depth bound) + K1 (signature_targets cover spec elements). v0.1 thin-pass.
- **[`rfcs/MPA-RFC-S_Scale-Management.md`](rfcs/MPA-RFC-S_Scale-Management.md)** — RFC-S, scale management. v0.2 thin-pass: RG flow as foundational structure; canonical representation as the fixed-point set of the flow; substrate gamut as the RG trajectory image; five-intent enumeration; compactification-points table replaces per-intent edge-case enumeration.
- **[`rfcs/MPA-RFC-S_Scale-Management_Block-In.md`](rfcs/MPA-RFC-S_Scale-Management_Block-In.md)** — RFC-S v0.1 block-in, preserved as honest-scope reference. Documents the standards-body weight that thin-RFC declines to import; not authoritative for operational lookups.
- **[`reference-drivers/surface-code-qec.md`](reference-drivers/surface-code-qec.md)** — first reference driver. Surface-code QEC translated into MPA's canonical representation, hand-built from v9. Subsequent drivers (substrate-implementation drivers in `mpc-*` repos) are validated against this one via the round-trip protocol of RFC-S §5.

## RFC sequence

| RFC | Topic | Status |
|---|---|---|
| RFC-1 | Spec object | v0.2 (thin-pass; foundational principles inherited) |
| RFC-2 | FDR-signature contract | v0.1 (thin-pass, no block-in stage) |
| RFC-3 | Consistency & completeness | v0.1 (thin-pass) |
| RFC-S | Scale management | v0.2 (thin-pass; v0.1 block-in preserved as honest-scope reference) |
| RFC-V | Reference vocabulary | v0.1 (thin-pass) |
| RFC-RI | Realizer interface | v0.1 (thin-pass) |

The RFC sequence is the substrate-neutral working space's specification. Substrate variation lives in drivers; user-intent variation lives at the realizer-interface intent flags; everything else is one shape per RFC version (no profile branching at the working-space layer).

## Foundational principles (v0.2 lands these)

Three disciplines borrowed from upstream domains, promoted to load-bearing architectural commitments:

1. **Color-management discipline.** Substrate-native / canonical / realizer-output as three layers with declared, named, versioned, swappable transforms between them. Working space is substrate-neutral by construction.
2. **Observer-driven scale management.** $\tau_{obs}$ is the camera. The canonical representation is observer-relative; cross-scale composition is camera motion, not transform invocation; no scale-class taxonomy baked in.
3. **Demand-bounded sufficiency.** The CD-and-human-ears precedent — the framework commits to *enough* representation for the demands placed on it, not maximally faithful to the substrate. **The MPA is not the bottleneck.** Drivers declare a demand envelope; the canonical representation is sized to it.

The block-in document carries the long-form treatment; RFC-1 v0.2 will canonicalize.

## Sibling repos

| Repo | Role |
|---|---|
| [mpa-character](../mpa-character/) | Authoring environment. Emits spec objects against this repo's RFC-1. Formerly "Substrate Synthesizer." |
| [mpa-central](../mpa-central/) | Cross-substrate coordination, library, pre-registrations, RULES.md. Not a parent — a known place. |
| [mpa-brain](../mpa-brain/) | v8 substrate (cognitive architecture). |
| [mpa-visualizer](../mpa-visualizer/) | Cross-substrate renderer. |
| `mpc-quantum` / `mpc-glass` / `mpc-sat` / etc. | Substrate implementations. Drivers translate substrate-native into canonical representation. |

## Discipline

- **One shape per RFC version.** Plurality lives in drivers (substrate-conditional), realizer-interface intent flags (user-intent-conditional), and version succession (time-conditional). Not at the working-space layer.
- **Drift-resistant.** Architectural commitments that get baked in early are the ones that don't get baked in wrong. Foundational principles land in v0.2's body, not just in commentary.
- **Versioned, not branched.** RFC-1 v0.1 → v0.2 → v1.0. No RFC-1A / RFC-1B.
