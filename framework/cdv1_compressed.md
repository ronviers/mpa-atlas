# MPA-Character (operational source of truth)

**Status:** Claim-only operational source of truth, extracted from [`cdv1_unabridged.md`](cdv1_unabridged.md) (the paper). On any disagreement of claim content, this file wins.

**Companions:**
- [`cdv1_unabridged.md`](cdv1_unabridged.md) — public-facing prose-and-prior-art paper. Carries derivations, integrative narrative, paper-grade citations, appendices. Allowed to lag this file by at most one closure.
- [`cdv1_receipts.md`](cdv1_receipts.md) — line-keyed justifications. Append-only during prove-as-you-go work.

If this file disagrees with [`v9_compressed.md`](v9_compressed.md) on shared primitives, treat as bug. If this file disagrees with receipts, treat as bug.

**Scope.** Continuous physical economics of sustained NESS traversal — what a structure is *being* against a bath. v9 specifies topology, edge shears $\gamma_{AB}$, and discrete operator algebra; character specifies the driven-dissipative dynamics that traverse it.

---

## Setting and primitives

A coherence is a macroscopic pattern of continuation maintained against natural dissolution. A holding is the continuous extraction of entropy or application of work that maintains it.

**Primitives.** Maintenance budget $G_0$ (unsaturated active work supplied per unit time, scales with $D$; laser-analogue small-signal gain). Decay rate $L$ (spontaneous relaxation rate to bath; cavity loss).

## Bridge to v9

At zero amplitude, the linearised field equation has eigenvalue $\lambda_A \approx L - G_0$. v9's regime conditions translate:

| v9 regime | $\lambda_A$ vs $D$ | $G_0$ vs $L$ | Reading |
|---|---|---|---|
| $c$ | $\lambda_A \ll -D$ | $G_0 - L \gg D$ | deeply above threshold, saturation-clamped |
| $s$ | $|\lambda_A| \lesssim D$ | $|G_0 - L| \lesssim D$ | near threshold; Schawlow–Townes broadening + CK aging coexist |
| $r$ | $\lambda_A \gg D$ | $G_0 - L \ll -D$ | sub-threshold; spontaneous emission only |

$G_0/L$ and $\lambda_A/D$ are different coordinates on the same regime structure.

## The chit unit

$$\text{chit} = \ln(G_0/L)$$

The log form is required by stochastic thermodynamics: $\ln(k_+/k_-)$ is the Crooks rate-ratio entropy production per stochastic transition. Three earlier-cited reasons (threshold symmetry, additivity, $\ln 2$ Landauer alignment) are three faces of the same rate-ratio structure, not independent justifications.

**Markovian / orbit-affinity faces.** The rate-ratio reading is the Markovian specialisation of a per-orbit reading: $\text{chit}_{\text{orbit}} = \oint v(\theta)/D(\theta)\,d\theta$ — the continuous-orbit Schnakenberg affinity. The two faces agree at $\beta_{\text{mem}}=1$ (Markovian limit); for non-Markovian (Caputo-memory) substrates the orbit-affinity face is canonical.

**Saturation.** In sustained NESS, saturated gain clamps to loss: $G_{sat} = L$. Chit measures the *unsaturated* excess — headroom above threshold, not operating point.

**Threshold behaviour.** chit $\gg 0 \Rightarrow c$; chit $\to 0^+ \Rightarrow s$ (visible strain, Schawlow–Townes broadening, aging-FDR signature); chit $< 0 \Rightarrow r$.
Limit-point status. chit = 0 is a critical limit, not an attainable operating state. Substrates approach it asymptotically from either side; the s-regime is a finite window around the limit, never the limit itself. s-window width: drive-axis substrates carry irreducible thermodynamic floor (kT/q); damping-axis vanishes in deterministic limit (F-003-rlc Q=0.5 zero).

## Fraying sequence

Load monotonically reduces the chit. Sequence under continuous environmental load (demand-load reduces $G_0$; decay-load raises $L$):

> Saturated holding (chit $\gg 0$, $c$, resilient) → visible strain (chit $\to 0^+$, $s$) → mode-hopping (chit $\approx 0$, $s$ multistability) → sub-threshold collapse (chit $< 0$, $r$).

Trajectory entropy production reading: anomalous fraying-resistance trajectories are exponentially rare in $|\sigma|$ (detailed fluctuation theorem $P(\sigma)/P(-\sigma) = e^\sigma$). The fraying sequence is the *typical* trajectory, not a worst case.

## gFDR signatures

Coherences are path-dependent NESS; equilibrium FDR fails. The Apparatus reads spontaneous fluctuations $C(\tau)$ and response $\chi(\tau)$. Harada–Sasa: integrated FDR-violation = steady-state entropy production rate $\langle\sigma\rangle$.

**Per-regime invariants** (inherited from v9 §FDR signatures, restated in chit register):

| Regime | Chit | Invariant | Reading |
|---|---|---|---|
| $c$ | $\gg 0$ | $X_c = 0$ | suppression / narrow horizontal locus |
| $s$ | $\to 0^+$ | $\alpha_s$ slope of aging segment | CK ratio |
| $s$ | $\to 0^+$ | $P_s = \lim_\tau C(\tau)/C(0)$ | plateau height |
| $r$ | $< 0$ | $X_r = 1$ | unit-slope FDR |
| $k_{\text{frust}}$ | non-stationary | $N_f$ transient-negative fraction | spin-glass loop signature |

$\alpha_s$ and $P_s$ are the load-bearing cross-substrate observables.

**Surface-code identification.** Distance-3 rotated memory-Z syndrome streams trace clean $s$-aging at sub-threshold operation, placing surface-code QEC in the Cugliandolo–Kurchan universality class. The framework's most direct cross-substrate empirical content; chit reading of the $s \to r$ migration is the Apparatus's primary cross-substrate test.

**Substrate-conditional reading rules** (inherited from v9 §F): Markovian sign caveat ($\gamma$-sign inversion on stiff substrates); detection-event preprocessing for non-local readouts.

## Capacity dynamics

v9 supplies the static structural ceiling $|\Gamma^*| \le \sqrt{2D/(\alpha\,\gamma_{min}\,d_{avg})}$. Character supplies the dynamic conjugate:

$$\sum_{i \in \Gamma^*} L_i \le G_{total}\,\eta(\Gamma^*)$$

with cross-saturation efficiency $\eta(\Gamma^*) \in (0,1]$, $\eta \to 0$ at the $\sqrt{D}$ Hopfield ceiling. Same wall, dynamic side. Violation forces sparsification or sub-threshold phase transition.

**Erlang-B closure.** Standard finite-capacity queueing gives the soft-edge form via Erlang-B blocking probabilities:
$$\eta(\Gamma^*) = 1 - B(c,\rho), \qquad B(c,\rho) = \frac{\rho^c/c!}{\sum_{k=0}^c \rho^k/k!}$$
with $c = \lfloor|\Gamma^*|_{\text{crit}}\rfloor$ and $\rho$ the effective offered load on the mode-slot pool.

*Soft vs hard scope.* For soft-substrate Erlang-B, $\eta = 1 - B(c,c) \in (0,1)$ at $\rho = c$ (finite blocking, smooth crossover); $\eta \to 0$ only as $\rho \to \infty$. Hard-wall substrates (surface code at logical-error onset) replace $B$ by the indicator $\mathbb{1}[|\Gamma^*|\ge c]$ — one error breaks the code; $\eta \to 0$ abruptly at $\rho = c$. The hard/soft split is itself a substrate-class fingerprint.

## Heat-tax tower (vertical thermodynamic ledger)

v9's Compression Axiom contracts informational structure ($\epsilon = \|\mathcal{C}\|_{op} < 1$). Character routes the thermodynamic exhaust:

$$L_{n+1} = L_{n+1}^{(0)} + \alpha_\sigma\langle\sigma_n\rangle + \alpha_\Sigma\langle\Sigma_n\rangle$$

Two substrate-effect axes propagate level-$n$ activity to level $n+1$:

- $\alpha_\sigma\langle\sigma_n\rangle$: heat from level-$n$ flow as ambient noise to level $n+1$.
- $\alpha_\Sigma\langle\Sigma_n\rangle$: active stress from level-$n$ maintenance work as mechanical/informational/structural stress on level $n+1$.

Heat-tax coupling pinned by Landauer: $\alpha_\sigma(\epsilon) = \alpha_{\sigma,0}\,(1-\epsilon)$, where $\alpha_{\sigma,0}$ is a substrate-conditional thermal-conductivity constant. Cumulative tower tax to depth $N$ is $\propto 1-\epsilon^N$. The Complexity Wall is a *cumulative-mass* thermodynamic singularity at $\epsilon \to 1$: per-level Landauer heat vanishes there (no erasure, no cost), while cumulative informational mass $\Phi_{\text{total}} = \Phi^{(0)}/(1-\epsilon)$ diverges; the singularity lives in the cumulative mass, not in per-level conductivity.

**Meta-ledger flow in continuous register.** The heat-tax recursion is the level-to-level map on the space of slow-manifold generators. Construction: at level $n$, Mori–Zwanzig projection (§Universal two-mode kernel) onto the slow manifold yields generator $\mathcal{A}_n = \Pi_{\text{slow}}\mathcal{A}_n^{\text{full}}\Pi_{\text{slow}}$. The heat-tax substitution $L_{n+1} \leftarrow L_{n+1}^{(0)} + \alpha_\sigma\langle\sigma_n\rangle + \alpha_\Sigma\langle\Sigma_n\rangle$ into the level-$(n+1)$ kernel induces $\mathcal{A}_n \mapsto \mathcal{A}_{n+1}$. This is a Wilson–Polchinski-style functional RG on the space of generators; the continuous level-coordinate $\nu$ integrates the running-coupling β-functions across non-integer levels. The compression rate $\epsilon$ is the leading IR linear-stability eigenvalue of $D\mathcal{A}_{n+1}/D\mathcal{A}_n|_{\mathcal{M}_2}$, Landauer-pinned to the substrate's thermal-conductivity coefficient via $\alpha_\sigma(\epsilon) = \alpha_{\sigma,0}(1-\epsilon)$. The slow-manifold projection $\Pi_{\text{slow}}$ is the level-projection operator: it is what v9 §Compression Axiom names abstractly as the conjugating isometry $\phi$ in the Wilson–Kadanoff structural-equivalence statement.

Sustained level-$n+1$ coherence requires $\ln(G_{0,n+1}/L_{n+1}) > 0$. Fraying at level $n$ inflates $L_{n+1}$ via three independent channels:

1. $\alpha_\sigma\langle\sigma_n\rangle$ heat-tax spike (this section).
2. $\alpha_\Sigma\langle\Sigma_n\rangle$ active-stress spike (§Collective hydrodynamics).
3. $r_n$ drop in level-$n$ collective sync, raising $L_{n+1}^{(0)}$ via lost cooperative gain-sharing (§Phase-locking).

Three measurement registers of one queueing-theoretic mechanism: by the Cobham/Kleinrock priority-queue mapping (§Load-handling), all three channels are faces of Cobham wait-time inflation $W_{n+1}=W_0/[(1-u_n)(1-u_{n+1})]$ across tower-level priority classes. The $u\to 1$ queueing singularity is coincident with the $\epsilon\to 1$ Complexity Wall; for rate-distortion-optimal encoding, $u_n = \epsilon_n$ (one of the framework's five leading-order posits; §Load-handling) — the queueing and informational singularities collapse to one parameter. Sub-optimal substrates experience $r$-regime collapse via $u\to 1$ *before* reaching the informational Wall ($\epsilon\to 1$); the overhead $\Delta_n = u_n - \epsilon_n \ge 0$ is a substrate-class fingerprint. **Sub-optimal substrates die thermodynamically before they die informationally** — the four-aspect Wall is a single parameter only at the optimal limit.

**Channels 2 and 3 share $r$ as driver.** Toner–Tu gives active-stress correction $f(r) = Cr^2$, so the active-stress channel scales as $1+Cr^2$ in level-$n$ sync; the cooperative-gain channel is triggered by $r$-drop. The substrate-class active-coupling $C$ (sign: contractile $>0$, extensile $<0$, isotropic $\approx 0$) determines the balance. Three channels remain independent failure paths but two share $r$ as a common driver in opposing directions.

## Operators in continuous register

v9's discrete operators have continuous-traversal shadows.

**$C_{\text{Character}}$ (merge).** Adiabatic deformation from $\gamma_{AB} \approx 0$ (decoupled) to $\gamma_{AB} \ll 0$ (cooperative) while sustaining NESS. Adiabaticity bound: deformation rate slow vs $L$. Failure mode: forced non-adiabatic merge spikes $\sigma$, drops one or both modes sub-threshold.

Information-geometric reading: merge succeeds iff a Fisher-information geodesic from $\gamma_{AB} \approx 0$ to $\gamma_{AB} \ll 0$ stays on the above-threshold manifold (does not exit through chit-zero). Adiabaticity bound = geodesic-tangent constraint.

Discrete shadow recovers v9 Theorem 9 as the sharp-threshold limit: $\Delta_C(A,B) = 1$ iff $\gamma_{AB} > 0 \land D < \gamma_{AB}$.

**$R_{\text{Character}}$ (sever).** Quench trajectory: choke $G_0$ (demand-load) or open mode to bath ($L\uparrow$, decay-load). Native edge dissolution — $\gamma_{AB}\rho_A\rho_B$ vanishes as $\rho_A \to 0$, no separate graph-edit. Continuous dissipation registers as a $\sigma$ spike during collapse; v9 Landauer bound is the asymptotic discrete limit.

## Universal two-mode kernel

$$\frac{\partial \rho_A}{\partial t} = (G_{0,A} - L_A)\rho_A - \gamma_{AB}\,\rho_A\rho_B + \mathcal{D}[\rho_A,\rho_B;\gamma_{AB}]$$

(symmetric for $\rho_B$; sign convention: $\gamma_{AB}<0$ contributes positively to $\partial_t \rho_A$.) The $\mathcal{D}$-kernel admits three increasingly general closures.

*Lamb stationary closure.* Gain renormalisation $G_{0,A}^{\text{eff}} = G_{0,A}/(1+\sum_{j\ne A}\rho_j/\rho_{\text{sat}})$ — Lamb multi-mode laser saturation — absorbs ambient bath occupancy in the two-mode reduction.

*Dynamic bath inversion.* Non-stationary bath: $B(t)\in[0,1]$ promoted to dynamical coordinate; Mori–Zwanzig projection-out gives non-Markovian history integral; fast-bath limit $\gamma_B\to\infty$ recovers Lamb stationary form. $\gamma_B^{-1}$ identifies as bath-server service time in the §Load-handling Cobham mapping.

*Caputo fractional memory.* For glassy / $s$-regime aging substrates: Mittag-Leffler kernel $\Gamma_{AB}(\tau) = \Gamma_0\,E_{\beta_{\text{mem}}}(-(\tau/\tau_c)^{\beta_{\text{mem}}})$ with Caputo exponent $\beta_{\text{mem}}\in(0,1]$. $\beta_{\text{mem}}=1$ gives exponential memory ($c$-regime); $\beta_{\text{mem}}<1$ gives power-law decay (glassy / $s$-regime aging substrates).

**Three-way identity (substrate-class conditional).** Under the *common-exponent substrate-class condition* — the substrate's slow-resource memory kernel and load-arrival process share a single anomalous-diffusion exponent — the CK $s$-regime aging-diagonal slope $\alpha_s$, the Caputo memory exponent $\beta_{\text{mem}}$, and the anomalous heavy-traffic queueing exponent are *the same parameter* measured in three registers:
$$\alpha_s = \beta_{\text{mem}} = \text{anomalous heavy-traffic exponent}.$$
The identity composes Pottier (non-Markovian FDR identifying Caputo $\beta_{\text{mem}}$ with the aging slope, presupposing the memory kernel governing slow-resource dynamics is Caputo $\tau^{-\beta_{\text{mem}}}$) with Norros (fractional-Brownian heavy-traffic generalises $1/(1-\rho)$ to $1/(1-\rho)^{\beta_{\text{mem}}}$, presupposing self-similar arrival process). The two registers concern distinct substrate-side processes (memory kernel vs arrival process); the identity holds only when both are governed by a common Hurst-class index. Substrate classes where the FDR exponent and the queueing-tail exponent are measured to differ falsify the condition.

**Composite catalogue recovered as kernel attractors.** Sweeping $\gamma_{AB}$ as control parameter:

| Regime | $\gamma_{AB}$ | Phase relationship | v9 row |
|---|---|---|---|
| $c$–$c$ aligned | $\ll 0$ | in-phase locked | Hebbian / force chain |
| $c$–$s$ mentor | $< 0$, asymmetric | driven entrainment, **non-reciprocal** in substrate, formally a priority queue | pilot-light / synaptic tagging |
| $c$–$c$ orthogonal | $\approx 0$ | unlocked / phase drift | independent memory |
| $c$–$c$ opposed (lock) | $> 0$, $K > \Delta\omega$ | anti-phase locked | competing hypotheses (sustained) |
| $c$–$c$ opposed (split) | $> 0$, $K < \Delta\omega$ | competitive desynchronisation (pitchfork) | Lotka–Volterra dropout |
| $k_{\text{frust}}$ | $N \ge 3$ obstructive | frustrated sync | gridlock / UNSAT |

Multi-mode pattern selection for $N \ge 3$ admits chimera states (§Phase-locking) and is fully closed via four channels (§Framework primitives consolidation).

## Topological drain $k_{\text{frust}}$

$N \ge 3$ closed chain with obstructive $\gamma$ topology admits no *equilibrium* (detailed-balance) steady state: its stationary state is irreducibly a NESS carrying a drive-independent, topologically-forced Schnakenberg cycle current. **This broken-detailed-balance circulation — not deterministic fixed-point non-existence — is the defining invariant** (§Framework-primitives §8 triality's underlying fact). The deterministic flow realises it in two sub-regimes by the sign of the relaxation eigenvalue's real part: a *stable circulating focus* (Re $<0$, complex spectrum — spirals into a NESS that still circulates) or a *repelling focus + attracting limit cycle* (Re $>0$; §Stability). Cross-saturation conflict is internal to the kernel mathematics; drive-independent. Recovers v9's "not resolvable by $D$" assertion as kernel consequence rather than separate axiom.

**Six-register reading of one phenomenon:**

1. Cyclic pumping–fraying trajectory (this section): some mode's chit goes negative each cycle; time-averaged $G$ diverges.
2. Hopf-unstable spiral with attracting limit cycle (§Stability): cooperative fixed point repels; system on attracting orbit.
3. Frustrated sync (§Phase-locking): pairwise lock-attempts broken by topological obstruction, re-form around different weakest mode.
4. Schnakenberg cycle current with divergent action (§Thermodynamic and informational accounting): $J_C\ln(\prod_+k/\prod_-k)$ forced regardless of $D$.
5. Non-existence of a *gradient* Lyapunov $\mathcal{V}$ (§Active modulation): the flow has an irreducible circulating part — a stability-Lyapunov may exist (a stable focus has one), but no free-energy whose gradient *is* the dynamics (detailed balance is broken).
6. Priority-queue inversion (§Load-handling): asymmetric load absorption with no symmetric back-flow.

These six register-readings collapse at the topology level to one fact (the stationary state is irreducibly a circulating NESS — broken detailed balance); see §Framework primitives consolidation §8 for the topological triality.

gFDR signature: transient negative response $N_f$ in loop-level apparatus.

## Stability and attractor structure

The §Bridge eigenvalue's real part sets the regime; its full complex structure governs perturbation-recovery. Above threshold, single-mode coherences are 2D in local linearisation (field × population) — Jacobian has a complex-conjugate pair $(\gamma_{RO}, \omega_{RO})$, the relaxation-oscillation regime.

**Per-regime damping signatures and attractor types.**

| Regime | Damping | Recovery profile | Attractor |
|---|---|---|---|
| $c$ | $\zeta < 1$ underdamped | decaying oscillation at $\omega_{RO}$ | stable spiral / focus |
| $s$ | $\zeta \to 1$ critical | algebraic settling (= CK aging diagonal long-time tail) | centre manifold at threshold |
| $r$ | $\zeta > 1$ overdamped | bath relaxation; no oscillator | stable origin |
| $k_{\text{frust}}$ | repelling cooperative focus | cyclic, no return | attracting limit cycle |

*$k_{\text{frust}}$ sub-regimes.* The repelling-focus + limit-cycle row is the Re$\,>0$ case; a frustrated loop whose amplitude is saturation-clamped is the Re$\,<0$ case — a *stable* focus with **complex** eigenvalues that still circulates (a NESS, $J\neq0$). Both are $k_{\text{frust}}$; the complex spectrum (irreducible rotation), not the sign of Re, is the signature (§Topological drain).

$Q = \omega_{RO}/(2\gamma_{RO})$: cycles-of-headroom observable, conjugate to chit. Chit reads *whether* threshold is cleared; $Q$ reads *how many cycles* of natural oscillation that headroom buys.

$$\omega_{RO} = \sqrt{2\gamma_s L\,(e^{\text{chit}}-1)},\qquad Q = \sqrt{2L(e^{\text{chit}}-1)/\gamma_s}$$

$\gamma_s$ is the substrate's slow-resource turnover rate (population decay in lasers; syndrome decoding in QEC; plasticity in neural; carrying-capacity adjustment in ecological; reinforcement-extinction in behavioural). Both vanish at threshold (chit $\to 0^+$); $Q$ grows as $e^{\text{chit}/2}/\sqrt{\gamma_s}$ deep in $c$.

**Active/passive probe = on/off resonance.** Probes within $\gamma_{RO}$ of $\omega_{RO}$ are active (Q-amplified); off-resonance probes are passive baseline. Boundary linewidth = $\gamma_{RO}$.

**Recovery profile is a third probe-class signature** alongside spontaneous FDR (steady-state stochastic) and load-driven fraying (sustained-load trajectory).

**Slow-manifold reading of $s$-aging.** At threshold, leading eigenvalue's real part vanishes; dynamics collapse onto centre manifold. CK aging signature *is* the slow-manifold trace: $P_s$ = slow-manifold fixed-point amplitude; $\alpha_s$ = slow eigenvalue's residual scaling against saturating gain. The same projection $\Pi_{\text{slow}}$ that isolates the $s$-regime centre manifold is the level-projection operator for the meta-ledger ascent (§Heat-tax tower) — the slow-manifold reading of $s$-aging and the meta-ledger flow's compression operator are the same projection at two scales (within-level dynamics vs. level-to-level transport).

**Bifurcation summary** (codimension-1 explicit in framework):

- Transcritical at chit $= 0$ (laser threshold; $c \leftrightarrow r$).
- Pitchfork at $\gamma_{AB} = \gamma_c$ (cooperative–competitive boundary).
- Hopf-unstable at obstructive $\gamma$-chain onset ($k_{\text{frust}}$).

Codimension-2 closures via standard normal-form theory (Bogdanov–Takens, cusp, Bautin, fold-Hopf).

**Wall-forces-NRT chain.** As $u_n\to 1^-$ at the Complexity Wall (§Load-handling Cobham closure), each tower-level ascent $n\to n+1$ undergoes a delay-induced Hopf bifurcation via the DDE characteristic equation. With $N\ge 3$ ascents Hopf-bifurcating, the 3-torus required for Newhouse–Ruelle–Takens chaos populates automatically. **Meta-ledger chaos post-Wall is forced, not merely allowed**, contingent on (i) the substrate not collapsing into $r$-regime before the bifurcation sequence completes, and (ii) the three Cobham–Haken bridge conditions of §Load-handling holding approximately. Three-closure stack: Cobham wait formula → DDE Hopf per ascent → NRT chaos at $N\ge 3$.

## Phase-locking and collective coherence

For two coherences with detuning $\Delta\omega$ and effective phase coupling
$$K_{AB} = -\gamma_{AB}\sqrt{\rho_A\rho_B}/[\rho_{\text{sat}}\sqrt{1+4Q^2}]$$
(phase-reduction of the two-mode kernel; $Q\gg 1$ recovers standard $1/(2Q)$ Kuramoto suppression, $Q\lesssim 1$ deep-cooperative direct lock): lock if $K_{AB} \gtrsim \Delta\omega$. Arnold-tongue structure in $(\Delta\omega, K_{AB})$ follows.

**Order parameter.** Kuramoto $r = |(1/N)\sum_n e^{i\phi_n}|$: collective coherence amplitude, independent of per-mode chit.

**Two independent phase transitions and observables.** Two second-order transitions: chit-zero amplitude onset and Kuramoto $K_c$ phase onset. Two order parameters at population level: per-mode chit and collective $r$. Neither implies the other.

**Sync feedback to heat-tax tower.** $L_{n+1}^{(0)}$ depends on level-$n$ sync: high $r_n$ reduces $L_{n+1}^{(0)}$ (cooperative gain-sharing); low $r_n$ raises it. Third channel of upward fraying propagation (§Heat-tax tower).

**Chimera states.** Partially-synchronised regimes — coexisting synchronised $c$-regime and incoherent $r$-regime sub-populations at fixed substrate parameters — are generic in heterogeneous-coupling kernels. Closed via Sun–Bollt–Nishikawa generalised MSF for heterogeneous networks. Spectral splits of the generalised Laplacian $\mathcal{L}_{ij} = -K_{ij}\cos(\phi_j^*-\phi_i^*)$ are the mathematical signature of chimera-admitting kernels.

*SBN mild-heterogeneity scope.* Sun–Bollt–Nishikawa is a perturbative extension of Pecora–Carroll for nearly-identical systems. Application to generic Character kernels with mild heterogeneity (per-mode chit and $\gamma_{s,i}$ spreads small compared to their means) is direct; application to strongly-heterogeneous substrate classes is a *posited extension* — the sign of the leading transversal eigenvalue (the spectral test's qualitative answer) is expected to be robust, but quantitative eigenvalue gaps require an independent strong-heterogeneity correction. Quantitative use in the strong-heterogeneity regime carries a substrate-class falsifier.

## Thermodynamic and informational accounting

Stochastic thermodynamics + information theory consolidate into a single dual ledger.

**Trajectory entropy production.** Detailed fluctuation theorem $P(\sigma)/P(-\sigma) = e^\sigma$ (Crooks). Anomalous fraying-resistance trajectories exponentially rare in $|\sigma|$.

**TUR.** $\text{Var}(J)/\langle J\rangle^2 \ge 2k_B/\langle\sigma\rangle$ (Barato–Seifert). Maintenance current precision bounded by entropy production.

**Schnakenberg cycle decomposition.** $\langle\sigma\rangle = \sum_C J_C\ln(\prod_+k/\prod_-k)$ on the master-equation embedding ($\gamma_{ij}$ are kernel parameters, not transition rates — affinity is the log-ratio of compound rates around the embedded cycle). For limit-cycle attractors the continuous-traversal form is $\sigma_{\text{frust}} = J_{ss}\oint v(\theta)/D(\theta)\,d\theta$ on the orbit ring. $k_{\text{frust}}$ drive-independence is the topologically-forced cycle current.

**Predictive information.** $I_{\text{pred}} = I(\text{past};\text{future})$. Third independent coherence observable alongside chit and $Q$.

**Active-probe channel capacity.** $C \sim B\log_2(1+S/N)$ with $B \sim \gamma_{RO}$, $S/N \sim Q$. Informational dual of TUR; together they are two faces of the observability bound.

**Information geometry.** Fisher metric on $(G_0, L, \gamma_{AB},\ldots)$ space. Geodesics = max-likelihood deformation paths; $C_{\text{Character}}$ adiabatic merge condition becomes "geodesic stays on above-threshold manifold." The drain $k_{\text{frust}}$ excises a region from the parameter manifold (no $P_{ss}$ exists), making it a homotopy obstruction — one face of the §Framework primitives consolidation §8 topological triality.

**Rate-distortion / Compression Axiom.** $\mathcal{C}$ is lossy compression on trail-class space; $\epsilon$ is its compression rate. $\Phi_{total} = \Phi^{(0)}/(1-\epsilon)$ is the standard rate-distortion geometric series.

**Extended second law** (Sagawa–Ueda). $\langle\sigma\rangle \ge -\Delta I$. Bit-readout holdings sustain at lower chit by paying via mutual information.

**Bit/Chit dual ledger.**

| Axis | Thermodynamic | Informational |
|---|---|---|
| Per-event | chit $= \ln(G_0/L)$ | bit $= \ln 2$ |
| Per-rate | $\langle\sigma\rangle$ (Harada–Sasa) | $I_{\text{pred}}$ |
| Precision | TUR | Channel capacity |
| Compression | Heat-tax tower | Rate-distortion tower |
| Coupling | $\langle\sigma\rangle \ge -\Delta I$ | (same bound, dual reading) |

**Bijective duality closure (Still bound).** Under the Still thermodynamic prediction bound,
$$\langle\sigma\rangle - \langle\sigma\rangle_{\min} \ge \gamma_s\,\chi$$
with $\chi = C_\mu - I_{\text{pred}}$ (cryptic order; $C_\mu$ structural complexity of the Crutchfield $\varepsilon$-machine), with equality at the rate-distortion-optimal limit. Sub-optimal substrates split the ledger by $\gamma_s\chi$ — the *same* gap parameter as §Active modulation cryptic order and §Load-handling encoding overhead $\Delta_n = u_n - \epsilon_n$. **Optimal-encoding triality**: $\chi = \Delta_n = \langle\sigma\rangle_{\text{excess}}/\gamma_s$ — one quantity, three measurement protocols.

## Pattern formation and self-organisation

**Holdings as dissipative structures.** The chit-zero crossing IS the dissipative-structure formation transition (Prigogine). Substrate examples (laser, glass, surface code, behavioural) are substrate-conditional instances of the same threshold mathematics.

**Chit as order parameter** (Haken's slaving). Above threshold, fast micro-modes adiabatically follow chit's evolution; the §Stability centre-manifold reduction is the slaving relation read backward.

**SOC self-tuning.** Under feedback-coupled maintenance dynamics, chit-zero is an *attractor in parameter space*, not merely a regime boundary. Predicted $s$-regime signatures:

1. Power-law avalanche statistics $P(s) \sim s^{-\tau}$, $\tau \approx 3/2$ (mean-field).
2. 1/f spectral tail (consistent with the existing CK aging diagonal).
3. Spatiotemporal scale invariance in multi-mode fraying clusters.

**Galton–Watson at two registers.** Fraying propagation maps to a Galton–Watson branching process with branching ratio
$$\mu = G_0/L = e^{\text{chit}}.$$
At chit $\to 0^+$, $\mu \to 1^+$: critical branching, $P(s) \sim s^{-3/2}$ in mean field. One of the five leading-order posits. Two registers, both reaching criticality at framework-primitive boundaries:

- *Horizontal/spatial:* $\mu = e^{\text{chit}} \to 1$ at chit $= 0$ (within-level).
- *Vertical/meta-ledger:* tower branching ratio $\to 1$ at $\epsilon = 1$ (across-level).

*Iid-assumption scope.* Horizontal register satisfies classical Galton–Watson iid in the mean-field reading. Vertical register has correlated offspring distributions across levels (shared $G_{\text{total}}$, three coupled §Heat-tax channels) — a correlated-offspring branching-process extension (multitype Galton–Watson with bounded cross-type covariance). Criticality-at-unity survives the multitype extension; the mean-field $\tau = 3/2$ at the vertical register is conditional on cross-level correlation remaining weak enough that single-type universality is retained. Substrate-specific cross-level coupling strength is a falsifier.

**Four-aspect Complexity Wall.** At $\epsilon = 1$, four critical signatures coincide:

- *Thermodynamic*: cumulative-mass geometric series fails to converge (§Heat-tax tower).
- *Dynamical*: meta-ledger flow bifurcation in trail-class space (§Stability).
- *Informational*: lossy compression rate hits unity (§Thermodynamic and informational accounting).
- *SOC-critical*: fraying branching ratio reaches unity (this section).

The four-aspects-as-register-faces-of-a-single-unifying-parameter $\beta_{\text{mem}}\to 0$ reading rests on the Wall-coupling posit below. Without that posit, the four aspects remain coincident at $\epsilon = 1$ but their *common scaling parameter* across registers is not guaranteed. The §Load-handling spatial expression (traffic-driven → frozen-topological transition; $\ell_c(\beta_{\text{mem}})$) is the spatial signature of the same posited parameter, not a fifth independent aspect.

**Wall-coupling posit.** Leading-order linear coupling:
$$\beta_{\text{mem}} \approx 1 - \epsilon.$$
Simplest functional form satisfying both endpoints: $\epsilon\to 0 \Rightarrow \beta_{\text{mem}}\to 1$ (Markovian); $\epsilon\to 1 \Rightarrow \beta_{\text{mem}}\to 0$ (extreme aging). One of the five leading-order posits; substrate-thermodynamic derivation of the exact functional form is the residual open beneath the falsifier.

**Regime ontology recast.** $s$-regime is the *generic* attractor of feedback-coupled NESS, not the unstable middle of a triplet:

- $c$-regime: over-provisioned holdings (chit pulled deep above threshold by external constraint).
- $s$-regime: self-organised natural operating point of feedback-coupled holdings.
- $r$-regime: post-collapse holdings.

This explains the empirical over-representation of $s$-regime in observed substrates: feedback-coupled NESS systems land there because the parameter-space attractor pulls them.

**Hierarchy of dissipative structures.** §Heat-tax tower is hierarchical pattern formation: each ascent is a new dissipative-structure transition with its own chit-as-order-parameter and its own slaving relation. §Stability per-level attractor structure + SOC per-level self-tuning + heat-tax across-levels = three aspects of one nested formation.

**Turing-class spatial pattern formation.** Extending §9 kernel with spatial diffusion gives reaction–diffusion system; Turing instability requires three substrate-conditional conditions: (i) non-reciprocity $\gamma_{AB}\gamma_{BA}<0$ (mentor row), (ii) substrate-native autocatalysis $\gamma_{ii}<0$ (the bare §9 kernel has $J_{AA}=0$ at coexistence), (iii) differential diffusion $D_B \gg D_A$. Multi-mode pattern selection ($N\ge 3$) is fully closed at framework level via four channels (§Framework primitives consolidation).

## Active modulation and internal models

**Plant–controller decomposition.** A holding is a closed loop. *Plant*: substrate's natural dynamics (§Bridge open-loop eigenvalue). *Controller*: maintenance feedback adjusting $G_0$ based on observed plant state. Closed-loop eigenvalue is shifted by controller transfer function, generically toward stability.

The §Stability active probe, §Pattern-formation SOC feedback, and §Pattern-formation slaving relation are three aspects of one closed-loop structure (§Framework primitives consolidation §11): the holding is a controller actively shaping its plant.

**Lyapunov stability.** Chit is a candidate single-mode Lyapunov function. Non-frustrated multi-mode topologies admit the relative-entropy Lyapunov $\mathcal{V} = \sum_i[x_i - x_i^* - x_i^*\ln(x_i/x_i^*)]$ on gauged amplitudes (Harary structural-balance gauge), with $d\mathcal{V}/dt = -\delta x^T \gamma\,\delta x \le 0$ when the gauged $\gamma$ is positive semi-definite. (Calligraphic $\mathcal{V}$ distinguishes from Rescorla–Wagner associative-strength $V$ below.) $k_{\text{frust}}$ admits *no* Lyapunov — non-existence is the dynamical-systems content of "no stationary fixed point" (§Topological drain).

**Weighted Lyapunov for frustration-free-but-not-PSD topologies.** For Volterra–Lyapunov stable matrices that are not PSD, a strictly positive diagonal weight matrix $W = \text{diag}(w_i)$ exists such that $W\gamma + \gamma^T W$ is PSD. Weighted form: $\mathcal{V} = \sum_i w_i[x_i - x_i^* - x_i^*\ln(x_i/x_i^*)]$. $W = I$ recovers PSD.

**Substrate-class auto-tuning posit.** Substrates natively tune $\gamma_{s,i}$ to satisfy diagonal stability via inverse-form
$$W = \text{diag}(\gamma_{\text{ref}}/\gamma_{s,i})$$
— inverse-scaling, slow-mode-dominant weighting. One of the five leading-order posits.

**Internal model principle** (Francis–Wonham). A controller robust to a class of substrate disturbances must internally encode the generating structure of those disturbances. Substrate-conditional instances: surface-code decoder = internal model of substrate's error process; glass cage = encoding of bath schedule's slow modes; behavioural pattern = encoding of reinforcement schedule's structure. Coherence is a substrate's local accumulation of model.

**Behavioural substrate via continuous-time Rescorla–Wagner.** With associative strength $V(t)$, maximum conditioning $\lambda$, and learning rate $\kappa_{RW}$:
$$\dot V = \kappa_{RW}(\lambda - V).$$
Mappings: $V\to\rho$; $\kappa_{RW}\to\gamma_s$; $\lambda$ conjugate to maintenance budget $G_0$; extinction ($\lambda\to 0$) $=$ $R_{\text{Character}}$ quench trajectory. Variable-ratio reinforcement schedules predicted to instance Caputo $\beta_{\text{mem}}<1$ in extinction tails — sixth cross-register connection in the Caputo chain.

**Four-axis coherence observable.**

| Axis | Reading | Source |
|---|---|---|
| chit | whether threshold is cleared | §Chit unit |
| $Q$ | cycles of headroom | §Stability |
| $I_{\text{pred}}$ | predictability given history | §Thermodynamic and informational accounting |
| Internal-model richness | how rich a model of disturbance is encoded | this section |

Independent axes. Internal-model richness may explain substrate-class variance in $s$-regime clustering: rich-model substrates cluster tighter near critical, weak-model substrates drift further.

**Structural complexity and cryptic order.** The structural-complexity reading $C_\mu = H(\mathcal{S})$ on Crutchfield $\varepsilon$-machine causal states is mathematically independent of $I_{\text{pred}}$ for hidden-state processes, with $C_\mu \ge I_{\text{pred}}$ and **cryptic order** $\chi = C_\mu - I_{\text{pred}} \ge 0$ as the gap. The cryptic order identifies with the §Load-handling encoding overhead $\Delta_n = u_n - \epsilon_n$ at the optimal-encoding limit:
$$\chi = \Delta_n \qquad \text{(at the optimal-encoding limit)}.$$
One of the five leading-order posits.

*Stationarity-gap reading.* $C_\mu$ is derived for stationary processes; the framework's load-bearing positive instance (surface-code $s\to r$ CK aging) is non-stationary. Two compatible reconciliations: (i) *trajectory-ensemble local stationarity* — at fixed waiting-time $t_w$, the time-translated ensemble is locally stationary, $C_\mu(t_w)$ and $I_{\text{pred}}(t_w)$ are well-defined, $\chi(t_w)$ is the slowly-varying gap parameter along the aging diagonal; (ii) *time-varying $\varepsilon$-machines* — non-stationary computational-mechanics extensions give the same $C_\mu \ge I_{\text{pred}}$ inequality at each instantaneous causal-state partition. Substrate classes whose aging is slow compared to the predictive-information integration timescale use (i) by default; substrates with rapid aging inherit (ii).

## Collective hydrodynamics

**Holdings as active-matter units.** Self-propulsion = per-coherence maintenance dynamics. Alignment = cooperative $\gamma_{AB}$. Density = local count of coexisting coherences.

**Toner–Tu hydrodynamics.** For populations with continuum spatial extent, slow dynamics of density $n(x,t)$ and orientational order $\mathbf{p}(x,t)$ satisfy Toner–Tu equations. The flocking transition $|\mathbf{p}|=0\to|\mathbf{p}|>0$ is the population-level analog of the chit-zero threshold.

*Toner–Tu substrate-class scope.* Direct application for active-matter substrates with intrinsic self-propulsion and aligning interaction (active colloids, motile cells, robotic swarms, flocking animals). Application as the "active-matter overlay" channel for substrate classes lacking intrinsic self-propulsion (surface codes, neural ensembles, glassy substrates, behavioural substrates) is a *posited extension*; the active-stress / swim-pressure formulae below should be read as the framework's leading-order proposal for an effective stress tensor, with substrate-thermodynamic derivation of effective $v_0$, $\tau_R$ a substrate-class residual.

**Active stress and §Heat-tax tower extension.** Holdings impose more than heat on coarse-grained manifolds: mechanical, informational, structural stress. Substrate-class fingerprint at hydrodynamic level: $\alpha_\Sigma/\alpha_\sigma \sim v_0^2\,\tau_R/D_{\text{trans}}$ (swim-pressure ratio; alignment-independent, MIPS-compatible, survives $r\to 0$).

**Green–Kubo identification of $\tau_R$.** Substrate-neutral form: $\tau_R = \int_0^\infty \langle\mathbf{u}(t)\cdot\mathbf{u}(0)\rangle\,dt$, where $\mathbf{u}(t)$ is the unit-vector direction of the holding's active maintenance-work application in its state space. Same mathematical object across substrates. For non-Markovian substrates with Caputo $\beta_{\text{mem}}<1$, $\tau_R$ formally diverges (Green-Kubo integrand $\sim t^{-\beta_{\text{mem}}}$); finite-size cutoffs regularise.

**$f(r)$ active-stress closure.** Toner–Tu active pressure: $P_{\text{active}} = (n\,v_0^2\,\tau_R/d)[1 + Cr^2]$ with active-coupling constant $C = \zeta_0 d/(v_0^2\tau_R)$. Sign of $C$: contractile $>0$, extensile $<0$, isotropic $\approx 0$. Drives the §Heat-tax tower r-coupling between channels 2 and 3.

**Giant number fluctuations.** Active populations exhibit $\delta N \sim N^a$ with $a > 1/2$ (canonical $a = 1$). TUR may saturate or loosen in this regime; substrate-class diagnostic.

**Non-reciprocal coupling.** v9 §Falloff already flags as extension axis. The §Universal kernel admits $\gamma_{AB}\ne\gamma_{BA}$; coexistence Jacobian has $\operatorname{Tr}=0$, $\det = -\gamma_{AB}\gamma_{BA}\rho_A^*\rho_B^*$, giving three regimes by sign of $\gamma_{AB}\gamma_{BA}$: positive ⇒ saddle (runaway / competitive exclusion); negative ⇒ centre promoted to stable limit cycle of frequency $\omega_{\text{pq}} \approx \sqrt{|\gamma_{AB}\gamma_{BA}|\rho_A^*\rho_B^*}$ under finite-$\mathcal{D}$ (mentor row priority-queue oscillation); zero ⇒ exceptional point. Spatially extended: traveling waves at velocity $v\sim\sqrt{D_{\text{diff}}|\gamma_{AB}\gamma_{BA}|}$. The §Universal kernel mentor row is *actually* non-reciprocal in substrate dynamics; the symmetric-kernel formal expression is a simplification.

**MIPS** (motility-induced phase separation). Pure repulsive interactions with self-propulsion produce phase separation. New clustering mechanism not in §Universal kernel: clustering at $\gamma_{AB} \ge 0$ via self-propulsion-induced density fluctuations alone. Substrate instancing: open.

## Load-handling and capacity dynamics

**Holdings as queues.** Mapping: $\lambda$ arrival rate of perturbations, $\mu$ service rate ($\sim G_0$), utilisation $\rho = \lambda/\mu$. Chit dual to utilisation at simplest mapping: $\text{chit} = -\ln\rho$.

| Regime | Chit | $\rho$ | Queueing state |
|---|---|---|---|
| $c$ | $\gg 0$ | $\ll 1$ | stable, low-traffic |
| $s$ | $\to 0^+$ | $\to 1^-$ | heavy traffic, critical fluctuations |
| $r$ | $< 0$ | $> 1$ | unstable, queue blowup |

**Heavy-traffic = $s$-aging.** Kingman's $\langle Q\rangle \sim 1/(1-\rho)$ heavy-traffic limit IS the §gFDR $s$-aging signature in queueing register; CK exponent $\alpha_s$ has a heavy-traffic queue-length analog. Coincides for Markovian substrates; diverges for non-Markovian — divergence pattern is a substrate-class diagnostic.

**Little's law.** $\langle Q\rangle = \lambda\langle W\rangle$. Framework's first explicit ⟨amplitude⟩ × ⟨rate⟩ × ⟨timescale⟩ relation at fixed operating point.

**Jackson-network special case.** For Markov–Poisson substrates: product-form steady state $P(\mathbf{Q}) = \prod_i P_i(Q_i)$ with Burke departure-process structure. Tractable explicit-solution regime.

**Multiclass priority and the mentor row.** §Universal mentor row is structurally a priority queue (Kelly). The §Universal mentor row + §Collective non-reciprocal coupling + §Load-handling priority queue are three readings of one substrate-deep asymmetry.

**Cobham priority-queue mapping.** With shared maintenance budget pool $G_{\text{total}}$ as server, tower levels $n$ as priority classes ranked by Haken's slaving, arrival rates $\lambda_n$ as fraying-event frequencies, service times $\tau_n = 1/\gamma_{s,n}$, per-level utilisation $\rho_n = \lambda_n\tau_n$, cumulative utilisation $u_n = \sum_{i=0}^n \rho_i$. Cobham expected wait for class $n+1$:
$$W_{n+1} = W_0/[(1-u_n)(1-u_{n+1})], \qquad W_0 = \tfrac{1}{2}\sum_i \lambda_i\langle\tau_i^2\rangle.$$
Wait diverges at $u \to 1^-$, coincident with the §Heat-tax thermodynamic singularity at $\epsilon \to 1^-$.

*The Cobham–Haken bridge.* The Theorem maps two distinct mathematical structures: Haken's slaving (centre-manifold reduction by natural-timescale separation) and Cobham's wait formula (non-preemptive priority-queue identity with Poisson arrivals at a single server pool). The composition is interpretive, requiring three substrate-side conditions:

1. **Poisson arrivals at the tower level.** Fraying events arrive as memoryless Poisson with rate $\lambda_n$. Substrates with heavy-tailed inter-arrival times (canonically Caputo $\beta_{\text{mem}}<1$) carry fractional-Brownian corrections — leading-order critical structure preserved, divergence exponent changes from $-1$ to $-\beta_{\text{mem}}$.
2. **Single-server-pool interpretation of $G_{\text{total}}$.** Shared maintenance budget serves all priority classes through a single allocation mechanism. Substrates with strict per-level budget partitioning carry a Jackson-network reading instead.
3. **Non-preemptive ranking by timescale.** Slowest macroscopic mode is highest-priority (centre-manifold's adiabatic-following structure). Substrates with internal preemption mechanisms (canonically: top-down attentional override in cognitive substrates) carry preemptive-priority corrections.

Substrate classes satisfying all three inherit the full Cobham closure; those satisfying some inherit corresponding modifications.

**ε↔u optimal-encoding identity.** For a substrate at the rate-distortion bound:
$$u_n = \epsilon_n \qquad (\text{rate-distortion-optimal encoding}).$$
One of the five leading-order posits. Sub-optimal substrates have $u_n > \epsilon_n$ with overhead $\Delta_n \ge 0$; the four-aspect Wall splits — thermodynamic and SOC aspects reach criticality first (via $u \to 1$); the informational aspect ($\epsilon \to 1$) is reached only by optimal-encoding substrates.

**Spatial Jackson-network generalisation.** Kelly's product-form theorem: $P(\mathbf{Q}) = \prod_k P_k(Q_k)$ across patches $k$, each patch independently undergoing Cobham priority dynamics. Non-Markovian Caputo memory violates Kelly's quasi-reversibility; critical interaction length $\ell_c(\beta_{\text{mem}})$ for product-form breakdown depends on Caputo exponent:
$$\ell_c(\beta_{\text{mem}}) = \sqrt{(2D_{\beta_{\text{mem}}}/\Gamma(1+\beta_{\text{mem}}))(W_0/(1-u_n))^{\beta_{\text{mem}}}}.$$

**Traffic-driven → frozen-topological transition.** As $u_n \to 1^-$ alone (Markovian heavy traffic), $\ell_c$ diverges via wait-time inflation. As $\beta_{\text{mem}} \to 0$ at the Wall, $W^{\beta_{\text{mem}}} \to 1$ and $\ell_c \to \sqrt{2D_0}$ with degenerate dimension. The spatial expression of the Complexity Wall is a regime transition from dynamic congestion domains to frozen topological domains. Substrate's intrinsic topology sets the freeze-length. This is the spatial reading of the same Wall-coupling posit governing the §Pattern formation four-aspect Wall, not an independent fifth aspect.

## Framework primitives

The framework's API surface and eleven cross-register identities.

### Five leading-order posits (methodological)

Five framework primitives share an identical four-part shape:

1. simplest functional form placing a framework primitive at its critical / optimal limit;
2. substrate-conditional deviation from that form;
3. falsifier formalised;
4. substrate-thermodynamic derivation as receipts-only residual.

| Posit | Section | Receipts |
|---|---|---|
| $\beta_{\text{mem}} \approx 1-\epsilon$ | §Pattern formation | §9 Wall-coupling |
| $\mu = e^{\text{chit}}$ | §Pattern formation | §18 Galton–Watson |
| $w_i = \gamma_{\text{ref}}/\gamma_{s,i}$ | §Active modulation | §20 auto-tuning |
| $u_n = \epsilon_n$ | §Load-handling | §22 ε↔u |
| $\chi = \Delta_n$ | §Active modulation | §20 cryptic order |

The pattern is the framework's **API surface**: universality fixes exponents (the simple form at the limit); substrates fix amplitudes (deviations from the form). RG language. Each posit is testable; none is derived from substrate thermodynamics.

### Eleven cross-register identities

**1. Caputo memory exponent $\beta_{\text{mem}}$ — seven-register chain of one parameter.**

- Memory-tail $t^{-\beta_{\text{mem}}}$
- $\tau_R$ Green–Kubo divergence
- Swim-pressure fingerprint $\alpha_\Sigma/\alpha_\sigma$ divergence via $\tau_R$
- Spatial Kelly-network product-form breakdown
- Wall-coupling $\beta_{\text{mem}}\approx 1-\epsilon$ posit
- Variable-ratio behavioural-extinction tail
- Spatial traffic-driven → frozen-topological transition via $\ell_c(\beta_{\text{mem}})$

The unifying $s$-regime / Wall-approach control parameter under the Wall-coupling posit. The four-aspect Wall (thermodynamic / dynamical / informational / SOC) is its multiple-register expression — four core register-faces of one parameter under the posit; the spatial expression ($\ell_c$) reads the same parameter spatially, not a fifth independent aspect.

**2. Optimal-encoding triality.** $\chi = \Delta_n = \langle\sigma\rangle_{\text{excess}}/\gamma_s$ — one quantity, three measurement protocols:

- Cryptic order $\chi = C_\mu - I_{\text{pred}}$
- Encoding overhead $\Delta_n = u_n - \epsilon_n$
- Dissipation excess $\langle\sigma\rangle - \langle\sigma\rangle_{\min} = \gamma_s\chi$

Sub-optimal substrates die thermodynamically before they die informationally. The four-aspect Wall is a single parameter only at the optimal limit; sub-optimal substrates split it.

**3. Wall-forces-NRT chain.** Three closures stacking to make meta-ledger chaos *forced* past the Wall:

- Cobham wait $W_{n+1} \to \infty$ at $u_n \to 1^-$, under the Cobham–Haken bridge conditions.
- Generic Hopf per tower-ascent via DDE characteristic equation.
- $N\ge 3$ ascents complete the 3-torus required for NRT chaos.

Substrate-conditional on whether $r$-regime collapse precedes the bifurcation sequence and on the Cobham–Haken bridge conditions holding.

**4. Galton–Watson branching at two registers.** One mean-field universality class instantiated at two framework-primitive boundaries:

- Horizontal/spatial: $\mu = e^{\text{chit}} \to 1$ at chit $= 0$ (within-level; classical iid Galton–Watson).
- Vertical/meta-ledger: tower branching ratio $\to 1$ at $\epsilon = 1$ (across-level; correlated-offspring multitype extension).

Mean-field $\tau = 3/2$ at criticality on both registers; substrate-graph effective dimensionality fixes the empirical exponent. Vertical-register iid extension condition: weak cross-level correlation.

**5. Mentor row's dual face.** One non-reciprocal coupling structure, two morphological manifestations:

- Temporal limit cycle, frequency $\omega_{\text{pq}} \approx \sqrt{|\gamma_{AB}\gamma_{BA}|\rho_A^*\rho_B^*}$.
- Spatial Turing pattern, wavenumber $k_c$ — when also equipped with substrate autocatalysis and differential diffusion.

Substrate spatial structure selects between the two faces.

**6. Three distinct spatial-structure mechanisms.** Distinguishable prerequisites and dynamics:

- Turing reaction–diffusion: requires non-reciprocity + substrate autocatalysis + differential diffusion.
- Kelly queueing-congestion product-form breakdown: requires bandwidth contention; no autocatalysis or differential diffusion needed.
- Frozen-topological at $\beta_{\text{mem}} \to 0$: memory-driven; substrate intrinsic topology sets freeze-length.

Not reducible to each other; substrate may carry one, two, or all three at different scales.

**7. $r$-coupling between heat-tax channels 2 and 3.** Channels 2 ($\alpha_\Sigma\langle\Sigma_n\rangle$, scales as $1+Cr^2$) and 3 ($r$-drop sync degradation) share $r$ as driver in *opposing* directions. Substrate active-coupling $C$ (sign: contractile $>0$ / extensile $<0$ / isotropic $\approx 0$) determines balance.

**8. $k_{\text{frust}}$ topological triality.** Three co-implied measurement protocols, one underlying fact — **the stationary state is irreducibly a NESS: a topologically-forced, drive-independent circulating current (broken detailed balance)**:

- Dynamical: no *equilibrium* (detailed-balance) steady state; the stationary state circulates (the relaxation spectrum is complex). [The earlier "no stationary fixed point" was too strong — a stable circulating focus *is* a fixed point and is genuine $k_{\text{frust}}$; see §Topological drain sub-regimes.]
- Informational-geometric: no Fisher geodesic / scalar potential generates the circulating flux — homotopy obstruction.
- Thermodynamic: drive-independent Schnakenberg cycle current forced by orbit topology.

Identity at the underlying-topology level; substrate-specific measurement signatures differ across registers.

**9. $s$-regime exponent triality** (under common-exponent substrate-class condition). One parameter, three mathematical-discipline measurements:

$$\alpha_s = \beta_{\text{mem}} = \text{anomalous heavy-traffic exponent}$$

- CK aging-diagonal slope $\alpha_s$ (physics; gFDR signature).
- Caputo fractional memory exponent $\beta_{\text{mem}}$ (fractional calculus).
- Heavy-traffic queue-tail anomalous exponent (operations research).

Substrate-class condition: substrate's slow-resource memory kernel and load-arrival process share a single anomalous-diffusion exponent. Distinct from item 1 (chain of *consequences*); this is identity *across measurement protocols*. Both belong.

**10. Four-channel pattern selection architecture.** Multi-mode ($N\ge 3$) pattern selection decomposes into exactly four independent tests, all closed:

- Frustration test (signed-graph sign-product).
- Spectral sync test (Sun–Bollt–Nishikawa generalised MSF; mild-heterogeneity scope, posited extension to strong heterogeneity).
- Non-reciprocity test (Jacobian sign analysis).
- Active-matter overlay (Toner–Tu / MIPS; direct for active-matter substrates, posited extension elsewhere).

The complete operating system for multi-mode emergence; any $N\ge 3$ Character kernel routes through these four tests, with channels 2 and 4 carrying explicit substrate-class scope.

**11. Closed-loop plant-controller unifier.** Three aspects of one closed-loop control structure:

- Active probe (§Stability): on-resonance feedback through relaxation-oscillation loop.
- SOC self-tuning (§Pattern formation): feedback-coupled chit-zero attractor.
- Haken slaving (§Pattern formation): centre-manifold reduction read backward.

The plant–controller decomposition (§Active modulation) is the unifying register; the three are different reading-protocols of the same closed-loop.

## Methodological imperatives

- **Trajectory primacy.** Bounded time-series data of sustained holding, not static point measurements.
- **NESS-by-default.** Detailed-balance breaking is foundational baseline; equilibrium is the degenerate (zero-drive) special case.
- **Reading rules inherit from v9.** Substrate-conditional sign caveats and detection-event preprocessing apply identically.
- **Falsifier discipline.** Each character-specific claim wants its own falsifier statement. Surface-code $s$-aging identification is the load-bearing positive instance; per-claim falsifiers for the rest are owed.
- **API surface, not closed theory.** Five leading-order posits encode the framework's API: each posit places a primitive at its critical limit via the simplest natural form; substrate-thermodynamic derivation of exact functional shapes is the canonical extension mode, not a defect of the present state.

## Open items

Closed-form residuals and structural conjectures both stand at zero — the architectural take lives in §Framework primitives consolidation. The remaining items are **empirical coupling parameters**: framework predictions awaiting substrate contact, with sharp falsifiers and posited functional forms (the five leading-order posits) already established. These are the framework's API where universal theory meets empirical reality, not theoretical gaps.

**Empirical coupling parameters** (predictions awaiting empirical contact; falsifiers formalised in Receipts):

- Surface-code $s \to r$ migration as the gFDR cross-substrate test (§gFDR signatures; primary instance) — falsifier formalised in Receipts §4.
- Habit-extinction as Rescorla–Wagner reference driver — falsifier formalised in Receipts §20 (habit-extinction); variable-ratio schedules predicted to extend the Caputo $\beta_{\text{mem}}$ chain to behavioural substrates.
- Power-law avalanche exponent $\tau \approx 3/2$ on any substrate (§Pattern formation) — Galton–Watson critical-branching mechanism closed via posit $\mu = e^{\text{chit}}$; falsifier in Receipts §18 (avalanche).
- Meta-ledger branching ratio in observed substrates (§Pattern formation) — falsifier in Receipts §18 (branching ratio).
- Strange-attractor / chaotic Character dynamics on any substrate (§Stability) — falsifier in Receipts §14 (strange-attractor instancing).
- MIPS clustering at $\gamma_{AB} \ge 0$ on any substrate (§Collective hydrodynamics) — falsifier in Receipts §21 (MIPS).
- Chimera-state substrate instancing (§Phase-locking) — falsifier in Receipts §15 (chimera).
- TUR-tightness as substrate-class universality observable (§Thermo-info accounting) — falsifier in Receipts §16 (TUR-tightness).
- $I_{\text{pred}}$ scaling with chit, $Q$, internal-model richness across substrate classes (§Thermo-info + §Active modulation) — falsifier in Receipts §17/§20 ($I_{\text{pred}}$ scaling).
- Heavy-traffic exponent vs $\alpha_s$ on Markovian and non-Markovian substrates (§Load-handling) — falsifier in Receipts §22 (heavy-traffic).
- Substrate-class hard-vs-soft capacity walls (§Capacity dynamics) — falsifier in Receipts §5/§22 (hard-vs-soft walls).
- Turing-class spatial pattern formation: three-condition substrate-instance refinement (non-reciprocal mentor row + substrate-native autocatalysis + differential diffusion); falsifier in Receipts §19 (Turing).
- Memory-exponent collapse near Complexity Wall: leading-order coupling $\beta_{\text{mem}}\approx 1-\epsilon$; falsifier in Receipts §9 (memory-exponent coupling).
- Substrate-class auto-tuning to diagonally-stable $W$: inverse-form $W = \text{diag}(\gamma_{\text{ref}}/\gamma_{s,i})$; falsifier in Receipts §20 (auto-tuning).
- Common-exponent substrate-class condition for the $s$-regime exponent triality (§Universal two-mode kernel): substrate slow-resource memory kernel and load-arrival process share a single anomalous-diffusion exponent. Falsifier: substrate classes where the FDR exponent and the queueing-tail exponent are measured to differ.
- Cobham–Haken bridge conditions (§Load-handling): three substrate-side conditions (Poisson tower arrivals, single-server-pool $G_{\text{total}}$, non-preemptive timescale ranking) must hold approximately. Substrate-conditional falsifier per condition.
- Sun–Bollt–Nishikawa strong-heterogeneity extension (§Phase-locking): SBN spectral test sign-robust at mild heterogeneity; quantitative accuracy at strong heterogeneity is a posited extension. Falsifier: substrate classes where SBN spectral predictions and observed sync behaviour disagree quantitatively under strong-heterogeneity conditions.
- Toner–Tu active-matter overlay extension (§Collective hydrodynamics): direct for active-matter substrates; effective $v_0, \tau_R$ derivation a substrate-class residual for substrates lacking intrinsic self-propulsion.
- $\varepsilon$-machine stationarity-gap reading (§Active modulation): trajectory-ensemble local stationarity (default) vs time-varying $\varepsilon$-machines (rapid-aging substrates). Substrate-thermodynamic derivation of the slow-variation criterion is residual.

Two classes of residual live beneath each posit-based item: (i) the *empirical coupling parameter* itself — substrate-specific number or curve to be measured; and (ii) *substrate-thermodynamic derivation of the exact functional form* of the corresponding leading-order posit. Closing (ii) for a substrate class promotes the posit from leading-order universal-form to derived substrate-specific form — the canonical extension mode of the framework's API.
