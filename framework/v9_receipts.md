# v9 receipts

**Companion to:** [`v9_compressed.md`](v9_compressed.md).
**Status:** Live. Append-only during prove-as-you-go work.

A single line in `v9_compressed.md` may rest on multi-session work. This file is where that work lives, keyed to the compressed line it justifies. The unabridged companion [`v9_unabridged.md`](v9_unabridged.md) becomes reconstructible from `v9_compressed.md` + this file; this file is what makes reconstruction tractable.

If receipts and compressed disagree, treat as bug.

---

## Workflow

When a session proves, derives, or composes a result that becomes a line in compressed:

1. Write the compressed line as usual.
2. **In the same session**, append an entry here under the matching section name.
3. Tag with a type (below).
4. Don't leave the session without at minimum a type tag and a one-line summary. Now is the cheapest moment; later is more expensive every time.

**No retrofitting.** Lines whose proof tree is gone get `unrecovered` and a brief note. An honest marker beats a plausible-sounding fabrication.

**Keying.** Reference compressed sections by name (`§Capacity`, `§Operators`), not line number. Section names are stable across edits; line numbers are not.

**Granularity.** One entry per claim needing justification *beyond* the compressed line itself. Definitional content needs no entry. A compressed section may have zero or many entries.

---

## Type tags

- `standard` — textbook result. Citation only.
- `composition` — standard components, bespoke assembly. Cite components + name the bespoke step.
- `bespoke` — novel result. Proof shard, condensed but verifiable.
- `unrecovered` — load-bearing, derivation lost. Marker only; do not fabricate.
- `open` — known open question carried forward from compressed.
- `empirical` — empirical claim. Point to dataset + analysis.

---

## Entries

### §Three typed objects (vertex regime) — three-regime threshold structure
**Type:** composition.
**Cite:** Sieberer–Buchhold–Diehl (driven open quantum systems); Haken (laser threshold). Inline in compressed.
**Bespoke step:** Identification of $c$/$s$/$r$ with above-threshold / near-threshold / sub-threshold cooperativity regimes. Load-bearing analogy of the framework; threads through to Character §1 bridge.

### §Operators — $R$: $W_R/\kappa \ge \ln 2 \cdot H(A\mid\text{rest})$
**Type:** unrecovered.
**Status:** Conditional-Landauer extension for severing. The $\kappa = k_B T \cdot \xi_{sub}$ recovery survives in compressed; the derivation of the *conditional* form (vs raw $H$) and the $\xi_{sub}$ identification with substrate-class is gone. Load-bearing — referenced by §Boolean section and Character §2 (Bit/Chit pairing).
**Future verification path:** rederive against Sagawa–Ueda info-thermodynamics; confirm the conditional form drops out as the natural generalization.

### §Capacity — $|\Gamma^*| \le \sqrt{2D/(\alpha\,\gamma_{min}\,d_{avg})}$
**Type:** unrecovered.
**Status:** Multi-session theorem. Components survive (Amit–Gutfreund–Sompolinsky 1985 for the $\sqrt{D}$ Hopfield ceiling; Mézard–Parisi–Zecchina 2002 for the sharp k-SAT wall, both cited inline). The connecting tissue is gone: identification of $(\Phi^*, \kappa)$ substrate envelope with $(D, \gamma_{min}, d_{avg})$ of the bound; specific factor $2/\alpha$; whether the bound is tight or order-of-magnitude. Capacity is load-bearing; this is the most painful `unrecovered` entry. Tied to Character §5 `η(Γ*)` open item — both close together if either is rederived.

### §Compression Axiom — $\epsilon = \|\mathcal{C}\|_{op} < 1$ contraction
**Type:** composition.
**Cite:** Banach fixed-point theorem (standard); Wilson–Kadanoff RG block-spin (standard); Krzakala et al. 2007 cavity-method frozen core (inline).
**Bespoke step:** Application of Banach contraction to the meta-ledger ascent operator $\mathcal{C}$. Once granted, closure conditions (operator norm < 1 ⇒ geometric convergence ⇒ Convergent Tower) follow. Tier 1 results (Convergent Tower, capacity bound, FDR signatures) are load-bearing on this step. Tier 2 (Wilson–Kadanoff structural equivalence) is open by compressed's own admission.

### §Trail-class metric — $\rho([A],[B]) = \lim_n \epsilon^{-n}\,\|\mathcal{C}^n(d_A - d_B)\|$
**Type:** bespoke.
**Shard:** Well-definedness rests on the spectral gap (isolated leading eigenvalue $\epsilon$ of $\mathcal{C}$). Faster-decaying modes vanish under $\epsilon^{-n}$ rescaling, leaving only the leading-eigenmode amplitude of $d_A - d_B$. Distinct from $\varepsilon_n = \|\mathcal{C}_n\|_{op}$, which measures rate of compression at level $n$ rather than distance between trail classes. At the Complexity Wall the spectral gap closes; $\rho$ is undefined there by construction.
**Open:** Closed-form behavior of $\rho$ as the spectral gap closes. Does it diverge? Does the gap close gracefully?

### §RG closure — Tier 2 (Wilson–Kadanoff structural equivalence)
**Type:** open.
**Status:** Compressed itself flags this as a classification conjecture with a three-step proof strategy: (i) trail-norm locality factorizes over $\tau_{obs}$-windows with exponentially small cross-terms; (ii) block variables $D_k$ at scale $b$ satisfy $D^{(b)} = f(b, D)$ with the same capacity bound; (iii) an isometry $\phi$ on $\mathcal{T}$ conjugates $\mathcal{C}$ to block-averaging on the slow manifold. Not load-bearing; framework runs on Tier 1 (Banach contraction).

### §Deformation calculus — Theorem 9
**Type:** unrecovered.
**Status:** $\Delta_C(A,B) = 1$ iff $\gamma_{AB} > 0 \land D < \gamma_{AB}$. Multi-session result. The deformation-calculus form survives in compressed; the derivation chain (associator bound → distributivity defect → Boolean deviation) is lost. Theorems 6 and 7 are similarly compressed without surviving derivations.
**Note:** Character §7 recovers Theorem 9 as the discrete-time limit of the adiabaticity bound — that's an *alternative* justification path, not a reconstruction of the original. Cross-link if the alternative holds up under closer reading.

### §Substrate-conditional reading — F.1 Markovian sign caveat
**Type:** bespoke.
**Shard:** Stiff/Markovian substrates (overdamped Langevin, syndrome streams) produce kernel-width artefact: the trail vector responds to the *derivative* of the stimulus rather than its level (in $\dot x = -\partial U/\partial x + \xi$, response sign tracks $\partial U/\partial x$ not $U$). Sign-flip of $\gamma_{AB}$ readings is the consequence; $|\gamma|$ + FDR shape are the invariants that survive the artefact. Confirmed against the surface-code substrate.
**Cite:** Standard overdamped-Langevin response theory (Risken).

### §Surface-code identification
**Type:** empirical.
**Status:** Distance-3 rotated memory-Z, sub-threshold operation, traces clean $s$-aging diagonal. Receipt is the dataset + FDR-fit analysis code.
**Locate before next reconstruction:** current location not tracked. Likely in `mpa-brain/experiments/` or an mpc-* analysis repo.
