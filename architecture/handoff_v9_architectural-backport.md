# Handoff: v9 architectural-framing back-port

**Status:** Planning document for the next session's v9 §Foundational-principles addition.
**Audience:** A future Claude (or human) coming into this work cold.
**Companion:** [v9 compressed](../framework/v9_compressed.md), [Architectural Block-In](MPA_Architectural_Block-In.md), [RFC-1 v0.2 §0](../rfcs/MPA-RFC-1_Spec-Object.md), [RFC-S v0.2 §0](../rfcs/MPA-RFC-S_Scale-Management.md).

---

## Goal

Add a §Foundational principles section near the top of `v9_compressed.md` that declares the five architectural principles in v9's voice, so v9 aligns with the principles the RFCs all inherit from the Block-In.

## Context

The five principles — color-management discipline, observer-driven scale management, demand-bounded sufficiency, singular working-space path, thin-RFC discipline — live in the Architectural Block-In §"Foundational principles (consolidated)". They were promoted to foundational *after* v9 stabilized. v9 itself doesn't currently mention them in its body.

Every RFC has a §0 that inherits the principles. v9 — the rigor source — doesn't. Asymmetry: RFCs declare principles that govern the framework that v9 carries the rigor for, but v9 doesn't acknowledge the principles itself. The fix is hygiene: v9 should also declare them, then point at the Block-In for the long-form treatment.

The Block-In §"v9 corrections needed" item 2 flags this back-port as pending, gated on RFC-1 v0.2 + RFC-S v0.2 stability. Both gates passed (both stable). Unblocked.

## What needs to happen

Insert a §Foundational principles section near the top of `H:/mpa-atlas/framework/v9_compressed.md`, after §Setting (currently the first content section after the title block). Suggested form (≤½ page):

```markdown
## Foundational principles

This framework operates under five architectural commitments declared by the [Architectural Block-In](../architecture/MPA_Architectural_Block-In.md):

1. **Color-management discipline.** Three layers (substrate-native / canonical / realizer-output) with declared, named, versioned, swappable transforms between them.
2. **Observer-driven scale management.** $\tau_{obs}$ is the camera; the canonical representation is observer-relative; cross-scale composition is camera motion, not transform invocation.
3. **Demand-bounded sufficiency.** The canonical representation is sized to declared demand. *The MPA is not the bottleneck.*
4. **Singular working-space path.** One canonical-representation shape per framework version; plurality lives in drivers, intent flags, and version succession.
5. **Thin-RFC discipline.** Exchange surfaces are written at gross-underengineering resolution by design. *It was never brittle if it never broke.*

How they thread through the rest of this document:
- §Scale-relativity instances observer-driven scale management.
- §Operators' algebra is closed in the canonical-representation layer.
- §Compression Axiom's trail-class metric $\rho$ is what each RFC's $\varepsilon_n$ semantics inherit at the operator-norm convention.
- §Setting's $D = \Phi^*/\kappa$ is the dimensional framing demand-bounded sufficiency operates under.

Long-form treatment of each principle lives in the Block-In; this section is the declaration in v9's voice.
```

## Failure modes to watch

- **Don't re-derive the principles.** That's the Block-In's job. v9 declares them; Block-In carries motivation and history.
- **Don't add weight beyond ½ page.** v9 is dense by design. This section earns its place by being short and pointed.
- **Don't make subsequent v9 sections depend on the principles section.** v9 should remain readable in any order; the principles section is a frame, not a load-bearing dependency.
- **Don't change existing v9 content.** This is an additive insert, not a rewrite. The principles already implicitly structure v9; the section makes that explicit, no more.
- **Don't update v9 unabridged.** The discipline (per repo CLAUDE.md) is that unabridged is rebuilt from compressed; allow it to lag.

## Completion criteria

- `v9_compressed.md` has a §Foundational principles section after §Setting.
- The section is ≤½ page.
- The section points at the Block-In for long-form treatment.
- Block-In §"v9 corrections needed" item 2 (currently *Pending*) moves to *Closed* with a one-line note pointing at the new v9 section.
- No other v9 content is touched.

## Effort estimate

~15 minutes for a careful agent. Read v9 §Setting for placement context; read Block-In §Foundational-principles for content; write the section; update the Block-In's "v9 corrections needed" entry.

## Why this matters

It's hygiene, but not zero-leverage. After the back-port, v9 reads as a self-coherent rigor document that *acknowledges its own foundations* rather than a document that pre-dates them. Future readers (and future RFC authors) get the principles without having to round-trip to the Block-In on first read of v9.
