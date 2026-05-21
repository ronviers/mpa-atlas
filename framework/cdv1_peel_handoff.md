# Handoff — peel cdv1_compressed to claim-density

**Disposable.** Delete this file when the rewrite lands. It is the baton for
one focused session.

## The job, in one line

`cdv1_compressed.md` is 460 lines to `v9_compressed.md`'s 174 (~2.6×). The gap
is not richer claims — it is **re-hosted borrowed apparatus** from the ten
cross-framework adoptions that cascaded 2026-05-20 (`translating FDR.md`) and
all landed inline here. Peel each adoption down to *MPA's own* content; relocate
the borrowed machinery to where it already belongs. Nothing is deleted —
everything moves to a home that already exists.

## Why this is overdue (the diagnosis)

v9 states structure it *owns* and stops. cdv1 absorbed every adoption as full
prose + the source field's equations. The adoption-heavy sections —

| cdv1 section | adopted from | receipts home (already exists) |
|---|---|---|
| Stability and attractor structure | class-B laser RO, attractor classification | §13 |
| Phase-locking and collective coherence | Kuramoto synchronization | §15 |
| Pattern formation and self-organisation | SOC + Turing + dissipative structures | §9, §18, §19 |
| Active modulation and internal models | control theory, Francis–Wonham, Rescorla–Wagner, Crutchfield ε-machines | §17, §20 |
| Collective hydrodynamics | active matter: Toner–Tu, MIPS, Green–Kubo | §21 |
| Load-handling | queueing: Kingman, Jackson, Cobham, Kelly, Erlang-B | §22, §5 |

— plus the adopted halves of *Thermo-info accounting* — are ~150–170 lines,
almost the entire gap. **The receipts already cite and compose this apparatus.**
The SoT is duplicating derivations that have a home.

## The knife (function test — apply per passage, not per percentage)

For each line, ask: *is this MPA's own predicted measurement on a named
substrate, or is it the source field's apparatus?* Five buckets:

1. **Borrowed apparatus** (the source field's equations, derivations, worked
   intermediate steps — Cobham's wait formula, Toner–Tu equations, Kuramoto
   phase reduction) → **relocate to the matching receipts §** (composition
   entry). If the SoT carried an explicit formula the receipts only *cited*,
   move the formula into the receipts entry so nothing is lost.
2. **The mapping-claim** ("holdings are queues: chit = −ln ρ; c/s/r ↔
   stable/heavy-traffic/unstable") → **stays, as one line.** This is MPA's
   cross-substrate universality claim — the POSITION.md hard core. Do not strip
   it.
3. **MPA observable + named falsifier** → **stays.** Each adoption already has
   a falsifier (Receipts §, mirrored in §Open items). Keep the load-bearing
   observable and the falsifier pointer.
4. **Genuine MPA primitive** (the five posits P1–P5; the chit unit; the kernel)
   → **stays.** P4 (ε↔u) lives inside Load-handling but is framework content,
   not borrowed.
5. **Framing / expository prose** ("the framework's first explicit
   ⟨amplitude⟩×⟨rate⟩×⟨timescale⟩ relation") → **drop** (it is narrative; if
   it earns a place it is in `cdv1_unabridged.md`, which is allowed to lag).

Residue per section: roughly 3–5 lines (mapping + observable + falsifier +
any primitive) replacing 20–38.

## Worked example — Load-handling (the template)

**Before:** `cdv1_compressed.md` §Load-handling, ~34 lines, four displayed
borrowed equations (Kingman, Cobham, Kelly ℓ_c, Little).

**After (paste-ready):**

```markdown
## Load-handling (queueing register)

**Mapping.** Holdings are queues: $\text{chit} = -\ln\rho$ (utilisation
$\rho=\lambda/\mu$, service $\mu\sim G_0$); regimes c/s/r ↔ stable /
heavy-traffic / unstable. Borrowed apparatus and its compositions — Kingman
heavy-traffic, Little's law, Jackson/Burke product-form, Cobham priority-wait,
Kelly spatial, Erlang-B capacity — in Receipts §22 (+ §5, the Erlang-B closure
of the §Capacity ceiling).

**Heavy-traffic = $s$-aging** (load-bearing). Kingman's $\langle Q\rangle\sim
(1-\rho)^{-1}$ divergence is the §gFDR $s$-aging signature in the queueing
register: the FDR aging exponent $\alpha_s$ and the queueing-tail exponent are
one critical phenomenon. Coincide for Markovian substrates, diverge for
non-Markovian (divergence pattern = substrate-class diagnostic). **Falsifier
(Receipts §22):** substrate classes where the heavy-traffic exponent and
$\alpha_s$ are measured to differ. (Reframed mm1 falsifier — §Universal
two-mode kernel.)

**Wall coincidence.** Cobham priority-wait and Kelly spatial interaction-length
both diverge at utilisation $u\to1^-$, coincident with the §Heat-tax
thermodynamic singularity at $\epsilon\to1^-$; the four-aspect split is the P4
identity below. Frozen-topological transition detail in Receipts §22.

**ε↔u optimal-encoding identity** (posit P4 — §Five posits). $u_n=\epsilon_n$
at the rate-distortion bound; sub-optimal substrates carry overhead
$\Delta_n=u_n-\epsilon_n\ge0$. Thermodynamic and SOC aspects reach criticality
first (via $u\to1$); the informational aspect ($\epsilon\to1$) only for
optimal-encoding substrates — **sub-optimal substrates die thermodynamically
before they die informationally.**
```

**Receipts side (so nothing is lost):** append to `cdv1_receipts.md` §22 the
explicit formulas the SoT used to carry but receipts only cited — Kingman
$(1-\rho)^{-1}$, Little $\langle Q\rangle=\lambda\langle W\rangle$, Cobham
$W_{n+1}=W_0/[(1-u_n)(1-u_{n+1})]$, the Kelly spatial $\ell_c(\beta_{\text{mem}})$
form, the three Cobham–Haken bridge conditions with their per-condition
substrate falsifiers, and the traffic-driven → frozen-topological transition.
§22 already cites all the sources; this just lands the equations under the
citation. Keep the concept-name key (`§22 — Load-handling … (queueing theory)`)
unchanged — it is the stable anchor.

Net: ~34 lines → ~14, four borrowed equations → zero, every claim keeps its
falsifier, and the apparatus is fully preserved one file over.

## Per-section plan (carry the template)

Each row: what's borrowed (→ its receipts §), what stays (the load-bearing MPA
claim), the falsifier that already exists. The §Open-items live-falsifier list
already names most of these — keep it in sync.

- **Stability and attractor structure** → keep: the mpa-legal RO form
  $\gamma_{RO}=(\gamma_s/2)e^{\text{chit}}$ and non-monotonic $Q$ (today's
  landed fix), $Q$-as-S/N. Relocate: class-B laser RO derivation → §13.
- **Phase-locking** → keep: sign convention ($\gamma_{AB}$ sign → in/anti-phase
  lock), the $Q$-crossover *result*. Relocate: Kuramoto phase reduction +
  $K_{AB}$ closed form → §15. Falsifier: chimera-state SBN (§15).
- **Thermo-info accounting** → mostly stays (this is MPA's thermo↔info
  correspondence): bit/chit ledger + its falsifier (§17/§20), the χ=Δ_n=⟨σ⟩/γ_s
  optimal-encoding identity (P5). Relocate: re-derivations of TUR / channel
  capacity / rate-distortion → cite, don't re-host. **Most core of the six —
  trim lightest.**
- **Pattern formation** → keep: posits P1 (β_mem≈1−ε) and P2 (μ=e^chit), the
  Turing three-condition falsifier. Relocate: SOC/avalanche + Turing +
  dissipative-structure machinery → §9, §18, §19.
- **Active modulation** → keep: posit P3 (auto-tuning $w_i$), P5 (cryptic order
  χ=Δ_n), the four-axis coherence observable, internal-model-richness
  prediction. Relocate: control-theory / Francis–Wonham / Rescorla–Wagner /
  ε-machine machinery → §17, §20. Falsifiers: §20, §14.
- **Collective hydrodynamics** → keep: MIPS falsifier (high-Péclet clustering
  at $\gamma_{AB}\ge0$), active-stress fingerprint, TUR-tightness. Relocate:
  Toner–Tu / Green–Kubo / giant-number-fluctuation machinery → §21. **Most
  speculative of the six** — the SoT already flags it a "posited extension /
  substrate-class residual" for non-active-matter substrates. Candidate for the
  hardest trim; see decision (1) below.
- **Load-handling** → done above (template).

## Optional structural improvement (evaluate, don't assume)

Mirror v9's **Composite catalogue** with a single **Adoption catalogue** table:
one row per adopted register — `register | MPA mapping (one phrase) | load-bearing
observable | falsifier | receipts §`. That collapses six prose sections into a
table plus the few genuinely load-bearing claims promoted to their own lines
(heavy-traffic=s-aging, the five posits, the MIPS/active-stress fingerprints).
Strongly recommended *if* the per-section peel still reads as six thin-but-
separate sections; skip it if the peel alone already lands cdv1 near v9 density.

## Where things go — no new external document

The three-suffix pattern already has every slot:
- **Derivations / borrowed apparatus** → `cdv1_receipts.md` (composition
  entries; §-keyed; already the home for §5/§6/§13/§15/§16/§22).
- **Narrative / prior-art / motivation** → `cdv1_unabridged.md` (allowed to
  lag; do not touch this session).
- **Claims + falsifiers + pointers** → `cdv1_compressed.md` (the peel target).

Do **not** create a fourth artifact. The one scenario that would justify one: a
*machine-readable* adoption registry for a downstream consumer — but that need
is already met by `mpa-auditor/corpus/api-manifest.json` (curated from cdv1
§Open items + receipts). If that file needs rows, update it; don't make a new
markdown doc.

## What you (Ron) need to decide / provide before or during the session

1. **How hard to trim the speculative adoptions.** Collective hydrodynamics
   (and the active-matter overlay generally) is a *posited extension* with no
   load-bearing positive instance — unlike surface-code/glass which carry the
   primary cross-substrate test. Decide per adoption: stays as a live falsifier,
   or demotes to §Open conjectures (research notes). This is a judgment about
   what has earned framework status; the session should not guess it.
2. **External citations / prior-art to point at.** If your outbound research
   channel has returned a report bearing on any adoption's prior-art mapping,
   hand it to the session so receipts entries cite it rather than re-deriving.
3. **Confirm "no new document."** Above I recommend relocating into receipts.
   If you'd rather the adoptions live as a standalone catalogue doc, say so —
   it changes the target.
4. **One PR or staged.** Recommend one branch, one PR: all six sections peeled
   + matching receipts appends in the same commit, so no half-relocated state
   is ever pushed.

## Hard guardrails (atlas discipline)

- **Forward-only** ([[feedback_forward_only_no_lineage]]). No "moved from §X"
  notes in the SoT — the relocation lives in git history + the receipts entry.
  The peeled SoT must read as if it was always claim-dense.
- **Nothing deleted — relocated.** Every borrowed formula leaving the SoT lands
  in a receipts §. Verify by diff: receipts grows by what the SoT shed.
- **Falsifier per surviving claim.** If a claim has no named falsifier on a
  named substrate (or substrate class), it is not framework content — demote to
  §Open conjectures, don't keep it in the body.
- **mpa-legal.** Don't freeze a quantity the physics requires to flow while
  peeling. (The γ_RO fix is the cautionary instance.)
- **Receipts keying.** Entries are `### §N — Concept name`; the concept name is
  the stable anchor. Append under the existing §; never renumber.
- **Character round-trip before landing** (atlas CLAUDE.md, non-negotiable). A
  spec change to cdv1 must round-trip through a character-test run: from
  `H:/mpa-conform`, `python -m conformer.cli test-character`, watch the dailies
  in DJV (`H:\tools\djv\djv-3.4.2-windows-amd64\bin\djv.exe`). If a substrate's
  character changes shape under the peeled spec, the shot reveals it before the
  commit. **Ron watches this** — it is human-in-the-loop, not a CI gate.

## Done criteria

- cdv1_compressed density approaches v9's (claim-only; borrowed apparatus gone).
- Every surviving claim carries a named falsifier + receipts pointer.
- Receipts grew by exactly what the SoT shed (no apparatus lost).
- §Open items / §Open conjectures consistent with the peeled body.
- Character test round-tripped clean in DJV; then commit + push (one PR).
