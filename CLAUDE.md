# Discipline: thin

Working in this repo means working under **thin-RFC discipline.** This document names it explicitly so future sessions don't accidentally revert to standards-body defaults. Read this before touching any RFC.

**Companion: program-wide testing methodology.** [`H:/mpa-central/METHODOLOGY.md`](H:/mpa-central/METHODOLOGY.md) is the four-cut testing discipline applied across all mpa repos. The thin-RFC discipline below governs RFC text in this repo; METHODOLOGY.md governs what counts as MPA testing work program-wide. Both share the same brittleness instinct: thin where standards bodies are thick.

---

## Principle

Exchange surfaces are written at gross-underengineering resolution by design. Half a page per object is the target. **Not less rigorous, not phoned-in** — deliberately thin *where standards bodies are thick*. The framework underneath (the [character_engine](framework/character_engine.md) + [character_receipts_engine](framework/character_receipts_engine.md) set) is dense (derivation-heavy); the protocols on top are thin; the total weight is correctly distributed.

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

- **character_engine** → the *claims* axis: operator algebra, capacity bounds, FDR signatures, Compression Axiom, chit unit, two-mode kernel, heat-tax tower, five posits, adoption catalogue, consolidated falsifiers, regime ontology — densely stated. One phenomenology, two readings (STRUCTURAL + CHARACTER) joined at a shared spine; both apply to any substrate (glass, QEC, brain, behavioral, future).
- **character_receipts_engine** → line-keyed justifications behind the engine claims (citation, composition, bespoke proof shard, or `unrecovered` marker), plus the CORRECTIONS & PROMOTED REFINEMENTS log and the prior-art map.
- **character_frontier** → the maturity ledger / GATES state machine (steeping → sharpening → battery → staked → promoted) that quarantines provisional work.
- **character_prior_art** → the borrowed-results axis: `pa:` keys, what each import borrows and what reading MPA adds.
- **Architectural block-in** → cross-cutting decisions, the five foundational principles, multi-RFC framing
- **Mechanical validation** (FDR round-trip checks, Theorem-9 checks, capacity envelope checks) → enforcement
- **The RFC itself** → exchange contract, nothing else

If you find yourself writing derivation, motivation, or alternative-considered prose inside an RFC, it belongs in character_engine (claims) / character_receipts_engine (derivations) / block-in (decisions), not here.

**Receipts discipline.** When a session proves, derives, or composes a result that becomes a line in `character_engine.md`, append a justification entry to [`framework/character_receipts_engine.md`](framework/character_receipts_engine.md) *in the same session*. Discipline rules (workflow, type tags, keying) live there. Lines whose proof tree is genuinely lost get an honest `unrecovered` marker — no fabricated reconstructions.

**`framework/` is canonical-only — not a scratchpad.** Everything in `framework/` (excluding `archive/`) is active/live canonical: the four-axis set `character_engine.md` (claims, the operational source of truth), `character_receipts_engine.md` (derivations), `character_frontier.md` (maturity ledger), `character_prior_art.md` (borrowed results), plus `character_applications.md`, `character_fdr_treatment.md`, `character_units.md`, and the methodology reference `translating_FDR_steps.md`. Working material — handoffs, planning/blocking docs, drafts, session notes, scratch, pasted exchanges — goes in `docs/`, never `framework/`. Superseded canonical docs go to `framework/archive/`. Do not stage scratch in `framework/`.

## Forces pushing toward heavyweight (resist)

These are the rationalizations that grow protocols from half a page to dozens:

- *"What if a future implementer..."* — there is no future implementer. Single author per artifact. We version when one arrives.
- *"For completeness we should enumerate..."* — completeness lives in character_engine / character_receipts_engine. Pointers, not duplication.
- *"It would be safer to spec the edge case..."* — edge cases live as compactification points, named once. Defense lives in mechanical validation, not in prose.
- *"MUST / SHOULD / MAY granularity..."* — language of multi-stakeholder negotiation. We have one author. Declarative writing suffices.
- *"This [Provisional] tag will help future maintainers..."* — it's a note-to-self disguised as a spec annotation. Move to the character_frontier ledger or character_receipts_engine's open-questions.

When you notice yourself reaching for one of these, that's a signal: stop, name the force, check whether it's actual stress (something broke) or anticipated stress (something might).

## When tempted to thicken

1. **Stop.** Don't add the prose.
2. **Name the force.** Concrete, falsifiable. "Implementer X tried to do Y and got Z" is a force. "Someone might..." is not.
3. **If the force is anticipated, not actual:** do not thicken. The discipline says to wait for the break.
4. **If the force is actual:** thicken that spot only. Add a debt-marker comment naming the break and the revert condition. Do not generalize the fix beyond the break.
5. **Update this document** if a new resistible-force pattern emerges from real experience.

## Scope (what this discipline governs and does not)

**Governs:**
- All RFCs (RFC-1, RFC-S, RFC-2, RFC-3, RFC-V, RFC-RI, future RFCs)
- Schema files
- Protocol-adjacent operational documents

**Does not govern:**
- **character_engine** — the operational source of truth; the full claim set (STRUCTURAL + CHARACTER readings on one spine). Allowed to be dense. Maintained dense, not thin.
- **character_receipts_engine** — line-keyed justifications behind the engine claims, plus the corrections log and prior-art map. Append-only; grows with proof activity.
- **character_frontier / character_prior_art / character_applications / character_fdr_treatment / character_units** — the rest of the four-axis canonical set + applications/treatment/units. Allowed to be dense.
- **Architectural block-in** — meta-document, allowed to grow as principles consolidate. (But each principle inside should be tight.)
- **READMEs, handoffs** — operational meta, written for clarity over brevity. (Still: short is better.)

If unsure whether something is a protocol or a meta-document: protocols specify *exchange contracts*; meta-documents specify *how we work*. Anything an external implementer would read to populate a spec object is a protocol. Anything only an internal contributor reads is meta.

## Background

- [Architectural Block-In v0.2](architecture/MPA_Architectural_Block-In.md) — foundational principles section (five principles, including thin-RFC discipline as #5).
- [RFC-S v0.2](rfcs/MPA-RFC-S_Scale-Management.md) — worked example of the discipline applied to a section that resisted thinning. RG flow as foundational structure (§0.6); compactification absorbs edge cases (§6); sheaves and coalgebras flagged as Tier-3 reserve (Appendix C). The v0.1 block-in is preserved at `MPA-RFC-S_Scale-Management_Block-In.md` as honest-scope reference.
- [character_engine](framework/character_engine.md) — the operational source of truth (claims axis). RFCs point here for rigor. One phenomenology, two readings — STRUCTURAL (discrete operator algebra, finite-$D$ interior) and CHARACTER (continuous driven-dissipative dynamics: chit unit, two-mode kernel, heat-tax tower, gFDR signatures, five posits) — joined at the Boolean→MPA deformation spine. Claim-only; substrate-neutral.
- [character_receipts_engine](framework/character_receipts_engine.md) — line-keyed justifications for the engine claims, the corrections log, and the prior-art map.
- [character_frontier](framework/character_frontier.md) — maturity ledger / GATES state machine. [character_prior_art](framework/character_prior_art.md) — borrowed-results axis. Plus `character_applications.md`, `character_fdr_treatment.md`, `character_units.md`.

## Origin

The discipline was named explicitly in a session on 2026-05-08, after the user observed that workstations heat-mapped during a day of production traverse a narrow path despite their nominal feature space — and that mature standards (color management's ICC v4, ~120 pages) carry decades of constituency baggage MPA does not have. The framing the user introduced: ***peel*, not scrape.** Peel away the legacy paths down to the singular working path actually used.

The justification phrasing — *it was never brittle if it never broke* — is the user's. It is not a hedge or a slogan; it is the discipline's load-bearing claim about what brittleness means and when underspecification is correct.


## Character test suite — spec-stability contract

mpa-atlas is the upstream of the character test framework owned by
mpa-conform. Canonical doc:
[`H:/mpa-conform/conformer/tests/character/README.md`](../mpa-conform/conformer/tests/character/README.md).

The engine's (`character_engine.md`) Character projection (universal two-mode kernel, gFDR signatures,
five-bucket regime classifier, heat-tax tower, chit unit, Compression Axiom)
and RFC-S (scale-management semantics) are the **structures character tests
verify substrates render *as*.** Real measurements are projected through these
structures to land in the framework's canonical space; the shots in
`H:/mpa-conform/output/tests/character/<timestamp>/` are the visible
record of whether that projection holds.

**Spec changes here must round-trip through a character test run before
landing.** This is not a CI gate; it is a discipline. Open a fresh
character-test dailies (`python -m conformer.cli test-character` from
`H:/mpa-conform`), watch the shots in DJV, then ship the spec change.
If a substrate's character changes shape under the new spec, the
shot reveals it before users do.

This pairs with thin-RFC discipline: we do not thicken specs
speculatively, but we also do not change them without watching the
character round-trip.


## Rendering discipline — the water MPA swims in

Canonical doc:
[`H:/mpa-conform/conformer/shot/RENDERING_DISCIPLINE.md`](../mpa-conform/conformer/shot/RENDERING_DISCIPLINE.md).
Established 2026-05-17. Every visual property in every shot maps to
framework data; differentiation, not decoration. The discipline is not
a feature -- it is the medium every visualization in the MPA suite
operates in, and it does not get re-litigated per session.

This repo's contribution to shot rendering is whatever its
character-test contract above already names. Any addition that would
violate the two rules (every property maps to data; differentiation
not decoration) does not land; the discipline does not bend.
