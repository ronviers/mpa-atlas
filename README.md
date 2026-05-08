# mpa-atlas

Protocols and framework documents for MPA (Metastable Propositional Algebra). The canonical theory, the RFC sequence that turns it into a checkable contract, and the architectural commitments that govern how those documents fit together.

mpa-atlas is upstream of every other repo in the constellation. Substrates speak to it (drivers translate substrate-native data into the canonical representation it defines); realizers consume from it (the realizer-interface RFC defines what they receive); the authoring environment ([mpa-character](../mpa-character/)) emits artifacts shaped to its spec-object protocol.

## What's here

- **[`framework/v9_MPA_A_Driven-Dissipative_Synthesis_with_Boolean_Limit.md`](framework/v9_MPA_A_Driven-Dissipative_Synthesis_with_Boolean_Limit.md)** — the canonical theory document. Driven-dissipative synthesis, Boolean as the $D \to \infty$ limit, the meta-ledger tower, the operator algebra $\Sigma = \{C, S, K, R\}$, the Compression Axiom. mpa-atlas is the sole source of truth for v9.
- **[`framework/v9_compressed.md`](framework/v9_compressed.md)** — operating-density compression of v9 for context-bounded reads. Companion artifact, not a substitute.
- **[`architecture/MPA_Architectural_Block-In.md`](architecture/MPA_Architectural_Block-In.md)** — the architectural commitments made when the program shifted from "build the translator" to "specify the input contract first." Color-management discipline, observer-driven scale management, demand-bounded sufficiency. Block-in resolution: right shapes in the right places, surfaces not yet refined. The RFCs refine specific pieces against this block-in.
- **[`rfcs/MPA-RFC-1_Spec-Object.md`](rfcs/MPA-RFC-1_Spec-Object.md)** — RFC-1, the spec-object protocol. The typed configuration $(V, E, \Gamma, D, \tau_{obs}, P)$ and what it means to be a valid instance. v0.1 draft; v0.2 owed (incorporates the foundational principles from the block-in).
- **[`rfcs/MPA-RFC-S_Scale-Management_Block-In.md`](rfcs/MPA-RFC-S_Scale-Management_Block-In.md)** — RFC-S, scale management. Observer-as-camera, no scale-class taxonomy, persistence profile as observer trajectory.

## RFC sequence

| RFC | Topic | Status |
|---|---|---|
| RFC-1 | Spec object | v0.1 (revision owed: v0.2 with foundational principles) |
| RFC-2 | FDR-signature contract | not started |
| RFC-3 | Consistency & completeness | not started |
| RFC-S | Scale management | block-in level |
| RFC-V | Reference vocabulary | not started |
| RFC-RI | Realizer interface | not started |

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
