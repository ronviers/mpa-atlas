# The Transport-Law Method — Six Steps (extending predictions)

The **outbound** recipe, twin to the inbound translation recipe (`translating_FDR_steps.md`,
`mpa_fdr_treatment.md`). Translation brings an import *into* the framework; this gets predictions
*out* of imports already adopted. Provenance tags: **[est.]** = established literature (resolves to a
`pa:` key in `mpa_prior_art.md`), **[MPA]** = the framework's own binding.

The unit of predictive content is **not** a claim "X = Y." It is the **transport map**: one substrate
parameter $\theta$, read in several registers through fixed *known* functions $f_i$, so that a measurement
in one register pins $\theta$ and predicts the others — $\text{register}_j=f_j\!\big(f_i^{-1}(\text{register}_i)\big)$.
A numerical identity is the degenerate special case where the maps happen to agree at one point.

---

## Why it works — what lets MPA surface correct structure

This is the load-bearing claim; the recipe is its mechanization. MPA surfaces correct things — the
transport law, the frustrated triad it "dragged into the light" (`mpa_fdr_treatment.md` §4–5) — for four
interlocking reasons, none of them luck:

1. **One degeneracy, read from many sides.** Boolean ($D\to\infty$), Markov, equilibrium, detailed
   balance, the balanced gaugeable ring, $X\equiv1$, $\mathcal{A}=0$, $\beta=1$ are *the same* degenerate
   point in MPA's reading. The spine is literally the deformation away from it. So every register's
   degenerate limit is forced to **one** place — the coincidence point — and the source theories' separate
   "trivial limits" are revealed as a single shared origin.

2. **Gauge-invariant order parameters force structure, not parametrization.** $\mathcal{A}=\oint v/D_0$,
   chit, $\varepsilon$, $X$, $\beta$ are coordinate-free, so they survive substrate-stripping. Asking the
   *necessity* question about a coordinate-free quantity — "what is the **minimal carrier** of
   $\mathcal{A}\ne0$?" — cannot return a number; it returns a **structure** (the directed, imbalanced,
   chiral 3-cycle). This is why MPA surfaces topology on its own: gauge-invariance + minimality push
   structure into the light.

3. **Co-parametrization over-determines, and over-determination is both the content and the filter.**
   Forcing independently-derived imports to read one $\theta$ makes the system over-determined; the
   consistency demand is content the sources never had to meet (the prediction). The same
   over-determination is the **sieve**: a binding that cannot be over-determined — single register,
   definitional identity, a hand-frozen constant — cannot be checked, and that is exactly where MPA risks
   metaphor.

4. **Two readings cross-check every object.** Each must hold as both a discrete operator-algebra invariant
   (STRUCTURAL) and a continuous driven-dissipative attractor/fixed point (CHARACTER). Surviving both is two
   independent derivations of one object — the triad is both a signed-graph balance object and a
   complex-Jacobian-spectrum object; that double-grounding is why it reads as *forced*, not chosen.

**Net.** MPA is correct-by-construction wherever it merely re-reads an import (it cannot be more wrong than
its source). It can add error **only** in the bindings it proposes — the co-parametrizations and
minimal-carrier identifications. It surfaces *correct* bindings because its proposal mechanism (minimal,
gauge-invariant departure from one named degeneracy) emits precisely the structures that recur across the
dissipative universe — anomalous exponents, limit cycles, frustrated cycles, complex spectral pairs — and
its filters (over-determination + the two-reading cross-check + the mpa-legal "does it flow or sit inert"
audit) reject the rest. **The failure mode is named:** where a binding cannot be over-determined, the filter
is blind. The gate ledger (`mpa_frontier.md`) and the corrections log keep proposals in the filterable
regime. **[MPA]**

---

## The recipe — six steps (each guards one failure mode)

**Step 1 — Find a shared-parameter bundle.** In the adoption catalogue + prior-art map, locate a set of
imported results the spine ties to *one* substrate quantity $\theta$. *Guards: ungrounded analogy — if no
single $\theta$ is forced, there is no bundle.*

**Step 2 — Confirm register independence in the sources (the metabolize gate).** The source disciplines
must not already equate the registers. *Guards: a definitional identity masquerading as a prediction — if
the literature already ties them, the map is empty and MPA adds nothing.* **[MPA]**

**Step 3 — Write each map explicitly** from the import's own asymptotics: $\text{register}_i=f_i(\theta)$,
then compose $f_j\circ f_i^{-1}$. *Guards: hand-waving — a map you cannot write is not a prediction.*

**Step 4 — Locate the coincidence / degeneracy point** where all $f_i$ agree (the imported-math limit:
$\beta=1$, $\varepsilon\to0$, equilibrium). *Guards: claiming content at the limit where MPA is pure import
— attach the math in the interior, never at the degenerate point.*

**Step 5 — Rank by leverage** = how fast the maps separate near the achievable operating point. *Guards:
spending a battery on a weak test — maps that stay close give no discriminating power; maps that diverge
fast (e.g. $\beta/(2-\beta)$ vs $1/\beta$ below $\beta=1$) turn a small $\theta$-error into a large,
falsifiable register disagreement.*

**Step 6 — Pre-register the collapse falsifier; run it on one substrate across $\ge2$ registers.** If the
inferred $\theta$'s fail to agree through the maps, the law is falsified for that substrate class. *Guards:
false closure — a transport law with no collapse test is metaphor.* Candidates enter the gate machine at
`steeping` (`mpa_frontier.md`) and only stake on a surviving collapse test.

---

## Worked example — the $s$-exponent transport law ($\beta$-hub)

$\theta=\beta$, one shared anomalous-diffusion exponent, read in three registers (receipts §9; engine
ADOPTION queueing + consolidated falsifier; closed-form adjudication in
`docs/exponent_identity_check.py`):

| register | map $f_i(\beta)$ | source |
|---|---|---|
| FDR aging / memory | $\alpha_s=\beta_{\text{mem}}=\beta$ | `pa:ck-aging`, `pa:pottier-fdr`, `pa:caputo-fractional` **[est.]** |
| fBm queue, heavy traffic | $\beta/(2-\beta)$ ($H=\beta/2$) | `pa:fbm-queueing` **[est.]** |
| M/G/1 heavy-tailed service | $1/\beta$ | `pa:kingman` **[est.]** |

- **Coincidence (Step 4):** all three $=1$ only at $\beta=1$ (Markovian). Off-Markovian they are distinct
  known functions — the interior is where the law has content.
- **Leverage (Step 5):** at $\beta=0.6$ the legs read $0.600\,/\,0.429\,/\,1.667$ — wide separation, a
  high-leverage test.
- **Falsifier (Step 6):** a substrate whose measured aging and queue-tail exponents fail to collapse onto a
  common $\beta$ through the maps. **[MPA]**

The predictive content is the **transport** — measure aging on a substrate, predict its queue tail — which
is new because Pottier never spoke to Norros (Step 2 passes). The old "$\alpha_s=\beta=$ heavy-traffic
exponent" identity was the $\beta=1$ point mistaken for the whole law (corrections log, receipts §9).

---

## Candidate bundles (open — `mpa_frontier.md` `steeping`)

- **$\varepsilon$-hub (distance-to-Wall).** Registers: FDR aging $\beta_{\text{mem}}\approx1-\varepsilon$
  (P1, engine) · heat-tax $\alpha(\varepsilon)=\alpha_0(1-\varepsilon)$ (§6) · avalanche branching $\to1$
  at $\varepsilon=1$, SOC $\tau\approx3/2$ (`pa:` SOC) · CTRW critical length $\ell_c(\beta_{\text{mem}})$
  (`pa:ctrw`). Degenerate at $\varepsilon=0$ (equilibrium) and $\varepsilon=1$ (Wall: all $\to1$ / diverge);
  bites in the open interior. **Prediction:** aging slope $\to\varepsilon\to$ branching ratio + correlation
  length on one substrate.
- **chit-hub ($=-\ln\rho$).** Registers: queue load chit $=-\ln\rho$ (engine ADOPTION) · relaxation
  oscillation $Q(\text{chit})$ non-monotonic, peak at chit$=1\,$ch (§13) · phase-lock suppression
  $K_{AB}\propto(1+4Q^2)^{-1/2}$ (§15). Degenerate at chit$\to0$ and chit$\to\infty$ (both $Q\to0$,
  overdamped); signal only in the mid-chit band. **Prediction:** RO ringing band $\to$ chit $\to$ load +
  phase-lock suppression. (RO and phase-locking are both on the testbeds — start here per leverage + cost.)
- **triad-hub (on/off-valued, not exponent-valued).** The two-frame construction is *already* a transport
  law of this flavor and `staked`: self-probe definedness $\Leftrightarrow J\ne0\Leftrightarrow\mathcal{A}
  \ne0\Leftrightarrow\triangle$ (`mpa_fdr_treatment.md` §4). It shows the schema is not exponent-specific —
  any iff-chain across registers is a transport law, and its collapse falsifier is the iff-chain break.

---

*Imports* (all `pa:` keys → `mpa_prior_art.md`): `ck-aging`, `pottier-fdr`, `caputo-fractional`,
`fbm-queueing`, `kingman`, `ctrw`. Everything else — the transport-map framing, the six-step filter, the
over-determination-as-sieve reading, the $\varepsilon$/chit-hub bundles — is the residual MPA owns by the
prior-art ledger's exclusion rule.
