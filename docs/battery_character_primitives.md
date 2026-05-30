# battery:character-primitives — falsifier-of-record spec (draft)

**Status:** draft for review (2026-05-29). Not yet planted in `mpa_frontier.md`. This is the
runnable falsifier the multi-week promotion effort *derives against* — so the work has a fixed
target with explicit kill/vindicate, not a table to defend.

**Rung claim:** the character **deformation-generator basis** (the elementary topological
deformations of the asymmetric triad + each one's forced normal/coupling-pull response) is a
**non-instance, structural** claim. Its promotion gate is therefore a **forced-not-fitted
derivation** (GATES, `staked → promoted`, clause (a) second branch), which is achievable
synthetically — *provided* the structural claim is kept clean of the coverage claim (see SCOPE).

---

## Compact frontier entry (ready to plant in the BATTERY section)

> * `battery:character-primitives` **[battery]** — *verdict:* the elementary deformations of the
>   asymmetric triad form a **finite, closed generator basis**, and each generator forces a
>   **canonical** normal/coupling-pull response that lands on an established universal form (no fit).
>   The basis: {uniform damping; chirality magnitude+sign; normal-orientation/tilt; anisotropic
>   splitting/detuning; drive/noise; inter-block coupling+parity; rotating parametric squeeze}.
>   Runnable: `mpa-conform/scripts/{chiral_bonding, chiral_selffield, chiral_tilt, tilt_rescue,
>   establishment_compare, character_primitives, squeeze_dynamics}.py`. · **↑** **promotes** the
>   *character deformation-algebra* to engine (an `OPERATORS`-adjacent section) when ALL hold:
>   **(C)** completeness of the basis is *derived* (a closure result, not a catalogue); **(R)** each
>   non-model-specific response is *forced* to its canonical closed form (receipts in prior-art);
>   **(I5)** collapse + iff-chain + flow pass; **(G)** goalpost-optic (shrinks the falsifiable
>   surface); with the meta-scale protecting symmetry either **derived** or scoped **conditional**.
>   · **✗** the basis is not closed (a triad deformation that is not a composition of the
>   generators); OR a claimed generator's response is fitted / model-specific (e.g. the ~39° tilt
>   node — stays frontier); OR the protecting symmetry can only be hand-supplied (fitted) and admits
>   neither derivation nor honest conditioning; OR I5 fails (an inert constant in any response, or
>   the basis is asserted rather than entailed). · **→** engine `OPERATORS` (new: deformation
>   generators) + `TWO FACES` / `TWO BITS`; receipts §deformation generators; prior-art
>   `nonhermitian-ep`, `adler-locking`, `bifurcation-normal-forms`, `nonreciprocal-transition`,
>   `kuramoto`, `slaving`, `mz-projection`, `frank-autocatalysis`, `kondepudi`. Operationalizes the
>   structural side of `frustration-ascent`.

---

## OBJECT

The character-bearing operator's **deformation space** and its decomposition into elementary
generators, each carrying a forced response (how it moves the chimeric normal, what effective
coupling it induces, what bifurcation/threshold it forces). The triad `M = −γI + g·A_CYC` is the
minimal carrier (the frustrable sub-topology); the generators deform it.

## FORCED-NOT-FITTED TARGET (what the derivation must establish)

1. **(C) Completeness / closure — the load-bearing piece.** A *derivation* that the deformation
   space of the character-bearing operator decomposes into exactly the listed generators and is
   **closed** under them. Sketch of the required decomposition: the drift `M ∈ gl(3)` splits as
   symmetric ⊕ antisymmetric (= uniform-damping trace ⊕ traceless-symmetric splitting ⊕ the
   antisymmetric axial = chirality magnitude+sign+orientation); plus the noise/drive (diffusion
   tensor); plus the nonlinearity (gain/saturation); plus the time-periodic (Floquet/parametric)
   axis. The bar: **prove this set is exhaustive for the character-bearing operator** — a catalogue
   of "deformations we tried" does NOT clear it. A closure is a law; a list is frontier.
2. **(R) Each response forced.** Every generator's normal/coupling-pull response derived as its
   canonical closed form, with the prior-art receipt:
   | generator | forced response (closed form) | canonical home (prior-art) |
   |---|---|---|
   | uniform damping | Re-shift only; normal & chirality invariant | (trivial) |
   | chirality magnitude+sign | achiral point at g=0 (parity boundary); chimeric normal = axial vector ∥(1,1,1) | `signed-balance`, `frank-autocatalysis` |
   | normal-orientation / tilt | exceptional point at δ=2Γ; locking range θ_c∝κ | `nonhermitian-ep`, `adler-locking` |
   | anisotropic splitting/detuning | ω = √(Γ²−(δ/2)²); EP collision at δ=2Γ | `nonhermitian-ep` |
   | drive / noise | NESS current; topological sign drive-independent, drive-set sign gauge-removable | `ness-currents`, `cycle-affinity` |
   | inter-block coupling + parity | induced antisym M_eff ∝ sub-chirality (Schur); pull-rescue κ≳θ/const | `nonreciprocal-transition`, `slaving`, `mz-projection`, `adler-locking` |
   | rotating parametric squeeze | parametric tongue at Ω=2ω₀, a_c≈γ; phase-deformation = Adler √(Δ²−K²) circulation cliff + SNIC intermittency + Z2 phase basin | `adler-locking`, `bifurcation-normal-forms` (Floquet/Mathieu, circle map) |
   The establishment pass (`establishment_compare.py`) already verified the headline forms on
   synthetic data: EP square-root law R²=1.0000; Arnold-tongue θ_c∝κ; pitchfork K_c=c, β=½;
   non-reciprocity √3g/(γ²+3g²). Receipts: see prior-art keys above.
3. **(I5) self-application three-filter.** *Collapse* — the basis is over-determined (each response
   independently confirmed by its establishment landing; not a single-register identity). *Iff-chain*
   — the basis is the **entailed** generator decomposition (point C), not an asserted list. *Flow*
   — every response moves with the operating point; **no inert constant** anywhere (EP threshold,
   locking range, pitchfork point, parametric a_c all parametric — re-verify none is frozen).
4. **(G) goalpost-optic.** Promotion must *shrink* the falsifiable surface: the basis makes the
   sharper prediction that *any* character deformation is a composition of these generators with
   these responses — a deformation that fails to decompose, or whose response misses its canonical
   form, is then a kill of the engine claim.

## KILL CONDITIONS (any one ⇒ does not promote)

- **K1 — basis not closed:** a triad deformation that is not a composition of the listed generators
  (completeness fails). The basis stays a frontier catalogue.
- **K2 — a fitted response:** a claimed generator whose response is model-specific / does not land
  on a forced canonical form. (Known instance: the **~39° symmetric-cone chirality-reversal node** —
  matched neither the 60° Berry solid-angle nor the magic angle; it stays frontier and does NOT
  promote. Any other such cell stays frontier.)
- **K3 — symmetry only hand-suppliable:** the meta-scale symmetry protecting the collective
  degeneracy admits neither a forced derivation nor an honest conditional scoping — i.e. it can only
  be drawn in by hand. Hand-supplied = fitted = cannot cross. That piece stays parasitic/frontier.
- **K4 — I5 fail:** an inert constant in any response (flow fail), or the basis asserted rather than
  entailed (iff-chain fail).

## VINDICATE CONDITIONS (all ⇒ promote)

C (closure derived) ∧ R (each non-model-specific response forced, with receipts) ∧ I5 (collapse +
iff-chain + flow) ∧ G (goalpost shrinks) — with the protecting symmetry **derived** (the prize) OR
scoped as an explicit **conditional law** ("given a substrate-supplied protecting symmetry, the
generators force the collective degeneracy to lift into a protected meta-cycle"; honest,
parasitic-on-substrate, promotable as a conditional). Then the character **deformation-algebra**
promotes to the engine as an `OPERATORS`-adjacent section, with line-keyed receipts.

## RUNNABLE APPARATUS

`mpa-conform/scripts/` — `chiral_bonding.py` (Schur seeding + conditionality), `chiral_selffield.py`
(self-field SSB / Curie), `chiral_tilt.py` (tilt break + node), `tilt_rescue.py` (precise θ_c +
pull-rescue), `establishment_compare.py` (canonical-form verification), `character_primitives.py`
(the basis + responses; `weak`/`strong`), `squeeze_dynamics.py` (the parametric-squeeze = Adler
phase reading). Figures under `mpa-conform/output/calibration/`.

## SCOPE (the clean split that keeps it disciplined)

- **Structural law** — "the triad's deformation space decomposes into these generators, each forcing
  this response." Non-instance → promotable by this synthetic derivation. **This battery covers it.**
- **Coverage / life claim** — "real substrates' character is a composition of these generators"
  (the syn3 alive-loop). Instance → stays the real-substrate frontier (`syn3_alive_loop_handoff.md`).
  This battery does **not** touch it; conflating the two breaks the discipline.
