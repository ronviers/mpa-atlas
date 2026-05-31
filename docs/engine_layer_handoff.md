# Handoff — build the engine's first-contact layer (§0)

**You are building this now.** Not groundwork, not a future task — your job this session is to write the §0
definitional layer into `mpa_engine.md`. Everything below is to let you do that. (Earlier sessions did the
groundwork and made the decisions; nothing is left to re-decide except where this doc says "ask Ron.")

---

## YOUR JOB (in order)

1. **Read `framework/mpa_engine.md` cold.** Notice: it defines *symbols* but never its own *nouns* — "character"
   (its own name), "ch" (its own unit), "Banach reference", "NESS", "drive/dissipation" are used heavily and
   defined nowhere. A stranger (or an infographic tool) can manipulate the formulas but can't say what they mean.

2. **Read `docs/engine_definitional_gap_audit.md`.** It is the *content* of what you're writing: every undefined
   load-bearing term, sorted A/B/C, each with a drafted one-line definition and a pointer to where its rigor
   lives. You refine these into prose; you do not re-derive them.

3. **Write a new `## §0 — Objects & Definitions` section at the TOP of `mpa_engine.md`** (above PARAMETERS):
   - Open with the identity line (verbatim, it's settled):
     > **MPA — a phenomenology of character in driven-dissipative systems. A measurement discipline: one
     > coordinate system forcing established results to read together; an effective description — not claimed
     > fundamental.**
   - Then one plain sentence per term, each ending with a pointer to where rigor lives. Order: the 5 **A-terms**
     first (character, ch, Banach reference, NESS, drive/dissipation — non-negotiable), then the **B-terms**
     (chit + its ch↔character link, trail, holding, coherence, the why-two-faces line), then **C-terms** lightly
     (substrate, metabolize/subtractive, k_frust-in-words, gauge, τ_obs).
   - State the lineage **once** as a credential (see "Settled decisions" below).
   - Target ~12–15 entries. If it bloats past the engine's density, move the C-terms to a `mpa_glossary.md`
     companion — but A+B stay in the engine (a model fed only the engine must get them).

4. **Thread the ch pointer** into every existing "ch" / "1 ch" usage already in the engine (OPERATORS R floor,
   TWO BITS, THERMO↔INFO per-event row) so the unit stops floating.

5. **Stop and show Ron** the §0 draft before committing. This is public-facing prose on a published framework;
   he reviews voice and wording first.

---

## SETTLED DECISIONS (do not re-open these)

- **Identity line:** the verbatim block in step 3. Settled wording (Ron's). Don't rephrase it.
- **The name is NOT your problem.** Use "MPA" plainly as the handle throughout. Do **not** invent or propose a
  new name — the new name is the deliberate *final capstone* of the whole rewrite, chosen with Ron much later.
  §0 carries zero naming weight.
- **Lineage, stated once as credential (not apology):** MPA descends from *Metastable Propositional Calculus*
  (MPC) — a far larger framework (a full four-valued logic + a separation theorem + a quantum conjecture) that
  its authors **deliberately scaled down** to today's disciplined engine. Most frameworks inflate; this one was
  cut back. That is the honesty signal — worth one sentence in §0, worn not hidden. (The Calculus→Algebra shift
  in the acronym was itself the first such cut. "Propositional" is now vestigial since the live work is dynamics
  not logic — but do NOT relitigate that; it resolves itself when the capstone name lands.)

---

## VOICE (this decides whether §0 reads compelling or like a textbook glossary)

**Write as the same author as the rest of the engine — declarative, confident, naming what is there.** Not a
teacher, not an explainer.

- **Avoid the educator register** ("Let's understand what character is…"). It condescends to a physics-literate
  audience, it pads, and it clashes with the engine's density.
- **Use the naturalist register:** "**Character is** the substrate-general structure of how a driven-dissipative
  system holds, deforms, and circulates under load." Assert the object into existence the way a physics text
  says "entropy is…". No hedging, no scaffold.
- **Let the framework speak for itself where an object is *forced*.** The ch isn't "a unit we chose" — it's
  "the unit the framework picks for itself" (the Q-peak forces chit=ln2; the erasure floor forces the same
  ln2). Show the framework discovering its own structure. Where a term is just a label (e.g. "substrate"), a
  plain sentence is fine — **don't fake self-emergence for a mere label** (that's the cringe direction).
- **Touchstone to match:** the engine's own line 7 ("a measurement discipline, not a model") and the units doc's
  "the framework picks its own amplitude unit." **Touchstone to avoid:** anything that sounds like explaining
  MPA *to outsiders* or *down to learners*.

---

## GUARDRAILS

- **This is not thickening the claims.** Thin-RFC discipline bars duplicating derivations and speculative
  edge-casing; it never barred *defining your terms*. §0 adds no new structure, no new falsifier, no
  redefinition — it gives existing claims their dictionary. (If challenged, this is the defense.)
- **Define by pointing, not duplicating.** Each entry links to where rigor lives (`mpa_units.md` §1, TWO FACES,
  receipts, conform); it does not re-derive.
- **Don't overclaim.** Any definition touching vindication (character, the claims, the Banach reference) stays
  honest: synthetically vindicated, real-substrate vindication still owed (per `engine_readiness_assessment.md`).
- **"character" is substrate-general, never psychological.** No personality/biology framing — substrate-neutral
  examples only (`feedback_no_anthropocentric_framing`).

---

## REFERENCE DOCS (read as needed, not front-to-back)

- `docs/engine_definitional_gap_audit.md` — **the content** (read fully; step 2).
- `framework/mpa_engine.md` — **the target** (read fully; step 1).
- `framework/mpa_units.md` — where **ch** / chit / the forced unit live; your ch/chit definitions point here.
- `framework/mpa_fdr_treatment.md` — where two-frame / FD-ratio / NESS live in long form.
- `docs/engine_readiness_assessment.md` — the honest scope your definitions must not exceed.
- `docs/naming_decision.md` — full reasoning behind the settled name decisions (only if you want the why).
- `CLAUDE.md` (this repo) — thin-RFC discipline.
- (Optional, for a later telos preamble — NOT this session) memory `project_syn3_alive_loop_northstar.md`.

---

## STATE (where the project stands — context, not tasks)

All committed and pushed. This session's predecessors closed: the frustration-ascent generative bet (legal),
the Tier-B two-frame magnitude identity, vocab-refactor step 1 (retired "violation"/"wall" as prose anchors),
and hardened the dissipative-Rosetta tool SOP. The engine's claim skeleton is complete and synthetically
vindicated; real-substrate vindication is data-gated (parked, not failed). The §0 layer you're building is the
first step of the eventual public-facing engine rewrite; the rewrite's final step is the capstone name.
