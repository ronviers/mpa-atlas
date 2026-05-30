# Candidate engine updates — character-primitives + homochirality crossings (DRAFT 2026-05-30)

**LANDED 2026-05-30.** Ron approved the proposal + leanings; the chart and both crossings were applied
to `framework/` (engine §DEFORMATION GENERATORS / the character deformation chart; receipts
§deformation-generators + §Homochirality `proven`; frontier staked entries removed; §commit-line
crossing (2)). This doc is kept as the naming-rationale record.

**Purpose.** Concrete candidate *engine* text for the two crossings, written so we could nail down
**how to categorize/name the deformation primitives**. Both tests passed clean:

- **character-primitives** — `mpa-conform/scripts/rps_character.py` **5/5**: RPS's emergent Jacobian
  *produces* $A_{\text{CYC}}$ (Antisym $=x^*(\alpha-\beta)/2\,A_{\text{CYC}}$, residual 0), forced EP
  normal form $R^2{=}1.0000$, C3-meta-arena lift (b1 3→4, 0% generic closure, $\kappa^2$ vs $\kappa$).
  Crossing = `staked`→`promoted` (the coverage instance). Scope: one real emergent instance
  (ecological 3-cycle; linear-Jacobian reading at coexistence).
- **homochirality** — `mpa-conform/scripts/homochiral_triad.py` **4/4**: emergent mirror-chiral-3-cycle
  + Frank cross-inhibition; spontaneous parity break (parity-exact 50/50); protected 3-cycle NESS on the
  winner; drive→racemic / sign-held; beats all three nulls (incl. the 2-component-bistable trap).
  Crossing = `staked`→`promoted` (named real-substrate stake; also instances `frustration-ascent`'s
  self-lighting leg). Scope: a model Frank/Kondepudi-class network — not the literal ancient biochemistry.

---

## CANDIDATE A — character-primitives (the naming centerpiece)

### A.1 The primitive chart — proposed engine prose (replaces/augments §DEFORMATION GENERATORS)

> **The character primitives — the deformation chart.** A character-bearing drift admits a finite,
> *closed* set of deformations; tabulating each generator's forced response is a universal **coordinate
> chart for substrate character** (the map, not the substrates). Two tiers.
>
> **Linear core** — the deformation space of $M=-\gamma I+g\,A_{\text{CYC}}$ is $\mathfrak{gl}(3,\mathbb{R})$,
> **Cartan-decomposed** (exhaustive $1{+}3{+}5{=}9$, closed under the Lie bracket):
>
> | primitive | block | dim | deforms | forced response (canonical form) |
> |---|---|---|---|---|
> | **Damping** | $\mathbb{R}I$ (center) | 1 | uniform relaxation rate | trivial $\mathrm{Re}$-shift |
> | **Chirality** | $\mathfrak{so}(3)$ | 3 | rotation: magnitude · sign · orientation (axis) | sign-flip at the achiral point (pitchfork center); → EP under splitting |
> | **Splitting** | $\mathrm{Sym}_0$ | 5 | anisotropic detuning | non-Hermitian **EP**: $\omega^2=\omega_0^2-(\delta/2)^2$, EP at $\delta=2\omega_0$ |
>
> **Closed extensions** — each closes on a named structure beyond $\mathfrak{gl}(3)$:
>
> | primitive | structure | forced response |
> |---|---|---|
> | **Noise** | diffusion tensor $\in\mathrm{Sym}^+$ (continuous Lyapunov) | stationary covariance / NESS current |
> | **Nonlinearity** | gain/saturation normal forms | pitchfork / Hopf |
> | **Drive-periodicity** | Floquet / monodromy | parametric resonance → Adler circle map |
> | **Composition** | Schur on coupled triads | RG type-identity (again $\mathfrak{gl}(3)$ drift $+\mathrm{Sym}^+$ noise) |
>
> **Not primitives** (model-specific — stay frontier, K2; do NOT promote): the $\sim39°$ symmetric-cone
> chirality-reversal node; the non-uniform-squeeze secondary tongues.
>
> **Real instance (RPS).** On rock-paper-scissors (cyclic May-Leonard, real emergent C3-symmetric), the
> Jacobian at coexistence *composes* from these generators with the forced responses: its chirality
> channel **is** the emergent $A_{\text{CYC}}$ (Antisym $=x^*(\alpha-\beta)/2\,A_{\text{CYC}}$, residual
> 0 — forced onto the $(1,1,1)$ $\mathfrak{so}(3)$ axis, *not* hand-drawn); the EP normal form holds on
> the emergent plane ($R^2{=}1.0000$); and the conditional lift closes on the C3-coupled meta-arena
> (b1 3→4; $\omega_{\text{meta}}\propto\kappa^2$ so(3)-seed vs real-split $\propto\kappa$ Sym$_0$;
> generic C3-broken coupling kills it in 0%). `mpa-conform/scripts/rps_character.py`.

### A.2 Naming / categorization decisions to nail down

1. **Object name** (what we call the whole chart):
   - **(rec) "the character deformation chart"** — matches the "coordinate chart for substrate character" framing.
   - alts: "the deformation-generator basis" (current, mathematical); "character primitives" (current frontier key, kept as the `key`); a coined proper name.
2. **Structure**: **(rec) two tiers** (linear core $\mathfrak{gl}(3)$ / closed extensions). Alts: a flat
   7-item list; or grouped by *response class* (trivial / pitchfork / EP / Adler-tongue / Floquet).
3. **Per-primitive names** (the 7): **(rec) descriptive** — damping · chirality · splitting · noise ·
   nonlinearity · drive-periodicity · composition. Coin candidates if wanted: chirality → **"chimeric
   generator"** (ties to the chimeric sign/triad); splitting → "detuning" or "anisotropy";
   drive-periodicity → "parametric".
4. **K2 cells**: keep the $\sim39°$ node + squeeze tongues **out** of the primitive set (stated
   explicitly so future tests don't promote them). **(rec) yes, keep them out.**

### A.3 Staked-note + instance edits (the rung move)

- §DEFORMATION GENERATORS closing line — currently *"Staked (bridge rung, un-instanced on real
  substrates) … the coverage claim stays the parked instance frontier."* → **"Coverage instanced
  2026-05-30 on RPS (`rps_character.py`): real character composes from these generators with the forced
  responses; promoted. Receipts §deformation-generators."**
- receipts §deformation-generators: `staked` → `proven`, append the RPS evidence (A.1 last paragraph).
- new receipts `§commit-line crossing (2)`: what crossed, evidence, scope, absorbed docs.
- frontier: remove `staked:character-primitives`; update the `frustration-ascent` structural-side note
  (structural side now promoted on RPS; self-lighting leg instanced by homochirality below).

---

## CANDIDATE B — homochirality (small engine footprint; mostly receipts/frontier)

Homochirality is an **instance of the topological bit**, not a new engine object — so the engine edit is
one line; the rung move lives in receipts/frontier.

- **engine** §TWO BITS (or §CENTRAL COMMITMENT) — add an instance clause: *"Which-handedness instanced
  on a real emergent chiral-autocatalysis substrate (`homochiral_triad.py`): a Frank SSB freezes the
  protected sign of a 3-cycle NESS; drive sets magnitude (→ racemic), the sign is held and flips only by
  **substrate-specific rewiring** — here the racemic-saddle crossing, consistent with the corrected
  §Two bits (no universal $\ge1$ ch)."*
- **receipts** §Homochirality: `staked` → `proven`, append the homochiral-triad evidence (SSB +
  protected 3-cycle NESS + drive-sweep + the three nulls + parity-exact 50/50).
- **frontier**: remove `staked:homochirality`.
- **note**: this also discharges `frustration-ascent`'s self-lighting leg (the spontaneous SSB RPS
  lacked) — update that frontier entry's verdict accordingly (coverage/instance side advancing).

---

## DECISIONS TO NAIL DOWN (the short list)

1. **Object name** for the chart (A.2.1) — *character deformation chart* / *deformation-generator basis* / coined?
2. **Structure** — two tiers vs flat vs by-response (A.2.2).
3. **Per-primitive names** — descriptive vs any coined (e.g. *chimeric generator* for chirality) (A.2.3).
4. **K2 cells stay out** — confirm (A.2.4).
5. **Homochirality flip framing** — confirm "substrate-specific racemic-saddle crossing, not $\ge1$ ch"
   (the corrected-§Two-bits framing) (Candidate B).

Once these are set, the engine/receipts/frontier edits are mechanical and I'll land them as one
consistent crossing (I1-checked), same pattern as the two-bits correction.
