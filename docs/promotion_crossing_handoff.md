# Real-Substrate Crossing — Promotion-Queue Handoff (2026-05-30)

**Read cold. This is the active baton.** The campaign's first commit-line crossing just landed, and
it revealed a **repeatable strategy** for crossing the rest of the queue. Continue that process.

## STATUS (one line)

`central-commitment` + `two-frame-construction` **promoted staked→core** via a real emergent substrate
(rock-paper-scissors); the queue is no longer dammed — the path to feed it is now known and cheap.

---

## THE BREAKTHROUGH (the strategy — use it)

For the whole campaign every staked claim was stuck behind one gate: *needs a real substrate, not
synthetic.* That gate is now openable, on two realizations:

1. **REAL = EMERGENT, not physical.** A simulation is a **real instance** iff its structure *emerges*
   from generic rules + noise rather than being *drawn in by hand*. RPS's circulation, a glass's
   aging, a library primitive's dynamics — all emergent → **vindication-grade, not calibration.**
   (Authored = hand-drawn = synthetic = calibration. The distinction is authored-vs-emergent, never
   computational-vs-physical. This is the framework's own criterion — the library already grants its
   glass/quantum sims real status.)
2. **CIRCULATION gates are cheap; RESPONSE gates are expensive.** The circulation/triad claims read a
   **current** (J, 𝒜) *directly* from the unperturbed dynamics — no perturbation, no ensemble-averaged
   response, no estimator. The FDR/aging claims need a **perturbation response** (χ) — ensemble
   averaging, big runs, and a subtle estimator. **Prefer direct observables.** RPS crossed in 58 s;
   the SK/FDR probe was compute-marginal and ate hours.

**The template (RPS, `mpa-conform/scripts/rps_triad.py`):** pick an emergent substrate that carries
the structure a gate needs → measure the gate's observable *directly* → show the protected/invariant
part is drive-independent and the amplitude flows → run the null control → cross. 58 seconds, clean.

---

## ⚠ THE FAKE-NaN RULE (read this — it has bitten us THREE times)

**When a readout produces NaN, garbage, or an extreme value, suspect the READOUT, not the substrate.**
The recurring failure is **reading a local/pointwise quantity of a noisy or degenerate field instead
of the global invariant.** Instances so far:

- **tower_chaos_diagnostic:** a positive *finite-time* Lyapunov tail on a torus looked like chaos. It
  was just non-uniform flow speed. The global invariant (Poincaré section / full spectrum) said
  "smooth torus." → read the global invariant, not the local fluctuation.
- **wall-forces-chaos:** reading the Wall (a degenerate boundary) by *importing a limit-case result*
  instead of *entailing it from interior structure*. Boundary behavior is an entailed theorem of the
  interior — never asserted at the degenerate point (now codified in the membership self-test (iii)
  and frontier I6).
- **SK gFDR (this session):** my X-readout took **local slopes/gradients of a noisy χ-vs-C curve** →
  X = −4.19, NaN, a paramagnet "overshoot." Ron called it immediately: *"it could be your test… is
  this a place where the fake NaNs show up? increase the samples."* Both fixes were exactly right —
  (a) replace the local-slope readout with the **global** invariant (mean *peel below the FDT line*),
  and (b) raise n_real so the estimator's noise averages out (the overshoot 1.37→1.03 at n_real=10k
  was pure finite-sample noise in *my* estimator, not the substrate).

**The rule, operational:**
- A NaN / wild value at a degenerate point or from a local gradient = **a malformed readout, not a
  result.** Do not report it as a finding; fix the readout.
- **Read the global invariant** (the overall shape, the integrated/averaged quantity, the topological
  invariant) — not the pointwise slope/angle/clock of a noisy field.
- **Beat noise with samples** before concluding (but size the run — see below). If more samples make
  the "anomaly" vanish, it was the readout.
- This is the same family as: NaN-at-orthogonal-zeros (never read the pointwise angular clock at the
  polar origin), FTLE-tail-on-a-torus, and boundary-import-vs-interior-entailment.

**Operational companions (also banked this session):**
- **Tests under one hour** (`feedback_keep_tests_under_one_hour`). A "30-min" SK run took 4+ hours —
  cost goes **super-linear at large n_real** (memory-bandwidth-bound). **Time a small probe, measure,
  extrapolate with a ~3× margin, size comfortably under 1 hr** *before* launching. Never trust an
  a-priori estimate.
- **Cheap direct observables over expensive ensemble responses** (the circulation-vs-FDR split above).

---

## WHAT CROSSED (the mechanics — reuse them)

`battery:sign-interior` RV1 fired on RPS → `central-commitment` + `two-frame-construction` (mutually
entailed) crossed staked→core. The exact edit pattern for any future crossing:

1. **Frontier:** mark the battery entry RV1-fired (the breadcrumb); **remove** the promoted
   `staked:*` entries from the STAKED section (they are load-bearing now, off the frontier).
2. **Receipts:** retag the entry `staked → proven` and append the **real-instance evidence**; add a
   **`§commit-line crossing`** entry to `## CORRECTIONS & PROMOTED REFINEMENTS` recording *what
   crossed, the evidence, the honest scope, and which core docs absorbed it* (GATES requirement).
3. **Engine:** usually **no edit** — staked claims already live in the engine as declarative text.
   Keep it **forward-only, no navel-gaze**; lineage lives in receipts/frontier (the tracking docs).
4. **Fix stale pointers:** grep for `staked:<key>` and "both staked claims" — patch them in passing.
5. **I1 check:** every `staked` receipts entry ↔ one `[staked]` frontier entry. Retag + removal must
   stay in sync.
6. **Scope honestly in the log:** one instance is the gate's "a real instance," but record the scope
   (single instance, noise model). **Do not over-promote adjacent claims** — `two-bits` and
   `homochirality` were *supported* by RPS but stayed staked (RPS isn't their specific instance).

---

## THE QUEUE + PRIORITIZED NEXT MOVES

Ledger now: **staked 6** (was 8), **battery 3** (sign-interior fired). Prioritized by
leverage-per-cost — the cheap emergent/circulation crossings first:

1. **`character-primitives` via RPS (HIGH leverage, cheap).** RPS *is* the C3-symmetric protected
   arena the deformation-algebra was waiting on. Run the deformation apparatus
   (`character_closure.py` generators / the gl(3) Cartan picture) **on RPS**: does RPS's character
   compose from the generators, and does the protected meta-cycle survive RPS's native deformations
   within its C3 symmetry? If yes → `staked:character-primitives` crosses (the structural-law
   promotion lands on a real arena). This is the natural next crossing.
2. **`two-bits` via RPS floor-isolation (cheap).** RPS already shows the topological bit is *free to
   hold* and *flips only by rewiring*. Owed: the **floor-isolation protocol** — a quasistatic
   handedness flip *through the balanced (achiral) state* measuring the **≥1 ch** cost, split from the
   rewiring work. Extend RPS with that protocol → crosses `two-bits`.
3. **`homochirality` via a chiral-autocatalysis sim (cheap, named stake).** RPS is *adjacent*
   (ecological, not biochemical). Build a Frank / Kondepudi chiral-autocatalysis network (another
   emergent substrate), drive-sweep: magnitude→racemic while sign invariant; the three nulls.
   Crosses the named real-substrate stake.
4. **`wall-as-type-boundary` via `battery:wall-ladder` on a real cascade (medium).** Run
   `clv_diagnostic.py` (θ_min, already validated) on a real *emergent multi-scale* substrate's RG
   levels — read them as NHIM plateaus, drive one to ε→1, watch θ_min→0. A coupled-oscillator or
   reaction-diffusion cascade could serve.
5. **(Lower — the expensive FDR/response gates.)** `gfdr-two-step` (SK is compute-marginal; if pursued,
   use the **no-field Chatelain/Ricci-Tersenghi estimator** to avoid the two-branch decorrelation,
   not the step-field method), `memory-collapse` (fbm/east, β_mem(ε)), `seam-collapse`/`thm9-crossover`,
   `auto-tuning`. Deprioritize vs the circulation crossings unless specifically wanted.

Recommended single next move: **#1 (character-primitives on RPS)** — highest leverage, cheap, and it
completes the deformation-algebra arc this session staked.

---

## APPARATUS (mpa-conform/scripts/)

- **`rps_triad.py`** — the RPS chimeric-triad instance + the crossing template (the one to extend).
- **`sk_gfdr_twostep.py`** — calibrated FDR diagnostic; the **staggered-field** estimator + the
  finding that the library's generic FDR protocol applies a uniform field (FDT-mismatched to the
  self-overlap). The expensive path; calibrated but compute-marginal at N=100.
- **`character_closure.py`** (gl(3) Cartan closure), **`clv_diagnostic.py`** (θ_min NHIM diagnostic),
  `character_primitives.py`, `chiral_*`, `frustration_ascent.py`, etc. — the character/cascade line.
- Library: **`H:/mpa-central/library/primitives/`** — ~15 emergent substrates (sk, east, fbm,
  lotka_volterra, driven_ring, logistic_chaos, …) running a shared paired-FDR protocol. Useful for
  the FDR gates; **no 3-cycle** in the library (RPS fills that gap — consider promoting RPS into the
  library as a primitive if reused).

## RELATED HANDOFFS / RECORD

- `character_engine_promotion_handoff.md` — the character-deformation-algebra baton; its goal
  (`character-primitives` to `staked`) is **done**; the next step is #1 above (cross it on RPS).
- Crossing logged in `mpa_receipts_engine.md` `§commit-line crossing`; frontier reflects the new
  ledger. Memory: `project_frustration_ascent_recursion.md`.

## DISCIPLINE

Emergent = real (vindication, not calibration). Keep the engine forward-only. Hold weighty canonical
edits for review, but the crossing pattern is established. Strict scope in promotion logs. Tests under
one hour; probe-then-extrapolate. **And whenever a number looks wrong: suspect the readout — read the
global invariant, beat the noise — before suspecting the substrate.**
