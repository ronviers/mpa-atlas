# Character′ — the morphospace lift of `character`

> **Status: DRAFT, staged in `docs/`. NOT canonical, NOT in `framework/`.**
> This is a single-move lift of [`framework/character.md`](../framework/character.md):
> every quantity re-read as *structure on the manifold of characters* rather than a
> property of one NESS. It is held out of `framework/` deliberately — the lift leans on
> imports whose preconditions are unverified and on one bespoke binding with no receipt.
> Promotion waits on the intake research this draft maps out.

## How to read this

The lift is **one operation applied wholesale**: *read each object in `character.md` as a
coordinate or structure on character-space, not as a property of a single steady state.*
It can be a single move precisely because `character.md` is already coordinatized by the
right objects — the affinity `a` is already a coordinate, the deformation algebra
`gl(3,ℝ)` is already a tangent space. Nothing is invented here; the existing document is
re-pointed at the manifold. The honest symbol is not a derivative but the lift to the
**tangent bundle**, `Tℭ`; "character′" is shorthand.

Marker key (this draft is also the research map):

- `[est: source]` — established import with a named receipt. May still carry a
  precondition to verify before it can be leaned on.
- `[bespoke]` — the framework's own binding, **no external receipt**. Needs a derivation
  or a kill before promotion.
- `▶ INTAKE` — a research target: what to bring in, and the precondition to check. The
  collected `▶ INTAKE` lines *are* the research map.
- `⚠ CAVEAT` — a known limit or idealization of the framing itself.

---

## Abstract′

`character` is the finite-drive structure of one NESS, organized by the affinity
`a = ln(G₀/L)`. **character′** is the geometry of the *space of all such structures*: a
manifold whose points are characters, whose tangent space is the deformation algebra,
whose continuous and discrete sectors are the population and circulation bits, and whose
boundary is isolation. A system's character is a point; load is motion; coupling is the
law of the *relative* coordinate between two points; identity is the subset of
coordinates the boundary conditions leave free, sustained as a loop rather than stored as
a state. The content is again forcing-plus-receipts: the lift imports the geometry of
`GL(n,ℝ)`, synchronization theory, non-Hermitian degeneracy, topological-defect
interaction, decoherence-free subsystems, and theoretical morphology — and owes a receipt
for each.

## Object′ — character-space

A coordinate system for *the set of driven-dissipative steady states*, not for one of
them. A character is a point `χ ∈ ℭ`; the document `character.md` describes the structure
*at* a point and *in its tangent space*. character′ describes `ℭ` as a whole: its
stratification, its tangent decomposition, its boundary, and the rules two points obey
when their separation is small. It introduces no dynamics; it re-reads the imported
results as manifold structure and tests the alignment by the same over-determination.

## The point and its tangent space  *(lift of: Control parameter + deformation algebra)*

At a point `χ`, the linear response decomposes onto `gl(3,ℝ)`, Cartan-split into scaling
`ℝI`, rotation/chirality `so(3)`, and shear/detuning `Sym₀`. Read as geometry: **this is
the tangent space `T_χ ℭ`.** The affinity `a` is the abelian/radial coordinate (distance
from the degenerate equilibrium corner); chirality is the compact/angular coordinate;
shear is the non-compact/hyperbolic direction carrying the exceptional points.

- `[est: Cartan/KAK decomposition]` — the `ℝI ⊕ so(3) ⊕ Sym₀` split and `dim = 9`.
- `[bespoke]` — identifying this algebra as *the* tangent space of character-space.
  It was only **instanced** on the RPS replicator (residual `~10⁻¹⁶`), i.e. for the
  3-state minimal triad.

⚠ CAVEAT — character-space is **stratified by `n`**: 3-state triads sit on `gl(3,ℝ)`,
larger substrates on `gl(n,ℝ)`. "Two systems close" means two points in a common stratum,
or one embedded in another's. A single global tangent space is not claimed.

✓ RESOLVED (outbound research, 2026-06-01) — **isostable / phase-amplitude reduction**
(Wilson, Moehlis, Ermentrout; isochrons ← Winfree). The precondition **fails**: isostable
reduction breaks down exactly at loss of normal hyperbolicity (slowest Floquet/Koopman
exponent → 0; Wilson 2022 *explicitly* excludes bifurcation points). But the receipt
**substitutes** — the near-threshold (`s`-regime) tangent space is realized by
**center-manifold + normal-form theory** `[est]` (and `[emerging]` adaptive phase-amplitude
reduction, Monga–Wilson–Moehlis 2019, which hands off to center-manifold coordinates at
threshold). Net: the receipt is **regime-stratified** — isostable in the `c`-regime,
center-manifold/normal-form in the `s`-regime — and the **handoff occurs exactly at the
marginal point** (loss of normal hyperbolicity), which `character.md` already names. The
receipt-switch point *is* the framework's marginal point — a consistency win, not a leak.

## The tangent split: metric and topological  *(lift of: Two degrees of freedom)*

The two bits become the two sectors of the tangent space, with categorically different
laws:

1. **Population bit → metric sector** (the `ℝI ⊕ so(3) ⊕ Sym₀` continuous directions).
   Erasable at the Landauer bound; two nearby population bits **average/interpolate**.
2. **Circulation bit → topological sector** (discrete winding of `𝒜`). Protected; changes
   only by rewiring; two of them **fuse**, never average.

Decoherence sits exactly across this split: it selects pointer states and erases the
rest, so it is **aligned with the population bit** and **orthogonal to the circulation
bit**. The protected sector is a decoherence-free subsystem — unreadable by the
environment without a rewiring.

- `[est: Zurek einselection / pointer states]` — decoherence selects the metric sector.
- `[est: Zanardi, Lidar, Knill–Laflamme — decoherence-free / noiseless subsystems]` — the
  named complement of decoherence.
- `[bespoke]` — identifying the circulation bit *with* a decoherence-free subsystem (the
  distance-3 surface code is the suggestive worked example: logical qubit in the
  protected part, syndrome in the decohering part).

✓ RESOLVED (outbound research, 2026-06-01) — the **DFS ≡ circulation-bit** identification
is **structural, not analogy** `[est]`. The classical analog is the **commutant of the
strong-symmetry algebra of the Markov/Liouvillian generator** (Buča–Prosen 2012;
Albert–Jiang 2014) together with **Schnakenberg gauge-irremovable cycle currents** — the
protected circulation bit *is* such a current. Caveat `[open]`: no single unified
classical-DFS theorem (matching Knill–Laflamme–Viola) exists — the analog lives "in
pieces," and that unification is a candidate *secondary* contribution, not claimed here.

## Motion on the manifold  *(lift of: Threshold regimes + Coarse-graining)*

Increasing load is a **monotone descent in `a`** — a path on `ℭ`. The threshold
trichotomy (`a ≫ 0` / `a ≈ 0⁺` / `a < 0`) is three regions of that path; the
near-threshold `s`-region is the generic attractor. Level-to-level coarse-graining (the
RG contraction with modulus `ε`) is **the same kind of motion, one level up** — a path on
the manifold of *coarse-grained* characters. The marginal point `ε → 1` is **loss of
normal hyperbolicity**: the locus where the slow manifold — and with it the separability
that lets us call the point a single character — ceases to persist.

- `[est: Haken; Sieberer–Buchhold–Diehl]` — the driven-open trichotomy.
- `[est: Wilson–Polchinski RG; Banach contraction; Krein–Rutman; Fenichel]` — the flow,
  its modulus, and the marginal point.

## Proximity — the relative-character vector  *(NEW; the heart of character′)*

"Two systems close" = a small **relative-character vector** `δχ = χ_B ⊖ χ_A` in a common
stratum. Its rules split by which sector `δχ` occupies.

### Family A — metric rules (continuous part of `δχ`)

One rule per Cartan direction, with **different signs set by the compact/non-compact
structure of the Killing form** — bounded directions attract, hyperbolic directions
coalesce:

- **Chirality / `so(3)` (compact):** proximity → **locking/entrainment**.
  `[est: Kuramoto, Adler]`; strength already in-engine as `K_AB ∝ (1+4Q²)^{-1/2}`.
- **Scaling / `a` (abelian):** proximity under a shared drive → **competition**
  (gain-clamping; winner pushes loser below threshold). `[est: laser mode competition,
  Haken/Siegman]`.
- **Shear / `Sym₀` (non-compact):** proximity → **exceptional-point coalescence**,
  `ω² = ω₀² − (δ/2)²`; eigenvectors merge, the two characters lose independence.
  `[est: Kato perturbation theory; non-Hermitian EP]`.

The unifying claim — *the sign of the proximity law is the sign of the Killing form in
that direction* — is `[est: Cartan/Killing form]` as mathematics but `[bespoke]` as a
*character* statement.

### Family B — topological rules (discrete winding of `δχ`)

- **Fusion, not averaging.** Circulation bits `±1` combine by a discrete rule: co-rotating
  reinforce (higher winding), counter-rotating **annihilate** to a bound dipole or to zero
  net `𝒜`. `[est: Kosterlitz–Thouless vortex–antivortex interaction]`.
  ⚠ CAVEAT — anyon fusion is the *quantum cousin* and is **analogy only**: anyons carry
  braid-group representations on a degenerate Hilbert space a classical current does not
  have. Import the fusion *shape* from vortices, not the machinery from anyons.
- **Threshold, not transfer.** No continuous exchange of circulation; below a coupling
  threshold the triads are topologically inert to each other; at threshold they **rewire
  discontinuously** (first-order in the topological sector while the metric sector stays
  smooth).
- **Union-graph frustration (the generative rule).** Re-run Harary balance on the *union*
  graph including the coupling edges: two balanced (non-circulating) systems can couple
  into a frustrated joint triad neither had — **proximity as a creation operator for
  protected current.** `[est: Harary/Cartwright structural balance]`, extended to the
  union.

▶ INTAKE — **active-nematic defect braiding** (Giomi, Bowick, Dogic): Family B with *real
data*, and a bridge to the Veenstra/Bartolo active-lattice circulation data already in
hand (mismatched to the single-unit perturbation protocol, but possibly a fit for a
*two-unit proximity* protocol).
▶ INTAKE — **signed-network / structural-balance dynamics** (Antal–Krapivsky–Redner) for
the union-graph rule.

### Family C — the cross-rule (re-routed by research, 2026-06-01)

In isolation the two bits are independent (aging never couples to circulation). Proximity
couples them: **the EP locus of Family A is where a real eigen-pair goes defective and can
split into a complex-conjugate pair.** EP *creation* by coupling and the *transfer* of EP
topology to a classical NESS Jacobian are both **`[est]`** (the 2×2 coupled-damped-modes
Jacobian is the minimal instance; Bergholtz–Budich–Kunst RMP 2021 for the topology, with
classical reality / Markov-positivity constraints).

**But the EP is *not* the source of protection** — the correction the research forced. A
generic coupling-created complex pair is **not** topologically protected (it deforms back
through `ω = 0`, reversing chirality, no singularity required); intrinsic protection of an
EP in a *finite-dimensional* classical Jacobian (no periodic parameter space) is
**`[open]`/`[contested]`** — the single point all three reviewers flagged as the field's
live disagreement. So:

- **EP = the spectral *onset signature*** of the circulating mode `[est]`.
- **Protection re-routes to Family B3** — the gauge-irremovable graph frustration minted by
  coupling, which **is** robustly protected and **is** minted (`[est]`, signed-graph
  theory). The complex pair is protected *because the frustrated triad forcing it is
  gauge-irremovable*, not because spectra are intrinsically topological. This is the
  framework's own iff-chain read in the right direction: `𝒜≠0 ⟺ complex pair ⟺ triad`,
  protection inherited from the triad.

`[bespoke — relocated]` — the residual MPA owns is no longer "an EP creates a protected
bit" but the **binding**: the graph-frustration object, the spectral complex pair, and the
thermodynamic `𝒜` are *one* minimal carrier read in three registers. The research confirms
each node is established and that **no unified theorem connects them** — so the edge is the
contribution. The central bet is now precisely located: *is the chirality of a NESS
circulation protected in a generic finite-dimensional dissipative system?* — open, with the
graph-frustration side as the derivation route.

## The conjugate cascade  *(lift of: Two fluctuation-dissipation readings)*

Every character cascade — protected structure built up the hierarchy — has a counterpart.
**Geometrically orthogonal** (the character cascade climbs in the protected subspace; its
counterpart runs in the decohering complement) but **causally conjugate, not
independent**: every protected bit built upward is paid for by a cascade of erasure
exported downward. The two are one entropy production read two ways —

```
∫(FDR departure) = ⟨σ⟩ = J · 𝒜
```

— lifted from a point to the tower (`W_{n+1} = W_0/[(1-u_n)(1-u_{n+1})]`). Orthogonal in
state space, **locked in the ledger**; the second law is the coupling between the two
cascades.

- `[est: Harada–Sasa identity]` — verified to machine precision on the rotational-OU
  testbed (in-framework).

▶ INTAKE — **stochastic thermodynamics of coupled NESS / continuous information flow**
(Horowitz–Esposito; Parrondo–Horowitz–Sagawa): how two characters split entropy production
and exchange information when coupled — the thermodynamic receipt the conjugate cascade
and the cross-rule both owe.

## Identity  *(NEW; lift of the protected-current necessity)*

Identity is not a property of one character read in isolation; it is a **relation between
a point and the manifold** — *which coordinates the boundary conditions left free, and the
trajectory taken through them.* Concretely: identity is the **circulation-bit / protected
sector**, the substructure the reservoir configuration permits but does not force.

Two consequences, both substrate-general:

1. **Sustained, not stored.** A protected current exists only while the system is driven;
   remove the drive and the protected sector dissolves. Identity is a *loop that is being
   run*, not a record that is being kept. ("Character is always on" and "identity depends
   on character" are then one statement — and the verb sense was latent in the word
   `character` from the start.)
2. **The irreducible residue.** The metric/population sector of any NESS is *forced* by
   its reservoir configuration — exactly as rare as the configuration, no more, and
   regenerable from it. The topological/circulation sector is **not** entailed by the
   configuration; it is the contingent, history-frozen residue of past rewirings.
   Reconstructing a system's driving reservoirs regenerates its *generic* character but
   never its *protected* substructure. Identity is precisely the part that the boundary
   conditions cannot supply.

`[bespoke]` — "identity ≡ the protected/topological coordinates, sustained as a loop." A
binding, not yet receipted; the DFS intake above is its most likely receipt.

## Isolation — the boundary of `ℭ`  *(lift of: Measurement discipline / open-interval)*

Isolation is the **unreachable boundary** of character-space on the coupling axis, as
equilibrium is on the drive axis. *Perfect* isolation is the degenerate corner
(`Boolean = Markov = equilibrium = detailed balance = X≡1 = 𝒜=0 = β=1`): a system with no
drive has no character. *Effective* isolation is real and **measured by `β`**: `β = 1`
(Markovian, memoryless bath) is the separable limit — effectively isolated; `β < 1`
(memory) is isolation failing — system and bath sharing history. Since `β = 1` is a
boundary, the open-interval discipline forbids attaining it at a finite operating point;
**no real system is even effectively perfectly isolated.** The degree of non-isolation is
the memory carried (`1 − β`, loosely; cf. `β_mem ≈ 1 − ε`). Existence is the open
interior; isolation is the edge.

- `[est: third law; QED spontaneous emission/Lamb shift; Gibbons–Hawking horizon
  temperature; Born–Markov separability ↔ Markovianity]` — perfect isolation forbidden;
  effective isolation = the separable/Markovian regime.

## Morphospace — the space itself  *(lift of: Object / the shadow space)*

`ℭ` is the **morphospace** of driven-dissipative structure: the space of all *possible*
characters, of which any realized substrate occupies a point or a path. The "shadow" of
any one science (the space of weathers that could be, behind the one realized) has no
unified name — it is the *ensemble* (stat mech), the *complementary channel* (quantum
info), the *basin's complement* (dynamics), the *adjacent possible* (Kauffman), the
*morphospace* (theoretical morphology). character′ is the bet that there is a single such
space for finite-drive structure, and that `ℭ` is it.

- `[est: Raup theoretical morphospace]` — the closest named precedent.

⚠ CAVEAT — morphospace works when the possibility space is **prestatable** (Raup could
parametrize every shell). For open-ended cascades (the alive loop), Kauffman's argument is
that the adjacent possible is **not** prestatable — the space is *generated as the system
moves*. So "`ℭ` as a fixed manifold" is an idealization; the honest shadow space may be
**growing, not given.** This is a genuine limit on the tangent-space framing, not a
footnote. `[bespoke / open]`

## Measurement discipline′ — what the falsifier becomes

The lift changes the falsifier. A steady-state **collapse** test (four quantities onto
`a`; three routes onto a common `β`) is either circular-by-construction (one injected
parameter recovered through known maps) or a re-derivation of imported theorems — trivial,
and not where character′ has content. The honest falsifier is the **generative-metaphor
meta-falsifier**:

- **Stall** — character′ stops ingesting (the gate ledger freezes, no new substrate lands,
  the proximity edges never go live on real data). A generative metaphor that stops
  generating is dead.
- **Float** — a node loses its receipt and is used anyway (an `unrecovered` marker that
  never recovers; the mpa-legal "sits inert" verdict). A metaphor with a bibliography but
  no live provenance.

The decisive test is **not** the union-graph frustration check — that re-derives
established signed-graph theory (union of balanced graphs can be unbalanced), the same
circularity as the collapse demos. It is the **open** question, run: couple a system whose
union graph is frustrated and test whether the resulting current's chirality is protected
against *all* continuous deformations (dies only on rewiring), not merely around a chosen
loop. Two clean, non-circular kills:

1. a circulation bit that **transfers continuously** between two coupled systems →
   topological protection (B2) false, the two-bit split collapses;
2. a coupling-created protected current whose chirality is **removable by smooth
   deformation while the frustrated triad persists** → protection is not inherited from the
   graph, the B3 re-route fails, and the binding has no teeth.

## Receipt ledger — status after outbound research (2026-06-01)

Imports (precondition verdicts):

1. **Isostable / phase-amplitude reduction** — **partial → substituted.** Fails into the
   `s`-regime; receipt regime-stratified (center-manifold/normal-form near threshold,
   handoff at the marginal point). Tangent-space framing survives.
2. **DFS / noiseless subsystems** — **imported, in pieces.** Strong-symmetry commutant +
   Schnakenberg cycle currents; circulation-bit ≡ DFS confirmed structural. No unified
   classical theorem (`[open]`).
3. **Non-Hermitian topology / EP braiding** — **split.** Creation + transfer to classical
   Jacobians imported (`[est]`); EP-as-protection-source **not** supported → Family C
   re-routed (above). Intrinsic finite-dim chirality protection `[open]`.
4. **Active-nematic defect braiding** — still owed (real-data bridge, P1).
5. **Coupled-NESS stochastic thermodynamics / information flow** — still owed (P1).
6. **Signed-network balance dynamics** — **imported** (`[est]`): union of balanced graphs
   can be unbalanced; minted frustration is gauge-irremovable and protected.

Bespoke bindings, post-research:

- `gl(n,ℝ)` as *the* tangent space — still owed a second instance beyond RPS.
- circulation bit ≡ decoherence-free subsystem — **receipted in pieces** (item 2).
- Family C — **relocated**: not "EP creates a protected bit" but the binding (graph ⟺
  spectral ⟺ thermodynamic, one carrier) + the open chirality-protection question.
- identity ≡ sustained protected-sector loop — still owed.

Open limit of the framing itself:

- Kauffman non-prestatability — `ℭ` may be growing, not a fixed manifold.

---

*Source:* [`framework/character.md`](../framework/character.md). This draft is the lift,
not a replacement; it promotes to `framework/` only when the ledger above is discharged.
