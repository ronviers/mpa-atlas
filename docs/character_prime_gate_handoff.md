# Character′ promotion — roadmap & handoff

> **Live baton.** Staged in `docs/`. The plan to discharge **Gate 1** (the
> `character_prime` receipt ledger) so the morphospace lift can promote into `framework/`,
> with a line of sight to **Gate 2** (the `character_double_prime` contribution layer).
> Self-contained: a cold reader needs only this file plus the three it points to.

## 0. Where this sits

Three staged artifacts, none canonical:

- [`character_prime.md`](character_prime.md) — the morphospace lift of `character.md`
  (point → manifold). Carries the **Gate 1** receipt ledger.
- [`lift_treatment.md`](lift_treatment.md) — the lift recorded as a repeatable move.
- [`character_double_prime.md`](character_double_prime.md) — the move applied a second time;
  emergence as closure of `ℭ` under coupling. Carries **Gate 2**, and is *doubly* gated
  (Gate 1 first).

This handoff removes Gate 1 and shows why one node of it removes the riskiest node of
Gate 2 at the same time.

## 1. The portable question (the thing that travels)

The work generated one question that carries the whole bet:

> **Does coupling *mint* protected structure, or merely *redistribute* it?**

It is worth stating **without any `character` vocabulary**, because (a) it travels, (b)
posing it in domain-native terms avoids leading the witness during intake, and (c) the
generative-metaphor posture says the vocabulary is optional for a physics audience. The
vocabulary-free form:

> *Is there protected structure that exists only in the composite — created by composition,
> not inherited from or recombined out of the parts — and if so, what is the minimal
> coupling that forces it?*

Domain restatements (these are the forms to hand to a research channel):

- **Non-Hermitian / spectral.** When two systems are coupled, can the coupling create a
  complex-conjugate eigen-pair or an exceptional point present in neither part **and**
  robust to continuous parameter change — or are the coupled system's robust oscillatory
  modes always traceable to the parts'?
- **Signed networks.** The union of two structurally-balanced signed graphs can be
  unbalanced. When does adding coupling edges manufacture a gauge-irremovable frustrated
  cycle neither component had? (Existence is likely near-theorem; the open part is
  *robustness/protection*.)
- **Coupled oscillators.** Coupling can create oscillation absent in the parts (Hopf in the
  composite). Is the created oscillation ever *topologically protected* — winding/chirality
  fixed against deformation — or always continuously deformable away?
- **Composition of codes (QEC).** Does composing two systems ever yield a protected /
  decoherence-free degree of freedom present in neither — genuinely new protected
  information — versus a logical mode that recombines the parts' protected subspaces?

That this question came out of the metaphor and reworded itself into four fields is itself
the first receipt for "generative metaphor with receipts." Phase R therefore does double
duty: it discharges the gate **and** tests whether the metaphor keeps generating questions
the imports must answer.

## 2. Standing order

**Research before tests.** Intake is now **complete** (Phase R, below) — the one remaining
empirical question (chirality protection) is itself the contribution-grade test, so Phase V
is now licensed. (User directive, this thread.)

## 3. Phase R — intake (removes most of Gate 1)

The `character_prime` ledger as research questions. Each resolves to one of:
**imported** (receipt found, precondition met) · **bespoke-confirmed** (precondition fails —
must derive or kill) · **partial**.

| # | bring in | precondition to verify | priority |
|---|---|---|---|
| 1 | **Isostable / phase-amplitude reduction** (Wilson, Moehlis, Ermentrout; isochrons ← Winfree) — receipt for the *whole* tangent-space framing | survives into the near-threshold `s`-regime, not just a stable limit cycle (`c`-regime)? | **P0** |
| 3 | **Non-Hermitian topology — EP as defect, eigenvalue braiding under EP encircling** (Bergholtz–Budich–Kunst; Wojcik et al.) — the double-duty node (see §7) | NESS-Jacobian EP ≡ spectral/Liouvillian EP? does EP-creation yield *protected* structure? | **P0** |
| 2 | **DFS / noiseless subsystems** (Zanardi, Lidar, Knill–Laflamme) — receipt for circulation-bit ≡ decoherence-free | same protection in a classical NESS Jacobian as in a Liouvillian? | **P0** |
| 6 | **Signed-network balance dynamics** (Antal–Krapivsky–Redner) — union-graph creation rule | is union-induced frustration *robust* (gauge-irremovable), not just transiently present? | P1 |
| 4 | **Active-nematic defect braiding** (Giomi, Bowick, Dogic) — Family B with real data; bridges the Veenstra/Bartolo lattice data | does a *two-unit proximity* protocol fit that data where the single-unit perturbation protocol did not? | P1 |
| 5 | **Coupled-NESS stochastic thermodynamics / information flow** (Horowitz–Esposito; Parrondo–Horowitz–Sagawa) — receipt for the conjugate cascade + cross-rule | their information-flow term ≡ our cross-sector coupling? | P1 |

**Phase R — DONE (2026-06-01, three-model outbound synthesis; reports in
`mint_vs_redistribute_research_prompt.md`, verdict in `mint_vs_redistribute_verdict.md`):**

| # | verdict |
|---|---|
| 1 isostable | **partial → substituted** — fails into the `s`-regime; center-manifold/normal-form is the near-threshold receipt; handoff at the marginal point (a consistency win) |
| 3 EP / braiding | **split** — creation + transfer to classical Jacobians imported; **EP ≠ protection source** → Family C re-routed; intrinsic finite-dim chirality protection `[open]` |
| 2 DFS | **imported, in pieces** — strong-symmetry commutant + Schnakenberg currents; no unified theorem (`[open]`) |
| 6 signed-balance | **imported** — union of balanced graphs can be unbalanced; minted frustration gauge-irremovable + protected |
| 4 defect-braiding | still owed (P1) |
| 5 coupled-NESS thermo | still owed (P1) |

Net: **Gate 1 largely clears.** The hinge (#3) did not import as written — protection
re-routed from the EP to signed-graph frustration (B3, imported) — and the residual narrows
to the *binding* plus one `[open]` question (finite-dim chirality protection).

## 4. Phase D — derive-or-kill the residue

For bindings Phase R leaves bespoke, either a **bespoke proof shard** (the framework's own
derivation; append to the receipts engine and add a `steeping` entry to `character_frontier.md`)
or a **kill**. Post-research, the residue is:

- the **binding** — graph-frustration ⟺ spectral complex-pair ⟺ thermodynamic `𝒜` as one
  minimal carrier ← the residual the research left undrawn (no unified theorem exists).
- the **protection** — is the minted current's chirality protected in a generic
  finite-dimensional dissipative system? ← the `[open]` question; derive from the
  graph-frustration (gauge-irremovable) side.
- `gl(n,ℝ)` as *the* tangent space ← still needs a **second instance** beyond RPS (a
  non-triad Jacobian decomposing onto `gl(n)` generators; cheap direct sim).
- identity ≡ sustained protected-sector loop ← rests on the binding + protection above.

(circulation bit ≡ decoherence-free is now receipted in pieces — out of the residue.)

## 5. Phase V — the non-circular tests (only after R + D)

Two, each `<1 hr` (time a probe first; cheap direct observables, no ensemble responses):

- **(a) s-regime tangent-space check** — confirm center-manifold/normal-form is the right
  near-threshold coordinate set and that it hands off from isostable exactly at the marginal
  point (the research's prediction, verified by sim).
- **(b) Chirality-protection test** *(decisive; shared with Gate 2)* — **not** the
  complex-pair count (that re-derives established signed-graph minting — circular). Couple a
  frustrated-union system and test whether the minted current's chirality survives *all*
  continuous deformations (dies only on rewiring), not just a chosen loop. The `[open]`
  field question, run. It can come back no — and that strips the binding's teeth.
  **— RUN 2026-06-01 (`mpa-conform/scripts/chiral_protection.py` + `chiral_transfer.py` +
  `chiral_transfer_ness.py`; figs in `output/calibration/`). VERDICT: qualified YES, the
  falsifier did NOT fire.** The chirality *sign* (= cycle-flux sign) survives 0/200 generic
  graph-fixed deformations at amplitude ≫ g, reversing only on rewiring (cycle-orientation
  flip). The EP / complex pair, by contrast, IS suppressible (killed in 53/200 by a reciprocal
  gradient, cycle intact) — **confirming the Family-C re-route directly: protection is in the
  gauge-irremovable triad/affinity, not the EP.** Ron's coupled-transfer probe sharpened it:
  the physical current *magnitude* bleeds (modestly through an equilibrium bridge, minted
  continuously through a non-reciprocal one) but the topological *bit* does not transfer
  (A's sign stays graph-locked). No conserved *integer* charge (holonomy ≤0.16). **⇒ protection
  is a discrete graph-flux invariant, not a Chern-like charge.** Two self-corrections caught en
  route (vacuous v1 deformations; an `antisym(Ω)` artifact that re-read the bare generator —
  fixed by the `C = ΩΣ` current). So `character_prime` promotes with the **cross-rule INTACT**.

## 6. Promotion criterion

When every ledger row is imported / derived / killed and **no node floats**, `character_prime`
promotes to `framework/` and earns a coined name (it is not "prime" forever). The Kauffman
non-prestatability caveat does **not** block promotion — it is a recorded scope boundary
(`ℭ` may be growing, not fixed), carried honestly, not a debt.

## 7. Vision — Gate 2 falls out of Gate 1's hinge

Row #3 was the pivot, and it resolved by **re-routing** rather than importing: the EP is the
spectral onset signature, the *protection* comes from signed-graph frustration (B3,
imported). That re-route is the best available outcome for the line of sight — it collapses
both gates onto **one** remaining question: *is the minted chirality protected in a generic
finite-dimensional dissipative system?* — simultaneously prime's last open binding and
character′′'s whole contribution.

1. The minting (existence of new protected structure under coupling) is **settled imported**
   (signed graphs). character′′ is therefore **not empty** — there is a rock-solid case.
2. The one open question is the **protection**. Phase V-(b), the chirality-protection test,
   is the **first real Gate-2 result**, and it is also what lets prime promote with the
   cross-rule intact rather than stripped.
3. Gate 2's remaining bindings (the binding; emergent identity; the alive loop) sequence
   after — the **alive loop stays parked** (program decision), recorded as the layer's
   target, not active work.

The metaphor did the generative half: it produced a question that travels into four fields.
The fields answered — and where they left a gap (the unified binding, the finite-dim
protection) is exactly where MPA's residual sits. The generative-metaphor thesis, confirmed
in one cycle.

## 8. What would falsify the whole direction (kept sharp)

- **The live one — RESOLVED 2026-06-01, did NOT fire.** Phase V-(b) found the minted
  chirality's *sign* is **not** removable by smooth deformation (0/200, reverses only on
  rewiring) → protection **is** graph-inherited (the discrete flux invariant), the binding
  keeps its teeth, Family C's re-route holds, and `character_prime` promotes with the cross-rule
  **intact**. *Honest residual:* protection is the discrete *sign*, not the current's
  localization (which bleeds) and not a conserved *integer* charge (holonomy sub-integer) — so
  the claim is "discrete graph-flux protection," not "topological (Chern-like) protection." The
  weaker-but-true statement, carried.
- Row #1 already resolved: isostable doesn't reach the `s`-regime, but center-manifold does,
  so the framing survives with a regime-stratified receipt. *(closed)*
- If the binding cannot be derived **and** no substrate exhibits it → character′′ is
  laundered metaphor and does not promote, though `character_prime` still can.

Name these so the handoff cannot drift into assuming success.

---

**Done-when:** Gate 1 ledger discharged, `character_prime` promoted to `framework/`.
**Next action (Phase R DONE, Phase V-(b) DONE 2026-06-01):** the decisive protection test is
run (qualified pass, cross-rule intact). The remaining gate residue is **the binding** —
derive graph ⟺ spectral ⟺ `𝒜` as one carrier from the gauge-irremovable side (no unified
theorem exists; this is the contribution), plus the P1 intake rows (#4 defect-braiding data,
#5 coupled-NESS thermo, optional support). Promotion to `framework/` is then a separate
explicit decision (the binding is the last floating node per I2).
**Reserved promotion names (chosen 2026-06-01, pending the actual file move):**
`character_prime` → **`character_manifold.md`** (substrate-neutral; names the tangent-space/
gl(n)/metric structure; alt considered: `character_morphospace` — more evocative but carries a
morphology flavor the substrate-agnostic discipline resists). `character_double_prime` →
**`character_composite.md`** (names the object without overclaiming; alts: `character_closure`
collides with the existing `character_closure_derivation.md`; `character_emergence`
pre-asserts the doubly-gated conclusion).
**Engine refinement — APPLIED 2026-06-01 (Ron approved):** the V-(b) result refined receipts
**§Topological-drain — k_frust invariant** — superseded "the invariant **is** the complex
spectrum" → **the invariant is the broken-detailed-balance affinity `𝒜` (non-gradient/
antisymmetric drift); the complex pair is its underdamped *signature*, suppressible to a real
overdamped circulation (`𝒜≠0`, `J≠0`) without restoring detailed balance.** The third sharp
falsifier was corrected ("J resolves to real spectrum" → "J resolves to a gradient/`𝒜→0`
structure"). The **same correction's minimal scoping clause** was applied to **§Central
commitment**'s spectral parenthetical (`𝒜≠0` iff non-gradient drift; the complex-pair iff holds
for the canonical isotropic-damping triad only) — its load-bearing triad-necessity claim is
untouched. No other promoted line affected.
**Repo note (2026-06-01):** the framework set is now `character_*.md` and its prose is
rebranded `MPA → Character`; this doc (in `docs/`) still says "MPA" pending a
publication-aware pass.
**Cross-refs:** [`character_prime.md`](character_prime.md) ·
[`lift_treatment.md`](lift_treatment.md) ·
[`character_double_prime.md`](character_double_prime.md) ·
`framework/character_frontier.md` (where surviving bespoke bindings get `steeping` entries once
instanced) · `framework/character_receipts_engine.md` (where Phase-D derivations land).
