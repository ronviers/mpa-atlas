# MPA — The Lift Move (object → space of objects), recorded

> **Status: staged in `docs/`. Methodology record of a move that produced a still-staged
> artifact ([`character_manifold.md`](../framework/character_manifold.md), promoted 2026-06-01).** Written in the register of
> [`framework/character_fdr_treatment.md`](../framework/character_fdr_treatment.md) — but held out of
> `framework/` because the move's output is itself not yet earned into canonical.

**Scope.** How the morphospace lift was made: the operation that turns a document about
*one object* into a document about *the space of such objects and their relations*, the
discipline that guards it step by step, what it imports versus owns — with
`character → character′` as the worked example, and the observation that the move is
**iterable**, the second iteration being where MPA would contribute.

**Notation.**

| symbol | meaning |
|---|---|
| `ℭ`, `ℭ_n` | character-space; its `n`-node stratum (`gl(n,ℝ)` tangent) |
| `χ` | a character — a point in `ℭ` |
| `T_χℭ` | tangent space at `χ` (the deformation algebra, read as geometry) |
| `⊗ : ℭ×ℭ→ℭ` | the coupling/closure map — propinquity-induced rewiring |
| `′` | the lift (point → space); `Tℭ` is the tangent-bundle reading |
| `[est]` / `[bespoke]` / `▶ INTAKE` / `⚠ CAVEAT` | provenance + research markers (as in `character_manifold.md`) |

Residual rule (as in the engine): what is not pointed at an import is owned.

---

## 1. The lift, as an operation

One sentence: **read each quantity in a document-about-an-object as structure on the space
of such objects and their relations.** It is *functorial* — the same reading applied
uniformly to every section, not a different trick per section. It is **single** (one pass)
iff the source is already coordinatized by quantities that are *already* space-structure.
`character.md` qualified: `a = ln(G₀/L)` was already a coordinate, `gl(3,ℝ)` was already a
tangent algebra. The lift re-points an existing, uniform document at the manifold; it
invents nothing.

*Guards: arbitrary re-skinning.* If the source is not pre-coordinatized, the lift
fragments into per-section inventions and is not one move.

## 2. The discipline — what was done, each step guarding a failure mode

(Parallel to `character_fdr_treatment.md` §1.)

1. **Confirm pre-coordinatization.** Find the quantities already shaped like manifold
   structure (`a` → coordinate; `gl(n,ℝ)` → tangent algebra). *Guards forced lift — if none
   exist, the move is not available; stop.*
2. **Fix one operation, write it once.** object → space-of-objects, applied uniformly.
   *Guards per-section invention — a separate device per section is not a single move.*
3. **Lift each quantity by the same reading.** point · tangent space · the two sectors ·
   the relative-coordinate (proximity) rules · path (coarse-graining) · degeneracy locus
   (marginal point) · boundary (isolation) · protected coordinates (identity). *Guards
   hand-waving — a quantity that won't lift is a named gap, not a glossed one.*
4. **Mark provenance at every lifted node.** `[est:]` with its precondition · `[bespoke]` ·
   `▶ INTAKE`. *Guards floating — a lifted reading with no receipt is metaphor (the
   generative-metaphor failure mode); the marker forces it into the open.*
5. **Hold out of canonical until the marked imports' preconditions are verified.** *Guards
   mis-import — leaning on machinery the substrate has not earned (the naive-grab failure).*
6. **Strip substrate-specific framing.** The lift is substrate-general or it is not the
   move. *Guards illustrative capture — the documented history of anthropocentric examples
   steering the framework wrong.*

**Meta-observation** (parallel to `character_fdr_treatment.md` line 41 — *working the translation
updated the framework*): recording this move surfaced that it is **iterable**, and that the
second iteration — the lift applied to `ℭ` itself — is where the residual stops being
re-read imports and becomes a proposal. *Working the lift relocated the program's sense of
where its own contribution sits.*

## 3. Worked example — `character → character′`

| `character.md` | `character′` reading | marker |
|---|---|---|
| control parameter `a` | radial coordinate on `ℭ` | `[est: KAK]` |
| deformation algebra `gl(3,ℝ)` | tangent space `T_χℭ` | `[bespoke]`, RPS-instanced |
| two degrees of freedom | metric / topological tangent sectors | `[est: DFS]` |
| frustration / protected current | discrete winding of the relative vector | `[est: balance]` |
| coupling (new) | sector-wise rules on `δχ` (Families A/B/C) | mixed |
| coarse-graining / RG | a path on `ℭ` | `[est: RG]` |
| marginal point | locus where `ℭ` degenerates | `[est: Fenichel]` |
| measurement / open interval | isolation = the boundary of `ℭ` | `[est]` |
| (implicit) | identity = the protected coordinates, sustained | `[bespoke]` |

Full artifact + its receipt ledger: [`character_manifold.md`](../framework/character_manifold.md).

## 4. The move iterated — `character′′`

`⊗ : ℭ×ℭ → ℭ`: the output of a coupling event is *itself a character*. So character-space
is **closed under coupling**, and applying the lift a second time to `ℭ` does not escape to
a meta-space — **it folds back onto `ℭ`.** The "space of character-spaces" is the directed
system of strata `{ℭ_n}` whose arrows are the coupling maps `ℭ_n → ℭ_{n+1}`; those arrows
*are* coupling (read up = emergence) and coarse-graining (read down). The folding-back is
the content: **emergence is internal to character-space — the non-additivity of the up-map,
not a jump to a higher ontology.**

Full second application: [`character_composite.md`](character_composite.md). It is
**doubly gated** — on `character_manifold`'s receipt ledger first (now discharged, Gate 1), then on its own bespoke
bindings — and it is the layer where MPA stops re-reading and proposes.

## 5. Falsifier of the move

The lift is a re-coordinatization, not a truth claim, so it "fails" only two ways, both
caught by Step 4's markers:

- **Fragmentation** — no single operation covers every section → the source was not about
  one coherent object, and the "single move" claim was false.
- **Floating** — a lifted node never acquires a receipt → that node was metaphor, and the
  lift has laundered metaphor as geometry. (This is the sharper risk at the second
  iteration, which is the least imported.)

---

*Imports.* The lift's *form* is standard mathematics — categorification / passage to a
moduli space / jet-prolongation. The residual MPA owns is the recognition that
`character.md` was pre-coordinatized to admit the move in a single pass, the specific
section-by-section readings, and the gap map those readings expose. `character′`'s own
imports are ledgered in [`character_manifold.md`](../framework/character_manifold.md).
