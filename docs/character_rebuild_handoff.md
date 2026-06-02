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
  This rebuild is presentation only.

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
   standard terms.
4. **Lead with the testable claim**; state falsifiers as kill conditions on named substrates.
5. **Honest scope** (§5) stated plainly: the contribution is the *forcing onto one parameter* + the
   *over-determination that makes the alignment a test* + the *emergence reading*. Everything else is
   imported — say so.
6. **Measurement discipline:** observables in open intervals; boundaries `{0,1,∞}` only as limits;
   no inert constants (every quantity flows with the operating point).

## 2. Target architecture (public vs internal)

- **`character-framework` (PUBLIC, scientific register):** the clean home. Houses the rebuilt
  `character.md` (basis), the emergence/lifts writeup, the real-instance writeup, and the README
  landing. Self-contained — the public face must NOT depend on old-register docs.
- **`mpa-atlas` (INTERNAL dev corpus):** `character_engine.md` (+ receipts, frontier, prior-art,
  fdr_treatment, composite, manifold) stay here as the dense working back-room. They do not need
  cleaning to be legitimate — they need to stop being the public face.
- **Do NOT move `character_engine.md` out of `mpa-atlas`.** `mpa-conform` reads it directly
  (`mpa-conform/conformer` deps; see mpa-conform/CLAUDE.md "What this repo reads from"). `character.md`,
  by contrast, has no downstream readers and is the natural seed of the public home.

## 3. Source materials (what to mine, from where)

| source (in `mpa-atlas/framework/` unless noted) | role | register caveat |
|---|---|---|
| `character.md` | **the basis** — point-level (one NESS), already clean | mostly done; update validation line (§4) |
| `character_composite.md`, `character_manifold.md` | source for the lifts + emergence | OLD register — re-express, don't copy |
| `character_fdr_treatment.md` | source for the two-frame method behind the lifts | OLD register (uses dead `ch`, engine keys) — **mine for rigor, do not anchor** |
| `character_prior_art.md` | the named attributions (rule §1.2) | reference |
| `character_receipts_engine.md`, `character_frontier.md` | what's earned vs provisional (honest-scope §5) | reference |
| DNA-NESS instance: `mpa-conform/scripts/emergent_identity_dna_ness.py` + `dna_ness_crosscheck.py`; provenance `docs/dna_ness_source.md` | the **one real instance** (world-vindication) | write up in scientific register |

## 4. The rebuilt public framework — the doc plan

1. **`character.md` (basis)** — migrate into `character-framework`, essentially as-is (it is already
   in register). Two edits: (a) **validation line** — it says "awaits experimental data"; update to
   "one real instance at the composite layer (a fuel-driven DNA reaction network; Nicholas et al.
   2025), with synthetic validation elsewhere"; (b) light polish for any residual coined term.
2. **`character_emergence.md` (NEW — the headline-value section, clean register)** — the two lifts
   (space of characters = manifold; closure = emergence under coupling), the **minting claim**
   (coupling produces a protected circulation neither part had = a discrete graph-flux invariant,
   sustained by drive, not stored, not Chern-like), the **two-frame method** behind it (mined from
   `character_fdr_treatment.md`), and the **one real instance** (the DNA-NESS: detailed-balanced DNA
   hybridization cycle driven by RNase-H fuel hydrolysis; minted affinity; run-loop collapses on fuel
   removal — observed experimentally; confirmed against the full non-linear model to cycling-rate
   ratio 1.002). State the idealizations (N=3 reduction, chemostat) plainly. This is the most-exposed
   layer — write it clean *and* honestly scoped.
3. **`README.md` (landing)** — the accessible front door (value-forward but honest): what a character
   is, why it's interesting (emergence made testable), the unification, "if it continues to check
   out" (conditional implications), honest scope. **Points at `character.md` + `character_emergence.md`
   as "start here"** — both now in-repo and in register. (The hollowed primer's value-forward
   *content* was good; its register and its link targets were wrong. Reuse the content shape, fix
   both.)
4. *(optional)* a self-contained **imports list** in `character-framework` so the public repo carries
   its own provenance (or link `character_prior_art.md`).

## 5. Honest-scope requirements (carry these — they are load-bearing post-retraction)

- **One** real instance (DNA-NESS); the rest synthetically vindicated.
- The central **β data-collapse test has not been run on real data**.
- The emergence/composite layer is the **most exposed**; write it clean but with idealizations
  stated (N=3 reduction of a nonlinear CRN, chemostat, enzyme QSS).
- The **alive loop** (self-sustaining recursive circulation — the deepest target) is **named,
  parked, work continues** — not claimed.
- The contribution is **small and honest**: a coordinate system + a falsifiable test + the emergence
  reading + one receipt. Be at peace with that scope — it is *why* it is less "not even wrong."
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
- **Do not move the engine** (conform reads it).
- **The dead-`ch` references in the live corpus** (engine §0 ch/chit nouns, `character_applications`,
  frontier batteries, README/CLAUDE inventories) are reconciled when the *internal* corpus gets its
  own register pass — NOT required for the public rebuild, but logged: the public face simply does
  not use them.
- The frozen tag **`character-v0.1`** captured the old corpus; cut a **new tag** for the clean public
  snapshot when the rebuild lands.

## 7. Sequence

1. **[DONE]** Hollow out `character-framework` (stub README; commit `70b3981`).
2. Migrate `character.md` → `character-framework`; update the validation line (§4.1); light register polish.
3. Write `character_emergence.md` (§4.2) — clean register; the lifts + minting + two-frame method + the DNA-NESS instance + idealizations. **Look at it together before finalizing** (most-exposed layer).
4. Write the README landing (§4.3) — value-forward, honest, pointing at the two clean docs.
5. *(optional)* the self-contained imports list (§4.4).
6. Tag `character-framework` **`v0.1`** (the clean public snapshot).
7. **(Later, deliberate, Ron's go)** the re-publication decision.

## 8. Done-when

`character-framework` presents the framework **entirely in the scientific register** —
`character.md` (basis, validation updated) + `character_emergence.md` (lifts/emergence/instance) +
README (landing) — no coined-noun debris, honest scope throughout, every import named, self-contained
(no dependence on old-register docs). The engine et al. remain the internal dev corpus in `mpa-atlas`.

**Cross-refs:** [`character.md`](../framework/character.md) (the basis/register) ·
[`character_fdr_treatment.md`](../framework/character_fdr_treatment.md) (lift method, mine for rigor) ·
[`character_composite.md`](../framework/character_composite.md) (emergence source) ·
[`character_prior_art.md`](../framework/character_prior_art.md) (the named imports) ·
`mpa-conform/scripts/dna_ness_crosscheck.py` + `docs/dna_ness_source.md` (the real instance).
