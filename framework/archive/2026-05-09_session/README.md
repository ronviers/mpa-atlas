# MPA Framework

Source-of-truth documents for the MPA framework's two analytical domains: **structural** (v9 lineage) and **character** (character-domain extension). The two domains are peers — neither downstream of the other. They share mathematical neighbors (driven-dissipative non-equilibrium steady states, Haken laser threshold, fluctuation-dissipation, time-frequency uncertainty) but cover distinct subject matter.

## Documents and roles

Per-domain three-layer pattern: operational spec, rigorous apparatus, public companion.

| Domain | Spec (operational) | Apparatus (rigorous) | Companion (public) |
|---|---|---|---|
| Structural | [`v9_compressed.md`](v9_compressed.md) | conflated with spec | [v9 unabridged](v9_MPA_A_Driven-Dissipative_Synthesis_with_Boolean_Limit.md) |
| Character | [`mpa character framework.md`](mpa%20character%20framework.md) | [`mpa character holding apparatus.md`](mpa%20character%20holding%20apparatus.md) | (none yet) |

Methodology and translation documents:
- [`translating FDR.md`](translating%20FDR.md) — worked example of the structural→character translation method (six-step process applied to force-deformation response). Origin document for the character-side translation methodology; the framework and apparatus evolved past it, but it remains the methodological reference.
- [`translating FDT.md`](translating%20FDT.md) — six-step translation applied to fluctuation-dissipation (statistical-physics FDR/FDT). Per-coherence-regime FDT predictions (imposed, emergent, critical) refine v9's structural-regime universality invariants. Disambiguation: cFDR (force-deformation, demonstrated below) vs cFDT (fluctuation-dissipation, the focus of this translation).
- [`cFDR demonstration.md`](cFDR%20demonstration.md) — operational use of cFDR (force-deformation) on common vocabulary; surfaces the three structural assumptions most often smuggled in.
- [`cFDT first analysis.md`](cFDT%20first%20analysis.md) — first contact between cFDT predictions and real data (mpc-glass and mpc-quantum sweep_g, smoke-scale). Result: cFDT's verbal predictions need refinement before they're testable; the framework's general claim survives. Recommendations for production-scale follow-up are in the document.

## Asymmetries (artifact, not design)

- **v9 conflates spec and apparatus.** Built before the spec/apparatus split was deliberate. The thin-RFC discipline in [`../CLAUDE.md`](../CLAUDE.md) notes "rigor lives in v9 compressed and apparatus docs."
- **Character-MPA has no public companion yet.** The framework spec carries part of that role (§1 motivation, §11 relation to existing work) but is operational, not introductory.

These are stage-of-development artifacts. Filling them is optional and pursued only when the gap actually matters (e.g., when an outsider-facing introduction to the character domain is needed).

## The two domains

- **Structural-MPA (v9 lineage)** covers what something is *made of* — vertex/edge/subgraph regimes, operators ($C, S, K, R$), Boolean limit, capacity bounds, FDR signatures, the Compression Axiom. Foundational vocabulary: trail vector, drive $D$, observer kernel $\tau_{obs}$, three-regime threshold structure ($c$/$s$/$r$).
- **Character-MPA** covers what something is *being, continuously* — substrate vs coherence, holding, chit-rate, three coherence types (fixed-point, limit-cycle, strange-attractor), three coherence regimes (imposed, emergent, critical), four operating-state dimensions (basin volume, chit-rate, $Q$, headroom), unified failure-mode taxonomy. Foundational vocabulary: substrate, coherence, mode, supply rate $P$, holding rate $g$, decay rate $\kappa$.

The domains are not in tension. Most real phenomena require analysis in multiple domains simultaneously; the framework provides each domain its native vocabulary and apparatus.

## How to read

- **For character-domain work:** [`mpa character framework.md`](mpa%20character%20framework.md) first; turn to [`mpa character holding apparatus.md`](mpa%20character%20holding%20apparatus.md) when derivation, full vocabulary, or rigorous foundations are needed.
- **For structural-domain work:** [`v9_compressed.md`](v9_compressed.md) is the dense source. Use the unabridged companion for prose context, prior-art mapping, and historical lineage. Do not lean on the unabridged for operational lookups.
- **For MPA orientation in general:** this README, then both specs in either order — they are peers and the reading order does not matter.
- **For methodology / how to extend the framework with new mathematical sources:** [`translating FDR.md`](translating%20FDR.md) (six-step structural→character translation) and the recent character-side adoption history (laser physics, dynamical systems, nonequilibrium thermodynamics, dissipative structures, information theory, synchronization, SOC, control theory, active matter, queueing theory — see apparatus §17, §18, §19).

## Precedence

Spec wins over apparatus; apparatus wins over companion. Within v9 specifically, v9_compressed wins over the unabridged version on any conflict. Within character-MPA, the framework spec wins over the apparatus on conflict.

## Working discipline

- [`../CLAUDE.md`](../CLAUDE.md) — repo-level discipline. Thin-RFC for protocol surfaces (gross-underengineering by design at exchange surfaces). The framework documents themselves are *not* governed by thin-RFC discipline; rigor lives here.
- User-level memory (auto-loaded each session) carries session-spanning preferences and cross-session conventions.
