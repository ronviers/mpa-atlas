# Dissipative Rosetta — field-mapping procedure (hand to outside models, read cold)

**What you are producing.** One *column* of a translation table: a single science's established categories,
each re-read in MPA's substrate-general "character" primitives. The deliverable is a table + a short
"what this surfaces" note + a flagged-for-review list. You do **not** need the MPA framework documents — this
procedure is self-contained. You **do** need your own field's literature, because every row must cite the
field's own established result.

**The one rule that governs everything: IMPORTS ONLY, METABOLIZE.** MPA brings no new machinery to your
field. It re-reads what the field already established, in a common coordinate system. You are building a
*translation table, not a theory of the field*. Three consequences, enforced by the checks below:
1. You never map a phenomenon **directly** to an MPA primitive. You route it through the phenomenon's **own
   established dissipative / non-equilibrium treatment** (with citation), then onto the primitive. That middle
   step is the load-bearing honesty gate.
2. You never write "MPA explains / predicts / proves X." You write "X (established as Y by [citation])
   re-reads as primitive Z." MPA contributes the *coordinate system*, nothing else.
3. If a phenomenon needs a **new** primitive to fit, it is **not a table row** — it is a flagged discovery
   (§6). Do not invent primitives to force a fit.

---

## 1. The target coordinate system — the character-primitive glossary

These are the columns of the common coordinate system. Each entry: **name** — meaning — *dissipative
signature to look for in your field* — `[anchor]` (leave the anchor as written; it is for the integrator, not
for you). A "substrate" = any driven-dissipative system (your field's objects).

**Foundational frame**
- **substrate-is-NESS** — every object is a driven-dissipative non-equilibrium steady state: energy/matter
  flows **in** (a drive) and is dissipated **out** (a sink). *Signature: identify the drive and the sink
  before anything else. If there's no sustained throughput, it's not a substrate.* `[POSITS]`
- **bootstrap constraint** — the drive is **supplied** from outside (second law); the system only
  *metabolizes* it, never self-levitates. *Signature: what happens when you remove the energy source? It
  decays.* `[POSITS / bootstrap]`

**The two faces (the sharpest lens — see §3)**
- **chirality / the MINTABLE face** (`Im λ`) — the rotation sense / handedness of a sustained circulation;
  **intrinsic** to the system's structure; the legal, mintable property. *Signature: a handedness, rotation
  direction, or cyclic order that the system's wiring sets.* `[chirality / sign(𝒜)]`
- **amplitude / the SUPPLIED face** (`Re λ`, gain) — the magnitude/energy/gain sustaining a structure;
  **external**; supplied by the drive, never minted. *Signature: the "strength" of a structure, which dies if
  the drive is cut.* `[Mintability corollary]`
- **the topological bit** — a discrete, gauge-irremovable handedness held *leak-free* (no ongoing energy cost
  to hold; flips only by rewiring). *Signature: a binary structural property (which-hand / which-way) fixed by
  topology, persisting without being actively maintained.* `[TWO BITS]`

**Regimes & onsets**
- **c/s/r trichotomy** — coherent / sub-threshold-critical / relaxed: a driven mode sits in one of three
  regimes by gain-vs-dissipation. *Signature: a control parameter whose crossing changes behavior qualitatively
  (ordered → critical → disordered).* `[§14 / three-regime threshold]`
- **ignition** — the bifurcation (pitchfork/transcritical) turning a structure **on** as drive crosses
  critical. *Signature: a pattern/structure that appears at a threshold (onset).* **DISCRIMINATOR: this is a
  bifurcation of a DYNAMICAL FLOW (a fixed point changes stability / a new attractor is born as a parameter
  crosses critical). A static decision boundary — an argmax/optimization that flips which choice is best (e.g.
  a go/no-go threshold in an expected-value calculation) — is NOT a bifurcation; it has no flow whose
  stability changes. Map those to a decision/threshold note, not ignition.** `[§14 bifurcations]`
- **chit** — the log ratio of gain to loss, ln(G/L); distance from balance; entropy-production per event.
  *Signature: a dimensionless drive-to-dissipation ratio, a "distance from equilibrium."* `[§2 chit]`
- **metastable basins** — multiple persistent macro-states with switching between them. *Signature: regime
  multiplicity, hysteresis, sudden transitions between long-lived states.* `[§14 attractors]`

**Sustained circulation**
- **k_frust / protected circulation** — an irreducible NESS current that cannot relax away — a
  topologically-forced cycle (complex-conjugate eigenvalue pair, broken detailed balance). *Signature: a
  persistent current/cycle/circulation in steady state that isn't just relaxation to rest.* **DISCRIMINATOR
  (do not over-map): the minimal protected carrier is N≥3 — a directed cycle of ≥3 mutually-countering states
  (rock-paper-scissors / cyclic dominance / replicator dynamics). A 2-state alternation (A↔B, "negative serial
  correlation"), a mixed-strategy distribution, or any reciprocal pair is N=2 → gauge-removable → NOT
  protected; it is not k_frust.** `[§10 / §16]`

**Non-oscillatory autonomy**
- **reservoir/release register** — a slow variable that charges → crosses a threshold → discharges
  (relaxation/excitable/hysteretic), **not** a limit cycle. *Signature: accumulation-then-dump dynamics;
  storage that fills and releases ("rain").* **DISCRIMINATOR: the structure must be SUSTAINED — it recharges
  and releases repeatedly in a steady state. A one-shot process that runs to an absorbing/terminating state
  (e.g. an absorbing Markov chain that ends at a goal/death/turnover) is NOT this primitive — a terminating
  chain is the antithesis of a NESS.** `[reservoir species]`

**Hierarchy & scale**
- **platformed topology / RG type-identity** — a coarse-grained level carrying its **own** coherent
  structure, again of the same form (recursion up a tower). *Signature: large-scale coherent structures
  emerging from coarse-graining smaller ones; each scale resembling the one below.* `[§6.5]`
- **heat-tax tower / plateau ladder** — fast modes serve slow modes up a hierarchy; each plateau is a
  persistent reduced description (a normally-hyperbolic manifold). *Signature: scale separation; an
  energy/information cascade; fast-slaved-to-slow.* `[COMPRESSION]`
- **the Wall / loss of normal hyperbolicity** — the boundary where the reduced (plateau) description fails;
  necessary-not-sufficient for chaos. *Signature: a predictability horizon, onset of turbulence/chaos,
  breakdown of an effective/slow-manifold description.* `[COMPRESSION / Wall]`

**(Advanced — use ONLY if the field LITERALLY supplies the structure; see the advanced-primitive guard below)**
- **the two frames** — fluctuation-response read two ways: external (response to an applied probe) vs
  self-probe (the system's own circulation as reference, defined *iff* a current exists). *Signature: a field
  with both a perturbation-response measure and an intrinsic-circulation measure.* `[TWO-FRAME CONSTRUCTION]`
- **deformation generators** — the linear structure near a fixed point decomposes as damping ⊕ chirality ⊕
  splitting/detuning. *Signature: you have the Jacobian/linearization of the dynamics.* `[DEFORMATION GENERATORS]`

> **⚠ ADVANCED-PRIMITIVE GUARD (the v2 NFL slip — do not repeat).** These two are the most over-reached
> primitives: "the field has adaptation/dynamics" is **not** enough to map to **deformation generators** — that
> requires the field to *literally write down the Jacobian* and decompose its eigenstructure (damping/chirality/
> splitting). Replicator/evolutionary-game adaptation converging to a stable mix is **c/s/r / ignition** (a flow
> with attractors), NOT deformation generators. Likewise the two frames needs an *actual* probe-response AND
> intrinsic-circulation pair, not just "feedback." If the field doesn't hand you the explicit linearization /
> the explicit two measurements, these primitives are off-limits — pick the regime/flow primitive instead. The
> failure pattern: reaching for the most *sophisticated-sounding* primitive when a basic one is the honest fit.

---

## 2. The per-row method (the three-column discipline)

Each row of your table has three columns + a grade:

| col | what goes here | the gate it enforces |
|---|---|---|
| **A — phenomenon** | a *named, established* object/effect in your field (not invented) | it must be real and standard in your field |
| **B — established dissipative home** | the field's **own** non-equilibrium/dissipative treatment of A, **with a citation** | the metabolize gate — if A has no dissipative treatment and isn't obviously a NESS structure, it is **not a row** (or it's a flagged gap, §6) |
| **C — character primitive** | the §1 primitive A maps to, with its `[anchor]` | the translation — pick the *one* primitive whose signature matches; if several fit, the phenomenon may be a within-field collapse (§5) |
| **grade** | `S` or `C`, + tight/loose (see §4) | honest scope |

**Procedure per candidate row:**
1. Name the phenomenon (col A).
2. Find its established dissipative/non-equilibrium home and cite it (col B). Pattern-formation, bifurcation,
   NESS, instability, dissipative-structure, self-organized-criticality, turbulence-cascade treatments are the
   usual homes. **No home, not obviously dissipative → not a row.**
3. Match col B's structure to the §1 signature it fits → col C.
4. Grade it (§4).
5. Apply §3 (the mint/supplied cut) — it often *is* the row's content.

**⚠ THE #1 FAILURE MODE — "a math model exists" ≠ "a dissipative home exists" (authenticity gate on col B).**
The single most common error is routing a row through *any* formal model of the phenomenon and calling it the
dissipative home. Col B must be a treatment of the phenomenon as **a dissipative / non-equilibrium / flow
object** — something with a drive, a dissipation, and dynamics whose *qualitative behaviour* (stability, cycle,
threshold-of-a-flow) is the content. **These are NOT dissipative homes by themselves:**
- a **Markov chain / stochastic process** is probabilistic structure, not dissipative dynamics — and an
  *absorbing/terminating* chain is the **antithesis** of a NESS (it ends; a NESS is sustained throughput);
- a **game-theoretic equilibrium / minimax / mixed strategy** is a static solution concept, not a flow (its
  *dynamical* cousin — replicator/evolutionary-game dynamics — IS a valid home; cite that, not the static
  equilibrium);
- an **optimization / expected-value argmax** is a decision rule, not a bifurcation of a flow.
If the only available home is one of these, either find the field's genuine dynamical treatment (replicator
dynamics, renewal/excitable model, bifurcation analysis of the flow) or **grade `loose` and say so** — never
`tight`. A row whose col B is "a formal model exists" is the over-claim the grades exist to catch.

---

## 3. The legal discipline — mint vs supplied (the sharpest lens)

This is the single most illuminating move, and the one most likely to surface something interesting. For any
**sustained structure** in your field, separate two things:
- **What it mints** (intrinsic, flows with the system): its **chirality / topology / handedness / sign** —
  the `Im λ` face. This is genuinely the system's own.
- **What it borrows** (supplied by the drive): its **amplitude / gain / energy** — the `Re λ` face. Cut the
  drive and this dies; the structure was *parasitic on the drive* for its magnitude.

**Worked exemplar (meteorology, the hurricane):** a cyclone's *rotation sense* (chirality) is intrinsic — set
by the system. Its *energy/intensity* (amplitude/gain) is **extracted from the sea-surface↔outflow temperature
gradient** (established: Emanuel's hurricane-as-Carnot-engine). Cut the gradient — a hurricane over cold water
— and it spins down. So a hurricane is **generative-of-circulation, parasitic-on-drive**. State this cut
explicitly for your field's sustained structures; it is usually the row's real payload.

(Background: MPA recently established that a cascade can *mint* chirality/topology but **cannot** mint
continuous-amplitude autonomy — the gain is always supplied. So when you find a structure whose *gain* appears
"self-sustaining," check what drive feeds it; the gain is supplied, the chirality is the system's own.)

---

## 4. Grading each row (honest scope)

- **`S` — structural** (most rows): a re-coordinatization of the field's established dissipative result.
  "Imported math; structural reach; not a measured character round-trip." This is the default and is fine.
- **`C` — character-grade** (rare, precious): the mapping is backed by an actual measured dynamical instance
  where the MPA reading was verified, not just analogized. Mark `C` **only** if you can point to such an
  instance; otherwise `S`.
- **Confidence within `S`:** *tight* (the field is explicit that the phenomenon is this dissipative structure —
  e.g. Rayleigh–Bénard convection, hurricane-as-heat-engine) vs *loose/analogical* (the mapping is suggestive,
  or the field's own treatment is itself contested — e.g. maximum-entropy-production conjectures). **Label
  each row's confidence.** A loose row is allowed; a loose row *mislabeled tight* is the failure.
- **GRADE-CEILING RULE (the deeper guard behind every over-map so far).** A row may be graded `tight` **only if
  the cited col-B home actually supplies the chosen primitive's own §1 signature** — not merely *a* dynamical
  model of the phenomenon. Ask: does the home produce the *specific structure the primitive names*? (deformation
  generators → an explicit Jacobian eigen-decomposition; k_frust → an N≥3 protected cycle; reservoir → sustained
  recharge; ignition → a flow whose fixed point changes stability). If the home is real but supplies something
  *weaker or adjacent* to the primitive, the ceiling is `loose`. "The field has a sophisticated model" never
  earns `tight` for a sophisticated primitive — only the matching signature does. (This is what both NFL passes
  missed: v1 graded `tight` on too-strong a structure, v2 on too-strong a primitive — same root, different costume.)

---

## 5. The collapse lens — what to foreground

Two kinds of "collapse" are the interesting output; foreground them in your "what this surfaces" note:
1. **Within-field collapse** — several of the field's *separately-named* phenomena map to the **same**
   primitive. (Meteorology: convection-onset, hurricane-genesis, precipitation-triggering, regime-transition
   are all **ignition/threshold**.) This says the field's distinct categories share one structure.
2. **The mint/supplied cut** (§3) applied across the field's sustained structures — usually the sharpest
   single insight per field.

(Cross-field collapse — the same primitive lighting up in *many* fields — is the integrator's job once
multiple columns exist; you don't need to do it, but flag any primitive that seems unusually load-bearing in
your field.)

---

## 6. Anti-drift — the checks, and what to do when a field resists

Run these before submitting. **If a check fires, the item is not a clean table row — split it out per the
instruction.** (These mirror the MPA "applications" register's discipline: the Rosetta *uses* the core, it does
not *extend* it.)

- **Check 1 — no structural verbs.** Your col B/C text must not use *proves / predicts / forces / requires /
  falsifies / establishes / cannot* in load-bearing position. You are *citing* the field and *matching* a
  primitive, not making a claim. ("Re-reads as," "maps to," "is the field's X seen as primitive Y" — good.)
- **Check 2 — no new falsifiers / kill conditions.** A Rosetta row never proposes a test that would refute
  something. If you find one, that's frontier material → flag it (below), don't table it.
- **Check 3 — no redefining primitives.** Use the §1 primitives as given. If none fit, see §6-FLAG.
- **Check 4 — col B must cite.** A row whose middle column has no established dissipative-home citation is not
  ready. Either find the home, or flag it as a gap.
- **Check 5 — substitution test.** If a sentence of yours, dropped into a core MPA document, would *change*
  what MPA claims, it's structural — cut it or flag it.

**§6-FLAG — the productive output when a field resists.** Three cases, each a *separate flagged list*, NOT a
table row:
1. **Gap** — an important phenomenon that has no clean dissipative home, or that the field has *not* connected
   to non-equilibrium structure. (MPA may be surfacing a connection the field hasn't drawn — the genuinely
   interesting case. Flag it; the integrator routes it to exploratory study.)
2. **New-structure candidate** — a phenomenon that would fit only if a *new* primitive existed. Describe the
   would-be primitive and the phenomenon. (This is how a field could *extend* MPA — but that is a deliberate,
   gated decision the integrator makes, never an auto-add.)
3. **Over-claim risk** — a row that's tempting but where the dissipative reading is weak/contested. Flag with
   your reservation rather than dropping silently.

---

## 6½. The messy-field wrapper — extra guards for the "handle-with-care" tier (§9)

The clean fields (fluid dynamics, optics, chemistry) need only §1–§6. The **contested** fields (economics,
AI, social, parts of physiology/ecology) carry high over-claim risk: thin consensus, rival schools,
equilibrium-theory baggage. Do **not** redesign the procedure for them — the honesty gates above were *built*
for this tension. Add only these four lightweight guards, in this order, **before** building the table. (They
are the containment pattern that produced a clean meteorology column despite that field's own internal
debates: select at the grain where consensus exists; quarantine the contested by grade; anchor on
thermodynamics, not school-of-thought.)

**A. Peanut-first scoping** (this *formalizes* §2's cite-gate as an explicit first step). Before any table,
list the field's **peanuts** — small, well-characterised sub-models with explicit equations of motion and
measured bifurcation/phase behaviour that *any school accepts as a dynamical system*. Build the core rows
**outward from the peanuts**, not from the field as a whole. Examples: economics → Keen–Grasselli
stock-flow-consistent Minsky model (debt = reservoir/release); AI → gradient-descent linearization near a
minimum / neural-tangent-kernel (Jacobian = deformation generators); physiology → Bergman minimal
glucose–insulin model (oscillation threshold = ignition); ecology/SES → fishery fold bifurcation under
harvest (metastable basins + ignition). The task is "build out from the peanuts," not "translate the field."

**B. Schools-of-thought preamble.** Write one paragraph of field-sociology first: which schools exist, what
they dispute, which peanuts *all* schools accept, which phenomena are championed by one school and rejected by
another. **Grading rule it imposes:** a row resting on a school-specific model is automatically `loose`
*regardless of mathematical tightness*, and its citation must **name the school**. When a phenomenon has rival
dissipative treatments, **list them both** and grade by the multiplicity, e.g.:
`| market crash as ignition | Sornette log-periodic vs Lux–Marchesi agent-based | ignition [§14] | S, loose (rival homes, none settled) |`
The disagreement becomes a *feature* of the table, not a flaw buried under a fake consensus.

**C. Drive-mandatory gate** (a HARD gate — this *operationalizes the bootstrap constraint*, §1/POSITS, and
makes §3's hurricane test mandatory). For **every** sustained structure proposed as a row, ask: *what is the
external drive, and what does the literature say happens when it is removed?* If the field **cannot name the
drive / throughput**, the structure does **not** get a row — it goes to §6-FLAG as an **"unidentified-drive"**
flag. This catches the most dangerous pseudo-autonomy over-claims at the door (e.g. an economy "minting"
growth with no specified energy/material/credit throughput that supplies it; growth is *supplied*, like every
gain — receipts §amplitude-autonomy).

**D. Adversary-anchor citation** (the existence-vs-cause cut — the load-bearing move). In a contested field,
build the row on the model the **contrarians themselves** use as their starting point — the *common adversary*,
not the winning side (BZ chemistry → Oregonator/FKN, which all sides argue *from*; economics → the
Hicks–Metzler inventory cycle or Phillips curve; AI → the empirical fact of double descent everyone must
explain). The cut that makes this work: **map the dynamical *regularity* both schools accept (that is the
row); grade the *causal interpretation* `loose` (that is the dispute).** A Phillips-curve row maps the
inflation–unemployment *regularity*, not anyone's theory of *why* — so it survives the factions.

**On flag-heavy columns (temper).** A messy field will yield many `loose` rows and a long §6-FLAG list. That
is **informative** — it maps the boundary of where the dissipative framing reaches and where the science is
unsettled. But a high flag-ratio is a **finding, not a goal**: it can equally mean the field resists the
framing *or* that MPA has little to say there. Do not pad flags or valorize flag-count. Report the ratio
honestly; let the peanuts carry the column.

---

## 7. Output format — return each field like this

```
# <Field> — dissipative Rosetta column

**NESS framing:** drive = <energy source>; sink = <dissipation>; the steady state = <one line>.

**Schools-of-thought preamble** (handle-with-care fields only — §6½ B): <one paragraph: rival schools, what
they dispute, which peanuts all schools accept, which phenomena are school-specific>.

**Peanuts** (§6½ A): <the small, all-schools-accept sub-models the core rows build outward from>.

## Table
| phenomenon (A) | established dissipative home + citation (B) | character primitive [anchor] (C) | grade |
|---|---|---|---|
| ... | ... (Author Year) | ... [primitive] | S, tight |
| ... | ... | ... | S, loose |
| ... | ... (instance verified ...) | ... | C |

## What this surfaces
- within-field collapses (which separate phenomena share one primitive)
- the mint/supplied cut for this field's sustained structures
- the one or two most striking re-readings

## Honest scope
- which rows are tight vs loose; what is NOT claimed (no character round-trip unless a row is graded C).

## Flagged for review (NOT table rows)
- gaps · unidentified-drive (§6½ C) · new-structure candidates · over-claim risks  (per §6-FLAG)
- flag-ratio (rows : flags), reported honestly — a finding, not a target (§6½ temper)
```

Keep each cell terse. The citation is mandatory in col B. Leave col C's `[anchor]` exactly as in §1.

---

## 8. The worked exemplar (meteorology) — your model

The meteorology column is already built (`dissipative_rosetta_meteorology.md`); use it as the pattern. Its
spine, abbreviated:

| phenomenon | established home | primitive | grade |
|---|---|---|---|
| convection onset | Rayleigh–Bénard / dissipative structures (Prigogine, Nicolis) | **ignition (c/s/r)** | S, tight |
| hurricane | hurricane-as-Carnot-engine (Emanuel 1986/91) | **k_frust + chirality, parasitic-on-drive** | S, tight |
| rotation sense (cyclonic hemisphere) | Coriolis / geostrophic balance | **topological bit / sign(𝒜)** | S, tight |
| precipitation (CAPE charge→trigger→release) | convective available potential energy | **reservoir/release register** | S, tight |
| jet streams / Rossby waves | baroclinic instability (Charney–Eady) | **platformed topology** | S, tight |
| blocking highs / regimes | Charney–DeVore multiple equilibria | **metastable basins** | S, loose |
| weather → climate | turbulent cascade / scale separation (Charney 2D) | **heat-tax tower / plateau ladder** | S, tight |
| atmosphere as a whole | driven-dissipative NESS; MEP (Paltridge) | **substrate-is-NESS** | S, loose (MEP contested) |
| Lorenz predictability limit | Lorenz 1963 deterministic chaos | **Wall / loss of normal hyperbolicity** | S, tight |

Its two headline "surfaces": (1) convection-onset, hurricane-genesis, precip-trigger, regime-transition all
collapse to **ignition** — one structure, four atmospheric guises; (2) the hurricane mint/supplied cut —
rotation minted, energy supplied — is the cleanest statement of "generative-of-circulation, parasitic-on-drive"
in any real system.

### 8b. Worked REJECTIONS (from the NFL play-calling column, 2026-05-31) — the three over-maps to avoid

A real handle-with-care column got the wrapper right but slipped the *primitive-matching* three times, all the
same way: **a formal model was mistaken for a dissipative home** (§2 authenticity gate). Use these as
do-not-repeat examples:

| tempting row | why it's WRONG | correct handling |
|---|---|---|
| football drive → **reservoir/release**, `tight`, via an *absorbing* Markov chain (Goldner 2012) | an absorbing chain **terminates** — antithesis of a sustained NESS; a stochastic-process model is math, not a dissipative home | grade `loose`, or re-anchor on a genuine renewal/excitable model of the *possession-exchange loop* (the sustained thing) |
| run/pass mixing → **k_frust**, `tight`, via minimax / negative serial correlation (Emara 2017) | binary alternation is **N=2 → gauge-removable → NOT protected**; a mixed-strategy equilibrium is static, not a flow | genuine k_frust needs **N≥3 cyclic dominance** (replicator dynamics over ≥3 play archetypes) — cite *that* sub-literature, or it's not k_frust |
| 4th-down go/kick → **ignition**, via expected-value optimization (Jordan 2009) | a static argmax decision boundary is not a bifurcation of a flow | map to a decision/threshold note, not ignition |

Common root: each had *a* model, none had a *dissipative/flow* home. The grades and the §1 discriminators are
the catch — when in doubt, `loose` + a §6-FLAG, never a `tight` over-map.

**8c. The v2 slip (after the v1 gates were added) — the over-map jumped one level up.** The corrected column
moved all three v1 errors into the flag list (good) but introduced a NEW `tight` over-map:

| tempting row | why it's WRONG | correct handling |
|---|---|---|
| strategy adaptation → **deformation generators**, `tight`, via replicator dynamics | "has adaptation/dynamics" ≠ "supplies an explicit Jacobian eigen-decomposition"; deformation generators is an *advanced* primitive reached for because it sounds sophisticated | replicator converging to a stable mix is **c/s/r / ignition** (a flow with attractors); grade-ceiling caps it at `loose` unless the field literally linearizes |

**The deeper lesson (banked for the integrator, not a row): the over-map RE-APPEARS one level up after each
gate.** v1 over-reached on *structure* (k_frust for N=2) → gated; v2 over-reached on *primitive sophistication*
(deformation for "adaptation") → now gated by the advanced-primitive guard + grade-ceiling. Expect the next
costume. **And the missed collapse worth chasing:** replicator dynamics over **≥3 mutually-countering
strategies** IS N≥3 cyclic dominance = RPS/May-Leonard = the framework's own k_frust flagship. A column that
routes ≥3-strategy play-archetype adaptation to **k_frust in strategy space** would surface the genuine
cross-column collapse (behavioral ⟷ ecological ⟷ the Central Commitment) — the real prize the NFL field was
sitting on (it has the data; "lots of available data" is exactly why it's a candidate `C`-grade behavioral
instance). Route that to frontier/applications, never auto-land.

---

## 9. Candidate fields, roughly by expected tightness

A starting menu (not exhaustive — MPA is substrate-general, so most sciences with sustained driven structure
qualify):
- **Tightest (dissipative-native — §1–§6 suffice):** ecology/population dynamics (predator-prey cycles,
  RPS/rock-paper-scissors — already a verified MPA instance, likely the first **`C`-grade** column), chemistry
  (oscillating reactions, BZ → build on Oregonator/FKN, the common adversary; autocatalysis/chirality),
  nonlinear optics (laser threshold/relaxation oscillation), fluid dynamics (instabilities, turbulence),
  condensed matter (phase transitions, glasses, active matter).
- **Mid (§1–§6, light wrapper):** neuroscience (excitable dynamics, criticality, up/down states =
  reservoir/release), epidemiology (SIR thresholds = ignition), geophysics (earthquakes/SOC), developmental
  biology (pattern formation/Turing), physiology (Bergman glucose–insulin peanut = ignition).
- **Handle with care (§6½ wrapper MANDATORY):** economics & markets (Minsky/Keen–Grasselli + Hicks–Metzler
  peanuts; equilibrium-theory baggage — grade most rows loose, drive-gate every "growth/self-sustaining"
  claim), AI/ML (NTK-linearization peanut = deformation generators; double descent as the common-adversary
  fact), social dynamics, linguistics, social-ecological systems (fishery fold = metastable basins). Highest
  over-claim risk; the schools preamble + drive-mandatory gate + adversary-anchor are required, not optional.

Return one column per field in the §7 format. The integrator assembles them, resolves cross-field collapses,
and decides any new-structure flags through the framework's own gate — none auto-land.

---

*Placement note (for the integrator, not the outside model): this procedure is a working/method doc in
`docs/`. The columns it produces are **applications**-register artifacts (use the core, do not extend it) and
land via `character_applications.md`'s authoring procedure + anti-drift checks. New-structure flags route to
`character_frontier.md` steeping, never auto-added. Whether the assembled Rosetta earns a standalone `mpa_rosetta.md`
is a `developed`-grade decision once ≥2 columns (one tight `S`, one `C`) exist.*
