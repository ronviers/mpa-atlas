# Real-Substrate Crossing — Promotion-Queue Handoff (2026-05-30)

**Read cold. This is the active baton.** The campaign's first commit-line crossing just landed, and
it revealed a **repeatable strategy** for crossing the rest of the queue. Continue that process.

## STATUS (one line)

`central-commitment` + `two-frame-construction` **promoted staked→core** via a real emergent substrate
(rock-paper-scissors); the queue is no longer dammed — the path to feed it is now known and cheap.

---

## BATCH STATUS — 2026-05-30 (three more crossings tested; HELD for review, nothing landed)

Three queue items run as falsification-grade experiments (strict pre-registered bars). Scripts +
figures on disk; **no canonical ledger edits, no commits** — all awaiting review. The ledger crossings
are staged (exact edits noted). Permanent home once they cross = frontier (staked-removal) + receipts
(staked→proven + §commit-line crossing); this section is the durable record until then.

1. **`character-primitives` → CROSSES (5/5)** · `mpa-conform/scripts/rps_character.py` · fig
   `output/calibration/rps_character.png`. The gl(3) deformation apparatus on RPS's **emergent**
   Jacobian: M_RPS *produces* $A_{\text{CYC}}$ (Antisym $=x^*(\alpha-\beta)/2\,A_{\text{CYC}}$, residual
   **0** — chirality generator emergent, not hand-drawn, forced onto the $(1,1,1)$ $\mathfrak{so}(3)$
   axis); forced EP normal form $R^2{=}1.0000$; C3-meta-arena lift closes (b1 3→4, **0%** generic
   closure, $\omega_{\text{meta}}\propto\kappa^{1.93}$ vs split $\propto\kappa^{1.01}$). One FAKE-NaN
   trap caught+fixed mid-run ($\kappa{=}0.3$ over-drove RPS's weakly-damped (0.1) chiral modes into
   instability; the global spectrum revealed it; scaled $\kappa{=}0.4\,\gamma_{\text{rot}}$). **Staged
   crossing:** engine line 67 ("staked, un-instanced" → "instanced on RPS"); receipts
   §deformation-generators staked→`proven` + RPS evidence; new §commit-line crossing(2); frontier
   remove `staked:character-primitives`, update the `frustration-ascent` structural-side note.

2. **`homochirality` → CROSSES (4/4)** · `mpa-conform/scripts/homochiral_triad.py` · fig
   `output/calibration/homochiral_triad.png`. **Built a genuine emergent substrate:** two MIRROR chiral
   3-cycles + Frank cross-inhibition. Spontaneously breaks parity (|ee|→1); the winning hand carries a
   **protected 3-cycle NESS circulation** (complex pair $-0.1\pm0.173i$, $\mathcal{A}\ne0$); drive-sweep
   $|J|\propto\sigma^2\to0$, sign held; **beats all three nulls** — incl. the trap, the 2-component
   Frank bistable (homochiral but $\mathcal{A}{=}0$ ⇒ the frustrated triad is necessary). Also instances
   `frustration-ascent`'s **self-lighting leg** (the spontaneous SSB RPS lacked). **Parity finding
   (Ron's catch — methodological):** the SSB split is **exactly 50/50 by an exact mirror symmetry**
   (equivariance residual $7\!\cdot\!10^{-15}$; aggregate 2000 ICs → $0.492\pm0.011$, 0.7σ; parity-paired
   ICs → **exactly 500/500**). The early 37/63 over 100 ICs was finite-sample — the *fix* was to
   demonstrate the symmetry (equivariance + paired ICs), not chase Monte-Carlo convergence. Physically:
   zero built-in chiral bias = a clean frozen-accident SSB (explicit-bias mechanisms, e.g. weak-force
   parity violation, are a separate add-on, out of scope). **Staged crossing:** receipts §Homochirality
   staked→`proven` + homochiral-triad evidence; frontier remove `staked:homochirality`; record in
   §commit-line crossing(2). (Scope: a model Frank/Kondepudi-class network — models biological
   homochirality, is not the literal ancient biochemical substrate.)

3. **`two-bits` → a CORRECTION to engine §Two bits (NOT a crossing); held for review** ·
   `mpa-conform/scripts/rps_two_bits.py` · fig `output/calibration/rps_two_bits.png`. **Ron's catch (the
   fake-NaN-at-zero rule, to its conclusion): "it cannot cost anything to flip the sign."** A flip
   $+1\!\leftrightarrow\!-1$ is a bijection (NOT gate) ⇒ logically REVERSIBLE ⇒ by Bennett NO Landauer
   floor; the $\ge1$ ch is the ERASURE cost (many-to-one), wrongly imported onto a flip. It only appears
   if you route the flip *through* the balanced state $\mathcal{A}{=}0$ — but that is the NEVER-ATTAINED
   boundary, and the per-flip cost there is an indeterminate fake-NaN ($0/0$). Verified: rewiring is a
   reversible **involution** ($-1\!\to\!+1\!\to\!-1$, the topological-qubit *braid*, never instantiates
   $\mathcal{A}{=}0$); and the would-be per-flip cost $\langle\sigma\rangle/\omega$ VARIES continuously
   ($4.16\!\to\!2.08\!\to\!0.42$, crosses ln2, dips below it) $\to0/0$ at balance — **no fixed floor.**
   So the topological SIGN bit is **free BOTH ways** (hold + flip). My earlier "entailed $b_1$ floor"
   reading was a half-measure — it still imported a cost living only at the never-attained zero.
   **What survives (cleaner):** the two bits are NOT "two costs, one per face." AMPLITUDE bit =
   *dissipative* (a real interior cost: maintenance $\langle\sigma\rangle{=}0.6$, leaks without drive);
   SIGN bit = *topological* (no interior cost; any flip cost is substrate-specific rewiring work, e.g.
   the homochirality racemic-saddle height, never a universal $\ge1$ ch). **PROPOSED ENGINE CORRECTION
   (held):** §Two bits / engine BITS — drop "$\ge1$ ch per protected sign to modify" + the $b_1$-ch
   forced-erasure floor *as a cost*; keep free-to-hold, gauge-irremovable, flips-only-by-rewiring (now a
   free reversible braid). Same error family as wall-forces-chaos: a quantity formulated at the degenerate
   boundary instead of entailed from the interior. (`staked:homochirality` + `central-commitment` are
   unaffected — none asserts the $\ge1$ ch.)

4. **`wall-ladder` — DEFERRED** (not built). CLV $\theta_{\min}$ diagnostic is built+validated; the
   vindicate needs a "real emergent cascade" driven to closure-loss ($\theta_{\min}\to0$), and *which*
   substrate counts as real-emergent-multi-scale is the substrate-judgment call flagged as Ron's. The
   expensive FDR gates (`gfdr-two-step`, `memory-collapse`) left alone per the cheap-observables discipline.

**Ledger if the staged crossings land: staked 6 → 4** (`character-primitives`, `homochirality` cross;
`central-commitment`+`two-frame` already crossed). **`two-bits` is now a CORRECTION, not a crossing** —
the engine §Two bits "$\ge1$ ch to modify" fires (boundary fake-NaN); its exact ledger disposition
(revise `staked:two-bits` to "free both ways" vs a §Two bits correction entry) is Ron's call.

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
