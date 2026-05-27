# Restructure spec — "Eleven cross-register identities"

**Purpose.** Hand-off to the rewrite session. Replaces the flat list of eleven items under §Framework primitives → *Eleven cross-register identities* with a claim-typed structure. No content is dropped; items are re-sorted, two are merged, two are moved out, and the relationship to the five leading-order posits is made explicit.

**Net count:** 11 flat items → 6 identities + 2 relations + 2 decompositions (one merge: #1+#9).

---

## 1. Diagnosis

The current heading conflates at least five distinct claim-types:

1. **Parameter identity** — one scalar equals another under stated conditions (X = Y = Z, same number).
2. **Structural identity** — one mechanism/object, multiple reading-protocols or morphologies.
3. **Universality coincidence** — one universality class instantiated at two framework limits.
4. **Forcing result** — A forces B forces C (causal chain, *not* an identity).
5. **Decomposition** — these N things are irreducibly independent (the *opposite* of an identity).

Two items (#6, #10) are type 5 and do not belong under "identities." One item (#3) is type 4 and is an identity only by courtesy. Two items (#1, #9) are the broad-propagation and tight-core layers of the same parameter and should merge.

Separately: items #1, #2, #3, #4 are entangled with the five leading-order posits (they restate or follow from them). The section currently presents posits and identities as parallel lists; they should be threaded.

---

## 2. Target structure

Rename the section to **"Cross-register structure"** with three subsections:

### A. Cross-register identities
Things that genuinely assert "this is that." Three subtypes.

**A1 — Parameter identities** (one scalar, multiple measurement protocols)
- **β_mem parameter identity** *(merge of old #1 + #9)*. Core three-way identity: `α_s = β_mem = anomalous heavy-traffic exponent` (gFDR / fractional calculus / operations research). Supporting propagation map: the seven registers the parameter surfaces in (memory-tail, τ_R Green–Kubo divergence, swim-pressure fingerprint, Kelly product-form breakdown, Wall-coupling posit, variable-ratio extinction tail, traffic→frozen-topological transition via ℓ_c). Controlling posit: `β_mem ≈ 1−ε`. Substrate-class condition for the core identity: slow-resource memory kernel and load-arrival process share a single anomalous-diffusion exponent.
- **Optimal-encoding identity** *(old #2)*. `χ = Δ_n = ⟨σ⟩_excess/γ_s` across cryptic order, encoding overhead, dissipation excess. This *is* posit `χ = Δ_n`; also rides posit `u_n = ε_n`. Holds only at the optimal limit; sub-optimal substrates split the four-aspect Wall.

**A2 — Structural identities** (one object, multiple reading-protocols)
- **Mentor-row dual face** *(old #5)*. One non-reciprocal coupling structure → temporal limit cycle (ω_pq) or spatial Turing pattern (k_c); substrate spatial structure selects.
- **k_frust topological identity** *(old #8)*. One topological fact (irreducible NESS, forced circulating current) read three ways: dynamical (complex relaxation spectrum), informational-geometric (homotopy obstruction), thermodynamic (Schnakenberg affinity forced nonzero). Identity at the underlying-topology level; signatures differ by register.
- **Plant-controller identity** *(old #11)*. One closed loop read three ways: active probe (§Stability), SOC self-tuning (§Pattern formation), Haken slaving (§Pattern formation). Unifying register: the plant–controller decomposition.

**A3 — Universality coincidence**
- **Galton–Watson dual-register** *(old #4)*. One mean-field class (τ = 3/2) at two limits: horizontal `μ = e^chit → 1` at chit = 0 (posit `μ = e^chit`); vertical tower branching → 1 at ε = 1. Substrate-graph dimensionality fixes the empirical exponent.

### B. Cross-register relations
Not identities — relations and forcing results between distinct objects.
- **Wall-forces-NRT** *(old #3)*. Forcing chain: Cobham wait → ∞ at u_n→1⁻ → generic Hopf per ascent → N≥3 ascents complete the 3-torus for NRT chaos. Consequence of posit `u_n = ε_n`. Substrate-conditional on r-collapse ordering and the Cobham–Haken bridge conditions. **[See §6 — judgment call on placement.]**
- **r-coupling, heat-tax channels 2 & 3** *(old #7)*. Channels share r as driver in opposing directions (channel 2 ∝ 1+Cr²; channel 3 = r-drop sync degradation); active-coupling sign C sets the balance.

### C. Decomposition theorems
Assertions of irreducible independence — moved out of "identities" entirely.
- **Three distinct spatial mechanisms** *(old #6)*. Turing reaction–diffusion / Kelly queueing-congestion / frozen-topological — explicitly not reducible to each other; substrate may carry one, two, or all three at different scales.
- **Four-channel pattern-selection architecture** *(old #10)*. Frustration / spectral-sync (SBN) / non-reciprocity / active-matter-overlay — four independent tests; the operating system for N≥3 emergence.

---

## 3. Disposition table (all eleven)

| Old # | Title | New home | Action |
|---|---|---|---|
| 1 | β_mem seven-register chain | A1 β_mem identity | **Merge** with #9; demote 7-register list to propagation map |
| 2 | Optimal-encoding triality | A1 optimal-encoding identity | Keep; mark as posit χ=Δ_n |
| 3 | Wall-forces-NRT chain | B relations | **Relabel** identity → forcing result |
| 4 | Galton–Watson at two registers | A3 universality coincidence | Keep |
| 5 | Mentor row's dual face | A2 structural identity | Keep |
| 6 | Three distinct spatial mechanisms | C decompositions | **Move out** of identities |
| 7 | r-coupling heat-tax 2 & 3 | B relations | **Relabel** identity → coupling relation |
| 8 | k_frust topological triality | A2 structural identity | Keep |
| 9 | s-regime exponent triality | A1 β_mem identity | **Merge** into #1 as the tight three-way core |
| 10 | Four-channel pattern selection | C decompositions | **Move out** of identities |
| 11 | Closed-loop plant-controller | A2 structural identity | Keep |

---

## 4. Posit ↔ identity thread

Make this explicit in the rewrite instead of running two parallel lists.

| Posit | Identity that carries it | Relationship |
|---|---|---|
| `β_mem ≈ 1−ε` | A1 β_mem identity | controlling posit of the chain |
| `χ = Δ_n` | A1 optimal-encoding identity | the identity *is* the posit |
| `u_n = ε_n` | A1 optimal-encoding + B Wall-forces-NRT | posit + its forced consequence |
| `μ = e^chit` | A3 Galton–Watson (horizontal) | posit instantiated at chit=0 |
| `w_i = γ_ref/γ_s,i` | (no clean identity) | loosely touches A2 coupling structures; **flag** — leave under posits only |

Recommendation: each identity that *is* or *follows from* a posit should name the posit inline; the posit table stops being a free-standing list and becomes the index into the identities.

---

## 5. Recurring form to note (optional editorial)

Four items share a "one thing, three readings" template — worth a one-line callout so the reader sees the rhyme:
- **Parameter trialities:** optimal-encoding (A1), β_mem core (A1).
- **Structural trialities:** k_frust (A2), plant-controller (A2).

Same 3-fan shape; parameter vs structural is the axis that separates them. Do *not* promote this to its own identity — it's a presentational observation, not a claim.

---

## 6. Open judgment calls for the rewrite session

1. **#3 placement (the live one).** It's titled a "chain" and is causal, so it is a forcing result, not an identity — placed in B above. But it is genuinely cross-register and load-bearing. Options: (a) B relations, as specced [recommended]; (b) keep under identities with an explicit "forcing, not identity" tag; (c) fold into §Load-handling / §Pattern formation as a theorem and cross-link. Pick one and be consistent with #7.

2. **Whether B survives as its own subsection** or #3 and #7 get absorbed into their home sections (§Load-handling, §Thermo-info heat-tax) with only a cross-link left behind. Keeping B preserves the "registers talk to each other" framing; absorbing it shortens the section. Lean: keep B if the cross-register framing is doing work elsewhere; absorb if not.

3. **`w_i` posit has no identity partner.** Confirm it should stay posit-only, or whether the mentor-row / auto-tuning coupling (A2) is close enough to thread. Lean: leave posit-only; don't manufacture an identity.

4. **A3 cardinality.** Galton–Watson is the sole universality coincidence. If the rewrite surfaces no second one, consider folding A3 into A2 with a "universality" tag rather than keeping a one-member subtype. Lean: keep separate only if a second coincidence is expected; otherwise fold.

---

## 7. One-line summary for the commit message

> Re-sorted eleven flat "identities" into 6 identities (parameter / structural / universality) + 2 relations + 2 decompositions; merged β_mem propagation (#1) with its three-way core (#9); moved #6/#10 out as decomposition theorems; threaded the five posits into the identities that carry them.
