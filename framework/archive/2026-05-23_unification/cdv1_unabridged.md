# Character Dynamics on Metastable Propositional Algebra v1

## A Continuous-Traversal Theory of Sustained Non-Equilibrium Coherences

> **Status.** Operational source of truth is [`cdv1_compressed.md`](cdv1_compressed.md), the claim-only artefact; on any disagreement of claim content the compressed file wins. This unabridged paper carries the integrative narrative, paper-grade prior-art integration, formal apparatus, and architectural reading guide. Lag-allowance: this file trails the compressed by at most one closure.
>
> **Companions.** [`cdv1_receipts.md`](cdv1_receipts.md) holds line-keyed justifications (each entry: cite, bespoke step, verification, don't-overclaim, open). [`v9_compressed.md`](v9_compressed.md) and [`v9_unabridged.md`](v9_unabridged.md) are the structural-projection counterpart: v9 specifies the discrete operator algebra and coupling-graph topology of trail-class traversal; this paper specifies the driven-dissipative dynamics that traverse it.

## Abstract

We develop the *Character* projection of the Metastable Propositional Algebra (MPA): a substrate-neutral continuous-traversal theory of the driven-dissipative dynamics that sustain non-equilibrium steady states (NESS). Where the structural projection v9 specifies the topology and discrete operator algebra of a coupling graph, Character specifies the physical economics of *being* a coherence on that graph against a bath. The framework rides on a single dimensionless primitive — the **chit**, $\mathrm{chit} = \ln(G_0/L)$, where $G_0$ is the unsaturated maintenance budget and $L$ the spontaneous decay rate — whose logarithmic form is forced by the Crooks rate-ratio entropy production (Crooks, 1999; Seifert, 2012). The chit has three faces: a Markovian per-stochastic-transition reading, a continuous per-orbit reading as the Schnakenberg affinity (Schnakenberg, 1976; Qian, 2001), and a Bit/Chit conjugacy that pairs it bijectively with the Landauer cost of erasure at the rate-distortion-optimal encoding limit (Still, Sivak, Bell, & Crooks, 2012). Three regimes inherit from v9 — committed $c$, suspended $s$, reset $r$ — together with the topological drain $k_{\mathrm{frust}}$. The framework's primary cross-substrate empirical content is the surface-code $s \to r$ migration: distance-3 rotated memory-Z syndrome streams trace a Cugliandolo–Kurchan aging diagonal at sub-threshold operation (Cugliandolo & Kurchan, 1993; Crisanti & Ritort, 2003), placing quantum error correction in the CK universality class. We identify a central observable triality $\alpha_s = \beta_{\mathrm{mem}} = \text{anomalous heavy-traffic exponent}$ as the composition of three distinct source results under a common-exponent substrate-class condition: the aging-diagonal slope, the Caputo fractional memory exponent (Caputo, 1967; Podlubny, 1999; Metzler & Klafter, 2000), and the queueing tail exponent (Kingman, 1962; Norros, 1994) coincide when the substrate's slow-resource memory kernel and load-arrival process share a single anomalous-diffusion exponent. The four-aspect Complexity Wall (thermodynamic / dynamical / informational / SOC-critical) is a single critical point at $\epsilon \to 1$ for rate-distortion-optimal substrates; sub-optimal substrates split it through the gap parameter $\chi = C_\mu - I_{\mathrm{pred}}$ (Crutchfield, 1989; Shalizi & Crutchfield, 2001), and *die thermodynamically before they die informationally*. Wall approach forces — does not merely permit — meta-ledger chaos in the Newhouse–Ruelle–Takens sense (Ruelle & Takens, 1971; Newhouse, Ruelle, & Takens, 1978), via the stack: Cobham wait inflation (Kleinrock, 1976) $\to$ delay-induced Hopf at every tower ascent (Mackey & Glass, 1977) $\to$ 3-torus completion at $N \ge 3$; the Cobham–Haken bridge is an interpretive composition requiring three explicit substrate-side conditions (Poisson tower arrivals, single-server-pool $G_{\mathrm{total}}$, non-preemptive timescale ranking). The framework's API surface comprises five leading-order posits and eleven cross-register identities; pattern selection at $N \ge 3$ closes through four independent channels (frustration; generalised MSF (Sun, Bollt, & Nishikawa, 2009), with mild-heterogeneity scope; non-reciprocity (Fruchart, Hanai, Littlewood, & Vitelli, 2021); active-matter overlay (Toner & Tu, 1995; Cates & Tailleur, 2015), direct for active-matter substrates and a posited extension elsewhere). What remains open is a substrate-conditional list of empirical coupling parameters — and beneath each, substrate-thermodynamic derivation of the posited functional form — each with falsifier formalised. The framework's contribution is not new physics per substrate; it is the organisation of established results from stochastic thermodynamics, glassy aging, computational mechanics, control theory, queueing theory, active matter, fractional calculus, dynamical systems, and information geometry into a single substrate-neutral apparatus whose primitives compose, with every composition's substrate-side conditions surfaced.

---

## §1 — Setting and primitives

Character governs the continuous physical economics of sustaining a non-equilibrium steady state. It rides on top of v9's setting: drive $D = \Phi^*/\kappa$, observer kernel $\tau_{\mathrm{obs}}$, trail vectors in trail-class space. Where v9 supplies the stability axis $\lambda_A$ and reads regimes against $\pm D$, Character supplies the laser-threshold conjugate.

The framework's four primitives:

- **Coherence.** A macroscopic pattern of continuation maintained against natural dissolution. Laser analogue: cavity field above threshold.
- **Holding.** Continuous extraction of entropy, or application of work, sustaining a coherence as a NESS — for example, syndrome-measurement streams in a surface-code substrate (Kitaev, 2003; Fowler, Mariantoni, Martinis, & Cleland, 2012); cage maintenance in a glassy supercooled liquid; carrying-capacity adjustment in a Lotka–Volterra ecology (Hofbauer & Sigmund, 1998); reinforcement-extinction dynamics in a Rescorla–Wagner behavioural loop (Rescorla & Wagner, 1972; Sutton & Barto, 1998).
- **Maintenance budget $G_0$.** Unsaturated active work supplied per unit time, scaling with $D$. Laser analogue: small-signal gain (Haken, 1983; Siegman, 1986).
- **Decay rate $L$.** Spontaneous relaxation rate to the bath. Laser analogue: cavity loss.

A coherence *is* a macroscopic pattern of continuation; a holding is the active work that maintains it. The pair $(G_0, L)$ characterises the holding's instantaneous economic state. The framework's predictive content is the shape of dynamics on this two-parameter axis, made substrate-neutral by replacing $(G_0, L)$ with their log-ratio (§3).

## §2 — Bridge to v9

At zero amplitude the linearised field equation has eigenvalue

$$\lambda_A \approx L - G_0$$

(loss minus gain), recovering the standard laser linearisation (Haken, 1983). v9's regime conditions translate directly into operational margins in $(G_0, L)$:

| v9 regime | $\lambda_A$ vs $D$ | $G_0$ vs $L$ | Reading |
|---|---|---|---|
| $c$ | $\lambda_A \ll -D$ | $G_0 - L \gg D$ | deeply above threshold; saturation-clamped |
| $s$ | $\lvert\lambda_A\rvert \lesssim D$ | $\lvert G_0 - L\rvert \lesssim D$ | near threshold; Schawlow–Townes broadening and Cugliandolo–Kurchan aging coexist |
| $r$ | $\lambda_A \gg D$ | $G_0 - L \ll -D$ | sub-threshold; spontaneous emission only |

$G_0/L$ and $\lambda_A/D$ are different coordinates on the same regime structure; the bridge fixes Character's relationship to v9 throughout. Substrate-conditional reading rules — the Markovian sign caveat and detection-event preprocessing of v9 §F — inherit without modification.

## §3 — The chit unit

The native Character unit is the operational margin of a sustained coherence.

> **Definition (chit).** For a coherence with unsaturated maintenance budget $G_0$ and spontaneous decay rate $L$,
> $$\mathrm{chit} = \ln(G_0/L).$$

The logarithmic form is not a stylistic choice but a structural requirement. For a stochastic process with effective forward rate $\sim G_0$ and effective backward rate $\sim L$, $\ln(G_0/L)$ is the per-stochastic-transition entropy production of the Crooks fluctuation theorem (Crooks, 1999; Seifert, 2012). Three independent justifications — threshold symmetry ($G_0 = L \Rightarrow \mathrm{chit} = 0$), additivity across compositions of independent gain stages ($\mathrm{chit}(G_1G_2/L_1L_2) = \mathrm{chit}(G_1/L_1) + \mathrm{chit}(G_2/L_2)$), and $\ln 2$-alignment with Landauer's bound for the Bit/Chit pairing — collapse to three faces of the same rate-ratio structure rather than independent reasons.

**Markovian / orbit-affinity duality.** The rate-ratio reading is the Markovian specialisation of a more general per-orbit reading. For limit-cycle attractors with phase coordinate $\theta \in [0,2\pi)$, deterministic velocity $v(\theta)$ from the kernel, and bath-induced diffusion $D(\theta)$, the per-orbit chit is the continuous-orbit Schnakenberg affinity (Schnakenberg, 1976; Qian, 2001; Seifert, 2012):

$$\mathrm{chit}_{\mathrm{orbit}} = \oint \frac{v(\theta)}{D(\theta)}\,d\theta = \ln\frac{\mathcal{P}_+}{\mathcal{P}_-},$$

with $\mathcal{P}_\pm$ the probabilities of clockwise vs counterclockwise orbit traversal. The two faces agree at $\beta_{\mathrm{mem}} = 1$ (Markovian limit); for non-Markovian Caputo-memory substrates (§9) the orbit-affinity face is canonical. The orbit reading is the discipline-native form for the Character projection.

**Saturation distinction.** In a sustained NESS, saturated gain clamps to loss: $G_{\mathrm{sat}} = L$. The chit measures the *unsaturated* excess — the headroom above threshold, not the operating point. It is the Character conjugate to v9's structural drive $D$.

**Bit/Chit pairing.** The structural bit measures static informational volume $H$ and the Landauer cost of erasure ($W_R/\kappa \ge \ln 2 \cdot H(A\mid\text{rest})$; Landauer, 1961). The Character chit measures the dynamic operational margin and the continuous Harada–Sasa entropy cost of sustaining a state against $L$ (Harada & Sasa, 2005). Bit and chit are conjugate, not orthogonal — two faces of one thermodynamic ledger. The full dual-ledger consolidation arrives at §13, with the Still bound (Still, Sivak, Bell, & Crooks, 2012) closing the bijection at the rate-distortion-optimal limit.

**Threshold behaviour.**

- $\mathrm{chit} \gg 0$: $c$-regime (sustained coherence). Coherence amplitude scales with the excess.
- $\mathrm{chit} \to 0^+$: $s$-regime (visible strain). Schawlow–Townes linewidth broadening; the aging FDR signature of §5 appears.
- $\mathrm{chit} < 0$: $r$-regime (sub-threshold collapse to bath relaxation).

Limit-point status. chit = 0 is a critical limit, not an attainable operating state. Physical substrates approach it asymptotically from either side; the s-regime is a finite window around the limit (|λ_A| ≲ D, width set by the bath fluctuation scale, substrate-conditional), never the limit itself. The bath fluctuation scale resolves substrate-conditionally on a two-class split: drive-axis substrates (regime walked via drive vs threshold) carry physically irreducible s-window width set by thermodynamic noise on the drive variable (kT/q for diodes, Schawlow–Townes broadening for lasers); damping-axis substrates (regime walked via Q) carry measurement-limited width that vanishes in the deterministic limit. F-003-rlc's ratio_minimum = 0 at Q = 0.5 exactly is the damping-axis deterministic signature; drive-axis substrates have a non-zero floor. Substrate-conditional identifications of the chit = 0 locus (all faces of G₀ = L): lasing threshold (laser); distance-3 memory-Z at threshold physical error rate (surface code); T_g (glass); λ → 0 extinction onset (Rescorla–Wagner behavioural); r/K crossing at carrying capacity (ecological). Cross-substrate comparison proceeds via the dimensionless invariants measured within each window (α_s, P_s, Q-conjugate scaling, β_mem), not by absolute window-width matching; the load-bearing condition for windows being commensurable is the common-exponent substrate-class condition (§Universal two-mode kernel).

## §4 — Fraying sequence

Character measurement uses observation under continuous environmental load, in contrast to the discrete state perturbation appropriate to v9. Two load axes:

- **Demand/drain load.** Constraints reducing $G_0$.
- **Decay load.** Increases in bath coupling, raising $L$.

Load monotonically reduces the chit. The fraying sequence, in laser-substrate language:

> Saturated holding ($\mathrm{chit} \gg 0$, $c$, resilient) $\to$ visible strain ($\mathrm{chit} \to 0^+$, $s$, restoring forces weaken) $\to$ mode-hopping ($\mathrm{chit} \approx 0$, $s$ with multistability, budget splits among competing flows) $\to$ sub-threshold collapse ($\mathrm{chit} < 0$, $r$).

Visible strain and mode-hopping together populate v9's $s$ regime; mode-hopping is the laser-physics name for the multistable substructure that produces the aging plateau in CK-class FDR signatures (§5).

**Trajectory entropy production reading.** For a holding trajectory over an interval, the path entropy production $\sigma[\gamma]$ is a path functional of the field history. The Crooks detailed fluctuation theorem $P(\sigma)/P(-\sigma) = e^\sigma$ (Crooks, 1999) constrains its distribution: anomalous fraying-resistance trajectories — modes that sustain despite chit drop — are exponentially suppressed in $\lvert\sigma\rvert$. The fraying sequence is the *typical* trajectory; survival against load is *exponentially rare* in dissipation magnitude.

## §5 — Generalised fluctuation–dissipation signatures

Coherences are path-dependent NESS structures; equilibrium FDR fails. The generalised-FDR apparatus reads the relationship between a trail vector's spontaneous fluctuations (correlation $C(\tau)$) and its response to small probes ($\chi(\tau)$).

**Thermodynamic grounding.** The integrated FDR-violation factor yields the steady-state entropy production rate $\langle\sigma\rangle$ (Harada & Sasa, 2005), quantifying the true thermodynamic cost of holding without arresting the system.

**Per-regime invariants** (inherited from v9 §Fluctuation–dissipation signatures, restated in chit register, with CK universality after Cugliandolo & Kurchan, 1993; Crisanti & Ritort, 2003):

| Regime | Chit | Invariant | Reading |
|---|---|---|---|
| $c$ | $\gg 0$ | $X_c = \lim_\tau \chi(\tau)/(C(0)-C(\tau)) = 0$ | suppression / narrow horizontal locus |
| $s$ | $\to 0^+$ | $\alpha_s = $ slope of aging segment in $\chi$ vs $C(0)-C$ | Cugliandolo–Kurchan ratio |
| $s$ | $\to 0^+$ | $P_s = \lim_\tau C(\tau)/C(0)$ | plateau height |
| $r$ | $< 0$ | $X_r = 1$ | unit-slope FDR |
| $k_{\mathrm{frust}}$ subgraph | non-stationary | $N_f = \int_T \min(0,\chi)\,d\tau \big/ \int_T \lvert\chi\rvert\,d\tau$ | transient-negative fraction |

The aging diagonal slope $\alpha_s$ and plateau height $P_s$ are the load-bearing cross-substrate observables; the rest are within-class structural identifiers.

> **Theorem (Surface-code identification).** Distance-3 rotated memory-Z syndrome streams in a surface-code substrate (Kitaev, 2003; Fowler et al., 2012), at sub-threshold operation, trace a clean $s$-aging diagonal in the generalised-FDR plane with non-trivial $(\alpha_s, P_s)$ and migrate toward $X_r = 1$ unit slope as the physical-error rate crosses threshold. This places quantum error correction in the Cugliandolo–Kurchan universality class.

This is the framework's primary cross-substrate empirical content. The falsifier is sharp: (a) syndrome FDR shows unit slope sub-threshold (no CK signature, no $s$-regime identification), or (b) FDR shape persists unchanged across the threshold crossing (no $s \to r$ migration). Either observation falsifies the framework's central cross-substrate identification.

**Substrate-conditional reading rules** (inherited from v9 §F without modification):

- *Markovian sign caveat (v9 §F.1).* Stiff or Markovian substrates (overdamped Langevin, syndrome streams) invert $\gamma$ signs as a kernel-width artefact; use $\lvert\gamma\rvert$ jointly with FDR shape, not signs alone.
- *Detection-event preprocessing (v9 §F.2).* When the readout violates $\dot x$-locality (a raw stabiliser flip propagates), apply canonical local preprocessing — for surface codes, $e_i(t) = s_i(t) \oplus s_i(t-1)$, so an error at $t$ triggers exactly two events. Trail by EMA against detection events.

## §6 — Capacity dynamics

v9 supplies the static structural ceiling $\lvert\Gamma^*\rvert \le \sqrt{2D/(\alpha\,\gamma_{\min}\,d_{\mathrm{avg}})}$, with the Hopfield $\sqrt{D}$ scaling in the dense regime (Hopfield, 1982). Character supplies the dynamic conjugate: a sustainable phase-locked subgraph $\Gamma^*$ requires the integrated loss to fit inside the cooperatively-shared global maintenance budget,

$$\sum_{i\in\Gamma^*} L_i \le G_{\mathrm{total}}\,\eta(\Gamma^*).$$

**Cross-saturation efficiency $\eta(\Gamma^*) \in (0,1]$.** Limiting behaviour is fixed by v9's structural derivation: $\eta \to 0$ at the $\sqrt{D}$ Hopfield ceiling, where non-orthogonal interference between continuous flows depletes shared gain. The Character bound is not independent of v9's structural bound — it is the same wall, read from the dynamic side.

> **Theorem (Erlang-B closure of $\eta$).** With static capacity $c = \lfloor\lvert\Gamma^*\rvert_{\mathrm{crit}}\rfloor$ and effective offered load $\rho$ on the mode-slot pool, cross-saturation efficiency satisfies
> $$\eta(\Gamma^*) = 1 - B(c,\rho), \qquad B(c,\rho) = \frac{\rho^c/c!}{\sum_{k=0}^c \rho^k/k!}$$
> (Erlang's loss formula; Erlang, 1917). Hard-wall substrates (e.g. a surface code at logical-error onset) replace $B$ by the indicator $\mathbb{1}[\lvert\Gamma^*\rvert \ge c]$.

The derivation is given in Appendix A.1. Limits: $\rho \ll c \Rightarrow \eta \to 1$ (sparse, no blocking). For soft-substrate Erlang-B, $\eta = 1 - B(c,c) \in (0,1)$ at $\rho = c$ (finite blocking probability; smooth crossover); $\eta \to 0$ only as $\rho \to \infty$. For hard-wall substrates the indicator gives $\eta \to 0$ abruptly at $\rho = c$ — the Hopfield-ceiling reading is the hard-wall limit. The soft/hard split is itself a substrate-class fingerprint (Open: §20). For surface codes a single error breaks the code — hard-wall, no probabilistic blocking; for behavioural substrates near attentional saturation the standard $B(c,\rho)$ applies — soft.

**Capacity-wall dynamics.** When the inequality $\sum L_i \le G_{\mathrm{total}}\eta$ is violated, the system cannot supply $G_{0,i}$ globally. It sparsifies — dropping vertices to $r$ — or distributes the deficit, driving the network into a sub-threshold phase transition, regardless of local chit margins. This is v9's static capacity ceiling rederived through the dynamic side and given an Erlang-B closure.

## §7 — Heat-tax tower

v9's Compression Axiom contracts informational structure up the meta-ledger tower with operator norm $\epsilon = \lVert\mathcal{C}\rVert_{\mathrm{op}} < 1$. Character routes the *thermodynamic exhaust* of that flow.

Each ascent pays a continuous maintenance cost — a heat tax. The decay rate at level $n+1$ inherits noise from level $n$'s entropy production *and* the active stress that level-$n$ holdings impose on the coarse-grained manifold:

$$L_{n+1} = L_{n+1}^{(0)} + \alpha_\sigma\langle\sigma_n\rangle + \alpha_\Sigma\langle\Sigma_n\rangle.$$

Two substrate-effect axes propagate level-$n$ activity to level $n+1$ via distinct conductivities $\alpha_\sigma$ (thermal/informational noise) and $\alpha_\Sigma$ (active stress); the bare $\beta$ symbol is reserved throughout for the Caputo memory exponent $\beta_{\mathrm{mem}}$:

- $\alpha_\sigma\langle\sigma_n\rangle$: heat from level-$n$ flow appearing as ambient noise at level $n+1$.
- $\alpha_\Sigma\langle\Sigma_n\rangle$: active stress from level-$n$ maintenance work appearing as mechanical / informational / structural stress at level $n+1$ (§16 active-matter extension).

> **Theorem (Landauer pin of $\alpha_\sigma(\epsilon)$).** At meta-ledger level $n$, the compression operator $\mathcal{C}_n$ retains fraction $\epsilon$ of level-$n$ informational mass $\Phi_n$ and erases fraction $(1-\epsilon)$. By Landauer's bound, erasure produces heat $\ge (1-\epsilon)\Phi_n k_B T_n \ln 2$ per ascent. The conductivity $\alpha_\sigma$ routing $\langle\sigma_n\rangle$ as ambient noise into $L_{n+1}$ must carry the $(1-\epsilon)$ prefactor:
> $$\alpha_\sigma(\epsilon) = \alpha_{\sigma,0}(1-\epsilon),$$
> with $\alpha_{\sigma,0}$ a substrate-conditional thermal-conductivity constant. Per-level Landauer heat $\alpha_\sigma(\epsilon)\langle\sigma_n\rangle \to 0$ vanishes at $\epsilon \to 1^-$ — no information erased, no Landauer cost. The Wall's thermodynamic content sits in cumulative informational mass: $\Phi_{\mathrm{total}} = \Phi^{(0)}/(1-\epsilon)$ from the rate-distortion geometric series (§13). Cumulative tower tax to depth $N$ scales as $1 - \epsilon^N$ for any per-level prefactor — convergent for $\epsilon < 1$ at depth $N \to \infty$, divergent in $N$ as the geometric series fails to converge at $\epsilon \ge 1$. The Complexity Wall is a thermodynamic singularity *of cumulative tower mass*, not of per-level heat.

The derivation is given in Appendix A.2.

**Three independent failure channels.** Sustained level-$n+1$ coherence requires $\ln(G_{0,n+1}/L_{n+1}) > 0$. Fraying at level $n$ inflates $L_{n+1}$ through three independent channels:

1. The $\alpha_\sigma\langle\sigma_n\rangle$ heat-tax spike (this section).
2. The $\alpha_\Sigma\langle\Sigma_n\rangle$ active-stress spike (§16).
3. An $r_n$ drop in level-$n$ collective sync, raising $L_{n+1}^{(0)}$ via lost cooperative gain-sharing (§12).

These three channels are *not* independent mechanisms but three measurement registers of one queueing-theoretic mechanism. By the Cobham/Kleinrock priority-queue mapping (Kleinrock, 1976; Cobham, 1954; §17), all three are faces of Cobham wait-time inflation $W_{n+1} = W_0/[(1-u_n)(1-u_{n+1})]$ across tower-level priority classes ranked by Haken's slaving principle (Haken, 1983), where $u_n$ is the level-$n$ cumulative utilisation. The mapping is an interpretive bridge between distinct mathematical structures (Haken slaving is a centre-manifold reduction, Cobham wait is a queueing-discipline formula); it requires three substrate-side conditions, stated explicitly in §17 and Appendix A.13. The queueing singularity $u_n \to 1^-$ is coincident with the informational Complexity Wall $\epsilon \to 1^-$; under the rate-distortion-optimal encoding identity $u_n = \epsilon_n$ (§17 ε↔u closure; one of the framework's five leading-order posits), the queueing and informational singularities collapse to a single parameter.

**r-coupling between channels 2 and 3.** Channels 2 and 3 share $r$ as a driver in *opposing* directions. Toner–Tu hydrodynamics (Toner & Tu, 1995; §16) gives an active-stress correction $f(r) = Cr^2$, so the active-stress channel scales as $1 + Cr^2$ in level-$n$ sync; the cooperative-gain channel is triggered by $r$-drop. The substrate active-coupling $C$ (sign: contractile $>0$, extensile $<0$, isotropic $\approx 0$) determines the balance. The three channels remain independent failure paths but two are coupled through $r$.

**Sub-optimal substrates die thermodynamically before they die informationally.** Sub-optimal substrates have $u_n > \epsilon_n$ with overhead $\Delta_n = u_n - \epsilon_n \ge 0$ as a substrate-class fingerprint; their thermodynamic and SOC-critical aspects reach criticality first (via $u \to 1$), while the informational aspect ($\epsilon \to 1$) is reached only by rate-distortion-optimal substrates. This is one face of the *optimal-encoding triality* — three faces of one gap parameter — consolidated in §18.

The heat-tax tower is the thermodynamic conjugate of v9's Convergent Tower / Complexity Wall. v9 bounds informational compression; Character bounds the heat that compression cannot avoid.

## §8 — Operators in continuous register

v9's discrete operators have continuous-traversal shadows. In v9, $C \in \Sigma$ is a discrete evaluation of joint stability with Boolean shadow $\land$; in Character, $C_{\mathrm{Character}}$ is the continuous adiabatic process of steering two budget densities into the cooperative fixed point of the universal two-mode kernel (§9). Similarly for $R$.

**$C_{\mathrm{Character}}$ (merge).** Adiabatic deformation from $\gamma_{AB} \approx 0$ (decoupled) to $\gamma_{AB} \ll 0$ (cooperative) while sustaining the NESS.

- *Phase-locking and gain sharing.* As $\gamma_{AB}$ goes negative, $G_A$ and $G_B$ overlap; the joint maintenance cost falls below the sum of isolated parts.
- *Adiabatic requirement.* The deformation rate must be slow relative to $L$. Forced non-adiabatically, the chit approaches zero, the system enters $s$-regime visible strain, and Harada–Sasa $\sigma$ spikes transiently before the cooperative fixed point is acquired.
- *Failure mode.* If the available drive cannot cover the transient cost, or if the underlying shear product resists cooperation, one or both modes drop sub-threshold and collapse to spontaneous emission.

Information-geometrically (§13), the merge succeeds iff a Fisher-information geodesic from $\gamma_{AB} \approx 0$ to $\gamma_{AB} \ll 0$ stays on the above-threshold manifold — that is, does not exit through the chit-zero locus. The adiabaticity bound becomes a geodesic-tangent constraint on the Fisher manifold (Amari & Nagaoka, 2000).

**Discrete shadow: v9 Theorem 9.** Sampled at fixed $D$, the adiabaticity bound recovers v9's deformation-calculus result $\Delta_C(A,B) = 1$ iff $\gamma_{AB} > 0 \land D < \gamma_{AB}$. The Boolean step function in v9 is the sharp-threshold limit of the continuous traversal-survivability function. Joint stability is not a static property of the merged state but a measure of the trajectory's survivability through the deformation.

**$R_{\mathrm{Character}}$ (sever).** Quench trajectory: choke $G_0$ (demand-load) or open mode to bath ($L \uparrow$, decay-load). Native edge dissolution — $\gamma_{AB}\rho_A\rho_B$ vanishes as $\rho_A \to 0$, no separate graph-edit required. Continuous dissipation registers as a $\sigma$ spike during collapse; v9's Landauer bound is the asymptotic discrete limit. The discrete logic of erasure is the asymptotic limit of the driven-dissipative collapse — Landauer is the integrated cost of the quench.

## §9 — Universal two-mode kernel

v9's Composite catalogue enumerates discrete pair-types between coherences: $c$–$c$ aligned, $c$–$s$ mentor, $c$–$c$ opposed, and so on. Character recovers these as fixed points and dynamical regimes of a single continuous two-mode field equation.

**Universal two-mode budget kernel.**

$$\frac{\partial \rho_A}{\partial t} = \underbrace{(G_{0,A} - L_A)\rho_A}_{\text{local threshold}} \;-\; \underbrace{\gamma_{AB}\,\rho_A\rho_B}_{\text{cross-saturation}} \;+\; \underbrace{\mathcal{D}[\rho_A,\rho_B;\gamma_{AB}]}_{\text{non-local kernel}}$$

(symmetric for $\rho_B$). Sign convention: $\gamma_{AB} < 0$ contributes positively to $\partial_t\rho_A$, matching v9.

**The $\mathcal{D}$-kernel admits three increasingly general closures**, derived in Appendix A.3.

*Lamb stationary closure (two-mode reduction).* Standard multi-mode laser gain depletion (Lamb, 1964; Haken, 1983) gives the effective gain

$$G_{0,A}^{\mathrm{eff}} = G_{0,A}\bigm/\Bigl(1 + \sum_{j\ne A}\rho_j/\rho_{\mathrm{sat}}\Bigr).$$

Under the two-mode reduction at mean-field-stationary rest-of-network occupancy, $G_{0,A}^{\mathrm{eff}}$ absorbs the bath load; the cubic cross-saturation term appears as the leading-order expansion around small densities.

*Dynamic bath inversion.* When ambient bath occupancy fluctuates on timescales comparable to $\rho_i$ relaxation, promote the bath to a dynamical coordinate $B(t) \in [0,1]$:

$$\dot B = \gamma_B[1 - B\,S(t)], \qquad \dot\rho_i = \bigl(G_{0,i}B(t) - L_i\bigr)\rho_i - \sum_j \gamma_{ij}\rho_i\rho_j.$$

Mori–Zwanzig projection-out of $B$ gives a non-Markovian history integral (Mori, 1965; Zwanzig, 1973). The fast-bath limit $\gamma_B \to \infty$ recovers the Lamb stationary form. The inverse bath-server rate $\gamma_B^{-1}$ identifies as the effective service time in the Cobham mapping of §17.

*Caputo fractional memory.* For glassy / $s$-regime aging substrates, the $\mathcal{D}$-kernel memory generalises from exponential to Mittag-Leffler relaxation: the Caputo derivative $^C D^{\beta_{\mathrm{mem}}}$ with exponent $\beta_{\mathrm{mem}} \in (0,1)$ governs slow-resource dynamics, giving

$$\Gamma_{AB}(\tau) = \Gamma_0\,E_{\beta_{\mathrm{mem}}}\bigl(-(\tau/\tau_c)^{\beta_{\mathrm{mem}}}\bigr), \qquad K(\tau) \sim \tau^{-\beta_{\mathrm{mem}}}/\Gamma(1-\beta_{\mathrm{mem}}) \text{ for } \tau \gg \tau_c$$

(Caputo, 1967; Mittag-Leffler, 1903; Podlubny, 1999; Mainardi, 2010; Metzler & Klafter, 2000). The Markovian limit $\beta_{\mathrm{mem}} = 1$ recovers the exponential closure. Off-Markovian $\beta_{\mathrm{mem}} < 1$ gives stretched-exponential or power-law decay — canonical glassy-substrate signature.

> **Theorem (Three-way exponent identity).** Under the *common-exponent substrate-class condition* — the substrate's slow-resource memory kernel and load-arrival process share a single anomalous-diffusion exponent — the Cugliandolo–Kurchan $s$-regime aging-diagonal slope $\alpha_s$, the Caputo fractional memory exponent $\beta_{\mathrm{mem}}$, and the anomalous heavy-traffic queueing exponent (Kingman, 1962; Norros, 1994) are *the same parameter* measured in three registers:
> $$\alpha_s \;=\; \beta_{\mathrm{mem}} \;=\; \text{anomalous heavy-traffic exponent}.$$

The identity composes two source results. From physics: the non-Markovian fluctuation–dissipation theorem (Pottier, 1985; Mainardi, 2010) identifies the Caputo exponent with the FDR aging slope, presupposing that the memory kernel governing slow-resource dynamics is the Caputo kernel $\tau^{-\beta_{\mathrm{mem}}}$. From operations research: the fractional-Brownian generalisation of Kingman's heavy-traffic limit (Norros, 1994; Leland, Taqqu, Willinger, & Wilson, 1994) generalises $1/(1-\rho)$ to $1/(1-\rho)^{\beta_{\mathrm{mem}}}$, presupposing that the load-arrival process is self-similar with the same Hurst-class exponent. The two registers therefore concern *distinct* substrate-side processes (memory kernel vs arrival process); the identity holds only when both are driven by a common underlying anomalous-diffusion structure. Three disciplines, one parameter, *one substrate-class condition* — this is the central architectural anchor (consolidated in §18); the condition itself is a substrate-class fingerprint, falsified by substrate classes where the FDR exponent and the queueing-tail exponent are measured to differ (§20 falsifier).

**Bifurcation analysis: the attractor skeleton.** Sweeping $\gamma_{AB}$ as a continuous control parameter recovers v9's catalogue as fixed points of this phase portrait:

| Regime | $\gamma_{AB}$ | Phase relationship | v9 row |
|---|---|---|---|
| $c$–$c$ aligned | $\ll 0$ | in-phase locked | Hebbian / force chain |
| $c$–$s$ mentor | $< 0$, asymmetric | driven entrainment, substrate-non-reciprocal, formally a priority queue | pilot-light / synaptic tagging |
| $c$–$c$ orthogonal | $\approx 0$ | unlocked / phase drift | independent memory |
| $c$–$c$ opposed (lock) | $> 0$, $K > \Delta\omega$ | anti-phase locked | competing hypotheses |
| $c$–$c$ opposed (split) | $> 0$, $K < \Delta\omega$ | competitive desynchronisation (pitchfork) | Lotka–Volterra dropout |
| $k_{\mathrm{frust}}$ | $N \ge 3$ obstructive | frustrated sync | gridlock / UNSAT |

The two views are complementary projections, not nested. v9's discrete pair-types are the named fixed points of this kernel; the kernel is the continuous-field representation of the same pair structure. Multi-mode pattern selection for $N \ge 3$ admits chimera states (§12) and is fully closed via four channels (§18).

## §10 — Topological drain $k_{\mathrm{frust}}$

In v9, $k_{\mathrm{frust}}$ is a topological invariant of the coupling graph: a cycle of $c$-edges with obstructive shear product, not resolvable by $D$. Character *derives* this invariance from the $N \ge 3$ universal kernel — the structural impossibility is the asymptotic shadow of a continuous-flow pathology, not a separate axiom.

**Non-stationary trajectory.** When $N$ modes are coupled in a closed chain with obstructive $\gamma$ topology, the coupled field equations admit no stationary synchronised fixed point. Cross-saturation terms $\gamma_{ij}\rho_i\rho_j$ continuously conflict; no mutual stabilisation exists.

- *Cyclic sub-threshold collapse.* Because no joint NESS exists, the kernel forces a non-stationary oscillatory trajectory. Some mode's chit goes negative on every cycle.
- *Pumping–fraying cycle.* As the forced mode collapses ($\rho \to 0$), the local cross-saturation conflict eases, the mode pumps back above threshold, the coupling landscape shifts, and a *different* mode is forced into fraying.

**Divergent maintenance economics.**

- *Time-averaged divergence.* Because the trajectory continuously bath-relaxes and re-pumps, the time-averaged $G$ required to hold the macroscopic pattern diverges.
- *Drive independence.* The drain cannot be relieved by raising $D$. The instability is internal to the cross-saturation mathematics, not an absolute-resource shortage. This recovers v9's "not resolvable by $D$" claim from the kernel.

**Six-register reading of one phenomenon.**

1. Cyclic pumping–fraying trajectory (this section): some mode's chit goes negative each cycle; time-averaged $G$ diverges.
2. Hopf-unstable spiral with attracting limit cycle (§11): cooperative fixed point repels; system on attracting orbit.
3. Frustrated sync (§12): pairwise lock-attempts broken by topological obstruction, re-form around different weakest mode.
4. Schnakenberg cycle current with divergent action (§13): $J_C \ln(\prod_+ k/\prod_- k)$ forced regardless of $D$.
5. Non-existence of Lyapunov function (§15): no positive-definite decreasing $\mathcal{V}$.
6. Priority-queue inversion (§17): asymmetric load absorption with no symmetric back-flow.

These six register-readings collapse at the topology level to the same fact — that no $P_{ss}$ exists in the excised parameter region. The deeper structure is the *topological triality* of §18: the dynamical (no stationary fixed point), informational-geometric (no Fisher geodesic traverses the region, a homotopy obstruction; Amari & Nagaoka, 2000), and thermodynamic (drive-independent Schnakenberg cycle current forced by orbit topology) faces of one excision.

**gFDR signature.** The dynamic cyclic collapse leaves a distinct thermodynamic trace: the constant exhaust and dynamical gridlock of the non-stationary trajectory register as the transient-negative response $N_f$ in loop-level spin-glass response theory (§5). It is the empirical measurement of a closed-chain NESS actively failing to find its attractor.

## §11 — Stability and attractor structure

The §2 bridge gives the linear-stability eigenvalue $\lambda_A \approx L - G_0$ at zero amplitude. Its real part (sign vs $D$) sets the regime; its full complex structure governs the *recovery profile* — how perturbations to the operating point return.

Above threshold, a single-mode coherence is generically two-dimensional in its local linearisation (field $\times$ population). The Jacobian at the saturated fixed point has a complex-conjugate eigenvalue pair with relaxation rate $\gamma_{RO}$ and oscillation frequency $\omega_{RO}$ — the *relaxation-oscillation* regime of laser physics (Haken, 1983; Siegman, 1986; Weiss & Vilaseca, 1991). Perturbations return via damped oscillation, not pure exponential decay.

**Per-regime damping signatures.**

| Regime | Damping | Recovery profile | Attractor |
|---|---|---|---|
| $c$ | $\zeta < 1$ underdamped | decaying oscillation at $\omega_{RO}$; resonance peak in active-probe response | stable spiral / focus |
| $s$ | $\zeta \to 1$ critical | slowest non-oscillatory return; algebraic settling tail; the §5 $s$-aging diagonal is its long-time limit | centre manifold at threshold |
| $r$ | $\zeta > 1$ overdamped | first-order bath relaxation; no oscillator | stable origin |
| $k_{\mathrm{frust}}$ | repelling cooperative focus | cyclic, no return | attracting limit cycle |

> **Theorem (Closed form of $\omega_{RO}$).** For the §9 single-mode kernel linearised at the saturated fixed point, the relaxation-oscillation parameters in chit register are
> $$\gamma_{RO} = \gamma_s/2, \qquad \omega_{RO} = \sqrt{2\gamma_s L\,(e^{\mathrm{chit}}-1)}, \qquad Q = \omega_{RO}/(2\gamma_{RO}) = \sqrt{2L(e^{\mathrm{chit}}-1)/\gamma_s},$$
> where $\gamma_s$ is the substrate's slow-resource turnover rate.

The derivation is given in Appendix A.4, recovering the standard class-B laser result (Haken, 1983; Siegman, 1986). The slow-resource turnover rate $\gamma_s$ takes substrate-conditional values: population decay in lasers, syndrome decoding in surface codes, plasticity in neural substrates, carrying-capacity adjustment in ecological substrates, reinforcement-extinction in behavioural substrates. Limits: $\mathrm{chit} \to 0^+$ ($s$-regime) gives $\omega_{RO} \to 0$, $Q \to 0$ — relaxation oscillations vanish at threshold, consistent with the critical-damping signature for $s$. Deep in $c$, $Q$ grows as $e^{\mathrm{chit}/2}/\sqrt{\gamma_s}$ — many cycles of headroom.

**$Q$-factor as Character observable.** $Q$ measures coherence cycles surviving per decay envelope. It is conjugate to the chit: $\mathrm{chit}$ reads *whether* the headroom holds; $Q$ reads *how many cycles* of natural oscillation that headroom buys under perturbation.

**Active/passive probe = on/off resonance.** Probes within $\gamma_{RO}$ of $\omega_{RO}$ are active (Q-amplified, engaging the maintenance feedback through the relaxation-oscillation loop); off-resonance probes are passive baseline. The boundary linewidth is $\gamma_{RO}$.

**Recovery profile is a third probe-class signature** alongside spontaneous FDR (steady-state stochastic) and load-driven fraying (sustained-load trajectory). Each isolates different content; the three are complementary.

**Slow-manifold reading of $s$-aging.** At threshold, the leading eigenvalue's real part vanishes; dynamics collapse onto the centre manifold (Guckenheimer & Holmes, 1983). The CK aging signature *is* the slow-manifold trace: $P_s$ is the slow-manifold fixed-point amplitude; $\alpha_s$ is the slow eigenvalue's residual scaling against saturating gain. This is not new physics, but recognition.

**Bifurcation summary** (codimension-1 explicit in framework):

- Transcritical at $\mathrm{chit} = 0$ (laser threshold; $c \leftrightarrow r$).
- Pitchfork at $\gamma_{AB} = \gamma_c$ (cooperative–competitive boundary).
- Hopf-unstable at obstructive $\gamma$-chain onset ($k_{\mathrm{frust}}$).

Codimension-2 closures follow from standard normal-form theory: Bogdanov–Takens at the pitchfork–Hopf intersection; cusp, Bautin, and fold-Hopf via the standard catastrophe-theory apparatus (Bogdanov, 1975; Takens, 1974; Kuznetsov, 2004).

> **Theorem (Wall-forces-NRT).** As $u_n \to 1^-$ at the Complexity Wall (§17 Cobham closure), each tower-level ascent $n \to n+1$ undergoes a delay-induced Hopf bifurcation (Mackey & Glass, 1977; Kuznetsov, 2004). With $N \ge 3$ ascents Hopf-bifurcating, the 3-torus required for Newhouse–Ruelle–Takens chaos populates automatically (Ruelle & Takens, 1971; Newhouse, Ruelle, & Takens, 1978). Meta-ledger chaos post-Wall is *forced, not merely allowed*, contingent on (i) the substrate not collapsing into $r$-regime before the bifurcation sequence completes, and (ii) the three substrate-side conditions of the Cobham–Haken bridge (§17, Appendix A.13) which set $u_n$ as the wait-inflation parameter.

The three-closure stack — Cobham wait formula $\to$ DDE Hopf per ascent $\to$ NRT chaos at $N \ge 3$ — is derived in Appendix A.5 and is one of the central architectural anchors of the framework (consolidated in §18).

## §12 — Phase-locking and collective coherence

§11 supplies the natural oscillation frequency $\omega_{RO}$ of a single coherence above threshold, together with the attractor types of the single-mode kernel. Synchronisation theory is the apparatus for *phase relationships* among coupled oscillators — when they lock, when they don't, and what the collective coherence reads (Kuramoto, 1984; Pikovsky, Rosenblum, & Kurths, 2001; Strogatz, 2003).

**Two-mode phase locking.** Two coherences $A,B$ above threshold have natural frequencies $\omega_A, \omega_B$ and detuning $\Delta\omega = \lvert\omega_A - \omega_B\rvert$. Coupling through $\gamma_{AB}$ locks the modes if $K_{AB} \gtrsim \Delta\omega$. Below the lock threshold, $\phi_A - \phi_B$ drifts; above, it is bounded. Arnold-tongue structure in $(\Delta\omega, K_{AB})$ follows directly.

> **Theorem (Closed form of $K_{AB}$).** Phase-reducing the §9 two-mode kernel near the limit cycle gives
> $$K_{AB} = -\gamma_{AB}\,\frac{\sqrt{\rho_A\rho_B}}{\rho_{\mathrm{sat}}}\,\frac{1}{\sqrt{1+4Q^2}}.$$

The derivation is given in Appendix A.6, following the standard Kuramoto phase-reduction apparatus applied to a relaxation oscillator (Kuramoto, 1984; Ermentrout & Terman, 2010). The geometric-mean-amplitude factor is the dimensionally-correct coupling carrier; the $(1+4Q^2)^{-1/2}$ susceptibility crossover interpolates the two regimes the framework already names. The weak-coupling / $c$-regime limit ($Q \gg 1$) recovers the standard $1/(2Q)$ Kuramoto suppression $K_{AB} \approx -\gamma_{AB}\sqrt{\rho_A\rho_B}/(2Q\rho_{\mathrm{sat}})$; the strong-coupling / $s$-regime ($Q \lesssim 1$) gives direct phase locking. Sign convention follows v9: $\gamma_{AB} < 0$ gives $K_{AB} > 0$ (in-phase lock); $\gamma_{AB} > 0$ gives $K_{AB} < 0$ (anti-phase lock).

**Order parameter.** Kuramoto $r = \lvert(1/N)\sum_n e^{i\phi_n}\rvert$: collective coherence amplitude, independent of per-mode chit.

**Two independent phase transitions and observables.** The framework reads $N$-mode NESS through two second-order transitions (chit-zero amplitude onset, Kuramoto $K_c$ phase onset) and two population-level order parameters (per-mode chit, collective $r$). Neither implies the other.

**Sync feedback to the heat-tax tower.** $L_{n+1}^{(0)}$ depends on level-$n$ sync: high $r_n$ reduces $L_{n+1}^{(0)}$ (cooperative gain-sharing); low $r_n$ raises it. This is the third channel of upward fraying propagation noted in §7.

**Chimera states.** Partially-synchronised regimes — coexisting synchronised $c$-regime and incoherent $r$-regime sub-populations at fixed substrate parameters — are generic in heterogeneous-coupling kernels (Kuramoto & Battogtokh, 2002; Abrams & Strogatz, 2004; Lazarides & Tsironis, 2015; Tinsley, Nkomo, & Showalter, 2012). The framework closes their mechanism through the generalised Master Stability Function for heterogeneous networks (Sun, Bollt, & Nishikawa, 2009; Pecora & Carroll, 1998). *Scope note:* the Sun–Bollt–Nishikawa apparatus is derived as a perturbative extension of Pecora–Carroll for nearly-identical systems; its use as a stability test on generic Character kernels is the *mild-heterogeneity* application of SBN. For strongly-heterogeneous substrate classes (large per-mode variance in $\omega_{RO,i}$, $\gamma_{s,i}$, or chit), the SBN spectral test should be read as a leading-order diagnostic that retains its sign reliably but not its exact eigenvalue gaps; quantitative use in the strong-heterogeneity regime is a posited extension whose accuracy is a substrate-class fingerprint (§20 falsifier). Spectral splits of the generalised Laplacian

$$\mathcal{L}_{ij} = -K_{ij}\cos(\phi_j^* - \phi_i^*) \quad (j \ne i), \qquad \mathcal{L}_{ii} = \sum_{j \ne i} K_{ij}\cos(\phi_j^* - \phi_i^*)$$

are the mathematical signature of chimera-admitting kernels: when the transversal spectrum partitions into a stable subspace (locked cluster, $c$-regime sub-population) and an unstable subspace (drifting modes, $r$-regime sub-population), the long-time attractor is a chimera. The derivation and substrate-instancing falsifier are given in Appendix A.7.

## §13 — Thermodynamic and informational accounting

Stochastic thermodynamics and information theory consolidate into a single dual ledger. Both are direct adoptions; the chit's $\ln$ structure already places the framework inside both registers.

**Trajectory entropy production.** Crooks's detailed fluctuation theorem $P(\sigma)/P(-\sigma) = e^\sigma$ (Crooks, 1999): anomalous fraying-resistance trajectories are exponentially rare in $\lvert\sigma\rvert$.

**Thermodynamic Uncertainty Relation.** $\mathrm{Var}(J)/\langle J\rangle^2 \ge 2k_B/\langle\sigma\rangle$ (Barato & Seifert, 2015; Horowitz & Gingrich, 2020). Maintenance-current precision is bounded by entropy production — the framework's first explicit precision–cost constraint. The TUR composes with the §7 heat-tax tower: at level $n+1$, the inherited noise floor $\alpha_\sigma\langle\sigma_n\rangle$ pays for level-$n$ precision (via TUR at level $n$) and inflates the level-$n+1$ loss rate (via §7 directly).

**Schnakenberg cycle decomposition.** $\langle\sigma\rangle = \sum_C J_C \ln(\prod_+ k/\prod_- k)$ on the master-equation embedding (Schnakenberg, 1976) — note that $\gamma_{ij}$ are kernel parameters, not transition rates; the affinity is the log-ratio of compound rates around the embedded cycle. For limit-cycle attractors (rows 6, 7 of §9) the continuous-traversal form is

$$\sigma_{\mathrm{frust}} = J_{ss}\oint v(\theta)/D(\theta)\,d\theta$$

on the orbit ring (Qian, 2001; Seifert, 2012). The drive-independence of $k_{\mathrm{frust}}$ is the topologically-forced cycle current — $v(\theta)$ integrates to nonzero by topology; drive scales $J_{ss}$ but not the affinity. The master-equation and orbit closures are derived in Appendix A.8.

**Predictive information.** $I_{\mathrm{pred}} = I(\text{past};\text{future})$ (Bialek, Nemenman, & Tishby, 2001). A third independent coherence observable alongside chit and $Q$:

| Observable | Reads |
|---|---|
| chit | *whether* threshold is cleared |
| $Q$ | *how many cycles* of headroom |
| $I_{\mathrm{pred}}$ | *how predictable* the trajectory is given history |

**Active-probe channel capacity.** $C \sim B\log_2(1 + S/N)$ with $B \sim \gamma_{RO}$, $S/N \sim Q$ (Shannon, 1948; Cover & Thomas, 2006). This is the informational dual of TUR; together they are the two faces of the observability bound.

**Information geometry.** Fisher metric on $(G_0, L, \gamma_{AB}, \ldots)$ space (Amari & Nagaoka, 2000). Geodesics are max-likelihood deformation paths; the §8 $C_{\mathrm{Character}}$ adiabatic merge condition becomes "geodesic stays on above-threshold manifold." The drain $k_{\mathrm{frust}}$ excises a region from the parameter manifold (no $P_{ss}$ exists there), making it a homotopy obstruction — one face of the topological triality consolidated in §18.

**Rate-distortion / Compression Axiom.** $\mathcal{C}$ is lossy compression on trail-class space; $\epsilon$ is its compression rate. The Convergent Tower $\Phi_{\mathrm{total}} = \Phi^{(0)}/(1-\epsilon)$ is the standard rate-distortion geometric series (Shannon, 1959; Cover & Thomas, 2006).

**Extended second law.** $\langle\sigma\rangle \ge -\Delta I$ (Sagawa & Ueda, 2010; Parrondo, Horowitz, & Sagawa, 2015). Bit-readout holdings sustain at lower chit by paying via mutual information.

**Bit/Chit dual ledger.**

| Axis | Thermodynamic | Informational |
|---|---|---|
| Per-event | $\mathrm{chit} = \ln(G_0/L)$ | $\mathrm{bit} = \ln 2$ |
| Per-rate | $\langle\sigma\rangle$ (Harada–Sasa) | $I_{\mathrm{pred}}$ |
| Precision | TUR | Channel capacity |
| Compression | Heat-tax tower | Rate-distortion tower |
| Coupling | $\langle\sigma\rangle \ge -\Delta I$ | (same bound, dual reading) |

> **Theorem (Bijective duality at the rate-distortion-optimal limit).** Under the Still thermodynamic prediction bound (Still, Sivak, Bell, & Crooks, 2012),
> $$\langle\sigma\rangle \;\ge\; \gamma_s[I_{\mathrm{mem}} - I_{\mathrm{pred}}] + \langle\sigma\rangle_{\min},$$
> with $I_{\mathrm{mem}} = C_\mu$ the structural complexity of the Crutchfield $\varepsilon$-machine (Crutchfield, 1989; Shalizi & Crutchfield, 2001). Identifying the cryptic order $\chi = C_\mu - I_{\mathrm{pred}} \ge 0$,
> $$\langle\sigma\rangle - \langle\sigma\rangle_{\min} \;\ge\; \gamma_s\,\chi,$$
> with equality at the rate-distortion-optimal encoding limit. Sub-optimal substrates split the dual ledger by exactly $\gamma_s\chi$.

The derivation is given in Appendix A.9. The same gap parameter $\chi$ appears as the §15 cryptic order and as the §17 ε↔u encoding overhead $\Delta_n = u_n - \epsilon_n$. This is the **optimal-encoding triality** — one quantity $\chi = \Delta_n = \langle\sigma\rangle_{\mathrm{excess}}/\gamma_s$ measured in three protocols (cryptic order / encoding overhead / dissipation excess) — consolidated in §18.

## §14 — Pattern formation and self-organisation

**Holdings as dissipative structures.** A coherence above threshold is a Prigogine dissipative structure: an ordered configuration sustained by continuous throughput against natural relaxation (Prigogine & Nicolis, 1977; Nicolis & Prigogine, 1989). The chit-zero crossing *is* the dissipative-structure formation transition. Substrate examples (laser, glass, surface code, behavioural, biological homeostasis) are substrate-conditional instances of the same threshold mathematics.

**Chit as order parameter (Haken's slaving).** Near the bifurcation, fast modes are *enslaved* by the slow order-parameter mode (Haken, 1983). The §11 centre-manifold reduction is the slaving relation read backward. Above threshold, fast micro-modes adiabatically follow the chit's evolution; the chit is not just a measure of holding-margin but the *order parameter* that emerges at the dissipative-structure transition.

**Self-organised criticality.** Under feedback-coupled maintenance dynamics, chit-zero is an *attractor in parameter space*, not merely a regime boundary. The SOC mechanism (Bak, Tang, & Wiesenfeld, 1987; Bak, 1996; Beggs & Plenz, 2003): slow stress accumulation interleaved with fast relaxation events drives the operating point to marginal regardless of initial conditions. Predicted $s$-regime signatures include power-law avalanche statistics $P(s) \sim s^{-\tau}$ with mean-field exponent $\tau \approx 3/2$ (Stauffer & Aharony, 1992), 1/f spectral tails consistent with the CK aging diagonal (Sethna, Dahmen, & Myers, 2001), and spatiotemporal scale invariance in multi-mode fraying clusters.

> **Theorem (Galton–Watson branching at chit-zero).** Fraying propagation maps to a Galton–Watson branching process (Galton & Watson, 1875; Harris, 1963) with branching ratio
> $$\mu = G_0/L = e^{\mathrm{chit}}.$$
> At $s$-regime threshold $\mathrm{chit} \to 0^+$, $\mu \to 1^+$ — Galton–Watson critical branching, giving avalanche-size distribution $P(s) \sim s^{-3/2}$ in mean field.

The derivation is given in Appendix A.10. The functional form $\mu = e^{\mathrm{chit}}$ is *posited* — one of the framework's five leading-order posits (§18). Universality fixes the exponent; substrate dimensionality fixes the empirical correction (2D directed-percolation gives $\tau \approx 1.26$; 3D substrates give intermediate values; mean-field gives $\tau = 3/2$ exactly).

**Galton–Watson at two registers.** The framework has *two* distinct critical branching processes, both reaching criticality at framework-primitive boundaries:

- *Horizontal / spatial:* branching ratio $\mu = e^{\mathrm{chit}} \to 1$ at $\mathrm{chit} = 0$ — the $s$-regime dissipative-structure transition.
- *Vertical / meta-ledger:* tower branching ratio $\to 1$ at $\epsilon = 1$ — the Complexity Wall.

Both yield Galton–Watson $\tau = 3/2$ at mean-field criticality. One SOC universality class instantiated at two framework registers (consolidated in §18).

**Meta-ledger as branching process.** The §7 heat-tax tower has the structure of a branching process: a level-$n$ fraying event raises $L_{n+1}$ via $\alpha_\sigma\langle\sigma_n\rangle$ and via the $r_n$-drop. The SOC-critical branching ratio reaching unity *is* the Complexity Wall. *Scope note on iid assumption:* classical Galton–Watson presupposes iid offspring distributions across generations. The horizontal (spatial / within-level) branching above satisfies this in the standard mean-field reading. The vertical (meta-ledger / cross-level) branching does *not*: the offspring distributions at successive tower levels are correlated through the shared maintenance budget $G_{\mathrm{total}}$ and through level-coupled $\alpha_\sigma\langle\sigma_n\rangle / \alpha_\Sigma\langle\Sigma_n\rangle / r_n$-drop channels (§7). Use of $\mu \to 1$ as the vertical-register critical threshold is therefore a *correlated-offspring branching-process posit*, sharper than classical GW: criticality-at-unity is robust under the standard correlated-branching extensions (multitype Galton–Watson with bounded cross-type covariance; Harris, 1963), but the mean-field exponent $\tau = 3/2$ at the vertical register is conditional on the cross-level correlations remaining weak enough that the single-type mean-field universality is retained. Substrate-specific cross-level coupling strengths are an open empirical question (§20 falsifier).

> **Theorem (Four-aspect Complexity Wall).** At $\epsilon = 1$, four critical signatures coincide:
> - **Thermodynamic:** $\alpha_\sigma(\epsilon)\sum_n \langle\sigma_n\rangle$ ill-conditioned as the cumulative-mass geometric series with ratio $\epsilon$ fails to converge (§7).
> - **Dynamical:** the meta-ledger flow undergoes a bifurcation in trail-class space (§11).
> - **Informational:** the lossy-compression rate hits unity (§13).
> - **SOC-critical:** the fraying branching ratio reaches unity (this section).

That these four aspects are register-faces of a *single* unifying parameter $\beta_{\mathrm{mem}} \to 0$ rests on the Wall-coupling posit $\beta_{\mathrm{mem}} \approx 1 - \epsilon$ stated immediately below. Without that posit, the four aspects remain coincident at $\epsilon = 1$ but their *common scaling parameter* across registers is not guaranteed; the §17 spatial expression of the Wall (traffic-driven $\to$ frozen-topological transition; $\ell_c(\beta_{\mathrm{mem}})$) is the spatial signature of the same posited parameter, not a fifth independent aspect.

**Wall-coupling posit.** Leading-order linear coupling between compression rate $\epsilon$ and Caputo memory exponent:

$$\beta_{\mathrm{mem}} \approx 1 - \epsilon.$$

This is the simplest functional form satisfying both endpoints: $\epsilon \to 0$ gives $\beta_{\mathrm{mem}} \to 1$ (Markovian); $\epsilon \to 1$ gives $\beta_{\mathrm{mem}} \to 0$ (extreme aging). The posit is testable, one of the framework's five leading-order posits (§18); substrate-thermodynamic derivation of the exact functional form is the residual open beneath the falsifier (§20).

**Caputo memory exponent as load-bearing Wall control parameter.** The four-aspect Wall is the multiple-register expression of $\beta_{\mathrm{mem}} \to 0$, not five aspects. The same parameter governs the swim-pressure divergence at the Wall via the §16 Green–Kubo identification, the spatial Kelly-network product-form breakdown (§17), the variable-ratio behavioural-extinction tail (§15), and the spatial traffic-driven $\to$ frozen-topological transition (§17). Seven registers, one parameter — the central Caputo chain consolidated in §18.

**Regime ontology recast.** $s$-regime is the *generic* attractor of feedback-coupled NESS, not the unstable middle of a triplet:

- $c$-regime: over-provisioned holdings (chit pulled deep above threshold by external constraint).
- $s$-regime: self-organised natural operating point of feedback-coupled holdings.
- $r$-regime: post-collapse holdings.

This explains the empirical over-representation of $s$-regime in observed substrates: feedback-coupled NESS systems land there because the parameter-space attractor pulls them.

**Hierarchy of dissipative structures.** The §7 heat-tax tower is hierarchical pattern formation: each ascent is a new dissipative-structure transition with its own chit-as-order-parameter and its own slaving relation. §11 per-level attractor structure, this section's per-level SOC self-tuning, and §7 heat-tax across levels are three aspects of one nested formation.

**Spatial pattern formation: Turing-class wavelength selection.** Extending the §9 kernel with spatial diffusion gives a reaction–diffusion system $\dot\rho_i = f_i(\rho) + D_i\nabla^2\rho_i$. Turing instability (Turing, 1952; Murray, 2003) requires three substrate-conditional conditions:

1. Non-reciprocal cross-coupling ($\gamma_{AB}\gamma_{BA} < 0$, the §16 mentor row): gives correct off-diagonal Jacobian signs $J_{AB} < 0$, $J_{BA} > 0$.
2. Substrate-native autocatalysis ($\gamma_{ii} < 0$): the bare §9 kernel has $J_{AA} = 0$ at coexistence; Lamb gain depletion gives $J_{AA} < 0$ (self-saturation); substrates without autocatalytic self-coupling do *not* exhibit Turing patterns.
3. Differential diffusion ($D_B \gg D_A$): canonical short-range activation / long-range inhibition.

The Turing instability derivation is given in Appendix A.11.

**Mentor row's dual face.** The non-reciprocal mentor structure produces *two distinct manifestations* depending on substrate spatial structure: a temporal limit cycle with frequency $\omega_{\mathrm{pq}} \approx \sqrt{\lvert\gamma_{AB}\gamma_{BA}\rvert\rho_A^*\rho_B^*}$ when not spatially extended (§16); a spatial Turing pattern when also equipped with substrate autocatalysis and differential diffusion. The temporal and spatial expressions of the same coupling asymmetry (consolidated in §18).

**Three distinct spatial-structure mechanisms.** Turing reaction–diffusion (this section; needs all three conditions); Kelly queueing-congestion product-form breakdown (§17; needs bandwidth contention only); frozen-topological at $\beta_{\mathrm{mem}} \to 0$ (§17). Not reducible to each other.

**Multi-mode pattern selection is fully closed at the framework level via four channels:** frustration test, generalised MSF spectral test, non-reciprocity test, active-matter overlay. Consolidated in §18.

## §15 — Active modulation and internal models

The active probe of §11, the SOC feedback of §14, and the slaving relation of §14 are partial control-theoretic content. This section formalises the closed-loop structure of holdings and adds the framework's deepest substrate-internal claim: the internal model principle.

**Plant–controller decomposition.** A holding is a closed loop. The *plant* is the substrate's natural dynamics (§2 open-loop eigenvalue). The *controller* is the maintenance feedback adjusting $G_0$ based on observed plant state. The closed-loop eigenvalue is shifted by the controller transfer function, generically toward stability (Åström & Murray, 2008).

The §11 active probe, §14 SOC feedback, and §14 slaving relation are three aspects of one closed-loop structure (consolidated in §18): the holding *is* a controller actively shaping its plant.

**Lyapunov stability.** The chit is a candidate single-mode Lyapunov function. Non-frustrated multi-mode topologies admit a relative-entropy Lyapunov $\mathcal{V}$ (Goh, 1977; Hofbauer & Sigmund, 1998; Takeuchi, 1996); the calligraphic symbol distinguishes the Lyapunov function from the Rescorla–Wagner associative-strength variable $V$ used below:

$$\mathcal{V} = \sum_i\bigl[x_i - x_i^* - x_i^*\ln(x_i/x_i^*)\bigr]$$

on gauged amplitudes (Harary structural-balance gauge; Harary, 1953), with $d\mathcal{V}/dt = -\delta x^T \gamma\,\delta x \le 0$ when the gauged $\gamma$ is positive semi-definite. The drain $k_{\mathrm{frust}}$ admits *no* Lyapunov — non-existence is the dynamical-systems content of "no stationary fixed point" (§10). The derivation is given in Appendix A.12.

**Weighted Lyapunov for frustration-free-but-not-PSD topologies.** For Volterra–Lyapunov stable matrices that are not PSD (Redheffer, 1985; Takeuchi, 1996), a strictly positive diagonal weight matrix $W = \mathrm{diag}(w_i)$ exists such that $W\gamma + \gamma^T W$ is PSD. The weighted relative-entropy Lyapunov:

$$\mathcal{V}(\{x\}) = \sum_i w_i\bigl[x_i - x_i^* - x_i^*\ln(x_i/x_i^*)\bigr].$$

Volterra–Lyapunov stable matrices are a strict superset of PSD: $W = I$ recovers PSD; some non-PSD matrices admit non-trivial $W$ satisfying the symmetric-part condition.

**Substrate-class auto-tuning posit.** Framework prediction: substrates natively tune $\gamma_{s,i}$ to satisfy diagonal stability via the inverse form

$$W = \mathrm{diag}(\gamma_{\mathrm{ref}}/\gamma_{s,i})$$

— inverse-scaling, slow-mode-dominant weighting. One of the framework's five leading-order posits (§18). Substrate-thermodynamic derivation of which $w_i \leftrightarrow \gamma_{s,i}$ form holds is the residual open beneath the falsifier (§20).

**Internal model principle.** A controller robust to a class of substrate disturbances must internally encode the generating structure of those disturbances (Francis & Wonham, 1976; Sontag, 2003). Substrate-conditional instances: the surface-code decoder is an internal model of the substrate's error process; the glass cage is an encoding of the bath schedule's slow modes; the behavioural pattern is an encoding of the reinforcement schedule's structure. *A coherence is a substrate's local accumulation of model.*

**Behavioural substrate via continuous-time Rescorla–Wagner.** With associative strength $V(t)$, maximum conditioning $\lambda$, and learning rate $\kappa_{RW}$ (Rescorla & Wagner, 1972; Sutton & Barto, 1998):

$$\dot V = \kappa_{RW}(\lambda - V).$$

Mappings to Character primitives: $V \to \rho$ (coherence amplitude); $\kappa_{RW} \to \gamma_s$ (slow-resource turnover); $\lambda$ conjugate to the maintenance budget $G_0$ (sustained reward schedule); extinction ($\lambda \to 0$) equals the $R_{\mathrm{Character}}$ quench trajectory. The behavioural substrate maps to first-order relaxation; variable-ratio reinforcement schedules are predicted to instance Caputo memory $\beta_{\mathrm{mem}} < 1$ in extinction tails — the sixth cross-register connection in the Caputo chain.

**Four-axis coherence observable.**

| Axis | Reading | Source |
|---|---|---|
| chit | whether threshold is cleared | §3 |
| $Q$ | cycles of headroom | §11 |
| $I_{\mathrm{pred}}$ | predictability given history | §13 |
| Internal-model richness | how rich a model of disturbance is encoded | this section |

The four axes are independent: chit can be high while $I_{\mathrm{pred}}$ is low; $Q$ can be high while internal-model richness is moderate. Internal-model richness may explain substrate-class variance in the $s$-regime clustering of §14 — rich-model substrates cluster tighter near critical, weak-model substrates drift further.

**Structural complexity and cryptic order.** The structural-complexity reading $C_\mu = H(\mathcal{S})$ on Crutchfield $\varepsilon$-machine causal states (Crutchfield, 1989; Shalizi & Crutchfield, 2001) is mathematically independent of $I_{\mathrm{pred}}$ for hidden-state processes, with $C_\mu \ge I_{\mathrm{pred}}$ and **cryptic order** $\chi = C_\mu - I_{\mathrm{pred}} \ge 0$ as the gap (Crutchfield, Ellison, & Mahoney, 2009). *Stationarity-gap note:* the $\varepsilon$-machine construction and the $C_\mu \ge I_{\mathrm{pred}}$ inequality are derived for stationary processes, whereas the framework's load-bearing positive instance — the surface-code $s \to r$ CK-aging signature (§5) — targets non-stationary trajectories. The reconciliation routes through two compatible readings: (i) the *trajectory-ensemble* reading: at each fixed waiting-time $t_w$, the time-translated ensemble is locally stationary, $C_\mu(t_w)$ and $I_{\mathrm{pred}}(t_w)$ are well-defined, and $\chi(t_w)$ is the slowly-varying gap parameter along the aging diagonal; (ii) the *non-stationary computational-mechanics* reading: time-varying $\varepsilon$-machines (Shalizi, 2003; standard non-stationary CSSR extensions) give the same $C_\mu \ge I_{\mathrm{pred}}$ inequality at each instantaneous causal-state partition. The framework uses (i) by default; substrate classes whose aging is too rapid for ensemble local-stationarity inherit (ii) as the conditional reading. The cryptic order identifies with the §17 sub-optimal encoding overhead at the optimal-limit closure:

$$\chi = \Delta_n \qquad (\text{at the optimal-encoding limit}).$$

One of the framework's five leading-order posits. The structural–informational gap drives the thermodynamic–informational split — see the §13 dual-ledger closure, consolidated in §18.

## §16 — Collective hydrodynamics

**Holdings as active-matter units.** Self-propulsion equals per-coherence maintenance dynamics. Alignment equals cooperative $\gamma_{AB}$. Density equals local count of coexisting coherences in a region.

**Toner–Tu hydrodynamics.** For populations with continuum spatial extent, slow dynamics of density $n(x,t)$ and orientational order $\mathbf{p}(x,t)$ satisfy the Toner–Tu equations (Toner & Tu, 1995, 1998; Marchetti et al., 2013). The flocking transition $\lvert\mathbf{p}\rvert = 0 \to \lvert\mathbf{p}\rvert > 0$ is the population-level analog of the chit-zero threshold. *Scope note:* Toner–Tu is derived for active-matter substrates with intrinsic self-propulsion and aligning interaction; its use as a Character overlay is direct for substrate classes carrying these structures (active colloids, motile cells, robotic swarms, flocking animals) and is a *posited extension* — Character's "active-matter overlay" channel — for substrate classes lacking intrinsic self-propulsion (surface codes, neural ensembles, glassy substrates, behavioural substrates). In the extension regime, the active stress / swim-pressure formulae below should be read as the Character framework's leading-order proposal for an effective stress tensor, with substrate-thermodynamic derivation of the effective $v_0, \tau_R$ a substrate-class residual (§20).

**Active stress and the §7 heat-tax extension.** Holdings impose more than heat on coarse-grained manifolds: mechanical stress (physical substrates), informational stress (surface-code syndrome buffers), structural stress (behavioural substrates). The substrate-class fingerprint at hydrodynamic level (Takatori & Brady, 2014; Solon et al., 2015):

$$\frac{\alpha_\Sigma}{\alpha_\sigma} \sim \frac{v_0^2\,\tau_R}{D_{\mathrm{trans}}}$$

(swim-pressure ratio; alignment-independent, MIPS-compatible, surviving $r \to 0$).

**Green–Kubo identification of $\tau_R$.** The substrate-neutral identification of the rotational persistence time is

$$\tau_R = \int_0^\infty \langle\mathbf{u}(t)\cdot\mathbf{u}(0)\rangle\,dt,$$

where $\mathbf{u}(t)$ is the unit-vector direction of the holding's active maintenance-work application in its state space (Brady, 2014; Cates & Tailleur, 2015). The same mathematical object across substrates: literal self-propulsion direction (active matter); trajectory direction of applied corrections (surface codes); population-vector orientation (neural). For non-Markovian substrates with Caputo $\beta_{\mathrm{mem}} < 1$, $\tau_R$ formally diverges (integrand $\sim t^{-\beta_{\mathrm{mem}}}$); finite-size cutoffs regularise.

**Active-stress closure.** Toner–Tu active pressure (Solon et al., 2015):

$$P_{\mathrm{active}} = \frac{n\,v_0^2\,\tau_R}{d}\bigl[1 + C r^2\bigr]$$

with active-coupling constant $C = \zeta_0 d/(v_0^2\tau_R)$. The substrate-class fingerprint via $C$: contractile ($C > 0$), extensile ($C < 0$), isotropic ($C \approx 0$). This drives the §7 $r$-coupling between heat-tax channels 2 and 3 (consolidated in §18).

**Giant number fluctuations.** Active populations exhibit $\delta N \sim N^a$ with $a > 1/2$ (canonical $a = 1$; Ramaswamy, Simha, & Toner, 2003). The TUR may saturate or loosen in this regime; substrate-class diagnostic.

**Non-reciprocal coupling.** v9's §Falloff already flags this as an extension axis. The §9 universal two-mode kernel admits $\gamma_{AB} \ne \gamma_{BA}$; the coexistence Jacobian has $\mathrm{Tr} = 0$, $\det = -\gamma_{AB}\gamma_{BA}\rho_A^*\rho_B^*$, giving three regimes by sign of $\gamma_{AB}\gamma_{BA}$ (Fruchart, Hanai, Littlewood, & Vitelli, 2021):

| Sign | $\det$ | Type | Reading |
|---|---|---|---|
| $> 0$ (both cooperative or both competitive) | $< 0$ | Saddle | runaway / competitive exclusion |
| $< 0$ (asymmetric, mentor / exploitation) | $> 0$ | Centre $\to$ limit cycle under $\mathcal{D}$ | priority-queue oscillation |
| $= 0$ (one-sided) | $= 0$ | Exceptional point | non-diagonalisable; phase drift / unlock |

Finite-$\mathcal{D}$ corrections promote the linear centre (mentor regime) to a stable limit cycle with frequency $\omega_{\mathrm{pq}} \approx \sqrt{\lvert\gamma_{AB}\gamma_{BA}\rvert\rho_A^*\rho_B^*}$; spatially extended, traveling waves with phase velocity $v \sim \sqrt{D_{\mathrm{diff}}\lvert\gamma_{AB}\gamma_{BA}\rvert}$. The §9 mentor row is *actually* non-reciprocal in substrate dynamics; the symmetric-kernel formal expression is a simplification.

**Motility-induced phase separation.** Pure repulsive interactions with self-propulsion produce phase separation — a clustering mechanism not present in §9 (Cates & Tailleur, 2015; Fily & Marchetti, 2012). Clustering at $\gamma_{AB} \ge 0$ via self-propulsion-induced density fluctuations alone. Substrate instancing: open (§20).

## §17 — Load-handling and capacity dynamics

§6 gives the static capacity bound; §4 gives the load-driven fraying sequence. Queueing theory is the apparatus for *temporal* load-handling: how a holding processes the time-resolved arrival stream of perturbations, what its waiting-time and saturation statistics are, and how to compose holdings into networks.

**Holdings as queues.** Mapping: $\lambda$ arrival rate of perturbations, $\mu$ service rate ($\sim G_0$), utilisation $\rho = \lambda/\mu$. The chit is dual to utilisation at the simplest mapping: $\mathrm{chit} = -\ln\rho$.

| Regime | Chit | $\rho$ | Queueing state |
|---|---|---|---|
| $c$ | $\gg 0$ | $\ll 1$ | stable, low-traffic |
| $s$ | $\to 0^+$ | $\to 1^-$ | heavy traffic, critical fluctuations |
| $r$ | $< 0$ | $> 1$ | unstable, queue blowup |

**Heavy traffic equals $s$-aging.** Kingman's $\langle Q\rangle \sim 1/(1-\rho)$ heavy-traffic limit (Kingman, 1962) *is* the $s$-aging signature of §5 in queueing register; the CK exponent $\alpha_s$ has a heavy-traffic queue-length analog. The two coincide for Markovian substrates and diverge for non-Markovian ones — the divergence pattern is a substrate-class diagnostic (falsifier in §20).

**Little's law.** $\langle Q\rangle = \lambda\langle W\rangle$ (Little, 1961). The framework's first explicit $\langle\text{amplitude}\rangle \times \langle\text{rate}\rangle \times \langle\text{timescale}\rangle$ relation at fixed operating point.

**Jackson-network special case.** For Markov–Poisson substrates: product-form steady state $P(\mathbf{Q}) = \prod_i P_i(Q_i)$ with Burke departure-process structure (Jackson, 1957; Burke, 1956). Tractable explicit-solution regime; applicable when memoryless-arrival and exponential-service assumptions hold.

**Multiclass priority and the mentor row.** The §9 mentor row is structurally a priority queue (Kelly, 1979): the mentor's processing serves the follower's load preferentially. The §9 mentor row, §16 non-reciprocal coupling, and this section's priority queue are three readings of one substrate-deep asymmetry.

> **Theorem (Cobham priority-queue mapping).** For a hierarchy with shared maintenance budget pool $G_{\mathrm{total}}$ as server, tower levels $n$ as priority classes ranked by Haken's slaving (fast micro-modes serve slow macro-modes), arrival rates $\lambda_n$ as fraying-event frequencies, and service times $\tau_n = 1/\gamma_{s,n}$, the Cobham expected wait for priority class $n+1$ is
> $$W_{n+1} = \frac{W_0}{(1-u_n)(1-u_{n+1})}, \qquad W_0 = \tfrac{1}{2}\sum_i \lambda_i\langle\tau_i^2\rangle,$$
> with per-level utilisation $\rho_n = \lambda_n\tau_n$ and cumulative utilisation $u_n = \sum_{i=0}^n \rho_i$. A level-$n$ load spike $\rho_n \uparrow$ consumes shared-pool bandwidth; Kleinrock conservation forces compensating wait inflation $W_{n+1} \uparrow$. The §7 three-channel decomposition labels three measurement registers of the resulting $L_{n+1}$ inflation.

*The Cobham–Haken bridge.* The Theorem maps two distinct mathematical structures onto each other: Haken's slaving is a centre-manifold reduction whose ranking is by *natural-timescale separation* of fast vs slow modes; Cobham's priority-queue formula is a wait-time identity for *non-preemptive priority service* with Poisson arrivals at a *single server pool*. The mapping is interpretive, not derivational, and inherits three substrate-side conditions: (i) **Poisson arrivals at the tower level** — fraying events arrive at rate $\lambda_n$ as a memoryless Poisson process (or close enough that the heavy-tailed corrections of the fractional generalisation are leading-order); (ii) **single-server-pool interpretation of $G_{\mathrm{total}}$** — the shared maintenance budget acts as one resource pool serving all priority classes, not a per-class allocation (substrates with strictly per-level budget partitioning carry a Jackson-network rather than Cobham mapping); (iii) **non-preemptive ranking by timescale** — Haken's centre-manifold slow modes serve as Cobham priority *classes* under the convention that the slowest macroscopic mode is highest-priority (consistent with the wait $W_{n+1}$ growing toward the slow-resource $\gamma_{s,n+1}$ pole). Substrate classes failing any of these inherit a corresponding modification of the Cobham formula; the framework's use of the Theorem is correct for substrate classes where all three approximately hold (Appendix A.13).

The derivation is given in Appendix A.13 following Cobham (1954) and Kleinrock (1976). Cobham wait diverges at $u \to 1^-$, coincident with the §7 thermodynamic singularity at $\epsilon \to 1^-$.

**ε↔u optimal-encoding identity.** For a substrate at the rate-distortion bound, arrival load onto the level-$n$ maintenance queue scales exactly with retained informational mass:

$$u_n = \epsilon_n \qquad (\text{rate-distortion-optimal encoding}).$$

One of the framework's five leading-order posits. Sub-optimal substrates have $u_n > \epsilon_n$ with overhead $\Delta_n \ge 0$; the four-aspect Wall splits, with thermodynamic and SOC aspects reaching criticality first (via $u \to 1$), the informational aspect ($\epsilon \to 1$) only by optimal-encoding substrates.

**Spatial Jackson-network generalisation.** Spatial extension via Kelly's product-form theorem (Kelly, 1979): $P(\mathbf{Q}) = \prod_k P_k(Q_k)$ across patches $k$, each patch independently undergoing Cobham priority dynamics; spatial coupling re-emerges only in transient response. Non-Markovian Caputo memory violates Kelly's quasi-reversibility; the critical interaction length $\ell_c(\beta_{\mathrm{mem}})$ for product-form breakdown depends on the Caputo exponent (derivation in Appendix A.14):

$$\ell_c(\beta_{\mathrm{mem}}) = \sqrt{\frac{2D_{\beta_{\mathrm{mem}}}}{\Gamma(1+\beta_{\mathrm{mem}})}\Bigl(\frac{W_0}{1-u_n}\Bigr)^{\beta_{\mathrm{mem}}}}.$$

**Traffic-driven $\to$ frozen-topological transition.** As $u_n \to 1^-$ alone (Markovian heavy traffic), $\ell_c$ diverges via wait-time inflation. As $\beta_{\mathrm{mem}} \to 0$ at the Wall, $W^{\beta_{\mathrm{mem}}} \to 1$ and $\ell_c \to \sqrt{2D_0}$ with degenerate dimension — the fractional diffusion law collapses to time-independent spread. This is the *spatial expression* of the Wall — a regime transition from dynamic congestion domains (traffic-driven, $\beta_{\mathrm{mem}} \sim 1$) to frozen topological domains (memory-driven, $\beta_{\mathrm{mem}} \to 0$). The substrate's intrinsic topology sets the freeze-length. The spatial expression is the §14 four-aspect Wall read spatially under the Wall-coupling posit, not an independent fifth aspect.

## §18 — Framework primitives consolidation

The closure of all closed-form residuals and structural conjectures produced architectural content that was not designed in. This section foregrounds it: one methodological pattern (the framework's API surface) and eleven cross-register identities (single primitives manifesting across registers). All material here is already in the framework; this section is a reading guide, not new claims.

### Five leading-order posits

Five framework primitives share an identical four-part shape:

1. simplest functional form placing a framework primitive at its critical / optimal limit;
2. substrate-conditional deviation from that form;
3. falsifier formalised;
4. substrate-thermodynamic derivation as receipts-only residual.

| Posit | Framework location | Receipts entry |
|---|---|---|
| $\beta_{\mathrm{mem}} \approx 1 - \epsilon$ | §14 Pattern formation | §9 Wall-coupling |
| $\mu = e^{\mathrm{chit}}$ | §14 Pattern formation | §18 Galton–Watson |
| $w_i = \gamma_{\mathrm{ref}}/\gamma_{s,i}$ | §15 Active modulation | §20 auto-tuning |
| $u_n = \epsilon_n$ | §7 Heat-tax tower | §17 ε↔u |
| $\chi = \Delta_n$ | §15 Active modulation | §15 cryptic order |

The pattern is the framework's **API surface**: universality fixes exponents (the simple form at the limit); substrates fix amplitudes (deviations from the form) — renormalisation-group language. Each posit is testable; none is derived from substrate thermodynamics. Future closures of the same shape are the canonical extension mode.

### Eleven cross-register identities

Each entry names one load-bearing primitive and the registers it manifests across.

**1. Caputo memory exponent $\beta_{\mathrm{mem}}$ — seven-register chain of one parameter.**

- Memory-tail $t^{-\beta_{\mathrm{mem}}}$ (§9 Caputo closure).
- Green–Kubo $\tau_R$ divergence (§16 $\tau_R$).
- Swim-pressure fingerprint $\alpha_\Sigma/\alpha_\sigma$ divergence via $\tau_R$ (§16).
- Spatial Kelly-network product-form breakdown (§17 spatial).
- Wall-coupling $\beta_{\mathrm{mem}} \approx 1 - \epsilon$ posit (§14 Wall-coupling).
- Variable-ratio behavioural-extinction tail (§15 habit-extinction).
- Spatial traffic-driven $\to$ frozen-topological transition via $\ell_c(\beta_{\mathrm{mem}})$ (§17 critical length).

The unifying $s$-regime / Wall-approach control parameter, *under the Wall-coupling posit* $\beta_{\mathrm{mem}} \approx 1 - \epsilon$. The four-aspect Wall (thermodynamic / dynamical / informational / SOC) is its multiple-register expression — *four core register-faces of one parameter under the posit*. The §17 spatial expression ($\ell_c$) reads the same parameter spatially; it is not a fifth independent aspect.

**2. Optimal-encoding triality.** $\chi = \Delta_n = \langle\sigma\rangle_{\mathrm{excess}}/\gamma_s$ — one quantity, three measurement protocols:

- Cryptic order $\chi = C_\mu - I_{\mathrm{pred}}$ (§15).
- Encoding overhead $\Delta_n = u_n - \epsilon_n$ (§17).
- Dissipation excess $\langle\sigma\rangle - \langle\sigma\rangle_{\min} = \gamma_s\chi$ (§13).

Sub-optimal substrates die thermodynamically before they die informationally. The four-aspect Wall is a single parameter only at the optimal limit; sub-optimal substrates split it.

**3. Wall-forces-NRT chain.** Three closures stacking to make meta-ledger chaos *forced* (not allowed) past the Wall:

- Cobham wait $W_{n+1} \to \infty$ at $u_n \to 1^-$ (§17), under the Cobham–Haken bridge conditions.
- Generic Hopf per tower-ascent via DDE characteristic equation (§11).
- $N \ge 3$ ascents complete the 3-torus required for NRT chaos (§11).

Substrate-conditional only on whether $r$-regime collapse precedes the bifurcation sequence and on the Cobham–Haken bridge conditions holding (§17).

**4. Galton–Watson branching at two registers.** One mean-field universality class instantiated at two framework-primitive boundaries:

- Horizontal / spatial: $\mu = e^{\mathrm{chit}} \to 1$ at $\mathrm{chit} = 0$ (within-level; §14).
- Vertical / meta-ledger: tower branching ratio $\to 1$ at $\epsilon = 1$ (across-level; §14).

Mean-field $\tau = 3/2$ at criticality on both registers; substrate-graph effective dimensionality fixes the empirical exponent. The horizontal register satisfies the classical iid-offspring assumption directly; the vertical register couples through shared $G_{\mathrm{total}}$ and the three §7 channels and is a correlated-offspring extension of classical Galton–Watson — criticality-at-unity survives standard multitype extensions, the mean-field exponent is conditional on weak cross-level correlation (§14 scope note).

**5. Mentor row's dual face.** One non-reciprocal coupling structure, two morphological manifestations:

- Temporal limit cycle, frequency $\omega_{\mathrm{pq}} \approx \sqrt{\lvert\gamma_{AB}\gamma_{BA}\rvert\rho_A^*\rho_B^*}$ (§16 non-reciprocal).
- Spatial Turing pattern, wavenumber $k_c$ — when also equipped with substrate autocatalysis and differential diffusion (§14 Turing).

Substrate spatial structure selects between the two faces; the underlying coupling asymmetry is the same.

**6. Three distinct spatial-structure mechanisms.** Distinguishable prerequisites and dynamics:

- Turing reaction–diffusion: requires non-reciprocity + substrate autocatalysis + differential diffusion (§14).
- Kelly queueing-congestion product-form breakdown: requires bandwidth contention; no autocatalysis or differential diffusion needed (§17).
- Frozen-topological at $\beta_{\mathrm{mem}} \to 0$: memory-driven; substrate intrinsic topology sets freeze-length (§17 critical length).

Not reducible to each other; a substrate may carry one, two, or all three at different scales.

**7. $r$-coupling between heat-tax channels 2 and 3.** Channels 2 ($\alpha_\Sigma\langle\Sigma_n\rangle$, scaling as $1 + Cr^2$) and 3 ($r$-drop sync degradation) share $r$ as driver in *opposing* directions. The substrate active-coupling $C$ (sign: contractile $> 0$, extensile $< 0$, isotropic $\approx 0$) determines balance (§16 $f(r)$). The three heat-tax channels remain independent failure paths but two are coupled through $r$.

**8. $k_{\mathrm{frust}}$ topological triality.** Three co-implied measurement protocols, one underlying fact (no $P_{ss}$ exists in the excised parameter region):

- Dynamical: no stationary fixed point (§10).
- Informational-geometric: no Fisher geodesic traverses the region — a homotopy obstruction (§13).
- Thermodynamic: drive-independent Schnakenberg cycle current forced by orbit topology (§13).

Identity at the underlying-topology level; substrate-specific measurement signatures differ across registers.

**9. $s$-regime exponent triality.** One parameter, three mathematical-discipline measurements all yielding the same numeric value *under the common-exponent substrate-class condition* (substrate slow-resource memory kernel and load-arrival process share a single anomalous-diffusion exponent; §9):

$$\alpha_s \;=\; \beta_{\mathrm{mem}} \;=\; \text{anomalous heavy-traffic exponent}.$$

- CK aging-diagonal slope $\alpha_s$ — physics, gFDR signature (§5).
- Caputo fractional memory exponent $\beta_{\mathrm{mem}}$ — fractional calculus (§9).
- Heavy-traffic queue-tail anomalous exponent — operations research (§17).

Three disciplines, one parameter; the substrate-class condition itself is a fingerprint (§20 falsifier). Distinct from item 1 (the $\beta_{\mathrm{mem}}$ chain of *consequences*); this is the $\beta_{\mathrm{mem}}$ *identity across measurement protocols*. Both belong.

**10. Four-channel pattern selection architecture.** Multi-mode ($N \ge 3$) pattern selection decomposes into exactly four independent tests, all closed:

- Frustration test (signed-graph sign-product; §§10, 13, 15).
- Spectral sync test (Sun–Bollt–Nishikawa generalised MSF; §12; mild-heterogeneity scope, posited extension to strong heterogeneity).
- Non-reciprocity test (Jacobian sign analysis; §16).
- Active-matter overlay (Toner–Tu, MIPS; §16; direct for active-matter substrates, posited extension elsewhere).

The complete operating system for multi-mode emergence; any $N \ge 3$ Character kernel routes through these four tests, with channels 2 and 4 carrying explicit substrate-class scope as noted.

**11. Closed-loop plant–controller unifier.** Three aspects of one closed-loop control structure (the holding shaping its own plant):

- Active probe (§11): on-resonance feedback through relaxation-oscillation loop.
- SOC self-tuning (§14): feedback-coupled chit-zero attractor.
- Haken slaving (§14): centre-manifold reduction read backward.

The plant–controller decomposition (§15) is the unifying register; the three are different reading-protocols of the same closed-loop.

## §19 — Methodological imperatives

- **Trajectory primacy.** Bounded time-series data of sustained holding, not static point measurements. The framework's primitives are NESS observables, defined on trajectory ensembles.
- **NESS-by-default.** Detailed-balance breaking is foundational baseline; equilibrium is the degenerate (zero-drive) special case. The framework does not specialise NESS theory to near-equilibrium; equilibrium specialises NESS theory to detailed balance.
- **Reading rules inherit from v9.** Substrate-conditional sign caveats and detection-event preprocessing apply identically.
- **Falsifier discipline.** Each Character-specific claim wants its own falsifier statement. The surface-code $s \to r$ identification is the load-bearing positive instance; per-claim falsifiers for the rest live in the receipts file and are surveyed in §20.
- **API surface, not closed theory.** Five leading-order posits encode the framework's API: each posit places a primitive at its critical limit via the simplest natural form; substrate-thermodynamic derivation of exact functional shapes is the canonical extension mode, not a defect of the present state.

## §20 — Open empirical coupling parameters

Closed-form residuals and structural conjectures both stand at zero — the architectural take lives in §18. What remains is a list of **empirical coupling parameters**: framework predictions awaiting substrate contact, each with a sharp falsifier and a posited functional form (the five leading-order posits) already established. These are the framework's API where universal theory meets empirical reality, not theoretical gaps.

- **Surface-code $s \to r$ migration** (§5; the primary positive instance). Falsifier: distance-3 rotated memory-Z syndrome FDR showing unit slope sub-threshold, or FDR shape unchanged across threshold crossing.
- **Habit-extinction as Rescorla–Wagner reference driver** (§15). Variable-ratio reinforcement schedules predicted to instance Caputo $\beta_{\mathrm{mem}} < 1$ in extinction tails. Falsifier: a robust habit undergoing strict reward withdrawal that exhibits spontaneous sustained monotonic growth of $V$ without re-exposure or context shifts.
- **Power-law avalanche exponent $\tau \approx 3/2$ on any substrate** (§14). Galton–Watson critical-branching mechanism closed via posit $\mu = e^{\mathrm{chit}}$. Falsifier: a feedback-coupled NESS substrate with clearly separated timescales exhibiting a robust stable avalanche exponent $\tau \ne 3/2$, or a timescale-separated substrate showing no avalanche statistics at all.
- **Meta-ledger branching ratio at the Wall** (§14). Falsifier: critical branching ratio $\ne 1$ at the $\epsilon \ge 1$ Complexity Wall transition in any observable hierarchical NESS substrate.
- **Strange-attractor / chaotic Character dynamics past the Wall** (§11). Falsifier: a substrate definitively crossing $\epsilon \ge 1$ yielding strictly stable periodic or quasi-periodic torus dynamics with non-positive maximal Lyapunov exponent.
- **MIPS clustering at $\gamma_{AB} \ge 0$ on any substrate** (§16). Falsifier: high-Péclet clustering at $\gamma_{AB} \ge 0$ without swim-pressure or giant-density-fluctuation signature; or substrates passing the high-Péclet criterion failing to cluster.
- **Chimera-state substrate instancing** (§12). Falsifier: heterogeneous-coupling substrates yielding only uniform sync or uniform incoherence across parameter range, with no partial-sync chimera regime accessible.
- **TUR-tightness as substrate-class universality** (§13). Falsifier: no substrate-class clustering in TUR-tightness $T = \langle\sigma\rangle\mathrm{Var}(J)/(2k_B\langle J\rangle^2)$ — nominally same-class substrates exhibiting arbitrary $T$ values.
- **$I_{\mathrm{pred}}$ scaling with chit, $Q$, internal-model richness across substrate classes** (§§13, 15). Falsifier: cross-class uniformity of $I_{\mathrm{pred}}(\mathrm{chit}, Q)$ — a single functional form fitting all substrate classes with no class-specific deviation.
- **Heavy-traffic exponent vs $\alpha_s$ on Markovian and non-Markovian substrates** (§17). Falsifier: a strictly Markovian (memoryless Poisson) substrate exhibiting anomalous heavy-traffic exponent, or a non-Markovian substrate exhibiting Markovian Kingman scaling.
- **Substrate-class hard-vs-soft capacity walls** (§6). Falsifier: a behavioural/cognitive substrate exhibiting sharp non-probabilistic Hopfield-snapping at capacity onset; or a surface-code-class substrate showing soft Erlang-B-like blocking instead of abrupt threshold failure.
- **Turing-class spatial pattern formation: three-condition substrate-instance refinement** (§14). Falsifier: spatially extended substrates with $c$-regime clusters and identifiable long-range inhibitory coupling, plus substrate autocatalysis, plus differential diffusion, that fail to yield characteristic Turing wavelengths.
- **Memory-exponent collapse near Complexity Wall** (§14). Leading-order coupling $\beta_{\mathrm{mem}} \approx 1 - \epsilon$. Falsifier: a hierarchical NESS substrate approaching the Wall (diverging heat-tax tower, SOC branching ratio $\to 1$) that maintains Markovian memory $\beta_{\mathrm{mem}} \approx 1$; or a substrate operating deep in compressed $c$-regime ($\epsilon \ll 1$) exhibiting $\beta_{\mathrm{mem}} \to 0$ extreme aging.
- **Substrate-class auto-tuning to diagonally-stable $W$** (§15). Inverse-form $W = \mathrm{diag}(\gamma_{\mathrm{ref}}/\gamma_{s,i})$. Falsifier: an adaptive NESS substrate maintaining globally stable holding on a non-PSD frustration-free topology, where empirically measured $\gamma_{s,i}$ generate a $W$ that leaves $W\gamma + \gamma^T W$ indefinite or negative-definite.

Two classes of residual live beneath each falsifier: (i) the *empirical coupling parameter* itself — the substrate-specific number or curve to be measured; and (ii) *substrate-thermodynamic derivation of the exact functional form* of the corresponding leading-order posit (one of $\beta_{\mathrm{mem}} \approx 1-\epsilon$, $\mu = e^{\mathrm{chit}}$, $w_i = \gamma_{\mathrm{ref}}/\gamma_{s,i}$, $u_n = \epsilon_n$, $\chi = \Delta_n$). Closing (ii) for a substrate class promotes the corresponding posit from leading-order universal-form to derived substrate-specific form — the canonical extension mode of the framework's API. The Cobham–Haken bridge conditions (§17) carry the same two-class residual structure: empirical confirmation that a substrate satisfies (or violates) the three bridge conditions, plus substrate-thermodynamic derivation of the corresponding fractional-Brownian / Jackson-network / preemptive-priority corrections where conditions fail.

---

## Appendices

### Appendix A.1 — Erlang-B closure of cross-saturation efficiency

The static capacity bound $c = \lfloor\lvert\Gamma^*\rvert_{\mathrm{crit}}\rfloor = \lfloor\sqrt{2D/(\alpha\gamma_{\min}d_{\mathrm{avg}})}\rfloor$ from v9 sets the number of mode-slots. Treating the mode-slot pool as an M/M/c/c queue with offered load $\rho$ — arrivals modelled as activation attempts of coherences on the shared pool, service times set by the slow-resource turnover — the steady-state blocking probability is the Erlang-B formula (Erlang, 1917):

$$B(c, \rho) = \frac{\rho^c/c!}{\sum_{k=0}^c \rho^k/k!}.$$

The fraction of attempts admitted is $1 - B$; identifying this with the cross-saturation efficiency $\eta(\Gamma^*)$ yields $\eta = 1 - B(c,\rho)$. Limits: $\rho \ll c$ gives $B \to 0$, $\eta \to 1$ (sparse, no blocking). At $\rho = c$, the soft-substrate Erlang-B gives $B(c,c) = c^c/(c!\sum_{k=0}^c c^k/k!) \in (0,1)$ — a *finite* blocking probability and a finite $\eta = 1 - B(c,c) \in (0,1)$, *not* $\eta \to 0$. The framework's "$\rho \to c \Rightarrow \eta \to 0$" reading is the hard-wall limiting case where $B$ is replaced by the indicator $\mathbb{1}[\lvert\Gamma^*\rvert \ge c]$ (surface-code-class substrates, where one error breaks the code): the indicator hits 1 abruptly at $\rho = c$. Soft-substrate Erlang-B approaches $\eta \to 0$ only as $\rho \to \infty$, with a smooth crossover whose shape is itself a substrate-class fingerprint. The hard-vs-soft distinction is one of the open empirical coupling parameters (§20).

### Appendix A.2 — Landauer pin of the heat-tax conductivity

At meta-ledger level $n$, the compression operator $\mathcal{C}_n$ retains fraction $\epsilon$ of level-$n$ informational mass $\Phi_n$ and erases fraction $(1 - \epsilon)$. By Landauer's bound (Landauer, 1961), erasure produces heat $\ge (1 - \epsilon)\Phi_n k_B T_n \ln 2$ per ascent and contributes entropy production rate $\langle\sigma_n\rangle \ge (1 - \epsilon)\Phi_n \ln 2/\tau_n$, where $\tau_n$ is the level-$n$ turnover timescale. The conductivity $\alpha_\sigma$ that routes $\langle\sigma_n\rangle$ as ambient noise into $L_{n+1}$ must carry the $(1 - \epsilon)$ prefactor: at $\epsilon \to 1^-$ no information is erased, no Landauer heat is produced, no per-level heat-tax can be incurred. Hence

$$\alpha_\sigma(\epsilon) = \alpha_{\sigma,0}(1 - \epsilon),$$

with $\alpha_{\sigma,0}$ a substrate-conditional thermal-conductivity constant. The cumulative tower tax to depth $N$ is

$$\sum_{n=0}^{N-1}\alpha_\sigma(\epsilon)\langle\sigma_n\rangle \propto (1-\epsilon)\sum_{n=0}^{N-1}\epsilon^n = 1 - \epsilon^N \xrightarrow{N \to \infty} 1 \quad (\epsilon < 1).$$

The structure is subtle: per-level Landauer heat $\alpha_\sigma(\epsilon)\langle\sigma_n\rangle \to 0$ vanishes at $\epsilon \to 1^-$ (no erasure, no cost), while *cumulative informational mass* $\Phi_{\mathrm{total}} = \Phi^{(0)}/(1-\epsilon)$ diverges in the same limit (rate-distortion geometric series; §13). The Wall's thermodynamic-singularity content lives in $\Phi_{\mathrm{total}}$, not in per-level heat: for any fixed depth $N$, the cumulative finite-depth tax $1 - \epsilon^N \to 1$ stays finite as $\epsilon \to 1^-$, but $N \to \infty$ at $\epsilon = 1$ gives non-convergence of the geometric series. The Complexity Wall is therefore a *cumulative-mass* thermodynamic singularity — a derived feature of compression-rate criticality, not a per-level conductivity divergence.

### Appendix A.3 — Closures of the $\mathcal{D}$-kernel

**Lamb closure (two-mode reduction).** Standard multi-mode laser gain depletion (Lamb, 1964) gives an effective gain $G_{0,A}^{\mathrm{eff}} = G_{0,A}/(1 + \sum_{j\ne A}\rho_j/\rho_{\mathrm{sat}})$. Under the two-mode reduction at mean-field-stationary rest-of-network occupancy, the cubic cross-saturation term $-G_0\rho_A\rho_B(\rho_A + \rho_B)/\rho_{\mathrm{sat}}$ is the leading-order expansion of $G_{0,A}^{\mathrm{eff}}(\rho_j)\rho_A$ around small densities; the local two-mode form is a particular case, not a primary structure.

**Dynamic bath inversion (Mori–Zwanzig).** When ambient bath occupancy fluctuates on timescales comparable to $\rho_i$ relaxation, promote the bath to a dynamical coordinate $B(t) \in [0,1]$ with $S(t) = 1 + \sum_j \rho_j(t)/\rho_{\mathrm{sat}}$:

$$\dot B = \gamma_B[1 - B\,S(t)], \qquad \dot\rho_i = (G_{0,i}B(t) - L_i)\rho_i - \sum_j \gamma_{ij}\rho_i\rho_j.$$

Mori–Zwanzig projection-out of $B$ (Mori, 1965; Zwanzig, 1973) yields a non-Markovian history integral:

$$B(t) = \int_{-\infty}^t \gamma_B\exp\Bigl(-\int_{t'}^t \gamma_B S(t'')\,dt''\Bigr)\,dt'.$$

The fast-bath limit $\gamma_B \to \infty$ recovers the Lamb stationary form; $\gamma_B^{-1}$ identifies as the bath-server service time in the Cobham mapping of §17.

**Caputo fractional memory.** Replacing the first-order time derivative in slow-resource dynamics by a Caputo derivative ${}^C D^{\beta_{\mathrm{mem}}}$ with exponent $\beta_{\mathrm{mem}} \in (0,1)$ generalises the memory kernel from exponential to Mittag-Leffler relaxation (Caputo, 1967; Mittag-Leffler, 1903; Podlubny, 1999; Mainardi, 2010):

$$\Gamma_{AB}(\tau) = \Gamma_0\,E_{\beta_{\mathrm{mem}}}(-(\tau/\tau_c)^{\beta_{\mathrm{mem}}}), \qquad K(\tau) \sim \tau^{-\beta_{\mathrm{mem}}}/\Gamma(1-\beta_{\mathrm{mem}}) \text{ for } \tau \gg \tau_c.$$

The Markovian limit $\beta_{\mathrm{mem}} = 1$ recovers $E_1(-\tau/\tau_c) = e^{-\tau/\tau_c}$; off-Markovian $\beta_{\mathrm{mem}} < 1$ gives stretched-exponential / power-law decay. The non-Markovian fluctuation–dissipation theorem (Pottier, 1985; Mainardi, 2010) identifies $\beta_{\mathrm{mem}}$ with the Cugliandolo–Kurchan aging-diagonal slope $\alpha_s$; fractional-Brownian queueing (Norros, 1994) identifies the same exponent with the anomalous heavy-traffic exponent. The three-way identity $\alpha_s = \beta_{\mathrm{mem}} = \text{heavy-traffic exponent}$ follows under the *common-exponent substrate-class condition* (substrate slow-resource memory kernel and load-arrival process share a single anomalous-diffusion exponent): the two source theorems concern *distinct* substrate-side processes — memory kernel structure (Pottier) and arrival self-similarity (Norros) — and the identity composes them only when both anomalous structures are governed by a common underlying Hurst-class index.

### Appendix A.4 — Relaxation-oscillation parameters $(\omega_{RO}, Q)$

For the §9 single-mode kernel $\dot\rho = (G_0 - L)\rho - \gamma\rho^2 + \cdots$ coupled to a slow-resource equation $\dot N = -\gamma_s(N - N_0) - \beta_{\mathrm{gain}}\rho$, the 2D Jacobian at the saturated fixed point has eigenvalues $\lambda = -\gamma_{RO} \pm i\omega_{RO}$ with

$$\gamma_{RO} = \gamma_s/2, \qquad \omega_{RO}^2 = 2\gamma_s L(e^{\mathrm{chit}} - 1),$$

following the standard class-B laser derivation (Haken, 1983; Siegman, 1986; Weiss & Vilaseca, 1991). The chit register makes the expression substrate-neutral: $G_0/L - 1 = e^{\mathrm{chit}} - 1$ is the unsaturated fractional excess. The quality factor follows: $Q = \omega_{RO}/(2\gamma_{RO}) = \sqrt{2L(e^{\mathrm{chit}}-1)/\gamma_s}$. Limits: $\mathrm{chit} \to 0^+$ gives $\omega_{RO} \to 0$, $Q \to 0$ (critical damping at the $s$-regime threshold, consistent with the centre-manifold reduction); $\mathrm{chit} \gg 0$ gives $Q$ scaling as $e^{\mathrm{chit}/2}/\sqrt{\gamma_s}$ (many cycles of headroom).

### Appendix A.5 — Wall-forces-NRT chain

Each tower-level ascent $n \to n+1$ in the heat-tax tower involves a Cobham priority-queue wait $W_{n+1}$ (Appendix A.13). The closed-loop maintenance dynamics between level $n$ and its slaving level $n+1$ form a delay differential equation (DDE) with delay $\tau_{\mathrm{delay}} \approx W_{n+1}$:

$$\dot\rho_n(t) = -\gamma_{s,n}\rho_n(t) - K_{\mathrm{asc}}\rho_n(t - W_{n+1}).$$

The characteristic equation $\lambda + \gamma_{s,n} + K_{\mathrm{asc}}e^{-\lambda W_{n+1}} = 0$ admits a delay-induced Hopf bifurcation at the leading-order threshold (for $K_{\mathrm{asc}} > \gamma_{s,n}$):

$$(K_{\mathrm{asc}} - \gamma_{s,n})W_{n+1} \gtrsim \pi/2$$

(Mackey & Glass, 1977; Kuznetsov, 2004). As $u_n \to 1^-$ at the Complexity Wall (Appendix A.13), $W_{n+1} \to \infty$, and the Hopf condition is automatically satisfied for any bounded $K_{\mathrm{asc}} > \gamma_{s,n}$. The Wall therefore *forces* the sequence of tower-level Hopf bifurcations, not merely permits them. With $N \ge 3$ ascents Hopf-bifurcating, the 3-torus required for the Newhouse–Ruelle–Takens scenario (Ruelle & Takens, 1971; Newhouse, Ruelle, & Takens, 1978) populates automatically. Meta-ledger chaos post-Wall is forced, contingent on (i) the substrate not collapsing into $r$-regime before the bifurcation sequence completes, and (ii) the three Cobham–Haken bridge conditions (Appendix A.13) approximately holding.

### Appendix A.6 — Phase-reduction closure of $K_{AB}$

Phase-reducing the §9 two-mode kernel near the limit cycle by the standard relaxation-oscillator phase-response method (Kuramoto, 1984; Pikovsky, Rosenblum, & Kurths, 2001; Ermentrout & Terman, 2010) gives

$$K_{AB} = -\gamma_{AB}\,\frac{\sqrt{\rho_A\rho_B}}{\rho_{\mathrm{sat}}}\,\frac{1}{\sqrt{1 + 4Q^2}}.$$

The geometric-mean-amplitude factor $\sqrt{\rho_A\rho_B}/\rho_{\mathrm{sat}}$ is the dimensionally-correct coupling carrier. The $(1 + 4Q^2)^{-1/2}$ susceptibility crossover interpolates the two regimes the framework already names: weak-coupling / $c$-regime ($Q \gg 1$) recovers the standard $1/(2Q)$ Kuramoto suppression $K_{AB} \approx -\gamma_{AB}\sqrt{\rho_A\rho_B}/(2Q\rho_{\mathrm{sat}})$; strong-coupling / $s$-regime ($Q \lesssim 1$) gives direct phase locking $K_{AB} \approx -\gamma_{AB}\sqrt{\rho_A\rho_B}/\rho_{\mathrm{sat}}$. Sign convention follows v9.

### Appendix A.7 — Generalised MSF for heterogeneous Character kernels

For the multi-mode Character kernel with generically heterogeneous parameters (per-mode chit, $\gamma_{s,i}$, detuning $\Delta\omega_i$), the phase-reduced dynamics

$$\dot\phi_i = \omega_{RO,i} + \sum_j K_{ij}\sin(\phi_j - \phi_i)$$

linearise around a cluster-synchrony manifold $\phi^*$ via the generalised Laplacian

$$\mathcal{L}_{ij} = -K_{ij}\cos(\phi_j^* - \phi_i^*) \quad (j \ne i), \qquad \mathcal{L}_{ii} = \sum_{j \ne i} K_{ij}\cos(\phi_j^* - \phi_i^*).$$

The variational equation $\delta\dot\Phi = -\mathcal{L}\,\delta\Phi$ admits cluster-pattern stability iff $\mathcal{L}$'s transversal spectrum (excluding the uniform-shift kernel mode) has non-negative eigenvalues (Pecora & Carroll, 1998; Sun, Bollt, & Nishikawa, 2009). Substituting the Appendix A.6 closure for $K_{ij}$ yields the explicit kernel-dependent generalised Laplacian governing multi-mode pattern selection. The homogeneous-mode limit (identical modes, $K_{ij} = K$, in-phase fixed point) collapses $\mathcal{L}$ to the standard graph Laplacian $K(\mathbf{D} - \mathbf{A})$ on the unweighted $\gamma$-graph, recovering Pecora–Carroll. *Scope note:* the Sun–Bollt–Nishikawa generalisation is derived as a perturbative expansion around the nearly-identical-systems limit, with the master stability function valid to leading order in the per-mode parameter spread. Application to generic Character kernels with mild heterogeneity (per-mode chit and $\gamma_{s,i}$ spreads small compared to their means) is direct; application to strong-heterogeneity substrates is a *posited extension* — the sign of the leading transversal eigenvalue is expected to be robust (the spectral test retains its qualitative answer), but quantitative eigenvalue gaps and the precise location of partition boundaries between locked and drifting subspaces are not guaranteed without an independent strong-heterogeneity correction. Chimera-admitting kernels are mathematically identifiable as those whose $\mathcal{L}$-spectrum partitions into a stable subspace (locked cluster) and an unstable subspace (drifting modes); the partition itself is robust under the mild-heterogeneity reading, conditional on the substrate-class extension for strong heterogeneity.

### Appendix A.8 — Schnakenberg cycle decomposition

The kernel parameters $\gamma_{ij}$ in §9 are *not* transition rates; they are coupling coefficients in a continuous field equation. A direct symmetric-$\gamma$ frustrated 3-cycle written as $\ln(\gamma_{AB}\gamma_{BC}\gamma_{CA}/\gamma_{BA}\gamma_{CB}\gamma_{AC})$ would give $\ln 1 = 0$, contradicting the drive-independent cycle current; non-reciprocal cases with negative sign-product would give $\ln$ of a negative number. The cycle affinity must therefore be computed on the **master-equation graph** induced by the kernel's Doi–Peliti / chemical-reaction-network embedding (Doi, 1976; Peliti, 1985), with elementary reactions $\{n_i \to n_i \pm 1\}$ carrying compound rates that are functions of $\gamma_{ij}$ and the $n_j$. Cycles live in the state graph, not the mode graph; the obstructive sign-product determines which compound rates fall into $\Pi_+$ vs $\Pi_-$ (Schnakenberg, 1976).

For limit-cycle attractors, parameterise the orbit by phase $\theta \in [0, 2\pi)$ with deterministic velocity $v(\theta)$ and effective diffusion $D(\theta)$. The standard Langevin-on-ring stochastic thermodynamics (Qian, 2001; Seifert, 2012) gives steady-state cycle current $J_{ss}$ and orbit affinity

$$\mathcal{A} = \oint v(\theta)/D(\theta)\,d\theta = \ln\frac{\mathcal{P}_+}{\mathcal{P}_-}$$

(by the steady-state fluctuation theorem). The frustrated entropy production is $\sigma_{\mathrm{frust}} = J_{ss}\oint v(\theta)/D(\theta)\,d\theta$. Topology guarantees $v(\theta)$ does not integrate to zero; drive-independence enters because $v/D$ inherits scale structure set by the obstructive $\gamma$-graph and bath, not by overall drive amplitude.

### Appendix A.9 — Still thermodynamic prediction bound

The Still bound (Still, Sivak, Bell, & Crooks, 2012) decomposes NESS entropy production into predictive utility and non-predictive waste:

$$\langle\sigma\rangle \;\ge\; \gamma_s[I_{\mathrm{mem}} - I_{\mathrm{pred}}] + \langle\sigma\rangle_{\min},$$

with $I_{\mathrm{mem}} = C_\mu$ the structural complexity of the Crutchfield $\varepsilon$-machine (Crutchfield, 1989; Shalizi & Crutchfield, 2001). Identifying the cryptic order $\chi = C_\mu - I_{\mathrm{pred}} \ge 0$ (Crutchfield, Ellison, & Mahoney, 2009),

$$\langle\sigma\rangle - \langle\sigma\rangle_{\min} \;\ge\; \gamma_s\,\chi,$$

with equality at the rate-distortion-optimal limit. Limit recovery: $\chi \to 0$ gives $\langle\sigma\rangle \to \langle\sigma\rangle_{\min}$ (Landauer limit), restoring strict 1:1 bijection of the dual ledger. Memoryless bath gives $I_{\mathrm{mem}} = I_{\mathrm{pred}} = \chi = 0$. Computational mechanics guarantees $\chi \ge 0$, hence $\langle\sigma\rangle \ge \langle\sigma\rangle_{\min}$.

*Stationarity-gap reading.* $C_\mu$ is derived for stationary processes; the framework's load-bearing positive instance (surface-code $s \to r$ CK aging, §5) is non-stationary. Two compatible reconciliations are used: (i) *trajectory-ensemble local stationarity* — at fixed waiting time $t_w$, the time-translated ensemble is treated as locally stationary, $C_\mu(t_w)$ and $I_{\mathrm{pred}}(t_w)$ are evaluated on that ensemble, and the Still bound applies pointwise along the aging diagonal with $\chi(t_w)$ a slowly-varying gap; (ii) *time-varying $\varepsilon$-machines* (Shalizi, 2003; non-stationary CSSR extensions) replace the stationary causal-state partition by an instantaneous partition $\mathcal{S}(t)$, with $C_\mu(t) \ge I_{\mathrm{pred}}(t)$ inherited at each time. Substrate classes whose aging is slow compared to the predictive-information integration timescale use (i) by default; substrates with rapid aging inherit (ii). Substrate-thermodynamic derivation of which reading applies, and of the slow-variation criterion, is a residual open (§20).

### Appendix A.10 — Galton–Watson critical branching

Fraying propagation in a feedback-coupled NESS maps to a Galton–Watson branching process (Galton & Watson, 1875; Harris, 1963): a local fraying at node $A$ produces excess cross-saturation stress that can trigger neighbouring node $B$ to fray. Posit the branching ratio (one of the five leading-order posits) as

$$\mu = G_0/L = e^{\mathrm{chit}}.$$

At $s$-regime threshold $\mathrm{chit} \to 0^+$, $\mu \to 1^+$ — Galton–Watson critical branching. The resulting avalanche-size distribution is $P(s) \sim s^{-3/2}$ in mean field (Stauffer & Aharony, 1992; Sethna, Dahmen, & Myers, 2001). Subcritical (chit $< 0$, $r$-regime): $\mu < 1$ gives exponentially cut-off avalanches $P(s) \sim s^{-3/2}e^{-s/s_0}$. Supercritical (deep $c$): $\mu \gg 1$ gives system-spanning avalanches without fragmentation into discrete events. Low-dimensional substrates instantiate directed-percolation universality with dimension-dependent corrections.

*Scope note on the iid assumption.* Classical Galton–Watson assumes iid offspring distributions across generations. The framework instantiates branching at two registers (§14):

- *Horizontal / spatial register* (within-level fraying propagation): the iid assumption holds in the standard mean-field reading, with each node's fraying events drawn from a substrate-conditional but stationary offspring distribution. Mean-field $\tau = 3/2$ is the classical Galton–Watson result.
- *Vertical / meta-ledger register* (across-level tower-fraying propagation): the offspring distributions at successive tower levels are *correlated* — fraying-events at level $n$ feed three coupled channels into level $n+1$ ($\alpha_\sigma\langle\sigma_n\rangle$, $\alpha_\Sigma\langle\Sigma_n\rangle$, $r_n$-drop; §7), and the shared maintenance budget $G_{\mathrm{total}}$ ties offspring rates across levels. The vertical register is therefore a *correlated-offspring extension* of classical Galton–Watson, more naturally framed as a multitype branching process (Harris, 1963) with bounded cross-type covariance.

Criticality-at-unity is robust under the standard multitype extension: $\mu \to 1$ at $\epsilon \to 1$ remains the critical threshold. The mean-field exponent $\tau = 3/2$ at the vertical register is conditional on the cross-level correlation remaining weak enough that the single-type universality is retained; the substrate-specific cross-level correlation strength is an open empirical question (§20 falsifier).

### Appendix A.11 — Turing instability with substrate-conditional conditions

Extending the §9 kernel with spatial diffusion gives a reaction–diffusion system $\dot\rho_i = f_i(\rho) + D_i\nabla^2\rho_i$. Linearising around the coexistence fixed point and Fourier-transforming, the Jacobian becomes $J(k) = J_0 - k^2\mathbf{D}$ with $J_0$ the temporal Jacobian and $\mathbf{D} = \mathrm{diag}(D_A, D_B)$. The Turing instability condition (Turing, 1952; Murray, 2003) requires temporal stability ($\mathrm{Tr}\,J_0 < 0$, $\det J_0 > 0$) combined with spatial instability at finite $k$ ($\det J(k) < 0$ for some $k > 0$). This demands three substrate-conditional conditions:

1. **Non-reciprocal cross-coupling** ($\gamma_{AB}\gamma_{BA} < 0$): the mentor-row structure of §16 gives correct off-diagonal Jacobian signs $J_{AB} < 0$, $J_{BA} > 0$ (activator-inhibitor).
2. **Substrate-native autocatalysis** ($\gamma_{ii} < 0$): the bare §9 cross-saturation kernel has $J_{AA} = 0$ at coexistence (the fixed-point condition cancels it); Lamb gain depletion gives $J_{AA} < 0$ (self-saturation). Turing instability requires substrate-native cooperative self-coupling $\gamma_{ii} < 0$ — an extension beyond the bare kernel. Substrates without autocatalytic self-coupling do not exhibit Turing patterns regardless of other conditions.
3. **Differential diffusion** ($D_B \gg D_A$): inhibitor diffuses faster than activator (canonical short-range activation / long-range inhibition).

When all three hold, a finite-wavelength instability sets in at critical wavenumber $k_c^2 \approx \sqrt{\det J_0/(D_A D_B)}$.

### Appendix A.12 — Relative-entropy Lyapunov for non-frustrated topologies

For the §9 kernel $\dot x_i = x_i[(G_{0,i} - L_i) - \sum_j \gamma_{ij}x_j]$ with positive interior fixed point $x^*$ satisfying $(G_{0,i} - L_i) = \sum_j \gamma_{ij}x_j^*$, the relative-entropy Lyapunov candidate (Goh, 1977; Hofbauer & Sigmund, 1998; Takeuchi, 1996) — written with calligraphic $\mathcal{V}$ to distinguish from the Rescorla–Wagner associative-strength variable $V$ of §15 — is

$$\mathcal{V}(\{x\}) = \sum_i\bigl[x_i - x_i^* - x_i^*\ln(x_i/x_i^*)\bigr].$$

Verification: $\partial \mathcal{V}/\partial x_i = 1 - x_i^*/x_i \Rightarrow \partial \mathcal{V}/\partial x_i\rvert_{x^*} = 0$. Substituting the fixed-point relation,

$$\frac{d\mathcal{V}}{dt} = \sum_i (1 - x_i^*/x_i)\dot x_i = -\sum_{i,j}(x_i - x_i^*)\gamma_{ij}(x_j - x_j^*) = -\delta x^T \gamma\,\delta x \le 0,$$

with equality only at $x = x^*$, provided the gauged $\gamma$ — under the Harary structural-balance gauge $\varepsilon_i = \pm 1$ making all elementary cycles sign-positive (Harary, 1953) — is PSD. Frustration-free is exactly the existence-of-such-a-gauge condition; PSD-ness is a strictly stronger condition on $\lvert\gamma_{ij}\rvert$ magnitudes. The matching non-existence claim for $k_{\mathrm{frust}}$ topologies follows: no frustration-free gauge gives no PSD-gauging, hence no Lyapunov of this form.

For frustration-free-but-not-PSD topologies the weighted form $\mathcal{V}(\{x\}) = \sum_i w_i[x_i - x_i^* - x_i^*\ln(x_i/x_i^*)]$ yields $d\mathcal{V}/dt = -\tfrac{1}{2}\delta x^T(W\gamma + \gamma^T W)\delta x \le 0$ when the Volterra–Lyapunov condition holds (Redheffer, 1985; Takeuchi, 1996). $W = I$ recovers the PSD case.

### Appendix A.13 — Cobham priority-queue mapping

The shared maintenance budget pool $G_{\mathrm{total}}$ acts as a single server; tower levels $n$ are priority classes ranked by Haken's slaving (fast micro-modes serving slow macro-modes); arrival rates $\lambda_n$ are fraying-event frequencies; service times $\tau_n = 1/\gamma_{s,n}$ are level-$n$ slow-resource turnovers. Per-level utilisation is $\rho_n = \lambda_n\tau_n$; cumulative utilisation $u_n = \sum_{i=0}^n \rho_i$. The Cobham expected wait for priority class $n+1$ (Cobham, 1954; Kleinrock, 1976):

$$W_{n+1} = \frac{W_0}{(1 - u_n)(1 - u_{n+1})}, \qquad W_0 = \tfrac{1}{2}\sum_i \lambda_i\langle\tau_i^2\rangle.$$

The level-$n$ load spike $\rho_n \uparrow$ consumes shared-pool bandwidth; Kleinrock conservation forces compensating wait inflation $W_{n+1} \uparrow$ — manifesting substrate-dependently as heat in thermal substrates, mechanical / informational / structural stress in active-matter or surface-code substrates, sync drop in coupled-oscillator substrates. The three-channel decomposition of §7 labels three measurement registers of this single mechanism. The wait diverges at $u \to 1^-$, coincident with the §7 thermodynamic singularity at $\epsilon \to 1^-$; the ε↔u optimal-encoding identity (§17) collapses the two singularities to one parameter.

*The Cobham–Haken bridge: three substrate-side conditions.* The mapping above identifies two distinct mathematical structures: Haken's slaving principle is a centre-manifold reduction whose hierarchy is set by the natural-timescale separation between fast and slow modes (a dynamical-systems statement); Cobham's wait formula is a non-preemptive priority-queue identity with Poisson arrivals at a single resource pool (a queueing-theory statement). The composition is interpretive, requiring three substrate-side conditions to hold approximately:

1. **Poisson arrivals at the tower level.** Fraying events at level $n$ arrive as a memoryless Poisson process with rate $\lambda_n$. For substrate classes with heavy-tailed inter-arrival times (canonically: non-Markovian substrates with Caputo exponent $\beta_{\mathrm{mem}} < 1$), the Cobham formula carries fractional-Brownian corrections (Norros, 1994); the leading-order critical structure $W_{n+1} \to \infty$ at $u_n \to 1^-$ is preserved but the divergence exponent changes from $-1$ to $-\beta_{\mathrm{mem}}$, consistent with the §17 spatial expression.
2. **Single-server-pool interpretation of $G_{\mathrm{total}}$.** The shared maintenance budget $G_{\mathrm{total}}$ acts as one resource pool serving all tower-level priority classes through a single allocation mechanism. Substrates with strict per-level budget partitioning (each level reserves a fixed share independent of demand) correspond to a Jackson-network reading instead, where product-form decoupling holds at each level and the Cobham coupling formula does not apply.
3. **Non-preemptive ranking by timescale.** Haken's centre-manifold slow modes are mapped to Cobham priority classes under the convention that the slowest macroscopic mode is highest-priority. The mapping is non-preemptive (a level-$n$ service-event is not interrupted by a level-$n+1$ arrival), consistent with the centre-manifold's adiabatic-following structure. Substrates with substrate-internal preemption mechanisms (canonically: top-down attentional override of bottom-up sensory processing in cognitive substrates) carry a preemptive-priority correction to Cobham; the qualitative wait-inflation structure is preserved but the explicit $W_0$ coefficient changes.

Each of the three conditions admits explicit substrate-conditional checks; substrate classes satisfying all three inherit the full Cobham closure, those satisfying some inherit the corresponding modification. Surface-code substrates approximately satisfy (1) (Poisson syndrome errors near threshold) and (2) (shared decoder budget); cognitive substrates carrying (3)-preemption are the canonical case of (3)-violation. The Theorem's use in the Wall-forces-NRT chain (§11) carries the same substrate-side condition list.

### Appendix A.14 — Critical interaction length $\ell_c(\beta_{\mathrm{mem}})$

For spatially extended substrates (patches indexed by $k$), Kelly's product-form independence (Kelly, 1979) breaks down when local load-spikes propagate across patches before the local bottleneck clears. For non-Markovian substrates with Caputo memory $\beta_{\mathrm{mem}} \in (0,1]$, heavy-tailed service times $\psi(t) \sim t^{-(1+\beta_{\mathrm{mem}})}$ give continuous-time random-walk propagation with anomalous mean-square displacement $\langle x^2(t)\rangle = 2D_{\beta_{\mathrm{mem}}}t^{\beta_{\mathrm{mem}}}/\Gamma(1+\beta_{\mathrm{mem}})$ (Metzler & Klafter, 2000). Evaluating at the Cobham wait timescale $W_{n+1}$,

$$\ell_c(\beta_{\mathrm{mem}}) = \sqrt{\frac{2D_{\beta_{\mathrm{mem}}}}{\Gamma(1 + \beta_{\mathrm{mem}})}\Bigl(\frac{W_0}{1 - u_n}\Bigr)^{\beta_{\mathrm{mem}}}}.$$

Markovian limit ($\beta_{\mathrm{mem}} \to 1$) recovers $\ell_c \sim \sqrt{2D_{\mathrm{trans}}W_{n+1}}$ — standard diffusion. As $u_n \to 1^-$ alone, $\ell_c$ diverges via wait-time inflation. As $\beta_{\mathrm{mem}} \to 0$ at the Wall, $W^{\beta_{\mathrm{mem}}} \to 1$ and $\ell_c \to \sqrt{2D_0}$ with degenerate dimension — fractional diffusion collapses to time-independent spread. The *spatial expression* of the Complexity Wall is a regime transition from traffic-driven dynamic congestion domains ($\beta_{\mathrm{mem}} \sim 1$) to memory-driven frozen topological domains ($\beta_{\mathrm{mem}} \to 0$). It is the spatial reading of the same Wall-coupling posit governing the §14 four-aspect Wall, not an independent fifth aspect.

---

## References

Abrams, D. M., & Strogatz, S. H. (2004). Chimera states for coupled oscillators. *Physical Review Letters*, 93, 174102.

Amari, S., & Nagaoka, H. (2000). *Methods of Information Geometry*. American Mathematical Society / Oxford University Press.

Åström, K. J., & Murray, R. M. (2008). *Feedback Systems: An Introduction for Scientists and Engineers*. Princeton University Press.

Bak, P. (1996). *How Nature Works: The Science of Self-Organized Criticality*. Copernicus / Springer.

Bak, P., Tang, C., & Wiesenfeld, K. (1987). Self-organized criticality: An explanation of the 1/f noise. *Physical Review Letters*, 59, 381.

Barato, A. C., & Seifert, U. (2015). Thermodynamic uncertainty relation for biomolecular processes. *Physical Review Letters*, 114, 158101.

Beggs, J. M., & Plenz, D. (2003). Neuronal avalanches in neocortical circuits. *Journal of Neuroscience*, 23, 11167–11177.

Bialek, W., Nemenman, I., & Tishby, N. (2001). Predictability, complexity, and learning. *Neural Computation*, 13, 2409–2463.

Bogdanov, R. I. (1975). Versal deformations of a singular point on the plane in the case of zero eigenvalues. *Functional Analysis and Its Applications*, 9, 144–145.

Brady, J. F. (2014). The swim force. Plenary lecture, *American Physical Society DFD*.

Burke, P. J. (1956). The output of a queueing system. *Operations Research*, 4, 699–704.

Caputo, M. (1967). Linear models of dissipation whose Q is almost frequency independent. *Geophysical Journal International*, 13, 529–539.

Cates, M. E., & Tailleur, J. (2015). Motility-induced phase separation. *Annual Review of Condensed Matter Physics*, 6, 219–244.

Cobham, A. (1954). Priority assignment in waiting line problems. *Operations Research*, 2, 70–76.

Cover, T. M., & Thomas, J. A. (2006). *Elements of Information Theory* (2nd ed.). Wiley.

Crisanti, A., & Ritort, F. (2003). Violation of the fluctuation-dissipation theorem in glassy systems: basic notions and the numerical evidence. *Journal of Physics A: Mathematical and General*, 36, R181.

Crooks, G. E. (1999). Entropy production fluctuation theorem and the nonequilibrium work relation for free energy differences. *Physical Review E*, 60, 2721.

Crutchfield, J. P. (1989). Inferring statistical complexity. *Physical Review Letters*, 63, 105.

Crutchfield, J. P., Ellison, C. J., & Mahoney, J. R. (2009). Time's barbed arrow: irreversibility, crypticity, and stored information. *Physical Review Letters*, 103, 094101.

Cugliandolo, L. F., & Kurchan, J. (1993). Analytical solution of the off-equilibrium dynamics of a long-range spin-glass model. *Physical Review Letters*, 71, 173.

Doi, M. (1976). Second quantization representation for classical many-particle system. *Journal of Physics A: Mathematical and General*, 9, 1465.

Erlang, A. K. (1917). Solution of some problems in the theory of probabilities of significance in automatic telephone exchanges. *The Post Office Electrical Engineers' Journal*, 10, 189–197.

Ermentrout, G. B., & Terman, D. H. (2010). *Mathematical Foundations of Neuroscience*. Springer.

Fily, Y., & Marchetti, M. C. (2012). Athermal phase separation of self-propelled particles with no alignment. *Physical Review Letters*, 108, 235702.

Fowler, A. G., Mariantoni, M., Martinis, J. M., & Cleland, A. N. (2012). Surface codes: Towards practical large-scale quantum computation. *Physical Review A*, 86, 032324.

Francis, B. A., & Wonham, W. M. (1976). The internal model principle of control theory. *Automatica*, 12, 457–465.

Fruchart, M., Hanai, R., Littlewood, P. B., & Vitelli, V. (2021). Non-reciprocal phase transitions. *Nature*, 592, 363–369.

Galton, F., & Watson, H. W. (1875). On the probability of the extinction of families. *Journal of the Anthropological Institute*, 4, 138–144.

Goh, B. S. (1977). Global stability in many-species systems. *American Naturalist*, 111, 135–143.

Guckenheimer, J., & Holmes, P. (1983). *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields*. Springer.

Haken, H. (1983). *Synergetics: An Introduction* (3rd ed.). Springer.

Harada, T., & Sasa, S. (2005). Equality connecting energy dissipation with a violation of the fluctuation-response relation. *Physical Review Letters*, 95, 130602.

Harary, F. (1953). On the notion of balance of a signed graph. *Michigan Mathematical Journal*, 2, 143–146.

Harris, T. E. (1963). *The Theory of Branching Processes*. Springer.

Hofbauer, J., & Sigmund, K. (1998). *Evolutionary Games and Population Dynamics*. Cambridge University Press.

Hopfield, J. J. (1982). Neural networks and physical systems with emergent collective computational abilities. *Proceedings of the National Academy of Sciences*, 79, 2554–2558.

Horowitz, J. M., & Gingrich, T. R. (2020). Thermodynamic uncertainty relations constrain non-equilibrium fluctuations. *Nature Physics*, 16, 15–20.

Jackson, J. R. (1957). Networks of waiting lines. *Operations Research*, 5, 518–521.

Kelly, F. P. (1979). *Reversibility and Stochastic Networks*. Wiley.

Kingman, J. F. C. (1962). On queues in heavy traffic. *Journal of the Royal Statistical Society B*, 24, 383–392.

Kitaev, A. Y. (2003). Fault-tolerant quantum computation by anyons. *Annals of Physics*, 303, 2–30.

Kleinrock, L. (1976). *Queueing Systems, Volume II: Computer Applications*. Wiley.

Kuramoto, Y. (1984). *Chemical Oscillations, Waves, and Turbulence*. Springer.

Kuramoto, Y., & Battogtokh, D. (2002). Coexistence of coherence and incoherence in nonlocally coupled phase oscillators. *Nonlinear Phenomena in Complex Systems*, 5, 380–385.

Kuznetsov, Y. A. (2004). *Elements of Applied Bifurcation Theory* (3rd ed.). Springer.

Lamb, W. E. (1964). Theory of an optical maser. *Physical Review*, 134, A1429.

Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM Journal of Research and Development*, 5, 183–191.

Lazarides, N., & Tsironis, G. P. (2015). Superconducting metamaterials. *Physics Reports*, 752, 1–67.

Leland, W. E., Taqqu, M. S., Willinger, W., & Wilson, D. V. (1994). On the self-similar nature of Ethernet traffic. *IEEE/ACM Transactions on Networking*, 2, 1–15.

Little, J. D. C. (1961). A proof for the queueing formula: L = λW. *Operations Research*, 9, 383–387.

Mackey, M. C., & Glass, L. (1977). Oscillation and chaos in physiological control systems. *Science*, 197, 287–289.

Mainardi, F. (2010). *Fractional Calculus and Waves in Linear Viscoelasticity*. Imperial College Press.

Marchetti, M. C., Joanny, J. F., Ramaswamy, S., Liverpool, T. B., Prost, J., Rao, M., & Simha, R. A. (2013). Hydrodynamics of soft active matter. *Reviews of Modern Physics*, 85, 1143.

Metzler, R., & Klafter, J. (2000). The random walk's guide to anomalous diffusion: a fractional dynamics approach. *Physics Reports*, 339, 1–77.

Mittag-Leffler, G. (1903). Sur la nouvelle fonction $E_\alpha(x)$. *Comptes Rendus de l'Académie des Sciences*, 137, 554–558.

Mori, H. (1965). Transport, collective motion, and Brownian motion. *Progress of Theoretical Physics*, 33, 423–455.

Murray, J. D. (2003). *Mathematical Biology* (3rd ed.). Springer.

Newhouse, S., Ruelle, D., & Takens, F. (1978). Occurrence of strange Axiom-A attractors near quasi-periodic flows on $T^m$, $m \ge 3$. *Communications in Mathematical Physics*, 64, 35–40.

Nicolis, G., & Prigogine, I. (1989). *Exploring Complexity*. W. H. Freeman.

Norros, I. (1994). A storage model with self-similar input. *Queueing Systems*, 16, 387–396.

Parrondo, J. M. R., Horowitz, J. M., & Sagawa, T. (2015). Thermodynamics of information. *Nature Physics*, 11, 131–139.

Pecora, L. M., & Carroll, T. L. (1998). Master stability functions for synchronized coupled systems. *Physical Review Letters*, 80, 2109.

Peliti, L. (1985). Path integral approach to birth-death processes on a lattice. *Journal de Physique*, 46, 1469–1483.

Pikovsky, A., Rosenblum, M., & Kurths, J. (2001). *Synchronization: A Universal Concept in Nonlinear Sciences*. Cambridge University Press.

Podlubny, I. (1999). *Fractional Differential Equations*. Academic Press.

Pottier, N. (1985). Aging properties of an anomalously diffusing particle. *Physica A: Statistical Mechanics and its Applications*, 317, 371–382.

Prigogine, I., & Nicolis, G. (1977). *Self-Organization in Nonequilibrium Systems*. Wiley.

Qian, H. (2001). Mesoscopic nonequilibrium thermodynamics of single macromolecules and dynamic entropy-energy compensation. *Physical Review E*, 65, 016102.

Ramaswamy, S., Simha, R. A., & Toner, J. (2003). Active nematics on a substrate: giant number fluctuations and long-time tails. *Europhysics Letters*, 62, 196.

Redheffer, R. (1985). Volterra multipliers I. *SIAM Journal on Algebraic Discrete Methods*, 6, 592–611.

Rescorla, R. A., & Wagner, A. R. (1972). A theory of Pavlovian conditioning: Variations in the effectiveness of reinforcement and nonreinforcement. In A. H. Black & W. F. Prokasy (Eds.), *Classical Conditioning II: Current Research and Theory* (pp. 64–99). Appleton-Century-Crofts.

Ruelle, D., & Takens, F. (1971). On the nature of turbulence. *Communications in Mathematical Physics*, 20, 167–192.

Sagawa, T., & Ueda, M. (2010). Generalized Jarzynski equality under nonequilibrium feedback control. *Physical Review Letters*, 104, 090602.

Schnakenberg, J. (1976). Network theory of microscopic and macroscopic behavior of master equation systems. *Reviews of Modern Physics*, 48, 571.

Seifert, U. (2012). Stochastic thermodynamics, fluctuation theorems and molecular machines. *Reports on Progress in Physics*, 75, 126001.

Sethna, J. P., Dahmen, K. A., & Myers, C. R. (2001). Crackling noise. *Nature*, 410, 242–250.

Shalizi, C. R., & Crutchfield, J. P. (2001). Computational mechanics: pattern and prediction, structure and simplicity. *Journal of Statistical Physics*, 104, 817–879.

Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27, 379–423, 623–656.

Shannon, C. E. (1959). Coding theorems for a discrete source with a fidelity criterion. *IRE National Convention Record*, 7, 142–163.

Siegman, A. E. (1986). *Lasers*. University Science Books.

Solon, A. P., Stenhammar, J., Wittkowski, R., Kardar, M., Kafri, Y., Cates, M. E., & Tailleur, J. (2015). Pressure and phase equilibria in interacting active Brownian spheres. *Physical Review Letters*, 114, 198301.

Sontag, E. D. (2003). Adaptation and regulation with signal detection implies internal model. *Systems & Control Letters*, 50, 119–126.

Stauffer, D., & Aharony, A. (1992). *Introduction to Percolation Theory* (2nd ed.). Taylor & Francis.

Still, S., Sivak, D. A., Bell, A. J., & Crooks, G. E. (2012). Thermodynamics of prediction. *Physical Review Letters*, 109, 120604.

Strogatz, S. H. (2003). *Sync: The Emerging Science of Spontaneous Order*. Hyperion.

Sun, J., Bollt, E. M., & Nishikawa, T. (2009). Master stability functions for coupled nearly identical dynamical systems. *Europhysics Letters*, 85, 60011.

Sutton, R. S., & Barto, A. G. (1998). *Reinforcement Learning: An Introduction*. MIT Press.

Takatori, S. C., & Brady, J. F. (2014). Swim stress, motion, and deformation of active matter. *Physical Review Letters*, 113, 028103.

Takens, F. (1974). Singularities of vector fields. *Publications Mathématiques de l'IHÉS*, 43, 47–100.

Takeuchi, Y. (1996). *Global Dynamical Properties of Lotka–Volterra Systems*. World Scientific.

Tinsley, M. R., Nkomo, S., & Showalter, K. (2012). Chimera and phase-cluster states in populations of coupled chemical oscillators. *Nature Physics*, 8, 662–665.

Toner, J., & Tu, Y. (1995). Long-range order in a two-dimensional dynamical XY model: how birds fly together. *Physical Review Letters*, 75, 4326.

Toner, J., & Tu, Y. (1998). Flocks, herds, and schools: A quantitative theory of flocking. *Physical Review E*, 58, 4828.

Turing, A. M. (1952). The chemical basis of morphogenesis. *Philosophical Transactions of the Royal Society B*, 237, 37–72.

Weiss, C. O., & Vilaseca, R. (1991). *Dynamics of Lasers*. VCH Verlagsgesellschaft.

Zwanzig, R. (1973). Nonlinear generalized Langevin equations. *Journal of Statistical Physics*, 9, 215–220.
