# Discipline: thin

Working in this repo means working under **thin-RFC discipline.** This document names it explicitly so future sessions don't accidentally revert to standards-body defaults. Read this before touching any RFC.

---

## Principle

Exchange surfaces are written at gross-underengineering resolution by design. Half a page per object is the target. **Not less rigorous, not phoned-in** — deliberately thin *where standards bodies are thick*. The framework underneath ([v9 compressed](framework/v9_compressed.md)) is dense (~12KB, derivation-heavy); the protocols on top are thin; the total weight is correctly distributed.

## Justification

> *It was never brittle if it never broke.*

Brittleness is a measurement against actual stress. We have no legacy interop, no multi-stakeholder negotiation, no N>1 implementer divergence to defend against. Thin protocols that hold under the stress they encounter are correctly underspecified, not negligently so. When something breaks, we thicken that spot only, that break only, with a named debt-marker.

The defensive instincts that grew ICC v4 to ~120 pages, the IETF RFC tradition of MUST/SHOULD/MAY granularity, the 170-200-page projection in [RFC-S v0.1](rfcs/MPA-RFC-S_Scale-Management_Block-In.md) §12 — all real responses to forces that don't apply here yet. We don't import them prophylactically.

## Test

Every RFC carries a **page-budget self-check** at the end. Targets:

| RFC | Page budget |
|---|---|
| RFC-1 (spec object — foundational, fully-fielded) | ≤3 pages |
| RFC-S, RFC-2, RFC-3, RFC-RI | ≤1 page (½ page where the object admits it) |
| RFC-V (vocabulary) | ½ page |

Growth past target requires an explicit **debt-marker** in the document naming:
1. What force pushed past brevity (concrete, not "for completeness")
2. The revert-when-force-passes commitment

A debt-marker without revert conditions is not a debt-marker; it's surrender.

## The six-field template

Every RFC follows this structure:

1. **Object** (1 sentence) — what artifact this governs
2. **Shape** — typed declaration / schema
3. **Invariants** (numbered, ≤7) — what must always be true
4. **Operations** — what you can do with it, what they preserve
5. **Falsifiers** — what makes a candidate invalid
6. **Pointer** — which v9 sections carry the formal derivation

See [RFC-1 v0.2](rfcs/MPA-RFC-1_Spec-Object.md) for the canonical instance.

## Where the rigor actually lives

The thin protocols work because the rigor is elsewhere:

- **v9 compressed** → formal derivation, operator algebra, theorems, capacity bounds, FDR signatures, Compression Axiom
- **Architectural block-in** → cross-cutting decisions, the five foundational principles, multi-RFC framing
- **Mechanical validation** (FDR round-trip checks, Theorem-9 checks, capacity envelope checks) → enforcement
- **The RFC itself** → exchange contract, nothing else

If you find yourself writing derivation, motivation, or alternative-considered prose inside an RFC, it belongs in v9 or the block-in, not here.

## Forces pushing toward heavyweight (resist)

These are the rationalizations that grow protocols from half a page to dozens:

- *"What if a future implementer..."* — there is no future implementer. Single author per artifact. We version when one arrives.
- *"For completeness we should enumerate..."* — completeness lives in v9. Pointers, not duplication.
- *"It would be safer to spec the edge case..."* — edge cases live as compactification points, named once. Defense lives in mechanical validation, not in prose.
- *"MUST / SHOULD / MAY granularity..."* — language of multi-stakeholder negotiation. We have one author. Declarative writing suffices.
- *"This [Provisional] tag will help future maintainers..."* — it's a note-to-self disguised as a spec annotation. Move to an "Open" appendix or to v9's open-questions list.

When you notice yourself reaching for one of these, that's a signal: stop, name the force, check whether it's actual stress (something broke) or anticipated stress (something might).

## When tempted to thicken

1. **Stop.** Don't add the prose.
2. **Name the force.** Concrete, falsifiable. "Implementer X tried to do Y and got Z" is a force. "Someone might..." is not.
3. **If the force is anticipated, not actual:** do not thicken. The discipline says to wait for the break.
4. **If the force is actual:** thicken that spot only. Add a debt-marker comment naming the break and the revert condition. Do not generalize the fix beyond the break.
5. **Update this document** if a new resistible-force pattern emerges from real experience.

## Handoff completion discipline

When a handoff's deliverable lands, **delete the handoff in the same commit that lands the deliverable.** `architecture/handoff_*.md` answers "what work remains"; if the answer is "done," the file shouldn't exist. Stale handoffs read as live to-do lists, propagate stale companion-links and "(forthcoming)" tags into the RFCs and READMEs that reference them, and load future sessions with phantom work.

If a handoff carries reference value beyond planning (worked example, design rationale, failure-mode catalog), **absorb the durable content into the artifact it informed before deleting** — the RFC, the block-in, the code's CLAUDE.md, this CLAUDE.md. Don't keep the planning shell as a "preserved record"; the lessons live in the artifacts that survive.

**Audit at session start.** First action of every session: list `architecture/handoff_*.md` and ask of each: "is the deliverable still missing?" If no, the file is in the wrong shape — absorb-then-delete before doing anything else. This is the cheapest moment to catch debris; ten minutes here saves a slow drift toward an architecture/ directory that no longer matches the repo's actual state.

This discipline closed three completed handoffs at session 2026-05-08 (`handoff_schema_files`, `handoff_RFC-S_thin-pass`, `handoff_unblock_runs_and_ops`); the same drift had accumulated each because the closing commit landed the deliverable but didn't clean up the planning doc.

## Scope (what this discipline governs and does not)

**Governs:**
- All RFCs (RFC-1, RFC-S, RFC-2, RFC-3, RFC-V, RFC-RI, future RFCs)
- Schema files
- Protocol-adjacent operational documents

**Does not govern:**
- **v9 compressed** — the source of rigor. Allowed to be long because that's where derivation lives. Maintained dense, not thin.
- **v9 unabridged** — public-facing prose-and-prior-art document. Lives in `framework/`. Allowed to lag and to be long.
- **Architectural block-in** — meta-document, allowed to grow as principles consolidate. (But each principle inside should be tight.)
- **READMEs, handoffs** — operational meta, written for clarity over brevity. (Still: short is better.)

If unsure whether something is a protocol or a meta-document: protocols specify *exchange contracts*; meta-documents specify *how we work*. Anything an external implementer would read to populate a spec object is a protocol. Anything only an internal contributor reads is meta.

## Background

- [Architectural Block-In v0.2](architecture/MPA_Architectural_Block-In.md) — foundational principles section (five principles, including thin-RFC discipline as #5).
- [RFC-S v0.2](rfcs/MPA-RFC-S_Scale-Management.md) — worked example of the discipline applied to a section that resisted thinning. RG flow as foundational structure (§0.6); compactification absorbs edge cases (§6); sheaves and coalgebras flagged as Tier-3 reserve (Appendix C). The v0.1 block-in is preserved at `MPA-RFC-S_Scale-Management_Block-In.md` as honest-scope reference.
- [v9 compressed](framework/v9_compressed.md) — operational source of truth. RFCs point here for rigor.

## Origin

The discipline was named explicitly in a session on 2026-05-08, after the user observed that workstations heat-mapped during a day of production traverse a narrow path despite their nominal feature space — and that mature standards (color management's ICC v4, ~120 pages) carry decades of constituency baggage MPA does not have. The framing the user introduced: ***peel*, not scrape.** Peel away the legacy paths down to the singular working path actually used.

The justification phrasing — *it was never brittle if it never broke* — is the user's. It is not a hedge or a slogan; it is the discipline's load-bearing claim about what brittleness means and when underspecification is correct.
