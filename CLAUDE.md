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

## Handoff lifecycle discipline

`architecture/handoff_*.md` files are *transient* — planning artifacts for pending work. Content that outlives the handoff (architectural commitments, framework reasoning, design rationale, domain-general failure modes, conventions, worked examples of discipline) belongs in its real home — CLAUDE.md, block-in, RFC, code — not in a transient-named file. A future session reading `architecture/` won't grep `handoff_*` for spec content.

Three rules across the lifecycle:

1. **Creation.** A handoff contains only: goal, what to do for THIS task, completion criteria, effort estimate, task-specific failure modes. Anything broader belongs in its real home; the handoff cites it.

2. **Consumption.** Before working from a handoff, scan it actively: "what here would I need if this handoff didn't exist?" Anything answering yes is in the wrong file. Absorb to the right home before starting the work.

3. **Completion.** Delete the handoff in the same commit that lands its deliverable. Absorb any remaining durable content first.

**Audit at session start.** First action: list `architecture/handoff_*.md` and ask of each — deliverable still missing? If no, absorb-then-delete. If yes but the doc reads like it carries content beyond the pending work, restructure before doing the work.

**Smell trigger: ≤700 words per handoff.** Mechanical: `wc -w architecture/handoff_*.md`. Not a hard gate — over-budget triggers the consumption-time scan. At 2026-05-08 the active handoffs ran 661 / 663 / 1073 / 1220 / 1345; the over-budget three were verified as describing rich pending work and earned their words. The same check on `handoff_RFC-S_thin-pass.md` (well over budget at completion time, deleted this session) would have surfaced it immediately.

**Origin.** Added 2026-05-08 after three completed handoffs (`handoff_schema_files`, `handoff_RFC-S_thin-pass`, `handoff_unblock_runs_and_ops`) accumulated in `architecture/` because their closing commits landed the deliverable but didn't delete the planning doc. The first version of this section was completion-time-only and reactive; the lifecycle framing surfaces orphan content earlier, and the word-budget makes the smell automatic.

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
