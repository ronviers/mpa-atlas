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
**Cite:** Banach fixed-point theorem (standard); Wilson–Polchinski functional RG on space of generators (standard); cdv1 §Universal two-mode kernel (Mori–Zwanzig projection); cdv1 §Pattern formation (Haken slaving); cdv1 §Heat-tax tower (level-to-level map + Landauer pinning); Krzakala et al. 2007 (cavity-method frozen core, inline).
**Bespoke step:** Naming of cdv1's heat-tax tower flow on the space of slow-manifold generators as the compression operator $\mathcal{C}$ in v9's abstract register (cdv1 receipts §6.5). Once the cdv1 construction is in place, v9's Banach contraction $\epsilon < 1$ follows as IR linear-stability of $D\mathcal{A}_{n+1}/D\mathcal{A}_n|_{\mathcal{M}_2}$; the closure conditions (geometric convergence ⇒ Convergent Tower, capacity bound, FDR signatures) follow as before.
**Status:** Tier 1 (load-bearing) closes by composition. Tier 2 (Wilson–Kadanoff structural equivalence) closes by type-identity — see §RG closure entry below, now transitioned from open to closed.

### §Asymptotic closure — no exact 0 or 1 in framework predictions at non-asymptotic operating points
**Type:** structural invariant + survey.
**Cite:** v9 §Boolean section ("$\mathcal{M}_2$ terminal attractor; repeated compression contracts toward $\mathcal{M}_2$ geometrically"); v9 §Compression Axiom ($\varepsilon < 1$ strict; Complexity Wall as $\varepsilon \to 1$ singularity); cdv1 §The chit unit ("Limit-point status. chit = 0 is a critical limit, not an attainable operating state. Substrates approach it asymptotically from either side"); cdv1 §gFDR signatures ($X_c \ll 1$ in deep $c$; $X_r$ unit slope at equilibrium); cdv1 §Universal two-mode kernel ($\beta_{\text{mem}} = 1$ Markovian limit).
**Bespoke step:** Survey of every candidate exact-0/1 value in v9 + cdv1 (16 candidates audited 2026-05-15) resolves consistently: each is either an asymptotic limit (named explicitly with $\ll$, $\approx$, $\to$, or open-interval notation), a normalization convention (arbitrary scale, not a framework prediction), or a categorical label derived from continuous parameters where the categorical boundary is itself singular. No counterexample found across v9 + cdv1. The structural commitment is therefore that MPA carries no exact 0 or 1 at any non-asymptotic operating point, and this is a load-bearing identity of the continuous-physics framework. The only conceivable falsifier is at cosmic heat death (where equilibrium FDR would predict $X_r = 1$ exactly); standard cosmology has heat death as $t \to \infty$, never exactly reached, so the falsifier exists in principle but at the asymptotic boundary of physical reachability. Survey table archived at `mpa-conform/docs/asymptotic-closure-proposal.md` §Survey.

### §Trail-class metric — $\rho([A],[B]) = \lim_n \epsilon^{-n}\,\|\mathcal{C}^n(d_A - d_B)\|$
**Type:** composition.
**Cite:** Krein–Rutman theorem (1948) for positive contracting operators; von Mises power iteration (1929) for the rescaled-limit construction; Kato "Perturbation Theory for Linear Operators" (1966) for spectral projection and exceptional points; Heiss (2004) / Berry (2004) for non-Hermitian-degeneracy phenomenology near gap closure.
**Bespoke step:** Identification of $\rho$ as the Krein–Rutman dominant-eigenmode amplitude. Well-definedness rests on the spectral gap (isolated leading eigenvalue $\epsilon$ of $\mathcal{C}$). Faster-decaying modes vanish under $\epsilon^{-n}$ rescaling, leaving only the leading-eigenmode amplitude of $d_A - d_B$. Distinct from $\varepsilon_n = \|\mathcal{C}_n\|_{op}$, which measures rate of compression at level $n rather than distance between trail classes. At the Complexity Wall the spectral gap closes; $\rho$ is undefined there by construction.
**Open:** Closed-form behavior of $\rho$ as the spectral gap closes. Does it diverge? Does the gap close gracefully?
**Connection to slow-manifold projection (added).** With $\mathcal{C}$ constructed via cdv1's heat-tax + MZ + slow-manifold construction (§Compression Axiom entry above), the trail-class metric $\rho$ is the natural metric on the slow-manifold-projected trail space $\Pi_{\text{slow}}\mathcal{T}$. The $\epsilon^{-n}$ rescaling that defines the metric is dual to the IR linear-stability eigenvalue $\epsilon$ of the level-to-level map — distance between trail classes is measured by the leading-eigenmode amplitude that survives all faster-decaying modes' suppression.

### §RG closure — Tier 2 (Wilson–Kadanoff structural equivalence)
**Type:** composition (closed; previously open).
**Cite:** cdv1 receipts §6.5 — Meta-ledger flow construction; cdv1 §Heat-tax tower; cdv1 §Universal two-mode kernel; cdv1 §Pattern formation; Wilson–Polchinski functional RG (standard).
**Bespoke step:** Type-identity between v9's meta-ledger flow and Wilson–Kadanoff/Wilson–Polchinski functional RG established via cdv1's construction. Both are running-coupling flows on a space of generators with an IR-attracting fixed point ($\mathcal{M}_2$). The three-step proof strategy maps directly:
- (i) Locality factorization: spectral gap of $\mathcal{C}$ at the IR fixed point gives $\mathcal{O}(\epsilon^b)$ cross-window decay.
- (ii) Block-variable capacity preservation: heat-tax substitution coarse-grains the universal two-mode kernel into its own form at level $n+1$, transporting the capacity bound by standard RG arguments.
- (iii) Conjugating isometry: $\phi = \Pi_{\text{slow}}$ by construction (MZ + Haken slaving).

The framework is no longer running on Tier 1 alone; structural equivalence is grounded in cdv1's continuous-physics construction.
**Substrate scope:** Markovian / spectral-gap regime ($\beta_{\text{mem}} = 1$) is proven scope. Non-Markovian Caputo $\beta_{\text{mem}} < 1$ uses fractional-RG generalization (Mittag-Leffler-rescaled β-functions); per-substrate-class Hurst-class conservation under coarse-graining is the verification residual.
**Open** (substrate-conditional, downgraded from foundational): specific functional form of the β-functions on the space of generators per substrate class.

### §Deformation calculus — Theorem 9
**Type:** unrecovered.
**Status:** $\Delta_C(A,B) = 1$ iff $\gamma_{AB} > 0 \land D < \gamma_{AB}$. Multi-session result. The deformation-calculus form survives in compressed; the derivation chain (associator bound → distributivity defect → Boolean deviation) is lost. Theorems 6 and 7 are similarly compressed without surviving derivations.
**Note:** Character §7 recovers Theorem 9 as the discrete-time limit of the adiabaticity bound — that's an *alternative* justification path, not a reconstruction of the original. Cross-link if the alternative holds up under closer reading.

### §Substrate-conditional reading — F.1 Markovian sign caveat
**Type:** composition.
**Cite:** Risken "The Fokker-Planck Equation" (1989) for overdamped-Langevin response theory; Sekimoto "Stochastic Energetics" (2010); Seifert "Stochastic thermodynamics, fluctuation theorems and molecular machines" (Reports on Progress in Physics 75, 126001, 2012). The kernel-width artefact is textbook for the stiff / overdamped limit; empirical support spans colloidal physics, polymer dynamics, syndrome streams, neural mean-field models.
**Bespoke step:** Identification of $\gamma_{AB}$ sign as the framework-register variable that flips under the kernel-width artefact, and $|\gamma|$ + FDR shape as the substrate-class-invariant readings that survive. Confirmed against the surface-code substrate.

### §Surface-code identification
**Type:** empirical.
**Status:** Distance-3 rotated memory-Z, sub-threshold operation, traces clean $s$-aging diagonal. Receipt is the dataset + FDR-fit analysis code.
**Locate before next reconstruction:** current location not tracked. Likely in `mpa-brain/experiments/` or an mpc-* analysis repo.
