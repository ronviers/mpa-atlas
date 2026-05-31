# Handoff — adding the first-contact layer to the engine (read cold, next session)

**The job.** Give `mpa_engine.md` the definitional / first-contact layer it lacks, so it is **self-contained**
— a stranger (human or an infographic-builder model) can read it and grasp what its nouns *mean*, not just
manipulate its formulas. Today the engine is a dense reference card for people who already hold the concepts;
fed to a modern tool it renders the *machinery* (flows, bifurcations, the deformation chart) and leaves every
*noun* an empty center ("character" → arrows, "ch" → an unexplained tick, the Banach reference → absent). This
session is the **groundwork**; the layer itself is written next session because it must be done with the
rewrite's care, in a register-clean context, not a tool-colored one.

This handoff is also the entry point to the **eventual public-facing engine rewrite** (the larger multistep
goal: make the engine as compelling as the science). The first-contact layer is the first real step of that.

---

## THE DOCUMENT SET (everything the next session needs, all committed/pushed except where noted)

Read in this order:

1. **`docs/engine_definitional_gap_audit.md`** — the core input. The complete inventory of undefined
   load-bearing terms (severity A/B/C), each with a recommended one-line definition and a pointer to where its
   rigor already lives. **This is the content of the layer.** *(uncommitted as of session end — commit first.)*
2. **`docs/vocabulary_refactor_spec.md`** — the rename groundwork. "violation"→FD-ratio/FDR-departure,
   "wall"→marginal-point/ceiling/bound (step 1 DONE in prose; keys held for step 2). Its §"Sequence for the
   eventual full rewrite" is the master sequence this handoff slots into (the layer is step 4's opening move).
3. **`docs/engine_readiness_assessment.md`** — what the engine IS vs ISN'T (claim skeleton complete +
   synthetically vindicated; world-vindication blocked by a DATA gap, not a work gap). The layer must not
   overclaim past this — every definition that touches vindication carries the honest asterisk.
4. **`framework/mpa_engine.md`** — the target. Read it cold first, before the audit, to feel the gap yourself.
5. **`framework/mpa_units.md`** — where **ch**, chit-in-ch, the forced unit, and the anchor set are defined.
   The layer's "ch" / "chit" / unit definitions point here; do not duplicate, link.
6. **`framework/mpa_fdr_treatment.md`** — where the two-frame structure, FD ratio, FDR-departure live in
   long form. The layer's "two faces / drive / dissipation / NESS" definitions lean on this.
7. **`architecture/MPA_Architectural_Block-In.md`** — the motivating frames (observer-as-scale-manager, the
   three-layer architecture). Where the *why-we-think-this-way* meta lives; the layer borrows its framing
   register, not its content.
8. **The parked NORTH STAR** (memory: `project_syn3_alive_loop_northstar.md`) — the deep *why* (the
   self-sustaining autopoietic "loop of the loop"; "character is always on"). PARKED/out-of-reach, but it is
   what a telos preamble would draw on. Read it so the layer's voice knows what it is ultimately pointing at,
   even if the preamble is deferred.
9. **`CLAUDE.md` (mpa-atlas)** — the thin-RFC discipline. The layer must honor it (see "Discipline guardrail").

---

## WHAT TO BUILD (the recommended shape — from the audit)

A **§0 — Objects & Definitions** section at the **top** of `mpa_engine.md` (above PARAMETERS), so a model fed
only the engine reads the dictionary before the formalism. ~12–15 one-line entries:

- **Severity-A (absent, central):** character · ch · Banach reference · NESS · drive/dissipation. *(non-negotiable)*
- **Severity-B (under-defined):** chit (the word + its ch↔character links) · trail · holding · coherence · the
  why-two-faces / why-two-bits framing line.
- **Severity-C (light touch, one clause each):** substrate · metabolize/subtractive · k_frust-in-words · gauge
  family · τ_obs. If §0 bloats, spin the C-tier into a `mpa_glossary.md` companion (but then ship them together
  — a model fed only the engine must still get the A/B terms).

Each entry: one plain sentence + a pointer to where rigor lives (`mpa_units.md` §1, TWO FACES, receipts,
conform). The audit already drafts every one — refine, don't re-derive.

**Then:** thread the **ch** pointer into every existing "ch" / "1 ch" usage in the engine (OPERATORS R floor,
TWO BITS, THERMO↔INFO per-event row) so the unit stops floating.

---

## VOICE — how the model writing the layer should find its register (the hard part; reason it, don't default)

This is the question that decides whether the layer reads as compelling or as a textbook glossary. Guidance,
with the reasoning, not just a verdict:

**Do NOT anchor to "educator."** The educator voice ("Let's understand what character means!") is the default
an LLM falls into for a definitions task, and it is wrong here for three reasons: (i) it condescends — MPA's
audience is researchers who know dissipative physics, not students; (ii) it pads — educator voice explains
*around* a thing; the engine's whole virtue is that it doesn't; (iii) it imports a register foreign to the
dense, declarative engine, creating a seam. The §0 layer must read as *the same author* as the rest of the
engine, only at first-contact altitude.

**Anchor instead to: the precise naturalist.** The register that fits is the one MPA already half-has in its
header ("MPA is a measurement discipline, not a model") — declarative, confident, substrate-neutral, *naming
what is there*. A definition in this voice is not "character is the idea that…" but "**Character is** the
substrate-general structure of how a driven-dissipative system holds, deforms, and circulates under load." It
asserts the object into existence the way a good physics text asserts "entropy is…" — no hedging, no teaching
scaffold, no apology. The model should write each definition as if naming a thing every competent reader will
recognize once named — because that is exactly MPA's claim (these structures recur across the dissipative
universe; MPA only gives them one coordinate system).

**Can MPA speak for itself? — Partly, and it's the best move where it works.** The strongest definitions are
the ones where the framework's own logic *forces* the definition rather than the author asserting it. Example:
the ch is not "a unit we chose" — it is "the unit the framework picks for itself" (the Q-peak forces chit=ln2;
the erasure floor forces the same ln2; one quantum, two faces). That definition *speaks for itself* — it shows
the framework discovering its own unit. **Where a definition can be written as the framework forcing its own
hand, do that** (it is also the most compelling, and the most honest — it shows rather than tells). Where it
can't (e.g. "substrate" is just a scope word), a plain naturalist sentence suffices. So: **let MPA speak for
itself wherever the object is forced; name plainly where it is conventional.** Do not fake self-emergence for a
term that is merely a label — that is the cringe direction.

**Calibration touchstones for the model:** the voice that closed the amplitude-autonomy bet ("the gain is
external-frame of necessity") and the units doc's "the framework picks its own amplitude unit" — confident,
forced-not-asserted, zero scaffold. The voice to AVOID: the NFL-tool register (explaining MPA *to* an outside
field), and the educator register (explaining MPA *down* to a learner). The layer explains MPA *as itself, at
first sight.*

---

## THE NAME — "MPA" is undefined in canon, and may be off-putting; decide deliberately

**Finding (this session):** "MPA" appears throughout the framework but is **never once expanded or defined** —
not in the engine, not in the block-in, nowhere live. The name has no canonical referent. (Historically it
traces to the program's lineage; the live docs treat it as an opaque handle.)

**Why this matters for the layer:** the §0 layer is the first place a stranger meets the framework. An
undefined three-letter acronym at the top of a dense formal document is a *cold open* — it reads as
in-group jargon and can be off-putting before the reader reaches anything compelling. But renaming a published,
DOI'd framework (Zenodo 10.5281/zenodo.20357550, 4-author byline) is a heavy, non-local act — not a next-session
decision to make unilaterally.

**Recommended handling (decide WITH Ron, do not auto-resolve):**
- **Option 1 — define it, don't rename it.** Give "MPA" a one-line expansion in §0 that is *true to what it
  does* and *not off-putting*. The framework is, in its own words, a measurement discipline reading how
  driven-dissipative systems hold character — so an honest expansion exists in that direction. The §0 entry
  would state it once, plainly, and move on. Lowest-cost, removes the cold-open, preserves the published name.
  **(recommended starting point.)**
- **Option 2 — a public-facing display name + "MPA" as the internal/technical handle.** Like many frameworks
  carry a friendly name + a technical abbreviation. The display name does the first-contact work; "MPA" stays
  for citations/internal use. Bigger move; a branding decision.
- **Option 3 — leave "MPA" opaque, lean on the character of the work.** If the §0 definitions are compelling
  enough, the acronym matters less. Riskier for cold readers.

**Do NOT** invent an expansion and plant it as canon without Ron — the name is published and load-bearing
across repos. Bring options, let Ron choose. (Note Ron's standing preference for *coined names* over
descriptive accuracy — `feedback_prefer_coined_names` — which may favor a coined display name over a literal
acronym expansion.)

**DECIDED 2026-05-31 (Ron delegated; see `docs/naming_decision.md` — read it):** the name question was worked
through with the lineage in hand. The framework **deflated** from *Metastable Propositional Calculus* (MPC — a
full four-valued logic + separation theorem + quantum conjecture) to today's engine — *scaled down by its
authors*, which is the **credential**, not an embarrassment. Locked recommendations:
- **Identity (the §0 opening line):** *"MPA — a phenomenology of character in driven-dissipative systems. A
  measurement discipline: one coordinate system forcing established results to read together; an effective
  description — a better metaphor than most, but a metaphor until real substrates give it footing — not
  claimed fundamental."* ("phenomenology" = the engine's own line-1 word, the precise effective-not-fundamental
  term, matches the synthetic ceiling; anti-pretentious by construction.)
- **Letters:** keep "MPA" as citation handle; state etymology (MPC Calculus → MPA Algebra, the Calculus→Algebra
  shift = the first deflation) + the deflation **once, as credential**. Do NOT lead with the acronym expansion
  ("Propositional Algebra" names only the structural half; the live soul is the character projection).
- **"Propositional" is vestigial** (live work is dynamics, not logic) — FLAGGED for a deliberate future rename
  decision WITH Ron, explicitly OUT of scope for §0.
- **Confirm the MPC→MPA etymology with Ron** before stating it as fact — it is inferred (the lineage doc Ron
  pasted + repo names `mpc-*`/`mpa-*`), not verified in canon ("MPA" is undefined in every live doc).

---

## DISCIPLINE GUARDRAIL (so the layer doesn't get second-guessed)

- **This is NOT thickening the claims.** Thin-RFC discipline bars duplicating *derivations* and speculative
  edge-casing; it never barred *defining your terms*. A self-contained engine requires its nouns defined. The
  layer adds **no** new structure, **no** new falsifier, **no** redefinition of a coined object — it gives the
  existing claims their dictionary. Say so in the layer's own framing if useful.
- **Definitions point, don't duplicate.** Each entry links to where rigor lives; it does not re-derive.
- **Honor the readiness asterisk.** Any definition touching vindication (character, the Banach reference,
  the claims) carries the honest scope: synthetically vindicated, world-vindication data-gated (per
  `engine_readiness_assessment.md`). Do not let the first-contact layer quietly overclaim.
- **Character round-trip:** adding §0 is a definitional layer, not a change to what any substrate renders as —
  it should not trigger the spec-stability character-test round-trip. Flag to Ron if uncertain; he can overrule.
- **Coined-name preference** (`feedback_prefer_coined_names`) and **no-anthropocentric-framing**
  (`feedback_no_anthropocentric_framing` — character is NOT a human-domain concept; substrate-general examples
  only) both bind the layer's word choices.

---

## SEQUENCE (where this sits in the larger rewrite)

Per `vocabulary_refactor_spec.md` §Sequence:
1. ✅ vocab anchors retired (prose) — DONE this session.
2. retire the stable keys (`wall-as-type-boundary`, `battery:wall-ladder`, receipts `§Wall`) in one
   synchronized frontier↔receipts↔engine pass + I1 re-audit. *(can be done alongside or before the layer.)*
3. second anchor-sweep for other register-cringe terms (candidates to *evaluate, not presume*: "killshot,"
   "tripwire," "fraying").
4. **the first-contact layer (THIS handoff) → then the public-facing engine rewrite proper** — compelling
   prose, the §0 definitions, and (separate Ron decision) the telos preamble drawing on the parked north star.

**First action next session:** commit `docs/engine_definitional_gap_audit.md` (only uncommitted doc), then
build §0 from it in the naturalist voice above, bringing the name-options to Ron before touching "MPA."

---

## SESSION STATE AT HANDOFF (so next session knows where things stand)

- **frustration-ascent generative bet: CLOSED** (legal) — generative-of-chirality, parasitic-on-drive; amplitude
  autonomy is external-frame/supplied, not minted. Engine carries the Mintability corollary + test-validity guard.
- **Tier-B (two-frame exact magnitude identity + τ-reconciliation): CLOSED** — the last engine-internal close
  available without substrate data. `τ-window-reconciliation` promoted.
- **Vocab refactor step 1: DONE** (prose anchors retired; keys held).
- **The tool (dissipative Rosetta):** SOP hardened across two NFL passes; procedure + meteorology exemplar
  committed. NFL columns are productive-failure inputs, not landed columns.
- **Engine readiness:** claim skeleton complete + synthetically vindicated; world-vindication DATA-gated (the
  honest ceiling). Tier-A items all real-substrate-gated = parked, not failed.
- **Definitional gap: AUDITED** (this session); layer deferred to next (this handoff).
- All pushed except `engine_definitional_gap_audit.md` (commit next session).
