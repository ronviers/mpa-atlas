# Frustration-Ascent Cascade — Closure Handoff (2026-05-30)

**Read cold. This is the active baton for closing `frustration-ascent`'s cascade.** It supersedes the
substrate-hunt thread that spiralled out of `promotion_crossing_handoff.md` §THE FOUR MOVES (move #1).

## STATUS (one line)

The hunt for a substrate to close `frustration-ascent`'s joint resolved into: the single-substrate
**triple obstruction is SAME-LEVEL, not hierarchical**; a **stratified two-level cascade** both evades it
AND genuinely **GENERATES** a new autonomous register (base self-lights + selects handedness; the upper is
its own limit cycle that survives drive-removal). **THE OPEN CRUX:** in the demonstration the upper's
*autonomy* was **architecturally inserted** (a μ>0 Hopf placed by hand). The remaining uncertainty is
whether that autonomy can **emerge from coarse-graining** the base (genuine generation) or must always be
supplied (conditional generation — base only selects the handedness of a pre-existing register). **Two
next moves: (1) the full end-to-end stratified run; (2) the coarse-graining-emergence test — which
localizes the uncertainty exactly.** `frustration-ascent` stays `[sharpening]`.

## THE ARC (how we got here — read once, don't re-walk it)

#1 (the homochiral joint) was a **clean miss** (tilt-brittle). Chasing closure:
1. **Isotropy diagnosis** (`cascade_isotropy_diagnosis.py`): the #1 brittleness was **substrate-specific**
   — the homochiral winner's *weakly-damped chiral plane* (Re −0.1 vs collective −1), not the platforming
   mechanism. An isotropic (gapped) sub platforms a tilt-robust meta-cycle (θ_c→24°). May-Leonard is
   *intrinsically* anisotropic, so this needed a different substrate.
2. **Outbound research ×2** (`cascade research and prompt.md`): the closable single-unit is a **Z₂ splay**
   in a repulsive C₃ ring (BZ-droplet-realized, Fraden) — self-light + gapped. The decisive single-unit
   property (round 2): the chiral mode must be **gapped**, which needs **discrete** chirality (a continuous
   rotational SSB keeps a soft Goldstone phase mode regardless of distance from the EP).
3. **`splay_cascade.py`**: the splay self-lights + is gapped BUT **does NOT cascade** — its collective Schur
   reduction is **exactly symmetric** (the C₃ graph Laplacian), real-spectrum, no antisymmetric seed → +0.
4. **My over-reach + the outside correction** (`cascade outside opinions.md`): I called this a structural
   "triple obstruction → bootstrap-blocked." Model a + a non-normality check **walked it back**: the splay
   fails via *gradient-like collective reduction* (a property of that mechanism), NOT discreteness;
   discreteness does not forbid complex pairs. **The triple is an empirical pattern, not a theorem; it is a
   SAME-LEVEL closure obstruction, not a hierarchical one.**
5. **`hybrid_cascade.py`** (loophole b — stratify the roles, all 3 models endorse): a splay BASE transduces
   its self-lit Z₂ into a gapped Banach-class UPPER (100% consistent sign-lock, follows base flips). The
   transduction-observable lesson: drive from the base's **m=1 spatial projection** (carries the Z₂ as a
   rotation sense, monochromatic), NOT the m=3 order parameter Z₃ (chirality-BLIND).
6. **`hybrid_generation.py`** (the outside model's transduction-vs-generation distinction): the
   hybrid_cascade upper was a *passive damped focus* (weak/transduction). With an **autonomous** upper (μ>0
   limit cycle, handedness a bistable Z₂ var the base only *biases*), the upper **survives drive-removal**
   (100%, |z|→√μ, keeps its own winding) and **holds the base-selected handedness** (100%); the weak (μ<0)
   control decays. ⇒ **GENERATION** — the oscillation is the upper's own; the cascade spins up a new
   autonomous register, base self-lights + selects handedness. (Note: ALL our chiral substrates —
   RPS/homochiral/Banach — are noise-driven *foci* that decay without the drive; only the splay and
   Stuart-Landau limit cycles are autonomous.)

## WHERE THE REMAINING UNCERTAINTY LIVES (the center — Ron's question)

Decompose what the cascade must do at each ascent into THREE things, and track which is *emergent* vs
*inserted* across the apparatus:

| | b₁+1 (new protected cycle / topology) | handedness (which way) | **autonomy (a real limit cycle)** |
|---|---|---|---|
| `frustration_ascent` (linear) | **EMERGES** (coarse-grain → meta-triad) | emergent | ✗ — a damped **focus**, not autonomous |
| `splay_cascade` (coarse-grain splay base) | — | — | ✗ — gradient-like **node**, not autonomous |
| `hybrid_generation` | (single unit) | base **selects** it | ✓ but **INSERTED** by hand (μ>0 Hopf) |

So: **the topology (b₁) emerges from coarse-graining; the handedness can be selected from below; but the
AUTONOMY — the upper being a genuine limit cycle rather than a noise-driven focus — has only ever been
inserted.** That single quantity is where the uncertainty lives, and it is exactly the *generative-vs-
parasitic* (layer-2 I5) question: does the cascade **create** the upper register, or only **select the
handedness of a register that was supplied**?

Coarse-graining is the right probe because it asks the question cleanly: feed a *nonlinear, gain-bearing*
base (autonomous, self-lit) up through Π_slow and ask whether the collective effective dynamics
**Hopf-bifurcates into an autonomous oscillator** (gain transferred → emergent upper limit cycle) or stays
a damped focus (gain stuck in the base → upper must be inserted). The b₁ already threads up; the test is
whether the **gain/autonomy** threads up with it.

## NEXT MOVES

### Move 1 — the full end-to-end stratified cascade (ties transduction + generation + meta-arena + tilt)
One run, three base→upper composites, C₃-covariant meta-arena, with tilt. Confirms the *architecture*
works end-to-end (uppers still inserted):
- 3 **splay bases** (each self-lights a Z₂; both basins).
- 3 **autonomous upper registers** (μ>0 Hopf, bistable-handedness `s`), each with its handedness *biased*
  by its base (the validated transduction; drive = the base's m=1 spatial projection).
- **C₃-covariant even-parity** meta-coupling among the 3 uppers (the `character_closure` meta-arena).
- **Reads:** (a) bases self-light, uppers lock to them (transduction); (b) uppers survive base-removal
  (generation — drive-removal test on each); (c) the meta-arena platforms a **meta-cycle** (collective
  complex pair / b₁ up) from the 3 self-lit gapped uppers; (d) the meta-cycle **survives tilt** (θ_c~κ, the
  gapped-→-robust result). Expected: passes (each piece is shown; this ties them). KILL if the meta-cycle
  fails to appear or is tilt-brittle when assembled (an assembly-level surprise).
- Apparatus to reuse: `hybrid_generation.py` (base→autonomous-upper), `character_closure.py` /
  `cascade_isotropy_diagnosis.py` (the C₃-covariant meta-arena + tilt; gapped subs → robust).

### Move 2 — THE DEEP TEST: does the upper register EMERGE from coarse-graining? (localizes the uncertainty)
Replace the *inserted* μ>0 upper with one that must **emerge**. Build a base level whose **collective**
mode (after coarse-graining the fast base modes, Mori-Zwanzig Π_slow) **Hopf-bifurcates into an autonomous
chiral limit cycle**, inheriting the base's gain + chirality.
- **The question:** is the coarse-grained collective an autonomous oscillator (a complex pair with
  *positive* growth → limit cycle, survives elimination of the fast base modes) or a damped focus (μ_eff<0,
  not autonomous)?
- **Candidate mechanisms for autonomy-transfer** (the collective Hopf): **non-reciprocal** collective
  coupling among the bases (Fruchart non-reciprocal transition — the collective order parameter goes to a
  chiral limit cycle; `pa:nonreciprocal-transition`), or **delayed** collective feedback (delay-Hopf,
  §14 / `pa:delay-hopf` — note: this is also the deferred `wall-ladder` closure-loss route, so the two
  threads may converge), or net **gain** routed into the collective sector.
- **Verdict logic:** collective autonomous + chiral → the upper **EMERGES** = **genuine generation** (the
  cascade creates the register; the layer-2 generative bet is vindicated at the mechanism level, on a
  coarse-graining, not an insertion). Collective stays a focus → generation is **conditional** (the upper's
  autonomy must be supplied; the cascade selects handedness but does not create the register) — itself a
  sharp, honest result that pins the layer-2 claim to "selective, not creative."
- This is the test that **decides whether `frustration-ascent`'s generative bet is genuine or conditional**,
  and it is the natural next thing after Move 1.

## DISCIPLINE / PITFALLS (these bit this thread — honor them)

- **FAKE-NaN readouts bit twice.** (i) `splay_cascade`'s naive "smallest-|Re| modes" reported a 0.155
  "meta-cycle" that was the **intra-ring splay rotation** (a single ring already has it). (ii) The constant
  value + uniform==covariant were the tells. **Use the proper collective Schur projection** (onto the
  per-ring (1,1,1) nodes), never "smallest |Re|". Suspect any suspiciously-constant or control-insensitive
  number.
- **Check non-normality, not just eigenvalues.** A real-spectrum collective operator can still seed via
  transient growth (loophole c). The splay's was *symmetric* (ruled out), but always check ‖[J,Jᵀ]‖ /
  sup‖e^{Jt}‖ before concluding "+0, no seed."
- **The transduction observable matters.** The m=3 order parameter Z₃=e^{i3φ} is **chirality-blind** (the
  collective phase rotates with a fixed sense); the chirality lives in the *spatial firing order*. Use the
  **m=1 spatial projection** (carries the Z₂ as a rotation sense, monochromatic — no harmonic comb).
- **emergent = real, and INSERTED ≠ emergent.** The base self-lights (emergent). An *inserted* μ>0 upper is
  architectural, not emergent — which is exactly why Move 2 (emergence from coarse-graining) is the real bar.
- **Don't elevate empirical patterns to structural laws.** I called the triple "bootstrap-blocked"; outside
  review walked it back to "same-level, not hierarchical." State patterns as patterns.
- **Honest scope.** Everything here is synthetic (emergent base, but a minimal model). The `hybrid_generation`
  result is a *mechanism* demonstration with an *inserted* upper; the meta-arena robustness is by composition,
  not a full end-to-end run (Move 1 fixes that). A real emergent instance (BZ-droplet base + a chiral-resonator
  upper class) remains for a `battery`/crossing.

## APPARATUS (mpa-conform/scripts/) + RECORD

- `hybrid_generation.py` — base→**autonomous** upper, drive-removal test (GENERATION). The newest, the one to extend for Move 1.
- `hybrid_cascade.py` — base→passive upper (transduction; the m=1-drive transduction validated here).
- `splay_cascade.py` — the splay does NOT cascade (+0, gradient-like collective). The negative that set up the hybrid.
- `cascade_isotropy_diagnosis.py` — gapped subs platform tilt-robustly (θ_c→24°); the #1 brittleness is substrate-specific.
- `character_closure.py` / `chiral_bonding.py` — the C₃-covariant meta-arena (b₁ 3→4 from complex-pair subs); reuse for Move 1's meta-arena + Move 2's coarse-graining.
- `library_chiral_screen.py` — the library is ruled out (LV is a marginal center; driven_ring explicit).
- `homochiral_triad.py` / `homochiral_cascade.py` — the #1 self-lit substrate + the tilt-brittle joint.
- `frustration_ascent.py` / `dynamical_tower.py` — the original b₁-growth (linear focus) + the inserted-SL tower.
- Research: `cascade research and prompt.md` (rounds 1+2 + synthesis), `cascade outside opinions.md` (the transduction-vs-generation + bootstrap-blocked correction).
- Frontier: `mpa_frontier.md` `frustration-ascent` entry carries the full lineage; prior-art `splay-state`, `goldstone-mode`, `benjamin-feir`, `esposito-coarse-graining`. Memory: `project_frustration_ascent_recursion.md`.
- **No engine edits this whole thread** — all frontier/prior-art/doc tracking. The engine-review flag list (three-way cycle/affinity/current vocabulary; high-drive ceiling = structural stability; the asterisked platforming-recursion) is still owed Ron's review.
