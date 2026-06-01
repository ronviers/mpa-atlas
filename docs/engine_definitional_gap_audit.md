# Engine definitional-gap audit (2026-05-31)

> **STATUS: APPLIED 2026-05-31.** The §0 — Objects & Definitions layer this audit specified is now in
> `framework/character_engine.md` (top, above PARAMETERS). This doc is retained as the rationale of record for that
> layer. The remaining value here is the per-term reasoning; the layer itself is canonical in the engine.

**Method.** Read `character_engine.md` cold, as a stranger with modern tools would (e.g. an infographic-builder model
asked to render "character flow"). Flag every term used in *load-bearing* position that the engine never
*defines* — the assumed dictionary. The test that exposed it: an infographic model fed the engine renders the
**machinery** (flows, bifurcations, the deformation chart) confidently and the **nouns** as empty centers
("character" → decorative arrows; "ch" → an unexplained tick; the Banach reference → absent).

**Root cause.** The engine opens "Every line below is a definition, a formula, a condition, a mapping, or a
kill condition" — but it is a **dense reference card for people who already hold the concepts.** It has
PARAMETERS (symbols), STATES, OPERATORS — all *formal*. It has **no first-contact layer**: no §0 objects, no
glossary, no plain-language definition of its own central nouns. Those live scattered across `character_units.md`,
the architectural block-in, receipts, and **parked memory** — never in the engine itself. The thin discipline
correctly says *don't duplicate derivations*; it never said *don't define your terms*. The engine has overshot
thin → into not-self-contained: a claim whose nouns are undefined ("character-bearing drift") is a claim plus
an assumed dictionary, which a stranger cannot evaluate.

**Disposition.** Audit only this session (definitions written in a tool-colored session must not be
auto-planted; they need the rewrite's care). This inventory feeds the rewrite (step 4 of
`vocabulary_refactor_spec.md`). Recommended home when it lands: **§0 Objects & Definitions at the top of the
engine** (so a model fed only the engine reads definitions before formalism) — decided at rewrite time.

---

## The inventory — undefined load-bearing terms, by severity

Severity: **A** = load-bearing AND absent/never-defined in the engine (worst — the infographic empty centers).
**B** = symbol defined but the *concept/word* and its links are absent. **C** = used unexpanded, assumes prior knowledge.

### A — absent, yet central (the empty centers)

- **character** *(severity A — and it is the framework's NAME)*. Used 4× ("character-bearing drift,"
  "substrate character," "the character deformation chart"); defined nowhere. **Recommended one-liner:**
  *Character = the substrate-general structure of how a driven-dissipative system **holds, deforms, and
  circulates** under load — read as the deformation of the Boolean ring (amplitude face: c/s/r holding;
  sign-topological face: protected circulation). Not a metaphor: a measurable two-faced deformation. (Rigor:
  TWO FACES, DEFORMATION GENERATORS.)*

- **ch** *(severity A — the unit the whole framework is denominated in; appears 0× in the engine)*. **Recommended
  one-liner:** *ch ("character bit") = the framework's forced unit, 1 ch ≡ ln2 nats — one quantum of held
  character, surfacing on both faces: one ch of headroom (G₀/L=2, the Q-peak) and one ch of cost (the erasure
  floor). (Rigor: `character_units.md` §1.)* — and every "1 ch" / "ch" already in the engine (OPERATORS R floor,
  TWO BITS, THERMO↔INFO per-event row) should point here.

- **Banach substrate / Banach reference** *(severity A — appears 0× in the engine; the analytical reference the
  entire conform/auditor/tool layer conforms real substrates TO)*. **Recommended one-liner:** *The Banach
  reference = the analytically-tractable, tunable synthetic substrate (a contraction-mapping NESS) used as the
  fixed reference character that real substrates are conformed against — the ruler, regenerable and
  dialable, never the data. (Rigor: conform layer; `pa:banach-fixed-point`.)*

- **NESS** *(severity A — used ~12×, never expanded)*. **Recommended one-liner:** *NESS = non-equilibrium steady
  state: a system held in a stationary statistical state by a continuous throughput (drive in, dissipation
  out), NOT at thermal equilibrium — detailed balance broken. MPA's default object (AXIOMS: NESS-by-default).*

- **drive / dissipation** *(severity A — the two poles of every claim; never given the plain definition)*.
  **Recommended one-liner:** *Drive = the supplied work/throughput holding the system off equilibrium (coordinate
  D = Φ*/κ); dissipation = the heat/entropy export balancing it. A substrate is alive-as-character only while
  the drive flows; MPA metabolizes the drive, never supplies it (the bootstrap constraint).*

### B — symbol present, concept/word/links missing

- **chit** *(B — symbol defined `ln(G₀/L)`; the WORD and its links to **ch** and **character** are in units, not
  engine)*. **Recommended addition:** name it ("chit = headroom above threshold, the central character
  coordinate; measured in ch via chit/ln2") and link chit ↔ ch ↔ character explicitly. Right now a reader sees
  a log-ratio and misses it is the spine coordinate.

- **trail** *(B — used in OPERATORS / SCALE-RELATIVITY / "trail-integral"; never defined)*. **Recommended
  one-liner:** *Trail = the persisting time-integrated record of a holding (the substrate's maintained NESS
  history); what coarse-grains up the tower and what `τ_obs` reads at a scale.*

- **holding** *(B — used in POSITS/FRAYING/AXIOMS as the thing character is predicated of; never defined)*.
  **Recommended one-liner:** *Holding = a sustained NESS occupation of a mode/structure (the c/s/r object) —
  "held" = maintained above threshold against decay; the unit of what a substrate keeps.*

- **coherence** *(B — "coherence observable," "level-(n+1) coherence"; assumed)*. **Recommended one-liner:**
  *Coherence = the degree to which a holding stays organized under load — measured by the triple (chit, Q,
  I_pred); lost by fraying.*

- **the two bits / two faces** *(B — sections exist, but the engine never states in words WHY two, for a
  first reader)*. **Recommended framing line atop TWO FACES/TWO BITS:** *The deformation has two independent
  axes — how much is held (amplitude) and which way it circulates (sign-topological) — so character carries
  two independent bits, non-interconvertible.*

### C — used unexpanded (assume prior knowledge; lower urgency but real for a stranger)

- **metabolize / subtractive / "imports and binds"** *(C — the what-MPA-IS verbs, stated as slogans in the
  header)*. A stranger reads these as branding. **Recommended:** one line — *MPA adds no new mathematics; it
  imports established results and re-reads ("metabolizes") them in one coordinate system; all content is in the
  bindings and their over-determination (the collapse falsifier).*
- **substrate** *(C — the universal noun; never given its one-liner)*. *Substrate = any driven-dissipative
  system MPA reads (glass, laser, neural tissue, ecology, a market…); MPA is substrate-neutral by construction.*
- **k_frust** *(C — defined formally as the topological invariant, but never in words for first contact)*.
  *k_frust = the signature that a system carries a protected, drive-independent circulation (a frustrated
  triad) — it cannot relax to rest; "frustration" = no global ordering satisfies all the signed couplings.*
- **gauge / gauge-invariant / gauge-irremovable** *(C — load-bearing in the sign-topological face; assumed)*.
  *Gauge = a relabeling (node sign flips) that doesn't change physics; gauge-invariant = survives all
  relabelings (real structure); gauge-irremovable = a sign no relabeling can erase (the protected bit).*
- **τ_obs** *(C — "observer window"; defined as a parameter but the conceptual "MPA reads at a chosen scale"
  is implicit)*. Acceptable as-is; flag for the rewrite.

---

## What an infographic-builder model is missing right now (the concrete failure)

Fed the current engine, the model renders the **grammar** (chiral cycles, c→s→r migration, the marginal point,
the deformation chart) and misses **every noun**: "character" → vibe/arrows; "ch" → unexplained tick;
Banach reference → absent; drive/dissipation → assumed; NESS → jargon. It produces something that *looks* like
MPA with empty centers. The §0 layer is exactly what fills them.

## Recommendation for the rewrite (feeds `vocabulary_refactor_spec.md` step 4)

1. Add **§0 — Objects & Definitions** at the top of the engine: the A and B terms above, one line each, each
   pointing to where its rigor lives (units / TWO FACES / receipts / conform). ~12–15 lines.
2. Thread the **ch** pointer into every existing "ch"/"1 ch" usage in the engine.
3. The C terms get a light touch (one clause each) or a `mpa_glossary.md` companion if §0 gets too long.
4. This is the natural carrier for the **telos preamble** (the parked alive-loop *why*, asterisked) — a reader
   who now knows what "character" *is* is ready to be told what it's *for*. (Separate decision; flagged.)

**Discipline note:** this is NOT thickening the claims (thin discipline intact — no new structure, no new
falsifier, no redefinition). It is giving the existing claims their dictionary, which a self-contained engine
requires and the thin discipline never barred.
