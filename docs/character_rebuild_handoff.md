# Character — scientific-register rebuild: roadmap & handoff

> **Live baton.** The plan to rebuild the **public-facing** Character framework on the
> *scientific register* — the register exemplified by [`framework/character.md`](../framework/character.md),
> not the engine's coined-noun register. Self-contained: a cold reader needs only this file plus the
> docs it names. **Read `character.md` first** and match its register exactly; that is the whole point.

---

## 0. The decision, and why

**Decision (Ron, 2026-06-01):** the framework's public face is rebuilt on the **scientific register**.
`character.md` becomes the basis; the **engine's register is retired from the public face** (the
engine stays internal — see §2). The public home is the **`character-framework`** GitHub repo
(`github.com/ronviers/character-framework`), currently hollowed to a stub.

**Why (the load-bearing reason):** register *is* legitimacy here. `character.md` reads as a physics
paper — standard terms, every import named, the central claim a falsifiable data-collapse test, and
an explicit closing section ("everything else is a renaming; the residual is the forcing and the
umbrella term"). A reviewer can evaluate it. The **engine** reads as a private language — `ch`,
`chit`, holding, trail, fraying, `k_frust`, "the Wall," `c/s/r` — and a reader cannot tell depth from
idiosyncrasy. *That ambiguity is the "not even wrong" smell.* The scientific register removes it; it
is what makes the claim falsifiable-in-public. This is not cosmetics — checkability is the legitimacy.

**Context a cold reader needs:**
- A scientific-register switch happened in a prior session (it produced `character.md`) but **did
  not propagate** to the rest of the corpus or to later sessions. This handoff exists so it
  propagates this time. Do not assume any other doc is in the right register.
- **Zenodo was retracted** (~2026-05-29; DOI 10.5281/zenodo.20357550). Re-publication needs Ron's
  explicit go ([[project_mpa_publishing]]). The retraction was about an artifact that claimed more
  than it had — so the honest-scope rules (§5) are load-bearing, not decoration.
- `character-framework` was created with a value-forward primer, then **hollowed out** (that primer
  was old-register debris). It now holds only a stub README + LICENSE.
- **Nothing substantive is being redone.** The results (both gate closures, the binding-by-import,
  the DNA-NESS real instance + its full-nonlinear cross-check) are register-independent and stand.
  But this is **more than a storefront**: the rebuilt scientific document becomes the **new
  internal / dev source of truth** (§2) — dev continues on it, and the engine register is retired.
  What is redone is the *register*, not the *results*.

## 1. The register (non-negotiable rules, distilled from `character.md`)

1. **Standard units only.** Bits `= ln 2 nats = k_B ln 2` (the Landauer quantum). **The coined "ch"
   unit did not survive — never reintroduce it.** ("chit" as a *quantity* = `ln(G₀/L)` is fine, but
   prefer "affinity `a`" / "log gain-to-loss ratio" in the public register.)
2. **Name every import** to its established attribution (de Donder/Onsager/Crooks, Haken,
   Galton–Watson, Cugliandolo–Kurchan, Barato–Seifert/Horowitz–Gingrich, Harada–Sasa,
   Toulouse/Harary, May–Leonard/Schnakenberg, Wilson–Polchinski, Banach/Krein–Rutman, Fenichel,
   Kingman, Caputo/Mittag-Leffler, Kato, Kolmogorov). Source: [`character_prior_art.md`](../framework/character_prior_art.md).
3. **No coined-noun thicket.** Avoid holding, trail, fraying, killshot, "the Wall," `k_frust`-as-jargon,
   `c/s/r`-as-jargon. Use standard terms (cycle affinity, frustrated cycle, marginal point /
   loss of normal hyperbolicity, threshold regimes). Keep only the genuinely-needed coinages —
   **character** (the umbrella) and **the forcing** (onto one parameter) — and define them in
   standard terms. **Also avoid the word "emergence"** — the abused noun `character.md` itself flags;
   say what is meant precisely (composition under coupling, coupling-induced minting, the closure,
   non-additivity).
4. **Lead with the testable claim**; state falsifiers as kill conditions on named substrates.
5. **Honest scope** (§5) stated plainly: the contribution is the *forcing onto one parameter* + the
   *over-determination that makes the alignment a test* + the *composition reading* (what coupling
   mints). Everything else is imported — say so.
6. **Measurement discipline:** observables in open intervals; boundaries `{0,1,∞}` only as limits;
   no inert constants (every quantity flows with the operating point).
7. **Density by function (Ron's calibration 2026-06-01).** The **trio** (`character.md` +
   `character_manifold.md` + `character_composite.md`) is the canonical statement — read **tight**,
   `character.md`'s density, every line load-bearing. **Support docs** (`character_fdr_treatment.md`,
   `character_translation_method.md`) are depth/derivation — lengthy prose is *correct* there (they
   show the work), but tight-for-a-depth-doc (no slack). Don't force the trio's density on a
   derivation, or a derivation's length on the trio.

## 2. One register, not two — the architecture (CORRECTED, Ron 2026-06-01)

An earlier draft of this section split the world into a clean *public* register (`character-framework`)
over a dense *internal* engine register (`mpa-atlas`) kept as the back room. **That is wrong — and it
is precisely what failed to propagate.** The scientific register was meant to become the **new
internal / dev register**; instead dev kept running on the engine's coined-noun register, and the two
diverged. Do not re-create that split.

**There is one register going forward: scientific.** The rebuilt scientific-register document is
**both the public face and the internal / dev source of truth.** Development continues **on the
public-facing document** — new instances, refinements, eventually the alive loop — written in the
scientific register. The engine's coined-noun register is **retired to legacy** (frozen lineage, not
a maintained parallel).

Consequences (integration points; recommendation + Ron-confirm where noted):

- **Home (CONFIRMED, Ron 2026-06-01).** The scientific corpus is canonical in **`character-framework`**
  (the live home — public *and* dev), in a new **`framework/`** folder. **`mpa-atlas` and every
  `mpa-*` sibling are legacy**, frozen as lineage. Sequencing (Ron): **stand up the new `framework/`
  structure first** — a stable SoT — before relying on it; the legacy repos stay frozen-in-place,
  nothing is torn down, they just stop being where the work lives.
- **No parallel maintenance.** New dev lands in the scientific document **only**. **Do not edit the
  engine going forward** — freezing it is what prevents the divergence that caused this. (This
  *supersedes* the earlier "engine is the kept internal corpus.")
- **`conform` transition.** `mpa-conform` reads `mpa-atlas/framework/character_engine.md` for its
  substrate-conditional reading rules + class definitions. The engine is **frozen, not deleted**, so
  `conform` keeps reading the frozen copy **during the transition**; it repoints to the scientific
  SoT once that document is operationally complete enough to carry those rules. A deliberate
  transition, not a flag-day.
- **Scope consequence (important).** Because the scientific document is now the *dev SoT*, it must —
  over continued dev — absorb the engine's *operational* content (the two-mode kernel, the regime
  classifier, the gFDR signatures, the reading rules `conform` needs) **in scientific register**.
  The current rebuild (§4) is the **seed**; dev grows it into operational completeness. The rebuild
  is not a presentation layer over a separate corpus — it is the first increment of the new working
  source of truth.

## 3. Source materials (what to mine, from where)

| source (in `mpa-atlas/framework/` unless noted) | role | register caveat |
|---|---|---|
| `character.md` | **the basis** — point-level (one NESS), already clean | mostly done; update validation line (§4) |
| `character_composite.md`, `character_manifold.md` | source for the two lifts (the trio's other two) | OLD register — re-express, don't copy |
| `character_fdr_treatment.md` | source for the two-frame method behind the lifts | OLD register (uses dead `ch`, engine keys) — **mine for rigor, do not anchor** |
| `character_prior_art.md` | the named attributions (rule §1.2) | reference |
| `character_receipts_engine.md`, `character_frontier.md` | what's earned vs provisional (honest-scope §5) | reference |
| DNA-NESS instance: `mpa-conform/scripts/emergent_identity_dna_ness.py` + `dna_ness_crosscheck.py`; provenance `docs/dna_ness_source.md` | the **one real instance** (world-vindication) | write up in scientific register |

## 4. The rebuilt public framework — the doc plan

1. **`character.md` (basis)** — migrate into `character-framework`, essentially as-is (it is already
   in register). Two edits: (a) **validation line** — it says "awaits experimental data"; update to
   "one real instance at the composite layer (a fuel-driven DNA reaction network; Nicholas et al.
   2025), with synthetic validation elsewhere"; (b) light polish for any residual coined term.
2. **`character_manifold.md` (the space)** — rewrite the morphospace lift in scientific register: how
   characters sit next to each other (proximity), and the two sectors of a character — the continuous
   *population* sector and the discrete *circulation* sector — as the tangent structure of the space.
   Mine the old-register `character_manifold.md` for content, `character_fdr_treatment.md` for the
   two-frame method. Geometry of the space; **do not use "emergence."**
3. **`character_composite.md` (the closure)** — rewrite in scientific register: composition under
   coupling (`⊗ : ℭ×ℭ → ℭ`), the **minting claim** (coupling produces a protected circulation neither
   part had — a discrete graph-flux invariant, sustained by drive, not stored, not Chern-like), the
   two-frame method behind it, and the **one real instance** (the DNA-NESS: a detailed-balanced DNA
   hybridization cycle driven by RNase-H fuel hydrolysis; minted affinity; the current collapses when
   the fuel is cut — observed experimentally; confirmed against the full non-linear model to
   cycling-rate ratio 1.002). State the idealizations (N=3 reduction, chemostat) plainly. **The
   most-exposed layer — clean *and* honestly scoped, and NOT the word "emergence"** (composition /
   coupling-induced minting / the closure).
4. **`README.md` (landing)** — accessible front door (value-forward but honest): what a character is,
   why it's interesting (a *testable* account of what coupling mints — avoid "emergence"), the
   unification, "if it continues to check out" (conditional implications), honest scope. **Points at
   the trio (`character.md` · `character_manifold.md` · `character_composite.md`) as "start here."**
   Reuse the hollowed primer's value-forward content shape; fix its register and its link targets.
5. *(optional)* a self-contained **imports list** in `character-framework` so the repo carries its own
   provenance (or link `character_prior_art.md`).

## 5. Honest-scope requirements (carry these — they are load-bearing post-retraction)

- **One** real instance (DNA-NESS); the rest synthetically vindicated.
- The central **β data-collapse test has not been run on real data**.
- The **composite layer** (the closure) is the **most exposed**; write it clean but with idealizations
  stated (N=3 reduction of a nonlinear CRN, chemostat, enzyme QSS). Avoid "emergence" throughout.
- The **alive loop** (self-sustaining recursive circulation — the deepest target) is **named,
  parked, work continues** — not claimed.
- The contribution is **small and honest**: a coordinate system + a falsifiable test + the composition
  reading (what coupling mints) + one receipt. Be at peace with that scope — it is *why* it is less
  "not even wrong."
- Do not overclaim. When an outside (yes-and) model supplies implications, downgrade them to what is
  earned (the prior pattern: "architecture complete" → "built end to end"; "mechanized the
  definition of identity" → "a candidate, precise enough to be wrong, instanced once").

## 6. Pitfalls / traps (so they do not recur)

- **The register did not propagate before.** Be explicit; READ `character.md` first; match it.
- **The dead `ch` unit** — do not reintroduce. `character_fdr_treatment.md` still uses it; that is a
  source caveat, not a model.
- **`fdr_treatment` is old-register** (engine keys, `ch`, "fraying") — mine the *derivation*, drop
  the register.
- **The engine's pre-existing uncommitted WIP** (a c-regime τ_obs line in `character_engine.md`) —
  leave it untouched; do not entangle it in commits (it has been excluded all along).
- **Do not *edit* the engine going forward — freeze it.** Parallel maintenance of two registers is
  exactly the divergence that caused this. The engine is frozen-legacy (not deleted): `conform` reads
  the frozen copy during the transition (§2), then repoints to the scientific SoT. New dev lands in
  the scientific document only.
- **The dead-`ch` references in the live corpus** (engine §0 ch/chit nouns, `character_applications`,
  frontier batteries, README/CLAUDE inventories) are reconciled when the *internal* corpus gets its
  own register pass — NOT required for the public rebuild, but logged: the public face simply does
  not use them.
- The frozen tag **`character-v0.1`** captured the old corpus; cut a **new tag** for the clean public
  snapshot when the rebuild lands.

## 7. Sequence

1. **[DONE]** Hollow out `character-framework` (stub README; commit `70b3981`).
2. Migrate `character.md` → `character-framework`; update the validation line (§4.1); light register polish.
3. **[support docs DONE]** `character_fdr_treatment.md` + `character_translation_method.md` refactored
   into `character-framework/framework/` at depth-density (§1.7). Then rewrite the **trio's**
   `character_manifold.md` (the space) and `character_composite.md` (the closure) — **tight,
   `character.md` density (§1.7), NOT depth-density** — the two lifts + the minting claim + the
   DNA-NESS instance + idealizations; **no "emergence."** **Look at `character_composite.md` together**
   (most-exposed layer).
4. Write the README landing (§4.4) — value-forward, honest, pointing at the trio.
5. *(optional)* the self-contained imports list (§4.4).
6. Tag `character-framework` **`v0.1`** (the clean public snapshot).
7. **Establish the SoT transition (§2):** freeze the engine as legacy (no further edits); record that
   dev now lands in the scientific corpus; plan the `conform` repoint for when the scientific document
   is operationally complete. (`mpa-atlas/framework` → legacy is a Ron-confirm point.)
8. **(Later, deliberate, Ron's go)** the re-publication decision.

## 8. Done-when

`character-framework` presents the framework **entirely in the scientific register** —
the trio — `character.md` (basis, validation updated) + `character_manifold.md` (the space) +
`character_composite.md` (the closure + the DNA-NESS instance) — + README (landing): no coined-noun
debris, no "emergence," honest scope throughout, every import named, self-contained
(no dependence on old-register docs). And this corpus is **established as the new internal / dev
source of truth**: the engine register is frozen-legacy in `mpa-atlas`, new dev lands only in the
scientific document, and the `conform` dependency transition is planned (§2). One register, public
and internal, going forward — the divergence that caused this cannot recur.

**Cross-refs:** [`character.md`](../framework/character.md) (the basis/register) ·
[`character_fdr_treatment.md`](../framework/character_fdr_treatment.md) (lift method, mine for rigor) ·
[`character_composite.md`](../framework/character_composite.md) (the closure — composite source) ·
[`character_prior_art.md`](../framework/character_prior_art.md) (the named imports) ·
`mpa-conform/scripts/dna_ness_crosscheck.py` + `docs/dna_ness_source.md` (the real instance).
