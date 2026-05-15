# Translating Fluctuation-Dissipation: Character-Domain cFDT

**Status:** Translation document. Six-step structural→character translation applied to fluctuation-dissipation theorems and relations (FDT/FDR).
**Spec:** [`mpa character framework.md`](mpa%20character%20framework.md).
**Apparatus:** [`mpa character holding apparatus.md`](mpa%20character%20holding%20apparatus.md). The character-domain fluctuation-dissipation content here composes with apparatus §3 (entropy production, Harada–Sasa, three coherence regimes) and §15 (Q–Γ uncertainty).
**Methodology source:** [`translating FDR.md`](translating%20FDR.md). The six-step process originally worked through on Force-Deformation Response (mechanical FDR); applied here to the Fluctuation-Dissipation Relation (statistical-physics FDR/FDT).
**Sibling spec (other domain):** [`v9_compressed.md`](v9_compressed.md). v9's "Fluctuation-dissipation signatures" section provides the structural-MPA treatment with per-structural-regime universality invariants ($X_c$, $\alpha_s$, $P_s$, $X_r$, $N_f$); the present document adds an orthogonal coherence-regime axis.
**Directory map:** [`README.md`](README.md).

---

## Why this document

Two different things are called "FDR" in this corpus:

- **cFDR** (the framework's existing apparatus): character-domain Force-Deformation Response — stiffness, yield, fatigue, creep, hysteresis. Translated from structural mechanics. Demonstrated in [`cFDR demonstration.md`](cFDR%20demonstration.md).
- **FDR / FDT** (statistical physics): Fluctuation-Dissipation Relation / Theorem — the relation between spontaneous fluctuations and response to perturbation. The s-regime aging shape that mpc-glass and mpc-quantum measure as cross-substrate transfer evidence; the integrated FDT-violation that gives entropy production rate σ via Harada–Sasa.

These are different concepts sharing an abbreviation. This document translates the second into character-domain form, calling the result **cFDT** to disambiguate. The character-MPA framework already touches FDT at the foundation level (apparatus §3 ties σ to integrated FDT-violation), but a focused translation surfaces what character-MPA contributes that standard non-equilibrium FDR doesn't.

The contribution: standard non-equilibrium FDR identifies the s-regime aging diagonal as universal across NESS substrates with memory. Character-MPA refines this by predicting that *within* the s-regime, the parametric plot shape distinguishes the framework's three coherence regimes (imposed, emergent, critical). This is testable structure on top of the universality.

---

## Step 1: Deep commonality

FDT/FDR formalizes the relation between two measurable quantities of a stochastic process:

- $C(t, t') = \langle x(t)\, x(t') \rangle$ — the correlation function. How similar is the system's state at time $t$ to its state at time $t'$.
- $\chi(t, t')$ — the response function. How does the system at $t$ respond to a small perturbation applied at $t'$.

In equilibrium, these are tied: the same fluctuations that occur spontaneously also drive the response. The proportionality is $1/T$ (FDT). Out of equilibrium, the strict theorem breaks but a *generalized* relation still holds, with an FDR-violation factor $X(t, t')$:

$$\chi(t, t') = \frac{X(t, t')}{T} \frac{\partial C(t, t')}{\partial t'}$$

Stripped to its essence: FDR formalizes how a sustained process's spontaneous fluctuations and response to perturbation are related. That deep relation survives substrate-stripping. Character-domain holdings have both spontaneous fluctuations (the holding amplitude varies under noise) and response (probes elicit measurable response). The relation between the two is character-native content.

---

## Step 2: Hidden assumptions audit

Standard FDR/FDT embeds:

| Assumption | Holds for character domain? |
|---|---|
| Equilibrium baseline; FDT-violation is "deviation from equilibrium" | No — no rest state; every holding is NESS |
| Bath at fixed temperature $T$ coupled to system | No — substrate-equivalent decay-driving parameters; mode-specific |
| Single scalar observable $x$ | No — holdings are typically multi-mode, hierarchical |
| Stationary distribution | Partially — holds within a developmental phase, broken across phases |
| Linear response | No — saturation kicks in early; active modulation reshapes response |
| Memoryless / Markovian dynamics or specified memory kernel | No — substrate plasticity, internal models, dual-control all introduce memory |
| Single time-window readout | No — F-009 in mpc-glass already shows window-dependent regime |
| Passive probe (probe doesn't change system structure) | No — active modulation; probe can shift operating point |
| Gaussian fluctuations | No — power-law statistics in critical regime |
| Detailed balance at equilibrium | No — every NESS breaks detailed balance |

Most assumptions fail. The translation isn't a small adjustment; it's generalization across multiple simultaneous structural commitments.

---

## Step 3: Concept classification

| FDR/FDT concept | Bucket | Character-domain analogue |
|---|---|---|
| Correlation function $C(t,t')$ | Direct | Holding-amplitude correlation between times |
| Response function $\chi(t,t')$ | Direct | Holding-amplitude response to small perturbation |
| FDT (equilibrium relation) | Direct (degenerate) | Special case of cFDT at zero drive ($g, \kappa \to 0$) |
| X-ratio / FDR-violation factor $X(t,t')$ | Direct | Local measure of how out-of-equilibrium the holding is; integrated $X$ deviation gives σ (Harada–Sasa, apparatus §3) |
| Parametric plot $\chi$ vs $1 - C/C(0)$ | Direct | Same plot; shape encodes regime info |
| Aging diagonal (s-regime) | Direct | Universal signature of NESS with memory; v9's $\alpha_s$, $P_s$ |
| Plateau height $P_s$ | Direct | Asymptotic correlation; mode-dependent |
| Effective temperature $T_{\text{eff}}$ | Modified | Substrate-equivalent decay-driving parameter; mode- and history-dependent, not a single bath temperature |
| Single time-window readout | No transfer | Replace with multi-window cFDT sweep |
| Linear response | Modified | Replace with saturation-aware nonlinear response |
| Passive probe | Modified | Replace with active-probe formalism (probe-as-perturbation that the holder may modulate against) |
| Detailed balance | No transfer | Replace with detailed-balance-breaking as the defining feature of NESS (apparatus §3) |
| Gaussian fluctuations | Modified | Generic in imposed/emergent regimes; non-Gaussian (power-law) in critical regime |
| Stationary distribution | Modified | Replace with phase-stationary (within a developmental phase, apparatus §7) |

Most concepts transfer with renaming. The four "no transfer" or "modified" items are where character-MPA does work that standard non-equilibrium FDR doesn't.

---

## Step 4: Replacements for "no transfer" items

**R1. Substrate-equivalent temperature.** Standard FDT uses bath $T$. Character-domain has no literal temperature. The analogue is a substrate-equivalent decay-driving parameter $T_{\text{sub}}$ — a property of the substrate-in-mode that sets the scale of fluctuations driving decay. It is mode-specific, history-dependent, and may differ for different aspects of the same substrate (a behavioral substrate has different $T_{\text{sub}}$ for distractors-affecting-attention vs distractors-affecting-mood). The X-ratio $X = T_{\text{eff}}/T_{\text{sub}}$ measures how the system's effective fluctuation scale deviates from its substrate-driven scale — bounded above by 1 in the equilibrium limit.

**R2. Multi-window cFDT.** Single-window readout is wrong. The framework's regime classification is window-dependent at the structural-MPA level (mpc-glass F-009: regime-spectrum $R(\tau_{obs})$ as central observable) and at the character-MPA level (mode formation has developmental phases with different timescales). Character-FDT is naturally multi-window: $X(t, t', \tau_{obs})$. The shape of the parametric plot migrates with window. The migration itself is a regime-distinguishing observable.

**R3. Active-probe formalism.** Probes can engage the holder's active modulation. cFDT distinguishes:

- *Passive probe:* small, fast perturbation that doesn't engage active modulation. The holder's response is the linear-response function. This is the closest analogue to standard FDR.
- *Active probe:* slow or large perturbation that the holder modulates against. The holder's response includes its information-bottleneck-optimal compression of the probe (apparatus §3). The response function is no longer just material; it is the holder's response strategy.

The two probe types yield different parametric plots. Standard FDR conflates them; character-FDT separates them. For mpc-glass and mpc-quantum, this matters: small thermal/error-rate perturbations are passive probes; deliberate stress/fault injection that triggers correction-loop adaptation is an active probe.

**R4. Detailed-balance-breaking as default.** Standard FDR is framed as "violated relative to equilibrium." Character-MPA reframes: equilibrium is the special case (zero drive, $g = \kappa = 0$). The general case is sustained NESS with broken detailed balance, where cFDT holds with $X < 1$. The reframing is more than vocabulary — it changes what counts as the "anomaly" and what counts as the baseline. Aging is not anomaly; equilibrium is degeneracy.

---

## Step 5: Imported machinery

Most needed apparatus is already in the framework:

- **Stochastic thermodynamics** (Seifert, Sekimoto, Jarzynski, Crooks) — already imported (apparatus §3). Provides general FDT for non-equilibrium systems and the trajectory-level definition of entropy production.
- **Harada–Sasa relation** — already imported (apparatus §3). Integrated FDT-violation gives σ. The bridge between fluctuation-dissipation content and the framework's chit-rate primitive.
- **Cugliandolo–Kurchan generalized FDT** — well-developed structural-physics treatment of aging-system FDR. v9_compressed §"Fluctuation-dissipation signatures" cites the lineage; per-structural-regime invariants there ($X_c$, $\alpha_s$, $P_s$, $X_r$, $N_f$).
- **Information geometry on response functions** (Amari) — for the active-probe formalism. The holder's response strategy is information-geometric on the substrate's mode structure.
- **Linear-response theory and non-equilibrium extensions** (Kubo formula and generalizations) — well-developed; foundational for the response-function side.
- **Nonlinear response theory** — for saturation-aware extension. Character-domain holdings exit the linear regime quickly because saturation is the stabilization mechanism (apparatus §8).
- **Power-law and 1/f spectra theory** — for the critical-coherence regime (apparatus §3, from #6 SOC adoption).

No further imports needed; the apparatus already covers what cFDT requires.

---

## Step 6: Integration check

cFDT composes cleanly with existing framework apparatus:

- **Three coherence regimes (apparatus §3, framework §3.6).** Each predicts a distinct cFDT shape. Detailed predictions in the next section.
- **Bifurcation typology (apparatus §3).** Critical-slowing exponents near threshold show up in cFDT scaling. Saddle-node $|g - \kappa|^{1/2}$, pitchfork $|g - \kappa|$, Hopf $|g - \kappa|$ for the radial mode with neutral angular mode — all should appear as scaling exponents in the parametric plot near transitions.
- **Q–Γ uncertainty (apparatus §15).** Time-bandwidth uncertainty constrains cFDT shape: a sharp spectral feature (high $Q$) is conjugate to a slow temporal response (small $\Gamma$), and the parametric plot's shape is bounded by this constraint. Selectivity and responsiveness are conjugate; cFDT inherits the bound.
- **v9 structural-MPA per-regime invariants** ($X_c, \alpha_s, P_s, X_r, N_f$) — these classify within the structural c/s/k/r propositional regimes. Character-MPA's coherence regimes (imposed, emergent, critical) are orthogonal: a holding can be c-regime imposed, c-regime emergent, c-regime critical — three distinguishable cases sharing the c-regime structural classification. cFDT predicts that the structural invariants are *modulated* by the coherence regime; the universality v9 reports is conditional on coherence-regime selection.
- **mpc-glass F-009 multi-window result.** cFDT is naturally multi-window. The migration of the parametric plot across windows composes with character-MPA's developmental-phase apparatus (apparatus §7) — modes at different developmental phases produce different multi-window cFDT signatures.

Open: per-coherence-regime cFDT shapes haven't been verified empirically. The mpc-glass and mpc-quantum data already collected may be re-analyzable to test the predictions. That's the first contact case for cFDT.

---

## Per-regime cFDT predictions

The framework's central testable contribution. For each coherence regime (apparatus §3, framework §3.6), cFDT predicts a distinct parametric-plot shape and a distinct multi-window migration.

> **Empirical status (2026-05-05) — awaiting RFC-S-compliant test.** First operationalization attempt on smoke and library-grade data showed the parametric-plot characterizations don't separate operating points by gt-label as proposed. *That attempt was not a proper test.* The predictions below are stated in absolute observable space (parametric-plot shape, decay exponent, multi-window migration); under [MPA-RFC-S §1–§2](../rfcs/MPA-RFC-S_Scale-Management.md), regime predictions must be stated in $(D, \tau_{obs})$-space, with the substrate emitting $D = \Phi^*/\kappa$ per operating point and observer positions chosen via driver-profile auto-remap rule. None of those three (predictions in $(D, \tau_{obs})$-space, $D$ emission, driver profiles) is currently in place. See [`cFDT first analysis.md`](cFDT%20first%20analysis.md) §"Critical caveat" for the full diagnosis.
>
> Treat the per-regime claims below as *originally hypothesized* predictions — preserved for the record and as targets for re-derivation in $(D, \tau_{obs})$-space once the substrate-side $D$-emission and RFC-S driver profiles are in place. They are neither validated nor falsified by current data.

### Imposed coherence

- **Source.** Linear-NESS regime; coherence held at minimum entropy production by external constraint (Prigogine).
- **Short-time cFDT.** Close to equilibrium FDT line (unit slope, $X \approx 1$). The constraint maintains the holding near its lowest-dissipation NESS, so spontaneous fluctuations and response are tightly correlated.
- **Long-time cFDT.** Slight deviation; $X$ drops slowly with time-difference $\tau = t - t'$. The aging diagonal exists but is shallow.
- **Multi-window migration.** Shape relatively window-invariant; the system has a single dominant timescale set by the constraint.
- **On constraint removal.** Returns toward equilibrium FDT. The holding dissolves.
- **Distinguishing signature.** $X$ stays close to 1 across most of the parametric plot; the deviation is concentrated at very long times.

### Emergent coherence

- **Source.** Far-from-equilibrium self-organized regime; coherence sustained by its own dynamics (MaxEP-like).
- **Short-time cFDT.** Already deviating from FDT ($X < 1$ at short times). The system is actively dissipating, not just relaxing.
- **Long-time cFDT.** Structured aging diagonal. $X$ value depends on mode, on history, on substrate plasticity. Multiple timescales typical.
- **Multi-window migration.** Pronounced. Different windows show different effective $X$ values, because the substrate has multiple emergent timescales (developmental, operational, drift).
- **On constraint removal.** Persists; the holding is self-sustaining.
- **Distinguishing signature.** Significant FDT-violation across timescales; clear aging diagonal; window-dependent shape.

### Critical coherence

- **Source.** Self-organized to threshold; operates at near-zero reserve, with $\Gamma \to 0$.
- **Short-time cFDT.** Power-law fluctuations imply non-Lorentzian $C(t,t')$; the parametric plot is fractal-like rather than smooth-curved.
- **Long-time cFDT.** Scale-invariant. The parametric plot looks similar at all scales (the defining critical signature).
- **Spectrum.** $1/f$ rather than Lorentzian. Standard FDT computations using Lorentzian-shaped autocorrelations give incorrect $X$ values.
- **Multi-window migration.** None — the regime is scale-invariant by construction. This *distinguishes* critical from emergent, where multi-window migration is pronounced.
- **On constraint removal.** Depends on whether criticality was imposed (loses criticality) or self-organized (retains criticality if drive is sustained at threshold-permitting level).
- **Distinguishing signature.** Stationary scale-invariant parametric plot; no window-migration; power-law statistics rather than Gaussian.

---

## Composition with v9 structural-MPA

v9_compressed §"Fluctuation-dissipation signatures" provides per-structural-regime invariants:

- $X_c = 0$ for committed regime (suppressed response, narrow horizontal locus)
- $\alpha_s$ = slope of aging segment (CK ratio) for suspended regime
- $P_s$ = plateau height for suspended regime  
- $X_r = 1$ for reset regime (unit-slope FDT)
- $N_f$ = transient-negative fraction for frustrated regime

These classify the propositional state. cFDT adds an orthogonal classification of how the coherence is maintained:

| Structural regime | × | Coherence regime | = Combined classification |
|---|---|---|---|
| c (committed) | × | imposed | committed-imposed (rare; usually self-sustaining = emergent) |
| c (committed) | × | emergent | committed-emergent (the typical case for v9's c-regime) |
| c (committed) | × | critical | committed-critical (committed but operating at near-zero reserve; unusual but not impossible) |
| s (suspended) | × | imposed | suspended-imposed (the typical case for v9's s-regime — pumped by drive) |
| s (suspended) | × | emergent | suspended-emergent (sustained by self-organization, not external constraint; tests MaxEP claim) |
| s (suspended) | × | critical | suspended-critical (operating at threshold; SOC instances) |
| r (reset) | × | (any) | r is decayed; coherence regime is degenerate |
| k (frustrated) | × | (any) | k is structural; coherence regime is mode-of-frustration-maintenance |

The combined classification refines what's measured. v9's $\alpha_s$ for a given substrate may take different values depending on whether the s-regime is imposed (pumped) or emergent (self-organized) or critical (at threshold). The structural-MPA "universality" of $\alpha_s$ across substrates may be tighter (universal within each coherence regime) or looser (variable across coherence regimes) than current measurements suggest. This is testable.

The mpc-glass and mpc-quantum measurements report $\alpha_s$ values: glass at canonical aging, surface-code syndromes at sub-threshold. Are these in the same coherence regime? If so, $\alpha_s$ should match. If different coherence regimes, $\alpha_s$ should differ predictably. The cFDT layer sharpens the cross-substrate transfer test: it's not just "do they show the s-aging diagonal" but "do they show it at the same coherence regime."

---

## What this gives mpc-glass and mpc-quantum

cFDT delivers two contributions to those projects' ongoing work:

1. **A coherence-regime axis to add to existing measurements.** The same data can be re-read through the imposed/emergent/critical classification. The signatures (parametric-plot shape, multi-window migration, power-law vs Gaussian statistics) are computable from existing time-series. First contact case for cFDT — no new simulator runs required.
2. **Refined cross-substrate transfer test.** v9's claim is that the s-aging shape is universal across NESS substrates (glass, surface-code syndromes). cFDT predicts the universality is conditional: substrates in the same coherence regime should match; substrates in different coherence regimes should differ predictably. The cross-substrate match-or-fail isn't binary — it's a four-way comparison (do glass and QEC at the same coherence regime match? do they show predictable difference at different regimes?).

These contributions don't replace mpc-glass / mpc-quantum's existing structural-MPA work — they refine it. The s-aging diagonal universality is preserved; cFDT adds the regime axis that says when universality is tight and when it's loose.

---

## What cFDT is and is not

It is the character-domain translation of fluctuation-dissipation. Most concepts transfer directly with renaming; the structural assumptions to replace are about temperature, time-window, probe activity, and detailed-balance default. The framework apparatus already covers what's needed — no further imports.

It is not a new derivation of FDT (the existing physics is rigorous; nothing here replaces it). It is not a refutation of v9's per-structural-regime invariants (those are preserved). It is not a substitute for empirical work on glass and QEC substrates (the predictions need testing on real data).

The character-MPA contribution is the orthogonal axis: imposed/emergent/critical coherence regimes refine the universality claim that the s-aging diagonal makes about NESS substrates. The refinement is testable on data already collected.
