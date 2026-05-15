# Discipline: thin

Working in this repo means working under **thin-RFC discipline.** This document names it explicitly so future sessions don't accidentally revert to standards-body defaults. Read this before touching any RFC.

**Companion: program-wide testing methodology.** [`H:/mpa-central/METHODOLOGY.md`](H:/mpa-central/METHODOLOGY.md) is the four-cut testing discipline applied across all mpa repos. The thin-RFC discipline below governs RFC text in this repo; METHODOLOGY.md governs what counts as MPA testing work program-wide. Both share the same brittleness instinct: thin where standards bodies are thick.

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

- **v9 compressed** → operator algebra, theorems, capacity bounds, FDR signatures, Compression Axiom — the *claims*, densely stated
- **v9 receipts** → line-keyed justifications behind the compressed claims (citation, composition, bespoke proof shard, or `unrecovered` marker). The file that makes unabridged reconstruction tractable.
- **cdv1 compressed / cdv1 receipts** → same pattern for the Character projection (continuous physical economics of sustained NESS traversal). The structural projection (v9) and Character projection are complementary readings of the same NESS-substrate phenomenology — both apply to any substrate (glass, QEC, brain, behavioral, future).
- **Architectural block-in** → cross-cutting decisions, the five foundational principles, multi-RFC framing
- **Mechanical validation** (FDR round-trip checks, Theorem-9 checks, capacity envelope checks) → enforcement
- **The RFC itself** → exchange contract, nothing else

If you find yourself writing derivation, motivation, or alternative-considered prose inside an RFC, it belongs in v9 (claims) / receipts (derivations) / block-in (decisions), not here.

**Receipts discipline.** When a session proves, derives, or composes a result that becomes a line in `v9_compressed.md` or `cdv1_compressed.md`, append a justification entry to the matching receipts file *in the same session*. Discipline rules (workflow, type tags, keying) live in [`framework/v9_receipts.md`](framework/v9_receipts.md). Lines whose proof tree is genuinely lost get an honest `unrecovered` marker — no fabricated reconstructions.

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

## Scope (what this discipline governs and does not)

**Governs:**
- All RFCs (RFC-1, RFC-S, RFC-2, RFC-3, RFC-V, RFC-RI, future RFCs)
- Schema files
- Protocol-adjacent operational documents

**Does not govern:**
- **v9 compressed** — the source of structural-domain claims. Allowed to be dense. Maintained dense, not thin.
- **v9 receipts** — line-keyed justifications behind the compressed claims. Append-only; grows with proof activity.
- **v9 unabridged** — public-facing prose-and-prior-art document. Lives in `framework/`. Allowed to lag and to be long. Reconstructible from compressed + receipts.
- **cdv1 compressed / cdv1 receipts / cdv1 unabridged** — same three-suffix pattern for the Character projection (compressed claim-only, receipts line-keyed justifications, unabridged paper).
- **Architectural block-in** — meta-document, allowed to grow as principles consolidate. (But each principle inside should be tight.)
- **READMEs, handoffs** — operational meta, written for clarity over brevity. (Still: short is better.)

If unsure whether something is a protocol or a meta-document: protocols specify *exchange contracts*; meta-documents specify *how we work*. Anything an external implementer would read to populate a spec object is a protocol. Anything only an internal contributor reads is meta.

## Background

- [Architectural Block-In v0.2](architecture/MPA_Architectural_Block-In.md) — foundational principles section (five principles, including thin-RFC discipline as #5).
- [RFC-S v0.2](rfcs/MPA-RFC-S_Scale-Management.md) — worked example of the discipline applied to a section that resisted thinning. RG flow as foundational structure (§0.6); compactification absorbs edge cases (§6); sheaves and coalgebras flagged as Tier-3 reserve (Appendix C). The v0.1 block-in is preserved at `MPA-RFC-S_Scale-Management_Block-In.md` as honest-scope reference.
- [v9 compressed](framework/v9_compressed.md) — structural-domain operational source of truth. RFCs point here for rigor.
- [v9 receipts](framework/v9_receipts.md) — line-keyed justifications for v9 compressed claims.
- [cdv1 compressed](framework/cdv1_compressed.md) — Character-projection operational source of truth. Continuous physical economics of sustained NESS traversal: chit unit, universal two-mode kernel, heat-tax tower, gFDR signatures, five leading-order posits, eleven cross-register identities. Claim-only; substrate-neutral.
- [cdv1 receipts](framework/cdv1_receipts.md) — line-keyed justifications for cdv1 compressed claims.
- [cdv1 unabridged](framework/cdv1_unabridged.md) — public-facing prose-and-prior-art version of the Character projection. Rebuilt from compressed + receipts; allowed to lag between rebuilds.

## Origin

The discipline was named explicitly in a session on 2026-05-08, after the user observed that workstations heat-mapped during a day of production traverse a narrow path despite their nominal feature space — and that mature standards (color management's ICC v4, ~120 pages) carry decades of constituency baggage MPA does not have. The framing the user introduced: ***peel*, not scrape.** Peel away the legacy paths down to the singular working path actually used.

The justification phrasing — *it was never brittle if it never broke* — is the user's. It is not a hedge or a slogan; it is the discipline's load-bearing claim about what brittleness means and when underspecification is correct.
